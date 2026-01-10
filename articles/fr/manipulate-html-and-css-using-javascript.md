---
title: Comment manipuler HTML et CSS en utilisant JavaScript
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-19T18:00:02.000Z'
originalURL: https://freecodecamp.org/news/manipulate-html-and-css-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-pixabay-276205.jpg
tags:
- name: CSS
  slug: css
- name: DOM
  slug: dom
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment manipuler HTML et CSS en utilisant JavaScript
seo_desc: "In JavaScript, the HTML DOM (Document Object Model) represents the structure\
  \ and content of an HTML document as a tree-like structure. In it, each element,\
  \ attribute, and text node in the HTML document is represented as a node in the\
  \ DOM tree. \nIn th..."
---

En JavaScript, le DOM HTML (Document Object Model) représente la structure et le contenu d'un document HTML sous forme d'une structure arborescente. Dans celle-ci, chaque élément, attribut et nœud de texte du document HTML est représenté comme un nœud dans l'arbre DOM. 

Dans cet article, vous allez apprendre comment utiliser cette structure pour contrôler plus efficacement le comportement de vos éléments HTML. Vous apprendrez également comment l'utiliser pour ajouter une interactivité dynamique à l'expérience de vos utilisateurs. 

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/DIg-GoyKUqA]

## Comprendre les éléments du DOM

Le DOM HTML fournit un moyen d'interagir avec et de manipuler les éléments d'un document HTML en utilisant JavaScript. Il permet d'accéder, de modifier et d'ajouter des éléments dynamiquement, de changer les styles et les classes, de gérer les événements et d'effectuer d'autres opérations sur le document.

![commons.wikimedia.org/wiki/File:DOM-model.svg sous licence CC Attribution-Share Alike 3.0 Unported.\label{fig:dom_model}](https://www.freecodecamp.org/news/content/images/2023/06/642px-DOM-model.svg.png)
_commons.wikimedia.org/wiki/File:DOM-model.svg sous licence CC Attribution-Share Alike 3.0 Unported_

Comme vous pouvez le voir sur cette illustration, `Document` est l'objet de niveau supérieur représentant un document HTML. Il sert de point d'entrée pour accéder à l'arbre DOM et fournit des méthodes pour naviguer et manipuler le document. 

`Element` représente un élément HTML dans l'arbre DOM. Les éléments ont des propriétés qui permettent d'accéder et de modifier les attributs, les styles et le contenu. Vous pouvez sélectionner des éléments en utilisant diverses méthodes comme :

* `getElementById`
* `getElementsByTagName`
* `getElementsByClassName`
* `querySelector` 
* `querySelectorAll`

`Node` est la classe de base pour tous les types de nœuds dans l'arbre DOM. Les nœuds peuvent être des éléments, des nœuds de texte, des nœuds de commentaire, etc. Ils ont des propriétés et des méthodes pour des opérations courantes, telles que l'accès aux nœuds parents et enfants, la manipulation du contenu des nœuds, et plus encore.

Le DOM fournit un système d'événements pour gérer les interactions utilisateur et autres événements. Vous pouvez attacher des écouteurs d'événements aux éléments pour répondre à des événements comme les clics, les pressions de touches et les mouvements de souris.

## Comment interagir avec le DOM en utilisant JavaScript

En utilisant JavaScript, vous pouvez interagir avec le DOM HTML pour modifier dynamiquement le contenu et le comportement d'une page HTML. Cela permet de créer des applications web interactives, de mettre en œuvre des interfaces utilisateur dynamiques et d'effectuer diverses opérations sur le document en fonction des actions de l'utilisateur ou de la logique programmatique.

Voici un exemple simple qui fait quelque chose de surprenant :

```html
<!DOCTYPE html>
<html>
<head>
  <title>Exemple de manipulation du DOM</title>
</head>
<body>
  <h1 id="myHeading">Bonjour, le monde !</h1>
  <p id="myParagraph">Ceci est un paragraphe.</p>

  <script>
    // Changer le contenu et les propriétés des éléments HTML
    document.getElementById("myHeading").innerHTML = "Nouveau titre";
    document.getElementById("myParagraph").style.color = "red";
    document.getElementById("myParagraph").textContent = "Ceci est mis à jour.";
  </script>
</body>
</html>

```

Nous avons un document HTML qui contient un élément de titre `<h1>` avec un id de `myHeading` et un élément de paragraphe `<p>` avec un id de `myParagraph`. 

```
  <h1 id="myHeading">Bonjour, le monde !</h1>
  <p id="myParagraph">Ceci est un paragraphe.</p>
```

Le code JavaScript dans les balises `<script>` manipule ces éléments via le DOM.

```
 <script>
    // Changer le contenu et les propriétés des éléments HTML
    document.getElementById("myHeading").innerHTML = "Nouveau titre";
    document.getElementById("myParagraph").style.color = "red";
    document.getElementById("myParagraph").textContent = "Ceci est mis à jour.";
 </script>
```

Le code utilise la méthode `getElementById` pour sélectionner les éléments par leur attribut id. Il modifie ensuite le contenu et les propriétés des éléments en utilisant les techniques de manipulation du DOM suivantes :

* `innerHTML` définit le contenu HTML à l'intérieur de l'élément sélectionné. Dans ce cas, nous changeons le texte du titre en "Nouveau titre".
* `style` accède aux styles CSS de l'élément sélectionné. Nous définissons la couleur du texte du paragraphe en rouge.
* `textContent` définit le contenu textuel de l'élément sélectionné. Nous mettons à jour le texte du paragraphe en "Ceci est un paragraphe mis à jour."

Lorsque nous chargeons le document HTML dans un navigateur web, le code JavaScript s'exécute immédiatement. Vous ne verrez jamais le style HTML original, mais seulement les "mises à jour" ordonnées par le JavaScript. Le texte du titre sera "Nouveau titre", la couleur du texte du paragraphe sera rouge et le contenu du paragraphe sera "Ceci est mis à jour."

Cela démontre comment JavaScript peut interagir avec le DOM pour modifier dynamiquement le contenu et les propriétés des éléments HTML en fonction de la logique programmatique ou des interactions utilisateur.

## Comment rendre vos sites web plus interactifs

Vous pouvez également déclencher des changements sur une page HTML en réponse aux activités de l'utilisateur. Dans cet exemple, nous définissons deux fonctions JavaScript : `showMessage` et `changeColor`. Ces fonctions sont déclenchées à partir d'éléments HTML en utilisant l'attribut `onclick`.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Déclenchement de fonctions JavaScript</title>
  <script>
    function showMessage() {
      alert("Bouton cliqué !");
    }

    function changeColor() {
      document.getElementById("myDiv").style.backgroundColor = "red";
    }
  </script>
</head>
<body>
  <h1>Exemple de déclenchement de fonctions JavaScript</h1>
  
  <button onclick="showMessage()">Cliquez-moi</button>
  <div id="myDiv" style="width: 200px; height: 200px; background-color: blue;"></div>
  <button onclick="changeColor()">Changer la couleur</button>
</body>
</html>

```

La fonction `showMessage` affiche une boîte d'alerte avec le message "Bouton cliqué !" lorsque le bouton est cliqué. 

```
    function showMessage() {
      alert("Bouton cliqué !");
    }
```

La fonction `changeColor` change la couleur de fond de l'élément `<div>` avec l'id `myDiv` en rouge lorsque le bouton est cliqué. 

```
    function changeColor() {
      document.getElementById("myDiv").style.backgroundColor = "red";
    }
```

Le code HTML inclut un bouton avec l'attribut `onclick` défini sur `showMessage()`, qui déclenche la fonction `showMessage` lorsque le bouton est cliqué. 

De même, il y a un autre bouton avec l'attribut `onclick` défini sur `changeColor()`, qui déclenche la fonction `changeColor` lorsque le bouton est cliqué.

```
  <button onclick="showMessage()">Cliquez-moi</button>
  <div id="myDiv" style="width: 200px; height: 200px; background-color: blue;"></div>
  <button onclick="changeColor()">Changer la couleur</button>
```

Lorsque vous chargez le document HTML dans un navigateur web, vous verrez le titre, deux boutons et un élément `<div>` coloré. Cliquer sur le bouton "Cliquez-moi" déclenchera la fonction showMessage et affichera une alerte.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/js1.png)

Cliquer sur le bouton "Changer la couleur" déclenchera la fonction `changeColor` et changera la couleur de fond de l'élément `<div>` en rouge.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/js2.png)

Comme je suis sûr que vous pouvez le deviner, cela ne fait qu'effleurer la surface de ce que vous pouvez faire avec le DOM. Voici une liste plus longue d'éléments et de méthodes compatibles avec le DOM et d'attributs HTML avec lesquels vous pouvez également jouer :

* document.getElementById()
* document.getElementsByClassName()
* document.getElementsByTagName()
* document.querySelector()
* document.querySelectorAll()
* innerHTML, setAttribute()
* removeAttribute()
* classList
* classList.add()
* classList.remove()
* classList.toggle()
* onClick
* onMouseOver
* onMouseOut

## Conclusion

Ceci était une brève introduction aux éléments du DOM, où vous avez eu un aperçu rapide du comment et du pourquoi du _contrôle_ des éléments HTML. Vous avez également appris comment vous pouvez ajouter une interactivité dynamique et une versatilité programmatique fine à votre site web.

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _Et il y a beaucoup plus de bonnes technologies disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_