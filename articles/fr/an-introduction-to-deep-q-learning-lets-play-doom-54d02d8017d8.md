---
title: 'Une introduction au Deep Q-Learning : jouons à Doom'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-11T15:23:37.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HtKKEcDPWBouD813vU_KJg.png
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
seo_title: 'Une introduction au Deep Q-Learning : jouons à Doom'
seo_desc: 'By Thomas Simonini


  This article is part of Deep Reinforcement Learning Course with Tensorflow ?️. Check
  the syllabus here.


  Last time, we learned about Q-Learning: an algorithm which produces a Q-table that
  an agent uses to find the best action to t...'
---

Par Thomas Simonini

> Cet article fait partie du cours Deep Reinforcement Learning avec Tensorflow 🏁. Consultez le programme [ici](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

[La dernière fois](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe), nous avons appris le Q-Learning : un algorithme qui produit une Q-table qu'un agent utilise pour trouver la meilleure action à entreprendre étant donné un état.

Mais comme nous le verrons, produire et mettre à jour une Q-table peut devenir inefficace dans des environnements avec un grand espace d'états.

Cet article est la troisième partie d'une série de publications sur le Deep Reinforcement Learning. Pour plus d'informations et de ressources, consultez le [programme du cours](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

Aujourd'hui, nous allons créer un Deep Q Neural Network. Au lieu d'utiliser une Q-table, nous allons implémenter un réseau de neurones qui prend un état et approxime les Q-valeurs pour chaque action basée sur cet état.

Grâce à ce modèle, nous pourrons créer un agent qui apprend à jouer à [Doom](https://en.wikipedia.org/wiki/Doom_(1993_video_game)) !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4XjhLC0IAOznnk5613PsQ.gif)
_Notre agent DQN_

Dans cet article, vous apprendrez :

* Qu'est-ce que le Deep Q-Learning (DQL) ?
* Quelles sont les meilleures stratégies à utiliser avec le DQL ?
* Comment gérer le problème de limitation temporelle
* Pourquoi nous utilisons l'expérience replay
* Quelles sont les mathématiques derrière le DQL
* Comment l'implémenter dans Tensorflow

### **Ajouter 'Deep' au Q-Learning**

Dans le [dernier article](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe), nous avons créé un agent qui joue à Frozen Lake grâce à l'algorithme Q-learning.

Nous avons implémenté la fonction Q-learning pour créer et mettre à jour une Q-table. Pensez à cela comme une "feuille de triche" pour nous aider à trouver la récompense future maximale attendue d'une action, étant donné un état actuel. C'était une bonne stratégie, mais ce n'est pas scalable.

Imaginez ce que nous allons faire aujourd'hui. Nous allons créer un agent qui apprend à jouer à Doom. Doom est un grand environnement avec un espace d'états gigantesque (des millions d'états différents). Créer et mettre à jour une Q-table pour cet environnement ne serait pas efficace du tout.

La meilleure idée dans ce cas est de créer un [réseau de neurones](http://neuralnetworksanddeeplearning.com/) qui approximera, étant donné un état, les différentes Q-valeurs pour chaque action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w5GuxedZ9ivRYqM_MLUxOQ.png)

### **Comment fonctionne le Deep Q-Learning ?**

Voici l'architecture de notre Deep Q Learning :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LglEewHrVsuEGpBun8_KTg.png)

Cela peut sembler complexe, mais je vais expliquer l'architecture étape par étape.

Notre Deep Q Neural Network prend une pile de quatre frames en entrée. Ceux-ci passent à travers son réseau et produisent un vecteur de Q-valeurs pour chaque action possible dans l'état donné. Nous devons prendre la plus grande Q-valeur de ce vecteur pour trouver notre meilleure action.

Au début, l'agent se comporte très mal. Mais avec le temps, il commence à associer les frames (états) avec les meilleures actions à effectuer.

#### **Partie de prétraitement**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QgGnC_0BkQEtPqMUftRC6A.png)

Le prétraitement est une étape importante. Nous voulons réduire la complexité de nos états pour réduire le temps de calcul nécessaire à l'entraînement.

Tout d'abord, nous pouvons convertir chaque état en niveaux de gris. La couleur n'ajoute pas d'information importante (dans notre cas, nous devons simplement trouver l'ennemi et le tuer, et nous n'avons pas besoin de couleur pour le trouver). C'est une économie importante, car nous réduisons nos trois canaux de couleur (RGB) à 1 (niveaux de gris).

Ensuite, nous recadrons le frame. Dans notre exemple, voir le plafond n'est pas vraiment utile.

Ensuite, nous réduisons la taille du frame et nous empilons quatre sous-frames ensemble.

#### **Le problème de la limitation temporelle**

[Arthur Juliani](https://www.freecodecamp.org/news/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8/undefined) donne une excellente explication sur ce sujet dans [son article](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2). Il a une idée ingénieuse : utiliser des [réseaux de neurones LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) pour gérer le problème.

Cependant, je pense qu'il est préférable pour les débutants d'utiliser des frames empilés.

La première question que vous pouvez poser est : pourquoi empiler les frames ensemble ?

Nous empilons les frames ensemble car cela nous aide à gérer le problème de la limitation temporelle.

Prenons un exemple, dans le jeu de Pong. Lorsque vous voyez ce frame :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lwyObh4p-jQjk19Q6qyIg.png)

Pouvez-vous me dire où la balle va ?

Non, car un seul frame ne suffit pas pour avoir un sens du mouvement !

Mais que se passe-t-il si j'ajoute trois frames supplémentaires ? Ici, vous pouvez voir que la balle va vers la droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MooQJUIkR_FVV2weeVPr8A.png)

C'est la même chose pour notre agent Doom. Si nous lui donnons un seul frame à la fois, il n'a aucune idée du mouvement. Et comment peut-il prendre une décision correcte, s'il ne peut pas déterminer où et à quelle vitesse les objets se déplacent ?

#### **Utilisation des réseaux de convolution**

Les frames sont traités par trois couches de convolution. Ces couches vous permettent d'exploiter les relations spatiales dans les images. Mais aussi, parce que les frames sont empilés ensemble, vous pouvez exploiter certaines propriétés spatiales à travers ces frames.

Si vous n'êtes pas familier avec la convolution, veuillez lire cet [excellent article intuitif](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721) par [Adam Geitgey](https://www.freecodecamp.org/news/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8/undefined).

Chaque couche de convolution utilisera ELU comme fonction d'activation. ELU s'est avéré être une bonne [fonction d'activation pour les couches de convolution](https://arxiv.org/pdf/1511.07289.pdf).

Nous utilisons une couche entièrement connectée avec la fonction d'activation ELU et une couche de sortie (une couche entièrement connectée avec une fonction d'activation linéaire) qui produit l'estimation de la Q-valeur pour chaque action.

#### **Experience Replay : faire un usage plus efficace de l'expérience observée**

L'expérience replay nous aidera à gérer deux choses :

* Éviter d'oublier les expériences précédentes.
* Réduire les corrélations entre les expériences.

Je vais expliquer ces deux concepts.

Cette partie et les illustrations ont été inspirées par la grande explication dans le chapitre Deep Q Learning du Nanodegree Deep Learning Foundations par [Udacity](https://eu.udacity.com/).

#### **Éviter d'oublier les expériences précédentes**

Nous avons un gros problème : la variabilité des poids, car il y a une forte corrélation entre les actions et les états.

Souvenez-vous, dans le premier article ([Introduction au Reinforcement Learning](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419)), nous avons parlé du processus de Reinforcement Learning :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aKYFRoEmmKkybqJOvLt2JQ.png)

À chaque étape, nous recevons un tuple (état, action, récompense, nouvel_état). Nous apprenons de celui-ci (nous alimentons le tuple dans notre réseau de neurones), puis nous jetons cette expérience.

Notre problème est que nous donnons des échantillons séquentiels des interactions avec l'environnement à notre réseau de neurones. Et il tend à oublier les expériences précédentes car il les écrase avec de nouvelles expériences.

Par exemple, si nous sommes au premier niveau puis au deuxième (qui est totalement différent), notre agent peut oublier comment se comporter au premier niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p4lfgKLiollqbkWYZ_jnlg.png)
_En apprenant à jouer au niveau de l'eau, notre agent oubliera comment se comporter au premier niveau_

Par conséquent, il peut être plus efficace d'utiliser les expériences précédentes en apprenant avec elles plusieurs fois.

Notre solution : créer un "tampon de replay". Celui-ci stocke les tuples d'expérience lors de l'interaction avec l'environnement, puis nous échantillonnons un petit lot de tuples pour alimenter notre réseau de neurones.

Pensez au tampon de replay comme à un dossier où chaque feuille est un tuple d'expérience. Vous l'alimentez en interagissant avec l'environnement. Ensuite, vous prenez quelques feuilles aléatoires pour alimenter le réseau de neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RFt8MBBkUSPZdolp_WfZFA.png)

Cela empêche le réseau d'apprendre uniquement ce qu'il a fait immédiatement.

#### **Réduire la corrélation entre les expériences**

Nous avons un autre problème : nous savons que chaque action affecte l'état suivant. Cela produit une séquence de tuples d'expérience qui peuvent être fortement corrélés.

Si nous entraînons le réseau dans l'ordre séquentiel, nous risquons que notre agent soit influencé par l'effet de cette corrélation.

En échantillonnant à partir du tampon de replay de manière aléatoire, nous pouvons briser cette corrélation. Cela empêche les valeurs d'action d'osciller ou de diverger de manière catastrophique.

Il sera plus facile de comprendre cela avec un exemple. Supposons que nous jouons à un jeu de tir à la première personne, où un monstre peut apparaître à gauche ou à droite. Le but de notre agent est de tirer sur le monstre. Il a deux armes et deux actions : tirer à gauche ou tirer à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IxrNQjJCa-WiLzoe0zPojQ.png)
_Le tableau représente les approximations des Q-valeurs_

Nous apprenons avec une expérience ordonnée. Supposons que nous savons que si nous tirons sur un monstre, la probabilité que le monstre suivant vienne de la même direction est de 70 %. Dans notre cas, c'est la corrélation entre nos tuples d'expérience.

Commençons l'entraînement. Notre agent voit le monstre à droite et tire dessus en utilisant l'arme de droite. C'est correct !

Ensuite, le monstre suivant vient également de la droite (avec une probabilité de 70 %), et l'agent tirera avec l'arme de droite. Encore une fois, c'est bien !

Et ainsi de suite...

![Image](https://cdn-media-1.freecodecamp.org/images/1*Eg4HoqjJstVq9fhdfPQrKQ.png)
_L'arme rouge est l'action prise_

Le problème est que cette approche augmente la valeur de l'utilisation de l'arme de droite dans tout l'espace d'états.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hHNtNnRnFWoVegKQdTRLNA.png)
_Nous pouvons voir que la Q-valeur pour le monstre étant à gauche et tirant avec l'arme de droite est positive (même si ce n'est pas rationnel)_

Et si notre agent ne voit pas beaucoup d'exemples à gauche (puisque seulement 30 % viendront probablement de la gauche), notre agent finira par choisir la droite indépendamment de l'endroit d'où vient le monstre. Ce n'est pas rationnel du tout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pTDJxVIg6GHn5gLv_myczw.png)
_Même si le monstre vient à gauche, notre agent tirera avec l'arme de droite_

Nous avons deux stratégies parallèles pour gérer ce problème.

Tout d'abord, nous devons arrêter d'apprendre tout en interagissant avec l'environnement. Nous devrions essayer différentes choses et jouer un peu au hasard pour explorer l'espace d'états. Nous pouvons sauvegarder ces expériences dans le tampon de replay.

Ensuite, nous pouvons rappeler ces expériences et apprendre d'elles. Après cela, retournez jouer avec la fonction de valeur mise à jour.

Par conséquent, nous aurons un meilleur ensemble d'exemples. Nous pourrons généraliser des motifs à partir de ces exemples, les rappelant dans n'importe quel ordre.

Cela aide à éviter de se fixer sur une région de l'espace d'états. Cela empêche de renforcer la même action encore et encore.

Cette approche peut être vue comme une forme d'apprentissage supervisé.

Nous verrons dans les futurs articles que nous pouvons également utiliser le "prioritized experience replay". Cela nous permet de présenter des tuples rares ou "importants" au réseau de neurones plus fréquemment.

### **Notre algorithme de Deep Q-Learning**

D'abord un peu de mathématiques :

[Souvenez-vous que nous mettons à jour notre Q-valeur](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe) pour un état et une action donnés en utilisant l'équation de Bellman :

![Image](https://cdn-media-1.freecodecamp.org/images/1*js8r4Aq2ZZoiLK0mMp_ocg.png)

Dans notre cas, nous voulons mettre à jour les poids de notre réseau de neurones pour réduire l'erreur.

L'erreur (ou erreur TD) est calculée en prenant la différence entre notre Q_target (valeur maximale possible de l'état suivant) et Q_value (notre prédiction actuelle de la Q-valeur)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zplt-1wTWu_7BGmZCBFjbQ.png)

```
Initialiser l'environnement Doom E
Initialiser la mémoire de replay M avec une capacité N (= capacité finie)
Initialiser les poids du DQN w
pour épisode dans max_épisode :
    s = État de l'environnement
    pour étapes dans max_étapes :
        Choisir l'action a à partir de l'état s en utilisant epsilon greedy.
        Prendre l'action a, obtenir r (récompense) et s' (état suivant)
        Stocker le tuple d'expérience <s, a, r, s'> dans M
        s = s' (état = nouvel_état)
        Obtenir un minibatch aléatoire de tuples d'expérience de M
        Définir Q_target = récompense(s,a) + γmaxQ(s')
        Mettre à jour w = α(Q_target - Q_value) * ∇w Q_value
```

Il y a deux processus qui se déroulent dans cet algorithme :

* Nous échantillonnons l'environnement où nous effectuons des actions et stockons les tuples d'expérience observés dans une mémoire de replay.
* Sélectionnez le petit lot de tuples aléatoires et apprenez-en en utilisant une étape de mise à jour de descente de gradient.

### **Implémentons notre Deep Q Neural Network**

> Nous avons fait une vidéo où nous implémentons un agent Deep Q-learning avec Tensorflow qui apprend à jouer à Atari Space Invaders 🎮🚀.

Maintenant que nous savons comment cela fonctionne, nous allons implémenter notre Deep Q Neural Network étape par étape. Chaque étape et chaque partie du code est expliquée directement dans le notebook Jupyter lié ci-dessous.

Vous pouvez y accéder dans le [dépôt du cours Deep Reinforcement Learning](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/tree/master/DQN/doom).

C'est tout ! Vous venez de créer un agent qui apprend à jouer à Doom. Génial !

N'oubliez pas d'implémenter chaque partie du code par vous-même. Il est vraiment important d'essayer de modifier le code que je vous ai donné. Essayez d'ajouter des époques, changez l'architecture, ajoutez des Q-valeurs fixes, changez le taux d'apprentissage, utilisez un environnement plus difficile (comme Health Gathering)... et ainsi de suite. Amusez-vous !

Dans le prochain article, je discuterai des dernières améliorations du Deep Q-learning :

* Q-valeurs fixes
* Prioritized Experience Replay
* Double DQN
* Dueling Networks

Mais la prochaine fois, nous travaillerons sur les Policy Gradients en entraînant un agent qui joue à Doom, et nous essaierons de survivre dans un environnement hostile en collectant de la santé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dNEZ6GX3Fp4DCLj59XrnFQ.gif)

Si vous avez aimé mon article, **veuillez cliquer sur le 👏 ci-dessous autant de fois que vous avez aimé l'article** afin que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou me tweeter [@ThomasSimonini](https://twitter.com/ThomasSimonini).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

Continuez à apprendre, restez génial !

#### Cours de Deep Reinforcement Learning avec Tensorflow 🏁

📜 [Programme](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)

🎥 [Version vidéo](https://www.youtube.com/channel/UC8XuSf1eD9AF8x8J19ha5og?view_as=subscriber)

Partie 1 : [Une introduction au Reinforcement Learning](https://medium.com/p/4339519de419/edit)

Partie 2 : [Plonger plus profondément dans le Reinforcement Learning avec le Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)

Partie 3 : [Une introduction au Deep Q-Learning : jouons à Doom](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)

Partie 3+ : [Améliorations dans le Deep Q Learning : Dueling Double DQN, Prioritized Experience Replay, et Q-targets fixes](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)

Partie 4 : [Une introduction aux Policy Gradients avec Doom et Cartpole](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f)

Partie 5 : [Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the Hedgehog !](https://medium.freecodecamp.org/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d)

Partie 6 : [Proximal Policy Optimization (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e)

Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)