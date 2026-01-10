---
title: Comment utiliser les objets Map et Set en JavaScript – Expliqué avec des exemples
  de code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-02-21T21:39:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-and-set-objects-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/javascript-mat-and-set-objects-introduction.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les objets Map et Set en JavaScript – Expliqué avec des
  exemples de code
seo_desc: "Map and Set are two JavaScript data structures you can use to store a collection\
  \ of values, similar to Objects and Arrays. They are specialized data structures\
  \ that can help you store and manipulate related values. \nIn this tutorial, we\
  \ will see how ..."
---

Map et Set sont deux structures de données JavaScript que vous pouvez utiliser pour stocker une collection de valeurs, similaires aux Objets et aux Tableaux. Ce sont des structures de données spécialisées qui peuvent vous aider à stocker et manipuler des valeurs liées. 

Dans ce tutoriel, nous verrons comment Map et Set fonctionnent en détail et quand les utiliser. Nous explorerons également les méthodes de composition de l'objet Set qui ont été récemment ajoutées à la norme JavaScript.

## Table des matières

<ul>
  <li><a href="#objet-map-explique">L'objet Map expliqué</a></li>
  <ul>
    <li><a href="#comment-creer-un-objet-map">Comment créer un objet Map</a></li>
    <li>
      <a href="#methodes-et-proprietes-de-lobjet-map"
        >Méthodes et propriétés de l'objet Map</a
      >
    </li>
    <li>
      <a href="#autres-facons-de-creer-un-objet-map"
        >Autres façons de créer un objet Map</a
      >
    </li>
    <li>
      <a href="#iterer-sur-les-donnees-dun-objet-map">Itérer sur les données d'un objet Map</a>
    </li>
    <li>
      <a href="#quand-utiliser-lobjet-map">Quand utiliser l'objet Map</a>
    </li>
  </ul>
  <li><a href="#objet-set-explique">L'objet Set expliqué</a></li>
  <ul>
    <li>
      <a href="#comment-creer-un-objet-set">Comment créer un objet Set</a>
    </li>
    <li>
      <a href="#methodes-et-proprietes-de-lobjet-set"
        >Méthodes et propriétés de l'objet Set</a
      >
    </li>
    <li><a href="#methodes-de-composition-de-set">Méthodes de composition de Set</a></li>
    <li><a href="#iterer-sur-un-objet-set">Itérer sur un objet Set</a></li>
    <li>
      <a href="#quand-utiliser-lobjet-set">Quand utiliser l'objet Set</a>
    </li>
  </ul>
  <li><a href="#conclusion">Conclusion</a></li>
</ul>


## L'objet Map expliqué

L'objet `Map` stocke les données dans une structure de paires clé/valeur, tout comme un Objet. Les principales différences entre un objet régulier et une `Map` sont :

* Une `Map` peut avoir n'importe quel type de données comme valeur de clé
* Une `Map` maintient l'ordre des données ajoutées à l'objet

### Comment créer un objet Map

Pour créer un objet `Map`, vous pouvez appeler le constructeur `Map()` comme suit :

```js
const myMap = new Map();
```

Le code ci-dessus crée un nouvel objet `Map` vide.

### Méthodes et propriétés de l'objet Map

Un objet `Map` possède les méthodes et propriétés suivantes :

* `set(clé, valeur)` – Ajoute une paire clé/valeur à une Map
* `get(clé)` – Récupère une valeur d'une Map (retourne `undefined` si la clé n'existe pas)
* `has(clé)` – Vérifie si une Map possède une clé spécifique
* `delete(clé)` – Supprime une clé spécifique d'une Map
* `clear()` – Supprime tous les éléments d'une Map
* `keys()` – Retourne toutes les clés d'une Map
* `values()` – Retourne toutes les valeurs d'une Map
* `entries()` – Retourne toutes les clés et valeurs d'une Map
* `size` – Retourne le nombre d'éléments dans Map

Pour insérer des données dans l'objet `Map`, vous pouvez utiliser la méthode `set()` :

```js
const myMap = new Map();

myMap.set(1, 'Jack');
myMap.set(2, 'Jill');
myMap.set('animal', 'Elephant');
```

Le code ci-dessus crée un objet `Map` avec 3 entrées comme suit :

```txt
Map(3)
0: {1 => "Jack"}
1: {2 => "Jill"}
2: {"animal" => "Elephant"}
```

Pour récupérer une valeur de l'objet `Map`, vous devez utiliser la méthode `get()` et passer la clé comme argument :

```js
console.log(myMap.get(1)); // Jack

console.log(myMap.get('animal')); // Elephant


```

Pour voir combien de paires clé/valeur une `Map` contient, vous pouvez accéder à la propriété `size` :

```js
myMap.size; // 3
```

Pour voir si une certaine clé existe dans un objet `Map`, vous pouvez utiliser la méthode `has()`. Voir l'exemple ci-dessous :

```js
myMap.has(1); // true

myMap.has(10); // false
```

Pour supprimer une paire clé/valeur d'un objet `Map`, vous pouvez utiliser la méthode `delete()` et passer la clé de la paire que vous souhaitez supprimer comme suit :

```js
myMap.delete(1);

console.log(myMap);
// 0: {2 => "Jill"}
// 1: {"animal" => "Elephant"}
```

Si vous souhaitez supprimer toutes les paires clé/valeur, vous pouvez utiliser la méthode `clear()` à la place :

```js
myMap.clear();

console.log(myMap); // Map(0) {size: 0}
```

### Autres façons de créer un objet Map

Vous pouvez également créer un objet `Map` à partir d'un tableau comme suit :

```js
const myMap = new Map([
  [1, 'Jack'],
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);
```

Lors de la création d'une `Map` à partir d'un tableau, vous devez créer un tableau à deux dimensions et spécifier deux éléments dans chaque tableau. 

Le premier élément sera la clé, le deuxième élément sera la valeur. Toute valeur supplémentaire dans le tableau sera ignorée.

Dans l'exemple ci-dessous, la valeur 'Johnson' du premier tableau sera ignorée par le constructeur `Map()` :

```js
const myMap = new Map([
  [1, 'Jack', 'Johnson'], // la valeur 'Johnson' est ignorée
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);
```

Parce que vous pouvez créer un objet `Map` à partir d'un tableau, vous pouvez également en créer un à partir d'un objet. Vous devez d'abord transformer l'objet en tableau en utilisant la méthode `Object.entries()`.

L'exemple suivant montre comment utiliser un objet pour créer une `Map` :

```js
const person = {
    'name': 'Jack',
    'age': 20,
}

const myMap = new Map(Object.entries(person));

console.log(myMap); // Map(2) { 'name' => 'Jack', 'age' => 20 }
```

### Itérer sur les données d'un objet Map

Pour itérer sur les données d'un objet `Map`, vous pouvez utiliser soit la méthode `forEach()`, soit la boucle `for .. of` :

```js
const myMap = new Map([
  [1, 'Jack'],
  [2, 'Jill'],
  ['animal', 'Elephant'],
]);

// itérer en utilisant la méthode forEach()
myMap.forEach((value, key) => {
  console.log(`${key}: ${value}`);
});

// ou en utilisant la boucle for .. of

for (const [key, value] of myMap) {
  console.log(`${key}: ${value}`);
}
```

Les deux méthodes donnent la même sortie :

```txt
1: Jack
2: Jill
animal: Elephant
```

### Quand utiliser l'objet Map

Vous pouvez considérer l'objet `Map` comme une version améliorée de l'objet régulier. Il peut utiliser n'importe quel type de données comme valeur de clé, tandis qu'un objet ne peut utiliser que des valeurs de chaîne comme clés.

Sous le capot, l'objet `Map` performe mieux lorsque vous devez ajouter et supprimer des clés, vous pourriez donc envisager de l'utiliser lorsque vos données changent fréquemment.

De plus, l'objet Map possède de nombreuses méthodes utiles pour la manipulation de données, telles que `has()` pour voir si la Map contient une clé spécifique, `keys()` pour obtenir toutes les clés définies dans la `Map`, `values` pour obtenir toutes les valeurs, et `entries()` pour obtenir toutes les paires clé/valeur.

Mais si vous souhaitez simplement créer un objet sans manipulation supplémentaire, alors vous n'avez pas besoin d'utiliser l'objet `Map`. 

Un exemple est lorsque vous envoyez une requête réseau en utilisant la méthode `fetch()`. Vous créeriez un objet et le convertiriez en une chaîne JSON, donc l'utilisation d'un objet `Map` ne donnerait aucun avantage.

## L'objet Set expliqué

L'objet `Set` vous permet de stocker une collection d'éléments, tout comme un tableau. Les différences entre un `Set` et un tableau sont :

* Un `Set` nécessite que tous les éléments soient uniques
* Un `Set` a moins de méthodes pour la manipulation de données

### Comment créer un objet Set

Pour créer un nouvel objet `Set`, vous devez appeler le constructeur `Set()` comme suit :

```js
const mySet = new Set();
```

Le code ci-dessus créera un nouvel ensemble vide.

### Méthodes et propriétés de l'objet Set 

Un objet `Set` possède les méthodes et propriétés suivantes :

* `add(valeur)` – Ajoute une valeur à un Set
* `has(valeur)` – Vérifie si un Set contient une valeur spécifique
* `delete(valeur)` – Supprime une valeur spécifique d'un Set
* `clear()` – Supprime tous les éléments d'un Set
* `keys()` – Retourne toutes les valeurs d'un Set
* `values()` – Retourne toutes les valeurs d'un Set
* `entries()` – Retourne toutes les valeurs d'un Set sous forme de tableau `[valeur, valeur]`
* `size` – Retourne le nombre d'éléments dans Set

Notez que les méthodes `keys()` et `values()` dans un objet Set retournent la même sortie.

Il y a aussi la méthode `entries()` qui retourne un tableau comme suit :

```js
const mySet = new Set(['Jack', 'Jill', 'John']);

console.log(mySet.entries());
```

Sortie :

```txt
[Set Entries] {
  [ 'Jack', 'Jack' ],
  [ 'Jill', 'Jill' ],
  [ 'John', 'John' ]
}
```

Remarquez comment les valeurs sont répétées une fois dans chaque tableau ci-dessus. La méthode `entries()` est créée pour rendre `Set` similaire à l'objet `Map`, mais vous n'en aurez probablement pas besoin.

Il existe des méthodes supplémentaires que vous pouvez utiliser pour interagir avec un autre objet `Set`. Nous les discuterons dans la section suivante.

Pour ajouter un élément à l'objet Set, vous pouvez utiliser la méthode add :

```js
const mySet = new Set();

mySet.add(1);
mySet.add(2);
mySet.add(3);

console.log(mySet); // [1, 2, 3]
```

Pour obtenir toutes les valeurs stockées dans un `Set`, appelez la méthode `values()` :

```js
mySet.values(); // [Set Iterator] { 'Jack', 'Jill', 'John' }
```

Pour vérifier si le `Set` contient une valeur spécifique, utilisez la méthode `has()` :

```js
mySet.has('Jack'); // true

mySet.has('Michael'); // false
```

Pour supprimer une seule valeur, appelez la méthode `delete()`. Pour supprimer toutes les valeurs, utilisez la méthode `clear()` :

```js
mySet.delete('Jill');

mySet.clear();
```

### Méthodes de composition de Set

Outre les méthodes régulières ci-dessus, `Set` dispose également de méthodes de composition que vous pouvez utiliser pour effectuer diverses opérations de théorie des ensembles telles que la différence, l'union et l'intersection.

Le tableau suivant provient de la [documentation MDN Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set_composition) :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/set-composition-methods.png)
_Une liste des méthodes de composition de Set_

Par exemple, vous pouvez obtenir un ensemble contenant les différences entre deux autres ensembles comme suit :

```js
const setA = new Set([1, 2, 3, 4, 5]);

const setB = new Set([4, 5, 6, 7, 8]);

const diffsA = setA.difference(setB); // Set(3) {1, 2, 3}
const diffsB = setB.difference(setA); // Set(3) {6, 7, 8}

```

Ici, `setA.difference(setB)` retourne un `Set` contenant les valeurs uniques à l'objet `setA`.

Les valeurs opposées sont retournées lorsque vous exécutez la méthode `setB.difference(setA)`.

Notez que ces méthodes sont de nouvelles additions à la norme JavaScript, et à l'heure actuelle, seul Safari 17 et Chrome 122 supportent ces méthodes.

Très probablement, ces méthodes seront incluses dans Node.js bientôt.

### Itérer sur un objet Set

Pour itérer sur un objet `Set`, vous pouvez utiliser soit la méthode `forEach()`, soit la boucle `for .. of` :

```js
const mySet = new Set(['Jack', 'Jill', 'John']);

// itérer en utilisant la méthode forEach()
mySet.forEach(value => {
  console.log(value);
});

// ou en utilisant la boucle for .. of

for (const value of mySet) {
  console.log(value);
}
```

Sortie :

```txt
Jack
Jill
John
```

### Quand utiliser l'objet Set

Vous pouvez considérer l'objet `Set` comme la version alternative du tableau régulier.

Parce qu'un objet `Set` ignore les valeurs en double, vous pouvez utiliser cet objet pour purger les doublons d'un tableau, puis transformer l'objet `Set` en tableau :

```js
const myArray = [1, 1, 2, 2, 3, 3];

const uniqueArray = [...new Set(myArray)];

console.log(uniqueArray); // [ 1, 2, 3 ]
```

Une autre raison pour laquelle vous pourriez vouloir utiliser un `Set` est lorsque vous devez composer plusieurs objets set en utilisant les méthodes de composition, telles que `union()` et `difference()`. Ces méthodes ne sont pas disponibles dans un tableau.

## Conclusion

Dans cet article, vous avez appris comment les objets Map et Set fonctionnent et quand les utiliser dans votre code.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://codewithnathan.com/beginning-modern-javascript).

[![](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À plus tard !