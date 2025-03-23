from pathlib import Path
import json
import os
import shutil
import sys
import tempfile
import zipfile

#! Force the client side config to `required` in the `mrpack`.
#!
#! # Usage
#! ```
#! python client-env-required.py `<source_file>` [`<target_file>`]
#! ```
#!
#! # Description
#! The required `<source_file>` must point to the input `mrpack` file.
#! The optional `<target_file>` argument will be used instead of overwriting the `<source_file>`.
#!
#! The `<source_file>` will be repacked with the client config set to `required` for all mods.
#! This is currently necessary for the Modrinth app to also include server only mods on local
#! installs.
#!
#! Unpacks the `<source_file>` in a local `tmp` directory.
#!
#! # References
#! - https://github.com/scyfar/scydventure/discussions/25#discussion-8087151
#! - https://github.com/modrinth/code/blob/827e3ec0a0a7149709df4d292add222c490e8318/packages/app-lib/src/api/profile/mod.rs#L860C1-L865C65

# Verify required arguments
if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(__file__)} <source_file> [<target_file>]")
    sys.exit(1)

source_file = os.path.normpath(sys.argv[1])

target_file = source_file
if len(sys.argv) > 2:
    target_file = os.path.normpath(sys.argv[2])

# Check, if source file exists
if not Path(source_file).exists():
    print(f"Error: Source file '{source_file}' does not exist.")
    sys.exit(1)

# Create a temporary working directory.
tmp_dir = tempfile.mkdtemp()

try:
    # Unpack the mrpack
    with zipfile.ZipFile(source_file, 'r') as zip_ref:
        zip_ref.extractall(tmp_dir)

    # Load modrinth.index.json
    index_file_path = Path(tmp_dir) / "modrinth.index.json"
    if not index_file_path.exists():
        print("Error: modrinth.index.json not found in the archive.")
        sys.exit(1)

    with open(index_file_path, "r") as f:
        index_data = json.load(f)

    # Change all 'env.client' settings to 'required'
    if "files" in index_data:
        for file_entry in index_data["files"]:
            if "env" in file_entry and "client" in file_entry["env"]:
                file_entry["env"]["client"] = "required"

    # Save the modified JSON back
    with open(index_file_path, "w") as f:
        json.dump(index_data, f, indent=2)

    # Repack the directory into a new mrpack file
    with zipfile.ZipFile(target_file, 'w', zipfile.ZIP_DEFLATED) as zip_out:
        for foldername, subfolders, filenames in os.walk(tmp_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Create archive-relative path
                archive_name = os.path.relpath(file_path, tmp_dir)
                zip_out.write(file_path, archive_name)

    print(f"Repacked mrpack created at: {target_file}")

finally:
    shutil.rmtree(tmp_dir)
