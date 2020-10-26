---
description: Installs and setup THEIA IDE locally on your device. Real VS Code experience
---

### _theia-ide-skill.andlo_  
## Description:  
This skill installs Theia IDE on your Mycroft device. This is an easy way to make and edit skills
with integratio to Github, and tools like mycroft-msm and mycroft-msk directly from the integrated
shell.

Theia provides Microsoft VS Code experience in the browser.

### New in this release
* Installer rewrite so picroft is downloading precompiled package and prepaired for other precompiled
packages for other platforms. Installer wil always install latest Theia-for-Mycroft from
https://github.com/andlo/theia-for-mycroft/
* Installer Builds and compile on systems where there isnt precompiled package for if system has more
than 4 Gb memmory.
* No more support for Mark_1 as debian jessie isnt supported and theia cant build properly.
* Added workspace setting on home.mycroft.at. Default to skills directory.
* Debug is working by using PTVSD, but requere remote-debug skill to activate and inject
debug adaptor https://github.com/andlo/remote-debug-skill and change settings for padatious
single_thread. remote-debug skills is at time of writing on way to market and PR to makea setting
for controling padatious single_thread is on its way to mycroft.core.


https://www.theia-ide.org/index.html

  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Run IDE.  
> End theia IDE.  
> Restart IDE.  
  
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install THEIA IDE
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install THEIA IDE```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/andlo/theia-ide-skill](https://github.com/andlo/theia-ide-skill)  
**Owner:** [@andlo](https://github.com/andlo)  
**Created:** 2018 Nov 05 20:34:10 UTC  **Last updated:** 2020 Oct 26 08:49:09 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/theia-ide)  
**Categories:** [ Productivity ]   
**Tags:** \#theia \#IDE \#editor \#dev \#vscode   
