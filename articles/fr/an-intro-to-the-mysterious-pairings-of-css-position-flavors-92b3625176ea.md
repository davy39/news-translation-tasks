---
title: Une introduction aux mystérieux appariements des saveurs de position CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-16T16:16:20.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-the-mysterious-pairings-of-css-position-flavors-92b3625176ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LLCPNx0V3gV4bhsPgjR0Xw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction aux mystérieux appariements des saveurs de position CSS
seo_desc: 'By Anabella Spinelli

  Ever since I started learning about web development I found CSS positioning to be
  a mixture of mysterious co-dependant properties whose interactions and influences
  I never quite understood. Like most newbies, I just juggled aroun...'
---

Par Anabella Spinelli

Depuis que j'ai commencé à apprendre le développement web, j'ai trouvé le positionnement CSS être un mélange de propriétés mystérieuses et codépendantes dont les interactions et les influences n'ont jamais été tout à fait comprises. Comme la plupart des débutants, je me suis contentée de jongler avec `position`, `display`, `float`, `clear`, et toutes leurs combinaisons possibles de valeurs jusqu'à ce que cela ressemble à ce que je voulais.

C'est ainsi que fonctionne CSS, n'est-ce pas ?

Maintenant, après quelques années de concentration sur les tests d'API, je voulais revisiter ce vieux CSS vanilla et essayer de vraiment comprendre ces propriétés de mise en page de base, tout en essayant de comprendre ce que font les jeunes branchés de nos jours et de sauter à nouveau dans le train du développement.

C'est ma première étape : position.

#### Faire connaissance avec les propriétés

La propriété `position` peut être une chose mystérieuse à rencontrer lorsque vous commencez à apprendre le CSS. C'est comme si on vous donnait un ensemble d'épices inconnues qui se ressemblent, mais qui ont des saveurs très différentes et dont les combinaisons ne fonctionnent pas toujours comme prévu.

Ceci est une tentative de décrire les meilleurs et les plus courants _appariements_ entre eux afin que vous puissiez les appliquer facilement dans vos premières étapes de cuisine web. Tout comme nous apprenons dans la cuisine — le persil va bien avec l'ail, mais pas tellement avec la cannelle.

Tout d'abord, définissons à quoi ressemble chaque variante de position :

* `static` **:** c'est ce que chaque élément HTML a par défaut. Cela signifie que l'élément sera positionné selon le **flux normal du document**. C'est essentiellement le _sel_ de tous.
* `relative` **:** les éléments avec une position relative peuvent être placés _relativement_ à l'espace qu'ils occuperaient dans le flux normal du document. Ils font toujours partie du flux du document, mais supportent les propriétés `top, right, bottom et left`. Quelles que soient les valeurs que vous attribuez à ces propriétés, elles seront calculées en utilisant sa position et ses limites naturelles comme référence. Comme ajouter un peu de poivre, cela ne fait pas beaucoup de mal.
* `absolute` **:** celui-ci est délicat — c'est un peu comme le cumin, il peut être un très bon ajout, mais vous devez l'utiliser avec précaution. Les éléments absolus sont **retirés du flux normal du document**. Cela signifie qu'ils n'affectent pas et ne sont pas affectés par d'autres éléments de la page. Cependant, ils seront placés _relativement_ (oui, je sais, restez avec moi) à leur ancêtre `positionné` le plus proche. Cela signifie que n'importe quel élément parent dont la _position est explicitement définie_. Il peut être ajusté finement en utilisant `top, right, bottom et left`. Donc, c'est similaire au positionnement relatif, mais, comme il ne fait plus partie du flux du document, il utilise un parent comme référence.
* `fixed` **:** ah, celui-ci est facile. Les éléments fixes ne font pas partie du flux du document et leur position est basée sur toute la fenêtre, parfois appelée _viewport_. De plus, ils ne sont pas affectés par le défilement.

#### Alors, comment pouvons-nous les mélanger ?

Utilisez `position: relative;` chaque fois que vous voulez décaler un élément un peu de l'endroit où il serait normalement, mais vous ne voulez pas que tout le reste bouge avec lui. N'oubliez pas que tous les autres éléments se comporteront comme s'il n'avait pas bougé.

Utilisez `position: absolute;` lorsque vous vous souciez de l'endroit où se trouve l'élément par rapport à son parent ou à son conteneur avec une position, dans cet exemple, `relative`. Notez pour cela que la propriété `position` ne se cascade pas, donc cela utilisera le parent le plus proche avec une déclaration _relative explicite_. Si vous voulez forcer la cascade de cette propriété, vous pouvez la déclarer comme `position: inherit;`.

Gardez à l'esprit que la position de cet élément est définie par la taille et la forme de ses parents relatifs, donc si vous changez cela, cet élément pourrait être affecté aussi.

Enfin, `position: fixed;` est une chose amusante avec laquelle jouer. Les utilisations normales incluent les barres de navigation collantes, les pieds de page ou les menus latéraux. N'oubliez pas qu'il est hors du flux normal du document, donc cela signifie :

* vous pouvez le placer où vous voulez et rien d'autre ne se cassera
* cela signifie aussi qu'il ne fera rien d'autre que ce que vous ne lui dites pas explicitement de faire, donc vous devez définir ses 2 coordonnées pour qu'il apparaisse du tout.
* ces 2 coordonnées (à savoir, `top` ou `bottom`, plus `left` ou `right`) seront mesurées à partir du bord de la fenêtre.

Il y a une autre option que je n'ai pas couverte : `position: sticky`. Cela fait en sorte que les éléments se comportent et défilent normalement, puis collent à une certaine position tandis que le reste du contenu continue à défiler. J'ai décidé de la laisser de côté, car elle est encore expérimentale et dépasse le cadre _comprendre les bases_ de cet article. Mais, si vous êtes curieux, [voici](https://alligator.io/css/position-sticky/) un lien montrant de quoi il s'agit.

_J'espère que vous avez apprécié la lecture et appris quelque chose en cours de route. Si vous avez des commentaires ou des retours, j'adorerais les lire._