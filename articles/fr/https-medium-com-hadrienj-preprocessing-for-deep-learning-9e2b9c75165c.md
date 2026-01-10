---
title: 'Prétraitement pour le deep learning : de la matrice de covariance au blanchiment
  d''image'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-16T22:44:23.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-hadrienj-preprocessing-for-deep-learning-9e2b9c75165c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ehXogigFyLpyy2q2sz80HA.png
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Prétraitement pour le deep learning : de la matrice de covariance au blanchiment
  d''image'
seo_desc: 'By hadrienj

  The goal of this post is to go from the basics of data preprocessing to modern techniques
  used in deep learning. My point is that we can use code (such as Python/NumPy) to
  better understand abstract mathematical notions. Thinking by codin...'
---

Par hadrienj

Le but de cet article est de passer des bases du prétraitement des données aux techniques modernes utilisées en deep learning. Mon idée est que nous pouvons utiliser du code (comme Python/NumPy) pour mieux comprendre des notions mathématiques abstraites. Penser en codant ! 💡

Nous commencerons par des concepts basiques mais très utiles en science des données et en machine learning/deep learning, comme les matrices de variance et de covariance. Nous irons plus loin avec certaines techniques de prétraitement utilisées pour alimenter des images dans des réseaux de neurones. Nous essaierons d'obtenir des informations plus concrètes en utilisant du code pour voir ce que chaque équation fait réellement.

Le **prétraitement** fait référence à toutes les transformations appliquées aux données brutes avant qu'elles ne soient fournies à l'algorithme de machine learning ou de deep learning. Par exemple, entraîner un réseau de neurones convolutionnel sur des images brutes conduira probablement à de mauvaises performances de classification ([Pal & Sudeep, 2016](https://ieeexplore.ieee.org/document/7808140/)). Le prétraitement est également important pour accélérer l'entraînement (par exemple, les techniques de centrage et de mise à l'échelle, voir [Lecun et al., 2012 ; voir 4.3](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)).

Voici le plan de ce tutoriel :

**1. Contexte :** Dans la première partie, nous rappellerons quelques notions sur la variance et la covariance. Nous verrons comment générer et tracer des données fictives pour mieux comprendre ces concepts.

**2. Prétraitement :** Dans la deuxième partie, nous verrons les bases de certaines techniques de prétraitement qui peuvent être appliquées à tout type de données — **normalisation par la moyenne**, **standardisation** et **blanchiment**.

**3. Blanchiment d'images :** Dans la troisième partie, nous utiliserons les outils et concepts acquis dans **1.** et **2.** pour effectuer un type spécial de blanchiment appelé **Analyse des Composantes à Zéro (ZCA)**. Il peut être utilisé pour prétraiter des images pour le deep learning. Cette partie sera très pratique et amusante ☀️!

N'hésitez pas à forker [le notebook associé à cet article](https://github.com/hadrienj/Preprocessing-for-deep-learning)! Par exemple, vérifiez les formes des matrices chaque fois que vous avez un doute.

### 1. Contexte

#### A. Variance et covariance

La variance d'une variable décrit à quel point les valeurs sont dispersées. La covariance est une mesure qui indique le degré de dépendance entre deux variables.

Une covariance positive signifie que les valeurs de la première variable sont grandes lorsque les valeurs de la deuxième variable sont également grandes. Une covariance négative signifie l'inverse : les grandes valeurs d'une variable sont associées à de petites valeurs de l'autre.

La valeur de la covariance dépend de l'échelle de la variable, ce qui la rend difficile à analyser. Il est possible d'utiliser le coefficient de corrélation, qui est plus facile à interpréter. Le coefficient de corrélation est simplement la covariance normalisée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GH0ou22oJEwAw89GkrS8-w.png)
_Une covariance positive signifie que les grandes valeurs d'une variable sont associées à de grandes valeurs de l'autre (à gauche). Une covariance négative signifie que les grandes valeurs d'une variable sont associées à de petites valeurs de l'autre (à droite)._

La matrice de covariance est une matrice qui résume les variances et covariances d'un ensemble de vecteurs et peut en dire long sur vos variables. La diagonale correspond à la variance de chaque vecteur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5V2y7dyc7YclTRqdVjoOrQ.png)
_Une matrice **A** et sa matrice de covariance. La diagonale correspond à la variance de chaque vecteur colonne._

Vérifions simplement avec la formule de la variance :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EpBVFBmFboZeAxANYe6PEg.png)

avec **n** la longueur du vecteur, et **x̄** la moyenne du vecteur. Par exemple, la variance du premier vecteur colonne de **A** est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nIpi1287Raa-n9NKwVHrsA.png)

C'est la première cellule de notre matrice de covariance. Le deuxième élément sur la diagonale correspond à la variance du deuxième vecteur colonne de **A**, et ainsi de suite.

**Note** : les vecteurs extraits de la matrice **A** correspondent aux colonnes de **A**.

Les autres cellules correspondent à la covariance entre deux vecteurs colonnes de **_A_**. Par exemple, la covariance entre la première et la troisième colonne se trouve dans la matrice de covariance à la colonne 1 et à la ligne 3 (ou à la colonne 3 et à la ligne 1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ce3wTRBXCJUG7fFf95CQ9Q.png)
_La position dans la matrice de covariance. La colonne correspond à la première variable et la ligne à la seconde (ou l'inverse). La covariance entre le premier et le troisième vecteur colonne de **A** est l'élément à la colonne 1 et à la ligne 3 (ou l'inverse = même valeur)._

Vérifions que la covariance entre le premier et le troisième vecteur colonne de **A** est égale à -2,67. La formule de la covariance entre deux variables **_X_** et **Y** est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y1kVDzXPCxhRRsk8snmzTQ.png)

Les variables **X** et **Y** sont les premier et troisième vecteurs colonnes dans le dernier exemple. Décomposons cette formule pour être sûr qu'elle est claire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWZDmC8GrNL-xNqGG1CjyA.png)

1. Le symbole somme (**Σ**) signifie que nous allons itérer sur les éléments des vecteurs. Nous commencerons avec le premier élément (**i=1**) et calculerons le premier élément de **X** moins la moyenne du vecteur **X**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aFL3dzKMDXf9vj2_J5tNPQ.png)

2. Multipliez le résultat par le premier élément de **Y** moins la moyenne du vecteur **_Y_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/1*AKo4naYravnW3-3NrwSXTg.png)

3. Répétez le processus pour chaque élément des vecteurs et calculez la somme de tous les résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lk6JZa0lHqswjKwD5wKziQ.png)

4. Divisez par le nombre d'éléments dans le vecteur.

**Exemple 1.**

Commençons par la matrice **A** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6NqwIfr6XlHSL_NIXtXsA.png)

Nous allons calculer la covariance entre les premier et troisième vecteurs colonnes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BvbRAxHeb40LU5goEDsoLg.png)

et

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jx4vbnRDKW95fF2nYSygZg.png)

**x̄=3**, **ȳ=4**, et **n=3** donc nous avons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PcvOUuCgOCY_qQhLb5AimA.png)

OK, super ! C'est la valeur de la matrice de covariance.

**Maintenant, la méthode facile**. Avec NumPy, la matrice de covariance peut être calculée avec la fonction `np.cov`.

**Il est à noter** que si vous voulez que NumPy utilise les colonnes comme vecteurs, le paramètre `rowvar=False` doit être utilisé. De plus, `bias=True` divise par **n** et non par **n-1**.

Créons d'abord le tableau :

```
array([[1, 3, 5],       [5, 4, 1],       [3, 8, 6]])
```

Maintenant, nous allons calculer la covariance avec la fonction NumPy :

```
array([[ 2.66666667, 0.66666667, -2.66666667],       [ 0.66666667, 4.66666667, 2.33333333],       [-2.66666667, 2.33333333, 4.66666667]])
```

Cela semble bon !

**Trouver la matrice de covariance avec le produit scalaire**

Il existe une autre façon de calculer la matrice de covariance de **A**. Vous pouvez centrer **A** autour de 0. La moyenne du vecteur est soustraite de chaque élément du vecteur pour avoir un vecteur avec une moyenne égale à 0. Il est multiplié par sa propre transposée, et divisé par le nombre d'observations.

Commençons par une implémentation et ensuite nous essaierons de comprendre le lien avec l'équation précédente :

Testons cela sur notre matrice **A** :

```
array([[ 2.66666667, 0.66666667, -2.66666667],       [ 0.66666667, 4.66666667, 2.33333333],       [-2.66666667, 2.33333333, 4.66666667]])
```

Nous obtenons le même résultat qu'avant.

L'explication est simple. Le produit scalaire entre deux vecteurs peut être exprimé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hdHYlHiK3s0IDwwWytJO0A.png)

C'est exact, c'est la somme des produits de chaque élément des vecteurs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6zDuuYJtL6yiuE1CatrYDQ.png)
_Le produit scalaire correspond à la somme des produits de chaque élément des vecteurs._

Si **n** est le nombre d'éléments dans nos vecteurs et que nous divisons par **n** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNMJtFhQF2v56K1OLE0_Yw.png)

Vous pouvez noter que cela n'est pas trop éloigné de la formule de la covariance que nous avons vue précédemment :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RYVpFx0lrkTEl_R92ocGgQ.png)

La seule différence est que, dans la formule de la covariance, nous soustrayons la moyenne d'un vecteur de chacun de ses éléments. C'est pourquoi nous devons centrer les données avant de faire le produit scalaire.

Maintenant, si nous avons une matrice **A**, le produit scalaire entre **A** et sa transposée vous donnera une nouvelle matrice :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Qw42RtGhHQWXD4rkA-MTQ.png)
_Si vous commencez avec une matrice centrée sur zéro, le produit scalaire entre cette matrice et sa transposée vous donnera la variance de chaque vecteur et la covariance entre eux, c'est-à-dire la matrice de covariance._

C'est la matrice de covariance !

#### B. Visualiser les données et les matrices de covariance

Afin d'obtenir plus d'informations sur la matrice de covariance et comment elle peut être utile, nous allons créer une fonction pour la visualiser avec des données 2D. Vous pourrez voir le lien entre la matrice de covariance et les données.

Cette fonction calculera la matrice de covariance comme nous l'avons vu ci-dessus. Elle créera deux sous-graphiques — un pour la matrice de covariance et un pour les données. La fonction `heatmap()` de [Seaborn](https://seaborn.pydata.org) est utilisée pour créer des gradients de couleur — les petites valeurs seront colorées en vert clair et les grandes valeurs en bleu foncé. Nous avons choisi l'une de nos couleurs de palette, mais vous pouvez préférer d'autres couleurs. Les données sont représentées sous forme de nuage de points.

#### C. Simulation de données

**Données non corrélées**

Maintenant que nous avons la fonction de traçage, nous allons générer quelques données aléatoires pour visualiser ce que la matrice de covariance peut nous dire. Nous commencerons par quelques données tirées d'une distribution normale avec la fonction NumPy `np.random.normal()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C5wwjainirV9mQHDlei9SQ.png)
_Tirage d'échantillon d'une distribution normale avec NumPy._

Cette fonction nécessite la moyenne, l'écart-type et le nombre d'observations de la distribution en entrée. Nous allons créer deux variables aléatoires de 300 observations avec un écart-type de 1. La première aura une moyenne de 1 et la seconde une moyenne de 2. Si nous tirons aléatoirement deux ensembles de 300 observations d'une distribution normale, les deux vecteurs seront non corrélés.

```
(300, 2)
```

**Note 1** : Nous transposons les données avec `.T` car la forme originale est `(2, 300)` et nous voulons le nombre d'observations comme lignes (donc avec la forme `(300, 2)`).

**Note 2** : Nous utilisons la fonction `np.random.seed` pour la reproductibilité. Le même nombre aléatoire sera utilisé la prochaine fois que nous exécuterons la cellule.

Vérifions à quoi ressemblent les données :

```
array([[ 2.47143516, 1.52704645],       [ 0.80902431, 1.7111124 ],       [ 3.43270697, 0.78245452],       [ 1.6873481 , 3.63779121],       [ 1.27941127, -0.74213763],       [ 2.88716294, 0.90556519],       [ 2.85958841, 2.43118375],       [ 1.3634765 , 1.59275845],       [ 2.01569637, 1.1702969 ],       [-0.24268495, -0.75170595]])
```

Bien, nous avons deux vecteurs colonnes.

Maintenant, nous pouvons vérifier que les distributions sont normales :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wb8r7PRje6nunmN-iMrUyQ.png)

Cela semble bon !

Nous pouvons voir que les distributions ont des écarts-types équivalents mais des moyennes différentes (1 et 2). Donc c'est exactement ce que nous avons demandé.

Maintenant, nous pouvons tracer notre ensemble de données et sa matrice de covariance avec notre fonction :

```
Matrice de covariance :[[ 0.95171641 -0.0447816 ] [-0.0447816 0.87959853]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kq4mIBv4hFGzOuhoftcFVQ.png)

Nous pouvons voir sur le nuage de points que les deux dimensions ne sont pas corrélées. Notez que nous avons une dimension avec une moyenne de 1 (axe y) et l'autre avec une moyenne de 2 (axe x).

De plus, la matrice de covariance montre que la variance de chaque variable est très grande (autour de 1) et la covariance des colonnes 1 et 2 est très petite (autour de 0). Puisque nous avons assuré que les deux vecteurs sont indépendants, cela est cohérent. L'inverse n'est pas nécessairement vrai : une covariance de 0 ne garantit pas l'indépendance (voir [ici](https://stats.stackexchange.com/questions/12842/covariance-and-independence)).

**Données corrélées**

Maintenant, construisons des données dépendantes en spécifiant une colonne à partir de l'autre.

```
Matrice de covariance :[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*r-OmoGkWJvkWqjFO0ltV3w.png)

La corrélation entre les deux dimensions est visible sur le nuage de points. Nous pouvons voir qu'une ligne pourrait être tracée et utilisée pour prédire **y** à partir de **x** et vice versa. La matrice de covariance n'est pas diagonale (il y a des cellules non nulles en dehors de la diagonale). Cela signifie que la covariance entre les dimensions est non nulle.

C'est super ! Nous avons maintenant tous les outils pour voir différentes techniques de prétraitement.

### 2. Prétraitement

#### A. Normalisation par la moyenne

La normalisation par la moyenne consiste simplement à soustraire la moyenne de chaque observation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ym0P7PyUgZlML1QlGeUlvQ.png)

où **X'** est l'ensemble de données normalisé, **X** est l'ensemble de données original, et **x̄** est la moyenne de **X**.

La normalisation par la moyenne a pour effet de centrer les données autour de 0. Nous allons créer la fonction `center()` pour faire cela :

Essayons avec la matrice **B** que nous avons créée précédemment :

```
Avant :
```

```
Matrice de covariance :[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*PaAR5buk8ICGSyiTKAeh_w.png)

```
Après :
```

```
Matrice de covariance :[[ 0.95171641 0.92932561] [ 0.92932561 1.12683445]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeCA2GooKYzbVqevDVG0FA.png)

Le premier graphique montre à nouveau les données originales **B** et le deuxième graphique montre les données centrées (regardez l'échelle).

#### B. Standardisation ou normalisation

La standardisation est utilisée pour mettre toutes les caractéristiques à la même échelle. Chaque dimension centrée sur zéro est divisée par son écart-type.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2PX6slhDPJkjibJiecX25Q.png)

où **X'** est l'ensemble de données standardisé, **X** est l'ensemble de données original, **x̄** est la moyenne de **X**, et **σ** est l'écart-type de **_X_**. 

Créons un autre ensemble de données avec une échelle différente pour vérifier que cela fonctionne.

```
Matrice de covariance :[[ 0.95171641 0.83976242] [ 0.83976242 6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vTAyUBAcepxHyvX449hESQ.png)

Nous pouvons voir que les échelles de **x** et **y** sont différentes. Notez également que la corrélation semble plus faible en raison des différences d'échelle. Maintenant, standardisons cela :

```
Matrice de covariance :[[ 1.          0.34500274] [ 0.34500274  1.        ]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0a6gXhWnLPBv8i-L7PbYKA.png)

Cela semble bon. Vous pouvez voir que les échelles sont les mêmes et que l'ensemble de données est centré sur zéro selon les deux axes.

Maintenant, jetez un coup d'œil à la matrice de covariance. Vous pouvez voir que la variance de chaque coordonnée — la cellule en haut à gauche et la cellule en bas à droite — est égale à 1.

Cette nouvelle matrice de covariance est en fait la matrice de corrélation. Le coefficient de corrélation de Pearson entre les deux variables (**c1** et **c2**) est 0,54220151.

#### C. Blanchiment

Le blanchiment, ou sphérisation, des données signifie que nous voulons les transformer pour avoir une matrice de covariance qui est la matrice identité — 1 sur la diagonale et 0 pour les autres cellules. Il est appelé blanchiment en référence au bruit blanc.

[Voici plus de détails sur la matrice identité.](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.3-Identity-and-Inverse-Matrices/)

Le blanchiment est un peu plus compliqué que les autres prétraitements, mais nous avons maintenant tous les outils dont nous avons besoin pour le faire. Il implique les étapes suivantes :

* Centrer les données sur zéro
* Décorrélation des données
* Redimensionnement des données

Prenons à nouveau **C** et essayons de faire ces étapes.

1. **Centrage sur zéro**

Cela fait référence à la normalisation par la moyenne (**2. A**). Vérifiez les détails sur la fonction `center()`.

```
Matrice de covariance :[[ 0.95171641  0.83976242] [ 0.83976242  6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AXOzdgC8gjiwpg-9AsfzKw.png)

**2. Décorrélation**

À ce stade, nous devons décorrélationner nos données. Intuitivement, cela signifie que nous voulons faire tourner les données jusqu'à ce qu'il n'y ait plus de corrélation. Regardez l'image suivante pour voir ce que je veux dire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ehXogigFyLpyy2q2sz80HA.png)

Le graphique de gauche montre des données corrélées. Par exemple, si vous prenez un point de données avec une grande valeur **x**, il y a des chances que le **y** associé soit également assez grand.

Maintenant, prenez tous les points de données et faites une rotation (peut-être de 45 degrés dans le sens inverse des aiguilles d'une montre). Les nouvelles données, tracées à droite, ne sont plus corrélées. Vous pouvez voir que les grandes et petites valeurs de **y** sont liées au même type de valeurs de **x**.

La question est : comment pourrions-nous trouver la bonne rotation afin d'obtenir les données non corrélées ?

En fait, c'est exactement ce que font les vecteurs propres de la matrice de covariance. Ils indiquent la direction où la dispersion des données est à son maximum :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1SAoJ_o70IygSmDnKiCkmw.png)

Les vecteurs propres de la matrice de covariance vous donnent la direction qui maximise la variance. La direction de la **ligne verte** est celle où la variance est maximale. Regardez simplement les points les plus petits et les plus grands projetés sur cette ligne — la dispersion est grande. Comparez cela avec la projection sur la **ligne orange** — la dispersion est très petite.

Pour plus de détails sur la décomposition propre, voir [cet article](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/).

Nous pouvons donc décorrélationner les données en les projetant à l'aide des vecteurs propres. Cela aura pour effet d'appliquer la rotation nécessaire et de supprimer les corrélations entre les dimensions. Voici les étapes :

* Calculer la matrice de covariance
* Calculer les vecteurs propres de la matrice de covariance
* Appliquer la matrice des vecteurs propres aux données — cela appliquera la rotation

Emballons cela dans une fonction :

Essayons de décorrélationner notre matrice centrée sur zéro **C** pour voir cela en action :

```
Matrice de covariance :[[ 0.95171641 0.83976242] [ 0.83976242 6.22529922]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ok5JSx7zN4lg9FAcZOE6Ew.png)

```
Matrice de covariance :[[ 5.96126981e-01 -1.48029737e-16] [ -1.48029737e-16 3.15205774e+00]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HmJGGe0cP6X-p0W-VuRfBg.png)

Bien ! Cela fonctionne.

Nous pouvons voir que la corrélation n'est plus présente. La matrice de covariance, maintenant une matrice diagonale, confirme que la covariance entre les deux dimensions est égale à 0.

**3. Redimensionnement des données**

L'étape suivante consiste à mettre à l'échelle la matrice non corrélée afin d'obtenir une matrice de covariance correspondant à la matrice identité. Pour ce faire, nous mettons à l'échelle nos données décorrélées en divisant chaque dimension par la racine carrée de sa valeur propre correspondante.

**Note** : nous ajoutons une petite valeur (ici 10^-5) pour éviter la division par 0.

```
Matrice de covariance :[[ 9.99983225e-01 -1.06581410e-16] [ -1.06581410e-16 9.99996827e-01]]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vFleYrVKknN5zwO3SNA5hQ.png)

Hourra ! Nous pouvons voir avec la matrice de covariance que tout est bon. Nous avons quelque chose qui ressemble à une matrice identité — 1 sur la diagonale et 0 ailleurs.

### 3. Blanchiment d'images

Nous allons voir comment le blanchiment peut être appliqué pour prétraiter un ensemble de données d'images. Pour ce faire, nous utiliserons l'article de [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) où ils donnent quelques détails sur le processus. Cette technique de prétraitement est appelée Analyse des Composantes à Zéro (ZCA).

Consultez l'article, mais voici le type de résultat qu'ils ont obtenu. Les images originales (à gauche) et les images après le ZCA (à droite) sont montrées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YyKLLSzcAMX_9cCBbjP2sg.png)
_Blanchiment d'images du jeu de données CIFAR10. Résultats de l'article de [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/)._

Commençons par le commencement. Nous allons charger des images du jeu de données CIFAR. Ce jeu de données est disponible à partir de Keras et vous pouvez également le télécharger [ici](https://www.cs.toronto.edu/~kriz/cifar.html).

```
(50000, 32, 32, 3)
```

L'ensemble d'entraînement du jeu de données CIFAR10 contient 50000 images. La forme de `X_train` est `(50000, 32, 32, 3)`. Chaque image est de 32px par 32px et chaque pixel contient 3 dimensions (R, G, B). Chaque valeur est la luminosité de la couleur correspondante entre 0 et 255.

Nous allons commencer par sélectionner seulement un sous-ensemble des images, disons 1000 :

```
(1000, 32, 32, 3)
```

C'est mieux. Maintenant, nous allons remodeler le tableau pour avoir des données d'image plates avec une image par ligne. Chaque image sera `(1, 3072)` car 32 x 32 x 3 = 3072. Ainsi, le tableau contenant toutes les images sera `(1000, 3072)` :

```
(1000, 3072)
```

L'étape suivante est de pouvoir voir les images. La fonction `imshow()` de Matplotlib ([doc](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html)) peut être utilisée pour afficher les images. Elle a besoin d'images avec la forme (M x N x 3), donc créons une fonction pour remodeler les images et pouvoir les visualiser à partir de la forme `(1, 3072)`.

Par exemple, traçons une des images que nous avons chargées :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ylvIdrsU1GyVkJwP6cwTdA.png)

Mignon !

Nous pouvons maintenant implémenter le blanchiment des images. [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) décrivent le processus :

**1.** La première étape consiste à redimensionner les images pour obtenir la plage [0, 1] en divisant par 255 (la valeur maximale des pixels).

Rappelons que la formule pour obtenir la plage [0, 1] est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*g8aDx7zkR7G4GoZzLJONhA.png)

mais, ici, la valeur minimale est 0, donc cela donne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QSSqNJa6rbJGOEQMk_Jp0A.png)

```
X.min() 0.0X.max() 1.0
```

**Soustraction de la moyenne : par pixel ou par image ?**

OK, cool, la plage de nos valeurs de pixel est maintenant entre 0 et 1. L'étape suivante est :

**2.** Soustraire la moyenne de toutes les images.

**Faites attention ici.**

Une façon de faire est de prendre chaque image et de soustraire la moyenne de cette image de chaque pixel ([Jarrett et al., 2009](https://www.computer.org/csdl/proceedings/iccv/2009/4420/00/05459469.pdf)). L'intuition derrière ce processus est qu'il centre les pixels de chaque image autour de 0.

Une autre façon de faire est de prendre chacun des 3072 pixels que nous avons (32 par 32 pixels pour R, G et B) pour chaque image et de soustraire la moyenne de ce pixel à travers toutes les images. Cela s'appelle la soustraction de la moyenne par pixel. Cette fois, chaque pixel sera centré autour de 0 **selon toutes les images**. Lorsque vous alimenterez votre réseau avec les images, chaque pixel est considéré comme une caractéristique différente. Avec la soustraction de la moyenne par pixel, nous avons centré chaque caractéristique (pixel) autour de 0. Cette technique est couramment utilisée (par exemple [Wan et al., 2013](http://proceedings.mlr.press/v28/wan13.html)).

Nous allons maintenant effectuer la soustraction de la moyenne par pixel à partir de nos 1000 images. Nos données sont organisées avec ces dimensions `(images, pixels)`. C'était `(1000, 3072)` car il y a 1000 images avec 32 x 32 x 3 = 3072 pixels. La moyenne par pixel peut ainsi être obtenue à partir du premier axe :

```
(3072,)
```

Cela nous donne 3072 valeurs qui est le nombre de moyennes — une par pixel. Voyons le type de valeurs que nous avons :

```
array([ 0.5234 , 0.54323137, 0.5274 , …, 0.50369804, 0.50011765, 0.45227451])
```

Cela est proche de 0,5 car nous avons déjà normalisé à la plage [0, 1]. Cependant, nous devons encore soustraire la moyenne de chaque pixel :

Juste pour nous convaincre que cela a fonctionné, nous allons calculer la moyenne du premier pixel. Espérons que ce soit 0.

```
array([ -5.30575583e-16, -5.98021632e-16, -4.23439062e-16, …, -1.81965554e-16, -2.49800181e-16, 3.98570066e-17])
```

Ce n'est pas exactement 0 mais c'est suffisamment petit pour que nous puissions considérer que cela a fonctionné !

Maintenant, nous voulons calculer la matrice de covariance des données centrées sur zéro. Comme nous l'avons vu ci-dessus, nous pouvons la calculer avec la fonction `np.cov()` de NumPy.

**Veuillez noter** que nos variables sont nos différentes images. Cela implique que les variables sont les lignes de la matrice **X**. Juste pour être clair, nous allons donner cette information à NumPy avec le paramètre `rowvar=TRUE` même si c'est `True` par défaut (voir la [doc](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html)) :

**Maintenant, la partie magique** — nous allons calculer les valeurs singulières et les vecteurs de la matrice de covariance et les utiliser pour faire tourner notre ensemble de données. Jetez un coup d'œil à [mon article](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.8-Singular-Value-Decomposition/) sur la décomposition en valeurs singulières (SVD) si vous avez besoin de plus de détails.

**Note** : Cela peut prendre un peu de temps avec beaucoup d'images et c'est pourquoi nous utilisons seulement 1000. Dans l'article, ils ont utilisé 10000 images. N'hésitez pas à comparer les résultats en fonction du nombre d'images que vous utilisez :

Dans l'article, ils ont utilisé l'équation suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ucN3UJIcEWsuYu1EZjA3KA.png)

avec **U** les vecteurs singulaires gauches et **S** les valeurs singulières de la covariance de l'ensemble de données initial normalisé d'images, et **X** l'ensemble de données normalisé. **ε** est un hyper-paramètre appelé le coefficient de blanchiment. **diag(a)** correspond à une matrice avec le vecteur **a** comme diagonale et 0 dans toutes les autres cellules.

Nous allons essayer d'implémenter cette équation. Commençons par vérifier les dimensions de la SVD :

```
(1000, 1000) (1000,)
```

**S** est un vecteur contenant 1000 éléments (les valeurs singulières). **diag(S)** sera ainsi de forme `(1000, 1000)` avec **S** comme diagonale :

```
[[ 8.15846654e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 4.68234845e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 2.41075267e+00 …, 0.00000000e+00 0.00000000e+00 0.00000000e+00] …,  [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 3.92727365e-05 0.00000000e+00 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 3.52614473e-05 0.00000000e+00] [ 0.00000000e+00 0.00000000e+00 0.00000000e+00 …, 0.00000000e+00 0.00000000e+00 1.35907202e-15]]
```

```
forme : (1000, 1000)
```

Vérifiez cette partie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l5DfX7eqQvIgndc4B749Gg.png)

Cela est également de forme `(1000, 1000)` ainsi que **U** et **U^T**. Nous avons vu aussi que **X** a la forme `(1000, 3072)`. La forme de **X_ZCA** est donc :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2aSZTPJiOgdApva29IZyUg.png)

ce qui correspond à la forme de l'ensemble de données initial. Bien.

Nous avons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TdmO3dBq-ne84RqY-EtZ2Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mEVlWSSed1Ne_eQ7UiqrZQ.png)

Décevant ! Si vous regardez l'article, ce n'est pas le type de résultat qu'ils montrent. En fait, c'est parce que nous n'avons pas redimensionné les pixels et qu'il y a des valeurs négatives. Pour ce faire, nous pouvons les remettre dans la plage [0, 1] avec la même technique que ci-dessus :

```
min : 0.0max : 1.0
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ylvIdrsU1GyVkJwP6cwTdA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Cd3O07GnABlmvfGflJDqg.png)

Hourra ! C'est super ! Cela ressemble à une image de l'article. Comme mentionné précédemment, ils ont utilisé 10000 images et non 1000 comme nous.

Pour voir les différences dans les résultats en fonction du nombre d'images que vous utilisez et de l'effet de l'hyper-paramètre **ε**, voici les résultats pour différentes valeurs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZN5tPhzho7QCbL4VCXYKGQ.png)

Le résultat du blanchiment est différent en fonction du nombre d'images que nous utilisons et de la valeur de l'hyper-paramètre **ε**. L'image de gauche est l'image originale. Dans l'article, [Pal & Sudeep (2016)](https://ieeexplore.ieee.org/document/7808140/) ont utilisé 10000 images et epsilon = 0,1. Cela correspond à l'image en bas à gauche.

C'est tout !

J'espère que vous avez trouvé quelque chose d'intéressant dans cet article. Vous pouvez le lire sur mon [blog](https://hadrienj.github.io/posts/Preprocessing-for-deep-learning/), avec LaTeX pour les maths, ainsi que d'autres articles.

Vous pouvez également forker le notebook Jupyter sur Github [ici](https://github.com/hadrienj/Preprocessing-for-deep-learning).

#### Références

[K. Jarrett, K. Kavukcuoglu, M. Ranzato, et Y. LeCun, « What is the best multi-stage architecture for object recognition ? », dans 2009 IEEE 12th International Conference on Computer Vision, 2009, pp. 2146–2153.](https://www.computer.org/csdl/proceedings/iccv/2009/4420/00/05459469.pdf)

[A. Krizhevsky, « Learning Multiple Layers of Features from Tiny Images », Mémoire de maîtrise, Université de Tront, 2009.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.222.9220&rep=rep1&type=pdf)

[Y. A. LeCun, L. Bottou, G. B. Orr, et K.-R. Müller, « Efficient BackProp », dans Neural Networks: Tricks of the Trade, Springer, Berlin, Heidelberg, 2012, pp. 9–48.](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

[K. K. Pal et K. S. Sudeep, « Preprocessing for image classification by convolutional neural networks », dans 2016 IEEE International Conference on Recent Trends in Electronics, Information Communication Technology (RTEICT), 2016, pp. 1778–1781.](https://ieeexplore.ieee.org/document/7808140/)

[L. Wan, M. Zeiler, S. Zhang, Y. L. Cun, et R. Fergus, « Regularization of Neural Networks using DropConnect », dans International Conference on Machine Learning, 2013, pp. 1058–1066.](http://proceedings.mlr.press/v28/wan13.html)

**Excellent ressources et QA**

[Wikipedia — Transformation de blanchiment](https://en.wikipedia.org/wiki/Whitening_transformation)

[CS231 — Réseaux de neurones convolutionnels pour la reconnaissance visuelle](http://cs231n.github.io/neural-networks-2/)

[Dustin Stansbury — The Clever Machine](https://theclevermachine.wordpress.com/2013/03/30/the-statistical-whitening-transform/)

[Quelques détails sur la matrice de covariance](http://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/)

[SO — Blanchiment d'image en Python](https://stackoverflow.com/questions/41635737/is-this-the-correct-way-of-whitening-an-image-in-python)

[Normalisation par la moyenne par image ou à partir de l'ensemble de données entier](http://ufldl.stanford.edu/wiki/index.php/Data_Preprocessing)

[Soustraction de la moyenne — toutes les images ou par image ?](https://stackoverflow.com/questions/29743523/subtract-mean-from-image)

[Pourquoi le centrage est important — Voir la section 4.3](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

[Kernel Kaggle sur ZCA](https://www.kaggle.com/nicw102168/exploring-zca-and-color-image-whitening/notebook)

[Comment ZCA est implémenté dans Keras](https://github.com/keras-team/keras-preprocessing/blob/b9d142456a64ef228475f07cb2f2d38fd05bd249/keras_preprocessing/image.py#L1254:L1257)