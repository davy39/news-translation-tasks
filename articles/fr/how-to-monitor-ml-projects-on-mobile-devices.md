---
title: Comment surveiller les projets de Machine Learning sur votre appareil mobile📱
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-24T19:20:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-ml-projects-on-mobile-devices
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Frame-4-1.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: mobile
  slug: mobile
seo_title: Comment surveiller les projets de Machine Learning sur votre appareil mobile📱
seo_desc: "By Rishit Dagli\nWhat if you could monitor your Colab, Kaggle, or AzureML\
  \ Machine Learning projects on your mobile phone? You'd be able to check in on your\
  \ models on the fly – even while taking a walk\U0001F6B6. \nIf you are an ML developer,\
  \ you know how train..."
---

Par Rishit Dagli

Et si vous pouviez surveiller vos projets Colab, Kaggle ou AzureML de Machine Learning sur votre téléphone mobile ? Vous pourriez vérifier vos modèles en déplacement – même en vous promenant🚶. 

Si vous êtes un développeur en ML, vous savez combien l'entraînement des modèles peut prendre du temps. Ne serait-ce pas génial de pouvoir surveiller cela depuis votre téléphone mobile ?

Eh bien, vous pouvez le faire – et en moins de 5 lignes de code.

## Pourquoi la surveillance à distance de vos modèles est utile

Avant de passer au tutoriel et de vous montrer comment cela fonctionne, laissez-moi brièvement décrire ce que vous pouvez faire avec [TF Watcher](https://github.com/Rishit-dagli/TF-Watcher), un projet open-source que nous utiliserons pour surveiller nos travaux de ML :

* S'intègre parfaitement à votre flux de travail ML, vous n'avez donc pas besoin de changer autre chose dans votre code pour le faire fonctionner
* Toutes vos visualisations et tableaux de bord sont en temps réel
* Vous souhaitez probablement partager votre tableau de bord en direct ou un tableau de bord précédemment exécuté avec vos collègues, et cela vous permet également de créer des liens partageables
* C'est une PWA qui vous permet de surveiller vos modèles hors ligne dans une capacité limitée
* Vous obtenez également un contrôle précis sur le moment où vous souhaitez enregistrer les métriques

## Comment surveiller vos projets ML sur votre téléphone

Passons maintenant au tutoriel sur la façon de surveiller vos modèles sur un appareil mobile avec Google Colab. Je vais vous montrer comment utiliser cet outil dans Google Colab, afin que chacun puisse l'essayer, mais vous pouvez pratiquement reproduire cela n'importe où (même sur votre machine locale).

N'hésitez pas à suivre avec [ce notebook colab](https://colab.research.google.com/github/Rishit-dagli/TF-Watcher/blob/main/docs/source/TF-Watcher-Quickstart.ipynb).

### **Installer le package Python tf-watcher**

Pour surveiller vos travaux de Machine Learning sur des appareils mobiles, vous devez installer le package Python `tf-watcher`. Il s'agit d'un package Python open-source que j'ai développé, et vous pouvez trouver le code source dans [ce dépôt GitHub](https://github.com/Rishit-dagli/TF-Watcher). 

Pour installer le package Python depuis PyPI, exécutez la commande suivante dans votre cellule de notebook :

```
 !pip install tf-watcher
```

### Comment créer un modèle simple

Pour les besoins de cet exemple, nous verrons comment vous pouvez surveiller un travail d'entraînement – mais vous pouvez utiliser ce package pour surveiller vos travaux d'évaluation ou de prédiction également. Vous verrez bientôt comment vous pouvez facilement spécifier les métriques que vous souhaitez surveiller.

Dans cet exemple, nous utiliserons [Fashion MNIST](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist), un ensemble de données simple de 60 000 images en niveaux de gris de 10 catégories de mode. Nous commençons par charger l'ensemble de données, puis nous effectuerons un simple prétraitement pour accélérer davantage notre exemple.

Cependant, vous pouvez utiliser tout ce dont nous parlons dans cet article dans vos expériences plus complexes.

Récupérons l'ensemble de données :

```python
import tensorflow as tf

# Charger les données MNIST d'exemple et les prétraiter
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

# Limiter les données à 1000 échantillons pour accélérer
x_train = x_train[:1000]
y_train = y_train[:1000]
x_test = x_test[:1000]
y_test = y_test[:1000]
```

Maintenant, nous allons créer un simple réseau de neurones qui n'a qu'une seule couche `Dense`. Je vais vous montrer comment utiliser cela avec l'API Sequential de TensorFlow, mais cela fonctionne de la même manière avec l'API Functionnelle ou les modèles sous-classés.

```python
# Définir le modèle Keras
def get_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(1, input_dim=784))
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=0.1),
        loss="mean_squared_error",
        metrics=["accuracy"],
    )
    return model
```

Vous avez peut-être remarqué qu'en compilant notre modèle, nous avons également spécifié `metrics` qui nous permet de préciser quelles métriques nous devons surveiller. 

Ici, je mentionne "accuracy" donc je devrais pouvoir surveiller la précision sur mon appareil mobile. Par défaut, nous avons enregistré "loss" donc dans ce cas, nous surveillerions 2 métriques : loss et accuracy.

Vous pouvez ajouter autant de métriques que vous le souhaitez. Vous pouvez également utiliser les [métriques intégrées](https://www.tensorflow.org/api_docs/python/tf/keras/metrics) de TensorFlow ou ajouter votre propre métrique personnalisée.

### Comment créer une instance d'une classe de rappel

Vous allez maintenant importer TF Watcher et créer une instance de l'une de ses classes :

```python
import tfwatcher

MonitorCallback = tfwatcher.callbacks.EpochEnd(schedule = 1)
```

Dans cet exemple :

* Nous utilisons la classe `EpochEnd` de TF Watcher pour spécifier que nous sommes intéressés par l'opération au niveau de l'époque. Il existe plusieurs de ces classes que vous pouvez utiliser pour vos propres besoins – découvrez toutes les autres classes dans [la documentation](https://rishit-dagli.github.io/TF-Watcher/). 
* Nous passons `schedule` à 1 pour surveiller après chaque époque. Vous pourriez passer 3 à la place (pour surveiller après chaque 3 époques) ou vous pourriez également passer une liste des numéros d'époque spécifiques que vous souhaitez surveiller.

Lorsque vous exécutez ce morceau de code, vous devriez voir quelque chose comme ceci imprimé :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-76.png)
_ID unique pour votre session_

Cela inclut un ID unique de 7 caractères pour votre session. Assurez-vous de noter cet ID car vous l'utiliserez pour surveiller votre modèle.

## Comment commencer à surveiller votre modèle 🚀

Maintenant, nous allons entraîner le modèle que nous avons construit et surveiller les métriques en temps réel pour l'entraînement sur un appareil mobile.

```python
model = get_model()

history = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=100,
    validation_split=0.5,
    callbacks = [MonitorCallback]
)
```

Dans ce morceau de code, nous commençons à entraîner notre modèle pour 100 époques (ce devrait être assez rapide dans ce cas). Nous ajoutons également l'objet que nous avons créé dans l'étape précédente en tant que `callback`. 

Si dans votre cas vous surveillez la prédiction au lieu de l'entraînement, vous ajouteriez `callbacks = [MonitorCallback]` dans la méthode predict.

Une fois que vous avez exécuté le morceau de code ci-dessus, vous pouvez commencer à le surveiller depuis l'application web sur votre appareil mobile. 

Allez sur [https://www.tfwatcher.tech/](https://www.tfwatcher.tech/) et entrez l'ID unique que vous avez créé ci-dessus. Il s'agit d'une PWA, ce qui signifie que vous pouvez également l'installer sur vos appareils mobiles et l'utiliser comme une application native Android.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-80.png)
_Installer l'application web_

Une fois que vous avez ajouté votre ID de session, vous devriez pouvoir voir vos logs progresser en temps réel à travers les graphiques. En plus des métriques, vous devriez également pouvoir voir le temps qu'il a fallu pour chaque époque. Dans d'autres cas, cela pourrait être le temps pris pour un lot.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/TF-Watcher--MLH-Recording.png)
_Le tableau de bord de surveillance_

### Comment partager les tableaux de bord

Puisque le ML est très collaboratif, vous pourriez vouloir partager vos tableaux de bord en direct avec des collègues. Pour ce faire, cliquez simplement sur le bouton de partage de lien et l'application crée un lien partageable pour que quiconque puisse voir votre progression en direct ou les tableaux de bord stockés.

[Voici le lien partageable](https://www.tfwatcher.tech/logs/ybhzyxK) pour le tableau de bord que j'ai créé dans ce tutoriel.

## Que pouvez-vous faire d'autre avec TF Watcher ?

Bien que l'exemple que je viens de montrer semblait assez cool, il y a beaucoup plus que nous pouvons faire avec cet outil. Je vais maintenant brièvement parler de deux de ces scénarios : l'entraînement distribué et l'exécution non-eager.

### Entraînement distribué

Vous pourriez souvent distribuer votre entraînement de Machine Learning sur plusieurs GPU, plusieurs machines ou TPU. Vous faites probablement cela avec l'API TensorFlow `[tf.distribute.Strategy](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)`. 

Vous pouvez l'utiliser de la même manière avec la plupart des stratégies de distribution avec une utilisation limitée lors de l'utilisation de `ParameterServer` dans une boucle d'entraînement personnalisée.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-79.png)
_Entraînement distribué_

Vous pouvez trouver de bons exemples sur la façon d'utiliser ces stratégies avec TensorFlow Keras [ici](https://www.tensorflow.org/guide/distributed_training#examples_and_tutorials).

### Exécution non-eager

Dans TensorFlow 2, l'exécution eager est activée par défaut. Mais vous voudrez souvent utiliser [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) pour créer des graphes à partir de vos programmes. C'est un outil de transformation qui crée des graphes de flux de données indépendants de Python à partir de votre code Python.

L'une des premières versions de ce projet utilisait certains appels Numpy, mais devinez quoi, vous pouvez maintenant utiliser le code de la même manière en mode non-eager également.

## **Merci d'avoir lu !**

Merci de m'avoir suivi jusqu'à la fin. Vous pouvez maintenant surveiller vos projets de Machine Learning depuis n'importe où sur votre appareil mobile et les faire passer au niveau supérieur. J'espère que vous êtes aussi excité de commencer à utiliser cela que je l'étais.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@rishit_dagli](https://twitter.com/rishit_dagli).