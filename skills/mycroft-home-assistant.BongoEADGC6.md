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

**Github:** (https://github.com/BongoEADGC6/mycroft-home-assistant)

**Owner:** [@BongoEADGC6](https://github.com/BongoEADGC6) ![avatart](https://avatars2.githubusercontent.com/u/12252699?v=4)

