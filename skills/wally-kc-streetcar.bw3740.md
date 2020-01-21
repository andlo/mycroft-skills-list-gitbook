---
description: 
---
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions.

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page, with a routeID and directionID, makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop. Keep in mind some intersections have 2 stops, so direction matters.

This skill is still in it's early stages of development. With the planned expansions of the line, there will be tweaks needed. This is for the good of the KC and Mycroft communities, so please add/suggest new features.

**Github:** | (https://github.com/bw3740/wally-kc-streetcar)  
**Owner:** | [@bw3740](https://github.com/bw3740)  
**Created:** | 2018-02-22T22:43:14Z  **Last updated:** 2019-06-05T15:06:37Z  
**License:** | [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/bw3740/wally-kc-streetcar```
{% endtab %}
  {% endtabs %}
  