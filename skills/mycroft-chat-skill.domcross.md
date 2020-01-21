---
description: The Mycroft Chat allows you to interact with other community users. This skill allows you to monitor Mycroft Chat and find out if you have been mentioned or if there are unread messages. The messages can be read to you by Mycroft as well
---
In your [skill settings](https://home.mycroft.ai) you must enter your username (as given in your Mycroft Chat account settings) and your personal access token.
In case you do not have a token you can specify your login-id (usually that is your email) and your password.
NOTE: your password will be stored in clear text in your settings.json!)

There is also the option to set the time interval between refresh/check for updates.
When monitoring is active the skill will use that time period for automated checking.
The option "notify on updates" is only applicable when monitoring is active -
when the option is activated Mycroft willl speak out loud the number of unread messages and mentions.

**Github:** | (https://github.com/domcross/mycroft-chat-skill)  
**Owner:** | [@domcross](https://github.com/domcross)  
**Created:** | 2018-12-07T18:43:59Z  **Last updated:** 2019-10-27T19:29:12Z  
**License:** | [Apache License 2.0](https://api.github.com/licenses/apache-2.0)  
**Market status:** | [In Market](https://market.mycroft.ai/skill/mycroft-chat)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
**Tags:** \#chat \#mattermost \#[![Say \#Thanks \#to \#the \#author \#of \#this \#skill!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/domcross)   
{% hint style="info" %}
This skill is in Mycroft Market. That means it is aproved by the Mycroft Skill testers
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Mycroft Chat
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Mycroft Chat```
{% endtab %}
  {% endtabs %}
  