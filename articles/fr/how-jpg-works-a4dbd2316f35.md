---
title: Comment fonctionne le JPG
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-26T16:07:48.000Z'
originalURL: https://freecodecamp.org/news/how-jpg-works-a4dbd2316f35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1YlapM2olkIcSfsba31zPg.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: Mathematics
  slug: mathematics
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne le JPG
seo_desc: 'By Colt McAnlis

  The JPG file format was one of the most technologically impressive advancements
  to image compression to come on the scene in 1992. Since then, it’s been a dominant
  force in representation of photo quality images on the internet. And f...'
---

Par Colt McAnlis

Le format de fichier JPG était l'une des avancées technologiques les plus impressionnantes en matière de compression d'images à apparaître en 1992. Depuis lors, il a été une force dominante dans la représentation des images de qualité photo sur Internet. Et pour de bonnes raisons. Une grande partie de la technologie derrière le fonctionnement du JPG est exceptionnellement complexe et nécessite une compréhension approfondie de la manière dont l'œil humain s'adapte à la perception des couleurs et des contours.

Et puisque je m'intéresse à ce genre de choses (et vous aussi, si vous lisez ceci), je voulais décomposer le fonctionnement du codage JPG, afin que nous puissions mieux comprendre comment créer des fichiers JPG plus petits.

### L'ESSENTIEL

Le schéma de compression JPG est divisé en plusieurs phases. L'image ci-dessous les décrit à un niveau élevé, et nous allons parcourir chaque phase ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/qQ1MqV5RNe2rMk9DxFX2r6Kdgua2wgRqOiSM)

### Conversion de l'espace colorimétrique

L'un des principes clés de la compression de données _avec perte_ est que les capteurs humains ne sont pas aussi précis que les systèmes informatiques. Scientifiquement, l'œil humain n'a que la capacité physique de distinguer environ [10 millions de couleurs différentes](https://en.wikipedia.org/wiki/Color_vision). Cependant, il y a beaucoup de choses qui peuvent influencer la manière dont l'œil humain perçoit une couleur ; parfaitement illustré avec des [illusions de couleur](https://www.washingtonpost.com/news/wonk/wp/2015/02/27/12-fascinating-optical-illusions-show-how-color-can-trick-the-eye/), ou le fait que [cette robe](http://www.wired.com/2015/02/science-one-agrees-color-dress/) a brisé Internet. L'essentiel est que l'œil humain peut être facilement manipulé en ce qui concerne les couleurs qu'il perçoit.

La quantification est une forme de cet effet dans la compression d'images avec perte, cependant le JPG adopte une approche différente à cela : les [_modèles de couleur_](https://en.wikipedia.org/wiki/Color_model). Un [**espace colorimétrique**](https://en.wikipedia.org/wiki/Color_space) est une organisation spécifique des couleurs, et son **modèle de couleur** représente la formule mathématique de la manière dont ces couleurs sont représentées (par exemple, des triplets en RVB, ou des quadruplets en CMJN).

Ce qui est puissant dans ce processus, c'est que vous pouvez _convertir d'un modèle de couleur à un autre_, ce qui signifie que vous pouvez changer la représentation mathématique d'une couleur donnée, avec un ensemble complètement différent de valeurs numériques.

Par exemple, ci-dessous se trouve une couleur spécifique, et sa représentation dans les modèles de couleur RVB et CMJN, elles sont la même couleur pour l'œil humain, mais peuvent être représentées avec un ensemble différent de valeurs numériques.

![Image](https://cdn-media-1.freecodecamp.org/images/OnvMl4KzBJWq6gOK2SPkPoGbAlwDqqc4zNxM)

Le JPG convertit du RVB au modèle de couleur [Y,Cb,Cr](https://en.wikipedia.org/wiki/YCbCr) ; qui comprend la luminance (Y), le chroma bleu (Cb) et le chroma rouge (Cr). La raison en est que les expériences psycho-visuelles (aka comment le cerveau traite les informations que l'œil voit) démontrent que l'œil humain est plus sensible à la [luminance](https://en.wikipedia.org/wiki/Luminance) qu'à la [chrominance](https://en.wikipedia.org/wiki/Chrominance), ce qui signifie que nous pouvons négliger des changements plus importants dans la chrominance sans affecter notre perception de l'image. Ainsi, nous pouvons apporter des changements agressifs aux canaux CbCr avant que l'œil humain ne les remarque.

![Image](https://cdn-media-1.freecodecamp.org/images/6mkX2q2kbYcu8oZzUdVFDmAtG9AaBN-fElFR)

### Sous-échantillonnage

L'un des résultats intéressants de l'espace colorimétrique YCbCr est que les canaux Cb/Cr résultants ont moins de détails fins ; ils contiennent moins _d'informations_ que le canal Y.

En conséquence, l'algorithme JPG _redimensionne_ les canaux Cb et Cr pour qu'ils soient environ ¼ de leur taille originale (notez qu'il y a quelques nuances dans la manière dont cela est fait que je ne couvre pas ici...), ce qui est appelé _sous-échantillonnage_.

Ce qui est important à noter ici, c'est que le sous-échantillonnage est un processus de compression avec perte (vous ne pourrez pas récupérer les couleurs sources exactes, mais seulement une approximation proche), mais son impact global sur les composants visuels du cortex visuel humain est minimal. La luminance (Y) est là où se trouvent les éléments intéressants et puisque nous ne sous-échantillonnons que les canaux CbCr, l'impact sur le système visuel est faible.

![Image](https://cdn-media-1.freecodecamp.org/images/-znUHa8bzPEQl-Kkk7pjZGoYImvOqR66aHZV)

### Image divisée en blocs de 8x8 pixels

À partir de maintenant, le JPG effectue toutes les opérations sur des blocs de 8x8 pixels. Cela est fait parce que nous nous attendons généralement à ce qu'il n'y ait pas beaucoup de variance sur les blocs de 8x8, même dans des photos très complexes, il tend à y avoir une certaine similarité locale ; cette similarité est ce dont nous allons profiter lors de notre compression plus tard.

Il est intéressant de noter qu'à ce stade, nous introduisons l'un des premiers "artéfacts" courants du codage JPG. Le "sanglage des couleurs" est lorsque les couleurs le long des bords nets peuvent "sangler" de l'autre côté. Cela est dû au fait que les canaux de chrominance, qui expriment la couleur des pixels, ont vu chaque bloc de 4 pixels moyenné en une seule couleur, et certains de ces blocs traversent le bord net.

### Transformation en Cosinus Discrète

Jusqu'à présent, les choses ont été assez calmes. Les espaces colorimétriques, le sous-échantillonnage et le blocage sont des choses simples dans le monde de la compression d'images. Mais maintenant... maintenant, les vraies mathématiques apparaissent.

Le composant clé de la transformation DCT est qu'elle suppose que tout signal numérique peut être recréé en utilisant une combinaison de fonctions cosinus.

Par exemple, si nous avons ce graphique ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/nopZw-il6uckw6Y6BzwZeR7ECQ4JiuNjYjbl)

Vous pouvez voir qu'il s'agit en réalité d'une somme de cos(x)+cos(2x)+cos(4x)

![Image](https://cdn-media-1.freecodecamp.org/images/oIY6HNHnh-6ZFXhFC7h31SrqdQwTgQx93XW1)

Peut-être une meilleure illustration de cela est le _décodage_ réel d'une image, étant donné une série de fonctions cosinus sur un espace 2D. Pour montrer cela, je présente l'un des GIFs les plus incroyables sur Internet : le codage d'un bloc de 8x8 pixels en utilisant des cosinus dans un espace 2D :

![Image](https://cdn-media-1.freecodecamp.org/images/kLijP2Qp8DJiRAdxh4nFZ-CH0gtbC1bZPxj4)

Ce que vous regardez ici est la reconstruction d'une image (panneau le plus à gauche). À chaque image, nous prenons une nouvelle valeur de base (panneau de droite) et la multiplions par une valeur de poids (texte du panneau de droite) pour produire la contribution à l'image (panneau central).

Comme vous pouvez le voir, en sommant diverses valeurs de cosinus contre un poids, nous pouvons reconstruire notre image originale (assez bien...)

C'est le contexte fondamental de la manière dont la [Transformation en Cosinus Discrète](https://en.wikipedia.org/wiki/Discrete_cosine_transform) fonctionne. L'idée est que _n'importe quel_ bloc de 8x8 peut être représenté comme une somme de transformations en cosinus pondérées, à diverses fréquences. L'astuce de tout cela est de déterminer _quelles_ entrées de cosinus utiliser et comment elles doivent être pondérées ensemble.

Il s'avère que le problème du "_quels cosinus utiliser_" est assez simple ; après beaucoup de tests, un ensemble de valeurs de cosinus a été choisi pour produire les meilleurs résultats, ce sont nos _fonctions de base_ et visualisées dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/U9kFCMBRjEh8szwttgD2Da8wCMNFYFgRZm9d)

En ce qui concerne le problème du "_comment elles doivent être pondérées ensemble_", appliquez simplement (HA !) cette formule.

![Image](https://cdn-media-1.freecodecamp.org/images/8fXCBt8IZ50aqTGLoBEw3cFg6jMcNKu38HQt)

Je vous épargnerai la signification de toutes ces valeurs, vous pouvez les rechercher sur la [page wikipedia](https://en.wikipedia.org/wiki/JPEG).

Le résultat de base est que pour un bloc de 8x8 pixels dans chaque canal de couleur, l'application de la formule ci-dessus et des fonctions de base générera une nouvelle matrice de 8x8, qui représente les poids à utiliser lors de la reconstruction. Voici une illustration du processus :

![Image](https://cdn-media-1.freecodecamp.org/images/RY-LRchafokMirED3ITTC7eg66vaf0cwc0Qf)

Cette matrice, G, représente les poids de base à utiliser pour reconstruire l'image (la petite valeur décimale dans le coin inférieur droit de l'animation ci-dessus). Basiquement, pour chaque base, nous la multiplions par le poids dans cette matrice, additionnons le tout ensemble, et obtenons notre image résultante.

À ce stade, nous ne travaillons plus dans les espaces colorimétriques, mais plutôt directement avec la matrice G (poids de base), toute compression supplémentaire est effectuée directement sur cette matrice.

Le problème ici, cependant, est que nous avons maintenant converti des valeurs entières alignées sur des octets en nombres réels. Ce qui augmente effectivement notre information (passant de 1 octet à 1 float (4 octets)). Pour résoudre cela et commencer à produire une compression plus significative, nous passons à la phase de quantification.

### Quantification

Donc, nous ne voulons pas compresser les données en virgule flottante. Cela gonflerait notre flux et ne serait pas efficace. À cette fin, nous aimerions trouver un moyen de convertir la matrice des poids en valeurs dans l'espace [0,255]. Directement, nous pourrions faire cela en trouvant la valeur min/max de la matrice (-415,38 et 77,13, respectivement) et en divisant chaque nombre dans cette plage pour nous donner une valeur entre [0,1] à laquelle nous multiplions par 255 pour obtenir notre valeur finale.

Par exemple : [34,12 - -415,38] / [77,13 — -415,38] *255 = 232

Cela fonctionne, mais le compromis est une réduction significative de la précision. Cette mise à l'échelle produira une distribution inégale des valeurs, dont le résultat est une perte visuelle significative de l'image.

Au lieu de cela, le JPG prend une autre voie. Plutôt que d'utiliser la plage de valeurs dans la matrice comme valeur de mise à l'échelle, il utilise une matrice précalculée de facteurs de quantification. Ces QF n'ont pas besoin de faire partie du flux, ils peuvent plutôt faire partie du codec lui-même.

[Cet exemple](http://en.wikipedia.org/wiki/JPEG#Quantization) montre une matrice couramment utilisée de facteurs de quantification, une pour chaque image de base,

![Image](https://cdn-media-1.freecodecamp.org/images/WcY8WWftuLo7v2OaESHHvf7ui1ged-WZ3z-9)

Nous utilisons maintenant les matrices Q et G, pour calculer notre matrice de coefficients DCT quantifiée :

![Image](https://cdn-media-1.freecodecamp.org/images/wvhPZdb89o8S1W-lhSuRaYTVBA4gt4CkOtZ-)

Par exemple, en utilisant les valeurs G[0,0]=−415,37 et Q[0,0]=16 :

![Image](https://cdn-media-1.freecodecamp.org/images/5CO5bwBzT45Jb8JHs1pBKZ27RFkKANgh5wBx)

Résultant en une matrice finale de :

![Image](https://cdn-media-1.freecodecamp.org/images/a78idWouY9t1kbYP8lRRQRrSPBwR38L-gK3k)

Observez à quel point la matrice devient plus simple — elle contient maintenant un grand nombre d'entrées qui sont petites ou nulles, ce qui la rend beaucoup plus facile à compresser.

En tant qu'à-côté rapide, nous appliquons ce processus aux canaux Y, CbCr indépendamment, et à ce titre, nous avons besoin de deux matrices différentes : une pour Y, et l'autre pour les canaux C :

![Image](https://cdn-media-1.freecodecamp.org/images/5bhD9pdtD2KqunLqkKIlq5oPdIwlmtQ21ehG)

![Image](https://cdn-media-1.freecodecamp.org/images/oJk0tX7rbtvfEx1zY-xc2ziktSvqnwI1IOMn)

La quantification compresse l'image de deux manières importantes : premièrement, elle limite la plage effective des poids, diminuant le nombre de bits nécessaires pour les représenter. Deuxièmement, beaucoup des poids deviennent identiques ou nuls, améliorant la compression dans la troisième étape, le codage entropique.

Ainsi, la quantification est la source principale des artéfacts JPEG. Parce que les images dans le coin inférieur droit tendent à avoir les plus grands diviseurs de quantification, les artéfacts JPEG auront tendance à ressembler à des combinaisons de ces images. La matrice des facteurs de quantification peut être directement contrôlée en modifiant le niveau de "qualité" du JPEG, qui met à l'échelle ses valeurs vers le haut ou vers le bas (nous couvrirons cela dans une minute)

### Compression

À ce stade, nous sommes de retour dans le monde des valeurs entières et pouvons avancer avec l'application d'une étape de compression sans perte à nos blocs. En regardant nos données transformées, vous devriez remarquer quelque chose d'intéressant :

![Image](https://cdn-media-1.freecodecamp.org/images/r9fHl5FWEhoy4TpV1yl65-LdF5S2Busax14o)

À mesure que vous vous déplacez de la gauche supérieure vers la droite inférieure, la fréquence des zéros augmente. Cela ressemble à un suspect principal pour le codage par longueur de série. Mais les ordres ligne-majeure et colonne-majeure ne sont pas idéaux ici, car cela entrelacerait ces séries de zéros, plutôt que de les regrouper.

Au lieu de cela, nous commençons par le coin supérieur gauche et zigzaguons en diagonale à travers la matrice, allant et venant jusqu'à atteindre le coin inférieur droit.

![Image](https://cdn-media-1.freecodecamp.org/images/2q1G-swbNYbJki1cnxLFhA7j2VsFUyfuSC2A)

Le résultat de notre matrice de luminance, dans cet ordre, devient :

_−26,−3,0,−3,−2,−6,2,−4,1,−3,1,1,5,1,2,−1,1,−1,2,0,0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0_

Une fois les données dans ce format, les étapes suivantes sont simples : exécuter RLE sur la séquence, puis appliquer un encodeur statistique ([Huffman](https://www.youtube.com/watch?v=6rnF2Mo80x0&list=PLOU2XLYxmsIJGErt5rrCqaSGTMyyqNt2H&index=2) / [Arithmétique](https://www.youtube.com/watch?v=FdMoL3PzmSA&index=7&list=PLOU2XLYxmsIJGErt5rrCqaSGTMyyqNt2H) / ANS) sur les résultats.

Et Boom. Votre bloc est maintenant encodé en JPG.

### Comprendre le paramètre de qualité

Maintenant que vous comprenez comment les fichiers JPG sont réellement créés, il est utile de revisiter le concept du paramètre _qualité_ que vous voyez normalement lors de l'exportation d'images JPG depuis Photoshop (ou autre).

Ce paramètre, que nous appellerons q, est un entier de 1 à 100. Vous devriez considérer q comme une mesure de la qualité de l'image : des valeurs plus élevées de q correspondent à des images de meilleure qualité et à des tailles de fichier plus grandes.

**Cette valeur de qualité est utilisée pendant la phase de quantification, pour ajuster les facteurs de quantification de manière appropriée.** Ainsi, par poids de base, l'étape de quantification ressemble maintenant à _round(Gi,k / alpha*Qi,k)_

Où le symbole _alpha_ est créé en résultat du paramètre de qualité.

![Image](https://cdn-media-1.freecodecamp.org/images/-FKBFg1RRuWt9P058hCBVsLiM9mKtG0vshlU)

Lorsque alpha ou Q[x,y] est augmenté (rappelez-vous que de grandes valeurs d'alpha correspondent à des valeurs plus petites du paramètre de qualité q), plus d'informations sont perdues, et la taille du fichier **diminue**.

Ainsi, si vous voulez un fichier plus petit, au coût de plus d'artéfacts visuels, vous pouvez définir une valeur de qualité plus faible pendant la phase d'exportation.

![Image](https://cdn-media-1.freecodecamp.org/images/VXlYqSNrwgnq3JHL2x9ewrc962jxL-r6CMNm)

Remarquez ci-dessus, dans l'image de la plus faible qualité, comment nous voyons des signes clairs de l'étape de blocage, ainsi que de l'étape de quantification.

Probablement le plus important, c'est que _le paramètre de qualité varie en fonction de l'image_. Puisque chaque image est unique et présente différents types d'artéfacts visuels, la valeur Q sera également unique.

### Conclusion

Une fois que vous comprenez comment l'algorithme JPG fonctionne, quelques choses deviennent évidentes :

1. Obtenir la bonne valeur de qualité, par image, est important pour trouver le compromis entre la qualité visuelle et la taille du fichier.
2. Puisque ce processus est basé sur des blocs, les artéfacts auront tendance à se produire en bloc, ou en "grincement".
3. Puisque les blocs traités ne se mélangent pas les uns avec les autres, le JPG ignore généralement l'opportunité de compresser de grandes étendues de blocs similaires ensemble. Aborder cette préoccupation est quelque chose que le format WebP fait bien.

Et si vous voulez jouer avec tout cela par vous-même, toute cette folie peut être réduite à un [fichier d'environ 1000 lignes](https://github.com/richgel999/jpeg-compressor/pull/7/files?short_path=04c6e90).

#### HEY !

Vous voulez savoir comment rendre vos [fichiers JPG plus petits](https://medium.com/@duhroach/reducing-jpg-file-size-e5b27df3257c) ?

Vous voulez savoir comment fonctionnent les [fichiers PNG](https://medium.com/@duhroach/how-png-works-f1174e3cc7b7#.k84u38rna), ou comment [les rendre plus petits](https://medium.com/@duhroach/reducing-png-file-size-8473480d0476#.8prys6ckk) ?

Vous voulez plus de bonnes choses sur la compression de données ? [Achetez mon livre](http://shop.oreilly.com/product/0636920052036.do) !