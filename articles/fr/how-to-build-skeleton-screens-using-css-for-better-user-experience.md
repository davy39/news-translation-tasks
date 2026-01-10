---
title: Exemple de Skeleton Loader – Comment créer un écran squelette avec CSS pour
  une meilleure UX
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-04-25T13:49:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-skeleton-screens-using-css-for-better-user-experience
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Build-Skeleton-Screens-for-Better-UX.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: user experience
  slug: user-experience
- name: Web Development
  slug: web-development
seo_title: Exemple de Skeleton Loader – Comment créer un écran squelette avec CSS
  pour une meilleure UX
seo_desc: 'Content loaders, skeleton screens, ghost elements, and content placeholders.
  These are the names given to the effect we''ll be exploring today.

  Many companies, such as Linkedin, Facebook, Youtube and Slack, use this effect in
  their apps and websites, ...'
---

Les chargeurs de contenu, les écrans squelettes, les éléments fantômes et les espaces réservés de contenu. Ce sont les noms donnés à l'effet que nous allons explorer aujourd'hui.

De nombreuses entreprises, telles que LinkedIn, Facebook, YouTube et Slack, utilisent cet effet dans leurs applications et sites web, comme vous l'avez peut-être remarqué.

Autant nous, développeurs, voulons que nos sites web se chargent le plus rapidement possible, il arrive que beaucoup de données doivent être rendues sur la page, donc les écrans squelettes sont une excellente option.

Dans cet article, nous aborderons :

* [Qu'est-ce qu'un écran squelette](#heading-qu-est-ce-qu-un-ecran-squelette)

* [Différents types d'écrans squelettes](#differentstypesofskeletonscreens)

* [Pourquoi utiliser des écrans squelettes](#heading-pourquoi-utiliser-des-ecrans-squelettes)

* [Quand les utiliser](#heading-quand-les-utiliser)

* [Points à garder à l'esprit](#heading-points-a-garder-a-l-esprit)

* [Création d'une interface utilisateur de chargement squelette Daily Dev](#heading-creation-d-une-interface-utilisateur-de-chargement-squelette-daily-dev)

  * [Configurer le projet](#heading-etape-1-configurer-le-projet)

  * [Concevoir les éléments squelettes](#heading-etape-2-concevoir-les-elements-squelettes)

  * [Cloner le modèle de carte](#heading-etape-3-cloner-le-modele-de-carte)

  * [Créer un fichier JSON](#heading-etape-4-creer-un-fichier-json)

  * [Remplir les éléments HTML](#heading-etape-5-remplir-les-elements-html-avec-le-contenu-approprie)

## Prérequis

Cet article suppose que vous avez :

* Des connaissances en HTML et CSS (SASS)

* Des connaissances en JavaScript (ES6)

Nous utiliserons HTML et SASS pour ce projet. Si vous souhaitez commencer avec SASS, consultez ce [Guide du débutant](https://freecodecamp.org/news/beginners-guide-to-sass).

## Qu'est-ce qu'un écran squelette ?

Un écran squelette est un espace réservé animé qui simule la mise en page d'un site web pendant le chargement des données.

Ils informent l'utilisateur que du contenu est en cours de chargement et, plus important encore, indiquent ce qui est en cours de chargement, qu'il s'agisse d'une image, d'un texte, d'une carte, etc.

Cela donne à l'utilisateur l'impression que le site web est plus rapide car il sait déjà quel type de contenu est en cours de chargement avant qu'il n'apparaisse. Cela est appelé **performance perçue**.

Voici quelques exemples d'écrans squelettes de Facebook et LinkedIn :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/1-2.png align="left")

*État de chargement du fil d'actualité LinkedIn*

![Image](https://www.freecodecamp.org/news/content/images/2022/04/2-2.png align="left")

*État de chargement du fil d'actualité Facebook*

## Différents types d'écrans squelettes

Il existe 2 principaux types d'écrans squelettes :

* Espaces réservés de contenu

* Espaces réservés de couleur

Les espaces réservés de contenu sont généralement des boîtes et des cercles gris clair qui simulent l'apparence de la page, comme montré dans les images ci-dessus pour Facebook et LinkedIn.

Les espaces réservés de couleur sont plus difficiles à créer car ils simulent non seulement la mise en page de l'interface utilisateur, mais aussi la couleur dominante. On les trouve le plus souvent sur les sites web axés sur les images tels que Pinterest et Unsplash.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/9.gif align="left")

*Exemple d'espace réservé de couleur de Pinterest*

## Pourquoi utiliser des écrans squelettes ?

* Ils semblent plus rapides et sont plus conviviaux. Une meilleure performance perçue offre une bonne UX et aide à augmenter le taux de conversion.

* Le problème avec les spinners/chargeurs est que nous ne savons pas ce qui est en cours de chargement ni combien de temps cela prendra.

* L'utilisation de spinners/chargeurs crée une période d'incertitude pour l'utilisateur puisque le temps de chargement est inconnu.

* Les écrans squelettes attirent l'attention de l'utilisateur sur la progression plutôt que sur le temps d'attente.

* Cela crée une illusion de vitesse et de temps de chargement court.

## Quand les utiliser

* Utilisez-les pour informer l'utilisateur que quelque chose est en cours de chargement lorsque plusieurs éléments sont chargés en même temps.

* Utilisez-les lorsque le chargement des données prend plus de 3 secondes.

* Utilisez-les sur les sites web avec beaucoup de trafic.

* Utilisez-les pour un processus en arrière-plan ou de longue durée.

## Points à garder à l'esprit

Lors de la mise en œuvre d'écrans squelettes, nous devons garder à l'esprit l'objectif que nous essayons d'atteindre avec le site web ou l'application, et prioriser le chargement du contenu.

L'utilisation d'écrans de chargement squelettes n'est pas une excuse pour sauter l'optimisation réelle des performances, et si vous pouvez mettre en cache du contenu significatif et l'afficher, ce sera bien.

## Création d'une interface utilisateur de chargement squelette Daily Dev

Dans cette section, nous allons plonger dans la mise en œuvre de l'écran de chargement squelette en suivant un processus étape par étape pour une meilleure compréhension.

Nous allons en créer un similaire à la section de flux de daily.dev.

### Étape 1 : Configurer le projet

Tout d'abord, pour coder avec moi, clonez ou téléchargez le code de départ pour la mise en page [ici](https://github.com/israelmitolu/Skeleton-Loading-using-CSS/tree/master/starter). Vous pouvez télécharger les fichiers en utilisant [DownGit](https://minhaskamal.github.io/DownGit/#/home).

Le code contient la mise en page de la carte, donc nous allons continuer à partir de là dans les étapes suivantes.

Pour commencer, démarrez le serveur de développement dans l'IDE et ouvrez votre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/screencapture-codepen-io-israelmitolu-full-wvpOaQd-2022-04-21-17_16_47.png align="left")

*Mise en page de la carte de départ*

### Étape 2 : Concevoir les éléments squelettes

Il y a 5 éléments que nous voulons créer pour le chargement squelette : l'image du logo, le titre, les détails, l'image de couverture et la section de pied de page.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/4-3.png align="left")

*Éléments squelettes de Daily Dev*

Maintenant, nous allons ajouter des classes `skeleton` aux emplacements des éléments ci-dessus.

Pour le logo,

```html
<img class="card__header header__img skeleton" />
```

Pour le titre, il y aura 2 divs pour représenter les deux lignes que nous avons dans l'image ci-dessus.

```html
<div class="skeleton skeleton-text"></div>
<div class="skeleton skeleton-text"></div>
```

Pour les détails, ajoutez le code suivant à l'intérieur de la div de classe `body__text` :

```html
<div class="skeleton skeleton-text skeleton-text__body"></div>
```

À l'intérieur de la div `body__img`, ajoutez le code suivant :

```html
<img class="skeleton" alt="" id="cover-img" />
```

Pour le pied de page, ajoutez ce code :

```html
<div class="skeleton skeleton-text skeleton-footer"></div>
```

Voici le code HTML complet pour la carte :

```html
<a class="card" id="card-link" target="_blank">
  <div class="card__header">
    <div>
      <img class="card__header header__img skeleton" id="logo-img" alt="" />
    </div>
    <h3 class="card__header header__title" id="card-title">
      <div class="skeleton skeleton-text"></div>
      <div class="skeleton skeleton-text"></div>
    </h3>
  </div>

  <div class="card__body">
    <div class="card__body body__text" id="card-details">
      <div class="skeleton skeleton-text skeleton-text__body"></div>
    </div>

    <div class="card__body body__img">
      <img class="skeleton" alt="" id="cover-img" />
    </div>
  </div>

  <div class="card__footer" id="card-footer">
    <div class="skeleton skeleton-text skeleton-footer"></div>
  </div>
</a>
```

Maintenant, ajoutons un peu de style pour créer les composants squelettes :

```scss
.skeleton {
  animation: skeleton-loading 1s linear infinite alternate;
}

@keyframes skeleton-loading {
  0% {
    background-color: hsl(200, 20%, 80%);
  }
  100% {
    background-color: hsl(200, 20%, 95%);
  }
}

.skeleton-text {
  width: 100%;
  height: 0.7rem;
  margin-bottom: 0.5rem;
  border-radius: 0.25rem;
}

.skeleton-text__body {
  width: 75%;
}

.skeleton-footer {
  width: 30%;
}
```

Voici la mise en page résultante :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/5.gif align="left")

*Chargement du composant de carte*

### Étape 3 : Cloner le modèle de carte

Insérez une balise `template` entre le `container` et l'élément `card` dans le fichier `index.html`.

Dans l'image ci-dessus, il y a une balise `template` que j'ai commentée, et oui, c'est un [élément HTML valide](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) ;). Il est utilisé pour déclarer des fragments de HTML qui peuvent être clonés et insérés dans le document par un script.

```html
<template id="card-template">
```

Par conséquent, assurez-vous d'ajouter la balise de fermeture `</template>` après la balise de fermeture de la div `card`.

Maintenant, regardons le code JavaScript que nous allons utiliser pour cloner le modèle de carte.

Créez une balise `script` juste avant la fin de la balise `body`, et ajoutez le code suivant :

```js
const container = document.querySelector(".container");
const cardTemplate = document.getElementById("card-template");
for (let i = 0; i < 10; i++) {
  container.append(cardTemplate.content.cloneNode(true));
}
```

Le code ci-dessus récupère le conteneur de la page et le modèle de carte, puis crée 9 clones/copies de la carte (ce qui fait 10 au total). Ensuite, il ajoute/insère les cartes dans le conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/6.gif align="left")

*Interface utilisateur squelette de carte clonée*

### Étape 4 : Créer un fichier JSON

Nous avons besoin de données avant de pouvoir ajouter du contenu à la page. Normalement, vous devriez obtenir des données avec un site web externe, mais nous allons utiliser celui que j'ai configuré spécifiquement pour ce projet.

Pour commencer, créez un fichier appelé `data.json` dans le dossier du projet.

Ajoutez le code suivant au fichier JSON.

```json
[
  {
    "id": 1,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/4a287b2e7cb5499bae863f8e7137cdb4",
    "title": "Writing Cleaner CSS Using BEM ",
    "details": "Mar 12, 2022  4m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/dd19e7a56475f39ab1c38167c02c7b58",
    "link": "https://israelmitolu.hashnode.dev/writing-cleaner-css-using-bem-methodology"
  },
  {
    "id": 2,
    "logoImage": "https://daily-now-res.cloudinary.com/image/upload/t_logo,f_auto/v1628412854/logos/freecodecamp",
    "title": "The Beginner's Guide to Sass",
    "details": "Apr 05, 2022  8m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/bec6719be210973098293a32dc732d1e",
    "link": "https://www.freecodecamp.org/news/the-beginners-guide-to-sass/"
  },
  {
    "id": 3,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/devto",
    "title": "I made Squid Game with Javascript",
    "details": "Oct 25, 2021  3m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/1f947033365381cbe322ddf294ad7169",
    "link": "https://dev.to/0shuvo0/i-made-squid-game-with-javascript-10j9"
  },
  {
    "id": 4,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/4a287b2e7cb5499bae863f8e7137cdb4",
    "title": "Using Custom Cursors with Javascript for a Better User Experience",
    "details": "Feb 12, 2022  9m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/3d056b99c95b37cd35ae5cfc6a8b38be",
    "link": "https://israelmitolu.hashnode.dev/using-custom-cursors-with-javascript-for-a-better-user-experience"
  },
  {
    "id": 5,
    "logoImage": "https://daily-now-res.cloudinary.com/image/upload/t_logo,f_auto/v1628412854/logos/freecodecamp",
    "title": "React Best Practices - Tips for Writing Better React Code in 2022",
    "details": "Feb 03, 2022  31m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/5a629fff5583f9ab5f0931d14736b299",
    "link": "https://www.freecodecamp.org/news/best-practices-for-react/"
  },
  {
    "id": 6,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/tnw",
    "title": "You suck at Googling: 5 tips to improve your search skills",
    "details": "Mar 31, 2022  4m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/e318150ae67c2083ff3585a96f366f7b",
    "link": "https://thenextweb.com/news/5-tips-to-improve-your-google-search-skills"
  },
  {
    "id": 7,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/logrocket",
    "title": "A better way of solving prop drilling in React apps",
    "details": "Jan 14, 2022  13m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/6fe4c4060bca638b419d8b2c63d8eaf7",
    "link": "https://blog.logrocket.com/solving-prop-drilling-react-apps/"
  },
  {
    "id": 8,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/dz",
    "title": "Golang and Event-Driven Architecture",
    "details": "Apr 18, 2022  6m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/d06eddd82c62288df6e2600bcda61579",
    "link": "https://dzone.com/articles/golang-and-event-driven-architecture"
  },
  {
    "id": 9,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/4a287b2e7cb5499bae863f8e7137cdb4",
    "title": "Introduction to Git In 16 Minutes",
    "details": "Mar 18, 2021  8m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/3c02111a8f242f607551500432e17a78",
    "link": "https://vickyikechukwu.hashnode.dev/introduction-to-git-in-16-minutes"
  },
  {
    "id": 10,
    "logoImage": "https://res.cloudinary.com/daily-now/image/upload/t_logo,f_auto/v1/logos/4a287b2e7cb5499bae863f8e7137cdb4",
    "title": "How to Create a Sleek Preloader Animation Using GSAP Timeline",
    "details": "Jan 25, 2022  7m read time",
    "coverImage": "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/e238c35cb9d41dd9a5475602aef00119",
    "link": "https://israelmitolu.hashnode.dev/how-to-create-a-sleek-preloader-animation-using-gsap-timeline"
  }
]
```

Pour répliquer la section de flux de Daily Dev, nous avons créé des données qui ont un tableau d'objets avec des propriétés telles que id, logo image, titre, détails et image de couverture.

### Étape 5 : Remplir les éléments HTML avec le contenu approprié

Ajoutez le code suivant à la balise script qui contient votre JavaScript :

```javascript
fetch("data.json")
  .then((response) => response.json())
  .then((posts) => {
    container.innerHTML = "";
    posts.forEach((post) => {
      const div = cardTemplate.content.cloneNode(true);
      div.getElementById("card-link").href = post.link;
      div.getElementById("logo-img").src = post.logoImage;
      div.getElementById("card-title").textContent = post.title;
      div.getElementById("card-details").textContent = post.details;
      div.getElementById("cover-img").src = post.coverImage;
      div.getElementById(
        "card-footer"
      ).innerHTML = ` <ion-icon name="arrow-up"></ion-icon>
          <ion-icon name="chatbox-ellipses"></ion-icon>
          <ion-icon name="bookmark"></ion-icon>`;
      container.append(div);
    });
  });
```

Le code ci-dessus est ce que nous allons utiliser pour ajouter du contenu aux cartes une fois qu'elles ont terminé de se charger.

Maintenant, laissez-moi expliquer le code bit par bit :

```json
fetch("data.json")
  .then((response) => response.json())
```

Ici, nous avons une requête fetch de base, où nous définissons le chemin vers la ressource. Dans ce cas, le fichier `data.json`. Si c'était une API externe, vous utiliseriez l'URL du point de terminaison comme argument :

La méthode `fetch()` ne retourne pas directement le corps de la réponse JSON mais retourne plutôt une promesse qui se résout avec un objet Response.

Pour en savoir plus, consultez la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

```json
.then((posts) => {
    container.innerHTML = "";
    posts.forEach((post) => {
      const div = cardTemplate.content.cloneNode(true);
      div.getElementById("logo-img").src = post.logoImage;
      div.getElementById("card-title").textContent = post.title;
      div.getElementById("card-details").textContent = post.details;
      div.getElementById("cover-img").src = post.coverImage;
      div.getElementById(
        "card-footer"
      ).innerHTML = `<ion-icon name="arrow-up"></ion-icon>
          <ion-icon name="chatbox-ellipses"></ion-icon>
          <ion-icon name="bookmark"></ion-icon>`;
      container.append(div);
    });
  });
```

Ici, nous définissons ce qui doit se passer après avoir récupéré les données.

Le code efface d'abord la page, puis exécute une méthode `forEach()` qui extrait les propriétés du fichier JSON, puis les insère dans les éléments de la carte (image du logo, titre de la carte,...) en utilisant la propriété `.textContent`.

Enfin, pour le pied de page, nous avons utilisé `.innerHTML` pour insérer les icônes en tant que contenu HTML.

Si vous avez tout ajouté correctement, il ne devrait y avoir aucune erreur, et voici notre interface utilisateur de chargement squelette entièrement fonctionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/7-1.gif align="left")

*Notre interface utilisateur squelette Daily Dev terminée*

Consultez la [démo en direct](https://daily-dev-ui.netlify.app/) et le [dépôt de code source](https://github.com/israelmitolu/Skeleton-Loading-using-CSS) sur GitHub.

### Limitation du réseau dans Chrome DevTools

Il est important de noter que nous n'avons pas défini de délai d'attente car cet écran squelette dépend de la vitesse du réseau de l'utilisateur.

Si vous souhaitez le simuler à différentes vitesses de réseau, allez dans l'onglet réseau dans les outils de développement de votre navigateur.

Voici comment faire dans Chrome v100 :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/8.gif align="left")

*Limitation du réseau dans Chrome DevTools*

1. Ouvrez DevTools (Ctrl+Shift+i).

2. Allez dans l'onglet "Réseau".

3. Sélectionnez le type de connexion que vous souhaitez

4. Rechargez la page pour voir les assets se télécharger à la vitesse de connexion spécifiée.

Si les options par défaut ne vous conviennent pas, vous pouvez créer un profil de limitation de réseau personnalisé en sélectionnant l'option tout en haut du menu déroulant.

## Conclusion

Vous êtes arrivé jusqu'à la fin ! Vous avez appris le chargement squelette, et comment il contribue à l'expérience utilisateur en créant l'illusion de vitesse lors du chargement des données, et vous avez mis en œuvre le vôtre.

J'espère que vous avez trouvé ce tutoriel utile et qu'il servira de bon point de départ pour créer diverses interfaces de chargement squelettes.

Si vous avez trouvé cet article instructif, partagez-le avec vos amis et votre réseau. N'hésitez pas non plus à me contacter sur [Twitter](https://twitter.com/israelmitolu) et sur mon [blog](https://israelmitolu.hashnode.dev) où je partage des ressources et des articles pour faire de vous un meilleur développeur.

Merci d'avoir lu, et bon codage !

Avant de partir, voici quelques packages de chargement squelettes pour [React](https://blog.openreplay.com/3-ways-to-implement-skeleton-components-in-react#heading-what-is-a-skeleton-component), [Angular](https://openbase.com/categories/js/best-angular-loading-skeleton-libraries) et [Vue](https://openbase.com/categories/js/best-vue-loading-skeleton-libraries).