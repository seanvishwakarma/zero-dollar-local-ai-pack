#!/usr/bin/env python3
"""
The Zero-Dollar Dev: Local LLM Benchmark Utility
Tests inference throughput (Tokens/Second), Time to First Token (TTFT), and latency.
Zero external pip dependencies required (uses standard library urllib).

Usage:
    python benchmark-local-llm.py --model deepseek-r1:7b --prompt "Write a quicksort implementation in Python with type annotations and docstrings."
"""

import argparse
import json
import time
import urllib.request
import urllib.error


def run_benchmark(model_name: str, host: str, prompt: str):
    url = f"http://{host}/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": True,
        "options": {"temperature": 0.6, "num_ctx": 4096},
    }

    print("=" * 60)
    print(f"Benchmarking Model: {model_name}")
    print(f"Target Ollama Host: {url}")
    print("=" * 60)

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )

    start_time = time.time()
    first_token_time = None
    token_count = 0

    try:
        with urllib.request.urlopen(req) as response:
            for line in response:
                if not line:
                    continue
                data = json.loads(line.decode("utf-8"))
                if not first_token_time and data.get("response"):
                    first_token_time = time.time()
                if "response" in data:
                    token_count += 1
                if data.get("done"):
                    eval_count = data.get("eval_count", token_count)
                    eval_duration_ns = data.get("eval_duration", 0)
                    total_duration_ns = data.get("total_duration", 0)
                    prompt_eval_count = data.get("prompt_eval_count", 0)
                    prompt_eval_duration_ns = data.get("prompt_eval_duration", 0)

                    end_time = time.time()
                    total_wall_time = end_time - start_time
                    ttft = (first_token_time - start_time) if first_token_time else 0.0

                    tok_per_sec = (
                        (eval_count / (eval_duration_ns / 1e9))
                        if eval_duration_ns > 0
                        else (token_count / total_wall_time)
                    )
                    prompt_tok_per_sec = (
                        (prompt_eval_count / (prompt_eval_duration_ns / 1e9))
                        if prompt_eval_duration_ns > 0
                        else 0.0
                    )

                    print("\n" + "-" * 60)
                    print(f"Results Summary for: {model_name}")
                    print("-" * 60)
                    print(f"Tokens Generated      : {eval_count} tokens")
                    print(f"Generation Throughput : {tok_per_sec:.2f} tokens/second")
                    print(
                        f"Prompt Processing     : {prompt_tok_per_sec:.2f} tokens/second ({prompt_eval_count} prompt tokens)"
                    )
                    print(f"Time to First Token   : {ttft * 1000:.2f} ms")
                    print(f"Total Wall Clock Time : {total_wall_time:.2f} seconds")
                    print("=" * 60)
                    print(
                        "Benchmark completed successfully. The Zero-Dollar Dev (https://thezerodollardev.blogspot.com/)"
                    )
                    return

    except urllib.error.URLError as e:
        print(
            f"Connection Error: Could not connect to Ollama at {url}. Make sure Ollama is running."
        )
        print(f"Detail: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark local LLM performance.")
    parser.add_argument(
        "--model", type=str, default="deepseek-r1:7b", help="Model name in Ollama"
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1:11434", help="Ollama host address"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="Explain the difference between flash attention and standard multi-head attention in 3 paragraphs.",
        help="Benchmark prompt",
    )
    args = parser.parse_args()

    run_benchmark(args.model, args.host, args.prompt)
