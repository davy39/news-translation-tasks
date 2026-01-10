---
title: 'Deep Learning pour les Développeurs : Outils que vous pouvez utiliser pour
  coder des Réseaux de Neurones dès le Jour 1'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T05:21:31.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_9GcuoDUbWGTSFjdIkduA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Deep Learning pour les Développeurs : Outils que vous pouvez utiliser
  pour coder des Réseaux de Neurones dès le Jour 1'
seo_desc: 'By Emil Wallner

  The current wave of deep learning took off five years ago. Exponential progress
  in computing power followed by a few success stories created the hype.

  Deep learning is the technology that drives cars, beats humans at Atari games, and
  ...'
---

Par Emil Wallner

La vague actuelle de deep learning a décollé il y a cinq ans. Des progrès exponentiels en puissance de calcul, suivis de quelques histoires à succès, ont créé l'engouement.

Le deep learning est la technologie qui conduit les voitures, bat les humains aux jeux Atari et diagnostique le cancer.

![Image](https://cdn-media-1.freecodecamp.org/images/wiSIAggUyeRJ3d80mJ6NC3pmsyAUq-5kjev9)
_Photo par [Unsplash](https://unsplash.com/photos/y3FkHW1cyBE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Arif Wahid</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Quand j'ai commencé à apprendre le deep learning, j'ai passé deux semaines à faire des recherches. J'ai sélectionné des outils, comparé des services cloud et recherché des cours en ligne. En rétrospective, j'aurais aimé pouvoir construire des réseaux de neurones dès le premier jour. C'est ce que cet article vise à faire.

Vous n'avez besoin d'aucun prérequis. Cependant, une compréhension de base de [Python](https://www.codecademy.com/tracks/python), de la [ligne de commande](https://www.codecademy.com/learn/learn-the-command-line) et du [Jupyter notebook](https://www.youtube.com/watch?v=HW29067qVWk) sera utile.

Le deep learning est une branche de l'apprentissage automatique. Il s'est avéré être une méthode efficace pour trouver des motifs dans des [données brutes](https://ml4a.github.io/images/figures/mnist-input.png), telles qu'une image ou un son.

Supposons que vous souhaitiez faire une classification d'images de chats et de chiens. Sans programmation spécifique, il trouve d'abord les contours dans les images. Ensuite, il construit des motifs à partir de ceux-ci. Ensuite, il détecte les nez, les queues et les pattes. Cela permet au réseau de neurones de faire la classification finale des chats et des chiens.

Cependant, il existe de meilleurs algorithmes d'apprentissage automatique pour les données structurées. Par exemple, si vous avez une feuille Excel ordonnée avec des données consommateurs et que vous souhaitez prédire leur prochaine commande. Vous pouvez alors prendre une approche [traditionnelle](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) et utiliser des algorithmes de [machine learning plus simples](http://1.bp.blogspot.com/-ME24ePzpzIM/UQLWTwurfXI/AAAAAAAAANw/W3EETIroA80/s1600/drop_shadows_background.png).

### Logique de Base

Imaginez une machine avec des roues dentées ajustées aléatoirement = ❄. Les roues sont empilées en couches et elles s'impactent toutes les unes les autres. Initialement, la machine ne fonctionne pas. Les roues sont ajustées aléatoirement et elles doivent toutes être réglées pour donner la sortie correcte.

Un ingénieur examinera alors toutes les roues et marquera celles qui causent l'erreur. Il commence par la dernière couche de roues, le résultat de toutes les erreurs combinées. Une fois qu'il connaît les erreurs que la dernière couche cause, il travaille à rebours. De cette façon, il peut calculer combien chaque roue contribue à l'erreur. Nous appelons ce processus **rétropropagation**.

L'ingénieur ajuste ensuite chaque roue en fonction de l'erreur qu'elle a causée et fait fonctionner la machine à nouveau. Il continue à faire fonctionner la machine, calcule les erreurs et ajuste chaque roue. Il reste dans cette routine jusqu'à ce que la machine donne la sortie correcte.

![Image](https://cdn-media-1.freecodecamp.org/images/YxuSQz5AhCbEoVT4-IDEBbesFNptm382snxh)

Les réseaux de neurones fonctionnent de la même manière. Ils connaissent l'entrée et la sortie et ajustent les roues pour trouver la corrélation entre les deux. Étant donné une entrée, ils ajustent les roues pour prédire la sortie. Ils comparent ensuite les valeurs prédites avec les valeurs réelles.

Pour minimiser les erreurs, la différence est entre les valeurs prédites et les valeurs réelles. Le réseau de neurones ajuste les roues. Il ajuste les roues jusqu'à ce que la différence entre les valeurs prédites et les valeurs réelles soit aussi faible que possible.

Minimiser l'erreur de manière optimale est la **descente de gradient**. Les erreurs sont calculées avec la fonction `erreur / coût`.

### Un Réseau de Neurones Artificiels Peu Profond

Beaucoup pensent aux réseaux de neurones artificiels comme des répliques numériques de notre [néocortex](https://en.wikipedia.org/wiki/Neocortex). Ce n'est pas vrai.

Nous ne savons pas assez de choses sur notre cerveau pour faire cette affirmation. C'était une source d'inspiration pour Frank Rosenblatt, l'inventeur des réseaux de neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/oqskTIEj4LPhqdN2LaE-6Xey64v2Q1C3cNDT)

Jouez avec le [Simulateur de Réseau de Neurones](https://www.mladdict.com/neural-network-simulator) pendant une ou deux heures pour avoir une intuition.

Nous allons commencer par implémenter un simple réseau de neurones pour nous familiariser avec la syntaxe dans [TFlearn](http://tflearn.org/). Un problème classique 101 pour commencer est l'[opérateur OR](https://msdn.microsoft.com/en-us/library/f355wky8.aspx). Bien que les réseaux de neurones soient mieux adaptés à d'autres types de données, c'est un bon problème pour comprendre comment cela fonctionne.

![Image](https://cdn-media-1.freecodecamp.org/images/T5c8Wq0fQkIioROwuUrD91XOdECSqVCVgW8H)

Tous les programmes de deep learning suivent la même logique de base :

* Il commence par inclure des bibliothèques, puis importer et nettoyer les données. Toutes les entrées sont traduites en [chiffres](https://ml4a.github.io/images/figures/mnist-input.png), qu'il s'agisse d'images, d'audio ou de données sensorielles. Ces longues listes de nombres sont l'entrée de nos réseaux de neurones.
* Maintenant, concevez votre réseau de neurones. Choisissez le type et la quantité de couches à avoir dans votre réseau.
* Ensuite, il entre dans le processus d'apprentissage. Il connaît les valeurs d'entrée et de sortie et recherche la corrélation entre elles.
* La dernière étape vous donne une prédiction de votre réseau de neurones entraîné.

Voici le code pour notre réseau de neurones :

**Sortie**

```
Training Step: 2000  | total loss: 0.00072 | time: 0.002s| SGD | epoch: 2000 | loss: 0.00072 -- iter: 4/4Testing OR operator0 or 0: [[ 0.04013482]]0 or 1: [[ 0.97487926]]1 or 0: [[ 0.97542077]]1 or 1: [[ 0.99997282]]
```

**Ligne 1** Les lignes commençant par # sont des commentaires. Ils sont utilisés pour expliquer le code.

**Ligne 2** Inclure la bibliothèque TFlearn. Cela nous permet d'utiliser des fonctions de deep learning de [Tensorflow](https://www.tensorflow.org/) de Google.

**Lignes 5-6** Les données du tableau sont stockées dans des listes. Le point à la fin de chaque nombre mappe chaque entier en flottants. Il stocke des nombres avec des valeurs décimales qui rendent les calculs précis.

**Ligne 9** Initialiser le réseau de neurones et spécifier la dimension ou la forme de nos données d'entrée. Chaque opérateur OR vient en paire et a donc la forme de 2. None est une valeur par défaut et représente la taille du lot.

**Ligne 10** Notre couche de sortie. La fonction d'activation mappe la sortie dans la couche entre un intervalle. Dans notre cas, nous utilisons une fonction Sigmoid qui mappe la valeur entre 0 et 1.

[Lire plus](http://tflearn.org/layers/core/) sur les lignes 9 et 10.

**Ligne 11** Appliquer la [régression](http://tflearn.org/layers/estimator/). L'[optimiseur](http://tflearn.org/optimizers/) choisit quel algorithme minimiser la fonction de coût. Le taux d'apprentissage décide de la rapidité de modification du réseau de neurones, et la variable de perte décide comment calculer les erreurs.

**Ligne 14** Sélectionne quel réseau de neurones utiliser. Il est également utilisé pour spécifier où stocker les journaux d'entraînement.

**Ligne 15** Entraîne votre réseau de neurones et modèle. Sélectionnez vos données d'entrée (OR) et les vraies étiquettes (Y_truth). Les époques déterminent combien de fois exécuter toutes vos données à travers votre réseau de neurones. Si vous définissez `snapshot=True`, il validera le modèle après chaque époque.

**Lignes 18-22** Fait une prédiction avec votre modèle entraîné. Dans notre cas, il retourne la probabilité de retourner Vrai/1.

[Lire plus](http://tflearn.org/models/dnn/) sur les lignes 14-22.

**Étiquettes de sortie** Le premier résultat signifie que la combinaison [0.] & [0.] a une probabilité de 4% d'être vraie, et ainsi de suite. L'étape d'entraînement indique combien de lots vous avez entraînés.

Puisque les données peuvent tenir dans un lot, c'est la même chose que l'[Époque](https://medium.com/towards-data-science/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9). Si les données sont trop grandes pour la mémoire, vous devez diviser l'entraînement en morceaux. La perte mesure la somme des erreurs de chaque époque.

SGD signifie Descente de Gradient Stochastique et est une méthode pour minimiser la fonction de coût.

`Iter` affiche l'index de données actuel et la quantité totale d'éléments d'entrée.

Vous pouvez trouver la logique et la syntaxe ci-dessus dans presque tous les réseaux de neurones TFlearn. La meilleure façon de se familiariser avec le code est de le modifier et de créer quelques erreurs.

![Image](https://cdn-media-1.freecodecamp.org/images/IGUJu9SQOzqZmrvGki-RgLH2qrYBBHSIhUIL)
_La courbe de perte montre la quantité d'erreurs pour chaque étape d'entraînement_

Avec [Tensorboard](TensorBoard: Visualizing Learning), vous pouvez visualiser chaque expérience et construire une intuition pour voir comment chaque paramètre change l'entraînement.

Voici une suggestion de quelques exemples que vous pouvez exécuter. Je recommande de jouer avec pendant quelques heures pour se familiariser avec l'environnement et les paramètres de TFlearn.

**Expériences**

* Augmenter l'entraînement et les époques
* Essayez d'ajouter et de changer un paramètre pour chaque fonction de la documentation. Par exemple, `g = tflearn.fullyconnected(g, 1, activation='sigmoid')` devient `tflearn.fullyconnected(g, 1, activation='sigmoid', bias=False)`
* Ajoutez des entiers dans les données d'entrée
* Changez la forme dans la couche d'entrée
* Changez la fonction d'activation dans la couche de sortie
* Utilisez une méthode différente pour la descente de gradient
* Changez la façon dont le réseau de neurones calcule le coût
* Changez les X et Y en opérateurs logiques AND et NOT
* Changez les données de sortie en opérateurs logiques XOR. Par exemple, échangez le dernier Y_truth de [1.] à [0.]. Vous devez ajouter une couche dans votre réseau pour que cela fonctionne
* Faites-le apprendre plus vite
* Trouvez un moyen de faire en sorte que chaque étape d'apprentissage prenne plus de 0,1 seconde

### Getting Started

Python combiné avec Tensorflow est la pile la plus courante pour le deep learning.

TFlearn est un framework de haut niveau qui fonctionne sur Tensorflow.

Un autre framework courant est [Keras](https://keras.io/). C'est une bibliothèque plus robuste, mais je trouve la syntaxe de TFlearn plus propre et plus facile à comprendre.

Ils sont tous deux des frameworks de haut niveau qui fonctionnent sur Tensorflow.

Vous pouvez exécuter des réseaux de neurones simples sur le CPU de votre ordinateur. Mais la plupart des expériences prendront plusieurs heures, voire des semaines, à s'exécuter. C'est pourquoi la plupart utilisent des GPU modernes pour le deep learning, souvent via un service cloud.

La solution la plus facile pour les GPU cloud est [FloydHub](https://www.floydhub.com/). Si vous avez des compétences de base en ligne de commande, cela ne devrait pas prendre plus de 5 minutes pour configurer FloydHub.

[Utilisez la documentation de FloydHub](http://docs.floydhub.com/getstarted/quick_start/) pour installer l'outil de ligne de commande `floyd-cli`. FloydHub propose également une assistance sur leur chat Intercom si vous êtes bloqué à un moment donné.

Lançons votre premier réseau de neurones dans FloydHub en utilisant TFlearn, Jupyter Notebook et Tensorboard.

Après avoir installé et vous être connecté à FloydHub, téléchargez les fichiers dont vous avez besoin pour ce guide.

Allez dans votre terminal et tapez la commande suivante :

```
git clone https://github.com/emilwallner/Deep-Learning-101.git
```

Ouvrez le dossier et initialisez FloydHub :

```
cd Deep-Learning-101floyd init 101
```

Le tableau de bord web de FloydHub s'ouvrira dans votre navigateur, et vous serez invité à créer un nouveau projet FloydHub appelé `101`. Une fois cela fait, retournez à votre terminal et exécutez la même commande `init`.

```
floyd init 101
```

Vous êtes maintenant prêt à exécuter votre travail de réseau de neurones sur FloydHub.

Avec la commande `floyd run`, vous pouvez passer divers paramètres. Dans notre cas, nous voudrons :

* Monter un jeu de données public sur FloydHub, que j'ai déjà téléchargé. Dans le répertoire de données, tapez `--data emilwallner/datasets/cifar-10/1:data`. Vous pouvez explorer ce jeu de données (et de nombreux autres jeux de données publics) en le visualisant sur [FloydHub](https://www.floydhub.com/emilwallner/datasets/cifar-10/1)
* Utiliser un GPU cloud avec `--gpu`
* Activer Tensorboard avec `--tensorboard`
* Exécuter le travail en mode Jupyter Notebook avec `--mode jupyter`

D'accord, lançons notre travail :

```
floyd run --data emilwallner/datasets/cifar-10/1:data --gpu --tensorboard --mode jupyter
```

Une fois qu'il initialise Jupyter dans votre navigateur, cliquez sur le fichier nommé `start-here.ipnyb`.

`start-here.ipnyb` est un simple réseau de neurones pour se familiariser avec la syntaxe dans TFlearn. Il apprend la logique de l'opérateur OR, expliquée plus en détail plus tard.

Dans la barre de menu, cliquez sur **Kernel > Restart & Run** _A_ll. Si vous voyez le message, c'est qu'il fonctionne, alors vous êtes prêt à partir.

Allez dans votre projet FloydHub pour trouver le lien pour Tensorboard.

### Un Réseau de Neurones Profond

Le deep learning est constitué de réseaux de neurones avec plus d'une couche cachée. Il existe déjà de nombreux tutoriels détaillés sur le fonctionnement des CNN (Convolutional Neural Networks). Vous pouvez les trouver [ici](https://www.youtube.com/watch?v=FmpDIaiMIeA&t=1202s), [ici](http://cs231n.github.io/convolutional-networks/), et [ici](https://www.youtube.com/watch?v=LxfUGhug-iQ).

Nous allons donc nous concentrer sur les notions de haut niveau que vous pouvez appliquer à la plupart des réseaux de neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/S1F2lrtbFVZQr0x4HNQh3woW0gJuGsidK2tT)
_Note : la visualisation n'est pas un réseau de neurones profond. Il lui faut plus d'une couche cachée._

Vous voulez entraîner des réseaux de neurones pour faire des prédictions sur des données qu'ils n'ont pas été entraînés à reconnaître. Ils ont besoin d'une capacité à généraliser. C'est un équilibre entre l'apprentissage et l'oubli.

Vous voulez qu'ils apprennent à séparer le signal du bruit. Mais aussi qu'ils oublient les signaux qui ne se trouvent que dans les données d'entraînement.

Si le réseau de neurones n'apprend pas assez, il est sous-ajusté. L'inverse est le surajustement. C'est quand il a trop appris des données d'entraînement.

La **régularisation** est le processus qui réduit le surajustement en oubliant les signaux spécifiques à l'entraînement.

Pour avoir une intuition de ces concepts, nous allons travailler avec le [jeu de données CIFAR-10](https://pgaleone.eu/images/autoencoders/tf/cifar10_io_l2.png). C'est un jeu de données avec 60k images dans dix catégories différentes, comme des voitures, des camions et des oiseaux. Le but est de prédire à quelle catégorie parmi les dix appartient une nouvelle image.

![Image](https://cdn-media-1.freecodecamp.org/images/A-akFBc01o4drN3dr7gdsA7OyMi4Dhg4-HNf)

Pour avoir une intuition de ces concepts, nous allons travailler avec le [jeu de données CIFAR-10](https://pgaleone.eu/images/autoencoders/tf/cifar10_io_l2.png). C'est un jeu de données avec 60k images dans dix catégories différentes, comme des voitures, des camions et des oiseaux. Le but est de prédire à quelle catégorie parmi les dix appartient une nouvelle image.

![Image](https://cdn-media-1.freecodecamp.org/images/ITJQ-dCw10uIsWOA7XZq2lSnLXpv8sDI92dl)
_Images d'exemple de CIFAR_

Normalement, nous devons extraire les données, les nettoyer et appliquer des filtres aux images. Mais pour simplifier, nous allons nous concentrer uniquement sur les réseaux de neurones. Vous pouvez exécuter tous les exemples à partir du notebook Jupyter [dans la section installation](https://github.com/emilwallner/Deep-Learning-101).

La couche d'entrée prend une image qui a été mappée en chiffres. La couche de sortie classe les images en dix catégories. Les couches cachées sont un mélange de couches de convolution, de pooling et de couches connectées.

### Choix du nombre de couches

Faisons une comparaison entre un réseau de neurones avec un ensemble de couches contre trois ensembles de couches. Chaque ensemble comprend une couche de convolution, de pooling et une couche connectée.

Les deux premières expériences sont appelées `[experiment-0-few-layers.ipynb](https://github.com/emilwallner/Deep-Learning-101/blob/master/experiment_0_few_layers.ipynb)` et `[experiment-0-three-layer-sets.ipynb](https://github.com/emilwallner/Deep-Learning-101/blob/master/experiment_0_three_layer_sets.ipynb)`.

Vous pouvez exécuter ces notebooks en cliquant sur **Kernel > Restart & Run** All dans la barre de menu. Ensuite, jetez un coup d'œil au journal d'entraînement dans Tensorboard. Vous verrez que celui avec de nombreuses couches est ~15% plus précis. La couche avec peu de couches est sous-ajustée — elle n'apprend pas assez.

Vous pouvez exécuter le même exemple à partir du dossier que vous avez téléchargé précédemment, ainsi que toutes les expériences à venir.

![Image](https://cdn-media-1.freecodecamp.org/images/nhKF4BVT-0KA8bqo5gsEwzFUAWiAmwqA3OZ1)
_experiment_0.ipynb dans le dépôt_

Jetez un coup d'œil à la **Précision** et à la **Précision/Validation**. Il est considéré comme une bonne pratique en deep learning de diviser le jeu de données en deux. Un pour l'entraînement du réseau de neurones et un autre pour sa validation. De cette façon, vous pouvez dire à quel point le réseau de neurones fait des prédictions sur de nouvelles données, ou sa capacité à généraliser.

C'est ainsi que vous pouvez dire à quel point le réseau de neurones fait des prédictions sur de nouvelles données, ou sa capacité à généraliser.

Comme nous pouvons le voir, la précision des données d'entraînement est plus élevée que la précision sur le jeu de données de validation. Le réseau de neurones a inclus du bruit de fond et des détails qui l'empêchent de prédire de nouvelles images.

Pour traiter le surajustement, vous pouvez punir les fonctions complexes et introduire du bruit dans le réseau de neurones. Les techniques de régularisation courantes pour prévenir cela sont les couches de dropout et la punition des fonctions complexes.

### Couches de Dropout

Nous pouvons comparer la régularisation par dropout à la valeur d'une démocratie. Au lieu d'avoir quelques neurones puissants qui décident du résultat final, ils distribuent le pouvoir.

Le réseau de neurones est forcé d'apprendre plusieurs représentations indépendantes. Lorsqu'il fait la prédiction finale, il a alors plusieurs motifs distincts à apprendre.

Voici un exemple de réseau de neurones avec une couche de dropout.

Dans cette comparaison, les réseaux de neurones sont les mêmes sauf qu'un a une couche de dropout et l'autre non.

![Image](https://cdn-media-1.freecodecamp.org/images/60CuozZU6MufIXA-HLU4OI5MIKJdOE66hBaU)

Dans chaque couche du réseau de neurones, les neurones deviennent dépendants les uns des autres. Certains neurones gagnent plus d'influence que d'autres. La couche de dropout désactive aléatoirement différents neurones. De cette façon, chaque neurone doit construire une contribution distincte à la sortie finale.

La deuxième méthode populaire pour prévenir le surajustement est d'appliquer une fonction de régularisation `L1` ou `L2` sur chaque couche.

### Régularisation L1 et L2

Supposons que vous souhaitiez décrire un cheval. Si la description est trop détaillée, vous excluez trop de chevaux. Mais si elle est trop générale, vous pourriez inclure d'autres animaux. La régularisation `L1` et `L2` aide le réseau à faire cette distinction.

Si nous faisons une comparaison similaire à l'expérience précédente, nous obtenons un résultat similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/zoEytKBHqDVjcNvSDm3YK2z7cWylAnJGv3Tj)

Le réseau de neurones avec des fonctions de régularisation surpasse celui sans elles.

La fonction de régularisation `L2` punit les fonctions qui sont trop complexes. Elle mesure combien chaque fonction contribue à la sortie finale. Elle punit ensuite celles avec de grands coefficients.

### Taille du lot

Un autre hyperparamètre central est la taille du lot, la quantité de données à utiliser pour chaque étape d'entraînement. Ci-dessous, une comparaison entre un grand et un petit lot.

![Image](https://cdn-media-1.freecodecamp.org/images/hHpM6FwJszVpHN2VB4sRYGM9UsVGFpNgezr7)

Comme nous le voyons dans le résultat, une grande taille de lot nécessite moins de cycles mais a des étapes d'entraînement plus précises. En comparaison, une taille de lot plus petite est plus aléatoire mais prend plus d'étapes pour compenser.

Une grande taille de lot nécessite moins d'étapes d'apprentissage. Mais vous avez besoin de plus de mémoire et de temps pour calculer chaque étape.

### Taux d'apprentissage

La dernière expérience est une comparaison entre un réseau avec des taux d'apprentissage petits, moyens et grands.

![Image](https://cdn-media-1.freecodecamp.org/images/01vs2qbUxLz3gD2ajxqYrhUEyc0I8qtn6xJl)

Le taux d'apprentissage est souvent considéré comme l'un des paramètres les plus importants en raison de son impact. Il régule comment ajuster le changement de prédiction pour chaque étape d'apprentissage. Si le taux d'apprentissage est trop élevé ou trop bas, il pourrait ne pas converger, comme le grand taux d'apprentissage ci-dessus.

Il n'y a pas de manière fixe de concevoir des réseaux de neurones. Beaucoup de cela a à voir avec l'expérimentation. Regardez ce que les autres ont fait en ajoutant des couches et en ajustant les hyperparamètres.

Si vous avez accès à beaucoup de puissance de calcul, vous pouvez créer des programmes pour concevoir et ajuster les hyperparamètres.

Lorsque vous avez terminé d'exécuter votre travail, vous devriez arrêter votre instance de GPU cloud en cliquant sur Annuler dans le tableau de bord web de FloydHub pour votre travail.

### Prochaines Étapes

Dans le [dépôt d'exemples officiel de TFlearn](https://github.com/tflearn/tflearn/tree/master/examples/images), vous pouvez vous familiariser avec certains des CNN les mieux performants. Essayez de copier certaines des méthodes et améliorez la validation pour le jeu de données CIFAR-10. Le meilleur résultat à ce jour est de 96,53 % (Graham, 2014).

Il est également utile d'apprendre la syntaxe Python et de se familiariser avec la ligne de commande. Cela réduit la charge cognitive inutile afin que vous puissiez vous concentrer sur les notions de deep learning. Commencez par le [cours sur Python](https://www.codecademy.com/tracks/python) de Codecademy, puis faites celui sur la [ligne de commande](https://www.codecademy.com/learn/learn-the-command-line). Cela ne devrait pas prendre plus de trois jours si vous le faites à temps plein.

**Remerciements à** [Ignacio Tonoli de Maussion](https://www.freecodecamp.org/news/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b/undefined), [Per Harald Borgen](https://www.freecodecamp.org/news/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b/undefined), [Jean-Luc Wingert](https://www.freecodecamp.org/news/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b/undefined), [Sai Soundararaj](https://twitter.com/sasounda), et [Charlie Harrington](https://www.freecodecamp.org/news/deep-learning-for-developers-tools-you-can-use-to-code-neural-networks-on-day-1-34c4435ae6b/undefined) pour avoir lu les brouillons de cet article. Et gratitude envers la [communauté TFlearn](https://github.com/tflearn/tflearn/blob/master/examples/basics/linear_regression.py) pour la documentation et le code exemple.

#### **À propos d'Emil Wallner**

Ceci est la première partie d'une série de blogs en plusieurs parties alors que j'apprends le deep learning. J'ai passé une décennie à explorer l'apprentissage humain. J'ai travaillé pour l'école de commerce d'Oxford, investi dans des startups éducatives et construit une entreprise de technologie éducative. L'année dernière, je me suis inscrit à [Ecole 42](https://twitter.com/paulg/status/847844863727087616) pour appliquer mes connaissances de l'apprentissage humain à l'apprentissage automatique.

Vous pouvez suivre mon parcours d'apprentissage sur [Twitter](https://twitter.com/EmilWallner). Si vous avez des questions/suggestions, veuillez laisser un commentaire ci-dessous ou me contacter sur [Medium](https://medium.com/@emilwallner).

Ceci a été publié pour la première fois en tant que post communautaire sur le [blog de Floydhub](http://blog.floydhub.com/my-first-weekend-of-deep-learning/).