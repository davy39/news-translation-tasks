---
title: Comment numéroté automatiquement les éléments avec les compteurs CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T18:31:54.000Z'
originalURL: https://freecodecamp.org/news/numbering-with-css-counters
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Numbering-with-CSS-Counters.png
tags:
- name: automation
  slug: automation
- name: CSS
  slug: css
- name: Productivity
  slug: productivity
seo_title: Comment numéroté automatiquement les éléments avec les compteurs CSS
seo_desc: 'By Erisan Olasheni

  CSS counters are used to add counts to elements. The count is added by providing
  variables that can be initialized (using counter-reset), and these variables can
  then be incremented by CSS rules.

  Many developers overlook this power...'
---

Par Erisan Olasheni

Les compteurs CSS sont utilisés pour ajouter des comptes aux éléments. Le compte est ajouté en fournissant des **variables** qui peuvent être initialisées (en utilisant `counter-reset`), et ces variables peuvent ensuite être incrémentées par des règles CSS.

De nombreux développeurs négligent cette puissante fonctionnalité CSS, et c'est pourquoi nous allons passer en revue comment travailler avec les compteurs dans ce tutoriel.

## Quand utiliser les compteurs CSS

Les compteurs CSS peuvent être utilisés chaque fois que vous avez besoin d'un système de comptage sur votre page web. Certains des meilleurs cas d'utilisation sont :

* Numérotation de listes complexes
* Création de liens de pagination dynamiques
* Numérotation des étapes dans un système d'intégration.

Dans ce tutoriel, nous allons parler de l'utilisation des compteurs CSS pour **créer des listes complexes** et **créer une pagination dynamique**.

## Comment utiliser les compteurs CSS

Le système de comptage CSS se compose des propriétés `counter-reset`, `counter-increment`, `counter()` et `counters()` et `content`. Ces propriétés prennent en charge tout ce que vous devez faire dans le système de comptage CSS.

Examinons de plus près ces propriétés pour comprendre comment elles peuvent être utilisées.

### Propriétés des compteurs expliquées

* `counter-reset` : Utilisé pour **réinitialiser** ou **initialiser** votre compteur. Pour utiliser les compteurs CSS, vous devez d'abord en créer un avec cette propriété.
* `counter-increment` : Utilisé pour **incrémenter** la variable d'un compteur déjà **initialisé**.
* `counter()` : Cette fonction fait la magie. Elle est utilisée à l'intérieur de la propriété content, sur un pseudo-sélecteur `:before` ou `:after`, pour **ajouter** les comptes.
* `counters()` : Utilisé pour le comptage hérité, et génère l'instance d'une variable de compteur parent dans l'enfant.
* `content` : Utilisé pour **ajouter** la valeur de compte (chaînes) en manipulant le contenu pour `:before` et `:after` [sélecteurs CSS](https://lyty.dev/css/css-selector.html).

Maintenant que nous comprenons ces propriétés et valeurs des compteurs CSS, plongeons dans nos exemples.

## Numérotation des éléments sur une page web

La numérotation peut être faite en HTML, mais la numérotation CSS offre des moyens dynamiques et faciles à contrôler de faire le travail en utilisant les compteurs CSS. L'exemple suivant numéroté les éléments sur une page web avec CSS.

Tout d'abord, nous allons configurer une numérotation simple qui fait une numérotation à un seul niveau. Ensuite, nous passerons à un exemple plus avancé où nous configurerons une table des matières.

### Numérotation simple

Dans cet exemple, nous allons créer un compteur d'éléments simple avec CSS. Dans votre HTML, créez simplement votre structure d'éléments comme ceci :

```html
<div>
  <p>Mercury</p>
  <p>Venus</p>
  <p>Earth</p>
</div>

```

Dans le CSS, nous allons faire trois choses clés :

1. Initialiser le compteur sur la div parent en utilisant `counter-reset`
2. Incrémenter la valeur du compteur de 1 sur le `div p` enfant en utilisant `counter-increment`
3. Ajouter les variables du compteur avant le contenu `div p` en utilisant le pseudo-sélecteur `:before`.

Allons-y !

```css
div {
  list-style-type: none;
  counter-reset: css-counter 0; /* initialise le compteur à 0; utilisez -1 pour une numérotation basée sur zéro */
}

div p {
  counter-increment: css-counter 1; /* Augmente le compteur de 1. */
}

div p:before {
  content: counter(css-counter) ". "; /* Applique le compteur avant le contenu des enfants. */
}

```

### Le résultat

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225271319_CSS_Counters_Elements_Numbering_CSS_Do_It_Yourself_Lyty_dev.png)

La numérotation ci-dessus a été faite avec du CSS pur. Intéressant, n'est-ce pas ?

Maintenant, nous allons implémenter une numérotation plus complexe qui rend les compteurs CSS dignes d'être appris. Nous allons numéroté les éléments imbriqués avec la fonction `counters()`, qui peut être utilisée pour le comptage hérité. Cela génère l'instance d'un compteur parent dans l'enfant.

### Numérotation de la table des matières

```html
<ul>
  <li>
    Développement Web
    <ul>
      <li>HTML</li>
      <li>
        CSS
        <ul>
          <li>Introduction à CSS</li>
          <li>Sélecteurs CSS</li>
          <li>Animation CSS</li>
        </ul>
      </li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Design Graphique</li>
  <li>Éducation Informatique</li>
</ul>

```

Le CSS ressemble à ceci :

```css
ul {
  list-style-type: none;
  counter-reset: css-counters 0; /* initialise le compteur, définissez -1 pour des compteurs basés sur zéro */
}

ul li:before {
  counter-increment: css-counters;
  content: counters(css-counters, ".") " "; /* génère des compteurs hérités des parents */
}

```

### Le résultat

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225350657_CSS_Counters_Inherited_Element_Counting_Example_CSS_Do_It_Yourself_Lyty_dev.png)

Maintenant, vous pouvez voir la puissance de l'imbrication des comptes avec `counters()`. Cela vous évite le tracas d'une imbrication incorrecte. Pour vous aider à éviter les erreurs, il hérite des propriétés de compteur des parents et y ajoute le compteur de l'enfant.

Maintenant que nous sommes bons pour la numérotation des éléments, que faire ensuite ?

## Création d'une pagination dynamique

Créer une pagination avec les compteurs CSS est assez simple. La pagination est généralement faite avec HTML, en répétant le même ensemble d'éléments et en changeant les nombres à l'intérieur pour créer une navigation vers chaque page d'un résultat.

Un développeur peut choisir d'utiliser quelque chose de dynamique comme faire des boucles qui génèrent les éléments, ou le faire à partir du serveur. Mais aujourd'hui, nous allons utiliser CSS pour le faire dynamiquement !

Comment ? Avec notre fonction `counters()`.

De la même manière que nous avons incrémenté nos valeurs pour la numérotation ci-dessus, nous pouvons également créer une liste de pagination dynamique avec (vous l'avez deviné) les compteurs CSS.

Commençons :

```html
<ul>
  <li class="previous">&lt;</li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li class="next">&gt;</li>
</ul>

```

**Note :** Vous n'avez pas besoin d'ajouter de nombres à l'intérieur des `li`, et vous pouvez en faire autant que vous le souhaitez. Nos `counters()` CSS vont faire la numérotation pour nous.

Le CSS ressemble à ceci :

```css
ul {
  list-style-type: none;
  counter-reset: paginate-counter 0;
}

ul li {
  border: solid 3px #ccc;
  color: #36f;
  border: 5px;
  float: left;
  margin: 5px;
  padding: 8px 10px;
  font-size: 14px;
  cursor: pointer;
  text-align: center;
}

/* Définition des styles pour le texte intérieur */
ul li:not(.previous):not(.next):before {
  counter-increment: paginate-counter;
  content: counter(paginate-counter);
}

```

Le résultat

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225376032_CSS_Counters_CSS_Pagination_Example_CSS_Do_It_Yourself_Lyty_dev.png)

Que pouvez-vous faire d'autre avec les compteurs ? Faites-moi part de vos idées.

Merci !