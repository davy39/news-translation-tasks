---
title: Le positionnement CSS expliqué en construisant un sundae à la glace
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-27T05:27:06.000Z'
originalURL: https://freecodecamp.org/news/css-positioning-explained-by-building-an-ice-cream-sundae-831cb884bfa9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gOT0k2y6W0gRYEylFp0cxQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Le positionnement CSS expliqué en construisant un sundae à la glace
seo_desc: 'By Kevin Kononenko

  If you’ve made an ice cream sundae before, then you can understand CSS positioning.

  Your divs are zooming around the screen like Roman candles.

  They’re diving deep into their container, then coming back up to the surface like
  a wha...'
---

Par Kevin Kononenko

#### Si vous avez déjà fait un sundae à la glace, alors vous pouvez comprendre le positionnement CSS.

Vos divs se déplacent à travers l'écran comme des fusées.

Elles plongent profondément dans leur conteneur, puis remontent à la surface comme une baleine.

Elles poussent les autres éléments hors du chemin, puis quittent complètement le conteneur comme un homme d'affaires impatient.

Et d'une manière ou d'une autre, cela se produit d'une nouvelle manière excitante chaque fois que vous changez cette ligne de CSS désagréable : la [propriété position](https://developer.mozilla.org/en-US/docs/Web/CSS/position).

Chaque personne qui a appris le CSS est passée par là. Le positionnement CSS semble être nonsensique jusqu'à ce que des heures d'essais et d'erreurs vous donnent enfin une compréhension vague.

Cet article mettra fin à la confusion, une fois pour toutes. La propriété position ne semble pas avoir de relation évidente avec un concept du monde réel... jusqu'à ce que vous considériez le modeste sundae à la glace.

Nous couvrirons les propriétés de position suivantes :

* Absolute
* Static (par défaut)
* Fixed
* Relative

![Image](https://cdn-media-1.freecodecamp.org/images/1*XDzlibMEpQuEbSi685SOzg.png)

Et, pour plus de clarté, un sundae à la glace sera composé de 4 composants principaux :

* Le verre
* Les boules de glace
* La crème fouettée
* Les cerises

### Le Sundae à la Glace en HTML

Si vous deviez expliquer la structure d'un sundae à la glace avec du HTML, cela ressemblerait probablement à ceci.

Ou, sous forme d'image :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pvC4ymGkc2rr8O53vdhzLA.png)

Avant de plonger dans le CSS, nous pouvons faire quelques observations :

1. Le nombre de boules de glace est limité par la hauteur du verre. Nous ne pouvons pas continuer à empiler des boules de glace indéfiniment. Finalement, tout ce bel ensemble basculerait.
2. Vous pouvez mettre les cerises où bon vous semble. Les cerises n'obéissent pas au flux et à l'empilement des boules. Elles sont plus petites et peuvent se loger dans des recoins où vous ne pouvez pas mettre une boule de glace. Et, de plus, ajouter des cerises ne perturbera pas l'ordre des boules.
3. La crème fouettée se trouve toujours sur le dessus, peu importe le nombre de boules. Avez-vous déjà vu un sundae à la glace avec la crème fouettée au milieu et rien sur le dessus ? Moi non plus.

### Position Relative/Static : Le Verre et les Boules

Comme montré dans la première image, notre tour penchée de glace ne peut contenir que 5 boules avant de basculer. Disons que ces 5 boules ont une hauteur totale de 500 pixels, et que chaque boule est directement empilée sur l'autre. Notre div fullSundae, dans ce cas, aurait une hauteur de 500px pour indiquer qu'elle ne peut contenir que ces 5 boules, et pas plus. C'est un exemple de la **position par défaut, static**. Nous l'utilisons pour montrer que la hauteur n'est pas liée à une div conteneur.

La chose simple à faire ensuite serait de donner à chaque iceCreamScoop une hauteur de 100px, ce qui correspondrait à la hauteur de la div fullSundae. Cela ne serait pas amusant, car la div glass serait de 300px par défaut. Regardons cela d'une autre manière.

Puisque la div glass contient trois des cinq boules, et que toutes les boules ont la même hauteur, nous pouvons voir que la div glass représente 60% de la hauteur de la div fullSundae. C'est une opportunité pour la **position relative** ! Vous pouvez définir la div glass en position relative et lui donner une hauteur de 60%. La div glass regardera la hauteur de la div fullSundae entière et occupera 60% de cet espace. Le pourcentage est relatif à la hauteur de la div conteneur, qui a été explicitement définie à 500px.

Vous pouvez aller encore plus loin. Si vous définissez chaque iceCreamScoop dans la div glass en **position relative**, chaque boule calculera sa hauteur en fonction de la hauteur de la div glass. Le verre peut contenir trois boules, donc chaque boule doit avoir une hauteur de 33,3%. Voici tout cela en code.

### Position Fixed : La Crème Fouettée

La position fixed devrait être la plus facile. Un élément en **position fixed** restera en place peu importe à quel point le body s'étend. En termes de glace, c'est la crème fouettée sur le dessus. Peu importe le nombre de boules de glace que vous essayez d'empiler, la crème fouettée sera toujours sur le dessus, avec la même relation exacte avec les boules. Elle est positionnée par rapport au body, et non à la div conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lp3sSuQHCV9zq_XEsfjGBw.png)

La crème fouettée est indépendante de la série de boules de glace. La quantité de crème fouettée n'affecte pas le nombre maximum de boules que vous pouvez avoir dans le sundae complet. Elle reste à un endroit constant sur la page.

Vous voyez souvent la position fixed dans les en-têtes et les pieds de page. Ce sont les éléments qui restent en place, même lorsque vous faites défiler la page ou la div.

### Position Absolute : Les Cerises

Il y a une raison pour laquelle j'ai gardé la Position Absolute pour la fin : elle peut conduire à un code difficile à maintenir si vous l'utilisez trop fréquemment. Vous avez été averti. Mais, elle fonctionne parfaitement pour les cerises dans cet exemple.

Vous pouvez mettre des cerises presque n'importe où dans ce sundae à la glace. Vous pouvez en mettre un tas sur le dessus, et cela ne basculera pas. Vous pouvez les coincer dans le verre lui-même, et vous pourrez toujours mettre la même quantité de glace. Elles n'obéissent pas aux mêmes règles que les éléments en position static et position relative. De plus, vous pouvez les retirer sans perturber aucun autre élément.

Ce sont les composants clés de la **position absolute**. Les éléments en position absolute ne perturbent pas le placement des autres éléments, mais vous devez indiquer leur position explicitement. Si vous ne le faites pas, ils se positionnent par défaut dans le coin supérieur gauche du body. Ou, si l'un de leurs parents a une position relative, ils vont dans le coin supérieur gauche de cette div.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZoRoAU2rrzf5IdHuz-xmtg.png)

Regardez ce sundae rempli de cerises. Il y a des cerises ajoutées à plusieurs endroits, et elles ne perturbent pas le flux des autres éléments. Mais, gardez à l'esprit que vous ne pouvez pas empiler les cerises comme vous empilez les boules de glace. Les cerises ne s'empilent pas. Vous devez placer chacune explicitement.

Une dernière note : la position absolute est calculée en fonction du parent le plus proche qui n'est PAS en position static. Si tous les parents sont en position static, elle est calculée en fonction de l'ensemble du body. Donc, dans le cas ci-dessus, les cerises dans le verre sont positionnées en fonction de la hauteur de la div glass, et non en fonction de la hauteur de la div fullSundae. La div glass a une position relative.

Maintenant, allez pratiquer, et quand vous vous sentirez un peu plus à l'aise... vous méritez une glace !

EDIT : Vous pouvez maintenant construire un sundae à la glace avec le positionnement CSS dans ce [tutoriel interactif](https://www.rtfmanual.io/csssundae/) !

Avez-vous aimé cet article ? Donnez-lui un "cœur" pour qu'il puisse aider les autres aussi !

[_Cet article est initialement paru sur le blog CodeAnalogies_](https://blog.codeanalogies.com/2016/08/27/css-positioning-explained-by-building-an-ice-cream-sundae/)_.