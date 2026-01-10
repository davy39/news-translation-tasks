---
title: D'où viennent tous les octets ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-12T19:39:33.000Z'
originalURL: https://freecodecamp.org/news/where-do-all-the-bytes-come-from-f51586690fd0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qimWOyFboQoLx32R.
tags:
- name: compression
  slug: compression
- name: Design
  slug: design
- name: Game Development
  slug: game-development
- name: Image Compression
  slug: image-compression
- name: learning
  slug: learning
seo_title: D'où viennent tous les octets ?
seo_desc: 'By Colt McAnlis

  Great question Dion! I will answer it, and not just because you’re my new boss,
  but because it’s a good question. (but also because you’re my new boss.)

  I want to set something clear here though : we’re not really comparing Apples-to-...'
---

Par Colt McAnlis

Excellente question Dion ! Je vais y répondre, et pas seulement _parce que_ tu es mon nouveau patron, mais parce que c'est une bonne question. (mais aussi parce que [tu es mon nouveau patron](https://medium.com/ben-and-dion/heading-to-google-take-2-0-153841c6e1ae#.asvmj5s45).)

Je veux cependant clarifier quelque chose ici : nous ne comparons pas vraiment des pommes avec des pommes, alors définissons d'abord quelques technologies.

### Comment Mario fonctionne

Parlons donc de la façon dont le jeu Super Mario original fonctionnait, du point de vue des ressources.

La console NES originale était conçue pour afficher des images de 256 pixels de large par 240 pixels de haut ; cela signifie que l'image finale devant être affichée à l'écran faisait 180 ko de taille.

En outre, la NES n'avait que 2 ko de RAM. Une cartouche pouvait contenir de 8 ko à 1 Mo de données de jeu. Il était donc impossible de charger l'intégralité du contenu du jeu en mémoire principale. En gros, un sous-ensemble des données de la cartouche de 1 Mo devait être chargé dans les 2 ko de RAM et utilisé pour rendre l'écran de 180 ko. Comment y parvenir ?

[Feuilles de sprites](https://en.wikipedia.org/wiki/Sprite_%28computer_graphics%29).

Les feuilles de sprites contiennent de petites tuiles graphiques, réutilisées encore et encore. Par exemple, voici une réinterprétation de la feuille de sprites originale de Super Mario :

![Image](https://cdn-media-1.freecodecamp.org/images/0*dwRaOKJJTu_i9TvZ.)
_Ce n'est pas la feuille de sprites originale exacte, mais vous pouvez vous faire une idée des petits blocs de données qui peuvent être utilisés encore et encore._

Chaque petit carré de 16x16 pixels représente une « tuile » et les artistes les assemblaient pour créer les niveaux réels. Les niveaux eux-mêmes devenaient un grand tableau 2D d'index pointant vers la feuille de sprites. (J'en parle en détail dans la Leçon 3 de mon [cours de développement de jeux HTML5 @ Udacity](https://www.udacity.com/course/html5-game-development--cs255), ou dans mon livre [HTML5 Game Development Insights](http://www.apress.com/9781430266976).) Ajoutez un peu de [Run-Length-Encoding](https://en.wikipedia.org/wiki/Run-length_encoding), ou un peu de [LZ77](https://www.youtube.com/watch?v=Jqc418tQDkg), et vous obtenez un format assez compact pour les niveaux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qimWOyFboQoLx32R.)
_Voici, ce niveau que vos parents n'ont jamais pu terminer._

Ainsi, avec des concepts comme les feuilles de tuiles et les feuilles de sprites, nous pouvons utiliser un petit ensemble d'images pour créer de grandes scènes et mondes. C'est généralement ainsi que fonctionnent la plupart des jeux. Même les jeux 3D auront un ensemble de textures communes appliquées plusieurs fois et à différents endroits dans le jeu lui-même.

Parlons maintenant de la compression générique des images.

### Comment les images sont compressées

Voici la partie « pas juste » de cette comparaison. Les algorithmes de compression d'images génériques n'ont aucune connaissance du domaine concernant les pixels qu'ils contiennent. JPG, PNG, WebP ont tous été conçus pour des _photos_ et non pour des _écrans de jeu_. Le résultat est que pour un bloc de pixels donné de 16x16, ces algorithmes supposent qu'il est unique dans l'image ; en dehors d'une quantification des couleurs, il n'y a pas de logique réelle ajoutée pour déterminer si un autre bloc de 16x16 pourrait être un _duplicata exact_ du bloc actuel. Cela signifie généralement qu'il existe une limite inférieure à la compression d'un bloc de données donné.

Par exemple, [JPG](https://en.wikipedia.org/wiki/JPEG) divise une image donnée en blocs de 8x8 pixels, convertit l'espace colorimétrique RVB en version [YCbCr](https://en.wikipedia.org/wiki/YCbCr), puis applique une [transformée en cosinus discrète](https://en.wikipedia.org/wiki/Discrete_cosine_transform) sur ces blocs. Ce n'est qu'**après** cette étape qu'un encodeur sans perte intervient pour voir s'il peut faire correspondre des groupes de doublons communs en utilisant DPCM ou RLE.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xdUjGXy1FE9sgpqE.)
_Une vue en blocs du fonctionnement de la compression JPG._

Ainsi, le seul endroit où deux blocs pourraient être compactés en un seul bloc est si leur version post-DCT est identique et que RLE peut faire des recommandations de pas. Cela n'arrive pas souvent.

[Malgré ses autres défauts](https://www.youtube.com/watch?v=jHXzzHElFPk), PNG est bien meilleur à cet égard. La compression PNG est entièrement sans perte (donc la qualité de votre image est élevée, mais vos économies de compression sont faibles), et basée sur le codec DEFLATE, qui associe [LZSS](https://www.youtube.com/watch?v=Jqc418tQDkg) avec [Compression Arithmétique](https://www.youtube.com/watch?v=FdMoL3PzmSA). Le résultat est que de longues séquences de pixels similaires peuvent être réduites à une taille beaucoup plus petite. C'est pourquoi une image avec un arrière-plan très uniforme sera toujours plus petite en PNG qu'en JPG.

#### L'image ci-dessous est un fichier PNG de 5,9 ko, tandis que l'image JPG est de 106 ko

![Image](https://cdn-media-1.freecodecamp.org/images/0*sUO8JCbLZc_i-524.)
_Car cette image contient de nombreux pixels dupliqués (le fond du ciel bleu), les compresseurs comme PNG font un meilleur travail que leurs homologues JPG basés sur des blocs._

### Pommes vs. Pitaya

Mon propos ici est qu'il est un peu injuste de comparer le contenu d'un jeu à une seule image sur Internet.

Du côté du jeu, vous commencez avec un petit ensemble de tuiles réutilisables et vous les indexez pour construire votre image plus grande, nous pouvons faire cela parce que nous savons comment le jeu va être fait. De l'autre côté, JPG/PNG/WebP essayent simplement de compresser les données qu'ils trouvent dans des blocs locaux, sans réel désir de faire correspondre le contenu répété. La compression d'image est clairement désavantagée ici, car ils n'ont pas de connaissance préalable de leur espace de données, ils ne peuvent pas vraiment faire d'hypothèses à ce sujet.

Je veux dire, considérons [La Scène Demo](https://en.wikipedia.org/wiki/Demoscene) qui est très axée sur [ce genre de chose](https://en.wikipedia.org/wiki/.kkrieger). Ils peuvent entasser 30 minutes d'un shooter 3D entier dans 64 ko parce qu'ils comprennent et savent beaucoup plus de choses sur leurs données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KFIQVD2tHQ3nu9GBEu3RWg.jpeg)
_Une comparaison bien plus pertinente. La démo [.kkrieger](https://en.wikipedia.org/wiki/.kkrieger" rel="noopener" target="_blank" title=") a réussi à caser 30 minutes de gameplay d'un shooter 3D, avec physique, son, textures et IA dans 64 ko de données. Cela semble être un gain massif pour seulement 24 ko de plus que le Mario original._

Cela montre simplement qu'avec la bonne quantité de connaissance préalable de vos données, vous pouvez faire de grandes choses avec la compression.

### Vers l'avenir.

Évidemment, nous avons évolué depuis les écrans de 256x240 de l'époque de la NES. [Le téléphone dans ma poche](https://www.google.com/nexus/5x/) a un écran de 1 920 x 1 080 pixels pour une taille de 5,2", ce qui lui donne une densité d'environ 423 pixels par pouce. Pour comparer cela en termes de pixels, cela représente ~33 écrans de Super Mario, ou plutôt, 8 Mo de données de pixels. Je ne pense pas que quiconque soit surpris que les résolutions d'écran augmentent, mais cela s'accompagne également du besoin de _plus de données_.

C'est quelque chose sur lequel [j'insiste depuis un certain temps](https://www.youtube.com/watch?v=dmX2MpEBYhw). Alors que nous obtenons des écrans plus grands, les canaux de contenu doivent augmenter leurs résolutions de sortie afin de toujours bien paraître sur nos configurations à haute densité (sinon, [nous obtenons un flou de mise à l'échelle...](http://www.leemunroe.com/designing-for-high-resolution-retina-displays/)). Cela, bien sûr, fait grossir la taille de nos jeux vidéo, de nos [pages web](http://royal.pingdom.com/2011/11/21/web-pages-getting-bloated-here-is-why/), et même de nos [vidéos YouTube en streaming](http://mashable.com/2014/01/03/youtube-4k-ces/). En gros, nous envoyons plus de données à des appareils plus petits simplement à cause de la résolution de l'écran. Ce qui, pour les 2 prochains milliards de personnes dans les marchés émergents, sur des connexions 2G, est comme la pire idée jamais.

Mais je m'égare. C'est un autre sujet.