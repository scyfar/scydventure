from pathlib import Path
import os
import subprocess
import sys
import toml

# Check, if the source and target directories are provided
# The `source` must be the path to the directory with the version, which should be exported
# The `target` must be the directory where the `mrpack` should be created
if len(sys.argv) != 3:
    print(f"Usage: python {os.path.basename(__file__)} <source> <target>")
    sys.exit(1)

source_dir = os.path.normpath(sys.argv[1])
target_dir = os.path.normpath(sys.argv[2])
root_dir = os.getcwd()

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
name = config["name"]
version = config["version"]

# Export the mrpack file using packwiz
os.chdir(source_dir)
subprocess.run([
    "packwiz",
    "modrinth",
    "export",
    "--output",
    f"{root_dir}/{target_dir}/{name}-{version}.mrpack"
], check=True)
