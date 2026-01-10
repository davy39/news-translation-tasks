---
title: Cours sur l'ajustement fin des modèles LLM
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-05-21T16:22:01.246Z'
originalURL: https://freecodecamp.org/news/fine-tuning-llm-models-course
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1716308506161/f7e61904-4b87-4578-a04b-e60b6221a1df.png
tags:
- name: finetuning
  slug: finetuning
- name: youtube
  slug: youtube
seo_title: Cours sur l'ajustement fin des modèles LLM
seo_desc: Fine-tuning is a process in machine learning that allows you to adapt pre-trained
  models to specific tasks or datasets, enhancing their performance and usability.
  We just posted a comprehensive course on the freeCodeCamp.org YouTube channel that
  will...
---

L'ajustement fin est un processus en apprentissage automatique qui permet d'adapter des modèles pré-entraînés à des tâches ou des ensembles de données spécifiques, améliorant ainsi leurs performances et leur utilité. Nous venons de publier un cours complet sur la chaîne YouTube [freeCodeCamp.org](http://freeCodeCamp.org) qui vous apprendra tout ce que vous devez savoir sur l'ajustement fin des grands modèles de langage (LLM). Krish Naik a développé ce cours. Krish est un développeur et instructeur expérimenté.

Dans ce cours, vous apprendrez l'ajustement fin en utilisant QLORA et LORA, ainsi que les techniques de quantification avec LLama2, Gradient et le modèle Google Gemma. Décomposons ce que signifient ces termes et ce que vous apprendrez dans chaque section :

* **QLORA (Quantized Low-Rank Adaptation)** : QLORA est une technique qui combine la quantification et l'adaptation de faible rang. La quantification réduit la précision des poids du modèle, ce qui peut réduire significativement la taille du modèle et accélérer les calculs. L'adaptation de faible rang implique l'ajustement d'un petit nombre de paramètres dans le modèle, rendant l'ajustement fin plus efficace et moins gourmand en ressources.

* **LORA (Low-Rank Adaptation)** : Similaire à QLORA mais sans quantification, LORA se concentre sur l'adaptation d'un petit sous-ensemble des paramètres du modèle. Cela en fait une approche légère et efficace pour l'ajustement fin de grands modèles sur des tâches spécifiques.

* **Quantification avec LLama2** : La quantification est une technique utilisée pour compresser les modèles en réduisant le nombre de bits nécessaires pour représenter chaque paramètre. LLama2 est un framework qui aide à implémenter la quantification, facilitant le déploiement de modèles sur des appareils avec des ressources computationnelles limitées tout en maintenant les performances.

* **Gradient** : Cela fait référence aux méthodes d'optimisation basées sur le gradient utilisées lors de l'ajustement fin. Comprendre les gradients est crucial pour l'entraînement des modèles d'apprentissage automatique, car les gradients indiquent la direction dans laquelle les paramètres du modèle doivent être ajustés pour minimiser l'erreur.

* **Modèle Google Gemma** : Le modèle Google Gemma est un framework avancé qui intègre diverses techniques pour l'optimisation et l'ajustement fin des modèles. Vous apprendrez comment tirer parti de ses fonctionnalités pour améliorer les performances de vos modèles ajustés.

Voici les sections de ce cours :

* **Introduction** : Commencez par un aperçu du cours et de ses objectifs. Comprenez l'importance de l'ajustement fin dans le contexte des grands modèles de langage et obtenez un aperçu de ce que vous accomplirez à la fin du cours.

* **Intuition de la quantification** : Plongez dans le concept de quantification. Apprenez comment la quantification aide à optimiser les modèles en réduisant leur taille et leurs exigences computationnelles sans compromettre significativement les performances.

* **Intuition approfondie de LORA et QLORA** : Explorez les mécanismes approfondis de LORA (Low-Rank Adaptation) et QLORA (Quantized Low-Rank Adaptation). Comprenez comment ces techniques améliorent l'efficacité de l'ajustement fin en adaptant un petit nombre de paramètres.

* **Ajustement fin avec LLama2** : Apprenez à ajuster finement les modèles en utilisant LLama2. Cette section inclut des étapes pratiques et des conseils pour implémenter l'ajustement fin avec cet outil puissant.

* **Intuition approfondie des LLM 1-bit** : Obtenez des informations sur les LLM 1-bit (Large Language Models). Comprenez comment cette approche simplifie les calculs des modèles et aide à un ajustement fin efficace.

* **Ajustement fin avec les modèles Google Gemma** : Découvrez comment ajuster finement les modèles en utilisant Google Gemma. Cette section fournit un guide complet pour tirer parti des capacités de Google Gemma pour l'ajustement fin des grands modèles de langage.

* **Construction de pipelines LLM sans code** : Apprenez à construire des pipelines LLM sans écrire de code. Cette section est idéale pour ceux qui préfèrent une approche sans code pour construire et gérer des pipelines d'ajustement fin.

* **Ajustement fin avec vos propres données personnalisées** : Comprenez comment ajuster finement les modèles en utilisant vos propres données personnalisées. Cette section pratique vous guidera à travers les étapes de préparation et d'utilisation de vos données pour un ajustement fin efficace.

Ce cours est parfait pour toute personne intéressée à approfondir sa compréhension de l'apprentissage automatique et de l'intelligence artificielle. Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=iOdFUJiB0Zc) (3 heures de visionnage).

%[https://www.youtube.com/watch?v=iOdFUJiB0Zc]