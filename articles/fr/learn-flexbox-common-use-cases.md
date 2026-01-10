---
title: Apprendre Flexbox avec ces 8 cas d'utilisation les plus courants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-03T23:50:56.000Z'
originalURL: https://freecodecamp.org/news/learn-flexbox-common-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Ep5_thumbnail.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
seo_title: Apprendre Flexbox avec ces 8 cas d'utilisation les plus courants
seo_desc: 'By Thu Nghiem

  When it comes to building responsive websites, Flexbox makes it super easy to create
  flexible and responsive layouts. So learning Flexbox is a must for front-end developers.

  But many tutorials try to teach you everything at once and for...'
---

Par Thu Nghiem

Lorsque l'on construit des sites web responsives, Flexbox rend super facile la création de mises en page flexibles et responsives. Ainsi, apprendre Flexbox est un must pour les développeurs front-end.

Mais de nombreux tutoriels essaient de tout vous enseigner en une seule fois et oublient de vous dire quand et pourquoi vous utiliserez chaque concept.

Dans ce tutoriel, je vais vous montrer les cas d'utilisation les plus courants de Flexbox en résolvant huit tâches ensemble. À la fin, vous serez prêt à utiliser Flexbox dans vos prochains projets.

Vous pouvez télécharger le starter ici : [Flexbox-Tutorial-Starter](https://bit.ly/3eNPw2T)

Voici une vidéo que vous pouvez regarder si vous souhaitez compléter cet article :

%[https://youtu.be/3G4MfMAeamg]

### Installation

Si vous téléchargez et ouvrez le fichier index.html, vous verrez 8 tâches au total. Pour chaque tâche, vous trouverez des conteneurs et des éléments à l'intérieur. Les éléments sont des éléments `div` avec une `largeur` et une `hauteur` de `40px`.

## Tâche 1 : Aligner les éléments de bloc horizontalement dans Flexbox

Pour la première tâche, nous voulons aligner les éléments de bloc horizontalement. Par défaut, les éléments de bloc sont empilés les uns sur les autres. Mais si nous les plaçons à l'intérieur d'un conteneur flex :

```css
.container {
  display: flex;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-17.10.46-1.png)

Tous les éléments de bloc seront alignés sur l'axe horizontal. Plutôt facile, n'est-ce pas ? 😉 Et c'est tout pour la première tâche.

## Tâche 2 : Centrer un ou plusieurs éléments au milieu du conteneur dans Flexbox

Pour la tâche suivante, nous devons centrer certains éléments au milieu du conteneur. Nous pouvons le faire en définissant le conteneur flex pour qu'il ait `justify-content: center;` et `align-items: center;` :

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-17.11.13-1.png)

Et c'est tout pour la tâche 2. Mais avant de continuer, examinons de plus près les propriétés `justify-content` et `align-items`.

### 1. Propriété justify-content

Avec `justify-content`, nous pouvons aligner le ou les éléments sur l'axe horizontal.

Par exemple, si nous voulons aligner le ou les éléments sur l'axe horizontal au **début** du conteneur, nous ferons ceci :

```scss
.container {
  display: flex;
  justify-content: flex-start;
}

```

À la **fin** du conteneur, nous ferons ceci :

```scss
.container {
  display: flex;
  justify-content: flex-end;
}

```

Et au **milieu** du conteneur, nous ferons ceci :

```scss
.container {
  display: flex;
  justify-content: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-1.png)

### 2. Propriété align-items

Cette propriété est similaire à `justify-content`, mais elle s'applique à l'axe vertical. Avec `align-items`, nous pouvons aligner le ou les éléments sur l'axe vertical au **début** du conteneur comme ceci :

```scss
.container {
  display: flex;
  align-items: flex-start;
}

```

À la **fin** du conteneur comme ceci :

```scss
.container {
  display: flex;
  align-items: flex-end;
}

```

* Et au **milieu** du conteneur comme ceci :

```scss
.container {
  display: flex;
  align-items: center;
}

```

Maintenant, si nous combinons `justify-content` et `align-items`, nous pouvons aligner le ou les éléments au milieu du conteneur, dans le coin inférieur droit, le coin supérieur droit, et ainsi de suite.

## Tâche 3 : Répartir l'espace entre les éléments dans Flexbox

Pour la troisième tâche, nous devons ajouter des espaces égaux entre les éléments. Pour y parvenir, c'est assez simple. Tout ce que nous avons à faire est de donner au conteneur flex `justify-content: space-between;`.

```scss
.container {
  display: flex;
  justify-content: space-between;
}

```

`justify-content: space-between;` nous donne des espaces égaux entre les éléments.

Cela est super utile dans la navigation, par exemple, où nous devons mettre des espaces égaux entre les éléments :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/navigation.png)

Et parce que nous regardons `space-between`, avec `justify-content`, nous pouvons également lui donner les valeurs `space-evenly` et `space-around`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/justify.png)

#### `justify-content: space-evenly;`

Si nous donnons à `justify-content` une valeur de `space-evenly`, des espaces seront non seulement ajoutés entre les éléments, mais aussi avant le premier élément et après le dernier élément.

#### `justify-content: space-evenly;`

Si nous donnons à `justify-content` une valeur de `space-around`, des espaces égaux seront ajoutés autour des éléments.

## Tâche 4 : Pousser les éléments à la fin du conteneur dans Flexbox

Pour la tâche 4, nous devons pousser le dernier élément à la fin du conteneur sur l'axe horizontal. Je vais vous montrer 3 options en utilisant Flexbox.

#### Option 1 : utiliser `justify-content: space-between;`

Avec 2 éléments à l'intérieur du conteneur, nous pouvons utiliser `justify-content: space-between;`. Cela poussera le premier élément au début et le dernier élément à la fin du conteneur.

```scss
.container {
  display: flex;
  justify-content: space-between;
}

```

Vous pouvez voir dans l'exemple lorsque nous avons seulement le logo et le bouton :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dtxocmk4n22t3ga8h4ro.png)

ou le logo et les éléments de navigation :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/kchezon63sxjjjcr6o31.png)

#### Option 2 : utiliser une `div` vide avec `flex-grow`

Avec plus de 3 éléments, j'aime ajouter une `div` vide avec `flex-grow: 1` entre les éléments.

Par exemple, si je place une `div` avec `flex-grow: 1` entre le deuxième élément et le dernier élément (troisième élément), la `div` vide s'étendra autant que possible et poussera le dernier élément à la fin du conteneur :

```html
  <div class="option-2">
     <div class="container">
        <div class="item sm"></div>

        <div class="item"></div>

        <div class="space"></div>

        <div class="item"></div>
        </div>
  </div>

```

```scss
  .option-2 .space {
    flex-grow: 1;
  }

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-grow.png)

Vous pourriez le voir dans une navigation plus complexe comme :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/53bomxpqg8dattgno25f.png)

#### Option 3 : utiliser `flex-grow` pour un élément

Si nous avons 2 éléments, par exemple, nous pouvons donner au premier élément `flex-grow: 1;`. En faisant cela, le premier élément s'étendra autant que possible, poussant ainsi le dernier élément à la fin du conteneur.

```scss
  .option-3 .item:first-child {
    flex-grow: 1;
  }

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-grow-2.png)

Quelques exemples dans les composants d'entrée :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ww5uvqfjntpfab9nah8a.png)

#### Bonus

Nous pouvons également utiliser `margin-left: auto` pour pousser le dernier élément à la fin du conteneur. Par exemple, dans l'option 1, nous pouvons donner au dernier élément `margin-left: auto;` et cela fonctionnera de la même manière.

```css
.task-4 .option-1 .container {
  display: flex;
}

.task-4 .option-1 .item:last-child {
  margin-left: auto;
}

```

`margin: auto` est super utile, mais plongeons-nous dans cela dans un autre article et une autre vidéo.

## Tâche 5 : Construire une mise en page de colonnes de taille relative dans Flexbox

En donnant à l'élément une valeur flex de `flex: {nombre}`, nous pouvons contrôler la taille de l'élément par rapport aux autres éléments. Par exemple avec ce code :

```css
.task-5 .item-1 {
  flex: 3;
}

.task-5 .item-2 {
  flex: 1;
}

.task-5 .item-3 {
  flex: 1;
}

.task-5 .item-4 {
  flex: 1;
}

```

Nous venons de créer une mise en page qui a au total 6 colonnes. L'élément 1 prend 3 colonnes, tandis que les 3 autres éléments prendront chacun 1 colonne :

Cela est utile, par exemple, dans une mise en page de tableau :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4jsmaoxclhje1bmlxr68.png)

Cette mise en page est tirée d'un autre tutoriel, où je montre comment construire une application React + Next.js de A à Z. Voici le [lien YouTube](https://youtu.be/v8o9iJU5hEA) si vous souhaitez regarder et coder en même temps.

## Tâche 6 : Construire une mise en page responsive dans Flexbox avec et sans media queries

### 1. Mise en page responsive sans media query

Si nous donnons à un conteneur flex `flex-wrap: wrap` :

```css
.task-6 .container {
  display: flex;
  flex-wrap: wrap;
}

```

Nous aurons une mise en page responsive où les éléments n'essaieront pas de se rétrécir à l'intérieur du conteneur :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.44.31.png)

### 2. Mise en page responsive avec media query

Avec les media queries, nous aurons plus de contrôle sur la taille des éléments. Supposons que dans un conteneur `flex-wrap`, nous voulons avoir 2 colonnes. Nous pouvons faire cela en :

```css
.task-6 .container {
  display: flex;
  flex-wrap: wrap;
}

.task-6 .item {
  flex-basis: 50%;
}

```

Maintenant, les éléments seront disposés en une mise en page à 2 colonnes, où chaque colonne prend la moitié du conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.45.25.png)

Avec la même logique, supposons que nous voulons avoir une mise en page à 4 colonnes lorsque l'écran est plus large que `375px`, nous pouvons donner à chaque élément `flex-basis: 25%` :

```css
@media (min-width: 375px) {
  .task-6 .item {
    display: flex;
    flex-basis: 25%;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.47.20.png)

## Tâche 7 : Changer l'ordre des éléments dans Flexbox (peu courant)

Avec Flexbox, nous pouvons changer l'ordre des éléments. Par exemple, à l'intérieur d'un conteneur flex, si nous avons 4 éléments et que nous voulons placer le premier élément à la fin de la ligne. Tout ce que nous avons à faire est de donner à l'élément `order: 1`.

```css
.task-7 .item-1 {
  order: 1;
}

```

Par défaut, la propriété `order` a une valeur égale à 0 et elle peut prendre un nombre négatif.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.48.20.png)

## Tâche 8 : Changer la position d'un élément à l'intérieur d'un conteneur flex (peu courant)

Un élément à l'intérieur du flex peut changer de position par lui-même en utilisant `align-self`.

```css
align-self: auto | flex-start | flex-end | center | baseline | stretch;

```

Par exemple, supposons que nous voulons avoir l'élément 3 à la fin du conteneur sur l'axe vertical. Nous pouvons faire ceci :

```css
.task-8 .container {
  display: flex;
}

.task-8 .item-3 {
  align-self: flex-end;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.49.00.png)

## Propriété `flex-direction`

Flexbox a une propriété `flex-direction` par défaut. `flex-direction` a la valeur `row`, ce qui signifie que les éléments sont alignés sur l'axe horizontal.

Si nous voulons que les éléments soient alignés sur l'axe vertical, nous pouvons utiliser `flex-direction: column;`.

Par exemple, dans la tâche 3, si nous donnons au conteneur flex `flex-direction: column;` :

```css
.task-3 .container {
  display: flex;

  justify-content: space-between;
  flex-direction: column;
}

```

Nous aurons :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.50.19.png)

Ce que nous venons d'apprendre pour flex-direction: row; fonctionnera toujours de la même manière pour flex-direction: column;, mais au lieu d'un axe horizontal, ce sera un axe vertical.

## Conclusion

Maintenant que vous avez appris Flexbox et [CSS Grid](https://www.freecodecamp.org/news/learn-css-grid-by-building-5-layouts/), vous pouvez continuer en construisant des sites web responsives. Vous pouvez trouver une liste de projets à faire sur [devchallenges.io](https://devchallenges.io/), ou vous pouvez me rejoindre dans le tutoriel vidéo suivant, où nous construirons un site web professionnel de A à Z :

%[https://youtu.be/CrryRvjYsgc]

Merci d'avoir lu cet article. Ce sujet appartient à la série de vidéos que je mettrai à jour sur [Learn.DevChallenges.io](https://learn.devchallenges.io/). Pour rester informé, suivez-moi sur les réseaux sociaux ou abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1). Sinon, bon codage et à bientôt dans les prochaines vidéos et articles 👋.

**__________ 🐣 À propos de moi __________**

Je suis un développeur full-stack, un designer UX/UI et un créateur de contenu. Vous pouvez mieux me connaître dans cette courte vidéo :

[Contenu intégré](https://www.youtube.com/embed/qCkmFd-72JY?feature=oembed)

* Je suis le fondateur de [DevChallenges](https://devchallenges.io/)
* Abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1)
* Suivez-moi sur [Twitter](https://twitter.com/thunghiemdinh)
* Rejoignez [Discord](https://discord.com/invite/3R6vFeM)