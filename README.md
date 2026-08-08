# REFramework - Monster Hunter Wilds / RE9 (RE Engine)

**REFramework** is an open-source mod framework and scripting platform for Capcom RE Engine games - Monster Hunter Wilds, Resident Evil 9 (Requiem), and other RE Engine titles. Download the latest nightly build v1.5.9.2, fix black screen and crash issues after TU4, install Nexus mods, and enable VR support, FOV tweaks, and ray tracing adjustments. REFramework MH Wilds is the essential modding prerequisite for Monster Hunter Wilds PC mods, and REFramework RE9 brings the same powerful toolkit to Resident Evil Requiem.

<img width="4032" height="1152" alt="images1" src="https://github.com/user-attachments/assets/436e4717-e5ac-48dd-b47a-d855123a916d" />
<img width="3881" height="1108" alt="images2" src="https://github.com/user-attachments/assets/9b20206a-a706-4123-b9bf-7db3ef6e8f89" />


## Install
[Download `REFramework-Installer.zip`]()
---

<img width="385" height="190" alt="images3" src="https://github.com/user-attachments/assets/18ad44f6-b578-4378-bbe0-7e5c9b03f33d" />
<img width="3881" height="1108" alt="images4" src="https://github.com/user-attachments/assets/0fc827b6-d150-4866-b342-0389629513a3" />
<img width="2560" height="1440" alt="images5" src="https://github.com/user-attachments/assets/2c1063c1-3711-4ece-8ffd-2e1ce7f87dc8" />



## Key Features
- **Monster Hunter Wilds support** - latest nightly build v1.5.9.2 compatible with TU4 and beyond
- **RE9 / Resident Evil Requiem support** - FOV control, ray tracing tweaks, VR mode, and script loading
- **Lua scripting API** - write and load custom scripts that hook into the RE Engine's internal functions via the re. namespace
- **VR mod** - flat-to-VR conversion for supported titles via the UEVR/REFramework VR plugin
- **Nexus mod loading** - REFramework is a prerequisite for most MH Wilds and RE9 mods on Nexus Mods
- **Freecam** - fly around the game world with WASD + mouse look, perfect for screenshots
- **FOV changer** - adjustable field of view slider for MH Wilds and RE9, works in cutscenes
- **Crash and black screen fixes** - each nightly tracks RE Engine updates and patches compatibility issues
- **Debug overlay** - entity inspector, transform editor, spawn menu, and runtime memory viewer
- **GitHub nightly builds** - auto-updated builds tracking the latest RE Engine patches

<img width="1920" height="1080" alt="images6" src="https://github.com/user-attachments/assets/277b3d96-0575-43de-a354-dd90e9a7a4aa" />
<img width="411" height="117" alt="images7" src="https://github.com/user-attachments/assets/f4c1b202-0cb7-4fd0-b519-770c18d2de2b" />

## Getting Started
1. **Download** the latest reframework nightly using the button above.
2. **Extract** and copy `dinput8.dll` into your Monster Hunter Wilds or RE9 game folder (where the .exe is located).
3. **Launch the game** - the REFramework overlay appears automatically.
4. Press **Insert** to toggle the REFramework overlay menu.
5. Browse to **Mods** to manage your installed Lua scripts and Nexus mods.
6. For Nexus mods, place mod files in the `natives/` or `reframework/autorun/` subfolder.

**Tip:** For TU4 compatibility after a game update, always download the latest nightly from this repository. Old dinput8.dll versions will cause black screen or crash issues.

<img width="368" height="510" alt="images8" src="https://github.com/user-attachments/assets/f14558a8-8de1-4512-a18a-92e5fef3a086" />
<img width="519" height="634" alt="images9" src="https://github.com/user-attachments/assets/5a156ba1-6289-4625-b3e4-5f4f2e949a49" />
<img width="785" height="425" alt="images10" src="https://github.com/user-attachments/assets/0fdce70f-f92e-46a0-9003-853b7ed8b9ac" />

## REFramework MH Wilds - Fixing Common Issues

**Reframework MH Wilds black screen?**
Update to the latest nightly v1.5.9.2 - black screen issues are usually caused by a version mismatch after a Monster Hunter Wilds game patch. Delete the old dinput8.dll and replace it with the latest from this repository.

**Reframework MH Wilds crash / TU4 crash?**
After each major title update (TU1, TU2, TU3, TU4), REFramework needs a corresponding update. Download the latest nightly from this repo. v1.5.9.2 specifically fixes major frame pacing issues (micro stuttering) caused by the anti-tamper in Monster Hunter Wilds.

**Reframework MH Wilds not working after update?**
Delete the old `dinput8.dll` and replace it with the latest from this repository. Do not mix versions. Verify the file is in the same folder as `MonsterHunterWilds.exe`.

**Reframework MH Wilds uninstall?**
Simply delete `dinput8.dll` from your game folder. REFramework leaves no other files behind.

**Reframework MH Wilds ban risk?**
REFramework is a single-player mod framework. Using it in online sessions may trigger anti-cheat. Use offline or in your private lobby.

## REFramework RE9 Features

| Feature | Status |
|---|---|
| FOV control | Supported |
| Ray tracing tweaks | Supported |
| VR mode | Plugin required |
| Lua script loader | Supported |
| Nexus mod prerequisite | Supported |
| RE9 nightly updates | Supported |
| Freecam | Supported |
| Debug menu | Supported |

**Reframework RE9 download** - use the same archive above. It includes both the MH Wilds and RE9 builds.

**Reframework RE9 how to remove?** - delete `dinput8.dll` from the RE9 game folder.

**Reframework RE9 black screen?** - update to the latest nightly v1.5.9.2. Often caused by an RE Engine patch.

**Reframework RE9 VR?** - install the UEVR REFramework plugin after installing REFramework itself.

## Supported RE Engine Games

| Game | Support Status |
|---|---|
| Monster Hunter Wilds | Full support, nightly updates |
| Resident Evil 9 (Requiem) | Full support, FOV/VR/scripts |
| Resident Evil 4 (2023) | Mature, stable build |
| Resident Evil Village (RE8) | Stable, VR mod available |
| Resident Evil 2 (2019) | Legacy support |
| Resident Evil 3 (2020) | Legacy support |
| Resident Evil 7 | Legacy support |
| Dragon's Dogma 2 | Active support |
| Street Fighter 6 | Script support |
| Dead Rising Deluxe Remaster | Supported via DD2.zip |

## System Requirements
- **Windows 10 / 11** (64-bit)
- Monster Hunter Wilds or RE9 (Resident Evil Requiem) installed via Steam
- DirectX 12 capable GPU
- Administrator privileges recommended for first launch

## Security & Legal
REFramework is intended for single-player use. Using it in online sessions may violate Capcom's Terms of Service.

**Recommendations:**
- Download **only** from this official GitHub repository.
- Scan files on [VirusTotal](https://www.virustotal.com) before running.
- Always keep your nightly build up to date after RE Engine patches.
- Do not mix old and new dinput8.dll versions.

## License & Acknowledgments
### License
**REFramework** is shared under the **MIT License**.

**Copyright (C) 2026 reframeworkmod**

### Acknowledgments
- **praydog** for creating the original REFramework project and the entire RE Engine modding ecosystem.
- The MH Wilds and RE9 modding communities on Nexus Mods, GitHub, and the Monster Hunter Modding Discord.
- Contributors who reported compatibility issues after RE Engine patches and title updates.


<img width="739" height="415" alt="images11" src="https://github.com/user-attachments/assets/6fb1650f-ba60-445a-8a82-3a2653af19c7" />
<img width="590" height="338" alt="images12" src="https://github.com/user-attachments/assets/746b2200-03f4-48d2-af56-86233a019982" />
