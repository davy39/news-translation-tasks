---
title: Ce que nous voulons vraiment dire lorsque nous parlons de prototypes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-14T00:26:41.000Z'
originalURL: https://freecodecamp.org/news/what-we-really-mean-when-we-talk-about-prototypes-165586f29fa9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5dxjDGWBfN796dwrZcVHaw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ce que nous voulons vraiment dire lorsque nous parlons de prototypes
seo_desc: 'By Hayden Betts

  Beginning JavaScript devs often mistakenly use one word — “prototype” — to refer
  to two different concepts. But what exactly is the difference between an “object’s
  prototype” and the “prototype property” of JavaScript functions?


  But ...'
---

Par Hayden Betts

Les développeurs JavaScript débutants utilisent souvent à tort un seul mot — « prototype » — pour désigner deux concepts différents. Mais quelle est exactement la différence entre le « prototype d'un objet » et la « propriété prototype » des fonctions JavaScript ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*L04gw3FTaj-fQE6b-bY2Ug.png)
_Mais pourquoi… ?_

Je pensais comprendre le concept de « prototypes » et d'héritage prototypal en JavaScript. Mais je continuais à me sentir confus par les références à « prototype » dans le code et dans la documentation.

Une grande partie de ma confusion a disparu lorsque j'ai réalisé que **lorsqu'on écrit sur JavaScript, les gens utilisent souvent de manière informelle « prototype » pour** **décrire deux concepts distincts mais liés.**

1. **Le prototype d'un objet** : L'objet modèle à partir duquel un autre objet JavaScript hérite des méthodes et des propriétés. ([MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes))
2. **La propriété [non-énumérable](https://stackoverflow.com/questions/17893718/what-does-enumerable-mean) `prototype` des fonctions JavaScript** : _Une commodité pour faciliter un modèle de conception_ (ce modèle de conception sera expliqué en profondeur bientôt !)_._   
Pas significative en elle-même jusqu'à ce qu'elle soit délibérément définie pour avoir une fonction liée à l'héritage. La plus utile lorsqu'elle est utilisée avec des fonctions constructeurs et des fonctions d'usine (explication à venir !). Bien que toutes les fonctions JS aient cette propriété par défaut. Contient une propriété `constructor`, qui fait référence à la fonction originale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vmv0NSt-8jA_qOcbPuCzxA.png)
_Même les fonctions triviales ont une propriété prototype par défaut._

Pendant longtemps, j'étais à l'aise avec la définition 1, mais pas avec la définition 2.

### Pourquoi cette distinction est-elle importante ?

Avant de comprendre la différence entre « le prototype d'un objet » et la « propriété `prototype` non-énumérable des fonctions », je me suis retrouvé confus par des expressions comme celle-ci :

```
Array.prototype.slice.call([1, 2], 0, 1);// [ 1 ]
```

_(note : la première — mais pas la seule — étape pour comprendre ce qui précède est de comprendre `call()`. Voici un rapide [rappel](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) au cas où !)_

Une question à laquelle je n'étais pas en mesure de répondre auparavant :

* « Pourquoi cherchons-nous `slice` dans le prototype du constructeur `Array` ? Le constructeur `Array` lui-même ne devrait-il pas contenir la méthode `slice`, et son prototype ne contenir que quelques méthodes de très bas niveau que tous les objets partagent ? »

Ces questions ont été totalement éclaircies lorsque j'ai compris le modèle de conception que la propriété `prototype` des fonctions constructeurs `Array` existe pour permettre.

### 3 étapes pour comprendre la propriété prototype des fonctions JS

Pour comprendre la propriété `prototype` des fonctions JS, vous devez comprendre le modèle de conception qu'elle permet. Je vais construire une compréhension de ce modèle en travaillant d'abord à travers deux alternatives moins préférables.

#### Implémentation 1 : Le modèle de classe fonctionnelle

Imaginons que nous voulons créer un jeu dans lequel nous interagissons avec des chiens. Nous voulons créer rapidement de nombreux chiens qui ont accès à des méthodes communes comme **pet** et **giveTreat.**

Nous pourrions commencer à implémenter notre jeu en utilisant le [modèle de classe fonctionnelle](https://www.thegreatcodeadventure.com/javascripts-functional-class-pattern/) comme suit :

Nettoyons un peu cela en stockant ces méthodes dans leur propre objet. Ensuite, étendons-les à l'intérieur de la fonction d'usine `createDog`.

Bien que cette implémentation soit facile à comprendre et reflète commodément l'héritage basé sur les classes dans d'autres langages, elle présente au moins un problème majeur : nous copions nos définitions de méthodes dans chaque objet chien que nous créons en utilisant notre fonction d'usine `createDog`.

Cela prend plus de mémoire que nécessaire et n'est pas [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Ne serait-il pas agréable si, au lieu de copier les définitions de méthodes dans `zeus` et `casey`, nous pouvions définir nos méthodes en un seul endroit. Ensuite, faire en sorte que `zeus` et `casey` pointent vers cet endroit ?

#### Refactorisation 1 : Implémentation d'un modèle de conception « Prototypal Class »

L'héritage prototypal nous donne exactement ce que nous avons demandé ci-dessus. Il nous permettra de définir nos méthodes dans un objet prototype. Ensuite, faire en sorte que `zeus`, `casey`, et infiniment plus d'objets comme eux pointent vers ce prototype. `zeus` et `casey` auront alors accès à toutes les méthodes et propriétés de ce prototype par référence.

> _NOTE : Pour les moins familiers, il existe [de nombreux](https://guide.freecodecamp.org/javascript/prototypes/) [excellents](https://hackernoon.com/prototypes-in-javascript-5bba2990e04b) [tutoriels](https://medium.freecodecamp.org/prototype-in-js-busted-5547ec68872) qui expliquent le concept d'héritage prototypal en beaucoup plus de profondeur que je ne le fais ici !_

> _UNE NOTE SUR MES EXEMPLES CI-DESSOUS : Pour une clarté pédagogique, j'utilise des [fonctions d'usine](https://stackoverflow.com/questions/8698726/constructor-function-vs-factory-functions) nommées_ `createDog`_, plutôt que des [fonctions constructeurs](https://stackoverflow.com/questions/8698726/constructor-function-vs-factory-functions) ES5, pour implémenter un [modèle prototypal](https://medium.com/javascript-scene/3-different-kinds-of-prototypal-inheritance-es6-edition-32d777fa16c9) d'héritage. Je choisis d'utiliser des fonctions d'usine parce qu'elles ont moins de « magie sous le capot » et de « sucre syntaxique » que les constructeurs ES5. Espérons que cela facilite la concentration sur le problème en question !_

Super ! Maintenant, les objets correspondant à `zeus` et `casey` ne contiennent pas eux-mêmes de copies des méthodes `giveTreat` et `pet`. Au lieu de cela, les objets recherchent ces méthodes dans leur prototype `methodsForShowingAffection`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XDj8pysP_Qt6QUc94J7tWw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFxKUWpR7gkaIkoiHG4i3w.png)

Mais ne serait-il pas agréable si `methodsForShowingAffection` était encapsulé dans la fonction d'usine `createDog` ? Cela rendrait clair que ces méthodes sont destinées à être utilisées uniquement avec cette fonction. Ainsi, une simple refactorisation nous laisse avec :

#### Refactorisation 2 : Héritage prototypal + la propriété prototype des fonctions d'usine

Super ! Mais `methodsForShowingAffection` n'est-il pas un nom long et étrange pour une propriété ? Pourquoi ne pas utiliser quelque chose de plus générique et prévisible ? Il s'avère que les concepteurs de Javascript nous fournissent exactement ce que nous cherchons. Une propriété intégrée `prototype` sur chaque fonction, y compris une sur notre fonction d'usine `createDog`.

Notez qu'il n'y a rien de spécial dans cette propriété `prototype`. Comme montré ci-dessus, nous pourrions obtenir exactement le même résultat en définissant le prototype de `createDog` sur un objet séparé appelé `methodsForShowingAffection`. La normalité de la propriété `prototype` sur les fonctions en Javascript suggère son cas d'utilisation prévu : une commodité destinée à faciliter un modèle de conception courant. Rien de plus, rien de moins.

**Lectures complémentaires :**

Pour en savoir plus sur la propriété `prototype` des fonctions en JavaScript, voir la section « the function prototype » dans [cet](http://sporto.github.io/blog/2013/02/22/a-plain-english-guide-to-javascript-prototypes/) article de blog de [Sebastian Porto](https://www.freecodecamp.org/news/what-we-really-mean-when-we-talk-about-prototypes-165586f29fa9/undefined).

L'article [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes) sur les prototypes.