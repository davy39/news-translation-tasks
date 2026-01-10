---
title: Comment activer la syntaxe ES6 (et au-delà) avec Node et Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-23T16:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VAo90seDRpFYq7utRkPEJg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment activer la syntaxe ES6 (et au-delà) avec Node et Express
seo_desc: 'By Jonathan Cunanan

  Have you ever tried to write front-end apps using ES6 syntax, but then  when you
  decided to learn back-end development with Node.js and Express,  you realized that
  you can’t use stuff like import from and  export default?  If so, ...'
---

Par Jonathan Cunanan

Avez-vous déjà essayé d'écrire des applications front-end en utilisant la syntaxe ES6, mais ensuite, lorsque vous avez décidé d'apprendre le développement back-end avec Node.js et Express, vous avez réalisé que vous ne pouviez pas utiliser des choses comme `import from` et `export default` ? Si c'est le cas, vous êtes au bon endroit ! Voici un guide étape par étape sur la façon de configurer vos environnements de développement et de production, de mettre en place des scripts, et en bonus, nous apprendrons comment ajouter des tests !

### Table des matières / Résumé des sujets

* [Comment cela fonctionne-t-il ?](#heading-comment-cela-fonctionne-t-il-une-vue-densemble-de-ce-dont-nous-avons-besoin)
* [Prérequis](#heading-prerequis)
* [Installation d'Express](#heading-installation-dexpress)
* [Configuration des scripts](#heading-configuration-des-scripts)
* [Bonus](#heading-bonus-ajouter-des-tests)
* [TL;DR](#heading-tldr)

### Comment cela fonctionne-t-il ? Une vue d'ensemble de ce dont nous avons besoin

Pour activer une expérience de développement similaire à celle du front-end tout en développant des applications back-end, voici une vue d'ensemble des processus qui se déroulent dans votre projet.

#### Transpileur de code de ES6+ vers ES5

Nous avons besoin d'un package qui traduit la syntaxe ES6 et au-delà en code ES5. Le code ES5 est le style de syntaxe JS qui est lisible par Node.js, comme `module.exports` ou `var module = require('module')`. Notez qu'à l'heure actuelle, presque 99 % de la syntaxe ES6+ peut être utilisée dans Node.js. C'est là que le package appelé [_babel_](https://babeljs.io/) excelle.

Babel prend un fichier js, convertit le code qu'il contient et produit un nouveau fichier.

#### Script qui supprime les fichiers

Chaque fois que nous modifions quelque chose dans notre code, nous le transmettons au transpileur, et il produit une nouvelle copie à chaque fois. C'est pourquoi nous avons besoin d'un script qui supprime les fichiers avant que la nouvelle copie transpilée n'arrive. Et pour cela, il existe un package appelé [rimraf](https://www.npmjs.com/package/rimraf). Rimraf supprime les fichiers. Nous le démontrerons plus tard.

#### Observateur des changements de fichiers

Lors du codage en Node.js, le redémarrage automatique de notre serveur ne vient pas directement comme lorsque l'on fait un projet basé sur create-react-app ou vue-cli. C'est pourquoi nous installerons un package appelé [nodemon](https://www.npmjs.com/package/nodemon), qui exécute quelque chose chaque fois que nous modifions un fichier dans notre code. Nous pouvons utiliser nodemon pour redémarrer notre serveur chaque fois qu'un fichier est modifié.

Voici donc la vue d'ensemble de haut niveau de son fonctionnement. Avec cela, commençons à configurer notre projet.

### Prérequis

Avant de commencer, nous devons configurer certaines choses.

1. Assurez-vous d'avoir Node.js et npm installés. Je recommande d'installer leur dernière version LTS ou leur version stable actuelle. Vous pouvez l'installer via [Node.js Source](https://nodejs.org/en/download/) ou [NVM](https://github.com/creationix/nvm) (Node Version Manager).
2. Connaissance de base des commandes du terminal. La plupart des commandes sont de toute façon dans le tutoriel, donc vous n'avez pas à vous en soucier.
3. Assurez-vous d'avoir votre terminal ouvert et votre éditeur de texte préféré installé.

C'est tout, nous sommes prêts à commencer !

### Installation d'Express

En utilisant le générateur Express, nous allons créer un nouveau projet avec du code généré, déplacer certains fichiers et convertir du code en syntaxe ES6. Nous devons le convertir à ce stade précoce car nous avons besoin d'un moyen de vérifier si notre code ES6 fonctionne.

#### Configuration du projet

Exécutez cette commande dans votre terminal. Vous pouvez nommer `your-project-name` avec le nom que vous souhaitez. Le drapeau `--no-view` signifie que nous n'utiliserons aucun moteur de templating tel que handlebars, ejs ou pug pour notre application Express squelette.

`npx express-generator your-project-name --no-view`

Après avoir créé votre application, vous devez accéder à votre répertoire d'application. Pour Windows Powershell et les terminaux Linux, utilisez :

`cd your-project-name`

Ensuite, ouvrez l'éditeur de texte que vous préférez. Pour ma part, j'utilise simplement VSCode, donc j'ai mon terminal et mon éditeur de texte ouverts en même temps. Mais vous pouvez utiliser n'importe quel éditeur de texte que vous voulez.

#### Installation des packages et déplacement et suppression des fichiers

Après avoir préparé le projet généré, nous devons `installer` les dépendances et déplacer certains dossiers. Exécutez cette commande pour installer Express et d'autres packages.

npm install

Pendant que vous attendez l'installation des dépendances, suivez ces étapes.

* créez un dossier `server/`
* Placez `bin/` , `app.js` et `routes/` à l'intérieur du dossier `server/`.
* Renommez `www`, trouvé dans `bin` en `[www.js](http://www.js)`
* Laissez le dossier `public/` à la racine de votre projet.

Votre structure de fichiers ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image.png)
_Voici à quoi ressemble notre structure de fichiers. Le dossier `public/` est à la racine, et tous les fichiers `.js` sont à l'intérieur du dossier `server/`._

Maintenant, parce que nous avons modifié la structure des fichiers, notre script de démarrage du serveur ne fonctionnera pas. Mais nous allons le corriger en cours de route.

#### Conversion en code ES6

La conversion du code généré en ES6 est un peu fastidieuse, donc je vais simplement poster le code ici et vous pouvez le copier et le coller.

Code pour `bin/www.js` :

Maintenant, parce que nous avons modifié la structure des fichiers, notre script de démarrage du serveur ne fonctionnera pas. Voici ce que nous allons faire pour le corriger. Dans votre fichier package.json, renommez le script de démarrage en `server` trouvé dans un objet JSON appelé `"scripts"`

```json
// package.json
{
  "name": "your-project-name",
  // ....other details
  "scripts": {
    "server": "node ./server/bin/www"
  }
}
```

Vous verrez que nous avons changé le chemin du fichier de `./bin/www` à `./server/bin/www` parce que nous avons déplacé les fichiers dans `server/`. Nous utiliserons le script de démarrage plus tard.

Essayez-le ! Essayez de démarrer le serveur en tapant `npm run server` dans votre terminal, et allez sur `localhost:3000` dans votre navigateur.

#### Conversion du code de niveau supérieur pour utiliser les imports ES6

La conversion du code généré en ES6 est un peu fastidieuse, donc je vais simplement poster le code ici et vous pouvez le copier et le coller.

Code pour `bin/www.js` :

```json
// bin/www.js
/**
 * Module dependencies.
 */
import app from '../app';
import debugLib from 'debug';
import http from 'http';
const debug = debugLib('your-project-name:server');
// ..generated code below.
```

Presque toutes nos modifications ne concernent que le haut et le bas des fichiers. Nous laissons le reste du code généré tel quel.

Code pour `routes/index.js` et `routes/users.js` :

```json
// routes/index.js and users.js
import express from 'express';
var router = express.Router();
// ..stuff below
export default router;
```

Code pour `app.js` :

```json
// app.js
import express from 'express';
import path from 'path';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import indexRouter from './routes/index';
import usersRouter from './routes/users';
var app = express();
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, '../public')));
app.use('/', indexRouter);
app.use('/users', usersRouter);
export default app;
```

Dans `app.js`, parce que nous avons laissé `public/` à la racine du projet, nous devons changer le chemin statique d'Express d'un dossier vers le haut. Remarquez que le chemin `'public'` est devenu `'../public'`.

`app.use(express.static(path.join(__dirname, '../public')));`

D'accord, nous avons terminé la conversion du code ! Configurons nos scripts maintenant.

### Configuration des scripts

Lors de la configuration des scripts, chaque script joue un rôle différent. Et nous réutilisons chaque script npm. Pour nos environnements de développement et de production, ils ont une configuration différente. (Presque identique, vous verrez plus tard) C'est pourquoi nous devons composer nos scripts pour pouvoir les utiliser sans avoir à taper les mêmes choses encore et encore.

#### Installer `npm-run-all`

Puisque certaines commandes du terminal ne fonctionnent pas sur windows cmd, nous devons installer un package appelé `npm-run-all` pour que ce script fonctionne dans n'importe quel environnement. Exécutez cette commande à la racine de votre projet dans le terminal.

`npm install --save npm-run-all`

#### Installer babel, nodemon et rimraf

Babel est un transpileur JavaScript moderne. Un transpileur signifie que votre code JavaScript moderne sera transformé en un format plus ancien que Node.js peut comprendre. Exécutez cette commande à la racine de votre projet dans le terminal. Nous utiliserons la dernière version de babel (Babel 7+).

Notez que Nodemon est notre observateur de fichiers et Rimraf est notre package de suppression de fichiers.

`npm install --save [@babel/core](http://twitter.com/babel/core) [@babel/cli](http://twitter.com/babel/cli) [@babel/preset-env](http://twitter.com/babel/preset-env) nodemon rimraf`

#### Ajout du script de transpilation

Avant que babel ne commence à convertir le code, nous devons lui dire quelles parties du code traduire. Notez qu'il existe de nombreuses configurations disponibles, car babel peut convertir de nombreuses syntaxes JS pour tous les types de besoins différents. Heureusement, nous n'avons pas besoin de nous en soucier car il existe une configuration par défaut disponible. Nous utilisons la configuration par défaut appelée preset-env (celle que nous avons installée précédemment) dans notre fichier package.json pour dire à Babel dans quel format nous transpilons le code.

À l'intérieur de votre fichier `package.json`, créez un objet `"babel"` et mettez ce paramètre.

```
// package.json
{  
  // .. contents above
  "babel": {
    "presets": ["@babel/preset-env"]
  },
}
```

Après cette configuration, nous sommes maintenant prêts à tester si babel convertit vraiment le code. Ajoutez un script nommé transpile dans votre `package.json` :

```
// package.json
"scripts": {
    "start": "node ./server/bin/www",
    "transpile": "babel ./server --out-dir dist-server",
}
```

Maintenant, que s'est-il passé ici ? Tout d'abord, nous devons exécuter la commande cli `babel`, spécifier les fichiers à convertir, dans ce cas, les fichiers dans `server/` et mettre le contenu transpilé dans un dossier différent appelé `dist-server` à la racine de notre projet.

Vous pouvez le tester en exécutant cette commande

`npm run transpile`

Vous verrez un nouveau dossier apparaître.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-1.png)
_Un nouveau dossier appelé dist-server est apparu en raison du script que nous avons exécuté._

Hourra, cela a fonctionné ! ✅ Comme vous pouvez le voir, il y a un dossier qui a la même structure de dossiers que notre dossier serveur mais avec du code converti à l'intérieur. Plutôt cool, non ? L'étape suivante consiste à essayer de faire fonctionner notre serveur !

#### Script de nettoyage

Pour avoir une nouvelle copie à chaque fois que nous transpilons du code dans de nouveaux fichiers, nous avons besoin d'un script qui supprime les anciens fichiers. Ajoutez ce script à votre package.json

```
"scripts": {
  "server": "node ./dist-server/bin/www",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

Ce script npm que nous avons créé signifie qu'il supprime le dossier `dist-server/`

Maintenant, pour combiner transpile et clean, ajoutez un script appelé `build`, qui combine les deux processus.

```
// scripts
"build": "npm-run-all clean transpile"
```

#### Exécution du script de développement

Maintenant que nous avons un script de build, nous devons exécuter notre serveur de développement. Nous allons ajouter un script appelé `dev` dans notre package.json. Cela prend en charge la définition de notre environnement Node sur "development", la suppression de l'ancien code transpilé et son remplacement par un nouveau.

```
"scripts": {
  "build": "npm-run-all clean transpile"
  "server": "node ./dist-server/bin/www",
  "dev": "NODE_ENV=development npm-run-all build server",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

Notez ici que nous avons changé à nouveau le fichier que nous exécutons dans notre script serveur. Nous exécutons le chemin de fichier avec le code transpilé, trouvé dans `dist-server/`.

#### Ajout des scripts de production

Si nous avons un script dev qui définit l'environnement Node sur développement, nous avons un script `prod` qui le définit sur "production". Nous utilisons cette configuration lorsque nous déployons. (Heroku, AWS, DigitalOcean, etc.) Nous ajoutons à nouveau notre script de démarrage et notre script prod dans notre package.json.

```
"scripts": {
  "start": "npm run prod"
  "build": "npm-run-all clean transpile"
  "server": "node ./dist-server/bin/www",
  "dev": "NODE_ENV=development npm-run-all build server",
  "prod": "NODE_ENV=production npm-run-all build server",
  "transpile": "babel ./server --out-dir dist-server",
  "clean": "rimraf dist-server"
}
```

Nous définissons le script `start` par défaut sur prod car le script de démarrage est toujours utilisé par les plateformes de déploiement comme AWS ou Heroku pour démarrer un serveur.

Essayez soit en exécutant `npm start` ou `npm run prod`.

```
// package.json
...
"nodemonConfig": { 
  "exec": "npm run dev",
  "watch": ["server/*", "public/*"],
  "ignore": ["**/__tests__/**", "*.test.js", "*.spec.js"]
},
"scripts": { 
  // ... other scripts
  "watch:dev": "nodemon"
}
```

#### Et si le serveur redémarre automatiquement chaque fois qu'un fichier change ?

Un dernier script, pour compléter notre configuration de développement. Nous devons ajouter un script d'observation de fichiers qui exécute une commande chaque fois qu'un changement est fait dans un fichier. Ajoutez un objet JSON nommé "nodemonConfig" dans votre package.json. C'est là que nous stockons ce que nous disons à l'observateur de faire lorsqu'un fichier change.

Ajoutez également un script appelé `watch:dev` dans votre package.json

```
// package.json
...
"nodemonConfig": { 
  "exec": "npm run dev",
  "watch": ["server/*", "public/*"],
  "ignore": ["**/__tests__/**", "*.test.js", "*.spec.js"]
},
"scripts": { 
  // ... other scripts
  "watch:dev": "nodemon"
}
```

La configuration de Nodemon contient des paramètres liés à

* Quelle commande exécuter chaque fois qu'un fichier change, dans notre cas `npm run dev`
* Quels dossiers et fichiers observer
* Et quels fichiers ignorer

Plus d'informations sur la configuration de nodemon [ici](https://github.com/remy/nodemon#config-files).

Maintenant que nous avons notre observateur de fichiers, vous pouvez maintenant simplement exécuter `npm run watch:dev`, coder et enregistrer votre fichier. Et chaque fois que vous allez sur `localhost:3000`, vous verrez les changements. Essayez-le !

### Bonus : Ajoutez des tests !

Pour ajouter des tests à notre projet, installez simplement [Jest](https://www.npmjs.com/package/jest) depuis npm, ajoutez quelques configurations et ajoutez un script appelé `test` dans notre package.json

`npm i -D jest`

Ajoutez un objet appelé "jest", et un script de test dans votre package.json

```
// package.json
...
"jest": { 
  "testEnvironment": "node"
},
"scripts": {
  // ..other scripts 
  "test": "jest"
}
```

Essayez-le, créez un fichier sample.test.js, écrivez n'importe quels tests et exécutez le script !

`npm run test`

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-2.png)
_Capture d'écran d'exemple de l'exécution de npm run test._

### TL;DR

Voici les étapes simplifiées pour activer ES6 dans Node.js. J'inclurai également le dépôt afin que vous puissiez copier et inspecter le code complet.

* Créez un nouveau projet en utilisant la commande terminal `express your-project-name`.
* Déplacez `bin/`, `routes/` et `app` dans un nouveau dossier appelé `src/`, et convertissez le code en ES6. N'oubliez pas non plus de renommer `bin/www` en `[www.js](http://www.js)`
* Installez toutes les dépendances et devDependencies

```
npm i npm-run-all @babel/cli @babel/core @babel/preset-env nodemon rimraf --save
npm i -D jest
```

* Ajoutez ces scripts à votre package.json

```js
"scripts": { 
  "start": "npm run prod", 
  "build": "npm-run-all clean transpile", 
  "server": "node ./dist-server/bin/www", 
  "dev": "NODE_ENV=development npm-run-all build server", 
  "prod": "NODE_ENV=production npm-run-all build server", 
  "transpile": "babel ./server --out-dir dist-server", 
  "clean": "rimraf dist-server", 
  "watch:dev": "nodemon", 
  "test": "jest" 
}
```

* Mettez les configurations pour babel, nodemon et jest dans votre package.json

```js
"nodemonConfig": {
  "exec": "npm run dev",
  "watch": [ "server/*", "public/*" ],
  "ignore": [ "**/__tests__/**", "*.test.js", "*.spec.js" ] 
}, 
"babel": { 
  "presets": [ "@babel/preset-env" ]
},
"jest": {
  "testEnvironment": "node"
},
```

* Testez vos scripts en exécutant `npm run your-script-here`
* Vous verrez le [dépôt complet sur mon github](https://github.com/jcunanan05/express-es6-sample/tree/master)

### Notes et avertissements

Notez que cette configuration peut ne pas être idéale pour toutes les situations, en particulier pour les grands projets. (comme 1k fichiers de code). L'étape de transpilation et de suppression peut ralentir votre environnement de développement. De plus, les modules ES arrivent presque dans Node. Mais, néanmoins, c'est un bon matériel éducatif pour comprendre comment la transpilation fonctionne sous le capot comme lorsque nous développons des applications front-end :)

### Conclusion

Très bien ! J'espère que vous avez beaucoup appris. Merci d'avoir lu jusqu'ici.

Bon codage !

[Voir le dépôt complet ici.](https://github.com/jcunanan05/express-es6-sample/tree/master)

Cet article est publié dans freeCodecamp news.

[? Twitter](https://twitter.com/devJonathanC_) - [? freeCodeCamp](https://www.freecodecamp.org/jcunanan05) - [? Portfolio](https://jonathancunanan.com) - [⚒️ Github](https://github.com/jcunanan05)