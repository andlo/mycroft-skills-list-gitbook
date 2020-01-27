---
description: An intercom, and soon to be messaging, and video calling skill for Mycroft!
---

### _communications-skill.LinusS1_  
## Description:  
Use this skill to broadcast messages across your home.
When this skill is installed on two or more of your devices, the devices will automatically find and connect to each other.

After they connect, you can say something like "Announce dinner's ready" and all your devices will say that message.

**Setup**
On certain devices (most likely the Mark I), you will have to allow incoming connections through the firewall. Run the following commands on your device:

`sudo ufw allow from any to any port 4445 proto tcp`

`sudo ufw allow from any to any port 4446 proto tcp`

**If the skill does not work, make sure you've entered those commands, and restarted your device**

**Security**
The skill does try to do some basic security implementations, however you **MUST** run this on a WPA2 secured wifi network, if you use wifi.

**Roadmap**
This is only the beginning of this skill!
The future includes:
- Not having to allow ports in (this will be done automatically)
- Calling and video calling!  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Announce that.  
> Announce.  
> Announce.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/LinusS1/communications-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/LinusS1/communications-skill](https://github.com/LinusS1/communications-skill)  
**Owner:** [@LinusS1](https://github.com/LinusS1)  
**Created:** 2018 Dec 25 01:28:55 UTC  **Last updated:** 2019 Dec 11 22:44:08 UTC  
**License:** Apache License 2.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ Daily ] [ Entertainment ] [ Information ] [ IoT ] [ Media ] [ Productivity ]   
**Tags:** \#intercom \#intercoms \#communication \#communications \#broadcast \#broadcasting \#connect \#devices \#video \#calling \#call   
