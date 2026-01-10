---
title: Comprendre les réseaux de capsules — La nouvelle architecture séduisante de
  l'IA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T09:22:41.000Z'
originalURL: https://freecodecamp.org/news/understanding-capsule-networks-ais-alluring-new-architecture-bdb228173ddc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e2Y2V1vCy6oo5Of7x0guUA.jpeg
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comprendre les réseaux de capsules — La nouvelle architecture séduisante
  de l'IA
seo_desc: 'By Nick Bourdakos

  Convolutional neural networks have done an amazing job, but are rooted in problems.
  It’s time we started thinking about new solutions or improvements — and now, enter
  capsules.

  Previously, I briefly discussed how capsule networks co...'
---

Par Nick Bourdakos

Les réseaux de neurones convolutifs ont fait un travail incroyable, mais ils sont ancrés dans des problèmes. Il est temps de commencer à réfléchir à de nouvelles solutions ou améliorations — et maintenant, voici les capsules.

Précédemment, j'ai brièvement discuté de la manière dont les [réseaux de capsules](https://hackernoon.com/capsule-networks-are-shaking-up-ai-heres-how-to-use-them-c233a0971952) combattent certains de ces problèmes traditionnels. Au cours des derniers mois, je me suis immergé dans tout ce qui concerne les capsules. Je pense qu'il est temps que nous essayions tous de mieux comprendre comment les capsules fonctionnent réellement.

Pour faciliter le suivi, j'ai construit un outil de visualisation qui vous permet de voir ce qui se passe à chaque couche. Cela est associé à une implémentation simple du réseau. Tout cela peut être trouvé sur GitHub [ici](https://github.com/bourdakos1/CapsNet-Visualization).

Voici l'architecture CapsNet. Ne vous inquiétez pas si vous ne comprenez pas encore ce que tout cela signifie. Je vais le parcourir couche par couche, avec autant de détails que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/Op1KJBfyIbUzHSC0vkoRJvjH3ocLz0JHkGQa)

### Partie 0 : L'entrée

L'entrée dans CapsNet est l'image réelle fournie au réseau de neurones. Dans cet exemple, l'image d'entrée fait 28 pixels de haut et 28 pixels de large. Mais les images sont en réalité en 3 dimensions, et la 3ème dimension contient les canaux de couleur.

L'image dans notre exemple n'a qu'un seul canal de couleur, car elle est en noir et blanc. La plupart des images que vous connaissez ont 3 ou 4 canaux, pour le Rouge-Vert-Bleu et éventuellement un canal supplémentaire pour l'Alpha, ou la transparence.

![Image](https://cdn-media-1.freecodecamp.org/images/JsT7hjCCcZeqgMPdCwsIm0kZM0mZyI9CmJpJ)

Chacun de ces pixels est représenté par une valeur de 0 à 255 et stocké dans une matrice 28x28x1 [28, 28, 1]. Plus le pixel est brillant, plus la valeur est grande.

### Partie 1a : Convolutions

La première partie de CapsNet est une couche de convolution traditionnelle. Qu'est-ce qu'une couche de convolution, comment fonctionne-t-elle et quel est son but ?

Le but est d'extraire certaines caractéristiques extrêmement basiques de l'image d'entrée, comme des bords ou des courbes.

Comment pouvons-nous faire cela ?

Réfléchissons à un bord :

![Image](https://cdn-media-1.freecodecamp.org/images/-9bmuVavZCvlaCXQ4MbGOtmoVhbiNW46gVmk)

Si nous regardons quelques points sur l'image, nous pouvons commencer à repérer un motif. Concentrez-vous sur les couleurs à gauche et à droite du point que nous regardons :

![Image](https://cdn-media-1.freecodecamp.org/images/dflKsJkPVCdZEX4IxiL8-AWo-rEx57UzGSgu)

Vous pourriez remarquer qu'ils ont une différence plus grande si le point est un bord :

```
255 - 114 = 141
114 - 153 = -39
153 - 153 = 0
255 - 255 = 0
```

Que se passerait-il si nous passions chaque pixel de l'image et remplacions sa valeur par la valeur de la différence des pixels à gauche et à droite ? En théorie, l'image devrait devenir entièrement noire sauf pour les bords.

Nous pourrions faire cela en bouclant à travers chaque pixel de l'image :

```py
for pixel in image {
  result[pixel] = image[pixel - 1] - image[pixel + 1]
}
```

Mais ce n'est pas très efficace. Nous pouvons plutôt utiliser quelque chose appelé une "convolution". Techniquement parlant, c'est une "corrélation croisée", mais tout le monde aime les appeler des convolutions.

Une convolution fait essentiellement la même chose que notre boucle, mais elle tire parti des mathématiques matricielles.

Une convolution est effectuée en alignant une petite "fenêtre" dans le coin de l'image qui ne nous permet de voir que les pixels de cette zone. Nous faisons ensuite glisser la fenêtre sur tous les pixels de l'image, en multipliant chaque pixel par un ensemble de poids puis en additionnant toutes les valeurs qui se trouvent dans cette fenêtre.

Cette fenêtre est une matrice de poids, appelée un "noyau".

Nous ne nous intéressons qu'à 2 pixels, mais lorsque nous enveloppons la fenêtre autour d'eux, elle encapsulera le pixel entre eux.

```
Fenêtre :
┌─────────────────────────────────────────┐
│ left_pixel middle_pixel right_pixel │
└─────────────────────────────────────────┘
```

Pouvez-vous penser à un ensemble de poids que nous pouvons multiplier par ces pixels afin que leur somme soit égale à la valeur que nous recherchons ?

```
Fenêtre :
┌─────────────────────────────────────────┐
│ left_pixel middle_pixel right_pixel │
└─────────────────────────────────────────┘
(1 * 255) + (0 * 255) + (-1 * 114) = 141
```

Avec ces poids, notre noyau ressemblera à ceci :

```py
noyau = [1  0 -1]
```

Cependant, les noyaux sont généralement carrés — nous pouvons donc le remplir avec plus de zéros pour qu'il ressemble à ceci :

```py
noyau = [
  [0  0  0]
  [1  0 -1]
  [0  0  0]
]
```

Voici un joli gif pour voir une convolution en action :

![Image](https://cdn-media-1.freecodecamp.org/images/rqyFdp9d5FoE45uEXUQ2aBJO0o9VXTDQJgK3)

**Note :** La dimension de la sortie est réduite par la taille du noyau plus 1. Par exemple : `(7 — 3) + 1 = 5` (plus d'informations à ce sujet dans la section suivante)

Voici à quoi ressemble l'image originale après avoir effectué une convolution avec le noyau que nous avons créé :

![Image](https://cdn-media-1.freecodecamp.org/images/AGSh8yNcivMnI6qWMg8Bv-oXzlDt0iJq1Tbn)

Vous pourriez remarquer que certains bords sont manquants. Plus précisément, les horizontaux. Pour les mettre en évidence, nous aurions besoin d'un autre noyau qui regarde les pixels au-dessus et en dessous. Comme ceci :

```py
noyau = [
  [0  1  0]
  [0  0  0]
  [0 -1  0]
]
```

De plus, ces deux noyaux ne fonctionneront pas bien avec les bords d'autres angles ou les bords qui sont flous. Pour cette raison, nous utilisons de nombreux noyaux (dans notre implémentation CapsNet, nous utilisons 256 noyaux). Et les noyaux sont normalement plus grands pour permettre plus de marge de manœuvre (nos noyaux seront de 9x9).

Voici à quoi ressemblait l'un des noyaux après l'entraînement du modèle. Ce n'est pas très évident, mais il s'agit simplement d'une version plus grande de notre détecteur de bords qui est plus robuste et ne trouve que les bords qui passent du clair au foncé.

```py
noyau = [
  [ 0.02 -0.01  0.01 -0.05 -0.08 -0.14 -0.16 -0.22 -0.02]
  [ 0.01  0.02  0.03  0.02  0.00 -0.06 -0.14 -0.28  0.03]
  [ 0.03  0.01  0.02  0.01  0.03  0.01 -0.11 -0.22 -0.08]
  [ 0.03 -0.01 -0.02  0.01  0.04  0.07 -0.11 -0.24 -0.05]
  [-0.01 -0.02 -0.02  0.01  0.06  0.12 -0.13 -0.31  0.04]
  [-0.05 -0.02  0.00  0.05  0.08  0.14 -0.17 -0.29  0.08]
  [-0.06  0.02  0.00  0.07  0.07  0.04 -0.18 -0.10  0.05]
  [-0.06  0.01  0.04  0.05  0.03 -0.01 -0.10 -0.07  0.00]
  [-0.04  0.00  0.04  0.05  0.02 -0.04 -0.02 -0.05  0.04]
]
```

**Note :** J'ai arrondi les valeurs car elles sont assez grandes, par exemple `0.01783941`

Heureusement, nous n'avons pas à choisir à la main cette collection de noyaux. C'est ce que fait l'entraînement. Les noyaux commencent tous vides (ou dans un état aléatoire) et continuent à être ajustés dans la direction qui rend la sortie plus proche de ce que nous voulons.

Voici à quoi ressemblaient les 256 noyaux (je les ai colorés comme des pixels pour qu'ils soient plus faciles à digérer). Plus les nombres sont négatifs, plus ils sont bleus. 0 est vert et positif est jaune :

![Image](https://cdn-media-1.freecodecamp.org/images/Y8IabW01OPBRTqQWsAWB2P3Hf8hAAGHmmWHo)
_256 noyaux (9x9)_

Après avoir filtré l'image avec tous ces noyaux, nous obtenons une pile de 256 images de sortie.

### Partie 1b : ReLU

ReLU (formellement connu sous le nom de Rectified Linear Unit) peut sembler compliqué, mais c'est en réalité assez simple. ReLU est une fonction d'activation qui prend une valeur. Si elle est négative, elle devient zéro, et si elle est positive, elle reste la même.

En code :

```py
x = max(0, x)
```

Et sous forme de graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/JhWsW6xuVqhqPP-sZxcjYQaxQtBvAo8C9QPZ)

Nous appliquons cette fonction à toutes les sorties de nos convolutions.

Pourquoi faisons-nous cela ? Si nous n'appliquons pas une sorte de fonction d'activation à la sortie de nos couches, alors l'ensemble du réseau de neurones pourrait être décrit comme une fonction linéaire. Cela signifierait que tout ce que nous faisons est un peu inutile.

Ajouter une non-linéarité nous permet de décrire tous types de fonctions. Il existe de nombreux types de fonctions différentes que nous pourrions appliquer, mais ReLU est la plus populaire car elle est très peu coûteuse à effectuer.

Voici les sorties de la couche ReLU Conv1 :

![Image](https://cdn-media-1.freecodecamp.org/images/GgrWjGfNKnG1Fq0cMHfd3r7r75BPn3XstvpK)
_256 sorties (20x20 pixels)_

### Partie 2a : PrimaryCaps

La couche PrimaryCaps commence comme une couche de convolution normale, mais cette fois nous effectuons une convolution sur la pile de 256 sorties des convolutions précédentes. Au lieu d'avoir un noyau de 9x9, nous avons un noyau de 9x9x256.

Alors, que cherchons-nous exactement ?

Dans la première couche de convolutions, nous cherchions des bords et des courbes simples. Maintenant, nous cherchons des formes légèrement plus complexes à partir des bords que nous avons trouvés précédemment.

Cette fois, notre "stride" est de 2. Cela signifie qu'au lieu de nous déplacer d'un pixel à la fois, nous faisons des pas de 2. Un stride plus grand est choisi afin que nous puissions réduire la taille de notre entrée plus rapidement :

![Image](https://cdn-media-1.freecodecamp.org/images/NCX7uIB7uaBTSWeBKL8rkvGNsnp0C2joHZWb)

**Note :** La dimension de la sortie serait normalement de 12, mais nous la divisons par 2, à cause du stride. Par exemple : `_((20 — 9) + 1) / 2 = 6_`

Nous allons convoluer les sorties 256 fois de plus. Nous allons donc obtenir une pile de 256 sorties de 6x6.

Mais cette fois, nous ne nous contentons pas de simples vieux nombres.

Nous allons découper la pile en 32 paquets avec 8 cartes chacun.

Nous pouvons appeler ce paquet une "couche de capsules".

Chaque couche de capsules a 36 "capsules".

Si vous suivez (et êtes un génie des maths), cela signifie que chaque capsule a un tableau de 8 valeurs. C'est ce que nous pouvons appeler un "vecteur".

Voici ce dont je parle :

![Image](https://cdn-media-1.freecodecamp.org/images/WLSoM2zmTDLNhLvNiKYqHmP0y-PdRBOlEM0K)

Ces "capsules" sont nos nouveaux pixels.

Avec un seul pixel, nous ne pouvions stocker que la confiance de savoir si nous avions trouvé un bord à cet endroit. Plus le nombre est élevé, plus la confiance est grande.

Avec une capsule, nous pouvons stocker 8 valeurs par emplacement ! Cela nous donne l'opportunité de stocker plus d'informations que simplement si nous avons trouvé une forme à cet endroit. Mais quels autres types d'informations voudrions-nous stocker ?

En regardant la forme ci-dessous, que pouvez-vous me dire à son sujet ? Si vous deviez dire à quelqu'un d'autre comment la redessiner, et qu'il ne pouvait pas la regarder, que diriez-vous ?

![Image](https://cdn-media-1.freecodecamp.org/images/q4J8nHBxTm35TE99THoituJTGJ6ssKnyWEpO)

Cette image est extrêmement basique, donc il n'y a que quelques détails dont nous avons besoin pour décrire la forme :

* Type de forme
* Position
* Rotation
* Couleur
* Taille

Nous pouvons appeler ces "paramètres d'instantiation". Avec des images plus complexes, nous aurons besoin de plus de détails. Ils peuvent inclure la pose (position, taille, orientation), la déformation, la vitesse, l'albédo, la teinte, la texture, et ainsi de suite.

Vous vous souvenez peut-être que lorsque nous avons fait un noyau pour la détection de bords, il ne fonctionnait que sur un angle spécifique. Nous avions besoin d'un noyau pour chaque angle. Nous pouvions nous en sortir lorsque nous traitons des bords car il y a très peu de façons de décrire un bord. Une fois que nous atteignons le niveau des formes, nous ne voulons pas avoir un noyau pour chaque angle de rectangles, ovales, triangles, et ainsi de suite. Cela deviendrait ingérable, et cela deviendrait encore pire lorsque nous traitons des formes plus compliquées qui ont des rotations en 3 dimensions et des caractéristiques comme l'éclairage.

C'est l'une des raisons pour lesquelles les réseaux de neurones traditionnels ne gèrent pas très bien les rotations invisibles :

![Image](https://cdn-media-1.freecodecamp.org/images/Q3flECHZIW6K8e7CDMQZ0CFa2rhXjB2rK2IZ)

Alors que nous passons des bords aux formes et des formes aux objets, il serait bien si nous avions plus de place pour stocker ces informations utiles supplémentaires.

Voici une comparaison simplifiée de 2 couches de capsules (une pour les rectangles et l'autre pour les triangles) vs 2 sorties de pixels traditionnelles :

![Image](https://cdn-media-1.freecodecamp.org/images/zzt6LWsLz4-aSteZyXvJcM8bydUtgOrtaLFX)

Comme un vecteur 2D ou 3D traditionnel, ce vecteur a un angle et une longueur. La longueur décrit la probabilité, et l'angle décrit les paramètres d'instantiation. Dans l'exemple ci-dessus, l'angle correspond en réalité à l'angle de la forme, mais ce n'est pas normalement le cas.

En réalité, il n'est pas vraiment faisable (ou du moins facile) de visualiser les vecteurs comme ci-dessus, car ces vecteurs sont à 8 dimensions.

Puisque nous avons toutes ces informations supplémentaires dans une capsule, l'idée est que nous devrions être capables de recréer l'image à partir d'elles.

Cela semble génial, mais comment incitons-nous le réseau à vouloir réellement apprendre ces choses ?

Lors de l'entraînement d'un CNN traditionnel, nous nous soucions uniquement de savoir si le modèle prédit la bonne classification. Avec un réseau de capsules, nous avons ce que l'on appelle une "reconstruction". Une reconstruction prend le vecteur que nous avons créé et essaie de recréer l'image d'entrée originale, étant donné uniquement ce vecteur. Nous notons ensuite le modèle en fonction de la proximité de la reconstruction avec l'image originale.

Je vais entrer dans plus de détails à ce sujet dans les sections à venir, mais voici un exemple simple :

![Image](https://cdn-media-1.freecodecamp.org/images/0jLnyPRFOgdEwEn7DqZwWJfaC05p09CUQmUd)

### Partie 2b : Squashing

Après avoir nos capsules, nous allons effectuer une autre fonction de non-linéarité (comme ReLU), mais cette fois l'équation est un peu plus impliquée. La fonction met à l'échelle les valeurs du vecteur de sorte que seule la longueur du vecteur change, pas l'angle. De cette façon, nous pouvons rendre le vecteur entre 0 et 1 pour qu'il soit une probabilité réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/XlLc1MM5cqr99LQrKT5yUJ99CTdU09xGuZ7C)

Voici à quoi ressemblent les **longueurs** des vecteurs de capsules après le squashing. À ce stade, il est presque impossible de deviner ce que chaque capsule recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/NiLltl6OVOmQJFsirTZUmIeNEEN9w5Tpdmfe)
_Gardez à l'esprit que chaque pixel est en réalité un vecteur de longueur 8_

### Partie 3 : Routing by Agreement

L'étape suivante consiste à décider quelles informations envoyer au niveau suivant. Dans les réseaux traditionnels, nous ferions probablement quelque chose comme le "max pooling". Le max pooling est un moyen de réduire la taille en ne transmettant que le pixel le plus activé de la région à la couche suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/EunY9PPwbi-iYghdzGKkqKvbZMuM3w4gnFb2)

Cependant, avec les réseaux de capsules, nous allons faire quelque chose appelé le routage par accord. Le meilleur exemple de cela est l'exemple du bateau et de la maison illustré par Aurélien Géron dans [cette excellente vidéo](https://www.youtube.com/watch?v=pPN8d0E3900). Chaque capsule essaie de prédire les activations de la couche suivante en fonction d'elle-même :

![Image](https://cdn-media-1.freecodecamp.org/images/UDpR9qNsGInbGZU8wHqC1oY3rDQ9l9X0IC3K)

En regardant ces prédictions, quel objet choisiriez-vous pour passer à la couche suivante (sans connaître l'entrée) ? Probablement le bateau, n'est-ce pas ? La capsule rectangle et la capsule triangle sont d'accord sur l'apparence du bateau. Mais elles ne sont pas d'accord sur l'apparence de la maison, donc il est peu probable que l'objet soit une maison.

Avec le routage par accord, nous ne transmettons que les informations utiles et jetons les données qui ajouteraient simplement du bruit aux résultats. Cela nous donne une sélection beaucoup plus intelligente que de simplement choisir le plus grand nombre, comme dans le max pooling.

Avec les réseaux traditionnels, les caractéristiques mal placées ne les dérangent pas :

![Image](https://cdn-media-1.freecodecamp.org/images/mby8Ob1WxB0mhI20jgQOiZGjHkS-dtbp6Kvg)

Avec les réseaux de capsules, les caractéristiques ne seraient pas d'accord entre elles :

![Image](https://cdn-media-1.freecodecamp.org/images/vlks3XiJhSJR94-5D7Yqklknx4dsbPaqAsZA)

Espérons que cela fonctionne de manière intuitive. Cependant, comment cela fonctionne-t-il mathématiquement ?

Nous avons 10 classes de chiffres différentes que nous prédisons :

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

**Note :** Dans l'exemple du bateau et de la maison, nous prédisions 2 objets, mais maintenant nous prédisons 10.

Contrairement à l'exemple du bateau et de la maison, les prédictions ne sont pas en réalité des images. Au lieu de cela, nous essayons de prédire le vecteur qui décrit l'image.

Les prédictions de la capsule pour chaque classe sont faites en multipliant son vecteur par une matrice de poids pour chaque classe que nous essayons de prédire.

Rappelez-vous que nous avons 32 couches de capsules, et chaque couche de capsules a 36 capsules. Cela signifie que nous avons un total de 1 152 capsules.

```py
cap_1 * poids_pour_0 = prédiction
cap_1 * poids_pour_1 = prédiction
cap_1 * poids_pour_2 = prédiction
cap_1 * ...
cap_1 * poids_pour_9 = prédiction

cap_2 * poids_pour_0 = prédiction
cap_2 * poids_pour_1 = prédiction
cap_2 * poids_pour_2 = prédiction
cap_2 * ...
cap_2 * poids_pour_9 = prédiction

...

cap_1152 * poids_pour_0 = prédiction
cap_1152 * poids_pour_1 = prédiction
cap_1152 * poids_pour_2 = prédiction
cap_1152 * ...
cap_1152 * poids_pour_9 = prédiction
```

Vous allez obtenir une liste de 11 520 prédictions.

Chaque poids est en réalité une matrice de 16x8, donc chaque prédiction est une multiplication de matrices entre le vecteur de capsule et cette matrice de poids :

![Image](https://cdn-media-1.freecodecamp.org/images/t8WRLiBJtfWjHLUSvhtx2bywlEO7SM0oNKnb)

Comme vous pouvez le voir, notre prédiction est un vecteur à 16 degrés.

D'où vient le 16 ? C'est un choix arbitraire, tout comme 8 l'était pour nos capsules originales.

Mais il convient de noter que nous voulons augmenter le nombre de dimensions de nos capsules plus nous allons profondément dans le réseau. Cela devrait avoir du sens intuitivement, car plus nous allons profondément, plus nos caractéristiques deviennent complexes et plus nous avons besoin de paramètres pour les recréer. Par exemple, vous aurez besoin de plus d'informations pour décrire un visage entier que simplement l'œil d'une personne.

L'étape suivante consiste à déterminer quelles sont les 11 520 prédictions qui sont les plus en accord les unes avec les autres.

Il peut être difficile de visualiser une solution à cela lorsque nous pensons en termes de vecteurs à haute dimension. Pour des raisons de santé mentale, commençons par prétendre que nos vecteurs sont simplement des points dans un espace à 2 dimensions :

![Image](https://cdn-media-1.freecodecamp.org/images/8uTYSisUIxhfjxwWpRQND1XfNZUXyfmlU-UI)

Nous commençons par calculer la moyenne de tous les points. Chaque point commence avec une importance égale :

![Image](https://cdn-media-1.freecodecamp.org/images/HMOGH8gQek305eZpEnFag2ygCnKwD7TvjcFN)

Nous pouvons ensuite mesurer la distance entre chaque point et la moyenne. Plus le point est éloigné de la moyenne, moins ce point devient important :

![Image](https://cdn-media-1.freecodecamp.org/images/eAlr6nS0NEb7E4OxH1eWZBSTkJBxD9owKHdW)

Nous recalculons ensuite la moyenne, cette fois en tenant compte de l'importance du point :

![Image](https://cdn-media-1.freecodecamp.org/images/ewEmGgjUWcL50lc4X-oWwYvxcvwYKwKCtTm0)

Nous finissons par passer par ce cycle 3 fois :

![Image](https://cdn-media-1.freecodecamp.org/images/XA6mhI9UzGcTbM90pI9kiiNKBVLhd4YBX9Yo)

Comme vous pouvez le voir, à mesure que nous passons par ce cycle, les points qui ne sont pas d'accord avec les autres commencent à disparaître. Les points les plus en accord finissent par être transmis à la couche suivante avec les activations les plus élevées.

### Partie 4 : DigitCaps

Après l'accord, nous obtenons dix vecteurs à 16 dimensions, un vecteur pour chaque chiffre. Cette matrice est notre prédiction finale. La longueur du vecteur est la confiance de la détection du chiffre — plus il est long, mieux c'est. Le vecteur peut également être utilisé pour générer une reconstruction de l'image d'entrée.

Voici à quoi ressemblent les longueurs des vecteurs avec l'entrée de 4 :

![Image](https://cdn-media-1.freecodecamp.org/images/-t0Ke6HoBg-EBjS3XIQfROS827ilzyLzWEbK)

Le cinquième bloc est le plus brillant, ce qui signifie une confiance élevée. Rappelez-vous que 0 est la première classe, ce qui signifie que 4 est notre classe prédite.

### Partie 5 : Reconstruction

La partie reconstruction de l'implémentation n'est pas très intéressante. Ce ne sont que quelques couches entièrement connectées. Mais la reconstruction elle-même est très cool et amusante à explorer.

Si nous reconstruisons notre entrée 4 à partir de son vecteur, voici ce que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/eQWDk11SEC85p0ygADaNCofea7Y2Ogl-ugo9)

Si nous manipulons les curseurs (le vecteur), nous pouvons voir comment chaque dimension affecte le 4 :

![Image](https://cdn-media-1.freecodecamp.org/images/9lXaCa9nKAK93jrOHN5exN1sKiXPuYwAmEV7)

Je recommande de cloner le dépôt de visualisation pour jouer avec différentes entrées et voir comment les curseurs affectent la reconstruction :

```bash
git clone https://github.com/bourdakos1/CapsNet-Visualization.git
cd CapsNet-Visualization
pip install -r requirements.txt
```

Exécutez l'outil :

```bash
python run_visualization.py
```

Puis pointez votre navigateur vers : [http://localhost:5000](http://localhost:5000/)

### Réflexions finales

Je pense que les reconstructions des réseaux de capsules sont époustouflantes. Même si le modèle actuel n'est entraîné que sur des chiffres simples, cela fait courir mon esprit avec les possibilités qu'une architecture mature entraînée sur un ensemble de données plus grand pourrait atteindre.

Je suis très curieux de voir comment manipuler les vecteurs de reconstruction d'une image plus compliquée l'affecterait. Pour cette raison, mon prochain projet est de faire fonctionner les réseaux de capsules avec les ensembles de données CIFAR et smallNORB.

Merci d'avoir lu ! Si vous avez des questions, n'hésitez pas à me contacter à bourdakos1@gmail.com, à vous connecter avec moi sur [LinkedIn](https://www.linkedin.com/in/nicholasbourdakos), ou à me suivre sur [Medium](https://medium.com/@bourdakos1) et [Twitter](https://twitter.com/bourdakos1).

Si vous avez trouvé cet article utile, cela signifierait beaucoup pour moi si vous lui donniez quelques applaudissements ? et le partagez pour aider les autres à le trouver ! Et n'hésitez pas à laisser un commentaire ci-dessous.