---
title: 'JavaScript : Mettre la première lettre en majuscule'
date: '2022-06-23T15:46:56.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/dillionmegida/
originalURL: https://freecodecamp.org/news/javascript-capitalize-first-letter-of-word
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/capitalize-first-letter.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_desc: "By Dillion Megida\nWhen you're coding, there are many ways to capitalize\
  \ the first letter of a word. You can use CSS as well as some JavaScript methods.\
  \ \nIn this article, I will show you one approach to achieve this.\nTo capitalize\
  \ the first letter of ..."
---


Lorsque vous développez, il existe de nombreuses façons de mettre la première lettre d'un mot en majuscule. Vous pouvez utiliser CSS ainsi que certaines méthodes JavaScript.

<!-- more -->

Dans cet article, je vais vous montrer une approche pour y parvenir.

Pour mettre la première lettre d'un mot en majuscule avec JS, vous devez comprendre trois méthodes de chaînes de caractères : **charAt**, **slice** et **toUpperCase**.

## La méthode de chaîne JavaScript `charAt`

Vous utilisez cette méthode pour récupérer le caractère à une position spécifiée dans une chaîne. En utilisant cette méthode, nous pouvons récupérer la première lettre d'un mot :

```js
const word = "freecodecamp"

const firstLetter = word.charAt(0)
// f
```

## La méthode de chaîne JavaScript `slice`

Vous utilisez cette méthode pour extraire une sous-chaîne d'une chaîne entière. Nous utiliserons cette méthode pour extraire la partie restante d'un mot (en excluant la première lettre) :

```js
const word = "freecodecamp"

const remainingLetters = word.substring(1)
// reecodecamp
```

## La méthode de chaîne JavaScript `toUpperCase`

`toUpperCase` est une méthode de chaîne qui renvoie la version en majuscules d'une chaîne spécifiée. Nous l'utiliserons pour mettre la première lettre en majuscule :

```js
const firstLetter = "f"

const firstLetterCap = firstLetter.toUpperCase()
// F
```

## Comment mettre la première lettre d'un mot en majuscule en JavaScript

En utilisant les trois méthodes de chaînes ci-dessus, nous allons récupérer le premier caractère du mot, le mettre en majuscule, puis le concaténer avec la partie restante extraite.

Cette approche donnera un nouveau mot dont la première lettre est en majuscule.

Voici le code correspondant :

```js
const word = "freecodecamp"

const firstLetter = word.charAt(0)

const firstLetterCap = firstLetter.toUpperCase()

const remainingLetters = word.slice(1)

const capitalizedWord = firstLetterCap + remainingLetters
// Freecodecamp
// F is capitalized
```

La version courte du code ci-dessus est :

```js
const word = "freecodecamp"

const capitalized =
  word.charAt(0).toUpperCase()
  + word.slice(1)
  
// Freecodecamp
// F is capitalized
```

Merci de votre lecture, et bon code !
