---
title: Trouver son chemin avec .map()
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-01-24T18:01:19.000Z'
originalURL: https://freecodecamp.org/news/finding-your-way-with-map-aecb8ca038f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1m6Z6xg7J2DDFOsK_-HgBw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Trouver son chemin avec .map()
seo_desc: The verbosity and elegance of a solution are driven by the tools we have
  to solve a particular problem. While the goal of problem-solving is to solve a problem,
  it’s methods should move towards the most elegant way possible. The journey towards
  such ...
---

La verbosité et l'élégance d'une solution sont déterminées par les outils dont nous disposons pour résoudre un problème particulier. Bien que l'objectif de la résolution de problèmes soit *de résoudre un problème*, ses méthodes doivent tendre vers la manière la plus élégante possible. Le chemin vers une telle solution semble cependant se situer sur une courbe asymptotique. La perfection se rapproche de plus en plus mais reste à jamais hors de portée.

#### Le Problème

Imaginez avoir un tableau et devoir modifier chaque élément de ce tableau. Peut-être, par exemple, prendre un tableau de tailles en pouces et devoir les convertir en centimètres. Ou peut-être convertir un tableau de températures en Celsius en Fahrenheit. Si vous êtes nouveau en programmation, votre esprit pourrait immédiatement penser à une forme de boucle. Et, devinez quoi ? Je suis sûr que vous pourriez faire en sorte que cela fonctionne.

Cependant, je suis ici pour vous donner un outil supplémentaire — quelque chose pour vous rapprocher un peu plus de l'élégance : `Array.prototype.map()`.

La méthode `map` nous permet de transformer chaque élément d'un tableau, sans affecter le tableau original. Elle est considérée comme une *fonction d'ordre supérieur* et une technique de programmation fonctionnelle car elle prend une fonction comme argument et nous effectuons un calcul sans muter l'état de notre application.

> `Map` est une propriété héritée du prototype de tableau. Les prototypes fournissent des méthodes intégrées que les objets possèdent (les tableaux sont des types spéciaux d'objets aux yeux de JavaScript). Bien que `map` puisse être un peu plus étranger, ce prototype n'est pas différent, par exemple, du prototype `Array.length`. Ce sont simplement des méthodes intégrées à JavaScript. Les prototypes de tableau peuvent être ajoutés et mutés par : `Array.prototype.<someMethodHere>` = ...

À la fin de cette leçon, nous découvrirons comment `map` fonctionne et nous écrirons notre propre méthode de prototype de tableau.

#### Alors, que fait .map() ?

Supposons que vous avez un tableau de températures en Celsius que vous souhaitez convertir en Fahrenheit.

Il existe plusieurs façons de résoudre ce problème. Une façon pourrait être d'écrire une boucle `for` pour créer un tableau de températures en Fahrenheit à partir des températures en Celsius données.

Avec la boucle `for`, nous pourrions écrire :

```js
const celciusTemps = [22, 36, 71, 54];
const getFahrenheitTemps = (function(temp) {
   const fahrenheitTemps = [];
   for (let i = 0; i < celciusTemps.length; i += 1) {
      temp = celciusTemps[i] * (9/5) + 32
      fahrenheitTemps.push(temp);
   }
   console.log(fahrenheitTemps); [71.6, 96.8, 159.8, 129.2
})();
```

Quelques points à noter :

1. Cela fonctionne.
   
2. Nous utilisons une Expression de Fonction Invocable Immédiatement (IIFE) pour éviter d'avoir également à appeler la fonction.
   
3. C'est un peu verbeux et pas très élégant.
   

`Map` nous permet de prendre le code ci-dessus et de le refactoriser comme suit :

```js
const fahrenheitTemps = celciusTemps.map(e => e * (9/5) + 32);
console.log(fahrenheitTemps); // [71.6, 96.8, 159.8, 129.2]
```

#### Alors, comment fonctionne map ?

`Map` prend une fonction et applique cette fonction à chaque élément du tableau. Nous pourrions écrire `map` un peu plus verbeux avec ES5 pour voir cela un peu plus clairement.

```js
const fahrenheitTemps = celciusTemps
   
   .map(function(elementOfArray) {
      return elementOfArray * (9/5) + 32;
   });
console.log(fahrenheitTemps); // [71.6, 96.8, 159.8, 129.2]
```

Si notre fonction map pouvait dire ce qu'elle fait, elle dirait :

« Pour chaque élément du tableau, je le multiplie par (9/5), puis j'ajoute 32. Lorsque cela est fait, je retourne le résultat comme un élément dans un nouveau tableau appelé fahrenheitTemps. »

Regardons un cas d'utilisation plus courant. Supposons que nous avons un tableau d'objets `people`. Chaque objet a une paire clé-valeur `name` et `age`. Nous voulons créer une variable qui contient simplement les noms de tout le monde dans le tableau. Avec notre méthode de boucle `for`, nous pourrions écrire :

```js
const people = [
   {name: "Steve", age: 32},
   {name: "Mary", age: 28},
   {name: "Bill", age: 41},
];
const getNames = (function(person) {
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // ["Steve", "Mary", "Bill"];
})();
```

Avec `map` :

```js
const names = people.map(e => e.name);
console.log(names) // ["Steve", "Mary", "Bill"];
```

Remarquez ici que nous ne transformons rien, nous retournons simplement la paire clé-valeur `name`.

Encore une fois, la boucle `for` fonctionne. Mais elle est verbeuse, et nous devons créer une nouvelle fonction personnalisée chaque fois que nous voulons faire une transformation différente. Une partie principale de la programmation est d'écrire du code DRY (Don't Repeat Yourself). Ces fonctions d'ordre supérieur comme map nous permettent de faire de la programmation plus complexe en moins de lignes de code que nous ne pourrions sans elles.

#### Réinventer la roue :

Pour mieux comprendre ce qui se passe sous le capot, nous allons créer notre propre fonction map que nous attacherons au prototype de tableau.

Tout d'abord, pour attacher une méthode de prototype à un Array, nous allons écrire :

`Array.prototype.<yourMethodHere>`

donc pour nous :

`Array.prototype.myMap = <our code>`

Mais, quel sera notre code ?

Nous avons déjà la logique dont nous avons besoin à partir des boucles `for` ci-dessus. Tout ce que nous avons à faire est de le refactoriser un peu. Refactorisons la dernière fonction que nous avons écrite `getNames()`.

Rappelons que cette fonction prenait une personne (en d'autres termes un élément de notre tableau), effectuait une transformation personnalisée sur cet élément (avec la boucle `for` et une certaine logique), et retournait un tableau de noms (ou un nouveau tableau).

```js
const getNames = (function(person) {
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // ["Steve", "Mary", "Bill"];
})();
```

Tout d'abord, changeons le nom de notre fonction. Après tout, cette nouvelle méthode ne suppose pas savoir quel type de tableau elle va traiter :

```js
const myMap = (function(person) { // Nom changé
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // ["Steve", "Mary", "Bill"];
})();
```

Deuxièmement, nous créons notre propre version de `.map()`. Nous savons que cela prendra une fonction que l'utilisateur fournit. Changeons le paramètre que notre fonction prend :

```js
// C'est un peu verbeux, mais un nom de paramètre très clair
const myMap = (function(userProvidedFunction) { 
   const names = [];
   for (let i = 0; i < people.length; i += 1) {
      name = people[i].name;
      names.push(name);
   }
   console.log(names); // ["Steve", "Mary", "Bill"];
})();
```

Enfin, nous n'avons aucune idée du tableau sur lequel cette méthode va agir. Nous ne pouvons donc pas nous référer à `people.length` mais nous *pouvons* nous référer à `this.length`. `this` retournera le tableau sur lequel la méthode agit. De plus, nettoyons certains des autres noms de variables :

```js
const myMap = (function(userProvidedFunction) { 
   // changer le nom de la variable
   const newArr = [];
   // utiliser "this.length"   
   for (let i = 0; i < this.length; i += 1) { 
   
      // utiliser "this[i]", et changer le nom de la variable      
      const newElement = this[i];
  
      // mettre à jour le tableau dans lequel nous poussons
      newArr.push(newElement); 
   }
   // Retourner le nouveau tableau créé
   return newArr; 
})();
```

Nous y sommes presque, mais il y a une chose que nous oublions. Nous n'avons pas transformé le tableau ! Tout ce que nous avons fait ci-dessus est de retourner l'ancien tableau. Nous devons appliquer la fonction fournie par l'utilisateur à chaque élément du tableau :

```js
const myMap = (function(userProvidedFunction) { 
   const newArr = [];
   for (let i = 0; i < this.length; i += 1) {
      
      /* Transformer l'élément en le passant dans la 
       * fonction fournie par l'utilisateur
       */
      const newElement = userProvidedFunction(this[i]); 
      
      newArr.push(newElement); 
   }
   return newArr;
})();
```

Enfin, nous pouvons attacher notre nouvelle fonction à `Array.prototype`.

`Array.prototype.myMap = myMap;`

Un dernier contrôle de cohérence :

```js
const myArray = [1, 2, 3];
// Multiplier chaque élément par 2
const myMappedArray = myArray.myMap(e => e * 2)
console.log(myMappedArray) // [2, 4, 6];
```

#### Résumé

`Map` est une méthode de prototype offerte par les tableaux. En coulisses, elle parcourt le tableau, appliquant une fonction fournie par l'utilisateur à chaque élément. En fin de compte, elle retourne un nouveau tableau avec les valeurs transformées. Elle fait cela sans muter le tableau original. Parce que le paramètre qu'elle prend est une fonction, elle est considérée comme une fonction d'ordre supérieur. De plus, son utilisation relève du paradigme de la programmation fonctionnelle.

Merci d'avoir lu !

woz