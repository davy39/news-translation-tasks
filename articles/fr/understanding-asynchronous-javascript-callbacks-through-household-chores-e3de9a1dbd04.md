---
title: Comprendre les callbacks asynchrones en JavaScript à travers les tâches ménagères
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-16T08:55:08.000Z'
originalURL: https://freecodecamp.org/news/understanding-asynchronous-javascript-callbacks-through-household-chores-e3de9a1dbd04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VUwszg-nhLvQ4uN5iqBLag.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comprendre les callbacks asynchrones en JavaScript à travers les tâches
  ménagères
seo_desc: 'By Stephen Mayeux

  If you’ve ever done the laundry, you can understand how callbacks work.

  The other day I read Kevin Kononenko’s brilliantly funny and easy-to-understand
  guide to MVC frameworks. He explains the Model-View-Controller paradigm through
  ...'
---

Par Stephen Mayeux

#### Si vous avez déjà fait la lessive, vous pouvez comprendre comment fonctionnent les callbacks.

L'autre jour, j'ai lu le guide brillamment drôle et facile à comprendre de [Kevin Kononenko](https://www.freecodecamp.org/news/understanding-asynchronous-javascript-callbacks-through-household-chores-e3de9a1dbd04/undefined) sur les frameworks MVC. Il explique le [paradigme Modèle-Vue-Contrôleur à travers la commande de boissons dans un bar](https://medium.freecodecamp.com/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053#.9bjays8jc), et c'est l'une de mes explications de programmation préférées, je pense, de tous les temps !

J'ai vraiment apprécié cela parce que c'était écrit sans prétention ni élitisme, et cela m'a fait me demander pourquoi beaucoup d'autres codeurs expérimentés ne peuvent pas aider les débutants sans l'attitude _l337er-than-thou_ ?

J'enseigne actuellement l'anglais en Corée du Sud, et nous, les enseignants, devons penser comme Kevin tout le temps. De nos jours, il est vraiment mal vu d'expliquer explicitement les concepts grammaticaux, donc les bons enseignants essaient de contextualiser la langue cible (c'est-à-dire la grammaire ou le vocabulaire qu'ils veulent enseigner) avec des histoires, des films, de la musique et des images.

Cette méthodologie d'enseignement a été influencée par des linguistes britanniques dans les années 1980, ce qui a informé la pédagogie moderne des langues étrangères aujourd'hui. Peut-être que la même chose se passe en ce moment pour l'éducation à la programmation !

Kevin sera difficile à égaler, mais j'aimerais expliquer comment fonctionnent les callbacks asynchrones en JavaScript à travers le contexte de l'accomplissement de tâches ménagères courantes.

#### Liste de tâches synchrones

Un grand merci à ma femme qui a fait le double de sa part de tâches à la maison pendant que j'apprends à coder. Je lui dois beaucoup !

Je donne généralement un coup de main à la maison le dimanche, et sa liste de tâches pour moi ressemble à ceci :

1. Faire la lessive
2. Donner un bain au chien
3. Trier le recyclage
4. Équilibrer le budget
5. Décider ce que nous allons faire pour le dîner.

**À part technique :** Au cœur, JavaScript est un langage de programmation synchrone, ce qui signifie qu'il exécute une ligne de code à la fois. Il ne peut pas passer à la ligne de code suivante tant que la ligne actuelle n'a pas fini de s'exécuter. Considérez cet exemple :

```
function syncChores() {  console.log('Do the laundry');  console.log('wash the dog');  console.log('sort the recycling');}
```

```
syncChores();
```

```
/* La sortie apparaît dans le même ordre qu'elle a été écrite :
```

```
   Do the laundry   wash the dog   sort the recycling
```

```
*/
```

Maintenant, imaginez si je faisais mes tâches ménagères de manière synchrone dans la vraie vie. Que se passerait-il ? À quoi cela ressemblerait-il ?

Si vous revenez à ma liste, vous verrez que faire la lessive est le premier élément. Il faut environ 35 minutes pour qu'un cycle de lavage typique se termine et 45 minutes supplémentaires pour qu'une charge de linge sèche. Donc pendant 80 minutes, je suis simplement assis sur mes fesses paresseuses, sans faire d'autres tâches, tandis que j'attends de manière synchrone que la lessive se termine.

Voici à quoi cela ressemble avec du pseudocode :

```
function doLaundry() {  startWashCycle();  switchToDryer();  foldAndIronClothes();}
```

```
function washDog() {  // imaginez ici du code pour laver le chien}
```

```
function sortRecycling() {  // et imaginez ici du code pour trier le recyclage}
```

```
doLaundry();// Maintenant, attendez 80 minutes avant de compléter les autres fonctions
```

```
// Maintenant, je peux enfin laver mon chien !washDog();sortRecycling();
```

Pas très efficace, n'est-ce pas ? Dans la vraie vie, les adultes occupés s'attaqueraient à ces tâches de manière asynchrone, ce qui signifie qu'ils commenceraient la lessive, continueraient à faire d'autres tâches sur la liste, et reviendraient à la lessive lorsque le cycle de lavage serait terminé.

Cette action de revenir à la lessive lorsqu'elle est prête est analogue à la **fonction de callback** en JavaScript, et nos machines à laver nous rappellent littéralement avec une alarme ou un buzzer ! Cela nous permet de continuer à faire d'autres tâches et de poursuivre la tâche de lessive lorsqu'elle est prête pour nous.

#### Liste de tâches asynchrones

Refaisons les tâches ménagères, cette fois de manière asynchrone. À quoi cela ressemblerait-il en pseudocode ?

```
function doLaundry(callback) {  // imaginez le code initial qui lance le cycle de lavage  // prend 80 minutes pour compléter le cycle de lavage
```

```
  callback(err, cleanLaundry);}
```

```
doLaundry(function(err, cleanLaundry) {  // parfois nos machines à laver tombent en panne  // mieux vaut gérer cette erreur possible
```

```
  if (err) throw err;
```

```
  // si aucune erreur, passer au sèche-linge après la fin du lavage
```

```
  // Tada ! Notre callback nous alertant que le lavage est terminé !
```

```
  switchToDryer(cleanLaundry);
```

```
});
```

```
// pendant que nous attendons, JavaScript exécutera ceci maintenant !
```

```
washDog();
```

```
// toujours du temps pour plus de tâches !
```

```
sortRecycling();
```

```
// ce qui suit sera indéfini car ce n'est pas encore prêt
```

```
console.log(cleanLaundry);
```

```
// Maintenant, la lessive est prête ! // Retour et passage des vêtements au sèche-linge
```

```
// Les vêtements sont en train de sécher. Continuons à faire plus de tâches.// Tanya sera impressionnée par ma productivité !
```

```
balanceBudget();
```

Comme l'article de Kevin, ceci n'était destiné qu'à clarifier le concept de callbacks. Si vous voulez un guide plus pratique, consultez [Callback Hell](http://callbackhell.com).

#### À votre tour

Cela aide si vous pouvez appliquer des concepts abstraits à des situations réelles. Pouvez-vous penser à ce que vous faites à la maison, à l'école ou au travail qui ressemble à du code synchrone et asynchrone ? Écrivez-les dans les commentaires ci-dessous !