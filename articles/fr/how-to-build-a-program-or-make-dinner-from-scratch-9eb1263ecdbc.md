---
title: Comment coder un algorithme de satellite et cuisiner une paella à partir de
  zéro
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2017-09-12T04:59:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-program-or-make-dinner-from-scratch-9eb1263ecdbc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uarF1UhF3lwjGaG6.
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment coder un algorithme de satellite et cuisiner une paella à partir
  de zéro
seo_desc: 'What if I told you that by the end of this article, you’d be able to calculate
  the orbital period of satellites around Earth using their average altitudes and…
  You tuned out already, didn’t you?

  Okay, how about this: I’m going to teach you how to mak...'
---

Et si je vous disais qu'à la fin de cet article, vous seriez capable de calculer la période orbitale des satellites autour de la Terre en utilisant leurs altitudes moyennes et… Vous avez déjà décroché, n'est-ce pas ?

D'accord, que diriez-vous de ceci : Je vais vous apprendre à faire de la paella !

![Image](https://cdn-media-1.freecodecamp.org/images/K5J7Hmgwkud1hIc25kbc5jAA0SSWGx1zizcp)
_Fait vrai : les gens sont beaucoup plus susceptibles d'accepter la complexité si elle vient avec la promesse de nourriture._

**Et** vous apprendrez à écrire une fonction qui fait ce dont j'ai parlé ci-dessus, tout comme je l'ai fait pour ce [défi freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/map-the-debris).

Je promets qu'il y a une leçon morale globale qui vous bénéficiera chaque jour pour le reste de votre vie. Ou, au moins, vous nourrira pour une nuit. Commençons.

### La seule chose que je sais sur la paella, c'est que c'est un émoticône

![Image](https://cdn-media-1.freecodecamp.org/images/FUy-LzL3XdgwjakWS68MYzE4b-CVBw9Lg4w9)
_Sauf si vous lisez ceci sur un téléphone Samsung, auquel cas vous regardez un hotpot coréen._

L'une de mes choses préférées dans le fait de vivre dans le monde aujourd'hui est qu'il est **totalement acceptable** de ne presque rien savoir sur quelque chose. Il y a cent ans, vous auriez pu passer toute votre vie sans savoir autre chose sur la paella que le fait que c'est un émoticône.* Mais aujourd'hui ? Vous pouvez simplement [la chercher](https://en.wikipedia.org/wiki/Paella).

_*_C'était une blague.

Comme pour toutes les choses dans la vie, lorsque nous ne sommes pas sûrs, nous nous tournons vers Internet. Dans ce cas, l'entrée pour _paella_ sur Wikipédia, qui dit :

> _« La paella… est un plat de riz valencien. La paella a des racines anciennes, mais sa forme moderne est originaire du milieu du XIXe siècle près de la lagune de l'Albufera sur la côte est de l'Espagne adjacente à la ville de Valence. De nombreux non-Espagnols considèrent la paella comme le plat national de l'Espagne, mais la plupart des Espagnols la considèrent comme un plat régional valencien. Les Valenciens, à leur tour, considèrent la paella comme l'un de leurs symboles identitaires._

> _Les types de paella incluent la paella valencienne, la paella végétarienne/végane (espagnol : paella de verduras), la paella aux fruits de mer (espagnol : paella de marisco), et la paella mixte (espagnol : paella mixta), parmi beaucoup d'autres. » — [Wikipédia](https://en.wikipedia.org/wiki/Paella)_

À ce stade, vous êtes probablement rempli de questions. Dois-je parler à un Valencien ? Dois-je suivre un cours en ligne sur l'histoire de l'Espagne ? Quel type de paella devrais-je essayer de faire ? Quel est l'avis commun des chefs modernes en matière de types de paella ?

Si vous vous lancez pour répondre à toutes ces questions, une chose est certaine : vous ne finirez jamais par faire de la paella. Vous passerez des heures et des heures à taper des questions dans les moteurs de recherche, et des années plus tard, vous vous réveillerez avec un master en cuisine valencienne.

### La méthode de la « Question la Plus Importante »

Quand je me parle à moi-même à voix haute en public (est-ce que tout le monde ne le fait pas ?), je fais référence à cela comme « QPI » (rime avec « Nick »). J'imagine aussi QPI comme une chips tortilla plutôt croustillante et assez adorable, anthropomorphisée. Ne me demandez pas pourquoi.

![Image](https://cdn-media-1.freecodecamp.org/images/o4PQKBeJDNs5WUxbTOq4ajFB3rXci7M3-bLk)

QPI fait tourner son corps triangulaire croustillant pour me pointer dans la bonne direction. La bonne direction prend toujours la forme de la question la plus importante que vous devez vous poser à n'importe quelle étape de la résolution de problèmes. La première question la plus importante est toujours celle-ci :

**Quel est l'objectif que je veux atteindre ?**

Eh bien, vous voulez faire de la paella.

La prochaine QPI devient alors : combien dois-je réellement savoir sur la paella pour commencer à la faire ?

Vous avez déjà entendu ce conseil : tout grand problème peut être décomposé en plusieurs problèmes plus petits et plus faciles à gérer. Dans cette petite constellation de problèmes de taille réduite, il n'y en a qu'**un** que vous devez résoudre pour arriver **presque** à une solution complète.

Dans le cas de la fabrication de la paella, nous avons besoin d'une recette. C'est un problème de taille réduite qu'un moteur de recherche peut résoudre pour nous :

> **Recette de Paella Simple**

> Dans un bol moyen, mélanger 2 cuillères à soupe d'huile d'olive, de paprika, d'origan, de sel et de poivre. Remuer les morceaux de poulet pour les enrober. Couvrir et réfrigérer.

> Chauffer 2 cuillères à soupe d'huile d'olive dans une grande poêle ou une poêle à paella à feu moyen. Ajouter l'ail, les flocons de piment rouge et le riz. Cuire en remuant pour enrober le riz d'huile, environ 3 minutes. Ajouter les filaments de safran, la feuille de laurier, le persil, le bouillon de poulet et le zeste de citron. Porter à ébullition, couvrir et réduire le feu à moyen-doux. Laisser mijoter 20 minutes.

> Pendant ce temps, chauffer 2 cuillères à soupe d'huile d'olive dans une poêle séparée à feu moyen. Ajouter le poulet mariné et l'oignon ; cuire 5 minutes. Ajouter le poivron et la saucisse ; cuire 5 minutes. Ajouter les crevettes ; cuire en tournant les crevettes jusqu'à ce que les deux côtés soient roses.

> Étaler le mélange de riz sur un plateau de service. Recouvrir du mélange de viande et de fruits de mer. ([allrecipes.com](http://allrecipes.com/recipe/84137/easy-paella/))

Et _voilà_ ! Croyez-le ou non, nous y sommes **presque** déjà.

Avoir un ensemble d'instructions étape par étape faciles à comprendre est vraiment la majeure partie du travail. Il ne reste plus qu'à rassembler les ingrédients et à faire la paella. À partir de ce moment, vos QPI peuvent devenir moins fréquentes et moins importantes par rapport au problème global. (Où puis-je acheter du paprika ? Comment savoir quand la saucisse est cuite ? Comment régler le minuteur de mon téléphone pour 20 minutes ? Comment arrêter de penser à cette délicieuse odeur ? Quel filtre Instagram capture le mieux l'extase de cette paella en ce moment ?)

![Image](https://cdn-media-1.freecodecamp.org/images/dCdbgwrAiqHllenfvHM2aEpPU4pyrR0tKfFf)
_La réponse à cette dernière question est « Nashville »._

### Je ne sais toujours rien sur le calcul des périodes orbitales des satellites

D'accord. Examinons le problème :

> Retourner un nouveau tableau qui transforme l'altitude moyenne des éléments en leurs périodes orbitales.

> Le tableau contiendra des objets au format {name: 'name', avgAlt: avgAlt}.

> Vous pouvez lire sur les périodes orbitales sur wikipedia.

> Les valeurs doivent être arrondies à l'entier le plus proche. Le corps en orbite est la Terre.

> Le rayon de la terre est de 6367,4447 kilomètres, et la valeur de la Masse Gravitationnelle (GM) de la terre est de 398600,4418 km3s-2.

> `orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}])` doit retourner `[{name: "sputnik", orbitalPeriod: 86400}]`.

Eh bien, il s'avère que pour calculer la période orbitale des satellites, nous avons aussi besoin d'une recette. Étonnant, les choses que l'on peut trouver sur internet de nos jours.

Courtoisie de [dummies.com](http://www.dummies.com/education/science/physics/how-to-calculate-the-period-and-orbiting-radius-of-a-geosynchronous-satellite/) (oui ! #noshame), voici notre recette :

![Image](https://cdn-media-1.freecodecamp.org/images/R9x3IprnkrRQd6GXHjIfE-prhYcIwmvpIkVJ)
_C'est un peu mignon, d'une certaine manière._

Cela peut sembler assez compliqué. Mais comme nous l'avons déjà vu, nous devons simplement répondre à la prochaine QPI : combien dois-je réellement savoir sur cette formule pour commencer à l'utiliser ?

Dans le cas de ce défi, pas trop. On nous donne déjà `earthRadius`, et `avgAlt` fait partie de notre objet d'arguments. Ensemble, ils forment le rayon, _r_. Avec quelques requêtes de recherche et un peu de voyage mental dans le temps jusqu'à votre cours de maths élémentaires, nous pouvons décrire cette formule en un mélange d'anglais :

**_T_, la période orbitale, est égale à 2 multiplié par Pi, multiplié à son tour par la racine carrée du rayon, _r_ cubé, divisé par la masse gravitationnelle, _GM_.**

JavaScript a une propriété `Math.PI`, ainsi qu'une fonction `Math.sqrt()` et une fonction `Math.pow()`. En utilisant celles-ci combinées avec un calcul simple, nous pouvons représenter cette équation en une seule ligne assignée à une variable :

```
var orbitalPeriod = 2 * Math.PI * (Math.sqrt(Math.pow((earthRadius + avgAlt), 3) / GM));
```

De l'intérieur vers l'extérieur :

1. Ajouter `earthRadius` et `avgAlt`
2. Élever au cube le résultat de l'étape 1
3. Diviser le résultat de l'étape 2 par GM
4. Prendre la racine carrée du résultat de l'étape 3
5. Multiplier 2 fois Pi fois le résultat de l'étape 4
6. Assigner la valeur retournée à `orbitalPeriod`

Croyez-le ou non, nous y sommes presque déjà.

La prochaine QPI pour ce défi est de prendre l'objet d'arguments, extraire les informations dont nous avons besoin, et retourner le résultat de notre équation dans le format requis. Il y a plusieurs façons de faire cela, mais je suis satisfait d'une boucle `for` simple :

```js
function orbitalPeriod(arr) {
   var resultArr = [];
   for (var teapot = 0; teapot < arguments[0].length; teapot++) {
     var GM = 398600.4418;
     var earthRadius = 6367.4447;
     var avgAlt = arguments[0][teapot]['avgAlt'];
     var name = arguments[0][teapot]['name'];
     var orbitalPeriod = 2 * Math.PI * (Math.sqrt(Math.pow((earthRadius + avgAlt), 3) / GM));
     var result = {
       name: name,
       orbitalPeriod: Math.round(orbitalPeriod)
     }
     resultArr.push(result);
   }
   return resultArr; 
}
```

Si vous avez besoin d'un rappel sur l'itération à travers les tableaux, jetez un œil à mon [article sur l'itération, mettant en vedette des tableaux de petit-déjeuner](https://victoria.dev/verbose/iterating-over-objects-and-arrays-frequent-errors/) ! (5 minutes de lecture)

Ne regardez pas maintenant, mais vous venez d'acquérir la capacité de calculer la période orbitale des satellites. Vous pourriez même le faire **tout en** faisant de la paella, si vous le souhaitiez. Sérieusement. Mettez-le sur votre CV.

### Tl;dr : la leçon morale globale

Que ce soit pour cuisiner, coder ou autre chose, les problèmes peuvent sembler au début confus, insurmontables ou tout simplement ennuyeux. Si vous êtes confronté à un tel défi, rappelez-vous simplement : ils sont beaucoup plus digestes avec une portion de chips QPI de taille réduite.

![Image](https://cdn-media-1.freecodecamp.org/images/F3rfvQ7g-sDnegvv677q7y7gKXkmRPKsPjoU)

Merci d'avoir lu !

Si vous avez aimé cet article, j'adorerais le savoir ! Vous pouvez trouver cet article et d'autres expliquant des concepts de codage avec de la nourriture [sur mon blog.](https://victoria.dev/verbose/)