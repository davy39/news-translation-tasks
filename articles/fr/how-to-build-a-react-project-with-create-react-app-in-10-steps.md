---
title: Comment construire un projet React avec Create React App en 10 étapes
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-05T17:12:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-project-with-create-react-app-in-10-steps
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/how-to-build-a-react-project-with-create-react-app-in-10-steps.png
tags:
- name: create-react-app
  slug: create-react-app
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment construire un projet React avec Create React App en 10 étapes
seo_desc: 'The package Create React App makes creating and developing React apps a
  breeze.

  It is one of the easiest ways to spin up a new React project and is an ideal choice
  to use for your own personal projects as well as for serious, large-scale applications...'
---

Le package Create React App facilite la création et le développement d'applications React.

C'est l'une des manières les plus simples de lancer un nouveau projet React et c'est un choix idéal pour vos propres projets personnels ainsi que pour des applications sérieuses et à grande échelle.

Nous allons couvrir, étape par étape, comment utiliser toutes les fonctionnalités majeures de Create React App pour construire rapidement et facilement vos propres projets React.

Tout au long de ce guide, j'ai également inclus de nombreux conseils utiles que j'ai appris en construisant des applications avec Create React App pour rendre votre flux de travail encore plus facile.

Commençons.

### Outils dont vous aurez besoin :

* Node installé sur votre ordinateur. Vous pouvez télécharger Node sur [nodejs.org](https://nodejs.org). Create React App nécessite une version de Node d'au moins 10.
* Un gestionnaire de paquets appelé npm. Il est automatiquement inclus dans votre installation de Node. Vous devez avoir une version npm d'au moins 5.2.
* Un bon éditeur de code pour travailler avec nos fichiers de projet. Je recommande vivement d'utiliser l'éditeur Visual Studio Code. Vous pouvez le télécharger sur [code.visualstudio.com](https://code.visualstudio.com).

## Étape 1. Comment installer Create React App

Pour utiliser Create React App, nous devons d'abord ouvrir notre terminal ou ligne de commande sur notre ordinateur.

Pour créer un nouveau projet React, nous pouvons utiliser l'outil `npx`, à condition d'avoir une version npm d'au moins 5.2.

> Note : Vous pouvez vérifier quelle version npm vous avez en exécutant dans votre terminal `npm -v`

npx nous donne la possibilité d'utiliser le package `create-react-app` sans avoir à l'installer d'abord sur notre ordinateur, ce qui est très pratique.

L'utilisation de npx garantit également que nous utilisons la dernière version de Create React App pour créer notre projet :

```bash
npx create-react-app mon-application-react
```

Une fois que nous exécutons cette commande, un dossier nommé "mon-application-react" sera créé à l'endroit que nous avons spécifié sur notre ordinateur et tous les packages dont il a besoin seront automatiquement installés.

> Note : La création d'une nouvelle application React avec create-react-app prend généralement 2-3 minutes, parfois plus.

Create React App nous propose également des modèles à utiliser pour des types spécifiques de projets React.

Par exemple, si nous voulions créer un projet React qui utilise l'outil TypeScript, nous pourrions utiliser un modèle pour cela au lieu d'avoir à installer TypeScript manuellement.

Pour créer une application React qui utilise TypeScript, nous pouvons utiliser le modèle TypeScript de Create React App :

```bash
npx create-react-app mon-application-react --template typescript
```

## Étape 2. Examen de la structure du projet

Une fois que nos fichiers de projet ont été créés et que nos dépendances ont été installées, la structure de notre projet devrait ressembler à ceci :

```
mon-application-react
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
└── src
```

À quoi servent chacun de ces fichiers et dossiers ?

* `README.md` est un fichier markdown qui inclut de nombreux conseils utiles et liens qui peuvent vous aider pendant que vous apprenez à utiliser Create React App. 
* `node_modules` est un dossier qui inclut tout le code lié aux dépendances que Create React App a installées. Vous n'aurez jamais besoin d'entrer dans ce dossier.
* `package.json` gère les dépendances de notre application et ce qui est inclus dans notre dossier node_modules pour notre projet, ainsi que les scripts dont nous avons besoin pour exécuter notre application.
* `.gitignore` est un fichier utilisé pour exclure des fichiers et dossiers du suivi par Git. Nous ne voulons pas inclure de gros dossiers comme le dossier node_modules 
* `public` est un dossier que nous pouvons utiliser pour stocker nos actifs statiques, tels que des images, des svgs et des polices pour notre application React.
* `src` est un dossier qui contient notre code source. C'est là que tout notre code lié à React résidera et c'est ce avec quoi nous travaillerons principalement pour construire notre application.

> Note : Un nouveau dépôt Git est créé chaque fois que vous créez un nouveau projet avec Create React App. Vous pouvez commencer à enregistrer les modifications de votre application immédiatement en utilisant `git add .` et `git commit -m "votre message de commit"`.

## Étape 3. Comment exécuter votre projet React

Une fois que vous avez glissé votre projet dans votre éditeur de code, vous pouvez ouvrir votre terminal (dans VSCode, allez dans View > Terminal).

Pour démarrer votre projet React, vous pouvez simplement exécuter :

```bash
npm start
```

Lorsque nous exécutons notre projet, un nouvel onglet de navigateur s'ouvrira automatiquement sur le navigateur par défaut de notre ordinateur pour afficher notre application.

Le serveur de développement démarrera sur localhost:3000 et, immédiatement, nous pouvons voir la page d'accueil de départ de notre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-02-03-at-8.56.40-PM.png)

D'où vient le contenu de notre application ? 

Il provient du fichier App.js dans le dossier src. Si nous nous rendons dans ce fichier, nous pouvons commencer à apporter des modifications au code de notre application.

```js
// src/App.js

import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

En particulier, supprimons les balises `p` et `a`, et ajoutons un élément `h1` avec le nom de notre application, "React Posts Sharer" :

```js
// src/App.js

import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>React Posts Sharer</h1>
      </header>
    </div>
  );
}

export default App;
```

Lorsque vous enregistrez en utilisant Command/Ctrl + S, vous verrez notre page se mettre à jour immédiatement pour ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-02-03-at-9.04.31-PM.png)

Ce qui est génial avec le serveur de développement, c'est qu'il se rafraîchit automatiquement pour refléter nos modifications. Il n'est pas nécessaire de rafraîchir manuellement le navigateur.

> Note : La seule fois où vous pourriez avoir besoin de rafraîchir le navigateur lorsque vous travaillez avec Create React App, c'est lorsque vous avez une erreur.

## Étape 4. Comment exécuter des tests avec la bibliothèque React Testing Library

Create React App rend très simple le test de votre application React. 

Il inclut tous les packages dont vous avez besoin pour exécuter des tests en utilisant la bibliothèque React Testing Library (`@testing-library/react`).

Un test de base est inclus dans le fichier App.test.js dans src. Il teste que notre composant App affiche avec succès un lien avec le texte "learn react".

Nous pouvons exécuter nos tests avec la commande :

```bash
npm run test
```

> Note : Les tests seront exécutés dans tous les fichiers qui se terminent par .test.js lorsque vous exécutez la commande `npm run test`

Si nous exécutons cela, cependant, notre test échouera. 

C'est parce que nous n'avons plus d'élément de lien, mais un élément de titre. Pour faire passer notre test, nous voulons obtenir un élément de titre avec le texte "React Posts Sharer". 

```js
// src/App.test.js

import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders app title element", () => {
  render(<App />);
  const titleElement = screen.getByText(/React Posts Sharer/i);
  expect(titleElement).toBeInTheDocument();
});
```

Une fois que nous exécutons notre test à nouveau, nous voyons qu'il passe :

```bash
PASS  src/App.test.js

  ✓ renders app title element (54 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        2.776 s, estimated 3 s
Ran all test suites related to changed files.
```

> Note : Lorsque vous exécutez la commande de test, vous n'avez pas besoin de la démarrer et de l'arrêter manuellement. Si vous avez un test qui échoue, vous pouvez sauter dans votre code d'application, corriger votre erreur, et une fois que vous appuyez sur enregistrer, tous les tests seront automatiquement réexécutés.

## Étape 5. Comment modifier les métadonnées de l'application

Comment fonctionne notre projet ? Nous pouvons voir comment en allant dans le fichier index.js.

```js
// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

Le package ReactDOM rend notre application (spécifiquement le composant App et chaque composant à l'intérieur), en l'attachant à un élément HTML avec une valeur d'id de 'root'.

Cet élément peut être trouvé dans `public/index.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>

```

L'ensemble de l'application React est attaché à cette page HTML en utilisant la div avec l'id root que vous voyez ci-dessus.

Nous n'avons pas besoin de changer quoi que ce soit dans les balises `body`. Cependant, il est utile de changer les métadonnées dans les balises `head`, pour informer les utilisateurs et les moteurs de recherche sur notre application spécifique.

Nous pouvons voir qu'il inclut des balises meta pour un titre, une description et une image de favicon (la petite icône dans l'onglet du navigateur).

Vous verrez également plusieurs autres balises comme theme-color, apple-touch-icon et manifest. Celles-ci sont utiles si les utilisateurs veulent ajouter votre application à l'écran d'accueil de leur appareil ou ordinateur.

Dans notre cas, nous pouvons changer le titre en le nom de notre application et la description pour correspondre à l'application que nous créons :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="App for sharing peoples' posts from around the web"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>React Posts Sharer</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>

```

## Étape 6. Comment travailler avec des images et autres actifs

Si nous regardons notre composant App, nous voyons que nous utilisons un élément `img`. 

Ce qui est intéressant, c'est que nous importons un fichier de notre dossier src, comme s'il s'agissait d'une variable exportée de ce fichier.

```js
// src/App.js

import "./App.css";
import logo from "./logo.svg";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>React Posts Sharer</h1>
      </header>
    </div>
  );
}

export default App;
```

Nous pouvons importer des fichiers image et d'autres actifs statiques directement dans nos composants React. Cette fonctionnalité provient de la configuration webpack de Create React App.

Au lieu d'inclure des actifs statiques directement dans notre dossier src, nous avons également la possibilité de les inclure dans notre dossier public.

Si nous déplaçons notre fichier logo.svg de src vers public, au lieu d'importer notre fichier en utilisant la syntaxe d'importation, nous pouvons écrire ce qui suit :

```js
// src/App.js

import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/logo.svg" className="App-logo" alt="logo" />
        <h1>React Posts Sharer</h1>
      </header>
    </div>
  );
}

export default App;
```

Tout fichier placé dans le dossier public peut être utilisé dans les fichiers .js ou .css avec la syntaxe : `/nomdufichier.extension`.

Ce qui est pratique avec Create React App, c'est que nous n'avons pas besoin d'utiliser un élément `img` du tout pour afficher ce svg. 

Nous pouvons importer ce svg en tant que composant en utilisant la syntaxe suivante :

```js
// src/App.js

import { ReactComponent as Logo } from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Logo style={{ height: 200 }} />
        <h1>React Posts Sharer</h1>
      </header>
    </div>
  );
}

export default App;
```

Que se passe-t-il ici ? Nous pouvons importer le fichier svg en tant que ReactComponent puis le renommer comme nous le souhaitons en utilisant le mot-clé `as`.

_En d'autres termes, nous pouvons utiliser notre svg importé comme nous le ferions pour un composant régulier._

Les fichiers svg ont traditionnellement été difficiles à utiliser dans React. Cette syntaxe de composant les rend très faciles à utiliser et nous permet de faire des choses comme utiliser des styles en ligne (comme vous le voyez ci-dessus, où nous définissons la hauteur du logo à 200px).

## Étape 7. Comment installer des dépendances

Pour notre application de partage de posts que nous créons, récupérons quelques données de posts à afficher dans notre application à partir de l'API JSON Placeholder.

Nous pouvons utiliser une dépendance appelée `axios` pour faire une requête afin d'obtenir nos posts.

Pour installer axios, exécutez :

```bash
npm install axios
```

> Note : Vous pouvez installer plus facilement des packages en utilisant la commande raccourcie `npm i axios` au lieu de `npm install`

Lorsque nous installons axios, il sera ajouté à notre dossier `node_modules`. 

Nous pouvons passer en revue toutes les dépendances que nous avons installées directement dans notre fichier package.json et voir qu'axios a été ajouté à la section "dependencies" :

```json
{
  "name": "mon-application-react",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.11.4",
    "@testing-library/react": "^11.1.0",
    "@testing-library/user-event": "^12.1.10",
    "axios": "^0.21.1",
    "react": "^17.0.1",
    "react-dom": "^17.0.1",
    "react-scripts": "4.0.2",
    "web-vitals": "^1.0.1"
  }
}
```

Nous ne l'inclurons pas dans ce projet, mais si vous êtes intéressé par l'utilisation de TypeScript avec votre projet Create React App existant, le processus est très simple.

Vous devez simplement installer la dépendance `typescript` et les définitions de type appropriées à utiliser pour le développement et les tests React :

```bash
npm install typescript @types/node @types/react @types/react-dom @types/jest

```

Après cela, vous pouvez simplement redémarrer votre serveur de développement et renommer tout fichier React qui se termine par .js en .tsx et vous avez un projet React et TypeScript fonctionnel.

## Étape 8. Comment importer des composants

Au lieu d'écrire tout notre code dans le composant App, créons un composant séparé pour récupérer nos données et les afficher.

Nous appellerons ce composant Posts, alors créons un dossier dans src pour contenir tous nos composants et mettons un fichier à l'intérieur : Posts.js.

Le chemin complet pour notre fichier de composant est `src/components/Posts.js`.

Pour récupérer nos posts, nous les demanderons à JSON Placeholder, les mettrons dans une variable d'état appelée posts, puis les mapperons pour afficher leur titre et leur corps :

```js
// src/components/Posts.js

import React from "react";
import axios from "axios";

function Posts() {
  const [posts, setPosts] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("http://jsonplaceholder.typicode.com/posts")
      .then((response) => setPosts(response.data));
  }, []);

  return (
    <ul className="posts">
      {posts.map((post) => (
        <li className="post" key={post.id}>
          <h4>{post.title}</h4>
          <p>{post.body}</p>
        </li>
      ))}
    </ul>
  );
}

export default Posts;

```

Nous récupérons et retournons nos données de posts à partir du composant Posts, mais pour les voir dans notre application, nous devons les importer dans le composant App.

Retournons à App.js et importons-le en allant dans le dossier components et en obtenant le composant Posts de Posts.js.

Après cela, nous pouvons placer notre composant Posts sous notre `header` :

```js
// src/App.js

import Posts from "./components/Posts";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/logo.svg" className="App-logo" alt="logo" />
        <h1>React Posts Sharer</h1>
      </header>
      <Posts />
    </div>
  );
}

export default App;
```

Et nous pouvons voir tous nos posts récupérés sur notre page d'accueil sous notre header :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-02-03-at-11.24.54-PM.png)

## Étape 9 : Comment styliser notre application avec CSS

Notre application pourrait bénéficier de styles améliorés.

Create React App vient avec le support CSS prêt à l'emploi. Si vous allez dans App.js, vous pouvez voir en haut que nous importons un fichier App.css de src.

> Note : Vous pouvez importer des fichiers .css dans n'importe quel composant que vous souhaitez, cependant ces styles seront appliqués globalement à notre application. Ils ne sont pas limités au composant dans lequel le fichier .css est importé.

Dans App.css, nous pouvons ajouter quelques styles pour améliorer l'apparence de notre application :

```css
/* src/App.css */

.App {
  text-align: center;
  margin: 0 auto;
  max-width: 1000px;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

.App-header {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
}

li {
  list-style-type: none;
}

.post {
  margin-bottom: 4em;
}

.post h4 {
  font-size: 2rem;
}
```

Il y a aussi une autre feuille de style globale appelée index.css qui contient des règles de style plus générales.

Dans celle-ci, nous pouvons ajouter quelques propriétés supplémentaires pour l'élément body pour rendre notre arrière-plan sombre et notre texte blanc :

```css
/* src/index.css */

body {
  background-color: #282c34;
  color: white;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

Après avoir ajouté ces styles, nous avons une application beaucoup plus belle :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-02-03-at-11.20.29-PM.png)

Soyez conscient qu'il est également très facile d'ajouter des configurations CSS plus avancées, comme si vous voulez ajouter des modules CSS ou SASS à votre application React. 

Plus de ressources utiles pour le stylisme CSS sont incluses dans votre fichier README.md.

## Étape 10. Comment construire l'application et la publier

Une fois que nous sommes satisfaits de notre application et que nous sommes prêts à la publier, nous pouvons la construire avec la commande suivante :

```bash
npm run build
```

Cette commande créera une version de production optimisée pour notre projet et affichera quels fichiers elle a générés et leur taille :

```bash
Compiled successfully.

File sizes after gzip:

  46.62 KB  build/static/js/2.1500c654.chunk.js
  1.59 KB   build/static/js/3.8022f77f.chunk.js
  1.17 KB   build/static/js/runtime-main.86c7b7c2.js
  649 B     build/static/js/main.ef6580eb.chunk.js
  430 B     build/static/css/main.5ae9c609.chunk.css
```

La sortie provient de l'outil de construction Webpack. 

Il aide à nous donner une idée de la taille de nos fichiers d'application car la taille de nos fichiers .js en particulier peut avoir un grand impact sur les performances de notre application.

Chaque chunk inclut une chaîne ou un hash unique, qui changera à chaque construction pour s'assurer que toute nouvelle déploiement n'est pas sauvegardée (mise en cache) par le navigateur. 

Si nous n'avions pas ce hash de cache-busting pour chacun de nos fichiers, nous ne pourrions probablement pas voir les modifications que nous avons apportées à notre application.

Enfin, nous pouvons exécuter notre projet React construit localement avec l'aide du package npm `serve`. 

Cela est utile pour détecter toute erreur que nous pourrions avoir avec la version finale de notre projet avant de la mettre en ligne sur le web.

Comme create-react-app, nous pouvons utiliser npx pour exécuter `serve` sans l'installer globalement sur notre ordinateur.

```bash
npx serve
```

En utilisant `serve`, notre application démarrera sur un port de développement différent au lieu de 3000. Dans ce cas, localhost:5000.

Et avec cela, nous avons une application React complète prête à être publiée en ligne sur n'importe quel service de déploiement, comme Netlify, Github Pages, ou Heroku !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais souhaité avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*