---
title: Tutoriel CSS Media Query – Résolutions standards, points de rupture CSS et
  tailles de téléphones cibles
date: '2020-04-08T17:59:44.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bb5740569d1a4ca2d74.jpg
tags:
- name: responsive design
  slug: responsive-design
seo_desc: 'By Cem Eygi

  In the past, building a website was much simpler. Today a website’s layout should
  adapt itself not only to computers, but also tablets, mobile devices, and even TVs.

  Making a website with an adaptable layout is called Responsive Web Desig...'
---


Par Cem Eygi

<!-- more -->

Par le passé, la création d'un site web était beaucoup plus simple. Aujourd'hui, la mise en page d'un site web doit s'adapter non seulement aux ordinateurs, mais aussi aux tablettes, aux appareils mobiles et même aux téléviseurs.

Concevoir un site web avec une mise en page adaptable est ce qu'on appelle le Design Web Responsif (Responsive Web Design). Et les CSS Media Queries sont l'une des parties les plus importantes du Design Responsif. Dans cet article, nous allons examiner de plus près les Media Queries et comment les utiliser en CSS.

Si vous préférez, vous pouvez regarder la version vidéo ci-dessous :

<iframe width="560" height="315" src="https://www.youtube.com/embed/P_vkS4UJNDk" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

## Qu'est-ce qu'une Media Query ?

Une Media Query est une fonctionnalité de CSS3 qui permet à une page web d'adapter sa mise en page à différentes tailles d'écran et types de médias.

### Syntaxe

```
@media media type and (condition: breakpoint) {
  // CSS rules
}
```

Nous pouvons cibler différents types de médias sous une variété de conditions. Si la condition et/ou les types de médias correspondent, alors les règles à l'intérieur de la media query seront appliquées, sinon elles ne le seront pas.

La syntaxe peut sembler compliquée au début, alors expliquons chaque partie en détail…

### La règle @media

Nous commençons à définir les media queries avec la règle `@media` et incluons ensuite les règles CSS à l'intérieur des accolades. La règle `@media` est également utilisée pour spécifier les types de médias cibles.

```
@media () {
  // CSS rules
}
```

### Parenthèses

À l'intérieur des parenthèses, nous définissons une condition. Par exemple, je souhaite appliquer une taille de police plus grande pour les appareils mobiles. Pour ce faire, nous devons définir une largeur maximale qui vérifie la largeur d'un appareil :

```
.text {
  font-size: 14px;
}

@media (max-width: 480px) {
  .text {
    font-size: 16px;
  }
}
```

Normalement, la taille du texte sera de `14px`. Cependant, comme nous avons appliqué une media query, elle passera à `16px` lorsqu'un appareil a une largeur maximale de `480px` ou moins.

**Important : placez toujours vos media queries à la fin de votre fichier CSS.**

### Types de médias

Si nous n'appliquons pas de type de média, la règle `@media` sélectionne par défaut tous les types d'appareils. Sinon, les types de médias viennent juste après la règle `@media`. Il existe de nombreux types d'appareils, mais nous pouvons les regrouper en 4 catégories :

-   all — pour tous les types de médias
-   print — pour les imprimantes
-   screen — pour les écrans d'ordinateur, les tablettes et les smartphones
-   speech — pour les lecteurs d'écran qui « lisent » la page à haute voix

Par exemple, lorsque je veux sélectionner uniquement les écrans, je placerai le mot-clé `screen` juste après la règle `@media`. Je dois également concaténer les règles avec le mot-clé `and` :

```
@media screen and (max-width: 480px) {
  .text {
    font-size: 16px;
  }
}
```

### Points de rupture (Breakpoints)

Les points de rupture (breakpoints) sont peut-être le terme le plus courant que vous entendrez et utiliserez. Un breakpoint est une clé pour déterminer quand changer la mise en page et adapter les nouvelles règles à l'intérieur des media queries. Revenons à notre exemple du début :

```
@media (max-width: 480px) {
  .text {
    font-size: 16px;
  }
}
```

Ici, le point de rupture est `480px`. Maintenant, la media query sait quand définir ou écraser la nouvelle classe. En résumé, si la largeur d'un appareil est inférieure à `480px`, la classe `text` sera appliquée, sinon elle ne le sera pas.

#### Points de rupture courants : existe-t-il une résolution standard ?

L'une des questions les plus fréquemment posées est : « Quel point de rupture dois-je utiliser ? ». Il existe une multitude d'appareils sur le marché, nous ne pouvons donc pas et ne devrions pas définir des points de rupture fixes pour chacun d'eux.

C'est pourquoi nous ne pouvons pas dire qu'il existe une résolution standard pour les appareils, mais il existe certains points de rupture couramment utilisés dans la programmation quotidienne. Si vous utilisez un framework CSS (comme Bootstrap, Bulma, etc.), vous pouvez également utiliser leurs points de rupture.

Voyons maintenant quelques points de rupture courants pour les largeurs d'appareils :

-   320px — 480px : Appareils mobiles
-   481px — 768px : iPads, Tablettes
-   769px — 1024px : Petits écrans, ordinateurs portables
-   1025px — 1200px : Ordinateurs de bureau, grands écrans
-   1201px et plus — Écrans extra larges, TV

Comme je l'ai dit plus haut, ces points de rupture peuvent différer et il n'y a pas de standard exactement défini, mais ce sont ceux qui sont couramment utilisés.

## Conclusion

Le Design Responsif est un impératif dans le domaine de la conception et du développement web d'aujourd'hui. Les media queries sont l'une des parties les plus importantes de la création de mises en page responsives, et j'espère que vous trouverez mon article utile pour comprendre comment fonctionnent les media queries.

**Si vous souhaitez en savoir plus sur le développement web, n'hésitez pas à [vous abonner à ma chaîne.][1]**

Merci de m'avoir lu !

[1]: https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber