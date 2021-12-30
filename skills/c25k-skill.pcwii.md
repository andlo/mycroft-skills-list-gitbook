---
description: Use mycroft.ai as a fitness coach and work your way through the 9 week Couch to 5km running program
---

### _c25k-skill.pcwii_  
## Description:  
Mycroft.ai becomes your motivational coach as you work your way through each of the intervals in the workout.
* Depending on the length of the current interval motivations will be provided at the 1/4, 1/2, 3/4
points of the interval.
This skill uses a schedule json (c25k.json) to track and support you as you work
through the couch to 5k running program.
The default c25k.json file is based on the Couch to 5 km running program.
Other workout json files could be created based on this and selected from the websettings.

The skill will keep track of the last week #, day # that you completed and proceed through each day
of the workout found in the json file.
* The skill will loose this information if the mycroft is rebooted or the skill is updated.
- Mycroft does not properly push websettings changes in skills to the web ui.
- I will work to address this in future updates (20200202).  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Start my workout.  
> Start my run.  
> I want to run.  
> Change my workout to week 3 day 4.  
> [ ] WIP (20200202)  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/pcwii/c25k-skill](https://github.com/pcwii/c25k-skill)  
**Owner:** [@pcwii](https://github.com/pcwii)  
**Created:** 2020 Jan 23 20:44:46 UTC  **Last updated:** 2020 May 12 20:14:31 UTC  
**License:** No License  
  
**Categories:** [ Fitness ]   
**Tags:** \#C25K \#fitness \#running \#workout   
