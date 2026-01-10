---
title: Projet de Développement Web – Comment Créer une Page de Destination avec HTML,
  CSS et JavaScript
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-17T16:56:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-landing-page-with-html-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/website-g09d6960db_1280.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Projet de Développement Web – Comment Créer une Page de Destination avec
  HTML, CSS et JavaScript
seo_desc: 'Having a good landing page for your website is important. It can help drive
  customers to your site where they''ll find your products and services and hopefully
  take action.

  In this text-based tutorial, I’m going to take you through how to make a landi...'
---

Avoir une bonne page de destination pour votre site web est important. Elle peut aider à attirer des clients vers votre site où ils trouveront vos produits et services et, espérons-le, passeront à l'action.

Dans ce tutoriel basé sur du texte, je vais vous guider à travers la création d'une page de destination pour une chaîne de télévision de boxe avec du HTML, CSS et JavaScript simples.

Le nom de notre chaîne de télévision fictive est JabTV, et le but de la création de la page de destination est de collecter des emails.

À la fin de ce tutoriel, vous serez capable de créer :
- un menu hamburger réactif
- un commutateur de thème sombre et clair
- une galerie d'images en lightbox
- un bouton de retour en haut de page
- et surtout, une page web réactive

Les avantages ne s'arrêtent pas là. Je crois qu'en tant que débutant, vous pourrez également améliorer votre CSS après avoir terminé ce tutoriel.

Pour me suivre, récupérez les fichiers de démarrage depuis ce [dépôt GitHub](https://github.com/Ksound22/JabTV-Landing-Page/tree/starter)
Consultez également la démonstration en direct pour vous familiariser avec ce que nous construisons.

## Table des Matières
- [La Structure du Dossier du Projet](#heading-la-structure-du-dossier-du-projet)
- [La Structure HTML de Base](#heading-la-structure-html-de-base)
- [Comment Créer la Barre de Navigation](#heading-comment-creer-la-barre-de-navigation)
- [Comment Styliser la Barre de Navigation](#heading-comment-styliser-la-barre-de-navigation)
- [Comment Créer la Section Hero](#heading-comment-creer-la-section-hero)
- [Comment Styliser la Section Hero](#heading-comment-styliser-la-section-hero)
- [Comment Créer la Section À Propos](#heading-comment-creer-la-section-a-propos)
- [Comment Créer la Galerie d'Images Lightbox](#heading-comment-creer-la-galerie-dimages-lightbox)
- [Comment Styliser la Galerie d'Images Lightbox](#heading-comment-styliser-la-galerie-dimages-lightbox)
- [Comment Créer la Section des Parties Prenantes](#heading-comment-creer-la-section-des-parties-prenantes)
- [Comment Styliser la Section des Parties Prenantes](#heading-comment-styliser-la-section-des-parties-prenantes)
- [Comment Créer la Section d'Abonnement par Email](#heading-comment-creer-la-section-dabonnement-par-email)
- [Comment Styliser la Section d'Abonnement par Email](#heading-comment-styliser-la-section-dabonnement-par-email)
- [Comment Créer le Pied de Page](#heading-comment-creer-le-pied-de-page)
- [Comment Créer le Bouton de Retour en Haut de Page](#heading-comment-creer-le-bouton-de-retour-en-haut-de-page)
- [Comment Créer le Commutateur de Thème Sombre et Clair](#heading-comment-creer-le-commutateur-de-theme-sombre-et-clair)
- [Comment Styliser le Commutateur de Thème Sombre et Clair](#heading-comment-styliser-le-commutateur-de-theme-sombre-et-clair)
- [Comment Rendre la Page de Destination Réactive](#heading-comment-rendre-la-page-de-destination-reactive)
- [Comment Créer un Menu Hamburger pour la Page de Destination](#heading-comment-creer-un-menu-hamburger-pour-la-page-de-destination)
- [Conclusion](#heading-conclusion)


## La Structure du Dossier du Projet

La structure du dossier suit la convention que de nombreux développeurs front-end utilisent.

Les fichiers HTML et readme ainsi qu'une capture d'écran pour le readme sont à la racine. Les fichiers CSS, les fichiers JavaScript, les icônes et les images vont dans leurs sous-dossiers respectifs à l'intérieur du dossier assets.

![ss-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-1.png)

## La Structure HTML de Base

La structure HTML de base ressemble à ceci :
```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- CSS de la page web -->
    <link rel="stylesheet" href="assets/css/styles.css" />

    <!-- CSS de la lightbox simple -->
    <link rel="stylesheet" href="assets/css/simple-lightbox.min.css" />

    <!-- Favicons -->
    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="assets/icons/apple-touch-icon.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="assets/icons/favicon-32x32.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="16x16"
      href="assets/icons/favicon-16x16.png"
    />

    <title>Page de Destination JabTV</title>
  </head>
  <body>
    <!-- Barre de navigation -->

    <!-- Commutateur de thème sombre/clair -->

    <!-- Barres -->

    <!-- Section hero -->

    <!-- Section à propos -->

    <!-- Galerie d'images lightbox -->

    <!-- Parties prenantes de Jab TV -->

    <!-- Abonnement par email -->

    <!-- Icônes sociales -->

    <!-- Bouton de retour en haut -->

    <!-- Script de la page web -->
    <script src="assets/js/app.js"></script>

    <!-- CDN des icônes Ion -->
    <script
      type="module"
      src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"
    ></script>

    <!-- Lightbox simple -->
    <script src="assets/js/simple-lightbox.min.js"></script>
    <script>
      // Initialisateur de la lightbox simple
    </script>
  </body>
</html>
```

Nous allons coder la page de destination section par section pour que ce ne soit pas trop compliqué à comprendre.

## Comment Créer la Barre de Navigation

La barre de navigation aura un logo à gauche et des éléments de menu de navigation à droite. Plus tard, nous placerons le commutateur de thème sombre et clair entre le logo et les éléments de navigation, mais concentrons-nous d'abord sur le logo et les éléments de menu.

Pour le logo, je n'utiliserai pas une image mais une combinaison de texte et d'emoji placés à l'intérieur d'une balise span afin de pouvoir les styliser différemment.

Le HTML pour le logo ressemble à ceci :

```html
<nav>
      <a href="#" class="logo">
        <h1>
          <span class="jab">Jab</span><span class="tv">TV</span
          ><span class="fist">👊</span>
        </h1>
      </a>
</nav>
```

C'est une combinaison des mots « Jab » et « TV », avec un emoji de coup de poing.

Les éléments du menu de navigation sont des liens génériques placés dans une balise de liste non ordonnée, comme montré dans l'extrait ci-dessous :

```html    
<ul>
        <li class="nav-item">
          <a href="#apropos" class="nav-link" id="nav-link">À propos</a>
        </li>
        <li class="nav-item">
          <a href="#stars" class="nav-link" id="nav-link">Stars de la Boxe</a>
        </li>
        <li class="nav-item">
          <a href="#partiesprenantes" class="nav-link" id="nav-link"
            >Parties prenantes</a
          >
        </li>
        <li class="nav-item">
          <a href="#sub" class="nav-link" id="nav-link">S'abonner</a>
        </li>
</ul>
```

En outre, nous avons besoin de quelques barres pour le menu mobile. Les barres seront cachées sur la version de bureau et visibles sur les téléphones mobiles.

Pour cela, j'utiliserai des barres faites avec du HTML et du CSS brut, pas des icônes. Les barres seront des balises span placées dans une div conteneur avec une classe de `hamburger`.
 
```html 
<div class="hamburger" id="hamburger">
    <span class="bar"></span>
    <span class="bar"></span>
    <span class="bar"></span>
</div>
```
Le menu de navigation ressemble maintenant à ceci dans le navigateur :
![ss-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-2.png)

### Comment Styliser la Barre de Navigation

La barre de navigation est assez laide à ce stade, donc nous devons la styliser. Nous devons styliser le logo pour qu'il ressemble à un logo, et nous utiliserons Flexbox pour placer le logo et les éléments de menu côte à côte.

Pour toute la page web, j'utiliserai la police Roboto. J'ai également déclaré quelques variables CSS et quelques réinitialisations moins compliquées.

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,700&display=swap");

/* Variables CSS */
:root {
  --normal-font: 400;
  --bold-font: 600;
  --bolder-font: 900;
  --primary-color: #0652dd;
  --secondary-color: #ea2027;
  --line-height: 1.7rem;
  --transition: 0.4s ease-in;
}

/* Effet de défilement fluide */
html {
  scroll-behavior: smooth;
}

/* Réinitialisations */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  transition: var(--transition);
}

 body {
  font-family: "Roboto", sans-serif;
}

ul li {
  list-style-type: none;
}

a {
  text-decoration: none;
  color: var(--primary-color);
}

a:hover {
  color: var(--secondary-color);
} 
```

Dans l'extrait de code CSS ci-dessus, je supprime la marge et le remplissage par défaut attribués à tous les éléments par les navigateurs et je définis le box-sizing sur border-box. De cette façon, le remplissage et la marge définis seront plus intentionnels.

J'ai également défini une transition (déclarée dans les variables) afin que vous puissiez voir chaque transition sur le site web.

Tous les liens seront bleus en apparence et rouges au survol – correspondant aux couleurs primaire et secondaire.

Pour styliser le logo, je vais rendre le premier `<span>` rouge, le deuxième `<span>` bleu, et le `.fist` rouge. Les couleurs rouge et bleue ont été définies comme couleur secondaire et couleur primaire respectivement dans les variables CSS.

Les couleurs rouge et bleue sont couramment utilisées dans la boxe amateur et d'autres sports de combat, c'est pourquoi je les ai choisies pour le site web.

```css
.fist {
  color: var(--secondary-color);
}

.jab {
  color: var(--primary-color);
}

.tv {
  color: var(--secondary-color);
}
```

Jusqu'à présent, la barre de navigation ressemble à ceci :
![ss-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-3.png)

Pour placer le logo et les éléments de menu côte à côte, je vais utiliser Flexbox. Je vais également cacher les barres car nous n'en avons besoin que sur les appareils mobiles.

```css
nav {
  background: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  box-shadow: 2px 3px 2px #f1f1f1;
}
```

J'ai appliqué une ombre de boîte pour m'assurer que l'utilisateur sait où la barre de navigation se termine.

Je vais également rendre la barre de navigation collante, afin qu'elle reste toujours en haut lorsque l'utilisateur fait défiler vers le bas. Cela aide à créer une bonne expérience utilisateur.

Je vais le faire avec 4 lignes de CSS :
```css
 position: sticky;
  top: 0;
  left: 0;
  z-index: 1;
```

Pour cacher les barres, je vais cibler la classe `.hamburger` et lui donner un affichage de none :

```css
.hamburger {
  display: none;
}
```

La barre de navigation a l'air beaucoup mieux :
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-1.png)

Mais le logo devrait être plus grand. Nous devons également nous assurer que les éléments de menu sont côte à côte et non les uns sur les autres, donc Flexbox sera à nouveau instrumental ici.

```css
.logo {
  font-size: 2rem;
  font-weight: 500;
}

ul {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-item {
  margin-left: 2rem;
}

.nav-link {
  font-weight: var(--bold-font);
}
```

Jetez un coup d'œil à la barre de navigation maintenant :
![ss-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-5.png)

Cela ne peut pas être mieux !

Et notez que le logo n'est pas une image. Cela signifie que vous pouvez toujours le mettre à jour avec CSS.

## Comment Créer la Section Hero

La section hero va contenir une courte description de JabTV, des boutons d'appel à l'action (CTA), et un vieux téléviseur fait avec de l'art CSS. Nous allons faire le téléviseur avec la balise `iframe` afin qu'une vidéo puisse être affichée à l'intérieur.

La vidéo que nous placerons dans l'`iframe` est celle du grand boxeur Mohammed Ali.

En bref, voici ce que nous construisons :
![ss-6](https://www.freecodecamp.org/news/content/images/2022/01/ss-6.png)

Le HTML pour la section hero est dans l'extrait de code ci-dessous :

```html
    <section class="hero">
      <div class="intro-text">
        <h1>
          <span class="hear"> Vous pouvez Entendre les Jabs </span> <br />
          <span class="connecting"> Connectant</span>
        </h1>
        <p>
          Une plateforme de streaming en ligne pour les matchs de boxe <br />
          Nous consacrons également un temps spécial aux retours en arrière car l'ancien est l'or
        </p>
        <a class="btn red" href="#">En savoir plus</a>
        <a class="btn blue" href="#">S'abonner</a>
      </div>
      <div class="i-frame">
        <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/sUmM_PFpsvQ"
          title="Lecteur vidéo YouTube"
          frameborder="10"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        ></iframe>
        <div class="stand-1"></div>
        <div class="stand-2"></div>
      </div>
    </section>
 ```

Avec le HTML ci-dessus, voici ce que nous avons dans le navigateur :
![ss-7-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-1.png)

### Comment Styliser la Section Hero

Pour aligner le texte et le téléviseur côte à côte, nous avons besoin de Flexbox.
```css
display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.9rem;
  max-width: 1100px;
  margin: 2rem auto -6rem;
}
```
En plus d'aligner les choses avec Flexbox, j'ai également donné à la section une largeur maximale de `1100px` afin que l'utilisateur n'ait pas à regarder jusqu'à l'extrémité extrême pour voir le contenu de la section – c'est bon pour l'expérience utilisateur.

J'ai appliqué une marge de `2rem` en haut, auto à gauche et à droite, et `-6rem` en bas pour centrer tout dans la section.

Jusqu'à présent, nous avons ceci dans le navigateur :
![ss-8](https://www.freecodecamp.org/news/content/images/2022/01/ss-8.png)

Pour styliser les textes `h1` de la section hero, je les ai placés dans leurs balises `span` respectives, afin de pouvoir les styliser différemment.

Par conséquent, je vais cibler les textes avec les attributs de classe des balises span :

```css
.intro-text h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.intro-text h3 {
  margin-bottom: 0.5rem;
}

.hero p {
  line-height: var(--line-height);
}

.hear {
  color: var(--primary-color);
}

.connecting {
  color: var(--secondary-color);
}
```

N'oubliez pas qu'il y a 2 boutons dans la section, donc j'ai un style de base défini pour eux :

```css
.btn {
  margin-top: 1rem;
  display: inline-block;
  padding: 0.8rem 0.6rem;
  border: none;
  font-size: 1.4rem;
  border-radius: 5px;
  color: #fff;
}

.red {
  background-color: var(--secondary-color);
  margin-right: 1.5rem;
}

.red:hover {
  background-color: #f1262d;
  color: #fff;
}

.blue {
  background-color: var(--primary-color);
}

.blue:hover {
  background-color: #095cf7;
  color: #fff;
}
```

La section prend forme :
![ss-9](https://www.freecodecamp.org/news/content/images/2022/01/ss-9.png)

Ensuite, nous devons faire en sorte que l'`iframe` ressemble à un téléviseur. La propriété `border` nous aidera à y parvenir.

Dans le HTML, rappelez-vous que j'ai 2 balises `div` avec les classes `stand-1` et `stand-2`. Je vais faire les supports pour le vieux téléviseur avec les 2 balises `div` en utilisant la propriété `transform` – qui est instrumentale pour faire tourner ou incliner un élément.

```css
iframe {
  max-width: 30rem;
  border-top: 40px groove var(--primary-color);
  border-bottom: 40px groove var(--primary-color);
  border-right: 28px solid var(--secondary-color);
  border-left: 28px solid var(--secondary-color);
}

.stand-1 {
  height: 90px;
  width: 6px;
  background-color: var(--primary-color);
  transform: rotate(40deg);
  position: relative;
  top: -16px;
  left: 200px;
}
.stand-2 {
  height: 90px;
  width: 6px;
  background-color: var(--secondary-color);
  transform: rotate(-40deg);
  position: relative;
  top: -105px;
  left: 255px;
}
```
Pour pouvoir déplacer les supports, j'ai utilisé la propriété `position` et je l'ai définie sur `relative`, ce qui m'a ensuite aidé à assigner les propriétés `left` et `top` aux supports.

La section hero a maintenant pris forme complète :
![ss-10-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-10-1.png)

## Comment Créer la Section À Propos

La section à propos fera ce que le nom implique – elle détaillera ce qu'est JabTV aussi brièvement que possible. La section contiendra du texte et une image de fond.

Le HTML pour cette section n'est pas compliqué :

```html
 <section class="about" id="apropos">
      <h3>Regardez les Jabs</h3>
      <p>
        Notre objectif principal est d'apporter des matchs de boxe en direct aux fans du monde entier
      </p>

      <h3>Ce n'est pas seulement les Combats !</h3>
      <p>
        Nous diffusons également des documentaires spécialement conçus pour les grands, le mode de vie
        des boxeurs, les nouvelles, et plus encore.
      </p>
</section>
```

Si vous vous demandez pourquoi il n'y a pas de balise `img`, c'est parce que j'ai prévu d'apporter l'image de fond avec la propriété CSS `background`.

La propriété `background` est un raccourci pour :
- `background-color`
- `background-image`
- `background-position`
- `background-cover`
- `background-repeat`
- `background-origin`
- `background-clip`
- et `background-attachment`

Seule la propriété que vous spécifiez sera appliquée, donc vous pouvez toujours sauter l'une des propriétés.

En plus de la propriété de fond, j'utiliserai également Flexbox pour aligner le texte du HTML afin qu'il puisse bien paraître sur l'image de fond.

Voici comment j'ai utilisé la propriété de position en combinaison avec Flexbox :

```css
.about {
  position: relative;
  background: url("../images/jab-transformed.png") no-repeat top center/cover;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 1.5rem;
  margin: 2rem 0;
}
```

Et voici à quoi ressemble la section dans le navigateur jusqu'à présent :
![ss-11](https://www.freecodecamp.org/news/content/images/2022/01/ss-11.png)

Pour rendre les textes lisibles et plus beaux, j'ai utilisé un peu plus de CSS :

```css
.about h3 {
  font-size: 3em;
  margin-bottom: -20px;
}

.about p {
  font-size: 1.5em;
}

.about h3 {
  text-shadow: 2px 2px 2px #333;
}

.about p {
  text-shadow: 2px 2px 2px #333;
  font-size: 1.8rem;
}
```

Notez que j'ai appliqué une ombre de texte aux textes puisqu'ils sont affichés sur une image. Vous devriez faire cela dans chaque projet pour une meilleure accessibilité.

La section À propos a l'air beaucoup plus belle maintenant :
![ss-12](https://www.freecodecamp.org/news/content/images/2022/01/ss-12.png)

## Comment Créer la Galerie d'Images Lightbox

Pour la galerie d'images lightbox, je ne vais pas la faire à partir de zéro – sinon, ce tutoriel deviendrait incroyablement long. Je vais utiliser un plugin appelé simple lightbox, et CSS grid pour l'alignement des images.

Pour utiliser le plugin simple lightbox, vous devez le télécharger depuis leur [site web](https://simplelightbox.com/). Tout ce dont nous avons besoin est le fichier CSS et JavaScript minifié.

Lorsque vous extrayez le fichier zip téléchargé, copiez et collez le fichier CSS et JavaScript minifié dans les sous-dossiers js et css à l'intérieur des assets, et liez-les de manière appropriée, comme je l'ai fait dans le fichier HTML de démarrage.

Pour faire fonctionner la lightbox, vous devez envelopper une balise d'ancrage (`<a>`) autour de l'image dans une balise `<img>`.

L'attribut `href` de la balise d'ancrage doit également correspondre à la source de l'image, et ils doivent tous aller à l'intérieur d'une balise div conteneur à laquelle vous devrez attribuer un attribut de classe.

Cet attribut de classe sera utilisé pour initialiser la galerie avec JavaScript. Ne vous inquiétez pas, le JavaScript ne sera pas compliqué. La galerie présentera des stars de la boxe que je considère parmi les plus grandes.

Le HTML pour la galerie d'images simple lightbox est dans l'extrait de code ci-dessous :

```html
<section class="stars" id="stars">
      <div class="stars-gallery">
        <a href="assets/images/boda--femi.jpg" class="big">
          <img
            src="assets/images/boda--femi.jpg"
            alt="Anthony Joshua"
            title="AJ"
          />
        </a>

        <a href="assets/images/tyson-fury.jpg" class="big">
          <img
            src="assets/images/tyson-fury.jpg"
            alt="Tyson Fury"
            title="Gypsy King"
          />
        </a>

        <a href="assets/images/iron-mike.webp.jpg" class="big">
          <img
            src="assets/images/iron-mike.webp.jpg"
            alt="Iron Mike"
            title="Iron Mike"
          />
        </a>

        <a href="assets/images/ali.jpg" class="big">
          <img
            src="assets/images/ali.jpg"
            alt="Mohammed Ali"
            title="The Greatest"
          />
        </a>

        <a href="assets/images/wilder.jpg" class="big"
          ><img
            src="assets/images/wilder.jpg"
            alt="Deontay Wilder"
            title="Bronze Bomber"
          />
        </a>

        <a href="assets/images/big-george.jpg" class="big">
          <img
            src="assets/images/big-george.jpg"
            alt="George Foreman"
            title="Big George Foreman"
          />
        </a>
      </div>
</section>
```
Pour faire fonctionner la galerie et la faire défiler en douceur lors de la visualisation des images, vous devez l'initialiser avec une ligne de JavaScript :

```js
<script>
     var lightbox = new SimpleLightbox(".stars-gallery a");
</script>
```

Notre galerie d'images lightbox fonctionne maintenant :
![gif1](https://www.freecodecamp.org/news/content/images/2022/01/gif1.gif)

### Comment Styliser la Galerie d'Images Lightbox

Les images sont mal alignées, donc nous devons les arranger avec CSS Grid :
```css
.stars-gallery {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
}
```

Dans l'extrait de code CSS ci-dessus, j'ai ciblé la `div` avec une classe de `stars-gallery` et je lui ai donné un affichage de grid, afin que nous puissions utiliser d'autres propriétés de CSS sur les éléments à l'intérieur de la `div`.

J'ai défini la colonne dont j'ai besoin avec ` grid-template-columns: repeat(5, 1fr);`, ce qui confinera les images dans 5 colonnes.

Jusqu'à présent, voici à quoi ressemble la galerie :
![gif2](https://www.freecodecamp.org/news/content/images/2022/01/gif2.gif)

Il reste encore des choses à faire, car il y a un espace blanc et l'une des images n'est plus visible.

Je vais donner à toutes les images une hauteur et une largeur de 100%, afin qu'elles soient toutes visibles :

```css
.stars-gallery img,
.stars-gallery a {
  width: 100%;
  height: 100%;
}
```
![ss-13](https://www.freecodecamp.org/news/content/images/2022/01/ss-13.png)

Ensuite, je vais cibler la première image et définir une ligne et une colonne de grille pour elle :

```css
.stars-gallery a:first-child {
  grid-row: 1/3;
  grid-column: 1/3;
}
```

Avec la ligne et la colonne de grille définies, la première image occupera les deux premières lignes horizontalement, et les deux premières colonnes verticalement.

Je vais également cibler la deuxième image et définir une colonne de grille pour elle :
```css
.stars-gallery a:nth-child(2) {
  grid-column: 3/5;
}
```

Notre galerie d'images est maintenant bien arrangée et fonctionne bien :
![gif3](https://www.freecodecamp.org/news/content/images/2022/01/gif3.gif)

## Comment Créer la Section des Parties Prenantes

La section des parties prenantes contient celles responsables de la gestion de JabTV.

Le HTML pour cette section est dans l'extrait ci-dessous :

```html
<section class="people" id="partiesprenantes">
      <div class="stakeholders">
        <div class="persons">
          <div class="person-1">
            <img src="assets/images/john.jpg" alt="John Doe" />
            <p class="name">John Doe</p>
            <p class="role">Fondateur</p>
          </div>
          <div class="person-2">
            <img src="assets/images/jane.jpg" alt="Jane Doe" />
            <p class="name">Jane Doe</p>
            <p class="role">Directrice Générale</p>
          </div>
          <div class="person-3">
            <img src="assets/images/jnr.jpg" alt="John Doe Jnr" />
            <p class="name">John Doe JNR</p>
            <p class="role">Analyste en Chef</p>
          </div>
        </div>
      </div>
</section>
```

Voici à quoi ressemble la section :
![ss-14](https://www.freecodecamp.org/news/content/images/2022/01/ss-14.png)

Mais ce n'est pas ce que nous voulons, donc nous avons du stylisme à faire.

### Comment Styliser la Section des Parties Prenantes

Je vais utiliser CSS grid pour disposer les images, les noms et les rôles des parties prenantes. Vous pouvez utiliser Flexbox pour cela si vous le souhaitez. Mais avant cela, je vais faire un petit ajustement pour la section :

```css
 .people {
  margin-top: 2rem;
  padding: 1rem 0;
}

.stakeholders {
  margin: 2rem auto;
  max-width: 1100px;
}

.stakeholders img {
  border-radius: 0.6rem;
}
```
Dans l'extrait de code ci-dessus, j'ai poussé la section vers le bas avec une marge supérieure de 2rem. J'ai ciblé la classe `.people` pour faire cela.

La chose suivante que j'ai faite a été de cibler la classe `.stakeholders`, et je lui ai assigné une marge de `2rem` en haut et en bas. Je l'ai également centrée à gauche et à droite avec `auto`.

En ciblant à nouveau la classe `.stakeholders`, j'ai également donné à la section une largeur maximale de 1100px, afin que des espaces soient créés à gauche et à droite. Cela garantit que l'utilisateur ne regarde pas à l'extrême gauche et à l'extrême droite avant de voir les choses.

Cela rend les choses un peu meilleures :
![ss-15-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-15-1.png)

Pour enfin disposer les images et le texte avec CSS grid, voici ce que j'ai fait :

```css
.persons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  place-items: center;
  gap: 1rem;
}
```

Puisqu'il y a 3 images dans une `div` :

- J'ai défini 3 colonnes pour la section
- aligné tout au centre horizontalement et verticalement avec `place-items`
- ajouté un espace de `1rem` dans les balises `div` avec la propriété `gap`

Tout a maintenant l'air bien sauf le texte :
![ss-16](https://www.freecodecamp.org/news/content/images/2022/01/ss-16.png)

Pour rendre le texte plus beau, je vais le cibler avec les classes `.name` et `.role` et l'aligner au centre, puis lui attribuer une couleur et une police si nécessaire :

```css
.name {
  color: var(--primary-color);
  text-align: center;
}

.role {
  color: var(--secondary-color);
  text-align: center;
  font-size: 0.8rem;
}
```

La section a maintenant l'air assez bien :
![ss-17](https://www.freecodecamp.org/news/content/images/2022/01/ss-17.png)

## Comment Créer la Section d'Abonnement par Email

La section d'abonnement par email sera aussi courte que possible. Je ne ferai aucune intégration pour collecter des emails ici.

À cette fin, si vous voulez simplement collecter des emails, vous pouvez utiliser formspree. Il est préférable d'utiliser un service comme Mailchimp ou Convertkit, cependant, afin que vous puissiez faire quelque chose avec les emails que vous avez collectés.

Le HTML pour cette section ne fait que 12 lignes :

```html
<section class="sub" id="sub">
      <h3>Abonnez-vous à notre newsletter pour les mises à jour</h3>
      <form action="#">
        <input
          type="email"
          name="email"
          id="email-sub"
          class="email-sub"
          required
        />
        <input
          type="submit"
          value="S'abonner"
          id="submit-btn"
          class="submit-btn"
        />
      </form>
</section>
```

Comme vous pouvez le voir, j'ai une entrée pour l'email et un bouton de soumission à l'intérieur d'un formulaire.
La section n'a pas l'air trop mal dans le navigateur :
![ss-18](https://www.freecodecamp.org/news/content/images/2022/01/ss-18.png)

### Comment Styliser la Section d'Abonnement par Email

Nous devons aligner le `h3` et le `form` au centre, et rendre le bouton d'abonnement beau.

Voici comment j'ai aligné le `h3` et le formulaire au centre :

```css
.sub {
  margin-top: 2rem;
}

.sub h3 {
  text-align: center;
}

form {
  text-align: center;
  margin: 0.4rem 2rem;
}
```
Remarquez que j'ai également poussé la section vers le bas avec une marge de `2rem`.

Pour éloigner le formulaire du `h3`, je lui ai donné une marge de `0.4rem` en haut et en bas, et `2rem` à gauche et à droite.

Le formulaire a maintenant l'air beaucoup mieux :
![ss-19](https://www.freecodecamp.org/news/content/images/2022/01/ss-19.png)

La prochaine chose que nous devrions faire est de rendre la zone de saisie et le bouton d'abonnement plus beaux. J'ai attaché une classe `.email-sub` à la zone de saisie, donc je vais la cibler avec la classe et appliquer un peu de style :

```css
.email-sub {
  padding: 0.2rem;
  border: 1px solid var(--primary-color);
  border-radius: 4px;
}

.email-sub:focus {
  border: 1px solid var(--secondary-color);
  outline: none;
}
```

Voici ce qui se passe avec la zone de saisie avec le CSS ci-dessus :

- J'ai donné à la saisie un remplissage de 0.2rem pour un meilleur espacement
- Je lui ai donné (à la saisie) une bordure bleue solide de 1px
- J'ai rendu les coins de la saisie arrondis avec un rayon de bordure de 4px
- lorsque ciblé, c'est-à-dire lorsque vous essayez de taper dans la saisie, j'ai changé la couleur de la bordure en couleur secondaire du site web
- enfin, j'ai défini le contour sur aucun pour supprimer le contour disgracieux qui apparaît lors de la frappe dans les zones de saisie.

J'ai rendu le bouton d'abonnement plus beau avec le CSS ci-dessous :

```css
.submit-btn {
  background-color: var(--primary-color);
  color: #fff;
  padding: 0.3rem;
  margin: 0 0.5rem;
  border: none;
  border-radius: 2px;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: #095cf7;
}
```

La section d'abonnement a maintenant l'air vraiment cool :
![ss-20](https://www.freecodecamp.org/news/content/images/2022/01/ss-20.png)

Je vais également inclure quelques icônes sociales dans la section.
Pour les icônes, j'utiliserai des icônes ioniques.

Les icônes seront enveloppées dans une balise d'ancrage, afin qu'elles puissent hériter des styles définis pour les liens dans les réinitialisations CSS.

```html
<section class="social">
      <h3>Connectez-vous avec nous sur les réseaux sociaux</h3>
      <div class="socicons">
        <a href="#"> <ion-icon name="logo-twitter"></ion-icon> </a>
        <a href="#"> <ion-icon name="logo-instagram"></ion-icon> </a>
        <a href="#"> <ion-icon name="logo-facebook"></ion-icon> </a>
      </div>
</section>
```

Le CSS pour les icônes sociales n'est pas compliqué :

```css
.social {
  text-align: center;
  margin: 2rem;
}

.socicons {
  font-size: 1.3rem;
}
```

Voici à quoi ressemble finalement la section d'abonnement par email :
![ss-21](https://www.freecodecamp.org/news/content/images/2022/01/ss-21.png)

Pour en savoir plus sur les icônes Ion, consultez le fichier readme joint au projet sur GitHub.

## Comment Créer le Pied de Page

Le HTML pour le pied de page est une ligne :

```html
<footer>&copy;2020. Tous droits réservés</footer>
```

Si vous vous demandez ce que signifie `&copy;`, c'est l'entité de caractère pour le © que vous voyez toujours dans les pieds de page des sites web.

Le CSS est fait en 6 lignes :

```css
footer {
  border-top: 1px solid #f1f1f1;
  box-shadow: 0px -2px 3px #f1f1f1;
  text-align: center;
  padding: 2rem;
}
```
J'ai appliqué une `border-top` et une `box-shadow` au pied de page afin que la partie supérieure puisse correspondre à la barre de navigation.

![ss-22](https://www.freecodecamp.org/news/content/images/2022/01/ss-22.png)

## Comment Créer le Bouton de Retour en Haut de Page

Pour une meilleure expérience utilisateur, implémentons un bouton de retour en haut de page. Lorsque l'on clique dessus, ce bouton emmènera l'utilisateur en haut de la page, où qu'il se trouve.

Le HTML pour le bouton de retour en haut de page est dans l'extrait de code ci-dessous :
 ```html
<i class="scroll-up" id="scroll-up"
      ><img
        src="assets/icons/icons8-upward-arrow.png"
        class="socicon up-arrow"
        alt="up-arrow"
/></i>
```

Nous utiliserons les attributs de classe pour styliser le bouton, et les identifiants pour le sélectionner dans notre fichier JavaScript. C'est ainsi que nous ferons les choses dans le CSS et le JavaScript.

Pour rendre le bouton visible partout et beau, je vais lui donner une position fixe et augmenter la largeur et la hauteur. Je vais également lui donner un curseur de pointeur, afin que l'utilisateur sache ce qui se passe lorsqu'il survole le curseur dessus.

```css
.scroll-up {
  position: fixed;
  right: 0.5%;
  bottom: 3%;
  cursor: pointer;
}

.up-arrow {
  width: 3rem;
  height: 3rem;
}
```
![ss-23](https://www.freecodecamp.org/news/content/images/2022/01/ss-23.png)

Pour enfin implémenter la fonctionnalité de retour en haut, nous allons écrire 7 lignes de JavaScript :

```js
const scrollUp = document.querySelector("#scroll-up");

scrollUp.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});
```

**Que fait le script ?**

Dans la première ligne, j'ai sélectionné le bouton en l'assignant à une variable appelée `scrollUp`.

J'ai utilisé la méthode `querySelector()` pour cela car elle est apparemment plus rapide. Vous pouvez utiliser `getElementById` aussi.

Pour obtenir l'action de clic de l'utilisateur sur le bouton, j'ai utilisé une fonctionnalité importante du DOM (Document Object Model) appelée eventListener.

Dans la fonction `eventListener()`, j'ai apporté une méthode d'objet de fenêtre appelée `scrollTo`, qui aide à se déplacer n'importe où sur la page web.

Pour dire à la méthode scrollTo où faire défiler, vous devez lui assigner une propriété de haut et gauche, ou haut et bas selon le cas. J'ai donc assigné un haut et une gauche de 0.

La dernière chose que j'ai faite a été de définir la propriété behavior sur une chaîne de caractères "smooth", afin que les choses s'animent en douceur lorsque le bouton est cliqué.

Notre bouton de retour en haut fonctionne maintenant parfaitement :
![gif4](https://www.freecodecamp.org/news/content/images/2022/01/gif4.gif)

Nous avons maintenant un site web complet ! Mais poussons les choses un peu plus loin en ajoutant un commutateur de thème sombre et clair, puisque beaucoup de gens apprécient désormais l'utilisation des sites web en mode sombre.

## Comment Créer le Commutateur de Thème Sombre et Clair

Pour rendre le commutateur de thème sombre accessible n'importe où sur la page de destination, je vais le placer dans notre barre de navigation collante.

Je vais utiliser :
- une div avec la classe theme-switch pour loger tout
- un type d'entrée de case à cocher pour basculer entre le mode sombre et clair
- une étiquette pour mettre les 2 icônes pour la lune (mode sombre) et le soleil (mode clair)
- une div avec une classe de switcher à l'intérieur de l'étiquette pour créer une forme de balle. Cette forme couvrirait une icône lorsque l'utilisateur basculerait vers le mode clair ou sombre

Voici comment j'ai converti les points ci-dessus en code HTML :

```html
<div class="theme-switch">
    <input type="checkbox" class="checkbox" id="checkbox" />
    <label for="checkbox" class="label">
       <ion-icon name="partly-sunny-outline" class="sun"></ion-icon>
       <ion-icon name="moon-outline" class="moon"></ion-icon>
       <div class="switcher"></div>
    </label>
</div>
```

Et voici à quoi cela ressemble dans le navigateur :
![ss-24_LI](https://www.freecodecamp.org/news/content/images/2022/01/ss-24_LI.jpg)

### Comment Styliser le Commutateur de Thème Sombre et Clair

La première chose que je vais faire est de rendre la case à cocher invisible et de la positionner de manière absolue.

Nous devons faire cela car ce dont nous avons besoin est la fonctionnalité d'une case à cocher pour basculer entre le mode clair et sombre – mais nous n'avons pas besoin de la rendre visible à l'utilisateur.

```css
.checkbox {
  opacity: 0;
  position: absolute;
}
```

Ensuite, je vais positionner l'étiquette de manière relative, centrer tout ce qu'elle contient avec Flexbox, et lui donner un fond sombre. Avec cela et quelques autres stylisations mineures, le commutateur de thème sombre sera plus visible.

```css
.label {
  width: 50px;
  height: 29px;
  background-color: #111;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 30px;
  padding: 6px;
  position: relative;
}
```
![ss-25_LI](https://www.freecodecamp.org/news/content/images/2022/01/ss-25_LI.jpg)

Tout ce que vous voyez maintenant est un fond sombre. Ne vous inquiétez pas. Tout deviendra visible à nouveau.

Souvenez-vous de la `div` avec une classe de `switcher` ? Faisons-la blanche et ronde pour qu'elle ressemble vraiment à une balle. Nous allons également la positionner de manière absolue car elle est à l'intérieur de l'étiquette qui a été positionnée de manière relative.

```css
.switcher {
  background-color: #fff;
  position: absolute;
  top: 5px;
  left: 2px;
  height: 20px;
  width: 20px;
  border-radius: 50%;
}
```

Définir la largeur, la hauteur et un border-radius de 50% est ainsi que vous rendez quoi que ce soit rond en CSS.![ss-27](https://www.freecodecamp.org/news/content/images/2022/01/ss-27.png)

Notre commutateur de thème sombre prend forme, mais rendons les icônes visibles en leur donnant les couleurs appropriées de rougeâtre pour le soleil et de jaune pour la lune.

```css
.moon {
  color: #ffa502;
}

.sun {
  color: #ff4757;
}
```

Enfin, pour pouvoir déplacer la balle de gauche à droite, nous devons utiliser la pseudo-classe :checked sur notre case à cocher, et cibler la balle avec une classe de switcher, puis utiliser la propriété transform pour la déplacer en définissant une valeur en pixels :

```css
.checkbox:checked + .label .switcher {
  transform: translateX(24px);
}
```

Notre balle se déplace maintenant et les icônes s'affichent correctement :
![gif5](https://www.freecodecamp.org/news/content/images/2022/01/gif5.gif)

Ce que nous devons faire maintenant est d'utiliser JavaScript pour basculer entre le mode clair et sombre et définir les couleurs pour le mode sombre.

Vous pouvez trouver l'ensemble des couleurs pour notre thème sombre dans l'extrait ci-dessous :
```css
body.dark {
  background-color: #1e272e;
}

body.dark .bar {
  background-color: #fff;
}

body.dark p {
  color: #fff;
}

body.dark h3 {
  color: #fff;
}

body.dark nav {
  background-color: #1e272e;
  box-shadow: 2px 3px 2px #111010;
}

body.dark ul {
  background-color: #1e272e;
}

body.dark .name {
  color: var(--primary-color);
}

body.dark .role {
  color: var(--secondary-color);
}

body.dark footer {
  color: #fff;
  border-top: 1px solid #111010;
  box-shadow: 0px -2px 3px #111010;
}
```

Et voici comment j'ai utilisé JavaScript pour basculer la classe `body.dark` en utilisant l'événement de changement sur la case à cocher et la méthode `toggle()` du DOM :

```css
const checkbox = document.querySelector("#checkbox");

checkbox.addEventListener("change", () => {
  // Basculer le thème du site web
  document.body.classList.toggle("dark");
});
```

Remarquez que j'ai sélectionné la case à cocher avec un identifiant de `#checkbox` et que je l'ai assignée à une variable `checkbox`. Essayez toujours d'utiliser des identifiants pour JavaScript et des classes pour CSS, afin de ne pas vous confondre.

Les utilisateurs peuvent maintenant basculer entre les modes clair et sombre sur notre page de destination :
![gif6](https://www.freecodecamp.org/news/content/images/2022/01/gif6.gif)

## Comment Rendre la Page de Destination Réactive

La page de destination n'est pas encore réactive, donc nous devons corriger cela.

Pour rendre la page de destination réactive, nous devons créer un menu hamburger pour les appareils plus petits, à l'intérieur d'une requête média. Nous allons également utiliser Flexbox et Grid une fois de plus pour faire en sorte que les sections s'empilent les unes sur les autres.

### Comment Créer un Menu Hamburger pour la Page de Destination

Pour le menu hamburger, la première chose que je vais faire est de rendre les barres visibles sur un appareil avec une largeur d'écran inférieure à 768 pixels.

Je vais également définir un curseur de pointeur pour les barres, afin que l'utilisateur sache qu'il peut cliquer lorsqu'il survole la souris dessus.

```css
@media screen and (max-width: 768px) {
  .hamburger {
    display: block;
    cursor: pointer;
  }
```

Ensuite, je vais changer la direction flex des éléments du menu de navigation en colonne en ciblant la liste non ordonnée qui les contient, afin qu'ils se placent les uns sur les autres.

Je vais également donner à la liste un fond blanc, aligner chaque élément à l'intérieur au centre, et rendre les éléments de la liste fixes avec la propriété left définie à 100%, afin qu'elle soit sortie de la fenêtre d'affichage (invisible).

```css
ul {
    background-color: #fff;
    flex-direction: column;
    position: fixed;
    left: 100%;
    top: 5rem;
    width: 100%;
    text-align: center;
  }
```

Jusqu'à présent, voici ce que nous avons dans le navigateur :
![ss-27-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-27-1.png)

Pour rendre les éléments de navigation visibles, je vais attacher un attribut de classe active à la liste non ordonnée qui les contient et définir `left` à `0`. Cette classe sera basculée avec JavaScript lorsque l'utilisateur clique sur les barres.

```css
ul.active {
    left: 0;
}
```

Les éléments de navigation sont devenus mal espacés :
![ss-28](https://www.freecodecamp.org/news/content/images/2022/01/ss-28.png)

Pour s'assurer que les éléments du menu de navigation sont bien espacés, je vais les cibler avec la classe `.nav-item` et leur donner des marges :

```css
.nav-item {
    margin: 2rem 0;
  }
```

L'extrait de code CSS ci-dessus donne à chaque élément du menu de navigation une marge de 2rem en haut et en bas, et 0 à gauche et à droite, afin qu'ils aient l'air comme ceci :
![ss-29](https://www.freecodecamp.org/news/content/images/2022/01/ss-29.png)

Il y a une dernière chose à faire avec les barres – nous devons nous assurer qu'elles changent en forme de X lorsqu'elles sont cliquées, et reviennent aux barres lorsqu'elles sont cliquées à nouveau.

Pour ce faire, nous allons attacher une classe active au menu hamburger, puis faire tourner les barres. N'oubliez pas que cette classe active sera basculée par JavaScript.

```css
.hamburger.active .bar:nth-child(2) {
    opacity: 0;
  }

  .hamburger.active .bar:nth-child(1) {
    transform: translateY(10px) rotate(45deg);
  }

  .hamburger.active .bar:nth-child(3) {
    transform: translateY(-10px) rotate(-45deg);
  } 
```

Pour effectuer le basculement, nous avons besoin de JavaScript :

```js
const hamburger = document.querySelector("#hamburger");
const navMenu = document.querySelector("ul");

function openMenu() {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
}
```

Voici ce que j'ai fait en JavaScript :

- J'ai sélectionné les barres avec l'identifiant hamburger, et la liste non ordonnée avec l'élément (`ul`)
- J'ai écrit une fonction nommée `openMenu` pour obtenir les classlists du menu hamburger et de la liste non ordonnée, puis j'ai utilisé la méthode `toggle()` pour apporter la classe active.

Nos éléments de menu de navigation sont maintenant basculés d'avant en arrière avec les barres changeant de forme selon les besoins :
![gif8gif](https://www.freecodecamp.org/news/content/images/2022/01/gif8gif.gif)

Mais il y a un problème. Les éléments du menu ne sont pas cachés à chaque fois que l'un d'eux est cliqué. Nous devons faire en sorte que cela se produise pour une meilleure expérience utilisateur.

Pour ce faire, nous avons besoin de JavaScript à nouveau. Nous allons :

- sélectionner tous les éléments de navigation avec querySelectorAll() en ciblant leurs identifiants
- écouter un événement de clic sur chacun des éléments du menu de navigation avec la méthode de tableau forEach()
- écrire une fonction pour supprimer la classe `.active` – ce qui ramènera finalement le menu de navigation à son état d'origine.

```js
const navLink = document.querySelectorAll("#nav-link");

navLink.forEach((n) => n.addEventListener("click", closeMenu));
function closeMenu() {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}
```

Tout fonctionne maintenant bien avec notre menu mobile :
![gif9](https://www.freecodecamp.org/news/content/images/2022/01/gif9.gif)

Si vous avez remarqué, d'autres parties du site web ne sont pas belles sur les appareils mobiles. Il y a même une barre de défilement horizontale ennuyeuse. Nous ne sommes pas en 1998 mais en 2022 !
![gif10](https://www.freecodecamp.org/news/content/images/2022/01/gif10.gif)

L'ajout des styles suivants à la requête média le corrigera :

```css
 .logo {
    font-size: 1.5rem;
  }
 
 .hero {
    flex-direction: column;
    max-width: 500px;
  }

  .intro-text h1 {
    font-size: 2.3rem;
  }

  .btn {
    padding: 0.5rem;
    font-size: 1.2rem;
  }

  iframe {
    max-width: 26rem;
  }

  .stand-1 {
    left: 170px;
  }
  .stand-2 {
    left: 225px;
  }

  .about {
    text-align: center;
  }

  .persons {
    grid-template-columns: repeat(1, 1fr);
  } 
}
```

Avec le CSS ci-dessus, j'ai réduit les tailles, changé la direction en colonne si nécessaire pour que les sections s'empilent les unes sur les autres, et j'ai aligné correctement les supports de la télévision.
![gif11](https://www.freecodecamp.org/news/content/images/2022/01/gif11.gif)

En regardant la page de destination sur des téléphones plus petits, nous pouvons vraiment faire mieux :
![gif12](https://www.freecodecamp.org/news/content/images/2022/01/gif12.gif)

Pour rendre la page de destination réactive sur des téléphones plus petits, je vais intégrer quelques changements sur les appareils mobiles avec une largeur d'écran de 420px et moins :
```css
@media screen and (max-width: 420px) {
  .hero {
    max-width: 330px;
  }

  .intro-text h1 {
    font-size: 2rem;
  }

  iframe {
    max-width: 330px;
  }

  .stand-1 {
    left: 140px;
  }
  .stand-2 {
    left: 195px;
  }
}
```

Nous avons maintenant une page de destination entièrement réactive :
![gif13](https://www.freecodecamp.org/news/content/images/2022/01/gif13.gif).

Récupérez la copie finale du code de la page de destination depuis ce [dépôt GitHub](https://github.com/Ksound22/JabTV-Landing-Page/tree/master).

## Conclusion

Dans ce tutoriel détaillé, vous avez appris comment créer :
- un site web entièrement réactif
- un commutateur de thème sombre
- un menu hamburger
- une galerie d'images lightbox
- un bouton de retour en haut de page.

Ce sont des fonctionnalités que vous pouvez toujours intégrer dans un nouveau projet ou un projet existant, alors n'hésitez pas à revenir à cet article chaque fois que vous en avez besoin.

Si vous trouvez ce tutoriel basé sur du texte utile, partagez-le en tweettant un merci ou en collant le lien sur vos plateformes de médias sociaux.

Merci d'avoir lu !