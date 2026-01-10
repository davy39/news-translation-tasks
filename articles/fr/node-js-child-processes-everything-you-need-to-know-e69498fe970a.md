---
title: 'Processus enfants Node.js : Tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-08T20:08:22.000Z'
originalURL: https://freecodecamp.org/news/node-js-child-processes-everything-you-need-to-know-e69498fe970a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I56pPhzO1VQw8SIsv8wYNA.png
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
seo_title: 'Processus enfants Node.js : Tout ce que vous devez savoir'
seo_desc: "By Samer Buna\nHow to use spawn(), exec(), execFile(), and fork()\n\nUpdate:\
  \ This article is now part of my book “Node.js Beyond The Basics”.  \nRead the updated\
  \ version of this content and more about Node at jscomplete.com/node-beyond-basics.\n\
  \nSingle-th..."
---

Par Samer Buna

#### Comment utiliser spawn(), exec(), execFile(), et fork()  


> **Mise à jour :** Cet article fait maintenant partie de mon livre « Node.js Beyond The Basics ».  
>   
> Lisez la version mise à jour de ce contenu et plus sur Node à [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/g/node-cps).

Les performances single-thread et non-bloquantes de Node.js fonctionnent très bien pour un seul processus. Mais finalement, un seul processus sur un seul CPU ne suffira pas à gérer la charge de travail croissante de votre application.

Peu importe la puissance de votre serveur, un seul thread ne peut supporter qu'une charge limitée.

Le fait que Node.js s'exécute dans un seul thread ne signifie pas que nous ne pouvons pas tirer parti de plusieurs processus et, bien sûr, de plusieurs machines également.

L'utilisation de plusieurs processus est le meilleur moyen de mettre à l'échelle une application Node. Node.js est conçu pour construire des applications distribuées avec de nombreux nœuds. C'est pourquoi il est nommé _Node_. L'évolutivité est intégrée à la plateforme et ce n'est pas quelque chose que vous commencez à penser plus tard dans la durée de vie d'une application.

> Cet article est une rédaction d'une partie de [mon cours Pluralsight sur Node.js](https://www.pluralsight.com/courses/nodejs-advanced). Je couvre un contenu similaire en format vidéo là-bas.

Veuillez noter que vous aurez besoin d'une bonne compréhension des événements et des flux de Node.js avant de lire cet article. Si ce n'est pas déjà fait, je vous recommande de lire ces deux autres articles avant de lire celui-ci :

**[Comprendre l'architecture pilotée par événements de Node.js](https://www.freecodecamp.org/news/understanding-node-js-event-driven-architecture-223292fcbc2d/)**  
_[La plupart des objets de Node — comme les requêtes HTTP, les réponses et les flux — implémentent le module EventEmitter pour qu'ils puissent...](https://www.freecodecamp.org/news/understanding-node-js-event-driven-architecture-223292fcbc2d/)_

[**Flux : Tout ce que vous devez savoir**](https://medium.freecodecamp.com/node-js-streams-everything-you-need-to-know-c9141306be93)  
_[Les flux Node.js ont la réputation d'être difficiles à utiliser et encore plus difficiles à comprendre. Eh bien, j'ai de bonnes nouvelles...](https://www.freecodecamp.org/news/node-js-streams-everything-you-need-to-know-c9141306be93/)_

### Le module des processus enfants

Nous pouvons facilement lancer un processus enfant en utilisant le module `child_process` de Node et ces processus enfants peuvent facilement communiquer entre eux avec un système de messagerie.

Le module `child_process` nous permet d'accéder aux fonctionnalités du système d'exploitation en exécutant n'importe quelle commande système dans un processus enfant.

Nous pouvons contrôler le flux d'entrée de ce processus enfant et écouter son flux de sortie. Nous pouvons également contrôler les arguments à passer à la commande du système d'exploitation sous-jacente, et nous pouvons faire ce que nous voulons avec la sortie de cette commande. Nous pouvons, par exemple, rediriger la sortie d'une commande comme entrée d'une autre (comme nous le faisons sous Linux) car toutes les entrées et sorties de ces commandes peuvent nous être présentées en utilisant les [flux Node.js](https://medium.freecodecamp.com/node-js-streams-everything-you-need-to-know-c9141306be93).

_Notez que les exemples que j'utiliserai dans cet article sont tous basés sur Linux. Sous Windows, vous devez remplacer les commandes que j'utilise par leurs alternatives Windows._

Il existe quatre façons différentes de créer un processus enfant dans Node : `spawn()`, `fork()`, `exec()`, et `execFile()`.

Nous allons voir les différences entre ces quatre fonctions et quand utiliser chacune.

#### Processus enfants lancés

La fonction `spawn` lance une commande dans un nouveau processus et nous pouvons l'utiliser pour passer des arguments à cette commande. Par exemple, voici le code pour lancer un nouveau processus qui exécutera la commande `pwd`.

```
const { spawn } = require('child_process');

const child = spawn('pwd');
```

Nous déstructurons simplement la fonction `spawn` du module `child_process` et l'exécutons avec la commande du système d'exploitation comme premier argument.

Le résultat de l'exécution de la fonction `spawn` (l'objet `child` ci-dessus) est une instance de `ChildProcess`, qui implémente l'[API EventEmitter](https://medium.freecodecamp.com/understanding-node-js-event-driven-architecture-223292fcbc2d). Cela signifie que nous pouvons enregistrer des gestionnaires pour les événements sur cet objet enfant directement. Par exemple, nous pouvons faire quelque chose lorsque le processus enfant se termine en enregistrant un gestionnaire pour l'événement `exit` :

```js
child.on('exit', function (code, signal) {
  console.log('child process exited with ' +
              `code ${code} and signal ${signal}`);
});
```

Le gestionnaire ci-dessus nous donne le code de sortie du processus enfant et le `signal`, le cas échéant, qui a été utilisé pour terminer le processus enfant. Cette variable `signal` est nulle lorsque le processus enfant se termine normalement.

Les autres événements pour lesquels nous pouvons enregistrer des gestionnaires avec les instances `ChildProcess` sont `disconnect`, `error`, `close`, et `message`.

* L'événement `disconnect` est émis lorsque le processus parent appelle manuellement la fonction `child.disconnect`.
* L'événement `error` est émis si le processus n'a pas pu être lancé ou tué.
* L'événement `close` est émis lorsque les flux `stdio` d'un processus enfant sont fermés.
* L'événement `message` est le plus important. Il est émis lorsque le processus enfant utilise la fonction `process.send()` pour envoyer des messages. C'est ainsi que les processus parent/enfant peuvent communiquer entre eux. Nous verrons un exemple de cela ci-dessous.

Chaque processus enfant obtient également les trois flux `stdio` standard, auxquels nous pouvons accéder en utilisant `child.stdin`, `child.stdout`, et `child.stderr`.

Lorsque ces flux sont fermés, le processus enfant qui les utilisait émettra l'événement `close`. Cet événement `close` est différent de l'événement `exit` car plusieurs processus enfants peuvent partager les mêmes flux `stdio` et donc un processus enfant qui se termine ne signifie pas que les flux ont été fermés.

Puisque tous les flux sont des émetteurs d'événements, nous pouvons écouter différents événements sur ces flux `stdio` qui sont attachés à chaque processus enfant. Contrairement à un processus normal, dans un processus enfant, les flux `stdout`/`stderr` sont des flux lisibles tandis que le flux `stdin` est un flux inscriptible. Cela est essentiellement l'inverse de ces types tels que trouvés dans un processus principal. Les événements que nous pouvons utiliser pour ces flux sont les standards. Plus important encore, sur les flux lisibles, nous pouvons écouter l'événement `data`, qui contiendra la sortie de la commande ou toute erreur rencontrée lors de l'exécution de la commande :

```js
child.stdout.on('data', (data) => {
  console.log(`child stdout:\n${data}`);
});

child.stderr.on('data', (data) => {
  console.error(`child stderr:\n${data}`);
});
```

Les deux gestionnaires ci-dessus journaliseront les deux cas vers les flux `stdout` et `stderr` du processus principal. Lorsque nous exécutons la fonction `spawn` ci-dessus, la sortie de la commande `pwd` est imprimée et le processus enfant se termine avec le code `0`, ce qui signifie qu'aucune erreur ne s'est produite.

Nous pouvons passer des arguments à la commande exécutée par la fonction `spawn` en utilisant le deuxième argument de la fonction `spawn`, qui est un tableau de tous les arguments à passer à la commande. Par exemple, pour exécuter la commande `find` sur le répertoire courant avec un argument `-type f` (pour lister uniquement les fichiers), nous pouvons faire :

```js
const child = spawn('find', ['.', '-type', 'f']);
```

Si une erreur se produit lors de l'exécution de la commande, par exemple, si nous donnons à find une destination invalide ci-dessus, le gestionnaire d'événements `data` de `child.stderr` sera déclenché et le gestionnaire d'événements `exit` signalera un code de sortie de `1`, ce qui signifie qu'une erreur s'est produite. Les valeurs d'erreur dépendent en réalité du système d'exploitation hôte et du type d'erreur.

Un `stdin` de processus enfant est un flux inscriptible. Nous pouvons l'utiliser pour envoyer une commande. Tout comme n'importe quel flux inscriptible, le moyen le plus simple de le consommer est d'utiliser la fonction `pipe`. Nous redirigeons simplement un flux lisible vers un flux inscriptible. Puisque le `stdin` du processus principal est un flux lisible, nous pouvons le rediriger vers un flux `stdin` de processus enfant. Par exemple :

```js
const { spawn } = require('child_process');

const child = spawn('wc');

process.stdin.pipe(child.stdin)

child.stdout.on('data', (data) => {
  console.log(`child stdout:\n${data}`);
});
```

Dans l'exemple ci-dessus, le processus enfant invoque la commande `wc`, qui compte les lignes, les mots et les caractères sous Linux. Nous redirigeons ensuite le `stdin` du processus principal (qui est un flux lisible) vers le `stdin` du processus enfant (qui est un flux inscriptible). Le résultat de cette combinaison est que nous obtenons un mode d'entrée standard où nous pouvons taper quelque chose et lorsque nous appuyons sur `Ctrl+D`, ce que nous avons tapé sera utilisé comme entrée de la commande `wc`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s9dQY9GdgkkIf9zC1BL6Bg.gif)
_Gif capturé de mon cours Pluralsight — Advanced Node.js_

Nous pouvons également rediriger l'entrée/sortie standard de plusieurs processus les uns vers les autres, tout comme nous pouvons le faire avec les commandes Linux. Par exemple, nous pouvons rediriger le `stdout` de la commande `find` vers le `stdin` de la commande `wc` pour compter tous les fichiers dans le répertoire courant :

```js
const { spawn } = require('child_process');

const find = spawn('find', ['.', '-type', 'f']);
const wc = spawn('wc', ['-l']);

find.stdout.pipe(wc.stdin);

wc.stdout.on('data', (data) => {
  console.log(`Number of files ${data}`);
});
```

J'ai ajouté l'argument `-l` à la commande `wc` pour qu'elle ne compte que les lignes. Lorsque le code ci-dessus est exécuté, il sortira un compte de tous les fichiers dans tous les répertoires sous le répertoire courant.

#### Syntaxe Shell et la fonction exec

Par défaut, la fonction `spawn` ne crée pas de _shell_ pour exécuter la commande que nous lui passons. Cela la rend légèrement plus efficace que la fonction `exec`, qui crée un shell. La fonction `exec` a une autre différence majeure. Elle _met en mémoire tampon_ la sortie générée par la commande et passe la valeur de sortie entière à une fonction de rappel (au lieu d'utiliser des flux, ce que fait `spawn`).

Voici l'exemple précédent `find | wc` implémenté avec une fonction `exec`.

```js
const { exec } = require('child_process');

exec('find . -type f | wc -l', (err, stdout, stderr) => {
  if (err) {
    console.error(`exec error: ${err}`);
    return;
  }

  console.log(`Number of files ${stdout}`);
});
```

Puisque la fonction `exec` utilise un shell pour exécuter la commande, nous pouvons utiliser la _syntaxe shell_ directement ici en utilisant la fonctionnalité de _pipe_ du shell.

Notez que l'utilisation de la syntaxe shell comporte un [risque de sécurité](https://blog.liftsecurity.io/2014/08/19/Avoid-Command-Injection-Node.js/) si vous exécutez une sorte d'entrée dynamique fournie externement. Un utilisateur peut simplement effectuer une attaque par injection de commande en utilisant des caractères de syntaxe shell comme ; et $ (par exemple, `command + '; rm -rf ~'`)

La fonction `exec` met en mémoire tampon la sortie et la passe à la fonction de rappel (le deuxième argument de `exec`) en tant qu'argument `stdout`. Cet argument `stdout` est la sortie de la commande que nous voulons imprimer.

La fonction `exec` est un bon choix si vous devez utiliser la syntaxe shell et si la taille des données attendues de la commande est petite. (Rappelez-vous, `exec` mettra en mémoire tampon toutes les données en mémoire avant de les retourner.)

La fonction `spawn` est un bien meilleur choix lorsque la taille des données attendues de la commande est grande, car ces données seront diffusées avec les objets IO standard.

Nous pouvons faire en sorte que le processus enfant lancé hérite des objets IO standard de ses parents si nous le souhaitons, mais aussi, plus important encore, nous pouvons faire en sorte que la fonction `spawn` utilise également la syntaxe shell. Voici la même commande `find | wc` implémentée avec la fonction `spawn` :

```js
const child = spawn('find . -type f | wc -l', {
  stdio: 'inherit',
  shell: true
});
```

En raison de l'option `stdio: 'inherit'` ci-dessus, lorsque nous exécutons le code, le processus enfant hérite du `stdin`, `stdout` et `stderr` du processus principal. Cela fait en sorte que les gestionnaires d'événements de données du processus enfant soient déclenchés sur le flux `process.stdout` principal, ce qui fait que le script sort le résultat immédiatement.

En raison de l'option `shell: true` ci-dessus, nous avons pu utiliser la syntaxe shell dans la commande passée, tout comme nous l'avons fait avec `exec`. Mais avec ce code, nous obtenons toujours l'avantage de la diffusion des données que la fonction `spawn` nous offre. _C'est vraiment le meilleur des deux mondes._

Il y a quelques autres bonnes options que nous pouvons utiliser dans le dernier argument des fonctions `child_process` en plus de `shell` et `stdio`. Nous pouvons, par exemple, utiliser l'option `cwd` pour changer le répertoire de travail du script. Par exemple, voici le même exemple de comptage de tous les fichiers fait avec une fonction `spawn` utilisant un shell et avec un répertoire de travail défini sur mon dossier Téléchargements. L'option `cwd` ici fera en sorte que le script compte tous les fichiers que j'ai dans `~/Downloads` :

```js
const child = spawn('find . -type f | wc -l', {
  stdio: 'inherit',
  shell: true,
  cwd: '/Users/samer/Downloads'
});
```

Une autre option que nous pouvons utiliser est l'option `env` pour spécifier les variables d'environnement qui seront visibles pour le nouveau processus enfant. La valeur par défaut de cette option est `process.env` qui donne à toute commande l'accès à l'environnement du processus actuel. Si nous voulons remplacer ce comportement, nous pouvons simplement passer un objet vide comme option `env` ou de nouvelles valeurs là pour être considérées comme les seules variables d'environnement :

```js
const child = spawn('echo $ANSWER', {
  stdio: 'inherit',
  shell: true,
  env: { ANSWER: 42 },
});
```

La commande echo ci-dessus n'a pas accès aux variables d'environnement du processus parent. Elle ne peut pas, par exemple, accéder à `$HOME`, mais elle peut accéder à `$ANSWER` car elle a été passée comme variable d'environnement personnalisée via l'option `env`.

Une dernière option importante de processus enfant à expliquer ici est l'option `detached`, qui fait que le processus enfant s'exécute indépendamment de son processus parent.

En supposant que nous avons un fichier `timer.js` qui maintient la boucle d'événements occupée :

```js
setTimeout(() => {  
  // keep the event loop busy
}, 20000);
```

Nous pouvons l'exécuter en arrière-plan en utilisant l'option `detached` :

```js
const { spawn } = require('child_process');

const child = spawn('node', ['timer.js'], {
  detached: true,
  stdio: 'ignore'
});

child.unref();
```

Le comportement exact des processus enfants détachés dépend du système d'exploitation. Sous Windows, le processus enfant détaché aura sa propre fenêtre de console tandis que sous Linux, le processus enfant détaché sera fait leader d'un nouveau groupe de processus et de session.

Si la fonction `unref` est appelée sur le processus détaché, le processus parent peut se terminer indépendamment de l'enfant. Cela peut être utile si l'enfant exécute un processus de longue durée, mais pour le maintenir en arrière-plan, les configurations `stdio` de l'enfant doivent également être indépendantes du parent.

L'exemple ci-dessus exécutera un script node (`timer.js`) en arrière-plan en le détachant et en ignorant également ses descripteurs de fichiers `stdio` parent afin que le parent puisse se terminer tandis que l'enfant continue de s'exécuter en arrière-plan.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WhvMs8zv-WS6v7nDXmDUzw.gif)
_Gif capturé de mon cours Pluralsight — Advanced Node.js_

#### La fonction execFile

Si vous devez exécuter un fichier sans utiliser de shell, la fonction `execFile` est ce dont vous avez besoin. Elle se comporte exactement comme la fonction `exec`, mais n'utilise pas de shell, ce qui la rend un peu plus efficace. Sur Windows, certains fichiers ne peuvent pas être exécutés seuls, comme les fichiers `.bat` ou `.cmd`. Ces fichiers ne peuvent pas être exécutés avec `execFile` et nécessitent soit `exec` soit `spawn` avec shell défini sur true pour être exécutés.

#### La fonction *Sync

Les fonctions `spawn`, `exec`, et `execFile` du module `child_process` ont également des versions synchrones bloquantes qui attendront jusqu'à ce que le processus enfant se termine.

```
const { 
  spawnSync, 
  execSync, 
  execFileSync,
} = require('child_process');
```

Ces versions synchrones sont potentiellement utiles lorsque vous essayez de simplifier les tâches de script ou toute tâche de traitement de démarrage, mais elles doivent être évitées sinon.

#### La fonction fork()

La fonction `fork` est une variation de la fonction `spawn` pour lancer des processus node. La plus grande différence entre `spawn` et `fork` est qu'un canal de communication est établi vers le processus enfant lors de l'utilisation de `fork`, donc nous pouvons utiliser la fonction `send` sur le processus forké ainsi que l'objet global `process` lui-même pour échanger des messages entre les processus parent et forkés. Nous faisons cela via l'interface du module `EventEmitter`. Voici un exemple :

Le fichier parent, `parent.js` :

```js
const { fork } = require('child_process');

const forked = fork('child.js');

forked.on('message', (msg) => {
  console.log('Message from child', msg);
});

forked.send({ hello: 'world' });
```

Le fichier enfant, `child.js` :

```js
process.on('message', (msg) => {
  console.log('Message from parent:', msg);
});

let counter = 0;

setInterval(() => {
  process.send({ counter: counter++ });
}, 1000);
```

Dans le fichier parent ci-dessus, nous forkons `child.js` (qui exécutera le fichier avec la commande `node`) puis nous écoutons l'événement `message`. L'événement `message` sera émis chaque fois que l'enfant utilise `process.send`, ce que nous faisons toutes les secondes.

Pour transmettre des messages du parent à l'enfant, nous pouvons exécuter la fonction `send` sur l'objet forké lui-même, puis, dans le script enfant, nous pouvons écouter l'événement `message` sur l'objet global `process`.

Lorsque nous exécutons le fichier `parent.js` ci-dessus, il enverra d'abord l'objet `{ hello: 'world' }` à imprimer par le processus enfant forké, puis le processus enfant forké enverra une valeur de compteur incrémentée toutes les secondes à imprimer par le processus parent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GOIOTAZTcn40qZ3JwgsrNA.gif)
_Capture d'écran de mon cours Pluralsight — Advanced Node.js_

Faisons un exemple plus pratique sur la fonction `fork`.

Supposons que nous avons un serveur http qui gère deux endpoints. L'un de ces endpoints (`/compute` ci-dessous) est coûteux en calcul et prendra quelques secondes à compléter. Nous pouvons utiliser une longue boucle for pour simuler cela :

```js
const http = require('http');

const longComputation = () => {
  let sum = 0;
  for (let i = 0; i < 1e9; i++) {
    sum += i;
  };
  return sum;
};

const server = http.createServer();

server.on('request', (req, res) => {
  if (req.url === '/compute') {
    const sum = longComputation();
    return res.end(`Sum is ${sum}`);
  } else {
    res.end('Ok')
  }
});

server.listen(3000);
```

Ce programme a un gros problème ; lorsque l'endpoint `/compute` est demandé, le serveur ne pourra pas gérer d'autres requêtes car la boucle d'événements est occupée par l'opération de la longue boucle for.

Il existe plusieurs façons de résoudre ce problème en fonction de la nature de l'opération longue, mais une solution qui fonctionne pour toutes les opérations est de simplement déplacer l'opération de calcul dans un autre processus en utilisant `fork`.

Nous déplaçons d'abord toute la fonction `longComputation` dans son propre fichier et la faisons invoquer cette fonction lorsqu'elle est instruite via un message du processus principal :

Dans un nouveau fichier `compute.js` :

```js
const longComputation = () => {
  let sum = 0;
  for (let i = 0; i < 1e9; i++) {
    sum += i;
  };
  return sum;
};

process.on('message', (msg) => {
  const sum = longComputation();
  process.send(sum);
});
```

Maintenant, au lieu de faire l'opération longue dans la boucle d'événements du processus principal, nous pouvons `fork` le fichier `compute.js` et utiliser l'interface de messages pour communiquer des messages entre le serveur et le processus forké.

```js
const http = require('http');
const { fork } = require('child_process');

const server = http.createServer();

server.on('request', (req, res) => {
  if (req.url === '/compute') {
    const compute = fork('compute.js');
    compute.send('start');
    compute.on('message', sum => {
      res.end(`Sum is ${sum}`);
    });
  } else {
    res.end('Ok')
  }
});

server.listen(3000);
```

Lorsque une requête à `/compute` se produit maintenant avec le code ci-dessus, nous envoyons simplement un message au processus forké pour commencer à exécuter l'opération longue. La boucle d'événements du processus principal ne sera pas bloquée.

Une fois que le processus forké a terminé cette opération longue, il peut renvoyer son résultat au processus parent en utilisant `process.send`.

Dans le processus parent, nous écoutons l'événement `message` sur le processus enfant forké lui-même. Lorsque nous recevons cet événement, nous aurons une valeur `sum` prête à être envoyée à l'utilisateur demandeur via http.

Le code ci-dessus est, bien sûr, limité par le nombre de processus que nous pouvons fork, mais lorsque nous l'exécutons et demandons l'endpoint de calcul longue durée via http, le serveur principal n'est pas du tout bloqué et peut prendre d'autres requêtes.

Le module `cluster` de Node, qui est le sujet de mon prochain article, est basé sur cette idée de fork de processus enfant et d'équilibrage de charge des requêtes parmi les nombreux forks que nous pouvons créer sur n'importe quel système.

C'est tout ce que j'ai pour ce sujet. Merci d'avoir lu ! À la prochaine !

Apprendre React ou Node ? Consultez mes livres :

* [Apprendre React.js en construisant des jeux](http://amzn.to/2peYJZj)
* [Node.js Au-delà des bases](http://amzn.to/2FYfYru)