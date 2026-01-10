---
title: Comment obtenir des API GraphQL instantanées sur votre application Laravel
  existante
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T16:16:05.000Z'
originalURL: https://freecodecamp.org/news/instant-graphql-apis-on-your-existing-laravel-app-e4af9917148c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q3KiCaC7_bynx8CfVlTXNw.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: Laravel
  slug: laravel
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment obtenir des API GraphQL instantanées sur votre application Laravel
  existante
seo_desc: 'By Karthikeya Viswanath

  TL;DR


  Setup GraphQL engine — Install Hasura GraphQL engine and expose tables over a GraphQL
  API

  Authentication and Securing your GraphQL Server

  Migrations


  In this post, we’ll use the Hasura GraphQL Engine to get instant Grap...'
---

Par Karthikeya Viswanath

#### TL;DR

* [**Installation du moteur GraphQL**](#heading-installation) — Installez le moteur GraphQL Hasura et exposez les tables via une API GraphQL
* [**Authentification et sécurisation de votre serveur GraphQL**](#heading-authentification)
* [**Migrations**](#heading-migrations)

Dans cet article, nous utiliserons le [Hasura GraphQL Engine](https://hasura.io) pour obtenir des API GraphQL instantanées sur mon application Laravel existante en cours d'exécution localement.

Pour les besoins de ce projet, nous utiliserons une application Laravel ToDo d'exemple construite avec Laravel 5.1, et nous modifierons le code pour intégrer HGE. (Veuillez noter cependant que Laravel 5.1 a déjà atteint sa fin de vie en juin 2018, et vous devriez migrer vers une version plus récente si vous utilisez toujours celle-ci.)

Vous pouvez trouver l'application d'exemple initiale [ici](https://github.com/milon/laravel-todo), le dépôt final [ici](https://github.com/hasura/laravel-todo-hge), et une application en direct pour que vous puissiez la tester [ici](http://laravel-todo-hge.herokuapp.com/).

Voici à quoi ressemblera notre architecture prévue :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hEit6SqjtIbh0gdYFE0cGw.png)
_Architecture avant et après l'intégration avec HGE_

### Installation du moteur GraphQL

Le [moteur GraphQL Hasura](https://hasura.io/) (HGE) vous offre une API GraphQL instantanée en temps réel sur votre base de données Postgres existante. HGE fonctionne directement avec votre système existant :

* [**Base de données Postgres**](#heading-postgres) — Se connecte à votre base de données existante et fournit une API GraphQL pour votre base de données.
* [**Système d'authentification**](#heading-authentification) — Se connecte à votre système d'authentification existant pour sécuriser l'API GraphQL.
* [**Système de migration**](#heading-migrations) — Le moteur GraphQL Hasura n'interfère pas avec le système de migration Laravel existant. Les schémas peuvent être gérés séparément dans Laravel tant qu'ils n'altèrent pas le schéma suivi par le moteur GraphQL. Plus d'informations sur la manière dont le moteur GraphQL Hasura gère l'état de votre schéma [ici](https://docs.hasura.io/1.0/graphql/manual/engine-internals/index.html).

Il est également livré avec une console pratique, avec GraphiQL intégré, utile pour le débogage des API GraphQL.

### Installation

Le moteur GraphQL Hasura peut être installé sur Heroku en utilisant le bouton ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*dcgu-klnpwTWilYiGMdM6Q.jpeg)
_Cliquez sur ce bouton pour déployer le moteur GraphQL sur Heroku_

ou sur toute machine capable d'exécuter Docker. Consultez la section [getting-started](https://docs.hasura.io/1.0/graphql/manual/getting-started/index.html) pour plus d'informations.

Pour les besoins de ce tutoriel, nous avons configuré une instance HGE pour notre application Laravel [ici](https://hge-laravel-todo.herokuapp.com/console) (utilisez la clé d'accès `helloworld`, nous expliquerons comment cela fonctionne ci-dessous).

#### [Installation utilisant Docker](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/index.html)

Avant d'installer le moteur GraphQL Hasura, vous aurez besoin d'une chaîne de connexion postgres. Vous pouvez l'obtenir à partir de votre fichier `config/database.php`, ou de votre fichier `.env`, là où vos identifiants de stockage sont conservés.

En mettant les détails ensemble :

```
postgres://username:SECUREPASSWORD@host:port/database_name
```

Suivez les instructions [ici](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/index.html).

Une fois que le moteur GraphQL Hasura démarre, la visite de [http://localhost:8080](http://localhost:8080) ouvre la console Hasura. La console fournit une instance GraphiQL pour tester facilement toutes vos requêtes GraphQL, mutations, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dJlxjx1PHK5flNXiKVy5sg.jpeg)
_Console du moteur GraphQL Hasura_

Maintenant, allez dans l'onglet Data, et suivez toutes les tables pour créer des API GraphQL instantanées !

### Authentification

Par défaut, HGE est installé en mode développement. Toutes les tables/vues suivies par HGE peuvent être consultées/mises à jour sans aucune vérification. Cela n'est pas recommandé pour un environnement de production. Hasura vous permet de définir des contrôles d'accès granulaires pour chaque champ de votre schéma GraphQL, c'est-à-dire chaque table ou vue de votre schéma Postgres. Ces règles de contrôle d'accès peuvent utiliser des variables dynamiques qui accompagnent chaque requête. Consultez la [documentation](https://docs.hasura.io/1.0/graphql/manual/auth/index.html) pour plus d'informations.

HGE peut être sécurisé contre l'accès direct en configurant une URL de webhook qui sera appelée pour valider chaque requête, sauf si la requête contient une `access-key` valide.

Commençons par faire une simple requête pour les utilisateurs :

Et l'exécuter dans GraphiQL :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VVG55IL6bFoDlYnCDvk9vg.png)

Notez que `x-hasura-user-id` est défini sur "2" et `x-hasura-role` est défini sur "user". Ce sont les en-têtes `auth` qui devront être définis par le `auth-hook` en [mode production](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/securing-graphql-endpoint.html). (Le moteur GraphQL démarré avec `access-key` et `auth-hook`).

#### Sécuriser l'API GraphQL

![Image](https://cdn-media-1.freecodecamp.org/images/1*nJKLzkgQXGd7a7ILDBAEfQ.png)
_Architecture du webhook_

La première étape consiste à [sécuriser HGE](https://docs.hasura.io/1.0/graphql/manual/deployment/securing-graphql-endpoint.html) avec une `access-key` et à configurer `auth-hook` avec un webhook, qui dans ce cas sera servi par l'application Laravel. Ce webhook sera invoqué par le moteur GraphQL, avec les en-têtes attachés à la requête. Le webhook retournera les `x-hasura-role` et `x-hasura-user-id` appropriés, qu'il peut obtenir en authentifiant l'utilisateur avec l'en-tête `Authorization` qui est transmis à partir de la requête.

Ici, l'hôte du auth-hook sera votre adresse IP sur le réseau docker bridge si vous utilisez docker, ou votre URL de webhook sinon. Vous pouvez ignorer la section `postgres` si vous utilisez une base de données Postgres externe.

Pour configurer les indicateurs `access-key` / `auth-hook` sur votre instance Heroku de HGE, [suivez ces instructions](https://docs.hasura.io/1.0/graphql/manual/deployment/heroku/securing-graphql-endpoint.html). Nous supposerons que le webhook est à `/hge-webhook` pour l'instant, nous le configurerons sur Laravel plus tard.

Essayons de faire la requête à nouveau et voyons quelle est la réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*afYqLtDIyrJyR7RU7iG6_w.jpeg)

C'est parce que nous n'avons pas encore configuré le webhook, ou même défini les en-têtes `Authorization` corrects.

### Configuration du webhook Laravel

Configurons notre application d'exemple sur Heroku, afin que nous puissions facilement la déployer et tester nos modifications.

Pour les besoins de ce tutoriel, nous avons déployé une application d'exemple avec le webhook [ici](http://laravel-todo-hge.herokuapp.com). L'instance HGE correspondante peut être accessible [ici](https://hge-laravel-todo.herokuapp.com/console). (Clé d'accès : `helloworld`)

Vous pouvez vous inscrire sur cette application d'exemple, et ajouter/supprimer des todos sur l'application.

Ajoutons maintenant un webhook pour authentifier les requêtes envoyées à notre instance HGE. Nous allons le faire en utilisant un middleware, alors générons d'abord une classe middleware.

`php artisan make:middleware webhookMiddleware`

Ajoutons d'abord la route à notre fichier `app/Http/routes.php` :

Maintenant, nous allons enregistrer notre middleware en l'ajoutant au fichier `app/Http/Kernel.php` sous `routeMiddleware` :

Maintenant, configurons le webhook réel à `app/Http/Middleware/webhookMiddleware.php` :

Cette page utilise simplement le jeton bearer `Authorization` pour démarrer une session, puis utilise Auth de Laravel pour vérifier et obtenir l'ID de l'utilisateur. Vous pouvez modifier cela pour ajouter votre logique de session/jeton personnalisée, et vérifier l'authentification.

Si authentifié, nous retournons les variables `x-hasura-role` et `x-hasura-user-id` en JSON. Cela authentifiera la requête à HGE.

Maintenant, nous avons besoin d'un moyen facile d'obtenir le jeton de session d'un utilisateur connecté, alors ajoutons cela à notre `resources/views/users/profile.blade.php` :

Maintenant, connectez-vous et allez dans le Profil de l'utilisateur pour voir votre nouveau jeton de session :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KvPgJCAvDSq3btHtZ-xw7A.png)

Faisons un commit et déployons cela sur Heroku :

`git commit -am "Add HGE webhook"`

`git push heroku master`

Une fois poussé, dirigeons-nous vers la console HGE pour tester notre nouveau webhook !

![Image](https://cdn-media-1.freecodecamp.org/images/1*2hIa4anl3efGIqbJv2dgLw.png)
_Autorisation utilisant le jeton Bearer_

Le webhook retourne les `x-hasura-user-id` et `x-hasura-role` correspondants, et le moteur GraphQL répond avec les résultats appropriés comme configuré dans les règles d'accès.

### Système de migration

HGE est livré avec un puissant système de migration inspiré de Rails, et les modifications apportées dans la console HGE génèrent automatiquement des fichiers de schéma dans votre dossier lorsqu'ils sont exécutés en tant que `hasura console` (vous pouvez installer le [Hasura CLI](https://docs.hasura.io/1.0/graphql/manual/hasura-cli/install-hasura-cli.html) pour cela).

Pour les besoins de ce blog, cependant, nous laisserons Laravel gérer nos migrations, et nous exporterons simplement les métadonnées HGE afin qu'elles puissent suivre le schéma et les permissions séparément.

Vous pouvez consulter la [documentation HGE](https://docs.hasura.io/1.0/graphql/manual/migrations/database-with-migrations.html) pour des instructions plus détaillées.

Une fois que vous avez tout configuré comme décrit dans le lien ci-dessus, vous pouvez simplement ajouter le dossier créé à votre dépôt de contrôle de version pour le code Laravel.

Pour exporter les métadonnées, exécutez la commande suivante dans le dossier créé par la commande `hasura init` dans les instructions de migration :

`hasura metadata export`

Puisque nous laissons Laravel gérer les migrations, évitez de faire des modifications de schéma via la console Hasura, afin que les migrations Laravel restent votre source de vérité sur le schéma.

C'est tout ! Nous avons maintenant un point de terminaison HGE sécurisé fonctionnant parfaitement avec l'authentification interne de Laravel. Allez de l'avant et écrivez du code !

[**_Hasura_**](https://goo.gl/fR68ep) _vous offre des API GraphQL instantanées en temps réel sur n'importe quelle base de données Postgres sans avoir à écrire de code backend._