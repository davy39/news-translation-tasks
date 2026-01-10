---
title: Projet HTML et CSS – Comment Construire un Clone de YouTube Étape par Étape
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-26T21:32:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-website-with-html-and-css-step-by-step
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/photo-1460925895917-afdab827c52f.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: Projet HTML et CSS – Comment Construire un Clone de YouTube Étape par Étape
seo_desc: 'By Ogundiran Ayobami

  In this tutorial we will build a YouTube clone step by step. You''ll learn how to
  create layouts and add content to those layouts.

  If you have been struggling to build a real website with HTML & CSS, this is the
  article for you. B...'
---

Par Ogundiran Ayobami

Dans ce tutoriel, nous allons construire un clone de YouTube étape par étape. Vous apprendrez comment créer des mises en page et ajouter du contenu à ces mises en page.

Si vous avez du mal à construire un site web réel avec HTML & CSS, cet article est fait pour vous. Parce que je vais vous apprendre à le faire étape par étape pour réduire vos difficultés.

Nous discuterons de la façon de créer la mise en page du clone de YouTube avec HTML et CSS et vous apprendrez comment faire une mise en page à deux colonnes.

Attendez ! Si vous êtes un débutant total et que vous ne comprenez même pas la différence entre HTML et CSS, vous pouvez regarder la vidéo ci-dessous pour apprendre tout ce dont vous avez besoin pour commencer...

[![Cours accéléré HTML](https://img.youtube.com/vi/dXC4EEkO1vI/0.jpg)](https://www.youtube.com/watch?v=dXC4EEkO1vI)

Il est important de diviser les choses en plus petites parties pour rendre nos projets plus faciles à construire. Donc, nous devons diviser ce clone de YouTube en plus petites unités que nous construirons étape par étape.

## Décomposition du Clone de YouTube

Dans le clone de YouTube que nous allons construire, le site web a environ 6 unités :

![youtube-clone-repeation-1](https://www.freecodecamp.org/news/content/images/2022/01/youtube-clone-repeation-1.PNG)

L'**En-tête** contient trois sections (gauche, centre et droite). La section gauche contient le logo et le menu, le centre contient la boîte de recherche et une icône, et la droite contient des icônes de navigation. Les icônes sont basées sur des éléments similaires, ce qui signifie que nous concevons un élément d'icône puis nous le copions, le collons et l'éditons pour créer les autres.

Le **Corps principal** contient deux sections (barre latérale et contenu). Les liens de navigation dans la barre latérale sont également similaires, donc ils ne sont qu'une seule chose. La même chose se produit pour les vidéos dans la section de contenu.

Donc, notre clone de YouTube a un en-tête, un corps principal, une barre latérale, un contenu, une carte vidéo, un lien de navigation et une icône de navigation comme principales unités. C'est la décomposition des unités de la page web que nous voulons créer.

## Mise en Page du Clone de YouTube

La première chose que nous devons faire est de créer la structure de mise en page du clone de YouTube avec HTML. Nous allons faire cela avec le code ci-dessous :

```js
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Material Icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <!-- Fichier CSS -->
    <link rel="stylesheet" href="styles/index.css" />
    <title>Clone de YouTube avec HTML & CSS</title>
  </head>
  <body>
      <header class="header">.</header>
      <main>
          <div class="side-bar">.</div>
          <div class="content">.</div>
      </main>
  <!-- Fin du Corps Principal -->
</body>
</html>
```

Dans ce tutoriel, je suppose que vous comprenez comment utiliser les balises meta HTML et comment lier un fichier CSS. Si ce n'est pas le cas, vous pouvez en apprendre davantage à leur sujet dans la vidéo que j'ai ajoutée ci-dessus. Mais vous n'avez pas besoin de les comprendre pour ce que nous apprenons dans cette leçon, alors continuez à lire.

Nous avons une balise header pour créer la section d'en-tête du clone de YouTube. Nous ajouterons le logo YouTube, la boîte de recherche et d'autres icônes de navigation à l'en-tête plus tard.

Il y a aussi la section principale qui contient la barre latérale et le contenu. La barre latérale contiendra quelques liens de navigation tandis que le contenu contiendra des vidéos. Donc, c'est tout pour la structure avec juste HTML.

Attendez ! Notre code ne semble pas trop beau après exécution. Eh bien, nous allons corriger cela avec CSS. Alors ajoutons du CSS pour vraiment créer une mise en page YouTube.

### CSS pour le Clone de YouTube

#### Étape 1 : Utiliser @import en CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
```

Commençons par « import url('path')... Que fait-il ? Nous l'utilisons pour lier la police Google appelée Roboto afin de pouvoir l'utiliser comme police de notre site web.

#### Étape 2 : Réinitialiser les styles par défaut de HTML

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

L'astérisque * est un sélecteur CSS qui sélectionne toutes les balises HTML de notre page. Nous définissons leur margin et padding à 0. Nous définissons ensuite leur box-sizing à border-box. Pourquoi faisons-nous cela ?

Nous voulons que la largeur ou la hauteur, la bordure, la margin et le padding s'additionnent pour être la longueur totale. Voici ce que je veux dire : en CSS, si une boîte a une largeur de 100px et un padding de 10px, la largeur de la boîte sera maintenant de 110px

Mais nous ne voulons pas cela – nous voulons que tout soit à 100px. La largeur devrait toujours être de 100px y compris la margin de 10px au lieu de la faire passer à 110px. C'est ce que fait `box-sizing: border-box`.

Note : lorsque vous l'utilisez, vous commencerez à mieux comprendre comment cela fonctionne – mais pour l'instant, je voulais juste donner un aperçu auquel un débutant peut rapidement s'identifier.

#### Étape 3 : Définir la font-family

```css
body {
  font-family: 'Roboto', sans-serif;
}
```

Nous sélectionnons la balise body et définissons sa font-family à Roboto et utilisons sans-serif comme solution de repli au cas où Roboto n'est pas disponible.

#### Étape 4 : Styliser l'en-tête

```css
/* section header*/
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 15px;
  }
```

Le nom de classe `.header` est utilisé pour sélectionner (ou se connecter à) la section d'en-tête de notre site web afin que nous puissions ajouter quelques styles. 

Nous définissons sa propriété display à flex pour créer une mise en page, et ensuite nous pouvons facilement la diviser en sections. Nous la diviserons en sections plus tard.

`Justify-content: space-between` signifie que nous voulons que les contenus dans l'en-tête aient de l'espace entre eux une fois qu'il y en a plus d'un.

`Align-items: centre` est utilisé pour déplacer tous les contenus de l'en-tête vers le centre-gauche de votre écran. Cela s'appelle l'alignement vertical. Nous définissons enfin la `height` de l'`header` à 60px et son padding à 15px.

#### Étape 5 : Définir la hauteur de la section principale

```css
main {
    height: calc(100vh - 70px);
    display: flex;
    background-color: #f9f9f9;
  }
```

Nous définissons la `height` de la section principale à `calc( 100vh - 70px)`... Que signifie-t-il ? V signifie `viewport`, qui est la partie visible de l'écran d'une fenêtre sans défilement. « height » signifie longueur verticale, et nous pouvons également utiliser « w » qui signifie width - longueur horizontale. 

En bref, 100vh signifie la hauteur totale qui est visible dans un navigateur sans défilement. Et nous utilisons calc ( 100vh - 70px) pour exécuter un calcul qui soustrait 70px de 100vh.

Nous définissons sa propriété display à flex pour créer une mise en page. Enfin, nous définissons sa couleur de fond à `#f9f99f` qui est une sorte d'argent ou de cendré.

#### Étape 6 : Masquer la barre de défilement

```css
/* Sidebar */ 
.side-bar {
    height: 100%;
    width: 17%;
    background-color: white;
    overflow-y: hidden;
  } 
```

La `height` de la .side-bar est définie à 100% de son parent. Cela signifie qu'elle aura la même hauteur que son parent. Sa largeur est définie à 17% de son parent et la couleur de fond est définie à blanc. 

Hey ! Qu'est-ce que `overflow-y: hidden` ? Lorsque Twitter charge 10 tweets à la fois, vous ne pouvez pas tout voir en même temps et vous devez faire défiler, n'est-ce pas ? Dans ce cas, nous masquons la barre de défilement. Gracias !

#### Étape 7 : Ajouter des requêtes média pour la réactivité

```css
@media (max-width: 768px) {
    .side-bar {
      display: none;
    }
  }
```

Nous utilisons cette requête média pour rendre un site web réactif sur mobile, tablettes et desktop. Lorsque le clone de YouTube est sur un appareil dont l'écran est inférieur ou égal à 768px (comme mobile & tablette), la barre latérale disparaîtra. De plus, max-width: 768px signifie qu'un écran d'appareil peut être inférieur ou égal à 768px.

D'accord, nous avons construit la mise en page de notre clone de YouTube. Voici le résultat...

![87SgHIdIE](https://www.freecodecamp.org/news/content/images/2022/01/87SgHIdIE.jpg)

## Comment Ajouter du Contenu à la Section d'En-tête

Dans cette partie, nous allons discuter de la façon de diviser un élément en sections et d'ajouter du contenu à la section d'en-tête. 

En bref, nous divisons la section d'en-tête du clone de YouTube en trois sections : gauche, centre et droite. Et chacune des sections contient quelques balises. Commençons !

### Étape 1 : Ajouter des enfants et des petits-enfants à l'en-tête

Ici, nous allons simplement ajouter des balises HTML à la section d'en-tête du clone de YouTube. Nous allons faire cela avec le code ci-dessous :

```html
<header>
 <div class="logo left">
   <i id="menu" class="material-icons">menu</i>
   <img src="https://www.freecodecamp.org/news/content/images/2022/01/yt-logo.png">
 </div>
 
 <div class="search center">
   <form action="">
     <input type="text" placeholder="Rechercher" />
     <button><i class="material-icons">search</i></button>
   </form>
   <i class="material-icons mic">mic</i>
 </div>
 
 <div class="icons right">
   <i class="material-icons">videocam</i>
   <i class="material-icons">apps</i>
   <i class="material-icons">notifications</i>
   <i class="material-icons display-this">account_circle</i>
 </div>
</header>
```

Après avoir divisé l'en-tête en trois sections en ajoutant trois blocs de code séparés, il est temps d'utiliser CSS pour le rendre plus beau. Commençons.

### Étape 2 : Styliser la section gauche 

```css
.left {
  display: flex;
  align-items: center;
}
 
.left #menu {
  padding: 0 7px;
  cursor: pointer;
}
```

N'oubliez pas, nous avons défini la propriété `justify-content` de l'en-tête à space-between, ce qui signifie qu'il y aura un espace égal entre chaque balise dans l'en-tête.

Maintenant, nous avons donné une classe `left` parce qu'elle devrait être du côté gauche. Nous définissons sa propriété display à flex pour créer des sections avec la mise en page. Ses enfants sont alignés au centre-gauche de l'en-tête. Nous accédons également au menu qui est à l'intérieur de la section gauche avec son `id`. 

Nous définissons son `padding top et bottom` à 0 et son `padding left et right` à 7px. Sa propriété `cursor` est définie à pointer afin que lorsque la souris est dessus, elle affichera un doigt pointé.

### Étape 3 : Styliser la section centrale et son formulaire

```css
.search {
  display: flex;
}
 
.search form {
  display: flex;
  border: 1px solid #ddd;
  height: 45px;
}
```

Hey ! Vous devriez savoir ce que nous faisons dans la classe search maintenant. :)

Nous définissons sa propriété display à flex afin que nous puissions créer une mise en page avec ses enfants. Nous faisons de même pour le formulaire qui est à l'intérieur de la section search/center.

Son épaisseur de bordure est définie à 1px, type à solid, et couleur à #ddd (quelque chose d'argenté ou de cendré).

### Étape 4 : Styliser l'entrée dans le formulaire de recherche

```css
.search input {
  width: 600px;
  padding:10px;
  border: 0;
  height: 100%;
  border-radius: 2px 0 0 2px
}

input:focus {
  outline: none;
  border: 1px solid #ddd;
}
```

Nous sélectionnons l'`input` qui est à l'intérieur de la section search avec `.search input`. Nous définissons son border-radius à 2px top, 0 right, 0 bottom, et 2px left. Alors, qu'est-ce que border-radius ? Ce sont les bords courbés d'un objet avec quatre angles.

### Étape 5 : Styliser les icônes/boutons de recherche et de micro

```css
.search button {
  height: 100%;
  width: 60px;
  border: none;
}
 
.mic {
  margin-top: 10px;
}
```

Le bouton à l'intérieur de la section search est également sélectionné avec `.search button`. Sa hauteur est définie à 100% de son parent. Nous ne voulons pas qu'il ait de bordure, donc nous définissons sa bordure à 0.

Nous accédons à l'icône du microphone avec son nom de classe `.mic` et définissons sa margin-top à 10px afin qu'elle descende un peu.

Enfin, stylisons toutes les material-icons que nous avons sur la page web :

```css
  .material-icons {
    color: rgb(100, 100, 100);
    padding: 0 7px;
    cursor: pointer;
  }
```

Dépêchez-vous ! Nous avons ajouté des enfants et des sections à l'en-tête du clone de YouTube. Découvrez le résultat final ci-dessous :

![Youtube-clone-with-header-contents](https://www.freecodecamp.org/news/content/images/2022/01/Youtube-clone-with-header-contents.PNG)

## Comment Ajouter du Contenu à la Barre Latérale

Dans cette partie, nous allons discuter de la façon d'ajouter des liens de navigation au clone de YouTube. En bref, nous allons ajouter un ensemble de liens à la barre latérale existante.

### Étape 1 : Ajouter des enfants et des petits-enfants à la barre latérale

Nous allons ajouter le code HTML suivant à la barre latérale :

```html
<!-- <div class="side-bar"> -->

   <div class="nav">
      <a class="nav-link active">
        <i class="material-icons">home</i>
        <span>Accueil</span>
      </a>
  </div>

<!-- </div> -->
```

Ensuite, nous devons d'abord styliser la navbar, qui est l'enveloppe pour tous les liens :

```css
.nav {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    margin-top: 15px;
  }
```

La seule chose que j'expliquerai ici est flex-direction. Cela détermine si nous voulons que les enfants apparaissent dans une colonne (verticale) ou une ligne (horizontale). Dans ce cas, nous optons pour un affichage horizontal.

Ensuite, stylisons le nav-link ci-dessus avec CSS comme montré ci-dessous :

```css
.nav-link {
    display: flex;
    align-items: center;
    padding: 12px 25px;
  }
  
 .nav-link span {
    margin-left: 15px;
  }
  
 .nav-link:hover {
    background: #e5e5e5;
    cursor: pointer;
  }
 
.active {
    background: #e5e5e5;
 }
```

Oups – il n'y a rien à expliquer ici car j'ai déjà expliqué de nombreux concepts similaires !

D'accord, parlons de `.home:hover`. Les styles qu'il contient ne seront appliqués que lorsque nous déplacerons notre curseur sur le lien de navigation d'accueil. C'est tout.

Hey... attendez. Nous avons de nombreux liens dans la barre latérale, alors comment allons-nous les créer ? Eh bien, nous faisons simplement ce que tout développeur aime - copier et coller puis l'éditer comme ci-dessous :

```html
<div class="side-bar">
<div class="nav">
   <a class="nav-link active">
      <i class="material-icons">home</i>
      <span>Accueil</span>
   </a>
   <a class="nav-link">
      <i class="material-icons">local_fire_department</i>
      <span>Tendances</span>
   </a>
   <a class="nav-link">
      <i class="material-icons">subscriptions</i>
      <span>Abonnements</span>
   </a>
 </div>
 <hr>
</div>
```

Après avoir collé trois liens, nous voulons les regrouper en catégories distinctes en utilisant la balise <hr> pour créer une ligne qui les sépare de la catégorie suivante. Maintenant, stylisons la balise hr.

```css
hr {
    height: 1px;
    background-color: #e5e5e5;
    border: none;
  }
```

Ensuite, nous ajouterons le code restant après la balise hr comme ci-dessous :

```html
<!-- <div class="nav">
     hr -->
    <a class="nav-link">
       <i class="material-icons">library_add_check</i>
       <span>Bibliothèque</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">history</i>
       <span>Historique</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">play_arrow</i>
       <span>Vos Vidéos</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">watch_later</i>
       <span>À Regarder Plus Tard</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">thumb_up</i>
       <span>Vidéos Aimées</span>
    </a>
<!-- </div> -->
```

Wow, nous avons terminé avec la barre latérale du clone de YouTube et voici le résultat que nous obtenons :

![youtube-clone-with-nav-content](https://www.freecodecamp.org/news/content/images/2022/01/youtube-clone-with-nav-content.PNG)

## Comment Ajouter des Vidéos à la Section de Contenu

Dans cette partie du tutoriel sur le clone de YouTube, nous allons ajouter des vidéos à la zone de contenu. Vous devez dupliquer la vidéo (et non les vidéos) à plusieurs endroits pour qu'elle ressemble à YouTube et vous pouvez les éditer avec des informations uniques de vidéo YouTube si elles sont disponibles.

```html
<div class="videos">
  <!-- une vidéo commence -->
    <div class="video">
       <div class="thumbnail">
          <img src="https://img.youtube.com/vi/zUwB_imVjmg/maxresdefault.jpg" alt="" />
        </div>

          <div class="details">
             <div class="author">
                <img src="https://yt3.ggpht.com/bpzY-S4DYlbTeOpY5hIA7qz_hcbMkgvLAugtwKBGTTImNnWAGudX0y53bo_fJZ0auypxrWkUiw=s88-c-k-c0x00ffffff-no-rj" alt="" />
             </div>
             <div class="title">
                <h3>
                    Introvertis & Création de Contenu | Sumudu Siriwardana
                 </h3>
                 <a href="">
                        Francesco Ciulla
                  </a>
                  <span> 2M Vues • Il y a 3 Mois </span>
             </div>
           </div>

         </div>
   <!-- une vidéo se termine -->
 </div>
```

Maintenant, appliquons du CSS.

```css
.content {
  background-color: #f9f9f9;
  width: 100%;
  height: 100%;
  padding: 15px 15px;
  border-top: 1px solid #ddd;
  overflow-y: scroll;
}

.videos {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
}

.video {
  width: 270px;
  margin-bottom: 30px;
}
```

Si vous vérifiez le style pour `.videos`, vous verrez `flex-wrap`. C'est la seule propriété que je n'ai pas expliquée auparavant, alors expliquons-la.

Lorsque l'écran ne peut prendre que quatre éléments, par exemple, les autres éléments seront déplacés vers une autre ligne. C'est ce que fait « flex-wrap ».

```css
.thumbnail {
  width: 100%;
  height: 170px;
}

.thumbnail img {
  object-fit: cover;
  height: 94%;
  width: 100%;
}
.author img {
  object-fit: cover;
  border-radius: 50%;
  height: 40px;
  width: 40px;
  margin-right: 10px;
}
```

La seule chose que vous ne comprenez peut-être pas ci-dessus parce que nous ne l'avons pas expliquée auparavant est `object-fit: cover`. Alors, comment l'utilisons-nous ?

`object-fit` dans ce cas est utilisé pour rogner l'image à son conteneur afin de supprimer le débordement (zones où l'image est plus grande que son conteneur) en hauteur et en largeur :

```css
.details {
  display: flex;
}
 
.title {
  display: flex;
  flex-direction: column;
}
 
.title h3 {
  color: rgb(3, 3, 3);
  line-height: 18px;
  font-size: 14px;
  margin-bottom: 6px;
}
 
.title a,
span {
  text-decoration: none;
  color: rgb(96, 96, 96);
  font-size: 12px;
}
```

Dans ce cas, nous faisons une mise en page à partir de `.details` et parce que nous ne définissons pas sa flex-direction à property, elle sera définie à row – qui est sa valeur par défaut. Vous voyez qu'une mise en page est également faite à partir du titre et que ses enfants apparaissent dans une colonne en définissant flex-direction à column.

Nous sélectionnons la balise h3 qui est à l'intérieur de `.title` et nous définissons sa couleur à quelque chose de noir... Je vais expliquer comment comprendre le code de couleur plus tard.

`line-height` est utilisé pour définir la hauteur d'une ligne de texte et dans ce cas, nous la définissons à 18px.

Enfin, nous utilisons `.title a, span` pour sélectionner la balise d'ancrage dans `.title`. Nous sélectionnons également toutes les balises span de la page et définissons leur text-decoration à none.

Alors, qu'est-ce que la décoration de texte ? Elle a un design tel qu'un soulignement qu'une balise d'ancrage a, et nous le masquons dans ce cas en le définissant à none. Nous avons ajouté des vidéos au clone de YouTube et le résultat final est ci-dessous :

![youtube-clone-completed](https://www.freecodecamp.org/news/content/images/2022/01/youtube-clone-repeation.PNG)

## Comment Rendre le Clone de YouTube Réactif

Dans cette partie du tutoriel, nous allons rendre le clone de YouTube que nous avons construit un peu réactif. Comment faisons-nous cela ? Eh bien, nous allons utiliser les requêtes média CSS. Maintenant, commençons !

Donc, nous allons ajouter le code CSS ci-dessous au fichier CSS du clone de YouTube.

```css
@media (max-width: 768px) {
    .side-bar {
      display: none;
    }
    .search {
      display: none;
    }
}
```

```@media (max-width: 768px) { }``` est utilisé pour définir les tailles d'écran des appareils auxquelles le code dans la requête média s'appliquera.

Dans cet exemple, `max-width: 768px` signifie que les styles dans la requête média seront appliqués à toute taille d'écran qui est égale ou inférieure à 768px.

Donc, chaque fois que la taille de l'écran utilisée est de 768px ou moins, nous masquerons la barre latérale et l'entrée de recherche en définissant leur propriété display à none.

```css
@media (max-width: 900px) {
    .search input {
      width: 25rem;
    }
  }
```

Enfin, nous rendons l'entrée de recherche un peu plus petite chaque fois que la taille de l'écran de l'appareil utilisé est inférieure ou égale à 900px.

C'est tout.

Hourraaaay... nous avons terminé la création du clone de YouTube. Maintenant, allez et construisez le vôtre et n'oubliez pas de jouer avec. 

Ajoutez ou retirez certaines choses du tutoriel pour être sûr de vraiment comprendre ce que vous faites. Bonne chance ! 

## Une dernière chose

[Ayobami Ogundiran](https://www.twitter.com/codingnninja) aime écrire l'histoire avec le développement de logiciels et aide actuellement ceux qui ont du mal à comprendre et à construire des projets avec HTML, CSS et JavaScript à travers You Too Can Code. 

Rejoignez-moi via [Groupe Telegram](https://t.me/+HEUn1Y-ME6GW9ssD) ou [Groupe Discord](https://discord.com/invite/WGtNSHUnDZ).