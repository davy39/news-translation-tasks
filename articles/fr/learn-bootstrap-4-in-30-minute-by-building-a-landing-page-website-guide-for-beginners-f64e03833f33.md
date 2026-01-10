---
title: Apprendre Bootstrap 4 en 30 minutes en construisant un site web de page de
  destination
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-17T19:31:55.000Z'
originalURL: https://freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1_a4TocueD3AqEpsDDv4bA.jpeg
tags:
- name: bootstrap 4
  slug: bootstrap-4
- name: Design
  slug: design
- name: front end
  slug: front-end
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre Bootstrap 4 en 30 minutes en construisant un site web de page
  de destination
seo_desc: 'By SaidHayani@


  A guide for beginners


  “Bootstrap is a free, open-source front-end library for designing websites and web
  applications. It contains HTML- and CSS-based design templates for everything from
  typography, forms, buttons, navigation and ot...'
---

Par SaidHayani@

![Image](https://cdn-media-1.freecodecamp.org/images/1*a9OoxPsn-hrbjYpbNV6DzA.gif)

### Un guide pour les débutants

> « Bootstrap est une bibliothèque front-end gratuite et open-source pour la conception de sites web et d'applications web. Elle contient des modèles de conception basés sur HTML et CSS pour tout, de la typographie, des formulaires, des boutons, de la navigation et d'autres composants d'interface, ainsi que des extensions JavaScript. Contrairement à de nombreux autres frameworks web, Bootstrap se concentre uniquement sur le développement front-end. » — [Wikipedia](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)

> [Salut, avant de commencer, consultez mon cours complet pour apprendre Bootstrap 4, où vous apprendrez les nouvelles fonctionnalités de Bootstrap et comment les utiliser pour créer de meilleures expériences utilisateur](https://skl.sh/2NbSAYj).

Il existe de nombreuses versions de Bootstrap, la version 4 étant la plus récente. Dans cet article, nous allons construire un site web en utilisant Bootstrap 4.

### Prérequis

Avant de commencer, il y a quelques compétences que vous devrez connaître pour apprendre et utiliser le framework Bootstrap :

* Les bases de HTML
* Une connaissance de base de CSS
* Et un peu de JQuery de base

### Table des matières

Nous allons couvrir les sujets suivants tout en construisant le site web :

* [Téléchargement et installation de Bootstrap 4](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#telechargement-et-installation-de-bootstrap-4)
* [Les nouvelles fonctionnalités de Bootstrap 4](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#les-nouvelles-fonctionnalites-de-bootstrap-4)
* [Système de grille Bootstrap](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#systeme-de-grille-bootstrap)
* [Barre de navigation](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#barre-de-navigation)
* [En-tête](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#entete)
* [Boutons](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#boutons)
* [Section À propos](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#section-a-propos)
* [Section Portfolio](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#section-portfolio)
* [Section Blog](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#section-blog)
* [Cartes](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#cartes)
* [Section Équipe](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#section-equipe)
* [Formulaire de contact](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#formulaire-de-contact)
* [Polices](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#polices)
* [Effet de défilement](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#effet-de-defilement)
* [Conclusion](https://www.freecodecamp.org/news/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33/#conclusion)

### Téléchargement et installation de Bootstrap 4

Il existe trois façons d'installer et d'inclure Bootstrap 4 pour votre projet :

1. Utiliser npm

Vous pouvez installer Bootstrap 4 en exécutant cette commande `npm install bootstrap`

2. Utiliser un Content Delivery Network (CDN)

En incluant ce lien dans votre projet entre les balises head :

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
```

3. Télécharger la bibliothèque [Bootstrap 4](http://getbootstrap.com/) et l'utiliser localement.

La structure de notre projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyhB-vVWlIwbNpDH_JNZYg.png)

### Les nouvelles fonctionnalités de Bootstrap 4

Quoi de neuf dans Bootstrap 4 ? Et quelles sont les différences entre Bootstrap 3 et 4 ?

Bootstrap 4 arrive maintenant avec certaines fonctionnalités géniales qui n'existaient pas dans la dernière version :

* Bootstrap 4 est écrit en utilisant Flexbox Grid, alors que Bootstrap 3 était écrit en utilisant la méthode float.   
Si vous êtes nouveau dans Flexbox, consultez [ce tutoriel](https://scrimba.com/p/pL65cJ/canLGCw).
* Bootstrap 4 utilise les unités CSS `rem` alors que Bootstrap 3 utilise `px`.  
[Voyez comment ces deux unités diffèrent.](https://zellwk.com/blog/media-query-units/)
* Les panneaux, les miniatures et les puits ont été complètement supprimés.   
Vous pouvez lire plus en détail sur les changements globaux et les fonctionnalités supprimées de Bootstrap 4 [ici](http://getbootstrap.com/docs/4.0/migration/#global-changes).

Sans entrer trop dans les détails ici, passons à d'autres choses importantes.

### Le système de grille Bootstrap

Le système de grille Bootstrap vous aide à créer votre mise en page et à construire facilement un site web réactif. Il n'y a pas eu de changements dans les noms de classes, à l'exception de la classe `.xs`, qui n'existe plus dans Bootstrap 4.

La grille est divisée en 12 colonnes, donc votre mise en page sera basée sur cela.

Pour utiliser le système de grille, vous devrez ajouter une classe `.row` à la div principale.

```html
col-lg-2 // classe utilisée pour les grands appareils comme les ordinateurs portables
col-md-2 // classe utilisée pour les appareils moyens comme les tablettes
col-sm-2// classe utilisée pour les petits appareils comme les téléphones mobiles
```

### Barre de navigation

![Image](https://cdn-media-1.freecodecamp.org/images/1*VbIQyNsPrZ143nV8LaHLAg.png)

Le wrapper de la barre de navigation est assez cool dans Bootstrap 4. Il est très utile lorsqu'il s'agit de construire une barre de navigation réactive.

Pour l'obtenir, nous allons ajouter la classe `navbar` à notre fichier `**index.html**` :

```html
<!-- navbar -->  
 <nav class="navbar navbar-expand-lg fixed-top ">  
 <a class="navbar-brand" href="#">Accueil</a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Basculer la navigation">  
 <span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse " id="navbarSupportedContent">     <ul class="navbar-nav mr-4">
 <li class="nav-item">
     <a class="nav-link" data-value="about" href="#">À propos</a>        </li>  
<li class="nav-item">
    <a class="nav-link " data-value="portfolio" href="#">Portfolio</a>    
 </li>
 <li class="nav-item"> 
    <a class="nav-link " data-value="blog" href="#">Blog</a>         </li>   
<li class="nav-item">  
   <a class="nav-link " data-value="team" href="#">         Équipe</a>       </li>  
<li class="nav-item"> 
 <a class="nav-link " data-value="contact" href="#">Contact</a>       </li> 
</ul> 
</div></nav>
```

<iframe src="https://codesandbox.io/embed/38nnqwl8n6?fontsize=14" title="38nnqwl8n6" allow="geolocation; microphone; camera; midi; vr; accelerometer; gyroscope; payment; ambient-light-sensor; encrypted-media" style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;" sandbox="allow-modals allow-forms allow-popups allow-scripts allow-same-origin"></iframe>

Créez et incluez un fichier `**main.css**` afin de pouvoir personnaliser le style CSS.

Placez ceci dans la balise `head` de votre fichier `**index.html**` :

```html
<link rel="stylesheet" type="text/css" href="css/main.css">
```

Ajoutons quelques couleurs à notre barre de navigation :

```css
.navbar{ background:#F97300;}

.nav-link , .navbar-brand{ color: #f4f4f4; cursor: pointer;}

.nav-link{ margin-right: 1em !important;}

.nav-link:hover{ background: #f4f4f4; color: #f97300; }

.navbar-collapse{ justify-content: flex-end;}

.navbar-toggler{  background:#fff !important;}
```

La nouvelle grille Bootstrap est construite avec le système Flexbox, donc pour l'alignement, vous devez utiliser une propriété Flexbox. Par exemple, pour placer le menu de la barre de navigation à droite, nous devons ajouter une propriété `justify-content` et la définir sur `flex-end`.

```css
.navbar-collapse{
 justify-content: flex-end;
}
```

Ajoutez la classe `.fixed-top` à la barre de navigation pour lui donner une position fixe.

Pour rendre la couleur de fond de la barre de navigation claire, ajoutez `.bg-light`. Pour un fond sombre, ajoutez `.bg-dark`, et pour un fond bleu clair, ajoutez   
`.bg-primary`.

Voici à quoi cela devrait ressembler :

```css
.bg-dark{
background-color:#343a40!important
}
.bg-primary{
background-color:#007bff!important
}
```

### En-tête

```html
<header class="header">
  
</header>
```

Essayons de créer une mise en page pour l'en-tête.

Ici, nous voulons nous assurer que l'en-tête prend la hauteur de la fenêtre, donc nous allons utiliser un peu de code `JQuery`.

Tout d'abord, créez un fichier nommé `**main.js**` et incluez-le dans le fichier `**index.html**` avant la balise de fermeture `body` :

```html
<script type="text/javascript" src='js/main.js'></script>
```

Dans le fichier `main.js`, insérez ce petit code de JQuery :

```js
$(document).ready(function(){
 $('.header').height($(window).height());
 
})
```

Ce serait assez cool si nous définissions une belle image de fond pour l'en-tête :

```css
/* style de l'en-tête */
.header{
 background-image: url('../images/headerback.jpg');
 background-attachment: fixed;
 background-size: cover;
 background-position: center;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*LmLTI-enV2RSKjsO9hzPxQ.png)

Ajoutons un calque pour rendre l'en-tête un peu plus professionnel :

Ajoutez ceci à votre fichier `**index.html**` :

```html
<header class="header">
  <div class="overlay"></div>
</header>
```

Puis, ajoutez ceci à votre fichier `**main.css**` :

```css
.overlay{
 position: absolute;
 min-height: 100%;
 min-width: 100%;
 left: 0;
 top: 0;
 background: rgba(244, 244, 244, 0.79);
}
```

Maintenant, nous devons ajouter une description à l'intérieur de l'en-tête.

Pour envelopper notre description, nous allons d'abord créer une `div` et lui donner une classe `.container`.

`.container` est une classe Bootstrap qui vous aidera à envelopper votre contenu et à rendre votre mise en page plus réactive :

```html
<header class="header">
  <div class="overlay"></div>
   <div class="container">
    
   </div>
  
</header>
```

Ensuite, ajoutez une autre `div` qui contiendra la description.

```html
<div class="description ">
   <h1>    Bonjour, bienvenue sur mon site officiel
    <p>    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>   
 <button class="btn btn-outline-secondary btn-lg">Voir plus</button>   </h1>  
</div>
```

Nous lui donnerons une classe `.description` et ajouterons la classe `.text-center` pour nous assurer que le contenu est placé au centre de la page.

#### Boutons

Ajoutez la classe `.btn btn-outline-secondary` à l'élément `button`. Il existe de nombreuses autres classes Bootstrap pour les boutons.

Consultez quelques exemples :

[**CodePen Embed — boutons dans Bootstrap 4**](https://codepen.io/Saidalmaghribi/embed/oEWgbw)  
[_Buttons Button primary Button default Button danger Button info Button warning Button dark Button success Buttons…_codepen.io](https://codepen.io/Saidalmaghribi/embed/oEWgbw)

Voici à quoi ressemble le style pour `.description` dans le fichier `**main.css**` :

```css
.description{
    position: absolute;
    top: 30%;
    margin: auto;
    padding: 2em;
    
}
.description h1{
 color:#F97300 ;
}
.description p{
 color:#666;
 font-size: 20px;
 width: 50%;
 line-height: 1.5;
}
.description button{
 border:1px  solid #F97300;
 background:#F97300;
 color:#fff;
}
```

Après tout cela, notre en-tête ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kV7umhOF5QPveMmADXUCSw.png)

Cool, n'est-ce pas :).

### Section À propos

![Image](https://cdn-media-1.freecodecamp.org/images/1*VWnyo3Jg4brsW5YRZToCiQ.png)

Dans cette section, nous allons utiliser une partie de la grille Bootstrap pour diviser la section en deux parties.

Pour commencer notre grille, nous devons assigner la classe `.row` à la div parente.

```html
<div class="row"></div>
```

La première section sera à gauche et contiendra une image, la deuxième section sera à droite et contiendra une description.

Chaque `div` prendra 6 colonnes — cela signifie la moitié de la section. N'oubliez pas qu'une grille est divisée en 12 colonnes.

Dans la première `div` du côté gauche :

```html
<div class="row"> 
 // côté gauche
<div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/team-3.jpg" class="img-fluid">
    <span class="text-justify">Développeur Web</span>
 </div>
 
</div>
```

Après avoir ajouté les éléments HTML du côté droit, la structure du code ressemblera à ceci :

```html
<div class="row">
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/team-3.jpg" class="img-fluid">
    <span class="text-justify">Développeur Web</span>
   </div>
   <div class="col-lg-8 col-md-8 col-sm-12 desc">
     
    <h3>D.John</h3>
    <p>
       ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
     tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
     quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
     consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
     cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
     proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
   </div>
  </div>
```

Voici comment je l'ai fait ressembler :

```css
.about{
 margin: 4em 0;
 padding: 1em;
 position: relative;
}
.about h1{
 color:#F97300;
 margin: 2em;
}
.about img{
 height: 100%;
    width: 100%;
    border-radius: 50%
}
.about span{
 display: block;
 color: #888;
 position: absolute;
 left: 115px;
}
.about .desc{
 padding: 2em;
 border-left:4px solid #10828C;
}
.about .desc h3{
 color: #10828C;
}
.about .desc p{
 line-height:2;
 color:#888;
}
```

### Section Portfolio

Maintenant, passons à la partie suivante et créons une section portfolio qui contiendra une galerie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fNaqxcagCvh8Ue3lZvK6Vw.png)

La structure de notre code HTML pour la section Portfolio ressemble à ceci :

```html
<!-- portfolio -->
<div class="portfolio">
     <h1 class="text-center">Portfolio</h1>
 <div class="container">
  <div class="row">
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port13.png" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port1.png" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port6.png" class="img-fluid">
   </div>
      
<div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port3.png" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port11.png" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/electric.png" class="img-fluid">
   </div>
      
<div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/Classic.jpg" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port1.png" class="img-fluid">
   </div>
   <div class="col-lg-4 col-md-4 col-sm-12">
    <img src="images/portfolio/port8.png" class="img-fluid">
   </div>
  </div>
 </div>
</div>
```

Ajoutez `.img-fluid` à chaque image pour la rendre réactive.

Chaque élément de notre galerie prendra 4 colonnes (rappel, `col-md-4` pour les appareils moyens, `col-lg-4` pour les grands appareils). Cela équivaut à 33,33333 % sur les grands appareils comme les ordinateurs de bureau et les grandes tablettes, et 12 colonnes sur un petit appareil (comme l'iPhone, les appareils mobiles) prendront 100 % du conteneur.

Ajoutons un peu de style à notre galerie :

```css
/*Portfolio*/
.portfolio{
 margin: 4em 0;
    position: relative; 
}
.portfolio h1{
 color:#F97300;
 margin: 2em; 
}
.portfolio img{
  height: 15rem;
  width: 100%;
  margin: 1em;
  
}
```

### **Section Blog**

![Image](https://cdn-media-1.freecodecamp.org/images/1*3y9bIjRwf2RtGRzMIXwZIQ.png)

#### Cartes

Les cartes dans Bootstrap 4 rendent la conception de blogs beaucoup plus facile. Les cartes sont appropriées pour les articles et les publications.

Pour créer une carte, nous utilisons la classe `.card` et l'assignons à un élément _div_,

La classe de carte contient de nombreuses fonctionnalités :

* `.card-header` : définit l'en-tête de la carte
* `.card-body` : pour le corps de la carte
* `.card-title` : le titre de la carte
* `card-footer` : définit le pied de page de la carte.
* `.card-image` : pour l'image de la carte

Ainsi, le HTML de notre site web devrait maintenant ressembler à ceci :

```html
<!-- Section des publications -->
<div class="blog">
 <div class="container">
 <h1 class="text-center">Blog</h1>
  <div class="row">
   <div class="col-md-4 col-lg-4 col-sm-12">
    <div class="card">
     <div class="card-img">
      <img src="images/posts/polit.jpg" class="img-fluid">
     </div>
     
     <div class="card-body">
     <h4 class="card-title">Titre de l'article</h4>
      <p class="card-text">
       
       proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
     </div>
     <div class="card-footer">
      <a href="" class="card-link">Lire la suite</a>
     </div>
    </div>
   </div>
   <div class="col-md-4 col-lg-4 col-sm-12">
    <div class="card">
     <div class="card-img">
      <img src="images/posts/images.jpg" class="img-fluid">
     </div>
     
     <div class="card-body">
        <h4 class="card-title">Titre de l'article</h4>
      <p class="card-text">
       
       proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
     </div>
     <div class="card-footer">
      <a href="" class="card-link">Lire la suite</a>
     </div>
    </div>
   </div>
   <div class="col-md-4 col-lg-4 col-sm-12">
    <div class="card">
     <div class="card-img">
      <img src="images/posts/imag2.jpg" class="img-fluid">
     </div>
     
     <div class="card-body">
     <h4 class="card-title">Titre de l'article</h4>
      <p class="card-text">
       
       proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
     </div>
     <div class="card-footer">
      <a href="" class="card-link">Lire la suite</a>
     </div>
    </div>
   </div>
  </div>
 </div>
</div>
```

Nous devons ajouter un peu de style CSS aux cartes :

```css
.blog{
 margin: 4em 0;
 position: relative; 
}
.blog h1{
 color:#F97300;
 margin: 2em; 
}
.blog .card{
 box-shadow: 0 0 20px #ccc;
}
.blog .card img{
 width: 100%;
 height: 12em;
}
.blog .card-title{
 color:#F97300;
  
}
.blog .card-body{
 padding: 1em;
}
```

Après avoir ajouté la section Blog à notre site web, la conception devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHMPSea2jWdZ2dc_b658eA.png)

Cool, n'est-ce pas ? ?

### **Section Équipe**

![Image](https://cdn-media-1.freecodecamp.org/images/1*1PaKtdHChKl534aExUfjCQ.png)

Dans cette section, nous allons utiliser le système de grille pour distribuer l'espace de manière égale entre les images. Chaque image prend 3 colonnes (`**.col-md-3**`) du conteneur — cela équivaut à 25 % de l'espace total.

Notre structure HTML :

```html
<!-- Section Équipe -->
<div class="team">
 <div class="container">
    <h1 class="text-center">Notre Équipe</h1>
  <div class="row">
   <div class="col-lg-3 col-md-3 col-sm-12 item">
    <img src="images/team-2.jpg" class="img-fluid" alt="équipe">
    <div class="des">
      Sara
     </div>
    <span class="text-muted">Manager</span>
   </div>
   <div class="col-lg-3 col-md-3 col-sm-12 item">
    <img src="images/team-3.jpg" class="img-fluid" alt="équipe">
    <div class="des">
       Chris
     </div>
    <span class="text-muted">Ingénieur logiciel</span>
   </div>
   <div class="col-lg-3 col-md-3 col-sm-12 item">
    <img src="images/team-2.jpg" class="img-fluid" alt="équipe">
    <div class="des">
      Layla 
     </div>
    <span class="text-muted">Développeur Front End</span>
   </div>
   <div class="col-lg-3 col-md-3 col-sm-12 item">
    <img src="images/team-3.jpg" class="img-fluid" alt="équipe">
     <div class="des">
      J.Jirard
     </div>
    <span class="text-muted">Manager d'équipe</span>
   </div>
  </div>
 </div>
</div>
```

Et ajoutons un peu de style :

```css
.team{
 margin: 4em 0;
 position: relative;  
}
.team h1{
 color:#F97300;
 margin: 2em; 
}
.team .item{
 position: relative;
}
.team .des{
 background: #F97300;
 color: #fff;
 text-align: center;
 border-bottom-left-radius: 93%;
 transition:.3s ease-in-out;
 
}
```

Ajouter un calque à l'image au survol en utilisant l'animation serait bien ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SxGguj9S8JMncs-D3uNcsA.gif)

Pour créer cet effet, ajoutez les styles ci-dessous au fichier `**main.css**` :

```css
.team .item:hover .des{
 height: 100%;
 background:#f973007d;
 position: absolute;
 width: 89%;
 padding: 5em;
 top: 0;
 border-bottom-left-radius: 0;
}
```

Super cool ! ?

### Formulaire de contact

![Image](https://cdn-media-1.freecodecamp.org/images/1*vaI3jh3TFwSKBn6BcsBedw.png)

Le formulaire de contact est la dernière section à ajouter, puis nous avons terminé ?.

La section du formulaire de contact contiendra un formulaire grâce auquel les visiteurs pourront envoyer un e-mail ou donner leur avis. Nous allons utiliser certaines classes Bootstrap pour rendre le design beau et réactif.

Comme Bootstrap 3, Bootstrap 4 utilise également la classe `.form-control` pour les champs de saisie, mais il y a quelques nouvelles fonctionnalités ajoutées — comme le passage de `.input-group-addon` (obsolète) à `**.input-group-prepend**` (pour utiliser des icônes comme étiquettes).

Voir [la documentation Bootstrap 4](https://getbootstrap.com/docs/4.0/migration/#input-groups) pour plus d'informations. Dans notre formulaire de contact, nous allons envelopper chaque saisie entre une `div` qui a la classe `.form-group`.

Le fichier `**index.html**` ressemble maintenant à ceci :

```html
<!-- Formulaire de contact -->
<div class="contact-form">
 <div class="container">
  <form>
   <div class="row">
    <div class="col-lg-4 col-md-4 col-sm-12">
      <h1>Contactez-nous</h1> 
    </div>
    <div class="col-lg-8 col-md-8 col-sm-12 right">
       <div class="form-group">
         <input type="text" class="form-control form-control-lg" placeholder="Votre Nom" name="">
       </div>
       <div class="form-group">
         <input type="email" class="form-control form-control-lg" placeholder="VotreEmail@email.com" name="email">
       </div>
       <div class="form-group">
         <textarea class="form-control form-control-lg">
          
         </textarea>
       </div>
       <input type="submit" class="btn btn-secondary btn-block" value="Envoyer" name="">
    </div>
   </div>
  </form>
 </div>
</div>
```

Styles de la section de contact :

**main.css**

```css
.contact-form{
 margin: 6em 0;
 position: relative;  
}

.contact-form h1{
 padding:2em 1px;
 color: #F97300; 
}
.contact-form .right{
 max-width: 600px;
}
.contact-form .right .btn-secondary{
 background:  #F97300;
 color: #fff;
 border:0;
}
.contact-form .right .form-control::placeholder{
 color: #888;
 font-size: 16px;
}
```

#### Polices

Je pense que les polices par défaut sont laides, donc nous allons utiliser l'API Google Fonts, et nous choisirons **Raleway** qui est une belle police et appropriée à notre modèle.

Ajoutez ce lien dans votre fichier `**main.css**` :

```css
@import url('https://fonts.googleapis.com/css?family=Raleway');
```

et définissez le style global pour les balises HTML et les titres :

```css
html,h1,h2,h3,h4,h5,h6,a{
 font-family: "Raleway";
}
```

#### **Effet de défilement**

![Image](https://cdn-media-1.freecodecamp.org/images/1*a9OoxPsn-hrbjYpbNV6DzA.gif)

La dernière chose manquante est l'effet de défilement. Ici, nous devrons utiliser un peu de JQuery. Ne vous inquiétez pas si vous n'êtes pas familier avec cela, ajoutez simplement ce code dans votre fichier `**main.js**` :

```js
$(".navbar a").click(function(){
  $("body,html").animate({
   scrollTop:$("#" + $(this).data('value')).offset().top
  },1000)
  
 })
```

et ajoutez un attribut `data-value` à chaque lien de la barre de navigation :

```html
<li class="nav-item">
         <a class="nav-link" data-value="about" href="#">À propos</a>
       </li>
       <li class="nav-item">
         <a class="nav-link " data-value="portfolio" href="#">Portfolio</a>
       </li>
       <li class="nav-item">
         <a class="nav-link " data-value="blog" href="#">Blog</a>
       </li>
       <li class="nav-item">
         <a class="nav-link " data-value="team" href="#">
         Équipe</a>
       </li>
       <li class="nav-item">
         <a class="nav-link " data-value="contact" href="#">Contact</a>
       </li>
```

Définissez un attribut `id` pour chaque section.

**Note** : L'`id` doit être identique à l'attribut `data-value` dans le lien de la barre de navigation pour que le défilement fonctionne :

```html
<div class="about" id="about"></div>
```

### Conclusion

Bootstrap 4 est une excellente option pour construire votre application web. Il offre une haute qualité d'éléments d'interface utilisateur et il est facile à personnaliser, à intégrer et à utiliser. Il vous aidera également à inclure la réactivité dans votre site web, offrant ainsi une expérience utilisateur premium à vos utilisateurs.

Vous trouverez les fichiers du projet sur [GitHub](https://github.com/hayanisaid/bootstrap4-website).

> Si vous avez besoin de thèmes et de modèles Bootstrap, vous pouvez consulter [BootstrapBay](https://bootstrapbay.sjv.io/DV1q2), ils ont des produits géniaux

Consultez mon cours Bootstrap pour apprendre Bootstrap 4 :

[**Cours intensif Bootstrap 4 : de base à avancé | Said Hayani | Skillshare**](https://skl.sh/2LaD1ym)  
[_Dans ce cours, vous allez apprendre la version 4 de Bootstrap, le framework CSS pour construire des modèles flexibles et…_skl.sh](https://skl.sh/2LaD1ym)