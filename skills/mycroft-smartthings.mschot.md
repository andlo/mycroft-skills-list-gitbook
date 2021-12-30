---
description: 
---

### _mycroft-smartthings.mschot_  
## Description:  
Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
"HomeAssistantSkill": {
"host": "hass.mylan.net",
"password": "mysupersecrethasspass",
"portnum": 8123,
"ssl": true|false
}
```

NOTE: portnum is for the port number you have Home Assistant running on. 8123 is default.

NOTE: SSL support is currently secure as it does verify the cert.

You will then need to restart mycroft.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/mschot/mycroft-smartthings```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/mschot/mycroft-smartthings](https://github.com/mschot/mycroft-smartthings)  
**Owner:** [@mschot](https://github.com/mschot)  
**Created:** 2018 Feb 01 20:26:25 UTC  **Last updated:** 2019 Aug 26 00:36:43 UTC  
**License:** GNU Lesser General Public License v3.0  
  
**Categories:** [ uncategorized ]   
