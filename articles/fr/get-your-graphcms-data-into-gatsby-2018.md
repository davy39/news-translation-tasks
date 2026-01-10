---
title: Obtenez vos données GraphCMS dans Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-25T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/get-your-graphcms-data-into-gatsby-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-2.png
tags: []
seo_title: Obtenez vos données GraphCMS dans Gatsby
seo_desc: 'By Scott Spence

  Let''s set up Gatsby to pull data from GraphCMS.

  https://www.youtube.com/watch?v=S9JeASI5tck

  This will be a walk-through of setting up some basic data on the headless CMS, GraphCMS
  and then querying that data in Gatsby.

  1. Set up Graph...'
---

Par Scott Spence

Configurons Gatsby pour récupérer des données depuis GraphCMS.

%[https://www.youtube.com/watch?v=S9JeASI5tck]

Ce sera un guide pas à pas pour configurer des données de base sur le CMS headless, GraphCMS, puis interroger ces données dans Gatsby.

## 1. Configurer GraphCMS

Créez un compte GraphCMS à l'adresse [https://app.graphcms.com/signup](https://app.graphcms.com/signup) et sélectionnez le plan développeur.

## 2. Définir les données

Créez un nouveau projet et ajoutez-y des données à interroger.

Sélectionnez l'option **Créer un nouveau projet**, appelez-le comme vous le souhaitez. Dans cet exemple, il s'agira d'une liste de projets, je l'appelle donc _Liste de projets_.

Dans la barre latérale, sélectionnez **Schema** et créez un modèle, dans ce cas **Projet**. Dans le modèle de projet, nous aurons un _Titre_ et une _Description_.

Sélectionnez les champs dans le plateau de droite en cliquant sur l'onglet **CHAMPS** et faites-les glisser et déposez-les dans le modèle **Projet** que nous avons créé.

## 3. Configurer l'API publique de GraphCMS

Dans les paramètres de GraphCMS, définissez les **Permissions de l'API publique** sur **LECTURE**, faites défiler vers le bas jusqu'à **Endpoints** et copiez l'URL pour la configurer dans Gatsby.

C'est tout pour la configuration du CMS, maintenant, récupérons ces données dans notre frontend Gatsby !

## 4. Configurer Gatsby

Dans votre projet Gatsby, installez `gatsby-source-graphql` et configurez-le dans `gatsby-config.js`. La configuration devrait ressembler à ceci :

```js
{
  resolve: 'gatsby-source-graphql',
  options: {
    typeName: 'GRAPHCMS',
    fieldName: 'graphCmsData',
    url: 'https://api-euwest.graphcms.com/v1/projectid/master',
  }
},

```

Dans cet exemple, nous utilisons [codesandbox.io](https://codesandbox.io/dashboard/recent) comme éditeur de texte et le Gatsby Default Starter que vous obtenez lorsque vous sélectionnez Gatsby parmi les SERVER TEMPLATES disponibles dans [codesandbox.io](https://codesandbox.io/dashboard/recent).

## 5. Interroger les données dans Gatsby GraphiQL

Maintenant que le point de terminaison est configuré, nous pourrons interroger les données avec l'interface utilisateur GraphiQL de Gatsby. Nous pouvons façonner la requête que nous voulons utiliser pour afficher les données ici.

Dans l'aperçu de notre application dans [codesandbox.io](https://codesandbox.io/dashboard/recent), si vous ajoutez `___grapgql` à la fin de l'URL, cela ouvrira l'interface utilisateur Gatsby GraphiQL, où nous pouvons façonner les données que nous voulons interroger.

Si nous ouvrons quelques accolades `{}` et faisons Cmd+Espace, nous verrons les champs disponibles où nous pouvons sélectionner le champ `graphCmsData` que nous avons défini dans le plugin `gatsby-source-graphql`.

En sélectionnant les champs que nous avons créés dans GraphCMS, puis en exécutant la requête, nos données définies s'afficheront.

```js
{
  graphCmsData {
    projects {
      id
      status
      title
      description
    }
  }
}

```

## 6. Afficher les données

Utilisez l'export `graphql` de Gatsby pour interroger les données depuis le point de terminaison GraphCMS.

Dans `pages/index.js`, ajoutez l'export `graphql` aux imports `gatsby`.

```js
import { graphql, Link } from 'gatsby';

```

Tout en bas, définissez la requête :

```js
export const query = graphql`
  {
    graphCmsData {
      projects {
        id
        status
        title
        description
      }
    }
  }
`;

```

Vous pourrez alors accéder à la prop `data` dans le composant `IndexPage`. Nous devons déstructurer la prop `data` dans les arguments du composant :

```js
const IndexPage = ({ data }) => (

```

Maintenant, nous pouvons accéder aux `data` passées dans le composant. Nous avons juste besoin d'un moyen de les visualiser ! Heureusement pour nous, il existe un composant pratique de Wes Bos que nous pouvons utiliser appelé [Dump](https://github.com/wesbos/dump). Créez donc un nouveau composant `dump.js` dans `components`, puis importez-le dans le fichier `index.js` et ajoutez le composant pour voir ce qu'il y a dans les props :

```js
const IndexPage = ({ data }) => (
  <Layout>
    <h1>Salut tout le monde</h1>
    <Dump data={data} />
    <p>Bienvenue sur votre nouveau site Gatsby.</p>
    <p>Maintenant, allez construire quelque chose de grand.</p>
    <div style={{ maxWidth: '300px', marginBottom: '1.45rem' }}>
      <Image />
    </div>
    <Link to="/page-2/">Aller à la page 2</Link>
  </Layout>
);

```

Le résultat devrait être le même que celui de la requête Gatsby GraphiQL que nous avons créée :

```json
data ?{
 "graphCmsData": {
  "projects": [
   {
    "id": "cjoxa812txqoh0932hz0bs345",
    "status": "PUBLISHED",
    "title": "Project 1",
    "description": "Description 1"
   },
   {
    "id": "cjoxa8cctxqqj0932710u39db",
    "status": "PUBLISHED",
    "title": "Project 2",
    "description": "Description 2"
   },
   {
    "id": "cjoxa8pbqxqt309324z9bcddv",
    "status": "PUBLISHED",
    "title": "Project 3",
    "description": "Description 3"
   },
   {
    "id": "cjoxa959vxqvz0932g1jn5ss3",
    "status": "PUBLISHED",
    "title": "Project 4",
    "description": "Description 4"
   }
  ]
 }
}

```

### Merci d'avoir lu ?

Si j'ai oublié quelque chose ou s'il existe une meilleure façon de faire quelque chose, n'hésitez pas à me le faire savoir.

Suivez-moi sur [Twitter](https://twitter.com/spences10) ou posez-moi des questions sur [Ask Me Anything](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**