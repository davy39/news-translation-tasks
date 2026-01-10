---
title: Une brève introduction à l'apprentissage par renforcement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T21:17:00.000Z'
originalURL: https://freecodecamp.org/news/a-brief-introduction-to-reinforcement-learning-7799af5840db
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7i8JA5t1Nx3HlK4E
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
seo_title: Une brève introduction à l'apprentissage par renforcement
seo_desc: 'By ADL

  Reinforcement Learning is an aspect of Machine learning where an agent learns to
  behave in an environment, by performing certain actions and observing the rewards/results
  which it get from those actions.

  With the advancements in Robotics Arm M...'
---

Par ADL

L'apprentissage par renforcement est un aspect de l'apprentissage automatique où un agent apprend à se comporter dans un environnement, en effectuant certaines actions et en observant les récompenses/résultats qu'il obtient de ces actions.

Avec les avancées en manipulation de bras robotiques, Google Deep Mind battant un joueur professionnel d'Alpha Go, et récemment l'équipe OpenAI battant un joueur professionnel de DOTA, le domaine de l'apprentissage par renforcement a vraiment explosé ces dernières années.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EM8x5jAL-SeUUG7b4anCQg.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rvGVriKT_aLeLKvAP16S0A.gif)
_Exemples_

Dans cet article, nous discuterons :

* Ce qu'est l'apprentissage par renforcement et ses détails comme les récompenses, les tâches, etc.
* 3 catégorisations de l'apprentissage par renforcement

#### Qu'est-ce que l'apprentissage par renforcement ?

Commençons l'explication avec un exemple — disons qu'il y a un petit bébé qui commence à apprendre à marcher.

Divisons cet exemple en deux parties :

#### 1. **Le bébé commence à marcher et atteint avec succès le canapé**

Puisque le canapé est le but final, le bébé et les parents sont heureux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sDMJA6qzlo59o7iivh6U6Q.jpeg)

Donc, le bébé est heureux et reçoit des félicitations de ses parents. C'est positif — le bébé se sent bien _(Récompense positive +n)._

#### 2. **Le bébé commence à marcher et tombe à cause d'un obstacle et se blesse.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*i_999FG_Y-DnlCtpEKb5Vw.jpeg)

Aïe ! Le bébé se blesse et a mal. C'est négatif — le bébé pleure _(Récompense négative -n)._

C'est ainsi que nous, humains, apprenons — par essai et erreur. L'apprentissage par renforcement est conceptuellement le même, mais c'est une approche computationnelle pour apprendre par les actions.

### Apprentissage par renforcement

Supposons que notre agent d'apprentissage par renforcement apprend à jouer à Mario comme exemple. Le processus d'apprentissage par renforcement peut être modélisé comme une boucle itérative qui fonctionne comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vz3AN1mBUR2cr_jEG8s7Mg.png)

* L'agent RL reçoit l'**état S₀** de l'**environnement** c'est-à-dire Mario
* Sur la base de cet **état S₀**, l'agent RL prend une **action A₀**, disons — notre agent RL se déplace vers la droite. Initialement, cela est aléatoire.
* Maintenant, l'environnement est dans un nouvel état **S₁** (nouvelle frame de Mario ou du moteur de jeu)
* L'environnement donne une certaine **récompense R₁** à l'agent RL. Il donne probablement un +1 parce que l'agent n'est pas encore mort.

Cette boucle RL continue jusqu'à ce que nous soyons morts ou que nous atteignions notre destination, et elle produit en continu une séquence d'**état, action et récompense.**

Le but de base de notre agent RL est de maximiser la récompense.

### Maximisation de la récompense

L'agent RL fonctionne essentiellement sur une hypothèse de maximisation de la récompense. **C'est pourquoi l'apprentissage par renforcement doit avoir la meilleure action possible afin de maximiser la récompense.**

Les récompenses cumulatives à chaque étape de temps avec l'action respective sont écrites comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*up3hsG1ToqndcnmdA8tbRw.png)

Cependant, les choses ne fonctionnent pas de cette manière lorsque l'on additionne toutes les récompenses.

Comprenons cela en détail :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l8wl4hZvZAiLU56hT9vLlg.png)

Disons que notre agent RL (souris robotique) est dans un labyrinthe qui contient **du fromage, des chocs électriques et des chats**. Le but est de manger la quantité maximale de fromage avant d'être mangé par le chat ou de recevoir un choc électrique.

Il semble évident de manger le fromage près de nous plutôt que le fromage proche du chat ou du choc électrique, car plus nous sommes proches du choc électrique ou du chat, plus le danger de mourir augmente. Par conséquent, la récompense près du chat ou du choc électrique, même si elle est plus grande (plus de fromage), sera réduite. Cela est fait en raison du facteur d'incertitude.

Cela a du sens, n'est-ce pas ?

#### **L'actualisation des récompenses fonctionne comme suit :**

Nous définissons un taux d'actualisation appelé **gamma**. Il doit être compris entre 0 et 1. Plus le gamma est grand, plus l'actualisation est faible et vice versa.

Donc, nos récompenses cumulatives attendues (actualisées) sont :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ef-5D-aBUShEnvMjiCujNw.png)
_Récompenses cumulatives attendues_

### Tâches et leurs types dans l'apprentissage par renforcement

Une **tâche** est une instance unique d'un problème d'apprentissage par renforcement. Nous avons essentiellement deux types de tâches : **continues et épisodiques.**

#### Tâches continues

**Ce sont les types de tâches qui continuent indéfiniment.** Par exemple, un agent RL qui fait du trading Forex/Actions automatisé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Rpz3cfDnays7p4-e)
_Photo par [Unsplash](https://unsplash.com/@chrisliverani?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Chris Liverani</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Dans ce cas, l'agent doit apprendre à choisir les meilleures actions et interagir simultanément avec l'environnement. Il n'y a pas de point de départ et d'état final.

**L'agent RL doit continuer à fonctionner jusqu'à ce que nous décidions de l'arrêter manuellement.**

#### Tâche épisodique

Dans ce cas, nous avons un point de départ et un point final **appelé l'état terminal. Cela crée un épisode** : une liste d'États (S), d'Actions (A), de Récompenses (R).

Par exemple, jouer à un jeu de _counter strike_, où nous tirons sur nos adversaires ou nous sommes tués par eux. Nous les tuons tous et complétons l'épisode ou nous sommes tués. Donc, il n'y a que deux cas pour compléter les épisodes.

### Compromis entre exploration et exploitation

Il y a un concept important de compromis entre exploration et exploitation dans l'apprentissage par renforcement. L'exploration consiste à trouver plus d'informations sur un environnement, tandis que l'exploitation consiste à exploiter des informations déjà connues pour maximiser les récompenses.

**Exemple de la vie réelle :** Disons que vous allez au même restaurant tous les jours. Vous exploitez essentiellement. Mais d'un autre côté, si vous cherchez un nouveau restaurant chaque fois avant d'aller dans l'un d'eux, alors c'est de l'**exploration**. L'exploration est très importante pour la recherche de futures récompenses qui pourraient être plus élevées que les récompenses proches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R9hA8rKx52oByN5Xa7Aqng.png)

Dans le jeu ci-dessus, notre souris robotique peut avoir une bonne quantité de petit fromage (+0,5 chacun). Mais en haut du labyrinthe, il y a une grande somme de fromage (+100). Donc, si nous nous concentrons uniquement sur la récompense la plus proche, notre souris robotique n'atteindra jamais la grande somme de fromage — elle exploitera simplement.

Mais si la souris robotique fait un peu d'exploration, elle peut trouver la grande récompense, c'est-à-dire le gros fromage.

C'est le concept de base du **compromis entre exploration et exploitation.**

### Approches de l'apprentissage par renforcement

Comprenons maintenant les approches pour résoudre les problèmes d'apprentissage par renforcement. Il y a essentiellement 3 approches, mais nous ne prendrons que 2 approches majeures dans cet article :

#### 1. Approche basée sur les politiques

Dans l'apprentissage par renforcement basé sur les politiques, nous avons une politique que nous devons optimiser. La politique définit essentiellement comment l'agent se comporte :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0eMOC89KDSeJAPxEpOZi5Q.png)

Nous apprenons une fonction de politique qui nous aide à mapper chaque état à la meilleure action.

En approfondissant les politiques, nous divisons davantage les politiques en deux types :

* **Déterministe** : une politique à un état donné (s) retournera toujours la même action (a). **Cela signifie qu'elle est pré-mappée comme S=(s) ➔ A=(a).**
* **Stochastique** : Elle donne une distribution de probabilité sur différentes actions. **c'est-à-dire Politique Stochastique ➔ p( A = a | S = s )**

#### 2. Basée sur la valeur

Dans l'apprentissage par renforcement basé sur la valeur, le but de l'agent est d'optimiser la fonction de valeur _V(s)_ qui est définie comme une fonction qui nous indique la récompense future maximale attendue que l'agent doit obtenir à chaque état.

La valeur de chaque état est le montant total de la récompense qu'un agent RL peut s'attendre à collecter à l'avenir, à partir d'un état particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kvtRAhBZO-h77Iw1.)

L'agent utilisera la fonction de valeur ci-dessus pour sélectionner quel état choisir à chaque étape. L'agent choisira toujours l'état avec la plus grande valeur.

Dans l'exemple ci-dessous, nous voyons qu'à chaque étape, nous prendrons la plus grande valeur pour atteindre notre objectif : 1 ➔ 3 ➔ 4 ➔ 6 et ainsi de suite...

![Image](https://cdn-media-1.freecodecamp.org/images/1*96F7YC253a5-mXNPVUTCSg.png)
_Labyrinthe_

### Le jeu de Pong — Une étude de cas intuitive

![Image](https://cdn-media-1.freecodecamp.org/images/1*6D27X-9bipEPrgHrrjwIRA.gif)

Prenons un exemple de la vie réelle de jouer à Pong. Cette étude de cas vous introduira simplement à l'intuition de **comment fonctionne l'apprentissage par renforcement**. Nous n'entrerons pas dans les détails dans cet exemple, mais dans le prochain article, nous approfondirons certainement.

Supposons que nous apprenons à notre agent RL à jouer au jeu de Pong.

Essentiellement, nous alimentons les frames du jeu (nouveaux états) dans l'algorithme RL et laissons l'algorithme décider où aller en haut ou en bas. Ce réseau est dit être un **réseau de politiques**, que nous discuterons dans notre prochain article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nGQ4cQneWpgbUpl7aREGwg.jpeg)

La méthode utilisée pour entraîner cet algorithme est appelée le **gradient de politique**. Nous alimentons des frames aléatoires du moteur de jeu, et l'algorithme produit une sortie aléatoire qui donne une récompense et cela est réinjecté dans l'algorithme/réseau. C'est un **processus itératif.**

Nous discuterons des **gradients de politique** dans le prochain article avec plus de détails.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-SwnWvR-VhZRhX-a9ruF6Q.png)
_Environnement = Moteur de jeu et Agent = Agent RL_

Dans le contexte du jeu, le tableau de score agit comme une récompense ou un retour pour l'agent. Chaque fois que l'agent marque +1, il comprend que l'action prise était suffisamment bonne à cet état.

Maintenant, nous allons entraîner l'agent à jouer au jeu de Pong. Pour commencer, nous allons alimenter un ensemble de frames de jeu **(états)** dans le réseau/algorithme et laisser l'algorithme décider de l'action. Les actions initiales de l'agent seront évidemment mauvaises, mais notre agent peut parfois avoir assez de chance pour marquer un point et cela pourrait être un événement aléatoire. Mais grâce à cet événement aléatoire chanceux, il reçoit une récompense et cela aide l'agent à comprendre que la série d'actions était suffisamment bonne pour obtenir une récompense.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cdq5CaGCJCU6ePiXS9GbYg.png)
_Résultats pendant l'entraînement_

Donc, à l'avenir, l'agent est susceptible de prendre les actions qui lui rapporteront une récompense plutôt qu'une action qui ne le fera pas. Intuitivement, l'agent RL apprend à jouer au jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*roRyfK2mmV1E_MsN0cRzcg.gif)
_Source : OLEGIF.com_

#### Limites

Pendant l'entraînement de l'agent, lorsqu'un agent perd un épisode, l'algorithme rejettera ou réduira la probabilité de prendre toutes les séries d'actions qui existaient dans cet épisode.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H6wuWYx1wlGRTNfiFGWvhA.png)
_La démarcation rouge montre toutes les actions prises dans un épisode perdant_

Mais si l'agent se comportait **bien** depuis le début de l'épisode, mais a perdu le jeu à cause des deux dernières actions, il n'a pas de sens de rejeter toutes les actions. Il serait plus judicieux de simplement supprimer les deux dernières actions qui ont entraîné la perte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZSPXbb8q_2zZiVEQdbDX9A.png)
_La démarcation verte montre toutes les actions qui étaient correctes et la démarcation rouge montre les actions qui devraient être supprimées._

Cela s'appelle le **problème d'attribution de crédit**. Ce problème survient en raison d'un **paramétrage de récompense clairsemé**. C'est-à-dire, au lieu de recevoir une récompense à chaque étape, nous recevons la récompense à la fin de l'épisode. Donc, c'est à l'agent d'apprendre quelles actions étaient correctes et quelle action réelle a conduit à perdre le jeu.

Ainsi, en raison de ce paramétrage de récompense clairsemé en RL, l'algorithme est très inefficace en termes d'échantillons. Cela signifie qu'un grand nombre d'exemples d'entraînement doivent être alimentés afin d'entraîner l'agent. Mais le fait est que les paramétrages de récompense clairsemés échouent dans de nombreuses circonstances en raison de la complexité de l'environnement.

Il existe donc quelque chose appelé **façonnage des récompenses** qui est utilisé pour résoudre cela. Mais encore une fois, le façonnage des récompenses souffre également de certaines limitations, car nous devons concevoir une fonction de récompense personnalisée pour chaque jeu.

#### Note de clôture

Aujourd'hui, l'apprentissage par renforcement est un domaine d'étude passionnant. Des développements majeurs ont été réalisés dans ce domaine, dont l'apprentissage par renforcement profond est l'un d'eux.

Nous aborderons l'apprentissage par renforcement profond dans nos prochains articles. Cet article couvre de nombreux concepts. Prenez votre temps pour comprendre les concepts de base de l'apprentissage par renforcement.

Mais je tiens à mentionner que le renforcement n'est pas une boîte noire secrète. Toutes les avancées que nous voyons aujourd'hui dans le domaine de l'apprentissage par renforcement sont le résultat d'esprits brillants travaillant jour et nuit sur des applications spécifiques.

La prochaine fois, nous travaillerons sur un agent Q-learning et aborderons également d'autres notions de base de l'apprentissage par renforcement.

En attendant, profitez de l'IA 🤖...

> **Important** : Cet article est la 1ère partie de la série sur l'apprentissage par renforcement profond. La série complète sera disponible à la fois sous forme de texte lisible sur [Medium](https://medium.com/@alamba093) et sous forme de vidéo explicative sur [ma chaîne YouTube](https://www.youtube.com/channel/UCRkxhh51YKqpn2gaUI3MXjg).

Pour une compréhension plus approfondie et intuitive de l'apprentissage par renforcement, je vous recommande de regarder la vidéo ci-dessous :

Abonnez-vous à ma chaîne YouTube pour plus de vidéos sur l'IA : [**ADL**](https://goo.gl/u72j6u).

_Si vous avez aimé mon article, veuillez cliquer sur le **?** car je reste motivé à écrire des articles et veuillez me suivre sur Medium._

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8B3R6kZjTkMKPv3MnUYxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-etmF1WRWkvWO6cSol7f1w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DWddirTA0TDNoAL34xjag.png)

Si vous avez des questions, veuillez me le faire savoir dans un commentaire ci-dessous ou sur [**Twitter**](https://twitter.com/I_AM_ADL). Abonnez-vous à ma chaîne YouTube pour plus de vidéos tech : [**ADL**](https://goo.gl/u72j6u).