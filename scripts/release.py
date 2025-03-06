from pathlib import Path
import os
import subprocess
import sys
import toml

# Check, if the new version is provided
# The `new_version` must follow the format of `<pack-version>_<minecraft-version>_<loader>`
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <new_version>")
    sys.exit(1)

new_version = sys.argv[1].strip().lower()
# Strip leading 'v'
if new_version.startswith("v"):
    new_version = new_version[1:]

# Deconstruct the new version
pack_version, mc_version, loader = new_version.split("_", 2)

source_dir = os.path.normpath(f"./packwiz/{mc_version}/{loader}")

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

# Load pack.toml file
with open(f"{source_dir}/pack.toml", "r") as f:
    config = toml.load(f)

# Update version
if config["version"] != new_version:
    config["version"] = new_version

    with open(f"{source_dir}/pack.toml", "w") as f:
        toml.dump(config, f)

    # Git add & commit
    subprocess.run(["git", "-C", source_dir, "add", "pack.toml"], check=True)
    commit_message = f"chore(release): prepare for release {new_version}"
    subprocess.run(
        ["git", "-C", source_dir, "commit", "-m", commit_message],
        check=True,
    )
else:
    print(f"The current version is already set to '{new_version}'; no changes made")
    user_input = input(f"Do you want to continue? (y/N): ").strip().lower()
    if user_input != "y":
        sys.exit(0)

# Create the release tag
tag_message = f"Release version {new_version}"
subprocess.run(
    ["git", "-C", source_dir, "tag", "-s", f"{new_version}", "-m", tag_message],
    check=True,
)

# Push the tag
subprocess.run(["git", "push", "--follow-tags"], check=True)
