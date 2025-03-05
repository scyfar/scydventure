from pathlib import Path
from urllib.parse import urlparse
import json
import os
import requests
import subprocess
import sys
import tempfile

# Check, if the source directory is provided
# The `source` must be the path to the directory with the version, which should have mods installed
if len(sys.argv) != 2:
    print(f"Usage: python {os.path.basename(__file__)} <source>")
    sys.exit(1)

source_dir = os.path.normpath(sys.argv[1])

# Check, if source directory exists
if not Path(source_dir).exists():
    print(f"Error: Source directory '{source_dir}' does not exist.")
    sys.exit(1)

with open(f"{source_dir}/.modlist.json", "r") as f:
    modlist_json = json.load(f)

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

for mod_json in modlist_json:
    # Get the mod slug from the URL
    slug = urlparse(mod_json["url"].strip()).path.split("/")[2]

    # Get the project data from the Modrinth API
    response = do_request(f"https://api.modrinth.com/v2/project/{slug}")
    if not response.status_code == 200:
        continue

    project_json = response.json()
    title_text = f"[{project_json.get('title', mod_json['url'])}]({mod_json['url']})"
    license_text = get_license_text(
        project_json["license"]["id"].replace("LicenseRef-", ""),
        project_json["license"]["url"],
        mod_json["url"]
    )
    notes_text = mod_json.get("notes", "")
    owner_text = mod_json.get("owner", "")
    if not owner_text:
        # Get the owner data
        response = do_request(f"https://api.modrinth.com/v2/project/{slug}/members")
        if not response.status_code == 200:
            continue

        members_json = response.json()
        owner_text = get_owner_text(members_json)

    # Print out the Markdown table line
    print(f"| {title_text} | {owner_text} | {license_text} | {notes_text} | ")
