"""
models_catalog.py
The exact 45 Preview / Free Endpoint models live on NVIDIA Build:
https://build.nvidia.com/models?filters=nimType%3Anim_type_preview
"""

from typing import List, Dict, Any

# The exact 45 Free Preview Endpoint Models from build.nvidia.com
NVIDIA_NIM_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "moonshotai/kimi-k3_1-pro",
        "alt_id": "moonshotai/kimi-k3.1-pro",
        "name": "kimi-k3.1-pro",
        "provider": "Moonshot AI",
        "family": "moonshotai",
        "model_type": "chat",
        "is_preview": True,
        "description": "3T-class open model with 1M-token context specialized for agentic coding, 3D modeling, and finance.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.60, 2.00)
    },
    {
        "id": "mistralai/mistral-large-4-1t-a52b",
        "name": "Mistral Large 4",
        "provider": "Mistral AI",
        "family": "mistral",
        "model_type": "chat",
        "is_preview": True,
        "description": "1T-total / 52B-active granular MoE for text and image input with reasoning and function calling.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (2.00, 6.00)
    },
    {
        "id": "nvidia/nemotron-3.5-parse",
        "name": "nemotron-3.5-parse",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vlm",
        "is_preview": True,
        "description": "Extract text, tables, and document layout from page images.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.30, 0.60)
    },
    {
        "id": "nvidia/nemotron-3.5-bolt-e4b",
        "name": "Nemotron 3.5 Bolt E4B",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Compact text model for reasoning, tool calling, and agentic chat.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.25)
    },
    {
        "id": "nvidia/nemotron-3_5-rerank-8b",
        "alt_id": "nvidia/nemotron-3.5-rerank-8b",
        "name": "nemotron-3.5-rerank-8b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "rerank",
        "is_preview": True,
        "description": "8B multimodal reranking model scoring relevance between passage and query.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.20)
    },
    {
        "id": "nvidia/nemotron-3_5-embed-1b",
        "alt_id": "nvidia/nemotron-3.5-embed-1b",
        "name": "nemotron-3.5-embed-1b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "embed",
        "is_preview": True,
        "description": "1B multimodal embedding model for text and document-image retrieval in RAG applications.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.05, 0.05)
    },
    {
        "id": "nvidia/nemotron-3_5-embed-8b",
        "alt_id": "nvidia/nemotron-3.5-embed-8b",
        "name": "nemotron-3.5-embed-8b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "embed",
        "is_preview": True,
        "description": "8B multimodal embedding model for text and document-image retrieval in RAG applications.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.10, 0.10)
    },
    {
        "id": "minimaxai/minimax-m3.1-flash",
        "name": "minimax-m3.1-flash",
        "provider": "MiniMax",
        "family": "minimax",
        "model_type": "chat",
        "is_preview": True,
        "description": "Native multimodal mixture-of-experts model for coding, agentic workflows, and computer use.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.50, 1.50)
    },
    {
        "id": "ipd/rfd4-proteina",
        "name": "rfd4-proteina",
        "provider": "IPD",
        "family": "biology",
        "model_type": "specialized",
        "is_preview": True,
        "description": "A unified generative model for protein, enzyme, binder and antibody design.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.50, 1.00)
    },
    {
        "id": "nvidia/nemotron-3.5-super-vl-120b-a12b",
        "name": "nemotron-3.5-super-vl-120b-a12b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Nemotron 3.5 Super early-access reasoning model for agentic, coding, and multimodal workloads.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (1.00, 2.00)
    },
    {
        "id": "stepfun-ai/step-5-preview",
        "name": "Step 5 Preview",
        "provider": "StepFun",
        "family": "stepfun",
        "model_type": "chat",
        "is_preview": True,
        "description": "~600B-total / 27B-active multimodal MoE with 1M context, reasoning and tool calling in NVFP4.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.50, 1.50)
    },
    {
        "id": "nvidia/kumo-tabular",
        "name": "Kumo Tabular",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "specialized",
        "is_preview": True,
        "description": "Tabular in-context learning model for classification and regression over structured tables.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/body-pose",
        "name": "3D Body Pose",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "Estimate 3D human body pose and skeleton from video input.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "deepseek-ai/deepseek-v4.1-flash",
        "alt_id": "deepseek-ai/deepseek-v3",
        "name": "deepseek-v4.1-flash",
        "provider": "DeepSeek",
        "family": "deepseek",
        "model_type": "chat",
        "is_preview": True,
        "description": "552B MoE, 8B active params with native multimodal support and lower API cost using smaller KV cache.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.30, 1.00)
    },
    {
        "id": "nvidia/kumo-relational",
        "name": "Kumo Relational",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "specialized",
        "is_preview": True,
        "description": "Relational foundation model for prediction over structured, multi-table data.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "z-ai/glm-5-3-flash",
        "name": "glm-5-3-flash",
        "provider": "Z.ai",
        "family": "z-ai",
        "model_type": "chat",
        "is_preview": True,
        "description": "Multimodal 320B-total / 18B-active MoE with hybrid KDA and sparse MLA attention in FP8.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.40, 1.20)
    },
    {
        "id": "nvidia/nemotron-3.5-lightning-30b-a3b",
        "name": "nemotron-3.5-lightning-30b-a3b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Fastest 30B A3B MoE model with leading domain accuracy for specialized agentic tasks.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.30, 0.60)
    },
    {
        "id": "meta/muse-glimmer-30b",
        "name": "muse-glimmer-30b",
        "provider": "Meta",
        "family": "meta",
        "model_type": "chat",
        "is_preview": True,
        "description": "Multimodal reasoning model accepting text and images with native tool-calling and chain-of-thought.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.35, 0.70)
    },
    {
        "id": "nvidia/riva-translate-4b-instruct-v2",
        "name": "riva-translate-4b-instruct-v2",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Translation model in 37 languages with few-shot example prompting capability.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.10, 0.15)
    },
    {
        "id": "nvidia/ising-calibration-1.5-31b",
        "name": "ising-calibration-1.5-31b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vlm",
        "is_preview": True,
        "description": "Dense multimodal vision-language model analyzing quantum computing calibration plots.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.35, 0.70)
    },
    {
        "id": "nvidia/nemotron-3-embed-1b",
        "name": "nemotron-3-embed-1b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "embed",
        "is_preview": True,
        "description": "1B embedding model for semantic search, retrieval, and RAG applications.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.05, 0.05)
    },
    {
        "id": "poolside/laguna-xs-2.1",
        "name": "laguna-xs-2.1",
        "provider": "Poolside",
        "family": "poolside",
        "model_type": "chat",
        "is_preview": True,
        "description": "Efficient 33B MoE for local, long-horizon agentic coding and terminal tasks.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.40, 0.80)
    },
    {
        "id": "google/diffusiongemma-26b-a4b-it",
        "name": "diffusiongemma-26b-a4b-it",
        "provider": "Google",
        "family": "google",
        "model_type": "chat",
        "is_preview": True,
        "description": "Diffusion-based 26B parameter LLM enabling parallel token generation for real-time text apps.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.30, 0.60)
    },
    {
        "id": "nvidia/nemotron-3-ultra-550b-a55b",
        "name": "nemotron-3-ultra-550b-a55b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Hybrid Mamba-Transformer MoE with 1M context, excelling in agentic reasoning, coding, and planning.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (2.00, 3.00)
    },
    {
        "id": "nvidia/nemotron-3.5-content-safety",
        "name": "nemotron-3.5-content-safety",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Multilingual, multimodal model for detecting unsafe and toxic content.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.20)
    },
    {
        "id": "nvidia/cosmos3-nano",
        "name": "cosmos3-nano",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "Generates images, videos and action predictions from text, visual inputs and spatial controls.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.25, 0.50)
    },
    {
        "id": "nvidia/cosmos3-nano-reasoner",
        "name": "cosmos3-nano-reasoner",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vlm",
        "is_preview": True,
        "description": "Vision language model that excels in understanding physical world dynamics using structured reasoning.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.25, 0.50)
    },
    {
        "id": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        "name": "nemotron-3-nano-omni-30b-a3b-reasoning",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Omni-modal reasoning model understanding images, video, speech, and text.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.35, 0.70)
    },
    {
        "id": "nvidia/synthetic-video-detector",
        "name": "synthetic-video-detector",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "AI-powered micro-service for detecting AI-generated (synthetic) videos.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/active-speaker-detection",
        "name": "Active Speaker Detection",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "Detect and track speaker identities across video frames.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/ising-calibration-1-35b-a3b",
        "name": "ising-calibration-1-35b-a3b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vlm",
        "is_preview": True,
        "description": "Open VLM for quantum computer calibration chart understanding across qubit modalities.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.35, 0.70)
    },
    {
        "id": "google/gemma-4-31b-it",
        "alt_id": "google/gemma-2-27b-it",
        "name": "gemma-4-31b-it",
        "provider": "Google",
        "family": "google",
        "model_type": "chat",
        "is_preview": True,
        "description": "Dense 31B model delivering frontier reasoning for coding, agentic workflows, and fine-tuning.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.35, 0.70)
    },
    {
        "id": "nvidia/nemotron-voicechat",
        "name": "nemotron-voicechat",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Nemotron conversational voice model optimized for real-time speech responses.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/cosmos-transfer2_5-2b",
        "alt_id": "nvidia/cosmos-transfer2.5-2b",
        "name": "cosmos-transfer2.5-2b",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "Generates physics-aware video world states for physical AI development using text prompts.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.30)
    },
    {
        "id": "nvidia/streampetr",
        "name": "streampetr",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "StreamPETR offers efficient 3D object detection for autonomous driving.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/llama-3_1-nemotron-safety-guard-8b-v3",
        "alt_id": "nvidia/llama-3.1-nemotron-safety-guard-8b-v3",
        "name": "llama-3.1-nemotron-safety-guard-8b-v3",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "chat",
        "is_preview": True,
        "description": "Leading multilingual content safety model for enhancing LLM safety and moderation.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.20)
    },
    {
        "id": "openai/gpt-oss-20b",
        "name": "gpt-oss-20b",
        "provider": "OpenAI",
        "family": "openai",
        "model_type": "chat",
        "is_preview": True,
        "description": "Smaller Mixture of Experts (MoE) text LLM for efficient AI reasoning and math.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.25, 0.50)
    },
    {
        "id": "meta/llama-guard-4-12b",
        "name": "llama-guard-4-12b",
        "provider": "Meta",
        "family": "meta",
        "model_type": "chat",
        "is_preview": True,
        "description": "Multimodal model to classify safety for input prompts as well as output responses.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.30)
    },
    {
        "id": "nvidia/bnr",
        "name": "Background Noise Removal",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "audio",
        "is_preview": True,
        "description": "Removes unwanted noises from audio improving speech intelligibility.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.10, 0.20)
    },
    {
        "id": "nvidia/magpie-tts-zeroshot",
        "name": "magpie-tts-zeroshot",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "audio",
        "is_preview": True,
        "description": "Expressive and engaging text-to-speech generated from a short audio sample.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.30)
    },
    {
        "id": "nvidia/sparsedrive",
        "name": "sparsedrive",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "End-to-end autonomous driving stack integrating perception, prediction, and planning.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/bevformer",
        "name": "bevformer",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "vision",
        "is_preview": True,
        "description": "Advanced transformer for multi-frame bird's-eye-view 3D perception in autonomous driving.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.20, 0.40)
    },
    {
        "id": "nvidia/studiovoice",
        "name": "Studio Voice",
        "provider": "NVIDIA",
        "family": "nvidia",
        "model_type": "audio",
        "is_preview": True,
        "description": "Enhance input speech recorded in noisy environments, producing studio-quality audio.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.30)
    },
    {
        "id": "meta/llama-3.2-90b-vision-instruct",
        "name": "llama-3.2-90b-vision-instruct",
        "provider": "Meta",
        "family": "meta",
        "model_type": "chat",
        "is_preview": True,
        "description": "Cutting-edge vision-language model excelling in high-quality reasoning from images.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.90, 1.20)
    },
    {
        "id": "google/google-paligemma",
        "alt_id": "google/paligemma",
        "name": "paligemma",
        "provider": "Google",
        "family": "google",
        "model_type": "vlm",
        "is_preview": True,
        "description": "Vision language model adept at comprehending text and visual inputs to produce informative responses.",
        "cost_nvidia": "$0.00 (Preview Free Tier)",
        "commercial_rate": (0.15, 0.20)
    }
]

def get_known_catalog() -> List[Dict[str, Any]]:
    """Return the exact 45 preview models from build.nvidia.com immediately."""
    return NVIDIA_NIM_CATALOG
