---
description: 
---

### _skill-score.deejcunningham_  
## Description:  
Skill-score is an application that enables Mycroft to answer user questions about Major League Baseball (MLB) scores. [Mycroft](https://mycroft.ai) is an open-source AI voice assistant. Skill-score uses [panzarino's mlbgame API](https://github.com/panzarino/mlbgame) to report an MLB team's latest final scores, including live scores.

User input has the format:
"What is the {team}'s score?"

If a game is in progress, Mycroft will respond:
"The {team} are winning/losing {score} to {score} against the {opponent} in the top/middle/bottom/end of the {inning}."

If a game is not in progress, Mycroft will respond:
"The {team} won/lost {score} to {score} against the {opponent} {number-of-days} ago."

### Next Goals

The next goals for skill-score are the ability to:
* give the time of the next MLB game; and
* support more leagues (e.g., National Football League, National Basketball League), depending on available APIs.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> What is the Royals score?  
> What is the Angels score?  
> What is the Yankees score?  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/deejcunningham/skill-score```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/deejcunningham/skill-score](https://github.com/deejcunningham/skill-score)  
**Owner:** [@deejcunningham](https://github.com/deejcunningham)  
**Created:** 2018 May 17 23:56:07 UTC  **Last updated:** 2019 Oct 29 21:49:58 UTC  
**License:** MIT License  
  
**Categories:** [ uncategorized ]   
