---
description: Play downloaded mp3 files on your Music path with MycroftAI on Linux
---

### _local-music-skill.thevirtuoso1973_  
## Description:  
This is a 'skill'/add-on for the MycroftAI assistant that lets you play mp3 files on your computer.

Mycroft currently looks through the files in `~/Music` (`/home/Music`) path to see if the song mentioned is present.
You can edit the code in `__init__.py` if you want it to look through another directory.

It compares the filenames to the user's request and plays the matching song, if a match is confident enough.

N.B. you can put a bunch of mp3 files in a folder and ask it to play _folder name_ and it'll play all the songs in that folder. Great for albums!  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Play Money by Pink Floyd.  
> Pause.  
> Resume.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/thevirtuoso1973/local-music-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/thevirtuoso1973/local-music-skill](https://github.com/thevirtuoso1973/local-music-skill)  
**Owner:** [@thevirtuoso1973](https://github.com/thevirtuoso1973)  
**Created:** 2019 Aug 11 16:09:10 UTC  **Last updated:** 2020 Jan 01 14:53:10 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Music ] [ Entertainment ] [ IoT ] [ Media ]   
**Tags:** \#music \#linux \#listen \#downloaded   
