---
title: Apprendre le RAG à partir de zéro – Tutoriel Python IA d'un ingénieur LangChain
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-04-17T17:33:58.322Z'
originalURL: https://freecodecamp.org/news/mastering-rag-from-scratch
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1713375208533/25d36579-4e59-4a7f-b63e-a67ec6de69b8.jpeg
tags:
- name: 'RAG '
  slug: rag
- name: youtube
  slug: youtube
seo_title: Apprendre le RAG à partir de zéro – Tutoriel Python IA d'un ingénieur LangChain
seo_desc: Retrieval-Augmented Generation (RAG) can be extremely helpful when developing
  projects with Large Language Models. It combines the power of retrieval systems
  with advanced natural language generation, providing a sophisticated approach to
  generating ...
---

La génération augmentée par récupération (RAG) peut être extrêmement utile lors du développement de projets avec des grands modèles de langage. Elle combine la puissance des systèmes de récupération avec la génération avancée de langage naturel, offrant une approche sophistiquée pour générer des réponses précises et riches en contexte.

Nous venons de publier un cours approfondi sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à implémenter le RAG à partir de zéro. Lance Martin a créé ce cours. Il est ingénieur logiciel chez LangChain et possède un doctorat en apprentissage automatique appliqué de Stanford.

## Qu'est-ce que le RAG ?

La génération augmentée par récupération (RAG) est un framework puissant qui intègre la récupération dans le processus de génération de séquences. Essentiellement, le RAG fonctionne en récupérant des documents ou des extraits de données pertinents en fonction d'une requête, puis utilise ces informations récupérées pour générer une réponse cohérente et contextuellement appropriée. Cette méthode est particulièrement précieuse dans des domaines comme le développement de chatbots, où la capacité à fournir des réponses précises dérivées de vastes bases de données de connaissances est cruciale.

Le RAG améliore fondamentalement les capacités de compréhension et de génération de langage naturel des modèles en leur permettant d'accéder et d'exploiter une grande quantité de connaissances externes. L'approche repose sur la synergie entre deux composants principaux : un système de récupération et un modèle génératif. Le système de récupération identifie d'abord les informations pertinentes dans une base de connaissances, que le modèle génératif utilise ensuite pour élaborer des réponses non seulement précises, mais aussi riches en détails et en portée.

![Diagramme RAG](https://cdn.hashnode.com/res/hashnode/image/upload/v1713375387925/9246942a-79e4-4d94-b032-a85f10480a99.png align="center")

## Décomposition du cours

Le cours de Lance Martin couvre méticuleusement tous les aspects du RAG, en commençant par un aperçu qui prépare le terrain pour une exploration plus approfondie. Le cours est structuré pour guider les étudiants à travers l'ensemble du processus de mise en œuvre d'un système RAG à partir de zéro :

* **Indexation** : Les apprenants commenceront par comprendre comment créer des systèmes d'indexation efficaces pour stocker et récupérer des données, ce qui est fondamental pour tout modèle basé sur la récupération.

* **Récupération** : Cette section plonge dans les mécanismes de récupération des documents les plus pertinents en réponse à une requête.

* **Génération** : Après la récupération, l'accent est mis sur la génération de texte cohérent à partir des données récupérées, en utilisant des techniques avancées de traitement du langage naturel.

* **Traduction de requêtes** : Plusieurs stratégies pour traduire et affiner les requêtes sont discutées, y compris les techniques Multi-Query, RAG Fusion, Décomposition, Step Back et les approches HyDE, chacune offrant des avantages uniques en fonction de l'application.

* **Routing, Construction de requêtes et Techniques d'indexation avancées** : Ces segments explorent des éléments plus sophistiqués des systèmes RAG, tels que le routage des requêtes vers des modèles appropriés, la construction de requêtes efficaces et des techniques d'indexation avancées comme RAPTOR et ColBERT.

* **CRAG et Adaptive RAG** : Le cours introduit également le CRAG (Conditional RAG) et l'Adaptive RAG, des améliorations qui offrent encore plus de flexibilité et de puissance au framework RAG standard.

* **Le RAG est-il vraiment mort ?** : Enfin, une discussion sur la pertinence actuelle et future du RAG dans la recherche et les applications pratiques, stimulant la pensée critique et l'exploration au-delà du cours.

Chaque section est remplie d'exercices pratiques, d'exemples concrets et d'explications détaillées qui garantissent que les étudiants non seulement apprennent la théorie, mais appliquent également les concepts dans des contextes pratiques.

Ce cours est idéal pour les ingénieurs logiciels, les scientifiques des données et les chercheurs ayant une solide formation en apprentissage automatique et en traitement du langage naturel qui cherchent à élargir leur expertise dans les techniques avancées d'IA.

Regardez le cours complet [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/sVcwVQRHIc8) (2,5 heures de visionnage).

%[https://youtu.be/sVcwVQRHIc8]