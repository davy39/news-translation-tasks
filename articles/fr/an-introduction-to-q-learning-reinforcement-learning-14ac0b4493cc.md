---
title: 'Une introduction à l''apprentissage Q : apprentissage par renforcement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-03T21:31:39.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DX9ZRnzwmh2FImV-
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
seo_title: 'Une introduction à l''apprentissage Q : apprentissage par renforcement'
seo_desc: 'By ADL

  This article is the second part of my “Deep reinforcement learning” series. The
  complete series shall be available both on Medium and in videos on my YouTube channel.

  In the first part of the series we learnt the basics of reinforcement learni...'
---

Par ADL

Cet article est la deuxième partie de ma série « Deep reinforcement learning ». La série complète sera disponible à la fois sur [Medium](https://medium.com/@alamba093) et en vidéos sur [ma chaîne YouTube](https://www.youtube.com/channel/UCRkxhh51YKqpn2gaUI3MXjg).

Dans la [première partie de la série](https://medium.freecodecamp.org/a-brief-introduction-to-reinforcement-learning-7799af5840db), nous avons appris les **bases de l'apprentissage par renforcement**. 

Q-Learning est un algorithme d'apprentissage basé sur les valeurs en apprentissage par renforcement. Dans cet article, nous apprenons le Q-Learning et ses détails :

* Qu'est-ce que le Q-Learning ?
* Les mathématiques derrière le Q-Learning
* Implémentation en utilisant Python

### Q-Learning — un aperçu simplifié

Disons qu'un **robot** doit traverser un **labyrinthe** et atteindre le point final. Il y a des **mines**, et le robot ne peut se déplacer qu'une case à la fois. Si le robot marche sur une mine, il meurt. Le robot doit atteindre le point final dans le temps le plus court possible.

Le système de notation/récompense est le suivant :

1. Le robot perd 1 point à chaque étape. Cela est fait pour que le robot prenne le chemin le plus court et atteigne l'objectif le plus rapidement possible.
2. Si le robot marche sur une mine, la perte de points est de 100 et le jeu se termine.
3. Si le robot obtient de l'énergie ⚡, il gagne 1 point.
4. Si le robot atteint l'objectif final, il obtient 100 points.

Maintenant, la question évidente est : **Comment entraîner un robot à atteindre l'objectif final avec le chemin le plus court sans marcher sur une mine ?**

![Image](https://cdn-media-1.freecodecamp.org/images/3JXI06jyHegMS1Yx8rhIq64gkYwSTM7ZhD25)

Alors, comment résoudre cela ?

### Introduction à la Q-Table

Q-Table est simplement un nom sophistiqué pour une table de consultation simple où nous calculons les récompenses futures maximales attendues pour une action à chaque état. Basiquement, cette table nous guidera vers la meilleure action à chaque état.

![Image](https://cdn-media-1.freecodecamp.org/images/CcNuUwGnpHhRKkERqJJ6xl7N2W8jcl1yVdE8)

Il y aura quatre actions possibles à chaque case non bordure. Lorsqu'un robot est dans un état, il peut soit monter, descendre, aller à droite ou à gauche.

Alors, modélisons cet environnement dans notre Q-Table.

Dans la Q-Table, les colonnes sont les actions et les lignes sont les états.

![Image](https://cdn-media-1.freecodecamp.org/images/AjVvggEquHgsnMN8i4N35AMfx53vZtELEL-l)

Chaque score de la Q-Table sera la récompense future maximale attendue que le robot obtiendra s'il effectue cette action dans cet état. C'est un processus itératif, car nous devons améliorer la Q-Table à chaque itération.

Mais les questions sont :

* Comment calculons-nous les valeurs de la Q-Table ?
* Les valeurs sont-elles disponibles ou prédéfinies ?

Pour apprendre chaque valeur de la Q-Table, nous utilisons l'**algorithme Q-Learning**.

### Mathématiques : l'algorithme Q-Learning

#### Fonction Q

La **fonction Q** utilise l'équation de Bellman et prend deux entrées : l'état (**s**) et l'action (**a**).

![Image](https://cdn-media-1.freecodecamp.org/images/s39aVodqNAKMTcwuMFlyPSy76kzAmU5idMzk)

En utilisant la fonction ci-dessus, nous obtenons les valeurs de **Q** pour les cellules de la table.

Lorsque nous commençons, toutes les valeurs dans la Q-Table sont à zéro.

Il y a un processus itératif de mise à jour des valeurs. À mesure que nous commençons à explorer l'environnement, la fonction Q nous donne de meilleures et meilleures approximations en mettant continuellement à jour les valeurs Q dans la table.

Maintenant, comprenons comment la mise à jour se fait.

### Introduction au processus de l'algorithme Q-Learning

![Image](https://cdn-media-1.freecodecamp.org/images/oQPHTmuB6tz7CVy3L05K1NlBmS6L8MUkgOud)

Chacune des cases colorées est une étape. Comprenons chacune de ces étapes en détail.

#### **Étape 1 : initialiser la Q-Table**

Nous allons d'abord construire une Q-Table. Il y a n colonnes, où n = nombre d'actions. Il y a m lignes, où m = nombre d'états. Nous allons initialiser les valeurs à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/TQ9Wy3guJHUecTf0YA5AuQgB9yVIohgLXKIn)

![Image](https://cdn-media-1.freecodecamp.org/images/gWnhK5oLqjcQkSzuuT8WgMVOGdCEp68Xvt6F)

Dans notre exemple de robot, nous avons quatre actions (a=4) et cinq états (s=5). Nous allons donc construire une table avec quatre colonnes et cinq lignes.

#### **Étape 2 et 3 : choisir et effectuer une action**

Cette combinaison d'étapes est effectuée pendant une durée indéfinie. Cela signifie que cette étape s'exécute jusqu'à ce que nous arrêtions l'entraînement, ou que la boucle d'entraînement s'arrête comme défini dans le code.

Nous allons choisir une action (a) dans l'état (s) en fonction de la Q-Table. Mais, comme mentionné précédemment, lorsque l'épisode commence initialement, chaque valeur Q est 0.

Le concept de compromis entre exploration et exploitation entre alors en jeu. [Cet article contient plus de détails](https://medium.freecodecamp.org/a-brief-introduction-to-reinforcement-learning-7799af5840db).

Nous allons utiliser quelque chose appelé la **stratégie epsilon-greedy**.

Au début, les taux epsilon seront plus élevés. Le robot explorera l'environnement et choisira des actions de manière aléatoire. La logique derrière cela est que le robot ne sait rien de l'environnement.

À mesure que le robot explore l'environnement, le taux epsilon diminue et le robot commence à exploiter l'environnement.

Au cours du processus d'exploration, le robot devient progressivement plus confiant dans l'estimation des valeurs Q.

**Pour l'exemple du robot, il y a quatre actions à choisir** : haut, bas, gauche et droite. Nous commençons l'entraînement maintenant — notre robot ne sait rien de l'environnement. Le robot choisit donc une action aléatoire, disons droite.

![Image](https://cdn-media-1.freecodecamp.org/images/k0IARc6DzE3NBl2ugpWkzwLkR9N4HRkpSpjw)

Nous pouvons maintenant mettre à jour les valeurs Q pour être au début et aller à droite en utilisant l'équation de Bellman.

#### **Étape 4 et 5 : évaluer**

Maintenant, nous avons effectué une action et observé un résultat et une récompense. Nous devons mettre à jour la fonction Q(s,a).

![Image](https://cdn-media-1.freecodecamp.org/images/TnN7ys7VGKoDszzv3WDnr5H8txOj3KKQ0G8o)

Dans le cas du jeu de robot, pour réitérer la structure de notation/récompense est :

* **énergie** = +1
* **mine** = -100
* **fin** = +100

![Image](https://cdn-media-1.freecodecamp.org/images/EpQDzt7lCbmFyMVUzNGaPam3WCYNuD1-hVxu)

![Image](https://cdn-media-1.freecodecamp.org/images/xQtpQAhBocPC46-f0GRHDOK3ybrz4ZasaDo4)

Nous allons répéter cela encore et encore jusqu'à ce que l'apprentissage soit arrêté. De cette manière, la Q-Table sera mise à jour.

### Implémentation Python du Q-Learning

Le concept et l'implémentation du code sont [expliqués dans ma vidéo](https://www.youtube.com/watch?v=yefGGgz20tY).

Abonnez-vous à ma chaîne YouTube pour plus de vidéos sur l'IA : [**ADL**](https://goo.gl/u72j6u).

### Enfin... faisons un récapitulatif

* Le Q-Learning est un algorithme d'apprentissage par renforcement basé sur les valeurs qui est utilisé pour trouver la politique de sélection d'action optimale en utilisant une fonction Q.
* Notre objectif est de maximiser la fonction de valeur Q.
* La Q-Table nous aide à trouver la meilleure action pour chaque état.
* Elle aide à maximiser la récompense attendue en sélectionnant la meilleure de toutes les actions possibles.
* Q(état, action) retourne la récompense future attendue de cette action dans cet état.
* Cette fonction peut être estimée en utilisant le Q-Learning, qui met à jour itérativement Q(s,a) en utilisant l'**équation de Bellman**.
* Initialement, nous explorons l'environnement et mettons à jour la Q-Table. Lorsque la Q-Table est prête, l'agent commencera à exploiter l'environnement et à prendre de meilleures actions.

**La prochaine fois, nous travaillerons sur un exemple de deep Q-learning**.

En attendant, profitez de l'IA ?.

**Important** : Comme indiqué précédemment, cet article est la deuxième partie de ma série « Deep Reinforcement Learning ». La série complète sera disponible à la fois en articles sur [Medium](https://medium.com/@alamba093) et en vidéos sur [ma chaîne YouTube](https://www.youtube.com/channel/UCRkxhh51YKqpn2gaUI3MXjg).

Si vous avez aimé mon article, **veuillez cliquer sur le ?** pour m'aider à rester motivé à écrire des articles. Veuillez me suivre sur Medium et sur les autres réseaux sociaux :

![Image](https://cdn-media-1.freecodecamp.org/images/Dxy5hJfhxEP5eWOBqW6QOqH0QgjIU04PD6rQ)

![Image](https://cdn-media-1.freecodecamp.org/images/d8UR8YDfmLtfDokKlQb32-prgyUUEWt3-glP)

![Image](https://cdn-media-1.freecodecamp.org/images/qPgqeEBS0ugejKsKGGHD3KpoyYyGEHytVENe)

Si vous avez des questions, n'hésitez pas à me le faire savoir dans un commentaire ci-dessous ou sur [**Twitter**](https://twitter.com/I_AM_ADL).

Abonnez-vous à [ma chaîne YouTube](https://goo.gl/u72j6u) pour plus de vidéos tech.