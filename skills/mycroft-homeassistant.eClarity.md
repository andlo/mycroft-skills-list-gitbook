---
description: 
---

### _mycroft-homeassistant.eClarity_  
## Description:  
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
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/eClarity/mycroft-homeassistant```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/eClarity/mycroft-homeassistant](https://github.com/eClarity/mycroft-homeassistant)  
**Owner:** [@eClarity](https://github.com/eClarity)  
**Created:** 2017 May 31 01:18:43 UTC  **Last updated:** 2019 Jan 07 09:51:53 UTC  
**License:** GNU Lesser General Public License v3.0  
  
**Categories:** [ uncategorized ]   
