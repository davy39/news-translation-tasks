---
title: Comment nous avons construit l'API GraphQL de la Coupe du Monde 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T14:35:46.000Z'
originalURL: https://freecodecamp.org/news/building-the-2018-world-cup-graphql-api-fab40ccecb9e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*y_uooSFcpVZy14uv
tags:
- name: Grandstack
  slug: grandstack
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: World Cup
  slug: world-cup
seo_title: Comment nous avons construit l'API GraphQL de la Coupe du Monde 2018
seo_desc: 'By Michael Hunger

  After the second round of matches at World Cup 2018 got underway, we wanted to create
  an easy way for people to answer all their questions about the teams involved.


  TL;DR

  We’ve created a Neo4j backed GraphQL API for World Cup 2018....'
---

Par Michael Hunger

Après le deuxième tour de matchs de la Coupe du Monde 2018, nous voulions créer un **moyen facile** pour les gens de répondre à toutes leurs questions sur les équipes impliquées.

![Image](https://cdn-media-1.freecodecamp.org/images/0*y_uooSFcpVZy14uv)

### TL;DR

Nous avons créé une API GraphQL soutenue par Neo4j pour la Coupe du Monde 2018. Vous pouvez l'essayer [ici](https://worldcup-2018.now.sh/).

### Construire une API GraphQL soutenue par Neo4j

Nous avions déjà créé une [base de données avec _toutes les données de la Coupe du Monde_](https://medium.com/neo4j/world-cup-2018-graph-19fbac0a75db) pour que les gens puissent l'utiliser et l'interroger, mais nous voulions rendre les données accessibles aux personnes qui ne connaissent pas le langage de requête de Neo4j, Cypher.

**GraphQL à la rescousse !**

Avant d'en arriver là, examinons d'abord le modèle de graphe Neo4j que nous avons créé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zfRcG-bR_cMXR8cF)

Le nœud **WorldCup** se trouve au centre de notre graphe, et toutes les autres parties du modèle tournent autour de celui-ci. Nous avons un nœud WorldCup pour chaque tournoi.

Ensuite, nous avons le pays **hôte** qui est connecté au nœud WorldCup par une relation **HOSTED_BY**. Les **Matchs** appartiennent également à une **WorldCup**, et chaque **Pays** nomme une **Équipe de Joueurs** qui les représentera dans un tournoi de la Coupe du Monde.

Un joueur est connecté à un nœud **Apparition** pour chaque match auquel il participe, soit comme titulaire, soit comme remplaçant. S'il marque un **But**, le nœud Apparition sera connecté à ce nœud But.

### Le Kit de Démarrage GRANDstack

D'accord, assez parlé de Neo4j, revenons à GraphQL.

Le GRANDstack combine **G**raphQL, **R**eact, **A**pollo et la **B**ase de données **N**eo4j en un ensemble facile à utiliser pour construire rapidement des APIs et des applications. Il utilise le schéma GraphQL pour transpiler automatiquement les requêtes GraphQL en **une seule** requête Neo4j et est capable de générer automatiquement toutes les requêtes, mutations et champs à partir du schéma annoté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqKavloPXkMx3dNIkvK8Vw.png)
_Logo GRANDstack_

Nous avons utilisé le [kit de démarrage GRANDstack.io](https://github.com/grand-stack/grand-stack-starter/tree/master/api) pour créer une API GraphQL sur notre base de données Neo4j existante.

Il se compose de deux parties : un backend `api` et un frontend `ui`. Le backend sert l'API GraphQL ainsi qu'un GraphQL Playground (un navigateur et éditeur vraiment pratique pour les requêtes GraphQL), qui fournit également le schéma de données, la documentation et la complétion automatique.

Nous l'avons forké dans notre propre dépôt, puis fusionné dans une [branche `worldcup`](https://github.com/grand-stack/grand-stack-starter/tree/worldcup) pour que vous puissiez l'utiliser.

La première étape consiste à créer un **schéma GraphQL**. Vous pouvez voir ce que nous avons conçu ci-dessous, qui correspond étroitement à ce que nous avons dans notre Modèle de Graphe.

Un schéma minimal ressemble à ceci :

Nous l'avons considérablement étendu avec quelques extensions spécifiques à GRANDstack pour Neo4j afin d'avoir quelques mappages alternatifs, etc.

[**grand-stack/grand-stack-starter**](https://github.com/grand-stack/grand-stack-starter/blob/worldcup/api/src/graphql-schema.js)
[_grand-stack-starter - Projet de démarrage simple pour les applications full stack GRANDstack_github.com](https://github.com/grand-stack/grand-stack-starter/blob/worldcup/api/src/graphql-schema.js)

Une fois que nous avons défini le schéma, nous avons mis à jour notre fichier .env pour pointer vers notre base de données hébergée sur Neo4j Cloud (https://neo4j.com/cloud/).

```
NEO4J_URI=bolt://c27d992b.databases.neo4j.ioNEO4J_USER=worldcupNEO4J_PASSWORD=worldcup
```

Vous pouvez exécuter cela localement en exécutant `yarn && yarn start`. Cela lancera le Playground à l'adresse [http://localhost:4000](http://localhost:4000), où vous pourrez commencer à jouer avec quelques requêtes.

Nous pouvons écrire quelques requêtes pour trouver le meilleur joueur du monde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*A5TZARxOgWIqVRc4)
_GraphQL Playground_

Bien sûr, nous pouvons en apprendre beaucoup plus sur lui.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2Q2NxAJRiibIYumb)
_Résultat des détails sur Messi_

### Déploiement sur zeit.now

Maintenant, nous sommes prêts à déployer. Nous pourrions déployer notre service n'importe où hébergeant des applications Node.js, mais @Will.Lyon a recommandé [Zeit Now](https://zeit.co/now) — un service formidable et facile à utiliser pour héberger votre application, qui dispose d'un plan gratuit facile à utiliser pour les petits projets.

Nous installons simplement le service, puis exécutons la commande `now` dans notre répertoire pour déployer. Pour des URLs stables, vous pouvez donner un alias au projet avec un nom fixe.

Le serveur GraphQL est déployé à l'adresse [https://worldcup-2018.now.sh/](https://worldcup-2018.now.sh/) et est prêt à être utilisé maintenant. Examinons les types de requêtes que nous pouvons exécuter contre le jeu de données.

#### Portugal vs. Maroc

Alors que j'écris cet article, le **Portugal** joue contre le **Maroc**. Nous pouvons vérifier le dernier score en exécutant cette requête GraphQL dans le playground défini ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZQMuxQj0WEr0yiKC)
_Résultats Portugal vs. Maroc_

Le Portugal mène 1-0 pour le moment, et ce n'est pas une surprise d'apprendre que Cristiano Ronaldo était le buteur.

#### Qui est Cristiano ?

Si nous voulons en savoir plus sur Cristiano, nous pouvons également interroger les joueurs. Par exemple, la requête suivante nous montrera sa date de naissance et combien de buts il a marqués dans la Coupe du Monde, ainsi que combien de buts il a marqués cette fois-ci :

Il a donc marqué 4 buts à la Coupe du Monde 2018 et 7 au total, ce qui signifie qu'il a marqué plus de buts dans ce tournoi que dans les précédents combinés !

#### Score de l'Allemagne en 1990

Bien que l'Allemagne n'ait pas bien commencé cette Coupe du Monde, nous pouvons écrire une requête nostalgique pour découvrir le score de la finale de la Coupe du Monde 1990 :

#### Mauvais souvenirs en 1966 :(

Ou nous pourrions remonter à 1966, comme mon collègue Mark m'a forcé à le faire :

### Garder les données fraîches

La base de données est mise à jour via un travail Lambda toutes les quelques minutes pendant que les matchs sont joués, donc les données devraient être raisonnablement fraîches chaque fois que vous les interrogez.

![Image](https://cdn-media-1.freecodecamp.org/images/0*y1MqPFFZjGLJb6Mt)

### L'interface React

Le frontend `ui` est essentiellement une application React qui utilise Apollo Client pour interroger notre API et rendre les résultats dans des composants.

Veuillez noter que le code React actuel est vraiment laid et horrible. Nous vous laissons le défi de construire de belles applications web et/ou mobiles en utilisant l'**API GraphQL de la Coupe du Monde**. :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1dH26XFHo70f9Ns1CEgkyA.png)
_mon (laid) écran de coupe du monde_

Bien sûr, vous pouvez également utiliser Vue ou Angular ou d'autres frameworks UI que vous aimez.

Il se connecte à l'URL fournie dans le fichier `.env`, où nous mettons soit notre `http://localhost:4000` local, soit notre URI now.sh.

```
REACT_APP_GRAPHQL_URI=https://worldcup-2018.now.sh/
```

Encore une fois, une seule commande `now` déploie également notre UI. Dans notre cas, nous n'en avons pas besoin, mais Zeit now offre un support si vous avez des identifiants secrets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SA6pQOO4Bb50zPeu0dO4oQ.jpeg)

### Hackathon GRANDstack

Heureusement, le [Hackathon GRANDstack](https://blog.grandstack.io/announcing-the-grandstack-online-hackathon-for-graphql-europe-2018-7d256ebf68e1) **est toujours en cours pour recueillir de grandes idées** et il y a des prix vraiment cool pour vos soumissions.

> Merci beaucoup à mon collègue [Mark Needham](https://www.freecodecamp.org/news/building-the-2018-world-cup-graphql-api-fab40ccecb9e/undefined) pour tout le travail acharné de mise en place des données et du modèle.