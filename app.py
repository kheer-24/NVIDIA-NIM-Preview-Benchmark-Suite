"""
app.py
Local Web Server & Visualizer for NVIDIA NIM 45 Preview Models Benchmark.
Supports Start, Stop, and Restart controls.
Serves localhost webview on http://localhost:8000 and auto-opens default browser.
"""

import os
import sys
import json
import threading
import webbrowser
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
RESULTS_FILE = BASE_DIR / "results.json"
MODELS_FILE = BASE_DIR / "models.json"

load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)

import benchmark

# Benchmark runner state
BENCHMARK_LOCK = threading.Lock()
IS_RUNNING = False
CURRENT_MODEL = None

def set_current_model(model_name):
    global CURRENT_MODEL
    CURRENT_MODEL = model_name

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class BenchmarkRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        global IS_RUNNING, CURRENT_MODEL
        path = self.path.split("?")[0]

        # Root route serves index.html
        if path == "/" or path == "/index.html":
            self.serve_file(STATIC_DIR / "index.html", "text/html")
            return

        # Direct access to models.json and results.json
        if path == "/models.json":
            self.serve_file(MODELS_FILE, "application/json")
            return

        if path == "/results.json":
            if not RESULTS_FILE.exists():
                self.send_json_response([])
                return
            self.serve_file(RESULTS_FILE, "application/json")
            return

        # Status endpoint
        if path == "/api/status":
            load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)
            env_key = os.getenv("NVIDIA_API_KEY", "").strip()
            has_key = bool(env_key and env_key.startswith("nvapi-"))
            masked = (env_key[:8] + "..." + env_key[-4:]) if has_key else None

            # Count completed models
            completed_count = 0
            if RESULTS_FILE.exists():
                try:
                    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        completed_count = len(data)
                except Exception:
                    completed_count = 0

            # Count total models
            total_models = 45
            if MODELS_FILE.exists():
                try:
                    with open(MODELS_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        total_models = len(data)
                except Exception:
                    total_models = 45

            self.send_json_response({
                "status": "online",
                "is_running": IS_RUNNING,
                "current_model": CURRENT_MODEL,
                "completed": completed_count,
                "total": total_models,
                "has_env_key": has_key,
                "masked_key": masked
            })
            return

        # Static assets
        static_file = STATIC_DIR / path.lstrip("/")
        if static_file.exists() and static_file.is_file():
            mime = "text/css" if path.endswith(".css") else ("application/javascript" if path.endswith(".js") else "text/html")
            self.serve_file(static_file, mime)
            return

        super().do_GET()

    def do_POST(self):
        global IS_RUNNING, CURRENT_MODEL
        path = self.path.split("?")[0]

        # Start benchmark
        if path == "/api/benchmark/start":
            with BENCHMARK_LOCK:
                if IS_RUNNING:
                    self.send_json_response({"success": False, "message": "Benchmark is already running"}, 400)
                    return

                restart = False
                content_len = int(self.headers.get("Content-Length", 0))
                if content_len > 0:
                    try:
                        body = json.loads(self.rfile.read(content_len).decode("utf-8"))
                        restart = body.get("restart", False)
                    except Exception:
                        pass

                def worker():
                    global IS_RUNNING, CURRENT_MODEL
                    IS_RUNNING = True
                    try:
                        benchmark.run_all(restart=restart, current_model_callback=set_current_model)
                    finally:
                        IS_RUNNING = False
                        CURRENT_MODEL = None

                t = threading.Thread(target=worker, daemon=True)
                t.start()

                self.send_json_response({"success": True, "message": "Benchmark started"})
                return

        # Stop benchmark
        if path == "/api/benchmark/stop":
            with BENCHMARK_LOCK:
                benchmark.request_stop()
                IS_RUNNING = False
                CURRENT_MODEL = None
                self.send_json_response({"success": True, "message": "Stop signal sent"})
                return

        self.send_response(404)
        self.end_headers()

    def send_json_response(self, data, status=200):
        content = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def serve_file(self, filepath: Path, mime_type: str):
        if not filepath.exists():
            self.send_response(404)
            self.end_headers()
            return
        with open(filepath, "rb") as f:
            content = f.read()
        self.send_response(200)
        self.send_header("Content-Type", mime_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        pass

def main():
    parser = argparse.ArgumentParser(description="NVIDIA NIM 45 Preview Benchmark Server")
    parser.add_argument("--host", default="127.0.0.1", help="Host address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), BenchmarkRequestHandler)
    url = f"http://localhost:{args.port}"

    print("=" * 65)
    print("  NVIDIA NIM 45 PREVIEW MODELS SPEED BENCHMARK")
    print("=" * 65)
    print(f"  [+] Webview URL:    {url}")
    print(f"  [+] Models catalog: 45 preview models loaded from models.json")
    print(f"  [+] Results file:   results.json (persisted)")
    print(f"  [+] API Key file:   .env (set NVIDIA_API_KEY=nvapi-...)")
    print("=" * 65)

    if not args.no_browser:
        try:
            print("  Opening default web browser...")
            webbrowser.open(url)
        except Exception as e:
            print(f"  Browser open error: {e}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == "__main__":
    main()
