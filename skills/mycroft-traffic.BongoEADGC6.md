---
description: 
---
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
