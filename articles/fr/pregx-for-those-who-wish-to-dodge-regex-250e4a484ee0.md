---
title: Vous détestez les regex ? Eh bien, j'ai une solution pour vous…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T00:54:09.000Z'
originalURL: https://freecodecamp.org/news/pregx-for-those-who-wish-to-dodge-regex-250e4a484ee0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FJQFtX72NUMaHFebSRIgHw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Vous détestez les regex ? Eh bien, j'ai une solution pour vous…
seo_desc: 'By Bukhari Muhammad

  The following piece presents my latest package on NPM, which is also available on
  GitHub as a repository. I wrote it in hope that it be beneficial to all who may
  need it.

  So… What is PregX?


  PregX — Largest library of popular & co...'
---

Par Bukhari Muhammad

Le texte suivant présente mon dernier [package](http://npmjs.com/package/pregx) sur NPM, également disponible sur GitHub en tant que [dépôt](https://github.com/bukharim96/pregx). Je l'ai écrit dans l'espoir qu'il soit bénéfique à tous ceux qui pourraient en avoir besoin.

### Alors… Qu'est-ce que PregX ?

![Image](https://cdn-media-1.freecodecamp.org/images/ICoOkdsuimq4rxqdfwgcv6spCf01dvDeG2rP)
_PregX — Plus grande bibliothèque de motifs Regex populaires et couramment utilisés pour JavaScript_

**PregX**, contrairement à la croyance populaire, fait référence à : _Popular Regex (Patterns)_, et non aux expressions régulières Perl. En parlant de « commun », il s'agit d'une bibliothèque — écrite en JavaScript — qui vise à être la plus grande collection de **expressions régulières** populaires et courantes.

Les développeurs peu familiers avec les expressions régulières peuvent rencontrer des difficultés lorsqu'ils tentent d'utiliser des notations et une syntaxe complexes d'**expressions régulières**. Cette bibliothèque devrait aider ces développeurs à accomplir des tâches courantes nécessitant des expressions régulières. Elle tire parti des motifs pré-écrits que nous utilisons le plus fréquemment dans nos projets.

### Pourquoi ne pas écrire vos propres expressions régulières ?

![Image](https://cdn-media-1.freecodecamp.org/images/XgBx9MtbjoGJVVDMpfC-6DjBD6jHEuBXcR9J)
_[Source de l'image.](https://www.flickr.com/photos/sirexkat/1128067974/in/album-72157601455231098/" rel="noopener" target="_blank" title=")_

L'approche [Don't Repeat Yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) stipule que la répétition dans le code doit être réduite via l'automatisation ou l'abstraction. Il s'agit d'un principe fondamental de la programmation qui doit être respecté chaque fois que possible. Puisque la duplication gaspille à la fois du temps et de l'espace, je me suis donné beaucoup de mal pour trouver une solution non seulement pour moi, mais aussi pour les autres.

Quel est l'intérêt du principe _DRY_ si nous continuons à réinventer le pain chaque fois qu'un Tom, Dick ou Harry découvre le blé ?

J'ai trouvé des motifs **regex** courants. Mon idée était d'abstraire chacun de ces motifs populaires en une fonction pure utile. Cette abstraction ne mutera ni n'altérera l'état de la chaîne donnée pour correspondre. Chaque fonction retournera ensuite un tableau des éléments correspondants dans la chaîne donnée.

**PregX** n'a pas été conçu pour s'opposer à l'originalité. Il a deux objectifs simultanés. Un objectif est de réduire le temps que les développeurs passent à essayer d'utiliser **regex**. L'autre objectif est d'éviter la complexité là où elle n'a pas sa place.

Bien que, coupable comme chargé, ce package est également (indirectement) destiné à ceux qui évitent toujours d'écrire des expressions régulières.

Ensuite, vous devrez peut-être écrire vos propres **regex**. Votre approche dépend entièrement des besoins de la tâche à accomplir.

### Quand devrais-je utiliser PregX ?

Bonne question, quand devriez-vous ?

**PregX** peut être utilisé lorsque la fonctionnalité intégrée ne parvient pas à atteindre, ou est inadéquate pour, votre résultat complexe souhaité. Certains pourraient soutenir que **regex** pourrait accomplir cette tâche.

**Regex** pourrait raccourcir le code efficacement. Cependant, cela peut aussi réduire la lisibilité de votre code, selon la complexité de la tâche à accomplir.

Pourquoi ne pas opter pour une solution prête à l'emploi qui est abstraite en une fonction utile ?

C'est là que **PregX** entre en jeu. Les motifs sont abstraits en fonctions conformément au [_Paradigme de Programmation Fonctionnelle_](https://en.wikipedia.org/wiki/Functional_programming). Cela en fait la solution de référence pour les tâches regex courantes. L'utilisation de **PregX** permet d'atteindre le même résultat, sans se contenter d'un code moins lisible ou de réinventer le pain.

Un principe largement exact est : Quel que soit le motif que vous préparez, il y a probablement une personne qui l'a déjà écrit. **PregX** suit cette règle empirique, en accumulant de tels motifs pour la majorité des développeurs **non-regex**.

Ensuite, tout cela dépend de ce avec quoi vous êtes à l'aise. Si vous n'êtes pas doué pour écrire vos propres motifs, alors c'est une solution facile.

### Quand ne pas utiliser PregX

Si vous cherchez un motif hors du commun, super spécifique à vos besoins, alors **PregX** n'est tout simplement pas la réponse. **PregX** n'est pas destiné à remplacer **regex**, ce serait super idiot. **Regex** restera toujours la meilleure solution lorsqu'il s'agit de tâches précises ou explicites de cette nature. En résumé, un bon développeur saura quand utiliser un moule à pain et quand utiliser une boulangerie.

### La simplicité et l'utilité de PregX

J'ai pensé que je montrerais quelques exemples de code pratiques pour démontrer l'extraordinaire de cette bibliothèque. C'est-à-dire, si vous n'êtes pas encore convaincu par tout le discours ennuyeux que j'ai écrit jusqu'à présent. ?

#### Exemple de carte de crédit

L'exemple suivant montre comment faire correspondre un numéro de carte de crédit en utilisant une chaîne, avec `getCreditCardNumber()`. On pourrait même spécifier le type de carte de crédit à faire correspondre, via la propriété `cardType` de l'objet `config` de la fonction. Par défaut, cette fonction fait correspondre les numéros de carte Visa. Vérifiez cet exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/OcbvsOcAojZxXioMkhtXRuVFmmjK9l3WqU9K)
_`getCreditCardNumber()`_

Pas impressionné ? J'ai assez de tours dans mon sac pour vous tenter.

#### Exemple de code postal

Si l'exemple de code ci-dessus ne vous a pas convaincu, alors celui-ci le fera.

Le motif de la fonction `getPostalCode()` est l'un des nombreux motifs que j'ai écrits moi-même. Il existe de nombreuses solutions qui tentent de faire cela. Aucune ne correspond au standard de **PregX**.

J'ai utilisé [la Liste des Codes Postaux de Wikipedia](https://en.wikipedia.org/wiki/List_of_postal_codes) comme référence, et j'ai conçu la plus grande fonction unique de **PregX**. Avec **le support de la correspondance des adresses postales de plus de 150 pays**, cette fonction — au moins pour moi — reste la meilleure solution pour accomplir cette tâche courante. Jetez un coup d'œil :

![Image](https://cdn-media-1.freecodecamp.org/images/s9cA9wloQL53PU3W2BTw2KiFz-2zWgSWeKs8)
_`getPostalCode()`_

### Motifs actuellement supportés

**PregX** supporte une liste sélectionnée de 35 (et plus) motifs différents, tous bien testés pour correspondre à leur texte approprié. Voici une liste des motifs supportés :

![Image](https://cdn-media-1.freecodecamp.org/images/EUb230uJGrGSbnKlsrTVvxkeaOXUUUNNXyLv)
_Motifs Supportés_

### Convaincu ?

Ce ne sont que deux exemples parmi les nombreux motifs que contient cette bibliothèque. Pour la documentation, des exemples d'utilisation et plus d'informations sur **PregX**, consultez son [dépôt](http://github.com/bukharim96/pregx) sur GitHub. Mieux encore, clonez-le ou testez-le en l'installant simplement via NPM :

```
npm install pregx --save
```

J'adorerais avoir votre avis sur ce package. **PregX** contient actuellement 35 motifs, j'espère qu'il atteindra ~100. Alors, n'hésitez pas à contribuer avec des motifs utiles. [Étoilez-le sur git](https://github.com/bukharim96/pregx/).

Il s'agit de mon premier projet open source sur [NPM](http://npmjs.com/package/pregx), mais pas mon premier sur GitHub. Aimez-le, [forkez-le](https://github.com/bukharim96/pregx/). Détestez-le, critiquez-le. Pour obtenir des mises à jour sur les progrès de ce dépôt ainsi que des conseils cool liés à JavaScript / React, suivez-moi sur twitter : [@bukharim96](https://twitter.com/bukharim96)

Merci d'avoir lu cet article.

Paix.