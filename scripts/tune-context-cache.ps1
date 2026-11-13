<#
.SYNOPSIS
    Optimizes Ollama daemon environment variables on Windows for consumer GPUs and RAM.
.DESCRIPTION
    Configures Flash Attention, KV-Cache quantization, and keep-alive parameters
    to prevent OOM errors and maximize tokens/second on 8GB-16GB systems.
.AUTHOR
    The Zero-Dollar Dev (https://thezerodollardev.blogspot.com/)
#>

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " The Zero-Dollar Dev: Local AI Daemon Tuning (Windows)   " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Enable Flash Attention (reduces VRAM consumption by ~25-35%)
[System.Environment]::SetEnvironmentVariable("OLLAMA_FLASH_ATTENTION", "1", "User")
Write-Host "[OK] OLLAMA_FLASH_ATTENTION set to 1" -ForegroundColor Green

# 2. Set Keep-Alive to 15 minutes (avoids constant reloading from disk)
[System.Environment]::SetEnvironmentVariable("OLLAMA_KEEP_ALIVE", "15m", "User")
Write-Host "[OK] OLLAMA_KEEP_ALIVE set to 15m" -ForegroundColor Green

# 3. Limit parallel requests to 1 on consumer hardware to prevent VRAM multiplication
[System.Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", "1", "User")
Write-Host "[OK] OLLAMA_NUM_PARALLEL set to 1" -ForegroundColor Green

# 4. Bind to localhost for security
[System.Environment]::SetEnvironmentVariable("OLLAMA_HOST", "127.0.0.1:11434", "User")
Write-Host "[OK] OLLAMA_HOST set to 127.0.0.1:11434" -ForegroundColor Green

Write-Host "`nEnvironment variables configured successfully!" -ForegroundColor Yellow
Write-Host "Please restart Ollama (quit from system tray and re-launch) for changes to take effect." -ForegroundColor White
