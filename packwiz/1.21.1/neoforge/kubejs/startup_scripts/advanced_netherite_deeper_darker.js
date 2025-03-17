// minecraft:netherite_upgrade_smithing_template
// deeperdarker:warden_upgrade_smithing_template

StartupEvents.registry("item", (event) => {
  // Builder does not allow multiple items for applies_to in tooltip
  event
    .create("scydventure:dark_netherite_upgrade_smithing_template")
    .formattedDisplayName(
      Text.translatable(
        "item.scydventure.dark_netherite_upgrade_smithing_template.tooltip.display_name"
      )
    )
    // Custom namespace does not work
    .texture("kubejs:item/dark_netherite_upgrade_smithing_template")
    .tooltip(
      Text.gray(
        Text.translatable(
          "item.scydventure.dark_netherite_upgrade_smithing_template.tooltip.description"
        )
      )
    )
    .tooltip("")
    .tooltip(
      Text.gray(
        Text.translatable(
          "item.scydventure.smithing_template.tooltip.applies_to"
        )
      )
    )
    .tooltip(
      Text.blue(
        Text.translatable(
          "item.scydventure.dark_netherite_upgrade_smithing_template.tooltip.indent_netherite_equipment"
        )
      )
    )
    .tooltip(
      Text.blue(
        Text.translatable(
          "item.scydventure.dark_netherite_upgrade_smithing_template.tooltip.indent_netherite-alloy_equipment"
        )
      )
    )
    .tooltip(
      Text.gray(
        Text.translatable(
          "item.scydventure.smithing_template.tooltip.ingredients"
        )
      )
    )
    .tooltip(
      Text.blue(
        Text.translatable(
          "item.scydventure.dark_netherite_upgrade_smithing_template.tooltip.indent_netherite-alloy_ingot"
        )
      )
    );
});
