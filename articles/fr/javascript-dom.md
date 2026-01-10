---
title: Comment fonctionne le Document Object Model en JavaScript – Tutoriel DOM pour
  débutants
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-01-19T15:21:29.000Z'
originalURL: https://freecodecamp.org/news/javascript-dom
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/JavaScript-DOM-cover-image1.jpg
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne le Document Object Model en JavaScript – Tutoriel DOM
  pour débutants
seo_desc: "The Document Object Model (DOM) is an essential part of web development.\
  \ It provides a way for programmers to interact with and manipulate the structure\
  \ of a website. \nWith the help of the DOM, developers can access and change the\
  \ different parts of ..."
---

Le Document Object Model (DOM) est une partie essentielle du développement web. Il fournit un moyen pour les programmeurs d'interagir avec et de manipuler la structure d'un site web. 

Avec l'aide du DOM, les développeurs peuvent accéder et modifier les différentes parties d'une page web. Cela leur permet de créer des sites web dynamiques et interactifs, où les interactions des utilisateurs peuvent déclencher des changements dans la mise en page et le contenu de la page. 

Comprendre le DOM est crucial pour créer des sites web réactifs et conviviaux. Donc, dans cet article, nous allons approfondir ce que le DOM peut faire et comment vous pouvez l'utiliser en JavaScript.

## Qu'est-ce que le DOM ?

Le DOM, ou Document Object Model, est comme une carte d'un site web. Tout comme une carte vous montre où se trouvent toutes les rues et les bâtiments dans une ville, le DOM vous montre où tout se trouve sur un site web. 

Le DOM aide votre ordinateur à comprendre les différentes parties d'un site web et comment elles sont assemblées. 

Tout comme vous pouvez utiliser une carte pour trouver votre chemin dans une ville, les programmeurs peuvent utiliser le DOM pour trouver différentes parties d'un site web et changer leurs propriétés. Par exemple, ils peuvent faire changer la couleur d'un bouton lorsque l'utilisateur passe la souris dessus ou faire bouger des images à l'écran.

Le DOM est comme un grand puzzle. Mais en utilisant JavaScript, nous pouvons déplacer les pièces du puzzle et faire en sorte qu'un site web ait l'apparence et le fonctionnement que nous voulons.

## Le DOM + JavaScript

JavaScript est un langage de programmation qui nous aide à interagir avec le DOM. Le DOM et JavaScript sont comme deux amis qui travaillent ensemble pour rendre les sites web cool et interactifs. Encore une fois, le DOM est comme une grande carte qui montre où se trouvent toutes les différentes parties du site web.

D'autre part, JavaScript est comme une baguette magique qui peut changer un site web en utilisant la carte (DOM) pour trouver les différentes parties du site web. Il peut faire changer la couleur d'un bouton lorsque vous cliquez dessus ou faire bouger une image à un autre endroit sur la page. 

Ensemble, le DOM et JavaScript donnent vie au site web et le font réagir à ce que vous faites, comme déplacer votre souris ou cliquer sur un bouton. 

En résumé, le DOM est comme une carte qui montre où tout se trouve et JavaScript est comme une baguette magique qui peut changer les choses sur cette carte.

## Structure du DOM – Comprendre l'arborescence DOM

Imaginez qu'un site web est comme un grand livre, et chaque page de ce livre représente une partie différente du site web. L'arborescence DOM est comme une table des matières pour ce livre. Elle vous montre toutes les différentes parties du site web, et comment elles sont organisées. 

Chaque partie du site web est appelée un "élément" et ces éléments sont disposés dans une structure en forme d'arbre. 

Le sommet de l'arbre est appelé la "racine" et il représente l'ensemble du site web. À partir de là, l'arbre se ramifie en différentes sections, comme les titres, les paragraphes, les images, et autres qui composent l'ensemble du site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/DOM-tree-5.png)
_Illustration de l'arborescence DOM_

Tout comme la table des matières d'un livre vous aide à trouver des pages spécifiques, l'arborescence DOM aide les ordinateurs à trouver des éléments spécifiques sur un site web. De plus, elle permet aux développeurs d'accéder et de modifier ces éléments, afin qu'ils puissent rendre le site web interactif. 

En bref, l'arborescence DOM représente la structure d'un site web de manière à ce que les ordinateurs puissent la comprendre. Les développeurs peuvent l'utiliser pour accéder et manipuler différents éléments dans cette structure afin de créer des pages web dynamiques.

## Comment accéder au DOM

Accéder aux éléments du DOM signifie trouver des parties spécifiques d'un site web et les modifier ou les manipuler. 

Pour accéder à un élément sur un site web, vous devez connaître l'élément spécifique que vous souhaitez accéder. 

JavaScript fournit différentes méthodes pour accéder aux éléments du DOM, telles que `getElementById`, `getElementsByTagName`, `querySelector`, et `querySelectorAll`. 

Ces méthodes vous permettent de trouver un élément en fonction de son `id`, de son `nom de balise`, ou de son `nom de classe` et de le sélectionner pour le manipuler. 

Par exemple, vous pouvez accéder à un bouton sur une page web et changer son texte ou sa couleur lorsque l'utilisateur clique dessus. Ou, vous pouvez accéder à une image sur une page web et la changer en une autre image lorsque l'utilisateur passe la souris dessus. 

Voici un exemple de la façon dont vous pourriez utiliser le DOM pour accéder à un élément sur une page web : 

Disons que vous avez une page web qui affiche une liste d'étudiants et que vous souhaitez changer la couleur de fond d'un étudiant spécifique lorsqu'il est cliqué. 

Vous pouvez utiliser la méthode DOM `getElementById` pour accéder à l'élément spécifique qui représente l'étudiant, puis utiliser la propriété `style` en JavaScript pour changer la couleur de fond de cet élément.

Voici à quoi cela pourrait ressembler :

```html
<div id="student-list">
  <div id="student-1" class="student">John</div>
  <div id="student-2" class="student">Alice</div>
  <div id="student-3" class="student">Bob</div>
</div>
```

```css
.student {
  padding: 40px;
  margin-bottom: 10px;
  cursor: pointer;
}
.student:hover {
  background-color: #f1f1f1;
}

```

```javascript
let student1 = document.getElementById("student-1");

student1.addEventListener("click", () => {
  student1.style.backgroundColor = "lightblue";
});

```

Dans cet exemple, JavaScript utilise la méthode `getElementById` pour sélectionner l'élément avec l'id "student-1" et change sa propriété `backgroundColor` en "light blue" lorsque vous cliquez dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Document_4.gif)

De même, vous pouvez utiliser `getElementsByClassName` pour sélectionner tous les éléments avec une classe spécifique et `querySelector` pour sélectionner un élément basé sur un sélecteur CSS.

Ce n'est qu'un exemple de base, mais il illustre comment vous pouvez utiliser le DOM pour accéder à des éléments spécifiques sur une page web et changer leurs propriétés en réponse à l'interaction de l'utilisateur.

## Comment ajouter, supprimer et modifier des éléments du DOM

Ajouter, supprimer et modifier des éléments dans le DOM fait référence à l'ajout de nouveaux éléments à une page web, à la suppression d'éléments existants et au changement des propriétés d'éléments existants.

Par exemple, si vous souhaitez ajouter un nouveau bouton à une page web, vous utiliseriez JavaScript pour créer un nouvel élément, puis utiliseriez le DOM pour ajouter cet élément à la page web. De même, si vous souhaitez supprimer un élément, vous utiliseriez le DOM pour trouver l'élément et ensuite le supprimer.

La modification d'éléments implique également de faire des changements aux propriétés d'un élément existant. Par exemple, vous pourriez utiliser le DOM pour changer le texte à l'intérieur d'un bouton.

Voici comment vous pouvez exprimer cela en code :

```html
    <div id="wrapper" class="btn-wrapper">
      <button id="create-btn" class="btn">Créer un nouveau bouton</button>
    </div>
```

```css
.btn-wrapper {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

```

```javascript
let createButton = document.getElementById("create-btn");
let wrapper = document.getElementById("wrapper");

createButton.addEventListener("click", () => {
  let newButton = document.createElement("button");
  newButton.innerHTML = "Cliquez-moi";
  wrapper.appendChild(newButton);
});
```

Dans l'exemple ci-dessus, nous créons un nouvel élément bouton et définissons le texte à l'intérieur du bouton sur "Cliquez-moi". Ensuite, nous utilisons la méthode `appendChild` pour ajouter cet nouvel élément bouton à la page web.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Document.gif)

## Récapitulatif

Le Document Object Model (DOM) est un outil essentiel pour créer des pages web interactives et dynamiques en utilisant JavaScript. Il permet aux développeurs d'accéder et de manipuler le contenu d'une page web en temps réel. 

Comprendre l'arborescence DOM et comment accéder, ajouter, supprimer et modifier des éléments est crucial pour les développeurs JavaScript.

Nous avons vu comment le DOM représente une page web sous forme d'arbre d'objets et comment nous pouvons utiliser différentes méthodes comme `getElementById`, `getElementsByTagName`, `querySelector`, et `querySelectorAll` pour accéder à des éléments spécifiques sur une page web. Avec ces méthodes, nous pouvons changer le contenu, le style ou la mise en page d'une page web après qu'elle a été chargée dans le navigateur. 

De plus, nous avons vu comment ajouter de nouveaux éléments à une page web, supprimer des éléments existants et changer les propriétés d'éléments existants.

## Conclusion

J'espère que cet article vous a donné une meilleure compréhension du Document Object Model et comment l'utiliser pour créer des pages web dynamiques. 

N'oubliez pas que le DOM est un outil puissant que vous pouvez utiliser pour créer des sites web incroyables, alors n'ayez pas peur d'expérimenter et d'essayer de nouvelles choses.

Merci d'avoir lu ! N'hésitez pas à partager cet article et à me suivre sur Twitter [@alege_dev](https://twitter.com/alege_dev) pour les mises à jour des futurs articles.