---
title: Comment j'ai enfin réussi à faire fonctionner Netlify Functions, Firebase et
  GraphQL ensemble
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/netlify-functions-firebase-and-graphql-working-together-at-last
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/levi-guzman-zdSoe8za6Hs-unsplash.jpg
tags:
- name: Firebase
  slug: firebase
- name: GraphQL
  slug: graphql
- name: netlify-functions
  slug: netlify-functions
seo_title: Comment j'ai enfin réussi à faire fonctionner Netlify Functions, Firebase
  et GraphQL ensemble
seo_desc: 'By Jeff M Lowery

  In a previous post I confessed defeat in attempting to get an AWS Lambda GraphQL
  server to connect to a Firebase server. I didn’t give up right away, though, and
  a short time later found a different Node package to achieve what I cou...'
---

Par Jeff M Lowery

Dans un [précédent article](https://www.freecodecamp.org/news/you-cant-get-there-from-here-how-netlify-lambda-and-firebase-led-me-to-a-serverless-dead-end/), j'ai avoué avoir échoué dans ma tentative de connecter un serveur GraphQL [AWS Lambda](https://www.netlify.com/products/functions/) à un serveur [Firebase](https://firebase.google.com/docs). Je n'ai pas abandonné tout de suite, cependant, et peu de temps après, j'ai trouvé un [package Node différent](https://www.npmjs.com/package/firebase-admin) pour réaliser ce que je n'avais pas pu faire auparavant.

Pourquoi utiliser AWS Lambda pour héberger un serveur GraphQL ? La scalabilité serait la raison évidente, mais je l'ai fait pour apprendre.

# Et j'ai beaucoup appris

Surtout en ce qui concerne le déploiement. J'ai utilisé Netlify Functions pour gérer le déploiement des fonctions AWS Lambda et du client React qui les appelle. Il y avait plus à faire que ce que je pensais initialement.

Il existe plusieurs façons de déployer un projet en utilisant Netlify :

## zip-it-and-ship-it

Il s'agit d'un [utilitaire](https://github.com/netlify/zip-it-and-ship-it) qui fonctionne beaucoup comme [webpack](https://webpack.js.org/) : pour chaque fonction, il crée un fichier d'archive qui regroupe la fonction ainsi que ses dépendances. Comme webpack, il ne charge que les dépendances qui sont réellement nécessaires à la fonction.

Netlify attend par convention un dossier /functions. Lors de l'écriture de nouvelles fonctions, leur source se trouve au même niveau que tout module NodeJS dont elles ont besoin comme dépendances. Si vous ajoutez une nouvelle fonction qui a de nouvelles dépendances de module, alors elles vont dans le dossier node_modules (en utilisant `yarn add` ou `npm install --save`).

L'image suivante montre deux fonctions lambda ainsi qu'un seul dossier node_modules :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-05-at-3.45.48-pm.png)

Pour utiliser zip-it-and-ship-it, vous écrivez un simple programme JavaScript qui est appelé par le script de construction de package.json.

**zipIt.js**

```text
const { zipFunctions } = require('@netlify/zip-it-and-ship-it')
zipFunctions('functions', 'functions-dist')
```

Et cela serait invoqué comme suit :

**package.json**

```text
"build": "npm-run-all build:*",
"build:app": "react-scripts build",
"build:functions": "node ./zipFuncs.js",
```

Une fois construit, plusieurs fichiers .zip sont générés. Ces archives contiennent le code de la fonction ainsi qu'un dossier node_modules qui n'est pas l'original, mais contient uniquement les dépendances nécessaires à chaque fonction :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-05-at-3.52.56-pm.png)

## netlify-lambda

Ce mécanisme de déploiement est similaire au précédent, mais utilise **babel** et **webpack** pour effectuer ses tâches. Si vous êtes à l'aise et familier avec webpack, cette option de déploiement pourrait être faite pour vous.

## déploiement continu

L'option de déploiement continu est disponible si vous utilisez l'un des dépôts pris en charge (GitHub, GitLab ou Bitbucket). Une fois que vous poussez des modifications vers votre dépôt, Netlify est notifié et exécutera vos processus de construction, qui peuvent impliquer zip-it-and-ship-it ou netlify-lambda... mais vous avez également l'option de déployer des fonctions non regroupées vers votre dépôt, et [Netlify utilisera zip-it-and-ship-it](https://github.com/netlify/netlify-lambda/issues/142#issuecomment-483880089) en arrière-plan.

## Netlify CLI

Le Netlify CLI offre une autre façon de déployer, sans trop de tracas ou de mystère. Il existe deux options principales de déploiement :

* `netlify deploy` poussera le [projet local vers un serveur Netlify.](https://docs.netlify.com/cli/get-started/#manual-deploys) Vous devez d'abord invoquer l'étape de construction localement, cependant.
* `netlify dev` [crée un serveur local](https://github.com/netlify/cli/blob/master/docs/netlify-dev.md), ainsi qu'un proxy vers vos fonctions lambda, et lance l'application. Il ne nécessite **pas** d'étape de construction.

Il existe également un script pour vous aider à créer vos fonctions lambda : `netlify function:create`. Si vous utilisez cette méthode, vous obtiendrez une structure de dossier différente de celle montrée précédemment :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-05-at-4.11.21-pm.png)

Dans ce cas, chaque fonction a son propre dossier, ainsi qu'un fichier node_modules et package.json (plus d'autres non montrés, tels que les fichiers .lock). Similaire à ce qui serait dans les archives .zip que zip-it-and-ship-it crée.

Maintenant, si vous générez vos lambdas de cette manière, le déploiement continu ne fonctionnera pas, car **zip-it-and-ship-it** ne gère pas cette structure de dossier par lui-même. Vous pouvez mettre quelque chose comme ceci dans votre script de construction pour corriger le déploiement continu :

```text
"build": "npm-run-all build:*",
"build:app": "react-scripts build",
"build:functions": "yarn --cwd functions/func1 install",
"build:functions": "yarn --cwd functions/func2 install",
```

Ces étapes de construction installeront les dépendances nécessaires pour chaque lambda.

# L'exemple

Votre devoir est de configurer un [compte Netlify](https://www.netlify.com/) et un [compte Firebase](https://firebase.google.com/). L'application utilisera [Netlify Identity](https://docs.netlify.com/visitor-access/identity/#enable-identity-in-the-ui) pour se connecter au service Netlify. Vous devrez également récupérer un [fichier JSON de credentials Firebase](https://firebase.google.com/docs/admin/setup#add_firebase_to_your_app) et le placer quelque part dans votre projet (l'exemple utilise fake-creds.json, qui est **FAUX**, donc ne fonctionnera pas).

## À propos de l'application

En tant que geek, je construis une base de données d'ouvertures d'échecs. J'ai un livre d'ouvertures dans un fichier JSON, à partir duquel je vais charger la base de données. Dans cet exemple quelque peu artificiel, le livre est en réalité stocké avec la fonction lambda dans le dossier /functions/pgnfen (`netlify function:create pgnfen`), cependant, le chargement est déclenché par le client React via un appel de mutation GraphQL.

## Création de la fonction lambda

J'ai utilisé [apollo-server-lambda](https://github.com/apollographql/apollo-server/tree/master/packages/apollo-server-lambda) pour ajouter une interface GraphQL à la base de données Firestore. Pour communiquer avec Firestore, j'utilise [firebase-admin](https://www.npmjs.com/package/firebase-admin). Lorsque vous utilisez `netlify function:create` pour créer votre fonction, il vous demandera quel modèle utiliser ; dans ce cas, le bon choix est en bleu :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-05-at-4.39.37-pm.png)

En outre, j'ai ajouté quelques fonctions utilitaires et des schémas et résolveurs GraphQL de support.

### La fonction lambda

Le cœur de toute l'opération se trouve dans `/functions/pgnfen.js`. Il crée le serveur, se connecte à Firebase, effectue les déclarations GraphQL nécessaires et enfin invoque la fonction de gestionnaire qui reçoit les requêtes du client et les transmet à la base de données via les résolveurs GraphQL :

```js
/* eslint-disable no-unused-vars */
const apolloLambda = require('apollo-server-lambda');
const admin = require('firebase-admin');
const typeDefs = require('./schema.gql');
const { fetchGames, addOpenings } = require('./resolvers');

const {
  ApolloServer,
} = apolloLambda;

const credential = require('./fake-creds.json');


admin.initializeApp({
  credential: admin.credential.cert(credential),
});


const resolvers = {
  Query: {
    allGames: (root, args, context) => [], //TBD
  },
  Mutation: {
    addOpenings: async (root, args, context) => addOpenings(root, args, { ...context, admin }),
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

exports.handler = server.createHandler(
  {
    cors: {
      origin: '*',
      credentials: true,
    },
  },
);
```

### Le schéma

Le schéma définit l'API GraphQL. 'Nuf dit.

```text
const typeDefs = `

type Mutation {
  addOpenings(start: Int!, end: Int!) : Int! 
}
`

module.exports = typeDefs;
```

### Le résolveur

Cela résout la mutation GraphQL addOpenings en requêtes Firestore (par lots, dans ce cas), puis renvoie un compte des documents soumis (si succès) :

```text
const openings = require('./scid.js');


const addOpenings = async (_, { start, end }, { admin }) => {
  const db = admin.firestore();
  const batch = db.batch();
  const fens = db.collection('chess/openings/fen');
  const data = openings.slice(start, end);

  data.forEach((opening) => {
    const id = opening.fen.replace(/\//g, '$');
    const doc = fens.doc(id);
    batch.set(doc, opening);
  });

  await batch.commit();

  return data.length;
};

module.exports = {  addOpenings };
```

### Le livre d'ouvertures

La version JSON du livre d'ouvertures se compose d'un SCID (un identifiant d'ouverture basé sur [ECO](https://www.365chess.com/eco.php)), ainsi que le nom de l'ouverture et sa [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation). Chacun devient un document dans la base de données.

```text
/* eslint-disable comma-dangle */
module.exports = [
  {
    SCID: 'A00b',
    desc: '"Barnes Opening"',
    fen: 'rnbqkbnr/pppppppp/8/8/8/5P2/PPPPP1PP/RNBQKBNR b KQkq - 0 1'
  },
  {
    SCID: 'A00b',
    desc: '"Fried fox"',
    fen: 'rnbqkbnr/pppp1ppp/8/4p3/8/5P2/PPPPPKPP/RNBQ1BNR b kq - 1 2'
  },
  {
    SCID: 'A00c',
    desc: '"Kadas Opening"',
    fen: 'rnbqkbnr/pppppppp/8/8/7P/8/PPPPPPP1/RNBQKBNR b KQkq h3 0 1'
  },
  ...
];
```

## Création du client

J'utilise apollo-client dans l'application React. La manière la plus simple de le faire est create-react-app, puis ajouter [apollo-boost] pour obtenir un client squelettique rapidement. Ensuite, créez un composant React pour déclencher un appel à la lambda, en utilisant l'API GraphQL qu'elle fournit.

Le composant fournira les indices de début/fin du livre d'ouvertures à charger, et un bouton de soumission.

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-06-at-1.54.54-pm.png)

Voici une version condensée du code du composant :

```text
/* eslint-disable no-alert */
import React, { useState } from 'react';
import fetch from 'node-fetch';
import ApolloClient, { gql } from 'apollo-boost';

const styles = {
//...
};

const client = new ApolloClient({
  uri: '/.netlify/functions/pgnfen',  //l'URL de la lambda
  fetch,
});

export default () => {
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(5);

  const clickHandler = async () => {
    const mutation = gql`mutation {
      addOpenings(start: ${start}, end: ${end})
    }`;

    // eslint-disable-next-line no-console
    const count = await client.mutate({ mutation })
      .catch((e) => { window.alert(e); });
    // console.dir(count);
    window.alert(`${count.data.addOpenings} documents written`);
  };

  const startEndHandler = (evt) => {
    if (evt.target.name === 'start') {
      setStart(evt.target.value);
    } else {
      setEnd(evt.target.value);
    }
  };

  return (
//...
    <input type="button" onClick={clickHandler} value="Load Scids" />  Row start:&nbsp;&nbsp;
    <input name="start" type="number" step="5" style={styles.numInput} onChange={startEndHandler} value={start} />
Row end:&nbsp;&nbsp;
     <input name="end" type="number" step="5" style={styles.numInput} onChange={startEndHandler} value={end} />
//...
  );
};
```

Et la réponse de la mutation s'affichera dans une boîte d'alerte de fenêtre :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-06-at-11.50.01-am.png)

## Bonus ajouté !

Puisque j'ai utilisé apollo-server-lambda comme base pour la fonction Netlify, je peux accéder directement au point de terminaison du service via une URL et cela ouvrira GraphQL Playground :

![Image](https://www.jeffamabob.com/media/screenshot-2019-11-06-at-11.55.16-am.png)

Ici, je peux tester des requêtes et des mutations avant de les intégrer dans mon code client React.

**De plus**, l'invocation de `netlify dev` me donne un serveur à rechargement à chaud grâce à create-react-app, donc je peux voir le résultat des modifications de code en temps "réel".

C'est tout ! Voici un lien vers le [code source](https://github.com/JeffML/firebase-lambda2).