---
title: Une introduction aux Policy Gradients avec Cartpole et Doom
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T18:25:15.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q00eKh5Tl9325LyfZrMwZA.png
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
seo_title: Une introduction aux Policy Gradients avec Cartpole et Doom
seo_desc: 'By Thomas Simonini


  This article is part of Deep Reinforcement Learning Course with Tensorflow ?️. Check
  the syllabus here.


  In the last two articles about Q-learning and Deep Q learning, we worked with value-based
  reinforcement learning algorithms. ...'
---

Par Thomas Simonini

> Cet article fait partie du cours Deep Reinforcement Learning avec Tensorflow 🏁. Consultez le programme [ici](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

Dans les deux derniers articles sur [Q-learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe) et [Deep Q learning](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8), nous avons travaillé avec des algorithmes d'apprentissage par renforcement basés sur la valeur. Pour choisir quelle action entreprendre étant donné un état, nous prenons l'action avec la valeur Q la plus élevée (récompense future maximale attendue que je vais obtenir à chaque état). Par conséquent, dans l'apprentissage basé sur la valeur, une politique n'existe que grâce à ces estimations de valeur d'action.

Aujourd'hui, nous allons apprendre une technique d'apprentissage par renforcement basée sur les politiques appelée Policy Gradients.

Nous allons implémenter deux agents. Le premier apprendra à garder la barre en équilibre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wj5RZ_EqKIeCQ4E7DgdvCw.gif)

Le second sera un agent qui apprend à survivre dans un environnement hostile de Doom en collectant des points de vie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dNEZ6GX3Fp4DCLj59XrnFQ.gif)
_Notre agent Policy Gradients_

Dans les méthodes basées sur les politiques, au lieu d'apprendre une fonction de valeur qui nous dit quelle est la somme attendue des récompenses étant donné un état et une action, nous apprenons directement la fonction de politique qui mappe l'état à l'action (sélectionner des actions sans utiliser une fonction de valeur).

Cela signifie que nous essayons directement d'optimiser notre fonction de politique π sans nous soucier d'une fonction de valeur. Nous allons directement paramétrer π (sélectionner une action sans une fonction de valeur).

Bien sûr, nous pouvons utiliser une fonction de valeur pour optimiser les paramètres de la politique. Mais la fonction de valeur ne sera pas utilisée pour sélectionner une action.

Dans cet article, vous apprendrez :

* Qu'est-ce que Policy Gradient, et ses avantages et inconvénients
* Comment l'implémenter dans Tensorflow.

### Pourquoi utiliser des méthodes basées sur les politiques ?

#### Deux types de politiques

Une politique peut être soit déterministe soit stochastique.

Une politique déterministe est une politique qui mappe les états aux actions. Vous lui donnez un état et la fonction retourne une action à entreprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NDEGtK42rEpYLkTPg2LBPA.png)

Les politiques déterministes sont utilisées dans des environnements déterministes. Ce sont des environnements où les actions entreprises déterminent le résultat. Il n'y a pas d'incertitude. Par exemple, lorsque vous jouez aux échecs et que vous déplacez votre pion de A2 à A3, vous êtes sûr que votre pion se déplacera à A3.

D'autre part, une politique stochastique produit une distribution de probabilité sur les actions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YCABimP7x1wZZZKqz2CoyQ.png)

Cela signifie qu'au lieu d'être sûr de prendre l'action _a_ (par exemple à gauche), il y a une probabilité que nous prenions une action différente (dans ce cas, 30 % que nous prenions sud).

La politique stochastique est utilisée lorsque l'environnement est incertain. Nous appelons ce processus un Processus de Décision de Markov Partiellement Observable (POMDP).

La plupart du temps, nous utiliserons ce second type de politique.

#### Avantages

> Mais le Deep Q Learning est vraiment génial ! Pourquoi utiliser des méthodes d'apprentissage par renforcement basées sur les politiques ?

Il y a trois avantages principaux à utiliser les Policy Gradients.

#### Convergence

Tout d'abord, les méthodes basées sur les politiques ont de meilleures propriétés de convergence.

Le problème avec les méthodes basées sur la valeur est qu'elles peuvent avoir de grandes oscillations pendant l'entraînement. Cela est dû au fait que le choix de l'action peut changer de manière dramatique pour un changement arbitrairement petit dans les valeurs d'action estimées.

D'autre part, avec le gradient de politique, nous suivons simplement le gradient pour trouver les meilleurs paramètres. Nous voyons une mise à jour fluide de notre politique à chaque étape.

Parce que nous suivons le gradient pour trouver les meilleurs paramètres, nous sommes garantis de converger vers un maximum local (pire cas) ou un maximum global (meilleur cas).

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lYcY5TBSqfNwdu8TduB6g.png)

#### Les gradients de politique sont plus efficaces dans les espaces d'action de haute dimension

Le deuxième avantage est que les gradients de politique sont plus efficaces dans les espaces d'action de haute dimension, ou lors de l'utilisation d'actions continues.

Le problème avec le Deep Q-learning est que leurs prédictions attribuent un score (récompense future maximale attendue) pour chaque action possible, à chaque étape de temps, étant donné l'état actuel.

Mais que se passe-t-il si nous avons une possibilité infinie d'actions ?

Par exemple, avec une voiture autonome, à chaque état, vous pouvez avoir un choix (presque) infini d'actions (tourner le volant à 15°, 17,2°, 19,4°, klaxonner…). Nous devrons produire une valeur Q pour chaque action possible !

D'autre part, dans les méthodes basées sur les politiques, vous ajustez simplement les paramètres directement : grâce à cela, vous commencerez à comprendre ce que sera le maximum, plutôt que de calculer (estimer) le maximum directement à chaque étape.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_hAkM4RIxjKjKqAYFR_9CQ.png)

#### Les gradients de politique peuvent apprendre des politiques stochastiques

Un troisième avantage est que le gradient de politique peut apprendre une politique stochastique, alors que les fonctions de valeur ne le peuvent pas. Cela a deux conséquences.

L'une d'entre elles est que nous n'avons pas besoin d'implémenter un compromis exploration/exploitation. Une politique stochastique permet à notre agent d'explorer l'espace d'état sans toujours prendre la même action. Cela est dû au fait qu'elle produit une distribution de probabilité sur les actions. Par conséquent, elle gère le compromis exploration/exploitation sans le coder en dur.

Nous nous débarrassons également du problème d'aliasing perceptuel. L'aliasing perceptuel se produit lorsque nous avons deux états qui semblent être (ou sont réellement) les mêmes, mais qui nécessitent des actions différentes.

Prenons un exemple. Nous avons un aspirateur intelligent, et son objectif est d'aspirer la poussière et d'éviter de tuer les hamsters.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zy9JMzCF3zwWDbjPaiKd2w.png)
_Cet exemple a été inspiré par l'excellent cours de David Silver : [http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/pg.pdf](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/pg.pdf" rel="noopener" target="_blank" title=")_

Notre aspirateur ne peut percevoir que l'emplacement des murs.

Le problème : les deux cas rouges sont des états aliasés, car l'agent perçoit un mur supérieur et un mur inférieur pour chacun des deux.

Sous une politique déterministe, la politique sera soit de se déplacer à droite lorsque l'état est rouge, soit de se déplacer à gauche. Dans les deux cas, notre agent sera bloqué et ne pourra jamais aspirer la poussière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V-jY8KezWKfsca_DExtXPQ.png)

Sous un algorithme RL basé sur la valeur, nous apprenons une politique quasi-déterministe (stratégie "epsilon greedy"). Par conséquent, notre agent peut passer beaucoup de temps avant de trouver la poussière.

D'autre part, une politique stochastique optimale se déplacera aléatoirement à gauche ou à droite dans les états gris. Par conséquent, elle ne sera pas bloquée et atteindra l'état objectif avec une probabilité élevée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zwe5kBczuErX8c0TH3rAmg.png)

#### Inconvénients

Naturellement, les Policy Gradients ont un grand inconvénient. La plupart du temps, ils convergent vers un maximum local plutôt que vers l'optimum global.

Au lieu du Deep Q-Learning, qui essaie toujours d'atteindre le maximum, les Policy Gradients convergent plus lentement, étape par étape. Ils peuvent prendre plus de temps à s'entraîner.

Cependant, nous verrons qu'il existe des solutions à ce problème.

### Recherche de politique

Nous avons notre politique π qui a un paramètre θ. Ce π produit une distribution de probabilité des actions.

![Image](https://cdn-media-1.freecodecamp.org/images/0*354cfoILK19WFTWa.)
_Probabilité de prendre l'action a étant donné l'état s avec les paramètres theta._

Génial ! Mais comment savons-nous si notre politique est bonne ?

Rappelez-vous que la politique peut être vue comme un problème d'optimisation. Nous devons trouver les meilleurs paramètres (θ) pour maximiser une fonction de score, J(θ).

![Image](https://cdn-media-1.freecodecamp.org/images/0*PfUAJaIGoEsvfbCG.)

Il y a deux étapes :

* Mesurer la qualité d'une π (politique) avec une fonction de score de politique J(θ)
* Utiliser l'ascension du gradient de politique pour trouver le meilleur paramètre θ qui améliore notre π.

L'idée principale ici est que J(θ) nous dira à quel point notre π est bonne. L'ascension du gradient de politique nous aidera à trouver les meilleurs paramètres de politique pour maximiser l'échantillon des bonnes actions.

#### Première étape : la fonction de score de politique J(θ)

Pour mesurer à quel point notre politique est bonne, nous utilisons une fonction appelée fonction objectif (ou fonction de score de politique) qui calcule la récompense attendue de la politique.

Trois méthodes fonctionnent également bien pour optimiser les politiques. Le choix dépend uniquement de l'environnement et des objectifs que vous avez.

Tout d'abord, dans un environnement épisodique, nous pouvons utiliser la valeur de départ. Calculez la moyenne du retour à partir de la première étape de temps (G1). Il s'agit de la récompense cumulée actualisée pour l'épisode entier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tP4l4IrIG3aMLTrMt-1-HA.png)

L'idée est simple. Si je commence toujours dans un certain état s1, quelle est la récompense totale que j'obtiendrai à partir de cet état de départ jusqu'à la fin ?

Nous voulons trouver la politique qui maximise G1, car elle sera la politique optimale. Cela est dû à l'hypothèse de récompense [expliquée dans le premier article](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419).

Par exemple, dans Breakout, je joue une nouvelle partie, mais j'ai perdu la balle après 20 briques détruites (fin de la partie). Les nouveaux épisodes commencent toujours au même état.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bNljRIeIigzMKh_F.png)

Je calcule le score en utilisant J1(θ). Frapper 20 briques est bien, mais je veux améliorer le score. Pour cela, je devrai améliorer les distributions de probabilité de mes actions en ajustant les paramètres. Cela se produit dans l'étape 2.

Dans un environnement continu, nous pouvons utiliser la valeur moyenne, car nous ne pouvons pas nous fier à un état de départ spécifique.

Chaque valeur d'état est maintenant pondérée (parce que certaines se produisent plus que d'autres) par la probabilité de l'occurrence de l'état respecté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S-XLkrvPuVUqLrFW1hmIMg.png)

Troisièmement, nous pouvons utiliser la récompense moyenne par étape de temps. L'idée ici est que nous voulons obtenir le plus de récompense par étape de temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3SejRRby6vAnThZ8c2UaQg.png)

#### Deuxième étape : l'ascension du gradient de politique

Nous avons une fonction de score de politique qui nous dit à quel point notre politique est bonne. Maintenant, nous voulons trouver un paramètre θ qui maximise cette fonction de score. Maximiser la fonction de score signifie trouver la politique optimale.

Pour maximiser la fonction de score J(θ), nous devons faire une ascension de gradient sur les paramètres de la politique.

L'ascension de gradient est l'inverse de la descente de gradient. Rappelez-vous que le gradient pointe toujours vers le changement le plus raide.

Dans la descente de gradient, nous prenons la direction de la diminution la plus raide de la fonction. Dans l'ascension de gradient, nous prenons la direction de l'augmentation la plus raide de la fonction.

Pourquoi l'ascension de gradient et non la descente de gradient ? Parce que nous utilisons la descente de gradient lorsque nous avons une fonction d'erreur que nous voulons minimiser.

Mais la fonction de score n'est pas une fonction d'erreur ! C'est une fonction de score, et parce que nous voulons maximiser le score, nous avons besoin de l'ascension de gradient.

L'idée est de trouver le gradient de la politique actuelle π qui met à jour les paramètres dans la direction de la plus grande augmentation, et itérer.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oh-lF13hYWt2Bd6V.)

D'accord, maintenant implémentons cela mathématiquement. Cette partie est un peu difficile, mais il est fondamental de comprendre comment nous arrivons à notre formule de gradient.

Nous voulons trouver les meilleurs paramètres θ*, qui maximisent le score :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xoGZI5v6lBS8s5OtBteJMA.png)

Notre fonction de score peut être définie comme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dl4Fp0Izhv6bC0-qgThByA.png)

Qui est la somme totale de la récompense attendue étant donné la politique.

Maintenant, parce que nous voulons faire une ascension de gradient, nous devons différencier notre fonction de score J(θ).

Notre fonction de score J(θ) peut également être définie comme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qySDorYr55KgVJ6H3bu_6Q.png)

Nous avons écrit la fonction de cette manière pour montrer le problème auquel nous sommes confrontés ici.

Nous savons que les paramètres de la politique changent la manière dont les actions sont choisies, et par conséquent, les récompenses que nous obtenons et les états que nous verrons et à quelle fréquence.

Il peut donc être difficile de trouver les changements de politique de manière à garantir une amélioration. Cela est dû au fait que la performance dépend des sélections d'actions et de la distribution des états dans lesquels ces sélections sont faites.

Ces deux aspects sont affectés par les paramètres de la politique. L'effet des paramètres de la politique sur les actions est simple à trouver, mais comment trouver l'effet de la politique sur la distribution des états ? La fonction de l'environnement est inconnue.

Par conséquent, nous sommes confrontés à un problème : comment estimer le ∇ (gradient) par rapport à la politique θ, lorsque le gradient dépend de l'effet inconnu des changements de politique sur la distribution des états ?

La solution sera d'utiliser le Théorème du Gradient de Politique. Cela fournit une expression analytique pour le gradient ∇ de J(θ) (performance) par rapport à la politique θ qui ne nécessite pas la différentiation de la distribution des états.

Calculons donc :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dl4Fp0Izhv6bC0-qgThByA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*i72jd_Hrimu9Aag70WGDmQ.png)

Rappelez-vous, nous sommes dans une situation de politique stochastique. Cela signifie que notre politique produit une distribution de probabilité π(τ ; θ). Elle produit la probabilité de prendre cette série d'étapes (s0, a0, r0…), étant donné nos paramètres actuels θ.

Mais différencier une fonction de probabilité est difficile, sauf si nous pouvons la transformer en logarithme. Cela la rend beaucoup plus simple à différencier.

Ici, nous utiliserons l'[astuce du rapport de vraisemblance](http://blog.shakirm.com/2015/11/machine-learning-trick-of-the-day-5-log-derivative-trick/) qui remplace la fraction résultante par une probabilité logarithmique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iKhO5anOAfc3oqJOM2i_8A.png)

Maintenant, convertissons la somme en une attente :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4Y7BwUu2JBRIJ8bxXkzDjg.png)

Comme vous pouvez le voir, nous devons seulement calculer la dérivée de la fonction de politique logarithmique.

Maintenant que nous avons fait cela, et c'était beaucoup, nous pouvons conclure sur les gradients de politique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zjEh737KfmDUzNECjW4e4w.png)

Ce gradient de politique nous dit comment nous devons déplacer la distribution de la politique en changeant les paramètres θ si nous voulons obtenir un score plus élevé.

R(τ) est comme un score de valeur scalaire :

* Si R(τ) est élevé, cela signifie qu'en moyenne nous avons pris des actions qui ont conduit à des récompenses élevées. Nous voulons augmenter les probabilités des actions vues (augmenter la probabilité de prendre ces actions).
* D'autre part, si R(τ) est faible, nous voulons diminuer les probabilités des actions vues.

Ce gradient de politique fait que les paramètres se déplacent le plus dans la direction qui favorise les actions qui ont le retour le plus élevé.

### Monte Carlo Policy Gradients

Dans notre notebook, nous utiliserons cette approche pour concevoir l'algorithme de gradient de politique. Nous utilisons Monte Carlo parce que nos tâches peuvent être divisées en épisodes.

```
Initialiser θ
pour chaque épisode τ = S0, A0, R1, S1, …, ST :
    pour t <-- 1 à T-1 :
        Δθ = α ∇θ(log π(St, At, θ)) Gt
        θ = θ + Δθ
```

```
Pour chaque épisode :
    À chaque étape de temps dans cet épisode :
         Calculer les probabilités logarithmiques produites par notre fonction de politique. Multiplier par la fonction de score.
         Mettre à jour les poids
```

Mais nous sommes confrontés à un problème avec cet algorithme. Parce que nous ne calculons R qu'à la fin de l'épisode, nous faisons la moyenne de toutes les actions. Même si certaines des actions entreprises étaient très mauvaises, si notre score est assez élevé, nous ferons la moyenne de toutes les actions comme bonnes.

Ainsi, pour avoir une politique correcte, nous avons besoin de beaucoup d'échantillons… ce qui entraîne un apprentissage lent.

### Comment améliorer notre modèle ?

Nous verrons dans les prochains articles quelques améliorations :

* Actor Critic : un hybride entre les algorithmes basés sur la valeur et les algorithmes basés sur les politiques.
* Proximal Policy Gradients : garantit que la déviation par rapport à la politique précédente reste relativement faible.

### Implémentons-le avec Cartpole et Doom

> Nous avons fait une vidéo où nous implémentons un **agent Policy Gradient avec Tensorflow qui apprend à jouer à Doom 💀 dans un environnement Deathmatch.**

**Vous pouvez accéder directement aux notebooks dans le [dépôt du cours Deep Reinforcement Learning](https://github.com/simoninithomas/Deep_reinforcement_learning_Course).**

**Cartpole :**

**Doom :**

**C'est tout ! Vous venez de créer un agent qui apprend à survivre dans un environnement Doom. Génial !**

**N'oubliez pas d'implémenter chaque partie du code par vous-même. Il est vraiment important d'essayer de modifier le code que je vous ai donné. Essayez d'ajouter des époques, de changer l'architecture, de changer le taux d'apprentissage, d'utiliser un environnement plus difficile… et ainsi de suite. Amusez-vous !**

**Dans le prochain article, je discuterai des dernières améliorations du Deep Q-learning :**

* **Valeurs Q fixes**
* **Replay d'expérience prioritaire**
* **Double DQN**
* **Réseaux Dueling**

**Si vous avez aimé mon article, **cliquez sur le 💙 ci-dessous autant de fois que vous avez aimé l'article** afin que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !**

**Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou à me tweeter [@ThomasSimonini](https://twitter.com/ThomasSimonini).**

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

#### **Continuez à apprendre, restez génial !**

#### **Cours de Deep Reinforcement Learning avec Tensorflow 🏁**

**📋 S[yllabus](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)**

**🎥 V[ersion vidéo](https://www.youtube.com/channel/UC8XuSf1eD9AF8x8J19ha5og?view_as=subscriber)**

**Partie 1 : [Une introduction à l'apprentissage par renforcement](https://medium.com/p/4339519de419/edit)**

**Partie 2 : [Plonger plus profondément dans l'apprentissage par renforcement avec Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)**

**Partie 3 : [Une introduction au Deep Q-Learning : jouons à Doom](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)**

**Partie 3+ : [Améliorations du Deep Q Learning : Dueling Double DQN, Prioritized Experience Replay, et Q-targets fixes](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)**

**Partie 4 : [Une introduction aux Policy Gradients avec Doom et Cartpole](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f)**

**Partie 5 : [Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the Hedgehog !](https://medium.freecodecamp.org/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d)**

**Partie 6 : [Proximal Policy Optimization (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e)**

**Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)**