---
title: Plonger plus profondément dans l'apprentissage par renforcement avec le Q-Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T20:04:07.000Z'
originalURL: https://freecodecamp.org/news/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sYFG8AhKTVnmv_VLRK0c0A.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Plonger plus profondément dans l'apprentissage par renforcement avec le
  Q-Learning
seo_desc: 'By Thomas Simonini


  This article is part of Deep Reinforcement Learning Course with Tensorflow ?️. Check
  the syllabus here.


  Today we’ll learn about Q-Learning. Q-Learning is a value-based Reinforcement Learning
  algorithm.

  This article is the second ...'
---

Par Thomas Simonini

> Cet article fait partie du cours d'apprentissage par renforcement profond avec Tensorflow 🚀. Consultez le programme [ici](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

Aujourd'hui, nous allons apprendre le Q-Learning. Le Q-Learning est un algorithme d'apprentissage par renforcement basé sur la valeur.

Cet article est la deuxième partie d'une série gratuite de publications de blog sur l'apprentissage par renforcement profond. Pour plus d'informations et de ressources, consultez le [programme du cours](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/). Voir [le premier article ici](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419).

Dans cet article, vous apprendrez :

* Qu'est-ce que le Q-Learning
* Comment l'implémenter avec Numpy

### La vue d'ensemble : le Chevalier et la Princesse

![Image](https://cdn-media-1.freecodecamp.org/images/1*h7B4EVx3B-sv5OvHH8nrNw.png)

Imaginons que vous êtes un chevalier et que vous devez sauver la princesse piégée dans le château montré sur la carte ci-dessus.

Vous pouvez vous déplacer d'une case à la fois. L'ennemi ne peut pas, mais si vous atterrissez sur la même case que l'ennemi, vous mourrez. Votre objectif est d'aller au château par le chemin le plus rapide possible. Cela peut être évalué en utilisant un système de "notation de points".

* Vous perdez -1 à chaque étape (perdre des points à chaque étape aide notre agent à être rapide).
* Si vous touchez un ennemi, vous perdez -100 points, et l'épisode se termine.
* Si vous êtes dans le château, vous gagnez, vous obtenez +100 points.

La question est : comment créer un agent capable de faire cela ?

Voici une première stratégie. Disons que notre agent essaie d'aller sur chaque case, puis colorie chaque case. Vert pour "sûr", et rouge sinon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*imHK8jFkt6udrUwm8RvOhA.png)
_La même carte, mais colorée pour montrer quelles cases sont sûres à visiter._

Ensuite, nous pouvons dire à notre agent de ne prendre que les cases vertes.

Mais le problème est que ce n'est pas vraiment utile. Nous ne savons pas quelle est la meilleure case à prendre lorsque les cases vertes sont adjacentes les unes aux autres. Ainsi, notre agent peut tomber dans une boucle infinie en essayant de trouver le château !

### Introduction à la Q-table

Voici une deuxième stratégie : créer une table où nous calculerons la récompense future maximale attendue, pour chaque action à chaque état.

Grâce à cela, nous saurons quelle est la meilleure action à prendre pour chaque état.

Chaque état (case) permet quatre actions possibles. Il s'agit de se déplacer à gauche, à droite, en haut ou en bas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kwu9TImqAWZCiooj3pLyCA.png)
_0 sont des mouvements impossibles (si vous êtes dans le coin supérieur gauche, vous ne pouvez pas aller à gauche ou en haut !)_

En termes de calcul, nous pouvons transformer cette grille en une table.

Cela s'appelle une **Q-table** ("Q" pour "qualité" de l'action). Les colonnes seront les quatre actions (gauche, droite, haut, bas). Les lignes seront les états. La valeur de chaque cellule sera la récompense future maximale attendue pour cet état et cette action donnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fBjmzVXBYdx2-QOXZhnzFQ.png)

Chaque score de la Q-table sera la récompense future maximale attendue que j'obtiendrai si je prends cette action dans cet état avec la meilleure politique donnée.

Pourquoi disons-nous "avec la politique donnée" ? C'est parce que **nous n'implémentons pas de politique.** Au lieu de cela, nous améliorons simplement notre Q-table pour toujours choisir la meilleure action.

Pensez à cette Q-table comme une "feuille de triche" de jeu. Grâce à cela, nous savons pour chaque état (chaque ligne dans la Q-table) quelle est la meilleure action à prendre, en trouvant le score le plus élevé dans cette ligne.

Oui ! Nous avons résolu le problème du château ! Mais attendez... Comment calculons-nous les valeurs pour chaque élément de la Q-table ?

Pour apprendre chaque valeur de cette Q-table, **nous utiliserons l'algorithme d'apprentissage Q.**

### Algorithme Q-learning : apprendre la fonction de valeur d'action

La fonction de valeur d'action (ou "Q-fonction") prend deux entrées : "état" et "action". Elle retourne la récompense future attendue de cette action dans cet état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6IqzImIFK1oEiVWmlu1Esw.png)

Nous pouvons voir cette fonction Q comme un lecteur qui parcourt la Q-table pour trouver la ligne associée à notre état, et la colonne associée à notre action. Elle retourne la valeur Q de la cellule correspondante. C'est la "récompense future attendue".

![Image](https://cdn-media-1.freecodecamp.org/images/1*yklmxNRdXleiDbv6aSZUIg.png)

Mais avant d'explorer l'environnement, la Q-table donne la même valeur fixe arbitraire (la plupart du temps 0). À mesure que nous explorons l'environnement, la Q-table nous donnera une approximation de mieux en mieux en mettant à jour de manière itérative Q(s,a) en utilisant l'équation de Bellman (voir ci-dessous !).

#### Le processus de l'algorithme Q-learning

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeoQEqWYYPs1P8yUwyaJVQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*voKUaGu68-cDuncy.)
_Le pseudo-code de l'algorithme Q-learning_

**Étape 1 : Initialiser les valeurs Q**  
Nous construisons une Q-table, avec _m_ colonnes (m = nombre d'actions), et _n_ lignes (n = nombre d'états). Nous initialisons les valeurs à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ut7-8VVa-TWC40_YAeqZ7Q.png)

**Étape 2 : Pour la vie (ou jusqu'à ce que l'apprentissage soit arrêté)**  
Les étapes 3 à 5 seront répétées jusqu'à ce que nous ayons atteint un nombre maximum d'épisodes (spécifié par l'utilisateur) ou jusqu'à ce que nous arrêtions manuellement l'entraînement.

**Étape 3 : Choisir une action**  
Choisir une action _a_ dans l'état actuel _s_ en fonction des estimations actuelles des valeurs Q.

Mais... quelle action pouvons-nous prendre au début, si toutes les valeurs Q sont égales à zéro ?

C'est là que le compromis exploration/exploitation dont nous avons parlé dans [le dernier article](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419) sera important.

L'idée est qu'au début, nous utiliserons la stratégie epsilon-greedy :

* Nous spécifions un taux d'exploration "epsilon", que nous fixons à 1 au début. C'est le taux d'étapes que nous ferons de manière aléatoire. Au début, ce taux doit être à sa valeur la plus élevée, car nous ne savons rien des valeurs dans la Q-table. Cela signifie que nous devons faire beaucoup d'exploration, en choisissant nos actions de manière aléatoire.
* Nous générons un nombre aléatoire. Si ce nombre > epsilon, alors nous ferons de "l'exploitation" (cela signifie que nous utilisons ce que nous savons déjà pour sélectionner la meilleure action à chaque étape). Sinon, nous ferons de l'exploration.
* L'idée est que nous devons avoir un epsilon élevé au début de l'entraînement de la fonction Q. Ensuite, le réduire progressivement à mesure que l'agent devient plus confiant dans l'estimation des valeurs Q.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9StLEbor62FUDSoRwxyJrg.png)

**Étape 4-5 : Évaluer !**  
Prenez l'action _a_ et observez l'état résultant _s'_ et la récompense _r_. Maintenant, mettez à jour la fonction Q(s,a).

Nous prenons l'action _a_ que nous avons choisie à l'étape 3, et l'exécution de cette action nous retourne un nouvel état _s'_ et une récompense _r_ (comme nous l'avons vu dans le processus d'apprentissage par renforcement dans [le premier article](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419)).

Ensuite, pour mettre à jour Q(s,a), nous utilisons **l'équation de Bellman** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmcVWHHbzCxDc-irBy9JTw.png)

L'idée ici est de mettre à jour notre Q(état, action) comme suit :

```
Nouvelle valeur Q =    Valeur Q actuelle +    lr * [Récompense + taux_actualisation * (valeur Q la plus élevée entre les actions possibles à partir du nouvel état s' ) — Valeur Q actuelle ]
```

Prenons un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-3MsnOxnipUICgRUWVz9Ng.png)

* Un fromage = +1
* Deux fromages = +2
* Gros tas de fromage = +10 (fin de l'épisode)
* Si vous mangez du poison pour rat = -10 (fin de l'épisode)

**Étape 1 : Nous initialisons notre Q-table**

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYB4uCHcwfa2SYlik9HNaQ.png)
_La Q-table initialisée_

**Étape 2 : Choisir une action**   
À partir de la position de départ, vous pouvez choisir entre aller à droite ou en bas. Parce que nous avons un taux epsilon élevé (puisque nous ne savons rien de l'environnement pour l'instant), nous choisissons aléatoirement. Par exemple... aller à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IyjuM__mnP-as7m5KTdUyA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VY6VFj3RnBMi9sPshouF8A.png)
_Nous nous déplaçons aléatoirement (par exemple, à droite)_

Nous avons trouvé un morceau de fromage (+1), et nous pouvons maintenant mettre à jour la valeur Q de l'état de départ et de l'action à droite. Nous faisons cela en utilisant l'équation de Bellman.

**Étape 4-5 : Mettre à jour la fonction Q**

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmcVWHHbzCxDc-irBy9JTw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wzI7Y0s26kw3fQTZx8HZ8A.png)

* Tout d'abord, nous calculons le changement de valeur Q ΔQ(départ, droite)
* Ensuite, nous ajoutons la valeur Q initiale au ΔQ(départ, droite) multiplié par un taux d'apprentissage.

Pensez au taux d'apprentissage comme une manière de déterminer à quelle vitesse un réseau abandonne l'ancienne valeur pour la nouvelle. Si le taux d'apprentissage est 1, la nouvelle estimation sera la nouvelle valeur Q.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IAhKNvQBreGJj2jWN7fleQ.png)
_La Q-table mise à jour_

Bien ! Nous venons de mettre à jour notre première valeur Q. Maintenant, nous devons faire cela encore et encore jusqu'à ce que l'apprentissage soit arrêté.

### Implémenter un algorithme Q-learning

> Nous avons fait une vidéo où nous implémentons un agent Q-learning qui apprend à jouer à Taxi-v2 avec Numpy.

Maintenant que nous savons comment cela fonctionne, nous allons implémenter l'algorithme Q-learning étape par étape. Chaque partie du code est expliquée directement dans le notebook Jupyter ci-dessous.

Vous pouvez y accéder dans le [dépôt du cours d'apprentissage par renforcement profond](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/tree/master/Q%20learning/FrozenLake).

Ou vous pouvez y accéder directement sur Google Colaboratory :

[**Q* Learning avec Frozen Lake**](https://colab.research.google.com/drive/17iM0vx848VYWFwW3Du-l-FCn3Y1VhCgx)  
[colab.research.google.com](https://colab.research.google.com/drive/17iM0vx848VYWFwW3Du-l-FCn3Y1VhCgx)

### Un récapitulatif...

* Le Q-learning est un algorithme d'apprentissage par renforcement basé sur la valeur qui est utilisé pour trouver la politique optimale de sélection d'actions en utilisant une fonction q.
* Il évalue quelle action prendre en fonction d'une fonction de valeur d'action qui détermine la valeur d'être dans un certain état et de prendre une certaine action dans cet état.
* Objectif : maximiser la fonction de valeur Q (récompense future attendue donnée un état et une action).
* La Q-table nous aide à trouver la meilleure action pour chaque état.
* Pour maximiser la récompense attendue en sélectionnant la meilleure de toutes les actions possibles.
* Le Q vient de la qualité d'une certaine action dans un certain état.
* Fonction Q(état, action) → retourne la récompense future attendue de cette action dans cet état.
* Cette fonction peut être estimée en utilisant le Q-learning, qui met à jour de manière itérative Q(s,a) en utilisant l'équation de Bellman.
* Avant d'explorer l'environnement : la Q-table donne la même valeur fixe arbitraire → mais à mesure que nous explorons l'environnement → Q nous donne une approximation de mieux en mieux.

C'est tout ! N'oubliez pas d'implémenter chaque partie du code par vous-même — il est vraiment important d'essayer de modifier le code que je vous ai donné.

Essayez d'ajouter des époques, changez le taux d'apprentissage, et utilisez un environnement plus difficile (comme Frozen-lake avec des cases de 8x8). Amusez-vous !

La prochaine fois, nous travaillerons sur le Deep Q-learning, l'une des plus grandes avancées en apprentissage par renforcement profond en 2015. Et nous entraînerons un agent qui joue à Doom et tue des ennemis !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4XjhLC0IAOznnk5613PsQ.gif)
_Doom !_

Si vous avez aimé mon article, **veuillez cliquer sur le 👏 ci-dessous autant de fois que vous avez aimé l'article** afin que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou me tweeter [@ThomasSimonini](https://twitter.com/ThomasSimonini).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

Continuez à apprendre, restez génial !

#### Cours d'apprentissage par renforcement profond avec Tensorflow 🚀

📜 [Programme](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)

📹 [Version vidéo](https://www.youtube.com/channel/UC8XuSf1eD9AF8x8J19ha5og?view_as=subscriber)

Partie 1 : [Une introduction à l'apprentissage par renforcement](https://medium.com/p/4339519de419/edit)

Partie 2 : [Plonger plus profondément dans l'apprentissage par renforcement avec le Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)

Partie 3 : [Une introduction au Deep Q-Learning : jouons à Doom](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)

Partie 3+ : [Améliorations dans le Deep Q Learning : Dueling Double DQN, Prioritized Experience Replay, et Q-targets fixes](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)

Partie 4 : [Une introduction aux Policy Gradients avec Doom et Cartpole](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f)

Partie 5 : [Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the Hedgehog !](https://medium.freecodecamp.org/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d)

Partie 6 : [Proximal Policy Optimization (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e)

Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)