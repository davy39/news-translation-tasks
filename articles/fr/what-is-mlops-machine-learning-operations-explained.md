---
title: Qu'est-ce que le MLOps ? Explication des opérations de Machine Learning
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-03-26T23:35:24.000Z'
originalURL: https://freecodecamp.org/news/what-is-mlops-machine-learning-operations-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/mlops_thumb.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Devops
  slug: devops
- name: Machine Learning
  slug: machine-learning
seo_title: Qu'est-ce que le MLOps ? Explication des opérations de Machine Learning
seo_desc: 'In this article, I''ll teach you about Machine Learning Operations, which
  is like DevOps for Machine Learning.

  Until recently, all of us were learning about the standard software development
  lifecycle (SDLC). It goes from requirement elicitation to de...'
---

Dans cet article, je vais vous enseigner les opérations de Machine Learning, qui sont comme le DevOps pour le Machine Learning.

Jusqu'à récemment, nous apprenions tous le cycle de vie standard du développement logiciel (SDLC). Il va de **l'élucidation des exigences** à la **conception**, au **développement**, aux **tests**, au **déploiement**, et jusqu'à la **maintenance**.

Nous étudiions (et étudions toujours) le modèle en cascade, le modèle itératif et les modèles agiles de développement logiciel.

Maintenant, nous sommes à une étape où presque toutes les organisations tentent d'incorporer le Machine Learning (ML) - souvent appelé Intelligence Artificielle - dans leur produit.

Cette nouvelle exigence de construction de systèmes ML ajoute et reforme certains principes du SDLC, donnant naissance à une nouvelle discipline d'ingénierie appelée Machine Learning Operations, ou MLOps. Et ce nouveau terme crée un buzz et a donné naissance à de nouveaux profils d'emploi.

Ici, nous parlerons de :

* Qu'est-ce que le MLOps ?
  
* Quels problèmes le MLOps résout-il ?
  
* Quelles compétences sont nécessaires pour le MLOps ?
  

Continuez à lire et je vais expliquer chacun en détail.

## Qu'est-ce que le MLOps ?

Si vous cherchez MLOps sur Google Trends, vous verrez que c'est une discipline relativement nouvelle. Encore une fois, elle est apparue parce que de plus en plus d'organisations tentent d'intégrer des systèmes ML dans leurs produits et plateformes.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-23-at-4.39.30-AM.png align="left")

### Voici comment je définirais le MLOps :

Le MLOps est une discipline d'ingénierie qui vise à unifier le développement des systèmes ML (dev) et le déploiement des systèmes ML (ops) afin de standardiser et de rationaliser la livraison continue de modèles performants en production.

### Pourquoi le MLOps ?

Jusqu'à récemment, nous traitions des quantités de données gérables et un très petit nombre de modèles à petite échelle.

Les tables tournent maintenant, et nous intégrons l'automatisation des décisions dans une large gamme d'applications. Cela génère de nombreux défis techniques qui proviennent de la construction et du déploiement de systèmes basés sur le ML.

Pour comprendre le MLOps, nous devons d'abord comprendre le cycle de vie des systèmes ML. Le cycle de vie implique plusieurs équipes différentes d'une organisation axée sur les données.

De haut en bas, les équipes suivantes contribuent :

* **Développement commercial ou Équipe produit** — définition des objectifs commerciaux avec des KPI
  
* **Ingénierie des données** — acquisition et préparation des données.
  
* **Science des données** — architecture des solutions ML et développement de modèles.
  
* **IT ou DevOps** — configuration complète du déploiement, surveillance aux côtés des scientifiques.
  

Voici une représentation très simplifiée du cycle de vie du ML.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-23-at-6.02.55-AM.png align="left")

Les équipes de Google ont effectué de nombreuses recherches sur les défis techniques qui accompagnent la construction de systèmes basés sur le ML. Un article NeurIPS sur [la dette technique cachée dans les systèmes ML](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) montre que le développement de modèles n'est qu'une très petite partie de l'ensemble du processus. Il existe de nombreux autres processus, configurations et outils qui doivent être intégrés au système.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-23-at-7.06.03-AM.png align="left")

Pour rationaliser l'ensemble de ce système, nous avons cette nouvelle culture d'ingénierie du Machine Learning. Le système implique tout le monde, de la direction supérieure avec des compétences techniques minimales aux scientifiques des données, en passant par les DevOps et les ingénieurs ML.

## Quels problèmes le MLOps résout-il ?

Gérer de tels systèmes à grande échelle n'est pas une tâche facile, et il existe de nombreux goulots d'étranglement qui doivent être pris en compte. Voici les principaux défis auxquels les équipes sont confrontées :

* Il y a une **pénurie de scientifiques des données** qui sont bons pour développer et déployer des applications web scalables. Il existe un nouveau profil d'ingénieurs ML sur le marché ces jours-ci qui vise à répondre à ce besoin. C'est un point idéal à l'intersection de la science des données et du DevOps.
  
* **Changement des objectifs commerciaux dans le modèle** — Il y a de nombreuses dépendances avec les données changeant continuellement, le maintien des normes de performance du modèle et la garantie de la gouvernance de l'IA. Il est difficile de suivre la formation continue des modèles et l'évolution des objectifs commerciaux.
  
* **Lacunes de communication** entre les équipes techniques et commerciales avec une langue commune difficile à trouver pour collaborer. Le plus souvent, cet écart devient la raison pour laquelle de grands projets échouent.
  
* **Évaluation des risques** — il y a beaucoup de débats autour de la nature de boîte noire de tels systèmes ML/DL. Souvent, les modèles tendent à dériver de ce pour quoi ils étaient initialement prévus. Évaluer le risque/coût de tels échecs est une étape très importante et minutieuse. Par exemple, le coût d'une recommandation vidéo inexacte sur YouTube serait beaucoup plus faible par rapport au fait de signaler une personne innocente pour fraude et de bloquer son compte, et de refuser ses demandes de prêt.
  

## Quelles compétences avez-vous besoin pour le MLOps ?

À ce stade, j'ai déjà donné de nombreux aperçus des goulots d'étranglement du système et de la manière dont le MLOps résout chacun d'entre eux. Vous pouvez découvrir les compétences que vous devez cibler à partir de ces défis.

Voici les compétences clés sur lesquelles vous devez vous concentrer :

### 1. Cadrage des problèmes de ML à partir des objectifs commerciaux

Le développement des systèmes de Machine Learning commence généralement par un objectif ou un but commercial. Il peut s'agir d'un objectif simple de réduire le pourcentage de transactions frauduleuses en dessous de 0,5 %, ou de construire un système pour détecter le cancer de la peau dans des images étiquetées par des dermatologues.

Ces objectifs ont souvent certaines mesures de performance, des exigences techniques, des budgets pour le projet et des KPI (Indicateurs Clés de Performance) qui pilotent le processus de surveillance des modèles déployés.

### 2. Architecturer des solutions ML et de données pour le problème

Après que les objectifs aient été clairement traduits en problèmes de ML, l'étape suivante consiste à commencer à rechercher des données d'entrée appropriées et les types de modèles à essayer pour ce type de données.

La recherche de données est l'une des tâches les plus ardues. C'est un processus avec plusieurs parties :

* Vous devez rechercher tout ensemble de données pertinent disponible,
  
* Vérifier la crédibilité des données et de leur source.
  
* La source de données est-elle conforme aux réglementations comme le RGPD ?
  
* Comment rendre l'ensemble de données accessible ?
  
* Quel est le type de source — statique (fichiers) ou streaming en temps réel (capteurs) ?
  
* Combien de sources doivent être utilisées ?
  
* Comment construire un pipeline de données qui peut alimenter à la fois l'entraînement et l'optimisation une fois le modèle déployé dans l'environnement de production ?
  
* Quels services cloud allez-vous utiliser ?
  

### 3. Préparation et traitement des données — partie de l'ingénierie des données.

La préparation des données inclut des tâches comme l'ingénierie des caractéristiques, le nettoyage (formatage, vérification des valeurs aberrantes, imputations, rééquilibrage, etc.), puis la sélection de l'ensemble de caractéristiques qui contribuent à la sortie du problème sous-jacent.

Vous devez concevoir un pipeline complet et ensuite le coder pour produire des données propres et compatibles qui seront alimentées à la phase suivante de développement du modèle.

Une partie importante du déploiement de tels pipelines est de choisir la bonne combinaison de services cloud et d'architecture qui est performante et rentable. Par exemple, si vous avez beaucoup de mouvements de données et de grandes quantités de données à stocker, vous pouvez envisager de construire des lacs de données en utilisant AWS S3 et AWS Glue.

Vous pourriez vouloir pratiquer la construction de quelques types différents de pipelines (Batch vs Streaming) et essayer de déployer ces pipelines dans le cloud.

### 4. Entraînement des modèles et expérimentation — science des données

Dès que vos données sont préparées, vous passez à l'étape suivante de l'entraînement de votre modèle ML.

Maintenant, la phase initiale de l'entraînement est itérative avec plusieurs types différents de modèles. Vous allez réduire à la meilleure solution en utilisant plusieurs mesures quantitatives comme la précision, la justesse, le rappel, et plus encore.

Vous pouvez également utiliser l'analyse qualitative du modèle qui tient compte des mathématiques qui pilotent ce modèle ou, simplement dit, l'explicabilité du modèle.

J'ai cette liste complète de tâches que vous pouvez lire sur l'entraînement des modèles ML :

%[https://towardsdatascience.com/task-cheatsheet-for-almost-every-machine-learning-project-d0946861c6d0]

Maintenant, vous allez effectuer beaucoup d'expériences avec différents types de données et de paramètres. Un autre défi auquel les scientifiques des données sont confrontés lors de l'entraînement des modèles est la **reproductibilité**. Cela peut être résolu en versionnant vos modèles et données.

Vous pouvez ajouter le contrôle de version à tous les composants de vos systèmes ML (principalement les données et les modèles) ainsi qu'aux paramètres.

Cela est maintenant très facile à accomplir avec le développement d'outils open-source comme [**DVC**](https://dvc.org/) et [**CML**](https://cml.dev/).

Les autres tâches incluent :

* Tester un modèle en écrivant des tests unitaires pour l'entraînement du modèle.
  
* Vérifier le modèle par rapport aux références, aux modèles plus simples et à travers différentes dimensions.
  
* Mettre à l'échelle l'entraînement du modèle en utilisant des systèmes distribués, des accélérateurs matériels et une analyse scalable.
  

### 5. Construction et automatisation des pipelines ML

Vous devez construire vos pipelines ML en gardant à l'esprit les tâches suivantes :

* Identifier les exigences du système — paramètres, besoins de calcul, déclencheurs.
  
* Choisir une architecture cloud appropriée — hybride ou multi-cloud.
  
* Construire des pipelines d'entraînement et de test.
  
* Suivre et auditer les exécutions des pipelines.
  
* Effectuer la validation des données.
  

### 6. Déploiement des modèles dans le système de production

Il existe principalement deux façons de déployer un modèle ML :

* Déploiement statique ou modèle intégré — où le modèle est intégré dans un logiciel d'application installable et est ensuite déployé. Par exemple, une application qui offre un scoring par lots des demandes.
  
* Déploiement dynamique — où le modèle est déployé en utilisant un framework web comme FastAPI ou Flask et est offert comme un point de terminaison API qui répond aux demandes des utilisateurs.
  

Dans le déploiement dynamique, vous pouvez utiliser différentes méthodes :

* déploiement sur un serveur (une machine virtuelle)
  
* déploiement dans un conteneur
  
* déploiement sans serveur
  
* streaming de modèle — au lieu des API REST, tous les modèles et le code d'application sont enregistrés sur un moteur de traitement de flux comme Apache Spark, Apache Storm et Apache Flink.
  

Voici les considérations :

* S'assurer que la documentation appropriée et les scores de test sont respectés.
  
* Révalider la précision du modèle.
  
* Effectuer des vérifications d'explicabilité.
  
* S'assurer que toutes les exigences de gouvernance ont été respectées.
  
* Vérifier la qualité de tout artefact de données
  
* Test de charge — utilisation des ressources de calcul.
  

### 7. Surveillance, optimisation et maintenance des modèles

Non seulement vous devez surveiller les performances des modèles en production, mais vous devez également garantir une bonne gouvernance et équitable.

La gouvernance ici signifie ajouter des mesures de contrôle pour garantir que les modèles répondent à leurs responsabilités envers toutes les parties prenantes, les employés et les utilisateurs qui sont affectés par eux.

Dans le cadre de cette phase, nous avons besoin de scientifiques des données et d'ingénieurs DevOps pour maintenir l'ensemble du système en production en effectuant les tâches suivantes :

* Suivre la dégradation des performances et la qualité commerciale des prédictions du modèle.
  
* Mettre en place des stratégies de journalisation et établir des métriques d'évaluation continues.
  
* Dépanner les pannes du système et l'introduction de biais.
  
* Ajuster les performances du modèle dans les pipelines d'entraînement et de service déployés en production.
  

### Lectures recommandées

Cet article parlait du MLOps, qui n'est pas un profil d'emploi mais un écosystème de plusieurs parties prenantes.

Si vous êtes quelqu'un qui travaille à la croisée du ML et de l'ingénierie logicielle (DevOps), vous pourriez être un bon candidat pour les startups et les organisations de taille moyenne qui recherchent des personnes capables de gérer de tels systèmes de bout en bout.

**Ingénieur ML** est la position qui sert ce point idéal et c'est ce que les candidats aspirants devraient cibler. Voici quelques ressources que vous pouvez consulter :

* **\[Livre\]**: Le livre d'Andriy Burkov sur [Machine Learning Engineering](http://www.mlebook.com/wiki/).
  
* **\[Livre\]**: [Introduction à MLOps par O'Reilly media](https://learning.oreilly.com/library/view/introducing-mlops/9781492083283/).
  
* Vous pouvez également viser des programmes de certification comme ceux ci-dessous :
  

%[https://cloud.google.com/certification/machine-learning-engineer]

%[https://aws.amazon.com/certification/certified-machine-learning-specialty/?ch=sec&sec=rmg&d=1]

Vous pouvez également regarder la version vidéo de ce blog ici :

%[https://youtu.be/0jLdp2Tl0sM]

Si ce tutoriel était utile, vous devriez consulter mes cours de science des données et de machine learning sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.