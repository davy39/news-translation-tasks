---
title: Apprendre CSS Flexbox en construisant 5 mises en page réactives
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-03-29T23:11:34.000Z'
originalURL: https://freecodecamp.org/news/learn-flexbox-build-5-layouts
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/FCC--4-.png
tags:
- name: CSS
  slug: css
- name: css flex
  slug: css-flex
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
seo_title: Apprendre CSS Flexbox en construisant 5 mises en page réactives
seo_desc: 'Here''s a practical guide to help you learn CSS Flexbox in 2021 by building
  5 responsive layouts. Let''s dive right in.🥇

  Table of Contents


  Flexbox Architecture

  Setup

  Level-1

  Level-2

  Level-3

  Level-4

  Level-5

  Conclusion


  You can check out the Figma desi...'
---

Voici un guide pratique pour vous aider à apprendre CSS Flexbox en 2021 en construisant 5 mises en page réactives. Plongeons directement dans le sujet.🧠

## Table des matières
   * [Architecture Flexbox](#heading-architecture-flexbox)
   * [Installation](#heading-installation)
   * [Niveau-1](#heading-mise-en-page-niveau-de-difficulte-1-comment-construire-une-mise-en-page-de-carte)
   * [Niveau-2](#heading-mise-en-page-niveau-de-difficulte-2-comment-construire-une-mise-en-page-de-barres-de-navigation)
   * [Niveau-3](#heading-mise-en-page-niveau-de-difficulte-3-comment-construire-une-mise-en-page-de-barres-laterales)
   * [Niveau-4](#heading-mise-en-page-niveau-de-difficulte-4-comment-construire-une-mise-en-page-de-carte-2)
   * [Niveau-5](#heading-mise-en-page-niveau-de-difficulte-5-le-saint-graal-des-mises-en-page)
   * [Conclusion](#heading-conclusion)

### Vous pouvez [**consulter la conception Figma ici**](https://www.figma.com/file/d1bG4msAzxixv9jWP8e4nA/Master-CSS-Flexbox-Layout?node-id=0%3A1)

### Vous pouvez également regarder ce tutoriel sur ma chaîne YouTube ici :

%[https://youtu.be/m8BSEUUB5so]

## Qu'est-ce que Flexbox ?

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Desktop---1--6--1.png)

Nous avons besoin d'un plan lorsque nous construisons une maison. De la même manière, nous avons besoin d'un plan pour **disposer** notre **contenu dans notre navigateur.** En même temps, nous devons créer des **mises en page réactives** pour **différentes tailles d'écran.**

C'est ce que **Flexbox** nous aide à faire – créer des mises en page réactives.

# Architecture Flexbox

Alors, comment fonctionne l'architecture Flexbox ? Les **éléments flexibles** [Contenus] sont distribués le long de l'**Axe Principal** et de l'**Axe Transversal.** Et, selon la propriété **flex-direction**, la position de la mise en page change entre les lignes et les colonnes.

![Architecture Flex Box](https://dev-to-uploads.s3.amazonaws.com/i/hy2oqjvsbk60ef92nktg.png)

# Tableau Flexbox

Ce tableau contient **toutes les propriétés et valeurs possibles** que vous pouvez utiliser avec flexbox. Vous pouvez vous y référer pendant le projet et expérimenter avec différentes valeurs.

![Tableau Flex Box](https://dev-to-uploads.s3.amazonaws.com/i/gv3jyh4xt4fbwtq1qejn.png)

## Avant de commencer...

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Desktop---2--1-.png)

Vous devez connaître **un peu de HTML** et **CSS**. Tout au long de ce tutoriel, vous apprendrez comment fonctionne Flexbox, comment ses diverses propriétés et valeurs fonctionnent, et comment fonctionnent les requêtes média (qui nous aident à créer des sites web réactifs).

# Installation du projet

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Frame-2--2-.png)

Avant de coder, nous devons enregistrer certaines valeurs dans des variables et effacer les styles par défaut du navigateur. En même temps, nous définirons quelques mixins de requêtes média pour gagner du temps et éviter la répétition de code.

## SCSS

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Frame-3--3-.png)

**SCSS** est un préprocesseur de CSS qui nous offre beaucoup plus de fonctionnalités que le CSS standard.

Par exemple, nous pouvons imbriquer des classes enfants dans leur classe parente, stocker des valeurs dans des variables, et bien plus encore. Cela nous aide vraiment à gagner du temps.

Commençons à jouer avec SCSS. Ouvrez [CodePen](https://codepen.io/) ou un éditeur de code et suivez ces étapes avec moi, étape par étape.👋

### Comment activer SCSS dans Codepen 👋

![SCSS](https://media.giphy.com/media/AkEzX8BD8Ef23fyGXP/giphy.gif)

Tout d'abord, définissez la couleur de la bordure, l'écart et les valeurs de remplissage dans vos variables.

```scss
$gap : 4vh;
$padding : 4vh;
$color : #48CAE4;
```

Ensuite, définissez divers points de rupture d'écran dans la carte SCSS. **Rappelez-vous**, sur notre carte SCSS, [mobile, tablette et bureau] sont des **clés** et les pixels sont des **valeurs**.

```scss
$bp : (
  mobile : 480px,
  tablet : 768px,
  desktop : 1440px,
);
```

Pour gagner du temps et du code, lors de la définition des requêtes média, nous utiliserons des **mixins et une boucle** sur les points de rupture que nous avons définis ci-dessus. 👋

```scss
@mixin query($display){
  @each $key, $value in $bp{
    
    //  définition de la largeur maximale
    @if ($display == $key){
      @media (max-width: $value){@content;}
    }
  }
}
```

Maintenant, nous devons **changer les styles par défaut de notre navigateur**. Nous supprimons la marge et le remplissage et définissons le box-sizing sur border-box.

```scss
//Changement des paramètres par défaut..

*{
  margin:0px;
  padding: 0px;
  box-sizing: border-box;
  
// Changement du corps ici

  body{
    width: 100%;
    min-height: 100vh;
    font-family: sans-serif;
    font-size: 45px;
  }
}

```

Parlons de la relation entre les classes HTML que nous allons utiliser. N'oubliez jamais que Flexbox fonctionne sur les classes enfants.

Par exemple, les propriétés Flexbox définies sur la **classe Container** fonctionnent sur **Block**, et les propriétés définies sur la **classe Block** fonctionnent sur la **classe Box**. Voici une explication illustrée de ce que je veux dire : 👋

![FLOW](https://dev-to-uploads.s3.amazonaws.com/i/ivmqdkg948wclyfs1n0t.png)

Maintenant, créons ces mises en page. Nous commencerons par un niveau de difficulté plus facile et passerons à des mises en page plus avancées.

# Niveau de difficulté de la mise en page-1 – Comment construire une mise en page de carte

![Niveau-1](https://dev-to-uploads.s3.amazonaws.com/i/yjx1adsec062quujq7ke.png)

### HTML

La **classe container** contiendra 3 enfants -> block-1, block-2 et block-3.

La **classe block-1** portera 3 boîtes -> box-1, box-2 et box-3.

Les mêmes règles s'appliquent pour les **classes block-2 et block-3**, mais les valeurs seront modifiées.

```html
<div class="container">

<!--block-1 a 3 enfants, box-1,box-2,box-3 -->

  <div class="block-1">
    <div class="box-1"> A </div>
    <div class="box-2"> B </div>
    <div class="box-3"> C </div>
  </div>

<!--similaire à block-1, les valeurs sont modifiées -->

  <div class="block-2">
    <div class="box-4"> D </div>
    <div class="box-5"> E </div>
    <div class="box-6"> F </div>
  </div>

<!--similaire à block-1, les valeurs sont modifiées -->

  <div class="block-3">
    <div class="box-7"> G </div>
    <div class="box-8"> H </div>
    <div class="box-9"> I </div>
  </div>
</div>

```

### SCSS

Maintenant, nous allons styliser notre classe container. N'oubliez pas, pour activer Flexbox et accéder à tous ses pouvoirs, vous devez écrire **`display: flex;`** comme ceci :

```scss
// Règles de style pour la classe container

.container{
  display: flex;

//pour disposer les classes .block-* en colonne
  flex-direction: column;

//Définir l'écart entre les classes .block-*
  gap: $gap;
  
// pour définir un peu de remplissage et de bordure à l'intérieur
  padding: $padding;
  border: 1vh solid $color;
}
```

Sélectionnez toutes les classes **`.block-*`** et stylisez-les ensemble. En même temps, en bas, nous définirons notre requête média en utilisant le **mixin** que nous avons créé pendant la phase d'installation.

```scss
[class ^="block-"]{

//Pour disposer les boîtes en ligne.
  display: flex;
  flex-direction: row;

//Supprimer la bordure (1vh+1vh), l'écart et le remplissage de la hauteur
// Puis répartir équitablement les espaces entre les
// classes .block-* en le divisant par 3

  height: (100vh-2vh -$gap*2-$padding*2) / 3;

// mettre un écart entre les classes .box-*
  gap: $gap;
  
// Règles de style pour l'affichage mobile

  @include query (mobile){
    flex-direction: column;
    
// vous pouvez choisir n'importe quelle valeur que vous souhaitez.
    height: 500px;
  }
  
}
```

Très bien, ensuite sélectionnez toutes les classes **`.box-*`** et stylisez-les ensemble comme ceci :

```scss
[class ^="box-"]{
  
// Pour centrer le texte dans chaque boîte
  display: flex;
  justify-content: center;
  align-items: center;
  
// Pour diviser les espaces entre les boîtes
// essayez flex-gap:1; vous pouvez voir la différence.
// flex-grow: 1; // 1+1+1 =3 => 1/3 X 100% => 33.33% chacun

  flex-basis: (100%)/3; // 33.33% chacun
  border : 2px solid black;
  border-radius: 10px;
  background-color: #c1c1c1;
}

```

# Niveau de difficulté de la mise en page-2 – Comment construire une mise en page de barre de navigation

![Niveau-2](https://dev-to-uploads.s3.amazonaws.com/i/dhkcw4npzbmp34lcm4yf.png)

### HTML

Supprimez le code HTML du niveau-1 et écrivez ce code à la place. En gros, c'est **1 classe parente avec 4 classes enfants.**

```html
<div class="container">
  <div class="item-1"> Accueil </div>
  <div class="item-2"> À propos </div>
  <div class="item-3"> Services </div>
  <div class="item-4"> Contact </div>
</div>


```

### SCSS

Voici les règles de style pour la **classe container** pour le niveau-2. En bas, nous mettrons en place une requête média en utilisant le mixin.

```scss
.container{
  font-size: 35px;
  display: flex;

//Pour définir l'orientation des éléments
  flex-direction: row;

// Pour distribuer l'espace disponible
  justify-content: space-evenly;
  padding: $padding;
  border : 1vh solid $color;

// les règles de style commencent à partir des écrans tablettes
  @include query(tablet){
    height : 100vh;
//Changer l'orientation des éléments
    flex-direction: column;
    align-items: center;

//Définir l'écart pour les éléments verticalement
    gap: $gap 
  }
}

```

# Niveau de difficulté de la mise en page-3 – Comment construire une mise en page de barre latérale

![Niveau-3](https://dev-to-uploads.s3.amazonaws.com/i/evaqt7tcdldtu7g3f9io.png)

### HTML

Maintenant, nous travaillerons avec ce bloc de code :

```html
<div class="container">
  <div class="block-1"> Gauche </div>
  <div class="block-2"> Droite </div>
</div>

```

### SCSS

Les règles de style de la **classe container** avec le mixin de requête média sont incluses en bas pour le niveau-3 :

```scss
.container{
  display: flex;
  flex-direction: row;
  gap: $gap;
  padding: $padding;

// Règles de style pour l'affichage mobile

  @include query(mobile){
    flex-direction: column;
  }
}
```

Ici, nous sélectionnons et stylisons toutes les classes **`.block-*`** avec la requête média pour l'affichage mobile :

```scss
[class ^="block-"]{

//Pour centrer le texte gauche, droite
  display: flex;
  justify-content: center;
  align-items: center;

  border : 4px solid $color;
//Définir la hauteur de chaque bloc
  height: 100vh -$padding*2;

// Règles de style pour l'affichage mobile
  @include query(mobile){
    height: 50vh -$padding*2;
  }
}
```

Maintenant, nous ciblons individuellement les classes block-1 et block-2. Nous changeons également la valeur flex-grow afin de distribuer l'espace à l'écran.

```scss
// Règles de style pour le bloc de gauche

.block-1{
//occupera 20% de la largeur disponible
  flex-grow: 2;
}

// Règles de style pour le bloc de droite

.block-2{
//occupera 80% de la largeur disponible
  flex-grow: 8;
}

```

### Faites une pause :D

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Break--1-.png)

# Niveau de difficulté de la mise en page-4 – Comment construire une mise en page de carte #2

![Niveau-4](https://dev-to-uploads.s3.amazonaws.com/i/6bwmcadjacdyh5fobk1d.png)

### HTML

Les règles HTML ici sont similaires au niveau-1 avec quelques changements :

```html
<div class="container">
    
  <div class="block-1">
    <div class="box-1"> A </div>
  </div>
    
    
  <div class="block-2">
    <div class="box-2"> B </div>
    <div class="box-3"> E </div>
  </div>
    
    
  <div class="block-3">
    <div class="box-4"> C </div>
    <div class="box-5"> D </div>
  </div>
    
</div>
</div>

```

### SCSS

Stylisez la classe container comme ceci :

```scss
.container {
  display: flex;
  flex-direction: column;
  padding: $padding;
  gap: $gap;
}
```

Ensuite, sélectionnez et stylisez toutes les classes **`block-*`** ensemble avec le mixin de requête média en bas pour les appareils mobiles :

```scss
[class ^="block-"]{
  display: flex;
  flex-direction: row;
  gap: $gap;
  
// Supprimer le remplissage, l'écart et diviser par 3
  height: (100vh -$gap*2 -$padding*2)/3;
  
// Règles de style pour la version mobile
  @include query(mobile){
    flex-direction: column;
  }
}
```

Maintenant, sélectionnez et stylisez toutes les classes **`box-*`** ensemble :

```scss
[class ^="box-"]{

// Pour placer la lettre au centre
  display: flex;
  justify-content: center;
  align-items: center;
  
// Bordure, rayon de bordure et couleur de fond
  border : 1vh solid $color;
  border-radius: 10px;
  background-color: #c1c1c1;
}
```

Maintenant, nous allons cibler individuellement les boîtes et **utiliser flex-basis pour distribuer l'espace à l'écran.**

```scss
//A
.box-1{
  flex-basis: 100%;
}

//B & D
.box-2, .box-5{
  flex-basis: 70%;
}
//E & C
.box-3,.box-4{
  flex-basis: 30%
}
```

Enfin, nous inclurons le mixin de requête média pour la version mobile.

```scss
// Règles de style pour la version mobile

@include query(mobile){
  .block-2{
    height: (100vh*2)/3; // 66.66vh
  }
  .block-3{
    flex-direction: row;
  }
  
// Sélection de B, E, C, D
  .box-2,.box-3,.box-4,.box-5{
    flex-basis: 50%;
  }
}

```

### Gagnez-vous déjà ? Augmentons la difficulté. 🔥

# Niveau de difficulté de la mise en page-5 – Le Saint Graal des mises en page

![Niveau-5](https://dev-to-uploads.s3.amazonaws.com/i/8lb4gh8povgvcb40iz0h.png)

### HTML

Les règles HTML ici sont similaires à celles du **niveau-1** et du **niveau-4** avec quelques changements :

```html
<div class="container">
    
  <div class="block-1">
    <div class="box-1"> A </div>
  </div>
    
  <div class="block-2">
    <div class="box-2"> B </div>
    <div class="box-3"> C </div>
    <div class="box-4"> D </div>
  </div>
    
  <div class="block-3">
    <div class="box-5"> E </div>
  </div>
</div>

```

### SCSS

Tout d'abord, changez les **styles de la classe container** comme ceci :

```scss
.container{
  display: flex;
  flex-direction: column;
  gap: $gap;
  padding: $padding;
}
```

Ensuite, ciblez et stylisez toutes les classes **`block-*`** ensemble.

```scss
// Règles de style de toutes les classes .block-*

[class ^="block-"]{
  display: flex;
  flex-direction: row;
  gap: $gap;
}
```

Ensuite, ciblez et stylisez toutes les classes **`box-*`** ensemble.

```scss
// Règles de style de toutes les classes .box-*

[class ^="box-"]{
  display: flex;
  justify-content: center;
  align-items: center;
  border : 1vh solid $color;
  border-radius: 10px;
}
```

Ensuite, ciblez individuellement les boîtes et **utilisez flex-basis pour distribuer l'espace à l'écran.**

```scss
// Définition de A & E ensemble
.box-1,.box-5{
  flex-basis: 100%;
  height: 20vh;
}

// Définition de C ici
.box-3{
  flex-basis: 60%;
// Suppression de l'écart et du remplissage
  height: 60vh -$gap*2-$padding*2;
}

// Définition de B & D ensemble
.box-2,.box-4{
  flex-basis: 20%;
}
```

Enfin, incluez le mixin de requête média pour la version mobile. Remarquez que nous **masquons box-2** pour la version mobile.

```scss
// Requête média pour l'écran mobile

@include query(mobile){
  .block-2{
    flex-direction: column;
    height: 60vh;
  }
// Masquer notre bloc B
  .box-2{
    display: none;
  }
// Augmenter la hauteur de C
  .box-3{
    flex-basis: 80%;
  }
}
```

## Conclusion

Merci d'avoir suivi ! Espérons que vous comprenez maintenant les bases de Flexbox. Voici votre médaille pour avoir lu jusqu'à la fin. ❤️

Les suggestions et critiques sont grandement appréciées ❤️ N'hésitez pas à me contacter via les liens de réseaux sociaux ci-dessous si vous avez des questions.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

## Crédits des images

[Avatar de chaton](https://www.flaticon.com/packs/kitty-avatars-3)
[Chaton avec canard](https://www.freepik.com/free-vector/cute-cats-set-funny-character-cartoon-illustration_12566246.htm#page=3&position=2)
[Lapin mignon](https://www.freepik.com/free-vector/set-cute-rabbit-with-duck-cartoon-illustration_12573651.htm#page=3&position=41)
[Ours mignon](https://www.freepik.com/free-vector/cute-bear-character-cartoon-illustration_12341164.htm#page=1&position=40#&position=40)

[Plus de conceptions de mise en page ici](https://csslayout.io/patterns/)

**YouTube [/ Joy Shaheb](https://www.youtube.com/c/joyshaheb)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**