---
title: Comment créer une mise en page Masonry avec HTML et CSS
subtitle: ''
author: Fanny Nyayic
co_authors: []
series: null
date: '2024-06-18T12:22:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-mansory-layout-using-html-and-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/HTML
seo_title: Comment créer une mise en page Masonry avec HTML et CSS
---

CSS-Only-Masonry-Layout.png
étiquettes:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: HTML
  slug: html
seo_title: null
seo_desc: "Une mise en page masonry est une conception basée sur une grille où les éléments sont disposés de manière à minimiser les espaces verticaux entre eux. \n\nun exemple de mise en page masonry\n\nContrairement aux grilles traditionnelles avec des hauteurs de ligne fixes, les mises en page masonry ajustent le positionnement des éléments dynamiquement en fonction de leur hauteur de contenu, créant un arrangement visuellement attrayant et économe en espace."
---

Une mise en page masonry est une conception basée sur une grille où les éléments sont disposés de manière à minimiser les espaces verticaux entre eux.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/masonry-layout.png)
_un exemple de mise en page masonry_

Contrairement aux grilles traditionnelles avec des hauteurs de ligne fixes, les mises en page masonry ajustent le positionnement des éléments dynamiquement en fonction de leur hauteur de contenu, créant un arrangement visuellement attrayant et économe en espace.

## Caractéristiques clés des mises en page Masonry

* Les éléments peuvent avoir des hauteurs variables, ce qui rend la mise en page plus organique et moins uniforme par rapport aux grilles standard.
* Les éléments sont positionnés pour remplir les espaces verticaux, créant une mise en page étroitement compacte sans grands espaces entre les éléments.
* Les mises en page masonry peuvent s'adapter à différentes tailles d'écran, ajustant le nombre de colonnes et le positionnement des éléments en conséquence.
* La mise en page est souvent utilisée pour les galeries, les portfolios et d'autres contenus visuels où une présentation esthétiquement plaisante est importante.

### Utilisations courantes

* Galeries d'images : Afficher des images de différentes tailles sans rognage.
* Mises en page de blogs : Disposer des articles de longueurs variables.
* Sites de commerce électronique : Présenter des produits avec différentes dimensions.

### Comment cela fonctionne

Les mises en page masonry sont souvent implémentées en utilisant CSS Grid ou des bibliothèques JavaScript comme Masonry.js. Ici, nous nous concentrerons sur l'approche CSS Grid.

## Comment créer une mise en page Masonry

### Étape 1 : Configurer votre projet

* Créez un dossier de projet : Créez un dossier pour votre projet sur votre ordinateur.
* Créez des fichiers HTML et CSS : À l'intérieur du dossier de projet, créez deux fichiers : `index.html` et `styles.css`.

```folder
Masonry/
├── index.html
└── styles.css

```

### Étape 2 : Écrire le HTML

* Utilisez un éditeur de texte comme Visual Studio Code, Sublime Text, ou tout autre éditeur que vous préférez.
* Ajoutez la structure de base d'un document HTML en appuyant sur `Shift+!`
* Changez le titre de Document à "CSS Masonry Layout"
* Sous le titre, liez votre fichier `styles.css` comme montré ci-dessous :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Masonry Layout</title>
    /** Lier styles.css **/
        <link rel="stylesheet" href="styles.css">
</head>
<body>
    
</body>
</html>

```

* Après avoir configuré votre structure HTML, créez les différentes divisions pour votre mise en page dans la zone du corps.

```html
<div class="masonry">
    <div class="item item1">Item 1</div>
    <div class="item item2">Item 2</div>
    <div class="item item3">Item 3</div>
    <div class="item item4">Item 4</div>
    <div class="item item5">Item 5</div>
    <div class="item item6">Item 6</div>
    <div class="item item7">Item 7</div>
    <div class="item item8">Item 8</div>
    <div class="item item9">Item 9</div>
    <div class="item item10">Item 10</div>
</div>
```

* `<div class="masonry">` est le conteneur pour notre mise en page masonry. Nous utiliserons CSS Grid pour créer l'effet masonry à l'intérieur de ce conteneur.
* `<div class="item item1">Item 1</div>` à `<div class="item item10">Item 10</div>` sont les éléments individuels (ou boîtes) à l'intérieur de notre mise en page masonry. Chaque élément a une classe `item` pour les styliser uniformément et une classe spécifique (par exemple : `item1`, `item2`, etc.) pour appliquer des styles uniques—comme différentes hauteurs et couleurs—à chaque élément.

Découpage des classes CSS :

* `item` : Cette classe est utilisée pour styliser tous les éléments uniformément. Elle définit la couleur de fond, le remplissage, le box-sizing, l'ombre de la boîte, le rayon de la bordure et les transitions pour les éléments.
* `item1` à `item10` : Ces classes sont utilisées pour définir des styles spécifiques pour chaque élément. Par exemple, `item1` peut avoir une hauteur et une couleur de fond différentes de `item2`, et ainsi de suite. Ces classes seront utilisées dans le CSS pour appliquer des styles spécifiques.

#### Étape 3 : Styliser avec CSS

* Ouvrez `styles.css` dans un éditeur de texte : Utilisez le même éditeur de texte pour ouvrir votre fichier CSS.
* Ajoutez quelques styles de base pour le `body` et le conteneur `masonry`.

```css
 body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        padding: 20px;
        margin: 0;
    }
    .masonry {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        grid-auto-rows: 10px;
        gap: 20px;
    }
```

Ce que cela signifie :

* `body` définit la police, la couleur de fond, le remplissage et supprime la marge par défaut.
* `.masonry` utilise CSS Grid pour créer une mise en page réactive avec des colonnes d'au moins `200px` de large et remplit automatiquement l'espace disponible. Les lignes ont une hauteur de base de `10px`, et il y a un espace de `20px` entre les éléments.

Ajoutez des styles pour les éléments à l'intérieur de la mise en page masonry.

```css
 .item {
        background-color: #ffffff;
        padding: 20px;
        box-sizing: border-box;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        transition: transform 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2em;
        color: #fff;
    }
    .item:hover {
        transform: translateY(-10px);
    }
```

Ce que cela signifie :

* `.item` définit un fond blanc, un remplissage, une ombre de boîte pour l'élévation, des coins arrondis et un effet de survol pour soulever légèrement l'élément. `display: flex` centre le contenu.
* `.item:hover` ajoutera un effet de transformation lorsque l'élément est survolé.

Définissez des dimensions et des couleurs spécifiques en définissant des styles spécifiques pour chaque élément afin de leur donner des hauteurs et des couleurs de fond différentes.

```css
.item1 { grid-row: span 15; background-color: #ff6f61; }
.item2 { grid-row: span 20; background-color: #6b5b95; }
.item3 { grid-row: span 10; background-color: #88b04b; }
.item4 { grid-row: span 25; background-color: #d65076; }
.item5 { grid-row: span 30; background-color: #ffb347; }
.item6 { grid-row: span 15; background-color: #45b8ac; }
.item7 { grid-row: span 20; background-color: #e94b3c; }
.item8 { grid-row: span 10; background-color: #6c5b7b; }
.item9 { grid-row: span 25; background-color: #00a86b; }
.item10 { grid-row: span 30; background-color: #b565a7;}
```

* Chaque classe d'élément (.item1, .item2, etc.) définit le nombre de lignes qu'elle couvre (grid-row: span X;) et attribue une couleur de fond unique.

### Étape 4 : Visualiser votre mise en page

Ouvrez `index.html` dans un navigateur web pour voir la mise en page masonry.

Vous pouvez ajouter plus d'éléments, changer les couleurs ou ajuster les tailles pour répondre à vos besoins de conception. Voici la mise en page que nous avons créée.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/masonry-layout-1.png)

### Tout mettre ensemble

Le fichier `index.html` devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Masonry Layout</title>
        <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="masonry">
        <div class="item item1">Item 1</div>
        <div class="item item2">Item 2</div>
        <div class="item item3">Item 3</div>
        <div class="item item4">Item 4</div>
        <div class="item item5">Item 5</div>
        <div class="item item6">Item 6</div>
        <div class="item item7">Item 7</div>
        <div class="item item8">Item 8</div>
        <div class="item item9">Item 9</div>
        <div class="item item10">Item 10</div>
    </div>
</body>
</html>
```

Le fichier `styles.css` ressemblera à ceci :

```css
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        padding: 20px;
        margin: 0;
    }
    .masonry {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        grid-auto-rows: 10px;
        gap: 20px;
    }

    .item {
        background-color: #ffffff;
        padding: 20px;
        box-sizing: border-box;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        transition: transform 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2em;
        color: #fff;
    }

    .item:hover {
        transform: translateY(-10px);
    }

    /* Dimensions et couleurs spécifiques pour chaque élément */
    .item1 { grid-row: span 15; background-color: #ff6f61; }
    .item2 { grid-row: span 20; background-color: #6b5b95; }
    .item3 { grid-row: span 10; background-color: #88b04b; }
    .item4 { grid-row: span 25; background-color: #d65076; }
    .item5 { grid-row: span 30; background-color: #ffb347; }
    .item6 { grid-row: span 15; background-color: #45b8ac; }
    .item7 { grid-row: span 20; background-color: #e94b3c; }
    .item8 { grid-row: span 10; background-color: #6c5b7b; }
    .item9 { grid-row: span 25; background-color: #00a86b; }
    .item10 { grid-row: span 30; background-color: #b565a7; }
```

## Résumé

Une mise en page masonry est un moyen efficace d'afficher du contenu avec des hauteurs variables dans une structure de type grille sans grands espaces verticaux, ce qui la rend idéale pour les galeries d'images, les blogs et les portfolios.

En utilisant CSS Grid, vous pouvez créer une mise en page masonry réactive et visuellement attrayante avec un code minimal.