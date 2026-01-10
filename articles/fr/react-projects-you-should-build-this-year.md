---
title: 7 projets React que vous devriez réaliser en 2021
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-22T17:04:07.000Z'
originalURL: https://freecodecamp.org/news/react-projects-you-should-build-this-year
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/7-react-projects-for-2021-2.png
tags:
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: React
  slug: react
- name: side project
  slug: side-project
seo_title: 7 projets React que vous devriez réaliser en 2021
seo_desc: 'React is a JavaScript library that is ideal for creating impressive apps.
  There are countless projects that you can make with React, but here are seven that
  are on my list to build in 2021.

  Why have I selected these seven projects in particular? I pi...'
---

React est une bibliothèque JavaScript idéale pour créer des applications impressionnantes. Il existe d'innombrables projets que vous pouvez réaliser avec React, mais en voici sept que j'ai sur ma liste à réaliser en 2021.

_Pourquoi ai-je sélectionné ces sept projets en particulier ?_ Je les ai choisis parce qu'ils s'appuient les uns sur les autres. Ils nécessitent que vous connaissiez des concepts similaires et essentiels comme l'authentification, le travail avec une API et une base de données, l'utilisation d'un routeur React pour ajouter des pages à votre application, et la lecture de médias comme l'audio ou la vidéo. 

De plus, de nombreuses applications peuvent être (et sont souvent) intégrées les unes aux autres. Les applications de médias sociaux peuvent inclure des applications de chat, les applications de musique ou de vidéo peuvent inclure des applications de commerce électronique, et ainsi de suite.

En d'autres termes, **la réalisation de l'un de ces projets** vous donnera les compétences et les connaissances nécessaires pour réaliser le reste des applications de la liste, y compris vos propres projets personnels.

Pour chaque projet, j'ai fourni plusieurs exemples concrets que vous pouvez utiliser pour trouver de l'inspiration, ainsi que quelques idées sur les outils que j'utiliserais éventuellement pour construire chaque application.

## 1. Application de chat en temps réel

**Exemples concrets** : Slack, Messenger, Discord, Crisp Chat

Presque tous nous utilisons une sorte d'application de chat en temps réel, qu'il s'agisse d'une application mobile comme WhatsApp ou Viber ou d'un outil de productivité comme Slack ou Discord. Cela peut également faire partie d'un widget de chat dans un site web où les clients peuvent parler directement avec les propriétaires du site. 

Toutes les applications de chat permettent aux utilisateurs d'envoyer des messages à d'autres en temps réel, de réagir aux messages, et elles montrent quand les utilisateurs sont en ligne ou hors ligne. 

### Comment construire une application de chat en temps réel : 

* Construisez votre projet avec create-react-app ou Next.js. 
* Utilisez un service comme Firebase ou les abonnements GraphQL pour créer et obtenir des messages en temps réel pour les utilisateurs.
* Ajoutez des réactions aux messages avec des emojis en utilisant le package npm emoji-mart
* Déployez sur le web en utilisant Firebase Tools

## 2. Application de médias sociaux

**Exemples concrets** : Facebook, Twitter, Instagram

L'application que vous connaissez probablement le mieux est une application de médias sociaux. À bien des égards, elle est similaire à une application de chat, mais étendue à une communauté plus large d'utilisateurs. 

Ces utilisateurs peuvent interagir les uns avec les autres de différentes manières : ils peuvent se suivre pour recevoir leurs publications, ajouter des médias comme des images et des vidéos à partager avec d'autres, et permettre aux utilisateurs d'interagir avec les publications, comme les aimer ou les commenter.

### Comment construire une application de médias sociaux : 

* Construisez votre frontend avec create-react-app, et le backend en utilisant une API Node
* Utilisez une base de données comme Postgres ou MongoDB, ainsi qu'un ORM comme Prisma (Postgres) ou Mongoose (MongoDB)
* Utilisez l'authentification sociale avec Google, Facebook ou Twitter, en utilisant Passport ou un service plus simple comme Auth0
* Déployez le backend sur Heroku, le frontend sur Netlify

## 3. Application de commerce électronique

**Exemples concrets** : Shopify, Etsy, Dev.to Storefront

Les vitrines où nous pouvons acheter des produits numériques ou physiques en ligne sont partout. Les applications de commerce électronique ajoutent la possibilité pour les utilisateurs d'ajouter et de supprimer des articles d'un panier d'achat, de visualiser leur panier et de passer à la caisse en utilisant une carte de crédit, ainsi que d'autres options de paiement comme Google Pay et Apple Pay. 

Si vous cherchez de l'inspiration, consultez certaines vitrines plus simples comme une vitrine Shopify, plutôt que de regarder un grand détaillant comme Amazon ou Walmart.

### Comment construire une application de commerce électronique : 

* Créez l'application avec create-react-app ou Next.js
* Ajoutez le package NPM `stripe`, plus `use-shopping-cart` pour gérer facilement les paiements directement avec Stripe Checkout
* Construisez une API Node pour gérer la création de sessions avec Stripe
* Déployez le backend sur Heroku, le frontend sur Netlify (ou déployez les deux sur Heroku)

## 4. Application de partage de vidéos

**Exemples concrets** : YouTube, TikTok, Snapchat

Une application de partage de vidéos est probablement la catégorie la plus large, car la vidéo est utilisée dans de nombreuses applications différentes et de nombreuses manières différentes. 

Vous avez des applications de partage de vidéos comme YouTube, qui vous permettent de rechercher n'importe quel navigateur et de chercher n'importe quelle vidéo que vous pouvez imaginer que les utilisateurs ont créée. De plus, TikTok et Snapchat nous donnent la possibilité de regarder des vidéos d'autres utilisateurs qui sont enregistrées dans un format beaucoup plus court et plus accessible, et sont plus orientées autour des interactions comme les likes et les vues.

### Comment construire une application de partage de vidéos : 

* Créez l'application avec create-react-app, et créez le backend avec Node/Express
* Utilisez Cloudinary pour les téléchargements d'images et de vidéos vers l'API Cloudinary
* Utilisez une base de données comme Postgres ou MongoDB, ainsi qu'un ORM comme Prisma (Postgres) ou Mongoose (MongoDB)
* Déployez le backend sur Heroku, le frontend sur Netlify (ou déployez les deux sur Heroku)

## 5. Application de blogging / portfolio

**Exemples concrets** : Medium, Dev.to, HashNode

Cet exemple d'application est peut-être le plus pratique. Le choix le plus immédiatement pratique pour vous de construire une application de blogging ou de portfolio est quelque chose qui met en valeur vos compétences. Cela vous permet de montrer ce que vous pouvez faire en tant que développeur, tout en vous permettant d'inclure des publications et du contenu qui reflètent ce que vous savez. 

La création de ces applications avec des outils comme Gatsby ou Nextjs (qui sont tous deux des frameworks React) est maintenant plus facile que jamais.

### Comment construire une application de blogging ou de portfolio : 

* Créez l'application avec Gatsby ou Next.js
* Utilisez le markdown pour les articles de blog avec un plugin de transformation markdown spécial comme `remark`
* Déployez le site sur Netlify ou Vercel

## 6. Application de forum

**Exemples concrets** : Reddit, StackOverflow, forum freeCodeCamp

Une application de forum est l'endroit où nous allons lorsque nous voulons obtenir de l'aide, et en tant que programmeurs, nous visitons des forums comme Reddit et Stack Overflow pour obtenir des réponses à nos questions de codage. 

Les forums combinent également de nombreux éléments des applications de chat et de médias sociaux à travers des publications, des commentaires et des réactions. Un forum est une version plus organisée d'une application de médias sociaux où les utilisateurs peuvent plus facilement trouver des réponses aux questions qu'ils recherchent. 

### Comment construire une application de forum : 

* Construisez votre frontend avec create-react-app, et le backend en utilisant une API Node
* Utilisez une base de données comme Postgres ou MongoDB, ainsi qu'un ORM comme Prisma (Postgres) ou Mongoose (MongoDB)
* Utilisez l'authentification sociale avec Google, Facebook ou Twitter, en utilisant Passport ou un service plus simple comme Auth0
* Déployez le backend sur Heroku, le frontend sur Netlify

## 7. Application de streaming musical

**Exemples concrets** : Spotify, Soundcloud, Pandora

Tout comme les applications React sont parfaites pour servir du contenu vidéo, elles sont également idéales pour le streaming de médias comme la musique. 

Les applications de musique ont une structure similaire aux applications de partage de vidéos et peuvent ou non permettre aux utilisateurs de télécharger leur propre musique. Elles permettent aux utilisateurs d'écouter de la musique, d'aimer des chansons, de les commenter et peut-être même d'acheter de la musique. 

De cette manière, une application de streaming musical peut combiner des éléments d'une application de partage de vidéos ainsi que d'une application de commerce électronique.

### Comment construire une application de streaming musical : 

* Créez l'application avec create-react-app, et créez le backend avec Node/Express
* Utilisez Cloudinary pour les téléchargements d'images et de vidéos vers l'API Cloudinary
* Utilisez une base de données comme Postgres ou MongoDB, ainsi qu'un ORM comme Prisma (Postgres) ou Mongoose (MongoDB)
* Déployez le backend sur Heroku, le frontend sur Netlify (ou déployez les deux sur Heroku)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*