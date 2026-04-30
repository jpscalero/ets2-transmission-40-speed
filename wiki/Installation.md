# Installation & Deployment Guide

This guide covers everything from basic mod installation to advanced source-code builds for the Antigravity 40-Speed mod.

## 📥 Method 1: Standard Installation (Recommended)

1.  **Download**: Navigate to the [Releases](../../releases) section and download the latest `Antigravity_40_Speed.scs` file.
2.  **Locate Mod Folder**: Open your Windows Explorer and go to:
    `%USERPROFILE%\Documents\Euro Truck Simulator 2\mod`
3.  **Deploy**: Copy the `.scs` file into this folder.
4.  **Activate**:
    - Launch ETS2.
    - Open the **Mod Manager**.
    - Find "Antigravity 40-Speed Transmission Pack".
    - Click the arrow to activate and ensure it has **High Priority** (top of the list).

## 🛠️ Method 2: Developer / Source Build

If you wish to modify the truck list or the gear ratios yourself, follow these steps:

1.  **Prerequisites**: Install [Python 3.x](https://www.python.org/).
2.  **Clone**: `git clone https://github.com/jpscalero/ets2-transmission-40-speed.git`
3.  **Generate**:
    - Open a terminal in the project directory.
    - Run `python generator.py`.
    - This will create a `mod_files` directory with the updated `/def` structure.
4.  **Pack**:
    - Use a tool like 7-Zip or WinRAR.
    - Select the **contents** of the `mod_files` folder.
    - Add to archive, choose **ZIP** format, and **Store** (No compression) as the compression level.
    - Rename `.zip` to `.scs`.

## ❓ Troubleshooting

- **Mod not appearing?** Verify that you are on v1.58. Check the `game.log.txt` for "Entry point not found" errors.
- **Physics Glitches?** Ensure you are using an Antigravity-compatible engine mod. Standard engines might feel "too slow" to shift with 40 gears.

For more help, open a [Bug Report](../../issues).
