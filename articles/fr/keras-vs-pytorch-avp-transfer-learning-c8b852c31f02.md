---
title: 'Keras vs PyTorch : comment distinguer Aliens vs Predators avec l''apprentissage
  par transfert'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T19:02:26.000Z'
originalURL: https://freecodecamp.org/news/keras-vs-pytorch-avp-transfer-learning-c8b852c31f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BFIC_uZzi2v1p2254LLv2Q.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Keras vs PyTorch : comment distinguer Aliens vs Predators avec l''apprentissage
  par transfert'
seo_desc: 'By Patryk Miziuła

  This article was written by Piotr Migdał, Rafał Jakubanis and myself. In the previous
  post, they gave you an overview of the differences between Keras and PyTorch, aiming
  to help you pick the framework that’s better suited to your n...'
---

Par Patryk Miziuła

Cet article a été écrit par [Piotr Migdał](http://p.migdal.pl/), [Rafał Jakubanis](https://medium.com/@rafaljakubanis) et moi-même. Dans le précédent article, ils vous ont donné un [aperçu des différences entre Keras et PyTorch](https://deepsense.ai/keras-or-pytorch/), visant à vous aider à choisir le framework le mieux adapté à vos besoins.

Maintenant, il est temps pour un combat.

Nous allons opposer Keras et PyTorch, montrant leurs forces et faiblesses en action. Nous présentons un problème réel, une question de vie ou de mort : distinguer les Aliens des Predators !

![Image](https://cdn-media-1.freecodecamp.org/images/1*fAS0pLDYQAwRvLiZtzPDCg.jpeg)
_Image tirée de notre dataset. Le Predator et l'Alien sont profondément intéressés par l'IA._

Nous allons effectuer une classification d'images, l'une des tâches de vision par ordinateur où le deep learning excelle. Comme l'entraînement à partir de zéro est irréalisable dans la plupart des cas (car il nécessite beaucoup de données), nous allons effectuer un apprentissage par transfert en utilisant ResNet-50 pré-entraîné sur ImageNet. Nous allons être aussi pratiques que possible, pour montrer à la fois les différences conceptuelles et les conventions.

En même temps, nous allons garder le code assez minimal, pour le rendre clair et facile à lire et à réutiliser. Voir les [notebooks sur GitHub](https://github.com/deepsense-ai/Keras-PyTorch-AvP-transfer-learning), les [kernels Kaggle](https://www.kaggle.com/pmigdal/alien-vs-predator-images/kernels) ou les [versions Neptune avec des graphiques](https://app.neptune.ml/deepsense-ai/Keras-vs-PyTorch).

### Attendez, qu'est-ce que l'apprentissage par transfert ? Et pourquoi ResNet-50 ?

> En pratique, très peu de gens entraînent un réseau de neurones convolutionnel entier à partir de zéro (avec une initialisation aléatoire), car il est relativement rare d'avoir un dataset de taille suffisante. Au lieu de cela, il est courant de pré-entraîner un ConvNet sur un très grand dataset (par exemple, ImageNet, qui contient 1,2 million d'images avec 1000 catégories), puis d'utiliser le ConvNet soit comme une initialisation, soit comme un extracteur de caractéristiques fixe pour la tâche qui nous intéresse. — _Andrej Karpathy, [Transfer Learning — CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/transfer-learning/)_

L'[apprentissage par transfert](http://cs231n.github.io/transfer-learning/) est un processus qui consiste à apporter de minuscules ajustements à un réseau entraîné sur une tâche donnée pour en effectuer une autre, similaire.

Dans notre cas, nous travaillons avec le modèle ResNet-50 entraîné pour classer les images du dataset [ImageNet](http://image-net.org/index). Il est suffisant pour [apprendre beaucoup de textures et de motifs](https://distill.pub/2017/feature-visualization/) qui peuvent être utiles dans d'autres tâches visuelles, même aussi étranges que ce cas Alien vs. Predator. Ainsi, nous utiliserons beaucoup moins de puissance de calcul pour obtenir de bien meilleurs résultats.

Dans notre cas, nous allons le faire de la manière la plus simple possible :

* garder les couches convolutionnelles pré-entraînées (appelées extracteur de caractéristiques), avec leurs poids gelés, et
* supprimer les couches denses originales et les remplacer par de nouvelles couches denses que nous utiliserons pour l'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BFIC_uZzi2v1p2254LLv2Q.png)

Alors, quel réseau devons-nous choisir comme extracteur de caractéristiques ?

[ResNet-50](http://dgschwend.github.io/netscope/#/preset/resnet-50) est un modèle populaire pour la classification d'images ImageNet (AlexNet, VGG, GoogLeNet, Inception, Xception sont d'autres modèles populaires). Il s'agit d'une architecture de réseau de neurones profond de 50 couches basée sur des [connexions résiduelles](https://blog.waya.ai/deep-residual-learning-9610bb62c355), qui sont des connexions qui ajoutent des modifications à chaque couche, plutôt que de changer complètement le signal.

ResNet était l'état de l'art sur ImageNet en 2015. Depuis, des [architectures plus récentes avec des scores plus élevés sur ImageNet](https://www.eff.org/ai/metrics) ont été inventées. Cependant, elles ne sont pas nécessairement meilleures pour généraliser à d'autres datasets (voir l'article arXiv [Do Better ImageNet Models Transfer Better?](https://arxiv.org/abs/1805.08974)).

D'accord, il est temps de plonger dans le code.

### Que le match commence !

Nous allons configurer notre défi Alien vs. Predator en sept étapes :

0. Préparer le dataset  
1. Importer les dépendances  
2. Créer des générateurs de données  
3. Créer le réseau  
4. Entraîner le modèle  
5. Sauvegarder et charger le modèle  
6. Faire des prédictions sur des images de test

Nous complétons cet article de blog avec du code Python dans des Jupyter Notebooks ([Keras-ResNet50.ipynb](https://github.com/deepsense-ai/Keras-PyTorch-AvP-transfer-learning/blob/master/Keras-ResNet50.ipynb), [PyTorch-ResNet50.ipynb](https://github.com/deepsense-ai/Keras-PyTorch-AvP-transfer-learning/blob/master/PyTorch-ResNet50.ipynb)). Cet environnement est plus pratique pour le prototypage que les scripts bruts, car nous pouvons l'exécuter cellule par cellule et examiner la sortie.

Très bien, c'est parti !

### 0. Préparer le dataset

Nous avons créé un dataset en effectuant une recherche Google avec les mots « alien » et « predator ». Nous avons sauvegardé des miniatures JPG (environ 250×250 pixels) et filtré manuellement les résultats. Voici quelques exemples :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QmyVYru66iPvvWcITUKobg.png)

Nous avons divisé nos données en deux parties :

* Données d'entraînement (347 échantillons par classe) — utilisées pour entraîner le réseau.
* Données de validation (100 échantillons par classe) — non utilisées pendant l'entraînement, mais nécessaires pour vérifier la performance du modèle sur des données précédemment invisibles.

Keras nécessite que les datasets soient organisés en dossiers de la manière suivante :

Si vous voulez voir le processus d'organisation des données en répertoires, consultez le fichier data_prep.ipynb. Vous pouvez télécharger le dataset depuis [Kaggle](https://www.kaggle.com/pmigdal/alien-vs-predator-images).

### 1. Importer les dépendances

D'abord, les détails techniques. Nous supposons que vous avez Python 3.5+, Keras 2.2.2 (avec TensorFlow 1.10.1 en backend) et PyTorch 0.4.1. Consultez le fichier [requirements.txt](https://github.com/deepsense-ai/Keras-PyTorch-AvP-transfer-learning/blob/master/requirements.txt) dans le dépôt.

Donc, d'abord, nous devons importer les modules requis. Nous allons séparer le code en Keras, PyTorch et commun (requis dans les deux).

Nous pouvons vérifier les versions des frameworks en tapant `keras.__version__` et `torch.__version__`, respectivement.

### 2. Créer des générateurs de données

Normalement, les images ne peuvent pas toutes être chargées en une fois, car cela serait trop pour la mémoire. En même temps, nous voulons bénéficier de l'augmentation de performance du GPU en traitant quelques images à la fois. Nous chargeons donc les images par _lots_ (par exemple, 32 images à la fois) en utilisant des générateurs de données. Chaque passage à travers l'ensemble du dataset est appelé une _époque_.

Nous utilisons également des générateurs de données pour le prétraitement : nous redimensionnons et normalisons les images pour les rendre comme ResNet-50 les aime (224 x 224 px, avec des canaux de couleur mis à l'échelle). Et enfin, mais non des moindres, nous utilisons des générateurs de données pour perturber aléatoirement les images à la volée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*G4WdPAp5x6Z22WiV4mMBqw.png)

Effectuer de tels changements est appelé _augmentation de données_. Nous l'utiliserons pour montrer à un réseau de neurones quels types de transformations n'ont pas d'importance. Ou, pour le dire autrement, nous allons nous entraîner sur un dataset potentiellement infini en générant de nouvelles images basées sur le dataset original.

Presque toutes les tâches visuelles bénéficient, à des degrés divers, de l'augmentation de données pour l'entraînement. Pour plus d'informations sur l'augmentation de données, voir [appliquée aux photos de plancton](http://benanne.github.io/2015/03/17/plankton.html) ou [comment l'utiliser dans Keras](https://machinelearningmastery.com/image-augmentation-deep-learning-keras/). Dans notre cas, nous appliquons aléatoirement des cisaillements, des zooms et des retournements horizontaux à nos aliens et predators.

Ici, nous créons des générateurs qui :

* chargent les données depuis les dossiers,
* normalisent les données (à la fois l'entraînement et la validation), et
* augmentent les données (uniquement l'entraînement).

Dans Keras, vous obtenez des augmentations intégrées et la méthode `preprocess_input` normalisant les images mises dans ResNet-50, mais vous n'avez aucun contrôle sur leur ordre. Dans PyTorch, vous devez normaliser les images manuellement, mais vous pouvez organiser les augmentations de la manière que vous souhaitez.

Il y a aussi d'autres nuances : par exemple, Keras remplit par défaut le reste de l'image augmentée avec les pixels de bordure (comme vous pouvez le voir sur l'image ci-dessus) tandis que PyTorch le laisse en noir. Chaque fois qu'un framework gère votre tâche beaucoup mieux que l'autre, examinez de plus près pour voir s'ils effectuent le prétraitement de manière identique ; nous parions qu'ils ne le font pas.

### 3. Créer le réseau

L'étape suivante consiste à importer un modèle ResNet-50 pré-entraîné, ce qui est un jeu d'enfant dans les deux cas. Nous allons geler toutes les couches convolutionnelles de ResNet-50 et n'entraîner que les deux dernières couches entièrement connectées (denses). Comme notre tâche de classification n'a que 2 classes (contre 1000 classes d'ImageNet), nous devons ajuster la dernière couche.

Ici, nous :

* chargeons le réseau pré-entraîné, coupons sa tête et gelons ses poids,
* ajoutons des couches denses personnalisées (nous choisissons 128 neurones pour la couche cachée), et
* définissons l'optimiseur et la fonction de perte.

Nous chargeons ResNet-50 depuis Keras et PyTorch sans effort. Ils offrent également de nombreuses autres architectures pré-entraînées bien connues : voir le [zoo de modèles de Keras](https://keras.io/applications/) et le [zoo de modèles de PyTorch](https://pytorch.org/docs/stable/torchvision/models.html). Alors, quelles sont les différences ?

Dans Keras, nous pouvons importer uniquement les couches d'extraction de caractéristiques, sans charger de données superflues (`include_top=False`). Nous créons ensuite un modèle de manière fonctionnelle, en utilisant les entrées et sorties du modèle de base. Ensuite, nous utilisons `model.compile(...)` pour y intégrer la fonction de perte, l'optimiseur et d'autres métriques.

Dans PyTorch, le modèle est un objet Python. Dans le cas de `models.resnet50`, les couches denses sont stockées dans l'attribut `model.fc`. Nous allons les écraser. La fonction de perte et les optimiseurs sont des objets séparés. Pour l'optimiseur, nous devons explicitement passer une liste de paramètres que nous voulons qu'il mette à jour.

Dans PyTorch, nous devons explicitement spécifier ce que nous voulons charger sur le GPU en utilisant la méthode `.to(device)`. Nous devons l'écrire chaque fois que nous voulons mettre un objet sur le GPU, si disponible. Eh bien...

![Image](https://cdn-media-1.freecodecamp.org/images/1*woYU8o65zMwH4UHvjWj7NA.jpeg)
_Cadre de 'AVP : Alien vs. Predator' : l'ordinateur de poignet des Predators. Nous sommes assez sûrs que le Predator pourrait l'utiliser pour calculer logsoftmax._

Le gel des couches fonctionne de manière similaire. Cependant, dans [The Batch Normalization layer of Keras is broken](http://blog.datumbox.com/the-batch-normalization-layer-of-keras-is-broken/) (dans la version actuelle ; merci à Przemysław Pobrotyn pour avoir soulevé ce problème), vous verrez que certaines couches sont modifiées de toute façon, même avec `trainable=False`.

Keras et PyTorch traitent la log-loss de manière différente.

Dans Keras, un réseau prédit des probabilités (a une fonction [softmax](https://medium.com/@uniqtech/understand-the-softmax-function-in-minutes-f3a59641e86d) intégrée), et ses fonctions de coût intégrées supposent qu'elles travaillent avec des probabilités.

Dans PyTorch, nous avons plus de liberté, mais la manière préférée est de retourner des logits. Cela est fait pour des raisons numériques, effectuer softmax puis log-loss signifie faire des opérations `log(exp(x))` inutiles. Donc, au lieu d'utiliser softmax, nous utilisons `LogSoftmax` (et `NLLLoss`) ou les combinons en une seule fonction de perte `nn.CrossEntropyLoss`.

### 4. Entraîner le modèle

D'accord, ResNet est chargé, alors préparons-nous à l'affrontement spatial !

![Image](https://cdn-media-1.freecodecamp.org/images/1*uuFsm4SiVj5TbWtGPtZ0IQ.png)
_Cadre de 'AVP : Alien vs. Predator' : le vaisseau mère des Predators. Oui, nous avons entendu dire qu'il n'y a pas de rumbles dans l'espace, mais rien n'est impossible pour les Aliens et les Predators._

Maintenant, nous allons procéder à l'étape la plus importante — l'entraînement du modèle. Nous devons passer les données, calculer la fonction de perte et modifier les poids du réseau en conséquence. Alors que nous avions déjà quelques différences entre Keras et PyTorch dans l'augmentation des données, la longueur du code était similaire. Pour l'entraînement... la différence est massive. Voyons comment cela fonctionne !

Ici, nous :

* entraînons le modèle, et
* mesurons la fonction de perte (log-loss) et la précision pour les ensembles d'entraînement et de validation.

Dans Keras, `model.fit_generator` effectue l'entraînement... et c'est tout ! L'entraînement dans Keras est aussi simple que cela. Et comme vous pouvez le trouver dans le notebook, Keras nous donne également une barre de progression et une fonction de chronométrage gratuitement. Mais si vous voulez faire quelque chose de non standard, alors la douleur commence...

PyTorch est à l'autre extrémité. Tout est explicite ici. Vous avez besoin de plus de lignes pour construire l'entraînement de base, mais vous pouvez librement changer et personnaliser tout ce que vous voulez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2WwHB_QkewusJM_ELzYXmg.jpeg)
_Shuriken du Predator revenant automatiquement à son propriétaire. Préféreriez-vous implémenter sa capacité de suivi dans Keras ou PyTorch ?_

Changeons de vitesse et analysons le code d'entraînement de PyTorch. Nous avons des boucles imbriquées, itérant sur :

* les époques,
* les phases d'entraînement et de validation, et
* les lots.

La boucle d'époque ne fait rien d'autre que répéter le code à l'intérieur. Les phases d'entraînement et de validation sont faites pour trois raisons :

* Certaines couches spéciales, comme la [normalisation par lots](https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html) (présente dans ResNet-50) et le [dropout](https://deepsense.ai/wp-content/uploads/2018/10/srivastava14a.pdf) (absent dans ResNet-50), fonctionnent différemment pendant l'entraînement et la validation. Nous définissons leur comportement par `model.train()` et `model.eval()`, respectivement.
* Nous utilisons différentes images pour l'entraînement et pour la validation, bien sûr.
* La chose la plus importante et la moins surprenante : nous entraînons le réseau uniquement pendant l'entraînement. Les commandes magiques `optimizer.zero_grad()`, `loss.backward()` et `optimizer.step()` (dans cet ordre) font le travail. Si vous savez ce qu'est la [rétropropagation](https://google-developers.appspot.com/machine-learning/crash-course/backprop-scroll/), vous appréciez leur élégance.

Nous prenons ensuite soin de calculer les pertes d'époque et les impressions nous-mêmes.

### 5. Sauvegarder et charger le modèle

#### Sauvegarde

Une fois notre réseau entraîné, souvent avec des coûts computationnels et temporels élevés, il est bon de le garder pour plus tard. Globalement, il existe deux types de sauvegardes :

* sauvegarder toute l'architecture du modèle et les poids entraînés (et l'état de l'optimiseur) dans un fichier, et
* sauvegarder les poids entraînés dans un fichier (en gardant l'architecture du modèle dans le code).

C'est à vous de choisir la méthode.

Ici, nous :

* sauvegardons le modèle.

Une ligne de code suffit dans les deux frameworks. Dans Keras, vous pouvez soit tout sauvegarder dans un fichier [HDF5](https://www.h5py.org/), soit sauvegarder les poids dans HDF5 et l'architecture dans un fichier JSON lisible. Au fait : [vous pouvez ensuite charger le modèle et l'exécuter dans le navigateur](https://medium.com/tensorflow/train-on-google-colab-and-run-on-the-browser-a-case-study-8a45f9b1474e).

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQupj2OpGHFnD6CrgSaPxA.jpeg)
_Cadre de 'Alien : Résurrection' : l'Alien évolue, tout comme PyTorch._

Actuellement, les créateurs de PyTorch [recommandent de sauvegarder uniquement les poids](https://pytorch.org/docs/stable/notes/serialization.html). Ils déconseillent de sauvegarder tout le modèle car l'API évolue encore.

#### Chargement

Le chargement des modèles est aussi simple que la sauvegarde. Vous devez simplement vous souvenir de la méthode de sauvegarde que vous avez choisie et des chemins des fichiers.

Ici, nous :

* chargeons le modèle.

Dans Keras, nous pouvons charger un modèle à partir d'un fichier JSON, au lieu de le créer en Python (au moins lorsque nous n'utilisons pas de couches personnalisées). Ce type de sérialisation le rend pratique pour transférer des modèles.

PyTorch peut utiliser n'importe quel code Python. Donc, nous devons pratiquement recréer un modèle en Python.

Le chargement des poids du modèle est similaire dans les deux frameworks.

### 6. Faire des prédictions sur des images de test

Très bien, il est enfin temps de faire quelques prédictions ! Pour vérifier équitablement la qualité de notre solution, nous allons demander au modèle de prédire le type de monstres à partir d'images non utilisées pour l'entraînement. Nous pouvons utiliser l'ensemble de validation, ou toute autre image.

Ici, nous :

* chargeons et prétraitons les images de test,
* prédisons les catégories d'images, et
* montrons les images et les prédictions.

La prédiction, comme l'entraînement, fonctionne par lots (ici nous utilisons un lot de 3 ; bien que nous puissions certainement aussi utiliser un lot de 1).

Dans Keras et PyTorch, nous devons charger et prétraiter les données. Une erreur de débutant est d'oublier l'étape de prétraitement (y compris la mise à l'échelle des couleurs). Cela peut fonctionner, mais entraînera des prédictions moins bonnes (puisqu'il voit effectivement les mêmes formes mais avec des couleurs et des contrastes différents).

Dans PyTorch, il y a deux étapes supplémentaires, car nous devons :

* convertir les logits en probabilités, et
* transférer les données vers le CPU et convertir en NumPy (heureusement, les messages d'erreur sont assez clairs lorsque nous oublions cette étape).

Et voici ce que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*a6XeWuUwwtBjFMfUlN-eyw.png)

Cela fonctionne !

Et qu'en est-il des autres images ? Si vous ne trouvez rien (ou personne) d'autre, essayez d'utiliser des photos de vos collègues. 😉

### Conclusion

Comme vous pouvez le voir, Keras et PyTorch diffèrent considérablement en termes de définition, de modification, d'entraînement, d'évaluation et d'exportation des modèles de deep learning standard. Pour certaines parties, il s'agit purement de différentes conventions d'API, tandis que pour d'autres, des différences fondamentales entre les niveaux d'abstraction sont impliquées.

Keras fonctionne à un niveau d'abstraction beaucoup plus élevé. Il est beaucoup plus plug&play, et généralement plus succinct, mais au détriment de la flexibilité.

PyTorch fournit un code plus explicite et détaillé. Dans la plupart des cas, cela signifie un code débogable et flexible, avec un faible surcoût. Pourtant, l'entraînement est beaucoup plus verbeux dans PyTorch. Cela fait mal, mais cela offre parfois beaucoup de flexibilité.

L'apprentissage par transfert est un grand sujet. Essayez de modifier vos paramètres (par exemple, les couches denses, l'optimiseur, le taux d'apprentissage, l'augmentation) ou choisissez une architecture de réseau différente.

Avez-vous essayé l'apprentissage par transfert pour la reconnaissance d'images ? Considérez la liste ci-dessous pour quelques inspirations :

* [Chihuahua vs. muffin, sheepdog vs. mop, shrew vs. kiwi](https://twistedsifter.com/2016/03/puppy-or-bagel-meme-gallery/) (serve déjà de [benchmark intéressant pour la vision par ordinateur](https://medium.freecodecamp.org/chihuahua-or-muffin-my-search-for-the-best-computer-vision-api-cbda4d6b425d))
* Images originales vs. images photoshopées
* Artichaut vs. brocoli vs. chou-fleur
* Zerg vs. Protoss vs. Orc vs. Elfe
* Meme ou pas meme
* [Est-ce une image d'un oiseau ?](https://xkcd.com/1425/)
* [Est-ce que c'est huggable ?](https://www.reddit.com/r/MachineLearning/comments/4casci/can_i_hug_that_i_trained_a_classifier_to_tell_you/)

Choisissez Keras ou PyTorch, sélectionnez un dataset, et faites-nous savoir comment cela s'est passé dans la section des commentaires ci-dessous 😉

Au fait, en novembre, nous organisons une [série de formations pratiques](https://deepsense.ai/machine-learning-and-deep-learning-training/) où vous pouvez en apprendre davantage sur Keras et PyTorch. Piotr Migdał et moi-même dirigerons certaines des sessions, alors n'hésitez pas à y jeter un coup d'œil.