---
description: 
---
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

**Github:** (https://github.com/mschot/mycroft-smartthings)

**Owner:** [@mschot](https://github.com/mschot) ![avatart](https://avatars1.githubusercontent.com/u/5399612?v=4)

