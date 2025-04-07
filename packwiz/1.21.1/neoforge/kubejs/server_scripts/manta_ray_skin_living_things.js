LootJS.lootTables((event) => {
  event.modifyEntityTables("livingthings:mantaray").createPool((pool) => {
    pool.when((c) => c.randomChance(0.15));
    pool.addEntry(LootEntry.of("scydventure:manta_ray_skin").setCount([1, 3]));
  });
});
