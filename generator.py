import os
import shutil
import logging

# --- CONFIGURATION (ETS2 v1.58 Internal Names) ---
TRUCKS = {
    "DAF XF": "daf.xf",
    "DAF XF 105": "daf.xf_105",
    "DAF 2021": "daf.2021",
    "DAF XD": "daf.xd",
    "Iveco Stralis": "iveco.stralis",
    "Iveco Hi-Way": "iveco.hiway",
    "Iveco S-Way": "iveco.sway",
    "MAN TGX": "man.tgx",
    "MAN TGX Euro 6": "man.tgx_euro6",
    "MAN TGX 2020": "man.tgx_2020",
    "MB Actros": "mercedes.actros",
    "MB New Actros": "mercedes.actros2014",
    "Renault Magnum": "renault.magnum",
    "Renault Premium": "renault.premium",
    "Renault T": "renault.t",
    "Scania R 2009": "scania.r",
    "Scania Streamline": "scania.streamline",
    "Scania R 2016": "scania.r_2016",
    "Scania S 2016": "scania.s_2016",
    "Volvo FH16 2009": "volvo.fh16",
    "Volvo FH16 2012": "volvo.fh16_2012"
}

PRICE = 2
UNLOCK = 0
BASE_DIR = "mod_files"
MOD_ID = "ag40" # Antigravity 40-Speed ID

# Setup Logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("ModAuditor")

# --- TEMPLATE ---
TRANSMISSION_TEMPLATE = """SiiNunit
{{
accessory_transmission_data : {id}.{truck}.transmission
{{
	name: "Antigravity 40-Speed {truck_display}"
	price: {price}
	unlock: {unlock}
	icon: "transmission_generic"

	differential_ratio: 3.0

{ratios_forward}

	ratios_reverse[0]: -15.0
	ratios_reverse[1]: -10.0
	ratios_reverse[2]: -5.0

	retarder: 3
}}
}}
"""

def generate_ratios(count):
    ratios = []
    # 40 gears: smooth progression from 15.0 to 0.5
    start = 15.0
    end = 0.5
    step = (start - end) / (count - 1)
    for i in range(count):
        ratio = start - (i * step)
        ratios.append(f"\tratios_forward[{i}]: {ratio:.2f}")
    return "\n".join(ratios)

def main():
    logger.info("Starting mod audit and repair for v1.58...")
    
    # Cleanup and folder creation
    if os.path.exists(BASE_DIR):
        shutil.rmtree(BASE_DIR)
        logger.info(f"Cleaned up {BASE_DIR}")
    
    ratios_str = generate_ratios(40)
    total_processed = 0

    for display_name, internal_name in TRUCKS.items():
        # Path: def/vehicle/truck/[internal_name]/transmission/
        path = os.path.join(BASE_DIR, "def", "vehicle", "truck", internal_name, "transmission")
        os.makedirs(path, exist_ok=True)
        
        # Header formatting: ag40.scania.s_2016.transmission
        # We use the raw internal name as requested
        content = TRANSMISSION_TEMPLATE.format(
            id=MOD_ID,
            truck=internal_name,
            truck_display=display_name,
            price=PRICE,
            unlock=UNLOCK,
            ratios_forward=ratios_str
        )
        
        file_name = f"{MOD_ID}_transmission.sii"
        file_path = os.path.join(path, file_name)
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Generated transmission for: {display_name} -> {internal_name}")
            total_processed += 1
        except Exception as e:
            logger.error(f"Failed to generate for {display_name}: {e}")

    logger.info(f"Audit Complete. Total trucks processed: {total_processed}")
    logger.info(f"Structure generated in: {os.path.abspath(BASE_DIR)}")

if __name__ == "__main__":
    main()
