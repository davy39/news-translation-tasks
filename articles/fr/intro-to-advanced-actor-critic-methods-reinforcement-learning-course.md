---
title: 'Introduction aux méthodes avancées Actor-Critic : Cours sur l''apprentissage
  par renforcement'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-30T22:20:15.000Z'
originalURL: https://freecodecamp.org/news/intro-to-advanced-actor-critic-methods-reinforcement-learning-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/activecritic.png
tags:
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: youtube
  slug: youtube
seo_title: 'Introduction aux méthodes avancées Actor-Critic : Cours sur l''apprentissage
  par renforcement'
seo_desc: 'Actor-Critic Methods are very useful reinforcement learning techniques.

  Actor-critic methods are most useful for applications in robotics as they allow
  software to output continuous, rather than discrete actions. This enables control
  of electric moto...'
---

Les méthodes Actor-Critic sont des techniques très utiles d'apprentissage par renforcement.

Les méthodes actor-critic sont particulièrement utiles pour les applications en robotique, car elles permettent au logiciel de produire des actions continues plutôt que discrètes. Cela permet de contrôler les moteurs électriques pour actionner le mouvement dans les systèmes robotiques, au prix d'une complexité computationnelle accrue.

Nous venons de publier un cours complet sur les méthodes Actor-Critic sur la chaîne YouTube de freeCodeCamp.org.

Dr. Tabor a développé ce cours. Il est physicien et ancien ingénieur en semi-conducteurs, désormais scientifique des données.

L'idée de base derrière les méthodes actor-critic est qu'il existe deux réseaux de neurones profonds. Le réseau acteur approxime la politique de l'agent : une distribution de probabilité qui nous indique la probabilité de sélectionner une action (continue) étant donné un certain état de l'environnement. Le réseau critique approxime la fonction de valeur : l'estimation par l'agent des récompenses futures qui suivent l'état actuel. Ces deux réseaux interagissent pour orienter la politique vers des états plus rentables, où la rentabilité est déterminée par l'interaction avec l'environnement.

Cela ne nécessite aucune connaissance préalable du fonctionnement de notre environnement, ni aucune entrée concernant les règles du jeu. Tout ce que nous avons à faire est de laisser l'algorithme interagir avec l'environnement et d'observer comment il apprend.

Ce cours intègre également certaines innovations utiles de l'apprentissage Q profond, telles que l'utilisation de tampons de relecture d'expérience et de réseaux cibles. Cela augmente la stabilité et la robustesse des politiques apprises, afin que nos agents puissent apprendre des politiques efficaces pour naviguer dans les environnements Open AI gym.

Voici les algorithmes abordés dans ce cours :

* Actor Critic
* Deep Deterministic Policy Gradients (DDPG)
* Twin Delayed Deep Deterministic Policy Gradients (TD3)
* Proximal Policy Optimization (PPO)
* Soft Actor Critic (SAC)
* Asynchronous Advantage Actor Critic (A3C)

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/K2qjAixgLqk) (6 heures de visionnage).

%[https://youtu.be/K2qjAixgLqk]