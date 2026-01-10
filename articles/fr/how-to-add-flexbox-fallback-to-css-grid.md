---
title: Comment ajouter un fallback Flexbox à CSS Grid
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-07-25T22:41:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-flexbox-fallback-to-css-grid
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca138740569d1a4ca4d57.jpg
tags:
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
seo_title: Comment ajouter un fallback Flexbox à CSS Grid
seo_desc: 'I shared how to build a calendar with CSS Grid in the previous article.
  Today, I want to share how to build a Flexbox fallback for the same calendar.

  How to provide support

  Generally, there are three ways to provide support when it comes to CSS.

  Firs...'
---

J'ai partagé comment construire un calendrier avec CSS Grid dans [l'article précédent][1]. Aujourd'hui, je veux partager comment construire un fallback Flexbox pour le même calendrier.

## Comment fournir un support

Généralement, il existe trois façons de fournir un support en ce qui concerne le CSS.

**Première méthode :** Écrire un code de fallback. Écraser le code de fallback.

```css
.selector {
  property: fallback-value;
  property: actual-value;
}
```

**Deuxième méthode :** Écrire un code de fallback. Écraser le code de fallback dans les requêtes de fonctionnalités CSS (`@supports`). Réinitialiser les propriétés à l'intérieur de `@supports` si nécessaire.

```css
.selector {
  property: fallback-value;
}

@supports (display: grid) {
  property: actual-value;
}
```

**Troisième méthode :** Tout écrire dans `@supports`.

```css
@supports not (display: grid) {
  .selector {
    property: fallback-value;
  }
}

@supports (display: grid) {
  .selector {
    property: actual-value;
  }
}
```

Ces trois méthodes sont listées par ordre de complexité décroissante. (Si vous devez écraser du code, c'est plus compliqué). Cela signifie que tout écrire dans `@supports` est le plus simple des trois.

La façon dont vous choisissez de supporter votre projet dépend du support des navigateurs pour :

1. La fonctionnalité
2. La fonctionnalité de fallback
3. Le support des requêtes de fonctionnalités

## Vérification du support

Le meilleur endroit pour vérifier le support est [caniuse][2]. Ici, je vois que le support pour CSS Grid est décent. Les navigateurs dont je dois m'inquiéter sont :

1. Opera Mini : 1,42 % d'utilisation mondiale
2. Navigateurs Android 2.1 à 4.4.4 : 0,67 % d'utilisation mondiale
3. Navigateur Blackberry : 0,02 % d'utilisation mondiale (Je ne vais pas m'inquiéter de celui-ci).

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/css-grid-support.png" alt=""></figure>

Le support pour le fallback (Flexbox) est également bon.

Mais nous avons un problème : le fallback Flexbox ne fonctionnerait pas pour Android 2.1 à 4.3 (il ne supporte pas le wrapping). L'utilisation mondiale pour Android 2.1 à 4.3 est de 0,37 %.

Ici, je dois décider :

1. Est-ce que fournir un fallback Flexbox pour Opera Mini (1,42 %), Android 4.4.4 (0,3 %), et Blackberry (0,02 %) vaut l'effort ?
2. Dois-je changer le fallback de Flexbox à une fonctionnalité plus ancienne pour supporter Android 2.1 à 4.3 (un autre 0,37 %) ?

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-support.png" alt=""></figure>

Supposons, pour ce projet, que je décide que le fallback Flexbox est suffisant. Je ne vais pas m'inquiéter d'Android 2.1 à 4.3.

Ensuite, je veux vérifier si les navigateurs supportent les requêtes de fonctionnalités CSS.

Ici, je vois :

1. Opera Mini supporte les requêtes de fonctionnalités
2. Android 4.4.4 supporte les requêtes de fonctionnalités
3. Le navigateur Blackberry ne supporte pas les requêtes de fonctionnalités
4. IE 11 ne supporte pas les requêtes de fonctionnalités

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/feature-queries-support" alt=""></figure>

## Décider comment écrire le code de fallback

Plus tôt, j'ai mentionné qu'il existe trois façons d'écrire un code de fallback pour CSS :

1. Écrire un code de fallback. Écraser le code de fallback.
2. Écrire un code de fallback. Écraser le code de fallback dans `@supports`.
3. Tout écrire dans `@supports`.

Si j'écris tout à l'intérieur de `@supports`, je peux fournir un support pour :

1. Opera Mini (1,43 %)
2. Android 4.4.4 (0,3 %)

Mais je perds le support pour :

1. IE 11 (2,3 %)
2. Blackberry (0,02 %)

Je ne veux pas abandonner les 2,3 % d'utilisateurs de IE, ce qui signifie que la Méthode 3 (tout écrire dans `@supports`) est exclue.

Si j'utilise la Méthode 2 (Écrire un code de fallback. Écraser le code de fallback dans `@supports`), je peux fournir un support pour :

1. IE 11 (2,3 %)
2. Opera Mini (1,43 %)
3. Android 4.4.4 (0,3 %)
4. Navigateur Blackberry (0,02 %)

C'est tout ce dont j'ai besoin. C'est pourquoi je vais opter pour la Méthode 2.

Note : Si vous voulez coder en même temps, vous pouvez utiliser [la démo][3] de [mon article précédent][4] comme point de départ.

## Désactiver le code Grid

Tout d'abord, nous plaçons le code CSS Grid sous `@supports` (comme nous en avons discuté ci-dessus).

```css
@supports (display: grid) {
  .day-of-week,
  .date-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
  }

  .date-grid button:first-child {
    grid-column: 6;
  }
}
```

Nous pouvons désactiver le code CSS Grid en définissant `display` sur une valeur invalide (pas `grid`). Cela désactive l'ensemble du bloc de code.

(Merci à Rachel Andrew pour ce truc astucieux. Je crois que je l'ai appris d'elle ?).

```css
@supports (display: gridx) {
  /*...*/
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/inital-layout.png" alt="Disposition initiale."></figure>

## Écrire le code Flexbox

Nous devons construire la même grille de sept colonnes avec Flexbox. La première chose à faire est de reconnaître que Flexbox et Grid fonctionnent différemment. Nous ne pourrons pas obtenir une réplique parfaite, mais nous pouvons nous en approcher.

La première chose est de définir `display` sur `flex`.

```css
.day-of-week,
.date-grid {
  display: flex;
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-1.png" alt="Résultats après avoir défini display sur flex."></figure>

Nous avons besoin que les boutons dans `.date-grid` s'enroulent, donc nous définissons `flex-wrap` sur `wrap`.

```css
.date-grid {
  flex-wrap: wrap;
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-2.png" alt="Boutons dans la grille de dates enveloppés aux bords."></figure>

Nous devons répliquer la grille de sept colonnes. Un moyen facile de faire cela est de calculer la largeur de la grille en fonction de la largeur de chaque bouton. Ici, j'ai déjà défini chaque bouton à 4.5ch. Cela signifie que la largeur de la grille devrait être `7 x 4.5ch`.

(Nous pouvons utiliser CSS Calc pour faire le calcul pour nous).

```css
.day-of-week,
.date-grid {
  max-width: calc(4.5ch * 7);
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-3.png" alt="Enveloppement à 7 colonnes"></figure>

Nous avons besoin que les éléments dans `.day-of-week` se répartissent sur la largeur disponible. Un moyen simple est de définir `justify-content` sur `space-between`.

```css
.day-of-week {
  justify-content: space-between;
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-4.png" alt="Après avoir défini space-between."></figure>

Ici, nous pouvons voir que les éléments dans `.day-of-week` s'étendent au-delà de la grille. Cette extension se produit parce que nous laissons Flexbox calculer `flex-basis` pour nous. Si nous voulons que chaque élément dans `.day-of-week` ait la même largeur, nous devons définir `flex-basis` nous-mêmes.

Dans ce cas, le moyen le plus simple est de définir `flex-basis` sur la largeur d'un élément de grille (ou `4.5ch`). Note : J'ai ajusté la `font-size` de chaque élément dans `.day-of-week` à `0.7em` (pour des raisons esthétiques visuelles). Nous devons tenir compte de ce changement.

```css
.day-of-week > * {
  flex-basis: calc(4.5ch / 0.7);
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-5.png" alt="Ajusté .day-of-week pour la taille."></figure>

Enfin, nous devons pousser le 1er février à vendredi. (Cinq colonnes). Puisque la colonne est `4.5ch`, nous le poussons simplement par `4.5ch x 5`.

(Encore une fois, nous pouvons utiliser CSS Calc pour nous aider avec cela).

```css
.date-grid button:first-child {
  margin-left: calc(4.5ch * 5);
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/flexbox-6.png" alt="Poussé le 1er février à vendredi"></figure>

## Correction de la version CSS Grid

Nous pouvons réactiver le code CSS Grid et apporter les modifications nécessaires maintenant.

```css
@supports (display: grid) {
  /* ... */
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/grid-fix-1.png" alt="Activation du code CSS Grid"></figure>

Ici, nous voyons certaines valeurs s'envoler loin à droite. Cela se produit parce que nous avons ajouté `margin-left` au premier élément de la grille. Nous devons réinitialiser la marge ajoutée.

```css
@supports (display: grid) {
  /* ... */
  .date-grid button:first-child {
    grid-column: 6;
    margin-left: 0;
  }
}
```

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/grid-fix-2.png" alt="Marge gauche supprimée."></figure>

Une autre chose : Nous pouvons supprimer `max-width` parce que nous n'en avons pas besoin dans le code CSS. (Même si cela n'affecte pas le code CSS, nous voulons toujours le supprimer. Il est toujours préférable d'avoir moins de propriétés).

```css
@supports (display: grid) {
  .day-of-week,
  .date-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    max-width: initial;
  }

  /* ... */
}
```

Voici la différence visuelle entre les versions Flexbox et CSS Grid. Pas trop mal !

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/difference.gif" alt="Différence visuelle entre le code Flexbox et CSS Grid"></figure>

## Une chose amusante

CSS Grid est cool parce qu'il suit la direction d'écriture. Nous pouvons facilement changer le flux de gauche à droite à droite à gauche.

Note : Je ne sais pas si les calendriers sont lus de droite à gauche dans les langues rtl. Je pensais juste que ce serait amusant de le mentionner ?).

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/rtl.gif" alt="Passage de ltr à rtl."></figure>

Notre code pour CSS Grid supporte naturellement ce comportement. Si vous voulez supporter le même comportement avec Flexbox, vous devez utiliser [les propriétés logiques CSS][5].

<figure><img src="https://zellwk.com/images/2019/calendar-flexbox/css-logical-properties-support.png" alt="Support pour les propriétés logiques CSS."></figure>

Puisque le support pour les propriétés logiques CSS n'est pas si bon, nous devons fournir un fallback pour cela. (La meilleure façon est par la Méthode 1 : Écrire un fallback ; écraser le fallback).

```css
.date-grid button:first-child {
  margin-left: calc(4.5ch * 5);
  margin-inline-start: calc(4.5ch * 5);
}

@supports (display: grid) {
  /* ... */
  .date-grid button:first-child {
    grid-column: 6;
    margin-left: 0;
    margin-inline-start: 0;
  }
}
```

C'est tout ! Voici un Codepen pour le code final :

<p class="codepen" data-height="581" data-theme-id="7929" data-default-tab="result" data-user="zellwk" data-slug-hash="ZNrezV" style="height: 581px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Building a Calendar with CSS Grid (and fallback with Flexbox)">
  <span>See the Pen <a href="https://codepen.io/zellwk/pen/ZNrezV/">
  Building a Calendar with CSS Grid (and fallback with Flexbox)</a> by Zell Liew (<a href="https://codepen.io/zellwk">@zellwk</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

[1]: https://zellwk.com/blog/calendar-with-css-grid
[2]: https://caniuse.com "Can I use"
[3]: https://codepen.io/zellwk/pen/xNpKwp "Codepen: Building a Calendar with CSS Grid"
[4]: https://zellwk.com/blog/calendar-with-css-grid
[5]: https://css-tricks.com/css-logical-properties/ "CSS Logical Properties"

<hr>

Merci d'avoir lu. Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/calendar-flexbox-fallback). Inscrivez-vous à [ma newsletter](https://zellwk.com) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.