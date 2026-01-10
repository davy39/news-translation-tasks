---
title: Comment stocker des objets ou des tableaux dans le stockage local du navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T07:55:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-objects-or-arrays-in-browser-local-storage
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/30-objects-arrays-localstorage.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Comment stocker des objets ou des tableaux dans le stockage local du navigateur
seo_desc: 'By Dillion Megida

  The local storage of browsers only accepts strings, but sometimes you want to store
  objects or arrays. How do you go about that? We''ll see how in this article.

  The browser local storage, is a Web Storage API that allows us to store ...'
---

Par Dillion Megida

Le stockage local des navigateurs n'accepte que les chaînes de caractères, mais parfois vous souhaitez stocker des objets ou des tableaux. Comment faire ? Nous allons voir comment dans cet article.

Le stockage local du navigateur est une API Web Storage qui nous permet de stocker des données pour un domaine à travers les sessions du navigateur. Ces données seront disponibles et accessibles par ce domaine pour toujours, jusqu'à ce qu'elles soient supprimées. Cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-81.png)

Vous pouvez accéder à cette vue en inspectant n'importe quelle page web, en allant dans la section Application, puis dans la section Storage, et en sélectionnant Local Storage. Vous verrez toutes les données qui ont été sauvegardées dans le stockage local pour le domaine de la page web.

Le stockage local est utile pour les données que vous souhaitez accéder rapidement, sans avoir à faire une requête API à un serveur backend. Un cas d'utilisation courant est les paramètres de personnalisation pour un utilisateur comme le schéma de couleurs ou d'autres paramètres que vous ne souhaitez pas toujours demander au serveur.

Cependant, vous ne pouvez stocker que des chaînes de caractères dans ce stockage :

```js
localStorage.setItem("key", "value")
```

Toute tentative de stocker un objet ou un tableau entraînera la conversion de la valeur en chaîne de caractères. Un objet comme `{name: "Dillion"}` sera converti en `"[object Object]"` et un tableau comme `[1,2]` sera converti en `"1,2"`.

Dans le cas du tableau, vous pouvez conserver les valeurs, mais pour l'objet, ces valeurs sont perdues. Alors, comment stocker correctement un objet et un tableau ?

J'ai une [vidéo sur ce sujet](https://youtu.be/E2rvDpubmnA) que vous pouvez également consulter.

## Conversion d'objets et de tableaux en chaînes de caractères

Puisque nous savons que le stockage local fonctionne avec des valeurs de chaîne de caractères, nous pouvons convertir les objets et les tableaux nous-mêmes, de manière à ne pas perdre le contenu de la valeur. Nous faisons cela en utilisant la méthode `JSON.stringify()`.

La méthode `stringify` de l'objet `JSON` convertit une valeur en une chaîne JSON, que nous pouvons stocker à la place. Voyons un exemple :

```js
const obj = {
  name: "Dillion",
  color_scheme: "dark"
}

const stringifiedObj = JSON.stringify(obj)

localStorage.setItem(
  "userInfo",
  stringifiedObj
)
```

Comme vous pouvez le voir ici, nous convertissons `obj` en une chaîne JSON, puis nous la stockons dans le stockage local. Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-86.png)

Lorsque vous cliquez sur l'élément dans le stockage, votre navigateur peut également vous montrer la valeur comme un objet réel sous le tableau (comme vous pouvez le voir ci-dessus).

Nous pouvons faire de même pour les tableaux :

```js
const interests = [
  "football",
  "fashion",
  "cooking"
]

const stringifiedInterests =
  JSON.stringify(interests)
  
localStorage.setItem(
  "interests",
  stringifiedInterests
)
```

Et la vue du stockage local :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-85.png)

Encore une fois, vous voyez que même si nous avons stocké une chaîne de caractères, le navigateur reconnaît qu'il s'agit d'un tableau converti en chaîne de caractères, donc en cliquant sur l'élément, vous voyez le tableau réel.

Puisqu'ils ont les valeurs sous forme de chaînes de caractères, comment les convertir en objets et tableaux lorsque nous voulons les utiliser ?

## Analyse des objets et tableaux convertis en chaînes de caractères

L'objet `JSON` dispose également d'une méthode `parse` qui permet d'analyser une chaîne JSON en valeur originale. Nous pouvons utiliser cette méthode pour obtenir l'objet original :

```js
const userInfo =
  localStorage.getItem('userInfo')
  
const userInfoParsed = JSON.parse(userInfo)

console.log(userInfoParsed.name)
// Dillion

console.log(userInfoParsed.color_scheme)
// dark
```

Et nous pouvons l'utiliser pour obtenir le tableau original :

```js
const interests =
  localStorage.getItem('interests')
  
const interestsParsed = JSON.parse(interests)

console.log(interestsParsed[1])
// fashion

console.log(interestsParsed[2])
// cooking
```

## Conclusion

Stocker des objets dans le stockage local vous permet de stocker un groupe de propriétés ensemble au lieu d'avoir plusieurs éléments dans le stockage. Par exemple, au lieu de stocker `userName` et `userColorScheme` séparément dans le stockage, vous pouvez stocker un objet avec les propriétés `name` et `color_scheme`.

Mais étant donné que le stockage local n'autorise que les valeurs de chaîne de caractères, vous devez d'abord convertir votre objet ou tableau en une chaîne de caractères.

Dans cet article, nous avons vu comment faire cela, ainsi que comment obtenir les valeurs originales lors de la récupération depuis le stockage local.

Si vous avez aimé cet article, veuillez le partager avec d'autres :)