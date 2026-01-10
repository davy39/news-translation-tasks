---
title: Tutoriel JavaScript Array.filter() – Comment parcourir les éléments d'un tableau
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-26T16:07:48.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/filter-cover.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Tutoriel JavaScript Array.filter() – Comment parcourir les éléments d'un
  tableau
seo_desc: 'The Array.filter() method is arguably the most important and widely used
  method for iterating over an array in JavaScript.

  The way the filter() method works is very simple. It entails filtering out one or
  more items (a subset) from a larger collectio...'
---

La méthode `Array.filter()` est sans doute la méthode la plus importante et la plus largement utilisée pour parcourir un tableau en JavaScript.

Le fonctionnement de la méthode `filter()` est très simple. Elle consiste à filtrer un ou plusieurs éléments (un sous-ensemble) à partir d'une collection plus grande d'éléments (un sur-ensemble) en fonction d'une certaine condition/préférence.

Nous faisons tous cela tous les jours, que ce soit en lisant, en choisissant des amis ou notre conjoint, en choisissant quel film regarder, et ainsi de suite.

## La méthode JavaScript `Array.filter()`

La méthode `filter()` prend une fonction de rappel et appelle cette fonction pour chaque élément qu'elle parcourt à l'intérieur du tableau cible. La fonction de rappel peut prendre les paramètres suivants :

* `currentItem` : Il s'agit de l'élément dans le tableau qui est actuellement parcouru.

* `index` : Il s'agit de la position d'index de `currentItem` à l'intérieur du tableau.

* `array` : Cela représente le tableau cible avec tous ses éléments.

La méthode filter crée un nouveau tableau et retourne tous les éléments qui passent la condition spécifiée dans le rappel.

## Comment utiliser la méthode `filter()` en JavaScript

Dans les exemples suivants, je vais démontrer comment vous pouvez utiliser la méthode `filter()` pour filtrer des éléments à partir d'un tableau en JavaScript.

### Exemple 1 de `filter()` : Comment filtrer des éléments hors d'un tableau

Dans cet exemple, nous filtrons chaque personne qui est un tout-petit (dont l'âge est compris entre 0 et 4 ans).

```js
let people = [
    {name: "aaron",age: 65},
    {name: "beth",age: 2},
    {name: "cara",age: 13},
    {name: "daniel",age: 3},
    {name: "ella",age: 25},
    {name: "fin",age: 1},
    {name: "george",age: 43},
]

let toddlers = people.filter(person => person.age <= 3)

console.log(toddlers)



/*
[{
  age: 2,
  name: "beth"
}, {
  age: 3,
  name: "daniel"
}, {
  age: 1,
  name: "fin"
}]
*/
```

### Exemple 2 de `filter()` : Comment filtrer des éléments en fonction d'une propriété particulière

Dans cet exemple, nous allons uniquement filtrer les membres de l'équipe qui sont développeurs.

```js
let team = [
	{
  		name: "aaron",
    	position: "developer"
 	 },
  	{
  		name: "beth",
    	position: "ui designer"
  	},
  	{
  		name: "cara",
    	position: "developer"
  	},
 	{
  		name: "daniel",
    	position: "content manager"
 	 },
  	{
  		name: "ella",
    	position: "cto"
  	},
  	{
  		name: "fin",
    	position: "backend engineer"
  	},
  	{
  		name: "george",
    	position: "developer"
  },

]

let developers = team.filter(member => member.position == "developer")

console.log(developers)


/*
[{
  name: "aaron",
  position: "developer"
}, {
  name: "cara",
  position: "developer"
}, {
  name: "george",
  position: "developer"
}]
*/
```

Dans l'exemple ci-dessus, nous avons filtré les développeurs. Mais que faire si nous voulons filtrer chaque membre qui n'est **pas** un développeur ?

Nous pourrions faire ceci :

```js
let team = [
	{ 
        name: "aaron",
   		position: "developer"
  	},
  	{
  		name: "beth",
   		position: "ui designer"
 	 },
  	{
  		name: "cara",
    	position: "developer"
  	},
  	{
  		name: "daniel",
    	position: "content manager"
  	},
  	{
  		name: "ella",
    	position: "cto"
  	},
  	{
  		name: "fin",
    	position: "backend engineer"
  	},
  	{
  		name: "george",
    	position: "developer"
  	},

]

let nondevelopers = team.filter(member => member.position !== "developer")

console.log(nondevelopers)


/*
[
    {
  		name: "beth",
  		position: "ui designer"
	}, 
    {
  		name: "daniel",
  		position: "content manager"
	}, 
    {
  		name: "ella",
  		position: "cto"
	}, 
    {
  		name: "fin",
  		position: "backend engineer"
	}
]

*/
```

### Exemple 3 de `filter()` : Comment accéder à la propriété index

C'est une compétition. Dans cette compétition, il y a trois gagnants. Le premier recevra la médaille d'or, le deuxième l'argent, et le troisième, le bronze.

En utilisant `filter` et en accédant à la propriété `index` de chaque élément à chaque itération, nous pouvons filtrer chacun des trois gagnants dans différentes variables.

```js
let winners = ["Anna", "Beth", "Cara"]

let gold = winners.filter((winner, index) => index == 0)
let silver = winners.filter((winner, index) => index == 1)
let bronze = winners.filter((winner, index) => index == 2)

console.log(Gold winner: ${gold}, Silver Winner: ${silver}, Bronze Winner: ${bronze})

// "Gold winner: Anna, Silver Winner: Beth, Bronze Winner: Cara"
```

### Exemple 4 de `filter()` : Comment utiliser le paramètre array

L'une des utilisations les plus courantes du troisième paramètre (array) est d'inspecter l'état du tableau en cours de parcours. Par exemple, nous pouvons vérifier s'il reste un autre élément dans le tableau. Selon le résultat, nous pouvons spécifier que différentes choses doivent se produire.

Dans cet exemple, nous allons définir un tableau de quatre personnes. Cependant, comme il ne peut y avoir que trois gagnants, la quatrième personne de la liste devra être exclue.

Pour pouvoir faire cela, nous devons obtenir des informations sur le tableau cible à chaque itération.

```js
let competitors = ["Anna", "Beth", "Cara", "David"]

function displayWinners(name, index, array) {
    let isNextItem = index + 1 < array.length ? true : false
    if (isNextItem) {
    	console.log(`Le gagnant n°${index+1} est ${name}.`);
    } else {
    	console.log(`Désolé, ${name} n'est pas l'un des gagnants.`)
    }
}

competitors.filter((name, index, array) => displayWinners(name, index, array))

/*
"Le gagnant n°1 est Anna."
"Le gagnant n°2 est Beth."
"Le gagnant n°3 est Cara."
"Désolé, David n'est pas l'un des gagnants."
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/sorry.png align="left")

*Oups, désolé David !*

### Comment utiliser l'objet de contexte

En plus de la fonction de rappel, la méthode `filter()` peut également prendre un objet de contexte.

```js
filter(callbackfn, contextobj)
```

Cet objet peut ensuite être référencé depuis l'intérieur de la fonction de rappel en utilisant le mot-clé `this`.

### Exemple 5 de `filter()` : Comment accéder à l'objet de contexte avec `this`

Cela va être similaire à l'`exemple 1`. Nous allons filtrer chaque personne dont l'âge est compris entre 13 et 19 ans (adolescents).

Cependant, nous ne allons pas coder en dur les valeurs à l'intérieur de la fonction de rappel. Au lieu de cela, nous allons définir ces valeurs 13 et 19 comme propriétés à l'intérieur de l'objet `range`, que nous allons ensuite passer à `filter` comme objet de contexte (deuxième paramètre).

```js
let people = [
    {name: "aaron", age: 65},
    {name: "beth", age: 15},
    {name: "cara", age: 13},
    {name: "daniel", age: 3},
    {name: "ella", age: 25},
    {name: "fin", age: 16},
    {name: "george", age: 18},
]

let range = {
  lower: 13,
  upper: 16
}

   
let teenagers = people.filter(function(person) {
	return person.age >= this.lower && person.age <= this.upper;
}, range)

console.log(teenagers)

/*
[{
  age: 15,
  name: "beth"
}, {
  age: 13,
  name: "cara"
}, {
  age: 16,
  name: "fin"
}]
*/
```

Nous avons passé l'objet `range` comme deuxième argument à `filter()`. À ce moment-là, il est devenu notre objet de contexte. Par conséquent, nous avons pu accéder à nos plages supérieure et inférieure dans notre fonction de rappel avec les références `this.upper` et `this.lower` respectivement.

## Conclusion

La méthode de tableau `filter()` filtre les éléments qui correspondent à l'expression de rappel et les retourne.

En plus de la fonction de rappel, la méthode `filter` peut également prendre un objet de contexte comme deuxième argument. Cela vous permettra d'accéder à l'une de ses propriétés depuis la fonction de rappel en utilisant `this`.

J'espère que vous avez tiré quelque chose d'utile de cet article.

**S**i vous voulez en savoir plus sur le développement Web, n'hésitez pas à visiter mon [Blog](https://ubahthebuilder.tech/my-top-10-youtube-channels-for-programmers).

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).