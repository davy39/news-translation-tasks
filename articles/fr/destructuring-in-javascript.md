---
title: Comment fonctionne la destructuration en JavaScript – Expliqué avec des exemples
  de code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-07T19:31:01.000Z'
originalURL: https://freecodecamp.org/news/destructuring-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-5--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne la destructuration en JavaScript – Expliqué avec des
  exemples de code
seo_desc: "Destructuring is a powerful JavaScript feature introduced in ES6 (ECMAScript\
  \ 2015). It makes it easier to extract values from arrays or properties from objects\
  \ and assign them to variables in a readable way. \nLet's delve into how destructuring\
  \ works ..."
---

La destructuration est une fonctionnalité puissante de JavaScript introduite dans ES6 (ECMAScript 2015). Elle facilite l'extraction de valeurs depuis des tableaux ou de propriétés depuis des objets et leur assignation à des variables de manière lisible. 

Plongeons dans le fonctionnement de la destructuration et explorons divers cas d'utilisation avec des exemples.

Vous pouvez obtenir le code source depuis [ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-destruturing/index.js).

## Table des matières

* [Qu'est-ce que la destructuration](#heading-quest-ce-que-la-destructuration) ?
* [Destructuration de tableau](#heading-destructuration-de-tableau)
* [Destructuration d'objet](#heading-destructuration-dobjet)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que la destructuration ?

La destructuration est une technique qui permet de déballer des valeurs depuis des tableaux ou des objets dans des variables séparées. 

Ce processus implique de décomposer des structures de données complexes en parties plus simples, facilitant ainsi leur manipulation.

## Destructuration de tableau

Commençons par la destructuration de tableau. Nous utiliserons l'exemple suivant.

Sans destructuration, extraire des valeurs depuis un tableau peut être verbeux :

```javascript
const hobbies = ["Reading", "Coding", "Hiking"];
const firstHobby = hobbies[0];
const secondHobby = hobbies[1];
const thirdHobby = hobbies[2];
console.log(firstHobby); // Sortie : Reading
console.log(secondHobby); // Sortie : Coding
console.log(thirdHobby); // Sortie : Hiking

```

Ici, vous accédez à chaque élément du tableau `hobbies` en utilisant la notation d'index et vous les assignez à des variables individuelles.

La destructuration simplifie ce processus en une seule ligne de code, comme ceci :

```javascript
const hobbies = ["Reading", "Coding", "Hiking"];
const [firstHobby, secondHobby, thirdHobby] = hobbies;
console.log(firstHobby); // Sortie : Reading
console.log(secondHobby); // Sortie : Coding
console.log(thirdHobby); // Sortie : Hiking

```

Dans cet exemple, vous extrayez les valeurs du tableau `hobbies` et vous les assignez aux variables `firstHobby`, `secondHobby` et `thirdHobby`, respectivement.

### Ignorer des éléments du tableau

Vous pouvez choisir d'ignorer certains éléments en les omettant du motif de destructuration :

```js
const hobbies = ["Reading", "Coding", "Hiking"];
const [firstHobby, , thirdHobby] = hobbies;
console.log(firstHobby); // Sortie : Reading
console.log(thirdHobby); // Sortie : Hiking


```

Dans cet exemple, vous destructurez le tableau `hobbies` mais vous n'assignez des valeurs qu'aux variables `firstHobby` et `thirdHobby`. Vous ignorez le deuxième élément du tableau en plaçant une virgule sans nom de variable entre `firstHobby` et `thirdHobby`. Cela vous permet d'extraire des éléments spécifiques du tableau tout en ignorant les autres, offrant plus de flexibilité et de contrôle dans vos motifs de destructuration.

### Destructuration de tableau imbriqué

La destructuration de tableau peut également être imbriquée. Voici un exemple :

```javascript
const nestedArray = [1, [2, 3], 4];
const [firstValue, [secondValue, thirdValue], fourthValue] = nestedArray;
console.log(firstValue); // Sortie : 1
console.log(secondValue); // Sortie : 2
console.log(thirdValue); // Sortie : 3
console.log(fourthValue); // Sortie : 4

```

Dans ce code, nous avons un tableau imbriqué `nestedArray`. En utilisant la destructuration de tableau imbriqué, vous extrayez des valeurs à la fois des tableaux externe et interne et vous les assignez aux variables `firstValue`, `secondValue`, `thirdValue` et `fourthValue`.

## Destructuration d'objet

Passons à la destructuration d'objet, considérons l'objet suivant :

```javascript
const person = {
  name: "John Doe",
  age: 30,
  city: "New York",
  occupation: "Software Engineer",
  hobbies: ["Reading", "Coding", "Hiking"]
};

```

### Destructuration régulière

La destructuration d'objet permet d'extraire des propriétés depuis des objets :

```javascript
const { name, age, city } = person;
console.log(name); // Sortie : John Doe
console.log(age); // Sortie : 30
console.log(city); // Sortie : New York

```

Dans cet exemple, `{ name, age, city }` est la syntaxe de destructuration. Cela signifie que vous extrayez les propriétés `name`, `age` et `city` de l'objet `person` et que vous les assignez à des variables de même nom. Ainsi, `name` aura la valeur `"John Doe"`, `age` aura `30` et `city` aura `"New York"`.

### Destructuration avec des noms différents

Vous pouvez assigner des propriétés extraites à des variables avec des noms différents :

```javascript
const { name: personName, age: personAge, city: personCity } = person;
console.log(personName); // Sortie : John Doe
console.log(personAge); // Sortie : 30
console.log(personCity); // Sortie : New York

```

Dans cet exemple, vous utilisez une syntaxe comme `{ name: personName, age: personAge, city: personCity }` qui vous permet d'assigner des propriétés extraites à des variables avec des noms différents. Ici, `name` de l'objet `person` est assigné à `personName`, `age` est assigné à `personAge` et `city` est assigné à `personCity`.

### Avoir des valeurs par défaut lors de la destructuration

Vous pouvez également fournir des valeurs par défaut pour les propriétés d'objet :

```javascript
const { name, age, gender = "Unknown" } = person;
console.log(gender); // Sortie : Unknown

```

Ici, vous fournissez une valeur par défaut `"Unknown"` pour la propriété `gender` au cas où elle ne serait pas présente dans l'objet `person`. Si `gender` n'est pas défini dans `person`, la variable `gender` prendra par défaut `"Unknown"`.

### Objets imbriqués

La destructuration d'objet supporte les objets imbriqués :

```javascript
const { name, address: { city, country } } = person;
console.log(city); // Sortie : New York
console.log(country); // Sortie : undefined (en supposant que address n'a pas de propriété country)

```

Dans cet exemple, `{ name, address: { city, country } }` est la syntaxe de destructuration. Vous extrayez la propriété `name` directement de l'objet `person`. Ensuite, dans l'objet `address`, vous extrayez les propriétés `city` et `country`. Ainsi, `city` aura la valeur `"New York"`, et `country` sera `undefined` en supposant que `address` n'a pas de propriété `country`.

## Conclusion

C'est tout ! Vous devriez maintenant avoir une bonne compréhension de comment fonctionne la destructuration en JavaScript pour les tableaux et les objets. 

N'hésitez pas à expérimenter avec les exemples de code pour renforcer votre compréhension. Si vous avez des retours ou des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/introvertedbot) ou [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/). Bon apprentissage !