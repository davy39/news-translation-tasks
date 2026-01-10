---
title: Le cours intensif React + GraphQL 2020
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-06-30T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-react-graphql-2020-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/React
seo_title: Le cours intensif React + GraphQL 2020
---

GraphQL-2020-Crash-Course-Cover--Large--1.png
tags:
- name: '2020'
  slug: '2020'
- name: Apollo GraphQL
  slug: apollo
- name: apollo client
  slug: apollo-client
- name: débutant
  slug: debutant
- name: GraphQL
  slug: graphql
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "Vous avez beaucoup entendu parler de l'utilisation de React avec GraphQL mais vous ne savez pas comment les combiner pour créer des applications incroyables ? Dans ce cours intensif, vous apprendrez à faire exactement cela en construisant une application de blog social complète. \nEn un après-midi, vous acquerrez les compétences de base..."
---

Avez-vous beaucoup entendu parler de l'utilisation de React avec GraphQL mais vous ne savez pas comment les combiner pour créer des applications incroyables ? Dans ce cours intensif, vous apprendrez à faire exactement cela en construisant une application de blog social complète. 

En un après-midi, vous acquerrez les compétences de base pour construire vos propres projets React et GraphQL.

## Pourquoi devriez-vous apprendre React avec GraphQL ?

React est la bibliothèque de référence pour créer des expériences d'application incroyables avec JavaScript. GraphQL, d'autre part, est un outil qui nous donne un moyen plus simple et plus direct de récupérer et de modifier nos données.

Ces données pourraient provenir d'une base de données standard (comme nous l'utiliserons dans notre application) ou, comme les frameworks React tels que Gatsby l'ont rendu possible, même de fichiers statiques tels que des fichiers markdown. Peu importe comment elles sont stockées, GraphQL améliore le travail avec les données dans nos applications.

Nous verrons comment exploiter la puissance de React et GraphQL en créant une application de blog social de A à Z, où vous pourrez créer, lire, modifier et supprimer des articles.

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/o51wpa2tgx9k85p8rse8.gif)](https://bit.ly/2020-react-graphql)

Vous pouvez [cliquer ici](https://courses.reedbarger.com/p/2020-react-graphql) pour accéder au cours.

## Quels outils allons-nous utiliser ?️

Ce cours intensif est destiné aux développeurs qui sont familiers avec React (y compris les React Hooks de base, tels que `useState` et `useEffect`), mais qui ne connaissent pas encore GraphQL.

Des connaissances de base en React sont supposées, mais aucune connaissance en GraphQL n'est requise. Nous couvrirons tous les concepts de base de GraphQL dont vous avez besoin en cours de route.

Tout au long du cours, nous utiliserons les technologies suivantes pour créer notre application :

* **React** (pour construire notre interface utilisateur)
* **GraphQL** (pour obtenir et modifier des données de manière déclarative)
* **Apollo Client** (pour nous permettre d'utiliser React et GraphQL ensemble)
* **Hasura** (pour créer et gérer notre API GraphQL + base de données)

Pour couronner le tout, nous utiliserons l'IDE en ligne CodeSandbox. Cela nous permettra de coder toute notre application dans le navigateur en temps réel, sans avoir besoin de créer des fichiers, des dossiers ou d'installer des dépendances nous-mêmes.

## Créer une API GraphQL de zéro

Pour commencer à travailler avec GraphQL, nous verrons comment créer une API GraphQL complète de zéro qui communiquera avec notre base de données. 

Heureusement, en utilisant le service (gratuit) **Hasura**, ce processus est très simple et direct. En quelques secondes, nous verrons comment créer et déployer une API GraphQL complète sur le web, connectée à une base de données Postgres qui se chargera de stocker les données de notre application.

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/ss4wp2tt4ernoe5ukea8.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445637)*Cliquez pour regarder cette leçon*

## Se familiariser avec GraphQL

Dans la deuxième leçon, nous verrons comment écrire en langage GraphQL en utilisant la console intégrée de notre API appelée **GraphiQL**. 

Tout d'abord, nous créerons une table dans notre base de données pour toutes les données de nos articles. Après quoi, Hasura créera automatiquement les **requêtes** (queries) et les **mutations** dont nous avons besoin, qui sont les noms des opérations GraphQL nous permettant de récupérer et de modifier des données dans notre base de données. 

Tout au long de cette leçon, nous nous familiariserons avec l'exécution de requêtes et de mutations dans GraphiQL, ce qui nous permettra de récupérer des ensembles complets d'articles et des articles individuels, ainsi que de créer, mettre à jour et supprimer nos données d'articles individuels. 

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/bo5twcv0hhal7xtj1ksw.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445640)*Cliquez pour regarder cette leçon*

## Connecter React à notre API GraphQL avec Apollo Client

Maintenant que nous sommes à l'aise avec l'utilisation de GraphQL et que nous comprenons ses fonctionnalités de base, nous verrons comment le connecter à notre client React. 

La façon dont nous connectons notre application React avec l'API GraphQL que nous avons créée se fait via une bibliothèque appelée **Apollo**. Nous verrons comment configurer le client Apollo en fournissant l'endpoint GraphQL qui pointe vers notre API, comme ceci :

```javascript
import ApolloClient from "apollo-boost";

const client = new ApolloClient({
  uri: "https://react-graphql.herokuapp.com/v1/graphql"
});
```

Avec notre client nouvellement créé, nous avons la possibilité d'exécuter n'importe quelle opération GraphQL via React. Pour ce faire, cependant, nous devons passer notre client à l'ensemble de nos composants React. Nous le faisons à l'aide du fournisseur Apollo (Apollo Provider), comme vous le voyez ci-dessous :

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/iplsbo37x2oujohn7ulc.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445642)*Cliquez pour regarder cette leçon*

### Récupérer des articles avec useQuery

Après avoir configuré notre client, nous verrons comment exécuter différentes opérations GraphQL avec lui, en utilisant des hooks React spéciaux fournis avec le package `@apollo/react-hooks`.

Le hook qui nous permet de requêter des données avec GraphQL s'appelle `useQuery`. Avec lui, nous verrons d'abord comment récupérer et afficher toutes les données de nos articles sur notre page d'accueil.

De plus, nous apprendrons comment écrire nos requêtes GraphQL directement dans nos fichiers JavaScript à l'aide d'une fonction spéciale appelée `gql`.

```jsx
import React from "react";
import { useQuery } from "@apollo/react-hooks";
import { gql } from "apollo-boost";

export const GET_POSTS = gql`
  query getPosts {
    posts {
      id
      title
      body
      createdAt
    }
  }
`;

function App() {
  const { data, loading } = useQuery(GET_POSTS);

  if (loading) return <div>Chargement...</div>;
  if (data.posts.length === 0) return <Empty />;

  return (
    <>
      <header className={classes.header}>
        <h2 className={classes.h2}>Tous les articles</h2>
        <Link to="/new" className={classes.newPost}>
          Nouvel article
        </Link>
      </header>
      {data.posts.map(post => (
        <Post key={post.id} post={post} />
      ))}
    </>
  );
}
```

## Créer et modifier de nouveaux articles avec useMutation

Après cela, we verrons comment créer de nouveaux articles avec le hook `useMutation`. Pour ce faire, nous examinerons comment travailler avec les variables GraphQL pour passer à notre mutation des valeurs dynamiques qui changeront à chaque exécution. 

Ensuite, nous verrons comment modifier nos articles. Pour ce faire, nous devrons récupérer un article individuel et l'afficher dans notre formulaire, afin que notre utilisateur puisse apporter des modifications aux données. Ensuite, nous devrons exécuter une mutation qui effectuera la mise à jour, basée sur l'ID de l'article. 

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/n9swv8j0qr962spqxhkx.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445643)*Cliquez pour regarder cette leçon*

## Gérer le chargement et les erreurs

Dans la leçon suivante, nous aborderons certains modèles essentiels pour gérer le processus de chargement de nos données. 

Il est important de le faire lorsque nous exécutons une mutation, pour nous assurer de ne pas soumettre nos formulaires plusieurs fois pendant que notre mutation est en cours d'exécution. Nous verrons également comment gérer les erreurs au cas où notre mutation ne serait pas exécutée correctement. 

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/548ekws3psm3cbfpqy8e.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445638)*Cliquez pour regarder cette leçon*

## Supprimer des articles

Enfin, nous verrons comment supprimer des articles de notre application. Tout d'abord, nous confirmerons que l'utilisateur souhaite réellement supprimer l'article qu'il a créé, puis nous effectuerons la mutation. 

De plus, nous verrons comment mettre à jour notre UI en réponse aux mutations avec la fonction pratique `refetch` qu'Apollo nous donne. Elle nous permettra de ré-exécuter une requête à la demande. Dans ce cas, nous le ferons après que la mutation de suppression a été effectuée avec succès.

[![Cliquez pour accéder au cours](https://dev-to-uploads.s3.amazonaws.com/i/ojjd4jjxuh0h7p1048ck.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445639)*Cliquez pour regarder cette leçon*

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le découvrir par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir quand j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*