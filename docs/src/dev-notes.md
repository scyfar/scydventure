# Development Notes

## Version

The version is composed like this: `<pack_version>_<minecraft_version>_<loader>`.

The `pack_version` follows the [semver](https://semver.org/) specification.
Most commonly used extensions are:

- `-draft`
  - This will be marked as draft release on GitHub
  - This will not be published on Modrinth
- `-alpha`
  - This will be marked as pre-release on GitHub
  - This will be published to Modrinth on the alpha channel
- `-beta` and `-rc.X`
  - This will be marked as pre-release on GitHub
  - This will be published to Modrinth on the beta channel

## `.modlist.json`

This file is located in `.packwiz/${minecraft_version}/${loader}`.

It is used to keep track of all the mods, which are installed in the pack version.
It is also the place where additional information about written permission for modpack usage are
placed.

The following scripts use this file:

- `attribution-data.py`
  - Requires the field `url`.
  - Uses `notes` to set the notes field. Can be Markdown. Value is not substituted with other data.
  - Uses `owner` to set the owner field. Can be Markdown.
    Value is substituted with data from member that has role `owner` from the Modrinth API.
- `packwiz-add-mods.py`
  - Requires the field `url`.
  - Does not use any other field.

Since `.modlist.json` is used for the attribution, all dependencies must also be listed, even though
`packwiz` and Modrinth are capable of resolving them.

## Distant Horizons

https://modrinth.com/mod/distanthorizons/version/2.2.1-a-1.21.1

When installing this, my RAM gets flooded using the default settings.
I have allocated 4096 MB for this pack and I don't want to go rise the requirements just because of
this mod.

## Shaders

The pack does not provide any shaders
During playtesting the shaders mod [Iris Shaders](https://modrinth.com/mod/iris) was used with
[Complementary Shaders - Reimagined](https://modrinth.com/shader/complementary-reimagined).
No changes were made to the default settings.

## Resource Packs

The pack does not ship with extra resource packs. However, it enables the ones provided from mods
such as Continuity.

> [!NOTE]
> The resource pack is enabled in the regular Minecraft options. Should an `options.txt` already
> exist, it is left untouched. In this case the resource packs must be enabled manually.

## `packwiz`

While working reasonably well, it is definitely not made for power-users. And especially not for
automation/scripting.

- Dependencies are not properly detected
- There is no "silent" option. It will always ask if dependencies should be installed
- It does not respect user edits on files
  - This is especially important to know then changing flags like the `preserve` setting in the
    [index.toml](https://packwiz.infra.link/reference/pack-format/index-toml/)

## Release Action

The automated release and publishing workflow is somewhat complicated due to the fact that I did
not manage to get the proper trigger working. Usually I would've liked to use
`on: { release: { types: [published] } }` but the asset data were not present.

A workaround now is to have everything in one workflow, passing assets along and downloading the
release notes with the GitHub CLI.
