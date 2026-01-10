---
title: Comment inverser un nombre en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-03T23:17:43.000Z'
originalURL: https://freecodecamp.org/news/js-basics-how-to-reverse-a-number-9aefc20afa8d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*9bS6yWpHz8_tuY52
tags:
- name: Women Who Code
  slug: women-who-code
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment inverser un nombre en JavaScript
seo_desc: 'By artismarti

  Examples using an arrow function and regular JS function


  _Photo by [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">chuttersnap on <a href="https://unsplash.com...'
---

Par artismarti

#### Exemples utilisant une fonction fléchée et une fonction JS régulière

![Image](https://cdn-media-1.freecodecamp.org/images/0*9bS6yWpHz8_tuY52)
_Photo par [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Inverser une chaîne de caractères ou inverser un nombre est l'une des questions courantes posées lors des entretiens de programmation. Voyons comment cela se fait.

#### **Règles/Limitations** :

* Les nombres négatifs doivent rester négatifs.

**_ex._** `-12345` _devient_ `-54321`

* Tous les zéros initiaux doivent être supprimés.

**_ex._** `321000` _devient_ `123` _et non_ `000123`

* La fonction peut accepter des flottants ou des entiers.

**_ex._** `543.2100` _devient_ `12.345`

* La fonction retournera les entiers sous forme d'entiers.

**_ex._** `54321` _devient_ `12345` _et non_ `12345.00`

#### **Solution avec une fonction fléchée** :

```js
const reversedNum = num => parseFloat(num.toString().split('').reverse().join('')) * Math.sign(num)
```

#### **Solution avec une fonction régulière** :

```js
function reversedNum(num) {
  return (
    parseFloat(
      num
        .toString()
        .split('')
        .reverse()
        .join('')
    ) * Math.sign(num)
  )
}
```

#### **_Différence entre une fonction fléchée et une fonction régulière_** :

Dans cet exemple, la seule différence entre la fonction fléchée et la fonction régulière est que la fonction régulière doit fournir une valeur de `return` explicite.

Les fonctions fléchées ont une valeur de `return` implicite — si elles peuvent être écrites en une ligne, sans avoir besoin des accolades `{}`.

<iframe height="500px" width="100%" src="https://repl.it/@artismarti/ReversedNumbers?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

#### **Décomposons les étapes** :

* **Convertir le nombre en chaîne de caractères**

`num.toString()` convertit le nombre donné en une chaîne de caractères. Nous faisons cela pour pouvoir utiliser la fonction `split` ensuite.

```js
let num = -5432100
num.toString()

// num = '-5432100'
```

* **Diviser la chaîne de caractères en un tableau**

`num.split('')` convertit la chaîne de caractères en un tableau de caractères. Nous faisons cela pour pouvoir utiliser la fonction de tableau reverse (_qui ne fonctionne pas sur une chaîne de caractères_).

```js
// num = '-5432100'

num.split('')

// num = [ '-', '5', '4', '3', '2', '1', '0', '0' ]
```

* **Inverser le tableau**

`num.reverse()` inverse l'ordre des éléments dans le tableau.

```js
// num = [ '-', '5', '4', '3', '2', '1', '0', '0' ]

num.reverse()

// num = [ '0', '0', '1', '2', '3', '4', '5', '-' ]
```

* **Rejoindre en une chaîne de caractères**

`num.join('')` réassemble les caractères inversés en une chaîne de caractères.

```js
// num = [ '0', '0', '1', '2', '3', '4', '5', '-' ]

num.join('')

// num = '0012345-'
```

* [**Analyser**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) **la valeur d'entrée en un nombre à virgule flottante** :

`parseFloat(num)` convertit `num` en un flottant à partir d'une chaîne de caractères.

```js
// num = '0012345-'

parseFloat(num)

// num = 12345
```

**Note** : `parseFloat` s'exécute à la fin (_même s'il est sur la première ligne de la fonction_) sur le nombre inversé et supprime tous les zéros initiaux.

* **Multiplier par le [signe](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sign) du nombre original — pour maintenir la valeur négative.**

`num * Math.sign(num)` multiplie le nombre par le signe du nombre original fourni.

```js
// valeur originale de num = -5432100
// num = 12345

num * Math.sign(-5432100)

// num = -12345
```

Et voilà !