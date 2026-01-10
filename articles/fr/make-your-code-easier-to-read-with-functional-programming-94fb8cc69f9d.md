---
title: Rendez votre code plus facile à lire avec la programmation fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T10:15:52.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-easier-to-read-with-functional-programming-94fb8cc69f9d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uFGSHrjaQSpCC6_rTKT3Lg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Rendez votre code plus facile à lire avec la programmation fonctionnelle
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Pure functions are easier to read and understand. All the function’s dependencies
  are in its definition and are therefore...'
---

Par Cristian Salcescu

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Les fonctions pures sont plus faciles à lire et à comprendre. Toutes les dépendances de la fonction sont dans sa définition et sont donc plus faciles à voir. Les fonctions pures tendent également à être petites et à faire une seule chose. Elles n'utilisent pas `this`, une source constante de confusion.

### Chaînage

> **Le chaînage** est une technique utilisée pour simplifier le code où plusieurs méthodes sont appliquées à un objet les unes après les autres.

[Comparons](https://jsfiddle.net/cristi_salcescu/5va5dkq7/) les deux styles : impératif et fonctionnel. Dans le style fonctionnel, j'utilise la boîte à outils de base pour les opérations sur les listes `filter()` et `map()`. Ensuite, je les enchaîne.

J'ai pris le cas d'une collection de tâches. Une tâche a un `id`, une description (`desc`), un booléen `completed`, un `type` et un objet `user` assigné. L'objet utilisateur a une propriété `name`.

```
//Style impératif
let filteredTasks = [];
for(let i=0; i<tasks.length; i++){
    let task = tasks[i];
    if (task.type === "RE" && !task.completed) {
        filteredTasks.push({ ...task, userName: task.user.name });
    }
}

//Style fonctionnel
function isPriorityTask(task){
   return task.type === "RE" && !task.completed;
}

function toTaskView(task) {
   return { ...task, userName: task.user.name };
}

let filteredTasks = tasks.filter(isPriorityTask).map(toTaskView);
```

Remarquez les callbacks pour `filter()` et `map()` en tant que **fonctions pures avec des noms révélant l'intention.**

> `_map()_` transforme une liste de valeurs en une autre liste de valeurs en utilisant une fonction de mappage.

Voici un [test de performance](https://jsperf.com/make-code-easier-to-read-imperative-vs-functional) mesurant la différence entre les deux styles. Il semble que l'approche fonctionnelle soit 60 % plus lente. Lorsque le processus impératif se termine en 10 millisecondes, l'approche fonctionnelle se terminera en 16 millisecondes. [Dans ce cas](https://jsfiddle.net/cristi_salcescu/v5jegr61/), l'utilisation de la boucle impérative sera une optimisation prématurée.

### Style sans point

Dans l'exemple précédent, j'ai utilisé le style sans point lors de la composition de fonctions. Le style sans point est une technique qui améliore la lisibilité en éliminant les arguments inutiles. Considérez le code suivant :

```
tasks.filter(task => isPriorityTask(task)).map(task => toTaskView(task));
```

En style sans point, il est écrit sans arguments :

```
tasks.filter(isPriorityTask).map(toTaskView);
```

Pour plus d'informations sur le style sans point, consultez [Comment la composition sans point fera de vous un meilleur programmeur fonctionnel](https://medium.freecodecamp.org/how-point-free-composition-will-make-you-a-better-functional-programmer-33dcb910303a)

### Application partielle

Ensuite, je veux examiner comment nous pouvons améliorer la lisibilité et également réutiliser une fonction existante. Avant de faire cela, nous avons besoin d'une nouvelle fonction dans notre boîte à outils.

> **L'application partielle** fait référence au processus de fixation d'un certain nombre d'arguments à une fonction.

> C'est un moyen de passer de la généralisation à la spécialisation.

Pour l'application partielle, nous pouvons utiliser la fonction `partial()` d'une bibliothèque populaire comme [underscore.js](http://underscorejs.org/#partial) ou [lodash.js](https://lodash.com/docs/4.17.5#partial). La méthode `bind()` peut également faire de l'application partielle.

Supposons que nous voulons refactoriser [le code impératif suivant](https://jsfiddle.net/cristi_salcescu/9p0ffasn/) en un style fonctionnel, plus facile à lire :

```
let filteredTasks = [];
for(let i=0; i<tasks.length; i++){
    let task = tasks[i];
    if (task.type === "NC") {
        filteredTasks.push(task);
    }
}
```

Comme je l'ai dit, cette fois nous voulons créer une fonction générique qui peut être utilisée pour filtrer par n'importe quel type de tâche. `isTaskOfType()` est la fonction générique. La fonction `partial()` est utilisée pour créer une nouvelle fonction prédicat `isCreateNewContent()` qui filtre par un type spécifique.

> **Une fonction prédicat** est une fonction qui prend une valeur en entrée et retourne vrai/faux en fonction de si la valeur satisfait la condition.

```
function isTaskOfType(type, task){
  return task.type === type;
}

let isCreateNewContent = partial(isTaskOfType, "NC");
let filteredTasks = tasks.filter(isCreateNewContent);
```

Remarquez la fonction prédicat. Elle a un nom exprimant son intention. Lorsque je lis `tasks.filter(isCreateNewContent)`, je comprends clairement quel type de `tasks` je sélectionne.

> `filter()` sélectionne des valeurs dans une liste en fonction d'une fonction prédicat qui décide quelles valeurs doivent être conservées.

### Réduire

[Je vais commencer un nouvel exemple](https://jsfiddle.net/cristi_salcescu/zo9zkrcc/) en utilisant une liste de courses. Voici à quoi la liste peut ressembler :

```
let shoppingList = [
   { name : "orange", units : 2, price : 10, type : "FRT"},
   { name : "lemon", units : 1, price : 15, type : "FRT"},
   { name : "fish", units : 0.5, price : 30, type : "MET"}
];
```

Je vais calculer le prix total et le prix des fruits uniquement. Voici le style impératif :

```
let totalPrice = 0, fruitsPrice = 0;
for(let i=0; i<shoppingList.length; i++){
   let line = shoppingList[i];
   totalPrice += line.units * line.price;
   if (line.type === "FRT") {
       fruitsPrice += line.units * line.price;
   }
}
```

Prendre l'approche fonctionnelle dans ce cas nécessitera l'utilisation de `reduce()` pour calculer le prix total.

> `reduce()` réduit une liste de valeurs à une seule valeur.

Comme nous l'avons fait auparavant, nous créons de nouvelles fonctions pour les callbacks requis et leur donnons des noms révélant l'intention : `addPrice()` et `areFruits()`.

```
function addPrice(totalPrice, line){
   return totalPrice + (line.units * line.price);
}

function areFruits(line){
   return line.type === "FRT";
}

let totalPrice = shoppingList.reduce(addPrice,0);
let fruitsPrice = shoppingList.filter(areFruits).reduce(addPrice,0);
```

### Conclusion

Les fonctions pures sont plus faciles à lire et à comprendre.

La programmation fonctionnelle décomposera les opérations sur les listes en étapes comme : filter, map, reduce, sort. En même temps, elle nécessitera de définir de nouvelles petites fonctions pures pour soutenir ces opérations.

Combiner la programmation fonctionnelle avec la pratique de donner des noms révélant l'intention améliore grandement la lisibilité du code.

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour plus d'informations sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)