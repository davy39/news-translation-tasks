---
title: Guide du débutant pour React Router
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-05T19:20:35.000Z'
originalURL: https://freecodecamp.org/news/beginner-s-guide-to-react-router-53094349669
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GH8GqFmDl0rTKfxn5xeZuQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Guide du débutant pour React Router
seo_desc: 'By Nader Dabit

  Or what I wish I knew when starting with React Router.


  Click here to go to the Github repo

  This tutorial uses React Router version 2.0.1 and Babel version 6.7.4


  React Router is the standard routing library for React. From the docs:


  ...'
---

Par Nader Dabit

Ou ce que j'aurais aimé savoir en commençant avec React Router.

> Cliquez [ici](https://github.com/dabit3/beginners-guide-to-react-router) pour accéder au dépôt Github

> Ce tutoriel utilise React Router version 2.0.1 et Babel version 6.7.4

React Router est la bibliothèque de routage standard pour React. D'après la documentation :

> « React Router maintient votre UI synchronisée avec l'URL. Il dispose d'une API simple avec des fonctionnalités puissantes comme le chargement de code paresseux, la correspondance dynamique des routes et la gestion des transitions de localisation intégrées. Faites de l'URL votre première pensée, pas une réflexion après coup. »

### Étape 1. Commencer

Pour commencer, vous pouvez soit [cloner le dépôt de démarrage](https://github.com/dabit3/beginners-guide-to-react-router) et passer à l'étape deux, soit suivre les étapes suivantes et configurer votre projet manuellement.

#### **Installation manuelle**

Tout d'abord, configurons notre environnement avec React, Babel et webpack. Créez un dossier et accédez-y. Ensuite, exécutez npm init -y :

```
npm init -y
```

* -y répond simplement oui à toutes les questions

Ensuite, installez react, react-router et react-dom et enregistrez-les comme dépendances :

```
npm i react react-dom react-router@2.0.1 --save
```

Ensuite, installez nos dépendances de développement. Ce seront webpack, webpack-dev-server, babel-core, babel-loader, babel-preset-es2015 et babel-preset-react

```
npm i webpack webpack-dev-server babel-core babel-loader babel-preset-es2015 babel-preset-react --save-dev
```

Maintenant, créons les fichiers de configuration pour webpack et babel :

```
touch .babelrc webpack.config.js
```

Ensuite, créons un dossier pour notre code. Nous appellerons ce dossier app :

```
mkdir app
```

Dans le répertoire app, créez trois fichiers : index.html app.js main.js

```
cd app
touch index.html app.js main.js
```

Notre structure de fichiers devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Tteoevz7v-Ur0ffYdB1WUgN8vtHzVKKoArPQ)

Maintenant, ouvrez le fichier .babelrc et ajoutez les presets pour react et ES2015 :

```
{ "presets": [  "es2015",  "react" ]}
```

Dans webpack.config.js, ajoutez la configuration suivante pour commencer :

```
module.exports = {  entry: './app/main.js',  output: {    path: './app',    filename: 'bundle.js'  },  devServer: {    inline: true,    contentBase: './app',    port: 8100  },  module: {    loaders: [      {        test: /\.js$/,        exclude: /node_modules/,        loader: 'babel'      }    ]  }}
```

> Si vous souhaitez en savoir plus sur webpack et babel, [consultez mon tutoriel sur le début avec webpack](https://medium.com/@dabit3/beginner-s-guide-to-webpack-b1f1a3638460#.5tirb1odd).

Maintenant que webpack et babel sont configurés, créons un raccourci pour webpack-dev-server. Ouvrez package.json et insérez le script suivant dans la clé « scripts » :

```
"scripts": {  "start": "webpack-dev-server"}
```

Maintenant, nous pouvons simplement exécuter npm start pour démarrer notre projet.

Configurons maintenant notre HTML et React. Ouvrez index.html et créez une page html de base. Ensuite, ajoutez une div avec l'id root, et une balise script référençant bundle.js :

```
<!DOCTYPE html>  <html lang="en">  <head>    <meta charset="UTF-8">    <title>React Router</title>  </head>  <body>    <div id="root"></div>    <script src="./bundle.js"></script>  </body></html>
```

Maintenant, allons dans notre main.js et configurons un point d'entrée pour notre application. Tapez ceci dans votre fichier main.js :

```
import React from 'react'
import ReactDOM from 'react-dom'
import App from './app'
ReactDOM.render(<App />, document.getElementById('root'))
```

Maintenant, allons dans app.js et créons notre composant d'application. Ouvrez app.js et tapez ce qui suit :

```
import React, { Component } from 'react'
import { Router, Route, Link, IndexRoute, hashHistory, browserHistory } from 'react-router'
```

```
const App = () => <h1>Bonjour le monde !</h1>
```

```
export default App
```

Nous n'utilisons pas encore Component ou l'un des composants Router / react-router, mais nous les importons pour pouvoir commencer à l'étape deux.

Maintenant, si vous exécutez le projet et naviguez vers [http://localhost:8100/](http://localhost:8100/), vous devriez obtenir 'Bonjour le monde !!!!!!' sur votre écran :

```
npm start
```

![Image](https://cdn-media-1.freecodecamp.org/images/lZ1pJFumTCxGVoEdyUrUx1JN3op-bL009x38)
_Bonjour le monde_

### Étape 2. Routage de base

Configurons une route de base. Nous allons remplacer le composant App par une classe React, qui retournera un composant Router. Router enveloppera toutes les routes que nous allons définir.

Chaque route sera identifiée dans un composant <Route>. Le composant <Route> prendra deux propriétés : path et component. Lorsqu'un chemin correspond au chemin donné au composant <Route>, il retournera le composant spécifié.

Dans app.js, refactorisez le composant App pour qu'il ressemble à ceci :

```
import React, { Component } from 'react'
import { Router, Route, Link, IndexRoute, hashHistory, browserHistory } from 'react-router'
```

```
class App extends Component {  render() {    return (      <Router history={hashHistory}>        <Route path='/' component={Home} />        <Route path='/address' component={Address} />      </Router>    )  }}
```

```
const Home = () => <h1>Bonjour depuis la page d'accueil !</h1>
const Address = () => <h1>Nous sommes situés au 555 Jackson St.</h1>
```

```
export default App
```

Maintenant, si vous naviguez vers [http://localhost:8100/](http://localhost:8100/), vous devriez voir notre composant Home, et si vous naviguez vers [http://localhost:8100/#/address](http://localhost:8100/#/address), vous devriez voir notre composant Address.

Vous remarquerez qu'il y a des chaînes de caractères aléatoires après le hash dans votre barre d'adresse :

> Lorsque vous utilisez hash history, vous verrez un élément supplémentaire dans votre chaîne de requête qui ressemble à quelque chose comme _k=123abc. Il s'agit d'une clé que history utilise pour rechercher des données d'état persistantes dans window.sessionStorage entre les chargements de page. [Lisez plus ici.](https://github.com/mjackson/history/blob/master/docs/HashHistoryCaveats.md)

Si vous souhaitez une adresse plus propre, ou si vous utilisez cela en production, vous pouvez envisager d'utiliser browserHistory au lieu de hashHistory. Lorsque vous utilisez browserHistory, vous devez avoir un serveur qui retournera toujours votre serveur à n'importe quelle route, par exemple, si vous utilisez nodejs, une configuration comme la suivante (issue de la documentation) fonctionnerait :

```
const express = require('express')
const path = require('path')
const port = process.env.PORT || 8080
const app = express()
// servir les actifs statiques normalement
app.use(express.static(__dirname + '/public'))
// gérer toutes les autres routes avec index.html, qui contiendra
// une balise script vers le(s) fichier(s) JavaScript de votre application.
app.get('*', function (request, response){
  response.sendFile(path.resolve(__dirname, 'public', 'index.html'))})
app.listen(port)
console.log("server started on port " + port)
```

Pour en savoir plus sur browserHistory, consultez [ce lien](https://github.com/reactjs/react-router/blob/master/docs/guides/Histories.md#browserhistory).

Pour le reste de ce tutoriel, nous utiliserons hashHistory.

### Étape 3. Route 404

Maintenant, que se passe-t-il si nous atteignons une route qui n'est pas définie ? Configurons une route 404 et un composant qui sera retourné si la route n'est pas trouvée :

```
const NotFound = () => (
  <h1>404.. Cette page est introuvable !</h1>)
```

Maintenant, _en dessous_ de notre route '/address', créez la route suivante :

```
<Route path='*' component={NotFound} />
```

Maintenant, si nous naviguons vers une route qui n'a pas été définie ([http://localhost:8100/#/asdfasdf](http://localhost:8100/#/asdfasdf)), nous devrions voir notre route 404.

### Étape 4. IndexRoute et Links

Maintenant, ajoutons une navigation pour nous déplacer entre les pages.

Pour ce faire, nous utiliserons le composant <Link>. <Link> est similaire à l'utilisation d'une balise d'ancrage html.

D'après la documentation :

> La principale façon de permettre aux utilisateurs de naviguer dans votre application. <Link> rendra une balise d'ancrage entièrement accessible avec le href approprié.

Pour ce faire, créons d'abord un composant Nav. Notre composant Nav contiendra des composants <Link>, et ressemblera à ceci :

```
const Nav = () => (
  <div>
    <Link to='/'>Accueil</Link>
    <Link to='/address'>Adresse</Link>
  </div>)
```

_Nous avons maintenant besoin d'un moyen de rendre notre composant Nav persistant sur toutes les pages._ Pour ce faire, nous envelopperons nos routes enfants dans un composant <Route> principal. Nous devrons également mettre à jour notre composant Home, et créer un nouveau composant appelé Container :

Container :

```
const Container = (props) => <div>
  <Nav />
  {props.children}
</div>
```

`{props.children}` permettra à toute route enveloppée dans cette route d'être rendue dans ce composant.

Maintenant, réécrivons notre composant App pour qu'il ressemble à ceci. Nous enveloppons nos routes HomePage, Address et NotFound à l'intérieur de la nouvelle route Container. Nous définissons également HomePage comme notre IndexRoute. Cela signifie que lorsque nous atteignons [http://localhost:8100](http://localhost:8100/#/), notre composant Home sera rendu, car il est spécifié comme l'index :

```
class App extends Component {
  render () {
    return (
      <Router history={hashHistory}>
        <Route path='/' component={Container}>
          <IndexRoute component={Home} />
          <Route path='/address' component={Address} />
          <Route path='*' component={NotFound} />
        </Route>
      </Router>
    )
  }}
```

Pour référence, notre code complet app.js devrait ressembler à [ceci](https://gist.github.com/dabit3/3d0d47c4a8bfccadfd5d15c58cfb1424).

Maintenant, lorsque nous naviguons vers [http://localhost:8100](http://localhost:8100/), nous devrions voir notre composant Home rendu, ainsi que nos composants Nav <Link> !

### Étape 5. Plusieurs enfants / IndexRoutes

Maintenant, disons que nous voulons imbriquer un flux Twitter et un flux Instagram dans notre composant d'adresse. Créons cette fonctionnalité.

Tout d'abord, réécrivons notre route d'adresse pour prendre deux nouveaux composants : InstagramFeed et TwitterFeed :

```
class App extends Component {
  render () {
    return (
      <Router history={hashHistory}>
        <Route path='/' component={Container}>
          <IndexRoute component={Home} />
          <Route path='address' component={Address}>
            <IndexRoute component={TwitterFeed} />
            <Route path='instagram' component={Instagram} />
          </Route>
          <Route path='*' component={NotFound} />
        </Route>
      </Router>
    )
  }}
```

Nous avons défini l'IndexRoute de l'adresse comme étant TwitterFeed, et nous avons également ajouté la route Instagram.

Maintenant, créons nos composants InstagramFeed et TwitterFeed. Ceux-ci seront très basiques pour que nous sachions que nous avons atteint les bonnes routes :

```
const Instagram = () => <h3>Flux Instagram</h3>
const TwitterFeed = () => <h3>Flux Twitter</h3>
```

Enfin, allez dans le composant Address, et ajoutez les liens vers les nouveaux composants ainsi que props.children, afin que les composants soient rendus :

```
const Address = (props) => <div>
  <br />
  <Link to='/address'>Flux Twitter</Link>

  <Link to='/address/instagram'>Flux Instagram</Link>
  <h1>Nous sommes situés au 555 Jackson St.</h1>
  {props.children}
</div>
```

Maintenant, lorsque nous naviguons vers [http://localhost:8100/#/address](http://localhost:8100/#/address), le composant d'adresse devrait être rendu ainsi que le composant TwitterFeed :

![Image](https://cdn-media-1.freecodecamp.org/images/-Fk1VA1cdpCAYTnuQ5DRi9jMPJwWkus7qn1w)

Pour référence, le code jusqu'à présent devrait ressembler à [ceci](https://gist.github.com/dabit3/0c2014b421f2bf98cd95d176f0b29bad).

### Étape 6. activeStyle / activeClassName et IndexLink

Nous allons maintenant voir comment styliser un Link en fonction de si la route est active. Il y a deux principales façons de faire cela, soit en ajoutant un style directement, soit via une classe.

D'après la documentation :

> <Link> peut savoir quand la route à laquelle il est lié est active et appliquer automatiquement un activeClassName et/ou activeStyle lorsqu'une de ces propriétés est donnée. Le <Link> sera actif si la route actuelle est soit la route liée, soit un descendant de la route liée. Pour que le lien soit actif uniquement sur la route liée exacte, utilisez <IndexLink> ou définissez la propriété onlyActiveOnIndex.

Tout d'abord, regardons activeStyle. Pour appliquer activeStyle, vous ajoutez simplement activeStyle comme propriété à un <Link> et passez le style que vous souhaitez que le <Link> ait :

```
<Link activeStyle={{color:'#53acff'}} to=''>Accueil</Link>
```

Mettons à jour notre composant Nav pour implémenter cela :

```
const Nav = () => (
  <div>
    <Link activeStyle={{color:'#53acff'}} to='/'>Accueil</Link>

    <Link activeStyle={{color:'#53acff'}} to='/address'>Adresse</Link>

    <Link activeStyle={{color:'#53acff'}} to='/about'>À propos</Link>
  </div>)
```

Maintenant, regardons comment cela apparaît dans notre navigateur. Vous remarquerez peut-être que lorsque vous cliquez sur adresse, que Accueil est toujours mis en évidence :

![Image](https://cdn-media-1.freecodecamp.org/images/gzgxtxcK49aa2N9m-dqV4vGWiFPwIZlCui4X)

C'est parce que lorsque vous utilisez <Link> avec activeStyle, le <Link> sera actif si la route actuelle est soit la route liée, soit un descendant de la route liée.

Cela signifie que parce que Adresse est un descendant de Accueil, il reste mis en évidence. Pour corriger cela, nous pouvons passer la propriété onlyActiveOnIndex à notre composant Link :

```
<Link onlyActiveOnIndex activeStyle={{color:'#53acff'}} to='/'>Accueil</Link>
```

Maintenant, lorsque nous regardons notre navigateur, le lien ne sera mis en évidence que si nous sommes sur le lien exact :

![Image](https://cdn-media-1.freecodecamp.org/images/WWiiso0wJuB8CfeLyzMy9yaW0RKtTs22hi92)

Il existe également un composant frère de <Link> appelé <IndexLink>. <IndexLink> n'est actif que lorsque la route actuelle est exactement la route liée.

D'après la documentation :

> Un <IndexLink> est similaire à un <Link>, sauf qu'il n'est actif que lorsque la route actuelle est exactement la route liée. Il est équivalent à un <Link> avec la propriété onlyActiveOnIndex définie.

Pour implémenter cela, importez d'abord <IndexLink> depuis react-router :

```
import { ..., IndexLink } from 'react-router'
```

Maintenant, remplacez simplement les composants <Link> dans nav par des composants <IndexLink> :

```
const Nav = () => (
  <div>
    <IndexLink activeStyle={{color:'#53acff'}} to='/'>Accueil</IndexLink>

    <IndexLink activeStyle={{color:'#53acff'}} to='/address'>Adresse</IndexLink>

    <IndexLink activeStyle={{color:'#53acff'}} to='/about'>À propos</IndexLink>
  </div>)
```

Maintenant, que dire de l'ajout de classes par rapport aux styles ? Pour ce faire, nous pouvons utiliser activeClassName. Configurons un style actif dans notre index.html :

```
<style>
  .active {
   color:#53acff
  }
</style>
```

Maintenant, nous remplacerons activeStyle par activeClassName dans notre composant Nav :

```
const Nav = () => (
  <div>
    <IndexLink activeClassName='active' to='/'>Accueil</IndexLink>

    <IndexLink activeClassName='active' to='/address'>Adresse</IndexLink>

    <IndexLink activeClassName='active' to='/about'>À propos</IndexLink>
  </div>)
```

Pour référence, notre code devrait maintenant ressembler à [ceci](https://gist.github.com/dabit3/ae4eeea9906c26e5643145664d540d0d).

### Étape 7. Composants nommés

En utilisant des composants nommés, nous pouvons spécifier des composants comme props pour une <Route>.

D'après la documentation :

> Lorsqu'une route a un ou plusieurs composants nommés, les éléments enfants sont disponibles par nom sur this.props. Dans ce cas, this.props.children sera indéfini. Tous les composants de route peuvent participer à l'imbrication.

Maintenant, plongeons dans le code et voyons à quoi cela ressemble réellement.

Tout d'abord, créons un nouveau composant qui rendra nos composants nommés. Ces composants seront disponibles comme props :

```
const NamedComponents = (props) => (
  <div>
    {props.title}<br />
    {props.subTitle}
  </div>)
```

Ensuite, créons deux nouveaux composants appelés Title et Subtitle :

```
const Title = () => (
  <h1>Bonjour depuis le composant Title</h1>)
const SubTitle = () => (
  <h1>Bonjour depuis le composant SubTitle</h1>)
```

Maintenant, créons une nouvelle route pour notre composant NamedComponents, et définissons les composants Title et Subtitle dans l'IndexRoute :

```
<Route path='/namedComponent' component={NamedComponents}>
  <IndexRoute components={{ title: Title, subTitle: SubTitle }} />
</Route>
```

Enfin, ajoutons un lien à notre nav pour naviguer vers ce composant :

```
<IndexLink activeClassName='active' to='/namedComponent'>Composants nommés</IndexLink>
```

Maintenant, nous devrions voir notre nouveau lien Composants nommés lorsque nous regardons notre navigateur, et lorsque nous cliquons sur le lien, nous devrions voir nos composants Title et SubTitle rendus à l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/dQMk0ADEJRtF0kf2rq9edM2fCWsKz4x4VTG-)

Pour référence, notre code devrait maintenant ressembler à [ceci](https://gist.github.com/dabit3/5a75ecdba89dc2a45c1aaaf2727ddad1).

### Étape 8. Paramètres de route

Une partie essentielle de nombreuses applications est la capacité à lire les paramètres de route à partir d'une URL.

Pour implémenter cela, revisitons notre composant About. Tout d'abord, réécrivons le chemin dans notre Router pour prendre un paramètre optionnel, nous l'appellerons name :

```
<Route path='/about/:name' component={About} />
```

Maintenant, réécrivons notre composant About pour utiliser cette variable name :

```
const About = (props) => (
  <div>
    <h3>Bienvenue sur la page À propos</h3>
    <h2>{props.params.name}</h2>
  </div>)
```

Maintenant, si nous visitons [http://localhost:8100/#/about/nader](http://localhost:8100/#/about/nader), nous verrons mon nom affiché sous « Bienvenue sur la page À propos ».

Le seul problème ici est que si nous revisitons [http://localhost:8100/#/about](http://localhost:8100/#/about), nous obtenons une erreur 404 car il n'y a pas de paramètre name. Pour corriger cela, nous pouvons rendre le paramètre optionnel en l'enveloppant dans des parenthèses :

```
<Route path='/about(/:name)' component={About} />
```

Maintenant, si nous visitons [http://localhost:8100/#/about](http://localhost:8100/#/about), nous n'obtenons plus d'erreur 404, et nous pouvons toujours accéder à la variable name.

Nous pouvons également aller plus loin en vérifiant si props.name est disponible et en affichant un contenu :

```
{ props.params.name && <h2>Bonjour, {props.params.name}</h2>}
```

Maintenant, le contenu ne sera affiché que si un paramètre name est disponible.

Pour référence, notre code devrait maintenant ressembler à [ceci](https://gist.github.com/dabit3/a31358742f837cf4826d55828931543f).

### Étape 9. Paramètres de chaîne de requête

Vous pouvez également passer des chaînes de requête comme props à n'importe quel composant qui sera rendu à une route spécifique, et accéder à ces paramètres comme props.location.query.

Pour voir comment cela fonctionne, créons un nouveau composant appelé Query, et rendons une propriété appelée props.location.query.message :

```
const Query = (props) => (
  <h2>{props.location.query.message}</h2>)
```

Maintenant, configurons notre nouvelle route Query dans la route d'adresse que nous avons déjà créée :

```
...
<Route path='/address' component={Address}>
  <IndexRoute component={TwitterFeed} />
  <Route path='instagram' component={Instagram} />
  <Route path='query' component={Query} />
</Route>
...
```

Enfin, créons un lien vers cette route en créant un nouveau composant Link, et passons une chaîne de requête appelée message et donnons-lui une valeur. Cela se fait dans la propriété 'to' que nous avons déjà utilisée.

Au lieu de passer un lien à 'to', nous passons un objet avec les propriétés pathname et query définies :

```
<IndexLink
  activeClassName='active'
  to={{
    pathname: '/address/query',
    query: { message: 'Bonjour depuis la requête de route' }
  }}>
  Requête de route
</IndexLink>
```

Maintenant, si nous cliquons sur notre lien Requête de route, nous devrions voir notre message rendu à l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/WE7uBdDkKZUL8Pa5yOtFTfEFyvzKPeUNBACl)

Pour référence, notre code devrait maintenant ressembler à [ceci](https://gist.github.com/dabit3/651f2dae058ff99810eb771c2817d622).

Cela couvre de nombreux cas d'utilisation de base pour commencer avec React Router.

> Je m'appelle [Nader Dabit](https://twitter.com/dabit3). Je suis développeur chez [School Status](https://www.schoolstatus.com/) où nous aidons les éducateurs à prendre des décisions pédagogiques intelligentes en fournissant toutes leurs données en un seul endroit. Découvrez-nous [@schoolstatusapp](https://twitter.com/schoolstatusapp).

> Si vous aimez React et React Native, écoutez notre podcast — [React Native Radio](https://devchat.tv/react-native-radio) sur [Devchat.tv](http://devchat.tv/)

> Si vous avez aimé cet article, veuillez le recommander et le partager ! Merci pour votre temps