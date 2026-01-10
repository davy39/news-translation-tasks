---
title: 'Algorithmes : Le Bon, La Brute et Le Truand'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-23T03:45:46.000Z'
originalURL: https://freecodecamp.org/news/algorithms-the-good-the-bad-and-the-ugly-e63db0a9cfb3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IPP7m_tu5VwSLAr2XIwaiA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Algorithmes : Le Bon, La Brute et Le Truand'
seo_desc: 'By Evaristo Caraballo

  Who has been in Free Code Camp without having the experience of spending hours trying
  to solve Algorithms?

  At Free Code Camp, we wanted to know why that was the case, and what more we could
  do to help you a bit.

  We made two diff...'
---

Par Evaristo Caraballo

Qui a été à Free Code Camp sans avoir vécu l'expérience de passer des heures à essayer de résoudre des **Algorithmes** ?

Chez Free Code Camp, nous voulions savoir pourquoi c'était le cas, et ce que nous pouvions faire de plus pour vous aider un peu.

Nous avons fait deux analyses différentes pour avoir une meilleure idée de ce qui se passait. Les données ont été collectées entre novembre 2014 et décembre 2015.

L'une de ces analyses consistait à suivre le nombre de fois où les gens collaient leur code pour qu'il soit vérifié par d'autres dans les salons de discussion Gitter pertinents. Nous avons obtenu des données à partir de l'API Gitter. Après un peu de nettoyage, nous avons essayé d'obtenir les noms des fonctions de chaque défi à partir des messages postés dans le salon d'aide. Bien que les données ne soient pas précises, c'est une bonne approximation de ce qui pourrait se passer.

Le graphique ci-dessus parle clairement de lui-même : les algorithmes comme les palindromes, la casse des titres, seek and destroy, le mot le plus long, la chaîne inversée, la mutation ou chunky monkey sont ceux pour lesquels beaucoup de gens demandent de l'aide.

Une autre analyse que nous avons faite consistait à prendre le temps moyen par page que chaque camper a passé sur chaque défi, en utilisant les données de Google Analytics.

Encore une fois, les plus difficiles sont des défis comme les palindromes, mais il y en a d'autres qui semblent également difficiles (disons 1/4 du temps moyen par niveau sur le même temps moyen), **surtout pour les niveaux de base et intermédiaires**, comme Spinal Tap Case, Pig Latin, Search and Replace, Common Multiple, Sum All Primes, Steamroller, Friendly Date Range, Pairwise, et autres.

En regardant les résultats, *pouvons-nous suggérer les facteurs qui affectent la performance des campers avec les algorithmes* ?

Les raisons les plus apparentes, données dans un ordre provisoire, sont :

* Les campers trouvent difficile de traiter particulièrement avec les _chaînes de caractères_, et **_Regex_** est un mauvais mot, peu importe le niveau !
* Il y a certains défis numériques qui rendent la vie des campers difficile, en particulier _ceux qui sont adaptés aux appels récursifs_.
* Un autre problème courant est de traiter avec des _collections imbriquées de tableaux/objets_.
* _La difficulté avec les concepts et les définitions_ est courante. Par exemple, le concept de « différence symétrique » (avec un algorithme Free Code Camp du même nom) est généralement troublant parce que beaucoup de campers ne comprennent pas correctement le concept, malgré l'inclusion d'une définition mathématique largement acceptée.

De même, en regardant le dernier graphique, vous vous demandez peut-être *pourquoi le temps par page ne semble pas refléter la difficulté du problème* ? Une explication pourrait être que les algorithmes de base et intermédiaires sont pris par des campers qui apprennent tout juste à coder ou qui voient JavaScript pour la première fois. Cependant, ceci est une explication provisoire et pourrait nécessiter plus d'analyses.

Si vous lisez ceci et que vous avez déjà souffert avec certains des algorithmes, vous réaliserez que vous n'êtes pas seul. Pour ceux qui commencent avec les algorithmes, je recommanderais ce qui suit :

* Essayez de voir si vous pouvez résoudre les plus faciles en premier : vous pourriez trouver une certaine pratique en résolvant ceux-ci qui pourrait vous aider à traiter les plus difficiles plus tard...
* Essayez de comprendre le problème ! Commencez par demander de quoi il s'agit.
* Faites des recherches. Consultez des livres, des références et d'autres cours en ligne. Et partagez. Nous offrons beaucoup d'aide avec un problème probablement similaire au vôtre. Demandez dans le salon de discussion. Envoyez un message à CamperBot. Consultez le Wiki. Essayez la programmation en binôme. Visitez un Campsite et codez avec d'autres campers en personne. Dans l'un des CodePens que j'ai faits pour cet article, j'ai également inclus des liens vers le wiki de Free Code Camp, afin que vous puissiez avoir un premier aperçu du problème et de la manière dont il est normalement résolu.
* Vous savez peut-être déjà que le problème est difficile : maintenant, la prochaine étape est d'essayer de comprendre _pourquoi_ et _quoi_ le rend si difficile. Cette approche est clé pour la résolution de problèmes algorithmiques, et la programmation en général. Étudiez, demandez et essayez à nouveau.
* Les données que nous avons utilisées pour ces analyses étaient de l'année dernière : cette année, [SaintPeter](http://gitter.im/saintpeter) et ses amis ont travaillé dur pour modifier le programme, vous pourriez donc remarquer une différence dans vos performances si vous travaillez à travers la section JavaScript de base améliorée. Si vous n'avez pas fait le programme mis à jour, il pourrait être utile de revisiter cette section.
* Mon conseil bonus ? Oui, essayez vraiment fort vous-même, mais... lisez aussi le code des autres. Lorsque vous lisez un livre sur JavaScript pour apprendre la programmation, c'est exactement ce que vous faites. Apprenez à inverser le génie du code existant et à le modifier pour répondre à vos besoins. Pourquoi ? Premièrement, il n'y a aucun intérêt à réinventer la roue. Deuxièmement, vous apprenez beaucoup en comprenant le travail de ceux qui ont déjà résolu le problème. Souvenez-vous : vous trouverez que la plupart du temps, vous réutiliserez des extraits modifiés d'un code précédent dans un nouveau. Donc, pas de honte à lire le code des autres. C'est d'ailleurs partie intégrante de la nature de l'Open Source...

Bon codage !

Je travaille également sur des visualisations connexes à [bl.ocks.org/evaristoc](http://bl.ocks.org/evaristoc).

Cette analyse ne fait qu'effleurer la surface de ce que nous pouvons apprendre des [données ouvertes de Free Code Camp](https://medium.freecodecamp.com/free-code-camp-christmas-special-giving-the-gift-of-data-6ecbf0313d62#.79rr68eop). Rejoignez notre [salon de discussion Data Science](http://gitter.im/freecodecamp/datascience) et aidez-nous à donner un sens à toutes ces données.