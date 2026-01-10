---
title: Comment décoller avec WebAssembly pour Go dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-07T19:21:43.000Z'
originalURL: https://freecodecamp.org/news/taking-off-with-webassembly-for-go-in-react-7c099bd907fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0nvsQXICkyKVMAq4hbYRPg.jpeg
tags:
- name: Go Language
  slug: go
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment décoller avec WebAssembly pour Go dans React
seo_desc: 'By Chris Chuck

  With Go version 1.11, we now get an experimental version of WebAssembly. If you
  don’t know what WebAssembly is, don’t fret. In short, WebAssembly aims to bring
  high performance, assembly-like code into the browser. This allows develope...'
---

Par Chris Chuck

Avec la version 1.11 de Go, nous obtenons maintenant une version expérimentale de [WebAssembly](https://webassembly.org/). Si vous ne savez pas ce qu'est WebAssembly, ne vous inquiétez pas. En bref, WebAssembly vise à apporter un code de type assembleur à haute performance dans le navigateur. Cela permet aux développeurs de mettre des tâches plus intensives en calcul dans le navigateur, que ce soit pour un [jeu](https://webassembly.org/demo/Tanks/) ou pour créer des [animations](https://demos.alanmacleod.eu/wasm-render/pub/) super cool.

Alors, avec cela, je vais vous montrer comment ajouter WebAssembly basé sur Go à une application React ! Ce guide suppose que vous avez une certaine familiarité avec Webpack, Babel et React. Si vous êtes nouveau dans ces technologies, je vous recommande vivement de consulter [ce tutoriel](https://medium.freecodecamp.org/part-1-react-app-from-scratch-using-webpack-4-562b1d231e75).

Ce tutoriel vous montrera comment créer une application React de base qui utilise WebAssembly pour Go. Dans un avenir proche, je vous montrerai comment construire un jeu de morpion dans lequel l'ordinateur est à 100 % invincible et nous utiliserons WebAssembly pour alimenter l'algorithme minimax (ne vous inquiétez pas, c'est plus facile que ça en a l'air !) ?

Le code pour cette partie (et les parties futures) sera sur Github [ici](https://floooh.github.io/oryol/asmjs/InfiniteSpheres.html).

#### Prérequis et installation initiale

Assurez-vous d'avoir Go 1.11 (minimum) et Node.js installés.

J'utilise Chrome version 69 et toutes les versions actuelles de Edge, Firefox et Safari prennent en charge WebAssembly [support](https://caniuse.com/#feat=wasm). Cependant, les résultats de ce tutoriel peuvent varier en fonction de la version/du navigateur.

Passons directement à la pratique, créez un dossier et `cd` dedans.

À l'intérieur de ce dossier, créez un dossier `client` et un dossier `server`.

#### L'application React

Commençons par construire l'application React. Ce n'est rien de plus qu'une application rendue côté client régulière avec quelques extras ajoutés !

D'abord, `cd` dans le dossier `client` et exécutez `npm init -y` pour initialiser votre `package.json`.

Après cela, exécutez ce qui suit :

```
npm install --save react react-dom && npm install --save-dev @babel/core @babel/plugin-proposal-class-properties @babel/plugin-proposal-decorators @babel/plugin-syntax-dynamic-import @babel/polyfill @babel/preset-env @babel/preset-react add-asset-html-webpack-plugin babel-loader html-webpack-plugin webpack webpack-cli webpack-dev-server
```

Une fois que vous avez fait cela, changez la partie `scripts` de votre `package.json` comme suit :

```
"scripts": {  "dev": "webpack-dev-server --mode development",  "build": "webpack --mode production"},
```

Ensuite, dans le dossier client, créez deux fichiers, un `.babelrc` et un `webpack.config.js`.

Dans le `.babelrc`, collez ce qui suit :

```
{  "presets": [ ["@babel/preset-env", { "modules": false } ],  "@babel/preset-react"],  "plugins": [    "@babel/plugin-proposal-class-properties",    ["@babel/plugin-proposal-decorators", { "legacy": true }],    "@babel/plugin-syntax-dynamic-import"  ]}
```

Et dans le `webpack.config.js`, collez ce qui suit :

Notez le `AddAssetHtmlPlugin` que nous utilisons pour injecter le fichier `wasm_exec.js` et le fichier `init_go.js` dans notre application via une balise de script. Ceux-ci doivent être dans l'ordre où ils sont montrés afin que le fichier `wasm_exec.js` s'exécute avant le fichier `init_go.js`. Le fichier `wasm_exec.js` configure simplement l'environnement d'exécution de Go dans le navigateur et le fichier `init_go.js` nous donne une instance globale et utilisable de l'objet Go. Mais nous en parlerons plus tard.

Maintenant, créez un dossier `src` et ajoutez un fichier `index.js`, un fichier `index.html`, un fichier `init_go.js`, un fichier `wasm_exec.js` et un dossier `components` avec un fichier `app.js` dedans. Votre répertoire devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8qMoT7ccXiXFpbNfb5wOew.png)

À partir de là, ajoutez ceci à votre `index.html` :

Dans le `index.js`, ajoutez ceci :

Et dans votre fichier `components/app.js`, ajoutez ce qui suit :

Maintenant, nous avons une application React extrêmement basique !

#### **WebAssembly sur le Client**

Dans le fichier `wasm_exec.js`, collez le code de [ici](https://github.com/golang/go/blob/master/misc/wasm/wasm_exec.js) (omis pour plus de concision).

Comme nous l'avons dit auparavant, cela instancie simplement l'environnement d'exécution de base pour Go dans le client. Il fournit un constructeur global `Go` que nous utiliserons plus tard.

Ensuite, nous devons faire quelque chose avec cet objet `Go`. Donc, dans votre fichier `init_go.js`, ajoutez ce qui suit :

Tout cela crée un nouvel objet `go` à partir du constructeur `Go` que nous avons créé précédemment et le lie à l'état global.

Allez-y et exécutez `npm run dev` puis naviguez vers `localhost:8080` dans le navigateur et vous devriez voir « Hello! » sur votre page web. Pas très intéressant, n'est-ce pas ? Mais ce que vous ne voyez pas, c'est que nous avons injecté notre objet global `go` !

![Image](https://cdn-media-1.freecodecamp.org/images/1*WeKkDngnfaVrJILoAxEJsQ.png)

Maintenant, changez votre fichier `components/app.js` comme suit :

Qu'avons-nous changé ? Commençons par les choses simples. Tout d'abord, nous avons ajouté un attribut `isLoading` à l'état. Cela nous permet de savoir que WebAssembly est encore en train de charger. Dans la fonction `render`, nous utilisons l'attribut `isLoading` de l'état pour rendre conditionnellement une `div` qui dit « Loading » ou un `button`.

Vous vous demandez peut-être : « Ce bouton a un `onClick` avec une fonction `sayHi`, mais je ne vois de fonction `sayHi` nulle part. » C'est là que WebAssembly entre en jeu. Lorsque nous écrivons notre code Go, nous définirons cette fonction et la lierons à l'état global là-bas. C'est pourquoi nous devons attendre que WebAssembly se charge avant de pouvoir rendre notre bouton. Mais nous comblerons ces lacunes plus tard.

En regardant la fonction `componentDidMount`, vous pouvez voir que nous appelons `WebAssembly.instantiateStreaming` qui est la [manière optimale de charger du code WebAssembly](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiateStreaming). Il prend une promesse qui retourne un fichier `wasm` et un `importObject` comme paramètres. Il retourne un module WebAssembly compilé. Cette promesse est une requête fetch vers notre API (que nous construirons ensuite !) et cet endpoint retourne simplement un fichier `wasm`. Après avoir obtenu le module, nous utilisons `go` pour l'exécuter et ensuite nous définissons `isLoading` à `false`.

Mais bien sûr, puisque nous n'avons rien sur `localhost:3000`, cela ne fonctionnera pas.

### Le Serveur

Maintenant, nous devons configurer le serveur pour servir notre fichier `wasm`. Tout d'abord, ouvrez un nouveau terminal et `cd` dans le dossier `server` que vous avez créé précédemment et exécutez `npm init -y` pour initialiser votre `package.json`.

Ensuite, installons quelques packages. Exécutez ce qui suit :

```
npm install --save compression cors express && npm install --save-dev nodemon
```

Changez la partie `scripts` de votre `package.json` comme suit :

```
"scripts": {  "dev": "nodemon index.js"},
```

Maintenant, dans le répertoire `server`, créez un fichier `index.js` et un dossier `go`. Dans ce dossier `go`, créez un fichier `main.go`.

Votre dossier devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8wCMDp9PG5iX4k-GwvJiaA.png)

Dans le `index.js`, collez ce qui suit :

Ce n'est qu'un simple serveur express qui sert un fichier `wasm` à partir du dossier `go`. Créons-le maintenant !

#### **WebAssembly sur le Serveur**

Dans votre fichier `main.go`, ajoutez ceci (un grand merci à TutoiralEdge pour son [tutoriel](https://tutorialedge.net/golang/go-webassembly-tutorial/)) :

Décortiquons cela. Tout d'abord, nous devons importer `fmt` pour l'impression de base et `syscall/js` afin de pouvoir utiliser toutes les nouvelles [fonctionnalités JavaScript](https://tip.golang.org/pkg/syscall/js/?GOOS=js&GOARCH=wasm) de Go. Ensuite, nous créerons notre fonction `sayHi` avec les paramètres `args []js.Value` même si nous n'allons pas passer d'arguments. Tout ce que fait cette fonction est d'imprimer « Hi! »

Dans la fonction `registerCallbacks`, nous lions notre fonction à l'état global dans notre navigateur. Maintenant, lorsque nous appelons la fonction `js.Global().Set`, nous allons d'abord nommer notre variable globale « sayHi » puis l'associer à notre fonction `sayHi` ci-dessus en l'enveloppant dans la fonction `js.NewCallback`.

Enfin, dans notre fonction `main`, nous ouvrons un canal et exécutons `registerCallbacks`. Le canal bloque simplement notre code Go pour qu'il ne termine pas son exécution.

Maintenant, tout ce qui reste est de compiler ce code Go en WebAssembly.

`cd` dans le dossier `go` et exécutez ce qui suit :

```
GOOS=js GOARCH=wasm go build -o main.wasm
```

Remarquez que notre `GOOS` est défini sur `js` et notre `GOARCH` est défini sur `wasm`. Cela signifie que notre système d'exploitation cible est `js` et l'architecture de compilation est `wasm`.

Votre structure de dossier devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yyFpDTmOJifjXkdX_O0OGA.png)

Comme vous pouvez le voir, nous avons maintenant un fichier `main.wasm` que nous pouvons servir.

`cd` retour dans le dossier `server` et exécutez `npm run dev`.

Votre serveur devrait maintenant fonctionner sur `localhost:3000`. Retournez à `localhost:8080` (en supposant que vous avez toujours le client en cours d'exécution) dans votre navigateur et actualisez-le. Après le chargement, ouvrez la console et cliquez sur le bouton. Il devrait imprimer « Hi! » dans la console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6gr60oiGn32hG6QPCfd6Eg.png)
_Ca marche !_

Comme vous l'avez probablement vu, il dira « Loading » pendant un certain temps avant que notre bouton n'apparaisse. C'est le [surcoût](https://medium.com/@mbebenita/webassembly-is-30x-faster-than-javascript-c71ea54d2f96) que nous subissons en utilisant WebAssembly. Cependant, après ce chargement initial, nous pouvons profiter de la gloire des performances de bas niveau et élevées.

Pour arrêter le client et le serveur, appuyez simplement sur `ctrl + c` dans vos terminaux.

### Conclusion

Merci d'avoir lu et j'espère que vous avez apprécié apprendre WebAssembly avec moi. Bien que ce soit une implémentation extrêmement basique de WebAssembly dans React, dans la prochaine partie de cette série, nous créerons un agent IA invincible au morpion. Alors restez à l'écoute si vous êtes intéressé par cela !

Si vous avez des commentaires ou des questions, n'hésitez pas à les laisser ci-dessous.

_Merci encore d'avoir lu ! Veuillez partager, laissez un_ ? (_ou deux), _et bon codage._

Ajoutez-moi sur [LinkedIn](https://www.linkedin.com/in/the-chris-chuck/)!