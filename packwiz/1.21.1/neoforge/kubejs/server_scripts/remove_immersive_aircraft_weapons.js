const remove_immersive_ids = [
  "immersive_aircraft:warship",
  "immersive_aircraft:rotary_cannon",
  "immersive_aircraft:heavy_crossbow",
  "immersive_aircraft:bomb_bay",
];

// Remove the recipes
ServerEvents.recipes((event) => {
  remove_immersive_ids.forEach((id) => event.remove({ id: id }));
});

// Add tag to hide in recipe viewers
ServerEvents.tags("item", (event) => {
  remove_immersive_ids.forEach((id) =>
    event.add("c:hidden_from_recipe_viewers", id)
  );
});

// Remove from loot tables
LootJS.lootTables((event) => {
  event
    .modifyLootTables(/.*/)
    .removeEntry(
      (entry) => entry.isItem() && remove_immersive_ids.includes(entry.item.id)
    );
});
