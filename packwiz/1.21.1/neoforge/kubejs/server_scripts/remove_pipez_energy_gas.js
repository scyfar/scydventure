const remove_pipez_ids = ["pipez:gas_pipe", "pipez:energy_pipe"];

// Remove the recipes
ServerEvents.recipes((event) => {
  remove_pipez_ids.forEach((id) => event.remove({ id: id }));
});

// Add tag to hide in recipe viewers
ServerEvents.tags("item", (event) => {
  remove_pipez_ids.forEach((id) =>
    event.add("c:hidden_from_recipe_viewers", id)
  );
});

// Remove from loot tables
LootJS.lootTables((event) => {
  event
    .modifyLootTables(/.*/)
    .removeEntry(
      (entry) => entry.isItem() && remove_pipez_ids.includes(entry.item.id)
    );
});
