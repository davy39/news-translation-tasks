---
title: Le guide définitif de Node.js – Apprendre Node pour les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-09-06T16:03:06.000Z'
originalURL: https://freecodecamp.org/news/the-definitive-node-js-handbook-6912378afc6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7F50Qc-ysFgy6tCjUyruTA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Le guide définitif de Node.js – Apprendre Node pour les débutants
seo_desc: 'Note: you can get a PDF, ePub, or Mobi version of this handbook for easier
  reference, or for reading on your Kindle or tablet.

  Introduction to Node.js

  This handbook is a getting started guide to Node.js, the server-side JavaScript
  runtime environment...'
---

Note : vous pouvez obtenir une version [PDF, ePub ou Mobi](https://flaviocopes.com/page/node-handbook/) de ce guide pour une référence plus facile, ou pour le lire sur votre Kindle ou tablette.

### Introduction à Node.js

Ce guide est un guide de démarrage pour Node.js, l'environnement d'exécution JavaScript côté serveur.

#### Aperçu

Node.js est un **environnement d'exécution pour JavaScript** qui s'exécute sur le **serveur**.

Node.js est open source, multiplateforme, et depuis son introduction en 2009, il est devenu extrêmement populaire et joue désormais un rôle significatif dans le paysage du développement web. Si les étoiles GitHub sont un facteur d'indication de popularité, avoir plus de 58 000 étoiles signifie être très populaire.

Node.js exécute le moteur JavaScript V8, le cœur de Google Chrome, en dehors du navigateur. Node.js est capable de tirer parti du travail des ingénieurs qui ont rendu (et continueront de rendre) le runtime JavaScript de Chrome extrêmement rapide, et cela permet à Node.js de bénéficier des énormes améliorations de performance et de la compilation Just-In-Time que V8 effectue. Grâce à cela, le code JavaScript s'exécutant dans Node.js peut devenir très performant.

Une application Node.js est exécutée par un seul processus, sans créer de nouveau thread pour chaque requête. Node fournit un ensemble de primitives d'E/S asynchrones dans sa bibliothèque standard qui empêcheront le code JavaScript de bloquer et généralement, les bibliothèques dans Node.js sont écrites en utilisant des paradigmes non bloquants, rendant un comportement bloquant une exception plutôt que la norme.

Lorsque Node.js doit effectuer une opération d'E/S, comme la lecture depuis le réseau, l'accès à une base de données ou au système de fichiers, au lieu de bloquer le thread, Node.js reprendra les opérations lorsque la réponse reviendra, au lieu de gaspiller des cycles CPU en attendant.

Cela permet à Node.js de gérer des milliers de connexions simultanées avec un seul serveur sans introduire la charge de gestion de la concurrence des threads, qui serait une source majeure de bugs.

Node.js a un avantage unique car des millions de développeurs frontend qui écrivent du JavaScript pour le navigateur sont désormais capables d'exécuter le code côté serveur et le code côté frontend sans avoir besoin d'apprendre un langage complètement différent.

Dans Node.js, les nouvelles normes ECMAScript peuvent être utilisées sans problème, car vous n'avez pas à attendre que tous vos utilisateurs mettent à jour leurs navigateurs — vous êtes responsable de la décision de la version ECMAScript à utiliser en changeant la version de Node.js, et vous pouvez également activer des fonctionnalités expérimentales spécifiques en exécutant Node avec des flags.

#### Il dispose d'un grand nombre de bibliothèques

Avec sa structure simple, le gestionnaire de paquets node ([npm](https://flaviocopes.com/npm/)) a aidé l'écosystème de Node.js à proliférer. Maintenant, le [registre npm](https://www.npmjs.com/) héberge près de 500 000 paquets open source que vous pouvez utiliser librement.

### Une application Node.js exemple

L'exemple le plus courant de Hello World de Node.js est un serveur web :

```js
const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World\n')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})
```

Pour exécuter ce snippet, enregistrez-le sous le nom `server.js` et exécutez `node server.js` dans votre terminal.

Ce code inclut d'abord le module `http` de Node.js.

Node.js dispose d'une bibliothèque standard [standard library](https://nodejs.org/api/) impressionnante, incluant un support de première classe pour le réseau.

La méthode `createServer()` de `http` crée un nouveau serveur HTTP et le retourne.

Le serveur est configuré pour écouter sur le port et le nom d'hôte spécifiés. Lorsque le serveur est prêt, la fonction de rappel est appelée, nous informant dans ce cas que le serveur est en cours d'exécution.

Chaque fois qu'une nouvelle requête est reçue, l'événement `request` est appelé, fournissant deux objets : une requête (un objet `[http.IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage)`) et une réponse (un objet `[http.ServerResponse](https://nodejs.org/api/http.html#http_class_http_serverresponse)`).

Ces deux objets sont essentiels pour gérer l'appel HTTP.

Le premier fournit les détails de la requête. Dans cet exemple simple, cela n'est pas utilisé, mais vous pourriez accéder aux en-têtes de la requête et aux données de la requête.

Le second est utilisé pour retourner des données à l'appelant.

Dans ce cas avec :

```js
res.statusCode = 200
```

Nous définissons la propriété `statusCode` à `200`, pour indiquer une réponse réussie.

Nous définissons l'en-tête Content-Type :

```js
res.setHeader('Content-Type', 'text/plain')
```

...et nous terminons la réponse, en ajoutant le contenu comme argument à `end()` :

```js
res.end('Hello World\n')
```

### Frameworks et outils Node.js

Node.js est une plateforme de bas niveau. Pour faciliter et rendre les choses plus intéressantes pour les développeurs, des milliers de bibliothèques ont été construites sur Node.js.

Beaucoup de celles-ci se sont établies au fil du temps comme des options populaires. Voici une liste non exhaustive de celles que je considère très pertinentes et qui valent la peine d'être apprises :

* [**Express**](https://expressjs.com/)  
 L'une des façons les plus simples et puissantes de créer un serveur web. Son approche minimaliste et son focus non opinionné sur les fonctionnalités principales d'un serveur sont la clé de son succès.
* [**Meteor**](https://flaviocopes.com/meteor/)  
Un framework full-stack incroyablement puissant, vous permettant d'adopter une approche isomorphe pour construire des applications avec JavaScript et partager du code sur le client et le serveur. Autrefois un outil clé en main qui fournissait tout, il s'intègre désormais avec des bibliothèques front-end telles que [React](https://flaviocopes.com/react/), [Vue](https://flaviocopes.com/vue-introduction/) et [Angular](https://angularjs.org/). Meteor peut également être utilisé pour créer des applications mobiles.
* [**Koa**](http://koajs.com/)  
Créé par la même équipe derrière Express, Koa vise à être encore plus simple et plus petit, s'appuyant sur des années de connaissances. Le nouveau projet est né du besoin de créer des changements incompatibles sans perturber la communauté existante.
* [**Next.js**](https://flaviocopes.com/nextjs/)  
Il s'agit d'un framework pour rendre des applications [React](https://reactjs.org/) côté serveur.
* [**Micro**](https://github.com/zeit/micro)  
Il s'agit d'un serveur très léger pour créer des microservices HTTP asynchrones.
* [**Socket.io**](https://socket.io/)  
Il s'agit d'un moteur de communication en temps réel pour construire des applications réseau.

### Une brève histoire de Node.js

#### Un regard en arrière sur l'histoire de Node.js de 2009 à aujourd'hui

Cela peut sembler incroyable, mais Node.js n'a que 9 ans.

En comparaison, JavaScript a 23 ans et le web tel que nous le connaissons (après l'introduction de Mosaic) a 25 ans.

9 ans est une période très courte pour une technologie, mais Node.js semble avoir toujours été là.

J'ai eu le plaisir de travailler avec Node.js depuis ses débuts, lorsqu'il n'avait que 2 ans, et malgré le peu d'informations disponibles, on pouvait déjà sentir que c'était une énorme avancée.

Dans cette section, je veux dresser le tableau général de Node.js dans son histoire, pour mettre les choses en perspective.

#### Un peu d'histoire

JavaScript est un langage de programmation qui a été créé chez Netscape comme outil de script pour manipuler des pages web dans leur navigateur, [Netscape Navigator](https://en.wikipedia.org/wiki/Netscape_Navigator).

Une partie du modèle économique de Netscape était de vendre des serveurs Web, qui incluaient un environnement appelé « Netscape LiveWire », qui pouvait créer des pages dynamiques en utilisant JavaScript côté serveur. L'idée de JavaScript côté serveur n'a donc pas été introduite par Node.js, elle est aussi ancienne que JavaScript — mais à l'époque, elle n'a pas eu de succès.

Un facteur clé qui a conduit à l'essor de Node.js était le timing. Il y a quelques années, JavaScript commençait à être considéré comme un langage sérieux, grâce aux applications « Web 2.0 » qui ont montré au monde à quoi pouvait ressembler une expérience moderne sur le web (pensez à Google Maps ou GMail).

La performance des moteurs JavaScript a considérablement augmenté grâce à la bataille de la concurrence des navigateurs, qui est toujours aussi forte. Les équipes de développement derrière chaque navigateur majeur travaillent dur chaque jour pour nous offrir de meilleures performances, ce qui est une énorme victoire pour JavaScript en tant que plateforme. Chrome V8, le moteur que Node.js utilise sous le capot, est l'un d'entre eux et en particulier, c'est le moteur JavaScript de Chrome.

Mais bien sûr, Node.js n'est pas populaire juste par pure chance ou timing. Il a introduit beaucoup de nouvelles façons de penser sur la programmation en JavaScript sur le serveur.

#### 2009

* Node.js est né
* La première forme de [npm](https://flaviocopes.com/npm/) est créée

#### 2010

* [Express](https://flaviocopes.com/express/) est né
* [Socket.io](https://socket.io/) est né

#### 2011

* npm atteint la version 1.0
* De grandes entreprises commencent à adopter Node : [LinkedIn](https://www.linkedin.com), [Uber](https://www.uber.com)
* [Hapi](https://hapijs.com/) est né

#### 2012

* L'adoption continue très rapidement

#### 2013

* Première grande plateforme de blogging utilisant Node.js : [Ghost](https://ghost.org/)
* [Koa](https://koajs.com/) est né

#### 2014

* Grand drame : [IO.js](https://iojs.org/) est un fork majeur de Node.js, avec pour objectif d'introduire le support ES6 et d'avancer plus rapidement

#### 2015

* La [Node.js Foundation](https://foundation.nodejs.org/) est née
* IO.js est fusionné avec Node.js
* npm introduit les modules privés
* [Node 4](https://nodejs.org/en/blog/release/v4.0.0/) (aucune version 1, 2, 3 n'a été publiée auparavant)

#### 2016

* L'incident [leftpad](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)
* [Yarn](https://flaviocopes.com/yarn/) est né : Node 6

#### 2017

* npm se concentre davantage sur la sécurité : Node 8
* [HTTP/2](https://nodejs.org/api/http2.html)
* [V8](https://flaviocopes.com/v8/) introduit Node dans sa suite de tests, faisant officiellement de Node une cible pour le moteur JavaScript, en plus de Chrome
* 3 milliards de téléchargements npm chaque semaine

#### 2018

* Node 10
* [ES modules](https://flaviocopes.com/es-modules/) support expérimental .mjs

### Comment installer Node.js

#### Comment installer Node.js sur votre système : un gestionnaire de paquets, l'installateur du site officiel ou nvm

Node.js peut être installé de différentes manières. Cet article met en lumière les plus courantes et pratiques.

Des packages officiels pour toutes les principales plateformes sont disponibles [ici](https://nodejs.org/en/download/).

Une manière très pratique d'installer Node.js est via un gestionnaire de paquets. Dans ce cas, chaque système d'exploitation a le sien.

Sur macOS, [Homebrew](https://brew.sh/) est la norme de facto, et — une fois installé — permet d'installer Node.js très facilement, en exécutant cette commande dans le CLI :

```
brew install node
```

D'autres gestionnaires de paquets pour Linux et Windows sont listés [ici](https://nodejs.org/en/download/package-manager/).

[nvm](https://github.com/creationix/nvm/blob/master/README.md) est une manière populaire d'exécuter Node.js. Il vous permet de basculer facilement entre les versions de Node.js, et d'installer de nouvelles versions pour les essayer et de revenir en arrière facilement si quelque chose ne fonctionne pas, par exemple.

C'est également très utile pour tester votre code avec d'anciennes versions de Node.js.

Ma suggestion est d'utiliser l'installateur officiel si vous débutez et que vous n'utilisez pas déjà Homebrew. Sinon, Homebrew est ma solution préférée.

### Combien de JavaScript devez-vous connaître pour utiliser Node.js ?

Si vous débutez avec JavaScript, à quel point devez-vous maîtriser le langage ?

En tant que débutant, il est difficile d'atteindre un point où vous êtes suffisamment confiant en vos capacités de programmation.

En apprenant à coder, vous pourriez également être confus quant à la frontière entre JavaScript et Node.js, et vice versa.

Je vous recommande d'avoir une bonne compréhension des principaux concepts de JavaScript avant de plonger dans Node.js :

* Structure lexicale
* Expressions
* Types
* Variables
* Fonctions
* this
* Fonctions fléchées
* Boucles
* Boucles et portée
* Tableaux
* Littéraux de gabarit
* Points-virgules
* Mode strict
* ECMAScript 6, 2016, 2017

Avec ces concepts en tête, vous êtes bien parti pour devenir un développeur JavaScript compétent, à la fois dans le navigateur et dans Node.js.

Les concepts suivants sont également clés pour comprendre la programmation asynchrone, qui est une partie fondamentale de Node.js :

* Programmation asynchrone et callbacks
* Minuteries
* Promesses
* Async et Await
* Fermetures
* La boucle d'événements

Heureusement, j'ai écrit un ebook gratuit qui explique tous ces sujets, et il s'appelle [JavaScript Fundamentals](https://flaviocopes.com/javascript/). C'est la ressource la plus compacte que vous trouverez pour apprendre tout cela.

### Différences entre Node.js et le navigateur

Comment l'écriture d'applications JavaScript dans Node.js diffère de la programmation pour le Web dans le navigateur.

Le navigateur et Node utilisent tous deux JavaScript comme langage de programmation.

Construire des applications qui s'exécutent dans le navigateur est une chose complètement différente de la construction d'une application Node.js.

Malgré le fait qu'il s'agisse toujours de JavaScript, il existe quelques différences clés qui rendent l'expérience radicalement différente.

Un développeur frontend qui écrit des applications Node.js a un énorme avantage — le langage reste le même.

Vous avez une énorme opportunité car nous savons à quel point il est difficile d'apprendre pleinement et profondément un langage de programmation. En utilisant le même langage pour effectuer tout votre travail sur le web — à la fois sur le client et sur le serveur — vous êtes dans une position unique d'avantage.

Ce qui change, c'est l'écosystème.

Dans le navigateur, la plupart du temps, ce que vous faites est d'interagir avec le DOM, ou d'autres API de la plateforme Web comme les Cookies. Ceux-ci n'existent pas dans Node.js, bien sûr. Vous n'avez pas les objets `document`, `window` et tous les autres objets fournis par le navigateur.

Et dans le navigateur, nous n'avons pas toutes les belles API que Node.js fournit à travers ses modules, comme la fonctionnalité d'accès au système de fichiers.

Une autre grande différence est que dans Node.js, vous contrôlez l'environnement. Sauf si vous construisez une application open source que n'importe qui peut déployer n'importe où, vous savez quelle version de Node.js vous allez utiliser pour exécuter l'application. Comparé à l'environnement du navigateur, où vous n'avez pas le luxe de choisir quel navigateur vos visiteurs vont utiliser, c'est très pratique.

Cela signifie que vous pouvez écrire tout le JavaScript moderne ES6-7-8-9 que votre version de Node supporte.

Puisque JavaScript évolue si rapidement, mais que les navigateurs peuvent être un peu lents et les utilisateurs un peu lents à mettre à jour — parfois sur le web, vous êtes coincé avec des versions plus anciennes de JavaScript/ECMAScript.

Vous pouvez utiliser Babel pour transformer votre code pour qu'il soit compatible ES5 avant de l'envoyer au navigateur, mais dans Node.js, vous n'en aurez pas besoin.

Une autre différence est que Node.js utilise le système de modules [CommonJS](https://flaviocopes.com/commonjs/), tandis que dans le navigateur, nous commençons à voir la norme ES Modules être implémentée.

En pratique, cela signifie que pour l'instant, vous utilisez `require()` dans Node.js et `import` dans le navigateur.

### Le moteur JavaScript V8

V8 est le nom du moteur JavaScript qui alimente Google Chrome. C'est la chose qui prend notre JavaScript et l'exécute lors de la navigation avec Chrome.

V8 fournit l'environnement d'exécution dans lequel JavaScript s'exécute. Le DOM et les autres API de la plateforme Web sont fournis par le navigateur.

Le point intéressant est que le moteur JavaScript est indépendant du navigateur dans lequel il est hébergé. Cette caractéristique clé a permis l'essor de Node.js. V8 a été choisi comme moteur par Node.js dès 2009, et avec la popularité explosive de Node.js, V8 est devenu le moteur qui alimente désormais une quantité incroyable de code côté serveur écrit en JavaScript.

L'écosystème Node.js est énorme et grâce à lui, V8 alimente également les applications de bureau, avec des projets comme [Electron](https://electronjs.org/).

#### Autres moteurs JS

D'autres navigateurs ont leur propre moteur JavaScript :

* Firefox a [Spidermonkey](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey)
* Safari a [JavaScriptCore](https://developer.apple.com/documentation/javascriptcore) (aussi appelé Nitro)
* Edge a [Chakra](https://github.com/Microsoft/ChakraCore)

et beaucoup d'autres existent également.

Tous ces moteurs implémentent la norme ECMA ES-262, aussi appelée ECMAScript, la norme utilisée par JavaScript.

#### La quête de performance

V8 est écrit en C++, et il est continuellement amélioré. Il est portable et fonctionne sur Mac, Windows, Linux et plusieurs autres systèmes.

Dans cette introduction à V8, je vais ignorer les détails d'implémentation de V8. Ils peuvent être trouvés sur des sites plus autoritaires, y compris le [site officiel de V8](https://developers.google.com/v8/), et ils changent avec le temps, souvent radicalement.

V8 évolue constamment, tout comme les autres moteurs JavaScript, pour accélérer le Web et l'écosystème Node.js.

Sur le web, il y a une course à la performance qui dure depuis des années, et nous (en tant qu'utilisateurs et développeurs) bénéficions beaucoup de cette compétition car nous obtenons des machines plus rapides et plus optimisées année après année.

#### Compilation

JavaScript est généralement considéré comme un langage interprété, mais les moteurs JavaScript modernes n'interprètent plus simplement JavaScript, ils le compilent.

Cela se produit depuis 2009 lorsque le compilateur JavaScript SpiderMonkey a été ajouté à Firefox 3.5, et tout le monde a suivi cette idée.

JavaScript est compilé en interne par V8 avec une compilation juste-à-temps (JIT) pour accélérer l'exécution.

Cela peut sembler contre-intuitif. Mais depuis l'introduction de Google Maps en 2004, JavaScript a évolué d'un langage qui exécutait généralement quelques dizaines de lignes de code à des applications complètes avec des milliers à des centaines de milliers de lignes s'exécutant dans le navigateur.

Nos applications peuvent maintenant s'exécuter pendant des heures à l'intérieur d'un navigateur, plutôt que d'être simplement quelques règles de validation de formulaire ou des scripts simples.

Dans ce **nouveau monde**, compiler JavaScript a tout son sens car même si cela peut prendre un peu plus de temps pour que le JavaScript soit **prêt**, une fois fait, il sera beaucoup plus performant que du code purement interprété.

### Comment quitter un programme Node.js

Il existe diverses façons de terminer une application Node.js.

Lors de l'exécution d'un programme dans la console, vous pouvez le fermer avec `ctrl-C`, mais ce dont je veux discuter ici est la sortie programmatique.

Commençons par la méthode la plus drastique, et voyons pourquoi vous êtes mieux de **ne pas** l'utiliser.

Le module principal `process` fournit une méthode pratique qui vous permet de quitter programmatiquement un programme Node.js : `process.exit()`.

Lorsque Node.js exécute cette ligne, le processus est immédiatement forcé de se terminer.

Cela signifie que tout rappel en attente, toute requête réseau encore en cours d'envoi, tout accès au système de fichiers, ou tout processus écrivant dans `stdout` ou `stderr` — tout sera immédiatement terminé de manière brutale.

Si cela vous convient, vous pouvez passer un entier qui signale au système d'exploitation le code de sortie :

```js
process.exit(1)
```

Par défaut, le code de sortie est `0`, ce qui signifie succès. Différents codes de sortie ont différentes significations, que vous pourriez vouloir utiliser dans votre propre système pour faire communiquer le programme avec d'autres programmes.

Vous pouvez en lire plus sur les codes de sortie [ici](https://nodejs.org/api/process.html#process_exit_codes).

Vous pouvez également définir la propriété `process.exitCode` :

```js
process.exitCode = 1
```

et lorsque le programme se terminera plus tard, Node.js retournera ce code de sortie.

Un programme se terminera correctement lorsque tout le traitement sera terminé.

Souvent avec Node.js, nous démarrons des serveurs, comme ce serveur HTTP :

```js
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('Hi!')
})

app.listen(3000, () => console.log('Server ready'))

```

Ce programme ne se terminera jamais. Si vous appelez `process.exit()`, toute requête actuellement en attente ou en cours d'exécution sera abandonnée. Ce n'est **pas bien**.

Dans ce cas, vous devez envoyer à la commande un signal `SIGTERM`, et le gérer avec le gestionnaire de signaux de processus :

**Note :** `process` ne nécessite pas de `require`, il est automatiquement disponible.

```js
const express = require('express')

const app = express()

app.get('/', (req, res) => {
  res.send('Hi!')
})

const server = app.listen(3000, () => console.log('Server ready'))

process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Process terminated')
  })
})

```

Qu'est-ce que les signaux ? Les signaux sont un système d'intercommunication de l'interface portable du système d'exploitation (POSIX) : une notification envoyée à un processus afin de l'informer d'un événement qui s'est produit.

`SIGKILL` est le signal qui indique à un processus de se terminer immédiatement, et agirait idéalement comme `process.exit()`.

`SIGTERM` est le signal qui indique à un processus de se terminer correctement. C'est le signal qui est envoyé par les gestionnaires de processus comme `upstart` ou `supervisord` et beaucoup d'autres.

Vous pouvez envoyer ce signal depuis l'intérieur du programme, dans une autre fonction :

```js
process.kill(process.pid, 'SIGTERM')
```

Ou depuis un autre programme Node.js en cours d'exécution, ou toute autre application en cours d'exécution sur votre système qui connaît le PID du processus que vous souhaitez terminer.

### Comment lire les variables d'environnement depuis Node.js

Le module principal `process` de Node fournit la propriété `env` qui héberge toutes les variables d'environnement qui ont été définies au moment où le processus a été démarré.

Voici un exemple qui accède à la variable d'environnement `NODE_ENV`, qui est définie par défaut sur `development`.

```js
process.env.NODE_ENV // "development"
```

La définir sur `production` avant l'exécution du script indiquera à Node.js qu'il s'agit d'un environnement de production.

De la même manière, vous pouvez accéder à toute variable d'environnement personnalisée que vous avez définie.

Ici, nous définissons 2 variables pour API_KEY et API_SECRET

```js
API_KEY=123123 API_SECRET=456456 node app.js
```

Nous pouvons les obtenir dans Node.js en exécutant

```js
process.env.API_KEY // "123123"
process.env.API_SECRET // "456456"

```

Vous pouvez écrire les variables d'environnement dans un fichier `.env` (que vous devez ajouter à `.gitignore` pour éviter de le pousser sur GitHub), puis

```
npm install dotenv
```

et au début de votre fichier principal Node, ajoutez

```js
require('dotenv').config()

```

De cette façon, vous pouvez éviter de lister les variables d'environnement dans la ligne de commande avant la commande `node`, et ces variables seront récupérées automatiquement.

**Note :** Certains outils, comme Next.js par exemple, rendent les variables d'environnement définies dans `.env` automatiquement disponibles sans avoir besoin d'utiliser `dotenv`.

### Où héberger une application Node.js

Une application Node.js peut être hébergée dans de nombreux endroits, en fonction de vos besoins.

Voici une liste non exhaustive des options que vous pouvez explorer lorsque vous souhaitez déployer votre application et la rendre accessible au public.

Je vais lister les options de la plus simple et contrainte à la plus complexe et puissante.

#### Option la plus simple : tunnel local

Même si vous avez une IP dynamique, ou que vous êtes sous un NAT, vous pouvez déployer votre application et servir les requêtes directement depuis votre ordinateur en utilisant un tunnel local.

Cette option est adaptée pour des tests rapides, une démonstration de produit ou le partage d'une application avec un très petit groupe de personnes.

Un outil très pratique pour cela, disponible sur toutes les plateformes, est [ngrok](https://ngrok.com/).

En l'utilisant, vous pouvez simplement taper `ngrok PORT` et le PORT que vous souhaitez est exposé sur internet. Vous obtiendrez un domaine ngrok.io, mais avec un abonnement payant, vous pouvez obtenir une URL personnalisée ainsi que plus d'options de sécurité (n'oubliez pas que vous ouvrez votre machine au public Internet).

Un autre service que vous pouvez utiliser est [localtunnel](https://github.com/localtunnel/localtunnel).

#### Déploiements sans configuration

#### Glitch

[Glitch](https://glitch.com/) est un terrain de jeu et un moyen de construire vos applications plus rapidement que jamais, et de les voir en direct sur leur propre sous-domaine glitch.com. Vous ne pouvez pas actuellement avoir un domaine personnalisé, et il y a quelques [restrictions](https://glitch.com/faq#restrictions) en place, mais c'est vraiment génial pour prototyper. Cela semble amusant (et c'est un plus), et ce n'est pas un environnement simplifié — vous obtenez toute la puissance de Node.js, un CDN, un stockage sécurisé pour les identifiants, l'import/export GitHub et bien plus encore.

Fournis par l'entreprise derrière FogBugz et Trello (et co-créateurs de Stack Overflow).

Je l'utilise beaucoup à des fins de démonstration.

#### Codepen

[Codepen](https://codepen.io/) est une plateforme et une communauté incroyables. Vous pouvez créer un projet avec plusieurs fichiers, et le déployer avec un domaine personnalisé.

#### Serverless

Une façon de publier vos applications, et de ne pas avoir de serveur du tout à gérer, est Serverless. Serverless est un paradigme où vous publiez vos applications sous forme de **fonctions**, et elles répondent sur un point de terminaison réseau (aussi appelé FAAS — Functions As A Service).

Deux solutions très populaires sont :

* [Serverless Framework](https://serverless.com/framework/)
* [Standard Library](https://stdlib.com/)

Ils fournissent tous deux une couche d'abstraction pour la publication sur AWS Lambda et d'autres solutions FAAS basées sur Azure ou l'offre Google Cloud.

#### PAAS

PAAS signifie Platform As A Service. Ces plateformes enlèvent beaucoup de choses dont vous devriez autrement vous soucier lors du déploiement de votre application.

#### Zeit Now

[Zeit](https://zeit.co/now) est une option intéressante. Vous tapez simplement `now` dans votre terminal, et il se charge de déployer votre application. Il existe une version gratuite avec des limitations, et la version payante est plus puissante. Vous oubliez simplement qu'il y a un serveur, vous déployez simplement l'application.

#### Nanobox

[Nanobox](https://nanobox.io/)

#### Heroku

[Heroku](https://www.heroku.com/) est une plateforme incroyable.

Voici un excellent article sur [comment commencer avec Node.js sur Heroku](https://devcenter.heroku.com/articles/getting-started-with-node).

#### Microsoft Azure

[Azure](https://azure.microsoft.com/en-us/) est l'offre Cloud de Microsoft.

Découvrez comment [créer une application web Node.js dans Azure](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-node).

#### Google Cloud Platform

[Google Cloud](https://cloud.google.com/) est une structure incroyable pour vos applications.

Ils ont une bonne [section de documentation Node.js](https://cloud.google.com/node/).

#### Serveur privé virtuel

Dans cette section, vous trouverez les suspects habituels, classés du plus convivial au moins convivial :

* [Digital Ocean](https://www.digitalocean.com/)
* [Linode](https://www.linode.com/)
* [Amazon Web Services](https://aws.amazon.com/), en particulier je mentionne Amazon Elastic Beanstalk car il abstrait un peu la complexité d'AWS.

Puisqu'ils fournissent une machine Linux vide sur laquelle vous pouvez travailler, il n'y a pas de tutoriel spécifique pour ceux-ci.

Il existe beaucoup plus d'options dans la catégorie VPS, ce sont juste celles que j'ai utilisées et que je recommanderais.

#### Bare metal

Une autre solution est d'obtenir un [serveur bare metal](https://en.wikipedia.org/wiki/Bare-metal_server), d'installer une distribution Linux, de le connecter à internet (ou d'en louer un mensuellement, comme vous pouvez le faire en utilisant le service [Vultr Bare Metal](https://www.vultr.com/pricing/baremetal/))

### Comment utiliser le REPL de Node.js

REPL signifie Read-Evaluate-Print-Loop, et c'est un excellent moyen d'explorer les fonctionnalités de Node.js de manière rapide.

La commande `node` est celle que nous utilisons pour exécuter nos scripts Node.js :

```
node script.js
```

Si nous omettons le nom de fichier, nous l'utilisons en mode REPL :

```
node
```

Si vous l'essayez maintenant dans votre terminal, voici ce qui se passe :

```
❡ node
>

```

la commande reste en mode veille et attend que nous entrions quelque chose.

**Astuce** : si vous ne savez pas comment ouvrir votre terminal, recherchez sur Google « Comment ouvrir le terminal sur <votre système d'exploitation> ».

Le REPL attend que nous entrions du code JavaScript.

Commencez simplement et entrez :

```
> console.log('test')
test
undefined
>

```

La première valeur, `test`, est la sortie que nous avons demandée à la console d'imprimer, puis nous obtenons undefined qui est la valeur de retour de l'exécution de `console.log()`.

Nous pouvons maintenant entrer une nouvelle ligne de JavaScript.

#### Utiliser la touche tab pour l'autocomplétion

Le REPL est interactif.

Lorsque vous écrivez votre code, si vous appuyez sur la touche `tab`, le REPL essaiera de compléter automatiquement ce que vous avez écrit pour correspondre à une variable que vous avez déjà définie ou à une variable prédéfinie.

#### Explorer les objets JavaScript

Essayez d'entrer le nom d'une classe JavaScript, comme `Number`, ajoutez un point et appuyez sur `tab`.

Le REPL imprimera toutes les propriétés et méthodes auxquelles vous pouvez accéder sur cette classe :

![Image](https://cdn-media-1.freecodecamp.org/images/MgYHCtgjD1rom1yKM43E-qBh7ansJuyglRWr)

#### Explorer les objets globaux

Vous pouvez inspecter les globaux auxquels vous avez accès en tapant `global.` et en appuyant sur `tab` :

![Image](https://cdn-media-1.freecodecamp.org/images/e2qWLuyjYC4DFZjEs2jYWK-NL9AXbpDiSdA7)

#### La variable spéciale _

Si après du code vous tapez `_`, cela imprimera le résultat de la dernière opération.

#### Commandes de point

Le REPL dispose de certaines commandes spéciales, toutes commençant par un point `.`. Ce sont :

* `.help` : affiche l'aide des commandes de point
* `.editor` : active l'éditeur, pour écrire du code JavaScript multiline avec facilité. Une fois que vous êtes dans ce mode, entrez ctrl-D pour exécuter le code que vous avez écrit.
* `.break` : lors de la saisie d'une expression multiline, entrer la commande .break annulera la saisie supplémentaire. Identique à appuyer sur ctrl-C.
* `.clear` : réinitialise le contexte REPL à un objet vide et efface toute expression multiline actuellement en cours de saisie.
* `.load` : charge un fichier JavaScript, relatif au répertoire de travail actuel
* `.save` : sauvegarde tout ce que vous avez entré dans la session REPL dans un fichier (spécifiez le nom de fichier)
* `.exit` : quitte le repl (identique à appuyer deux fois sur ctrl-C)

Le REPL sait quand vous tapez une instruction multiline sans avoir besoin d'invoquer `.editor`.

Par exemple, si vous commencez à taper une itération comme ceci :

```js
[1, 2, 3].forEach(num => {
```

et que vous appuyez sur `enter`, le REPL passera à une nouvelle ligne qui commence par 3 points, indiquant que vous pouvez maintenant continuer à travailler sur ce bloc.

```js
...   console.log(num)
... })

```

Si vous tapez `.break` à la fin d'une ligne, le mode multiline s'arrêtera et l'instruction ne sera pas exécutée.

### Node.js, accepter des arguments de la ligne de commande

Comment accepter des arguments dans un programme Node.js passés depuis la ligne de commande

Vous pouvez passer n'importe quel nombre d'arguments lors de l'appel d'une application Node.js en utilisant :

```
node app.js
```

Les arguments peuvent être autonomes ou avoir une clé et une valeur.

Par exemple :

```
node app.js flavio
```

ou

```
node app.js name=flavio
```

Cela change la manière dont vous allez récupérer cette valeur dans le code Node.js.

La manière de la récupérer est d'utiliser l'objet `process` intégré à Node.js.

Il expose une propriété `argv`, qui est un tableau contenant tous les arguments d'invocation de la ligne de commande.

Le premier argument est le chemin complet de la commande `node`.

Le deuxième élément est le chemin complet du fichier en cours d'exécution.

Tous les arguments supplémentaires sont présents à partir de la troisième position.

Vous pouvez itérer sur tous les arguments (y compris le chemin de node et le chemin du fichier) en utilisant une boucle :

```js
process.argv.forEach((val, index) => {
  console.log(`${index}: ${val}`)
})

```

Vous pouvez obtenir uniquement les arguments supplémentaires en créant un nouveau tableau qui exclut les deux premiers paramètres :

```js
const args = process.argv.slice(2)
```

Si vous avez un argument sans nom d'index, comme ceci :

```
node app.js flavio
```

you pouvez y accéder en utilisant

```js
const args = process.argv.slice(2)
args[0]

```

Dans ce cas :

```
node app.js name=flavio
```

`args[0]` est `name=flavio`, et vous devez le parser. La meilleure façon de le faire est d'utiliser la bibliothèque `minimist` [library](https://www.npmjs.com/package/minimist), qui aide à gérer les arguments :

```js
const args = require('minimist')(process.argv.slice(2))
args['name'] // flavio

```

### Sortie vers la ligne de commande en utilisant Node.js

Comment imprimer sur la console de la ligne de commande en utilisant Node.js, du simple console.log à des scénarios plus complexes

#### Sortie de base en utilisant le module console

Node.js fournit un module `console` qui offre de nombreuses façons très utiles d'interagir avec la ligne de commande.

Il est essentiellement le même que l'objet `console` que vous trouvez dans le navigateur.

La méthode la plus basique et la plus utilisée est `console.log()`, qui imprime la chaîne que vous lui passez sur la console.

Si vous passez un objet, il le rendra sous forme de chaîne.

Vous pouvez passer plusieurs variables à `console.log`, par exemple :

```js
const x = 'x'
const y = 'y'
console.log(x, y)

```

et Node.js imprimera les deux.

Nous pouvons également formater de jolies phrases en passant des variables et un spécificateur de format.

Par exemple :

```js
console.log('My %s has %d years', 'cat', 2)
```

* `%s` formate une variable en tant que chaîne
* `%d` ou `%i` formate une variable en tant qu'entier
* `%f` formate une variable en tant que nombre à virgule flottante
* `%O` utilisé pour imprimer une représentation d'objet

Exemple :

```js
console.log('%O', Number)
```

#### Effacer la console

`console.clear()` efface la console (le comportement peut dépendre de la console utilisée)

#### Compter les éléments

`console.count()` est une méthode pratique.

Prenez ce code :

```js
const x = 1
const y = 2
const z = 3

console.count(
  'The value of x is ' + x + ' and has been checked .. how many times?'
)

console.count(
  'The value of x is ' + x + ' and has been checked .. how many times?'
)

console.count(
  'The value of y is ' + y + ' and has been checked .. how many times?'
)
```

Ce qui se passe, c'est que `count` comptera le nombre de fois qu'une chaîne est imprimée, et imprimera le compte à côté.

Vous pouvez simplement compter les pommes et les oranges :

```js
const oranges = ['orange', 'orange']
const apples = ['just one apple']

oranges.forEach(fruit => {
  console.count(fruit)
})

apples.forEach(fruit => {
  console.count(fruit)
})
```

#### Imprimer la trace de la pile

Il peut y avoir des cas où il est utile d'imprimer la trace de la pile d'appels d'une fonction, peut-être pour répondre à la question : « Comment avez-vous atteint cette partie du code ? »

Vous pouvez le faire en utilisant `console.trace()` :

```js
const function2 = () => console.trace()
const function1 = () => function2()
function1()

```

Cela imprimera la trace de la pile. Voici ce qui est imprimé si j'essaie cela dans le REPL Node :

```
Trace
  at function2 (repl:1:33)
  at function1 (repl:1:25)
  at repl:1:1
  at ContextifyScript.Script.runInThisContext (vm.js:44:33)
  at REPLServer.defaultEval (repl.js:239:29)
  at bound (domain.js:301:14)
  at REPLServer.runBound [as eval] (domain.js:314:12)
  at REPLServer.onLine (repl.js:440:10)
  at emitOne (events.js:120:20)
  at REPLServer.emit (events.js:210:7)
```

#### Calculer le temps écoulé

Vous pouvez facilement calculer combien de temps une fonction met à s'exécuter, en utilisant `time()` et `timeEnd()`

```js
const doSomething = () => console.log('test')
const measureDoingSomething = () => {
  console.time('doSomething()')
  // faire quelque chose, et mesurer le temps que cela prend
  doSomething()
  console.timeEnd('doSomething()')
}

measureDoingSomething()

```

#### stdout et stderr

Comme nous l'avons vu, console.log est idéal pour imprimer des messages dans la console. C'est ce qu'on appelle la sortie standard, ou `stdout`.

`console.error` imprime dans le flux `stderr`.

Il n'apparaîtra pas dans la console, mais il apparaîtra dans le journal des erreurs.

#### Colorier la sortie

Vous pouvez colorier la sortie de votre texte dans la console en utilisant des séquences d'échappement. Une séquence d'échappement est un ensemble de caractères qui identifie une couleur.

Exemple :

```js
console.log('\x1b[33m%s\x1b[0m', 'hi!')
```

Vous pouvez essayer cela dans le REPL Node, et il imprimera `hi!` en jaune.

Cependant, c'est la manière de bas niveau de faire cela. La manière la plus simple de colorier la sortie de la console est d'utiliser une bibliothèque. [Chalk](https://github.com/chalk/chalk) est une telle bibliothèque, et en plus de la coloration, elle aide également avec d'autres facilités de style, comme rendre le texte en gras, en italique ou souligné.

Vous l'installez avec `npm install chalk`, puis vous pouvez l'utiliser :

```js
const chalk = require('chalk')
console.log(chalk.yellow('hi!'))

```

Utiliser `chalk.yellow` est beaucoup plus pratique que d'essayer de se souvenir des codes d'échappement, et le code est beaucoup plus lisible.

Consultez le lien du projet que j'ai posté ci-dessus pour plus d'exemples d'utilisation.

#### Créer une barre de progression

[Progress](https://www.npmjs.com/package/progress) est un package génial pour créer une barre de progression dans la console. Installez-le en utilisant `npm install progress`.

Ce snippet crée une barre de progression en 10 étapes, et toutes les 100 ms une étape est complétée. Lorsque la barre est complète, nous effaçons l'intervalle :

```js
const ProgressBar = require('progress')

const bar = new ProgressBar(':bar', { total: 10 })
const timer = setInterval(() => {
  bar.tick()
  if (bar.complete) {
    clearInterval(timer)
  }
}, 100)

```

### Accepter l'entrée de la ligne de commande dans Node.js

Comment rendre un programme CLI Node.js interactif ?

Node, depuis la version 7, fournit le module `readline` pour effectuer exactement cela : obtenir une entrée depuis un flux lisible tel que le flux `process.stdin`, qui pendant l'exécution d'un programme Node est l'entrée du terminal, une ligne à la fois.

```js
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

readline.question(`What's your name?`, (name) => {
  console.log(`Hi ${name}!`)
  readline.close()
})

```

Ce morceau de code demande le nom d'utilisateur, et une fois le texte entré et que l'utilisateur appuie sur entrée, nous envoyons un message de salutation.

La méthode `question()` affiche le premier paramètre (une question) et attend l'entrée de l'utilisateur. Elle appelle la fonction de rappel une fois que la touche entrée est pressée.

Dans cette fonction de rappel, nous fermons l'interface readline.

`readline` offre plusieurs autres méthodes, et je vous laisse les découvrir dans la documentation du package que j'ai liée ci-dessus.

Si vous avez besoin de demander un mot de passe, il est préférable de ne pas l'écho, mais plutôt d'afficher un symbole `*`.

La manière la plus simple est d'utiliser le package [readline-sync](https://www.npmjs.com/package/readline-sync) qui est très similaire en termes d'API et gère cela directement.

Une solution plus complète et abstraite est fournie par le package [Inquirer.js](https://github.com/SBoudrias/Inquirer.js).

Vous pouvez l'installer en utilisant `npm install inquirer`, puis vous pouvez reproduire le code ci-dessus comme ceci :

```js
const inquirer = require('inquirer')

var questions = [{
  type: 'input',
  name: 'name',
  message: "What's your name?",
}]

inquirer.prompt(questions).then(answers => {
  console.log(`Hi ${answers['name']}!`)
})

```

Inquirer.js vous permet de faire beaucoup de choses comme demander plusieurs choix, avoir des boutons radio, des confirmations, et plus encore.

Il est utile de connaître toutes les alternatives, surtout celles intégrées fournies par Node.js, mais si vous prévoyez de faire passer l'entrée CLI au niveau supérieur, Inquirer.js est un choix optimal.

### Exposer des fonctionnalités depuis un fichier Node.js en utilisant exports

Comment utiliser l'API `module.exports` pour exposer des données à d'autres fichiers dans votre application, ou à d'autres applications également

Node.js dispose d'un système de modules intégré.

Un fichier Node.js peut importer des fonctionnalités exposées par d'autres fichiers Node.js.

Lorsque vous souhaitez importer quelque chose, vous utilisez :

```js
const library = require('./library')

```

pour importer les fonctionnalités exposées dans le fichier `library.js` qui se trouve dans le dossier du fichier actuel.

Dans ce fichier, les fonctionnalités doivent être exposées avant de pouvoir être importées par d'autres fichiers.

Tout autre objet ou variable défini dans le fichier est par défaut privé et non exposé au monde extérieur.

C'est ce que l'API `module.exports` offerte par le système de [modules](https://nodejs.org/api/modules.html) nous permet de faire.

Lorsque vous attribuez un objet ou une fonction en tant que nouvelle propriété `exports`, c'est la chose qui est exposée. En tant que telle, elle peut être importée dans d'autres parties de votre application, ou dans d'autres applications également.

Vous pouvez le faire de 2 manières.

La première consiste à attribuer un objet à `module.exports`, qui est un objet fourni par défaut par le système de modules, et cela fera en sorte que votre fichier n'exporte **que cet objet** :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta'
}

module.exports = car

// ...dans l'autre fichier

const car = require('./car')

```

La deuxième manière consiste à ajouter l'objet exporté en tant que propriété de `exports`. Cette manière permet d'exporter **plusieurs** objets, fonctions ou données :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta'
}

exports.car = car

```

ou directement

```js
exports.car = {
  brand: 'Ford',
  model: 'Fiesta'
}

```

Et dans l'autre fichier, vous l'utiliserez en référençant une propriété de votre import :

```js
const items = require('./items')
items.car

```

ou

```js
const car = require('./items').car
```

Quelle est la différence entre `module.exports` et `exports` ?

Le premier expose **l'objet** qu'il pointe. Le second expose **les propriétés** de l'objet qu'il pointe.

### Introduction à npm

`npm` signifie **node package manager**.

En janvier 2017, plus de 350 000 packages ont été signalés comme étant listés dans le registre npm, ce qui en fait le plus grand dépôt de code pour un seul langage sur Terre, et vous pouvez être sûr qu'il existe un package pour (presque !) tout.

Il a commencé comme un moyen de télécharger et de gérer les dépendances des packages Node.js, mais il est depuis devenu un outil utilisé également en JavaScript front-end.

Il y a beaucoup de choses que `npm` fait.

#### Téléchargements

`npm` gère les téléchargements des dépendances de votre projet.

#### Installation de toutes les dépendances

Si un projet a un fichier `packages.json`, en exécutant

```
npm install
```

il installera tout ce dont le projet a besoin, dans le dossier `node_modules`, en le créant s'il n'existe pas déjà.

#### Installation d'un seul package

Vous pouvez également installer un package spécifique en exécutant

```
npm install <package-name>
```

Souvent, vous verrez plus de flags ajoutés à cette commande :

* `--save` installe et ajoute l'entrée au fichier `package.json` `dependencies`
* `--save-dev` installe et ajoute l'entrée au fichier `package.json` `devDependencies`

La différence est principalement que `devDependencies` sont généralement des outils de développement, comme une bibliothèque de test, tandis que `dependencies` sont regroupés avec l'application en production.

#### Mise à jour des packages

La mise à jour est également simplifiée, en exécutant

```
npm update
```

`npm` vérifiera tous les packages pour une version plus récente qui satisfait vos contraintes de versionnement.

Vous pouvez spécifier un seul package à mettre à jour également :

```
npm update <package-name>
```

#### Versioning

En plus des téléchargements simples, `npm` gère également le **versioning**, afin que vous puissiez spécifier n'importe quelle version spécifique d'un package, ou exiger une version supérieure ou inférieure à celle dont vous avez besoin.

De nombreuses fois, vous constaterez qu'une bibliothèque n'est compatible qu'avec une version majeure d'une autre bibliothèque.

Ou un bug dans la dernière version d'une bibliothèque, toujours non corrigé, cause un problème.

Spécifier une version explicite d'une bibliothèque aide également à maintenir tout le monde sur la même version exacte d'un package, afin que toute l'équipe exécute la même version jusqu'à ce que le fichier `package.json` soit mis à jour.

Dans tous ces cas, le versioning aide beaucoup, et `npm` suit la norme de versioning sémantique (semver).

#### Exécution de tâches

Le fichier package.json prend en charge un format pour spécifier des tâches en ligne de commande qui peuvent être exécutées en utilisant

```
npm run <task-name>
```

Par exemple :

```json
{
  "scripts": {
    "start-dev": "node lib/server-development",
    "start": "node lib/server-production"
  },
}

```

Il est très courant d'utiliser cette fonctionnalité pour exécuter Webpack :

```json
{
  "scripts": {
    "watch": "webpack --watch --progress --colors --config webpack.conf.js",
    "dev": "webpack --progress --colors --config webpack.conf.js",
    "prod": "NODE_ENV=production webpack -p --config webpack.conf.js",
  },
}

```

Ainsi, au lieu de taper ces longues commandes, qui sont faciles à oublier ou à mal taper, vous pouvez exécuter

```
$ npm watch
$ npm dev
$ npm prod

```

### Où npm installe-t-il les packages ?

Lorsque vous installez un package en utilisant `npm` (ou [yarn](https://flaviocopes.com/yarn/)), vous pouvez effectuer 2 types d'installation :

* une installation locale
* une installation globale

Par défaut, lorsque vous tapez une commande `npm install`, comme :

```
npm install lodash
```

le package est installé dans l'arborescence de fichiers actuelle, sous le sous-dossier `node_modules`.

Lorsque cela se produit, `npm` ajoute également l'entrée `lodash` dans la propriété `dependencies` du fichier `package.json` présent dans le dossier actuel.

Une installation globale est effectuée en utilisant le flag `-g` :

```
npm install -g lodash
```

Lorsque cela se produit, npm n'installera pas le package sous le dossier local, mais utilisera plutôt un emplacement global.

Où, exactement ?

La commande `npm root -g` vous indiquera où se trouve cet emplacement exact sur votre machine.

Sur macOS ou Linux, cet emplacement pourrait être `/usr/local/lib/node_modules`. Sur Windows, il pourrait être `C:\Users\YOU\AppData\Roaming\npm\node_modules`

Cependant, si vous utilisez `nvm` pour gérer les versions de Node.js, cet emplacement serait différent.

Par exemple, j'utilise `nvm` et l'emplacement de mes packages était affiché comme `/Users/flavio/.nvm/versions/node/v8.9.0/lib/node_modules`.

### Comment utiliser ou exécuter un package installé en utilisant npm

#### Comment inclure et utiliser dans votre code un package installé dans votre dossier node_modules

Lorsque vous installez un package en utilisant `npm` dans votre dossier `node_modules`, ou également globalement, comment l'utiliser dans votre code Node ?

Supposons que vous installiez `lodash`, la bibliothèque utilitaire JavaScript populaire, en utilisant

```
npm install lodash
```

Cela va installer le package dans le dossier local `node_modules`.

Pour l'utiliser dans votre code, vous devez simplement l'importer dans votre programme en utilisant `require` :

```js
const _ = require('lodash')
```

Que se passe-t-il si votre package est un exécutable ?

Dans ce cas, il placera le fichier exécutable sous le dossier `node_modules/.bin/`.

Une manière facile de le démontrer est [cowsay](https://www.npmjs.com/package/cowsay).

Le package cowsay fournit un programme en ligne de commande qui peut être exécuté pour faire dire quelque chose à une vache (et à d'autres animaux aussi).

Lorsque vous installez le package en utilisant `npm install cowsay`, il s'installera ainsi que quelques dépendances dans le dossier node_modules.

Il y a un dossier caché .bin, qui contient des liens symboliques vers les binaires de cowsay.

Comment exécuter ceux-ci ?

Vous pouvez bien sûr taper `./node_modules/.bin/cowsay` pour l'exécuter, et cela fonctionne, mais [npx](https://flaviocopes.com/npx/), inclus dans les versions récentes de npm (depuis 5.2), est une bien meilleure option. Vous exécutez simplement :

```
npx cowsay
```

et npx trouvera l'emplacement du package.

### Le guide package.json

Le fichier package.json est un élément clé dans de nombreuses bases de code d'applications basées sur l'écosystème Node.js.

Si vous travaillez avec JavaScript, ou si vous avez déjà interagi avec un projet JavaScript, Node.js ou un projet front-end, vous avez sûrement rencontré le fichier `package.json`.

À quoi sert-il ? Que devez-vous savoir à son sujet, et quelles sont certaines des choses cool que vous pouvez faire avec ?

Le fichier `package.json` est une sorte de manifeste pour votre projet. Il peut faire beaucoup de choses, complètement sans rapport. C'est un dépôt central de configuration pour les outils, par exemple. C'est aussi là où `[npm](https://flaviocopes.com/npm/)` et `[yarn](https://flaviocopes.com/yarn/)` stockent les noms et versions des packages qu'ils ont installés.

#### La structure du fichier

Voici un exemple de fichier package.json :

```json
{

}

```

Il est vide ! Il n'y a pas d'exigences fixes quant à ce qui doit figurer dans un fichier `package.json`, pour une application. La seule exigence est qu'il respecte le format JSON, sinon il ne peut pas être lu par les programmes qui tentent d'accéder à ses propriétés de manière programmatique.

Si vous construisez un package Node.js que vous souhaitez distribuer via `npm`, les choses changent radicalement, et vous devez avoir un ensemble de propriétés qui aideront les autres personnes à l'utiliser. Nous en verrons plus sur ce sujet plus tard.

Voici un autre package.json :

```json
{
  "name": "test-project"
}
```

Il définit une propriété `name`, qui indique le nom de l'application, ou du package, contenu dans le même dossier où se trouve ce fichier.

Voici un exemple beaucoup plus complexe, que j'ai extrait d'une application Vue.js d'exemple :

```json
{
  "name": "test-project",
  "version": "1.0.0",
  "description": "A Vue.js project",
  "main": "src/main.js",
  "private": true,
  "scripts": {
    "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
    "start": "npm run dev",
    "unit": "jest --config test/unit/jest.conf.js --coverage",
    "test": "npm run unit",
    "lint": "eslint --ext .js,.vue src test/unit",
    "build": "node build/build.js"
  },
  "dependencies": {
    "vue": "^2.5.2"
  },
  "devDependencies": {
    "autoprefixer": "^7.1.2",
    "babel-core": "^6.22.1",
    "babel-eslint": "^8.2.1",
    "babel-helper-vue-jsx-merge-props": "^2.0.3",
    "babel-jest": "^21.0.2",
    "babel-loader": "^7.1.1",
    "babel-plugin-dynamic-import-node": "^1.2.0",
    "babel-plugin-syntax-jsx": "^6.18.0",
    "babel-plugin-transform-es2015-modules-commonjs": "^6.26.0",
    "babel-plugin-transform-runtime": "^6.22.0",
    "babel-plugin-transform-vue-jsx": "^3.5.0",
    "babel-preset-env": "^1.3.2",
    "babel-preset-stage-2": "^6.22.0",
    "chalk": "^2.0.1",
    "copy-webpack-plugin": "^4.0.1",
    "css-loader": "^0.28.0",
    "eslint": "^4.15.0",
    "eslint-config-airbnb-base": "^11.3.0",
    "eslint-friendly-formatter": "^3.0.0",
    "eslint-import-resolver-webpack": "^0.8.3",
    "eslint-loader": "^1.7.1",
    "eslint-plugin-import": "^2.7.0",
    "eslint-plugin-vue": "^4.0.0",
    "extract-text-webpack-plugin": "^3.0.0",
    "file-loader": "^1.1.4",
    "friendly-errors-webpack-plugin": "^1.6.1",
    "html-webpack-plugin": "^2.30.1",
    "jest": "^22.0.4",
    "jest-serializer-vue": "^0.3.0",
    "node-notifier": "^5.1.2",
    "optimize-css-assets-webpack-plugin": "^3.2.0",
    "ora": "^1.2.0",
    "portfinder": "^1.0.13",
    "postcss-import": "^11.0.0",
    "postcss-loader": "^2.0.8",
    "postcss-url": "^7.2.1",
    "rimraf": "^2.6.0",
    "semver": "^5.3.0",
    "shelljs": "^0.7.6",
    "uglifyjs-webpack-plugin": "^1.1.1",
    "url-loader": "^0.5.8",
    "vue-jest": "^1.0.2",
    "vue-loader": "^13.3.0",
    "vue-style-loader": "^3.0.1",
    "vue-template-compiler": "^2.5.2",
    "webpack": "^3.6.0",
    "webpack-bundle-analyzer": "^2.9.0",
    "webpack-dev-server": "^2.9.1",
    "webpack-merge": "^4.1.0"
  },
  "engines": {
    "node": ">= 6.0.0",
    "npm": ">= 3.0.0"
  },
  "browserslist": ["> 1%", "last 2 versions", "not ie <= 8"]
}

```

il se passe **beaucoup** de choses ici :

* `name` définit le nom de l'application/package
* `version` indique la version actuelle
* `description` est une brève description de l'application/package
* `main` définit le point d'entrée de l'application
* `private` si défini sur `true` empêche l'application/package d'être accidentellement publiée sur `npm`
* `scripts` définit un ensemble de scripts node que vous pouvez exécuter
* `dependencies` définit une liste de packages `npm` installés en tant que dépendances
* `devDependencies` définit une liste de packages `npm` installés en tant que dépendances de développement
* `engines` définit les versions de Node sur lesquelles ce package/application fonctionne
* `browserslist` est utilisé pour indiquer les navigateurs (et leurs versions) que vous souhaitez prendre en charge

Toutes ces propriétés sont utilisées soit par `npm`, soit par d'autres outils que nous pouvons utiliser.

#### Décomposition des propriétés

Cette section décrit les propriétés que vous pouvez utiliser en détail. Je fais référence à « package » mais la même chose s'applique aux applications locales que vous n'utilisez pas comme packages.

La plupart de ces propriétés ne sont utilisées que sur le site web de npm, d'autres par des scripts qui interagissent avec votre code, comme `npm` ou d'autres.

#### `name`

Définit le nom du package.

Exemple :

```json
"name": "test-project"
```

Le nom doit comporter moins de 214 caractères, ne doit pas contenir d'espaces, il ne peut contenir que des lettres minuscules, des tirets (`-`) ou des traits de soulignement (`_`).

C'est parce que lorsqu'un package est publié sur `npm`, il obtient sa propre URL basée sur cette propriété.

Si vous avez publié ce package publiquement sur GitHub, une bonne valeur pour cette propriété est le nom du dépôt GitHub.

#### `author`

Liste le nom de l'auteur du package

Exemple :

```json
{
  "author": "Flavio Copes <flavio@flaviocopes.com> (https://flaviocopes.com)"
}
```

Peut également être utilisé avec ce format :

```json
{
  "author": {
    "name": "Flavio Copes",
    "email": "your@email.com",
    "url": "https://flaviocopes.com"
  }
}

```

#### `contributors`

En plus de l'auteur, le projet peut avoir un ou plusieurs contributeurs. Cette propriété est un tableau qui les liste.

Exemple :

```json
{
  "contributors": ["Flavio Copes <your@email.com> (https://flaviocopes.com)"]
}

```

Peut également être utilisé avec ce format :

```json
{
  "contributors": [
    {
      "name": "Flavio Copes",
      "email": "your@email.com",
      "url": "https://flaviocopes.com"
    }
  ]
}

```

#### `bugs`

Liens vers le suivi des problèmes du package, très probablement une page de problèmes GitHub

Exemple :

```json
{
  "bugs": "https://github.com/flaviocopes/package/issues"
}
```

#### `homepage`

Définit la page d'accueil du package

Exemple :

```json
{
  "homepage": "https://flaviocopes.com/package"
}

```

#### `version`

Indique la version actuelle du package.

Exemple :

```json
"version": "1.0.0"
```

Cette propriété suit la notation de version sémantique (semver) pour les versions, ce qui signifie que la version est toujours exprimée avec 3 chiffres : `x.x.x`.

Le premier chiffre est la version majeure, le second la version mineure et le troisième est la version de correctif.

Il y a une signification dans ces chiffres : une version qui ne corrige que des bugs est une version de correctif, une version qui introduit des changements compatibles avec les versions précédentes est une version mineure, une version majeure peut avoir des changements cassants.

#### `license`

Indique la licence du package.

Exemple :

```json
"license": "MIT"
```

#### `keywords`

Cette propriété contient un tableau de mots-clés associés à ce que fait votre package.

Exemple :

```json
"keywords": [
  "email",
  "machine learning",
  "ai"
]

```

Cela aide les gens à trouver votre package lorsqu'ils naviguent parmi des packages similaires, ou lorsqu'ils parcourent le site web npm.

#### `description`

Cette propriété contient une brève description du package.

Exemple :

```json
"description": "A package to work with strings"
```

Cela est particulièrement utile si vous décidez de publier votre package sur `npm` afin que les gens puissent découvrir de quoi il s'agit.

#### `repository`

Cette propriété spécifie où se trouve le dépôt de ce package.

Exemple :

```
"repository": "github:flaviocopes/testing",
```

Remarquez le préfixe `github`. Il existe d'autres services populaires intégrés :

```json
"repository": "gitlab:flaviocopes/testing",
```

```json
"repository": "bitbucket:flaviocopes/testing",
```

Vous pouvez définir explicitement le système de contrôle de version :

```json
"repository": {
  "type": "git",
  "url": "https://github.com/flaviocopes/testing.git"
}

```

Vous pouvez utiliser différents systèmes de contrôle de version :

```json
"repository": {
  "type": "svn",
  "url": "..."
}

```

#### `main`

Définit le point d'entrée du package.

Lorsque vous importez ce package dans une application, c'est là que l'application recherchera les exports du module.

Exemple :

```json
"main": "src/main.js"
```

#### `private`

si défini sur `true`, empêche l'application/package d'être accidentellement publiée sur `npm`

Exemple :

```json
"private": true
```

#### `scripts`

Définit un ensemble de scripts node que vous pouvez exécuter

Exemple :

```json
"scripts": {
  "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
  "start": "npm run dev",
  "unit": "jest --config test/unit/jest.conf.js --coverage",
  "test": "npm run unit",
  "lint": "eslint --ext .js,.vue src test/unit",
  "build": "node build/build.js"
}

```

Ces scripts sont des applications en ligne de commande. Vous pouvez les exécuter en appelant `npm run XXXX` ou `yarn XXXX`, où `XXXX` est le nom de la commande.

Exemple :  
`npm run dev`

Vous pouvez utiliser n'importe quel nom que vous voulez pour une commande, et les scripts peuvent faire littéralement tout ce que vous voulez.

#### `dependencies`

Définit une liste de packages `npm` installés en tant que dépendances.

Lorsque vous installez un package en utilisant npm ou yarn :

```
npm install <PACKAGENAME>
yarn add <PACKAGENAME>

```

ce package est automatiquement inséré dans cette liste.

Exemple :

```json
"dependencies": {
  "vue": "^2.5.2"
}

```

#### `devDependencies`

Définit une liste de packages `npm` installés en tant que dépendances de développement.

Ils diffèrent des `dependencies` car ils sont destinés à être installés uniquement sur une machine de développement, non nécessaires pour exécuter le code en production.

Lorsque vous installez un package en utilisant `npm` ou `yarn` :

```
npm install --dev <PACKAGENAME>
yarn add --dev <PACKAGENAME>

```

ce package est automatiquement inséré dans cette liste.

Exemple :

```json
"devDependencies": {
  "autoprefixer": "^7.1.2",
  "babel-core": "^6.22.1"
}

```

#### `engines`

Définit les versions de Node.js et autres commandes sur lesquelles ce package/application fonctionne.

Exemple :

```json
"engines": {
  "node": ">= 6.0.0",
  "npm": ">= 3.0.0",
  "yarn": "^0.13.0"
}

```

#### `browserslist`

Est utilisé pour indiquer les navigateurs (et leurs versions) que vous souhaitez prendre en charge. Il est référencé par Babel, Autoprefixer et d'autres outils, pour n'ajouter que les polyfills et les retours nécessaires aux navigateurs que vous ciblez.

Exemple :

```json
"browserslist": [
  "> 1%",
  "last 2 versions",
  "not ie <= 8"
]

```

Cette configuration signifie que vous souhaitez prendre en charge les 2 dernières versions majeures de tous les navigateurs avec au moins 1 % d'utilisation (selon les statistiques de [CanIUse.com](https://caniuse.com/)), à l'exception d'IE8 et des versions inférieures ([voir plus](https://www.npmjs.com/package/browserslist) sur browserslist).

#### Propriétés spécifiques aux commandes

Le fichier `package.json` peut également héberger une configuration spécifique aux commandes, par exemple pour Babel, ESLint, et plus encore.

Chaque commande a une propriété spécifique, comme `eslintConfig`, `babel` et autres. Celles-ci sont spécifiques aux commandes, et vous pouvez trouver comment les utiliser dans la documentation respective de la commande/du projet.

#### Versions des packages

Vous avez vu dans la description ci-dessus des numéros de version comme ceux-ci : `~3.0.0` ou `^0.13.0`. Que signifient-ils, et quels autres spécificateurs de version pouvez-vous utiliser ?

Ce symbole spécifie les mises à jour que votre package accepte, à partir de cette dépendance.

Étant donné que l'utilisation de semver (versioning sémantique) toutes les versions ont 3 chiffres, le premier étant la version majeure, le second la version mineure et le troisième est la version de correctif, vous avez ces règles :

* `~` : si vous écrivez `~0.13.0`, vous voulez uniquement mettre à jour les versions de correctif : `0.13.1` est ok, mais `0.14.0` ne l'est pas.
* `^` : si vous écrivez `^0.13.0`, vous voulez mettre à jour les versions de correctif et mineures : `0.13.1`, `0.14.0` et ainsi de suite.
* `*` : si vous écrivez `*`, cela signifie que vous acceptez toutes les mises à jour, y compris les mises à jour majeures.
* `>` : vous acceptez toute version supérieure à celle que vous spécifiez
* `>=` : vous acceptez toute version égale ou supérieure à celle que vous spécifiez
* `<=` : vous acceptez toute version égale ou inférieure à celle que vous spécifiez
* `<` : vous acceptez toute version inférieure à celle que vous spécifiez

Il existe d'autres règles également :

* aucun symbole : vous acceptez uniquement cette version spécifique que vous spécifiez
* `latest` : vous souhaitez utiliser la dernière version disponible

et vous pouvez combiner la plupart de ceux-ci dans des plages, comme ceci : `1.0.0 || >=1.1.0 <1.2.0`, pour utiliser soit 1.0.0 soit une version à partir de 1.1.0, mais inférieure à 1.2.0.

### Le fichier package-lock.json

Le fichier package-lock.json est généré automatiquement lors de l'installation des packages node.

Dans la version 5, npm a introduit le fichier `package-lock.json`.

À quoi sert-il ? Vous connaissez probablement le fichier `package.json`, qui est beaucoup plus courant et existe depuis beaucoup plus longtemps.

Le but du fichier est de garder une trace de la version exacte de chaque package qui est installé afin qu'un produit soit reproductible à 100 % de la même manière même si les packages sont mis à jour par leurs mainteneurs.

Cela résout un problème très spécifique que `package.json` n'a pas résolu. Dans package.json, vous pouvez définir les versions que vous souhaitez mettre à jour (correctif ou mineur), en utilisant la notation **semver**, par exemple :

* si vous écrivez `~0.13.0`, vous voulez uniquement mettre à jour les versions de correctif : `0.13.1` est ok, mais `0.14.0` ne l'est pas.
* si vous écrivez `^0.13.0`, vous voulez mettre à jour les versions de correctif et mineures : `0.13.1`, `0.14.0` et ainsi de suite.
* si vous écrivez `0.13.0`, c'est la version exacte qui sera utilisée, toujours

Vous ne commitez pas votre dossier node_modules sur Git, qui est généralement énorme, et lorsque vous essayez de répliquer le projet sur une autre machine en utilisant la commande `npm install`, si vous avez spécifié la syntaxe `~` et qu'une version de correctif d'un package a été publiée, celle-ci sera installée. Même chose pour `^` et les versions mineures.

Si vous spécifiez des versions exactes, comme `0.13.0` dans l'exemple, vous n'êtes pas affecté par ce problème.

Cela pourrait être vous, ou une autre personne essayant d'initialiser le projet de l'autre côté du monde en exécutant `npm install`.

Ainsi, votre projet original et le projet nouvellement initialisé sont en fait différents. Même si une version de correctif ou mineure ne devrait pas introduire de changements cassants, nous savons tous que des bugs peuvent (et le feront) se glisser.

Le `package-lock.json` définit la version actuellement installée de chaque package **dans le marbre**, et `npm` utilisera ces versions exactes lors de l'exécution de `npm install`.

Ce concept n'est pas nouveau, et d'autres gestionnaires de packages de langages de programmation (comme Composer en PHP) utilisent un système similaire depuis des années.

Le fichier `package-lock.json` doit être commit dans votre dépôt Git, afin qu'il puisse être récupéré par d'autres personnes, si le projet est public ou si vous avez des collaborateurs, ou si vous utilisez Git comme source pour les déploiements.

Les versions des dépendances seront mises à jour dans le fichier `package-lock.json` lorsque vous exécuterez `npm update`.

#### Un exemple

Voici une structure d'exemple d'un fichier `package-lock.json` que nous obtenons lorsque nous exécutons `npm install cowsay` dans un dossier vide :

```json
{
  "requires": true,
  "lockfileVersion": 1,
  "dependencies": {
    "ansi-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz",
      "integrity": "sha1-7QMXwyIGT3lGbAKWa922Bas32Zg="
    },
    "cowsay": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/cowsay/-/cowsay-1.3.1.tgz",
      "integrity": "sha512-3PVFe6FePVtPj1HTeLin9v8WyLl+VmM1l1H/5P+BTTDkMAjufp+0F9eLjzRnOHzVAYeIYFF5po5NjRrgefnRMQ==",
      "requires": {
        "get-stdin": "^5.0.1",
        "optimist": "~0.6.1",
        "string-width": "~2.1.1",
        "strip-eof": "^1.0.0"
      }
    },
    "get-stdin": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/get-stdin/-/get-stdin-5.0.1.tgz",
      "integrity": "sha1-Ei4WFZHiH/TFJTAwVpPyDmOTo5g="
    },
    "is-fullwidth-code-point": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz",
      "integrity": "sha1-o7MKXE8ZkYMWeqq5O+764937ZU8="
    },
    "minimist": {
      "version": "0.0.10",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-0.0.10.tgz",
      "integrity": "sha1-3j+YVD2/lggr5IrRoMfNqDYwHc8="
    },
    "optimist": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/optimist/-/optimist-0.6.1.tgz",
      "integrity": "sha1-2j6nRob6IaGaERwybpDrFaAZZoY=",
      "requires": {
        "minimist": "~0.0.1",
        "wordwrap": "~0.0.2"
      }
    },
    "string-width": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz",
      "integrity": "sha512-nOqH59deCq9SRHlxq1Aw85Jnt4w6KvLKqWVik6oA9ZklXLNIOlqg4F2yrT1MVa",
      "requires": {
        "is-fullwidth-code-point": "^2.0.0",
        "strip-ansi": "^4.0.0"
      }
    },
    "strip-ansi": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz",
      "integrity": "sha1-qEeQIusaw2iocTibY1JixQXuNo8=",
      "requires": {
        "ansi-regex": "^3.0.0"
      }
    },
    "strip-eof": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz",
      "integrity": "sha1-u0P/VZim6wXYm1n80SnJgzE2Br8="
    },
    "wordwrap": {
      "version": "0.0.3",
      "resolved": "https://registry.npmjs.org/wordwrap/-/wordwrap-0.0.3.tgz",
      "integrity": "sha1-o9XabNXAvAAI03I0u68b7WMFkQc="
    }
  }
}

```

Nous avons installé `cowsay`, qui dépend de :

* `get-stdin`
* `optimist`
* `string-width`
* `strip-eof`

À leur tour, ces packages nécessitent d'autres packages, comme nous pouvons le voir à partir de la propriété `requires` que certains ont :

* `ansi-regex`
* `is-fullwidth-code-point`
* `minimist`
* `wordwrap`
* `strip-eof`

Ils sont ajoutés par ordre alphabétique dans le fichier, et chacun a un champ `version`, un champ `resolved` qui pointe vers l'emplacement du package, et une chaîne `integrity` que nous pouvons utiliser pour vérifier le package.

### Trouver la version installée d'un package npm

Pour voir la dernière version de tous les packages npm installés, y compris leurs dépendances :

```
npm list
```

Exemple :

```
❡ npm list
/Users/flavio/dev/node/cowsay
└── cowsay@1.3.1
  ├── get-stdin@5.0.1
  ├── optimist@0.6.1
  │ ├── minimist@0.0.10
  │ └── wordwrap@0.0.3
  ├── string-width@2.1.1
  │ ├── is-fullwidth-code-point@2.0.0
  │ └── strip-ansi@4.0.0
  │   └── ansi-regex@3.0.0
  └── strip-eof@1.0.0
 
```

Vous pouvez également simplement ouvrir le fichier `package-lock.json`, mais cela implique un balayage visuel.

`npm list -g` est la même chose, mais pour les packages installés globalement.

Pour obtenir uniquement vos packages de premier niveau (basiquement, ceux que vous avez demandés à npm d'installer et que vous avez listés dans le `package.json`), exécutez `npm list --depth=0` :

```
❡ npm list --depth=0
/Users/flavio/dev/node/cowsay
└── cowsay@1.3.1
```

Vous pouvez obtenir la version d'un package spécifique en spécifiant le nom :

```
❡ npm list cowsay
/Users/flavio/dev/node/cowsay
└── cowsay@1.3.1
```

Cela fonctionne également pour les dépendances des packages que vous avez installés :

```
❡ npm list minimist
/Users/flavio/dev/node/cowsay
└── cowsay@1.3.1
  └── optimist@0.6.1
    └── minimist@0.0.10
```

Si vous souhaitez voir quelle est la dernière version disponible du package sur le dépôt npm, exécutez `npm view [package_name] version` :

```
❡ npm view cowsay version

1.3.1

```

### Installer une ancienne version d'un package npm

Installer une ancienne version d'un package npm peut être utile pour résoudre un problème de compatibilité.

Vous pouvez installer une ancienne version d'un package npm en utilisant la syntaxe `@` :

```
npm install <package>@<version>
```

Exemple :

```
npm install cowsay
```

installe la version 1.3.1 (au moment de l'écriture).

Installez la version 1.2.0 avec :

```
npm install cowsay@1.2.0
```

La même chose peut être faite avec les packages globaux :

```
npm install -g webpack@4.16.4
```

Vous pourriez également être intéressé par la liste de toutes les versions précédentes d'un package. Vous pouvez le faire avec `npm view <package> versions` :

```
❡ npm view cowsay versions

[ '1.0.0',
  '1.0.1',
  '1.0.2',
  '1.0.3',
  '1.1.0',
  '1.1.1',
  '1.1.2',
  '1.1.3',
  '1.1.4',
  '1.1.5',
  '1.1.6',
  '1.1.7',
  '1.1.8',
  '1.1.9',
  '1.2.0',
  '1.2.1',
  '1.3.0',
  '1.3.1' ]
```

### Mettre à jour toutes les dépendances Node vers leur dernière version

Lorsque vous installez un package en utilisant `npm install <packagena`me>, la dernière version disponible du package est téléchargée et placée dans le dossier `node_m`odules, et une entrée correspondante est ajoutée au fichier `packag`e.jso`n et `package-loc`k.json qui sont présents dans votre dossier actuel.

npm calcule les dépendances et installe la dernière version disponible de celles-ci également.

Disons que vous installez `[cowsay](https://www.npmjs.com/package/cowsay)`, un outil de ligne de commande cool qui vous permet de faire dire des **choses** à une vache.

Lorsque vous exécutez `npm install cowsay`, cette entrée est ajoutée au fichier `package.json` :

```json
{
  "dependencies": {
    "cowsay": "^1.3.1"
  }
}

```

et voici un extrait de `package-lock.json`, où j'ai supprimé les dépendances imbriquées pour plus de clarté :

```json
{
  "requires": true,
  "lockfileVersion": 1,
  "dependencies": {
    "cowsay": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/cowsay/-/cowsay-1.3.1.tgz",
      "integrity": "sha512-3PVFe6FePVtPj1HTeLin9v8WyLl+VmM1l1H/5P+BTTDkMAjufp+0F9eLjzRnOH",
      "requires": {
        "get-stdin": "^5.0.1",
        "optimist": "~0.6.1",
        "string-width": "~2.1.1",
        "strip-eof": "^1.0.0"
      }
    }
  }
}

```

Ces deux fichiers nous indiquent que nous avons installé la version `1.3.1` de cowsay, et notre règle pour les mises à jour est `^1.3.1`, ce qui, selon les règles de versionnement de npm (expliquées plus loin), signifie que npm peut mettre à jour vers les versions de correctif et mineures : `0.13.1`, `0.14.0` et ainsi de suite.

Si une nouvelle version mineure ou de correctif est disponible et que nous tapons `npm update`, la version installée est mise à jour, et le fichier `package-lock.json` est diligemment rempli avec la nouvelle version.

`package.json` reste inchangé.

Pour découvrir les nouvelles versions des packages, vous exécutez `npm outdated`.

Voici la liste de quelques packages obsolètes dans un dépôt que je n'ai pas mis à jour depuis un certain temps :

![Image](https://cdn-media-1.freecodecamp.org/images/dQXY78UwUHW2iHblpRRLd8YdM4Zvdyf-3ctc)

Certaines de ces mises à jour sont des versions majeures. L'exécution de `npm update` ne mettra pas à jour la version de celles-ci. Les versions majeures ne sont jamais mises à jour de cette manière car elles (par définition) introduisent des changements cassants, et `npm` veut vous éviter des ennuis.

Pour mettre à jour vers une nouvelle version majeure tous les packages, installez le package `npm-check-updates` globalement :

```
npm install -g npm-check-updates
```

puis exécutez-le :

```
ncu -u
```

Cela mettra à jour toutes les indications de version dans le fichier `package.json`, vers `dependencies` et `devDependencies`, afin que npm puisse installer la nouvelle version majeure.

Vous êtes maintenant prêt à exécuter la mise à jour :

```
npm update
```

Si vous venez de télécharger le projet sans les dépendances `node_modules` et que vous souhaitez installer les nouvelles versions dès le début, exécutez simplement

```
npm install
```

### Versioning sémantique utilisant npm

Le versioning sémantique est une convention utilisée pour donner un sens aux versions.

S'il y a une chose formidable dans les packages Node.js, c'est que tous ont convenu d'utiliser le versioning sémantique pour leur numérotation de version.

Le concept de versioning sémantique est simple : toutes les versions ont 3 chiffres : `x.y.z`.

* le premier chiffre est la version majeure
* le second chiffre est la version mineure
* le troisième chiffre est la version de correctif

Lorsque vous faites une nouvelle version, vous n'augmentez pas un nombre à votre guise, mais vous avez des règles :

* vous augmentez la version majeure lorsque vous faites des changements d'API incompatibles
* vous augmentez la version mineure lorsque vous ajoutez des fonctionnalités de manière rétrocompatible
* vous augmentez la version de correctif lorsque vous faites des corrections de bugs rétrocompatibles

La convention est adoptée dans tous les langages de programmation, et il est très important que chaque package `npm` l'adopte, car tout le système en dépend.

Pourquoi est-ce si important ?

Parce que `npm` a défini certaines règles que nous pouvons utiliser dans le [fichier `package.json`](https://flaviocopes.com/package-json/) pour choisir les versions vers lesquelles il peut mettre à jour nos packages, lorsque nous exécutons `npm update`.

Les règles utilisent ces symboles :

* `^`
* `~`
* `>
* `>=`
* `<`
* `<=`
* `=`
* `-`
* `||`

Voyons ces règles en détail :

* `^` : si vous écrivez `^0.13.0` lors de l'exécution de `npm update`, il peut mettre à jour vers les versions de correctif et mineures : `0.13.1`, `0.14.0` et ainsi de suite.
* `~` : si vous écrivez `~0.13.0`, lors de l'exécution de `npm update`, il peut mettre à jour vers les versions de correctif : `0.13.1` est ok, mais `0.14.0` ne l'est pas.
* `<` : vous acceptez toute version supérieure à celle que vous spécifiez
* `>=` : vous acceptez toute version égale ou supérieure à celle que vous spécifiez
* `<=` : vous acceptez toute version égale ou inférieure à celle que vous spécifiez
* `<` : vous acceptez toute version inférieure à celle que vous spécifiez
* `=` : vous acceptez cette version exacte
* `-` : vous acceptez une plage de versions. Exemple : `2.1.0 - 2.6.2`
* `||` : vous combinez des ensembles. Exemple : `< 2.1 || > 2.6`

Vous pouvez combiner certaines de ces notations, par exemple utiliser `1.0.0 || >=1.1.0 <1.2.0` pour utiliser soit 1.0.0 soit une version à partir de 1.1.0, mais inférieure à 1.2.0.

Il existe d'autres règles également :

* aucun symbole : vous acceptez uniquement cette version spécifique que vous spécifiez (`1.2.1`)
* `latest` : vous souhaitez utiliser la dernière version disponible

### Désinstaller des packages npm localement ou globalement

Pour désinstaller un package que vous avez précédemment installé **localement** (en utilisant `npm install <package-na`me> dans le dossier `node_m`odules), exécutez :

```
npm uninstall <package-name>
```

à partir du dossier racine du projet (le dossier qui contient le dossier node_modules).

Cette opération supprimera également la référence dans le [fichier](https://flaviocopes.com/package-json/) `[package.json](https://flaviocopes.com/package-json/)`.

Si le package était une dépendance de développement, listée dans les devDependencies du fichier `package.json`, vous devez utiliser le flag `-D` / `--save-dev` pour le supprimer du fichier :

```
npm uninstall -D <package-name>
```

Si le package est installé **globalement**, vous devez ajouter le flag `-g` / `--global` :

```
npm uninstall -g <package-name>
```

Exemple :

```
npm uninstall -g webpack
```

et vous pouvez exécuter cette commande depuis n'importe où sur votre système car le dossier où vous vous trouvez actuellement n'a pas d'importance.

### Packages npm globaux ou locaux

Quand un package est-il mieux installé globalement ? Et pourquoi ?

La principale différence entre les packages locaux et globaux est la suivante :

* **les packages locaux** sont installés dans le répertoire où vous exécutez `npm install <package-name>`, et ils sont placés dans le dossier `node_modules` sous ce répertoire
* **les packages globaux** sont tous placés en un seul endroit dans votre système (exactement où dépend de votre configuration), indépendamment de l'endroit où vous exécutez `npm install -g <package-name>`

Dans votre code, ils sont tous deux requis de la même manière :

```js
require('package-name')
```

Alors, quand devez-vous installer de l'une ou l'autre manière ?

En général, tous les packages doivent être installés **localement**.

Cela garantit que vous pouvez avoir des dizaines d'applications sur votre ordinateur, toutes exécutant une version différente de chaque package si nécessaire.

Mettre à jour un package global ferait en sorte que tous vos projets utilisent la nouvelle version, et comme vous pouvez l'imaginer, cela pourrait causer des cauchemars en termes de maintenance, car certains packages pourraient rompre la compatibilité avec d'autres dépendances, et ainsi de suite.

Tous les projets ont leur propre version locale d'un package, même si cela peut sembler un gaspillage de ressources, c'est minimal par rapport aux conséquences négatives possibles.

Un package doit être installé **globalement** lorsqu'il fournit une commande exécutable que vous exécutez depuis le shell (CLI), et qu'il est réutilisé entre les projets.

Vous pouvez également installer des commandes exécutables localement et les exécuter en utilisant [npx](https://flaviocopes.com/npx/), mais certains packages sont simplement mieux installés globalement.

De bons exemples de packages globaux populaires que vous pourriez connaître sont :

* `npm`
* `create-react-app`
* `vue-cli`
* `grunt-cli`
* `mocha`
* `react-native-cli`
* `gatsby-cli`
* `forever`
* `nodemon`

Vous avez probablement déjà certains packages installés globalement sur votre système. Vous pouvez les voir en exécutant :

```
npm list -g --depth 0
```

sur votre ligne de commande.

### Dépendances npm et devDependencies

Quand un package est-il une dépendance, et quand est-il une dépendance de développement ?

Lorsque vous installez un package npm en utilisant `npm install <package-name>`, vous l'installez **en tant que dépendance**.

Le package est automatiquement listé dans le fichier package.json, sous la liste `dependencies` (à partir de npm 5 : auparavant, vous deviez spécifier manuellement `--save`).

Lorsque vous ajoutez le flag `-D`, ou `--save-dev`, vous l'installez en tant que dépendance de développement, ce qui l'ajoute à la liste `devDependencies`.

Les **dépendances de développement** sont destinées à être des packages de développement uniquement, qui ne sont pas nécessaires en production. Par exemple, les packages de test, webpack ou Babel.

Lorsque vous passez **en production**, si vous tapez `npm install` et que le dossier contient un fichier `package.json`, ils sont installés, car npm suppose qu'il s'agit d'un déploiement de développement.

Vous devez définir le flag `--production` (`npm install --production`) pour éviter d'installer ces dépendances de développement.

### Le lanceur de packages Node npx

`npx` est une manière très intéressante d'exécuter les codes Node.js, et offre de nombreuses fonctionnalités utiles.

Dans cette section, je veux vous présenter une commande très puissante qui est disponible dans **npm** à partir de la version 5.2, publiée en juillet 2017 : **npx**.

Si vous ne souhaitez pas installer npm, vous pouvez installer npx en tant que [package autonome](https://www.npmjs.com/package/npx).

`npx` vous permet d'exécuter du code construit avec Node.js et publié via le registre npm.

#### Exécuter facilement des commandes locales

Les développeurs Node.js avaient l'habitude de publier la plupart des commandes exécutables en tant que packages globaux, afin qu'elles soient dans le chemin et exécutables immédiatement.

C'était une douleur car vous ne pouviez pas vraiment installer différentes versions de la même commande.

L'exécution de `npx commandname` trouve automatiquement la référence correcte de la commande à l'intérieur du dossier `node_modules` d'un projet, sans avoir besoin de connaître le chemin exact, et sans nécessiter que le package soit installé globalement et dans le chemin de l'utilisateur.

#### Exécution de commandes sans installation

Il y a une autre fonctionnalité géniale de `npm`, qui permet d'exécuter des commandes sans les installer au préalable.

C'est assez utile, principalement parce que :

1. vous n'avez pas besoin d'installer quoi que ce soit
2. vous pouvez exécuter différentes versions de la même commande, en utilisant la syntaxe `@version`

Une démonstration typique de l'utilisation de `npx` est la commande `cowsay`. `cowsay` imprimera une vache disant ce que vous avez écrit dans la commande. Par exemple :

`cowsay "Hello"` imprimera

```
 _______
< Hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Maintenant, cela fonctionne si vous avez la commande `cowsay` installée globalement depuis npm, sinon vous obtiendrez une erreur lorsque vous essayez d'exécuter la commande.

`npx` vous permet d'exécuter cette commande npm sans l'avoir installée localement :

```
npx cowsay "Hello"
```

Maintenant, c'est une commande amusante et inutile. D'autres scénarios incluent :

* exécuter l'outil CLI `vue` pour créer de nouvelles applications et les exécuter : `npx vue create my-vue-app`
* créer une nouvelle application React en utilisant `create-react-app` : `npx create-react-app my-react-app`

et bien d'autres.

Une fois téléchargé, le code téléchargé sera effacé.

#### Exécuter du code en utilisant une version différente de Node.js

Utilisez le `@` pour spécifier la version, et combinez cela avec le package npm `node` :

```
npx node@6 -v #v6.14.3
npx node@8 -v #v8.11.3
```

Cela aide à éviter des outils comme `nvm` ou les autres outils de gestion de versions de Node.

#### Exécuter des extraits de code arbitraires directement depuis une URL

`npx` ne vous limite pas aux packages publiés sur le registre npm.

Vous pouvez exécuter du code qui se trouve dans un [GitHub](https://flaviocopes.com/github/) gist, par exemple :

```
npx https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32
```

Bien sûr, vous devez être prudent lorsque vous exécutez du code que vous ne contrôlez pas, car avec un grand pouvoir vient une grande responsabilité.

### La boucle d'événements

La boucle d'événements est l'un des aspects les plus importants à comprendre sur JavaScript. Cette section explique les détails internes de la manière dont JavaScript fonctionne avec un seul thread, et comment il gère les fonctions asynchrones.

J'ai programmé pendant des années avec JavaScript, mais je n'ai jamais **complètement** compris comment les choses fonctionnent sous le capot. Il est tout à fait normal de ne pas connaître ce concept en détail. Mais comme d'habitude, il est utile de savoir comment cela fonctionne, et vous pourriez aussi être un peu curieux à ce stade.

Votre code JavaScript s'exécute en mono-thread. Il n'y a qu'une seule chose qui se passe à la fois.

C'est une limitation qui est en fait très utile, car elle simplifie beaucoup la manière dont vous programmez sans vous soucier des problèmes de concurrence.

Vous devez simplement faire attention à la manière dont vous écrivez votre code et éviter tout ce qui pourrait bloquer le thread, comme des appels réseau synchrones ou des boucles infinies.

Généralement, dans la plupart des navigateurs, il y a une boucle d'événements pour chaque onglet du navigateur, pour isoler chaque processus et éviter qu'une page web avec des boucles infinies ou un traitement lourd ne bloque tout votre navigateur.

L'environnement gère plusieurs boucles d'événements concurrentes, pour gérer les appels d'API par exemple. Les [Web Workers](https://flaviocopes.com/web-workers/) s'exécutent également dans leur propre boucle d'événements.

Vous devez principalement vous soucier que **votre code** s'exécutera sur une seule boucle d'événements, et écrire du code en gardant cela à l'esprit pour éviter de la bloquer.

#### Bloquer la boucle d'événements

Tout code JavaScript qui met trop de temps à rendre le contrôle à la boucle d'événements bloquera l'exécution de tout code JavaScript dans la page — même bloquera le thread de l'interface utilisateur — et l'utilisateur ne pourra pas cliquer, faire défiler la page, etc.

Presque toutes les primitives d'E/S en JavaScript sont non bloquantes. Les requêtes réseau, les opérations du système de fichiers Node.js, etc. Être bloquant est l'exception, et c'est pourquoi JavaScript est basé sur des callbacks, et plus récemment sur les promesses et async/await.

#### La pile d'appels

La pile d'appels est une file LIFO (Last In, First Out).

La boucle d'événements vérifie en continu la **pile d'appels** pour voir s'il y a une fonction qui doit s'exécuter.

En faisant cela, elle ajoute tout appel de fonction qu'elle trouve à la pile d'appels et les exécute chacun dans l'ordre.

Vous connaissez la trace de la pile d'erreurs à laquelle vous êtes peut-être familier, dans le débogueur ou dans la console du navigateur ?

Le navigateur recherche les noms de fonction dans la pile d'appels pour vous informer de la fonction qui origine l'appel actuel :

![Image](https://cdn-media-1.freecodecamp.org/images/SFxrWa7lVtAfUsjnjoMqgCGdG4bK0jDvi-11)

#### Une explication simple de la boucle d'événements

Prenons un exemple :

```js
const bar = () => console.log('bar')

const baz = () => console.log('baz')

const foo = () => {
  console.log('foo')
  bar()
  baz()
}

foo()

```

Ce code imprime :

```
foo
bar
baz
```

comme prévu.

Lorsque ce code s'exécute, `foo()` est d'abord appelé. À l'intérieur de `foo()`, nous appelons d'abord `bar()`, puis nous appelons `baz()`.

À ce stade, la pile d'appels ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bFPM-QZwRcB6APbq6sSJpyQMZHWRACvJzAly)

La boucle d'événements, à chaque itération, vérifie s'il y a quelque chose dans la pile d'appels, et l'exécute :

![Image](https://cdn-media-1.freecodecamp.org/images/T3jPPIkLHGvy0QXBrUz8cb3VM0bVVez-joQ4)

jusqu'à ce que la pile d'appels soit vide.

#### Mettre en file d'attente l'exécution de fonctions

L'exemple ci-dessus semble normal, il n'y a rien de spécial à ce sujet : JavaScript trouve des choses à exécuter, les exécute dans l'ordre.

Voyons comment différer une fonction jusqu'à ce que la pile soit claire.

Le cas d'utilisation de `setTimeout(() => {}), 0)` est d'appeler une fonction, mais de l'exécuter une fois que toutes les autres fonctions du code ont été exécutées.

Prenons cet exemple :

```js
const bar = () => console.log('bar')

const baz = () => console.log('baz')

const foo = () => {
  console.log('foo')
  setTimeout(bar, 0)
  baz()
}

foo()
```

Ce code imprime, peut-être de manière surprenante :

```
foo
baz
bar
```

Lorsque ce code s'exécute, `foo()` est d'abord appelé. À l'intérieur de `foo()`, nous appelons d'abord `setTimeout`, en passant `bar` comme argument, et nous lui demandons de s'exécuter immédiatement dès que possible, en passant `0` comme temporisateur. Ensuite, nous appelons `baz()`.

À ce stade, la pile d'appels ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/iUnlUVBLW8ozpE2ewbJswyp9tOP5OzPUXn0-)

Voici l'ordre d'exécution de toutes les fonctions de notre programme :

![Image](https://cdn-media-1.freecodecamp.org/images/MsT6C2UAZJaEEm6SmU266PO-V4b-DY0wlMqb)

Pourquoi cela se produit-il ?

#### La file d'attente des messages

Lorsque `setTimeout()` est appelé, le navigateur ou Node.js démarre le temporisateur. Une fois le temporisateur expiré, dans ce cas immédiatement car nous avons mis `0` comme délai, la fonction de rappel est placée dans la **file d'attente des messages**.

La file d'attente des messages est également l'endroit où les événements initiés par l'utilisateur comme les clics et les événements de clavier ou les réponses de fetch sont mis en file d'attente avant que votre code n'ait l'occasion de réagir à eux. Ou aussi les événements DOM comme `onLoad`.

La boucle donne la priorité à la pile d'appels. Elle traite d'abord tout ce qu'elle trouve dans la pile d'appels, et une fois qu'il n'y a plus rien là-bas, elle va chercher des choses dans la file d'attente des messages.

Nous n'avons pas à attendre des fonctions comme `setTimeout`, fetch ou autres pour faire leur propre travail, car elles sont fournies par le navigateur, et elles vivent sur leurs propres threads. Par exemple, si vous définissez le délai de `setTimeout` à 2 secondes, vous n'avez pas à attendre 2 secondes - l'attente se produit ailleurs.

#### File d'attente des tâches ES6

ECMAScript 2015 a introduit le concept de la file d'attente des tâches, qui est utilisée par les promesses (également introduites dans ES6/ES2015). C'est un moyen d'exécuter le résultat d'une fonction asynchrone dès que possible, plutôt que d'être placé à la fin de la pile d'appels.

Les promesses qui se résolvent avant la fin de la fonction actuelle seront exécutées juste après la fonction actuelle.

J'aime l'analogie d'un tour de montagnes russes dans un parc d'attractions : la file d'attente des messages vous replace dans la file d'attente après toutes les autres personnes dans la file d'attente, tandis que la file d'attente des tâches est le billet fastpass qui vous permet de faire un autre tour juste après avoir terminé le précédent.

Exemple :

```js
const bar = () => console.log('bar')

const baz = () => console.log('baz')

const foo = () => {
  console.log('foo')
  setTimeout(bar, 0)
  new Promise((resolve, reject) =>
    resolve('should be right after baz, before bar')
  ).then((resolve) => console.log(resolve))
  baz()
}

foo()

```

Cela imprime :

```
foo
baz
should be right after foo, before bar
bar
```

C'est une grande différence entre les promesses (et `async/await`, qui est construit sur les promesses) et les anciennes fonctions asynchrones via `setTimeout()` ou d'autres API de plateforme.

### Comprendre process.nextTick()

Alors que vous essayez de comprendre la boucle d'événements de Node.js, une partie importante de celle-ci est `process.nextTick()`. Elle interagit avec la boucle d'événements de manière spéciale.

Chaque fois que la boucle d'événements effectue un tour complet, nous l'appelons un tick.

Lorsque nous passons une fonction à `process.nextTick()`, nous instruisons le moteur de l'invoquer à la fin de l'opération actuelle, avant que le prochain tick de la boucle d'événements ne commence :

```js
process.nextTick(() => {
  // faire quelque chose
})

```

La boucle d'événements est occupée à traiter le code de la fonction actuelle.

Lorsque cette opération se termine, le moteur JavaScript exécute toutes les fonctions passées aux appels `nextTick` pendant cette opération.

C'est la manière dont nous pouvons dire au moteur JavaScript de traiter une fonction de manière asynchrone (après la fonction actuelle), mais dès que possible, sans la mettre en file d'attente.

Appeler `setTimeout(() => {}, 0)` exécutera la fonction au prochain tick, bien plus tard que lorsque vous utilisez `nextTick()`.

Utilisez `nextTick()` lorsque vous voulez vous assurer que dans la prochaine itération de la boucle d'événements, ce code est déjà exécuté.

### Comprendre setImmediate()

Lorsque vous souhaitez exécuter un morceau de code de manière asynchrone, mais dès que possible, une option est d'utiliser la fonction `setImmediate()` fournie par Node.js :

```js
setImmediate(() => {
  // exécuter quelque chose
})

```

Toute fonction passée en tant qu'argument de `setImmediate()` est un rappel qui est exécuté dans la prochaine itération de la boucle d'événements.

En quoi `setImmediate()` est-il différent de `setTimeout(() => {}, 0)` (en passant un délai de 0ms), et de `process.nextTick()` ?

Une fonction passée à `process.nextTick()` sera exécutée dans l'itération actuelle de la boucle d'événements, après la fin de l'opération actuelle. Cela signifie qu'elle sera toujours exécutée avant `setTimeout()` et `setImmediate()`.

Un rappel `setTimeout()` avec un délai de 0ms est très similaire à `setImmediate()`. L'ordre d'exécution dépendra de divers facteurs, mais ils seront tous deux exécutés dans la prochaine itération de la boucle d'événements.

### Minuteries

Lorsque vous écrivez du code JavaScript, vous pouvez vouloir retarder l'exécution d'une fonction. Apprenez à utiliser `setTimeout()` et `setInterval()` pour planifier des fonctions dans le futur.

#### `setTimeout()`

Lorsque vous écrivez du code JavaScript, vous pouvez vouloir retarder l'exécution d'une fonction. C'est le rôle de `setTimeout`.

Vous pouvez spécifier une fonction de rappel à exécuter plus tard, et une valeur exprimant combien de temps plus tard vous voulez qu'elle s'exécute, en millisecondes :

```js
setTimeout(() => {
  // s'exécute après 2 secondes
}, 2000)

setTimeout(() => {
  // s'exécute après 50 millisecondes
}, 50)

```

Cette syntaxe définit une nouvelle fonction. Vous pouvez appeler n'importe quelle autre fonction que vous voulez là-dedans, ou vous pouvez passer un nom de fonction existant, et un ensemble de paramètres :

```js
const myFunction = (firstParam, secondParam) => {
  // faire quelque chose
}

// s'exécute après 2 secondes
setTimeout(myFunction, 2000, firstParam, secondParam)
```

`setTimeout()` retourne l'identifiant de la minuterie. Cela est généralement non utilisé, mais vous pouvez stocker cet identifiant, et le supprimer si vous voulez annuler cette exécution de fonction planifiée :

```js
const id = setTimeout(() => {
  // devrait s'exécuter après 2 secondes
}, 2000)

// J'ai changé d'avis
clearTimeout(id)
```

#### Délai zéro

Si vous spécifiez le délai de la minuterie à `0`, la fonction de rappel sera exécutée dès que possible, mais après l'exécution de la fonction actuelle :

```js
setTimeout(() => {
  console.log('after ')
}, 0)

console.log(' before ')

```

imprimera `before after`.

Cela est particulièrement utile pour éviter de bloquer le CPU sur des tâches intensives et permettre à d'autres fonctions de s'exécuter tout en effectuant un calcul lourd, en mettant en file d'attente des fonctions dans le planificateur.

Certains navigateurs (IE et Edge) implémentent une méthode `setImmediate()` qui fait exactement cette même fonctionnalité, mais ce n'est pas standard et [indisponible sur d'autres navigateurs](https://caniuse.com/#feat=setimmediate). Mais c'est une fonction standard dans Node.js.

#### `setInterval()`

`setInterval()` est une fonction similaire à `setTimeout()` avec une différence. Au lieu d'exécuter la fonction de rappel une fois, elle l'exécutera indéfiniment, à l'intervalle de temps spécifique que vous spécifiez (en millisecondes) :

```js
setInterval(() => {
  // s'exécute toutes les 2 secondes
}, 2000)

```

La fonction ci-dessus s'exécute toutes les 2 secondes sauf si vous lui dites de s'arrêter, en utilisant `clearInterval`, en lui passant l'identifiant de l'intervalle que `setInterval` a retourné :

```js
const id = setInterval(() => {
  // s'exécute toutes les 2 secondes
}, 2000)

clearInterval(id)

```

Il est courant d'appeler `clearInterval` à l'intérieur de la fonction de rappel `setInterval`, pour lui permettre de déterminer automatiquement si elle doit s'exécuter à nouveau ou s'arrêter. Par exemple, ce code exécute quelque chose sauf si `App.somethingIWait` a la valeur `arrived` :

```js
const interval = setInterval(() => {
  if (App.somethingIWait === 'arrived') {
    clearInterval(interval)
    return
  }
  // sinon faire des choses
}, 100)

```

#### setTimeout récursif

`setInterval` démarre une fonction toutes les `n` millisecondes, sans aucune considération pour le moment où une fonction a terminé son exécution.

Si une fonction prend toujours le même temps, tout va bien :

![Image](https://cdn-media-1.freecodecamp.org/images/eyf875I-cxYqAgNDSeh7CeLg4RXdJIgJphEw)

Peut-être que la fonction prend des temps d'exécution différents, selon les conditions réseau par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/ge2DPdTuZwHnJIyUH9VSLok1J5WHPOlc1DML)

Et peut-être qu'une longue exécution chevauche la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/I9kJc6l-BIT850OGlNDJre80RcsLp7N4amvy)

Pour éviter cela, vous pouvez planifier un setTimeout récursif pour qu'il soit appelé lorsque la fonction de rappel se termine :

```js
const myFunction = () => {
  // faire quelque chose
  setTimeout(myFunction, 1000)
}

setTimeout(
  myFunction()
}, 1000)

```

pour atteindre ce scénario :

![Image](https://cdn-media-1.freecodecamp.org/images/B2kod2dFuR5U1uwaaW9SGiC1zX5gIUEaiJ8A)

`setTimeout` et `setInterval` sont également disponibles dans Node.js, via le [module Timers](https://nodejs.org/api/timers.html).

Node.js fournit également `setImmediate()`, qui est équivalent à utiliser `setTimeout(() => {}, 0)`, principalement utilisé pour travailler avec la boucle d'événements de Node.js.

### Programmation asynchrone et callbacks

JavaScript est synchrone par défaut et est mono-threadé. Cela signifie que le code ne peut pas créer de nouveaux threads et s'exécuter en parallèle.

#### Asynchronicité dans les langages de programmation

Les ordinateurs sont asynchrones par conception.

Asynchrone signifie que les choses peuvent se produire indépendamment du flux principal du programme.

Dans les ordinateurs grand public actuels, chaque programme s'exécute pendant un créneau horaire spécifique, puis il arrête son exécution pour laisser un autre programme continuer son exécution. Ce processus se déroule dans un cycle si rapide qu'il est impossible de le remarquer, et nous pensons que nos ordinateurs exécutent de nombreux programmes simultanément, mais c'est une illusion (sauf sur les machines multiprocesseurs).

Les programmes utilisent en interne des **interruptions**, un signal émis au processeur pour attirer l'attention du système.

Je ne vais pas entrer dans les détails internes de cela, mais gardez simplement à l'esprit qu'il est normal pour les programmes d'être asynchrones, et d'interrompre leur exécution jusqu'à ce qu'ils aient besoin d'attention, et l'ordinateur peut exécuter d'autres choses en attendant. Lorsqu'un programme attend une réponse du réseau, il ne peut pas bloquer le processeur jusqu'à ce que la requête se termine.

Normalement, les langages de programmation sont synchrones, et certains fournissent un moyen de gérer l'asynchronicité, dans le langage ou via des bibliothèques. C, Java, C#, PHP, Go, Ruby, Swift, Python, ils sont tous synchrones par défaut. Certains d'entre eux gèrent l'asynchronicité en utilisant des threads, en créant un nouveau processus.

#### JavaScript

JavaScript est **synchrone** par défaut et est mono-threadé. Cela signifie que le code ne peut pas créer de nouveaux threads et s'exécuter en parallèle.

Les lignes de code sont exécutées en série, les unes après les autres.

Par exemple :

```js
const a = 1
const b = 2
const c = a * b
console.log(c)
doSomething()

```

Mais JavaScript est né à l'intérieur du navigateur. Son travail principal, au début, était de répondre aux actions de l'utilisateur comme `onClick`, `onMouseOver`, `onChange`, `onSubmit` et ainsi de suite. Comment pouvait-il faire cela avec un modèle de programmation synchrone ?

La réponse se trouvait dans son environnement. Le **navigateur** fournit un moyen de le faire en fournissant un ensemble d'API qui peuvent gérer ce type de fonctionnalité.

Plus récemment, Node.js a introduit un environnement d'E/S non bloquant pour étendre ce concept à l'accès aux fichiers, aux appels réseau et ainsi de suite.

#### Callbacks

Vous ne pouvez pas savoir quand un utilisateur va cliquer sur un bouton, donc ce que vous faites est **définir un gestionnaire d'événements pour l'événement de clic**.

Ce gestionnaire d'événements accepte une fonction, qui sera appelée lorsque l'événement est déclenché :

```js
document.getElementById('button').addEventListener('click', () => {
  // élément cliqué
})

```

C'est ce qu'on appelle le **callback**.

Un callback est une simple fonction qui est passée en tant que valeur à une autre fonction, et qui ne sera exécutée que lorsque l'événement se produira. Nous pouvons faire cela parce que JavaScript a des fonctions de première classe, qui peuvent être assignées à des variables et passées à d'autres fonctions (appelées **fonctions d'ordre supérieur**)

Il est courant d'envelopper tout votre code client dans un écouteur d'événement `load` sur l'objet `window`, qui exécute la fonction de rappel uniquement lorsque la page est prête :

```js
window.addEventListener('load', () => {
  // fenêtre chargée
  // faire ce que vous voulez
})

```

Les callbacks sont utilisés partout, pas seulement dans les événements DOM.

Un exemple courant est l'utilisation de timers :

```js
setTimeout(() => {
  // s'exécute après 2 secondes
}, 2000)

```

Les [requêtes XHR](https://en.wikipedia.org/wiki/XMLHttpRequest) acceptent également un callback, dans cet exemple en assignant une fonction à une propriété qui sera appelée lorsqu'un événement particulier se produit (dans ce cas, l'état de la requête change) :

```js
const xhr = new XMLHttpRequest()
xhr.onreadystatechange = () => {
  if (xhr.readyState === 4) {
  xhr.status === 200 ? console.log(xhr.responseText) : console.error('error')
  }
}

xhr.open('GET', 'https://yoursite.com')
xhr.send()

```

#### Gestion des erreurs dans les callbacks

Comment gérez-vous les erreurs avec les callbacks ? Une stratégie très courante est d'utiliser ce que Node.js a adopté : le premier paramètre de toute fonction de callback est l'objet d'erreur — les callbacks « error-first ».

Si il n'y a pas d'erreur, l'objet est `null`. Si il y a une erreur, il contient une description de l'erreur et d'autres informations.

```js
fs.readFile('/file.json', (err, data) => {
  if (err !== null) {
    // gérer l'erreur
    console.log(err)
    return
  }
  
  // pas d'erreurs, traiter les données
  console.log(data)
})

```

#### Le problème avec les callbacks

Les callbacks sont géniaux pour les cas simples !

Cependant, chaque callback ajoute un niveau d'imbrication. Lorsque vous avez beaucoup de callbacks, le code commence à devenir compliqué très rapidement :

```js 
window.addEventListener('load', () => {
  document.getElementById('button').addEventListener('click', () => {
    setTimeout(() => {
      items.forEach(item => {
        // votre code ici
      })
    }, 2000)
  })
})

```

Ce n'est qu'un simple code à 4 niveaux, mais j'ai vu beaucoup plus de niveaux d'imbrication et ce n'est pas amusant.

Comment résoudre ce problème ?

#### Alternatives aux callbacks

À partir de ES6, JavaScript a introduit plusieurs fonctionnalités qui nous aident avec le code asynchrone qui n'impliquent pas l'utilisation de callbacks :

* Promesses (ES6)
* Async/Await (ES8)

### Promesses

Les promesses sont un moyen de gérer le code asynchrone en JavaScript, sans écrire trop de callbacks dans votre code.

#### Introduction aux promesses

Une promesse est communément définie comme **un proxy pour une valeur qui deviendra éventuellement disponible**.

Bien qu'elles existent depuis des années, elles ont été standardisées et introduites dans ES2015, et maintenant elles ont été remplacées dans ES2017 par les fonctions asynchrones.

Les **fonctions asynchrones** utilisent l'API des promesses comme leur bloc de construction, donc les comprendre est fondamental même si dans le nouveau code vous utiliserez probablement des fonctions asynchrones au lieu des promesses.

#### Comment fonctionnent les promesses, en bref

Une fois qu'une promesse a été appelée, elle commence dans un **état en attente**. Cela signifie que la fonction appelante continue l'exécution, tandis qu'elle attend que la promesse effectue son propre traitement, et donne un retour à la fonction appelante.

À ce stade, la fonction appelante attend qu'elle retourne la promesse dans un **état résolu**, ou dans un **état rejeté**, mais comme vous le savez, JavaScript est asynchrone — donc la fonction continue son exécution pendant que la promesse fait son travail.

#### Quelles API JS utilisent les promesses ?

En plus de votre propre code et du code des bibliothèques, les promesses sont utilisées par les API Web modernes standard telles que :

* **_l'API Battery_**
* l'[API Fetch](https://flaviocopes.com/fetch-api/)
* [Service Workers](https://flaviocopes.com/service-workers/)

Il est peu probable que dans le JavaScript moderne vous vous retrouviez **à ne pas** utiliser les promesses, alors commençons à plonger directement dedans.

#### Créer une promesse

L'API Promise expose un constructeur Promise, que vous initialisez en utilisant `new Promise()` :

```js
let done = true

const isItDoneYet = new Promise((resolve, reject) => {
  if (done) {
    const workDone = 'Here is the thing I built'
    resolve(workDone)
  } else {
    const why = 'Still working on something else'
    reject(why)
  }
})

```

Comme vous pouvez le voir, la promesse vérifie la constante globale `done`, et si celle-ci est vraie, nous retournons une promesse résolue, sinon une promesse rejetée.

En utilisant `resolve` et `reject`, nous pouvons communiquer une valeur en retour, dans l'exemple ci-dessus, nous retournons simplement une chaîne, mais cela pourrait être un objet également.

#### Consommer une promesse

Dans la dernière section, nous avons introduit comment une promesse est créée.

Maintenant, voyons comment la promesse peut être **consommée** ou utilisée :

```js
const isItDoneYet = new Promise()
//...

const checkIfItsDone = () => {
  isItDoneYet
    .then((ok) => {
      console.log(ok)
    })
    .catch((err) => {
      console.error(err)
    })
}

```

L'exécution de `checkIfItsDone()` exécutera la promesse `isItDoneYet()` et attendra qu'elle se résolve, en utilisant le rappel `then`, et s'il y a une erreur, elle la gérera dans le rappel `catch`.

#### Chaînage des promesses

Une promesse peut être retournée à une autre promesse, créant ainsi une chaîne de promesses.

Un excellent exemple de chaînage de promesses est donné par l'[API Fetch](https://flaviocopes.com/fetch-api), une couche au-dessus de l'API `XMLHttpRequest`, que nous pouvons utiliser pour obtenir une ressource et mettre en file d'attente une chaîne de promesses à exécuter lorsque la ressource est récupérée.

L'API Fetch est un mécanisme basé sur les promesses, et l'appel à `fetch()` est équivalent à définir notre propre promesse en utilisant `new Promise()`.

#### Exemple de chaînage de promesses

```js
const status = (response) => {
  if (response.status >= 200 && response.status < 300) {
    return Promise.resolve(response)
  }
  return Promise.reject(new Error(response.statusText))
}

const json = (response) => response.json()

fetch('/todos.json')
  .then(status)
  .then(json)
  .then((data) => {
    console.log('Request succeeded with JSON response', data)
  })
  .catch((error) => {
    console.log('Request failed', error)
  })

```

Dans cet exemple, nous appelons `fetch()` pour obtenir une liste d'éléments TODO à partir du fichier `todos.json` trouvé à la racine du domaine, et nous créons une chaîne de promesses.

L'exécution de `fetch()` retourne une [réponse](https://fetch.spec.whatwg.org/#concept-response), qui a de nombreuses propriétés, et parmi celles-ci nous référençons :

* `status`, une valeur numérique représentant le code de statut HTTP
* `statusText`, un message de statut, qui est `OK` si la requête a réussi

`response` a également une méthode `json()`, qui retourne une promesse qui se résoudra avec le contenu du corps traité et transformé en JSON.

Étant donné ces prémisses, voici ce qui se passe : la première promesse de la chaîne est une fonction que nous avons définie, appelée `status()`, qui vérifie le statut de la réponse et si ce n'est pas une réponse de succès (entre 200 et 299), elle rejette la promesse.

Cette opération fera en sorte que la chaîne de promesses saute toutes les promesses enchaînées listées et passera directement à l'instruction `catch()` en bas, enregistrant le texte `Request failed` ainsi que le message d'erreur.

Si cela réussit, elle appelle la fonction `json()` que nous avons définie. Puisque la promesse précédente, lorsqu'elle est réussie, a retourné l'objet `response`, nous le recevons en entrée de la deuxième promesse.

Dans ce cas, nous retournons les données JSON traitées, donc la troisième promesse reçoit le JSON directement :

```js
.then((data) => {
  console.log('Request succeeded with JSON response', data)
})
```

et nous l'affichons simplement dans la console.

#### Gestion des erreurs

Dans l'exemple, dans la section précédente, nous avions un `catch` qui était ajouté à la chaîne de promesses.

Lorsque quelque chose dans la chaîne de promesses échoue et lève une erreur ou rejette la promesse, le contrôle passe au `catch()` le plus proche en bas de la chaîne.

```js
new Promise((resolve, reject) => {
  throw new Error('Error')
}).catch((err) => {
  console.error(err)
})

// ou

new Promise((resolve, reject) => {
  reject('Error')
}).catch((err) => {
  console.error(err)
})

```

#### Erreurs en cascade

Si à l'intérieur du `catch()` vous levez une erreur, vous pouvez ajouter un second `catch()` pour la gérer, et ainsi de suite.

```js
new Promise((resolve, reject) => {
  throw new Error('Error')
})
  .catch((err) => {
    throw new Error('Error')
  })
  .catch((err) => {
    console.error(err)
  })

```

### Orchestration des promesses

#### `Promise.all()`

Si vous devez synchroniser différentes promesses, `Promise.all()` vous aide à définir une liste de promesses, et à exécuter quelque chose lorsqu'elles sont toutes résolues.

Exemple :

```js
const f1 = fetch('/something.json')
const f2 = fetch('/something2.json')

Promise.all([f1, f2])
  .then((res) => {
    console.log('Array of results', res)
  })
  .catch((err) => {
    console.error(err)
  })

```

La syntaxe d'affectation de déstructuration [ES2015](https://flaviocopes.com/ecmascript/#destructuring-assignments) permet également de faire :

```js
Promise.all([f1, f2]).then(([res1, res2]) => {
  console.log('Results', res1, res2)
})

```

Vous n'êtes pas limité à utiliser `fetch` bien sûr, **toute promesse est bonne à prendre**.

#### `Promise.race()`

`Promise.race()` s'exécute lorsque la première des promesses que vous lui passez est résolue, et elle exécute le rappel attaché une seule fois, avec le résultat de la première promesse résolue.

Exemple :

```js
const promiseOne = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, 'one')
})

const promiseTwo = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'two')
})

Promise.race([promiseOne, promiseTwo]).then((result) => {
  console.log(result) // 'two'
})

```

#### Erreur courante, Uncaught TypeError: undefined is not a promise

Si vous obtenez l'erreur `Uncaught TypeError: undefined is not a promise` dans la console, assurez-vous d'utiliser `new Promise()` au lieu de simplement `Promise()`.

### Async et Await

Découvrez l'approche moderne des fonctions asynchrones en JavaScript.

JavaScript a évolué très rapidement des callbacks aux promesses (ES2015), et depuis ES2017, JavaScript asynchrone est encore plus simple avec la syntaxe async/await.

Les fonctions async sont une combinaison de promesses et de générateurs, et en gros, elles sont une abstraction de plus haut niveau sur les promesses. Laissez-moi répéter : `async/await` est construit sur les promesses.

#### Pourquoi async/await a-t-il été introduit ?

Ils réduisent le code répétitif autour des promesses, et la limitation « ne pas rompre la chaîne » de l'enchaînement des promesses.

Lorsque les promesses ont été introduites dans ES2015, elles étaient destinées à résoudre un problème avec le code asynchrone, et elles l'ont fait, mais au cours des 2 années qui ont séparé ES2015 et ES2017, il était clair que les promesses ne pouvaient pas être la solution finale.

Les promesses ont été introduites pour résoudre le célèbre problème de l'enfer des callbacks, mais elles ont introduit leur propre complexité et complexité syntaxique.

Elles étaient de bonnes primitives autour desquelles une meilleure syntaxe pouvait être exposée aux développeurs, donc lorsque le moment était venu, nous avons obtenu les **fonctions async**.

Elles font en sorte que le code semble synchrone, mais il est asynchrone et non bloquant en arrière-plan.

#### Comment cela fonctionne

Une fonction `async` retourne une promesse, comme dans cet exemple :

```js
const doSomethingAsync = () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve('I did something'), 3000)
  })
}

```

Lorsque vous voulez appeler cette fonction, vous préfixez `await`, et le code appelant s'arrêtera **jusqu'à ce que la promesse soit résolue ou rejetée**. Un bémol : la fonction cliente doit être définie comme `async`.

Voici un exemple :

```js
const doSomething = async () => {
  console.log(await doSomethingAsync())
}

```

#### Un exemple rapide

Voici un exemple simple de `async/await` utilisé pour exécuter une fonction de manière asynchrone :

```js
const doSomethingAsync = () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve('I did something'), 3000)
  })
}

const doSomething = async () => {
  console.log(await doSomethingAsync())
}

console.log('Before')
doSomething()
console.log('After')

```

Le code ci-dessus imprimera ce qui suit dans la console du navigateur :

```
Before
After
I did something // après 3s

```

#### Promettre toutes les choses

Préfixer le mot-clé `async` à n'importe quelle fonction signifie que la fonction retournera une promesse.

Même si elle ne le fait pas explicitement, elle la fera retourner une promesse en interne.

C'est pourquoi ce code est valide :

```
const aFunction = async () => {
  return 'test'
}

aFunction().then(alert) // Cela alertera 'test'

```

et c'est la même chose que :

```js
const aFunction = async () => {
  return Promise.resolve('test')
}

aFunction().then(alert) // Cela alertera 'test'

```

#### Le code est beaucoup plus simple à lire

Comme vous pouvez le voir dans l'exemple ci-dessus, notre code semble très simple. Comparez-le au code utilisant des promesses simples, avec des chaînes et des fonctions de rappel.

Et ceci est un exemple très simple, les principaux avantages apparaîtront lorsque le code sera beaucoup plus complexe.

Par exemple, voici comment vous obtiendriez une ressource JSON et la parseriez, en utilisant des promesses :

```js
const getFirstUserData = () => {
  return fetch('/users.json') // obtenir la liste des utilisateurs
    .then((response) => response.json()) // parser JSON
    .then((users) => users[0]) // choisir le premier utilisateur
    .then((user) => fetch(`/users/${user.name}`)) // obtenir les données de l'utilisateur
    .then((userResponse) => userResponse.json()) // parser JSON
}

getFirstUserData()
```

Et voici la même fonctionnalité fournie en utilisant `await/async` :

```js
const getFirstUserData = async () => {
  const response = await fetch('/users.json') // obtenir la liste des utilisateurs
  const users = await response.json() // parser JSON
  const user = users[0] // choisir le premier utilisateur
  const userResponse = await fetch(`/users/${user.name}`) // obtenir les données de l'utilisateur
  const userData = await userResponse.json() // parser JSON
  return userData
}

getFirstUserData()

```

#### Plusieurs fonctions async en série

Les fonctions `async` peuvent être enchaînées très facilement, et la syntaxe est beaucoup plus lisible qu'avec les promesses simples :

```js
const promiseToDoSomething = () => {
  return new Promise(resolve => {
    setTimeout(() => resolve('I did something'), 10000)
  })
}

const watchOverSomeoneDoingSomething = async () => {
  const something = await promiseToDoSomething()
  return something + ' and I watched'
}

const watchOverSomeoneWatchingSomeoneDoingSomething = async () => {
  const something = await watchOverSomeoneDoingSomething()
  return something + ' and I watched as well'
}

watchOverSomeoneWatchingSomeoneDoingSomething().then(res => {
  console.log(res)
})

```

Imprimera :

```
I did something and I watched and I watched as well
```

#### Débogage plus facile

Le débogage des promesses est difficile car le débogueur ne passera pas sur le code asynchrone.

`async/await` rend cela très facile car pour le compilateur, c'est comme du code synchrone.

### L'émetteur d'événements Node.js

Vous pouvez travailler avec des événements personnalisés dans Node.js.

Si vous avez travaillé avec JavaScript dans le navigateur, vous savez à quel point l'interaction de l'utilisateur est gérée par des événements : clics de souris, pressions de touches du clavier, réactions aux mouvements de la souris, et ainsi de suite.

Du côté backend, Node.js nous offre la possibilité de construire un système similaire en utilisant le module `events`.

Ce module, en particulier, offre la classe `EventEmitter`, que nous utiliserons pour gérer nos événements.

Vous l'initialisez en utilisant :

```js
const EventEmitter = require('events')
const eventEmitter = new EventEmitter()

```

Cet objet expose, entre autres, les méthodes `on` et `emit`.

* `emit` est utilisé pour déclencher un événement
* `on` est utilisé pour ajouter une fonction de rappel qui sera exécutée lorsque l'événement est déclenché

Par exemple, créons un événement `start`, et à titre d'exemple, nous réagissons à celui-ci en nous contentant de journaliser dans la console :

```js
eventEmitter.on('start', () => {
  console.log('started')
})

```

Lorsque nous exécutons :

```js
eventEmitter.emit('start')
```

La fonction de gestionnaire d'événements est déclenchée, et nous obtenons la journalisation de la console.

**Note :** `addListener()` est un alias pour `on()`, au cas où vous verriez cela utilisé.

#### Passer des arguments à l'événement

Vous pouvez passer des arguments au gestionnaire d'événements en les passant comme arguments supplémentaires à `emit()` :

```js
eventEmitter.on('start', (number) => {
  console.log(`started ${number}`)
})

eventEmitter.emit('start', 23)

```

Plusieurs arguments :

```js
eventEmitter.on('start', (start, end) => {
  console.log(`started from ${start} to ${end}`)
})

eventEmitter.emit('start', 1, 100)

```

L'objet EventEmitter expose également plusieurs autres méthodes pour interagir avec les événements, comme :

* `once()` : ajoute un écouteur ponctuel
* `removeListener()` / `off()` : supprime un écouteur d'événement d'un événement
* `removeAllListeners()` : supprime tous les écouteurs d'un événement

### Comment fonctionnent les requêtes HTTP

Que se passe-t-il lorsque vous tapez une URL dans le navigateur, du début à la fin ?

Cette section décrit comment les navigateurs effectuent les requêtes de pages en utilisant le protocole HTTP/1.1.

Si vous avez déjà passé un entretien, vous avez peut-être été interrogé : « Que se passe-t-il lorsque vous tapez quelque chose dans la boîte de recherche Google et que vous appuyez sur entrée ? ».

C'est l'une des questions les plus populaires qui vous sont posées. Les gens veulent simplement voir si vous pouvez expliquer certains concepts plutôt basiques et si vous avez une idée de la manière dont Internet fonctionne réellement.

Dans cette section, j'analyserai ce qui se passe lorsque vous tapez une URL dans la barre d'adresse de votre navigateur et que vous appuyez sur entrée.

C'est un sujet très intéressant à disséquer dans ce manuel, car il touche à de nombreuses technologies que je peux approfondir dans des articles séparés.

C'est une technologie qui est très rarement modifiée, et qui alimente l'un des écosystèmes les plus complexes et les plus vastes jamais construits par l'homme.

### Le protocole HTTP

J'analyse uniquement les requêtes d'URL.

Les navigateurs modernes ont la capacité de savoir si ce que vous avez écrit dans la barre d'adresse est une URL réelle ou un terme de recherche, et ils utiliseront le moteur de recherche par défaut si ce n'est pas une URL valide.

Je suppose que vous tapez une URL réelle.

Lorsque vous entrez l'URL et appuyez sur entrée, le navigateur construit d'abord l'URL complète.

Si vous avez simplement entré un domaine, comme `flaviocopes.com`, le navigateur par défaut préfixera `HTTP://` à celui-ci, en utilisant le protocole HTTP par défaut.

#### Choses liées à macOS / Linux

Juste pour votre information. Windows pourrait faire certaines choses légèrement différemment.

#### Phase de recherche DNS

Le navigateur commence la recherche DNS pour obtenir l'adresse IP du serveur.

Le nom de domaine est un raccourci pratique pour nous, humains, mais Internet est organisé de telle sorte que les ordinateurs peuvent trouver l'emplacement exact d'un serveur via son adresse IP, qui est un ensemble de chiffres comme `222.324.3.1` (IPv4).

Tout d'abord, il vérifie le cache DNS local, pour voir si le domaine a déjà été résolu récemment.

**_Chrome dispose d'un visualiseur de cache DNS pratique que vous pouvez voir à cette URL : chrome://net-internals/#dns (copiez et collez-la dans la barre d'adresse du navigateur Chrome)_**

Si rien n'est trouvé là, le navigateur utilise le résolveur DNS, en utilisant l'appel système POSIX `gethostbyname` pour récupérer les informations de l'hôte.

#### gethostbyname

`gethostbyname` recherche d'abord dans le fichier hosts local, qui sur macOS ou Linux est situé dans `/etc/hosts`, pour voir si le système fournit les informations localement.

Si cela ne donne aucune information sur le domaine, le système fait une requête au serveur DNS.

L'adresse du serveur DNS est stockée dans les préférences système.

Voici 2 serveurs DNS populaires :

* `8.8.8.8` : le serveur DNS public de Google
* `1.1.1.1` : le serveur DNS de CloudFlare

La plupart des gens utilisent le serveur DNS fourni par leur fournisseur d'accès Internet.

Le navigateur effectue la requête DNS en utilisant le protocole UDP.

TCP et UDP sont deux des protocoles fondamentaux de la mise en réseau informatique. Ils se situent au même niveau conceptuel, mais TCP est orienté connexion, tandis que UDP est un protocole sans connexion, plus léger, utilisé pour envoyer des messages avec peu de surcharge.

Comment la requête UDP est effectuée n'est pas dans le cadre de ce manuel.

Le serveur DNS peut avoir l'IP du domaine dans le cache. Sinon, il demandera au **serveur DNS racine**. C'est un système (composé de 13 serveurs réels, répartis sur la planète) qui pilote tout l'internet.

Le serveur DNS ne **connaît pas** l'adresse de chaque nom de domaine sur la planète.

Ce qu'il connaît, ce sont les emplacements des **résolveurs DNS de premier niveau**.

Un domaine de premier niveau est l'extension de domaine : `.com`, `.it`, `.pizza` et ainsi de suite.

Une fois que le serveur DNS racine reçoit la requête, il transmet la requête à ce serveur DNS de domaine de premier niveau (TLD).

Disons que vous cherchez `flaviocopes.com`. Le serveur DNS de domaine racine retourne l'IP du serveur TLD .com.

Notre résolveur DNS mettra en cache l'IP de ce serveur TLD, afin de ne pas avoir à redemander au serveur DNS racine.

Le serveur DNS TLD aura les adresses IP des serveurs de noms faisant autorité pour le domaine que nous recherchons.

Comment ? Lorsque vous achetez un domaine, le bureau d'enregistrement du domaine envoie le serveur TLD approprié les serveurs de noms. Lorsque vous mettez à jour les serveurs de noms (par exemple, lorsque vous changez de fournisseur d'hébergement), cette information sera automatiquement mise à jour par votre bureau d'enregistrement de domaine.

Ce sont les serveurs DNS du fournisseur d'hébergement. Ils sont généralement plus d'un, pour servir de sauvegarde.

Par exemple :

* `ns1.dreamhost.com`
* `ns2.dreamhost.com`
* `ns3.dreamhost.com`

Le résolveur DNS commence par le premier, et essaie de demander l'IP du domaine (avec le sous-domaine, aussi) que vous recherchez.

C'est la source ultime de vérité pour l'adresse IP.

Maintenant que nous avons l'adresse IP, nous pouvons continuer notre voyage.

#### Poignée de main de la requête TCP

Avec l'adresse IP du serveur disponible, le navigateur peut maintenant initier une connexion TCP à celle-ci.

Une connexion TCP nécessite un peu de poignée de main avant de pouvoir être pleinement initialisée et de commencer à envoyer des données.

Une fois la connexion établie, nous pouvons envoyer la requête

#### Envoyer la requête

La requête est un document en texte brut structuré de manière précise déterminée par le protocole de communication.

Elle est composée de 3 parties :

* la ligne de requête
* l'en-tête de requête
* le corps de requête

#### La ligne de requête

La ligne de requête définit, sur une seule ligne :

* la méthode HTTP
* l'emplacement de la ressource
* la version du protocole

Exemple :

```
GET / HTTP/1.1
```

#### L'en-tête de requête

L'en-tête de requête est un ensemble de paires `champ: valeur` qui définissent certaines valeurs.

Il y a 2 champs obligatoires, dont l'un est `Host`, et l'autre est `Connection`, tandis que tous les autres champs sont optionnels :

```
Host: flaviocopes.com
Connection: close

```

`Host` indique le nom de domaine que nous voulons cibler, tandis que `Connection` est toujours défini sur `close` sauf si la connexion doit être maintenue ouverte.

Certains des champs d'en-tête les plus utilisés sont :

* `Origin`
* `Accept`
* `Accept-Encoding`
* `Cookie`
* `Cache-Control`
* `Dnt`

mais beaucoup d'autres existent.

La partie en-tête est terminée par une ligne vide.

#### Le corps de la requête

Le corps de la requête est facultatif, non utilisé dans les requêtes GET mais très utilisé dans les requêtes POST et parfois dans d'autres verbes aussi, et il peut contenir des données au format JSON.

Puisque nous analysons maintenant une requête GET, le corps est vide et nous ne regarderons pas plus loin.

#### La réponse

Une fois la requête envoyée, le serveur la traite et envoie une réponse.

La réponse commence par le code de statut et le message de statut. Si la requête est réussie et retourne un 200, elle commencera par :

```
200 OK
```

La requête peut retourner un code de statut et un message différents, comme l'un de ceux-ci :

```
404 Not Found
403 Forbidden
301 Moved Permanently
500 Internal Server Error
304 Not Modified
401 Unauthorized

```

La réponse contient ensuite une liste d'en-têtes HTTP et le corps de la réponse (qui, puisque nous faisons la requête dans le navigateur, sera du HTML).

#### Analyser le HTML

Le navigateur a maintenant reçu le HTML et commence à le parser, et répétera le même processus que nous avons fait pour toutes les ressources requises par la page :

* Fichiers CSS
* images
* la favicon
* Fichiers JavaScript
* …

Comment les navigateurs rendent la page ensuite est hors du cadre, mais il est important de comprendre que le processus que j'ai décrit n'est pas seulement pour les pages HTML, mais pour tout élément qui est servi via HTTP.

### Construire un serveur HTTP avec Node.js

Voici le serveur web HTTP que nous avons utilisé comme application Hello World Node.js dans l'introduction :

```js
const http = require('http')

const hostname = 'localhost'
const port = 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World\n')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})

```

Analysons-le brièvement. Nous incluons le [module](https://nodejs.org/api/http.html) `http`.

Nous utilisons le module pour créer un serveur HTTP.

Le serveur est configuré pour écouter sur le port spécifié, `3000`. Lorsque le serveur est prêt, la fonction de rappel `listen` est appelée.

La fonction de rappel que nous passons est celle qui sera exécutée à chaque requête qui arrive. Chaque fois qu'une nouvelle requête est reçue, l'événement `request` est appelé, fournissant deux objets : une requête (un objet `[http.IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage)`) et une réponse (un objet `[http.ServerResponse](https://nodejs.org/api/http.html#http_class_http_serverresponse)`).

`request` fournit les détails de la requête. Grâce à lui, nous accédons aux en-têtes de la requête et aux données de la requête.

`response` est utilisé pour remplir les données que nous allons retourner au client.

Dans ce cas avec :

```js
res.statusCode = 200
```

Nous définissons la propriété `statusCode` à `200`, pour indiquer une réponse réussie.

Nous définissons également l'en-tête `Content-Type` :

```js
res.setHeader('Content-Type', 'text/plain')
```

et nous terminons la réponse, en ajoutant le contenu comme argument à `end()` :

```js
res.end('Hello World\n')
```

### Faire des requêtes HTTP avec Node.js

Comment effectuer des requêtes HTTP avec Node.js en utilisant GET, POST, PUT et DELETE.

J'utilise le terme HTTP, mais HTTPS est ce qui devrait être utilisé partout, donc ces exemples utilisent HTTPS au lieu de HTTP.

#### Effectuer une requête GET

```js
const https = require('https')
const options = {
  hostname: 'flaviocopes.com',
  port: 443,
  path: '/todos',
  method: 'GET'
}

const req = https.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`)
  res.on('data', (d) => {
    process.stdout.write(d)
  })
})

req.on('error', (error) => {
  console.error(error)
})

req.end()

```

#### Effectuer une requête POST

```js
const https = require('https')

const data = JSON.stringify({
  todo: 'Buy the milk',
})

const options = {
  hostname: 'flaviocopes.com',
  port: 443,
  path: '/todos',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length,
  },
}

const req = https.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`)
  res.on('data', (d) => {
    process.stdout.write(d)
  })
})

req.on('error', (error) => {
  console.error(error)
})

req.write(data)
req.end()

```

#### PUT et DELETE

Les requêtes PUT et DELETE utilisent le même format de requête POST, et changent simplement la valeur de `options.method`.

### Requêtes HTTP dans Node.js en utilisant Axios

Axios est une bibliothèque JavaScript très populaire que vous pouvez utiliser pour effectuer des requêtes HTTP, qui fonctionne à la fois sur les plateformes navigateur et Node.js.

Elle supporte tous les navigateurs modernes, y compris le support pour IE8 et versions supérieures.

Elle est basée sur les promesses, et cela nous permet d'écrire du code async/await pour effectuer des requêtes [XHR](https://flaviocopes.com/xhr/) très facilement.

L'utilisation d'Axios présente plusieurs avantages par rapport à l'API Fetch native :

* supporte les anciens navigateurs (Fetch nécessite un polyfill)
* a un moyen d'annuler une requête
* a un moyen de définir un délai de réponse
* a une protection CSRF intégrée
* supporte la progression du téléchargement
* effectue une transformation automatique des données JSON
* fonctionne dans Node.js

#### Installation

Axios peut être installé en utilisant npm :

```
npm install axios
```

ou yarn :

```
yarn add axios
```

ou simplement l'inclure dans votre page en utilisant unpkg.com :

```js
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

```

#### L'API Axios

Vous pouvez démarrer une requête HTTP à partir de l'objet `axios` :

```js
axios({
  url: 'https://dog.ceo/api/breeds/list/all',
  method: 'get',
  data: {
    foo: 'bar'
  }
})

```

mais pour plus de commodité, vous utiliserez généralement :

* `axios.get()`
* `axios.post()`

(comme dans jQuery vous utiliseriez `$.get()` et `$.post()` au lieu de `$.ajax()`)

Axios offre des méthodes pour tous les verbes HTTP, qui sont moins populaires mais toujours utilisés :

* `axios.delete()`
* `axios.put()`
* `axios.patch()`
* `axios.options()`

et une méthode pour obtenir les en-têtes HTTP d'une requête, en ignorant le corps :

* `axios.head()`

#### Requêtes GET

Une manière pratique d'utiliser Axios est d'utiliser la syntaxe moderne (ES2017) `async/await`.

Cet exemple Node.js interroge l'[API Dog](https://dog.ceo/) pour récupérer une liste de toutes les races de chiens, en utilisant `axios.get()`, et il les compte :

```js
const axios = require('axios')

const getBreeds = async () => {
  try {
    return await axios.get('https://dog.ceo/api/breeds/list/all')
  } catch (error) {
    console.error(error)
  }
}

const countBreeds = async () => {
  const breeds = await getBreeds()
  if (breeds.data.message) {
    console.log(`Got ${Object.entries(breeds.data.message).length} breeds`)
  }
}

countBreeds()

```

Si vous ne souhaitez pas utiliser `async/await`, vous pouvez utiliser la syntaxe [Promesses](https://flaviocopes.com/javascript-promises/) :

```js
const axios = require('axios')

const getBreeds = () => {
  try {
    return axios.get('https://dog.ceo/api/breeds/list/all')
  } catch (error) {
    console.error(error)
  }
}

const countBreeds = async () => {
  const breeds = getBreeds()
    .then((response) => {
      if (response.data.message) {
        console.log(
          `Got ${Object.entries(response.data.message).length} breeds`
        )
      }
    })
    .catch((error) => {
      console.log(error)
    })
}

countBreeds()

```

#### Ajouter des paramètres aux requêtes GET

Une réponse GET peut contenir des paramètres dans l'URL, comme ceci : `[https://site.com/?foo=bar](https://site.com/?foo=bar.)`

Avec Axios, vous pouvez le faire simplement en utilisant cette URL :

```js
axios.get('https://site.com/?foo=bar')
```

ou vous pouvez utiliser une propriété `params` dans les options :

```js
axios.get('https://site.com/', {
  params: {
    foo: 'bar'
  }
})

```

#### Requêtes POST

Effectuer une requête POST est similaire à faire une requête GET, mais au lieu de `axios.get`, vous utilisez `axios.post` :

```
axios.post('https://site.com/')
```

Un objet contenant les paramètres POST est le deuxième argument :

```js
axios.post('https://site.com/', {
  foo: 'bar'
})

```

### Utilisation des WebSockets dans Node.js

Les WebSockets sont une alternative à la communication HTTP dans les applications Web.

Ils offrent un canal de communication bidirectionnel à longue durée de vie entre le client et le serveur.

Une fois établi, le canal est maintenu ouvert, offrant une connexion très rapide avec une faible latence et un faible surcoût.

### Support des navigateurs pour les WebSockets

Les WebSockets sont supportés par tous les navigateurs modernes.

### Comment les WebSockets diffèrent de HTTP

HTTP est un protocole très différent, et a une manière différente de communiquer.

HTTP est un protocole de requête/réponse : le serveur retourne certaines données lorsque le client les demande.

Avec les WebSockets :

* le **serveur peut envoyer un message au client** sans que le client ne demande explicitement quelque chose
* le client et le serveur peuvent **se parler simultanément**
* très peu de données de surcharge doivent être échangées pour envoyer des messages. Cela signifie une **communication à faible latence**.

Les WebSockets sont excellents pour les communications en temps réel et à longue durée de vie.

HTTP est excellent pour l'échange occasionnel de données et les interactions initiées par le client.

HTTP est beaucoup plus simple à implémenter, tandis que les WebSockets nécessitent un peu plus de surcharge.

### WebSockets sécurisés

Utilisez toujours le protocole sécurisé et chiffré pour les WebSockets, `wss://`.

`ws://` fait référence à la version non sécurisée des WebSockets (le `http://` des WebSockets), et doit être évitée pour des raisons évidentes.

### Créer une nouvelle connexion WebSockets

```js
const url = 'wss://myserver.com/something'
const connection = new WebSocket(url)

```

`connection` est un objet [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket).

Lorsque la connexion est établie avec succès, l'événement `open` est déclenché.

Écoutez-le en attribuant une fonction de rappel à la propriété `onopen` de l'objet `connection` :

```js
connection.onopen = () => {
  // ...
}

```

Si une erreur se produit, la fonction de rappel `onerror` est déclenchée :

```js
connection.onerror = error => {
  console.log(`WebSocket error: ${error}`)
}

```

### Envoyer des données au serveur en utilisant WebSockets

Une fois la connexion ouverte, vous pouvez envoyer des données au serveur.

Vous pouvez le faire commodément à l'intérieur de la fonction de rappel `onopen` :

```js
connection.onopen = () => {
  connection.send('hey')
}

```

### Recevoir des données du serveur en utilisant WebSockets

Écoutez avec une fonction de rappel sur `onmessage`, qui est appelée lorsque l'événement `message` est reçu :

```js
connection.onmessage = e => {
  console.log(e.data)
}

```

### Implémenter un serveur WebSockets en Node.js

[ws](https://github.com/websockets/ws) est une bibliothèque WebSockets populaire pour Node.js.

Nous allons l'utiliser pour construire un serveur WebSockets. Il peut également être utilisé pour implémenter un client, et utiliser WebSockets pour communiquer entre deux services backend.

Installez-le facilement en utilisant :

```
yarn init
yarn add ws

```

Le code que vous devez écrire est très peu :

```js
const WebSocket = require('ws')

const wss = new WebSocket.Server({ port: 8080 })

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    console.log(`Received message => ${message}`)
  })
  ws.send('ho!')
})

```

Ce code crée un nouveau serveur sur le port 8080 (le port par défaut pour les WebSockets), et ajoute une fonction de rappel lorsqu'une connexion est établie, envoyant `ho!` au client, et journalisant les messages qu'il reçoit.

### Voir un exemple en direct sur Glitch

[Voici](https://glitch.com/edit/#!/flavio-websockets-server-example) un exemple en direct d'un serveur WebSockets.

[Voici](https://glitch.com/edit/#!/flavio-websockets-client-example) un client WebSockets qui interagit avec le serveur.

### Travailler avec les descripteurs de fichiers dans Node.js

Avant de pouvoir interagir avec un fichier qui se trouve dans votre système de fichiers, vous devez obtenir un descripteur de fichier.

Un descripteur de fichier est ce qui est retourné par l'ouverture du fichier en utilisant la méthode `open()` offerte par le module `fs` :

```js
const fs = require('fs')

fs.open('/Users/flavio/test.txt', 'r', (err, fd) => {
  // fd est notre descripteur de fichier
})

```

Remarquez le `r` que nous avons utilisé comme deuxième paramètre de l'appel `fs.open()`.

Ce flag signifie que nous ouvrons le fichier en lecture.

D'autres flags que vous utiliserez couramment sont :

* `r+` ouvrir le fichier en lecture et écriture
* `w+` ouvrir le fichier en lecture et écriture, en positionnant le flux au début du fichier. Le fichier est créé s'il n'existe pas
* `a` ouvrir le fichier en écriture, en positionnant le flux à la fin du fichier. Le fichier est créé s'il n'existe pas
* `a+` ouvrir le fichier en lecture et écriture, en positionnant le flux à la fin du fichier. Le fichier est créé s'il n'existe pas

Vous pouvez également ouvrir le fichier en utilisant la méthode `fs.openSync`, qui au lieu de fournir l'objet descripteur de fichier dans un rappel, le retourne :

```js
const fs = require('fs')

try {
  const fd = fs.openSync('/Users/flavio/test.txt', 'r')
} catch (err) {
  console.error(err)
}

```

Une fois que vous avez obtenu le descripteur de fichier, de quelque manière que vous choisissiez, vous pouvez effectuer toutes les opérations qui le nécessitent, comme appeler `fs.open()` et de nombreuses autres opérations qui interagissent avec le système de fichiers.

### Statistiques des fichiers Node.js

Chaque fichier est accompagné d'un ensemble de détails que nous pouvons inspecter en utilisant Node.js.

En particulier, en utilisant la méthode `stat()` fournie par le module `fs`.

Vous l'appelez en passant un chemin de fichier, et une fois que Node.js obtient les détails du fichier, il appellera la fonction de rappel que vous passez avec 2 paramètres : un message d'erreur, et les statistiques du fichier :

```js
const fs = require('fs')
fs.stat('/Users/flavio/test.txt', (err, stats) => {
  if (err) {
    console.error(err)
    return
  }
  // nous avons accès aux statistiques du fichier dans `stats`
})

```

Node.js fournit également une méthode synchrone, qui bloque le thread jusqu'à ce que les statistiques du fichier soient prêtes :

```js
const fs = require('fs')
try {
  const stats = fs.stat('/Users/flavio/test.txt')
} catch (err) {
  console.error(err)
}

```

Les informations sur le fichier sont incluses dans la variable stats. Quel type d'informations pouvons-nous extraire en utilisant les stats ?

Beaucoup, y compris :

* si le fichier est un répertoire ou un fichier, en utilisant `stats.isFile()` et `stats.isDirectory()`
* si le fichier est un lien symbolique en utilisant `stats.isSymbolicLink()`
* la taille du fichier en octets en utilisant `stats.size`.

Il existe d'autres méthodes avancées, mais l'essentiel de ce que vous utiliserez dans votre programmation quotidienne est ceci :

```js
const fs = require('fs')
fs.stat('/Users/flavio/test.txt', (err, stats) => {
  if (err) {
    console.error(err)
    return
  }
  
  stats.isFile() // true
  stats.isDirectory() // false
  stats.isSymbolicLink() // false
  stats.size // 1024000 //= 1MB
})

```

### Chemins de fichiers Node.js

Chaque fichier dans le système a un chemin.

Sur Linux et macOS, un chemin peut ressembler à :

`/users/flavio/file.txt`

Alors que les ordinateurs Windows sont différents, et ont une structure telle que :

`C:\users\flavio\file.txt`

Vous devez faire attention lorsque vous utilisez des chemins dans vos applications, car cette différence doit être prise en compte.

Vous incluez ce module dans vos fichiers en utilisant :

```js
const path = require('path')
```

et vous pouvez commencer à utiliser ses méthodes.

#### Obtenir des informations à partir d'un chemin

Étant donné un chemin, vous pouvez extraire des informations en utilisant ces méthodes :

* `dirname` : obtenir le dossier parent d'un fichier
* `basename` : obtenir la partie nom de fichier
* `extname` : obtenir l'extension du fichier

Exemple :

```js
const notes = '/users/flavio/notes.txt'

path.dirname(notes) // /users/flavio
path.basename(notes) // notes.txt
path.extname(notes) // .txt
```

Vous pouvez obtenir le nom du fichier sans l'extension en spécifiant un deuxième argument à `basename` :

```js
path.basename(notes, path.extname(notes)) // notes
```

#### Travailler avec les chemins

Vous pouvez joindre deux ou plusieurs parties d'un chemin en utilisant `path.join()` :

```js
const name = 'flavio'
path.join('/', 'users', name, 'notes.txt') // '/users/flavio/notes.txt'
```

Vous pouvez obtenir le calcul du chemin absolu d'un chemin relatif en utilisant `path.resolve()` :

```js
path.resolve('flavio.txt') // '/Users/flavio/flavio.txt' si exécuté depuis mon dossier personnel
```

Dans ce cas, Node.js ajoutera simplement `/flavio.txt` au répertoire de travail actuel. Si vous spécifiez un deuxième paramètre de dossier, `resolve` utilisera le premier comme base pour le second :

```js
path.resolve('tmp', 'flavio.txt') // '/Users/flavio/tmp/flavio.txt' si exécuté depuis mon dossier personnel
```

Si le premier paramètre commence par une barre oblique, cela signifie qu'il s'agit d'un chemin absolu :

```js
path.resolve('/etc', 'flavio.txt') // '/etc/flavio.txt'
```

`path.normalize()` est une autre fonction utile, qui essaiera de calculer le chemin réel, lorsqu'il contient des spécificateurs relatifs comme `.` ou `..`, ou des barres obliques doubles :

```js
path.normalize('/users/flavio/..//test.txt') //  /users/test.txt
```

Mais `resolve` et `normalize` ne **vérifieront pas** si le chemin existe. Ils calculent simplement un chemin basé sur les informations qu'ils ont reçues.

### Lire des fichiers avec Node.js

La manière la plus simple de lire un fichier en Node.js est d'utiliser la méthode `fs.readFile()`, en lui passant le chemin du fichier et une fonction de rappel qui sera appelée avec les données du fichier (et l'erreur) :

```js
const fs = require('fs')

fs.readFile('/Users/flavio/test.txt', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data)
})

```

Alternativement, vous pouvez utiliser la version synchrone `fs.readFileSync()` :

```js
const fs = require('fs')

try {
  const data = fs.readFileSync('/Users/flavio/test.txt', 'utf8')
  console.log(data)
} catch (err) {
  console.error(err)
}

```

L'encodage par défaut est `utf8`, mais vous pouvez spécifier un encodage personnalisé en utilisant un deuxième paramètre.

`fs.readFile()` et `fs.readFileSync()` lisent le contenu complet du fichier en mémoire avant de retourner les données.

Cela signifie que les gros fichiers auront un impact majeur sur votre consommation de mémoire et la vitesse d'exécution du programme.

Dans ce cas, une meilleure option est de lire le contenu du fichier en utilisant des flux.

### Écrire des fichiers avec Node.js

La manière la plus simple d'écrire dans des fichiers en Node.js est d'utiliser l'API `fs.writeFile()`.

Exemple :

```js
const fs = require('fs')

const content = 'Some content!'

fs.writeFile('/Users/flavio/test.txt', content, (err) => {
  if (err) {
    console.error(err)
    return
  }
  // fichier écrit avec succès
})
```

Alternativement, vous pouvez utiliser la version synchrone `fs.writeFileSync()` :

```js
const fs = require('fs')

const content = 'Some content!'

try {
  const data = fs.writeFileSync('/Users/flavio/test.txt', content)
  // fichier écrit avec succès
} catch (err) {
  console.error(err)
}

```

Par défaut, cette API **remplacera le contenu du fichier** s'il existe déjà.

Vous pouvez modifier le comportement par défaut en spécifiant un flag :

```js
fs.writeFile('/Users/flavio/test.txt', content, { flag: 'a+' }, (err) => {})
```

Les flags que vous utiliserez probablement sont :

* `r+` ouvrir le fichier en lecture et écriture
* `w+` ouvrir le fichier en lecture et écriture, en positionnant le flux au début du fichier. Le fichier est créé s'il n'existe pas
* `a` ouvrir le fichier en écriture, en positionnant le flux à la fin du fichier. Le fichier est créé s'il n'existe pas
* `a+` ouvrir le fichier en lecture et écriture, en positionnant le flux à la fin du fichier. Le fichier est créé s'il n'existe pas

Vous pouvez en savoir plus sur les [flags](https://nodejs.org/api/fs.html#fs_file_system_flags).

#### Ajouter à un fichier

Une méthode pratique pour ajouter du contenu à la fin d'un fichier est `fs.appendFile()` (et son homologue `fs.appendFileSync()`) :

```js
const content = 'Some content!'

fs.appendFile('file.log', content, (err) => {
  if (err) {
    console.error(err)
    return
  }
  // terminé !
})

```

#### Utiliser des flux

Toutes ces méthodes écrivent le contenu complet dans le fichier avant de rendre le contrôle à votre programme (dans la version asynchrone, cela signifie exécuter le rappel)

Dans ce cas, une meilleure option est d'écrire le contenu du fichier en utilisant des flux.

### Travailler avec des dossiers dans Node.js

Le module principal `fs` de Node.js fournit de nombreuses méthodes pratiques que vous pouvez utiliser pour travailler avec des dossiers.

#### Vérifier si un dossier existe

Utilisez `fs.access()` pour vérifier si le dossier existe et si Node.js peut y accéder avec ses permissions.

#### Créer un nouveau dossier

Utilisez `fs.mkdir()` ou `fs.mkdirSync()` pour créer un nouveau dossier :

```js
const fs = require('fs')

const folderName = '/Users/flavio/test'

try {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir)
  }
} catch (err) {
  console.error(err)
}

```

#### Lire le contenu d'un répertoire

Utilisez `fs.readdir()` ou `fs.readdirSync` pour lire le contenu d'un répertoire.

Ce morceau de code lit le contenu d'un dossier, à la fois les fichiers et les sous-dossiers, et retourne leur chemin relatif :

```js
const fs = require('fs')
const path = require('path')

const folderPath = '/Users/flavio'

fs.readdirSync(folderPath)

```

Vous pouvez obtenir le chemin complet :

```js
fs.readdirSync(folderPath).map(fileName => {
  return path.join(folderPath, fileName)
}

```

Vous pouvez également filtrer les résultats pour ne retourner que les fichiers, et exclure les dossiers :

```js
const isFile = fileName => {
  return fs.lstatSync(fileName).isFile()
}

fs.readdirSync(folderPath).map(fileName => {
  return path.join(folderPath, fileName)
}).filter(isFile)

```

#### Renommer un dossier

Utilisez `fs.rename()` ou `fs.renameSync()` pour renommer un dossier.

Le premier paramètre est le chemin actuel, le second le nouveau chemin :

```js
const fs = require('fs')

fs.rename('/Users/flavio', '/Users/roger', err => {
  if (err) {
    console.error(err)
    return
  }
  // terminé
})
```

`fs.renameSync()` est la version synchrone :

```js
const fs = require('fs')

try {
  fs.renameSync('/Users/flavio', '/Users/roger')
} catch (err) {
  console.error(err)
}

```

#### Supprimer un dossier

Utilisez `fs.rmdir()` ou `fs.rmdirSync()` pour supprimer un dossier.

Supprimer un dossier qui contient du contenu peut être plus compliqué que nécessaire.

Dans ce cas, je recommande d'installer le module `fs-extra`, qui est très populaire et bien maintenu, et c'est un remplacement direct du module `fs`, offrant plus de fonctionnalités.

Dans ce cas, la méthode `remove()` est celle que vous voulez.

Installez-le en utilisant :

`npm install fs-extra`

et utilisez-le comme ceci :

```js
const fs = require('fs-extra')

const folder = '/Users/flavio'

fs.remove(folder, err => {
  console.error(err)
})

```

Il peut également être utilisé avec des promesses :

```js
fs.remove(folder).then(() => {
  // terminé
}).catch(err => {
  console.error(err)
})

```

ou avec `async/await` :

```js
async function removeFolder(folder) {
  try {
    await fs.remove(folder)
    // terminé
  } catch (err) {
    console.error(err)
  }
}

const folder = '/Users/flavio'
removeFolder(folder)

```

### Le module fs de Node.js

Le module `fs` fournit beaucoup de fonctionnalités très utiles pour accéder et interagir avec le système de fichiers.

Il n'est pas nécessaire de l'installer. Faisant partie du noyau de Node.js, il peut être utilisé simplement en le requérant :

```js
const fs = require('fs')
```

Une fois que vous le faites, vous avez accès à toutes ses méthodes, qui incluent :

* `fs.access()` : vérifier si le fichier existe et si Node peut y accéder avec ses permissions
* `fs.appendFile()` : ajouter des données à un fichier. Si le fichier n'existe pas, il est créé
* `fs.chmod()` : changer les permissions d'un fichier spécifié par le nom de fichier passé. Connexe : `fs.lchmod()`, `fs.fchmod()`
* `fs.chown()` : changer le propriétaire et le groupe d'un fichier spécifié par le nom de fichier passé. Connexe : `fs.fchown()`, `fs.lchown()`
* `fs.close()` : fermer un descripteur de fichier
* `fs.copyFile()` : copie un fichier
* `fs.createReadStream()` : créer un flux de fichier lisible
* `fs.createWriteStream()` : créer un flux de fichier inscriptible
* `fs.link()` : créer un nouveau lien physique vers un fichier
* `fs.mkdir()` : créer un nouveau dossier
* `fs.mkdtemp()` : créer un répertoire temporaire
* `fs.open()` : définir le mode de fichier
* `fs.readdir()` : lire le contenu d'un répertoire
* `fs.readFile()` : lire le contenu d'un fichier. Connexe : `fs.read()`
* `fs.readlink()` : lire la valeur d'un lien symbolique
* `fs.realpath()` : résoudre les pointeurs de chemin de fichier relatifs (`.`, `..`) vers le chemin complet
* `fs.rename()` : renommer un fichier ou un dossier
* `fs.rmdir()` : supprimer un dossier
* `fs.stat()` : retourne le statut du fichier identifié par le nom de fichier passé. Connexe : `fs.fstat()`, `fs.lstat()`
* `fs.symlink()` : créer un nouveau lien symbolique vers un fichier
* `fs.truncate()` : tronquer à la longueur spécifiée le fichier identifié par le nom de fichier passé. Connexe : `fs.ftruncate()`
* `fs.unlink()` : supprimer un fichier ou un lien symbolique
* `fs.unwatchFile()` : arrêter de surveiller les changements sur un fichier
* `fs.utimes()` : changer le timestamp du fichier identifié par le nom de fichier passé. Connexe : `fs.futimes()`
* `fs.watchFile()` : commencer à surveiller les changements sur un fichier. Connexe : `fs.watch()`
* `fs.writeFile()` : écrire des données dans un fichier. Connexe : `fs.write()`

Une chose particulière à propos du module `fs` est que toutes les méthodes sont asynchrones par défaut, mais elles peuvent également fonctionner de manière synchrone en ajoutant `Sync`.

Par exemple :

* `fs.rename()`
* `fs.renameSync()`
* `fs.write()`
* `fs.writeSync()`

Cela fait une énorme différence dans le flux de votre application.

**Note :** Node 10 inclut le [support expérimental](https://nodejs.org/api/fs.html#fs_fs_promises_api) pour une API basée sur les promesses.

Par exemple, examinons la méthode `fs.rename()`. L'API asynchrone est utilisée avec un rappel :

```js
const fs = require('fs')

fs.rename('before.json', 'after.json', (err) => {
  if (err) {
    return console.error(err)
  }
  // terminé
})

```

Une API synchrone peut être utilisée comme ceci, avec un bloc `try/catch` pour gérer les erreurs :

```js
const fs = require('fs')

try {
  fs.renameSync('before.json', 'after.json')
  // terminé
} catch (err) {
  console.error(err)
}

```

La différence clé ici est que l'exécution de votre script sera bloquée dans le deuxième exemple, jusqu'à ce que l'opération sur le fichier ait réussi.

### Le module path de Node.js

Le module `path` fournit beaucoup de fonctionnalités très utiles pour accéder et interagir avec le système de fichiers.

Il n'est pas nécessaire de l'installer. Faisant partie du noyau de Node.js, il peut être utilisé simplement en le requérant :

```js
const path = require('path')
```

Ce module fournit `path.sep` qui fournit le séparateur de segment de chemin (`\` sur Windows, et `/` sur Linux / macOS), et `path.delimiter` qui fournit le délimiteur de chemin (`;` sur Windows, et `:` sur Linux / macOS).

Voici les méthodes `path`.

#### `path.basename()`

Retourne la dernière portion d'un chemin. Un deuxième paramètre peut filtrer l'extension du fichier :

```js
require('path').basename('/test/something') // something
require('path').basename('/test/something.txt') // something.txt
require('path').basename('/test/something.txt', '.txt') // something

```

#### `path.dirname()`

Retourne la partie répertoire d'un chemin :

```js
require('path').dirname('/test/something') // /test
require('path').dirname('/test/something/file.txt') // /test/something

```

#### `path.extname()`

Retourne la partie extension d'un chemin :

```js
require('path').dirname('/test/something') // ''
require('path').dirname('/test/something/file.txt') // '.txt'

```

#### `path.isAbsolute()`

Retourne vrai si c'est un chemin absolu :

```js
require('path').isAbsolute('/test/something') // true
require('path').isAbsolute('./test/something') // false

```

#### `path.join()`

Joint deux ou plusieurs parties d'un chemin :

```js
const name = 'flavio'
require('path').join('/', 'users', name, 'notes.txt') // '/users/flavio/notes.txt'

```

#### `path.normalize()`

Essaie de calculer le chemin réel lorsqu'il contient des spécificateurs relatifs comme `.` ou `..`, ou des barres obliques doubles :

```js
require('path').normalize('/users/flavio/..//test.txt') // /users/test.txt
```

#### `path.parse()`

Analyse un chemin en un objet avec les segments qui le composent :

* `root` : la racine
* `dir` : le chemin du dossier à partir de la racine
* `base` : le nom du fichier + l'extension
* `name` : le nom du fichier
* `ext` : l'extension du fichier

Exemple :

```js
require('path').parse('/users/test.txt')
```

résulte en :

```js
{
  root: '/',
  dir: '/users',
  base: 'test.txt',
  ext: '.txt',
  name: 'test'
}

```

#### `path.relative()`

Accepte 2 chemins comme arguments. Retourne le chemin relatif du premier chemin au second, basé sur le répertoire de travail actuel.

Exemple :

```js
require('path').relative('/Users/flavio', '/Users/flavio/test.txt') // 'test.txt'
require('path').relative('/Users/flavio', '/Users/flavio/something/test.txt') // 'something/test.txt'
```

#### `path.resolve()`

Vous pouvez obtenir le calcul du chemin absolu d'un chemin relatif en utilisant `path.resolve()` :

```js
path.resolve('flavio.txt') // '/Users/flavio/flavio.txt' si exécuté depuis mon dossier personnel
```

En spécifiant un deuxième paramètre, `resolve` utilisera le premier comme base pour le second :

```js
path.resolve('tmp', 'flavio.txt') // '/Users/flavio/tmp/flavio.txt' si exécuté depuis mon dossier personnel

```

Si le premier paramètre commence par une barre oblique, cela signifie qu'il s'agit d'un chemin absolu :

```js
path.resolve('/etc', 'flavio.txt') // '/etc/flavio.txt'

```

### Le module os de Node.js

Ce module fournit de nombreuses fonctions que vous pouvez utiliser pour récupérer des informations du **système d'exploitation** sous-jacent et de l'ordinateur sur lequel le programme s'exécute, et interagir avec lui.

```js
const os = require('os')
```

Il existe quelques propriétés utiles qui nous indiquent certaines choses clés liées à la gestion des fichiers :

`os.EOL` donne la séquence de délimiteur de ligne. C'est `\n` sur Linux et macOS, et `\r\n` sur Windows.

Lorsque je dis Linux et macOS, je veux dire les plateformes POSIX. Pour simplifier, j'exclus d'autres systèmes d'exploitation moins populaires sur lesquels Node peut s'exécuter.

`os.constants.signals` nous indique toutes les constantes liées à la gestion des signaux de processus, comme SIGHUP, SIGKILL et ainsi de suite.

`os.constants.errno` définit les constantes pour le rapport d'erreurs, comme EADDRINUSE, EOVERFLOW et plus.

Vous pouvez les lire toutes [ici](https://nodejs.org/api/os.html#os_signal_constants).

Voyons maintenant les principales méthodes que `os` fournit :

* `os.arch()`
* `os.cpus()`
* `os.endianness()`
* `os.freemem()`
* `os.homedir()`
* `os.hostname()`
* `os.loadavg()`
* `os.networkInterfaces()`
* `os.platform()`
* `os.release()`
* `os.tmpdir()`
* `os.totalmem()`
* `os.type()`
* `os.uptime()`
* `os.userInfo()`

#### `os.arch()`

Retourne la chaîne qui identifie l'architecture sous-jacente, comme `arm`, `x64`, `arm64`.

#### `os.cpus()`

Retourne des informations sur les CPU disponibles sur votre système.

Exemple :

```js
[
  {
    model: 'Intel(R) Core(TM)2 Duo CPU P8600 @ 2.40GHz',
    speed: 2400,
    times: {
      user: 281685380,
      nice: 0,
      sys: 187986530,
      idle: 685833750,
      irq: 0,
    },
  },
  {
    model: 'Intel(R) Core(TM)2 Duo CPU P8600 @ 2.40GHz',
    speed: 2400,
    times: {
      user: 282348700,
      nice: 0,
      sys: 161800480,
      idle: 703509470,
      irq: 0,
    },
  },
]

```

#### `os.endianness()`

Retourne `BE` ou `LE` selon que Node.js a été compilé avec [Big Endian ou Little Endian](https://en.wikipedia.org/wiki/Endianness).

#### `os.freemem()`

Retourne le nombre d'octets représentant la mémoire libre dans le système.

#### `os.homedir()`

Retourne le chemin vers le répertoire personnel de l'utilisateur actuel.

Exemple :

```js
'/Users/flavio'
```

#### `os.hostname()`

Retourne le nom d'hôte.

#### `os.loadavg()`

Retourne le calcul fait par le système d'exploitation sur la charge moyenne.

Il ne retourne une valeur significative que sur Linux et macOS.

Exemple :

```js
[ 3.68798828125, 4.00244140625, 11.1181640625 ]
```

#### `os.networkInterfaces()`

Retourne les détails des interfaces réseau disponibles sur votre système.

Exemple :

```js
{
  lo0: [
    {
      address: '127.0.0.1',
      netmask: '255.0.0.0',
      family: 'IPv4',
      mac: 'fe:82:00:00:00:00',
      internal: true,
    },
    {
      address: '::1',
      netmask: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
      family: 'IPv6',
      mac: 'fe:82:00:00:00:00',
      scopeid: 0,
      internal: true,
    },
    {
      address: 'fe80::1',
      netmask: 'ffff:ffff:ffff:ffff::',
      family: 'IPv6',
      mac: 'fe:82:00:00:00:00',
      scopeid: 1,
      internal: true,
    },
  ],
  en1: [
    {
      address: 'fe82::9b:8282:d7e6:496e',
      netmask: 'ffff:ffff:ffff:ffff::',
      family: 'IPv6',
      mac: '06:00:00:02:0e:00',
      scopeid: 5,
      internal: false,
    },
    {
      address: '192.168.1.38',
      netmask: '255.255.255.0',
      family: 'IPv4',
      mac: '06:00:00:02:0e:00',
      internal: false,
    },
  ],
  utun0: [
    {
      address: 'fe80::2513:72bc:f405:61d0',
      netmask: 'ffff:ffff:ffff:ffff::',
      family: 'IPv6',
      mac: 'fe:80:00:20:00:00',
      scopeid: 8,
      internal: false,
    },
  ]
}

```

#### `os.platform()`

Retourne la plateforme pour laquelle Node.js a été compilé :

* `darwin`
* `freebsd`
* `linux`
* `openbsd`
* `win32`
* …plus

#### `os.release()`

Retourne une chaîne qui identifie le numéro de version du système d'exploitation.

#### `os.tmpdir()`

Retourne le chemin vers le dossier temporaire assigné.

#### `os.totalmem()`

Retourne le nombre d'octets représentant la mémoire totale disponible dans le système.

#### `os.type()`

Identifie le système d'exploitation :

* `Linux`
* `Darwin` sur macOS
* `Windows_NT` sur Windows

#### `os.uptime()`

Retourne le nombre de secondes pendant lesquelles l'ordinateur a fonctionné depuis son dernier redémarrage.

### Le module events de Node.js

Le module `events` nous fournit la classe `EventEmitter`, qui est essentielle pour travailler avec les événements dans Node.js.

J'ai publié un article complet à ce sujet, donc ici je vais simplement décrire l'API sans autres exemples sur la façon de l'utiliser.

```js
const EventEmitter = require('events')
const door = new EventEmitter()

```

L'écouteur d'événements utilise ses propres événements :

* `newListener` lorsqu'un écouteur est ajouté
* `removeListener` lorsqu'un écouteur est supprimé

Voici une description détaillée des méthodes les plus utiles :

* `emitter.addListener()`
* `emitter.emit()`
* `emitter.eventNames()`
* `emitter.getMaxListeners()`
* `emitter.listenerCount()`
* `emitter.listeners()`
* `emitter.off()`
* `emitter.on()`
* `emitter.once()`
* `emitter.prependListener()`
* `emitter.prependOnceListener()`
* `emitter.removeAllListeners()`
* `emitter.removeListener()`
* `emitter.setMaxListeners()`

#### `emitter.addListener()`

Alias pour `emitter.on()`.

#### `emitter.emit()`

Émet un événement. Il appelle de manière synchrone chaque écouteur d'événement dans l'ordre où ils ont été enregistrés.

#### `emitter.eventNames()`

Retourne un tableau de chaînes représentant les événements enregistrés sur l'EventListener actuel :

```js
door.eventNames()
```

#### `emitter.getMaxListeners()`

Obtient le nombre maximum d'écouteurs que l'on peut ajouter à un objet EventListener, qui est par défaut de 10 mais peut être augmenté ou diminué en utilisant `setMaxListeners()` :

```js
door.getMaxListeners()
```

#### `emitter.listenerCount()`

Obtient le nombre d'écouteurs de l'événement passé en paramètre :

```js
door.listenerCount('open')
```

#### `emitter.listeners()`

Obtient un tableau d'écouteurs de l'événement passé en paramètre :

```js
door.listeners('open')
```

#### `emitter.off()`

Alias pour `emitter.removeListener()` ajouté dans Node 10.

#### `emitter.on()`

Ajoute une fonction de rappel qui est appelée lorsqu'un événement est émis.

Utilisation :

```js
door.on('open', () => {
  console.log('Door was opened')
})

```

#### `emitter.once()`

Ajoute une fonction de rappel qui est appelée lorsqu'un événement est émis pour la première fois après l'avoir enregistré. Cette fonction de rappel ne sera appelée qu'une seule fois, jamais plus.

```js
const EventEmitter = require('events')
const ee = new EventEmitter()

ee.once('my-event', () => {
  // appeler la fonction de rappel une fois
})

```

#### `emitter.prependListener()`

Lorsque vous ajoutez un écouteur en utilisant `on` ou `addListener`, il est ajouté en dernier dans la file d'attente des écouteurs, et appelé en dernier. En utilisant `prependListener`, il est ajouté, et appelé, avant les autres écouteurs.

#### `emitter.prependOnceListener()`

Lorsque vous ajoutez un écouteur en utilisant `once`, il est ajouté en dernier dans la file d'attente des écouteurs, et appelé en dernier. En utilisant `prependOnceListener`, il est ajouté, et appelé, avant les autres écouteurs.

#### `emitter.removeAllListeners()`

Supprime tous les écouteurs d'un objet émetteur d'événements écoutant un événement spécifique :

```js
door.removeAllListeners('open')
```

#### `emitter.removeListener()`

Supprime un écouteur spécifique. Vous pouvez le faire en enregistrant la fonction de rappel dans une variable, lorsqu'elle est ajoutée, afin de pouvoir la référencer plus tard :

```js
const doSomething = () => {}
door.on('open', doSomething)
door.removeListener('open', doSomething)

```

#### `emitter.setMaxListeners()`

Définit le nombre maximum d'écouteurs que l'on peut ajouter à un objet EventListener, qui est par défaut de 10 mais peut être augmenté ou diminué :

```js
door.setMaxListeners(50)
```

### Le module http de Node.js

Le module `http` de Node.js fournit des fonctions et des classes utiles pour construire un serveur HTTP. C'est un module clé pour le réseau Node.js.

Il peut être inclus en utilisant :

```js
const http = require('http')
```

Le module fournit certaines propriétés et méthodes, et certaines classes.

#### Propriétés

#### `http.METHODS`

Cette propriété liste toutes les méthodes HTTP supportées :

```
> require('http').METHODS

/* [
  'ACL',
  'BIND',
  'CHECKOUT',
  'CONNECT',
  'COPY',
  'DELETE',
  'GET',
  'HEAD',
  'LINK',
  'LOCK',
  'M-SEARCH',
  'MERGE',
  'MKACTIVITY',
  'MKCALENDAR',
  'MKCOL',
  'MOVE',
  'NOTIFY',
  'OPTIONS',
  'PATCH',
  'POST',
  'PROPFIND',
  'PROPPATCH',
  'PURGE',
  'PUT',
  'REBIND',
  'REPORT',
  'SEARCH',
  'SUBSCRIBE',
  'TRACE',
  'UNBIND',
  'UNLINK',
  'UNLOCK',
  'UNSUBSCRIBE'
] */

```

#### `http.STATUS_CODES`

Cette propriété liste tous les codes de statut HTTP et leur description :

```js
> require('http').STATUS_CODES

/* {
  100: 'Continue',
  101: 'Switching Protocols',
  102: 'Processing',
  200: 'OK',
  201: 'Created',
  202: 'Accepted',
  203: 'Non-Authoritative Information',
  204: 'No Content',
  205: 'Reset Content',
  206: 'Partial Content',
  207: 'Multi-Status',
  208: 'Already Reported',
  226: 'IM Used',
  300: 'Multiple Choices',
  301: 'Moved Permanently',
  302: 'Found',
  303: 'See Other',
  304: 'Not Modified',
  305: 'Use Proxy',
  307: 'Temporary Redirect',
  308: 'Permanent Redirect',
  400: 'Bad Request',
  401: 'Unauthorized',
  402: 'Payment Required',
  403: 'Forbidden',
  404: 'Not Found',
  405: 'Method Not Allowed',
  406: 'Not Acceptable',
  407: 'Proxy Authentication Required',
  408: 'Request Timeout',
  409: 'Conflict',
  410: 'Gone',
  411: 'Length Required',
  412: 'Precondition Failed',
  413: 'Payload Too Large',
  414: 'URI Too Long',
  415: 'Unsupported Media Type',
  416: 'Range Not Satisfiable',
  417: 'Expectation Failed',
  418: "I'm a teapot",
  421: 'Misdirected Request',
  422: 'Unprocessable Entity',
  423: 'Locked',
  424: 'Failed Dependency',
  425: 'Unordered Collection',
  426: 'Upgrade Required',
  428: 'Precondition Required',
  429: 'Too Many Requests',
  431: 'Request Header Fields Too Large',
  451: 'Unavailable For Legal Reasons',
  500: 'Internal Server Error',
  501: 'Not Implemented',
  502: 'Bad Gateway',
  503: 'Service Unavailable',
  504: 'Gateway Timeout',
  505: 'HTTP Version Not Supported',
  506: 'Variant Also Negotiates',
  507: 'Insufficient Storage',
  508: 'Loop Detected',
  509: 'Bandwidth Limit Exceeded',
  510: 'Not Extended',
  511: 'Network Authentication Required',
} */

```

#### `http.globalAgent`

Pointe vers l'instance globale de l'objet Agent, qui est une instance de la classe `http.Agent`.

Il est utilisé pour gérer la persistance et la réutilisation des connexions pour les clients HTTP, et c'est un composant clé du réseau HTTP de Node.js.

Plus d'informations dans la description de la classe `http.Agent` plus loin.

#### Méthodes

#### `http.createServer()`

Retourne une nouvelle instance de la classe `http.Server`.

Utilisation :

```
const server = http.createServer((req, res) => {
  // gérer chaque requête avec ce rappel
})

```

#### `http.request()`

Effectue une requête HTTP à un serveur, en créant une instance de la classe `http.ClientRequest`.

#### `http.get()`

Similaire à `http.request()`, mais définit automatiquement la méthode HTTP sur GET, et appelle `req.end()` automatiquement.

#### Classes

Le module HTTP fournit 5 classes :

* `http.Agent`
* `http.ClientRequest`
* `http.Server`
* `http.ServerResponse`
* `http.IncomingMessage`

#### `http.Agent`

Node crée une instance globale de la classe `http.Agent` pour gérer la persistance et la réutilisation des connexions pour les clients HTTP, un composant clé du réseau HTTP de Node.

Cet objet garantit que chaque requête faite à un serveur est mise en file d'attente et qu'une seule socket est réutilisée.

Il maintient également un pool de sockets. Cela est clé pour des raisons de performance.

#### `http.ClientRequest`

Un objet `http.ClientRequest` est créé lorsque `http.request()` ou `http.get()` est appelé.

Lorsque une réponse est reçue, l'événement `response` est appelé avec la réponse, avec une instance `http.IncomingMessage` comme argument.

Les données retournées d'une réponse peuvent être lues de 2 manières :

* vous pouvez appeler la méthode `response.read()`
* dans le gestionnaire d'événements `response`, vous pouvez configurer un écouteur d'événements pour l'événement `data`, afin de pouvoir écouter le flux de données.

#### `http.Server`

Cette classe est couramment instanciée et retournée lors de la création d'un nouveau serveur en utilisant `http.createServer()`.

Une fois que vous avez un objet serveur, vous avez accès à ses méthodes :

* `close()` arrête le serveur d'accepter de nouvelles connexions
* `listen()` démarre le serveur HTTP et écoute les connexions

#### `http.ServerResponse`

Créé par un `http.Server` et passé comme deuxième paramètre à l'événement `request` qu'il déclenche.

Communément connu et utilisé dans le code comme `res` :

```js
const server = http.createServer((req, res) => {
  // res est un objet http.ServerResponse
})

```

La méthode que vous appellerez toujours dans le gestionnaire est `end()`, qui ferme la réponse, le message est complet et le serveur peut l'envoyer au client. Elle doit être appelée sur chaque réponse.

Ces méthodes sont utilisées pour interagir avec les en-têtes HTTP :

* `getHeaderNames()` obtient la liste des noms des en-têtes HTTP déjà définis
* `getHeaders()` obtient une copie des en-têtes HTTP déjà définis
* `setHeader('headername', value)` définit une valeur d'en-tête HTTP
* `getHeader('headername')` obtient un en-tête HTTP déjà défini
* `removeHeader('headername')` supprime un en-tête HTTP déjà défini
* `hasHeader('headername')` retourne vrai si la réponse a cet en-tête défini
* `headersSent()` retourne vrai si les en-têtes ont déjà été envoyés au client

Après avoir traité les en-têtes, vous pouvez les envoyer au client en appelant `response.writeHead()`, qui accepte le statusCode comme premier paramètre, le message de statut optionnel, et l'objet des en-têtes.

Pour envoyer des données au client dans le corps de la réponse, vous utilisez `write()`. Il enverra les données tamponnées au flux de réponse HTTP.

Si les en-têtes n'ont pas encore été envoyés en utilisant `response.writeHead()`, il enverra d'abord les en-têtes, avec le code de statut et le message qui sont définis dans la requête, que vous pouvez modifier en définissant les valeurs des propriétés `statusCode` et `statusMessage` :

```js
response.statusCode = 500
response.statusMessage = 'Internal Server Error'

```

#### `http.IncomingMessage`

Un objet `http.IncomingMessage` est créé par :

* `http.Server` lors de l'écoute de l'événement `request`
* `http.ClientRequest` lors de l'écoute de l'événement `response`

Il peut être utilisé pour accéder à la réponse :

* statut en utilisant ses méthodes `statusCode` et `statusMessage`
* en-têtes en utilisant sa méthode `headers` ou `rawHeaders`
* méthode HTTP en utilisant sa méthode `method`
* version HTTP en utilisant la méthode `httpVersion`
* URL en utilisant la méthode `url`
* socket sous-jacent en utilisant la méthode `socket`

Les données sont accessibles en utilisant des flux, puisque `http.IncomingMessage` implémente l'interface Readable Stream.

### Streams Node.js

Les streams sont l'un des concepts fondamentaux qui alimentent les applications Node.js.

Ils sont un moyen de gérer la lecture/écriture de fichiers, les communications réseau, ou tout type d'échange d'informations de bout en bout de manière efficace.

Les streams ne sont pas un concept unique à Node.js. Ils ont été introduits dans le système d'exploitation Unix il y a des décennies, et les programmes peuvent interagir les uns avec les autres en passant des streams à travers l'opérateur pipe (`|`).

Par exemple, de manière traditionnelle, lorsque vous demandez au programme de lire un fichier, le fichier est lu en mémoire, du début à la fin, puis vous le traitez.

En utilisant des streams, vous le lisez morceau par morceau, en traitant son contenu sans le garder tout en mémoire.

Le module `stream` de Node.js fournit la fondation sur laquelle toutes les API de streaming sont construites.

#### Pourquoi des streams ?

Les streams offrent essentiellement deux avantages majeurs par rapport à d'autres méthodes de gestion des données :

* **Efficacité mémoire** : vous n'avez pas besoin de charger de grandes quantités de données en mémoire avant de pouvoir les traiter
* **Efficacité temporelle** : il faut beaucoup moins de temps pour commencer à traiter les données dès que vous les avez, plutôt que d'attendre que toute la charge utile des données soit disponible pour commencer

#### Un exemple de stream

Un exemple typique est celui de la lecture de fichiers depuis un disque.

En utilisant le module `fs` de Node.js, vous pouvez lire un fichier et le servir via HTTP lorsqu'une nouvelle connexion est établie à votre serveur `http` :

```js
const http = require('http')
const fs = require('fs')

const server = http.createServer(function (req, res) {
  fs.readFile(__dirname + '/data.txt', (err, data) => {
    res.end(data)
  })
})

server.listen(3000)

```

`readFile()` lit le contenu complet du fichier et appelle la fonction de rappel lorsqu'il a terminé.

`res.end(data)` dans le rappel retournera le contenu du fichier au client HTTP.

Si le fichier est volumineux, l'opération prendra un certain temps. Voici la même chose écrite en utilisant des streams :

```js
const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
  const stream = fs.createReadStream(__dirname + '/data.txt')
  stream.pipe(res)
})

server.listen(3000)

```

Au lieu d'attendre que le fichier soit entièrement lu, nous commençons à le streamer vers le client HTTP dès que nous avons un morceau de données prêt à être envoyé.

#### pipe()

L'exemple ci-dessus utilise la ligne `stream.pipe(res)` : la méthode `pipe()` est appelée sur le flux de fichier.

Que fait ce code ? Il prend la source et la pipe vers une destination.

Vous l'appelez sur le flux source, donc dans ce cas, le flux de fichier est pipé vers la réponse HTTP.

La valeur de retour de la méthode `pipe()` est le flux de destination, ce qui est une chose très pratique qui nous permet de chaîner plusieurs appels `pipe()`, comme ceci :

```js
src.pipe(dest1).pipe(dest2)
```

Cette construction est la même que de faire :

```js
src.pipe(dest1)
dest1.pipe(dest2)
```

#### API Node.js alimentées par des streams

Grâce à leurs avantages, de nombreux modules principaux de Node.js offrent des capacités de gestion de streams natives, notamment :

* `process.stdin` retourne un stream connecté à stdin
* `process.stdout` retourne un stream connecté à stdout
* `process.stderr` retourne un stream connecté à stderr
* `fs.createReadStream()` crée un stream lisible vers un fichier
* `fs.createWriteStream()` crée un stream inscriptible vers un fichier
* `net.connect()` initie une connexion basée sur un stream
* `http.request()` retourne une instance de la classe http.ClientRequest, qui est un stream inscriptible
* `zlib.createGzip()` compresse les données en utilisant gzip (un algorithme de compression) dans un stream
* `zlib.createGunzip()` décompresse un stream gzip.
* `zlib.createDeflate()` compresse les données en utilisant deflate (un algorithme de compression) dans un stream
* `zlib.createInflate()` décompresse un stream deflate

#### Différents types de streams

Il existe quatre classes de streams :

* `Readable` : un stream que vous pouvez lire, mais pas écrire (vous pouvez recevoir des données, mais pas envoyer de données). Lorsque vous poussez des données dans un stream lisible, elles sont mises en mémoire tampon, jusqu'à ce qu'un consommateur commence à lire les données.
* `Writable` : un stream dans lequel vous pouvez écrire, mais pas lire (vous pouvez envoyer des données, mais pas recevoir)
* `Duplex` : un stream dans lequel vous pouvez à la fois écrire et lire, essentiellement une combinaison d'un stream Readable et Writable
* `Transform` : un stream Transform est similaire à un Duplex, mais la sortie est une transformation de son entrée

#### Comment créer un stream lisible

Nous obtenons le stream `Readable` du module `stream`, et nous l'initialisons :

```js
const Stream = require('stream')
const readableStream = new Stream.Readable()

```

Maintenant que le stream est initialisé, nous pouvons lui envoyer des données :

```js
readableStream.push('hi!')
readableStream.push('ho!')

```

#### Comment créer un stream inscriptible

Pour créer un stream inscriptible, nous étendons l'objet de base `Writable` et nous implémentons sa méthode `_write()`.

Tout d'abord, créez un objet stream :

```js
const Stream = require('stream')
const writableStream = new Stream.Writable()

```

puis implémentez `_write` :

```js
writableStream._write = (chunk, encoding, next) => {
  console.log(chunk.toString())
  next()
}

```

Vous pouvez maintenant y connecter un stream lisible :

```js
process.stdin.pipe(writableStream)
```

#### Comment obtenir des données à partir d'un stream lisible

Comment lisons-nous les données à partir d'un stream lisible ? En utilisant un stream inscriptible :

```js
const Stream = require('stream')

const readableStream = new Stream.Readable()
const writableStream = new Stream.Writable()

writableStream._write = (chunk, encoding, next) => {
  console.log(chunk.toString())
  next()
}

readableStream.pipe(writableStream)

readableStream.push('hi!')
readableStream.push('ho!')

```

Vous pouvez également consommer un stream lisible directement, en utilisant l'événement `readable` :

```js
readableStream.on('readable', () => {
  console.log(readableStream.read())
})

```

#### Comment envoyer des données à un stream inscriptible

En utilisant la méthode `write()` du stream :

```js
writableStream.write('hey!\n')
```

#### Signaler à un stream inscriptible que vous avez terminé l'écriture

Utilisez la méthode `end()` :

```js
const Stream = require('stream')

const readableStream = new Stream.Readable()
const writableStream = new Stream.Writable()

writableStream._write = (chunk, encoding, next) => {
  console.log(chunk.toString())
  next()
}

readableStream.pipe(writableStream)

readableStream.push('hi!')
readableStream.push('ho!')

writableStream.end()

```

### Les bases du travail avec MySQL et Node.js

MySQL est l'une des bases de données relationnelles les plus populaires au monde.

L'écosystème Node.js dispose de plusieurs packages différents qui vous permettent d'interfacer avec MySQL, de stocker des données, de récupérer des données, et ainsi de suite.

Nous utiliserons `[mysqljs/mysql](https://github.com/mysqljs/mysql)`, un package qui compte plus de 12 000 étoiles GitHub et existe depuis des années.

#### Installation du package Node.js MySql

Vous l'installez en utilisant :

```
npm install mysql
```

#### Initialisation de la connexion à la base de données

Vous incluez d'abord le package :

```js
const mysql = require('mysql')
```

et vous créez une connexion :

```js
const options = {
  user: 'the_mysql_user_name',
  password: 'the_mysql_user_password',
  database: 'the_mysql_database_name'
}

const connection = mysql.createConnection(options)

```

Vous initialisez une nouvelle connexion en appelant :

```js
connection.connect(err => {
  if (err) {
    console.error('An error occurred while connecting to the DB')
    throw err
  }
})

```

#### Les options de connexion

Dans l'exemple ci-dessus, l'objet `options` contenait 3 options :

```js
const options = {
  user: 'the_mysql_user_name',
  password: 'the_mysql_user_password',
  database: 'the_mysql_database_name'
}

```

Il y en a beaucoup d'autres que vous pouvez utiliser, y compris :

* `host`, le nom d'hôte de la base de données, par défaut `localhost`
* `port`, le numéro de port du serveur MySQL, par défaut 3306
* `socketPath`, utilisé pour spécifier un socket unix au lieu de l'hôte et du port
* `debug`, par défaut désactivé, peut être utilisé pour le débogage
* `trace`, par défaut activé, imprime les traces de pile lorsque des erreurs se produisent
* `ssl`, utilisé pour établir une connexion SSL au serveur (hors du cadre de ce tutoriel)

#### Effectuer une requête SELECT

Vous êtes maintenant prêt à effectuer une requête SQL sur la base de données. La requête, une fois exécutée, invoquera une fonction de rappel qui contient une éventuelle erreur, les résultats et les champs :

```js
connection.query('SELECT * FROM todos', (error, todos, fields) => {
  if (error) {
    console.error('An error occurred while executing the query')
    throw error
  }
  console.log(todos)
})

```

Vous pouvez passer des valeurs qui seront automatiquement échappées :

```js
const id = 223
connection.query('SELECT * FROM todos WHERE id = ?', [id], (error, todos, fields) => {
  if (error) {
    console.error('An error occurred while executing the query')
    throw error
  }
  console.log(todos)
})

```

Pour passer plusieurs valeurs, il suffit de mettre plus d'éléments dans le tableau que vous passez comme deuxième paramètre :

```js
const id = 223
const author = 'Flavio'
connection.query('SELECT * FROM todos WHERE id = ? AND author = ?', [id, author], (error,
  if (error) {
    console.error('An error occurred while executing the query')
    throw error
  }
  console.log(todos)
})

```

#### Effectuer une requête INSERT

Vous pouvez passer un objet :

```js
const todo = {
  thing: 'Buy the milk'
  author: 'Flavio'
}

connection.query('INSERT INTO todos SET ?', todo, (error, results, fields) => {
  if (error) {
    console.error('An error occurred while executing the query')
    throw error
  }
})

```

Si la table a une clé primaire avec `auto_increment`, la valeur de celle-ci sera retournée dans la valeur `results.insertId` :

```js
const todo = {
  thing: 'Buy the milk'
  author: 'Flavio'
}

connection.query('INSERT INTO todos SET ?', todo, (error, results, fields) => {
  if (error) {
    console.error('An error occurred while executing the query')
    throw error
  }}

  const id = results.resultId
  console.log(id)
)

```

#### Fermer la connexion

Lorsque vous devez terminer la connexion à la base de données, vous pouvez appeler la méthode `end()` :

```js
connection.end()
```

Cela garantit que toute requête en attente est envoyée, et que la connexion est terminée de manière élégante.

### La différence entre développement et production

Vous pouvez avoir différentes configurations pour les environnements de production et de développement.

Node.js suppose qu'il s'exécute toujours dans un environnement de développement. Vous pouvez signaler à Node.js que vous êtes en production en définissant la variable d'environnement `NODE_ENV=production`.

Cela se fait généralement en exécutant la commande :

```
export NODE_ENV=production
```

dans le shell, mais il est préférable de la mettre dans votre fichier de configuration shell (comme `.bash_profile` avec le shell Bash) car sinon le paramètre ne persiste pas en cas de redémarrage du système.

Vous pouvez également appliquer la variable d'environnement en la préfixant à votre commande d'initialisation de l'application :

```
NODE_ENV=production node app.js
```

Cette variable d'environnement est une convention largement utilisée dans les bibliothèques externes également.

Définir l'environnement sur `production` garantit généralement que :

* la journalisation est maintenue à un niveau essentiel minimum
* plus de niveaux de cache sont mis en place pour optimiser les performances

Par exemple, [Pug](https://pugjs.org/api/express.html), la bibliothèque de templating utilisée par Express, compile en mode debug si `NODE_ENV` n'est pas défini sur `production`. Les vues Express sont compilées à chaque requête en mode développement, tandis qu'en production, elles sont mises en cache. Il existe de nombreux autres exemples.

Express fournit des hooks de configuration spécifiques à l'environnement, qui sont automatiquement appelés en fonction de la valeur de la variable `NODE_ENV` :

```js
app.configure('development', () => {
  // ...
})

app.configure('production', () => {
  // ...
})

app.configure('production', 'staging', () => {
  // ...
})

```

Par exemple, vous pouvez utiliser cela pour définir différents gestionnaires d'erreurs pour différents modes :

```js
app.configure('development', () => {
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
})

app.configure('production', () => {
  app.use(express.errorHandler())
})

```

### Mots de la fin

J'espère que cette introduction à Node.js vous aidera à commencer à l'utiliser, ou à comprendre certains de ses concepts. Et avec un peu de chance, vous en saurez maintenant assez pour commencer à construire de grandes choses !