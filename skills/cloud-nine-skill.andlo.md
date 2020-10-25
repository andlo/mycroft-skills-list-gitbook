---
description: Installs and configure a local Cloud9 IDE
---

### _cloud-nine-skill.andlo_  
## Description:  
This skill installs and configure a local Cloud9 IDE for use to make, edit and manipulate skills on a Mycroft device.

Cloud9 is a full blown IDE accesable throug a webbrowser. That makes it ideal to make and devolep skills to and on a Mycroft device
It also includes a fulls shell so using git to push and pull is easyly done. Offcause alsp specifik Mycroft stuff like mycroft-msk can be run directly from here.

This is a local installation on your devices. So no data or anything to do whith Amazon AWS, Cloud9 and related online services.

#### How to install Cloud Nine Skill
Install Cloud Nine skill by …
```
msm install https://github.com/andlo/cloud-nine-skill.git
```
Install will install some exras on your device. That is nodejs, tmux and sqlite.
Initialazion will take quite some time and includes
* git download of c9.core
* compiling c9 node modules and extras
* setting up workspace

Duing install there is a lot of output in the log. It should however endup with the line “Cloud9 is up and running”

#### How to remove Cloud Nine Skill
Remove Cloud Nine Skill by …
```
msm remove cloud-nine
```
After that delete /home/pi/.mycroft/skills/CloudNine and subfolders. Also delete /home/pi/,c9 and /home/pi/node-gyp
and if not needed by other skills
```
apt-get remove nodejs tmux sqlite3 node-sqlite3
```  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)   
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/andlo/cloud-nine-skill](https://github.com/andlo/cloud-nine-skill)  
**Owner:** [@andlo](https://github.com/andlo)  
**Created:** 2018 Oct 26 17:11:47 UTC  **Last updated:** 2018 Nov 27 20:54:45 UTC  
**License:** No License  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ Configuration ] [ Productivity ]   
**Tags:** \#Cloud9 \#C9 \#IDE \#Dev   
