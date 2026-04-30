import zipfile
import os

MOD_FILENAME = "Antigravity_40_Speed_Transmission.scs"
SOURCE_DIR = "mod_files"

def package_mod():
    print(f"=== Antigravity Mod Packer ===")
    print(f"Target: {MOD_FILENAME}")
    
    # Check if directories exist
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: {SOURCE_DIR} not found. Run generator.py first.")
        return

    # Create ZIP with NO COMPRESSION (ZIP_STORED) as per SCS requirements
    with zipfile.ZipFile(MOD_FILENAME, 'w', zipfile.ZIP_STORED) as zip_file:
        # Add root files
        for filename in FILES_TO_INCLUDE:
            if os.path.exists(filename):
                print(f"Adding {filename}...")
                zip_file.write(filename, arcname=filename)
            else:
                print(f"Warning: {filename} not found, skipping.")
        
        # Add 'def' folder content recursively
        print("Adding definition files (def/)...")
        def_dir = os.path.join(SOURCE_DIR, "def")
        if os.path.exists(def_dir):
            for root, dirs, files in os.walk(def_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    # The structure inside the zip must start with 'def/'
                    arcname = os.path.relpath(full_path, SOURCE_DIR)
                    zip_file.write(full_path, arcname=arcname)
        else:
            print("Error: 'def' directory not found inside mod_files.")

    print(f"Success! Mod packaged as {MOD_FILENAME}")

if __name__ == "__main__":
    package_mod()
