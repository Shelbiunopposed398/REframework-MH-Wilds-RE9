# 🏰 TavernKeep - SillyTavern Self-Hosted Stack & Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-blue)](https://www.docker.com/)
[![Build Status](https://img.shields.io/badge/CI-Passing-brightgreen)](#automated-testing)

**TavernKeep** is a local-first, zero-config self-hosted launcher, orchestration stack, and management dashboard for [SillyTavern](https://github.com/SillyTavern/SillyTavern) paired with [Ollama](https://ollama.com/) local LLMs.

---

## ✨ Features

- **🚀 1-Click Orchestration:** Spin up SillyTavern, Ollama, Caddy (auto-HTTPS proxy), and TavernKeep in a single command.
- **🤖 LLM Model Manager:** Download models from the Ollama library or HuggingFace, view parameter info, and delete old models directly from the web UI.
- **📦 One-Click Backup & Restore:** Export and import all SillyTavern characters, chats, and configurations into unified `.zip` archives.
- **📊 System Resource Gauges:** Real-time monitoring of CPU, RAM, and Disk utilization.
- **📱 Responsive Glassmorphic Dashboard:** Built with modern Vanilla CSS, dark mode aesthetics, and zero heavy frontend frameworks.

---

## ⚡ Quick Start

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### 1. Clone Repository
```bash
git clone https://github.com/your-username/tavernkeep.git
cd tavernkeep
```

### 2. Run Installer

#### On Windows (PowerShell):
```powershell
.\scripts\install.ps1
```

#### On Linux / macOS (Bash):
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

---

## 🌐 Access Endpoints

Once the stack is running:

| Service | Local URL | Description |
|---|---|---|
| **SillyTavern Web UI** | `http://localhost:8000` | Main character chat interface |
| **TavernKeep Dashboard** | `http://localhost:5000/manager/` | Model management & backup dashboard |
| **Caddy Reverse Proxy** | `http://localhost:80` | Unified gateway |

---

## 🏗️ Project Architecture

```
sillytavern/
├── docker-compose.yml       # Container orchestration (SillyTavern + Ollama + Sidecar + Caddy)
├── Caddyfile                # Gateway routing configuration
├── tavernkeep/              # Python FastAPI Sidecar backend
│   ├── main.py              # Application entry point
│   ├── config.py            # Environment & folder configurations
│   ├── services/            # Ollama API & Zip backup services
│   ├── routers/             # API routes (/api/models, /api/backups, /api/system)
│   └── tests/               # Automated Pytest suite
├── dashboard/               # Frontend Control Panel (HTML5, CSS3, JS)
└── scripts/                 # One-click installation scripts (install.sh, install.ps1)
```

---

## 🧪 Automated Testing

TavernKeep includes a full test suite built with `pytest`. To run tests locally:

```bash
# Create virtual environment & install requirements
python -m venv venv
.\venv\Scripts\python -m pip install -r tavernkeep/requirements.txt

# Run pytest suite
.\venv\Scripts\python -m pytest tavernkeep/tests -v
```

---

## 📜 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
