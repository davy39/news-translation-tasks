---
title: 'Gatsby.js : Comment configurer et utiliser le générateur de site statique
  React'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T20:36:15.000Z'
originalURL: https://freecodecamp.org/news/setting-up-and-getting-used-to-gatsby-1fc27985ae8a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qQJDr-iY4irNKb1FHDseUw.jpeg
tags:
- name: Gatsby
  slug: gatsby
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Gatsby.js : Comment configurer et utiliser le générateur de site statique
  React'
seo_desc: 'By Aman Mittal

  Gatsby is a static site generator for React that released its first major version
  last month. It’s a tool that not only scaffolds projects (or websites) for you but
  claims that those sites are fast in performance. If you decide to use ...'
---

Par Aman Mittal

[Gatsby](https://www.gatsbyjs.org/) est un générateur de site statique pour React qui a publié sa première version majeure le mois dernier. C'est un outil qui non seulement échafaudage des projets (ou sites web) pour vous, mais affirme également que ces sites sont performants. Si vous décidez d'utiliser Gatsby, vous profiterez de la puissance des dernières technologies web telles que React.js, Webpack, et bien d'autres.

Il y a beaucoup de paradigmes modernes dont Gatsby s'occupe pour ses développeurs en arrière-plan pour commencer à construire et lancer leur projet. Une autre chose cool à propos de Gatsby que j'aime est son écosystème de plugins de données en constante croissance. Il permet à un développeur de récupérer des données directement dans une application générée par Gatsby en utilisant GraphQL.

Voici quelques-uns des avantages de l'utilisation de Gatsby :

* Le code HTML est généré côté serveur
* Facilement extensible par l'écosystème de plugins
* Système de construction basé sur Webpack pré-configuré (pas besoin de se casser la tête)
* Optimisé pour la vitesse. Gatsby charge uniquement les parties critiques, de sorte que votre site se charge aussi rapidement que possible. Une fois chargé, Gatsby précharge les ressources pour les autres pages de sorte que cliquer sur le site semble incroyablement rapide.
* Routage automatique basé sur la structure de vos répertoires. (pas besoin de bibliothèque de routage/navigation séparée)

Si vous connaissez les détails de React, vous pouvez certainement commencer avec Gatsbyjs en un rien de temps en lisant ce tutoriel. Je ne vous demande pas d'être avancé avec React mais seulement familier avec ses concepts. Si vous souhaitez rafraîchir vos connaissances sur le même sujet ou en apprendre davantage, je recommande les liens suivants :

* [Officiel de Facebook](https://reactjs.org/)
* [React Express (pas le serveur Express.js)](http://www.react.express/)

Assez avec l'introduction. Commençons.

### Installation de Gatsby CLI

Nous allons utiliser `npm` pour installer notre premier outil de base dont nous avons besoin pour configurer n'importe quel projet Gatsby. Vous pouvez également utiliser `yarn`. Dans votre terminal, veuillez exécuter cette commande :

```bash
npm install --global gatsby-cli
```

Vous devrez peut-être ajouter `sudo` au début de la commande si elle donne une erreur de permissions.

Pour démarrer un nouveau site, allez dans votre répertoire de projet souhaité. Sélectionnez un endroit sur votre système où vous pourriez stocker tous les terrains de jeu ou les applications dans leur phase initiale, puis dans le terminal :

```bash
gatsby new first-gatsby-site
```

Vous pouvez nommer votre projet comme vous le souhaitez, je l'ai nommé ainsi pour la brièveté.

![Image](https://cdn-media-1.freecodecamp.org/images/0*D0A60lp-sDgjvHi1.png)

Terminez l'installation et la configuration du projet. Ensuite, changez le répertoire dans le dossier nouvellement créé. Exécutez `gatsby develop` depuis la ligne de commande pour voir votre site en direct à l'adresse [http://localhost:8000](http://localhost:8000/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*jAK-XXvfqorbpKcv.png)

Dans votre fenêtre de navigateur, l'application Gatsby.js par défaut ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*_ajd3MY423FW8PO6.png)

Laissez la commande en cours d'exécution car elle active le rechargement à chaud. Maintenant, toute modification que nous apportons à notre projet sera reflétée directement, sans actualiser la page.

Actuellement, notre application contient deux pages. Par conséquent, le routage minimal est déjà fait pour nous. Avant de plonger dans le code et d'y apporter des modifications, nous devons comprendre la structure du projet. Ensuite, vous pourrez l'utiliser en le manipulant dans vos futurs projets.

### Plonger profondément dans la structure du projet

![Image](https://cdn-media-1.freecodecamp.org/images/0*9eiAcl39nN1Uj08q.png)

Chaque projet Gatsby contient au moins ces fichiers. Vous pourriez être familier avec certains d'entre eux tels que `node_modules`, le répertoire `public`, qui est servi lors du déploiement. Il contient également `package.json`, qui contient les métadonnées de toute application Javascript moderne.

Notre principal intérêt et préoccupation se trouvent dans le répertoire `src` et le fichier `gatsby-config.js`. Ceux-ci contiennent les métadonnées et autres informations essentielles sur notre application actuelle.

À l'intérieur de `src/`, il y a deux sous-répertoires : `layouts/` et `pages/`.

Le répertoire `layouts/` contient deux fichiers supplémentaires : `index.css` et `index.js`. Ceux-ci servent de point de départ de notre application.

```js
import React from "react";
import PropTypes from "prop-types";
import Link from "gatsby-link";
import Helmet from "react-helmet";

import "./index.css";

const Header = () => (
  <div
    style={{
      background: "rebeccapurple",
      marginBottom: "1.45rem"
    }}
  >
    <div
      style={{
        margin: "0 auto",
        maxWidth: 960,
        padding: "1.45rem 1.0875rem"
      }}
    >
      <h1 style={{ margin: 0 }}>
        <Link
          to="/"
          style={{
            color: "white",
            textDecoration: "none"
          }}
        >
          Gatsby
        </Link>
      </h1>
    </div>
  </div>
);

const TemplateWrapper = ({ children }) => (
  <div>
    <Helmet
      title="My First Gatsby Site"
      meta={[
        { name: "author", content: "amanhimself" },
        { name: "keywords", content: "sample, something" }
      ]}
    />
    <Header />
    <div
      style={{
        margin: "0 auto",
        maxWidth: 960,
        padding: "0px 1.0875rem 1.45rem",
        paddingTop: 0
      }}
    >
      {children()}
    </div>
  </div>
);

TemplateWrapper.propTypes = {
  children: PropTypes.func
};

export default TemplateWrapper;
```

Le composant `Header` contient les styles et le balisage qui servent actuellement d'en-tête à notre application. Il est reflété sur chaque page par `TemplateWrapper`, qui est notre principal composant de mise en page dans l'application. Cela signifie certainement que ce composant peut être utilisé pour afficher un menu de navigation (que nous allons faire dans un instant) ou un pied de page.

La balise `Link` que vous voyez est la manière dont Gatsby permet à nos visiteurs de naviguer d'une page à l'autre. La bibliothèque `react-helmet` qui sert à attacher des informations d'en-tête dans le HTML. Elle est actuellement générée par le JSX. Vous pouvez lire à propos de cette bibliothèque utile et conviviale pour les débutants sur sa [documentation officielle ici](https://github.com/nfl/react-helmet).

Remarquez la prop `{children()}`. Il s'agit d'une fonction qui s'exécute dans le code JSX pour déterminer l'emplacement exact où les composants enfants doivent être rendus.

### Page principale de l'application

Notre deuxième répertoire concerné `pages/` contient le reste des pages qui constituent notre application. Ce sont des composants React simples. Jetons un coup d'œil au fichier `index.js` à l'intérieur de ce répertoire qui sert actuellement de page principale à notre application.

```js
import React from "react";
import Link from "gatsby-link";

const IndexPage = () => (
  <div>
    <h1>Salut les gens</h1>
    <p>Bienvenue sur votre nouveau site Gatsby.</p>
    <p>Maintenant, allez construire quelque chose de grand.</p>
    <Link to="/page-2/">Aller à la page 2</Link>
  </div>
);

export default IndexPage;
```

De même, vous trouverez le code dans `page-2.js`. Si dans notre fenêtre de navigateur, nous essayons de naviguer vers la deuxième page, remarquez l'URL du site lorsque la deuxième page se charge.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6-NTcYa0m_ZMiJmx.png)

Elle est identique au nom du fichier. Nous utilisons également la balise `Link` de Gatsby pour revenir à la page d'accueil.

Ajoutons une autre page à notre site. À l'intérieur du répertoire `pages`, créez un nouveau fichier `page-3.js`.

```js
import React from "react";
import Link from "gatsby-link";

const ThirdPage = () => (
  <div>
    <h1>Troisième Page</h1>
    <p>C'est mon premier site Gatsby</p>
    <Link to="/page-2/">Retour à la Page 2</Link>
    <br />
    <Link to="/">Retour à la page d'accueil</Link>
  </div>
);

export default ThirdPage;
```

Maintenant, ajoutons le lien vers notre nouvelle page à la page d'accueil. Ouvrez le fichier `index.js` :

```js
import React from "react";
import Link from "gatsby-link";

const IndexPage = () => (
  <div>
    <h1>Salut les gens</h1>
    <p>Bienvenue sur votre nouveau site Gatsby.</p>
    <p>Maintenant, allez construire quelque chose de grand.</p>
    <Link to="/page-2/">Aller à la page 2</Link>
    <br />
    <Link to="/page-3">Nouvelle Page !</Link>
  </div>
);

export default IndexPage;
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*y_FCYqu-Zne_IfXH.png)

Cela s'affiche correctement sur notre page. Remarquez le fichier `404.js` dans le répertoire. Ce fichier est rendu lorsqu'aucune URL souhaitée n'est trouvée. Plus d'informations peuvent être lues dans la [documentation officielle de Gatsby](https://www.gatsbyjs.org/docs/add-404-page/).

Maintenant, pour rendre les choses un peu plus intéressantes. Ajoutons un menu de navigation dans le composant `Header` de notre mise en page.

### Ajout d'un menu de navigation

Ouvrez `layouts/index.js` et à l'intérieur du composant `Header`, ajoutez le code suivant :

```js
const Header = () => (
  <div
    style={{
      background: "rebeccapurple",
      marginBottom: "1.45rem"
    }}
  >
    <div
      style={{
        margin: "0 auto",
        maxWidth: 960,
        padding: "1.45rem 1.0875rem"
      }}
    >
      <h1 style={{ margin: 0 }}>
        <Link
          to="/"
          style={{
            color: "white",
            textDecoration: "none"
          }}
        >
          Gatsby
        </Link>
        <ul style={{ listStyle: "none", float: "right" }}>
          <li style={{ display: "inline-block", marginRight: "1rem" }}>
            <Link
              style={{
                color: "white",
                textDecoration: "none",
                fontSize: "x-large"
              }}
              to="/"
            >
              Accueil
            </Link>
          </li>
          <li style={{ display: "inline-block", marginRight: "1rem" }}>
            <Link
              style={{
                color: "white",
                textDecoration: "none",
                fontSize: "x-large"
              }}
              to="/page-2"
            >
              Page 2
            </Link>
          </li>
          <li style={{ display: "inline-block", marginRight: "1rem" }}>
            <Link
              style={{
                color: "white",
                textDecoration: "none",
                fontSize: "x-large"
              }}
              to="/page-3"
            >
              Page 3
            </Link>
          </li>
        </ul>
      </h1>
    </div>
  </div>
);
```

Si vous enregistrez le fichier, les résultats sont immédiatement reflétés sur la page d'accueil et sur chaque page.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0ZgP3U6tQtz1rIyz.png)

### Fichier de configuration

[https://gist.github.com/dfbefb5a09c93f1816198d9db253dd6c](https://gist.github.com/dfbefb5a09c93f1816198d9db253dd6c)

Le dernier fichier important de notre préoccupation est `gatsby-config.js` dans le dossier racine. Ce fichier peut contenir les métadonnées du site et des informations supplémentaires telles que les plugins que nous installons en utilisant la commande `npm`. Cependant, leur portée d'utilisation et de préoccupation est uniquement avec un projet généré en utilisant Gatsby CLI. Par défaut, le plugin `gatsby-plugin-react-helmet` est installé.

Une liste complète des plugins est répertoriée [ici](https://www.gatsbyjs.org/docs/plugins/).

### Déploiement de notre site statique

Jusqu'à présent, nous avons créé un site statique minimal qui sert de guide pour ce tutoriel. La dernière étape sur laquelle je souhaite me concentrer est le déploiement. J'utiliserai GitHub Pages pour le déploiement.

Pour déployer un projet sur GitHub Pages, assurez-vous que votre répertoire de travail actuel est initialisé en tant que dépôt git et hébergé sur GitHub. Si c'est bon, ajoutons un module appelé `gh-pages` en tant que dépendance de développement.

```bash
npm install --save-dev gh-pages
```

Ajoutez un script de déploiement dans `package.json` :

```js
"scripts": {
  "deploy": "gatsby build --prefix-paths && gh-pages -d public",
}
```

Dans `gatsby.config.js`, ajoutez le préfixe de chemin du dépôt comme suit :

```js
module.exports = {
  siteMetadata: {
    title: `Gatsby Default Starter`
  },
  pathPrefix: `/first-gatsby-site`,
  plugins: [`gatsby-plugin-react-helmet`]
};
```

Voir la [documentation officielle](https://www.gatsbyjs.org/docs/path-prefix/) sur le préfixe de chemin.

Maintenant, depuis votre terminal, exécutez :

```bash
npm run deploy
```

**Génial !** Votre site est maintenant en ligne sur `[https://username.github.io/project-name/](https://username.github.io/project-name/.)`[.](https://username.github.io/project-name/.)

Vous pouvez trouver le code complet de ce projet sur ce [dépôt GitHub](https://github.com/amandeepmittal/first-gatsby-site)

Pour plus de questions, contactez-moi sur [Twitter](https://twitter.com/amanhimself), ou lisez plus sur moi sur mon [site web](http://amanhimself.me/).