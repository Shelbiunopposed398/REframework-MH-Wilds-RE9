# TavernKeep One-Click Installer for Windows (PowerShell)
$ErrorActionPreference = "Stop"

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "   TavernKeep - SillyTavern Self-Hosted Stack          " -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Check Docker installation
$dockerInstalled = Get-Command docker -ErrorAction SilentlyContinue
if (-not $dockerInstalled) {
    Write-Host "[!] Error: Docker is not installed or not in PATH. Please install Docker Desktop." -ForegroundColor Red
    Exit 1
}

# Check Docker daemon running status
Write-Host "[*] Checking Docker Desktop service status..." -ForegroundColor Yellow
$dockerInfo = & docker info 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[!] Error: Docker Desktop is not running." -ForegroundColor Red
    Write-Host "    Please start Docker Desktop application on your PC and try again." -ForegroundColor Red
    Exit 1
}

Write-Host "[+] Docker Engine is running." -ForegroundColor Green
Write-Host "[*] Building and launching TavernKeep stack..." -ForegroundColor Yellow

docker compose up -d --build

Write-Host ""
Write-Host "========================================================" -ForegroundColor Green
Write-Host "SUCCESS: TavernKeep Stack is running!" -ForegroundColor Green
Write-Host " -> SillyTavern Web UI:     http://localhost:8000" -ForegroundColor White
Write-Host " -> TavernKeep Dashboard:   http://localhost:5000/manager/" -ForegroundColor White
Write-Host " -> Reverse Proxy (Caddy):  http://localhost:80" -ForegroundColor White
Write-Host "========================================================" -ForegroundColor Green
