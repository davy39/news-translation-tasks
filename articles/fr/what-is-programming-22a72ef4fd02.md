---
title: Nous programmons depuis des milliers d'années
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-19T12:30:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-programming-22a72ef4fd02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*baG6RijcVa8LysywkCpN8g.jpeg
tags:
- name: history
  slug: history
- name: language
  slug: language
- name: Philosophy
  slug: philosophy
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Nous programmons depuis des milliers d'années
seo_desc: 'By Tautvilas Mečinskas

  Computer programs are all around us. We interact with them every day. It looks as
  if software is becoming more and more important to our society. But why do we find
  programs so necessary to us? Why and when did we start program...'
---

Par Tautvilas Mečinskas

Les programmes informatiques sont partout autour de nous. Nous interagissons avec eux tous les jours. Il semble que le logiciel devienne de plus en plus important pour notre société. Mais pourquoi trouvons-nous les programmes si nécessaires ? Pourquoi et quand avons-nous commencé à programmer ? Qu'est-ce que l'essence de la programmation ? Ces questions peuvent sembler triviales, mais je pense qu'aujourd'hui nous n'avons toujours pas une bonne définition de ce qu'est la programmation. Peut-être que cet article peut aider à changer cela.

Il est assez difficile de définir la programmation parce qu'elle est si diverse. On peut programmer des jeux, des applications mobiles, des sites web, des compilateurs, des simulations et bien plus encore. Dans ce cas, il peut être utile de commencer par décomposer certaines idées fausses et de clarifier ce que la programmation n'est pas.

_La programmation n'est pas une science._ La science est l'art d'examiner le monde et de découvrir des motifs répétables. La méthode scientifique consiste à faire une hypothèse, puis à effectuer des expériences pour la prouver ou la rejeter. Nous n'utilisons pas une telle méthode en programmation — ainsi ce n'est pas une science. La programmation n'est pas une question de découverte, mais de créativité.

_La programmation n'est pas des mathématiques._ Oui, il y a un aspect mathématique à la programmation. Certaines parties des programmes peuvent être exprimées comme des fonctions mathématiques. Écrire un générateur de nombres de Fibonacci est amusant, mais complètement inutile sans une application réelle. Les mathématiques en programmation sont un moyen pour une fin, pas une partie centrale du processus.

_La programmation ne concerne pas les ordinateurs électroniques._ Les ordinateurs sont très utiles, mais pas nécessaires. Les programmes peuvent être compris et interprétés par des êtres humains également. Par conséquent, les ordinateurs sont juste des outils que nous utilisons en programmation.

Alors, qu'est-ce que la programmation ? Qu'est-ce qui est au cœur de chaque programme — grand ou petit ?

Les abstractions.

Qu'est-ce que l'abstraction ? C'est une image réduite du monde. En abstraisant, nous convertissons la réalité en symboles qui peuvent être transmis comme information. Le mot _abstraction_ provient de deux mots latins, qui sont _abs,_ signifiant **loin de** et _trahere,_ signifiant **tirer**. La traduction latine suggère que l'abstraction implique de séparer un élément du tout.

Le processus d'abstraction est-il unique à la programmation ? Pas vraiment. C'est quelque chose que les humains font depuis assez longtemps. Et nos outils les plus basiques d'abstraction sont la carte et l'horloge.

Les archéologues ont découvert des cartes en pierre que les humains ont faites [il y a plus de 14 000 ans](http://www.telegraph.co.uk/news/worldnews/europe/spain/5978900/Worlds-oldest-map-Spanish-cave-has-landscape-from-14000-years-ago.html). Cela montre que la cartographie est fondamentale pour les humains. C'est un processus de transformation du territoire en symboles en l'abstrayant. Une carte est un moyen d'abstraire l'espace. C'est un outil qui nous aide à comprendre le territoire environnant afin que la navigation soit plus facile.

Une horloge, en revanche, est un moyen d'abstraire le temps. Nous trouvons la nature continue du temps confuse, alors nous l'abstrayons. Les humains divisent le temps en intervalles discrets : années, mois, jours, heures, minutes, secondes. Alors qu'une carte nous aide à naviguer dans l'espace, une horloge nous aide à naviguer dans le temps. Le prédécesseur de l'horloge — le calendrier — est apparu [il y a plus de 10 000 ans](http://gizmodo.com/archaeologists-discover-worlds-oldest-calendar-in-scotl-922374641).

![Image](https://cdn-media-1.freecodecamp.org/images/K2-yzsletJjBjTnKwA7kvn4sz4Ynu1UOC3ou)
_Calendrier solaire géant [Chankillo](https://en.wikipedia.org/wiki/Chankillo" rel="noopener" target="_blank" title=") a été construit il y a 2 300 ans._

Qu'en est-il des ordinateurs alors ? Ce sont aussi des outils qui traitent des abstractions. Il y a 3 parties fondamentales à tout ordinateur :

1. Horloge interne — la manière de l'ordinateur d'abstraire le temps
2. Mémoire — la manière de l'ordinateur d'abstraire l'espace
3. Unité de traitement — la manière de l'ordinateur d'effectuer des opérations logiques

Ces installations donnent aux ordinateurs un moyen de comprendre les abstractions d'espace et leurs interactions dans le temps abstrait. Cela signifie que les programmes sont des abstractions de l'espace-temps, et que la programmation est l'art de créer des abstractions de l'espace-temps. Ces abstractions nous aident à naviguer dans la réalité, et c'est pourquoi elles sont si importantes pour nous.

Et il y a une méthode d'abstraction qui est très similaire à la programmation, mais qui est encore plus ancienne que les cartes, les horloges et les calendriers : le langage.

Si vous regardez de plus près notre langage naturel, vous verrez qu'il possède toutes les caractéristiques nécessaires pour abstraire l'espace-temps.

Examinons une phrase d'exemple :

> Allez dans le jardin et cueillez quelques fleurs ce soir.

**Le jardin** et **fleurs** font référence à l'espace abstrait. **Ce soir** est une manière d'abstraire le temps. **Et** ajoute de la logique à la phrase. **Allez à** et **cueillez** sont des sous-routines.

Nous pouvons facilement transformer la phrase ci-dessus en JavaScript :

```
whenEvening.then(()=>you.goTo(garden)).then(()=>you.pickUp(flower))
```

Cette phrase peut être comprise par un ordinateur qui a des définitions de **soir**, **vous**, **fleurs**, et les sous-routines nécessaires définies.

Le problème avec le langage naturel est qu'il a des applications très larges. Le langage peut être utilisé non seulement pour communiquer des informations, mais aussi pour exprimer des sentiments et des émotions. Les meilleurs exemples de programmes en langage naturel pur sont les lois, les règles des jeux de société et les manuels d'instructions.

![Image](https://cdn-media-1.freecodecamp.org/images/xQoLcFFm2PL69Hv3LpF1saAtoAn86lGejQ99)
_[ CC BY-NC-SA](https://en.wikipedia.org/wiki/Code_of_Hammurabi" rel="noopener" target="_blank" title="">Code de Hammurabi</a> est l'un des plus anciens programmes en langage naturel (photo par <a href="https://www.flickr.com/photos/prof_richard/" rel="noopener" target="_blank" title="">Richard</a> /<a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" rel="noopener" target="_blank" title="))_

Les langages de programmation, en revanche, sont stricts et ne peuvent créer que des abstractions. Les ordinateurs sont conçus pour interpréter ces abstractions de manière très spécifique et déterministe.

Pour écrire des programmes informatiques, il faut apprendre à encoder le langage naturel en symboles que l'ordinateur peut comprendre. Cela nécessite généralement une connaissance approfondie de l'architecture informatique et de la syntaxe du langage informatique choisi. Ainsi, si vous voulez qu'un ordinateur comprenne vos abstractions de réalité, vous devez apprendre à coder.

Les ordinateurs sont des outils qui peuvent exécuter des règles définies dans des programmes avec une vitesse et une précision surhumaines. Ils nous donnent la capacité de construire des abstractions complexes et multicouches, et de transformer nos programmes en cartes véritablement dynamiques et interactives de la réalité.

À bien des égards, la programmation est quelque chose que nous savons tous déjà faire. Le processus d'abstraction de la réalité est fondamental pour les êtres humains. La programmation informatique est simplement la manière la plus efficace de le faire.