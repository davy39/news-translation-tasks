---
title: Un guide complet pour débutants sur React Router (y compris les Hooks de Router)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T11:05:00.000Z'
originalURL: https://freecodecamp.org/news/a-complete-beginners-guide-to-react-router-include-router-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover.png
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Un guide complet pour débutants sur React Router (y compris les Hooks de
  Router)
seo_desc: 'By Ibrahima Ndaw

  React is a JavaScript library for building user interfaces. We can also extend it
  to build multi-page applications with the help of React Router. This is a third-party
  library that enables routing in our React apps.

  In this tutorial,...'
---

Par Ibrahima Ndaw

React est une bibliothèque JavaScript pour construire des interfaces utilisateur. Nous pouvons également l'étendre pour construire des applications multi-pages avec l'aide de React Router. Il s'agit d'une bibliothèque tierce qui permet le routage dans nos applications React.

Dans ce tutoriel, nous allons couvrir tout ce que vous devez savoir pour commencer avec React Router.

* [Installation du projet](#heading-installation)
* [Qu'est-ce que le routage ?](#heading-quest-ce-que-le-routage)
* [Configuration du routeur](#heading-configuration-du-routeur)
* [Rendu des routes](#heading-rendu-des-routes)
* [Utilisation des liens pour changer de pages](#heading-utilisation-des-liens-pour-changer-de-pages)
* [Passage de paramètres de route](#heading-passage-de-parametres-de-route)
* [Navigation programmatique](#heading-navigation-programmatique)
* [Redirection vers une autre page](#heading-redirection-vers-une-autre-page)
* [Redirection vers une page 404](#heading-redirection-vers-une-page-404)
* [Protection des routes](#heading-protection-des-routes)
* [Hooks du routeur](#heading-hooks-du-routeur)
* [useHistory](#heading-usehistory)
* [useParams](#heading-useparams)
* [useLocation](#heading-uselocation)
* [Réflexions finales](#heading-reflexions-finales)
* [Prochaines étapes](#heading-prochaines-etapes)

## Installation du projet

Pour pouvoir suivre ce tutoriel, vous devrez créer une nouvelle application React en exécutant la commande suivante dans votre terminal :

```shell
npx create-react-app react-router-guide

```

Ensuite, ajoutez ces lignes de code au fichier `App.js` :

```jsx
import React from "react";
import "./index.css"

export default function App() {
  return (
    <main>
      <nav>
        <ul>
          <li><a href="/">Accueil</a></li>
          <li><a href="/about">À propos</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
        </nav>
     </main>
  );
}
// Page d'accueil
const Home = () => (
  <Fragment>
    <h1>Accueil</h1>
    <FakeText />
  </Fragment>
  );
// Page À propos
const About = () => (
  <Fragment>
    <h1>À propos</h1>
    <FakeText />
  </Fragment>
  );
// Page Contact
const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

const FakeText = () => (
  <p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </p>
  )

```

Ensuite, si vous êtes prêt, commençons par répondre à une question importante : qu'est-ce que le routage ?

## Qu'est-ce que le routage ?

Le routage est la capacité de montrer différentes pages à l'utilisateur. Cela signifie que l'utilisateur peut se déplacer entre différentes parties d'une application en entrant une URL ou en cliquant sur un élément.

Comme vous le savez peut-être déjà, par défaut, React ne dispose pas de routage. Et pour l'activer dans notre projet, nous devons ajouter une bibliothèque nommée [react-router](https://reacttraining.com/react-router/web/guides/quick-start).

Pour l'installer, vous devrez exécuter la commande suivante dans votre terminal :

```shell
yarn add react-router-dom

```

Ou

```shell
npm install react-router-dom

```

Maintenant, nous avons installé notre routeur avec succès, commençons à l'utiliser dans la section suivante.

## Configuration du routeur

Pour activer le routage dans notre application React, nous devons d'abord importer `BrowserRouter` depuis `react-router-dom`.

Dans le fichier `App.js`, entrez ce qui suit :

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
  <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Accueil</a></li>
          <li><a href="/about">À propos</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
    </main>
</Router>
  );
}

```

Cela devrait contenir tout dans notre application où le routage est nécessaire. Cela signifie que si nous avons besoin de routage dans toute notre application, nous devons envelopper notre composant supérieur avec `BrowserRouter`.

Au fait, vous n'êtes pas obligé de renommer `BrowserRouter as Router` comme je le fais ici, je veux juste garder les choses lisibles.

Un routeur seul ne fait pas grand-chose. Ajoutons donc une route dans la section suivante.

## Rendu des routes

Pour rendre les routes, nous devons importer le composant `Route` depuis le package du routeur.

Dans votre fichier `App.js`, ajoutez le code suivant :

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
  <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Accueil</a></li>
          <li><a href="/about">À propos</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
  <Route path="/" render={() => <h1>Bienvenue !</h1>} />
    </main>
</Router>
  );
}

```

Ensuite, ajoutez-le là où nous voulons rendre le contenu. Le composant `Route` a plusieurs propriétés. Mais ici, nous avons juste besoin de `path` et `render`.

`path` : le chemin de la route. Ici, nous utilisons `/` pour définir le chemin de la page d'accueil.

`render` : affichera le contenu chaque fois que la route est atteinte. Ici, nous allons afficher un message de bienvenue à l'utilisateur.

Dans certains cas, servir des routes comme cela est parfaitement acceptable. Mais imaginez un cas où nous devons gérer un vrai composant – utiliser `render` peut ne pas être la bonne solution.

Alors, comment pouvons-nous afficher un vrai composant ? Eh bien, le composant `Route` a une autre propriété nommée `component`.

Mettons à jour notre exemple un peu pour le voir en action.

Dans votre fichier `App.js`, ajoutez le code suivant :

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Accueil</a></li>
          <li><a href="/about">À propos</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>

    <Route path="/" component={Home} />
    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Accueil</h1>
    <FakeText />
  </Fragment>
  );

```

Maintenant, au lieu de rendre un message, notre route va charger le composant `Home`.

Pour obtenir toute la puissance de React Router, nous devons avoir plusieurs pages et des liens avec lesquels jouer. Nous avons déjà des pages (des composants si vous voulez), alors maintenant ajoutons quelques liens pour pouvoir changer de pages.

## Utilisation des liens pour changer de pages

Pour ajouter des liens à notre projet, nous allons utiliser React Router à nouveau.

Dans votre fichier `App.js`, ajoutez le code suivant :

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

export default function App() {
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Accueil</Link></li>
          <li><Link to="/about">À propos</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>

    <Route path="/" exact component={Home} />
    <Route path="/about"  component={About} />
    <Route path="/contact"  component={Contact} />

    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Accueil</h1>
    <FakeText />
  </Fragment>
  );

const About = () => (
  <Fragment>
    <h1>À propos</h1>
    <FakeText />
  </Fragment>
  );

const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

```

Après avoir importé `Link`, nous devons mettre à jour notre barre de navigation un peu. Maintenant, au lieu d'utiliser la balise `a` et `href`, React Router utilise `Link` et `to` pour, eh bien, pouvoir changer de pages sans recharger la page.

Ensuite, nous devons ajouter deux nouvelles routes, `About` et `Contact`, pour pouvoir changer de pages ou de composants.

Maintenant, nous pouvons aller à différentes parties de notre application via des liens. Mais il y a un problème avec notre routeur : le composant `Home` est toujours affiché même si nous changeons pour d'autres pages.

C'est parce que React Router va vérifier si le `path` défini commence par `/`. Si c'est le cas, il va rendre le composant. Et ici, notre première route commence par `/`, donc le composant `Home` sera rendu chaque fois.

Cependant, nous pouvons encore changer le comportement par défaut en ajoutant la propriété `exact` à `Route`.

Dans `App.js`, ajoutez :

```jsx
    <Route path="/" exact component={Home} />

```

En mettant à jour la route `Home` avec `exact`, maintenant elle ne sera rendue que si elle correspond au chemin complet.

Nous pouvons encore l'améliorer en enveloppant nos routes avec `Switch` pour dire à React Router de charger une seule route à la fois.

Dans `App.js`, ajoutez :

```jsx
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

  <Switch>
    <Route path="/" exact component={Home} />
    <Route path="/about"  component={About} />
    <Route path="/contact"  component={Contact} />
  </Switch>

```

Maintenant que nous avons de nouveaux liens, utilisons-les pour passer des paramètres.

## Passage de paramètres de route

Pour passer des données entre les pages, nous devons mettre à jour notre exemple.

Dans votre fichier `App.js`, ajoutez le code suivant :

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Accueil</Link></li>
          <li><Link to={`/about/${name}`}>À propos</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
    </Switch>
    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Accueil</h1>
    <FakeText />
  </Fragment>
  );

const About = ({match:{params:{name}}}) => (
  // props.match.params.name
  <Fragment>
    <h1>À propos de {name}</h1>
    <FakeText />
  </Fragment>
);

const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

```

Comme vous pouvez le voir ici, nous commençons par déclarer une nouvelle constante `name` qui sera passée en tant que paramètre à la page `About`. Et nous ajoutons `name` au lien correspondant.

Avec cela, nous devons maintenant mettre à jour la route `About` en ajustant son chemin pour recevoir `name` en tant que paramètre `path="/about/:name"`.

Maintenant, le paramètre sera reçu en tant que props depuis le composant `About`. La seule chose que nous devons faire maintenant est de déstructurer les props et de récupérer la propriété `name`. Au fait, `{match:{params:{name}}}` est la même chose que `props.match.params.name`.

Nous avons fait beaucoup de choses jusqu'à présent. Mais dans certains cas, nous ne voulons pas utiliser de liens pour naviguer entre les pages.

Parfois, nous devons attendre qu'une opération se termine avant de naviguer vers la page suivante.

Alors, traitons ce cas dans la section suivante.

## Navigation programmatique

Les props que nous recevons ont quelques méthodes pratiques que nous pouvons utiliser pour naviguer entre les pages.

Dans `App.js`, ajoutez :

```jsx
const Contact = ({history}) => (
  <Fragment>
    <h1>Contact</h1>
    <button onClick={() => history.push('/') } >Aller à l'accueil</button>
    <FakeText />
  </Fragment>
  );

```

Ici, nous extrayons l'objet `history` des props que nous recevons. Il a quelques méthodes pratiques comme `goBack`, `goForward`, et ainsi de suite. Mais ici, nous allons utiliser la méthode `push` pour pouvoir aller à la page d'accueil.

Maintenant, traitons le cas où nous voulons rediriger notre utilisateur après une action.

## Redirection vers une autre page

React Router a un autre composant nommé `Redirect`. Comme vous l'avez deviné, il nous aide à rediriger l'utilisateur vers une autre page.

Dans `App.js`, ajoutez :

```jsx
import { BrowserRouter as Router, Route, Link, Switch, Redirect } from "react-router-dom";

const About = ({match:{params:{name}}}) => (
  // props.match.params.name
  <Fragment>
    { name !== 'John Doe' ? <Redirect to="/" /> : null }
    <h1>À propos de {name}</h1>
    <FakeText />
  </Fragment>
);

```

Maintenant, si le `name` passé en tant que paramètre n'est pas égal à `John Doe`, l'utilisateur sera redirigé vers la page d'accueil.

Vous pourriez argumenter que vous devriez rediriger l'utilisateur avec `props.history.push('/)`. Eh bien, le composant `Redirect` remplace la page et donc l'utilisateur ne peut pas revenir à la page précédente. Mais, avec la méthode push, ils le peuvent. Cependant, vous pouvez utiliser `props.history.replace('/)` pour imiter le comportement de `Redirect`.

Maintenant, passons à la suite et traitons le cas où l'utilisateur atteint une route qui n'existe pas.

## Redirection vers une page 404

Pour rediriger l'utilisateur vers une page 404, vous pouvez créer un composant pour l'afficher. Mais ici, pour garder les choses simples, je vais juste afficher un message avec `render`.

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Accueil</Link></li>
          <li><Link to={`/about/${name}`}>À propos</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
      <Route render={() => <h1>404 : page non trouvée</h1>} />
      
    </Switch>
    </main>
</Router>
  );
}

```

La nouvelle route que nous avons ajoutée va capturer chaque chemin qui n'existe pas et rediriger l'utilisateur vers la page 404.

Maintenant, passons à la suite et apprenons comment protéger nos routes dans la section suivante.

## Protection des routes

Il existe de nombreuses façons de protéger les routes dans React. Mais ici, je vais simplement vérifier si l'utilisateur est authentifié et le rediriger vers la page appropriée.

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  const isAuthenticated = false
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Accueil</Link></li>
          <li><Link to={`/about/${name}`}>À propos</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      {
      isAuthenticated ? 
      <>
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
      </> : <Redirect to="/" />
      }
      
    </Switch>
    </main>
</Router>
  );
}

```

Comme vous pouvez le voir ici, j'ai déclaré une variable pour simuler l'authentification. Ensuite, je vérifie si l'utilisateur est authentifié ou non. S'il l'est, je rends les pages protégées. Sinon, je le redirige vers la page d'accueil.

Nous avons couvert beaucoup de choses jusqu'à présent, mais une partie intéressante reste : les hooks du routeur.

Passons à la section finale et introduisons les Hooks.

## Hooks du routeur

Les hooks du routeur rendent les choses beaucoup plus faciles. Maintenant, vous pouvez accéder à l'historique, à l'emplacement ou aux paramètres de manière facile et élégante.

### useHistory

Le hook `useHistory` nous donne accès à l'instance de l'historique sans avoir à l'extraire des props.

```jsx
import { useHistory } from "react-router-dom";

const Contact = () => {
const history = useHistory();
return (
  <Fragment>
    <h1>Contact</h1>
    <button onClick={() => history.push('/') } >Aller à l'accueil</button>
  </Fragment>
  )
  };

```

### useParams

Ce hook nous aide à obtenir le paramètre passé dans l'URL sans utiliser l'objet props.

```jsx
import { BrowserRouter as Router, Route, Link, Switch, useParams } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Accueil</Link></li>
          <li><Link to={`/about/${name}`}>À propos</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
    </Switch>
    </main>
</Router>
  );
}

const About = () => {
  const { name } = useParams()
  return (
  // props.match.params.name
  <Fragment>
    { name !== 'John Doe' ? <Redirect to="/" /> : null }
    <h1>À propos de {name}</h1>
    <Route component={Contact} />
  </Fragment>
)
};

```

### useLocation

Ce hook retourne l'objet location qui représente l'URL actuelle.

```jsx
import { useLocation } from "react-router-dom";

const Contact = () => {
const { pathname } = useLocation();

return (
  <Fragment>
    <h1>Contact</h1>
    <p>URL actuelle : {pathname}</p>
  </Fragment>
  )
  };

```

## Réflexions finales

React Router est une bibliothèque incroyable qui nous aide à passer d'une application monopage à une application multipage avec une grande convivialité. (Gardez simplement à l'esprit – à la fin de la journée, c'est toujours une application monopage).

Et maintenant, avec les hooks du routeur, vous pouvez voir à quel point ils sont faciles et élégants. Ils sont définitivement quelque chose à considérer dans votre prochain projet.

Vous pouvez lire plus de mes articles sur [mon blog](https://www.ibrahima-ndaw.com/blog/).

## Prochaines étapes

[Documentation de React Router](https://reacttraining.com/react-router/web)

Photo par [Joshua Sortino](https://unsplash.com/@sortino?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/route?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)