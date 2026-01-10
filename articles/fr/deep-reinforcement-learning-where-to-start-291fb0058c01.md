---
title: 'Apprentissage par renforcement profond : par où commencer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-08T17:17:20.000Z'
originalURL: https://freecodecamp.org/news/deep-reinforcement-learning-where-to-start-291fb0058c01
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dsH8QHWSeAOFMuCrwkmWiw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Apprentissage par renforcement profond : par où commencer'
seo_desc: 'By Jannes Klaas

  Last year, DeepMind’s AlphaGo beat Go world champion Lee Sedol 4–1. More than 200
  million people watched as reinforcement learning (RL) took to the world stage. A
  few years earlier, DeepMind had made waves with a bot that could play A...'
---

Par Jannes Klaas

L'année dernière, [DeepMind](https://deepmind.com/) a battu [AlphaGo](https://deepmind.com/research/alphago/) [le champion du monde de Go, Lee Sedol, 4-1](https://www.wired.com/2016/03/two-moves-alphago-lee-sedol-redefined-future/). Plus de 200 millions de personnes ont regardé l'apprentissage par renforcement (RL) prendre la scène mondiale. Quelques années plus tôt, DeepMind avait fait des vagues avec un bot capable de jouer à des [jeux Atari](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf). L'entreprise a été rapidement acquise par Google.

De nombreux chercheurs pensent que le RL est notre meilleure chance de [créer une intelligence artificielle générale](https://en.wikipedia.org/wiki/Artificial_general_intelligence). C'est un domaine passionnant, avec de nombreux défis non résolus et un énorme potentiel.

Bien que cela puisse sembler difficile au premier abord, commencer dans le RL n'est en réalité pas si compliqué. Dans cet article, nous allons créer un simple bot avec [Keras](https://keras.io/) capable de jouer à un jeu de Catch.

### Le jeu

![Image](https://cdn-media-1.freecodecamp.org/images/1*dsH8QHWSeAOFMuCrwkmWiw.png)
_Une version plus joli du jeu sur lequel nous allons entraîner_

Catch est un jeu d'arcade très simple, que vous avez peut-être joué enfant. Des fruits tombent du haut de l'écran, et le joueur doit les attraper avec un panier. Pour chaque fruit attrapé, le joueur marque un point. Pour chaque fruit perdu, le joueur perd un point.

L'objectif ici est de laisser l'ordinateur jouer à Catch tout seul. Mais nous n'utiliserons pas le joli jeu ci-dessus. Au lieu de cela, nous utiliserons une version simplifiée pour faciliter la tâche :

![Image](https://cdn-media-1.freecodecamp.org/images/1*b4414av3RDXVcXBhbIJSnA.png)
_Notre jeu de Catch simplifié_

En jouant à Catch, le joueur choisit entre trois actions possibles. Il peut déplacer le panier vers la gauche, vers la droite ou rester immobile.

La base de cette décision est l'état actuel du jeu. En d'autres termes : les positions du fruit qui tombe et du panier.

Notre objectif est de créer un modèle qui, étant donné le contenu de l'écran de jeu, choisit l'action qui mène au score le plus élevé possible.

Cette tâche peut être vue comme un simple problème de classification. Nous pourrions demander à des joueurs humains experts de jouer au jeu plusieurs fois et d'enregistrer leurs actions. Ensuite, nous pourrions entraîner un modèle à choisir l'action « correcte » qui imite les joueurs experts.

Mais ce n'est pas ainsi que les humains apprennent. Les humains peuvent apprendre un jeu comme Catch par eux-mêmes, sans guidance. C'est très utile. Imaginez si vous deviez engager un groupe d'experts pour effectuer une tâche des milliers de fois chaque fois que vous vouliez apprendre quelque chose d'aussi simple que Catch ! Ce serait coûteux et lent.

Dans l'apprentissage par renforcement, le modèle s'entraîne à partir de l'expérience, plutôt que de données étiquetées.

### Apprentissage par renforcement profond

L'apprentissage par renforcement est inspiré par la psychologie comportementale.

Au lieu de fournir au modèle des actions « correctes », nous lui fournissons des récompenses et des punitions. Le modèle reçoit des informations sur l'état actuel de l'environnement (par exemple, l'écran du jeu informatique). Il produit ensuite une action, comme un mouvement de joystick. L'environnement réagit à cette action et fournit l'état suivant, ainsi que les récompenses éventuelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uq1GGg_NOi-Z4pVhOOYFTA.jpeg)

Le modèle apprend ensuite à trouver des actions qui mènent à des récompenses maximales.

Il existe de nombreuses façons de mettre cela en pratique. Ici, nous allons examiner le Q-Learning. Le Q-Learning a fait sensation lorsqu'il a été utilisé pour entraîner un ordinateur à jouer à des jeux Atari. Aujourd'hui, il reste un concept pertinent. La plupart des algorithmes modernes de RL sont une adaptation du Q-Learning.

#### Intuition du Q-learning

Une bonne façon de comprendre le Q-learning est de comparer le jeu de Catch avec le jeu d'échecs.

Dans les deux jeux, vous recevez un état, `S`. Aux échecs, il s'agit des positions des pièces sur le plateau. Dans Catch, il s'agit de l'emplacement du fruit et du panier.

Le joueur doit ensuite effectuer une action, `A`. Aux échecs, il s'agit de déplacer une pièce. Dans Catch, il s'agit de déplacer le panier vers la gauche ou la droite, ou de rester dans la position actuelle.

En conséquence, il y aura une récompense `R`, et un nouvel état `S'`.

Le problème avec Catch et les échecs est que les récompenses n'apparaissent pas immédiatement après l'action.

Dans Catch, vous ne gagnez des récompenses que lorsque les fruits touchent le panier ou tombent par terre, et aux échecs, vous ne gagnez une récompense que lorsque vous gagnez ou perdez la partie. Cela signifie que les récompenses sont **peu fréquentes**. La plupart du temps, `R` sera zéro.

Lorsque qu'il y a une récompense, elle n'est pas toujours le résultat de l'action prise immédiatement avant. Une action prise longtemps avant pourrait avoir causé la victoire. Découvrir quelle action est responsable de la récompense est souvent appelé le **problème d'attribution de crédit**.

Parce que les récompenses sont retardées, les bons joueurs d'échecs ne choisissent pas leurs coups uniquement en fonction de la récompense immédiate. Au lieu de cela, ils choisissent en fonction de la **récompense future attendue**.

Par exemple, ils ne pensent pas seulement à savoir s'ils peuvent éliminer une pièce de l'adversaire au prochain coup. Ils considèrent également comment prendre une certaine action maintenant les aidera à long terme.

Dans le Q-learning, nous choisissons notre action en fonction de la récompense future attendue la plus élevée. Nous utilisons une « fonction Q » pour la calculer. Il s'agit d'une [fonction mathématique](https://www.mathsisfun.com/sets/function.html) qui prend deux arguments : l'état actuel du jeu et une action donnée.

Nous pouvons écrire cela comme : `Q(état, action)`

Alors que dans l'état `S`, nous estimons la récompense future pour chaque action possible `A`. Nous supposons qu'après avoir pris l'action `A` et être passé à l'état suivant `S'`, tout se passe parfaitement.

La récompense future attendue `Q(S,A)` pour un état donné `S` et une action `A` est calculée comme la récompense immédiate `R`, plus la récompense future attendue par la suite `Q(S',A')`. Nous supposons que l'action suivante `A'` est optimale.

Parce qu'il y a une incertitude sur l'avenir, nous réduisons `Q(S',A')` par le facteur gamma γ.

`Q(S,A) = R + γ * max Q(S',A')`

Les bons joueurs d'échecs sont très bons pour estimer les récompenses futures dans leur tête. En d'autres termes, leur fonction Q `Q(S,A)` est très précise.

La plupart de la pratique des échecs tourne autour du développement d'une meilleure fonction Q. Les joueurs parcourent de nombreuses anciennes parties pour apprendre comment certains coups se sont déroulés dans le passé, et à quel point une action donnée est susceptible de mener à la victoire.

Mais comment une machine peut-elle estimer une bonne fonction Q ? C'est là que les réseaux de neurones entrent en jeu.

### Régression après tout

En jouant à un jeu, nous générons beaucoup d'« expériences ». Ces expériences consistent en :

* l'état initial, `S`
* l'action entreprise, `A`
* la récompense gagnée, `R`
* et l'état qui a suivi, `S'`

Ces expériences sont nos données d'entraînement. Nous pouvons formuler le problème d'estimation de `Q(S,A)` comme un [problème de régression](https://en.wikipedia.org/wiki/Regression_analysis). Pour résoudre cela, nous pouvons utiliser un [réseau de neurones](http://news.mit.edu/2017/explained-neural-networks-deep-learning-0414).

Étant donné un vecteur d'entrée constitué de `S` et `A`, le réseau de neurones est censé prédire la valeur de `Q(S,A)` égale à la cible : `R + γ * max Q(S',A')`.

Si nous sommes bons pour prédire `Q(S,A)` pour différents états `S` et actions `A`, nous avons une bonne approximation de la fonction Q. Notez que nous estimons `Q(S',A')` par le même réseau de neurones que `Q(S,A)`.

### Le processus d'entraînement

Étant donné un lot d'expériences `< S, A, R, S'` >, le processus d'entraînement se présente comme suit :

1. Pour chaque action possible `A'` (gauche, droite, rester), prédire la récompense future attendue `Q(S',A')` en utilisant le réseau de neurones
2. Choisir la valeur la plus élevée des trois prédictions comme `max Q(S',A')`
3. Calculer `r + γ * max Q(S',A')`. C'est la valeur cible pour le réseau de neurones
4. Entraîner le réseau de neurones en utilisant une fonction de perte. Il s'agit d'une fonction qui calcule à quel point la valeur prédite est proche ou éloignée de la valeur cible. Ici, nous utiliserons `0.5 * (predicted_Q(S,A) — target)²` comme fonction de perte.

Pendant le jeu, toutes les expériences sont stockées dans une **mémoire de relecture**. Cela agit comme un simple tampon dans lequel nous stockons les paires `< S, A, R, S'` >. La classe de relecture d'expérience gère également la préparation des données pour l'entraînement. Consultez le code ci-dessous :

### Définition du modèle

Il est maintenant temps de définir le modèle qui apprendra une fonction Q pour Catch.

Nous utilisons [Keras](https://keras.io/) comme interface pour [Tensorflow](https://www.tensorflow.org/). Notre modèle de base est un simple réseau dense à trois couches.

Déjà, ce modèle fonctionne assez bien sur cette version simplifiée de Catch. Rendez-vous sur GitHub pour la [implémentation complète](https://github.com/JannesKlaas/sometimes_deep_sometimes_learning/blob/master/reinforcement.ipynb). Vous pouvez expérimenter avec des modèles plus complexes pour voir si vous pouvez obtenir de meilleures performances.

### Exploration

Un ingrédient final pour le Q-Learning est l'exploration.

La vie quotidienne montre que parfois vous devez faire quelque chose de bizarre et/ou aléatoire pour découvrir s'il y a quelque chose de mieux que votre trotte quotidienne.

Il en va de même pour le Q-Learning. Toujours choisir la meilleure option signifie que vous pourriez manquer certains chemins inexplorés. Pour éviter cela, l'apprenant choisira parfois une option aléatoire, et pas nécessairement la meilleure.

Maintenant, nous pouvons définir la méthode d'entraînement :

J'ai laissé le jeu s'entraîner pendant 5 000 époques, et il se débrouille plutôt bien maintenant !

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzxoQUnU2ZPOKF2qmcdRwQ.gif)
_Notre joueur de Catch en action_

Comme vous pouvez le voir dans l'animation, l'ordinateur attrape les pommes qui tombent du ciel.

Pour visualiser comment le modèle a appris, j'ai tracé la [moyenne mobile](https://en.wikipedia.org/wiki/Moving_average) des victoires sur les époques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HEtvd7a1TBqPOaGQNulAQw.png)

### Où aller à partir d'ici

Vous avez maintenant une première vue d'ensemble et une intuition du RL. Je recommande de jeter un œil au [code complet](https://github.com/JannesKlaas/sometimes_deep_sometimes_learning/blob/master/reinforcement.ipynb) de ce tutoriel. Vous pouvez expérimenter avec.

Vous pourriez également vouloir consulter [la série d'Arthur Juliani](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0). Si vous souhaitez une introduction plus formelle, consultez [CS 234 de Stanford](http://web.stanford.edu/class/cs234/index.html), [CS 294 de Berkeley](http://rll.berkeley.edu/deeprlcourse/) ou [les conférences de David Silver de l'UCL](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html).

Une excellente façon de pratiquer vos compétences en RL est [OpenAI's Gym](https://gym.openai.com/envs/), qui offre un ensemble d'environnements d'entraînement avec une API standardisée.

#### Remerciements

Cet article s'appuie sur [l'exemple simple de RL d'Eder Santana](https://gist.github.com/EderSantana/c7222daa328f0e885093), de 2016. J'ai refactorisé son code et ajouté des explications dans un [notebook](https://github.com/JannesKlaas/sometimes_deep_sometimes_learning/blob/master/reinforcement.ipynb) que j'ai écrit plus tôt en 2017. Pour la lisibilité sur Medium, je ne montre ici que le code le plus pertinent. Rendez-vous sur le [notebook](https://github.com/JannesKlaas/sometimes_deep_sometimes_learning/blob/master/reinforcement.ipynb) ou [l'article original d'Eder](http://edersantana.github.io/articles/keras_rl/) pour plus d'informations.

#### À propos de Jannes Klaas

Ce texte fait partie du [matériel de cours sur l'apprentissage automatique en contexte financier](https://github.com/JannesKlaas/MLiFC), qui aide les étudiants en économie et en commerce à comprendre l'apprentissage automatique.

J'ai passé une décennie à construire des logiciels et je suis maintenant en train d'apporter l'apprentissage automatique au monde financier. J'étudie à la Rotterdam School of Management et j'ai fait des recherches avec l'Institut pour le logement et les études de développement urbain.

Vous pouvez me suivre sur [Twitter](https://twitter.com/jannesklaas). Si vous avez des questions ou des suggestions, veuillez laisser un commentaire ou me contacter sur [Medium](https://medium.com/@jannesklaas).