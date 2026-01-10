---
title: Webpack pour les rapides et les furieux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-11T12:27:31.000Z'
originalURL: https://freecodecamp.org/news/webpack-for-the-fast-and-the-furious-bf8d3746adbd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SpCunp0GLPDMsjM8hsX0qA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Webpack pour les rapides et les furieux
seo_desc: 'By Ashwin Hariharan


  Also published in my tech blog


  This is a guide that is meant to help you ease your development workflow and save
  your time by using a bunch of awesome tools that you’ve read about on the internet
  (does React Hot Loader ring any ...'
---

Par Ashwin Hariharan

> Également publié dans mon [blog technique](https://blog.booleanhunter.com/webpack-for-the-fast-and-the-furious/)

Ce guide est destiné à vous aider à simplifier votre flux de développement et à gagner du temps en utilisant un ensemble d'outils géniaux dont vous avez lu sur Internet (ça vous dit quelque chose, React Hot Loader ?)

Il est également conçu pour vous aider avec certains des problèmes les plus couramment rencontrés lors de l'utilisation de Webpack — et gagner du temps avant de commencer à vous arracher les cheveux. Après tout, vous voulez aller vite et résoudre d'autres problèmes importants.

Il y a des chances que vous ayez rencontré un ou plusieurs des problèmes suivants :

* Comment avoir plusieurs points d'entrée ?
* Comment shim des modules ?
* L'une des bibliothèques/plugins que j'utilise dépend de jQuery, comment gérer cela ?
* Je continue à obtenir _$ is not defined_ ou une autre erreur stupide dans l'un des plugins jQuery.
* Mon bundling prend une éternité à se terminer.
* J'ai lu un tas de tutoriels sur le remplacement de modules pour ReactJS et je pense que c'est vraiment cool, mais je continue à rencontrer des erreurs lors de la configuration.

Si vous rencontrez ces difficultés, terminez cet article avant de poster l'une de ces questions sur Stack Overflow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lQQ5F_hkfxFwcaWPAThRRA.jpeg)

Je suppose que vous connaissez déjà les avantages de Webpack et à quoi il sert. Si vous êtes débutant et que vous n'avez aucune idée de ce qu'est Webpack, je vous recommande vivement de lire à ce sujet [ici](https://medium.com/@housecor/browserify-vs-webpack-b3d7ca08a0a9#.r4eum99hk).

Je suppose également que vous construisez une application web et non une simple page statique, ce qui signifie que vous aurez un serveur web fonctionnant sur Node et Express. Vous utilisez probablement aussi un pilote NodeJS pour communiquer avec votre base de données — probablement MongoDB ou Redis.

Voici à quoi ressemble un fichier _webpack.config.js_ typique :

```js
/**
 * @Author Ashwin Hariharan
 * @Details Fichier de configuration Webpack pour ajouter de nouveaux vendeurs, définir des points d'entrée et shim des modules.
 */

var webpack = require('webpack');
var path = require("path");

var lib_dir = __dirname + '/public/libs',
    node_dir = __dirname + '/node_modules';
   // bower_dir = __dirname + '/bower_components'

var config = {
    resolve: {
        alias: {
            react: node_dir + '/react',
            reactDom: lib_dir + '/react-dom',
            jquery: lib_dir + '/jquery-1.11.2.min.js', 
            magnificPopup: lib_dir + '/jquery.magnific-popup.js' //Plugin jQuery
        }
    },   

    entry: {
        app: ['./public/src/js/app-main'],
        vendors: ['react','reactDom','jquery','magnificPopup']
    },

    output: {
        path: path.join(__dirname, "public"),
        filename: "dist/js/[name].bundle.js"
    },

    plugins: [
        new webpack.ProvidePlugin({
            jQuery: "jquery",
            'window.jQuery': "jquery"
        }),
        new webpack.optimize.CommonsChunkPlugin('vendors', 'dist/js/vendors.js', Infinity),
    ],
    
    module: {
        noParse: [
            new RegExp(lib_dir + '/react.js'),
            new RegExp(lib_dir +'/jquery-1.11.2.min.js')
        ],
        loaders: [
            { 
                test: /\.js$/, 
                loader: 'babel',
                query: {
                    presets: ['react', 'es2015']
                }
            }, 
        ]
    }
};

module.exports = config;
```

Cette configuration suppose que vous utilisez certains modules Node et des versions dist de quelques bibliothèques enregistrées dans un dossier _public/libs_. Si vous avez lu d'autres tutoriels, vous comprenez ce que font les configurations dans ce fichier, cependant je vais brièvement expliquer à quoi servent quelques éléments de ce fichier :

* **Aliases / vendeurs**

C'est ici que vous incluez toutes vos bibliothèques/modules Node/autres vendeurs et que vous mappez chacun d'eux à des alias. Ensuite, si vous utilisez un module dans une partie de la logique de votre application, vous pouvez écrire ceci (dans votre fichier _app-main.js_ ou tout autre fichier JS) :

```js
var React = require('react');
var ReactDom = require('reactDom');
var $ = require('jquery');

//Votre logique d'application
```

Ou si vous préférez AMD à CommonJS :

```js
define(
    [
        'react',
        'reactDom',
        'jquery'
    ],
    function(React, ReactDom, $) {
        //Votre logique d'application
    }
);
```

Ou en ES6 également :

```js
import React from 'react';
import ReactDom from 'reactDom';
import $ from 'jquery';
```

* **Définir vos points d'entrée**

```js
entry: {

}
```

Ce bloc dans votre configuration permet à Webpack de déterminer où votre application commence son exécution, et il crée des chunks à partir de cela. Avoir plusieurs points d'entrée dans votre application est toujours avantageux. En particulier, vous pouvez ajouter tous vos fichiers vendeurs — comme jQuery et ReactJS — dans un seul chunk. De cette façon, vos fichiers vendeurs resteront les mêmes, même lorsque vous modifiez vos fichiers sources.

Donc, dans la configuration ci-dessus, il y a deux points d'entrée. Un pour l'entrée de votre application où votre JS commence, et un pour vos vendeurs — chacun d'eux mappé à un nom de variable.

* **Votre répertoire de sortie et les noms des fichiers bundle**

```js
output: {
     path: path.join(__dirname, "public"),
     filename: "dist/js/[name].bundle.js"
 },
```

Ce bloc indique à Webpack comment nommer vos fichiers après le processus de build, et où les placer. Dans notre exemple, nous avons deux entrées nommées _app_ et _vendors_, donc après le processus de build, vous aurez deux fichiers appelés _app.bundle.js_ et _vendors.bundle.js_ dans le répertoire _/public/dist/js_.

* **Plugins**

Webpack vient avec un riche écosystème de plugins pour aider à répondre à des besoins spécifiques. Je vais brièvement expliquer quelques-uns des plus couramment utilisés :

* Utilisez le _CommonsChunkPlugin_ pour que Webpack détermine quel code/modules vous utilisez le plus, et le met dans un bundle séparé pour être utilisé n'importe où dans votre application.
* Vous pouvez optionnellement utiliser le _ProvidePlugin_ pour injecter des globaux. Il y a de nombreux plugins jQuery qui dépendent d'une variable globale jQuery comme _$,_ donc en utilisant ce plugin, Webpack peut préfixer _var $ = require("jquery")_ chaque fois qu'il rencontre l'identifiant global _$_. Idem pour tout autre plugin, comme Bootstrap.

En incluant _noParse,_ vous pouvez dire à Webpack de ne pas analyser certains modules. Cela est utile lorsque vous n'avez que la version dist de ces modules/bibliothèques. Améliore le temps de build.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C6GOoIv20fG5PZZdO4yrXQ.jpeg)

* **Loaders**

Maintenant, si vous écrivez du JSX dans votre code React, vous pouvez utiliser soit le _jsx-loader_ soit le _babel-loader_ pour pré-compiler le JSX en JavaScript. Donc vous pouvez exécuter _npm install jsx-loader_ et inclure ceci dans votre configuration :

```js
loaders: [
    {                 
        test: /\.js$/,                 
        loader: 'jsx-loader'             
    },
]
```

Cependant, si vous écrivez votre code en JSX et ES6, alors vous devrez utiliser le _babel-loader,_ ainsi que le plugin babel pour React. Donc exécutez _npm install babel-core babel-loader babel-preset-es2015 babel-preset-react_ et ajoutez ensuite ceci à votre configuration au lieu de ce qui précède.

```js
loaders: [
    { 
         test: /\.js$/, 
         loader: 'babel',
         query: {
             presets: ['react', 'es2015']
         },
         include: path.join(__dirname, 'public')
    }
]
```

De même, vous avez des loaders pour compiler TypeScript, CoffeeScript, etc.

### **Exemple**

* Votre fichier serveur web :

```js
var http = require("http");
var express = require("express");
var consolidate = require('consolidate');
var handlebars = require('handlebars');
var bodyParser = require('body-parser');

var routes = require('./routes');

var app = express();

//Définissez le nom du dossier à partir duquel vous servez la page html.
app.set('views', 'views'); 

//Pour utiliser handlebars comme moteur de template.
app.set('view engine', 'html');
app.engine('html', consolidate.handlebars);

//Définissez le dossier à partir duquel vous servez tous les fichiers statiques comme les images, css, javascripts, bibliothèques, etc.
app.use(express.static('./public')); 

app.use(bodyParser.urlencoded({ extended: true }));
var portNumber = 8000;

http.createServer(app).listen(portNumber, function(){
    console.log('Serveur à l'écoute sur le port '+ portNumber);
  	app.get('/', function(req, res){ 
  	    console.log('requête reçue sur /');
  		res.render('index.html');		
  	});
});
```

* app-main.js à partir duquel notre logique front-end commence :

```js
define(
    [
        'react',
        'reactDom',
        './components/home-page'
    ],
    function(React, ReactDom, HomePage){ 
        console.log('Page d'accueil chargée');
        ReactDom.render(<HomePage />, document.getElementById('componentContainer'));
    }
);
```

* _home-page.js_ est notre composant React parent qui pourrait contenir quelque chose comme ceci :

```js
define(['react', 'jquery', 'magnificPopup'], function(React, $) {
    var HomePage = React.createClass({
        getInitialState: function() {
            return {
                userName: 'ashwin'
            }
        },
        componentDidMount: function() {
            $('.test-popup-link').magnificPopup({
                type: 'image'
                // autres options
            });
        },
    	render: function() {
    	    return (
      	    	<div id="homePage">
      	    	    {this.state.userName}
      	    	    <a className="test-popup-link" href="path-to-image.jpg">Ouvrir la popup</a>
       	    	</div>
    	    );
    	}
    });

    return HomePage;
});
```

Ouvrez votre terminal, allez dans le dossier racine de votre projet et exécutez _webpack_ pour créer deux fichiers : _vendors.bundle.js_ et _app.bundle.js_. Incluez ces deux fichiers dans votre _index.html_ et allez sur [http://localhost:8000](http://localhost:8000) dans votre navigateur. Cela rendra un composant avec votre nom d'utilisateur affiché sur la page web.

Maintenant, à mesure que vous travaillez davantage sur Webpack, vous serez frustré de devoir constamment construire vos fichiers manuellement pour voir les changements reflétés sur votre navigateur. Ne serait-ce pas génial s'il y avait un moyen d'automatiser le processus de build chaque fois que vous apportez une modification à un fichier ? Donc, si vous êtes fatigué de taper la commande _webpack_ et de cliquer sur le bouton de rafraîchissement de votre navigateur chaque fois que vous changez un nom de classe, continuez à lire...

### Automatisation des builds avec Webpack Dev Server et React Hot Loader

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZgWwc89ePisURX5SzcchJQ.png)

Nous allons utiliser ce module génial appelé **Webpack Dev Server**_. C'est un serveur express qui fonctionne sur le port 8080 et émet des informations sur l'état de la compilation vers le client via une connexion socket. Nous allons également utiliser **React Hot Loader** qui est un plugin pour Webpack qui permet un rafraîchissement instantané en direct sans perdre l'état lors de l'édition de composants React.

* **Étape 1** : Alors, exécutez _npm install webpack-dev-server --save-dev_ puis _npm install react-hot-loader --save-dev_

Ensuite, vous devez modifier légèrement votre configuration Webpack pour utiliser ce plugin. Dans vos loaders, ajoutez ceci avant tout autre loader :

```js
{ 
    test: /\.jsx?$/, 
    loaders: ['react-hot'],
    include: path.join(__dirname, 'public')
}
```

Cela indique à Webpack d'utiliser React Hot Loader pour vos composants. Assurez-vous que React Hot Loader vient avant Babel dans le tableau des loaders. Assurez-vous également d'avoir _include: path.join(__dirname, 'public')_ pour éviter de traiter node_modules, sinon vous pourriez obtenir une erreur comme celle-ci :

_Uncaught TypeError: Cannot read property 'NODE_ENV' of undefined_

* **Étape 2** : Modifications de votre _index.html_

Si votre _index.html_ contient quelque chose comme ceci :

```html
<script src="/dist/js/vendors.js"></script>
<script src="/dist/js/app.bundle.js"></script>
```

Changez cela pour pointer vers votre proxy webpack-dev-server :

```html
<script src="http://localhost:8080/dist/js/vendors.js"></script>
<script src="http://localhost:8080/dist/js/app.bundle.js"></script>
```

* **Étape 3** : Exécutez _webpack-dev-server --hot --inline_,

attendez que le bundling soit terminé, puis allez sur [http://localhost:8000](http://localhost:8000) (le port de votre serveur express) dans votre navigateur.

Si vous rencontrez des erreurs lors de la configuration de React Hot Loader, vous trouverez ce [**guide de dépannage**](https://github.com/gaearon/react-hot-loader/blob/master/docs/Troubleshooting.md) et cette réponse géniale sur Stack Overflow sur [**Gestion de la dépendance des plugins jQuery avec Webpack**](http://stackoverflow.com/questions/28969861/managing-jquery-plugin-dependency-in-webpack) très utiles. De plus, vous pouvez jeter un coup d'œil à la configuration Webpack de mes projets [ici](https://github.com/ashwin01/ReactJS-AdminLTE) et [ici](https://github.com/ashwin01/crew-stack).

Ceci n'est destiné qu'au développement. En production, vous devez minifier tous vos fichiers. Exécuter simplement _webpack -p_ minifiera/uglifiera/concaténera tous vos fichiers.

Ne serait-ce pas génial s'il y avait un moyen de visualiser toutes vos dépendances de fichiers dans une belle visualisation en forme d'arbre ? Il existe une application web qui fait cela.

Dans votre terminal, exécutez _webpack --profile --json > stats.json_. Cela générera un fichier JSON appelé stats.json. Allez sur [http://webpack.github.io/analyse/](http://webpack.github.io/analyse/) et téléchargez le fichier, et vous verrez toutes les dépendances dans une structure en forme d'arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UmuieidXSVw6P6sRpYgsGQ.png)

> _Aimez ce que vous lisez ? Vous devriez [vous abonner](http://forum.booleanhunter.com). Je ne perdrai pas votre temps._