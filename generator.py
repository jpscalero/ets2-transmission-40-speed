import os
import logging

# ==========================================
# APEX DRIVE SYSTEMS - CONFIGURACIÓN V1.58
# ==========================================

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("Apex_Systems_Auditor")

# ID de accesorio (Máximo 12 caracteres para evitar errores de motor)
ACCESSORY_ID = "apex40"

# Lista de camiones nativos ETS2 v1.58
TRUCKS = [
    {"internal_name": "daf.2021", "display_name": "DAF 2021"},
    {"internal_name": "daf.xd", "display_name": "DAF XD"},
    {"internal_name": "daf.xf", "display_name": "DAF XF"},
    {"internal_name": "daf.xf_euro6", "display_name": "DAF XF Euro 6"},
    {"internal_name": "iveco.hiway", "display_name": "Iveco Hi-Way"},
    {"internal_name": "iveco.stralis", "display_name": "Iveco Stralis"},
    {"internal_name": "iveco.sway", "display_name": "Iveco S-Way"},
    {"internal_name": "man.tgx", "display_name": "MAN TGX"},
    {"internal_name": "man.tgx_euro6", "display_name": "MAN TGX Euro 6"},
    {"internal_name": "man.tgx_2020", "display_name": "MAN TGX 2020"},
    {"internal_name": "mercedes.actros", "display_name": "Mercedes-Benz Actros"},
    {"internal_name": "mercedes.actros2014", "display_name": "Mercedes-Benz New Actros"},
    {"internal_name": "renault.magnum", "display_name": "Renault Magnum"},
    {"internal_name": "renault.premium", "display_name": "Renault Premium"},
    {"internal_name": "renault.t", "display_name": "Renault Range T"},
    {"internal_name": "renault.etech_t", "display_name": "Renault E-Tech T"},
    {"internal_name": "scania.r", "display_name": "Scania R 2009"},
    {"internal_name": "scania.streamline", "display_name": "Scania Streamline"},
    {"internal_name": "scania.r_2016", "display_name": "Scania R 2016"},
    {"internal_name": "scania.s_2016", "display_name": "Scania S 2016"},
    {"internal_name": "volvo.fh16", "display_name": "Volvo FH16 2009"},
    {"internal_name": "volvo.fh16_2012", "display_name": "Volvo FH16 2012"}
]

# Plantilla de la transmisión .sii (SCS V1.58 Compliant)
TRANSMISSION_TEMPLATE = """SiiNunit
{{
accessory_transmission_data : {id}.{truck}.transmission
{{
	name: "Apex 40-Speed High-Performance"
	price: 2
	unlock: 0
	icon: "transmission_generic"

	# Gears: 40 Forward, 3 Reverse
{ratios}

	# Transmission Ratios Logic
	# Optimized for Apex Drive Systems - Stability Protocol
}}
}}
"""

def generate_ratios():
    """Genera 40 marchas lineales de 15.00 a 0.50."""
    ratios = []
    start_ratio = 15.0
    end_ratio = 0.5
    steps = 40
    decrement = (start_ratio - end_ratio) / (steps - 1)
    
    for i in range(steps):
        ratio = start_ratio - (i * decrement)
        ratios.append(f"\tratios_forward[{i}]: {ratio:.2f}")
    
    # Reverse ratios (Standard Heavy Duty)
    ratios.append("\tratios_reverse[0]: 12.00")
    ratios.append("\tratios_reverse[1]: 9.00")
    ratios.append("\tratios_reverse[2]: 6.00")
    
    return "\n".join(ratios)

def run_generator():
    logger.info("Iniciando Generación de Apex Drive Systems v1.58...")
    base_dir = "mod_files/def/vehicle/truck"
    ratios_content = generate_ratios()
    
    total_processed = 0
    for truck in TRUCKS:
        internal_name = truck["internal_name"]
        display_name = truck["display_name"]
        
        # Ruta SCS: /def/vehicle/truck/[nombre]/transmission/
        target_dir = os.path.join(base_dir, internal_name, "transmission")
        os.makedirs(target_dir, exist_ok=True)
        
        file_path = os.path.join(target_dir, "apex_40_speed.sii")
        
        try:
            content = TRANSMISSION_TEMPLATE.format(
                id=ACCESSORY_ID,
                truck=internal_name,
                ratios=ratios_content
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            total_processed += 1
        except Exception as e:
            logger.error(f"Error procesando {display_name}: {e}")

    logger.info(f"Generación completada. {total_processed} archivos creados en {base_dir}")

if __name__ == "__main__":
    run_generator()
