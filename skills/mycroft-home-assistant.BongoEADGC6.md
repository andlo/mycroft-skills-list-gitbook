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

NOTE: SSL support is currently insecure as it does not verify the cert. This means it will
work with a self signed cert, but shouldn't be used accross the internet.

You will then need to restart mycroft.

**Github:** | (https://github.com/BongoEADGC6/mycroft-home-assistant)  
**Owner:** | [@BongoEADGC6](https://github.com/BongoEADGC6)  
**Created:** | 2017-03-04T14:09:02Z  **Last updated:** 2018-07-02T12:16:07Z  
**License:** | [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/BongoEADGC6/mycroft-home-assistant```
{% endtab %}
  {% endtabs %}
  