---
title: Comment fonctionne la rétropropagation, et comment utiliser Python pour construire
  un réseau de neurones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-07T15:43:27.000Z'
originalURL: https://freecodecamp.org/news/build-a-flexible-neural-network-with-backpropagation-in-python-acffeb7846d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*MARKxJzRD2-8X6NZ.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Comment fonctionne la rétropropagation, et comment utiliser Python pour
  construire un réseau de neurones
seo_desc: 'By Samay Shamdasani

  Neural networks can be intimidating, especially for people new to machine learning.
  However, this tutorial will break down how exactly a neural network works and you
  will have a working flexible neural network by the end. Let’s ge...'
---

Par Samay Shamdasani

Les réseaux de neurones peuvent être intimidants, surtout pour les personnes nouvelles en apprentissage automatique. Cependant, ce tutoriel va décomposer comment exactement un réseau de neurones fonctionne et vous aurez un réseau de neurones flexible et fonctionnel à la fin. Commençons !

### Comprendre le processus

Avec environ 100 milliards de neurones, le cerveau humain traite les données à des vitesses [aussi rapides que 268 mph](http://discovermagazine.com/2011/mar/10-numbers-the-nervous-system)! En essence, un réseau de neurones est une collection de **neurones** connectés par des **synapses**.

Cette collection est organisée en trois couches principales : la couche d'entrée, la couche cachée et la couche de sortie.

Vous pouvez avoir plusieurs couches cachées, ce qui est là où le terme **apprentissage profond** entre en jeu. Dans un réseau de neurones artificiel, il y a plusieurs entrées, qui sont appelées **caractéristiques**, qui produisent au moins une sortie — qui est appelée une **étiquette**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*68NqSS6j-Ix0TkBgp103AQ.png)
_Image via Kabir Shah_

Dans le dessin ci-dessus, les cercles représentent les neurones tandis que les lignes représentent les synapses.

Le rôle d'une synapse est de prendre et multiplier les entrées et les **poids**.

Vous pouvez penser aux poids comme à la « force » de la connexion entre les neurones. Les poids définissent principalement la sortie d'un réseau de neurones. Cependant, ils sont très flexibles. Ensuite, une fonction d'activation est appliquée pour retourner une sortie.

Voici un bref aperçu de comment un simple réseau de neurones feedforward fonctionne :

1. Prendre les entrées sous forme de matrice (tableau 2D de nombres)
2. Multiplier les entrées par un ensemble de poids (cela est fait par [multiplication de matrices](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro), aka prendre le 'produit scalaire')
3. Appliquer une fonction d'activation
4. Retourner une sortie
5. L'erreur est calculée en prenant la différence entre la sortie souhaitée du modèle et la sortie prédite. C'est un processus appelé descente de gradient, que nous pouvons utiliser pour altérer les poids.
6. Les poids sont ensuite ajustés, selon l'erreur trouvée à l'étape 5.
7. Pour entraîner, ce processus est répété 1 000+ fois. Plus les données sont entraînées, plus nos sorties seront précises.

À leur cœur, les réseaux de neurones sont simples.

Ils effectuent simplement une multiplication de matrices avec l'entrée et les poids, et appliquent une fonction d'activation.

Lorsque les poids sont ajustés via le gradient de la fonction de perte, le réseau s'adapte aux changements pour produire des sorties plus précises.

Notre réseau de neurones modélisera une seule couche cachée avec trois entrées et une sortie. Dans le réseau, nous prédirons le score de notre examen basé sur les entrées du nombre d'heures étudiées et du nombre d'heures dormies la veille. La sortie est le 'score du test'.

Voici nos données d'exemple sur lesquelles nous entraînerons notre réseau de neurones :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jK4Ct8-EG913GkKZh0R1yg.png)
_Exemple original via [Welch Labs](https://www.youtube.com/watch?v=UJwK6jAStmg" rel="noopener" target="_blank" title=")_

Comme vous l'avez peut-être remarqué, le `?` dans ce cas représente ce que nous voulons que notre réseau de neurones prédise. Dans ce cas, nous prédisons le score du test de quelqu'un qui a étudié pendant quatre heures et dormi pendant huit heures basé sur ses performances précédentes.

### Propagation avant

Commençons à coder ce bad boy ! Ouvrez un nouveau fichier Python. Vous voudrez importer `numpy` car il nous aidera avec certains calculs.

Tout d'abord, importons nos données sous forme de tableaux numpy en utilisant `np.array`. Nous voudrons également normaliser nos unités car nos entrées sont en heures, mais notre sortie est un score de test de 0 à 100. Par conséquent, nous devons mettre à l'échelle nos données en divisant par la valeur maximale pour chaque variable.

Ensuite, définissons une `class` Python et écrivons une fonction `init` où nous spécifierons nos paramètres tels que les couches d'entrée, cachées et de sortie.

Il est temps pour notre premier calcul. Rappelez-vous que nos synapses effectuent un [produit scalaire](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro), ou multiplication de matrices de l'entrée et du poids. Notez que les poids sont générés aléatoirement et entre 0 et 1.

### Les calculs derrière notre réseau

Dans l'ensemble de données, nos données d'entrée, `X`, sont une matrice 3x2. Nos données de sortie, `y`, sont une matrice 3x1. Chaque élément de la matrice `X` doit être multiplié par un poids correspondant puis additionné avec tous les autres résultats pour chaque neurone de la couche cachée. Voici comment le premier élément de données d'entrée (2 heures d'étude et 9 heures de sommeil) calculerait une sortie dans le réseau :

![Image](https://cdn-media-1.freecodecamp.org/images/0*o8Rb-ztx6G4pjzgu.png)
_C'est tout ce qu'un réseau de neurones fait réellement !_

Cette image décompose ce que notre réseau de neurones fait réellement pour produire une sortie. Tout d'abord, les produits des poids générés aléatoirement (.2, .6, .1, .8, .3, .7) sur chaque synapse et les entrées correspondantes sont additionnés pour arriver aux premières valeurs de la couche cachée. Ces sommes sont en petite police car elles ne sont pas les valeurs finales pour la couche cachée.

Pour obtenir la valeur finale de la couche cachée, nous devons appliquer la [fonction d'activation](https://en.wikipedia.org/wiki/Activation_function).

Le rôle d'une fonction d'activation est d'introduire de la [non-linéarité](https://en.wikipedia.org/wiki/Nonlinear_system). Un avantage de cela est que la sortie est mappée d'une plage de 0 à 1, ce qui facilite l'ajustement des poids à l'avenir.

Il existe de nombreuses fonctions d'activation, pour de nombreux cas d'utilisation différents. Dans cet exemple, nous nous en tiendrons à l'une des plus populaires — la fonction sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PLWbjYTrSSy_fFhR.png)

Maintenant, nous devons utiliser à nouveau la multiplication de matrices, avec un autre ensemble de poids aléatoires, pour calculer notre valeur de couche de sortie.

Enfin, pour normaliser la sortie, nous appliquons simplement à nouveau la fonction d'activation.

Et voilà ! Théoriquement, avec ces poids, notre réseau de neurones calculera `.85` comme notre score de test ! Cependant, notre cible était `.92`. Notre résultat n'était pas mauvais, il n'est simplement pas le meilleur possible. Nous avons simplement eu un peu de chance lorsque j'ai choisi les poids aléatoires pour cet exemple.

Comment entraîner notre modèle pour apprendre ? Eh bien, nous le découvrirons très bientôt. Pour l'instant, continuons à coder notre réseau.

Si vous êtes toujours confus, je vous recommande vivement de consulter [cette](https://www.youtube.com/watch?v=UJwK6jAStmg) vidéo informative qui explique la structure d'un réseau de neurones avec le même exemple.

### Implémentation des calculs

Maintenant, générons nos poids aléatoirement en utilisant `np.random.randn()`. Rappelez-vous, nous aurons besoin de deux ensembles de poids. Un pour aller de l'entrée à la couche cachée, et l'autre pour aller de la couche cachée à la couche de sortie.

Une fois que nous avons toutes les variables configurées, nous sommes prêts à écrire notre fonction de propagation `forward`. Passons notre entrée, `X`, et dans cet exemple, nous pouvons utiliser la variable `z` pour simuler l'activité entre les couches d'entrée et de sortie.

Comme expliqué, nous devons prendre un produit scalaire des entrées et des poids, appliquer une fonction d'activation, prendre un autre produit scalaire de la couche cachée et du deuxième ensemble de poids, et enfin appliquer une fonction d'activation finale pour recevoir notre sortie :

Enfin, nous devons définir notre fonction sigmoïde :

Et voilà ! Un réseau de neurones (non entraîné) capable de produire une sortie.

Comme vous l'avez peut-être remarqué, nous devons entraîner notre réseau pour calculer des résultats plus précis.

### Rétropropagation — l'« apprentissage » de notre réseau

Puisque nous avons un ensemble aléatoire de poids, nous devons les altérer pour que nos entrées soient égales aux sorties correspondantes de notre ensemble de données. Cela se fait par une méthode appelée rétropropagation.

La rétropropagation fonctionne en utilisant une fonction de **perte** pour calculer à quel point le réseau était éloigné de la sortie cible.

#### Calcul de l'erreur

Une façon de représenter la fonction de perte est d'utiliser la fonction de **perte quadratique moyenne** :

![Image](https://cdn-media-1.freecodecamp.org/images/0*EdvxSgRqmgZQTfLM.png)

Dans cette fonction, `o` est notre sortie prédite, et `y` est notre sortie réelle. Maintenant que nous avons la fonction de perte, notre objectif est de la rapprocher le plus possible de 0. Cela signifie que nous devrons avoir presque aucune perte. Lorsque nous entraînons notre réseau, tout ce que nous faisons est de minimiser la perte.

Pour déterminer dans quelle direction altérer les poids, nous devons trouver le taux de changement de notre perte par rapport à nos poids. En d'autres termes, nous devons utiliser la dérivée de la fonction de perte pour comprendre comment les poids affectent l'entrée.

Dans ce cas, nous utiliserons une dérivée partielle pour nous permettre de prendre en compte une autre variable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vx-4e1tj4okQHSw1LYtBxA.png)
_Image via Kabir Shah_

Cette méthode est connue sous le nom de **descente de gradient**. En sachant dans quelle direction altérer nos poids, nos sorties ne peuvent que devenir plus précises.

Voici comment nous calculerons le changement incrémental de nos poids :

1. Trouver la **marge d'erreur** de la couche de sortie (o) en prenant la différence entre la sortie prédite et la sortie réelle (y)
2. Appliquer la [dérivée](https://en.wikipedia.org/wiki/Derivative) de notre fonction d'activation sigmoïde à l'erreur de la couche de sortie. Nous appelons ce résultat la **somme delta de sortie**.
3. Utiliser la somme delta de sortie de l'erreur de la couche de sortie pour déterminer combien notre couche z² (cachée) a contribué à l'erreur de sortie en effectuant un produit scalaire avec notre deuxième matrice de poids. Nous pouvons appeler cela l'erreur z².
4. Calculer la somme delta de sortie pour la couche z² en appliquant la dérivée de notre fonction d'activation sigmoïde (comme à l'étape 2).
5. Ajuster les poids de la première couche en effectuant un **produit scalaire de la couche d'entrée** avec la **somme delta de sortie cachée (z²)**. Pour le deuxième poids, effectuer un produit scalaire de la couche cachée (z²) et la **somme delta de sortie de sortie (o)**.

Calculer la somme delta de sortie puis appliquer la dérivée de la fonction sigmoïde sont très importants pour la rétropropagation. La dérivée de la sigmoïde, également connue sous le nom de **sigmoïde prime**, nous donnera le taux de changement, ou la pente, de la fonction d'activation à la somme de sortie.

Continuons à coder notre classe `Neural_Network` en ajoutant une fonction sigmoidPrime (dérivée de la sigmoïde) :

Ensuite, nous voudrons créer notre fonction de propagation `backward` qui fait tout ce qui est spécifié dans les quatre étapes ci-dessus :

Nous pouvons maintenant définir notre sortie en initiant la propagation avant et en initiant la fonction backward en l'appelant dans la fonction `train` :

Pour exécuter le réseau, tout ce que nous avons à faire est d'exécuter la fonction `train`. Bien sûr, nous voudrons le faire plusieurs fois, ou peut-être des milliers de fois. Nous utiliserons donc une boucle `for`.

Voici les 60 lignes complètes de génialité :

Et voilà ! Un réseau de neurones complet capable d'apprendre à partir d'entrées et de sorties.

Bien que nous ayons pensé à nos entrées comme des heures d'étude et de sommeil, et à nos sorties comme des scores de test, n'hésitez pas à les changer pour ce que vous voulez et observez comment le réseau s'adapte !

Après tout, tout ce que le réseau voit, ce sont les nombres. Les calculs que nous avons faits, aussi complexes qu'ils semblaient être, ont tous joué un grand rôle dans notre modèle d'apprentissage.

Si vous souhaitez prédire une sortie basée sur nos données entraînées, comme prédire le score du test si vous avez étudié pendant quatre heures et dormi pendant huit, consultez le [tutoriel complet ici](https://tryenlight.github.io).

### [Démo](https://repl.it/Jxmb/2) & [Source](https://github.com/TryEnlight/tryenlight.github.io/blob/master/demo/machine-learning/NeuralNetwork/NeuralNetwork.py)

#### Références

[Steven Miller](https://stevenmiller888.github.io/mind-how-to-build-a-neural-network/)

[Welch Labs](https://www.youtube.com/watch?v=bxe2T-V8XRs)

[Kabir Shah](https://blog.kabir.ml/posts/machine-learning.html)

Ce tutoriel a été initialement publié sur [Enlight](https://tryenlight.github.io), un site web qui héberge une variété de tutoriels et de projets pour apprendre en construisant ! Consultez-le pour plus de projets comme ceux-ci :)