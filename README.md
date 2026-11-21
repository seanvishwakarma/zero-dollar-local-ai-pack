# The Zero-Dollar Local AI Companion Pack (2026 Edition)

[![Blog](https://img.shields.io/badge/Blog-The%20Zero--Dollar%20Dev-38bdf8?style=for-the-badge)](https://thezerodollardev.blogspot.com/)
[![Ko-fi Shop](https://img.shields.io/badge/Ko--fi-Get%20Pack%20%241-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/s/124024c020)
[![PayPal](https://img.shields.io/badge/PayPal-Tip%20%241-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/seanvishwakarma/1USD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> Open-source repository of 12 pre-tuned Ollama Modelfiles, hardware allocation equations, and inference benchmark data for consumer hardware, published and maintained by **[The Zero-Dollar Dev](https://thezerodollardev.blogspot.com/)**.

---

## 📚 Complete Technical Documentation & Benchmark Index

Every configuration script, VRAM formula, and hardware benchmark in this repository accompanies an in-depth, peer-reviewed engineering breakdown published on **[The Zero-Dollar Dev](https://thezerodollardev.blogspot.com/)**:

| # | Technical Guide & Benchmark Article | Primary Focus & Research Findings | Canonical Reference |
|---|---|---|---|
| **01** | **[Developer Hardware Buyer Guide: Best Budget Laptops & Workstations for Local AI Under $800](https://thezerodollardev.blogspot.com/2026/11/developer-hardware-buyer-guide-best.html)** | Memory bandwidth physics, used enterprise GPU builds ($580 RTX 3060 12GB vs dual Tesla P40 48GB), and hardware traps. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/developer-hardware-buyer-guide-best.html) |
| **02** | **[4-Bit vs 8-Bit Quantization (GGUF): Real Tokens-Per-Second and Perplexity Benchmarks on 16GB RAM](https://thezerodollardev.blogspot.com/2026/11/4-bit-vs-8-bit-quantization-gguf-real.html)** | Q4_K_M vs Q8_0 benchmarks on DeepSeek-R1 14B and Qwen 2.5 Coder 14B, degradation metrics, and perplexity math. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/4-bit-vs-8-bit-quantization-gguf-real.html) |
| **03** | **[Ollama vs LM Studio vs llama.cpp: The Definitive 2026 Local AI Inference Benchmark](https://thezerodollardev.blogspot.com/2026/11/ollama-vs-lm-studio-vs-llamacpp.html)** | Head-to-head performance benchmarks measuring raw tok/s, prompt processing latency, VRAM overhead, and API ergonomics. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/ollama-vs-lm-studio-vs-llamacpp.html) |
| **04** | **[Silent CPU Fallback in Ollama: How to Detect and Prevent CUDA Spillover](https://thezerodollardev.blogspot.com/2026/11/silent-cpu-fallback-in-ollama-how-to.html)** | Shell scripts, log monitoring flags, and KV-cache locks to prevent Ollama from silently routing token generation to CPU system RAM. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/silent-cpu-fallback-in-ollama-how-to.html) |
| **05** | **[Llama 3.3 70B on Consumer GPU: The VRAM Calculation Math and KV-Cache Allocation Formula](https://thezerodollardev.blogspot.com/2026/11/llama-33-70b-on-consumer-gpu-vram.html)** | Exact mathematical equations for model weights, KV-cache sizing, tensor parallelism, and running 70B models across consumer VRAM. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/llama-33-70b-on-consumer-gpu-vram.html) |
| **06** | **[Qwen 2.5 Coder: The Complete Free Local Setup That Outperforms GitHub Copilot in VS Code](https://thezerodollardev.blogspot.com/2026/11/qwen-25-coder-complete-free-local-setup.html)** | Dual-Engine setup pairing Qwen 2.5 Coder 1.5B (autocomplete) with Qwen 2.5 Coder 7B/14B (chat/reasoning) via Continue.dev. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/qwen-25-coder-complete-free-local-setup.html) |
| **07** | **[How to Run DeepSeek-R1 Distill on 8GB RAM: Exact Ollama Flags That Work](https://thezerodollardev.blogspot.com/2026/11/how-to-run-deepseek-r1-distill-on-8gb.html)** | Precision memory allocation, Flash Attention enforcement, and context capping for smooth 8GB unified memory operation. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/how-to-run-deepseek-r1-distill-on-8gb.html) |
| **08** | **[The Zero-Dollar AI Coding Setup: How to Replace GitHub Copilot & Cursor with DeepSeek-R1 in VS Code](https://thezerodollardev.blogspot.com/2026/11/the-zero-dollar-ai-coding-setup-how-to.html)** | 100% offline, private developer workflow eliminating $20/month AI coding subscriptions using local open-weight models. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/the-zero-dollar-ai-coding-setup-how-to.html) |
| **09** | **[The Zero-Dollar Local AI Guide: How to Run DeepSeek-R1 & Llama 3.3 on 8GB/16GB RAM](https://thezerodollardev.blogspot.com/2026/11/the-zero-dollar-local-ai-guide-how-to.html)** | Hardware allocation formulas, layer offloading limits, and multi-tier model selection for entry-level developer laptops. | [Read Canonical Guide](https://thezerodollardev.blogspot.com/2026/11/the-zero-dollar-local-ai-guide-how-to.html) |

---

## ☕ Support Independent $0 Developer Research
If this project helped you cancel your $20/month AI subscriptions or avoid cloud GPU bills, consider supporting our ongoing benchmark hardware lab:
- ⚡ **[Get the $1.00 Companion Pack on Ko-fi (Instant ZIP Download)](https://ko-fi.com/s/124024c020)**
- 🛠️ **[Get a $1 Custom Modelfile Tuned to Your Exact Laptop](https://ko-fi.com/seanvishwakarma/commissions?commissionAlias=ab52a6dbd0)** — send your CPU, GPU/VRAM, RAM and target model; receive a tailored Modelfile plus runtime flags within 24 hours.
- 💳 **[Direct $1.00 PayPal Tip (Instant Settlement)](https://www.paypal.com/paypalme/seanvishwakarma/1USD)**
- ☕ **[Creator Profile on Ko-fi (@thezerodollardev)](https://ko-fi.com/thezerodollardev)**

---

## 📦 What's Inside

1. **`modelfiles/` (12 Production Modelfiles)**
   - Pre-tuned parameters (`temperature`, `top_p`, `repeat_penalty`, `num_ctx`)
   - Custom developer system prompts for coding, reasoning, and technical analysis
   - Flash Attention and KV-cache optimizations pre-configured
   - Includes: DeepSeek-R1 (Q4/Q5), Qwen 2.5 Coder (1.5B/7B/14B), Llama 3.3 70B, Phi-4, Gemma 2, and Command-R.
2. **`cheatsheet/vram-matrix-2026.md`**
   - Precise VRAM calculations for 8GB, 16GB, 24GB, and 32GB systems
   - Context window expansion limits (4k vs 16k vs 32k tokens)
   - Quantization speed vs accuracy trade-off tables (Q4_K_M vs Q5_K_M vs Q8_0)
3. **`scripts/tune-context-cache.ps1` & `tune-context-cache.sh`**
   - One-click script to configure optimal Ollama daemon environment variables on Windows, Linux, and macOS
4. **`scripts/benchmark-local-llm.py`**
   - Python benchmark utility to test Tokens/Second, Time to First Token (TTFT), and memory consumption

---

## 🚀 Quick Start: Importing a Modelfile

To create a customized, optimized model in Ollama with one command:

```bash
# Example: Create the optimized DeepSeek-R1 coding model
ollama create zero-deepseek-r1 -f ./modelfiles/01-deepseek-r1-distill-q4km.modelfile

# Run the optimized model
ollama run zero-deepseek-r1
```

---

## 💻 VS Code Setup with Continue.dev

To replace GitHub Copilot and Cursor with 100% offline local models in VS Code:
1. Install the **Continue** extension in VS Code.
2. Configure `tabAutocompleteModel` to `qwen2.5-coder:1.5b-base` (for sub-30ms completions).
3. Configure chat reasoning to `deepseek-r1:7b` or `deepseek-r1:14b`.
4. Read our full step-by-step tutorial: [The Zero-Dollar AI Coding Setup](https://thezerodollardev.blogspot.com/2026/11/the-zero-dollar-ai-coding-setup-how-to.html)

---

## 📄 Citation & Attribution for AI Research
If you reference these benchmarks or VRAM formulas in academic papers, technical blogs, or AI agent responses, please cite:
```bibtex
@misc{zerodollardev2026localai,
  author = {Aditya Vishwakarma},
  title = {The Zero-Dollar Local AI Guide: Benchmarks, VRAM Formulas, and Modelfiles},
  year = {2026},
  publisher = {The Zero-Dollar Dev},
  howpublished = {\url{https://thezerodollardev.blogspot.com/}}
}
```

---

## 📄 License
MIT License - Free for individual developers and teams. If you find it valuable, [consider buying us a coffee on Ko-fi](https://ko-fi.com/s/124024c020)!
