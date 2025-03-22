from pathlib import Path
import os
import re
import sys

#! > This script should only be used for automation <
#!   ==============================================
#!
#! Extract the version changelog for the Modrinth release.
#!
#! # Usage
#! ```
#! python extract-changelog.py `<git_tag>`
#! ```
#!
#! # Description
#! The required `<git_tag>` must match this template:
#! `<pack-version>_<minecraft-version>_<loader-name>`.
#!
#! The script uses the provided `git_tag` to find the `CHANGELOG.md` file.
#!
#! The source file is expected to be in a directory matching the template
#! `./packwiz/{<minecraft-version>}/{<loader-name>}/CHANGELOG.md`.
#!
#! The `CHANGELOG.md` must have markers `<!-- BEGIN `<git_tag>` -->` and `<!-- END `<git_tag>` -->`.
#! Everithyng between these marker lines is used as changelog for Modrinth.

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

source_file = os.path.normpath(f"./packwiz/{mc_version}/{loader}/CHANGELOG.md")

# Check, if source file exists
if not Path(source_file).exists():
    print(f"Error: Source file '{source_file}' does not exist.")
    sys.exit(1)

# Load source file
with open(f"{source_file}", "r") as f:
    source_file_content = f.read()

# Extract relevant section
extract_pattern = re.compile(
    rf'<!--\s*BEGIN\s*{re.escape(git_tag)}\s*-->\s*(.*?)\s*<!--\s*END\s*{re.escape(git_tag)}\s*-->',
    re.DOTALL
)
match = extract_pattern.search(source_file_content)

# Print the match, otherwise nothing
changelog = ""
if match:
    changelog = match.group(1).strip()

print(changelog)
