---
title: Tutoriel JavaScript Array.map() – Comment itérer à travers les éléments d'un
  tableau avec map()
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-19T16:16:57.000Z'
originalURL: https://freecodecamp.org/news/array-map-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/array-map.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript Array.map() – Comment itérer à travers les éléments
  d'un tableau avec map()
seo_desc: 'When ES6 (EmcaScript 2015) came out, it ushered in a whole new set of methods
  for iterating over an array. And one of the most useful is the map() method.

  Array.prototype.map() is a built-in array method for iterating through the elements
  inside an a...'
---

Lorsque ES6 (EmcaScript 2015) est sorti, il a introduit toute une nouvelle série de méthodes pour itérer sur un tableau. Et l'une des plus utiles est la méthode `map()`.

`Array.prototype.map()` est une méthode intégrée de tableau pour itérer à travers les éléments à l'intérieur d'une collection de tableau en JavaScript. Considérez la boucle comme un moyen de progresser d'un élément à un autre dans une liste, tout en maintenant l'ordre et la position de chaque élément.

Cette méthode [prend en entrée une fonction de rappel](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript/) qui est appelée pour chaque nouvel élément sur lequel elle itère.

La fonction de rappel prend en entrée trois paramètres :

* La valeur actuelle

* Son index

* Le tableau cible

Si vous êtes un débutant et que vous avez du mal à comprendre comment utiliser la méthode `map()` ou ce qu'elle fait exactement, alors cet article est pour vous.

Dans cet article, je vais expliquer la méthode `map()` et illustrer son fonctionnement avec quelques exemples simples.

## Comment la méthode map() fonctionne en JavaScript

Imaginez ceci : il y a une file de personnes à l'extérieur d'un hôpital attendant d'être vaccinées. Cela signifie qu'elles ne sont pas encore vaccinées.

Un par un, un médecin administre le vaccin à toutes ces personnes. Le médecin fait cela en itérant à travers la file. À une extrémité, il y a un groupe de personnes qui ne sont pas encore vaccinées. Le médecin a pris chacune d'entre elles, leur a administré le vaccin et les a retournées dans une **nouvelle** file de personnes vaccinées.

À une extrémité, il y a un tableau (A) sur lequel vous souhaitez opérer. `map()` prend tous les éléments de ce tableau (A), effectue une action cohérente sur chacun de ces éléments et les retourne dans un nouveau tableau (B).

## Comment utiliser la méthode map() – Exemple des Avengers

Pour illustrer comment `map()` fonctionne en JavaScript, considérons une liste de noms de certains de nos Avengers préférés. Le problème est que les noms de cette liste ne sont pas complets – ils manquent un suffixe important.

Avec `map()`, nous pouvons prendre tous les noms du tableau et ajouter le suffixe "man" à chacun d'entre eux :

```js
let firstNames = ["super", "spider", "ant", "iron"]
let lastName = "man";

let fullNames = firstNames.map(firstName => firstName + lastName);

console.log(fullNames);

// ["superman", "spiderman", "antman", "ironman"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map1-1.png align="left")

*CODE VISUEL*

### Et les femmes ?

Désolé, mon erreur. J'ai réalisé mon erreur et j'ai décidé d'inclure un personnage féminin à la **première** position dans le tableau. Chaque élément d'un tableau est identifié par une valeur unique, son **index** (ou position dans le tableau). Le premier élément aura un index de `0`, le deuxième un index de `1`, et ainsi de suite.

Puisqu'il y a maintenant une super-héroïne dans la liste, nous voudrons nous assurer d'ajouter le bon suffixe à la super-héroïne appropriée.

Puisque `map()` prend également en entrée l'index de l'élément que nous sommes en train d'itérer, nous pouvons faire cela en vérifiant l'index de notre héros et en nous assurant d'utiliser le suffixe "woman" pour le premier élément de notre tableau :

```js
let firstNames = ["wonder", "spider", "ant", "iron"]
let male = "man";
let female = "woman";

let fullNames = firstNames.map(function(firstName, index) {
    return (index == 0) ? firstName + female : firstName + male;
 });

console.log(fullNames);

["wonderwoman", "spiderman", "antman", "ironman"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--8.png align="left")

### Comment utiliser l'argument Index

En plus de la valeur sur laquelle on itère, map prend également en entrée sa position d'index. Cela est très utile si vous souhaitez effectuer différents types d'opérations en fonction de la position d'index de l'élément.

Dans l'exemple précédent, nous avons ajouté un suffixe différent en vérifiant l'index.

Pour connaître la position d'index de chacun de nos éléments dans le tableau, nous pouvons faire ceci :

```js
let fullNames = ["wonderwoman", "spiderman", "antman", "ironman"]

fullNames.map(function(firstName, index) {
    console.log(${firstName} est à la position ${index})
});

/*
"wonderwoman est à la position 0"
"spiderman est à la position 1"
"antman est à la position 2"
"ironman est à la position 3"
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--1.png align="left")

*RÉSULTAT*

### Comment multiplier tous les éléments du tableau par 2

Travaillons un peu avec des nombres maintenant. Dans cet exemple, nous voulons simplement multiplier chaque nombre dans le tableau cible par deux et ensuite retourner leurs produits dans un nouveau tableau :

```js
let numbers = [10, 20, 30, 40]
let multiplier = 2;

let products = numbers.map(number => number * multiplier);

console.log(products);

// [20, 40, 60, 80]
```

### Comment arrondir à l'entier le plus proche

Que faire si nous avons un tableau de décimales mais que nous voulons que chacun de ces nombres décimaux soit arrondi à l'entier le plus proche ?

```js
let numbers = [3.7, 4.9, 6.2]
let rounded = numbers.map(function(number) {
    return Math.round(number);
})

console.log(rounded);

// [4, 5, 6]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--2.png align="left")

### Comment convertir des chaînes en nombres

Nous avons une liste de nombres qui sont de type chaîne. Cependant, nous voulons convertir chacun en type nombre :

```js
let strings = ["10","20","30"]

let numbers = strings.map(function(string) {
    return Number(string);
})

console.log(numbers);

// [10, 20, 30]
```

### Comment obtenir les vrais noms des Avengers

Dans cet exemple, nous travaillons avec des objets. Nous avons cinq Avengers dans le tableau, et chacun a à la fois un vrai nom et un nom de héros. Cependant, nous voulons seulement récupérer leurs vrais noms dans le nouveau tableau.

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let realNames = avengers.map(avenger => avenger.name);

console.log(realNames);

// ["steve rogers", "tony stark", "bruce banner", "peter parker", "tchalla"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--5-1.png align="left")

### Comment obtenir les noms de héros des Avengers

Pour obtenir uniquement leurs noms de héros, nous faisons presque la même chose, sauf que dans ce cas, nous accédons à la propriété `heroName` :

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let heroNames = avengers.map(avenger => avenger.heroName);

console.log(heroNames);

// ["captain america", "iron man", "the hulk", "spiderman", "black panther"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/map--10.png align="left")

### Comment séparer une fonction

Au lieu de définir une fonction directement à l'intérieur de `map()`, nous pouvons définir la fonction à l'extérieur et ensuite l'appeler à l'intérieur de notre fonction `map()` :

```js
let avengers = [
    {name: "steve rogers", heroName: "captain america"},
    {name: "tony stark", heroName: "iron man"},
    {name: "bruce banner", heroName: "the hulk"},
    {name: "peter parker", heroName: "spiderman"},
    {name: "tchalla", heroName: "black panther"}
]

let getName = avenger => avenger.name;

let realNames = avengers.map(getName);

console.log(realNames);

// ["steve rogers", "tony stark", "bruce banner", "peter parker", "tchalla"]
```

### Comment fonctionne l'argument Array

Plus tôt, j'ai mentionné que lors de chaque itération, la méthode `map()` prend en entrée la valeur sur laquelle on itère et également sa position d'index. Il y a un autre argument à ajouter à ces deux-là, l'argument `Array`.

L'argument `arr` représente le tableau cible sur lequel on itère, ainsi que son contenu entier. Avec cet argument, vous pouvez essentiellement regarder dans le tableau complet pour trouver quelque chose.

Dans cet exemple, nous allons accéder au paramètre `arr` pour regarder et vérifier si l'élément actuel est le dernier élément de la liste. S'il ne l'est pas, nous accédons à l'élément suivant et le soustrayons de l'élément actuel. S'il est le dernier, nous le retournons simplement.

```js
const oldArray = [33, 20, 10, 5];
const newArray = oldArray.map((currentVal, index, arr) => {
    let nextItem = index + 1 < arr.length ? arr[index + 1] : 0
    return currentVal - nextItem;
	});


console.log(newArray);

// [13, 10, 5, 5]
```

## Conclusion

La méthode `map()` a été introduite dans ES6. Avec cette méthode, nous pouvons accéder et effectuer une action cohérente sur chaque élément à l'intérieur d'une collection de tableau.

Elle prend en entrée une fonction de rappel qu'elle appelle pour chaque nouvel élément sur lequel elle itère.

Dans ce tutoriel, j'ai introduit la méthode map(), illustré son fonctionnement avec une analogie et donné quelques exemples pratiques de son utilisation dans le code JavaScript.

J'espère que vous avez tiré quelque chose d'utile de cet article. Si vous aimez les tutoriels liés à la programmation comme celui-ci, vous devriez [consulter mon blog](https://ubahthebuilder.tech). J'y publie régulièrement des articles sur le développement logiciel.

Merci d'avoir lu et à bientôt.

**P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).