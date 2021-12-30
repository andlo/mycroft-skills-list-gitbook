---
description: Listen to music from your Spotify Premium music account.  **Spotify has disabled the API access for 
---

### _spotify-skill.forslund_  
## Description:  
Stream your favorite music from the popular Spotify music service. Spotify
Premium users can search and play tracks from their own playlists or the huge
Spotify music library.

You can also control your Mycroft device using the Spotify Connect system.
So play DJ on your phone while listening on Mycroft!

### This skill doesn't do any playback
This skill works with the Spotify Connect protocol to interact with Spotify devices, but doesn't perform any playback itself. If you want playback on the hosting Mycroft device, you'll need to set up a player yourself.

For Picroft users, [raspotify](https://github.com/dtcooper/raspotify) is a good choice.

Install it and then make changes to `/etc/default/raspotify.conf` as follows

- It is recommended to set the DEVICE_NAME to the name of the Mycroft unit (as registered at home.mycroft.ai) for automatic identification:

`DEVICE_NAME=""

- set your Spotify username and password under `OPTIONS`

`OPTIONS="--username  --password "`


You make sound work with raspotify you may need to edit `/lib/systemd/system/raspotify.service` and there change `User` and `Group` from `raspotify`to `pi`.


For desktop users the official spotify player works well.

The exception to this is the Mark-1 which is shipped with a spotify player library.

### Authorization:
This Skill uses two different methods of authentication. Both need to be filled in correctly for the **Skill** to function correctly.

#### Personal Access Token

##### Creating access token
From the [Spotify developer dashboard](https://developer.spotify.com/dashboard/)

1. Click "CREATE AN APP"
1. Fill out the create application form
1. Click on the new app and choose EDIT SETTINGS
1. Under Redirect URIs add `https://localhost:8888`

More info can be found [here](https://developer.spotify.com/documentation/general/guides/app-settings/).

##### Connecting spotify skill
After installing `mycroft-spotify`, from the mycroft-core folder run the auth.py script in the mycroft-spotify folder

```
source venv-activate.sh
python /opt/mycroft/skills/mycroft-spotify.forslund/auth.py
```

The script will try to guide you through connecting a developer account to the skill and store the credentials locally.

#### Username and password to authenticate a Mycroft device
In addition to account details, Mycroft needs to be authorized as a **device** for Spotify. To do this, we use your username and password for Spotify. These must be entered as well, or you will receive an error message like:

`I couldn't find any Spotify devices.  This skill requires a Spotify Premium account to work properly.`

when you try to use the **Skill** on a Mycroft device.

If you log in to Spotify using Facebook, your password will be your _Facebook_ password, but your Spotify device username. You can get your Spotify device username [here](https://www.spotify.com/us/account/set-device-password/).

_NOTE: You MUST have a Premium Spotify account to use this **Skill**. It will NOT work with a free Spotify account._  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> What Spotify devices are available?  
> Play discover weekly.  
> Play Hello Nasty on Spotify.  
> Play something by Covenant.  
> Play the album Hello Nasty on Spotify.  
> Play my liked songs.  
  
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Play Spotify
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Play Spotify```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/forslund/spotify-skill](https://github.com/forslund/spotify-skill)  
**Owner:** [@forslund](https://github.com/forslund)  
**Created:** 2017 Aug 02 15:15:44 UTC  **Last updated:** 2020 Oct 23 18:23:26 UTC  
**License:** Apache License 2.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/mycroft-spotify)  
**Categories:** [ Music ]   
**Tags:** \#spotify \#music   
