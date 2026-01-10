---
title: Comment créer une barre de navigation responsive avec un menu déroulant en
  utilisant JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-24T20:52:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-navigation-bar-with-dropdown-menu-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/responsive-navigation-bar-with-dropdown-menu-using-javascript.png
tags:
- name: JavaScript
  slug: javascript
- name: responsive design
  slug: responsive-design
seo_title: Comment créer une barre de navigation responsive avec un menu déroulant
  en utilisant JavaScript
seo_desc: 'By Victor Eke

  Navigation bars are essential components used a lot in websites and web apps. As
  a web developer, you will need to be able to customize them, either for a client
  project or a basic portfolio site.

  In this guide, you''ll learn how to buil...'
---

Par Victor Eke

Les barres de navigation sont des composants essentiels utilisés dans de nombreux sites web et applications web. En tant que développeur web, vous devrez être capable de les personnaliser, que ce soit pour un projet client ou un site portfolio basique.

Dans ce guide, vous apprendrez à créer une barre de navigation à partir de zéro en utilisant uniquement HTML, CSS et JavaScript. Vous apprendrez également à la rendre accessible.

Voici une capture d'écran de ce à quoi ressemblera cette barre de navigation :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/navigation-bar-final-result.jpg)
_Résultat final de la barre de navigation_

Ce design est inspiré de la [Minimal Navigation bar](https://dribbble.com/shots/17305696-Minimal-Navigation?utm_source=Clipboard_Shot&utm_campaign=tranmautritam&utm_content=Minimal%20Navigation&utm_medium=Social_Share&utm_source=Clipboard_Shot&utm_campaign=tranmautritam&utm_content=Minimal%20Navigation&utm_medium=Social_Share) de Tran Mau Tri Tam sur Dribbble.

## Étape 1 – Ajouter le balisage HTML

Pour des raisons de concision, nous utiliserons une bibliothèque d'icônes appelée [boxicons](https://github.com/atisawd/boxicons) pour importer certaines icônes pour cette barre de navigation. Je recommande vivement d'utiliser des SVGs en ligne à la place.

Pour utiliser cette bibliothèque, insérez le snippet ci-dessous dans l'en-tête de votre fichier HTML :

```html
<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
```

Le balisage est divisé en trois parties principales :

1. Un élément `div` avec une classe `nav-start`
2. Un autre élément `div` avec une classe `nav-end`
3. Un élément `button` avec un id `hamburger`

Tous ces éléments seront enfermés dans une balise `header`. Pour mieux expliquer cela, copiez le balisage ci-dessous et je vous expliquerai ce qui se passe après.

```html
<header id="nav-menu">
  <div class="container">
    <div class="nav-start">
      <a class="logo" href="/">
        <img src="https://github.com/Evavic44/responsive-navbar-with-dropdown/blob/main/assets/images/logo.png?raw=true" 
             width="35" 
             height="35" 
             alt="Inc Logo"
          />
      </a>
      <nav class="menu"></nav>
    </div>

    <div class="nav-end">
      <div class="right-container">
        <form class="search" role="search">
          <input type="search" name="search" placeholder="Rechercher" />
          <i class="bx bx-search" aria-hidden="true"></i>
        </form>

        <a href="#profile">
          <img src="https://github.com/Evavic44/responsive-navbar-with-dropdown/blob/main/assets/images/user.jpg?raw=true" 
               width="30" 
               height="30" 
               alt="image utilisateur" 
            />
        </a>
        <button class="btn btn-primary">Créer</button>
      </div>
    </div>
  </div>
</header>
```

Pour le nav-start, nous avons les éléments suivants :

* Un élément `<img>` pour le logo enveloppé dans une balise d'ancrage `<a>`.
* Un élément `<nav>` avec une classe `menu` qui contiendra tous les liens de navigation. Nous définirons ces liens plus tard en utilisant une combinaison de balises `<ul>`, `li>` et `<a>`.

Le nav-end contient les éléments suivants :

* Un élément `<form>` avec un rôle de recherche qui contient une entrée de recherche et une icône de recherche.
* Un élément bouton avec une classe `btn`. Nous utiliserons cette classe pour styliser le bouton.

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/markup-elements-broken-down-into-three-main-parts-1.png)

### Menu de navigation

Le menu de navigation `<nav>` est l'endroit où se trouveront les liens de navigation. Remplacez l'élément `nav` que vous avez ajouté précédemment par ce balisage ci-dessous :

```html
<nav class="menu">
    <button id="hamburger" aria-expanded="false">
      <i class="bx bx-menu" aria-hidden="true"></i>
    </button>
    <div class="menu">
        <ul class="menu-bar">
            <li>
                <button 
                  class="nav-link dropdown-btn" 
                  data-dropdown="dropdown1" 
                  aria-expanded="false">
                    Parcourir
                  <i class="bx bx-chevron-down" aria-hidden="true"></i>
                </button>
                <div id="dropdown1" class="dropdown"></div>
            </li>
            <li>
                <button 
                  class="nav-link dropdown-btn" 
                  data-dropdown="dropdown2" 
                  aria-expanded="false">
                    Découvrir
                  <i class="bx bx-chevron-down" aria-hidden="true"></i>
                </button>
                <div id="dropdown2" class="dropdown"></div>
            </li>
            <li><a class="nav-link" href="/">Emplois</a></li>
            <li><a class="nav-link" href="/">Livestream</a></li>
            <li><a class="nav-link" href="/">À propos</a></li>
        </ul>
    </div>
</nav>
```

Ici, vous avez une balise `nav` qui contient un bouton et une liste non ordonnée de cinq éléments `li` représentant chaque élément du menu de navigation : **parcourir, découvrir, emplois, livestream,** et **à propos**.

Le bouton sert de menu hamburger et est un bouton avec un id et `aria-expanded` défini sur "false". L'attribut `aria-expanded` nous permettra de rendre ce bouton plus accessible aux lecteurs d'écran.

Les deux premiers éléments de la liste, **parcourir** et **découvrir**, sont des éléments `button` et seront utilisés pour basculer leur menu déroulant individuel. Les éléments restants **Emplois, livestream**, et **à propos**, sont simplement des liens réguliers.

Avec le code jusqu'à présent, votre résultat devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Navigation-markup-with-links-and-popup-buttons.png)

### Élément déroulant

Ensuite, définissons l'élément déroulant pour chaque bouton de navigation. Voici le balisage pour le premier menu déroulant. Remplacez le premier élément `li` dans votre balisage par ceci :

```html
<!-- balisage tronqué pour plus de concision-->
<li>
    <button
      class="nav-link dropdown-btn"
      data-dropdown="dropdown1"
      aria-expanded="false"
    >
      Parcourir
      <i class="bx bx-chevron-down" aria-hidden="true"></i>
    </button>
    <div id="dropdown1" class="dropdown">
      <ul>
        <li>
          <a class="dropdown-link" href="#best-of-the-day">
            <img src="./assets/icons/botd.svg" class="icon" alt=""/>
            <div>
              <span class="dropdown-link-title"
                >Meilleur du jour</span
              >
              <p>Courts métrages présentés aujourd'hui par les conservateurs</p>
            </div>
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#featured-streams">
            <img src="./assets/icons/fs.svg" class="icon" alt=""/>
            <div>
              <span class="dropdown-link-title"
                >Streams en vedette</span
              >
              <p>Livestreams des créatifs de premier plan</p>
            </div>
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#subscriptions">
            <img src="./assets/icons/sp.svg" class="icon" alt=""/>
            <div>
              <span class="dropdown-link-title">Abonnements</span>
              <p>Accès exclusif</p>
            </div>
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#creative-feed">
            <img src="./assets/icons/cf.svg" class="icon" alt=""/>
            <div>
              <span class="dropdown-link-title">Fil créatif</span>
              <p>Voir les créations tendances</p>
            </div>
          </a>
        </li>
      </ul>
  
      <ul>
        <span id="apps- class="dropdown-link-title">Parcourir par applications</span>
        <li>
          <a class="dropdown-link" href="#adobe-xd">
            <img src="./assets/icons/xd.svg" alt=""/>
            Adobe XD
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#after-effect">
            <img src="./assets/icons/ae.svg" alt=""/>
            After Effect
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#sketch">
            <img src="./assets/icons/sketch.svg" alt=""/>
            Sketch
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#indesign">
            <img src="./assets/icons/indesign.svg" alt=""/>
            Indesign
          </a>
        </li>
        <li>
          <a class="dropdown-link" href="#figma">
            <img src="./assets/icons/figma.svg" alt="" />
            Figma
          </a>
        </li>
      </ul>
    </div>
  </li>
```

Vous pouvez obtenir les icônes SVG [ici](https://github.com/Evavic44/responsive-navbar-with-dropdown/tree/main/assets/icons).

Pour décomposer ce balisage, nous avons ajouté les éléments suivants :

* Un élément `div` avec un id `dropdown1` et une classe `dropdown`.
* Deux éléments `ul`.
* Un élément `span` avec une classe `dropdown-link-title` pour l'en-tête de chaque collection de `menu`.
* Une collection de liens définis en utilisant les balises `li` et `a`. Les liens ont chacun une classe `dropdown-link`.
* À l'intérieur de chaque balise d'ancrage, une icône est ajoutée via la balise `img`.

Remarque : Puisque les icônes ajoutées via la balise `img` sont strictement déclaratives, je recommande vivement de les ajouter en tant qu'éléments SVG directement. Je ne fais cela que pour rendre le code plus lisible.

Voici le balisage pour le deuxième élément déroulant `dropdown2` :

```html
<!-- balisage tronqué pour plus de concision-->
<li>
    <button
      class="nav-link dropdown-btn"
      data-dropdown="dropdown2"
      aria-expanded="false"
    >
      Découvrir
      <i class="bx bx-chevron-down" aria-hidden="true"></i>
    </button>
    <div id="dropdown2" class="dropdown">
      <ul aria-labelledby="categories-title">
        <span id="categories-title" class="dropdown-link-title">Parcourir les catégories</span>
        <li>
          <a class="dropdown-link" href="#branding">Branding</a>
        </li>
        <li>
          <a class="dropdown-link" href="#illustrations">Illustration</a>
        </li>
      </ul>
      <ul aria-labelledby="download-title">
        <span id="download-title" class="dropdown-link-title">Télécharger l'application</span>
        <li>
          <a class="dropdown-link" href="#mac-windows">MacOS & Windows</a>
        </li>
        <li>
          <a class="dropdown-link" href="#linux">Linux</a>
        </li>
      </ul>
    </div>
  </li>
```

Le résultat final devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/popup1-and-popup2-markup-1.png)

Le balisage complet sera fourni à la fin de ce tutoriel.

## Étape 2 – Styliser la barre de navigation

Comme toujours, nous commencerons par réinitialiser la marge et le remplissage par défaut de chaque élément sur la page, ajouter des variables globales et quelques styles de base à certains éléments.

```css
/* style.css */
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Inter", sans-serif;
}

:root {
  --dark-grey: #333333;
  --medium-grey: #636363;
  --light-grey: #eeeeee;
  --ash: #f4f4f4;
  --primary-color: #2b72fb;
  --white: white;
  --border: 1px solid var(--light-grey);
  --shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px,
    rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
}

body {
  font-family: inherit;
  background-color: var(--white);
  color: var(--dark-grey);
  letter-spacing: -0.4px;
}

ul {
  list-style: none;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  border: none;
  background-color: transparent;
  cursor: pointer;
  color: inherit;
}
```

Ensuite, ajoutez quelques styles réutilisables.

```css
.btn {
  display: block;
  background-color: var(--primary-color);
  color: var(--white);
  text-align: center;
  padding: 0.6rem 1.4rem;
  font-size: 1rem;
  font-weight: 500;
  border-radius: 5px;
}

.icon {
  padding: 0.5rem;
  background-color: var(--light-grey);
  border-radius: 10px;
}

.logo {
  margin-right: 1.5rem;
}

#nav-menu {
  border-bottom: var(--border);
}

.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1600px;
  margin: 0 auto;
  column-gap: 2rem;
  height: 90px;
  padding: 1.2rem 3rem;
}
```

Maintenant que vous avez terminé ce style de base, vous pouvez vous concentrer sur le style de la barre de navigation elle-même.

### Styles du menu de navigation

Voici le balisage pour styliser le conteneur de la barre de navigation :

```css
.menu {
  position: relative;
  background: var(--white);
}

.menu-bar li:first-child .dropdown {
  flex-direction: initial;
  min-width: 480px;
}

.menu-bar li:first-child ul:nth-child(1) {
  border-right: var(--border);
}

.menu-bar li:nth-child(n + 2) ul:nth-child(1) {
  border-bottom: var(--border);
}

.menu-bar .dropdown-link-title {
  font-weight: 600;
}

.menu-bar .nav-link {
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: -0.6px;
  padding: 0.3rem;
  min-width: 60px;
  margin: 0 0.6rem;
}

.menu-bar .nav-link:hover,
.dropdown-link:hover {
  color: var(--primary-color);
}

.nav-start,
.nav-end,
.menu-bar,
.right-container,
.right-container .search {
  display: flex;
  align-items: center;
}
```

### Styles du menu déroulant

En plus de styliser le menu déroulant, il sera masqué en utilisant une combinaison des propriétés `visibility` et `opacity`. L'idée est de montrer le menu uniquement lorsque le bouton individuel a été cliqué.

```css
.dropdown {
  display: flex;
  flex-direction: column;
  min-width: 230px;
  background-color: var(--white);
  border-radius: 10px;
  position: absolute;
  top: 36px;
  z-index: 1;
  visibility: hidden;
  opacity: 0;
  transform: scale(0.97) translateX(-5px);
  transition: 0.1s ease-in-out;
  box-shadow: var(--shadow);
}

.dropdown.active {
  visibility: visible;
  opacity: 1;
  transform: scale(1) translateX(5px);
}

.dropdown ul {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1.2rem;
  font-size: 0.95rem;
}

.dropdown-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.15rem;
}

.dropdown-link {
  display: flex;
  gap: 0.5rem;
  padding: 0.5rem 0;
  border-radius: 7px;
  transition: 0.1s ease-in-out;
}

.dropdown-link p {
  font-size: 0.8rem;
  color: var(--medium-grey);
}
```

Plus tard, le menu peut être basculé en restaurant les propriétés `visibility` et `opacity` à l'état par défaut en utilisant la classe `active`. Mais nous ferons cela via JavaScript.

Si vous préférez masquer complètement le menu, substituez les propriétés `opacity` et `visibility` par `display: none;`. Bien que cette propriété ne soit pas [animable](https://mdn.org/animatable-properties) en utilisant la transition en CSS.

### Styles du menu de droite

Ensuite, ajoutez le style pour l'entrée de recherche, le bouton et l'image de profil, puis masquez le bouton hamburger sur les écrans de bureau.

```css
.right-container {
  display: flex;
  align-items: center;
  column-gap: 1rem;
}

.right-container .search {
  position: relative;
}

.right-container img {
  border-radius: 50%;
}

.search input {
  background-color: var(--ash);
  border: none;
  border-radius: 6px;
  padding: 0.7rem;
  padding-left: 2.4rem;
  font-size: 16px;
  width: 100%;
  border: var(--border);
}

.search .search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  opacity: 0.6;
}

#hamburger {
  display: none;
  padding: 0.1rem;
  margin-left: 1rem;
  font-size: 1.9rem;
}
```

Voici à quoi cela devrait ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/final-styling-output-of-navigation-bar-and-popup-menu.png)

Pour terminer le style, ajoutez le style de la requête média :

```css
@media (max-width: 1100px) {
  #hamburger {
    display: block;
    position: relative;
    left: calc(100vw - 9rem);
  }

  .container {
    padding: 1.2rem;
    margin-right: 3rem;
  }

  .menu {
    display: none;
    position: absolute;
    top: 87px;
    left: 0;
    min-height: 100vh;
    width: 100vw;
  }

  .menu-bar li:first-child ul:nth-child(1) {
    border-right: none;
    border-bottom: var(--border);
  }

  .dropdown {
    display: none;
    min-width: 100%;
    border: none !important;
    border-radius: 5px;
    position: static;
    top: 0;
    left: 0;
    visibility: visible;
    opacity: 1;
    transform: none;
    box-shadow: none;
  }

  .menu.show,
  .dropdown.active {
    display: block;
  }

  .dropdown ul {
    padding-left: 0.3rem;
  }

  .menu-bar {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    row-gap: 1rem;
    padding: 1rem;
  }

  .menu-bar .nav-link {
    display: flex;
    justify-content: space-between;
    width: 100%;
    font-weight: 600;
    font-size: 1.2rem;
    margin: 0;
  }

  .menu-bar > li:not(:last-child) {
    padding-bottom: 0.5rem;
    border-bottom: var(--border);
  }
}

@media (max-width: 600px) {
  .right-container {
    display: none;
  }
}
```

Tout d'abord, cela arrange les éléments, et surtout, il cible la classe `hamburger` et la masque. Maintenant, sur les écrans de tablette et de mobile, la barre de navigation est responsive et le bouton hamburger est visible.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/responsive-navigation-bar-2.gif)

Cela complète le style de la barre de navigation. Passons à la fonctionnalité dans la section suivante.

## Étape 3 – Ajouter la fonctionnalité JavaScript

Pour la fonctionnalité JavaScript, nous nous concentrerons sur les catégories suivantes :

* Basculer la visibilité du menu déroulant
* Fermer le menu déroulant
* Basculer la visibilité du menu hamburger
* Basculer l'attribut aria-expanded

Tout d'abord, sélectionnez vos classes en utilisant la méthode `querySelector` du DOM et stockez-les dans des variables pour qu'elles soient réutilisables.

```javascript
// script.js
const dropdownBtn = document.querySelectorAll(".dropdown-btn");
const dropdown = document.querySelectorAll(".dropdown");
const hamburgerBtn = document.getElementById("hamburger");
const navMenu = document.querySelector(".menu");
const links = document.querySelectorAll(".dropdown a");
```

Ensuite, ajoutez les fonctions ci-dessous dans votre code. J'expliquerai leurs utilisations un peu plus tard.

```js
function setAriaExpandedFalse() {
  dropdownBtn.forEach((btn) => btn.setAttribute("aria-expanded", "false"));
}

function closeDropdownMenu() {
  dropdown.forEach((drop) => {
    drop.classList.remove("active");
    drop.addEventListener("click", (e) => e.stopPropagation());
  });
}

function toggleHamburger() {
    navMenu.classList.toggle("show");
    hamburgerBtn.setAttribute(
        "aria-expanded",
        hamburgerBtn.getAttribute("aria-expanded") === "false" ? "true" : "false"
    );
}
```

### Obtenir l'ID du menu déroulant

L'étape suivante consiste à obtenir l'ID du menu déroulant. Puisqu'il y a deux menus déroulants, la valeur sera basée sur le bouton de menu déroulant cliqué.

Pour obtenir l'ID, vous utiliserez la propriété `dataset` puis stockerez la valeur dans sa propre variable.

```js
dropdownBtn.forEach((btn) => {
  btn.addEventListener("click", function (e) {
    const dropdownIndex = e.currentTarget.dataset.dropdown;
    const dropdownElement = document.getElementById(dropdownIndex);
    console.log(dropdownElement);
  });
});

```

Pour décomposer ce snippet :

* La méthode `forEach` parcourt la collection de boutons
* La méthode `addEventListener()` attache un événement de clic à chaque bouton
* La propriété `currentTarget.dataset` récupère le menu déroulant actuel du bouton cliqué.
* Chacun des ids est utilisé pour cibler l'élément de menu déroulant correspondant

Cela signifie que lorsque le bouton avec un dataset de `dropdown1` est cliqué, l'élément `div` avec un id de `dropdown1` est enregistré dans la console, et inversement pour le bouton `dropdown2`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/get-popup-element-id-dynamically-1.gif)
_obtenir dynamiquement chaque élément de menu déroulant en utilisant la propriété dataset du bouton_

### Basculer le menu déroulant

Basculer le menu est assez facile maintenant que vous avez l'ID de l'élément de menu déroulant stocké dans une variable appelée `dropdownElement`. En ciblant cette variable, vous pouvez basculer la classe `active` sur chaque élément de menu déroulant.

```js
dropdownBtn.forEach((btn) => {
  btn.addEventListener("click", function (e) {
    const dropdownIndex = e.currentTarget.dataset.dropdown;
    const dropdownElement = document.getElementById(dropdownIndex);

    dropdownElement.classList.toggle("active");
    dropdown.forEach((drop) => {
      if (drop.id !== btn.dataset["dropdown"]) {
        drop.classList.remove("active");
      }
    });
    e.stopPropagation();
  });
});
```

En plus de basculer le menu déroulant, nous avons ajouté une condition pour vérifier si l'id de l'élément de menu déroulant actuel correspond au bouton actif. Cela garantit qu'un seul élément de menu déroulant est développé à la fois.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/toggling-dropdown-element.gif)
_basculer le menu déroulant_

### Basculer la propriété aria-expanded

La propriété `aria-expanded` permet aux technologies d'assistance d'annoncer si un menu interactif est développé ou réduit. Pour basculer cette propriété, insérez ce code à l'intérieur du bloc de code `btn` sous `e.stopPropagation()` :

```js
btn.setAttribute(
    "aria-expanded",
    btn.getAttribute("aria-expanded") === "false" ? "true" : "false"
);
```

Maintenant, chaque fois que le menu déroulant est visible, la propriété `aria-expanded` est définie sur true et lorsqu'il est réduit, elle est définie sur false.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/toggling-the-aria-expanded-property.gif)
_basculer la propriété aria-expanded_

### Réduire le menu déroulant

Jusqu'à présent, le menu déroulant se réduit uniquement lorsque les boutons sont cliqués. D'autres cas où il devrait être réduit incluent :

* Lorsque les liens à l'intérieur du menu déroulant sont cliqués
* Lorsque vous appuyez sur la touche ESC
* Lorsque vous cliquez sur le corps du document – essentiellement, à l'extérieur du conteneur de menu déroulant.

En appelant les fonctions créées précédemment, `closeDropdownMenu` et `setAriaExpandedFalse`, le menu déroulant peut être réduit et l'attribut `aria-expanded` défini sur false.

```js
// fermer le menu déroulant lorsque les liens du menu déroulant sont cliqués
links.forEach((link) =>
  link.addEventListener("click", () => {
    closeDropdownMenu();
    setAriaExpandedFalse();
  })
);

// fermer le menu déroulant lorsque vous cliquez sur le corps du document
document.documentElement.addEventListener("click", () => {
  closeDropdownMenu();
  setAriaExpandedFalse();
});

// fermer le menu déroulant lorsque la touche d'échappement est pressée
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeDropdownMenu();
    setAriaExpandedFalse();
  }
});

```

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/closing-dropdown-menu-when-dropdown-links-and-escape-key-is-clicked.gif)

### Basculer le menu hamburger

Pour voir la barre de navigation sur les écrans de tablette et de mobile, attachez la fonction `toggleHamburger` en tant que rappel sur le bouton hamburger, puis appelez la fonction à l'intérieur du bloc de code `links`.

```js
links.forEach((link) =>
  link.addEventListener("click", () => {
    closeDropdownMenu();
    setAriaExpandedFalse();
    toggleHamburger();
  })
);
```

```js
hamburgerBtn.addEventListener("click", toggleHamburger);
```

Cela basculera essentiellement une classe différente appelée `show` qui contrôle l'affichage de la barre de navigation ou la masque, et mettra à jour l'attribut `aria-expanded` en conséquence.

Notez que pour rendre le menu hamburger vraiment accessible, vous devrez le faire fermer automatiquement lorsqu'il perd le focus (soit par un changement de focus du clavier, soit par un clic de souris).

Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/show-hamburger-menu-on-tablet-and-mobile-screens.gif)

## Ajouter plus de menus déroulants

Vous pouvez ajouter plus de menus déroulants en remplaçant simplement l'un des éléments de liste par un lien vers celui avec un bouton et un menu déroulant. Pour que cela fonctionne, assurez-vous de mettre à jour les éléments suivants :

* L'ID du menu déroulant en fonction du nombre de menus dont vous avez besoin. Par exemple, un troisième menu aura un id de `dropdown3`
* Le bouton aura sa valeur `data-dropdown` définie sur `dropdown3`

Voici un exemple qui convertit le lien **Emplois** en un menu déroulant.

### Avant :

```html
<li><a class="nav-link" href="/">Emplois</a></li>
```

### Après :

```html
<li>
    <button
      class="nav-link dropdown-btn"
      data-dropdown="dropdown3"
      aria-expanded="false"
    >
      Emplois
      <i class="bx bx-chevron-down" aria-hidden="true"></i>
    </button>
    <div id="dropdown3" class="dropdown">
      <ul>
        <li><span class="dropdown-link-title">Logiciel</span></li>
        <li>
          <a class="dropdown-link" href="#frontend">Frontend</a>
        </li>
        <li>
          <a class="dropdown-link" href="#backend">Backend</a>
        </li>
        <li>
          <a class="dropdown-link" href="#ai-ml">IA/ML</a>
        </li>
        <li>
          <a class="dropdown-link" href="#mobile-dev">Développement Mobile</a>
        </li>
      </ul>
      <ul>
        <li>
          <span class="dropdown-link-title">Autres</span>
        </li>
        <li>
          <a class="dropdown-link" href="#ui-ux">UI/UX</a>
        </li>
        <li>
          <a class="dropdown-link" href="#writing">Rédaction Technique</a>
        </li>
      </ul>
    </div>
  </li>
```

Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/additional-dropdown-menu.png)
_Résultat final après l'ajout du troisième menu déroulant (Emplois)_

En suivant ce processus, vous pouvez ajouter autant de menus déroulants que vous le souhaitez.

Et avec cela, vous avez réussi à créer une barre de navigation responsive avec des menus déroulants en utilisant uniquement HTML, CSS et JavaScript. Vous avez également appris à rendre le menu accessible en utilisant quelques attributs aria, y compris la propriété `aria-expanded`.

### Voici le fichier codepen pour tester cette barre de navigation en action :

<iframe height="300" style="width: 100%;" scrolling="no" title="navbar with popup menu" src="https://codepen.io/evavic44/embed/QWZYEPQ?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/evavic44/pen/QWZYEPQ">
  navbar with popup menu</a> by Eke (<a href="https://codepen.io/evavic44">@evavic44</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Obtenez les fichiers de code depuis GitHub en utilisant ce [lien](https://github.com/Evavic44/responsive-navbar-with-dropdown)

## Conclusion

J'espère sincèrement que vous avez trouvé cet article intéressant ou utile. Si c'est le cas, partagez-le avec vos amis ou abonnez-vous à mon blog pour ne pas manquer les futures publications. Merci d'avoir lu.

[GitHub](https://github.com/Evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [LinkedIn](https://www.linkedin.com/in/victorekeawa/)