---
description: 
---
Home Assistant Skill for Mycroft

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

**Github:** | (https://github.com/mschot/mycroft-smartthings)  
**Owner:** | [@mschot](https://github.com/mschot)  
**Created:** | 2018-02-01T20:26:25Z  **Last updated:** 2019-08-26T00:36:43Z  
**License:** | [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
