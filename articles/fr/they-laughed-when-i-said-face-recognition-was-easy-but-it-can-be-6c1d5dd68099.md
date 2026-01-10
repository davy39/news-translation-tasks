---
title: Ils ont ri quand j'ai dit que la reconnaissance faciale était facile. Mais
  c'est le cas.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-29T17:55:45.000Z'
originalURL: https://freecodecamp.org/news/they-laughed-when-i-said-face-recognition-was-easy-but-it-can-be-6c1d5dd68099
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QhDzUIIwZVJBgaiKx4yBDA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Ils ont ri quand j'ai dit que la reconnaissance faciale était facile. Mais
  c'est le cas.
seo_desc: 'By Tirmidzi Faizal Aflahi

  Maybe you have seen it before. Maybe some of you use a face unlock feature that
  some phones have. This technology called Face Recognition is simply amazing. But,
  do you think it is hard to make an application based on that t...'
---

Par Tirmidzi Faizal Aflahi

Peut-être l'avez-vous déjà vu. Peut-être que certains d'entre vous utilisent la fonctionnalité de **déverrouillage par reconnaissance faciale** que [certains téléphones](https://www.theverge.com/circuitbreaker/2018/1/2/16840174/oneplus-5-face-unlock-oxygenos-open-beta) possèdent. Cette technologie appelée reconnaissance faciale est tout simplement incroyable. Mais, pensez-vous qu'il est difficile de créer une application basée sur cette technologie ? En réalité, ce n'est pas si difficile. Vous pouvez même le faire avec **moins de 10 lignes de code** ! Sérieusement. Voici mon tutoriel Tensorflow sur la reconnaissance faciale, spécialement pour vous.

### TL;DR

Voici le code, au cas où **_vous ne voudriez pas lire_** l'article. LOL.

```py
from easyfacenet.simple import facenet

images = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']
aligned = facenet.align_face(images)
comparisons = facenet.compare(aligned)

print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))
```

Et cela produira le résultat suivant :

```
Is image 1 and 2 similar?  True
Is image 1 and 3 similar?  False
```

Attendez, attendez. Pas de Tensorflow ? Bien sûr qu'il y en a. Pour ce tutoriel, j'utilise un algorithme appelé [Facenet](https://github.com/davidsandberg/facenet) qui a été développé avec Tensorflow. Et bien qu'il soit assez facile pour moi d'utiliser Facenet directement en codant la syntaxe Tensorflow, je ne pense pas que la plupart d'entre vous seraient à l'aise avec cela.

J'ai donc décidé de créer une autre interface par-dessus Facenet, que j'ai appelée [**Easy Facenet**](https://pypi.org/project/easyfacenet/). Pour installer la bibliothèque, il vous suffit de taper

```
pip install easyfacenet
```

Et vous êtes prêt à partir !

L'article ne devrait pas se terminer comme ça, n'est-ce pas ? _Bien sûr que non_.

Permettez-moi de vous expliquer, ligne par ligne, le tutoriel. En même temps, nous allons voir comment fonctionne la reconnaissance faciale en premier lieu.

### Reconnaissance faciale

![Image](https://cdn-media-1.freecodecamp.org/images/3DTIxnKPDarQyYXo88QGaPdggaYX85v6MyjF)
_Photo par [Unsplash](https://unsplash.com/photos/WiONHd_zYI4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Tianyi Ma</a> sur <a href="https://unsplash.com/search/photos/macbook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Alors, comment fonctionne la reconnaissance faciale ?

![Image](https://cdn-media-1.freecodecamp.org/images/xMHPbNlxw6NaWR4CtHNusWK1dR7bJXT7ov21)
_Courtoisie de [OpenFace](http://cmusatyalab.github.io/openface/" rel="noopener" target="_blank" title=")_

Comme vous pouvez le voir sur l'image ci-dessus, les étapes sont les suivantes :

1. Obtenir une image **d'entrée** qui doit **contenir un visage**(s)
2. Vous devez trouver où se trouve exactement le visage et **placer une boîte de délimitation autour du visage**
3. Pour la cohérence de l'algorithme, vous devez **transformer l'image**, de sorte que la position de la bouche, du nez et des yeux soit cohérente pour différentes images.
4. Ensuite, **recadrer l'image**
5. Entrer l'image recadrée dans l'**algorithme Facenet**, qui est un réseau de neurones profond.
6. Il produira une **représentation vectorielle** de ce visage. C'était un vecteur de 128 dimensions auparavant, maintenant c'est un vecteur de 512 dimensions.
7. Ensuite, vous pouvez faire ce que vous voulez avec cette représentation. Vous pouvez faire de la **classification**, du **clustering**, ou simplement utiliser un **calcul de similarité** entre les images.

Wow, c'était beaucoup de choses. Pourquoi est-ce si difficile ? Eh bien, en gros, vous pouvez regrouper ces 7 étapes en 3 étapes, qui sont,

1. **Alignement**, entrer une image et sortir le visage recadré aligné
2. **Intégration**, entrer le visage et sortir la représentation
3. **Comparaison**, comparer ces représentations — sont-elles similaires ou non ?

Parce qu'il n'y a que 3 étapes simples, le code devrait être aussi simple que cela, n'est-ce pas ?

Oui, cela peut être le cas, en utilisant **easyfacenet**.

### La bibliothèque Tensorflow de reconnaissance faciale la plus simple disponible

Décomposons le code bit par bit.

```py
from easyfacenet.simple import facenet
```

Importer le fichier _facenet_ depuis un module _simple_. Il y a trois méthodes que vous pouvez utiliser à l'intérieur du fichier. Ce sont, **align_face**, **embedding**, et **compare**.

Facilement, vous pouvez dire que chacune de ces méthodes représente chaque étape pour la reconnaissance faciale.

```py
images = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']
```

Maintenant, nous pouvons définir les images. Quelles sont ces images ? Eh bien, _celle-ci_.

![Image](https://cdn-media-1.freecodecamp.org/images/NBYPXP4BP9RJC2p6HPWbrA-gqx58OyqqbSVZ)
_Une photo de moi (image1.jpg)_

Et _celle-ci_.

![Image](https://cdn-media-1.freecodecamp.org/images/9Caduw4e7kq6XEEy2M3IqBWMzB5OoR0loQLh)
_Une autre photo de moi (image2.jpg)_

Et aussi _celle-ci_.

![Image](https://cdn-media-1.freecodecamp.org/images/1w9-X2Sxef4YMgYvsVNGf7OQRlCPzenTSXOO)
_Mon petit frère (image3.jpg)_

Nous avons les images. Maintenant, passons aux choses sérieuses.

### Étape 1. Alignement

```py
aligned = facenet.align_face(images)
```

La bibliothèque va essayer de trouver le visage à l'intérieur de l'image et recadrer le visage ainsi que [pré-blanchir](https://github.com/davidsandberg/facenet/issues/433) le visage. Le **pré-blanchiment** rendra l'entraînement plus facile au moment de l'entraînement, donc au moment de l'inférence, vous devrez également pré-blanchir l'image.

Le visage aligné pré-blanchi ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/CBCceYCyVyGh1er8p-Nl4mKgQxCIeVF49NwX)
_Image 1 à 3 de gauche à droite_

Maintenant, vous êtes prêt pour l'étape suivante. Prenez une pause et mâchez lentement !

### Étape 2. Intégrations

Attendez, attendez. Je ne vois pas d'intégrations dans l'exemple ci-dessus ? Eh bien, c'est parce que **la méthode de comparaison a déjà appelé l'intégration à l'intérieur**. Si vous voulez utiliser l'intégration d'une manière ou d'une autre, utilisez ceci.

```py
embeddings = facenet.embedding(aligned)
```

Les **intégrations** ressembleront à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/FkVJ2zmPEJyxo2uTVrctJEFPbq8jIXTT1iNs)
_Je ne vous recommande pas de regarder les nombres_

### Étape 3. Comparaison

```py
comparisons = facenet.compare(aligned)
```

Si vous avez 3 images, la variable **comparisons** aura 3 x 3 valeurs. Qui sont des **permutations** de chaque image comparée à chacune des autres. Par exemple, si vous voulez obtenir « **_l'image 1 est-elle similaire à l'image 2 ?_** », alors

```py
print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
```

**_L'image 1 est-elle similaire à l'image 3 ?_**

```py
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))
```

Vous n'avez pas déjà oublié que le tableau est indexé à zéro, n'est-ce pas ? Haha...

**Et, c'est tout**. Vous pouvez obtenir votre résultat de comparaison comme ça. La technique de comparaison que j'ai utilisée est la **similarité cosinus**. Vous pouvez utiliser n'importe quelle autre méthode de similarité que vous voulez. Vous pouvez définitivement utiliser une autre méthode comme le clustering ou la classification. Quelque chose comme le [Siamese Network](https://medium.com/@kuzuryu71/improving-siamese-network-performance-f7c2371bdc1e) est ce dont vous avez besoin.

### Que pouvez-vous faire ensuite ?

![Image](https://cdn-media-1.freecodecamp.org/images/61vE2pz5ezVb6SsLi3MzCzXg78COBEnKPi8j)
_Photo par [Unsplash](https://unsplash.com/photos/tMI2_-r5Nfo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Corinne Kutz</a> sur <a href="https://unsplash.com/search/photos/macbook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Comme je l'ai dit, c'est la **bibliothèque Tensorflow de reconnaissance faciale la plus simple disponible.** Vous pouvez donc commencer à faire ce que vous voulez aussi rapidement que possible.

Si vous êtes du genre bidouilleur, vous pouvez explorer la bibliothèque et créer le vrai code Tensorflow de reconnaissance faciale. Jetez un coup d'œil au code [ici](https://github.com/taflahi/facenet/blob/master/simple/facenet.py) car c'est la pierre angulaire de la bibliothèque. De plus, étendez le code ou vous pouvez créer votre propre fonctionnalité.

### Réflexions finales

Si vous voulez en savoir plus sur le **document** derrière cette technologie incroyable, vous pouvez regarder [ici](https://arxiv.org/abs/1503.03832) ainsi que [ici](http://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf).

En conclusion, l'utilisation d'easyfacenet peut vous aider énormément dans la création de votre projet de reconnaissance faciale. De plus, cette bibliothèque de reconnaissance faciale est **maintenue** uniquement **par moi.** Il est facile pour vous de demander une certaine fonctionnalité.

En ce qui concerne la mise en œuvre réelle pour l'autre méthode de similarité, je vous y emmènerai dans le prochain tutoriel. Pour cette raison, j'ajouterai la méthode exclusivement à l'intérieur de la bibliothèque.

Enfin, si vous voulez lire l'article original, je l'ai initialement publié sur mon blog ici à [thedatamage](https://thedatamage.com/face-recognition-tensorflow-tutorial/). Bien sûr, vous pouvez y lire beaucoup plus d'articles de ma part.