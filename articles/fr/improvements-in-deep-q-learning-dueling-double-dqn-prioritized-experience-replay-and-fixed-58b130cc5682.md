---
title: 'Améliorations dans l''apprentissage par renforcement profond : Dueling Double
  DQN, Prioritized Experience Replay et cibles Q fixes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T00:10:13.000Z'
originalURL: https://freecodecamp.org/news/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682
coverImage: https://cdn-media-1.freecodecamp.org/images/1*idlcWBCQGKJ2rMjKPwAKiQ.png
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
seo_title: 'Améliorations dans l''apprentissage par renforcement profond : Dueling
  Double DQN, Prioritized Experience Replay et cibles Q fixes'
seo_desc: 'By Thomas Simonini


  This article is part of Deep Reinforcement Learning Course with Tensorflow ?️. Check
  the syllabus here.


  In our last article about Deep Q Learning with Tensorflow, we implemented an agent
  that learns to play a simple version of Do...'
---

Par Thomas Simonini

> Cet article fait partie du cours d'apprentissage par renforcement profond avec Tensorflow 🎯. Consultez le programme [ici](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/).

Dans notre dernier article sur [l'apprentissage par renforcement profond avec Tensorflow](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8), nous avons implémenté un agent qui apprend à jouer à une version simple de Doom. Dans la version vidéo, [nous avons entraîné un agent DQN qui joue à Space Invaders](https://www.youtube.com/watch?v=gCJyVX98KJ4).

Cependant, pendant l'entraînement, nous avons vu qu'il y avait beaucoup de variabilité.

L'apprentissage par renforcement profond (Deep Q-Learning) a été introduit en 2014. Depuis, de nombreuses améliorations ont été apportées. Aujourd'hui, nous allons voir quatre stratégies qui améliorent — de manière dramatique — l'entraînement et les résultats de nos agents DQN :

* Cibles Q fixes
* Double DQN
* Dueling DQN (aka DDQN)
* Prioritized Experience Replay (aka PER)

Nous allons implémenter un agent qui apprend à jouer à Doom Deadly Corridor. Notre IA doit naviguer vers l'objectif fondamental (le gilet), et s'assurer de survivre en même temps en tuant des ennemis.

### Cibles Q fixes

#### Théorie

Nous avons vu dans l'article sur l'apprentissage par renforcement profond que, lorsque nous voulons calculer l'erreur TD (aka la perte), nous calculons la différence entre la cible TD (Q_target) et la valeur Q actuelle (estimation de Q).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zplt-1wTWu_7BGmZCBFjbQ.png)

Mais **nous n'avons aucune idée de la vraie cible TD.** Nous devons l'estimer. En utilisant l'équation de Bellman, nous avons vu que la cible TD est simplement la récompense de prendre cette action dans cet état plus la valeur Q la plus élevée actualisée pour l'état suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KsQ46R8zyTQlKGv91xi6ww.png)

Cependant, le problème est que nous utilisons les mêmes paramètres (poids) pour estimer la cible **et** la valeur Q. Par conséquent, il y a une grande corrélation entre la cible TD et les paramètres (w) que nous changeons.

Cela signifie qu'à chaque étape de l'entraînement, **nos valeurs Q changent mais la valeur cible change aussi.** Donc, nous nous rapprochons de notre cible mais la cible bouge aussi. C'est comme courir après une cible mouvante ! Cela conduit à de grandes oscillations pendant l'entraînement.

C'est comme si vous étiez un cowboy (l'estimation Q) et que vous vouliez attraper la vache (la cible Q), vous devez vous rapprocher (réduire l'erreur).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BCsZHA3cO3zsQySkRuWPEw.png)

À chaque étape, vous essayez de vous approcher de la vache, qui bouge aussi à chaque étape (parce que vous utilisez les mêmes paramètres).

![Image](https://cdn-media-1.freecodecamp.org/images/1*aKuCo_MvnoCa148m3U9YXg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*T5MwyKNbDmG9Vb_fQg1t-w.png)

Cela conduit à un chemin de poursuite très étrange (de grandes oscillations pendant l'entraînement).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kt6H_kh_rfSu7EkN9bU0oA.png)

Au lieu de cela, nous pouvons utiliser l'idée des cibles Q fixes introduite par DeepMind :

* Utiliser un réseau séparé avec des paramètres fixes (appelons-le w-) pour estimer la cible TD.
* À chaque étape Tau, nous copions les paramètres de notre réseau DQN pour mettre à jour le réseau cible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*D9i0I2EO7LKL2aAb2HLfTg.png)

Grâce à cette procédure, nous aurons un apprentissage plus stable car la fonction cible reste fixe pendant un certain temps.

#### Implémentation

L'implémentation des cibles Q fixes est assez simple :

* D'abord, nous créons deux réseaux (`DQNetwork`, `TargetNetwork`)

* Ensuite, nous créons une fonction qui prendra les paramètres de notre `DQNetwork` et les copiera dans notre `TargetNetwork`

* Enfin, pendant l'entraînement, nous calculons la cible TD en utilisant notre réseau cible. Nous mettons à jour le réseau cible avec le `DQNetwork` toutes les `tau` étapes (`tau` est un hyper-paramètre que nous définissons).

### Double DQN

#### Théorie

Les Double DQN, ou Double Learning, ont été introduits [par Hado van Hasselt](https://papers.nips.cc/paper/3964-double-q-learning). Cette méthode **gère le problème de la surestimation des valeurs Q.**

Pour comprendre ce problème, rappelez-vous comment nous calculons la cible TD :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KsQ46R8zyTQlKGv91xi6ww.png)

En calculant la cible TD, nous sommes confrontés à un problème simple : comment être sûr que **la meilleure action pour l'état suivant est l'action avec la valeur Q la plus élevée ?**

Nous savons que la précision des valeurs Q dépend des actions que nous avons essayées **et** des états voisins que nous avons explorés.

Par conséquent, au début de l'entraînement, nous n'avons pas assez d'informations sur la meilleure action à prendre. Par conséquent, prendre la valeur Q maximale (qui est bruyante) comme la meilleure action à prendre peut conduire à des faux positifs. Si des actions non optimales se voient régulièrement **attribuer une valeur Q plus élevée que l'action optimale, l'apprentissage sera compliqué.**

La solution est : lorsque nous calculons la cible Q, nous utilisons deux réseaux pour découpler la sélection de l'action de la génération de la valeur Q cible. Nous :

* utilisons notre réseau DQN pour sélectionner la meilleure action à prendre pour l'état suivant (l'action avec la valeur Q la plus élevée).
* utilisons notre réseau cible pour calculer la valeur Q cible de prendre cette action à l'état suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g5l4q162gDRZAAsFWtX7Nw.png)

Par conséquent, le Double DQN nous aide à réduire la surestimation des valeurs Q et, par conséquent, nous aide à nous entraîner plus rapidement et à avoir un apprentissage plus stable.

#### Implémentation

![Image](https://cdn-media-1.freecodecamp.org/images/1*oyGR6gJ4WyqeKOfq0Cd8iQ.png)

### Dueling DQN (aka DDQN)

#### Théorie

Rappelez-vous que les valeurs Q correspondent **à la qualité d'être dans cet état et de prendre une action dans cet état Q(s,a).**

Nous pouvons donc décomposer Q(s,a) comme la somme de :

* **V(s)** : la valeur d'être dans cet état
* **A(s,a)** : l'avantage de prendre cette action dans cet état (à quel point il est meilleur de prendre cette action par rapport à toutes les autres actions possibles dans cet état).

![Image](https://cdn-media-1.freecodecamp.org/images/1*yPtkPCxjXP2TbK8VlUuXtA.png)

Avec le DDQN, nous voulons séparer l'estimateur de ces deux éléments, en utilisant deux nouveaux flux :

* un qui estime la **valeur de l'état V(s)**
* un qui estime l'**avantage pour chaque action A(s,a)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*FkHqwA2eSGixdS-3dvVoMA.png)

Et ensuite nous combinons ces deux flux **à travers une couche d'agrégation spéciale pour obtenir une estimation de Q(s,a).**

Attendez ? **Mais pourquoi devons-nous calculer ces deux éléments séparément si ensuite nous les combinons ?**

En découplant l'estimation, intuitivement notre DDQN peut apprendre quels états sont (ou ne sont pas) précieux **sans** avoir à apprendre l'effet de chaque action à chaque état (puisqu'il calcule aussi V(s)).

Avec notre DQN normal, nous devons calculer la valeur de chaque action dans cet état. **Mais quel est l'intérêt si la valeur de l'état est mauvaise ?** Quel est l'intérêt de calculer toutes les actions dans un état lorsque toutes ces actions mènent à la mort ?

Par conséquent, en découplant, nous sommes capables de calculer V(s). Cela est particulièrement **utile pour les états où leurs actions n'affectent pas l'environnement de manière pertinente.** Dans ce cas, il est inutile de calculer la valeur de chaque action. Par exemple, se déplacer à droite ou à gauche n'a d'importance que s'il y a un risque de collision. Et, dans la plupart des états, le choix de l'action n'a aucun effet sur ce qui se passe.

Cela sera plus clair si nous prenons l'exemple dans l'article [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/pdf/1511.06581.pdf).

![Image](https://cdn-media-1.freecodecamp.org/images/0*qor_kPiSwiWt8uQF)

Nous voyons que le flux du réseau de valeur prête attention (le flou orange) à la route, et en particulier à l'horizon où les voitures apparaissent. Il prête également attention au score.

D'autre part, le flux d'avantage dans la première image à droite ne prête pas beaucoup d'attention à la route, car il n'y a pas de voitures devant (donc le choix de l'action est pratiquement sans importance). Mais, dans la deuxième image, il prête attention, car il y a une voiture immédiatement devant lui, et faire un choix d'action est crucial et très pertinent.

Concernant la couche d'agrégation, nous voulons générer les valeurs Q pour chaque action dans cet état. Nous pourrions être tentés de combiner les flux comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*ue6KTm1dRQ0A6sM4)

Mais si nous faisons cela, nous tomberons dans le **problème d'identifiabilité**, c'est-à-dire — étant donné Q(s,a), nous sommes incapables de trouver A(s,a) et V(s).

Et ne pas pouvoir trouver V(s) et A(s,a) étant donné Q(s,a) sera un problème pour notre rétropropagation. Pour éviter ce problème, nous pouvons forcer notre estimateur de fonction d'avantage à avoir un avantage de 0 à l'action choisie.

Pour ce faire, nous soustrayons l'avantage moyen de toutes les actions possibles de l'état.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kt9_Z41qxgiI0CDl)

Par conséquent, cette architecture nous aide à accélérer l'entraînement. Nous pouvons calculer la valeur d'un état sans calculer Q(s,a) pour chaque action dans cet état. Et cela peut nous aider à trouver des valeurs Q beaucoup plus fiables pour chaque action en découplant l'estimation entre deux flux.

#### Implémentation

La seule chose à faire est de modifier l'architecture DQN en ajoutant ces nouveaux flux :

### Prioritized Experience Replay

#### Théorie

Le Prioritized Experience Replay (PER) a été introduit en 2015 par [Tom Schaul](https://arxiv.org/search?searchtype=author&query=Schaul%2C+T). L'idée est que certaines expériences peuvent être plus importantes que d'autres pour notre entraînement, mais peuvent se produire moins fréquemment.

Parce que nous échantillonnons le lot uniformément (en sélectionnant les expériences aléatoirement), ces expériences riches qui se produisent rarement ont pratiquement aucune chance d'être sélectionnées.

C'est pourquoi, avec le PER, nous essayons de changer la distribution d'échantillonnage en utilisant un critère pour définir la priorité de chaque tuple d'expérience.

Nous voulons prendre en priorité **les expériences où il y a une grande différence entre notre prédiction et la cible TD, car cela signifie que nous avons beaucoup à apprendre à ce sujet.**

Nous utilisons la valeur absolue de l'amplitude de notre erreur TD :

![Image](https://cdn-media-1.freecodecamp.org/images/0*0qPwzal3qBIP0eFb)

Et nous **mettons cette priorité dans l'expérience de chaque tampon de relecture.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*iKTTN92E7wwnlh-E)

Mais nous ne pouvons pas simplement faire une priorisation gloutonne, car cela conduirait toujours à entraîner les mêmes expériences (qui ont une grande priorité), et donc à un sur-apprentissage.

Nous introduisons donc une priorisation stochastique, **qui génère la probabilité d'être choisi pour une relecture.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*iCkLY7L3R3mWEh_O)

Par conséquent, à chaque étape, nous obtiendrons un lot d'échantillons avec cette distribution de probabilité et nous entraînerons notre réseau sur celui-ci.

Mais, nous avons toujours un problème ici. Rappelez-vous qu'avec le Experience Replay normal, nous utilisons une règle de mise à jour stochastique. Par conséquent, **la manière dont nous échantillonnons les expériences doit correspondre à la distribution sous-jacente dont elles proviennent.**

Lorsque nous avons une expérience normale, nous sélectionnons nos expériences dans une distribution normale — simplement, nous sélectionnons nos expériences aléatoirement. Il n'y a pas de biais, car chaque expérience a la même chance d'être prise, donc nous pouvons mettre à jour nos poids normalement.

**Mais**, parce que nous utilisons un échantillonnage par priorité, l'échantillonnage purement aléatoire est abandonné. Par conséquent, nous introduisons un biais envers les échantillons à haute priorité (plus de chances d'être sélectionnés).

Et, si nous mettons à jour nos poids normalement, nous prenons un risque de sur-apprentissage. Les échantillons qui ont une haute priorité sont susceptibles d'être utilisés pour l'entraînement de nombreuses fois par rapport aux expériences à faible priorité (= biais). Par conséquent, nous mettrons à jour nos poids avec seulement une petite portion d'expériences que nous considérons comme vraiment intéressantes.

Pour corriger ce biais, nous utilisons des poids d'échantillonnage d'importance (IS) qui ajusteront la mise à jour en réduisant les poids des échantillons souvent vus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Lf3KBrOdyBYcOVqB)

Les poids correspondant aux échantillons à haute priorité ont très peu d'ajustement (parce que le réseau verra ces expériences de nombreuses fois), tandis que ceux correspondant aux échantillons à faible priorité auront une mise à jour complète.

Le rôle de **b** est de contrôler combien ces poids d'échantillonnage d'importance affectent l'apprentissage. En pratique, le paramètre b est recuit jusqu'à 1 sur la durée de l'entraînement, car ces poids sont plus importants **à la fin de l'apprentissage lorsque nos valeurs Q commencent à converger.** La nature non biaisée des mises à jour est la plus importante près de la convergence, comme expliqué dans cet [article](http://pemami4911.github.io/paper-summaries/deep-rl/2016/01/26/prioritizing-experience-replay.html).

#### Implémentation

Cette fois, l'implémentation sera un peu plus élaborée.

Tout d'abord, nous ne pouvons pas simplement implémenter le PER en triant tous les tampons de relecture d'expérience selon leurs priorités. Cela ne sera pas efficace du tout en raison de **O(nlogn) pour l'insertion et O(n) pour l'échantillonnage.**

Comme expliqué dans [cet article très bon](https://jaromiru.com/2016/11/07/lets-make-a-dqn-double-learning-and-prioritized-experience-replay/), nous devons utiliser une autre structure de données au lieu de trier un tableau — un sumtree **non trié.**

Un sumtree est un arbre binaire, c'est-à-dire un arbre avec un maximum de deux enfants pour chaque nœud. Les feuilles (nœuds les plus profonds) contiennent les valeurs de priorité, et un tableau de données qui pointe vers les feuilles contient les expériences.

La mise à jour de l'arbre et l'échantillonnage seront très efficaces (O(log n)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Go9DNr7YY-wMGdIQ7HQduQ.png)

Ensuite, nous créons un objet mémoire qui contiendra notre sumtree et nos données.

Ensuite, pour échantillonner un minibatch de taille k, la plage [0, priorité_totale] sera divisée en k plages. Une valeur est échantillonnée uniformément à partir de chaque plage.

Enfin, les transitions (expériences) qui correspondent à chacune de ces valeurs échantillonnées sont récupérées à partir du sumtree.

Cela sera beaucoup plus clair lorsque nous plongerons dans les détails complets dans le notebook.

### Agent Deathmatch de Doom

Cet agent est un Dueling Double Deep Q Learning avec PER et cibles Q fixes.

> Nous avons fait un tutoriel vidéo de l'implémentation :

> Le notebook est [ici](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Dueling%20Double%20DQN%20with%20PER%20and%20fixed-q%20targets/Dueling%20Deep%20Q%20Learning%20with%20Doom%20(%2B%20double%20DQNs%20and%20Prioritized%20Experience%20Replay).ipynb)

C'est tout ! Vous venez de créer un agent plus intelligent qui apprend à jouer à Doom. Génial ! Rappelez-vous que si vous voulez avoir un agent avec de très bonnes performances, **vous avez besoin de beaucoup plus d'heures de GPU (environ deux jours d'entraînement) !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*pN5raRODUzEQOLw0egyXYg.gif)

**Cependant, avec seulement 2-3 heures d'entraînement sur CPU** (oui CPU), notre agent a compris qu'il devait tuer les ennemis avant de pouvoir avancer. S'ils avancent sans tuer les ennemis, ils seront tués avant d'obtenir le gilet.

N'oubliez pas d'implémenter chaque partie du code par vous-même. Il est vraiment important d'essayer de modifier le code que je vous ai donné. Essayez d'ajouter des époques, changez l'architecture, ajoutez des valeurs Q fixes, changez le taux d'apprentissage, utilisez un environnement plus difficile... et ainsi de suite. Expérimentez, amusez-vous !

Rappelez-vous que c'était un gros article, alors assurez-vous de vraiment comprendre pourquoi nous utilisons ces nouvelles stratégies, comment elles fonctionnent, et les avantages de les utiliser.

Dans le prochain article, nous apprendrons une méthode hybride géniale entre les algorithmes d'apprentissage par renforcement basés sur la valeur et ceux basés sur les politiques. **C'est une base pour les algorithmes de pointe** : Advantage Actor Critic (A2C). Vous implémenterez un agent qui apprend à jouer à Outrun !

![Image](https://cdn-media-1.freecodecamp.org/images/1*0M5OiOwKemAwkObBy1K6VQ.gif)

Si vous avez aimé mon article, **cliquez sur le ? ci-dessous autant de fois que vous avez aimé l'article** pour que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Si vous avez des pensées, des commentaires, des questions, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou tweetez-moi [@ThomasSimonini](https://twitter.com/ThomasSimonini).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_yN1FzvEFDmlObiYsstIzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mD-f5VN1SWYvhrZAbvSu_w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PqiptT-Cdi8uwosxuFn2DQ.png)

Continuez à apprendre, restez génial !

#### Cours d'apprentissage par renforcement profond avec Tensorflow 🎯

📋 [Programme](https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)

📹 [Version vidéo](https://www.youtube.com/channel/UC8XuSf1eD9AF8x8J19ha5og?view_as=subscriber)

Partie 1 : [Une introduction à l'apprentissage par renforcement](https://medium.com/p/4339519de419/edit)

Partie 2 : [Plonger plus profondément dans l'apprentissage par renforcement avec Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)

Partie 3 : [Une introduction à l'apprentissage par renforcement profond : jouons à Doom](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)

Partie 3+ : [Améliorations dans l'apprentissage par renforcement profond : Dueling Double DQN, Prioritized Experience Replay et cibles Q fixes](https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682)

Partie 4 : [Une introduction aux gradients de politique avec Doom et Cartpole](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f)

Partie 5 : [Une introduction aux méthodes Advantage Actor Critic : jouons à Sonic the Hedgehog !](https://medium.freecodecamp.org/an-intro-to-advantage-actor-critic-methods-lets-play-sonic-the-hedgehog-86d6240171d)

Partie 6 : [Optimisation des politiques proximales (PPO) avec Sonic the Hedgehog 2 et 3](https://towardsdatascience.com/proximal-policy-optimization-ppo-with-sonic-the-hedgehog-2-and-3-c9c21dbed5e)

Partie 7 : [L'apprentissage par curiosité rendu facile Partie I](https://towardsdatascience.com/curiosity-driven-learning-made-easy-part-i-d3e5a2263359)