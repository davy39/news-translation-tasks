---
title: Définition Booléenne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-19T06:43:00.000Z'
originalURL: https://freecodecamp.org/news/boolean-definition
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605d74a79618b008528a7978.jpg
tags:
- name: Boolean
  slug: boolean
- name: Tech Terms
  slug: tech-terms
seo_title: Définition Booléenne
seo_desc: 'In computer science, a boolean refers to a value that is either true or
  false.

  Boolean gets its name from the English mathematician, George Boole.

  Boole created a new branch of algebra, now known as Boolean Algebra, where the value
  of true is 1 and t...'
---

En informatique, un booléen fait référence à une valeur qui est soit vraie soit fausse.

Le terme booléen tire son nom du mathématicien anglais, George Boole.

Boole a créé une nouvelle branche de l'algèbre, aujourd'hui connue sous le nom d'Algèbre de Boole, où la valeur vraie est 1 et la valeur fausse est 0. En algèbre de Boole, il existe trois opérations logiques principales : **ET**, **OU**, et **NON**.

L'algèbre de Boole a jeté les bases de l'ère de l'information et de l'informatique. Tous les ordinateurs fonctionnent selon les principes de base de l'algèbre de Boole, où 1, ou vrai, est allumé, et 0, ou faux, est éteint.

Pour cette raison, de nombreux langages de programmation incluent des types de données et des opérateurs booléens.

Par exemple, en JavaScript, il est courant de voir les types de données booléens `true` et `false` :

```js
const isCat = true;
```

JavaScript dispose également d'opérateurs logiques pour **ET** :

```js
const isCat = true;
const isCute = true;

if (isCat && isCute) { // isCat ET isCute sont tous deux vrais
  console.log("Il y a un chat mignon :D"); // affiche "Il y a un chat mignon :D" dans la console
}
```

**OU** :

```js
const isCat = true;
const isFluffy = false;

if (isCat || isFluffy) { // soit isCat, soit isFluffy, soit les deux sont vrais
  console.log("Il y a un animal qui pourrait être un chat, duveteux, ou les deux"); // affiche "Il y a un animal qui pourrait être un chat, duveteux, ou les deux" dans la console
}
```

Et **NON** :

```js
const isCat = true;
const isFluffy = false;

if (!isFluffy) { // isFluffy est faux, ou NON vrai
  console.log("Quel que soit cet animal, il n'est pas duveteux"); // affiche "Quel que soit cet animal, il n'est pas duveteux" dans la console
}
```

De plus, comme de nombreux autres langages de programmation, JavaScript dispose d'autres opérateurs qui retournent une valeur booléenne :

```js
const catName = 'Boomer';

if (catName === 'Boomer') { // évalue à vrai
  console.log('BOOMER VIT !'); // affiche 'BOOMER VIT !' dans la console
}
```

## Termes Techniques Associés :

* [Définition Binaire](https://www.freecodecamp.org/news/binary-definition/)
* [Définition Bit](https://www.freecodecamp.org/news/bit-definition/)