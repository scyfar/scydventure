// minecraft:netherite_upgrade_smithing_template
// deeperdarker:warden_upgrade_smithing_template
// => scydventure:dark_netherite_upgrade_smithing_template

ServerEvents.recipes((event) => {
  // Add shapeless crafting recipe for new template
  event.shapeless(
    Item.of("scydventure:dark_netherite_upgrade_smithing_template", 1),
    [
      "minecraft:netherite_upgrade_smithing_template",
      "deeperdarker:warden_upgrade_smithing_template",
    ]
  );

  // Change smithing recipes
  event.replaceInput(
    /advancednetherite:netherite_.*_smithing/,
    "minecraft:netherite_upgrade_smithing_template",
    "scydventure:dark_netherite_upgrade_smithing_template"
  );
});
