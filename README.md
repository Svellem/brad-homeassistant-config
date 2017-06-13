# Home Assistant Configuration
[Home Assistant](http://homeassistant.io) configuration files.

My HA is an Hassbian install on a Raspberry Pi 3 with an Aeotec Z-Wave stick.

Running HA version: 0.44.1

## Hardware
* Lights
  * LimitlessLED - [Milight RGB Bulbs](http://amzn.to/2slpT2W) using [MiLight WiFi Bridge](http://amzn.to/2roEQ59) x2
  * Ikea Tradfri - several bulbs via gateway
  * ESP8266 bulb with [AiLight firmware](https://github.com/stelgenhof/AiLight) - TESTING
* Wall Switches
  * [GE Z-Wave 12727 Wall Toggle Switch](http://amzn.to/2rnVCBs) x1
  * [GE Z-Wave 12729 Wall Toggle Dimmer Switch](http://amzn.to/2spiWil) x2
  * Enerwave Z-Wave ZWN-RSM2 Dual In-Wall Relay x1
* Smart Devices
  * [WEMO Mr. Coffee](http://amzn.to/2sysDuG)
  * [Withings Body Scale](http://amzn.to/2spNwIQ)
  * Fitbit
* Switches
  * [TP-Link HS100 Smart Switch](http://amzn.to/2sq1bQb)
  * [Sonoff Switches](https://www.itead.cc/sonoff-wifi-wireless-switch.html) running [Sonoff-HomeAssistant](https://github.com/KmanOz/Sonoff-HomeAssistant) firmware
* Media Players
  * [Volumio](https://volumio.org/) Raspberry Pi streaming player for stereo
  * Plex (Roku)
  * MPD - plays radio through speaker on HA Raspberry Pi
  * VLC - for TTS (not implemented yet)
* Sensors
  * [Wemos D1 Mini](http://amzn.to/2sydVU8) (esp8266) nodes with sensors for motion, temps, etc. via MQTT
  * Mi Flora plant sensors x9
  * [Z-Wave Motion Sensor](http://amzn.to/2symNta) (battery powered)
* Other Hardware
  * old iPhones with IPCam app
  * Synology DS413j - NAS
  
## Automations
* Alarm Clock
  * Make Morning Coffee when Alarm goes off
  * Alarm Clock - turn on lights and radio to wake me up
* Aquarium
  * Turn on 30 mins before sunrise and 1 hour after
  * Turn on 1 hour before sunset, turn off 4 hours after or at 10PM (whichever is first)
* IFTT Integration
  * When plants need to be watered, add them to my Todoist todo list
  * If Fitbit logs new sleep but no alarm is set, wake house up
  * Withings weigh in before bed 9pm - 12am, start goodnight sequence
* Lights
  * Sunset - 40m before sunset, turn on evening lights
  * Day - during day turn on day dim lights and throttle Transmission
  * Evening - turn on dim lights if I come home after 10pm
  * Turn everything off when no one's home
  * Turn Closet lights on/off by motion detector
  * Turn Bathroom lights on/off by motion detector
  * Turn Crawl space light on/off by door sensor
  * Turn kitchen lamps on/off using wall switch
  * Turn on office lamps using switch
* Media
  * Dim house lights when Plex starts playing
  * Turn on bathroom lights & lamp when movie pausd
  * Fade house lights up when Plex stops
* Notifications
  * Alarm - send weather summary and image from window camera when alarm goes off
  * Security - send image from front door camera if no one's home and door opens
  * Reminder - If I'm home at 10:30pm and coffee isn't ready but alarm is set, remind me
  * System - Notify if disk use gets high
  * System - Notify if new HA version available
* Timelapse - record JPEGs of sunrise/sunset
  

## TODO
* Swap the LimitlessLED lights from the MiLight bridge to [esp8266 DIY bridge](https://github.com/sidoh/esp8266_milight_hub)
* TTS
* Re-setup homebridge
* Add IR control of projector
