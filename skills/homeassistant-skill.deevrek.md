---
description: 
---
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

**Github:** | (https://github.com/deevrek/homeassistant-skill)  
**Owner:** | [@deevrek](https://github.com/deevrek)  
**Created:** | 2017-08-29T21:46:47Z  **Last updated:** 2017-08-29T21:50:21Z  
**License:** | [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/deevrek/homeassistant-skill```
{% endtab %}
  {% endtabs %}
  