---
title: Comment écrire des applications JavaScript modernes simples avec Webpack et
  des techniques de web progressif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T18:14:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-simple-modern-javascript-apps-with-webpack-and-progressive-web-techniques-a30354eab214
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x8FsCF_x1ZiNhJzGoTyM8A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment écrire des applications JavaScript modernes simples avec Webpack
  et des techniques de web progressif
seo_desc: 'By Anurag Majumdar

  Have you thought about making modern JavaScript applications with the simplest setup
  possible for your next project?

  If so, you have come to the right place!

  JavaScript frameworks exist to help us build applications in a generalize...'
---

Par Anurag Majumdar

Avez-vous pensé à créer des applications JavaScript modernes avec la configuration la plus simple possible pour votre prochain projet ?

Si c'est le cas, vous êtes au bon endroit !

Les frameworks JavaScript existent pour nous aider à construire des applications de manière généralisée avec la plupart des fonctionnalités courantes. Mais la plupart des applications n'ont peut-être pas besoin de toutes les fonctionnalités puissantes d'un framework. Il peut être excessif d'utiliser simplement un framework pour des exigences spécifiques (surtout pour des projets de petite à moyenne échelle).

Aujourd'hui, je vais vous montrer une approche pour utiliser des fonctionnalités modernes et construire vos propres applications Web personnalisées. Vous pouvez également construire votre propre framework sur le dessus des applications d'exemple si vous le souhaitez. Cela reste purement optionnel. La puissance de Vanilla JavaScript nous permet de suivre notre propre style de codage indépendamment des outils utilisés.

### Ce dont nous avons besoin

Avant de commencer, passons rapidement en revue les fonctionnalités dont nous avons besoin.

#### Planification architecturale

Pour garantir un chargement rapide et des expériences cohérentes, nous utiliserons les modèles suivants :

* Architecture Application Shell
* Modèle PRPL (**P**ush, **R**ender, **P**re-cache, **L**azy loading)

#### Configuration de la construction

Nous avons besoin d'une bonne configuration de construction personnalisée, nous utiliserons donc Webpack avec les exigences suivantes :

* Support ES6 et imports dynamiques
* Support SASS et CSS
* Configuration personnalisée pour le développement et la production
* Construction personnalisée du Service Worker

#### Fonctionnalités JavaScript minimales

Nous aborderons les fonctionnalités JavaScript minimales pour nous lancer et produire le résultat souhaité. Je vais vous montrer comment nous pouvons utiliser les fonctionnalités ES6 existantes dans nos applications vanilla au quotidien. Les voici :

* Modules ES6
* Imports dynamiques
* Syntaxe littérale d'objet ou syntaxe de classe ES6
* Fonctions fléchées ES6
* Littéraux de gabarit ES6

À la fin de cet article, vous trouverez une démonstration d'application exemple ainsi que son code source sur GitHub. Approfondissons, d'accord ? 😊

### Planification architecturale

L'avènement des **applications web progressives** a aidé à introduire de nouvelles architectures afin de rendre notre première peinture plus efficace. Combiner les modèles **App Shell** et **PRPL** peut entraîner une réactivité cohérente et des expériences similaires à celles d'une application.

#### Qu'est-ce que l'App Shell et le PRPL ?

**App Shell** est un modèle architectural pour construire des **applications web progressives** où vous livrez les ressources **critiques minimales** afin de charger votre site. Cela consiste essentiellement en toutes les ressources nécessaires pour la première peinture. Vous pouvez également mettre en cache les ressources critiques à l'aide d'un service worker.

**PRPL** fait référence à ce qui suit :

* **P**ousser les ressources critiques (surtout en utilisant HTTP/2) pour la route initiale.
* **R**endre la route initiale.
* **P**ré-cache les routes ou actifs restants.
* **L**azy load les portions d'une application au fur et à mesure des besoins (surtout lorsqu'elles sont requises par un utilisateur).

#### À quoi ressemblent ces architectures en code ?

Les modèles **App Shell** et **PRPL** sont utilisés ensemble pour atteindre les meilleures pratiques.

L'App shell ressemble quelque peu au morceau de code suivant :

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <!-- Styles Critiques -->
    <style>
        html {
            box-sizing: border-box;
        }

        *,
        *:after,
        *:before {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            padding: 0;
            font: 18px 'Oxygen', Helvetica;
            background: #ececec;
        }

        header {
            height: 60px;
            background: #512DA8;
            color: #fff;
            display: flex;
            align-items: center;
            padding: 0 40px;
            box-shadow: 1px 2px 6px 0px #777;
        }

        h1 {
            margin: 0;
        }

        .banner {
            text-decoration: none;
            color: #fff;
            cursor: pointer;
        }

        main {
            display: flex;
            justify-content: center;
            height: calc(100vh - 140px);
            padding: 20px 40px;
            overflow-y: auto;
        }

        button {
            background: #512DA8;
            border: 2px solid #512DA8;
            cursor: pointer;
            box-shadow: 1px 1px 3px 0px #777;
            color: #fff;
            padding: 10px 15px;
            border-radius: 20px;
        }

        .button {
            display: flex;
            justify-content: center;
        }

        button:hover {
            box-shadow: none;
        }

        footer {
            height: 40px;
            background: #2d3850;
            color: #fff;
            display: flex;
            align-items: center;
            padding: 40px;
        }
    </style>
    <title>Vanilla Todos PWA</title>
</head>

<body>

    <body>
        <!-- Section principale de l'application -->
        <header>
            <h3><a class="banner"> Vanilla Todos PWA </a></h3>
        </header>
        <main id="app"></main>
        <footer>
            <span>&copy; 2019 Anurag Majumdar - Vanilla Todos SPA</span>
        </footer>
      
        <!-- Scripts critiques -->
        <script async src="<%= htmlWebpackPlugin.files.chunks.main.entry %>"></script>

        <noscript>
            Ce site utilise JavaScript. Veuillez activer JavaScript dans votre navigateur.
        </noscript>
    </body>
</body>

</html>
```

Vous pouvez voir que l'application shell se compose du balisage minimal comme squelette.

**Lignes 9–82** : Les styles critiques ont été introduits dans le balisage pour garantir l'analyse directe du CSS au lieu de le lier à un autre fichier.

**Lignes 89–96** : Balisage principal de l'application shell ; ces zones seront manipulées plus tard par JavaScript (surtout, le contenu à l'intérieur de la balise main de la ligne 93).

**Ligne 99** : C'est là que les scripts entrent en jeu. L'attribut **async** aide à ne pas bloquer l'analyseur pendant le téléchargement des scripts.

L'application shell impose également les étapes **Push** et **Render** du modèle PR**PL**. Cela se produit lorsque le HTML est analysé par le navigateur pour former des pixels à l'écran. Il trouve facilement toutes les ressources critiques. De plus, les **scripts critiques** sont responsables de l'affichage de la **route initiale** par manipulation du DOM (**Render**).

Cependant, si nous n'utilisons pas de Service Worker pour mettre en cache le shell, il ne sera d'aucune utilité pour les rechargements futurs et les avantages de performance.

L'extrait de code suivant montre un service worker qui met en cache le shell et tous les actifs statiques nécessaires pour l'application.

```js
var staticAssetsCacheName = 'todo-assets-v3';
var dynamicCacheName = 'todo-dynamic-v3';

self.addEventListener('install', function (event) {
    self.skipWaiting();
    event.waitUntil(
      caches.open(staticAssetsCacheName).then(function (cache) {
        cache.addAll([
            '/',
            "chunks/todo.d41d8cd98f00b204e980.js","index.html","main.d41d8cd98f00b204e980.js"
        ]
        );
      }).catch((error) => {
        console.log('Erreur lors de la mise en cache des actifs statiques :', error);
      })
    );
  });

  self.addEventListener('activate', function (event) {
    if (self.clients && clients.claim) {
      clients.claim();
    }
    event.waitUntil(
      caches.keys().then(function (cacheNames) {
        return Promise.all(
          cacheNames.filter(function (cacheName) {
            return (cacheName.startsWith('todo-')) && cacheName !== staticAssetsCacheName;
          })
          .map(function (cacheName) {
            return caches.delete(cacheName);
          })
        ).catch((error) => {
            console.log('Une erreur est survenue lors de la suppression du cache existant :', error);
        });
      }).catch((error) => {
        console.log('Une erreur est survenue lors de la suppression du cache existant :', error);
    }));
  });

  self.addEventListener('fetch', (event) => {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request)
          .then((fetchResponse) => {
              return cacheDynamicRequestData(dynamicCacheName, event.request.url, fetchResponse.clone());
          }).catch((error) => {
            console.log(error);
          });
      }).catch((error) => {
        console.log(error);
      })
    );
  });

  function cacheDynamicRequestData(dynamicCacheName, url, fetchResponse) {
    return caches.open(dynamicCacheName)
      .then((cache) => {
        cache.put(url, fetchResponse.clone());
        return fetchResponse;
      }).catch((error) => {
        console.log(error);
      });
  }
```

**Lignes 4–17** : L'événement d'installation des service workers aide à mettre en cache tous les actifs statiques. Ici, vous pouvez mettre en cache les ressources de l'application shell (CSS, JavaScript, images, etc.) pour la première route (selon App shell). De plus, vous pouvez mettre en cache le reste des actifs de l'application en garantissant que l'application entière peut également fonctionner hors ligne. Cette mise en cache des actifs statiques en dehors du shell principal de l'application garantit l'étape **Pre-cache** du modèle PR**P**L.

**Lignes 19–38** : L'événement d'activation est l'endroit pour nettoyer les caches inutilisés.

**Lignes 40–63** : Ces lignes de code aident à récupérer les ressources du cache si elles sont dans le cache ou à aller sur le réseau. De plus, si un appel réseau est effectué, alors la ressource n'est pas dans le cache et est mise dans un nouveau cache séparé. Ce scénario aide à mettre en cache toutes les données dynamiques pour une application.

Dans l'ensemble, la plupart des parties de l'architecture ont été couvertes. La seule partie restante est l'étape de **chargement paresseux** du modèle PRP**L**. Je vais en discuter en ce qui concerne JavaScript.

### Notre configuration de construction

Qu'est-ce qu'une bonne structure architecturale sans une configuration de construction ? Webpack à la rescousse. Il existe d'autres outils comme Parcel, Rollup, etc., mais tous les concepts que nous appliquons à Webpack peuvent être appliqués à tout outil de ce type.

Je vais associer les concepts utilisés aux plugins afin que vous puissiez maîtriser les bases utilisées pour la configuration du flux de travail. C'est l'étape la plus importante pour commencer avec une bonne configuration de construction réutilisable pour votre propre application pour l'avenir.

Je sais à quel point il est difficile pour des développeurs comme nous de configurer Webpack ou tout autre outil à partir de zéro. L'article suivant a été une inspiration qui m'a aidé à créer ma propre configuration de construction :

[A tale of Webpack 4 and how to finally configure it in the right way. Updated.](https://hackernoon.com/a-tale-of-webpack-4-and-how-to-finally-configure-it-in-the-right-way-4e94c8e7e5c1)

Veuillez vous référer au lien ci-dessus si vous êtes bloqué quelque part avec la configuration de construction. Pour l'instant, vérifions les concepts nécessaires pour la construction.

#### Support ES6 et imports dynamiques

**Babel** est un transpileur populaire qui est là pour nous aider à transpiler les fonctionnalités ES6 en ES5. Nous aurons besoin des packages suivants pour activer babel avec webpack :

* @babel/core
* @babel/plugin-syntax-dynamic-import
* @babel/preset-env
* babel-core
* babel-loader
* babel-preset-env

Voici un exemple de babelrc pour référence :

```js
{
    "presets": ["@babel/preset-env"],
    "plugins": ["@babel/plugin-syntax-dynamic-import"]
}
```

Lors de la configuration de babel, nous devons alimenter la **2ème ligne** dans les presets pour permettre à babel de transpiler ES6 en ES5 et la **3ème ligne** dans les plugins pour activer le support d'import dynamique avec Webpack.

Voici comment babel est utilisé avec Webpack :

```js
module.exports = {
    entry: {
        // Mentionner le fichier d'entrée
    },
    output: {
        // Mentionner les noms de fichiers de sortie
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    },
    plugins: [
        // Plugins
    ]
};
```

**Lignes 10–17** : Le chargeur babel est utilisé pour configurer le processus de transpilation babel dans webpack.config.js. Pour simplifier, les autres parties de la configuration ont été éliminées ou commentées.

#### Support SASS et CSS

Pour configurer SASS et CSS, vous avez besoin des packages suivants :

* sass-loader
* css-loader
* style-loader
* MiniCssExtractPlugin

Voici à quoi ressemble la configuration :

```js
module.exports = {
    entry: {
        // Mentionner le fichier d'entrée
    },
    output: {
        // Mentionner les noms de fichiers de sortie
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            },
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].css'
        }),
    ]
};
```

**Lignes 17–25** : C'est la zone où les chargeurs sont enregistrés.

**Lignes 29–31** : Puisque nous utilisons un plugin pour extraire un fichier CSS, nous utilisons ici le **MiniCssExtractPlugin**.

#### Configuration personnalisée pour le développement et la production

Il s'agit de la section la plus importante du processus de construction. Nous savons tous que nous avons besoin d'une configuration de construction pour le développement et la production afin de développer des applications et également de déployer le distributable final sur le web.

Voici les packages qui seront utilisés :

* **clean-webpack-plugin** : Pour le nettoyage du contenu du dossier dist.
* **compression-webpack-plugin** : Pour la compression des fichiers du dossier dist.
* **copy-webpack-plugin** : Pour copier les actifs statiques, les fichiers ou les ressources de la source de l'application vers le dossier dist.
* **html-webpack-plugin** : Pour créer un fichier index.html dans le dossier dist.
* **webpack-md5-hash** : Pour hacher les fichiers sources de l'application dans le dossier dist.
* **webpack-dev-server** : Pour exécuter un serveur de développement local.

Voici le fichier de configuration final de Webpack :

```js
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const WebpackMd5Hash = require('webpack-md5-hash');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');

module.exports = (env, argv) => ({
    entry: {
        main: './src/main.js'
    },
    devtool: argv.mode === 'production' ? false : 'source-map',
    output: {
        path: path.resolve(__dirname, 'dist'),
        chunkFilename:
            argv.mode === 'production'
                ? 'chunks/[name].[chunkhash].js'
                : 'chunks/[name].js',
        filename:
            argv.mode === 'production' ? '[name].[chunkhash].js' : '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            },
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin('dist', {}),
        new MiniCssExtractPlugin({
            filename:
                argv.mode === 'production'
                    ? '[name].[contenthash].css'
                    : '[name].css'
        }),
        new HtmlWebpackPlugin({
            inject: false,
            hash: true,
            template: './index.html',
            filename: 'index.html'
        }),
        new WebpackMd5Hash(),
        new CopyWebpackPlugin([
            // {
            //     from: './src/assets',
            //     to: './assets'
            // },
            // {
            //     from: 'manifest.json',
            //     to: 'manifest.json'
            // }
        ]),
        new CompressionPlugin({
            algorithm: 'gzip'
        })
    ],
    devServer: {
        contentBase: 'dist',
        watchContentBase: true,
        port: 1000
    }
});
```

**Lignes 9–77** : L'ensemble de la configuration webpack est une fonction qui prend deux arguments. Ici, j'ai utilisé **argv**, c'est-à-dire les arguments envoyés lors de l'exécution des commandes webpack ou webpack-dev-server.

L'image ci-dessous montre la section des scripts dans package.json.

![Image](https://cdn-media-1.freecodecamp.org/images/1*99lCHt0UnbFBlTcfFjcgNg.png)
_scripts npm dans package.json_

En conséquence, si nous exécutons **npm run build**, cela déclenchera une construction de production, et si nous exécutons **npm run serve**, cela déclenchera un flux de développement avec un serveur de développement local.

**Lignes 44–77** : Ces lignes montrent comment les plugins et la configuration du serveur de développement doivent être configurés.

**Lignes 59–66** : Ces lignes sont des ressources ou des actifs statiques qui doivent être copiés de la source de l'application.

#### Construction personnalisée du Service Worker

Puisque nous savons tous à quel point il est fastidieux d'écrire les noms de tous les fichiers à nouveau pour la mise en cache, j'ai créé un script de construction personnalisé pour le service worker afin de capturer les fichiers dans le dossier **dist** et de les ajouter ensuite comme contenu du cache dans le modèle de service worker. Enfin, le fichier de service worker sera écrit dans le dossier **dist**.

Les concepts concernant le fichier de service worker dont nous avons parlé seront les mêmes. Voici le script en action :

```js
const glob = require('glob');
const fs = require('fs');

const dest = 'dist/sw.js';
const staticAssetsCacheName = 'todo-assets-v1';
const dynamicCacheName = 'todo-dynamic-v1';

let staticAssetsCacheFiles = glob
    .sync('dist/**/*')
    .map((path) => {
        return path.slice(5);
    })
    .filter((file) => {
        if (/\.gz$/.test(file)) return false;
        if (/sw\.js$/.test(file)) return false;
        if (!/\.+/.test(file)) return false;
        return true;
    });

const stringFileCachesArray = JSON.stringify(staticAssetsCacheFiles);

const serviceWorkerScript = `var staticAssetsCacheName = '${staticAssetsCacheName}';
var dynamicCacheName = '${dynamicCacheName}';
self.addEventListener('install', function (event) {
    self.skipWaiting();
    event.waitUntil(
      caches.open(staticAssetsCacheName).then(function (cache) {
        cache.addAll([
            '/',
            ${stringFileCachesArray.slice(1, stringFileCachesArray.length - 1)}
        ]
        );
      }).catch((error) => {
        console.log('Erreur lors de la mise en cache des actifs statiques :', error);
      })
    );
  });
  self.addEventListener('activate', function (event) {
    if (self.clients && clients.claim) {
      clients.claim();
    }
    event.waitUntil(
      caches.keys().then(function (cacheNames) {
        return Promise.all(
          cacheNames.filter(function (cacheName) {
            return (cacheName.startsWith('todo-')) && cacheName !== staticAssetsCacheName;
          })
          .map(function (cacheName) {
            return caches.delete(cacheName);
          })
        ).catch((error) => {
            console.log('Une erreur est survenue lors de la suppression du cache existant :', error);
        });
      }).catch((error) => {
        console.log('Une erreur est survenue lors de la suppression du cache existant :', error);
    }));
  });
  self.addEventListener('fetch', (event) => {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request)
          .then((fetchResponse) => {
              return cacheDynamicRequestData(dynamicCacheName, event.request.url, fetchResponse.clone());
          }).catch((error) => {
            console.log(error);
          });
      }).catch((error) => {
        console.log(error);
      })
    );
  });
  function cacheDynamicRequestData(dynamicCacheName, url, fetchResponse) {
    return caches.open(dynamicCacheName)
      .then((cache) => {
        cache.put(url, fetchResponse.clone());
        return fetchResponse;
      }).catch((error) => {
        console.log(error);
      });
  }
`;

fs.writeFile(dest, serviceWorkerScript, function(error) {
    if (error) return;
    console.log('Écriture du Service Worker réussie');
});
```

**Lignes 8–18** : C'est l'endroit où tout le contenu du dossier dist est capturé sous forme de tableau **staticAssetsCacheFiles**.

**Lignes 22–85** : Il s'agit du modèle de service worker dont nous avons parlé auparavant. Les concepts sont exactement les mêmes, sauf que nous introduisons des variables dans le modèle afin que nous puissions réutiliser le modèle de service worker et le rendre pratique pour une utilisation future. Ce modèle était également nécessaire puisque nous avions besoin d'ajouter le contenu du dossier **dist** au cache comme indiqué à la **ligne 33**.

**Lignes 87–90** : Enfin, un nouveau fichier de service worker sera écrit dans le dossier **dist** avec son contenu à partir du modèle de service worker **serviceWorkerScript**.

La commande pour exécuter le script ci-dessus est **node build-sw** et elle doit être exécutée après que **webpack --mode production** soit terminé.

Ce script de construction de service worker m'a vraiment beaucoup aidé à mettre en cache les fichiers facilement. Je l'utilise actuellement pour mes propres projets secondaires en raison de sa simplicité et de sa grande facilité à résoudre le problème de mise en cache.

Si vous souhaitez utiliser une bibliothèque pour les fonctionnalités liées aux applications web progressives, vous pouvez opter pour [Workbox](https://developers.google.com/web/tools/workbox/). Cette bibliothèque fait des choses vraiment soignées et possède des fonctionnalités incroyables que vous pouvez contrôler.

#### Dernier regard sur les packages

Voici un exemple de fichier package.json avec toutes les dépendances :

```json
{
  "name": "vanilla-todos-pwa",
  "version": "1.0.0",
  "description": "Une application todo simple utilisant ES6 et Webpack",
  "main": "src/main.js",
  "scripts": {
    "build": "webpack --mode production && node build-sw",
    "serve": "webpack-dev-server --mode=development --hot"
  },
  "keywords": [],
  "author": "Anurag Majumdar",
  "license": "MIT",
  "devDependencies": {
    "@babel/core": "^7.2.2",
    "@babel/plugin-syntax-dynamic-import": "^7.2.0",
    "@babel/preset-env": "^7.2.3",
    "autoprefixer": "^9.4.5",
    "babel-core": "^6.26.3",
    "babel-loader": "^8.0.4",
    "babel-preset-env": "^1.7.0",
    "clean-webpack-plugin": "^1.0.0",
    "compression-webpack-plugin": "^2.0.0",
    "copy-webpack-plugin": "^4.6.0",
    "css-loader": "^2.1.0",
    "html-webpack-plugin": "^3.2.0",
    "mini-css-extract-plugin": "^0.5.0",
    "node-sass": "^4.11.0",
    "sass-loader": "^7.1.0",
    "style-loader": "^0.23.1",
    "terser": "^3.14.1",
    "webpack": "^4.28.4",
    "webpack-cli": "^3.2.1",
    "webpack-dev-server": "^3.1.14",
    "webpack-md5-hash": "0.0.6"
  }
}
```

Rappelez-vous que Webpack est fréquemment mis à jour et que des changements continuent de se produire dans la communauté avec de nouveaux plugins remplaçant les existants. Il est donc important de noter les concepts nécessaires pour une configuration de construction plutôt que les packages réels utilisés.

### Fonctionnalités JavaScript

Nous avons tous un choix : soit écrire notre propre framework pour certaines fonctionnalités à utiliser par notre application telles que la détection de changement, le routage, les modèles de stockage, redux, etc., soit utiliser des packages déjà existants pour de telles fonctionnalités.

Maintenant, je vais parler des fonctionnalités minimales requises afin de structurer la disposition de notre application et de la faire fonctionner. Par la suite, vous pouvez ajouter vos propres frameworks ou packages à l'application.

#### Modules ES6

Nous utiliserons les instructions d'import et d'export ES6 et traiterons chaque fichier comme un module ES6. Cette fonctionnalité est couramment utilisée par des frameworks populaires comme Angular et React et est très pratique. Avec la puissance de notre configuration Webpack, nous pouvons pleinement utiliser la puissance des instructions d'import et d'export.

```jsx
import { appTemplate } from './app.template';
import { AppModel } from './app.model';

export const AppComponent = {
  // Code du composant App ici...
};
```

#### Syntaxe littérale d'objet ou syntaxe de classe ES6

La construction de composants est une partie très importante de notre application. Nous pouvons choisir d'aller avec les dernières normes web comme les Web Components, mais pour garder les choses simples, nous pouvons utiliser la syntaxe littérale d'objet ou la syntaxe de classe ES6.

Le seul problème avec la syntaxe de classe est que nous devons l'instancier puis l'exporter. Donc, pour garder les choses encore plus simples, j'ai utilisé la syntaxe littérale d'objet pour l'architecture des composants.

```jsx
import { appTemplate } from './app.template';
import { AppModel } from './app.model';

export const AppComponent = {

    init() {
        this.appElement = document.querySelector('#app');
        this.initEvents();
        this.render();
    },

    initEvents() {
        this.appElement.addEventListener('click', event => {
            if (event.target.className === 'btn-todo') {
                import( /* webpackChunkName: "todo" */ './todo/todo.module')
                    .then(lazyModule => {
                        lazyModule.TodoModule.init();
                    })
                    .catch(error => 'Une erreur est survenue lors du chargement du module');
            }
        });

        document.querySelector('.banner').addEventListener('click', event => {
            event.preventDefault();
            this.render();
        });
    },

    render() {
        this.appElement.innerHTML = appTemplate(AppModel);
    }
};
```

**Lignes 4–32** : Nous exportons un objet appelé **AppComponent** qui est immédiatement disponible pour une utilisation dans d'autres parties de notre application.

Vous pouvez utiliser la syntaxe de classe ES6 ou les Web Components standard et obtenir une manière plus déclarative d'écrire du code ici. Pour des raisons de simplicité, j'ai choisi d'écrire l'application de démonstration de manière plus impérative.

#### Imports dynamiques

Rappelez-vous que j'ai parlé de la partie manquante "L" du modèle **PRPL** ? L'import dynamique est la solution pour charger paresseusement nos composants ou modules. Puisque nous avons utilisé **App Shell** et **PRPL** ensemble pour mettre en cache le shell et d'autres actifs de route, les imports dynamiques importent le composant ou module paresseux depuis le cache au lieu du réseau.

Notez que si nous n'avions utilisé que l'architecture **App Shell**, les actifs restants de l'application, c'est-à-dire le contenu du dossier **chunks**, n'auraient pas été mis en cache.

**Lignes 15–19** : Voir le code du composant App ; c'est ici que les imports dynamiques brillent. Si nous cliquons sur un bouton ayant la classe **btn-todo**, alors seulement ce **TodoModule** est chargé. D'ailleurs, **TodoModule** est juste un autre fichier JavaScript qui consiste en un ensemble de composants objets.

#### Fonctions fléchées ES6 et littéraux de gabarit ES6

Les fonctions fléchées doivent être utilisées surtout lorsque nous voulons nous assurer que le mot-clé **this** à l'intérieur de la fonction fait référence au contexte environnant où la fonction fléchée est déclarée. En dehors de cela, ces fonctions aident vraiment à créer une syntaxe abrégée.

```jsx
export const appTemplate = model => `
    <section class="app">
        <h3> ${model.title} </h3>
        <section class="button">
            <button class="btn-todo"> Todo Module </button>
        </section>
    </section>
`;
```

L'exemple ci-dessus est une fonction de modèle définie comme une fonction fléchée qui accepte un modèle et retourne une chaîne HTML contenant les données du modèle. L'interpolation de chaîne est effectuée à l'aide des **littéraux de gabarit ES6**. Le vrai avantage des littéraux de gabarit est les **chaînes multi-lignes** et l'**interpolation** des données du modèle dans la chaîne.

Voici un micro-conseil pour gérer la création de modèles de composants et la génération de composants réutilisables : utilisez la fonction **reduce** pour accumuler toutes les chaînes HTML selon l'exemple suivant :

```jsx
const WorkModel = [
    {
        id: 1,
        src: '',
        alt: '',
        designation: '',
        period: '',
        description: ''
    },
    {
        id: 2,
        src: '',
        alt: '',
        designation: '',
        period: '',
        description: ''
    },
    //...
];


const workCardTemplate = (cardModel) => `
<section id="${cardModel.id}" class="work-card">
    <section class="work__image">
        <img class="work__image-content" type="image/svg+xml" src="${
            cardModel.src
        }" alt="${cardModel.alt}" />
    </section>
    <section class="work__designation">${cardModel.designation}</section>
    <section class="work__period">${cardModel.period}</section>
    <section class="work__content">
        <section class="work__content-text">
            ${cardModel.description}
        </section>
    </section>
</section>
`;

export const workTemplate = (model) => `
<section class="work__section">
    <section class="work-text">
        <header class="header-text">
            <span class="work-text__header"> Work </span>
        </header>
        <section class="work-text__content content-text">
            <p class="work-text__content-para">
                Cette zone signifie expérience de travail
            </p>
        </section>
    </section>
    <section class="work-cards">
        ${model.reduce((html, card) => html + workCardTemplate(card), '')}
    </section>
</section>
`;
```

Le morceau de code ci-dessus fait vraiment un travail important. Simple mais intuitif. Il suit un peu d'inspiration des frameworks existants.

**Lignes 1–19** : Il s'agit d'un tableau de modèle exemple sur lequel la fonction reduce peut s'exécuter afin de donner la fonctionnalité de modèle réutilisable.

**Ligne 53** : Cette ligne fait toute la magie en générant plusieurs composants réutilisables en une seule chaîne HTML. La fonction reduce prend l'accumulateur comme premier argument et chaque valeur du tableau comme deuxième argument.

Grâce à ces fonctionnalités simples, nous avons déjà une structure d'application en place. La meilleure façon d'apprendre une fonctionnalité est de la mettre en action, disent-ils, alors nous y voilà. 😊

### Démonstration de l'application

Félicitations pour être arrivé ici !

Cet article a couvert beaucoup de fonctionnalités et il faudra du temps pour maîtriser tous les concepts et techniques.

Voici une démonstration de l'application de liste de tâches construite avec toutes les fonctionnalités discutées dans cet article. [Cliquez ici](https://vanilla-todos-pwa.firebaseapp.com/) pour visiter le site.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6MBoDHLD7IsyNxa1MeXB4Q.gif)
_Démonstration de Vanilla Todos_

[Cliquez ici](https://github.com/anurag-majumdar/vanilla-todos-pwa) pour le lien vers le dépôt GitHub. N'hésitez pas à cloner le dépôt et à parcourir le code pour une meilleure compréhension des exemples conceptuels mentionnés dans l'article.

### Application de production exemple

Le site de production est un portfolio qui a été conçu, développé et conçu à partir de zéro en utilisant exactement les fonctionnalités spécifiées dans cet article. L'**application monopage** est décomposée en modules et composants personnalisés.

La flexibilité et la puissance qui accompagnent **Vanilla JavaScript** sont quelque chose d'unique et aident à produire des résultats étonnants.

[Cliquez ici](http://www.anurag-majumdar.com) pour accéder au site. Voici le site en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rcY16O1cdX0ED3J3eUGPdQ.gif)
_Portfolio personnalisé_

Visitez le site pour vous en faire une idée. Les couleurs ne sont pas reproduites avec précision dans la démonstration ici. L'ingénierie mise dans ce site a produit les résultats suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kxp8u-ojMzi6sfLzSo5Bww.png)
_Résultats Lighthouse du portfolio_

Jamais obtenu un score parfait de 100 auparavant dans aucune matière. 😊

### Conclusion

Il existe plusieurs projets que nous pourrions aimer construire en utilisant Vanilla JavaScript au lieu de frameworks afin d'atteindre certains résultats rapidement. J'ai écrit cet article pour aider les développeurs à utiliser une configuration personnalisée simple pour construire leurs futurs projets.

Le meilleur aspect du framework Vanilla est que les développeurs ont la liberté de façonner leurs schémas de pensée d'ingénierie selon divers cas d'utilisation. Qu'il s'agisse de programmation impérative ou déclarative, de création ou d'utilisation des dernières fonctionnalités existantes. Tant que nous produisons des applications cohérentes et performantes avec une bonne maintenabilité du code, notre travail est fait pour la journée.

Bon codage ! 😊

### Autres articles de moi

Retrouvez-moi sur [https://medium.com/@anurag.majumdar](https://medium.com/@anurag.majumdar)

#### ➡ Développement Web

* [Progressive Web App Shell : La clé pour charger votre site en moins d'une seconde !](https://medium.com/udacity-google-india-scholars/build-your-own-reusable-app-shell-from-scratch-7823f65e1fbd)
* [« Super » et « Extends » en JavaScript ES6 — Comprendre les parties difficiles](https://medium.com/beginners-guide-to-mobile-web-development/super-and-extends-in-javascript-es6-understanding-the-tough-parts-6120372d3420)
* [Introduction aux Polyfills et leur utilisation](https://medium.com/beginners-guide-to-mobile-web-development/introduction-to-polyfills-their-usage-9cd6db4b1923)

#### ➡ Événement de vie

* [Le défi de bourse Udacity Google Mobile Web et ses effets glorieux !](https://medium.com/@anurag.majumdar/udacitys-google-mobile-web-scholarship-challenge-and-its-glorious-effects-9cd4979f5053)