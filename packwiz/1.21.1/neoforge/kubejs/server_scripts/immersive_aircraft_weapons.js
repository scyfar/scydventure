const ids = [
  "immersive_aircraft:warship",
  "immersive_aircraft:rotary_cannon",
  "immersive_aircraft:heavy_crossbow",
  "immersive_aircraft:bomb_bay"
]

// remove
ServerEvents.recipes(event => {
  ids.forEach(id => event.remove({ id: id }));
});

// add tag to hide in recipe viewers (EMI)
ServerEvents.tags("item", event => {
  ids.forEach(id => event.add("c:hidden_from_recipe_viewers", id));
});

// remove from loot tables
LootJS.lootTables(event => {
  event.modifyLootTables(/.*/).removeEntry(entry => entry.isItem() && ids.includes(entry.item.id));
});
