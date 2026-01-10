---
title: Apprenez les Media Queries CSS en créant trois projets
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-04-26T15:21:29.000Z'
originalURL: https://freecodecamp.org/news/learn-css-media-queries-by-building-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/FCC-Thumbnail.png
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: responsive images
  slug: responsive-images
seo_title: Apprenez les Media Queries CSS en créant trois projets
seo_desc: 'Today we''re going to learn how to use CSS Media Queries to build responsive
  websites. And we''ll practice what we learn by completing three projects. Let''s
  go 🏅

  Table of Contents


  What are CSS Media Queries?

  Steps to follow

  The Syntax

  Practice Projec...'
---

Aujourd'hui, nous allons apprendre à utiliser les Media Queries CSS pour créer des sites web réactifs. Et nous mettrons en pratique ce que nous apprenons en réalisant trois projets. C'est parti 🏆

# Table des matières 

* [Qu'est-ce que les Media Queries CSS ?](#heading-questce-que-les-media-queries-css)
* [Étapes à suivre](#heading-comment-configurer-le-projet)
* [La Syntaxe](#heading-la-syntaxe-des-media-queries-css)
* [Projets pratiques](#heading-creons-quelques-projets-en-utilisant-les-media-queries-css)
* [Conclusion](#heading-conclusion)

Sujets à aborder en un coup d'œil :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7vrrjohwnmdvbtexg1r2.png)

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/HY8q4TD3KGM]

# Qu'est-ce que les Media Queries CSS ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kyjadc0b95rjuzjlcgck.png)

Les Media Queries CSS vous permettent de créer des sites web réactifs sur toutes les tailles d'écran, allant de l'ordinateur de bureau au mobile. Vous comprenez donc pourquoi il est important d'apprendre ce sujet.

Voici une démo de la magie des Media Queries 👇

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bb0qwxrhg0705lvs6ihs.png)

Nous construirons cela dans le projet 2 ci-dessous. Cette mise en page est appelée le **Card Layout**. Vous pouvez voir plus d'exemples de mises en page [ici !](https://csslayout.io/patterns/)

# Comment configurer le projet

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9wa8xgu2o74y2d60cq3g.png)

Pour ce projet, vous devez connaître un peu de HTML, de CSS et savoir comment travailler avec VS Code. Suivez-moi ->

1. Créez un dossier nommé "Project-1"
2. Ouvrez VS Code
3. Créez les fichiers **index.html, style.scss,** et **main.js**
4. Installez Live Server et le SASS Compiler
5. Lancez Live Server et le SASS Compiler

## HTML

En HTML, écrivez ce code à l'intérieur de la balise body 👇

```html
 <div class = "container"></div>

```

Nous avons également besoin de voir la taille exacte de notre fenêtre. Voici une démo de ce que je veux dire :

![Demo](https://media.giphy.com/media/06zg3tXmCsfA6hX5zo/giphy.gif)

Alors, écrivez cette ligne dans le fichier html :

```html
  <div id="size"></div>

```

## Qu'est-ce que le SCSS ?

Nous utiliserons SCSS, pas CSS. Mais..... qu'est-ce que le SCSS ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q5a3hp7070ls26dovja2.png)

SCSS est un préprocesseur de CSS qui est plus puissant que le CSS classique. En utilisant SCSS, nous pouvons ->

1. Imbriquer nos sélecteurs comme les branches d'un arbre et mieux gérer notre code.
2. Stocker diverses valeurs dans des variables
3. Utiliser des Mixins pour arrêter la répétition du code et gagner du temps

Et bien plus encore !

Dans notre SCSS, nous allons supprimer nos paramètres par défaut du navigateur, et nous allons changer le box-sizing, la font-size et la font-family comme ceci : 👇

```scss
*{
  margin : 0px;
  padding : 0px;
  box-sizing : border-box; 

  body{
    font-size : 35px;
    font-family : sans-serif;
  }
}

```

**N'oubliez pas** de définir la **hauteur** (height) de la classe **.container**. Sinon, nous ne parviendrons pas à obtenir les résultats souhaités :

```scss
.container{
  height : 100vh;
}

```

Vous vous souvenez de l'id supplémentaire que nous avons écrit en HTML ? Nous allons le styliser et le positionner dans notre navigateur ici :

```scss
#size {
  position: absolute;

// positionnement de la taille de l'écran sous notre texte principal
  top : 60%;
  left: 50%;

  transform: translateX(-50%);

  color : red;
  font-size : 35px;
}

```

## JavaScript

Nous devons mettre à jour la taille de notre écran à l'intérieur de notre id chaque fois que nous redimensionnons notre fenêtre. Alors, écrivez ce code dans votre fichier `main.js` :

```javascript

// 'screen' est le nom 👇 d'une fonction
window.onresize = screen;
window.onload = screen;

// Fonction nommée 'screen' 👇

function screen() {
  Width = window.innerWidth;
  document.getElementById("size").innerHTML 
   = "Width : " + Width + " px" 
}

```

## Télécharger les images pour le projet

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u72rvfe5181640ikqa32.png)

Un site web réactif signifie également des **Images réactives**. Nous allons donc également rendre nos images réactives dans ce projet. Les images sont sur mon **[dépôt GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Media-Query-Project)**. Voici comment les obtenir :

1. Visitez et copiez le lien ci-dessus ☝️
2. Allez sur **[downgit](https://minhaskamal.github.io/DownGit/#/home)** et collez le lien que vous avez copié
3. Suivez les étapes de cette vidéo 👇

![Down Git Steps to follow](https://cloud.githubusercontent.com/assets/5456665/17822364/940bded8-6678-11e6-9603-b84d75bccec1.gif)

Et.... nous sommes prêts ! Commençons à coder. 😊

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u5qj78v41btdq7sewdzs.png)

# La syntaxe des Media Queries CSS

Voici la syntaxe d'une Media Query :

```scss
@media screen and (max-width: 768px){
  .container{
   // Votre code ici
  }
}

```

Et voici une explication illustrée ->

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e1wvg9w8co1hq3d24uxi.png)

Divisons la syntaxe en quatre sections :

1. Déclaration de la Media Query
2. Le type de média (Media Type)
3. Fonctions min-width & max-width
4. Le code lui-même

### Pour comprendre les 4 sections de la syntaxe, commençons notre **Premier projet** :

![Project-1 Video](https://media.giphy.com/media/t4QOOfmnupAqnHcI9H/giphy.gif)

Nous allons construire ceci. ☝️ C'est un petit projet où la couleur d'arrière-plan change lors du redimensionnement de la fenêtre en procédant par petites étapes. Commençons !

### Le HTML

Placez le code suivant à l'intérieur de votre HTML, comme ceci :

```html
<div class = "container">

   <div class = "text">
      Hello Screen !
   </div>

</div>

```

### Le SCSS

Maintenant, nous allons stocker quatre codes de couleur dans des variables comme ceci : 👇

```scss
$color-1 : #cdb4db ; // Mobile
$color-2 : #fff1e6 ; // Tablette
$color-3 : #52b788 ; // Ordinateur portable
$color-4 : #bee1e6 ; // Bureau

```

Vous pouvez trouver plus de couleurs sur [coolors.co](https://coolors.co/palettes/trending) si vous souhaitez choisir les vôtres.

Maintenant, en bas, ciblez les classes `.container` et `.text`. Nous allons également centrer notre texte comme ceci 👇

```scss
.container{
// Pour placer le texte au centre

  display : grid;
  place-items : center;

  background-color : $color-1;
  height : 100vh;
}

.text{
 // laisser vide pour le moment
}

```

Jusqu'ici, tout va bien !

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/grc7r9mbpw7yvoisgj6c.png)

## 1. Comment déclarer les media queries 

Les Media Queries commencent par la déclaration `@media`. Le but principal de l'écriture de ceci est de **dire au navigateur** que nous avons spécifié une media query. Dans votre CSS, écrivez-le comme ceci : 👇

```scss
@media 

```

## 2. Comment définir le type de média

Ceci est utilisé pour spécifier la nature de l'appareil avec lequel nous travaillons. Les quatre valeurs sont :

* all
* print
* screen
* speech

Voici le but de chacune des valeurs en un coup d'œil 👇

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ea8yqchxnmdlqyq9es0m.png)

Nous déclarons le **type de média** après la déclaration `@media`, comme ceci :

```scss
@media screen

```

## Pourquoi écrivons-nous l'opérateur "and" ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t8qezvhk9m896ns97jta.png)

Disons que nous passons une commande dans un restaurant, "Un burger **et** une pizza". Notez que les deux commandes sont séparées par **[et]**.

De même, le type de média, les fonctions min-width et max-width sont essentiellement des conditions que nous donnons au navigateur. Nous n'écrivons pas l'opérateur **"and"** si nous n'avons qu'une seule condition. Comme ceci ->

```scss
@media screen {
  .container{
     // Votre code ici 
  }
}

```

Nous écrivons l'opérateur **and** si nous avons deux conditions, comme ceci :

```scss
@media screen and (max-width : 768px) {
  .container{
     // Votre code ici 
  }
}

```

Vous pouvez également ignorer le type de média et travailler uniquement avec min-width & max-width, comme ceci :

```scss
// Ciblage des tailles d'écran entre 480px & 768px 

@media (min-width : 480px) and (max-width : 768px) {
  .container{
     // Votre code ici 
  }
}

```

Si vous avez trois conditions ou plus, vous pouvez utiliser une **virgule**, comme ceci :

```scss
// Ciblage des tailles d'écran entre 480px & 768px 

@media screen, (min-width : 480px) and (max-width : 768px) {
  .container{
     // Votre code ici 
  }
}

```

## 3. Comment utiliser les fonctions min-width & max-width

Discutons du composant le plus important d'une media query, les points de rupture (breakpoints) de l'écran.

Pour être honnête, il n'existe pas de guide standard pour les points de rupture d'écran car il y a tellement de tailles d'écran sur le marché. Mais, pour notre projet, nous suivrons les valeurs de points de rupture d'écran de [The Official Bootstrap 5](https://getbootstrap.com/docs/5.0/layout/breakpoints/). Les voici :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7pqqlkxksxgouje83vhw.png)

Voici une liste de toutes les résolutions d'écran d'appareils sur [CSS-Tricks](https://css-tricks.com/snippets/css/media-queries-for-standard-devices/).

### La fonction max-width :

En utilisant cette fonction, nous créons une limite. Cela fonctionnera tant que nous sommes **à l'intérieur de la limite**. Voici un exemple 👇

Notre limite est de 500px :

![max-width](https://media.giphy.com/media/50L0raPo5ZSdxCOlmP/giphy.gif)

Remarquez comment la couleur violet clair est **désactivée** lorsque nous dépassons 500px.

Pour recréer cela, écrivez ce code en SCSS :

```scss
.container{
  background-color: white ;
  height: 100vh;
  display: grid;
  place-items: center;
}

```

En bas, insérez la media query comme ceci 👇

```scss
@media screen and (max-width : 500px){
  .container{
    background-color: $color-1;
  }
}

```

### La fonction min-width :

Nous créons également une limite ici. Mais cela fonctionnera si nous allons **en dehors de la limite**. Voici un exemple : 👇

Notre limite est de 500px :

![Min-width](https://media.giphy.com/media/iThpfWPRTBSQXn2gpO/giphy.gif)

Remarquez comment la couleur violet clair est **activée** après avoir dépassé la largeur de 500px.

Pour recréer cela, écrivez ce code en SCSS :

```scss
.container{
  background-color: white ;
  height: 100vh;
  display: grid;
  place-items: center;
}

```

En bas, insérez la media query comme ceci : 👇

```scss
@media screen and (min-width : 500px){
  .container{
    background-color: $color-1;
  }
}

```

Pour résumer, rappelez-vous que :

* **max-width** définit les styles à l'intérieur de la limite fixée

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/227jg6drq6faqc47e2ox.png)

* **min-width** définit les styles à l'extérieur de la limite fixée

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e8ds85udh6l20hdh6lbm.png)

## Le code lui-même

Assemblons notre premier projet !

Nous aurons quatre points de rupture d'écran :

* Mobile  -> 576px
* Tablette  -> 768px
* Ordinateur portable  -> 992px
* Bureau -> 1200px

Oui, nous suivons les points de rupture d'écran officiels de [bootstrap 5](https://getbootstrap.com/docs/5.0/layout/breakpoints/). Et chaque point de rupture recevra ces couleurs :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d42pdgggmovcrsq8p61n.png)

Pour quatre types d'appareils, nous aurons quatre Media Queries. Avant de toucher aux media queries, stockons d'abord les valeurs des points de rupture dans des variables, comme ceci :

**Note :** N'oubliez pas d'ajouter le signe **$** :

```scss
$mobile  : 576px;
$tablet  : 768px;
$laptop  : 992px; 
$desktop : 1200px;

```

Et notre classe `.container` devrait ressembler à ceci :

```scss
.container{
  background-color: white ;
  height: 100vh;
  display: grid;
  place-items: center;
}

```

Nous avons fait 50 % du chemin ! Maintenant, configurons les quatre media queries.

## Mais attendez...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/net2cuugxdaz9idwbwhl.png)

Vous devez suivre le bon ordre lors de l'écriture des media queries. Commencez à écrire de **l'affichage le plus grand vers l'affichage le plus petit.**

### Premier point de rupture pour le bureau – 1200px

Pour l'écran de bureau, écrivez ce code en SCSS : 👇

```scss
// utilisation de la variable ici qui est 👇 1200px
@media screen and (max-width: $desktop){
  .container{
    background-color: $color-4;
  }
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w1cuuy0m4zw57sh9zdzf.png)

### Deuxième point de rupture pour l'ordinateur portable – 992px

Pour les écrans d'ordinateurs portables, écrivez ce code en SCSS : 👇

```scss
// utilisation de la variable ici qui est 👇 992px
@media screen and (max-width: $laptop){
  .container{
    background-color: $color-3;
  }
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fng9y622xtb9pa6ngfwj.png)

### Troisième point de rupture pour la tablette – 768px

Pour les écrans de tablettes, écrivez ce code en SCSS : 👇

```scss
// utilisation de la variable ici qui est 👇 768px
@media screen and (max-width: $tablet){
  .container{
    background-color: $color-2;
  }
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7wqp9xjt4gg272pc3hkt.png)

### Quatrième point de rupture pour le mobile – 576px

Pour les écrans mobiles, écrivez ce code en SCSS : 👇

```scss
// utilisation de la variable ici qui est 👇 576px
@media screen and (max-width : $mobile){
  .container{
    background-color: $color-1;
  }
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z10764qm7cjjc8a2yb7j.png)

## Faites une pause

Félicitations pour avoir terminé le projet 1 ! Maintenant, **faites une pause. Vous le méritez.**

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p6j0uyekswj04ag3p2cl.png)

# Créons quelques projets en utilisant les Media Queries CSS

## Comment construire un portfolio réactif

Nous allons construire un petit site web réactif pour notre deuxième projet.

### Voici à quoi ressemblera la vue bureau :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ay01oqdseulalsw3gpdh.png)

### Et voici la vue mobile :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hob05vxov52hrm5quz0a.png)

D'accord alors, commençons à coder ! Tout d'abord, travaillons sur la vue bureau en faisant de petits pas.

### Avant de commencer

Créez un dossier nommé 'images' à l'intérieur de notre dossier Project-1. Placez toutes les images que vous avez téléchargées depuis mon **[dépôt GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Media-Query-Project)** à l'intérieur du dossier images.

## Le HTML

### Étape 1 – Créer les sections

Nous allons créer trois sections pour notre site web. Écrivez ce code dans votre HTML :

```html
<div class="container"> 

    <div class="header"></div>

    <div class="main"></div>

    <div class="footer"></div>

</div>

```

### Étape 2 – Logo et éléments de menu

Nous placerons le logo et les éléments de menu à l'intérieur du div .header, comme ceci :

```html
<div class="header">

      <div class="header__logo">Miya Ruma</div>

      <div class="header__menu">
          <div class="header__menu-1"> Home </div>
          <div class="header__menu-2"> Portfolio </div>
          <div class="header__menu-3"> Contacts </div>
      </div>

  </div>

```

### Étape 3 – Image et texte

Nous placerons l'image et le texte à l'intérieur du div .main, comme ceci :

```html
<div class="main">

     <div class="main__image"></div>

     <div class="main__text">

       <div class="main__text-1">Hello 👋</div>

       <div class="main__text-2">I'm <span>Miya Ruma</span></div>

       <div class="main__text-3">A Designer From</div>

       <div class="main__text-4">Tokyo, Japan</div>

     </div>

</div>

```

### Étape 4 – Icônes de réseaux sociaux

Nous placerons les icônes de réseaux sociaux à l'intérieur du div .footer, comme ceci :

```html
<div class="footer">

   <div class="footer__instagram">
      <img src="./images/instagram.png" alt="">
   </div>

   <div class="footer__twitter">
      <img src="./images/twitter-sign.png" alt="">
   </div>

    <div class="footer__dribbble">
       <img src="./images/dribbble-logo.png" alt="">
    </div>

    <div class="footer__behance">
       <img src="./images/behance.png" alt="">
    </div>

</div>

```

## Le SCSS

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8ou3jrlk5g9mjodfh88n.png)

### Étape 1 – Mettre à jour le SCSS

Supprimez tout ce qui se trouve dans notre SCSS et écrivez ce code à la place :

```scss
* {
  // placement de la marge à gauche et à droite
  margin: 0px 5px;

  padding: 0px;
  box-sizing: border-box;

  body {
    font-family: sans-serif;
  }
}

```

Voici ce que nous avons jusqu'à présent :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3egdxy9f5wf8xgc2ekn8.png)

### Étape 2 – Sélectionner toutes les classes en HTML

Sélectionnez toutes les classes que nous avons créées en HTML sur notre feuille de style.

```scss
.container{}

.header{}

.main{}

.footer{}

```

### Étape 3 – Sélectionner tous les enfants

Maintenant, sélectionnez tous les enfants des classes parentes.

```scss
.header{
  
  &__logo{}

  &__menu{}
}

.main{

  &__image{}

  &__text{}
}

.footer{

  [class ^="footer__"]{}

}

```

**Notez** que `&__logo` imbriqué dans `.header` est un raccourci pour `.header__logo`.

### Étape 4 – Définir le .container

Définissez le `.container` pour la mise en page de bureau, comme ceci :

```scss
.container{

// Définition de la hauteur
  height: 100vh;

  display: flex;

  flex-direction: column;
}

```

Appliquez `display: flex;` au `.header` et aux éléments de menu afin qu'il se comporte comme une ligne, et non comme une colonne :

```scss
.header{
  display: flex;
  flex-direction: row;

  &__logo{}

  &__menu{
    display: flex;
    flex-direction: row;
  }
}

```

Divisez chaque section et créez des bordures pour voir ce que nous faisons :

```scss
.header{
  display: flex;

// La bordure et la hauteur
  border: 2px solid red;
  height: 10%;

// Les autres sélecteurs sont ici

}

.main{

// La bordure et la hauteur
  border: 2px solid black;
  height: 80%;

// Les autres sélecteurs sont ici

}

.footer{

// Bordure et hauteur
  border: 2px solid green;
  height: 10%;

// Les autres sélecteurs sont ici
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o77rk1bj2m722jf41mju.png)

### Étape 5 – Terminer le style du .header

Terminons le style de notre section `.header` en utilisant les propriétés de flex-box et la taille de police appropriée :

```scss
.header {
// hauteur
  height: 10%;

  display: flex;
// Alignement du logo et du menu au centre
  align-items: center;

// espace entre le logo et le menu
  justify-content: space-between;

  &__logo {
    font-size: 4vw;
  }

  &__menu {
    display: flex;
    font-size: 2.5vw;

// pour mettre un espace entre les éléments du menu
    gap: 15px;
  }
}

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kx4d43xmeggdaw2h2pdf.png)

### Étape 6 – Ajouter l'image

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7tyojtcpe7o1o9mukum6.png)

Ajoutons l'image à l'intérieur de la section `.main` et créons une séparation pour l'image et le texte.

```scss
.main {
  // l'image et le texte agiront comme une ligne
  display: flex;
  flex-direction: row;

  // La bordure et la hauteur
  border: 2px solid black;
  height: 80%;

  &__image {
    // Ajout de l'image
    background-image: url("./images/Portrait.png");
    // couvrira la moitié de la largeur de l'écran
    width: 50%;
  }

  &__text {
    // couvrira la moitié de la largeur de l'écran
    width: 50%;
  }
}

```

Le résultat est un peu moche pour le moment, mais ne perdez pas espoir~

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2q13at8wcniamqpwh7jv.png)

### Étape 7 – Rendre l'image réactive

Stylez l'image pour qu'elle soit réactive comme ceci :

```scss
.main{
  &__image{
  // rendre l'image fluide
    background-size: contain;

  // arrêter la répétition de l'image
    background-repeat: no-repeat;

  // positionner l'image
    background-position: left center;
  }
}

```

Et voici ce que nous avons jusqu'à présent :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/24r955u9wwww9vdwwhk5.png)

L'image est réactive de la résolution **4k** jusqu'à l'écran de votre **montre connectée**. Vous ne me croyez pas ? Ouvrez les outils de développement de Chrome et testez par vous-même.

Vous pouvez en apprendre davantage sur les [propriétés d'arrière-plan ici](https://www.freecodecamp.org/news/learn-css-background-properties/) si vous souhaitez créer des images réactives pour des sites web réactifs.

![4k test](https://media.giphy.com/media/7Us5yEqyNW6IkOR1fs/giphy.gif)

### Étape 8 – Styler le texte

Stylisons notre texte maintenant. Tout d'abord, nous allons l'amener exactement au centre avec ce code :

```scss
.main{

  &__text {
    // couvrira la moitié de la largeur de l'écran
    width: 50%;
    display: flex;
    flex-direction: column;

// Pour l'amener au centre 
    justify-content: center;
    align-items: center;
  }

// Pour colorer le nom 
  span{
    color: red;
  }

}

```

Maintenant, définissons les tailles de police pour le texte :

```scss
.main{


  &__text{

// Pour ajouter des espaces entre les textes verticalement
    gap: 15px;
    
// taille de police pour "hello"
    &-1{
      font-size: 10vw;
    }

// taille de police pour les autres textes
    &-2,&-3,&-4{
      font-size: 5vw;
      
    }

  }
}


```

Le résultat ressemble à ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kne4bezy1ft0ro6ore0p.png)

À ce stade, vous pouvez supprimer toutes les bordures que nous avons placées à l'intérieur de nos classes header, main et footer.

### Étape 9 – La section footer

Tout d'abord, redimensionnez les images comme ceci :

```scss
.footer{
  [class^="footer__"] {
    img {
      width: 5.3vw;
    }
  }
}

```

Ensuite, positionnez les images à l'endroit souhaité, avec un petit espace entre les icônes, comme ceci :

```scss
.footer{
  display: flex;
  flex-direction: row;

// Pour aligner les icônes le long de l'axe X
  align-items: center;
// placement de l'image sur le côté droit
  justify-content: flex-end;
// Espace entre les icônes
  gap: 20px;

// marge sur le côté droit des icônes 
  margin-right: 10%;
}

```

Et voici le résultat, sans les guides :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/itzk2rwz621vjm1k833c.png)

### Étape 10 – La mise en page mobile

Nous y sommes presque...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9w8h1owma15wmrzqb5cd.png)

Créez une media query à 650px et stylez la classe `.header` comme ceci :

```scss
@media (max-width: 650px) {

  .header {

// Pour placer le logo au centre
    justify-content: center;

    &__logo {
      font-size: 40px;
    }
// masquage du menu sur appareil mobile
    &__menu {
      display: none;
    }
  }
}

```

### Étape 11 – Centrer .main

Maintenant, placez la section .main exactement au centre avec ce code :

```scss
@media (max-width: 650px){
// styles de la section header de l'étape 10...

// section main ici 
  .main {
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

```

### Étape 12 – Styler l'image et le texte pour le mobile

Stylez l'image et le texte pour la mise en page mobile comme ceci :

```scss
@media (max-width: 650px){

 .main {
   &__image {
// Taille de l'image 
      height: 200px;
      width: 200px;
      background-size: 100%;

// Pour avoir une image arrondie 
      border-radius: 100%;
      background-position: center;
    }

// Styles pour le texte ->
    &__text {
      width: 100%;

      &-1 {
        display: none;
      }
      &-2, &-3, &-4 {
        font-size: 30px;
      }
    }
}


```

### Étape 13 – Styler le footer pour le mobile

La dernière étape consiste à styliser la section footer pour la mise en page mobile :

```scss
@media (max-width: 650px){
  .footer {
// placement des icônes le long de l'axe X
    justify-content: center;
    margin: 0px;

    [class^="footer__"] {

// Redimensionnement des images pour la mise en page mobile
      img {
        width: 45px;
        height: 45px;
      }
    }
  }
}

```

Et voici notre résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7dxzqtz8it2xhzpxf4ll.png)

## Faites une pause

Beau travail jusqu'à présent ! Faites une pause avant de passer au projet suivant. 😊

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hdd7i01tivcfgg4nki0m.png)

## Projet 3 – Comment construire une mise en page en cartes (Card Layout)

Dans le projet 3, nous allons construire ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tf2o5njarct4ew24dnqj.png)

Alors, commençons.

## Le SCSS

Sur votre feuille de style, supprimez tout sauf les styles de `#size`. Et puis ajoutez ce code ici :

```scss
* {
  margin: 0px;
  padding: 0px 10px;
  box-sizing: border-box;

  body {
    font-family: sans-serif;
    font-size: 55px;
  }
}

#size{
  position: absolute;
// Positionnement du texte
  top: 60%;
  left: 50%;
  transform: translateX(-50%);
// couleur et taille du texte
  color: red;
  font-size: 40px;
}


```

## Le HTML

Votre HTML devrait ressembler à ceci à l'intérieur des balises body : 👇

```html
<div class="container"> 
   // Nous placerons le code ici
</div>

// Cela affichera la largeur de notre fenêtre en direct 
<div id="size"></div>

```

Maintenant, créez trois classes avec les noms de classe `.row-*` comme ceci 👇 à l'intérieur de `.container` :

```html
<div class="container"> 

   <div class="row-1">
   </div>

   <div class="row-2">
   </div>
  
   <div class="row-3">
   </div>
</div>

```

Chaque ligne aura trois boîtes avec les noms de classe `.box-*` comme ceci. 👇 Et oui, vous insérerez des lettres à l'intérieur des boîtes :

```html
<div class="container"> 

   <div class="row-1">
       <div class="box-1">A</div>
       <div class="box-2">B</div>
       <div class="box-3">C</div>
   </div>

   <div class="row-2">
       <div class="box-4">D</div>
       <div class="box-5">E</div>
       <div class="box-6">F</div>
   </div>
  
   <div class="row-3">
       <div class="box-7">G</div>
       <div class="box-8">H</div>
       <div class="box-9">I</div>
   </div>
</div>

```

Nous en avons terminé avec la partie HTML, et le résultat devrait ressembler à ceci : 👇

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u3jg1iphmhefdpn8gy12.png)

## Le SCSS

Suivez ces petites étapes une par une pour styliser le projet.

### Étape 1 – Ajouter du code SCSS

Pour sélectionner et styler toutes les boîtes et lignes ensemble, voici ce que nous écrivons dans notre CSS : 👇

```scss
.container{
  // styles ici 
}

[class ^="row-"]{
  // Styles appliqués sur toutes les lignes
}

[class ^="box-"]{
  // Styles appliqués sur toutes les boîtes
}

```

### Étape 2 – Faire en sorte que les boîtes se comportent comme des lignes

Les boîtes doivent se comporter comme une ligne. Ce code permettra d'y parvenir :

```scss
[class ^="row-"]{
  display: flex;
  flex-direction: row;
}

```

Et voici le résultat : 👇

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4utfjrr1bfmwwh81rb1a.png)

### Étape 3 – Définir les boîtes

Étendez les boîtes sur toute la largeur et la hauteur et placez les lettres au centre.

```scss
[class ^="box-"]{

  background-color: #c4c4c4;
  border: 2px solid black;

// Définition de la taille des boîtes 
  width : (100%)/3;
  height: (100vh)/3;

// Placer la lettre au centre
  display: grid;
  place-items: center;
}

```

Voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g4m7snz4kklns6xjinzh.png)

### Étape 4 – Créer des espaces entre les lignes

Ensuite, nous allons créer un espace entre les lignes, comme ceci :

```scss
.container{
  display: flex;
  flex-direction: column;
  height: 100vh;

// Création d'un espace entre les lignes 
  gap: 30px;
}

```

Maintenant, créons un espace entre les boîtes :

```scss
[class ^="row-"]{
  display: flex;
  flex-direction: row;

// Création d'un espace entre les boîtes
  gap : 30px;
}

```

Et voici à quoi cela ressemble :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xpus9dx40nxzysz9iceh.png)

### Étape 5 – Configurer la mise en page mobile

Créez la media query qui sera appliquée à 650px :

```scss
@media (max-width: 650px){
  // Nous écrirons le code ici
}

```

Changez l'orientation des boîtes sur l'écran mobile de ligne à colonne, et étirez les boîtes à 100 % de la largeur avec ce code :

```scss
@media (max-width: 650px){

// Changer l'orientation
  [class ^="row-"]{
    flex-direction: column;
  }

// Changer la largeur des boîtes
  [class ^="box-"]{
    width: 100%;
  }
}

```

Et voici le résultat mobile final :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pyis7sloasdv03lljhn9.png)

Au fait, le projet 2 fait partie de [cet article](https://www.freecodecamp.org/news/learn-flexbox-build-5-layouts/) que j'ai écrit. Si vous souhaitez en apprendre davantage et mettre en pratique vos compétences en Flexbox et en media query, n'hésitez pas !

# Conclusion

Voici votre médaille pour avoir lu jusqu'au bout ❤️

### Les suggestions et les critiques sont très appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

## Crédits

* [CSS Tricks](https://css-tricks.com/a-complete-guide-to-css-media-queries/)
* [Portrait](https://www.pexels.com/photo/woman-wearing-brown-bucket-cap-732425/) utilisé pour l'exemple de projet
* [Images de Vecteesy](https://www.vecteezy.com/members/joyshaheb/collections/blog-idea-1)
* [Panda](https://www.freepik.com/free-vector/cute-panda-hug-boba-milk-tea-cartoon-icon-illustration-animal-drink-icon-concept-premium-flat-cartoon-style_12571361.htm#position=0), [Glace](https://www.freepik.com/free-vector/kawaii-fast-food-cute-ice-cream-cookie-illustration_5769154.htm#position=1) & [Chat mignon](https://www.freepik.com/free-vector/cute-cats-set-funny-character-cartoon-illustration_12566246.htm)
* [Pack Licorne](https://www.flaticon.com/packs/unicorn-4) & [Avatar Kitty](https://www.flaticon.com/packs/kitty-avatars-3)
* [instagram](https://www.flaticon.com/free-icon/instagram_1384031), [Twitter](https://www.flaticon.com/free-icon/twitter-sign_25347), [Behance](https://www.flaticon.com/free-icon/behance_254383) et [icônes Dribbble](https://www.flaticon.com/free-icon/dribbble-logo_87400)
* [Bubble tea](https://www.freepik.com/free-vector/collection-kawaii-bubble-tea_10048123.htm#position=6)