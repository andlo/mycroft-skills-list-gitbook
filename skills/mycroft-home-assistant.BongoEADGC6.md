---
description: 
---

### _mycroft-home-assistant.BongoEADGC6_  
## Description:  
Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
"HomeAssistantSkill": {
"host": "hass.mylan.net",
"password": "mysupersecrethasspass",
"ssl": true|false
}
```

NOTE: SSL support is currently insecure as it does not verify the cert. This means it will
work with a self signed cert, but shouldn't be used accross the internet.

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
``` mycroft-msm install https://github.com/BongoEADGC6/mycroft-home-assistant```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/BongoEADGC6/mycroft-home-assistant](https://github.com/BongoEADGC6/mycroft-home-assistant)  
**Owner:** [@BongoEADGC6](https://github.com/BongoEADGC6)  
**Created:** 2017 Mar 04 14:09:02 UTC  **Last updated:** 2018 Jul 02 12:16:07 UTC  
**License:** GNU Lesser General Public License v3.0  
  
**Categories:** [ uncategorized ]   
