---
title: Guide du débutant pour React Router 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T18:15:30.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-react-router-4-8959ceb3ad58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pLzme1OXO4RQbO3eZROkgw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: react-router-4
  slug: react-router-4
- name: Web Development
  slug: web-development
seo_title: Guide du débutant pour React Router 4
seo_desc: 'By Emmanuel Yusufu

  React is a JavaScript library for building user interfaces. With the React paradigm,
  every piece of the UI is a component that manages its own self-contained state (data)
  and functions.

  React, like other front-end JavaScript framew...'
---

Par Emmanuel Yusufu

React est une bibliothèque JavaScript pour créer des interfaces utilisateur. Avec le paradigme React, chaque partie de l'interface utilisateur est un composant qui gère son propre état (données) et ses propres fonctions de manière autonome.

React, comme d'autres frameworks JavaScript front-end, est utile pour créer des Applications à Page Unique (SPAs). Ce sont des applications web qui ne nécessitent pas un rechargement complet de la page lors d'un changement de vue. Au lieu de cela, elles échangent les vues à l'intérieur ou à l'extérieur d'une section de la page au fur et à mesure que l'utilisateur navigue dans l'application.

Bien que les SPAs offrent une expérience de navigation fluide pour les utilisateurs, les fonctionnalités de routage des sites web traditionnels sont attendues.

Par exemple :

* chaque vue à l'écran doit avoir sa propre URL spécifique afin que je puisse ajouter la page aux favoris.
* Les boutons suivant et précédent doivent me permettre d'avancer ou de reculer dans mon historique de navigation.
* Les vues imbriquées et celles avec des paramètres doivent être prises en charge, comme `**example.com/products/shoes/101**`.

Dans la communauté React, React Router est la bibliothèque préférée pour gérer le routage. L'aspect le plus convaincant de cette version de la bibliothèque est qu'elle est « juste du React ». Les routes sont simplement des composants qui sont rendus à l'écran lorsque l'application est en cours d'exécution. Elles ne sont pas définies dans des fichiers externes comme c'est le cas dans d'autres frameworks.

### Prérequis

Vous aurez besoin des éléments suivants : **Connaissances de base de [React](https://reactjs.org/)**, [**Git**](https://git-scm.com/) **installé sur votre ordinateur**, et [**NPM**](https://www.npmjs.com/) **installé sur votre ordinateur**.

### Configuration

Si vous avez Git installé, localisez les [fichiers sources](https://github.com/emmyyusufu/react-router-demos) vides (sur la branche **_master_**) et clonez-les sur votre ordinateur en utilisant :

```
git clone https://github.com/emmyyusufu/react-router-demos.git
```

Ouvrez le dossier dans votre éditeur de texte et découvrez les sous-dossiers à l'intérieur :

![Image](https://cdn-media-1.freecodecamp.org/images/XRn9UAhItLVs86chje0B66vJQMZPxQrrVZqG)

Cet article est divisé en quatre sous-sections correspondant aux dossiers qui sont : `**Basic routing**` (Routage de base), `**Nested routing**` (Routage imbriqué), `**Nested routing with path parameters**` (Routage imbriqué avec paramètres de chemin) et `**Authenticated routing**` (Routage authentifié).

Pour lancer les démos, ouvrez un dossier donné dans votre terminal puis exécutez `npm install` suivi de `npm start`.

### #1 Routage de base

Commençons de zéro. Notez la structure du dossier de routage de base.

![Image](https://cdn-media-1.freecodecamp.org/images/Pud2nRBawlErdg9HXTiHOvT-6ALjicE-sHv-)
_Structure de dossier create-react-app modifiée._

Toutes les démos de cet article ont été initialement créées à l'aide de [create-react-app](https://github.com/facebookincubator/create-react-app). Cela apporte certains avantages tels qu'un serveur Webpack déjà configuré qui regrouperait tous les fichiers JavaScript de notre application dans un fichier `**bundle.js**` qui serait attaché au fichier `**index.html**` au moment de l'exécution. Au moment de l'exécution, le serveur de développement de Webpack écoutera tout changement dans notre fichier et le mettra à jour au fur et à mesure que l'application s'exécute pendant le développement.

J'ai créé un dossier `**components/**` pour conserver tous nos composants. Notez que :

* `**index.js**` est le fichier d'entrée de tous les fichiers `**.js**` de notre application. C'est là que le regroupement de Webpack sera effectué, donc tous les fichiers `**.js**` doivent y être importés.
* Le fichier `**App.js**` contiendra tout ce qui concerne notre application React.

Par défaut, create-react-app ne place pas `**App.js**` dans ce dossier. Mais parce que j'ai modifié la structure du dossier, j'ai apporté les modifications appropriées à l'URL du chemin et je l'ai importé dans `**index.js**`. Pour en savoir plus sur create-react-app, cette [référence](https://github.com/facebookincubator/create-react-app) serait utile.

Naviguez vers le premier dossier `**01-basic-routing**` et exécutez `npm install`.

Ouvrez le fichier `App.js` et vous devriez voir ce qui suit :

```
import React, { Component } from 'react';import '../styles/App.css';
```

```
// importer les composants de route ici
```

```
class App extends Component {  render() {    return (      <div className="App">
```

```
<div className="container">          <ul>            <li><a href="">Hello</a></li>            <li><a href="">About</a></li>            <li><a href="">Books</a></li>          </ul>          <hr/>
```

```
{/* Les routes iront ici */}
```

```
</div>
```

```
</div>    );  }}
```

```
export default App;
```

Exécutez npm start et visualisez l'application. Aucune modification n'a encore été apportée.

![Image](https://cdn-media-1.freecodecamp.org/images/fC9N5djph47YrTSWQ8jZLeDsoYR1FlkEQtch)
_Aucun changement effectué_

Installons React Router via NPM. Avec le dossier ouvert dans votre terminal, exécutez :

```
npm install react-router-dom
```

Pourquoi `**react-router-dom**` ? C'est parce que la bibliothèque React Router se compose de trois packages : `react-router`, `react-router-dom` et `react-router-native`.

`react-router` est le package principal pour le routeur, tandis que les deux autres sont spécifiques à l'environnement. Vous devriez utiliser `react-router-dom` si vous développez pour le web, et `react-router-native` si vous êtes dans un environnement de développement d'applications mobiles utilisant React Native.

Importez ce qui suit dans `**App.js**` :

```
// importer les composants de route ici
import {  BrowserRouter as Router,  Route,  Link,  Switch,  Redirect} from 'react-router-dom'
```

Plus tard, nous comprendrons ce que font ces composants. Tous les composants de routage dépendent de `BrowserRouter` pour leur fournir les APIs History de HTML5 du navigateur.

Notez que les **composants React** ont leur première lettre en majuscule afin de les identifier différemment des balises HTML par défaut.

_L'API History est un objet qui nous permet de gérer l'emplacement actuel via `history.location` ainsi que les emplacements précédents. Considérez la propriété `location` de l'objet comme un tableau. L'emplacement actuel est le dernier élément du tableau et nous manipulons le tableau via des méthodes telles que `history.push()` ou `history.replace`. Quelle que soit la manipulation effectuée sur le tableau, elle déclenchera une transition de page vers l'emplacement actuel. C'est ce qui se passe en coulisses lors de l'utilisation des composants `Link` et `Redirect` comme nous le verrons bientôt._

Nous avons importé le contenu de `BrowserRouter` dans la variable `Router`. Nous devons envelopper toute notre application avec lui afin qu'il fournisse les APIs nécessaires dans toute l'application. Dans `**App.js**`, ajoutez :

```
import React, { Component } from 'react';import '../styles/App.css';
```

```
// importer les composants de route ici
import {  BrowserRouter as Router,  Route,  Link,  Switch,  Redirect} from 'react-router-dom'
```

```
class App extends Component {  render() {    return (      <Router>        <div className="App">
```

```
<div className="container">            <ul>              <li><a href="">Hello</a></li>              <li><a href="">About</a></li>              <li><a href="">Books</a></li>            </ul>            <hr/>
```

```
{/* Les routes iront ici */}
```

```
</div>        </div>      </Router>    );  }}
```

```
export default App;
```

#### Le composant <Route />

Commençons à explorer le composant `Route`. Ce composant affiche une page si l'**emplacement URL actuel** correspond à la prop `path` spécifiée. Il accepte également les props `component`, `render` et `[children](https://reacttraining.com/react-router/web/api/Route/children-func)`.

Créons les nôtres là où il est écrit **{/* Les routes iront ici */}:**

```
<Route path="/hello" component={Hello} /><Route path="/about" component={About} /><Route path="/books" component={Books} />
```

Mais ces composants n'existent pas ! Oui, vous avez raison.

Encore une fois, avant de les créer, ajoutons plus d'imports à `App.js`. Importez depuis `HelloComponent.js`, `AboutComponent.js` et `BooksComponent.js` en utilisant `Hello`, `About` et `Books` comme variables. **La prop `component={}` utilise des accolades pour faire référence à des variables et non à des chaînes de caractères.**

```
import React, { Component } from 'react';import '../styles/App.css';
```

```
import Hello from './HelloComponent';import About from './AboutComponent';import Books from './BooksComponent';
```

```
// importer les composants de route ici
import {  BrowserRouter as Router,  Route,  Link,  Switch,  Redirect} from 'react-router-dom'
```

Notez que `render` est similaire à `component={}` mais il nous permet de définir un composant en ligne et directement sur place :

```
<Route path="/hello" render={() => {           return (              <div className="jumbotron">                <h1 className="display-3">Hello, world!</h1>              </div>             );      }}/>
```

Allez dans le fichier `HelloComponent.js` vide et collez :

```
import React from 'react';
```

```
const Hello = () => {    return (        <div className="jumbotron">            <h1 className="display-3">Hello, world!</h1>        </div>    );}
```

```
export default Hello;
```

Nous avons utilisé un composant fonctionnel sans état (Stateless functional component) ci-dessus. Nous les utilisons pour les composants qui ne rendent que du contenu statique sur une page web, par opposition aux composants qui rendent du contenu avec état/changeant.

Si vous ne l'avez pas remarqué, nous utilisons les styles Bootstrap 4 dans notre fichier `App.css`, d'où la classe `jumbotron` dans le `div`.

```
// à l'intérieur de App.css. Vous aurez besoin d'une connexion Internet pour charger les styles Bootstrap 4.
```

```
.App {  padding-top: 50px;}
```

```
@import url('https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css');
```

Allez dans le fichier `AboutComponent.js` vide et collez :

```
import React from 'react';
```

```
const About = () => {    return (        <div className="jumbotron">            <h1 className="display-3">About Me</h1>        </div>    );}
```

```
export default About;
```

Enfin, allez dans le fichier `BooksComponent.js` vide et collez :

```
import React from 'react';
```

```
const Books = () => {    return (        <div className="jumbotron">            <h1 className="display-3">My Books</h1>        </div>    );}
```

```
export default Books;
```

Une dernière chose dont nous avons besoin pour conclure cette section est le composant `Link`.

#### Le composant <Link></Link>

Celui-ci remplace la balise HTML par défaut `<a href=""></a>`. Il accepte une prop `to=""` qui pointe vers l'emplacement URL où nous voulons aller.

À l'intérieur de `App.js`, remplacez les balises d'ancrage par défaut par `Link` :

```
<ul>   <li><Link to="/hello">Hello</Link></li>   <li><Link to="/about">About</Link></li>   <li><Link to="/books">Books</Link></li></ul>
```

Exécutez `npm start` depuis votre terminal et voyez l'application complète :

![Image](https://cdn-media-1.freecodecamp.org/images/Bikt0cXslah4RGYMXJaH9lahKt4XQDq-VHx2)
_utilisation de Route et Link_

Comment rendriez-vous un composant si l'URL `/` est visitée, comme la page d'accueil ? Votre idée pourrait être de créer une route pour cela :

```
<Route path="/" component={Home} />
```

C'est bien, mais rappelez-vous que les autres chemins contiennent `/`. Donc, si nous visitions d'autres URLs telles que `/hello`, `/about` et `/books`, le composant `Home` continuerait d'être rendu par défaut. Pour corriger cela, écrivez une autre prop `exact` en la réglant sur `true` ou écrivez simplement `exact`.

```
<Route path="/" exact={true} component={Home} />
```

Cela garantirait que le composant `Home` ne soit rendu que dans les cas où l'URL correspond exactement à ceci : `/`.

Créez un nouveau fichier `HomeComponent.js` dans le dossier `**components/**`. Collez ceci dedans :

```
import React from 'react';
```

```
const Home = () => {    return (        <div className="jumbotron">            <h1 className="display-3">Landing page</h1>        </div>    );}
```

```
export default Home;
```

Importez-le dans `App.js` :

```
import Home from './HomeComponent';
```

Ajoutez-le à la liste des routes :

```
<Route exact={true} path="/" component={Home} /><Route path="/hello" component={Hello} /><Route path="/about" component={About} /><Route path="/books" component={Books} />
```

Visitez `http://localhost:3000` et visualisez :

![Image](https://cdn-media-1.freecodecamp.org/images/ZsRK0kSHsjC4ktFeW7iP9tWRpKP49s-w7dWb)
_Composant Home rendu sur le chemin '/'_

Faites quelques expériences. Supprimez `exact={true}` de la route Home et voyez ce qui se passe. Vous verrez pourquoi c'est important.

![Image](https://cdn-media-1.freecodecamp.org/images/IZKcPI-ckbkiqnv-AcYaBJZSRLAmvObQe9VC)
_Utilisez toujours exact={true} sur le chemin '/', sinon chaque <Route /> sera rendue._

#### Le composant <Switch></Switch>

Cela nécessitera d'être enveloppé autour des composants `Route` lorsque cela est nécessaire pour l'implémentation. Lorsqu'un chemin URL est visité, il permet uniquement à la première `<Route>` qui correspond au chemin d'être rendue.

Plus tôt, nous avions un problème avec `/` rendant le composant `Home` et celui d'autres chemins. Si nous créons un chemin `/hello/goodmorning`, que se passera-t-il ? Les composants du chemin `/hello` et `/hello/goodmorning` seront rendus. Switch aidera dans ce cas également en choisissant une seule route à rendre, mais la route la plus importante doit être disposée en premier.

![Image](https://cdn-media-1.freecodecamp.org/images/kko7Mjm1XatlbgdBczhMEYgt6-ty1jCnG6xn)
_Juste une expérience_

En utilisant `Switch`, nous pouvons éviter ce qui se passe dans l'image ci-dessus, mais seulement pour les URLs autres que `/`. `exact={true}` s'en occupe pour `/`. Rappelez-vous que `Switch` ne choisira que la première `Route` correspondante. Mettons-le à l'œuvre et voyons le résultat.

```
<Switch>    <Route exact path="/" component={Home} />    <Route path="/hello" component={Hello} />    <Route path="/hello/goodmorning" render={() => { return      <h1>Goodmorning</h1> }} />    <Route path="/books" component={Books} /></Switch>
```

![Image](https://cdn-media-1.freecodecamp.org/images/Y3oc88nscEDu-lRKnUIdD6f9NvxgM9WBaANZ)
_Seule la première route qui correspond à /hello/goodmorning est rendue._

De plus, `Switch` nous permet de spécifier une route à rendre si l'URL ne correspond à aucun emplacement. Pour cette route, laissez la prop `path` vide.

```
// Juste un exemple. Ne pas implémenter. Cette route fourre-tout serait en bas si elle était implémentée.
```

```
<Route component={NoMatch} />
```

En résumé, `Switch` fera ce qui suit :

* éviter le rendu de routes inclusives.
* inclure une route fourre-tout (catch-all) au bas de notre conteneur Switch.

### #2 Routage imbriqué

Rappelez-vous que nous pouvions rendre des composants via `Route` en ligne ou en spécifiant le composant :

```
<Route component={SomeComponent}/>
```

Ou

```
<Route render={() => { return <h1>Quelque chose</h1> }/>
```

Le composant qui sera créé via `Route` se verra automatiquement transmettre les objets `prop` suivants :

* match
* location
* history

Nous n'explorerons que l'utilisation de `match` car il est utile pour implémenter des routes imbriquées. L'objet `match` contient les propriétés suivantes :

* **params** — (objet) Paires clé/valeur analysées à partir de l'URL correspondant aux segments dynamiques du chemin.
* **isExact** — (booléen) vrai si l'URL entière correspondait (pas de caractères de fin).
* **path** — (chaîne) Le modèle de chemin utilisé pour la correspondance. Utile pour construire des `<Route>` imbriquées.
* **url** — (chaîne) La partie correspondante de l'URL. Utile pour construire des `<Link>` imbriqués.

Nous voulons ajouter de nouvelles routes sous la route `/book`. Ce seront des livres :

* HTML
* CSS
* React

Naviguez vers le deuxième sous-dossier `**02-nested-routing**` sur votre terminal et exécutez `npm install`.

In votre éditeur de code, ouvrez `BookComponent.js` et modifiez :

```
const Books = ({ match }) => {    return (<div>   <div className="jumbotron">        <h1 className="display-3">My Books</h1>   </div>
```

```
  <div className="container">    <div className="row">
```

```
      <div className="col-md-3">          <ul>            <li><Link to="">HTML</Link></li>            <li><Link to="">CSS</Link></li>            <li><Link to="">React</Link></li>          </ul>      </div>      <div className="col-md-9">
```

```
               {/* placer les routes ici */}      </div>    </div>
```

```
   </div>
```

```
</div>    );}
```

Installons React Router via NPM. Avec le dossier ouvert dans votre terminal, exécutez :

```
npm install react-router-dom
```

Nous avons démontré syntaxiquement que l'objet `match` est passé en tant que `props`. N'oubliez pas que les classes utilisées sont destinées à l'application des styles de Bootstrap. N'oubliez pas d'importer tous les composants de React Router après avoir importé React :

```
import React from 'react';import {    BrowserRouter as Router,    Route,    Link,    Switch,    Redirect  } from 'react-router-dom';
```

Nous n'avions pas besoin de tous les importer mais nous l'avons fait quand même. Placez les routes :

```
<Route path="" render={() => { return <h1>Livre HTML par Ducket</h1> }}/><Route path="" render={() => { return <h1>CSS par Racheal Andrews</h1> }}/><Route path="" render={() => { return <h1>Livre React par Fullstack.io</h1> }}/>
```

Nous utilisons le rendu de composant en ligne pour gagner du temps. Maintenant, remplissons le `to=""` de `Link` et le `path=""` de `Route`.

Apportez ces modifications :

```
<div className="col-md-3">    <ul>      <li><Link to={`${match.url}/html`}>HTML</Link></li>      <li><Link to={`${match.url}/css`}>CSS</Link></li>      <li><Link to={`${match.url}/react`}>React</Link></li>     </ul></div> <div className="col-md-9">
```

```
      <Route path={`${match.path}/html`} render={() => { return <h1>Livre HTML par Ducket</h1> }}/>      <Route path={`${match.path}/css`} render={() => { return <h1>CSS par Racheal Andrews</h1> }}/>      <Route path={`${match.path}/react`} render={() => { return <h1>Livre React par Fullstack.io</h1> }}/>
```

```
</div>
```

`${match.url}` s'évalue à `/books` et `${match.path}` s'évalue à `localhost://3000/books`. Les backticks (accents graves) utilisés sont la manière d'ES6 de concaténer des chaînes contenant des variables.

Sauvegardez, exécutez `npm start` et visualisez l'application fonctionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/W0Cakd4qGPzbCGb0otMjwNHTNTg6z-Rc7i-o)
_Routes imbriquées_

### #3 Routage imbriqué avec paramètres de chemin

Toute URL qui se termine par `/:id`, `/:user` ou `/:nimporte-quoi` indique que cette partie est une partie générée dynamiquement de l'URL qui pourrait être n'importe quelle valeur.

Nous pouvons accéder à ces parties via `match.params.id` pour une utilisation dans le routage.

Ouvrez à nouveau le troisième sous-dossier `**03-nested-routing-with-path-parameters**` dans votre terminal et exécutez `npm install`.

De plus, installons React Router via NPM. Avec le dossier ouvert dans votre terminal, exécutez :

```
npm install react-router-dom
```

Pour illustrer comment les paramètres de chemin peuvent être utilisés pour le routage, collez ce qui suit dans `Book.js` :

```
import React from 'react';import {    BrowserRouter as Router,    Route,    Link,    Switch,    Redirect  } from 'react-router-dom';
```

```
const Books = ({ match }) => {    return (        <div>            <div className="jumbotron">                <h1 className="display-3">My Books</h1>            </div>
```

```
<div className="container">          <div className="row">              <div className="col-md-3">          <ul>              <li><Link to={`${match.url}/html`}>HTML</Link></li>              <li><Link to={`${match.url}/css`}>CSS</Link></li>              <li><Link to={`${match.url}/react`}>React</Link></li>          </ul>                </div>                <div className="col-md-9">                    <Route path={`${match.path}/html`} render={() => { return <h1>Livre HTML par Ducket</h1> }}/>                    <Route path={`${match.path}/css`} render={() => { return <h1>CSS par Racheal Andrews</h1> }}/>                    <Route path={`${match.path}/react`} render={() => { return <h1>Livre React par Fullstack.io</h1> }}/>                    <Route path={`${match.path}/:id`} component={Child} />                </div>            </div>            </div>        </div>    );}
```

```
const Child = ({ match }) => (    <div>      <h3>Paramètre ID de l'URL : {match.params.id}</h3>    </div>);
```

```
export default Books;
```

Exécutez `npm start`.

![Image](https://cdn-media-1.freecodecamp.org/images/nFQfQLFAgCL1vj80YweZ630o3bzFqjTIOz9j)
_accès à la valeur du paramètre /:id_

### #4 Routage de chemin protégé

Ce type de routage est destiné aux pages d'un site web qui nécessitent que l'utilisateur se connecte et soit authentifié avant de visualiser ces pages. Un exemple est une page **Admin**.

Pour gérer les chemins protégés, nous devrons utiliser `<Redirect/>` (un composant standard) et `<PrivateRoute/>` (un composant personnalisé).

`<PrivateRoute/>` n'est pas le composant `<Route/>` standard. Le composant de route standard fourni par React Router est `<Route/>`. Nous définirons `<PrivateRoute/>` comme notre propre `<Route/>` personnalisé.

Les routes personnalisées sont nécessaires lorsque nous devons prendre une décision quant à savoir si une `<Route/>` d'intérêt doit être rendue ou non. Comme vous le verrez dans le code, nous listerons `<PrivateRoute/>` avec d'autres `<Route/>`s.

### Le composant <Redirect/>

Le rendu d'un `<Redirect>` naviguera vers un nouvel emplacement. Le nouvel emplacement remplacera l'emplacement actuel dans la pile d'historique, comme le font les redirections côté serveur (HTTP 3xx).

`<Redirect/>` possède quelques props mais nous utiliserons la prop d'objet `to` de cette façon :

```
<Redirect to={{        pathname: '/login',        state: { from: props.location }      }}/>
```

Lorsqu'il est utilisé, cela redirigera vers le chemin `/login`. Les informations sur le dernier emplacement avant la redirection seront accessibles par le composant `LoginPage` via `this.props.location.state`.

Naviguez vers le dernier sous-dossier `**04-authenticated-routing**`. Exécutez `npm install`.

Installez React Router via NPM. Avec le dossier ouvert dans votre terminal, exécutez :

```
npm install react-router-dom
```

Ouvrez `App.js` et ajoutez un nouvel élément de liste `/admin` aux éléments existants.

```
<ul>     <li><Link to="/hello">Hello</Link></li>     <li><Link to="/about">About</Link></li>     <li>         <Link to="/books">Books</Link>     </li>     <li>         <Link to="/admin">Admin</Link>     </li></ul>
```

Ajoutez `<PrivateRoute/>` et la route `/login` au groupe de `<Route/>`s existantes.

```
<Switch>            <Route exact path="/" component={Home} />            <Route path="/about" component={About} />            <Route path="/hello" component={Hello} />            <Route path="/books" component={Books} />            <Route path="/login" component={Login}/>            <PrivateRoute authed={fakeAuth.isAuthenticated} path="/admin" component={Admin} />          </Switch>
```

Maintenant, créez le composant `<PrivateRoute/>` en dehors du composant App :

```
const PrivateRoute = ({ component: Component, ...rest }) => (  <Route {...rest} render={props => (    fakeAuth.isAuthenticated ? (      <Component {...props}/>    ) : (      <Redirect to={{        pathname: '/login',        state: { from: props.location }      }}/>    )  )}/>)
```

`<PrivateRoute/>` finira par se réduire à un composant `<Route>`. Le composant `<Route>` utilise une opération ternaire pour déterminer quoi rendre selon que l'utilisateur est connecté ou non : un `<Redirect/>` vers la page de connexion ou le composant de la page Admin.

Créez le composant `Admin` :

```
const Admin = () => {  return (    <div className="jumbotron">      <h3 className="display-3">Accès Admin accordé</h3>    </div>  );}
```

Créez également le composant `Login` :

```
class Login extends React.Component {      constructor() {      super();        this.state = {        redirectToReferrer: false      }      // liaison de 'this'
      this.login = this.login.bind(this);    }      login() {        fakeAuth.authenticate(() => {        this.setState({ redirectToReferrer: true })      })    }      render() {      const { from } = this.props.location.state || { from: { pathname: '/' } }      const { redirectToReferrer } = this.state;        if (redirectToReferrer) {        return (          <Redirect to={from} />        )      }        return (        <div className="jumbotron">            <h1 className="display-3">Connexion requise</h1>            <p className="lead">Vous devez vous connecter pour voir la page à l'adresse {from.pathname}.</p>            <p className="lead">              <a className="btn btn-primary btn-lg" onClick={this.login} role="button">Connexion</a>            </p>        </div>      )    }  }    /* Une fausse fonction d'authentification */
  export const fakeAuth = {      isAuthenticated: false,    authenticate(cb) {      this.isAuthenticated = true       setTimeout(cb, 100)    },  }
```

Ce composant `Login` implémente une fausse fonction d'authentification qui définira un utilisateur comme étant connecté ou déconnecté.

Exécutez `npm start` et voyez l'application fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/PzSzkdxoxPdjdiLrnpGfrcPyxeGPSyElyqeg)
_Processus d'authentification_

Cela nous amène à la fin de l'article. Félicitations à vous si vous êtes arrivé jusqu'ici. Si vous souhaitez plus de détails sur React Router, consultez la [Documentation](https://reacttraining.com/react-router/web/guides/philosophy).

Si vous souhaitez la version complète du code, visitez la branche completed sur [Github](https://github.com/emmyyusufu/react-router-demos/tree/completed).

N'hésitez pas à me soutenir ([devapparel.co](http://www.devapparel.co)) et à avoir du style en le faisant. N'hésitez pas non plus à commenter ou à partager cet article. Merci de votre lecture !

_Publié à l'origine sur le [blog Zeolearn](https://www.zeolearn.com/magazine/beginners-guide-to-react-router-4)._