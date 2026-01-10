---
title: Tutoriel React Router – Comment rendre, rediriger, basculer, lier et plus,
  avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-26T17:55:23.000Z'
originalURL: https://freecodecamp.org/news/react-router-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad1740569d1a4ca27f2.jpg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
- name: ' Single Page Applications '
  slug: single-page-applications
seo_title: Tutoriel React Router – Comment rendre, rediriger, basculer, lier et plus,
  avec des exemples de code
seo_desc: "By Vijit Ail\nIf you have just started with React, you are probably still\
  \ wrapping your head around the whole Single Page Application concept. \nTraditionally\
  \ routing works like this: let's say you type in /contact in the URL. The browser\
  \ will make a G..."
---

Par Vijit Ail

Si vous venez de commencer avec React, vous êtes probablement encore en train de comprendre le concept entier des Applications à Page Unique (Single Page Application).

Traditionnellement, le routage fonctionne comme ceci : supposons que vous tapiez `/contact` dans l'URL. Le navigateur fera une requête GET au serveur, et le serveur retournera une page HTML en réponse.

Mais, avec le nouveau paradigme des Applications à Page Unique, toutes les requêtes d'URL sont gérées à l'aide du code côté client.

En appliquant cela dans le contexte de React, chaque page sera un composant React. React-Router fait correspondre l'URL et charge le composant pour cette page particulière.

Tout se passe si rapidement et de manière si transparente que l'utilisateur obtient une expérience similaire à une application native sur le navigateur. Il n'y a pas de page blanche clignotante entre les transitions de route.

Dans cet article, vous apprendrez à utiliser React-Router et ses composants pour créer une Application à Page Unique. Alors, ouvrez votre éditeur de texte préféré, et commençons.

## Installation du projet

Créez un nouveau projet React en exécutant la commande suivante.

```sh
yarn create react-app react-router-demo
```

J'utiliserai yarn pour installer les dépendances, mais vous pouvez utiliser npm également.

Ensuite, installons `react-router-dom`.

```
yarn add react-router-dom
```

Pour styliser les composants, je vais utiliser le framework CSS Bulma. Alors, ajoutons cela également.

```
yarn add bulma
```

Ensuite, importez `bulma.min.css` dans le fichier `index.js` et nettoyez tout le code boilerplate du fichier `App.js`.

```js
import "bulma/css/bulma.min.css";
```

Maintenant que vous avez configuré le projet, commençons par créer quelques composants de page.

## Création des composants de page

Créez un répertoire pages à l'intérieur du dossier src où nous placerons tous les composants de page.

Pour cette démonstration, créez trois pages - Accueil, À propos et Profil.

Collez le code suivant dans les composants Accueil et À propos.

```jsx
// pages/Home.js

import React from "react";

const Home = () => (
  <div>
    <h1 className="title is-1">Ceci est la page d'accueil</h1>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras gravida,
      risus at dapibus aliquet, elit quam scelerisque tortor, nec accumsan eros
      nulla interdum justo. Pellentesque dignissim, sapien et congue rutrum,
      lorem tortor dapibus turpis, sit amet vestibulum eros mi et odio.
    </p>
  </div>
);

export default Home;

```

```jsx
// pages/About.js

import React from "react";

const About = () => (
  <div>
    <h1 className="title is-1">Ceci est la page À propos</h1>
    <p>
      Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
      inceptos himenaeos. Vestibulum ante ipsum primis in faucibus orci luctus
      et ultrices posuere cubilia curae; Duis consequat nulla ac ex consequat,
      in efficitur arcu congue. Nam fermentum commodo egestas.
    </p>
  </div>
);

export default About;

```

Nous créerons la page Profil plus tard dans l'article.

## Création du composant Navbar

Commençons par créer la barre de navigation pour notre application. Ce composant utilisera le composant `<NavLink />` de `react-router-dom`.

Créez un répertoire appelé "components" à l'intérieur du dossier src.

```jsx
// components/Navbar.js

import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return ( 
  	<nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
      	{/* ... */}
      </div>
    </nav>
  );
 };
 
 export default Navbar;
```

La variable d'état `isOpen` sera utilisée pour déclencher le menu sur les appareils mobiles ou tablettes.

Alors, ajoutons le menu hamburger.

```jsx
const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return ( 
  	<nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
      <div className="navbar-brand">
          <a
            role="button"
            className={`navbar-burger burger ${isOpen && "is-active"}`}
            aria-label="menu"
            aria-expanded="false"
            onClick={() => setOpen(!isOpen)}
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
      	{/* ... */}
      </div>
    </nav>
  );
 };
```

Pour ajouter le lien dans le menu, utilisez le composant `<NavLink />` de `react-router-dom`.

Le composant `NavLink` fournit un moyen déclaratif de naviguer dans l'application. Il est similaire au composant `Link`, sauf qu'il peut appliquer un style actif au lien s'il est actif.

Pour spécifier quelle route naviguer, utilisez la prop `to` et passez le nom du chemin. La prop `activeClassName` ajoutera une classe active au lien s'il est actuellement actif.

```jsx
<NavLink
    className="navbar-item"
    activeClassName="is-active"
    to="/"
    exact
>
	Accueil
</NavLink>
```

Dans le navigateur, le composant `NavLink` est rendu comme une balise `<a>` avec une valeur d'attribut `href` qui a été passée dans la prop `to`.

De plus, ici, vous devez spécifier la prop `exact` pour qu'elle corresponde exactement à l'URL.

Ajoutez tous les liens et terminez le composant `Navbar`.

```jsx
import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return (
    <nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
        <div className="navbar-brand">
          <a
            role="button"
            className={`navbar-burger burger ${isOpen && "is-active"}`}
            aria-label="menu"
            aria-expanded="false"
            onClick={() => setOpen(!isOpen)}
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div className={`navbar-menu ${isOpen && "is-active"}`}>
          <div className="navbar-start">
            <NavLink className="navbar-item" activeClassName="is-active" to="/">
              Accueil
            </NavLink>

            <NavLink
              className="navbar-item"
              activeClassName="is-active"
              to="/apropos"
            >
              À propos
            </NavLink>

            <NavLink
              className="navbar-item"
              activeClassName="is-active"
              to="/profil"
            >
              Profil
            </NavLink>
          </div>

          <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons">
                <a className="button is-white">Se connecter</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

```

Si vous remarquez ici, j'ai ajouté un bouton de connexion. Nous reviendrons au composant `Navbar` plus tard lorsque nous discuterons des routes protégées.

## Rendu des pages

Maintenant que le composant `Navbar` est configuré, ajoutons-le à la page et commençons par le rendu des pages.

Puisque la barre de navigation est un composant commun à toutes les pages, au lieu d'appeler le composant dans chaque composant de page, il sera préférable de rendre le `Navbar` dans une disposition commune.

```jsx
// App.js

function App() {
  return (
    <>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        {/* Rendre la page ici */}
      </div>
    </>
  );
}
```

Maintenant, ajoutez les composants de page à l'intérieur du conteneur.

```jsx
// App.js

function App() {
  return (
    <>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        <Home />
      	<About />
      </div>
    </>
  );
}
```

Si vous vérifiez les résultats maintenant, vous remarquerez que les composants de la page d'accueil et de la page À propos sont tous deux rendus sur la page. C'est parce que nous n'avons pas encore ajouté de logique de routage.

Vous devez importer le composant `BrowserRouter` de React Router pour ajouter la capacité de router les composants. Tout ce que vous avez à faire est d'envelopper tous les composants de page à l'intérieur du composant `BrowserRouter`. Cela permettra à tous les composants de page d'avoir la logique de routage. Parfait !

Mais encore une fois, rien ne va changer avec les résultats – vous allez toujours voir les deux pages rendues. Vous devez rendre le composant de page uniquement si l'URL correspond à un chemin particulier. C'est là que le composant `Route` de React Router entre en jeu.

Le composant `Router` a une prop `path` qui accepte le chemin de la page, et le composant de page doit être enveloppé avec le `Router`, comme montré ci-dessous.

```jsx
<Route path="/apropos">
  <About />
</Route>
```

Alors, faisons de même pour le composant `Home`.

```jsx
<Route exact path="/">
  <Home />
</Route>
```

La prop `exact` ci-dessus indique au composant `Router` de faire correspondre le chemin exactement. Si vous n'ajoutez pas la prop `exact` sur le chemin `/`, il correspondra à toutes les routes commençant par un `/` incluant `/apropos`.

Si vous allez vérifier les résultats maintenant, vous verrez toujours les deux composants rendus. Mais, si vous allez à `/apropos`, vous remarquerez que seul le composant `About` est rendu. Vous voyez ce comportement parce que le routeur continue à faire correspondre l'URL avec les routes même après avoir déjà fait correspondre une route.

Nous devons dire au routeur d'arrêter de faire correspondre davantage une fois qu'il a fait correspondre une route. Cela se fait en utilisant le composant `Switch` de React Router.

```jsx
function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/apropos">
            <About />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  );
}
```

Et voilà ! Vous avez configuré avec succès le routage dans votre application React.

## Routes protégées et redirection

Lorsque vous travaillez sur des applications réelles, vous aurez certaines routes derrière un système d'authentification. Vous allez avoir des routes ou des pages qui ne peuvent être accessibles que par un utilisateur connecté. Dans cette section, vous apprendrez comment procéder à la mise en œuvre de telles routes.

**_Veuillez noter_** _que je ne vais pas créer de formulaire de connexion ou avoir un service backend pour authentifier l'utilisateur. Dans une application réelle, vous ne mettriez pas en œuvre l'authentification de la manière démontrée ici._

Créons le composant de page Profil qui ne devrait être accessible que par l'utilisateur authentifié.

```jsx
// pages/Profile.js

import { useParams } from "react-router-dom";

const Profile = () => {
  const { name } = useParams();
  return (
    <div>
      <h1 className="title is-1">Ceci est la page Profil</h1>
      <article className="message is-dark" style={{ marginTop: 40 }}>
        <div className="message-header">
          <p>{name}</p>
        </div>
        <div className="message-body">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.{" "}
          <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta
          nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida
          purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac{" "}
          <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et
          sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi
          magna a neque. Donec dui urna, vehicula et sem eget, facilisis sodales
          sem.
        </div>
      </article>
    </div>
  );
};

```

Nous récupérerons le nom de l'utilisateur à partir de l'URL en utilisant les paramètres de route.

Ajoutez la route Profil dans le routeur.

```jsx
<Route path="/profil/:name">
  <Profile />
</Route>
```

Actuellement, la page de profil peut être accessible directement. Donc, pour en faire une route authentifiée, créez un composant d'ordre supérieur (HOC) pour envelopper la logique d'authentification.

```jsx
const withAuth = (Component) => {
  const AuthRoute = () => {
    const isAuth = !!localStorage.getItem("token");
    // ...
  };

  return AuthRoute;
};
```

Pour déterminer si un utilisateur est authentifié ou non, récupérez le jeton d'authentification qui est stocké dans le navigateur lorsque l'utilisateur se connecte. Si l'utilisateur n'est pas authentifié, redirigez l'utilisateur vers la page d'accueil. Le composant `Redirect` de React Router peut être utilisé pour rediriger l'utilisateur vers un autre chemin.

```jsx
const withAuth = (Component) => {
  const AuthRoute = () => {
    const isAuth = !!localStorage.getItem("token");
    if (isAuth) {
      return <Component />;
    } else {
      return <Redirect to="/" />;
    }
  };

  return AuthRoute;
};
```

Vous pouvez également passer d'autres informations utilisateur comme le nom et l'ID utilisateur en utilisant les props au composant enveloppé.

Ensuite, utilisez le HOC `withAuth` dans le composant Profile.

```jsx
import withAuth from "../components/withAuth";

const Profile = () => {
 // ...
}

export default withAuth(Profile);
```

Maintenant, si vous essayez de visiter `/profil/JohnDoe`, vous serez redirigé vers la page d'accueil. C'est parce que le jeton d'authentification n'est pas encore défini dans votre stockage de navigateur.

D'accord, alors, retournons au composant `Navbar` et ajoutons les fonctionnalités de connexion et de déconnexion. Lorsque l'utilisateur est authentifié, affichez le bouton Déconnexion et lorsque l'utilisateur n'est pas connecté, affichez le bouton Connexion.

```jsx
// components/Navbar.js

const Navbar = () => {
	// ...
    return (
    	<nav
          className="navbar is-primary"
          role="navigation"
          aria-label="main navigation"
        >
        <div className="container">
        	{/* ... */}
            <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons">
                {!isAuth ? (
                  <button className="button is-white" onClick={loginUser}>
                    Se connecter
                  </button>
                ) : (
                  <button className="button is-black" onClick={logoutUser}>
                    Se déconnecter
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
        </nav>
    );
}


```

Lorsque l'utilisateur clique sur le bouton de connexion, définissez un jeton fictif dans le stockage local, et redirigez l'utilisateur vers la page de profil.

Mais nous ne pouvons pas utiliser le composant Redirect dans ce cas – nous devons rediriger l'utilisateur par programmation. Les jetons sensibles utilisés pour l'authentification sont généralement stockés dans des cookies pour des raisons de sécurité.

React Router a un HOC `withRouter` qui injecte l'objet `history` dans les props du composant pour exploiter l'API History. Il passe également les props `match` et `location` mises à jour au composant enveloppé.

```jsx
// components/Navbar.js

import { NavLink, withRouter } from "react-router-dom";

const Navbar = ({ history }) => { 
  const isAuth = !!localStorage.getItem("token");

  const loginUser = () => {
    localStorage.setItem("token", "some-login-token");
    history.push("/profil/Vijit");
  };

  const logoutUser = () => {
    localStorage.removeItem("token");
    history.push("/");
  };
  
  return ( 
   {/* ... */}
  );
};

export default withRouter(Navbar);
```

Et _voilà_ ! C'est tout. Vous avez également conquis le domaine des routes authentifiées.

Consultez la démonstration en direct [ici](https://react-router-demo.vijitail.dev/) et le code complet dans ce [dépôt](https://github.com/vijitail/react-router-demo) pour référence.

## Conclusion

J'espère qu'à présent vous avez une idée claire de la manière dont le routage côté client fonctionne en général et comment implémenter le routage dans React en utilisant la bibliothèque React Router.

Dans ce guide, vous avez appris les composants vitaux de React Router comme `Route`, `withRouter`, `Link`, et bien d'autres, ainsi que quelques concepts avancés comme les routes authentifiées, nécessaires pour construire une application.

Consultez la documentation de React Router [docs](https://reacttraining.com/react-router/web/guides/quick-start) pour obtenir un aperçu plus détaillé de chacun des composants.