# Consumer Hardware VRAM & Memory Fit Matrix (2026 Edition)
**Source:** The Zero-Dollar Dev (`https://thezerodollardev.blogspot.com/`)

---

## 1. Fast Reference Table by RAM / VRAM Tier

| System Spec | Dedicated VRAM | Recommended Models | Quantization | Maximum Safe Context | Expected Speed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8GB Unified / RAM** | Shared iGPU / 4GB dGPU | Qwen 2.5 Coder 7B, Llama 3.2 3B, DeepSeek-R1-Distill-Qwen-1.5B | Q4_K_M | 4,096 tokens | 22–35 tok/s |
| **16GB RAM / 6GB VRAM** | 6GB VRAM + 10GB CPU | DeepSeek-R1-Distill-Qwen-7B, Phi-4 14B, Gemma 2 9B | Q4_K_M / Q5_K_M | 8,192 tokens | 14–26 tok/s |
| **16GB Unified (Mac M1-M4)** | 12GB Unified Allocated | DeepSeek-R1-Distill-14B, Qwen 2.5 Coder 14B | Q4_K_M | 16,384 tokens | 18–28 tok/s |
| **24GB RAM / 12GB VRAM** | 12GB RTX 3060/4070 | Mistral Small 24B, DeepSeek-R1 14B Q5_K_M | Q4_K_M / Q5_K_M | 16,384 tokens | 20–35 tok/s |
| **32GB RAM / 16GB VRAM** | 16GB RTX 4080/4090 / Mac | Command-R 35B, Llama 3.3 70B (CPU offload) | Q4_K_M / Q3_K_M | 32,768 tokens | 8–18 tok/s (70B), 25–40 tok/s (35B) |

---

## 2. Memory Overhead Formula

Total System Memory required is calculated as:

$$\text{RAM/VRAM Required} = \text{Model Weights Size} + \text{KV Cache Memory} + \text{Runtime Context Overhead}$$

### KV-Cache Memory Calculation:
- **16-bit float (default):** $\approx 0.5 \text{ MB per token}$ on large 70B models, $\approx 0.12 \text{ MB per token}$ on 7B models.
- **8-bit quantized KV cache (`q8_0`):** Reduces KV cache footprint by **50%** with $<0.1\%$ perplexity degradation.
- **4-bit quantized KV cache (`q4_0`):** Reduces KV cache footprint by **75%**.

```bash
# Enable 8-bit quantized KV cache in Ollama / llama.cpp
export OLLAMA_FLASH_ATTENTION=1
export OLLAMA_KV_CACHE_TYPE=q8_0
```

---

## 3. Quantization Trade-offs

| Quantization Type | Bits / Weight | Quality Retention | Memory Savings vs FP16 | Recommended Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Q8_0** | 8.0 bits | 99.8% | 50% | High-precision coding (7B / 8B models) |
| **Q5_K_M** | 5.5 bits | 99.1% | 65% | Sweet spot for reasoning & math |
| **Q4_K_M** | 4.5 bits | 97.8% | 72% | Best default for 8GB & 16GB laptops |
| **Q3_K_M** | 3.5 bits | 92.4% | 78% | Running 70B models on 32GB RAM |
| **Q2_K** | 2.5 bits | <80% | 84% | Not recommended for production code |

---

## 4. Troubleshooting Out-Of-Memory (OOM) Errors

If you encounter `CUDA error: out of memory` or system freeze:
1. Reduce context window: add `PARAMETER num_ctx 4096` to your Modelfile.
2. Enable Flash Attention: `export OLLAMA_FLASH_ATTENTION=1`.
3. Offload fewer GPU layers: in llama.cpp, adjust `-ngl` downward by 4-6 layers until VRAM usage sits at 90% peak.
