---
title: Comment concevoir un système distribué qui contrôle l'animation d'objets en
  utilisant RxJx, Node et WebSockets
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
seo_title: Comment concevoir un système distribué qui contrôle l'animation d'objets
  en utilisant RxJx, Node et WebSockets
seo_desc: 'By Enrico Piccinin

  In my previous article, How to think reactively and animate moving objects using
  RxJs, I described how to build a MobileObject class that simulates the movement
  of an object subject to accelerations imposed on it by an external con...'
---

Par Enrico Piccinin

Dans mon article précédent, [Comment penser de manière réactive et animer des objets en mouvement en utilisant RxJs](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac), j'ai décrit comment construire une classe **MobileObject** qui simule le mouvement d'un objet soumis à des accélérations imposées par un contrôleur externe.

Maintenant, je veux vous montrer un système distribué simple qui permet à une application **Controller** de contrôler à distance le mouvement d'un **MobileObject**. Une deuxième application distante, le **Monitor**, montre le mouvement de l'objet sur un plan à deux dimensions. Au centre du système se trouve un **MobileObjectServer**, qui est l'endroit où vivent les **MobileObjects**.

Le but de cet article est d'expliquer comment la pensée réactive peut progressivement produire une conception qui mappe les exigences de manière très naturelle et produit une solution élégante. **Nous finirons par résoudre le problème en nous abonnant à un seul Observable**.

Nous nous concentrerons sur la partie serveur, qui est la plus intrigante de ce point de vue.

Pour l'implémentation, nous utiliserons RxJs et TypeScript. Le serveur fonctionne sur Node. Tous les composants communiquent en utilisant Web-Sockets.

La base de code complète, composée du Server Controller et Monitor, peut être trouvée [ici](https://github.com/EnricoPicci/mobile-object-observables).

### Schéma du système distribué

Le schéma logique du système distribué est représenté dans le diagramme suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*N6105oynT3__Doc_VreZhw.png)
_Schéma du système distribué_

Au centre se trouve le **MobileObjectServer** où les instances des **MobileObjets** s'exécutent. Chaque **MobileObject** est contrôlé par son **Controller**, qui est une application Web à travers laquelle nous pouvons émettre des commandes (comme accélérer, freiner) au **MobileObject**. Le mouvement de tous les **MobileObjects** peut être vu sur un ou plusieurs **Monitors**. Chaque **Monitor** est à nouveau une application Web.

Le diagramme suivant montre un exemple de flux d'interaction entre un **Controller**, un **Monitor** et le **MobileObjectServer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AMmLkEOKyV9vheNXM4F0fg.png)
_Flux d'interaction exemple_

### Les exigences du serveur en termes d'événements

Nous pouvons exprimer les exigences pour la partie serveur de notre système distribué en termes d'événements :

* **Événement1** — lorsqu'un **Controller** se connecte => créer un **MobileObject**
* **Événement2** — lorsqu'un **Controller** reçoit une commande => transmettre la commande au **MobileObject** contrôlé par le **Controller**
* **Événement3** — lorsqu'un **Controller** se déconnecte => supprimer le **MobileObject** contrôlé par le **Controller**
* **Événement4** — lorsqu'un **Monitor** se connecte => commencer à envoyer les données dynamiques de tous les **MobileObjects** en cours d'exécution au **Monitor** nouvellement connecté
* **Événement5** — lorsqu'un **MobileObject** est ajouté => commencer à envoyer ses données dynamiques à tous les **Monitors** connectés
* **Événement6** — lorsqu'un **Monitor** se déconnecte => arrêter d'envoyer les flux de données dynamiques pour tous les **MobileObjects** à ce **Monitor**

La pensée réactive produira une conception qui mappe naturellement les exigences exprimées de cette manière.

### Les éléments composant le serveur

Le composant serveur de l'application distribuée est composé de deux éléments principaux :

* la classe **MobileObject**, qui implémente la logique de mouvement dynamique en utilisant les Observables RxJs — cela a été décrit en détail [ici](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac)
* la classe **MobileObjectServer**, qui gère le protocole web-socket, reçoit des commandes du **Controller** et envoie aux **Monitors** toutes les informations sur la dynamique du **MobileObject**. Cette implémentation a été inspirée par [cet article](https://medium.com/dailyjs/real-time-apps-with-typescript-integrating-web-sockets-node-angular-e2b57cbd1ec1?t=1&cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email&iid=9b197a27b4a14948b1d2fd4ad999e0a1&uid=39235406&nid=244%20276893704) de [Luis Aviles](https://www.freecodecamp.org/news/reactive-thinking-how-to-design-a-distributed-system-with-rxjs-websockets-and-node-57d772f89260/undefined).

#### APIs de MobileObject

Faisons un bref aperçu de la classe **MobileObject** — tous les détails peuvent être trouvés [ici](https://medium.freecodecamp.org/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac) tandis que le code peut être trouvé dans [ce dépôt](https://github.com/EnricoPicci/mobile-object-observables).

Le **MobileObject** offre deux familles d'APIs.

La première est l'ensemble des méthodes par lesquelles un **Controller** externe peut émettre des commandes qui affectent la dynamique de l'objet (par exemple, accélérer, freiner).

Les secondes sont des flux de données en lecture seule qui communiquent aux clients externes, les **Monitors**, les données pertinentes sur le comportement dynamique de l'objet (c'est-à-dire, sa position et sa vitesse au fil du temps).

![Image](https://cdn-media-1.freecodecamp.org/images/1*fv6FyPHZ-6CifV96bFKUCg.png)
_APIs de MobileObject_

Pour déplacer une instance d'un **MobileObject**, un **Controller** doit l'allumer (avec la méthode `turnOn()`), appliquer l'accélération souhaitée (avec les méthodes `accelerateX(acc: number)` et `accelerateY(acc: number)`), et puis peut-être freiner (avec la méthode `brake()`).

Lorsque qu'un **Monitor** se connecte au **MobileObjectServer**, le **MobileObjectServer** s'abonne à `dynamicsObs` et à l'observable des **MobileObjects** en cours d'exécution sur le serveur. Il commence alors à envoyer les données liées à leur mouvement aux **Monitors** connectés.

Pour les besoins de cet article, c'est tout ce que vous devez savoir sur le **MobileObject**. 

### Sockets en tant qu'Observables

Le **MobileObjectServer** commence à faire quelque chose lorsqu'un client, soit un **Controller** soit un **Monitor**, ouvre une connexion websocket. Au fil du temps, le **MobileObjectServer** peut recevoir de nombreuses demandes pour ouvrir une connexion de la part de nombreux clients.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z4I5iqA1BdVKuth770mqMw.png)
_Séquence de sockets ouverts au fil du temps_

Cela ressemble à un Observable de sockets. Voici comment l'obtenir en utilisant la bibliothèque `socket.io` :

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

Via la fonction `sockets`, nous créons un Observable de `SocketObs` (nous verrons l'implémentation de cette classe plus tard). Chaque fois que le serveur websocket reçoit une demande de _connexion_ et crée un nouveau _socket_, l'Observable retourné par cette fonction émet une instance de `SocketObs` qui enveloppe le _socket_ nouvellement créé.

#### Messages sur les sockets en tant qu'Observables

Les sockets peuvent être utilisés pour envoyer des messages du client au serveur et vice versa. Avec la bibliothèque `socket.io`, nous pouvons envoyer des messages en utilisant la méthode `emit`.

`SocketIO.Socket.emit(event: string, args: any[]): SocketIO.Socket`

Le paramètre `event` peut être vu comme un identifiant du type de message que nous voulons envoyer. Les paramètres `args` peuvent être utilisés pour envoyer des données spécifiques à un seul message.

Quiconque est intéressé par un certain type de message (ou événement, pour utiliser la terminologie `socket.io`) peut commencer à écouter sur le socket en utilisant la méthode `on`.

`SocketIO.Emitter.on(event: string, fn: Function): SocketIO.Emitter`

![Image](https://cdn-media-1.freecodecamp.org/images/1*9dXtrny7FzljFxyS886iZg.png)
_Séquence de messages reçus au fil du temps_

Encore une fois, les séquences de messages reçues par le récepteur ressemblent à des Observables. Voici comment nous pouvons créer des Observables qui émettent chaque fois qu'un message d'un certain type est reçu.

La méthode `onMessageType` est celle qui fait le tour. Elle retourne un Observable, qui émet chaque fois qu'un message de type `messageType` est reçu.

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

De cette manière, les événements de sockets, ou messages comme nous les appelons ici, ont été transformés en Observables. Ce sont eux qui vont être les fondations de notre conception.

### Déterminer la nature du Client

Il existe deux types de clients qui peuvent se connecter avec le **MobileObjectServer**. L'un est le **Controller** et l'autre est le **Monitor**. Le **MobileObjectServer** doit d'abord déterminer quel type de client il va traiter sur un socket spécifique.

La manière dont nous avons choisi d'implémenter une telle logique est de faire en sorte que le **Controller** et le **Monitor** envoient différents types de messages comme premier message.

* **Controller** envoie un message de type BIND_CONTROLLER
* **Monitor** envoie un message de type BIND_MONITOR

En fonction du type du premier message reçu sur un socket, le **MobileObjectServer** est capable d'identifier s'il communique avec un **Controller** ou un **Monitor**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYPnLICInzJl6nG6oRVFVw.png)
_Comment déterminer la nature du client sur un socket_

Dès qu'un socket est créé, le **MobileObjectServer** doit commencer à écouter les deux types de messages, BIND_CONTROLLER et BIND_MONITOR. Le premier à se produire gagnera. C'est une `course` entre les deux Observables qui mappent les deux différents types de messages.

Une telle logique doit être répétée chaque fois qu'un nouveau socket est créé, c'est-à-dire chaque fois que l'Observable retourné par la fonction `[sockets](https://gist.github.com/EnricoPicci/35f3c3a2a2a3f96cfdf7b89d46a5d499)` émet. Par conséquent, nous devons fusionner tous les événements qui gagnent la course. Nous devons utiliser l'opérateur `mergeMap`, qui fusionne tous les événements soulevés par les Observables impliqués, et aplatit les résultats dans un nouvel Observable (`mergeMap` était autrefois connu sous le nom de `flatMap`).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ieEjio8CpdLJeO8Cje8ezA.png)
_Observable qui émet des événements spécifiques en fonction de la nature du Client_

Le code pour obtenir ce résultat est le suivant :

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

Maintenant que nous savons comment différencier les **Controllers** et les **Monitors**, nous pouvons nous concentrer sur ce qu'il faut faire dans ces deux cas.

### Événements pertinents pour un Monitor

Un **Monitor** montre le mouvement de tous les **MobileObjects** qui s'exécutent sur le **MobileObjectServer**. Donc le **MobileObjectServer** doit envoyer les bonnes informations aux monitors aux bons moments. Voyons d'abord quels sont ces moments, c'est-à-dire quels sont les événements pertinents dont le **MobileObjectServer** doit être conscient afin de remplir sa tâche.

#### Ajout et suppression de MobileObjects

Les premiers événements pertinents sont :

* un **MobileObject** a été ajouté => le MobileObject est affiché sur le **Monitor**
* un **MobileObject** a été supprimé => le MobileObject est supprimé du **Monitor**

Les **MobileObjects** sont ajoutés ou supprimés au fil du temps, donc de tels événements peuvent être modélisés avec deux Observables :

* un Observable qui émet lorsqu'un **MobileObject** est ajouté
* un Observable qui émet lorsqu'un **MobileObject** est supprimé

Une fois qu'un **Monitor** est connecté, le **MobileObjectServer** commence à s'intéresser aux deux Observables, donc il doit les `fusionner` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DL6Y8XNzv-8TjdV-A5_70A.png)
_Fusion des événements d'ajout et de suppression de MobileObject pour un Monitor_

Similaire à ce que nous avons vu précédemment, nous devons répéter une telle logique chaque fois qu'un **Monitor** est ajouté. Par conséquent, nous devons `mergeMap` tous les Observables qui sont le résultat de la `fusion` de l'Observable _'mobile object added'_ avec l'Observable _'mobile object removed'_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T8Pfbzu-eR4JH3PYwmQCFQ.png)
_Événements d'ajout et de suppression de MobileObject pour tous les Monitors_

Voici le code pour obtenir un Observable qui émet chaque fois qu'un **MobileObject** doit être ajouté ou supprimé de chaque **Monitor** :

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
                    // quelque chose sera ajouté ici bientôt pour faire fonctionner cette logique
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

Nous avons introduit quelques éléments avec ce code qui valent la peine d'être commentés ici.

Nous avons créé la classe `MobileObjectServer`, qui sera l'endroit où nous coderons toute notre logique serveur à partir de maintenant.

La méthode `handleMonitorsObs`, que nous allons enrichir plus tard, retourne simplement la `fusion` de deux Observables, `mobileObjectAdded` et `mobileObjectRemoved`, qui sont des Subjects. C'est la `fusion` "interne" montrée dans l'image ci-dessus.

Les Subjects sont des Observables, et peuvent donc être fusionnés comme nous le faisons ici. Mais les Subjects sont aussi des Observers, donc nous pouvons émettre des événements à travers eux. Comme nous le verrons plus tard dans le code, il y aura un moment où nous utiliserons ces Subjects pour émettre les événements que leurs noms suggèrent.

Le dernier point est lié au code que nous avons ajouté dans la méthode startSocketServer :

```
race(
   socket.onMessageType(MessageType.BIND_MONITOR)
   .pipe(
      map(() => (sObs: SocketObs) => this.handleMonitorObs(sObs))
   ),
   socket.onMessageType(MessageType.BIND_CONTROLLER)
   // quelque chose sera ajouté ici bientôt pour faire fonctionner cette logique
)
.pipe(
   mergeMap(handler => handler(socket))
)
```

C'est essentiellement une manière de dire : chaque fois qu'un message BIND_MONITOR est reçu, retourner la fonction

```js
(socketObs: SocketObs) => this.handleMonitorObs(socketObs)
```

qui sera exécutée dans l'opérateur `mergeMap` pipé dans le résultat de la fonction `race`. Cet opérateur `mergeMap` est le `mergeMap` externe montré dans l'image ci-dessus.

Une autre manière de lire le code est la suivante : tout événement correspondant à un message de type BIND_MONITOR est transformé par la logique de

```
mergeMap(() => this.handleMonitorObs(socket))
```

où `socket` est l'instance de type `SocketsObs` émise par la fonction `race`.

Bientôt nous ajouterons quelque chose de similaire pour le cas BIND_CONTROLLER pour faire fonctionner toute cette logique.

#### Gérer les Observables de dynamique de MobileObject

Considérons un **Monitor** qui se connecte au **MobileObjectServer**. Après la connexion, un couple de MobileObjects sont ajoutés au **MobileObjectServer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YRY2hAFqwOZVkNQ3I32mAw.png)
_MobileObjects ajoutés pour un Monitor_

Maintenant, pour chaque **MobileObject**, nous devons commencer à considérer les Observables de dynamique qu'ils offrent dans le cadre de leurs APIs. Ces Observables émettent, à intervalles de temps réguliers, des données sur la dynamique (position et vitesse) du **MobileObject**. Si `mobileObject` stocke une référence à un **MobileObject**, nous pouvons obtenir son Observable de dynamique via `mobileObject.dynamicsObs` (voir les APIs de MobileObject).

Tout d'abord, nous devons transformer chaque événement représentant le fait qu'un **MobileObject** a été ajouté en la série d'événements émis par son `dynamicsObs`. Ensuite, nous `mergeMap` toutes ces séries en un nouvel Observable unique qui émet tous les événements dynamiques pour tous les MobileObjects qui sont ajoutés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UTxwGbTOjjdLsq9Nh1Il3w.png)
_Événements de dynamique pour un seul Monitor_

Ensuite, nous appliquons tout ce jazz à tous les **Monitors** qui se connectent au **MobileObjectServer**. Nous finissons donc avec un nouvel Observable qui émet des données de dynamique pour tous les **Monitors** et tous les **MobileObjects** (plus tous les événements liés au fait qu'un **MobileObject** a été supprimé).

![Image](https://cdn-media-1.freecodecamp.org/images/1*r2U2J0j342nGlDEK4-Rwsw.png)
_Événements pertinents pour tous les Monitors_

Pour chaque intervalle de temps, nous avons des groupes de quatre événements liés à l'émission de données sur la dynamique de nos **MobileObjects**. Pourquoi ? Cela a du sens si nous pensons que nous avons deux **Monitors** et deux **MobileObjects**. Chaque **MobileObject** doit envoyer ses données de dynamique à chaque **Monitor** pour chaque intervalle de temps. Il est donc correct de voir quatre événements par intervalle de temps.

Une fois que cela est clair, le code est très simple :

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
                    // quelque chose sera ajouté ici bientôt pour faire fonctionner cette logique
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

Nous avons simplement introduit un changement simple. Nous avons modifié la méthode `handleMonitorObs` pour ajouter l'opérateur `mergeMap`. Cela transforme l'Observable `mobileObjectAdded` de sorte que le nouvel Observable émet les données de dynamique que nous recherchons.

Le reste est resté inchangé.

### Résumé jusqu'à présent

Qu'avons-nous fait jusqu'à présent ? Nous avons simplement transformé des Observables pour obtenir de nouveaux Observables qui émettent tous les événements auxquels **MobileObjectServer** s'intéresse lorsqu'il doit traiter un **Monitor**. Rien d'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zDynxsrbo7Vh5U915jKXlA.png)
_Transformations des Observables pertinents pour les Monitors_

Vous pouvez voir comment ces transformations sont reflétées dans le code dans l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tFariAfbE7FLeRr_1GeCAg.png)

La seule chose que nous devons faire maintenant est d'ajouter les _effets secondaires_ souhaités aux événements pertinents. Cela nous permettra finalement d'atteindre ce que nous voulons, c'est-à-dire communiquer au Monitor les bonnes informations au bon moment.

Mais avant de passer aux _effets secondaires_, couvrons ce que **MobileObjectServer** doit faire lorsqu'il interagit avec un **Controller**, l'autre client de notre système distribué.

### Événements pertinents pour un Controller

Lorsque qu'un **Controller** se connecte au **MobileObjectServer**, il y a moins de choses dont le serveur doit se soucier. Au moins, il y a moins d'événements pertinents imbriqués qui se produisent.

Les choses dont le **MobileObjectServer** doit se soucier sont :

* Un **Controller** s'est connecté, ce qui dans notre logique simple signifie que nous devons créer un tout nouveau **MobileObject**
* Le **Controller** a envoyé des commandes pour son **MobileObject**
* Le **Controller** s'est déconnecté. Dans notre implémentation, cela signifie que nous devons d'une manière ou d'une autre supprimer le **MobileObject** contrôlé par le **Controller** (nous avons une relation 1 à 1 entre **MobileObject** et son **Controller**)

Nous connaissons déjà le premier événement : c'est celui émis par l'Observable retourné par `socket.onMessageType(BIND_CONTROLLER)`.

Les commandes sont envoyées par le **Controller** au **MobileObjectServer** sous forme de messages. Nous pouvons donc créer un Observable de commandes reçues sur un certain _socket_ (reçues d'un certain Controller) puisque chaque Controller a son propre _socket_. Nous faisons cela en utilisant simplement la méthode `onMessageType` de `SocketObs`

```
socket.onMessageType(CONTROLLER_COMMAND)
```

`SocketObs` offre également une méthode, `onDisconnect`, qui retourne un Observable qui émet lorsque le _socket_ est déconnecté. C'est ce dont nous avons besoin pour traiter le troisième événement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LFWTYTT9W7p0gcNK3GrqoA.png)
_Événements pertinents lorsqu'un Controller se connecte à MobileObjectServer_

Puisque nous traitons avec plus d'un **Controller** potentiellement connecté au **MobileObjectServer**, il ne devrait pas vous surprendre d'apprendre que nous devons `mergeMap` le résultat de la `fusion`. C'est le même type de transformation que nous avons déjà fait plusieurs fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoOipJVQ4KsaEpVlF5VRDA.png)

Le code ne devrait pas être une surprise non plus.

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

Nous avons simplement ajouté une méthode `handleControllerObs` qui traite les _commandes reçues_ et la _déconnexion_ d'un Controller. Nous appliquons la transformation mergeMap comme nous l'avons déjà fait avec `handleMonitorObs`.

#### **Résumé des transformations appliquées aux Controllers**

Le diagramme suivant illustre toutes les transformations que nous avons appliquées en partant de l'Observable qui émet lorsqu'un **Controller** se connecte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoOipJVQ4KsaEpVlF5VRDA.png)
_Transformations des flux d'événements (Observables) pertinents pour les Controllers_

### L'Observable Final

Si nous mettons ensemble les transformations que nous avons faites pour les **Monitors** et les **Controllers**, ce que nous obtenons est l'Observable Final suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vrRAT7gGmSBn2QsR7XmyIQ.png)
_L'arbre d'événements produit en s'abonnant à l'Observable Final_

Simplement en s'abonnant à cet Observable Final unique, tout l'arbre d'événements se déploie.

### Effets secondaires

Le bel arbre d'événements que nous avons créé en nous abonnant à l'Observable Final ne fait rien. Mais il fait un bon travail en mappant les **Événements** que nous avons identifiés en décrivant les exigences du Serveur au début de cet article.

En gros, il nous dit clairement quand nous devons faire _quelque chose_.

Ce _quelque chose_ est ce que nous appelons un _effet secondaire_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jTYJFA6ScG_uakdASIRIRA.png)
_Effets secondaires_

Lorsque qu'un Controller se connecte et se déconnecte, nous créons ou supprimons respectivement un **MobileObject**. En tant qu'_effet secondaire_ de ces actions, nous déclenchons les événements "MobileObject ajouté" et "MobileObject supprimé" en utilisant les Subjects `mobileObjectAdded` et `mobileObjectRemoved` que nous avons introduits il y a quelques paragraphes.

#### Comment implémenter les _effets secondaires_

Dans RxJs, il existe différentes manières d'implémenter les _effets secondaires_.

Les Observers en sont une. Nous pouvons ajouter des Observers pendant que nous nous `abonnons` en utilisant l'opérateur `tap` (anciennement connu sous le nom de `do`).

Une autre manière est de les injecter dans toute fonction que nous passons à tout opérateur RxJs.

Nous allons principalement utiliser `tap`, car il nous permet de placer des effets secondaires dans tout l'arbre d'événements. Mais nous allons également placer des effets secondaires directement à l'intérieur des fonctions que nous passons aux opérateurs RxJs.

Le seul endroit où nous ne mettons pas d'effets secondaires est `subscribe`. La raison est que, étant donné la manière dont nous l'avons construit, le Final Observer émet de nombreux types d'événements différents. Par conséquent, `subscribe`, qui fonctionne de la même manière pour tous les événements, n'est pas le bon endroit pour mettre un comportement qui dépend de certains types d'événements.

Espérons qu'à ce stade, le code parle de lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x4BfIT5unvy9VT2u8NEUYQ.png)
_Implémentation des effets secondaires dans le code_

### Dernier point mais non des moindres : l'achèvement des Observables

Il y a une chose que nous devons encore faire pour compléter notre conception : arrêter les flux d'événements, ou compléter les Observables, lorsqu'un **Controller** ou un **Monitor** se déconnecte.

#### Lorsqu'un Controller se déconnecte

Lorsqu'un Controller se déconnecte, nous supprimons le **MobileObject** qu'il contrôle. Dans le cadre de la suppression, il est important de s'assurer que le **MobileObjectServer** arrête d'envoyer les données dynamiques liées à ce **MobileObject** aux Monitors connectés. Cela signifie que nous devons compléter l'Observable suivant :

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
)
```

Nous pouvons facilement y parvenir en utilisant simplement l'opérateur `takeUntil` avec l'Observable `mobileObjectRemoved` que nous connaissons déjà :

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
  takeUntil(this.mobileObjectRemoved.pipe(
    filter(id => id === mobObjInfo.mobObjId)
  ))
)
```

`takeUntil` garantit qu'un Observable se termine lorsque l'Observable passé en paramètre à `takeUntil` émet.

`mobileObjectRemoved` émet chaque fois qu'un **MobileObject** est supprimé. Ce que nous voulons, cependant, c'est d'arrêter l'envoi d'informations dynamiques lorsqu'un **MobileObject** spécifique, identifié par son id, est supprimé. Nous ajoutons donc la logique de `filter`.

#### Lorsqu'un Monitor se déconnecte

Dans ce cas, nous pouvons également utiliser **takeUntil**.

Nous savons lorsqu'un Monitor se déconnecte parce que le `socket`, de type `SocketObs`, qui lui est associé émet via l'Observable `socket.onDisconnect()`. Donc ce que nous devons faire, c'est arrêter l'envoi d'informations dynamiques lorsque `socket.onDisconnect()` émet.

La logique finale pour gérer l'achèvement de l'Observable est donc

```js
mobObjInfo.mobObj.dynamicsObs
.pipe(
  tap(dynamics => socket.send(MessageType.DYNAMICS_INFO, dynamics)),
  takeUntil(this.stopSendDynamics(socket, mobObjInfo.mobObjId))
)
```

où

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

Et voici à quoi ressemble le cœur du code implémentant notre logique :

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

Cela a été un voyage assez long. Nous avons vu un raisonnement guidé par la pensée réactive et certaines implémentations de ce raisonnement.

Nous avons commencé par transformer les événements WebSockets en Observables. Ensuite, en appliquant des transformations incrémentielles, nous avons fini par créer un seul Observable qui, une fois abonné, déploie tous les événements qui nous intéressent.

À ce stade, l'ajout des effets secondaires qui nous permettent d'atteindre notre objectif a été simple.

Ce processus mental de conception, qui est incrémental en lui-même, est le sens que je donne à la "Pensée Réactive".

La base de code complète, comprenant le Server Controller et Monitor, peut être trouvée [ici](https://github.com/EnricoPicci/mobile-object-observables).