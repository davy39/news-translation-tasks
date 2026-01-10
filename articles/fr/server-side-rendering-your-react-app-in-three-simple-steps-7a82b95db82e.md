---
title: Comment implémenter le rendu côté serveur dans votre application React en trois
  étapes simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-29T11:41:00.000Z'
originalURL: https://freecodecamp.org/news/server-side-rendering-your-react-app-in-three-simple-steps-7a82b95db82e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5d740569d1a4ca31bc.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
seo_title: Comment implémenter le rendu côté serveur dans votre application React
  en trois étapes simples
seo_desc: 'By Rohit Kumar

  Here’s what we will build in this tutorial: a nice React card like this one.


  In this tutorial, we’ll use server-side rendering to deliver an HTML response when
  a user or crawler hits a page URL. We’ll handle the latter requests on the...'
---

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_wk04sWGQkw36_XLFvPACrA-1.png)

Par Rohit Kumar

Voici ce que nous allons construire dans ce tutoriel : une belle carte React comme celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_wk04sWGQkw36_XLFvPACrA-1.png)

Dans ce tutoriel, nous utiliserons le rendu côté serveur pour fournir une réponse HTML lorsqu'un utilisateur ou un crawler accède à une URL de page. Nous gérerons les requêtes ultérieures côté client.

Pourquoi en avons-nous besoin ?

Laissez-moi vous guider vers la réponse.

## Quelle est la différence entre le rendu côté client et le rendu côté serveur ?

Dans le **rendu côté client**, votre navigateur télécharge une page HTML minimale. Il rend le JavaScript et remplit le contenu.

Le **rendu côté serveur**, en revanche, rend les composants React sur le serveur. Le résultat est du contenu HTML.

Vous pouvez combiner ces deux méthodes pour créer une application isomorphe.

## Inconvénients du rendu de React côté serveur

* Le SSR peut améliorer les performances si votre application est petite. Mais il peut aussi dégrader les performances si elle est lourde.
* Il augmente le temps de réponse (et cela peut être pire si le serveur est occupé).
* Il augmente la taille de la réponse, ce qui signifie que la page prend plus de temps à charger.
* Il augmente la complexité de l'application.

## Quand devez-vous utiliser le rendu côté serveur ?

Malgré ces conséquences du SSR, il existe certaines situations dans lesquelles vous pouvez et devez l'utiliser.

### 1. SEO

Chaque site web veut apparaître dans les recherches. Corrigez-moi si je me trompe.

Malheureusement, les crawlers des moteurs de recherche ne comprennent/pas encore le JavaScript.

Cela signifie qu'ils voient une page blanche, peu importe à quel point votre site est utile.

Beaucoup de gens disent que le crawler de Google [rend maintenant le JavaScript](https://www.searchenginejournal.com/googles-search-crawlers-natively-render-javascript-based-pages/226313/).

Pour tester cela, j'ai déployé l'application sur Heroku. Voici ce que j'ai vu sur la Google Search Console :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KgOtUd6XBbeZvR1FDBGcXA.png)
_Le crawler de Google ne rend pas React_

Une page blanche.

C'était la plus grande raison pour laquelle j'ai exploré le rendu côté serveur. Surtout lorsqu'il s'agit d'une [page pierre angulaire](https://yoast.com/what-is-cornerstone-content/) telle qu'une page de destination, un blog, etc.

Pour vérifier si Google rend votre site, visitez :

Tableau de bord de la Search Console > Crawl > Fetch as Google. Entrez l'URL de la page ou laissez-la vide pour la page d'accueil.

Sélectionnez FETCH AND RENDER. Une fois terminé, cliquez pour voir le résultat.

### 2. Améliorer les performances

Dans le SSR, les performances de l'application dépendent des ressources du serveur et de la vitesse du réseau de l'utilisateur. Cela le rend très utile pour les sites riches en contenu.

_Prenons un exemple_, disons que vous avez un téléphone mobile de prix moyen avec une vitesse internet lente. Vous essayez d'accéder à un site qui télécharge 4 Mo de données avant que vous ne puissiez voir quoi que ce soit.

Pourriez-vous voir quelque chose sur votre écran en 2 à 4 secondes ?

Revisiteriez-vous ce site ?

Je ne pense pas.

Une autre amélioration majeure est le [Temps de la Première Interaction de l'Utilisateur](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive). Il s'agit de la différence de temps entre le moment où un utilisateur accède à l'URL et le moment où il voit le contenu.

Voici la comparaison. Je l'ai testée sur un Mac de développement.

#### React rendu sur le serveur

![Image](https://cdn-media-1.freecodecamp.org/images/1*kYMHoa7OemCHA_KBzJ1w-w.png)
_Rapport de performance SSR (Chrome)_

Le temps de la première interaction est de 300 ms. L'hydratation se termine à 400 ms. L'événement de chargement se termine à environ 500 ms. Vous pouvez voir cela en consultant l'image ci-dessus.

#### React rendu sur le navigateur du client

![Image](https://cdn-media-1.freecodecamp.org/images/1*wquRCRboPDi7Ix2HAxvCAA.png)
_Rapport de performance côté client (Chrome)_

Le temps de la première interaction est de 400 ms. L'événement de chargement se termine à 470 ms.

Le résultat parle de lui-même. Il y a une différence de 100 ms dans le Temps de la Première Interaction de l'Utilisateur pour une application aussi petite.

### Comment cela fonctionne-t-il ? — (4 étapes simples)

* Créez un nouveau Redux Store à chaque requête.
* Optionnellement, dispatch quelques actions.
* Obtenez l'état du Store et effectuez le SSR.
* Envoyez l'état obtenu à l'étape précédente avec la réponse.

Nous utiliserons l'état passé dans la réponse pour créer l'état initial côté client.

Avant de commencer, [clonez/téléchargez l'exemple complet depuis Github](https://github.com/Rohitkrops/ssr) et utilisez-le comme référence.

### Commencer par configurer notre application

Tout d'abord, ouvrez votre éditeur et votre shell préférés. Créez un nouveau dossier pour votre application. Commençons.

```bash
npm init --yes
```

Remplissez les détails. Après la création de `package.json`, copiez les dépendances et les scripts ci-dessous.

Installez toutes les dépendances en exécutant :

```bash
npm install
```

Vous devez configurer Babel et webpack pour que notre script de build fonctionne.

Babel transforme ESM et React en code compris par Node et le navigateur.

Créez un nouveau fichier `.babelrc` et mettez la ligne suivante dedans.

```js
{
  "presets": ["@babel/env", "@babel/react"]
}

```

webpack bundle notre application et ses dépendances en un seul fichier. Créez un autre fichier `webpack.config.js` avec le code suivant dedans :

```js
const path = require('path');module.exports = {
    entry: {
        client: './src/client.js',
        bundle: './src/bundle.js'
    },
    output: {
        path: path.resolve(__dirname, 'assets'),
        filename: "[name].js"
    },
    module: {
        rules: [
            { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
        ]
    }
}
```

Le processus de build produit deux fichiers :

1. `assets/bundle.js` — application pure côté client.
2. `assets/client.js` — compagnon côté client pour le SSR.

Le dossier `src/` contient le code source. Les fichiers compilés par Babel vont dans `views/`. Le répertoire `views` sera créé automatiquement s'il n'est pas présent.

### Pourquoi devons-nous compiler les fichiers source ?

La raison est la différence de syntaxe [entre ESM et CommonJS](http://jsmodules.io/cjs.html). En écrivant React et Redux, nous utilisons largement import et export dans tous les fichiers.

Malheureusement, ils ne fonctionnent pas dans Node. C'est là que Babel vient à la rescousse. Le script ci-dessous indique à Babel de compiler tous les fichiers dans le répertoire `src` et de mettre le résultat dans `views`.

```json
"babel": "babel src -d views",
```

Maintenant, Node peut les exécuter.

### Copier les fichiers précodés et statiques

Si vous avez déjà cloné le dépôt, copiez depuis celui-ci. Sinon, [téléchargez le fichier ssr-static.zip depuis Dropbox](https://www.dropbox.com/s/2iijlivmlye6pqp/ssr-static.zip?dl=0). Extrayez-le et gardez ces trois dossiers à l'intérieur de votre répertoire d'application. Voici ce qu'ils contiennent.

1. L'application React et les composants résident dans `src/components`.
2. Les fichiers Redux dans `src/redux/`.
3. `assets/ & media/` : Contiennent des fichiers statiques tels que `style.css` et des images.

### Côté serveur

Créez deux nouveaux fichiers nommés `server.js` et `template.js` à l'intérieur du dossier `src/`.

### 1. src/server.js

La magie opère ici. C'est le code que vous avez recherché.

```jsx
import React from 'react';
import { renderToString } from 'react-dom/server';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

module.exports = function render(initialState) {
  // Modélise l'état initial  
  const store = configureStore(initialState);
  let content = renderToString(<Provider store={store} ><App /></Provider>);
  const preloadedState = store.getState();
  return {
    content,
    preloadedState
  };
};
```

Au lieu de rendre notre application, nous devons l'envelopper dans une fonction et l'exporter. La fonction accepte l'état initial de l'application.

Voici comment cela fonctionne.

1. Passez `initialState` à `configureStore()`. `configureStore()` retourne une nouvelle instance de Store. Conservez-la dans la variable `store`.
2. Appelez la méthode `renderToString()`, en fournissant notre App en entrée. Elle rend notre application sur le serveur et retourne le HTML produit. Maintenant, la variable `content` stocke le HTML.
3. Obtenez l'état du Redux Store en appelant `getState()` sur `store`. Conservez-le dans une variable `preloadedState`.
4. Retournez le `content` et `preloadedState`. Nous passerons ces éléments à notre template pour obtenir la page HTML finale.

#### `2. src/template.js`

`template.js` exporte une fonction. Elle prend `title`, `state` et `content` en entrée. Elle les injecte dans le template et retourne le document HTML final.

Pour transmettre l'état, le template attache `state` à `window.__STATE__` à l'intérieur d'une balise `<script>`.

Maintenant, vous pouvez lire `state` côté client en accédant à `window.__STATE__`.

Nous incluons également le compagnon SSR `assets/client.js` de l'application côté client dans une autre balise script.

Si vous demandez la version pure client, il ne met que `assets/bundle.js` à l'intérieur de la balise script.

### Le côté client

Le côté client est assez simple.

### 1. src/bundle.js

Voici comment écrire l'enveloppe React et Redux `Provider`. C'est notre application pure côté client. Pas de trucs ici.

```jsx
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

const store = configureStore();
render(
  <Provider store={store} > <App /> </Provider>,
  document.querySelector('#app')
);
```

### 2. src/client.js

Cela vous semble familier ? Oui, il n'y a rien de spécial sauf `window.__STATE__`. Tout ce que nous devons faire est de récupérer l'état initial de `window.__STATE__` et de le passer à notre fonction `configureStore()` en tant qu'état initial.

Jetons un coup d'œil à notre nouveau fichier client :

```jsx
import React from 'react';
import { hydrate } from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

const state = window.__STATE__;
delete window.__STATE__;
const store = configureStore(state);
hydrate(
  <Provider store={store} > <App /> </Provider>,
  document.querySelector('#app')
);
```

Passons en revue les changements :

1. Remplacez `render()` par `hydrate()`. `[hydrate()](https://reactjs.org/docs/react-dom.html#hydrate)` est le même que `render()` mais est utilisé pour hydrater les éléments rendus par `[ReactDOMServer](https://reactjs.org/docs/react-dom-server.html)`. Il garantit que le contenu est le même sur le serveur et le client.
2. Lisez l'état depuis l'objet global window `window.__STATE__`. Stockez-le dans une variable et supprimez le `window.__STATE__`.
3. Créez un nouveau store avec `state` comme initialState.

Tout est fait ici.

## Mettre tout ensemble

### Index.js

C'est le point d'entrée de notre application. Il gère les requêtes et les templates.

Il déclare également une variable `initialState`. Je l'ai modélisée avec des données dans le fichier `assets/data.json`. Nous allons la passer à notre fonction `ssr()`.

_Note : Lors de la référence à un fichier qui est à l'intérieur de `src/` depuis un fichier à l'extérieur de `src/`, utilisez `require()` normal et remplacez `src/` par `views/`. Vous connaissez la raison (compilation Babel)._

Routing

1. `/` : Par défaut, la page d'accueil rendue côté serveur.
2. `/client` : Exemple de rendu purement côté client.
3. `/exit` : Bouton d'arrêt du serveur. Disponible uniquement en développement.

#### Build & Run

Il est temps de construire et d'exécuter notre application. Nous pouvons le faire avec une seule ligne de code.

```bash
npm run build && npm run start
```

Maintenant, l'application est en cours d'exécution à l'adresse [http://localhost:3000](http://localhost:3000/).

### Prêt à devenir un pro de React ?

Je commence une nouvelle série à partir de lundi prochain pour améliorer vos compétences React, immédiatement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TEecv1nLg253xmyGgddhOw.gif)
_lien d'abonnement ci-dessous ?_

### Merci d'avoir lu ceci.

Si vous aimez cela et le trouvez utile, suivez-moi sur [Twitter](http://twitter.com/rohitkrops) & [Webflow](http://bit.ly/2zVj1fX).