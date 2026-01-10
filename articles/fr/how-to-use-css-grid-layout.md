---
title: Comment utiliser la mise en page CSS Grid – Explication des propriétés de la
  grille avec des exemples
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-05-25T15:32:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-grid-layout
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/CSS-GRID-3.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: Web Design
  slug: web-design
seo_title: Comment utiliser la mise en page CSS Grid – Explication des propriétés
  de la grille avec des exemples
seo_desc: 'Have you ever had a problem positioning items on your web browser? Perhaps
  every time you try to think of a solution, you become tired and give up.

  If so, stay tuned as I reveal a new method for resolving these kinds of problems
  with minimal or no st...'
---

Avez-vous déjà eu des problèmes pour positionner des éléments sur votre navigateur web ? Peut-être que chaque fois que vous essayez de penser à une solution, vous vous sentez fatigué et abandonnez.

Si c'est le cas, restez à l'écoute car je vais vous révéler une nouvelle méthode pour résoudre ces types de problèmes avec un minimum de stress ou sans stress du tout.

Bienvenue à tous. Dans ce tutoriel, nous allons voir comment utiliser la mise en page CSS Grid.

Tout d'abord, nous allons apprendre ce qu'est CSS Grid et à quoi il sert. Ensuite, nous passerons en revue les fonctionnalités de CSS Grid, les raisons pour lesquelles nous devrions l'étudier et les avantages qu'il apporte à nos projets. Enfin, nous discuterons du moment où il est préférable de l'utiliser.

## Qu'est-ce que CSS Grid ?

Alors, qu'est-ce que CSS Grid ?

CSS Grid est une mise en page bidimensionnelle que vous pouvez utiliser pour créer des éléments réactifs sur le web. Les éléments de la grille sont disposés en colonnes, et vous pouvez facilement positionner les lignes sans avoir à manipuler le code HTML.

Voici une définition concise de la mise en page CSS Grid :

> CSS Grid est un outil puissant qui permet de créer des mises en page bidimensionnelles pour les colonnes et les lignes sur le web. ([Source](https://learncssgrid.com/))

## Fonctionnalités de la mise en page CSS Grid

### Tailles de pistes flexibles

Vous pouvez utiliser l'unité `fr` (Fraction Unit) pour attribuer une valeur de pixel spécifiée à la grille. Cela rendra votre grille organisée et réactive.

### Positionnement des éléments

CSS Grid a grandement simplifié le positionnement des éléments dans le conteneur, où que vous souhaitiez les placer, sans avoir à manipuler le balisage HTML.

### Contrôles d'alignement

L'alignement d'un élément dans un conteneur est plus facile que jamais avec CSS Grid. Dans le conteneur, vous pouvez maintenant disposer les éléments horizontalement et verticalement comme vous le souhaitez.

## Avantages de CSS Grid

CSS Grid est très flexible et réactif. Il facilite la création de mises en page bidimensionnelles. CSS Grid est également facile à utiliser et est pris en charge par la plupart des navigateurs web.

CSS Grid rend votre balisage plus propre (dans votre code HTML) et vous offre beaucoup plus de flexibilité. Cela est en partie dû au fait que vous n'avez pas à changer le balisage (code HTML) pour changer la position d'un élément en utilisant CSS Grid.

En résumé, la mise en page CSS Grid nous aide à construire des mises en page plus complexes en utilisant à la fois des colonnes et des lignes.

## Quand utiliser CSS Grid

Bien que vous puissiez utiliser CSS Grid dans pratiquement tous les aspects du développement web, il existe certaines situations où il est idéal.

Par exemple, lorsque nous avons une mise en page de conception complexe à implémenter, CSS Grid est meilleur que la propriété CSS float. Cela est dû au fait que Grid est une mise en page bidimensionnelle (avec des colonnes **et** des lignes), tandis que la propriété CSS float est une mise en page unidimensionnelle (avec des colonnes **ou** des lignes).

Grid est également un bon choix lorsque nous avons besoin d'un espace ou d'un écart entre les éléments. En utilisant la propriété `gap` de CSS Grid, l'espacement de deux éléments est beaucoup plus facile qu'en utilisant les propriétés CSS `margin` et `padding`, qui pourraient compliquer les choses.

## Propriétés de CSS Grid

La mise en page CSS Grid se compose de nombreuses propriétés de grille. Maintenant, nous allons examiner certaines d'entre elles afin d'apprendre à les utiliser.

### Propriété du conteneur de grille

Il s'agit d'une propriété CSS Grid qui contient les éléments de la grille. Nous implémentons la propriété du conteneur de grille CSS en définissant le conteneur avec une propriété `display` de `grid` ou `in-line grid`.

Par exemple :

```css
display: grid;
```

ou

```css
display: inline-grid;
```

### Propriété grid-template-column

Il s'agit d'une propriété utilisée pour définir la largeur de chaque colonne. Elle peut également définir le nombre de colonnes que vous souhaitez définir pour votre projet.

Vous pouvez implémenter la propriété de colonne de grille CSS en utilisant `grid-template-column`.

Par exemple :

```css
grid-template-columns: 100px auto 100px;
```

Le code ci-dessus montre que nous avons trois colonnes. La largeur des colonnes un (la première colonne) et trois (la troisième colonne) est définie à `100px`. La largeur de la colonne deux (la colonne du milieu) est définie à `auto`.

Cela signifie que lorsque la taille de votre écran augmente, les colonnes un et trois prennent `100px` de la largeur de l'écran, tandis que la colonne deux prend la largeur restante de l'écran (qui est `auto`).

### Propriété grid-template-row

Vous utilisez la propriété de ligne CSS pour définir la hauteur de chaque colonne. Vous pouvez également l'utiliser pour définir le nombre de lignes que vous souhaitez définir dans votre projet.

Vous pouvez implémenter la propriété de ligne de grille CSS en utilisant `grid-template-row`, comme ceci :

```css
grid-template-rows: 50px 50px;
```

Le code ci-dessus montre que nous avons un total de deux lignes et que ces deux lignes font `50px` de haut.

Notez que nous pouvons également attribuer la propriété de colonne et de ligne à notre code HTML en une seule fois en utilisant simplement `grid-template`. `Grid-template` est une autre façon de représenter `grid-template-columns` et `grid-template-rows`.

Par exemple :

```css
grid-template: 50px 50px / 100px auto 100px;
```

Le code ci-dessus vous donnera le même résultat que `grid-template-columns` et `grid-template-rows`.

Pour utiliser la propriété `grid-template`, vous devrez attribuer la valeur à la ligne d'abord avant d'attribuer la valeur de la colonne, comme dans le code ci-dessus. Le `50px 50px` est pour la ligne tandis que `100px auto 100px` est pour la colonne.

Une façon de s'en souvenir est de penser à la lettre L :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-90.png align="left")

*grid-template*

Essayez cela et voyez par vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CSS-GRID-2.png align="left")

*Une grille avec une colonne de 100px auto 100px et une ligne de 50px 50px*

### Propriété column-gap

Comme son nom l'indique, il s'agit d'une propriété de grille qui attribue un espace entre deux colonnes ou plus dans un conteneur. Vous pouvez le faire en utilisant la propriété `column-gap` et en lui donnant une valeur. Par exemple :

```css
column-gap: 20px;
```

D'après le code ci-dessus, vous pouvez voir qu'un écart de `20px` a été attribué à la colonne.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/COLUMN-GAP-1.png align="left")

*20px column-gap*

### Propriété row-gap

Tout comme `column-gap`, `row-gap` est une propriété CSS qui attribue un espace entre deux lignes ou plus dans un conteneur. Par exemple :

```css
row-gap: 50px;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ROW-GAP-1.png align="left")

*row-gap: 50px;*

Notez que nous pouvons également attribuer un écart à la fois aux colonnes et aux lignes d'un conteneur en utilisant la propriété `gap`. Pour que cela fonctionne, nous n'attribuons qu'une seule valeur à la fois aux colonnes et aux lignes du conteneur, comme nous l'avons fait dans le code ci-dessus.

Voici un exemple :

```css
gap: 20px;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/GAP-1.png align="left")

*gap: 20px*

D'après le diagramme ci-dessus, nous pouvons voir qu'un `gap` de `20px` a été défini pour les colonnes et les lignes du conteneur, les rendant également espacés.

### Propriété justify-content

Il s'agit d'une propriété de grille que vous utilisez pour positionner les éléments (colonnes et lignes) horizontalement dans un conteneur. Elle montre comment le navigateur web positionne les espaces autour des éléments (colonnes et lignes).

La propriété justify-content a six valeurs possibles :

* `start`

* `end`

* `center`

* `space-around`

* `space-between`

* `space-evenly`

#### Start

Cela positionne les éléments sur le côté gauche du navigateur et peut être exécuté avec le code suivant :

```css
justify-content: start;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-START-1.png align="left")

*justify-content: start;*

#### End

Cela positionne les éléments sur le côté droit du navigateur et peut être exécuté avec le code suivant :

```css
justify-content: end;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-END-1.png align="left")

*justify-content: end;*

#### Center

Cela positionne les éléments au centre du navigateur et peut être exécuté avec le code suivant :

```css
justify-content: center;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-CENTER-1.png align="left")

*justify-content: center;*

#### Space-around

Cette propriété distribue les éléments dans le conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au conteneur suivant.

Ce code peut être exécuté comme ceci :

```css
justify-content: space-around;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-SPACE-AROUND-1.png align="left")

*justify-content: space-around*

#### Space-between

Tout comme la propriété `space-around`, `space-between` distribue les éléments dans le conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au suivant dans le conteneur. Il occupe toute la largeur du conteneur.

Ce code peut être exécuté comme ceci :

```css
justify-content: space-between;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-SPACE-BETWEEN-1.png align="left")

*justify-content: space-between*

#### Space-evenly

Comme son nom l'indique, cette propriété distribue les éléments dans le conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au suivant dans le conteneur.

Ce code peut être exécuté comme ceci :

```css
justify-content: space-evenly;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/JUSTIFY-SPACE-EVENLY-1.png align="left")

*justify-content: space-evenly;*

Notez que toutes les propriétés `justify-content` positionnent leurs éléments horizontalement. Essayez de le faire vous-même pour mieux le comprendre.

### Propriété align-content

`Align-content` est l'opposé de `justify-content`. Vous utilisez la propriété `align-content` pour positionner les éléments verticalement dans un conteneur.

Tout comme `justify-content`, la propriété `align-content` a six valeurs possibles :

* `start`

* `end`

* `center`

* `space-around`

* `space-between`

* `space-evenly`

#### Start

Cela positionne les éléments en haut du navigateur et peut être exécuté avec le code suivant :

```css
align-content: start;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-START-1.png align="left")

*align-content: start;*

#### End

Cela positionne les éléments en bas du navigateur et peut être exécuté avec le code suivant :

```css
align-content: end;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-END-1.png align="left")

*align-content: end*

#### Center

Cela positionne les éléments au centre du navigateur et peut être exécuté avec le code suivant :

```css
align-content: center;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-CENTER-1.png align="left")

*align-content: center;*

#### Space-around

Cette propriété distribue les éléments le long du côté du conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au suivant verticalement.

Ce code peut être exécuté comme ceci :

```css
align-content: space-around;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-SPACE-AROUND-1.png align="left")

*align-content: space-around*

#### Space-between

Tout comme la propriété `space-around`, `space-between` distribue les éléments dans le conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au suivant dans le conteneur, et occupe toute la largeur du conteneur dans la direction verticale.

Ce code peut être exécuté comme ceci :

```css
align-content: space-between;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-SPACE-BETWEEN-2.png align="left")

*align-content: space-between*

#### Space-evenly

Comme son nom l'indique, cette propriété distribue les éléments dans le conteneur de manière uniforme, où chaque élément dans le conteneur a une quantité égale d'espace par rapport au suivant verticalement.

Ce code peut être exécuté comme ceci :

```css
align-content: space-evenly;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ALIGN-CONTENT-SPACE-EVENLY-2.png align="left")

*align-content: space-evenly*

## Conclusion

Dans l'article d'aujourd'hui, nous avons étudié ce qu'est la mise en page CSS Grid, pourquoi nous devrions l'apprendre et les propriétés de CSS Grid.

Merci d'avoir lu.

Amusez-vous bien en codant !