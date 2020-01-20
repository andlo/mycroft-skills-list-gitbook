---
description: Common playback control system
---
This Skill doesn't do anything by itself, but it provides an important common
language for audio playback skills.  By handling simple phrases like
'pause', this one Skill can turn around and rebroadcast the [messagebus](https://mycroft.ai/documentation/message-bus/)
command `mycroft.audio.service.pause`, allowing several music services to share
common terminology such as "pause".

Additionally, this implements the common Play handler.  This allows playback
services to negotiate which is best suited to play back a specific request.
This capability is used by the [Spotify](https://github.com/forslund/spotify-skill) and [Pandora](https://github.com/mycroftai/pianobar-skill) Skills, among others.

**Github:** (https://github.com/MycroftAI/skill-playback-control)

**Owner:** [@MycroftAI](https://github.com/MycroftAI) ![avatart](https://avatars0.githubusercontent.com/u/14171097?v=4)

