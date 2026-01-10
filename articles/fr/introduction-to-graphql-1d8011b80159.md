---
title: 4 raisons pour lesquelles vous devriez essayer GraphQL dès aujourd'hui
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-23T21:30:40.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-graphql-1d8011b80159
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9Lp6ioBWW7wD2EZTZ7Mh9w.png
tags:
- name: api
  slug: api
- name: data
  slug: data
- name: database
  slug: database
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
seo_title: 4 raisons pour lesquelles vous devriez essayer GraphQL dès aujourd'hui
seo_desc: 'By Guido Schmitz

  Even though I’ve been developing (RESTful) APIs for some years now, I’ve started
  to become a big fan of GraphQL.

  In this post I’ll introduce you to GraphQL and what kind of advantages you will
  have over REST. Let’s get started.


  Grap...'
---

Par Guido Schmitz

Même si je développe des API (RESTful) depuis quelques années maintenant, je suis devenu un grand fan de GraphQL.

Dans cet article, je vais vous présenter GraphQL et les avantages qu'il offre par rapport à REST. Commençons.

> GraphQL est un langage de requête de données et un runtime conçu et utilisé chez Facebook pour demander et fournir des données aux applications mobiles et web depuis 2012.

#### **Pourquoi GraphQL ?**

* Un seul endpoint pour accéder à vos données
* Récupérez uniquement les données dont votre client a besoin en une seule requête (flexibilité)
* Pas besoin de personnaliser les endpoints pour vos vues
* Pas de gestion de versions

Imaginez avoir une application mobile qui possède un fil d'actualités.

Souvent, vos données évoluent avec le temps, et vous devez introduire de nouvelles versions de votre API tout en maintenant les anciennes versions. Cela est nécessaire car d'autres utilisateurs dépendent encore des anciennes versions, où ces nouvelles modifications de données n'ont pas encore été implémentées.

L'un des avantages de GraphQL est qu'il permet une flexibilité dans votre modèle de données en utilisant le [Type System](http://graphql.org/docs/typesystem/). Le Type System est une description des types d'objets que votre serveur peut retourner.

Décrivons un type Person, en utilisant l'implémentation JavaScript de GraphQL :

#### **Le système d'introspection**

Une autre chose intéressante à propos de GraphQL est son [système d'introspection](http://graphql.org/docs/introspection/). Cela nous permet de demander à notre serveur quelles requêtes il prend en charge. Comparez cela à une documentation intégrée. Si vous ne savez pas quels types sont disponibles, vous pouvez facilement demander à GraphQL avec cette simple requête :

```
{  __schema {    types {      name    }  }}
```

Ainsi, lorsqu'un nouveau développeur iOS arrive et doit récupérer des données depuis votre API, vous pouvez facilement le diriger vers cette documentation. À mesure que votre schéma évolue, cela sera toujours à jour grâce au système de types. Cool, non ?

> Pour rendre cela encore meilleur, il existe une bibliothèque IDE en navigateur disponible pour explorer votre API appelée [**GraphiQL**](https://github.com/graphql/graphiql).

#### **Interroger les données du serveur GraphQL**

Après avoir défini vos modèles de données en utilisant le système de types, vous pouvez exécuter des requêtes sur votre serveur GraphQL. Avant de pouvoir exécuter des requêtes sur le serveur, vous devez définir un type de requête racine :

Maintenant, vous pouvez réellement exécuter la requête sur notre serveur :

```
query PersonQuery {  person {    firstName    lastName    friends {      firstName    }  }}
```

Ainsi, vous demandez au serveur le type Person et ses amis associés. Pas d'endpoint qui retourne un tableau de ressources contenant tous les champs et un paramètre de requête **?include**. **_Juste les données dont notre client a besoin_**.

Supposons que vous ayez également un type News. Dans GraphQL, vous pouvez récupérer plusieurs types à la fois. Cela signifie que vous pouvez obtenir différentes ressources avec une seule requête :

```
query HomepageQuery {  person {    firstName    lastName  }  news(limit: 10) {    title    excerpt    createdAt    person {      firstName      lastName    }  }}
```

Si vous voulez que votre serveur prenne en charge cette requête, vous devez étendre un peu votre type de requête racine (Note : Si vous utilisez ce code, n'oubliez pas de définir le type news ?) :

Après avoir créé notre type de requête racine, nous devons l'ajouter à notre schéma :

```
new GraphQLSchema({ query: Query });
```

#### **Mutating data to the GraphQL server**

Ainsi, avec le type **query**, nous pouvons récupérer des données du serveur. Nous pouvons également ajouter, mettre à jour ou supprimer des données avec GraphQL. Nous pouvons faire cela en exécutant une **mutation** sur le serveur et laisser le serveur retourner les valeurs de la mutation que nous avons exécutée. Voici un exemple :

```
mutation addPerson {  createPerson(    firstName: 'John',    lastName: 'Doe'  ) {    firstName    lastName  }}
```

Définir une mutation est similaire à définir un type de requête racine. La seule chose que nous devons faire est de l'ajouter à notre schéma. Ainsi, notre schéma mis à jour ressemble à ceci :

```
new GraphQLSchema({ query: Query, mutation: Mutation });
```

> Plus d'informations sur la mise en forme des requêtes peuvent être trouvées dans la [documentation officielle](http://graphql.org/docs/queries/).

J'espère vous avoir donné une compréhension de base de GraphQL. Si vous avez des questions, n'hésitez pas à me tweeter [**@guidsen**](https://twitter.com/guidsen).

Je envoie également des newsletters hebdomadaires à mes abonnés sur JavaScript et ReactJS.  
[**Abonnez-vous ici pour acquérir des connaissances en JavaScript**](https://www.getrevue.co/profile/guidsen)**.**

Oh, et cliquez sur le ? ci-dessous pour que d'autres personnes voient cet article ici sur Medium. Merci pour votre lecture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*prif7-04oPf8Dqo1gvSDsQ.gif)