---
title: Cours sur les Bases de Données Relationnelles – Comment Apprendre SQL dans
  VSCode en Utilisant Docker et freeCodeCamp
subtitle: ''
author: Tom Mondloch
co_authors: []
series: null
date: '2021-09-16T16:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-freecodecamps-relational-databases-curriculum-using-docker-vscode-and-coderoad
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-12-at-9.22.55-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: freeCodeCamp Curriculum
  slug: freecodecamp-curriculum
- name: Relational Database
  slug: relational-database
seo_title: Cours sur les Bases de Données Relationnelles – Comment Apprendre SQL dans
  VSCode en Utilisant Docker et freeCodeCamp
seo_desc: 'You can now learn Relational Database concepts and SQL right inside your
  VSCode editor. This tutorial will walk you through how to install it using Docker.

  During this full-length 300-hour course, you will learn to build more than a dozen
  projects. S...'
---

Vous pouvez maintenant apprendre les concepts des bases de données relationnelles et SQL directement dans votre éditeur VSCode. Ce tutoriel vous guidera à travers l'installation en utilisant Docker.

Pendant ce cours complet de 300 heures, vous apprendrez à construire plus d'une douzaine de projets. Certains d'entre eux impliqueront des instructions étape par étape, et d'autres seront ouverts, avec des suites de tests élaborées.

Vous utiliserez de vrais outils et logiciels de développement comme VS Code, PostgreSQL, et la ligne de commande Linux/Unix pour compléter des tutoriels interactifs et construire des projets.

### Ce que vous allez apprendre

* La ligne de commande Linux/Unix

* Les bases de données relationnelles

* SQL et PostgreSQL

* Bash et les scripts Bash

* Git et GitHub

* Nano

* Et beaucoup d'autres concepts et outils

Ce cours a été rendu possible grâce à une subvention de [Class Central](https://www.classcentral.com/), un moteur de recherche et site de critique pour les cours en ligne.

## Comment installer Docker et exécuter le Programme de Bases de Données Relationnelles

Docker exécutera un conteneur sur votre ordinateur qui contient le logiciel et la structure de fichiers nécessaires pour ces tutoriels.

Vous travaillerez dans ce conteneur en utilisant VSCode et l'extension Dev Containers. Une fois qu'il est en cours d'exécution, l'extension CodeRoad exécutera les tutoriels que nous avons créés.

### Prérequis

Avant de commencer, vous devez avoir installé quelques éléments :

1. Le [Docker Engine](https://docs.docker.com/engine/install/)

2. [VS Code](https://code.visualstudio.com/download)

3. L'extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) pour VS Code

4. [Git](https://git-scm.com/downloads)

### Comment Exécuter un Projet dans Docker

Suivez ces étapes pour exécuter le conteneur Docker et démarrer un tutoriel :

1. Clonez le dépôt RDB Alpha sur votre ordinateur avec `git clone https://github.com/freeCodeCamp/rdb-alpha`

2. Ouvrez un terminal, naviguez jusqu'au répertoire `rdb-alpha`, et ouvrez VS Code avec `code .`

3. Dans VS Code, ouvrez la palette de commandes avec `Ctrl / Cmd + Shift + P`. Ensuite, entrez et exécutez `Dev Containers: Rebuild and Reopen in Container`

4. Une nouvelle fenêtre VS Code s'ouvrira et commencera à construire l'image Docker. Cela prendra plusieurs minutes pour la première construction

5. Une fois l'image construite, ouvrez à nouveau la palette de commandes avec `Ctrl / Cmd + Shift + P`, entrez et exécutez `CodeRoad: Start`. La commande ne sera pas disponible tant que l'extension n'aura pas fini de s'installer dans votre conteneur

6. Dans la fenêtre CodeRoad, cliquez sur "Start New Tutorial"

7. Cliquez sur l'onglet `URL` et entrez l'URL du fichier `tutorial.json` pour le projet que vous souhaitez démarrer (ex: https://raw.githubusercontent.com/freeCodeCamp/learn-bash-by-building-a-boilerplate/main/tutorial.json). Liste complète des tutoriels disponibles ci-dessous.

8. Cliquez sur le bouton "Start" pour commencer les leçons

### Comment Redémarrer ou Changer de Projets

Si vous redémarrez ou changez de projets, vous perdrez votre progression sur un tutoriel que vous auriez commencé ainsi que tous les fichiers ou dossiers que vous auriez créés.

1. Ouvrez la palette de commandes avec `Ctrl / Cmd + Shift + P`, entrez et exécutez `Dev-Containers: Rebuild Container`

2. Attendez que VS Code rouvre et recharge le conteneur

3. Ouvrez CodeRoad depuis la palette de commandes comme vous l'avez fait auparavant, cliquez sur "Start New Tutorial", et entrez l'URL du fichier `tutorial.json` pour le projet que vous souhaitez faire

### Cours Disponibles

Voici une liste des tutoriels actuellement disponibles. Ouvrez l'un d'eux et utilisez son URL, comme décrit dans les instructions ci-dessus, pour le démarrer.

* [Apprendre Bash en Construisant un Modèle](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-by-building-a-boilerplate/main/tutorial.json)

* [Apprendre les Bases de Données Relationnelles en Construisant une Base de Données de Personnages de Jeux Vidéo](https://raw.githubusercontent.com/freeCodeCamp/learn-relational-databases-by-building-a-database-of-video-game-characters/main/tutorial.json)

* [Base de Données des Corps Célestes](https://raw.githubusercontent.com/freeCodeCamp/learn-celestial-bodies-database/main/tutorial.json)

* [Apprendre les Scripts Bash en Construisant Cinq Programmes](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-scripting-by-building-five-programs/main/tutorial.json)

* [Apprendre SQL en Construisant une Base de Données Étudiante : Partie 1](https://raw.githubusercontent.com/freeCodeCamp/learn-sql-by-building-a-student-database-part-1/main/tutorial.json)

* [Apprendre SQL en Construisant une Base de Données Étudiante : Partie 2](https://raw.githubusercontent.com/freeCodeCamp/learn-sql-by-building-a-student-database-part-2/main/tutorial.json)

* [Base de Données de la Coupe du Monde](https://raw.githubusercontent.com/freeCodeCamp/learn-world-cup-database/main/tutorial.json)

* [Apprendre Bash Avancé en Construisant un Traducteur Kitty Ipsum](https://raw.githubusercontent.com/freeCodeCamp/learn-advanced-bash-by-building-a-kitty-ipsum-translator/main/tutorial.json)

* [Apprendre Bash et SQL en Construisant un Magasin de Location de Vélos](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-and-sql-by-building-a-bike-rental-shop/main/tutorial.json)

* [Planificateur de Rendez-vous de Salon](https://raw.githubusercontent.com/freeCodeCamp/learn-salon-appointment-scheduler/main/tutorial.json)

* [Apprendre Nano en Construisant un Château](https://raw.githubusercontent.com/freeCodeCamp/learn-nano-by-building-a-castle/main/tutorial.json)

* [Apprendre Git en Construisant un Objet de Référence SQL](https://raw.githubusercontent.com/freeCodeCamp/learn-git-by-building-an-sql-reference-object/main/tutorial.json)

* [Base de Données de la Table Périodique](https://raw.githubusercontent.com/freeCodeCamp/learn-periodic-table-database/main/tutorial.json)

* [Jeu de Devinette de Nombres](https://raw.githubusercontent.com/freeCodeCamp/learn-number-guessing-game/main/tutorial.json)

#### Voici une vidéo de moi faisant "Apprendre Bash en Construisant un Modèle" en 13 minutes et 38 secondes :

%[https://www.youtube.com/watch?v=VQmCwzfSM-k]

## Téléchargez également le Thème Sombre freeCodeCamp pour VS Code

Si vous aimez le schéma de couleurs utilisé par ces tutoriels, vous pouvez télécharger l'[extension du thème sombre freeCodeCamp](https://marketplace.visualstudio.com/items?itemName=freeCodeCamp.freecodecamp-dark-vscode-theme) depuis le Visual Studio Marketplace.

Vous pouvez [en apprendre plus sur le thème sombre ici](https://www.freecodecamp.org/news/vs-code-dark-mode-theme/).

## Aidez-nous à améliorer ces cours en posant des questions et en nous donnant votre avis

Si vous avez des questions sur ces nouveaux cours de bases de données relationnelles, si vous êtes bloqué à un moment donné, ou si vous avez simplement des commentaires généraux à leur sujet, vous pouvez créer un fil de discussion sur [le forum freeCodeCamp](https://forum.freecodecamp.org/).

Nous avons également notre propre système de salon de discussion similaire à Slack où vous pouvez poser des questions et contribuer à nos projets open source. [Rejoignez notre système de salon de discussion](https://chat.freecodecamp.org/home).

Bon codage.