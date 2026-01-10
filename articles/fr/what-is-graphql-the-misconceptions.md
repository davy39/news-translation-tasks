---
title: Qu'est-ce que GraphQL ? Débunking des mythes courants.
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-01-07T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-graphql-the-misconceptions
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/1_RHQ7lpGDV_M3yWRa9DiR2g-2.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
seo_title: Qu'est-ce que GraphQL ? Débunking des mythes courants.
seo_desc: "I love talking about GraphQL, especially with people who have been working\
  \ with GraphQL or thinking of adopting GraphQL. One common question people have\
  \ is why someone would want to move to GraphQL from REST. \nThere are a ton of resources\
  \ out there t..."
---

J'adore parler de GraphQL, surtout avec des personnes qui travaillent avec GraphQL ou qui envisagent d'adopter GraphQL. Une question courante que les gens se posent est de savoir pourquoi quelqu'un voudrait passer de REST à GraphQL. 

Il existe une tonne de ressources qui parlent de la différence entre REST et GraphQL et celles-ci sont excellentes à consulter si vous êtes intéressé par les différences entre ces deux technologies. Dans cet article de blog, je souhaite aborder quelques idées fausses et questions courantes sur GraphQL.

## Comment bénéficiez-vous de GraphQL sur le front end ?

En tant qu'ingénieur Front End, j'aime travailler avec une API GraphQL pour les raisons suivantes :

1. Vous pouvez tester instantanément des requêtes et des mutations en utilisant GraphiQL ou playground
2. Moins de données signifie une gestion d'état plus légère
3. Il décharge le travail lourd au serveur via les resolvers
4. Il dispose d'une documentation à jour et interactive

## En quoi est-il meilleur que REST ?

1. Il y a un seul endpoint pour récupérer toutes les ressources.
2. Vous évitez la sur-récupération de données (obtenir trop de champs alors que seuls quelques champs sont nécessaires).
3. Vous évitez la sous-récupération de données (devoir appeler plusieurs API parce qu'une seule API ne renvoie pas toutes les informations nécessaires).

## Mythe : GraphQL est utilisé pour interroger des bases de données graphiques.

GraphQL peut être utilisé pour interroger une base de données graphique, mais ce n'est pas son seul cas d'utilisation. Le "graph" dans GraphQL est utilisé pour représenter la structure de données en forme de graphe. Vous modélisez les données en termes de nœuds et de leurs connexions. Le schéma est utilisé pour représenter cette modélisation.

Il n'y a aucune limitation dans la spécification GraphQL qui impose que la source de données doit être un graphe.

## Mythe : GraphQL ne fonctionne qu'avec des bases de données ou des sources de données basées sur des graphes.

C'est une idée fausse que vous devez réécrire votre base de données pour adopter GraphQL. GraphQL peut être un wrapper autour de n'importe quelle source de données, y compris les bases de données. GraphQL est un `langage de requête pour votre API` - ce qui signifie qu'il s'agit d'une syntaxe pour demander des données.

## Mythe : La récupération de données avec des resolvers, des requêtes et des mutations fonctionne magiquement.

Vous devrez définir exactement ce que chacun d'eux doit faire. Vous écrirez des fonctions qui sont appelées lorsque des requêtes sont lancées, et vous écrirez des fonctions pour les resolvers qui renvoient exactement les données dont vous avez besoin et qui savent quelle API appeler. Vous définirez quelles données sont retournées via ces fonctions en appelant des resolvers.

## Mythe : GraphQL remplace Redux ou toute bibliothèque de gestion d'état

Redux est une bibliothèque de gestion d'état. GraphQL n'est pas une bibliothèque de gestion d'état. GraphQL aide à obtenir moins de données, ce qui entraîne moins de données à gérer côté client, mais ce n'est pas une solution de gestion d'état. 

Vous devrez toujours gérer l'état - bien que de manière plus légère. Des bibliothèques clientes comme Apollo et Relay peuvent être utilisées pour gérer l'état et elles ont un cache intégré. GraphQL n'est pas un remplacement pour Redux - il aide à réduire le besoin de celui-ci.

## Mythe : GraphQL est un langage de base de données.

GraphQL est un langage de programmation - spécifiquement un langage de requête. La spécification de GraphQL définit comment les runtimes GraphQL doivent implémenter le langage et comment les données doivent être communiquées entre le client et le serveur. 

GraphQL est utilisé pour demander des données et peut être utilisé à plusieurs endroits dans n'importe quelle couche, du front end au back end. Il existe des bases de données telles que DGraph qui implémentent la spécification GraphQL, permettant aux clients d'utiliser GraphQL pour interroger la base de données.

## Mythe : Vous ne pouvez pas avoir d'endpoints REST dans votre implémentation avec GraphQL.

Vous pouvez brancher plusieurs endpoints REST ou même plusieurs endpoints GraphQL dans votre application. Bien que ce ne soit pas une meilleure pratique d'avoir plusieurs endpoints REST, c'est techniquement possible.

## Mythe : GraphQL est difficile à introduire dans un projet existant.

GraphQL peut être intégré dans un projet existant. Vous pouvez commencer avec un composant de logique métier, brancher un endpoint GraphQL, et commencer à récupérer des données via GraphQL. Vous n'avez pas besoin de tout abandonner dans un projet pour commencer à utiliser GraphQL. 

Si le passage à un endpoint GraphQL est encore une tâche intimidante, vous pouvez commencer par masquer un endpoint REST en un endpoint GraphQL en utilisant des resolvers.

## Mythe : GraphQL est uniquement pour les développeurs front-end

GraphQL est agnostique de la plateforme. À mon avis, la beauté des avantages de GraphQL commence de l'intérieur vers l'extérieur - du back end au front end. 

En tant que développeur back end, vous êtes en mesure d'étendre l'API en ajoutant des champs sans avoir à publier une nouvelle version de l'API. Vous n'avez pas besoin d'écrire différents endpoints pour différents besoins puisque les clients peuvent récupérer les données dont ils ont besoin. 

Avec GraphQL, vous avez une visibilité sur les champs que les clients utilisent, ce qui fournit une instrumentation puissante.

## Mythe : GraphQL écrira lui-même les requêtes de base de données, je dois simplement spécifier les schémas et la relation entre eux

Vous devrez peut-être écrire les requêtes de base de données en fonction de la bibliothèque GraphQL que vous utilisez. Cependant, certaines bibliothèques comme Neo4j et Prisma écrivent également des requêtes de base de données et abstraient la logique du développeur. Tout, y compris les resolvers, les requêtes et les mutations, doit être défini.

## Mythe : GraphQL est utilisé pour dessiner des graphiques.

Souvent, les personnes nouvelles à GraphQL pensent que c'est un logiciel de traçage de graphiques tel que D3. GraphQL ne trace pas de graphiques.

## Mythe : GraphQL nécessite des clients compliqués et est presque impossible à faire avec un simple fetch HTTP

## Mythe : Il remplace les ORM.

Récemment, nous voyons beaucoup d'intégrations de bases de données et de GraphQL, mais GraphQL lui-même n'est pas cela.

Je pense que GraphQL est génial ! Il existe une multitude de bibliothèques qui aident un utilisateur à commencer avec GraphQL. Si vous êtes intéressé à apprendre GraphQL, [commencez par la documentation](https://graphql.org/learn/) ou [consultez ce cours Udemy](https://www.udemy.com/course/graphql-with-react-course/) que j'ai trouvé utile lorsque j'étais nouveau dans GraphQL.

%[https://twitter.com/shrutikapoor08/status/1205005069223022592]