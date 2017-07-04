#
# Are all lights off?
# If lights are on, how many?
# Should work regardless of light/switch domain
# 
# Return input_boolean.are_any_lights_on
# Attributes: number of lights & switches on and the total
#

lightStatus = 'off'
switchEntities = ["switch.aquarium","switch.edison_pendants","switch.office","switch.sink","switch.string_lights","switch.work_lamp","switch.bathroom_light"]
lightsOn = 0
switchesOn = 0
totalOn = 0
whichIcon = "mdi:lightbulb-outline"


for entity_id in hass.states.entity_ids('light'):
  state = hass.states.get(entity_id)
  # filter out individual tradfri bulbs
  if (state.state == 'on' and  "tradfri" not in entity_id):
    lightStatus = 'on'
    lightsOn = lightsOn + 1
for entity_id in switchEntities:
  state = hass.states.get(entity_id)
  if state.state == 'on':
    lightStatus = 'on'
    switchesOn = switchesOn + 1

if lightStatus == 'on':
  whichIcon = "mdi:lightbulb-on-outline"

totalOn = switchesOn + lightsOn

# Return sensor state
hass.states.set('input_boolean.are_any_lights_on', lightStatus, { 
    'friendly_name': 'Are Any Lights On?',
    'icon': whichIcon,
    'lights_on': lightsOn,
    'switches_on': switchesOn,
    'total_on': totalOn
})
