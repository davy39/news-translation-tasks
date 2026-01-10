---
title: Commencer avec TensorFlow sur le droit et les statistiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T07:34:40.000Z'
originalURL: https://freecodecamp.org/news/tensorflow-starter-on-law-and-statistics-646072b93b5a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xqr3ulVKnBwueUVk
tags:
- name: Law
  slug: law
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: statistics
  slug: statistics
- name: TensorFlow
  slug: tensorflow
seo_title: Commencer avec TensorFlow sur le droit et les statistiques
seo_desc: 'By Daniel Deutsch


  What this is about

  What we will use

  Get started

  Shell commands for installing everything you need

  Get data and draw a plot

  Import everything you need

  Create and plot some numbers

  Build a TensorFlow model

  Prepare data

  Set up variabl...'
---

Par Daniel Deutsch

* [De quoi il s'agit](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#de-quoi-il-sagit)
* [Ce que nous allons utiliser](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#ce-que-nous-allons-utiliser)
* [Commencer](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#commencer)
* [Commandes shell pour installer tout ce dont vous avez besoin](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#commandes-shell-pour-installer-tout-ce-dont-vous-avez-besoin)
* [Obtenir des données et tracer un graphique](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#obtenir-des-donnees-et-tracer-un-graphique)
* [Importer tout ce dont vous avez besoin](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#importer-tout-ce-dont-vous-avez-besoin)
* [Créer et tracer quelques nombres](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#creer-et-tracer-quelques-nombres)
* [Construire un modèle TensorFlow](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#construire-un-modele-tensorflow)
* [Préparer les données](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#preparer-les-donnees)
* [Configurer les variables et les opérations pour TensorFlow](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#configurer-les-variables-et-les-operations-pour-tensorflow)
* [Démarrer les calculs avec une session TensorFlow](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#demarrer-les-calculs-avec-une-session-tensorflow)
* [Visualiser le résultat et le processus](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md#visualiser-le-resultat-et-le-processus)

### De quoi il s'agit

Alors que j'explore TensorFlow, je voulais construire un exemple pour débutants et le documenter. Il s'agit d'un exemple très basique qui utilise une optimisation par descente de gradient pour entraîner des paramètres avec TensorFlow. Les variables clés sont **preuves** et **condamnations**. Cela illustrera :

* comment le nombre de condamnations dépend du nombre de preuves
* comment prédire le nombre de condamnations en utilisant un modèle de régression

Le fichier Python se trouve dans mon [dépôt sur GitHub](https://github.com/Createdd/lawstatistics/blob/feature/ReferenceBranchForArticle/evidencePrediction.py).

[Voir l'article avec une meilleure mise en forme sur GitHub.](https://github.com/Createdd/Writing/blob/master/2018/articles/LawStatisticsExample.md)

### Ce que nous allons utiliser

#### 1. TensorFlow (en tant que tf)

[Tenseurs](https://www.tensorflow.org/programmers_guide/tensors)

* tf.placeholders
* tf.Variables

[Fonction d'assistance](https://www.tensorflow.org/programmers_guide/variables#initializing_variables)

* tf.global_variables_initializer

[Opérations mathématiques](https://www.tensorflow.org/api_guides/python/math_ops)

* tf.add
* tf.multiply
* tf.reduce_sum
* tf.pow

[Construction d'un graphe](https://www.tensorflow.org/programmers_guide/graphs#building_a_tfgraph)

* tf.train.GradientDescentOptimizer

[Session](https://www.tensorflow.org/programmers_guide/graphs#executing_a_graph_in_a_tfsession)

* tf.Session

#### 2. Numpy (en tant que np)

* np.random.seed
* np.random.zeros
* np.random.randint
* np.random.randn
* np.random.asanyarray

#### 3. Matplotlib

#### 4. Math

### Commencer

Installez TensorFlow avec virtualenv. Voir le [guide](https://www.tensorflow.org/install/install_mac) sur le site TF.

#### Commandes shell pour installer tout ce dont vous avez besoin

```
sudo easy_install pip
```

```
pip3 install --upgrade virtualenv
```

```
virtualenv --system-site-packages <targetDirectory>
```

```
cd <targetDirectory>
```

```
source ./bin/activate
```

```
easy_install -U pip3
```

```
pip3 install tensorflow
```

```
pip3 install matplotlib
```

### Obtenir des données et tracer un graphique

#### Importer tout ce dont vous avez besoin

```
import tensorflow as tfimport numpy as npimport mathimport matplotlibmatplotlib.use('TkAgg')import matplotlib.pyplot as pltimport matplotlib.animation as animation
```

Comme vous pouvez le voir, j'utilise le backend "TkAgg" de matplotlib. Cela me permet de déboguer avec mon vsCode et ma configuration macOS sans aucune installation compliquée supplémentaire.

#### Créer et tracer quelques nombres

```
# Générer des nombres de preuves entre 10 et 20# Générer un nombre de condamnations à partir des preuves avec un bruit aléatoire ajouté
np.random.seed(42)
sampleSize = 200
numEvid = np.random.randint(low=10, high=50, size=sampleSize)
numConvict = numEvid * 10 + np.random.randint(low=200, high=400, size=sampleSize)
```

```
# Tracer les données pour avoir une idée
plt.title("Nombre de condamnations basées sur les preuves")
plt.plot(numEvid, numConvict, "bx")
plt.xlabel("Nombre de preuves")
plt.ylabel("Nombre de condamnations")
plt.show(block=False)  # Utilisez le mot-clé 'block' pour remplacer le comportement de blocage
```

Je crée des valeurs aléatoires pour les preuves. Le nombre de condamnations dépend de la quantité (nombre) de preuves, avec un bruit aléatoire. Bien sûr, ces nombres sont inventés, mais ils sont juste utilisés pour prouver un point.

### Construire un modèle TensorFlow

Pour construire un modèle basique de machine learning, nous devons préparer les données. Ensuite, nous faisons des prédictions, mesurons la perte et optimisons en minimisant la perte.

#### Préparer les données

```
# créer une fonction pour normaliser les valeurs
# utiliser 70% des données pour l'entraînement (les 30% restants doivent être utilisés pour les tests)
def normalize(array):
    return (array - array.mean()) / array.std()
```

```
numTrain = math.floor(sampleSize * 0.7)
```

```
# convertir la liste en un tableau et normaliser le tableau
trainEvid = np.asanyarray(numEvid[:numTrain])
trainConvict = np.asanyarray(numConvict[:numTrain])
trainEvidNorm = normalize(trainEvid)
trainConvictdNorm = normalize(trainConvict)
```

```
testEvid = np.asanyarray(numEvid[numTrain:])
testConvict = np.asanyarray(numConvict[numTrain:])
testEvidNorm = normalize(testEvid)
testConvictdNorm = normalize(testConvict)
```

Nous divisons les données en portions d'entraînement et de test. Ensuite, nous normalisons les valeurs, car cela est nécessaire pour les projets de machine learning. (Voir aussi « [mise à l'échelle des caractéristiques](https://en.wikipedia.org/wiki/Feature_scaling) ».)

#### Configurer les variables et les opérations pour TensorFlow

```
# définir les placeholders et les variables
tfEvid = tf.placeholder(tf.float32, name="Evid")
tfConvict = tf.placeholder(tf.float32, name="Convict")
tfEvidFactor = tf.Variable(np.random.randn(), name="EvidFactor")
tfConvictOffset = tf.Variable(np.random.randn(), name="ConvictOffset")
```

```
# définir l'opération pour prédire la condamnation basée sur les preuves en ajoutant les deux valeurs
# définir une fonction de perte (erreur quadratique moyenne)
tfPredict = tf.add(tf.multiply(tfEvidFactor, tfEvid), tfConvictOffset)
tfCost = tf.reduce_sum(tf.pow(tfPredict - tfConvict, 2)) / (2 * numTrain)
```

```
# définir un taux d'apprentissage et un optimiseur de descente de gradient
learningRate = 0.1
gradDesc = tf.train.GradientDescentOptimizer(learningRate).minimize(tfCost)
```

Les différences pragmatiques entre `tf.placeholder` et `tf.Variable` sont :

* les placeholders sont alloués pour le stockage des données, et les valeurs initiales ne sont pas requises
* les variables sont utilisées pour les paramètres à apprendre, et les valeurs initiales sont requises. Les valeurs peuvent être dérivées de l'entraînement.

J'utilise les opérateurs TensorFlow précisément comme `tf.add()`, car il est assez clair quelle bibliothèque est utilisée pour le calcul. Cela est au lieu d'utiliser l'opérateur `+`.

#### Démarrer les calculs avec une session TensorFlow

```
# initialiser les variables
init = tf.global_variables_initializer()
```

```
with tf.Session() as sess:
    sess.run(init)
```

```
    # configurer les paramètres d'itération
    displayEvery = 2
    numTrainingSteps = 50
```

```
    # Calculer le nombre de lignes pour l'animation
    # définir les variables pour la mise à jour pendant l'animation
    numPlotsAnim = math.floor(numTrainingSteps / displayEvery)
    evidFactorAnim = np.zeros(numPlotsAnim)
    convictOffsetAnim = np.zeros(numPlotsAnim)
    plotIndex = 0
```

```
    # itérer à travers les données d'entraînement
    for i in range(numTrainingSteps):
```

```
        # ======== Démarrer l'entraînement en exécutant la session et en alimentant le gradDesc
        for (x, y) in zip(trainEvidNorm, trainConvictdNorm):
            sess.run(gradDesc, feed_dict={tfEvid: x, tfConvict: y})
```

```
        # Imprimer le statut de l'apprentissage
        if (i + 1) % displayEvery == 0:
            cost = sess.run(
                tfCost, feed_dict={tfEvid: trainEvidNorm, tfConvict: trainConvictdNorm}
            )
            print(
                "itération #:",
                "%04d" % (i + 1),
                "coût=",
                "{:.9f}".format(cost),
                "evidFactor=",
                sess.run(tfEvidFactor),
                "convictOffset=",
                sess.run(tfConvictOffset),
            )
```

```
            # stocker le résultat de chaque étape dans les variables d'animation
            evidFactorAnim[plotIndex] = sess.run(tfEvidFactor)
            convictOffsetAnim[plotIndex] = sess.run(tfConvictOffset)
            plotIndex += 1
```

```
    # journaliser le résultat optimisé
    print("Optimisé!")
    trainingCost = sess.run(
        tfCost, feed_dict={tfEvid: trainEvidNorm, tfConvict: trainConvictdNorm}
    )
    print(
        "Coût d'entraînement=",
        trainingCost,
        "evidFactor=",
        sess.run(tfEvidFactor),
        "convictOffset=",
        sess.run(tfConvictOffset),
        "\n",
    )
```

Maintenant, nous arrivons à l'entraînement réel et à la partie la plus intéressante.

Le graphe est maintenant exécuté dans une `[tf.Session](https://www.tensorflow.org/programmers_guide/graphs#executing_a_graph_in_a_tfsession)`. J'utilise le « feeding » car il vous permet d'injecter des données dans n'importe quel tenseur dans un graphe de calcul. Vous pouvez en savoir plus sur la lecture des données [ici](https://www.tensorflow.org/api_guides/python/reading_data#Feeding).

`tf.Session()` est utilisé pour créer une session qui est automatiquement fermée à la sortie du contexte. La session se ferme également lorsqu'une exception non capturée est levée.

La méthode `tf.Session.run` est le principal mécanisme pour exécuter une `tf.Operation` ou évaluer un `tf.Tensor`. Vous pouvez passer un ou plusieurs objets `tf.Operation` ou `tf.Tensor` à `tf.Session.run`, et TensorFlow exécutera les opérations nécessaires pour calculer le résultat.

Tout d'abord, nous exécutons l'entraînement par descente de gradient tout en lui fournissant les données d'entraînement normalisées. Après cela, nous calculons la perte.

Nous répétons ce processus jusqu'à ce que les améliorations par étape soient très petites. Gardez à l'esprit que les `tf.Variables` (les paramètres) ont été adaptés tout au long et reflètent maintenant un optimum.

### Visualiser le résultat et le processus

```
# dé-normaliser les variables pour qu'elles soient à nouveau traçables
    trainEvidMean = trainEvid.mean()
    trainEvidStd = trainEvid.std()
    trainConvictMean = trainConvict.mean()
    trainConvictStd = trainConvict.std()
    xNorm = trainEvidNorm * trainEvidStd + trainEvidMean
    yNorm = (
        sess.run(tfEvidFactor) * trainEvidNorm + sess.run(tfConvictOffset)
    ) * trainConvictStd + trainConvictMean
```

```
    # Tracer le graphique des résultats
    plt.figure()
```

```
    plt.xlabel("Nombre de preuves")
    plt.ylabel("Nombre de condamnations")
```

```
    plt.plot(trainEvid, trainConvict, "go", label="Données d'entraînement")
    plt.plot(testEvid, testConvict, "mo", label="Données de test")
    plt.plot(xNorm, yNorm, label="Régession apprise")
    plt.legend(loc="upper left")
```

```
    plt.show()
```

```
    # Tracer un graphique animé qui montre le processus d'optimisation
    fig, ax = plt.subplots()
    line, = ax.plot(numEvid, numConvict)
```

```
    plt.rcParams["figure.figsize"] = (10, 8) # ajout de paramètres de taille fixe pour garder l'animation à l'échelle
    plt.title("Ajustement de la ligne de régression par descente de gradient")
    plt.xlabel("Nombre de preuves")
    plt.ylabel("Nombre de condamnations")
    plt.plot(trainEvid, trainConvict, "go", label="Données d'entraînement")
    plt.plot(testEvid, testConvict, "mo", label="Données de test")
```

```
    # définir une fonction d'animation qui change les ydata
    def animate(i):
        line.set_xdata(xNorm)
        line.set_ydata(
            (evidFactorAnim[i] * trainEvidNorm + convictOffsetAnim[i]) * trainConvictStd
            + trainConvictMean
        )
        return (line,)
```

```
    # Initialiser l'animation avec des zéros pour y
    def initAnim():
        line.set_ydata(np.zeros(shape=numConvict.shape[0]))
        return (line,)
```

```
    # appeler l'animation
    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=np.arange(0, plotIndex),
        init_func=initAnim,
        interval=200,
        blit=True,
    )
```

```
    plt.show()
```

Pour visualiser le processus, il est utile de tracer le résultat et peut-être même le processus d'optimisation.

![Image](https://cdn-media-1.freecodecamp.org/images/w31dQ19xkDhfLzWpeqqUkvmXVtsNeK-JkWDg)

Consultez ce [cours Pluralsight](https://www.pluralsight.com/courses/tensorflow-getting-started) qui m'a beaucoup aidé à commencer. :)

Merci d'avoir lu mon article ! N'hésitez pas à laisser vos commentaires !

Daniel est un étudiant en LL.M. en droit des affaires, travaillant comme ingénieur logiciel et organisateur d'événements technologiques à Vienne. Ses efforts d'apprentissage personnel actuels se concentrent sur le machine learning.

Connectez-vous sur :

* [LinkedIn](https://www.linkedin.com/in/createdd)
* [Github](https://github.com/Createdd)
* [Medium](https://medium.com/@ddcreationstudi)
* [Twitter](https://twitter.com/DDCreationStudi)
* [Steemit](https://steemit.com/@createdd)
* [Hashnode](https://hashnode.com/@DDCreationStudio)