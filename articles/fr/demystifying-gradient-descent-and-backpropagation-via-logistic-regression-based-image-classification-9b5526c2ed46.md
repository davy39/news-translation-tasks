---
title: Démystifier la descente de gradient et la rétropropagation via la régression
  logistique basée sur l'image…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-07T16:26:53.000Z'
originalURL: https://freecodecamp.org/news/demystifying-gradient-descent-and-backpropagation-via-logistic-regression-based-image-classification-9b5526c2ed46
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3CIrmxmNJnzNg8J2KFL2AQ.gif
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Démystifier la descente de gradient et la rétropropagation via la régression
  logistique basée sur l'image…
seo_desc: 'By Sachin Malhotra

  What’s all the hype about Deep Learning and what is a Neural Network anyway?

  Essentially,


  you have an architecture

  with millions of parameters shared amongst thousands of neurons

  stacked up in multiple layers

  with various activati...'
---

Par Sachin Malhotra

Qu'est-ce que tout ce battage autour de l'apprentissage profond et qu'est-ce qu'un réseau de neurones de toute façon ?

Essentiellement,

* vous avez une architecture
* avec des millions de paramètres partagés parmi des milliers de neurones
* empilés en plusieurs couches
* avec diverses fonctions d'activation appliquées aux logits ou aux sorties des couches
* et des entrées normalisées alimentées avec des initialisations de poids aléatoires.
* La perte sur le lot d'entraînement définit les gradients pour l'étape de rétropropagation à travers le réseau
* et la descente de gradient stochastique faisant sa magie pour entraîner le modèle et minimiser la perte jusqu'à convergence.

Si vous avez aimé l'article, n'hésitez pas à partager votre amour et à le partager autant que possible. C'est tout pour aujourd'hui les amis. J'espère que vous avez passé un bon moment à le lire. ?.

Vous ne pensiez pas vraiment que je mettrais fin à l'article au milieu de toute cette confusion concernant ce jargon technique, n'est-ce pas ? ?

Si vous êtes quelqu'un avec absolument aucune connaissance de tout cela et que tous les termes mentionnés précédemment vous semblent du grec, ne vous inquiétez pas. Parce qu'à la fin de cet article, je suis sûr que vous serez en mesure de l'entraîner, de le tester, de le rendre plus dense et donc, plus intelligent.

Commençons maintenant, d'accord ?

### Table des matières

* [L'algorithme d'apprentissage automatique ancestral](https://medium.com/p/9b5526c2ed46#f0d4)
* [Préparation des données](https://medium.com/p/9b5526c2ed46#3f91)
* [Dites bonjour au neurone](https://medium.com/p/9b5526c2ed46#76ab)
* [Propagation avant](https://medium.com/p/9b5526c2ed46#8c44)
* [Implémentation !](https://medium.com/p/9b5526c2ed46#ccfc)
* [Aplatissement de l'image](https://medium.com/p/9b5526c2ed46#b04c)
* [Fonction d'activation Sigmoïde](https://medium.com/p/9b5526c2ed46#f084)
* [Alimentation du réseau ?](https://medium.com/p/9b5526c2ed46#e062)
* [Faisons une prédiction ?](https://medium.com/p/9b5526c2ed46#7e0a)
* [Descendons la colline ?](https://medium.com/p/9b5526c2ed46#f98c)
* [Entrez : la fonction de perte ?](https://medium.com/p/9b5526c2ed46#e0b7)
* [Minimisation de la fonction de perte ](https://medium.com/p/9b5526c2ed46#1cdb)
* [La descente de gradient trouve-t-elle toujours le minimum global ?](https://medium.com/p/9b5526c2ed46#2893)
* [Laissez les gradients circuler ](https://medium.com/p/9b5526c2ed46#5df3)
* [Codons ! ?](https://medium.com/p/9b5526c2ed46#e389)

### L'algorithme d'apprentissage automatique ancestral

Commençons par une très brève (bien, trop brève) introduction à ce que fait essentiellement l'un des plus anciens algorithmes en apprentissage automatique.

Prenez quelques points sur un graphique 2D, et tracez une ligne qui les ajuste aussi bien que possible. Ce que vous venez de faire est généralisé à partir de quelques exemples de paires de valeurs d'entrée (x) et de valeurs de sortie (y) à une fonction générale qui peut mapper toute valeur d'entrée à une valeur de sortie.

Cela est connu sous le nom de **régression linéaire**, et c'est une technique merveilleuse pour extrapoler une fonction générale à partir d'un ensemble de paires entrée-sortie.

Et voici pourquoi avoir une telle technique est merveilleux : il existe un nombre incalculable de fonctions dans le monde réel pour lesquelles trouver les équations est une tâche très difficile, mais collecter des paires entrée-sortie est une tâche relativement plus facile à faire — par exemple, la fonction mappant une entrée d'audio enregistré d'un mot parlé à une sortie de ce que ce mot parlé est. [[Source]](http://www.andreykurenkov.com/writing/ai/a-brief-history-of-neural-nets-and-deep-learning/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DsWyE2NY7AxX-RSzHk5mzQ.png)
_Source : [https://www.oreilly.com/](https://www.oreilly.com/" rel="noopener" target="_blank" title=")_

Cependant, comme nous le savons tous, nous pouvons avoir des données qui ne sont pas linéairement séparables. Les points de données peuvent être trop dispersés pour que nous puissions avoir une fonction linéaire pour mapper approximativement les valeurs X données aux valeurs Y données. Un algorithme de régression linéaire est très adapté pour quelque chose comme la prédiction des prix des maisons étant donné un ensemble de caractéristiques artisanales. Mais il ne pourra pas ajuster les données qui ne peuvent être approximées que par une fonction non linéaire.

Et si l'énoncé du problème est celui de la **classification d'images** ? Supposons que nous avons une image en entrée et que nous voulons que notre modèle indique si l'image donnée est celle d'un chat ou d'un chien.

Comment allons-nous résoudre ce problème ?

Commençons par l'étape la plus basique qui est celle de la **préparation du jeu de données pour notre modèle**. Nous expliquerons le fonctionnement du modèle plus tard dans l'article.

L'un des aspects les plus importants de la construction de tout modèle d'apprentissage automatique est de préparer le jeu de données et de le mettre dans un format approprié que le modèle pourra traiter et tirer des conclusions significatives.

### Préparation des données

Le jeu de données que nous allons examiner dans cette tâche est la tâche de classification binaire Chats vs Chiens disponible sur [Kaggle](http://kaggle.com/c/dogs-vs-cats). En supposant que vous avez téléchargé le jeu de données, chargeons le jeu de données en mémoire et regardons quelques-unes des images disponibles dans le jeu de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W9z8zHGafvz98XQDyI1_Ww.png)

Les données sont disponibles sous forme de fichiers zip et après décompression, vous devriez avoir deux dossiers différents. Un pour `train` et l'autre pour `test`. Les données de `test` ne seront pas utilisées tout au long de l'article car nous nous contentons du jeu de données d'entraînement lui-même. Le dossier `train` contient environ 25000 images et nous les divisons en un jeu de données `train` plus petit avec 2000 images et un autre qui servira de jeu de validation contenant 5000 images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*flmbyyalr-gjvrSx2pVSAA.png)

Nous venons d'imprimer le nom d'un fichier aléatoire dans le jeu de données d'entraînement. Les noms de fichiers sont du type

```
cat.<some number>.jpg ou dog.<some number>.jpg
```

Notre modèle ne pourra pas simplement traiter les fichiers jpg. Il y a une certaine quantité de travail à faire sur ces images pour amener les données dans un certain format avant que notre modèle ne puisse les traiter et faire des prédictions.

#### Images en tant que représentations matricielles

Comme discuté précédemment, lors de l'entraînement de notre modèle, nous aurons une certaine image alimentée dans le modèle et le modèle nous donnera une prédiction quant à savoir s'il pense que l'image est celle d'un chat ou d'un chien. Le modèle peut être correct ou non, et s'il ne l'est pas, alors nous devons l'« entraîner » pour qu'il s'améliore dans la classification des images de chats et de chiens.

Un ordinateur stocke les données d'image sous la forme d'un tableau de données `M-par-N-par-3` qui définit les composantes de couleur rouge, verte et bleue pour chaque pixel individuel. Ainsi, si nous regardons les données d'image sous la forme d'une matrice multidimensionnelle, nous avons une matrice 3D avec les dimensions `(M, N, 3)` et chaque valeur sera une valeur entière dans la plage 0-255 où 0 représente le noir et 1 représente le blanc et les valeurs restantes constituent différentes nuances des composantes de couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LTtuPIc1N3_luff9LDR3jA.png)

[Imageio](https://imageio.github.io/) est une bibliothèque Python qui fournit une interface facile pour lire et écrire une large gamme de données d'image, y compris les images animées, la vidéo, les données volumétriques et les formats scientifiques.

[Numpy](http://www.numpy.org/) est un package de calcul scientifique en Python et est l'une des bibliothèques les plus fondamentales en Python pour manipuler et travailler avec des tableaux de haute dimension de manière efficace. Pour un guide détaillé sur Numpy et comment nous manipulons les données d'image, lisez [ceci](http://cs231n.github.io/python-numpy-tutorial/#numpy).

Je vous recommande fortement de parcourir le tutoriel Numpy mentionné ci-dessus. La programmation du modèle dont nous allons discuter par la suite est principalement réalisée en Numpy, et une compréhension de base des opérations en Numpy est extrêmement importante.

#### Redimensionnement des images

Ensuite, regardons à quoi ressemble le tableau numpy pour certaines de ces images, c'est-à-dire quelle est la dimensionnalité de certains de ces tableaux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xy5iD-h9-B3BVrvcST_OWg.png)
_Impression de 10 tailles d'images aléatoires à partir des données que nous avons._

Nous sélectionnons aléatoirement certaines des images de la liste `train_data` que nous avons créée et nous imprimons la forme, c'est-à-dire les dimensions des tableaux numpy représentant cette image.

Comme nous pouvons le voir, les tailles des images sont assez variées. Au niveau le plus basique, chaque pixel sera une entrée pour notre modèle de classification d'images et si le nombre de pixels est différent pour chaque image, alors le modèle ne pourra pas les traiter.

Nous avons besoin que les images soient de la même taille avant de les alimenter dans notre modèle.

Si vous êtes vaguement conscient de l'un des modèles d'apprentissage automatique ou d'apprentissage profond, vous devez avoir entendu parler de quelque chose connu sous le nom de `paramètres` du modèle.

Les paramètres sont ce qui porte l'essentiel de l'information apprise par nos modèles et le nombre de paramètres pour un modèle doit être fixé avant de commencer à entraîner le modèle.

Pour cette raison même, nous ne pouvons pas alimenter des images de taille dynamique. Nous devons fixer la taille des images et donc le nombre de pixels dans chaque image afin que nous puissions définir le nombre d'entrées pour notre modèle par exemple et également fixer les paramètres totaux apprenables pour notre modèle.

Ne vous inquiétez pas si vous n'avez aucune idée de ce que sont réellement ces `paramètres`. Nous y viendrons bientôt.

Pour l'instant, l'important est que **nous avons besoin que toutes les images soient de la même taille** pour que notre modèle puisse les traiter.

Voyons combien d'images ont des tailles supérieures à `64-par-64` en hauteur et en largeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bXVEyOWbkU4u9p-OkAsDrQ.png)
_99% des images peuvent être réduites à 64-par-64-3 images._

Comme nous pouvons le voir clairement, 99% des images ont des dimensions supérieures à `64-par-64` et donc, nous pouvons les réduire à la taille `64-par-64-par-3`.

Cette approche est juste une approche naïve que j'ai adoptée pour rendre toutes les images de la même taille et j'ai estimé que la réduction ne dégraderait pas autant la qualité des images que l'agrandissement, car l'agrandissement d'une image très petite en une grande conduit principalement à des effets pixelisés et rendrait l'apprentissage pour le modèle plus difficile. De plus, cette dimension `64-par-64-par-3` n'est pas un nombre magique, juste quelque chose que j'ai choisi.

Il y aurait des approches beaucoup meilleures pour le prétraitement des données en ce qui concerne les données d'image, mais cela suffira pour l'article actuel.

Passons à autre chose et regardons le code qui redimensionnerait toutes ces images et diviserait également les données en ensembles `train` et `test`. Nous divisons les données données en utilisant une division 80/20, c'est-à-dire que 80% des données seraient utilisées pour entraîner nos données et les 20% restants seraient utilisés pour tester notre modèle afin de voir la performance finale sur les données invisibles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*brJegYUIgHEz1Rg07YyX5A.png)
_Les fichiers train contiennent des tuples de la forme (image_matrix, 1 ou 0 selon qu'il s'agit d'un chat ou d'un chien)_

Pour redimensionner les images, nous avons utilisé la méthode `[scipy.misc.imresize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imresize.html)`. Cette méthode sera bientôt obsolète, donc mieux vaut vérifier d'autres [options](https://datascience.stackexchange.com/questions/5224/how-to-prepare-augment-images-for-neural-network) pour redimensionner les images également au lieu de compter sur celle-ci pour vos futures aventures.

La raison pour laquelle le fonctionnement interne de `scipy.misc.imresize` n'est pas fourni ici est qu'il n'est pas pertinent pour le cadre de cet article.

Maintenant que nous avons redimensionné nos images, regardons à quoi ressemblent nos données d'entraînement et de test maintenant, c'est-à-dire quelles sont leurs dimensions finales.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BgcM7hjRe9WDC-LRVbpXsw.png)
_Dimensions finales de nos données d'entraînement et de test qui peuvent être directement alimentées dans notre modèle._

#### Sauvegarde des données

Maintenant que nous avons traité nos données et que nous les avons dans le format dont nous avons besoin, nous pouvons enfin les sauvegarder dans deux fichiers séparés, à savoir `train.npz` et `valid.npz`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U1fhWibqTLH8VMBsW3suYQ.png)
_Sauvegarde des données d'entraînement et de test dans des fichiers._

La taille du fichier `train.npz` est de 1,8 Go et celle de `valid.npz` est de 469 Mo. Ces fichiers contiennent les tableaux numpy que nous avons créés précédemment pour représenter nos ensembles d'entraînement et de test respectivement.

Notez que dans cet ensemble de données, nous n'utilisons aucune architecture d'apprentissage profond sophistiquée. Nous expérimentons simplement et montrons la puissance d'un seul neurone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OGNO4PTnE60iGF4zQhJEZg.jpeg)
_Source : [https://i1.wp.com/blog.eyewire.org](https://i1.wp.com/blog.eyewire.org" rel="noopener" target="_blank" title=")_

En conséquence, nous n'avons pas une longue liste d'hyperparamètres à ajuster, et donc nous n'avons pas divisé les données originales en train, dev et test. Nous nous sommes contentés d'un ensemble d'entraînement et d'un ensemble de dev (ou un ensemble de validation ou un ensemble de test en ce qui concerne cet article). Donc, nous utilisons le terme données de validation ou données de test de manière interchangeable dans cet article.

Note : Le but des données d'entraînement, des données de dev ou de validation, et des données de test sont très différents les uns des autres. Les trois sont extrêmement importants

* chaque fois que nous résolvons un gros problème avec beaucoup de données et des architectures complexes, et
* où nous sommes réellement préoccupés par les résultats finaux étant sur un ensemble de test séparé et non vu.

Nous n'avons pas de telles exigences ici. Et donc, pas d'ensemble de test séparé.

Jetez un coup d'œil au notebook Jupyter qui rassemble tout ce dont nous avons discuté ci-dessus pour vous.

### Dites bonjour au neurone

Maintenant que nous avons prétraité nos données et que nous les avons dans un format que notre modèle de classification binaire pourra comprendre, permettons-nous de vous présenter le composant central de notre modèle : le neurone !

Le neurone est l'élément de calcul central de notre modèle de classification. Essentiellement, le neurone effectue ce que l'on appelle la `propagation avant` sur les données d'entrée.

Voyons ce que cela signifie.

### Propagation avant

Supposons pour l'instant que notre image est représentée par une seule valeur réelle. Nous appellerons cette seule valeur réelle une caractéristique représentant notre image d'entrée.

Si vous avez suivi et que vous avez parcouru l'étape de préparation des données, vous saurez que nous avons environ `12288` caractéristiques au total qui représentent une seule image.

Si vous n'êtes pas sûr de savoir comment nous sommes arrivés à ce nombre, ne vous inquiétez pas, nous y viendrons plus tard.

**Indice :** C'est 64 * 64 * 3 ?

Avant de continuer, regardons les notations que nous allons suivre tout au long de cet article

* un petit alphabet italique représente une valeur scalaire
* un petit alphabet gras non italique représente un vecteur, c'est-à-dire une matrice ligne `1-par-m` ou une matrice colonne `m-par-1`.
* les alphabets italiques majuscules représenteront des matrices d'une dimension donnée, par exemple `m-par-n`.

Soit `_x_` la caractéristique unique qui représente notre image d'entrée.

Maintenant, comme première étape de ce processus appelé propagation avant,

> le neurone applique une transformation linéaire à la caractéristique d'entrée

Ne vous laissez pas effrayer par ce que signifie cette **transformation linéaire**. Cela signifie essentiellement que nous avons quelque chose de la forme représentée par le diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NOvvMzvrcWMZ9Ji_C02iOw.png)

Ainsi, étant donné la caractéristique d'entrée _x,_ le neurone nous donne la sortie suivante :

```
Wx + b
```

Remarquez l'utilisation des notations dans le diagramme et dans la section de code ci-dessus. Ainsi, `_x_` représente une valeur scalaire, `_W_` représente une matrice, et **b** représente un vecteur.

La matrice _W_ est appelée matrice de `poids` et le vecteur **b** est connu sous le nom de vecteur de `biais`.

Vous vous souvenez lorsque nous parlions des paramètres du modèle plus tôt ? Eh bien, la matrice de poids et le vecteur de biais représenteraient les paramètres de notre modèle dans ce scénario.

**Note :** bien que nous parlions de `_W_` comme notre matrice de « poids » et de `**b**` comme notre vecteur de « biais », dans le scénario ci-dessus, puisque nous n'avons qu'une seule caractéristique d'entrée, nous avons seulement besoin d'une matrice `1-par-1` pour `_W_` et d'une valeur scalaire pour `**b**`.

C'est tout ce qu'il y a à la transformation linéaire de la caractéristique d'entrée. Nous la multiplions par un `poids` et nous ajoutons un `biais` pour obtenir une valeur transformée.

### _Wx_ + **b** = 94.233, Et maintenant ?

C'est juste une valeur aléatoire qui me vient à l'esprit. Le point que j'essaie de faire ici est de savoir ce que nous devons faire avec cette valeur transformée maintenant ?

Rappelez-vous, notre objectif ultime est d'entraîner un modèle qui sera capable de différencier un chien d'un chat.

Puisque cela est une tâche de classification binaire (seulement 2 classes parmi lesquelles le modèle peut choisir), nous devons avoir une sorte de seuil, disons ``. Lorsque le neurone génère une valeur au-dessus de ``, il sortira l'une des classes, sinon sa sortie serait la deuxième classe.

Il est vraiment difficile d'obtenir la plage de valeurs qu'une transformation linéaire donnerait. La valeur peut être n'importe quoi allant de `-inf` à `+inf`. Tout dépend de la plage de valeurs que la ou les caractéristiques d'entrée peuvent prendre et de la manière dont le poids et le biais ont été initialisés.

Ainsi, nous devons définitivement fixer la plage des valeurs de sortie par le neurone.

Comment faisons-nous cela ?

En appliquant ce que l'on appelle une fonction d'**activation** à la sortie linéaire du neurone.

La fonction d'activation fixera simplement la plage des valeurs de sortie par le neurone afin que nous puissions décider de notre seuil `` pour la sortie de classification par le neurone.

**Note :** La fonction d'activation fait bien plus que simplement fixer les valeurs de sortie du neurone, mais encore une fois, pour le cadre de cet article, savoir cela est plus que suffisant.

La fonction d'activation que nous allons considérer ici est connue sous le nom de fonction Sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gf2Qf07cng6zsXhRcPimQw.png)
_La fonction d'activation Sigmoïde_

Et voici le graphique de la fonction sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*a5QwiyaSyvRa6n3VKYVEnQ.png)
_Source : [https://www.vaetas.cz/img/machine-learning/sigmoid-function.png](https://www.vaetas.cz/img/machine-learning/sigmoid-function.png" rel="noopener" target="_blank" title=")_

Comme nous pouvons le voir sur le graphique ci-dessus, la fonction d'activation sigmoïde applique ce que l'on appelle une `transformation non linéaire` à la valeur d'entrée et la plage de la fonction sigmoïde est un ensemble de valeurs réelles entre [0, 1].

Ainsi, le neurone dans son ensemble effectue essentiellement deux opérations dans le cadre du processus de propagation avant.

1. Appliquer une transformation linéaire sur la ou les caractéristiques d'entrée et
2. Appliquer une transformation non linéaire (sigmoïde dans notre cas) par-dessus la sortie précédente pour donner la sortie finale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NqQz69UgV083Id6Ex7pcvA.png)
_Ensemble complet des transformations par un neurone._

### Mais attendez. Vous avez dit que chaque image a 12288 caractéristiques ?

Nous avons expliqué les calculs ci-dessus en supposant que l'image d'entrée serait représentée par une seule valeur de caractéristique.

Ce n'est cependant pas le cas que nous traitons. Vous vous souvenez que nous avions parcouru toute l'étape de préparation des données avant de commencer la propagation avant et que nous avions redimensionné nos images à `64-par-64-par-3` ?

Cela signifie que notre image traitée est essentiellement composée de `12288` pixels au total.

Pour notre cas d'utilisation et le modèle de classification simpliste avec lequel nous traitons, nous considérerons simplement chacun des pixels comme une caractéristique d'entrée.

Cela signifie que nous avons `12288` caractéristiques d'entrée par image pour notre modèle. Voyons maintenant les changements que cela introduit dans les dimensions des paramètres de notre modèle, c'est-à-dire le poids et le biais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJmDBOaKrIuEKo2-INTP6g.png)

Représentons le nombre de caractéristiques d'entrée de notre image par `nx`. Pour les images que nous allons considérer ici, le nombre de caractéristiques d'entrée serait de 12288.

Ainsi, nous alimentons toutes ces caractéristiques d'entrée pour une image donnée à notre neurone, il effectue une transformation linéaire sur chacune des caractéristiques, combine le résultat pour donner une valeur scalaire, puis applique la transformation sigmoïde sur la valeur pour enfin nous donner `y^` c'est-à-dire la classe à laquelle cette image appartient.

Notez que le modèle donne simplement une valeur réelle entre 0 et 1.

**L'interprétation est que si la valeur est > 0,5, c'est un chien/chat (peu importe la manière dont vous voulez le considérer) et pour toutes les autres valeurs, c'est l'autre classe.**

Nous pouvons soit représenter les caractéristiques d'entrée comme un `vecteur colonne` soit un `vecteur ligne`. Ainsi, nous pouvons soit avoir un vecteur de forme `12288-par-1)` soit `1-par-12288`. Considérons le premier, c'est-à-dire que nous aurons un vecteur colonne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uCvi3E7SeSbSHdBURchO9Q.png)
_Vecteur colonne représentant les caractéristiques d'entrée._

Nous aborderons la partie codage dans la section suivante. Ce n'est pas une tâche énorme de convertir les valeurs de pixels d'image `64-par-64-par-3` en `12288-par-1`.

Auparavant, nous avions expliqué le processus de propagation avant pour une seule caractéristique d'entrée. Nous avions une valeur de poids pour cette caractéristique d'entrée unique et ensuite nous avions également une valeur de biais pour celle-ci qui se combinait et nous donnait la transformation linéaire que nous recherchions.

De manière similaire, nous aurons besoin d'une valeur de poids pour **chacune** des caractéristiques d'entrée. Nous n'avons pas besoin d'une valeur de biais séparée pour chacune des caractéristiques. Une seule valeur, c'est-à-dire une valeur scalaire, suffirait ici.

La transformation linéaire devient maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9i3llqOioPkiikiNf6Bcxw.png)
_Transformation linéaire des caractéristiques d'entrée de l'image_

Pour chaque caractéristique d'entrée, nous la multiplions par sa valeur de poids correspondante, puis nous additionnons toutes ces valeurs ensemble et enfin nous ajoutons le terme de biais pour obtenir la valeur de transformation linéaire.

L'étape suivante reste la même : nous appliquons la fonction d'activation sigmoïde sur `_z_` et nous obtenons une valeur réelle entre 0 et 1 (rappellez-vous, c'est la plage de la fonction sigmoïde).

### Implémentation !

C'est la partie amusante. ?

Nous allons procéder en plusieurs étapes. Tout comme notre notebook Jupyter final serait structuré.

#### Récupération des données

![Image](https://cdn-media-1.freecodecamp.org/images/1*P79CrxXGktNJmRxVsV62mA.png)
_Obtention des données à partir des fichiers sauvegardés_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lmqi2fbp51aSkLnNeP7qog.png)
_Formes des tableaux numpy individuels_

Vous vous souvenez que nous avons sauvegardé nos données après prétraitement dans deux fichiers, à savoir `train.npz` et `valid.npz` ? Nous allons charger nos données à partir de ceux-ci et retourner 4 tableaux numpy différents.

1. `train_x_original` représente nos images d'entraînement dans leurs dimensions originales.
2. `train_y` contient les étiquettes correspondantes pour chacune des images. Juste pour vous rappeler, un `1` représente un chat et un `0` représente un chien.
3. `valid_x_original` est le même que `train_x_original` sauf qu'il contient le jeu de données de validation, c'est-à-dire le jeu de données sur lequel nous allons évaluer la performance de notre modèle.
4. `valid_y` sont les étiquettes pour les images du jeu de validation.

Maintenant, nous avons notre ensemble de données d'entraînement et de validation entier chargé en mémoire. Comme nous l'avons discuté précédemment, nous voulons convertir toutes les caractéristiques de l'image donnée en un vecteur colonne ou un vecteur ligne. Donc, pour chaque image, nous voulons soit un vecteur `12288-par-1` soit un vecteur `1-par-12288`. Voyons comment nous pouvons faire cela à partir de nos images originales de dimensions `64-par-64-par-3`.

#### Aplatissement de l'image

C'est une tâche assez simple dans NumPy. Étant donné une image de dimension `64-par-64-par-3`, nous voulons simplement changer sa forme en `12288-par-1` ou `1-par-12288`.

Puisque nous avons un grand nombre d'images, ce serait soit `12288-par-m` soit `m-par-12288` où `m` représente le nombre total d'images que nous alimenterons notre modèle, c'est-à-dire le nombre d'exemples d'entraînement.

Regardons le code pour cette transformation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Fa3PKCRDS1GSRzNPVHlGw.png)

Nous avons donc défini une fonction appelée `image2vec` qui prend essentiellement tout notre jeu de données dans sa dimension originale, c'est-à-dire `20000-par-64-par-64-par-3` pour l'ensemble d'entraînement et `5000-par-64-par-64-par-3` pour l'ensemble de validation et retourne les matrices aplaties.

Avez-vous remarqué ces lignes de code ?

```
# Normaliser notre jeu de données
train_x /= 255.
valid_x /= 255.
```

Ne vous inquiétez pas, nous y viendrons dans la section suivante lorsque nous discuterons de la fonction d'activation.

En revenant à notre matrice résultante, elle est en 2D et le premier indice est maintenant le nombre de caractéristiques dans chacune de nos images, c'est-à-dire `12288`, et le deuxième indice représente le nombre d'échantillons dans ce jeu de données qui sont `20000` dans l'ensemble d'entraînement et `5000` dans l'ensemble de validation.

Vous pourriez demander pourquoi cette manière spécifique d'organiser nos données. Pourquoi n'avons-nous pas opté pour les versions transposées, c'est-à-dire `m-par-12288` où `m` représente le nombre d'échantillons dans un jeu de données.

Je dirais que nous aurions pu faire cela. Il n'y a rien de mal avec cet arrangement des caractéristiques de l'image. Cependant, vous remarquerez l'avantage d'organiser nos données de cette manière dans les sections à venir lorsque nous aborderons la propagation avant pour l'ensemble du jeu de données.

Visuellement, la matrice aplatie finale ressemble à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/1*V8OxIKYrVuuPUhkD5LTMXA.png)
_La matrice aplatie représentant nos images._

#### Fonction d'activation Sigmoïde

L'étape suivante consiste à définir notre fonction d'activation. Nous avons décrit dans les sections précédentes que nous utilisons une fonction d'activation non linéaire qui, pour cette tâche, est la fonction sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SjRCsEHzX98O84YqBo1HDg.png)

Pour votre référence une fois de plus, voici à quoi ressemble la fonction sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CQyZ_xFQHa8uCJX8jMsq7A.png)
_Fonction Sigmoïde._

Comme expliqué précédemment et comme on peut le voir sur la figure ci-dessus,

> la sigmoïde donne une valeur de 0 pour des valeurs très élevées ou très basses

Par conséquent, nous devons normaliser nos valeurs de caractéristiques afin de ne pas avoir de valeurs trop grandes ou trop petites. Permettez-moi d'expliquer cela avec l'aide d'un exemple.

Considérons les images suivantes de chats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TLXi3KTnDb7-_vS0ilbP4Q.png)

Comme nous l'avons vu précédemment, nous devons redimensionner nos images pour les amener à une taille fixe. Regardons donc ces deux images après les avoir redimensionnées à `64-par-64-par-3`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xdHmf4xP9NbO17_N6LXGVA.png)
_Images redimensionnées._

Chaque image est essentiellement une matrice 3D composée de valeurs RVB de différentes intensités et elles représentent essentiellement les couleurs pour une image donnée.

Les valeurs des pixels (qu'il s'agisse de R, G ou B) vont de `0-255` où un `0` représente le noir complet et `255` est pour le blanc. Entre les deux, il y a des millions de combinaisons de couleurs possibles.

Regardons quelques-unes des valeurs de pixels pour chacune de ces images.

```
[137, 109, 70, 144, 117, 74, 154, 126, 79, 160, 132, 85, 165, 137, 90, 167, 139, 92, 178, 150, 103, 186, 159, 112, 194, 170, 126, 204, 182, 143, 210, 187, 153, 212, 188, 150, 213, 185, 138, 214, 178, 121, 213, 170, 100, 212, 164, 85, 213, 158, 73, 212, 155, 65, 215, 159, 72, 215, 161, 75, 217, 162, 80, 216, 165, 82, 214, 166, 84, 212, 166, 84, 221, 187, 124, 226, 205, 160, 232, 212, 175, 236, 216, 179, 242, 220, 183, 242, 219, 177, 243, 215, 167, 243, 213, 162, 242, 213, 163, 240]
```

Ce sont 100 valeurs de pixels consécutives pour l'image colorée. Ce qui compte ici, c'est la valeur de chacun de ces pixels. Les valeurs sont assez élevées comme on pourrait s'y attendre d'une image colorée comme celle du chat brun(âtre) montré ci-dessus.

```
[37, 37, 37, 37, 37, 37, 29, 29, 29, 35, 35, 35, 39, 39, 39, 36, 36, 36, 38, 38, 38, 88, 88, 88, 43, 43, 43, 34, 34, 34, 33, 33, 33, 52, 52, 52, 48, 48, 48, 40, 40, 40, 33, 33, 33, 33, 33, 33, 39, 39, 39, 52, 52, 52, 36, 36, 36, 34, 34, 34, 46, 46, 46, 31, 31, 31, 34, 34, 34, 33, 33, 33, 35, 35, 35, 34, 34, 34, 26, 26, 26, 32, 32, 32, 25, 25, 25, 29, 29, 29, 23, 23, 23, 44, 44, 44, 43, 43, 43, 20]
```

Même ensemble de valeurs de pixels mais pour l'image noire sont celles montrées ci-dessus. Comme nous pouvons le voir clairement, ces valeurs sont beaucoup plus petites que les valeurs correspondant à l'image colorée.

La raison est simple dans le sens où les valeurs de pixels noir et blanc sont celles dans le voisinage de 0 et naturellement, elles sont plus petites par rapport aux valeurs colorées qui sont dans le voisinage de 255, c'est-à-dire le blanc.

Nous avions parlé de la transformation linéaire sur les caractéristiques d'entrée de l'image donnée. À des fins de révision, voici la formule de transformation linéaire que nous avions utilisée pour une image avec plusieurs caractéristiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9i3llqOioPkiikiNf6Bcxw.png)
_Transformation linéaire des caractéristiques d'entrée de l'image_

Pour la même matrice de poids `_W_` et le vecteur de biais `**b**`, nous obtiendrons des valeurs extrêmement élevées pour les caractéristiques de l'image colorée par rapport à celles de l'image en noir et blanc, n'est-ce pas ?

Après cette transformation linéaire, nous appliquons la fonction d'activation sigmoïdale et nous avons vu précédemment que la fonction d'activation sigmoïdale donne une sortie de 0 pour des valeurs très élevées ou très basses.

Ainsi, naturellement, l'activation sigmoïdale pour le chat coloré se terminerait presque toujours par 0.

Comment résolvons-nous ce problème, pourrait-on demander ?

Nous **normalisons.**

```
# Normaliser notre jeu de données
train_x /= 255.
valid_x /= 255.
```

Cela amènera toutes les caractéristiques d'entrée dans la plage `[0,1]` et donc toutes ces valeurs, qu'il s'agisse d'images colorées ou d'images en noir et blanc, auraient une plage commune. Nous appelons ce processus la normalisation des caractéristiques de l'image.

Maintenant que nous avons toutes nos données traitées et chargées en mémoire, la seule chose qui reste est notre réseau, c'est-à-dire celui alimenté par notre seul neurone. Maintenant, nous allons alimenter toutes ces images à notre modèle de manière itérative et le modèle finira par apprendre (avec une certaine précision) à classer les images comme des chiens ou des chats.

Pour résumer ce que nous avons fait jusqu'à présent :

* Traiter le jeu de données d'images disponible pour nous et nous avons converti les images `.jpg` en tableaux numpy que notre modèle pourra traiter.
* Ensuite, nous avons chargé les deux fichiers `train.npz` et `valid.npz` en mémoire et nous avons aplati les images afin d'avoir `12288-par-1` au lieu de `64-par-64-par-3` images. Nous avons essentiellement rassemblé toutes les caractéristiques de l'image dans une seule colonne.
* Nous avons défini notre fonction d'activation sigmoïde et enfin,
* Nous avons discuté de la raison pour laquelle la normalisation des données est une étape nécessaire.

Maintenant, nous sommes prêts à passer au développement de notre modèle.

### Alimentation du réseau ?

Enfin, nous arrivons au point où nous sommes prêts à alimenter une image entière à notre réseau et à obtenir des prédictions. Voyons comment nous pouvons faire cela d'abord pour une seule image, puis pour l'ensemble de notre jeu de données en une seule fois.

#### Image unique

Comme discuté précédemment, chaque image a maintenant une dimension de `12288-par-1` et lorsque nous utilisons le mot « image », ce que nous voulons vraiment dire, ce sont les caractéristiques de cette image qui ont été aplaties et normalisées.

Pour la transformation linéaire, nous devons avoir une matrice de poids et un vecteur de biais. Nous savons que le modèle nous donnera finalement une seule valeur entre 0 et 1, c'est-à-dire après avoir appliqué la fonction d'activation sigmoïde, et donc le biais est simplement un scalaire.

Essentiellement, nous avons besoin de cette opération :

![Image](https://cdn-media-1.freecodecamp.org/images/1*epe5lbATkfGAgrXDdGmZPA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*3lOqit4y7kj08v4A)

C'est ce que l'on appelle le **produit de Hadamard** ou le produit élément par élément de deux vecteurs, puis nous faisons la somme de toutes ces valeurs.

Au lieu de faire cela, nous pouvons utiliser **un produit scalaire de la matrice de poids et du vecteur de caractéristiques**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ElKdT7LHxgrZFZgiI2r4lg.png)

Le produit scalaire de la matrice de poids et du vecteur représentant les caractéristiques de l'image d'entrée nous donnera la valeur de somme que nous recherchons.

Nous pouvons soit définir la matrice de poids comme un vecteur ligne et utiliser l'équation

```
W . x + b
```

ou nous pouvons prendre la matrice de poids comme un vecteur colonne et ensuite faire une transposée pour le produit scalaire.

```
transpose(W) . x + b
```

Ici, nous allons opter pour la deuxième option. Nous considérons la matrice de poids comme ayant la forme `12288-par-1` pour une seule image. Dans le but de la transformation linéaire, nous faisons la transposée de la matrice de poids avant de faire un produit scalaire avec le vecteur de caractéristiques.

Pour l'instant, sachez simplement que nous voulons que les valeurs de poids par image soient disposées sous la forme d'une seule colonne plutôt que de lignes. Cela rendra les calculs beaucoup plus faciles à l'avenir.

Il en va de même pour les caractéristiques d'entrée. Nous voulons qu'elles soient disposées en colonnes.

#### Alimentation de l'ensemble du jeu d'entraînement

Nous ne voulons pas vraiment traiter une image à la fois, car cela serait trop lent.

Idéalement, nous voulons faire une seule passe avant sur notre modèle (c'est-à-dire le seul neurone ici) et obtenir des prédictions pour l'ensemble du jeu d'entraînement. Tout en une seule fois !

Nous pouvons y parvenir en utilisant l'équation que nous avons examinée précédemment :

```
transpose(W) . X + b
```

**Note :** `_X_` représente une matrice contenant toutes nos images et `**x**` représente un seul vecteur d'image.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DwTuChaiToN9qnhPi4cDVg.png)
_Transformation linéaire sur l'ensemble du jeu de données de m exemples en une seule fois._

![Image](https://cdn-media-1.freecodecamp.org/images/1*GwF4WdSueEOLWOcsQ47WAw.png)
_Dimensions des matrices impliquées dans nos calculs_

Remarquez le changement de notations dans l'équation. Nous utilisions auparavant le petit `**x**` pour désigner les caractéristiques d'une seule image.

Puisque nous traitons l'ensemble de notre jeu de données en une seule fois, nous sommes passés à la notation capitale italique `_X_` qui représente l'ensemble du jeu de données et comme mentionné dans la figure ci-dessus, il est de dimension `12288-par-m` où chaque image se compose de 12288 caractéristiques et il y a `m` exemples au total.

Regardons le code pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IBzoDHrXF-pt6oHjlguTow.png)

La fonction `forward_propagate` est celle qui fait tout le travail pour nous. Nous obtenons d'abord le nombre d'exemples (ceci n'est pas utilisé ici, mais je l'ai mis juste pour montrer que la deuxième dimension représente le nombre d'exemples).

Selon l'algorithme que nous avons discuté jusqu'à présent, nous effectuons d'abord une transformation linéaire sur la matrice d'entrée `_X_`, qui représente notre jeu de données d'images.

Ensuite, nous appliquons la fonction d'activation sigmoïde sur la matrice résultante (vecteur dans ce cas) et obtenons les valeurs d'activation non linéaires appliquées par le neurone.

Nous avons initialisé un jeu de données aléatoire ici et l'avons utilisé pour montrer l'exécution et la sortie de la fonction `forward_propagate` ci-dessus.

### Faisons une prédiction ?

Maintenant que nous avons défini la structure de notre neurone et le calcul qu'il effectue sur les caractéristiques de l'image, nous sommes prêts à faire quelques classifications réelles avec notre modèle.

Mais, avant de faire cela, nous devons avoir une sorte de mesure pour voir à quel point notre modèle se comporte réellement sur l'ensemble de test.

Regardons le code qui calcule la précision de l'ensemble de test des prédictions de notre modèle. C'est la métrique principale que nous allons utiliser tout au long du reste de notre article pour évaluer les performances de notre modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-5RToiNDgZCZqKH2JGQ8QQ.png)

C'est le code pour mesurer la précision de notre modèle dans la tâche de classification chat vs chien (ensemble de test). Il s'avère qu'un modèle non entraîné — nous avons initialisé aléatoirement les poids et les valeurs de biais — atteint presque 50% de précision. Cela est attendu d'un échantillonneur aléatoire, car il s'agit d'une tâche de classification à 2 classes. Si nous choisissons une valeur dans [0,1] de manière aléatoire, il y a une probabilité de 50% que nous obtenions la bonne valeur.

La question qui se pose maintenant est, comment pouvons-nous améliorer notre modèle ?

Nous pouvons améliorer notre modèle par un algorithme appelé la **Descente de Gradient**. Allons de l'avant et voyons en quoi consiste cet algorithme et comment il peut nous aider à améliorer notre modèle.

### Descendons la colline ?

Le but de l'algorithme de descente de gradient est de minimiser la fonction de coût afin que notre modèle basé sur les neurones puisse apprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P0qx-JPybIs5UBE0J6Y59A.jpeg)
_Source : [https://www.pinterest.com/pin/409053578638780708/?lp=true](https://www.pinterest.com/pin/409053578638780708/?lp=true" rel="noopener" target="_blank" title=")_

Qu'est-ce que cette **fonction de coût** ?

Notre modèle **apprend aussi bien** ?

Je sais. Nous devons faire un pas en arrière et d'abord passer en revue ces termes avant de nous lancer dans notre algorithme de descente de gradient. Alors, voyons exactement ce qu'est une fonction de coût.

### La performance de notre modèle ?

Afin de quantifier à quel point notre modèle se comporte bien dans la tâche de classification, nous avons la métrique de précision. Notre objectif ultime est que la précision de classification du modèle augmente.

Le seul ensemble de paramètres contrôlant la précision de notre modèle sont les poids et le biais de notre modèle basé sur les neurones.

La raison en est que ce sont les valeurs responsables de la transformation des caractéristiques de l'image d'entrée et qui nous aident à obtenir une prédiction quant à savoir si l'image est celle d'un chien ou d'un chat.

Nous avons vu précédemment qu'un ensemble aléatoire de poids et de valeurs de biais peut atteindre une précision de classification de 50% sur l'ensemble de test. Cela signifie qu'il y a beaucoup de place pour l'amélioration du modèle.

Mathématiquement, nous devrions être en mesure de modifier les poids et les valeurs de biais de manière à ce que la précision du modèle devienne la meilleure. Nous voulons ces ensembles parfaits de poids et de biais afin que le modèle classe correctement toutes les images de notre ensemble de test.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzJ3i1wTMsKIOhEO9E_8yQ.png)

Nous devons mettre à jour les paramètres du modèle afin qu'il obtienne la précision la plus élevée possible sur les données de test de notre tâche de classification.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KglMFPoQFHL_knOSpNxFUA.jpeg)

Considérons une fonction mathématique comme celle ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e4Bpx81HzTzLY5cj8scGXQ.png)

En calcul, les maxima (ou minima) de toute fonction peuvent être trouvés en

* **prenant la dérivée différentielle du premier ordre de la fonction** et en l'égalisant à 0. Le point trouvé de cette manière peut être le point de maximum ou de minimum.
* Ensuite, nous substituons ces valeurs (le point que nous venons de trouver) dans la **dérivée différentielle du second ordre** de la fonction et si la valeur est positive, c'est-à-dire > 0, alors ce(s) point(s) représente(nt) le(s) point(s) de minima locaux, sinon les maxima locaux.

Si nous regardons le graphe de calcul de notre modèle basé sur les neurones pour une image composée de seulement 2 caractéristiques, il ressemble à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tuyubpz2kR0axX3omNAkMQ.png)

La valeur finale que nous obtenons est une valeur réelle entre 0 et 1 et nous l'utilisons pour faire une prédiction quant à savoir si l'image est celle d'un chien ou d'un chat.

Considérons les valeurs de sortie suivantes par le modèle sur la même image de temps en temps :

```
0.520.560.610.670.780.800.850.890.98
```

En regardant ces valeurs pour la même image, vous diriez que le modèle devient de plus en plus confiant que l'image appartient en fait à celle d'un chat (les valeurs > 0,5 sont considérées comme des images de chat dans l'implémentation actuelle. C'est vraiment à vous de voir comment vous voulez structurer vos données.)

Bien que le modèle devienne de plus en plus confiant dans ses prédictions, la prédiction réelle reste la même, c'est-à-dire un chat. Pour toutes ces valeurs, la prédiction finale du modèle est un chat.

Cela met clairement en évidence **un gros problème avec l'utilisation de la précision comme mesure d'optimisation pour obtenir les poids et biais optimaux du modèle**.

Nous aurions pu modéliser une fonction centrée autour de la précision et sa maximisation aurait été notre objectif.

Le nombre d'images correctement classées n'est pas une fonction lisse des poids et des biais dans le réseau. Pour la plupart, **apporter de petites modifications aux poids et aux biais ne provoquera aucun changement du tout dans le nombre d'images d'entraînement classées correctement**.

Cela rend difficile de déterminer comment modifier les poids et les biais pour obtenir de meilleures performances. Cela est visible à partir de l'exemple que nous venons de considérer.

Bien que le modèle devenait plus confiant, la précision ne reflétera jamais cela et donc, le modèle ne fera pas ce genre d'améliorations.

Ce dont nous avons besoin à la place, c'est **d'une mesure proxy** qui est quelque peu liée à la précision et qui est également une fonction lisse des poids et du biais.

### Entrez : La fonction de perte ?

Il s'agit d'un problème de classification binaire. Cela signifie que nous ne pouvons avoir que deux classes : 0 ou 1.

Dans un monde parfait, notre modèle donnerait un 0 pour un chien et un 1 pour un chat et dans ce cas, il atteindrait une précision de 100%. Donner un 0 pour un chien ou un 1 pour un chat montrerait la confiance à 100% du modèle dans ses prédictions. Cela ne se produit pas vraiment dans le scénario du monde réel (du moins pas encore !).

Notre modèle non entraîné semblera confus au début. Il ne sera pas trop sûr de ses prédictions. Il pourrait donc donner des valeurs comme `0.51, 0.49, 0.514`, etc. Juste parce que le seuil est franchi et que la prédiction **s'avère être correcte**, cela ne signifie pas que notre modèle est bien entraîné.

De la discussion ci-dessus, une chose est claire. Nous devons réduire l'écart entre la sortie du modèle et la sortie réelle. Moins l'écart est grand, mieux notre modèle est dans ses prédictions et plus il montre de confiance lors de la prédiction.

Cela signifie que pour une image de chien, nous voulons que notre modèle donne des valeurs aussi proches de 0 que possible et de même, pour les images de chat, nous voulons que notre modèle donne des valeurs aussi proches de 1 que possible.

C'est ce qui nous conduit à ce que l'on appelle le **terme de perte/erreur/coût** pour notre modèle. La fonction de perte modélise essentiellement la différence entre la prédiction de notre modèle et la sortie réelle. Idéalement, si ces deux valeurs sont éloignées, la valeur de perte ou la valeur d'erreur devrait être plus élevée. De même, si ces deux valeurs sont plus proches, la valeur d'erreur devrait être faible.

Étant donné ce type de fonction d'erreur comme proxy pour la performance de notre modèle, nous aimerions **minimiser la valeur de cette fonction de perte**.

Que pensez-vous ? La fonction de perte est-elle simplement la distance entre `y_predicted` et `y_actual` ?

```
|y_actual - y_predicted|
```

Eh bien, nous pouvons utiliser cette fonction de perte spécifique pour chaque image et faire la moyenne de la perte pour l'ensemble du jeu d'entraînement pour obtenir la perte pour l'ensemble de l'époque. Mais, cela n'est pas vraiment approprié.

La fonction de perte ci-dessous est connue sous le nom de **fonction de perte de différence absolue**

![Image](https://cdn-media-1.freecodecamp.org/images/1*d030zdG7e43z4xFCvxO4LQ.png)

Cependant, il est logique de considérer cette fonction de perte pour la minimisation, car à la fin de la journée, c'est la mesure proxy exacte dont nous avons parlé plus tôt qui nous permet de savoir à quel point notre modèle se comporte bien.

**J** est une notation courante pour la fonction de perte et **** représente les paramètres de notre modèle, c'est-à-dire les poids et les biais.

Mais, au lieu de prendre cette fonction comme notre fonction de perte, nous finissons par considérer la fonction suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Z1EmO0V--Um338O4gwhKw.png)

Cette fonction est connue sous le nom d'**erreur quadratique**. Nous avons simplement pris la différence entre la sortie réelle `y` et la sortie prédite `y^` et nous avons élevé cette valeur au carré (d'où le nom) et divisé par 2.

L'une des principales raisons de préférer l'erreur quadratique à l'erreur absolue est que l'erreur quadratique est **différentiable partout**, tandis que l'erreur absolue ne l'est pas (sa dérivée est indéfinie à 0).

Pour optimiser l'erreur quadratique, vous pouvez simplement mettre sa dérivée égale à 0 et résoudre ; pour optimiser l'erreur absolue, il faut souvent des techniques plus complexes.

De plus, les avantages de la mise au carré incluent :

* La mise au carré **donne toujours une valeur positive**, donc la somme ne sera pas nulle. Nous parlons de somme ici parce que nous allons additionner les valeurs de perte ou d'erreur pour chaque image dans notre ensemble de données d'entraînement et ensuite nous allons faire la moyenne pour trouver la perte pour l'ensemble du lot d'exemples d'entraînement.
* La mise au carré met l'accent sur les différences plus grandes — une caractéristique qui s'avère à la fois bonne et mauvaise (pensez à l'effet des valeurs aberrantes).

Considérons les graphiques de l'erreur absolue et des erreurs quadratiques respectivement ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xUGYWm3HBpYqqjZKHE0akQ.png)
_Erreur absolue. Nous pouvons avoir y^ — 0 ou y^ — 1 car l'étiquette réelle peut être 0 ou 1. Donc, deux lignes sont représentées ci-dessus._

![Image](https://cdn-media-1.freecodecamp.org/images/1*msqMb-F25hH6_fz0jEKfqA.png)
_De même, nous avons (y^ — 1) ou (y^) comme fonctions d'erreur quadratique._

Pour l'instant, oubliez le fait que nous appliquons une fonction d'activation sigmoïde à la sortie du neurone avant de faire des prédictions en l'utilisant. Alors, il n'y aurait pas de valeur minimale ou maximale définie pour l'erreur absolue comme il est clair à partir du graphique de cette fonction.

Mais, si nous regardons le graphique parabolique pour la fonction quadratique, nous pouvons voir la pointe inférieure qui est le minimum de cette fonction et cela se produit à ``= 0 ou 1 selon celui dont nous parlons. Mais, il y a un minimum bien défini pour cette fonction et donc elle est plus facile à optimiser.

C'est comme ça que je me sens maintenant après avoir travaillé sur cet article pendant si longtemps. J'espère que vous avez pu saisir tous les concepts importants que nous avons discutés jusqu'à présent. Il reste encore un long chemin à parcourir avant de conclure.

Vous pourriez vouloir faire une pause et revenir à l'article, car nous allons commencer avec l'algorithme de descente de gradient maintenant.

D'accord alors. J'espère que vous êtes de retour et prêt à continuer !

Définissons officiellement la fonction d'erreur que nous allons utiliser ici. Elle est connue sous le nom d'erreur quadratique moyenne et la formule est la suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xkb0tTBQu3_QodtbladJ-g.png)

Nous calculons l'erreur quadratique pour chaque image dans notre ensemble d'entraînement, puis nous **trouvons la moyenne** de ces valeurs et cela représente l'erreur globale du modèle sur notre ensemble d'entraînement.

### Minimisation de la fonction de perte 

Considérons l'exemple d'une seule image avec seulement 2 caractéristiques comme avant. Deux caractéristiques signifie que nous avons 2 valeurs de poids correspondantes et une valeur de biais. Au total, nous avons 3 paramètres pour notre modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eTKSIHxNRfqIF5nptyUmXA.png)

Nous voulons trouver des valeurs pour nos poids et le biais qui minimisent la valeur de notre fonction de perte. Puisque cela est une équation à plusieurs variables, cela signifie que nous devrons traiter les dérivées partielles de la fonction de perte correspondant à chacune de nos variables `w1, w2 et b`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z9b6gTqEKEL7cFv9Zs7ycA.png)

Cela peut sembler simple à faire car nous n'avons que 3 variables différentes.

Cependant, si nous considérons la tâche à accomplir, c'est-à-dire la classification d'images de chats vs chiens en utilisant notre modèle basé sur un seul neurone, nous avons `12288` poids.

Faire de l'optimisation multivariée avec autant de variables est inefficace sur le plan computationnel et n'est pas réalisable. Par conséquent, nous avons recours à des alternatives et des approximations.

**Fait amusant :** un modèle de réseau de neurones profond typique a des millions de poids et de biais ?.

Nous sommes prêts à apprendre l'algorithme de descente de gradient maintenant.

S'il y a un algorithme qui est utilisé dans presque tous les modèles d'apprentissage automatique, c'est la **Descente de Gradient**.

C'est l'algorithme qui aide notre modèle à **apprendre**. Sans la capacité d'apprentissage, tout modèle d'apprentissage automatique est essentiellement aussi bon qu'un modèle de devinette aléatoire.

C'est la capacité d'apprentissage accordée par l'algorithme de descente de gradient qui rend les modèles d'apprentissage automatique et d'apprentissage profond si cool.

Le but de cet algorithme est de minimiser la valeur de notre fonction de perte (surprise, surprise !). Et nous voulons le faire de manière efficace.

Comme discuté précédemment, le moyen le plus rapide serait de trouver les dérivées du second ordre de la fonction de perte par rapport aux paramètres du modèle. Mais, cela est coûteux en calcul.

L'essentiel de l'algorithme de descente de gradient est le processus d'atteindre la valeur d'erreur la plus basse. [Wikipedia](https://en.wikipedia.org/wiki/Gradient_descent#An_analogy_for_understanding_gradient_descent) a une excellente analogie pour l'algorithme de descente de gradient :

L'intuition de base derrière la descente de gradient peut être illustrée par un scénario hypothétique.

Une personne est coincée dans les montagnes et essaie de descendre (c'est-à-dire, essaie de trouver les minima). Il y a un brouillard épais de sorte que la visibilité est extrêmement faible. Par conséquent, le chemin descendant de la montagne n'est pas visible, donc ils doivent utiliser des informations locales pour trouver les minima.

Ils peuvent utiliser la méthode de la descente de gradient, qui implique de regarder la raideur de la colline à leur position actuelle, puis de procéder dans la direction avec la descente la plus raide (c'est-à-dire, en descente).

S'ils essayaient de trouver le sommet de la montagne (c'est-à-dire, les maxima), alors ils procéderaient dans la direction avec l'ascension la plus raide (c'est-à-dire, en montée). En utilisant cette méthode, ils finiraient par trouver leur chemin.

Cependant, supposons également que la raideur de la colline n'est pas immédiatement évidente avec une simple observation, mais qu'elle nécessite plutôt un instrument sophistiqué pour la mesurer, que la personne a à ce moment-là.

Il faut beaucoup de temps pour mesurer la raideur de la colline avec l'instrument, donc ils devraient minimiser leur utilisation de l'instrument s'ils veulent descendre de la montagne avant le coucher du soleil.

La difficulté est alors de choisir la fréquence à laquelle ils doivent mesurer la raideur de la colline afin de ne pas sortir de la piste.

Dans cette analogie,

* la personne représente notre **algorithme d'apprentissage**, et
* le chemin pris pour descendre de la montagne représente la **séquence de mises à jour des paramètres** que notre modèle explorera éventuellement.
* La raideur de la colline représente la **pente de la surface d'erreur** à ce point.
* L'instrument utilisé pour mesurer la raideur est la **différentiation** (la pente de la surface d'erreur peut être calculée en prenant la dérivée de la fonction d'erreur quadratique à ce point). C'est l'approximation que nous faisons lorsque nous appliquons la descente de gradient. Nous ne connaissons pas vraiment le point minimum, mais **nous connaissons la direction** qui nous mènera aux minima (locaux ou globaux) et nous faisons un pas dans cette direction.
* La direction que la personne choisit de suivre est alignée avec le gradient de la surface d'erreur à ce point.
* La quantité de temps qu'ils voyagent avant de prendre une autre mesure est le **taux d'apprentissage de l'algorithme**. C'est essentiellement la taille du pas que notre modèle (ou la personne descendant la colline) décide de prendre chaque fois.

Pour une compréhension plus approfondie et les mathématiques derrière l'algorithme de descente de gradient, je vous recommande de consulter :

[**Gradient Descent: All You Need to Know**](https://hackernoon.com/gradient-descent-aynk-7cbe95a778da)  
[_Gradient Descent is THE most used learning algorithm in Machine Learning. This post shows you almost everything you need to know..._hackernoon.com](https://hackernoon.com/gradient-descent-aynk-7cbe95a778da)

### La descente de gradient trouve-t-elle toujours le minimum global ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*uEGOBMCM78L7ah2Ahc3TeA.png)
_Source : [https://www.oreilly.com/](https://www.oreilly.com/" rel="noopener" target="_blank" title=")_

C'est l'une des figures les plus courantes associées à la descente de gradient et elle montre que notre fonction d'erreur est une fonction convexe lisse. Elle montre également que l'algorithme de descente de gradient trouve le minimum global.

La fonction de perte que nous avons définie est connue sous le nom de **fonction de perte quadratique moyenne**. La fonction prend deux paramètres : `` qui est la prédiction du modèle pour une entrée donnée `x` et ensuite nous avons `y` qui est l'étiquette réelle correspondant à cette entrée.

Clairement, notre fonction est une fonction convexe par rapport à la prédiction ``.

Cependant, si vous regardez l'équation développée de la fonction de perte que nous avons écrite il y a quelques paragraphes, vous verrez que la valeur de prédiction n'est pas quelque chose que nous pouvons contrôler directement.

Nous pouvons simplement contrôler les poids du modèle et la valeur de biais, c'est-à-dire les paramètres du modèle, et ils contrôlent à leur tour la prédiction.

Bien que la fonction de perte quadratique moyenne soit convexe par rapport à la prédiction du modèle ``, la propriété de convexité qui nous intéresse vraiment est par rapport aux paramètres du modèle.

Nous voulons que notre fonction de perte soit une fonction convexe lisse des poids de notre modèle.

Puisqu'un modèle typique d'apprentissage automatique a des millions de poids (notre modèle en a 12288 et il s'agit d'un seul neurone), notre fonction de perte peut contenir plusieurs points de minima locaux et la descente de gradient peut ne pas nécessairement trouver le minimum global.

Tout dépend des **tailles de pas que le modèle fait**, c'est-à-dire le taux d'apprentissage, de la durée d'entraînement du modèle et de la quantité de données d'entraînement dont dispose notre modèle.

### Laissez les gradients circuler 

D'accord. Donc, à ce stade, nous savons que ce sont les deux équations par lesquelles notre modèle apprendra à mieux classer les images de chats et de chiens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5BMHYemAg2fVAnQBbJtedg.png)

Le `` représente le taux d'apprentissage pour notre algorithme de descente de gradient, c'est-à-dire la taille du pas pour descendre la colline. Le(s) terme(s) à côté de `` représente(nt) les **gradients** de la fonction de perte correspondant aux poids et au biais respectivement.

La question ici est, comment calculons-nous réellement ces gradients ?

Regardons notre graphe de calcul pour le modèle simple avec lequel nous avons travaillé jusqu'à présent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p9B9v21-GWh3h1VmZJ1xOQ.png)

Nous savons déjà comment les activations circulent dans le sens direct. Nous prenons les caractéristiques de l'image d'entrée, nous les transformons linéairement, nous appliquons l'activation sigmoïde sur la valeur résultante, et enfin nous avons notre activation que nous utilisons ensuite pour faire une prédiction.

Ce que nous allons examiner dans cette section est le flux des gradients le long de la ligne rouge dans le diagramme ci-dessus par un processus connu sous le nom de **rétropropagation**.

Ne vous inquiétez pas !

À la fin de cette section, vous aurez une compréhension claire de ce que la rétropropagation fait pour nous et des mathématiques qui la sous-tendent (au moins pour notre modèle spécifique).

> La rétropropagation est essentiellement la règle de la chaîne du calcul appliquée aux graphes de calcul.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_KMMFvRP5X9kC59brI0ykw.png)

Supposons que nous voulions trouver la dérivée partielle de la variable `y` par rapport à `x` dans la figure ci-dessus. Nous ne pouvons pas le trouver directement car il y a 3 autres variables impliquées dans le graphe de calcul.

```
x --> (Un certain calcul) --> AA --> (Un certain calcul) --> BB --> (Un certain calcul) --> CC --> (Un certain calcul) --> y
```

Nous faisons donc ce processus de manière itérative en allant **en arrière** dans le graphe de calcul.

Nous trouvons d'abord la dérivée partielle de la sortie `y` par rapport à la variable `C`. Ensuite, nous utilisons la [règle de la chaîne](https://en.wikipedia.org/wiki/Chain_rule) du calcul et nous déterminons la dérivée partielle par rapport à la variable `B` et ainsi de suite jusqu'à ce que nous obtenions la dérivée partielle que nous recherchons.

C'est tout ce qu'il y a à la rétropropagation.

Évidemment, trouver réellement les dérivées dans un graphe de calcul est quelque chose qui est délicat et qui effraie la plupart des gens. Cependant, nous avons un modèle relativement simple ici et il est assez facile de faire de la rétropropagation ici. Donc, sans plus attendre, passons aux mathématiques de la rétropropagation sur notre graphe de calcul.

#### Étape 1 : dJ/d

L'équation finale pour notre fonction de perte est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lex7D1q4YLvVDytRBqLXJA.png)

La dérivée partielle de la fonction de perte par rapport à l'activation de notre modèle `` est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uyQtipJwArqLBJhwD3u_GQ.png)

C'était assez facile !

Passons à une étape **en arrière et calculons notre prochaine dérivée partielle**. Cela nous rapprochera d'un pas des gradients réels que nous voulons calculer.

#### Étape 2 : dJ/dA

C'est le point où nous appliquons la règle de la chaîne que nous avons mentionnée précédemment. Donc, pour calculer la dérivée partielle de la fonction de perte par rapport à la sortie transformée linéairement, c'est-à-dire la sortie de notre modèle **avant** d'appliquer l'activation sigmoïde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QkfTUtyhc0Hj75_uA0hIOQ.png)

La première partie de cette équation est la valeur que nous avions calculée à l'étape 1. Nous pouvons simplement l'utiliser ici.

La chose essentielle à calculer ici est la dérivée partielle de la prédiction de notre modèle par rapport à la sortie transformée linéairement, également connue sous le nom de **logit**.

Regardons l'équation de la prédiction de notre modèle en termes de logit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*56NMarxBAbwGyJEye2M-NQ.png)

Nous avons simplement écrit la formule pour la fonction d'activation sigmoïde.

La dérivée de la sortie finale de notre modèle par rapport au logit signifie simplement la dérivée partielle de la fonction sigmoïde par rapport à son entrée. Regardons une dérivation de la dérivée ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oA-sBWiG8FmgNeEYpnAYFA.png)

C'est beaucoup de mathématiques. Mais ce n'est que du calcul différentiel de base ici.

Si vous n'êtes pas intéressé par les mathématiques et la dérivation de cela, vous pouvez simplement regarder les valeurs finales de chacune de ces dérivées partielles. Vous en aurez besoin pour construire votre modèle à partir de zéro.

En continuant, nous pouvons simplifier davantage cette équation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5iQufIdGbgzcRGAT8wR3HA.png)

En substituant cette valeur dans notre équation précédente, nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ft1cdjtiR2tDsBbanFu1Ng.png)

Ouf ! C'était beaucoup de mathématiques, n'est-ce pas ?

Mais nous n'avons pas encore terminé. Il reste encore une étape à franchir dans cet algorithme de rétropropagation.

Nous devons encore trouver les dérivées partielles par rapport aux poids et au biais.

Passons à la suite et voyons comment nous pouvons faire cela.

#### Étape 3 : dJ / dW et dJ / db

Nous avons besoin de la dérivée partielle de la fonction de perte correspondant à **chacun des poids**. Mais puisque nous avons recours à la **vectorisation**, nous pouvons tout trouver en une seule fois. C'est pourquoi nous avons utilisé la notation capitale italique `_W_` au lieu de `w1 ou w2 ou tout autre poids individuel`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tV5DsdbJPAmqjbCD5cSlKQ.png)

Nous montrerons la dérivation pour les poids et laisserons la partie biais pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wJQi2eDpfhaglkvbqEXcLA.png)

### Codons ! ?

Mettons toutes les mathématiques que nous avons apprises dans la section précédente dans une fonction simple qui prend le vecteur d'activation `A` et le vecteur des étiquettes de sortie réelles `Y` et calcule les gradients de notre perte par rapport aux poids et au biais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YXA2wWNqRSIYvkFm5coFFQ.png)

* Le terme `dY_hat` représente la dérivée partielle de notre fonction de perte par rapport à la valeur de sortie finale `` et comme montré dans la section précédente, cette valeur est `A — Y`.
* Ensuite, nous avons `dA` qui est la dérivée partielle par rapport à la sortie transformée linéairement, `A`.
* Le terme suivant est `dW` et nous voyons que nous avons fait une multiplication de matrices ici pour obtenir cette valeur. Nous divisons par `m` pour obtenir le gradient moyen sur l'ensemble du jeu d'entraînement. C'est standard. Mais pourquoi avons-nous fait une multiplication de matrices ici ?

Dans la dernière figure de la section précédente, nous voyons que `dJ/dW = dJ/dA * X`.

Regardons de plus près les dimensions des deux quantités impliquées ici. Notre matrice `X` serait `12288-par-m` où chaque image a `12288` caractéristiques et nous avons `m` échantillons d'entraînement.

Les dimensions de la quantité `dJ/dA` seraient les mêmes que `A` et ce n'est rien d'autre qu'une seule valeur réelle par échantillon d'entraînement, c'est-à-dire `1-par-m`.

De plus, la dimension de la quantité `dJ/dW` devrait être la même que `W` car finalement, nous devons soustraire les gradients des valeurs de poids originales. Donc, les deux matrices doivent avoir les mêmes dimensions.

La matrice `W` a une dimension de `12288-par-1`. Donc, nous avons besoin que `dJ/dW` soit également `12288-par-1`. Pour que cela se produise :

![Image](https://cdn-media-1.freecodecamp.org/images/1*L80MmSmMxvBaGd3zx1cFcg.png)

J'espère que cela clarifie pourquoi nous avons écrit le code comme `np.matmul(X, dZ.T)` avant de prendre la moyenne.

Regroupons tout cela dans une seule fonction complète qui fait les choses suivantes :

* Prend l'entrée X et les paramètres du modèle W et b et applique la propagation avant sur l'entrée.
* Fait la rétropropagation pour calculer les gradients.
* Applique la descente de gradient sur les paramètres du modèle.
* Calcule la perte sur le jeu de données de validation pour mesurer la performance du modèle et nous utilisons cela pour voir si le modèle généralise bien ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4UHcq51DrFL9l4T1iVi0OA.png)

Nous avons cette fonction combinée qui fait la propagation avant et arrière pour nous. Donc, un seul appel à cette fonction et notre modèle aurait traité et appris une fois à partir de l'ensemble de notre jeu d'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-oIUF5ZRoQbsH7cAZQOqqw.png)

C'est la fonction principale qui fait essentiellement le même processus mais plusieurs fois.

Exposer le modèle plusieurs fois au jeu de données d'entraînement et le modèle apprend quelque chose de nouveau à chaque fois.

Ainsi, ces itérations sont connues sous le nom d'**époques** et nous avons cette fonction `model` qui, pour chaque époque, parcourt l'ensemble des étapes fournies précédemment.

Enfin, nous sommes à l'étape où nous pouvons entraîner notre modèle et voir combien un seul neurone peut réellement apprendre en ce qui concerne notre tâche de classification d'images de chats vs chiens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K5HpDPgWyFPlOabVkEyVSg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*xn1f8_qdFHMtrR76n-TUDA.png)
_Super !_

Cela signifie que sur l'**ensemble de validation/test non vu**, notre modèle est capable de prédire si l'image est celle d'un chat ou d'un chien avec une précision de 61%. C'est génial si vous me le demandez, car nous avons pu obtenir un gain de 10% par rapport à un devin aléatoire simplement en utilisant un **seul neurone**.

Juste pour le plaisir, j'ai tracé les pertes d'entraînement et de validation pour l'entraînement du modèle sur les 5000 époques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8wpjij06mca2fCKLFIL0SQ.png)

Les pertes d'entraînement et de validation diminuent régulièrement au fil du temps.

Une dernière chose avant de vous laisser jouer avec le code. Fournissons une image personnalisée à notre modèle, une image qui ne fait pas partie de notre jeu de données et voyons si elle est capable de prédire correctement si l'image est un chat ou un chien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JEfTr5PybQUvsRXBoaysuw.png)

Voilà ! C'est correct. En effet, c'est un chat.

Pour le code complet, veuillez consulter :

[**edorado93/Power-Of-A-Neuron**](https://github.com/edorado93/Power-Of-A-Neuron)  
[_Cats vs Dogs Image Classification using Logistic Regression - edorado93/Power-Of-A-Neuron_github.com](https://github.com/edorado93/Power-Of-A-Neuron)

Veuillez recommander cet article si vous pensez qu'il peut être utile pour quelqu'un ! De plus, n'hésitez pas à signaler les erreurs éventuelles dans les calculs ou le code lui-même. Cela serait grandement apprécié.