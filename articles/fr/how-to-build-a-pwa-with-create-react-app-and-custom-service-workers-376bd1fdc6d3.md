---
title: Comment créer une PWA avec Create-React-App et des service workers personnalisés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T16:29:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZFhS3HkqFBOeau1Amj4uBQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: Comment créer une PWA avec Create-React-App et des service workers personnalisés
seo_desc: 'By Zaid Humayun

  Note: This is not a primer on create-react-app or what a service worker is. This
  post assumes prior knowledge of both.

  So, I recently had the opportunity to work on a React project which involved publishing
  the resulting web applicati...'
---

Par Zaid Humayun

**Note : Ceci n'est pas une introduction à create-react-app ou à ce qu'est un service worker. Cet article suppose une connaissance préalable des deux.**

J'ai récemment eu l'opportunité de travailler sur un projet React qui impliquait de publier l'application web résultante en tant que Progressive Web Application (PWA).

J'ai réalisé à quel point il est difficile d'obtenir une PWA avec des routes personnalisées configurées à l'intérieur d'une build Create React App (CRA). J'espère que cela aidera quelqu'un dans une situation similaire.

### **PWAs dans Create-React-App**

Comment obtenir exactement une PWA fonctionnant à l'intérieur de notre shell CRA ?

Maintenant, le shell CRA inclut un service worker par défaut. Vous devriez avoir remarqué que dans un shell CRA de base, à l'intérieur du fichier `index.js`, il y a un appel à `registerServiceWorker` :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
```

Vous pouvez créer une nouvelle application CRA et regarder à l'intérieur du fichier `registerServiceWorker`.

Il semble assez complexe, mais il vérifie simplement si les variables d'environnement sont définies pour une build de production et si un `serviceWorker` est supporté dans le navigateur actuel.

Si vous exécutez une build avec la commande `yarn build`, vous pouvez ouvrir le dossier de build et vérifier à l'intérieur pour voir qu'un fichier `service-worker.js` a été généré. Il s'agit du fichier de service worker par défaut généré par CRA.

Le format du fichier est du JavaScript ES5 en ligne, ce qui le rend un peu difficile à lire. Mais vous pouvez le mettre dans n'importe quel prettifier, et vous devriez voir un fichier plus lisible.

En regardant le fichier ci-dessus, vous devriez voir qu'il crée simplement un cache statique avec le nom de cache suivant : `sw-precache-v3-sw-precache-webpack-plugin-+(selg.registration ? self.registration.scope)`. Il met ensuite en cache tous vos fichiers statiques comme `index.html` et vos fichiers `js` et `css` à l'intérieur de ce cache.

Vous devriez également voir un écouteur d'événement `fetch` qui intercepté un événement fetch et vérifie si l'application demande l'un des actifs statiques précédemment mis en cache.

Maintenant vient la question à un million de dollars : que faire si vous voulez configurer un cache dynamique pour une route spécifique ? En essence, un cache qui se mettra à jour avec les données envoyées par le serveur lorsque l'utilisateur visite une route spécifiée. Notez que cela signifie que les données ne seront pas disponibles au moment de la build, et ne pourront donc pas être mises en cache par le service worker généré par défaut.

### **Limitations des PWAs par défaut dans CRA**

Malheureusement, il n'est pas très facile d'accomplir ce qui précède lorsque vous utilisez CRA. À moins que vous ne soyez prêt à `eject`, bien sûr.

Jetez un œil à ces problèmes GitHub pour voir pourquoi l'équipe de CRA ne supportera pas la personnalisation du service worker par défaut.

[**Custom ServiceWorker config · Issue #2237 · facebook/create-react-app**](https://github.com/facebook/create-react-app/issues/2237)  
[_1.0.0 added Progressive Web App support, is it possible to support custom config in near future? I really don't want to…_github.com](https://github.com/facebook/create-react-app/issues/2237)[**Import scripts in Service Worker by piotr-cz · Pull Request #2714 · facebook/create-react-app**](https://github.com/facebook/create-react-app/pull/2714)  
[_This PR adds an ability to use importScripts option of SWPrecacheWebpackPlugin. How-to: create a file called…_github.com](https://github.com/facebook/create-react-app/pull/2714)

Alors, étant donné que nous ne pouvons pas sembler personnaliser le service-worker par défaut, comment pouvons-nous contourner cela ?

### **Comprendre comment CRA génère un Service Worker**

La première étape pour trouver une solution de contournement pour le système de build est de comprendre comment le système de build fonctionne.

Commençons donc par la [bibliothèque](https://github.com/GoogleChromeLabs/sw-precache) que le système de build utilise pour générer un fichier de service worker.

`sw-precache` est une bibliothèque qui vous permet de générer un fichier de service worker basé sur un modèle. Le fichier modèle est écrit en utilisant le moteur de modélisation d'underscore.

[Voici](https://github.com/GoogleChromeLabs/sw-precache/blob/master/service-worker.tmpl) le lien vers le fichier modèle dans le code source de `sw-precache`.

Encore une fois, le fichier modèle semble complexe, mais il est assez simple une fois que vous arrivez à comprendre le langage de modélisation.

Donc, ce qui se passe lorsque vous exécutez un processus de build dans un shell CRA, en relation avec la génération d'un service worker, est :

1. La bibliothèque `sw-precache` est exécutée en interne
2. Un objet d'options est fourni à `sw-precache` pour permettre la génération du fichier de service worker à partir du modèle
3. Le fichier de service worker est généré dans le dossier `build` avec le nom `service-worker.js`

### **Remplacer le Service Worker par défaut**

Maintenant, comment pouvons-nous remplacer le processus ci-dessus pour permettre à notre propre fichier de service worker personnalisé d'être généré ?

La réponse est basée sur la [réponse stackoverflow](https://stackoverflow.com/questions/47636757/add-more-service-worker-functionality-with-create-react-app?rq=1) de Jeff Posnick (un mainteneur de `sw-precache`).

Tout d'abord, nous devons exécuter la CLI `sw-precache` après le processus de build normal.

Installez la bibliothèque `sw-precache` en exécutant la commande suivante : `npm install --save-dev sw-precache`

Maintenant, la bibliothèque `sw-precache` fonctionne avec un fichier de configuration, qui est fourni via une option sur la CLI. Voici la commande : `sw-precache --config=sw-precache-config.js`, où `sw-precache-config.js` est le nom du fichier de configuration.

Voici un exemple de fichier de configuration.

```
module.exports = {
  staticFileGlobs: [
    'build/static/css/**.css',
    'build/static/js/**.js'
  ],
  swFilePath: './build/service-worker.js',
  templateFilePath: './service-worker.tmpl',
  stripPrefix: 'build/',
  handleFetch: false,
  runtimeCaching: [{
    urlPattern: /this\\.is\\.a\\.regex/,
    handler: 'networkFirst'
  }]
}
```

**Note :** Il est important que vous spécifiiez le swFilePath comme `./build/service-worker.js`. Cela permet au service worker généré à la suite de votre processus de build personnalisé d'écraser celui créé par CRA (ils partagent tous les deux le même nom, dans ce cas). Sinon, vous vous retrouverez avec deux fichiers de service worker dans votre répertoire de build !

Il existe une documentation approfondie sur les propriétés de l'objet et les valeurs valides qui peuvent leur être assignées sur la [page GitHub](https://github.com/GoogleChromeLabs/sw-precache) pour `sw-precache`.

L'option runtimeCaching est particulièrement intéressante, car elle offre une solution très extensible pour vous permettre de définir des règles personnalisées pour que votre service worker réponde au contenu dynamique.

Le templateFilePath est une option pour lorsque vous souhaitez que la CLI utilise votre fichier de modèle de service worker personnalisé. Mais vous allez presque toujours utiliser le fichier de modèle fourni par la bibliothèque elle-même.

Enfin, nous devons fournir le script pour signaler au système de build CRA que nous voulons que notre service worker personnalisé soit généré. Allez-y et installez la bibliothèque `sw-precache`.

Ensuite, mettez à jour le script de build du package.json, avec ce qui suit :

`build: react-scripts build && sw-precache --config=sw-precache-config.js`

Une fois que vous avez exécuté le processus de build avec `npm run build`, vous pouvez ouvrir le dossier de build et voir votre service worker généré.

Exécutez le processus de build avec et sans le service worker personnalisé et notez les différences entre les deux.

### **Conclusion**

Bien que cela puisse sembler une approche très verbeuse pour quelque chose d'aussi simple que la personnalisation d'un service worker, cette approche a l'avantage de vous maintenir fermement dans le shell create-react-app.

Il existe d'autres approches pour générer un service worker personnalisé (en utilisant une combinaison de [react-app-rewire](https://github.com/timarney/react-app-rewired) et [workbox](https://github.com/GoogleChrome/workbox)). J'essaierai de publier cette approche également dans un article.