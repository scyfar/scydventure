// https://github.com/Hardel-DW/NeoEnchant

LootJS.lootTables((event) => {
  event.modifyLootTables(LootType.CHEST).createPool((pool) => {
    pool.when((c) => c.randomChance(0.05));
    pool.addEntry(
      LootEntry.of("minecraft:enchanted_book")
        .withWeight(10)
        .enchantRandomly(["enchantplus:boots/step_assist"])
    );

    pool.addEntry(
      LootEntry.of("minecraft:enchanted_book")
        .withWeight(1)
        .enchant((builder) => {
          builder.withEnchantment("enchantplus:pickaxe/spawner_touch", 1);
        })
    );

    pool.addEntry(
      LootEntry.of("minecraft:enchanted_book")
        .withWeight(1)
        .enchant((builder) => {
          builder.withEnchantment("enchantplus:sword/pull", 1);
        })
    );
  });
});
