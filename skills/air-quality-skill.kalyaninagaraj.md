---
description: Mycroft reports real-time pollutant levels in your city
---

### _air-quality-skill.kalyaninagaraj_  
## Description:  
Get real-time air quality data for more than 1000 cities from
the [World Air Quality Index](https://aqicn.org/) (WAQI) project.

By default, Mycroft reports **real-time** (most recent,
one-hour average) fine particulate matter (PM 2.5) concentration
levels at a monitoring station in your city. You can also ask
Mycroft for PM 10, carbon monoxode (CO), nitrogen dioxide
(NO2), and sulphur dioxide (SO2) levels at
your location or in other cities. Mycroft will also report how
long back the reading was taken if the measurements were made more
than two hours ago, and a health cautionary statement (only for
PM 2.5 concentration levels) as suggested by the WAQI project.

The Air Quality skill requires an API key to access data from
the World Air Quality Index project. For instructions to obtain
a key, go to the skill settings in your Mycroft account. The
WAQI project's terms of acceptable data and API usage apply.

### Things to note
* Several stations record ozone levels but the WAQI project's
API doesn't mention the units (ppb, or milligrams per cubic meter).
So, for the present, this skill doesn't report ozone levels.
* Different government agencies have different air quality standards,
resulting in different nations using different air quality indices. To
standardize the reporting, this skill reports *raw* concentration
levels measured in micrograms per cubic meter.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> What is the air quality?  
> How polluted is the air in New Delhi?  
> What is the carbon monoxide level in Hong Kong?  
> What's the ozone level in Dublin?  
> What's the PM 10 level in Portland?  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/kalyaninagaraj/air-quality-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/kalyaninagaraj/air-quality-skill](https://github.com/kalyaninagaraj/air-quality-skill)  
**Owner:** [@kalyaninagaraj](https://github.com/kalyaninagaraj)  
**Created:** 2019 Dec 09 16:34:56 UTC  **Last updated:** 2019 Dec 27 14:13:06 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ Daily ] [ Information ]   
**Tags:** \#Air \#quality \#Pollutant \#level \#Mycroft \#AI   
