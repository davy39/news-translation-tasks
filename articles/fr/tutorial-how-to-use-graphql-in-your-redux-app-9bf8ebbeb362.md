---
title: Comment utiliser GraphQL dans votre application Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T06:17:24.000Z'
originalURL: https://freecodecamp.org/news/tutorial-how-to-use-graphql-in-your-redux-app-9bf8ebbeb362
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ItpcYJftmpYtiCk1GxO8bQ.png
tags:
- name: GraphQL
  slug: graphql
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Comment utiliser GraphQL dans votre application Redux
seo_desc: 'By Howon Song

  Fetching and managing data in Redux requires too much work. As Sashko Stubailo points
  out:


  Unfortunately the patterns for asynchronously loading server data in a Redux app
  aren’t as well established, and often involve using external he...'
---

Par Howon Song

Récupérer et gérer des données dans Redux nécessite trop de travail. Comme le [souligne Sashko Stubailo](https://www.freecodecamp.org/news/tutorial-how-to-use-graphql-in-your-redux-app-9bf8ebbeb362/undefined) :

> Malheureusement, les modèles pour charger de manière asynchrone les données du serveur dans une application Redux ne sont pas aussi bien établis, et impliquent souvent l'utilisation de bibliothèques externes, comme [redux-saga](https://github.com/yelouafi/redux-saga). Vous devez écrire du code personnalisé pour appeler vos points de terminaison du serveur, interpréter les données, les normaliser et les insérer dans le store — tout en gardant une trace des divers états d'erreur et de chargement.

À la fin de ce tutoriel, vous aurez appris comment résoudre ce problème en laissant Apollo Client récupérer et gérer les données pour vous. Vous n'aurez plus à écrire plusieurs dispatchers d'actions, réducteurs et normaliseurs pour récupérer et synchroniser les données entre votre front-end et votre back-end.

Mais avant de commencer le tutoriel, assurez-vous que :

* Vous connaissez les bases des requêtes GraphQL — si vous êtes entièrement nouveau dans GraphQL, vous devriez revenir après avoir fait ce [tutoriel](https://learngraphql.com/).
* Vous avez une certaine expérience de travail avec React/Redux — sinon, vous devriez revenir après avoir fait le [tutoriel react](https://facebook.github.io/react/docs/getting-started.html) et le [tutoriel redux](http://redux.js.org/docs/introduction/Motivation.html).

Dans ce tutoriel, nous allons parcourir 6 sections ensemble.

1. Configuration de l'environnement serveur (rapide)
2. Configuration de l'application boilerplate Redux
3. Ajout du client GraphQL (Apollo Client)
4. Récupération de données avec une requête GraphQL
5. Récupération de encore plus de données
6. Prochaines étapes

#### 1. Configuration de l'environnement serveur

Tout d'abord, nous avons besoin d'un serveur GraphQL. Le moyen le plus simple d'avoir un serveur en cours d'exécution est de compléter ce tutoriel génial [tutoriel](https://medium.com/apollo-stack/tutorial-building-a-graphql-server-cddaa023c035#.9f3v0r5ix).

Si vous vous sentez paresseux, vous pouvez simplement cloner mon [dépôt](https://github.com/woniesong92/apollo-starter-kit.git), qui est presque le même serveur que vous obtiendriez si vous faisiez le tutoriel vous-même. Le serveur prend en charge les requêtes GraphQL pour récupérer des données à partir d'une base de données SQLite.

Lançons-le et voyons s'il fonctionne correctement :

```
$ git clone https://github.com/woniesong92/apollo-starter-kit$ cd apollo-starter-kit$ npm install$ npm start
```

Le serveur devrait fonctionner à l'adresse [http://localhost:8080/graphql](http://localhost:8080/graphql). Naviguez jusqu'à cette page et voyez si vous obtenez une interface GraphiQL fonctionnelle avec des résultats comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/d3InQW6BYBXEZxgqjmSctEAYBvFezLSShkdq)

GraphiQL vous permet de tester différentes requêtes et de voir immédiatement quelle réponse vous obtenez du serveur. Si nous ne voulons pas le nom de famille d'un auteur et un message de cookie de fortune dans une réponse, nous pouvons mettre à jour la requête comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/pigA9zhd8bbXB0ZUSnh0qW1h9dr2Spo80MzE)

Et c'est exactement ce que nous voulons. Nous avons confirmé que notre serveur fonctionne bien et retourne de bonnes réponses, alors commençons à construire le client.

#### 2. Configuration de l'application boilerplate Redux

Pour simplifier, nous utiliserons un [boilerplate Redux](https://github.com/davezuko/react-redux-starter-kit) afin que nous puissions obtenir toute la configuration (par exemple, Babel, webpack, CSS, etc.) gratuitement. J'aime ce boilerplate car sa configuration est facile à suivre et est uniquement côté client — ce qui le rend parfait pour ce tutoriel.

```
$ git clone https://github.com/woniesong92/react-redux-starter-kit.git$ cd react-redux-starter-kit$ npm install$ npm start
```

Naviguons vers [http://localhost:3000/](http://localhost:3000/) pour voir si le serveur client est en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/9I6YDSNjFPPbWb0E7QngMQIgO4v14SgHKNvI)

Hourra ! Le client est en cours d'exécution. Il est temps pour nous de commencer à ajouter un client GraphQL. Encore une fois, notre objectif est de récupérer facilement des données à partir du serveur et de les rendre dans la page d'accueil (HomeView) sans trop d'effort en utilisant des requêtes GraphQL.

#### 3. Ajout du client GraphQL (Apollo Client)

Installez les packages apollo-client, react-apollo et graphql-tag.

```
$ npm install apollo-client react-apollo graphql-tag --save
```

Ensuite, ouvrez le fichier src/containers/AppContainer.js, la racine de notre application Redux. C'est ici que nous passons le store Redux aux composants enfants, en utilisant le Provider de react-redux.

```
import React, { PropTypes } from 'react'import { Router } from 'react-router'import { Provider } from 'react-redux'
```

```
class AppContainer extends React.Component {  static propTypes = {    history: PropTypes.object.isRequired,    routes: PropTypes.object.isRequired,    routerKey: PropTypes.number,    store: PropTypes.object.isRequired  }
```

```
render () {    const { history, routes, routerKey, store } = this.props
```

```
return (      <Provider store={store}>        <div>          <Router history={history} children={routes} key={routerKey} />        </div>      </Provider>    )  }}
```

```
export default AppContainer
```

Nous devons initialiser un ApolloClient et remplacer le Provider de react-redux par ApolloProvider de react-apollo.

```
import React, { Component, PropTypes } from 'react'import { Router } from 'react-router'import ApolloClient, { createNetworkInterface, addTypename } from 'apollo-client'import { ApolloProvider } from 'react-apollo'
```

```
const client = new ApolloClient({  networkInterface: createNetworkInterface('http://localhost:8080/graphql'),  queryTransformer: addTypename,})
```

```
class AppContainer extends Component {  static propTypes = {    history: PropTypes.object.isRequired,    routes: PropTypes.object.isRequired,    store: PropTypes.object.isRequired  }
```

```
render () {    const { history, routes } = this.props
```

```
return (      <ApolloProvider client={client}>        <div>          <Router history={history} children={routes} />        </div>      </ApolloProvider>    )  }}
```

```
export default AppContainer
```

C'est tout ! Nous venons d'ajouter un client GraphQL à une application Redux simple.

Allons-y et essayons notre première requête GraphQL.

#### 4. Récupération de données avec des requêtes GraphQL

Ouvrez src/views/HomeView.js

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
// C'est ici que vous récupérez généralement les données stockées dans le store redux (par exemple, posts: state.posts.data)const mapStateToProps = (state, { params }) => ({
```

```
})
```

```
// C'est ici que vous liez généralement le dispatch aux actions utilisées pour demander des données au backend. Vous appellerez le dispatcher dans componentDidMount.const mapDispatchToProps = (dispatch) => {  const actions = {}
```

```
  return {    actions: bindActionCreators(actions, dispatch)  }}
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(HomeView)
```

HomeView est un conteneur Redux conventionnel (composant intelligent). Pour utiliser les requêtes GraphQL au lieu des dispatchers d'actions pour récupérer des données, nous allons apporter quelques modifications ensemble.

1. Supprimez mapDispatchToProps() et mapStateToProps() complètement.

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
export default connect({
```

```
})(HomeView)
```

2. Ajoutez mapQueriesToProps() et définissez une requête GraphQL qui récupérera les informations de l'auteur. Remarquez comment cela correspond exactement à la même requête que nous avons testée au début en utilisant l'interface GraphIQL sur le serveur.

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
// NOTE: Cela sera automatiquement déclenché lorsque le composant sera rendu, envoyant cette requête GraphQL exacte au backend.const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({
```

```
})(HomeView)
```

3. Remplacez connect de react-redux par connect de react-apollo et passez mapQueriesToProps comme argument. Une fois que mapQueriesToProps est connecté à ApolloClient, la requête récupérera automatiquement les données du backend lorsque HomeView sera rendu, et passera les données via les props.

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: connect différent !import gql from 'graphql-tag' // NOTE: nous permet de définir des requêtes GraphQL dans un langage de template
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

4. Rendre les données qui sont passées via les props :

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: connect différent !import gql from 'graphql-tag' // NOTE: nous permet de définir des requêtes GraphQL dans un langage de template
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    const author = this.props.data.author    if (!author) {      return <h1>Chargement</h1>    }
```

```
    return (      <div>        <h1>{author.firstName}'s posts</h1>        {author.posts && author.posts.map((post, idx) => (          <li key={idx}>{post.title}</li>        ))}      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

Si tout s'est bien passé, votre HomeView rendu devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/E2gXbodtbyO-a59P8MJKn6g0P1WeiKGeh9of)

Pour récupérer et rendre les données que nous voulions, nous n'avons pas eu à écrire de dispatcher d'action, de réducteur ou de normaliseur. Tout ce que nous avons dû faire sur le client était d'écrire une seule requête GraphQL !

Nous avons réussi à atteindre notre objectif initial. Mais cette requête était assez simple. Que se passe-t-il si nous voulions afficher tous les auteurs au lieu d'un seul auteur ?

#### 5. Récupération de encore plus de données

Pour récupérer et afficher tous les auteurs, nous devons mettre à jour notre requête GraphQL et notre méthode de rendu :

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: connect différent !import gql from 'graphql-tag' // NOTE: nous permet de définir des requêtes GraphQL dans un langage de template
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    const authors = this.props.data.authors    if (!authors) {      return <h1>Chargement</h1>    }
```

```
    return (      <div>        {authors.map((author, idx) => (          <div key={'author-'+idx}>            <h1>{author.firstName}'s posts</h1>            {author.posts && author.posts.map((post, idx) => (              <li key={idx}>{post.title}</li>            ))}          </div>        ))}      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          authors {            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

Cependant, une fois que vous actualisez votre page HomeView dans le navigateur, vous remarquerez que vous avez une erreur dans votre console :

_ApolloError {graphQLErrors: Array[1], networkError: undefined, message: "Erreur GraphQL : Impossible d'interroger le champ \"authors\" sur le type \"Query\". Vouliez-vous dire \"author\" ?"}_

Ah, c'est vrai ! Dans notre serveur GraphQL, nous n'avons pas vraiment défini comment récupérer les _authors_.

Retournez à notre serveur et voyons ce que nous avons. Ouvrez le fichier apollo-starter-kit/data/resolvers.js

```
import { Author, FortuneCookie } from './connectors';
```

```
const resolvers = {  Query: {    author(_, args) {      return Author.find({ where: args });    },    getFortuneCookie() {      return FortuneCookie.getOne()    }  },  Author: {    posts(author) {      return author.getPosts();    },  },  Post: {    author(post) {      return post.getAuthor();    },  },};
```

```
export default resolvers;
```

En regardant le résolveur Query, nous remarquons que notre serveur GraphQL ne comprend que les requêtes _author_ et _getFortuneCookie_ pour l'instant. Nous devrions lui apprendre comment "résoudre" la requête _authors_.

```
import { Author, FortuneCookie } from './connectors';
```

```
const resolvers = {  Query: {    author(_, args) {      return Author.find({ where: args });    },    getFortuneCookie() {      return FortuneCookie.getOne()    },    authors() { // la requête "authors" signifie retourner tous les auteurs !      return Author.findAll({})    }  },  ...};
```

```
export default resolvers;
```

Nous n'avons pas encore terminé. Ouvrez le fichier apollo-starter-kit/data/schema.js

```
const typeDefinitions = `...
```

```
type Query {  author(firstName: String, lastName: String): Author  getFortuneCookie: String}schema {  query: Query}`;
```

```
export default [typeDefinitions];
```

Ce schéma clarifie le type de requêtes que le serveur doit attendre. Il ne s'attend pas encore à la requête _authors_, alors mettons-le à jour.

```
const typeDefinitions = `...
```

```
type Query {  author(firstName: String, lastName: String): Author  getFortuneCookie: String,  authors: [Author] // la requête 'authors' doit retourner un tableau de                     // Author}schema {  query: Query}`;
```

```
export default [typeDefinitions];
```

Maintenant que notre serveur GraphQL sait ce que signifie la requête "authors", retournons à notre client. Nous avons déjà mis à jour notre requête, donc nous n'avons pas besoin de toucher à quoi que ce soit.

```
export class HomeView extends React.Component {
```

```
...
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          authors {            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

Avec cette requête, nous nous attendons à obtenir tous les auteurs avec leurs prénoms et leurs publications. Allez-y et actualisez le navigateur pour voir si nous obtenons les bonnes données.

![Image](https://cdn-media-1.freecodecamp.org/images/IO6Xv-2NVPI1eCan85UgeJZghfpDF-Ouj7Ec)

Si tout s'est bien passé, votre page HomeView ressemblera à ceci.

#### 6. Prochaines étapes

Ce tutoriel n'explore qu'une petite partie de GraphQL et laisse de côté de nombreux concepts tels que la mise à jour des données sur le serveur ou l'utilisation d'un serveur backend différent (par exemple, Rails).

Alors que je travaille à introduire ces concepts dans les tutoriels suivants, vous pouvez lire l'article de Sashko [post](https://medium.com/apollo-stack/apollo-client-graphql-with-react-and-redux-49b35d0f2641#.iqsgdstls) ou la [documentation d'Apollo Client](http://docs.apollostack.com/apollo-client/) pour mieux comprendre ce qui se passe sous le capot (par exemple, ce qui s'est passé lorsque nous avons remplacé Provider par ApolloProvider ?).

Plonger dans le code source de [GitHunt](https://github.com/apollostack/GitHunt), une application exemple complète de client et serveur Apollo, semble également être un excellent moyen d'apprendre.

Si vous avez des commentaires, n'hésitez pas à les laisser dans les commentaires. Je ferai de mon mieux pour être utile 😊