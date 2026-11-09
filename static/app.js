// static/app.js - NVIDIA NIM 45 Preview Models Benchmark Suite Logic

// Built-in catalog of all 45 models for instantaneous zero-latency rendering
const CATALOG_MODELS = [
  { id: "moonshotai/kimi-k3_1-pro", name: "kimi-k3.1-pro", provider: "Moonshot AI", family: "moonshotai", description: "3T-class open model with 1M-token context for coding and finance." },
  { id: "mistralai/mistral-large-4-1t-a52b", name: "Mistral Large 4", provider: "Mistral AI", family: "mistral", description: "1T-total / 52B-active granular MoE with reasoning and tool calling." },
  { id: "nvidia/nemotron-3.5-parse", name: "nemotron-3.5-parse", provider: "NVIDIA", family: "nvidia", description: "Extract text, tables, and document layout from page images." },
  { id: "nvidia/nemotron-3.5-bolt-e4b", name: "Nemotron 3.5 Bolt E4B", provider: "NVIDIA", family: "nvidia", description: "Compact text model for reasoning, tool calling, and agentic chat." },
  { id: "nvidia/nemotron-3_5-rerank-8b", name: "nemotron-3.5-rerank-8b", provider: "NVIDIA", family: "nvidia", description: "8B multimodal reranking model scoring relevance between passage and query." },
  { id: "nvidia/nemotron-3_5-embed-1b", name: "nemotron-3.5-embed-1b", provider: "NVIDIA", family: "nvidia", description: "1B multimodal embedding model for text and document retrieval." },
  { id: "nvidia/nemotron-3_5-embed-8b", name: "nemotron-3.5-embed-8b", provider: "NVIDIA", family: "nvidia", description: "8B multimodal embedding model for RAG and semantic retrieval." },
  { id: "minimaxai/minimax-m3.1-flash", name: "minimax-m3.1-flash", provider: "MiniMax", family: "minimax", description: "Native multimodal MoE for coding, agentic workflows, and computer use." },
  { id: "ipd/rfd4-proteina", name: "rfd4-proteina", provider: "IPD", family: "biology", description: "Generative model for protein, enzyme, and antibody design." },
  { id: "nvidia/nemotron-3.5-super-vl-120b-a12b", name: "nemotron-3.5-super-vl-120b-a12b", provider: "NVIDIA", family: "nvidia", description: "Reasoning model for agentic, coding, and multimodal workloads." },
  { id: "stepfun-ai/step-5-preview", name: "Step 5 Preview", provider: "StepFun", family: "stepfun", description: "~600B MoE with 1M context, reasoning and tool calling in NVFP4." },
  { id: "nvidia/kumo-tabular", name: "Kumo Tabular", provider: "NVIDIA", family: "nvidia", description: "In-context learning for classification and regression over tables." },
  { id: "nvidia/body-pose", name: "3D Body Pose", provider: "NVIDIA", family: "nvidia", description: "Estimate 3D human body pose and skeleton from video input." },
  { id: "deepseek-ai/deepseek-v4.1-flash", name: "deepseek-v4.1-flash", provider: "DeepSeek", family: "deepseek", description: "552B MoE, 8B active params with native multimodal support." },
  { id: "nvidia/kumo-relational", name: "Kumo Relational", provider: "NVIDIA", family: "nvidia", description: "Relational foundation model for prediction over multi-table data." },
  { id: "z-ai/glm-5-3-flash", name: "glm-5-3-flash", provider: "Z.ai", family: "z-ai", description: "Multimodal 320B MoE with hybrid KDA and sparse MLA attention in FP8." },
  { id: "nvidia/nemotron-3.5-lightning-30b-a3b", name: "nemotron-3.5-lightning-30b-a3b", provider: "NVIDIA", family: "nvidia", description: "Fastest 30B A3B MoE for specialized agentic tasks." },
  { id: "meta/muse-glimmer-30b", name: "muse-glimmer-30b", provider: "Meta", family: "meta", description: "Multimodal reasoning model with native tool-calling and chain-of-thought." },
  { id: "nvidia/riva-translate-4b-instruct-v2", name: "riva-translate-4b-instruct-v2", provider: "NVIDIA", family: "nvidia", description: "Translation model in 37 languages with few-shot example prompting." },
  { id: "nvidia/ising-calibration-1.5-31b", name: "ising-calibration-1.5-31b", provider: "NVIDIA", family: "nvidia", description: "Vision-language model analyzing quantum computing calibration plots." },
  { id: "nvidia/nemotron-3-embed-1b", name: "nemotron-3-embed-1b", provider: "NVIDIA", family: "nvidia", description: "1B embedding model for semantic search and retrieval." },
  { id: "poolside/laguna-xs-2.1", name: "laguna-xs-2.1", provider: "Poolside", family: "poolside", description: "Efficient 33B MoE for local, long-horizon agentic coding." },
  { id: "google/diffusiongemma-26b-a4b-it", name: "diffusiongemma-26b-a4b-it", provider: "Google", family: "google", description: "Diffusion-based 26B LLM enabling parallel token generation." },
  { id: "nvidia/nemotron-3-ultra-550b-a55b", name: "nemotron-3-ultra-550b-a55b", provider: "NVIDIA", family: "nvidia", description: "Hybrid Mamba-Transformer MoE with 1M context for agentic reasoning." },
  { id: "nvidia/nemotron-3.5-content-safety", name: "nemotron-3.5-content-safety", provider: "NVIDIA", family: "nvidia", description: "Multilingual model for detecting unsafe and toxic content." },
  { id: "nvidia/cosmos3-nano", name: "cosmos3-nano", provider: "NVIDIA", family: "nvidia", description: "Generates images, videos and action predictions from text and visuals." },
  { id: "nvidia/cosmos3-nano-reasoner", name: "cosmos3-nano-reasoner", provider: "NVIDIA", family: "nvidia", description: "Vision language model for physical world structured reasoning." },
  { id: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning", name: "nemotron-3-nano-omni-30b-a3b-reasoning", provider: "NVIDIA", family: "nvidia", description: "Omni-modal reasoning model understanding video, speech, and text." },
  { id: "nvidia/synthetic-video-detector", name: "synthetic-video-detector", provider: "NVIDIA", family: "nvidia", description: "AI micro-service for detecting AI-generated (synthetic) videos." },
  { id: "nvidia/active-speaker-detection", name: "Active Speaker Detection", provider: "NVIDIA", family: "nvidia", description: "Detect and track speaker identities across video frames." },
  { id: "nvidia/ising-calibration-1-35b-a3b", name: "ising-calibration-1-35b-a3b", provider: "NVIDIA", family: "nvidia", description: "Open VLM for quantum computer calibration charts." },
  { id: "google/gemma-4-31b-it", name: "gemma-4-31b-it", provider: "Google", family: "google", description: "Dense 31B model for coding, agentic workflows, and fine-tuning." },
  { id: "nvidia/nemotron-voicechat", name: "nemotron-voicechat", provider: "NVIDIA", family: "nvidia", description: "Conversational voice model optimized for real-time speech responses." },
  { id: "nvidia/cosmos-transfer2_5-2b", name: "cosmos-transfer2.5-2b", provider: "NVIDIA", family: "nvidia", description: "Generates physics-aware video world states for physical AI." },
  { id: "nvidia/streampetr", name: "streampetr", provider: "NVIDIA", family: "nvidia", description: "StreamPETR offers efficient 3D object detection for autonomous driving." },
  { id: "nvidia/llama-3_1-nemotron-safety-guard-8b-v3", name: "llama-3.1-nemotron-safety-guard-8b-v3", provider: "NVIDIA", family: "nvidia", description: "Leading multilingual content safety model for LLM moderation." },
  { id: "openai/gpt-oss-20b", name: "gpt-oss-20b", provider: "OpenAI", family: "openai", description: "Mixture of Experts text LLM for efficient reasoning and math." },
  { id: "meta/llama-guard-4-12b", name: "llama-guard-4-12b", provider: "Meta", family: "meta", description: "Multimodal safety classifier for prompts and responses." },
  { id: "nvidia/bnr", name: "Background Noise Removal", provider: "NVIDIA", family: "nvidia", description: "Removes unwanted noises from audio improving speech." },
  { id: "nvidia/magpie-tts-zeroshot", name: "magpie-tts-zeroshot", provider: "NVIDIA", family: "nvidia", description: "Text-to-speech generated from short audio sample." },
  { id: "nvidia/sparsedrive", name: "sparsedrive", provider: "NVIDIA", family: "nvidia", description: "End-to-end autonomous driving stack with perception and planning." },
  { id: "nvidia/bevformer", name: "bevformer", provider: "NVIDIA", family: "nvidia", description: "Multi-frame bird's-eye-view 3D perception for autonomous driving." },
  { id: "nvidia/studiovoice", name: "Studio Voice", provider: "NVIDIA", family: "nvidia", description: "Produces studio-quality speech from low-quality audio." },
  { id: "meta/llama-3.2-90b-vision-instruct", name: "llama-3.2-90b-vision-instruct", provider: "Meta", family: "meta", description: "Vision-language model excelling in reasoning from images." },
  { id: "google/google-paligemma", name: "paligemma", provider: "Google", family: "google", description: "Vision language model adept at text and visual comprehension." }
];

let allModels = [...CATALOG_MODELS];
let benchmarkResults = [];
let currentFamilyFilter = 'all';
let tpsChartInstance = null;
let latencyChartInstance = null;

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  initCharts();
  renderModelsList(); // Immediate instant render of all 45 models
  checkServerStatus();
  setupEventListeners();
  loadModelsFromServer();
});

// Setup Chart.js instances
function initCharts() {
  const tpsCtx = document.getElementById('tpsChart').getContext('2d');
  tpsChartInstance = new Chart(tpsCtx, {
    type: 'bar',
    data: {
      labels: [],
      datasets: [{
        label: 'Tokens / Sec',
        data: [],
        backgroundColor: 'rgba(118, 185, 0, 0.75)',
        borderColor: '#76b900',
        borderWidth: 1.5,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.parsed.y} tokens/sec`
          }
        }
      },
      scales: {
        x: {
          ticks: { color: '#9ca3af', font: { size: 10 } },
          grid: { display: false }
        },
        y: {
          ticks: { color: '#9ca3af', font: { size: 10 } },
          grid: { color: 'rgba(255,255,255,0.05)' },
          title: { display: true, text: 'Tokens / Sec', color: '#9ca3af', font: { size: 10 } },
          beginAtZero: true
        }
      }
    }
  });

  const latCtx = document.getElementById('latencyChart').getContext('2d');
  latencyChartInstance = new Chart(latCtx, {
    type: 'bar',
    data: {
      labels: [],
      datasets: [
        {
          label: 'TTFT (ms)',
          data: [],
          backgroundColor: 'rgba(56, 189, 248, 0.75)',
          borderColor: '#38bdf8',
          borderWidth: 1,
          borderRadius: 4
        },
        {
          label: 'Total Latency (ms)',
          data: [],
          backgroundColor: 'rgba(168, 85, 247, 0.55)',
          borderColor: '#a855f7',
          borderWidth: 1,
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: { color: '#d1d5db', font: { size: 10 } }
        },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.dataset.label}: ${ctx.parsed.y} ms`
          }
        }
      },
      scales: {
        x: {
          ticks: { color: '#9ca3af', font: { size: 10 } },
          grid: { display: false }
        },
        y: {
          ticks: { color: '#9ca3af', font: { size: 10 } },
          grid: { color: 'rgba(255,255,255,0.05)' },
          title: { display: true, text: 'Milliseconds (ms)', color: '#9ca3af', font: { size: 10 } },
          beginAtZero: true
        }
      }
    }
  });
}

// Check server status (.env API Key)
async function checkServerStatus() {
  try {
    const res = await fetch('/api/status');
    const data = await res.json();
    const statusDot = document.getElementById('api-status-dot');
    const statusText = document.getElementById('api-status-text');

    if (data.has_env_key) {
      statusDot.className = 'w-2.5 h-2.5 rounded-full bg-[#76b900] shadow-[0_0_8px_#76b900]';
      statusText.textContent = `API Key: Active (${data.masked_key})`;
    } else {
      statusDot.className = 'w-2.5 h-2.5 rounded-full bg-red-400';
      statusText.textContent = 'API Key: Missing in .env';
    }
  } catch (e) {
    console.error('Status check error:', e);
  }
}

// Sync models from server
async function loadModelsFromServer() {
  try {
    const res = await fetch('/api/models');
    if (res.ok) {
      const data = await res.json();
      if (data.models && data.models.length > 0) {
        allModels = data.models;
        renderModelsList();
      }
    }
  } catch (e) {
    console.log('Using local catalog cache:', e);
  }
}

// Render model checklist based on current filter & search
function renderModelsList() {
  const container = document.getElementById('models-list');
  const searchInput = document.getElementById('model-search');
  const search = searchInput ? searchInput.value.toLowerCase().trim() : '';

  const filtered = allModels.filter(m => {
    // Family filter
    if (currentFamilyFilter !== 'all') {
      const familyMatch = (m.family && m.family.toLowerCase().includes(currentFamilyFilter)) ||
                          (m.id && m.id.toLowerCase().includes(currentFamilyFilter)) ||
                          (m.provider && m.provider.toLowerCase().includes(currentFamilyFilter));
      if (!familyMatch) return false;
    }
    // Search input
    if (search) {
      const match = m.id.toLowerCase().includes(search) || 
                    m.name.toLowerCase().includes(search) || 
                    (m.description && m.description.toLowerCase().includes(search));
      if (!match) return false;
    }
    return true;
  });

  document.getElementById('models-count-badge').textContent = `${allModels.length} models`;

  if (filtered.length === 0) {
    container.innerHTML = '<div class="text-center py-6 text-xs text-gray-500">No models match the filter.</div>';
    return;
  }

  container.innerHTML = filtered.map((m, idx) => `
    <label class="flex items-start space-x-2.5 p-2 rounded hover:bg-[#19222e] cursor-pointer transition select-none border border-transparent hover:border-gray-800">
      <input type="checkbox" class="model-checkbox mt-0.5 w-3.5 h-3.5 rounded text-[#76b900] focus:ring-[#76b900] bg-gray-900 border-gray-700" 
             value="${m.id}" ${idx < 4 ? 'checked' : ''}>
      <div class="flex-1 min-w-0">
        <div class="flex items-center space-x-1.5 flex-wrap">
          <span class="font-medium text-xs text-gray-200 truncate">${m.name || m.id}</span>
          <span class="text-[9px] px-1.5 py-0.2 rounded bg-[#76b900]/20 text-[#8ce400] font-semibold border border-[#76b900]/30">Preview</span>
          <span class="text-[9px] px-1.5 py-0.2 rounded bg-gray-800 text-gray-400">${m.provider || 'NVIDIA'}</span>
        </div>
        <div class="text-[10px] text-gray-500 font-mono truncate">${m.id}</div>
      </div>
    </label>
  `).join('');

  updateBatchCount();

  container.querySelectorAll('.model-checkbox').forEach(cb => {
    cb.addEventListener('change', updateBatchCount);
  });
}

function updateBatchCount() {
  const checked = document.querySelectorAll('.model-checkbox:checked').length;
  document.getElementById('batch-count-btn').textContent = checked;
}

// Setup Event Listeners
function setupEventListeners() {
  // Family pills filter
  document.querySelectorAll('#family-pills .pill-filter').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#family-pills .pill-filter').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFamilyFilter = btn.dataset.family;
      renderModelsList();
    });
  });

  // Search input
  const searchInput = document.getElementById('model-search');
  if (searchInput) {
    searchInput.addEventListener('input', renderModelsList);
  }

  // Select all / clear buttons
  document.getElementById('btn-select-all').addEventListener('click', () => {
    document.querySelectorAll('.model-checkbox').forEach(cb => cb.checked = true);
    updateBatchCount();
  });
  document.getElementById('btn-clear-selection').addEventListener('click', () => {
    document.querySelectorAll('.model-checkbox').forEach(cb => cb.checked = false);
    updateBatchCount();
  });

  // Run benchmark action
  document.getElementById('btn-run-benchmark').addEventListener('click', runBenchmarkBatch);

  // Output Inspector modal
  document.getElementById('btn-close-output-modal').addEventListener('click', () => {
    document.getElementById('output-modal').classList.add('hidden');
  });

  // Clear results
  document.getElementById('btn-clear-results').addEventListener('click', () => {
    benchmarkResults = [];
    updateResultsUI();
  });

  // Export CSV
  document.getElementById('btn-export-csv').addEventListener('click', exportCSV);

  // Export JSON
  document.getElementById('btn-export-json').addEventListener('click', exportJSON);
}

// Execute benchmark sequentially across checked models
async function runBenchmarkBatch() {
  const checkedBoxes = Array.from(document.querySelectorAll('.model-checkbox:checked'));
  if (checkedBoxes.length === 0) {
    alert('Please select at least one model from the catalog.');
    return;
  }

  const modelIds = checkedBoxes.map(cb => cb.value);
  const runBtn = document.getElementById('btn-run-benchmark');
  const progressBox = document.getElementById('benchmark-progress');
  const progressText = document.getElementById('progress-text');

  runBtn.disabled = true;
  runBtn.classList.add('opacity-50');
  progressBox.classList.remove('hidden');

  for (let i = 0; i < modelIds.length; i++) {
    const mid = modelIds[i];
    progressText.textContent = `[${i + 1}/${modelIds.length}] Benchmarking ${mid}...`;

    try {
      const res = await fetch('/api/benchmark', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model_id: mid })
      });

      const data = await res.json();
      if (data.success) {
        handleBenchmarkResult(data);
      } else {
        console.warn(`Benchmark issue for ${mid}:`, data.error);
        if (data.error && data.error.includes('NVIDIA_API_KEY is not set')) {
          alert('NVIDIA_API_KEY is not set. Please open the .env file in the project directory, add your key (NVIDIA_API_KEY=nvapi-...), and save it.');
          break;
        }
      }
    } catch (e) {
      console.error(`Network error for ${mid}:`, e);
    }
  }

  progressBox.classList.add('hidden');
  runBtn.disabled = false;
  runBtn.classList.remove('opacity-50');
}

// Update results history
function handleBenchmarkResult(result) {
  const existingIdx = benchmarkResults.findIndex(r => r.model_id === result.model_id);
  if (existingIdx >= 0) {
    benchmarkResults[existingIdx] = result;
  } else {
    benchmarkResults.unshift(result);
  }
  updateResultsUI();
}

// Update UI components (Cards, Charts, Table)
function updateResultsUI() {
  const tableBody = document.getElementById('results-table-body');
  
  if (benchmarkResults.length === 0) {
    tableBody.innerHTML = '<tr><td colspan="8" class="text-center py-8 text-gray-500">No benchmark tests executed yet. Select models and click "Benchmark Selected Models".</td></tr>';
    document.getElementById('stat-avg-tps').textContent = '--';
    document.getElementById('stat-avg-ttft').textContent = '--';
    document.getElementById('stat-avg-latency').textContent = '--';
    document.getElementById('stat-saved-cost').textContent = 'Market value saved: $0.00';
    updateCharts([], [], [], []);
    return;
  }

  const validResults = benchmarkResults.filter(r => r.success);
  const avgTps = validResults.reduce((acc, r) => acc + (r.tokens_per_sec || 0), 0) / (validResults.length || 1);
  const avgTtft = validResults.reduce((acc, r) => acc + (r.ttft_ms || 0), 0) / (validResults.length || 1);
  const avgLatency = validResults.reduce((acc, r) => acc + (r.total_latency_ms || 0), 0) / (validResults.length || 1);
  const totalSavedCost = validResults.reduce((acc, r) => acc + (r.raw_cost_commercial || 0), 0);

  document.getElementById('stat-avg-tps').textContent = `${avgTps.toFixed(1)} /s`;
  document.getElementById('stat-avg-ttft').textContent = `${Math.round(avgTtft)} ms`;
  document.getElementById('stat-avg-latency').textContent = `${(avgLatency / 1000).toFixed(2)} s`;
  document.getElementById('stat-saved-cost').textContent = `Market value saved: $${totalSavedCost.toFixed(5)}`;

  tableBody.innerHTML = benchmarkResults.map((r, i) => `
    <tr class="hover:bg-[#161f2a]/60 transition">
      <td class="py-3 px-3 font-medium text-white">
        <div class="flex items-center space-x-1.5">
          <span class="truncate max-w-[220px]" title="${r.model_id}">${r.model_id}</span>
        </div>
      </td>
      <td class="py-3 px-3 text-right font-mono font-bold text-[#76b900]">${r.tokens_per_sec || '--'}</td>
      <td class="py-3 px-3 text-right font-mono text-cyan-400">${r.ttft_ms ? Math.round(r.ttft_ms) : '--'}</td>
      <td class="py-3 px-3 text-right font-mono text-gray-300">${r.total_latency_ms ? (r.total_latency_ms / 1000).toFixed(2) + 's' : '--'}</td>
      <td class="py-3 px-3 text-right font-mono text-gray-400">${r.prompt_tokens || 0} / ${r.completion_tokens || 0}</td>
      <td class="py-3 px-3 text-right font-semibold text-[#76b900]">FREE</td>
      <td class="py-3 px-3 text-right font-mono text-gray-300">${r.cost_commercial_est || '$0.00'}</td>
      <td class="py-3 px-3 text-center">
        <button onclick="viewOutput(${i})" class="text-xs text-gray-300 hover:text-white px-2 py-0.5 rounded bg-[#1e293b] border border-gray-700 hover:border-gray-500">
          Inspect
        </button>
      </td>
    </tr>
  `).join('');

  const chartLabels = validResults.map(r => {
    const parts = r.model_id.split('/');
    return parts[parts.length - 1];
  });
  const tpsData = validResults.map(r => r.tokens_per_sec || 0);
  const ttftData = validResults.map(r => Math.round(r.ttft_ms || 0));
  const latencyData = validResults.map(r => Math.round(r.total_latency_ms || 0));

  updateCharts(chartLabels, tpsData, ttftData, latencyData);
}

function updateCharts(labels, tpsData, ttftData, latencyData) {
  if (tpsChartInstance) {
    tpsChartInstance.data.labels = labels;
    tpsChartInstance.data.datasets[0].data = tpsData;
    tpsChartInstance.update();
  }
  if (latencyChartInstance) {
    latencyChartInstance.data.labels = labels;
    latencyChartInstance.data.datasets[0].data = ttftData;
    latencyChartInstance.data.datasets[1].data = latencyData;
    latencyChartInstance.update();
  }
}

// Modal view full output
window.viewOutput = function(idx) {
  const result = benchmarkResults[idx];
  if (!result) return;

  document.getElementById('modal-model-name').textContent = result.model_id;
  document.getElementById('modal-model-stats').textContent = 
    `Tokens/sec: ${result.tokens_per_sec || '--'} | TTFT: ${result.ttft_ms || '--'} ms | Total Latency: ${(result.total_latency_ms / 1000).toFixed(2)}s | Total Tokens: ${result.total_tokens}`;
  document.getElementById('modal-output-content').textContent = result.full_output || '[No output text captured]';
  document.getElementById('output-modal').classList.remove('hidden');
};

// Export to CSV
function exportCSV() {
  if (benchmarkResults.length === 0) {
    alert('No results to export.');
    return;
  }
  const headers = ['Model ID', 'Tokens Per Sec', 'TTFT (ms)', 'Total Latency (ms)', 'Prompt Tokens', 'Completion Tokens', 'Total Tokens', 'NVIDIA Cost', 'Commercial Cost Est', 'Timestamp'];
  const rows = benchmarkResults.map(r => [
    `"${r.model_id}"`,
    r.tokens_per_sec,
    r.ttft_ms,
    r.total_latency_ms,
    r.prompt_tokens,
    r.completion_tokens,
    r.total_tokens,
    `"${r.cost_nvidia}"`,
    `"${r.cost_commercial_est}"`,
    `"${r.timestamp}"`
  ]);

  const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(e => e.join(','))].join('\n');
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', `nvidia_nim_benchmark_${Date.now()}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Export to JSON
function exportJSON() {
  if (benchmarkResults.length === 0) {
    alert('No results to export.');
    return;
  }
  const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(benchmarkResults, null, 2));
  const link = document.createElement('a');
  link.setAttribute('href', dataStr);
  link.setAttribute('download', `nvidia_nim_benchmark_${Date.now()}.json`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
