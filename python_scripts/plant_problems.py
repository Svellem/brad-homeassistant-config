problemPlants = 0

# For every plant
for entity_id in hass.states.entity_ids('plant'):
    state = hass.states.get(entity_id)
    if state.state == 'problem':
        problemPlants = problemPlants + 1
# Set states
hass.states.set('sensor.water_plants', problemPlants, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Plants with Problems',
})
