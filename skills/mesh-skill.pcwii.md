---
description: Send MQTT messages and commands between multiple mycroft.ai devices
---

### _mesh-skill.pcwii_  
## Description:  
A flock of Seagulls, a pride of Lions, a swarm of Bees, and a "mesh of Mycrofts".

This skill utilizes the lightweight MQTT messaging protocol to connect a group ("mesh") of Mycroft units together. The skill has the ability to send messages (intercom) and commands (messagebus) to one or more remote Mycroft units.
1. Each Mycroft unit has the ability to publish both Mycroft requests and responses to the the MQTT broker.
The MQTT Topics for this communication is...
* ```/RemoteDevices/deviceUUID/request```
* ```/RemoteDevices/deviceUUID/response```
2. The deviceUUID is a unique ID created from the MAC of the sending Mycroft unit.
*This is intended to be a general MQTT broadcast and can be subscribed to by any MQTT client (ie. Home Assistant?).
3. Each Mycroft unit has it's own Device Name (location_id) that can be set in the web interface.
4. The Mycroft unit will automatically subscribe to all messages sent to it's own Device Name (location_id).
* ```/RemoteDevices/```
* The  is automatically obtained from the Mycroft Device Settings web page...
![location_id](/images/location_id.png)
* location id's are automatically converted to lowercase to avoid confusion

5. When a message is sent from any Mycroft unit, the message will be published to "Mycroft/RemoteDevices/location_id".
6. The destination location_id is specified in the skill dialog.
7. The message payload will contain the following Json...
* ```{"source":"", "message":"is dinner ready yet"}```  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Send a remote message.  
> Send a remote command.  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/pcwii/mesh-skill](https://github.com/pcwii/mesh-skill)  
**Owner:** [@pcwii](https://github.com/pcwii)  
**Created:** 2019 Dec 21 13:58:30 UTC  **Last updated:** 2020 Apr 28 07:51:42 UTC  
**License:** No License  
  
**Categories:** [ IoT ]   
**Tags:** \#mesh \#remote \#connect \#control \#MQTT \#HA \#Homeassistant   
