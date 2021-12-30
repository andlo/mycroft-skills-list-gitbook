---
description: 
---

### _wally-kc-streetcar.bw3740_  
## Description:  
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions.

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page, with a routeID and directionID, makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop. Keep in mind some intersections have 2 stops, so direction matters.

This skill is still in it's early stages of development. With the planned expansions of the line, there will be tweaks needed. This is for the good of the KC and Mycroft communities, so please add/suggest new features.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Kc street car at third.  
> Kansas city streetcar at ninth heading north.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/bw3740/wally-kc-streetcar```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/bw3740/wally-kc-streetcar](https://github.com/bw3740/wally-kc-streetcar)  
**Owner:** [@bw3740](https://github.com/bw3740)  
**Created:** 2018 Feb 22 22:43:14 UTC  **Last updated:** 2019 Jun 05 15:06:37 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ uncategorized ]   
