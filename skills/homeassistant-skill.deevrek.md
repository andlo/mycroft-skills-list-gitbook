--- 
description: 
categories: uncategorized   
tags:   
---

# Home Assistant Skill for Mycroft  
### _homeassistant-skill.deevrek_  
## About:  
Add a block to your ~/.mycroft/mycroft.conf file like this:
"HomeAssistantSkill": {
"host": "hass.mylan.net",
"password": "mysupersecrethasspass",
"ssl": true|false
}
NOTE: SSL support is currently secure as it does verify the cert.
You will then need to restart mycroft.

## Skill information:  
**Github:** | [https://github.com/deevrek/homeassistant-skill](https://github.com/deevrek/homeassistant-skill)  
**Owner:** | [@deevrek](https://github.com/deevrek)  
**Created:** | 2017 Aug 29 21:46:47 UTC  **Last updated:** 2017 Aug 29 21:50:21 UTC  
**License:** | GNU Lesser General Public License v3.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/deevrek/homeassistant-skill```
{% endtab %}
  {% endtabs %}
  