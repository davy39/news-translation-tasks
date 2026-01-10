---
title: Imaginez React Router comme votre opérateur de standard téléphonique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T19:04:43.000Z'
originalURL: https://freecodecamp.org/news/imagine-react-router-as-your-switchboard-operator-f4f1ac22188c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MfOaLBtqjvchvWlqk6Z6Hw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Imaginez React Router comme votre opérateur de standard téléphonique
seo_desc: 'By Jay Papisan

  Like an old-school telephone switchboard, React Router is a smooth, behind-the-scenes
  operator for your single page (SPA) React application. Users click a link, the URL
  changes, views change and for all they know they’ve moved on to an...'
---

Par Jay Papisan

Comme un standard téléphonique à l'ancienne, React Router est un opérateur fluide et discret pour votre application React en une seule page (SPA). Les utilisateurs cliquent sur un lien, l'URL change, les vues changent et pour eux, ils ont l'impression d'être passés à une autre page — sauf qu'ils ne l'ont pas fait. React Router est un outil clé pour donner à votre SPA l'apparence d'une application multi-pages tout en conservant le rendu rapide du DOM virtuel de React.

Passons en revue les composants de base de l'utilisation de React Router pour configurer une navigation simple. Pour une application web, vous exécuterez `yarn add react-router-dom`. Il existe de nombreuses façons de répartir vos composants de routeur, mais pour des raisons d'explication, nous allons utiliser ce qui suit pour illustrer la hiérarchie des composants nécessaires. Nous allons passer en revue chacun des composants en gras ci-dessous — **Provider, BrowserRouter, Switch** et **Route**.

```
import React from 'react';import ReactDOM from 'react-dom';import { Provider } from 'react-redux';import { createStore, applyMiddleware } from 'redux';import { BrowserRouter, Route, Switch } from 'react-router-dom';import promise from 'redux-promise';import { PostsNew, PostsShow, PostsIndex } from './components'
```

```
const createStoreWithMiddleware = applyMiddleware(promise)(createStore);
```

```
ReactDOM.render( &lt;Provider store={createStoreWithMiddleware(reducers)}&gt;  <BrowserRouter>   <div>    &lt;Switch>     <Route path="/posts/new" component={ PostsNew } />     <Route path="/posts/:id" component={ PostsShow } />     <Route path="/" component={ PostsIndex } />    </Switch>   </div>  </BrowserRouter> </Provider>, document.getElementById('root'));
```

### Opérateur… alias <Provider />

Et si votre appel était coupé et que vous deviez réessayer _(rechargement de la page)_ ? Vous voulez revenir en arrière et rappeler votre dernier ami _(retour du navigateur)_ ? Pas de problème, l'opérateur — alias `Provider` — vous couvre. Il utilise la puissance du `store` de Redux pour conserver tout votre historique de navigation. Considérez-le comme l'opérateur indiscret (et **composant parent**) de tous vos composants React Router.

```
<Provider store={createStoreWithMiddleware(reducers)}>
```

### Téléphone ou télégraphe ?… alias <BrowserRouter />

Vous ne pouvez pas passer un appel téléphonique avec un télégraphe. De même, vous avez besoin du bon routeur pour les applications natives ou web. Pour la plupart des applications web, l'importation de `BrowserRouter`, qui fonctionne sur les navigateurs HTML5, fera l'affaire.

### Qui ?.. alias <Switch />

Votre opérateur est paresseux… il parcourt l'annuaire téléphonique et appelle la première personne qui correspond. En supposant que vous ne souhaitez rendre qu'un seul composant par URL, `Switch` permet un rendu exclusif (par correspondance d'expression régulière en arrière-plan). Faites attention à l'ordre dans lequel vous les placez — mettez les plus spécifiques en premier et les génériques en dernier.

Par exemple, ne placez pas `path="/"` en premier ou vous ne quitterez jamais la maison…

```
&lt;Switch&gt;  <Route path="/posts/new" component={ PostsNew } />  <Route path="/posts/:id" component={ PostsShow } />  <Route path="/" component={ PostsIndex } /> </Switch>
```

### Numéro de téléphone… alias <Route />

Les opérateurs de standard utilisaient-ils des numéros de téléphone ? Peu importe… le composant `Route` rend le composant spécifique que vous avez défini pour correspondre à une URL. Remarquez ci-dessous le `:id` — en utilisant la puissance de l'[objet match](https://reacttraining.com/react-router/core/api/match) de React Router, tout ce qui suit le `:` est accessible dans votre composant rendu, par exemple comme : `this.props.match.params.id`

```
&lt;Route path="/posts/:id" component={ PostsShow } />
```

### Rediriger l'appel… alias <Link />

Cet appel devient redondant, rappelons rapidement quelqu'un d'autre ou retournons à la maison. Avec le composant `Link` de React Router (un wrapper élégant pour une balise d'ancrage HTML), vous pouvez insérer un lien comme vous le feriez pour un bouton de retour à la maison ou des balises d'ancrage à travers vos composants. Il suffit de mettre votre destination dans le champ `to` et de styliser comme vous le feriez en ligne ou d'ajouter un wrapper de bouton.

```
import { Link } from 'react-router-dom';
```

```
class YourThing extends Component {   render() {     return(       <div>        <Link to="/"> Accueil </Link>       </div>     )   }}
```

C'est tout pour quelques bases très simples, bien qu'il y ait beaucoup plus disponible. Consultez la excellente [documentation](https://reacttraining.com/react-router/) et les tutoriels pour les innombrables façons de personnaliser vos routes. Merci d'avoir lu mon deuxième article sur Medium. Donnez-moi quelques commentaires, corrections ou applaudissements si cela vous a été utile.