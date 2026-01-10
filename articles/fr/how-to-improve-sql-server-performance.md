---
title: Comment améliorer les performances de SQL Server
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-05-17T17:49:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-sql-server-performance
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/sqlserver.png
tags:
- name: SQL
  slug: sql
- name: youtube
  slug: youtube
seo_title: Comment améliorer les performances de SQL Server
seo_desc: 'SQL server performance can be tricky. But there are a lot of things you
  can do to increase the speed of your queries.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to improve performance on SQL Server.

  Raj...'
---

Les performances du serveur SQL peuvent être délicates. Mais il existe de nombreuses choses que vous pouvez faire pour augmenter la vitesse de vos requêtes.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à améliorer les performances de SQL Server.

Rajan Arora a développé ce cours. Rajan est un développeur très expérimenté et un excellent enseignant.

Dans ce cours, vous verrez comment diagnostiquer ce qui se passe avec une instruction SQL lente et quelles stratégies sont disponibles pour rendre ces instructions plus rapides.

Tout d'abord, vous apprendrez comment les développeurs doivent utiliser les index de base de données dans leur base de données, y compris quelles colonnes doivent être indexées et comment s'assurer qu'une instruction SQL utilisera un index.

Ensuite, vous passerez en revue comment certains outils de diagnostic intégrés dans SQL Server peuvent vous aider à trouver les problèmes de performance dans votre application, y compris comment identifier les instructions SQL les plus lentes dans votre application.

Puis, vous verrez comment tracer toutes les instructions SQL que votre application génère dans SQL Server et comment comprendre ces données.

Enfin, vous examinerez les pratiques que vous pouvez mettre en œuvre dans votre application pour garantir les meilleures performances possibles.

À la fin de ce cours, en tant que développeur d'applications, vous aurez les outils nécessaires pour résoudre les problèmes de performance que vous pourriez rencontrer lors de l'utilisation de SQL Server.

Voici les sections de ce cours.

### Installation

* 1.1 Introduction au cours
* 1.2 Pourquoi les développeurs doivent comprendre les performances SQL
* 1.3 Outils dont vous avez besoin
* 1.4 Restaurer la base de données d'exemple
* 1.5 Concept de table
* 1.6 Concept d'index
* 1.7 Résumé

### Analyse des instructions SQL pour les performances

* 2.1 Introduction
* 2.2 Comprendre comment SQL Server exécutera une instruction SQL
* 2.3 Lecture et interprétation d'un plan d'exécution pour une instruction SQL
* 2.4 Obtention des statistiques d'exécution pour une instruction SQL
* 2.5 Amélioration des performances des instructions en ajoutant un index
* 2.6 Réécriture des instructions SQL pour améliorer les performances
* 2.7 Opérations courantes du plan d'exécution
* 2.8 Résumé

### Construction d'index

* 3.1 Introduction
* 3.2 Rappel de la terminologie des index
* 3.3 Que dois-je indexer dans ma base de données ?
* 3.4 Pourquoi l'ordre des colonnes d'index est important
* 3.5 Sélectivité des index expliquée
* 3.6 Clauses LIKE et sélectivité des index
* 3.7 Comment les fonctions dans la clause WHERE affectent les index
* 3.8 Colonnes incluses et index couvrant
* 3.9 Sur-indexation
* 3.10 Interprétation des recommandations d'index de SQL Server
* 3.11 Résumé

### Trouver les goulots d'étranglement dans les performances de SQL Server

* 4.1 Introduction
* 4.2 Obtention d'informations sur les sessions SQL Server et l'utilisation des ressources
* 4.3 Trouver quelles instructions SQL sont actuellement en cours d'exécution
* 4.4 Trouver les instructions SQL les plus lentes et les plus coûteuses
* 4.5 Obtention des recommandations de SQL Server sur les index manquants
* 4.6 Trouver les index qui ne sont pas utilisés
* 4.7 Résumé

### Capture des journaux de trace de l'application à partir de SQL Server

* 5.1 Introduction
* 5.2 Configuration d'une trace SQL Profiler
* 5.3 Exécution d'une trace SQL Profiler
* 5.4 Exécution d'une trace en tant que trace côté serveur
* 5.5 Introduction à l'utilisation des événements étendus pour le traçage SQL
* 5.6 Configuration d'une session de trace d'événements étendus
* 5.7 Exécution et configuration des paramètres d'affichage pour une trace d'événements étendus
* 5.8 Analyse des données de trace des événements étendus
* 5.9 Utilisation des événements étendus dans SQL Azure
* 5.10 Résumé

### Appliquer les pratiques courantes pour de meilleures performances

* 6.1 Introduction
* 6.2 Utiliser SQL paramétré
* 6.3 Les procédures stockées sont-elles plus rapides que le SQL dans le code de l'application ?
* 6.4 Comportement de validation et performance
* 6.5 Les mappers relationnels d'objets génèrent simplement du SQL
* 6.6 Résolution du problème des sélections N+1
* 6.7 Résumé

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=HvxmF0FUwrM).

%[https://www.youtube.com/watch?v=HvxmF0FUwrM]