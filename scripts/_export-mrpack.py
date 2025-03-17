from pathlib import Path
import os
import subprocess
import sys
import toml

#! > This script should only be used for automation <
#!   ==============================================
#!
#! Export the modpack files in the `mrpack` format using the `packwiz` tool.
#!
#! # Usage
#! ```
#! python _export-mrpack.py `<git_tag>` [`<file_name>`]
#! ```
#!
#! # Description
#! The required `<git_tag>` must match this template:
#! `<pack-version>_<minecraft-version>_<loader-name>`.
#! The optional `<file_name>` argument will be used instead of generating a name.
#!
#! The script uses the provided `git_tag` to find the files to export. The tool `packwiz` is used
#! to create a `mrpack` file.
#!
#! The source files are expected to be in a directory matching the template
#! `./packwiz/{<minecraft-version>}/{<loader-name>}`.
#!
#! The exported `mrpack` file will be placed in the directory the script was executed from (`.`).
#!
#! If no `<file_name>` was provided, the `mrpack` will be named matching the template
#! `{name}-{version}.mrpack`. The values `name` and `version` are retrieved from
#! `./packwiz/{<minecraft-version>}/{<loader-name>}/pack.toml`.
#!
#! The `packwiz` command used is
#! ```
#! packwiz modrinth export --output <file_name>
#! ```
#!
#! # References
#! - https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack
#! - https://packwiz.infra.link/

# Verify required arguments
if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(__file__)} <git_tag> [<file_name>]")
    sys.exit(1)

git_tag = sys.argv[1].strip().lower()
# Strip leading 'v'
if git_tag.startswith("v"):
    git_tag = git_tag[1:]

# Deconstruct the git_tag
pack_version, mc_version, loader = git_tag.split("_")

source_dir = os.path.normpath(f"./packwiz/{mc_version}/{loader}")
target_dir = os.path.normpath(".")

file_name = ""
if len(sys.argv) > 2:
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
