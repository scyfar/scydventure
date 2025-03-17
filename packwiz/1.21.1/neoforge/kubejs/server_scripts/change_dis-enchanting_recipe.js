// disenchanting_table:disenchanting_table

ServerEvents.recipes((event) => {
  event.remove({ id: "disenchanting_table:disenchanting_table" });
  event.shaped(
    Item.of("disenchanting_table:disenchanting_table", 1),
    [" L ", "DED", "OOO"],
    {
      D: "minecraft:diamond",
      E: "minecraft:enchanting_table",
      L: "minecraft:lapis_lazuli",
      O: "minecraft:obsidian",
    }
  );
});
