---
title: JavaScript Ajouter à un Tableau – JS Append
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-14T18:29:54.000Z'
originalURL: https://freecodecamp.org/news/javascript-add-to-an-array-js-append
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/kelly-sikkema--1_RZL8BGBM-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: JavaScript Ajouter à un Tableau – JS Append
seo_desc: "You can use arrays in JavaScript to store a group of variables, often referred\
  \ to as elements or items of the array. Each of these elements will have an index\
  \ number assigned to them starting from zero. \nBy default, you can use the index\
  \ of an elemen..."
---

Vous pouvez utiliser des tableaux en JavaScript pour stocker un groupe de variables, souvent appelées éléments ou items du tableau. Chacun de ces éléments aura un numéro d'index qui lui est attribué, commençant à zéro. 

Par défaut, vous pouvez utiliser l'index d'un élément dans un tableau pour accéder ou modifier sa valeur.

Mais JavaScript fournit différentes méthodes que vous pouvez utiliser pour ajouter/ajouter plus d'éléments à un tableau. 

## Comment ajouter un élément à un tableau en JavaScript en utilisant la méthode `push`

La méthode `push` prend en paramètre(s) l'élément ou les éléments à ajouter au tableau. 

Voici un exemple :

```javascript
let myArr = [2, 4, 6];

myArr.push(8);

console.log(myArr);
// [ 2, 4, 6, 8 ]

```

Dans le code ci-dessus, le tableau `myArr` avait 3 éléments à l'initialisation — [2, 4, 6]. 

En utilisant la méthode `push`, nous avons ajouté 8 au tableau : `myArr.push(8)`. 

Vous pouvez ajouter plus d'un élément lorsque vous utilisez la méthode `push` en passant les éléments comme paramètres séparés par des virgules. Voici un exemple :

```javascript
let myArr = [2, 4, 6];

myArr.push(8, 10, 12);

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12 ]

```

## Comment ajouter un élément à un tableau en JavaScript en utilisant la méthode `splice`

Vous pouvez utiliser la méthode `splice` pour ajouter de nouveaux éléments, supprimer des éléments et remplacer des éléments existants dans un tableau. 

Voici à quoi ressemble la syntaxe :

```txt
splice(index, deleteNum, item1, ..., itemN)
```

Examinons la signification de chaque paramètre ci-dessus :

`index` désigne l'index de départ où la méthode `splice` commencera son opération.

`deleteNum` désigne le nombre d'éléments à supprimer à partir de `index`. 

`item1` désigne la valeur de l'élément à insérer à `index`. 

Si les explications ci-dessus semblent confuses, les exemples suivants devraient vous aider à mieux comprendre. 

Voici le premier exemple, montrant comment vous pouvez ajouter un élément à un tableau en utilisant la méthode `splice` :

```javascript
let myArr = [2, 4, 6];

myArr.splice(3,0,8)

console.log(myArr);
// [ 2, 4, 6, 8 ]
```

Décomposons le code ci-dessus dans sa forme la plus simple. Commençons par les index — le tableau avait trois éléments initialement :

2 => index 0  
4 => index 1  
6 => index 2

Nous avons passé trois paramètres à la méthode `splice` : `splice(3,0,8)`. 

Le premier paramètre — 3 — désigne l'index de départ pour la méthode `splice`. L'index 3 dans notre tableau vient immédiatement après le dernier élément. 

Le deuxième paramètre — 0 — désigne le nombre d'éléments à supprimer à partir de l'index 3 (l'index spécifié ci-dessus).

Le troisième paramètre — 8 — désigne la valeur à insérer à l'index spécifié. Donc 8 est inséré à l'index 3. Lorsque nous l'avons enregistré dans la console, nous avons obtenu ceci : `[ 2, 4, 6, 8 ]`

Si vous comprenez comment fonctionne la méthode `splice`, vous pouvez probablement passer à la section suivante. Sinon, l'exemple suivant simplifiera davantage.

```javascript
let myArr = [2, 4, 6, 8, 10, 12, 14];

myArr.splice(3,2,16)

console.log(myArr);
// [ 2, 4, 6, 16, 12, 14 ]
```

Décomposons-le comme nous l'avons fait dans le dernier exemple : 

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5  
14 => index 6

La méthode `splice` avait trois paramètres : `splice(3,2,16)`. 

Le premier paramètre est 3. Cela signifie que nous commençons à l'index trois qui a une valeur de 8. 

Le deuxième paramètre est 2 qui désigne combien d'éléments doivent être supprimés à partir de l'index 3. 

Le troisième paramètre est 16 qui est la valeur à insérer à l'index 3. 

Si vous regardez la sortie, vous remarquerez que 16 occupe maintenant l'index 3 tandis que les deux éléments du tableau initial (8 et 10) ont été supprimés : `[ 2, 4, 6, 16, 12, 14 ]`. 

Donc le tableau est passé de :

Tableau initial = [2, 4, 6, 8, 10, 12, 14]. 

À la suppression de deux éléments à partir de l'index 3 = [ 2, 4, 6, 12, 14 ]. 

À l'ajout de 16 à l'index 3 = [ 2, 4, 6, 16, 12, 14 ]. 

## Comment ajouter un élément à un tableau en JavaScript en utilisant la méthode `concat`

Vous pouvez fusionner ou concaténer deux ou plusieurs tableaux en utilisant la méthode `concat`. Voici un exemple :

```javascript
let myArr1 = [2, 4, 6, 8];
let myArr2 = [10, 12, 14]

myArr = myArr1.concat(myArr2)

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12, 14 ]


```

Le code ci-dessus est assez simple. Nous avons créé deux tableaux différents — `myArr1` et `myArr2`. 

Nous avons ensuite fusionné les deux en un seul tableau, stocké dans la variable `myArr` : `myArr1.concat(myArr2)`.

## Comment ajouter un élément à un tableau en JavaScript en utilisant la syntaxe de décomposition (`...`)

Vous pouvez également utiliser la syntaxe de décomposition ES6 (`...`) pour fusionner des tableaux comme nous l'avons fait dans la dernière section.

```javascript
let myArr1 = [2, 4, 6, 8];
let myArr2 = [10, 12, 14]

myArr = [ ...myArr1, ...myArr2]

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12, 14 ]


```

La syntaxe de décomposition, telle qu'utilisée ci-dessus, copie toutes les valeurs des deux tableaux dans le tableau `myArr` : `myArr = [ ...myArr1, ...myArr2]`.

## Résumé

Dans cet article, nous avons parlé des différentes méthodes que vous pouvez utiliser pour ajouter et ajouter des éléments à un tableau JavaScript. 

Nous avons donné des exemples en utilisant les méthodes `push`, `splice` et `concat` ainsi que la syntaxe de décomposition ES6 (`...`). 

Bon codage !