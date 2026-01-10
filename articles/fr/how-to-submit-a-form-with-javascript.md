---
title: Comment soumettre un formulaire avec JavaScript – Exemple de bouton de soumission
  JS
date: '2023-01-20T22:01:03.000Z'
author: Joel Olawanle
authorURL: https://www.freecodecamp.org/news/author/joel-olawanle/
originalURL: https://freecodecamp.org/news/how-to-submit-a-form-with-javascript
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--10-.png
tags:
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
seo_desc: 'When building applications and websites on the internet, you’ll sometimes
  need your users to supply information by filling out a form.

  But then you might wonder – how do you get this data from the form? Well, you can
  do this with JavaScript.

  In this ...'
---


Lors de la création d'applications et de sites web sur internet, vous aurez parfois besoin que vos utilisateurs fournissent des informations en remplissant un formulaire.

<!-- more -->

Mais vous pourriez alors vous demander : comment récupérer ces données du formulaire ? Eh bien, vous pouvez le faire avec JavaScript.

Dans cet article, vous apprendrez comment créer un formulaire et en extraire les données lors de sa soumission avec JavaScript.

Cet article ne traitera pas de la manière d'insérer des données dans une base de données – il couvrira uniquement la soumission d'un formulaire. Mais sachez qu'une fois ces données récupérées, vous pouvez les envoyer vers la base de données de votre choix, les utiliser pour manipuler des informations, et bien plus encore.

Pour soumettre un formulaire en utilisant JavaScript, vous devez d'abord créer le formulaire et ajouter des attributs spécifiques et distinctifs aux champs de saisie. Vous utiliserez ces attributs pour récupérer les données lorsque l'utilisateur soumet le formulaire, puis appellerez une fonction pour gérer les validations (éventuellement si des données sont soumises).

## Comment créer le formulaire HTML

Pour commencer, créons un formulaire HTML de base avec deux champs : nom d'utilisateur (username) et mot de passe (password). Nous ajouterons également un bouton qui sera utilisé pour soumettre le formulaire et déclencher une action JavaScript.

```js
<form action="">
  <h1>Login</h1>
  <input type="text" class="form-control" placeholder="Enter your Username...">
  <input type="password" class="form-control" placeholder="Enter your Password...">
  <button type="submit">Submit</button>
</form>
```

Pour récupérer les données de ce formulaire via JavaScript, vous devrez attacher des attributs spécifiques au champ de saisie du formulaire et au formulaire lui-même. Ces attributs peuvent être un `id`, une `class`, ou même la balise `name`. Cela aidera à récupérer les données en JavaScript en utilisant les méthodes du document.

Par exemple, si vous utilisez un attribut `id` sur votre champ de saisie, vous pouvez accéder aux données du champ et à d'autres valeurs en utilisant la méthode du document `getElementByID('idName')` :

```js
// HTML
<input type="text" id="username" class="form-control" placeholder="Enter your Username...">

// JS
let myUsername = document.getElementById('username');
console.log(myUsername);
```

Si vous utilisez un attribut `class`, vous utiliserez `getElementsByClassName(className)`, qui renvoie un tableau de tous les éléments possédant cette `className`. S'il n'y a qu'un seul élément, vous pouvez utiliser l'index `0` pour accéder à ses données :

```js
// HTML
<input type="text" class="username" class="form-control" placeholder="Enter your Username...">

// JS
let myUsername = document.getElementsByClassName('username');
console.log(myUsername[0]);
```

Si vous utilisez l'attribut `name`, vous utiliserez `getElementsByName(name)`. C'est similaire au fonctionnement de l'attribut class puisqu'il renvoie également un tableau que vous pouvez parcourir ou auquel vous pouvez accéder via son numéro d'index :

```js
// HTML
<input type="text" name="username" class="form-control" placeholder="Enter your Username...">

// JS
let myUsername = document.getElementsByName('username');
console.log(myUsername[0]);
```

> Note : Cela ne retournera pas la valeur de saisie mais l'élément d'entrée lui-même.

## Comment soumettre un formulaire avec JavaScript

La première étape consiste à attacher votre attribut préféré au formulaire, que vous pourrez utiliser pour suivre le moment où le formulaire est soumis. Il peut s'agir d'un attribut `id`, `class` ou `name`, mais pour cet article, j'utiliserai `id` pour le formulaire et les champs de saisie :

```js
<form action="" id="loginForm">
  <h1>Login</h1>
  <input type="text" id="username" class="form-control" placeholder="Enter your Username...">
  <input type="password" id="password" class="form-control" placeholder="Enter your Password...">
  <button type="submit">Submit</button>
</form>
```

À ce stade, vous pouvez maintenant gérer la soumission du formulaire avec JavaScript. Vous récupérez d'abord le formulaire avec votre attribut préféré, qui peut être un id, et vous le stockez dans une variable :

```js
let loginForm = document.getElementById("loginForm");
```

Ensuite, vous pouvez attacher l' `addEventListener` à la variable du formulaire et écouter un événement de soumission. Cet écouteur d'événements vous permet d'attacher une fonction de rappel qui se déclenche une fois le formulaire soumis :

```js
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // handle submit
});
```

À ce stade, vous pouvez maintenant récupérer les données du formulaire et effectuer toute opération de votre choix. Pour cet article, validons d'abord les données en vérifiant si le champ est vide avant d'effectuer toute opération :

```js
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let username = document.getElementById("username");
  let password = document.getElementById("password");

  if (username.value == "" || password.value == "") {
    // throw error
  } else {
    // perform operation with form input
  }
});
```

Voici l'intégralité du code JavaScript :

```js
let loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let username = document.getElementById("username");
  let password = document.getElementById("password");

  if (username.value == "" || password.value == "") {
    alert("Ensure you input a value in both fields!");
  } else {
    // perform operation with form input
    alert("This form has been successfully submitted!");
    console.log(
      `This form has a username of ${username.value} and password of ${password.value}`
    );

    username.value = "";
    password.value = "";
  }
});
```

Voir le Pen [Soumission de formulaire JS][1] par Olawanle Joel ([@olawanlejoel][2]) sur [CodePen][3].

## Conclusion

Dans cet article, vous avez appris comment soumettre un formulaire avec JavaScript et comment cela fonctionne avec les différentes méthodes du DOM.

Il existe d'autres façons de procéder, mais c'est une méthode simple pour gérer la soumission en JavaScript.

Vous pouvez accéder à plus de 150 de mes articles en [visitant mon site web][4]. Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.

[1]: https://codepen.io/olawanlejoel/pen/xxzvdqQ
[2]: https://codepen.io/olawanlejoel
[3]: https://codepen.io
[4]: https://joelolawanle.com/contents