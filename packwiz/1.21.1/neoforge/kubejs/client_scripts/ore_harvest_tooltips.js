// minecraft:netherite_pickaxe
// advancednetherite:netherite_iron_pickaxe
// advancednetherite:netherite_gold_pickaxe
// advancednetherite:netherite_emerald_pickaxe
// advancednetherite:netherite_diamond_pickaxe
// deeperdarker:resonarium_pickaxe
// deeperdarker:warden_pickaxe

const ore_harvest_tooltip_ids = [
  "minecraft:netherite_pickaxe",
  "advancednetherite:netherite_iron_pickaxe",
  "advancednetherite:netherite_gold_pickaxe",
  "advancednetherite:netherite_emerald_pickaxe",
  "advancednetherite:netherite_diamond_pickaxe",
  "deeperdarker:resonarium_pickaxe",
  "deeperdarker:warden_pickaxe",
];

ItemEvents.modifyTooltips((event) => {
  event.add(
    ore_harvest_tooltip_ids,
    { shift: false },
    Text.white("Hold §e[SHIFT]§r to see more info"),
  );
  event.add(
    ore_harvest_tooltip_ids,
    { shift: true },
    Text.white("Capable of mining the entire ore vein when [SHIFT] is held"),
  );
});
