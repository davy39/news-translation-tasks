---
title: Comment fonctionne le DOM JavaScript – Un tutoriel pratique
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2022-09-12T20:19:15.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-dom-a-practical-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/DOMpract-2-.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne le DOM JavaScript – Un tutoriel pratique
seo_desc: 'If you were listening to music on an app and you wanted to pause or skip
  a song, you''d have to do that through the app.

  This process is similar to how the Document Object Model or DOM works. Here, the
  music app represents the DOM because it serves as...'
---

Si vous écoutiez de la musique sur une application et que vous souhaitiez mettre en pause ou passer une chanson, vous devriez le faire via l'application.

Ce processus est similaire à la manière dont fonctionne le Document Object Model ou DOM. Ici, l'application musicale représente le DOM car elle sert de moyen pour apporter des modifications à la musique.

Dans ce tutoriel, vous apprendrez ce qu'est le DOM et comment il fonctionne de manière pratique.

## Qu'est-ce que le DOM ?

Le DOM est une API Web qui permet aux développeurs d'utiliser une logique de programmation pour apporter des modifications à leur code HTML. C'est une manière fiable d'apporter des modifications qui transforment les sites web statiques en sites dynamiques.

C'est un sujet important dans le développement web car le DOM sert de première utilisation de JavaScript dans le navigateur.

Le code HTML n'est pas considéré comme faisant partie du DOM tant qu'il n'est pas analysé par le navigateur. Pour voir ce qui arrive à votre code HTML lorsque cette analyse se produit, copiez votre code à partir de la balise **`<body>`** et collez-le [ici](https://software.hixie.ch/utilities/js/live-dom-viewer/) (dans la boîte avec le titre 'Markup to test' après les trois points).

## Que construisons-nous ?

Dans cet article, nous allons apprendre les parties les plus importantes et souvent utilisées du DOM en construisant ce projet simple :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/domProject-1.gif)

Découvrez-le sur CodePen [ici](https://codepen.io/ophyboamah/pen/bGMdbve).

## Fonctionnalités du projet

Comme vous pouvez le voir dans la démonstration du projet ci-dessus, voici les fonctionnalités que nous allons implémenter :

1. **Changement dynamique de couleur** : Lorsqu'une couleur est cliquée, la couleur de l'image de la voiture, du bouton addToCart et de l'étiquette changent pour correspondre à la couleur sélectionnée.
2. **Changement de bouton** : Cliquer sur le bouton addToCart révèle le bouton de succès et vice versa.

## Prérequis

* Connaissance de base du HTML et du CSS.
* Connaissance de base du JavaScript
* Un IDE (éditeur de texte)
* Un navigateur web

**NB** : Comme l'objectif de l'article est d'apprendre JavaScript et le DOM, nous ne mettrons pas l'accent sur le code HTML et CSS. Nous allons simplement les parcourir rapidement pour que vous puissiez configurer l'application. Ensuite, nous plongerons dans l'apprentissage du DOM.

## Code HTML :

Dans notre fichier `index.html`, nous allons créer la structure de base du projet qui inclut la liaison de notre fichier CSS, Font Awesome et Google Fonts – tout cela dans notre balise `<head>`. Dans notre balise `<body>`, nous allons créer notre carte de produit et lier notre balise JavaScript à la fin de la balise `<body>`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css"
      integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css" />
    <title>DOM Pratique</title>
  </head>
  <body>
    <div class="product-card">
      <div class="product-image">
        <!-- <img src="./img/gray-benz.jpg" alt="cars" /> -->
      </div>
      <div class="product-description">
        <h3 class="tag">VOITURE</h3>
        <h1 class="product-title">Mercedes Benz c300 2022</h1>
        <p class="product-details">
          <span class="mileage">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-car"></i
            ></span>
            Kilométrage : 4 000 miles
          </span>
          <span class="fuel">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-gas-pump"></i
            ></span>
            Carburant : 25mpg
          </span>
          <span class="safety">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-shield"></i></span
            >Sécurité :
            <span class="stars">
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
            </span>
          </span>
        </p>
        <p>Choisissez une couleur :</p>
        <div class="colors-price">
          <div class="colors">
            <span class="red"></span>
            <span class="gray"></span>
            <span class="black"></span>
          </div>
          <div class="pricing">
            <h2 class="new-price">134 450 $</h2>
            <h4 class="old-price"><s>140 500 $</s></h4>
          </div>
        </div>
        <button id="button">
          <span style="font-size: 1em; color: white">
            <i class="fa-solid fa-cart-shopping"></i>
          </span>
          <span class="button-text">Ajouter au panier</span>
        </button>
        <button class="feedback">
          <span id="white-button"
            >😃 Ouahou, vous êtes sur le point de posséder une Mercedes 🎊</span
          >
        </button>
      </div>
    </div>
    <script src="app.js"></script>
  </body>
</html>
```

## Code CSS : 

Dans notre fichier `style.css`, nous allons d'abord définir nos styles généraux comme ceci :

```css
* {
  font-family: "Poppins", sans-serif;
}

body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow-y: hidden;
  background-color: antiquewhite;
}

```

Ensuite, nous allons styliser notre produit, en commençant par l'étiquette, l'image, la description et les détails.

```css
/* étiquette du produit */
.tag {
  font-size: 0.9rem;
  background-color: black;
  border-radius: 5px;
  width: 4rem;
  display: flex;
  justify-content: center;
  color: #fff;
}

/* produit*/
.product-title {
  font-size: 2rem;
  font-weight: 700;
}

.product-card {
  background: #fff;
  display: grid;
  /* align-items: center; */
  grid-template-rows: 55% 45%;
  height: 80%;
  width: 30%;
  box-shadow: 10px 10px 25px 0px #3c3c3c;
}

.product-image {
  /* border: 2px solid black; */
  background-image: url("./img/black-benz.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 40px 10px;
  width: 28rem;
  height: 66%;
}

.product-description {
  background-color: #62c256;
  color: #fff;
  padding-left: 20px;
  margin-top: -67px;
}

.product-details {
  display: flex;
  flex-direction: column;
  margin-top: -20px;
}

.product-image img {
  width: 28rem;
}

.stars {
  color: yellow;
  font-size: 1em;
}
```

Ensuite, nous allons styliser nos couleurs : leurs prix, les couleurs en tant que groupe, et les couleurs individuelles.

```css
/* couleurs */
.colors-price {
  display: flex;
  align-items: center;
  width: 70%;
  justify-content: space-between;
  margin-top: -15px;
}

.colors {
  display: flex;
  width: 6rem;
  justify-content: space-between;
  cursor: pointer;
}

.red {
  background: red;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.gray {
  background: gray;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.black {
  background: black;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.pricing {
  display: flex;
  width: 12rem;
  justify-content: space-between;
  align-items: center;
}

.old-price {
  font-weight: 100;
}

```

Enfin, nous allons styliser nos boutons avec ce code :

```css
/* boutons */
button {
  cursor: pointer;
}

#button {
  background-color: #000;
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
}

button white-button {
  background-color: #fff;
}

.button-text {
  color: #fff;
  margin-left: 5px;
}

.feedback {
  display: none;
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
}

```

## Implémentation du DOM

Tout dans le DOM tombe dans l'une de ces deux catégories : sélectionner des éléments et manipuler des éléments. Après avoir créé nos fichiers HTML et CSS, nous nous dirigeons vers notre fichier `app.js` pour implémenter ce qui suit :

1. **Sélectionner** : Nous référençons tous les éléments que nous voulons rendre dynamiques à partir de notre code HTML et nous leur attribuons des variables dans notre fichier JavaScript.
2. **Manipuler** : Une fois que nous avons sélectionné et lié les variables, nous créons les diverses fonctions responsables des manipulations et nous les lions ensuite aux variables.

## Comment sélectionner des éléments dans le DOM

Pour accéder aux éléments HTML que vous souhaitez manipuler, vous devez rendre JavaScript conscient que de tels éléments existent. C'est ce qu'on appelle généralement la "sélection" d'éléments – les lier essentiellement.

Dans le DOM, il n'y a pas une seule manière de localiser et de référencer un élément pour le manipuler. Au lieu de cela, cela dépendra du [sélecteur](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) que vous avez utilisé dans la balise de l'élément.

Vous faites cela en attribuant l'élément à une variable. Cela prend le format suivant. Gardez à l'esprit que _tous les sélecteurs DOM sont précédés de l'objet document et d'un point_ :

```javascript
const example = document.[DOMselector]
```

Dans notre fichier JavaScript, nous devons sélectionner tous les éléments que nous voulons manipuler tels que le bouton, les couleurs, la carte d'image et l'étiquette.

Nous allons utiliser autant de sélecteurs DOM que possible, alors apprenons-en plus à leur sujet.

### Comment utiliser `querySelector`

`querySelector` est une méthode qui accepte le sélecteur CSS exact dans une chaîne et retourne un élément. Vous pouvez l'utiliser pour sélectionner les couleurs rouge et noire ainsi que la carte d'image, en utilisant leurs noms de classe.

Si vous souhaitiez utiliser cette approche pour sélectionner et retourner plus d'un élément, vous pouvez utiliser **`QuerySelectorAll`** à la place.

```javascript
const redColor = document.querySelector(".red");
```

Le code ci-dessus lie le span avec la classe "red" `<span class="red"></span>` de notre code HTML à la variable redColor dans notre JavaScript.

```javascript
const blackColor = document.querySelector(".black");

```

Le code ci-dessus lie le span avec la classe "black" `<span class="black"></span>` de notre code HTML à la variable blackColor dans notre JavaScript.

```javascript
const imageCard = document.querySelector(".product-image");
```

Le code ci-dessus lie le div avec la classe "product-image" `<div class="product-image">` de notre code HTML à la variable imageCard dans notre JavaScript.

```javascript
const feedbackBtn = document.querySelector(".feedback");
```

Le code ci-dessus lie le bouton avec la classe "feedback" `<button class="feedback">` de notre code HTML à la variable feedbackBtn dans notre JavaScript.

### Comment utiliser `getElementsByClassName`

Vous pouvez utiliser ce sélecteur pour sélectionner la couleur grise. Il est très similaire au `querySelector`. La seule différence est que cette méthode accepte simplement le nom de la classe, sans le point précédent (.)

```javascript
const grayColor = document.getElementsByClassName("gray");
```

Le code ci-dessus lie le span avec la classe "gray" `<span class="gray"></span>` de notre code HTML à la variable grayColor dans notre JavaScript.

### Comment utiliser `getElementById`

Vous pouvez utiliser ce sélecteur pour sélectionner le bouton du panier. Il est très similaire au `getElementsByClassName`. La seule différence est que, parce que nous utilisons l'ID pour montrer l'unicité, il est utilisé sur un seul élément. Cette méthode se lit getElement, _sans le s_.

```javascript
const cartButton = document.getElementById("button");
```

Le code ci-dessus lie le bouton avec l'id "button" `<button id="button">` de notre code HTML à la variable cartButton dans notre JavaScript.

### Comment utiliser `GetElementsByTagName`

Les attributs ne sont pas les seuls moyens de sélectionner un élément. Vous pouvez également utiliser les noms de balise. Si vous avez utilisé la balise que vous ciblez plus d'une fois, alors elle retournera une liste d'éléments. Utilisez l'indexation pour sélectionner le bon.

```javascript
const itemTag = document.getElementsByTagName("h3")[0];
```

Le code ci-dessus lie le h3 qui contient notre étiquette de produit `<h3 class="tag">` de notre code HTML à la variable itemTag dans notre JavaScript.

De tous ceux-ci, querySelector et querySelectorAll sont probablement les plus populaires en raison de leur généralité et de leur moindre restriction.

## Comment manipuler des éléments dans le DOM

La manipulation est le but principal du DOM. C'est tout ce qui se passe après que vous avez référencé et sélectionné le ou les éléments avec lesquels vous souhaitez travailler. Cela conduit à un changement dans l'état de l'élément, de statique à dynamique.

Deux concepts que vous devez connaître pour comprendre la manipulation du DOM sont les **événements** et les **gestionnaires**.

### Qu'est-ce que les événements ?

Utilisons la même analogie musicale que précédemment. Sur l'application musicale, vous devez effectuer une action [cliquer ou balayer] avant que les fonctionnalités ne se déclenchent.

Dans le DOM, cette action est connue sous le nom d'événement. Il existe des événements tels que clic, défilement, survol de souris, changement, et plus encore.

Dans le DOM, les réponses sont liées à chaque événement. Cela signifie qu'il doit y avoir une veille de l'événement afin de donner une réponse. Cela est connu sous le nom d'**écouteur d'événement**. Les écouteurs d'événements se présentent généralement sous la forme d'une méthode `addEventListener` qui prend deux arguments (événement, gestionnaire d'événement).

#### Anatomie d'un événement

Les événements DOM contiennent normalement un élément, son écouteur d'événement et une fonction.

```
élément.[méthodeÉcouteurÉvénement(événement, gestionnaireÉvénement)
```

### Qu'est-ce que les gestionnaires d'événements ?

Les gestionnaires d'événements sont les réponses qui sont déclenchées lorsque nos méthodes d'écouteur d'événement lisent un événement. Sans gestionnaires d'événements, il n'y aurait aucun moyen d'alerter notre code qu'un événement s'est produit.

Toutes les modifications qui se produisent dans le DOM, telles que le style, l'ajout, la suppression, etc., dépendent des gestionnaires d'événements. Ce sont les fonctions trouvées dans le deuxième argument d'une méthode **addEventListener**. Elles sont toujours prêtes à s'exécuter dès que l'événement (premier argument) se produit.

```javascript
redColor.addEventListener("click", function () {
  cartButton.style.backgroundColor = "red";
  itemTag.style.backgroundColor = "red";
  imageCard.style.backgroundImage = 'url("./img/red-benz.webp")';
});
```

Dans le code ci-dessus, la fonction après l'événement 'click' est le gestionnaire d'événement. Cela signifie que tout ce qui se trouve dans cette fonction sera implémenté dès que la couleur rouge est cliquée.

## Comment implémenter des événements et des gestionnaires d'événements

Dans ce projet, nous allons utiliser des événements et des gestionnaires d'événements pour environ 5 implémentations. Nous allons passer en revue chacune d'elles maintenant.

Tout d'abord, nous allons les utiliser pour **rendre la couleur rouge fonctionnelle**. Une fois qu'un utilisateur clique sur la couleur rouge, le bouton du panier et l'étiquette de l'article se voient attribuer des styles sous la forme d'une couleur de fond rouge. La carte d'image se voit également attribuer une image de fond rouge.

Nous faisons cela en prenant la variable `redColor` et en ajoutant un écouteur d'événement de 'click'. Cela signifie que nous voulons que notre code soit alerté lorsque la couleur rouge est cliquée. En retour, le gestionnaire d'événement `function` est en place pour s'exécuter immédiatement.

```javascript
redColor.addEventListener("click", function () {
  cartButton.style.backgroundColor = "red";
  itemTag.style.backgroundColor = "red";
  imageCard.style.backgroundImage = 'url("./img/red-benz.webp")';
});
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/redColor-1.gif)
_Aperçu de la couleur rouge_

Ensuite, nous allons **rendre la couleur grise fonctionnelle**. Lorsque l'utilisateur clique sur la couleur grise, le bouton du panier et l'étiquette de l'article se voient attribuer des styles sous la forme d'une couleur de fond grise. La carte d'image se voit également attribuer une image de fond grise.

Nous faisons cela en prenant la variable `grayColor` et en ajoutant un écouteur d'événement de 'click'. Cela signifie que nous voulons que notre code soit alerté lorsque la couleur grise est cliquée. En retour, le gestionnaire d'événement `function` est en place pour s'exécuter immédiatement.

```javascript
grayColor[0].addEventListener("click", function () {
  cartButton.style.backgroundColor = "gray";
  itemTag.style.backgroundColor = "gray";
  imageCard.style.backgroundImage = 'url("./img/gray-benz.jpg")';
});
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/grayColor-1.gif)
_Aperçu de la couleur grise_

Ensuite, nous allons **rendre la couleur noire fonctionnelle**. Lorsque l'utilisateur clique sur la couleur noire, le bouton du panier et l'étiquette de l'article se voient attribuer des styles sous la forme d'une couleur de fond noire. La carte d'image se voit également attribuer une image de fond noire.

Nous faisons cela en prenant la variable `blackColor` et en ajoutant un écouteur d'événement de 'click'. Cela signifie que nous voulons que notre code soit alerté lorsque la couleur noire est cliquée. En retour, le gestionnaire d'événement `function` est en place pour s'exécuter immédiatement.

```javascript
blackColor.addEventListener("click", function () {
  cartButton.style.backgroundColor = "black";
  itemTag.style.backgroundColor = "black";
  imageCard.style.backgroundImage = 'url("./img/black-benz.jpg")';
});
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/blackColor-1.gif)
_Aperçu de la couleur noire_

Nous avons examiné une approche des gestionnaires d'événements, qui consiste à créer la fonction dans la méthode addEventListener.

Une autre approche consiste à créer une fonction avant de passer le nom de la fonction en tant qu'argument dans la méthode addEventListener.

### Comment implémenter le bouton du panier

Nous commençons par créer une fonction nommée cart. La fonction cart masque le bouton du panier et affiche le bouton de feedback. Le nom de la fonction cart est ensuite passé à la méthode de l'écouteur d'événement en tant que deuxième argument.

```javascript
const cart = () => {
  cartButton.style.display = "none";
  feedbackBtn.style.display = "block";
};
cartButton.addEventListener("click", cart);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/cartButton.gif)
_Aperçu du bouton du panier_

### Comment implémenter le bouton de feedback

Nous créons d'abord une fonction nommée feedback. La fonction feedback masque le bouton de feedback et affiche le bouton du panier. Le nom de la fonction feedback est ensuite passé à la méthode de l'écouteur d'événement en tant que deuxième argument.

```javascript
const feedback = () => {
  cartButton.style.display = "block";
  feedbackBtn.style.display = "none";
};
feedbackBtn.addEventListener("click", feedback);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/feedbackButton.gif)
_Aperçu du bouton de feedback_

## Code complet du projet

Voici le projet que nous avons construit ensemble dans cet article :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/domProject-2.gif)

Voici le code HTML complet :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css"
      integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css" />
    <title>DOM Pratique</title>
  </head>
  <body>
    <div class="product-card">
      <div class="product-image">
        <!-- <img src="./img/gray-benz.jpg" alt="cars" /> -->
      </div>
      <div class="product-description">
        <h3 class="tag">VOITURE</h3>
        <h1 class="product-title">Mercedes Benz c300 2022</h1>
        <p class="product-details">
          <span class="mileage">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-car"></i
            ></span>
            Kilométrage : 4 000 miles
          </span>
          <span class="fuel">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-gas-pump"></i
            ></span>
            Carburant : 25mpg
          </span>
          <span class="safety">
            <span style="font-size: 1em; color: black"
              ><i class="fa-solid fa-shield"></i></span
            >Sécurité :
            <span class="stars">
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
            </span>
          </span>
        </p>
        <p>Choisissez une couleur :</p>
        <div class="colors-price">
          <div class="colors">
            <span class="red"></span>
            <span class="gray"></span>
            <span class="black"></span>
          </div>
          <div class="pricing">
            <h2 class="new-price">134 450 $</h2>
            <h4 class="old-price"><s>140 500 $</s></h4>
          </div>
        </div>
        <button id="button">
          <span style="font-size: 1em; color: white">
            <i class="fa-solid fa-cart-shopping"></i>
          </span>
          <span class="button-text">Ajouter au panier</span>
        </button>
        <button class="feedback">
          <span id="white-button"
            >😃 Ouahou, vous êtes sur le point de posséder une Mercedes 🎊</span
          >
        </button>
      </div>
    </div>
    <script src="app.js"></script>
  </body>
</html>

```

Voici le CSS :

```css
* {
  font-family: "Poppins", sans-serif;
}

body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow-y: hidden;
  background-color: antiquewhite;
}

/* étiquette du produit */
.tag {
  font-size: 0.9rem;
  background-color: black;
  border-radius: 5px;
  width: 4rem;
  display: flex;
  justify-content: center;
  color: #fff;
}

/* produit*/
.product-title {
  font-size: 2rem;
  font-weight: 700;
}

.product-card {
  background: #fff;
  display: grid;
  /* align-items: center; */
  grid-template-rows: 55% 45%;
  height: 80%;
  width: 30%;
  box-shadow: 10px 10px 25px 0px #3c3c3c;
}

.product-image {
  /* border: 2px solid black; */
  background-image: url("./img/black-benz.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 40px 10px;
  width: 28rem;
  height: 66%;
}

.product-description {
  background-color: #62c256;
  color: #fff;
  padding-left: 20px;
  margin-top: -67px;
}

.product-details {
  display: flex;
  flex-direction: column;
  margin-top: -20px;
}

.product-image img {
  width: 28rem;
}

.stars {
  color: yellow;
  font-size: 1em;
}

/* couleurs */
.colors-price {
  display: flex;
  align-items: center;
  width: 70%;
  justify-content: space-between;
  margin-top: -15px;
}

.colors {
  display: flex;
  width: 6rem;
  justify-content: space-between;
  cursor: pointer;
}

.red {
  background: red;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.gray {
  background: gray;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.black {
  background: black;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.pricing {
  display: flex;
  width: 12rem;
  justify-content: space-between;
  align-items: center;
}

.old-price {
  font-weight: 100;
}

/* boutons */
button {
  cursor: pointer;
}

#button {
  background-color: #000;
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
}

button white-button {
  background-color: #fff;
}

.button-text {
  color: #fff;
  margin-left: 5px;
}

.feedback {
  display: none;
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
}

```

Voici le code JavaScript :

```javascript
// 1. Changer la couleur de la voiture et la couleur du bouton addToCart lorsqu'une couleur est sélectionnée
// - Sélection des éléments
const redColor = document.querySelector(".red");
const grayColor = document.getElementsByClassName("gray");
const blackColor = document.querySelector(".black");
const cartButton = document.getElementById("button");
const itemTag = document.getElementsByTagName("h3")[0];
const imageCard = document.querySelector(".product-image");
const feedbackBtn = document.querySelector(".feedback");

// Modification des éléments
// - Ajout des écouteurs d'événements
// - Couleur rouge
redColor.addEventListener("click", function () {
  cartButton.style.backgroundColor = "red";
  itemTag.style.backgroundColor = "red";
  imageCard.style.backgroundImage = 'url("./img/red-benz.webp")';
});

// - Couleur grise
grayColor[0].addEventListener("click", function () {
  cartButton.style.backgroundColor = "gray";
  itemTag.style.backgroundColor = "gray";
  imageCard.style.backgroundImage = 'url("./img/gray-benz.jpg")';
});

// - Couleur noire
blackColor.addEventListener("click", function () {
  cartButton.style.backgroundColor = "black";
  itemTag.style.backgroundColor = "black";
  imageCard.style.backgroundImage = 'url("./img/black-benz.jpg")';
});

// Implémentation du clic sur le bouton
// - Bouton du panier
const cart = () => {
  cartButton.style.display = "none";
  feedbackBtn.style.display = "block";
};
cartButton.addEventListener("click", cart);

// - Bouton de feedback
const feedback = () => {
  cartButton.style.display = "block";
  feedbackBtn.style.display = "none";
};
feedbackBtn.addEventListener("click", feedback);

```

# Conclusion

Le DOM est une partie essentielle du développement web moderne car il aide les développeurs à transformer les sites web et les applications web de statiques en dynamiques.

En tant que débutant, il peut être assez difficile de comprendre le DOM et tout ce qu'il implique. Prendre le temps de construire quelques projets simples comme celui-ci vous aidera à renforcer les concepts.

Merci d'avoir lu 👋🏾. J'espère que vous l'avez trouvé utile.