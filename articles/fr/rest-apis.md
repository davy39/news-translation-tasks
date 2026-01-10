---
title: API REST
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T19:44:00.000Z'
originalURL: https://freecodecamp.org/news/rest-apis
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce0740569d1a4ca34ad.jpg
tags:
- name: REST API
  slug: rest-api
- name: toothbrush
  slug: toothbrush
seo_title: API REST
seo_desc: 'History

  REST stands for Representational State Transfer protocol. Roy Fielding defined REST
  in his PhD dissertation in 2000.

  What is a REST API?

  REST was developed to provide a uniform interface for


  Identifying resources

  Manipulation of resources

  Se...'
---

## Histoire

REST signifie **Re**presentational **S**tate **T**ransfer protocol. Roy Fielding a défini REST dans sa thèse de doctorat en 2000.

## Qu'est-ce qu'une API REST ?

REST a été développé pour fournir une interface uniforme pour

* Identifier les ressources
* Manipuler les ressources
* Messages auto-descriptifs
* Utiliser l'hypermédia comme moteur de l'état de l'application (HATEOS)

## Bonnes pratiques

### Bases

**Méthode** ||		[http://api.co/v2/cars](http://api.co/v2/cars)	||	[http://api.co/v2/cars/1234](http://api.co/v2/cars/1234) 

* GET ||				Lister toutes les voitures 	||	   Récupérer une voiture individuelle 
* POST ||			Créer une nouvelle voiture     ||				Erreur 
* PUT ||		Remplacer les collections de voitures  ||  Remplacer la voiture avec l'id 1234   
								par une nouvelle 
* DELETE ||       Supprimer toutes les voitures 			||		   Supprimer la voiture avec l'id 1234

_Note : lors des opérations PUT, soit le client soit le serveur peut générer des identifiants_

### Les noms sont bons, les verbes sont mauvais

* Utilisez des noms pour référencer les ressources comme `cars`, `fruits`, etc.
* Utilisez des verbes pour les déclarations d'actions `convertMilesToKms`, `getNutritionalValues`

### Singulier ou pluriel ?

Utilisez une grammaire correcte pour la déclaration

**À éviter** `/person/145`

**Préférer** `/people/154` Supposez retourner la 154ème personne de la liste des personnes

### Cas d'utilisation

Utilisez l'un des modèles ci-dessous et soyez **cohérent !**

Styles de casExemple**UpperCamelCase**`http://api.fintech.cp/DailyTransactions/Today`**lowerCamelCase**`http://api.fintech.cp/dailyTransactions/today`**snake_case**`http://api.fintech.cp/daily_transactions/today`

### Relations et ressources

* Les ressources peuvent avoir des relations `one-to-many`, `many-to-many`, `many-to-one`, etc. Les mapper correctement est crucial.

**Mapping One-to-Many**

Par exemple, `Tickets/145/messages/4` suggère une relation one-to-many entre `tickets` et `messages`. Signifiant qu'un ticket a `N` messages. Le message n'est pas une ressource autonome. Vous ne pouvez pas avoir `/messages/4`.

**Mapping Many to Many**

Par exemple, `/usergroups/345/users/56` suggère de sélectionner le 345ème groupe d'utilisateurs et d'obtenir l'utilisateur avec l'id 56. Cependant, un utilisateur peut être dans plusieurs `usergroups`, c'est-à-dire que `/usergroups/209/users/56` est également valide. Dans un tel cas, pour séparer la ressource dépendante `users` dans un endpoint séparé comme `/users/56` et fournir un lien de ressource dans `/usergroups/209/users/56`

### Paramètres de l'API

* **PATH** : _requis_ pour accéder à la ressource Ex. `/cars`, `/fruits`
* **Paramètres de requête** : _optionnels_ pour filtrer la liste Ex. `/cars?type=SUV&year=2010`
* **Body** : Logique spécifique à la ressource. Requête de recherche avancée. Parfois, cela peut avoir à la fois des paramètres de requête et de body.
* **Header** : Doit contenir des données globales ou spécifiques à la plateforme. Ex. Paramètres de clé API, clés cryptées pour l'authentification, informations sur le type de périphérique, par exemple mobile ou desktop ou endpoint, type de données de périphérique, par exemple xml ou json. Utilisez l'en-tête pour communiquer ces paramètres

### Codes de statut HTTP

Utilisez les codes de statut corrects

CodesSignification1xxRequête reçue et comprise.2xxAction demandée par le client a été reçue, comprise et demandée.3xxLe client doit prendre des mesures supplémentaires pour compléter la requête. La plupart de ces codes de statut sont utilisés dans la redirection d'URL.4xxDestiné aux situations où il semble que l'erreur a été causée par le client.5xxLe serveur n'a pas pu satisfaire une requête.

Un peu plus sur **2xx** !

* **201 Ressource créée.** POST `/cars` doit retourner HTTP 201 créé avec l'en-tête `location` indiquant comment accéder à la ressource Ex. `location` : `api.com/cars/124` dans l'en-tête

**202 - Accepté**

Utilisez ceci si la tâche est énorme à exécuter. Dites au client qu'il a accepté la requête et qu'il va/est en train de traiter/processus Aucun payload n'est retourné

**204 - Aucun contenu**

Utilisé lorsque supprimé `DELETE cars/124` Ne retourne aucun contenu. Mais peut également retourner `200 OK` si l'API a l'intention d'envoyer la ressource supprimée pour un traitement ultérieur.

Les ressources dangereuses **5xx** !

* **500** Erreur interne du serveur
* **504** Délai d'attente de la passerelle. Le serveur n'a pas reçu de réponse en temps opportun

Moins connu **4xx** suggère que vous passez un mauvais paramètre. Peut également passer des informations qui sont incorrectes. Ex.

`DELETE /cars/MH09234`

retourne `4xx` ou message `Expecting int car id /car/id got string car/MH09234`