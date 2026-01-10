---
title: Comprendre le fonctionnement d'Express.js en construisant votre propre multiplexeur
  de serveur à partir de zéro
subtitle: ''
author: Sifundo
co_authors: []
series: null
date: '2024-10-03T15:31:46.815Z'
originalURL: https://freecodecamp.org/news/understand-how-expressjs-works-by-building-your-own-server-multiplexer-from-scratch
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/urBiLDuUhMU/upload/65f541a7f0d11691008b4e93d89f2d29.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: backend
  slug: backend
- name: webdev
  slug: webdev
- name: Express
  slug: express
seo_title: Comprendre le fonctionnement d'Express.js en construisant votre propre
  multiplexeur de serveur à partir de zéro
seo_desc: 'Kata Machines have become the go-to method for mastering tough concepts,
  and it''s hard to find a better tool for deliberate practice.

  If you haven’t come across a kata yet, trust me—you will soon enough.

  There’s a reason why developers love katas, wh...'
---

Les Kata Machines sont devenues la méthode de référence pour maîtriser des concepts difficiles, et il est difficile de trouver un meilleur outil pour la pratique délibérée.

Si vous n'avez pas encore rencontré de kata, faites-moi confiance—vous le ferez bientôt.

Il y a une raison pour laquelle les développeurs adorent les katas, qu'ils les utilisent pour aiguiser leurs compétences pour des projets personnels ou se préparer pour des entretiens.

Un kata est une question de pratique **délibérée**. Cela vient des arts martiaux comme le Karaté et le Judo, et, selon Wikipedia, il est défini comme une séquence prédéterminée de mouvements, de techniques et de motifs qui suivent un ordre spécifique (source : [wikipedia](https://en.wikipedia.org/wiki/Kata)).

Les Kata Machines viennent de cette idée : apprendre par des exercices et une pratique délibérée, consciente (chorégraphiée).

J'ai réalisé à quel point les katas sont parfaits lorsque j'apprenais Haskell à l'époque. Si vous savez, vous savez. Haskell était une bête à apprendre pour moi à l'époque !

Alors, je me suis dit, pourquoi ne pas faire de même pour le backend ? Il suffit de choisir un concept de haut niveau et de le creuser de manière répétée et délibérée jusqu'à son cœur et ses premiers principes.

Dans cet article, j'ai choisi les frameworks côté serveur. Nous allons décomposer l'idée d'un "framework" en utilisant Express comme exemple.

Nous allons prendre Express de haut niveau :

```js
const express = require("express");

const PORT = 3000;
const app = express();

app.get("/", (req, res) => {
  res.send("Hello, world!");
});

app.listen(PORT, () => console.log("Server listening on port:", PORT));
```

Et creuser jusqu'à ce que nous touchions le code natif de Node.js :

```c
void TCPWrap::New(const FunctionCallbackInfo<Value>& args) {
  CHECK(args.IsConstructCall());
  CHECK(args[0]->IsInt32());
  Environment* env = Environment::GetCurrent(args);
  int type_value = args[0].As<Int32>()->Value();
  TCPWrap::SocketType type = static_cast<TCPWrap::SocketType>(type_value);
  ProviderType provider;
  switch (type) {
    case SOCKET:
      provider = PROVIDER_TCPWRAP;
      break;
    case SERVER:
      provider = PROVIDER_TCPSERVERWRAP;
      break;
    default:
      UNREACHABLE();
  }
  new TCPWrap(env, args.This(), provider);
}
```

Et ayant acquis cette nouvelle intuition, nous allons reconstruire avec une implémentation "Express" personnalisée :

```js
function serverMux() {
  function hook(req, res) {
    // À implémenter
  }
  return {
    hook
  };
}

const app = serverMux();

const server = http.createServer((req, res) => {
  app.hook(req, res);
});
```

Ce sera un sacré voyage – et gratifiant à cela !

Je suppose que vous avez quelques connaissances en backend et que vous vous classez comme un débutant avancé qui cherche à monter de niveau.

Si cela vous ressemble, nous sommes prêts à continuer.

### Voici ce que nous allons couvrir :

* [Forme 1 : Frameworks côté serveur](#forme-1--frameworks-cote-serveur)
    
    * [Premier exercice : Déballage d'Express.js](#premier-exercice--deballage-d-expressjs)
        
    * [Le serveur](#le-serveur)
        
    * [La socket dans Node.js](#la-socket-dans-nodejs)
        
    * [La socket dans le code source de Node.js](#la-socket-dans-le-code-source-de-nodejs)
        
* [Forme 2 : Implémentation d'un multiplexeur de serveur personnalisé](#forme-2--implementation-d-un-multiplexeur-de-serveur-personnalise)
    
    * [Création de notre routeur personnalisé](#creation-de-notre-routeur-personnalise)
        
    * [Squelette de base du multiplexeur](#squelette-de-base-du-multiplexeur)
        
    * [La fonction Hook](#la-fonction-hook)
        
    * [Pourquoi utiliser une file d'attente ?](#pourquoi-utiliser-une-file-d-attente-)
        
        * [Opérations de la file d'attente](#operations-de-la-file-d-attente)
            
    * [Enveloppe de requête](#enveloppe-de-requete)
        
    * [Test de la file d'attente](#test-de-la-file-d-attente)
        
    * [Traitement des requêtes](#traitement-des-requetes)
        
    * [Table de recherche et gestionnaires](#table-de-recherche-et-gestionnaires)
        
    * [Enregistrement des gestionnaires](#enregistrement-des-gestionnaires)
        

* [Conclusion](#conclusion)
    

## Forme 1 : Frameworks côté serveur

Le terme "framework côté serveur" est large. Réfléchissez-y : `mysql2` pourrait être considéré comme un framework selon la manière dont vous classez les frameworks et les bibliothèques. Même `sharp.js` pour l'édition d'images pourrait entrer dans le cadre des frameworks côté serveur, n'est-ce pas ?

Mais la question est, quel type de framework est Express.js ?

Express est un multiplexeur—spécifiquement, un multiplexeur de serveur (server mux). Je vous promets, le terme n'est pas aussi complexe qu'il en a l'air. L'implémentation, cependant—c'est une toute autre histoire.

En termes simples, un server mux est un routeur. Bien sûr, Express et autres server mux gèrent plus que juste le routage, mais c'est l'idée de base.

Express prend les objets `request` et `response` du serveur et les route. Ne vous inquiétez pas, nous plongerons dans le routage bientôt.

Voici un point intéressant : si Express n'est pas le serveur, alors qu'est-ce que le serveur exactement ?

Pour répondre à cela, nous devons regarder le code source d'Express.js, que vous pouvez cloner depuis GitHub :

```bash
git clone https://github.com/expressjs/express.git
```

Une fois que vous êtes prêt, nous pouvons plonger directement dans notre premier approfondissement.

### Premier exercice : Déballage d'Express.js

Ouvrez votre code source d'Express dans un éditeur. Vous trouverez le fichier d'entrée `express.js` dans le dossier `lib`.

Vous pouvez parcourir le fichier, mais nous allons nous concentrer sur les lignes 42 et 43—le cœur de tout cela :

```js
mixin(app, EventEmitter.prototype, false);
mixin(app, proto, false);
```

Ce que vous regardez est la composition d'objets : un modèle de conception où un objet est créé en combinant les propriétés et méthodes d'autres objets.

Notre objet cible ici est `proto`, qui est importé depuis `application.js`, le cœur d'Express.

Ouvrons ce fichier. Il y a beaucoup de code, mais rappelez-vous, notre objectif est de déterminer où se trouve le serveur dans Express.

S'il y a une fonction dans Express que tout le monde connaît probablement, c'est `listen`. L'essence d'un serveur est de "écouter" sur un réseau. Alors, faites un rapide `Ctrl+F` pour "listen," et vous trouverez la définition à la ligne 633 :

```js
app.listen = function listen() {
  var server = http.createServer(this);
  return server.listen.apply(server, arguments);
};
```

La voici, la fameuse fonction `listen`. Avons-nous trouvé le serveur ?

```js
var server = http.createServer(this);
```

Nous avons déjà vu une version de cela dans l'introduction :

```js
const server = http.createServer((req, res) => {
  app.hook(req, res);
});
```

Cela confirme qu'Express est effectivement un multiplexeur de serveur, et que le serveur réel est retourné par la fonction `createServer` de Node.js depuis le package `http`.

C'est un bon progrès !

Nous avons pelé une couche, mais nous pouvons aller plus profond. Que fait exactement `createServer`, et qu'est-ce que cet objet `server` ?

### Le serveur

Un serveur est l'unité de base du backend. À sa base, le concept est simple : comment deux processus ou plus peuvent-ils communiquer sur un réseau ?

C'est l'idée fondamentale derrière la programmation réseau. Nous avons des appareils équipés d'adresses IP pour l'identification et de ports pour l'échange de données sur un réseau.

La communication elle-même est complexe, c'est là que les protocoles interviennent pour faciliter le processus.

Les protocoles les plus courants sont UDP et TCP :

* **UDP** est un protocole sans connexion et ne garantit pas une communication fiable, mais permet un transfert de données à faible latence et efficace. Cela est idéal pour les applications sensibles au temps telles que la visioconférence, les jeux en ligne et la voix sur IP (VoIP) (source [Wikipedia](https://en.wikipedia.org/wiki/User_Datagram_Protocol)).
    
* **TCP** est un protocole orienté connexion avec une transmission de données fiable, ordonnée et vérifiée pour les erreurs entre les applications sur des appareils en réseau. C'est une partie majeure des applications internet (source [Wikipedia](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)).
    

TCP est le protocole le plus largement utilisé en raison de sa fiabilité, et la plupart des applications côté serveur avec lesquelles vous travaillerez, y compris Express, sont basées sur TCP.

Bien que j'aime les particularités et la puissance d'UDP, nous nous concentrerons sur TCP, en traçant ses racines dans Node.js.

Nous avons déjà vu un aperçu de cela :

```c
void TCPWrap::New(const FunctionCallbackInfo<Value>& args) {
  // du code
  new TCPWrap(env, args.This(), provider);
}
```

Avant de creuser cela, nous devons répondre à une question clé : Que signifie vraiment être un processus serveur ?

Sans entrer trop dans les descripteurs de fichiers, les sockets ou les couches réseau, un serveur est un objet de niveau OS responsable de la gestion de la communication entre les nœuds. Lorsque vous appelez :

```js
const http = require("node:http");

const something = http.createServer({});
```

Vous créez un objet de niveau OS, communément appelé **socket**. Cette socket facilite la communication réseau entre les appareils, ainsi que la gestion du codage et du décodage des données.

En bref, `createServer` abstrait et retourne cet objet socket.

Et, oui, nous pouvons implémenter cette socket dans Node.js. Rappelez-vous, Node.js a un accès natif à l'OS, permettant à JavaScript de fonctionner au niveau système.

### La socket dans Node.js

Voici un code qui crée une socket de serveur :

```js
// Utilisation de Node v20
const net = require('node:net');

const server = net.createServer((c) => {
  console.log('client connecté', c.remoteAddress);
  c.write("Hello; world");

  c.on('end', () => {
    console.log('client déconnecté');
  });
});

server.on('error', (err) => {
  throw err;
});

server.listen(3000, () => {
  console.log('server bound');
});
```

Bien que `net.createServer((c)` soit encore une abstraction de haut niveau comme `http.createServer`, il retourne la socket brute.

L'objet `c` représente le client qui a établi la connexion (dial). Au-delà de l'écriture, nous pouvons faire beaucoup plus.

Par exemple, voici une simple opération d'écriture :

```js
c.write("Hello world");
```

Notre socket fonctionne sur `localhost:3000`. Si vous faites une requête (ou utilisez `curl`) :

```bash
curl localhost:3000
```

La pile réseau de niveau OS encode non seulement vos données mais aussi des informations sur qui vous êtes et où vous trouver—sous la forme d'une réponse, entre autres.

C'est ce que le serveur reçoit, et il est important de savoir où envoyer la réponse (comme l'IP, etc.).

Donc, l'objet `c` représente tout cela !

Nous avons couvert beaucoup de concepts de surface, mais avant de conclure cette partie, voici un défi bonus :

Essayez d'écrire une classe sur le serveur pour gérer plusieurs connexions. Vous pourriez stocker ces connexions dans une structure de données et envoyer périodiquement des données tant que la connexion reste ouverte.

Nous sommes à environ trois couches de profondeur maintenant, mais le voyage n'est pas terminé. Rappelez-vous l'objectif ?

Maintenant, il est temps de cloner le code source de Node.js. Ne vous inquiétez pas, nous nous concentrerons uniquement sur les parties pertinentes.

```bash
git clone https://github.com/nodejs/node.git
```

### La socket dans le code source de Node.js

Commençons le traçage ! Node.js est une base de code massive—c'est un moteur entier qui fait bien plus que simplement gérer les sockets. Mais aujourd'hui, nous ne nous intéressons qu'à la partie réseau.

Tout d'abord, naviguez jusqu'au dossier `lib`, et à l'intérieur, vous trouverez un fichier appelé `net.js`. C'est là que la plupart du travail se fait pour les applications réseau. Si vous faites défiler jusqu'à la ligne 210, vous verrez une vue familière :

```js
function createServer(options, connectionListener) {
  return new Server(options, connectionListener);
}
```

C'est tout ! Chaque fois que nous créons un serveur, il appelle cette fonction et retourne un objet `Server`. Chaque fois que vous voyez `new` en JavaScript, vous devriez avoir un moment d'illumination—cela signifie qu'un nouvel objet ou une nouvelle classe (plan) est créé.

Nous pouvons donc tracer et trouver la définition de `Server` :

À la ligne 1737

À première vue, il peut sembler qu'il ne se passe rien de spécial. Mais JavaScript a une manière insidieuse de cacher la complexité.

Voici le truc : JavaScript est un langage basé sur les prototypes. Cela signifie que les objets peuvent hériter des fonctionnalités d'autres objets via les prototypes. À la ligne 1791, nous voyons cela en action :

```js
ObjectSetPrototypeOf(Server.prototype, EventEmitter.prototype);
```

En anglais simple : notre objet `Server` hérite de tous les comportements d'autres objets comme `EventEmitter`, par exemple. C'est un modèle courant dans les bibliothèques JavaScript—rappellez-vous le mixin dans Express ?

À ce stade, si vous n'avez jamais travaillé avec des prototypes ou JavaScript Orienté Objet (OOJS), cela peut sembler être un territoire avancé. Mais ne vous inquiétez pas—les bonnes personnes chez [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain) ont un excellent guide sur les prototypes pour vous mettre à niveau.

Maintenant, qu'est-ce qu'une chose que nous savons avec certitude à propos d'un serveur Node.js ? Il a une fonction `listen`. Nous l'utilisons tout le temps dans le code côté serveur (même dans les frameworks comme Express). Alors, vérifions si notre objet `Server` a une fonction `listen`.

Faites défiler un peu plus bas, et la voici à la ligne 2006 :

```js
Server.prototype.listen = function(...args) {}
```

Cette fonction gère beaucoup de choses—comme la validation du numéro de port—mais la partie clé commence autour de la ligne 2016, où le commentaire nous dit clairement :

```js
// start TCP server listening on host:port
```

Nous savons ce qu'est TCP !

Les fonctions importantes ici sont `lookupAndListen` et `listenInCluster`. Elles sont responsables du démarrage du serveur TCP réel :

```js
// start TCP server listening on host:port
if (options.host) {
  lookupAndListen(this, options.port | 0, options.host, backlog, options.exclusive, flags);
} else {
  listenInCluster(this, null, options.port | 0, 4, backlog, undefined, options.exclusive);
}
```

En creusant dans `lookupAndListen` (ligne 2156), nous trouvons qu'il appelle `listenInCluster`, qui nous mène à une autre fonction : `server._listen2` (oui, plus de traçage !) :

```js
server._listen2(address, port, addressType, backlog, fd, flags);
```

Comme l'expliquent les commentaires, tout cela est une question de compatibilité ascendante :

```js
// _listen2 sets up the listened handle, it is still named like this
// to avoid breaking code that wraps this method
```

Je sais que cela peut sembler une chasse à l'oie sauvage, mais faites-moi confiance, tracer à travers une grande base de code comme Node.js nécessite de la patience. Nous nous rapprochons.

Donc, `._listen2` est défini dans le prototype de notre objet `Server` et pointe vers une fonction appelée `setupListenHandle` (ligne 1856). Cette fonction est le véritable hub où tout se rassemble.

Autour des lignes 1870 et 1883, vous trouverez la fonction `createServerHandle` :

```js
function createServerHandle(address, port, addressType, fd, flags) {
  handle = new TCP(TCPConstants.SERVER);
  isTCP = true;
  return handle;
}
```

Enfin ! Nous avons atteint le cœur : l'objet `TCP`. C'est là que le serveur TCP réel est créé, le cœur. Nous pourrions nous arrêter ici, satisfaits d'avoir trouvé le serveur TCP, mais pourquoi ne pas creuser plus profond ?

Rappelez-vous que `new TCP` crée un objet, donc nous devons déterminer ce que `TCP` représente réellement.

Remontez à la ligne 68, où vous verrez l'importation suivante :

```js
const {
  TCP,
  TCPConnectWrap,
  constants: TCPConstants,
} = internalBinding('tcp_wrap');
```

C'est là que les choses deviennent intéressantes. Vous pourriez vous demander : "Quel genre d'importation est-ce ? Ce n'est pas votre instruction `require` ou `import` habituelle." C'est parce que JavaScript seul ne peut pas gérer les serveurs TCP—il a besoin d'aide de C++.

Node.js, qui est construit sur le moteur V8, repose sur des liaisons C++ pour faire le travail lourd. Ces liaisons sont comme un pont, permettant à JavaScript de communiquer avec des fonctions système de bas niveau (comme la création d'un serveur TCP). `internalBinding('tcp_wrap')` est l'un de ces ponts.

Pour vraiment tracer les choses à leur source, nous devons plonger dans le code C++ de Node.js. Vous trouverez `tcp_wrap.cc` dans le dossier `src` (parmi d'autres comme `crypto`, `streams`, `async`, `fs`). Ouvrez-le, et vous trouverez cette fonction :

```cpp
void TCPWrap::New(const FunctionCallbackInfo<Value>& args) {
  CHECK(args.IsConstructCall());
  CHECK(args[0]->IsInt32());
  Environment* env = Environment::GetCurrent(args);
  int type_value = args[0].As<Int32>()->Value();
  TCPWrap::SocketType type = static_cast<TCPWrap::SocketType>(type_value);
  ProviderType provider;
  switch (type) {
    case SOCKET:
      provider = PROVIDER_TCPWRAP;
      break;
    case SERVER:
      provider = PROVIDER_TCPSERVERWRAP;
      break;
    default:
      UNREACHABLE();
  }
  new TCPWrap(env, args.This(), provider);
}
```

C'est là que le serveur TCP est *réellement* créé. Vous pouvez voir des fonctions plus familières comme `bind`, et tout ce que JavaScript fait est simplement un miroir de ces opérations de plus bas niveau.

Nous avons tracé notre chemin depuis le JavaScript de haut niveau jusqu'au C++—le vrai début d'un serveur TCP dans Node.js.

Nous avons terminé la première partie de l'introduction : "Et creuser encore et encore jusqu'à ce que nous touchions le code natif de Node.js" et maintenant il est temps de reconstruire.

## Forme 2 : Implémentation d'un multiplexeur de serveur personnalisé

Avant de plonger dans le code, l'objectif n'est pas de se concentrer sur la complexité du développement du multiplexeur (car cela peut devenir compliqué). Au lieu de cela, il s'agit de montrer comment le **serveur** et le **multiplexeur** s'emboîtent.

Si quoi que ce soit, voici la principale leçon à retenir : le flux du serveur vers le routeur, et finalement vers l'appelant (le client qui a fait la requête).

Rappelez-vous, nous avons déjà vu un concept similaire dans Express :

```js
// L'application Express hérite de EventEmitter de Node
mixin(app, EventEmitter.prototype, false);
// Implémente le multiplexeur de serveur avec des fonctions comme listen, handle, middleware
mixin(app, proto, false);
```

En coulisses, beaucoup de code complexe est abstrait. Cela aide à simplifier les choses et rend le code plus propre, mais à des fins d'enseignement, nous adopterons une approche plus verbeuse. De cette façon, vous pouvez voir comment tout est connecté.

### Création de notre routeur personnalisé

Commençons simplement et construisons un serveur de base. Vous savez probablement déjà comment créer un serveur natif dans Node.js :

```js
const server = http.createServer((req, res) => {
   app.hook(req, res);
});
```

Ici, nous introduisons un objet `app` avec une fonction `hook` (que nous implémenterons bientôt). C'est là que le serveur redirige `req` et `res` vers notre routeur personnalisé. Ce **hook** est le point de rencontre—l'interaction entre le serveur et le routeur (mux).

### Squelette de base du multiplexeur

Commençons par créer la structure de notre mux :

```js
function serverMux() {
  function hook(req, res) {
    // À implémenter
  }
  return {
    hook
  };
}

const app = serverMux();

const server = http.createServer((req, res) => {
  app.hook(req, res);
});
```

### La fonction Hook

La fonction `hook` est notre intermédiaire entre le serveur et le mux. Elle reçoit les objets de requête (`req`) et de réponse (`res`) du serveur et les transmet à notre mux :

```js
function hook(req, res) {
    requestsQueue.push(requestWrapper(req, res));
    console.log("nouvelle requête !");
    processRequests();
}
```

Ici, nous avons introduit quelques nouvelles choses :

* `requestWrapper` : Une fonction pour envelopper `req` et `res`.
    
* `processRequests` : Une fonction pour gérer le traitement des requêtes.
    
* `requestsQueue` : Un tableau JavaScript de base qui servira de file d'attente pour le traitement des requêtes.
    

Mettons à jour `serverMux` pour refléter cela :

```js
function serverMux() {
    const requestsQueue = [];
    
    async function processRequests() {
      // À implémenter
    }

    function hook(req, res) {
      requestsQueue.push(requestWrapper(req, res));
      console.log("nouvelle requête !");
      processRequests();
    }

    return {
      hook
    };
}
```

### Pourquoi utiliser une file d'attente ?

Vous vous demandez peut-être pourquoi nous utilisons une file d'attente au lieu de traiter les requêtes immédiatement comme le fait Express avec `app.handle`. Eh bien, stocker les requêtes dans une file d'attente aide à simuler une boucle d'événements. Cela nous donnera une meilleure visibilité sur la manière dont les requêtes sont traitées, une par une.

#### Opérations de la file d'attente

Une file d'attente est une structure de données de type premier entré, premier sorti (FIFO). Tout comme une file d'attente dans un magasin, la requête qui arrive en premier est traitée en premier.

Dans notre cas, `requestsQueue` est un tableau. Voici comment nous allons gérer l'ajout et le retrait de la file d'attente :

* **Ajouter (push)** : Nous ajoutons les requêtes à la file d'attente avec `requestsQueue.push(requestWrapper(req, res));`
    
* **Retirer (shift)** : Nous retirons la prochaine requête de la file d'attente avec `const c = requestsQueue.shift();`
    

### Enveloppe de requête

La fonction `requestWrapper` est un utilitaire simple qui enveloppe les objets `req` et `res` entrants et extrait certaines informations utiles :

```js
function requestWrapper(req, res) {
    return {
      url: req.url,
      method: req.method,
      req,
      res
    };
}
```

Dans des frameworks plus avancés comme [Hono.js](https://hono.dev/), l'enveloppe de requête peut ajouter des fonctionnalités supplémentaires, telles que des méthodes d'assistance pour définir les en-têtes ou analyser le contenu du corps. Pour l'instant, nous gardons les choses simples et retournons simplement la requête et la réponse avec l'URL et la méthode.

### Test de la file d'attente

Testons cela en enregistrant la file d'attente des requêtes à chaque nouvelle requête. Mettez à jour votre fonction `hook` :

```js
function hook(req, res) {
    requestsQueue.push(requestWrapper(req, res));
    console.log("Nouvelle requête en file d'attente !", requestsQueue);
    processRequests();
}
```

Démarrez le serveur avec :

```bash
node index.js
```

Maintenant, ouvrez un autre terminal et faites une requête au serveur :

```bash
curl http://localhost:3000
```

Vous devriez voir la file d'attente enregistrée dans la console. Le terminal peut sembler bloqué car nous n'avons pas encore répondu à la requête. Vous pouvez quitter le processus manuellement pour l'instant.

### Traitement des requêtes

Voici la fonction complète `processRequests` :

```js
async function processRequests() {
    while (requestsQueue.length > 0) {
        const c = requestsQueue.shift();
        if (c) {
            const handler = lookupTable[c.url] || lookupTable["/notfound"];
            if (handler) {
                (async function() {
                    handler(c.req, c.res);
                })();
            } else {
                console.log("Gestionnaire introuvable manquant !");
            }
        }
    }
}
```

Décomposons cela :

1. **Traitement de la file d'attente** : Nous parcourons la file d'attente, retirant chaque requête une par une.
    
2. **Recherche du gestionnaire** : Pour chaque requête, nous vérifions si un gestionnaire existe dans le `lookupTable` pour l'URL. Si ce n'est pas le cas, nous utilisons un gestionnaire `/notfound`.
    
3. **Exécution du gestionnaire** : Nous exécutons le gestionnaire, en passant les objets de requête et de réponse.
    

### Table de recherche et gestionnaires

Nous avons besoin d'un moyen de mapper les URL à leurs gestionnaires respectifs. C'est là que le `lookupTable` intervient :

```js
const lookupTable = {
    "/": (req, res) => {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello, World!\n');
    },
    "/notfound": (req, res) => {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found\n');
    }
};
```

Lorsque qu'une requête arrive, nous vérifions si l'URL correspond à une entrée dans la table. Si c'est le cas, nous appelons la fonction de gestionnaire correspondante.

Par exemple, appeler `curl http://localhost:3000` atteindra la route `/` et retournera "Hello, World!". Si vous appelez une route inexistante comme `/random`, cela déclenchera le gestionnaire 404.

### Enregistrement des gestionnaires

Enfin, ajoutons une méthode pour enregistrer de nouveaux gestionnaires de manière dynamique :

```js
function serverMux() {
  const lookupTable = {};

  function registerHandler(path, handler) {
    if (typeof path !== 'string' || !path) {
      throw new Error("Le chemin doit être une chaîne non vide");
    }
    if (typeof handler !== 'function') {
      throw new Error("Le gestionnaire doit être une fonction");
    }
    lookupTable[path] = handler;
  }

  return {
    hook,
    registerHandler
  };
}
```

Maintenant, nous pouvons enregistrer dynamiquement de nouvelles routes avec leurs gestionnaires :

```js
app.registerHandler("/", (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Page d\'accueil\n');
});

app.registerHandler("/about", (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('À propos de nous\n');
});
```

Voici un exemple complet de `registerHandler` en action :

```js
const app = serverMux();

app.registerHandler("/", (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, World!');
});

app.registerHandler("/about", (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>À propos de nous</h1>');
});

app.registerHandler("/contact", (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Contactez-nous</h1>');
});

app.registerHandler("/api/data", (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ message: 'Données de l\'API' }));
});

app.registerHandler("/notfound", (req, res) => {
  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('404 Non trouvé');
});

const server = http.createServer((req, res) => {
  console.log(req.url);
  app.hook(req, res);
});
```

Remarquez à quel point cela ressemble à Express ?

```js
app.get("/", (req, res) => {

});
```

Juste un peu plus verbeux !

Maintenant, exécutez le serveur et testez-le en collant ceci dans votre terminal :

```bash
for /l %i in (1,1,100) do curl -X GET http://localhost:3000
```

Cela enverra 100 requêtes. Essayez d'ouvrir deux terminaux ou plus et d'exécuter la même commande simultanément pour voir comment votre serveur gère la charge.

Félicitations ! Vous avez construit un multiplexeur de serveur (mux) de base. Cela ne révolutionnera peut-être pas le monde, mais c'est un bon point de départ pour comprendre comment fonctionne le routage dans les frameworks web.

# Conclusion

Dans cet article, nous avons plongé en profondeur dans le concept des frameworks côté serveur, en utilisant Express comme notre exemple principal. Nous l'avons traqué depuis ses abstractions de haut niveau jusqu'au serveur TCP natif construit en C++. Ensuite, pour ancrer ces idées, nous avons construit notre propre multiplexeur de serveur simple.

C'est un exercice d'apprentissage puissant, car nous avons enlevé la magie et creusé jusqu'au cœur de comment les choses fonctionnent. Bien que cet exemple ne soit que la pointe de l'iceberg, il vous donne les outils pour explorer encore plus profondément. Pour un défi, regardez comment Express gère la correspondance de motifs et l'enregistrement des routes—essayez d'améliorer notre simple multiplexeur !

J'ai laissé de côté des sujets plus avancés comme la mise à jour de notre file d'attente avec une liste chaînée et la simulation de requêtes concurrentes, donc c'est quelque chose que vous pouvez explorer.

Merci d'avoir lu ! J'espère que vous avez apprécié cette exploration autant que j'ai aimé l'écrire. Si vous avez des pensées, des questions, ou si vous voulez simplement vous connecter, je suis sur [x](https://x.com/codelit09), n'hésitez pas à me contacter.

Et bien sûr, profitez de votre fuseau horaire !