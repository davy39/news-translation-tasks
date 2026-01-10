---
title: Exemple de division de chaîne JavaScript – Comment diviser une chaîne en un
  tableau en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T00:04:13.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-string-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/jon-flobrant-rB7-LCa_diU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Exemple de division de chaîne JavaScript – Comment diviser une chaîne en
  un tableau en JS
seo_desc: "By David\nA string is a data structure that represents a sequence of characters,\
  \ and an array is a data structure that contains multiple values. \nAnd did you\
  \ know – a string can be broken apart into an array of multiple strings using the\
  \ split method...."
---

Par David

Une chaîne de caractères est une structure de données qui représente une séquence de caractères, et un tableau est une structure de données qui contient plusieurs valeurs. 

Et saviez-vous – une chaîne peut être divisée en un tableau de plusieurs chaînes à l'aide de la méthode `split`. Voyons comment cela fonctionne avec quelques exemples.

## TL;DR

Si vous voulez juste le code, le voici :

```javascript
const publisher = 'free code camp'
publisher.split(' ') // [ 'free', 'code', 'camp' ]

```

## Syntaxe

Selon le [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), la syntaxe dont vous aurez besoin pour diviser la chaîne est `str.split([separator[, limit]])`. Si nous appliquons cela à l'exemple ci-dessus :

* `str` est `publisher`
* `separator` est `' '`
* il n'y a pas de `limit`

## Quand avez-vous besoin de diviser une chaîne ?

### Exemple 1 : obtenir une partie d'une chaîne

Voici un exemple courant qui implique d'obtenir le token d'un en-tête d'authentification qui fait partie d'un système d'authentification basé sur des tokens. 

Si cela ne signifie rien pour vous, ce n'est pas grave. Tout ce que vous devez savoir pour l'exemple suivant, c'est qu'il y a une chaîne avec la valeur `bearer token`, mais seul `token` est nécessaire (car c'est la partie qui identifie l'utilisateur) :

```javascript
const authHeader = 'bearer token'
const split = authHeader.split(' ') // (1) [ 'bearer', 'token' ]
const token = split[1] // (2) token
```

Voici ce qui se passe dans le code ci-dessus :

1. La chaîne est divisée avec `' '` comme séparateur
2. La deuxième entrée du tableau est accessible

### Exemple 2 : appliquer des méthodes de tableau à une chaîne

Souvent, l'entrée que vous recevez est une chaîne, mais vous souhaitez appliquer des méthodes de tableau (par exemple, `map`, `filter`, ou `reduce`). 

Par exemple, supposons que vous recevez une chaîne de code morse et que vous souhaitez voir ce qu'elle donne en anglais :

```javascript
const morse = '-.-. --- -.. .'
// (1)
const morseToChar = {
  '-.-.': 'c',
  '-..': 'd',
  '.': 'e',
  '---': 'o',
}

const morseArray = morse.split(' ') // (2) [ '-.-.', '---', '-..', '.' ]
const textArray = morseArray.map((char) => morseToChar[char]) // (3) [ 'c', 'o', 'd', 'e' ]
const text = textArray.join(") // (4)

```

Voici ce qui se passe dans le code ci-dessus :

1. Un objet littéral est créé pour mapper les caractères morse à l'alphabet anglais
2. Le code morse est divisé en un tableau avec un `' '` comme séparateur. (Sans `' '` comme argument, vous vous retrouveriez avec un tableau qui a des entrées séparées pour chaque `.` et `-`.)
3. Le tableau de code morse est mappé/transformé en un tableau de texte
4. Une chaîne est créée à partir du tableau avec `''` comme séparateur. (Sans `''` comme argument, la sortie serait `c,o,d,e`.)

## Comment ajouter une limite à split

Selon le [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), il est également possible de passer une `limit` comme argument à `split`. Je n'ai jamais eu besoin de le faire, mais voici comment vous pourriez l'appliquer :

```javascript
const publisher = 'free code camp'
publisher.split(' ', 1) // [ 'free' ]

```

Dans l'exemple ci-dessus, le tableau est limité à une entrée. Sans cela, la valeur du tableau serait `[ 'free', 'code', 'camp' ]`.

## Avant de partir…

Merci d'avoir lu jusqu'ici ! J'écris sur mes expériences professionnelles et éducatives en tant que développeur logiciel autodidacte, alors n'hésitez pas à consulter [mon site web](https://learnitmyway.com/) ou à vous abonner à [ma newsletter](https://learnitmyway.com/newsletter) pour plus de contenu.

Vous pourriez également aimer :

* [Apprendre JavaScript avec ces ressources](https://learnitmyway.com/learn-javascript-with-these-resources/)
* [Matériel d'apprentissage - développement logiciel](https://www.learnitmyway.com/2016/11/11/learning-material-software-development/) (en commençant par l'Intro à l'informatique)