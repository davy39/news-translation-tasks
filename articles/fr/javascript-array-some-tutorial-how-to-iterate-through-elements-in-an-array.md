---
title: Tutoriel JavaScript Array.some() – Comment parcourir les éléments d'un tableau
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-07T22:14:16.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-some-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/array-some.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript Array.some() – Comment parcourir les éléments d'un
  tableau
seo_desc: 'When you''re working with an array in JavaScript, sometimes you might just
  want to check if at least one element inside that array passes a test. And you might
  not care about any other subsequent matches.

  In such a case, you should use the some() Java...'
---

Lorsque vous travaillez avec un tableau en JavaScript, il arrive parfois que vous souhaitiez simplement vérifier si **au moins un** élément du tableau passe un test. Et vous ne vous souciez peut-être pas des autres correspondances ultérieures.

Dans un tel cas, vous devriez utiliser la méthode `some()` de JavaScript. Voyons donc comment elle fonctionne.

## Comment utiliser la méthode Array.some() en JavaScript

La méthode `some()` est une méthode `Array.prototype` (intégrée) qui prend une fonction de rappel et testera cette fonction à chaque itération contre l'élément actuel.

Si un élément du tableau passe le test spécifié dans le rappel, la méthode arrête l'itération et retourne `true`. Si aucun élément ne passe le test, la méthode retourne `false`.

La méthode prend trois paramètres :

* `currentItem` : Il s'agit de l'élément à l'intérieur du tableau qui est actuellement parcouru

* `index` : Il s'agit de la position d'index de `currentItem` à l'intérieur du tableau

* `array` : Cela représente la collection de tableaux à laquelle la méthode `some()` est liée


Une façon simple de comprendre l'idée principale derrière la méthode `Array.some()` est de considérer l'une de nos plus grandes tendances en tant qu'êtres humains : **la généralisation**. Les gens ont tendance à faire des généralisations basées sur une seule expérience ou perception.

Par exemple, si une certaine personne d'un certain endroit se comporte d'une certaine manière, beaucoup de gens supposeront que tout le monde de cet endroit se comporte de la même manière. Même si une telle supposition était basée sur une seule expérience.

La méthode `some()` **se fait essentiellement une opinion** dès qu'elle trouve une correspondance et retourne `true`.

## Comment utiliser Array.some() dans votre JavaScript

Dans les exemples suivants, nous allons examiner de manière pratique comment utiliser la méthode `some()` dans notre JavaScript.

### Comment tester au moins une correspondance avec `some()`

Dans cet exemple, nous vérifierons s'il y a au moins un homme dans le tableau `people`

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  }
  
]


function isThereMale(person) {
	return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person)) // true
```

Puisqu'un homme existe réellement, la méthode `some()` retourne true.

Même si nous devions définir deux hommes dans le tableau, la méthode retournera toujours `true`. La méthode ne se soucie pas de savoir s'il y a un deuxième homme ou non, tout ce qui l'intéresse est le premier.

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ethan",
    sex: "Male"
  }
  
]


function isThereMale(person) {
	return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person)) // true
```

Si tous les éléments d'un tableau échouent au test de rappel, la méthode `some()` retournera `false`.

Dans cet exemple, puisque il n'y a pas d'homme dans notre tableau de personnes, `false` sera retourné à la place :

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Bella",
    sex: "Female"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ella",
    sex: "Female"
  }
  
]


function isThereMale(person) {
		return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person))) // false
```

### Comment utiliser le paramètre index avec `some()`

La fonction de rappel définie dans `some()` peut accéder à la propriété index de chaque élément parcouru. L'index est simplement une valeur numérique qui identifie de manière unique la position de chaque élément dans un tableau. Ainsi, vous pouvez référencer n'importe quel élément du tableau par son index.

Ici, nous utilisons la valeur de l'index pour construire un message que nous enregistrons sur la console :

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ethan",
    sex: "Male"
  }
  
]


function isThereMale(person, index) {
		if (person.sex === "Male") console.log(`No ${index+1}, qui est ${person.name}, est un Homme`)
		return person.sex === "Male"
}

console.log(people.some((person, index) => isThereMale(person, index)))

/* 
"No 2, qui est Ben, est un Homme"

true
*/
```

## Comment utiliser l'objet de contexte avec `some()`

En plus de la fonction de rappel, `some()` peut également prendre un objet de contexte.

```js
some(callbackFn, contextObj)
```

Nous pouvons ensuite faire référence à l'objet depuis l'intérieur de la fonction **callback** à chaque itération, en utilisant `this` comme référence. Cela nous permet d'accéder à toutes les propriétés ou méthodes définies dans l'objet de contexte.

### Exemple d'utilisation de l'objet de contexte avec `some()`

Dans cet exemple, nous cherchons à vérifier si au moins une personne dans le tableau de personnes est une **tricénaire**. C'est-à-dire que l'âge de la personne se situe entre 30 et 39 ans.

Nous pouvons définir la règle dans l'objet `conditions` puis y accéder depuis l'intérieur de la fonction de rappel en utilisant la notation `this.property`. Nous effectuons ensuite une vérification pour déterminer si au moins une personne correspond aux critères.

```js
let people = [{
    name: "Anna",
    age: 20
  },

  {
    name: "Ben",
    age: 35
  },

  {
    name: "Cara",
    age: 8
  },
  
  {
    name: "Danny",
    age: 17
  },
  
  {
    name: "Ethan",
    age: 28
  }
  
]

let conditions = {
	lowerAge: 30,
  upperAge: 39
}



console.log(people.some(person => function(person) {
	return person.age >= this.lowerAge && person.age <= this.upperAge
}, conditions)) // true
```

Puisqu'une personne (Ben) se situe dans cette fourchette, `some()` retournera `true`.

## **Conclusion**

La méthode `some()` est une méthode `Array.prototype` qui prend une fonction de rappel et appelle cette fonction pour chaque élément du tableau lié.

Lorsque qu'un élément passe le test de rappel, la méthode retourne `true` et arrête la boucle. Sinon, elle retourne `false`.

En plus de la fonction de rappel, la méthode `some()` peut également prendre un objet de contexte comme deuxième argument. Cela vous permettra d'accéder à l'une de ses propriétés depuis la fonction de rappel en utilisant `this`.

J'espère que vous avez appris quelque chose d'utile dans cet article.

**S**i vous souhaitez en savoir plus sur le développement Web, n'hésitez pas à visiter mon [blog](https://ubahthebuilder.tech/the-ultimate-tutorial-on-javascript-dom-js-dom-with-examples)

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).