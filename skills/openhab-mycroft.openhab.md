---
description: This skill adds openHAB support to Mycroft
---
openHAB

This skill adds [openHAB](http://www.openhab.org/) support to [Mycroft](https://mycroft.ai).
The skill takes advantage of the openHAB REST API, so it works both with the v1.x and v2.x of openHAB.

In order to make openHAB Items accessible to Mycroft, they need to be [tagged](https://www.openhab.org/addons/integrations/homekit/).
Device names recognized by Mycroft are matched against openHAB Item Labels.

The above examples would all work with the following set of openHAB Item definitons:

```java
Color DiningroomLight "Diningroom Light" <light> (gKitchen) [ "Lighting" ] {channel="hue:0200:1:bloom1:color"}
Color KitchenLight "Kitchen Light" <light> (gKitchen) [ "Lighting" ] {channel="hue:0200:1:bloom1:color"}
Switch GoodNight "Good Night"	[ "Switchable" ]

Number MqttID1Temperature "Bedroom Temperature" <temperature> [ "CurrentTemperature" ] {mqtt="<[mosquitto:mysensors/SI/1/1/1/0/0:state:default]"}
Number MqttID1Humidity "Bedroom Humidity" [ "CurrentHumidity" ] {mqtt="<[mosquitto:mysensors/SI/1/0/1/0/1:state:default]"}

Group gThermostat "Main Thermostat" [ "gMainThermostat" ]
Number MainThermostatCurrentTemp "Main Thermostat Current Temperature" (gMainThermostat) [ "CurrentTemperature" ]
Number MainThermostatTargetTemperature "Main Thermostat Target Temperature" (gMainThermostat) [ "TargetTemperature" ]
String MainThermostatHeatingCoolingMode "Main Thermostat Heating/Cooling Mode" (gMainThermostat) [ "homekit:HeatingCoolingMode" ]
```

If items are modified in openHAB, a refresh in Mycroft is needed by the command:

- *"Hey Mycroft, refresh openhab items"*

If you've forgotten what items have been identified, you can ask Mycroft:
- *"Hey Mycroft, list openhab items"*

**Github:** | (https://github.com/openhab/openhab-mycroft)  
**Owner:** | [@openhab](https://github.com/openhab)  
**Created:** | 2017-09-07T19:37:21Z  **Last updated:** 2019-12-20T15:45:08Z  
**License:** | [Eclipse Public License 2.0](https://api.github.com/licenses/epl-2.0)  
**Market status:** | [In Market](https://market.mycroft.ai/skill/openhab-skill) PR-1145 new waiting  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
