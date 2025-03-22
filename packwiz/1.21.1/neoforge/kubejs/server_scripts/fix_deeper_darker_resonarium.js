// KubeJS deletes Java generated recipes if any `recipe` event is used
// https://github.com/KubeJS-Mods/KubeJS/issues/822
//
// deeperdarker:resonarium_shovel
// deeperdarker:resonarium_pickaxe
// deeperdarker:resonarium_axe
// deeperdarker:resonarium_hoe
// deeperdarker:resonarium_sword
// deeperdarker:resonarium_helmet
// deeperdarker:resonarium_chestplate
// deeperdarker:resonarium_leggings
// deeperdarker:resonarium_boots
// deeperdarker:resonarium_plate

const types = [
  "shovel",
  "pickaxe",
  "axe",
  "hoe",
  "sword",
  "helmet",
  "chestplate",
  "leggings",
  "boots",
];

ServerEvents.recipes((event) => {
  for (const type of types) {
    event.smithing(
      Item.of(`deeperdarker:resonarium_${type}`),
      "scydventure:resonarium_smithing_template",
      `minecraft:iron_${type}`,
      "deeperdarker:resonarium_plate"
    );
  }
});
