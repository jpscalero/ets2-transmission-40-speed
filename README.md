# ETS2 40-Speed Transmission Mod (v1.58)

Automated transmission mod for Euro Truck Simulator 2 (v1.58). This mod adds a high-performance 40-speed transmission to all native trucks in the game.

## Features
- **40 Forward Gears**: Smooth ratio progression from 15.00 to 0.50.
- **3 Reverse Gears**: Optimized for heavy maneuvering.
- **Full Compatibility**: Works with all 21 native trucks in v1.58 (Scania, Volvo, MAN, DAF, Iveco, Renault, MB).
- **Early Access**: Available from level 0 for only 2 credits.
- **SCS Compliant**: Validated folder structure and syntax for Prism3D.

## How to Install
1. Download the latest `.scs` file from the [Releases](link-to-releases) (if available) or generate it yourself.
2. Place the file in your `Documents/Euro Truck Simulator 2/mod` folder.
3. Activate the mod in the Game Mod Manager.

## For Developers
This mod is generated using a Python script. To modify or add new trucks:
1. Edit `generator.py`.
2. Run the script:
   ```bash
   python generator.py
   ```
3. The output will be in the `mod_files/` directory.

## Credits
- Created by Antigravity Modding Auditor.
- Project lead: [jpscalero](https://github.com/jpscalero).
