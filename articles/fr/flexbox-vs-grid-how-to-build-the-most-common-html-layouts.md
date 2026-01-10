---
title: Flexbox vs Grid - Comment construire les mises en page HTML les plus courantes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/flexbox-vs-grid-how-to-build-the-most-common-html-layouts
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/halacious-weRQAu9TA-A-unsplash-1.jpg
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
seo_title: Flexbox vs Grid - Comment construire les mises en page HTML les plus courantes
seo_desc: "By Ondrej Polesny\nThere are so many great CSS resources all over the internet.\
  \ But what if you just want a simple layout and you want it NOW? \nIn this article,\
  \ I describe the 5 most common web page layouts and how to build them using both\
  \ Flexbox and..."
---

Par Ondrej Polesny

Il existe de nombreuses ressources CSS excellentes sur tout l'internet. Mais que faire si vous voulez simplement une mise en page basique et que vous la voulez MAINTENANT ? 

Dans cet article, je décris les 5 mises en page de pages web les plus courantes et comment les construire en utilisant à la fois Flexbox et Grid.

### Comment cela va fonctionner

Il y a un lien sous chaque mise en page pour le code HTML et CSS complet sur CodePen. 

Notez que j'utilise SASS pour composer les définitions de style, donc si vous voulez faire de même en local, installez SASS en utilisant :

```js
npm i sass -g
```

## Modèle de carte de base

![Image](https://www.freecodecamp.org/news/content/images/2020/08/card.png)

J'ai utilisé la carte ci-dessus comme base de la mise en page de la page web. Elle est composée de trois éléments dans une direction verticale, donc des blocs `div` normaux fonctionneraient bien. Cependant, je devrai plus tard faire en sorte que l'élément du milieu - le paragraphe de texte - s'étire.

Ici, Flexbox et Grid font le travail de manière transparente. Je préfère Flexbox car c'est plus simple pour moi.

**Gagnant : Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/rNeOEQJ), [CodePen Grid](https://codepen.io/ondrabus/pen/mdPeZvd)

Commençons maintenant à créer nos différentes mises en page.

## #1 Carte centrée verticalement et horizontalement

![Image](https://www.freecodecamp.org/news/content/images/2020/08/card--1-.png)

Avec Flexbox, nous avons besoin d'un élément qui centre horizontalement, et d'un autre (l'élément enfant) qui centre verticalement. 

L'ordre des éléments est défini par `flex-direction`. La façon dont l'élément se positionne dans l'espace disponible est définie par `align-self` sur l'élément ou `align-items` sur son parent.

Avec Grid, nous avons besoin de trois colonnes et trois lignes. Ensuite, nous positionnons la carte dans la cellule du milieu. 

Le centrage horizontal est facile. Nous définissons trois colonnes et leurs tailles en utilisant `grid-template-columns: auto 33% auto` car la carte doit être aussi large que 1/3 de la zone visible. 

Le problème est que nous ne connaissons pas les dimensions verticales. Nous voulons que les lignes du haut et du bas occupent l'espace restant, ce qui n'est pas possible avec grid. La carte est centrée, mais sa hauteur dépend de la hauteur de la fenêtre. 

Cependant, nous pouvons résoudre cela avec un élément d'enveloppement supplémentaire autour de la carte et la centrer en utilisant `margin`.

**Gagnant : Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/vYGYobr), [CodePen Grid](https://codepen.io/ondrabus/pen/yLOYdLO)

## #2 Deux cartes centrées verticalement et horizontalement 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/two-cards.png)

Souvent, nous devons centrer plus d'un seul élément. Ces deux cartes doivent également maintenir la même hauteur si l'une ou l'autre contient un texte plus long.

Avec Flexbox, nous devons envelopper les deux cartes dans un autre élément et l'utiliser pour centrer les deux cartes à la fois. 

Nous ne pouvons pas utiliser `align-items` ici car cela s'applique à l'axe Y dans ce cas. Nous devons définir comment l'espace restant sur l'axe X doit être distribué avec `justify-content: center`. Cela garantit que les deux cartes sont centrées horizontalement.

Si nous omettons le problème de hauteur variable de Grid, nous pouvons obtenir le même résultat même sans aucun élément d'enveloppement supplémentaire. Cette fois, nous définissons grid avec cinq colonnes avec `grid-template-columns: auto 33% 50px 33% auto`. Le reste reste le même que dans l'exemple précédent.

**Gagnant : Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/mdPybJa), [CodePen Grid](https://codepen.io/ondrabus/pen/RwaWXOp)

## #3 Plusieurs cartes de même largeur et hauteur

![Image](https://www.freecodecamp.org/news/content/images/2020/08/cards.png)

Ceci est un autre cas d'utilisation typique pour les blogs, les sites e-commerce, ou généralement tout site qui affiche une sorte de liste. Nous voulons que les cartes aient la même largeur et hauteur. La hauteur doit être déduite de l'élément le plus grand de la liste.

Cela peut être fait en Flexbox en utilisant `flex-wrap: wrap`. Les éléments passeront à la ligne suivante si leur largeur dépasse l'espace restant de chaque ligne. Cependant, la même hauteur n'est préservée que dans le cadre d'une seule ligne, sauf si vous la définissez explicitement.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-flexbox-1.png)

Grid montre ici sa vraie puissance. Cette mise en page peut être créée en utilisant `grid-auto-rows: 1fr` qui impose la même hauteur sur toutes les lignes.

**Gagnant : Grid**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/LYNpawv), [CodePen Grid](https://codepen.io/ondrabus/pen/QWNjPLg)

## #4 Texte et images alternés centrés verticalement et horizontalement

![Image](https://www.freecodecamp.org/news/content/images/2020/08/alternating-text.png)

Dans cet exemple, nous avons du texte avec des boutons CTA accompagné d'une image de l'autre côté. Les deux composants doivent être centrés verticalement, car leur taille peut varier.

C'est un jeu d'enfant pour Flexbox. Chaque ligne est un élément `article` divisé en deux conteneurs d'enveloppement, `.img` et `.content`. Ils sont nécessaires pour une distribution de taille égale (`flex-basis: 50%`). 

Le centrage vertical du contenu intérieur est défini par `align-items: center`. 

L'alternance est obtenue en inversant la direction de Flexbox par `flex-direction: row-reverse` sur chaque article impair.

Grid gère également ce cas d'utilisation de manière agréable. Nous n'avons pas besoin de définir une grande grille, mais plutôt une pour chaque `article`. 

Il définit des colonnes de largeur égale qui sont centrées verticalement en utilisant `align-items: center`. 

L'alternance est définie au niveau de la cellule par des valeurs inversées pour `grid-column`.

**Gagnant : égalité**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/BaKoEyQ), [CodePen Grid](https://codepen.io/ondrabus/pen/WNwrOOv)

## #5 En-tête horizontal avec menu

![Image](https://www.freecodecamp.org/news/content/images/2020/08/menu.png)

Pour réaliser cette conception en utilisant Flexbox, les deux côtés de l'en-tête doivent être représentés par un seul élément.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-flexbox.png)

Le logo et le nom de l'entreprise forment une `ancre` à gauche, et le menu est un seul élément `nav` à droite. Flexbox les positionne avec `justify-content: space-between`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-grid.png)

Avec Grid, nous avons besoin de deux colonnes - une pour le logo et l'autre pour le menu. Le menu est une autre grille qui distribue la taille des colonnes de manière égale en utilisant `grid-template-columns: repeat(4, minmax(0, 1fr))`. 

Le problème ici est que si nous voulons ajouter un autre élément au menu, nous devons également ajuster le CSS.

**Gagnant : Flexbox**

[CodePen Flexbox](https://codepen.io/ondrabus/pen/wvGMqXq), [CodePen Grid](https://codepen.io/ondrabus/pen/oNxbeKx)

## Et le gagnant est...

Le score final est de 5:2 en faveur de Flexbox, mais cela ne signifie pas qu'il devient le gagnant ultime de CSS. Il existe des situations où vous devez utiliser l'un ou l'autre, parfois même les deux ensemble, pour obtenir ce dont vous avez besoin.

Si vous avez besoin d'un positionnement flexible et conditionnel, utilisez Flexbox. Si vous voulez créer des listes ou des structures similaires qui nécessitent des éléments de taille égale ou ont une forme de tableau, utilisez Grid. 

En tant que développeur front-end, vous ne pourrez pas vous en sortir sans connaître les deux.

[Guide de référence Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), [Guide de référence Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

P.S. Si j'ai oublié une mise en page que vous utilisez quotidiennement, faites-le moi savoir sur [Twitter](https://twitter.com/ondrabus) et je préparerai une suite :-)