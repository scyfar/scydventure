<div align="center">

# Scydventure ⛏🛡🪄

<samp>An opinionated modpack</samp>

---

[GitHub repository](https://github.com/scyfar/scydventure)
⏺
[Docs](https://scyfar.github.io/scydventure/)

[![github.com - scydventure](https://img.shields.io/github/v/release/scyfar/scydventure?label=%20&logo=github)](https://github.com/scyfar/scydventure/releases/latest)

---

</div>

# Description

Scydventure is a heavily opinionated modpack.
It has no specific topic and tries to make Minecraft more enjoyable but not overpowered.

# Release

An important note for releases is, that the leading information comes from the `pack.toml`.
The `./scripts/release.py` automatically gathers the required information.

This modpack uses [`packwiz`][packwiz] to manage and export the files.

> [!NOTE]
> Currently, this pack focuses on distributing via [Modrinth](https://modrinth.com/) and for the
> [NeoForge](https://neoforged.net/) mod loader only.
> Other platforms and loaders _may_ follow. No promises though.

# Scripts

## Add mods

> [!CAUTION]
> This script will delete all files in `<target>/mods`.

Mods must be listed in a file named `.modlist.json` in the respective packwiz version directory.
Each JSON object must have a key `url` with a valid URL to the mod or to a specific version at the
Modrinth website.

Dependencies must be also added to this file, despite `packwiz` potentially resolving them. This is
due to the other use in the `./scripts/attribution-data.py` script.

> [!IMPORTANT]
> Unfortunately, packwiz does not allow for silent dependency installation, and it does not properly
> detect if it is already added.
> Therefore, this script requires manual intervention.

The script `./scripts/packwiz-add-mods.py` will add the mods listed in the `.modlist.json` file.
Use it like this:

```shell
python ./scripts/packwiz-add-mods.py ./packwiz/1.21.1/neoforge/
```

## Export mrpack

The script `./scripts/export-mrpack.py` will export the version provided and create the
`mrpack` in the target directory. Use it like this:

```shell
python ./scripts/export-mrpack.py ./packwiz/1.21.1/neoforge/ ./target/
```

## Attribution data

The script `./scripts/attribution-data.py` will use the `.modlist.json` to get attribution data and
print a Markdown table row for each entry.
This table may not be completely filled, and certain fields can be substituted in the JSON file.

This file must contain all mods including the dependencies for a complete list in the documentation.
For details please see
[the documentation](https://scyfar.github.io/scydventure/dev-notes.html#modlistjson).
Use it like this:

```shell
python ./scripts/attribution-data.py ./packwiz/1.21.1/neoforge/
```

The resulting table can be seen [here](https://scyfar.github.io/scydventure/attribution.html).

# Resource Packs

The pack does not ship with resource packs but enables them if mods have built-in ones.
If an `options.txt` exists prior to installing the modpack, the resource packs must be manually
enabled.

# Attribution

Thanks to all the mod, library and tool developers. A special shoutout to the ones providing
software [used for this modpack](https://scyfar.github.io/scydventure/attribution.html).

# License

## Source Code

Scydventure is free and open source. All code in this repository is licensed under
the ISC license ([LICENSE](LICENSE) or
[https://spdx.org/licenses/ISC.html](https://spdx.org/licenses/ISC.html)).

Unless explicitly stated, any source code contributed shall be licensed as above, without any
additional terms or conditions.

## Assets

<img src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" height="31" />

All assets are located in the [/assets](/assets) directory of this repository and are licensed under \
[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

Assets may be licensed differently if a file named `LICENSE` is placed alongside the file.

<!-- link references -->

[packwiz]: https://packwiz.infra.link/
