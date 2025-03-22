// brickfurnace:brick_furnace
// brickfurnace:brick_blast_furnace
// brickfurnace:brick_smoker

ServerEvents.recipes((event) => {
  // Require Nether Brick(s) to slightly delay the faster furnaces
  event.replaceInput(
    { id: "brickfurnace:brick_furnace" },
    "minecraft:brick",
    "minecraft:nether_brick"
  );
  event.replaceInput(
    { id: "brickfurnace:brick_blast_furnace" },
    "minecraft:bricks",
    "minecraft:nether_bricks"
  );
});
