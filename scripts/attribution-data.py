from pathlib import Path
from urllib.parse import urlparse
import json
import os
import requests
import subprocess
import sys
import tempfile
import toml

#! > This script requires internet access <
#!   ====================================
#! - https://raw.githubusercontent.com/spdx/license-list-data/refs/heads/main/json/licenses.json
#! - https://api.modrinth.com/
#!
#! Generate the attribution data for all used mods.
#!
#! # Usage
#! ```
#! python attribution-data.py `<source_directory>`
#! ```
#!
#! # Description
#! The required `<source_directory>` will be used to get the `.modlist.json`.
#!
#! The script will print the configured Minecraft and NeoForge version from `pack.toml`.
#! The script will print markdown table rows with the columns "mod title", "version", "owner" and
#! "license" to the terminal.
#!
#! Caches the `licenses.json` in a local `tmp` directory. The `tmp` directory will be automatically
#! removed with the next restart (on Linux).
#!
#! # References
#! - https://docs.modrinth.com/api/

def do_request(url):
    response = requests.get(url)
    if not response.status_code == 200:
        print(f"Error when requesting '{url}'")
        print(f"{response}")

    return response

def get_license_text(license_id, project_license_url, fallback_url):
    if project_license_url:
        return f"[{license_id}]({project_license_url})"

    cache_dir = os.path.join(tempfile.gettempdir(), "scydventure-attribution-data")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    cache_file = os.path.join(cache_dir, "licenses.json")
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            licenses_json = json.load(f)
    else:
        response = do_request("https://raw.githubusercontent.com/spdx/license-list-data/refs/heads/main/json/licenses.json")
        if not response.status_code == 200:
            return ""

        licenses_json = response.json()
        with open(cache_file, "w") as f:
            json.dump(licenses_json, f)

    for spdx_license in licenses_json["licenses"]:
        if spdx_license["licenseId"] == license_id:
            return f"[{license_id}]({spdx_license['reference']})"

    return f"[{license_id}]({fallback_url})"

def get_owner_text(members_json):
    for member in members_json:
        if member["role"].lower() == "owner":
            return f"[{member['user']['username']}](https://modrinth.com/user/{member['user']['username']})"

    return ""

# Verify required arguments
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <source_directory>")
    sys.exit(1)

source_dir = os.path.normpath(sys.argv[1])

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

with open(f"{source_dir}/pack.toml", "r") as f:
    pack_config = toml.load(f)

print(f"The [Minecraft](https://www.minecraft.net/en-us) version is `{pack_config.get('versions', {}).get('minecraft', '')}`.\\")
print(f"The [NeoForge](https://neoforged.net/) version is `{pack_config.get('versions', {}).get('neoforge', '')}`.\n\n")
print(f"| Mod | Version | Author | License |")
print(f"| --- | ------- | ------ | ------- |")

with open(f"{source_dir}/.modlist.json", "r") as f:
    modlist_json = json.load(f)

for mod_json in modlist_json:
    # Get the mod slug from the URL
    slug = urlparse(mod_json["url"].strip()).path.split("/")[2]

    # Get the project data from the Modrinth API
    response = do_request(f"https://api.modrinth.com/v2/project/{slug}")
    if not response.status_code == 200:
        continue

    project_json = response.json()
    title_text = f"[{project_json.get('title', mod_json['url'])}]({mod_json['url']})".replace('|', '\|')
    license_text = get_license_text(
        project_json["license"]["id"].replace("LicenseRef-", ""),
        project_json["license"]["url"],
        mod_json["url"]
    ).replace('|', '\|')
    owner_text = mod_json.get("owner", "").replace('|', '\|')
    if not owner_text:
        # Get the owner data from members
        response = do_request(f"https://api.modrinth.com/v2/project/{slug}/members")
        if response.status_code == 200:
            members_json = response.json()
            owner_text = get_owner_text(members_json).replace('|', '\|')

        if not owner_text:
            # Get the owner data from the organization
            response = do_request(f"https://api.modrinth.com/v3/project/{slug}/organization")
            if response.status_code == 200:
                organization_json = response.json()
                owner_text = f"[{organization_json['name']}](https://modrinth.com/organization/{organization_json['slug']})".replace('|', '\|')

    # Load the mod pw.toml file
    version_text = ""
    with open(f"{source_dir}/mods/{slug}.pw.toml", "r") as f:
        mod_config = toml.load(f)

    mod_version_id = mod_config.get("update", {}).get("modrinth", {}).get("version", "")
    if mod_version_id:
        # Get the version data
        response = do_request(f"https://api.modrinth.com/v2/project/{slug}/version/{mod_version_id}")
        if response.status_code == 200:
            mod_version_json = response.json()
            version_text = f"[{mod_version_json['name']}](https://modrinth.com/mod/{slug}/version/{mod_version_id})".replace('|', '\|')

    # Print out the Markdown table line
    print(f"| {title_text} | {version_text} | {owner_text} | {license_text} |")
