---
description: Play music via your Mopidy Server
---

### _mopidy_skill.forslund_  
## Description:  
Mopidy is an extensible stand alone music server handling music libraries and remote services alike. This skill interfaces with the server through the REST api.

### Mycroft Setup

Mycroft needs to be pointed to the mopidy server, this is easily done using the skill settings page on Mycroft-Home. By default it will try to connect to a mopidy server on localhost.

### Mopidy Setup

I recommend using the official [mopidy install guide](https://docs.mopidy.com/en/latest/installation/) to get the software for your specific system.

In addition to the base installation of mopidy the skill REQUIRES the local-mysql plugin to fetch the metadata from the local library and should be able to use the data from the `mopidy-gmusic` plugin.

Mopidy configuration is complex and this description will only touch the areas that are relevant for the skill. Mopidy settings are made in *~/.config/mopidy/mopidy.conf* for a desktop install and under */etc/mopidy/mopidy.conf* for picroft/Mark-1 (if it doesn't exist it needs to be created).

This readme only covers the basics, for more details check out the official documentation at https://www.mopidy.com

#### Local music

For playing music from the local file system or file share check under the heading

` [local] `

and make sure the following config options are set according to your system

```
enabled = true
library = sqlite
media_dir = PATH_TO_YOUR_MUSIC
```

after this is done scan the local collection by running

` mopidy local scan `  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Play Armikrog OST.  
> Play something by Terry Scott Taylor.  
> Play rock music.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/forslund/mopidy_skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/forslund/mopidy_skill](https://github.com/forslund/mopidy_skill)  
**Owner:** [@forslund](https://github.com/forslund)  
**Created:** 2016 Oct 28 05:52:28 UTC  **Last updated:** 2020 Jan 19 08:24:16 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ Music ]   
**Tags:** \#mopidy \#music   
