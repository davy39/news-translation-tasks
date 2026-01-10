---
title: Construire un système de recommandation de livres sémantique en utilisant un
  LLM et Python
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-01-28T05:00:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-semantic-book-recommender-using-an-llm-and-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738189159544/c76e8b2c-46c2-4efd-9f4c-9891702a21b8.png
tags:
- name: llm
  slug: llm
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Construire un système de recommandation de livres sémantique en utilisant
  un LLM et Python
seo_desc: Finding your next favorite book can be a challenge, but what if you could
  build a smart system that recommends books tailored to your interests? With the
  power of large language models (LLMs) and Python, you can create an intelligent
  book recommendat...
---

Trouver votre prochain livre préféré peut être un défi, mais que se passerait-il si vous pouviez construire un système intelligent qui recommande des livres adaptés à vos intérêts ? Grâce à la puissance des grands modèles de langage (LLMs) et de Python, vous pouvez créer un moteur de recommandation de livres intelligent qui aide les lecteurs à découvrir des livres en fonction de leur contenu, de leurs thèmes et de leurs sentiments.

Nous venons de publier un cours sur la chaîne YouTube [freeCodeCamp.org](http://freeCodeCamp.org) qui vous apprendra à construire un système de recommandation de livres en utilisant des LLMs, la recherche vectorielle et Python. Tout au long de ce cours, vous apprendrez à traiter les descriptions de livres, à les convertir en représentations mathématiques (embeddings) et à utiliser des techniques de recherche avancées pour trouver des livres similaires. À la fin, vous aurez un moteur de recommandation fonctionnel avec une interface conviviale construite avec Gradio.

### Ce que vous apprendrez dans ce cours

#### **Préparation et nettoyage des données textuelles**

Avant de construire le système de recommandation, vous avez besoin d'un ensemble de données bien structuré. Le cours commence par vous apprendre à collecter et à prétraiter les descriptions de livres, à identifier et à gérer les données manquantes, et à supprimer les descriptions non pertinentes ou trop courtes pour améliorer la qualité des recommandations.

#### **Introduction aux grands modèles de langage et à la recherche vectorielle**

Vous explorerez le fonctionnement des LLMs et pourquoi ils sont utiles pour construire des moteurs de recommandation. En transformant les descriptions de livres en vecteurs numériques, vous pouvez effectuer un filtrage basé sur le contenu pour trouver des livres avec des thèmes et des styles d'écriture similaires. Vous aurez également une expérience pratique avec **LangChain**, un framework puissant pour travailler avec les LLMs et les bases de données vectorielles.

#### **Construction de la base de données vectorielle et recherche de livres similaires**

Le cœur de ce système repose sur le stockage des embeddings de livres dans une **base de données vectorielle** et l'utilisation de techniques de recherche de similarité pour trouver des livres qui correspondent à une requête donnée. Vous implémenterez la recherche vectorielle en utilisant Python et LangChain pour récupérer des recommandations de livres de manière efficace.

#### **Amélioration des recommandations avec la classification Zero-Shot et l'analyse de sentiment**

Pour rendre le système de recommandation encore plus intelligent, vous utiliserez la **classification Zero-Shot** en utilisant des LLMs pré-entraînés de **Hugging Face**. Cela vous permet de classer les livres par genres ou thèmes sans avoir besoin de données d'entraînement étiquetées. De plus, vous apprendrez à utiliser des LLMs fine-tunés pour l'**analyse de sentiment**, en extrayant les émotions des descriptions de livres pour affiner davantage les recommandations.

#### **Construction d'une interface conviviale avec Gradio**

Pour rendre le système de recommandation accessible aux utilisateurs, vous créerez un tableau de bord interactif en utilisant **Gradio**. Cela permet aux utilisateurs de saisir un titre ou une description de livre et de recevoir des recommandations personnalisées instantanément.

Prêt à construire votre propre moteur de recommandation de livres intelligent ? Consultez le [cours complet sur la chaîne YouTube de freeCodeCamp](https://youtu.be/Q7mS1VHm3Yw) (2 heures de visionnage).

%[https://youtu.be/Q7mS1VHm3Yw]