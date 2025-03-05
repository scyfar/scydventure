from pathlib import Path
import json
import os
import subprocess
import sys
import shutil

# Check, if the source directory is provided
# The `source` must be the path to the directory with the version, which should have mods installed
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <source>")
    sys.exit(1)

source_dir = os.path.normpath(sys.argv[1])

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

# Delete existing mod files
mods_dir = f"{source_dir}/mods"
shutil.rmtree(mods_dir, ignore_errors=True)
os.makedirs(mods_dir, exist_ok=True)

with open(f"{source_dir}/.modlist.json", "r") as f:
    modlist = json.load(f)

for mod in modlist:
    # Add the mod using packwiz
    subprocess.run([
        "packwiz",
        "modrinth",
        "add",
        mod["url"],
        "--pack-file",
        f"{source_dir}/pack.toml",
        "--meta-folder-base",
        source_dir
    ], check=True)
