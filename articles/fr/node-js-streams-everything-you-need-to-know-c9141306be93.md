---
title: 'Node.js Streams : Tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-23T05:01:05.000Z'
originalURL: https://freecodecamp.org/news/node-js-streams-everything-you-need-to-know-c9141306be93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SGJw31T5Q9Zfsk24l2yirg.gif
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
seo_title: 'Node.js Streams : Tout ce que vous devez savoir'
seo_desc: "By Samer Buna\n\nUpdate: This article is now part of my book “Node.js Beyond\
  \ The Basics”.  \nRead the updated version of this content and more about Node at\
  \ jscomplete.com/node-beyond-basics.\n\nNode.js streams have a reputation for being\
  \ hard to work wit..."
---

Par Samer Buna

> **Mise à jour :** Cet article fait désormais partie de mon livre « Node.js Beyond The Basics ».  
>   
> Lisez la version mise à jour de ce contenu et plus sur Node à [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/g/node-streams).

Les streams de Node.js ont la réputation d'être difficiles à utiliser et encore plus difficiles à comprendre. Eh bien, j'ai une bonne nouvelle pour vous — ce n'est plus le cas.

Au fil des années, les développeurs ont créé de nombreux packages dans le but de faciliter le travail avec les streams. Mais dans cet article, je vais me concentrer sur l'API native des streams de [Node.js](https://nodejs.org/api/stream.html).

> « Les streams sont l'idée la plus mal comprise et la meilleure de Node. »  
>   
> — Dominic Tarr

### Que sont exactement les streams ?

Les streams sont des collections de données — tout comme les tableaux ou les chaînes de caractères. La différence est que les streams peuvent ne pas être disponibles en une seule fois, et ils n'ont pas besoin de tenir en mémoire. Cela rend les streams vraiment puissants lorsque l'on travaille avec de grandes quantités de données, ou des données qui proviennent d'une source externe un _morceau_ à la fois.

Cependant, les streams ne concernent pas seulement le travail avec de grandes données. Ils nous donnent également le pouvoir de la composabilité dans notre code. Tout comme nous pouvons composer des commandes Linux puissantes en enchaînant d'autres commandes Linux plus petites, nous pouvons faire exactement la même chose dans Node avec les streams.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fp3dyVZckIUjPFOp58x-zQ.png)
_Composabilité avec les commandes Linux_

```js
const grep = ... // Un stream pour la sortie de grep
const wc = ... // Un stream pour l'entrée de wc

grep.pipe(wc)
```

De nombreux modules intégrés dans Node implémentent l'interface de streaming :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lhOvZiDrVbzF8_l8QX3ACw.png)
_Capture d'écran de mon cours Pluralsight — Advanced Node.js_

La liste ci-dessus contient quelques exemples d'objets natifs de Node.js qui sont également des streams lisibles et inscriptibles. Certains de ces objets sont à la fois des streams lisibles et inscriptibles, comme les sockets TCP, les streams zlib et crypto.

Remarquez que les objets sont également étroitement liés. Alors qu'une réponse HTTP est un stream lisible sur le client, c'est un stream inscriptible sur le serveur. Cela est dû au fait que dans le cas HTTP, nous lisons essentiellement à partir d'un objet (`http.IncomingMessage`) et écrivons dans un autre (`http.ServerResponse`).

Notez également comment les streams `stdio` (`stdin`, `stdout`, `stderr`) ont les types de streams inverses lorsqu'il s'agit de processus enfants. Cela permet une manière vraiment facile de pipeliner vers et depuis ces streams à partir des streams `stdio` du processus principal.

### Un exemple pratique de streams

La théorie est formidable, mais souvent pas convaincante à 100 %. Voyons un exemple démontrant la différence que les streams peuvent faire en termes de consommation de mémoire.

Créons d'abord un gros fichier :

```js
const fs = require('fs');
const file = fs.createWriteStream('./big.file');

for(let i=0; i<= 1e6; i++) {
  file.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n');
}

file.end();
```

Regardez ce que j'ai utilisé pour créer ce gros fichier. Un stream inscriptible !

Le module `fs` peut être utilisé pour lire et écrire dans des fichiers en utilisant une interface de stream. Dans l'exemple ci-dessus, nous écrivons dans ce `big.file` via un stream inscriptible avec 1 million de lignes dans une boucle.

L'exécution du script ci-dessus génère un fichier d'environ ~400 Mo.

Voici un simple serveur web Node conçu pour servir exclusivement le `big.file` :

```js
const fs = require('fs');
const server = require('http').createServer();

server.on('request', (req, res) => {
  fs.readFile('./big.file', (err, data) => {
    if (err) throw err;
  
    res.end(data);
  });
});

server.listen(8000);
```

Lorsque le serveur reçoit une requête, il servira le gros fichier en utilisant la méthode asynchrone `fs.readFile`. Mais attendez, ce n'est pas comme si nous bloquions la boucle d'événements ou autre chose. Tout est parfait, n'est-ce pas ? N'est-ce pas ?

Eh bien, voyons ce qui se passe lorsque nous exécutons le serveur, nous y connectons et surveillons la mémoire pendant ce temps.

Lorsque j'ai exécuté le serveur, il a commencé avec une quantité normale de mémoire, 8,7 Mo :

![Image](https://cdn-media-1.freecodecamp.org/images/1*125_8HQ4KzJkeBcj1LcEiQ.png)

Ensuite, je me suis connecté au serveur. Remarquez ce qui est arrivé à la mémoire consommée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SGJw31T5Q9Zfsk24l2yirg.gif)

Wow — la consommation de mémoire a bondi à 434,8 Mo.

Nous avons essentiellement mis tout le contenu du `big.file` en mémoire avant de l'écrire dans l'objet de réponse. Cela est très inefficace.

L'objet de réponse HTTP (`res` dans le code ci-dessus) est également un stream inscriptible. Cela signifie que si nous avons un stream lisible qui représente le contenu de `big.file`, nous pouvons simplement pipeliner ces deux streams l'un dans l'autre et obtenir un résultat presque identique sans consommer ~400 Mo de mémoire.

Le module `fs` de Node peut nous donner un stream lisible pour n'importe quel fichier en utilisant la méthode `createReadStream`. Nous pouvons pipeliner cela vers l'objet de réponse :

```js
const fs = require('fs');
const server = require('http').createServer();

server.on('request', (req, res) => {
  const src = fs.createReadStream('./big.file');
  src.pipe(res);
});

server.listen(8000);
```

Maintenant, lorsque vous vous connectez à ce serveur, une chose magique se produit (regardez la consommation de mémoire) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*iWNNIMhF9QmD25Vho6-fRQ.gif)

_Qu'est-ce qui se passe ?_

Lorsque qu'un client demande ce gros fichier, nous le streamons un morceau à la fois, ce qui signifie que nous ne le mettons pas du tout en mémoire tampon. L'utilisation de la mémoire a augmenté d'environ 25 Mo et c'est tout.

Vous pouvez pousser cet exemple à ses limites. Régénérez le `big.file` avec cinq millions de lignes au lieu d'un million, ce qui porterait le fichier à bien plus de 2 Go, et c'est en fait plus grand que la limite de mémoire tampon par défaut dans Node.

Si vous essayez de servir ce fichier en utilisant `fs.readFile`, vous ne pouvez tout simplement pas le faire, par défaut (vous pouvez changer les limites). Mais avec `fs.createReadStream`, il n'y a aucun problème à streamer 2 Go de données vers le demandeur, et surtout, l'utilisation de la mémoire du processus sera à peu près la même.

Prêt à apprendre les streams maintenant ?

> Cet article est une transcription d'une partie de [mon cours Pluralsight sur Node.js](https://www.pluralsight.com/courses/nodejs-advanced). J'y couvre un contenu similaire en format vidéo.

### Streams 101

Il existe quatre types fondamentaux de streams dans Node.js : Readable, Writable, Duplex et Transform streams.

* Un stream lisible est une abstraction pour une source à partir de laquelle des données peuvent être consommées. Un exemple de cela est la méthode `fs.createReadStream`.
* Un stream inscriptible est une abstraction pour une destination vers laquelle des données peuvent être écrites. Un exemple de cela est la méthode `fs.createWriteStream`.
* Un stream duplex est à la fois lisible et inscriptible. Un exemple de cela est une socket TCP.
* Un stream de transformation est essentiellement un stream duplex qui peut être utilisé pour modifier ou transformer les données au fur et à mesure qu'elles sont écrites et lues. Un exemple de cela est le stream `zlib.createGzip` pour compresser les données en utilisant gzip. Vous pouvez penser à un stream de transformation comme à une fonction où l'entrée est la partie du stream inscriptible et la sortie est la partie du stream lisible. Vous pourriez également entendre parler de streams de transformation sous le nom de « through streams ».

Tous les streams sont des instances de `EventEmitter`. Ils émettent des événements qui peuvent être utilisés pour lire et écrire des données. Cependant, nous pouvons consommer les données des streams de manière plus simple en utilisant la méthode `pipe`.

#### La méthode pipe

Voici la ligne magique que vous devez retenir :

```js
readableSrc.pipe(writableDest)
```

Dans cette simple ligne, nous pipelinons la sortie d'un stream lisible — la source de données, comme l'entrée d'un stream inscriptible — la destination. La source doit être un stream lisible et la destination doit être un stream inscriptible. Bien sûr, ils peuvent tous deux être des streams duplex/transform. En fait, si nous pipelinons dans un stream duplex, nous pouvons enchaîner les appels de pipe comme nous le faisons dans Linux :

```js
readableSrc
  .pipe(transformStream1)
  .pipe(transformStream2)
  .pipe(finalWrtitableDest)
```

La méthode `pipe` retourne le stream de destination, ce qui nous permet de faire l'enchaînement ci-dessus. Pour les streams `a` (lisible), `b` et `c` (duplex), et `d` (inscriptible), nous pouvons :

```js
a.pipe(b).pipe(c).pipe(d)

# Ce qui est équivalent à :
a.pipe(b)
b.pipe(c)
c.pipe(d)

# Ce qui, dans Linux, est équivalent à :
$ a | b | c | d
```

La méthode `pipe` est le moyen le plus simple de consommer des streams. Il est généralement recommandé d'utiliser soit la méthode `pipe`, soit de consommer des streams avec des événements, mais d'éviter de mélanger ces deux approches. Habituellement, lorsque vous utilisez la méthode `pipe`, vous n'avez pas besoin d'utiliser des événements, mais si vous avez besoin de consommer les streams de manière plus personnalisée, les événements seraient la voie à suivre.

#### Événements des streams

Outre la lecture à partir d'une source de stream lisible et l'écriture vers une destination inscriptible, la méthode `pipe` gère automatiquement quelques choses en cours de route. Par exemple, elle gère les erreurs, les fins de fichiers et les cas où un stream est plus lent ou plus rapide que l'autre.

Cependant, les streams peuvent également être consommés avec des événements directement. Voici le code équivalent simplifié en événements de ce que la méthode `pipe` fait principalement pour lire et écrire des données :

```js
# readable.pipe(writable)

readable.on('data', (chunk) => {
  writable.write(chunk);
});

readable.on('end', () => {
  writable.end();
});
```

Voici une liste des événements et fonctions importants qui peuvent être utilisés avec les streams lisibles et inscriptibles :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HGXpeiF5-hJrOk_8tT2jFA.png)
_Capture d'écran de mon cours Pluralsight - Advanced Node.js_

Les événements et fonctions sont quelque peu liés car ils sont généralement utilisés ensemble.

Les événements les plus importants sur un stream lisible sont :

* L'événement `data`, qui est émis chaque fois que le stream transmet un morceau de données au consommateur
* L'événement `end`, qui est émis lorsqu'il n'y a plus de données à consommer à partir du stream.

Les événements les plus importants sur un stream inscriptible sont :

* L'événement `drain`, qui est un signal que le stream inscriptible peut recevoir plus de données.
* L'événement `finish`, qui est émis lorsque toutes les données ont été vidées vers le système sous-jacent.

Les événements et fonctions peuvent être combinés pour une utilisation personnalisée et optimisée des streams. Pour consommer un stream lisible, nous pouvons utiliser les méthodes `pipe`/`unpipe`, ou les méthodes `read`/`unshift`/`resume`. Pour consommer un stream inscriptible, nous pouvons en faire la destination de `pipe`/`unpipe`, ou simplement y écrire avec la méthode `write` et appeler la méthode `end` lorsque nous avons terminé.

#### Modes en Pause et en Flux des Streams Lisibles

Les streams lisibles ont deux modes principaux qui affectent la manière dont nous pouvons les consommer :

* Ils peuvent être soit en mode **pause**
* Soit en mode **flux**

Ces modes sont parfois appelés modes pull et push.

Tous les streams lisibles commencent en mode pause par défaut, mais ils peuvent être facilement basculés en mode flux et revenir en mode pause lorsque nécessaire. Parfois, le basculement se fait automatiquement.

Lorsque qu'un stream lisible est en mode pause, nous pouvons utiliser la méthode `read()` pour lire à partir du stream à la demande, cependant, pour un stream lisible en mode flux, les données circulent en continu et nous devons écouter les événements pour les consommer.

En mode flux, les données peuvent en fait être perdues si aucun consommateur n'est disponible pour les traiter. C'est pourquoi, lorsque nous avons un stream lisible en mode flux, nous avons besoin d'un gestionnaire d'événements `data`. En fait, le simple fait d'ajouter un gestionnaire d'événements `data` bascule un stream en pause en mode flux et le fait de supprimer le gestionnaire d'événements `data` bascule le stream en mode pause. Certaines de ces actions sont effectuées pour la compatibilité ascendante avec l'ancienne interface des streams de Node.

Pour basculer manuellement entre ces deux modes de stream, vous pouvez utiliser les méthodes `resume()` et `pause()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HI-mtispQ13qm8ib5yey3g.png)
_Capture d'écran de mon cours Pluralsight — Advanced Node.js_

Lorsque vous consommez des streams lisibles en utilisant la méthode `pipe`, vous n'avez pas à vous soucier de ces modes car `pipe` les gère automatiquement.

### Implémentation des Streams

Lorsque nous parlons de streams dans Node.js, il y a deux tâches principales différentes :

* La tâche d'**implémentation** des streams.
* La tâche de **consommation** de ceux-ci.

Jusqu'à présent, nous n'avons parlé que de la consommation de streams. Implémentons-en quelques-uns !

Les implémenteurs de streams sont généralement ceux qui `require` le module `stream`.

#### Implémentation d'un Stream Inscriptible

Pour implémenter un stream inscriptible, nous devons utiliser le constructeur `Writable` du module stream.

```
const { Writable } = require('stream');
```

Nous pouvons implémenter un stream inscriptible de nombreuses manières. Nous pouvons, par exemple, étendre le constructeur `Writable` si nous le souhaitons

```js
class myWritableStream extends Writable {
}
```

Cependant, je préfère l'approche plus simple du constructeur. Nous créons simplement un objet à partir du constructeur `Writable` et lui passons un certain nombre d'options. La seule option requise est une fonction `write` qui expose le morceau de données à écrire.

```js
const { Writable } = require('stream');

const outStream = new Writable({
  write(chunk, encoding, callback) {
    console.log(chunk.toString());
    callback();
  }
});

process.stdin.pipe(outStream);
```

Cette méthode write prend trois arguments.

* Le **chunk** est généralement un buffer sauf si nous configurons le stream différemment.
* L'argument **encoding** est nécessaire dans ce cas, mais généralement nous pouvons l'ignorer.
* Le **callback** est une fonction que nous devons appeler après avoir terminé le traitement du morceau de données. C'est ce qui signale si l'écriture a réussi ou non. Pour signaler un échec, appelez le callback avec un objet d'erreur.

Dans `outStream`, nous faisons simplement un `console.log` du chunk en tant que chaîne et appelons le `callback` après cela sans erreur pour indiquer le succès. C'est un stream _echo_ très simple et probablement pas très utile. Il renverra tout ce qu'il reçoit.

Pour consommer ce stream, nous pouvons simplement l'utiliser avec `process.stdin`, qui est un stream lisible, donc nous pouvons simplement pipeliner `process.stdin` dans notre `outStream`.

Lorsque nous exécutons le code ci-dessus, tout ce que nous tapons dans `process.stdin` sera renvoyé en utilisant la ligne `console.log` de `outStream`.

Ce n'est pas un stream très utile à implémenter car il est déjà implémenté et intégré. Cela est très similaire à `process.stdout`. Nous pouvons simplement pipeliner `stdin` dans `stdout` et nous obtiendrons exactement la même fonctionnalité d'écho avec cette seule ligne :

```js
process.stdin.pipe(process.stdout);
```

#### Implémenter un Stream Lisible

Pour implémenter un stream lisible, nous avons besoin de l'interface `Readable`, et nous construisons un objet à partir de celle-ci, et nous implémentons une méthode `read()` dans le paramètre de configuration du stream :

```js
const { Readable } = require('stream');

const inStream = new Readable({
  read() {}
});
```

Il existe une manière simple d'implémenter des streams lisibles. Nous pouvons simplement `push` directement les données que nous voulons que les consommateurs consomment.

```js
const { Readable } = require('stream'); 

const inStream = new Readable({
  read() {}
});

inStream.push('ABCDEFGHIJKLM');
inStream.push('NOPQRSTUVWXYZ');

inStream.push(null); // Plus de données

inStream.pipe(process.stdout);
```

Lorsque nous `push` un objet `null`, cela signifie que nous voulons signaler que le stream n'a plus de données.

Pour consommer ce simple stream lisible, nous pouvons simplement le pipeliner dans le stream inscriptible `process.stdout`.

Lorsque nous exécutons le code ci-dessus, nous lirons toutes les données de `inStream` et les échoierons vers la sortie standard. Très simple, mais aussi pas très efficace.

Nous poussons essentiellement toutes les données dans le stream _avant_ de le pipeliner vers `process.stdout`. La meilleure façon est de pousser les données _à la demande_, lorsqu'un consommateur les demande. Nous pouvons faire cela en implémentant la méthode `read()` dans l'objet de configuration :

```js
const inStream = new Readable({
  read(size) {
    // il y a une demande sur les données... Quelqu'un veut les lire.
  }
});
```

Lorsque la méthode read est appelée sur un stream lisible, l'implémentation peut pousser des données partielles dans la file d'attente. Par exemple, nous pouvons pousser une lettre à la fois, en commençant par le code de caractère 65 (qui représente A), et en l'incrémentant à chaque push :

```js
const inStream = new Readable({
  read(size) {
    this.push(String.fromCharCode(this.currentCharCode++));
    if (this.currentCharCode > 90) {
      this.push(null);
    }
  }
});

inStream.currentCharCode = 65;

inStream.pipe(process.stdout);
```

Pendant que le consommateur lit un stream lisible, la méthode `read` continuera à se déclencher, et nous pousserons plus de lettres. Nous devons arrêter ce cycle quelque part, et c'est pourquoi une instruction if pour pousser null lorsque le currentCharCode est supérieur à 90 (qui représente Z).

Ce code est équivalent au plus simple avec lequel nous avons commencé, mais maintenant nous poussons les données à la demande lorsque le consommateur les demande. Vous devriez toujours faire cela.

#### Implémentation de Streams Duplex/Transform

Avec les streams Duplex, nous pouvons implémenter à la fois des streams lisibles et inscriptibles avec le même objet. C'est comme si nous héritions des deux interfaces.

Voici un exemple de stream duplex qui combine les deux exemples inscriptibles et lisibles implémentés ci-dessus :

```js
const { Duplex } = require('stream');

const inoutStream = new Duplex({
  write(chunk, encoding, callback) {
    console.log(chunk.toString());
    callback();
  },

  read(size) {
    this.push(String.fromCharCode(this.currentCharCode++));
    if (this.currentCharCode > 90) {
      this.push(null);
    }
  }
});

inoutStream.currentCharCode = 65;

process.stdin.pipe(inoutStream).pipe(process.stdout);
```

En combinant les méthodes, nous pouvons utiliser ce stream duplex pour lire les lettres de A à Z et nous pouvons également l'utiliser pour sa fonctionnalité d'écho. Nous pipelinons le stream lisible `stdin` dans ce stream duplex pour utiliser la fonctionnalité d'écho et nous pipelinons le stream duplex lui-même dans le stream inscriptible `stdout` pour voir les lettres A à Z.

Il est important de comprendre que les côtés lisibles et inscriptibles d'un stream duplex fonctionnent complètement indépendamment l'un de l'autre. Ce n'est qu'un regroupement de deux fonctionnalités dans un objet.

Un stream de transformation est le stream duplex le plus intéressant car sa sortie est calculée à partir de son entrée.

Pour un stream de transformation, nous n'avons pas besoin d'implémenter les méthodes `read` ou `write`, nous devons seulement implémenter une méthode `transform`, qui combine les deux. Elle a la signature de la méthode `write` et nous pouvons l'utiliser pour `push` des données également.

Voici un simple stream de transformation qui renvoie tout ce que vous tapez après l'avoir transformé en majuscules :

```js
const { Transform } = require('stream');

const upperCaseTr = new Transform({
  transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase());
    callback();
  }
});

process.stdin.pipe(upperCaseTr).pipe(process.stdout);
```

Dans ce stream de transformation, que nous consommons exactement comme l'exemple de stream duplex précédent, nous avons seulement implémenté une méthode `transform()`. Dans cette méthode, nous convertissons le `chunk` en sa version en majuscules puis nous `push` cette version comme partie lisible.

#### Mode Objet des Streams

Par défaut, les streams attendent des valeurs Buffer/String. Il existe un flag `objectMode` que nous pouvons définir pour que le stream accepte n'importe quel objet JavaScript.

Voici un simple exemple pour démontrer cela. La combinaison suivante de streams de transformation permet de mapper une chaîne de valeurs séparées par des virgules en un objet JavaScript. Ainsi, « a,b,c,d » devient {a: b, c: d}.

```js
const { Transform } = require('stream');

const commaSplitter = new Transform({
  readableObjectMode: true,
  
  transform(chunk, encoding, callback) {
    this.push(chunk.toString().trim().split(','));
    callback();
  }
});

const arrayToObject = new Transform({
  readableObjectMode: true,
  writableObjectMode: true,
  
  transform(chunk, encoding, callback) {
    const obj = {};
    for(let i=0; i < chunk.length; i+=2) {
      obj[chunk[i]] = chunk[i+1];
    }
    this.push(obj);
    callback();
  }
});

const objectToString = new Transform({
  writableObjectMode: true,
  
  transform(chunk, encoding, callback) {
    this.push(JSON.stringify(chunk) + '\n');
    callback();
  }
});

process.stdin
  .pipe(commaSplitter)
  .pipe(arrayToObject)
  .pipe(objectToString)
  .pipe(process.stdout)
```

Nous passons la chaîne d'entrée (par exemple, « a,b,c,d ») à travers `commaSplitter` qui pousse un tableau comme ses données lisibles (`["a", "b", "c", "d"]`). L'ajout du flag `readableObjectMode` sur ce stream est nécessaire car nous y poussons un objet, pas une chaîne.

Nous prenons ensuite le tableau et le pipelinons dans le stream `arrayToObject`. Nous avons besoin d'un flag `writableObjectMode` pour que ce stream accepte un objet. Il poussera également un objet (le tableau d'entrée mappé en un objet) et c'est pourquoi nous avions également besoin du flag `readableObjectMode` là aussi. Le dernier stream `objectToString` accepte un objet mais pousse une chaîne, et c'est pourquoi nous avions seulement besoin d'un flag `writableObjectMode` là. La partie lisible est une chaîne normale (l'objet stringifié).

![Image](https://cdn-media-1.freecodecamp.org/images/1*u2kQzUD0ruPpt-xx0UOHoA.png)
_Utilisation de l'exemple ci-dessus_

#### Streams de transformation intégrés de Node

Node dispose de quelques streams de transformation intégrés très utiles. Notamment, les streams zlib et crypto.

Voici un exemple qui utilise le stream `zlib.createGzip()` combiné avec les streams lisibles/inscriptibles `fs` pour créer un script de compression de fichiers :

```js
const fs = require('fs');
const zlib = require('zlib');
const file = process.argv[2];

fs.createReadStream(file)
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream(file + '.gz'));
```

Vous pouvez utiliser ce script pour gzipper n'importe quel fichier que vous passez en argument. Nous pipelinons un stream lisible pour ce fichier dans le stream de transformation zlib intégré puis dans un stream inscriptible pour le nouveau fichier gzippé. Simple.

Le côté cool de l'utilisation des pipes est que nous pouvons en fait les combiner avec des événements si nous en avons besoin. Par exemple, si je veux que l'utilisateur voie un indicateur de progression pendant que le script fonctionne et un message « Terminé » lorsque le script est terminé. Puisque la méthode `pipe` retourne le stream de destination, nous pouvons également enchaîner l'enregistrement des gestionnaires d'événements :

```js
const fs = require('fs');
const zlib = require('zlib');
const file = process.argv[2];

fs.createReadStream(file)
  .pipe(zlib.createGzip())
  .on('data', () => process.stdout.write('.'))
  .pipe(fs.createWriteStream(file + '.zz'))
  .on('finish', () => console.log('Terminé'));
```

Ainsi, avec la méthode `pipe`, nous pouvons facilement consommer des streams, mais nous pouvons toujours personnaliser davantage notre interaction avec ces streams en utilisant des événements si nécessaire.

Ce qui est génial avec la méthode `pipe`, c'est que nous pouvons l'utiliser pour _composer_ notre programme pièce par pièce, de manière beaucoup plus lisible. Par exemple, au lieu d'écouter l'événement `data` ci-dessus, nous pouvons simplement créer un stream de transformation pour rapporter la progression, et remplacer l'appel `.on()` par un autre appel `.pipe()` :

```js
const fs = require('fs');
const zlib = require('zlib');
const file = process.argv[2];

const { Transform } = require('stream');

const reportProgress = new Transform({
  transform(chunk, encoding, callback) {
    process.stdout.write('.');
    callback(null, chunk);
  }
});

fs.createReadStream(file)
  .pipe(zlib.createGzip())
  .pipe(reportProgress)
  .pipe(fs.createWriteStream(file + '.zz'))
  .on('finish', () => console.log('Terminé'));
```

Ce stream `reportProgress` est un simple stream pass-through, mais il rapporte également la progression à la sortie standard. Remarquez comment j'ai utilisé le deuxième argument dans la fonction `callback()` pour pousser les données à l'intérieur de la méthode `transform()`. Cela est équivalent à pousser les données en premier.

Les applications de la combinaison de streams sont sans fin. Par exemple, si nous devons chiffrer le fichier avant ou après l'avoir gzippé, tout ce que nous avons à faire est de pipeliner un autre stream de transformation dans cet ordre exact dont nous avons besoin. Nous pouvons utiliser le module `crypto` de Node pour cela :

```js
const crypto = require('crypto');
// ...

fs.createReadStream(file)
  .pipe(zlib.createGzip())
  .pipe(crypto.createCipher('aes192', 'a_secret'))
  .pipe(reportProgress)
  .pipe(fs.createWriteStream(file + '.zz'))
  .on('finish', () => console.log('Terminé'));
```

Le script ci-dessus compresse puis chiffrer le fichier passé et seuls ceux qui ont le secret peuvent utiliser le fichier généré. Nous ne pouvons pas décompresser ce fichier avec les utilitaires de décompression normaux car il est chiffré.

Pour pouvoir réellement décompresser tout ce qui est compressé avec le script ci-dessus, nous devons utiliser les streams opposés pour crypto et zlib dans l'ordre inverse, ce qui est simple :

```js
fs.createReadStream(file)
  .pipe(crypto.createDecipher('aes192', 'a_secret'))
  .pipe(zlib.createGunzip())
  .pipe(reportProgress)
  .pipe(fs.createWriteStream(file.slice(0, -3)))
  .on('finish', () => console.log('Terminé'));
```

En supposant que le fichier passé est la version compressée, le code ci-dessus créera un stream de lecture à partir de celui-ci, le pipelinera dans le stream crypto `createDecipher()` (en utilisant le même secret), pipelinera la sortie de celui-ci dans le stream zlib `createGunzip()`, puis écrira les choses en retour dans un fichier sans la partie extension.

C'est tout ce que j'ai pour ce sujet. Merci d'avoir lu ! À la prochaine !

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)