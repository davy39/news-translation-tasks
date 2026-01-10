---
title: Comment créer des workflows IA no-code avec Activepieces
author: Manish Shivanandhan
date: '2025-12-05T15:36:59.411Z'
originalURL: https://freecodecamp.org/news/how-to-build-no-code-ai-workflows-using-activepieces
description: 'L''intelligence artificielle fait désormais partie du travail quotidien
  de nombreuses équipes. On l''utilise pour rédiger du contenu, analyser des données,
  répondre aux demandes de support et orienter les décisions commerciales.

  Mais la création de workflows IA reste difficile pour beaucoup d''utilisateurs.
  La plupart des outils nécessitent du code, une configuration complexe ou une longue
  formation.

  Activepieces rend cela beaucoup plus facile. C''est un outil open source qui permet
  à n''importe qui de créer des workflows intelligents avec un constructeur visuel
  simple.'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764948981880/a78ae4ab-0430-4f37-a30a-1683e1403c0a.png
tags:
- name: AI
  slug: ai
- name: No Code
  slug: no-code
- name: Open Source
  slug: opensource
seo_desc: 'Artificial intelligence is now part of daily work for many teams. People
  use it to write content, analyse data, answer support requests, and guide business
  decisions.

  But building AI workflows is still hard for many users. Most tools need code, a
  com...'
---


L'intelligence artificielle fait désormais partie du travail quotidien de nombreuses équipes. On l'utilise pour rédiger du contenu, analyser des données, répondre aux demandes de support et orienter les décisions commerciales.

Mais la création de workflows IA reste difficile pour beaucoup d'utilisateurs. La plupart des outils nécessitent du code, une configuration complexe ou une longue formation.

Activepieces rend cela beaucoup plus facile. C'est un outil open source qui permet à n'importe qui de créer des workflows intelligents avec un constructeur visuel simple.

Vous pouvez mélanger des modèles d'IA, des sources de données et des systèmes sans écrire de code. Cela rend l'automatisation plus accessible aux équipes qui souhaitent travailler plus vite et réduire les efforts manuels.

Dans ce guide, nous allons apprendre ce qu'est Activepieces, comment travailler avec, et comment déployer notre propre version sur le cloud en utilisant Sevalla.

## Ce que nous allons aborder

* [Qu'est-ce qu'Activepieces ?](#heading-qu-est-ce-qu-activepieces)
    
* [Comprendre l'écosystème Activepieces](#heading-comprendre-l-ecosysteme-activepieces)
    
* [Créer un workflow dans Activepieces](#heading-creer-un-workflow-dans-activepieces)
    
* [Déployer ActivePieces sur le Cloud avec Sevalla](#heading-deployer-activepieces-sur-le-cloud-avec-sevalla)
    
* [Exemples concrets](#heading-exemples-concrets)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'Activepieces ?

[Activepieces](https://github.com/activepieces/activepieces) est une plateforme d'automatisation open source qui mise sur la facilité d'utilisation.

Vous pouvez l'héberger sur votre propre serveur ou l'utiliser dans le cloud. La plateforme utilise un constructeur de flux épuré où chaque bloc représente une étape. Ces blocs sont appelés des pièces (pieces).

![Mise en page d'Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683020718/b2d3f49b-8edf-435e-bbd7-4cb10dd80dbf.png align="center")

Une pièce peut appeler une API, se connecter à un outil comme Google Sheets, exécuter un modèle d'IA ou attendre une intervention humaine. En reliant les pièces entre elles, vous pouvez construire des workflows qui agissent comme des agents.

Ils peuvent écouter des événements, effectuer des analyses, créer du contenu, évaluer des données ou envoyer des résultats vers d'autres outils.

## Comprendre l'écosystème Activepieces

L'objectif principal d'Activepieces est de permettre aux utilisateurs techniques et non techniques de créer des workflows incluant de l'IA. Il offre une interface visuelle simple tout en disposant d'une couche développeur robuste sous le capot.

Les développeurs peuvent créer de nouvelles pièces en TypeScript. Ces pièces personnalisées apparaissent ensuite dans le constructeur visuel pour que tout le monde puisse les utiliser. Cela permet de garder la logique avancée invisible derrière une interface conviviale.

La plateforme dispose d'une bibliothèque croissante de plus de deux cents pièces. Beaucoup proviennent de la communauté.

![Intégrations Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683057739/69d6eb1c-b75e-4711-9d76-0638b43c242f.png align="center")

Elles incluent des outils courants comme l'e-mail, Slack, Google Workspace, OpenAI et Notion. Il existe également des pièces pour lire des liens, analyser du texte, appeler des webhooks ou attendre des événements planifiés.

La bibliothèque s'enrichit rapidement car n'importe qui peut contribuer avec de nouvelles pièces. Chaque pièce est un package npm, elle s'intègre donc parfaitement dans l'écosystème JavaScript plus large.

Activepieces prend également en charge l'intervention humaine. Par exemple, un workflow peut s'interrompre et attendre que quelqu'un révise un message avant de l'envoyer. Il peut également collecter des réponses via un formulaire.

Ces options permettent de construire des flux qui mélangent l'automatisation avec le jugement humain. C'est particulièrement utile pour les tâches où le risque ou l'exactitude sont cruciaux, comme les contrôles de conformité ou les flux d'approbation.

Une part majeure de la plateforme réside dans sa conception orientée IA. Elle inclut un support natif pour les fournisseurs d'IA populaires. Vous pouvez construire des agents qui analysent du texte, réécrivent des messages, classent du contenu, extraient des champs ou prennent des décisions.

Vous pouvez même demander à l'IA de nettoyer des données à l'intérieur d'un flux, sans avoir besoin de code. Cela facilite l'utilisation de l'IA pour accélérer le travail et supprimer les étapes répétitives.

## Créer un workflow dans Activepieces

Chaque workflow commence par un déclencheur (trigger). Un déclencheur est une action qui lance le flux.

Il peut s'agir d'un nouveau message, d'un nouveau fichier, d'une requête web ou d'une planification temporelle. Une fois le déclencheur activé, le flux s'exécute étape par étape. Chaque étape est une pièce que vous choisissez dans la bibliothèque.

Le constructeur affiche le flux dans une mise en page verticale simple. Vous pouvez ajouter des branches, des boucles, des tentatives de réexécution et du mapping de données.

![Workflow Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683082555/3a25c6b8-7454-4b2e-b421-7bbbe65212be.png align="center")

Le mapping de données est le processus consistant à indiquer au flux comment transmettre les informations d'une étape à une autre. Il utilise une interface simple où vous sélectionnez des champs des étapes précédentes pour les connecter aux nouvelles.

Lorsque des pièces d'IA sont ajoutées, le workflow devient plus puissant. Par exemple, vous pouvez transmettre le texte d'un formulaire à un modèle d'IA et obtenir un résumé.

Vous pouvez transmettre un lien vers un document et en extraire les points principaux. Vous pouvez demander à l'IA de répondre à une question ou de décider si un message correspond à une catégorie. Ces résultats passent ensuite à l'étape suivante, où ils peuvent être stockés ou envoyés.

## Déployer ActivePieces sur le Cloud avec Sevalla

Pour utiliser Activepieces, vous pouvez soit l'installer sur votre ordinateur (non recommandé en raison de la complexité de la configuration), [acheter un abonnement cloud](https://www.activepieces.com/), ou l'auto-héberger.

Si vous préférez l'installer sur votre ordinateur, [voici les instructions](https://www.activepieces.com/docs/install/options/docker).

L'auto-hébergement vous donne un contrôle total et est généralement préféré par les équipes techniques qui souhaitent conserver les données sensibles en interne.

Vous pouvez choisir n'importe quel fournisseur cloud, comme AWS, DigitalOcean ou d'autres pour configurer ActivePieces. Mais je vais utiliser Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur PaaS conçu pour les développeurs et les équipes de développement qui déploient des fonctionnalités et des mises à jour en permanence de la manière la plus efficace possible. Il propose l'hébergement d'applications, de bases de données, de stockage objet et d'hébergement de sites statiques pour vos projets.

J'utilise Sevalla pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun frais pour cet exemple.
    
* Sevalla dispose d'un [modèle pour ActivePieces](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource nécessaire à l'installation.
    

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Templates. Vous pouvez voir Activepieces parmi les modèles disponibles.

![Modèles Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683152719/dcc829e0-c06e-4e23-b118-d09a3b5cea32.png align="center")

Cliquez sur le modèle « Activepieces ». Vous verrez les ressources nécessaires pour provisionner l'application. Cliquez sur « Deploy Template ».

![Provisionnement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683186122/a6e557b8-b001-4fb3-9637-c208f8a7d81f.png align="center")

Vous pouvez voir la ressource en cours de provisionnement. Une fois le déploiement terminé, allez sur l'application Activepieces et cliquez sur « Visit app ». Entrez votre nom, e-mail et mot de passe, et vous serez redirigé vers le tableau de bord.

![Tableau de bord Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683211801/02a70ff2-7f42-4b98-8109-4acf22e690cd.png align="center")

Cliquez sur « New Flow ». Vous pouvez soit créer un flux à partir de zéro, soit choisir l'un des nombreux modèles proposés par Activepieces.

Choisissons le modèle « LinkedIn content idea generator ».

![Modèles Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683242859/1dc73871-8e16-4f0b-b535-0f781a4e5cb6.png align="center")

Cliquez sur « Use template ». Vous verrez le workflow généré pour vous. Vous pouvez également ajouter ou supprimer des composants en fonction de vos besoins.

![Workflow Activepieces](https://cdn.hashnode.com/res/hashnode/image/upload/v1764683271246/17d52f70-0d79-4