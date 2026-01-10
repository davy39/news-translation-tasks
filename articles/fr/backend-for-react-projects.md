---
title: Quel Backend Devez-Vous Utiliser pour React ?
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-22T21:04:58.000Z'
originalURL: https://freecodecamp.org/news/backend-for-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/backend-for-react.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: React
  slug: react
seo_title: Quel Backend Devez-Vous Utiliser pour React ?
seo_desc: "What backend should you choose for the React projects you are building?\
  \ \nThere are so many different options to pick from, how do you know whether the\
  \ backend you choose is the right one? \nIn this guide, you'll learn how to pick\
  \ the appropriate backe..."
---

Quel backend devez-vous choisir pour les projets React que vous construisez ?

Il existe tant d'options différentes parmi lesquelles choisir, comment savoir si le backend que vous choisissez est le bon ?

Dans ce guide, vous apprendrez à choisir le backend approprié pour le type d'application React que vous créez de la manière la plus simple et la moins coûteuse possible.

Plongeons-nous dans le sujet !

## Mon Application a-t-elle Besoin d'un Backend ?

En tant que développeurs React, la construction de notre projet se concentre largement sur ce que l'utilisateur voit, ce qui est connu sous le nom de **frontend**.

Dans chaque projet React, nous gérons les données sur le client via l'état et les interactions utilisateur. Cependant, de nombreuses applications ne sont pas possibles sans les données provenant du backend.

Le **backend** s'occupe de la récupération ou de la mise à jour des données dans notre application et est caché à l'utilisateur.

La plupart des backends se composent de deux parties :

1. Un endroit pour stocker nos données (souvent une base de données)
2. Une méthode pour récupérer les données (souvent une API)

Mais voici la bonne nouvelle : selon le type d'application que vous créez, vous n'aurez peut-être besoin ni de l'un ni de l'autre.

## Étape 1 : Pas de Backend

Si vous construisez une application où vos données changent très rarement, vous n'avez probablement pas besoin d'une base de données ou d'une API.

Par exemple, si vous construisez un blog personnel que vous mettez à jour quelques fois par semaine au mieux et qui est construit en tant que site statique utilisant Next.js ou Gatsby, vous n'avez pas besoin d'un backend.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/react-and-nextjs.jpg)
_Les sites statiques construits avec Gatsby ou Next.js n'ont peut-être pas besoin de backend_

Au lieu de cela, vous pourriez simplement écrire vos articles de blog sous forme de fichiers markdown, qui sont stockés et suivis (en utilisant Git) dans un dossier de projet.

Si vous avez une application de commerce électronique où les données des produits changent rarement, vous pourriez stocker toutes les données de l'application dans des fichiers JSON que vous importez et utilisez simplement dans votre application React.

Si vous êtes prêt à mettre à jour les fichiers manuellement et à redéployer votre projet, cela peut être tout ce dont vous avez besoin.

Le type de backend que vous choisissez dépend de certaines caractéristiques clés de vos données que vous devez vous poser :

* Mes données changent-elles souvent ?
* Suis-je prêt à gérer mes données sous forme de fichiers et dossiers locaux ?
* Les données ou fichiers de mon application peuvent-ils être suivis dans le contrôle de version (Git) ?
* D'autres personnes vont-elles mettre à jour les données ?
* Mon application aura-t-elle besoin d'authentification ?

Selon vos réponses à ces questions, vous pourriez être en mesure de vous contenter d'utiliser des fichiers statiques comme source de données.

Opter pour cette solution vous permettra finalement d'économiser beaucoup d'argent sur les coûts de base de données et d'hébergement, puisque les sites statiques peuvent être hébergés sur un niveau gratuit de nombreux fournisseurs d'hébergement.

## Étape 2 : Systèmes de Gestion de Contenu

Si vous avez besoin de plus de fonctionnalités que celles que les fichiers statiques seuls peuvent offrir, les systèmes de gestion de contenu sont l'étape suivante.

Les **systèmes de gestion de contenu** ou (CMS) nous donnent des outils pour gérer plus facilement notre contenu. Ils nous offrent souvent des applications dédiées avec des éditeurs intégrés pour visualiser, mettre à jour et structurer plus facilement nos données.

Ce dont nous avons spécifiquement besoin pour notre application React est un CMS headless.

Un **CMS headless** n'a pas d'interface visible, puisque React servira d'interface utilisateur pour notre application.

Un CMS est idéal pour votre application si vous avez simplement trop de données à gérer sous forme de fichiers séparés ou si vous souhaitez que d'autres utilisateurs potentiellement non techniques modifient ou ajoutent du contenu à votre application.

Certains des CMS les plus simples vont des feuilles de calcul de type Excel comme Google Sheets et Airtable, aux applications de prise de notes comme Notion.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/alt-cms-examples.jpg)
_Vous pouvez utiliser des outils comme Google Sheet, Airtable et Notion pour fonctionner comme le CMS de votre application_

L'avantage de ces solutions est qu'elles sont faciles à utiliser, ont un niveau gratuit généreux et ont leur propre API intégrée pour récupérer des données.

Il existe d'autres CMS qui offrent des fonctionnalités conviviales pour les développeurs telles que la gestion des images et des actifs multimédias ainsi que des fonctionnalités API plus étendues.

Certains des CMS les plus conviviaux pour les développeurs incluent :

* Sanity
* GraphCMS
* Contentful

![Image](https://www.freecodecamp.org/news/content/images/2024/08/sanity-graph-cms-contentful.jpg)
_Sanity, GraphCMS et Contentful sont des CMS plus puissants et conviviaux pour les développeurs_

Et si vous cherchez des systèmes de gestion de contenu qui sont les plus puissants, avec des fonctionnalités comme l'authentification intégrée et la mise à jour des données depuis votre client React, consultez :

* Strapi
* KeystoneJS

![Image](https://www.freecodecamp.org/news/content/images/2024/08/strapi-keystonejs.jpg)
_Voulez-vous un CMS qui est essentiellement un backend complet ? Consultez Strapi ou KeystoneJS_

## Étape 3 : Backend en tant que Service

La limitation avec les systèmes de gestion de contenu est qu'ils sont excellents pour gérer et accéder aux données.

Cependant, lorsque vous devez ajouter des fonctionnalités plus complexes et personnalisées telles que la mise à jour des données depuis votre client React, l'authentification des utilisateurs, la protection du contenu et les données en temps réel, un CMS standard est insuffisant.

Gérer une base de données et construire une API complète pour interagir avec cette base de données est un défi intimidant, surtout si vous n'avez travaillé que sur le frontend.

Si c'est votre cas, il peut être intéressant de se tourner vers un **backend en tant que service** (BaaS). Il vous donnera une grande partie de la puissance d'un backend personnalisé sans les connaissances spécifiques au domaine.

Le BaaS le plus populaire est **Firebase**, et pour de bonnes raisons. Il vous offre une tonne de fonctionnalités que vous ne pourriez tout simplement pas construire vous-même, y compris des dizaines de stratégies d'authentification, des bases de données NoSQL en temps réel, du stockage cloud, des outils de machine learning, et bien plus encore.

Il existe de nombreux autres BaaS qui vous offrent la productivité de Firebase, avec peu ou pas de code requis :

* Supabase
* Hasura
* Appwrite

![Image](https://www.freecodecamp.org/news/content/images/2024/08/firebase-supabase-hasura.jpg)
_Firebase, Supabase et Hasura sont tous d'excellents backends à utiliser si vous n'êtes pas à l'aise de construire le vôtre_

**Avertissement** : La vitesse de développement pour tous ces services peut vous aider à construire et à livrer vos applications plus rapidement. Mais soyez conscient que tous ont leurs propres coûts associés, tels que le stockage cloud que vous utilisez et le nombre d'opérations de base de données que vous effectuez (lectures/écritures).

## Étape 4 : Construisez Votre Propre Backend

Avant de considérer cette étape, vous devriez examiner attentivement si vous pourriez potentiellement utiliser les options 1 à 3.

Il s'agit de l'option la plus avancée à choisir en tant que développeur React car elle nécessite le plus de connaissances, de temps et de compétences en codage.

Cela dit, c'est aussi la plus personnalisable, puisque vous pouvez construire exactement ce dont vous avez besoin pour alimenter votre application.

Des livres entiers ont été écrits sur des parties spécifiques de la construction de votre propre backend, mais voici ce que je recommanderais en tant que personne ayant construit de nombreuses applications de production utilisant un backend personnalisé.

Je recommande d'utiliser une **base de données SQL** telle que Postgres ou MySQL. Des services tels que Heroku, Render.com et PlanetScale offrent des bases de données hébergées (souvent avec des sauvegardes gratuites quotidiennes) à des prix intéressants.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/heroku-render-planetscale.jpg)
_Heroku, Render.com et PlanetScale sont parmi les meilleurs endroits pour héberger votre base de données_

Sauf si vous êtes très à l'aise et confiant pour écrire des instructions SQL brutes et connaissez toutes les précautions de sécurité à prendre pour éviter des choses désagréables comme l'injection SQL, utilisez un **mappage objet-relationnel** (un ORM) pour créer un schéma de base de données et interagir avec lui.

Je recommande vivement d'utiliser **Prisma** comme ORM. Il génère tout le code nécessaire pour effectuer chaque type d'opération contre votre base de données ainsi que les types pour chacun.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-22-at-1.31.43-PM.png)
_Utilisez Prisma comme ORM_

Bien que vous puissiez certainement construire un backend Node personnalisé en utilisant votre bibliothèque ou framework Node préféré (Express, Fastify, Nest.js), je vous conseillerais de commencer petit et d'utiliser une fonctionnalité comme les routes API de Next.js.

Des outils comme les routes API de Next vous permettent de construire votre API rapidement sans avoir besoin d'exécuter et de gérer votre code serveur dans un dépôt séparé.

## Devenez un Développeur React Professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*