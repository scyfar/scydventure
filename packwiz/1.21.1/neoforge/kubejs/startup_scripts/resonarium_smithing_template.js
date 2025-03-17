// KubeJS deletes Java generated recipes if any `recipe` event is used
// https://github.com/KubeJS-Mods/KubeJS/issues/822
// Additionally, smithing templates must contain a template, which the original does not
// The resonarium smithing template is easy to craft and can be used for the resonarium tools

StartupEvents.registry("item", (event) => {
  // The official smithing_template builder has a bug with the tooltip title and first line
  event
    .create("scydventure:resonarium_smithing_template")
    .formattedDisplayName(
      Text.translatable(
        "item.scydventure.resonarium_smithing_template.tooltip.display_name"
      )
    )
    // Custom namespace does not work
    .texture("kubejs:item/resonarium_smithing_template")
    .tooltip(
      Text.gray(
        Text.translatable(
          "item.scydventure.resonarium_smithing_template.tooltip.description"
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
          "item.scydventure.resonarium_smithing_template.tooltip.indent_iron_equipment"
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
          "item.scydventure.resonarium_smithing_template.tooltip.indent_resonarium_plate"
        )
      )
    );
});
