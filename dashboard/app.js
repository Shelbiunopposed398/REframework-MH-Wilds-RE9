// TavernKeep Web Dashboard Application Logic

const API_BASE = ""; // Relative URL since dashboard is served by TavernKeep backend

document.addEventListener("DOMContentLoaded", () => {
    initDashboard();
});

function initDashboard() {
    // Initial fetch
    checkHealth();
    fetchSystemStats();
    fetchModels();
    fetchBackups();

    // Set up polling intervals
    setInterval(checkHealth, 10000);
    setInterval(fetchSystemStats, 5000);

    // Event listeners
    document.getElementById("pull-model-form").addEventListener("submit", handlePullModel);
    document.getElementById("refresh-models-btn").addEventListener("click", fetchModels);
    document.getElementById("create-backup-btn").addEventListener("click", handleCreateBackup);
    document.getElementById("close-modal-btn").addEventListener("click", closeModal);
}

// System Health Checks
async function checkHealth() {
    try {
        const res = await fetch(`${API_BASE}/api/system/health`);
        const data = await res.json();
        
        const backendBadge = document.getElementById("backend-status");
        const ollamaBadge = document.getElementById("ollama-status");

        backendBadge.innerHTML = `<span class="dot online"></span> Backend: Online`;
        
        if (data.services.ollama_llm_engine === "online") {
            ollamaBadge.innerHTML = `<span class="dot online"></span> Ollama Engine: Online`;
        } else {
            ollamaBadge.innerHTML = `<span class="dot offline"></span> Ollama Engine: Offline`;
        }
    } catch (err) {
        document.getElementById("backend-status").innerHTML = `<span class="dot offline"></span> Backend: Offline`;
        document.getElementById("ollama-status").innerHTML = `<span class="dot offline"></span> Ollama Engine: Offline`;
    }
}

// Fetch System Stats (CPU, RAM, Disk)
async function fetchSystemStats() {
    try {
        const res = await fetch(`${API_BASE}/api/system/stats`);
        if (!res.ok) return;
        const data = await res.json();

        // CPU
        const cpuPercent = Math.round(data.cpu.usage_percent);
        document.getElementById("cpu-value").textContent = `${cpuPercent}%`;
        document.getElementById("cpu-bar").style.width = `${cpuPercent}%`;

        // RAM
        const ramPercent = Math.round(data.memory.used_percent);
        document.getElementById("ram-value").textContent = `${ramPercent}%`;
        document.getElementById("ram-bar").style.width = `${ramPercent}%`;

        // Disk
        const diskPercent = Math.round(data.disk.used_percent);
        document.getElementById("disk-value").textContent = `${diskPercent}%`;
        document.getElementById("disk-bar").style.width = `${diskPercent}%`;
    } catch (err) {
        // Silently ignore stat polling errors
    }
}

// Fetch Installed Models
async function fetchModels() {
    const grid = document.getElementById("models-grid");
    const countBadge = document.getElementById("models-count");
    
    try {
        const res = await fetch(`${API_BASE}/api/models`);
        if (!res.ok) throw new Error("Failed to fetch models");
        const models = await res.json();

        countBadge.textContent = models.length;

        if (models.length === 0) {
            grid.innerHTML = `<div class="empty-state">No local LLM models installed. Use the pull form above to download one.</div>`;
            return;
        }

        grid.innerHTML = models.map(m => {
            const sizeGB = (m.size / (1024 * 1024 * 1024)).toFixed(2);
            return `
                <div class="model-card">
                    <div class="model-card-header">
                        <div class="model-name">🤖 ${escapeHtml(m.name)}</div>
                        <span class="model-size">${sizeGB} GB</span>
                    </div>
                    <div class="model-card-actions">
                        <button class="btn secondary small" onclick="showModelInfo('${escapeHtml(m.name)}')">ℹ️ Details</button>
                        <button class="btn danger small" onclick="deleteModel('${escapeHtml(m.name)}')">🗑️ Delete</button>
                    </div>
                </div>
            `;
        }).join("");
    } catch (err) {
        grid.innerHTML = `<div class="empty-state" style="color: var(--accent-danger)">Error loading models: ${err.message}</div>`;
    }
}

// Pull New Model
async function handlePullModel(e) {
    e.preventDefault();
    const input = document.getElementById("model-name-input");
    const btn = document.getElementById("pull-btn");
    const statusMsg = document.getElementById("pull-status-message");

    const modelName = input.value.trim();
    if (!modelName) return;

    btn.disabled = true;
    showStatus(statusMsg, "info", `Pulling '${modelName}' from Ollama library... This might take a few minutes.`);

    try {
        const res = await fetch(`${API_BASE}/api/models/pull`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: modelName })
        });

        const data = await res.json();

        if (res.ok && data.status === "success") {
            showStatus(statusMsg, "success", `Successfully pulled '${modelName}'!`);
            input.value = "";
            fetchModels();
        } else {
            showStatus(statusMsg, "error", data.detail || data.message || "Failed to pull model");
        }
    } catch (err) {
        showStatus(statusMsg, "error", `Network error: ${err.message}`);
    } finally {
        btn.disabled = false;
    }
}

// Delete Model
async function deleteModel(modelName) {
    if (!confirm(`Are you sure you want to delete the model '${modelName}'?`)) return;

    try {
        const res = await fetch(`${API_BASE}/api/models/${encodeURIComponent(modelName)}`, {
            method: "DELETE"
        });
        const data = await res.json();

        if (res.ok && data.status === "success") {
            fetchModels();
        } else {
            alert(`Delete failed: ${data.detail || data.message}`);
        }
    } catch (err) {
        alert(`Error deleting model: ${err.message}`);
    }
}

// Show Model Detailed Info Modal
async function showModelInfo(modelName) {
    const modal = document.getElementById("info-modal");
    const modalTitle = document.getElementById("modal-title");
    const modalBody = document.getElementById("modal-json-content");

    modalTitle.textContent = `Model Info: ${modelName}`;
    modalBody.textContent = "Loading model details...";
    modal.classList.remove("hidden");

    try {
        const res = await fetch(`${API_BASE}/api/models/${encodeURIComponent(modelName)}/info`);
        if (!res.ok) throw new Error("Could not retrieve model details.");
        const data = await res.json();
        modalBody.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        modalBody.textContent = `Error: ${err.message}`;
    }
}

function closeModal() {
    document.getElementById("info-modal").classList.add("hidden");
}

// Backups Management
async function fetchBackups() {
    const listBody = document.getElementById("backups-list");

    try {
        const res = await fetch(`${API_BASE}/api/backups`);
        if (!res.ok) throw new Error("Failed to fetch backups list");
        const backups = await res.json();

        if (backups.length === 0) {
            listBody.innerHTML = `<tr><td colspan="4" class="text-center" style="color: var(--text-muted)">No backups found. Click 'Create Backup' to create one.</td></tr>`;
            return;
        }

        listBody.innerHTML = backups.map(b => {
            const sizeMB = (b.size_bytes / (1024 * 1024)).toFixed(2);
            return `
                <tr>
                    <td>📦 <strong>${escapeHtml(b.filename)}</strong></td>
                    <td>${sizeMB} MB</td>
                    <td>${escapeHtml(b.modified_at)}</td>
                    <td class="text-right">
                        <a href="${API_BASE}/api/backups/${encodeURIComponent(b.filename)}/download" class="btn secondary small" download>⬇️ Download</a>
                        <button class="btn success small" onclick="restoreBackup('${escapeHtml(b.filename)}')">🔄 Restore</button>
                        <button class="btn danger small" onclick="deleteBackup('${escapeHtml(b.filename)}')">🗑️ Delete</button>
                    </td>
                </tr>
            `;
        }).join("");
    } catch (err) {
        listBody.innerHTML = `<tr><td colspan="4" class="text-center" style="color: var(--accent-danger)">Error: ${err.message}</td></tr>`;
    }
}

async function handleCreateBackup() {
    const tagInput = document.getElementById("backup-tag-input");
    const label = tagInput.value.trim();

    try {
        const res = await fetch(`${API_BASE}/api/backups`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: label || null })
        });
        const data = await res.json();

        if (res.ok && data.status === "success") {
            tagInput.value = "";
            fetchBackups();
        } else {
            alert(`Backup failed: ${data.detail || data.message}`);
        }
    } catch (err) {
        alert(`Error creating backup: ${err.message}`);
    }
}

async function restoreBackup(filename) {
    if (!confirm(`Restore SillyTavern data from '${filename}'? Current characters and chats will be overwritten.`)) return;

    try {
        const res = await fetch(`${API_BASE}/api/backups/${encodeURIComponent(filename)}/restore`, {
            method: "POST"
        });
        const data = await res.json();

        if (res.ok && data.status === "success") {
            alert("Backup restored successfully!");
            fetchBackups();
        } else {
            alert(`Restore failed: ${data.detail || data.message}`);
        }
    } catch (err) {
        alert(`Error restoring backup: ${err.message}`);
    }
}

async function deleteBackup(filename) {
    if (!confirm(`Permanently delete backup '${filename}'?`)) return;

    try {
        const res = await fetch(`${API_BASE}/api/backups/${encodeURIComponent(filename)}`, {
            method: "DELETE"
        });
        const data = await res.json();

        if (res.ok && data.status === "success") {
            fetchBackups();
        } else {
            alert(`Delete failed: ${data.detail || data.message}`);
        }
    } catch (err) {
        alert(`Error deleting backup: ${err.message}`);
    }
}

// Helpers
function showStatus(element, type, text) {
    element.className = `status-msg ${type}`;
    element.textContent = text;
}

function escapeHtml(str) {
    return str.replace(/[&<>"']/g, match => {
        const escape = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;'
        };
        return escape[match];
    });
}
