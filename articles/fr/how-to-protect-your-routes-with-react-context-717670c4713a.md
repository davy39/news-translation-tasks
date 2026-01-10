---
title: Comment protéger vos routes avec React Context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T20:22:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-protect-your-routes-with-react-context-717670c4713a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wmwNRYeBumNlEKriJxLHjg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment protéger vos routes avec React Context
seo_desc: 'By paul christophe

  Among the changes in React 16.3 is a new stable version of the Context API. We’re
  going to take a look at how it works by building a protected route component.

  What is Context?

  Context is about encapsulating state. It allows us to ...'
---

Par paul christophe

Parmi les changements dans [React 16.3](https://reactjs.org/blog/2018/03/29/react-v-16-3.html) se trouve une nouvelle version stable de l'**API Context**. Nous allons examiner comment elle fonctionne en construisant un **composant de route protégé**.

#### Qu'est-ce que le Context ?

Le Context concerne l'encapsulation de l'état. Il nous permet de transmettre des données d'un composant parent fournisseur à n'importe quel composant abonné dans l'arborescence. Sans gestion d'état, nous devons souvent "percer" les props à travers chaque composant le long du chemin.

#### N'est-ce pas le rôle de Redux ?

**Oui**, le Context fonctionne de manière similaire à la façon dont les composants peuvent se connecter à l'état global de Redux. Cependant, un élément natif comme le Context sera souvent une meilleure solution pour les petites et moyennes applications qui n'ont pas besoin de la complexité de Redux.

#### Concepts de base

Il y a trois éléments dans le Context :

* `createContext` — L'appel à cette fonction retourne une paire de composants, `Provider` et `Consumer`.
* `Provider` — un composant qui permet à un ou plusieurs `Consumers` de s'abonner aux changements.
* `Consumer` — un composant abonné à un Provider

### Commençons à construire

Nous allons construire une application avec **deux** routes. L'une est **une page d'accueil** avec un accès global. L'autre est **une page de tableau de bord** avec un accès restreint pour les utilisateurs connectés. Vous pouvez trouver la [version finale ici](https://codesandbox.io/s/p71pr7jn50).

> _Essayez-le : allez sur /dashboard sans être connecté. Connectez-vous et naviguez librement entre les routes. Depuis le tableau de bord, déconnectez-vous et il vous redirigera vers la page d'accueil._

#### En-tête du Context

Pour démontrer la fonctionnalité de base du Context, commençons par construire un composant d'en-tête qui nous permet de nous connecter et de nous déconnecter. Tout d'abord, créons notre contexte dans un nouveau fichier.

```
/* AuthContext.js */
```

```
import React from 'react';
```

```
const AuthContext = React.createContext();
```

Exportez un composant `AuthProvider` pour définir notre état (si l'utilisateur est connecté) et passez son état à la prop `value` sur le `Provider`. Nous allons simplement exposer `AuthConsumer` avec un nom significatif.

```
/* AuthContext.js */
```

```
...
```

```
class AuthProvider extends React.Component {  state = { isAuth: false }
```

```
  render() {    return (      <AuthContext.Provider        value={{ isAuth: this.state.isAuth }}      >        {this.props.children}      </AuthContext.Provider>    )  }}
```

```
const AuthConsumer = AuthContext.Consumer
```

```
export { AuthProvider, AuthConsumer }
```

Dans index.js, enveloppez notre application dans `AuthProvider`.

```
/* index.js */import React from 'react';import { render } from 'react-dom';import { AuthProvider } from './AuthContext';import Header from './Header';
```

```
const App = () => (  <div>    <AuthProvider>      <Header />    </AuthProvider>  </div>);
```

```
render(<App />, document.getElementById('root'));
```

Maintenant, créons notre `Header` et importons notre `AuthConsumer` (je laisse de côté le style pour plus de clarté).

```
/* Header.js */import React from 'react'import { AuthConsumer } from './AuthContext'import { Link } from 'react-router-dom'
```

```
export default () => (  <header>    <AuthConsumer>    </AuthConsumer>  </header>)
```

Les Consumers de Context doivent avoir **une fonction comme enfant direct**. Cette fonction recevra la valeur de notre `Provider`.

```
/* Header.js */...export default () => (  <header>    <AuthConsumer>
```

```
      {({ isAuth }) => (        <div>          <h3>            <Link to="/">              ACCUEIL            </Link>          </h3>
```

```
          {isAuth ? (            <ul>              <Link to="/dashboard">                Tableau de bord              </Link>              <button>                déconnexion              </button>            </ul>          ) : (            <button>connexion</button>          )}        </div>      )}
```

```
    </AuthConsumer>  </header>)
```

Parce que `isAuth` est défini sur false, seul le bouton de connexion sera visible. Essayez de changer la valeur à `true` (il passera au bouton de déconnexion).

D'accord, essayons de basculer `isAuth` dans le code. Nous allons passer une fonction de connexion et de déconnexion depuis notre `Provider`.

```
/* AuthContext.js */...class AuthProvider extends React.Component {  state = { isAuth: false }
```

```
  constructor() {    super()    this.login = this.login.bind(this)    this.logout = this.logout.bind(this)  }
```

```
  login() {    // définition d'un timeout pour imiter une connexion asynchrone    setTimeout(() => this.setState({ isAuth: true }), 1000)  }
```

```
  logout() {    this.setState({ isAuth: false })  }
```

```
  render() {    return (      <AuthContext.Provider        value={{          isAuth: this.state.isAuth,          login: this.login,          logout: this.logout        }}      >        {this.props.children}      </AuthContext.Provider>    )  }}
```

Ces fonctions nous permettront de basculer notre état d'authentification dans `Header`.

```
/* Header.js */...export default () => (  <header>    <AuthConsumer>      {({ isAuth, login, logout }) => (        <div>          <h3>            <Link to="/">              ACCUEIL            </Link>          </h3>
```

```
          {isAuth ? (            <ul>              <Link to="/dashboard">                Tableau de bord              </Link>              <button onClick={logout}>                déconnexion              </button>            </ul>          ) : (            <button onClick={login}>connexion</button>          )}        </div>      )}    </AuthConsumer>  </header>)
```

### Route protégée avec Context

Maintenant que nous avons couvert les bases, étendons ce que nous avons appris pour créer un composant de route protégé.

Tout d'abord, créez les composants de page `Landing` et `Dashboard`. Notre tableau de bord ne sera visible que lorsque l'utilisateur est connecté. Les deux pages seront aussi simples que ci-dessous :

```
/* Dashboard.js */import React from 'react'
```

```
const Dashboard = () => <h2>Tableau de bord de l'utilisateur</h2>
```

```
export default Dashboard
```

Maintenant, routons vers ces pages.

```
/* index.js */import React from 'react';import { render } from 'react-dom';import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';import { AuthProvider } from './AuthContext';import Landing from './Landing';import Dashboard from './Dashboard';import Header from './Header';
```

```
const App = () => (  <div>    <Router>      <AuthProvider>        <Header />        <Switch>          <Route path="/dashboard" component={Dashboard} />          <Route path="/" component={Landing} />        </Switch>      </AuthProvider>    </Router>  </div>);
```

```
render(<App />, document.getElementById('root'));
```

Dans cet état actuel, vous pouvez naviguer vers `/` et `/dashboard`. Nous allons créer un composant de route spécial qui vérifie si un utilisateur est connecté, appelé `ProtectedRoute`. La configuration est similaire à notre composant `Header`.

```
/* ProtectedRoute.js */import React from 'react';import { Route, Redirect } from 'react-router-dom';import { AuthConsumer } from './AuthContext';
```

```
const ProtectedRoute = () => (  <AuthConsumer>    {({ isAuth }) => (
```

```
    )}  </AuthConsumer>);
```

```
export default ProtectedRoute;
```

La route privée fonctionnera exactement comme une route `react-router` normale, donc nous allons exposer le composant et toutes les autres props qui lui sont passées.

```
const ProtectedRoute = ({ component: Component, ...rest }) => (
```

Maintenant, la partie intéressante : nous allons utiliser la variable `isAuth` pour déterminer si elle doit rediriger ou rendre le composant de la route protégée.

```
const ProtectedRoute = ({ component: Component, ...rest }) => (  <AuthConsumer>    {({ isAuth }) => (      <Route        render={          props =>            isAuth             ? <Component {...props} />             : <Redirect to="/" />        }        {...rest}      />    )}  </AuthConsumer>)
```

Dans notre fichier `index`, importons `ProtectedRoute` et utilisons-le sur notre route de tableau de bord.

```
/* index.js */...
```

```
  <ProtectedRoute path="/dashboard" component={Dashboard} />
```

Super, maintenant nous avons des routes protégées ! Essayez de pointer le navigateur vers `/dashboard` et regardez-le vous renvoyer vers la page d'accueil.

Encore une fois, voici le lien pour la [démo fonctionnelle](https://codesandbox.io/s/p71pr7jn50). Lisez plus sur le Context dans la [Documentation Officielle de React](https://reactjs.org/docs/context.html).