---
title: Encore plus sur le fonctionnement de Flexbox — expliqué en grands, colorés,
  gifs animés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-21T02:58:49.000Z'
originalURL: https://freecodecamp.org/news/even-more-about-how-flexbox-works-explained-in-big-colorful-animated-gifs-a5a74812b053
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PghNPeo_XAXroKXksXGfCQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: flexbox
  slug: flexbox
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Encore plus sur le fonctionnement de Flexbox — expliqué en grands, colorés,
  gifs animés
seo_desc: 'By Scott Domes

  Last time we got started with the basic Flexbox properties: flex-direction, justify-content,
  align-items, and align-self.

  These commands are powerful for creating basic layouts. But once you start building
  webpages with Flexbox, you’ll...'
---

Par Scott Domes

[La dernière fois](https://medium.freecodecamp.com/an-animated-guide-to-flexbox-d280cf6afc35#.xdqa0my2e), nous avons commencé avec les propriétés de base de Flexbox : flex-direction, justify-content, align-items et align-self.

Ces commandes sont puissantes pour créer des mises en page de base. Mais une fois que vous commencez à construire des pages web avec Flexbox, vous devrez approfondir pour maximiser son potentiel.

Maintenant, examinons en profondeur le dimensionnement Flexbox — et comment vous pouvez l'utiliser pour construire des mises en page adaptables et belles.

### Propriété #1 : Flex-Basis

Dans le [dernier article](https://medium.freecodecamp.com/an-animated-guide-to-flexbox-d280cf6afc35#.xdqa0my2e), nous avons principalement examiné les propriétés qui s'appliquent aux éléments conteneurs. Cette fois, nous allons examiner exclusivement le dimensionnement appliqué aux éléments enfants.

Notre première propriété est, à mon avis, l'une des propriétés les moins bien expliquées dans les tutoriels Flexbox.

Mais — ne vous inquiétez pas. C'est en fait assez simple.

Flex-basis contrôle la taille par défaut d'un élément, _avant qu'il ne soit manipulé par d'autres propriétés Flexbox_ (plus sur cela plus tard).

Dans le GIF ci-dessous, cela signifie qu'il est interchangeable avec la propriété width :

![Image](https://cdn-media-1.freecodecamp.org/images/Ozhyix5MXR41DUiTeklQi8s3OaKx7PeIHrgd)

Ce qui rend flex-basis unique par rapport à width, cependant, c'est qu'il correspond à nos bons vieux axes flex :

![Image](https://cdn-media-1.freecodecamp.org/images/J2U9wilK4oozfqtigLJNdxD1CHjYIJ0vEd-M)

Flex-basis affecte la taille d'un élément _le long de l'axe principal_.

Voyons ce qui se passe lorsque nous gardons notre flex-basis identique, mais changeons la direction de notre axe principal :

![Image](https://cdn-media-1.freecodecamp.org/images/KpHqxOlDyHFOv95zrQ0pXDGda5yreWWNtCpi)

Notez que nous avons dû passer de la définition de la hauteur manuellement à la définition de la largeur. Flex-basis détermine ainsi alternativement la largeur **ou** la hauteur, selon flex-direction.

### Propriété #2 : Flex Grow

Maintenant, nous allons devenir un peu plus complexes.

Tout d'abord, définissons tous nos carrés à la même largeur, 120px :

![Image](https://cdn-media-1.freecodecamp.org/images/mOqzMCiRuivr30Lunbn5QhJPkIAXSe8phXe8)

Maintenant, en ce qui concerne la propriété appelée **flex-grow**, la valeur par défaut est **0**. Cela signifie que les carrés ne sont pas autorisés à grandir pour occuper l'espace dans le conteneur.

Que signifie cela ? Eh bien, essayons d'incrémenter flex-grow à **1** pour chaque carré :

![Image](https://cdn-media-1.freecodecamp.org/images/9xJ4cFVbLr3V-4yaAkg2lvO1jXEU6Bfm8BHe)

Les carrés occupent collectivement toute la largeur du conteneur, avec l'espace uniformément réparti entre eux. _La valeur flex-grow remplace la largeur._

La partie déroutante de flex-grow, cependant, est de savoir ce que la valeur signifie réellement. Que signifie réellement **flex-grow: 1** ?

Eh bien, voici à quoi cela ressemble si nous définissons le flex-grow de chaque carré à 999 :

![Image](https://cdn-media-1.freecodecamp.org/images/oJzGOF2s0NewsPEbRGZOBDVjxmt0kW6V2Vto)

C'est... exactement la même chose.

C'est parce que flex-grow n'est pas une valeur absolue — c'est une valeur relative.

Ce qui compte, ce n'est pas la valeur de flex-grow d'un carré prise isolément, mais _ce qu'elle est en relation avec les autres carrés._

Si nous définissons chaque carré à flex-grow: 1, puis ajustons le flex-grow du Carré #3, alors nous voyons les changements :

![Image](https://cdn-media-1.freecodecamp.org/images/duNzzISFc-oJJ4pFXr9OvCNwF46JawATpzrx)

Pour vraiment comprendre ce qui se passe ici, prenons une petite pause pour faire quelques (simples) mathématiques.

Chaque carré commence avec un flex-grow de 1. Si nous additionnons le flex-grow de chaque carré, notre total est de six. Le conteneur est ainsi divisé en 6 sections séparées. **Chaque carré grandit pour remplir 1/6 de l'espace disponible dans le conteneur.**

Lorsque nous définissons le flex-grow du Carré #3 à 2, le conteneur est maintenant divisé en **7** sections différentes, puisque le total des propriétés flex-grow est 1 + 1 + 2 + 1 + 1 + 1.

Le Carré #3 obtient alors 2/7 de cet espace, et les autres obtiennent 1/7.

Lorsque nous passons à flex-grow: 3 pour le Carré #3, le conteneur est divisé en 8 sections (1 + 1 + 3 + 1 + 1 + 1) et le Carré #3 obtient 3/8, et les autres obtiennent 1/8.

Et ainsi de suite.

**Flex-grow est une question de proportions**. Si nous définissons chaque carré à flex-grow: 4, et le carré #3 à flex-grow: 12, nous obtenons le même résultat que si c'était 1 et 3, respectivement :

![Image](https://cdn-media-1.freecodecamp.org/images/MSjVkzxK-p1w5dlRY9WdHibzxx81BCIHNC1S)

Ce qui compte, c'est ce que chaque carré flex-grow est _proportionnel aux autres._

En guise de note finale, rappelez-vous que tout comme flex-basis, flex-grow s'applique le long de l'axe principal. Nos carrés ne grandiront qu'en largeur, sauf si nous définissons la flex-direction sur colonne.

### Propriété #3 : Flex Shrink

Flex-shrink est l'opposé de flex-grow, déterminant combien un carré est autorisé à rétrécir.

Il n'entre en jeu que si les éléments doivent rétrécir pour s'adapter à leur conteneur — c'est-à-dire lorsque le conteneur est tout simplement trop petit.

Son utilisation principale est de spécifier quels éléments vous souhaitez rétrécir, et quels éléments vous ne souhaitez pas. Par défaut, chaque carré a un flex-shrink de 1 — ce qui signifie qu'il rétrécira à mesure que la boîte se contracte.

Voyons cela en action. Dans les GIF ci-dessous, les carrés ont un flex-grow de 1, donc ils remplissent le conteneur, et un flex-shrink de 1, donc ils sont autorisés à rétrécir à mesure qu'il le fait.

![Image](https://cdn-media-1.freecodecamp.org/images/C1klDRyn4YCjpqlCy1PvpBVp1q0LOyXVuktg)

Maintenant, définissons le flex-shrink du Carré #3 à 0. Il est interdit de rétrécir, donc bien qu'il grandisse pour s'adapter au conteneur, il refuse de descendre en dessous de sa largeur définie de 120px.

![Image](https://cdn-media-1.freecodecamp.org/images/RITwrqDlcobhm-nFslcJ4ItB3yXdJbXNcAjy)

La valeur par défaut pour flex-shrink est 1 — cela signifie que vos éléments rétréciront jusqu'à ce que vous leur disiez de ne pas le faire !

Encore une fois, flex-shrink est une question de proportions. Si une boîte a un flex-shrink de 6, et les autres ont un flex-shrink de 2, la première boîte rétrécira 3 fois plus vite que les autres, à mesure que l'espace se comprime.

Notez la formulation : le carré avec un flex-shrink 3 fois plus grand rétrécira 3 fois plus vite. **Cela ne signifie pas qu'il rétrécira à 1/3 de la largeur.**

Dans un instant, nous allons approfondir combien les choses rétrécissent et grandissent. Mais d'abord, passons à notre dernière propriété, et rassemblons tout.

### Propriété #4 : Flex

Flex est un raccourci pour grow, shrink et basis — le tout ensemble.

Il est défini par défaut à 0 (grow) 1 (shrink) et auto (basis).

Pour notre dernier exemple, simplifions à deux boîtes.

Voici leurs propriétés :

```
.square#one {  flex: 2 1 300px;}
```

```
.square#two {  flex: 1 2 300px;}
```

Les deux ont la même flex-basis. Cela signifie que s'il y a assez d'espace pour les deux (le conteneur fait 600px plus de la place pour les marges et le remplissage), ils feront tous les deux 300px de large.

Mais à mesure que la boîte grandit, le Carré 1 (avec le flex-grow le plus élevé) grandira deux fois plus vite. À mesure que la boîte se contracte, le Carré 2 (avec le flex-shrink le plus élevé) rétrécira deux fois plus vite.

Tout ensemble maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/05-bXAiCAQUBtI9Ve-RIWGfqiEMtmRGWIxwM)

#### Comment les choses rétrécissent et grandissent

Voici ce qui peut être déroutant : lorsque le Carré 1 grandit, il ne devient pas deux fois plus grand que le Carré 2. De même, lorsque le Carré 2 rétrécit, il ne devient pas la moitié de la taille du Carré 1 — même si le rapport de flex-shrink est de 2 à 1.

Ce n'est pas leur taille qui est de 2 à 1 ou de 1 à 2. _C'est leur taux de rétrécissement et de croissance._

#### Un peu de mathématiques

La taille de départ pour le conteneur est de 640px. Après avoir tenu compte d'un remplissage de 20px de chaque côté du conteneur, cela laisse assez de place pour que les deux carrés reviennent à leur flex-basis de 300px.

Lorsque le conteneur est défini à 430px, nous avons perdu **210px** d'espace. Le Carré 1, avec le flex-shrink de 1, perd **70px**. Le Carré 2, avec le flex-shrink de 2, perd **140px**.

Lorsque le conteneur rétrécit à 340px, nous avons maintenant perdu **300px** d'espace. Le Carré 1 perd **100px**, le Carré 2 perd **200px**.

L'espace perdu est divisé selon le rapport de leurs flex-shrinks respectifs (2 à 1).

C'est la même histoire avec flex-grow. Lorsque le conteneur grandit à 940px, et que nous avons gagné **300px** d'espace, le Carré 1 obtient un supplémentaire **200px**, et le Carré 2 obtient un supplémentaire **100px**.

**En ce qui concerne les propriétés flex, les proportions sont le nom du jeu.**

![Image](https://cdn-media-1.freecodecamp.org/images/gcKDE1w0DRxSmdxs5GtMNtKtNSvg9rBOTpJU)

Dans le GIF ci-dessus, vous pouvez voir comment la largeur s'ajuste selon les rapports, avec le delta (Δ) montrant la différence par rapport à la flex-basis.

### Conclusion

En guise de récapitulation finale : flex-basis contrôle la taille d'un élément le long de l'axe principal avant toute croissance ou rétrécissement. Flex-grow détermine combien il grandira en proportion des éléments frères, et flex-shrink détermine combien il rétrécira.

Nous avons quelques autres propriétés Flexbox à couvrir — restez à l'affût pour cela dans les semaines à venir.

Merci beaucoup pour votre lecture ! La réponse à ces articles a été écrasante. J'apprécie vraiment que tout le monde prenne le temps de lire, répondre, recommander et partager !

Si vous souhaitez voir un concept particulier (Flexbox ou autre) expliqué dans un article similaire, laissez une réponse ou tweetez-moi. Vous pouvez également me suivre sur [Twitter](https://twitter.com/scottdomes) et Medium (en cliquant sur le bouton suivre ci-dessous).