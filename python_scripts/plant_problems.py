problemPlants = 0
allproblemPlants = []
waterPlants = []
numberWater = 0
fertilizePlants = []
numberFertilize = 0
deadBatteries = []
numberdeadBatteries = 0
whichIcon = "mdi:help-circle-outline"

for entity_id in hass.states.entity_ids('plant'):
    state = hass.states.get(entity_id)
    if state.state == 'problem':
        problemPlants = problemPlants + 1
        allproblemPlants.append(state.name)
        problem = state.attributes.get('problem') or 'none'
        if "conductivity low" in problem:
          fertilizePlants.append(state.name)
          numberFertilize = numberFertilize + 1
        if "moisture low" in problem:
          waterPlants.append(state.name)
          numberWater = numberWater + 1
        if "battery low" in problem:
          deadBatteries.append(state.name)
          numberdeadBatteries = numberDeadBatteries + 1

# Set icon
if problemPlants > 0:
  whichIcon = "mdi:alert-circle-outline"
else:
  whichIcon = "mdi:check-circle-outline"

# Set states
hass.states.set('sensor.water_plants', problemPlants, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Problem Plants',
    'icon': whichIcon,
    'problem_plants': allproblemPlants,
    'water': waterPlants,
    'water_number': numberWater,
    'fertilize': fertilizePlants,
    'fertilize_number': numberFertilize,
    'battery_change': deadBatteries,
    'battery_number': numberdeadBatteries
})
