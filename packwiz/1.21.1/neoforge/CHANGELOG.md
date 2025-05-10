# Scydventure - Changelog

<!-- BEGIN 1.0.1_1.21.1_neoforge -->

## What's Changed (`1.0.1_1.21.1_neoforge`)

- The mods [Waystones](https://modrinth.com/mod/waystones/version/21.1.17+neoforge-1.21.1) and
  [Balm](https://modrinth.com/mod/balm/version/21.0.41+neoforge-1.21.1) were updated since the
  waystone generation was broken. With this update the generation of waystones in villages has been
  disabled. Waystones can be crafted and found in the wild.

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/1.0.1_1.21.1_neoforge

For questions to a particular version, feel free to head over to the
[respective version discussion on GitHub.](https://github.com/scyfar/scydventure/discussions/categories/versions)

<!-- END 1.0.1_1.21.1_neoforge -->
<!-- BEGIN 1.0.0_1.21.1_neoforge -->

## What's Changed (`1.0.0_1.21.1_neoforge`)

- Custom manta ray skin was removed again due to issues between LootJS and JER.
  This was introduced to make the resonarium gear more accessible. But with all provided tools it
  is not necessary anyway, since the scutes can be found using the Natures Compass and the Biplane.

- The mod [Iris Shaders](https://modrinth.com/mod/iris) was removed as Scydventure does not provide
  shaders, making the mod potentially useless to load. It can easily be added manually if shaders
  are desired (much like resource packs).

All mods have been updated to their latest version as of 2025-04-14 and NeoForge was updated to
`21.1.147`.

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/1.0.0_1.21.1_neoforge

For questions to a particular version, feel free to head over to the
[respective version discussion on GitHub.](https://github.com/scyfar/scydventure/discussions/categories/versions)

<!-- END 1.0.0_1.21.1_neoforge -->
<!-- BEGIN 0.2.0-beta_1.21.1_neoforge -->

## What's Changed (`0.2.0-beta_1.21.1_neoforge`)

- The mod [Neo Enchant+](https://modrinth.com/datapack/neoenchant) has been removed. The
  implementation for the enchant effects is too powerful and not configurable.

- The [Farmer's Delight](https://modrinth.com/mod/farmers-delight) settings have been changed.
    - The village compost heaps are now disabled.
    - The boost changes for rich soil has been lowered to `0.05` (was `0.2`).
    - The fortune effect bonus for the cutting board has ben lowered to `0.05` (was `0.1`)

- The mod [Villager Leads](https://modrinth.com/mod/exline-villager-leads) was added for better
  villager handling.

- The mod [Tree Harvester](https://modrinth.com/mod/tree-harvester) was added.

- The mod [Ore Harvester](https://modrinth.com/mod/ore-harvester) was added.

- The mod [Leaves Be Gone](https://modrinth.com/mod/leaves-be-gone) was removed. The added mod
  [Tree Harvester](https://modrinth.com/mod/tree-harvester) already provides this functionality.

- The double door config was changed to support `16` (was `10`) adjacent doors at once.

All mods have been updated to their latest version as of 2025-04-07 and NeoForge was updated to
`21.1.145`.

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/0.2.0-beta_1.21.1_neoforge

For questions to a particular version, feel free to head over to the
[respective version discussion on GitHub.](https://github.com/scyfar/scydventure/discussions/categories/versions)

<!-- END 0.2.0-beta_1.21.1_neoforge -->
<!-- BEGIN 0.1.0-beta_1.21.1_neoforge -->

## What's Changed (`0.1.0-beta_1.21.1_neoforge`)

- The mod [Sophisticated Storage](https://modrinth.com/mod/sophisticated-storage) was replaced in
favor of [Tom's Simple Storage Mod](https://modrinth.com/mod/toms-storage). Tom's does fit better
and provides the desired crafting grid with all the storage attached. Additionally, it provides a
good way to get a wireless terminal.

- The mod [ExtraSounds Next](https://modrinth.com/mod/extrasoundsforge) was replaced by the mod
[Sounds](https://modrinth.com/mod/sound) for better customization and better overall sound quality.

- The mod [Short Circuit](https://modrinth.com/mod/short-circuit) was removed as it was not providing
the easy compacted redstone interaction as hoped.

- The mod [NetherPortalFix](https://modrinth.com/mod/netherportalfix) was added to better connect the
nether portals (even in single player mode).

- Add `biomesoplenty:pasture` as pollen biome for [Subtle Effects](https://modrinth.com/mod/subtle-effects).

All mods have been updated to their latest version as of 2025-04-04 and NeoForge was updated to
`21.1.143`.

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/0.1.0-beta_1.21.1_neoforge

For questions to a particular version, feel free to head over to the
[respective version discussion on GitHub.](https://github.com/scyfar/scydventure/discussions/categories/versions)

<!-- END 0.1.0-beta_1.21.1_neoforge -->
<!-- BEGIN 0.1.2-alpha_1.21.1_neoforge -->

## What's Changed (`0.1.2-alpha_1.21.1_neoforge`)

This is a technical release.

No changes were made to the actual mod-pack. This release fixes the installation issue where mods
targeted for the server only would not be properly installed.

You can read about the details [in the Dev-Log.](https://github.com/scyfar/scydventure/discussions/25)

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/0.1.2-alpha_1.21.1_neoforge

For questions to a particular version, feel free to head over to the
[respective version discussion on GitHub.](https://github.com/scyfar/scydventure/discussions/categories/versions)

<!-- END 0.1.2-alpha_1.21.1_neoforge -->
<!-- BEGIN 0.1.1-alpha_1.21.1_neoforge -->

## What's Changed (`0.1.1-alpha_1.21.1_neoforge`)

This is a technical release.

No changes were made to the actual mod-pack, but additional information is added to the metadata:

- A new `*_singleplayer.mrpack` asset is attached to versions. This is required since otherwise
  server side mods will not be installed on local installations. Use this if you run the pack
  entirely on your system and don't have a dedicated server. See
  [this discussion](https://github.com/scyfar/scydventure/discussions/25)
- Dependency information is now added to each version, so it is immediately clear which mods are
  included in the mod-pack.

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/0.1.1-alpha_1.21.1_neoforge

<!-- END 0.1.1-alpha_1.21.1_neoforge -->
<!-- BEGIN 0.1.0-alpha_1.21.1_neoforge -->

## What's Changed (`0.1.0-alpha_1.21.1_neoforge`)

This is the initial alpha release of Scydventure.

The most notable changes apart from the inception are:

- The day and night cycles have been changed. The day should be noticeably longer.
- With access to Netherbrick, a new tier for furnaces unlocks for faster smelting.
- The world is much more lively, atmospheric and interesting to explore, but also more dangerous.
- To guard against the dangers, additional armor and weaponry is available.
- Adventures can be extended thanks to backpacks and storage systems can be as functional as they
  should be
- More enchantments introduce an extended progression and make the game more enjoyable

**Technical Changelog**: https://github.com/scyfar/scydventure/releases/tag/0.1.0-alpha_1.21.1_neoforge

<!-- END 0.1.0-alpha_1.21.1_neoforge -->
