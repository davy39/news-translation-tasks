---
title: Métacaractères des expressions régulières - Que signifie \d en RegEx ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-02T13:42:55.000Z'
originalURL: https://freecodecamp.org/news/what-does-d-mean-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--2-.png
tags:
- name: Regex
  slug: regex
seo_title: Métacaractères des expressions régulières - Que signifie \d en RegEx ?
seo_desc: 'Regular expressions, otherwise known as RegEx or RegExp for short, are
  a defined pattern for matching a string or specific part(s) of a string. This string
  includes any character out there, be it letters, symbols, or digits.

  In this article, we’ll lo...'
---

Les expressions régulières, également connues sous le nom de RegEx ou RegExp, sont un motif défini pour correspondre à une chaîne de caractères ou à des parties spécifiques d'une chaîne. Cette chaîne inclut n'importe quel caractère, qu'il s'agisse de lettres, de symboles ou de chiffres.

Dans cet article, nous examinerons le caractère RegEx `\d`, que vous pouvez utiliser pour correspondre à un chiffre.


## Ce que nous allons couvrir
- [Qu'est-ce que `\d` en RegEx ?](#heading-quest-ce-que-d-en-regex)
- [Comment utiliser le métacaractère `\d`](#heading-comment-utiliser-le-metacaractere-d)
- [Quelle est la différence entre l'ensemble de caractères de chiffre `[0-9]` et le métacaractère `\d` ?](#heading-quelle-est-la-difference-entre-lensemble-de-caracteres-de-chiffre-0-9-et-le-metacaractere-d)
- [Conclusion](#heading-conclusion)


## Qu'est-ce que `\d` en RegEx ?

`\d` n'est pas seulement un « caractère » en RegEx, c'est l'un des « métacaractères » pour correspondre à des chaînes.

Par définition, les métacaractères sont des caractères qui ont une signification spéciale lors de la définition d'un motif pour correspondre à une chaîne.

Ainsi, **`\d` est un métacaractère qui correspond à n'importe quel chiffre de 0 à 9**. Vous pouvez l'utiliser pour correspondre à un chiffre ou à un ensemble de chiffres tels que des numéros de téléphone, des identifiants numériques, et plus encore.

En plus de `\d`, il existe d'autres métacaractères tels que :

* `\w` qui correspond à tous les caractères de mot (a-z, A-Z, 0-9, et _)
* `\D` qui correspond à tous les caractères non-chiffres. C'est l'opposé de `\d`
* `\W` qui correspond à tous les caractères non-mots
* `\s` qui correspond à tous les espaces blancs, y compris la barre d'espace, la tabulation et le retour


## Comment utiliser le métacaractère `\d`

Examinons comment correspondre à des nombres avec le métacaractère `\d`.

Le premier exemple que nous allons examiner est la correspondance d'un identifiant numérique, par exemple `7253289593`.

C'est un nombre à 10 chiffres. Pour le correspondre, vous pouvez répéter le métacaractère `\d` 10 fois :

![Screenshot-2023-03-02-at-12.10.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-02-at-12.10.33.png)

Ou vous pouvez écrire un seul `\d` et le répéter 10 fois :

![Screenshot-2023-03-02-at-12.11.39](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-02-at-12.11.39.png)

Vous pouvez également correspondre à des numéros de téléphone, par exemple des numéros de téléphone américains :

![Screenshot-2023-03-02-at-12.16.25](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-02-at-12.16.25.png)

Ou des numéros de téléphone nigérians de cette manière :

![Screenshot-2023-03-02-at-12.17.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-02-at-12.17.33.png)

Ce métacaractère `\d` fonctionne également bien avec JavaScript :

```js
// Tester un identifiant numérique
let id = '7253289593';
let regex1 = /\d{10}/g;

console.log(regex1.test(id)); // true

// Tester un numéro de téléphone américain
let UsPhoneNum = '(123) 456-7890';
let regex2 = /\(\d{3}\)\s\d{3}-\d{4}/g;

console.log(regex2.test(UsPhoneNum)); // true

// Tester un numéro de téléphone nigérian
let naijaPhoneNum = '08133333333';
let regex3 = /\d{11}/g;

console.log(regex3.test(naijaPhoneNum)); // true
```


## Quelle est la différence entre l'ensemble de caractères de chiffre `[0-9]` et le métacaractère `\d` ?

Il n'y a pas de grande différence entre l'ensemble de caractères `[0-9]` et le métacaractère `\d`.

La seule différence que vous pourriez voir est que certaines variantes de RegEx ne supportent pas `\d` mais supportent `[0-9]`. Par exemple, le RegEx de grep ne supporte pas le métacaractère `\d`.

Ainsi, si vous utilisez `[0-9]` à la place de `\d`, vous obtiendrez toujours une correspondance.

Par exemple, correspondons à l'identifiant numérique de l'exemple précédent avec `[0-9]` au lieu de `\d` :

![Screenshot-2023-03-02-at-12.28.17](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-02-at-12.28.17.png)

Vous pouvez voir que c'est toujours une correspondance. Ainsi, il n'y a pas de différence entre l'ensemble de caractères `[0-9]` et le métacaractère `\d`.


## Conclusion

Cet article vous a montré ce qu'est le métacaractère RegEx `\d` et comment l'utiliser. Nous avons examiné quelques exemples et l'avons également comparé avec l'ensemble de caractères de chiffre, `[0-9]`, afin que vous sachiez comment ils fonctionnent tous les deux.

Merci d'avoir lu.