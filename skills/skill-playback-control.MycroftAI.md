---
description: Common playback control system
---
Playback Control

This Skill doesn't do anything by itself, but it provides an important common
language for audio playback skills.  By handling simple phrases like
'pause', this one Skill can turn around and rebroadcast the [messagebus](https://mycroft.ai/documentation/message-bus/)
command `mycroft.audio.service.pause`, allowing several music services to share
common terminology such as "pause".

Additionally, this implements the common Play handler.  This allows playback
services to negotiate which is best suited to play back a specific request.
This capability is used by the [Spotify](https://github.com/forslund/spotify-skill) and [Pandora](https://github.com/mycroftai/pianobar-skill) Skills, among others.

**Github:** | (https://github.com/MycroftAI/skill-playback-control)  
**Owner:** | [@MycroftAI](https://github.com/MycroftAI)  
**Created:** | 2017-06-14T11:25:44Z  **Last updated:** 2019-11-29T16:20:35Z  
**License:** | [Apache License 2.0](https://api.github.com/licenses/apache-2.0)  
**Market status:** | [In Market](https://market.mycroft.ai/skill/mycroft-playback-control)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
