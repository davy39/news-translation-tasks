---
title: Une plongée approfondie dans les plongements de mots pour l'analyse de sentiment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T14:27:33.000Z'
originalURL: https://freecodecamp.org/news/word-embeddings-for-sentiment-analysis
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/1_u9pwb9JShvDIU7j1G9iszQ.jpeg
tags:
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
- name: Python
  slug: python
- name: Sentiment analysis
  slug: sentiment-analysis
- name: text mining
  slug: text-mining
seo_title: Une plongée approfondie dans les plongements de mots pour l'analyse de
  sentiment
seo_desc: "By Bert Carremans\nWhen applying one-hot encoding to words, we end up with\
  \ sparse (containing many zeros) vectors of high dimensionality. On large data sets,\
  \ this could cause performance issues. \nAdditionally, one-hot encoding does not\
  \ take into accou..."
---

Par Bert Carremans

Lorsque nous appliquons le codage one-hot aux mots, nous obtenons des vecteurs clairsemés (contenant de nombreux zéros) de grande dimensionnalité. Sur de grands ensembles de données, cela pourrait causer des problèmes de performance. 

De plus, le codage one-hot ne tient pas compte de la sémantique des mots. Ainsi, des mots comme _avion_ et _aéronef_ sont considérés comme deux caractéristiques différentes alors que nous savons qu'ils ont un sens très similaire. Les plongements de mots abordent ces deux problèmes.

Les plongements de mots sont des vecteurs denses avec une dimensionnalité beaucoup plus faible. Deuxièmement, les relations sémantiques entre les mots sont reflétées dans la distance et la direction des vecteurs.

Nous travaillerons avec l'ensemble de données [TwitterAirlineSentiment sur Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment). Cet ensemble de données contient environ 15K tweets avec 3 classes possibles pour le sentiment (positif, négatif et neutre). Dans mon précédent article, nous avons essayé de [classifier les tweets](https://www.freecodecamp.org/news/sentiment-analysis-with-text-mining/) en tokenisant les mots et en appliquant deux classificateurs. Voyons si les plongements de mots peuvent surpasser cela.

Après avoir lu ce tutoriel, vous saurez comment calculer des plongements de mots spécifiques à une tâche avec la couche Embedding de **Keras**. Deuxièmement, nous examinerons si les plongements de mots formés sur un corpus plus large peuvent améliorer la précision de notre modèle.

La structure de ce tutoriel est la suivante :

* Intuition derrière les plongements de mots
* Configuration du projet
* Préparation des données
* Keras et sa couche Embedding
* Plongements de mots pré-entraînés — GloVe
* Entraînement des plongements de mots avec plus de dimensions

# Intuition derrière les plongements de mots

Avant de pouvoir utiliser des mots dans un classificateur, nous devons les convertir en nombres. Une façon de le faire est de simplement mapper les mots à des entiers. Une autre façon est de les encoder en one-hot. Chaque tweet pourrait alors être représenté comme un vecteur avec une dimension égale à (un ensemble limité de) les mots dans le corpus. Les mots apparaissant dans le tweet ont une valeur de 1 dans le vecteur. Toutes les autres valeurs du vecteur sont égales à zéro.

Les plongements de mots sont calculés différemment. Chaque mot est positionné dans un **_espace multi-dimensionnel_**. Le nombre de dimensions dans cet espace est choisi par le scientifique des données. Vous pouvez expérimenter avec différentes dimensions et voir ce qui donne le meilleur résultat.

Les **_valeurs du vecteur pour un mot représentent sa position_** dans cet espace de plongement. Les synonymes se trouvent proches les uns des autres tandis que les mots avec des significations opposées ont une grande distance entre eux. Vous pouvez également appliquer des opérations mathématiques sur les vecteurs qui devraient produire des résultats sémantiquement corrects. Un exemple typique est que la somme des plongements de mots de _roi_ et _femelle_ produit le plongement de mot de _reine_.

# Configuration du projet

Commençons par importer tous les packages pour ce projet.

```python
import pandas as pd
import numpy as np
import re
import collections
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from keras import models
from keras import layers
```

Nous définissons certains paramètres et chemins utilisés tout au long du projet. La plupart d'entre eux sont auto-explicatifs. Mais d'autres seront expliqués plus loin dans le code.

```python
NB_WORDS = 10000  # Paramètre indiquant le nombre de mots que nous mettrons dans le dictionnaire
VAL_SIZE = 1000  # Taille de l'ensemble de validation
NB_START_EPOCHS = 10  # Nombre d'époques avec lesquelles nous commençons généralement l'entraînement
BATCH_SIZE = 512  # Taille des lots utilisés dans la descente de gradient mini-batch
MAX_LEN = 24  # Nombre maximum de mots dans une séquence
GLOVE_DIM = 100  # Nombre de dimensions des plongements de mots GloVe
root = Path('../')
input_path = root / 'input/'
ouput_path = root / 'output/'
source_path = root / 'source/'
```

Tout au long de ce code, nous utiliserons également certaines fonctions auxiliaires pour la préparation des données, la modélisation et la visualisation. Ces définitions de fonctions ne sont pas montrées ici pour garder l'article de blog sans encombrement. Vous pouvez toujours vous référer au [notebook sur Github](https://github.com/bertcarremans/TwitterUSAirlineSentiment/blob/master/source/Using%20Word%20Embeddings%20for%20Sentiment%20Analysis.ipynb) pour voir le code.

# Préparation des données

## Lecture des données et nettoyage

Nous lisons le fichier CSV avec les tweets et appliquons un mélange aléatoire sur ses index. Après cela, nous supprimons les mots vides et les @ mentions. Un ensemble de test de 10% est séparé pour évaluer le modèle sur de nouvelles données.

```python
df = pd.read_csv(input_path / 'Tweets.csv')
df = df.reindex(np.random.permutation(df.index))
df = df[['text', 'airline_sentiment']]
df.text = df.text.apply(remove_stopwords).apply(remove_mentions)
X_train, X_test, y_train, y_test = train_test_split(df.text, df.airline_sentiment, test_size=0.1, random_state=37)
```

## Convertir les mots en entiers

Avec le **_Tokenizer_** de Keras, nous convertissons les tweets en séquences d'entiers. Nous limitons le nombre de mots aux **_NB_WORDS_** mots les plus fréquents. De plus, les tweets sont nettoyés avec certains filtres, mis en minuscules et divisés sur les espaces.

```python
tk = Tokenizer(num_words=NB_WORDS,
filters='!"#$%&()*+,-./:;<=>?@[\]^_`{"}~\t\n',lower=True, split=" ")
tk.fit_on_texts(X_train)
X_train_seq = tk.texts_to_sequences(X_train)
X_test_seq = tk.texts_to_sequences(X_test)
```

## Longueur égale des séquences

Chaque lot doit fournir des séquences de longueur égale. Nous y parvenons avec la méthode **_pad_sequences_**. En spécifiant **_maxlen_**, les séquences sont remplies de zéros ou tronquées.

```python
X_train_seq_trunc = pad_sequences(X_train_seq, maxlen=MAX_LEN)
X_test_seq_trunc = pad_sequences(X_test_seq, maxlen=MAX_LEN)
```

## Encodage de la variable cible

Les classes cibles sont des chaînes de caractères qui doivent être converties en vecteurs numériques. Cela est fait avec le **_LabelEncoder_** de Sklearn et la méthode **_to_categorical_** de Keras.

```python
le = LabelEncoder()
y_train_le = le.fit_transform(y_train)
y_test_le = le.transform(y_test)
y_train_oh = to_categorical(y_train_le)
y_test_oh = to_categorical(y_test_le)
```

## Séparation de l'ensemble de validation

À partir des données d'entraînement, nous séparons un ensemble de validation de 10% à utiliser pendant l'entraînement.

```python
X_train_emb, X_valid_emb, y_train_emb, y_valid_emb = train_test_split(X_train_seq_trunc, y_train_oh, test_size=0.1, random_state=37)
```

# Modélisation

## Keras et la couche Embedding

Keras fournit un moyen pratique de convertir chaque mot en un vecteur multi-dimensionnel. Cela peut être fait avec la couche **_Embedding_**. Elle calculera les plongements de mots (ou utilisera des plongements pré-entraînés) et recherchera chaque mot dans un dictionnaire pour trouver sa représentation vectorielle. Ici, nous entraînerons des plongements de mots avec 8 dimensions.

```python
emb_model = models.Sequential()
emb_model.add(layers.Embedding(NB_WORDS, 8, input_length=MAX_LEN))
emb_model.add(layers.Flatten())
emb_model.add(layers.Dense(3, activation='softmax'))
emb_history = deep_model(emb_model, X_train_emb, y_train_emb, X_valid_emb, y_valid_emb)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_-XjJ4DTQ5RQ8jZOF.png)

Nous avons une précision de validation d'environ 74%. Le nombre de mots dans les tweets est plutôt faible, donc ce résultat est assez bon. En comparant la perte d'entraînement et de validation, nous voyons que le modèle commence à **surapprendre** à partir de l'époque 6.

Dans un article précédent, j'ai discuté de la manière dont nous pouvons [éviter le surapprentissage](https://www.freecodecamp.org/news/handling-overfitting-in-deep-learning-models/). Vous pourriez vouloir lire cela si vous voulez approfondir ce sujet.

Lorsque nous entraînons le modèle sur toutes les données (y compris les données de validation, mais à l'exclusion des données de test) et fixons le nombre d'époques à 6, nous obtenons une précision de test de 78%. Ce résultat de test est correct, mais voyons si nous pouvons améliorer avec des plongements de mots pré-entraînés.

```python
emb_results = test_model(emb_model, X_train_seq_trunc, y_train_oh, X_test_seq_trunc, y_test_oh, 6)
print('/n')
print('Précision de test du modèle de plongements de mots : {0:.2f}%'.format(emb_results[1]*100))
```

## Plongements de mots pré-entraînés — GloVe

Parce que les données d'entraînement ne sont pas si grandes, le modèle pourrait ne pas être en mesure d'apprendre de bons plongements pour l'analyse de sentiment. Alternativement, nous pouvons charger des plongements de mots pré-entraînés construits sur des données d'entraînement beaucoup plus grandes.

La [base de données GloVe](https://nlp.stanford.edu/projects/glove/) contient plusieurs plongements de mots pré-entraînés, et plus spécifiquement des **_plongements entraînés sur des tweets_**. Cela pourrait donc être utile pour la tâche à accomplir.

Tout d'abord, nous mettons les plongements de mots dans un dictionnaire où les clés sont les mots et les valeurs sont les plongements de mots.

```python
glove_file = 'glove.twitter.27B.' + str(GLOVE_DIM) + 'd.txt'
emb_dict = {}
glove = open(input_path / glove_file)
for line in glove:
    values = line.split()
    word = values[0]
    vector = np.asarray(values[1:], dtype='float32')
    emb_dict[word] = vector
glove.close()
```

Avec les plongements GloVe chargés dans un dictionnaire, nous pouvons rechercher le plongement pour chaque mot dans le corpus des tweets de la compagnie aérienne. Ceux-ci seront stockés dans une matrice avec une forme de **_NB_WORDS_** et **_GLOVE_DIM_**. Si un mot n'est pas trouvé dans le dictionnaire GloVe, les valeurs de plongement de mot pour le mot sont nulles.

```python
emb_matrix = np.zeros((NB_WORDS, GLOVE_DIM))
for w, i in tk.word_index.items():
    if i < NB_WORDS:
        vect = emb_dict.get(w)
        if vect is not None:
        emb_matrix[i] = vect
    else:
        break
```

Ensuite, nous spécifions le modèle comme nous l'avons fait avec le modèle ci-dessus.

```python
glove_model = models.Sequential()
glove_model.add(layers.Embedding(NB_WORDS, GLOVE_DIM, input_length=MAX_LEN))
glove_model.add(layers.Flatten())
glove_model.add(layers.Dense(3, activation='softmax'))
```

Dans la couche Embedding (qui est la couche 0 ici), nous **_définissons les poids_** pour les mots à ceux trouvés dans les plongements de mots GloVe. En définissant **_trainable_** à False, nous nous assurons que les plongements de mots GloVe ne peuvent pas être modifiés. Après cela, nous exécutons le modèle.

```python
glove_model.layers[0].set_weights([emb_matrix])
glove_model.layers[0].trainable = False
glove_history = deep_model(glove_model, X_train_emb, y_train_emb, X_valid_emb, y_valid_emb)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_uhsGcl8UG_JYUycb.png)

Le modèle surapprend rapidement après 3 époques. De plus, la précision de validation est inférieure par rapport aux plongements entraînés sur les données d'entraînement.

```python
glove_results = test_model(glove_model, X_train_seq_trunc, y_train_oh, X_test_seq_trunc, y_test_oh, 3)
print('/n')
print('Précision de test du modèle glove : {0:.2f}%'.format(glove_results[1]*100))
```

En tant qu'exercice final, voyons quels résultats nous obtenons lorsque nous entraînons les plongements avec le même nombre de dimensions que les données GloVe.

## Entraînement des plongements de mots avec plus de dimensions

Nous entraînerons les plongements de mots avec le même nombre de dimensions que les plongements GloVe (c'est-à-dire GLOVE_DIM).

```python
emb_model2 = models.Sequential()
emb_model2.add(layers.Embedding(NB_WORDS, GLOVE_DIM, input_length=MAX_LEN))
emb_model2.add(layers.Flatten())
emb_model2.add(layers.Dense(3, activation='softmax'))
emb_history2 = deep_model(emb_model2, X_train_emb, y_train_emb, X_valid_emb, y_valid_emb)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_boJxTu7msbxWzexm.png)

```python
emb_results2 = test_model(emb_model2, X_train_seq_trunc, y_train_oh, X_test_seq_trunc, y_test_oh, 3)
print('/n')
print('Précision de test du modèle de plongement de mots 2 : {0:.2f}%'.format(emb_results2[1]*100))
```

Sur les données de test, nous obtenons de bons résultats, mais nous ne surpassons pas la régression logistique avec le CountVectorizer. Il y a donc encore place à l'amélioration.

# Conclusion

Le meilleur résultat est obtenu avec des plongements de mots de 100 dimensions qui sont entraînés sur les données disponibles. Cela surpasse même l'utilisation de plongements de mots qui ont été entraînés sur un corpus Twitter beaucoup plus grand.

Jusqu'à présent, nous avons simplement mis une couche Dense sur les plongements aplatis. En faisant cela, **_nous ne tenons pas compte des relations entre les mots_** dans le tweet. Cela peut être réalisé avec un réseau de neurones récurrent ou un réseau de convolution 1D. Mais c'est quelque chose pour un futur article 😊