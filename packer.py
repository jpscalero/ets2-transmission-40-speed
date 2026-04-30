import zipfile
import os

# ==========================================
# APEX DRIVE SYSTEMS - MOD PACKER
# ==========================================

MOD_FILENAME = "Apex_Drive_Systems_40_Speed.scs"
SOURCE_DIR = "mod_files"
FILES_TO_INCLUDE = ["manifest.sii", "description.txt", "mod_icon.png"]

def package_mod():
    print(f"=== Apex Drive Systems: Mod Packer ===")
    print(f"Target: {MOD_FILENAME}")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: {SOURCE_DIR} not found. Run generator.py first.")
        return

    with zipfile.ZipFile(MOD_FILENAME, 'w', zipfile.ZIP_STORED) as zip_file:
        for filename in FILES_TO_INCLUDE:
            if os.path.exists(filename):
                print(f"Adding {filename}...")
                zip_file.write(filename, arcname=filename)
            else:
                print(f"Warning: {filename} not found, skipping.")
        
        print("Adding definition files (def/)...")
        def_dir = os.path.join(SOURCE_DIR, "def")
        if os.path.exists(def_dir):
            for root, dirs, files in os.walk(def_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, SOURCE_DIR)
                    zip_file.write(full_path, arcname=arcname)
        else:
            print("Error: 'def' directory not found inside mod_files.")

    print(f"Success! Apex Mod packaged as {MOD_FILENAME}")

if __name__ == "__main__":
    package_mod()
