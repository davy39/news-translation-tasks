---
title: Comment encoder et décoder HTML Base64 en utilisant JavaScript – Exemple d'encodage
  JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-08T19:20:23.000Z'
originalURL: https://freecodecamp.org/news/encode-decode-html-base64-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template-1.png
tags:
- name: encoding
  slug: encoding
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment encoder et décoder HTML Base64 en utilisant JavaScript – Exemple
  d'encodage JS
seo_desc: 'When building an application or writing a program, you may need to encode
  or decode with HTML Base64 in JavaScript.

  This is possible thanks to two Base64 helper functions that are part of the HTML
  specification and are supported by all modern browser...'
---

Lorsque vous construisez une application ou écrivez un programme, vous pouvez avoir besoin d'encoder ou de décoder avec HTML Base64 en JavaScript.

Cela est possible grâce à deux fonctions d'assistance Base64 qui font partie de la spécification HTML et sont prises en charge par tous les navigateurs modernes.

Dans cet article, vous apprendrez ce qu'est Base64 et comment il fonctionne pour convertir des données binaires, des [chaînes de caractères](https://www.freecodecamp.org/news/what-is-a-string-in-javascript/) régulières et bien plus encore en texte ASCII.

## Qu'est-ce que Base64 ?

[Base64](https://en.wikipedia.org/wiki/Base64) est un groupe de schémas d'encodage binaire-texte représentant des données binaires au format de chaîne ASCII. Il est couramment utilisé pour encoder des données qui doivent être stockées ou transmises de manière à ne pas pouvoir être directement représentées sous forme de texte.

L'encodage Base64 fonctionne en mappant les données binaires à 64 caractères de l'ensemble de caractères ASCII. Les 64 caractères utilisés dans l'encodage Base64 sont : `A-Z`, `a-z`, `0-9`, `+`, et `/`.

Le processus d'encodage prend 3 octets de données binaires et les mappe à 4 caractères de l'ensemble ci-dessus, de sorte qu'un seul caractère représente chaque 6 bits de données binaires. Le résultat est une chaîne de caractères ASCII qui peut être transmise ou stockée sous forme de texte.

Le décodage Base64 est le processus inverse de l'encodage. Il prend une chaîne encodée Base64 et mappe chaque caractère à sa représentation binaire de 6 bits. Les données binaires résultantes sont une reconstruction des données binaires originales encodées en Base64.

## Comment encoder et décoder HTML Base64 en utilisant JavaScript

Pour encoder et décoder en JavaScript, vous utiliserez les fonctions JavaScript `btoa()` et `atob()` qui sont disponibles et prises en charge par les navigateurs web modernes.

Ces fonctions d'assistance JavaScript sont nommées d'après d'anciennes commandes Unix pour convertir le binaire en ASCII (btoa) et l'ASCII en binaire (atob).

Vous pouvez encoder une chaîne en base64 en JavaScript en utilisant la fonction `btoa()` et décoder une chaîne base64 en utilisant la fonction `atob()`. Par exemple, si vous avez une chaîne stockée dans une variable, comme vu ci-dessous, vous pouvez d'abord l'encoder en Base64 :

```js
let myString = "Bienvenue chez freeCodeCamp !";
let encodedValue = btoa(myString);
console.log(encodedValue); // V2VsY29tZSB0byBmcmVlQ29kZUNhbXAh
```

Vous pouvez également décoder la `encodedValue` pour retrouver sa forme originale en utilisant la fonction `atob()`. Cette fonction prend la valeur encodée et la décode depuis Base64 :

```js
let myString = "Bienvenue chez freeCodeCamp !";
let encodedValue = btoa(myString);
let decodedValue = atob(encodedValue);
console.log(decodedValue); // Bienvenue chez freeCodeCamp !
```

Vous savez maintenant comment encoder et décoder Base64 en JavaScript.

## Plus d'exemples d'encodage JavaScript

Vous pouvez également encoder des données binaires en texte ASCII encodé Base64 en JavaScript en utilisant la fonction `btoa()` :

```js
let binaryData = new Uint8Array([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]);
let stringValue = String.fromCharCode.apply(null, binaryData);
console.log(stringValue); // "Hello World"

let encodedValue = btoa(stringValue);
console.log(encodedValue); // SGVsbG8gV29ybGQ=
```

Dans l'exemple ci-dessus, vous avez d'abord converti les valeurs Unicode en caractères, puis encodé la chaîne.

Vous pouvez également décoder le texte ASCII encodé Base64 en données binaires en JavaScript en utilisant la fonction `atob()` :

```js
let encodedValue = "SGVsbG8gV29ybGQ=";
let binaryData = new Uint8Array(atob(encodedValue).split("").map(function (c) {
    return c.charCodeAt(0);
}));
console.log(binaryData); // Uint8Array [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
```

## Conclusion !

Dans cet article, vous avez appris ce que signifie Base64, comment il fonctionne et quand encoder et décoder en JavaScript.

Base64 n'est pas destiné à être une méthode de chiffrement sécurisée, ni à être une méthode de compression, car l'encodage d'une chaîne en Base64 entraîne généralement une sortie 33 % plus longue.

L'encodage Base64 est couramment utilisé en JavaScript pour des situations comme :

* Stocker et transmettre des données binaires sous forme de texte.

* Chiffrer des données où les données encodées sont envoyées sur un canal non sécurisé et décodées à l'autre extrémité. Cependant, cela ne doit pas être considéré comme une méthode de chiffrement sécurisée, car elle peut être facilement décodée.

* Transfert de données entre des systèmes avec des jeux de caractères différents.

* Stocker des données binaires dans une base de données.

Merci d'avoir lu et amusez-vous bien en codant !

Vous pouvez accéder à plus de 185 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.