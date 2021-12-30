---
description: This skill adds openHAB support to Mycroft
---

### _openhab-mycroft.openhab_  
## Description:  
This skill adds [openHAB](http://www.openhab.org/) support to [Mycroft](https://mycroft.ai).
The skill takes advantage of the openHAB REST API, so it works both with the v1.x and v2.x of openHAB.

In order to make openHAB Items accessible to Mycroft, they need to be [tagged](https://www.openhab.org/addons/integrations/homekit/).
Device names recognized by Mycroft are matched against openHAB Item Labels.

The above examples would all work with the following set of openHAB Item definitons:

```java
Color DiningroomLight "Diningroom Light"  (gKitchen) [ "Lighting" ] {channel="hue:0200:1:bloom1:color"}
Color KitchenLight "Kitchen Light"  (gKitchen) [ "Lighting" ] {channel="hue:0200:1:bloom1:color"}
Switch GoodNight "Good Night"	[ "Switchable" ]

Number MqttID1Temperature "Bedroom Temperature"  [ "CurrentTemperature" ] {mqtt="<[mosquitto:mysensors/SI/1/1/1/0/0:state:default]"}
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
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Turn on Diningroom Light.  
> Switch off Kitchen Light.  
> Put on Good Night.  
> What is Good Night status?  
> What is the status of Good Night?  
> Set Diningroom to 50 percent.  
> Dim Kitchen.  
> Bright Kitchen.  
> Dim Kitchen by 20 percent.  
> What's Bedroom temperature?  
> Tell me the temperature of Bedroom.  
> What's the Bedroom humidity?  
> I'd like to know the humidity of Bedroom.  
> Adjust Main Thermostat to 21 degrees.  
> Regulate Main Thermostat to 20 degrees.  
> Decrease Main Thermostat by 2 degrees.  
> Increase Main Thermostat by 1 degrees.  
> What is Main Thermostat is regulated to?  
> How the Main Thermostat tuned to?  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/openhab/openhab-mycroft```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/openhab/openhab-mycroft](https://github.com/openhab/openhab-mycroft)  
**Owner:** [@openhab](https://github.com/openhab)  
**Created:** 2017 Sep 07 19:37:21 UTC  **Last updated:** 2020 Jul 13 10:04:02 UTC  
**License:** Eclipse Public License 2.0  
**Market status:** [Pending Market](https://market.mycroft.ai/skill/) [ PR-1303 ] [ new ] [ needs validation ]  
**Categories:** [ IoT ]   
**Tags:** \#openHAB \#smarthome \#IoT \#Automation \#opensource   
