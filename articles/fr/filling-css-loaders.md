---
title: Comment créer des chargeurs CSS de remplissage en utilisant un seul élément
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2024-10-23T17:33:35.718Z'
originalURL: https://freecodecamp.org/news/filling-css-loaders
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729637821745/50ff0461-350c-441c-9726-b838d3ef0a5c.jpeg
tags:
- name: CSS
  slug: css
- name: loaders
  slug: loaders
- name: animations
  slug: animations
- name: HTML
  slug: html
seo_title: Comment créer des chargeurs CSS de remplissage en utilisant un seul élément
seo_desc: 'In a previous article, I showed you how to create two types of CSS loaders:
  a spinner and a progress bar. In this article, you’ll learn about another variation
  called a filling CSS loader.

  I think a demo is worth thousands of words, so check out this...'
---

Dans [un article précédent](https://www.freecodecamp.org/news/how-to-create-a-css-only-loader), je vous ai montré comment créer deux types de chargeurs CSS : un spinner et une barre de progression. Dans cet article, vous apprendrez une autre variation appelée chargeur CSS de remplissage.

Je pense qu'une démonstration vaut mille mots, alors consultez ce Codepen :

<iframe height="450" style="width:100%;height:450px" src="https://codepen.io/t_afif/embed/preview/ExqvRXO/77e4af243170fc28a0c8193a55b7ffe5?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/ExqvRXO/77e4af243170fc28a0c8193a55b7ffe5">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Dans le Pen ci-dessus, je vous montre quatre chargeurs CSS différents de style remplissage, mais nous pouvons en créer encore plus. Vous pouvez consulter [cette collection](https://css-loaders.com/filling/) que j'ai créée pour voir plus de 20 chargeurs différents.

Vous pourriez penser que l'article va être super long, je veux dire, combien de temps faudra-t-il pour expliquer comment créer 20 chargeurs CSS différents ?

Eh bien, ne vous inquiétez pas, ce tutoriel sera super rapide, car je vais vous montrer quelques astuces CSS qui vous aident à créer autant de variations que vous le souhaitez. Les chargeurs semblent différents, mais ils reposent tous sur les mêmes techniques. En ajustant simplement quelques paramètres, vous pouvez obtenir un tout nouveau chargeur.

## Configuration initiale du chargeur

Comme tous [les chargeurs CSS](https://css-loaders.com/) que je crée, le code HTML est aussi simple qu'un seul élément. Rien de plus ! Voici à quoi cela ressemble :

```xml
<div class="loader">Chargement</div>
```

Ensuite, nous appliquons le CSS suivant :

```css
.loader {
  font-weight: bold;
  text-transform: uppercase;
  color: #0000; /* ou transparent */
  -webkit-text-stroke: 1px #000;
}
```

Rien de sophistiqué pour l'instant. Nous rendons le texte transparent et nous ajoutons un contour noir. Voici à quoi cela ressemble :

![Le texte "Chargement" avec un contour noir et une couleur transparente](https://cdn.hashnode.com/res/hashnode/image/upload/v1729506785632/fe01d18e-6d7d-4d49-a5d0-ef6766c51241.png align="center")

Le `-webkit-text-stroke` est toujours marqué comme expérimental, mais il a [un bon support de navigateur](https://caniuse.com/mdn-css_properties_-webkit-text-stroke), donc vous devriez pouvoir l'utiliser sans aucun problème. Cela dit, il est toujours bon de tester votre code dans différents navigateurs pour vous assurer que tout fonctionne correctement.

## Comment remplir le texte avec des couleurs

Maintenant, il est temps de remplir notre texte (c'est pourquoi cette technique est appelée les chargeurs CSS de remplissage !). Pour ce faire, nous allons nous appuyer sur des gradients et `background-clip: text`. Voici le code :

```css
.loader {
  background-image: conic-gradient(#000 0 0);
  background-position: left;
  background-size: 40% 100%;
  background-repeat: no-repeat;
  background-clip: text;
}
```

Ou la version abrégée si vous préférez un code plus compact :

```css
.loader {
  background: 
    conic-gradient(#000 0 0) text
    left/40% 100% no-repeat;
}
```

![la différence entre avec et sans background-clip: text](https://cdn.hashnode.com/res/hashnode/image/upload/v1729507914013/b8991ffe-0b81-4ae0-a356-c102023c2f6c.png align="center")

La figure ci-dessus illustre la différence entre l'utilisation ou non de `background-clip: text`. Il est assez clair que le résultat de gauche est celui que nous visons. Nous limitons la coloration de l'arrière-plan uniquement au texte au lieu de l'élément entier.

Le `conic-gradient(#000 0 0)` semble étrange, n'est-ce pas ? Il vous permet d'avoir un gradient d'une seule couleur. J'ai écrit un petit conseil à ce sujet que je vous invite à lire pour comprendre pourquoi nous utilisons cette syntaxe particulière dans cet article, « [Comment définir correctement un gradient d'une seule couleur](https://css-tip.com/one-color-gradient/) ».

## Comment créer les chargeurs de remplissage

Croyez-le ou non, nous avons presque terminé car nous avons tout ce dont nous avons besoin pour créer les chargeurs CSS. Pour le premier chargeur, nous animons simplement le `background-size` comme suit :

```css
#l1 {
  animation: l1 1s linear infinite;
}
@keyframes l1 {  /*  largeur  hauteur */
  0% {background-size: 0%   100%}
  to {background-size: 120% 100%}
}
```

Nous commençons avec une largeur égale à `0%` jusqu'à atteindre une largeur égale à `120%`. J'aurais pu utiliser `100%`, mais je veux que la coloration complète reste plus longtemps, donc j'utilise une valeur supérieure à `100%`. Quant à la hauteur (la deuxième valeur du `background-size`), elle reste à `100%`.

Le deuxième chargeur utilise la même animation, mais au lieu d'une fonction de timing linéaire, nous utilisons `steps()` pour avoir une animation discrète.

```css
#l2 {
  font-family: monospace;
  animation: l2 2s steps(8, jump-none) infinite;
}
@keyframes l2 {
  0% {background-size: 0%           100%}
  to {background-size: 100% 100%}
}
```

Le texte contient 7 caractères, donc nous utilisons 8 étapes (`N + 1`). J'utilise également une police monospace pour m'assurer que tous les caractères ont la même largeur. Au cas où vous vous interrogeriez sur la valeur `jump-none`, lisez ce qui suit : [Comment utiliser correctement steps() avec les animations](https://css-tip.com/steps/).

[C'est essentiellement le principal truc. En animant](https://css-tip.com/steps/) les propriétés d'arrière-plan, nous créons différents types de chargeurs. Il s'agit soit du `background-size` comme les précédents, soit du `background-position` comme ci-dessous :

<iframe height="400" style="width:100%;height:400px" src="https://codepen.io/t_afif/embed/preview/bGXogOx/59e12d693e164ac69804a554bbac8588?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/bGXogOx/59e12d693e164ac69804a554bbac8588">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Pouvez-vous comprendre comment ils fonctionnent avant de vérifier mon code ? Ce sera votre premier devoir !

## Comment utiliser plusieurs gradients

Utiliser un seul gradient est suffisant pour créer de nombreuses variations, mais nous pouvons faire encore plus si nous introduisons plusieurs gradients. Si vous regardez le quatrième chargeur de la première démonstration, vous verrez que j'utilise sept gradients, un gradient par caractère.

```css
#l4 {
  font-family: monospace;
  --g: conic-gradient(#000 0 0) no-repeat text;
  background: var(--g) 0,var(--g) 1ch,var(--g) 2ch,var(--g) 3ch,var(--g) 4ch,var(--g) 5ch,var(--g) 6ch;
  background-position-y: bottom;
  animation: l4 3s infinite;
}
@keyframes l4 {
  0%     {background-size: 1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   }
  14.28% {background-size: 1ch 100%,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   }
  28.57% {background-size: 1ch 100%,1ch 100%,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   }
  42.85% {background-size: 1ch 100%,1ch 100%,1ch 100%,1ch 0   ,1ch 0   ,1ch 0   ,1ch 0   }
  57.14% {background-size: 1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 0   ,1ch 0   ,1ch 0   }
  71.43% {background-size: 1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 0   ,1ch 0   }
  85.71% {background-size: 1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 0   }
  100%   {background-size: 1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%,1ch 100%}
}
```

J'utilise le même gradient, donc nous considérons une variable CSS `--g` pour éviter la répétition. Ensuite, j'appelle cette variable 7 fois à l'intérieur de la propriété d'arrière-plan. Tous les gradients ont la même position Y (`bottom`) mais une position X différente. C'est pourquoi vous voyez `0, 1ch, 2ch, ..., 6ch`.

Maintenant, si vous vérifiez l'animation, j'anime simplement la hauteur de chaque gradient individuellement. À `0%`, tous ont une hauteur égale à `0`. Ensuite, je mets à jour leur hauteur une par une jusqu'à ce que tous soient à `100%`. La largeur ne change pas, elle est toujours égale à `1ch` (la largeur d'un caractère).

Cela peut sembler difficile au premier abord, mais si vous y pensez un gradient à la fois, c'est assez simple.

Et le troisième chargeur, pourriez-vous demander ? Pour celui-ci, je vais m'appuyer sur [mon générateur en ligne pour les formes ondulées](https://css-generators.com/wavy-shapes/) pour générer la configuration du gradient :

![Capture d'écran du générateur de formes ondulées](https://cdn.hashnode.com/res/hashnode/image/upload/v1729635835522/2f8726a3-e6bb-4949-8846-8408dad56a64.png align="center")

Ensuite, j'anime le `background-position` comme suit :

```css
#l3 {
  background:
    radial-gradient(1.13em at 50% 1.6em,#000 99%,#0000 101%) calc(50% - 1.6em) 0/3.2em 100%,
    radial-gradient(1.13em at 50% -0.8em,#0000 99%,#000 101%) 50% .8em/3.2em 100% repeat-x;
  background-clip: text;
  animation: l3 2s linear infinite;
}
@keyframes l3 {
  0% {background-position: calc(50% - 1.6em) 0,     50%          .8em}
  to {background-position: calc(50% + 1.6em) 0,calc(50% + 3.2em) .8em}
}
```

Celui-ci est probablement un peu plus délicat, mais c'est un autre exemple pour illustrer toutes les possibilités. De la configuration de gradient simple à la plus complexe, nous pouvons créer autant de chargeurs que nous le souhaitons.

Et si vous créiez votre propre chargeur CSS ? Vous pouvez utiliser ce que vous avez appris dans l'article et essayer de créer un chargeur qui ne fait pas partie de [ma collection](https://css-loaders.com/filling/). La meilleure façon d'apprendre est de pratiquer, alors essayez !

## Conclusion

En créant des chargeurs sympas, nous avons passé en revue un ensemble d'astuces CSS liées aux gradients et aux arrière-plans. Même si la création de chargeurs n'est pas votre objectif, vous pouvez toujours réutiliser les mêmes astuces pour faire autre chose.

N'oubliez pas de consulter mon [blog CSS Tip](https://css-tip.com/) où je partage des astuces et des démonstrations CSS sympas.