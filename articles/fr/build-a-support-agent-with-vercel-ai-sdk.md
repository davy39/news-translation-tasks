---
title: Créer un agent de support avec le Vercel AI SDK
author: Beau Carnes
date: '2025-12-23T16:34:48.007Z'
originalURL: https://freecodecamp.org/news/build-a-support-agent-with-vercel-ai-sdk
description: 'Le Vercel AI SDK est une boîte à outils orientée TypeScript pour créer
  des fonctionnalités d''IA. Il simplifie la génération de texte, les embeddings et
  les sorties structurées.

  Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous
  apprendra à utiliser le Vercel AI SDK pour...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766507669760/bf3fe42c-d729-4b59-9eca-2677e1b49e2a.jpeg
tags:
- name: Vercel
  slug: vercel
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_desc: 'Vercel AI SDK is a TypeScript-first toolkit for building AI features. It
  streamlines text generation, embeddings, and structured outputs.

  We just posted a course on the freeCodeCamp.org YouTube channel that will teach
  you to use the Vercel AI SDK to ...'
---


Le Vercel AI SDK est une boîte à outils orientée TypeScript pour créer des fonctionnalités d'IA. Il simplifie la génération de texte, les embeddings et les sorties structurées.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra à utiliser le Vercel AI SDK pour créer et déployer un agent de support client capable de prendre des décisions autonomes pour soit répondre aux questions basées sur votre documentation de support, soit effectuer des recherches sur le web en temps réel.

Dans ce cours, vous allez déployer un agent de support client qui :

* Intègre les documents de support dans un vector store Supabase.
    
* Utilise la récupération (retrieval) et la recherche web comme outils, sélectionnés à la volée en fonction de la question de l'utilisateur.
    
* Classifie les intentions avec des sorties structurées (via `generateObject` + `Zod`).
    
* Répond aux questions avec des réponses fondées et fiables — en s'appuyant sur vos documents lorsque c'est pertinent ou en effectuant des recherches sur le web en temps réel si nécessaire.
    

Le cours couvre les sujets suivants :

* Expliquer le RAG et les embeddings et décider quand utiliser chacun d'eux.
    
* Configurer Supabase comme vector store : créer des tables, intégrer des documents et gérer le chunking/découpage de texte pour les fichiers volumineux.
    
* Implémenter la récupération avec Supabase RPC afin que votre agent puisse récupérer le bon contexte pour n'importe quelle question.
    
* Utiliser les bases du Vercel AI SDK : embeddings et `generateText` pour des appels de modèles rapides et fiables.
    
* Produire des sorties structurées avec `generateObject` et `Zod` pour valider et router les intentions.
    
* Appeler des outils avec l'AI SDK — définir des schémas, câbler l'exécution et maintenir la sécurité des types (type-safe).
    
* Traiter la récupération et la recherche web comme des outils, et les composer dans un flux de décision unique pour l'agent.
    
* Utiliser l'outil de recherche web d'OpenAI pour extraire des informations fraîches en temps réel lorsque vos documents ne suffisent pas.
    
* Combiner le tout dans un agent de support qui choisit la meilleure stratégie (récupération, recherche ou réponse directe) et explique ses réponses.
    

Regardez le cours complet [sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/WKIjkxxNH0c) (durée : 2 heures).

%[https://youtu.be/WKIjkxxNH0c]