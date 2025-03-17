// => scydventure:resonarium_smithing_template

ServerEvents.recipes((event) => {
  event.shapeless(Item.of("scydventure:resonarium_smithing_template", 1), [
    "#c:stones",
    "#c:cobblestones",
  ]);
});
