---
title: Comment créer un calendrier avec CSS Grid
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-07-17T00:15:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-calendar-with-css-grid
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca16b740569d1a4ca4e77.jpg
tags:
- name: CSS Grid
  slug: css-grid
- name: Design
  slug: design
- name: technology
  slug: technology
seo_title: Comment créer un calendrier avec CSS Grid
seo_desc: 'Building a calendar with CSS Grid is actually quite easy. I want to show
  you how to do it.

  Here''s what you''ll create by the end of this article:



  Creating the HTML

  You can tell from the image that the calendar contains three parts:


  The month indica...'
---

Créer un calendrier avec CSS Grid est en réalité assez simple. Je veux vous montrer comment faire.

Voici ce que vous aurez créé à la fin de cet article :

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/calendar-fixed.png" alt="Un calendrier construit avec CSS Grid"></figure>

# Création du HTML

Vous pouvez voir sur l'image que le calendrier contient trois parties :

1. L'indicateur de mois
2. L'indicateur de jours de la semaine/week-end
3. Les dates elles-mêmes

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/structure.png" alt="Structure du calendrier"></figure>

La meilleure façon de structurer le HTML est de suivre ce qui semble naturel. Nous allons créer le HTML selon ces trois sections :

```html
<div class="calendar">
  <div class="month-indicator">...</div>
  <div class="day-of-week">...</div>
  <div class="date-grid">...</div>
</div>
```

Vous devriez également voir que nous avons besoin de sept colonnes pour la grille.

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/seven-columns.png" alt="Sept colonnes nécessaires pour la grille"></figure>

Nous allons nous concentrer sur `.day-of-week` et `.date-grid` puisque nous parlons uniquement de la grille.

## Structuration de la grille

Il existe deux façons de créer la CSS Grid.

La première méthode consiste à fusionner les éléments de `.day-of-week` et `.date-grid` en un seul sélecteur. Si nous faisons cela, nous pouvons définir le sélecteur en `display: grid`. Voici à quoi aurait ressembler le HTML si nous avions fait cela :

```html
<div class="grid">
  <!-- Jour de la semaine -->
  <div>Di</div>
  <div>Lu</div>
  <div>Ma</div>
  <div>Me</div>
  <div>Je</div>
  <div>Ve</div>
  <div>Sa</div>

  <!-- Dates -->
  <button><time datetime="2019-02-01">1</time></button>
  <button><time datetime="2019-02-02">2</time></button>
  <button><time datetime="2019-02-03">3</time></button>
  <!-- ... -->
  <button><time datetime="2019-02-28">28</time></button>
</div>
```

Je décourage cette méthode car le HTML perd son sens structurel. Je préfère garder `.day-of-week` et `.date-grid` comme éléments séparés si possible. Cela me permet de lire/comprendre facilement le code que j'ai écrit.

Voici la structure HTML que j'ai choisie :

```html
<div class="day-of-week">
  <div>Di</div>
  <div>Lu</div>
  <div>Ma</div>
  <div>Me</div>
  <div>Je</div>
  <div>Ve</div>
  <div>Sa</div>
</div>

<div class="date-grid">
  <button><time datetime="2019-02-01">1</time></button>
  <button><time datetime="2019-02-02">2</time></button>
  <button><time datetime="2019-02-03">3</time></button>
  <!-- ... -->
  <button><time datetime="2019-02-28">28</time></button>
</div>
```

La meilleure façon de créer une CSS Grid avec la structure que je propose est d'utiliser subgrid. Malheureusement, la plupart des navigateurs ne supportent pas encore subgrid. En attendant, la meilleure façon est de créer deux grilles séparées — une pour `.day-of-week` et une pour `.date-grid`.

`.day-of-week` et `.date-grid` peuvent tous deux utiliser la même grille de sept colonnes.

```css
/* La grille */
.day-of-week,
.date-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/calendar-grid.png" alt="1 février 2019 commence un vendredi"></figure>

## Positionnement des dates

Février 2019 commence un vendredi. Si nous voulons que le calendrier soit correct, nous devons nous assurer que :

1. Le 1 février 2019 tombe un vendredi
2. Le 2 février 2019 tombe un samedi
3. Le 3 février 2019 tombe un dimanche
4. Et ainsi de suite...

Avec CSS Grid, cette partie est facile.

CSS Grid a un algorithme de placement qui suit plus ou moins les règles suivantes (si vous n'avez pas défini `grid-auto-flow` sur `dense`) :

1. Placer les éléments qui ont un `grid-column` ou `grid-row` explicite en premier
2. Remplir le reste selon le dernier élément placé

Cela signifie que :

1. Si le premier élément tombe sur la colonne 6
2. Le deuxième élément sera placé dans la colonne 7.
3. Le troisième élément sera placé sur la ligne suivante, dans la colonne 1 (car il n'y a que sept colonnes).
4. Le quatrième élément sera placé dans la colonne 2,
5. Et ainsi de suite...

Ainsi, si nous positionnons le 1 février sur la sixième colonne (vendredi), le reste des dates sera placé correctement.

C'est aussi simple que cela !

```css
/* Positionner le premier jour sur un vendredi */
.date-grid button:first-child {
  grid-column: 6;
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/calendar-fixed.png" alt="1 février 2019 commence un vendredi"></figure>

Voici un codepen pour que vous puissiez jouer avec :

<p class="codepen" data-height="581" data-theme-id="7929" data-default-tab="result" data-user="zellwk" data-slug-hash="xNpKwp" style="height: 581px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Building a Calendar with CSS Grid">
  <span>See the Pen <a href="https://codepen.io/zellwk/pen/xNpKwp/">
  Building a Calendar with CSS Grid</a> by Zell Liew (<a href="https://codepen.io/zellwk">@zellwk</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

## Vous voulez en savoir plus ?

Cet article contient une fraction d'un composant (un sélecteur de date) de Learn JavaScript. Il y a tellement plus que je veux vous montrer. (Mais ce sont surtout des sujets liés à JavaScript).

Par exemple, dans Learn JavaScript, je vous montre comment :

1. Créer un calendrier pour n'importe quel mois (et n'importe quelle année)
2. Ajouter un bouton précédent/suivant pour changer de mois
3. Cliquer sur chaque date pour afficher une date

Voici à quoi cela ressemble :

<figure><img src="https://zellwk.com/images/2019/calendar-css-grid/datepicker.gif" alt="Exemple du sélecteur de date en action"></figure>

<hr>

Merci d'avoir lu. Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/calendar-with-css-grid). Inscrivez-vous à [ma newsletter](https://zellwk.com) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.