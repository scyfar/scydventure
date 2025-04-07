// Resonarium gear requires a drop from sludge and any scute, which is both reasonably rare. To make
// it available a little easier, the manta ray from Living Things should drop some of their skin
// which will be used as `scute` substitute for the resonarium tools.

StartupEvents.registry("item", (event) => {
  event
    .create("scydventure:manta_ray_skin")
    .formattedDisplayName(Text.translatable("item.scydventure.manta_ray_skin.tooltip.display_name"))
    .texture("kubejs:item/manta_ray_skin")
    .tag("deeperdarker:scutes");
});
