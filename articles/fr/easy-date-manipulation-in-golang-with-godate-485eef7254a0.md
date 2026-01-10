---
title: Manipulation facile des dates en Golang avec Godate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T16:31:17.000Z'
originalURL: https://freecodecamp.org/news/easy-date-manipulation-in-golang-with-godate-485eef7254a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6iBVfeqbc8V9MEuhlYOTdQ.jpeg
tags:
- name: coding
  slug: coding
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Manipulation facile des dates en Golang avec Godate
seo_desc: 'By Kofo Okesola

  I have always been and always will be a fan of Carbon and how easy it is to get
  date manipulation done so efficiently. Being a fan of Carbon and also being a fan
  of Golang I thought why not write a library called godate. It will do fo...'
---

Par Kofo Okesola

J'ai toujours été et je serai toujours un fan de [Carbon](https://carbon.nesbot.com/) et de la facilité avec laquelle on peut manipuler les dates de manière si efficace. Étant un fan de Carbon et aussi un fan de Golang, je me suis dit pourquoi ne pas écrire une [bibliothèque appelée godate](https://github.com/kofoworola/godate). Elle fera pour Golang ce que Carbon fait pour PHP, et dans cet article, je vais expliquer comment l'utiliser.

### Décomposition du package

Le package est principalement une structure `GoDate` avec ses méthodes d'assistance disponibles, qui agit comme un wrapper pour une structure `Time`. Il inclut également quelques fonctions pour l'initialisation, par exemple `Now`, `Tomorrow`.

### Utilisation

#### Installation

```
go get github.com/kofoworola/godate
```

Il supporte également [le nouveau système de modules de Go](https://github.com/golang/go/wiki/Modules). Vous pouvez simplement l'importer dans votre projet et l'exécuter. Go tentera d'installer la dernière version du package, qui est la v1.2.0 au moment de la rédaction de cet article.

#### Utilisation

Créez une nouvelle structure GoDate avec l'une des méthodes actuellement disponibles.

Notez la différence de fuseau horaire, c'est pourquoi je recommande de créer une structure GoDate avec un objet `time.Location` passé.

Une fois que vous avez une structure, vous pouvez facilement enchaîner des méthodes sur la structure pour obtenir votre résultat comme suit :

### Méthodes disponibles

#### Comparaison

Les méthodes de comparaison disponibles sont `IsBefore`, `IsAfter` et `IsWeekend`. Les noms des méthodes expliquent ce qu'elles font :

#### Différence

Les méthodes de différence les plus importantes sont mises en évidence ci-dessous. Bien qu'il y ait plus de méthodes incluses qui sont également utilisées dans la logique de celles-ci :

Les méthodes `Difference` qui prennent un autre `goDate` comme paramètre calculent la différence comme `methodOwner — parameter`. Une différence négative signifie que le paramètre se produit après le `methodOwner`.

#### Formatage de chaîne

Voici les méthodes de formatage de chaîne actuellement disponibles. Vous pouvez également [formater](https://yourbasic.org/golang/format-parse-string-time-date-example/) (vous pourriez vouloir lire cela si vous êtes nouveau dans les dates en Golang) cela à votre manière en appelant la méthode `Format()`.

#### Assistant

Certaines des méthodes d'assistance supplémentaires et leurs sorties sont listées ci-dessous :

Notez que les méthodes `EndOfWeek` et `StartOfWeek` utilisent `time.Sunday` comme début de semaine par défaut. Ce comportement peut être changé pour la structure godate actuelle en appelant `now.SetFirstDay(time.Monday)`.

### Conclusion

Le package est loin d'être complet (et ne le sera probablement jamais). L'objectif est de fournir une API de gestion des dates robuste, similaire et même meilleure (quelqu'un est ambitieux ici...) que [Carbon](https://carbon.nesbot.com). Donc, vous, les amateurs de Go comme moi, devriez faire pleuvoir des PR sur le [dépôt](https://github.com/kofoworola/godate) (et des étoiles :)