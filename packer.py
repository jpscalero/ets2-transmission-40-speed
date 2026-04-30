import zipfile
import os

MOD_FILENAME = "Universal_40_Speed_Transmission.scs"
SOURCE_DIR = "mod_files"
MANIFEST = "manifest.sii"

def package_mod():
    print(f"Packaging mod into {MOD_FILENAME}...")
    
    # Check if files exist
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: {SOURCE_DIR} not found.")
        return
    if not os.path.exists(MANIFEST):
        print(f"Error: {MANIFEST} not found.")
        return

    # Create ZIP with NO COMPRESSION (ZIP_STORED)
    with zipfile.ZipFile(MOD_FILENAME, 'w', zipfile.ZIP_STORED) as zip_file:
        # Add manifest.sii to root
        print("Adding manifest.sii...")
        zip_file.write(MANIFEST, arcname="manifest.sii")
        
        # Add 'def' folder content
        print("Adding definition files...")
        def_dir = os.path.join(SOURCE_DIR, "def")
        for root, dirs, files in os.walk(def_dir):
            for file in files:
                full_path = os.path.join(root, file)
                # Keep the 'def/...' structure
                arcname = os.path.relpath(full_path, SOURCE_DIR)
                zip_file.write(full_path, arcname=arcname)

    print(f"Success! Mod packaged as {MOD_FILENAME}")

if __name__ == "__main__":
    package_mod()
