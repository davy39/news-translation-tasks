---
title: Démystifier le rendu côté serveur dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T13:58:27.000Z'
originalURL: https://freecodecamp.org/news/demystifying-reacts-server-side-render-de335d408fe4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ecd_MVlJQoZ3bNn-xclFiA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Démystifier le rendu côté serveur dans React
seo_desc: 'By Alex Moldovan

  Let’s have a closer look at the feature that allows you to build universal applications
  with React.

  Server-Side Rendering — SSR from here on — is the ability of a front-end framework
  to render markup while running on a back-end syste...'
---

Par Alex Moldovan

Examinons de plus près la fonctionnalité qui permet de créer des **applications** **universelles** avec **React**.

Le rendu côté serveur — SSR par la suite — est la capacité d'un **framework front-end** à rendre du balisage tout en s'exécutant sur un **système back-end**.

Les applications capables de rendre à la fois sur le serveur et sur le client sont appelées **applications universelles**.

### Pourquoi s'en soucier ?

Pour comprendre pourquoi le SSR est nécessaire, nous devons comprendre l'évolution des applications web au cours des 10 dernières années.

Cela est étroitement lié à l'essor de l'[_Application à Page Unique_](https://medium.com/@NeotericEU/single-page-application-vs-multiple-page-application-2591588efe58) — SPA par la suite. Les SPA offrent de grands avantages en termes de vitesse et d'UX par rapport aux applications traditionnelles rendues côté serveur.

Mais il y a un piège. La requête initiale au serveur retourne généralement un fichier **HTML** **vide** avec un ensemble de liens CSS et JavaScript (JS). Ensuite, les fichiers externes doivent être récupérés afin de rendre le balisage pertinent.

Cela signifie que l'utilisateur devra attendre plus longtemps pour le **rendu initial**. Cela signifie également que les crawlers peuvent interpréter votre page comme vide.

L'idée est donc de rendre votre application sur le serveur initialement, puis de tirer parti des capacités des SPA sur le client.

**SSR + SPA = Application Universelle**

*Vous trouverez le terme _application isomorphe_ dans certains articles — c'est la même chose.

Maintenant, l'utilisateur n'a pas à attendre que votre JS se charge et obtient un **HTML** **complètement** **rendu** dès que la requête initiale retourne une réponse.

Imaginez l'énorme amélioration pour les utilisateurs naviguant sur des réseaux 3G lents. Plutôt que d'attendre plus de 20 secondes pour que le site se charge, vous obtenez du contenu sur leur écran presque instantanément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v0wyppYBPaeqoeKRplinvQ.png)

Et maintenant, toutes les requêtes faites à votre serveur retournent un HTML complètement rendu. Une excellente nouvelle pour votre département SEO !

Les [crawlers](https://en.wikipedia.org/wiki/Web_crawler) verront désormais votre site web comme n'importe quel autre site statique sur le web et **indexeront** tout le contenu que vous rendez sur le serveur.

Donc, pour résumer, les deux principaux avantages que nous obtenons du SSR sont :

* Des temps plus rapides pour le rendu initial de la page
* Des pages HTML entièrement indexables

## Comprendre le SSR — une étape à la fois

Prenons une approche itérative pour construire notre exemple complet de SSR. Nous commençons avec l'API de React pour le rendu côté serveur et nous ajouterons quelque chose à chaque étape.

Vous pouvez suivre [ce dépôt](https://github.com/alexnm/react-ssr) et les tags définis pour chaque étape.

### Installation de base

Commençons par le commencement. Pour utiliser le SSR, nous avons besoin d'un serveur ! Nous utiliserons une simple application _Express_ qui rendra notre application React.

```javascript
import express from "express";
import path from "path";

import React from "react";
import { renderToString } from "react-dom/server";
import Layout from "./components/Layout";

const app = express();

app.use( express.static( path.resolve( __dirname, "../dist" ) ) );

app.get( "/*", ( req, res ) => {
    const jsx = ( <Layout /> );
    const reactDom = renderToString( jsx );

    res.writeHead( 200, { "Content-Type": "text/html" } );
    res.end( htmlTemplate( reactDom ) );
} );

app.listen( 2048 );

function htmlTemplate( reactDom ) {
    return `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>React SSR</title>
        </head>
        
        <body>
            <div id="app">${ reactDom }</div>
            <script src="./app.bundle.js"></script>
        </body>
        </html>
    `;
}
```

Nous devons dire à Express de servir nos fichiers statiques depuis notre dossier de sortie — ligne 10.

Nous créons une route qui gère toutes les requêtes entrantes non statiques. Cette route répondra avec le HTML rendu.

Nous utilisons `renderToString` — lignes 13–14 — pour convertir notre JSX de départ en une `string` que nous insérons dans le modèle HTML.

En tant que note, nous utilisons les mêmes plugins Babel pour le code client et pour le code serveur. Donc _JSX_ et _ES Modules_ fonctionnent à l'intérieur de `server.js`.

La méthode correspondante sur le client est maintenant `ReactDOM.hydrate`. Cette fonction utilisera l'application React rendue côté serveur et attachera les gestionnaires d'événements.

```javascript
import ReactDOM from "react-dom";
import Layout from "./components/Layout";

const app = document.getElementById( "app" );
ReactDOM.hydrate( <Layout />, app );
```

Pour voir l'exemple complet, consultez le tag `basic` dans le [dépôt](https://github.com/alexnm/react-ssr/tree/basic).

C'est tout ! Vous venez de créer votre première application React **rendue côté serveur** !

#### React Router

Nous devons être honnêtes ici, l'application ne fait pas grand-chose. Ajoutons donc quelques routes et voyons comment nous gérons la partie serveur.

```javascript
import { Link, Switch, Route } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";

export default class Layout extends React.Component {
    /* ... */

    render() {
        return (
            <div>
                <h1>{ this.state.title }</h1>
                <div>
                    <Link to="/">Accueil</Link>
                    <Link to="/about">À propos</Link>
                    <Link to="/contact">Contact</Link>
                </div>
                <Switch>
                    <Route path="/" exact component={ Home } />
                    <Route path="/about" exact component={ About } />
                    <Route path="/contact" exact component={ Contact } />
                </Switch>
            </div>
        );
    }
}
```

Le composant `Layout` rend maintenant plusieurs routes sur le client.

Nous devons imiter la configuration du routeur sur le serveur. Ci-dessous, vous pouvez voir les principaux changements à apporter.

```javascript
/* ... */
import { StaticRouter } from "react-router-dom";
/* ... */

app.get( "/*", ( req, res ) => {
    const context = { };
    const jsx = (
        <StaticRouter context={ context } location={ req.url }>
            <Layout />
        </StaticRouter>
    );
    const reactDom = renderToString( jsx );

    res.writeHead( 200, { "Content-Type": "text/html" } );
    res.end( htmlTemplate( reactDom ) );
} );

/* ... */
```

Sur le serveur, nous devons envelopper notre application React dans le composant `StaticRouter` et fournir la `location`.

En tant que note, le `context` est utilisé pour suivre les redirections potentielles lors du rendu du DOM React. Cela doit être géré avec une [réponse 3XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#Redirection_messages) du serveur.

L'exemple complet peut être vu sur le tag `router` dans le [même dépôt](https://github.com/alexnm/react-ssr/releases/tag/router).

#### Redux

Maintenant que nous avons des capacités de routage, intégrons [Redux](https://redux.js.org/).

Dans le scénario simple, nous avons besoin de Redux pour gérer la gestion d'état sur le client. Mais que faire si nous devons rendre des parties du DOM en fonction de cet état ? Il est logique d'initialiser Redux sur le serveur.

Si votre application **dispatche** des **actions** sur le **serveur**, elle doit **capturer** l'état et l'envoyer avec le HTML. Sur le client, nous alimentons cet état initial dans Redux.

Examinons d'abord le serveur :

```javascript
/* ... */
import { Provider as ReduxProvider } from "react-redux";
/* ... */

app.get( "/*", ( req, res ) => {
    const context = { };
    const store = createStore( );

    store.dispatch( initializeSession( ) );

    const jsx = (
        <ReduxProvider store={ store }>
            <StaticRouter context={ context } location={ req.url }>
                <Layout />
            </StaticRouter>
        </ReduxProvider>
    );
    const reactDom = renderToString( jsx );

    const reduxState = store.getState( );

    res.writeHead( 200, { "Content-Type": "text/html" } );
    res.end( htmlTemplate( reactDom, reduxState ) );
} );

app.listen( 2048 );

function htmlTemplate( reactDom, reduxState ) {
    return `
        /* ... */
        
        <div id="app">${ reactDom }</div>
        <script>
            window.REDUX_DATA = ${ JSON.stringify( reduxState ) }
        </script>
        <script src="./app.bundle.js"></script>
        
        /* ... */
    `;
}
```

Cela semble laid, mais nous devons envoyer l'état JSON complet avec notre HTML.

Ensuite, nous regardons le client :

```javascript
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";
import { Provider as ReduxProvider } from "react-redux";

import Layout from "./components/Layout";
import createStore from "./store";

const store = createStore( window.REDUX_DATA );

const jsx = (
    <ReduxProvider store={ store }>
        <Router>
            <Layout />
        </Router>
    </ReduxProvider>
);

const app = document.getElementById( "app" );
ReactDOM.hydrate( jsx, app );
```

Remarquez que nous appelons `createStore` deux fois, d'abord sur le serveur, puis sur le client. Cependant, sur le client, nous initialisons l'état avec l'état enregistré sur le serveur. Ce processus est similaire à l'hydratation du DOM.

L'exemple complet peut être vu sur le tag `redux` dans le [même dépôt](https://github.com/alexnm/react-ssr/releases/tag/redux).

#### Récupération de données

La dernière pièce du puzzle est le chargement des données. C'est là que cela devient un peu plus délicat. Supposons que nous avons une API servant des données JSON.

Dans notre base de code, je récupère tous les événements de la saison 2018 de Formule 1 [à partir d'une API publique](https://ergast.com/mrd/). Supposons que nous voulons afficher tous les événements sur la page **Accueil**.

Nous pouvons appeler notre API uniquement depuis le client après que l'application React soit montée et que tout soit rendu. Mais cela aura un mauvais impact sur l'UX, montrant potentiellement un spinner ou un chargeur avant que l'utilisateur ne voie un contenu pertinent.

Nous avons déjà Redux, comme moyen de stocker des données sur le serveur et de les envoyer au client.

Et si nous faisons nos appels API sur le serveur, stockons les résultats dans Redux, puis rendons le HTML complet avec les données pertinentes pour le client ?

Mais comment pouvons-nous savoir quels appels doivent être faits ?

Tout d'abord, nous avons besoin d'une autre façon de déclarer les routes. Nous passons donc au fichier de configuration des routes.

```javascript
export default [
    {
        path: "/",
        component: Home,
        exact: true,
    },
    {
        path: "/about",
        component: About,
        exact: true,
    },
    {
        path: "/contact",
        component: Contact,
        exact: true,
    },
    {
        path: "/secret",
        component: Secret,
        exact: true,
    },
];
```

Et nous déclarons statiquement les exigences de données sur chaque composant.

```javascript
/* ... */
import { fetchData } from "../store";

class Home extends React.Component {
    /* ... */

    render( ) {
        const { circuits } = this.props;

        return (
            /* ... */
        );
    }
}
Home.serverFetch = fetchData; // déclaration statique des exigences de données

/* ... */
```

Gardez à l'esprit que `serverFetch` est inventé, vous pouvez utiliser ce qui vous semble mieux.

En tant que note ici, `fetchData` est une [action Redux thunk](https://github.com/gaearon/redux-thunk), retournant une promesse lorsqu'elle est dispatchée.

Sur le serveur, nous pouvons utiliser une fonction spéciale de `react-router`, appelée `matchRoute`.

```javascript
/* ... */
import { StaticRouter, matchPath } from "react-router-dom";
import routes from "./routes";

/* ... */

app.get( "/*", ( req, res ) => {
    /* ... */

    const dataRequirements =
        routes
            .filter( route => matchPath( req.url, route ) ) // filtrer les chemins correspondants
            .map( route => route.component ) // mapper vers les composants
            .filter( comp => comp.serverFetch ) // vérifier si les composants ont des exigences de données
            .map( comp => store.dispatch( comp.serverFetch( ) ) ); // dispatcher les exigences de données

    Promise.all( dataRequirements ).then( ( ) => {
        const jsx = (
            <ReduxProvider store={ store }>
                <StaticRouter context={ context } location={ req.url }>
                    <Layout />
                </StaticRouter>
            </ReduxProvider>
        );
        const reactDom = renderToString( jsx );

        const reduxState = store.getState( );

        res.writeHead( 200, { "Content-Type": "text/html" } );
        res.end( htmlTemplate( reactDom, reduxState ) );
    } );
} );

/* ... */
```

Avec cela, nous obtenons une liste de composants qui seront montés lorsque React sera rendu en chaîne sur l'URL actuelle.

Nous recueillons les _exigences de données_ et attendons que tous les appels API retournent. Enfin, nous reprenons le rendu du serveur, mais avec les données déjà disponibles dans Redux.

L'exemple complet peut être vu sur le tag `fetch-data` dans le [même dépôt](https://github.com/alexnm/react-ssr/tree/fetch-data).

Vous remarquez probablement que cela entraîne une pénalité de performance, car nous retardons le rendu jusqu'à ce que les données soient récupérées.

C'est là que vous commencez à comparer les métriques et faites de votre mieux pour comprendre quels appels sont essentiels et lesquels ne le sont pas. Par exemple, la récupération des produits pour une application de commerce électronique peut être cruciale, mais les prix et les filtres de la barre latérale peuvent être chargés de manière paresseuse.

#### Helmet

En bonus, examinons le SEO. En travaillant avec React, vous pouvez vouloir définir différentes valeurs dans votre balise `<head>`. Par exemple, vous pouvez vouloir définir le _titre_, les balises _meta_, les _mots-clés_, etc.

Gardez à l'esprit que la balise `<head>` ne fait normalement pas partie de votre application React !

[react-helmet](https://github.com/nfl/react-helmet) vous couvre dans ce scénario. Et il a un excellent support pour le SSR.

```javascript
import React from "react";
import Helmet from "react-helmet";

const Contact = () => (
    <div>
        <h2>Ceci est la page de contact</h2>
        <Helmet>
            <title>Page de Contact</title>
            <meta name="description" content="Ceci est une preuve de concept pour React SSR" />
        </Helmet>
    </div>
);

export default Contact;
```

Vous ajoutez simplement vos données `head` n'importe où dans votre arbre de composants. Cela vous donne le support pour changer les valeurs en dehors de l'application React montée sur le client.

Et maintenant, nous ajoutons le support pour le SSR :

```javascript
/* ... */
import Helmet from "react-helmet";
/* ... */

app.get( "/*", ( req, res ) => {
    /* ... */
        const jsx = (
            <ReduxProvider store={ store }>
                <StaticRouter context={ context } location={ req.url }>
                    <Layout />
                </StaticRouter>
            </ReduxProvider>
        );
        const reactDom = renderToString( jsx );
        const reduxState = store.getState( );
        const helmetData = Helmet.renderStatic( );

        res.writeHead( 200, { "Content-Type": "text/html" } );
        res.end( htmlTemplate( reactDom, reduxState, helmetData ) );
    } );
} );

app.listen( 2048 );

function htmlTemplate( reactDom, reduxState, helmetData ) {
    return `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            ${ helmetData.title.toString( ) }
            ${ helmetData.meta.toString( ) }
            <title>React SSR</title>
        </head>
        
        /* ... */
    `;
}
```

Et maintenant, nous avons un exemple React SSR entièrement fonctionnel !

Nous avons commencé par un simple rendu de HTML dans le contexte d'une application _Express_. Nous avons progressivement ajouté le routage, la gestion d'état et la récupération de données. Enfin, nous avons géré les changements en dehors du cadre de l'application React.

Le code final est sur `master` dans le [même dépôt](https://github.com/alexnm/react-ssr) mentionné précédemment.

#### Conclusion

Comme vous l'avez vu, le SSR n'est pas une grosse affaire, mais cela peut devenir complexe. Et c'est beaucoup plus facile à comprendre si vous construisez vos besoins étape par étape.

Est-il utile d'ajouter le SSR à votre application ? Comme toujours, cela dépend. C'est une nécessité si votre site web est public et accessible à des centaines de milliers d'utilisateurs. Mais si vous construisez une application de type outil/tableau de bord, cela peut ne pas valoir l'effort.

Cependant, tirer parti de la puissance des applications universelles est un pas en avant pour la communauté front-end.

Utilisez-vous une approche similaire pour le SSR ? Ou pensez-vous que j'ai manqué quelque chose ? Laissez-moi un message ci-dessous ou sur [Twitter](https://twitter.com/alexnmoldovan).

Si vous avez trouvé cet article utile, aidez-moi à le partager avec la communauté !