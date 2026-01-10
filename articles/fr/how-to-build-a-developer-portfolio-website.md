---
title: Comment créer votre propre site web de portfolio de développeur avec HTML,
  CSS et JavaScript
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-04T20:59:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-developer-portfolio-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/responsive-web-design.png
tags:
- name: Job Hunting
  slug: job-hunting
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: 'self-improvement '
  slug: self-improvement
seo_title: Comment créer votre propre site web de portfolio de développeur avec HTML,
  CSS et JavaScript
seo_desc: "Everyone needs websites and web applications these days. So there are many\
  \ opportunities for you if you work as a web developer. \nBut if you want to get\
  \ a web developer job, you'll need a good portfolio website to showcase your skills\
  \ and experience...."
---

Tout le monde a besoin de sites web et d'applications web de nos jours. Il y a donc de nombreuses opportunités pour vous si vous travaillez en tant que développeur web.

Mais si vous voulez obtenir un emploi de développeur web, vous aurez besoin d'un bon site web de portfolio pour mettre en valeur vos compétences et votre expérience.

Dans ce tutoriel, je vais discuter de certaines des principales raisons pour lesquelles vous devriez créer un site web de portfolio pour vous-même. Ensuite, je vais vous guider à travers la création de votre propre site web de portfolio entièrement réactif avec HTML, CSS et JavaScript.

## Table des matières

* [Qu'est-ce qu'un site web de portfolio de développeur ?](#heading-questce-quun-site-web-de-portfolio-de-developpeur)
* [Pourquoi vous devriez avoir un site web de portfolio](#heading-pourquoi-vous-devriez-avoir-un-site-web-de-portfolio)
* [Projet de portfolio - Comment créer votre propre portfolio de développeur en ligne](#heading-projet-de-portfolio-comment-creer-votre-propre-portfolio-de-developpeur-en-ligne)
* [La structure des dossiers du projet](#heading-la-structure-des-dossiers-du-projet)
* [Le code de base HTML](#heading-le-code-de-base-html)
* [La section de la barre de navigation](#heading-la-section-de-la-barre-de-navigation)
* [Comment styliser la barre de navigation](#heading-comment-styliser-la-barre-de-navigation)
* [Comment créer la section héro](#heading-comment-creer-la-section-hero)
* [Comment styliser la section héro](#heading-comment-styliser-la-section-hero)
* [Comment créer la section Plus à mon sujet](#heading-comment-creer-la-section-plus-a-mon-sujet)
* [Comment créer la section Compétences](#heading-comment-creer-la-section-competences)
* [Comment styliser la section Compétences](#heading-comment-styliser-la-section-competences)
* [Comment créer la section Projets](#heading-comment-creer-la-section-projets)
* [Comment styliser la section Projet](#heading-comment-styliser-la-section-projet)
* [Comment créer la section Contact](#heading-comment-creer-la-section-contact)
* [Comment styliser la section Contact](#heading-comment-styliser-la-section-contact)
* [Comment styliser les icônes sociales](#heading-comment-styliser-les-iconessociales)
* [Comment ajouter le bouton de défilement vers le haut](#heading-comment-ajouter-le-bouton-de-defilement-vers-le-haut)
* [Le HTML pour le bouton de défilement vers le haut](#heading-le-html-pour-le-bouton-de-defilement-vers-le-haut)
* [Comment styliser l'icône de défilement vers le haut](#heading-comment-styliser-licone-de-defilement-vers-le-haut)
* [Comment rendre votre site web de portfolio réactif](#heading-comment-rendre-votre-site-web-de-portfolio-reactif)
* [Comment créer la requête média pour les tablettes et les téléphones mobiles (largeur maximale 720px)](#heading-comment-creer-la-requete-media-pour-les-tablettes-et-les-telephones-mobiles-largeur-maximale-720px)
* [Comment créer le menu hamburger](#heading-comment-creer-le-menu-hamburger)
* [Le JavaScript pour le menu hamburger](#heading-le-javascript-pour-le-menu-hamburger)
* [Comment rendre la section héro réactive](#heading-comment-rendre-la-section-hero-reactive)
* [Comment rendre la section Plus à mon sujet réactive](#heading-comment-rendre-la-section-plus-a-mon-sujet-reactive)
* [Comment rendre la section Compétences réactive](#heading-comment-rendre-la-section-competences-reactive)
* [Comment rendre la section Projets réactive](#heading-comment-rendre-la-section-projets-reactive)
* [Comment rendre le formulaire de contact réactif](#heading-comment-rendre-le-formulaire-de-contact-reactif)
* [Comment rendre le site web réactif sur les petits téléphones](#heading-comment-rendre-le-site-web-reactif-sur-les-petits-telephones)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un site web de portfolio de développeur ?

Un site web de portfolio de développeur fournit des informations pertinentes aux employeurs potentiels sur vos compétences, votre expérience et les projets sur lesquels vous avez travaillé.

Vous pouvez considérer votre site web de portfolio comme votre CV en ligne.

## Pourquoi vous devriez avoir un site web de portfolio

### 1. Un site web de portfolio augmente votre présence en ligne

En tant que développeur, vous avez besoin d'une présence en ligne. Vous pouvez cultiver cette présence en ligne sur les plateformes de médias sociaux telles que Twitter, Facebook et Instagram. Mais celles-ci ne vous appartiennent pas entièrement, car les modérateurs de ces plateformes ont presque un contrôle total sur votre compte.

Avec votre propre site web de portfolio, il est en ligne sur votre propre domaine. Et les gens peuvent facilement vous trouver lorsqu'ils recherchent votre nom sur un moteur de recherche comme Google, à condition que vous mettiez en place les bonnes choses en matière de SEO.

### 2. Un site web de portfolio est votre CV en ligne

Votre site web de portfolio est comme votre CV en ligne. Les clients potentiels et les responsables de recrutement peuvent facilement vous trouver en ligne et consulter vos projets précédents et vos compétences.

Cela signifie également que lorsque quelqu'un veut vous donner l'opportunité de travailler pour lui et qu'il demande vos projets précédents, vous lui donnez simplement un lien vers votre site web (votre portfolio). Il contient non seulement vos projets, mais aussi vos compétences et des informations sur votre expérience passée.

### 3. Un site web de portfolio montre des preuves d'expertise dans votre domaine

Avoir (et encore moins construire vous-même) un site web de portfolio en tant que développeur envoie un message clair que vous mettez vos compétences en pratique et que vous savez ce que vous faites.

Un portfolio peut également aider à établir la confiance avec les clients, car ils ont des preuves directes de la qualité de votre travail.

## Projet de portfolio - Comment créer votre propre portfolio de développeur en ligne

Vous pouvez créer un site web de portfolio cool pour vous-même avec HTML, CSS et JavaScript. Et c'est ce que nous allons faire ici.

Je l'ai déjà fait il y a quelques mois et je l'ai mis à disposition de tous en tant que produit gratuit sur Gumroad, alors j'ai décidé de créer un tutoriel sur la façon dont je l'ai fait.

Voici la [démo en direct](https://eager-williams-af0d00.netlify.app/?) de ce que nous allons construire.

Pour me suivre, vous pouvez récupérer les fichiers de démarrage depuis [GitHub](https://github.com/Ksound22/developer-portfolio/tree/starter).

### La structure des dossiers du projet

Pour éviter la confusion, je vais organiser les fichiers HTML, CSS, JavaScript, icônes et images du projet dans leurs dossiers respectifs.

Le fichier HTML va dans le dossier racine, et les fichiers image, icône, CSS et JavaScript seront dans leurs sous-dossiers séparés dans un dossier d'actifs. C'est une pratique courante.

![ss1](https://www.freecodecamp.org/news/content/images/2021/10/ss1.png)

Il y a également un fichier readme contenant tous les outils que j'ai utilisés dans le projet, avec leurs liens respectifs. Il est disponible dans les fichiers de démarrage.

### Le code de base HTML

Chacun a ses préférences lors du codage d'un projet entier avec HTML, CSS et JavaScript. Certains aiment définir tout le code de base HTML d'abord, puis le CSS plus tard, mais j'aime tout faire section par section.

Je vais donc commencer par la section de la barre de navigation. Mais il est bon de montrer à quoi ressemble le code de base HTML d'abord :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Styles CSS -->
    <link rel="stylesheet" href="assets/css/styles.css" />

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

    <!-- Animate CSS CDN -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    />
    <title>Jane Doe | Développeur Web</title>
  </head>

  <body>
    <!-- Barre de navigation -->

    <!-- Section héro -->

    <!-- Plus à propos -->

    <!-- Section compétences -->

    <!-- Section projets -->

    <!-- Section contact -->

    <!-- Comptes sociaux - Fixés à droite -->

    <!-- Défilement vers le haut -->

    <!-- Section pied de page -->

    <!-- Scripts du site web -->
    <script src="assets/js/app.js"></script>

    <!-- Scripts des icônes Ion -->
    <script
      type="module"
      src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"
    ></script>
    <script
      nomodule
      src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"
    ></script>
  </body>
</html>
```

J'ai commenté toutes les sections dans le HTML pour que vous puissiez mieux suivre. Dans le code de base, il y a également les CDN pour animate CSS (une bibliothèque d'animations CSS), et Ionic icons, la bibliothèque d'icônes que j'ai choisie pour le projet.

J'ai créé une favicon via Favicon IO et je l'ai liée dans la section head. La favicon est la petite image qui s'affiche sur un onglet du navigateur.

### La section de la barre de navigation

La section de la barre de navigation contient le logo simple de texte `h1`, et le menu de navigation :

```html
 <nav>
      <h1>JANE DOE</h1>
      <ul class="navigation">
        <li><a href="#about" class="nav-link">À propos</a></li>
        <li><a href="#skills" class="nav-link">Compétences</a></li>
        <li><a href="#projects" class="nav-link">Projets</a></li>
        <li><a href="#contact" class="nav-link">Contact</a></li>
      </ul>
      <button class="burger-menu" id="burger-menu">
        <ion-icon class="bars" name="menu-outline"></ion-icon>
      </button>
</nav>
```

Si vous vous demandez ce que représente l'élément bouton, ce sont les barres pour basculer le menu de navigation sur mobile (un menu hamburger). Cela sera caché sur le bureau mais affiché sur mobile.

Je vais également lier les sections individuelles du site web à ces éléments de navigation, de sorte que lorsque l'utilisateur clique sur l'un des éléments de navigation, il est dirigé vers la section qui correspond à l'élément de navigation sur lequel il clique.

C'est pourquoi j'ai défini les attributs de référence hypertexte (`href`) sur `#about`, `#skills`, `#projects` et `#contacts`, respectivement. La section individuelle du site web aura ces attributs comme identifiants.

La barre de navigation ressemble maintenant à ceci : 
![ss2](https://www.freecodecamp.org/news/content/images/2021/10/ss2.png)

### Comment styliser la barre de navigation

La barre de navigation a définitivement besoin d'un peu de style pour la rendre plus agréable.

Avant de styliser correctement la barre de navigation, je vais déclarer quelques variables CSS pour faciliter les choses plus tard. En effet, avec les variables CSS, il est plus facile d'éviter la redondance et la répétition dans votre fichier CSS.

La syntaxe pour déclarer les variables CSS ressemble à ceci :
```css
:root {
  --nom-de-la-variable: valeur;
}
```

Pour utiliser la variable, vous faites ceci :

```css
sélecteur {
  propriété: var(--nom-de-la-variable);
}
```

Je vais également importer la police Roboto de Google et déclarer quelques réinitialisations CSS pour supprimer certaines fonctionnalités par défaut telles que la marge et le remplissage pour les éléments, la `text-decoration` pour les balises d'ancrage et le `list-style-type` pour les listes.

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,700&display=swap");

/* Variables */
:root {
  --font-family: "Roboto", sans-serf;
  --normal-font: 400;
  --bold-font: 700;
  --bolder-font: 900;
  --bg-color: #fcfcfc;
  --primary-color: #4756df;
  --secondary-color: #ff7235;
  --primary-shadow: #8b8eaf;
  --secondary-shadow: #a17a69;
  --bottom-margin: 0.5rem;
  --bottom-margin-2: 1rem;
  --line-height: 1.7rem;
  --transition: 0.3s;
}
/* Fin des variables */

html {
  scroll-behavior: smooth;
}

/* Réinitialisations CSS */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

ul {
  list-style-type: none;
}

a {
  text-decoration: none;
  color: var(--primary-color);
}

a:hover {
  color: var(--secondary-color);
}

body {
  font-family: var(--font-family);
}
```

Si vous remarquez, j'ai défini un état de survol pour tous les liens sur le site web des lignes 39 à 41. Lorsque l'utilisateur survole un lien, il change pour la couleur secondaire que j'ai définie dans les variables CSS.

Voici une bonne règle de base pour déclarer les variables CSS : si vous trouvez que vous utilisez souvent la même propriété et la même valeur dans le même fichier CSS, vous devriez déclarer une variable pour éviter la répétition.

Vous devriez également rendre les noms de vos variables aussi descriptifs que possible, comme je l'ai fait, afin d'aider les autres qui pourraient travailler avec votre code.

Avec les réinitialisations, il y a quelques changements dans la barre de navigation dans le navigateur :
![ss3](https://www.freecodecamp.org/news/content/images/2021/10/ss3.png)

Pour styliser la barre de navigation et aligner le contenu, je vais utiliser CSS Flexbox :

```css
nav {
  position: sticky;
  top: 0;
  left: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 3.5rem;
  background-color: var(--bg-color);
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
}
```

**Que fait le CSS ci-dessus ?**

J'ai rendu la barre de navigation collante avec la propriété de position, de sorte qu'elle reste en haut quoi qu'il arrive.

La propriété `z-index` avec la valeur 1 s'assure que la barre de navigation s'affiche par-dessus tout autre élément sur la page web. C'est ainsi que vous créez une barre de navigation collante.

En outre, j'ai également appliqué une ombre au bas de la barre de navigation avec la propriété `box-shadow`.

La barre de navigation a un nouveau look : 
![ss4](https://www.freecodecamp.org/news/content/images/2021/10/ss4.png)

Mais nous n'avons pas encore terminé. Les éléments du menu de navigation doivent être côte à côte, et non les uns sur les autres. Je vais le faire avec Flexbox également.

Je vais également terminer le reste du style de la barre de navigation en rendant le h1, les éléments de navigation et le bouton du menu hamburger plus beaux. Je vais le faire avec quelques variables CSS initialement déclarées.

```css
nav h1 {
  color: var(--primary-color);
}

nav a {
  color: var(--primary-color);
  transition: var(--transition);
}
nav a:hover {
  color: var(--secondary-color);
  border-bottom: 2px solid var(--secondary-color);
}

nav ul {
  display: flex;
  gap: 1.9rem;
}

nav ul li {
  font-weight: var(--bold-font);
}
```

Le menu hamburger doit également être caché. Il a une classe de `.burger-menu`, donc nous pouvons définir un affichage de none avec lui et également rendre le bouton plus beau.

```css
.burger-menu {
  color: var(--primary-color);
  font-size: 2rem;
  border: 0;
  background-color: transparent;
  cursor: pointer;
  display: none;
}
```

Notre barre de navigation est bien plus belle maintenant : 
![ss5](https://www.freecodecamp.org/news/content/images/2021/10/ss5.png)

### Comment créer la section héro

La section suivante sur laquelle nous allons travailler est la section héro. Cela ne prendra pas autant de travail que la barre de navigation.

Le code de base HTML pour la section héro est dans l'extrait de code ci-dessous :

```html
<section class="hero" id="about">
      <img
        src="assets/images/wfh_1.svg"
        alt="jane-doe"
        loading="lazy"
        class="hero-img"
      />
      <div class="bio animate__animated animate__shakeX">
        <h2 class="bio-title">À propos de moi</h2>
        <p class="bio-text">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia sed
          dolorem fugit sapiente porro veniam pariatur dolore nostrum delectus
          inventore tempore minus nemo, iste ullam illo laboriosam maiores
          repudiandae quos!
        </p>
      </div>
</section>
```

La seule chose qui est un peu étrange, ce sont les classes `animate__animated animate__shakeX` attachées à la div contenant le texte « À propos de moi ». Les noms de classe proviennent d'animate CSS et ils servent à animer le conteneur de texte « À propos de moi ».

Avec cela, le site web prend un nouveau look :
![ss6](https://www.freecodecamp.org/news/content/images/2021/10/ss6.png)

### Comment styliser la section héro

Flexbox viendra à la rescousse une fois de plus ! Cette section contient deux ensembles principaux de contenu - une image et du texte dans une div. Nous pouvons donc utiliser flexbox pour les afficher côte à côte. Vous pouvez voir comment cela fonctionne dans l'extrait de code CSS ci-dessous :

```css
.hero {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  max-width: 68.75rem;
  margin: auto;
}
```
![ss7](https://www.freecodecamp.org/news/content/images/2021/10/ss7.png)

Notre image de Jane Doe est trop grande, nous devons donc réduire sa largeur et sa hauteur. Nous devons également styliser le texte de la bio (texte À propos de moi) pour une meilleure lisibilité. Les variables CSS initialement déclarées seront très utiles ici.

```css
.hero img {
  height: 37.5rem;
  width: 37.5rem;
}

.bio {
  width: 25rem;
  padding: 0.625rem;
  border-radius: 6px;
  box-shadow: 0px 2px 15px 2px var(--primary-shadow);
}

.bio h1 {
  margin-bottom: var(--bottom-margin);
}

.bio p {
  line-height: var(--line-height);
  padding: 0.3rem 0;
}
```

La section héro est maintenant belle : 
![ss8](https://www.freecodecamp.org/news/content/images/2021/10/ss8.png)

### Comment créer la section Plus à mon sujet

J'ai inclus cette section pour inclure quelques informations supplémentaires sur Jane Doe avec un texte de remplissage.

Vous pouvez profiter de cela pour inclure des informations que vous n'avez pas pu mettre dans la section À propos de moi.

Le code de base HTML pour cette section est assez court et simple :

```html
    <section class="more-about">
      <h2>Plus à mon sujet</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis
        nesciunt excepturi quos obcaecati incidunt voluptatem ipsam sunt ipsum,
        autem deleniti cupiditate molestias quis unde quae totam porro dicta
        iure animi inventore, veniam hic! Omnis nulla, delectus a voluptatibus
      </p>
      <p>
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequuntur
        nostrum dolor minus, libero delectus praesentium perferendis
      </p>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero,
        consequuntur labore? Ea totam voluptas amet!
      </p>
    </section>
```

Le CSS est également simple. Tout ce que nous allons faire est de définir une `background-color` avec la variable CSS `--bg-color`, rendre la section lisible en définissant le padding, la marge, la hauteur de ligne et aligner le texte h2 au centre :

```css
.more-about {
  background-color: var(--bg-color);
  padding: 1rem 6rem;
}

.more-about h2 {
  margin-bottom: var(--bottom-margin);
  text-align: center;
}

.more-about p {
  line-height: var(--line-height);
  padding: 0.4rem;
}
```

Dans le navigateur, la section Plus à mon sujet ressemble à ceci :
![ss9](https://www.freecodecamp.org/news/content/images/2021/10/ss9.png)

### Comment créer la section Compétences

À partir de la démo en direct, vous verrez que la section compétences contient des compétences pertinentes telles que HTML, CSS, JavaScript, et ainsi de suite. J'ai pu obtenir les icônes de ces langages en tant que SVGs depuis Icons8.

Le code de base HTML pour cette section est dans l'extrait de code ci-dessous :

```html
 <section class="skills" id="skills">
      <h2 class="skill-header">Mes principales compétences</h2>

      <div class="skills-wrapper">
        <div class="first-set animate__animated animate__pulse">
          <img
            src="assets/icons/icons8-html-5.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
          <img
            src="assets/icons/icons8-css3.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
          <img
            src="assets/icons/icons8-javascript.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
        </div>

        <div class="second-set animate__animated animate__pulse">
          <img
            src="assets/icons/icons8-bootstrap.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
          <img
            src="assets/icons/icons8-react-native.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
          <img
            src="assets/icons/icons8-git.svg"
            alt=""
            loading="lazy"
            class="icon icon-card"
          />
        </div>
      </div>
    </section>
```

Il y a six icônes au total. Et au lieu de devoir les aligner avec Flexbox, je les ai regroupées en deux endroits (3 par groupe), avec les classes first-set et second-set, afin qu'elles restent les unes sur les autres. Cela signifie que les styles que nous appliquerons seront plus lisibles. Facile !

Remarquez que j'ai attaché l'attribut loading aux icônes et images individuelles et que je l'ai défini sur lazy. Cela garantira que les images ne sont chargées que lorsque l'utilisateur fait défiler jusqu'aux sections qui les contiennent. Cela accélérera ensuite le temps de chargement, car seul ce qui est nécessaire sera chargé.

### Comment styliser la section Compétences

Sans style, la section compétences ressemble à ceci :
![ss10edited](https://www.freecodecamp.org/news/content/images/2021/10/ss10edited.jpg)

Nous devrions styliser un peu la section car elle n'est pas encore assez belle :

```css
.skills {
  max-width: 68.75rem;
  margin: auto;
  text-align: center;
  margin-top: 2.5rem;
}

.skill-header {
  margin-bottom: 1rem;
}

.skills-wrapper img {
  padding: 1.25rem;
}

.icon {
  width: 11.875rem;
  height: 11.25rem;
}
```

Dans le CSS ci-dessus, j'ai défini une largeur maximale pour toute la section afin de pousser les éléments vers le centre pour une meilleure expérience utilisateur.

D'autres styles que nous avons appliqués concernent la clarté et la lisibilité. Par exemple, j'ai augmenté la taille des icônes pour les rendre plus visibles avec les propriétés de largeur et de hauteur. J'ai également appliqué un padding de 1rem (16 pixels) à toutes les icônes pour les éloigner un peu les unes des autres.

La section compétences est maintenant cool :
![ss11](https://www.freecodecamp.org/news/content/images/2021/10/ss11.png)

Cependant, je pense que la section peut être meilleure, alors j'ai décidé d'apporter quelques améliorations supplémentaires avec la propriété box-shadow.

Souvenez-vous, dans le HTML, qu'il y a un attribut de classe appelé `.icon-card` attaché à toutes les icônes. Je vais utiliser le nom de la classe pour mettre toutes les icônes dans une carte :

```css
.icon-card {
  background-color: #fff;
  border-radius: 11px;
  box-shadow: 0 3px 10px var(--secondary-shadow);
  padding: 20px;
  margin: 10px;
}
```
La section compétences est bien meilleure :
![ss12](https://www.freecodecamp.org/news/content/images/2021/10/ss12.png)
Regardez ça !


### Comment créer la section Projets

L'un des principaux objectifs d'un site web de portfolio est de montrer vos projets. Nous devons donc créer une section pour présenter les projets sur lesquels vous avez travaillé par le passé.

Cette section est probablement la plus fastidieuse à styliser, mais Flexbox ne cessera pas d'être notre ami.

Le HTML pour cette section est dans l'extrait de code ci-dessous :

```html
<section class="projects" id="projects">
      <h2 class="projects-title">Certains de mes projets récents</h2>
      <div class="projects-container">
        <div class="project-container project-card">
          <img
            src="assets/images/expenseTracker.png"
            alt="suivi-des-depenses"
            loading="lazy"
            class="project-pic"
          />
          <h3 class="project-title">Suivi des dépenses</h3>
          <p class="project-details">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quas
            ratione vel inventore labore commodi modi quos culpa aut saepe!
            Alias!
          </p>
          <a href="#" target="_blank" class="project-link">Voir</a>
        </div>
        <div class="project-container project-card">
          <img
            src="assets/images/netflixClone.png"
            alt="clone-netflix"
            loading="lazy"
            class="project-pic"
          />
          <h3 class="project-title">Clone Netflix</h3>
          <p class="project-details">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quas
            ratione vel inventore labore commodi modi quos culpa aut saepe!
            Alias!
          </p>
          <a href="#" target="_blank" class="project-link">Voir</a>
        </div>
        <div class="project-container project-card">
          <img
            src="assets/images/greenyEarth.png"
            alt="terre-verte"
            loading="lazy"
            class="project-pic"
          />
          <h3 class="project-title">Terre verte</h3>
          <p class="project-details">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quas
            ratione vel inventore labore commodi modi quos culpa aut saepe!
            Alias!
          </p>
          <a href="#" target="_blank" class="project-link">Voir</a>
        </div>
      </div>
    </section>
```

En regardant le HTML, il y a trois projets au total, tous dans leurs divs individuelles avec le nom de classe project-container et project-card. Ces noms de classe seront instrumentaux pour styliser les projets de manière cohérente.

L'élément de section conteneur lui-même a une classe de projects, et un attribut id de projects également. Le nom de classe est pour le style, et l'id est pour le lier au lien Projets sur la barre de navigation.

Les projets ont leurs images individuelles avec le nom de classe `project-pic`, leurs titres avec une classe de `project-title`, plus de détails avec le nom de classe `project-details`, et des liens avec le nom de classe `project-link`.

Le seul but de donner à tous des noms de classe uniques est de les styliser.

Ce sont quelques-uns des projets sur lesquels j'ai travaillé moi-même lorsque je commençais en tant que développeur.

La section des projets ressemble à ceci dans le navigateur :
![projects-unstyled](https://www.freecodecamp.org/news/content/images/2021/10/projects-unstyled.gif)

La section ne semble pas encore bonne, bien qu'il y ait même une barre de défilement horizontale gênante causée par les images. Nous avons donc beaucoup à faire avec CSS.

### Comment styliser la section Projet

Tout d'abord, je vais donner à toute la section une couleur de fond en définissant la couleur grisâtre (--bg-color) que nous avons déclarée dans les variables CSS comme valeur.

Je vais également réduire la largeur et la hauteur des images de projet en utilisant la classe `project-pic`. Ensuite, j'utiliserai Flexbox pour placer les projets côte à côte.

```css
.projects {
  background-color: var(--bg-color);
  padding: 32px 0;
  margin-top: 2rem;
}

.project-pic {
  width: 65%;
  height: 60%;
}

.projects-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

La section semble beaucoup mieux :
![ss13Edited](https://www.freecodecamp.org/news/content/images/2021/10/ss13Edited.jpg)

Les images semblent maintenant meilleures, mais le titre du projet, les détails du projet et les liens du projet doivent être alignés correctement dans leurs conteneurs individuels.

L'ensemble de la section projet doit également être poussé vers le centre. Vous n'avez pas besoin de Flexbox pour cela, bien que cela puisse être fait en définissant la propriété d'alignement du texte sur la valeur center :

```css
.projects-title {
  text-align: center;
  margin-bottom: 1rem;
}

.project-container {
  text-align: center;
  width: 21.875rem;
  padding: 1rem;
}
```

Remarquez que j'ai également défini une largeur de `21.875rem (350 pixels)` pour les conteneurs de projets individuels. Cela les éloignera des côtés pour une meilleure expérience utilisateur. Dans ce cas, l'utilisateur n'aurait pas besoin de regarder tout le long avant de tout voir.

La section semble maintenant meilleure :
![ss14](https://www.freecodecamp.org/news/content/images/2021/10/ss14.png)

Nous pouvons encore améliorer cette section. Les titres des projets, les détails des projets et les liens des projets semblent regroupés, nous devons donc ajouter un peu de padding et de marges.

Les conteneurs de projets individuels doivent également avoir un aspect plus distinct. La propriété `box-shadow` sera à nouveau instrumentale ici, je vais donc les mettre dans leurs cartes individuelles.

```css
.project-container p {
  padding: 0.4rem;
}

.project-title {
  margin-bottom: var(--bottom-margin);
}

.project-details {
  margin-bottom: var(--bottom-margin);
}

.project-card {
  background-color: #fff;
  border-radius: 11px;
  box-shadow: 0 3px 10px var(--primary-shadow);
  padding: 20px;
  margin: 10px;
}
```

La section projet semble beaucoup mieux maintenant :
![ss15](https://www.freecodecamp.org/news/content/images/2021/10/ss15.png)

### Comment créer la section Contact

Si un employeur ou un client potentiel trouve votre site web de portfolio attrayant, il pourrait vouloir vous contacter. Vous voudrez donc avoir un formulaire de contact dans cette section, ainsi que des liens vers vos profils de réseaux sociaux.

Le HTML pour cette section ressemble à ceci :

```html
<section class="contact" id="contact">
      <h2>Contactez-moi</h2>
      <div class="contact-form-container">
        <div class="contact-form">
          <form action="https://formspree.io/f/xyylngw" method="POST">
            <div class="form-control">
              <label for="name">Nom</label>
              <input
                type="text"
                id="name"
                name="sender-name"
                placeholder="Entrez votre nom"
                class="input-field"
                required
              />
            </div>
            <div class="form-control">
              <label for="email">Email</label>
              <input
                type="email"
                id="email"
                name="sender-email"
                placeholder="Entrez votre email"
                class="input-field"
                required
              />
            </div>
            <div class="form-control">
              <label for="message">Message</label>
              <textarea
                id="message"
                cols="60"
                rows="10"
                placeholder="Entrez votre message"
                name="message"
                class="input-field"
                required
              ></textarea>
            </div>
            <input
              type="submit"
              value="Envoyer"
              id="submit-btn"
              class="submit-btn"
            />
          </form>
        </div>
      </div>
    </section>
```

Ici, nous avons créé un formulaire de contact avec des champs de saisie pour le nom et l'email, une `textarea` pour que les gens puissent entrer le message à envoyer, et un bouton d'envoi pour envoyer le message afin que vous puissiez le voir.

Si vous regardez bien l'élément formulaire, vous verrez que j'ai un attribut action défini sur une URL de Formspree. C'est ce que j'ai choisi pour la soumission du formulaire. Avec Formspree, vous pouvez recevoir le message directement dans votre boîte de réception sans avoir à configurer un serveur avec du PHP ou du JavaScript complexe.

Notez que vous ne pouvez pas utiliser mon URL - cela ne fonctionnera pas pour vous. Vous pouvez facilement configurer le vôtre sur le site web de Formspree gratuitement. J'ai également joint une ressource sur la façon de configurer Formspree au fichier readme du projet.

J'ai défini certains attributs `id` et `class` pour les entrées individuelles afin de les styliser. Il y a également un attribut `name` pour tous les champs de saisie. Cela est requis par le service de soumission de formulaire Formspree.

Pour obtenir une validation de base, j'ai attaché un attribut `required`, de sorte que le formulaire refuse de s'envoyer si l'utilisateur laisse l'un des champs de saisie non remplis.

### Comment styliser la section Contact

Sans style, la section contact ne semble pas du tout bonne :
![ss16Edited](https://www.freecodecamp.org/news/content/images/2021/10/ss16Edited.jpg)

Tout ce que je vais faire en CSS est d'aligner tout le contenu au centre et de rendre les champs de saisie plus beaux.

Avec les propriétés d'alignement du texte et de marge, vous pouvez aligner le h2 et le conteneur pour le formulaire de contact au centre.

Je vais également mettre tout le formulaire dans une carte avec la propriété `box-shadow`.

```css
.contact {
  margin-top: 2rem;
}

.contact h2 {
  text-align: center;
  margin-bottom: var(--bottom-margin-2);
}

.contact-form-container {
  max-width: 40.75rem;
  margin: 0 auto;
  padding: 0.938rem;
  border-radius: 5px;
  box-shadow: 0 3px 10px var(--secondary-shadow);
}
```
![ss17](https://www.freecodecamp.org/news/content/images/2021/10/ss17.png)

Les champs de saisie, la zone de texte, les étiquettes et les espaces réservés ont définitivement besoin d'un peu de style pour aider à l'alignement et à la clarté :

```css
.contact-form-container label {
  line-height: 2.7em;
  font-weight: var(--bold-font);
  color: var(--primary-color);
}

.contact-form-container textarea {
  min-height: 6.25rem;
  font-size: 14px;
}

.contact-form-container .input-field {
  width: 100%;
  padding-top: 10px;
  padding-bottom: 10px;
  border-radius: 5px;
  border: none;
  border: 2px outset var(--primary-color);
  font-size: 0.875rem;
  outline: none;
}
```

Le formulaire semble mieux maintenant : ![ss18](https://www.freecodecamp.org/news/content/images/2021/10/ss18.png)

Mais les espaces réservés ne sont pas cohérents avec les étiquettes. Nous devons donc leur donner une couleur et un peu de padding. Je vais leur donner la couleur principale définie dans les listes de variables CSS.

Pour sélectionner les espaces réservés pour le style, vous pouvez utiliser la pseudo-classe placeholder :

```css
.input-field::placeholder {
  padding: 0.5rem;
  color: var(--primary-color);
}
```

![ss19](https://www.freecodecamp.org/news/content/images/2021/10/ss19.png)

Dans le formulaire de contact, la seule chose qui reste est de styliser le bouton. Les boutons sont assez faciles à styliser :

```css
.submit-btn {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  background-color: #fff;
  border: 2px solid var(--primary-color);
  border-radius: 5px;
  font-size: 1rem;
  font-weight: var(--bold-font);
  transition: var(--transition);
}
```

Dans l'extrait de code CSS ci-dessus, j'ai fait en sorte que le bouton traverse tout le conteneur du formulaire en lui donnant une largeur de 100 %. Je l'ai également rendu plus visible avec un peu de padding, une marge, une bordure et un poids de police plus gras.

La propriété `border-radius` avec une valeur de 5px supprime les bords tranchants et la transition sert à ralentir un peu les choses lorsque le bouton est en état de survol.

L'état de survol est défini dans l'extrait de code CSS ci-dessous :

```css
.submit-btn:hover {
  background-color: var(--primary-color);
  border: 2px solid var(--primary-color);
  cursor: pointer;
}
```

Le formulaire semble beaucoup mieux maintenant :
![contact-form-hover-effect](https://www.freecodecamp.org/news/content/images/2021/10/contact-form-hover-effect.gif)

N'oubliez pas que le fait d'avoir vos liens de réseaux sociaux sur votre site web de portfolio est un plus pour toute personne qui pourrait vouloir vous contacter. C'est la prochaine chose que nous allons faire, et nous allons le faire de manière unique.

Le HTML pour les boutons sociaux est dans l'extrait de code ci-dessous :

```html
    <div class="socials">
      <a href="#" target="_blank"
        ><img
          src="assets/icons/icons8-twitter-circled.gif"
          alt="Twitter"
          loading="lazy"
          class="socicon"
      /></a>
      <a href="#" target="_blank"
        ><img
          src="assets/icons/icons8-instagram.gif"
          alt="Instagram"
          loading="lazy"
          class="socicon"
      /></a>
      <a href="#" target="_blank"
        ><img
          src="assets/icons/icons8-linkedin-circled.gif"
          alt="Linkedin"
          loading="lazy"
          class="socicon"
      /></a>
      <a href="#" target="_blank"
        ><img src="assets/icons/icons8-github.gif" alt="Github" class="socicon"
      /></a>
```

Les icônes sociales que j'ai choisies sont des icônes gif animées d'icons8. Je les ai toutes mises dans un conteneur avec la classe `socials`, et je leur ai donné une classe individuelle `socicon` pour le style.

Jetez un coup d'œil à quelques icônes de réseaux sociaux animées qui vous font un clin d'œil ci-dessous :
![animated-social-icons](https://www.freecodecamp.org/news/content/images/2021/10/animated-social-icons.gif)

### Comment styliser les icônes sociales

```css
.socials {
  display: flex;
  flex-direction: column;
  position: fixed;
  right: 1%;
  bottom: 50%;
}

.socicon {
  width: 2rem;
  height: 2rem;
}
```

Avec le CSS ci-dessus, les icônes sociales seront fixées à droite sur la page web, de sorte que toute personne visitant le site web les voie, peu importe où elle fait défiler.

J'ai également réduit la taille des icônes en leur attribuant à toutes des valeurs de propriété `width` et `height` réduites.
![good-icons](https://www.freecodecamp.org/news/content/images/2021/10/good-icons.gif)

Regardez ça !

La seule chose qui reste à faire est le pied de page. Il n'y a rien de complexe dans le HTML et le CSS du pied de page à part l'entité de caractère réservé pour le symbole de copyright et le cœur :

```html
<footer>
      <p class="copy">&copy; Copyright 2021</p>
      <p class="copy">
        Construit avec &#x2661; par
        <a href="https://twitter.com/koladechris" target="_blank"
          >Kolade Chris (Ksound)</a
        >
      </p>
</footer>
```

```css
footer {
  background-color: var(--bg-color);
  padding: 1.25rem;
  text-align: center;
  margin: 2rem 0 0;
}
```

Nous avons maintenant un site web de portfolio complet !
![full-fledged-portfolio](https://www.freecodecamp.org/news/content/images/2021/10/full-fledged-portfolio.gif)

Mais nous devons le rendre réactif, car il ne semble pas bon sur les appareils plus petits :
![unresponsive-portfolio](https://www.freecodecamp.org/news/content/images/2021/10/unresponsive-portfolio.gif)

Nous devons faire en sorte que tout le contenu des sections individuelles s'affiche sur une section au-dessus de l'autre (dans une disposition en colonne). Nous pouvons le faire assez facilement avec des requêtes média et Flexbox.

Avant d'ajouter les requêtes média pour la réactivité, implémentons un bouton de défilement vers le haut avec HTML, CSS et JavaScript.

## Comment ajouter le bouton de défilement vers le haut

### Le HTML pour le bouton de défilement vers le haut
Pour le HTML, j'ai obtenu une icône animée d'Icons8 et j'ai décidé de la mettre dans une balise i.

La balise i a une classe de `scroll-up` pour le style et un id de `scroll-up` pour la sélectionner avec JavaScript. Cela est dû au fait que dans mes projets, j'aime utiliser les classes pour le style et les ids pour les fonctionnalités JavaScript.

```html
  <i class="scroll-up" id="scroll-up"
      ><img
        src="assets/icons/icons8-upward-arrow.gif"
        class="socicon up-arrow"
        alt="scroll-up"
    /></i>
```

### Comment styliser l'icône de défilement vers le haut

Je vais rendre l'icône de défilement vers le haut fixe comme les icônes sociales. Je vais également lui donner une propriété de curseur de type pointeur, de sorte que le curseur change lorsque l'utilisateur le survole.

Avec la classe up-arrow attachée à l'icône de défilement vers le haut, je vais également augmenter la taille de l'icône pour une meilleure visibilité :

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

L'icône semble bonne :
![scroll-up-first](https://www.freecodecamp.org/news/content/images/2021/10/scroll-up-first.gif)

Mais elle ne fait encore rien. Nous devons donc la rendre fonctionnelle avec quelques lignes de JavaScript :

```js
// fonctionnalité de défilement vers le haut
const scrollUp = document.querySelector("#scroll-up");

scrollUp.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});
```

**Que fait le script ci-dessus ?**

La première ligne sélectionne le bouton de défilement vers le haut avec l'attribut id qui lui est attaché dans le HTML. Nous avons utilisé la méthode `querySelector()`. Vous pouvez également utiliser la méthode `getElementById()`.

Dans les lignes restantes, j'ai utilisé l'écouteur d'événements `click` pour obtenir l'action de clic de l'utilisateur et exploiter la partie `scrollTo` de l'objet windows pour rendre le bouton fonctionnel.

Avec cette fonctionnalité, lorsque l'utilisateur clique sur le bouton de défilement vers le haut, la page fait défiler vers le haut et le côté gauche du site web en douceur. J'ai fait cela en définissant le haut sur `0`, la gauche sur `0` et le comportement sur `smooth`.

![scroll-up](https://www.freecodecamp.org/news/content/images/2021/10/scroll-up.gif)

Vous pouvez en savoir plus sur l'objet windows en ouvrant la console des outils de développement de votre navigateur. Tapez window et appuyez sur entrer, puis vous verrez tout ce qui est disponible dans l'objet windows, comme je l'ai fait ci-dessous :

![window-object](https://www.freecodecamp.org/news/content/images/2021/10/window-object.gif)

## Comment rendre votre site web de portfolio réactif

Pour rendre le site web réactif, nous allons utiliser les requêtes média CSS et Flexbox.

Tout d'abord, nous devons rendre les images et le texte plus petits, puis nous devons faire en sorte que le contenu de chaque section s'affiche dans une disposition verticale en définissant la `flex-direction` sur colonne.

Dans la requête média, je vais utiliser 2 points d'arrêt - `720px` et `420px`.

Le point d'arrêt 720px est pour les tablettes et les téléphones mobiles, et 420px est pour les petits téléphones comme un iPhone 6, et les petits téléphones Android.

Les points d'arrêt des requêtes média sont les points auxquels vous souhaitez que le contenu d'un site web réponde en fonction de la largeur d'un appareil. Ainsi, tout code placé sous le point d'arrêt 720px se reflète sur les appareils avec un écran inférieur ou supérieur à 720px, selon que vous spécifiez max-width ou min-width.

Dans le cas d'une largeur maximale de `720px`, la syntaxe de la requête média ressemble à ceci :

```css
@media screen and (max-width: 720px) {
  /* les changements se reflètent sur l'écran avec une largeur de 720px et en dessous */
}
```

### Comment créer la requête média pour les tablettes et les téléphones mobiles (largeur maximale 720px)

Nous allons commencer à rendre le site web réactif dès la barre de navigation, car la barre de navigation ne semble pas bonne sur les appareils plus petits.

![ss21](https://www.freecodecamp.org/news/content/images/2021/10/ss21.png)

Tout d'abord, je vais réduire le padding de la barre de navigation afin que le logo `h1` et les éléments du menu de navigation s'intègrent bien :

```css
nav {
    padding: 1.5rem 1rem;
  }
```

Les choses semblent maintenant un peu meilleures :
![ss22](https://www.freecodecamp.org/news/content/images/2021/10/ss22.png)

Sur les petits appareils, les éléments du menu de navigation doivent être les uns sur les autres, et ils doivent être cachés. Il est donc temps de mettre à jour le code pour que le menu hamburger soit initialement caché.

### Comment créer le menu hamburger

Pour créer le menu hamburger, nous devons sortir les éléments du menu de navigation de la fenêtre. Ensuite, nous devons définir une classe de `show` sur les éléments de liste de navigation qui sera basculée avec quelques lignes de JavaScript (rappelons que les éléments de navigation sont dans une liste non ordonnée).

```css
 nav ul {
    position: fixed;
    background-color: var(--bg-color);
    flex-direction: column;
    top: 86px;
    left: 10%;
    width: 80%;
    text-align: center;
    transform: translateX(120%);
    transition: transform 0.5s ease-in;
  }

   nav ul li {
    margin: 8px;
  }
```

Dans l'extrait de code CSS ci-dessus, j'ai défini une position fixe sur la liste non ordonnée (`ul`) pour la faire flotter sur l'écran. Je l'ai également poussée vers le bas de 86px depuis le haut avec `top: 86px`, et de 10% vers la gauche.

Je lui ai donné une largeur de 80% de son parent (l'élément nav du HTML), je l'ai poussée vers le centre avec `text-align: center`, et enfin je l'ai cachée avec la propriété transform définie sur `translateX(120%)`. Cela la poussera vers la droite et la forcer à sortir de la fenêtre.

Et maintenant, lorsque l'utilisateur clique pour afficher les éléments de navigation, ils glissent tous depuis la droite. Super.

Si vous voulez que les éléments du menu de navigation glissent depuis la gauche, changez la valeur de la propriété `transform` en `transform: translateX(-120%)` (c'est l'opposé direct de `transform: translateX(120%)`). C'est aussi simple que cela, selon votre préférence.

J'ai également attribué une marge de 8px aux éléments de navigation pour leur donner plus d'espace.

La barre de navigation ressemble maintenant à ceci :
![ss22-1](https://www.freecodecamp.org/news/content/images/2021/10/ss22-1.png)

La barre du menu hamburger reste cachée. Nous devons donc l'afficher en lui donnant un affichage de bloc, en définissant une classe de show pour la translation sur l'axe des x à 0 afin de l'afficher, puis en la basculant avec JavaScript.

```css
 .burger-menu {
    display: block;
  }

  nav ul.show {
    transform: translateX(0);
  }
```
![ss24](https://www.freecodecamp.org/news/content/images/2021/10/ss24.png)

Nos barres de menu hamburger sont maintenant affichées, mais les éléments de navigation restent cachés. Pour les afficher, nous devons basculer la classe show en marche et en arrêt avec JavaScript.

### Le JavaScript pour le menu hamburger

Pour basculer les éléments du menu de navigation de la barre de navigation en marche et en arrêt avec JavaScript, nous devons d'abord sélectionner tous les éléments pertinents de la barre de navigation et les stocker dans quelques variables :

```js
// Sélections du menu hamburger de la barre de navigation

const burger = document.querySelector("#burger-menu");
const ul = document.querySelector("nav ul");
const nav = document.querySelector("nav");
```

- La variable `burger` sélectionne les barres du menu hamburger
- La variable `ul` sélectionne les éléments de la liste (les liens de navigation ensemble)
- La variable `nav` sélectionne le conteneur lui-même (l'élément nav)

Ce que nous devons faire ensuite est de basculer la classe `nav ul.show` lorsque l'utilisateur clique sur la barre du menu hamburger. Nous allons faire cela en ajoutant un écouteur d'événements de clic à la barre du menu hamburger, puis en utilisant la méthode toggle pour supprimer et ajouter la classe `show`.

Rappelez-vous que nous l'avons sélectionnée et stockée dans une variable appelée `burger`.

```js
burger.addEventListener("click", () => {
  ul.classList.toggle("show");
});
```

Nos éléments de navigation peuvent maintenant être basculés en marche et en arrêt :
![nav-toggling-quirk](https://www.freecodecamp.org/news/content/images/2021/10/nav-toggling-quirk.gif)

Mais il y a un problème - le menu de navigation mobile n'est pas caché à chaque fois que l'un des liens des éléments de navigation est cliqué. Nous devons donc supprimer la classe nav ul.show lorsque l'un des liens des éléments de navigation est cliqué.

Nous pouvons le faire avec quelques lignes de JavaScript également :

```js
// Fermer le menu hamburger lorsqu'un lien est cliqué

// Sélectionner les liens de navigation
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach((link) =>
  link.addEventListener("click", () => {
    ul.classList.remove("show");
  })
);
```

Rappelez-vous que les liens de navigation ont une classe de `nav-link` depuis le HTML. J'ai donc sélectionné tous ceux avec cette classe et je les ai mis dans une variable appelée navLink. Nous avons fait cela avec la méthode `querySelectorAll()`.

J'ai ensuite parcouru tous les liens avec la méthode de tableau `forEach` et j'ai écouté un événement de clic sur tous. Ensuite, j'ai utilisé la méthode `remove()` fournie par le DOM pour supprimer la classe `show` à chaque fois que l'un des éléments du menu de navigation est cliqué. Cela fera sortir tous les éléments de la liste de la fenêtre.

![nav-toggling-quirk-fixed](https://www.freecodecamp.org/news/content/images/2021/10/nav-toggling-quirk-fixed.gif)

Regardez ça !

C'est beaucoup de travail. Avec ce que nous venons de couvrir, vous pouvez créer un menu hamburger pour n'importe quel site web.

### Comment rendre la section héro réactive

La section héro ne semble pas si bonne pour le moment :
![ss25](https://www.freecodecamp.org/news/content/images/2021/10/ss25.png)

Tout ce que nous devons faire est de lui donner une direction de flex en colonne dans la requête média, réduire la largeur et la hauteur de l'image de Jane Doe, et rendre le texte À propos de moi (texte de bio) lisible.

```css
.hero {
    margin-top: -4rem;
    flex-direction: column;
    gap: 0;
  }

  .hero img {
        height: 37.5rem;
        width: 30rem;
    }

  .bio {
    margin-top: -7rem;
    width: 20.5rem;
  }
```

La section héro semble meilleure maintenant :
![ss26](https://www.freecodecamp.org/news/content/images/2021/10/ss26.png)

### Comment rendre la section Plus à mon sujet réactive

La section Plus à mon sujet ne semble pas mauvaise, mais nous pouvons certainement l'améliorer :
![ss27](https://www.freecodecamp.org/news/content/images/2021/10/ss27.png)

J'ai le CSS suivant pour la rendre lisible et plus présentable :

```css
 .more-about {
    margin-top: 2rem;
    padding: 1rem 3.5rem;
  }

  .more-about h2 {
    text-align: center;
  }

  .more-about p {
    text-align: justify;
  }
```

J'ai poussé toute la section un peu vers le bas et j'ai augmenté le padding de tous les côtés, aligné le `h2` au centre et justifié le texte.
![ss28](https://www.freecodecamp.org/news/content/images/2021/10/ss28.png)

### Comment rendre la section Compétences réactive

Les icônes de compétences semblent trop grandes :
![ss29](https://www.freecodecamp.org/news/content/images/2021/10/ss29.png)

Tout ce que nous devons faire dans la requête média est de réduire la taille des icônes avec les propriétés de largeur et de hauteur :

```css
.icon {
    width: 5.875rem;
    height: 5.25rem;
  }
```

![ss30](https://www.freecodecamp.org/news/content/images/2021/10/ss30.png)

### Comment rendre la section Projets réactive

Dans la section projets, nous devons faire en sorte que les trois projets s'empilent les uns sur les autres en définissant la direction de flex sur colonne. Je vais également réduire un peu la largeur des conteneurs individuels.

```css
 .projects-container {
    flex-direction: column;
  }

  .project-container {
    width: 20.875rem;
  }
```

### Comment rendre le formulaire de contact réactif

La largeur du formulaire de contact doit être réduite pour l'éloigner des côtés et s'assurer que les icônes des réseaux sociaux fixes ne sont pas au-dessus. 

Tout ce que nous devons faire est de définir une largeur maximale :

```css
 .contact-form-container {
    max-width: 23.75rem;
  }
```

Le formulaire de contact semble maintenant mieux :
![ss32](https://www.freecodecamp.org/news/content/images/2021/10/ss32.png)

### Comment rendre le site web réactif sur les petits téléphones

Sur les petits téléphones comme l'iPhone 6, 7 et 8 plus, les icônes sociales et l'icône de défilement vers le haut ne s'affichent pas. Il y a aussi une barre de défilement horizontale.
![smaller-phones-responive-quirks](https://www.freecodecamp.org/news/content/images/2021/10/smaller-phones-responive-quirks.gif)

Pour corriger ces problèmes, je vais ajouter quelques requêtes média au point d'arrêt 420px :

```css
@media screen and (max-width: 420px) {
  .hero img {
    height: 37.5rem;
    width: 23rem;
  }

  .bio {
    width: 18.3rem;
  }

  .project-container {
    width: 17.875rem;
  }

  .contact-form-container {
    max-width: 17.75rem;
  }
} 
```

J'ai réduit la taille de notre image de Jane Doe, et j'ai également réduit la largeur du texte de bio (texte À propos de moi), du conteneur de projet et du conteneur de formulaire de contact.

Tous ces changements feront en sorte que les icônes fixes du côté droit du site web s'affichent - les icônes des réseaux sociaux et de défilement vers le haut.
![smaller-phones-responsiveness-quirk-fixed](https://www.freecodecamp.org/news/content/images/2021/10/smaller-phones-responsiveness-quirk-fixed.gif)

Tout semble maintenant bon :
![fully-responsive](https://www.freecodecamp.org/news/content/images/2021/10/fully-responsive.gif)

C'est la fin de tout. Nous avons un site web de portfolio entièrement réactif.

Vous pouvez télécharger la version finale sous forme de fichier zip depuis ce [dépôt GitHub](https://github.com/Ksound22/developer-portfolio).

Vous pouvez également consulter la [démo en direct](https://eager-williams-af0d00.netlify.app/?) du site web de portfolio. Il contient un fichier readme qui contient des informations sur les outils que j'ai utilisés et comment vous pouvez personnaliser le site web.

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est un site web de portfolio de développeur et pourquoi vous devriez en avoir un.

Vous avez également appris comment créer un site web de portfolio entièrement réactif avec HTML, CSS et JavaScript.

Les différentes parties de ce tutoriel sont chacune de petits projets qui, combinés, se transforment en un site web d'une page géant. Par exemple, vous pouvez créer un design de carte, une barre de menu réactive, un formulaire de contact fonctionnel et un bouton de défilement vers le haut, comme le couvre le tutoriel.

N'hésitez pas à personnaliser le site web à votre goût.

Si vous trouvez ce tutoriel utile, vous pouvez le partager avec vos amis et votre famille. J'apprécierais vraiment cela.