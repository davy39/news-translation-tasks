---
title: Reconnaissance d'Images Démystifiée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-23T14:00:28.000Z'
originalURL: https://freecodecamp.org/news/image-recognition-demystified-fc9c89b894ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W0QURB5AK4NvOX62yYPLwg.jpeg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Reconnaissance d'Images Démystifiée
seo_desc: 'By gk_

  Nothing in machine learning captivates the imagination quite like the ability to
  recognize images. Identifying imagery must connote “intelligence,” right? Let’s
  demystify.

  The ability to “see,” when it comes to software, begins with the abilit...'
---

Par gk_

Rien en apprentissage automatique ne captive autant l'imagination que _la capacité à reconnaître des images_. Identifier des images doit connoter l'« intelligence », n'est-ce pas ? Démystifions.

La capacité de « voir », lorsqu'il s'agit de logiciels, commence par la capacité à classer. La classification est la correspondance de motifs avec des données. Les images sont des données sous forme de matrices bidimensionnelles.

La reconnaissance d'images consiste à classer des données dans une catégorie parmi plusieurs. C'est un travail utile : vous pouvez classer une image entière ou des éléments au sein d'une image.

![Image](https://cdn-media-1.freecodecamp.org/images/1*peDK8ySk0NHBRJMxSEzu8w.jpeg)

L'une des applications classiques et très utiles de la classification d'images est la reconnaissance optique de caractères ([OCR](https://en.wikipedia.org/wiki/Optical_character_recognition)) : _passer d'images de langage écrit à du texte structuré_.

Cela peut être fait pour n'importe quel alphabet et une grande variété de styles d'écriture.

### Étapes du processus

Nous allons construire du code pour reconnaître des chiffres numériques dans des images et montrer comment cela fonctionne. Cela prendra 3 étapes :

1. rassembler et organiser des **données** à utiliser (85 % de l'effort)
2. construire et tester un **modèle prédictif** (10 % de l'effort)
3. utiliser le modèle pour **reconnaître** des images (5 % de l'effort)

La préparation des données est de loin la plus grande partie de notre travail, _ceci est vrai pour la plupart des travaux en science des données_. Il y a une raison pour laquelle cela s'appelle la science des DONNÉES !

La construction de notre modèle prédictif et son utilisation pour prédire des valeurs _est entièrement mathématique_. Nous utilisons un logiciel pour itérer à travers les données, [pour forger itérativement des « poids » au sein d'équations mathématiques](https://medium.com/p/how-neural-networks-work-ff4c7ad371f7), et pour travailler avec des structures de données. Le logiciel n'est pas « intelligent », il travaille avec des équations mathématiques pour effectuer le travail de connaissance étroit, dans ce cas : reconnaître des images de chiffres.

En pratique, la plupart de ce que les gens étiquetent comme « IA » est vraiment juste un logiciel [effectuant un travail de connaissance](https://medium.com/intuitionmachine/the-ai-label-is-bullshit-559b171867ff).

### Notre modèle prédictif et les données

Nous allons utiliser l'un des modèles prédictifs les plus simples : la régression des « k plus proches voisins » ou « kNN », publiée pour la première fois par E. Fix, J.L. Hodges en 1952.

Une explication simple de cet algorithme est [ici](https://www.analyticsvidhya.com/blog/2014/10/introduction-k-neighbours-algorithm-clustering/) et une vidéo de ses mathématiques [ici](https://www.youtube.com/watch?v=4ObVzTuFivY). Et aussi [ici](http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/) pour ceux qui veulent construire l'algorithme à partir de zéro.

Voici comment cela fonctionne : imaginez un graphique de points de données et des cercles capturant k points, chaque valeur de k étant validée par rapport à vos données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rmdr7RsUPOWranwOuuIl7w.png)
_crédit : [http://bdewilde.github.io](http://bdewilde.github.io/about-me/" rel="noopener" target="_blank" title=")_

L'erreur de validation pour k dans vos données a un minimum qui peut être déterminé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WUjVS8di8GVnTise0pRUOw.png)
_crédit : [https://www.analyticsvidhya.com](https://www.analyticsvidhya.com" rel="noopener" target="_blank" title=")_

Étant donné la valeur « meilleure » pour k, vous pouvez classer d'autres points avec une certaine mesure de précision.

Nous utiliserons [l'algorithme kNN de scikit-learn](http://scikit-learn.org/stable/modules/neighbors.html) pour éviter de construire les mathématiques nous-mêmes. Heureusement, cette bibliothèque nous fournit également nos [données d'images](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z0-GGUh1Z9O2J4jlDFgyrg.png)
_crédit : [http://scikit-learn.org](http://scikit-learn.org" rel="noopener" target="_blank" title=")_

Commençons.

Le code est [ici](https://github.com/ugik/notebooks/blob/master/Digits%20Classification.ipynb), nous utilisons [iPython notebook](https://ipython.org/notebook.html) qui est une manière productive de travailler sur des projets de science des données. La syntaxe du code est Python et notre exemple est emprunté [à sk-learn](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html).

Commencez par importer les bibliothèques nécessaires :

Ensuite, nous organisons nos données :

```
images d'entraînement : 1527, images de test : 269
```

Vous pouvez manipuler la fraction et avoir plus ou moins de données de test, nous verrons bientôt comment cela impacte la précision de notre modèle.

À ce stade, vous vous demandez probablement : comment les images de chiffres sont-elles organisées ? Ce sont des tableaux de valeurs, une pour chaque pixel dans une image 8x8. Inspectons-en une.

```
# une dimension[  0.   1.  13.  16.  15.   5.   0.   0.   0.   4.  16.   7.  14.  12.   0.   0.   0.   3.  12.   2.  11.  10.   0.   0.   0.   0.   0.   0.  14.   8.   0.   0.   0.   0.   0.   3.  16.   4.   0.   0.   0.   0.   1.  11.  13.   0.   0.   0.   0.   0.   9.  16.  14.  16.   7.   0.   0.   1.  16.  16.  15.  12.   5.   0.]
```

```
# deux dimensions[[  0.   1.  13.  16.  15.   5.   0.   0.] [  0.   4.  16.   7.  14.  12.   0.   0.] [  0.   3.  12.   2.  11.  10.   0.   0.] [  0.   0.   0.   0.  14.   8.   0.   0.] [  0.   0.   0.   3.  16.   4.   0.   0.] [  0.   0.   1.  11.  13.   0.   0.   0.] [  0.   0.   9.  16.  14.  16.   7.   0.] [  0.   1.  16.  16.  15.  12.   5.   0.]]
```

Les mêmes données d'image sont affichées sous forme de tableau plat (unidimensionnel) et à nouveau sous forme de tableau 8x8 dans un tableau (bidimensionnel). Imaginez chaque ligne de l'image comme un tableau de 8 pixels, il y a 8 lignes. Nous pourrions ignorer les niveaux de gris (les valeurs) et travailler avec des 0 et des 1, cela simplifierait un peu les mathématiques.

Nous pouvons « tracer » cela pour voir ce tableau sous sa forme « pixelisée ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*kuMXKLWP30lCcinFeFmlwg.png)

Quel est ce chiffre ? Demandons à notre modèle, mais d'abord nous devons le construire.

```
Score KNN : 0.951852
```

Par rapport à nos données de test, notre modèle des plus proches voisins avait un score de précision de 95 %, pas mal. Revenez en arrière et changez la valeur de la « fraction » pour voir comment cela impacte le score.

```
array([2])
```

Le modèle prédit que le tableau montré ci-dessus est un « **2** », ce qui semble correct.

Essayons quelques autres, rappelez-vous _ce sont des chiffres de nos données de test_, nous n'avons pas utilisé ces images pour construire notre modèle (très important).

![Image](https://cdn-media-1.freecodecamp.org/images/1*7_tI-pWkoL_TGnznn03XSQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*i_66ipCudPzXp_7xybbduQ.png)

Pas mal.

Nous pouvons créer un chiffre fictif et voir ce que notre modèle en pense.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qbRTa4wnIY2dzrzTMjPMBA.png)

Si nous avions une collection d'images de chiffres nonsensiques, nous pourrions les ajouter à notre entraînement avec une étiquette non numérique — juste une autre classification.

### Alors, comment fonctionne la reconnaissance d'images ?

* **les données d'image sont organisées** : à la fois l'entraînement et le test, avec des étiquettes (X, y)

Les données d'entraînement sont gardées séparées des données de test, ce qui signifie également que nous supprimons les doublons (ou quasi-doublons) entre eux.

* **un modèle est construit** en utilisant l'un des plusieurs modèles mathématiques ([kNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression), [réseau de neurones convolutif](https://en.wikipedia.org/wiki/Convolutional_neural_network), etc.)

Le type de modèle que vous choisissez dépend de vos données et du type et de la complexité du travail de classification.

* de nouvelles données sont mises dans le modèle pour **générer une prédiction**

C'est extrêmement rapide : le résultat d'un seul calcul mathématique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWwtxuFc-EwBhAj3-FMXUQ.jpeg)

Si vous avez une collection de photos avec _et sans_ chats, vous pouvez construire un modèle pour classer si une photo contient un chat. Remarquez que vous avez besoin d'images d'entraînement qui sont dépourvues de tout chat pour que cela fonctionne.

Bien sûr, vous pouvez appliquer plusieurs modèles à une photo et identifier plusieurs choses.

### Grandes Données

Un défi significatif dans tout cela est _la taille de chaque image_ puisque 8x8 n'est pas une taille d'image raisonnable pour autre chose que de petits chiffres, il n'est pas rare de traiter des images de 500x500 pixels, ou plus. Cela fait 250 000 pixels par image, donc 10 000 images d'entraînement signifie _effectuer des mathématiques sur 2,5 milliards de valeurs_ pour construire un modèle. Et les mathématiques ne sont pas seulement de l'addition ou de la multiplication : nous multiplions des matrices, multiplions par des poids en virgule flottante, calculons des dérivées. C'est pourquoi la puissance de traitement (et la mémoire) est clé dans certaines applications d'apprentissage automatique.

Il existe des stratégies pour traiter ce problème de taille d'image :

* utiliser des unités de traitement graphique matérielles ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit)) pour accélérer les mathématiques
* réduire les images à des dimensions plus petites, sans perdre de clarté
* réduire les couleurs à des niveaux de gris et des gradients (vous pouvez toujours _voir_ le chat)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hcsGFgx20IiVrKaw5tSaHw.png)

* regarder des sections d'une image pour trouver ce que vous cherchez

La bonne nouvelle est qu'une fois qu'un modèle est construit, peu importe combien cela a été laborieux, la prédiction est rapide. Le traitement d'images est utilisé dans des applications allant de la reconnaissance faciale à l'OCR en passant par les voitures autonomes.

Maintenant, vous comprenez les bases de comment cela fonctionne.