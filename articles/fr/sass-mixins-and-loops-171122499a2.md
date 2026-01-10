---
title: Comment utiliser les Mixins et les Boucles Sass
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-11T17:04:37.000Z'
originalURL: https://freecodecamp.org/news/sass-mixins-and-loops-171122499a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G3EYLVI1Rwf-PIou6TLwQA.jpeg
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Sass
  slug: sass
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les Mixins et les Boucles Sass
seo_desc: 'By Jason Arnold

  My current love affair with Sass continues and we’ve taken it to the next level.
  What started out as a faster, less-syntaxy way to write my CSS, has now grown into
  a much more committed relationship.

  We are ready to experiment a littl...'
---

Par Jason Arnold

Mon aventure amoureuse actuelle avec Sass continue et nous l'avons portée à un niveau supérieur. Ce qui a commencé comme une manière plus rapide et moins syntaxique d'écrire mon CSS, est maintenant devenu une relation bien plus engagée.

Nous sommes prêts à expérimenter un peu. J'ai récemment essayé deux des fonctionnalités les plus utiles de Sass, les **Mixins** et les **Boucles**.

#### Mixins et Boucles

Avec les Mixins et les Boucles, la frontière entre CSS et un autre langage de programmation comme JavaScript devient un peu floue. Lorsque vous pensez à votre code en termes de fonctions que vous définissez à un endroit et appelez à un autre, ou de boucles qui itèrent sur un morceau de code un certain nombre de fois, vous ne pensez probablement pas à CSS. Je sais que je ne l'ai jamais fait.

CSS est pour le style. Pourquoi aurais-je besoin de boucler sur un style ou d'appeler un style défini ailleurs ? Cela n'a même pas de sens en termes de CSS. C'est totalement étranger. De plus, n'y a-t-il pas quelque chose sur la '[séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns)' (SoC) ?

Mais en réfléchissant davantage à la SoC, peut-être que cette méthode a plus de sens.

CSS devrait gérer le style du site, n'est-ce pas ? Alors, pourquoi ai-je utilisé la méthode `.style()` de JavaScript ou la méthode `.css()` de jQuery pour gérer cela ? Pourquoi ne puis-je pas changer dynamiquement le style à l'intérieur de CSS ?

Eh bien, Sass vous rapproche un peu de cela. Quel que soit le côté de la clôture SoC où vous vous situez, les Mixins et les Boucles dans Sass peuvent vous faire gagner un temps et des efforts sérieux lors du style de vos sites.

#### Mixins

Je vais commencer par les Mixins. En termes simples, vous pouvez penser à un Mixin comme à une fonction JavaScript pour CSS. Vous définissez un Mixin quelque part dans votre code Sass et vous lui passez des paramètres que vous référencez à l'intérieur du Mixin. Ensuite, ailleurs dans le code Sass, vous appelez ce Mixin et vous passez des arguments qui correspondent aux paramètres et tout cela est exécuté. Confus ? Oui, un peu, alors passons par un exemple.

Tout d'abord, vous définissez un Mixin dans Sass. Cela se fait avec `=`. La syntaxe d'une définition de Mixin ressemble à ceci (rappelez-vous que le `$` est utilisé dans Sass pour définir des variables) :

```sass
=mixinName($param1, $param2, $etc)
  Le code Sass va ici...
```

Ce Mixin peut ensuite être appelé n'importe où ailleurs dans votre code où vous en avez besoin. Et vous passez les arguments dont le Mixin a besoin et Sass convertit tout cela en CSS.

Voici un exemple de Mixin que j'ai écrit pour définir une boîte basique.

```sass
=box($height, $width, $backgroundColor)
  height: $height
  width: $width
  background-color: $backgroundColor
  margin-bottom: 5px
  border: 1px solid black
```

J'ai défini mes trois paramètres après le nom du Mixin, dans ce cas, c'est `box`. Ensuite, j'ai du code Sass, dont une partie appelle les paramètres. Je peux maintenant utiliser ce Mixin ailleurs dans mon code Sass chaque fois que je veux définir une boîte avec ces caractéristiques. Je peux appeler le Mixin autant de fois que je veux, en passant différents arguments à chaque fois. Vous appelez un Mixin avec le caractère `+`.

```sass
.box-1
  +box(100px, 200px, tomato)
  
.box-2
  +box(50px, 100px, rbga(100, 255, 255, 0.5)
```

La page rendra maintenant ces propriétés CSS sur les parties de la page avec les classes `.box-1` et `.box-2`. Voici le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-FOQhFUtopbuUNWgQ5lpNg.png)
_Excitant !_

Cela peut être un peu décevant avec seulement 2 boîtes. Mais si vous avez un site où vous devez définir plusieurs éléments similaires, les Mixins peuvent vous faire gagner beaucoup de temps. Et si vous devez changer ou ajouter une propriété à tous ceux-ci, vous n'avez qu'un seul endroit où aller.

Si je voulais transformer ces boîtes en ovales en ajoutant une propriété `border-radius`, je le fais une seule fois dans le Mixin plutôt que pour chaque boîte dans mon CSS.

#### Boucles

La deuxième fonctionnalité de Sass abordée ici est les Boucles et elles sont exactement ce que vous pensez qu'elles sont. Le concept est le même que dans la plupart des autres langages de programmation. Vous avez un morceau de code qui doit être itéré un certain nombre de fois.

Sass a également ces options et elles sont appelées **directives de contrôle**. Elles commencent par le symbole `@` et la syntaxe est assez facile à comprendre. Celles-ci incluent un `@if`, `@for`, `@each`, et `@while`. Je vais couvrir le `@for` aujourd'hui mais vous pouvez en lire plus sur toutes celles-ci [ici](http://thesassway.com/intermediate/if-for-each-while).

La directive de contrôle `@for` se présente en deux options différentes, les options `to` et `through`. Cela fait référence à la `<fin>` de la boucle. `to` est exclusif et `through` est inclusif.

La syntaxe pour la version `through` d'une boucle `@for` est la suivante :

```sass
@for <$variable> from <start> through <end>
  Le code Sass va ici...
```

La version `to` est la même. Il suffit de remplacer `through` par `to`.

La `$variable` peut être n'importe quel nom que vous voulez lui donner. Les valeurs `<début>` et `<fin>` doivent être des entiers.

Voici un exemple que j'ai écrit qui crée 10 divs sur la page, chacune plus large que la précédente et d'une couleur légèrement différente. J'ai également inclus celles-ci dans un Mixin afin de pouvoir passer des paramètres et l'appeler où j'en avais besoin.

```sass
=graph($height, $baseColor)
  @for $i from 1 through 10
    .line-#{$i}
      height: $height
      width: 2em * $i
      background-color: rgba($i * ($baseColor + 20), $i *  ($baseColor + 10), $i * ($baseColor + 5), 1)
```

Cela crée 10 sélecteurs CSS différents de `.line-1`, `.line-2`, et ainsi de suite. Chaque sélecteur a la **hauteur** spécifiée par `$height`, une **largeur** de `2em *` la **valeur** de `i` et une couleur de fond basée sur le **nombre** `$baseColor` passé.

J'appelle ensuite ce Mixin comme n'importe quel autre

```sass
+graph(10px, 10)
```

Et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GL5VWDJUXrT4n_CAEMvjuA.png)
_Tellement beige !_

Vous pouvez également ajouter des choses comme des pseudo-classes CSS à ces boucles. Voici un autre exemple avec la pseudo-classe `:hover`.

```sass
=stack
  @for $i from 1 through 30
    .stack-#{$i}
    position: absolute
    height: 100px
    width: 100px
    top $i + 10px
    left $i + 10px
    background-color: rgba($i * 1, $i * 2, $i * 3, 1)
    
    &:hover
      background-color: rgba($i * 2, $i * 4, $i * 8, 1)
```

Appelez ce Mixin comme suit (aucun argument nécessaire) :

```sass
+stack
```

La boucle s'exécutera une fois lorsque la page se rendra et ensuite à nouveau sur chaque élément `.stack` individuel lorsque la souris survolera celui-ci. Cela change la couleur de fond.

C'était beaucoup plus facile et rapide d'écrire ce Mixin avec une boucle `@for` plutôt que d'écrire 299 lignes de CSS. Et encore une fois, si je veux changer quelque chose pour tous ceux-ci, je le fais une fois au lieu de 299 fois.

Le résultat est décevant puisque vous ne pouvez pas survoler la capture d'écran. Voici un [CodePen](https://codepen.io/thejasonfile/full/wdmpjZ/) avec tous les exemples ci-dessus.

Ce ne sont là que deux des excellents outils que Sass offre. Ils peuvent vous aider à créer du CSS magnifique et fonctionnel en une fraction du temps.

J'espère que vous avez apprécié cet article. N'hésitez pas à me faire savoir si vous avez des questions. Merci !