---
title: Tutoriel React Router Version 6 – Comment configurer le routeur et naviguer
  vers d'autres composants
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-12-14T21:41:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-router-version-6
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/react-router-cover.svg.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: Web Development
  slug: web-development
seo_title: Tutoriel React Router Version 6 – Comment configurer le routeur et naviguer
  vers d'autres composants
seo_desc: "In this tutorial, we'll talk about what React Router is and how to use\
  \ it. Then we'll discuss its features and how to use them in your React app to navigate\
  \ to and render multiple components. \nPrerequisites\n\nA React app\nA good understanding\
  \ of what c..."
---

Dans ce tutoriel, nous parlerons de ce qu'est React Router et de la manière de l'utiliser. Ensuite, nous discuterons de ses fonctionnalités et de la manière de les utiliser dans votre application React pour naviguer et rendre plusieurs composants. 

### **Prérequis**

* Une application React
* Une bonne compréhension de ce que sont les composants dans React. 
* Node.js installé.

### Voici un scrim interactif sur la manière de configurer React Router et de naviguer vers d'autres composants :

<iframe src="https://scrimba.com/scrim/crd9bBC6?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## React en tant qu'application monopage (SPA)

Vous devez comprendre comment les pages sont rendues dans une application React avant de vous lancer dans le routage. Cette section est destinée aux débutants – vous pouvez la sauter si vous comprenez déjà ce qu'est une SPA et comment elle se rapporte à React. 

Dans les applications non monopages, lorsque vous cliquez sur un lien dans le navigateur, une requête est envoyée au serveur avant que la page HTML ne soit rendue. 

Dans React, le contenu des pages est créé à partir de nos composants. Ce que fait React Router, c'est intercepter la requête envoyée au serveur et injecter dynamiquement le contenu à partir des composants que nous avons créés. 

C'est l'idée générale derrière les SPA, qui permet de rendre le contenu plus rapidement sans que la page ne soit actualisée.

Lorsque vous créez un nouveau projet, vous verrez toujours un fichier `index.html` dans le dossier public. Tout le code que vous écrivez dans votre composant `App`, qui agit comme le composant racine, est rendu dans ce fichier HTML. Cela signifie qu'il n'y a qu'un seul fichier HTML où votre code sera rendu.

Que se passe-t-il lorsque vous avez un composant différent que vous préféreriez rendre en tant que page différente ? Créez-vous un nouveau fichier HTML ? La réponse est non. React Router – comme son nom l'indique – vous aide à router/naviguer et à rendre votre nouveau composant dans le fichier `index.html`.

Ainsi, en tant qu'application monopage, lorsque vous naviguez vers un nouveau composant en utilisant React Router, le `index.html` sera réécrit avec la logique du composant.

## Comment installer React Router

Pour installer React Router, il vous suffit d'exécuter `npm install react-router-dom@6` dans le terminal de votre projet et d'attendre que l'installation soit terminée. 

Si vous utilisez yarn, utilisez cette commande : `yarn add react-router-dom@6`.

## Comment configurer React Router

La première chose à faire une fois l'installation terminée est de rendre React Router disponible partout dans votre application. 

Pour ce faire, ouvrez le fichier `index.js` dans le dossier `src` et importez `BrowserRouter` depuis `react-router-dom`, puis enveloppez le composant racine (le composant `App`) avec celui-ci. 

Voici à quoi ressemblait initialement le fichier `index.js` :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


```

Après avoir apporté des modifications avec React Router, voici ce que vous devriez avoir :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById("root")
);
```

Tout ce que nous avons fait, c'est remplacer `React.StrictMode` par `BrowserRouter`, qui a été importé depuis `react-router-dom`. Maintenant, les fonctionnalités du routeur sont accessibles depuis n'importe quelle partie de votre application.

## Comment router vers d'autres composants

Nous avons enfin terminé la configuration, alors maintenant nous allons voir comment router et rendre différents composants.

### Étape 1 - Créer plusieurs composants

Nous allons créer les composants `Home`, `About` et `Contact` comme suit :

```js
function Home() {
  return (
    <div>
      <h1>Ceci est la page d'accueil</h1>
    </div>
  );
}

export default Home;

```

```js
import React from 'react'

function About() {
    return (
        <div>
            <h1>Ceci est la page à propos</h1>
        </div>
    )
}

export default About
```

```js
import React from 'react'

function Contact() {
    return (
        <div>
            <h1>Ceci est la page de contact</h1>
        </div>
    )
}

export default Contact
```

### Étape 2 - Définir les routes

Puisque le composant `App` agit comme le composant racine où notre code React est initialement rendu, nous allons créer toutes nos routes dans celui-ci. 

Ne vous inquiétez pas si cela ne vous semble pas très clair – vous comprendrez mieux après avoir regardé l'exemple ci-dessous.

```js
import { Routes, Route } from "react-router-dom"
import Home from "./Home"
import About from "./About"
import Contact from "./Contact"

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="about" element={ <About/> } />
        <Route path="contact" element={ <Contact/> } />
      </Routes>
    </div>
  )
}

export default App

```

Nous avons d'abord importé les fonctionnalités que nous allons utiliser – `Routes` et `Route`. Après cela, nous avons importé tous les composants dont nous avions besoin pour attacher une route. Maintenant, décomposons le processus.

`Routes` agit comme un conteneur/parent pour toutes les routes individuelles qui seront créées dans notre application.

`Route` est utilisé pour créer une seule route. Il prend deux attributs : 

* `path`, qui spécifie le chemin URL du composant souhaité. Vous pouvez appeler ce chemin comme vous le souhaitez. Ci-dessus, vous remarquerez que le premier chemin est une barre oblique (/). Tout composant dont le chemin est une barre oblique sera rendu en premier chaque fois que l'application se charge pour la première fois. Cela implique que le composant `Home` sera le premier composant à être rendu.
* `element`, qui spécifie le composant que la route doit rendre. 

Tout ce que nous avons fait maintenant, c'est définir nos routes et leurs chemins, et les attacher à leurs composants respectifs. 

Si vous venez de la version 5, vous remarquerez que nous n'utilisons pas `exact` et `switch`, ce qui est génial. 

### Étape 3 - Utiliser `Link` pour naviguer vers les routes

Si vous avez codé jusqu'à ce point sans aucune erreur, votre navigateur devrait rendre le composant `Home`. 

Nous allons maintenant utiliser une autre fonctionnalité de React Router pour naviguer vers d'autres pages en fonction de ces routes et chemins que nous avons créés dans le composant `App`. C'est-à-dire : 

```js
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>Ceci est la page d'accueil</h1>
      <Link to="about">Cliquez pour voir notre page à propos</Link>
      <Link to="contact">Cliquez pour voir notre page de contact</Link>
    </div>
  );
}

export default Home;

```

Le composant `Link` est similaire à l'élément d'ancrage (<a>) en HTML. Son attribut `to` spécifie quel chemin le lien vous mène. 

Rappelez-vous que nous avons créé les chemins listés dans le composant `App`, donc lorsque vous cliquez sur le lien, il parcourra vos routes et rendra le composant avec le chemin correspondant.

N'oubliez pas d'importer `Link` depuis `react-router-dom` avant de l'utiliser.

## Conclusion

À ce stade, nous avons vu comment installer, configurer et utiliser les fonctionnalités de base de React Router pour naviguer vers différentes pages dans votre application. Cela couvre assez bien les bases pour commencer, mais il existe de nombreuses autres fonctionnalités plus intéressantes.

Par exemple, vous pouvez utiliser `useNavigate` pour rediriger les utilisateurs vers diverses pages, et vous pouvez utiliser `useLocation` pour obtenir l'URL actuelle. Bon, nous ne commencerons pas un autre tutoriel à la fin de l'article. 

Vous pouvez consulter plus de fonctionnalités dans la [documentation de React Router](https://reactrouter.com/docs/en/v6).

Vous pouvez me trouver sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Abonnez-vous à ma [newsletter](https://www.getrevue.co/profile/The-Congregation-of-Programmers) pour des ressources d'apprentissage gratuites.

Bon codage !