---
title: Créez des applications web sécurisées avec PHP, Symfony et MongoDB
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-09-11T13:30:55.425Z'
originalURL: https://freecodecamp.org/news/build-secure-web-applications-with-php-symfony-and-mongodb
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757573041841/0bbcb80c-76b9-4792-be3b-fba79ea344b1.png
tags:
- name: MongoDB
  slug: mongodb
- name: Symfony
  slug: symfony
- name: PHP
  slug: php
- name: youtube
  slug: youtube
seo_title: Créez des applications web sécurisées avec PHP, Symfony et MongoDB
seo_desc: 'Data breaches are a constant threat, and traditional encryption practices
  often aren''t enough to protect sensitive information throughout its entire lifecycle.

  We just posted a course on the freeCodeCamp.org YouTube channel that will teach
  you how to...'
---

Les violations de données sont une menace constante, et les pratiques de chiffrement traditionnelles ne suffisent souvent pas à protéger les informations sensibles tout au long de leur cycle de vie.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra à créer des applications véritablement sécurisées dès le départ en utilisant PHP, Symfony et MongoDB.

J'ai développé ce cours. Je vais vous apprendre à construire un système où les données sont protégées non seulement au repos et en transit, mais aussi lorsqu'elles sont utilisées.

Tout au long de ce tutoriel complet et étape par étape, vous construirez une application de finances personnelles entièrement fonctionnelle. L'application permettra aux utilisateurs de créer des comptes, d'enregistrer des transactions et de consulter leurs informations financières.

Le cœur de ce cours se concentre sur la résolution d'un défi majeur de la sécurité des applications : comment effectuer des requêtes sur des données chiffrées. Vous apprendrez à trouver un utilisateur par son numéro de sécurité sociale ou à rechercher des transactions dans une plage de montants spécifique, le tout sans jamais déchiffrer les informations sur le serveur de base de données.

J'utilise le Queryable Encryption de MongoDB pour chiffrer les données sensibles côté client. Ces données sont ensuite stockées sous forme de champs chiffrés entièrement aléatoires dans la base de données, tout en permettant l'exécution de requêtes d'égalité et de vérification de plage sur celles-ci. Le serveur n'a jamais accès aux données non chiffrées ni aux clés de chiffrement, ce qui maintient la sécurité des données tout au long de leur cycle de vie.

Ce tutoriel est conçu pour les développeurs ayant une certaine expérience de PHP et d'un Framework comme Symfony ou Laravel, mais même si vous débutez avec ces technologies, vous devriez pouvoir suivre.

Regardez le cours complet dès maintenant [sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/UuknxVdqzb4) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=UuknxVdqzb4]