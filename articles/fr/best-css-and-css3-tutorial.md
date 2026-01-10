---
title: Les meilleurs tutoriels CSS et CSS3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T00:43:00.000Z'
originalURL: https://freecodecamp.org/news/best-css-and-css3-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f10740569d1a4ca409f.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: Tutorial
  slug: tutorial
seo_title: Les meilleurs tutoriels CSS et CSS3
seo_desc: 'Cascading Style Sheets (CSS)

  CSS is an acronym for Cascading Style Sheets. It was first invented in 1996, and
  is now a standard feature of all major web browsers.

  CSS allows for developers to control how web pages look by “styling” the HTML structure...'
---

### **Feuilles de style en cascade (CSS)**

CSS est l'acronyme de Cascading Style Sheets. Il a été inventé pour la première fois en 1996 et est maintenant une fonctionnalité standard de tous les principaux navigateurs web.

CSS permet aux développeurs de contrôler l'apparence des pages web en "stylisant" la structure HTML de cette page.

Les spécifications CSS sont maintenues par le [World Wide Web Consortium (W3C)](https://www.w3.org/).

Vous pouvez construire des choses assez incroyables en CSS seul, comme ce jeu [Minesweeper en pur CSS](https://codepen.io/bali_balo/pen/BLJONk) (qui n'utilise pas de JavaScript).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFcKk9KxqHAnWa1ECcKDOQ.png)

Un bon point de départ est le programme freeCodeCamp [Introduction à CSS de base](https://learn.freecodecamp.org/responsive-web-design/basic-css).

Une autre suggestion pour les débutants est le guide du W3C [Commencer avec HTML + CSS](https://www.w3.org/Style/Examples/011/firstcss) qui enseigne comment créer une feuille de style.

Le site [CSS Zen Garden](http://www.csszengarden.com/) est un excellent exemple de la manière dont le même HTML peut être stylisé pour avoir un aspect totalement unique.

Pour une démonstration de la puissance de CSS, consultez [Species In Pieces](http://species-in-pieces.com/#).

# Tutoriels pour commencer avec CSS et CSS3

Le meilleur endroit pour commencer à apprendre CSS est avec le [tutoriel d'introduction à CSS de 2 heures de freeCodeCamp](https://www.youtube.com/watch?v=ieTHC78giGQ).

Ensuite, si vous vous sentez plus aventureux, nous avons un [cours complet de 12 heures qui couvre HTML, HTML5 et CSS en détail](https://www.youtube.com/watch?v=mU6anWqZJcc).

![Image](https://img.youtube.com/vi/mU6anWqZJcc/maxresdefault.jpg)

## **Flexbox**

Flexbox est une nouvelle façon de structurer le contenu en CSS3. Il offre une merveilleuse façon de créer des sites web réactifs qui fonctionnent bien sur différentes tailles d'écran et d'ordonner le contenu.

Il y a 3 étapes simples pour utiliser Flexbox :

1. Convertir le conteneur parent en un conteneur flex en utilisant `display: flex;`
2. Ajuster la disposition des différents conteneurs en utilisant `flex-direction`
3. Ajuster la disposition des éléments dans un conteneur en utilisant des propriétés comme `justify-content`, `align-items`, etc.

Flexbox vous permet de disposer, aligner et ajuster efficacement l'espace entre différents éléments de page, même si vous ne connaissez pas leur taille exacte. Au lieu de cela, les éléments et les conteneurs sont dynamiques et vont "s'adapter" pour remplir au mieux l'espace disponible.

* **axe principal** : L'axe principal d'un conteneur flex le long duquel les éléments flex sont disposés. Gardez à l'esprit que cela peut être horizontal ou vertical selon la propriété `flex-direction`.
* **main-start | main-end** : Les éléments flex sont placés dans un conteneur de `main-start` à `main-end`.
* **taille principale** : La dimension principale d'un élément flex, qui peut être sa largeur ou sa hauteur, agit comme la taille principale de l'élément.
* **axe transversal** : L'axe qui est perpendiculaire à l'axe principal. La direction de l'axe transversal dépend de la direction de l'axe principal.
* **cross-start | cross-end** : Les lignes flex et les éléments sont placés dans un conteneur flex en commençant par le côté `cross-start` au côté `cross-end`.
* **taille transversale** : La dimension transversale de l'élément (largeur ou hauteur) agit comme la taille transversale de l'élément.

## **Disposition en grille (Grid Layout)**

CSS Grid Layout, simplement connu sous le nom de Grid, est un schéma de disposition qui est le plus récent et le plus puissant en CSS. Il est [supporté par tous les principaux navigateurs](https://caniuse.com/#feat=css-grid) et offre un moyen de positionner des éléments sur la page et de les déplacer.

Il peut automatiquement assigner des éléments à des _zones_, les redimensionner, prendre en charge la création de colonnes et de lignes basées sur un motif que vous définissez, et il effectue tous les calculs en utilisant la nouvelle unité `fr`.

### **Pourquoi Grid ?**

* Vous pouvez facilement avoir une grille de 12 colonnes avec une ligne de CSS. `grid-template-columns: repeat(12, 1fr)`
* Grid vous permet de déplacer des éléments dans n'importe quelle direction. Contrairement à Flex, où vous pouvez déplacer des éléments soit horizontalement (`flex-direction: row`) soit verticalement (`flex-direction: column`) - et pas les deux en même temps - Grid vous permet de déplacer n'importe quel _élément de grille_ vers n'importe quelle _zone de grille_ prédéfinie sur la page. Les éléments que vous déplacez n'ont pas besoin d'être adjacents.
* Avec CSS Grid, vous pouvez **changer l'ordre des éléments HTML en utilisant uniquement CSS**. Déplacez quelque chose du haut vers la droite, déplacez des éléments qui étaient dans le pied de page vers la barre latérale, etc. Au lieu de déplacer le `<div>` de `<footer>` à `<aside>` dans le HTML, vous pouvez simplement changer son placement avec `grid-area` dans la feuille de style CSS.

### **Grid vs. Flex**

* Flex est unidimensionnel - soit horizontal soit vertical, tandis que Grid est bidimensionnel, ce qui signifie que vous pouvez déplacer des éléments dans les plans horizontal et vertical
* Dans Grid, nous appliquons des styles de disposition au conteneur parent et non aux éléments. Flex, en revanche, cible l'élément flex pour définir des propriétés comme `flex-basis`, `flex-grow` et `flex-shrink`
* Grid et Flex ne sont pas mutuellement exclusifs. Vous pouvez utiliser les deux sur le même projet.

### **Vérification de la compatibilité du navigateur avec `@supports`**

Idéalement, lorsque vous construisez un site, vous le concevriez avec Grid et utiliseriez Flex comme solution de repli. Vous pouvez savoir si votre navigateur supporte grid avec la règle CSS `@support` (aka feature query). Voici un exemple :

```css
.container {
  display: grid; /* afficher la grille par défaut */
}

@supports not (display: grid) { /* si la grille n'est pas supportée par le navigateur */
  .container {
    display: flex; /* afficher flex au lieu de la grille */
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

### **Définition des templates**

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

Voici un exemple de code sur la façon de définir et d'assigner des zones de grille :

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

Grid introduit une nouvelle unité `fr`, qui signifie _fraction_. L'avantage d'utiliser l'unité `fr` est qu'elle prend en charge les calculs pour vous. L'utilisation de `fr` évite les problèmes de marge et de remplissage. Avec `%` et `em`, etc., cela devient une équation mathématique lors du calcul de `grid-gap`. Si vous utilisez l'unité `fr`, elle calculera automatiquement les tailles des colonnes et des gouttières et ajustera la taille des colonnes en conséquence. De plus, il n'y aura pas de décalages de débordement à la fin.

## Exemples

#### **Changer l'ordre des éléments en fonction de la taille de l'écran**

Supposons que vous souhaitiez déplacer le pied de page en bas sur les petits écrans et à droite sur les grands écrans, et qu'il y a un tas d'autres éléments HTML entre les deux.

La solution simple consiste à changer les `grid-template-areas` en fonction de la taille de l'écran. Vous pouvez également **changer le nombre de colonnes et de lignes en fonction de la taille de l'écran**. C'est une alternative beaucoup plus propre et plus simple au système de grille de Bootstrap (`col-xs-8 col-sm-6 col-md-4 col-lg-3`).

```css
.site {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "title title"
    "main header"
    "main sidebar"
}

@media screen and (min-width: 34em) { /* Si l'écran est assez grand, utilisez un template différent pour les zones de grille */
  .site {
    grid-template-columns: 2fr 1fr 1fr;
    grid-template-areas:
      "title title title"
      "main header header"
      "main sidebar footer"
  }
}
```

#### **Plus d'informations :**

* [CSS Grid Playground par Mozilla](https://mozilladevelopers.github.io/playground/) : Excellent point de départ si vous êtes nouveau dans les grilles CSS. Il contient des visuels pour vous aider à comprendre facilement la terminologie
* [YouTube : Morten Rand-Hendriksen : CSS Grid Changes Everything (About Web Layouts)](https://www.youtube.com/watch?v=txZq7Laz7_4) : Cette présentation vous convaincra en moins d'une heure pourquoi les grilles CSS sont cool et pourquoi/comment vous devriez les utiliser.
* [Vidéos : Learn Grid Layout Video Series par Rachel Andrew](https://gridbyexample.com/video/) : Rachel Andrew est une experte en la matière. Les titres des vidéos peuvent sembler étranges et écrasants, mais le contenu est court et précis
* [Livre : Get Ready for CSS Grid Layout par Rachel Andrew](https://abookapart.com/products/get-ready-for-css-grid-layout)

# **Sélecteurs**

Les sélecteurs sont des règles CSS pour cibler des éléments HTML afin d'appliquer des styles. Les noms de balises, les noms de classes, les identifiants et les attributs sont quelques-uns des crochets utilisés comme sélecteurs.

## **Syntaxe des sélecteurs**

Les sélecteurs arrangés dans une séquence spécifique construisent une règle pour cibler des éléments. Un exemple :

```css
/* sélectionne les balises d'ancrage */
a { 
    color: orange;
}

/* sélectionne les éléments avec la classe hero */
.hero {
    text-align: center;
}
```

## **Types de sélecteurs**

* Les sélecteurs de type et les noms de balises sont utilisés pour sélectionner des éléments tels que `h1` ou `a`.
* Les sélecteurs universels s'appliquent à tous les éléments.
* `div *` correspond à tous les éléments dans les éléments div.
* Les sélecteurs d'attributs sont des sélecteurs qui ciblent des éléments en fonction de leurs attributs [et éventuellement de leurs valeurs].
* `h1[title]` sélectionne les éléments `h1` avec l'attribut `title`.
* Les sélecteurs de classe sont des sélecteurs qui ciblent des éléments en utilisant leurs noms de classe.
* Les sélecteurs d'identifiant sont des sélecteurs qui utilisent l'identifiant pour cibler des éléments. `#logo` sélectionne l'élément avec `logo` comme identifiant.
* Les sélecteurs de pseudo-classe sont des sélecteurs spéciaux qui ciblent des éléments en fonction de leur état. Le sélecteur `a:hover` applique un style lorsque le pointeur survole les liens.

## **Combinateurs de sélecteurs**

Combinateur : But `espace blanc` Combinateur de descendant. `.nav li` sélectionne tous les enfants `li` dans la classe `.nav`, y compris les éléments `li` imbriqués. `>` Combinateur d'enfant. `.menu > li` sélectionne tous les li qui sont des enfants directs des éléments avec la classe `.menu`. `+` Combinateur de frère adjacent. `.logo + h1` cible `h1` qui est un frère immédiat de la classe `.logo`. `~` Combinateur de frère général. `header ~ div` cible les éléments `div` qui sont des frères des éléments `header`.

Cette section détaille tous ces sélecteurs.

#### **Plus d'informations :**

Vous pouvez en apprendre plus sur les sélecteurs sur ces ressources :

* [Spécification officielle des sélecteurs CSS3](https://www.w3.org/TR/css3-selectors)
* [Page sur les sélecteurs sur Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)
* [Feuille de triche des sélecteurs CSS sur les guides FreeCodeCamp](https://guide.freecodecamp.org/css/tutorials/css-selectors-cheat-sheet)

Les sélecteurs en CSS (feuilles de style en cascade) sont déterminés en fonction de la _spécificité_. Avec cela, nous pouvons être plus spécifiques sur nos règles de style et remplacer d'autres règles qui peuvent cibler le même élément mais ne sont pas aussi spécifiques.

La façon dont cette hiérarchie de spécificité fonctionne est basée sur le poids. Cela signifie qu'un sélecteur d'élément a un poids de 1 (un), un sélecteur de classe a un poids de 10 (dix) et un sélecteur d'identifiant a un poids de 100 (cent). Nous pouvons combiner différents sélecteurs ensemble pour être plus spécifiques sur l'élément que nous voulons changer.

Par exemple :

```css
    p {
      color: blue;
    }
    p .red {
       color: red;
    }
```

Notre sélecteur de type p sélectionnera tous les éléments p dans notre document html, mais il n'a qu'un poids de un. En revanche, le sélecteur de classe a un poids de 11, car nous combinons un sélecteur de type avec un sélecteur de classe (ce sélecteur correspond à tous les éléments p avec une classe de red).

Note :

* Les règles directement ciblées auront toujours la priorité sur les règles qui héritent des éléments de leurs ancêtres.
* La spécificité n'est appliquée que lorsque plusieurs déclarations ciblent le même élément, et seulement alors cette règle est appliquée.
* La spécificité est généralement la raison pour laquelle certaines des règles de style ne s'appliquent pas aux éléments lorsque vous vous attendez à ce qu'elles le fassent.

## **Affichage CSS**

La propriété display spécifie le type de boîte utilisé pour un élément HTML. Elle a 20 valeurs de mots-clés possibles. Les plus couramment utilisées sont :

```css
    .none             {display: none}
    .block            {display: block}
    .inline-block     {display: inline-block}
    .inline           {display: inline}
    .flex             {display: flex}
    .inline-flex      {display: inline-flex}
    .inline-table     {display: inline-table}
    .table            {display: table}
    .inherit          {display: inherit}
    .initial          {display: initial}
```

La propriété `display:none` peut souvent être utile lors de la création d'un site web réactif. Par exemple, vous pouvez vouloir masquer un élément sur une page lorsque la taille de l'écran diminue afin de compenser le manque d'espace. `display: none` non seulement masquera l'élément, mais tous les autres éléments de la page se comporteront comme si cet élément n'existait pas.

C'est la plus grande différence entre cette propriété et la propriété `visibility: hidden`, qui masque l'élément mais garde tous les autres éléments de la page au même endroit qu'ils apparaîtraient si l'élément masqué était visible.

Ces valeurs de mots-clés sont regroupées en six catégories :

* `<display-inside>`
* `<display-outside>`
* `<display-listitem>`
* `<display-box>`
* `<display-internal>`
* `<display-legacy>`