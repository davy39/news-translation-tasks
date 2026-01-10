---
title: 'Convertisseur d''heure sur 24 heures : comment convertir AM/PM en heure sur
  24 heures'
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
seo_title: 'Convertisseur d''heure sur 24 heures : comment convertir AM/PM en heure
  sur 24 heures'
seo_desc: 'There are two primary methods of showing the time. First there''s the 12
  hour clock that uses AM and PM, and then there''s the 24 hour clock.

  Most countries prefer the 24 hour clock method, but the 12 hour clock is widely
  used in Latin America and Engl...'
---

Il existe deux méthodes principales pour afficher l'heure. Tout d'abord, il y a l'**horloge sur 12 heures** qui utilise **AM** et **PM**, puis il y a l'**horloge sur 24 heures**.

La plupart des pays préfèrent la méthode de l'horloge sur 24 heures, mais l'horloge sur 12 heures est largement utilisée en Amérique latine et dans les pays anglophones. Dans la méthode de l'horloge sur 12 heures, il est 12:00 deux fois par jour à minuit (AM) et à midi (PM).

Le tableau ci-dessous montre la conversion entre les systèmes d'horloge sur 12 heures et sur 24 heures :

| Horloge 12 heures | Horloge 24 heures |
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


### Horloge sur 12 heures

La journée est divisée en deux périodes de 12 heures allant de minuit à midi (heures AM), et de midi à minuit (heures PM).

Les abréviations AM et PM proviennent du latin :

* AM : _ante meridiem_, avant midi
* PM : _post meridiem_, après midi

### Horloge sur 24 heures

La journée va de minuit à minuit et est divisée en 24 heures de 0 (minuit) à 23. L'heure est affichée en heures et minutes depuis minuit.

## Conversion d'une horloge 12 heures en horloge 24 heures

À partir de la première heure de la journée (12:00 AM ou minuit à 12:59 AM), soustrayez 12 heures :

* 12:00 AM = 0:00
* 12:15 AM = 0:15

De 1:00 AM à 12:59 PM, les heures et les minutes restent les mêmes :

* 9:00 AM = 9:00
* 12:59 PM = 12:59

Pour les heures entre 1:00 PM et 11:59 PM, ajoutez 12 heures :

* 3:17 PM = 15:17
* 11:59 PM = 23:59

## Conversion d'une horloge 24 heures en horloge 12 heures

À partir de la première heure de la journée (0:00 / minuit à 0:59), ajoutez 12 heures et AM à l'heure :

* 0:30 = 12:30 AM
* 0:55 = 12:55 AM

De 1:00 à 11:59, ajoutez simplement AM à l'heure :

* 2:25 = 2:25 AM
* 9:30 = 9:30 AM

Pour les heures entre 12:00 à 12:59, ajoutez simplement PM à l'heure :

* 12:15 = 12:15 PM
* 12:48 = 12:48 PM

Pour les heures entre 13:00 à 23:59, soustrayez 12 heures et ajoutez PM à l'heure :

* 16:55 = 4:55 PM
* 21:45 = 9:45 PM