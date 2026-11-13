# The Zero-Dollar Local AI Companion Pack (2026 Edition)
**Publisher:** The Zero-Dollar Dev (`https://thezerodollardev.blogspot.com/`)  
**Companion to:** *The Zero-Dollar Local AI Guide: How to Run DeepSeek-R1 & Llama 3.3 on 8GB/16GB RAM*

Thank you for supporting independent developer research! This companion pack provides ready-to-import Ollama Modelfiles, memory allocation tables, tuning scripts, and benchmark utilities to get maximum inference speed on consumer hardware.

---

## 📦 What's Inside

1. **`modelfiles/` (12 Production Modelfiles)**
   - Pre-tuned parameters (`temperature`, `top_p`, `repeat_penalty`, `num_ctx`)
   - Custom developer system prompts for coding, reasoning, and technical analysis
   - Flash Attention and KV-cache optimizations pre-configured
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

## ☕ Support & Future Updates
- **Blog:** [The Zero-Dollar Dev](https://thezerodollardev.blogspot.com/)
- **Ko-fi:** [ko-fi.com/thezerodollardev](https://ko-fi.com/thezerodollardev)
- **Direct PayPal Support:** [paypal.me/seanvishwakarma](https://www.paypal.com/paypalme/seanvishwakarma)
