---
title: Qu'est-ce que CSS Subgrid ? Un tutoriel pratique
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-08-21T18:17:03.633Z'
originalURL: https://freecodecamp.org/news/what-is-css-subgrid
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724227015705/f55ae862-c81f-4453-af92-cb96acf0d13d.png
tags:
- name: CSS
  slug: css
- name: webdev
  slug: webdev
- name: web layout
  slug: web-layout
seo_title: Qu'est-ce que CSS Subgrid ? Un tutoriel pratique
seo_desc: 'When designers create layouts in their mockups, everything including the
  content typically looks perfectly aligned and consistent.

  But in the real world, user-generated content varies wildly. For example, one testimonial
  card might have a brief sente...'
---

Lorsque les designers créent des mises en page dans leurs maquettes, tout, y compris le contenu, semble généralement parfaitement aligné et cohérent.

Mais dans le monde réel, le contenu généré par l'utilisateur varie considérablement. Par exemple, une carte de témoignage peut comporter une phrase courte, tandis qu'une autre contient un paragraphe entier. Cela rend difficile le maintien d'un alignement parfait.

CSS Subgrid peut facilement gérer ces incohérences de mise en page Web. Il permet aux éléments imbriqués de s'aligner sur leur grille parente, garantissant un aspect cohérent quel que soit le contenu.

Dans ce tutoriel, nous explorerons comment utiliser CSS Subgrid pour créer une section de produits qui reste flexible et esthétique. Vous pouvez avancer pour voir ce que nous allons construire [ici](#heading-comment-construire-une-section-de-produits-avec-subgrid).

### Table des matières

* [Les limites de CSS Grid](#heading-les-limites-de-css-grid)
    
* [Comment construire une section de produits avec Subgrid](#heading-comment-construire-une-section-de-produits-avec-subgrid)
    
* [Comment fonctionne Subgrid ?](#heading-comment-fonctionne-subgrid)
    
* [Comment utiliser Subgrid](#heading-comment-utiliser-subgrid)
    
* [Subgrid dans les DevTools du navigateur](#heading-subgrid-dans-les-devtools-du-navigateur)
    
* [Conclusion](#heading-conclusion)
    

## Les limites de CSS Grid

Ajouter un `display: grid` à un conteneur signifie que seuls les enfants directs deviennent des grilles. Si ces enfants directs ont également des enfants, ils ne font pas partie de la grille principale – ils s'affichent donc selon leur flux normal.

C'est problématique car, sans lien direct les uns avec les autres, chacun occupera l'espace dont il a besoin sans se soucier de ses voisins. Cela conduit à un contenu mal aligné comme vous pouvez le voir sur la gauche de l'image ci-dessous.

![Une image montrant un exemple de grille avec et sans subgrid](https://cdn.hashnode.com/res/hashnode/image/upload/v1724192748056/e6d99008-5a04-4a83-927d-0d46be2e17a5.png align="center")

Le projet que nous allons construire explore une solution Subgrid en quelques lignes de code CSS qui nous aidera à obtenir l'alignement souhaité visible sur la droite de l'image ci-dessus.

## Comment construire une section de produits avec Subgrid

### Ce que nous allons construire

![Une image du projet final à construire dans ce tutoriel](https://cdn.hashnode.com/res/hashnode/image/upload/v1724225971840/767e1b9e-bd54-4505-b3ad-2c39901b28c3.png align="center")

Consultez-le sur [Codepen](https://codepen.io/ophyboamah/pen/OJevpQP).

### Prérequis

* Connaissances de base en HTML et CSS (Pour un rappel sur le fonctionnement de CSS Grid, consultez [mon précédent article sur les mises en page Web](https://www.freecodecamp.org/news/web-layouts-use-css-grid-and-flex-to-create-responsive-webpages/))
    
* Un IDE (éditeur de texte)
    
* Un navigateur Web
    

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Comme l'accent de cet article est mis sur Subgrid, nous n'accorderons pas beaucoup d'importance au code HTML et CSS de départ. Nous allons simplement les passer en revue rapidement pour que vous puissiez vous installer. Ensuite, nous plongerons dans l'apprentissage de l'ajout de Subgrid.</div>
</div>

### Code HTML :

Dans notre fichier `index.html`, nous allons créer la structure de base du projet, ce qui inclut la liaison de notre fichier CSS et des Google Fonts – le tout à l'intérieur de la balise `<head>`. Dans la balise `<body>`, nous créerons un conteneur principal pour loger toutes les cartes. Ensuite, nous créerons trois cartes individuelles sous forme d'articles – chacune avec une icône, un titre, du texte et un bouton.

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Lexend+Deca:wght@100..900&display=swap"
    rel="stylesheet">
  <link
    href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@100..900&family=Inter:wght@100..900&family=Lexend+Deca:wght@100..900&display=swap"
    rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <title>Cartes de produits Subgrid d'Ophy</title>
</head>
<body>
  <div class="cards-container">
    <article class="sedans">
      <img src="./assets/icon-sedans.svg" alt="une icône montrant une berline">
      <h3>Berlines</h3>
      <p>
        Choisissez une berline pour son prix abordable et son excellente économie de carburant. Idéal pour rouler en ville
        ou lors de votre prochain voyage - laissez libre cours à votre imagination.
      </p>
      <button>
        En savoir plus
      </button>
    </article>
    <article class="suvs">
      <img src="./assets/icon-suvs.svg" alt="une icône montrant un SUV">
      <h3>SUV</h3>
      <p>
        Optez pour un SUV pour son intérieur spacieux, sa puissance et sa polyvalence.
      </p>
      <button>
        En savoir plus
      </button>
    </article>
    <article class="luxury">
      <img src="./assets/icon-luxury.svg" alt="une icône montrant un véhicule de luxe">
      <h3>
        Extrême Luxe
      </h3>
      <p>
        Roulez dans les meilleures marques de voitures sans prix excessifs. Profitez du confort amélioré d'une location de luxe
        et arrivez avec style.
      </p>
      <button>
        En savoir plus
      </button>
    </article>
  </div>
<footer>
      Cartes de produits Subgrid d'Ophy | <a href="https://www.frontendmentor.io/">Design de Frontend Mentor </a>
</footer>
</body>
</html>
```

### Code CSS :

Dans notre fichier `style.css`, nous allons d'abord définir nos styles globaux et de base :

```css
/* Réinitialisations globales */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Variables racines */
:root {
  --primary-font: "Lexend Deca", sans-serif;
  --secondary-font: "Big Shoulders Display", sans-serif;
  --heading-color: #F2F2F2;
  --font-color: #FFF;
  --sedans-background: #E28625;
  --suv-background: #006971;
  --luxury-background: #004140;
  --heading-font-size: 2.5rem;
  --button-font-size: 0.9rem;
  --default-padding: 1rem 0;
}

/* Styles de base */
html {
  font-size: 16px;
}

body {
  font-family: var(--primary-font);
  margin: 0 auto;
  max-width: 920px;
}

/* Styles de titre */
h3 {
  font-family: var(--secondary-font);
  color: var(--heading-color);
  font-size: var(--heading-font-size);
}
/* Styles de paragraphe */
p {
  font-family: var(--primary-font);
  font-optical-sizing: auto;
  font-weight: 200; 
  color: var(--font-color);
  padding: var(--default-padding);
  line-height: 1.5;
}
/* Pied de page */
  footer {
    text-align: center;
    margin-top: 1.5rem;
    a {
      text-decoration: none;
    }
  }
```

Ensuite, nous allons styliser le conteneur principal des cartes et le bouton. Notez que nous avons spécifié des colonnes et des lignes pour le conteneur de cartes en utilisant respectivement `grid-template-columns` et `grid-template-rows`.

```css
/* Conteneur */
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-template-rows: repeat(4, auto);
  min-height: 31.25rem;
  margin-top: 10.688rem;
  button {
    font-size: var(--button-font-size);
    background: var(--font-color);
    border: none;
    padding: 0.5rem 1.5rem;
    border-radius: 25px;
    width: 70%;
    &:hover {
      cursor: pointer;
      background: none;
      color: var(--font-color);
      border: 1px solid var(--font-color);
    }
}
```

Ensuite, nous créerons des styles de cartes généraux ainsi que des styles de cartes individuels.

```css
/* Tous */
.suvs,
.sedans,
.luxury {
  padding: 3rem;
  h3 {
    font-size: var(--heading-font-size);
    text-transform: uppercase;
  }
}
/* Berlines */
.sedans {
  background-color: var(--sedans-background);
  border-radius: 10px 0 0 10px;
  button {
    color: var(--sedans-background);
  }
}
/* SUV */
.suvs {
  background-color: var(--suv-background);
  button {
    color: var(--suv-background);
  }
}
/* Luxe */
.luxury {
  background-color: var(--luxury-background);
  border-radius: 0 10px 10px 0;
  button {
    color: var(--luxury-background);
  }
}
```

L'image ci-dessous sera le résultat après l'exécution du code de départ ci-dessus. Les cartes ont été créées sous forme de colonnes de grille, mais les lignes à l'intérieur des cartes individuelles ne s'alignent pas correctement en raison de la différence de longueur du contenu.

![Une image des cartes de produits sans Subgrid](https://cdn.hashnode.com/res/hashnode/image/upload/v1724176252090/b3540574-6779-4486-8622-fbf8fe8e9a09.png align="center")

## Comment fonctionne Subgrid ?

L'affichage ci-dessus serait un cauchemar pour les designers et les parties prenantes jusqu'à ce qu'il soit corrigé. Auparavant, pour résoudre ce problème, les développeurs devaient transformer ces cartes en grilles imbriquées. Mais ce code finissait par devenir désordonné et difficile à maintenir.

CSS Subgrid permet à un élément de grille d'hériter des pistes de grille (lignes ou colonnes) de sa grille parente, plutôt que de définir les siennes. Ceci est particulièrement utile pour maintenir un alignement cohérent entre les grilles imbriquées et leurs grilles parentes.

Dans notre projet, au lieu de définir une ligne pour les icônes, les titres, le texte et les boutons, nous pouvons les faire hériter de la même structure de leur grille parente (le conteneur de cartes).

## Comment utiliser Subgrid

Pour créer un `subgrid`, attribuez le mot-clé comme valeur à `grid-template-columns` ou `grid-template-rows` d'une grille imbriquée.

Pour implémenter cela dans notre projet, nous allons d'abord transformer l'élément article en conteneur de grille afin de placer ses enfants dans une grille structurée. Ensuite, `grid-template-rows` reçoit la valeur `subgrid`. Cela hérite de la structure de lignes de la grille du conteneur de cartes.

Définir `grid-row` sur `span 4` signifie essentiellement que l'élément doit occuper un espace qui couvre 4 lignes de la grille parente.

```css
  article {
    display: grid;
    grid-template-rows: subgrid;
    grid-row: span 4;
}
```

### Code facultatif

Le code ci-dessous pour positionner les éléments avec `grid-row` n'est pas nécessaire dans ce projet puisque nous utilisons Subgrid correctement. Mais il peut s'avérer utile pour des mises en page plus complexes lorsque vous souhaitez un contrôle explicite sur le placement de chaque élément dans la grille.

```css
    img {
      grid-row: 1/2;
    }

    h3 {
      grid-row: 2/3;
    }

    p {
      grid-row: 3/4;
    }

    button {
      grid-row: 4/5;
    }
```

Une fois que `subgrid` est appliqué, nos cartes devraient être parfaitement alignées comme indiqué dans l'image ci-dessous. Cet alignement se produit parce que les éléments enfants de chaque carte (comme les titres, les paragraphes et les boutons) partagent désormais la même structure de grille, héritée du parent. Ils sont "conscients" les uns des autres et ajustent automatiquement leurs positions pour rester synchronisés.

![Une image des cartes de produits alignées à l'aide de subgrid](https://cdn.hashnode.com/res/hashnode/image/upload/v1724182833885/5d985d19-d203-4bd3-a5b2-afbf0f060fa9.png align="center")

Par exemple, même si les titres des berlines et des SUV sont plus courts, la grille garantit que leurs paragraphes et boutons commencent sur les mêmes lignes, maintenant la cohérence sur toutes les cartes. Cela conduit à une mise en page plus propre et plus organisée, où chaque élément est aligné quelles que soient les variations de longueur du contenu.

## Subgrid dans les DevTools du navigateur

Dans n'importe quel navigateur moderne, faites un clic droit sur la page Web du projet et sélectionnez "Inspecter" dans la liste des options. Ou utilisez le raccourci (command + option + I sur Mac ou control + shift + I sur Windows) pour ouvrir l'onglet Éléments des DevTools.

![Une image d'un subgrid inspecté dans les DevTools de Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1724164230096/01861ffd-27a3-4394-bf96-fefcedd890f2.png align="center")

Comme vous pouvez le voir dans l'image ci-dessus, tout comme pour la grille classique, Subgrid a également un badge. Activez-le pour inspecter ou déboguer un Subgrid. Il affiche une superposition montrant les colonnes, les lignes et leurs numéros par-dessus l'élément dans la fenêtre d'affichage.

## Conclusion

Subgrid est un outil précieux pour aligner les mises en page – ce que vous deviez faire manuellement par le passé. Désormais, les grilles imbriquées peuvent hériter de propriétés telles que les lignes et les colonnes de leurs grilles parentes. Cela étend les capacités de CSS Grid pour créer des designs cohérents et parfaitement alignés.

Si vous êtes un jour tenté de créer une boucle sans fin de grilles CSS juste pour obtenir l'alignement parfait d'un design avec du contenu de tailles différentes, utilisez plutôt CSS Subgrid pour rendre votre code plus propre et plus facile à gérer.

Voici quelques ressources utiles :

* [MDN sur CSS Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid)
    
* [Apprendre CSS Subgrid](https://www.youtube.com/watch?v=Yl8hg2FG20Q)
    
* [Web Dev sur CSS Subgrid](https://web.dev/articles/css-subgrid)