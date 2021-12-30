---
description: Fallback using any offline AIML2.0 chatbot
---

### _fallback-chatbot.Fantailed_  
## Description:  
**WARNING**: Do NOT install this skill if you aren't at least somewhat familiar with linux as it WILL break your Picroft installation!!!
Because of the mere size of Program-Y, there are a few incompatibilities and installation difficulties that have to be manually resolved.
Please read the whole description before proceeding.


This skill makes use of the offline Python AIML2.0 interpreter Program-Y.


At the moment, it only supports my own stupid bot called BakaBot, but adding your own bots will be supported very soon.

Some dependencies of Program-Y have to be installed with a pip version prior to 10. If the automatic installation of dependencies doesn't work, try downgrading to pip 9.0.3 first:
`pip install pip==9.0.3`.

Then, install Program-Y manually using `pip install programy`.

This will break Mycroft in its current state as one of the dependencies requires `websocket-client>=0.35.0` to work. As a result, pip will update websocket-client to a version that Mycroft in turn does not support anymore. Downgrade to 0.35.0 and you should be fine:

```pip install websocket-client==0.35.0```

If the lxml install fails, do the following:
```
sudo apt install -y libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo pip3 install lxml
```
Note that the installation of lxml can be _very_ slow on low RAM devices like the Raspberry Pi (I am talking in the order of 10min+!). If you
ever doubt that it's even doing anything, open another terminal and run `htop` on it.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
  
### Examples:  
> My name is Dave.  
> What is my name?  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/Fantailed/fallback-chatbot```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/Fantailed/fallback-chatbot](https://github.com/Fantailed/fallback-chatbot)  
**Owner:** [@Fantailed](https://github.com/Fantailed)  
**Created:** 2018 Nov 26 21:57:05 UTC  **Last updated:** 2018 Nov 29 15:35:16 UTC  
**License:** Other  
  
**Categories:** [ Entertainment ] [ Daily ]   
**Tags:** \#\chatbot \#\aiml \#\aiml2.0   
