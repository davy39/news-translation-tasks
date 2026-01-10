---
title: Apprendre TensorFlow, le modèle Word2Vec et l'algorithme TSNE en utilisant
  des groupes de rock
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-14T18:03:18.000Z'
originalURL: https://freecodecamp.org/news/learn-tensorflow-the-word2vec-model-and-the-tsne-algorithm-using-rock-bands-97c99b5dcb3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xlBuDrRto5N7_lVCtsoE7g.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Apprendre TensorFlow, le modèle Word2Vec et l'algorithme TSNE en utilisant
  des groupes de rock
seo_desc: 'By Patrick Ferris

  Learning the “TensorFlow way” to build a neural network can seem like a big hurdle
  to getting started with machine learning. In this tutorial, we’ll take it step by
  step and explain all of the critical components involved as we buil...'
---

Par Patrick Ferris

Apprendre la méthode "TensorFlow" pour construire un réseau de neurones peut sembler être un obstacle majeur pour commencer avec l'apprentissage automatique. Dans ce tutoriel, nous allons procéder étape par étape et expliquer tous les composants critiques impliqués tout en construisant un modèle Bands2Vec en utilisant les données de [Pitchfork](https://www.kaggle.com/nolanbconaway/pitchfork-data) provenantes de [Kaggle](https://www.kaggle.com/nolanbconaway/pitchfork-data).

Pour le code complet, consultez la page GitHub [page](https://github.com/patricoferris/machinelearning/blob/master/word2vec/Pitchfork.ipynb).

## Le modèle Word2Vec

Les réseaux de neurones consomment des nombres et produisent des nombres. Ils sont très bons pour cela. Mais donnez-leur du texte, et ils feront une crise et ne feront rien de remotivement intéressant.

Si le travail du réseau de neurones est de traiter les nombres et de produire une sortie significative, alors c'est à nous de nous assurer que ce que nous lui fournissons est également significatif. Cette quête d'une représentation significative de l'information a donné naissance au modèle Word2Vec.

Une approche pour travailler avec des mots est de former des [vecteurs encodés one-hot](https://en.wikipedia.org/wiki/One-hot). Créez une longue liste (le nombre de mots distincts dans notre vocabulaire) de zéros, et faites en sorte que chaque mot pointe vers un index unique de cette liste. Si nous voyons ce mot, faites en sorte que cet index dans la liste soit un nombre un.

Bien que cette approche fonctionne, elle nécessite beaucoup d'espace et est complètement dénuée de sens. 'Bon' et 'Excellent' sont aussi similaires que 'Canard' et 'Trou noir'. Si seulement il y avait un moyen de vectoriser les mots afin que nous préservions cette similarité contextuelle...

Heureusement, il existe un moyen !

En utilisant un réseau de neurones, nous pouvons produire des 'embeddings' de nos mots. Ce sont des vecteurs qui représentent chaque mot unique extrait des poids des connexions au sein de notre réseau.

Mais la question reste : comment nous assurer qu'ils sont significatifs ? La réponse : alimenter des paires de mots en tant que mot cible et mot de contexte. Faites cela suffisamment de fois, en ajoutant quelques mauvais exemples aussi, et le réseau de neurones commence à apprendre quels mots apparaissent ensemble et comment cela forme presque un graphe. Comme un réseau social de mots interconnectés par des contextes. 'Bon' va vers 'utile' qui va vers 'attentionné' et ainsi de suite. Notre tâche est d'alimenter ces données dans le réseau de neurones.

L'une des approches les plus courantes est le modèle [Skipgram](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf), générant ces paires cible-contexte basées sur le déplacement d'une fenêtre à travers un ensemble de données de texte. Mais que faire si nos données ne sont pas des phrases, mais que nous avons toujours une signification contextuelle ?

Dans ce tutoriel, nos mots sont des noms d'artistes et nos contextes sont des genres et des scores de critique moyens. Nous voulons que l'artiste A soit proche de l'artiste B s'ils partagent un genre et ont un score de critique moyen similaire. Alors commençons.

## Construction de notre ensemble de données

[Pitchfork](https://pitchfork.com/) est un magazine musical en ligne américain couvrant principalement le rock, l'indépendant et la nouvelle musique. Les données publiées sur Kaggle ont été extraites de leur site web et contiennent des informations comme des critiques, des genres et des dates liées à chaque artiste.

Créons une classe artiste et un dictionnaire pour stocker toutes les informations utiles que nous voulons.

Super ! Maintenant, nous voulons fabriquer nos paires cible-contexte basées sur le genre et le score de critique moyen. Pour cela, nous allons créer deux dictionnaires : un pour les différents genres uniques, et un pour les scores (discrétisés en entiers).

Nous allons ajouter tous nos artistes au genre correspondant et au score moyen dans ces dictionnaires pour les utiliser plus tard lors de la génération de paires d'artistes.

Une dernière étape avant de plonger dans le code TensorFlow : générer un lot ! Un lot est comme un échantillon de données que notre réseau de neurones utilisera pour chaque époque. Une époque est un passage à travers le réseau de neurones dans une phase d'entraînement. Nous voulons générer deux tableaux numpy. L'un contiendra le code suivant :

## TensorFlow

Il existe une myriade de tutoriels et de sources de connaissances sur TensorFlow. N'importe lequel de ces [excellents articles](https://medium.freecodecamp.org/search?q=tensorflow) vous aidera ainsi que la [documentation](https://www.tensorflow.org/tutorials/). Le code suivant est largement basé sur le tutoriel [word2vec](https://github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/examples/tutorials/word2vec/word2vec_basic.py) des gens de TensorFlow eux-mêmes. J'espère pouvoir démystifier certaines parties et les réduire à l'essentiel.

La première étape consiste à comprendre la représentation du 'graphe'. Cela est incroyablement utile pour les visualisations [TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard) et pour créer une image mentale des flux de données au sein du réseau de neurones.

Prenez le temps de lire le code et les commentaires ci-dessous. Avant de fournir des données à un réseau de neurones, nous devons initialiser toutes les parties que nous allons utiliser. Les placeholders sont les entrées prenant ce que nous donnons au 'feed_dict'. Les variables sont des parties mutables du graphe que nous allons éventuellement ajuster. La partie la plus importante de notre modèle est la fonction de perte. C'est le score de notre performance et la carte au trésor pour savoir comment nous pouvons nous améliorer.

L'estimation de contraste de bruit (NCE) est une fonction de perte. Habituellement, nous utiliserions l'entropie croisée et le softmax, mais dans le monde du traitement du langage naturel, toutes nos classes se résument à chaque mot unique.

Sur le plan computationnel, cela est mauvais. NCE change le cadre du problème des probabilités de classes à savoir si une paire cible-contexte est correcte (une classification binaire). Il prend une vraie paire puis échantillonne pour obtenir de mauvaises paires, la constante `num_sampled` contrôle cela. Notre réseau de neurones apprend à distinguer entre ces bonnes et mauvaises paires. Finalement, il apprend les contextes ! Vous pouvez lire plus sur NCE et comment il fonctionne [ici](https://www.tensorflow.org/api_docs/python/tf/nn/nce_loss).

## Exécuter le réseau de neurones

Maintenant que tout est bien configuré, nous devons simplement appuyer sur le gros bouton vert 'go' et tourner nos pouces pendant un moment.

### Visualisation utilisant TSNE

D'accord, nous n'avons pas tout à fait terminé. Nous avons maintenant des vecteurs riches en contexte et de 64 dimensions pour nos artistes, mais cela fait peut-être trop de dimensions pour vraiment visualiser leur utilité.

Heureusement pour nous, nous pouvons écraser cette information en deux dimensions tout en conservant autant de propriétés que les 64 dimensions avaient ! C'est l'embedding stochastique de voisins distribués en T, ou TSNE pour faire court. Cette [vidéo](https://www.youtube.com/watch?v=NEaUSP4YerM) fait un excellent travail d'explication de l'idée principale derrière TSNE, mais je vais essayer de donner un aperçu général.

TSNE est une approche de réduction de dimensionnalité qui conserve les similarités (comme la distance euclidienne) des dimensions supérieures. Pour ce faire, il construit d'abord une matrice de similarités point à point calculées en utilisant une distribution normale. Le centre de la distribution est le premier point, et la similarité du deuxième point est la valeur de la distribution à la distance entre les points éloignés du centre de la distribution.

Ensuite, nous projetons aléatoirement sur la dimension inférieure et faisons exactement le même processus en utilisant une distribution t. Maintenant, nous avons deux matrices de similarités point à point. L'algorithme déplace ensuite lentement les points dans la dimension inférieure pour essayer de les faire ressembler à la matrice de la dimension supérieure où les similarités étaient préservées. Et répéter. Heureusement, Sci-kit Learn a une fonction qui peut faire le travail de calcul pour nous.

## Les Résultats

![Image](https://cdn-media-1.freecodecamp.org/images/1*RIQ6oJsW_ZfH2pgpNDiTDA.png)
_Tous les artistes tracés en utilisant leur embedding de faible dimension_

L'aspect incroyable de ces embeddings est que, tout comme les vecteurs, ils supportent les opérations mathématiques. L'exemple classique étant : `King — Man + Woman = Queen`, ou du moins très proche de cela. Essayons un exemple.

Prenez les embeddings de faible dimension de Coil, un groupe avec les genres suivants, `['electronic', 'experimental', 'rock']`, et le score moyen `7.9`. Maintenant, soustrayez les embeddings de faible dimension de Elder Ones, un groupe avec les genres, `['electronic']`, et le score moyen `7.8`. Avec cette différence d'embedding, trouvez les groupes les plus proches et imprimez leurs noms et genres.

```
Artiste : black lips, Score Moyen : 7.48, Genres : ['rock', 'rock', 'rock', 'rock', 'rock']
```

```
Artiste : crookers, Score Moyen : 5.5, Genres : ['electronic']
```

```
Artiste : guided by voices, Score Moyen : 7.23043478261, Genres : ['rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock']
```

Cela a fonctionné ! Nous obtenons des groupes de rock et électronique avec des scores de critique vaguement similaires. Ci-dessous sont les trois cents premiers groupes tracés avec des étiquettes. J'espère que vous avez trouvé ce projet éducatif et inspirant. Allez de l'avant et construisez, explorez et jouez !

![Image](https://cdn-media-1.freecodecamp.org/images/1*grGZRnIl-nutaVEiwzvLDA.png)
_Trois cents artistes tracés et étiquetés_