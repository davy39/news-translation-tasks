---
title: Voici les nouvelles méthodes et fonctions intégrées en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-06T15:35:51.000Z'
originalURL: https://freecodecamp.org/news/here-are-the-new-built-in-methods-and-functions-in-javascript-8f4d2fd794fa
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6T_wl1LRh_Cd7JZS.png
tags:
- name: ES6
  slug: es6
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Voici les nouvelles méthodes et fonctions intégrées en JavaScript
seo_desc: 'By Said Hayani

  In the past few years, JavaScript has come out with many new releases. They have
  brought new features particularly in the syntax and its core. These updates have
  made JavaScript more readable and clever. I will introduce us to the new ...'
---

Par Said Hayani

Au cours des dernières années, JavaScript a sorti de nombreuses nouvelles versions. Elles ont apporté de nouvelles fonctionnalités, particulièrement en termes de syntaxe et de son cœur. Ces mises à jour ont rendu JavaScript plus lisible et intelligent. Je vais vous présenter les nouvelles méthodes pour les tableaux, les objets et les chaînes de caractères. Ces nouvelles méthodes peuvent gérer les données de manière élégante et efficace en écrivant moins de code. C'est ce que nous allons expliquer dans cet article.

### Les nouvelles méthodes d'objets

L'objet est ce qui fait de JavaScript un langage de programmation puissant. Les objets vous permettent de regrouper différents types de données. Si vous souhaitez apprendre un nouveau framework JavaScript comme React, Vue ou Angular, vous devez savoir comment utiliser les objets et leurs méthodes. Ces frameworks utilisent des objets pour obtenir et gérer les entrées utilisateur. Les nouvelles versions de JavaScript apportent de nouvelles méthodes aux objets qui les rendent plus amusants. Voici les nouvelles méthodes d'objets :

#### Object.assign()

La méthode Object.assign() a plusieurs fonctions. Elle peut copier un objet, cloner à partir d'un autre objet ou concaténer deux objets ou plus.

* Copier les valeurs d'un autre objet :

![Image](https://cdn-media-1.freecodecamp.org/images/0*qBKsVujrVAl6xOLe.png)

* Cloner un objet vers un nouvel objet

![Image](https://cdn-media-1.freecodecamp.org/images/0*mcuQcGDjdMp0cJr0.png)

* Vous pouvez également fusionner des propriétés en double avec Object.assign() en définissant deux crochets vides comme premier argument :

![Image](https://cdn-media-1.freecodecamp.org/images/0*SijirtBAtch9RQJV.png)

#### Object.entries()

La méthode Object.entries() retourne les clés et les valeurs de l'objet sous forme de tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/0*blt56m05sgP-W66J.png)

#### Object.getOwnPropertyDescriptors()

Object.getOwnPropertyDescriptors nous permet d'obtenir le descripteur de propriétés pour un objet.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kHGzsS7CxFNC4KxR.png)

C'est vraiment utile pour vérifier le descripteur de propriété de l'objet, par exemple, voir s'il est modifiable ou énumérable.

### Les nouvelles méthodes de tableaux

Les nouvelles versions de JavaScript ont fourni de nouvelles méthodes pour les tableaux. Voici les nouvelles méthodes de tableaux :

#### Array.includes()

![Image](https://cdn-media-1.freecodecamp.org/images/0*eUKyNo_HsBiZlu-5.png)

Array.includes() nous permet de vérifier si une propriété existe dans un tableau. Vous pouvez voir la différence entre l'ancien code et la nouvelle syntaxe (ES6). La nouvelle méthode est courte et plus lisible.

#### Array.find()

Array.find() nous aide à trouver un élément dans un tableau. Il prend une fonction de rappel comme argument. La fonction de rappel offre plus d'options pour trouver et extraire des données complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*W22CN1By0zY_5b5c.png)

Si la propriété que nous recherchons existe, elle retourne la valeur trouvée. Sinon, elle retourne indéfini.

#### Array.findIndex()

Array.findIndex() retourne l'index de l'élément trouvé au lieu de la valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*geI5dkTiKkgj1fcJ.png)

#### Array.values()

Cette nouvelle méthode retourne un itérateur de tableau des valeurs afin que nous puissions exécuter une boucle for pour extraire chaque valeur du tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zy4yz0gjJmr4OFjE.png)

#### Array.entries()

Array.entries() retourne à la fois la clé et la valeur dans un format de tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/0*e3yydx80kfPQ4z45.png)

#### Array.from()

Array.from() a été introduit dans la version ES6. Il peut faire plusieurs choses en exécutant une fonction map() sur les données. Il peut convertir une chaîne en tableau ou même créer un nouveau tableau à partir des données.

![Image](https://cdn-media-1.freecodecamp.org/images/0*KB7Rka-Xbqfz3JSJ.png)

#### Array.keys()

Comme son nom l'indique, cette méthode retourne les clés du tableau.

### Les nouvelles méthodes de chaînes de caractères

Les nouvelles versions de JavaScript ont fourni de nouvelles méthodes de chaînes de caractères. Voici les nouvelles méthodes de chaînes de caractères :

#### String.repeat()

La méthode String.repeat() vous permet de répéter une chaîne de caractères.

![Image](https://cdn-media-1.freecodecamp.org/images/0*eGcnsadh8dExe7Cv.png)

#### String.includes()

String.includes() fonctionne comme Array.includes(). Il retourne un booléen si la valeur entrée existe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*pgzvrQp-DDjq5qph.png)

### Les nouvelles méthodes de nombres

Les nouvelles versions de JavaScript ont fourni de nouvelles méthodes de nombres. Voici les nouvelles méthodes de nombres :

#### Number.isNaN()

Cette méthode a été publiée dans la mise à jour ES6. Elle vérifie la valeur de nombre passée et retourne vrai si la valeur est NaN. Sinon, elle retourne faux. Cette méthode est inspirée de la fonction classique isNAN() en JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8VdOzRolKT5_sz8w.png)

#### Number.isInteger()

Comme la méthode précédente, Number.isInteger() vérifie si la valeur passée est un entier ou non. Il retournera vrai si la valeur est un entier et faux si ce n'est pas le cas.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4KiJXHrDWgDKiSuv.png)

#### Number.isSafeInteger()

Vous pouvez toujours vouloir valider les entrées des utilisateurs pour vous assurer qu'il s'agit d'un nombre. Number.isSafeInteger() vérifie si le nombre est un nombre sûr.

[En savoir plus ici](https://www.sitepoint.com/es6-number-methods/)

![Image](https://cdn-media-1.freecodecamp.org/images/0*HOWyMxHakQXnhaf-.png)

#### Number.isFinite()

Number.isFinite() vérifie si la valeur passée est un nombre fini ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hZ7YCJL1fR6wRz-c.png)

### **Support des navigateurs**

Les nouvelles méthodes de nombres sont presque supportées par les principaux navigateurs, à l'exception d'Opera Mini et IE-11. Le support est montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*XZu4NeqSS8Bs0szA.png)

### Nouveaux objets spécifiques

JavaScript vient avec de nouvelles fonctions spécifiques qui nous permettent d'écrire un code plus performant. Voici les nouvelles méthodes d'objets spécifiques :

### Objet Proxy()

Proxy est l'une des grandes additions à JavaScript. Il crée un comportement personnalisé pour notre code. Avec Proxy, vous pouvez gérer :

* la validation des données utilisateur
* la correction des données
* la recherche de propriété
* l'assignation
* l'énumération
* l'invocation de fonction

Vérifiez d'autres utilisations de Proxy et ses méthodes [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy).

Pour comprendre le proxy, nous allons écrire deux exemples.

**Exemple 1 :**

Dans cet exemple, nous validons les données lors de leur récupération auprès d'un utilisateur. Nous allons essayer de définir le comportement d'une erreur indéfinie.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yWBsgDpISrx1K9Y3.png)

Comme vous le voyez dans l'exemple ci-dessus, userInfo.favCar retourne `undefined`. Que faire si nous voulons gérer ce message d'erreur ? Si nous voulons créer un comportement personnalisé pour l'erreur, par exemple, afficher un autre message au lieu de undefined, nous pouvons utiliser Proxy dans ce cas.

![Image](https://cdn-media-1.freecodecamp.org/images/0*rX4-Jfbm21ZoTDyC.png)

Nous avons défini un nouveau proxy et lui avons donné deux arguments — l'objet et le gestionnaire. Le gestionnaire exécute un code de validation et vérifie si la propriété existe dans l'objet. Il retourne la propriété si elle existe. Sinon, il retourne le message que nous avons défini et cela s'appelle **property lookup**.

**Exemple 2 :**

Dans cet exemple, nous allons créer une validation pour une valeur spécifique dans l'objet en utilisant la méthode **set**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zQ31N-WaHiuTcdli.png)

Dans cet exemple, nous pouvons valider le type de données et retourner une nouvelle TypeError(). Cela rend le débogage beaucoup plus facile. Vous pouvez comprendre davantage avec cet [article utile](https://hackernoon.com/introducing-javascript-es6-proxies-1327419ab413).

### **Support des navigateurs**

Proxy fonctionne assez bien pour tous les principaux navigateurs comme vous pouvez le voir ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*7-0oJu4wU3M-1SYP.png)

#### Objet Set()

L'objet Set est une nouvelle fonctionnalité en JavaScript. Il nous permet de stocker des valeurs uniques. Il dispose d'un ensemble de méthodes avec lesquelles vous pouvez jouer. La méthode Object.add vous permet d'ajouter une nouvelle propriété à l'objet. Object.delete supprime une propriété de l'objet. Object.clear efface toutes les propriétés de l'objet. L'exemple ci-dessous explique les méthodes de l'objet.

![Image](https://cdn-media-1.freecodecamp.org/images/0*u9kaEZqYht6qpTFH.png)

En savoir plus sur l'objet Set() [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set).

### Conclusion

Nous venons de couvrir les nouvelles méthodes intégrées introduites par JavaScript. Avec ces nouvelles fonctionnalités, je n'utilise plus l'ancienne syntaxe et les anciennes méthodes dans mon code. Les nouvelles méthodes vous permettent d'écrire du code JavaScript performant et efficace de manière élégante.

Vous pouvez également consulter mes articles sur la [nouvelle syntaxe ES6](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2) pour rafraîchir vos compétences en JavaScript.

> Vous pouvez me trouver sur T[witter](https://twitter.com/SaidHYN?lang=en) et [Instagram](https://www.instagram.com/saidhappy6/)

**_Articles précédents :_**

* [JavaScript ES6 — Écrire moins, faire plus](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2)
* [Apprendre Bootstrap 4 en 30 min en construisant un site web de landing page](https://medium.freecodecamp.org/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33)
* [Angular 6 et ses nouvelles fonctionnalités, tout expliqué en trois minutes](https://medium.freecodecamp.org/angular-what-is-the-new-briefly-e6837348dd3a)
* [Comment utiliser le routage dans Vue.js pour créer une meilleure expérience utilisateur](https://medium.freecodecamp.org/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9)
* [Voici les moyens les plus populaires de faire une requête HTTP en JavaScript](https://medium.freecodecamp.org/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa)
* [Apprendre à créer votre première application Angular en 20 minutes](https://medium.freecodecamp.org/learn-how-to-create-your-first-angular-app-in-20-min-146201d9b5a7)