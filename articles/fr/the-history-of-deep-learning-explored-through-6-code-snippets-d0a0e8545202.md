---
title: L'Histoire de l'Apprentissage Profond — Explorée à Travers 6 Extraits de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T15:21:37.000Z'
originalURL: https://freecodecamp.org/news/the-history-of-deep-learning-explored-through-6-code-snippets-d0a0e8545202
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1XwEuMPRIA1eOVvmbzFebA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: L'Histoire de l'Apprentissage Profond — Explorée à Travers 6 Extraits de
  Code
seo_desc: 'By Emil Wallner

  In this article, we’ll explore six snippets of code that made deep learning what
  it is today. We’ll cover the inventors and the background to their breakthroughs.
  Each story includes simple code samples on FloydHub and GitHub to play ...'
---

Par Emil Wallner

Dans cet article, nous explorerons six extraits de code qui ont fait de l'apprentissage profond ce qu'il est aujourd'hui. Nous aborderons les inventeurs et le contexte de leurs percées. Chaque histoire inclut des exemples de code simples sur [FloydHub](https://www.floydhub.com/emilwallner/projects/deep-learning-from-scratch/) et [GitHub](https://github.com/emilwallner/Deep-Learning-From-Scratch) avec lesquels vous pouvez jouer.

Si c'est votre première rencontre avec l'apprentissage profond, je vous suggère de lire mon [Apprentissage Profond 101 pour Développeurs](https://medium.freecodecamp.org/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b).

Pour exécuter les exemples de code sur FloydHub, installez l'[outil de ligne de commande floyd](https://www.youtube.com/watch?v=byLQ9kgjTdQ&t=167s). Ensuite, clonez les [exemples de code que j'ai fournis](https://github.com/emilwallner/Deep-Learning-From-Scratch) sur votre machine locale.

**Note :** Si vous êtes nouveau sur FloydHub, vous pourriez vouloir lire la section [commencer avec FloydHub](http://blog.floydhub.com/my-first-weekend-of-deep-learning) dans mon article précédent.

Initialisez le CLI dans le dossier du projet d'exemple sur votre machine locale. Vous pouvez maintenant lancer le projet sur FloydHub avec la commande suivante :

```
floyd run --data emilwallner/datasets/mnist/1:mnist --tensorboard --mode jupyter
```

### La Méthode des Moindres Carrés

L'apprentissage profond a commencé avec un extrait de mathématiques.

Je l'ai traduit en Python :

```
# y = mx + b# m est la pente, b est l'ordonnée à l'origine
def compute_error_for_line_given_points(b, m, coordinates):
    totalError = 0
    for i in range(0, len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(coordinates))
# exemple compute_error_for_line_given_points(1, 2, [[3,6],[6,9],[12,18]])
```

Cela a été publié pour la première fois par **Adrien-Marie Legendre** en 1805. Il était un mathématicien parisien également connu pour avoir mesuré le mètre.

Il avait une obsession particulière pour prédire l'emplacement futur des comètes. Il avait les emplacements de quelques comètes passées. Il était infatigable dans sa recherche d'une méthode pour calculer leur trajectoire.

C'était vraiment l'un de ces moments où l'on jette des spaghettis sur le mur pour voir s'ils collent. Il a essayé plusieurs méthodes, puis une version a finalement retenu son attention.

Le processus de Legendre a commencé par deviner l'emplacement futur d'une comète. Ensuite, il a élevé au carré les erreurs qu'il avait commises, et enfin, il a révisé sa supposition pour réduire la somme des erreurs quadratiques. C'était le germe de la régression linéaire.

Jouez avec le code ci-dessus dans le notebook Jupyter que j'ai fourni pour vous familiariser avec. `m` est le coefficient et `b` la constante pour votre prédiction, et les `coordinates` sont les emplacements de la comète. Le but est de trouver une combinaison de `m` et `b` où l'erreur est la plus petite possible.

![Image](https://cdn-media-1.freecodecamp.org/images/ba4HRSuaGzgU79dgGjzoRkduR04LRse5T2GT)

C'est le cœur de l'apprentissage profond :

* Prendre une entrée et une sortie souhaitée
* Puis rechercher la corrélation entre les deux

### Descente de Gradient

La méthode de Legendre pour essayer manuellement de réduire le taux d'erreur était chronophage. Peter Debye était un lauréat du prix Nobel des Pays-Bas. Il a formalisé une [solution](https://www.abebooks.de/erstausgabe/N%C3%A4herungsformeln-Zylinderfunktionen-gro%C3%9Fe-Werte-Arguments-unbeschr%C3%A4nkt/5088409685/bd) pour ce processus un siècle plus tard en 1909.

Imaginons que Legendre n'avait qu'un paramètre à considérer — nous l'appellerons `X`. L'axe `Y` représente la valeur d'erreur pour chaque valeur de `X`. Legendre cherchait où `X` donne l'erreur la plus faible.

Dans cette représentation graphique, nous pouvons voir que la valeur de `X` qui minimise l'erreur `Y` est lorsque `X = 1.1`.

![Image](https://cdn-media-1.freecodecamp.org/images/aH56TazoHp7zbWeePQt5G6JUlkRdzvmUT-KJ)

Peter Debye a remarqué que la pente à gauche du minimum est négative, tandis qu'elle est positive de l'autre côté. Ainsi, si vous connaissez la valeur de la pente à n'importe quelle valeur `X`, vous pouvez guider `Y` vers son minimum.

Cela a conduit à la méthode de **descente de gradient**. Le principe est utilisé dans presque tous les modèles d'apprentissage profond.

Pour jouer avec cela, supposons que la fonction d'erreur est `Error = x⁵ - 2x³ - 2`. Pour connaître la pente de n'importe quelle valeur `X`, nous prenons sa dérivée, qui est `5x⁴ - 6x²` :

![Image](https://cdn-media-1.freecodecamp.org/images/8H7R0VES9qE9ID2uj6rpcyQUJyBotKsM0RuE)

Regardez la [vidéo de Khan Academy](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/ab-basic-diff-rules/v/derivative-properties-example) si vous avez besoin de rafraîchir vos connaissances sur les dérivées.

Les mathématiques de Debye traduites en Python :

```
current_x = 0.5 # l'algorithme commence à x=0.5
learning_rate = 0.01 # multiplicateur de la taille du pas
num_iterations = 60 # le nombre de fois où la fonction est entraînée
```

```
# la dérivée de la fonction d'erreur (x**4 = la puissance de 4 ou x^4)

def slope_at_given_x_value(x):
    return 5 * x**4 - 6 * x**2
```

```
# Déplacer X à droite ou à gauche en fonction de la pente de la fonction d'erreur

for i in range(num_iterations):
   previous_x = current_x
   current_x += -learning_rate * slope_at_given_x_value(previous_x)
   print(previous_x)
```

```
print("Le minimum local se produit à %f" % current_x)
```

L'astuce ici est le `learning_rate`. En allant dans la direction opposée de la pente, il approche le minimum. De plus, plus il se rapproche du minimum, plus la pente devient petite. Cela réduit chaque étape à mesure que la pente approche zéro.

`num_iterations` est votre temps estimé d'itérations avant d'atteindre le minimum. Jouez avec les paramètres pour avoir une intuition de la descente de gradient.

### Régression Linéaire

En combinant la méthode des moindres carrés et la descente de gradient, vous obtenez la régression linéaire. Dans les années 1950 et 1960, un groupe d'économistes expérimentaux a implémenté des versions de ces idées sur les premiers ordinateurs. La logique était implémentée sur des cartes perforées physiques — de véritables programmes logiciels faits à la main. Il fallait plusieurs jours pour préparer ces cartes perforées et jusqu'à 24 heures pour exécuter une analyse de régression à travers l'ordinateur.

Voici un exemple de régression linéaire traduit en Python pour que vous n'ayez pas à le faire sur des cartes perforées :

```
# Prix du blé/kg et le prix moyen du pain

wheat_and_bread = [[0.5,5],[0.6,5.5],[0.8,6],[1.1,6.8],[1.4,7]]
```

```

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]
```

```

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)
    return [b, m]
```

```

gradient_descent_runner(wheat_and_bread, 1, 1, 0.01, 100)
```

Cela ne devrait pas introduire quoi que ce soit de nouveau. Cependant, cela peut être un peu déroutant de fusionner la fonction d'erreur avec la descente de gradient. Exécutez le code et jouez avec ce [simulateur de régression linéaire](https://www.mladdict.com/linear-regression-simulator).

### Le Perceptron

Entrez Frank Rosenblatt — le gars qui disséquait des cerveaux de rats pendant la journée et cherchait des signes de vie extraterrestre la nuit. En 1958, il a fait la une du New York Times : « [New Navy Device Learns By Doing](http://query.nytimes.com/mem/archive-free/pdf?res=9D01E4D8173DE53BBC4053DFB1668383649EDE) » avec une machine qui imite un [neurone](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.335.3398&rep=rep1&type=pdf).

Si vous montriez à la machine de Rosenblatt 50 ensembles de deux images, l'une avec une marque à gauche et l'autre à droite, elle pouvait faire la distinction sans être pré-programmée. Le public s'est emballé avec les possibilités d'une véritable machine apprenante.

![Image](https://cdn-media-1.freecodecamp.org/images/lErc6OCToA3Nl-by3HR1DaPJPyhJCum3BnpW)

Pour chaque cycle d'entraînement, vous commencez avec des données d'entrée à gauche. Des poids aléatoires initiaux sont ajoutés à toutes les données d'entrée. Ils sont ensuite additionnés. Si la somme est négative, elle est traduite en `0`, sinon, elle est mappée en `1`.

Si la prédiction est correcte, alors rien ne se passe avec les poids dans ce cycle. Si elle est incorrecte, vous multipliez l'erreur par un taux d'apprentissage. Cela ajuste les poids en conséquence.

Exécutons le [perceptron](https://en.wikipedia.org/wiki/Perceptron) avec la logique classique OR.

![Image](https://cdn-media-1.freecodecamp.org/images/h4ffeWRX2erb6koh0V6I0U2fpF3emfKWwNJH)

La machine perceptron traduite en Python :

```
from random import choice
from numpy import array, dot, random

1_or_0 = lambda x: 0 if x < 0 else 1
training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]
weights = random.rand(3)
errors = []
learning_rate = 0.2
num_iterations = 100
```

```
for i in range(num_iterations):
    input, truth = choice(training_data)
    result = dot(weights, input)
    error = truth - 1_or_0(result)
    errors.append(error)
    weights += learning_rate * error * input
    for x, _ in training_data:
        result = dot(x, w)
        print("{}: {} -> {}".format(input[:2], result, 1_or_0(result)))
```

En 1969, Marvin Minsky et Seymour Papert ont détruit l'[idée](https://mitpress.mit.edu/books/perceptrons). À l'époque, Minsky et Papert dirigeaient le laboratoire d'IA au MIT. Ils ont écrit un livre prouvant que le perceptron ne pouvait résoudre que des problèmes linéaires. Ils ont également démystifié les affirmations sur le perceptron multicouche. Malheureusement, Frank Rosenblatt est mort dans un accident de bateau deux ans plus tard.

En 1970, un étudiant finlandais en master a découvert la [théorie](http://people.idsia.ch/~juergen/linnainmaa1970thesis.pdf) pour résoudre des problèmes non linéaires avec des perceptrons multicouches. En raison des critiques généralisées du perceptron, le financement de l'IA s'est tari pendant plus d'une décennie. Cela a été connu comme le premier hiver de l'IA.

Le pouvoir de la critique de Minsky et Papert était le problème XOR. La logique est la même que la logique OR avec une exception — lorsque vous avez deux déclarations vraies (1 & 1), vous retournez Faux (0).

![Image](https://cdn-media-1.freecodecamp.org/images/eqIi2OmxtXfTpSRkg3plKjH7QNQrKUopLp82)

Dans la logique OR, il est possible de diviser la combinaison vraie des fausses. Mais comme vous pouvez le voir, vous ne pouvez pas diviser la logique XOR avec une seule fonction linéaire.

### Réseaux de Neurones Artificiels

En 1986, plusieurs expériences ont prouvé que les réseaux de neurones pouvaient résoudre des problèmes non linéaires complexes. À l'époque, les ordinateurs étaient 10 000 fois plus rapides par rapport à quand la théorie a été développée. C'est ainsi que [Rumelhart](http://www.nature.com/nature/journal/v323/n6088/abs/323533a0.html?foxtrotcallback=true) a introduit le célèbre article :

> Nous décrivons une nouvelle procédure d'apprentissage, la rétropropagation, pour les réseaux d'unités semblables à des neurones. La procédure ajuste de manière répétée les poids des connexions dans le réseau afin de minimiser une mesure de la différence entre le vecteur de sortie réel du réseau et le vecteur de sortie souhaité. En conséquence des ajustements de poids, les unités internes « cachées » qui ne font pas partie de l'entrée ou de la sortie en viennent à représenter des caractéristiques importantes du domaine de la tâche, et les régularités de la tâche sont capturées par les interactions de ces unités. La capacité à créer de nouvelles caractéristiques utiles distingue la rétropropagation des méthodes plus simples et antérieures telles que la procédure de convergence du perceptron — **Nature** 323, 533–536 (09 octobre 1986)

Pour comprendre le cœur de cet article, nous coderons l'implémentation d'Andrew Trask de DeepMind. Ce n'est pas un extrait de code aléatoire. Il a été utilisé dans le cours d'apprentissage profond d'Andrew Karpathy à Stanford et dans le cours Udacity de Siraj Raval. Il résout le problème XOR, mettant fin au premier hiver de l'IA.

![Image](https://cdn-media-1.freecodecamp.org/images/Ri7kkXcNIMI57JA4mNK0hZfSG4t-ylF7lxPO)

Avant de plonger dans le code, jouez avec [ce simulateur](https://www.mladdict.com/neural-network-simulator) pendant une à deux heures pour saisir la logique de base. Ensuite, lisez [l'article de blog de Trask](http://iamtrask.github.io/2015/07/12/basic-python-network/).

Notez que le paramètre ajouté `[1]` dans les données `X_XOR` sont des [neurones de biais](https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks).

Ils ont le même comportement qu'une constante dans une fonction linéaire :

```
import numpy as np
```

```
X_XOR = np.array([[0,0,1], [0,1,1], [1,0,1],[1,1,1]])
y_truth = np.array([[0],[1],[1],[0]])
```

```
np.random.seed(1)
syn_0 = 2*np.random.random((3,4)) - 1
syn_1 = 2*np.random.random((4,1)) - 1
```

```

def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output
def sigmoid_output_to_derivative(output):
    return output*(1-output)
```

```

for j in range(60000):
    layer_1 = sigmoid(np.dot(X_XOR, syn_0))
    layer_2 = sigmoid(np.dot(layer_1, syn_1))
    error = layer_2 - y_truth
    layer_2_delta = error * sigmoid_output_to_derivative(layer_2)
    layer_1_error = layer_2_delta.dot(syn_1.T)
    layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
    syn_1 -= layer_1.T.dot(layer_2_delta)
    syn_0 -= X_XOR.T.dot(layer_1_delta)
    print("Output After Training: \n", layer_2)
```

La rétropropagation, la multiplication de matrices et la descente de gradient combinées peuvent être difficiles à comprendre. Les visualisations de ce processus sont souvent une simplification de ce qui se passe sous le capot. Concentrez-vous sur la compréhension de la logique derrière cela, mais ne vous inquiétez pas trop d'avoir une image mentale de cela.

De plus, regardez la [conférence](https://www.youtube.com/watch?v=i94OvYb6noo) d'Andrew Karpathy sur la rétropropagation, jouez avec [ces visualisations](http://www.benfrederickson.com/numerical-optimization/), et lisez le [chapitre](http://neuralnetworksanddeeplearning.com/chap2.html) de Michael Nielsen à ce sujet.

### Réseaux de Neurones Profonds

Les réseaux de neurones profonds sont des réseaux de neurones avec plus d'une couche entre la couche d'entrée et la couche de sortie. La notion a été [introduite](http://www.aaai.org/Papers/AAAI/1986/AAAI86-029.pdf) par Rina Dechter en 1986. Mais elle n'a pas gagné l'attention du grand public avant [2012](https://trends.google.com/trends/explore?date=all&q=deep%20learning). Cela s'est produit peu après la [victoire de Jeopardy](http://www.nytimes.com/2011/02/17/science/17jeopardy-watson.html?pagewanted=all&mcubz=0) d'IBM Watson et le [reconnaisseur de chats](https://www.youtube.com/watch?v=TK4qLwTye_s) de Google.

La structure de base des réseaux de neurones profonds est restée la même. Mais ils sont maintenant appliqués à plusieurs problèmes différents. Il y a également eu beaucoup d'améliorations en matière de régularisation.

En 1963, c'était un ensemble de fonctions mathématiques pour simplifier les [données bruyantes de la Terre](https://en.wikipedia.org/wiki/Tikhonov_regularization). Ils sont maintenant utilisés dans les réseaux de neurones pour améliorer leur capacité à [généraliser](https://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/).

Une grande partie de l'innovation est due à la puissance de calcul. Cela a amélioré les cycles d'innovation des chercheurs — ce qui prenait un supercalculateur un an pour calculer au milieu des années quatre-vingt prend une demi-seconde avec la technologie GPU d'aujourd'hui.

Le coût réduit du calcul et le développement des bibliothèques d'apprentissage profond l'ont maintenant rendu accessible au grand public. Regardons un exemple d'une pile d'apprentissage profond courante, en commençant par la couche de base :

* **GPU** > Nvidia Tesla K80. Le matériel couramment utilisé pour le traitement graphique. Comparés aux CPU, ils sont en moyenne 50 à 200 fois plus rapides pour l'apprentissage profond.
* **CUDA** > langage de programmation de bas niveau pour les GPU
* **CuDNN** > bibliothèque de Nvidia pour optimiser CUDA
* **Tensorflow** > framework d'apprentissage profond de Google sur CuDNN
* **TFlearn** > un framework frontal pour Tensorflow

Regardons la [classification d'images MNIST](https://www.tensorflow.org/get_started/mnist/beginners) des chiffres, le « Hello World » de l'apprentissage profond.

![Image](https://cdn-media-1.freecodecamp.org/images/-hAKHt0TR2Rnrcj7XYnM9KGPvvIwMhUmK483)

Implémenté dans TFlearn :

```
from __future__ import division, print_function, absolute_import
import tflearn
from tflearn.layers.core import dropout, fully_connected
from tensorflow.examples.tutorials.mnist import input_data
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
```

```
# Chargement et prétraitement des données
mnist = input_data.read_data_sets("/data/", one_hot=True)
X, Y, testX, testY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
X = X.reshape([-1, 28, 28, 1])
testX = testX.reshape([-1, 28, 28, 1])
```

```
# Construction du réseau convolutionnel
network = tflearn.input_data(shape=[None, 28, 28, 1], name='input')
network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = fully_connected(network, 128, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 256, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 10, activation='softmax')
network = regression(network, optimizer='adam', learning_rate=0.01,
                       loss='categorical_crossentropy', name='target')
```

```
# Entraînement
model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit({'input': X}, {'target': Y}, n_epoch=20,
           validation_set=({'input': testX}, {'target': testY}),
           snapshot_step=100, show_metric=True, run_id='convnet_mnist')
```

Il existe de nombreux articles expliquant le problème MNIST : [ici](https://www.youtube.com/watch?v=NMd7WjZiCzc) et [ici](https://www.oreilly.com/learning/not-another-mnist-tutorial-with-tensorflow).

### Résumons

Comme vous le voyez dans l'exemple TFlearn, la logique principale de l'apprentissage profond est toujours similaire au perceptron de Rosenblatt. Au lieu d'utiliser une fonction de Heaviside binaire, les réseaux d'aujourd'hui utilisent principalement des activations Relu (unité linéaire rectifiée).

Dans la dernière couche du réseau de neurones convolutionnel, la perte est égale à `categorical_crossentropy`. Il s'agit d'une évolution de la méthode des moindres carrés de Legendre, une régression logistique pour plusieurs catégories. L'optimiseur `adam` provient du travail de descente de gradient de Debye.

La notion de régularisation de Tikhonov est largement implémentée sous la forme de couches de dropout et de fonctions de régularisation, `L1/L2`.

Si vous voulez une meilleure intuition des réseaux de neurones et comment les implémenter, lisez mon article précédent : [**_Apprentissage Profond 101 pour Codeurs._**](https://medium.freecodecamp.org/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b)

**Merci à [Ignacio Tonoli de Maussion](https://www.freecodecamp.org/news/the-history-of-deep-learning-explored-through-6-code-snippets-d0a0e8545202/undefined)**, Brian Young, [Paal Rgd](https://www.freecodecamp.org/news/the-history-of-deep-learning-explored-through-6-code-snippets-d0a0e8545202/undefined), [Tomas Moška](https://www.freecodecamp.org/news/the-history-of-deep-learning-explored-through-6-code-snippets-d0a0e8545202/undefined), et [Charlie Harrington](https://www.freecodecamp.org/news/the-history-of-deep-learning-explored-through-6-code-snippets-d0a0e8545202/undefined) pour avoir lu les brouillons de cet article. Les sources de code sont incluses dans les notebooks Jupyter.

#### À propos d'Emil Wallner

Cela fait partie d'une série de blogs en plusieurs parties alors que j'apprends l'apprentissage profond. J'ai passé une décennie à explorer l'apprentissage humain. J'ai travaillé pour l'école de commerce d'Oxford, investi dans des startups éducatives et construit une entreprise de technologie éducative. L'année dernière, je me suis inscrit à [Ecole 42](https://twitter.com/paulg/status/847844863727087616) pour appliquer mes connaissances de l'apprentissage humain à l'apprentissage machine.

Vous pouvez suivre mon parcours d'apprentissage sur [Twitter](https://twitter.com/EmilWallner). Si vous avez des questions ou des suggestions, veuillez laisser un commentaire ci-dessous ou me contacter sur [M](https://medium.com/@emilwallner)edium.

Cela a été publié pour la première fois en tant qu'article communautaire sur le [blog de Floydhub](https://blog.floydhub.com/coding-the-history-of-deep-learning).