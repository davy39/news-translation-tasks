---
title: Comment fonctionne un MCP sous le capot ? Le flux de travail MCP expliqué
author: Ajay Patel
date: '2025-12-16T18:35:11.600Z'
originalURL: https://freecodecamp.org/news/how-does-an-mcp-work-under-the-hood
description: 'Nous avons tous été confrontés à cette limitation gênante de l''IA :
  elle peut écrire du code ou expliquer des sujets complexes en quelques secondes,
  mais dès que vous lui demandez de vérifier un fichier local ou d''exécuter une requête
  de base de données rapide, elle se heurte à un mur. C''est comme avoir un assistant
  génial enfermé...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765909617721/fa533504-3dab-48c3-9b92-0b89a81af025.png
tags:
- name: mcp
  slug: mcp
- name: Model Context Protocol
  slug: model-context-protocol
- name: AI
  slug: ai
seo_desc: Understand how MCP enables AI to interact with external systems, enhancing
  capabilities beyond initial training limits.
---


Nous avons tous été confrontés à cette limitation gênante de l'IA : elle peut écrire du code ou expliquer des sujets complexes en quelques secondes, mais dès que vous lui demandez de vérifier un fichier local ou d'exécuter une requête de base de données rapide, elle se heurte à un mur. C'est comme avoir un assistant génial enfermé dans une pièce vide — intelligent, mais complètement coupé de votre travail réel. C'est là que le Model Context Protocol (MCP) change la donne. Dans cet article, nous explorerons le MCP en profondeur.

## Table des matières

* [Serveur MCP : l'A à Z du Model Context Protocol](#heading-serveur-mcp-l-a-a-z-du-model-context-protocol)
    
* [Qu'est-ce que le MCP (Model Context Protocol) ?](#heading-qu-est-ce-que-le-mcp-model-context-protocol)
    
* [Architecture du MCP](#heading-architecture-du-mcp)
    
* [Comment fonctionne le MCP ?](#heading-comment-fonctionne-le-mcp)
    
* [MCP vs RAG](#heading-mcp-vs-rag)
    
* [MCP vs A2A](#heading-mcp-vs-a2a)
    
* [Ressources](#heading-ressources)
    
* [Conclusion](#heading-conclusion)
    

## Serveur MCP : l'A à Z du Model Context Protocol

Les LLM possèdent des connaissances et des capacités de raisonnement impressionnantes, ce qui leur permet d'accomplir de nombreuses tâches complexes. Mais le problème est que leurs connaissances sont limitées à leurs données d'entraînement initiales. Cela signifie qu'ils ne peuvent pas accéder à votre calendrier, exécuter des requêtes SQL ou envoyer un e-mail.

Il était clair que, pour donner aux LLM une connaissance du monde réel, nous devions fournir des intégrations leur permettant d'accéder à des informations en temps réel ou d'effectuer des actions dans le monde réel. Cela mène au problème classique MxN, où les développeurs doivent construire et maintenir des intégrations personnalisées pour chaque combinaison de M modèles et N outils.

L'image ci-dessous démontre bien le problème MxN :

![problème mxn - connecter chaque modèle à chaque outil individuellement](https://cdn.hashnode.com/res/hashnode/image/upload/v1764841852514/f4279e47-416d-4559-8908-16199eab3820.jpeg align="center")

Le function calling (également connu sous le nom d'appel d'outils) offre un moyen puissant et flexible pour les modèles d'OpenAI de s'interfacer avec des systèmes externes et d'accéder à des données en dehors de leurs données d'entraînement. Cependant, cette fonctionnalité est actuellement exclusive aux modèles d'OpenAI, créant un vendor lock-in.

C'est là que le MCP intervient. Le MCP est une approche « écrire une fois, utiliser partout » pour résoudre ce problème. Un développeur d'application peut écrire un seul serveur MCP pour n'importe quel système d'IA et exposer un ensemble d'outils et de données. De même, un système d'IA peut implémenter le protocole et se connecter à n'importe quel serveur MCP existant aujourd'hui ou à l'avenir.

## Qu'est-ce que le MCP (Model Context Protocol) ?

Le MCP est un standard open-source, développé par Anthropic, pour connecter les applications d'IA à des systèmes externes.

En utilisant un MCP, les applications d'IA comme Claude ou ChatGPT peuvent se connecter à des sources de données telles que des fichiers locaux et des bases de données, des outils comme des moteurs de recherche et des calculatrices, et des flux de travail comme des prompts spécialisés — leur permettant d'accéder à des informations clés et d'accomplir des tâches.

Pensez au MCP comme à un port USB-C pour les applications d'IA. Tout comme l'USB-C fournit un moyen standardisé de connecter des appareils électroniques, un MCP fournit un moyen standardisé de connecter des applications d'IA à des systèmes externes.

L'image ci-dessous vous aidera à mieux comprendre le serveur MCP :

![structure du model context protocol](https://cdn.hashnode.com/res/hashnode/image/upload/v1764763126029/45a8d0a7-a4f4-47e4-afb9-268930bd1c47.png align="center")

## Architecture du MCP

Le Model Context Protocol a une structure claire avec des composants qui travaillent ensemble pour aider les LLM et les systèmes externes à interagir facilement. Un MCP suit une architecture client-serveur simple, qui peut être décomposée en trois composants clés :

### **Hôte MCP**

L'hôte est l'application d'IA orientée utilisateur, l'environnement où le modèle d'IA réside et interagit avec l'utilisateur. Les hôtes gèrent la découverte, les permissions et la communication entre les clients et les serveurs. Il peut s'agir d'une application de chat comme l'interface ChatGPT d'OpenAI ou l'application de bureau Claude d'Anthropic, ou d'un IDE enrichi par l'IA comme Cursor et Windsurf.

### **Client MCP**

Le client MCP est un composant au sein de l'hôte qui gère la communication de bas niveau avec le serveur MCP. Les clients MCP sont instanciés par les applications hôtes pour communiquer avec des serveurs MCP particuliers. Chaque client gère une communication directe avec un serveur.

Ici, la différence est importante : l'hôte est l'application avec laquelle les utilisateurs interagissent, tandis que les clients sont les composants qui permettent les connexions aux serveurs.

### **Serveur MCP**

Le serveur MCP est le programme ou service externe qui expose les capacités (outils, données, etc.) à l'application. Un serveur MCP peut être vu comme une enveloppe autour d'une fonctionnalité, qui expose un ensemble d'outils ou de ressources de manière standardisée afin que n'importe quel client MCP puisse les invoquer.

Les serveurs peuvent s'exécuter localement sur la même machine que l'hôte, ou à distance sur un service cloud, car le MCP est conçu pour prendre en charge les deux scénarios de manière transparente.

L'image ci-dessous vous aidera à mieux comprendre le concept :

![comment fonctionne le mcp](https://cdn.hashnode.com/res/hashnode/image/upload/v1764841995822/fdec43d4-705e-4385-8eac-b436ec22c386.jpeg align="center")

Un serveur MCP peut exposer une ou plusieurs capacités au client. Les capacités sont essentiellement les fonctionnalités ou fonctions que le serveur met à disposition.

Le serveur MCP fournit les capacités suivantes :

* **Outils (Tools) :** Les outils sont les fonctions qui effectuent une action au nom du modèle d'IA. Une IA peut utiliser cet outil chaque fois que nécessaire. Les outils sont déclenchés par le choix du modèle d'IA, ce qui signifie que le LLM (via l'hôte) décide d'appeler un outil lorsqu'il détermine qu'il doit effectuer une tâche spécifique. Par exemple : `send_email` -> envoyer l'e-mail à l'utilisateur.
    
* **Ressources (Resources) :** Les ressources fournissent des données en lecture seule au modèle d'IA. Une ressource peut être un enregistrement de base de données ou une base de connaissances que l'IA peut interroger pour obtenir des informations, mais ne peut pas modifier.
    
* **Prompts :** Les prompts sont des modèles prédéfinis ou des flux de travail que le serveur peut fournir.
    

### **Couche de transport**

La couche de transport utilise des messages JSON-RPC 2.0 pour communiquer entre le client et le serveur. Pour cela, nous avons principalement deux méthodes de transport :

* **Entrée/Sortie standard (stdio) :** Idéal pour les environnements locaux, offrant une transmission de messages rapide et synchrone.
    
* **Événements envoyés par le serveur (SSE) :** Le mieux adapté pour les ressources distantes, permettant un streaming de données unidirectionnel efficace et en temps réel du serveur vers le client.
    

## Comment fonctionne le MCP ?

Un MCP donne à un assistant d'IA la capacité d'utiliser en toute sécurité des outils, des bases de données et des services externes. Imaginez que vous demandiez à Claude :

> « Trouve le dernier rapport de ventes dans notre base de données et envoie-le par e-mail à mon manager. »

### **Étape #1 - Découverte d'outils**

Lorsque nous lançons un client MCP (Claude Desktop), il se connecte à vos serveurs MCP configurés et demande : « Que puis-je faire avec les outils disponibles ? »

Chaque serveur répond avec ses outils disponibles :

`database_query`, `email_sender`, `file_browser`

Désormais, Claude connaît les outils dont il dispose.

### **Étape #2 - Compréhension de votre besoin**

Claude lit votre requête et réalise :

* Il doit récupérer des informations qu'il n'a pas (dans ce cas, il doit trouver les données de vente via `database_query`).
    
* Il doit effectuer une action externe (envoyer un e-mail via `email_sender`).
    

Claude planifie donc une séquence d'outils en 2 étapes.

### **Étape #3 - Demande de permission**

Avant qu'une action externe ne se produise, Claude Desktop vous demande : « Claude veut interroger votre base de données de ventes. Autoriser ? »

Rien ne se passe sans votre approbation. C'est le cœur du modèle de sécurité du MCP.

### **Étape #4 - Interrogation de la base de données**

Une fois que vous avez accordé la permission, Claude envoie un appel d'outil MCP structuré au serveur `database_query`.

Ensuite, le serveur effectuera une recherche sécurisée dans la base de données et renverra les données du dernier rapport de ventes. Cela ne donne pas à Claude un accès direct à la base de données.

### **Étape #5 - Envoi de l'e-mail**

Une fois que Claude a les données, il déclenche une deuxième demande de permission : « Claude veut envoyer un e-mail en votre nom. Approuver ? »

Une fois approuvé, le MCP envoie les informations au serveur `email_sender`, et Claude formatera l'e-mail et le livrera à votre manager.

### **Étape #6 - Réponse naturelle**

Claude finalise le tout proprement et vous envoie une réponse : « C'est fait ! J'ai trouvé le