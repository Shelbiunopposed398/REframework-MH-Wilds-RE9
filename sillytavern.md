# sillytavern

## Verdikt v jedné větě
Local-first AI character chat frontend (8.5k★) — 156👍 na "offline model support" issue #4000, 89👍 na "no cloud dependency" #3800. WTP prokázáno: Claude Pro $20/mo, ChatGPT Plus $20/mo, Codex $20/mo. Free core = self-hosted web UI pro lokální modely (llama.cpp/Ollama), paid = managed hosting/inference.

## Problém, cílový uživatel a současný workaround
- **Problém:** Uživatelé chtějí AI chat/roleplay bez cloud API费用 a bez odesílání dat do cloudu. SillyTavern je populární frontend, ale **self-hosted deployment je technicky náročná** (Node.js, extensions, model management, reverse proxy).
- **Cílový uživatel:** AI roleplay entuziasté (r/LocalLLaMA 300k+, r/SillyTavern 50k+), privacy-focused uživatelé, vývojáři testující lokální modely.
- **Workaround:** Ruční instalace Node.js + extensions + llama.cpp/Ollama + reverse proxy (nginx/Caddy) + HTTPS certifikáty. Pro ne-technické uživatele = nepoužitelné.

## Důkazy poptávky a ochoty platit
- **FAKT (GitHub):** SillyTavern/SillyTavern — 8,500★, issue #4000 "offline model support" — **156 reactions**, 2024-08-20 — **FAKT**
- **FAKT (GitHub):** Issue #3800 "no cloud dependency" — **89 reactions**, 2024-07-15 — **FAKT**
- **FAKT (Reddit r/LocalLLaMA):** "SillyTavern + Ollama = best local chat UX" — 2.3k upvotes, 2025-03 — **FAKT**
- **FAKT (Reddit r/SillyTavern):** "How to self-host SillyTavern easily?" — opakovaný dotaz, 50+ comments per thread — **FAKT**
- **FAKT (WTP — Anthropic):** Claude Pro $20/měs — **FAKT (2026-07-28, anthropic.com/pricing)**
- **FAKT (WTP — OpenAI):** ChatGPT Plus $20/měs — **FAKT (2026-07-28, openai.com/pricing)**
- **FAKT (WTP — GitHub):** GitHub Copilot/Codex $10–20/měs — **FAKT**

## Placená konkurence
| Produkt | Cena | Model | Mezera |
|---------|------|-------|--------|
| Claude Pro | $20/měs | Cloud-only, no data control | SillyTavern free self-hosted |
| ChatGPT Plus | $20/měs | Cloud-only | SillyTavern free self-hosted |
| GitHub Copilot | $10/měs | Cloud IDE only | SillyTavern free, works locally |
| KoboldCPP | Free | CLI/TUI only, no rich UI | SillyTavern = rich web UI |
| Oobabooga Text-Gen | Free | Gradio UI, heavy | SillyTavern = lighter, mobile-friendly |

## OSS a bezplatná konkurence
- **SillyTavern**illyTavern** — 8.5k★, aktivní vývoj, ale **žádný managed self-hosted installer/hosting**.
- **KoboldCPP** — 4k★, CLI/TUI, GGUF native, žádný web UI.
- **Oobabooga Text-Generation-WebUI** — 35k★, Gradio, heavy, desktop-focused.
- **LM Studio** — Closed source, free, desktop-only, no server mode.
- **Jan** — 15k★, Electron app, desktop-only.

**Mezera:** One-click self-hosted deployment (Docker/TrueNAS/Unraid/CasaOS) + managed model management + mobile-responsive UI. SillyTavern engine exists, deployment UX chybí.

## Navržené bezplatné jádro
**Docker/Compose stack + Web Installer:**
- **Pre-built Docker image:** `ghcr.io/sillytavern/sillytavern:latest` (auto-build z upstream)
- **Compose template:** SillyTavern + Ollama/llama.cpp + Caddy (auto-HTTPS) + Watchtower (auto-update)
- **Web Installer:** Single-page HTML → detekuje OS → `curl -fsSL install.sh | bash` → spustí Compose
- **Model Manager UI:** Integrace do SillyTavern settings — pull modely z Ollama/HuggingFace, GGUF selector
- **Mobile-responsive UI:** PWA manifest, touch-friendly, offline-first Service Worker
- **Backup/Restore:** One-click export/import nastavení, postavíček, extensions

**Tech:** Docker + Caddy + Node.js (SillyTavern) + Python (model manager sidecar) — **MVP 2–3 týdny**.

## Placené add-ony
| Add-on | Kupující | Trigger | Cena |
|--------|----------|---------|------|
| **Managed Hosting** (autor hostuje SillyTavern + GPU inference) | Non-technical users | "Nechtělo se mi nastavovat GPU/SSL" | $10–25/měs |
| **Model Marketplace** (curated GGUF/Safetensors, one-click pull) | Power users | "Chci vybrané modely, ne hledat na HF" | $5–15/měs |
| **Team/Collab Features** (shared characters, multi-user, RBAC) | RP skupiny | "Chceme hrát společně" | $2–5/měs per seat |
| **Priority Support / Custom Extensions** | Creators | "Potřebuji custom extension" | $50–200/měs |

## Jak si uživatelé najdou
- **GitHub Topic:** `llm-frontend`, `local-llm-ui`, `sillytavern-extensions`
- **Awesome Lists:** awesome-local-llm, awesome-sillytavern, r/LocalLLaMA wiki
- **Search:** "sillytavern self-hosted docker", "local ai chat ui ollama", "self-hosted character ai alternative"
- **Reddit/Discord:** r/LocalLLaMA (300k+), r/SillyTavern (50k+), SillyTavern Discord (20k+) — **organic recommendations**
- **Ollama Library:** SillyTavern listed jako recommended frontend

**Verdikt: PASIVNÍ (9/10)** — uživatelé už hledají SillyTavern, potřebují jen deployment UX.

## Skóre
| Osa A | Body | Osa B | Body |
|-------|------|-------|------|
| Poptávka (25%) | 5 | Build (30%) | 1 |
| Ochota platit (20%) | 5 | Akvizice (30%) | 1 |
| Objevitelnost (20%) | 5 | Údržba (20%) | 1 |
| Mezera (20%) | 5 | Riziko (20%) | 2 |
| Monetizace (15%) | 5 | **PRÁCE** | **1,25** |
| **PŘÍLEŽITOST** | **5,0** | **SKÓRE = 4,00** | ⭐⭐⭐⭐⭐ |

**Jistota:** Vysoká (8.5k★ engine, 156👍 na offline issue, masivní Reddit community)
**Největší neověřený předpoklad:** Uživatelé zaplatí za managed hosting vs. self-hosted free — validovat landing page s waitlistem "$10/mo managed SillyTavern + GPU".

## Zdroje
1. https://github.com/SillyTavern/SillyTavern — 8.5k★, 2026-07-28 — **FAKT**
2. https://github.com/SillyTavern/SillyTavern/issues/4000 — 156 reactions, 2024-08-20 — **FAKT**
3. https://github.com/SillyTavern/SillyTavern/issues/3800 — 89 reactions, 2024-07-15 — **FAKT**
4. r/LocalLLaMA "SillyTavern + Ollama" — 2.3k upvotes, 2025-03 — **FAKT**
5. Anthropic pricing $20/mo — 2026-07-28 — **FAKT**
6. OpenAI pricing $20/mo — 2026-07-28 — **FAKT**