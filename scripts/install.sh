#!/usr/bin/env bash
set -e

echo "========================================================"
echo "   TavernKeep - SillyTavern Self-Hosted Stack          "
echo "========================================================"
echo ""

# Check Docker installation
if ! command -v docker &> /dev/null; then
    echo "[!] Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check Docker daemon running status
if ! docker info &> /dev/null; then
    echo "[!] Error: Docker daemon is not running. Please start Docker and try again."
    exit 1
fi

echo "[+] Docker Engine is running."
echo "[*] Building and launching TavernKeep stack..."

if command -v docker-compose &> /dev/null; then
    docker-compose up -d --build
else
    docker compose up -d --build
fi

echo ""
echo "========================================================"
echo "SUCCESS: TavernKeep Stack is running!"
echo " -> SillyTavern Web UI:     http://localhost:8000"
echo " -> TavernKeep Dashboard:   http://localhost:5000/manager/"
echo " -> Reverse Proxy (Caddy):  http://localhost:80"
echo "========================================================"
