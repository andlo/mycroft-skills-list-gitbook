--- 
description: 
---

# Home Assistant Skill for Mycroft  
### _mycroft-homeassistant.eClarity_  
## About:  
Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
"HomeAssistantSkill": {
"host": "hass.mylan.net",
"password": "mysupersecrethasspass",
"ssl": true|false
}
```

NOTE: SSL support is currently secure as it does verify the cert.

You will then need to restart mycroft.

## Skill information:  
**Github:** | [https://github.com/eClarity/mycroft-homeassistant](https://github.com/eClarity/mycroft-homeassistant)  
**Owner:** | [@eClarity](https://github.com/eClarity)  
**Created:** | 2017 May 31 01:18:43 UTC  **Last updated:** 2019 Jan 07 09:51:53 UTC  
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
``` mycroft-msm install https://github.com/eClarity/mycroft-homeassistant```
{% endtab %}
  {% endtabs %}
  