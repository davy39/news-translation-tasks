---
title: Feuille de triche des sélecteurs CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-07T00:36:00.000Z'
originalURL: https://freecodecamp.org/news/css-selectors-cheat-sheet
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ed4740569d1a4ca3f63.jpg
tags:
- name: CSS
  slug: css
seo_title: Feuille de triche des sélecteurs CSS
seo_desc: "In CSS, selectors are patterns used to select DOM elements.\nHere is an\
  \ example of using selectors. In the following code, a and h1 are selectors:\na\
  \ {\n  color: black;\n}\n\nh1 {\n  font-size 24px;\n}\n\nCheat sheet of common selectors\n\
  head selects the elemen..."
---

En CSS, les sélecteurs sont des motifs utilisés pour sélectionner des éléments du DOM.

Voici un exemple d'utilisation des sélecteurs. Dans le code suivant, `a` et `h1` sont des sélecteurs :

```css
a {
  color: black;
}

h1 {
  font-size: 24px;
}
```

## **Feuille de triche des sélecteurs courants**

`head` sélectionne l'élément avec la balise `head`

`.red` sélectionne tous les éléments avec la classe 'red'

`#nav` sélectionne les éléments avec l'Id 'nav'

`div.row` sélectionne tous les éléments avec la balise `div` et la classe 'row'

`[aria-hidden="true"]` sélectionne tous les éléments avec l'attribut `aria-hidden` ayant une valeur de "true"

* Sélecteur générique. Sélectionne tous les éléments du DOM. Voir ci-dessous pour son utilisation avec d'autres sélecteurs

## Nous pouvons combiner les sélecteurs de manière intéressante

### Quelques exemples :

`li a` Combinateur descendant du DOM. Toutes les balises `a` qui sont des enfants des balises `li`

`div.row *` sélectionne tous les éléments qui sont des descendants (ou enfants) des éléments avec la balise `div` et la classe 'row'

`li > a` Combinateur de différence. Sélectionne les descendants directs, au lieu de tous les descendants comme les sélecteurs descendants

`li + a` Le combinateur adjacent. Il sélectionne l'élément qui est immédiatement précédé par l'élément précédent. Dans ce cas, seulement le premier `a` après chaque `li`.

`li, a` Sélectionne tous les éléments `a` et tous les éléments `li`.

`li ~ a` Le combinateur de frères. Sélectionne l'élément `a` suivant un élément `li`.

## Pseudo-sélecteurs ou pseudo-classes structurelles

Ceux-ci sont également utiles pour sélectionner des éléments structurels du DOM.

### En voici quelques-uns :

`:first-child` Cible le premier élément immédiatement à l'intérieur (ou enfant) d'un autre élément

`:last-child` Cible le dernier élément immédiatement à l'intérieur (ou enfant) d'un autre élément

`:nth-child()` Cible le n-ième élément immédiatement à l'intérieur (ou enfant) d'un autre élément. Accepte les entiers, `even`, `odd`, ou des formules

`a:not(.name)` Sélectionne tous les éléments `a` qui ne sont pas de la classe `.name`

`::after` Permet d'insérer du contenu sur une page à partir de CSS, au lieu de HTML. Bien que le résultat final ne soit pas réellement dans le DOM, il apparaît sur la page comme s'il y était. Ce contenu se charge après les éléments HTML.

`::before` Permet d'insérer du contenu sur une page à partir de CSS, au lieu de HTML. Bien que le résultat final ne soit pas réellement dans le DOM, il apparaît sur la page comme s'il y était. Ce contenu se charge avant les éléments HTML.

Nous pouvons utiliser les pseudo-classes pour définir un état spécial d'un élément du DOM. Mais elles ne pointent pas vers un élément par elles-mêmes.

### Quelques exemples :

`:hover` sélectionne un élément qui est survolé par un pointeur de souris

`:focus` sélectionne un élément recevant le focus du clavier ou programmatiquement

`:active` sélectionne un élément en cours de clic par un pointeur de souris

`:link` sélectionne tous les liens qui n'ont pas encore été cliqués

`:visited` sélectionne un lien qui a déjà été cliqué

## Plus d'informations sur le sélecteur nth-child

Le sélecteur `nth-child` est une pseudo-classe CSS prenant un motif pour correspondre à un ou plusieurs éléments en fonction de leur position parmi les frères.

### Syntaxe

```css
  a:nth-child(motif) {
    /* Le CSS va ici */
  }
```

### **Motif**

Les motifs acceptés par `nth-child` peuvent se présenter sous la forme de mots-clés ou d'une équation de la forme An+B.

#### **Mots-clés**

##### **Impair**

Impair retourne tous les éléments impairs d'un type donné.

```css
  a:nth-child(odd) {
    /* Le CSS va ici */
  }
```

##### **Pair**

Pair retourne tous les éléments pairs d'un type donné.

```css
  a:nth-child(even) {
    /* Le CSS va ici */
  }
```

#### **An+B**

Retourne tous les éléments correspondant à l'équation An+B pour chaque valeur entière positive de n (en plus de 0).

Par exemple, ce qui suit correspondra à chaque 3ème élément d'ancrage :

```css
  a:nth-child(3n) {
    /* Le CSS va ici */
  }
```

## **Jeux**

[CSS Diner](http://flukeout.github.io/) est un jeu web qui enseigne presque tout ce qu'il y a à savoir sur la combinaison des sélecteurs.

## **Références supplémentaires**

Il existe de nombreux autres sélecteurs CSS ! Apprenez-en davantage sur [CodeTuts](http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048), [CSS-tricks.com](https://css-tricks.com/almanac/selectors/), ou sur [Mozilla Developer Network](https://developer.mozilla.org/en/docs/Web/Guide/CSS/Getting_started/Selectors).