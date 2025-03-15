from pathlib import Path
import os
import subprocess
import sys
import toml

#! Update the modpack version, create a Git tag and push everything.
#!
#! # Usage
#! ```
#! python release.py `<git_tag>`
#! ```
#!
#! # Description
#! The required `<git_tag>` will be set as new version in the `pack.toml`. It must match this
#! template: `<pack-version>_<minecraft-version>_<loader-name>`
#!
#! The source files are expected to be in a directory matching the template
#! `./packwiz/{<minecraft-version>}/{<loader-name>}`.
#!
#! The script updates the `./packwiz/{<minecraft-version>}/{<loader-name>}/pack.toml` with the
#! `<git_tag>` if it is not already set to that version and commits the changes.
#!
#! The `git` commands used are
#! ```
#! git -C "./packwiz/{<minecraft-version>}/{<loader-name>}" add pack.toml
#! git -C "./packwiz/{<minecraft-version>}/{<loader-name>}" commit -m "chore(release): prepare for release {<git_tag>}"
#! ```
#!
#! It creates a Git tag with the name `<git_tag>` and pushes all local changes.
#!
#! The `git` commands used are
#! ```
#! git -C "./packwiz/{<minecraft-version>}/{<loader-name>}" -s <git_tag> -m "Release version {<git_tag>}"
#! git push --follow-tags"
#! ```
#!
#! # References
#! - https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack
#! - https://packwiz.infra.link/

# Verify required arguments
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <git_tag>")
    sys.exit(1)

git_tag = sys.argv[1].strip().lower()
# Strip leading 'v'
if git_tag.startswith("v"):
    git_tag = git_tag[1:]

# Deconstruct the new version
pack_version, mc_version, loader = git_tag.split("_", 2)

source_dir = os.path.normpath(f"./packwiz/{mc_version}/{loader}")

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

# Load pack.toml file
with open(f"{source_dir}/pack.toml", "r") as f:
    config = toml.load(f)

# Update version
if config["version"] != git_tag:
    config["version"] = git_tag

    with open(f"{source_dir}/pack.toml", "w") as f:
        toml.dump(config, f)

    # Git add & commit
    subprocess.run(["git", "-C", source_dir, "add", "pack.toml"], check=True)
    commit_message = f"chore(release): prepare for release {git_tag}"
    subprocess.run(
        ["git", "-C", source_dir, "commit", "-m", commit_message],
        check=True,
    )
else:
    print(f"The current version is already set to '{git_tag}'; no changes made")
    user_input = input(f"Do you want to continue? (y/N): ").strip().lower()
    if user_input != "y":
        sys.exit(0)

# Create the release tag
tag_message = f"Release version {git_tag}"
subprocess.run(
    ["git", "-C", source_dir, "tag", "-s", f"{git_tag}", "-m", tag_message],
    check=True,
)

# Push the changes and tag
subprocess.run(["git", "push", "--follow-tags"], check=True)
