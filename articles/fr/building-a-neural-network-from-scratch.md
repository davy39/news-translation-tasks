---
title: Comment construire un réseau de neurones à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T14:32:09.000Z'
originalURL: https://freecodecamp.org/news/building-a-neural-network-from-scratch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fff740569d1a4ca4600.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: Comment construire un réseau de neurones à partir de zéro
seo_desc: 'By Aditya

  Neural Networks are like the workhorses of Deep learning. With enough data and computational
  power, they can be used to solve most of the problems in deep learning. It is very
  easy to use a Python or R library to create a neural network and...'
---

Par Aditya

Les réseaux de neurones sont comme les chevaux de trait de l'apprentissage profond. Avec suffisamment de données et de puissance de calcul, ils peuvent être utilisés pour résoudre la plupart des problèmes en apprententissage profond. Il est très facile d'utiliser une bibliothèque Python ou R pour créer un réseau de neurones et l'entraîner sur n'importe quel jeu de données et obtenir une grande précision.

Nous pouvons traiter les réseaux de neurones comme une simple boîte noire et les utiliser sans aucune difficulté. Mais même si cela semble très facile, il est beaucoup plus excitant d'apprendre ce qui se cache derrière ces algorithmes et comment ils fonctionnent.

Dans cet article, nous allons entrer dans certains détails de la construction d'un réseau de neurones. Je vais utiliser Python pour écrire le code du réseau. Je vais également utiliser la bibliothèque numpy de Python pour effectuer des calculs numériques. Je vais essayer d'éviter certains détails mathématiques compliqués, mais je vais faire référence à quelques ressources brillantes à la fin si vous voulez en savoir plus à ce sujet.

Alors, commençons.

## Idée

Avant de commencer à écrire du code pour notre réseau de neurones, attendons et comprenons exactement ce qu'est un réseau de neurones.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/nn.png)
_[Source](https://miro.medium.com/max/980/1*oc1gaCFvgWXq_gHQFM63UQ.png)_

Sur l'image ci-dessus, vous pouvez voir un diagramme très simple d'un réseau de neurones. Il a des cercles colorés connectés les uns aux autres avec des flèches pointant dans une direction particulière. Ces cercles colorés sont parfois appelés _neurones_.

Ces _neurones_ ne sont rien d'autre que des fonctions mathématiques qui, lorsqu'on leur donne une certaine _entrée_, génèrent une _sortie_. La _sortie_ des _neurones_ dépend de l'_entrée_ et des _paramètres_ des _neurones_. Nous pouvons mettre à jour ces _paramètres_ pour obtenir une valeur souhaitée du réseau.

Chacun de ces _neurones_ est défini en utilisant la _fonction sigmoïde_. Une _fonction sigmoïde_ donne une sortie entre zéro et un pour chaque entrée qu'elle reçoit. Ces unités sigmoïdes sont connectées les unes aux autres pour former un réseau de neurones.

Par connexion ici, nous entendons que la sortie d'une couche d'unités sigmoïdes est donnée comme entrée à chaque unité sigmoïde de la couche suivante. De cette manière, notre réseau de neurones produit une sortie pour toute entrée donnée. Le processus continue jusqu'à ce que nous ayons atteint la couche finale. La couche finale génère sa sortie.

Ce processus d'un réseau de neurones générant une _sortie_ pour une _entrée_ donnée est la _propagation avant_. La sortie de la couche finale est également appelée la _prédiction_ du réseau de neurones. Plus tard dans cet article, nous discuterons de la manière dont nous _évaluons les prédictions_. Ces évaluations peuvent être utilisées pour dire si notre réseau de neurones a besoin d'amélioration ou non.

Juste après que la couche finale génère sa sortie, nous calculons la _fonction de coût_. La fonction de coût calcule à quel point notre réseau de neurones est éloigné de faire ses prédictions souhaitées. La valeur de la fonction de coût montre la différence entre la _valeur prédite_ et la _valeur réelle_.

Notre objectif ici est de minimiser la valeur de la _fonction de coût_. Le processus de minimisation de la fonction de coût nécessite un algorithme qui peut mettre à jour les valeurs des _paramètres_ dans le réseau de telle manière que la fonction de coût atteigne sa _valeur minimale_.

Des algorithmes tels que la _descente de gradient_ et la _descente de gradient stochastique_ sont utilisés pour mettre à jour les _paramètres_ du réseau de neurones. Ces algorithmes mettent à jour les valeurs des poids et des biais de chaque couche dans le réseau en fonction de la manière dont cela affectera la minimisation de la fonction de coût. L'effet sur la minimisation de la fonction de coût par rapport à chacun des poids et des biais de chacun des neurones d'entrée dans le réseau est calculé par la _rétropropagation_.

## Code

Donc, nous connaissons maintenant les principales idées derrière les réseaux de neurones. Commençons à implémenter ces idées en code. Nous allons commencer par importer toutes les bibliothèques requises.

```python3
import numpy as np
import matplotlib.pyplot as plt
```

Comme je l'ai mentionné, nous n'allons pas utiliser de bibliothèques d'apprentissage profond. Donc, nous utiliserons principalement numpy pour effectuer des calculs mathématiques efficacement.

La première étape dans la construction de notre réseau de neurones sera d'initialiser les paramètres. Nous devons initialiser deux paramètres pour chacun des neurones dans chaque couche : 1) _Poids_ et 2) _Biais_.

Ces poids et biais sont déclarés sous forme _vectorisée_. Cela signifie qu'au lieu d'initialiser les poids et les biais pour chaque neurone individuel dans chaque couche, nous allons créer un vecteur (ou une matrice) pour les poids et un autre pour les biais, pour chaque couche.

Ces vecteurs de _poids_ et de _biais_ seront combinés avec l'entrée de la couche. Ensuite, nous appliquerons la fonction sigmoïde sur cette combinaison et enverrons cela comme entrée à la couche suivante.

**layer_dims** contient les dimensions de chaque couche. Nous allons passer ces dimensions de couches à la fonction **init_parms** qui les utilisera pour initialiser les paramètres. Ces paramètres seront stockés dans un dictionnaire appelé **params**. Donc dans le dictionnaire params, **params['W1']** représentera la matrice de poids pour la couche 1.

```
def init_params(layer_dims):
    np.random.seed(3)
    params = {}
    L = len(layer_dims)
    
    for l in range(1, L):
        params['W'+str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1])*0.01
        params['b'+str(l)] = np.zeros((layer_dims[l], 1))
        
    return params
```

Super ! Nous avons initialisé les poids et les biais et maintenant nous allons définir la _fonction sigmoïde_. Elle calculera la valeur de la fonction sigmoïde pour toute valeur donnée de **Z** et stockera également cette valeur comme cache. Nous allons stocker les valeurs de cache car nous en avons besoin pour implémenter la rétropropagation. Le **Z** ici est l'_hypothèse linéaire_.

Notez que la fonction sigmoïde fait partie de la classe des _fonctions d'activation_ dans la terminologie des réseaux de neurones. Le travail d'une _fonction d'activation_ est de façonner la sortie d'un neurone.

Par exemple, la fonction sigmoïde prend une entrée avec des valeurs discrètes et donne une valeur qui se situe entre zéro et un. Son but est de convertir les sorties linéaires en sorties non linéaires. Il existe différents types de _fonctions d'activation_ qui peuvent être utilisées pour de meilleures performances, mais nous allons nous en tenir à la sigmoïde pour des raisons de simplicité.

```
# Z (hypothèse linéaire) - Z = W*X + b , 
# W - matrice de poids, b- vecteur de biais, X- Entrée 

def sigmoid(Z):
	A = 1/(1+np.exp(np.dot(-1, Z)))
    cache = (Z)
    
    return A, cache
```

Maintenant, commençons à écrire le code pour la propagation avant. Nous avons discuté précédemment que la _propagation avant_ prendra les valeurs de la couche précédente et les donnera comme entrée à la couche suivante. La fonction ci-dessous prendra les _données d'entraînement_ et les _paramètres_ comme entrées et générera une sortie pour une couche, puis elle alimentera cette sortie à la couche suivante, et ainsi de suite.

```
def forward_prop(X, params):
    
    A = X # entrée de la première couche c'est-à-dire les données d'entraînement
    caches = []
    L = len(params)//2
    for l in range(1, L+1):
        A_prev = A
        
        # Hypothèse linéaire
        Z = np.dot(params['W'+str(l)], A_prev) + params['b'+str(l)] 
        
        # Stockage du cache linéaire
        linear_cache = (A_prev, params['W'+str(l)], params['b'+str(l)]) 
        
        # Application de la sigmoïde sur l'hypothèse linéaire
        A, activation_cache = sigmoid(Z) 
        
         # stockage des caches linéaire et d'activation
        cache = (linear_cache, activation_cache)
        caches.append(cache)
    
    return A, caches
```

**A_prev** est l'entrée de la première couche. Nous allons boucler à travers toutes les couches du réseau et calculer l'hypothèse linéaire. Après cela, il prendra la valeur de **Z** (hypothèse linéaire) et la donnera à la fonction d'activation sigmoïde. Les valeurs de cache sont stockées en cours de route et s'accumulent dans **caches**. Enfin, la fonction retournera la valeur générée et le cache stocké.

Définissons maintenant notre fonction de coût.

```
def cost_function(A, Y):
    m = Y.shape[1]
    
    cost = (-1/m)*(np.dot(np.log(A), Y.T) + np.dot(log(1-A), 1-Y.T)) 
    
    return cost
```

À mesure que la valeur de la fonction de coût diminue, la performance de notre modèle devient meilleure. La valeur de la fonction de coût peut être minimisée en mettant à jour les valeurs des paramètres de chacune des couches dans le réseau de neurones. Des algorithmes tels que la _Descente de Gradient_ sont utilisés pour mettre à jour ces valeurs de manière à minimiser la fonction de coût.

La Descente de Gradient met à jour les valeurs à l'aide de certains termes de mise à jour. Ces termes de mise à jour appelés _gradients_ sont calculés en utilisant la rétropropagation. Les valeurs de gradient sont calculées pour chaque neurone dans le réseau et représentent le changement dans la sortie finale par rapport au changement dans les paramètres de ce neurone particulier.

```
def one_layer_backward(dA, cache):
    linear_cache, activation_cache = cache
    
    Z = activation_cache
    dZ = dA*sigmoid(Z)*(1-sigmoid(Z)) # La dérivée de la fonction sigmoïde
    
    A_prev, W, b = linear_cache
    m = A_prev.shape[1]
    
    dW = (1/m)*np.dot(dZ, A_prev.T)
    db = (1/m)*np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)
    
    return dA_prev, dW, db
```

Le code ci-dessus exécute l'étape de rétropropagation pour une seule couche. Il calcule les valeurs de gradient pour les unités sigmoïdes d'une couche en utilisant les valeurs de cache que nous avons stockées précédemment. Dans le cache d'activation, nous avons stocké la valeur de **Z** pour cette couche. En utilisant cette valeur, nous allons calculer **dZ**, qui est la dérivée de la fonction de coût par rapport à la sortie linéaire du neurone donné.

Une fois que nous avons calculé tout cela, nous pouvons calculer **dW**, **db** et **dA_prev**, qui sont les dérivées de la fonction de coût par rapport aux poids, aux biais et à l'activation précédente respectivement. J'ai directement utilisé les formules dans le code. Si vous n'êtes pas familier avec le calcul, cela peut sembler trop compliqué au début. Mais pour l'instant, pensez-y comme à n'importe quelle autre formule mathématique.

Après cela, nous allons utiliser ce code pour implémenter la rétropropagation pour l'ensemble du réseau de neurones. La fonction **backprop** implémente le code pour cela. Ici, nous avons créé un dictionnaire pour mapper les gradients à chaque couche. Nous allons parcourir le modèle dans une direction inverse et calculer le gradient.

```
def backprop(AL, Y, caches):
    grads = {}
    L = len(caches)
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)
    
    dAL = -(np.divide(Y, AL) - np.divide(1-Y, 1-AL))
    
    current_cache = caches[L-1]
    grads['dA'+str(L-1)], grads['dW'+str(L-1)], grads['db'+str(L-1)] = one_layer_backward(dAL, current_cache)
    
    for l in reversed(range(L-1)):
        
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = one_layer_backward(grads["dA" + str(l+1)], current_cache)
        grads["dA" + str(l)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp
        
    return grads
```

Une fois que nous avons parcouru toutes les couches et calculé les gradients, nous allons stocker ces valeurs dans le dictionnaire **grads** et le retourner.

Enfin, en utilisant ces valeurs de gradient, nous allons mettre à jour les paramètres pour chaque couche. La fonction **update_parameters** parcourt toutes les couches et met à jour les paramètres et les retourne.

```
def update_parameters(parameters, grads, learning_rate):
    L = len(parameters) // 2
    
    for l in range(L):
        parameters['W'+str(l+1)] = parameters['W'+str(l+1)] -learning_rate*grads['W'+str(l+1)]
        parameters['b'+str(l+1)] = parameters['b'+str(l+1)] -  learning_rate*grads['b'+str(l+1)]
        
    return parameters
```

Enfin, il est temps de tout rassembler. Nous allons créer une fonction appelée **train** pour entraîner notre réseau de neurones.

```
def train(X, Y, layer_dims, epochs, lr):
    params = init_params(layer_dims)
    cost_history = []
    
    for i in range(epochs):
        Y_hat, caches = forward_prop(X, params)
        cost = cost_function(Y_hat, Y)
        cost_history.append(cost)
        grads = backprop(Y_hat, Y, caches)
        
        params = update_parameters(params, grads, lr)
        
        
    return params, cost_history
```

Cette fonction passera par toutes les fonctions étape par étape pour un nombre donné d'_époques_. Après avoir terminé cela, elle retournera les paramètres mis à jour finaux et l'historique des coûts. L'historique des coûts peut être utilisé pour évaluer la performance de votre architecture de réseau.

## Conclusion

Si vous lisez encore ceci, merci ! Cet article était un peu compliqué, donc ce que je vous suggère de faire est d'essayer de jouer avec le code. Vous pourriez en tirer quelques idées supplémentaires et peut-être trouver quelques erreurs dans le code aussi. Si c'est le cas ou si vous avez des questions ou les deux, n'hésitez pas à me contacter sur [twitter](https://twitter.com/aditya_dehal). Je ferai de mon mieux pour vous aider.

## Ressources

* [Liste de lecture sur les réseaux de neurones](https://youtu.be/aircAruvnKk) - par 3Blue1Brown
* [Réseaux de neurones et apprentissage profond](http://neuralnetworksanddeeplearning.com/chap1.html) - par Michael A. Nielsen
* [Descente de gradient et descente de gradient stochastique](https://www.quora.com/Whats-the-difference-between-gradient-descent-and-stochastic-gradient-descent/answer/Sebastian-Raschka-1)