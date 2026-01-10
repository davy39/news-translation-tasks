---
title: Comment garder votre code JavaScript simple et augmenter sa lisibilité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T12:34:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-javascript-code-simple-and-increase-its-readability-94d6a949afc4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XsmvUvDELQVWAl3zhTvvlQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment garder votre code JavaScript simple et augmenter sa lisibilité
seo_desc: 'By Leonardo Lima

  After a few years working almost exclusively with Ruby on Rails and some jQuery,
  I changed my focus to front-end development. I discovered the beauties of JavaScript
  ES6 syntax and the exciting modern libraries such as React and Vue....'
---

Par Leonardo Lima

Après quelques années à travailler presque exclusivement avec Ruby on Rails et un peu de jQuery, j'ai changé mon focus pour le développement front-end. J'ai découvert les beautés de la syntaxe JavaScript ES6 et les bibliothèques modernes excitantes telles que React et Vue. J'ai commencé à implémenter de nouvelles fonctionnalités en utilisant uniquement du JavaScript Vanilla ES6, et je suis instantanément tombé amoureux de toute cette nouvelle abstraction de classe et de ces fonctions fléchées.

De nos jours, je génère de grandes quantités de code JavaScript. Mais, puisque je me considère comme un Padawan JavaScript, il y a encore beaucoup de place pour l'amélioration. À travers mes études et observations, j'ai appris que même avec l'utilisation des sucres syntaxiques présentés dans ES6, si vous ne suivez pas les principes principaux de [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf), votre code a une forte chance de devenir complexe à lire et à maintenir.

Pour démontrer ce dont je parle, je vais vous guider à travers une fantastique session de Code Review que j'ai eue la semaine dernière avec un [ami](https://github.com/anderson06). Nous allons commencer avec une classe JavaScript de 35 lignes et finir avec un beau morceau de code de 11 lignes utilisant uniquement des fonctions élégantes. Avec de la patience et de la résilience, vous serez en mesure d'observer et d'appliquer le modèle à votre propre base de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2Dp7SafVzM24sQg_6YrmfA.gif)
_Processus de refactorisation présenté dans cet article_

### La fonctionnalité

Ce que je devais faire était assez simple et trivial : obtenir certaines informations de la page et envoyer une requête à un service de suivi tiers. Nous construisions un suiveur d'événements côté client et suivions certaines actions de page avec lui.

Les exemples de code ci-dessous implémentent la même tâche en utilisant différentes tactiques de conception de code.

#### Jour 1 — Utilisation de la syntaxe de classe ES6 (aka Object Prototype Pattern wrapper)

Vous pouvez remarquer ci-dessus que j'ai commencé intelligemment : en isolant le suiveur générique `SuccessPlanTracker` pour être réutilisé dans une autre page en plus de l'Index Vide.

Mais, attendez une minute. Si ceci est un suiveur d'index vide, que fait donc cet étranger `TrackNewPlanAdd` ici ?

#### Jour 2 — Se débarrasser du code boilerplate de la classe

D'accord, maintenant le nom du fichier reflète clairement la responsabilité de la fonctionnalité et, regardez cela, il n'y a plus de classe `EmptyIndexTracker` qui nous donne moins de code boilerplate. En savoir plus [ici](https://gist.github.com/indiesquidge/f8c486795d7dd455c0327ce7e0aa8c16) et [ici](https://www.accelebrate.com/blog/javascript-es6-classes-and-prototype-inheritance-part-1-of-2/). Nous utilisons des variables de fonctions simples et, mec, quelle bonne prise en utilisant ces points de [ES6 Object Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator) brillants.

Je découvre que la méthode [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll) retourne déjà une Liste, donc nous sommes en mesure de supprimer la fonction `Array.from()` de `Array.from(document.getElementsByClassName('js-empty-index-tracking'))`. Souvenez-vous que la méthode [getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByClassName) retourne un objet.

De plus, puisque la responsabilité centrale est de lier les éléments HTML, l'invocation de la fonction `document.addEventListener('DOMContentLoaded')` n'appartient plus au fichier.

Bon travail !

#### Jour 3 — Suppression des anciennes pratiques ES5 et isolation des responsabilités encore plus.

Si vous prêtez une attention particulière, il n'y a pas de classe `SuccessPlanTracker` dans le code ci-dessus — elle a subi le même sort que l'ancienne `EmptyIndexTracker`. L'état d'esprit de tuer les classes, une fois installé, se propage et se multiplie. Mais ne craignez rien, mon bon gars.

Souvenez-vous, essayez toujours de garder vos fichiers JavaScript simples. Il n'est pas nécessaire de connaître les états des instances de classe, et les classes exposaient pratiquement une seule méthode.

Ne pensez-vous pas que l'utilisation de l'abstraction de classe ES6 était un peu exagérée ?

Avez-vous également remarqué que j'ai supprimé les instances de variables du haut du fichier ? Cette pratique remonte à ES5, et nous n'avons pas besoin de nous en soucier autant maintenant que nous avons la syntaxe ES6+.

Enfin, le dernier grand changement dans cette troisième version. Notre lieur de suiveur d'index vide ne fait maintenant qu'une seule chose : la liaison des éléments.

En suivant ces étapes, le code s'est rapproché du Principe de Responsabilité Unique — l'un des principes SOLID les plus importants.

#### Jour 4 — Éviter la manipulation négligente du DOM

Hé, il y a plus de lignes maintenant, menteur !

Le problème est que notre troisième version était un peu cassée. Nous mutions de manière inappropriée les datasets des éléments DOM dans la ligne `properties.emptyIndexAction = button.dataset.trackingIdentifier`.

La propriété d'un bouton était passée à un autre bouton, générant des événements de suivi mélangés. Pour résoudre cette situation, nous avons supprimé la responsabilité d'assigner la propriété `emptyIndexAction` de la boucle de liaison à une fonction appropriée en créant sa propre méthode scopée `trackAction()`.

En ajoutant ces lignes supplémentaires, nous avons amélioré notre code, mieux encapsulant chaque action.

#### Enfin, pour conclure et écrire

* Si vous voulez concevoir et écrire des morceaux de code merveilleux, vous devez être prêt à explorer davantage et à aller au-delà des limites d'une syntaxe propre et moderne.
* Même si la première version de votre code s'est avérée simple et lisible, cela ne signifie pas nécessairement que le système a une bonne conception ou qu'il suit au moins l'un des principes [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf).
* Il est essentiel d'accepter les revues de code constructives et de laisser d'autres développeurs pointer ce que vous pouvez faire mieux.
* Pour garder votre code simple, vous devez penser plus grand.

Merci beaucoup d'avoir lu l'article. Avez-vous un autre exemple de refactorisation ou une leçon de revue de code à partager ? Laissez un commentaire ci-dessous ! De plus, vous pouvez m'aider à partager ce message avec d'autres en applaudissant et en le partageant.

**ProTip à emporter** : Voici une feuille de triche très utile ES6 (ES2015+) [cheatsheet](https://devhints.io/es6)

_*Santé à [@anderson06](https://github.com/anderson06) pour être un si bon pote de code me donnant des feedbacks géniaux._