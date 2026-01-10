---
title: 'Exiger des modules dans Node.js : Tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-19T18:48:49.000Z'
originalURL: https://freecodecamp.org/news/requiring-modules-in-node-js-everything-you-need-to-know-e7fbd119be8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AL0-iuggGnBLSvSVvt0Xzw.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'Exiger des modules dans Node.js : Tout ce que vous devez savoir'
seo_desc: "By Samer Buna\n\nUpdate: This article is now part of my book “Node.js Beyond\
  \ The Basics”.  \nRead the updated version of this content and more about Node at\
  \ jscomplete.com/node-beyond-basics.\n\nNode uses two core modules for managing\
  \ module dependencies:..."
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « Node.js Beyond The Basics ». 
>   
> Lisez la version mise à jour de ce contenu et plus sur Node à [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/g/node-modules).

Node utilise deux modules principaux pour gérer les dépendances des modules :

* Le module `require`, qui semble être disponible dans la portée globale — pas besoin de `require('require')`.
* Le module `module`, qui semble également être disponible dans la portée globale — pas besoin de `require('module')`.

Vous pouvez considérer le module `require` comme la commande et le module `module` comme l'organisateur de tous les modules requis.

Exiger un module dans Node n'est pas un concept si compliqué.

```js
const config = require('/path/to/file');
```

L'objet principal exporté par le module `require` est une fonction (comme utilisé dans l'exemple ci-dessus). Lorsque Node invoque cette fonction `require()` avec un chemin de fichier local comme seul argument de la fonction, Node passe par la séquence suivante d'étapes :

* **Résolution** : Pour trouver le chemin absolu du fichier.
* **Chargement** : Pour déterminer le type du contenu du fichier.
* **Encapsulation** : Pour donner au fichier sa portée privée. C'est ce qui rend les objets `require` et `module` locaux à chaque fichier que nous exigeons.
* **Évaluation** : C'est ce que la VM fait finalement avec le code chargé.
* **Mise en cache** : Ainsi, lorsque nous exigeons à nouveau ce fichier, nous ne passons pas par toutes les étapes une autre fois.

Dans cet article, je vais tenter d'expliquer avec des exemples ces différentes étapes et comment elles affectent la manière dont nous écrivons des modules dans Node.

Laissez-moi d'abord créer un répertoire pour héberger tous les exemples en utilisant mon terminal :

```bash
mkdir ~/learn-node && cd ~/learn-node
```

Toutes les commandes dans le reste de cet article seront exécutées depuis `~/learn-node`.

#### Résolution d'un chemin local

Permettez-moi de vous présenter l'objet `module`. Vous pouvez le vérifier dans une simple session REPL :

```bash
~/learn-node $ node
> module
Module {
  id: '<repl>',
  exports: {},
  parent: undefined,
  filename: null,
  loaded: false,
  children: [],
  paths: [ ... ] }
```

Chaque objet module obtient une propriété `id` pour l'identifier. Cet `id` est généralement le chemin complet vers le fichier, mais dans une session REPL, c'est simplement `<repl>`.

Les modules Node ont une relation un-à-un avec les fichiers sur le système de fichiers. Nous exigeons un module en chargeant le contenu d'un fichier en mémoire.

Cependant, puisque Node permet de nombreuses façons d'exiger un fichier (par exemple, avec un chemin relatif ou un chemin préconfiguré), avant de pouvoir charger le contenu d'un fichier en mémoire, nous devons trouver l'emplacement absolu de ce fichier.

Lorsque nous exigeons un module `'find-me'`, sans spécifier de chemin :

```js
require('find-me');
```

Node recherchera `find-me.js` dans tous les chemins spécifiés par `module.paths` — dans l'ordre.

```bash
~/learn-node $ node
> module.paths
[ '/Users/samer/learn-node/repl/node_modules',
  '/Users/samer/learn-node/node_modules',
  '/Users/samer/node_modules',
  '/Users/node_modules',
  '/node_modules',
  '/Users/samer/.node_modules',
  '/Users/samer/.node_libraries',
  '/usr/local/Cellar/node/7.7.1/lib/node' ]
```

La liste des chemins est essentiellement une liste de répertoires node_modules sous chaque répertoire du répertoire courant au répertoire racine. Elle inclut également quelques répertoires hérités dont l'utilisation n'est pas recommandée.

Si Node ne peut pas trouver `find-me.js` dans l'un de ces chemins, il lancera une erreur « cannot find module ».

```bash
~/learn-node $ node
> require('find-me')
Error: Cannot find module 'find-me'
    at Function.Module._resolveFilename (module.js:470:15)
    at Function.Module._load (module.js:418:25)
    at Module.require (module.js:498:17)
    at require (internal/module.js:20:19)
    at repl:1:1
    at ContextifyScript.Script.runInThisContext (vm.js:23:33)
    at REPLServer.defaultEval (repl.js:336:29)
    at bound (domain.js:280:14)
    at REPLServer.runBound [as eval] (domain.js:293:12)
    at REPLServer.onLine (repl.js:533:10)
```

Si vous créez maintenant un répertoire local `node_modules` et placez un `find-me.js` dedans, la ligne `require('find-me')` le trouvera.

```bash
~/learn-node $ mkdir node_modules 

~/learn-node $ echo "console.log('I am not lost');" > node_modules/find-me.js

~/learn-node $ node
> require('find-me');
I am not lost
{}
>
```

Si un autre fichier `find-me.js` existait dans l'un des autres chemins, par exemple, si nous avons un répertoire `node_modules` sous le répertoire personnel et que nous avons un fichier `find-me.js` différent dedans :

```bash
$ mkdir ~/node_modules
$ echo "console.log('I am the root of all problems');" > ~/node_modules/find-me.js
```

Lorsque nous `require('find-me')` depuis le répertoire `learn-node` — qui a son propre `node_modules/find-me.js`, le fichier `find-me.js` sous le répertoire personnel ne sera pas chargé du tout :

```bash
~/learn-node $ node
> require('find-me')
I am not lost
{}
>
```

Si nous supprimons le répertoire local `node_modules` sous `~/learn-node` et essayons de `require('find-me')` une fois de plus, le fichier sous le répertoire `node_modules` du répertoire personnel serait utilisé :

```bash
~/learn-node $ rm -r node_modules/
~/learn-node $ node
> require('find-me')
I am the root of all problems
{}
>
```

#### Exiger un dossier

Les modules n'ont pas besoin d'être des fichiers. Nous pouvons également créer un dossier `find-me` sous `node_modules` et y placer un fichier `index.js`. La même ligne `require('find-me')` utilisera le fichier `index.js` de ce dossier :

```bash
~/learn-node $ mkdir -p node_modules/find-me

~/learn-node $ echo "console.log('Found again.');" > node_modules/find-me/index.js

~/learn-node $ node
> require('find-me');
Found again.
{}
>
```

Notez comment il a ignoré le chemin `node_modules` du répertoire personnel à nouveau puisque nous avons un chemin local maintenant.

Un fichier `index.js` sera utilisé par défaut lorsque nous exigeons un dossier, mais nous pouvons contrôler quel nom de fichier utiliser au début sous le dossier en utilisant la propriété `main` dans `package.json`. Par exemple, pour faire en sorte que la ligne `require('find-me')` se résolve vers un fichier différent sous le dossier `find-me`, tout ce que nous avons à faire est d'ajouter un fichier `package.json` dedans et de spécifier quel fichier doit être utilisé pour résoudre ce dossier :

```bash
~/learn-node $ echo "console.log('I rule');" > node_modules/find-me/start.js

~/learn-node $ echo '{ "name": "find-me-folder", "main": "start.js" }' > node_modules/find-me/package.json

~/learn-node $ node
> require('find-me');
I rule
{}
>
```

#### require.resolve

Si vous voulez uniquement résoudre le module et ne pas l'exécuter, vous pouvez utiliser la fonction `require.resolve`. Cela se comporte exactement de la même manière que la fonction principale `require`, mais ne charge pas le fichier. Elle lancera toujours une erreur si le fichier n'existe pas et retournera le chemin complet vers le fichier lorsqu'il est trouvé.

```bash
> require.resolve('find-me');
'/Users/samer/learn-node/node_modules/find-me/start.js'
> require.resolve('not-there');
Error: Cannot find module 'not-there'
    at Function.Module._resolveFilename (module.js:470:15)
    at Function.resolve (internal/module.js:27:19)
    at repl:1:9
    at ContextifyScript.Script.runInThisContext (vm.js:23:33)
    at REPLServer.defaultEval (repl.js:336:29)
    at bound (domain.js:280:14)
    at REPLServer.runBound [as eval] (domain.js:293:12)
    at REPLServer.onLine (repl.js:533:10)
    at emitOne (events.js:101:20)
    at REPLServer.emit (events.js:191:7)
>
```

Cela peut être utilisé, par exemple, pour vérifier si un package optionnel est installé ou non et ne l'utiliser que lorsqu'il est disponible.

#### Chemins relatifs et absolus

Outre la résolution des modules depuis les répertoires `node_modules`, nous pouvons également placer le module n'importe où et l'exiger avec des chemins relatifs (`./` et `../`) ou avec des chemins absolus commençant par `/`.

Si, par exemple, le fichier `find-me.js` était sous un dossier `lib` au lieu du dossier `node_modules`, nous pouvons l'exiger avec :

```js
require('./lib/find-me');
```

#### Relation parent-enfant entre les fichiers

Créez un fichier `lib/util.js` et ajoutez une ligne `console.log` pour l'identifier. De plus, `console.log` l'objet `module` lui-même :

```bash
~/learn-node $ mkdir lib
~/learn-node $ echo "console.log('In util', module);" > lib/util.js
```

Faites de même pour un fichier `index.js`, qui est ce que nous allons exécuter avec la commande node. Faites en sorte que ce fichier `index.js` exige `lib/util.js` :

```bash
~/learn-node $ echo "console.log('In index', module); require('./lib/util');" > index.js
```

Exécutez maintenant le fichier `index.js` avec node :

```bash
~/learn-node $ node index.js
In index Module {
  id: '.',
  exports: {},
  parent: null,
  filename: '/Users/samer/learn-node/index.js',
  loaded: false,
  children: [],
  paths: [ ... ] }
In util Module {
  id: '/Users/samer/learn-node/lib/util.js',
  exports: {},
  parent:
   Module {
     id: '.',
     exports: {},
     parent: null,
     filename: '/Users/samer/learn-node/index.js',
     loaded: false,
     children: [ [Circular] ],
     paths: [...] },
  filename: '/Users/samer/learn-node/lib/util.js',
  loaded: false,
  children: [],
  paths: [...] }
```

Notez comment le module principal `index` `(id: '.')` est maintenant listé comme parent pour le module `lib/util`. Cependant, le module `lib/util` n'a pas été listé comme enfant du module `index`. Au lieu de cela, nous avons la valeur `[Circular]` car il s'agit d'une référence circulaire. Si Node imprime l'objet module `lib/util`, il entrera dans une boucle infinie. C'est pourquoi il remplace simplement la référence `lib/util` par `[Circular]`.

Plus important encore, que se passe-t-il si le module `lib/util` exige le module principal `index` ? C'est là que nous entrons dans ce qu'on appelle la dépendance modulaire circulaire, qui est autorisée dans Node.

Pour mieux comprendre, comprenons d'abord quelques autres concepts sur l'objet module.

#### exports, module.exports, et chargement synchrone des modules

Dans n'importe quel module, exports est un objet spécial. Si vous l'avez remarqué ci-dessus, chaque fois que nous avons imprimé un objet module, il avait une propriété exports qui a été un objet vide jusqu'à présent. Nous pouvons ajouter n'importe quel attribut à cet objet exports spécial. Par exemple, exportons un attribut id pour `index.js` et `lib/util.js` :

```js
// Ajoutez la ligne suivante en haut de lib/util.js
exports.id = 'lib/util';

// Ajoutez la ligne suivante en haut de index.js
exports.id = 'index';
```

Lorsque nous exécutons maintenant `index.js`, nous verrons ces attributs comme gérés sur l'objet `module` de chaque fichier :

```bash
~/learn-node $ node index.js
In index Module {
  id: '.',
  exports: { id: 'index' },
  loaded: false,
  ... }
In util Module {
  id: '/Users/samer/learn-node/lib/util.js',
  exports: { id: 'lib/util' },
  parent:
   Module {
     id: '.',
     exports: { id: 'index' },
     loaded: false,
     ... },
  loaded: false,
  ... }
```

J'ai supprimé certains attributs dans la sortie ci-dessus pour la garder brève, mais notez comment l'objet `exports` a maintenant les attributs que nous avons définis dans chaque module. Vous pouvez mettre autant d'attributs que vous voulez sur cet objet exports, et vous pouvez même changer l'objet entier pour qu'il soit autre chose. Par exemple, pour changer l'objet exports pour qu'il soit une fonction au lieu d'un objet, nous faisons ce qui suit :

```js
// Ajoutez la ligne suivante dans index.js avant le console.log

module.exports = function() {};
```

Lorsque vous exécutez `index.js` maintenant, vous verrez comment l'objet `exports` est une fonction :

```bash
~/learn-node $ node index.js
In index Module {
  id: '.',
  exports: [Function],
  loaded: false,
  ... }
```

Notez comment nous n'avons pas fait `exports = function() {}` pour faire de l'objet `exports` une fonction. Nous ne pouvons pas vraiment faire cela parce que la variable `exports` à l'intérieur de chaque module est juste une référence à `module.exports` qui gère les propriétés exportées. Lorsque nous réassignons la variable `exports`, cette référence est perdue et nous introduirons une nouvelle variable au lieu de changer l'objet `module.exports`.

L'objet `module.exports` dans chaque module est ce que la fonction `require` retourne lorsque nous exigeons ce module. Par exemple, changez la ligne `require('./lib/util')` dans `index.js` en :

```js
const UTIL = require('./lib/util');

console.log('UTIL:', UTIL);
```

Ce qui précède capturera les propriétés exportées dans `lib/util` dans la constante `UTIL`. Lorsque nous exécutons `index.js` maintenant, la toute dernière ligne produira :

```bash
UTIL: { id: 'lib/util' }
```

Parlons également de l'attribut `loaded` sur chaque module. Jusqu'à présent, chaque fois que nous avons imprimé un objet module, nous avons vu un attribut `loaded` sur cet objet avec une valeur de `false`.

Le module `module` utilise l'attribut `loaded` pour suivre quels modules ont été chargés (valeur vraie) et quels modules sont encore en cours de chargement (valeur fausse). Nous pouvons, par exemple, voir le module `index.js` entièrement chargé si nous imprimons son objet `module` au prochain cycle de la boucle d'événements en utilisant un appel `setImmediate` :

```
// Dans index.js
setImmediate(() => {
  console.log('The index.js module object is now loaded!', module)
});
```

La sortie de cela serait :

```bash
The index.js module object is now loaded! Module {
  id: '.',
  exports: [Function],
  parent: null,
  filename: '/Users/samer/learn-node/index.js',
  loaded: true,
  children:
   [ Module {
       id: '/Users/samer/learn-node/lib/util.js',
       exports: [Object],
       parent: [Circular],
       filename: '/Users/samer/learn-node/lib/util.js',
       loaded: true,
       children: [],
       paths: [Object] } ],
  paths:
   [ '/Users/samer/learn-node/node_modules',
     '/Users/samer/node_modules',
     '/Users/node_modules',
     '/node_modules' ] }
```

Notez comment dans cette sortie `console.log` retardée, à la fois `lib/util.js` et `index.js` sont entièrement chargés.

L'objet `exports` devient complet lorsque Node finit de charger le module (et le marque ainsi). Le processus entier d'exigence/chargement d'un module est _synchrone_. C'est pourquoi nous avons pu voir les modules entièrement chargés après un cycle de la boucle d'événements.

Cela signifie également que nous ne pouvons pas changer l'objet `exports` de manière asynchrone. Nous ne pouvons pas, par exemple, faire ce qui suit dans n'importe quel module :

```js
fs.readFile('/etc/passwd', (err, data) => {
  if (err) throw err;
  
  exports.data = data; // Ne fonctionnera pas.
});
```

#### Dépendance circulaire des modules

Essayons maintenant de répondre à la question importante sur la dépendance circulaire dans Node : Que se passe-t-il lorsque le module 1 exige le module 2, et que le module 2 exige le module 1 ?

Pour le découvrir, créons les deux fichiers suivants sous `lib/`, `module1.js` et `module2.js` et faisons en sorte qu'ils s'exigent mutuellement :

```js
// lib/module1.js

exports.a = 1;

require('./module2');

exports.b = 2;
exports.c = 3;

// lib/module2.js

const Module1 = require('./module1');
console.log('Module1 is partially loaded here', Module1);
```

Lorsque nous exécutons `module1.js`, nous voyons ce qui suit :

```bash
~/learn-node $ node lib/module1.js
Module1 is partially loaded here { a: 1 }
```

Nous avons exigé `module2` avant que `module1` ne soit entièrement chargé, et puisque `module2` a exigé `module1` alors qu'il n'était pas entièrement chargé, ce que nous obtenons de l'objet `exports` à ce moment-là sont toutes les propriétés exportées avant la dépendance circulaire. Seule la propriété `a` a été signalée parce que `b` et `c` ont été exportées après que `module2` a exigé et imprimé `module1`.

Node garde cela vraiment simple. Pendant le chargement d'un module, il construit l'objet `exports`. Vous pouvez exiger le module avant qu'il ne soit entièrement chargé et vous obtiendrez simplement un objet exports partiel avec ce qui a été défini jusqu'à présent.

#### JSON et addons C/C++

Nous pouvons exiger nativement des fichiers JSON et des fichiers d'addons C++ avec la fonction require. Vous n'avez même pas besoin de spécifier une extension de fichier pour le faire.

Si une extension de fichier n'a pas été spécifiée, la première chose que Node essaiera de résoudre est un fichier `.js`. Si Node ne peut pas trouver un fichier `.js`, il essaiera un fichier `.json` et analysera le fichier `.json` s'il est trouvé comme un fichier texte JSON. Après cela, il essaiera de trouver un fichier binaire `.node`. Cependant, pour éviter toute ambiguïté, vous devriez probablement spécifier une extension de fichier lorsque vous exigez autre chose que des fichiers `.js`.

Exiger des fichiers JSON est utile si, par exemple, tout ce que vous devez gérer dans ce fichier est quelques valeurs de configuration statiques, ou quelques valeurs que vous lisez périodiquement depuis une source externe. Par exemple, si nous avions le fichier `config.json` suivant :

```json
{
  "host": "localhost",
  "port": 8080
}
```

Nous pouvons l'exiger directement comme ceci :

```
const { host, port } = require('./config');

console.log(`Server will run at http://${host}:${port}`);
```

L'exécution du code ci-dessus donnera cette sortie :

```bash
Server will run at http://localhost:8080
```

Si Node ne peut pas trouver un fichier `.js` ou `.json`, il recherchera un fichier `.node` et l'interprétera comme un module d'addon compilé.

Le site de documentation de Node contient un [fichier d'addon exemple](https://nodejs.org/api/addons.html#addons_hello_world) qui est écrit en C++. C'est un module simple qui expose une fonction `hello()` et la fonction hello produit « world ».

Vous pouvez utiliser le package `node-gyp` pour compiler et construire le fichier `.cc` en un fichier `.node`. Vous devez simplement configurer un fichier [binding.gyp](https://nodejs.org/api/addons.html#addons_building) pour dire à `node-gyp` quoi faire.

Une fois que vous avez le fichier `addon.node` (ou tout autre nom que vous spécifiez dans `binding.gyp`), vous pouvez alors l'exiger nativement comme n'importe quel autre module :

```js
const addon = require('./addon');

console.log(addon.hello());
```

Nous pouvons en fait voir le support des trois extensions en regardant `require.extensions`.

![Image](https://cdn-media-1.freecodecamp.org/images/D3NuN7cetXAjYpHfqBGribFo-ex0fj-AvuDA)

En regardant les fonctions pour chaque extension, vous pouvez clairement voir ce que Node fera avec chacune. Il utilise `module._compile` pour les fichiers `.js`, `JSON.parse` pour les fichiers `.json`, et `process.dlopen` pour les fichiers `.node`.

#### Tout le code que vous écrivez dans Node sera encapsulé dans des fonctions

L'encapsulation des modules de Node est souvent mal comprise. Pour la comprendre, laissez-moi vous rappeler la relation `exports`/`module.exports`.

Nous pouvons utiliser l'objet `exports` pour exporter des propriétés, mais nous ne pouvons pas remplacer directement l'objet `exports` parce qu'il est juste une référence à `module.exports`.

```js
exports.id = 42; // C'est correct.

exports = { id: 42 }; // Cela ne fonctionnera pas.

module.exports = { id: 42 }; // C'est correct.
```

Comment exactement cet objet `exports`, qui semble être global pour chaque module, est-il défini comme une référence sur l'objet `module` ?

Laissez-moi poser une question de plus avant d'expliquer le processus d'encapsulation de Node.

Dans un navigateur, lorsque nous déclarons une variable dans un script comme ceci :

```
var answer = 42;
```

Cette variable `answer` sera disponible globalement dans tous les scripts après le script qui l'a définie.

Ce n'est pas le cas dans Node. Lorsque nous définissons une variable dans un module, les autres modules du programme n'auront pas accès à cette variable. Alors, comment se fait-il que les variables dans Node soient magiquement limitées en portée ?

La réponse est simple. Avant de compiler un module, Node encapsule le code du module dans une fonction, que nous pouvons inspecter en utilisant la propriété `wrapper` du module `module`.

```bash
~ $ node
> require('module').wrapper
[ '(function (exports, require, module, __filename, __dirname) { ',
  '\n});' ]
>
```

Node n'exécute aucun code que vous écrivez dans un fichier directement. Il exécute cette fonction d'encapsulation qui contiendra votre code dans son corps. C'est ce qui maintient les variables de niveau supérieur définies dans un module limitées à ce module.

Cette fonction d'encapsulation a 5 arguments : `exports`, `require`, `module`, `__filename`, et `__dirname`. C'est ce qui les fait paraître globaux alors qu'en fait ils sont spécifiques à chaque module.

Tous ces arguments obtiennent leurs valeurs lorsque Node exécute la fonction d'encapsulation. `exports` est défini comme une référence à `module.exports` avant cela. `require` et `module` sont tous deux spécifiques à la fonction à exécuter, et les variables `__filename`/`__dirname` contiendront le nom de fichier absolu et le chemin du répertoire du module encapsulé.

Vous pouvez voir cette encapsulation en action si vous exécutez un script avec un problème sur sa première ligne :

```bash
~/learn-node $ echo "euaohseu" > bad.js

~/learn-node $ node bad.js
~/bad.js:1
(function (exports, require, module, __filename, __dirname) { euaohseu
                                                              ^
ReferenceError: euaohseu is not defined
```

Notez comment la première ligne du script telle que rapportée ci-dessus était la fonction d'encapsulation, et non la mauvaise référence.

De plus, puisque chaque module est encapsulé dans une fonction, nous pouvons en fait accéder aux arguments de cette fonction avec le mot-clé `arguments` :

```bash
~/learn-node $ echo "console.log(arguments)" > index.js

~/learn-node $ node index.js
{ '0': {},
  '1':
   { [Function: require]
     resolve: [Function: resolve],
     main:
      Module {
        id: '.',
        exports: {},
        parent: null,
        filename: '/Users/samer/index.js',
        loaded: false,
        children: [],
        paths: [Object] },
     extensions: { ... },
     cache: { '/Users/samer/index.js': [Object] } },
  '2':
   Module {
     id: '.',
     exports: {},
     parent: null,
     filename: '/Users/samer/index.js',
     loaded: false,
     children: [],
     paths: [ ... ] },
  '3': '/Users/samer/index.js',
  '4': '/Users/samer' }
```

Le premier argument est l'objet `exports`, qui commence vide. Ensuite, nous avons les objets `require`/`module`, tous deux étant des instances associées au fichier `index.js` que nous exécutons. Ils ne sont pas des variables globales. Les deux derniers arguments sont le chemin du fichier et son chemin de répertoire.

La valeur de retour de la fonction d'encapsulation est `module.exports`. À l'intérieur de la fonction encapsulée, nous pouvons utiliser l'objet `exports` pour changer les propriétés de `module.exports`, mais nous ne pouvons pas réassigner exports lui-même parce qu'il est juste une référence.

Ce qui se passe est à peu près équivalent à :

```js
function (require, module, __filename, __dirname) {
  let exports = module.exports;
  
  // Votre Code...
  
  return module.exports;
}
```

Si nous changeons tout l'objet `exports`, il ne sera plus une référence à `module.exports`. C'est ainsi que fonctionnent les objets de référence JavaScript partout, pas seulement dans ce contexte.

#### L'objet require

Il n'y a rien de spécial à propos de `require`. C'est un objet qui agit principalement comme une fonction qui prend un nom ou un chemin de module et retourne l'objet `module.exports`. Nous pouvons simplement remplacer l'objet `require` par notre propre logique si nous le souhaitons.

Par exemple, peut-être pour des raisons de test, nous voulons que chaque appel à `require` soit simulé par défaut et retourne simplement un faux objet au lieu de l'objet exports du module requis. Cette simple réassignation de require fera l'affaire :

```js
require = function() {

  return { mocked: true };
  
}
```

Après avoir fait la réassignation ci-dessus de `require`, chaque appel à `require('something')` dans le script retournera simplement l'objet simulé.

L'objet require a également ses propres propriétés. Nous avons vu la propriété `resolve`, qui est une fonction qui effectue uniquement l'étape de résolution du processus require. Nous avons également vu `require.extensions` ci-dessus.

Il y a aussi `require.main` qui peut être utile pour déterminer si le script est en train d'être requis ou exécuté directement.

Supposons, par exemple, que nous avons cette simple fonction `printInFrame` dans `print-in-frame.js` :

```js
// Dans print-in-frame.js

const printInFrame = (size, header) => {
  console.log('*'.repeat(size));
  console.log(header);
  console.log('*'.repeat(size));
};
```

La fonction prend un argument numérique `size` et un argument de chaîne `header` et imprime ce header dans un cadre d'étoiles contrôlé par la taille que nous spécifions.

Nous voulons utiliser ce fichier de deux manières :

1. Directement depuis la ligne de commande comme ceci :

```bash
~/learn-node $ node print-in-frame 8 Hello
```

En passant 8 et Hello comme arguments de ligne de commande pour imprimer « Hello » dans un cadre de 8 étoiles.

2. Avec `require`. En supposant que le module requis exportera la fonction `printInFrame` et que nous pourrons simplement l'appeler :

```
const print = require('./print-in-frame');

print(5, 'Hey');
```

Pour imprimer le header « Hey » dans un cadre de 5 étoiles.

Ce sont deux utilisations différentes. Nous avons besoin d'un moyen de déterminer si le fichier est exécuté en tant que script autonome ou s'il est requis par d'autres scripts.

C'est là que nous pouvons utiliser cette simple instruction if :

```js
if (require.main === module) {
  // Le fichier est exécuté directement (pas avec require)
}
```

Nous pouvons donc utiliser cette condition pour satisfaire les exigences d'utilisation ci-dessus en invoquant la fonction printInFrame différemment :

```js
// Dans print-in-frame.js

const printInFrame = (size, header) => {
  console.log('*'.repeat(size));
  console.log(header);
  console.log('*'.repeat(size));
};

if (require.main === module) {
  printInFrame(process.argv[2], process.argv[3]);
} else {
  module.exports = printInFrame;
}
```

Lorsque le fichier n'est pas requis, nous appelons simplement la fonction `printInFrame` avec les éléments `process.argv`. Sinon, nous changeons simplement l'objet `module.exports` pour qu'il soit la fonction `printInFrame` elle-même.

#### Tous les modules seront mis en cache

La mise en cache est importante à comprendre. Laissez-moi utiliser un exemple simple pour la démontrer.

Supposons que vous avez le fichier `ascii-art.js` suivant qui imprime un en-tête cool :

![Image](https://cdn-media-1.freecodecamp.org/images/RbgFBaBdZszHFKEcmsyE8mMW7udDG4NdYofy)

Nous voulons afficher cet en-tête chaque fois que nous _exigeons_ le fichier. Donc lorsque nous exigeons le fichier deux fois, nous voulons que l'en-tête s'affiche deux fois.

```js
require('./ascii-art') // affichera l'en-tête.
require('./ascii-art') // n'affichera pas l'en-tête.
```

Le second require n'affichera pas l'en-tête à cause de la mise en cache des modules. Node met en cache le premier appel et ne charge pas le fichier lors du second appel.

Nous pouvons voir ce cache en imprimant `require.cache` après le premier require. Le registre de cache est simplement un objet qui a une propriété pour chaque module requis. Les valeurs de ces propriétés sont les objets `module` utilisés pour chaque module. Nous pouvons simplement supprimer une propriété de cet objet `require.cache` pour invalider ce cache. Si nous faisons cela, Node rechargera le module pour le mettre à nouveau en cache.

Cependant, ce n'est pas la solution la plus efficace pour ce cas. La solution simple est d'encapsuler la ligne de log dans `ascii-art.js` avec une fonction et d'exporter cette fonction. De cette manière, lorsque nous exigeons le fichier `ascii-art.js`, nous obtenons une fonction que nous pouvons exécuter pour invoquer la ligne de log à chaque fois :

```js
require('./ascii-art')() // affichera l'en-tête.
require('./ascii-art')() // affichera également l'en-tête.
```

C'est tout ce que j'ai sur ce sujet. Merci d'avoir lu. À la prochaine !

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)