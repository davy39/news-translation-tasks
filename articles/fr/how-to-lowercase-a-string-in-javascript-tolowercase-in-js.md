---
title: Comment mettre une chaîne en minuscules en JavaScript – toLowerCase() en JS
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-10-17T15:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-lowercase-a-string-in-javascript-tolowercase-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-magda-ehlers-1337382.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment mettre une chaîne en minuscules en JavaScript – toLowerCase() en
  JS
seo_desc: 'Strings are a fundamental part of working with JavaScript. And the toLowerCase()
  method is one of the many integrated methods that you can use to work with strings.

  In this article, we''ll see how to make strings lowercase with the toLowerCase()
  metho...'
---

Les chaînes de caractères sont une partie fondamentale du travail avec JavaScript. Et la méthode `toLowerCase()` est l'une des nombreuses méthodes intégrées que vous pouvez utiliser pour travailler avec des chaînes.

Dans cet article, nous verrons comment mettre des chaînes en minuscules avec la méthode `toLowerCase()` en JavaScript.

## **Qu'est-ce qu'une chaîne de caractères ?**

Une chaîne de caractères est un type de données qui peut contenir de nombreux caractères différents. Une chaîne est écrite comme une série de caractères entre des guillemets simples ou doubles.

```javascript
const exampleString = 'I am a String!'
console.log(exampleString); // I am a String!
```

## **Qu'est-ce qu'une méthode ?**

Une méthode est une fonction que vous pouvez utiliser sur un type de données spécifique. Les méthodes peuvent prendre ou non des arguments.

## **Comment fonctionne la méthode `toLowerCase()` ?**

La méthode `toLowerCase()` est une méthode de chaîne qui retourne une nouvelle chaîne entièrement en minuscules. Si la chaîne originale contient des lettres majuscules, dans la nouvelle chaîne, celles-ci seront en minuscules. Toute lettre minuscule ou tout caractère qui n'est pas une lettre n'est pas affecté.

```javascript
console.log(exampleString.toLowerCase()); // i am a string!

console.log('FREECODECAMP'.toLowerCase()); // freecodecamp

```

## **Ce qu'il faut garder à l'esprit lors de l'utilisation de la méthode toLowerCase**

La méthode `toLowerCase()` fait quelque chose de assez simple : elle crée une nouvelle chaîne où toutes les lettres majuscules sont maintenant en minuscules. Mais il y a quelques choses à garder à l'esprit lors de son utilisation. Examinons-les.

### **Les chaînes sont immuables**

Les chaînes sont un type de données immuable, ce qui signifie qu'elles ne peuvent pas être modifiées. La chaîne originale restera inchangée après l'utilisation de la méthode `toLowerCase()`.

Dans les exemples ci-dessus, la méthode `toLowerCase()` a agi sur `exampleString` mais ne l'a jamais modifiée. Vérifier la valeur de `exampleString` montre toujours la valeur originale :

```javascript
console.log(exampleString); // I am a string!

console.log(exampleString.toLowerCase()); // i am a string!

console.log(exampleString); // I am a string!

```

### **La méthode `toLowerCase()` retourne une nouvelle chaîne**

Cela signifie que la méthode `toLowerCase()` retourne une nouvelle chaîne. Vous devrez l'enregistrer dans une variable si vous souhaitez l'utiliser à nouveau dans votre code.

```javascript
const newString = exampleString.toLowerCase()

console.log(newString); // i am a string!
```

### **Les chaînes sont sensibles à la casse**

Les chaînes sont sensibles à la casse, donc une chaîne en minuscules est différente d'une chaîne en majuscules.

```javascript
console.log('freecodecamp' === 'FREECODECAMP'); // false

```

Cela est utile lorsque l'on pense à ce pour quoi la méthode `toLowerCase()` pourrait être utile. Dans l'exemple, vous verrez comment cette fonctionnalité rend la méthode `toLowerCase()` utile et nécessaire lors de la création d'un script ou d'un programme qui traite des chaînes.

## **Exemple de la méthode `toLowerCase()` – Comment vérifier si la saisie de l'utilisateur correspond**

Écrivons une petite application qui pose une question à l'utilisateur, obtient la saisie et donne un retour sur la réponse de l'utilisateur.

Il existe diverses façons de faire cela : vous pourriez l'utiliser dans une application web, en obtenant la valeur d'un élément `input` avec `type="text"`. Pour garder cela simple, dans l'exemple, vous verrez l'utilisation de la fonction JavaScript `prompt`.

La fonction `prompt` affichera une fenêtre contextuelle de message du navigateur avec un champ de saisie dans lequel l'utilisateur peut écrire une réponse :

```javascript
const answer = prompt("What color is the sun?")
if (answer === "yellow") {
  alert("Correct!")
} else {
  alert("That is not the correct color!")
}
```

Ce code pose une question à l'utilisateur, "What color is the sun?", et attend une réponse. Ensuite, il vérifie si la réponse est "yellow", et si c'est le cas, il affiche "Correct!". Si ce n'est pas le cas, il affiche "That is not the correct color!".

Mais il y a un problème avec ce code.

En exécutant ce code, vous aurez cette question posée dans la fenêtre contextuelle :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-69.png)

Si vous répondez "Yellow", il dit "That is not the correct color!"

Pourquoi cela se produit-il ?

Rappelez-vous que les chaînes sont sensibles à la casse. Le script vérifie si l'utilisateur a saisi la chaîne `yellow` – `Yellow`, avec un "Y" majuscule, est une chaîne différente.

Vous pouvez facilement corriger cela en utilisant la méthode `toLowerCase()`, et en apportant cette petite modification au code :

```javascript
const answer = prompt("What color is the sun?")
if (answer.toLowerCase() === "yellow") {
  alert("Correct!")
} else {
  alert("That is not the correct color!")
}
```

Et maintenant, si vous essayez à nouveau...

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-70.png)

Qu'est-ce qui a changé ? En écrivant `answer.toLowerCase()`, vous vous assurez que la chaîne vérifiée est entièrement en minuscules avant de la comparer avec la chaîne de réponse correcte "yellow". De cette manière, peu importe si l'utilisateur écrit "YELLOW" ou "yELLOW" ou "yellow" – tout est converti en minuscules.

Merci d'avoir lu ! Maintenant, vous savez comment utiliser la méthode `toLowerCase()` en JavaScript.