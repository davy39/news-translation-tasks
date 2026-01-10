---
title: Les Différences Entre forEach() et map() que Tout Développeur Doit Connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T17:50:37.000Z'
originalURL: https://freecodecamp.org/news/4-main-differences-between-foreach-and-map
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/cover4.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Les Différences Entre forEach() et map() que Tout Développeur Doit Connaître
seo_desc: "By Ibrahima Ndaw\nJavaScript has some handy methods which help us iterate\
  \ through our arrays. The two most commonly used for iteration are Array.prototype.map()\
  \ and Array.prototype.forEach(). \nBut I think that they remain a little bit unclear,\
  \ especia..."
---

Par Ibrahima Ndaw

JavaScript dispose de certaines méthodes pratiques qui nous aident à parcourir nos tableaux. Les deux méthodes les plus couramment utilisées pour l'itération sont `Array.prototype.map()` et `Array.prototype.forEach()`. 

Mais je pense qu'elles restent un peu floues, surtout pour un débutant. Parce qu'elles effectuent toutes les deux une itération et produisent quelque chose. Alors, quelle est la différence ?

Dans cet article, nous allons examiner les points suivants :

* Définitions
* La valeur de retour
* La capacité à enchaîner d'autres méthodes
* Mutabilité
* Vitesse de performance
* Réflexions finales

## Définitions

La méthode `map` reçoit une fonction en tant que paramètre. Ensuite, elle l'applique à chaque élément et retourne un nouveau tableau entièrement peuplé avec les résultats de l'appel de la fonction fournie. 

Cela signifie qu'elle retourne un nouveau tableau qui contient une image de chaque élément du tableau. Elle retournera toujours le même nombre d'éléments.

```javascript

const myAwesomeArray = [5, 4, 3, 2, 1]

myAwesomeArray.map(x => x * x)

// >>>>>>>>>>>>>>>>> Sortie : [25, 16, 9, 4, 1]
```

Comme `map`, la méthode `forEach()` reçoit une fonction en tant qu'argument et l'exécute une fois pour chaque élément du tableau. Cependant, au lieu de retourner un nouveau tableau comme `map`, elle retourne `undefined`.

```javascript
const myAwesomeArray = [
  { id: 1, name: "john" },
  { id: 2, name: "Ali" },
  { id: 3, name: "Mass" },
]

myAwesomeArray.forEach(element => console.log(element.name))
// >>>>>>>>> Sortie : john
//                    Ali
//                    Mass
```

## 1. La valeur de retour

La première différence entre `map()` et `forEach()` est la valeur de retour. La méthode `forEach()` retourne `undefined` et `map()` retourne un nouveau tableau avec les éléments transformés. Même si elles font le même travail, la valeur de retour reste différente.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]
myAwesomeArray.forEach(x => x * x)
//>>>>>>>>>>>>>valeur de retour : undefined

myAwesomeArray.map(x => x * x)
//>>>>>>>>>>>>>valeur de retour : [1, 4, 9, 16, 25]

```

## 2. La capacité à enchaîner d'autres méthodes

La deuxième différence entre ces méthodes de tableau est le fait que `map()` est chaînable. Cela signifie que vous pouvez attacher `reduce()`, `sort()`, `filter()` et ainsi de suite après avoir effectué une méthode `map()` sur un tableau. 

C'est quelque chose que vous ne pouvez pas faire avec `forEach()` parce que, comme vous pouvez le deviner, elle retourne `undefined`.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]
myAwesomeArray.forEach(x => x * x).reduce((total, value) => total + value)
//>>>>>>>>>>>>> Uncaught TypeError: Cannot read property 'reduce' of undefined
myAwesomeArray.map(x => x * x).reduce((total, value) => total + value)
//>>>>>>>>>>>>>valeur de retour : 55

```

## 3. Mutabilité

En général, le mot "mutate" signifie changer, alterner, modifier ou transformer. Et dans le monde JavaScript, il a la même signification. 

Un objet mutable est un objet dont l'état peut être modifié après sa création. Alors, qu'en est-il de `forEach` et `map` concernant la mutabilité ?

Eh bien, selon la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript) :

`forEach()` ne mute pas le tableau sur lequel il est appelé. (Cependant, `callback` peut le faire).

`map()` ne mute pas le tableau sur lequel il est appelé (bien que `callback`, si invoqué, puisse le faire).

_JavaScript est bizarre_.

![Gif](https://media.giphy.com/media/KWn5YHuCzP3FK/giphy.gif)

Ici, nous voyons une définition très similaire, et nous savons tous qu'elles reçoivent toutes les deux un `callback` en tant qu'argument. Alors, laquelle repose sur l'immuabilité ?

Eh bien, à mon avis, cette définition n'est pas claire. Et pour savoir laquelle ne mute pas le tableau original, nous devons d'abord vérifier comment ces deux méthodes fonctionnent.

La méthode `map()` retourne un nouveau tableau entièrement peuplé avec les éléments transformés et la même quantité de données. Dans le cas de `forEach()`, même si elle retourne `undefined`, elle mutera le tableau original avec le `callback`.

Par conséquent, nous voyons clairement que `map()` repose sur l'immuabilité et que `forEach()` est une méthode de mutation.

## 4. Vitesse de performance

En ce qui concerne la vitesse de performance, elles sont un peu différentes. Mais, est-ce que cela compte ? Eh bien, cela dépend de diverses choses comme votre ordinateur, la quantité de données que vous traitez, et ainsi de suite. 

Vous pouvez vérifier par vous-même avec l'exemple ci-dessous ou avec [jsPerf](https://jsperf.com/) pour voir laquelle est la plus rapide.

```javascript
const myAwesomeArray = [1, 2, 3, 4, 5]

const startForEach = performance.now()
myAwesomeArray.forEach(x => (x + x) * 10000000000)
const endForEach = performance.now()
console.log(`Vitesse [forEach] : ${endForEach - startForEach} millisecondes`)

const startMap = performance.now()
myAwesomeArray.map(x => (x + x) * 10000000000)
const endMap = performance.now()
console.log(`Vitesse [map] : ${endMap - startMap} millisecondes`)

```

# Réflexions finales

Comme toujours, le choix entre `map()` et `forEach()` dépendra de votre cas d'utilisation. Si vous prévoyez de changer, d'alterner ou d'utiliser les données, vous devriez choisir `map()`, car il retourne un nouveau tableau avec les données transformées. 

Mais, si vous n'aurez pas besoin du tableau retourné, n'utilisez pas `map()` - utilisez plutôt `forEach()` ou même une boucle `for`.

Espérons que cet article clarifie les différences entre ces deux méthodes. Si vous connaissez d'autres différences, n'hésitez pas à les partager dans la section des commentaires, sinon merci de l'avoir lu.

Lisez plus de mes articles sur [mon blog](https://www.ibrahima-ndaw.com)

Photo par [Franck V.](https://unsplash.com/@franckinjapan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/different?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)