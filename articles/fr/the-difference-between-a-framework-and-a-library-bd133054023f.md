---
title: La Différence Entre un Framework et une Bibliothèque
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-02-01T17:28:23.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-a-framework-and-a-library-bd133054023f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tO6yh-odg-YDLazUQ6FWVQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: La Différence Entre un Framework et une Bibliothèque
seo_desc: 'Developers often use the terms “library” and “framework” interchangeably.
  But there is a difference.

  Both frameworks and libraries are code written by someone else that is used to help
  solve common problems.

  For example, let’s say you have a program ...'
---

Les développeurs utilisent souvent les termes « bibliothèque » et « framework » de manière interchangeable. Mais il y a une différence.

Les frameworks et les bibliothèques sont tous deux du code écrit par quelqu'un d'autre, utilisé pour aider à résoudre des problèmes courants.

Par exemple, imaginons que vous avez un programme où vous prévoyez de travailler avec des chaînes de caractères. Vous décidez de garder votre code DRY (ne vous répétez pas) et d'écrire quelques fonctions réutilisables comme celles-ci :

```js
function getWords(str) {
   const words = str.split(' ');
   return words;
}
function createSentence(words) {
   const sentence = words.join(' ');
   return sentence;
}
```

Félicitations. Vous avez créé une bibliothèque.

Il n'y a rien de magique avec les frameworks ou les bibliothèques. Les bibliothèques et les frameworks sont tous deux du code réutilisable écrit par quelqu'un d'autre. Leur but est de vous aider à résoudre des problèmes courants de manière plus facile.

J'utilise souvent une maison comme métaphore pour les concepts de développement web.

Une bibliothèque est comme aller chez Ikea. Vous avez déjà une maison, mais vous avez besoin d'un peu d'aide pour les meubles. Vous n'avez pas envie de fabriquer votre propre table à partir de zéro. Ikea vous permet de choisir différentes choses à mettre dans votre maison. Vous êtes en contrôle.

Un framework, en revanche, est comme construire une maison modèle. Vous avez un ensemble de plans et quelques choix *limités* en matière d'architecture et de design. En fin de compte, c'est l'entrepreneur et les plans qui sont en contrôle. Et ils vous diront quand et où vous pouvez fournir votre contribution.

#### La Différence Technique

La différence technique entre un framework et une bibliothèque réside dans un terme appelé inversion de contrôle.

Lorsque vous utilisez une bibliothèque, vous êtes responsable du flux de l'application. Vous choisissez quand et où appeler la bibliothèque. Lorsque vous utilisez un framework, c'est le framework qui est responsable du flux. Il fournit quelques endroits pour que vous puissiez insérer votre code, mais il appelle le code que vous avez inséré selon ses besoins.

Examinons un exemple en utilisant jQuery (une bibliothèque) et Vue.js (un framework).

Imaginons que nous voulons afficher un message d'erreur lorsqu'une erreur est présente. Dans notre exemple, nous allons cliquer sur un bouton et simuler une erreur.

#### Avec jQuery :

```html
// index.html
<html>
   <head>
      <script src="https://code.jquery.com/jquery-3.3.1.min.js"
      </script>
      <script src="./app.js"></script>
   </head>
   <body>
      <div id="app">
         <button id="myButton">Submit</button>
       </div>
   </body>
</html>
// app.js
// Un ensemble de notre propre code,
// suivi de l'appel de la bibliothèque jQuery
let error = false;
const errorMessage = 'An Error Occurred';
$('#myButton').on('click', () => {
  error = true; // simuler une erreur et définir error = true
  if (error) {
    $('#app')
       .append(`<p id="error">${errorMessage}</p>`);
  } else {
    $('#error').remove();
  }
});
```

Remarquez comment nous utilisons jQuery. *Nous* disons à notre programme où nous voulons l'appeler. C'est un peu comme aller dans une bibliothèque physique et prendre certains livres sur l'étagère quand nous en avons besoin.

Ce n'est pas pour dire que les fonctions jQuery ne nécessitent pas certaines entrées *une fois* que nous les appelons, mais jQuery lui-même est une bibliothèque de ces fonctions. Nous sommes en contrôle.

#### Avec Vue.js

```html
//index.html
<html>
   <head>
      <script src="https://cdn.jsdelivr.net/npm/vue"></script>
      <script src="./app.js"></script>
   </head>
   <body>
      <div id="app"></div>
   </body>
</html>
const vm = new Vue({
  template: `<div id="vue-example">
               <button @click="checkForErrors">Submit</button>
               <p v-if="error">{{ errorMessage }}</p>
             </div>`,
  el: '#vue-example',
  data: {
    error: null,
    errorMessage: 'An Error Occurred',
  },
  methods: {
    checkForErrors()  {
      this.error = !this.error;
    },
  },
});
```

Avec Vue, nous devons remplir les blancs. Le constructeur Vue est un objet avec certaines propriétés. Il nous dit ce dont il a besoin, puis derrière les scènes, Vue décide quand il en a besoin. Vue inverse le contrôle du programme. Nous insérons notre code dans Vue. Vue est en contrôle.

La différence entre une bibliothèque et un framework réside dans le fait qu'il y ait ou non une inversion de contrôle.

#### Une note sur le fait d'être « opinionné »

Vous entendrez souvent les frameworks et les bibliothèques décrits comme « opinionnés » ou « non-opinionnés ». Ces termes sont subjectifs. Ils tentent de définir le niveau de liberté qu'un développeur a lors de la structuration de son code.

Les frameworks sont généralement plus opinionnés, car — par définition — l'inversion de contrôle nécessite une concession de la liberté de conception de l'application.

Encore une fois, le degré auquel quelque chose est opinionné est subjectif. Par exemple, je considérerais personnellement Angular comme un framework très opinionné, et Vue.js comme un framework moins opinionné.

### En résumé

* Les frameworks et les bibliothèques sont tous deux du code écrit par quelqu'un d'autre qui vous aide à effectuer certaines tâches courantes de manière moins verbeuse.

* Un framework inverse le contrôle du programme. Il dit au développeur ce dont il a besoin. Une bibliothèque ne le fait pas. Le programmeur appelle la bibliothèque où et quand *il* en a besoin.

* Le degré de liberté qu'une bibliothèque ou un framework donne au développeur déterminera à quel point elle ou il est « opinionné ».

Merci d'avoir lu !