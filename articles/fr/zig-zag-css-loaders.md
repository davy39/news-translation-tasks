---
title: Comment créer des loaders CSS en zig-zag avec un seul élément
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2024-11-20T23:40:49.710Z'
originalURL: https://freecodecamp.org/news/zig-zag-css-loaders
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732045303831/af9240a9-6a25-4b13-a397-102ee098db78.jpeg
tags:
- name: CSS
  slug: css
- name: animations
  slug: animations
seo_title: Comment créer des loaders CSS en zig-zag avec un seul élément
seo_desc: 'In a previous article, I showed you how to create filling CSS loaders collection
  where each loader was built using a single HTML element. Here, you’ll learn more
  about loaders by creating the Zig-Zag collection.

  Here is an overview of what you’ll be ...'
---

Dans [un article précédent](https://www.freecodecamp.org/news/filling-css-loaders), je vous ai montré comment créer une collection de loaders CSS de remplissage où chaque loader était construit avec un seul élément HTML. Ici, vous en apprendrez davantage sur les loaders en créant [la collection Zig-Zag](https://css-loaders.com/zig-zag/).

Voici un aperçu de ce que vous allez construire :

<iframe height="500" style="width:100%;height:500px" src="https://codepen.io/t_afif/embed/preview/RwXdvKj/83804c95907793e888c3036d7dd29251?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/RwXdvKj/83804c95907793e888c3036d7dd29251">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Vous pouvez également consulter [ma collection en ligne](https://css-loaders.com/zig-zag/) pour voir jusqu'à 20 variations utilisant une forme en zig-zag.

Nous n'étudierons pas toutes les variations, mais je vais vous montrer quelques astuces qui vous aideront à créer autant de variations que vous le souhaitez.

## Comment créer une forme en zig-zag

La première étape consiste à créer une forme en zig-zag. Pour cela, vous pouvez récupérer le code de mon site de formes CSS : [https://css-shape.com/zig-zag-line/](https://css-shape.com/zig-zag-line/).

![Forme en zig-zag de css-shape.com](https://cdn.hashnode.com/res/hashnode/image/upload/v1731707755150/f1782db9-fa7f-472e-b771-cfc1c2046e0c.png align="center")

Vous pouvez ajuster les différentes variables pour obtenir le zig-zag souhaité. Dans notre cas, j'utiliserai une version plus simple sans variables.

```css
.loader {
  height: 47px; /* contrôle la taille */
  aspect-ratio: 5;
  background:
   conic-gradient(from 135deg at top,#000 90deg,#0000 0) top,
   conic-gradient(from 135deg at top,#0000 90deg,#000 0) bottom;
  background-size: 20% 50%;
  background-repeat: repeat-x;
}
```

Et voici une figure pour illustrer comment ces gradients créent la forme :

![Dégradés de couleurs créés par le code](https://cdn.hashnode.com/res/hashnode/image/upload/v1731708477342/bbe3e0b6-24a2-498d-992b-4ee152b0d74c.png align="center")

Le premier dégradé a créé la partie rouge tandis que le second a créé la partie verte. Nous avons deux formes triangulaires qui se répètent horizontalement.

Puisque nous avons cinq répétitions, j'ai utilisé `aspect-ratio: 5` et `20% (100%/5)` dans le `background-size`. Vous pouvez le rendre plus générique en introduisant une variable pour contrôler le nombre de répétitions, mais comme je l'ai dit précédemment, je vais garder les choses simples.

Je tiens à souligner que lors de l'utilisation de gradients, vous pouvez obtenir le même résultat en utilisant différentes syntaxes. Par exemple, je peux mettre à jour le code précédent avec ce qui suit :

```css
.loader {
  height: 47px; /* contrôle la taille */
  aspect-ratio: 5;
  background:
   conic-gradient(from 135deg at top   ,#000 90deg,#0000 0),
   conic-gradient(from -45deg at bottom,#000 90deg,#0000 0) 12.5% 100%;
  background-size: 20% 50%;
  background-repeat: repeat-x;
}
```

C'est toujours la même sortie mais avec une syntaxe différente pour le second gradient. Avez-vous remarqué la partie répétée dans les gradients ? Cette partie contrôle la coloration et nous pouvons la définir comme une variable pour éviter la répétition et pouvoir mettre à jour la couleur une seule fois dans le code.

```css
.loader {
  height: 47px; /* contrôle la taille */
  aspect-ratio: 5;
  --c:#000 /* la couleur */ 90deg,#0000 0;
  background:
   conic-gradient(from 135deg at top   ,var(--c)),
   conic-gradient(from -45deg at bottom,var(--c)) 12.5% 100%;
  background-size: 20% 50%;
  background-repeat: repeat-x;
}
```

Maintenant, nous avons notre forme en zig-zag et nous sommes prêts à l'animer.

## Comment animer la forme en zig-zag

Puisque nous utilisons un fond, nous allons animer le `background-position` pour obtenir notre premier loader. L'idée est de déplacer les gradients horizontalement et de créer un mouvement infini.

```css
.loader {
  height: 47px; /* contrôle la taille */
  aspect-ratio: 5;
  --c:#000 /* la couleur */ 90deg,#0000 0;
  background:
   conic-gradient(from 135deg at top   ,var(--c)),
   conic-gradient(from -45deg at bottom,var(--c)) 12.5% 100%;
  background-size: 20% 50%;
  background-repeat: repeat-x;
  animation: loading .8s infinite linear;
}

@keyframes loading {
  0%   {background-position: 0   0,12.5% 100%}
  100% {background-position: 25% 0,37.5% 100%}
}
```

Remarquez comment nous avons augmenté la valeur X du `background-position` de `25%`. Au cas où vous vous demanderiez quelle est la logique derrière cette valeur, voici la formule :

`0.2 / (1 - 0.2) = .25 = 25%`

`.2` correspond au `20%` utilisé dans le `background-size`.

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/poMBgQO/5ddc67ad2324e68680f9d1071e46dc96?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/poMBgQO/5ddc67ad2324e68680f9d1071e46dc96">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Nous avons notre premier loader ! En fait, deux loaders car nous pouvons facilement changer la direction du mouvement en ajoutant `animation-direction: reverse`.

Essayons une animation différente : en utilisant `clip-path` et la valeur `inset()`. Nous pouvons facilement ajuster cette technique pour créer de nombreuses variations.

Commençons par un exemple de base :

```css
.loader {
  /* même code que précédemment */
  animation: loading .8s infinite linear;
}
@keyframes loading {
  0%   {clip-path: inset(0 100% 0 0)}
  100% {clip-path: inset(0 0    0 0)}
}
```

La valeur `inset()` crée un rectangle où seule la partie à l'intérieur sera visible. Pour cela, nous définissons une distance de chaque côté de l'élément (haut, droite, bas, gauche).

Logiquement, `inset(0 0 0 0)` montre tout l'élément puisque toutes les distances sont égales à 0, mais `inset(0 100% 0 0)` cache complètement l'élément puisque la valeur de droite est égale à 100%. Elle touchera donc le bord opposé, créant un rectangle vide.

En animant cette valeur de droite de `100%` à `0`, nous créons une animation de révélation. Une autre variation de loader !

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/WNVWrVy/f6214a24e77a0ad6694d3a5bf93d2a23?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/WNVWrVy/f6214a24e77a0ad6694d3a5bf93d2a23">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Si vous inspectez le code de la deuxième animation, vous verrez que j'ai fait la même chose mais avec le côté gauche.

Nous pouvons également avoir un effet de glissement si nous animons à la fois les valeurs de gauche et de droite tout en gardant leur différence constante.

```css
.loader {
  /* même code que précédemment */
  animation: loading .8s infinite linear;
}
@keyframes loading {
  0%   {clip-path: inset(0 60% 0 0  )}
  100% {clip-path: inset(0 0   0 60%)}
}
```

La valeur de droite passe de `60%` à `0` et celle de gauche de `0` à `60%`, donc nous avons une différence constante égale à `60%` qui créera l'illusion d'un rectangle glissant. Un autre loader sympa !

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/wvVZGwy/71a0f6a7bf177c51252230d7e272fb57?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/wvVZGwy/71a0f6a7bf177c51252230d7e272fb57">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

En essayant différentes combinaisons de valeurs `inset()`, vous pouvez obtenir de nombreux loaders CSS. Essayez ! Vous pouvez également consulter [ma collection en ligne](https://css-loaders.com/zig-zag/) et essayer d'identifier les variations qui utilisent `clip-path: inset()`.

## Comment créer une animation discrète

Pour obtenir une animation discrète, vous pouvez utiliser la fonction de temporisation `steps()` au lieu de `linear`. Commençons avec le premier exemple en utilisant `steps(2)`.

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/YzmbzGL/28874aa2a6066deb4d06fdbefaaade62?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/YzmbzGL/28874aa2a6066deb4d06fdbefaaade62">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Nous pouvons faire la même chose avec presque toutes les variations. Essayons avec celles qui utilisent `clip-path: inset()`.

```css
.loader {
  /* même code que précédemment */
  animation: loading .8s infinite steps(5);
}
@keyframes loading {
  0%   {clip-path: inset(0 100% 0 0)}
  100% {clip-path: inset(0 0    0 0)}
}
```

Nous avons cinq répétitions, alors voyons ce que nous obtiendrons avec `steps(5)`.

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/JjgqjNr/9a6b43cda41ed9ec9cb49ea9bdaabb56?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/JjgqjNr/9a6b43cda41ed9ec9cb49ea9bdaabb56">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Pour l'instant, ce n'est pas bon car nous ne voyons pas toutes les répétitions. L'animation s'arrête à 4 répétitions, mais nous devons voir tout l'élément (5 répétitions). Le compte commence à partir de 0, donc ce dont nous avons vraiment besoin, c'est de 6 étapes au lieu de 5 pour montrer toutes les répétitions.

```css
.loader {
  /* même code que précédemment */
  animation: loading .8s infinite steps(6);
}
@keyframes loading {
  0%   {clip-path: inset(0 100% 0 0)}
  100% {clip-path: inset(0 0    0 0)}
}
```

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/RwXmKje/df2744eb1e707246a628b22ce96c7e4c?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/RwXmKje/df2744eb1e707246a628b22ce96c7e4c">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Même avec 6 étapes, le résultat n'est toujours pas bon, mais ne vous inquiétez pas, ce n'est pas un bug. Le comportement par défaut de `steps()` nous donne cette sortie, mais nous pouvons la mettre à jour pour obtenir la sortie attendue :

```css
.loader {
  /* même code que précédemment */
  animation: loading .8s infinite steps(6,jump-none);
}
@keyframes loading {
  0%   {clip-path: inset(0 100% 0 0)}
  100% {clip-path: inset(0 0    0 0)}
}
```

Si vous n'êtes pas familier avec `jump-none`, c'est une valeur qui peut résoudre la plupart de vos problèmes lors de l'utilisation de `steps()`. J'ai écrit un court article à ce sujet si vous voulez plus de détails : « [Comment utiliser correctement steps() avec les animations](https://css-tip.com/steps/) »

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/JjgqEpO/5433bef4c1b86de39837108b68ca8eba?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/JjgqEpO/5433bef4c1b86de39837108b68ca8eba">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Notre animation est parfaite maintenant ! Nous pouvons également en faire une animation à 11 étapes (`5×2 + 1`) et obtenir un autre loader sympa.

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/vYowgRV/47df83689104665da6997c41a5825efb?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/vYowgRV/47df83689104665da6997c41a5825efb">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Même l'effet de glissement peut avoir sa variation discrète.

<iframe height="300" style="width:100%" src="https://codepen.io/t_afif/embed/preview/bGXyZpO/799d03f2d573655e6522476418c6006a?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/bGXyZpO/799d03f2d573655e6522476418c6006a">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Pouvez-vous comprendre pourquoi j'utilise 4 et 7 étapes ? Je vous laisse faire le calcul comme petit exercice.

## Conclusion

Cet article vous a montré comment créer des formes en zig-zag, comment les animer en utilisant `clip-path`, et comment créer des animations discrètes. Vous pouvez également envisager d'autres astuces comme l'utilisation des deux pseudo-éléments pour avoir deux formes.

Je n'ai pas exploré toutes les variations, mais vous avez maintenant la recette pour en créer la plupart !

Vous pouvez explorer [ma collection de loaders Zig-Zag](https://css-loaders.com/zig-zag/) pour étudier d'autres variations et essayer de créer votre propre loader. C'est une bonne opportunité de pratiquer ce que vous avez appris dans cet article.