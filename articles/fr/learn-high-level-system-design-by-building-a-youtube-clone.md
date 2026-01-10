---
title: Apprendre la conception de systèmes de haut niveau en créant un clone de YouTube
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-06-11T16:33:23.910Z'
originalURL: https://freecodecamp.org/news/learn-high-level-system-design-by-building-a-youtube-clone
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1718206158910/699b887d-0621-4647-a184-306ad88c55f1.png
tags:
- name: System Design
  slug: system-design
- name: React
  slug: reactjs
- name: youtube
  slug: youtube
seo_title: Apprendre la conception de systèmes de haut niveau en créant un clone de
  YouTube
seo_desc: High-Level System Design involves creating a blueprint for complex systems,
  focusing on architecture, component interactions, and scalability. It addresses
  how different parts of a system communicate, manage data, and handle user requests
  efficiently...
---

La conception de systèmes de haut niveau implique la création d'un plan pour des systèmes complexes, en se concentrant sur l'architecture, les interactions des composants et la scalabilité. Elle traite de la manière dont différentes parties d'un système communiquent, gèrent les données et traitent les requêtes des utilisateurs de manière efficace.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org sur la conception de systèmes de haut niveau. Ce cours offre une approche pratique unique pour comprendre les concepts de conception de systèmes de haut niveau (HLD) en construisant une plateforme entièrement fonctionnelle similaire à YouTube. Keerti Purswani a développé ce cours.

## Qu'est-ce que la conception de systèmes de haut niveau ?

La conception de systèmes de haut niveau implique la création d'un plan pour des systèmes complexes, en se concentrant sur l'architecture, les interactions des composants et la scalabilité. Elle traite de la manière dont différentes parties d'un système communiquent, gèrent les données et traitent les requêtes des utilisateurs de manière efficace.

## Aperçu du cours

Dans ce cours, vous commencerez par un flux de système de base et incorporerez progressivement trois services clés : **upload, watch et transcoder**. Chaque service est important pour construire une plateforme vidéo scalable et robuste. Voici un aperçu détaillé de ce que vous apprendrez :

1. **Service d'upload** : Apprenez à gérer efficacement les uploads de vidéos, y compris le découpage en morceaux et la gestion des transferts de grands fichiers.

2. **Service de transcodage** : Plongez dans le transcodage avec FFmpeg, un outil puissant pour convertir les formats vidéo et optimiser les vidéos pour différents appareils.

3. **Service de lecture** : Implémentez le streaming adaptatif avec HLS (HTTP Live Streaming) pour garantir une lecture fluide dans diverses conditions de réseau et sur différents appareils.

#### Technologies couvertes

Ce cours utilise une gamme de technologies modernes pour construire le clone de YouTube :

* **Front-end** : JavaScript et React pour créer des interfaces utilisateur dynamiques.

* **Back-end** : Node.js et Express pour construire des applications côté serveur scalables.

* **Base de données** : Prisma comme outil ORM (Object-Relational Mapping) pour interagir avec les bases de données.

* **Frameworks** : Next.js pour le rendu côté serveur et l'amélioration des performances.

* **Autres outils** : Docker pour la conteneurisation et Redis pour le caching afin d'améliorer les performances et la scalabilité.

À la fin de ce cours, vous aurez une compréhension approfondie des principes de conception de systèmes de haut niveau et une expérience pratique dans la construction d'une application complexe. Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/FiXOaYnW64w) (2 heures de visionnage).

%[https://youtu.be/FiXOaYnW64w]