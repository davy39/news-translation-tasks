---
title: Comment utiliser une RegExp pour confirmer la fin d'une chaîne en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T21:51:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-regexp-to-confirm-the-ending-of-a-string-in-javascript-4b42f3749af1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YLruZvgbUfHmlITM
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
seo_title: Comment utiliser une RegExp pour confirmer la fin d'une chaîne en JavaScript
seo_desc: 'By Catherine Vassant (aka Codingk8)

  Using the Regexp ?️ constructor


  _Photo by [Unsplash](https://unsplash.com/@jluebke?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Justin Luebke on <a href="https://unsplash.com?utm_...'
---

Par Catherine Vassant (aka Codingk8)

Utilisation du constructeur Regexp ?


![Image](https://cdn-media-1.freecodecamp.org/images/0*YLruZvgbUfHmlITM)
_Photo par [Unsplash](https://unsplash.com/@jluebke?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Justin Luebke</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

_Cet article est basé sur le défi "[Confirm the ending](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending)" de [freeCodeCamp](https://www.freecodecamp.org/)._

Ce défi consiste à vérifier si une chaîne se termine par une séquence spécifique de lettres ou non.

Dans cet article, j'expliquerai comment résoudre ce défi en utilisant une RegExp.

L'aspect intéressant de cette solution est l'utilisation du constructeur RegExp pour créer la RegExp spécifique dont vous avez besoin pour vérifier les chaînes passées en arguments.

#### Défi de l'algorithme

> Vérifiez si une chaîne (premier argument, `str`) se termine par la chaîne cible donnée (deuxième argument, `target`).

> Ce défi peut être résolu avec la méthode `.endsWith()`, introduite dans ES2015. Mais pour les besoins de ce défi, nous aimerions que vous utilisiez l'une des méthodes de sous-chaîne JavaScript à la place.

#### Cas de test fournis

> `confirmEnding("Bastian", "n")` doit retourner true.

> `confirmEnding("Congratulation", "on")` doit retourner true.

> `confirmEnding("Connor", "n")` doit retourner false.

> `confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification")` doit retourner false.

> `confirmEnding("He has to give me a new name", "name")` doit retourner true.

> `confirmEnding("Open sesame", "same")` doit retourner true.

> `confirmEnding("Open sesame", "pen")` doit retourner false.

> `confirmEnding("Open sesame", "game")` doit retourner false.

> `confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain")` doit retourner false.

> `confirmEnding("Abstraction", "action")` doit retourner true.

> N'utilisez pas la méthode intégrée `.endsWith()` pour résoudre le défi.

### 1. La première idée qui ne fonctionne pas du tout

Si, comme moi, vous êtes un amateur de RegExp, votre première tentative pourrait être d'essayer de résoudre le défi avec le **code ci-dessous**, et cela **ne fonctionnera pas**.

La raison est que, avec cette syntaxe, la fonction test() recherchera la chaîne spécifique "target" et non "target" en tant que variable passée en argument.

Si nous revenons à nos cas de test, ceux qui devraient retourner "false" passent, mais aucun de ceux qui devraient retourner "true" ne passe, ce qui est assez prévisible.

![Image](https://cdn-media-1.freecodecamp.org/images/0*eIBStwAQ1PDwZkrJ)
_Photo par [Unsplash](https://unsplash.com/@fotolancaster?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Pablo Lancaster Jones</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### 2. Résoudre le défi en créant la RegExp spécifique dont vous avez besoin avec le constructeur RegExp

Pour utiliser une RegExp qui va "comprendre" que l'argument "target" est une variable et non la chaîne "target", vous devez **créer une RegExp sur mesure en utilisant le constructeur RegExp**.

Et, avant d'aller plus loin, revenons une minute en arrière et regardons ce que nous voulons tester : l'argument "target" doit être la fin de l'argument "str". Cela signifie que **notre RegExp doit se terminer par le caractère "$"**.

#### **Maintenant, nous pouvons résoudre ce défi en trois étapes**

**Étape 1** - Créez une variable en ajoutant le "$" à la fin de l'argument "target", en utilisant la méthode concat() dans ce cas.

**Étape 2** - Utilisez le constructeur RegExp et l'opérateur "new" pour créer la bonne RegExp avec la variable ci-dessus.

**Étape 3** - Retournez le résultat de la fonction test().

Et cela passe tous les cas de test magnifiquement ?

#### **Cela peut être refactorisé en deux lignes comme ceci**

**Note** : puisque aucun des cas de test n'implique de tester la casse des lettres, il n'est pas nécessaire d'utiliser le drapeau "i".

#### Liens utiles

[String.prototype.concat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat) dans MDN

[RegExp.prototype.test()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test) dans MDN

[Constructeur RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) dans MDN

[Expressions régulières](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/regular-expressions) dans [freeCodeCamp](https://www.freecodecamp.org/)

#### Autres solutions à ce défi

Le **défi "[Get a Hint](https://guide.freecodecamp.org/certifications/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending/)"** suggère une solution utilisant la **méthode slice()**.

Vous pouvez trouver deux autres façons de résoudre ce défi, l'une avec la **méthode substr()** et l'autre avec la **méthode endsWith(), expliquées par [Sonya Moisset](https://www.freecodecamp.org/news/how-to-use-a-regexp-to-confirm-the-ending-of-a-string-in-javascript-4b42f3749af1/undefined) dans [cet article](https://medium.freecodecamp.org/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac)**.

Cette solution RegExp ad-hoc peut **également vous aider à résoudre le défi "[Search and Replace](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/search-and-replace)"** de l'algorithme intermédiaire de freeCodeCamp.

**Merci d'avoir lu !** ✨

Si vous avez aimé cet article, **n'hésitez pas à "applaudir" autant de fois que vous le souhaitez** et à le partager **pour aider d'autres personnes à le trouver**. Cela pourrait faire leur journée.

Si vous avez une **réaction/question/suggestion**, n'hésitez pas à laisser un **commentaire ci-dessous**. Je serai ravie de vous lire !

Vous pouvez également entrer en contact et/ou me suivre sur [**Twitter**](https://twitter.com/codingk8).