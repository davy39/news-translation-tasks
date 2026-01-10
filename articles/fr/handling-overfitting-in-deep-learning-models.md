---
title: Comment gérer le surapprentissage dans les modèles de deep learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T22:36:48.000Z'
originalURL: https://freecodecamp.org/news/handling-overfitting-in-deep-learning-models
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/1_XXtWMdH-YVL8z1VtnfG_iw.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: keras
  slug: keras
- name: Overfitting
  slug: overfitting
- name: Python
  slug: python
- name: regularization
  slug: regularization
seo_title: Comment gérer le surapprentissage dans les modèles de deep learning
seo_desc: 'By Bert Carremans

  Overfitting occurs when you achieve a good fit of your model on the training data,
  but it does not generalize well on new, unseen data. In other words, the model learned
  patterns specific to the training data, which are irrelevant i...'
---

Par Bert Carremans

Le surapprentissage (overfitting) se produit lorsque votre modèle s'ajuste bien aux données d'entraînement, mais ne généralise pas bien sur de nouvelles données invisibles. En d'autres termes, le modèle a appris des motifs spécifiques aux données d'entraînement, qui sont irrelevants dans d'autres données.

Nous pouvons identifier le surapprentissage en regardant les métriques de validation comme la perte (loss) ou la précision (accuracy). Habituellement, la métrique de validation cesse de s'améliorer après un certain nombre d'époques et commence à diminuer par la suite. La métrique d'entraînement continue de s'améliorer car le modèle cherche à trouver le meilleur ajustement pour les données d'entraînement.

Il existe plusieurs manières de réduire le surapprentissage dans les modèles de deep learning. La meilleure option est d'**obtenir plus de données d'entraînement**. Malheureusement, dans des situations réelles, vous n'avez souvent pas cette possibilité en raison du temps, du budget ou des contraintes techniques.

Une autre façon de réduire le surapprentissage est de **diminuer la capacité du modèle à mémoriser les données d'entraînement**. Ainsi, le modèle devra se concentrer sur les motifs pertinents dans les données d'entraînement, ce qui entraîne une meilleure généralisation. Dans cet article, nous discuterons de trois options pour y parvenir.

# Installation du projet

Nous commençons par importer les packages nécessaires et configurer certains paramètres. Nous utiliserons [Keras](https://keras.io/) pour ajuster les modèles de deep learning. Les données d'entraînement sont le [jeu de données Twitter US Airline Sentiment de Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment).

```python
# Packages de base
import pandas as pd 
import numpy as np
import re
import collections
import matplotlib.pyplot as plt
from pathlib import Path
# Packages pour la préparation des données
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.utils.np_utils import to_categorical
from sklearn.preprocessing import LabelEncoder
# Packages pour la modélisation
from keras import models
from keras import layers
from keras import regularizers
NB_WORDS = 10000  # Paramètre indiquant le nombre de mots que nous mettrons dans le dictionnaire
NB_START_EPOCHS = 20  # Nombre d'époques avec lesquelles nous commençons habituellement l'entraînement
BATCH_SIZE = 512  # Taille des lots utilisés dans la descente de gradient mini-batch
MAX_LEN = 20  # Nombre maximum de mots dans une séquence
root = Path('../')
input_path = root / 'input/' 
ouput_path = root / 'output/'
source_path = root / 'source/'
```

# Quelques fonctions auxiliaires

Nous utiliserons quelques fonctions auxiliaires tout au long de cet article.

```python
def deep_model(model, X_train, y_train, X_valid, y_valid):
    '''
    Fonction pour entraîner un modèle multi-classes. Le nombre d'époques et 
    batch_size sont définis par les constantes en haut du
    notebook. 
    
    Paramètres:
        model : modèle avec l'architecture choisie
        X_train : caractéristiques d'entraînement
        y_train : cible d'entraînement
        X_valid : caractéristiques de validation
        Y_valid : cible de validation
    Sortie:
        historique d'entraînement du modèle
    '''
    model.compile(optimizer='rmsprop'
                  , loss='categorical_crossentropy'
                  , metrics=['accuracy'])
    
    history = model.fit(X_train
                       , y_train
                       , epochs=NB_START_EPOCHS
                       , batch_size=BATCH_SIZE
                       , validation_data=(X_valid, y_valid)
                       , verbose=0)
    return history
def eval_metric(model, history, metric_name):
    '''
    Fonction pour évaluer un modèle entraîné sur une métrique choisie. 
    La métrique d'entraînement et de validation est tracée dans un
    graphique en ligne pour chaque époque.
    
    Paramètres:
        history : historique d'entraînement du modèle
        metric_name : perte ou précision
    Sortie:
        graphique en ligne avec les époques en axe x et la métrique en
        axe y
    '''
    metric = history.history[metric_name]
    val_metric = history.history['val_' + metric_name]
    e = range(1, NB_START_EPOCHS + 1)
    plt.plot(e, metric, 'bo', label='Train ' + metric_name)
    plt.plot(e, val_metric, 'b', label='Validation ' + metric_name)
    plt.xlabel('Numéro d\'époque')
    plt.ylabel(metric_name)
    plt.title('Comparaison de l\'entraînement et de la validation ' + metric_name + ' pour ' + model.name)
    plt.legend()
    plt.show()
def test_model(model, X_train, y_train, X_test, y_test, epoch_stop):
    '''
    Fonction pour tester le modèle sur de nouvelles données après l'avoir
    entraîné sur l'ensemble complet des données d'entraînement avec le nombre optimal d'époques.
    
    Paramètres:
        model : modèle entraîné
        X_train : caractéristiques d'entraînement
        y_train : cible d'entraînement
        X_test : caractéristiques de test
        y_test : cible de test
        epochs : nombre optimal d'époques
    Sortie:
        précision de test et perte de test
    '''
    model.fit(X_train
              , y_train
              , epochs=epoch_stop
              , batch_size=BATCH_SIZE
              , verbose=0)
    results = model.evaluate(X_test, y_test)
    print()
    print('Précision de test: {0:.2f}%'.format(results[1]*100))
    return results
    
def remove_stopwords(input_text):
    '''
    Fonction pour supprimer les stopwords anglais d'une série Pandas.
    
    Paramètres:
        input_text : texte à nettoyer
    Sortie:
        série Pandas nettoyée 
    '''
    stopwords_list = stopwords.words('english')
    # Certains mots qui peuvent indiquer un certain sentiment sont conservés via une liste blanche
    whitelist = ["n't", "not", "no"]
    words = input_text.split() 
    clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
    return " ".join(clean_words) 
    
def remove_mentions(input_text):
    '''
    Fonction pour supprimer les mentions, précédées par @, dans une série Pandas
    
    Paramètres:
        input_text : texte à nettoyer
    Sortie:
        série Pandas nettoyée 
    '''
    return re.sub(r'@\w+', '', input_text)
def compare_models_by_metric(model_1, model_2, model_hist_1, model_hist_2, metric):
    '''
    Fonction pour comparer une métrique entre deux modèles 
    
    Paramètres:
        model_hist_1 : historique d'entraînement du modèle 1
        model_hist_2 : historique d'entraînement du modèle 2
        metrix : métrique à comparer, perte, acc, val_loss ou val_acc
        
    Sortie:
        tracé des métriques des deux modèles
    '''
    metric_model_1 = model_hist_1.history[metric]
    metric_model_2 = model_hist_2.history[metric]
    e = range(1, NB_START_EPOCHS + 1)
    
    metrics_dict = {
        'acc' : 'Précision d\'entraînement',
        'loss' : 'Perte d\'entraînement',
        'val_acc' : 'Précision de validation',
        'val_loss' : 'Perte de validation'
    }
    
    metric_label = metrics_dict[metric]
    plt.plot(e, metric_model_1, 'bo', label=model_1.name)
    plt.plot(e, metric_model_2, 'b', label=model_2.name)
    plt.xlabel('Numéro d\'époque')
    plt.ylabel(metric_label)
    plt.title('Comparaison ' + metric_label + ' entre les modèles')
    plt.legend()
    plt.show()
    
def optimal_epoch(model_hist):
    '''
    Fonction pour retourner le numéro d'époque où la perte de validation est
    à son minimum
    
    Paramètres:
        model_hist : historique d'entraînement du modèle
    Sortie:
        numéro d'époque avec perte de validation minimale
    '''
    min_epoch = np.argmin(model_hist.history['val_loss']) + 1
    print("Perte de validation minimale atteinte à l'époque {}".format(min_epoch))
    return min_epoch
```

# Préparation des données

## Nettoyage des données

Nous chargeons le CSV avec les tweets et effectuons un mélange aléatoire. C'est une bonne pratique de mélanger les données avant de les diviser entre un ensemble d'entraînement et de test. Ainsi, les classes de sentiment sont également distribuées sur les ensembles d'entraînement et de test. Nous ne conserverons que la colonne **text** comme entrée et la colonne **airline_sentiment** comme cible.

La prochaine chose que nous ferons est de **supprimer les stopwords**. Les stopwords n'ont aucune valeur pour prédire le sentiment. De plus, comme nous voulons construire un modèle qui peut être utilisé pour d'autres compagnies aériennes également, nous **supprimons les mentions**.

```python
df = pd.read_csv(input_path / 'Tweets.csv')
df = df.reindex(np.random.permutation(df.index))  
df = df[['text', 'airline_sentiment']]
df.text = df.text.apply(remove_stopwords).apply(remove_mentions)
```

## Division Train-Test

L'évaluation des performances du modèle doit être effectuée sur un ensemble de test séparé. Ainsi, nous pouvons estimer à quel point le modèle généralise bien. Cela est fait avec la méthode **train_test_split** de scikit-learn.

```
X_train, X_test, y_train, y_test = train_test_split(df.text, df.airline_sentiment, test_size=0.1, random_state=37)
```

## Conversion des mots en nombres

Pour utiliser le texte comme entrée pour un modèle, nous devons d'abord convertir les mots en tokens, ce qui signifie simplement convertir les mots en entiers qui font référence à un index dans un dictionnaire. Ici, nous ne conserverons que les mots les plus fréquents dans l'ensemble d'entraînement.

Nous nettoyons le texte en appliquant des **filtres** et en mettant les mots en **minuscules**. Les mots sont séparés par des espaces.

```python
tk = Tokenizer(num_words=NB_WORDS,
               filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{"}~\t\n',
               lower=True,
               char_level=False,
               split=' ')
tk.fit_on_texts(X_train)
```

Après avoir créé le dictionnaire, nous pouvons convertir le texte d'un tweet en un vecteur avec des valeurs NB_WORDS. Avec **mode=binary**, il contient un indicateur si le mot est apparu dans le tweet ou non. Cela est fait avec la méthode **texts_to_matrix** du Tokenizer.

```python
X_train_oh = tk.texts_to_matrix(X_train, mode='binary')
X_test_oh = tk.texts_to_matrix(X_test, mode='binary')
```

## Conversion des classes cibles en nombres

Nous devons également convertir les classes cibles en nombres, qui à leur tour sont encodés en one-hot avec la méthode **to_categorical** dans Keras.

```python
le = LabelEncoder()
y_train_le = le.fit_transform(y_train)
y_test_le = le.transform(y_test)
y_train_oh = to_categorical(y_train_le)
y_test_oh = to_categorical(y_test_le)
```

## Séparation d'un ensemble de validation

Maintenant que nos données sont prêtes, nous séparons un ensemble de validation. Cet ensemble de validation sera utilisé pour évaluer les performances du modèle lorsque nous ajustons les paramètres du modèle.

```python
X_train_rest, X_valid, y_train_rest, y_valid = train_test_split(X_train_oh, y_train_oh, test_size=0.1, random_state=37)
```

# Deep learning

## Création d'un modèle qui surapprend

Nous commençons par un modèle qui surapprend. Il a 2 couches densément connectées de 64 éléments. La **input_shape** pour la première couche est égale au nombre de mots que nous avons conservés dans le dictionnaire et pour lesquels nous avons créé des caractéristiques one-hot-encoded.

Comme nous devons prédire 3 classes de sentiment différentes, la dernière couche a 3 éléments. La fonction d'activation **softmax** assure que les trois probabilités s'additionnent à 1.

Le nombre de paramètres à entraîner est calculé comme **(nb inputs x nb éléments dans la couche cachée) + nb termes de biais**. Le nombre d'entrées pour la première couche est égal au nombre de mots dans notre corpus. Les couches suivantes ont le nombre de sorties de la couche précédente comme entrées. Ainsi, le nombre de paramètres par couche est :

* Première couche : (10000 x 64) + 64 = 640064
* Deuxième couche : (64 x 64) + 64 = 4160
* Dernière couche : (64 x 3) + 3 = 195

```python
base_model = models.Sequential()
base_model.add(layers.Dense(64, activation='relu', input_shape=(NB_WORDS,)))
base_model.add(layers.Dense(64, activation='relu'))
base_model.add(layers.Dense(3, activation='softmax'))
base_model.name = 'Modèle de base'
```

Parce que ce projet est une prédiction multi-classes à étiquette unique, nous utilisons **categorical_crossentropy** comme fonction de perte et **softmax** comme fonction d'activation finale. Nous ajustons le modèle sur les données d'entraînement et validons sur l'ensemble de validation. Nous exécutons pour un nombre prédéterminé d'époques et verrons quand le modèle commence à surapprendre.

```python
base_history = deep_model(base_model, X_train_rest, y_train_rest, X_valid, y_valid)
base_min = optimal_epoch(base_history)
eval_metric(base_model, base_history, 'loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_ZwKhGQkYF3FqQlhe.png)

Au début, la **perte de validation** diminue. Mais à l'époque 3, cela s'arrête et la perte de validation commence à augmenter rapidement. C'est à ce moment que les modèles commencent à surapprendre.

La **perte d'entraînement** continue de diminuer et atteint presque zéro à l'époque 20. Cela est normal car le modèle est entraîné pour s'ajuster aux données d'entraînement aussi bien que possible.

# Gestion du surapprentissage

Maintenant, nous pouvons essayer de faire quelque chose contre le surapprentissage. Il existe différentes options pour cela.

* **Réduire la capacité du réseau** en supprimant des couches ou en réduisant le nombre d'éléments dans les couches cachées
* Appliquer une **régularisation**, qui revient à ajouter un coût à la fonction de perte pour les grands poids
* Utiliser des **couches de dropout**, qui supprimeront aléatoirement certaines caractéristiques en les mettant à zéro

## Réduction de la capacité du réseau

Notre premier modèle a un grand nombre de paramètres entraînables. Plus ce nombre est élevé, plus il est facile pour le modèle de mémoriser la classe cible pour chaque échantillon d'entraînement. Évidemment, ce n'est pas idéal pour généraliser sur de nouvelles données.

En réduisant la capacité du réseau, vous le forcez à apprendre les motifs qui comptent ou qui minimisent la perte. D'autre part, réduire trop la capacité du réseau conduira à un **sous-apprentissage**. Le modèle ne pourra pas apprendre les motifs pertinents dans les données d'entraînement.

Nous réduisons la capacité du réseau en supprimant une couche cachée et en réduisant le nombre d'éléments dans la couche restante à 16.

```python
reduced_model = models.Sequential()
reduced_model.add(layers.Dense(16, activation='relu', input_shape=(NB_WORDS,)))
reduced_model.add(layers.Dense(3, activation='softmax'))
reduced_model.name = 'Modèle réduit'
reduced_history = deep_model(reduced_model, X_train_rest, y_train_rest, X_valid, y_valid)
reduced_min = optimal_epoch(reduced_history)
eval_metric(reduced_model, reduced_history, 'loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_ZDi9EJn6dORo4LCY.png)

Nous pouvons voir qu'il faut plus d'époques avant que le modèle réduit ne commence à surapprendre. La perte de validation augmente également plus lentement que notre premier modèle.

```python
compare_models_by_metric(base_model, reduced_model, base_history, reduced_history, 'val_loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_W8RSZtaBR-SDIGn5.png)

Lorsque nous comparons la perte de validation du modèle de base, il est clair que le modèle réduit commence à surapprendre à une époque ultérieure. La perte de validation reste plus basse beaucoup plus longtemps que le modèle de base.

## Application de la régularisation

Pour traiter le surapprentissage, nous pouvons appliquer une régularisation des poids au modèle. Cela ajoutera un coût à la fonction de perte du réseau pour les grands poids (ou valeurs de paramètres). En conséquence, vous obtenez un modèle plus simple qui sera forcé d'apprendre uniquement les motifs pertinents dans les données d'entraînement.

Il existe une **régularisation L1 et une régularisation L2**.

* La régularisation L1 ajoutera un coût par rapport à la **valeur absolue des paramètres**. Elle entraînera certains des poids à être égaux à zéro.
* La régularisation L2 ajoutera un coût par rapport à la **valeur au carré des paramètres**. Cela entraîne des poids plus petits.

Essayons avec la régularisation L2.

```python
reg_model = models.Sequential()
reg_model.add(layers.Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='relu', input_shape=(NB_WORDS,)))
reg_model.add(layers.Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='relu'))
reg_model.add(layers.Dense(3, activation='softmax'))
reg_model.name = 'Modèle de régularisation L2'
reg_history = deep_model(reg_model, X_train_rest, y_train_rest, X_valid, y_valid)
reg_min = optimal_epoch(reg_history)
```

Pour le modèle régularisé, nous remarquons qu'il commence à surapprendre à la même époque que le modèle de base. Cependant, la perte augmente beaucoup plus lentement par la suite.

```python
eval_metric(reg_model, reg_history, 'loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_4UV4tgegrn6UOdRX.png)

```python
compare_models_by_metric(base_model, reg_model, base_history, reg_history, 'val_loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_5ybMcTqkOXyC7xc4.png)

## Ajout de couches de dropout

La dernière option que nous essayerons est d'ajouter des couches de dropout. Une couche de dropout mettra aléatoirement à zéro les caractéristiques de sortie d'une couche.

```python
drop_model = models.Sequential()
drop_model.add(layers.Dense(64, activation='relu', input_shape=(NB_WORDS,)))
drop_model.add(layers.Dropout(0.5))
drop_model.add(layers.Dense(64, activation='relu'))
drop_model.add(layers.Dropout(0.5))
drop_model.add(layers.Dense(3, activation='softmax'))
drop_model.name = 'Modèle avec couches de dropout'
drop_history = deep_model(drop_model, X_train_rest, y_train_rest, X_valid, y_valid)
drop_min = optimal_epoch(drop_history)
eval_metric(drop_model, drop_history, 'loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_B0SuqLpCTYGP4Bwz.png)

Le modèle avec des couches de dropout commence à surapprendre plus tard que le modèle de base. La perte augmente également plus lentement que le modèle de base.

```python
compare_models_by_metric(base_model, drop_model, base_history, drop_history, 'val_loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_ykk8IT9v3wgsq1Wf.png)

Le modèle avec les couches de dropout commence à surapprendre plus tard. Comparé au modèle de base, la perte reste également beaucoup plus basse.

# Entraînement sur l'ensemble complet des données d'entraînement et évaluation sur les données de test

À première vue, le modèle réduit semble être le meilleur modèle pour la généralisation. Mais vérifions cela sur l'ensemble de test.

```python
base_results = test_model(base_model, X_train_oh, y_train_oh, X_test_oh, y_test_oh, base_min)
reduced_results = test_model(reduced_model, X_train_oh, y_train_oh, X_test_oh, y_test_oh, reduced_min)
reg_results = test_model(reg_model, X_train_oh, y_train_oh, X_test_oh, y_test_oh, reg_min)
drop_results = test_model(drop_model, X_train_oh, y_train_oh, X_test_oh, y_test_oh, drop_min)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_faz4dZBCsh3yB6tAZzSXkg.png)

# Conclusion

Comme montré ci-dessus, les trois options aident à réduire le surapprentissage. Nous parvenons à augmenter considérablement la précision sur les données de test. Parmi ces trois options, le modèle avec les couches de dropout performe le mieux sur les données de test.

Vous pouvez trouver le notebook sur [GitHub](https://github.com/bertcarremans/TwitterUSAirlineSentiment/blob/master/source/Handling%20overfitting%20in%20deep%20learning%20models.ipynb). Amusez-vous bien avec !