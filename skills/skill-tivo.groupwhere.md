--- 
description: 
categories: uncategorized   
tags:   
---

# skill-tivo  
### _skill-tivo.groupwhere_  
## About:  
Based on ideas from the following sites:




Add the following to your mycroft.conf and restart mycroft-skills
"TivoSkill": {
"name": "Bob's Tivo",
"host": "192.168.0.84",
"port": 31339,
"zapuser": "your@email.addr",
"zappass": "YOURZAP2ITPASS",
"debug": false
}
Port should always be 31339.  Zap2iT is optional but will allow mycroft to tell you what is playing on the current channel.  Without it, it will only tell you the channel.
Currently, the following functions are working:
* "Tivo status"
* "Tivo channel up"
* "Tivo channel down"
* "Tivo channel set 2 3 1"
* "Tivo pause"
* "Tivo play"
* "Tivo off"
* "Tivo on"
These functions should be working but require some additional testing.  These are specifically to initiate and stop a recording in progress:
* "Tivo record"
* "Tivo stop"
Mycroft will respond with, e.g.:
* "Bob's Tivo is currently watching channel 231"
* "Bob's Tivo is currently watching channel 231 Raiders of the Lost Ark" (with your zap2it account setup and with the correct lineup selected with their service)
* "Bob's Tivo is off"
* "Bob's Tivo is playing"

## Skill information:  
**Github:** | [https://github.com/groupwhere/skill-tivo](https://github.com/groupwhere/skill-tivo)  
**Owner:** | [@groupwhere](https://github.com/groupwhere)  
**Created:** | 2018 Mar 17 16:20:08 UTC  **Last updated:** 2018 Aug 09 16:55:23 UTC  
**License:** | GNU General Public License v3.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/groupwhere/skill-tivo```
{% endtab %}
  {% endtabs %}
  