---
description: Listen to music from your Spotify Premium music account
---

### _mycroft-spotify-skill.Mel1818_  
## Description:  
Stream your favorite music from the popular Spotify music service.  Spotify
Premium users can search and play tracks from their own playlists or the huge
Spotify music library.

You can also control your Mycroft device using the Spotify Connect system.
So play DJ on your phone while listening on Mycroft!

### Authorization:
This Skill uses two different methods of authentication. Both need to be filled in correctly for the **Skill** to function correctly.

#### API connection to your Spotify account
After installing `mycroft-spotify`, in your [Skill
settings for Spotify](https://home.mycroft.ai/#/skill) in home.mycroft.ai you will see settings for the Spotify Skill. You will see a username and password field and a 'Connect' button. Ignore the username and password field for now, and click the 'Connect' button. You will be prompted to log in to Spotify, and to authorize Mycroft AI to use your Spotify account using OAuth. This allows Mycroft access to your account details such as Playlists.

#### Username and password to authenticate a Mycroft device
In addition to account details, Mycroft needs to be authorized as a **device** for Spotify. To do this, we use your username and password for Spotify. These must be entered as well, or you will receive an error message like:

`I couldn't find any Spot-ify devices.  This skill requires a Spotify Premium account to work properly.`

when you try to use the **Skill** on a Mycroft device.

If you log in to Spotify using Facebook, your password will be your _Facebook_ password, but your Spotify device username. You can get your Spotify device username [here](https://www.spotify.com/us/account/set-device-password/).

_NOTE: You MUST have a Premium Spotify account to use this **Skill**. It will NOT work with a free Spotify account._  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> What Spotify devices are available?  
> Play discover weekly.  
> Search Spotify for Hello Nasty.  
> Play something by Coventant.  
> Play the album Hello Nasty on Spotify.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/Mel1818/mycroft-spotify-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/Mel1818/mycroft-spotify-skill](https://github.com/Mel1818/mycroft-spotify-skill)  
**Owner:** [@Mel1818](https://github.com/Mel1818)  
**Created:** 2019 Sep 04 12:50:47 UTC  **Last updated:** 2019 Sep 04 18:30:58 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Music ]   
**Tags:** \#spotify \#music   
