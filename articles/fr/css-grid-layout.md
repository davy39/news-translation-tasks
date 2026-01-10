---
title: CSS Grid Layout
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T18:14:00.000Z'
originalURL: https://freecodecamp.org/news/css-grid-layout
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3c740569d1a4ca36a6.jpg
tags:
- name: CSS Grid
  slug: css-grid
- name: grid layout
  slug: grid-layout
- name: toothbrush
  slug: toothbrush
seo_title: CSS Grid Layout
seo_desc: 'Grid Layout

  CSS Grid Layout, simply known as Grid, is a layout scheme that is the newest and
  the most powerful in CSS. It is supported by all major browsers and provides a way
  to position items on the page and move them around.

  It can automatically a...'
---

## **Mise en page Grid**

CSS Grid Layout, simplement connu sous le nom de Grid, est un schéma de mise en page qui est le plus récent et le plus puissant en CSS. Il est [pris en charge par tous les principaux navigateurs](https://caniuse.com/#feat=css-grid) et offre un moyen de positionner des éléments sur la page et de les déplacer.

Il peut automatiquement assigner des éléments à des _zones_, dimensionner et redimensionner ces éléments, prendre en charge la création de colonnes et de lignes basées sur un motif que vous définissez, et effectuer tous les calculs en utilisant la nouvelle unité `fr`.

### **Pourquoi Grid ?**

* Vous pouvez facilement avoir une grille de 12 colonnes avec une ligne de CSS. `grid-template-columns: repeat(12, 1fr)`
* Grid vous permet de déplacer des éléments dans n'importe quelle direction. Contrairement à Flex, où vous pouvez déplacer des éléments soit horizontalement (`flex-direction: row`) soit verticalement (`flex-direction: column`) - mais pas les deux en même temps, Grid vous permet de déplacer n'importe quel _élément de grille_ vers n'importe quelle _zone de grille_ prédéfinie sur la page. Les éléments que vous déplacez n'ont pas besoin d'être adjacents.
* Avec CSS Grid, vous pouvez **changer l'ordre des éléments HTML en utilisant uniquement CSS**. Déplacez quelque chose du haut vers la droite, déplacez des éléments qui étaient dans le pied de page vers la barre latérale, etc. Au lieu de déplacer le `<div>` de `<footer>` vers `<aside>` dans le HTML, vous pouvez simplement changer son placement avec `grid-area` dans la feuille de style CSS.

### **Grid vs. Flex**

* Flex est unidimensionnel - soit horizontal soit vertical, tandis que Grid est bidimensionnel, ce qui signifie que vous pouvez déplacer des éléments dans les plans horizontal et vertical
* Dans Grid, nous appliquons les styles de mise en page au conteneur parent et non aux éléments. Flex, en revanche, cible l'élément flex pour définir des propriétés comme `flex-basis`, `flex-grow` et `flex-shrink`
* Grid et Flex ne sont pas mutuellement exclusifs. Vous pouvez utiliser les deux sur le même projet.

### **Vérification de la compatibilité du navigateur avec `@supports`**

Idéalement, lorsque vous construisez un site, vous le concevriez avec Grid et utiliseriez Flex comme solution de repli. Vous pouvez savoir si votre navigateur prend en charge grid avec la règle CSS `@support` (aka feature query). Voici un exemple :

```css
.container {
  display: grid; /* afficher la grille par défaut */
}

@supports not (display: grid) { /* si la grille n'est pas prise en charge par le navigateur */
  .container {
    display: flex; /* afficher flex au lieu de grid */
  }
}
```

### **Premiers pas**

Pour faire de n'importe quel élément une grille, vous devez assigner sa propriété `display` à `grid`, comme ceci :

```css
.conatiner {
  display: grid;
}
```

Et c'est tout. Vous venez de faire de votre `.container` une grille. Chaque élément à l'intérieur du `.container` devient automatiquement un élément de grille.

### **Définition des modèles**

Lignes et colonnes

```css
grid-template-columns: 1fr 1fr 1fr 1fr;
grid-template-rows: auto 300px;
```

Zones

```css
grid-template-areas: 
  "a a a a"
  "b c d e"
  "b c d e"
  "f f f f";
```

ou

```css
grid-template-areas:
  "header header header header"
  "nav main main sidebar";
```

### **Zones de grille**

Voici un exemple de code sur la façon de définir et d'assigner des zones de grille

```css
.site {
  display: grid;
  grid-template-areas: /* appliqué au conteneur de grille */
    "head head" /* vous attribuez des cellules à des zones en donnant aux cellules un nom de zone */
    "nav  main" /* le nombre de valeurs dépend du nombre de cellules que vous avez dans la grille */
    "nav  foot";
}

.site > header {
  grid-area: head;
}

.site > nav {
  grid-area: nav;
}

.site > main {
    grid-area: main;
}

.site > footer {
    grid-area: foot;
}
```

### **L'unité `fr`**

Grid introduit une nouvelle unité `fr`, qui signifie _fraction_. Le bon côté de l'utilisation de l'unité `fr` est qu'elle prend en charge les calculs pour vous. L'utilisation de `fr` évite les problèmes de marge et de remplissage. Avec `%` et `em`, etc., cela devient une équation mathématique lors du calcul de `grid-gap`. Si vous utilisez l'unité `fr`, elle calculera automatiquement les tailles des colonnes et des gouttières et ajustera la taille des colonnes en conséquence, et il n'y aura pas de décalages de fin non plus.

### **Exemples**

#### **Changer l'ordre des éléments en fonction de la taille de l'écran**

Supposons que vous souhaitiez déplacer le pied de page en bas sur les petits écrans et à droite sur les grands écrans, et qu'il y a un tas d'autres éléments HTML entre les deux.

La solution simple consiste à changer les `grid-template-areas` en fonction de la taille de l'écran. Vous pouvez également **changer le nombre de colonnes et de lignes en fonction de la taille de l'écran**, aussi. C'est une alternative beaucoup plus propre et plus simple au système de grille de Bootstrap (`col-xs-8 col-sm-6 col-md-4 col-lg-3`).

```css
.site {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "title title"
    "main header"
    "main sidebar"
}

@media screen and (min-width: 34em) { /* Si l'écran est assez grand, utilisez un modèle différent pour les zones de grille */
  .site {
    grid-template-columns: 2fr 1fr 1fr;
    grid-template-areas:
      "title title title"
      "main header header"
      "main sidebar footer"
  }
}
```

Voir le stylo [CSS Grid par exemple - 2 (zones de grille + écart de grille)](https://codepen.io/aamnah/pen/RLVVoE/) par Aamnah Akram ([@aamnah](https://codepen.io/aamnah)) sur [CodePen](https://codepen.io/).