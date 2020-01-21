---
description: Mycroft reports real-time pollutant levels in your city
---
Air Quality

Get real-time air quality data for more than 1000 cities from
the [World Air Quality Index](https://aqicn.org/) (WAQI) project.

By default, Mycroft reports **real-time** (most recent,
one-hour average) fine particulate matter (PM 2.5) concentration
levels at a monitoring station in your city. You can also ask
Mycroft for PM 10, carbon monoxode (CO), nitrogen dioxide
(NO<sub>2</sub>), and sulphur dioxide (SO<sub>2</sub>) levels at
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

**Github:** | (https://github.com/kalyaninagaraj/air-quality-skill)  
**Owner:** | [@kalyaninagaraj](https://github.com/kalyaninagaraj)  
**Created:** | 2019-12-09T16:34:56Z  **Last updated:** 2019-12-27T14:13:06Z  
**License:** | [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
