---
title: Adding Socket.io to multi-threaded Node.js
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
seo_title: null
seo_desc: 'By Maciej Cieślar

  One of the disadvantages of Node is that it is single-threaded. Of course, there
  is a way around it — namely a module called cluster. Cluster enables us to spread
  our application over multiple threads.

  Now, however, a new problem pr...'
---

By Maciej Cieślar

One of the disadvantages of Node is that it is single-threaded. Of course, there is a way around it — namely a module called **cluster**_._ Cluster enables us to spread our application over multiple threads.

Now, however, a new problem presents itself. See, our code being run across multiple instances actually has some significant downsides. One of them is not having global states.

Normally, in a single-threaded instance, this would not be much of a worry. For us now it changes everything.

Let’s see why.

### So, what is the problem?

Our application is a simple online chat running on four threads. This enables a user to be logged in at the same time on their phone and computer.

Imagine that we have sockets set up exactly the way we would have set them for one thread. In other words we now have one big global state with sockets.

When the user logs in on their computer, the website opens up the connection with a Socket.io instance on our server. The socket is stored in the state of thread #3.

Now, imagine the user goes to the kitchen to grab a snack and takes their phone with them — naturally wanting to keep texting with their friends online.

Their phone connects to thread #4, and the socket is saved in the thread’s state.

Sending a message from their phone will do the user no good. Only people from thread #3 are going to be able to see the message. That is because the sockets saved on thread #3 are not somehow magically stored on threads #1, #2 and #4 as well.

Funny enough, even the user themself is not going to see their messages on their computer once they come back from the kitchen.

Of course, when they refresh the website, we could send a GET request and fetch the last 50 messages, but we cannot really say it is the ‘dynamic’ way, can we?

### Why is this happening?

Spreading our server over multiple threads is in some way tantamount to having several separate servers. They do not know about each other’s existence and certainly do not share any memory. This means that an object on one instance does not exist on the other.

Sockets saved in thread #3 are not necessarily all the sockets that the user is using at the moment. If the user’s friends are on different threads, they are not going to see the user’s messages unless they refresh the website.

Ideally, we would like to notify other instances about an event for the user. This way we can be sure that every connected device is receiving live updates.

### A solution

We can notify other threads by using [Redis](https://redis.io/)’ publish/subscribe [messaging paradigm](https://redis.io/topics/pubsub) (**pubsub**).

**Redis** is an open source (**BSD**-licensed) in-memory data structure store. It can be used as a database, cache and message broker.

This means that we can use Redis to have events distributed between our instances.

Note that normally we would probably store our entire structure inside Redis. However, since the structure is not serializable and needs to be kept “alive” inside the memory, we are going to store part of it on each instance.

### The flow

Let’s now think about the steps in which we are going to handle an incoming event.

1. The event called **message** comes to one of our sockets — this way, we do not have to listen for every possible event.
2. Inside the object passed to the handler of this event as an argument, we can find the name of the event. For example, **sendMessage** — `.on('message', ({ event }) =>{})`.
3. If there is a handler for this name, we are going execute it.
4. The handler may execute **dispatch** with a response.
5. The dispatch sends the response event to our Redis pubsub_._ From there it gets **emitted** to each one of our instances.
6. Each instance emits it to their socketsState, ensuring every connected client is going to receive the event.

Seems complicated, I know, but bear with me.

### Implementation

Here is the [repository](https://github.com/maciejcieslar/multithreaded-socket) with the environment ready, so that we do not have to install and set everything up ourselves.

First, we are going to set up a server with **Express**.

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
  console.log(`Listening on port ${port}.`);
});
```

We create an Express app, HTTP server and init sockets.

Now we can focus on adding sockets.

We pass the Socket.io’s server instance to our function in which we set the middlewares.

```javascript
const initSocket = (instance: socketio.Namespace): socketio.Namespace =>
  instance.use(onAuth).use(onConnection);
```

### onAuth

The **onAuth** function simply imitates a mock authorization. In our case it is token-based.

Personally, I would probably replace it with [JWT](https://jwt.io/) in the future, but it is not enforced in any way.

```javascript
const onAuth: SocketMiddleware = (socket, next) => {
  const { token, id }: { token: string; id: string } =
    socket.request._query || socket.request.headers;

  if (!token) {
    return next(new Error('Authorization failed, no token has been provided!'));
  }

  // mock
  const user = checkToken(token, id);

  socket.user = user;

  return next();
};
```

Now, let’s move on to the **onConnection** middleware.

### onConnection

```javascript
const onConnection: SocketMiddleware = (socket, next) => {
  if (!socket.user) {
    return next(new Error('Something went wrong.'));
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

Here we see that we retrieve the user’s **id**, which was set in the previous middleware, and save it in our socketsState, with the key being the id and the value being an array of sockets.

Next, we listen for the **message** event. Our entire logic is based on that — every event the frontend sends us is going to be called: **message**.

The name of the event will be sent inside the arguments object — as stated above.

### Handlers

As you can see in onConnection, specifically in the listener for the message event, we are looking for a handler based on the event’s name.

Our **handlers** is simply an object in which the key is the event name and the value is the function. We will use it to listen for events and respond accordingly.

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
        message: `A message from user with id: ${id} has been send`,
      },
    });
  },
  postUpdated: async ({ id, args }) => {
    dispatch({
      id,
      event: dispatchTypes.POST_UPDATED_NOTIFICATION,
      args: {
        message: 'A post you have been mentioned in has been updated',
      },
    });
  },
};

export = handlers;
```

Also, later on, we are going to add the **dispatch** function and use it to send the event across the instances.

### SocketsState

We know the interface of our state, but we have yet to implement it.

We add methods for adding and removing a socket, as well as for emitting an event.

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

The **add** function checks whether the state has a property which is equal to the user’s id. If that is the case, then we simply add it to our already existing array. Otherwise, we create a new array first.

The **remove** function also checks if the state has the user’s id in its properties. If not — it does nothing. Otherwise, it filters the array to remove the socket from the array. Then if the array is empty it removes it from the state, setting the property to **undefined**.

### Redis’ pubsub

For creating our **pubsub** we are going to use the package called **node-redis-pubsub**.

```javascript
import * as NRP from 'node-redis-pubsub';

const client = new NRP({
  port: 6379,
  scope: 'message',
});

export = client;
```

### Adding dispatch

Ok, now all that’s left to do is to add the dispatch function…

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

…and add a listener for **outgoing_socket_message**. This way, each instance receives the event and sends it to the user’s sockets.

```javascript
pubsub.on('outgoing_socket_message', ({ event, id, args }) =>
  socketsState.emit({ event, id, args }),
);
```

### Making it all multi-threaded

Finally, let’s add the code needed for our server to be multi-threaded.

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
      console.log(`Worker ${worker.process.pid} finished his job.`);
      return null;
    }

    console.log(
      `Worker ${
        worker.process.pid
      } crashed with code ${code} and status ${status}.`,
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
    console.log(`Listening on port ${port}.`);
  });
}

```

Note: We have to kill the port, because after quitting our **Nodemon** process with Ctrl + c it just hangs there.

With a little tweaking, we now have working sockets across all instances. As a result: a much more efficient server.

Thank you very much for reading!

I appreciate that it all might seem overwhelming at first and strenuous to take it all in at once. With that in mind, I highly encourage you to read the code again in its entirety and ponder it as a whole.

If you have any questions or comments feel free to put them in the comment section below or send me a [message](https://www.mcieslar.com/contact).

Check out my [social media](https://www.maciejcieslar.com/about/)!

[Join my newsletter](http://eepurl.com/dAKhxb)!

_Originally published at [www.mcieslar.com](https://www.mcieslar.com/adding-socket-io-to-multithreaded-node) on September 10, 2018._

