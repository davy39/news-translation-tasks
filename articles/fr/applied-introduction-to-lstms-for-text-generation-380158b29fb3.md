---
title: Une introduction appliquée aux LSTM pour la génération de texte — utilisant
  Keras et les noyaux Kaggle avec GPU
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T01:25:03.000Z'
originalURL: https://freecodecamp.org/news/applied-introduction-to-lstms-for-text-generation-380158b29fb3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JxNsHuuN9ESnlzDntuBqBQ.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: Une introduction appliquée aux LSTM pour la génération de texte — utilisant
  Keras et les noyaux Kaggle avec GPU
seo_desc: 'By Megan Risdal

  Kaggle recently gave data scientists the ability to add a GPU to Kernels (Kaggle’s
  cloud-based hosted notebook platform). I knew this would be the perfect opportunity
  for me to learn how to build and train more computationally intensi...'
---

Par Megan Risdal

[Kaggle](https://www.kaggle.com/) a récemment donné aux scientifiques des données la possibilité d'ajouter un GPU aux [Noyaux](https://www.kaggle.com/kernels) (la plateforme de notebooks hébergée dans le cloud de Kaggle). Je savais que ce serait l'occasion parfaite pour moi d'apprendre à construire et à entraîner des modèles plus intensifs en calcul.

Avec [Kaggle Learn](https://www.kaggle.com/learn/deep-learning), la [documentation Keras](https://keras.io/), et des données de langage naturel intéressantes de [freeCodeCamp](https://www.freecodecamp.org/), j'avais tout ce dont j'avais besoin pour passer des [forêts aléatoires](https://www.kaggle.com/mrisdal/exploring-survival-on-the-titanic) aux réseaux de neurones récurrents.

![Image](https://cdn-media-1.freecodecamp.org/images/Fr8gPPB9gylc-IX97WKJdBm1d8we94yx152e)
_Jeu de données de freeCodeCamp sur Kaggle Datasets._

Dans cet article de blog, je vais vous montrer comment j'ai utilisé le texte des [journaux de chat Gitter de freeCodeCamp](https://www.kaggle.com/freecodecamp/all-posts-public-main-chatroom) publiés sur Kaggle Datasets pour entraîner un réseau LSTM qui génère de nouvelles sorties textuelles.

Vous pouvez trouver tout mon code reproductible dans ce [notebook Python](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation/notebook).

Maintenant que vous pouvez utiliser des **GPU** dans les noyaux — la plateforme de notebooks hébergée dans le cloud de Kaggle — avec **6 heures de temps d'exécution**, vous pouvez entraîner des modèles beaucoup plus intensifs en calcul que jamais auparavant sur Kaggle.

J'utiliserai un GPU pour entraîner le modèle dans ce notebook. (Vous pouvez demander un GPU pour votre session en cliquant sur l'onglet "Paramètres" depuis l'éditeur de noyau.)

```
import tensorflow as tfprint(tf.test.gpu_device_name())# Voir https://www.tensorflow.org/tutorials/using_gpu#allowing_gpu_memory_growthconfig = tf.ConfigProto()config.gpu_options.allow_growth = True
```

![Image](https://cdn-media-1.freecodecamp.org/images/PxD98069C0tEmNjWCZeqi2R8X2PJKAT8l4RW)

J'utiliserai le texte de l'un des utilisateurs les plus prolifiques du canal comme données d'entraînement. Ce notebook se compose de deux parties :

1. Lecture, exploration et préparation des données
2. Entraînement du LSTM sur les journaux de chat d'un seul identifiant utilisateur et génération de nouveau texte comme sortie

[Vous pouvez suivre en lisant simplement le notebook ou vous pouvez le fork](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation) (cliquez sur "Fork notebook") et exécuter les cellules vous-même pour apprendre ce que fait chaque partie de manière interactive. À la fin, vous apprendrez **comment formater les données textuelles en entrée d'un modèle LSTM au niveau des caractères implémenté dans Keras** et à votre tour, utiliser les prédictions au niveau des caractères du modèle pour **générer de nouvelles séquences de texte**.

Avant de plonger dans le code, qu'est-ce qu'un réseau LSTM ("Long Short-Term Memory") ?

Dans ce tutoriel, nous adopterons une approche pratique pour implémenter cette variante de réseau de neurones récurrents, spécialement équipée pour gérer les dépendances à longue distance (y compris celles que l'on obtient avec le langage) dans Keras, un framework de deep learning.

Si vous souhaitez revoir davantage les fondements théoriques, je vous recommande de consulter cet excellent article de blog, [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

### Partie une : Préparation des données

Dans la partie une, je vais d'abord lire les données et essayer de les explorer suffisamment pour vous donner une idée de ce avec quoi nous travaillons. L'une de mes frustrations en suivant des tutoriels non interactifs (comme du code statique partagé sur GitHub) est qu'il est souvent difficile de savoir comment les données que vous souhaitez utiliser diffèrent de l'exemple de code. Vous devez les télécharger et les comparer localement, ce qui est fastidieux.

Les deux avantages de suivre ce tutoriel en utilisant les noyaux sont que a) je vais essayer de vous donner des aperçus des données à chaque étape significative ; et 2) vous pouvez toujours [fork ce notebook](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation) et ?boom? vous avez une copie de mon environnement, des données, de l'image Docker, et tout cela sans téléchargement ni installation nécessaire. Surtout si vous avez de l'expérience avec l'installation de CUDA pour utiliser les GPU pour le deep learning, vous apprécierez à quel point il est merveilleux d'avoir un environnement déjà configuré pour vous.

#### Lire les données

```
import pandas as pdimport numpy as np# Lire uniquement les deux colonnes dont nous avons besoin chat = pd.read_csv('../input/freecodecamp_casual_chatroom.csv', usecols = ['fromUser.id', 'text'])
```

```
# Supprimer l'identifiant utilisateur pour CamperBotchat = chat[chat['fromUser.id'] != '55b977f00fc9f982beab7883'] chat.head()
```

![Image](https://cdn-media-1.freecodecamp.org/images/JdWmZVD9DDxPuIZ8YrbIzCWjGzMBM7FvNLTZ)

Cela a l'air bien !

#### Explorer les données

Dans mon graphique ci-dessous, vous pouvez voir le nombre de messages des dix participants les plus actifs du chat par leur identifiant utilisateur dans le Gitter de freeCodeCamp :

```
import matplotlib.pyplot as pltplt.style.use('fivethirtyeight')f, g = plt.subplots(figsize=(12, 9))chat['fromUser.id'].value_counts().head(10).plot.bar(color="green")g.set_xticklabels(g.get_xticklabels(), rotation=25)plt.title("Utilisateurs les plus actifs dans le canal Gitter de freeCodeCamp")plt.show(g)
```

![Image](https://cdn-media-1.freecodecamp.org/images/T-vw8lpBrUrSMircm9JvOvhtIF2yV9IPVFYh)

Ainsi, l'identifiant utilisateur `55a7c9e08a7b72f55c3f991e` est l'utilisateur le plus actif du canal avec plus de 140 000 messages. Nous utiliserons ses messages pour entraîner le LSTM à générer de nouvelles phrases similaires à celles de `55a7c9e08a7b72f55c3f991e`. Mais d'abord, jetons un coup d'œil aux premiers messages de `55a7c9e08a7b72f55c3f991e` pour avoir une idée de ce dont ils parlent :

```
chat[chat['fromUser.id'] == "55a7c9e08a7b72f55c3f991e"].text.head(20)
```

![Image](https://cdn-media-1.freecodecamp.org/images/q1Eul6QWB93FqoxHrsZettuYle2z6vZQ21a6)

Je vois des mots et des phrases comme "documentation", "pair coding", "BASH", "Bootstrap", "CSS", etc. Et je peux seulement supposer que la phrase commençant par "With all of the various frameworks…" fait référence à JavaScript. Oui, cela semble être sur le sujet en ce qui concerne freeCodeCamp. Ainsi, nous nous attendons à ce que nos nouvelles phrases ressemblent à peu près à cela si nous réussissons.

#### Préparer les données de séquence pour l'entrée dans le LSTM

Actuellement, nous avons un dataframe avec des colonnes correspondant aux identifiants utilisateur et au texte des messages, où chaque ligne correspond à un seul message envoyé. Cela est assez éloigné de la forme 3D requise par la couche d'entrée de notre réseau LSTM : `model.add(LSTM(batch_size, input_shape=(time_steps, features)))` où `batch_size` est le nombre de séquences dans chaque échantillon (peut être un ou plusieurs), `time_steps` est la taille des observations dans chaque échantillon, et `features` est le nombre de caractéristiques observables possibles (c'est-à-dire, les caractères dans notre cas).

Alors, comment passer d'un dataframe à des données de séquence dans la bonne forme ? Je vais le diviser en trois étapes :

1. Sous-ensemble des données pour former un corpus
2. Formater le corpus de #1 en tableaux de séquences semi-superposées de longueur uniforme et de caractères suivants
3. Représenter les données de séquence de #2 sous forme de tenseurs booléens clairsemés

#### Sous-ensemble des données pour former un corpus

Dans les deux cellules suivantes, nous allons récupérer uniquement les messages de `55a7c9e08a7b72f55c3f991e` (`'fromUser.id' == '55a7c9e08a7b72f55c3f991e'`) pour sous-ensembler les données et réduire le vecteur de chaînes en une seule chaîne. Puisque nous ne nous soucions pas de savoir si notre modèle génère du texte avec une capitalisation correcte, nous utilisons `tolower()`. Cela donne au modèle une dimension de moins à apprendre.

Je vais également utiliser uniquement les 20 % premiers des données comme échantillon, car nous n'avons pas besoin de plus pour générer un texte à peu près décent. Vous pouvez essayer de fork ce noyau et expérimenter avec plus (ou moins) de données si vous le souhaitez.

```
user = chat[chat['fromUser.id'] == '55a7c9e08a7b72f55c3f991e'].textn_messages = len(user)n_chars = len(' '.join(map(str, user)))print("55a7c9e08a7b72f55c3f991e représente %d messages" % n_messages)print("Leurs messages totalisent %d caractères" % n_chars)
```

![Image](https://cdn-media-1.freecodecamp.org/images/JkGCjTyc6B2LeUxyAZhboKGyO6Ru7v9UHVe4)

```
sample_size = int(len(user) * 0.2)user = user[:sample_size]user = ' '.join(map(str, user)).lower()user[:100] # Afficher les 100 premiers caractères
```

![Image](https://cdn-media-1.freecodecamp.org/images/PZb-K0vqqMNwYkucZlLRGp32crjFnS664ksC)

#### Formater le corpus en tableaux de séquences semi-superposées de longueur uniforme et de caractères suivants

Le reste du code utilisé ici est adapté de [ce script d'exemple](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py), initialement écrit par François Chollet (auteur de Keras et Kaggler), pour préparer les données dans le format correct pour l'entraînement d'un LSTM. Puisque nous entraînons un modèle au niveau des caractères, nous relions les caractères uniques (comme "a", "b", "c", ...) à des indices numériques dans la cellule ci-dessous. Si vous réexécutez ce code vous-même en cliquant sur ["Fork Notebook"](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation/), vous pouvez imprimer tous les caractères utilisés.

```
chars = sorted(list(set(user)))print('Nombre de caractères uniques (c'est-à-dire, caractéristiques) :', len(chars))
```

```
char_indices = dict((c, i) for i, c in enumerate(chars))indices_char = dict((i, c) for i, c in enumerate(chars))
```

![Image](https://cdn-media-1.freecodecamp.org/images/J-Dyhx6j1PSRK3zsijxFrF8Atvvzgy5F41En)

Cette prochaine étape de cellule nous donne un tableau, `sentences`, composé de séquences de `maxlen` (40) caractères découpées en étapes de 3 caractères à partir de notre corpus `user`, et `next_chars`, un tableau de caractères uniques de `user` à `i + maxlen` pour chaque `i`. J'ai imprimé les 10 premières chaînes du tableau afin que vous puissiez voir que nous découpons le corpus en "phrases" partiellement superposées et de longueur égale.

```
maxlen = 40step = 3sentences = []next_chars = []for i in range(0, len(user) - maxlen, step):    sentences.append(user[i: i + maxlen])    next_chars.append(user[i + maxlen])print('Nombre de séquences :', len(sentences), "\n")print(sentences[:10], "\n")print(next_chars[:10])
```

![Image](https://cdn-media-1.freecodecamp.org/images/GOwu0LKKiu9bwftZwaTNu0FapNo6BKbpS182)

Vous pouvez voir comment le caractère suivant la première séquence `'hi folks. just doing the new signee stuf'` est le caractère `f` pour terminer le mot "stuff". Et le caractère suivant la séquence `'folks. just doing the new signee stuff. '` est le caractère `h` pour commencer le mot "hello". De cette manière, il devrait être clair maintenant comment `next_chars` est les "étiquettes de données" ou la vérité de terrain pour nos séquences dans `sentences` et notre modèle entraîné sur ces données étiquetées sera capable de générer de _nouveaux caractères suivants_ comme prédictions étant donné une entrée de séquence.

#### Représenter les données de séquence sous forme de tenseurs booléens clairsemés

La cellule suivante prendra quelques secondes à s'exécuter si vous [suivez de manière interactive dans le noyau](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation/). Nous créons des tenseurs booléens clairsemés `x` et `y` encodant des caractéristiques au niveau des caractères à partir de `sentences` et `next_chars` pour les utiliser comme entrées du modèle que nous entraînons. La forme que nous obtenons sera : `input_shape=(maxlen, len(chars))` où `maxlen` est 40 et `len(chars)` est le nombre de caractéristiques (c'est-à-dire, le nombre unique de caractères de notre corpus).

```
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)y = np.zeros((len(sentences), len(chars)), dtype=np.bool)for i, sentence in enumerate(sentences):    for t, char in enumerate(sentence):        x[i, t, char_indices[char]] = 1    y[i, char_indices[next_chars[i]]] = 1
```

### Partie deux : Modélisation

Dans la partie deux, nous effectuons l'entraînement réel du modèle et la génération de texte. Nous avons exploré les données et les avons remodelées correctement afin de pouvoir les utiliser comme entrée de notre modèle LSTM. Cette partie se compose de deux sections :

1. Définition d'un modèle de réseau LSTM
2. Entraînement du modèle et génération de prédictions

#### Définition d'un modèle de réseau LSTM

Commençons par lire nos bibliothèques. J'utilise Keras, qui est une interface populaire et facile à utiliser pour un backend TensorFlow. Lisez plus sur [pourquoi utiliser Keras comme framework de deep learning ici](https://keras.io/why-use-keras/). Ci-dessous, vous pouvez voir les modèles, couches, optimiseurs et callbacks que nous allons utiliser.

```
from keras.models import Sequentialfrom keras.layers import Dense, Activationfrom keras.layers import LSTMfrom keras.optimizers import RMSpropfrom keras.callbacks import LambdaCallback, ModelCheckpointimport randomimport sysimport io
```

![Image](https://cdn-media-1.freecodecamp.org/images/oh7JrJZ0CoIJR1YWCTL-045pe0jRxVzhcovb)

Dans la cellule ci-dessous, nous définissons le modèle. Nous commençons par un modèle séquentiel et ajoutons un LSTM comme couche d'entrée. La forme que nous définissons pour notre entrée est identique à nos données à ce stade, ce qui est exactement ce dont nous avons besoin. J'ai sélectionné une `batch_size` de 128, qui est le nombre d'échantillons, ou séquences, que notre modèle examine pendant l'entraînement avant de se mettre à jour. Vous pouvez expérimenter avec différents nombres ici si vous le souhaitez. J'ajoute également une couche de sortie dense. Enfin, nous utiliserons une couche d'activation avec `softmax` comme fonction d'activation, car nous faisons essentiellement une classification multiclasse pour prédire le caractère suivant dans une séquence.

```
model = Sequential()model.add(LSTM(128, input_shape=(maxlen, len(chars))))model.add(Dense(len(chars)))model.add(Activation('softmax'))
```

Maintenant, nous pouvons compiler notre modèle. Nous utiliserons `RMSprop` avec un taux d'apprentissage de `0.1` pour optimiser les poids dans notre modèle (vous pouvez expérimenter avec différents taux d'apprentissage ici) et `categorical_crossentropy` comme notre fonction de perte. L'entropie croisée est la même que la perte logarithmique couramment utilisée comme métrique d'évaluation dans les compétitions de classification binaire sur Kaggle (sauf que dans notre cas, il y a plus de deux résultats possibles).

```
optimizer = RMSprop(lr=0.01)model.compile(loss='categorical_crossentropy', optimizer=optimizer)
```

Notre modèle est maintenant prêt. Avant de lui fournir des données, la cellule ci-dessous définit quelques fonctions auxiliaires [avec du code modifié à partir de ce script](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py). La première, `sample()`, échantillonne un index à partir d'un tableau de probabilités avec une certaine `temperature`. Petite pause pour demander, qu'est-ce que la température exactement ?

> **_Température_** _est un facteur d'échelle appliqué aux sorties de notre couche dense avant d'appliquer la fonction d'activation `softmax`. En résumé, elle définit à quel point les suppositions du modèle pour le caractère suivant dans une séquence sont conservatrices ou "créatives". Des valeurs plus faibles de `temperature` (par exemple, `0,2`) généreront des suppositions "sûres", tandis que des valeurs de `temperature` supérieures à `1,0` commenceront à générer des suppositions "plus risquées". Pensez-y comme à la quantité de surprise que vous auriez en voyant un mot anglais commencer par "st" par rapport à "sg". Lorsque la température est basse, nous pouvons obtenir beaucoup de "the" et "and" ; lorsque la température est élevée, les choses deviennent plus imprévisibles._

En tout cas, la seconde consiste à définir une fonction de rappel pour imprimer le texte prédit généré par notre LSTM entraîné à la première époque, puis à chaque cinquième époque suivante avec cinq paramètres différents de `temperature` à chaque fois (voir la ligne `for diversity in [0.2, 0.5, 1.0, 1.2]:` pour les valeurs de `temperature` ; n'hésitez pas à les ajuster également !). De cette façon, nous pouvons ajuster le bouton `temperature` pour voir ce qui nous donne le meilleur texte généré, allant de conservateur à créatif. Notez que nous utilisons notre modèle pour prédire en fonction d'une séquence aléatoire, ou "graine", à partir de nos données sous-ensemblistes originales, `user` : `start_index = random.randint(0, len(user) - maxlen - 1)`.

Enfin, nous nommons notre fonction de rappel `generate_text`, que nous ajouterons à la liste des rappels lorsque nous ajusterons notre modèle dans la cellule suivante.

```
def sample(preds, temperature=1.0):    # fonction auxiliaire pour échantillonner un index à partir d'un tableau de probabilités    preds = np.asarray(preds).astype('float64')    preds = np.log(preds) / temperature    exp_preds = np.exp(preds)    preds = exp_preds / np.sum(exp_preds)    probas = np.random.multinomial(1, preds, 1)    return np.argmax(probas)def on_epoch_end(epoch, logs):    # Fonction invoquée pour les époques spécifiées. Imprime le texte généré.    # Utilisation de epoch+1 pour être cohérent avec les époques d'entraînement imprimées par Keras    if epoch+1 == 1 or epoch+1 == 15:        print()        print('----- Génération de texte après l\'époque : %d' % epoch)        start_index = random.randint(0, len(user) - maxlen - 1)        for diversity in [0.2, 0.5, 1.0, 1.2]:            print('----- diversité :', diversity)            generated = ''            sentence = user[start_index: start_index + maxlen]            generated += sentence            print('----- Génération avec la graine : "' + sentence + '"')            sys.stdout.write(generated)            for i in range(400):                x_pred = np.zeros((1, maxlen, len(chars)))                for t, char in enumerate(sentence):                    x_pred[0, t, char_indices[char]] = 1.                preds = model.predict(x_pred, verbose=0)[0]                next_index = sample(preds, diversity)                next_char = indices_char[next_index]                generated += next_char                sentence = sentence[1:] + next_char                sys.stdout.write(next_char)                sys.stdout.flush()            print()    else:        print()        print('----- Pas de génération de texte après l\'époque : %d' % epoch)generate_text = LambdaCallback(on_epoch_end=on_epoch_end)
```

#### Entraînement du modèle et génération de prédictions

Enfin, nous y sommes arrivés ! Nos données sont prêtes (`x` pour les séquences, `y` pour les caractères suivants), nous avons choisi une `batch_size` de `128`, et nous avons défini une fonction de rappel qui imprimera le texte généré en utilisant `model.predict()` à la fin de la première époque, suivie de chaque cinquième époque avec cinq paramètres différents de `temperature` à chaque fois. Nous avons un autre rappel, `ModelCheckpoint`, qui sauvegardera le meilleur modèle à chaque époque s'il s'est amélioré en fonction de notre valeur de perte (trouvez le fichier de poids sauvegardé `weights.hdf5` dans l'onglet "Output" du noyau).

Ajustons notre modèle avec ces spécifications et `epochs = 15` pour le nombre d'époques à entraîner. Et bien sûr, n'oublions pas d'utiliser notre GPU ! Cela rendra l'entraînement/la prédiction beaucoup plus rapide que si nous utilisions un CPU. Dans tous les cas, vous voudrez toujours prendre un déjeuner ou aller vous promener en attendant que le modèle s'entraîne et génère des prédictions si vous exécutez ce code de manière interactive.

P.S. Si vous exécutez cela de manière interactive dans votre propre notebook sur Kaggle, vous pouvez cliquer sur le bouton bleu "Stop" à côté de la console en bas de votre écran pour interrompre l'entraînement du modèle.

```
# définir le point de contrôlefilepath = "weights.hdf5"checkpoint = ModelCheckpoint(filepath,                              monitor='loss',                              verbose=1,                              save_best_only=True,                              mode='min')# ajuster le modèle en utilisant notre gpuwith tf.device('/gpu:0'):    model.fit(x, y,              batch_size=128,              epochs=15,              verbose=2,              callbacks=[generate_text, checkpoint])
```

![Image](https://cdn-media-1.freecodecamp.org/images/qbPSuBNNnf0SNAxvcj6UoQT7ieWC3zeqMNIx)
_Exemple de sortie après la première époque._

### Conclusion

Et voilà ! Si vous avez exécuté ce notebook dans [Kaggle Kernels](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation/), vous avez probablement vu le modèle imprimer le texte généré caractère par caractère avec un effet dramatique.

J'espère que vous avez apprécié apprendre comment passer d'un dataframe contenant des lignes de texte à l'utilisation d'un modèle LSTM implémenté avec Keras dans les noyaux pour générer de nouvelles phrases grâce à la puissance des GPU. Vous pouvez voir comment notre modèle s'est amélioré de la première époque à la dernière. Le texte généré par les prédictions du modèle lors de la première époque ne ressemblait pas vraiment à de l'anglais. Et globalement, des niveaux de diversité plus faibles génèrent du texte avec beaucoup de répétitions, tandis que des niveaux de diversité plus élevés correspondent à plus de charabia.

Pouvez-vous ajuster le modèle ou ses hyperparamètres pour générer un texte encore meilleur ? Essayez-le vous-même en [forkant ce notebook](https://www.kaggle.com/mrisdal/intro-to-lstms-w-keras-gpu-for-text-generation/) (cliquez sur "Fork Notebook" en haut).

#### Inspiration pour les prochaines étapes

Voici quelques idées pour prendre ce que vous avez appris ici et l'étendre :

1. Expérimentez avec différents (hyper)-paramètres comme la quantité de données d'entraînement, le nombre d'époques ou de tailles de lots, `temperature`, etc.
2. Essayez le même code avec différentes données ; fork ce notebook, allez dans l'onglet "Data" et supprimez la source de données freeCodeCamp, puis ajoutez un autre jeu de données ([bons exemples ici](https://www.kaggle.com/datasets?sortBy=hottest&group=public&page=1&pageSize=20&size=all&filetype=all&license=all&tagids=11208)).
3. Essayez des architectures de réseau plus compliquées comme l'ajout de couches de dropout.
4. Apprenez-en plus sur le deep learning sur [Kaggle Learn](https://www.kaggle.com/learn/deep-learning), une série de vidéos et de tutoriels pratiques dans les noyaux.
5. Utilisez `weights.hdf5` dans l'onglet "Output" pour prédire en fonction de différentes données dans un nouveau noyau ce que ce serait si l'utilisateur de ce tutoriel complétait les phrases de quelqu'un d'autre.
6. Comparez l'effet d'accélération de l'utilisation d'un CPU par rapport à un GPU sur un exemple minimal.