---
description: 
---

### _PFE1718-automation-handler.PFE1718_  
## Description:  
The automation-handler skill is part of the [**habits automation system**](https://github.com/PFE1718/mycroft-habits-automation) that aims to detect the **user habits** when using [Mycroft](https://mycroft.ai/), and to offer automation of these identified habits. You can find a detailed definition of a **habit** on the [project page](https://github.com/PFE1718/mycroft-habits-automation).

This skill allows you to automate some of the habits that Mycroft has detected and it handles their automation. When you first reproduce a detected habit, Mycroft will ask you if this habit should be automatized.

The habit detection is done by two other complementary skills:
1. The [**skill-listener**](https://github.com/PFE1718/mycroft-skill-listener), that logs the user activity. It is also  responsible for launching the 2 other skills when needed.
2. The [**habit-miner**](https://github.com/PFE1718/mycroft-habit-miner-skill), that extracts the habits of the user from the logs.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> List my habits.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/PFE1718/PFE1718-automation-handler```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/PFE1718/PFE1718-automation-handler](https://github.com/PFE1718/PFE1718-automation-handler)  
**Owner:** [@PFE1718](https://github.com/PFE1718)  
**Created:** 2018 Jan 08 14:38:15 UTC  **Last updated:** 2018 Nov 19 08:46:17 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ uncategorized ]   
