---
title: Comment créer une application de vote en temps réel full-stack avec Hasura
  et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-29T19:07:27.000Z'
originalURL: https://freecodecamp.org/news/build-a-full-stack-real-time-voting-app-with-hasura-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-rodnae-productions-7581108.jpg
tags:
- name: application
  slug: application
- name: full stack
  slug: full-stack
- name: React
  slug: react
seo_title: Comment créer une application de vote en temps réel full-stack avec Hasura
  et React
seo_desc: 'By Catalin Pit

  This article will teach you how to build a voting application that displays the
  poll results in real-time. Each time someone votes, the application updates automatically
  and shows the new results.

  Even though you will build a full-stac...'
---

Par Catalin Pit

Cet article vous apprendra à créer une application de vote qui affiche les résultats du sondage en temps réel. Chaque fois que quelqu'un vote, l'application se met à jour automatiquement et affiche les nouveaux résultats.

Même si vous allez construire une application full-stack, vous n'écrirez aucun code backend grâce à Hasura !

![Capture d'écran de l'application de sondage en temps réel construite avec Hasura et React](https://cdn.hashnode.com/res/hashnode/image/upload/v1646303998900/GysSg52mZ.png)

L'application utilisera :

* Hasura GraphQL Engine pour le backend
* React et Apollo pour le frontend

[Démo en direct](https://realtime-poll.demo.hasura.io/) | [Explorateur Backend](https://cloud.hasura.io/public/graphiql?endpoint=https%3A%2F%2Frealtime-poll.hasura.app/v1/graphql) | [Dépôt GitHub](https://github.com/catalinpit/graphql-engine/tree/master/community/sample-apps/realtime-poll)

## Pourquoi ces technologies ?

Avant d'aller plus loin, parlons des technologies que nous utiliserons pour la pile de l'application.

### Hasura GraphQL Engine

[Hasura](https://hasura.io) est un [GraphQL Engine](https://github.com/hasura/graphql-engine) open source qui vous permet de créer une API GraphQL instantanée et en temps réel sans écrire de code backend du tout.

Vous vous demandez peut-être comment cela fonctionne. Hasura se connecte à votre base de données et génère automatiquement l'API en fonction de vos tables et vues de base de données. Vous obtenez des éléments tels que le schéma GraphQL et les résolveurs (Resolvers) prêts à l'emploi.

Par conséquent, la raison du choix d'Hasura est d'accélérer le processus de création de l'API GraphQL en temps réel. Hasura se charge de tout le travail lourd, afin que nous puissions nous concentrer sur d'autres choses.

### React et Apollo Client

React est l'un des Frameworks JavaScript les plus populaires avec une excellente communauté. Il est également polyvalent, vous permettant de créer des applications web et mobiles.

Apollo Client est un client GraphQL complet qui vous permet de créer des composants d'interface utilisateur et de récupérer des données via GraphQL de manière transparente. Apollo Client est également l'un des clients GraphQL les plus populaires.

Ensemble, React et Apollo Client forment une combinaison puissante qui répond aux exigences de l'application de vote en temps réel.

## Modélisation des données

La première étape consiste à déterminer la structure de la base de données. La base de données contiendra les tables suivantes :

* user – un _user_ est une personne qui vote au sondage
* poll – le _poll_ représente la question (_ex. quel est votre framework préféré ?_)
* option – une _option_ est une option de sondage que les gens peuvent choisir
* vote – un _vote_ est le lien entre un utilisateur et une option de sondage. Il représente le vote de l'utilisateur.

![drawSQL-export-2022-03-04_10_53.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646384055424/h8aci5wK0.png)

La figure ci-dessus illustre les tables et les relations de la base de données.

Il existe une relation `one-to-many` (un-à-plusieurs) entre `user` et `vote`. Un utilisateur peut voter plusieurs fois, mais un vote ne peut appartenir qu'à un seul utilisateur.

Le `poll` et l' `option` ont une relation `one-to-many`, ce qui signifie qu'un sondage peut avoir plusieurs options, mais qu'une option n'appartient qu'à un seul sondage.

Enfin, il existe une relation `one-to-many` entre les tables `option` et `vote`. Cela signifie que vous ne pouvez choisir qu'une seule option. Un vote représente une option.

La base de données possède également deux vues – `online_users` et `poll_results`. Elles affichent le nombre d'utilisateurs en ligne et les résultats du sondage.

## Mise en œuvre du backend avec Hasura

Vous pouvez utiliser Hasura de deux manières :

* localement à l'aide de Docker ([voir le guide](https://hasura.io/docs/latest/graphql/core/getting-started/docker-simple.html#docker-simple))
* dans le cloud à l'aide de Hasura Cloud ([voir le guide](https://hasura.io/docs/latest/graphql/cloud/getting-started/index.html#cloud-getting-started))

Il convient de mentionner que Hasura Cloud offre également des fonctionnalités avancées de performance, de sécurité et de surveillance. Voici quelques-unes des choses qu'il propose :

* mise à l'échelle automatique de votre application
* surveillance et traçage
* limitation du débit (rate limiting)

Ce ne sont là que trois avantages, mais il y en a plus. Si vous voulez les consulter, vous pouvez le faire [ici](https://hasura.io/cloud/).

Ce tutoriel utilise la version cloud, mais vous pouvez suivre le tutoriel même si vous utilisez Hasura localement. Ceci étant dit, commençons à construire le backend.

### Configuration de la base de données

Après avoir configuré le compte, allez sur le tableau de bord du projet et cliquez sur l'onglet "DATA".

![Screenshot 2022-03-03 at 15.04.47.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646391279001/BCP-EtIN2.png)

Dans l'onglet "DATA", vous pouvez vous connecter à une base de données existante ou en créer une nouvelle sur Heroku. Nous allons créer une nouvelle base de données, alors cliquez sur l'option "Create Heroku Database".

Après cela, cliquez sur "Create Database" et vous devriez avoir une base de données PostgreSQL opérationnelle en quelques secondes.

### Tables de la base de données

L'étape suivante consiste à créer les tables de la base de données. Allez dans votre base de données nouvellement créée et cliquez sur le bouton "Create Table".

![Screenshot 2022-03-04 at 14.21.48.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646396538475/13G3LsTT9.png)

Cliquer sur le bouton ouvre une nouvelle page où vous pouvez créer une nouvelle table.

#### Table User

La table "user" possède les colonnes suivantes :

* id (clé primaire) – UUID, `gen_random_uuid()`, Unique
* created_at – Timestamp, `now()`
* online_ping – Boolean, Nullable
* last_seen_at – Timestamp, Nullable

La figure illustre les colonnes de la table, les types et d'autres configurations.

![Screenshot 2022-03-04 at 14.27.36.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646398900732/dI-bt0NnQ.png)

Avant d'enregistrer la table, définissez la colonne `id` comme Clé Primaire, comme indiqué dans la figure ci-dessus.

Après cela, faites défiler vers le bas et appuyez sur le bouton "Add Table" pour l'enregistrer. Vous pouvez suivre le même processus pour créer les autres tables.

#### Table Poll

La table "poll" possède les colonnes suivantes :

* id (clé primaire) – UUID, `gen_random_uuid()`, Unique
* created_at – Timestamp, `now()`
* created_by – UUID, nullable
* question – text

#### Table Option

La table "option" possède les colonnes suivantes :

* id (clé primaire) – UUID, `gen_random_uuid()`, Unique
* poll_id – UUID
* text – text

#### Table Vote

La table "vote" possède les colonnes suivantes :

* id (clé primaire) – UUID, `gen_random_uuid()`, Unique
* created_by_user_id – UUID
* option_id – UUID
* created_at – Timestamp, `now()`

### Vues de la base de données

Nous utiliserons des vues pour les résultats du sondage et les utilisateurs en ligne car elles nous permettent de réutiliser des requêtes complexes. Une vue est le résultat d'une requête sur une ou plusieurs tables.

Vous pouvez considérer une vue comme la sauvegarde d'une requête complexe en lui donnant un nom afin de pouvoir la réutiliser. Une vue est appelée une "table virtuelle" et vous pouvez l'interroger comme vous le feriez avec une table normale.

#### Résultats du sondage

L'affichage des résultats du sondage nécessite d'effectuer des jointures de base de données sur les tables `poll`, `option` et `vote`.

La première jointure de base de données renvoie tous les enregistrements de la table `vote` et les enregistrements correspondants de la table `option`. Autrement dit, elle renvoie chaque vote et son option de sondage associée.

La deuxième jointure renvoie tous les enregistrements de la table `option` et les enregistrements correspondants de la table `poll`. Autrement dit, elle renvoie toutes les options et le sondage auquel elles appartiennent.

Après cela, la vue compte tous les enregistrements renvoyés et les renvoie sous le nom de "votes".

```sql
CREATE
OR REPLACE VIEW "public"."poll_results" AS
SELECT
  poll.id AS poll_id,
  o.option_id,
  count(*) AS votes
FROM
  (
    (
      SELECT
        vote.option_id,
        option.poll_id,
        option.text
      FROM
        (
          vote
          LEFT JOIN option ON ((option.id = vote.option_id))
        )
    ) o
    LEFT JOIN poll ON ((poll.id = o.poll_id))
  )
GROUP BY
  poll.question,
  o.option_id,
  poll.id;
```

Où ajoutez-vous ces vues de base de données ?

Pour ajouter les vues de base de données, allez dans l'onglet "DATA" et cliquez sur l'option "SQL". La page "SQL" vous permet d'exécuter des instructions SQL directement sur la base de données.

![Screenshot 2022-03-10 at 14.08.23.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646914117338/RcIcFniVe.png)

Après cela, ajoutez le code SQL et cliquez sur le bouton "Run!". S'il n'y a pas d'erreurs, vous devriez pouvoir accéder et utiliser la vue nouvellement créée.

#### Utilisateurs en ligne

Pour le nombre d'utilisateurs en ligne, nous pouvons également utiliser une vue.

La table `users` possède une propriété `last_seen_at` qui assure le suivi de la dernière connexion des utilisateurs. Nous pouvons utiliser cette propriété pour déterminer le nombre d'utilisateurs connectés (en ligne).

```sql
CREATE
OR REPLACE VIEW "public"."online_users" AS
SELECT
  count(*) AS count
FROM
  "user"
WHERE
  (
    "user".last_seen_at > (now() - '00:00:15' :: interval)
  );
```

La vue ci-dessus compte le nombre d'utilisateurs vus au cours des 15 dernières secondes. S'ils se sont connectés pendant les 15 dernières secondes, nous les comptons comme des utilisateurs en ligne.

### Relations

La dernière étape de la mise en œuvre du backend consiste à configurer les relations entre les tables. Avec Hasura, vous pouvez créer des relations entre les tables de deux manières :

1. en utilisant des contraintes de clé étrangère (foreign key constraints)
2. manuellement (lorsqu'il n'est pas possible d'utiliser des contraintes de clé étrangère)

Par la suite, nous créerons des relations en ajoutant des contraintes de clé étrangère. Si vous souhaitez en savoir plus sur les relations, la documentation comporte une section complète sur les [table relationships](https://hasura.io/docs/latest/graphql/core/databases/postgres/schema/table-relationships/index.html).

#### User – Vote

Naviguez vers "Modify" dans la table `vote` et cliquez sur le bouton indiquant "Add a foreign key".

![Screenshot 2022-03-10 at 16.05.35.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646921160263/stfCBtYDb.png)

Configurons la colonne `created_by_user_id` comme clé étrangère pour la colonne `id` dans la table `users`.

L'image illustre le processus d'ajout de clés étrangères.

![Screenshot 2022-03-10 at 16.07.09.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646921268139/YzXpsQC1h.png)

En suivant le même processus, ajoutez la colonne `option_id` comme clé étrangère pour la colonne `id` dans la table `option`.

La valeur du champ "Reference Table" doit être `option`. La valeur pour "From" doit être `option_id`, tandis que la valeur pour "To" doit être `id`.

Puisque vous avez ajouté les clés étrangères, Hasura suggère automatiquement des relations potentielles. Si vous allez dans l'onglet "Relationships", vous devriez voir les relations suggérées.

Lorsque vous cliquez sur le bouton "Add", vous avez la possibilité de nommer votre relation. Vous pouvez soit laisser le nom par défaut, soit en utiliser un personnalisé.

![Screenshot 2022-03-10 at 16.15.49.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646921792095/fXUhw7ppq.png)

Enregistrez les relations en appuyant sur le bouton "Add" et vous avez terminé !

#### Poll – Option

Allez dans la table `option` et ajoutez `poll_id` comme clé étrangère pour la colonne `id` dans la table `poll`.

* **Reference Table** – poll
* **From** – poll_id
* **To** – id

Après l'avoir enregistré, allez dans l'onglet "Relationships" et n'acceptez que la "Object Relationship" suggérée.

#### Option – Vote

Lorsque vous avez configuré les clés étrangères pour la relation "User – Vote" plus tôt, vous avez ajouté la colonne `option_id` comme clé étrangère pour la colonne `id` dans la table `option`.

Cela signifie qu'il ne reste plus qu'à aller dans l'onglet "Relationships" de la table `poll` et à accepter l' "Array Relationship" suggérée.

#### Vue Poll Results

Pour la vue `poll_results`, nous devons définir manuellement les relations avec les tables `option` et `poll`. En regardant la vue, vous pouvez voir que nous avons les clés étrangères `poll_id` et `option_id`.

Allez dans l'onglet "Relationships" de `poll_results` pour ajouter les relations manuellement. Une fois sur place, cliquez sur le bouton indiquant "Configure".

Les relations entre `poll_results` et les tables `option` et `poll` sont des relations d'objet (object relationships).

Configurez la relation entre `poll_results` et `option` comme indiqué dans la figure ci-dessous.

![Screenshot 2022-03-16 at 14.05.57.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1647432404572/wVAaTy93w.png)

La relation entre `poll_results` et `poll` est configurée de manière similaire. Ajoutez les informations suivantes :

* **Relationship Type** – Object Relationship
* **Relationship Name** – poll
* **Reference Schema** – public
* **Reference Table** – poll
* **From** – poll_id
* **To** – id

Enregistrez-les et vous en avez fini avec les relations !

### L'API GraphQL est prête

Vous disposez maintenant d'une API GraphQL entièrement fonctionnelle sans avoir écrit une seule ligne de code. Si vous allez dans l'API Explorer de la console Hasura, vous pouvez insérer, modifier et supprimer des données.

Imaginez construire la même application manuellement – ce serait assez fastidieux et chronophage.

![Screenshot 2022-03-10 at 16.57.13.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1646924258746/MRS3Us3SX.png)

L'étape suivante consiste à mettre en œuvre la partie frontend.

## Mise en œuvre du frontend

La première étape de la mise en œuvre du frontend consiste à créer et à initialiser le projet. Allez dans votre dossier préféré et exécutez :

```
npx create-react-app realtime-poll
```

Une fois l'installation terminée, allez dans le dossier `realtime-poll` et installez les dépendances requises :

```
npm i react-bootstrap react-google-charts @apollo/client graphql graphql-ws
```

Le paquet `react-bootstrap` nous permettra de construire l'interface de l'application avec Bootstrap, tandis que `react-google-charts` nous aidera à afficher les résultats du sondage sous forme de graphique. Les autres paquets nous permettront d'utiliser l'API GraphQL que nous avons construite précédemment.

Avant d'aller plus loin, supprimez `setupTests.js`, `reportWebVitals.js` et `logo.svg` du dossier `src`. Après cela, supprimez toutes les références à ces fichiers dans `index.js` et `App.js`.

### Configuration du client GraphQL avec Apollo

L'application de vote utilise les abonnements GraphQL (Subscriptions) pour afficher les résultats du sondage en temps réel. Lorsque les gens votent, les résultats du sondage se mettent à jour automatiquement, nous devons donc les afficher sans forcer les gens à rafraîchir la page.

Une souscription GraphQL est une opération qui nous permet de le faire en s'abonnant aux événements du serveur. Lorsque les données (_résultats du sondage_) sont mises à jour (_quelqu'un vote_), nous recevons les mises à jour en temps réel.

Puisque les données sont poussées vers le client chaque fois qu'il y a une mise à jour, nous avons besoin d'une connexion spéciale. Les abonnements GraphQL utilisent les WebSockets, ce qui nous permet de maintenir une connexion ouverte entre le serveur et le client.

_Note : Cet article aborde brièvement les Subscriptions. Pour plus d'informations, consultez la documentation pour [en savoir plus sur les GraphQL Subscriptions](https://hasura.io/learn/graphql/intro-graphql/graphql-subscriptions/)._

Commençons à implémenter le client GraphQL avec Apollo. La première étape consiste à créer un nouveau fichier dans le dossier `src` :

```
📂 realtime-poll
 └ 📁 node_modules
   📁 package-lock.json
   📁 package.json
   📁 public
   📁 README.md
   📂 src
    └ apollo.js
```

Ouvrez le fichier nouvellement créé, `apollo.js`, et importez les paquets suivants :

```javascript
import { ApolloClient, HttpLink, InMemoryCache, split } from "@apollo/client";
import { GraphQLWsLink } from '@apollo/client/link/subscriptions';
import { createClient } from "graphql-ws";
import { getMainDefinition } from "@apollo/client/utilities";
```

Après cela, stockez le point de terminaison (endpoint) de votre application dans une variable séparée. Remplacez la valeur "realtime-poll-example.hasura.app" par l'URL de votre application.

Comme nous l'avons mentionné précédemment, les abonnements GraphQL utilisent le protocole WebSocket, nous avons donc besoin de deux liens. Nous utiliserons un lien, `httpURL`, pour les requêtes (queries) et les mutations, et l'autre, `wsURI`, pour les abonnements.

```javascript
const GRAPHQL_ENDPOINT = "realtime-poll-example.hasura.app";

const scheme = (proto) =>
  window.location.protocol === "https:" ? `${proto}s` : proto;

const wsURI = `${scheme("ws")}://${GRAPHQL_ENDPOINT}/v1/graphql`;
const httpURL = `${scheme("https")}://${GRAPHQL_ENDPOINT}/v1/graphql`;
```

Nous avons également une fonction (splitter) qui détermine quel lien utiliser. Si l'opération est une requête ou une mutation, elle utilise le lien HTTP. Sinon, elle utilise le lien WebSocket.

```javascript
const splitter = ({ query }) => {
  const { kind, operation } = getMainDefinition(query) || {};
  const isSubscription =
    kind === "OperationDefinition" && operation === "subscription";
  return isSubscription;
};
```

`GraphQLWsLink` nous permet d'exécuter les abonnements. Le constructeur `createClient` reçoit le lien WebSocket et des options de connexion supplémentaires en paramètres. Ensuite, nous passons la valeur renvoyée par `createClient` au constructeur `GraphQLWsLink`.

```javascript
const cache = new InMemoryCache();
const options = { reconnect: true };

const wsLink = new GraphQLWsLink(createClient({ url: wsURI, connectionParams: { options } }));
```

Il nous reste à :

* configurer le lien HTTP pour les requêtes et les mutations
* utiliser la fonction splitter
* créer l'ApolloClient

La fonction `split` prend la fonction splitter que nous avons écrite précédemment et les deux liens comme arguments. Nous passons le lien renvoyé par la fonction "split" comme argument au constructeur `ApolloClient`.

```javascript
const httpLink = new HttpLink({ uri: httpURL });
const link = split(splitter, wsLink, httpLink);
const client = new ApolloClient({ link, cache });
```

Enfin, nous exportons le client afin de pouvoir l'utiliser pour les requêtes, les mutations et les abonnements.

```javascript
export default client;
```

Vous pouvez voir le code complet dans [ce gist](https://gist.github.com/catalinpit/839c22b0a430c5b690a3d2d409115674).

### Opérations GraphQL

Nous utiliserons quelques [requêtes GraphQL](https://hasura.io/learn/graphql/intro-graphql/graphql-queries/), [mutations](https://hasura.io/learn/graphql/intro-graphql/graphql-mutations/) et [abonnements](https://hasura.io/learn/graphql/intro-graphql/graphql-subscriptions/) dans l'application. Ils seront également affichés sur la page d'accueil de l'application.

![Screenshot 2022-03-15 at 14.39.13.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1647347965793/tZyz3XUhX.png)

Par conséquent, nous les stockerons dans un fichier séparé et les importerons si nécessaire.

Allez dans le dossier `src` et créez un nouveau fichier nommé `GraphQL.jsx`.

```
📂 realtime-poll
 └ 📁 node_modules
   📁 package-lock.json
   📁 package.json
   📁 public
   📁 README.md
   📂 src
    └ GraphQL.jsx
```

Ouvrez `GraphQL.jsx` et ajoutez les imports suivants :

```jsx
import gql from "graphql-tag";
import React from "react";
import { Card } from "react-bootstrap";
```

Nous avons besoin de `gql` pour que les requêtes, mutations et abonnements GraphQL puissent être analysés dans l'AST GraphQL standard. Nous avons également besoin de React et du composant Card car nous allons rendre les chaînes de requête, mutation et abonnement GraphQL sur la page.

#### Obtenir les sondages

L'application a besoin d'une requête pour récupérer tous les sondages de la base de données.

```jsx
const QUERY_GET_POLL = gql`
  query {
    poll(limit: 10) {
      id
      question
      options(order_by: { id: desc }) {
        id
        text
      }
    }
  }
`;
```

La requête ci-dessus renvoie 10 sondages avec leur id, leur question et leurs options (réponses). Les options sont triées par ordre décroissant par l'id.

#### Voter

Puisqu'il s'agit d'un sondage, il devrait y avoir un moyen de choisir une réponse et de voter.

```jsx
const MUTATION_VOTE = gql`
  mutation vote($optionId: uuid!, $userId: uuid!) {
    insert_vote(
      objects: [{ option_id: $optionId, created_by_user_id: $userId }]
    ) {
      returning {
        id
      }
    }
  }
`;
```

La mutation ci-dessus insère un nouveau vote dans la base de données.

#### Résultats du sondage en temps réel

L'application de vote affiche les résultats en temps réel à l'aide de cet abonnement :

```jsx
const SUBSCRIPTION_RESULT = gql`
  subscription getResult($pollId: uuid!) {
    poll_results(
      order_by: { option_id: desc }
      where: { poll_id: { _eq: $pollId } }
    ) {
      option_id
      option {
        id
        text
      }
      votes
    }
  }
`;
```

Ce sont les opérations GraphQL utilisées par l'application pour afficher les sondages, permettre aux utilisateurs de voter et afficher les résultats en temps réel.

Le fichier contient également :

* deux mutations pour créer un nouvel utilisateur et marquer l'utilisateur comme étant en ligne
* un abonnement pour afficher le nombre d'utilisateurs en ligne en temps réel

Vous pouvez trouver le code complet pour `GraphQL.jsx` dans ce [gist](https://gist.github.com/catalinpit/11d9e23b12878749b7eb44a22b047169).

### Mise en œuvre du sondage

L'étape suivante consiste à mettre en œuvre le sondage. Créez un nouveau fichier `Poll.jsx` dans le dossier `src`.

```
📂 realtime-poll
 └ 📁 node_modules
   📁 package-lock.json
   📁 package.json
   📁 public
   📁 README.md
   📂 src
    └ Poll.jsx
```

Le fichier `Poll.jsx` contiendra deux composants :

* `PollQuestion` qui représente le sondage lui-même et gère le vote
* `Poll` qui affiche la question du sondage et les réponses

Ouvrez le fichier nouvellement créé et ajoutez les imports suivants :

```javascript
import { useMutation, useQuery } from "@apollo/client";
import React, { useEffect, useState } from "react";
import { Button, Form } from "react-bootstrap";
import { Error, Loading } from "./Components";
import { MUTATION_VOTE, QUERY_GET_POLL } from "./GraphQL";
import { Result } from "./Result";
```

La première ligne importe les deux hooks d'Apollo Client qui vous permettent d'exécuter des requêtes et des mutations. Nous importons React et ses deux hooks par défaut sur la deuxième ligne, tandis que sur la troisième ligne, nous importons deux composants Bootstrap.

Les trois dernières lignes importent des composants React personnalisés, des requêtes GraphQL et des mutations. Ils n'existent pas encore, mais nous les implémenterons plus tard.

#### Composant PollQuestion

L'étape suivante consiste à implémenter le composant pour la question du sondage. Le composant "PollQuestion" gère le processus de vote. Après vos imports, écrivez le code suivant :

```jsx
const PollQuestion = ({ poll, userId }) => {
    const defaultState = {
      optionId: "",
      pollId: poll.id,
      voteBtnText: "🗳 Vote",
      voteBtnStyle: "primary",
    };
    const [state, setState] = useState(defaultState);
    const [vote, { data, loading, error }] = useMutation(MUTATION_VOTE);
};
```

Dans le code ci-dessus, nous définissons l'état par défaut du sondage. Lorsqu'une personne visite le sondage pour la première fois, aucune réponse ne doit être sélectionnée. De plus, le bouton doit afficher "🗳 Vote".

L'image illustre à quoi ressemble le sondage avec l'état par défaut.

![Screenshot 2022-03-15 at 09.48.04.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1647330497362/WhUxYq-qx.png)

Nous utilisons également le hook `useMutation` pour que les gens puissent voter. Le hook renvoie un tableau contenant deux éléments. Le premier élément (`vote`) est une fonction que nous pouvons appeler pour exécuter la mutation. Le second est un objet que nous pouvons déstructurer davantage.

Nous devons mettre à jour l' `optionId` chaque fois qu'un utilisateur sélectionne une réponse. Par exemple, si l'utilisateur sélectionne "Vue" dans ce sondage, nous définissons l' `optionId` sur l'id de cette option.

```jsx
const handleOptionChange = (e) => {
    const optionId = e.currentTarget.value;
    setState((prev) => ({ ...prev, optionId }));
};
```

Passons à l'écriture de la logique pour gérer la soumission d'un vote. Tout d'abord, nous devons nous assurer que les utilisateurs ne peuvent pas soumettre un formulaire vide. Si l'utilisateur n'a pas sélectionné de réponse, le bouton devient jaune et invite l'utilisateur à choisir une réponse et à réessayer.

![Screenshot 2022-03-15 at 10.34.43.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1647333432909/GPH4Vn4Hj.png)

Si une réponse est sélectionnée, nous appelons la fonction `vote` renvoyée par le hook `useMutation`. Nous passons l'id de la réponse sélectionnée et l'id de l'utilisateur qui a voté.

```jsx
const handlesubmitVote = (e) => {
    e.preventDefault();

    if (!state.optionId) {
      setState({
        voteBtnText: "✋ Sélectionnez une option et réessayez",
        voteBtnStyle: "warning",
      });
      return;
    }

    setState({
      voteBtnText: "🗳️ Soumission en cours",
      voteBtnStyle: "info",
    });

    vote({
      variables: {
        optionId: state.optionId,
        userId,
      },
    });
};
```

Si le vote réussit, nous mettons à jour l'état du bouton en conséquence. Après 5 secondes, nous réinitialisons l'état du bouton afin que les utilisateurs puissent voter à nouveau. S'il y a une erreur, le bouton le soulignera.

Le hook `useEffect` s'exécute chaque fois que la valeur de `data` ou `error` change.

```jsx
useEffect(() => {
    if (data) {
      setState({
        voteBtnText: "👍 Terminé",
        voteBtnStyle: "success",
      });

      // Ré-autoriser le vote après 5 secondes
      let timer = setTimeout(() => {
        setState({
          voteBtnText: "🗳️ Vote",
          voteBtnStyle: "primary",
        });
      }, 5000);

      return () => clearTimeout(timer);
    }

    if (error) {
      setState({
        voteBtnText: "Erreur 😟 Réessayez",
        voteBtnStyle: "danger",
      });
    }
}, [data, error]);
```

Enfin, nous rendons le formulaire, les options du sondage et le bouton de vote.

```jsx
return (
    <div className="textLeft">
      <h3>{poll.question}</h3>
      <Form
        className="pollForm textLeft"
        onSubmit={(e) => {
          handlesubmitVote(e);
        }}
      >
        {poll.options.map(({ id, text }) => (
          <Form.Check
            custom
            type="radio"
            name="voteCandidate"
            id={id}
            key={id}
            value={id}
            label={text}
            onChange={handleOptionChange}
          />
        ))}
        <Button
          className="voteBtn info"
          variant={state.voteBtnStyle}
          type="submit"
        >
          {state.voteBtnText}
        </Button>
      </Form>
    </div>
);
```

Nous en avons terminé avec le composant `PollQuestion`. Vous pouvez trouver le code complet pour `PollQuestion` dans ce [gist](https://gist.github.com/catalinpit/74a64bcb9a6af13364ea1ebf8aa61729).

#### Composant Poll

Le composant `Poll` affiche la question du sondage et les résultats. Commençons par appeler le hook `useQuery` avec la chaîne de requête GraphQL qui renvoie tous les sondages.

```jsx
export const Poll = ({ userId }) => {
    const { data, loading, error } = useQuery(QUERY_GET_POLL);
  
    if (loading) return <Loading />;
    if (error) return <Error message={error.message} />;
};
```

La propriété `data` contiendra un tableau de sondages si la requête réussit. Une fois que nous avons le tableau, nous le parcourons avec map et rendons les sondages et leurs réponses correspondantes.

```jsx
return (
    <div className="container">
      {data?.poll.map((poll) => (
        <div key={poll.id} className="pollWrapper wd100">
          <div className="displayFlex">
            <div className="col-md-4 pollSlider">
              <PollQuestion poll={poll} userId={userId} />
            </div>
            <div className="col-md-8 pollresult">
              <Result pollId={poll.id} />
            </div>
          </div>
        </div>
      ))}
    </div>
);
```

Si vous regardez le code ci-dessus, vous pouvez observer que nous utilisons le composant `Result`, qui n'existe pas encore. Dans la prochaine étape, nous allons faire justement cela !

Vous pouvez trouver le code complet du fichier `Poll` dans ce [gist](https://gist.github.com/catalinpit/f8015f660984f7f1997e3b8caedf6085).

### Composant Result

Commençons par créer le fichier `Result.jsx` dans le dossier `src`.

```
📂 realtime-poll
 └ 📁 node_modules
   📁 package-lock.json
   📁 package.json
   📁 public
   📁 README.md
   📂 src
    └ Result.jsx
```

Ouvrez le fichier et ajoutez les imports suivants :

```jsx
import { useSubscription } from "@apollo/client";
import React from "react";
import { Chart } from "react-google-charts";
import { Error, Loading } from "./Components";
import { SUBSCRIPTION_RESULT } from "./GraphQL";
```

La première ligne importe le hook `useSubscription`, que nous utiliserons pour afficher les résultats du sondage en temps réel. Sur la deuxième ligne, nous importons React et sur la troisième ligne, nous importons le composant Chart. Les deux dernières lignes importent deux composants personnalisés et la chaîne d'abonnement GraphQL.

Écrivez le code suivant après les imports :

```jsx
export const Result = ({ pollId }) => {
    const { data, loading, error } = useSubscription(SUBSCRIPTION_RESULT, {
      variables: { pollId },
    });
  
    const hasResults = data?.poll_results.length > 0;
    
    if (loading) return <Loading />;
    if (error) return <Error message={error.message} />;
  
    return (
      <div>
        {hasResults ? <PollChart data={data?.poll_results} /> : <p>Pas de résultat</p>}
      </div>
    );
};
```

Le composant "Result" prend un ID de sondage comme prop afin de pouvoir afficher les résultats pour ce sondage spécifique.

Dans la première ligne, nous appelons le hook `useSubscription` avec l'ID du sondage. Si l'appel réussit, la propriété `data` contiendra un tableau avec les résultats du sondage. De plus, tous les nouveaux votes seront reflétés dans la propriété `data`. Le tableau avec les résultats du sondage se met à jour chaque fois qu'un nouveau vote est soumis.

Avant d'afficher les résultats du sondage, nous vérifions s'il y a des résultats. S'il y en a, nous affichons les résultats. Sinon, nous affichons une chaîne "Pas de résultat".

Si vous regardez le code, vous pouvez voir que nous utilisons un composant `PollChart`. Vous pouvez trouver le code pour `PollChart` et le code complet pour `Result.jsx` dans ce [gist](https://gist.github.com/catalinpit/ede866d28e62928f58904447d9d4ba36).

L'article se concentre sur les parties essentielles de la mise en œuvre du frontend. Il souligne comment mettre en œuvre les parties les plus délicates. Vous pouvez parcourir le code complet de l'application dans ce [dépôt GitHub](https://github.com/catalinpit/graphql-engine/tree/master/community/sample-apps/realtime-poll).

## Conclusion

À ce stade, vous disposez d'une application full-stack sans avoir écrit de code backend. Hasura fournit une interface utilisateur utile que vous pouvez utiliser pour construire votre API. Par conséquent, il simplifie et raccourcit le processus de création d'une API GraphQL.

Vous pouvez :

* voir une [démo en direct](https://realtime-poll.demo.hasura.io/) de l'application
* explorer le [backend](https://cloud.hasura.io/public/graphiql?endpoint=https%3A%2F%2Frealtime-poll.hasura.app/v1/graphql)
* parcourir le code complet dans ce [dépôt GitHub](https://github.com/catalinpit/graphql-engine/tree/master/community/sample-apps/realtime-poll)

Si cela vous intéresse, j'ai également écrit sur la [création d'un backend e-commerce](https://catalins.tech/hasura-ecommerce-backend) avec un minimum de code.

Merci de m'avoir lu ! Si vous voulez rester en contact, connectons-nous sur Twitter [@catalinmpit](https://twitter.com/intent/follow?screen_name=catalinmpit). Je publie également des articles régulièrement sur mon blog [catalins.tech](https://catalins.tech) si vous souhaitez lire plus de contenu de ma part.