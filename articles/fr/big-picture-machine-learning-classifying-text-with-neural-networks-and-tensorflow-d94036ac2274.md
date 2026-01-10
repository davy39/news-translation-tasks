---
title: 'Big Picture Machine Learning: Classifier du texte avec des réseaux de neurones
  et TensorFlow'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-09T21:49:41.000Z'
originalURL: https://freecodecamp.org/news/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W2vzGrXR1ua5KN-X0m9oMw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: 'Big Picture Machine Learning: Classifier du texte avec des réseaux de
  neurones et TensorFlow'
seo_desc: 'By Déborah Mesquita

  Developers often say that if you want to get started with machine learning, you
  should first learn how the algorithms work. But my experience shows otherwise.

  I say you should first be able to see the big picture: how the applicat...'
---

Par Débora Mesquita

Les développeurs disent souvent que si vous voulez commencer avec le machine learning, vous devriez d'abord apprendre comment les algorithmes fonctionnent. Mais mon expérience montre le contraire.

Je dis que vous devriez d'abord être capable de voir le big picture : **comment les applications fonctionnent**. Une fois que vous comprenez cela, il devient beaucoup plus facile de plonger en profondeur et d'explorer le fonctionnement interne des algorithmes.

Alors, comment développer une intuition et atteindre cette compréhension globale du machine learning ? Une bonne façon de faire cela est de **créer des modèles de machine learning**.

En supposant que vous ne savez toujours pas comment créer tous ces algorithmes à partir de zéro, vous voudrez utiliser une bibliothèque qui a déjà tous ces algorithmes implémentés pour vous. Et cette bibliothèque est **TensorFlow**.

Dans cet article, nous allons créer un modèle de machine learning pour classer des textes en catégories. Nous allons couvrir les sujets suivants :

1. **Comment TensorFlow fonctionne**
2. **Qu'est-ce qu'un modèle de machine learning**
3. **Qu'est-ce qu'un réseau de neurones**
4. **Comment le réseau de neurones apprend**
5. **Comment manipuler les données et les passer aux entrées du réseau de neurones**
6. **Comment exécuter le modèle et obtenir les résultats de prédiction**

Vous allez probablement apprendre beaucoup de nouvelles choses, alors commençons ! 🚀

### TensorFlow

[TensorFlow](https://www.tensorflow.org/) est une bibliothèque open-source pour le machine learning, créée à l'origine par Google. Le nom de la bibliothèque nous aide à comprendre comment nous travaillons avec elle : les tenseurs sont des tableaux multidimensionnels qui circulent à travers les nœuds d'un graphe.

#### tf.Graph

Chaque calcul dans TensorFlow est représenté comme un graphe de flux de données. Ce graphe a deux éléments :

* un ensemble de `tf.Operation`, qui représente des unités de calcul
* un ensemble de `tf.Tensor`, qui représente des unités de données

Pour voir comment tout cela fonctionne, vous allez créer ce graphe de flux de données :

![Image](https://cdn-media-1.freecodecamp.org/images/FqZ0WWUano-1PMy9ip69CsKrZYFjlaC4iozV)
_Un graphe qui calcule x+y_

Vous allez définir `x = [1,3,6]` et `y = [1,1,1]`. Comme le graphe fonctionne avec `tf.Tensor` pour représenter les unités de données, vous allez créer des tenseurs constants :

```
import tensorflow as tf
```

```
x = tf.constant([1,3,6]) y = tf.constant([1,1,1])
```

Maintenant, vous allez définir l'unité d'opération :

```
import tensorflow as tf
```

```
x = tf.constant([1,3,6]) y = tf.constant([1,1,1])
```

```
op = tf.add(x,y)
```

Vous avez tous les éléments du graphe. Maintenant, vous devez construire le graphe :

```
import tensorflow as tf
```

```
my_graph = tf.Graph()
```

```
with my_graph.as_default():    x = tf.constant([1,3,6])     y = tf.constant([1,1,1])
```

```
    op = tf.add(x,y)
```

Voici comment fonctionne le flux de travail de TensorFlow : vous créez d'abord un graphe, et seulement ensuite vous pouvez effectuer les calculs (exécuter réellement les nœuds du graphe avec des opérations). Pour exécuter le graphe, vous devrez créer une `tf.Session`.

#### tf.Session

Un objet `tf.Session` encapsule l'environnement dans lequel les objets `Operation` sont exécutés et les objets `Tensor` sont évalués (d'après [la documentation](https://www.tensorflow.org/api_docs/python/tf/Session)). Pour cela, nous devons définir quel graphe sera utilisé dans la Session :

```
import tensorflow as tf
```

```
my_graph = tf.Graph()
```

```
with tf.Session(graph=my_graph) as sess:    x = tf.constant([1,3,6])     y = tf.constant([1,1,1])
```

```
    op = tf.add(x,y)
```

Pour exécuter les opérations, vous utiliserez la méthode `tf.Session.run()`. Cette méthode exécute une "étape" du calcul TensorFlow, en exécutant le fragment de graphe nécessaire pour exécuter chaque objet `Operation` et évaluer chaque `Tensor` passé dans l'argument `fetches`. Dans votre cas, vous allez exécuter une étape des opérations de somme :

```
import tensorflow as tf
```

```
my_graph = tf.Graph()
```

```
with tf.Session(graph=my_graph) as sess:    x = tf.constant([1,3,6])     y = tf.constant([1,1,1])
```

```
    op = tf.add(x,y)    result = sess.run(fetches=op)    print(result)
```

```
>>>; [2 4 7]
```

### Un modèle prédictif

Maintenant que vous savez comment TensorFlow fonctionne, vous devez apprendre à créer un modèle prédictif. En bref,

**Algorithme de machine learning** + **données** = **modèle prédictif**

Le processus de construction d'un modèle est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/gdMcFEDuaj8M7U0IQsxh77naKKo8vRKbsROi)
_Le processus de création d'un modèle prédictif_

Comme vous pouvez le voir, le modèle consiste en un algorithme de machine learning "entraîné" avec des données. Lorsque vous avez le modèle, vous obtiendrez des résultats comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/GKPyWdL-Z31sZhmSFqGGH6y6Bw6VAqiu7PaJ)
_Flux de travail de prédiction_

Le but du modèle que vous allez créer est de classer les textes en catégories, nous définissons cela :

**entrée** : texte, **résultat** : catégorie

Nous avons un ensemble de données d'entraînement avec tous les textes étiquetés (chaque texte a une étiquette indiquant à quelle catégorie il appartient). En machine learning, ce type de tâche est appelé **apprentissage supervisé**.

> "Nous connaissons les bonnes réponses. L'algorithme fait des prédictions de manière itérative sur les données d'entraînement et est corrigé par l'enseignant." — [Jason Brownlee](http://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/)

Vous allez classer les données en catégories, donc c'est aussi une tâche de **classification**.

Pour créer le modèle, nous allons utiliser des réseaux de neurones.

### Réseaux de neurones

Un réseau de neurones est un modèle computationnel (une façon de décrire un système en utilisant le langage mathématique et les concepts mathématiques). Ces systèmes sont auto-apprenants et entraînés, plutôt que programmés explicitement.

Les réseaux de neurones sont inspirés par notre système nerveux central. Ils ont des nœuds connectés qui sont similaires à nos neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/ngj7GZs1s5M0eOI3RyNVKqqj17menI4lJjMr)
_Un réseau de neurones_

Le Perceptron était le premier algorithme de réseau de neurones. [Cet article](https://appliedgo.net/perceptron/) explique très bien le fonctionnement interne d'un perceptron (l'animation "Inside an artificial neuron" est fantastique).

Pour comprendre comment fonctionne un réseau de neurones, nous allons en fait construire une architecture de réseau de neurones avec TensorFlow. Cette architecture a été utilisée par [Aymeric Damien](https://github.com/aymericdamien) dans [cet exemple](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/notebooks/3_NeuralNetworks/multilayer_perceptron.ipynb).

#### Architecture du réseau de neurones

Le réseau de neurones aura 2 couches cachées ([vous devez choisir](http://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw) combien de couches cachées le réseau aura, cela fait partie de la conception de l'architecture). Le travail de chaque couche cachée est de [transformer les entrées en quelque chose que la couche de sortie peut utiliser](http://stats.stackexchange.com/questions/63152/what-does-the-hidden-layer-in-a-neural-network-compute).

**Couche cachée 1**

![Image](https://cdn-media-1.freecodecamp.org/images/6YQgGFOd-HLll7zGB7gA-sjCkVb4RYuZLnka)
_Couche d'entrée et 1ère couche cachée_

Vous devez également définir combien de nœuds la 1ère couche cachée aura. Ces nœuds sont également appelés caractéristiques ou neurones, et dans l'image ci-dessus, ils sont représentés par chaque cercle.

Dans la couche d'entrée, chaque nœud correspond à un mot du jeu de données (nous verrons comment cela fonctionne plus tard).

Comme expliqué [ici](https://appliedgo.net/perceptron/), chaque nœud (neurone) est multiplié par un poids. Chaque nœud a une valeur de poids, et pendant la phase d'entraînement, le réseau de neurones ajuste ces valeurs afin de produire une sortie correcte (attendez, nous en apprendrons plus à ce sujet dans une minute).

En plus de multiplier chaque nœud d'entrée par un poids, le réseau ajoute également un biais ([rôle du biais dans les réseaux de neurones](http://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks)).

Dans votre architecture, après avoir multiplié les entrées par les poids et additionné les valeurs au biais, les données passent également par une **fonction d'activation**. Cette fonction d'activation définit la sortie finale de chaque nœud. Une analogie : imaginez que chaque nœud est une lampe, la fonction d'activation indique si la lampe s'allumera ou non.

Il existe [de nombreux types de fonctions d'activation](https://en.wikipedia.org/wiki/Activation_function). Vous utiliserez l'unité linéaire rectifiée (ReLu). Cette fonction est définie ainsi :

_f(x)_ = _max(0,x)_ [la sortie est x ou 0 (zéro), selon la valeur la plus grande]

Exemples : si **_x_ = -1**, alors **_f(x) = 0_**_(zéro) ; si **x = 0.7**, alors **f(x) = 0.7**_.

**Couche cachée 2**

La 2ème couche cachée fait exactement ce que la 1ère couche cachée fait, mais maintenant l'entrée de la 2ème couche cachée est la sortie de la 1ère.

![Image](https://cdn-media-1.freecodecamp.org/images/hvIts6lxc2bXXMQzEA8af3Fk760Ih2zjoFl3)
_1ère et 2ème couches cachées_

**Couche de sortie**

Et nous arrivons enfin à la dernière couche, la couche de sortie. Vous utiliserez le [codage one-hot](https://en.wikipedia.org/wiki/One-hot) pour obtenir les résultats de cette couche. Dans ce codage, un seul bit a la valeur 1 et tous les autres ont une valeur zéro. Par exemple, si nous voulons coder trois catégories (sports, espace et infographie) :

```
+-------------------+-----------+|    catégorie       |   valeur   |+-------------------|-----------+|      sports       |    001    ||      espace        |    010    || infographie       |    100    ||-------------------|-----------|
```

Ainsi, le nombre de nœuds de sortie est le nombre de classes du jeu de données d'entrée.

Les valeurs de la couche de sortie sont également multipliées par les poids et nous ajoutons également le biais, mais maintenant la fonction d'activation est différente.

Vous voulez étiqueter chaque texte avec une catégorie, et ces catégories sont mutuellement exclusives (un texte n'appartient pas à deux catégories en même temps). Pour tenir compte de cela, au lieu d'utiliser la fonction d'activation ReLu, vous utiliserez la fonction [Softmax](https://en.wikipedia.org/wiki/Softmax_function). Cette fonction transforme la sortie de chaque unité en une valeur comprise entre 0 et 1 et s'assure également que la somme de toutes les unités est égale à 1. De cette manière, la sortie nous indiquera la probabilité de chaque texte pour chaque catégorie.

```
| 1.2                    0.46|| 0.9   -> [softmax] ->  0.34|| 0.4                    0.20|
```

Et maintenant vous avez le graphe de flux de données de votre réseau de neurones. En traduisant tout ce que nous avons vu jusqu'à présent en code, le résultat est :

```
# Paramètres du réseau
n_hidden_1 = 10        # Nombre de caractéristiques de la 1ère couche
n_hidden_2 = 5         # Nombre de caractéristiques de la 2ème couche
n_input = total_words  # Mots dans le vocabulaire
n_classes = 3          # Catégories : infographie, espace et baseball
```

```
def multilayer_perceptron(input_tensor, weights, biases):    layer_1_multiplication = tf.matmul(input_tensor, weights['h1'])    layer_1_addition = tf.add(layer_1_multiplication, biases['b1'])    layer_1_activation = tf.nn.relu(layer_1_addition)
```

```
# Couche cachée avec activation RELU    layer_2_multiplication = tf.matmul(layer_1_activation, weights['h2'])    layer_2_addition = tf.add(layer_2_multiplication, biases['b2'])    layer_2_activation = tf.nn.relu(layer_2_addition)
```

```
# Couche de sortie avec activation linéaire    out_layer_multiplication = tf.matmul(layer_2_activation, weights['out'])    out_layer_addition = out_layer_multiplication + biases['out']
```

```
return out_layer_addition
```

(Nous parlerons du code pour la fonction d'activation de la couche de sortie plus tard.)

### Comment le réseau de neurones apprend

Comme nous l'avons vu précédemment, les valeurs de poids sont mises à jour pendant que le réseau est entraîné. Maintenant, nous allons voir comment cela se passe dans l'environnement TensorFlow.

#### tf.Variable

Les poids et les biais sont stockés dans des variables (`tf.Variable`). Ces variables maintiennent l'état dans le graphe à travers les appels à `run()`. En machine learning, nous commençons généralement les valeurs de poids et de biais par une [distribution normale](https://en.wikipedia.org/wiki/Normal_distribution).

```
weights = {    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))}biases = {    'b1': tf.Variable(tf.random_normal([n_hidden_1])),    'b2': tf.Variable(tf.random_normal([n_hidden_2])),    'out': tf.Variable(tf.random_normal([n_classes]))}
```

Lorsque nous exécutons le réseau pour la première fois (c'est-à-dire que les valeurs de poids sont celles définies par la distribution normale) :

```
valeurs d'entrée : x
poids : w
biais : b
valeurs de sortie : z
```

```
valeurs attendues : expected
```

Pour savoir si le réseau apprend ou non, vous devez comparer les valeurs de sortie (_z_) avec les valeurs attendues (_expected_). Et comment calculons-nous cette différence (perte) ? Il existe de nombreuses méthodes pour cela. Parce que nous travaillons avec une tâche de classification, la meilleure mesure pour la perte est l'[erreur d'entropie croisée](https://en.wikipedia.org/wiki/Cross_entropy).

[James D. McCaffrey](https://jamesmccaffrey.wordpress.com/) a écrit [une explication brillante](https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/) sur pourquoi c'est la meilleure méthode pour ce type de tâche.

Avec TensorFlow, vous allez calculer l'erreur d'entropie croisée en utilisant la méthode `tf.nn.softmax_cross_entropy_with_logits()` (ici se trouve la fonction d'activation softmax) et calculer l'erreur moyenne (`tf.reduce_mean()`).

```
# Construire le modèle
prediction = multilayer_perceptron(input_tensor, weights, biases)
```

```
# Définir la perte
entropy_loss = tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=output_tensor)
loss = tf.reduce_mean(entropy_loss)
```

Vous voulez trouver les meilleures valeurs pour les poids et les biais afin de minimiser l'erreur de sortie (la différence entre la valeur que nous avons obtenue et la valeur correcte). Pour cela, vous allez utiliser la méthode de [descente de gradient](https://en.wikipedia.org/wiki/Gradient_descent). Plus précisément, vous allez utiliser la [descente de gradient stochastique](https://en.wikipedia.org/wiki/Stochastic_gradient_descent).

![Image](https://cdn-media-1.freecodecamp.org/images/MI54d2-a1xt1hEAvaTeNh-K8BkC7Y716wsvt)
_Descente de gradient. Source : [https://sebastianraschka.com/faq/docs/closed-form-vs-gd.html](https://sebastianraschka.com/faq/docs/closed-form-vs-gd.html" rel="noopener" target="_blank" title=")_

Il existe également de nombreux algorithmes pour calculer la descente de gradient, vous allez utiliser l'[Estimation Adaptative du Moment (Adam)](http://sebastianruder.com/optimizing-gradient-descent/index.html#adam). Pour utiliser cet algorithme dans TensorFlow, vous devez passer la valeur learning_rate, qui détermine les étapes incrémentielles des valeurs pour trouver les meilleures valeurs de poids.

La méthode `tf.train.AdamOptimizer(learning_rate)**.minimize(loss)**` est un [sucre syntaxique](https://en.wikipedia.org/wiki/Syntactic_sugar) qui fait deux choses :

1. **compute_gradients**(loss, <liste de variables>)
2. **apply_gradients**(<liste de variables>)

La méthode met à jour toutes les `tf.Variables` avec les nouvelles valeurs, donc nous n'avons pas besoin de passer la liste des variables. Et maintenant vous avez le code pour entraîner le réseau :

```
learning_rate = 0.001
```

```
# Construire le modèle
prediction = multilayer_perceptron(input_tensor, weights, biases)
```

```
# Définir la perte
entropy_loss = tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=output_tensor)
loss = tf.reduce_mean(entropy_loss)
```

```
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
```

### Manipulation des données

Le jeu de données que vous allez utiliser contient de nombreux textes en anglais et nous devons manipuler ces données pour les passer au réseau de neurones. Pour cela, vous allez faire deux choses :

1. Créer un index pour chaque mot
2. Créer une matrice pour chaque texte, où les valeurs sont 1 si un mot est dans le texte et 0 sinon

Voyons le code pour comprendre ce processus :

```
import numpy as np    #numpy est un package pour le calcul scientifique
from collections import Counter
```

```
vocab = Counter()
```

```
text = "Hi from Brazil"
```

```
#Obtenir tous les mots
for word in text.split(' '):    vocab[word]+=1        #Convertir les mots en index
def get_word_2_index(vocab):    word2index = {}    for i,word in enumerate(vocab):        word2index[word] = i            return word2index
```

```
#Maintenant nous avons un index
word2index = get_word_2_index(vocab)
```

```
total_words = len(vocab)
```

```
#C'est ainsi que nous créons un tableau numpy (notre matrice)
matrix = np.zeros((total_words),dtype=float)
```

```
#Maintenant nous remplissons les valeurs
for word in text.split():    matrix[word2index[word]] += 1
```

```
print(matrix)
```

```
>>> [ 1.  1.  1.]
```

Dans l'exemple ci-dessus, le texte était "Hi from Brazil" et la matrice était **[ 1. 1. 1.]**. Que se passe-t-il si le texte était seulement "Hi" ?

```
matrix = np.zeros((total_words),dtype=float)
```

```
text = "Hi"
```

```
for word in text.split():    matrix[word2index[word.lower()]] += 1
```

```
print(matrix)
```

```
>>> [ 1.  0.  0.]
```

Vous allez faire la même chose avec les étiquettes (catégories des textes), mais maintenant vous allez utiliser le codage one-hot :

```
y = np.zeros((3),dtype=float)
```

```
if category == 0:    y[0] = 1.        # [ 1.  0.  0.]elif category == 1:    y[1] = 1.        # [ 0.  1.  0.]else:     y[2] = 1.       # [ 0.  0.  1.]
```

### Exécution du graphe et obtention des résultats

Maintenant vient la meilleure partie : obtenir les résultats du modèle. D'abord, examinons de plus près le jeu de données d'entrée.

#### Le jeu de données

Vous allez utiliser les [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/), un jeu de données avec 18 000 messages sur 20 sujets. Pour charger ce jeu de données, vous allez utiliser la bibliothèque [scikit-learn](http://scikit-learn.org/stable/index.html). Nous allons utiliser seulement 3 catégories : **comp.graphics**, **sci.space** et **rec.sport.baseball**. Le scikit-learn a deux sous-ensembles : un pour l'entraînement et un pour les tests. La recommandation est que **vous ne devriez jamais regarder les données de test**, car cela peut interférer avec vos choix lors de la création du modèle. Vous ne voulez pas créer un modèle pour prédire ces données de test spécifiques, vous voulez créer un modèle avec une bonne **généralisation**.

Voici comment vous allez charger les jeux de données :

```
from sklearn.datasets import fetch_20newsgroups
```

```
categories = ["comp.graphics","sci.space","rec.sport.baseball"]
```

```
newsgroups_train = fetch_20newsgroups(subset='train', categories=categories)
newsgroups_test = fetch_20newsgroups(subset='test', categories=categories)
```

#### Entraînement du modèle

Dans la [terminologie des réseaux de neurones](http://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks), une époque = une passe avant (obtenir les valeurs de sortie) et une passe arrière (mettre à jour les poids) de _tous_ les exemples d'entraînement.

Vous vous souvenez de la méthode `tf.Session.run()` ? Examinons-la de plus près :

`tf.Session.run(fetches, feed_dict=None, options=None, run_metadata=None)`

Dans le graphe de flux de données du début de cet article, vous avez utilisé l'opération de somme, mais nous pouvons également passer une liste de choses à exécuter. Dans cette exécution du réseau de neurones, vous allez passer deux choses : le calcul de la perte et l'étape d'optimisation.

Le paramètre `feed_dict` est l'endroit où nous passons les données pour chaque étape d'exécution. Pour passer ces données, nous devons définir des `tf.placeholders` (pour alimenter le `feed_dict`).

Comme le dit la documentation de TensorFlow :

> "Un placeholder existe uniquement pour servir de cible aux feeds. Il n'est pas initialisé et ne contient aucune donnée." — [Source](https://www.tensorflow.org/programmers_guide/reading_data)

Vous allez donc définir vos placeholders comme ceci :

```
n_input = total_words # Mots dans le vocabulaire
n_classes = 3         # Catégories : infographie, sci.space et baseball
```

```
input_tensor = tf.placeholder(tf.float32,[None, n_input],name="input")
output_tensor = tf.placeholder(tf.float32,[None, n_classes],name="output")
```

Vous allez séparer les données d'entraînement en lots :

> "Si vous utilisez des placeholders pour **alimenter l'entrée**, vous pouvez spécifier une **dimension de lot variable** en créant le placeholder avec tf.placeholder(…, shape=[**None**, …]). L'élément None de la forme correspond à une dimension de taille variable." — [Source](https://www.tensorflow.org/versions/r0.11/resources/faq)

Nous allons alimenter le dict avec un lot plus grand lors du test du modèle, c'est pourquoi vous devez définir une dimension de lot variable.

La fonction `get_batches()` nous donne le nombre de textes avec la taille du lot. Et maintenant nous pouvons exécuter le modèle :

```
training_epochs = 10
```

```
# Lancer le graphe
with tf.Session() as sess:    sess.run(init) #init les variables (distribution normale, vous vous souvenez ?)
```

```
    # Cycle d'entraînement    for epoch in range(training_epochs):        avg_cost = 0.        total_batch = int(len(newsgroups_train.data)/batch_size)        # Boucle sur tous les lots        for i in range(total_batch):            batch_x,batch_y = get_batch(newsgroups_train,i,batch_size)            # Exécuter l'opération d'optimisation (rétropropagation) et l'opération de coût (pour obtenir la valeur de perte)            c,_ = sess.run([loss,optimizer], feed_dict={input_tensor: batch_x, output_tensor:batch_y})
```

Maintenant vous avez le modèle, entraîné. Pour le tester, vous devrez également créer des éléments de graphe. Nous allons mesurer la précision du modèle, donc vous devez obtenir l'index de la valeur prédite et l'index de la valeur correcte (parce que nous utilisons le codage one-hot), vérifier s'ils sont égaux et calculer la moyenne pour tout le jeu de données de test :

```
    # Tester le modèle    index_prediction = tf.argmax(prediction, 1)    index_correct = tf.argmax(output_tensor, 1)    correct_prediction = tf.equal(index_prediction, index_correct)
```

```
    # Calculer la précision    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))    total_test_data = len(newsgroups_test.target)    batch_x_test,batch_y_test = get_batch(newsgroups_test,0,total_test_data)    print("Précision :", accuracy.eval({input_tensor: batch_x_test, output_tensor: batch_y_test}))
```

```
>>> Epoch: 0001 loss= 1133.908114347    Epoch: 0002 loss= 329.093700409    Epoch: 0003 loss= 111.876660109    Epoch: 0004 loss= 72.552971845    Epoch: 0005 loss= 16.673050320    Epoch: 0006 loss= 16.481995190    Epoch: 0007 loss= 4.848220565    Epoch: 0008 loss= 0.759822878    Epoch: 0009 loss= 0.000000000    Epoch: 0010 loss= 0.079848485    Optimisation terminée !
```

```
    Précision : 0.75
```

Et c'est tout ! Vous avez créé un modèle utilisant un réseau de neurones pour classer des textes en catégories. Félicitations ! 🎉

Vous pouvez voir le notebook avec le **code final** [ici](https://github.com/dmesquita/understanding_tensorflow_nn).

Conseil : modifiez les valeurs que nous avons définies pour voir comment les changements affectent le temps d'entraînement et la précision du modèle.

Des questions ou des suggestions ? Laissez-les dans les commentaires. Oh, et merci d'avoir lu ! 😊 ✍️

Avez-vous trouvé cet article utile ? Je fais de mon mieux pour écrire un article approfondi chaque mois, vous pouvez [recevoir un email lorsque j'en publie un nouveau](https://goo.gl/forms/SLrJDrGtxgAoILkt1).

_Cela signifierait beaucoup si vous cliquez sur le 👏 et partagez avec des amis. Suivez-moi pour plus d'articles sur la Data Science et le Machine Learning._