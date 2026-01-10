---
title: 'Comment configurer Webpack 4 avec Angular 7 : un guide complet'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T21:52:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-configure-webpack-4-with-angular-7-a-complete-guide-9a23c879f471
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uNX5QUpeczuU_CjXouZxnA.jpeg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: webpack
  slug: webpack
seo_title: 'Comment configurer Webpack 4 avec Angular 7 : un guide complet'
seo_desc: 'By Samuel Teboul

  The Angular CLI makes it easy to create an application that already works, right
  out of the box. It is a great tool, but have you never thought: "How does it work?
  How can I build an application without the CLI?"

  Those questions came...'
---

Par Samuel Teboul

L'Angular CLI facilite la création d'une application qui fonctionne déjà, directement après l'installation. C'est un excellent outil, mais vous ne vous êtes jamais demandé : _"Comment cela fonctionne-t-il ? Comment puis-je construire une application sans le CLI ?"_

Ces questions me sont venues à l'esprit lorsque Angular 7 a été publié. J'ai commencé à chercher des réponses sur le web et ce que j'ai trouvé n'était pas à jour pour mon besoin. En effet, comme Angular et webpack évoluent constamment, les dépendances et les configurations aussi.

Dans cet article, vous allez apprendre :

* Comment configurer une application Angular 7 basique, à partir de zéro
* Comment configurer webpack pour le mode développement (compilation Just-in-Time)
* Comment configurer webpack pour le mode production (compilation Ahead-of-Time)

### Angular 7 : configurer une application basique

Créez un nouveau fichier `package.json` et ajoutez les lignes suivantes pour installer Angular et ses dépendances.

```json
"dependencies": 
  "@angular/animations": "~7.0",
  "@angular/common": "~7.0",
  "@angular/compiler": "~7.0",
  "@angular/compiler-cli": "~7.0",
  "@angular/core": "~7.0",
  "@angular/forms": "~7.0",
  "@angular/http": "~7.0",
  "@angular/platform-browser": "~7.0",
  "@angular/platform-browser-dynamic": "~7.0",
  "@angular/platform-server": "~7.0",
  "@angular/router": "~7.0",
  "@angular/upgrade": "~7.0",
  "core-js": "~2.5",
  "rxjs": "~6.3",
  "zone.js": "~0.8"
}
```

J'ai longtemps lutté pour trouver la meilleure structure de dossiers qui convienne à chaque projet Angular, surtout lorsque l'application grandit en taille. Cet [article](https://medium.com/@motcowley/angular-folder-structure-d1809be95542) m'a beaucoup appris sur le sujet.

Créez un nouveau dossier `src` et les dossiers/fichiers suivants à l'intérieur. Toute la logique métier de notre application Angular sera dans ce dossier.

```bash
src
|__ app
    |__ modules
        |__ menu
            |__ components
                |__ menu
                    |__ menu.component.html
                    |__ menu.component.scss
                    |__ menu.component.ts
            |__ menu.module.ts
            |__ menu-routing.module.ts
|__ shared
         |__ components
             |__ home
                 |__ home.component.html
                 |__ home.component.scss
                 |__ home.component.ts
|__ app.component.html
        |__ app.component.scss        
        |__ app.component.ts
        |__ app.module.ts
        |__ app-routing.module.ts
|__ index.html
|__ main.ts
```

Chaque application a au moins un module Angular, le module _racine_ que vous utilisez pour lancer l'application. Par convention, il est généralement appelé `AppModule`. Je crée un autre module, le `MenuModule`, pour vous montrer comment vous pouvez utiliser le chargement paresseux dans votre projet, surtout pour la production.

Quelques points importants :

* `index.html`

Ajouter `<base href="/">` indique à notre routeur Angular comment composer les URLs de navigation. Cette ligne signifie que votre application démarrera à partir du dossier racine, c'est-à-dire localement, elle considérera `localhost:3000/` et sur le serveur, elle considérera le dossier racine.

* `app-routing.module.ts`

Il y a trois étapes principales pour configurer un module de fonctionnalité à chargement paresseux :

1. Créer le module de fonctionnalité
2. Créer le module de routage du module de fonctionnalité
3. Configurer les routes

`{path: 'menu', loadChildren:'./modules/menu/menu.module#MenuModule'}` indique à Angular de charger paresseusement notre module de fonctionnalité `MenuModule` au moment où l'utilisateur visite la route `/menu`.

### Configuration de TypeScript

Ajoutez les lignes suivantes à votre fichier `package.json` :

```json
"devDependencies": {
  "@types/core-js": "~2.5",
  "@types/node": "~10.12",
  "typescript": "~3.1"
}
```

Créez dans le dossier racine de votre projet un fichier `tsconfig.json` :

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "noImplicitAny": true,
    "suppressImplicitAnyIndexErrors": true,
    "lib": ["es6", "dom"],
    "typeRoots": ["node_modules/@types"]
  },
  "exclude": ["node_modules"]
}
```

Ceci est un fichier de configuration TypeScript basique. Il est essentiel d'installer les définitions de types pour `node` et `core-js`. Sans cela, TypeScript ne pourra pas compiler notre application Angular en JavaScript.

### Configuration de Webpack pour le mode développement (compilation Just-in-Time)

Tout d'abord, que signifie _compilation_ ? Cela ne signifie pas compiler les fichiers TypeScript en JavaScript, cela n'est pas lié à Angular. Angular lui-même doit compiler vos templates HTML en JavaScript et cela peut se produire à deux moments différents :

* Après que votre application soit téléchargée dans le navigateur (JiT)

![Image](https://cdn-media-1.freecodecamp.org/images/sRk7L8PTi7CphpbxdOxOGoHPvMx3jfskkjii)
_Compilation JiT_

* Juste après le développement, au moment de la construction, avant que votre application soit téléchargée dans le navigateur (AoT)

![Image](https://cdn-media-1.freecodecamp.org/images/eGuSnScvGTy4JzYxa6Vmo8JXcVZSLTn2H84h)

#### Qu'est-ce que webpack ?

Selon Wikipedia :

> Webpack est un module bundler JavaScript open source. Son but principal est de bundler les fichiers JavaScript pour une utilisation dans un navigateur, mais il est également capable de transformer, bundler ou packager à peu près n'importe quelle ressource ou asset. Webpack prend des modules avec des dépendances et génère des assets statiques représentant ces modules. C'est un module bundler principalement pour JavaScript, mais il peut transformer des assets front-end comme HTML, CSS, et même des images si les plugins correspondants sont inclus.

Pour dire à webpack comment bundler notre application, nous devons configurer ce que nous appelons les [Concepts de base](https://webpack.js.org/concepts/) :

**Entrée** — Un point d'entrée indique quel module webpack doit utiliser pour commencer à construire son graphe de dépendances interne. Webpack déterminera quels autres modules et bibliothèques dépendent de ce point d'entrée (directement et indirectement).

**Sortie** — La propriété de sortie indique à webpack où émettre les bundles qu'il crée et comment nommer ces fichiers. Par défaut, c'est `./dist/main.js` pour le fichier de sortie principal et le dossier `./dist` pour tout autre fichier généré.

**Loaders** — À un niveau élevé, les loaders ont deux propriétés dans votre configuration webpack :

* La propriété test identifie quel(s) fichier(s) doit(vent) être transformé(s).
* La propriété use indique quel loader doit être utilisé pour effectuer la transformation.

**Plugins** — Alors que les loaders sont utilisés pour transformer certains types de modules, les plugins peuvent être utilisés pour effectuer une gamme plus large de tâches comme l'optimisation des bundles, la gestion des assets et l'injection de variables d'environnement.

Tous ces éléments doivent être configurés dans le fichier de configuration webpack `webpack.config.js`.

#### Configurer webpack

Dans le dossier `src`, nous devons créer 2 fichiers supplémentaires :

* `vendor.ts` qui importe uniquement les modules tiers de l'application.
* `polyfills.ts` nous avons besoin de polyfills pour exécuter une application Angular dans la plupart des navigateurs comme expliqué dans le guide [Support des navigateurs](https://v5.angular.io/guide/browser-support). Ce fichier de bundle sera chargé en premier, c'est donc un bon endroit pour configurer l'environnement du navigateur pour la production ou le développement.

Créez un nouveau dossier `config` et les fichiers suivants à l'intérieur :

* `webpack.config.common.js` : configuration que nous utiliserons pour le développement et la production.

**Entrée** — Pour cette application (et pour la plupart d'entre elles en fait), nous avons 3 points d'entrée différents : `vendor.ts`, `polyfills.ts` et `main.ts`.

```json
entry: {
    vendor: './src/vendor.ts',
    polyfills: './src/polyfills.ts',
    main: './src/main.ts'
}
```

**Loaders** — Nous chargeons les fichiers `.html` avec `html-loader` qui est assez standard. Le chargement des fichiers `.scss` est un peu délicat pour une application Angular et j'ai lutté pendant de nombreuses heures pour comprendre comment le faire.

Tout d'abord, nous devons charger les fichiers sass en utilisant deux loaders `sass-loader` et `css-loader`. Si vous voulez faciliter le débogage, surtout en mode développement, il est vraiment important d'ajouter `sourceMap: true` comme option. Dans une application Angular, nous ajoutons des styles aux composants en passant un chemin de fichier au tableau `styleUrls` comme suit `styleUrls: ["./path/styles.scss"]`, mais nous devons avoir le style sous forme de chaîne et `to-string-loader` le fera pour nous et convertira la sortie en chaîne.

```json
{
    test: /\.html$/,
    loader: 'html-loader'
},
{
    test: /\.(scss|sass)$/,
    use: [
        'to-string-loader',
        { 
            loader: 'css-loader', 
            options: { 
                sourceMap: true 
            } 
        },
        { 
            loader: 'sass-loader', 
            options: { 
                sourceMap: true 
            } 
        }
    ],
    include: helpers.root('src', 'app')
}
```

**Plugins** — `CleanWebpackPlugin` supprimera/nettoiera votre dossier de build avant de reconstruire. Le plugin `HtmlWebpackPlugin` générera un fichier HTML5 pour vous qui inclut tous vos bundles webpack dans le corps en utilisant des balises script. Il ne nécessite que le chemin vers le template.

```js
new CleanWebpackPlugin(
    helpers.root('dist'),
    {
        root: helpers.root(),
        verbose: true
    }
),
new HtmlWebpackPlugin({
    template: 'src/index.html'
})
```

* `webpack.config.dev.js` est notre configuration webpack que nous utiliserons uniquement pour le mode développement.

```js
mode: "development"
```

Dans webpack 4, le mode choisi indique à webpack d'utiliser ses optimisations intégrées en conséquence.

```
devtool: 'cheap-module-eval-source-map'
```

Cette option contrôle si et comment les source maps sont générées. En utilisant `cheap-module-eval-source-map`, les Source Maps des loaders sont traitées pour de meilleurs résultats. Cependant, les Source Maps des loaders sont simplifiées à une seule mapping par ligne.

```js
output: {
    path: helpers.root('dist'),
    publicPath: '/',
    filename: '[name].bundle.js',
    chunkFilename: '[id].chunk.js'
}
```

La clé `output` contient un ensemble d'options indiquant à webpack comment et où il doit sortir vos bundles, assets et tout ce que vous bundlez ou chargez avec webpack. Ici, nous disons à webpack de sortir nos bundles dans le dossier `dist`.

```js
optimization: {
    noEmitOnErrors: true
}
```

Passe l'étape d'émission chaque fois qu'il y a des erreurs lors de la compilation. Cela garantit qu'aucun asset erroné n'est émis. La clé `optimization` a de nombreuses autres options qui sont définies par défaut en fonction du mode de configuration webpack (développement/production). Vous pouvez en lire plus à ce sujet [ici](https://webpack.js.org/configuration/optimization/#optimization-noemitonerrors).

```json
{
    test: /\.ts$/,
    loaders: [
        'babel-loader',
        {
            loader: 'awesome-typescript-loader',
            options: {
                configFileName: helpers.root('tsconfig.json')
            }
        },
        'angular2-template-loader',
        'angular-router-loader'
    ],
    exclude: [/node_modules/]
}
```

`angular-router-loader` est un loader webpack qui permet le chargement de modules basé sur des chaînes avec le routeur Angular.

`angular2-template-loader` est un loader en chaîne qui inline tous les html et styles dans les composants Angular.

`awesome-typescript-loader` est actuellement le loader TypeScript webpack le plus rapide. Il utilise la résolution de dépendances pour construire le graphe de dépendances des modules. Cela accélère relativement le processus de build.

`babel-loader` permet de transpiler les fichiers JavaScript.

```js
devServer: {
    historyApiFallback: true,
    stats: 'minimal'
}
```

Lorsque vous utilisez l'[API History HTML5](https://developer.mozilla.org/en-US/docs/Web/API/History), la page `index.html` devra probablement être servie à la place de toute réponse `404`. Pour cela, nous devons activer `historyApiFallback`.

L'option `stats` vous permet de contrôler précisément quelles informations de bundle sont affichées. Cela peut être un bon compromis si vous voulez certaines informations de bundle, mais pas toutes.

#### Ajout de scripts

Ajoutez les lignes suivantes à votre fichier `package.json` :

```json
"scripts": {
  "build:dev": "webpack-dev-server --inline --hot --progress --port 8080"
}
```

`--hot` active le Hot Module Replacement (HMR) de webpack. Il échange, ajoute ou supprime des [modules](https://webpack.js.org/concepts/modules/) pendant qu'une application est en cours d'exécution, sans rechargement complet. Cela peut accélérer considérablement le développement de plusieurs manières :

* Conserver l'état de l'application qui est perdu lors d'un rechargement complet.
* Économiser un temps de développement précieux en ne mettant à jour que ce qui a changé.
* Les modifications apportées au CSS/JS dans le code source entraînent une mise à jour instantanée du navigateur, ce qui est presque comparable à la modification des styles directement dans les outils de développement du navigateur.

Maintenant, vous êtes prêt ! Vous pouvez exécuter `npm run build:dev`, ouvrir votre navigateur et naviguer vers `localhost:8080`.

### Configuration de Webpack pour le mode production (compilation Ahead-of-Time)

#### Avantages de la compilation AoT

* Avec AoT, le navigateur télécharge une version pré-compilée de l'application. Le navigateur charge du code exécutable afin qu'il puisse rendre l'application immédiatement, sans attendre de compiler l'application d'abord.
* Le compilateur inline les templates HTML externes et les feuilles de style CSS dans le JavaScript de l'application, éliminant ainsi les requêtes AJAX séparées pour ces fichiers sources.
* Il n'est pas nécessaire de télécharger le compilateur Angular si l'application est déjà compilée. Le compilateur représente environ la moitié d'Angular lui-même, donc l'omettre réduit considérablement la charge de l'application.
* Le compilateur AoT détecte et signale les erreurs de liaison de template lors de l'étape de build avant que les utilisateurs ne puissent les voir.
* AoT compile les templates HTML et les composants en fichiers JavaScript longtemps avant qu'ils ne soient servis au client. Sans templates à lire et sans évaluation risquée de HTML ou JavaScript côté client, il y a moins d'opportunités pour les attaques par injection.

#### Configurer webpack

Dans votre dossier `config`, créez un nouveau fichier `webpack.config.prod.js`

```js
mode: 'production'
```

Nous procédons généralement à la compilation AoT en mode production et, comme je l'ai écrit précédemment, dans webpack 4, le mode choisi indique à webpack d'utiliser ses optimisations intégrées en conséquence.

```js
output: {
    path: helpers.root('dist'),
    publicPath: '/',
    filename: '[hash].js',
    chunkFilename: '[id].[hash].chunk.js'
}
```

Nous indiquons également à webpack de sortir nos bundles dans le dossier `dist`. Nous incluons un hash dans les noms de fichiers pour tirer parti du cache côté client de manière efficace. De cette façon, webpack sait si un fichier a changé ou non. Webpack fournit des **placeholders** à cet effet. Ces chaînes sont utilisées pour attacher des informations spécifiques aux sorties. Les plus utiles sont :

* `[id]` retourne l'ID du chunk.
* `[path]` retourne le chemin du fichier.
* `[name]` retourne le nom du fichier.
* `[ext]` retourne l'extension. `[ext]` fonctionne pour la plupart des champs disponibles.
* `[hash]` retourne le hash de la build. Si une partie de la build change, cela change également.
* `[chunkhash]` retourne un hash spécifique au chunk d'entrée. Chaque `entry` défini dans la configuration reçoit un hash qui lui est propre. Si une partie de l'entrée change, le hash changera également. `[chunkhash]` est plus granulaire que `[hash]` par définition.
* `[contenthash]` retourne un hash généré basé sur le contenu.

Il est préférable d'utiliser particulièrement `hash` et `chunkhash` uniquement pour la production, car le hachage n'est pas essentiel pendant le développement.

```js
optimization: {
    noEmitOnErrors: true,
    splitChunks: {
        chunks: 'all'
    },
    runtimeChunk: 'single',
    minimizer: [
        new UglifyJsPlugin({
            cache: true,
            parallel: true
        }),
        
         new OptimizeCSSAssetsPlugin({
             cssProcessor: cssnano,
             cssProcessorOptions: {
                 discardComments: {
                     removeAll: true
                 }
             },
             canPrint: false
         })
    ]
}
```

* Comme en mode développement, nous voulons sauter la phase d'émission chaque fois qu'il y a des erreurs lors de la compilation. Cela garantit qu'aucun asset erroné n'est émis.
* `chunks: 'all'` indique quels chunks seront sélectionnés pour l'optimisation. Fournir `all` peut être particulièrement puissant, car cela signifie que les chunks peuvent être partagés même entre les chunks async et non-async.
* Les modules importés sont initialisés pour chaque chunk de runtime séparément. Comme [webpack](https://webpack.js.org/configuration/optimization/#optimization-runtimechunk) le suggère, tout en travaillant sur un projet avec **plusieurs points d'entrée**, vous voulez avoir une seule instance de runtime. Pour cela, vous devez le définir sur `'single'`.
* `UglifyJsPlugin` utilise [uglify-js](https://github.com/mishoo/UglifyJS2) pour minifier vos fichiers JavaScript. Nous définissons les propriétés `cache` et `parallel` à `true` afin d'activer la mise en cache des fichiers et d'utiliser l'exécution parallèle multi-processus pour améliorer la vitesse de build. Il y a plus d'options disponibles et je vous invite à en apprendre plus sur [ce plugin](https://webpack.js.org/plugins/uglifyjs-webpack-plugin/).
* `OptimizeCSSAssetsPlugin` recherchera les assets CSS pendant la build webpack et les optimisera et les minimisera. Le processeur CSS utilisé pour l'optimisation est `cssnano`. Tous les commentaires seront supprimés de notre CSS minifié et aucun message ne sera imprimé dans la console.

```js
module: {
    rules: [
        {
            test: /(?:\.ngfactory\.js|\.ngstyle\.js|\.ts)$/,
            loader: '@ngtools/webpack'
        }
    ]
}

plugins: [
    new ngw.AngularCompilerPlugin({
        tsConfigPath: helpers.root('tsconfig.aot.json'),
        entryModule: helpers.root('src', 'app', 'modules', 'app', 'app.module#AppModule')
    })
]
```

`@ngtools/webpack` est le plugin officiel qui compile AoT vos composants et modules Angular. Le loader fonctionne avec le plugin webpack pour compiler votre TypeScript. Il est important d'inclure les deux et de ne pas inclure d'autre loader de compilateur TypeScript.

#### Ajout du fichier main.aot.ts

Dans le dossier `src`, ajoutez le fichier `main.aot.ts` :

```ts
import { enableProdMode } from '@angular/core';
import { platformBrowser } from '@angular/platform-browser';

import { AppModuleNgFactory } from './app/app.module.ngfactory';

enableProdMode();

platformBrowser().bootstrapModuleFactory(AppModuleNgFactory);
```

Votre point d'entrée `main` est un peu différent en mode production et avec la compilation AoT :

* Importez `enableProdMode` pour désactiver le mode développement d'Angular, ce qui désactive les assertions et autres vérifications dans le framework.
* Importez `platformBrowser` **ET NON** `platformBrowserDynamic` car dans la compilation AoT, votre application est livrée au navigateur déjà compilée, alors qu'en compilation JiT, cela se produit au niveau du navigateur.
* Au lieu d'importer `AppModule`, vous devez importer `AppModuleFactory`, qui est votre application compilée générée par notre compilateur Angular.

#### Ajout de scripts

Ajoutez les scripts suivants à votre fichier `package.json` :

```json
"webpack-prod": "cross-env NODE_ENV=production webpack --mode production"

"build:prod": "npm run build:clean && ngc && npm run webpack-prod && npm run build:clean"

"build:clean": "del-cli 'src/**/*.js' 'src/**/*.js.map' 'src/**/*.ngsummary.json' 'src/**/*.metadata.json' 'src/**/**/*.ngfactory.ts' 'src/**/*.ngstyle.ts' 'src/**/*.shim.ts'"

"serve": "lite-server"
```

* `build:clean` : le compilateur Angular génère de nombreux fichiers afin de compiler votre application. Pour rester propre dans notre projet, nous supprimons tous ces fichiers avant la compilation et après la génération des bundles.
* `build:prod` : exécute le compilateur Angular avec la commande `ngc`, puis exécute webpack en mode production pour générer vos bundles.
* `serve` : j'utilise lite-server pour servir notre application et voir à quoi elle ressemble. Bien sûr, vous n'en aurez pas besoin dans un projet réel car votre application sera servie par le cloud.

Maintenant, vous pouvez exécuter `npm run build:prod` pour compiler votre application Angular et construire vos bundles. Ensuite, exécutez `npm run serve` pour servir votre application dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/39EEGVKAPyVpEV4COWHMG5OkhLsj0s8b-ljg)
_Hugh Jackman appréciant l'article_

J'espère que vous avez apprécié cet article ! Si vous avez des questions/suggestions, faites-le moi savoir dans les commentaires ci-dessous.

Les fichiers du projet sont sur mon GitHub :

[**samteb/Angular-7-Webpack-4**](https://github.com/samteb/Angular-7-Webpack-4)  
[_Contribute to samteb/Angular-7-Webpack-4 development by creating an account on GitHub._github.co](https://github.com/samteb/Angular-7-Webpack-4)