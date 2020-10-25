---
description: A skill to control your Mycroft instance through a TelegramBot
---

### _telegram-skill.luke5sky_  
## Description:  
You need to create a telegram bot (via BotFather) and save the Bot Token, your ChatID and your MyCroft Device name on home.mycroft.ai under skill settings.
You can now commmunicate with your MyCroft Unit via this bot.

Settings:
- BOT TOKEN (MANDATORY): Your bot token you got from BotFather
- DEVICE NAME (CASE SENSITIVE | MANDATORY): Your Device name you configured on home.mycroft.ai - Devices - Registered Devices
- BOT TOKEN SECOND MYCROFT DEVICE (OPTIONAL): If you have a second Mycroft Device and you want to use this skill with it -> put your second bot token here (it has to be an other bot than the first one because telegram only allows one device to get updates from one bot)
- SECOND MYCROFT DEVICE NAME (IF YOU HAVE A SECOND DEVICE): Your Device name from your second Device you configured on home.mycroft.ai - Devices - Registered Devices
- PRIMARY USERNAME (OPTIONAL): You do not need to put anything here, the skill does not use this field. It is only for yourself to know which Chat ID belongs to whom
- PRIMARY CHAT ID (MANDATORY): You will get your Chat ID from the Telegram-Skill if you have configured BOT TOKEN (first field) and DEVICE NAME, saved and then write anything to the bot.
- SECOND USERNAME (OPTIONAL): For second User if you have one
- SECOND CHAT ID (IF YOU HAVE A SECOND USER): Same as PRIMARY CHAT ID with Telegram-Account of second user

Detailed HowTo:

- Install this skill on your Mycroft Device

- Create a telegram bot:
Open Telegram App on your smartphone, click on the search symbol in the upper right corner
Search for BotFather and click on it
Now type /newbot hit enter
Botfather should reply with: Alright, a new bot. How are we going to call it? please chosse a name for your bot.
Give your bot a displayname like Mycroft
Botfather should reply with: Good. Now let's choose a username for your bot. It must end in bot. Like this, for example: TetrisBot or tetris-bot.
Give your bot unique username like lukesmycroftbot
Botfather should now give you your token for this bot
Save this token and don't post it online or send it to people, safety first!

Telegram documentation on botfather: https://core.telegram.org/bots#6-botfather

- Go to home.mycroft.ai - skills and search for the telegram-skills settings

- Copy/paste your token botfather gave you in the field BOT TOKEN (MANDATORY)

- Copy/paste your device name from home.mycroft.ai - devices in DEVICE NAME (CASE SENSITIVE | MANDATORY)

- SAVE and wait till the settings are synced to your Mycroft Unit (or reboot your device to trigger the sync)

- Open Telegram App on your smartphone and search (upper right corner) for your bot (username or displayname) click on it and write test or hello to your bot
It should respond with: This is your ChatID: YOURCHATID

- Copy/paste this under PRIMARY CHAT ID (MANDATORY)

- SAVE and wait till the settings are synced to your Mycroft Unit (or reboot your device to trigger the sync)

- On every reboot your bot should send you this welcome message: Telegram-Skill on Mycroft Unit YOURUNIT is loaded and ready to use.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Telegram
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Telegram```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/luke5sky/telegram-skill](https://github.com/luke5sky/telegram-skill)  
**Owner:** [@luke5sky](https://github.com/luke5sky)  
**Created:** 2018 Jul 04 10:49:00 UTC  **Last updated:** 2020 Oct 15 13:43:21 UTC  
**License:** Apache License 2.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/telegram)  
**Categories:** [ Productivity ] [ IoT ]   
**Tags:** \#messenger \#bot \#telegram-bot   
