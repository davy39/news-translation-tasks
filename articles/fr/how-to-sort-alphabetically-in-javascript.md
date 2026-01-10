---
title: Trier par ordre alphabétique en JavaScript – Comment trier par nom en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-29T19:59:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-alphabetically-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--4-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Trier par ordre alphabétique en JavaScript – Comment trier par nom en JS
seo_desc: 'Sometimes you might have an array of words where you want to sort each
  word alphabetically (from a-z). Or you might have an array of objects containing
  user information including names, for example, where you want to sort the users
  by their names.

  We...'
---

Parfois, vous pouvez avoir un tableau de mots que vous souhaitez trier chacun par ordre alphabétique (de a à z). Ou vous pouvez avoir un tableau d'objets contenant des informations utilisateur, y compris des noms, par exemple, où vous souhaitez trier les utilisateurs par leurs noms.

Nous pouvons faire cela en JavaScript en utilisant la méthode `sort()` directement ou avec la fonction de comparaison.

Au cas où vous seriez pressé, voici les deux méthodes :

```js
// trier un tableau de noms
names.sort();

// trier un tableau d'objets avec un nom
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});
```

Apprenons maintenant comment nous sommes arrivés à ces deux solutions.

## Comment trier un tableau de noms par ordre alphabétique

Supposons que nous avons un tableau de noms :

```js
let names  = ["John Doe", "Alex Doe", "Peter Doe", "Elon Doe"];
```

Nous pouvons trier ces noms par ordre alphabétique en utilisant la méthode `sort()` :

```js
let sortedNames = names.sort();
console.log(sortedNames);
```

Cela retournera un tableau de noms triés par ordre alphabétique :

```bash
["Alex Doe","Elon Doe","John Doe","Peter Doe"]
```

**Note :** Dans une situation où certains noms commencent par une majuscule tandis que d'autres commencent par une minuscule, le résultat sera incorrect car la méthode `sort()` place les lettres majuscules avant les minuscules :

```js
let names = ["John Doe", "alex Doe", "peter Doe", "Elon Doe"];
let sortedNames = names.sort();

console.log(sortedNames); // ["Elon Doe","John Doe","alex Doe","peter Doe"]
```

Vous devrez donc vous assurer que les mots sont tous dans le même cas, sinon cela ne retournera pas les noms par ordre alphabétique comme nous le souhaitons.

## Comment trier par nom par ordre alphabétique en JavaScript

Dans un scénario réel, nous pourrions avoir un tableau d'utilisateurs avec les informations de chaque utilisateur dans un objet. Ces informations pourraient être n'importe quoi en plus du nom de l'utilisateur. Par exemple :

```js
let users = [
  {
    name: "John Doe",
    age: 17
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "Alex Doe",
    age: 14
  }
];
```

En regardant l'objet ci-dessus, la méthode précédente dans laquelle nous avons simplement appliqué la méthode `sort()` sur le tableau directement ne fonctionnera pas. Au lieu de cela, elle retournera le même tableau mais les éléments ne seront pas dans l'ordre que nous voulons.

Nous utiliserons la méthode `sort()` ainsi que la fonction de comparaison pour trier ce tableau d'utilisateurs par nom.

Nous utiliserons la fonction de comparaison pour définir un ordre de tri alternatif. Elle retourne une valeur négative, nulle ou positive, selon les arguments :

Syntaxe :

```js
function(a, b){return a - b}
```

Lorsque nous passons cette fonction de comparaison dans la méthode `sort()`, elle compare chaque valeur en fonction de la condition que nous avons définie, puis trie chaque nom selon la valeur retournée (négative, nulle, positive).

* Si le résultat est négatif, `a` est trié avant `b`.
  
* Si le résultat est positif, `b` est trié avant `a`.
  
* Si le résultat est `0`, aucun changement n'est apporté à l'ordre de tri des deux valeurs.
  

En utilisant l'exemple ci-dessus, nous pouvons maintenant utiliser la méthode `sort()` ainsi que la fonction de comparaison de cette manière :

```js
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});

console.log(users);
```

Le code ci-dessus compare chaque nom. S'il est plus grand, il retourne 1. S'il est plus petit, il retourne -1. Sinon, il retourne 0. La valeur retournée est utilisée pour trier les valeurs de notre tableau par ordre alphabétique :

```bash
[
  {
    name: "Alex Doe",
    age: 14
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  }
]
```

**Note :** Comme nous l'avons vu précédemment, cela fonctionne toujours selon la casse des lettres et triera les lettres majuscules avant les minuscules :

```js
let users = [
  {
    name: "alex Doe",
    age: 14
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  }
];
    
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});

console.log(users);
```

Sortie :

```bash
[
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  },
  {
    name: "alex Doe",
    age: 14
  }
]
```

## Conclusion

Dans cet article, vous avez appris comment trier un tableau par ordre alphabétique en utilisant la méthode `sort()` dans deux situations possibles.

Dans une situation où les noms ont des cas de lettres différents, il est préférable de les convertir d'abord dans un cas de lettre spécifique avant d'utiliser la méthode `sort()`.

Bon codage !