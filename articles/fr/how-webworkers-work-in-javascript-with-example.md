---
title: Comment fonctionnent les Web Workers en JavaScript – Avec un exemple pratique
  en JS
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-01-04T00:31:54.000Z'
originalURL: https://freecodecamp.org/news/how-webworkers-work-in-javascript-with-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/christopher-burns-8KfCR12oeUM-unsplash-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: websocket
  slug: websocket
- name: webworker
  slug: webworker
seo_title: Comment fonctionnent les Web Workers en JavaScript – Avec un exemple pratique
  en JS
seo_desc: "In this article, I will walk you through an example that will show you\
  \ how web workers function in JavaScript with the help of WebSockets. \nI think\
  \ it's helpful to work with a practical use case because it is much simpler to understand\
  \ the concepts w..."
---

Dans cet article, je vais vous guider à travers un exemple qui vous montrera comment les web workers fonctionnent en JavaScript avec l'aide des WebSockets. 

Je pense qu'il est utile de travailler avec un cas d'utilisation pratique car il est beaucoup plus simple de comprendre les concepts lorsque vous pouvez les relier à la vie réelle. 

Dans ce guide, vous allez apprendre ce que sont les web workers en JavaScript, vous aurez une brève introduction aux WebSockets, et vous verrez comment vous pouvez gérer les sockets de la manière appropriée. 

Cet article est assez orienté application/pratique, donc je vous suggère d'essayer l'exemple au fur et à mesure pour obtenir une bien meilleure compréhension.

Plongeons-nous dans le sujet.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Que sont les web workers en JavaScript ?](#heading-que-sont-les-web-workers-en-javascript)
* [Brève introduction aux web sockets](#heading-brève-introduction-aux-web-sockets)
* [Description du cas d'utilisation](#heading-description-du-cas-dutilisation)
* [Structure du projet](#heading-structure-du-projet)
* [Architecture client et serveur](#heading-architecture-client-et-serveur)
* [Système de Worker](#heading-système-de-worker)
* [Communication entre l'UI et le socket via web worker](#heading-communication-entre-lui-et-le-socket-via-web-worker)
* [Résumé](#heading-resumé)

## Prérequis

Avant de commencer à lire cet article, vous devriez avoir une compréhension de base des sujets suivants :

* Diagrammes de classes : Nous allons les utiliser pour présenter notre exemple. Voici quelques ressources que vous pouvez utiliser pour en apprendre davantage à leur sujet : 
    * [Diagrammes de classes](https://drawio-app.com/uml-class-diagrams-in-draw-io/)
    * [Cours sur les diagrammes UML](https://www.freecodecamp.org/news/uml-diagrams-full-course/)
* [Diagramme de contexte et diagrammes de conteneurs](https://www.notion.so/JS-Classes-a-boon-to-the-society-6360d1a702fe49da9b7ba98b0e03fe37)
* [React](https://reactjs.org/)
* Web sockets
    * [Introduction aux sockets](https://javascript.info/websocket)
    * [Comment JavaScript fonctionne : Plongée en profondeur dans les WebSockets et HTTP/2 avec SSE + comment choisir le bon chemin](https://blog.sessionstack.com/how-javascript-works-deep-dive-into-websockets-and-http-2-with-sse-how-to-pick-the-right-path-584e6b8e3bf7)
* [Différence entre portée et contexte](https://blog.kevinchisholm.com/javascript/difference-between-scope-and-context/)
* [Objets globaux](https://developer.mozilla.org/en-US/docs/Glossary/Global_object)

## Que sont les web workers en JavaScript ?

Un web worker est une fonctionnalité du navigateur. Ce sont de vrais threads du système d'exploitation qui peuvent être créés en arrière-plan de votre page actuelle afin qu'ils puissent effectuer des tâches complexes et intensives en ressources. 

Imaginez que vous avez des données volumineuses à récupérer depuis le serveur, ou que des rendus complexes doivent être effectués sur l'UI. Si vous faites cela directement sur votre page web, celle-ci pourrait devenir saccadée et impacter l'UI. 

Pour atténuer cela, vous pouvez simplement créer un thread – c'est-à-dire un web worker – et laisser le web worker s'occuper des tâches complexes. 

Vous pouvez communiquer avec le web worker de manière assez simple, ce qui peut être utilisé pour transférer des données entre le worker et l'UI.

Des exemples courants de web workers seraient : 

* Pages de tableau de bord qui affichent des données en temps réel telles que les prix des actions, les utilisateurs actifs en temps réel, etc.
* Récupération de gros fichiers depuis le serveur
* Fonctionnalité d'enregistrement automatique

Vous pouvez créer un web worker en utilisant la syntaxe suivante :

```javascript
const worker = new Worker("<worker_file>.js");
```

`Worker` est une interface API qui vous permet de créer un thread en arrière-plan. Nous devons passer un paramètre, qui est un fichier `<worker_file>.js`. Cela spécifie le fichier worker que l'API doit exécuter.

**NOTE** : Un thread est créé une fois qu'un appel `Worker` est initié. Ce thread ne communique qu'avec son créateur, c'est-à-dire le fichier qui a créé ce thread.

Un worker peut être partagé ou utilisé par plusieurs consommateurs/scripts. Ce sont des workers partagés. La syntaxe du worker partagé est très similaire à celle des workers mentionnés ci-dessus.

```javascript
const worker = new SharedWorker("<worker_file>.js");
```

Vous pouvez en lire plus sur les `SharedWorker`s dans [ce guide](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker).

### Histoire des web workers

Les web workers s'exécutent dans un contexte différent, c'est-à-dire qu'ils ne s'exécutent pas dans une portée globale telle que le contexte de la fenêtre. Les web workers ont leur propre contexte de worker dédié qui s'appelle `DedicatedWorkerGlobalScope`.

Il y a certains cas où vous ne pouvez pas utiliser les web workers, cependant. Par exemple, vous ne pouvez pas les utiliser pour manipuler le DOM ou les propriétés de l'objet window. Cela est dû au fait que le worker n'a pas accès à l'objet window. 

Les web workers peuvent également créer de nouveaux web workers. Les web workers communiquent avec leur créateur en utilisant certaines méthodes comme `postMessage`, `onmessage`, et `onerror`. Nous examinerons ces méthodes de plus près dans les sections suivantes de cet article.

## Brève introduction aux Web Sockets

Un web socket est un type de communication qui se produit entre deux parties/entités utilisant un protocole WebSocket. Il fournit en fait un moyen de communiquer entre les deux entités connectées de manière persistante. 

Vous pouvez créer un simple web socket comme ci-dessous :

```javascript
const socket = new WebSocket("ws://example.com");
```

Ici, nous avons créé une simple connexion socket. Vous remarquerez que nous avons passé un paramètre au constructeur `WebSocket`. Ce paramètre est une URL à laquelle la connexion doit être établie. 

Vous pouvez en lire plus sur les web sockets en vous référant au lien **Websockets** dans les prérequis.

## Description du cas d'utilisation

**NOTE** : Les diagrammes de contexte, de conteneur et de classe dessinés dans cet article de blog ne suivent pas exactement les conventions exactes de ces diagrammes. Ils sont approximés ici afin que vous puissiez comprendre les concepts de base.

Avant de commencer, je vous suggère de lire sur les modèles c4, les diagrammes de conteneurs et les diagrammes de contexte. Vous pouvez trouver des ressources à leur sujet dans la section des prérequis.

Dans cet article, nous allons considérer le cas d'utilisation suivant : le transfert de données en utilisant des web workers via le protocole socket.

Nous allons construire une application web qui tracera les données sur un graphique linéaire toutes les 1,5 secondes. L'application web recevra les données de la connexion socket via les web workers. Voici le diagramme de contexte de notre cas d'utilisation :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/c4_webworker.drawio--2-.png)
_Diagramme de conteneur_

Comme vous pouvez le voir sur le diagramme ci-dessus, il y a 4 composants principaux à notre cas d'utilisation :

1. Personne : Un utilisateur qui va utiliser notre application
2. Système logiciel : Application cliente – Il s'agit de l'UI de notre application. Elle se compose d'éléments DOM et d'un web worker.
3. Système logiciel : Système de worker – Il s'agit d'un fichier worker qui réside dans l'application cliente. Il est responsable de la création d'un thread worker et de l'établissement de la connexion socket.
4. Système logiciel : Application serveur – Il s'agit d'un simple fichier JavaScript qui peut être exécuté par `node` pour créer un serveur socket. Il se compose de code qui aide à lire les messages de la connexion socket.

Maintenant que nous comprenons le cas d'utilisation, plongeons-nous dans chacun de ces modules et voyons comment l'application entière fonctionne.

## **Structure du** Projet

Veuillez suivre ce [lien](https://github.com/keyurparalkar/webworker_examples) pour obtenir le code complet du projet que j'ai développé pour cet article.

Notre projet est divisé en deux dossiers. Le premier est le dossier serveur qui contient le code serveur. Le second est le dossier client, qui contient l'UI client, c'est-à-dire une application React et le code du web worker. 

Voici la structure des répertoires :

```
├── client
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── README.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── components
│   │   │   ├── LineChartSocket.jsx
│   │   │   └── Logger.jsx
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── pages
│   │   │   └── Homepage.jsx
│   │   ├── wdyr.js
│   │   └── workers
│   │       └── main.worker.js
│   └── yarn.lock
└── server
    ├── package.json
    ├── package-lock.json
    └── server.mjs
```

Pour exécuter l'application, vous devez d'abord démarrer le serveur socket. Exécutez les commandes suivantes une à la fois pour démarrer le serveur socket (en supposant que vous êtes dans le répertoire parent) :

```shell
cd server
node server.mjs
```

Ensuite, démarrez l'application cliente en exécutant les commandes suivantes (en supposant que vous êtes dans le répertoire parent) :

```shell
cd client
yarn run start
```

Ouvrez `http://localhost:3000` pour démarrer l'application web.

## Application Client et Serveur

L'application cliente est une simple application React, c'est-à-dire une application [CRA](https://create-react-app.dev/), qui se compose d'une page d'accueil. Cette page d'accueil se compose des éléments suivants :
- Deux boutons : `start connection` et `stop connection` qui aideront à démarrer et arrêter la connexion socket selon les besoins.
- Un composant de graphique linéaire - Ce composant tracerà les données que nous recevons du socket à intervalles réguliers.
- Message journalisé - Il s'agit d'un simple composant React qui affichera l'état de la connexion de nos web sockets.

Voici le diagramme de conteneur de notre application cliente.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Untitled.png)
_Diagramme de conteneur : Application cliente_

Voici à quoi ressemblera l'UI :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2021-12-28-08-32-06.png)
_UI réelle_

Pour consulter le code de l'UI client, allez dans le dossier client. Il s'agit d'une application create-react-app régulière, sauf que j'ai supprimé certains codes de base que nous n'avons pas besoin pour ce projet. 

`App.jsx` est en fait le code de démarrage. Si vous le consultez, nous avons appelé le composant `<Homepage />` dans celui-ci.

Maintenant, examinons le composant `Homepage`.

```jsx
const Homepage = () => {
  const [worker, setWorker] = useState(null);
  const [res, setRes] = useState([]);
  const [log, setLog] = useState([]);
  const [buttonState, setButtonState] = useState(false);

  const hanldeStartConnection = () => {
    // Envoyer le message au worker [postMessage]
    worker.postMessage({
      connectionStatus: "init",
    });
  };

  const handleStopConnection = () => {
    worker.postMessage({
      connectionStatus: "stop",
    });
  };
	
	//UseEffect1
  useEffect(() => {
    const myWorker = new Worker(
      new URL("../workers/main.worker.js", import.meta.url)
    ); //NOUVELLE SYNTAXE
    setWorker(myWorker);

    return () => {
      myWorker.terminate();
    };
  }, []);

	//UseEffect2
  useEffect(() => {
    if (worker) {
      worker.onmessage = function (e) {
        if (typeof e.data === "string") {
          if(e.data.includes("[")){
            setLog((preLogs) => [...preLogs, e.data]);
          } else {
            setRes((prevRes) => [...prevRes, { stockPrice: e.data }]);
          }
        }

        if (typeof e.data === "object") {
          setButtonState(e.data.disableStartButton);
        }
      };
    }
  }, [worker]);

  return (
    <>
      <div className="stats">
        <div className="control-panel">
          <h3>Exemple WebWorker Websocket</h3>
          <button
            id="start-connection"
            onClick={hanldeStartConnection}
            disabled={!worker || buttonState}
          >
            Démarrer la connexion
          </button>
          &nbsp;
          <button
            id="stop-connection"
            onClick={handleStopConnection}
            disabled={!buttonState}
          >
            Arrêter la connexion
          </button>
        </div>
        <LineChartComponent data={res} />
      </div>
      <Logger logs={log}/>
    </>
  );
};
```

Comme vous pouvez le voir, il s'agit simplement d'un composant fonctionnel régulier qui rend deux boutons – un graphique linéaire, et un composant personnalisé `Logger`. 

Maintenant que nous savons à quoi ressemble notre composant de page d'accueil, plongeons-nous dans la manière dont le thread du web worker est réellement créé. Dans le composant ci-dessus, vous pouvez voir qu'il y a deux hooks `useEffect` utilisés. 

Le premier est utilisé pour créer un nouveau thread worker. Il s'agit d'un simple appel au constructeur `Worker` avec un nouvel opérateur comme nous l'avons vu dans la section précédente de cet article. 

Mais il y a quelques différences ici : nous avons passé un objet URL au constructeur du worker plutôt que de passer le chemin du fichier worker dans la chaîne.

```javascript
const myWorker = new Worker(new URL("../workers/main.worker.js", import.meta.url));
```

Vous pouvez en lire plus sur cette syntaxe [ici](https://webpack.js.org/guides/web-workers/).

Si vous essayez d'importer ce web worker comme ci-dessous, alors notre create-react-app ne pourra pas le charger/bundler correctement, donc vous obtiendrez une erreur puisque le fichier worker n'a pas été trouvé pendant le bundling :

```javascript
const myWorker = new Worker("../workers/main.worker.js");
```

Ensuite, nous ne voulons pas non plus que notre application exécute le thread worker même après le rafraîchissement, ou ne voulons pas créer plusieurs threads lorsque nous rafraîchissons la page. Pour atténuer cela, nous allons retourner un callback dans le même useEffect. Nous utilisons ce callback pour effectuer des nettoyages lorsque le composant est démonté. Dans ce cas, nous terminons le thread worker.

Nous utilisons le `useEffect2` pour gérer les messages reçus du worker.

Les web workers ont une propriété intégrée appelée `onmessage` qui aide à recevoir les messages envoyés par le thread worker. Le `onmessage` est un gestionnaire d'événements de l'interface worker. Il est déclenché chaque fois qu'un événement de message est déclenché. Cet événement de message est généralement déclenché chaque fois que le gestionnaire `postMessage` est exécuté (nous examinerons cela plus en détail dans une section ultérieure).

Ainsi, afin d'envoyer un message au thread worker, nous avons créé deux gestionnaires. Le premier est `handleStartConnection` et le second est `handleStopConnection`. Tous deux utilisent la méthode `postMessage` de l'interface worker pour envoyer le message au thread worker. 

Nous parlerons du message `{connectionStatus: init}` dans notre prochaine section.

Vous pouvez en lire plus sur le fonctionnement interne de `onmessage` et `postMessage` dans les ressources suivantes :

- [Onmessage](https://developer.mozilla.org/en-US/docs/Web/API/Worker/onmessage)
- [Postmessage](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage)

Puisque nous avons maintenant une compréhension de base de la manière dont notre code client fonctionne, passons à l'apprentissage du **Système de Worker dans notre diagramme de contexte ci-dessus.**

## Système de Worker

Pour comprendre le code dans cette section, assurez-vous de consulter le fichier `src/workers/main.worker.js`.

Pour vous aider à comprendre ce qui se passe ici, nous allons diviser ce code en trois parties :

1. Une section `self.onmessage`
2. Comment la connexion socket est gérée en utilisant la fonction `socketManagement()`
3. Pourquoi nous avons besoin de la variable `socketInstance` en haut

### Comment fonctionne `self.onmessage`

Lorsque vous créez une application web worker, vous écrivez généralement un fichier worker qui gère tous les scénarios complexes que vous voulez que le worker exécute. Tout cela se passe dans le fichier `main.worker.js`. Ce fichier est notre fichier worker. 

Dans la section précédente, nous avons vu que nous avons établi un nouveau thread worker dans le `useEffect`. Une fois le thread créé, nous avons également attaché les deux gestionnaires aux boutons `start` et `stop` de la connexion respective. 

Le bouton `start connection` exécutera la méthode `postMessage` avec le message : `{connectionStatus: init}`. Cela déclenche l'événement de message, et puisque l'événement de message est déclenché, tous les événements de message sont capturés par la propriété `onmessage`. 

Dans notre fichier `main.worker.js`, nous avons attaché un gestionnaire à cette propriété `onmessage` :

```javascript
self.onmessage = function (e) {
  const workerData = e.data;
  postMessage("[WORKER] Web worker onmessage établi");
  switch (workerData.connectionStatus) {
    case "init":
      socketInstance = createSocketInstance();
      socketManagement();
      break;

    case "stop":
      socketInstance.close();
      break;

    default:
      socketManagement();
  }
}
```

Ainsi, chaque fois qu'un événement de message est déclenché dans le client, il sera capturé dans ce gestionnaire d'événements. 

Le message `{connectionStatus: init}` que nous envoyons depuis le client est reçu dans l'événement `e`. En fonction de la valeur de connectionStatus, nous utilisons le switch case pour gérer la logique. 

**NOTE** : Nous avons ajouté ce switch case car nous devons isoler une partie du code que nous ne voulons pas exécuter tout le temps (nous examinerons cela dans une section ultérieure).

### Comment la connexion socket est gérée en utilisant la fonction `socketManagement()`

Il y a plusieurs raisons pour lesquelles j'ai déplacé la logique de création et de gestion d'une connexion socket dans une fonction séparée. Voici le code pour une meilleure compréhension du point que j'essaie de faire :

```javascript
function socketManagement() {
  if (socketInstance) {
    socketInstance.onopen = function (e) {
      console.log("[open] Connexion établie");
      postMessage("[SOCKET] Connexion établie");
      socketInstance.send(JSON.stringify({ socketStatus: true }));
      postMessage({ disableStartButton: true });
    };

    socketInstance.onmessage = function (event) {
      console.log(`[message] Données reçues du serveur : ${event.data}`);
      postMessage( event.data);
    };

    socketInstance.onclose = function (event) {
      if (event.wasClean) {
        console.log(`[close] Connexion fermée proprement, code=${event.code}`);
        postMessage(`[SOCKET] Connexion fermée proprement, code=${event.code}`);
      } else {
        // e.g. processus serveur tué ou réseau en panne
        // event.code est généralement 1006 dans ce cas
        console.log('[close] Connexion morte');
        postMessage('[SOCKET] Connexion morte');
      }
      postMessage({ disableStartButton: false });
    };

    socketInstance.onerror = function (error) {
      console.log(`[error] ${error.message}`);
      postMessage(`[SOCKET] ${error.message}`);
      socketInstance.close();
    };
  }
}
```

Il s'agit d'une fonction qui vous aidera à gérer votre connexion socket :
- Pour recevoir le message du serveur socket, nous avons la propriété `onmessage` à laquelle est assigné un gestionnaire d'événements.
- Chaque fois qu'une connexion socket est ouverte, vous pouvez effectuer certaines opérations. Pour cela, nous avons la propriété `onopen` qui est assignée à un gestionnaire d'événements.
- Et si une erreur se produit ou lorsque nous fermons la connexion, nous utilisons les propriétés `onerror` et `onclose` du socket.

Pour créer une connexion socket, il y a une fonction séparée :

```javascript
function createSocketInstance() {
  let socket = new WebSocket("ws://localhost:8080");

  return socket;
} 
```

Toutes ces fonctions sont appelées dans un switch case comme ci-dessous dans le fichier `main.worker.js` :

```javascript
self.onmessage = function (e) {
  const workerData = e.data;
  postMessage("[WORKER] Web worker onmessage établi");
  switch (workerData.connectionStatus) {
    case "init":
      socketInstance = createSocketInstance();
      socketManagement();
      break;

    case "stop":
      socketInstance.close();
      break;

    default:
      socketManagement();
  }
}
```

Ainsi, en fonction du message que l'UI client envoie au worker, la fonction appropriée sera exécutée. Il est assez explicite de savoir quel message doit déclencher quelle fonction particulière, en fonction du code ci-dessus.

Maintenant, considérons un scénario où nous avons placé tout le code à l'intérieur de `self.onmessage`.

```javascript
self.onmessage = function(e){
    console.log("Objet Worker présent ", e);
    postMessage({isLoading: true, data: null});

    let socket = new WebSocket("ws://localhost:8080");

		socket.onopen = function(e) {
		  console.log("[open] Connexion établie");
		  console.log("Envoi au serveur");
		  socket.send("Mon nom est John");
		};
		
		socket.onmessage = function(event) {
		  console.log(`[message] Données reçues du serveur : ${event.data}`);
		};
		
		socket.onclose = function(event) {
		  if (event.wasClean) {
		    console.log(`[close] Connexion fermée proprement, code=${event.code} raison=${event.reason}`);
		  } else {
		    // e.g. processus serveur tué ou réseau en panne
		    // event.code est généralement 1006 dans ce cas
		    console.log('[close] Connexion morte');
		  }
		};

			socket.onerror = function(error) {
			  console.log(`[error] ${error.message}`);
			};
}
```

Cela causerait les problèmes suivants :

1. À chaque appel `postMessage` fait par l'UI client, il y aurait eu une nouvelle instance de socket.
2. Il aurait été difficile de fermer la connexion socket.

Pour ces raisons, tout le code de gestion des sockets est écrit dans une fonction `socketManagement` et géré à l'aide d'un switch case.

### Pourquoi nous avons besoin de la variable `socketInstance` en haut

Nous avons besoin d'une variable `socketInstance` en haut car celle-ci stockera l'instance de socket qui a été créée précédemment. Il s'agit d'une pratique sûre puisque personne ne peut accéder à cette variable de l'extérieur car `main.worker.js` est un module séparé.

## Communication entre l'UI et le socket via web worker

Maintenant que nous comprenons quelle partie du code est responsable de quelle section, nous allons examiner comment nous établissons une connexion socket via les webworkers. Nous verrons également comment nous répondons via le serveur socket pour afficher un graphique linéaire sur l'UI.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Untitled--1-.png)
_Flux de bout en bout de l'application_

**NOTE** : Certaines appels ne sont pas intentionnellement montrés dans le diagramme car cela rendrait le diagramme encombré. Assurez-vous de vous référer au code également tout en vous référant à ce diagramme.

Maintenant, comprenons d'abord ce qui se passe lorsque vous cliquez sur le bouton `start connection` sur l'UI :
1. Une chose à noter ici est que notre thread web worker est créé une fois que le composant est monté, et est supprimé/terminé lorsque le composant est démonté.
1. Une fois le bouton `start connection` cliqué, un appel `postMessage` est fait avec `{connectionStatus: init}`
1. Le gestionnaire d'événements `onmessage` du web worker, qui écoute tous les événements de message, sait qu'il a reçu *connectionStatus comme init.* Il correspond au cas, c'est-à-dire dans le switch case de `main.worker.js`. Il appelle ensuite `createSocketInstance()` qui retourne une nouvelle connexion socket à l'URL : `ws://localhost:8080`
1. Après cela, une fonction `socketManagement()` est appelée qui vérifie si le socket est créé et exécute ensuite quelques opérations.
1. Dans ce flux, puisque la connexion socket vient d'être établie, le gestionnaire d'événements `onopen` de socketInstance est exécuté. 
1. Cela enverra un message `{socketStatus: true}` au serveur socket. Cela enverra également un message à l'UI client via `postMessage({ disableStartButton: true})` qui indique à l'UI client de désactiver le bouton de démarrage.
1. Chaque fois que la connexion socket est établie, alors le `on('connection', ()=>{})` du socket serveur est invoqué. Donc dans l'étape 3, cette fonction est invoquée à l'extrémité du serveur.
1. Le `on('message', () => {})` du socket est invoqué chaque fois qu'un message est envoyé au socket. Donc à l'étape 6, cette fonction est invoquée à l'extrémité du serveur. Cela vérifie si le `socketStatus` est vrai, puis il commence à envoyer un entier aléatoire toutes les 1,5 secondes à l'UI client via les web workers.

Maintenant que nous avons compris comment la connexion est établie, passons à la compréhension de la manière dont le serveur socket envoie les données à l'UI client :

1. Comme discuté ci-dessus, le serveur socket a reçu le message pour envoyer les données, c'est-à-dire un nombre aléatoire toutes les 1,5 secondes.
2. Ces données sont reçues à l'extrémité du web worker en utilisant le gestionnaire `onmessage`. 
3. Ce gestionnaire appelle ensuite la fonction `postMessage` et envoie ces données à l'UI.
4. Après avoir reçu les données, il les ajoute à un tableau en tant qu'objet `stockPrice`. 
5. Cela sert de source de données pour notre composant de graphique linéaire et est mis à jour toutes les 1,5 secondes.

Maintenant que nous comprenons comment la connexion est établie, passons à la compréhension de la manière dont le serveur socket envoie les données à l'UI client :
1. Comme discuté ci-dessus, le serveur socket a reçu le message pour envoyer les données, c'est-à-dire un nombre aléatoire, toutes les 1,5 secondes.
1. Ces données sont reçues à l'extrémité du web worker en utilisant le gestionnaire `onmessage` du socket. 
1. Ce gestionnaire appelle ensuite la fonction `postMessage` du web worker et envoie ces données à l'UI.
1. Après avoir reçu les données via `useEffect2`, il les ajoute à un tableau en tant qu'objet `stockPrice`. 
1. Cela sert de source de données pour notre composant de graphique linéaire et est mis à jour toutes les 1,5 secondes.

**NOTE** : Nous utilisons recharts pour tracer le graphique linéaire. Vous pouvez trouver plus d'informations à ce sujet sur [la documentation officielle](https://recharts.org/en-US/).

Voici à quoi ressemblera notre application en action :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/ezgif.com-gif-maker.gif)
_Exemple de fonctionnement_

## Résumé

Voici donc une rapide introduction à ce que sont les web workers et comment vous pouvez les utiliser pour résoudre des problèmes complexes et créer de meilleures interfaces utilisateur. Vous pouvez utiliser les web workers dans vos projets pour gérer des scénarios complexes d'interface utilisateur. 

Si vous souhaitez optimiser vos workers, lisez les bibliothèques suivantes :

* [comlink](https://www.npmjs.com/package/comlink)
* [thread.js](https://threads.js.org/)

Merci d'avoir lu !

Suivez-moi sur [twitter](https://twitter.com/keurplkar), [github](http://github.com/keyurparalkar), et [linkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).