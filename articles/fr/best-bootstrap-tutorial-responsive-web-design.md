---
title: Les meilleurs tutoriels Bootstrap pour le design web responsive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-22T17:33:00.000Z'
originalURL: https://freecodecamp.org/news/best-bootstrap-tutorial-responsive-web-design
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1e740569d1a4ca40e6.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: responsive design
  slug: responsive-design
seo_title: Les meilleurs tutoriels Bootstrap pour le design web responsive
seo_desc: 'Bootstrap is a popular front-end framework for web development. It contains
  pre-built components and design elements to style HTML content. Modern browsers
  such as Chrome, Firefox, Opera, Safari, and Internet Explorer support Bootstrap.

  Bootstrap inc...'
---

Bootstrap est un framework front-end populaire pour le développement web. Il contient des composants et des éléments de design pré-construits pour styliser le contenu HTML. Les navigateurs modernes tels que Chrome, Firefox, Opera, Safari et Internet Explorer supportent Bootstrap.

Bootstrap inclut un système de grille responsive pour des mises en page variées. C'est un excellent point de départ pour construire un site web adapté aux mobiles. Il inclut également des fonctionnalités JavaScript optionnelles comme le contenu pliable, les carrousels et les modales.

#### **Historique des versions**

Twitter a initialement développé le framework Bootstrap comme un outil interne. Ils l'ont publié en tant que projet open source en août 2011.

Bootstrap 2 a été publié en janvier 2012. L'une des principales fonctionnalités était l'introduction du système de grille responsive à 12 colonnes. Bootstrap 3 est apparu en août 2013, passant à un design plat et une approche mobile-first. Bootstrap 4 est disponible en bêta depuis août 2017, et inclut maintenant Sass et Flexbox.

Bootstrap 4 a été en développement pendant deux ans avant de publier quelques versions bêta en 2017, tandis que la première version stable est sortie en janvier 2018. Certains changements notables incluent :

* Passage de Less à Sass ;
* Passage à Flexbox et amélioration du système de grille ;
* Ajout de cartes (remplaçant les puits, les miniatures et les panneaux) ;
* Et bien plus encore !

Au moment de la rédaction, la dernière version de Bootstrap est [4.1.3](http://blog.getbootstrap.com/2018/07/24/bootstrap-4-1-3/). Si vous souhaitez rester informé des dernières nouvelles et annonces, suivez-les [ici](http://blog.getbootstrap.com/).

#### **Installation**

Il existe deux options principales pour ajouter Bootstrap à votre projet web. Vous pouvez lier des sources publiques ou télécharger directement le framework.

##### **Lier à une autre source**

Vous pouvez ajouter le CSS de Bootstrap en utilisant un élément `<link>` à l'intérieur de la balise `<head>` de votre page web qui référence un Content Delivery Network (CDN) :

`<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">`

L'ajout des éléments JavaScript de Bootstrap est similaire avec des éléments `<script>` généralement placés en bas de votre balise `</body>`. Vous devrez peut-être inclure certaines dépendances en premier. Portez une attention particulière à l'ordre indiqué :

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
```

_Note : Ce ne sont que des exemples et ils peuvent changer sans préavis. Veuillez vous référer à un CDN pour les liens actuels à inclure dans votre projet._

##### **Télécharger/Installer**

Vous pouvez télécharger et installer les fichiers sources de Bootstrap avec Bower, Composer, Meteor ou npm. Cela permet un meilleur contrôle et l'option d'inclure ou d'exclure des modules selon les besoins.

`npm install bootstrap`

`gem 'bootstrap', '~> 4.1.3'`

_Note : Ce ne sont que des exemples et ils peuvent changer sans préavis. Veuillez vous référer au [site web de Bootstrap](https://getbootstrap.com/) pour les liens les plus à jour._

#### **Le système de grille Bootstrap**

Le système de grille est un système flexbox mobile-first pour construire rapidement des mises en page de toutes formes et tailles adaptées à tous les appareils. Il est basé sur une mise en page à 12 colonnes et possède plusieurs niveaux, un pour chaque plage de requêtes média.

Bootstrap vient avec des classes de grille pré-définies pour votre utilisation dans le balisage. Voir plus de détails et d'exemples à [https://getbootstrap.com/docs/4.1/layout/grid/](https://getbootstrap.com/docs/4.1/layout/grid/)

### **Fonctionnalités de Bootstrap**

* Bootstrap 3 supporte les dernières versions de Google Chrome, Firefox, Internet Explorer, Opera et Safari (sauf sur Windows). Il supporte également jusqu'à IE8 et la dernière version de Firefox Extended Support Release (ESR).[12]
* Depuis la version 2.0, Bootstrap supporte le design web responsive. Cela signifie que la mise en page des pages web s'ajuste dynamiquement, en tenant compte des caractéristiques de l'appareil utilisé (ordinateur de bureau, tablette, téléphone mobile).
* À partir de la version 3.0, Bootstrap a adopté une philosophie de design mobile-first, en mettant l'accent sur le design responsive par défaut.
* La version 4.0 a ajouté la prise en charge de Sass et Flexbox.

#### **Plus d'informations :**

Bootstrap dispose d'une documentation complète avec de nombreux [exemples](https://getbootstrap.com/docs/4.0/examples/) et un [modèle HTML pour commencer](https://getbootstrap.com/docs/4.0/getting-started/introduction/) (ce modèle n'inclut que le script ; il ne contient pas de configuration du système de grille si c'est ce que vous cherchez).

De plus, vous pouvez trouver des thèmes [gratuits](https://bootswatch.com/) et [payants](https://themes.getbootstrap.com/) qui s'appuient sur le framework Bootstrap pour offrir un look plus personnalisé et stylisé.

#### **Ressources Bootstrap :**

[Blog officiel de Bootstrap](http://blog.getbootstrap.com/)

[Inspiration de sites Bootstrap](http://expo.getbootstrap.com/)

[Présentation des sites construits avec Bootstrap](http://builtwithbootstrap.com/)

[Linter HTML pour les projets utilisant Bootstrap](https://github.com/twbs/bootlint)

[Éléments de design et extraits de code pour Bootstrap](https://bootsnipp.com/)

[Code, thèmes et ressources d'add-ons pour Bootstrap](http://expo.getbootstrap.com/resources/)

# Guide de démarrage avec Bootstrap

L'utilisation de Bootstrap facilite la conception d'un site web entièrement responsive et est un framework qui vaut la peine d'être appris.

#### **Qu'est-ce qu'un site web responsive ?**

Un site web responsive est un site qui redimensionne et réorganise les éléments de la page en fonction de la taille de votre navigateur. Avec un site web responsive, si vous redimensionnez votre navigateur, vous pouvez voir les changements se produire en temps réel. Bootstrap rend votre site web responsive pour vous.

#### **Comment ajouter Bootstrap à votre page**

Ajouter Bootstrap à votre page est un processus rapide, il suffit d'ajouter ce qui suit aux balises `<head>` dans votre code.

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
```

Vous devrez également ajouter ce qui suit entre les balises `body` dans votre code. Avec Bootstrap, vous utiliserez des balises `<div>`. Lorsque vous utilisez de nombreuses fonctionnalités de Bootstrap, chaque balise aura son propre ensemble unique de classes appliquées qui permet à la balise d'effectuer sa tâche. D'autres sections de ce guide Bootstrap montreront plus d'exemples de la façon dont Bootstrap utilise les balises `<div>`. (Les balises `<div>` ne sont pas exclusives à Bootstrap, cependant Bootstrap en fait usage.)

Ci-dessous se trouve le code qui serait ajouté aux balises `body` dans votre code pour terminer le démarrage. Gardez à l'esprit que bien que cela crée le conteneur, la page restera vide jusqu'à ce que vous ajoutiez du contenu au conteneur.

```html
<div class="alert alert-success" role="alert">
    <strong>Félicitations !</strong>
    <p>Bootstrap fonctionne maintenant sur cette page</p>
</div>
```

# Modèles

Les modèles sont des kits pré-construits qui facilitent la création d'une nouvelle page web. Si vous avez une idée générale de la mise en page souhaitée, ou si vous souhaitez parcourir une bibliothèque de modèles de mise en page courants pour des idées, les modèles Bootstrap éliminent une grande partie de la monotonie et des frustrations du processus de construction initial. Cette assistance vous aide à vous concentrer sur les détails plus fins du projet au lieu de vous demander pourquoi le CSS ne coopère pas.

### **Commencer**

* La page web officielle de Bootstrap propose des "Thèmes" au lieu de modèles. Les thèmes sont simplement des projets de démarrage entièrement construits, tandis qu'un modèle décrit simplement un cadre HTML pré-construit. Les thèmes coûtent de l'argent et aident peut-être le développeur novice, tandis que de nombreux modèles sont open source et ne fournissent que les éléments de mise en page préliminaires nécessaires.
* Ci-dessous se trouve une liste de modèles de mise en page, spécialement conçus pour Bootstrap. Amusez-vous bien !

### **Liens vers les modèles**

* [Modèles StartBootstrap](https://startbootstrap.com/)
* [Modèles Bootstrap de W3 Schools](https://www.w3schools.com/bootstrap/bootstrap_templates.asp)
* [Wrap Bootstrap](https://wrapbootstrap.com/)
* [Wow Slider](http://wowslider.com/posts/35-top-free-bootstrap-templates-2016-95.html)
* [Bootstrap Made](https://bootstrapmade.com/)

## **Barre de navigation**

Le framework Bootstrap vous fournit une fonctionnalité appelée barres de navigation. En bref, une barre de navigation (également appelée navbars) est un en-tête en haut de la page pour afficher des informations de navigation.

#### **Comment utiliser**

Pour utiliser les barres de navigation Bootstrap, vous ajoutez un élément `<nav>` en haut à l'intérieur de l'élément `<body>` de votre page web. Il existe divers styles que vous pouvez ajouter pour personnaliser l'affichage de vos navbars.

#### **Exemple de code**

Voici le code nécessaire pour créer une navbar de base.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du site</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Accueil</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>
</nav>
```

#### **Styles de navbar**

Bootstrap fournit un ensemble de classes dans le framework Bootstrap pour styliser vos navbars. Ces classes sont les suivantes :

* `navbar navbar-default` Il s'agit du style par défaut pour vos navbars.
* `navbar navbar-inverse` Cela est similaire au style par défaut sauf que les couleurs sont inversées.

#### **Ajout de menus déroulants à la navbar**

Vous pouvez inclure un menu déroulant dans une navbar. Cette fonctionnalité nécessite d'inclure le fichier JavaScript de Bootstrap pour fonctionner.

```html
<li class="dropdown">
  <a class="dropdown-toggle" data-toggle="dropdown" href="#">Menu déroulant
    <span class="caret"></span>
  </a>
<ul class="dropdown-menu">
    <li><a href="#">Élément 1</a></li>
    <li><a href="#">Élément 2</a></li>
    <li><a href="#">Élément 3</a></li>
  </ul>
</li>
```

#### **Ajout de boutons à la navbar**

Vous pouvez ajouter des boutons sur la navbar. Les classes de boutons Bootstrap existantes fonctionnent, cependant vous devrez inclure la classe `navbar-btn` à la fin de la liste des classes.

```html
<button class="btn navbar-btn">Bouton</button>
```

#### **Ajout de formulaires à la navbar**

Vous pouvez également ajouter des formulaires à la navbar. Cela pourrait être utilisé pour des tâches telles qu'un champ de recherche, un champ de connexion rapide, etc.

```html
<form class="navbar-form navbar-right">
  <div class="form-group">
      <input type="text" class="form-control" placeholder="Rechercher">
  </div>  
  <button type="submit" class="btn btn-default">Rechercher</button>  
</form>
```

#### **Alignement des éléments à droite sur la navbar**

Dans certains cas, vous pourriez vouloir aligner des éléments dans une navbar à droite (par exemple, un bouton de connexion ou d'inscription). Pour ce faire, vous devrez utiliser la classe `navbar-right`.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du site</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Accueil</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="#">Lien d'action #1</a></li>
      <li><a href="#">Lien d'action #2</a></li>
    </ul>
  </div>
</nav>
```

#### **Affichage de la navbar indépendamment du défilement**

Dans certains cas, vous pourriez vouloir garder la navbar en haut ou en bas de l'écran indépendamment du défilement. Vous devrez ajouter soit la classe `navbar-fixed-top` soit `navbar-fixed-bottom` à l'élément `<nav>`.

```html
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du site</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Accueil</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>
</nav>
```

#### **Réduction de la navbar**

Sur un petit écran (comme un téléphone ou une tablette), la navbar va prendre trop de place. Heureusement, l'option de réduire la navbar existe. Vous pouvez accomplir cela en utilisant l'exemple suivant.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du site</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Accueil</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>
</nav>
```

#### **Exemples de navbar**

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Navigation_Bar___freeCodeCamp_Guide-1.png)