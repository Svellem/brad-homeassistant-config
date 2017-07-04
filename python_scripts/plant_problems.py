problemPlants = 0
waterPlants = []
numberWater = 0
fertilizePlants = []
numberFertilize = 0

for entity_id in hass.states.entity_ids('plant'):
    state = hass.states.get(entity_id)
    if state.state == 'problem':
        problemPlants = problemPlants + 1
        problem = state.attributes.get('problem') or 'none'
        if "conductivity low" in problem:
          fertilizePlants.append(state.name)
          numberFertilize = numberFertilize + 1
        if "moisture low" in problem:
          waterPlants.append(state.name)
          numberWater = numberWater + 1
# Set states
hass.states.set('sensor.water_plants', problemPlants, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Problem Plants',
    'water': waterPlants,
    'water_number': numberWater,
    'fertilize': fertilizePlants,
    'fertilize_number': numberFertilize
})
