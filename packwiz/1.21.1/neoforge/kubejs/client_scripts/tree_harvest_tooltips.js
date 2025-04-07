// minecraft:netherite_axe
// advancednetherite:netherite_iron_axe
// advancednetherite:netherite_gold_axe
// advancednetherite:netherite_emerald_axe
// advancednetherite:netherite_diamond_axe
// deeperdarker:resonarium_axe
// deeperdarker:warden_axe

const tree_harvest_tooltip_ids = [
  "minecraft:netherite_axe",
  "advancednetherite:netherite_iron_axe",
  "advancednetherite:netherite_gold_axe",
  "advancednetherite:netherite_emerald_axe",
  "advancednetherite:netherite_diamond_axe",
  "deeperdarker:resonarium_axe",
  "deeperdarker:warden_axe",
];

ItemEvents.modifyTooltips((event) => {
  event.add(
    tree_harvest_tooltip_ids,
    { shift: false },
    Text.white("Hold §e[SHIFT]§r to see more info"),
  );
  event.add(
    tree_harvest_tooltip_ids,
    { shift: true },
    Text.white("Capable of mining the entire tree when [SHIFT] is held"),
  );
});
