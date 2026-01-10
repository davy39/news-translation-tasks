---
title: 'Apprendre à mon robot à penser : « Ma prise est nulle »'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T20:12:33.000Z'
originalURL: https://freecodecamp.org/news/teaching-my-robot-to-think-my-grasp-sucks-5e3d5a908745
coverImage: https://cdn-media-1.freecodecamp.org/images/1*14ZzW3BGzORaYeo_xHvFWA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: robotics
  slug: robotics
seo_title: 'Apprendre à mon robot à penser : « Ma prise est nulle »'
seo_desc: 'By Ugo Cupcic

  As the Chief Technical Architect of the Shadow Robot Company, I spend a lot of time
  thinking about grasping things with our robots. This story is a quick delve into
  the world of grasp robustness prediction using machine learning.

  First ...'
---

Par Ugo Cupcic

En tant qu'architecte technique en chef de la [Shadow Robot Company](https://www.shadowrobot.com/), je passe beaucoup de temps à réfléchir sur la manière de saisir des objets avec [nos robots](https://www.shadowrobot.com/products/). Cette histoire est une plongée rapide dans le monde de la prédiction de la robustesse de la prise utilisant l'apprentissage automatique.

Tout d'abord, pourquoi se concentrer sur cela ? Il existe actuellement des projets beaucoup plus excitants utilisant l'apprentissage profond pour la robotique. Par exemple, le travail réalisé par Ken Goldberg et son équipe à l'UC Berkeley sur [DexNet](https://berkeleyautomation.github.io/dex-net/) est très impressionnant. Ils parviennent à saisir de manière fiable 99 % de leur ensemble de test en utilisant l'apprentissage profond. Mais lorsque nous travaillons sur la livraison d'une « Main qui Saisit » en tant que produit, nous devons nous concentrer sur la livraison de petites itérations robustes en premier. Pouvoir prédire si une prise est stable ou non, de manière dynamique, est un sujet intéressant pour l'industrie. Par exemple, si vous pouvez déterminer qu'une prise a une forte chance d'échouer avant qu'elle ne le fasse réellement, vous pouvez gagner beaucoup de temps en re-saisissant.

Le but n'est pas de vous donner la meilleure solution pour la qualité de la prise en utilisant l'apprentissage automatique, mais plutôt de donner une introduction douce à l'utilisation de l'apprentissage automatique en robotique pour un but directement utile qui est difficile à résoudre [avec les algorithmes standards existants](https://medium.com/@ugocupcic/how-to-tell-if-my-robots-grasp-is-stable-7811fa3d16b8).

Si vous voulez sauter les explications et mettre la main à la pâte avec l'ensemble de données open source et le code, [rendez-vous sur Kaggle](https://www.kaggle.com/ugocupcic/grasping-dataset).

### Collecte de l'ensemble de données

En utilisant le [Smart Grasping Sandbox](https://medium.freecodecamp.org/an-open-sandbox-for-robot-grasping-cee467a3fabb), nous avons collecté un grand ensemble de données pour notre but. Puisque notre objectif est de classer si une prise est stable ou non, nous devons collecter un ensemble de données contenant à la fois des prises stables et instables. Nous avions également besoin de quantifier la stabilité d'une prise automatiquement afin d'annoter nos données facilement — au lieu de les annoter manuellement.

Quelles données devons-nous enregistrer ? Nous obtenons beaucoup de données de la simulation. Pour simplifier les choses, nous allons nous concentrer uniquement sur l'état des articulations. Cet état contient — pour chaque articulation — la position, le couple et la vitesse. Puisque nous voulons une qualité de prise qui soit indépendante de l'objet, nous n'utiliserons pas la position de l'articulation : la forme de la main est purement spécifique à l'objet. Nous allons donc enregistrer la vitesse et le couple de chaque articulation.

Notre ensemble de données ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C5BDb5q3GBZ20G3DPHMVzw.png)
_Aperçu de l'ensemble de données_

#### Une mesure objective de la stabilité de la prise

En simulation, il existe un moyen facile de vérifier si une prise est stable ou non. Une fois l'objet saisi — si la prise est stable — alors l'objet ne devrait pas bouger dans la main. Cela signifie que la distance entre l'objet et la paume ne devrait pas changer lorsque l'on secoue l'objet. Heureusement pour nous, cette mesure est très facile à obtenir en simulation !

![Image](https://cdn-media-1.freecodecamp.org/images/1*RWxTUMlwHQyTVIZ9g1Sx2g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l9qyPBafqs6h5-n2aHkDyg.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UWO-hJVxzJF8lBL0YwVKnA.jpeg)
_1. première prise 2. puis secouer, tout en 3. mesurant la distance entre la paume et l'objet_

#### Enregistrons quelques données

Maintenant que nous savons ce que nous faisons, nous allons utiliser le Sandbox pour enregistrer un grand ensemble de données. Vous pouvez jeter un coup d'œil au code que j'utilise pour cela [ici](https://github.com/shadow-robot/smart_grasping_sandbox/blob/master/smart_grasping_sandbox/nodes/grasp_quality.py). Puisque le Sandbox fonctionne sur Docker, il est très facile de lancer plusieurs instances en parallèle sur un serveur et de les laisser fonctionner en parallèle pendant un certain temps.

Puisque je ne fais pas confiance aux simulations pour fonctionner trop longtemps — appelez cela une forte conviction basée sur l'expérience personnelle, comme l'effet de démonstration — je ne lance également que 100 itérations de prise avant de redémarrer le conteneur Docker avec un environnement vierge.

Afin d'obtenir un ensemble de données pertinent, je randomise la pose de la prise autour d'une bonne prise — que j'ai trouvée empiriquement : nous voulons suffisamment de mauvaises prises. J'utilise également différentes distances d'approche. Cela me donne — approximativement — un ratio de 50/50 de prises stables et instables — avec beaucoup de prises entre les deux.

Pour votre commodité, j'ai rendu cet ensemble de données public et vous pouvez le trouver sur [Kaggle](https://www.kaggle.com/ugocupcic/grasping-dataset).

### Apprenons !

Maintenant que nous avons collecté un bon ensemble d'apprentissage, nous voulons enseigner à un réseau de neurones afin de prédire si une prise est stable ou non, en fonction de l'état actuel des articulations.

#### Qu'est-ce qu'un réseau de neurones ?

Avec tout le battage actuel autour de l'apprentissage profond, il est facile d'imaginer un ordinateur avec un cerveau apprenant de nouvelles choses de manière auto-magique. Démystifions rapidement le réseau de neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ou2uG2WHO0adhX6GORTwQQ.jpeg)

Comme montré ci-dessus, un réseau de neurones prend en entrée un vecteur — dans notre cas, le couple et la vitesse pour chaque doigt. Ensuite, ce vecteur est transformé plusieurs fois — autant de fois qu'il y a de couches — et un vecteur final est la sortie du réseau de neurones : la classification des données qui ont été fournies. Dans notre cas, la sortie que nous voulons est de savoir si la prise est robuste ou non — donc c'est un vecteur de taille 1.

Pendant le processus d'apprentissage, nous allons alimenter le réseau avec des valeurs que nous avons collectées dans l'ensemble de données. Puisque nous savons si ces valeurs d'articulation sont pour des prises stables ou instables — notre ensemble de données est annoté — le processus de formation ajuste les paramètres des différentes transitions entre les couches.

L'art de l'apprentissage automatique consiste à choisir la topographie du réseau — combien de couches et de neurones, plus quelles fonctions de transition utiliser dans notre réseau — ainsi qu'à collecter un bon ensemble de données. Si nous avons tout cela, alors nous pouvons former un réseau qui généralisera bien aux cas qui n'ont pas été vus pendant l'entraînement.

#### Formation du réseau

Le but de cet exercice n'est pas de créer l'algorithme parfait de prédiction de la qualité de la prise, mais plutôt de montrer simplement comment il est possible d'utiliser le bac à sable de préhension intelligente pour l'apprentissage automatique. J'ai choisi une topologie très simple pour le réseau : j'utilise une seule couche cachée entre la couche d'entrée et la couche de sortie. Pour plus de détails, reportez-vous au [notebook iPython](https://www.kaggle.com/ugocupcic/grasp-quality-prediction).

Pour simplifier les choses, j'utilise l'excellente [bibliothèque Keras](https://keras.io/). Si vous ne pouvez pas attendre et voulez voir le code réel, allez sur [Kaggle](https://www.kaggle.com/ugocupcic/grasping-dataset). Sinon, continuez à lire !

Après avoir chargé l'ensemble de données en mémoire, je le divise entre l'ensemble d'entraînement et l'ensemble de test. La validation sera effectuée sur une partie de l'ensemble d'entraînement, et j'utiliserai l'ensemble de test pour voir s'il généralise bien.

Puisque mon réseau est petit, l'entraînement est relativement rapide, même sur mon ordinateur portable. Lorsque j'entraîne des réseaux plus profonds, je lance l'image docker sur une machine puissante dans le cloud, en utilisant les GPU de NVidia pour accélérer l'entraînement.

Après avoir entraîné mon réseau, j'obtiens une précision de 78,87 %.

### Test de mon réseau entraîné sur des données en direct

Maintenant que nous avons entraîné notre réseau de neurones, nous pouvons l'utiliser pour prédire la qualité de la prise en temps réel sur la simulation. Comme vous pouvez le voir dans la vidéo ci-dessous, la prédiction fonctionne bien la plupart du temps.

Comme vous pouvez le voir dans cette vidéo, la prédiction en direct de la prise — le graphique bleu à gauche — est supérieure à 0,5 lors de la première saisie de la balle. Cela donne une prise très stable. En revanche, lors de la deuxième saisie, la métrique reste en dessous de 0,2, prédisant à juste titre que la saisie échouera.

### Mots de la fin

J'espère que cette histoire a piqué votre intérêt. Si vous voulez essayer d'entraîner votre propre algorithme sur cet ensemble de données, la chose la plus facile à faire est d'[aller sur Kaggle.com](https://www.kaggle.com/ugocupcic/grasping-dataset) où tout est déjà configuré pour vous.

Évidemment, il y a beaucoup plus à faire pour déployer cette méthode en production. La première chose à aborder est d'avoir une meilleure simulation afin de saisir une grande variété d'objets. Je vais également examiner la possibilité d'avoir une qualité de prise objective en direct — celle qui est utilisée pour annoter notre ensemble de données — afin de pouvoir utiliser la prédiction de séries temporelles au lieu de la prédiction ponctuelle. Et le défi final sera de transférer cet apprentissage au robot réel.

Il y a tant de sujets intéressants à explorer avec l'apprentissage automatique en robotique : la qualité de la prise, la détection de glissement, parmi tant d'autres.

J'espère que vous avez hâte de tester vos idées sur le bac à sable. Si vous le faites, [faites-le moi savoir sur Twitter](http://twitter.com/ugocupcic) !