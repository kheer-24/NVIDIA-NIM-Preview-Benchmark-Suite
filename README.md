# NVIDIA NIM Preview Benchmark Suite

A benchmarking dashboard for all 45 free preview endpoint models on NVIDIA NIM.
Measures **Tokens / Second**, **Time to First Token (TTFT)**, **End-to-End Latency**, and **estimated cost savings** against commercial cloud rates.

Model catalog source: https://build.nvidia.com/models?filters=nimType%3Anim_type_preview

## Requirements

- Python 3.10 or higher
- An NVIDIA NIM API key (free, see below)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup

### 1. Get a free NVIDIA NIM API key

1. Go to https://build.nvidia.com
2. Sign in or create an account
3. Navigate to any model page and click **Get API Key**
4. Copy the key — it starts with `nvapi-`

### 2. Create the `.env` file

In the root of this project folder, create a file named `.env` (no extension):

```
NVIDIA_API_KEY=nvapi-your-key-here
```

Replace `nvapi-your-key-here` with your actual key. 


### 3. Run the app

```bash
python app.py
```

Or on Windows, double-click `start.bat`.

The browser will open automatically at `http://localhost:8000`.

---

## Running a Benchmark

1. Open `http://localhost:8000` in your browser
2. Click **Start Benchmark** — the suite will run through all 45 models one by one
3. Click **Stop** to pause at any time — progress is saved and you can resume later
4. Click **Reset** to clear all results and start fresh
5. Use the sort controls (by TPS or TTFT) and the search bar to explore results
6. Click **Export CSV** or **Export JSON** to download the data

Each model is tested with a standard prompt and measured for:
- Tokens generated per second during streaming
- Time until the first token arrived (TTFT)
- Total response time

---

## Project Structure

```
NIM/
├── app.py               -- HTTP server, REST API endpoints, browser auto-open
├── benchmark.py         -- Benchmark engine: streaming, timing, result collection
├── models.json          -- All 45 NVIDIA NIM preview model definitions
├── models_catalog.py    -- Legacy catalog reference (not used at runtime)
├── requirements.txt     -- Python dependencies
├── start.bat            -- One-click Windows launcher
├── run_benchmark.bat    -- Batch file to run benchmark directly
├── static/
│   └── index.html       -- Full web UI (vanilla HTML/CSS/JS, no external CDN)
├── .env                 -- Your API key (git-ignored, create manually)
├── .gitignore           -- Git ignore rules
└── README.md            -- This file (git-ignored, stays local)
```

---

## The 45 Free Preview Models

| # | Model ID | Provider |
|---|----------|----------|
| 1 | moonshotai/kimi-k3_1-pro | Moonshot AI |
| 2 | mistralai/mistral-large-4-1t-a52b | Mistral AI |
| 3 | nvidia/nemotron-3.5-parse | NVIDIA |
| 4 | nvidia/nemotron-3.5-bolt-e4b | NVIDIA |
| 5 | nvidia/nemotron-3_5-rerank-8b | NVIDIA |
| 6 | nvidia/nemotron-3_5-embed-1b | NVIDIA |
| 7 | nvidia/nemotron-3_5-embed-8b | NVIDIA |
| 8 | minimaxai/minimax-m3.1-flash | MiniMax AI |
| 9 | ipd/rfd4-proteina | IPD |
| 10 | nvidia/nemotron-3.5-super-vl-120b-a12b | NVIDIA |
| 11 | stepfun-ai/step-5-preview | StepFun AI |
| 12 | nvidia/kumo-tabular | NVIDIA |
| 13 | nvidia/body-pose | NVIDIA |
| 14 | deepseek-ai/deepseek-v4.1-flash | DeepSeek AI |
| 15 | nvidia/kumo-relational | NVIDIA |
| 16 | z-ai/glm-5-3-flash | Z.ai |
| 17 | nvidia/nemotron-3.5-lightning-30b-a3b | NVIDIA |
| 18 | meta/muse-glimmer-30b | Meta |
| 19 | nvidia/riva-translate-4b-instruct-v2 | NVIDIA |
| 20 | nvidia/ising-calibration-1.5-31b | NVIDIA |
| 21 | nvidia/nemotron-3-embed-1b | NVIDIA |
| 22 | poolside/laguna-xs-2.1 | Poolside |
| 23 | google/diffusiongemma-26b-a4b-it | Google |
| 24 | nvidia/nemotron-3-ultra-550b-a55b | NVIDIA |
| 25 | nvidia/nemotron-3.5-content-safety | NVIDIA |
| 26 | nvidia/cosmos3-nano | NVIDIA |
| 27 | nvidia/cosmos3-nano-reasoner | NVIDIA |
| 28 | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning | NVIDIA |
| 29 | nvidia/synthetic-video-detector | NVIDIA |
| 30 | nvidia/active-speaker-detection | NVIDIA |
| 31 | nvidia/ising-calibration-1-35b-a3b | NVIDIA |
| 32 | google/gemma-4-31b-it | Google |
| 33 | nvidia/nemotron-voicechat | NVIDIA |
| 34 | nvidia/cosmos-transfer2_5-2b | NVIDIA |
| 35 | nvidia/streampetr | NVIDIA |
| 36 | nvidia/llama-3_1-nemotron-safety-guard-8b-v3 | NVIDIA |
| 37 | openai/gpt-oss-20b | OpenAI |
| 38 | meta/llama-guard-4-12b | Meta |
| 39 | nvidia/bnr | NVIDIA |
| 40 | nvidia/magpie-tts-zeroshot | NVIDIA |
| 41 | nvidia/sparsedrive | NVIDIA |
| 42 | nvidia/bevformer | NVIDIA |
| 43 | nvidia/studiovoice | NVIDIA |
| 44 | meta/llama-3.2-90b-vision-instruct | Meta |
| 45 | google/google-paligemma | Google |

---

## Notes

- All 45 models are hosted on NVIDIA's free preview tier — no charges apply during benchmarking
- Some models (e.g., embedding, reranking, protein design, audio, video) may not support standard chat completion and will show a `skip` or `error` result — this is expected
- `results.json` is saved locally and git-ignored; it persists between runs so you can stop and resume
- The benchmark runs models sequentially to avoid rate limits

---

## License

MIT
