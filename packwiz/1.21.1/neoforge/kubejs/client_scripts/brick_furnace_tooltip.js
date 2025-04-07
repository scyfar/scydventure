// brickfurnace:brick_furnace
// brickfurnace:brick_blast_furnace
// brickfurnace:brick_smoker

const brickfurnace_tooltip_ids = [
  "brickfurnace:brick_furnace",
  "brickfurnace:brick_blast_furnace",
  "brickfurnace:brick_smoker",
];

ItemEvents.modifyTooltips((event) => {
  event.add(
    brickfurnace_tooltip_ids,
    { shift: false },
    Text.white("Hold §e[SHIFT]§r to see more info"),
  );
  event.add(
    brickfurnace_tooltip_ids,
    { shift: true },
    Text.white("Smelts items twice as fast as the vanilla variant"),
  );
});
