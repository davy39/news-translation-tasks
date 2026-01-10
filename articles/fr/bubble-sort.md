---
title: Le Tri Bulle Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T17:24:00.000Z'
originalURL: https://freecodecamp.org/news/bubble-sort
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8f740569d1a4ca3864.jpg
tags:
- name: algorithms
  slug: algorithms
- name: bubble
  slug: bubble
seo_title: Le Tri Bulle Expliqué
seo_desc: Just like the way bubbles rise from the bottom of a glass, bubble sort is
  a simple algorithm that sorts a list, allowing either lower or higher values to
  bubble up to the top. The algorithm traverses a list and compares adjacent values,
  swapping them...
---

Tout comme les bulles qui remontent du fond d'un verre, le **tri bulle** est un algorithme simple qui trie une liste, permettant aux valeurs les plus basses ou les plus hautes de remonter à la surface. L'algorithme parcourt une liste et compare les valeurs adjacentes, les échangeant si elles ne sont pas dans le bon ordre.

Avec une complexité dans le pire des cas de O(n^2), le tri bulle est très lent comparé à d'autres algorithmes de tri comme le tri rapide. L'avantage est qu'il est l'un des algorithmes de tri les plus faciles à comprendre et à coder à partir de zéro.

### **Exemple :**

```js
let arr = [4, 2, 6, 3, 9];
let sorted = false

while(!sorted) {
  sorted = true
  for(var i = 0; i < arr.length; i++) {
    if(arr[i] < arr[i - 1]) {
      let temp = arr[i];
      arr[i] = arr[i - 1];
      arr[i - 1] = temp;
      sorted = false;
    }
  }
}
```

### Premier passage à travers la liste :

* En commençant par `[4, 2, 6, 3, 9]`, l'algorithme compare les deux premiers éléments du tableau, 4 et 2. Il les échange car 2 < 4 : `[2, 4, 6, 3, 9]`
* Il compare les deux valeurs suivantes, 4 et 6. Comme 4 < 6, elles sont déjà dans l'ordre, et l'algorithme continue : `[2, 4, 6, 3, 9]`
* Les deux valeurs suivantes sont également échangées car 3 < 6 : `[2, 4, 3, 6, 9]`
* Les deux dernières valeurs, 6 et 9, sont déjà dans l'ordre, donc l'algorithme ne les échange pas.

### Deuxième passage à travers la liste :

* 2 < 4, donc il n'est pas nécessaire d'échanger les positions : `[2, 4, 3, 6, 9]`
* L'algorithme échange les deux valeurs suivantes car 3 < 4 : `[2, 3, 4, 6, 9]`
* Pas d'échange car 4 < 6 : `[2, 3, 4, 6, 9]`
* Encore une fois, 6 < 9, donc aucun échange ne se produit : `[2, 3, 4, 6, 9]`

La liste est déjà triée, mais l'algorithme de tri bulle ne le réalise pas. En fait, il doit effectuer un passage complet à travers la liste sans échanger aucune valeur pour savoir que la liste est triée.

#### **Troisième passage à travers la liste :**

* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`

Il est clair que le tri bulle est loin d'être l'algorithme de tri le plus efficace. Néanmoins, il est simple à comprendre et à implémenter soi-même.

Maintenant, allez-vous verser une boisson froide et pétillante – vous le méritez.