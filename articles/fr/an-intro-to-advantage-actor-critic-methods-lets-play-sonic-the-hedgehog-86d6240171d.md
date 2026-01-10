---
title: 'Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the
  Hedgehog !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T17:09:48.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aRLyiDd3jEtCSHctP58Dvw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: 'Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic
  the Hedgehog !'
seo_desc: 'By Thomas Simonini

  Since the beginning of this course, we’ve studied two different reinforcement learning
  methods:


  Value based methods (Q-learning, Deep Q-learning): where we learn a value function
  that will map each state action pair to a value. Th...'
---

Par Thomas Simonini

Depuis le [début de ce cours](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/), nous avons étudié deux méthodes différentes d'apprentissage par renforcement :

* **Méthodes basées sur la valeur** (Q-learning, Deep Q-learning) : où nous apprenons une fonction de valeur **qui mappe chaque paire état-action à une valeur.** Grâce à ces méthodes, nous trouvons la meilleure action à prendre pour chaque état — l'action avec la plus grande valeur. Cela fonctionne bien lorsque vous avez un ensemble fini d'actions.
* **Méthodes basées sur la politique** (REINFORCE avec Policy Gradients) : où nous optimisons directement la politique sans utiliser de fonction de valeur. Cela est utile lorsque l'espace d'action est continu ou stochastique. Le problème principal est de trouver une bonne fonction de score pour calculer à quel point une politique est bonne. Nous **utilisons les récompenses totales de l'épisode.**

Mais ces deux méthodes ont de grands inconvénients. C'est pourquoi, aujourd'hui, nous allons étudier un nouveau type de méthode d'apprentissage par renforcement que nous pouvons appeler une méthode "hybride" : **Actor Critic**. Nous allons utiliser deux réseaux de neurones :

* un Critic qui mesure à quel point l'action prise est bonne (basé sur la valeur)
* un Actor qui contrôle comment notre agent se comporte (basé sur la politique)

Maîtriser cette architecture est essentiel pour comprendre les algorithmes de pointe tels que **Proximal Policy Optimization (aka PPO). PPO est basé sur Advantage Actor Critic.**

Et vous allez implémenter un agent Advantage Actor Critic (A2C) qui apprend à jouer à Sonic the Hedgehog !

![Image](https://cdn-media-1.freecodecamp.org/images/1*F00fSSixgAp2CbzzI0_v7A.gif)
_Extrait de notre agent jouant à Sonic après 10h d'entraînement sur GPU._

### La quête d'un meilleur modèle d'apprentissage

#### Le problème avec les Policy Gradients

La [méthode Policy Gradient](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f) a un gros problème. Nous sommes dans une situation de Monte Carlo, attendant jusqu'à la fin de l'épisode pour calculer la récompense. Nous pouvons conclure que si nous avons une récompense élevée (**R(t)**), toutes les actions que nous avons prises étaient bonnes, même si certaines étaient vraiment mauvaises.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mKu7H4saf9pP7wfALYh6Kw.png)

Comme nous pouvons le voir dans cet exemple, même si A3 était une mauvaise action (a conduit à des récompenses négatives), **toutes les actions seront moyennées comme bonnes car la récompense totale était importante.**

Par conséquent, pour avoir une politique optimale, nous avons besoin de beaucoup d'échantillons. Cela produit un apprentissage lent, car il faut beaucoup de temps pour converger.

**Et si, au lieu de cela, nous pouvons faire une mise à jour à chaque étape ?**

### Introduction à Actor Critic

Le modèle Actor Critic est une meilleure fonction de score. Au lieu d'attendre jusqu'à la fin de l'épisode comme nous le faisons dans Monte Carlo REINFORCE, **nous faisons une mise à jour à chaque étape (TD Learning).**

![Image](https://cdn-media-1.freecodecamp.org/images/1*4TRtwlftFmWGNzZde45kaA.png)

Parce que nous faisons une mise à jour à chaque étape, nous ne pouvons pas utiliser les récompenses totales R(t). Au lieu de cela, nous devons entraîner un modèle Critic **qui approxime la fonction de valeur** (rappelons que la fonction de valeur calcule la récompense future maximale attendue étant donné un état et une action). Cette fonction de valeur remplace la fonction de récompense dans le gradient de politique qui calcule les récompenses uniquement à la fin de l'épisode.

#### Comment fonctionne Actor Critic

Imaginez que vous jouez à un jeu vidéo avec un ami qui vous donne des commentaires. Vous êtes l'Actor et votre ami est le Critic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e1N-YzQmJt-5KwUkdUvAHg.png)

Au début, vous ne savez pas comment jouer, alors vous essayez des actions au hasard. Le Critic observe votre action et fournit des commentaires.

Apprenant de ces commentaires, **vous mettrez à jour votre politique et serez meilleur à jouer à ce jeu.**

D'autre part, votre ami (Critic) mettra également à jour sa propre façon de fournir des commentaires pour qu'ils soient meilleurs la prochaine fois.

Comme nous pouvons le voir, l'idée de Actor Critic est d'avoir deux réseaux de neurones. Nous estimons les deux :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xoZipWE6lQgWyRh1.)
_**ACTOR** : Une fonction de politique, contrôle comment notre agent agit._

![Image](https://cdn-media-1.freecodecamp.org/images/0*vQZrik2laT8hdRMb.)
_**CRITIC** : Une fonction de valeur, mesure à quel point ces actions sont bonnes._

Les deux fonctionnent en parallèle.

Parce que nous avons deux modèles (Actor et Critic) qui doivent être entraînés, cela signifie que nous avons deux ensembles de poids (θ pour notre action et w pour notre Critic) **qui doivent être optimisés séparément :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*KlX2-kNXRYLAYpdnI8VPiA.png)

#### Le processus Actor Critic

![Image](https://cdn-media-1.freecodecamp.org/images/1*zSsxcz9LjkCwFGcLgJZzdw.png)

À chaque étape t, nous prenons l'état actuel (St) de l'environnement et le passons en entrée à travers notre Actor et notre Critic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZwthrqP0X12yiYDraWoQMg.png)

Notre Politique prend l'état, produit une action (At), et reçoit un nouvel état (St+1) et une récompense (Rt+1).

Grâce à cela :

* le Critic calcule la valeur de prendre cette action dans cet état
* l'Actor met à jour ses paramètres de politique (poids) en utilisant cette valeur q

![Image](https://cdn-media-1.freecodecamp.org/images/1*ohA7iaViVAElqnSJvbYWpA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dGG7HIvsf_EKro2AOT6sKQ.png)

Grâce à ses paramètres mis à jour, l'Actor produit l'action suivante à prendre à At+1 **étant donné** le nouvel état St+1. Le Critic met ensuite à jour ses paramètres de valeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yd2F4KHmgn0lDA8nI9aSQw.png)

### A2C et A3C

#### Introduction de la fonction Advantage pour stabiliser l'apprentissage

Comme nous l'avons vu dans l'article sur [les améliorations du Deep Q Learning](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682), les méthodes basées sur la valeur ont **une grande variabilité.**

Pour réduire ce problème, nous avons parlé d'utiliser la fonction d'avantage au lieu de la fonction de valeur.

La fonction d'avantage est définie comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SvSFYWx5-u5zf38baqBgyQ.png)

Cette fonction nous dira **l'amélioration par rapport à la moyenne de l'action prise dans cet état.** En d'autres termes, cette fonction calcule la récompense supplémentaire que j'obtiens si je prends cette action. La récompense supplémentaire est celle au-delà de la valeur attendue de cet état.

Si A(s,a) > 0 : notre gradient est poussé dans cette direction.

Si A(s,a) < 0 (notre action fait pire que la valeur moyenne de cet état), notre gradient est poussé dans la direction opposée.

Le problème de l'implémentation de cette fonction d'avantage est qu'elle nécessite deux fonctions de valeur — Q(s,a) et V(s). Heureusement, **nous pouvons utiliser l'erreur TD comme un bon estimateur de la fonction d'avantage.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*fmWayfCY4QVIounYXWi2rg.png)

#### Deux stratégies différentes : Asynchrone ou Synchrone

Nous avons deux stratégies différentes pour implémenter un agent Actor Critic :

* A2C (aka Advantage Actor Critic)
* A3C (aka Asynchronous Advantage Actor Critic)

**À cause de cela**, nous travaillerons avec A2C et non A3C. Si vous voulez voir une implémentation complète de A3C, consultez l'excellent article d'[Arthur Juliani](https://www.freecodecamp.org/news/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d/undefined) sur [A3C](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2) et son [implémentation de Doom](https://github.com/awjuliani/DeepRL-Agents/blob/master/A3C-Doom.ipynb).

Dans A3C, nous n'utilisons pas la mémoire d'expérience car cela nécessite beaucoup de mémoire. Au lieu de cela, nous exécutons de manière asynchrone **différents agents en parallèle sur plusieurs instances de l'environnement.** Chaque travailleur (copie du réseau) mettra à jour le réseau global de manière asynchrone.

D'autre part, la seule différence dans A2C est que nous mettons à jour le réseau global de manière synchrone. Nous attendons que tous les travailleurs aient terminé leur entraînement et calculé leurs gradients pour les moyenner, afin de mettre à jour notre réseau global.

#### Choisir A2C ou A3C ?

Le problème de A3C est expliqué dans [cet excellent article](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html#a2c). À cause de la nature asynchrone de A3C, certains travailleurs (copies de l'Agent) joueront avec des versions plus anciennes des paramètres. Ainsi, la mise à jour d'agrégation ne sera pas optimale.

C'est pourquoi A2C attend que chaque acteur termine son segment d'expérience avant de mettre à jour les paramètres globaux. Ensuite, nous redémarrons un nouveau segment d'expérience avec tous les acteurs parallèles ayant les mêmes nouveaux paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0gZsoyvY01liRdZZXilZpA.png)
_Ce schéma est inspiré de [cet article](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html#a2c)._

Par conséquent, l'entraînement sera plus cohésif et plus rapide.

### Implémentation d'un agent A2C qui joue à Sonic the Hedgehog

#### A2C en pratique

En pratique, comme expliqué dans [ce post Reddit](https://www.reddit.com/r/reinforcementlearning/comments/7eljkx/understanding_a2c_and_a3c_multiple_actors/), la nature synchrone de A2C signifie **que nous n'avons pas besoin de différentes versions (différents travailleurs) de A2C.**

Chaque travailleur dans A2C aura le même ensemble de poids puisque, contrairement à A3C, A2C met à jour tous ses travailleurs en même temps.

En fait, nous créons **plusieurs versions d'environnements** (disons huit) et les exécutons en parallèle.

Le processus sera le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bNw9TH5700_x3X64YXHPdQ.png)

* Crée un vecteur de n environnements en utilisant la bibliothèque multiprocessing
* Crée un objet runner qui gère les différents environnements, exécutés en parallèle.
* A deux versions du réseau :

1. step_model : qui génère des expériences à partir des environnements
2. train_model : qui entraîne les expériences.

Lorsque le runner fait un pas (modèle à pas unique), cela effectue un pas pour chacun des n environnements. Cela produit un lot d'expérience.

Ensuite, nous calculons le gradient en une seule fois en utilisant train_model et notre lot d'expérience.

Enfin, nous mettons à jour le step model avec les nouveaux poids.

Rappelons que calculer le gradient en une seule fois est la même chose que collecter des données, calculer le gradient pour chaque travailleur, puis faire la moyenne. Pourquoi ? **Parce que la somme des dérivées (somme des gradients) est la même chose que prendre les dérivées de la somme.** Mais la deuxième méthode est plus élégante et une meilleure façon d'utiliser le GPU.

#### A2C avec Sonic the Hedgehog

Maintenant que nous comprenons comment A2C fonctionne en général, nous pouvons implémenter notre agent A2C jouant à Sonic ! Cette vidéo montre la différence de comportement de notre agent entre 10 minutes d'entraînement (à gauche) et 10 heures d'entraînement (à droite).

L'implémentation est dans le dépôt GitHub [ici](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/tree/master/A2C%20with%20Sonic%20the%20Hedgehog), et le notebook explique l'implémentation. Je vous donne le modèle sauvegardé entraîné avec environ 10h+ sur GPU.

Cette implémentation est beaucoup plus complexe que les implémentations précédentes. Nous commençons à implémenter des algorithmes de pointe, donc nous devons être **de plus en plus efficaces avec notre code.** C'est pourquoi, dans cette implémentation, nous allons séparer le code en différents objets et fichiers.

C'est tout ! Vous venez de créer un agent qui apprend à jouer à Sonic the Hedgehog. C'est génial ! Nous pouvons voir qu'avec 10 heures d'entraînement, notre agent ne comprend pas les loopings, par exemple, donc nous devrons utiliser une architecture plus stable : PPO.

**Prenez le temps de considérer tous les accomplissements que vous avez réalisés depuis le [premier chapitre de ce cours](https://medium.com/free-code-camp/an-introduction-to-reinforcement-learning-4339519de419) :** nous sommes passés de simples jeux textuels (OpenAI taxi-v2) à des jeux complexes comme Doom et Sonic the Hedgehog en utilisant des architectures de plus en plus puissantes. Et c'est fantastique !

La prochaine fois, nous apprendrons sur les Proximal Policy Gradients, l'architecture qui a gagné le [OpenAI Retro Contest](https://contest.openai.com/2018-1/). Nous entraînerons notre agent à jouer à Sonic the Hedgehog 2 et 3 et cette fois, il terminera des niveaux entiers !

N'oubliez pas d'implémenter chaque partie du code par vous-même. Il est vraiment important d'essayer de modifier le code que je vous ai donné. Essayez d'ajouter des époques, changez l'architecture, changez le taux d'apprentissage, et ainsi de suite. Expérimenter est la meilleure façon d'apprendre, alors amusez-vous !

Si vous avez aimé mon article, **veuillez cliquer sur le ? ci-dessous autant de fois que vous avez aimé l'article** pour que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Cet article fait partie de mon cours de Deep Reinforcement Learning avec TensorFlow ?. Consultez le programme [ici](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello [at] simoninithomas [dot] com, ou me tweeter [@ThomasSimonini](https://twitter.com/ThomasSimonini).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

#### Cours de Deep Reinforcement Learning :

> Nous réalisons une **version vidéo du cours de Deep Reinforcement Learning avec Tensorflow** ? où nous nous concentrons sur la partie implémentation avec tensorflow [ici](https://youtu.be/q2ZOEFAaaI0).

_Partie 1 : [Une introduction à l'apprentissage par renforcement](https://medium.com/p/4339519de419/edit)_

_Partie 2 : [Plonger plus profondément dans l'apprentissage par renforcement avec Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)_

_Partie 3 : [Une introduction au Deep Q-Learning : jouons à Doom](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)_

Partie 3+ : [Améliorations du Deep Q Learning : Dueling Double DQN, Prioritized Experience Replay, et Q-targets fixes](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)

Partie 4 : [Une introduction aux Policy Gradients avec Doom et Cartpole](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f)

Partie 6 : [Proximal Policy Optimization (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e)

Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)