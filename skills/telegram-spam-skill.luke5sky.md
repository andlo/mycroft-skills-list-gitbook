---
description: A skill to connect a telegram bot to MyCroft. THIS SKILL IS NOT GETTING ANY UPDATES!  This will se
---

### _telegram-spam-skill.luke5sky_  
## Description:  
You need to create a telegram bot (via BotFather) and save the Bot Token, your ChatID and your MyCroft Device name on home.mycroft.ai under skill settings.
After this restart your MyCroft Unit.
You can now commmunicate with your MyCroft Unit via this bot.

Settings:
- BOT TOKEN (MANDATORY): Your bot token you got from BotFather
- MYCROFT DEVICE NAME (MANDATORY): Your Device name you configured on home.mycroft.ai - Devices - Registered Devices
- USERNAME (OPTIONAL): You do not need to put anything here, the skill does not use this field. It is only for yourself to know which Chat ID belongs to whom
- CHAT ID (MANDATORY): You will get your Chat ID from the Telegram-Skill if you have configured BOT TOKEN (first field) and MYCROFT DEVICE NAME, saved and then write anything to the bot.

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

- Copy/paste your device name from home.mycroft.ai - devices in MYCROFT DEVICE NAME (MANDATORY)

- SAVE and wait till the settings are synced to your Mycroft Unit (or reboot your device to trigger the sync)

- Open Telegram App on your smartphone and search (upper right corner) for your bot (username or displayname) click on it and write test or hello to your bot
It should respond with: This is your ChatID: YOURCHATID

- Copy/paste this under CHAT ID (MANDATORY)

- reboot your device to trigger the sync

- Your bot should send you this welcome message: Telegram-Skill on Mycroft Unit YOURUNIT is loaded and ready to use.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/luke5sky/telegram-spam-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/luke5sky/telegram-spam-skill](https://github.com/luke5sky/telegram-spam-skill)  
**Owner:** [@luke5sky](https://github.com/luke5sky)  
**Created:** 2019 Jan 04 10:25:15 UTC  **Last updated:** 2020 Oct 15 14:25:55 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Productivity ] [ IoT ]   
**Tags:** \#messenger \#bot \#telegram-bot   
