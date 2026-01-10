---
title: Créer des API avec Python - Cours gratuit de 19 heures
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-01T21:00:54.000Z'
originalURL: https://freecodecamp.org/news/creating-apis-with-python-free-19-hour-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pythonapi.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Créer des API avec Python - Cours gratuit de 19 heures
seo_desc: 'A lot of API tutorials just teach the absolute minimum. But a production-ready
  API is much more complicated than what most tutorials teach.

  We just published a massive 19-hour course on the freeCodeCamp.org YouTube channel
  that will teach you how to ...'
---

Beaucoup de tutoriels sur les API n'enseignent que le strict minimum. Mais une API prête pour la production est bien plus complexe que ce que la plupart des tutoriels enseignent.

Nous venons de publier un cours massif de 19 heures sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à construire une API complète en utilisant Python et la bibliothèque FastAPI.

Sanjeev Thiyagarajan a développé ce cours. Sanjeev est un excellent enseignant et sait vraiment comment décomposer les choses pour les débutants.

L'API construite dans ce cours est pour une application de type réseau social où les utilisateurs peuvent créer/lire/supprimer/mettre à jour des publications ainsi qu'aimer les publications d'autres utilisateurs. Elle inclut l'enregistrement des utilisateurs et l'authentification.

Tout d'abord, vous apprendrez les fondamentaux de la conception d'API, y compris les routes, la sérialisation/désérialisation, la validation de schéma et les modèles. Vous apprendrez également comment configurer et utiliser les bases de données SQL.

Ensuite, vous apprendrez comment intégrer l'API avec la base de données en utilisant à la fois des requêtes SQL brutes et l'ORM SqlAlchemy. PostgreSQL est utilisé comme base de données, mais tout ce que vous apprendrez sera applicable à presque toutes les autres bases de données SQL.

Ensuite, vous apprendrez comment configurer les tests pour l'application en utilisant la bibliothèque pytest. Vous configurerez une base de données de test et effectuerez un bon nombre de tests d'intégration.

Après avoir créé l'API, vous apprendrez comment déployer l'API en utilisant deux méthodes différentes. La première consiste à déployer sur une machine Ubuntu et la seconde à déployer sur Heroku. Vous apprendrez même comment dockeriser l'application.

Enfin, vous apprendrez comment construire un pipeline CI/CD en utilisant les actions GitHub.

Voici une liste complète des sujets abordés dans ce cours complet :

### Section 1 : Introduction

* Projet du cours
* Introduction au cours
* Aperçu du projet du cours

### Section 2 : Installation

* Installation de Python sur Mac
* Installation et configuration de VS Code sur Mac
* Installation de Python sur Windows
* Installation et configuration de VS Code sur Windows
* Bases de l'environnement virtuel Python
* Environnement virtuel sur Windows
* Environnement virtuel sur Mac

### Section 3 : FastAPI

* Installer les dépendances avec pip
* Démarrer FastAPI
* Opérations de chemin
* Ordre des opérations de chemin (oui, c'est important)
* Introduction à Postman
* Requêtes HTTP Post
* Validation de schéma avec Pydantic
* Opérations CRUD
* Stocker les publications dans un tableau
* Créer des publications
* Collections Postman et sauvegarde des requêtes
* Récupérer une publication
* L'ordre du chemin est important
* Changer les codes de statut de réponse
* Supprimer des publications
* Mettre à jour des publications
* Documentation automatique
* Paquets Python

### Section 4 : Bases de données

* Introduction aux bases de données
* Installation de Postgres sur Windows
* Installation de Postgres sur Mac
* Schéma de base de données et tables
* Gestion de Postgres avec l'interface graphique PgAdmin
* Votre première requête SQL
* Filtrer les résultats avec le mot-clé "where"
* Opérateurs SQL
* Mot-clé IN
* Correspondance de motifs avec le mot-clé LIKE
* Ordonner les résultats
* LIMIT et OFFSET
* Insertion de données
* Suppression de données
* Mise à jour de données

### Section 5 : Python + SQL brut

* Configuration de la base de données de l'application
* Connexion à la base de données avec Python
* Récupération des publications
* Création d'une publication
* Récupération d'une publication
* Suppression d'une publication
* Mise à jour d'une publication

### Section 6 : ORM

* Introduction aux ORM
* Configuration de SQLAlchemy
* Ajout de la colonne CreatedAt
* Récupération de toutes les publications
* Création de publications
* Récupération d'une publication par ID
* Suppression d'une publication
* Mise à jour d'une publication

### Section 7 : Modèles Pydantic

* Pydantic vs modèles ORM
* Approfondissement des modèles Pydantic
* Modèle de réponse

### Section 8 : Authentification et utilisateurs

* Création de la table des utilisateurs
* Opération de chemin d'enregistrement des utilisateurs
* Hachage des mots de passe des utilisateurs
* Refactorisation de la logique de hachage
* Récupération d'un utilisateur par ID
* Routeurs FastAPI
* Préfixe de routeur
* Balises de routeur
* Bases des tokens JWT
* Processus de connexion
* Création d'un token
* OAuth2 PasswordRequestForm
* Vérification que l'utilisateur est connecté
* Correction de bugs
* Protection des routes
* Test d'un token expiré
* Récupération de l'utilisateur dans les routes protégées
* Fonctionnalités avancées de Postman

### Section 9 : Relations

* Bases des relations SQL
* Clés étrangères Postgres
* Clés étrangères SQLAlchemy
* Mise à jour du schéma de publication pour inclure l'utilisateur
* Attribution de l'ID du propriétaire lors de la création d'une nouvelle publication
* Suppression et mise à jour uniquement de vos propres publications
* Récupération uniquement des publications de l'utilisateur connecté
* Relations Sqlalchemy
* Paramètres de requête
* Nettoyage de notre fichier main.py
* Variables d'environnement

### Section 10 : Système de vote/like

* Théorie du vote/like
* Table des votes
* Votes Sqlalchemy
* Route des votes
* Jointures SQL
* Jointures dans SqlAlchemy
* Récupération d'une publication avec des jointures

### Section 11 : Migration de base de données avec Alembic

* Qu'est-ce qu'un outil de migration de base de données
* Configuration d'Alembic
* Première révision d'Alembic
* Retour arrière du schéma de la base de données Alembic
* Finalisation du reste du schéma avec Alembic
* Désactiver la création du moteur SqlAlchemy

### Section 12 : Liste de contrôle pré-déploiement

* Qu'est-ce que CORS ?????
* Prérequis Git
* Installation de Git
* Github

### Section 13 : Déploiement sur Heroku

* Introduction à Heroku
* Créer une application Heroku
* Fichier procfile Heroku
* Ajout d'une base de données Postgres
* Variables d'environnement dans Heroku
* Migrations Alembic sur l'instance Postgres Heroku
* Pousser les changements en production

### Section 14 : Déploiement sur Ubuntu

* Créer une machine virtuelle Ubuntu
* Mettre à jour les paquets
* Installer Python
* Installer Postgres et configurer le mot de passe
* Configuration de Postgres
* Créer un nouvel utilisateur et configurer l'environnement Python
* Variables d'environnement
* Migrations Alembic sur la base de données de production
* Gunicorn
* Création d'un service Systemd
* NGINX
* Configuration du nom de domaine
* SSL/HTTPS
* Activation de NGINX
* Pare-feu
* Pousser les changements de code en production

### Section 15 : Docker

* Dockerfile
* Docker Compose
* Conteneur Postgres
* Montages de liaison
* Dockerhub
* Production vs Développement

### Section 16 : Tests

* Introduction aux tests
* Écrire votre premier test
* Les flags -s et -v
* Tester plus de fonctions
* Paramétrer
* Tester des classes
* Fixtures
* Combiner Fixtures + Paramétrer
* Tester les exceptions
* FastAPI TestClient
* Flags Pytest
* Test de création d'utilisateur
* Configuration de la base de données de test
* Créer et détruire la base de données après chaque test
* Plus de Fixtures pour gérer l'interaction avec la base de données
* Barres obliques finales dans le chemin
* Portée des Fixtures
* Fixture de test utilisateur
* Test/validation de token
* Conftest.py
* Test de connexion échoué
* Test de récupération de toutes les publications
* Fixture de publications pour créer des publications de test
* Test de récupération non autorisé des publications
* Test de récupération d'une publication
* Test de création d'une publication
* Test de suppression d'une publication
* Mise à jour d'une publication
* Tests de vote

### Section 17 : Pipeline CI/CD

* Introduction à CI/CD
* Actions GitHub
* Création de jobs
* Configuration de python/dépendances/pytest
* Variables d'environnement
* Secrets GitHub
* Base de données de test
* Construction d'images Docker
* Déploiement sur Heroku
* Tests échoués dans le pipeline
* Déploiement sur Ubuntu

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/0sOvCWFmrtA) (19 heures de visionnage).

%[https://youtu.be/0sOvCWFmrtA]