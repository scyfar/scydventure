from pathlib import Path
import json
import os
import subprocess
import sys
import shutil

#! > This script requires internet access <
#!   ====================================
#!
#! Add mods to the modpack using the `packwiz` tool.
#!
#! # Usage
#! ```
#! python add-mods.py <source_directory>
#! ```
#!
#! # Description
#! The required `<source_directory>` will be used to get the `.modlist.json` and where the modpack
#! base directory is assumed.
#!
#! All entries in the `.modlist.json` are looped and the command below is executed with the `url`
#! value of the entry.
#!
#! The `packwiz` command used is
#! ```
#! packwiz modrinth add <url> --pack-file "<source_directory>/pack.toml" --meta-folder-base <source_directory>
#! ```
#!
#! # References
#! - https://packwiz.infra.link/

# Verify required arguments
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <source_directory>")
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

os.chdir(source_dir)
subprocess.run(["packwiz", "refresh"], check=True)
