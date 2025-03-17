from pathlib import Path
import os
import subprocess
import sys
import toml

#! Export the modpack files in the `mrpack` format using the `packwiz` tool.
#!
#! # Usage
#! ```
#! python export-mrpack.py `<source_directory>` `<target_directory>` [`<file_name>`]
#! ```
#!
#! # Description
#! The required `<source_directory>` will be used to get the modpack files from.
#! The required `<target_directory>` will be used to store the exported file in.
#! The optional `<file_name>` argument will be used instead of generating a name.
#!
#! The tool `packwiz` is used to create a `mrpack` file.
#!
#! If no `<file_name>` was provided, the `mrpack` will be named matching the template
#! `{name}-{version}.mrpack`. The values `name` and `version` are retrieved from
#! `<source_directory>/pack.toml`.
#!
#! The `packwiz` command used is
#! ```
#! packwiz modrinth export --output "<target_directory>/<file_name>"
#! ```
#!
#! # References
#! - https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack
#! - https://packwiz.infra.link/

# Verify required arguments
if len(sys.argv) < 3:
    print(f"Usage: python {os.path.basename(__file__)} <source_directory> <target_directory> [<file_name>]")
    sys.exit(1)

source_dir = os.path.normpath(sys.argv[1])
target_dir = os.path.normpath(sys.argv[2])
root_dir = os.getcwd()

file_name = ""
if len(sys.argv) > 3:
    file_name = sys.argv[3].strip()

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
    f"{root_dir}/{target_dir}/{file_name}"
], check=True)
