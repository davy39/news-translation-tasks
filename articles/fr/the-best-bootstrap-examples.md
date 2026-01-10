---
title: Les meilleurs exemples de Bootstrap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-04T00:27:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-bootstrap-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9edf740569d1a4ca3fa4.jpg
tags:
- name: Bootstrap
  slug: bootstrap
seo_title: Les meilleurs exemples de Bootstrap
seo_desc: 'Bootstrap is a popular front-end framework for web development. It contains
  pre-built components and design elements to style HTML content. Modern browsers
  such as Chrome, Firefox, Opera, Safari, and Internet Explorer support Bootstrap.

  Bootstrap inc...'
---

Bootstrap est un framework front-end populaire pour le développement web. Il contient des composants et des éléments de design pré-construits pour styliser le contenu HTML. Les navigateurs modernes tels que Chrome, Firefox, Opera, Safari et Internet Explorer supportent Bootstrap.

Bootstrap inclut un système de grille responsive pour des mises en page variées. C'est un excellent point de départ pour construire un site web adapté aux mobiles. Il inclut également une fonctionnalité JavaScript optionnelle, telle que le contenu pliable, les carrousels et les modales.

## Pourquoi utiliser Bootstrap ?

Bootstrap offre une solution facile à la fois pour le design et la réactivité. Il est rempli d'éléments magnifiques qui peuvent être davantage stylisés avec votre propre CSS personnalisé, ainsi qu'un système de grille complet pour garder votre site web responsive sur tous les écrans tout en utilisant une syntaxe propre et compréhensible. Vous pouvez construire un site web professionnel sans aucun CSS ou JavaScript et personnaliser facilement les éléments si nécessaire.

## Historique des versions

Twitter a initialement développé le framework Bootstrap comme un outil interne. Ils l'ont publié en tant que projet open source en août 2011.

Bootstrap 2 a été publié en janvier 2012. L'une des principales fonctionnalités était l'introduction du système de grille responsive à 12 colonnes. Bootstrap 3 est apparu en août 2013, passant à un design plat et une approche mobile-first. Bootstrap 4 est disponible en bêta depuis août 2017, et inclut maintenant Sass et Flexbox.

Bootstrap 4 a été en développement pendant deux ans avant de publier quelques versions bêta en 2017, tandis que la première version stable est sortie en janvier 2018. Certains changements notables incluent :

* Passage de Less à Sass ;
* Passage à Flexbox et amélioration du système de grille ;
* Ajout de cartes (remplaçant les puits, les miniatures et les panneaux) ;
* Et bien plus encore !

Au moment de la rédaction, la dernière version de Bootstrap est [4.1.3](http://blog.getbootstrap.com/2018/07/24/bootstrap-4-1-3/). Si vous souhaitez rester informé des dernières annonces, suivez-les [ici](http://blog.getbootstrap.com/).

## Fonctionnalités de Bootstrap

* Bootstrap 3 supporte les dernières versions de Google Chrome, Firefox, Internet Explorer, Opera et Safari (sauf sur Windows). Il supporte également les versions antérieures jusqu'à IE8 et la dernière version de Firefox Extended Support Release (ESR).[12]
* Depuis la version 2.0, Bootstrap supporte le design web responsive. Cela signifie que la mise en page des pages web s'ajuste dynamiquement, en tenant compte des caractéristiques de l'appareil utilisé (ordinateur de bureau, tablette, téléphone mobile).
* À partir de la version 3.0, Bootstrap a adopté une philosophie de design mobile-first, mettant l'accent sur le design responsive par défaut.
* La version 4.0 a ajouté la prise en charge de Sass et de flexbox.
* La version 4.1 a ajouté un nouveau contrôle de formulaire de plage personnalisé.
* Bootstrap ne vous limite pas à un format CSS fixe mais vous permet de développer rapidement en permettant des surcharges de style en utilisant la cascade pour ajouter/modifier les styles par défaut.

## Commencer

Bootstrap est un framework gratuit et open source développé par Twitter qui fournit une variété de modèles pour l'utilisation avec le développement web front-end. L'utilisation de Bootstrap facilite la conception d'un site web entièrement responsive et est un framework qui vaut la peine d'être appris.

### Comment ajouter Bootstrap à ma page ?

L'ajout de Bootstrap à votre page est un processus rapide, il suffit d'ajouter ce qui suit aux balises `<head>` dans votre code.

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
```

_Note : Ce ne sont que des exemples et peuvent changer sans préavis. Veuillez vous référer à un CDN pour les liens actuels à inclure dans votre projet._

Certains composants Bootstrap nécessitent d'autres fichiers JavaScript, consultez la documentation Bootstrap [ici](https://getbootstrap.com/docs/4.1/getting-started/introduction/#js) pour trouver les derniers fichiers de script.

Vous devrez également ajouter ce qui suit entre les balises `body` dans votre code. Avec Bootstrap, vous utiliserez des balises `<div>` lorsque vous utiliserez de nombreuses fonctionnalités de Bootstrap.

```html
<div class="alert alert-success" role="alert">
    <strong>Félicitations !</strong>
    <p>Bootstrap fonctionne maintenant sur cette page</p>
</div>
```

**Félicitations !**

Bootstrap fonctionne maintenant sur cette page.

### Installation de Bootstrap avec un gestionnaire de paquets

Un gestionnaire de paquets populaire est NPM ou Node Package Manager. Vous devrez installer Node.js, qui inclut le Node Package Manager. Visitez [Node.js](https://nodejs.org/en/) et téléchargez les fichiers nécessaires en fonction de votre système d'exploitation, puis installez-les.

Une fois installé et configuré, ouvrez la ligne de commande ou la console, et tapez ce qui suit dans le dossier du projet avec lequel vous souhaitez utiliser Bootstrap. Au moment de la rédaction, cela installera la version 4.0.0 de Bootstrap.

```html
npm install bootstrap@4.0.0 --save
```

Une fois que NPM a terminé le téléchargement et l'installation de Bootstrap 4, il y aura un nouveau dossier appelé `node_modules` dans votre dossier de projet s'il n'y était pas déjà.

* `/bootstrap` qui contient les versions CSS et Sass de nos fichiers.
* `/jquery` qui est utilisé par Bootstrap dans divers composants.
* `/tether` qui est une bibliothèque pour le positionnement des éléments.

## Système de grille

En résumé, le système de grille Bootstrap vous aide à créer des mises en page responsives, et il est composé d'un système de lignes et de colonnes qui vous aide à structurer votre contenu.

Les lignes sont des groupes horizontaux de colonnes, et chaque page a un maximum de 12 colonnes par ligne. Dans chaque ligne, le contenu est placé à l'intérieur des colonnes et peut s'étendre sur une à 12 colonnes.

Bootstrap a cinq différents types de niveaux de grille : Extra petit, Petit, Moyen, Grand et Extra grand. Il y a un point d'arrêt défini pour chacun de ces niveaux de grille. Bootstrap utilise des pixels pour définir les points d'arrêt des niveaux de grille.

### Conteneur

Le conteneur est l'élément le plus externe qui _contient_ votre grille. Utilisez `container` pour un conteneur de largeur fixe au milieu de l'écran (ajoute une marge supplémentaire sur les grands écrans) ou `container-fluid` pour une largeur complète.

```text
<div class="container"></div>
```

### Ligne

Utilisez `row` pour regrouper vos colonnes. Cela gardera tout bien aligné et vous aidera à structurer votre grille.

```text
<div class="row"></div>
```

### Colonnes

Les classes de colonnes indiquent le nombre de colonnes que vous souhaitez utiliser parmi les 12 possibles par ligne. Par exemple, `col-sm-6` signifierait que vos colonnes utilisent la moitié de la largeur de la `row` sur un petit écran, et `col-lg-4` utiliserait un tiers sur un grand écran.

Voici comment vous définiriez un préfixe de classe pour utiliser une largeur de colonne sur les différentes tailles d'écran :

* **Extra Petit** `col-1`
* **Petit** `col-sm-1`
* **Moyen** `col-md-1`
* **Grand** `col-lg-1`
* **Extra Grand** `col-xl-1`

```text
<div class="col-sm-1"></div>
```

### Exemple

Une grille en pleine largeur qui a quatre colonnes, chacune prenant une ligne complète sur les écrans xs, la moitié d'une ligne sur les écrans sm et md, et un quart de la largeur de la ligne sur les écrans qui sont grands et au-dessus :

```text
<div class="container-fluid">
  <div class="row">
    <div class="col-12 col-sm-6 col-lg-4">Première Colonne</div>
    <div class="col-12 col-sm-6 col-lg-4">Deuxième Colonne</div>
    <div class="col-12 col-sm-6 col-lg-4">Troisième Colonne</div>
    <div class="col-12 col-sm-6 col-lg-4">Quatrième Colonne</div>
  </div>
</div>
```

_Notez que `col-md` et `col-xl` ne sont pas définis, où une taille n'est pas définie, elle passera par défaut à la taille inférieure suivante qui a été spécifiée._

Bootstrap fournit un système de grille à 12 colonnes prêt à l'emploi pour une utilisation dans les mises en page. Considérez le code suivant.

```html
   <div class="container">
	<div class="row">
		<div class="col-md-6">Contenu</div>
		<div class="col-md-6">Contenu</div>
	<div>
   </div>
```

où :

```text
- col = colonne
- md = taille de l'écran
- 6 = largeur de la colonne
```

En tant que système de grille à 12 colonnes, toutes les largeurs de colonnes de grille définies par l'utilisateur doivent totaliser 12.

Les valeurs de taille d'écran peuvent être attribuées comme suit :

* xs - < 768px Téléphones
* sm - < 992px Tablettes
* md - < 1200px Ordinateurs portables
* lg - > 1200px Ordinateurs de bureau

Le code et l'image suivants montrent ce qui est possible en utilisant différentes largeurs de colonnes.

```html
	<div class="container">
		<div class="row">
			<div class="example col-md-6">Contenu</div>
			<div class="example col-md-6">Contenu</div>
		<div>
	</div>

	<div class="container">
		<div class="row">
			<div class="example col-md-4">Contenu</div>
			<div class="example col-md-4">Contenu</div>
			<div class="example col-md-4">Contenu</div>
		<div>
	</div>

	<div class="container">
		<div class="row">
			<div class="example col-md-3">Contenu</div>
			<div class="example col-md-3">Contenu</div>
			<div class="example col-md-3">Contenu</div>
			<div class="example col-md-3">Contenu</div>
		<div>
	</div>

	<div class="container">
		<div class="row">
			<div class="example col-md-2">Contenu</div>
			<div class="example col-md-2">Contenu</div>
			<div class="example col-md-2">Contenu</div>
			<div class="example col-md-2">Contenu</div>
			<div class="example col-md-2">Contenu</div>
			<div class="example col-md-2">Contenu</div>
		<div>
	</div>

	<div class="container">
		<div class="row">
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
			<div class="example col-md-1">Contenu</div>
		</div>
	</div>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-39.png)

## Boutons

Le framework Bootstrap vous offre diverses options de style pour les boutons. Ces styles vous aident à fournir une représentation visuelle à l'utilisateur de ce que le bouton peut faire.

### Comment utiliser

Pour utiliser les boutons Bootstrap, vous devez suivre les mêmes étapes que pour créer un bouton en HTML, sauf que vous appliquez également la classe CSS applicable au bouton. Un exemple de code a été fourni ci-dessous.

**Exemple de code :**

`<button type="button" class="btn btn-primary">Principal</button>`

Vous pouvez également utiliser les boutons Bootstrap avec les éléments `<a>` et `<input>` comme le montrent les exemples ci-dessous. Selon la [documentation Bootstrap](https://getbootstrap.com/docs/4.0/components/buttons/),

Lorsque vous utilisez des classes de boutons sur des éléments utilisés pour déclencher des fonctionnalités dans la page (comme le contenu pliable), plutôt que de lier à de nouvelles pages ou sections dans la page actuelle, ces liens doivent recevoir un `role="button"` pour transmettre correctement leur objectif aux technologies d'assistance telles que les lecteurs d'écran.

`<a class="btn btn-primary" href="#" role="button">Ce bouton est un lien</a>`

`<input class="btn btn-primary" type="submit" value="Soumettre">`

### Liste des classes de boutons

Voici une liste des classes CSS que Bootstrap fournit pour les boutons. Elles donnent la couleur de fond aux boutons.

`.btn` C'est le bouton de base de Bootstrap. C'est un prérequis si vous voulez que les autres boutons Bootstrap fonctionnent correctement.

`<button type="button" class="btn">Basique</button>`

`.btn-primary` Bouton principal de Bootstrap. La couleur par défaut est #007bff.

`<button type="button" class="btn btn-primary">Principal</button>`

`.btn-secondary` Bouton secondaire de Bootstrap. La couleur par défaut est #6c757d.

`<button type="button" class="btn btn-secondary">Secondaire</button>`

`.btn-success` Bouton de succès de Bootstrap. La couleur par défaut est #28a745.

`<button type="button" class="btn btn-success">Succès</button>`

`.btn-info` Bouton d'information de Bootstrap. La couleur par défaut est #17a2b8.

`<button type="button" class="btn btn-info">Info</button>`

`.btn-warning` Bouton d'avertissement de Bootstrap. La couleur par défaut est #ffc107.

`<button type="button" class="btn btn-warning">Avertissement</button>`

`.btn-danger` Bouton de danger de Bootstrap. La couleur par défaut est #dc3545.

`<button type="button" class="btn btn-danger">Danger</button>`

`.btn-link` Bouton de lien de Bootstrap.

`<button type="button" class="btn btn-link">Lien</button>`

`.btn-light` Bouton clair de Bootstrap.

`<button type="button" class="btn btn-light">Clair</button>`

`.btn-dark` Bouton sombre de Bootstrap.

`<button type="button" class="btn btn-dark">Sombre</button>`

`.btn-dark` C'est le bouton sombre de Bootstrap.

`.btn-secondary` C'est le bouton secondaire de Bootstrap.

### Tailles des boutons

Voici une liste des classes CSS pour différentes tailles de boutons.

`.btn-lg` Bouton grand de Bootstrap.

`<button type="button" class="btn btn-lg">Grand</button>`

`.btn-md` C'est le bouton moyen de Bootstrap.

`<button type="button" class="btn btn-md">Moyen</button>`

`.btn-sm` Bouton petit de Bootstrap.

`<button type="button" class="btn btn-sm">Petit</button>`

`.btn-md` C'est le bouton moyen de Bootstrap.

`.btn-xs` C'est le bouton extra petit de Bootstrap.

`<button type="button" class="btn btn-xs">Extra Petit</button>`

`.btn-block` C'est le bouton en pleine largeur de Bootstrap.

### État du bouton désactivé

Cela est utilisé pour montrer que le bouton est désactivé en estompant le bouton. Cela peut être réalisé en ajoutant "disabled" à la balise `<button>`.

`.btn-block` C'est le bouton de niveau bloc de Bootstrap. Ils s'étendent en fait sur toute la largeur de leur élément parent. Par exemple, un élément de formulaire avec une largeur de 200px, cela signifie que le bouton btn-block aurait une largeur de 200px.

### Boutons en contour

Il est possible d'avoir également des boutons en contour plutôt que des boutons entièrement colorés. Cela est réalisé en plaçant le préfixe `outline` entre la classe de bouton que vous souhaitez. Un exemple d'utilisation serait le suivant :

`<button type="button" class="btn btn-outline-primary">Principal</button>`

`<button type="button" class="btn btn-outline-secondary">Secondaire</button>`

`<button type="button" class="btn btn-outline-success">Succès</button>`

`<button type="button" class="btn btn-outline-danger">Danger</button>`

`<button type="button" class="btn btn-outline-warning">Avertissement</button>`

`<button type="button" class="btn btn-outline-info">Info</button>`

`<button type="button" class="btn btn-outline-light">Clair</button>`

`<button type="button" class="btn btn-outline-dark">Sombre</button>`

Les boutons en contour font partie de Bootstrap depuis la version 4 - assurez-vous que vous utilisez la bonne version si vous ne parvenez pas à les faire fonctionner.

### Boutons en ligne

Vous pouvez créer une ligne de boutons en ligne en ajoutant la classe `.d-inline-block` à l'élément qui définit l'affichage du bouton en bloc en ligne. Par exemple : `<button class="btn btn-primary d-inline-block btn-lg"></button>`

### Groupement de boutons

Il est possible de regrouper plus d'un bouton pour certaines utilisations comme la pagination. Le regroupement de boutons peut être fait en créant un `div` parent pour tous les boutons que vous souhaitez regrouper, en utilisant la classe `.btn-group` sur ce `div` :

```html
<div class="btn-group" role="group" aria-label="Exemple de base">
  <button type="button" class="btn btn-secondary">Gauche</button>
  <button type="button" class="btn btn-secondary">Milieu</button>
  <button type="button" class="btn btn-secondary">Droite</button>
</div>
```

## Menus déroulants

Bootstrap fournit des menus déroulants en tant que plugin pour afficher des listes de liens. Un menu déroulant est un bouton qui bascule l'affichage d'une liste de liens.

Les menus déroulants de Bootstrap sont conçus pour être génériques et applicables à diverses situations. Par exemple, il est possible de créer des menus déroulants qui contiennent des champs de recherche ou des formulaires de connexion.

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Exemple de menu déroulant
  </button>
  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Une autre action</a>
    <a class="dropdown-item" href="#">Autre chose ici</a>
  </div>
</div>
```

La classe _.dropdown_ indique un menu déroulant.

Pour ouvrir le menu déroulant, utilisez un bouton ou un lien avec une classe _.dropdown-toggle_ et l'attribut _data-toggle="dropdown_.

La classe _.caret_ crée une icône de flèche en forme de chevron (▼), qui indique que le bouton est un menu déroulant.

Ajoutez la classe _.dropdown-menu_ à un élément de liste non ordonnée pour construire le menu déroulant.

## Barre de navigation

Le framework Bootstrap vous offre une fonctionnalité appelée barres de navigation. En bref, une barre de navigation (également appelée navbar) est un en-tête en haut de la page pour afficher des informations de navigation.

### Comment utiliser

Pour utiliser les barres de navigation Bootstrap, vous ajoutez un élément `<nav>` en haut à l'intérieur de l'élément `<body>` de votre page web. Il existe divers styles que vous pouvez ajouter pour personnaliser l'affichage de vos barres de navigation.

Voici le code nécessaire pour créer une barre de navigation basique :

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du Site</a>
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

### Styles de barre de navigation

Bootstrap fournit un ensemble de classes dans le framework Bootstrap pour styliser vos barres de navigation. Ces classes sont les suivantes :

* `navbar navbar-default` C'est le style par défaut pour vos barres de navigation.
* `navbar navbar-inverse` C'est similaire au style par défaut sauf que les couleurs sont inversées.

### Ajout de menus déroulants à la barre de navigation

Vous pouvez inclure un menu déroulant dans une barre de navigation. Cette fonctionnalité nécessite que vous incluez le fichier JavaScript de Bootstrap pour qu'elle fonctionne.

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

### Ajout de boutons à la barre de navigation

Vous pouvez ajouter des boutons sur la barre de navigation. Les classes de boutons Bootstrap existantes fonctionnent, mais vous devrez inclure la classe `navbar-btn` à la fin de la liste des classes.

```html
<button class="btn navbar-btn">Bouton</button>
```

### Ajout d'un logo ou d'un nom de marque à la barre de navigation

La classe `navbar-brand` peut être appliquée à la plupart des éléments, mais un ancrage fonctionne mieux car certains éléments peuvent nécessiter des classes utilitaires ou des styles personnalisés.

```html
<!-- En tant que lien -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
</nav>
```

```html
<!-- En tant qu'en-tête -->
<nav class="navbar navbar-light bg-light">
  <span class="navbar-brand mb-0 h1">Navbar</span>
</nav>
```

### Ajout de formulaires à la barre de navigation

Vous pouvez également ajouter des formulaires à la barre de navigation. Cela pourrait être utilisé pour des tâches telles qu'un champ de recherche, un champ de connexion rapide, etc.

```html
<form class="navbar-form navbar-right">
  <div class="form-group">
      <input type="text" class="form-control" placeholder="Rechercher">
  </div>  
  <button type="submit" class="btn btn-default">Rechercher</button>  
</form>
```

### Alignement des éléments à droite sur la barre de navigation

Dans certains cas, vous pouvez vouloir aligner des éléments dans une barre de navigation à droite (par exemple, un bouton de connexion ou d'inscription). Pour ce faire, vous devrez utiliser la classe `navbar-right`.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du Site</a>
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

### Affichage de la barre de navigation indépendamment du défilement

Dans certains cas, vous pouvez vouloir garder la barre de navigation en haut ou en bas de l'écran, indépendamment du défilement. Vous devrez ajouter soit la classe `navbar-fixed-top` ou `navbar-fixed-bottom` à l'élément `<nav>`.

```html
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du Site</a>
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

### Réduction de la barre de navigation

Sur un petit écran (comme un téléphone ou une tablette), la barre de navigation va prendre trop de place. Heureusement, l'option de réduire la barre de navigation existe. Vous pouvez accomplir cela en utilisant l'exemple suivant.

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Nom du Site</a>
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

## Jumbotron

`Jumbotron` est un composant léger et flexible pour mettre en avant du contenu de style unité héroïque. `Jumbotron` est un composant responsive dont le but principal est de focaliser l'attention du visiteur ou de mettre en évidence une information spéciale.

Jumbotron utilise presque tout autre code Bootstrap pour augmenter davantage sa valeur d'engagement. Il fonctionne avec des images, des polices agrandies, différents styles de fond, etc.

### Fonctionnalités les plus attrayantes de Jumbotron

* Mettre en avant les messages marketing sur votre site
* Présentation de projet
* Introduction d'article
* Présentation d'image

### Comment utiliser

Utilisez un élément `<div>` avec la classe `.jumbotron` pour créer un jumbotron :

```text
<div class="jumbotron">
  <h1 class="display-4">Bonjour le monde !</h1>
  <p class="lead">Ceci est une unité héroïque simple, un composant de style jumbotron simple pour attirer l'attention supplémentaire sur le contenu ou les informations en vedette.</p>
  <hr class="my-4">
  <p>Il utilise des classes utilitaires pour la typographie et l'espacement pour espacer le contenu dans le conteneur plus grand.</p>
  <a class="btn btn-primary btn-lg" href="#" role="button">En savoir plus</a>
</div>
   
```

### Jumbotron fluide

Pour rendre le jumbotron en pleine largeur et sans coins arrondis, ajoutez la classe modificatrice `.jumbotron-fluid` et ajoutez un `.container` ou `.container-fluid` à l'intérieur.

```text
<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Jumbotron fluide</h1>
    <p class="lead">Ceci est un jumbotron modifié qui occupe tout l'espace horizontal de son parent.</p>
  </div>
</div>
```

## Formulaires

Le framework Bootstrap fournit une fonctionnalité de formulaire que vous pouvez utiliser pour créer facilement de beaux formulaires HTML. L'utilisation du formulaire Bootstrap donne à chaque élément de formulaire individuel un style global unifié. Le formulaire Bootstrap ajoute l'espacement et l'apparence appropriés à chaque élément.

Chaque élément de formulaire Bootstrap doit avoir une classe _form-control_. Cette classe est la manière dont Bootstrap sait quels éléments styliser. Tous les éléments textuels comme **input**, **textarea** et **select** qui ont la classe _form-control_ auront une largeur de 100% par défaut.

Il existe deux types de formulaires Bootstrap, qui sont :

* Formulaire en ligne - crée le formulaire sur une seule ligne. Utile pour les formulaires de connexion dans une barre de navigation
* Formulaire horizontal - crée un formulaire avec chaque élément dans une ligne différente

### Exemple de formulaire basique

```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Adresse e-mail</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Mot de passe</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Mot de passe">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">Fichier à télécharger</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Exemple de texte d'aide de niveau bloc ici.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Cochez-moi
    </label>
  </div>
  <button type="submit" class="btn btn-default">Soumettre</button>
</form>
```

### Exemple de formulaire en ligne

```html
<form class="form-inline">
  <div class="form-group">
    <label for="exampleInputName2">Nom</label>
    <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">Email</label>
    <input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
  </div>
  <button type="submit" class="btn btn-default">Envoyer l'invitation</button>
</form>
```

### Exemple de formulaire horizontal

```html
<form class="form-horizontal">
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword3" class="col-sm-2 control-label">Mot de passe</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3" placeholder="Mot de passe">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <div class="checkbox">
        <label>
          <input type="checkbox"> Se souvenir de moi
        </label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-default">Se connecter</button>
    </div>
  </div>
</form>
```

## Entrées de formulaire

Bootstrap supporte les contrôles de formulaire suivants :

1. input
2. textarea
3. checkbox
4. radio
5. select
6. range

### 1. Input

Bootstrap supporte tous les types d'entrée HTML5 : text, password, datetime, datetime-local, date, month, time, week, number, email, url, search, tel, et color.

**Note : Les entrées ne seront PAS entièrement stylisées si leur type n'est pas correctement déclaré !**

L'exemple suivant contient deux éléments d'entrée ; l'un de type text et l'autre de type password :

```html
<div class="form-group">
  <label for="usr">Nom :</label>
  <input type="text" class="form-control" id="usr">
</div>
<div class="form-group">
  <label for="pwd">Mot de passe :</label>
  <input type="password" class="form-control" id="pwd">
</div>
```

### 2. Textarea

L'exemple suivant contient une textarea :

```html
<div class="form-group">
  <label for="comment">Commentaire :</label>
  <textarea class="form-control" rows="5" id="comment"></textarea>
</div>
```

### 3. Cases à cocher

Les cases à cocher sont utilisées si vous voulez que l'utilisateur sélectionne un nombre quelconque d'options parmi une liste d'options prédéfinies.

L'exemple suivant contient trois cases à cocher. La dernière option est désactivée :

```html
<div class="checkbox">
  <label>
  <input type="checkbox" value="">Option 1</label>
</div>
<div class="checkbox">
  <label>
  <input type="checkbox" value="">Option 2</label>
</div>
<div class="checkbox disabled">
  <label>
  <input type="checkbox" value="" disabled>Option 3</label>
</div>
```

Utilisez la classe **.checkbox-inline** si vous voulez que les cases à cocher apparaissent sur la même ligne :

```html
<label class="checkbox-inline"><input type="checkbox" value="">Option 1</label>
<label class="checkbox-inline"><input type="checkbox" value="">Option 2</label>
<label class="checkbox-inline"><input type="checkbox" value="">Option 3</label>
```

### 4. Boutons radio

Les boutons radio sont utilisés si vous voulez limiter l'utilisateur à une seule sélection parmi une liste d'options prédéfinies.

L'exemple suivant contient trois boutons radio. La dernière option est désactivée :

```html
<div class="radio">
  <label><input type="radio" name="optradio">Option 1</label>
</div>
<div class="radio">
  <label><input type="radio" name="optradio">Option 2</label>
</div>
<div class="radio disabled">
  <label><input type="radio" name="optradio" disabled>Option 3</label>
</div>
```

Utilisez la classe **.radio-inline** si vous voulez que les boutons radio apparaissent sur la même ligne :

```html
<label class="radio-inline"><input type="radio" name="optradio">Option 1</label>
<label class="radio-inline"><input type="radio" name="optradio">Option 2</label>
<label class="radio-inline"><input type="radio" name="optradio">Option 3</label>
```

### 5. Sélection (Liste)

Les listes de sélection sont utilisées si vous voulez permettre à l'utilisateur de choisir parmi plusieurs options.

L'exemple suivant contient une liste déroulante (liste de sélection) :

```html
<div class="form-group">
  <label for="sel1">Liste de sélection :</label>
  <select class="form-control" id="sel1">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
  </select>
</div>
```

### 6. Plage

Les listes de sélection sont utilisées si vous voulez permettre à l'utilisateur de choisir parmi plusieurs options.

L'exemple suivant contient une liste déroulante (liste de sélection) :

```html
<form>
  <div class="form-group">
    <label for="formControlRange">Exemple d'entrée de plage</label>
    <input type="range" class="form-control-range" id="formControlRange">
  </div>
</form>
```

### Comment rendre les entrées Bootstrap accessibles

Les champs de saisie doivent avoir des étiquettes ou une autre forme d'identifiant tel que des balises WAI-ARIA pour répondre aux directives d'accessibilité du contenu Web ou [WCAG](https://www.w3.org/WAI/tutorials/forms/) en abrégé. Afin que les lecteurs d'écran transmettent avec précision à un utilisateur les étiquettes associées aux entrées, les étiquettes doivent référencer l'entrée correspondante.

Cela peut être fait en utilisant le paramètre `for` en HTML :

```html
<label for="email-input">Entrez l'email</label>
<input type="email" class="form-control" id="email-input" placeholder="Entrez l'email">
```

L'attribut `for` de l'étiquette **référence toujours** le champ de saisie par son **ID**. Cela indique au lecteur d'écran que cette étiquette est définitivement pour ce champ de saisie, ce qui minimisera la confusion pour tout utilisateur utilisant un lecteur d'écran pour visiter un site web. Dans l'exemple ci-dessus, si un utilisateur clique sur le mot "Entrez l'email", alors l'utilisateur pourra taper. Si l'attribut 'for' n'était pas attaché à l'étiquette, alors si un utilisateur clique sur les mots 'Entrez l'email', rien ne se passerait. L'utilisateur devrait cliquer sur le champ de saisie d'email pour pouvoir taper.

## Tableaux

### Tableau de base

Pour obtenir l'exemple de style de base, ajoutez la classe de base `.table` à tout élément `<table>`.

```text
<table class="table">
  ...
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-40.png)

### En-tête de tableau

Vous pouvez définir une section d'en-tête séparée dans la structure de votre tableau. Voici un exemple :

```html
<table class="table">
    <thead class=theat-dark>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Premier</th>
      <th scope="col">Dernier</th>
      <th scope="col">Handle</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Bob</td>
      <td>Robo</td>
      <td>@bro</td>
    </tr>
  </tbody>
</table>
```

### Tableau rayé

Pour obtenir l'effet de lignes rayées (zébrées) dans les tableaux, utilisez `.table-striped` en plus de `.table` sur tout élément `<table>`. Les tableaux rayés sont stylisés via le sélecteur CSS `:nth-child`, qui n'est pas disponible dans Internet Explorer 8.

```text
<table class="table table-striped">
  ...
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-41.png)

### Tableau bordé

Pour obtenir un tableau bordé, utilisez `.table-bordered` en plus de `.table` sur tout élément `<table>`.

```text
<table class="table table-bordered">
  ...
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-42.png)

### Tableau survol

Pour obtenir l'effet de survol des lignes sur les tableaux, utilisez `.table-hover` en plus de `.table` sur tout élément `<table>`.

```text
<table class="table table-hover">
  ...
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-43.png)

### Tableau condensé

Pour obtenir un tableau condensé, utilisez `.table-condensed` en plus de `.table` sur tout élément `<table>`.

```text
<table class="table table-condensed">
  ...
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-44.png)

### Tableau responsive

Pour obtenir un tableau responsive en enveloppant tout tableau `.table` dans un élément `.table-responsive`.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-45.png)

Les développeurs peuvent changer le style de chaque ligne `<tr>` et/ou cellule `<td>` individuelle en utilisant des **classes contextuelles**.

* `.active` - Applique la couleur de survol à une ligne ou cellule particulière
* `.success` - Indique une action réussie ou positive
* `.info` - Indique un changement ou une action informative neutre
* `.warning` - Indique un avertissement qui pourrait nécessiter une attention
* `.danger` - Indique une action dangereuse ou potentiellement négative

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-46.png)