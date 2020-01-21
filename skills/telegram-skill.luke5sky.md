---
description: A skill to connect a telegram bot to MyCroft
---
You need to create a telegram bot (via BotFather) and save the Bot Token, your ChatID and your MyCroft Device name on home.mycroft.ai under skill settings.
After this restart your MyCroft Unit.
You can now commmunicate with your MyCroft Unit via this bot.

Settings:
- BOT TOKEN (MANDATORY): Your bot token you got from BotFather
- MYCROFT DEVICE NAME (MANDATORY): Your Device name you configured on home.mycroft.ai - Devices - Registered Devices
- BOT TOKEN SECOND MYCROFT DEVICE (OPTIONAL): If you have a second Mycroft Device and you want to use this skill with it -> put your second bot token here (it has to be an other bot than the first one because telegram only allows one device to get updates from one bot)
- SECOND MYCROFT DEVICE NAME (IF YOU HAVE A SECOND DEVICE): Your Device name from your second Device you configured on home.mycroft.ai - Devices - Registered Devices
- USERNAME 1 (OPTIONAL): You do not need to put anything here, the skill does not use this field. It is only for yourself to know which Chat ID belongs to whom
- CHAT ID 1 (MANDATORY): You will get your Chat ID from the Telegram-Skill if you have configured BOT TOKEN (first field) and MYCROFT DEVICE NAME, saved and then write anything to the bot.
- USERNAME 2 (OPTIONAL): For second User if you have one
- CHAT ID 2 (IF YOU HAVE A SECOND USER): Same as CHAT ID 1 with Telegram-Account of second user

Detailed HowTo:

- Install this skill on your Mycroft Device

- Create a telegram bot:
Open Telegram App on your smartphone, click on the search symbol in the upper right corner<br/>
Search for BotFather and click on it<br/>
Now type /newbot hit enter<br/>
Botfather should reply with: Alright, a new bot. How are we going to call it? please chosse a name for your bot.<br/>
Give your bot a displayname like Mycroft<br/>
Botfather should reply with: Good. Now let's choose a username for your bot. It must end in bot. Like this, for example: TetrisBot or tetris-bot.<br/>
Give your bot unique username like lukesmycroftbot<br/>
Botfather should now give you your token for this bot<br/>
Save this token and don't post it online or send it to people, safety first!<br/>

Telegram documentation on botfather: https://core.telegram.org/bots#6-botfather

- Go to home.mycroft.ai - skills and search for the telegram-skills settings

- Copy/paste your token botfather gave you in the field BOT TOKEN (MANDATORY)

- Copy/paste your device name from home.mycroft.ai - devices in MYCROFT DEVICE NAME (MANDATORY)

- SAVE and wait till the settings are synced to your Mycroft Unit (or reboot your device to trigger the sync)

- Open Telegram App on your smartphone and search (upper right corner) for your bot (username or displayname) click on it and write test or hello to your bot
It should respond with: This is your ChatID: YOURCHATID

- Copy/paste this under CHAT ID 1 (MANDATORY)

- reboot your device to trigger the sync

- Your bot should send you this welcome message: Telegram-Skill on Mycroft Unit YOURUNIT is loaded and ready to use.

**Github:** | (https://github.com/luke5sky/telegram-skill)  
**Owner:** | [@luke5sky](https://github.com/luke5sky)  
**Created:** | 2018-07-04T10:49:00Z  **Last updated:** 2019-10-20T20:17:48Z  
**License:** | [Apache License 2.0](https://api.github.com/licenses/apache-2.0)  
**Market status:** | [In Market](https://market.mycroft.ai/skill/telegram)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
**Tags:** \#messenger \#bot \#telegram-bot   
{% hint style="info" %}
This skill is in Mycroft Market. That means it is aproved by the Mycroft Skill testers
{% endhint %}
  {% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Telegram
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Telegram```
{% endtab %}
  {% endtabs %}
  