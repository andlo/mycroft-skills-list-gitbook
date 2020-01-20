---
description: 
---
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions.

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page, with a routeID and directionID, makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop. Keep in mind some intersections have 2 stops, so direction matters.

This skill is still in it's early stages of development. With the planned expansions of the line, there will be tweaks needed. This is for the good of the KC and Mycroft communities, so please add/suggest new features.

**Github:** | (https://github.com/bw3740/nerdery-kc-streetcar)

**Owner:** | [@bw3740](https://github.com/bw3740) ![avatart](https://avatars2.githubusercontent.com/u/8460730?v=4)

