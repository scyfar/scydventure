# Development Notes

## .modlist.json

This file is located in `.packwiz/${minecraft_version}/${modloader}`.

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
