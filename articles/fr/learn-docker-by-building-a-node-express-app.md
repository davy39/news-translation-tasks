---
title: Apprenez Docker en construisant une application Node / Express
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-04-29T20:05:04.000Z'
originalURL: https://freecodecamp.org/news/learn-docker-by-building-a-node-express-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/dockerdevops.png
tags:
- name: Docker
  slug: docker
- name: youtube
  slug: youtube
seo_title: Apprenez Docker en construisant une application Node / Express
seo_desc: 'Docker is an open source project that makes it easy to create containers
  and container-based apps. Docker''s lightweight and portable software containers
  simplify application development, testing, and deployment.

  We just released a course on the freeC...'
---

Docker est un projet open source qui facilite la création de conteneurs et d'applications basées sur des conteneurs. Les conteneurs logiciels légers et portables de Docker simplifient le développement, les tests et le déploiement d'applications.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous aidera à apprendre les bases fondamentales de Docker en construisant une application Node/Express avec une base de données MongoDB et Redis.

Sanjeev Thiyagarajan a développé ce cours. Sanjeev a énormément d'expérience avec Docker et il est tout à fait qualifié pour enseigner ce cours.

Tout d'abord, vous apprendrez à utiliser un seul conteneur. Progressivement, vous ajouterez de la complexité à l'application en intégrant un conteneur MongoDB, puis en ajoutant enfin une base de données Redis pour l'authentification.

Vous apprendrez à faire les choses manuellement avec le CLI et aussi à utiliser Docker Compose. Le cours se concentre sur les défis du passage d'un environnement de développement à un environnement de production. Vous apprendrez à déployer avec une VM Ubuntu comme serveur de production et à utiliser un orchestrateur de conteneurs comme Docker Swarm pour gérer les mises à jour progressives (rolling updates).

Voici les sections de ce cours :

### Partie 1 : Introduction

* Intro & démo de l'application Express
* Images personnalisées avec Dockerfile
* Couches d'images Docker et mise en cache
* Réseautage Docker et ouverture de ports
* Fichier Dockerignore
* Synchronisation du code source avec les bind mounts
* Astuce pour les volumes anonymes
* Bind Mounts en lecture seule
* Variables d'environnement
* Chargement des variables d'environnement à partir d'un fichier
* Suppression des volumes obsolètes
* Docker Compose
* Configurations de développement vs production

### Partie 2 : Travailler avec plusieurs conteneurs

* Ajout d'un conteneur MongoDB
* Communication entre conteneurs
* Fichier de configuration Express
* Ordre de démarrage des conteneurs
* Construction d'une application CRUD
* Inscription et connexion
* Authentification avec sessions et Redis
* Revue d'architecture
* Nginx pour l'équilibrage de charge vers plusieurs conteneurs Node
* Express CORS

### Partie 3 : Passage en production

* Installation de Docker sur Ubuntu (Digital Ocean)
* Configuration de Git
* Variables d'environnement sur Ubuntu
* Déploiement de l'application sur le serveur de production
* Pousser les changements à la dure
* Reconstruction des conteneurs
* Revue du flux de travail de Dev à Prod
* Flux de travail Dockerhub amélioré
* Automatisation avec Watchtower 
* Pourquoi nous avons besoin d'un orchestrateur
* Docker Swarm
* Pousser les changements vers la pile (stack) Swarm

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org](https://www.youtube.com/watch?v=9zUHg7xjIqQ) (5 heures de visionnage).

%[https://www.youtube.com/watch?v=9zUHg7xjIqQ]