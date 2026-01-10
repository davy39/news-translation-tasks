---
title: JavaScript forEach – Comment parcourir un tableau en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:20:04.000Z'
originalURL: https://freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99d8740569d1a4ca2204.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript forEach – Comment parcourir un tableau en JS
seo_desc: "By Cem Eygi\nThe JavaScript forEach method is one of the several ways to\
  \ loop through arrays. Each method has different features, and it is up to you,\
  \ depending on what you're doing, to decide which one to use. \nIn this post, we\
  \ are going to take a cl..."
---

Par Cem Eygi

La méthode JavaScript forEach est l'une des plusieurs façons de parcourir des tableaux. Chaque méthode a des caractéristiques différentes, et c'est à vous, selon ce que vous faites, de décider laquelle utiliser. 

Dans cet article, nous allons examiner de plus près la méthode JavaScript forEach.

Considérons que nous avons le tableau suivant ci-dessous :

```javascript
const numbers = [1, 2, 3, 4, 5];
```

L'utilisation de la boucle "for" traditionnelle pour parcourir le tableau serait comme ceci :

```javascript
for (i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
} 
```

## Qu'est-ce qui rend la méthode forEach() différente ?

La méthode forEach est également utilisée pour parcourir des tableaux, mais elle utilise une fonction différemment de la boucle "for" classique. 

La méthode forEach passe une [fonction de rappel](https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/) pour chaque élément d'un tableau avec les paramètres suivants : 

* Valeur actuelle (obligatoire) - La valeur de l'élément actuel du tableau
* Index (optionnel) - Le numéro d'index de l'élément actuel
* Tableau (optionnel) - L'objet tableau auquel appartient l'élément actuel

Permettez-moi d'expliquer ces paramètres étape par étape. 

Tout d'abord, pour parcourir un tableau en utilisant la méthode forEach, vous avez besoin d'une fonction de rappel (ou fonction anonyme) : 

```javascript
numbers.forEach(function() {
    // code
});
```

La fonction sera exécutée pour chaque élément du tableau. Elle doit prendre au moins un paramètre qui représente les éléments d'un tableau :

```javascript
numbers.forEach(function(number) {
    console.log(number);
});
```

C'est tout ce que nous devons faire pour parcourir le tableau :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z-2.png)

Alternativement, vous pouvez utiliser la représentation de la fonction fléchée ES6 pour simplifier le code :

```javascript
numbers.forEach(number => console.log(number));
```

## Paramètres optionnels

### Index

Très bien, continuons avec les paramètres optionnels. Le premier est le paramètre "index", qui représente le numéro d'index de chaque élément. 

En gros, nous pouvons voir le numéro d'index d'un élément si nous l'incluons comme deuxième paramètre :

```javascript
numbers.forEach((number, index) => {
    console.log('Index: ' + index + ' Valeur: ' + number);
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z-3.png)

### Tableau

Le paramètre tableau est le tableau lui-même. Il est également optionnel et peut être utilisé si nécessaire dans diverses opérations. Sinon, si nous l'appelons, il sera simplement imprimé autant de fois que le nombre d'éléments du tableau :

```javascript
numbers.forEach((number, index, array) => {
    console.log(array);
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Ads-z.png)

Vous pouvez voir l'exemple d'utilisation de la méthode forEach() dans cette vidéo :

%[https://youtu.be/E2GawbHDFfs]

## Support des navigateurs

La méthode Array.forEach est [prise en charge](https://caniuse.com/#search=Array.foreach) dans tous les navigateurs sauf IE version 8 ou antérieure :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z.png)
_[caniuse.com](https://caniuse.com)_

**Si vous souhaitez en savoir plus sur le développement Web, n'hésitez pas à visiter ma [Chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber).**

Merci d'avoir lu !