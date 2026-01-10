---
title: Vous voulez comprendre rapidement la pile MEAN ? Voici une documentation avec
  des diagrammes utiles.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-08T11:01:56.000Z'
originalURL: https://freecodecamp.org/news/cjn-understanding-mean-stack-through-diagrams
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-08-at-3.58.32-AM.png
tags:
- name: documentation
  slug: documentation
- name: full stack
  slug: full-stack
- name: ' Single Page Applications '
  slug: single-page-applications
- name: software architecture
  slug: software-architecture
- name: Web Development
  slug: web-development
seo_title: Vous voulez comprendre rapidement la pile MEAN ? Voici une documentation
  avec des diagrammes utiles.
seo_desc: 'By Clark Jason Ngo

  This article is based on my capstone for the City University of Seattle. The title
  of my research is "Software Documentation and Architectural Analysis of Full Stack
  Development". The goal of my research was to reduce the learning ...'
---

Par Clark Jason Ngo

Cet article est basé sur mon projet de fin d'études pour l'[Université de la Ville de Seattle](https://www.cityu.edu/). Le titre de ma recherche est "Documentation logicielle et analyse architecturale du développement full stack". L'objectif de ma recherche était de réduire la courbe d'apprentissage pour comprendre les projets open source et le développement full stack, et j'ai choisi la pile MEAN.

J'ai créé les diagrammes suivants, en utilisant [Lucidchart](https://www.lucidchart.com/), pour une compréhension plus facile. Ces diagrammes UML étaient basés sur le modèle de vue architecturale 4+1 :

* Analogie du restaurant
* Vue de processus utilisant un diagramme de séquence
* Scénario utilisant un diagramme de séquence
* Vue physique utilisant un diagramme de déploiement
* Vue de développement utilisant un diagramme de package
* Vue logique utilisant un diagramme de classe

La recherche était plus axée sur le déploiement et le flux de requêtes et de réponses.

# Pile MEAN

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/logo1.png)

La pile MEAN est une solution full-stack JavaScript open-source. Elle est composée de MongoDB, Express, Angular et Node.js.

L'idée derrière celle-ci est de résoudre les problèmes courants liés à la connexion de ces frameworks, de construire un framework robuste pour soutenir les besoins de développement quotidiens et d'aider les développeurs à utiliser de meilleures pratiques tout en travaillant avec des composants JavaScript populaires.

## Back-end avec Node.js

Node.js est conçu pour gérer les E/S asynchrones tandis que JavaScript dispose d'une boucle d'événements intégrée pour le côté client. Cela rend Node.js rapide par rapport à d'autres environnements. Cependant, l'approche basée sur les événements/les rappels rend Node.js difficile à apprendre et à déboguer.

Node.js inclut des modules tels que Mongoose, qui est un modèle d'objets MongoDB, et le framework d'application web Express. Grâce aux modules Node, l'abstraction peut être réalisée, ce qui réduit la complexité globale de la pile MEAN.

## Back-end avec le Framework Express

Express est un framework d'application minimaliste et non opinionné pour Node.js. C'est une couche au-dessus de Node.js qui est riche en fonctionnalités pour le développement web et mobile sans masquer aucune fonctionnalité de Node.js.

## Front-end avec Angular

Angular est une plateforme de développement web construite en TypeScript qui fournit aux développeurs des outils robustes pour créer le côté client des applications web.

Il permet le développement d'applications web monopage où le contenu change dynamiquement en fonction du comportement et des préférences de l'utilisateur. Il dispose d'une injection de dépendances pour garantir que, chaque fois qu'un composant est modifié, les autres composants qui lui sont liés seront modifiés automatiquement.

## Base de données avec MongoDB

MongoDB est une base de données NoSQL qui stocke les données en BJSON (Binary JavaScript Object Notation).

MongoDB est devenu la base de données standard de facto pour les applications Node.js afin de répondre au paradigme "JavaScript partout" en utilisant JSON (JavaScript Object Notation) pour transmettre des données entre les différentes couches (front-end, back-end et la base de données).

Maintenant que nous avons couvert ces bases, examinons ces diagrammes.

## Analogie du restaurant

Comme je voulais aborder la courbe d'apprentissage abrupte, j'ai choisi une analogie de restaurant pour permettre à l'utilisateur de comprendre et de retenir le processus de requête et de réponse dans une application full stack.

Le client (utilisateur final) passe sa commande par l'intermédiaire du serveur (contrôleur), et le serveur transmet la demande à la personne à la fenêtre de commande (usine de service).

Ces trois composants constituent le serveur front-end. L'usine de service sera celle qui communiquera avec le cuisinier (contrôleur) dans le back-end. Le cuisinier ira ensuite chercher les ingrédients nécessaires (données) dans le réfrigérateur (serveur de base de données).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/analogy_request.png)

Le réfrigérateur sera en mesure de fournir le matériel nécessaire (données) au cuisinier dans le back-end. Le cuisinier peut maintenant traiter ces données et les renvoyer à l'usine de service du front-end.

Le contrôleur (serveur) remettra le repas préparé au client (utilisateur). Le client pourra maintenant consommer le repas (données).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/analogy_response.png)

## Vue de processus utilisant un diagramme de séquence

Qui l'utilise ou ce qu'il montre :

* Intégrateurs
* Performance
* Évolutivité

Dans la vue de processus, je montre d'abord le serveur front-end et le serveur back-end séparément, puis je les connecte ensemble avec le serveur de base de données.

Dans le premier exemple, une application Angular a été déployée avec un JSON codé en dur dans un fichier `service.ts` (situé dans l'usine de service).

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_frontend.png)

L'application Angular peut communiquer avec des API tierces pour obtenir des données et les afficher à l'utilisateur.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_frontend_api.png)

Dans notre back-end, l'exemple d'application Node.js commence avec un JSON codé en dur qui peut être traité et utilisé comme réponse.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_backend.png)

Ce back-end peut être connecté à des API tierces ou à un serveur de base de données pour obtenir le JSON, le traiter et le renvoyer au demandeur.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_backend_database.png)

Avec les processus du serveur front-end, du serveur back-end et du serveur de base de données expliqués, je montre la combinaison de ces trois serveurs ci-dessous :

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/pro_mean.png)

Lorsqu'une requête HTTP est effectuée, le front-end sera déclenché et Angular prendra la requête. La requête sera transmise en interne dans Angular avec Route envoyant une requête pour la vue à View/Template.

View/Template demandera le Controller. Le Controller créera ensuite une requête HTTP vers un endpoint RESTful (Representational state transfer) vers le Server Side, qui est Express/Node.js. La requête sera ensuite transmise en interne avec Express/Node.js de son Route au Controller/Model.

Le Controller/Model fera une requête via le Mongoose ODM pour interagir avec le Database Server qui a MongoDB. MongoDB traitera la requête et répondra au rappel à Express/Node.js.

Express/Node.js envoie une réponse JSON au Controller Angular. Le Controller Angular répondra alors avec une vue.

## Vue de scénario utilisant un diagramme de séquence

Qui l'utilise ou ce qu'il montre :

* Décrire les interactions entre objets et entre processus

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/sce_book_store.png)

Le scénario décrit ci-dessus implique un utilisateur accédant à une application de librairie. Lorsque l'utilisateur entre l'URL, JavaScript sera exécuté et atteindra le routeur du serveur front-end, qui est le AppRoutingModule. Le AppRoutingModule appellera le BooksComponent, qui chargera fetchBooks comme son injection de dépendance.

fetchBooks créera ensuite une requête HTTP vers le serveur back-end qui dispose d'un routeur, d'un contrôleur et d'un modèle pour traiter la requête et interroger le serveur de base de données.

Le serveur de base de données traite la requête, et avec le serveur back-end en attente, récupérera les données et les renverra au serveur front-end sous forme de réponse JSON.

Le front-end disposera maintenant des données et de la vue de modèle à afficher à l'utilisateur.

## Vue physique utilisant un diagramme de déploiement

Qui l'utilise et ce qu'il montre :

* Ingénieur système
* Topologie
* Communications

Le diagramme de déploiement montre 3 serveurs : front-end, back-end et base de données. Dans le front-end, nous avons besoin du navigateur car les applications Angular sont des applications web basées sur le navigateur.

Le serveur back-end héberge notre Node.js avec Express au-dessus de Node.js. Dans Express, nous avons l'application et Mongoose au-dessus. Express gérera la communication entre le front-end et la base de données. Le serveur de base de données n'inclut que MongoDB. Il utilise JSON pour communiquer entre les serveurs.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_overview.png)

Dans notre première version de la pile MEAN, nous allons déployer localement en utilisant notre machine locale (localhost) pour déployer le serveur front-end, le serveur back-end et le serveur de base de données.

Nous allons utiliser les ports par défaut suivants : Angular - port 4200, Node.js/Express – port 3000, et MongoDB – port 27017.

Le diagramme ci-dessous montre l'application web full stack en notation UML.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_local_uml.png)

En passant à la production réelle, la chose à migrer vers le cloud est notre base de données. Pour MongoDB, j'ai choisi MongoDB Atlas comme solution cloud.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_local_cloud_uml.png)

La dernière étape du déploiement en production consiste à télécharger notre code front-end sur Amazon S3 et à télécharger le back-end dans une instance EC2 avec AWS. Ils communiqueront tous entre eux avec des endpoints HTTP/HTTPS.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_cloud_uml.png)

Voici un autre diagramme pour montrer notre déploiement de production sans utiliser la notation UML.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/phy_cloud.png)

## Vue de développement utilisant un diagramme de package

Qui l'utilise et ce qu'il montre :

* Programmeurs
* Gestion de logiciels

La vue de package de l'application Angular montre que chaque composant Angular est importé dans le AppModule. AppModule et AppRoutingModule dépendent de BooksComponent. Le BooksComponent dépend de BookDetailComponentDialog et ApiService.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/dev_angular.png)

La vue de package de l'application Node.js montre que toutes les opérations CRUD (contrôleurs) telles que fetch all books, fetch a book, update a book et delete a book sont importées par l'application. De plus, toute la logique des opérations CRUD réside dans le modèle book.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/dev_nodejs.png)

## Vue logique utilisant un diagramme de classe

Qui l'utilise et ce qu'il montre :

* Utilisateur final
* Fonctionnalité

L'application de librairie n'a présenté qu'une seule classe appelée Book. Les membres de la classe sont : title, isbn, author, picture et price. Les méthodes sont : addBook, fetchBooks, fetchBook, updateBook et deleteBook.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/log_book.png)

La structure du modèle Book au format JSON.

![Image](https://github.com/clarkngo/cityu_capstone/raw/master/images/log_book_json.png)

**Voici quelques vidéos pour les diagrammes :**

%[https://youtu.be/hPNziXpjf7E?list=PLK4sJSsw4V-fxsMJEC8YV7cPDlYxp7Ib2]

**Documentation disponible sur mon GitHub :**

%[https://github.com/clarkngo/cityu_capstone]

Retrouvez-moi sur [LinkedIn](https://www.linkedin.com/in/clarkngo/). =)