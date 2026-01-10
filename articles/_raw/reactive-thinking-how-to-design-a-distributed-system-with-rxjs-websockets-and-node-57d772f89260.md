---
title: How to design a distributed system that controls object animation using RxJx,
  Node, and WebSockets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T18:59:27.000Z'
originalURL: https://freecodecamp.org/news/reactive-thinking-how-to-design-a-distributed-system-with-rxjs-websockets-and-node-57d772f89260
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nrD86pjtZh_Xjn9AJZKLRQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: RxJS
  slug: rxjs
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Enrico Piccinin

  In my previous article, How to think reactively and animate moving objects using
  RxJs, I described how to build a MobileObject class that simulates the movement
  of an object subject to accelerations imposed on it by an external con...'
---

By Enrico Piccinin

In my previous article, [How to think reactively and animate moving objects using RxJs](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac), I described how to build a **MobileObject** class that simulates the movement of an object subject to accelerations imposed on it by an external controller.

Now I want to show you a simple distributed system that allows a **Controller** app to remotely control the movement of a **MobileObject.** A second remote app, the **Monitor**, shows the movement of the object on a two-dimensional plan. At the center of the system lays a **MobileObjectServer**, which is the place where the **MobileObjects** live.

The goal of this article is to explain how Reactive thinking can progressively produce a design which maps the requirements very naturally and produces a neat solution. **We will end up solving the problem subscribing to just ONE Observable**.

We’ll focus on the server part, which is the most intriguing from this standpoint.

For the implementation, we’ll use RxJs and TypeScript. The server runs on Node. All the components communicate using Web-Sockets.

The full code base, comprised of the Server Controller and Monitor, can be found [here](https://github.com/EnricoPicci/mobile-object-observables).

### Schema of the distributed system

The logical schema of the distributed system is represented in the following diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/1*N6105oynT3__Doc_VreZhw.png)
_Schema of the distributed system_

At the center lays the **MobileObjectServer** where the instances of the **MobileObjets** run. Each **MobileObject** is controlled by its **Controller**, that is a Web app through which we can issue commands (like accelerate, brake) to the **MobileObject**. The movement of all **MobileObjects** can be seen on one or more **Monitors**. Each **Monitor** is again a Web app.

The following diagram shows a sample interaction flow between one **Controller**, one **Monitor,** and the **MobileObjectServer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AMmLkEOKyV9vheNXM4F0fg.png)
_Sample interaction flow_

### The Server Requirements in terms of events

We can express the requirements for the server part of our distributed system in terms of events:

* **Event1** — when a **Controller** connects => create **a MobileObj**ect
* **Event2** — when a **Controller** receives a command => forward the command to t**he MobileObj**ect controlled by t**he Control**ler
* **Event3** — when a **Controller** disconnects => delete t**he MobileObje**ct controlled by t**he Control**ler
* **Event4** — when a **Monitor** connects => start sending dynamics data of all runni**ng MobileObje**cts to the newly connect**ed Moni**tor
* **Event5** — when a **MobileObject** is added => start sending its dynamics data to all t**he Monito**rs connected
* **Event6** — when a **Monitor** disconnects => stop sending the streams of dynamics data for a**ll MobileObje**cts to th**at Moni**tor

Reactive thinking will produce a design which naturally maps the requirements expressed in this way.

### The elements composing the server

The server component of the distributed application is made up of two main elements:

* the **MobileObject** class, which implements the dynamic movement logic using RxJs Observables — this has been described in detail [here](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac)
* the **MobileObjectServer** class**,** which manages the web-socket protocol, receiving commands from the **Controller** and sending out to the **Monitors** all information about the dynamics of **MobileObject.** This implementation has been inspired by [this article](https://medium.com/dailyjs/real-time-apps-with-typescript-integrating-web-sockets-node-angular-e2b57cbd1ec1?t=1&cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email&iid=9b197a27b4a14948b1d2fd4ad999e0a1&uid=39235406&nid=244%20276893704) from [Luis Aviles](https://www.freecodecamp.org/news/reactive-thinking-how-to-design-a-distributed-system-with-rxjs-websockets-and-node-57d772f89260/undefined).

#### MobileObject APIs

Let’s have a brief overview of the **MobileObject** class — all details can be found [here](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac) while the code can be found in [this repository](https://github.com/EnricoPicci/mobile-object-observables).

The **MobileObject** offers two families of APIs.

The first one is the set of methods through which an external **Controller** can issue commands that affect the dynamics of the object (for example, accelerate, brake).

The second are streams of readonly data which communicate to external clients, the **Monitors**, the relevant data about the dynamic behaviour of the object (that is, its position and velocity over time).

![Image](https://cdn-media-1.freecodecamp.org/images/1*fv6FyPHZ-6CifV96bFKUCg.png)
_APIs of MobileObject_

In order to move an instance of a **MobileObject**, a **Controller** has to turn it on (with the `turnOn()` method), apply the desired acceleration (with the methods `accelerateX(acc: number)` and `accelerateY(acc: number)`), and then maybe brake (with the method `brake()`).

When a **Monitor** connects to the **MobileObjectServer**, the **MobileObjectServer** subscribes to the `dynamicsObs` and the observable of the **MobileObjects** running in the server. It then starts sending the data related to their movement to the connected **Monitors**.

For the purpose of this article, this is all you need to know about the **MobileObject**.

### Sockets as Observables

The **MobileObjectServer** starts doing something when a client, either a **Controller** or a **Monitor**, opens a websocket connection. Over the course of time, the **MobileObjectServer** can receive many requests to open a connection from many clients.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z4I5iqA1BdVKuth770mqMw.png)
_Sequence of sockets opened over time_

This looks like an Observable of sockets. This is how to obtain it using the `socket.io` library:

```js
import { Server } from 'http';

import { Observable } from 'rxjs';
import { Observer } from 'rxjs';

import * as socketIoServer from 'socket.io';

import {SocketObs} from './socket-obs';

export function sockets(httpServer: Server, port) {
    httpServer.listen(port, () => {
        console.log('Running server on port %s', port);
    });
    return new Observable<SocketObs>(
        (subscriber: Observer<SocketObs>) => {
            socketIoServer(httpServer).on('connect', 
                socket => {
                    console.log('client connected');
                    subscriber.next(new SocketObs(socket));
                }
            );
        }
    );
}
```

Via the function `sockets`, we create an Observable of `SocketObs` (we will see the implementation of this class later). Any time the websocket server receives a _connect_ request and creates a new _socket_, the Observable returned by this function emits an instance of `SocketObs` which wraps the _socket_ just created.

#### Messages over sockets as Observables

Sockets can be used to send messages from the client to the server and vice versa. With the `socket.io` library, we can send messages using the `emit` method.

`SocketIO.Socket.emit(event: string, …args: any[]): SocketIO.Socket`

The parameter `event` can be seen as an identifier of the type of message we want to send. The `…args` parameters can be used to send data specific to a single message.

Whoever is interested in a certain type of message (or event, to use the `socket.io` terminology) can start listening on the socket using the method `on`.

`SocketIO.Emitter.on(event: string, fn: Function): SocketIO.Emitter`

![Image](https://cdn-media-1.freecodecamp.org/images/1*9dXtrny7FzljFxyS886iZg.png)
_Sequence of messages received over time_

Again, the sequences of messages received by the Receiver look like Observables. This is how we can create Observables that actually emit any time a message of a certain type is received.

The `onMessageType` method is the one that does the trick. It returns an Observable, which emits any time a message of type `messageType` is received.

```js
import { Observable, Observer } from 'rxjs';

export class SocketObs {
    constructor(private socket: SocketIO.Socket) {}
    
    onMessageType(messageType): Observable<any> {
        return new Observable<any>((observer: Observer<any>) => {
            this.socket.on(messageType, data => observer.next(data));
        });
    }
}
```

In this way, sockets events, or messages as we call them here, have been transformed into Observables. These are going to be the foundations of our design.

### Determine the nature of the Client

There are two types of clients which can connect with the **MobileObjectServer.** One is the **Controller** and one is the **Monitor**. The **MobileObjectServer** first needs to determine which type of client it is going to deal with on a specific socket.

The way we have chosen to implement such logic is to have the **Controller** and the **Monitor** send different message types as their first message.

* **Controller** sends a message of type BIND_CONTROLLER
* **Monitor** sends a message of type BIND_MONITOR

Depending on the type of the first message received on a socket, the **MobileObjectServer** is able to identify whether it is communicating with a **Controller** or a **Monitor**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYPnLICInzJl6nG6oRVFVw.png)
_How to determine the nature of the client on a socket_

As soon as a socket is created, the **MobileObjectServer** has to start listening to both types of messages, BIND_CONTROLLER and BIND_MONITOR. The first to occur will win. It is a `race` between the two Observables which map the two different types of messages.

Such logic has to be repeated any time a new socket is created, that is any time the Observable returned by the function `[sockets](https://gist.github.com/EnricoPicci/35f3c3a2a2a3f96cfdf7b89d46a5d499)` emits. Therefore, we need to merge all the events that win the race. We need to use the `mergeMap` operator, which merges all the events raised by the Observables involved, and flatten the results into a new Observable (`mergeMap` was formerly know as `flatMap`).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ieEjio8CpdLJeO8Cje8ezA.png)
_Observable that emits specific events depending on the nature of the Client_

The code to obtain this result is the following:

```js
startSocketServer(httpServer: Server) {
    sockets(httpServer, this.port).pipe(
        mergeMap(socket =>
            race(
                socket.onMessageType(MessageType.BIND_MONITOR),
                socket.onMessageType(MessageType.BIND_CONTROLLER)
            )
        )
    )
    .subscribe();
}
```

Now that we know how to differentiate **Controllers** and **Monitors**, we can focus on what to do in these two cases.

### Events relevant for a Monitor

A **Monitor** shows the movement of all **MobileObjects** which are running on the **MobileObjectServer**. So the **MobileObjectServer** has to send the right information to the monitors at the right times. Let’s see first what those times are, that is which are the relevant events that the **MobileObjectServer** has to be aware of in order to fulfill its job.

#### Adding and removing MobileObjects

The first relevant events are:

* a **MobileObject** has been added => the MobileObject is shown on t**he Moni**tor
* a **MobileObject** has been removed => the MobileObject is removed from t**he Moni**tor

**MobileObjects** are added or removed over time, so such events can be modeled with two Observables:

* an Observable which emits when a **MobileObject** is added
* an Observable which emits when a **MobileObject** is removed

Once a **Monitor** is connected, the **MobileObjectServer** starts being interested in both of those Observables, so it has to `merge` them:

![Image](https://cdn-media-1.freecodecamp.org/images/1*DL6Y8XNzv-8TjdV-A5_70A.png)
_Merging MobileObject added and removed events for a Monitor_

Similar to what we have seen before, we need to repeat such logic any time a **Monitor** is added. Therefore we need to `mergeMap` all the Observables which are the result of the `merge` of the _‘mobile object added’_ Observable with the _‘mobile object removed’_ Observable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T8Pfbzu-eR4JH3PYwmQCFQ.png)
_Events for MobileObject added and removed for all Monitors_

This is the code to obtain an Observable which emits any time a **MobileObject** has to be added to or removed from every **Monitor:**

```js
import {sockets} from './socket-io-observable';
import {SocketObs} from './socket-obs';

class MobileObjectServer {
    private mobileObjectAdded = new Subject<{mobObj: MobileObject, mobObjId: string}>();
    private mobileObjectRemoved = new Subject<string>();

    startSocketServer(httpServer: Server) {
        sockets(httpServer, this.port).pipe(
            mergeMap(socket =>
                race(
                    socket.onMessageType(MessageType.BIND_MONITOR)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleMonitorObs(socketObs))
                    ),
                    socket.onMessageType(MessageType.BIND_CONTROLLER)
                    // something will be added here soon to make this logic work
                )
                .pipe(
                    mergeMap(handler => handler(socket))
                )
            )
        )
        .subscribe();
    }

    handleMonitorObs(socket: SocketObs) {
        const mobObjAdded = this.mobileObjectAdded;
        const mobObjRemoved = this.mobileObjectRemoved;
        return merge(mobObjAdded, mobObjRemoved);
    }
}

```

We have introduced a few things with this code which are worth commenting on here.

We have created the `MobileObjectServer` class, which will be the place where we will code all our server logic from now on.

The method `handleMonitorsObs`, which we are going to enrich later on, returns simply the `merge` of two Observables, `mobileObjectAdded` and `mobileObjectRemoved`, which are Subjects. This is the “inner” `merge` shown in the picture above.

Subjects are Observables, and therefore can be merged as we do here. But Subjects are also Observers, so we can emit events through them. As we will see later in the code, there will be a time when we will use these Subjects to emit the events their names suggest.

The last point is related to the code we have added in the startSocketServer method:

```
race(
   socket.onMessageType(MessageType.BIND_MONITOR)
   .pipe(
      map(() => (sObs: SocketObs) => this.handleMonitorObs(sObs))
   ),
   socket.onMessageType(MessageType.BIND_CONTROLLER)
   // something will be added here soon to make this logic work
)
.pipe(
   mergeMap(handler => handler(socket))
)
```

This is basically a way to say: any time a BIND_MONITOR message is received, return the function

```js
(socketObs: SocketObs) => this.handleMonitorObs(socketObs)
```

which will be executed within the `mergeMap` operator piped into the result of the `race` function. This `mergeMap` operator is the external `mergeMap` shown in the picture above.

Another way to read the code is the following: any event corresponding to a message of type BIND_MONITOR gets transformed by the logic of

```
mergeMap(() => this.handleMonitorObs(socket))
```

where `socket` is the instance of type `SocketsObs` emitted by the `race` function.

Soon we will add something similar for the BIND_CONTROLLER case to make this whole logic work.

#### Handle MobileObject dynamics Observables

Let’s consider one **Monitor** which connects to the **MobileObjectServer**. After the connection, a couple of MobileObjects are added to the **MobileObjectServer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YRY2hAFqwOZVkNQ3I32mAw.png)
_MobileObjects added for one Monitor_

Now for each **MobileObject,** we have to start considering the dynamics Observables they offer as part of their APIs. These Observables emit, at regular intervals of time, data about the dynamics (position and velocity) of the **MobileObject**. If `mobileObject` stores a reference to a **MobileObject**, we can obtain its dynamics Observable via `mobileObject.dynamicsObs` (see MobileObject APIs).

First we have to transform each event representing the fact that a **MobileObject** has been added into the series of events emitted by its `dynamicsObs`. Then we `mergeMap` all these series into a new single Observable which emits all dynamic events for all MobileObjects which are added.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UTxwGbTOjjdLsq9Nh1Il3w.png)
_Dynamics events for a single Monitor_

Then we apply all this jazz to all the **Monitors** which connect to the **MobileObjectServer.** So we end up with a new Observable which emits dynamics data for all **Monitors** and all **MobileObjects** (plus all events related to the fact that a **MobileObject** has been removed).

![Image](https://cdn-media-1.freecodecamp.org/images/1*r2U2J0j342nGlDEK4-Rwsw.png)
_Relevant events for all Monitors_

Per each time interval, we have groups of four events related to the emission of data about the dynamics of our **MobileObjects**. Why? This makes sense if we think that we have two **Monitors** and two **MobileObjects**. Each **MobileObject** has to send its dynamics data to each **Monitor** per every time interval. Therefore it is correct to see four events per each time interval.

Once this is clear, the code is very simple:

```js
import {sockets} from './socket-io-observable';
import {SocketObs} from './socket-obs';

class MobileObjectServer {
    private mobileObjectAdded = new Subject<{mobObj: MobileObject, mobObjId: string}>();
    private mobileObjectRemoved = new Subject<string>();


    startSocketServer(httpServer: Server) {
        sockets(httpServer, this.port).pipe(
            mergeMap(socket =>
                race(
                    socket.onMessageType(MessageType.BIND_MONITOR)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleMonitorObs(socketObs))
                    ),
                    socket.onMessageType(MessageType.BIND_CONTROLLER)
                    // something will be added here soon to make this logic work
                )
                .pipe(
                    mergeMap(handler => handler(socket))
                )
            )
        )
        .subscribe();
    }

    handleMonitorObs(socket: SocketObs) {
        const mobObjAdded = this.mobileObjectAdded
                              .pipe(
                                mergeMap(data => data.mobileObject.dynamicsObs)
                              );
        const mobObjRemoved = this.mobileObjectRemoved;
        return merge(mobObjAdded, mobObjRemoved);
    }

}

```

We have just introduced one simple change. We changed the `handleMonitorObs` method to add the `mergeMap` operator. This transforms the `mobileObjectAdded` Observable so that the new Observable emits the dynamics data we are looking for.

The rest has remained untouched.

### Summary so far

What have we done so far? We have just transformed Observables to obtain new Observables which emit all the events **MobileObjectServer** is interested in when it has to deal with a **Monitor**. Nothing else.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zDynxsrbo7Vh5U915jKXlA.png)
_Transformations of Observables relevant for Monitors_

You can see how these transformations are reflected in the code in the following image:

![Image](https://cdn-media-1.freecodecamp.org/images/1*tFariAfbE7FLeRr_1GeCAg.png)

The only thing we need to do now is to add the desired _side effects_ to the relevant events. This will eventually allow us to achieve what we want, that is to communicate to the Monitor the right information at the right time.

But before moving to _side effects_, let’s cover what **MobileObjectServer** needs to do when interacting with a **Controller**, the other client in our distributed system.

### Events relevant for a Controller

When a **Controller** connects to the **MobileObjectServer** there are fewer things that the server needs to care about. At least there are fewer nested relevant events happening.

The things that the **MobileObjectServer** needs to care about are:

* A **Controller** has connected, which in our simple logic means that we have to create a brand new **MobileObject**
* The **Controller** has sent commands for its **MobileObject**
* The **Controller** has disconnected. In our implementation, this means that we somehow have to delete the **MobileObject** controlled by the **Controller** (we have a 1 to 1 relationship between **MobileObject** and its **Controller**)

We already know the first event: it is the one emitted by the Observable returned by `socket.onMessageType(BIND_CONTROLLER)`.

Commands are sent by the **Controller** to the **MobileObjectServer** in the form of messages. So we can create an Observable of commands received over a certain _socket (_received from a certain Controller) since each Controller has its own _socket._ We do this by simply using the `onMessageType` method of `SocketObs`

```
socket.onMessageType(CONTROLLER_COMMAND)
```

`SocketObs` also offers a method, `onDisconnect`, which returns an Observable that emits when the _socket_ is disconnected. This is what we need in order to deal with the third event.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LFWTYTT9W7p0gcNK3GrqoA.png)
_Events relevant when a Controller connects to MobileObjectServer_

Since we are dealing with more than one **Controller** potentially connecting to the **MobileObjectServer**, it should not surprise you to learn that we need to `mergeMap` the result of the `merge`. This is the same type of transformation we have already done a few times.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoOipJVQ4KsaEpVlF5VRDA.png)

The code should be no surprise as well.

```js
startSocketServer(httpServer: Server) {
        sockets(httpServer, this.port).pipe(
            mergeMap(socket =>
                race(
                    socket.onMessageType(MessageType.BIND_MONITOR)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleMonitorObs(socketObs))
                    ),
                    socket.onMessageType(MessageType.BIND_CONTROLLER)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleControllerObs(socketObs))
                    ),
                )
                .pipe(
                    mergeMap(handler => handler(socket))
                )
            )
        )
        .subscribe();
}

handleMonitorObs(socket: SocketObs) {
        const mobObjAdded = this.mobileObjectAdded
                              .pipe(
                                mergeMap(data => data.mobileObject.dynamicsObs)
                              );
        const mobObjRemoved = this.mobileObjectRemoved;
        return merge(mobObjAdded, mobObjRemoved);
}

handleControllerObs(socket: SocketObs) {
        const commands = socket.onMessageType(MessageType.CONTROLLER_COMMAND);
        const disconnect = socket.onDisconnect();

        return merge(commands, disconnect);
}
```

We have simply added an `handleControllerObs` method that deals with _commands received_ and the _disconnect_ of a Controller. We apply the mergeMap transformation to it as we have already done with `handleMonitorObs`.

#### **Summary of the transformations applied to Controllers**

The following diagram illustrates all transformations we have applied starting from the Observable that emits when a **Controller** connects.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoOipJVQ4KsaEpVlF5VRDA.png)
_Transformations of event streams (Observables) relevant for Controllers_

### The Final Observable

If we put together the transformations we have done for both the **Monitors** and the **Controllers,** what we obtain is the following final Observable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vrRAT7gGmSBn2QsR7XmyIQ.png)
_The tree of events produced subscribing the Final Observable_

Just by subscribing to this one final Observable, the whole tree of events gets unfolded.

### Side effects

The beautiful tree of events we have created by subscribing to the Final Observable does not do anything. But it does a good job of mapping the **_Events_** we identified while describing the requirements of the Server at the beginning of this article.

Basically it tells us clearly when we have to do _something_.

This _something_ is what we call a _side effect_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jTYJFA6ScG_uakdASIRIRA.png)
_Side effects_

When a Controller connects and disconnects, we respectively create or delete a **MobileObject**. As _side effect_ of these actions is that we raise “_MobileObject added”_ and _“MobileObject deleted”_ events using the `mobileObjectAdded` and `mobileObjectRemoved` Subjects we introduces some paragraphs ago.

#### How to implement _side effects_

In RxJs there are different ways to implement _side effects_.

Observers is one. We can add Observers while we `subscribe` using the `tap` operator (formerly know as `do`).

Another way is to inject them in any function we pass to any RxJs operator.

We are mainly going to use `tap`, since it allows us to place side effects throughout the entire tree of events. But we are also going to place side effects directly inside functions we pass to RxJs operators.

The only place we do not put side effects is `subscribe`. The reason is that, given how we built it, the Final Observer emits many different types of events. Therefore `subscribe`, which works the same for all events, is not the right place to put behavior which depends on certain types of events.

Hopefully at this point the code sort of speaks for itself.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x4BfIT5unvy9VT2u8NEUYQ.png)
_Implementation of Side Effects in the code_

### Last but not least: completion of Observables

There is one thing that we still need to do to complete our design: stop the streams of events, or complete the Observables, when either a **Controller** or a **Monitor** disconnects.

#### When a Controller disconnects

When a Controller disconnects, we delete the **MobileObject** it controls. As part of the deletion, it is important to make sure that the **MobileObjectServer** stops sending dynamics data related to this **MobileObject** to the connected Monitors. This means that we must complete the following Observable:

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
)
```

We can easily achieve this just using the `takeUntil` operator together with the `mobileObjectRemoved` Observable we already know:

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
  takeUntil(this.mobileObjectRemoved.pipe(
    filter(id => id === mobObjInfo.mobObjId)
  ))
)
```

`takeUntil` ensures that an Observable completes when the Observable passed as a parameter to `takeUntil` emits.

`mobileObjectRemoved` emits every time a **MobileObject** is removed. What we want, though, is to stop sending dynamics info when a specific **MobileObject**, identified by its id, is removed. So we add the `filter` logic.

#### When a Monitor disconnects

In this case, we can also use **takeUntil**.

We know when a Monitor disconnects because the `socket`, of type `SocketObs`, associated to it emits via the `socket.onDisconnect()` Observable. So what we need to do is stop sending dynamics info when `socket.onDisconnect()` emits.

So the final logic to govern the completion of the Observable is

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
  takeUntil(this.stopSendDynamics(socket, mobObjInfo.mobObjId))
)
```

where

```
private stopSendDynamics(socket: SocketObs, mobObjId: string){
  return merge(
            this.mobileObjectRemoved.pipe(
                                       filter(id => id === mobObjId)
                                     ),
            socket.onDisconnect()
  );
}
```

And this is how the core of the code implementing our logic looks:

```js
import {sockets} from './socket-io-observable';
import {SocketObs} from './socket-obs';

class MobileObjectServer {
    private mobileObjectAdded = new Subject<{mobObj: MobileObject, mobObjId: string}>();
    private mobileObjectRemoved = new Subject<string>();


        public startSocketServer(httpServer: Server) {
        sockets(httpServer, this.port).pipe(
            mergeMap(socket =>
                race(
                    socket.onMessageType(MessageType.BIND_MONITOR)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleMonitorObs(socketObs))
                    ),
                    socket.onMessageType(MessageType.BIND_CONTROLLER)
                    .pipe(
                        map(() => (socketObs: SocketObs) => this.handleControllerObs(socketObs))
                    ),
                )
                .pipe(
                    mergeMap(handler => handler(socket)) 
                )
            )
        )
        .subscribe();
    }


    private handleMonitorObs(socket: SocketObs) {
        const mobObjAdded = this.mobileObjectAdded
                                .pipe(
                                    tap(mobObjInfo => socket.send(MessageType.MOBILE_OBJECT, mobObjInfo.mobObjId)),
                                    mergeMap(mobObjInfo => mobObjInfo.mobObj.dynamicsObs
                                                    .pipe(
                                                        tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
                                                        takeUntil(this.stopSendDynamicsInfo(socket, mobObjInfo.mobObjId))
                                                    )
                                    )
                                );
        const mobObjRemoved = this.mobileObjectRemoved
                                .pipe(
                                    tap(mobObjId => socket.send(MessageType.MOBILE_OBJECT_REMOVED, mobObjId)),
                                );
        return merge(mobObjAdded, mobObjRemoved);
    }

    private handleControllerObs(socket: SocketObs) {
        const {mobObj, mobObjId} = this.newMobileObject();
        
        this.mobileObjectAdded.next({mobObj, mobObjId});

        const commands = socket.onMessageType(MessageType.CONTROLLER_COMMAND)
                        .pipe(
                            tap(command  => this.execute(command, mobObj))
                        );

        const disconnect = socket.onDisconnect()
                        .pipe(
                            tap(() => this.mobileObjectRemoved.next(mobObjId)),
                        );

        return merge(commands, disconnect);
    }

    private stopSendDynamicsInfo(socket: SocketObs, mobObjId: string) {
        return merge(this.mobileObjectRemoved.pipe(filter(id => id === mobObjId)), socket.onDisconnect());
    }

}

```

### Conclusion

It has been a pretty long journey. We have seen some reasoning driven by Reactive Thinking and some implementations of this reasoning.

We started transforming WebSockets events into Observables. Then, applying incremental transformations, we ended up creating a single Observable that, once subscribed, unfolds all the events we are interested in.

At this point, adding the side effects that allow us to achieve our goal has been straightforward.

This mental process of design, which is incremental in itself, is the meaning I give to “Reactive Thinking”.

The full code base, comprising Server Controller and Monitor, can be found [here](https://github.com/EnricoPicci/mobile-object-observables).

