---
title: Ajout de Socket.io à Node.js multithread
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T20:47:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-socket-io-to-multi-threaded-node-js-df404b424276
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iCeTauiYBnC5UTzlOIKmyw.jpeg
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
seo_title: Ajout de Socket.io à Node.js multithread
seo_desc: 'By Maciej Cieślar

  One of the disadvantages of Node is that it is single-threaded. Of course, there
  is a way around it — namely a module called cluster. Cluster enables us to spread
  our application over multiple threads.

  Now, however, a new problem pr...'
---

Par Maciej Cieślar

L'un des inconvénients de Node est qu'il est monothread. Bien sûr, il existe un moyen de contourner cela — à savoir un module appelé **cluster**. Cluster nous permet de répartir notre application sur plusieurs threads.

Cependant, un nouveau problème se présente. Voyez-vous, notre code exécuté sur plusieurs instances a en réalité quelques inconvénients significatifs. L'un d'eux est de ne pas avoir d'états globaux.

Normalement, dans une instance monothread, cela ne serait pas une grande source d'inquiétude. Pour nous maintenant, cela change tout.

Voyons pourquoi.

### Donc, quel est le problème ?

Notre application est un simple chat en ligne fonctionnant sur quatre threads. Cela permet à un utilisateur d'être connecté en même temps sur son téléphone et son ordinateur.

Imaginez que nous avons configuré les sockets exactement de la manière dont nous les aurions configurés pour un seul thread. En d'autres termes, nous avons maintenant un grand état global avec des sockets.

Lorsque l'utilisateur se connecte sur son ordinateur, le site web ouvre la connexion avec une instance Socket.io sur notre serveur. Le socket est stocké dans l'état du thread #3.

Maintenant, imaginez que l'utilisateur va dans la cuisine pour prendre une collation et emporte son téléphone avec lui — naturellement, il veut continuer à discuter avec ses amis en ligne.

Son téléphone se connecte au thread #4, et le socket est enregistré dans l'état du thread.

Envoyer un message depuis son téléphone ne servira à rien pour l'utilisateur. Seules les personnes du thread #3 pourront voir le message. Cela est dû au fait que les sockets enregistrés sur le thread #3 ne sont pas magiquement stockés sur les threads #1, #2 et #4 également.

Ironiquement, même l'utilisateur lui-même ne verra pas ses messages sur son ordinateur une fois qu'il reviendra de la cuisine.

Bien sûr, lorsqu'il actualisera le site web, nous pourrions envoyer une requête GET et récupérer les 50 derniers messages, mais nous ne pouvons pas vraiment dire que c'est la manière 'dynamique', n'est-ce pas ?

### Pourquoi cela se produit-il ?

Répartir notre serveur sur plusieurs threads est en quelque sorte équivalent à avoir plusieurs serveurs séparés. Ils ne connaissent pas l'existence des autres et ne partagent certainement aucune mémoire. Cela signifie qu'un objet sur une instance n'existe pas sur les autres.

Les sockets enregistrés dans le thread #3 ne sont pas nécessairement tous les sockets que l'utilisateur utilise à ce moment-là. Si les amis de l'utilisateur sont sur différents threads, ils ne verront pas les messages de l'utilisateur à moins qu'ils n'actualisent le site web.

Idéalement, nous aimerions notifier les autres instances d'un événement pour l'utilisateur. De cette manière, nous pouvons être sûrs que chaque appareil connecté reçoit des mises à jour en direct.

### Une solution

Nous pouvons notifier les autres threads en utilisant le paradigme de messagerie publish/subscribe (**pubsub**) de [Redis](https://redis.io/).

**Redis** est un magasin de structures de données en mémoire open source (sous licence **BSD**). Il peut être utilisé comme une base de données, un cache et un courtier de messages.

Cela signifie que nous pouvons utiliser Redis pour avoir des événements distribués entre nos instances.

Notez que normalement, nous stockerions probablement toute notre structure à l'intérieur de Redis. Cependant, puisque la structure n'est pas sérialisable et doit être gardée 'vivante' dans la mémoire, nous allons stocker une partie de celle-ci sur chaque instance.

### Le flux

Réfléchissons maintenant aux étapes dans lesquelles nous allons gérer un événement entrant.

1. L'événement appelé **message** arrive à l'un de nos sockets — de cette manière, nous n'avons pas à écouter chaque événement possible.
2. À l'intérieur de l'objet passé au gestionnaire de cet événement en tant qu'argument, nous pouvons trouver le nom de l'événement. Par exemple, **sendMessage** — `.on('message', ({ event }) =>{})`.
3. Si un gestionnaire existe pour ce nom, nous allons l'exécuter.
4. Le gestionnaire peut exécuter **dispatch** avec une réponse.
5. Le dispatch envoie l'événement de réponse à notre Redis pubsub. De là, il est **émis** à chacune de nos instances.
6. Chaque instance l'émet à leur socketsState, garantissant que chaque client connecté va recevoir l'événement.

Cela semble compliqué, je sais, mais restez avec moi.

### Implémentation

Voici le [dépôt](https://github.com/maciejcieslar/multithreaded-socket) avec l'environnement prêt, afin que nous n'ayons pas à installer et configurer tout nous-mêmes.

Tout d'abord, nous allons configurer un serveur avec **Express**.

```javascript
import * as moduleAlias from 'module-alias';

moduleAlias.addAliases({
  src: __dirname,
});

import * as express from 'express';
import * as http from 'http';
import * as socketio from 'socket.io';

const port = 7999;

const app = express();
const server = http.createServer(app);
const io = initSocket(socketio(server).of('/socket'));

server.listen(port, () => {
  console.log(`Écoute sur le port ${port}.`);
});
```

Nous créons une application Express, un serveur HTTP et initialisons les sockets.

Maintenant, nous pouvons nous concentrer sur l'ajout des sockets.

Nous passons l'instance du serveur Socket.io à notre fonction dans laquelle nous définissons les middlewares.

```javascript
const initSocket = (instance: socketio.Namespace): socketio.Namespace =>
  instance.use(onAuth).use(onConnection);
```

### onAuth

La fonction **onAuth** imite simplement une autorisation simulée. Dans notre cas, elle est basée sur un token.

Personnellement, je la remplacerais probablement par [JWT](https://jwt.io/) à l'avenir, mais ce n'est pas imposé de quelque manière que ce soit.

```javascript
const onAuth: SocketMiddleware = (socket, next) => {
  const { token, id }: { token: string; id: string } =
    socket.request._query || socket.request.headers;

  if (!token) {
    return next(new Error('Échec de l\'autorisation, aucun token n\'a été fourni !'));
  }

  // mock
  const user = checkToken(token, id);

  socket.user = user;

  return next();
};
```

Passons maintenant au middleware **onConnection**.

### onConnection

```javascript
const onConnection: SocketMiddleware = (socket, next) => {
  if (!socket.user) {
    return next(new Error('Quelque chose s\'est mal passé.'));
  }

  const { id } = socket.user;

  socketsState.add(id, socket);

  socket.on('message', ({ event, args }) => {
    const handler = handlers[event];

    if (!handler) {
      return null;
    }

    return handler && handler({ id, args });
  });

  socket.on('disconnect', () => {
    return socketsState.remove(id, socket);
  });

  return next();
};
```

Ici, nous voyons que nous récupérons l'**id** de l'utilisateur, qui a été défini dans le middleware précédent, et le sauvegardons dans notre socketsState, avec la clé étant l'id et la valeur étant un tableau de sockets.

Ensuite, nous écoutons l'événement **message**. Toute notre logique est basée sur cela — chaque événement que le frontend nous envoie sera appelé : **message**.

Le nom de l'événement sera envoyé à l'intérieur de l'objet d'arguments — comme indiqué ci-dessus.

### Handlers

Comme vous pouvez le voir dans onConnection, spécifiquement dans l'écouteur de l'événement message, nous cherchons un gestionnaire basé sur le nom de l'événement.

Notre **handlers** est simplement un objet dans lequel la clé est le nom de l'événement et la valeur est la fonction. Nous allons l'utiliser pour écouter les événements et répondre en conséquence.

```javascript
const dispatchTypes = {
  MESSAGE_SENT: 'message_sent',
  POST_UPDATED_NOTIFICATION: 'post_updated_notification',
};

interface Handlers {
  [key: string]: ({ id, args }: { id: string; args: any }) => any;
}

const handlers: Handlers = {
  sendMessage: async ({ id, args }) => {
    // await sendMessageToUser();

    dispatch({
      id,
      event: dispatchTypes.MESSAGE_SENT,
      args: {
        message: `Un message de l'utilisateur avec l'id: ${id} a été envoyé`,
      },
    });
  },
  postUpdated: async ({ id, args }) => {
    dispatch({
      id,
      event: dispatchTypes.POST_UPDATED_NOTIFICATION,
      args: {
        message: 'Un post dans lequel vous avez été mentionné a été mis à jour',
      },
    });
  },
};

export = handlers;
```

De plus, plus tard, nous allons ajouter la fonction **dispatch** et l'utiliser pour envoyer l'événement à travers les instances.

### SocketsState

Nous connaissons l'interface de notre état, mais nous devons encore l'implémenter.

Nous ajoutons des méthodes pour ajouter et supprimer un socket, ainsi que pour émettre un événement.

```javascript
import * as socketio from 'socket.io';

interface SocketsState {
  [id: string]: socketio.Socket[];
}

const socketsState: SocketsState = {};

const add = (id: string, socket: socketio.Socket) => {
  if (!socketsState[id]) {
    socketsState[id] = [];
  }

  socketsState[id] = [...socketsState[id], socket];

  return socketsState[id];
};

const remove = (id: string, socket: socketio.Socket) => {
  if (!socketsState[id]) {
    return null;
  }

  socketsState[id] = socketsState[id].filter((s) => s !== socket);

  if (!socketsState[id].length) {
    socketsState[id] = undefined;
  }

  return null;
};

const emit = ({
  event,
  id,
  args,
}: {
  event: string;
  id: string;
  args: any;
}) => {
  if (!socketsState[id]) {
    return null;
  }

  socketsState[id].forEach((socket) =>
    socket.emit('message', { event, id, args }),
  );

  return null;
};

export { add, remove, emit };

```

La fonction **add** vérifie si l'état a une propriété qui est égale à l'id de l'utilisateur. Si c'est le cas, alors nous l'ajoutons simplement à notre tableau déjà existant. Sinon, nous créons d'abord un nouveau tableau.

La fonction **remove** vérifie également si l'état a l'id de l'utilisateur dans ses propriétés. Si ce n'est pas le cas, elle ne fait rien. Sinon, elle filtre le tableau pour supprimer le socket du tableau. Ensuite, si le tableau est vide, elle le supprime de l'état, en définissant la propriété à **undefined**.

### Redis' pubsub

Pour créer notre **pubsub**, nous allons utiliser le package appelé **node-redis-pubsub**.

```javascript
import * as NRP from 'node-redis-pubsub';

const client = new NRP({
  port: 6379,
  scope: 'message',
});

export = client;
```

### Ajout de dispatch

Ok, maintenant tout ce qu'il nous reste à faire est d'ajouter la fonction dispatch...

```javascript
const dispatch = ({
  event,
  id,
  args,
}: {
  event: string;
  id: string;
  args: any;
}) => pubsub.emit('outgoing_socket_message', { event, id, args });
```

...et ajouter un écouteur pour **outgoing_socket_message**. De cette manière, chaque instance reçoit l'événement et l'envoie aux sockets de l'utilisateur.

```javascript
pubsub.on('outgoing_socket_message', ({ event, id, args }) =>
  socketsState.emit({ event, id, args }),
);
```

### Rendre le tout multithread

Enfin, ajoutons le code nécessaire pour que notre serveur soit multithread.

```javascript
import * as os from 'os';
import * as cluster from 'cluster';

const spawn = () => {
  const numWorkes = os.cpus().length;

  for (let i = 0; i < numWorkes; i += 1) {
    cluster.fork();
  }

  cluster.on('online', () => {
    console.log('Worker spawned');
  });

  cluster.on('exit', (worker, code, status) => {
    if (code === 0 || worker.exitedAfterDisconnect) {
      console.log(`Worker ${worker.process.pid} a terminé son travail.`);
      return null;
    }

    console.log(
      `Worker ${
        worker.process.pid
      } a crashé avec le code ${code} et le statut ${status}.`,
    );
    return cluster.fork();
  });
};

export { spawn };
```

```javascript
import * as moduleAlias from 'module-alias';

moduleAlias.addAliases({
  src: __dirname,
});

import * as express from 'express';
import * as http from 'http';
import * as cluster from 'cluster';
import * as socketio from 'socket.io';
import * as killPort from 'kill-port';
import { initSocket } from 'src/common/socket';
import { spawn } from 'src/clusters';

const port = 7999;

if (cluster.isMaster) {
  killPort(port).then(spawn);
} else {
  const app = express();
  const server = http.createServer(app);
  const io = initSocket(socketio(server).of('/socket'));

  server.listen(port, () => {
    console.log(`Écoute sur le port ${port}.`);
  });
}

```

Note : Nous devons tuer le port, car après avoir quitté notre processus **Nodemon** avec Ctrl + c, il reste simplement en suspens.

Avec un peu de réglage, nous avons maintenant des sockets fonctionnels sur toutes les instances. Résultat : un serveur beaucoup plus efficace.

Merci beaucoup d'avoir lu !

J'apprécie que tout cela puisse sembler écrasant au premier abord et difficile à assimiler d'un coup. Dans cet esprit, je vous encourage vivement à relire le code dans son intégralité et à le considérer comme un tout.

Si vous avez des questions ou des commentaires, n'hésitez pas à les mettre dans la section des commentaires ci-dessous ou à m'envoyer un [message](https://www.mcieslar.com/contact).

Consultez mes [réseaux sociaux](https://www.maciejcieslar.com/about/) !

[Rejoignez ma newsletter](http://eepurl.com/dAKhxb) !

_Publié à l'origine sur [www.mcieslar.com](https://www.mcieslar.com/adding-socket-io-to-multithreaded-node) le 10 septembre 2018._