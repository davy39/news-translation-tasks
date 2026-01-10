---
title: Une introduction à l'apprentissage par renforcement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T06:16:59.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-reinforcement-learning-4339519de419
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0gd5LIk1e7RWF3HygxgH-g.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: 'tech '
  slug: tech
seo_title: Une introduction à l'apprentissage par renforcement
seo_desc: 'By Thomas Simonini

  Reinforcement learning is an important type of Machine Learning where an agent learn
  how to behave in a environment by performing actions and seeing the results.

  In recent years, we’ve seen a lot of improvements in this fascinating...'
---

Par Thomas Simonini

L'apprentissage par renforcement est un type important de Machine Learning où un agent apprend à se comporter dans un environnement en effectuant des actions et en voyant les résultats.

Ces dernières années, nous avons vu de nombreuses améliorations dans ce domaine de recherche fascinant. Parmi les exemples, citons [DeepMind et l'architecture Deep Q learning](https://deepmind.com/research/dqn/) en 2014, [battre le champion du jeu de Go avec AlphaGo](https://deepmind.com/research/alphago/) en 2016, [OpenAI et le PPO](https://blog.openai.com/openai-baselines-ppo/) en 2017, parmi d'autres.

Dans cette série d'articles, nous nous concentrerons sur l'apprentissage des différentes architectures utilisées aujourd'hui pour résoudre les problèmes d'apprentissage par renforcement. Celles-ci incluront Q-learning, Deep Q-learning, Policy Gradients, Actor Critic, et PPO.

Dans cet premier article, vous apprendrez :

* Qu'est-ce que l'apprentissage par renforcement et comment les récompenses sont l'idée centrale
* Les trois approches de l'apprentissage par renforcement
* Ce que signifie le "Deep" dans Deep Reinforcement Learning

Il est vraiment important de maîtriser ces éléments avant de plonger dans l'implémentation d'agents de Deep Reinforcement Learning.

L'idée derrière l'apprentissage par renforcement est qu'un agent apprendra de l'environnement en interagissant avec lui et en recevant des récompenses pour avoir effectué des actions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zySSJwywQGerKSbjHBtkyg.png)

Apprendre de l'interaction avec l'environnement vient de nos expériences naturelles. Imaginez que vous êtes un enfant dans un salon. Vous voyez une cheminée et vous vous en approchez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aQuWM51KnoGIUGTGNzoRIw.png)

C'est chaud, c'est positif, vous vous sentez bien _(Récompense positive +1)_. Vous comprenez que le feu est une chose positive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5shp6Uzu7XT41vrOJ7-3gw.png)

Mais ensuite, vous essayez de toucher le feu. Aïe ! Cela brûle votre main _(Récompense négative -1)_. Vous venez de comprendre que le feu est positif lorsque vous êtes à une distance suffisante, car il produit de la chaleur. Mais si vous vous en approchez trop, vous serez brûlé.

C'est ainsi que les humains apprennent, par l'interaction. L'apprentissage par renforcement est simplement une approche computationnelle de l'apprentissage par l'action.

### Le processus d'apprentissage par renforcement

![Image](https://cdn-media-1.freecodecamp.org/images/1*aKYFRoEmmKkybqJOvLt2JQ.png)

Imaginons un agent apprenant à jouer à Super Mario Bros comme exemple concret. Le processus d'apprentissage par renforcement (RL) peut être modélisé comme une boucle qui fonctionne ainsi :

* Notre agent reçoit **l'état S0** de **l'environnement** (Dans notre cas, nous recevons la première image de notre jeu (état) de Super Mario Bros (environnement))
* Sur la base de cet **état S0**, l'agent effectue une **action A0** (notre agent se déplacera vers la droite)
* L'environnement passe à un **nouvel** **état S1** (nouvelle image)
* L'environnement donne une **récompense R1** à l'agent (non mort : +1)

Cette boucle RL produit une séquence d'**état, action et récompense**.

Le but de l'agent est de maximiser la récompense cumulative attendue.

#### L'idée centrale de l'hypothèse de récompense

Pourquoi le but de l'agent est-il de maximiser la récompense cumulative attendue ?

Eh bien, l'apprentissage par renforcement est basé sur l'idée de l'hypothèse de récompense. Tous les objectifs peuvent être décrits par la maximisation de la récompense cumulative attendue.

**C'est pourquoi en apprentissage par renforcement, pour avoir le meilleur comportement, nous devons maximiser la récompense cumulative attendue.**

La récompense cumulative à chaque étape de temps t peut être écrite comme :

![Image](https://cdn-media-1.freecodecamp.org/images/0*ylz4lplMffGQR_g3.)

Ce qui est équivalent à :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AFAuM1Y8zmso4yB5mOApZA.png)
_Merci à [Pierre-Luc Bacon](https://twitter.com/pierrelux" rel="noopener" target="_blank" title=") pour la correction_

Cependant, en réalité, nous ne pouvons pas simplement additionner les récompenses comme cela. Les récompenses qui arrivent plus tôt (au début du jeu) sont plus probables à se produire, car elles sont plus prévisibles que la récompense future à long terme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tciNrjN6pW60-h0PiQRiXg.png)

Disons que votre agent est cette petite souris et votre adversaire est le chat. Votre objectif est de manger la quantité maximale de fromage avant d'être mangé par le chat.

Comme nous pouvons le voir dans le diagramme, il est plus probable de manger le fromage près de nous que le fromage proche du chat (plus nous sommes proches du chat, plus c'est dangereux).

Par conséquent, la récompense près du chat, même si elle est plus grande (plus de fromage), sera actualisée. Nous ne sommes pas vraiment sûrs de pouvoir la manger.

Pour actualiser les récompenses, nous procédons comme suit :

Nous définissons un taux d'actualisation appelé gamma. Il doit être compris entre 0 et 1.

* Plus le gamma est grand, plus l'actualisation est faible. Cela signifie que l'agent d'apprentissage se soucie davantage de la récompense à long terme.
* En revanche, plus le gamma est petit, plus l'actualisation est grande. Cela signifie que notre agent se soucie davantage de la récompense à court terme (le fromage le plus proche).

Notre récompense cumulative actualisée attendue est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zrzRTXt8rtWF5fX__kZ-yQ.png)
_Merci à [Pierre-Luc Bacon](https://twitter.com/pierrelux" rel="noopener" target="_blank" title=") pour la correction_

Pour simplifier, chaque récompense sera actualisée par gamma à l'exposant de l'étape de temps. À mesure que l'étape de temps augmente, le chat se rapproche de nous, donc la récompense future est de moins en moins probable à se produire.

### Tâches épisodiques ou continues

Une tâche est une instance d'un problème d'apprentissage par renforcement. Nous pouvons avoir deux types de tâches : épisodiques et continues.

#### **Tâche épisodique**

Dans ce cas, nous avons un point de départ et un point de fin **(un état terminal). Cela crée un épisode** : une liste d'états, d'actions, de récompenses et de nouveaux états.

Par exemple, pensez à Super Mario Bros, un épisode commence au lancement d'un nouveau Mario et se termine : lorsque vous êtes tué ou que vous atteignez la fin du niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PPs51sGAtRKJft0iUCw6VA.png)
_Début d'un nouvel épisode_

#### Tâches continues

**Ce sont des tâches qui continuent indéfiniment (pas d'état terminal).** Dans ce cas, l'agent doit apprendre à choisir les meilleures actions et interagir simultanément avec l'environnement.

Par exemple, un agent qui fait du trading automatique d'actions. Pour cette tâche, il n'y a pas de point de départ et d'état terminal. **L'agent continue de fonctionner jusqu'à ce que nous décidions de l'arrêter.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*5T_Ta3QauHUEMUCzev6Wyw.jpeg)

### Méthodes d'apprentissage Monte Carlo vs TD

Nous avons deux façons d'apprendre :

* Collecter les récompenses **à la fin de l'épisode** puis calculer la **récompense future maximale attendue** : _Approche Monte Carlo_
* Estimer **les récompenses à chaque étape** : _Apprentissage par différence temporelle_

#### Monte Carlo

Lorsque l'épisode se termine (l'agent atteint un "état terminal"), **l'agent regarde la récompense cumulative totale pour voir comment il s'en est sorti.** Dans l'approche Monte Carlo, les récompenses ne sont **reçues qu'à la fin du jeu.**

Ensuite, nous commençons un nouveau jeu avec les connaissances ajoutées. **L'agent prend de meilleures décisions à chaque itération.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RLLzQl4YadpbhPlxpa5f6A.png)

Prenons un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tciNrjN6pW60-h0PiQRiXg.png)

Si nous prenons l'environnement du labyrinthe :

* Nous commençons toujours au même point de départ.
* Nous terminons l'épisode si le chat nous mange ou si nous nous déplaçons > 20 étapes.
* À la fin de l'épisode, nous avons une liste d'états, d'actions, de récompenses et de nouveaux états.
* L'agent additionnera les récompenses totales Gt (pour voir comment il s'en est sorti).
* Il mettra ensuite à jour V(st) en fonction de la formule ci-dessus.
* Puis commencera un nouveau jeu avec cette nouvelle connaissance.

En exécutant de plus en plus d'épisodes, **l'agent apprendra à jouer de mieux en mieux.**

#### Apprentissage par différence temporelle : apprendre à chaque étape de temps

L'apprentissage TD, en revanche, n'attendra pas la fin de l'épisode pour mettre à jour **l'estimation de la récompense future maximale attendue : il mettra à jour son estimation de valeur V pour les états non terminaux St survenant lors de cette expérience.**

Cette méthode est appelée TD(0) ou **TD à une étape (mise à jour de la fonction de valeur après toute étape individuelle).**

![Image](https://cdn-media-1.freecodecamp.org/images/1*LLfj11fivpkKZkwQ8uPi3A.png)

Les méthodes TD **n'attendent que jusqu'à l'étape de temps suivante pour mettre à jour les estimations de valeur.** À l'étape t+1, elles forment immédiatement **une cible TD en utilisant la récompense observée Rt+1 et l'estimation actuelle V(St+1).**

La cible TD est une estimation : en fait, vous mettez à jour l'estimation précédente V(St) **en la mettant à jour vers une cible à une étape.**

### Compromis exploration/exploitation

Avant de regarder les différentes stratégies pour résoudre les problèmes d'apprentissage par renforcement, nous devons aborder un autre sujet très important : le compromis exploration/exploitation.

* L'exploration consiste à trouver plus d'informations sur l'environnement.
* L'exploitation consiste à exploiter les informations connues pour maximiser la récompense.

Rappelez-vous, le but de notre agent RL est de maximiser la récompense cumulative attendue. Cependant, nous pouvons tomber dans un piège courant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*APLmZ8CVgu0oY3sQBVYIuw.png)

Dans ce jeu, notre souris peut avoir une quantité infinie de petits fromages (+1 chacun). Mais en haut du labyrinthe, il y a une énorme quantité de fromage (+1000).

Cependant, si nous nous concentrons uniquement sur la récompense, notre agent n'atteindra jamais l'énorme quantité de fromage. Au lieu de cela, il n'exploitera que la source de récompenses la plus proche, même si cette source est petite (exploitation).

Mais si notre agent fait un peu d'exploration, il peut trouver la grande récompense.

C'est ce que nous appelons le compromis exploration/exploitation. Nous devons définir une règle qui aide à gérer ce compromis. Nous verrons dans les futurs articles différentes façons de le gérer.

### Trois approches de l'apprentissage par renforcement

Maintenant que nous avons défini les éléments principaux de l'apprentissage par renforcement, passons aux trois approches pour résoudre un problème d'apprentissage par renforcement. Il s'agit des approches basées sur la valeur, basées sur la politique et basées sur le modèle.

#### Basée sur la valeur

Dans l'apprentissage par renforcement basé sur la valeur, le but est d'optimiser la fonction de valeur _V(s)_.

La fonction de valeur est une fonction qui nous indique la récompense future maximale attendue que l'agent obtiendra à chaque état.

La valeur de chaque état est le montant total de la récompense qu'un agent peut s'attendre à accumuler dans le futur, en commençant par cet état.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kvtRAhBZO-h77Iw1.)

L'agent utilisera cette fonction de valeur pour sélectionner quel état choisir à chaque étape. L'agent prend l'état avec la plus grande valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2_JRk-4O523bcOcSy1u31g.png)

Dans l'exemple du labyrinthe, à chaque étape, nous prendrons la plus grande valeur : -7, puis -6, puis -5 (et ainsi de suite) pour atteindre l'objectif.

#### Basée sur la politique

Dans l'apprentissage par renforcement basé sur la politique, nous voulons optimiser directement la fonction de politique _π(s)_ sans utiliser de fonction de valeur.

La politique est ce qui définit le comportement de l'agent à un moment donné.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8B4cAhvM-K4y9a5U.)
_action = politique(état)_

Nous apprenons une fonction de politique. Cela nous permet de mapper chaque état à la meilleure action correspondante.

Nous avons deux types de politiques :

* Déterministes : une politique à un état donné retournera toujours la même action.
* Stochastiques : sortie d'une distribution de probabilité sur les actions.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DNiQGeUl1FKunRbb.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fii7Z01laRGateAJDvloAQ.png)

Comme nous pouvons le voir ici, la politique indique directement la meilleure action à prendre pour chaque étape.

#### Basée sur le modèle

Dans l'apprentissage par renforcement basé sur le modèle, nous modélisons l'environnement. Cela signifie que nous créons un modèle du comportement de l'environnement.

Le problème est que chaque environnement nécessitera une représentation de modèle différente. C'est pourquoi nous ne parlerons pas de ce type d'apprentissage par renforcement dans les prochains articles.

### Introduction au Deep Reinforcement Learning

Le Deep Reinforcement Learning introduit des réseaux de neurones profonds pour résoudre les problèmes d'apprentissage par renforcement — d'où le nom "deep".

Par exemple, dans le prochain article, nous travaillerons sur le Q-Learning (apprentissage par renforcement classique) et le Deep Q-Learning.

Vous verrez que la différence est que dans la première approche, nous utilisons un algorithme traditionnel pour créer une table Q qui nous aide à trouver quelle action prendre pour chaque état.

Dans la deuxième approche, nous utiliserons un réseau de neurones (pour approximer la récompense basée sur l'état : valeur q).

![Image](https://cdn-media-1.freecodecamp.org/images/1*w5GuxedZ9ivRYqM_MLUxOQ.png)
_Schéma inspiré du notebook Q learning par Udacity_

Félicitations ! Il y avait beaucoup d'informations dans cet article. Assurez-vous de bien comprendre le matériel avant de continuer. Il est important de maîtriser ces éléments avant d'entrer dans la partie amusante : créer des IA qui jouent à des jeux vidéo.

Important : cet article est la première partie d'une série gratuite de billets de blog sur le Deep Reinforcement Learning. Pour plus d'informations et de ressources, [consultez le syllabus.](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)

La prochaine fois, nous travaillerons sur un agent Q-learning qui apprend à jouer au jeu Frozen Lake.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zW-o3-S4JrNpLbztKp3U4A.gif)
_FrozenLake_

Si vous avez aimé mon article, **veuillez cliquer sur le ? ci-dessous autant de fois que vous avez aimé l'article** afin que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou me tweeter [@ThomasSimonini](https://twitter.com/ThomasSimonini).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

Santé !

#### **Cours de Deep Reinforcement Learning :**

> Nous réalisons une **version vidéo du cours de Deep Reinforcement Learning avec Tensorflow** ? où nous nous concentrons sur la partie implémentation avec tensorflow [ici.](https://youtu.be/q2ZOEFAaaI0)

_Partie 1 : [Une introduction à l'apprentissage par renforcement](https://www.freecodecamp.org/news/an-introduction-to-reinforcement-learning-4339519de419/www.freecodecamp.org/news/an-introduction-to-reinforcement-learning-4339519de419/)_

_Partie 2 : [Approfondir l'apprentissage par renforcement avec le Q-Learning](https://www.freecodecamp.org/news/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe/)_

_Partie 3 : [Une introduction au Deep Q-Learning : jouons à Doom](https://www.freecodecamp.org/news/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8/)_

Partie 3+ : [Améliorations du Deep Q Learning : Dueling Double DQN, Prioritized Experience Replay, et Q-targets fixes](https://www.freecodecamp.org/news/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682/)

Partie 4 : [Une introduction aux Policy Gradients avec Doom et Cartpole](https://www.freecodecamp.org/news/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f/)

Partie 5 : [Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the Hedgehog !](https://www.freecodecamp.org/news/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d/)

Partie 6 : [Proximal Policy Optimization (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e?gi=30cae83cd9a5)

Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)