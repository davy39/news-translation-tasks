---
title: Comment créer un menu accordéon avec HTML, CSS et JavaScript
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-29T19:45:33.000Z'
originalURL: https://freecodecamp.org/news/build-an-accordion-menu-using-html-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/accordion-canva.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer un menu accordéon avec HTML, CSS et JavaScript
seo_desc: 'You can use HTML, CSS and JavaScript to create stylish and dynamic web
  elements. And one useful element you can build is an accordion menu.

  Accordion menus expand and collapse when a user clicks a button. It''s a great way
  to not have to show all the ...'
---

Vous pouvez utiliser HTML, CSS et JavaScript pour créer des éléments web stylisés et dynamiques. Et l'un des éléments utiles que vous pouvez construire est un menu accordéon.

Les menus accordéons s'étendent et se replient lorsqu'un utilisateur clique sur un bouton. C'est une excellente façon de ne pas avoir à afficher toutes les informations sur un sujet d'emblée, et de donner plutôt aux utilisateurs l'option de n'afficher que ce dont ils ont besoin.

Dans ce tutoriel, je vais vous montrer comment construire un menu accordéon simple qui ressemble à ceci :

![ezgif.com-gif-maker.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1632910257498/EuFFg0l3d.gif align="left")

## Qu'est-ce qu'un menu accordéon ?

En conception d'interface utilisateur, un menu accordéon est une liste empilée verticalement de diverses pièces d'information. Pour chaque liste, il y a un en-tête étiqueté pointant vers le contenu correspondant. Le contenu de chaque liste est masqué par défaut. Cliquer sur une étiquette particulière développera son contenu.

Un cas d'utilisation très courant pour les accordéons est de contenir une liste de questions fréquemment posées. Cliquer sur une question affichera la réponse correspondante.

## Comment construire un menu accordéon en utilisant HTML, CSS et JS

Nous commencerons par définir le balisage HTML. Si vous utilisez un IDE comme VS Code et que vous avez installé emmet, créez un nouveau fichier `index.html` et tapez `!` suivi de la touche entrée. Cela devrait créer un code de base HTML pour votre projet.

Alternativement, vous pouvez copier le code suivant dans votre `index.html`, ou obtenir le code de ce projet depuis [Codepen](https://codepen.io/ubahthebuilder/pen/gORqxNe).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <script src="app.js" type="text/javascript"></script>
</body>
</html>
```

La structure du dossier est simple. Nous allons créer un dossier appelé accordion. À l'intérieur du dossier, nous créerons trois fichiers : `index.html`, `styles.css`, et `app.js`. Nous allons également lier tous les fichiers dans notre balisage HTML comme vous pouvez le voir ci-dessus.

### Balisage HTML pour l'accordéon

Pour chaque liste dans le menu, nous aurons deux `div` – une pour l'étiquette, l'autre pour le contenu.

```html
<body>
  <div class="accordion-body">
  <div class="accordion">
    <h1>Foire aux questions</h1>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que le HTML</div>
      <div class="content">Hypertext Markup Language (HTML) est un langage informatique qui constitue la plupart des pages web et des applications en ligne. Un hypertexte est un texte utilisé pour référencer d'autres morceaux de texte, tandis qu'un langage de balisage est une série de marquages qui indique aux serveurs web le style et la structure d'un document. Le HTML est très simple à apprendre et à utiliser.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que le CSS ?</div>
      <div class="content">CSS signifie Cascading Style Sheets. C'est le langage pour décrire la présentation des pages Web, y compris les couleurs, la mise en page et les polices, rendant ainsi nos pages Web présentables aux utilisateurs. Le CSS est conçu pour créer des feuilles de style pour le web. Il est indépendant du HTML et peut être utilisé avec n'importe quel langage de balisage basé sur XML. Le CSS est couramment appelé le langage de design du web.
</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que JavaScript ?</div>
      <div class="content">JavaScript est un langage de script ou de programmation qui vous permet de mettre en œuvre des fonctionnalités complexes sur les pages web — chaque fois qu'une page web fait plus que simplement s'asseoir et afficher des informations statiques pour que vous les regardiez — afficher des mises à jour de contenu en temps opportun, des cartes interactives, des graphiques animés 2D/3D, des jukeboxes vidéo défilants, etc. — vous pouvez parier que JavaScript est probablement impliqué. C'est le troisième du trio du web.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que React ?</div>
      <div class="content">React est une bibliothèque JavaScript créée pour construire des interfaces utilisateur rapides et interactives pour les applications web et mobiles. C'est une bibliothèque open-source, basée sur des composants, front-end, responsable uniquement de la couche de vue de l'application. Dans l'architecture Model View Controller (MVC), la couche de vue est responsable de l'apparence et de la sensation de l'application. React a été créé par Jordan Walke, un ingénieur logiciel chez Facebook. </div>
    </div>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que PHP ?</div>
      <div class="content">PHP est un langage de script côté serveur et polyvalent qui est particulièrement adapté au développement web. PHP signifiait à l'origine Personal Home Page. Cependant, maintenant, cela signifie Hypertext Preprocessor. C'est un acronyme récursif car le premier mot lui-même est également un acronyme.</div>
    </div>
    <hr>
    <div class="container">
      <div class="label">Qu'est-ce que Node JS ?</div>
      <div class="content">Node.js est un environnement d'exécution JavaScript open-source, multiplateforme, côté serveur qui s'exécute sur le moteur V8 et exécute du code JavaScript en dehors d'un navigateur web. Node.js permet aux développeurs d'utiliser JavaScript pour écrire des outils en ligne de commande et pour le script côté serveur—exécuter des scripts côté serveur pour produire du contenu de page web dynamique avant que la page ne soit envoyée au navigateur web de l'utilisateur. Par conséquent, Node.js représente un paradigme "JavaScript partout".</div>
    </div>
    <hr>
  </div>
  </div>

  <script src="index.js" type="text/javascript"></script>
</body>
```

Sans CSS, notre page aura l'air toute nue, comme ceci :

![htmlook.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632478639319/6_WWaZagG.png align="left")

*À quoi ressemble le menu accordéon sans CSS*

### Comment styliser l'accordéon avec CSS

Nous voulons bien sûr que notre menu accordéon ait une belle apparence. Il est temps d'ajouter un peu de CSS. J'ai ajouté quelques commentaires dans le code pour expliquer ce que fait chaque partie :

```c
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

/* Définit la couleur de fond du body en bleu. Définit la police en Rubik */

body {
  background-color: #0A2344;
  font-family: 'rubik', sans-serif;
}

/* Aligne le texte du titre au centre. */
 
h1 {
  text-align: center;
}

/* Définit la largeur pour l'accordéon. Définit la marge à 90px en haut et en bas et auto à gauche et à droite */

.accordion {
  width: 800px;
  margin: 90px auto;
  color: black;
  background-color: white;
  padding: 45px 45px;
}
```

Avec tous ces styles appliqués, voici à quoi ressemblera notre accordéon maintenant :

![withcss1.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632479039630/X8DyVEIrx.png align="left")

*Styles ajoutés au menu accordéon*

Maintenant, nous devons commencer à faire un peu de travail à l'intérieur pour configurer sa fonctionnalité. Tout d'abord, nous définissons la propriété de position pour chacun des conteneurs (contenant à la fois l'étiquette et le contenu) à relative.

Cela signifie que nous pouvons maintenant positionner ses enfants par rapport à lui.

```css
.accordion .container {
  position: relative;
  margin: 10px 10px;
}

/* Positionne les étiquettes par rapport au .container. Ajoute un remplissage en haut et en bas et augmente la taille de la police. Rend également son curseur en pointeur */

.accordion .label {
  position: relative;
  padding: 10px 0;
  font-size: 30px;
  color: black;
  cursor: pointer;
}
```

Vous pouvez maintenant remarquer la différence dans l'image ci-dessous :

![withcss2.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632479377592/ZaOptRvWO5.png align="left")

La prochaine action sera d'ajouter un petit signe '+' à la fin de chaque liste. Cela permettra aux utilisateurs de savoir qu'ils peuvent développer la section pour en apprendre/savoir plus.

Nous allons réaliser cela en utilisant le sélecteur `::before`. Le sélecteur `::before` et `::after` est utilisé pour placer du contenu avant ou après un élément spécifié.

Ici, nous insérons '+' avant l'étiquette. Mais nous utiliserons les propriétés de décalage `top` et `right` pour le placer dans le coin supérieur droit.

```css

/* Positionne le signe plus à 5px de la droite. Le centre en utilisant la propriété transform. */

.accordion .label::before {
  content: '+';
  color: black;
  position: absolute;
  top: 50%;
  right: -5px;
  font-size: 30px;
  transform: translateY(-50%);
}

/* Cache le contenu (height: 0), diminue la taille de la police, justifie le texte et ajoute une transition */

.accordion .content {
  position: relative;
  background: white;
  height: 0;
  font-size: 20px;
  text-align: justify;
  width: 780px;
  overflow: hidden;
  transition: 0.5s;
}

/* Ajoute une ligne horizontale entre les contenus */

.accordion hr {
  width: 100;
  margin-left: 0;
  border: 1px solid grey;
}
```

Cela rendra tout meilleur. Remarquez également que le contenu de chaque liste est maintenant masqué.

![nowbig.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632480128515/4Q2E4YR5d.png align="left")

*Le contenu du menu accordéon est maintenant masqué*

### Ajout de JavaScript à notre accordéon

À ce stade, notre accordéon est presque statique. Pour qu'un conteneur affiche le contenu lorsqu'un utilisateur clique dessus, nous devons ajouter un peu de JavaScript.

Accédez à votre script `app.js` et tapez le code suivant :

```js
const accordion = document.getElementsByClassName('container');

for (i=0; i<accordion.length; i++) {
  accordion[i].addEventListener('click', function () {
    this.classList.toggle('active')
  })
}
```

Ce script accédera à toutes nos listes par `classname` de `container`.

Ensuite, nous allons parcourir la liste. Pour chaque conteneur, nous voulons simplement y enregistrer un écouteur d'événement. Lorsqu'il est cliqué, nous voulons basculer la classe "active" sur cet élément.

Maintenant, nous allons tester cet effet. Cliquez sur le premier conteneur avec l'étiquette `Qu'est-ce que le HTML`, ouvrez vos DevTools (cliquez sur F12), et inspectez-le à l'intérieur de l'onglet éléments.

Vous devriez trouver la classe `active` enregistrée sur lui :

![active.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632480884158/5AuG4fo_q.png align="left")

*Classe active basculée sur le premier élément de menu*

Cliquer à nouveau sur l'élément supprimera la classe `active` de celui-ci.

### Comment finaliser l'application

Il y a une dernière chose que nous devons faire. Nous devons créer une classe active dans une feuille de style. Nous allons définir comment nous voulons que notre accordéon apparaisse une fois que JavaScript bascule la classe sur un conteneur.

```css

/* Affiche la partie contenu lorsqu'elle est active. Définit la hauteur */

.accordion .container.active .content {
  height: 150px;
}

/* Change du signe plus au signe négatif une fois actif */

.accordion .container.active .label::before {
  content: '-';
  font-size: 30px;
}
```

Voici à quoi ressemble et se comporte notre application à la fin :

![ezgif.com-gif-maker.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1632910257498/EuFFg0l3d.gif align="left")

*Apparence finale*

## Conclusion

Dans ce tutoriel, nous avons donc construit un menu accordéon en utilisant HTML, CSS et JavaScript.

Merci d'avoir suivi. J'espère que vous avez appris quelque chose d'utile dans ce tutoriel.

Si vous êtes intéressé par du contenu comme celui-ci, [suivez mon blog](https://ubahthebuilder.tech).

Passez une excellente semaine.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).