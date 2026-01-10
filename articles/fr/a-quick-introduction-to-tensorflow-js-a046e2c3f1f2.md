---
title: Une introduction rapide à TensorFlow.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T18:22:49.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-tensorflow-js-a046e2c3f1f2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TqGRmDuim8mReF9m.
tags:
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: TensorFlow
  slug: tensorflow
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide à TensorFlow.js
seo_desc: 'By Pau Pavón

  TensorFlow has been around for a while now. Until last month, though, it was only
  available for Python and a few other programming languages, like C and Java. And
  you might think those would be more than enough.

  I had heard of TensorFlow...'
---

Par Pau Pavón

TensorFlow existe depuis un certain temps. Jusqu'au mois dernier, cependant, il n'était disponible que pour Python et quelques autres langages de programmation, comme C et Java. Et vous pourriez penser que cela serait plus que suffisant.

J'avais entendu parler de TensorFlow dans le passé. Même si je ne savais rien sur l'apprentissage automatique ou profond, j'étais assez sûr que c'était l'un des frameworks les plus utilisés pour ces fins. J'avais vu beaucoup de choses cool faites avec : la détection d'objets dans les images, la reconnaissance vocale, et même la composition musicale !

Imaginez pouvoir faire toutes ces choses cool de ML dans le navigateur, sans installer de bibliothèques et sans avoir à compiler toutes ces lignes de code encore et encore. Eh bien, c'est ce que TensorFlow.js est venu faire.

Si vous voulez en savoir plus sur la façon et la raison pour lesquelles ce framework incroyable a vu le jour, vous pouvez consulter [TensorFlow](https://www.freecodecamp.org/news/a-quick-introduction-to-tensorflow-js-a046e2c3f1f2/undefined) ici sur Medium !

Dès que j'ai découvert cela, j'ai voulu commencer à apprendre comment TensorFlow.js fonctionne. Et c'est exactement ce que j'ai commencé à faire : j'ai trouvé [une série de tutoriels par The Coding Train sur YouTube](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YIeVA3dNxbR9PYj4wV31oQ), qui sont toujours en cours (en fait, ils viennent de commencer) et j'ai commencé à m'amuser un peu avec les choses.

Je voudrais vous donner une introduction rapide à TensorFlow (TF) afin que vous puissiez me suivre tout au long de mon voyage et apprendre avec moi.

### Les bases de TensorFlow.js

Commençons ! Tout d'abord, vous devez savoir que toute la documentation se trouve sur [le site web de TF](https://js.tensorflow.org/), sous la section Référence de l'API.

> Mais attendez, pourquoi s'appelle-t-il TensorFlow ? Qu'est-ce qu'un tenseur ?

Je vous en prie. Un tenseur est essentiellement une structure de nombres. En mathématiques, il existe différentes façons de représenter les nombres. Vous pouvez avoir simplement le nombre lui-même, un vecteur, une matrice, et ainsi de suite. Un tenseur est simplement un terme général pour toutes ces différentes représentations de données.

Dans TF, les tenseurs sont différenciés par leur **rang**, ou, en d'autres termes, le nombre de **dimensions** qu'ils ont.

Ce sont les plus courants :

#### Scalaire (rang-0)

Juste un nombre. Voici comment vous pouvez en créer un et l'afficher dans la console :

```
tf.scalar(4.5).print();
```

Et la sortie est la suivante :

```
Tensor  4.5
```

#### Tensor1d, tensor2d, tensor3d et tensor4d (rang- 1, 2, 3 et 4 respectivement)

Ce sont des tenseurs de dimensions supérieures. Si vous vouliez créer un tenseur de rang-1, par exemple, vous pourriez simplement faire :

```
tf.tensor1d([3, 7, 8]).print();
```

Ce qui donnerait :

```
Tensor  [3, 7, 8]
```

#### Tensor (rang-n)

Si vous ne connaissez pas les dimensions de votre tenseur, vous pouvez simplement en créer un avec la fonction suivante (remarquez comment les deux exemples ci-dessus fonctionnent tout aussi bien avec cette autre méthode) :

```
tf.tensor(4.5).print();tf.tensor([3, 7, 8]).print();
```

Cela donne exactement la même sortie qu'avant.

Vous pouvez, en outre, passer un couple de paramètres supplémentaires à ces fonctions.

#### tf.tensor(values, shape?, dtype?)

Commençons par **values**. C'est le seul paramètre obligatoire, et le seul que nous avons passé dans les exemples précédents. Vous pouvez soit passer un tableau plat de valeurs (ou même un seul nombre dans les scalaires) et spécifier la forme vous-même, soit vous pouvez passer un tableau imbriqué.

Maintenant, vous vous demandez peut-être ce qu'est **shape**. Alors, disons que vous voulez sortir le tenseur suivant :

```
[[1, 5], [4, 7]]
```

C'est-à-dire, vous avez deviné juste, une matrice 2x2. Vous pouvez soit créer ce tenseur en passant un tableau plat et en spécifiant la forme comme deuxième paramètre de la fonction

```
tf.tensor([1, 5, 4, 7], [2, 2]).print();
```

ou en passant un tableau imbriqué

```
tf.tensor([[1, 5], [4, 7]]).print();
```

Enfin, nous avons **dtype**. Cela spécifie le type de données. Pour l'instant, **int32, float32** et **bool** sont les trois types supportés.

#### Opérations

Mais, que pouvez-vous faire avec ces tenseurs ? Eh bien, entre autres choses, vous pouvez effectuer des calculs mathématiques sur eux, comme des opérations arithmétiques :

**Note** : les opérations suivantes sont effectuées élément par élément, ce qui signifie que chaque terme du premier tenseur impliqué est associé au terme à sa même place dans l'autre tenseur.

```
const a = tf.tensor1d([4, 7, 2, 1]);const b = tf.tensor1d([20, 30, 40, 50]);
```

Il y a deux façons d'additionner ces deux tenseurs :

```
a.add(b).print();
```

ou,

```
tf.add(a, b);
```

Les deux donnent :

```
Tensor  [24, 37, 42, 51]
```

Voici comment ils fonctionnent pour la soustraction,

```
tf.sub(a, b).print();
```

```
Tensor //output  [-16, -23, -38, -49]
```

la multiplication,

```
tf.mul(a, b).print();
```

```
Tensor //output  [80, 210, 80, 50]
```

et la division :

```
tf.div(a, b).print();
```

```
Tensor //output  [0.2, 0.2333333, 0.05, 0.02]
```

C'est assez simple et direct.

### Essayez par vous-même !

Si vous ne l'avez pas encore fait, je vous encourage à essayer ce qui précède par vous-même. Ce sont les bases les plus élémentaires de TF, mais ces concepts sont clés pour comprendre les parties plus complexes (et plus amusantes) de celui-ci.

Merci d'avoir lu !

Edit : Consultez la [playlist YouTube](https://www.youtube.com/playlist?list=PL1jmMFbLDfgX0Q-rBbfoBdNFl8MS3kTh9) d'ADL sur TensorFlow, je suis sûr qu'elle vous aidera !