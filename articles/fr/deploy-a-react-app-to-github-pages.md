---
title: Comment déployer une application React avec routage sur GitHub Pages
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-02-22T22:53:34.000Z'
originalURL: https://freecodecamp.org/news/deploy-a-react-app-to-github-pages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/602aaa1e0a2838549dcc5c67.jpg
tags:
- name: github pages
  slug: github-pages
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment déployer une application React avec routage sur GitHub Pages
seo_desc: "When we build projects, we want to showcase them online. Instead of buying\
  \ a domain and taking the time to configure it, it's easier just to host it using\
  \ GitHub Pages. \nA project that just uses JavaScript, HTML and CSS is simple to\
  \ host on GitHub Pa..."
---

Lorsque nous construisons des projets, nous voulons les présenter en ligne. Au lieu d'acheter un domaine et de prendre le temps de le configurer, il est plus facile de l'héberger simplement en utilisant [GitHub Pages](https://pages.github.com/).

Un projet qui utilise uniquement JavaScript, HTML et CSS est simple à héberger sur GitHub Pages. Les projets construits avec React, Vue ou Angular nécessitent cependant certaines configurations. Cela permet à toute personne visitant votre application en ligne d'avoir la même expérience que vous lorsque vous construisez l'application localement.

Dans cet article, je vais vous montrer comment créer une application React simple qui utilise le routage, puis nous apprendrons comment la télécharger sur GitHub Pages. Nous accorderons une attention particulière à la partie routage, car il est important de la comprendre et de la mettre en œuvre.

> ⚠️ Cet article suppose que vous avez quelques connaissances de React et Git.

### Prérequis

Vous devez avoir Node, yarn et npm installés sur votre machine. Pour vérifier s'ils sont installés, ouvrez une fenêtre de terminal et tapez ce qui suit :

```bash
npm -v
yarn -v
node -v
```

Si ces commandes affichent un numéro de version dans le terminal, vous êtes prêt à commencer. Sinon, vous devez installer ce qui manque.

* [Node](https://nodejs.org/en/download/) (contient npm)
* [Yarn](https://classic.yarnpkg.com/en/docs/install/#windows-stable)

Nous devrons également créer un dépôt sur GitHub. Rendez-vous sur votre compte et créez un nouveau dépôt. Choisissez le nom que vous jugez approprié pour ce projet, mais je vais utiliser **starter-project** pour le reste de cet article.

Pour créer notre projet, nous allons utiliser **create-react-app**. C'est un package qui vous permet de créer une application monopage avec facilité. Pour créer un projet, vous devez taper ce qui suit dans le terminal :

```bash
npx create-react-app starter-project
```

Une fois l'opération terminée, vous aurez un projet React de base, prêt à l'emploi. Pour voir s'il fonctionne correctement, allez dans le répertoire du projet (dans notre exemple, ce serait starter-project) et exécutez la commande :

```bash
yarn start
```

Si tout se passe bien, vous verrez un message dans le terminal indiquant que votre application est en cours d'exécution sur un serveur local à cette adresse : **http://localhost:3000**

Si vous vous y rendez dans votre navigateur, vous verrez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/IB8uRE3cjN.gif)

## Comment déployer votre projet sur GitHub

Vous avez peut-être remarqué que nous n'avons créé aucun dépôt sur GitHub. Donc, avant de continuer, nous devons y télécharger notre projet. Rendez-vous sur votre compte GitHub et créez un dépôt avec le même nom que le projet React.

> ☝️ Assurez-vous de marquer votre dépôt comme public. Si vous le marquez comme privé, vous ne pourrez pas utiliser GitHub Pages.

Nous allons ajouter ce dépôt comme un remote à notre projet. Pour ce faire, dans le terminal, tapez :

```bash
git remote add <nom-du-remote> <url-du-dépôt>
```

Donc, dans notre cas, la commande ressemble à ceci :

```bash
git remote add origin https://github.com/TomerPacific/starter-project
```

> Il est important d'appeler le remote **_origin_** car il sera utilisé dans notre processus de déploiement.

Après avoir exécuté la commande ci-dessus, nous ne pouvons pas encore pousser notre code. D'abord, nous devons configurer une branche upstream et définir le remote comme origin.

```bash
 git push --set-upstream origin master
```

Maintenant, nous pouvons pousser tous les fichiers de notre projet vers notre dépôt.

Pour pouvoir télécharger notre application construite sur GitHub Pages, nous devons d'abord installer le [package gh-pages](https://www.npmjs.com/package/gh-pages).

```bash
yarn add gh-pages
```

Ce package nous aidera à déployer notre code sur la branche gh-pages qui sera utilisée pour héberger notre application sur GitHub Pages.

Pour nous permettre d'utiliser correctement le package gh-pages, nous devons ajouter deux clés à notre valeur de scripts dans le fichier package.json :

```package.json
"scripts": {
    "start": "react-scripts start",
    "predeploy": "npm run build", <----------- #1
    "deploy": "gh-pages -d build", <---------- #2
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

Ensuite, nous devons modifier notre fichier package.json en ajoutant le champ **homepage**. Ce champ est utilisé par React pour déterminer l'URL racine dans le fichier HTML construit. Nous y mettrons l'URL de notre dépôt GitHub.

```package.json
{
  "name": "starter-project",
  "homepage": "https://tomerpacific.github.io/starter-project/", <----
  "version": "0.1.0",
  /....
}
```

Pour déployer notre application, tapez ce qui suit dans le terminal :

```bash
npm run deploy
```

L'exécution de la commande ci-dessus prend en charge la construction de votre application et la pousse vers une branche appelée gh-pages, que GitHub utilise pour lier avec GitHub Pages.

> 🚧 Si vous n'avez pas nommé votre remote **_origin_**, vous obtiendrez une erreur lors de cette phase indiquant que : **Failed to get remote.origin.url (task must either be run in a git repository with a configured origin remote or must be configured with the "repo" option)**.

Vous saurez que le processus a réussi si, à la fin, vous voyez le mot **Published**. Nous pouvons maintenant nous rendre dans notre dépôt GitHub sous Paramètres et faire défiler jusqu'à la section GitHub Pages.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/chrome_egdTtIso1X.png)

Si vous voyez un message similaire à celui ci-dessus, cela signifie que votre application est maintenant hébergée avec succès sur GitHub Pages.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-308.png)
_Photo par [Unsplash](https://unsplash.com/@noahglynn?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Noah Glynn</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Routage dans React

Jusqu'à présent, tout va bien :

1. Nous avons une application React de base hébergée sur GitHub Pages
2. Nous avons également un processus rationalisé pour la déployer lorsque nous voulons apporter des modifications

Mais puisque le but de cet article est de montrer une application plus complexe que celle que nous avons initialement créée, nous allons discuter du routage.

Un composant qui manque à notre application est la navigation. Notre application ne sera pas une seule page, elle aura probablement plusieurs pages. Alors, comment les utilisateurs pourront-ils naviguer entre elles ?

Le routage est la pratique de sélectionner un chemin pour le trafic dans un réseau. Ou en termes plus basiques, ce qui se passe lorsque vous cliquez sur un lien à l'intérieur d'une page web et où vous êtes redirigé.

React est une bibliothèque, et elle ne contient pas tout ce dont vous avez besoin pour votre application dès la sortie de la boîte (dans notre cas, le routage). Par conséquent, nous devons installer [react router](https://reactrouter.com/web/guides/quick-start).

React router a différents composants pour les applications web et pour les applications natives. Puisque nous construisons une application web, nous utiliserons **react-router-dom**.

```bash
yarn add react-router-dom
```

Pour utiliser le routage dans notre application, créons un élément de navigation qui sera visible en haut de l'application. Nous allons ajouter cela à l'intérieur de notre fichier App.js et remplacer le balisage HTML actuel qui s'y trouve.

```html
 <div>
     <nav>
         <ul id="navigation">
             <li>
                 <Link to="/">Accueil</Link>
             </li>
             <li>
                 <Link to="/about">À propos</Link>
             </li>
             <li>
                 <Link to="/contact">Contact</Link>
             </li>
         </ul>
     </nav>
</div>
```

Habituellement, dans un projet non React, nous mettrions un chemin relatif vers nos pages HTML pour chaque section. De cette façon, le navigateur sait où charger les données. 

Mais dans notre projet, nous n'aurons pas de pages HTML différentes pour chaque section. Nous chargerons simplement un composant différent. Le balisage qui se trouvait à l'intérieur de App.js se trouvera maintenant à l'intérieur d'un composant appelé Home.

```javascript
import './App.css';
import React from 'react';
import logo from './logo.svg';

class Home extends React.Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Modifier <code>src/App.js</code> et enregistrer pour recharger.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Apprendre React
                </a>
                </header>
            </div>
            
        );
    }

}

export default Home;
```

Comme nous avons créé trois sections dans notre navigation et pris en charge la section d'accueil, donnons un autre exemple avec la section **À propos**.

Nous allons créer un nouveau fichier appelé **About.jsx** qui contiendra notre modèle et notre code pour la section à propos.

```javascript
import React from 'react';

const divStyle = {
    color:'white'
};

class About extends React.Component {
    
    render() {
        return (
            <div style={divStyle}>
                <h2>Page À propos</h2>
                <main>
                    <p>Cette section contient des informations sur...</p>
                </main>
            </div>
        )
    }
}



export default About;
```

Vous vous demandez peut-être comment l'application saura rediriger l'utilisateur une fois qu'il a cliqué sur le lien à propos ? Pour cela, nous utiliserons un composant appelé **Route**. 

La Route est l'un des composants les plus importants dans react-router car elle vous permet de rendre différents composants en fonction du chemin de l'URL. Pour notre projet, nous utiliserons le code ci-dessous à l'intérieur de App.js juste en dessous du balisage de navigation.

```html
<Switch>
    <Route exact path="/">
    <Home />
    </Route>
    <Route path="/about">
    <About />
    </Route>
</Switch>
```

Vous pouvez voir que nous avons créé deux routes pour l'accueil et à propos. Le composant Switch nous permet de regrouper les composants de route ensemble et il ne correspondra qu'à l'un d'eux.

Notre fichier App.js combiné ressemble à ceci :

```javascript
import './App.css';
import React from 'react';
import { Route, Switch, Link } from "react-router-dom";
import About from './About';
import Home from './Home';

class App extends React.Component {
  render() {
      return (
        <div className="App">
          <div>
            <nav>
              <ul id="navigation">
                <li>
                  <Link to="/">Accueil</Link>
                </li>
                <li>
                <Link to="/about">À propos</Link>
                </li>
                <li>
                <Link to="/contact">Contact</Link>
                </li>
              </ul>
            </nav>
          </div>
            <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/about">
              <About />
            </Route>
          </Switch>
          </div>
            );
  }
}

export default App;

```

Une dernière chose que nous devons faire est d'envelopper notre projet entier dans un composant Router. Nous devons faire cela car cela nous permet d'utiliser le routage dans notre application. Nous utiliserons le composant BrowserRouter car il utilise l'API d'historique HTML5.

```html
ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

Si nous exécutons les choses localement, tout semble fonctionner. Déployons notre projet augmenté sur GitHub Pages et voyons quel est le résultat.

## Comment gérer le routage en utilisant HashRouter

À première vue, tout semble fonctionner correctement. Mais lorsque vous essayez d'actualiser la page ou de naviguer via le navigateur lui-même, vous continuerez à obtenir des erreurs 404.

Pourquoi cela se produit-il ? Parce que GitHub Pages ne supporte pas l'historique du navigateur comme le fait votre navigateur. Dans notre cas, la route **https://tomerpacific.github.io/starter-project/about** n'aide pas GitHub Pages à comprendre où diriger l'utilisateur (puisqu'il s'agit d'une route frontend).

Pour surmonter ce problème, nous devons utiliser un Hash Router au lieu d'un Browser Router dans notre application. Ce type de routeur utilise la partie hash de l'URL pour garder l'UI synchronisée avec l'URL.

```html
ReactDOM.render(
  <React.StrictMode>
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

Vous pouvez en lire plus à ce sujet [ici](https://create-react-app.dev/docs/deployment/#github-pages-https-pagesgithubcom).

Déployez votre application à nouveau et vous serez satisfait du résultat. Plus d'erreurs 404.

Cet article a été inspiré par le travail sur un projet à moi. Vous pouvez le voir ci-dessous :

%[https://tomerpacific.github.io/julOnSaleReact/]

Et vous pouvez voir le code source ici :

%[https://github.com/TomerPacific/julOnSaleReact]