---
title: Comment planifier des tâches ad-hoc avec DynamoDB TTL et Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T00:43:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-ad-hoc-tasks-with-dynamodb-ttl-and-lambda-421fa5778993
coverImage: https://cdn-media-1.freecodecamp.org/images/0*C_kNu0DfEkRCWkxf.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Comment planifier des tâches ad-hoc avec DynamoDB TTL et Lambda
seo_desc: 'By Yan Cui

  CloudWatch Events let you easily create cron jobs with Lambda. However, it’s not
  designed for running lots of ad-hoc tasks, each to be executed once, at a specific
  time. The default limit on CloudWatch Events is a lowly 100 rules per regio...'
---

Par Yan Cui

[CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) vous permet de créer facilement des tâches cron avec Lambda. Cependant, il n'est pas conçu pour exécuter de nombreuses tâches ad-hoc, chacune devant être exécutée une fois, à un moment spécifique. La limite par défaut sur CloudWatch Events est de seulement [100 règles par région par compte](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html). Il s'agit d'une limite souple, il est donc possible de demander une augmentation de la limite. Mais la faible limite initiale suggère qu'elle n'est pas conçue pour des cas d'utilisation où vous devez planifier **des millions de tâches ad-hoc**.

**CloudWatch Events est conçu pour exécuter des tâches récurrentes.**

![Image](https://cdn-media-1.freecodecamp.org/images/lqXGe3MgGpO8atm0UG35G8t3X6-nO0-IwKVU)
_[https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html" rel="noopener" target="_blank" title=")_

### Le Problème

Il est possible de faire cela dans presque tous les langages de programmation. Par exemple, .Net a la classe `[Timer](https://docs.microsoft.com/en-us/dotnet/api/system.timers.timer?view=netframework-4.7.2)` et JavaScript a la fonction `[setInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp)`. Mais je me retrouve souvent à vouloir une abstraction de service avec laquelle travailler. Il existe de nombreux cas d'utilisation pour un tel service, par exemple :

* Un système de tournoi pour jeux aurait besoin d'exécuter une logique métier lorsque le tournoi commence et se termine.
* Un système d'événements (pensez à [eventbrite.com](https://www.eventbrite.com/) ou [meetup.com](https://meetup.com/)) aurait besoin d'un mécanisme pour envoyer des rappels en temps opportun aux participants.
* Un suivi de tâches (pensez à [wunderlist](https://www.wunderlist.com/)) aurait besoin d'un mécanisme pour envoyer des rappels lorsqu'une tâche est due.

Cependant, AWS ne propose pas de service pour ce type de charges de travail. CloudWatch Events est la chose la plus proche, mais comme discuté ci-dessus, il n'est pas destiné aux cas d'utilisation mentionnés. Vous pouvez cependant les implémenter en utilisant des tâches cron. Mais de telles implémentations ont d'autres défis.

J'ai implémenté une telle abstraction de service à plusieurs reprises dans ma carrière. J'ai expérimenté avec plusieurs approches différentes :

* tâche cron (avec CloudWatch Events)
* envelopper la classe .Net `Timer` en tant que point de terminaison HTTP
* utiliser le délai d'attente de visibilité SQS pour masquer les tâches jusqu'à ce qu'elles soient dues

Et récemment, j'ai vu un certain nombre de personnes utiliser [DynamoDB Time-To-Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html) (TTL) pour implémenter ces tâches ad-hoc. Dans cet article, nous allons examiner cette approche et voir où elle pourrait être applicable pour vous.

### Comment mesurons-nous l'approche ?

Pour ce type de tâche ad-hoc, nous nous soucions normalement de :

* **Précision** : à quel point la tâche est exécutée près de l'heure planifiée ? Plus c'est proche, mieux c'est.
* **Échelle (nombre de tâches ouvertes)** : la solution peut-elle évoluer pour supporter de nombreuses tâches ouvertes, c'est-à-dire des tâches qui sont planifiées mais pas encore exécutées ?
* **Échelle (points chauds)** : la solution peut-elle évoluer pour exécuter de nombreuses tâches autour du même moment ? Par exemple, des millions de personnes définissent un minuteur pour se rappeler de regarder le Superbowl, donc tous les minuteurs se déclenchent à proximité de l'heure de coup d'envoi.

### DynamoDB TTL en tant que mécanisme de planification

À haut niveau, cette approche ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4P77Vvmy5ZDOynG2ImgXBdbaEfRKfOmy1fpE)

* Une table DynamoDB `scheduled_items` qui contient toutes les tâches planifiées pour exécution.
* Une fonction `scheduler` qui écrit la tâche planifiée dans la table `scheduled_items`, avec le TTL défini à l'heure d'exécution planifiée.
* Une fonction `execute-on-schedule` qui s'abonne au flux DynamoDB pour `scheduled_items` et réagit aux événements `REMOVE`. Ces événements correspondent à la suppression d'éléments de la table.

#### Évolutivité (nombre de tâches ouvertes)

Puisque le nombre de tâches ouvertes se traduit simplement par le nombre d'éléments dans la table `scheduled_items`, cette approche peut évoluer pour des millions de tâches ouvertes.

DynamoDB peut également gérer de grands débits (des milliers de TPS). Cette approche peut donc également être appliquée à des scénarios où des milliers d'éléments sont planifiés par seconde.

#### Évolutivité (points chauds)

Lorsque de nombreux éléments sont supprimés en même temps, ils sont simplement mis en file d'attente dans le flux DynamoDB. AWS ajuste également automatiquement le nombre de fragments dans le flux, donc à mesure que le débit augmente, le nombre de fragments augmentera en conséquence.

Cependant, les événements sont traités en séquence. Il peut donc falloir un certain temps pour que votre fonction traite l'événement en fonction de :

* sa position dans le flux, et
* le temps qu'il faut pour traiter chaque événement.

Ainsi, bien que cette approche puisse évoluer pour supporter de nombreuses tâches expirant en même temps, elle ne peut pas garantir que les tâches soient exécutées à temps.

#### Précision

C'est une grande question concernant cette approche. Selon la [documentation officielle](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html), les éléments expirés sont supprimés **dans les 48 heures**. C'est une énorme marge d'erreur !

![Image](https://cdn-media-1.freecodecamp.org/images/uubpqNjDRYU8sQFNzf3l6sYT9bUvnVqHWmvx)

En tant qu'expérience, j'ai configuré une machine à états Step Functions pour :

1. ajouter un nombre configurable d'éléments à la table `scheduled_items`, avec un TTL expirant entre 1 et 10 minutes
2. suivre l'heure à laquelle la tâche est planifiée et lorsqu'elle est effectivement prise en charge par la fonction `execute-on-schedule`
3. attendre que tous les éléments soient supprimés

La machine à états ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/DZ7zKEkjn26InqsMwDg8qkDXTlcE75FasIcr)

J'ai effectué plusieurs séries de tests. Les résultats sont cohérents, quel que soit le nombre d'éléments dans la table. Un rapide coup d'œil à la table vous indique que, en moyenne, une tâche est exécutée **11 minutes** APRES son heure planifiée.

![Image](https://cdn-media-1.freecodecamp.org/images/maU40YnAni5P0wmpbSHHucooNaZLzI17Txxx)
_US-EAST-1_

J'ai répété les expériences dans plusieurs autres régions AWS :

![Image](https://cdn-media-1.freecodecamp.org/images/DLYm48ZBEoFPqNuTmfF6CgSs8uWbf5DnFU76)

Je ne sais pas pourquoi il y a une telle différence marquée entre US-EAST-1 et les autres régions. Une explication est que le processus TTL nécessite un peu de temps pour se mettre en route après la création d'une table. Comme je dévelopais initialement contre la région US-EAST-1, son processus TTL a été "préparé" par rapport aux autres régions.

### Conclusions

Sur la base du résultat de mon expérience, il semble que l'utilisation de DynamoDB TTL comme mécanisme de planification ne peut pas garantir une précision raisonnable.

D'une part, l'approche est très évolutive. Mais d'autre part, les tâches planifiées sont exécutées avec au moins plusieurs minutes de retard, ce qui la rend inadaptée à de nombreux cas d'utilisation.