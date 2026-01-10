---
title: Comment créer une galerie d'images avec CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:50:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2H0HPHmFNs2t78Zog8kd9w.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une galerie d'images avec CSS Grid
seo_desc: 'Image galleries made by websites like Unsplash, Pinterest Etc, are made
  by techniques like positioning or translating the image item which is a very cumbersome
  task to do. You can achieve the same functionality very quickly using CSS Grids.


  For exam...'
---

Les galeries d'**images** créées par des sites comme [Unsplash](https://unsplash.com/), [Pinterest](https://www.pinterest.com/) etc., sont réalisées grâce à des techniques comme le **positionnement** ou la **translation** des éléments images, ce qui est une tâche très fastidieuse. Vous pouvez obtenir la même fonctionnalité très rapidement en utilisant les **CSS Grids**.

> **Par exemple :** Ci-dessus se trouve une galerie d'images avec des images de **largeurs** et **hauteurs variées**, ce qui est un cas d'utilisation parfait pour les grilles CSS.

#### **Commençons !**

### La grille sous-jacente

Maintenant, créons une grille **8x8**. Nous pouvons créer une grille d'autres tailles également, mais cela dépend du type de galerie que vous souhaitez. Dans notre cas, une grille **8x8** sera idéale.

* Un conteneur de grille est défini en réglant la propriété **display** d'un élément sur **grid**. Ainsi, la **div**, avec la **classe grid**, sera notre **conteneur de grille**.
* Nous utilisons la propriété **grid-template-columns** pour définir les **pistes de colonnes** et **grid-template-rows** pour définir les **pistes de lignes**. Nous déclarons ces propriétés sur le conteneur de grille. Dans notre exemple, nous allons créer un conteneur de grille 8x8.
* **grid-gap :** Il définit la taille de l'**écart entre les lignes** **et** **colonnes** dans une mise en page de grille. La valeur de l'écart de grille peut être n'importe quelle unité de longueur CSS. Dans notre exemple, j'ai donné la valeur de **15px** pour rendre notre **grille plus belle**.

**HTML :**

```html
<div class="gallery"></div>
```

**CSS :**

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(8, 5vw);
    grid-gap: 15px;
}
```

> **_Note:_** _La hauteur des lignes est liée à la largeur de la fenêtre, de sorte que les cellules maintiennent parfaitement leur rapport d'aspect. Nous avons **8 lignes** chacune avec une hauteur de **5 unités de largeur de la fenêtre**. J'ai expérimenté avec ces hauteurs et je suis arrivé à la conclusion que **5%** de la **largeur de la fenêtre** est la **taille parfaite** pour la hauteur. Nous faisons cela en définissant la hauteur de la ligne à **5vw (largeur de la fenêtre)**._

![Image](https://cdn-media-1.freecodecamp.org/images/1*ho1ZrgKcjhTl6EfmTbZvEw.png)
_**Grille CSS 8x8 (8 pistes de colonnes et 8 pistes de lignes) avec lignes de grille de 1 à 9 (colonnes et lignes)**_

> **_Note:_** _Tous les **enfants directs** de la **grille** deviennent automatiquement des **éléments de grille**._

### Insertion des éléments de grille

Maintenant, nous allons insérer les éléments de grille à l'intérieur du conteneur de grille :

```html
<div class="gallery">
  <figure class="gallery__item gallery__item--1">
    <img src="img/image-1.jpg" class="gallery__img" alt="Image 1">
  </figure>
  <figure class="gallery__item gallery__item--2">
    <img src="img/image-2.jpg" class="gallery__img" alt="Image 2">
  </figure>
  <figure class="gallery__item gallery__item--3">
    <img src="img/image-3.jpg" class="gallery__img" alt="Image 3">
  </figure>
  <figure class="gallery__item gallery__item--4">
    <img src="img/image-4.jpg" class="gallery__img" alt="Image 4">
  </figure>
  <figure class="gallery__item gallery__item--5">
    <img src="img/image-5.jpg" class="gallery__img" alt="Image 5">
  </figure>
  <figure class="gallery__item gallery__item--6">
    <img src="img/image-6.jpg" class="gallery__img" alt="Image 6">
  </figure>
</div>
```

### Stylisation des images

```css
.gallery__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

Définir la valeur **object-fit** sur **cover** est comme définir la **taille de l'arrière-plan** sur **cover** pour l'**image de fond**. Nous faisons cela pour que l'image puisse remplir la hauteur et la largeur de sa boîte (l'élément de grille), en maintenant son rapport d'aspect.

> **_Note:_** _La propriété object-fit ne fonctionne que si nous définissons les propriétés **width** et **height**._

![Image](https://cdn-media-1.freecodecamp.org/images/1*FBsVH1n06ufBr_WcB_xDDQ.png)

> **_Note:_** _Par défaut, les **éléments de grille** sont disposés selon les **règles de placement automatique de la grille**._

### **Positionnement des éléments de grille**

Avant de commencer à positionner les éléments de grille, nous allons étudier quelques concepts de base.

La **div** de la grille est le **conteneur de grille**, et tous les éléments **enfants directs** sont les **éléments de grille**. Lorsque nous avons défini les pistes de grille avec grid-template-columns et grid-template-rows, **la grille nous a fourni des lignes numérotées appelées lignes de grille** à utiliser pour positionner les éléments. Vous pouvez vous référer à chaque ligne de grille par un index numérique.

Les **colonnes commencent à un**, de **gauche** à **droite** par défaut, et les **lignes** commencent également à un de **haut** en **bas**. Il faut **deux lignes de grille** pour faire une seule colonne ou ligne, une ligne de chaque côté, donc notre grille de **8 colonnes** et **8 lignes** se compose de **9 lignes de colonnes** et **9 lignes de lignes**.

Les lignes verticales **1** et **2** déterminent les points de **début** et de **fin** de la **première colonne**. Les lignes **2** et **3** déterminent la **deuxième colonne** et ainsi de suite. De même, les lignes horizontales **1** et **2** déterminent la position de la **première ligne**, et les lignes **2** et **3** déterminent la deuxième ligne et ainsi de suite. Connaître les concepts ci-dessus vous aidera à comprendre comment nous allons positionner les **éléments (images)** sur notre grille.

Maintenant, nous allons utiliser les **numéros de lignes de grille** pour contrôler la manière dont les éléments sont placés en appliquant des propriétés directement à un élément de grille. Nous pouvons spécifier sur quelle ligne un élément de grille **commence** et **se termine**, et combien de pistes il doit **s'étendre**.

#### **1er élément de grille**

Créons donc une nouvelle règle qui cible le premier élément de grille. Nous allons d'abord utiliser la propriété **grid-column-start** pour indiquer la ligne de grille de colonne où le premier élément de grille commence. La propriété **grid-column-end** indique où le premier élément de grille se termine.

Ainsi, la **valeur** de grid-column-start est un nombre qui indique la ligne de grille au bord gauche d'une colonne. La **valeur** de grid-column-end indique la ligne de grille qui marque le bord droit de la colonne.

Dans l'exemple donné ci-dessous, définir **grid-column-start** à **1** et **grid-column-end** à **3** signifie que l'élément de grille s'étendra du bord gauche de la ligne de grille, **ligne 1** à **ligne 3**, remplissant **2 colonnes**. Nous allons également utiliser les propriétés **grid-row-start** et **grid-row-end** pour indiquer les positions de **début** et de **fin** de l'élément de grille sur les **lignes de grille de lignes** de la même manière que nous l'avons fait pour la colonne.

```css
.gallery__item--1 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 3;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ScnDXtFn-7wffVN62rqg5w.png)
_Placement du premier élément_

> **_Note:_** _Maintenant, nous allons positionner les autres éléments selon les mêmes principes que nous avons appris ci-dessus._

#### **2ème élément de grille**

```css
.gallery__item--2 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 1;
    grid-row-end: 3;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*U-OLT0CdIjjxvaV-4YpjLg.png)
_Placement du deuxième élément_

#### **3ème élément de grille**

```css
.gallery__item--3 {
    grid-column-start: 5;
    grid-column-end: 9;
    grid-row-start: 1;
    grid-row-end: 6;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wEZB6kvCDGquI_PH1yH4gQ.png)
_Placement du troisième élément_

#### **4ème élément de grille**

```css
.gallery__item--4 {
    grid-column-start: 1;
    grid-column-end: 5;
    grid-row-start: 3;
    grid-row-end: 6;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AkEoMuGUJM5oB7q-2SLnxA.png)
_Placement du quatrième élément_

#### **5ème élément de grille**

```css
.gallery__item--5 {
    grid-column-start: 1;
    grid-column-end: 5;
    grid-row-start: 6;
    grid-row-end: 9;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0SA_xLddgWzrV7y0hK8kEQ.png)
_Placement du cinquième élément_

#### **6ème élément de grille**

```css
.gallery__item--6 {
    grid-column-start: 5;
    grid-column-end: 9;
    grid-row-start: 6;
    grid-row-end: 9;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rmUZZ0lsviNcnofEoAnRPw.png)
_Placement du sixième élément_

Vous pouvez trouver le code complet ci-dessous.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300,400,400i|Nunito:300,300i" rel="stylesheet">
        <link rel="stylesheet" href="css/style.css">
        <link rel="shortcut icon" type="image/png" href="img/favicon.png">

        <title>CSS Grids Gallery</title>
    </head>
    <body>
        <div class="container">
            <div class="gallery">
                <figure class="gallery__item gallery__item--1">
                    <img src="img/image-1.jpg" alt="Gallery image 1" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--2">
                    <img src="img/image-2.jpg" alt="Gallery image 2" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--3">
                    <img src="img/image-3.jpg" alt="Gallery image 3" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--4">
                    <img src="img/image-4.jpg" alt="Gallery image 4" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--5">
                    <img src="img/image-5.jpg" alt="Gallery image 5" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--6">
                    <img src="img/image-6.jpg" alt="Gallery image 6" class="gallery__img">
                </figure>
            </div>
        </div>
    </body>
</html>
```

Et le CSS :

```css
*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit; 
}

html {
  box-sizing: border-box;
  font-size: 62.5%; 
}

body {
  font-family: "Nunito", sans-serif;
  color: #333;
  font-weight: 300;
  line-height: 1.6; 
}

.container {
  width: 60%;
  margin: 2rem auto; 
}

.gallery {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-template-rows: repeat(8, 5vw);
  grid-gap: 1.5rem; 
}

.gallery__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block; 
}

.gallery__item--1 {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 3;

  /** Syntaxe alternative **/
  /* grid-column: 1 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--2 {
  grid-column-start: 3;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 3;

  /** Syntaxe alternative **/
  /* grid-column: 3 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--3 {
  grid-column-start: 5;
  grid-column-end: 9;
  grid-row-start: 1;
  grid-row-end: 6;

  /** Syntaxe alternative **/
  /* grid-column: 5 / span 4;
  grid-row: 1 / span 5; */
}

.gallery__item--4 {
  grid-column-start: 1;
  grid-column-end: 5;
  grid-row-start: 3;
  grid-row-end: 6;

  /** Syntaxe alternative **/
  /* grid-column: 1 / span 4;  */
  /* grid-row: 3 / span 3; */
}

.gallery__item--5 {
  grid-column-start: 1;
  grid-column-end: 5;
  grid-row-start: 6;
  grid-row-end: 9;

  /** Syntaxe alternative **/
  /* grid-column: 1 / span 4; */
  /* grid-row: 6 / span 3; */
}

.gallery__item--6 {
  grid-column-start: 5;
  grid-column-end: 9;
  grid-row-start: 6;
  grid-row-end: 9;

  /** Syntaxe alternative **/
  /* grid-column: 5 / span 4; */
  /* grid-row: 6 / span 3; */
}
```

Vous pouvez essayer d'ajouter votre propre CSS pour faire en sorte que cette galerie ait l'apparence que vous souhaitez. Vous pouvez également créer des galeries d'images plus complexes très facilement.

Vous pouvez en apprendre davantage sur les CSS Grids dans le lien ci-dessous.

[**Un guide complet de Grid | CSS-Tricks**](https://css-tricks.com/snippets/css/complete-guide-grid/)
[_CSS Grid Layout est le système de mise en page le plus puissant disponible en CSS. Il s'agit d'un système bidimensionnel, ce qui signifie qu'il peut..._css-tricks.com](https://css-tricks.com/snippets/css/complete-guide-grid/)

J'espère que vous avez trouvé cet article informatif et utile. J'adorerais avoir votre retour !

**Merci d'avoir lu !**