---
title: Comment utiliser Fast.ai – Une passerelle conviviale pour le Deep Learning
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-02-02T00:10:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-fast-ai-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Untitled-design.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
seo_title: Comment utiliser Fast.ai – Une passerelle conviviale pour le Deep Learning
seo_desc: 'Fast.ai is a user-friendly library that brings the power of deep learning
  to your fingertips, regardless of your skill level. Let’s learn how it works.

  Have you ever felt curious about deep learning but found the technical complexity
  overwhelming? Fa...'
---

Fast.ai est une bibliothèque conviviale qui met la puissance du deep learning à votre portée, quel que soit votre niveau de compétence. Apprenons comment elle fonctionne.

Avez-vous déjà été curieux à propos du deep learning mais trouvé la complexité technique écrasante ? [Fast.ai](https://fast.ai/) est votre réponse.

Fast.ai simplifie le voyage dans le deep learning. Il rend le deep learning accessible même si vous n'êtes pas un data scientist expérimenté.

Dans cet article, nous explorerons ce qu'est Fast.ai, pourquoi il se distingue, et comment vous pouvez commencer avec quelques exemples de code de base.

## Qu'est-ce que Fast.ai ?

Fast.ai est une bibliothèque construite sur PyTorch, l'un des principaux frameworks de deep learning.

Elle est conçue pour rendre le deep learning plus accessible. La bibliothèque fournit des composants de haut niveau qui facilitent la construction et l'entraînement de réseaux de neurones.

Ce qui distingue Fast.ai, c'est son accent sur la praticité et sa capacité à être utilisé par des personnes ayant différents niveaux d'expérience en codage.

## Pourquoi choisir Fast.ai ?

### Convivial

La bibliothèque Fast.ai simplifie le processus de deep learning et abstrait de nombreux détails complexes, rendant plus facile pour les utilisateurs de créer des modèles puissants.

La bibliothèque **f**[**astai**](https://docs.fast.ai/) repose sur des frameworks de deep learning populaires comme PyTorch. Elle fournit une API de haut niveau pour construire et entraîner des réseaux de neurones.

Vous pouvez également intégrer d'autres modèles puissants comme les [transformers Hugging Face](https://www.freecodecamp.org/news/hugging-face-transformer-library-overview/) en utilisant Fast.ai.

### Approche pratique

Fast.ai met l'accent sur une approche pratique et concrète du deep learning.

La bibliothèque Fast.ai se concentre sur l'utilisation pratique et les applications réelles, vous aidant à apprendre en faisant.

Leurs cours et ressources sont conçus pour aider les étudiants à se lancer rapidement avec des modèles de machine learning. Ceux-ci incluent la construction et l'entraînement de réseaux de neurones pour la reconnaissance d'images, le traitement du langage naturel, et bien d'autres.

### Cours gratuits

Fast.ai propose [des cours en ligne gratuits](https://course.fast.ai/) qui couvrent une large gamme de sujets sur le deep learning. Les cours Fast.ai sont parmi les meilleurs sur le marché et leurs étudiants sont devenus des chercheurs populaires en machine learning.

Ces cours sont connus pour leur praticité, leurs explications claires et l'utilisation de jeux de données réels. Ces cours sont conçus pour être accessibles aux individus ayant différents niveaux de connaissances préalables en IA.

Fast.ai intègre également les derniers développements dans ses cours et ressources, garantissant que les étudiants aient accès à des techniques de pointe.

## Comment commencer avec Fast.ai

Maintenant que vous comprenez ce qu'est Fast.ai, écrivons un peu de code. Vous pouvez consulter [le notebook google colab](https://colab.research.google.com/) si vous voulez essayer rapidement cet exemple.

**Note :** Il est recommandé d'exécuter ce code sur votre système car l'exécuter dans colab prendra beaucoup de temps (environ 30 minutes).

Avant d'utiliser la bibliothèque, vous devez configurer votre environnement. Fast.ai fonctionne sur Python et nécessite PyTorch.

Vous pouvez installer Fast.ai en utilisant la commande pip (supprimez le **`!`** si vous l'installez sur votre terminal, car le **`!`** est uniquement pour les notebooks colab. Les notebooks traitent le code suivant **`!`** comme des scripts shell).

```
!pip install fastai
```

Nous allons passer par un exemple simple d'analyse de sentiments dans cet article, démontrant comment vous pouvez implémenter des modèles NLP en utilisant la bibliothèque fast.ai.

Commençons par importer la bibliothèque :

```
from fastai.text.all import *
```

Cette ligne de code importe des fonctionnalités spécifiques de la bibliothèque Fast.ai pour le traitement du langage naturel (NLP), en particulier l'analyse de texte.

Permettez-moi de vous le décomposer :

`from fastai.text.all` spécifie que vous souhaitez importer tous les composants du module `fastai.text` qui contient des outils et des fonctions pour travailler avec des données textuelles.

En incluant cette ligne au début de votre code, vous rendez toutes les fonctionnalités liées au texte de la bibliothèque Fastai disponibles pour votre utilisation, facilitant ainsi des tâches comme l'analyse de sentiments, la classification de texte, et autres.

Ensuite, nous utiliserons le jeu de données IMDB, également disponible dans Fast.ai.

```
path = untar_data(URLs.IMDB)
```

Cette ligne de code télécharge et extrait le jeu de données IMDB, le rendant prêt pour un traitement et une analyse ultérieurs.

La variable `path` contiendra le chemin de fichier local vers le jeu de données, vous permettant d'accéder et de travailler avec les données dans votre code.

Ensuite, nous devons charger les données. Les [chargeurs de données](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) sont utilisés pour charger et traiter efficacement les données pendant l'entraînement d'un modèle de machine learning.

`TextDataLoaders` est une classe fournie par la bibliothèque Fast.ai qui vous permet de créer des chargeurs de données spécialement conçus pour les données textuelles.

```
dls = TextDataLoaders.from_folder(path, valid='test')
```

`from_folder(path, valid='test')` est un appel de fonction sur la classe `TextDataLoaders`. Il est utilisé pour créer les chargeurs de données.

Voici ce que signifie chaque argument :

* `path` : Il s'agit du chemin du répertoire où vos données textuelles sont stockées. Dans ce cas, il s'agit de la variable `path` que vous avez précédemment définie, qui contient le chemin local vers le jeu de données IMDB.
* `valid='test'` : Cet argument spécifie quel dossier ou sous-ensemble de vos données doit être utilisé pour la validation. Dans le jeu de données IMDB, il y a généralement deux sous-ensembles principaux : `train` pour les données d'entraînement et `test` pour les données de test ou de validation. En définissant `valid` sur `test`, vous indiquez que le dossier 'test' dans le répertoire `path` doit être utilisé pour la validation. Il s'agit d'une pratique courante en machine learning d'avoir un ensemble de validation séparé pour évaluer les performances du modèle pendant l'entraînement.
* La variable résultante `dls` contiendra les chargeurs de données textuelles, qui incluent à la fois les divisions de données d'entraînement et de validation. Ces chargeurs de données peuvent être utilisés pour charger et prétraiter des lots de données textuelles pendant l'entraînement de votre modèle d'analyse de sentiments ou de tout autre modèle basé sur du texte.

Maintenant que nous avons les données pour l'entraînement, entraîons le modèle.

Nous allons créer un modèle de classification de texte en utilisant la bibliothèque Fast.ai, l'affiner sur les données textuelles fournies, et l'entraîner pour un nombre spécifié d'époques (répétitions).

```
learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)
```

Décomposons chaque ligne :

* `text_classifier_learner` — Le classificateur de texte learner est utilisé pour créer un objet learner pour l'entraînement et le travail avec des modèles de classification de texte. Examinons les arguments.
* `dls` — Il s'agit de l'objet chargeur de données que vous avez précédemment créé en utilisant `TextDataLoaders.from_folder()`. Il contient les données d'entraînement et de validation pour votre tâche de classification de texte.
* `AWD_LSTM` — Il s'agit d'une architecture prédéfinie pour le réseau de neurones utilisé dans les tâches de classification de texte. AWD_LSTM signifie [ASGD Weight-Dropped LSTM](https://arxiv.org/pdf/1708.02182v1.pdf). Il s'agit d'un type d'architecture de [réseau de neurones récurrents](https://aws.amazon.com/what-is/recurrent-neural-network/) (RNN) qui est efficace pour les données séquentielles comme le texte.
* `drop_mult=0.5` — Cet argument contrôle la quantité de régularisation par abandon appliquée au réseau de neurones. L'abandon est une technique de régularisation utilisée pour prévenir le surapprentissage (entraîner le modèle trop). `drop_mult=0.5` signifie que l'abandon sera appliqué à un taux modéré.
* `metrics=accuracy` — Cela spécifie que la métrique de précision doit être utilisée pour évaluer les performances du modèle pendant l'entraînement. La précision est une métrique courante pour les tâches de classification, mesurant le pourcentage d'exemples correctement classés.

Maintenant, affinons le modèle en utilisant les données chargées.

```
learn.fine_tune(1)
```

* `learn.fine_tune(1)` — Cette ligne de code affine le modèle de classification de texte.
* `1` — Le paramètre `1` est le nombre d'époques pour lesquelles le modèle sera entraîné. Une époque est un passage à travers l'ensemble du jeu de données d'entraînement. L'entraînement sur plusieurs époques permet au modèle d'apprendre des données plusieurs fois, ici pour simplifier, nous utilisons 1.

En résumé, ces lignes de code créent un modèle de classification de texte, chargent vos données textuelles, affinent le modèle sur les données pendant une époque en utilisant un taux d'apprentissage spécifié, et utilisent la précision comme métrique pour évaluer les performances du modèle.

L'objet `learn` résultant représente votre modèle de classification de texte entraîné, qui peut être utilisé pour faire des prédictions sur de nouvelles données textuelles.

Nous avons terminé. Maintenant, notre modèle est prêt à commencer à prédire les sentiments du texte.

Testons le modèle avec une critique de film.

```
learn.predict("I really loved that movie, it was awesome!")
```

Et voici le résultat.

```
('pos', tensor(1), tensor([0.4885, 0.5115]))
```

Le `pos` indique que la phrase donnée est une phrase positive. Le tableau suivant indique à quel point le modèle est confiant dans la prédiction de savoir si la phrase donnée est positive ou négative. Ce score de confiance peut être amélioré en augmentant le nombre d'époques (ce qui prendra beaucoup de temps à entraîner, sauf si vous avez un ordinateur puissant).

J'espère que cela vous aide à comprendre comment travailler avec la bibliothèque Fast.ai. Je préfère personnellement utiliser [Huggingface](https://huggingface.co/) pour la plupart des cas d'utilisation, mais si je dois entraîner des modèles à partir de zéro, Fast.ai serait mon premier choix.

## Conclusion

Fast.ai offre un excellent point de départ pour toute personne intéressée par le deep learning. Sa simplicité et sa praticité en font un outil précieux pour les débutants et les praticiens expérimentés.

En utilisant Fast.ai, vous découvrirez que le deep learning n'est pas aussi intimidant qu'il n'y paraît. Que vous soyez un étudiant, un développeur ou un apprenant curieux, Fast.ai peut être votre passerelle vers le monde fascinant de l'intelligence artificielle. Alors, commencez, expérimentez et profitez du voyage dans le deep learning avec Fast.ai.

Si vous êtes un étudiant en IA, abonnez-vous à **[turingtalks.ai](https://www.turingtalks.ai/)** pour apprendre des concepts pratiques sur le machine learning général et le NLP. Vous pouvez également [**visiter mon site web**](https://manishmshiva.com/) pour entrer en contact avec moi.