---
title: Opérateur Modulo en JavaScript – Comment Utiliser le Modulo en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-10T19:35:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-modulo-operator-how-to-use-the-modulus-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--1--1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Opérateur Modulo en JavaScript – Comment Utiliser le Modulo en JS
seo_desc: 'In JavaScript, you may need to perform mathematical calculations such as
  determining if a number is even or odd, wrapping values within a range, and converting
  between degrees and radians in trigonometry.

  To help you perform all these mathematical ca...'
---

En JavaScript, vous pourriez avoir besoin d'effectuer des calculs mathématiques tels que déterminer si un nombre est pair ou impair, envelopper des valeurs dans une plage, et convertir entre degrés et radians en trigonométrie.

Pour vous aider à effectuer tous ces calculs mathématiques, l'opérateur modulo peut être extrêmement utile.

Cet article expliquera ce qu'est l'opérateur modulo en JavaScript, comment l'utiliser et quels calculs mathématiques il peut effectuer.

## Qu'est-ce que l'Opérateur Modulo en JavaScript ?

L'opérateur modulo en JavaScript, également connu sous le nom d'opérateur de reste, est utilisé pour trouver le reste après la division d'un nombre par un autre. L'opérateur modulo en JavaScript est représenté par le signe de pourcentage (`%`).

Par exemple, `10 modulo 3` sera 1 (j'expliquerai comment cela fonctionne après l'exemple de code ci-dessous). La forme courte est 10 mod 3 = 1. Mais pour JavaScript, vous utiliserez `10 % 3`. Il divise le premier opérande (le dividende) par le second opérande (le diviseur) et retourne le reste.

let dividend = 10; let divisor = 3; let result = dividend % divisor; console.log(result); // retourne 1

Dans l'exemple ci-dessus, `10` divisé par `3` donne un quotient de `3` et un reste de `1`. L'opérateur modulo retourne ce reste, qui est `1`.

## Différentes Façons d'Utiliser l'Opérateur Modulo

Vous pouvez utiliser l'opérateur modulo de plusieurs manières, telles que vérifier si des nombres sont pairs ou impairs, envelopper des valeurs dans une plage, et bien plus encore.

### Comment vérifier si un nombre est pair ou impair avec l'opérateur modulo

Il existe de nombreuses façons de vérifier si un nombre est pair ou impair en JavaScript. Mais une méthode simple et souvent utilisée consiste à utiliser l'opérateur modulo. Vous faites cela en vérifiant si le résultat de l'opération `nombre modulo 2` est égal à 0 – si c'est le cas, le nombre est pair. Sinon, il est impair.

```js
let n = 7;
if (n % 2 === 0) {
  console.log(n + " est pair");
} else {
  console.log(n + " est impair");
}
```

Dans l'exemple ci-dessus, `n` représente le nombre. Vous pouvez essayer n'importe quel nombre et confirmer. Par exemple, vous pouvez en faire une fonction et passer des valeurs en arguments :

```js
const checkNumber = (n) => {
  if (n % 2 === 0) {
    console.log(n + " est pair");
  } else {
    console.log(n + " est impair");
  }
};

checkNumber(8); // "8 est pair"
checkNumber(21); // "21 est impair"
checkNumber(17); // "17 est impair"
checkNumber(10); // "10 est pair"
```

### Comment envelopper des valeurs dans une plage avec l'opérateur modulo

Envelopper une valeur/un nombre dans une plage fait référence à la prise d'un nombre qui se situe en dehors d'une plage spécifiée (par exemple 0 à 360) et à le "ramener" dans la plage. Envelopper des nombres dans une plage peut être utilisé pour normaliser des valeurs à une plage spécifique.

Vous pouvez utiliser l'opérateur modulo pour envelopper une valeur dans une plage en l'utilisant comme base pour une opération modulo.

Par exemple, dans une simulation, vous pourriez vouloir vous assurer que les angles sont toujours compris entre 0 et 360 degrés, même s'ils dépassent cette plage. Envelopper la valeur de l'angle dans la plage garantit qu'elle reste dans la plage souhaitée.

```js
let angle = 450;
let result = angle % 360;
console.log(result); // retourne 90
```

Dans cet exemple, l'angle de `450` degrés est enveloppé dans la plage de `0` à `360` degrés en utilisant l'opérateur modulo. Il retournera `90` qui se situe dans la plage.

## Conclusion

Dans cet article, vous avez appris à utiliser l'opérateur modulo et vu diverses façons dont il fonctionne.

Un opérateur modulo est un outil puissant pour diverses opérations mathématiques en JavaScript. Comprendre son utilisation et ses applications peut grandement simplifier votre code et le rendre plus efficace.

Vous pouvez accéder à plus de 185 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.