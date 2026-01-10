---
title: '24 Hour Clock Converter: How to Convert AM/PM to 24 Hour Time'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-23T17:03:00.000Z'
originalURL: https://freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-cottonbro-5185163.jpg
tags:
- name: how-to
  slug: how-to
- name: projects
  slug: projects
seo_title: null
seo_desc: 'There are two primary methods of showing the time. First there''s the 12
  hour clock that uses AM and PM, and then there''s the 24 hour clock.

  Most countries prefer the 24 hour clock method, but the 12 hour clock is widely
  used in Latin America and Engl...'
---

There are two primary methods of showing the time. First there's the **12 hour clock** that uses **AM** and **PM**, and then there's the **24 hour clock**.

Most countries prefer the 24 hour clock method, but the 12 hour clock is widely used in Latin America and English-speaking countries. In the 12 hour clock method, it is 12:00 twice a day at midnight (AM) and noon (PM).

The table below shows the conversion between the 12 hour and 24 hour clock systems:

| 12 hour clock | 24 hour clock |
|:-------------:|:-------------:|
|12:00 AM |	00:00|
|01:00 AM |	01:00|
|02:00 AM |	02:00|
|03:00 AM |	03:00|
|04:00 AM |	04:00|
|05:00 AM |	05:00|
|06:00 AM |	06:00|
|07:00 AM |	07:00|
|08:00 AM |	08:00|
|09:00 AM |	09:00|
|10:00 AM |	10:00|
|11:00 AM |	11:00|
|12:00 PM |	12:00|
|01:00 PM |	13:00|
|02:00 PM |	14:00|
|03:00 PM |	15:00|
|04:00 PM |	16:00|
|05:00 PM |	17:00|
|06:00 PM |	18:00|
|07:00 PM |	19:00|
|08:00 PM |	20:00|
|09:00 PM |	21:00|
|10:00 PM |	22:00|
|11:00 PM |	23:00|


### 12 Hour Clock

The day is split into two 12 hour periods running from midnight to noon (AM hours), and noon to midnight (PM hours).

The abbreviations AM and PM are from Latin:

* AM: _ante meridiem,_ before midday
* PM: _post meridiem_, after midday

### 24 Hour Clock

The day runs from midnight to midnight and is divided into 24 hours from 0 (midnight) to 23. Time is shown in hours and minutes since midnight.

## Converting from a 12 Hour to a 24 Hour Clock

Starting from the first hour of the day (12:00 AM or midnight to 12:59 AM), subtract 12 hours:

* 12:00 AM = 0:00
* 12:15 AM = 0:15

From 1:00 AM to 12:59 PM, the hours and minutes remain the same:

* 9:00 AM = 9:00
* 12:59 PM = 12:59

For times between 1:00 PM to 11:59 PM, add 12 hours:

* 3:17 PM = 15:17
* 11:59 PM = 23:59

## Converting from a 24 Hour to a 12 Hour Clock

Starting from the first hour of the day (0:00 / midnight to 0:59), add 12 hours and AM to the time:

* 0:30 = 12:30 AM
* 0:55 = 12:55 AM

From 1:00 to 11:59, simply add AM to the time:

* 2:25 = 2:25 AM
* 9:30 = 9:30 AM

For times between 12:00 to 12:59, just add PM to the time:

* 12:15 = 12:15 PM
* 12:48 = 12:48 PM

For times between 13:00 to 23:59, subtract 12 hours and add PM to the time:

* 16:55 = 4:55 PM
* 21:45 = 9:45 PM

