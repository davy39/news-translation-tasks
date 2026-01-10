---
title: Comment construire un réseau de neurones à trois couches à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T20:46:04.000Z'
originalURL: https://freecodecamp.org/news/building-a-3-layer-neural-network-from-scratch-99239c4af5d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qn4w7OSeKqSOEBJIljy7xw.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire un réseau de neurones à trois couches à partir de zéro
seo_desc: 'By Daphne Cornelisse

  In this post, I will go through the steps required for building a three layer neural
  network. I’ll go through a problem and explain you the process along with the most
  important concepts along the way.

  The problem to solve

  A farm...'
---

Par Daphne Cornelisse

Dans cet article, je vais passer en revue les étapes nécessaires pour construire un **réseau de neurones à trois couches**. Je vais aborder un problème et vous expliquer le processus ainsi que les concepts les plus importants en cours de route.

#### **Le problème à résoudre**

Un agriculteur en Italie avait un problème avec sa machine d'étiquetage : elle mélangeait les étiquettes de trois cultivars de vin. Maintenant, il lui reste 178 bouteilles, et personne ne sait quel cultivar les a produites ! Pour aider cet homme, nous allons construire un **classifieur** qui reconnaît le vin en fonction de 13 attributs du vin.

![Image](https://cdn-media-1.freecodecamp.org/images/9hi4uXDfAP97lsSUoJQZmKomiT9AegFGIoZ3)

Le fait que nos données soient étiquetées (avec l'une des trois étiquettes de cultivars) en fait un problème d'**apprentissage supervisé**. Essentiellement, ce que nous voulons faire, c'est utiliser nos données d'entrée (les 178 bouteilles de vin non classées), les passer à travers notre [réseau de neurones](https://en.wikipedia.org/wiki/Artificial_neural_network), et obtenir l'étiquette correcte pour chaque cultivar de vin en sortie.

Nous allons entraîner notre algorithme à mieux prédire (y-hat) à quel cultivar appartient chaque bouteille.

Maintenant, il est temps de commencer à construire le réseau de neurones !

#### **Approche**

Construire un réseau de neurones, c'est presque comme construire une fonction très compliquée, ou assembler une recette très difficile. Au début, les ingrédients ou les étapes que vous devrez suivre peuvent sembler écrasants. Mais si vous décomposez tout et le faites étape par étape, vous vous en sortirez.

![Image](https://cdn-media-1.freecodecamp.org/images/FDWrPCgJTJbH3MPUSyT0tgG2Zi2TYczZDOAj)
_Aperçu du réseau de neurones à 3 couches, un classifieur de vin_

En bref :

* La couche d'entrée (x) se compose de 178 neurones.
* A1, la première couche, se compose de 8 neurones.
* A2, la deuxième couche, se compose de 5 neurones.
* A3, la troisième et dernière couche, se compose de 3 neurones.

#### **Étape 1 : la préparation habituelle**

Importez toutes les bibliothèques nécessaires (NumPy, skicit-learn, pandas) et le jeu de données, et définissez x et y.

```
#importation de toutes les bibliothèques et du jeu de données
```

```
import pandas as pdimport numpy as np
```

```
df = pd.read_csv('../input/W1data.csv')df.head()
```

```
# Importation des packages
```

```
# Matplotlib import matplotlibimport matplotlib.pyplot as plt
```

```
# SciKitLearn est une bibliothèque d'utilitaires d'apprentissage automatiqueimport sklearn
```

```
# Le module de jeu de données sklearn aide à générer des jeux de données
```

```
import sklearn.datasetsimport sklearn.linear_modelfrom sklearn.preprocessing import OneHotEncoderfrom sklearn.metrics import accuracy_score
```

#### Étape 2 : initialisation

Avant de pouvoir utiliser nos poids, nous devons les initialiser. Comme nous n'avons pas encore de valeurs à utiliser pour les poids, nous utilisons des valeurs aléatoires entre 0 et 1.

En Python, la fonction `random.seed` génère des "nombres aléatoires". Cependant, les nombres aléatoires ne sont pas vraiment aléatoires. Les nombres générés sont **pseudo-aléatoires**, ce qui signifie que les nombres sont générés par une formule compliquée qui les fait paraître aléatoires. Pour générer des nombres, la formule prend la valeur précédente générée comme entrée. S'il n'y a pas de valeur précédente générée, elle prend souvent l'heure comme première valeur.

C'est pourquoi nous initialisons le générateur — pour nous assurer que nous obtenons toujours **les mêmes nombres aléatoires**. Nous fournissons une valeur fixe que le générateur de nombres peut utiliser comme point de départ, qui est zéro dans ce cas.

```
np.random.seed(0)
```

#### Étape 3 : propagation avant

Il y a grossièrement deux parties dans l'entraînement d'un réseau de neurones. D'abord, vous propagez vers l'avant à travers le NN. C'est-à-dire que vous faites des "pas" vers l'avant et comparez ces résultats avec les valeurs réelles pour obtenir la différence entre votre sortie et ce qu'elle devrait être. Vous voyez essentiellement comment le NN se comporte et trouvez les erreurs.

Après avoir initialisé les poids avec un nombre pseudo-aléatoire, nous faisons un pas linéaire vers l'avant. Nous calculons cela en prenant notre entrée A0 fois le [produit scalaire](https://en.wikipedia.org/wiki/Dot_product) des poids initialisés aléatoirement plus un **biais**. Nous avons commencé avec un biais de 0. Cela est représenté comme :

![Image](https://cdn-media-1.freecodecamp.org/images/5W4PMaH25UEe40tRUDbVDC7og51z0igKwXlE)

Maintenant, nous prenons notre z1 (notre pas linéaire) et le passons à travers notre première **fonction d'activation**. Les fonctions d'activation sont très importantes dans les réseaux de neurones. Essentiellement, elles convertissent un signal d'entrée en un signal de sortie — c'est pourquoi elles sont également connues sous le nom de _fonctions de transfert_. Elles introduisent des **propriétés non linéaires** à nos fonctions en convertissant l'entrée linéaire en une sortie non linéaire, ce qui permet de représenter des fonctions plus complexes.

Il existe différents types de fonctions d'activation (expliquées en profondeur dans [cet](https://towardsdatascience.com/activation-functions-and-its-types-which-is-better-a9a5310cc8f) article). Pour ce modèle, nous avons choisi d'utiliser la fonction d'activation **tanh** pour nos deux couches cachées — A1 et A2 — qui nous donne une valeur de sortie entre -1 et 1.

Puisque c'est un problème de **classification multi-classe** (nous avons 3 étiquettes de sortie), nous utiliserons la fonction **softmax** pour la couche de sortie — A3 — car cela calculera les probabilités pour les classes en produisant une valeur entre 0 et 1.

![Image](https://cdn-media-1.freecodecamp.org/images/gYlH0AENAen9ENfZHFLUSPO55QHBxeAJAK59)
_fonction tanh_

En passant z1 à travers la fonction d'activation, nous avons créé notre première couche cachée — A1 — qui peut être utilisée comme entrée pour le calcul de l'étape linéaire suivante, z2.

![Image](https://cdn-media-1.freecodecamp.org/images/NzEFXU1tOIbpqcbBuH9b1Hp6sSjS3buGDScK)

En Python, ce processus ressemble à ceci :

```
# Ceci est la fonction de propagation avant
def forward_prop(model,a0):        # Charger les paramètres du modèle    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'],model['b3']        # Faire la première étape linéaire     z1 = a0.dot(W1) + b1        # Passer à travers la première fonction d'activation    a1 = np.tanh(z1)        # Deuxième étape linéaire    z2 = a1.dot(W2) + b2        # Passer à travers la deuxième fonction d'activation    a2 = np.tanh(z2)        # Troisième étape linéaire    z3 = a2.dot(W3) + b3        # Pour la troisième fonction d'activation linéaire, nous utilisons la fonction softmax    a3 = softmax(z3)        # Stocker tous les résultats dans ces valeurs    cache = {'a0':a0,'z1':z1,'a1':a1,'z2':z2,'a2':a2,'a3':a3,'z3':z3}    return cache
```

En fin de compte, toutes nos valeurs sont stockées dans le [cache](https://en.wikipedia.org/wiki/Cache_(computing)).

#### **Étape 4 : propagation arrière**

Après avoir propagé vers l'avant à travers notre NN, nous propagons notre gradient d'erreur vers l'arrière pour mettre à jour nos paramètres de poids. Nous connaissons notre erreur et voulons la minimiser autant que possible.

Nous faisons cela en prenant la **dérivée de la fonction d'erreur**, par rapport aux poids (W) de notre NN, en utilisant la **descente de gradient**.

Visualisons ce processus avec une analogie.

Imaginez que vous êtes parti pour une promenade dans les montagnes pendant l'après-midi. Mais maintenant, il est une heure plus tard et vous avez un peu faim, il est donc temps de rentrer à la maison. Le seul problème est qu'il fait noir et qu'il y a beaucoup d'arbres, donc vous ne pouvez voir ni votre maison ni où vous êtes. Oh, et vous avez oublié votre téléphone à la maison.

Mais ensuite, vous vous souvenez que votre maison est dans une vallée, le point le plus bas de toute la région. Donc, si vous descendez simplement la montagne pas à pas jusqu'à ce que vous ne sentiez plus de pente, en théorie, vous devriez arriver à votre maison.

Alors, vous y allez, descendant pas à pas avec soin. Maintenant, imaginez la montagne comme la fonction de perte, et vous êtes l'algorithme, essayant de trouver votre maison (c'est-à-dire le **point le plus bas**). Chaque fois que vous faites un pas vers le bas, nous mettons à jour vos coordonnées de localisation (l'algorithme **met à jour les paramètres**).

![Image](https://cdn-media-1.freecodecamp.org/images/m8Xo6IMJOekf9jdAWTq0jPwCljHlRYc3cbIx)

La fonction de perte est représentée par la montagne. Pour atteindre une perte faible, l'algorithme suit la pente — c'est-à-dire la dérivée — de la fonction de perte.

Lorsque nous descendons la montagne, nous mettons à jour nos coordonnées de localisation. L'algorithme met à jour les paramètres du réseau de neurones. En nous rapprochant du point minimum, nous approchons de notre objectif de **minimiser notre erreur**.

En réalité, la descente de gradient ressemble plus à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yYETGNqV2TLJsWtttVOKOTM89d2gro-dbweZ)

Nous commençons toujours par calculer **la pente de la fonction de perte** par rapport à z, la pente de l'étape linéaire que nous faisons.

La notation est la suivante : dv est la dérivée de la fonction de perte, par rapport à une variable v.

![Image](https://cdn-media-1.freecodecamp.org/images/GdkfhHiVWvdczRJ47nnXNduOs9Cc7VD9Jr3t)

Ensuite, nous calculons **la pente de la fonction de perte** par rapport à nos poids et biais. Parce que c'est un NN à 3 couches, nous allons itérer ce processus pour z3,2,1 + W3,2,1 et b3,2,1. Propager vers l'arrière de la couche de sortie à la couche d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/lwb8WY18okHbEZMwv933Cotyls3EQ5TG5R39)

Voici à quoi ressemble ce processus en Python :

```
# Ceci est la fonction de propagation arrière
def backward_prop(model,cache,y):
```

```
# Charger les paramètres du modèle    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'],model['W3'],model['b3']        # Charger les résultats de la propagation avant    a0,a1, a2,a3 = cache['a0'],cache['a1'],cache['a2'],cache['a3']        # Obtenir le nombre d'échantillons    m = y.shape[0]        # Calculer la dérivée de la perte par rapport à la sortie    dz3 = loss_derivative(y=y,y_hat=a3)
```

```
# Calculer la dérivée de la perte par rapport aux poids de la deuxième couche    dW3 = 1/m*(a2.T).dot(dz3) #dW2 = 1/m*(a1.T).dot(dz2)         # Calculer la dérivée de la perte par rapport au biais de la deuxième couche    db3 = 1/m*np.sum(dz3, axis=0)        # Calculer la dérivée de la perte par rapport à la première couche    dz2 = np.multiply(dz3.dot(W3.T) ,tanh_derivative(a2))        # Calculer la dérivée de la perte par rapport aux poids de la première couche    dW2 = 1/m*np.dot(a1.T, dz2)        # Calculer la dérivée de la perte par rapport au biais de la première couche    db2 = 1/m*np.sum(dz2, axis=0)        dz1 = np.multiply(dz2.dot(W2.T),tanh_derivative(a1))        dW1 = 1/m*np.dot(a0.T,dz1)        db1 = 1/m*np.sum(dz1,axis=0)        # Stocker les gradients    grads = {'dW3':dW3, 'db3':db3, 'dW2':dW2,'db2':db2,'dW1':dW1,'db1':db1}    return grads
```

#### Étape 5 : la phase d'entraînement

Pour atteindre les **poids et biais optimaux** qui nous donneront la sortie souhaitée (les trois cultivars de vin), nous devrons **entraîner** notre réseau de neurones.

Je pense que cela est très intuitif. Pour presque tout dans la vie, vous devez vous entraîner et pratiquer de nombreuses fois avant de devenir bon. De même, un réseau de neurones devra subir de nombreuses [époques](https://stackoverflow.com/questions/31155388/meaning-of-an-epoch-in-neural-networks-training) ou itérations pour nous donner une prédiction précise.

Lorsque vous apprenez quelque chose, disons que vous lisez un livre, vous avez un certain **rythme**. Ce rythme ne doit pas être trop lent, car la lecture du livre prendrait des siècles. Mais il ne doit pas non plus être trop rapide, car vous pourriez manquer une leçon très précieuse dans le livre.

De la même manière, vous devez spécifier un "**taux d'apprentissage**" pour le modèle. Le taux d'apprentissage est le multiplicateur pour mettre à jour les paramètres. Il détermine à quelle vitesse ils peuvent changer. Si le taux d'apprentissage est faible, l'entraînement prendra plus de temps. Cependant, si le taux d'apprentissage est trop élevé, nous pourrions manquer un minimum. Le taux d'apprentissage est exprimé comme :

![Image](https://cdn-media-1.freecodecamp.org/images/WbtYyr8LAqllg-qqUMKgd7QXYF7by14NX3qB)

* **:=** signifie que c'est une définition, pas une équation ou une déclaration prouvée.
* **_a_** est le taux d'apprentissage appelé _alpha_
* **dL(w)** est la dérivée de la perte totale par rapport à notre poids **w**
* **da** est la dérivée de _alpha_

Nous avons choisi un taux d'apprentissage de 0,07 après quelques expérimentations.

```
# Ce que nous retournons à la fin
model = initialise_parameters(nn_input_dim=13, nn_hdim= 5, nn_output_dim= 3)
model = train(model,X,y,learning_rate=0.07,epochs=4500,print_loss=True)
plt.plot(losses)
```

![Image](https://cdn-media-1.freecodecamp.org/images/t96e4a19Lzjs3CQcsvGfqPEXZVXzl-zL1JmC)

Enfin, voici notre graphique. Vous pouvez tracer votre précision et/ou votre perte pour obtenir un beau graphique de votre précision de prédiction. Après 4 500 époques, notre algorithme a une précision de 99,4382022472 %.

#### Résumé bref

Nous commençons par alimenter les données dans le réseau de neurones et effectuons plusieurs opérations matricielles sur ces données d'entrée, couche par couche. Pour chacune de nos trois couches, nous prenons le produit scalaire de l'entrée par les poids et ajoutons un biais. Ensuite, nous passons cette sortie à travers une **fonction d'activation** de notre choix.

La sortie de cette fonction d'activation est ensuite utilisée comme entrée pour la couche suivante pour suivre la même procédure. Ce processus est itéré trois fois puisque nous avons trois couches. Notre sortie finale est **y-hat**, qui est la **_prédiction_** de quel vin appartient à quel cultivar. C'est la fin du processus de propagation avant.

Nous calculons ensuite la **différence** entre notre prédiction (y-hat) et la sortie attendue (y) et utilisons cette valeur d'erreur pendant la rétropropagation.

Lors de la rétropropagation, nous prenons notre erreur — la différence entre notre prédiction y-hat et y — et nous la poussons mathématiquement à travers le NN dans l'autre direction. Nous apprenons de nos erreurs.

En prenant la dérivée des fonctions que nous avons utilisées lors du premier processus, nous essayons de découvrir quelle valeur nous devons donner aux **poids** afin d'obtenir la **meilleure prédiction possible**. Essentiellement, nous voulons savoir quelle est la relation entre la valeur de notre poids et l'erreur que nous obtenons en résultat.

Et après de nombreuses époques ou itérations, le NN a appris à nous donner des prédictions plus précises en adaptant ses paramètres à notre jeu de données.

![Image](https://cdn-media-1.freecodecamp.org/images/C0p7wTfuU3eBYeDP01K-TKmgvy2N-xYFW6KU)
_Aperçu de la propagation avant et arrière_

Cet article a été inspiré par le défi de la semaine 1 du [Bletchley Machine Learning](https://ai-bootcamp.org) Bootcamp qui a commencé le 7 février. Au cours des neuf prochaines semaines, je suis l'une des 50 étudiants qui passeront par les fondamentaux de l'apprentissage automatique. Chaque semaine, nous discutons d'un sujet différent et devons soumettre un défi, ce qui nécessite de vraiment comprendre les matériaux.

Si vous avez des questions ou des suggestions, faites-le [moi](https://www.linkedin.com/in/daphnecornelisse/) savoir !

Ou si vous voulez consulter le code complet, vous pouvez le trouver [ici](https://www.kaggle.com/daphnecor/week-1-3-layer-nn?scriptVersionId=2495447) sur Kaggle.

Vidéos recommandées pour une compréhension plus approfondie des réseaux de neurones :

* La série de [3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) sur les réseaux de neurones
* La série de [Siraj Raval](https://www.youtube.com/watch?v=vOppzHpvTiQ&t=274s) sur l'apprentissage profond