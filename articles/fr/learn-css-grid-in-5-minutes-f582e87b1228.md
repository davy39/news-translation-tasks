---
title: Apprendre CSS Grid en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T21:40:00.000Z'
originalURL: https://freecodecamp.org/news/learn-css-grid-in-5-minutes-f582e87b1228
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Oc88rInEcNuY-xCN3e1iPQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre CSS Grid en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Per Harald Borgen

  Grid layouts are fundamental to the design of websites, and the CSS Grid module
  is the most powerful and easiest tool for creating it. I personally think it’s a
  lot better than for example Bootstrap (read why here).

  The module ha...'
---

Par Per Harald Borgen

Les mises en page de grille sont fondamentales pour la conception de sites web, et le module CSS Grid est l'outil le plus puissant et le plus facile pour les créer. Je pense personnellement qu'il est bien meilleur que Bootstrap, par exemple (lisez pourquoi [ici](https://hackernoon.com/how-css-grid-beats-bootstrap-85d5881cf163)).

Le module a également obtenu le support natif des [principaux navigateurs](https://caniuse.com/#feat=css-grid) (Safari, Chrome, Firefox, Edge), donc je crois que tous les développeurs front-end devront apprendre cette technologie dans un _futur pas trop lointain_.

Dans cet article, je vais vous guider à travers les bases de CSS Grid aussi rapidement que possible. Je vais omettre tout ce que vous ne devriez pas avoir à connaître jusqu'à ce que vous ayez compris les bases.

J'ai également créé un cours gratuit sur CSS Grid. [Cliquez ici pour obtenir un accès complet.](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_5_minute_article)

![Image](https://cdn-media-1.freecodecamp.org/images/1*T8nvKEYxNZq0UhpF-bsmEA.png)

Alternativement, consultez [cet article](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098), qui explique ce que vous apprendrez tout au long du cours :

Maintenant, plongeons-nous dans le sujet !

### Votre première mise en page de grille

Les deux ingrédients principaux d'une grille CSS sont le **conteneur** (parent) et les **éléments** (enfants). Le conteneur est la grille elle-même et les éléments sont le contenu à l'intérieur de la grille.

Voici le balisage pour un conteneur avec six éléments à l'intérieur :

```
<div class="wrapper">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
  <div>6</div>
</div>

```

Pour transformer notre `div` conteneur en une **grille**, nous lui donnons simplement un affichage de type `grid` :

Mais cela ne fait rien pour l'instant, car nous n'avons pas défini comment nous voulons que notre grille apparaisse. Elle empilera simplement 6 `div` les unes sur les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vTY7C5FMIp8OLkjrgp-vBg.png)

J'ai ajouté un peu de style, mais cela n'a rien à voir avec CSS Grid.

### Colonnes et lignes

Pour la rendre bidimensionnelle, nous devons définir les colonnes et les lignes. Créons trois colonnes et deux lignes. Nous utiliserons les propriétés `grid-template-row` et `grid-template-column`.

Comme nous avons écrit trois valeurs pour `grid-template-columns`, nous obtiendrons trois colonnes. Nous obtiendrons deux lignes, car nous avons spécifié deux valeurs pour `grid-template-rows`.

Les valeurs dictent la largeur que nous voulons pour nos colonnes (100px) et la hauteur que nous voulons pour nos lignes (50px). Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJNIdDiScjhI9CZjdxv3Eg.png)

Pour vous assurer de bien comprendre la relation entre les valeurs et l'apparence de la grille, regardez également cet exemple.

```
.wrapper {
    display: grid;
    grid-template-columns: 200px 50px 100px;
    grid-template-rows: 50px 50px;
}

```

Essayez de comprendre la connexion entre le code et la mise en page.

Voici comment cela se présente :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M9WbiVEFcseUCW6qeG4lSQ.png)

### Placement des éléments

La prochaine chose que vous devez apprendre est comment placer les éléments sur la grille. C'est là que vous obtenez des superpouvoirs, car cela rend la création de mises en page extrêmement simple.

Créons une grille 3x3, en utilisant le même balisage que précédemment.

```
.wrapper {
    display: grid;
    grid-template-columns: 100px 100px 100px;
    grid-template-rows: 100px 100px 100px;
}

```

Cela donnera la mise en page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M9WbiVEFcseUCW6qeG4lSQ.png)

Remarquez que nous ne voyons qu'une grille 3x2 sur la page, alors que nous l'avons définie comme une grille 3x3. C'est parce que nous n'avons que six éléments pour remplir la grille. Si nous en avions trois de plus, la dernière ligne serait également remplie.

Pour positionner et redimensionner les éléments, nous allons les cibler et utiliser les propriétés `grid-column` et `grid-row` :

```
.item1 {
    grid-column-start: 1;
    grid-column-end: 4;
}

```

Ce que nous disons ici, c'est que nous voulons que l'élément1 commence sur la première ligne de la grille et se termine sur la quatrième ligne de colonne. En d'autres termes, il occupera toute la ligne.

Voici comment cela se présentera à l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*he7CoAzdQB3sei_WpHOtNg.png)

Êtes-vous confus quant à la raison pour laquelle nous avons 4 lignes de colonne alors que nous n'avons que 3 colonnes ? Jetez un coup d'œil à cette image, où j'ai dessiné les lignes de colonne en noir :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l-adYpQCGve7W6DWY949pw.png)

Remarquez que nous utilisons maintenant toutes les lignes de la grille. Lorsque nous avons fait en sorte que le premier élément occupe toute la première ligne, il a poussé le reste des éléments vers le bas.

Enfin, je voudrais montrer une manière plus simple d'écrire la syntaxe ci-dessus :

Pour vous assurer que vous avez bien compris ce concept, réarrangeons un peu les éléments.

```
.item1 {
    grid-column-start: 1;
    grid-column-end: 3;
}

.item3 {
    grid-row-start: 2;
    grid-row-end: 4;
}

.item4 {
    grid-column-start: 2;
    grid-column-end: 4;
}

```

Voici à quoi cela ressemble sur la page. Essayez de comprendre pourquoi cela ressemble à cela. Cela ne devrait pas être trop difficile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QDSybpxjXSat6UtoHgUapQ.png)

Et c'est tout !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_5_minute_article) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_5_minute_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_5_minute_article)_