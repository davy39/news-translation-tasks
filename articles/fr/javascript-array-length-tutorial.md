---
title: "Longueur du tableau JavaScript \x13 Comment trouver la longueur d'un tableau\
  \ en JS"
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2024-02-01T15:56:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-length-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-venelin-dimitrov-3476312.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: "Longueur du tableau JavaScript \x13 Comment trouver la longueur d'un tableau\
  \ en JS"
seo_desc: 'JavaScript arrays are fundamental data structures that allow you to store
  and manipulate collections of elements efficiently.

  While working with arrays, you''ll often need to know their length. The length of
  an array tells us how many elements are pre...'
---

Les tableaux JavaScript sont des structures de données fondamentales qui permettent de stocker et de manipuler des collections d'éléments de manière efficace.

Lors de la manipulation de tableaux, vous aurez souvent besoin de connaître leur longueur. La longueur d'un tableau nous indique combien d'éléments sont présents dans le tableau. Vous pouvez utiliser cette information pour vérifier si un tableau est vide et, si ce n'est pas le cas, parcourir les éléments qu'il contient.

## Comment trouver la longueur d'un tableau

### Utilisation de la propriété `<.length>`

JavaScript possède une propriété `<.length>` qui retourne la taille d'un tableau sous forme de nombre (entier).

Voici un exemple de son utilisation :

```python
let numbers = [12,13,14,25]
let numberSize = numbers.length
console.log(numberSize)
# Sortie
# 4
```

Dans le code ci-dessus, une variable nommée `numbers` stocke un tableau de nombres, tandis que la variable `numberSize` stocke le nombre d'éléments présents dans le tableau en utilisant la méthode `.length`. La taille du nombre est ensuite affichée à l'aide de console.log  d'où la sortie 4.

Vérifions maintenant le type de données de la propriété `length` :

```python
let numbers = [12,13,14,25]
let numberSize = numbers.length
console.log(typeof numberSize)
# Sortie
# number
```

Dans le code ci-dessus, nous voyons que la sortie est `number`.

Voici un exemple de la façon d'accéder à un élément de tableau avec la propriété `length` dans une boucle for :

```python
let numbers = [12,13,14,25]
for (i = 0; i < numbers.length; i++){
   console.log(numbers[i]);
}
# Sortie
# 12
# 13
# 14
# 25
```

### Sans utiliser la méthode `.length()`

Dans cette méthode, nous allons parcourir les éléments et compter chacun des éléments présents dans le tableau.

Voici comment cela fonctionne :

```python
function arrayLength(arr) {
   let count = 0;
   for (const element of arr) {
     count++;
   }

   return count; 
}
let numbers = [12,13,14,25]
console.log("Longueur du tableau :", arrayLength(numbers));
# Sortie
# Longueur du tableau : 4
```

Dans le code ci-dessus, il y a une fonction nommée `arrayLength` qui accepte le tableau en entrée. Nous avons créé une variable appelée `count` qui est initialisée à 0. La variable `count` stockera le nombre d'éléments dans le tableau.

Pour compter les éléments dans le tableau, nous avons utilisé une [boucle for-of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) pour vérifier chaque élément dans le tableau.

Le code parcourt chaque élément du tableau jusqu'à ce qu'il rencontre undefined. C'est-à-dire que nous parcourons chaque élément du tableau jusqu'à ce que nous atteignions la fin du tableau où il n'y a plus d'éléments à vérifier. Enfin, nous retournons `count` comme sortie.

Nous passons la variable `<numbers>` en entrée de la fonction afin d'obtenir la longueur du tableau comme valeur retournée.

## Conclusion

La méthode la plus courante et la plus simple consiste à utiliser la propriété length du tableau. Mais vous pouvez également utiliser une méthode plus longue en parcourant le tableau. Ces méthodes vous permettent de travailler avec des tableaux de différentes tailles et types.

Si vous avez des questions, vous pouvez me contacter sur [Twitter](https://twitter.com/HeritageAlabi1) .