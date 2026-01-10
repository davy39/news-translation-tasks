---
title: Mise à l'échelle des applications Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-14T01:32:54.000Z'
originalURL: https://freecodecamp.org/news/scaling-node-js-applications-8492bd8afadc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C7ICI8d7aAna_zTZvZ64MA.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: scaling
  slug: scaling
seo_title: Mise à l'échelle des applications Node.js
seo_desc: 'By Samer Buna

  Everything you need to know about Node.js built-in tools for scalability


  Update: This article is now part of my book “Node.js Beyond The Basics”.

  Read the updated version of this content and more about Node at jscomplete.com/node-beyon...'
---

Par Samer Buna

#### Tout ce que vous devez savoir sur les outils intégrés de Node.js pour la scalabilité  


> **Mise à jour :** Cet article fait désormais partie de mon livre « Node.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur Node à [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/g/scaling-node).

La scalabilité dans Node.js n'est pas une réflexion après coup. C'est quelque chose qui est intégré au cœur du runtime. Node est nommé Node pour souligner l'idée qu'une application Node devrait comprendre plusieurs petits nœuds distribués qui communiquent entre eux.

Exécutez-vous plusieurs nœuds pour vos applications Node ? Exécutez-vous un processus Node sur chaque cœur CPU de vos machines de production et équilibrez-vous la charge de toutes les requêtes parmi eux ? Saviez-vous que Node dispose d'un module intégré pour vous aider avec cela ?

Le module _cluster_ de Node non seulement fournit une solution prête à l'emploi pour utiliser la pleine puissance CPU d'une machine, mais il aide également à augmenter la disponibilité de vos processus Node et offre une option pour redémarrer toute l'application avec un temps d'arrêt zéro. Cet article couvre toute cette richesse et plus encore.

> Cet article est une rédaction d'une partie de [mon cours Pluralsight sur Node.js](https://www.pluralsight.com/courses/nodejs-advanced). Je couvre un contenu similaire en format vidéo là-bas.

### Stratégies de scalabilité

La charge de travail est la raison la plus populaire pour laquelle nous mettons à l'échelle nos applications, mais ce n'est pas la seule raison. Nous mettons également à l'échelle nos applications pour augmenter leur disponibilité et leur tolérance aux pannes.

Il y a principalement trois choses différentes que nous pouvons faire pour mettre à l'échelle une application :

#### 1 — Clonage

La chose la plus facile à faire pour mettre à l'échelle une grande application est de la cloner plusieurs fois et de faire en sorte que chaque instance clonée gère une partie de la charge de travail (avec un équilibreur de charge, par exemple). Cela ne coûte pas beaucoup en termes de temps de développement et c'est très efficace. Cette stratégie est le minimum que vous devriez faire et Node.js dispose du module intégré, `cluster`, pour vous faciliter la mise en œuvre de la stratégie de clonage sur un seul serveur.

#### 2 — Décomposition

Nous pouvons également mettre à l'échelle une application en la [décomposant](https://builttoadapt.io/whats-your-decomposition-strategy-e19b8e72ac8f) en fonction des fonctionnalités et des services. Cela signifie avoir plusieurs applications différentes avec des bases de code différentes et parfois avec leurs propres bases de données et interfaces utilisateur dédiées.

Cette stratégie est couramment associée au terme _Microservice_, où micro indique que ces services doivent être aussi petits que possible, mais en réalité, la taille du service n'est pas ce qui est important, mais plutôt l'application de couplage lâche et de haute cohésion entre les services. La mise en œuvre de cette stratégie n'est souvent pas facile et pourrait entraîner des problèmes inattendus à long terme, mais lorsque cela est fait correctement, les avantages sont grands.

#### 3 — Partitionnement

Nous pouvons également diviser l'application en plusieurs instances où chaque instance est responsable d'une partie seulement des données de l'application. Cette stratégie est souvent appelée _partitionnement horizontal_, ou _sharding_, dans les bases de données. Le partitionnement des données nécessite une étape de recherche avant chaque opération pour déterminer quelle instance de l'application utiliser. Par exemple, peut-être voulons-nous partitionner nos utilisateurs en fonction de leur pays ou de leur langue. Nous devons d'abord faire une recherche de ces informations.

La mise à l'échelle réussie d'une grande application devrait finalement implémenter les trois stratégies. Node.js facilite cela, mais je vais me concentrer sur la stratégie de clonage dans cet article et explorer les outils intégrés disponibles dans Node.js pour la mettre en œuvre.

Veuillez noter que vous avez besoin d'une bonne compréhension des processus enfants de Node.js avant de lire cet article. Si vous ne l'avez pas encore fait, je vous recommande de lire cet autre article d'abord :

[**Processus enfants Node.js : Tout ce que vous devez savoir**](https://medium.freecodecamp.org/node-js-child-processes-everything-you-need-to-know-e69498fe970a)  
[_Comment utiliser spawn(), exec(), execFile(), et fork()_medium.freecodecamp.org](https://medium.freecodecamp.org/node-js-child-processes-everything-you-need-to-know-e69498fe970a)

### Le module Cluster

Le module cluster peut être utilisé pour activer l'équilibrage de charge sur les multiples cœurs CPU d'un environnement. Il est basé sur la méthode `fork` du module de processus enfant et permet essentiellement de forker le processus principal de l'application autant de fois que nous avons de cœurs CPU. Il prendra ensuite le relais et équilibrera la charge de toutes les requêtes vers le processus principal sur tous les processus forkés.

Le module cluster est l'assistant de Node pour mettre en œuvre la stratégie de scalabilité par clonage, mais uniquement sur une machine. Lorsque vous avez une grande machine avec beaucoup de ressources ou lorsqu'il est plus facile et moins cher d'ajouter plus de ressources à une machine plutôt que d'ajouter de nouvelles machines, le module cluster est une excellente option pour une implémentation vraiment rapide de la stratégie de clonage.

Même les petites machines ont généralement plusieurs cœurs et même si vous ne vous inquiétez pas de la charge sur votre serveur Node, vous devriez activer le module cluster de toute façon pour augmenter la disponibilité et la tolérance aux pannes de votre serveur. C'est une étape simple et lorsque vous utilisez un gestionnaire de processus comme PM2, par exemple, cela devient aussi simple que de fournir un argument à la commande de lancement !

Mais laissez-moi vous expliquer comment utiliser le module cluster de manière native et expliquer comment il fonctionne.

La structure de ce que fait le module cluster est simple. Nous créons un processus _maître_ et ce processus maître fork un certain nombre de processus _travailleurs_ et les gère. Chaque processus travailleur représente une instance de l'application que nous voulons mettre à l'échelle. Toutes les requêtes entrantes sont gérées par le processus maître, qui est celui qui décide quel processus travailleur doit gérer une requête entrante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7ICI8d7aAna_zTZvZ64MA.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Le travail du processus maître est facile car il utilise en réalité un algorithme _round-robin_ pour choisir un processus travailleur. Cela est activé par défaut sur toutes les plateformes sauf Windows et peut être modifié globalement pour laisser l'équilibrage de charge être géré par le système d'exploitation lui-même.

L'algorithme round-robin distribue la charge uniformément sur tous les processus disponibles sur une base rotationnelle. La première requête est transmise au premier processus travailleur, la deuxième au processus travailleur suivant dans la liste, et ainsi de suite. Lorsque la fin de la liste est atteinte, l'algorithme recommence depuis le début.

C'est l'un des algorithmes d'équilibrage de charge les plus simples et les plus utilisés. Mais ce n'est pas le seul. Des algorithmes plus avancés permettent d'assigner des priorités et de sélectionner le serveur le moins chargé ou celui avec le temps de réponse le plus rapide.

#### Équilibrage de charge d'un serveur HTTP

Clonons et équilibrons la charge d'un serveur HTTP simple en utilisant le module cluster. Voici le simple exemple de serveur hello-world de Node légèrement modifié pour simuler un travail CPU avant de répondre :

```
// server.js
const http = require('http');
const pid = process.pid;

http.createServer((req, res) => {
  for (let i=0; i<1e7; i++); // simuler le travail CPU
  res.end(`Géré par le processus ${pid}`);
}).listen(8080, () => {
  console.log(`Processus démarré ${pid}`);
});
```

Pour vérifier que l'équilibreur que nous allons créer va fonctionner, j'ai inclus le `pid` du processus dans la réponse HTTP pour identifier quelle instance de l'application gère réellement une requête.

Avant de créer un cluster pour cloner ce serveur en plusieurs travailleurs, faisons un simple benchmark du nombre de requêtes que ce serveur peut gérer par seconde. Nous pouvons utiliser l'[outil de benchmarking Apache](https://httpd.apache.org/docs/2.4/programs/ab.html) pour cela. Après avoir exécuté le simple code `server.js` ci-dessus, exécutez cette commande `ab` :

```
ab -c200 -t10 http://localhost:8080/
```

Cette commande testera la charge du serveur avec 200 connexions simultanées pendant 10 secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w8VmzV81atlTzHn7pDXu1g.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Sur ma machine, le serveur à nœud unique a pu gérer environ 51 requêtes par seconde. Bien sûr, les résultats ici seront différents sur différentes plateformes et ce test de performance est très simplifié et n'est pas précis à 100 %, mais il montrera clairement la différence qu'un cluster ferait dans un environnement multi-cœurs.

Maintenant que nous avons un benchmark de référence, nous pouvons mettre à l'échelle l'application avec la stratégie de clonage en utilisant le module cluster.

Au même niveau que le fichier `server.js` ci-dessus, nous pouvons créer un nouveau fichier (`cluster.js`) pour le processus maître avec ce contenu (l'explication suit) :

```js
// cluster.js
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  const cpus = os.cpus().length;

  console.log(`Forking pour ${cpus} CPUs`);
  for (let i = 0; i<cpus; i++) {
    cluster.fork();
  }
} else {
  require('./server');
}
```

Dans `cluster.js`, nous avons d'abord requis les modules `cluster` et `os`. Nous utilisons le module `os` pour lire le nombre de cœurs CPU avec lesquels nous pouvons travailler en utilisant `os.cpus()`.

Le module `cluster` nous donne le drapeau booléen pratique `isMaster` pour déterminer si ce fichier `cluster.js` est chargé en tant que processus maître ou non. La première fois que nous exécutons ce fichier, nous exécuterons le processus maître et ce drapeau `isMaster` sera défini sur vrai. Dans ce cas, nous pouvons instruire le processus maître de forker notre serveur autant de fois que nous avons de cœurs CPU.

Maintenant, nous lisons simplement le nombre de CPU que nous avons en utilisant le module `os`, puis avec une boucle for sur ce nombre, nous appelons la méthode `cluster.fork`. La boucle for créera simplement autant de travailleurs que le nombre de CPU dans le système pour tirer parti de toute la puissance de traitement disponible.

Lorsque la ligne `cluster.fork` est exécutée à partir du processus maître, le fichier actuel, `cluster.js`, est exécuté à nouveau, mais cette fois en _mode travailleur_ avec le drapeau `isMaster` défini sur faux. _Il y a en fait un autre drapeau défini sur vrai dans ce cas si vous devez l'utiliser, qui est le drapeau `isWorker`._

Lorsque l'application s'exécute en tant que travailleur, elle peut commencer à faire le travail réel. C'est là que nous devons définir notre logique de serveur, ce que, pour cet exemple, nous pouvons faire en requérant le fichier `server.js` que nous avons déjà.

C'est essentiellement tout. C'est à quel point il est facile de tirer parti de toute la puissance de traitement d'une machine. Pour tester le cluster, exécutez le fichier `cluster.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*c0S-W4GYgCGB_maJ94ZLPw.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

J'ai 8 cœurs sur ma machine, donc il a démarré 8 processus. Il est important de comprendre que ce sont des processus Node.js complètement différents. Chaque processus travailleur ici aura sa propre boucle d'événements et son espace mémoire.

Lorsque nous sollicitons maintenant le serveur web plusieurs fois, les requêtes commenceront à être gérées par différents processus travailleurs avec différents identifiants de processus. Les travailleurs ne seront pas exactement tournés en séquence car le module cluster effectue certaines optimisations lors du choix du prochain travailleur, mais la charge sera d'une manière ou d'une autre distribuée parmi les différents processus travailleurs.

Nous pouvons utiliser la même commande `ab` ci-dessus pour tester la charge de ce cluster de processus :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5_EogHG-Egf2uAMOj9PmCA.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Le cluster que j'ai créé sur ma machine a pu gérer 181 requêtes par seconde contre les 51 requêtes par seconde que nous avons obtenues en utilisant un seul processus Node. La performance de cette simple application a triplé avec seulement quelques lignes de code.

#### Diffusion de messages à tous les travailleurs

La communication entre le processus maître et les travailleurs est simple car sous le capot, le module cluster utilise simplement l'API `child_process.fork`, ce qui signifie que nous avons également des canaux de communication disponibles entre le processus maître et chaque travailleur.

Sur la base de l'exemple `server.js`/`cluster.js` ci-dessus, nous pouvons accéder à la liste des objets travailleurs en utilisant `cluster.workers`, qui est un objet qui contient une référence à tous les travailleurs et peut être utilisé pour lire des informations sur ces travailleurs. Puisque nous avons des canaux de communication entre le processus maître et tous les travailleurs, pour diffuser un message à tous, nous avons simplement besoin d'une simple boucle sur tous les travailleurs. Par exemple :

```js
Object.values(cluster.workers).forEach(worker => {
  worker.send(`Bonjour Travailleur ${worker.id}`);
});
```

Nous avons simplement utilisé `Object.values` pour obtenir un tableau de tous les travailleurs à partir de l'objet `cluster.workers`. Ensuite, pour chaque travailleur, nous pouvons utiliser la fonction `send` pour envoyer toute valeur que nous voulons.

Dans un fichier travailleur, `server.js` dans notre exemple, pour lire un message reçu de ce processus maître, nous pouvons enregistrer un gestionnaire pour l'événement `message` sur l'objet global `process`. Par exemple :

```js
process.on('message', msg => {
  console.log(`Message du maître : ${msg}`);
});
```

Voici ce que je vois lorsque je teste ces deux ajouts à l'exemple cluster/serveur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6XfoWiNKTCiDjqar7L5_xw.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Chaque travailleur a reçu un message du processus maître. _Remarquez comment les travailleurs n'ont pas démarré dans l'ordre._

Rendons cet exemple de communication un peu plus pratique. Supposons que nous voulons que notre serveur réponde avec le nombre d'utilisateurs que nous avons créés dans notre base de données. Nous allons créer une fonction fictive qui retourne le nombre d'utilisateurs que nous avons dans la base de données et la faire simplement élever sa valeur au carré chaque fois qu'elle est appelée (croissance idéale) :

```js
// **** Appel fictif à la base de données
const numberOfUsersInDB = function() {
  this.count = this.count || 5;
  this.count = this.count * this.count;
  return this.count;
}
// ****
```

Chaque fois que `numberOfUsersInDB` est appelé, nous supposerons qu'une connexion à la base de données a été établie. Ce que nous voulons faire ici — pour éviter plusieurs requêtes à la base de données — est de mettre en cache cet appel pendant une certaine période, par exemple 10 secondes. Cependant, nous ne voulons toujours pas que les 8 travailleurs forkés effectuent leurs propres requêtes à la base de données et finissent par avoir 8 requêtes à la base de données toutes les 10 secondes. Nous pouvons faire en sorte que le processus maître effectue une seule requête et informe tous les 8 travailleurs de la nouvelle valeur du compteur d'utilisateurs en utilisant l'interface de communication.

En mode processus maître, nous pouvons, par exemple, utiliser la même boucle pour diffuser la valeur du compteur d'utilisateurs à tous les travailleurs :

```js
// Juste après la boucle de fork dans le bloc isMaster=true
const updateWorkers = () => {
  const usersCount = numberOfUsersInDB();
  Object.values(cluster.workers).forEach(worker => {
    worker.send({ usersCount });
  });
};

updateWorkers();
setInterval(updateWorkers, 10000);
```

Ici, nous invoquons `updateWorkers` pour la première fois, puis nous l'invoquons toutes les 10 secondes en utilisant un `setInterval`. De cette façon, toutes les 10 secondes, tous les travailleurs recevront la nouvelle valeur du compteur d'utilisateurs via le canal de communication du processus et une seule connexion à la base de données sera établie.

Dans le code du serveur, nous pouvons utiliser la valeur `usersCount` en utilisant le même gestionnaire d'événements `message`. Nous pouvons simplement mettre en cache cette valeur avec une variable globale de module et l'utiliser où nous voulons.

Par exemple :

```js
const http = require('http');
const pid = process.pid;

let usersCount;

http.createServer((req, res) => {
  for (let i=0; i<1e7; i++); // simuler le travail CPU
  res.write(`Géré par le processus ${pid}\n`);
  res.end(`Utilisateurs : ${usersCount}`);
}).listen(8080, () => {
  console.log(`Processus démarré ${pid}`);
});

process.on('message', msg => {
  usersCount = msg.usersCount;
});
```

Le code ci-dessus fait en sorte que le serveur web travailleur réponde avec la valeur `usersCount` mise en cache. Si vous testez le code du cluster maintenant, pendant les 10 premières secondes, vous obtiendrez « 25 » comme nombre d'utilisateurs de la part de tous les travailleurs (et une seule requête à la base de données serait effectuée). Ensuite, après 10 autres secondes, tous les travailleurs commenceront à signaler le nouveau nombre d'utilisateurs, 625 (et une seule autre requête à la base de données serait effectuée).

Tout cela est possible grâce aux canaux de communication entre le processus maître et tous les travailleurs.

#### Augmentation de la disponibilité du serveur

L'un des problèmes de l'exécution d'une seule instance d'une application Node est que lorsque cette instance plante, elle doit être redémarrée. Cela signifie un certain temps d'arrêt entre ces deux actions, même si le processus était automatisé comme il se doit.

Cela s'applique également au cas où le serveur doit être redémarré pour déployer un nouveau code. Avec une seule instance, il y aura un temps d'arrêt qui affecte la disponibilité du système.

Lorsque nous avons plusieurs instances, la disponibilité du système peut être facilement augmentée avec seulement quelques lignes de code supplémentaires.

Pour simuler un plantage aléatoire dans le processus serveur, nous pouvons simplement faire un appel à `process.exit` à l'intérieur d'un minuteur qui se déclenche après un temps aléatoire :

```js
// Dans server.js
setTimeout(() => {
  process.exit(1) // mort par timeout aléatoire
}, Math.random() * 10000);
```

Lorsque qu'un processus travailleur se termine ainsi, le processus maître sera notifié en utilisant l'événement `exit` sur l'objet modèle `cluster`. Nous pouvons enregistrer un gestionnaire pour cet événement et simplement forker un nouveau processus travailleur lorsqu'un processus travailleur se termine.

Par exemple :

```js
// Juste après la boucle de fork dans le bloc isMaster=true
cluster.on('exit', (worker, code, signal) => {
  if (code !== 0 && !worker.exitedAfterDisconnect) {
    console.log(`Le travailleur ${worker.id} a planté. ` +
                'Démarrage d'un nouveau travailleur...');
    cluster.fork();
  }
});
```

Il est bon d'ajouter la condition if ci-dessus pour s'assurer que le processus travailleur a réellement planté et n'a pas été déconnecté manuellement ou tué par le processus maître lui-même. Par exemple, le processus maître pourrait décider que nous utilisons trop de ressources en fonction des schémas de charge qu'il voit et il devra tuer quelques travailleurs dans ce cas. Pour ce faire, nous pouvons utiliser les méthodes `disconnect` sur n'importe quel travailleur et, dans ce cas, le drapeau `exitedAfterDisconnect` sera défini sur vrai. L'instruction if ci-dessus empêchera de forker un nouveau travailleur pour ce cas.

Si nous exécutons le cluster avec le gestionnaire ci-dessus (et le plantage aléatoire dans `server.js`), après un nombre aléatoire de secondes, les travailleurs commenceront à planter et le processus maître forkera immédiatement de nouveaux travailleurs pour augmenter la disponibilité du système. Vous pouvez en fait mesurer la disponibilité en utilisant la même commande `ab` et voir combien de requêtes le serveur ne pourra pas gérer globalement (parce que certaines des requêtes malchanceuses devront faire face au cas de plantage et c'est difficile à éviter.)

Lorsque j'ai testé le code, seulement 17 requêtes ont échoué sur plus de 1800 dans l'intervalle de test de 10 secondes avec 200 requêtes simultanées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B72o6QhsyiNnEQU5Wx20RQ.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

C'est plus de 99 % de disponibilité. En ajoutant simplement quelques lignes de code, nous n'avons plus à nous soucier des plantages de processus. Le gardien maître surveillera ces processus pour nous.

#### Redémarrages sans temps d'arrêt

Et si nous voulons redémarrer tous les processus travailleurs lorsque, par exemple, nous devons déployer un nouveau code ?

Nous avons plusieurs instances en cours d'exécution, donc au lieu de les redémarrer ensemble, nous pouvons simplement les redémarrer une à la fois pour permettre aux autres travailleurs de continuer à servir les requêtes pendant qu'un travailleur est redémarré.

La mise en œuvre de cela avec le module cluster est facile. Puisque nous ne voulons pas redémarrer le processus maître une fois qu'il est en cours d'exécution, nous avons besoin d'un moyen d'envoyer à ce processus maître une commande pour lui indiquer de commencer à redémarrer ses travailleurs. Cela est facile sur les systèmes Linux car nous pouvons simplement écouter un signal de processus comme `SIGUSR2`, que nous pouvons déclencher en utilisant la commande `kill` sur l'identifiant du processus et en passant ce signal :

```js
// Dans Node
process.on('SIGUSR2', () => { ... });
// Pour déclencher cela
$ kill -SIGUSR2 PID
```

De cette façon, le processus maître ne sera pas tué et nous avons un moyen de lui indiquer de commencer à faire quelque chose. `SIGUSR2` est un signal approprié à utiliser ici car ce sera une commande utilisateur. Si vous vous demandez pourquoi pas `SIGUSR1`, c'est parce que Node l'utilise pour son débogueur et vous voulez éviter tout conflit.

Malheureusement, sur Windows, ces signaux de processus ne sont pas pris en charge et nous devrions trouver un autre moyen de commander le processus maître pour faire quelque chose. Il existe quelques alternatives. Nous pouvons, par exemple, utiliser l'entrée standard ou l'entrée socket. Ou nous pouvons surveiller l'existence d'un fichier `process.pid` et surveiller cet événement de suppression. Mais pour garder cet exemple simple, nous supposerons simplement que ce serveur s'exécute sur une plateforme Linux.

Node fonctionne très bien sur Windows, mais je pense que c'est une option beaucoup plus sûre d'héberger des applications Node de production sur une plateforme Linux. Ce n'est pas seulement à cause de Node lui-même, mais aussi de nombreux autres outils de production qui sont beaucoup plus stables sur Linux. C'est mon opinion personnelle et vous êtes libre de l'ignorer complètement.

_En passant, sur les versions récentes de Windows, vous pouvez en fait utiliser un sous-système Linux et cela fonctionne très bien. Je l'ai testé moi-même et ce n'était rien de moins qu'impressionnant. Si vous développez une application Node sur Windows, consultez [Bash sur Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) et essayez-le._

Dans notre exemple, lorsque le processus maître reçoit le signal `SIGUSR2`, cela signifie qu'il est temps pour lui de redémarrer ses travailleurs, mais nous voulons le faire un travailleur à la fois. Cela signifie simplement que le processus maître ne doit redémarrer le travailleur suivant que lorsqu'il a terminé de redémarrer le travailleur actuel.

Pour commencer cette tâche, nous devons obtenir une référence à tous les travailleurs actuels en utilisant l'objet `cluster.workers` et nous pouvons simplement stocker les travailleurs dans un tableau :

```
const workers = Object.values(cluster.workers);
```

Ensuite, nous pouvons créer une fonction `restartWorker` qui reçoit l'index du travailleur à redémarrer. De cette façon, nous pouvons effectuer le redémarrage en séquence en faisant en sorte que la fonction s'appelle elle-même lorsqu'elle est prête pour le travailleur suivant. Voici un exemple de fonction `restartWorker` que nous pouvons utiliser (l'explication suit) :

```js
const restartWorker = (workerIndex) => {
  const worker = workers[workerIndex];
  if (!worker) return;

  worker.on('exit', () => {
    if (!worker.exitedAfterDisconnect) return;
    console.log(`Processus terminé ${worker.process.pid}`);
    
    cluster.fork().on('listening', () => {
      restartWorker(workerIndex + 1);
    });
  });

  worker.disconnect();
};

restartWorker(0);
```

À l'intérieur de la fonction `restartWorker`, nous avons obtenu une référence au travailleur à redémarrer et puisque nous allons appeler cette fonction de manière récursive pour former une séquence, nous avons besoin d'une condition d'arrêt. Lorsque nous n'avons plus de travailleur à redémarrer, nous pouvons simplement retourner. Nous voulons ensuite déconnecter ce travailleur (en utilisant `worker.disconnect`), mais avant de redémarrer le travailleur suivant, nous devons forker un nouveau travailleur pour remplacer celui que nous déconnectons.

Nous pouvons utiliser l'événement `exit` sur le travailleur lui-même pour forker un nouveau travailleur lorsque le travailleur actuel existe, mais nous devons nous assurer que l'action de sortie a été déclenchée après un appel de déconnexion normal. Nous pouvons utiliser le drapeau `exitedAfetrDisconnect`. Si ce drapeau n'est pas vrai, la sortie a été causée par autre chose que notre appel de déconnexion et dans ce cas, nous devons simplement retourner et ne rien faire. Mais si le drapeau est défini sur vrai, nous pouvons continuer et forker un nouveau travailleur pour remplacer celui que nous déconnectons.

Lorsque ce nouveau travailleur forké est prêt, nous pouvons redémarrer le suivant. Cependant, rappelez-vous que le processus de fork n'est pas synchrone, donc nous ne pouvons pas simplement redémarrer le travailleur suivant après l'appel de fork. Au lieu de cela, nous pouvons surveiller l'événement `listening` sur le nouveau travailleur forké, qui nous indique que ce travailleur est connecté et prêt. Lorsque nous recevons cet événement, nous pouvons redémarrer en toute sécurité le travailleur suivant dans la séquence.

C'est tout ce dont nous avons besoin pour un redémarrage sans temps d'arrêt. Pour le tester, vous devrez lire l'identifiant du processus maître à envoyer au signal `SIGUSR2` :

```
console.log(`Master PID: ${process.pid}`);
```

Démarrez le cluster, copiez l'identifiant du processus maître, puis redémarrez le cluster en utilisant la commande `kill -SIGUSR2 PID`. Vous pouvez également exécuter la même commande `ab` tout en redémarrant le cluster pour voir l'effet que ce processus de redémarrage aura sur la disponibilité. Spoiler alert, vous devriez obtenir ZÉRO requête échouée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NjG0e2ARIDQiYSHWNvdNPQ.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Les moniteurs de processus comme PM2, que j'utilise personnellement en production, rendent toutes les tâches que nous avons parcourues jusqu'à présent extrêmement faciles et offrent beaucoup plus de fonctionnalités pour surveiller la santé d'une application Node.js. Par exemple, avec PM2, pour lancer un cluster pour n'importe quelle application, tout ce que vous avez à faire est d'utiliser l'argument `-i` :

```
pm2 start server.js -i max
```

Et pour faire un redémarrage sans temps d'arrêt, vous émettez simplement cette commande magique :

```
pm2 reload all
```

Cependant, je trouve utile de comprendre d'abord ce qui se passera réellement sous le capot lorsque vous utiliserez ces commandes.

#### État partagé et équilibrage de charge collant

Les bonnes choses ont toujours un coût. Lorsque nous équilibrons la charge d'une application Node, nous perdons certaines fonctionnalités qui ne sont adaptées qu'à un seul processus. Ce problème est quelque peu similaire à ce qui est connu dans d'autres langues comme la sécurité des threads, qui concerne le partage de données entre les threads. Dans notre cas, il s'agit de partager des données entre les processus travailleurs.

Par exemple, avec une configuration de cluster, nous ne pouvons plus mettre en cache les choses en mémoire car chaque processus travailleur aura son propre espace mémoire. Si nous mettons en cache quelque chose dans la mémoire d'un travailleur, les autres travailleurs n'auront pas accès à celui-ci.

Si nous devons mettre en cache des choses avec une configuration de cluster, nous devons utiliser une entité séparée et lire/écrire dans l'API de cette entité à partir de tous les travailleurs. Cette entité peut être un serveur de base de données ou si vous souhaitez utiliser un cache en mémoire, vous pouvez utiliser un serveur comme Redis ou créer un processus Node dédié avec une API de lecture/écriture pour que tous les autres travailleurs communiquent avec.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dIR_CAkmtPFgtaGTOKBFkA.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Ne voyez pas cela comme un inconvénient, car l'utilisation d'une entité séparée pour vos besoins de mise en cache d'application fait partie de la _décomposition_ de votre application pour la scalabilité. Vous devriez probablement le faire même si vous exécutez sur une machine à cœur unique.

Autre que la mise en cache, lorsque nous exécutons sur un cluster, la communication avec état devient généralement un problème. Comme la communication n'est pas garantie d'être avec le même travailleur, la création d'un canal avec état sur un travailleur n'est pas une option.

L'exemple le plus courant pour cela est l'authentification des utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jKAmrLPMer6_kmpIjyGzxA.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Avec un cluster, la requête d'authentification arrive au processus d'équilibrage maître, qui est envoyée à un travailleur, en supposant que ce soit A dans cet exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dNUlcuEXPkk44A63ct0s0g.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Le travailleur A reconnaît maintenant l'état de cet utilisateur. Cependant, lorsque le même utilisateur fait une autre requête, l'équilibreur de charge finira par les envoyer à d'autres travailleurs, qui ne les ont pas authentifiés. Garder une référence à une session utilisateur authentifiée dans la mémoire d'une instance ne fonctionnera plus.

Ce problème peut être résolu de nombreuses manières. Nous pouvons simplement partager l'état entre les nombreux travailleurs que nous avons en stockant les informations de ces sessions dans une base de données partagée ou un nœud Redis. Cependant, l'application de cette stratégie nécessite certaines modifications de code, ce qui n'est pas toujours une option.

Si vous ne pouvez pas faire les modifications de code nécessaires pour créer un stockage partagé de sessions ici, il existe une stratégie moins invasive mais pas aussi efficace. Vous pouvez utiliser ce qui est connu sous le nom d'équilibrage de charge collant. Cela est beaucoup plus simple à mettre en œuvre car de nombreux équilibreurs de charge prennent en charge cette stratégie par défaut. L'idée est simple. Lorsqu'un utilisateur s'authentifie avec une instance de travailleur, nous gardons un enregistrement de cette relation au niveau de l'équilibreur de charge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4LNRLkZ9n_p8OKtmRM9LA.png)
_Capture d'écran capturée depuis mon cours Pluralsight — Advanced Node.js_

Ensuite, lorsque le même utilisateur envoie une nouvelle requête, nous effectuons une recherche dans cet enregistrement pour déterminer quel serveur a authentifié leur session et continuons à les envoyer à ce serveur au lieu du comportement distribué normal. De cette façon, le code côté serveur n'a pas besoin d'être modifié, mais nous ne bénéficions pas vraiment de l'équilibrage de charge pour les utilisateurs authentifiés ici, donc utilisez l'équilibrage de charge collant uniquement si vous n'avez pas d'autre option.

Le module cluster ne prend en réalité pas en charge l'équilibrage de charge collant, mais quelques autres équilibreurs de charge peuvent être configurés pour effectuer un équilibrage de charge collant par défaut.

Merci d'avoir lu.

Apprendre React ou Node ? Consultez mes livres :

* [Apprendre React.js en construisant des jeux](http://amzn.to/2peYJZj)
* [Node.js Au-delà des bases](http://amzn.to/2FYfYru)