---
title: Démarrez rapidement sur IBM Cloud avec VueJS, FeathersJS et GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-16T11:39:26.000Z'
originalURL: https://freecodecamp.org/news/a-rapid-start-on-ibm-cloud-with-vuejs-feathersjs-graphql-1-2-cd2b76606d66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f47Cf5dkbqfW3XdFGleQ_w.png
tags:
- name: Cloud
  slug: cloud
- name: IBM
  slug: ibm
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Démarrez rapidement sur IBM Cloud avec VueJS, FeathersJS et GraphQL
seo_desc: 'By Thomas Reinecke

  Are you looking for a rapid start on playing around with IBMs Cloud? What about
  taking this opportunity and combining it with some of the latest and greatest technologies
  for the Web VueJS, FeathersJS and GraphQL? Well then this is...'
---

Par Thomas Reinecke

Vous cherchez à démarrer rapidement avec le Cloud d'IBM ? Que diriez-vous de saisir cette opportunité et de la combiner avec certaines des technologies les plus récentes et les plus performantes pour le Web : VueJS, FeathersJS et GraphQL ? Alors, cet article est un incontournable pour vous, afin de décoller en moins d'une heure.

![Image](https://cdn-media-1.freecodecamp.org/images/w4pRjRmdxL65HzbJwT7aQoSl9q1hsK2F5Zo4)

**Ce que nous allons faire :**

* Aperçu de l'application
* créer un nouveau dépôt git sur GitHub
* initialiser l'application frontend basée sur Vue CLI
* initialiser l'application backend basée sur FeathersJS CLI
* ajouter des capacités GraphQL au backend
* tester l'API GraphQL et publier/souscrire
* ajouter des dépendances à l'application frontend existante
* créer une SPA simple qui appelle un backend GraphQL
* déploiement sur le Cloud d'IBM

### Aperçu de l'application

![Image](https://cdn-media-1.freecodecamp.org/images/hkO5W-QuFFqay74i6Tua3j2LPbs7ZyeKjOou)

### Créer un nouveau dépôt git sur GitHub

Si vous n'avez pas encore de compte GitHub, allez sur github.com et créez-en un. Créez-vous un nouveau dépôt appelé « VueAndIBMsCloud » (ou tout autre nom que vous souhaitez). En supposant que vous savez bien utiliser une console, utilisez le code suivant pour créer votre premier commit de projet :

```bash
mkdir VueAndIBMsCloud
cd VueAndIBMsCloud
echo "# VueAndIBMsCloud" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/<yourRepo>/VueAndIBMsCloud.git
git push -u origin master
```

### Initialiser l'application frontend basée sur Vue CLI

Si vous avez besoin de plus de détails pour installer Vue CLI, consultez cet article et revenez.

[**Installation - Vue.js**](https://vuejs.org/v2/guide/installation.html)  
[_Vue.js - The Progressive JavaScript Framework_](https://vuejs.org/v2/guide/installation.html)  
[vuejs.org](https://vuejs.org/v2/guide/installation.html)

Utilisez vue-cli pour initialiser un projet "frontend" basé sur une application Web progressive (PWA) :

```bash
npm install -g vue-cli
vue init pwa frontend

? Project name frontend
? Project short name: fewer than 12 characters to not be truncated on homescreens (default: same as name)
? Project description A Vue.js project
? Author thomasreinecke <thomas.reinecke@de.ibm.com>
? Vue build runtime
? Install vue-router? Yes
? Use ESLint to lint your code? No
? Setup unit tests with Karma + Mocha? No
? Setup e2e tests with Nightwatch? No
```

Maintenant, compilez le projet et exécutez-le pour la première fois (au lieu de "npm", je recommande d'utiliser "yarn") :

```bash
cd frontend
yarn
yarn dev
```

Votre application frontend est en cours d'exécution à l'adresse [http://localhost:8080](http://localhost:8080)

![Image](https://cdn-media-1.freecodecamp.org/images/XxEi5MzErMTo6APfzLGiZqwCvqmld8XhQA67)

Félicitations, vous venez de créer l'application frontend basée sur VueJs.

### Initialiser l'application backend basée sur FeathersJS CLI

![Image](https://cdn-media-1.freecodecamp.org/images/rHH7NIYxUwbv6rxsDJx4YS9mC2v7Yrv9vCFM)

Utilisez la CLI FeathersJS pour initialiser le projet backend. Si vous avez besoin de plus de détails sur FeatherJS CLI, utilisez le lien suivant et revenez :

[**feathersjs/cli**](https://github.com/feathersjs/cli)  
[_cli - The command line interface for scaffolding Feathers applications_](https://github.com/feathersjs/cli)  
[github.com](https://github.com/feathersjs/cli)

```bash
npm install -g @feathersjs/cli
mkdir backend
cd backend
feathers generate app

? Project name backend
? Description
? What folder should the source files live in? src
? Which package manager are you using (has to be installed globally)? Yarn
? What type of API are you making? REST, Realtime via Socket.io

yarn start
```

Votre application backend est en cours d'exécution à l'adresse [http://localhost:3030/](http://localhost:3030/)

### Ajouter des capacités GraphQL au backend

Ouvrez Visual Studio Code (ou votre IDE préféré) > Ouvrir… > pointez-le vers le dossier **VueAndIBMsCloud**.

Ouvrez **backend/src/index.html** et remplacez ce qui s'y trouve par le code suivant :

```js
/* eslint-disable no-console */
const logger = require('winston');
const app = require('./app');
const port = app.get('port');

const createSubscriptionServer = app.get('createSubscriptionServer');

// créer le serveur de subscription et l'associer au serveur
const server = app.listen(port, () => createSubscriptionServer(server));

process.on('unhandledRejection', (reason, p) =>
  logger.error('Unhandled Rejection at: Promise ', p, reason)
);

server.on('listening', () =>
  logger.info('Feathers application started on http://%s:%d',  
  app.get('host'), port)
);
```

Dans le fichier **backend/package.json**, ajoutez les dépendances supplémentaires suivantes pour GraphQL :

```json
"express-session": "1.15.6",
"graphql": "0.12.3",
"graphql-subscriptions": "0.5.6",
"graphql-tools": "2.18.0",
"subscriptions-transport-ws": "0.9.5",
"apollo-server-express": "1.3.2",
```

Exécutez "**yarn**" sur la ligne de commande pour intégrer les bibliothèques supplémentaires dans votre projet backend. Nous sommes maintenant prêts à créer le service Graphql avec un peu plus d'aide de la CLI feather :

```bash
feathers generate service

? What kind of service is it? A custom service
? What is the name of the service? graphql
? Which path should the service be registered on? /graphql
```

Vous remarquerez qu'un nouveau répertoire a été créé : services/graphql.

Nous allons créer le service GraphQL un peu différemment du modèle de service featherJS. Allez-y et supprimez les fichiers **graphql.hooks.js** et **graphql.class.js**.

```bash
rm services/graphql/graphql.hooks.js
rm services/graphql/graphql.class.js
```

Mettez à jour **services/graphql/graphql.service.js** avec le code suivant :

```js
const { graphqlExpress, graphiqlExpress } = require('apollo-server-express');
const { execute, subscribe } = require('graphql');
const { SubscriptionServer } = require('subscriptions-transport-ws');
const { makeExecutableSchema } = require('graphql-tools');
const TypeDefinitions = require('./graphql.typeDefs');
const Resolvers = require('./graphql.resolvers');

module.exports = function () {
  const app = this;
  const port = app.get('port');
  const schema = makeExecutableSchema({
    typeDefs: TypeDefinitions,
    resolvers: Resolvers.call(app)
  });
    
  // fournir un endpoint à graphql pour la bibliothèque cliente apollo graphql
  app.use('/graphql', graphqlExpress((req) => {
    return {
      schema,
      context: {}
    };
  }));
    
  // fournir un endpoint à graphiql : le module explorateur d'API
  app.use('/graphiql', graphiqlExpress({
    endpointURL: '/graphql',
    subscriptionsEndpoint: `ws://localhost:${port}/subscriptions`
  }));
    
  // définir le serveur API ici
  app.set('createSubscriptionServer', function
    createSubscriptionServer(server) {
    return new SubscriptionServer({
      execute, subscribe, schema,
      onConnect: () => { console.log('Client Connected'); },
      onDisconnect: () => { console.log('Client Disconnected'); }
    },
    {
      server, path: '/subscriptions',
    });
  });
};
```

Maintenant, créez les typedef et resolvers GraphQL : créez deux nouveaux fichiers sous **services/graphql** : **graphql.typeDefs.js** et **graphql.resolvers.js** et ajoutez le code suivant :

#### graphql.resolvers.js

```js
const { PubSub } = require('graphql-subscriptions');
const pubsub = new PubSub();
const ITEM_ADDED = 'ITEM_ADDED';

module.exports = function () {
  return {
    Query: {
      Welcome (root, { id }, context) {
        return 'Welcome to VueAndIBMsCLoud example';
      },
      Items (root, { id }, context) {
        return [
          {
            id: 1,
            title: 'Item 1',
            status: 'open',
            created_at: new Date()
          },
          {
            id: 2,
            title: 'Item 2',
            status: 'closed',
            created_at: new Date()
          }
        ];
      }
    },
    Mutation: {
      addItem(root, { id, title, status }, context) {
        const item = {
          id,
          title,
          status,
          created_at: new Date()
        };
        pubsub.publish(ITEM_ADDED, { itemAdded: item });
        return item;
      },
    },
    Subscription: {
      itemAdded: {
        subscribe: () => pubsub.asyncIterator(ITEM_ADDED),
      }
    }
  };
};
```

#### graphql.typeDefs.js

```js
const typeDefinitions = `
  type Item {
    id: ID!
    title: String
    status: String
    created_at: String
  }

  type Query {
    Welcome: String,
    Items: [Item]
  }

  type Mutation {
    addItem(id: ID!, title: String!, status: String): Item
  }

  type Subscription {
    itemAdded: Item
  }

  schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
  }
`;

module.exports = typeDefinitions;
```

Presque terminé. Ajoutons un script de démarrage à **package.json** dans la section 'scripts' :

```json
"dev": "NODE_ENV=development node src/",
```

Et maintenant, exécutez 'yarn dev'. Vous devriez voir un message comme :  
_info: Feathers application started on [http://localhost:3030](http://localhost:3030)_

### Tester l'API GraphQL et publier/souscrire

Essayez graphiQL comme module explorateur d'API [http://localhost:3030/graphiql](http://localhost:3030/graphiql) et exécutez un premier test comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Cij0N9AVsxCBewYTxbI445VIuQHYLelT9ykO)

Félicitations, vous avez inclus une API GraphQL dans votre projet !

Maintenant, testons une récupération de données plus complexe :

![Image](https://cdn-media-1.freecodecamp.org/images/7nPlyOR4GDe-bogMKrszWYNauZrXu8Jfyadd)

Et maintenant, testons la souscription. Ouvrez graphiql dans une deuxième fenêtre de navigateur et configurez la souscription comme ceci et appuyez sur le bouton "play" :

![Image](https://cdn-media-1.freecodecamp.org/images/fq3SMdiiBnB5qc0BW7Ve7hR6dT67UbcUb5hS)

Retournez à la première fenêtre du navigateur graphiql, entrez la mutation suivante qui vous permet d'ajouter un élément au tableau Items. Puisque nous avons configuré publier/souscrire, nous nous attendons à pousser les changements vers le tableau Items à tous les abonnés :

![Image](https://cdn-media-1.freecodecamp.org/images/WtwyidSbX4k3jBM-Wuzc8u4AUh85GzEgf85F)

Placez les deux fenêtres du navigateur côte à côte et appuyez sur "Play" dans la première fenêtre. Vous remarquerez que le serveur backend va pousser le changement de données dans votre deuxième fenêtre graphiql :

![Image](https://cdn-media-1.freecodecamp.org/images/WZdJuyvtG2hKqyr7U9rGD2sVZhGiM04ZQqzM)

N'est-ce pas génial ? Félicitations, vous avez également configuré publier/souscrire basé sur graphiql dans votre projet.

### Ajouter des dépendances à l'application frontend

Dans le fichier **frontend/package.json**, ajoutez les dépendances supplémentaires suivantes pour inclure Graphql, ApolloJS et la prise en charge des souscriptions (via Websockets) :

```json
"dependencies": {
  "apollo-cache-inmemory": "1.1.5",
  "apollo-client": "2.2.0",
  "apollo-link": "1.0.7",
  "apollo-link-http": "1.3.2",
  "apollo-link-ws": "1.0.4",
  "apollo-utilities": "1.0.4",
  "graphql": "0.12.3",
  "graphql-tag": "2.6.1",
  "subscriptions-transport-ws": "0.9.5",
  "vue": "^2.5.2",
  "vue-apollo": "3.0.0-alpha.3",
  "vue-router": "^3.0.1"
}
```

Exécutez "**yarn**" pour intégrer les dépendances dans votre projet frontend.

```bash
cd frontend
yarn
```

Modifiez **frontend/main.js** et remplacez le code par le suivant :

```js
import Vue from 'vue'
import App from './App'
import router from './router'

import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { split } from 'apollo-link'
import { WebSocketLink } from 'apollo-link-ws'
import { getMainDefinition } from 'apollo-utilities'

import VueApollo from 'vue-apollo'

// ajouter des identifiants de ressource unifiés pour Dev et Prod (IBM Cloud)
const uris = {
  dev: 'localhost:3030',
  prod: 'VueAndIBMsCloud.mybluemix.net'
}

// configurer httpLink en fonction de l'environnement
const httpLink = new HttpLink({
  uri: (window.location.hostname === 'localhost') ? `http://${uris.dev}/graphql` : `https://${uris.prod}/graphql`
  })

// configurer le lien web socket en fonction de l'environnement
const wsLink = new WebSocketLink({
  uri: (window.location.hostname === 'localhost') ? `ws://${uris.dev}/subscriptions` : `wss://${uris.prod}/subscriptions`,
  options: {
    reconnect: true
  }
})

const link = split(
  ({ query }) => {
    const { kind, operation } = getMainDefinition(query)
    return kind === 'OperationDefinition' && operation === 'subscription'
  },
  wsLink,
  httpLink
)

// définir le client apollo
const apolloClient = new ApolloClient({
  link,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  apolloProvider,
  router,
  render: h => h(App)
})
```

Cela préparera votre application frontend à utiliser ApolloClient comme bibliothèque pour fournir la prise en charge des requêtes, mutations et souscriptions GraphQL. Dans l'objet **uris**, remplacez **VueAndIBMsCloud.mybluemix.net** par votre cible de déploiement productive de l'application backend.

### Ajouter une interface utilisateur appelant le backend GraphQL

Dans vos sources frontend, ouvrez **src/App.vue** et remplacez-le par le code suivant :

```js
<template>
  <div id="app">
    <h1>{{ welcome }}</h1>
    <ul>
      <li v-for="(item) of items" v-bind:key="item.id">{{item.title + ' - ' + item.status}}</li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'app',
  data () {
    return {
      welcome: '',
      items: []
    }
  },
  mounted () {
    this.$apollo.query({
      query: gql`query {
        Welcome
        Items {
          id
          title
          status
        }
      }`
    }).then(({data}) => {
      this.welcome = data.Welcome
      this.items = data.Items
    }).catch((error) => {
      console.error(error)
    })
  },
}
</script>

<style>
body {
  margin: 50px;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

main {
  text-align: center;
  margin-top: 40px;
}

header {
  margin: 0;
  height: 56px;
  padding: 0 16px 0 24px;
  background-color: #35495E;
  color: #ffffff;
}

header span {
  display: block;
  position: relative;
  font-size: 20px;
  line-height: 1;
  letter-spacing: .02em;
  font-weight: 400;
  box-sizing: border-box;
  padding-top: 16px;
}
</style>
```

Enregistrez et exécutez **yarn dev** pour le démarrer. Vous devriez maintenant voir la nouvelle page d'accueil de votre application frontend (qui n'a pas encore l'air super excitante, mais c'est la première fois que nous voyons des données de votre backend graphQL dans votre frontend — n'est-ce pas génial ?)

![Image](https://cdn-media-1.freecodecamp.org/images/kJq1yDrUsyjTXkCruNi4mTFqNsuIztSUHNbF)

Maintenant que nous avons notre intégration e2e entre notre frontend et le backend graphQL, poussons-le vers le cloud d'IBM et exécutons-le là-bas.

### Préparer IBM Cloud pour le déploiement

* configurer Bluemix CLI sur votre bureau : [https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html#getting-started](https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html#getting-started)
* connectez-vous au cloud d'IBM : **bx login**
* définissez la cible et le contexte de l'espace dans IBM Cloud de manière interactive (allez sur [https://console.bluemix.net/dashboard/apps/](https://console.bluemix.net/dashboard/apps/) pour inspecter vos options) : **bx target — cf**

Vous devriez maintenant voir ceci :

```
API endpoint:     <votre endpoint> (<version de l'API>)
Region:           <votre région>
User:             <votre nom d'utilisateur>
Account:          <votre compte>
Resource group:   default
Org:              <votre organisation>
Space:            <votre espace>
```

Vous avez maintenant défini la portée de déploiement pour vos deux applications.

### Déploiement du backend sur Bluemix

Dans le projet backend, créez un nouveau fichier manifest.yml et entrez le contenu suivant :

```yml
applications:
  - path: .
    memory: 1024M
    instances: 1
    domain: eu-de.mybluemix.net
    name: vueAndIbmsCloud-api
    host: vueAndIbmsCloud-api
    disk_quota: 1024M
```

Ajoutez le script de déploiement suivant à package.json dans la section "scripts" :

```json
"deploy": "bx cf push vueAndIbmsCloud-api"
```

(Vous devez changer ce nom d'application pour le rendre unique, par exemple, ajoutez un index de votre choix dans manifest.yml et package.json.)

#### **Installer BlueMix CLI**

[https://console.bluemix.net/docs/cli/index.html](https://console.bluemix.net/docs/cli/index.html)  
[https://developer.ibm.com/courses/labs/1-install-bluemix-command-line-interface-cli-dwc020/](https://developer.ibm.com/courses/labs/1-install-bluemix-command-line-interface-cli-dwc020/)

Exécutez **yarn deploy**, et cela déployera votre application backend sur IBM Cloud.

### Déploiement du frontend sur Bluemix

Nous déployons l'application frontend basée sur un serveur nginx, qui offre de meilleures performances (en temps de réponse et en débit) qu'un serveur node.

Selon le nom que vous avez choisi comme cible de déploiement backend, assurez-vous qu'il est correctement reflété dans **frontend/src/main.js**. Dans l'objet **uris**, remplacez 'vueandibmscloud-api.eu-de.mybluemix.net' par l'URL où se trouve votre serveur backend. Vous pouvez inspecter l'URL dans la console Bluemix > cliquez sur votre application > affichez l'URL de l'application.

Dans le dossier racine de l'application frontend, créez le fichier manifest.yml et incluez le contenu suivant :

```yml
applications:
  - path: .
    memory: 1024M
    instances: 1
    domain: mybluemix.net
    name: vueAndIbmsCloud
    host: vueAndIbmsCloud
    disk_quota: 1024M
    buildpack: staticfile_buildpack
```

Ajoutez le script de déploiement suivant à package.json dans la section "scripts" :

```json
"deploy": "npm run build; cp manifest.yml dist/manifest.yml; cd dist; bx cf push vueAndIbmsCloud"
```

(Vous devez changer ce nom d'application pour le rendre unique, par exemple, ajoutez un index de votre choix dans manifest.yml et package.json.)

Exécutez **yarn deploy**, et cela déployera votre application frontend sur IBM Cloud.

Félicitations :) Vous pouvez maintenant utiliser votre application frontend sur le Cloud d'IBM.

Retrouvez les sources sur GitHub : [https://github.com/thomasreinecke/VueAndIBMsCloud](https://github.com/thomasreinecke/VueAndIBMsCloud)