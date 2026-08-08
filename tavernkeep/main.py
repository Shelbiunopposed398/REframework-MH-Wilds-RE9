from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

from tavernkeep.routers import models, backups, system
from tavernkeep.config import DASHBOARD_DIR

app = FastAPI(
    title="TavernKeep Manager API",
    description="Backend sidecar API for SillyTavern self-hosted stack management, Ollama model pulling, and backups.",
    version="1.0.0"
)

# Enable CORS for local management dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(system.router)
app.include_router(models.router)
app.include_router(backups.router)

# Serve Dashboard static frontend if available
if DASHBOARD_DIR.exists():
    app.mount("/manager", StaticFiles(directory=str(DASHBOARD_DIR), html=True), name="dashboard")

@app.get("/")
def read_root():
    return {
        "app": "TavernKeep Manager API",
        "status": "online",
        "docs": "/docs",
        "dashboard": "/manager/"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("tavernkeep.main:app", host="0.0.0.0", port=5000, reload=True)
