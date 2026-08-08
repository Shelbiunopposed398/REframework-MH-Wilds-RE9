import os
from pathlib import Path

# Application configuration & environment settings
BASE_DIR = Path(__file__).resolve().parent.parent

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
SILLYTAVERN_DATA_DIR = Path(os.getenv("SILLYTAVERN_DATA_DIR", BASE_DIR / "data" / "sillytavern"))
BACKUP_DIR = Path(os.getenv("BACKUP_DIR", BASE_DIR / "backups"))
DASHBOARD_DIR = Path(os.getenv("DASHBOARD_DIR", BASE_DIR / "dashboard"))

# Ensure directories exist
SILLYTAVERN_DATA_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
