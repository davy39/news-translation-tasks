---
title: Apprendre la Validation de Formulaire JavaScript – Construire un Projet JS
  pour Débutants ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-09-22T18:33:54.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-form-validation-by-making-a-form
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Frame-31.png
tags:
- name: Form validations
  slug: form-validations
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Apprendre la Validation de Formulaire JavaScript – Construire un Projet
  JS pour Débutants ✨
seo_desc: "Today we're going to learn how to do form validation in JavaScript. We'l\
  \ also add images and media queries to build out the entire project and keep it\
  \ as a portfolio.  \nHere's the project demo that we're gonna build \U0001F447\n\
  \nDesktop design\nHere's a small ..."
---

Aujourd'hui, nous allons apprendre comment faire de la **validation de formulaire** en JavaScript. Nous ajouterons également des images et des requêtes média pour construire l'ensemble du projet et le garder comme **portfolio**.  

Voici la démonstration du projet que nous allons construire 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-30--1-.png)
_**Design desktop**_

Voici un petit échantillon de comment le formulaire fonctionnera 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dvdfvdf-1.gif)
_**Échantillon du projet**_

## **Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :**

%[https://youtu.be/VufN46OyFng]

## Code source

Vous pouvez obtenir le code source, y compris les images, à partir d'ici :

* [CodePen](https://codepen.io/joyshaheb/pen/XWgdOyY)
* [GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Form-Validation)

# Comment installer le projet

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-1--1-.png)

Suivez ces étapes pour configurer notre projet : 👋

* Créez un nouveau dossier nommé "Projet" et ouvrez VS Code
* Créez les fichiers index.html, style.css et main.js
* Liez les fichiers à l'intérieur du HTML
* Téléchargez les [images depuis mon dépôt GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Form-Validation)
* Collez ce lien font-awesome à l'intérieur de la balise head. Ensuite, nous pourrons accéder aux icônes Font Awesome 👋👋

```html
<link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
      crossorigin="anonymous"
    />
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-2--1-.png)

# Voici ce que nous allons couvrir :

* Écrire le HTML
* Ajouter le CSS
* Écrire le JavaScript
* Ajouter un bouton de médias sociaux
* Ajouter les images
* Requêtes média pour la version mobile (responsive)

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-20--2-.png)
_**Table des matières**_

# Comment écrire le HTML

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-3.png)

Créez une classe nommée `.container` à l'intérieur de la balise body et hébergez la balise form qui aura un id de form 👋

```html
<div class="container">

	<form id="form"></form>
    
</div>
```

Et à l'intérieur de la balise form, créez 4 `div`, comme ceci 👋

```html
<form id="form">

    <div class="title">Commencer</div>
    
    <div></div>
    <div></div>
    <div></div>
    
</form>
```

À l'intérieur de ces 3 balises div vides, créons 3 inputs [Nom d'utilisateur, Email et Mot de passe] ainsi que les icônes et les labels.

**Note** : nous créons un nom de classe `.error`. Nous allons injecter le message d'erreur ici en utilisant JavaScript. 

#### Input Nom d'utilisateur

```html
<!-- Input Nom d'utilisateur -->
        
<div>
	<label for="username">Nom d'utilisateur</label>
    <i class="fas fa-user"></i>
    
    <input
        type="text"
        name="username"
        id="username"
        placeholder="Joy Shaheb"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### Input Email

```html
<!-- Input Email -->
        
<div>
	<label for="email">Email</label>
    <i class="far fa-envelope"></i>
    
    <input
        type="email"
        name="email"
        id="email"
        placeholder="abc@gmail.com"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### Input Mot de passe

```html
<!-- Input Mot de passe -->
        
<div>
	<label for="password">Mot de passe</label>
    <i class="fas fa-lock"></i>
    
    <input
        type="password"
        name="password"
        id="password"
        placeholder="Mot de passe ici"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### Comment faire le bouton

Enfin, ajoutez le bouton avant la balise de fermeture du formulaire comme ceci :

```html
<form>
    <!-- autres codes sont ici -->
    
    <button id="btn" type="submit">Soumettre</button>
    
</form>
```

Voici le résultat jusqu'à présent 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdgdfgdfdffcvb.png)
_**Résultat jusqu'à présent**_

Félicitations pour avoir terminé la partie HTML ! 🎾🎉👨🏽‍💻

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-7.png)

# Comment ajouter le CSS

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-4.png)

Ajoutons le CSS pour styliser notre formulaire. D'abord, supprimons les styles par défaut de notre navigateur, y compris la font-family 👋

```css
/**
* ! modification des styles par défaut du navigateur
**/

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: sans-serif;
}
```

Maintenant, appliquez ces styles pour la balise form :

```css
/**
* ! règles de style pour la section form
**/

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 400px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  padding: 50px;
}
```

Ensuite, apportez ces modifications pour notre texte de titre : 👋👋

```css
.title {
  font-size: 25px;
  font-weight: bold;
  margin-bottom: 20px;
}
```

Votre résultat jusqu'à présent 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fsdfsdsfxvxcvxd.png)
_**Résultat jusqu'à présent**_

Maintenant, ajoutez une marge en bas de notre texte de label comme ceci :

```css
label {
  display: block;
  margin-bottom: 5px;
}
```

Et ajoutez ces styles pour changer l'apparence de nos balises input 👋👋

```css
form div input {
  width: 100%;
  height: 40px;
  border-radius: 8px;
  outline: none;
  border: 2px solid #c4c4c4;
  padding: 0 30px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

```

Ajoutez ce code pour ajouter un peu d'espace et des effets de changement de couleur :

```css
form div {
  position: relative;
  margin-bottom: 15px;
}

input:focus {
  border: 2px solid #f2796e;
}
```

Le résultat jusqu'à présent 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdfdfdfdfvdfv.png)
_**Résultat jusqu'à présent**_

## Comment styliser les icônes

Maintenant, nous allons styliser les icônes que nous avons importées depuis font-awesome. Suivez le code : ✨✨

```css
/**
* ! règles de style pour les icônes du formulaire
**/

form div i {
  position: absolute;
  padding: 10px;
}

```

Voici le résultat de l'ajout de ces deux lignes 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fddfvdfvdfvgfbh.png)
_**Résultat jusqu'à présent**_

Maintenant, ajoutez ces styles pour styliser la classe error, ainsi que les icônes de succès et d'échec 👋👋

```css
.failure-icon,
.error {
  color: red;
}

.success-icon {
  color: green;
}

.error {
  font-size: 14.5px;
  margin-top: 5px;
}
```

Voici le résultat jusqu'à présent 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ddsfsddsdscsfvv.png)
_**Résultat jusqu'à présent**_

Regardez, les icônes de succès et d'échec se chevauchent. Ne vous inquiétez pas, nous allons les manipuler en JavaScript. Pour l'instant, vous pouvez les cacher comme ceci 👋👋

```css
.success-icon,
.failure-icon {
  right: 0;
  opacity: 0;
}

```

Maintenant, stylisons notre bouton de soumission, comme ceci 👋

```css
/* Règles de style pour le bouton de soumission */

button {
  margin-top: 15px;
  width: 100%;
  height: 45px;
  background-color: #f2796e;
  border: 2px solid #f2796e;
  border-radius: 8px;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.1s ease;
}
```

Si vous voulez ajouter un effet de survol, alors oui, ajoutez ces styles 👋👋

```css
button:hover {
  opacity: 0.8;
}
```

# Prenez une pause !

Jusqu'à présent, tout va bien. Prenez une pause – vous le méritez.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-33.png)

# Comment ajouter le JavaScript

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-6.png)

Tout d'abord, nous devons cibler toutes nos classes et id depuis le HTML à l'intérieur du JavaScript. Pour accomplir cette tâche efficacement, créez ces deux fonctions 👋👋

```css
let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);
```

Ensuite, stockez les classes et id à l'intérieur de ces variables 👋

**Note** : Essayez de ne pas faire de fautes d'orthographe. Sinon, votre JavaScript ne fonctionnera pas.

```javascript
let username = id("username"),
  email = id("email"),
  password = id("password"),
  form = id("form"),
  
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");
```

Maintenant, nous allons cibler notre formulaire et ajouter l'écouteur d'événement **submit** 👋 

```css

form.addEventListener("submit", (e) => {
  e.preventDefault();
});

```

Maintenant, nous allons créer une fonction nommée engine qui effectuera tout type de travail de validation de formulaire pour nous. Elle aura trois arguments – suivez ici : 👋

```js
let engine = (id, serial, message) => {}
```

Les arguments représentent ce qui suit :

* `id` ciblera notre id
* `serial` ciblera nos classes [classe error, icônes de succès et d'échec]
* `message` imprimera un message à l'intérieur de notre classe .error 

Maintenant, créez une instruction `if, else` comme ceci 👋

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
  } 
  
  else {
  }
}
```

**Note** : **`id.value.trim()`** supprimera tous les espaces blancs supplémentaires de la valeur que l'utilisateur saisit. Vous pouvez vous faire une idée de son fonctionnement en regardant cette illustration 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-19-1.png)
_**trim() utilisé pour supprimer les espaces supplémentaires**_

Maintenant, regardons nos objectifs 👋

* Nous voulons que le JavaScript imprime un message à l'intérieur de la classe **error** chaque fois que l'utilisateur **soumet un formulaire vide**. En même temps, nous voulons que les icônes **failure** soient également mises en évidence. 
* Mais, si l'utilisateur **remplit tous les inputs** et le soumet, nous voulons que l'icône **success** soit visible.

Pour accomplir cela, écrivez cette logique 👋 pour imprimer le message :

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
  } 
  
  else {
    errorMsg[serial].innerHTML = "";
  }
}
```

Pour que les icônes fonctionnent correctement, ajoutez ce code : 👋👋

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
    id.style.border = "2px solid red";
    
    // icônes
    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
  } 
  
  else {
    errorMsg[serial].innerHTML = "";
    id.style.border = "2px solid green";
    
    // icônes
    failureIcon[serial].style.opacity = "0";
    successIcon[serial].style.opacity = "1";
  }
}
```

Il est temps d'implémenter notre fonction nouvellement créée. Écrivez ceci à l'endroit où nous avons ajouté l'écouteur d'événement submit 👋

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();

  engine(username, 0, "Le nom d'utilisateur ne peut pas être vide");
  engine(email, 1, "L'email ne peut pas être vide");
  engine(password, 2, "Le mot de passe ne peut pas être vide");
});
```

Ici, nous passons les noms d'id, les numéros de série de nos noms de classe et le message qui doit être imprimé lorsque nous trouvons une erreur lorsque l'utilisateur soumet le formulaire. 

Voici les résultats jusqu'à présent 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dvdfvdf.gif)
_**Le résultat jusqu'à présent**_

## Comment ajouter les boutons de médias sociaux

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-10.png)

Jusqu'à présent, tout va bien, ajoutons des options d'inscription via les médias sociaux. Suivez ici. 👋 

À l'intérieur de la balise form, créez une nouvelle `div` avec le nom de classe `social` :

```html
<form id="form">

    <div class="social">
    
      <div class="title">Commencer</div>
      
      <div class="question">
        Vous avez déjà un compte ? <br />
        <span>Connectez-vous</span>
      </div>

      <div class="btn"></div>

      <div class="or">Ou</div>
    </div>
    
    <!-- autres codes sont ici-->
</form>
```

À l'intérieur de la classe `.btn`, nous créons deux autres divs avec les noms de classe `.btn-1` et `.btn-2` avec les images et le texte également

```html
<div class="btn">
  <div class="btn-1">
     <img src="https://img.icons8.com/color/30/000000/google-logo.png" />
     S'inscrire
  </div>
  
  <div class="btn-2">
    <img src="https://img.icons8.com/ios-filled/30/ffffff/facebook-new.png" />
     S'inscrire
   </div>
</div>
```

Voici les résultats jusqu'à présent 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfvgdfdsfdsf.png)
_**Le résultat jusqu'à présent**_

Maintenant, stylisons d'abord `.btn-1` et `.btn-2`. Nous allons changer l'alignement des boutons en ligne depuis la colonne 👋

```css
/**
* ! règles de style pour la section sociale
**/

.btn {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 15px;
}
```

Voici à quoi cela ressemble maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfdfdfdbgf.png)
_**Le résultat jusqu'à présent**_

Maintenant, ajoutez des styles pour le bouton comme ceci : 👋

```css
.btn-1,
.btn-2 {
  padding: 10px 5px;
  width: 100%;
  display: flex;
  gap: 15px;
  justify-content: center;
  align-items: center;
  border: 2px solid #c4c4c4;
  border-radius: 8px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
```

Changez la couleur de l'icône et la couleur du texte de `.btn-2` comme ceci : 👋

```css
.btn-2 {
  background-color: #4f70b5;
  color: white;
}
```

Ensuite, apportez ces petites modifications pour améliorer l'apparence du composant :

```css
.or {
  text-align: center;
}

.question {
  font-size: 15px;
}

span {
  color: #f2796e;
  cursor: pointer;
}
```

Le résultat jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdfhgnmhg.png)
_**Résultat jusqu'à présent**_

## Comment ajouter les images 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-9.png)

Maintenant, ajoutons des images à notre projet. D'abord, écrivons le HTML 👋

```html
<div class="container">

      <div class="content">
        <div class="logo">
          <img src="https://svgshare.com/i/_go.svg" alt="" />
        </div>
        
        <div class="image"></div>
        
        <div class="text">
          Commencez gratuitement et obtenez <br />
          des offres attractives aujourd'hui !
        </div>  
      </div>
      
   <form id="form">
   <!-- autres codes sont ici -->
   </form>
   
</div>
```

Le résultat jusqu'à présent 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfghgjgjgytfh.png)
_**Résultat jusqu'à présent**_

Maintenant, nous devons changer l'orientation de notre contenu de colonne en ligne. Suivez ici 👋

```css
.container {
  display: flex;
  flex-direction: row;
}
```

Ajoutez ces règles de style pour la section de contenu :

```css
/**
* ! règles de style pour la section de contenu
**/

.content {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  background-color: #f2796e;
  width: 55%;
  min-height: 100vh;
  padding: 10px 20px;
}

form {
   width: 45%;
   max-width: none;
}
```

Le résultat jusqu'à présent 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dsffgythjy.png)
_**Résultat jusqu'à présent**_

Ajoutez l'illustration principale en CSS :

```css
.image {
  background-image: url("https://svgshare.com/i/_gZ.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  /* border: 2px solid black; */
  height: 65%;
}

```

Et ajoutez ces styles pour la classe `.text` :

```css
.text {
  text-align: center;
  color: white;
  font-size: 18px;
}

form {
   width: 45%;
   max-width: none;
}
```

Le résultat jusqu'à présent 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/wewrwerew.png)
_**Résultat jusqu'à présent**_

## Comment ajouter des requêtes média pour la version mobile

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-8.png)

Nous voulons rendre cela responsive. Nous allons donc ajouter des requêtes média pour nous aider avec cela.

Pour les écrans avec une largeur à partir de 900px, nous ajouterons ces styles. Suivez ici 👋👋

```css
@media (max-width: 900px) {
  .container {
    flex-direction: column;
  }

  form,
  .content {
    width: 100%;
  }

  .btn {
    flex-direction: column;
  }
  .image {
    height: 70vh;
  }
}
```

Pour les écrans avec une largeur à partir de 425px, nous apporterons ces modifications mineures 👋

```css
@media (max-width: 425px) {
  form {
    padding: 20px;
  }
}

```

Voici le résultat final 👋👋

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fgbgfnghnghnhgmjhgnmhgnggfbgfgfb.gif)
_**Le résultat final**_

# Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-5.png)
_**Félicitations !**_

Félicitations pour avoir lu jusqu'à la fin. Maintenant, vous pouvez facilement et efficacement utiliser JavaScript pour gérer la validation de formulaire. Non seulement cela, **vous avez également un projet à montrer à votre recruteur local !**

Voici votre médaille pour avoir lu jusqu'à la fin ❤️

### Suggestions & Critiques sont hautement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

* [**LinkedIn/ JoyShaheb**](https://www.linkedin.com/in/joyshaheb/)
* **[YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)**
* **[Twitter / JoyShaheb](https://twitter.com/JoyShaheb)**
* **[Instagram/ JoyShaheb](https://www.instagram.com/joyshaheb/)**