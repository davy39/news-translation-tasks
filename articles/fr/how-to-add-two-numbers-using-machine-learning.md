---
title: Comment additionner deux nombres - La méthode Machine Learning
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-08-01T19:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-two-numbers-using-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Sum-of-2-numbers-using-ML
seo_title: Comment additionner deux nombres - La méthode Machine Learning
---

Banner.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_title: null
seo_desc: "Dans le monde du machine learning, nous rencontrons souvent des problèmes complexes,\
  \ de la reconnaissance d'images au traitement du langage naturel. \nMais faisons un pas\
  \ en arrière et explorons quelque chose de plus élémentaire mais tout aussi intrigant : l'addition ! Oui,\
  \ vous avez bien lu..."
---

Dans le monde du machine learning, nous rencontrons souvent des problèmes complexes, de la reconnaissance d'images au traitement du langage naturel. 

Mais faisons un pas en arrière et explorons quelque chose de plus élémentaire mais tout aussi intrigant : l'addition ! Oui, vous avez bien lu – l'addition. 

Dans ce tutoriel, nous allons construire un réseau de neurones capable d'apprendre l'art d'additionner deux nombres.

Une petite note avant de commencer : je ne recommande pas d'utiliser le machine learning pour trouver la somme de deux nombres en pratique. J'ai essayé cela par curiosité lorsque j'ai commencé à apprendre le machine learning. Et je souhaitais simplement partager cela avec vous tous pour rendre l'apprentissage amusant. 

Vous pouvez utiliser ce tutoriel comme une sorte de guide de démarrage dans votre parcours en machine learning. Parfois, il est difficile de trouver de bons ensembles de données propres en tant qu'ingénieur débutant en machine learning. Cela rend plus difficile le travail et l'apprentissage des problèmes de machine learning si vous n'avez pas un ensemble de données solide.

Mais ne vous inquiétez pas – dans ce tutoriel, nous allons créer notre propre ensemble de données (paires de nombres à additionner) et nettoyer les données. Cela vous donnera un bon ensemble de données que vous pourrez utiliser dans vos propres problèmes et avec vos propres modèles. 

Très bien, avant de plonger, révisons quelques bases du machine learning et du deep learning.

## Bases du Deep Learning

Il y a quelques termes de machine learning et de deep learning que je vais utiliser dans l'exercice. Il est donc préférable de les comprendre à un niveau élevé en quelques phrases avant de plonger.

### Qu'est-ce qu'un réseau de neurones ?

Un réseau de neurones est un modèle computationnel inspiré de la structure et des fonctions du cerveau humain. Il se compose de nœuds interconnectés (neurones) organisés en couches. Les réseaux de neurones sont entraînés sur des données pour apprendre des motifs et faire des prédictions.

### Qu'est-ce qu'une fonction d'activation ?

Une fonction d'activation est appliquée à la sortie d'un neurone pour introduire de la non-linéarité. Elle permet aux réseaux de neurones d'apprendre des relations complexes dans les données. Les fonctions d'activation courantes incluent ReLU (Unité Linéaire Rectifiée) et Sigmoid.

### Qu'est-ce qu'une fonction de perte ?

Une fonction de perte est une mesure de la correspondance entre les prédictions d'un modèle et les vraies valeurs cibles. Pendant l'entraînement, le but est de minimiser la fonction de perte, guidant le modèle à faire de meilleures prédictions.

### Qu'est-ce que la descente de gradient ?

La descente de gradient est un algorithme d'optimisation utilisé pour minimiser la fonction de perte. Il ajuste les paramètres du modèle de manière itérative dans la direction de la descente la plus raide, guidé par les gradients de la fonction de perte par rapport aux paramètres.

### Qu'est-ce que la rétropropagation ?

La rétropropagation est un algorithme fondamental utilisé dans l'entraînement des réseaux de neurones. Il calcule les gradients de la fonction de perte par rapport à chaque paramètre du modèle et les propage en arrière à travers le réseau pour mettre à jour les poids pendant la descente de gradient.

### Qu'est-ce que la taille de lot ?

La taille de lot représente le nombre d'échantillons d'entraînement utilisés dans un passage avant/arrière pendant l'entraînement. Des tailles de lot plus grandes peuvent accélérer l'entraînement mais nécessitent plus de mémoire.

### Qu'est-ce qu'une époque ?

Une époque représente une itération complète à travers l'ensemble du jeu de données d'entraînement pendant l'entraînement.

Ce ne sont que quelques-uns des nombreux termes que vous rencontrerez dans le vaste domaine du machine learning et du deep learning. Mais ils sont suffisants pour vous aider à comprendre l'exercice suivant.

## Prérequis

Voici une liste de contrôle pour vous aider à commencer avec les bases du machine learning. Avant de suivre ce tutoriel, vous devriez les avoir installés et prêts (mais ce n'est pas obligatoire).

1. Installez Anaconda (il est fourni avec de nombreuses bibliothèques de machine learning par défaut). 
2. Créez un environnement dans Anaconda : cela est fortement recommandé, car seul l'environnement créé sera affecté si quelque chose ne va pas. Votre installation complète d'Anaconda ne sera pas affectée.
3. Assurez-vous d'avoir un bon éditeur de code/IDE comme Visual Studio Code.
4. Installez Keras (cette exigence est spécifique à cet exercice).

Avez-vous tous ces éléments prêts ? J'espère que vous êtes excité. Plongeons dans notre exercice.

## Comment additionner deux nombres en utilisant le Machine Learning

### Créer un dossier et un fichier

Créez un nouveau dossier avec n'importe quel nom. Naviguez dans le dossier et créez un fichier nommé `addition.ipynb`. Ouvrez le dossier dans Visual Studio Code ou tout autre IDE que vous utilisez.

Ensuite, créez des blocs de code pour chacune des sections suivantes en appuyant sur le bouton "+ Code" en haut à gauche dans VS Code.

### Importer les bibliothèques

Importez les bibliothèques `numpy` et `keras` avec ces commandes :

```py
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
```

### Préparer les données

La précision de vos modèles de machine learning dépend des données avec lesquelles vous entraînez votre modèle. 

Pour créer les données d'addition dont nous aurons besoin ici, créons des paires de 1000 nombres aléatoires qui seront considérés comme notre entrée. La sortie sera la somme des nombres dans chaque paire.

```py
num_samples = 1000
X_train = np.random.rand(num_samples, 2)
y_train = X_train[:, 0] + X_train[:, 1]
```

### Définir le réseau de neurones

Construisons un réseau de neurones avec deux couches d'entrée – une couche cachée avec 8 neurones, et une couche de sortie avec un seul neurone. Nous utiliserons la fonction d'activation "relu".

```py
model = Sequential()
model.add(Dense(8, input_shape=(2,), activation='relu'))
model.add(Dense(1))
```

### Compiler le modèle

Compilez le modèle en utilisant le MSE (Erreur Quadratique Moyenne) comme fonction de perte et l'optimiseur Adam.

```py
model.compile(loss='mse', optimizer='adam')
```

### Entraîner le modèle

Entraînez le modèle pendant 100 époques, avec une taille de lot de 32.

```py
batch_size = 32
epochs = 100
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)
```

Cela peut prendre quelques secondes selon la configuration de votre CPU. Cela a pris environ 10 à 15 secondes sur mon ordinateur portable pour se terminer.

### Tester le modèle

Maintenant que nous avons entraîné notre modèle, testons-le avec quelques entrées personnalisées. J'ai pris deux entrées mais vous pouvez tester votre modèle avec n'importe quel nombre d'entrées.

```python
test_input = np.array([[1, 2], [0.3, 0.4]])
predicted_sum = model.predict(test_input)
```

### Afficher les valeurs

La prédiction est terminée. Voyons si elles sont correctes en affichant les valeurs prédites :

```python
print("Sommes prédites :")
print(predicted_sum)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-187.png)
_Exemple de sortie des valeurs prédites_

Assez proche, n'est-ce pas ?

## Conclusion

Dans ce tutoriel, vous avez appris comment construire un réseau de neurones pour effectuer des additions.

Si vous êtes curieux, vous pouvez essayer de construire un réseau de neurones pour effectuer des soustractions juste pour le plaisir. Bonne chance :)

J'espère que vous avez apprécié la lecture de cet article. Si vous souhaitez en apprendre davantage sur l'intelligence artificielle / le machine learning / le deep learning, abonnez-vous à mes articles en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_addition_nn) qui contient une liste consolidée de tous mes blogs.