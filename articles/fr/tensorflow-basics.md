---
title: "Comment utiliser TensorFlow pour le Deep Learning \x13 Les bases pour les\
  \ d\x0Ebutants"
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-02-14T23:46:51.000Z'
originalURL: https://freecodecamp.org/news/tensorflow-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/tensorflow.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: neural networks
  slug: neural-networks
- name: tensor
  slug: tensor
- name: TensorFlow
  slug: tensorflow
seo_title: "Comment utiliser TensorFlow pour le Deep Learning \x13 Les bases pour\
  \ les d\x0Ebutants"
seo_desc: 'TensorFlow is a library that helps engineers build and train deep learning
  models. It provides all the tools we need to create neural networks.

  We can use TensorFlow to train simple to complex neural networks using large sets
  of data.

  TensorFlow is u...'
---

TensorFlow est une bibliothque qui aide les ingnieurs 0 construire et entranner des modles de deep learning. Elle fournit tous les outils dont nous avons besoin pour crer des rseaux de neurones.

Nous pouvons utiliser TensorFlow pour entranner des rseaux de neurones simples ou complexes en utilisant de grands ensembles de donnes.

TensorFlow est utilis dans une varit d'applications, de la reconnaissance d'images et de la parole au traitement du langage naturel et 0 la robotique. TensorFlow nous permet de construire rapidement et facilement des modles d'IA puissants avec une grande prcision et performance.

TensorFlow fonctionne 9galement avec des GPU et des TPU, qui sont des types de puces informatiques conues pour 9tendre les capacits de TensorFlow. Ces puces permettent 0 TensorFlow de fonctionner plus rapidement, ce qui est utile lorsque vous avez beaucoup de donnes 0 traiter.

Dans cet article, nous allons apprendre ce que sont les tenseurs et comment travailler avec eux en utilisant TensorFlow. Plongeons-nous directement dans le sujet.

## Qu'est-ce qu'un tenseur ?

Une explication simple serait qu'un tenseur est un tableau multi-dimensionnel.

![Image](https://miro.medium.com/max/1050/1*rLcM-j8b61Xlfk81k_exKw.png)
_Scalaire, Vecteur, Matrice et Tenseur_

Un scalaire est un nombre unique. Un vecteur est un tableau de nombres. Une matrice est un tableau 0 deux dimensions. Un tenseur est un tableau 0 n dimensions.

Dans TensorFlow, tout peut atre considr comme un tenseur, y compris un scalaire. Un scalaire serait un tenseur de dimension 0, un vecteur de dimension 1, et une matrice de dimension 2.

Cela est utile car nous ne sommes pas limits 0 travailler avec des ensembles de donnes complexes dans TensorFlow. TensorFlow peut grer tout type de donnes et les alimenter dans des modles de machine learning.

## Qu'est-ce que TensorFlow ?

TensorFlow est une bibliothque logicielle open-source pour la construction de rseaux de neurones. L'9quipe Google Brain est celle qui l'a dveloppe et c'est la bibliothque de deep learning la plus populaire sur le marche aujourd'hui.

Vous pouvez utiliser TensorFlow pour construire des modles d'IA, y compris la reconnaissance d'images et de la parole, le traitement du langage naturel et la mod9lisation pr9dictive.

![Image](https://miro.medium.com/max/1050/1*mPUeOmKYoWvPcZFjMdsiUQ.gif)
_R9seau de neurones de classification_

TensorFlow utilise un graphe de flux de donnes pour repr9senter les calculs. Pour faire simple, TensorFlow a facilit la construction de modles de machine learning complexes.

TensorFlow g9re beaucoup de travail en coulisses, ce qui le rend utile lors de la construction et de l'entraînement de tout type de mod9le de machine learning. TensorFlow g9re 9galement les calculs, y compris la parall9lisation et l'optimisation, au nom de l'utilisateur.

## TensorFlow et Keras

![Image](https://miro.medium.com/max/1050/1*X7QA_c8KHk7nD0tywv-OVg.png)
_TensorFlow et Keras_

TensorFlow dispose d'une API de haut niveau appele Keras. Keras 9tait un projet autonome qui est maintenant disponible dans la bibliothque TensorFlow. Keras facilite la dfinition et l'entraînement des mod9les tandis que TensorFlow offre un contr4le plus pouss9 sur les calculs.

TensorFlow prend en charge une large gamme de mat9riel, y compris les CPU, les GPU et les TPU. Les TPU sont des unites de traitement de tenseurs, con7ues sp9cifiquement pour travailler avec les tenseurs et TensorFlow.

Nous pouvons 9galement ex9cuter TensorFlow sur des appareils mobiles et des appareils IoT en utilisant TensorFlow Lite. TensorFlow dispose 9galement d'une grande communaut9 de d9veloppeurs et est mis 0 jour avec de nouvelles fonctionnalites et capacites.

## Comment construire des tenseurs avec TensorFlow

Commen7ons 0 9crire du code. Si vous n'avez pas TensorFlow install9, vous pouvez utiliser un [Google colab notebook](https://colab.research.google.com/) pour suivre.

Commen7ons par importer TensorFlow et afficher la version.

```
import tensorflow as tf
print(tf.__version__)
```

```
OUTPUT:
2.9.2

```

Commen7ons par cr9er un scalaire en utilisant tf.constant. Nous utilisons tf.constant pour cr9er une nouvelle valeur constante. Nous pouvons 9galement utiliser tf.variable pour cr9er une valeur variable. Nous allons ensuite afficher la valeur et v9rifier la dimension du scalaire en utilisant la propri9t9 ndim. Sa dimension sera z9ro car il s'agit d'une seule valeur.

```
scalar = tf.constant(7)
print(scalar)
print(scalar.ndim)
```

```
OUTPUT:
tf.Tensor(7, shape=(), dtype=int32)
0
```

Maintenant, cr9ons un vecteur et affichons ses dimensions. Vous pouvez voir que la dimension est 1.

```
vector = tf.constant([10,10])
print(vector)
print(vector.ndim)
```

```
OUTPUT:
tf.Tensor([10 10], shape=(2,), dtype=int32)
1
```

Maintenant, essayons de cr9er une matrice et d'afficher ses dimensions.

```
matrix = tf.constant([
    [10,11],
    [12,13]
])
print(matrix)
print(matrix.ndim)
```

```
OUTPUT:
tf.Tensor(
[[10 11]
 [12 13]], shape=(2, 2), dtype=int32)
2
```

Vous verrez que la dimension est maintenant 2. Vous pouvez 9galement voir que la forme de la matrice est 2 par 2.

Les formes et les dimensions sont utiles lors de l'utilisation de TensorFlow car nous changerons souvent ces donnes lors de l'utilisation de ces donnes pour entranner des rseaux de neurones.

Nous avons vu que ces tenseurs ont un type de donnes par dfaut de int32. Que faire si nous voulons cr9er un ensemble de donnes avec un type de donnes personnalis9 ?

tf.constant nous fournit l'argument dtype. Cr9ons la m9me matrice 0 nouveau avec float16 comme type de donnes.

```
tensor_1 = tf.constant([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
],dtype='float32')
print(tensor_1)
```

```
OUTPUT:
tf.Tensor(
[[[1. 2. 3.]]

 [[4. 5. 6.]]

 [[7. 8. 9.]]], shape=(3, 1, 3), dtype=float32)
```

Maintenant, cr9ons un tenseur. Nous allons entrer un tableau 0 trois dimensions dans tf.constant. Nous allons 9galement afficher ses dimensions.

```
tensor = tf.constant([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
])
print(tensor)
print(tensor.ndim)
```

```
OUTPUT:
tf.Tensor(
[[[1 2 3]]
 [[4 5 6]]
 [[7 8 9]]], shape=(3, 1, 3), dtype=int32)
3
```

Nous avons maintenant un tenseur de dimension 3 et de forme 3 par 1 par 3. C'est le tenseur le plus simple que vous puissiez cr9er. Dans des scnarios r9els, nous traiterons des tenseurs de dimensions sup9rieures et de formes plus grandes.

Maintenant, voyons comment cr9er un tenseur variable. Nous n'utiliserons pas souvent de tenseurs variables par rapport aux tenseurs constants, mais il est bon de savoir que nous avons une option.

Nous utiliserons tf.Variable pour cr9er un tenseur variable. La diff9rence entre le tenseur constant et le tenseur variable est que vous pouvez changer les donnes dans un tenseur variable, mais vous ne pouvez pas changer les valeurs dans un tenseur constant. Cr9ons un tenseur variable et affichons les dimensions.

```
var_tensor = tf.Variable([
    [
        [1,2,3]
    ],
    [
        [4,5,6]
    ],
    [
        [7,8,9]
    ]
])
print(var_tensor)
```

```
OUTPUT:
<tf.Variable 'Variable:0' shape=(3, 1, 3) dtype=int32, numpy=
array([[[1, 2, 3]],
       [[4, 5, 6]],
       [[7, 8, 9]]], dtype=int32)>
```

# Comment g9n9rer et charger des tenseurs

Voyons comment g9n9rer des tenseurs. Dans la plupart des cas, vous ne cr9erez pas de tenseurs 0 partir de z9ro. Vous chargerez soit un ensemble de donnes, convertirez d'autres ensembles de donnes comme des tableaux NumPy en tenseurs, ou g9n9rerez des tenseurs. Commen7ons par voir comment g9n9rer des tenseurs.

Cr9ons un tenseur avec des valeurs al9atoires. Il existe deux fa7ons courantes de le faire : g9n9rer une distribution normale de donnes ou une distribution uniforme de donnes.

![Image](https://miro.medium.com/max/1050/0*tRWkwBjuQvgi2rGG.png)
_Distribution normale_

La distribution normale est une courbe en forme de cloche qui repr9sente la distribution des donnes. La plupart des donnes seront proches de la moyenne et moins de donnes seront 9loignes de la moyenne. Cela signifie que la probabilit9 d'obtenir une valeur proche de la moyenne est plus 9leve.

![Image](https://miro.medium.com/max/1050/0*SOM1PR1htTNzuRMS.png)
_Distribution uniforme_

La distribution uniforme est une ligne droite qui repr9sente la distribution des donnes. Toutes les valeurs dans une distribution uniforme auront une probabilit9 9gale de se produire dans une plage donne.

Avant de g9n9rer des valeurs al9atoires, vous devez comprendre ce qu'est une graine. Si nous utilisons une valeur de graine, nous pouvons reg9n9rer le m9me ensemble de donnes plusieurs fois. Cela sera utile lorsque nous voudrons tester notre mod9le de machine learning contre les m9mes donnes apr9s avoir ajust9 ses performances.

Cr9ons deux tableaux de tenseurs al9atoires. Nous allons d'abord d9finir une graine et g9n9rer les valeurs al9atoires en utilisant cette graine.

```
seed = tf.random.Generator.from_seed(42)
```

Maintenant, nous allons cr9er une distribution normale et uniforme avec la forme 3 par 2.

```
normal_tensor = seed.normal(shape=(3,2))
print(normal_tensor)
uniform_tensor = seed.uniform(shape=(3,2))
print(uniform_tensor)
```

```
OUTPUT:
tf.Tensor( [[-0.7565803  -0.06854702]  [ 0.07595026 -1.2573844 ]  [-0.23193765 -1.8107855 ]], shape=(3, 2), dtype=float32)
tf.Tensor( [[0.7647915  0.03845465]  [0.8506975  0.20781887]  [0.711869   0.8843919 ]], shape=(3, 2), dtype=float32)
```

Nous avons cr99 deux tenseurs, l'un avec une distribution normale de nombres al9atoires et l'autre avec une distribution uniforme de nombres al9atoires.

Ensuite, nous allons cr9er un tenseur avec des z9ros et des uns. Dans TensorFlow, les tenseurs remplis de z9ros ou de uns sont souvent utilis9s comme point de d9part pour cr9er d'autres tenseurs. Ils peuvent 9galement atre des espaces r9serv9s pour les entr9es dans un graphe de calcul.

Pour cr9er un tenseur de z9ros, utilisez la fonction tf.zeros avec une forme comme argument d'entre. Pour cr9er un tenseur avec des uns, nous utilisons tf.ones avec la forme comme argument d'entre.

```
zeros = tf.zeros(shape=(3,2))
print(zeros)
ones = tf.ones(shape=(3,2))
print(ones)
```

```
OUTPUT:
tf.Tensor(
[[0. 0.]
 [0. 0.]
 [0. 0.]], shape=(3, 2), dtype=float32)
tf.Tensor(
[[1. 1.]
 [1. 1.]
 [1. 1.]], shape=(3, 2), dtype=float32)
```

Maintenant, voyons comment convertir des tableaux NumPy en tenseurs. Si vous ne savez pas [ce qu'est NumPy](https://numpy.org/), c'est une biblioth9que Python pour le calcul num9rique. Elle nous aide 0 g9rer de grands ensembles de donnes et 0 effectuer une vari9t9 de calculs sur eux.

Importons NumPy et cr9ons un tableau NumPy en utilisant la fonction arrange de NumPy.

```
import numpy as np
numpy_arr = np.arange(1,25,dtype=np.int32)
```

Maintenant, nous pouvons cr9er un tenseur en utilisant la fonction tf.constant avec le tableau NumPy comme entre. TensorFlow a un support int9gr9 pour g9rer les tableaux NumPy, donc il suffit d'importer un tableau NumPy et de d9finir une forme.

```
print(numpy_arr)
numpy_tensor = tf.constant(numpy_arr,shape=[2,4,3])
print(numpy_tensor)
```

```
OUTPUT:
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
tf.Tensor(
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]
 [[13 14 15]
  [16 17 18]
  [19 20 21]
  [22 23 24]]], shape=(2, 4, 3), dtype=int32)
```

Vous pouvez voir 0 la fois le tableau NumPy ainsi que notre tenseur. Le tableau NumPy original 9tait de 1x12 mais notre tenseur est de 2x4x3. Cela s'appelle le remodelage d'un tenseur, que nous ferons souvent lors de l'entraînement de rseaux de neurones profonds.

# Op9rations de base utilisant TensorFlow

Nous avons appris comment les tenseurs sont cr99s dans TensorFlow. Maintenant, voyons quelques op9rations de base utilisant des tenseurs.

Nous allons commencer par obtenir quelques informations sur nos tenseurs. Cr9ons un tenseur 4D avec des valeurs 0 avec la forme 2x3x4x5.

```
rank4_tensor = tf.zeros([2,3,4,5])
print(rank4_tensor)
```

```
OUTPUT:
tf.Tensor(
[[[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]
 [[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]], shape=(2, 3, 4, 5), dtype=float32)
```

Nous avons cr99 notre tenseur de rang 4. Maintenant, obtenons quelques informations sur la taille, la forme (nombre de valeurs) et la dimension du tenseur.

Nous utiliserons la fonction tf.size pour obtenir la taille. Les propri9t9s shape et ndim nous donneront la forme et les dimensions du tenseur.

```
print("Size",tf.size(rank4_tensor))
print("shape",rank4_tensor.shape)
print("Dimension",rank4_tensor.ndim)
```

```
OUTPUT: 

Size tf.Tensor(120, shape=(), dtype=int32)
shape (2, 3, 4, 5)
Dimension 4
```

Regardons quelques calculs simples en utilisant le tenseur. Je vais cr9er un nouveau tenseur de base.

```
basic_tensor = tf.constant([[10,11],[12,13]])
print(basic_tensor)
```

```
OUTPUT: 

tf.Tensor(
[[10 11]
 [12 13]], shape=(2, 2), dtype=int32)
```

Essayons quelques op9rations simples. Nous pouvons ajouter, soustraire, multiplier et diviser chaque valeur dans un tenseur en utilisant les op9rateurs de base.

```
print(basic_tensor + 10)
print(basic_tensor - 10)
print(basic_tensor * 10)
print(basic_tensor / 10)
```

```
OUTPUT:
tf.Tensor(
[[20 21]
 [22 23]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[0 1]
 [2 3]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[100 110]
 [120 130]], shape=(2, 2), dtype=int32)
tf.Tensor(
[[1.  1.1]
 [1.2 1.3]], shape=(2, 2), dtype=float64)
```

Maintenant, essayons la multiplication de matrices. Je vais cr9er deux tenseurs simples tensor_011 et tensor_012.

```
tensor_011 = tf.constant([[2,2],[4,4]])
tensor_012 = tf.constant([[2,3],[4,5]])
```

Gardez 0 l'esprit que dans la multiplication de matrices, les dimensions int9rieures doivent correspondre. Par exemple, une multiplication (3, 5) * (3, 5) ne fonctionnera pas, mais (3, 5) * (5, 3) fonctionnera.

La forme finale de la matrice r9sultante sera sa dimension ext9rieure. Donc, un tenseur 3x5 multipli9 par un tenseur 5x3 nous donnera un tenseur 5x5. Nous utiliserons la fonction tf.matmul pour effectuer la multiplication de matrices.

```
print(tf.matmul(tensor_011,tensor_012))
```

```
OUTPUT:
tf.Tensor(
[[12 16]
 [24 32]], shape=(2, 2), dtype=int32)
```

Ensuite, regardons le remodelage et la transposition d'une matrice. Comme nous l'avons vu auparavant, nous utiliserons souvent le remodelage pour changer la structure de notre matrice lors de l'entraînement de rseaux de neurones.

Par exemple, une matrice de pixels d'image de 28x28 sera convertie en un tableau de pixels 0 une dimension de 784 pour un rseau de neurones de classification d'images.

Pour remodeler, nous utilisons la fonction tf.reshape. Pour transposer, nous utilisons la fonction tf.transpose. Si vous ne savez pas ce qu'est une transpose, c'est la conversion des lignes en colonnes et des colonnes en lignes.

```
print(tf.reshape(tensor_011,[4,1]))
print(tf.transpose(tensor_011))
```

```
OUTPUT:
tf.Tensor(
[[2]
 [2]
 [4]
 [4]], shape=(4, 1), dtype=int32)
tf.Tensor(
[[2 4]
 [2 4]], shape=(2, 2), dtype=int32)
```

Enfin, regardons quelques op9rations d'agr9gation comme min, max, 9cart-type, carr9 et racine carre.

Pour trouver les valeurs minimale et maximale, nous utilisons les fonctions tf.reduce_min et tf.reduce_max. Et pour trouver la somme du tableau, nous utilisons la fonction tf.reduce_sum.

```
tensor_013 = tf.constant([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],dtype='float32')
print(tf.reduce_min(tensor_013))
print(tf.reduce_max(tensor_013))
print(tf.reduce_sum(tensor_013))
```

```
OUTPUT:
tf.Tensor(1.0, shape=(), dtype=float32)
tf.Tensor(9.0, shape=(), dtype=float32)
tf.Tensor(45.0, shape=(), dtype=float32)
```

Maintenant, pour l'9cart-type et la variance, nous utilisons la fonction tf.math.reduce_std et la fonction tf.math.reduce_variance.

```
print(tf.math.reduce_std(tensor_013))
print(tf.math.reduce_variance(tensor_013))
```

```
OUTPUT:
tf.Tensor(2.5819888, shape=(), dtype=float32)
tf.Tensor(6.6666665, shape=(), dtype=float32)
```

Trouvons le carr9, la racine carre et le logarithme de chaque valeur dans un tenseur.

```
print(tf.sqrt(tensor_013))
print(tf.square(tensor_013))
print(tf.math.log(tensor_013))
```

```
OUTPUT:
tf.Tensor(
[[1.        1.4142135 1.7320508]
 [2.        2.236068  2.4494898]
 [2.6457512 2.828427  3.       ]], shape=(3, 3), dtype=float32)
tf.Tensor(
[[ 1.  4.  9.]
 [16. 25. 36.]
 [49. 64. 81.]], shape=(3, 3), dtype=float32)
tf.Tensor(
[[0.        0.6931472 1.0986123]
 [1.3862944 1.609438  1.7917595]
 [1.9459102 2.0794415 2.1972246]], shape=(3, 3), dtype=float32)
```

Nous avons appris les bases de TensorFlow dans cet article. Vous ates maintenant 9quip9 pour travailler avec TensorFlow et l'utiliser pour mod9liser des donnes.

Si vous souhaitez commencer 0 utiliser ces connaissances et construire un projet, vous pouvez consulter mon cours sur la [construction d'un rseau de neurones de reconnaissance d'9criture 0 la main en utilisant TensorFlow](https://learn.manishmshiva.com/tensorflow-basics-handwriting-recognition-using-computer-vision). Vous pouvez 9galement apprendre des concepts avanc9s de TensorFlow en utilisant la [documentation officielle](https://www.tensorflow.org/overview).

## Conclusion

TensorFlow est une biblioth9que puissante pour construire des mod9les de deep learning. Elle dispose de tous les outils dont nous avons besoin pour construire des rseaux de neurones afin de r9soudre des probl9mes comme la classification d'images, l'analyse des sentiments, les pr9dictions du march9 boursier, etc.

Avec l'av8nement de technologies comme ChatGPT, apprendre TensorFlow vous donnera une longueur d'avance sur le march9 du travail actuel.

_J'esp8re que vous avez aim9 cet article. Vous pouvez en apprendre plus sur moi et mes articles/vid9os sur_ [_manishmshiva.com_](https://www.manishmshiva.com/)_._