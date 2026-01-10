---
title: Entraîner un modèle Core ML avec Turi Create pour classer les races de chiens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T15:02:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-train-a-core-ml-model-with-turi-create-to-classify-dog-breeds-bc1d0fa108b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uwijKPq06BeRriP7Xf1faA.jpeg
tags:
- name: iOS
  slug: ios
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Entraîner un modèle Core ML avec Turi Create pour classer les races de
  chiens
seo_desc: 'By Vardhan Kishore Agrawal

  In this tutorial, you’ll learn how to train a custom dog-breed classification Core
  ML model to use in your iOS and macOS apps. Your Core ML model will be able to distinguish
  between five different breeds by the end of this ...'
---

Par Vardhan Kishore Agrawal

Dans ce tutoriel, vous apprendrez à entraîner un modèle Core ML personnalisé pour la classification des races de chiens à utiliser dans vos applications iOS et macOS. Votre modèle Core ML sera capable de distinguer cinq races différentes à la fin de ce tutoriel !

Vous vous souvenez peut-être qu'Apple a acquis la startup de machine learning et d'intelligence artificielle Turi il y a quelques années pour plus de 200 millions de dollars ; elle offre des outils puissants pour créer des modèles avancés de machine learning en un temps record.

Dans ce tutoriel, vous apprendrez à installer Turi Create sur votre Mac, à créer un script Python et à utiliser ce script pour entraîner un modèle Core ML que vous pourrez glisser directement dans vos projets Xcode et implémenter rapidement dans vos applications.

### Commencer

Avant de commencer avec la partie réelle du machine learning, assurons-nous d'abord de l'installation de Turi et Python — et, bien sûr, vous devrez vous assurer que votre matériel et votre logiciel répondent aux exigences de Turi.

#### Exigences

Comme pour tout logiciel que vous installez, Turi Create a des exigences spécifiques, que vous pouvez trouver sur leur [page officielle GitHub](https://github.com/apple/turicreate).

**Turi Create supporte :**

* macOS 10.12+
* Linux (avec glibc 2.12+)
* Windows 10 (via WSL)

**Turi Create nécessite :**

* Python 2.7, 3.5, 3.6
* Architecture x86_64
* Au moins 4 Go de RAM

En résumé, tant que votre Mac est _raisonnablement_ récent, vous devriez pouvoir exécuter Turi Create. Si vous le souhaitez, vous pouvez suivre avec un autre système d'exploitation ; cependant, vous devrez peut-être modifier certaines étapes pour qu'elles fonctionnent.

#### Installation

L'installation de Turi Create est assez simple, surtout si vous êtes familier avec la ligne de commande. Bien que vous puissiez choisir d'utiliser une version plus récente de Python, j'utiliserai Python 2.7 dans ce tutoriel.

Dans macOS Mojave, Python 2.7 est installé par défaut, donc tout ce que vous avez à faire est de vérifier la version. Sur votre Mac, ouvrez **Applications > Utilitaires > Terminal** ou recherchez-le simplement avec le raccourci clavier **Commande-Espace**.

Pour vérifier la version de Python sur votre Mac, entrez :

```bash
$ python -version
```

Cela vous indiquera la version de Python, et votre console devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nLSxumsPp-coRvXZ22pNYcOK24GwXZsV0bmB)
_**Figure 1 :** Vérification de la version de Python_

Si votre version n'est pas Python 2.7, ou si elle n'est pas installée sur votre ordinateur pour une raison quelconque, vous devriez l'installer [à ce lien](https://www.python.org/downloads/release/python-2714/). Si votre sortie ressemble à la mienne, vous êtes prêt à continuer.

> **Note :** Certaines personnes préfèrent utiliser une machine virtuelle pour installer Turi Create puisque c'est ce qu'Apple recommande. Mais pour garder les choses simples, nous allons simplement l'installer directement.

Pour installer Turi Create, entrez simplement ce qui suit dans votre fenêtre de terminal :

```bash
$ pip install turicreate
```

C'est tout ! Turi Create est installé avec succès sur votre Mac et est prêt à être utilisé. Vous pouvez maintenant construire des modèles de classification, de détection, de régression et d'autres types de modèles.

#### Jeu de données

Pour tout modèle de machine learning, vous avez besoin d'un jeu de données. Dans ce tutoriel, vous apprendrez à entraîner un modèle simple de classification de races de chiens, qui nécessite une classification d'images. Les données que j'utiliserai proviennent du [Jeu de données de chiens de l'Université de Stanford](http://vision.stanford.edu/aditya86/ImageNetDogs/).

Pour que Turi puisse reconnaître les images pré-classifiées, vous devrez les organiser en fonction de ce qu'elles représentent. Par exemple, toutes les images de golden retrievers seraient dans un dossier, tandis que toutes les images de labradoodles seraient dans un autre.

Pour simplifier, nous n'utiliserons que cinq races parmi les centaines du jeu de données de Stanford, mais vous pouvez en utiliser autant que vous le souhaitez. J'ai déjà organisé cela pour vous et créé un [dépôt pour cela](https://github.com/vhanagwal/dog-breed-dataset). Si vous choisissez d'ajouter plus de races de chiens, ajoutez simplement plus de dossiers et nommez-les comme vous le souhaitez.

#### Structure des dossiers

À ce stade, vous avez peut-être compris que la manière dont vous organisez votre jeu de données est cruciale pour pouvoir entraîner correctement le modèle — il n'y a pas d'autre moyen pour que Turi Create sache ce qui va où. Prenez un moment pour vous organiser.

![Image](https://cdn-media-1.freecodecamp.org/images/J75WxYJWuv0-0C4VIfnZXtJoPn05EEAsh-2p)
_**Figure 2 :** Structure de dossier de départ_

Ce diagramme hiérarchique devrait tout expliquer, et vous devrez organiser vos dossiers dans cet ordre avant de continuer avec ce tutoriel. Si vous souhaitez changer les noms ou organiser les choses différemment, vous devrez vous assurer de prendre note de cela.

### Entraînement du classifieur

Après avoir terminé la configuration, vous êtes prêt à plonger dans le cœur de ce tutoriel — l'entraînement réel de votre classifieur. Nous travaillerons principalement en Python, mais si vous n'avez jamais utilisé Python auparavant, ce n'est pas grave. Je vais expliquer chaque étape au fur et à mesure, et si vous avez des questions, n'hésitez pas à laisser un commentaire ci-dessous.

#### Fichier Python

Tout d'abord, nous aurons besoin d'un endroit pour mettre nos pensées (c'est-à-dire, bien sûr, en Python). Si vous avez déjà un éditeur qui supporte Python, comme [Atom](https://atom.io) ou un environnement de développement intégré comme [PyCharm](https://www.jetbrains.com/pycharm/), vous pouvez les utiliser pour créer un fichier vide appelé `dog_breeds.py`.

Si vous préférez la route plus développeuse, comme moi, vous pouvez utiliser le Terminal pour faire la même chose. Vous devrez créer ce fichier à l'intérieur de votre dossier `ml_classifier`, aux côtés du dossier `images` afin que votre hiérarchie ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nmjzxj2FQ5g5fECIe5r2wYhcUgL1bOsA8ZJh)
_**Figure 3 :** Structure de dossier avec le fichier Python_

Pour créer un nouveau fichier, entrez d'abord dans le répertoire cible :

```bash
$ cd ml_classifier
```

Ensuite, créez un nouveau fichier nommé `dog_breeds.py`.

```bash
$ touch dog_breeds.py
```

Voilà ! Vos dossiers, fichiers et images sont tous là où ils doivent être, et vous êtes prêt à continuer avec l'étape suivante. Nous utiliserons Xcode pour ouvrir notre fichier, alors assurez-vous de l'avoir installé et à jour.

#### Chargement des images du jeu de données

Enfin, il est temps de commencer à dire à Turi ce qu'il doit faire via le fichier Python que nous venons de créer. Si vous double-cliquez sur le fichier, il devrait s'ouvrir par défaut dans Xcode, si vous l'avez installé. Sinon, vous pouvez également utiliser un autre éditeur ou un IDE Python.

#### 1. Importer les frameworks

```py
import turicreate
```

En haut du fichier, vous devrez importer le framework Turi Create. Si vous le souhaitez, vous pouvez créer un nom de référence en ajoutant `as <votre nom>`. Par exemple, si vous vouliez vous référer à `it` comme tc dans votre code, vous pourriez écrire :

```py
import turicreate as tc
```

Cela vous permettrait de l'appeler `tc` au lieu d'écrire `turicreate`. Dans ce tutoriel, j'utiliserai la version complète, en l'appelant `turicreate` pour réduire l'ambiguïté.

Vous devrez également gérer les noms de dossiers et autres tâches liées au système d'exploitation afin de classer vos images. Cela nécessitera une autre bibliothèque Python appelée `os`. Pour l'importer, ajoutez simplement ce qui suit :

```py
import os
```

#### 2. Chargement des images

```py
data = turicreate.image_analysis.load_images("images/")
```

Ici, nous stockons toutes les images de notre jeu de données dans une variable appelée `data`. Puisque notre fichier `dog_breeds.py` est dans le même répertoire que le dossier `images`, nous pouvons simplement mettre `images/` comme chemin.

#### 3. Définition des étiquettes

Maintenant que Turi Create a toutes vos images, vous devez lier les noms de dossiers à un nom d'étiquette. Ces noms d'étiquettes sont ce qui sera retourné dans votre modèle Core ML lorsqu'il sera utilisé dans une application iOS ou MacOS.

```py
data["label"] = data["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))
```

Cela vous permet de mapper tous vos noms de dossiers à un nom d'étiquette, ce qui indique à Turi Create que toutes les images qui sont dans le dossier cocker_spaniel sont effectivement des Cocker Spaniels, par exemple.

#### 4. Sauvegarder en tant que `SFrame`

Au cas où vous ne seriez pas familier avec un `SFrame`, en termes simples, c'est un dictionnaire de toutes vos données (dans ce cas, une image) et de toutes les étiquettes (dans ce cas, la race de chien). Sauvegardez votre `SFrame` comme ceci :

```py
data.save("dog_classifier.sframe")
```

Cela vous permet de stocker vos images étiquetées pour une utilisation dans l'étape suivante. Il s'agit d'un type de données assez standard dans l'industrie du machine learning.

### Entraînement et test

Après que Turi Create ait toutes vos images étiquetées en place, il est temps d'entrer dans la ligne droite et de finalement entraîner votre modèle. Nous devons également diviser les données de sorte que 80 % soient utilisées pour l'entraînement et 20 % soient sauvegardées pour tester le modèle une fois qu'il a terminé l'entraînement — nous n'aurons pas à le tester manuellement.

#### 1. Chargement du SFrame

Maintenant, nous devons charger le SFrame que nous venons de créer à l'étape précédente. C'est ce que nous utiliserons pour diviser en données de test et d'entraînement plus tard.

```py
data = turicreate.SFrame("dog_classifier.sframe")
```

Cela assigne la variable `data`, qui est maintenant de type `SFrame`, au SFrame que nous avons sauvegardé à l'étape précédente. Maintenant, nous devrons diviser les données en données de test et d'entraînement. Comme mentionné précédemment, nous allons faire une division 80:20 des données de test et d'entraînement.

#### 2. Division des données

Il est temps de diviser les données. Après votre code SFrame, ajoutez ce qui suit :

```py
testing, training = data.random_split(0.8)
```

Ce code divise aléatoirement les données 80-20 et les assigne à deux variables, `testing` et `training`, respectivement. Maintenant, Turi testera automatiquement votre modèle sans que vous ayez besoin de fournir manuellement des images de test et de créer une application — si vous devez faire des ajustements, vous n'aurez pas besoin de l'implémenter complètement d'abord, et au lieu de cela, vous pourrez les faire directement dans votre fichier Python.

#### 3. Entraînement, test et exportation

Votre travail acharné a enfin porté ses fruits ! Dans cette ligne de code Python, vous direz simplement à Turi Create d'entraîner votre modèle, tout en spécifiant l'architecture que vous souhaitez utiliser.

```py
classifier = turicreate.image_classifier.create(testing, target="label", model="resnet-50")
```

Vous dites simplement à Turi d'utiliser vos données de `testing` (spécifiées précédemment), et de les utiliser pour prédire les `labels` (basés sur la structure de dossier précédente), tout en utilisant `resnet-50`, qui est l'une des architectures de modèles de machine learning les plus précises.

Pour utiliser vos données de test et vous assurer que votre modèle est précis, ajoutez ceci :

```py
testing = classifier.evaluate(training)print testing["accuracy"]
```

Cela utilise les données de `training` que vous avez spécifiées et stocke les résultats après le test dans une variable appelée (vous l'avez deviné) `testing`. Pour votre information, il imprime la précision, mais vous pouvez également imprimer d'autres choses, donné assez de temps sur les API de Turi Create.

Dernier point mais non des moindres, vous pouvez sauvegarder votre modèle directement dans votre système de fichiers avec cette ligne après lui avoir donné un nom utile :

```py
classifier.save("dog_classifier.model")classifier.export_coreml("dog_classifier.mlmodel")
```

Bien sûr, vous pouvez également sauvegarder votre modèle dans d'autres formats, mais pour cet exemple, je l'ai sauvegardé en tant que modèle Core ML.

### Exécution et sortie

Pour tous les développeurs iOS là-bas — non, ce n'est pas un projet Xcode qui continue à compiler automatiquement et à se plaindre des erreurs. Afin que le code que vous venez d'écrire s'exécute, nous devons le faire via le terminal.

#### Exécution du fichier Python

L'exécution du fichier Python est facile ! Assurez-vous d'être dans le bon répertoire, et tout ce que vous avez à faire est d'entrer ce qui suit dans votre fenêtre de terminal :

```bash
python dog_breeds.py
```

#### Sortie

Après quelques minutes d'entraînement, votre dossier `images` et votre fichier `dog_breeds.py` seront accompagnés d'un SFrame, d'un dossier de modèle et d'un fichier **.mlmodel**, qui est votre modèle Core ML !

Vous serez également présenté avec une sortie dans votre fenêtre de terminal, qui ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/rMfcBjxekEbOIEOeFqhUdCOdGxwwVOZ1YSLk)
_**Figure 4 :** Sortie après l'exécution de Python_

Cela vous donne des informations sur l'entraînement et la précision de l'entraînement, le nombre d'images traitées et d'autres informations utiles, que vous pouvez utiliser pour analyser votre modèle sans même jamais l'utiliser.

### Conclusion

J'espère que vous avez apprécié la lecture de ce tutoriel autant que j'ai apprécié le faire ! Voici quelques étapes sur la suite. Si vous voulez apprendre à utiliser votre modèle Core ML dans une application iOS, consultez un autre de mes tutoriels :

[**Commencez avec la reconnaissance d'images dans Core ML**](https://code.tutsplus.com/tutorials/image-classification-through-machine-learning-using-coreml--cms-29819?_ga=2.101472841.993700883.1547096068-312075175.1521244044)  
[_Avec les avancées technologiques, nous en sommes au point où nos appareils peuvent utiliser leurs caméras intégrées pour identifier avec précision…_](https://code.tutsplus.com/tutorials/image-classification-through-machine-learning-using-coreml--cms-29819?_ga=2.101472841.993700883.1547096068-312075175.1521244044)  
[tutsplus.com](https://code.tutsplus.com/tutorials/image-classification-through-machine-learning-using-coreml--cms-29819?_ga=2.101472841.993700883.1547096068-312075175.1521244044)

Ce tutoriel vous montrera comment prendre votre modèle `dog_classifier.mlmodel` résultant et l'implémenter dans une application iOS réelle. Il vous apprendra également à analyser un flux vidéo en direct et à prendre des images individuelles pour la classification d'images.

Si vous avez des questions ou des commentaires concernant ce tutoriel, n'hésitez pas à les poser dans la section des commentaires ci-dessous ! Je suis toujours impatient d'entendre des retours, des questions ou comment vous avez utilisé vos connaissances de ce tutoriel.

### Il est facile de soutenir mon travail !

N'oubliez pas d'**appuyer sur ce bouton "clap"** autant de fois que vous le pouvez, de **partager ce tutoriel** sur les réseaux sociaux et de **me suivre sur Twitter**.

[**Vardhan Agrawal (@vhanagwal) | Twitter**](https://twitter.com/vhanagwal)  
[_Les derniers Tweets de Vardhan Agrawal (@vhanagwal). Développeur #ios complètement autodidacte, #formateur, et humain…_](https://twitter.com/vhanagwal)