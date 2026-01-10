---
title: Apprendre les opérations CRUD en JavaScript en créant une APPLICATION TODO
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2022-04-13T17:57:32.000Z'
originalURL: https://freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Frame-12--2-.png
tags:
- name: crud
  slug: crud
- name: JavaScript
  slug: javascript
seo_title: Apprendre les opérations CRUD en JavaScript en créant une APPLICATION TODO
seo_desc: 'Today we''re gonna learn how to do CRUD Operations in JavaScript by making
  a Todo App. Let''s get started 🔥

  This is the app we''re making today:



  Live preview

  GitHub Repository


  You can watch this tutorial on YouTube as well if you like 🎥

  https://you...'
---

Aujourd'hui, nous allons apprendre à effectuer des opérations CRUD en JavaScript en créant une application Todo. Commençons 🔥

Voici l'application que nous allons créer aujourd'hui :

![Application que nous allons créer aujourd'hui](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ut6o5hbsrzb5eccm72v.png)

- [Aperçu en direct](https://crud-application-al9am9v2v-joyshaheb.vercel.app/)
- [Dépôt GitHub](https://github.com/JoyShaheb/CRUD-Application)

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez 🎥


%[https://youtu.be/fL9cts8ykbU]

# Table des matières

- Qu'est-ce que CRUD ?
- Comprendre les principes CRUD
- Comment créer une application To-Do en utilisant les opérations CRUD

## Qu'est-ce que CRUD ?

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/agloiqjwk11qr7mu39y4.png)

CRUD signifie -

- C : Create (Créer)
- R : Read (Lire)
- U : Update (Mettre à jour)
- D : Delete (Supprimer)

![Forme complète de CRUD](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3md2xtw76u0y1fr8polm.png)

CRUD est un type de mécanisme qui vous permet de créer des données, de lire des données, de les modifier et de supprimer ces données. Dans notre cas, nous allons créer une application Todo, donc nous aurons 4 options pour créer des tâches, lire des tâches, mettre à jour des tâches ou supprimer des tâches.

## Comprendre les principes CRUD

Avant de commencer le tutoriel, comprenons d'abord les principes CRUD. Pour cela, créons une application de médias sociaux très très simple.

![Projet d'application de médias sociaux](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8cr1ueopcx4bfgz7j8ov.gif)

## Installation

![Configuration du projet](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9o3h86jd7md2bo54n4cd.png)

Pour ce projet, nous allons suivre les étapes ci-dessous :

- Créer 3 fichiers nommés index.html, style.css et main.js
- Lier le fichier JavaScript et CSS à index.html
- Démarrer votre serveur en direct

### HTML

À l'intérieur de la balise body, créez une div avec un nom de classe `.container`. Là, nous aurons 2 sections, `.left` et `.right` 👍

```HTML
<body>
  <h1>Application de médias sociaux</h1>
  <div class="container">

    <div class="left"></div>
    <div class="right"></div>

  </div>
</body>
```

Du côté gauche, nous allons créer nos publications. Du côté droit, nous pouvons voir, mettre à jour et supprimer nos publications. Maintenant, créez un formulaire à l'intérieur de la balise div .left 👍

```HTML
<div class="left">
  <form id="form">
    <label for="post">Écrivez votre publication ici</label>
    <br><br>
    <textarea name="post" id="input" cols="30" rows="10"></textarea>
    <br> <br>
    <div id="msg"></div>
    <button type="submit">Publier</button>
  </form>
</div>
```

Écrivez ce code à l'intérieur du HTML afin que nous puissions afficher notre publication du côté droit 👍

```HTML
<div class="right">
  <h3>Vos publications ici</h3>
  <div id="posts"></div>
</div>
```

Ensuite, nous allons insérer le CDN de font-awesome à l'intérieur de la balise head pour utiliser ses polices dans notre projet 👍

```HTML
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
```

Maintenant, nous allons créer quelques publications d'exemple avec des icônes de suppression et d'édition. Écrivez ce code à l'intérieur de la div avec l'id #posts : 👍

```HTML
<div id="posts">
  <div>
    <p>Bonjour le monde publication 1</p>
    <span class="options">
      <i class="fas fa-edit"></i>
      <i class="fas fa-trash-alt"></i>
    </span>
  </div>

  <div >
    <p>Bonjour le monde publication 2</p>
    <span class="options">
      <i class="fas fa-edit"></i>
      <i class="fas fa-trash-alt"></i>
    </span>
  </div>
</div>
```

Le résultat jusqu'à présent ressemble à ceci :

![Résultat du balisage HTML](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6ra3w4flp2et2wsf94m2.png)

### CSS

![Ajout de CSS pour le projet 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/djlwav0yj8w5vld3ux5z.png)

Gardons cela simple. Écrivez ces styles à l'intérieur de votre feuille de style : 👍

```CSS
body {
  font-family: sans-serif;
  margin: 0 50px;
}

.container {
  display: flex;
  gap: 50px;
}

#posts {
  width: 400px;
}

i {
  cursor: pointer;
}
```

Maintenant, écrivez ces styles pour la div de publication et les icônes d'options : 👍

```CSS
#posts div {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.options {
  display: flex;
  gap: 25px;
}

#msg {
  color: red;
}
```

Les résultats jusqu'à présent ressemblent à ceci : 👍

![Le résultat après l'ajout de la partie css du projet 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dttu77ecfpd235byt4pi.png)

### Partie JavaScript

![Démarrage de la partie javascript](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nl1o5q5kcymkfyrsme8f.png)

Selon ce diagramme, nous allons avancer avec le projet. Ne vous inquiétez pas, je vais tout expliquer en cours de route. 👍

![diagramme](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vlsw0253j7st1ictip03.png)

#### Validation du formulaire

Tout d'abord, ciblons tous les sélecteurs d'ID du HTML en JavaScript. Comme ceci : 👍

```js
let form = document.getElementById("form");
let input = document.getElementById("input");
let msg = document.getElementById("msg");
let posts = document.getElementById("posts");
```

Ensuite, construisez un écouteur d'événement de soumission pour le formulaire afin qu'il puisse empêcher le comportement par défaut de notre application. En même temps, nous allons créer une fonction nommée `formValidation`. 👍

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("bouton cliqué");

  formValidation();
});

let formValidation = () => {};
```

Maintenant, nous allons faire une instruction if else à l'intérieur de notre fonction `formValidation`. Cela nous aidera à empêcher les utilisateurs de soumettre des champs de saisie vides. 👍

```js
let formValidation = () => {
  if (input.value === "") {
    msg.innerHTML = "La publication ne peut pas être vide";
    console.log("échec");
  } else {
    console.log("succès");
    msg.innerHTML = "";
  }
};
```

Voici le résultat jusqu'à présent : 👍

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7sb8faq21j5dzy9vlswj.gif)

Comme vous pouvez le voir, un message s'affichera également si l'utilisateur essaie de soumettre le formulaire vide.

#### Comment accepter les données des champs de saisie

Quelles que soient les données que nous obtenons des champs de saisie, nous les stockerons dans un objet. Créons un objet nommé `data`. Et, créons une fonction nommée `acceptData` : 👍

```js
let data = {};

let acceptData = () => {};
```

L'idée principale est que, en utilisant la fonction, nous collectons les données des saisies et les stockons dans notre objet nommé `data`. Maintenant, terminons de construire notre fonction `acceptData`.

```js
let acceptData = () => {
  data["text"] = input.value;
  console.log(data);
};
```

De plus, nous avons besoin que la fonction `acceptData` fonctionne lorsque l'utilisateur clique sur le bouton de soumission. Pour cela, nous allons déclencher cette fonction dans l'instruction else de notre fonction `formValidation`. 👍

```js
let formValidation = () => {
  if (input.value === "") {
    // Les autres codes sont ici
  } else {
    // Les autres codes sont ici
    acceptData();
  }
};
```

Lorsque nous saisissons des données et soumettons le formulaire, sur la console nous pouvons voir un objet contenant les valeurs de saisie de notre utilisateur. Comme ceci : 👍

![résultat jusqu'à présent sur la console](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jje41w8b70hpdgyonpqj.png)

#### Comment créer des publications en utilisant les littéraux de gabarit JavaScript

Afin de publier nos données de saisie du côté droit, nous devons créer un élément div et l'ajouter à la div des publications. Tout d'abord, créons une fonction et écrivons ces lignes : 👍

```js
let createPost = () => {
  posts.innerHTML += ``;
};
```

Les backticks sont des littéraux de gabarit. Ils fonctionneront comme un gabarit pour nous. Ici, nous avons besoin de 3 choses : une div parent, la saisie elle-même, et la div des options qui porte les icônes d'édition et de suppression. Terminons notre fonction 👍

```js
let createPost = () => {
  posts.innerHTML += `
  <div>
    <p>${data.text}</p>
    <span class="options">
      <i onClick="editPost(this)" class="fas fa-edit"></i>
      <i onClick="deletePost(this)" class="fas fa-trash-alt"></i>
    </span>
  </div>
  `;
  input.value = "";
};
```

Dans notre fonction `acceptdata`, nous allons déclencher notre fonction `createPost`. Comme ceci : 👍

```js
let acceptData = () => {
  // Les autres codes sont ici

  createPost();
};
```

Le résultat jusqu'à présent : 👍

![Résultat jusqu'à présent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8cr1ueopcx4bfgz7j8ov.gif)

Jusqu'à présent, tout va bien, nous avons presque terminé avec le projet 1.

![jusqu'à présent tout va bien](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oyrijoc70cy0sebiu1a5.png)

#### Comment supprimer une publication

Afin de supprimer une publication, tout d'abord, créons une fonction à l'intérieur de notre fichier javascript :

```js
let deletePost = (e) => {};
```

Ensuite, nous déclenchons cette fonction `deletePost` à l'intérieur de toutes nos icônes de suppression en utilisant un attribut onClick. Vous écrirez ces lignes en HTML et sur le littéral de gabarit. 👍

```html
<i onClick="deletePost(this)" class="fas fa-trash-alt"></i>
```

Le mot-clé `this` fera référence à l'élément qui a déclenché l'événement. Dans notre cas, `this` fait référence au bouton de suppression.

Regardez attentivement, le parent du bouton de suppression est le span avec le nom de classe options. Le parent du span est la div. Donc, nous écrivons `parentElement` deux fois afin que nous puissions sauter de l'icône de suppression à la div et la cibler directement pour la supprimer.

Terminons notre fonction. 👍

```js
let deletePost = (e) => {
  e.parentElement.parentElement.remove();
};
```

Le résultat jusqu'à présent : 👍

![résultat de la suppression d'une publication](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m9upccmzs4zszg1nfrdf.gif)

#### Comment modifier une publication

Afin de modifier une publication, tout d'abord, créons une fonction à l'intérieur de notre fichier JavaScript :

```js
let editPost = (e) => {};
```

Ensuite, nous déclenchons cette fonction `editPost` à l'intérieur de toutes nos icônes d'édition en utilisant un attribut onClick. Vous écrirez ces lignes en HTML et sur le littéral de gabarit. 👍

```html
<i onClick="editPost(this)" class="fas fa-edit"></i>
```

Le mot-clé `this` fera référence à l'élément qui a déclenché l'événement. Dans notre cas, `this` fait référence au bouton d'édition.

Regardez attentivement, le parent du bouton d'édition est le span avec le nom de classe options. Le parent du span est la div. Donc, nous écrivons `parentElement` deux fois afin que nous puissions sauter de l'icône d'édition à la div et la cibler directement pour la supprimer.

Ensuite, quelles que soient les données à l'intérieur de la publication, nous les ramenons dans le champ de saisie pour les modifier.

Terminons notre fonction. 👍

```js
let editPost = (e) => {
  input.value = e.parentElement.previousElementSibling.innerHTML;
  e.parentElement.parentElement.remove();
};
```

Le résultat jusqu'à présent : 👍

![Résultat de la modification d'une publication](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uqymvra7ejzi59ekpscd.gif)

## Prenez une pause !

![Prenez une pause](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rywq5vr0yz4e0hoosfn9.png)

Félicitations à tous pour avoir terminé le projet 1. Maintenant, prenez une petite pause !

# Comment créer une application To-Do en utilisant les opérations CRUD

![Créons une application todo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qbjnnnfvbqmmm8x3mdfw.png)

Commençons à créer le projet 2, qui est une application To-Do.

## Configuration du projet

![Configuration du projet](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pg9yjnp9s7176xomxlnj.png)

Pour ce projet, nous allons suivre les étapes ci-dessous :

- Créer 3 fichiers nommés index.html, style.css et main.js
- Lier les fichiers JavaScript et CSS à index.html
- Démarrer notre serveur en direct

### HTML

Écrivez ce code de démarrage à l'intérieur du fichier HTML : 👍

```html
<div class="app">
  <h4 class="mb-3">APPLICATION TODO</h4>

  <div id="addNew" data-bs-toggle="modal" data-bs-target="#form">
    <span>Ajouter une nouvelle tâche</span>
    <i class="fas fa-plus"></i>
  </div>
</div>
```

La div avec l'id `addNew` est le bouton qui ouvrira la modale. Le span sera affiché sur le bouton. Le `i` est l'icône de font-awesome.

Nous allons utiliser bootstrap pour créer notre modale. Nous utiliserons la modale pour ajouter de nouvelles tâches. Pour cela, ajoutez le lien CDN de bootstrap à l'intérieur de la balise head. 👍

```html
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
  rel="stylesheet"
  integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
  crossorigin="anonymous"
/>

<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
  crossorigin="anonymous"
></script>
```

Pour voir les tâches créées, nous utiliserons une div avec l'id tasks, à l'intérieur de la div avec le nom de classe app. 👍

```html
<h5 class="text-center my-3">Tâches</h5>

<div id="tasks"></div>
```

Insérez le CDN de font-awesome à l'intérieur de la balise head pour utiliser les polices dans notre projet 👍

```HTML
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
```

Copiez et collez le code ci-dessous qui provient de la modale bootstrap. Il contient un formulaire avec 3 champs de saisie et un bouton de soumission. Si vous le souhaitez, vous pouvez rechercher sur le site de Bootstrap en écrivant 'modal' dans la barre de recherche.

```html
<!-- Modal -->
<form
  class="modal fade"
  id="form"
  tabindex="-1"
  aria-labelledby="exampleModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Ajouter une nouvelle tâche</h5>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="modal"
          aria-label="Close"
        ></button>
      </div>
      <div class="modal-body">
        <p>Titre de la tâche</p>
        <input type="text" class="form-control" name="" id="textInput" />
        <div id="msg"></div>
        <br />
        <p>Date d'échéance</p>
        <input type="date" class="form-control" name="" id="dateInput" />
        <br />
        <p>Description</p>
        <textarea
          name=""
          class="form-control"
          id="textarea"
          cols="30"
          rows="5"
        ></textarea>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
          Fermer
        </button>
        <button type="submit" id="add" class="btn btn-primary">Ajouter</button>
      </div>
    </div>
  </div>
</form>
```

Le résultat jusqu'à présent : 👍

![Configuration du fichier Html](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eazu2i62bilebhgbrclr.png)

Nous avons terminé la configuration du fichier HTML. Commençons le CSS.

### CSS

![Ajout de la partie css](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bqldzsv7vcq7ed4sbptj.png)

Ajoutez ces styles dans le body afin que nous puissions garder notre application au centre exact de l'écran.

```css
body {
  font-family: sans-serif;
  margin: 0 50px;
  background-color: #e5e5e5;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

Stylisons la div avec le nom de classe app. 👍

```css
.app {
  background-color: #fff;
  width: 300px;
  height: 500px;
  border: 5px solid #abcea1;
  border-radius: 8px;
  padding: 15px;
}
```

Le résultat jusqu'à présent : 👍

![Styles de l'application](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vuunx9tkgvw5uxqq05ab.png)

Maintenant, stylisons le bouton avec l'id `addNew`. 👍

```css
#addNew {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(171, 206, 161, 0.35);
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}
.fa-plus {
  background-color: #abcea1;
  padding: 3px;
  border-radius: 3px;
}
```

Le résultat jusqu'à présent : 👍

![Bouton Ajouter une nouvelle tâche](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mt353dpjsczqtf8msb71.png)

Si vous cliquez sur le bouton, la modale apparaît comme ceci : 👍

![Apparition de la modale](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jfmc7fyzdef7nnmxf7ap.gif)

### Ajoutez le JS

![Ajout du JavaScript](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xv4u6j0gafmqxwoh6rpm.png)

Dans le fichier JavaScript, tout d'abord, sélectionnez tous les sélecteurs du HTML que nous devons utiliser. 👍

```javascript
let form = document.getElementById("form");
let textInput = document.getElementById("textInput");
let dateInput = document.getElementById("dateInput");
let textarea = document.getElementById("textarea");
let msg = document.getElementById("msg");
let tasks = document.getElementById("tasks");
let add = document.getElementById("add");
```

#### Validations du formulaire

Nous ne pouvons pas laisser un utilisateur soumettre des champs de saisie vides. Donc, nous devons valider les champs de saisie. 👍

```javascript
form.addEventListener("submit", (e) => {
  e.preventDefault();
  formValidation();
});

let formValidation = () => {
  if (textInput.value === "") {
    console.log("échec");
    msg.innerHTML = "La tâche ne peut pas être vide";
  } else {
    console.log("succès");
    msg.innerHTML = "";
  }
};
```

Ajoutez également cette ligne à l'intérieur du CSS :

```css
#msg {
  color: red;
}
```

Le résultat jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j0b0aidh5hbc2hxkp378.gif)

Comme vous pouvez le voir, la validation fonctionne. Le code JavaScript ne permet pas à l'utilisateur de soumettre des champs de saisie vides, sinon vous allez voir un message d'erreur.

#### Comment collecter des données et utiliser le stockage local

Quelles que soient les saisies que l'utilisateur écrit, nous devons les collecter et les stocker dans le stockage local.

Tout d'abord, nous collectons les données des champs de saisie, en utilisant la fonction nommée `acceptData` et un tableau nommé `data`. Ensuite, nous les poussons à l'intérieur du stockage local comme ceci : 👍

```javascript
let data = [];

let acceptData = () => {
  data.push({
    text: textInput.value,
    date: dateInput.value,
    description: textarea.value,
  });

  localStorage.setItem("data", JSON.stringify(data));

  console.log(data);
};
```

Notez également que cela ne fonctionnera jamais à moins que vous n'invoquiez la fonction `acceptData` à l'intérieur de l'instruction else de la validation du formulaire. Suivez ici : 👍

```js
let formValidation = () => {

  // Les autres codes sont ici
   else {

    // Les autres codes sont ici

    acceptData();
  }
};
```

Vous avez peut-être remarqué que la modale ne se ferme pas automatiquement. Pour résoudre cela, écrivez cette petite fonction à l'intérieur de l'instruction else de la validation du formulaire : 👍

```js
let formValidation = () => {

  // Les autres codes sont ici
   else {

    // Les autres codes sont ici

    acceptData();
    add.setAttribute("data-bs-dismiss", "modal");
    add.click();

    (() => {
      add.setAttribute("data-bs-dismiss", "");
    })();
  }
};
```

Si vous ouvrez les outils de développement Chrome, allez dans l'application et ouvrez le stockage local. Vous pouvez voir ce résultat : 👍

![Résultat du stockage local](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7mku6j28tknry3xqrwg3.png)

#### Comment créer de nouvelles tâches

Afin de créer une nouvelle tâche, nous devons créer une fonction, utiliser des littéraux de gabarit pour créer les éléments HTML, et utiliser une carte pour pousser les données collectées de l'utilisateur à l'intérieur du gabarit. Suivez ici : 👍

```javascript
let createTasks = () => {
  tasks.innerHTML = "";
  data.map((x, y) => {
    return (tasks.innerHTML += `
    <div id=${y}>
          <span class="fw-bold">${x.text}</span>
          <span class="small text-secondary">${x.date}</span>
          <p>${x.description}</p>
  
          <span class="options">
            <i onClick= "editTask(this)" data-bs-toggle="modal" data-bs-target="#form" class="fas fa-edit"></i>
            <i onClick ="deleteTask(this);createTasks()" class="fas fa-trash-alt"></i>
          </span>
        </div>
    `);
  });

  resetForm();
};
```

Notez également que la fonction ne s'exécutera jamais à moins que vous ne l'invoquiez à l'intérieur de la fonction `acceptData`, comme ceci : 👍

```js
let acceptData = () => {
  // Les autres codes sont ici

  createTasks();
};
```

Une fois que nous avons terminé de collecter et d'accepter les données de l'utilisateur, nous devons effacer les champs de saisie. Pour cela, nous créons une fonction appelée `resetForm`. Suivez ici : 👍

```js
let resetForm = () => {
  textInput.value = "";
  dateInput.value = "";
  textarea.value = "";
};
```

Le résultat jusqu'à présent : 👍

![Ajout de cartes de tâches](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8li973gq11jlrarl0nln.png)

Comme vous pouvez le voir, il n'y a pas de styles avec la carte. Ajoutons quelques styles : 👍

```css
#tasks {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
}

#tasks div {
  border: 3px solid #abcea1;
  background-color: #e2eede;
  border-radius: 6px;
  padding: 5px;
  display: grid;
  gap: 4px;
}
```

Stylisez les boutons d'édition et de suppression avec ce code : 👍

```css
#tasks div .options {
  justify-self: center;
  display: flex;
  gap: 20px;
}

#tasks div .options i {
  cursor: pointer;
}
```

Le résultat jusqu'à présent : 👍

![Styles des modèles de cartes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/axe47wf6jutn330b5scn.png)

#### Fonction pour supprimer une tâche

Regardez ici attentivement, j'ai ajouté 3 lignes de code à l'intérieur de la fonction.

- La première ligne supprimera l'élément HTML de l'écran,
- la deuxième ligne supprimera la tâche ciblée du tableau de données,
- et la troisième ligne mettra à jour le stockage local avec les nouvelles données.

```js
let deleteTask = (e) => {
  e.parentElement.parentElement.remove();

  data.splice(e.parentElement.parentElement.id, 1);

  localStorage.setItem("data", JSON.stringify(data));

  console.log(data);
};
```

Maintenant, créez une tâche factice et essayez de la supprimer. Le résultat jusqu'à présent ressemble à ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0qv50ozqjp239ldg0g21.gif)

#### Fonction pour modifier les tâches

Regardez ici attentivement, j'ai ajouté 5 lignes de code à l'intérieur de la fonction.

- La ligne 1 cible la tâche que nous avons sélectionnée pour modifier
- Les lignes 2, 3 et 4, ciblent les valeurs [tâche, date, description] de la tâche que nous avons sélectionnée pour modifier
- la ligne 5 exécute la fonction de suppression pour supprimer les données sélectionnées à la fois du stockage local, de l'élément HTML et du tableau de données.

```js
let editTask = (e) => {
  let selectedTask = e.parentElement.parentElement;

  textInput.value = selectedTask.children[0].innerHTML;
  dateInput.value = selectedTask.children[1].innerHTML;
  textarea.value = selectedTask.children[2].innerHTML;

  deleteTask(e);
};
```

Maintenant, essayez de créer une tâche factice et de la modifier. Le résultat jusqu'à présent : 👍

![Modification d'une tâche](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nbxn7c7rs33chuafjca9.gif)

#### Comment obtenir des données du stockage local

Si vous actualisez la page, vous remarquerez que toutes vos données ont disparu. Afin de résoudre ce problème, nous exécutons une IIFE (Immediately invoked function expression) pour récupérer les données du stockage local. Suivez ici : 👍

```js
(() => {
  data = JSON.parse(localStorage.getItem("data")) || [];
  console.log(data);
  createTasks();
})();
```

Maintenant, les données s'afficheront même si vous actualisez la page.

## Conclusion
![Félicitations](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0tenojs64uefxutl7ysn.png)

Félicitations pour avoir réussi à terminer ce tutoriel. Vous avez appris à créer une application de liste de tâches en utilisant les opérations CRUD. Maintenant, vous pouvez créer votre propre application CRUD en utilisant ce tutoriel.

Voici votre médaille pour avoir lu jusqu'à la fin. ❤️

## Suggestions et critiques sont grandement appréciées ❤️

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

- [LinkedIn/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)
- [YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)
- [Twitter / JoyShaheb](https://twitter.com/JoyShaheb)
- [Instagram / JoyShaheb](https://www.instagram.com/joyshaheb/)