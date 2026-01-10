---
title: 'Une introduction aux CSS Image Sprites : ils sont faciles à apprendre et utiles
  à connaître'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T19:22:07.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-css-image-sprites-theyre-easy-to-learn-and-great-to-know-c13beec82403
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pc6EbbKjoFzSbVCMiA8OOQ.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction aux CSS Image Sprites : ils sont faciles à apprendre
  et utiles à connaître'
seo_desc: 'By Zlatan Bekric

  Image sprites have been here since the 1970s. They were used for the first computer
  animations on Atari and other consoles. As time went on they were used less and
  less by front-end developers who wanted more advanced (read: realisti...'
---

Par Zlatan Bekric

Les sprites d'images existent depuis les années 1970. Ils étaient utilisés pour les premières animations informatiques sur Atari et d'autres consoles. Avec le temps, ils ont été de moins en moins utilisés par les développeurs front-end qui voulaient des graphismes plus avancés (c'est-à-dire réalistes) pour la 3D et la réalité virtuelle.

Cependant, ces dernières années, ils ont fait un retour.

_Sprite est un terme de graphisme informatique pour une image bitmap en deux dimensions qui est intégrée dans une scène plus grande._

Au cours des dernières années, Facebook, Twitter, Instagram et de nombreuses autres plateformes de médias sociaux ont connu une croissance fulgurante. Avec cette croissance est venue leur nécessité d'optimiser là où c'était possible et de réduire la taille des requêtes serveur. C'est alors que les sprites d'images CSS sont revenus dans le courant dominant.

Pour une plateforme comme Facebook — qui compte plus d'un milliard d'utilisateurs — l'affichage d'icônes, d'images et de contenus similaires nécessite plusieurs requêtes serveur. Ces requêtes surchargent inutilement le trafic.

### Que faire pour réduire les requêtes serveur et la bande passante ? Utiliser les sprites d'images CSS.

Au lieu de faire une requête pour votre image de profil, l'image de profil de votre ami, les miniatures de vos albums, etc., les sprites vous permettent d'utiliser une seule image, ce qui signifie une seule requête. Vous pouvez manipuler cette image pour afficher ces images comme des portions d'une image plus grande.

Prenons un exemple avec des drapeaux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pc6EbbKjoFzSbVCMiA8OOQ.png)
_Image originale_

Voyons maintenant comment cela fonctionne :

Comme vous pouvez le voir dans le code ci-dessus, nous avons configuré la base qui se compose de trois divs, où chaque div sera un porteur de sprite.

Tout d'abord, nous avons choisi le div avec l'ID de first. Notre div aura une taille de hauteur et de largeur qui sera affichée sur notre page. En arrière-plan, nous chargerons une image avec **URL ("https://i.postimg.cc/R0N7nkH9/flags.png")**.

La prochaine chose est de redimensionner notre image d'arrière-plan avec **background-size:1400px .** (Nous pouvons utiliser la taille réelle en pixels, le pourcentage, em ou rem.) Ce paramètre nous permettra de "zoomer" sur une image jusqu'au point où seule une certaine partie de l'image sera visible.

Enfin, les deux paramètres qui suivent **background:**

**URL("https://i.postimg.cc/R0N7nkH9/flags.png"),** déplaceront la portion de l'image principale, qui sera visible le long des axes X et Y. Ce qui signifie que dans ce cas **background:**

**URL("https://i.postimg.cc/R0N7nkH9/flags.png") -86px -87px;** nous afficherons la partie qui est décalée du haut de l'image de 87 pixels du haut et de 86 pixels de la gauche.

Le premier nombre (**-86px**) représente l'axe X où négatif signifie un déplacement de gauche à droite et positif signifie un déplacement de droite à gauche. Le second nombre (**-87px**) est utilisé pour le décalage du haut vers le bas, où les règles inversées s'appliquent, un nombre positif signifie un déplacement du bas vers le haut, et négatif bien sûr un déplacement du haut vers le bas.

Comme vous pouvez le voir sur l'image originale, le drapeau que nous avons obtenu (Bosnie) est effectivement le deuxième en partant du haut et le deuxième en partant de la gauche.

Assez bien ? OK, continuons.

Maintenant, remplissons le div avec un ID de second. Les mêmes règles de configuration s'appliqueront et le seul changement sera que dans ce cas, nous resterons sur l'axe X d'origine **(0px),** et la direction Y ira de la partie inférieure vers le haut **(89px).** Encore une fois, si vous vérifiez l'image originale, vous pouvez voir que (Ouzbékistan) est le premier en partant du bas et le premier en partant de la gauche.

Et enfin, mais non des moindres...

Oui, enfin, nous remplissons le dernier div avec un ID de third. Les règles sont les mêmes, et si vous avez deviné que nous nous sommes déplacés du bas vers le haut, eh bien c'est vrai.

Maintenant, le moment de vérité...

Dans le cas ci-dessus, nous nous déplacions le long des axes X et Y pour afficher certaines portions de l'image avec des drapeaux. En allant de droite à gauche et vers le bas, nous avons obtenu la Bosnie (axe X), en allant du bas et de la gauche (axe Y), nous avons obtenu la Thaïlande et l'Ouzbékistan. Comme vous l'avez vu, nous utilisons une seule image, ce qui signifie une seule requête pour une image.

Il est important de savoir que lorsque vous construisez les sprites, l'image de base doit avoir les mêmes portions d'images à l'intérieur, pour votre propre commodité. Comme dans ce cas où nous nous déplaçons vers la gauche et la droite, le haut et le bas, par la taille de la portion plus l'espace blanc. L'Ouzbékistan (89px) et la Thaïlande (178px) ont une différence de 89px qui est leur taille réelle (87px) plus l'espace blanc (1px + 1px).

### Oui, vous pouvez aussi faire des animations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hnEOIUREyM1xmpIxNntrcg.png)
_Image originale_

Pour réaliser ce style d'animations old school, nous avons seulement besoin des propriétés d'animation CSS. Dans ce cas, nous avons déplacé l'image originale le long de l'axe X, et nous obtenons cette animation old style. Croyez-moi, avec les sprites, il n'y a pas de limites.

C'est aussi simple que cela :)

J'espère que vous avez apprécié la lecture de cet article.

Restez à l'écoute pour plus...

![Image](https://cdn-media-1.freecodecamp.org/images/1*tEK16gxQMCiapg2WWIz2Uw.png)