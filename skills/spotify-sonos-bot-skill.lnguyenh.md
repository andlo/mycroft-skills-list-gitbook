---
description: !Join the chat at 
---

### _spotify-sonos-bot-skill.lnguyenh_  
## Description:  
**Mycroft** (https://mycroft.ai/) is an open source project that provides a local and controlled alternative to Google Assistant and Alexa. Mycroft can run on a Raspberry Pi. Similarly to Alexa, you can add functionalities to your Mycroft voice assistant setup by installing "skills".

This project is a **skill** for Mycroft that provides convenient voice commands to play Spotify music on Sonos speakers.

Big kudos to:
- the project **Node Sonos HTTP API** (https://github.com/jishi/node-sonos-http-api/) which does most of the work and exposes an easy to use Sonos API
- the project **Spotipy** (https://github.com/plamere/spotipy) that is used for populating the user's list of personal spotify playlists, and to play the most popular songs for a given artist.

In its current state, this project provides all the commands I have needed in order to voice-control Sonos and Spotify while cooking dinner :). **It currently only supports playing music on one Sonos speaker** but using the node http api, it should be fairly easy to add support for several speakers.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/lnguyenh/spotify-sonos-bot-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/lnguyenh/spotify-sonos-bot-skill](https://github.com/lnguyenh/spotify-sonos-bot-skill)  
**Owner:** [@lnguyenh](https://github.com/lnguyenh)  
**Created:** 2020 Oct 14 20:38:48 UTC  **Last updated:** 2020 Oct 18 18:43:24 UTC  
**License:** MIT License  
  
**Categories:** [ & ] [ Music ] [ Audio ]   
**Tags:** \#**Spotify** \#**Sonos**   
