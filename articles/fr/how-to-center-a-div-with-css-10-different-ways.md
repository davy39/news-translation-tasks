---
title: Comment centrer une div avec CSS – 10 méthodes différentes
subtitle: ''
author: Soham De Roy
co_authors: []
series: null
date: '2022-07-20T22:08:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-a-div-with-css-10-different-ways
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Group-49.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment centrer une div avec CSS – 10 méthodes différentes
seo_desc: "As a web developer, sometimes centering a div feels like one of the toughest\
  \ jobs on planet Earth. \nWell, not anymore. In this article, you'll learn 10 different\
  \ ways to center a div. We will explore how to center divs using the CSS position\
  \ property..."
---

En tant que développeur web, parfois **centrer une div** semble être l'une des tâches les plus difficiles sur Terre. 

Eh bien, ce n'est plus le cas. Dans cet article, vous apprendrez 10 méthodes différentes pour centrer une `div`. Nous explorerons comment centrer des divs en utilisant la propriété CSS **position**, CSS **Flexbox** et CSS **Grid**. 

Après avoir lu cet article, je suis convaincu que vous commencerez à centrer des `divs` comme un pro.

## Comment centrer une `div`

Pour ce tutoriel, j'utiliserai le même HTML pour les 10 méthodes que nous allons discuter ci-dessous. Le HTML contient simplement une `div` parent et une `div` enfant à l'intérieur. 

L'objectif principal de cet article est de centrer la `div` interne par rapport à son parent. Je ne modifierai que les fichiers CSS, mais vous pourrez voir les 10 méthodes différentes prendre effet.

Le fichier HTML principal est le suivant :

```HTML
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Centrer des divs</title>
    <link rel="stylesheet" href="./basicStyle.css" />
    <!-- Changez le lien du fichier CSS ici -->
    <link rel="stylesheet" href="" />
    <style>
      * {
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
      }
    </style>
  </head>
  <body>
    <div id="parentContainer">
      <div id="childContainer"></div>
    </div>
  </body>
</html>
```

Avec simplement le style de base donné dans les lignes suivantes :

```CSS
#parentContainer {
  width: 400px;
  height: 400px;
  background-color: #f55353;
}
#childContainer {
  width: 100px;
  height: 100px;
  background-color: #feb139;
}
```

Nous obtiendrons quelque chose comme ceci :


![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-05-27-at-15.02.59.png)
_Ce que le HTML et le CSS de base nous donnent._

Nous créons simplement une `div` parent et lui donnons une `width` et une `height` de `400px`, et une `color` de `#f55353`. 

De même, nous créons une `div` enfant à l'intérieur et lui donnons une `width` et une `height` de `100px` et lui donnons une `color` de `#feb139`.

L'objectif final de cet article sera de réaliser cette transformation :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Group-23.png)

## Comment centrer une div en utilisant la propriété CSS `position`

### 1. Comment utiliser position: relative, absolute et les valeurs de décalage top, left

```css
#parentContainer {
  position: relative;
}
#childContainer {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

La propriété **position** en CSS définit comment l'élément est positionné sur la page. La valeur par défaut de la propriété position est `static`. Les autres valeurs que la propriété position peut prendre sont `relative`, `absolute`, `fixed` et `sticky`. 

Maintenant, lorsque nous donnons un `position: absolute` à un élément DOM, il **devient absolu par rapport à toute la page**. Cela serait utile si nous voulions centrer la `div` par rapport à toute la page. 

D'autre part, définir l'élément parent sur `position: relative` rend l'élément enfant (avec `position: absolute`) **absolu, relatif à l'élément parent et non à toute la page**. 

Dans l'exemple ci-dessus, nous faisons exactement cela. Nous donnons à l'élément parent un `position: relative` et à l'enfant un `position: absolute`. 

Avec la propriété position, nous pouvons spécifier quatre autres propriétés à savoir `top`, `right`, `bottom` et `left` qui déterminent ensuite l'emplacement final/position de l'élément. 

Les propriétés `top` et `bottom` spécifient le **positionnement vertical** de l'élément tandis que `left` et `right` spécifient le **positionnement horizontal**. 

### 2. Comment utiliser position: relative et absolute, les valeurs de décalage top, left, right et bottom et margin: auto

```css
#parentContainer {
  position: relative;
}
#childContainer {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
}

```

En continuant avec nos connaissances sur les positions du point 1 ci-dessus, nous utilisons la propriété `margin` en CSS ici. `margin: auto` permet au navigateur de sélectionner une **marge appropriée** pour l'élément enfant. 

Dans la plupart des cas, cela permet à l'élément enfant de prendre sa largeur spécifiée et le navigateur **distribue l'espace restant de manière égale** entre les paires de marges gauche et droite ou haut et bas ou parmi les deux paires. 

Si nous mentionnons uniquement `top: 0`, `bottom: 0` et `margin: auto`, cela centre l'élément enfant **verticalement**. 

De même, si nous mentionnons uniquement `left: 0`, `right: 0` et `margin: auto`, alors cela centra l'enfant **horizontalement**. 

Et si nous mentionnons toutes les propriétés comme montré dans le bloc de code ci-dessus, alors nous obtenons une `div` parfaitement **centrée à la fois horizontalement et verticalement**.

## Comment centrer une div en utilisant CSS Flexbox

### 3. Comment utiliser Flexbox, justify-content et align-item

Les deux méthodes ci-dessus sont basées sur une méthode plus classique d'alignement des éléments dans la page. Les approches modernes utilisent **Flexbox** (pour la modélisation de mise en page unidirectionnelle) et les propriétés de mise en page **Grid** (pour la modélisation de mise en page bidimensionnelle plus complexe). 

Voyons l'approche Flexbox :

Flexbox n'est pas seulement une seule propriété, mais c'est un module qui comprend un ensemble de propriétés. Certaines de ces propriétés sont destinées au **conteneur** (c'est-à-dire le conteneur parent) et certaines pour les **éléments enfants** à l'intérieur.

Le diagramme ci-dessous montre une liste de propriétés destinées aux éléments parents et enfants par rapport à Flexbox.
![Group-42](https://www.freecodecamp.org/news/content/images/2022/07/Group-42.png)

Il n'est pas possible de couvrir toutes les propriétés dans cet article. Plutôt, regardons certaines des propriétés que nous utilisons dans cet article.

Comme mentionné ci-dessus, il y a deux entités différentes dans le modèle Flexbox, le conteneur parent et l'élément enfant. 

La propriété `display: flex` définit un conteneur comme un conteneur flex. `flex-direction` est une autre propriété du conteneur parent qui peut prendre l'une des quatre valeurs `row` (valeur par défaut), `row-reverse`, `column` et `column-reverse`. 

Lors de l'utilisation de Flexbox, nous devons prendre en compte deux axes différents, à savoir l'**axe principal** et l'**axe transversal**. 

Pour les cas où `flex-direction` est `row` ou `row-reverse`, l'**axe horizontal est l'axe principal et l'axe vertical est l'axe transversal**. 

De même, lorsque `flex-direction` est `column` ou `column-reverse`, alors l'**axe vertical est l'axe principal et l'axe horizontal est l'axe transversal**. Reportez-vous aux diagrammes ci-dessous pour plus de clarté visuelle :

![Group-43](https://www.freecodecamp.org/news/content/images/2022/07/Group-43.png)

![Group-44](https://www.freecodecamp.org/news/content/images/2022/07/Group-44.png)

La propriété `justify-content` du conteneur parent définit l'alignement de ses enfants le long de l'axe principal. Ainsi, `justify-content: center` définit l'alignement de tous ses éléments enfants au centre par rapport à l'axe principal.

De même, la propriété `align-items` du conteneur parent définit l'alignement de ses enfants le long de l'axe transversal. Ainsi, `align-items: center` définit l'alignement de tous ses éléments enfants au centre par rapport à l'axe transversal.

Ainsi, le bloc de code ci-dessous alignera parfaitement notre élément enfant au centre de l'élément parent, à la fois verticalement et horizontalement. 

Dans cette méthode, nous n'avons pas besoin de spécifier quoi que ce soit explicitement pour l'élément enfant. `display: flex`, `justify-content` et `align-items` gèrent tout depuis le composant parent.

```css
#parentContainer {
  display: flex;
  justify-content: center;
  align-items: center;
}

```

### 4. Comment utiliser Flexbox, justify-content et align-self

Cette méthode est simplement une alternative à la méthode ci-dessus et lui est assez similaire.

Mais au lieu d'utiliser la propriété `align-items` (dans la propriété du conteneur parent), qui définit l'alignement pour **tous les éléments enfants** par rapport à l'axe transversal, nous utilisons `align-self` (dans les éléments enfants) qui définit l'alignement des **éléments flex individuels** sur l'axe transversal.

```css
#parentContainer {
  display: flex;
  justify-content: center;
}
#childContainer {
  align-self: center;
}

```

### 5. Comment utiliser Flexbox et margin: auto

Flexbox nous donne des capacités très puissantes d'alignement et de distribution d'espace. De plus, comme mentionné ci-dessus, `margin: auto` permet au navigateur de sélectionner une marge appropriée pour l'élément enfant. 

Dans la plupart des cas, cela permet à l'élément enfant de prendre sa largeur spécifiée et le navigateur distribue l'espace restant de manière égale entre les paires de marges gauche et droite ou haut et bas ou parmi les deux paires. 

Cela signifie que définir le conteneur parent comme `flex` et donner à l'enfant un `margin: auto` permet au navigateur de distribuer uniformément l'espace restant le long des directions verticale et horizontale.

```css
#parentContainer {
  display: flex;
}
#childContainer {
  margin: auto;
}

```

## Comment centrer une div en utilisant CSS Grid

### 6. Comment utiliser Grid, justify-content et align-items

CSS Grid, ou simplement Grid, est utilisé pour la modélisation de mise en page **bidimensionnelle** par rapport à Flexbox que vous utilisez pour la modélisation **unidimensionnelle**. 

Similaire à Flexbox, nous avons le concept de conteneur de grille ou conteneur parent et d'éléments de grille ou éléments enfants. 

Le diagramme ci-dessous liste toutes les propriétés que vous pouvez utiliser pour le parent et les enfants. Comme CSS Grid est un sujet vaste en soi, il n'est pas dans le cadre de cet article de discuter de chaque propriété. Donc, discutons des propriétés que nous utilisons dans cet article.

![Group-45](https://www.freecodecamp.org/news/content/images/2022/07/Group-45.png)

`display: grid` initie un élément à devenir un conteneur de grille.

`justify-items` et `align-items` alignent les éléments à l'intérieur de la grille le long de l'axe en ligne (ligne) et de l'axe de bloc (colonne) respectivement.

D'autre part, si la taille totale de la grille est inférieure au conteneur de grille (ce qui peut se produire si tous les éléments de grille sont dimensionnés avec des unités non flexibles comme px), alors dans ce cas, nous pouvons contrôler l'alignement de la grille dans le conteneur de grille en utilisant `justify-content` et `align-content`.

`justify-content` et `align-content` alignent la grille le long de l'axe en ligne (ligne) et de l'axe de bloc (colonne) respectivement.

Vous pouvez trouver une explication complète de toutes ces propriétés ici : [Un guide complet sur Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

Pour notre cas, il n'y a qu'une seule **cellule de grille** et un seul élément enfant à l'intérieur, donc nous pouvons utiliser `justify-content` ou `justify-items` ainsi que `align-content` ou `align-items` de manière interchangeable et obtenir le même résultat.

```css
#parentContainer {
  display: grid;
  justify-content: center;
  align-items: center;
}
```

### 7. Comment utiliser Grid et place-items

Vous pouvez utiliser `place-items` pour définir les propriétés `align-items` et `justify-items` dans la même déclaration. De même, `place-content` définit à la fois `justify-content` et `align-content` dans la même déclaration.

Comme mentionné ci-dessus, dans ce cas d'utilisation, nous pouvons utiliser `justify-content` ou `justify-items` ainsi que `align-content` ou `align-items` de manière interchangeable. De la même manière, nous pouvons également utiliser `place-items` ainsi que `place-content` de manière interchangeable et obtenir le même résultat (spécifiquement pour ce cas d'utilisation. Pour tout autre cas d'utilisation, nous devons analyser quelle propriété doit être utilisée).

```CSS
#parentContainer {
  display: grid;
  place-items: center;
}
```

### 8. Comment utiliser Grid, align-self et justify-self

Similaire à Flexbox, Grid prend également en charge l'alignement individuel des éléments de grille en utilisant les propriétés `align-self` et `justify-self` (propriétés à spécifier dans l'élément enfant). 

`justify-self` aligne les éléments de grille à l'intérieur d'une cellule de grille le long de l'axe en ligne (ligne) tandis que `align-self` aligne les éléments de grille à l'intérieur de la cellule de grille le long de l'axe de bloc (colonne).

```css
#parentContainer {
  display: grid;
}
#childContainer {
  align-self: center;
  justify-self: center;
}

```

### 9. Comment utiliser Grid et place-self

La propriété `place-self` définit les propriétés `justify-self` et `align-self` dans une seule déclaration. Ainsi, attribuer à un élément enfant `place-self: center` centre l'enfant à la fois verticalement et horizontalement.

```CSS
#parentContainer {
  display: grid;
}
#childContainer {
  place-self: center;
}
```

### 10. Comment utiliser Grid et margin: auto

Similaire à Flexbox, Grid nous donne également des capacités puissantes d'alignement et de distribution d'espace. 

Comme vu au point 5, nous pouvons faire un processus similaire avec Grid au lieu d'utiliser Flexbox et nous obtiendrons le même résultat si nous attribuons `margin: auto` à l'élément enfant.

```CSS
#parentContainer {
  display: grid;
}
#childContainer {
  margin: auto;
}
```

## Voici le résultat

Eh bien, comme prévu, suivre l'une des méthodes ci-dessus donnera ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-05-27-at-15.02.39.png)

## Résumé

Dans cet article, nous avons vu comment centrer une div en utilisant 10 méthodes différentes. Ces méthodes étaient :

1. Utilisation de **position: relative**, **absolute** et des valeurs de décalage **top**, **left**
2. Utilisation de **position**: **relative** et **absolute**, des valeurs de décalage **top**, **left**, **right** et **bottom** et **margin: auto**
3. Utilisation de **flexbox**, **justify-content** et **align-item**
4. Utilisation de **flexbox**, **justify-content** et **align-self**
5. Utilisation de **flexbox** et **margin: auto**
6. Utilisation de **grid**, **justify-content** et **align-items**
7. Utilisation de **grid** et **place-items**
8. Utilisation de **grid**, **align-self** et **justify-self**
9. Utilisation de **grid** et **place-self**
10. Utilisation de **grid** et **margin: auto**

Nous avons également examiné ce que signifient toutes ces propriétés comme `justify-content`, `align-items`, `position` et comment nous pouvons les utiliser ensemble pour centrer nos divs.


## Quelques bonnes ressources

1. [Un guide complet sur Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
2. [Un guide complet sur Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
3. [Apprendre Flexbox et Grid en construisant une page de destination responsive](https://www.freecodecamp.org/news/css-flexbox-and-grid-tutorial/) 



## Lien GitHub

Vous pouvez trouver le lien GitHub pour tous les fichiers de toutes les méthodes mentionnées ci-dessus ici : [Lien GitHub](https://github.com/sohamderoy/blog-setup-centring-divs)

## Conclusion

Merci d'avoir lu ! J'espère que vous avez aimé cet article sur 10 méthodes différentes pour centrer une `div` et j'espère qu'elles vous seront utiles à l'avenir. 

N'hésitez pas à partager cet article avec vos amis – je vous en serais vraiment reconnaissant. Restez à l'écoute pour plus de contenu incroyable. Peace out! 🔥

## Liens sociaux

- [LinkedIn](https://www.linkedin.com/feed/)
- [Site Web](https://www.sohamderoy.dev/)
- [Twitter](https://twitter.com/_sohamderoy)