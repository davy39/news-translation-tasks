---
title: Tutoriel JavaScript Array.find() – Comment itérer à travers les éléments d'un
  tableau
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-01T16:41:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-find-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/find-method-js.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Tutoriel JavaScript Array.find() – Comment itérer à travers les éléments
  d'un tableau
seo_desc: 'When you''re working with an array collection, sometimes you''ll only need
  to find out if an item exists in the array so you can retrieve it. And you won''t
  care how many other items (if any) exist within the same array.

  Well, we can use the find() meth...'
---

Lorsque vous travaillez avec une collection de tableau, parfois vous n'aurez besoin que de vérifier si un élément existe dans le tableau afin de le récupérer. Et vous ne vous soucierez pas du nombre d'autres éléments (s'il y en a) qui existent dans le même tableau.

Eh bien, nous pouvons utiliser la méthode `find()` pour faire exactement cela.

## Comment fonctionne la méthode Array.find()

La méthode `find()` est une méthode `Array.prototype` (c'est-à-dire intégrée) qui prend une fonction de rappel et appelle cette fonction pour chaque élément sur lequel elle itère à l'intérieur du tableau auquel elle est liée.

Lorsqu'elle trouve une correspondance (en d'autres termes, la fonction de rappel retourne `true`), la méthode retourne cet élément de tableau particulier et interrompt immédiatement la boucle. Ainsi, la méthode `find()` retourne le premier élément à l'intérieur d'un tableau qui satisfait la fonction de rappel.

La fonction de rappel peut prendre les paramètres suivants :

* `currentItem` : Il s'agit de l'élément dans le tableau qui est actuellement en cours d'itération.

* `index` : Il s'agit de la position d'index de `currentItem` à l'intérieur du tableau.

* `array` : Cela représente le tableau cible ainsi que tous ses éléments.

## **Comment utiliser la méthode** `find()` **en JavaScript**

Dans les exemples suivants, je vais démontrer comment vous pouvez utiliser la méthode `find()` pour récupérer le premier élément d'un tableau qui correspond à une condition spécifiée en JavaScript.

### Comment obtenir un seul élément avec find()

Supposons que vous avez un chien qui disparaît. Vous le signalez aux autorités compétentes et elles rassemblent un groupe de chiens retrouvés.

Pour pouvoir trouver votre chien, vous devez fournir des informations uniques à son sujet. Par exemple, la race de votre chien (un Chihuahua) pourrait être utilisée pour l'identifier.

Nous pouvons exprimer ce scénario en JavaScript en utilisant une collection de tableau. Le tableau appelé `foundDogs` contiendra tous les noms des chiens retrouvés ainsi que leurs races respectives. Et nous utiliserons la méthode `find()` pour trouver le chien qui est un Chihuahua à l'intérieur du tableau.

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
]

function findMyDog(dog) {
  return dog.breed === "Chihuahua"
}

let myDog = foundDogs.find(dog => findMyDog(dog));

console.log(myDog);


/*

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

La méthode find cesse d'itérer lorsqu'une correspondance est trouvée.

Il y a quelque chose de très important à retenir à propos de `find()` : elle cesse de s'exécuter dès que la fonction de rappel retourne une instruction `true`.

Pour illustrer cela, nous allons à nouveau utiliser l'exemple du chien disparu. Cette fois, nous allons supposer que deux Chihuahuas ont été trouvés.

Mais la méthode `find()` ne retournera que la première instance de Chihuahua qu'elle découvre dans le tableau. Toute autre instance sera ensuite ignorée.

Nous pouvons également le voir facilement en enregistrant la position d'index de cet élément dans la console :

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
  
  {
    breed: "Chihuahua",
    color: "yellow"
  }
]


function findMyDog(dog, index) {
	if (dog.breed === "Chihuahua") console.log(index);
  return dog.breed === "Chihuahua"
}


let myDog = foundDogs.find((dog, index) => findMyDog(dog, index));


console.log(myDog);

/* 
1

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/findreturns1.png align="left")

### Comment utiliser une affectation de déstructuration

Vous pouvez rendre votre code plus concis en combinant à la fois l'affectation de déstructuration et une expression de fonction fléchée.

Nous utiliserons la déstructuration pour extraire uniquement la propriété de nom de l'objet que nous passons ensuite en tant que paramètre à la fonction de rappel.

Nous obtiendrons le même résultat :

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
]

 


let myDog = foundDogs.find(({breed}) => breed === "Chihuahua");

console.log(myDog);

/*

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

### Comment trouver un élément par son index

Dans cet exemple, nous allons trouver et retourner la place appartenant à 'David' à l'intérieur du tableau en utilisant sa valeur d'index unique. Cela démontre une façon dont nous pouvons utiliser la propriété `index` à l'intérieur de notre fonction `callback` avec la méthode `find()` :

```js
let reservedPositions = [{
    name: "Anna",
    age: 24
  },

  {
    name: "Beth",
    age: 22
  },

  {
    name: "Cara",
    age: 25
  },
  
  {
    name: "David",
    age: 30
  },
  
  {
    name: "Ethan",
    age: 26
  }
]


function findByIndex(person, index) {
  return index === 3
}


let myPosition = reservedPositions.find((person, index) => findByIndex(person, index));

console.log(myPosition);

/*
{
  age: 30,
  name: "David"
}
*/
```

## Vous pouvez utiliser l'objet de contexte avec find()

En plus de la fonction de rappel, la méthode `find()` peut également prendre un objet de contexte.

```js
find(callback, contextObj)
```

Nous pouvons ensuite faire référence à cet objet depuis l'intérieur de la fonction **callback** à chaque itération, en utilisant le mot-clé `this` comme référence. Cela nous permet d'accéder à toutes les propriétés ou méthodes définies à l'intérieur de l'objet de contexte.

### Comment utiliser l'objet de contexte avec find()

Supposons que nous avons un tableau de candidatures à des emplois et que nous voulons sélectionner uniquement le premier candidat qui répond à tous les critères.

Tous les critères sont définis à l'intérieur d'un objet de contexte appelé `criteria` et cet objet est ensuite passé en tant que deuxième paramètre dans la méthode `find()`. Ensuite, depuis l'intérieur de la fonction de rappel, nous accédons à l'objet pour vérifier si un candidat correspond à tous les critères spécifiés.

```js
let applicants = [
    {name: "aaron", yrsOfExperience: 18, age: 66},
    {name: "beth", yrsOfExperience:  0, age: 18},
    {name: "cara", yrsOfExperience: 4, age: 22},
    {name: "daniel", yrsOfExperience: 3, age: 16},
    {name: "ella", yrsOfExperience: 5, age: 25},
    {name: "fin", yrsOfExperience: 0, age: 16},
    {name: "george", yrsOfExperience: 6, age: 28},
]

let criteria = {
	minimumExperience: 3,
  lowerAge: 18,
  upperAge: 65
}

   
let luckyApplicant = applicants.find(function(applicant) {
	return applicant.yrsOfExperience >= this.minimumExperience && applicant.age <= this.upperAge
  && applicant.age >= this.lowerAge ;
}, criteria)

console.log(luckyApplicant);

/*
{
  age: 22,
  name: "cara",
  yrsOfExperience: 4
}
*/
```

Techniquement, trois candidats (Cara, Ella et George) répondent tous aux critères. En d'autres termes, les trois ont au moins 18 ans, ne sont pas plus âgés que 65 ans et ont au moins 3 ans d'expérience professionnelle.

Cependant, puisque la méthode `find()` retourne toujours UNIQUEMENT la première instance qui évalue à vrai, les deux autres seront ignorés et la boucle sera rompue.

## **Conclusion**

La méthode `find()` est une méthode `Array.prototype` qui prend une fonction de rappel et appelle cette fonction pour chaque élément à l'intérieur du tableau lié.

Lorsque la fonction de rappel évalue à `true`, la méthode retourne l'élément actuel et rompt la boucle. Elle retourne uniquement la première correspondance – toute autre correspondance présente à l'intérieur du tableau sera ignorée.

En plus de la fonction de rappel, la méthode `find()` peut également prendre un objet de contexte comme deuxième argument. Cela vous permettra d'accéder à l'une de ses propriétés depuis la fonction de rappel en utilisant `this`.

J'espère que vous avez tiré quelque chose d'utile de cet article.

**S**i vous voulez en savoir plus sur le développement Web, n'hésitez pas à visiter mon [blog](https://ubahthebuilder.tech/the-ultimate-tutorial-on-javascript-dom-js-dom-with-examples)

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).