---
titel: Home Assistant Skill for Mycroft
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
