---
title: Compression de données utilisant des images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T08:01:47.000Z'
originalURL: https://freecodecamp.org/news/data-compression-using-images-5eaede612c28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l0Zu6jD5IX6sjxMeNpuoXA.png
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Compression de données utilisant des images
seo_desc: 'By Dan Ruta

  The original motivation for this side-project was finding a better way to save and
  load weights trained by a browser based neural network, while developing jsNet.
  To save weights, as JSON, I would have to log the content out, in the conso...'
---

Par Dan Ruta

La motivation initiale pour ce projet secondaire était de trouver une meilleure façon de sauvegarder et de charger les poids entraînés par un réseau de neurones basé sur un navigateur, tout en développant [jsNet](https://github.com/DanRuta/jsNet). Pour sauvegarder les poids, sous forme de JSON, je devais enregistrer le contenu, dans la console ou sur la page, et comme vous pouvez l'imaginer, cela devenait assez compliqué lorsque les réseaux devenaient grands et qu'il y avait beaucoup de données.

La solution que j'ai trouvée a été d'encoder les données sous forme d'images, qui sont beaucoup mieux gérées que le texte JSON brut. Sans le vouloir, l'algorithme que j'ai utilisé pour cela semble non seulement avoir bien fonctionné, mais la taille finale du fichier était aussi petite que la compression gzip, la battant même dans la plupart des cas.

J'ai donc pensé polir et [publier](https://github.com/DanRuta/PNGArrays) cela en tant que bibliothèque autonome, pour une utilisation générale. Cet article sert de vue d'ensemble de l'algorithme de compression, pour ceux qui s'intéressent à ce genre de choses.

### L'Algorithme

Sans plus attendre, voici un bref aperçu de haut niveau de la conversion de tableau en image :

* Les nombres sont convertis en base 15, les premiers caractères étant des métadonnées
* Les résultats sont concaténés
* Chaque paire de caractères hexadécimaux est ensuite convertie en une valeur Uint8Clamped
* Enfin, cela est dessiné sur une toile, puis soit retourné (navigateur), soit sauvegardé dans un fichier (nodejs)

Quant à la conversion d'une image en données de tableau :

* L'image est lue soit à partir d'un fichier, d'un Uint8ClampedArray, soit à partir d'un élément HTML img
* Chaque valeur dans le Uint8ClampedArray est convertie en base 16
* Une fois concaténée en une chaîne, la sortie est divisée le long du caractère de métadonnées « f »
* Chaque chaîne hexadécimale est ensuite analysée pour être reconvertie en un nombre

Des étapes de normalisation supplémentaires et facultatives peuvent être effectuées avant et après les conversions, pour potentiellement réduire davantage la quantité de métadonnées, et donc la taille du fichier.

#### Les métadonnées

Si les nombres étaient convertis en base 16 (0 à f), ce que les images utilisent, il n'y aurait aucun moyen de différencier les valeurs séparées, une fois concaténées. Par conséquent, ils sont convertis en base 15 (0 à e), et le caractère f est utilisé comme délimiteur, pour séparer les valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/wClA7AqfH99FDleLbxUKjZY-UqsUeK0-beV3)
_Où la longue liste de données est divisée_

![Image](https://cdn-media-1.freecodecamp.org/images/Utj9cQNBYBgGwdANSOlNF7LUH71YXaDDTEIr)
_Les valeurs séparées, après la division_

À partir de là, un peu plus de métadonnées peuvent être nécessaires pour d'autres choses. Mais à partir de maintenant, cela peut être représenté en base 15, car c'est au début, ce qui signifie que nous n'avons pas besoin de plus de caractères uniquement pour les métadonnées.

**Positif ou négatif**
Le premier bit supplémentaire de métadonnées nécessaire est de savoir si le nombre est positif ou négatif. Ce serait cependant un gaspillage d'utiliser un caractère entier juste pour une valeur binaire, donc cela est fusionné dans les métadonnées pour savoir combien de caractères en base 15 stockent le côté gauche du nombre (à gauche de la virgule décimale).

Voir la section **Configurations** ci-dessous pour plus d'informations, mais par défaut, un seul caractère est utilisé pour encoder les deux, comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/54ixPs6sNAmnYhV3pjE5Wjdas0vb-XODMCWY)
_0–7 pour négatif, 8-e pour positif_

Les valeurs à 7 ou moins représentent un nombre négatif, tandis que le reste représente un nombre positif.

**Nombre de caractères en base 15 pour le côté gauche**
De plus, chacune des valeurs représente combien de caractères en base 15 sont utilisés pour représenter le côté gauche de la virgule décimale.

Par exemple, **3** représente un nombre négatif, avec 4 chiffres à gauche, comme _-1234.xyz_. Et **a** représente un nombre positif, avec 3 chiffres à gauche, comme _123.xyz_.

**Le nombre de zéros décimaux de tête**
Enfin, par défaut, le nombre de zéros de tête dans une valeur décimale est stocké. Encore une fois, voir la section **Configurations** ci-dessous, mais par défaut, 1 caractère est utilisé, permettant jusqu'à 15 zéros décimaux de tête, comme 0.0000000000000001.

Ainsi, avec les configurations par défaut, la valeur **1430.01623** serait convertie en ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/bF9EjCkQnIKXqZruKDPrQvhWLKvnmvGgi1rj)
_Fa1655733_

« F » est le délimiteur, « a » représente une valeur positive avec 3 caractères (655) représentant la partie gauche de la virgule décimale, le « 1 » représente 1 zéro de tête, dans 1430.**_0_**1623, et le reste représente la valeur réelle. Les trois premiers caractères, « 655 », sont convertis de la base 15 en 1430, et le reste, « 733 », est converti en 1623. Le résultat est concaténé, avec le zéro de tête ajouté.

#### Configurations

Par défaut, un seul caractère de métadonnées est utilisé pour encoder combien de caractères hexadécimaux sont utilisés pour représenter le côté gauche de la virgule décimale (655 => 1430, dans l'exemple ci-dessus). Cela fixe la limite à une valeur hexadécimale maximale de eeeeeee, qui est 170859374 en décimal. Bien que cela devrait suffire pour la plupart des cas, il est toujours possible de représenter plus, simplement en utilisant 2 caractères.

![Image](https://cdn-media-1.freecodecamp.org/images/MYbd-8ua090Q5OlZjXKQVvmGl1cdvnkm0iT6)
_F791655733_

Dans ce scénario, les nombres positifs sont stockés comme tout ce qui est au-dessus de 112, et les nombres négatifs comme tout ce qui est en dessous. Cela signifie qu'il y a un maximum théorique de 113 caractères hexadécimaux qui peuvent représenter le côté gauche du nombre, soit 7912473587054163204202262246064660222224606482062446620828868288862844044480028440444220620006824802826420808608284080640028606608644. Cependant, en pratique, l'arrondi de `parseInt` devient étrange après 15 caractères, donc 999999999999999 devrait être un point d'arrêt.

Mais, pour économiser encore plus d'espace, cette configuration peut être définie à 0, pour ignorer complètement ces métadonnées, si vous savez avec certitude que les nombres sont positifs et dans la plage 0–1 (vous pouvez toujours normaliser/dénormaliser en utilisant les fonctions d'assistance incluses). Ainsi, _0.123_ serait converti en :

![Image](https://cdn-media-1.freecodecamp.org/images/wnFehZUkLF5t0GCP8nl8AAH9J6gksedk87wR)
_F083_

Où « 83 » est la conversion hexadécimale de 123. Il n'y a pas de caractère stocké pour le côté gauche de la virgule décimale, car le nombre est supposé être 0.

Enfin, le caractère de métadonnées pour les zéros de tête peut également être activé ou désactivé, pour lorsque vos données consistent en entiers, ou au plus, en décimaux sans zéros de tête. Le désactiver pour l'exemple ci-dessus donnerait :

![Image](https://cdn-media-1.freecodecamp.org/images/vlUY8NWqqzh3tvZctNemH4ES0TyztGvxs1v3)
_F83_

C'est la configuration minimale, et avec un peu de prétraitement des données, elle peut aider à réduire considérablement la taille du fichier.

#### Benchmarks

Les deux formats les plus intéressants étaient PNG et WebP. Les deux peuvent être sauvegardés à partir d'une toile, et les deux peuvent utiliser le canal alpha, ce qui signifie qu'ils sont assez facilement interchangeables (au moins dans la version navigateur).

Comme le problème initial que je résolvais était les poids des réseaux de neurones, le premier ensemble de benchmarks concernait les poids de 3 réseaux de neurones, chacun quadruplant en taille, pour tester l'évolutivité, qui semblait non affectée. Les configurations ont été laissées par défaut, non optimisées.

![Image](https://cdn-media-1.freecodecamp.org/images/mqSrpZuSFulDN5oLnqvswKP3-4iuSvwDWoaq)
_Taille du fichier relative à la compression gzip_

Le format PNG fait le travail, mais WebP bat réellement gzip ! Presque... à 98,5 % de la taille, d'après ces 3 tests. L'utilisation du canal alpha n'a pas aidé à réduire la taille du fichier, mais elle a réduit la taille de l'image, en pixels, donc elle a été laissée comme une configuration activable.

Le prochain ensemble de benchmarks concerne la configuration de capacité. Pour cela, et l'ensemble suivant de tests, j'ai créé un tableau aléatoire de nombres dans la plage de 0 à 1, avec 1 décimale, par exemple : _0.1, 0.4, 0.7, 0.2_, et ainsi de suite, pour m'assurer que les données étaient valides pour toute configuration, et j'ai testé les variantes PNG et WebP, à partir de la sortie du navigateur. 80 000 nombres ont été utilisés pour ce benchmark.

![Image](https://cdn-media-1.freecodecamp.org/images/po7ntrJWjRArrBcfhXwIaKA5QL7tmnvrqbMk)
_Taille du fichier relative à gzip_

WebP a assez facilement battu le format PNG, et même gzip, lorsque la capacité était définie à 0, l'égalant lorsqu'elle était définie à 1, et légèrement plus grande lorsqu'elle était définie à 2.

Enfin, les tailles ont été comparées pour la configuration des zéros décimaux de tête, pour chaque configuration de capacité, pour le format WebP. Cette fois, un ensemble de 500 000 nombres a été utilisé, du même type que ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/FBqgimg6gs2QlxIG4vvYXZHz5Mvjusg-zf--)
_Taille du fichier relative à gzip_

Cette configuration particulière semble en fait faire pire sur la configuration de capacité la plus petite, mais légèrement mieux sur le reste.

Mon conclusion de ces tests est que si les données sont normalisées comme étape de prétraitement, et que vous pouvez utiliser le format WebP, il y a un potentiel pour une bien meilleure compression. Vous obtenez également quelques images assez cool :

![Image](https://cdn-media-1.freecodecamp.org/images/iYRRcKnxwJKTaIuP5UL7Ct1p2nMNGeUSqM6G)

![Image](https://cdn-media-1.freecodecamp.org/images/ACJ074tWqKwlE8CBMr1UOBec17Ij10KeOVfn)

![Image](https://cdn-media-1.freecodecamp.org/images/NcMgYS70Crx6uG1hOOffuCWhTf0c5l4BMb-C)

Les fichiers de benchmarks peuvent être trouvés dans [le dépôt](https://github.com/DanRuta/IMGArrays), sur GitHub.

#### Alors, qu'est-ce qui suit ?

Les contributions sont toujours les bienvenues, car j'adorerais améliorer cela, et obtenir une taille de fichier encore plus petite. À l'avenir, lorsque moi ou quelqu'un d'autre aura le temps, cela pourrait être porté vers WebAssembly, pour des gains de vitesse de conversion potentiels.

D'autres choses qui pourraient valoir la peine d'être ajoutées pourraient être une configuration « auto », pour déterminer toutes les configurations automatiquement, en parcourant d'abord les données, pour voir ce qui est réellement nécessaire.

Et enfin, pour éviter d'avoir à garder une trace des configurations, pour une utilisation lors de l'analyse de l'image, toutes les configurations pourraient être stockées dans la sortie encodée, sous forme de pixels « d'en-tête », derrière un délimiteur FF.

Mais pour l'instant, pour conclure, voici une image des poids pour un réseau de neurones entraîné à reconnaître des chiffres manuscrits ([MNIST](http://yann.lecun.com/exdb/mnist/)). En supposant que Medium n'applique aucune compression de leur côté, vous devriez pouvoir la charger en utilisant [jsNet](https://github.com/DanRuta/jsNet), dans une structure 784–100–10, et avoir un modèle entraîné, tout cela à partir d'une image PNG !

![Image](https://cdn-media-1.freecodecamp.org/images/MKYC2YV27sfNsvyhAdCrTjDquaEYlQHn-nir)
_Configuration par défaut_

La page GitHub pour cela est [ici](https://github.com/DanRuta/PNGArrays) et mon Twitter est [@Dan_Ruta](http://twitter.com/Dan_Ruta).