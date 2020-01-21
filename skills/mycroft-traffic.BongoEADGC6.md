---
description: 
---
Traffic Skill for Mycroft

Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
"TrafficSkill": {
"api_key": "REPLACETHISWITHKEYFROMGOOGLE",
"pois": {
"default": {
"destinations": {
"work": "1 Main Street, Beverly Hills, CA 90210"
},
"origins": {
"home": "350 5th Ave, New York, NY 10118"
}
}
}
}
```
* Google API key can be obtained [HERE](https://developers.google.com/maps/documentation/directions/start#get-a-key)

**Github:** | (https://github.com/BongoEADGC6/mycroft-traffic)  
**Owner:** | [@BongoEADGC6](https://github.com/BongoEADGC6)  
**Created:** | 2017-03-04T14:09:37Z  **Last updated:** 2019-11-14T08:44:48Z  
**License:** | No License - dont use this skill !  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
