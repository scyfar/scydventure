from pathlib import Path
import json
import os
import sys
import toml

#! > This script should only be used for automation <
#!   ==============================================
#!
#! Generates the JSON array used for the Modrinth dependency information.
#!
#! # Usage
#! ```
#! python _dependency-information.py `<git_tag>`
#! ```
#!
#! # Description
#! The required `<git_tag>` must match this template:
#! `<pack-version>_<minecraft-version>_<loader-name>`.
#!
#! The script uses the provided `git_tag` to find the source files.
#!
#! The source files are expected to be in a directory matching the template
#! `./packwiz/{<minecraft-version>}/{<loader-name>}/mods`.

# Verify required arguments
if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(__file__)} <git_tag>")
    sys.exit(1)

git_tag = sys.argv[1].strip().lower()
# Strip leading 'v'
if git_tag.startswith("v"):
    git_tag = git_tag[1:]

# Deconstruct the git_tag
pack_version, mc_version, loader = git_tag.split("_")

source_dir = os.path.normpath(f"./packwiz/{mc_version}/{loader}/mods")

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

# Initialize with optional mods
# HVnmMxH1: Complementary Shaders - Reimagined
json_result = [{"project_id": "HVnmMxH1", "dependency_type": "optional"}]

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path) and filename.endswith(".pw.toml"):
        try:
            config = toml.load(file_path)
            mod_id = config.get("update", {}).get("modrinth", {}).get("mod-id")
            version = config.get("update", {}).get("modrinth", {}).get("version")
            json_result.append({"project_id": mod_id, "version": version, "dependency_type": "embedded"})
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

print(json.dumps(json_result, indent=None))
