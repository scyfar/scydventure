from pathlib import Path
import os
import subprocess
import sys
import toml

# Check, if the new version is provided
# The `new_version` must follow the format of `<pack-version>_<minecraft-version>_<loader>`
# An optional `file_name` can be provided
if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(__file__)} <new_version>")
    sys.exit(1)

new_version = sys.argv[1].strip().lower()
# Strip leading 'v'
if new_version.startswith("v"):
    new_version = new_version[1:]

# Deconstruct the new_version
pack_version, mc_version, loader = new_version.split("_")

source_dir = os.path.normpath(f"./packwiz/{mc_version}/{loader}")
target_dir = os.path.normpath(".")

file_name = ""
if sys.argv[2]:
    file_name = sys.argv[2].strip()

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

# Check, if target directory exists
if not Path(target_dir).exists():
    print(f"Error: Target directory '{target_dir}' does not exist.")
    sys.exit(1)

# Load pack.toml file
with open(f"{source_dir}/pack.toml", "r") as f:
    config = toml.load(f)

# Extract name and version from pack.toml
config_name = config["name"]
config_version = config["version"]

# Export the mrpack file using packwiz
os.chdir(source_dir)
if not file_name:
    file_name = f"{config_name}-{config_version}.mrpack"

subprocess.run([
    "packwiz",
    "modrinth",
    "export",
    "--output",
    f"../../../{target_dir}/{file_name}"
], check=True)
