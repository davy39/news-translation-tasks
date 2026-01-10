---
title: 'Bataille des unités CSS : EM contre REMs…COMBAT ! ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T17:35:26.000Z'
originalURL: https://freecodecamp.org/news/em-units-versus-rem-units-fight-382c16af8a67
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VbEg9oepDwSg4mrtTYfNfA.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Bataille des unités CSS : EM contre REMs…COMBAT ! ?'
seo_desc: 'By ZAYDEK

  tl;dr don’t just use px

  CSS Unit Battle: EMs Vs. REMs…FIGHT! ?

  “Two units enter! One unit leaves…” –ThunderDOM

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to...'
---

Par ZAYDEK

#### tl;dr n'utilisez pas *uniquement* px

# Bataille des unités CSS : EM contre REMs…COMBAT ! ?

#### « Deux unités entrent ! Une unité sort… » – ThunderDOM

Avant de commencer l'article, je souhaite partager que je développe un produit, et j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de votre participation ! Et maintenant, revenons à notre programme habituel.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Je collecte des données sur les besoins des développeurs web en matière d'outils éducatifs basés sur le web, et j'aimerais avoir vos réponses. Dans la description de chaque question, j'ai inclus mes propres réponses pour que vous puissiez aussi mieux me connaître ! Il y a ~15 questions ? <a href="https://t.co/qvGU3dF0DB">https://t.co/qvGU3dF0DB</a>.</p>&mdash; username[ZAYDEK] (@username_ZAYDEK) <a href="https://twitter.com/username_ZAYDEK/status/1103914471267790854?ref_src=twsrc%5Etfw">8 mars 2019</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Qui gagnerait dans un COMBAT ?</p>&mdash; username[ZAYDEK] (@username_ZAYDEK) <a href="https://twitter.com/username_ZAYDEK/status/984669337733623808?ref_src=twsrc%5Etfw">13 avril 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Salut ! ? Je suis Zaydek, et je suis là pour vous aider à apprendre le HTML et le CSS. Dans cet article, nous explorerons la différence entre les unités « em » et « rem », et nous comprendrons leur fonctionnement à partir des principes de base.

Quand j'ai appris le HTML et le CSS pour la première fois, c'était un vrai calvaire parce que je n'avais pas bien compris les bases. Ayant appris quelques choses sur le web, j'aimerais partager quelques idées et encouragements, car cela peut être plus simple que vous ne l'imaginez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f375llkXaEoZFZ7ag2gbFQ.png)
_[Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

#### J'ai également enseigné un [cours gratuit HTML/CSS](https://scrimba.com/g/gbuildablog) sur Scrimba où j'enseigne comment construire un beau blog à partir de *zéro*. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbuildablog) ?

#### [Scrimba.com](https://scrimba.com/g/gbuildablog) est une plateforme interactive front-end où les sites web sont enregistrés sous forme d'événements — et non de vidéos — et peuvent être modifiés ! ?

### L'unité em

Em a une étymologie intéressante. `em` signifie discrètement « M ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*7oSiRfywVN_y4-GZPSH6kg.jpeg)
_EMCEPTION_

Cela semble récursif, n'est-ce pas ? Comment `em` peut-il être auto-référentiel ? C'est si astucieux… si subtil. Eh bien, `em` — tel que nous le connaissons en CSS — ne représente pas le caractère « m », mais une relation avec la `font-size` de son parent.

Supposons que nous définissions :

```html
<!DOCTYPE html>
<html>
    <head>
        …
        <style>
            
.a { font-size: 40px; }
.b { font-size: 30px; }
            
        </style>
    </head>
    <body>
        <div class="wrapper">
            <span class="a"></span>
            <span class="b"></span>
        </div>
    </body>
</html>
```

Ici, nous avons défini un `wrapper` avec deux éléments `span`, chacun sans contenu. Donc notre site web est terrible ! Mais ce que nous pouvons faire, c'est donner à nos éléments `span` un peu de texte pour démontrer comment `em` fonctionne :

```html
    …
    <body>
        <div class="wrapper">
            <span class="a">bonjour de l'intérieur .a</span>
            <span class="b">bonjour de l'intérieur .b</span>
        </div>
    </body>
    …
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VbEg9oepDwSg4mrtTYfNfA.png)
_[Cliquez ici](https://scrimba.com/c/cKLrDA8" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Nous venons d'ajouter du texte à nos éléments `span`. Et le texte s'affiche en différentes tailles, `40px` et `30px`. Définissons la `font-size` du `wrapper` à `20px`, puis refactorisons nos `.a` et `.b` `font-size` en utilisant `em`.

```html
        …
        <style>
.wrapper { font-size: 20px; }
.a { font-size: 1.5em; }
.b { font-size: 2.0em; }
        </style>
        …
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*UMgJfL52mB3OtB9I-Yviqg.png)
_[Cliquez ici](https://scrimba.com/c/c8v7DcK" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Quoi ? La `font-size` de nos paragraphes a été inversée ! Maintenant, nous pouvons commencer à explorer comment `em` fonctionne. Si nous avions défini `font-size` comme `20px`, `1em` signifierait `1 * 20px`. Donc `1em` est en quelque sorte sans signification.

Cependant, dans notre CSS, nous avons défini la `font-size` de `.a` comme `1.5em` et celle de `.b` comme `2.0em`. Étant donné que leur parent est `20px`, ces expressions s'évaluent donc à `30px` et `40px`. Donc, l'inverse !

Il y a une objection à l'utilisation de `em`. Si nous avions défini plusieurs parents, comme des éléments à l'intérieur d'éléments, chacun avec leur propre `font-size` définie en `em`, il devient peu intuitif de déterminer quelle est la `font-size` de l'enfant.

### L'unité rem

![Image](https://cdn-media-1.freecodecamp.org/images/1*_N_VW425174tKw-HRjQWMg.jpeg)

`rem` signifie **root em**. Et `grem` signifie **Groot em** — ce qui n'existe pas.

Donc, un `em` est un multiplicateur de la `font-size` de son élément parent, tandis qu'un `rem` est un multiplicateur de la `font-size` de son élément racine. Racine ?

```
   html <- racine
   /  \
head  body
 /      \
…        …
```

Voici à quoi ressemble notre site web — un arbre ! — un arbre « à l'envers » !

```html
        …
        <style>
html { font-size: 20px; }
.a { font-size: 1.5rem; }
.b { font-size: 2.0rem; }
        </style>
        …
```

Ici, nous avons remplacé `.wrapper` par `html`, car maintenant nous utilisons `rem`. Étant donné cela, `.a` et `.b` héritent désormais de leur `font-size` de l'élément `html`, au lieu de notre `.wrapper`.

Notez que rien n'a changé — notre site web est identique, mais nous avons rompu une relation **parent-enfant** `em` avec une relation **racine-enfant** `rem`.

Encore mieux, nous pouvons remplacer l'élément `html` par une [pseudo-classe](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) :

```css
:root { font-size: 20px; }
```

Encore une fois — identique, mais sémantique. Donc, `rem` diffère de `em` parce qu'au lieu d'hériter de la `font-size` du parent, il saute à l'élément `html` ou `:root`. Que se passerait-il si nous changions la `font-size` de `:root` :

```css
:root { font-size: 15px; }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hNpvFL0jg9sfkeJ4wmYfUw.png)
_[Cliquez ici](https://scrimba.com/c/cpK9WCa" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Qu'est-il arrivé ? Notre `span` est 25 % plus petit — évalué à `22.5px` et `30px` — parce que nous avons changé la `font-size` de `:root`. Et c'est une idée géniale. Parce que nous pouvons écrire du CSS non pas en règles, mais en relations.

Récapitulons : nous utilisons `em` pour créer une relation superficielle avec le parent le plus proche d'un élément qui évalue une `font-size`, tandis que nous utilisons `rem` pour créer une relation profonde avec `:root`.

### Les em et rem + les requêtes média

Une idée encore plus géniale que la façon dont nous utilisons `em` et `rem` est de les utiliser en tandem pour les requêtes média. Les requêtes média nous permettent de remplacer le CSS dans certaines circonstances, comme la largeur du site web.

Par exemple :

```html
        …
        <style>
p { color: green; }
@media (max-width: 8.5in) { p { color: blue; } }
        </style>
        …
```

Ici, `p` s'affiche en `green`, mais si la largeur est égale ou inférieure à `8.5in`, le même `p` s'affiche en `blue`. Et nous pouvons aller plus loin : au lieu d'utiliser les requêtes média pour la `color`, nous pouvons les utiliser pour la `font-size` :

```html
        …
        <style>
:root { font-size: 20px; }
.a { font-size: 1.5rem; }
.b { font-size: 2.0rem; }
@media (max-width: 650px) { :root { font-size: 3vw; } }
        </style>
        …
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*UwA6pNec8rhj8I8rgEoP6w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BzUDaxmebj4maN_U-C9k8A.png)
_[Cliquez ici](https://scrimba.com/c/cyM3RSr" rel="noopener" target="_blank" title=") pour ouvrir dans le bac à sable de Scrimba_

Si notre site web est rendu avec une largeur égale ou inférieure à `650px`, nos `em` et `rem` héritent de leur `font-size` non pas comme `20px`, mais comme `3vw`, ou 3 % de la largeur de notre viewport. En faisant cela, nous avons connecté notre CSS au lieu de le cloisonner.

**Une dernière note** : `em` et `rem` ne sont pas limités à `font-size`. Nous pouvons utiliser `em` et `rem` pour décrire `width`, `height` — partout où CSS attend une taille. En combinant cela avec les requêtes média, nous devenons des super-héros CSS.

Apprendre le HTML et le CSS n'a pas à être douloureux — cela peut être subtil et ces langages peuvent être assez puissants. Et `em`, `rem` et `grem` sont certaines des unités les plus puissantes à notre disposition que nous pouvons utiliser pour concevoir des sites web.

#### N'oubliez pas qu'il y a un [cours gratuit](https://scrimba.com/g/gbulma) sur Scrimba où j'enseigne comment créer le même site web à partir de *zéro*. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbulma) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*f375llkXaEoZFZ7ag2gbFQ.png)