---
title: JavaScript Number to String – Comment utiliser toString pour convertir un Int
  en String
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-22T13:48:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-number-to-string-how-to-use-tostring-to-convert-an-int-into-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/js-number-tostring.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Number to String – Comment utiliser toString pour convertir
  un Int en String
seo_desc: 'The toString() method is a built-in method of the JavaScript Number object
  that allows you to convert any number type value into its string type representation.

  How to Use the toString Method in JavaScript

  To use the toString() method, you simply nee...'
---

La méthode `toString()` est une méthode intégrée de l'objet `Number` de JavaScript qui vous permet de convertir toute valeur de type `number` en sa représentation de type `string`.

## Comment utiliser la méthode toString en JavaScript

Pour utiliser la méthode `toString()`, vous devez simplement appeler la méthode sur une valeur de type `number`. L'exemple suivant montre comment convertir la valeur numérique `24` en sa représentation sous forme de chaîne. Remarquez comment la valeur de la variable `str` est entourée de guillemets doubles :

```js
var num = 24;
var str = num.toString();

console.log(num); // 24
console.log(str); // "24"
```

Vous pouvez également appeler la méthode `toString()` directement sur une valeur de type `number`, mais vous devez ajouter des parenthèses `()` pour envelopper la valeur, sinon JavaScript répondra avec une erreur `Invalid or unexpected token`.

La méthode `toString()` peut également convertir des nombres flottants et négatifs comme montré ci-dessous :

```js
24.toString(); // Erreur : Invalid or unexpected token
(24).toString(); // "24"
(9.7).toString(); // "9.7"
(-20).toString(); // "-20"
```

Enfin, la méthode `toString()` accepte également le paramètre `radix` ou `base`. Le `radix` vous permet de convertir un nombre du système décimal (base 10) en une chaîne représentant le nombre dans d'autres systèmes de numération.

Les systèmes de numération valides pour la conversion incluent :

* Système binaire (base 2) qui a 2 chiffres, 0 et 1
* Système ternaire (base 3) qui a 3 chiffres 0, 1 et 2
* Système quaternaire (base 4) qui a 4 chiffres, 0, 1, 2 et 3
* Et ainsi de suite jusqu'au système hexatridécimal (base 36) qui a la combinaison des chiffres arabes 0 à 9 et des lettres latines A à Z

```js
Number.toString(radix);
```

Le paramètre `radix` accepte une donnée de type `number` avec des valeurs allant de `2` à `36`. Voici un exemple de conversion du nombre décimal `5` en sa représentation binaire (base 2) :

```js
var str = (5).toString(2);

console.log(str); // "101"
```

Le nombre décimal `5` du code ci-dessus est converti en son équivalent binaire `101` puis converti en chaîne.

## Comment utiliser d'autres types de données avec la méthode toString()

Outre la conversion du type `number`, la méthode `toString()` est également disponible pour convertir d'autres types de données en leurs représentations sous forme de chaîne.

Par exemple, vous pouvez convertir un type `array` en sa représentation `string` comme suit :

```js
var arr = [ "Nathan", "Jack" ];
var str = arr.toString();

console.log(str); // "Nathan,Jack"
```

Ou un type `boolean` en `string` comme montré ci-dessous :

```js
var bool = true;
var str = bool.toString();

console.log(str); // "true"
```

Mais je pense que vous utiliserez le plus souvent la méthode `toString()` pour convertir un `number` en `string` plutôt que les autres. C'est ce que je fais habituellement aussi :)

## **Merci d'avoir lu ce tutoriel**

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !