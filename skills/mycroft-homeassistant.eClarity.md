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

**Github:** | (https://github.com/eClarity/mycroft-homeassistant)  
**Owner:** | [@eClarity](https://github.com/eClarity)  
**Created:** | 2017-05-31T01:18:43Z  **Last updated:** 2019-01-07T09:51:53Z  
**License:** | [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/eClarity/mycroft-homeassistant```
{% endtab %}
  {% endtabs %}
  