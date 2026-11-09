"""
benchmark.py
NVIDIA NIM 45 Preview Models Speed & Performance Benchmark.
Supports graceful start, stop, resume, and restart.
Saves progress incrementally to results.json after every model.
"""

import os
import json
import time
import sys
import threading
import argparse
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Safe console output encoding
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)

MODELS_FILE = BASE_DIR / "models.json"
RESULTS_FILE = BASE_DIR / "results.json"
BASE_URL = "https://integrate.api.nvidia.com/v1"
DEFAULT_PROMPT = "What is the difference between latency and throughput in large language models? Answer in two concise sentences."
RATE_LIMIT_WAIT = 6    # seconds between calls to respect rate limits
REQUEST_TIMEOUT = 45   # timeout for hung models

# Global stop event for graceful cancellation
STOP_EVENT = threading.Event()

def request_stop():
    """Signal benchmark loop to stop gracefully."""
    STOP_EVENT.set()

def reset_stop():
    """Reset stop signal before starting a new run."""
    STOP_EVENT.clear()

def is_stop_requested():
    return STOP_EVENT.is_set()

def get_api_key():
    load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)
    return os.getenv("NVIDIA_API_KEY", "").strip()

def load_models():
    with open(MODELS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_results():
    if not RESULTS_FILE.exists():
        return []
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_results(results):
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

def benchmark_single_model(client, model_id, label, prompt=DEFAULT_PROMPT):
    print(f"\n[>>] Testing {label} ({model_id})...")
    start = time.perf_counter()
    first_token_time = None
    token_count = 0
    full_text = ""

    try:
        # Check if embedding model
        if "embed" in model_id.lower():
            emb_resp = client.embeddings.create(
                model=model_id,
                input=[prompt],
                extra_body={"input_type": "query"} if "nvidia" in model_id else None
            )
            elapsed = time.perf_counter() - start
            tokens = getattr(emb_resp.usage, "total_tokens", 10) if hasattr(emb_resp, "usage") else 10
            tps = round(tokens / max(elapsed, 0.001), 2)
            print(f"   [Embedding] {tokens} tokens in {elapsed:.2f}s = {tps} tok/s")
            return {
                "id": model_id,
                "label": label,
                "status": "ok",
                "total_time_s": round(elapsed, 3),
                "tokens": tokens,
                "tokens_per_second": tps,
                "ttft_s": round(elapsed, 3),
                "cost_nvidia": "$0.00 (Preview Free Tier)",
                "cost_commercial_est": f"${(tokens / 1_000_000 * 0.10):.6f}",
                "response_preview": "[Embedding Vector Generated]",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

        # Standard streaming completion
        stream = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=256,
            stream=True
        )

        for chunk in stream:
            if is_stop_requested():
                break
            if not getattr(chunk, "choices", None):
                continue
            delta = chunk.choices[0].delta if chunk.choices else None
            if delta and getattr(delta, "content", None):
                if first_token_time is None:
                    first_token_time = time.perf_counter()
                full_text += delta.content
                token_count += 1
                sys.stdout.write(".")
                sys.stdout.flush()

        elapsed = time.perf_counter() - start
        ttft = (first_token_time - start) if first_token_time else elapsed
        gen_duration = (time.perf_counter() - first_token_time) if first_token_time else elapsed

        if gen_duration > 0.001 and token_count > 1:
            tps = round((token_count - 1) / gen_duration, 2)
        else:
            tps = round(token_count / max(elapsed, 0.001), 2)

        est_commercial = round((token_count / 1_000_000.0) * 0.80, 6)
        print(f"\n   [OK] {token_count} tokens | TTFT: {ttft*1000:.0f}ms | Speed: {tps} tok/s")

        return {
            "id": model_id,
            "label": label,
            "status": "ok",
            "total_time_s": round(elapsed, 3),
            "tokens": token_count,
            "tokens_per_second": tps,
            "ttft_s": round(ttft, 3),
            "cost_nvidia": "$0.00 (Preview Free Tier)",
            "cost_commercial_est": f"${est_commercial:.6f}",
            "response_preview": full_text[:200] if full_text else "[Complete]",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        msg = str(e)
        elapsed = time.perf_counter() - start
        print(f"\n   [ERR] Error: {msg[:100]}")
        return {
            "id": model_id,
            "label": label,
            "status": "error",
            "error": msg[:200],
            "total_time_s": round(elapsed, 3),
            "tokens": 0,
            "tokens_per_second": 0,
            "ttft_s": None,
            "cost_nvidia": "$0.00",
            "cost_commercial_est": "$0.00",
            "response_preview": f"Error: {msg[:120]}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

def run_all(restart=False, single_model=None, current_model_callback=None):
    reset_stop()
    api_key = get_api_key()
    if not api_key:
        print("\n[!] Error: NVIDIA_API_KEY is not set in .env")
        print("Please open .env and set: NVIDIA_API_KEY=nvapi-your-key-here\n")
        return False

    client = OpenAI(base_url=BASE_URL, api_key=api_key, timeout=REQUEST_TIMEOUT)
    models = load_models()

    if restart and RESULTS_FILE.exists():
        RESULTS_FILE.unlink()
        print("[*] Restarting: Deleted previous results.json")

    results = load_results()
    done_ids = {r["id"] for r in results}

    if single_model:
        target = next((m for m in models if m["id"] == single_model), None)
        if not target:
            target = {"id": single_model, "label": single_model}
        if current_model_callback:
            current_model_callback(target["label"])
        res = benchmark_single_model(client, target["id"], target["label"])
        existing_idx = next((i for i, r in enumerate(results) if r["id"] == target["id"]), None)
        if existing_idx is not None:
            results[existing_idx] = res
        else:
            results.append(res)
        save_results(results)
        return True

    print(f"\nNVIDIA NIM Benchmark: {len(models)} preview models queued")
    print(f"Already completed: {len(done_ids)} | Remaining: {len(models) - len(done_ids)}")

    for m in models:
        if is_stop_requested():
            print("\n[!] Benchmark stopped by user request.")
            break

        mid = m["id"]
        if mid in done_ids:
            print(f"[Skip] (done): {m['label']}")
            continue

        if current_model_callback:
            current_model_callback(m["label"])

        res = benchmark_single_model(client, mid, m["label"])
        results.append(res)
        save_results(results)

        # Interruptible sleep interval
        wait_seconds = RATE_LIMIT_WAIT * 2 if (res.get("status") == "error" and "429" in res.get("error", "")) else RATE_LIMIT_WAIT
        for _ in range(int(wait_seconds * 2)):
            if is_stop_requested():
                break
            time.sleep(0.5)

    if current_model_callback:
        current_model_callback(None)

    if is_stop_requested():
        print(f"\n[!] Stopped. Progress saved to {RESULTS_FILE}")
    else:
        print(f"\nAll benchmarks finished! Results saved to {RESULTS_FILE}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NVIDIA NIM 45 Preview Models Speed Benchmark")
    parser.add_argument("--restart", action="store_true", help="Delete results.json and start from scratch")
    parser.add_argument("--resume", action="store_true", help="Continue from last completed model (default)")
    parser.add_argument("--model", type=str, default=None, help="Benchmark only a specific model ID")
    args = parser.parse_args()

    run_all(restart=args.restart, single_model=args.model)
