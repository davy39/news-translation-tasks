---
title: Qu'est-ce qu'il faut pour construire un chatbot ? Découvrons-le.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-28T13:15:30.000Z'
originalURL: https://freecodecamp.org/news/what-does-it-take-to-build-a-chatbot-lets-find-out-b4d009ea8cfd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7EKSA6aQvAYaT6eoV7zEsw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'il faut pour construire un chatbot ? Découvrons-le.
seo_desc: 'By Vanco Stojkov

  Without any delay, the image below shows what we are building:


  An image of nothing.

  To answer the question in the title, “What does it take to build a chatbot?” the
  answer is not much.

  I’m a web developer. It has been my desire to d...'
---

Par Vanco Stojkov

Sans plus tarder, l'image ci-dessous montre ce que nous construisons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tdRn6YIXgnilQWSJrZ5k2w.gif)
_Une image de rien._

Pour répondre à la question du titre, « Qu'est-ce qu'il faut pour construire un chatbot ? », la réponse est : pas grand-chose.

Je suis développeur web. Il a toujours été mon désir de me plonger dans ce domaine passionnant. Malheureusement, je ne peux pas dire que j'ai les connaissances en compréhension du langage naturel (NLU) nécessaires pour construire un chatbot sans aide. La bonne nouvelle est que cette aide est disponible aujourd'hui.

L'API [Cloud Natural Language de Google](https://cloud.google.com/natural-language/), les [API Cognitive Services de Microsoft](https://azure.microsoft.com/en-us/services/cognitive-services/language-understanding-intelligent-service/) et [Watson Conversation d'IBM](https://www.ibm.com/watson/developercloud/conversation.html) fournissent des services NLU commerciaux, avec des niveaux gratuits généreux. Il existe également des services complètement gratuits, du moins pour l'instant. Cela inclut [API.AI](https://api.ai/), qui a récemment été acquis par Google, et [Wit.ai](https://wit.ai/), qui appartient à Facebook.

Du point de vue d'un développeur web, c'est toute l'aide dont nous avons besoin — une API qui éliminera la complexité pour nous.

### Commençons par la partie amusante

Si vous êtes impatient de voir l'exemple en direct, voici la [démo disponible sur Heroku](https://ti-bot.herokuapp.com/). L'ensemble du code pour cet exemple [est disponible sur GitHub](https://github.com/van100j/tibot).

Pour les besoins de cet article, nous allons créer un chatbot appelé TiBot pour répondre à nos questions sur la date et l'heure. Nous utiliserons l'API de [API.AI](https://api.ai/) pour traiter ces questions. Je pense que API.AI est plus intuitif et plus facile à utiliser que [Wit.ai](https://wit.ai/).

À l'arrière-plan, un simple serveur Node.js traitera les requêtes envoyées depuis l'application front-end via WebSockets. Nous récupérerons ensuite une réponse de l'API de traitement du langage. Enfin, nous enverrons la réponse via WebSockets.

À l'avant, nous avons une application de type messagerie construite sur un seul composant [Angular](https://angular.io/). [Angular](https://angular.io/) est construit en [TypeScript](https://www.typescriptlang.org/) (un sur-ensemble typé de JavaScript). Si vous n'êtes pas familier avec l'un ou l'autre, vous devriez toujours être en mesure de comprendre le code.

J'ai choisi [Angular](https://angular.io/) parce qu'il utilise intrinsèquement [RxJS](http://reactivex.io/rxjs/) (la bibliothèque ReactiveX pour JavaScript). RxJS gère les flux de données asynchrones de manière incroyablement puissante et simple.

### Configuration de API.AI

API.AI dispose d'une section [Docs](https://api.ai/docs/getting-started/basics) bien organisée. Tout d'abord, nous devons nous familiariser avec certains des termes et concepts de base liés aux API, et connaître le NLU en général.

Une fois que nous avons [créé un compte](https://console.api.ai/api-client/#/login) sur API.AI, nous devons créer un [agent](https://api.ai/docs/agents) pour démarrer notre projet. Avec chaque agent, nous obtenons des clés API — des jetons d'accès client et développeur. Nous utilisons le jeton d'accès client pour accéder à l'API.

Les agents sont comme des projets ou des modules NLU. Les parties importantes d'un agent sont les [intentions](https://api.ai/docs/intents), les [entités](https://api.ai/docs/entities) et les [actions et paramètres](https://api.ai/docs/actions-and-parameters).

Les [intentions](https://api.ai/docs/intents) sont les réponses que l'API retourne ou, selon API.AI, « une correspondance entre ce qu'un utilisateur dit et l'action qui doit être entreprise par votre logiciel ». Par exemple, si un utilisateur dit : « Je veux réserver un vol », le résultat que nous recevons devrait ressembler à ce qui suit :

`{ ... "action": "book_flight" ... }`

Les [entités](https://api.ai/docs/entities) aident à extraire des données de ce que dit l'utilisateur. Si un utilisateur dit : « Je veux réserver un vol pour Paris », nous voulons obtenir les informations sur Paris. Nous avons besoin de ces données transmises à notre logique afin que nous puissions réserver un vol pour Paris pour notre utilisateur. Le résultat devrait ressembler à ceci :

```
{  ...  "action": "book_flight",   "parameters": {    "destination": "Paris"  }  ...}
```

Les entités sont des valeurs de paramètres, comme des types de données. Il existe des [entités définies par le système](https://api.ai/docs/reference/system-entities) par la plateforme API.AI. Des exemples incluent `@sys.date`, `@sys.color`, `@sys.number`. D'autres plus complexes incluent `@sys.phone-number`, `@sys.date-period`, `@sys.unit-length-name`.

Nous pouvons également définir nos propres entités, ou les transmettre à la volée avec chaque requête. Un bon exemple de transmission d'entités à la volée est celui des utilisateurs écoutant leurs playlists. Les utilisateurs ont une entité playlist dans leur requête ou une session utilisateur avec toutes les chansons de la playlist. Nous pourrions répondre à « Jouer Daydreaming » si l'utilisateur écoute actuellement la playlist _A Moon Shaped Pool_ de Radiohead.

Les actions et paramètres envoient des requêtes à l'API afin qu'elles résultent en une action. Mais elles peuvent également aboutir à quelque chose que notre chatbot ne comprend pas. Nous pouvons choisir de revenir à une réponse par défaut dans ce cas.

Les paramètres sont les compagnons des actions. Ils complètent et finalisent l'action. Dans certains cas, nous n'avons pas besoin de paramètres. Mais il y a des cas où les actions n'ont de sens qu'avec des paramètres. Un exemple est la réservation d'un vol sans connaître la destination. C'est quelque chose à quoi nous devons penser avant même de commencer à créer les intentions.

Enfin, le code suivant montre comment la réponse de l'API devrait apparaître pour une intention résolue :

La partie la plus importante du JSON est l'objet `"result"` avec les propriétés `"action"` et `"parameters"` discutées ci-dessus. La confiance pour la requête résolue (dans la plage de 0 à 1) est indiquée par `"score"`. Si `"score"` est zéro, notre requête n'a pas été comprise.

Il est intéressant de noter que le tableau `"context"` contient des informations sur les intentions non résolues qui peuvent nécessiter une réponse de suivi. Par exemple, si un utilisateur dit : « Je veux réserver un vol », nous traiterions l'action `book_flight` (le contexte). Mais pour obtenir la `"destination"` requise, nous pourrions répondre par : « Ok, où souhaitez-vous aller ? » et traiter la `"destination"` dans la requête suivante.

### Le back-end

Nous construisons une application de chat. La communication entre le client et le serveur se fera via WebSockets. À cette fin, nous utiliserons [une bibliothèque WebSocket Node.js](https://github.com/websockets/ws) sur le serveur. Notre module WebSockets ressemble à ceci :

Le format des messages WebSockets est un JSON encodé en chaîne avec les propriétés `"type"` et `"msg"`.

La chaîne `"type"` fait référence à l'une des suivantes :

`"bot"`, qui répond à l'utilisateur.

`"user"`, qui est la question de l'utilisateur au bot.

`"sessionId"`, qui émet un identifiant de session unique.

La réponse de notre chatbot est contenue dans `"msg"`. Elle est renvoyée à l'utilisateur, la question de l'utilisateur, ou le sessionId.

La méthode `processRequest(msg)` représente le cœur de la fonctionnalité de notre serveur. Elle fait d'abord une requête à l'API :

Ensuite, elle exécute `doIntent()` — l'action spécifique pour l'intention de l'utilisateur, basée sur la réponse de l'API :

`doIntent()` vérifie s'il existe une fonction pour gérer l'action dans la réponse. Elle appelle ensuite cette fonction avec les paramètres de la réponse. Si aucune fonction n'existe pour l'action, ou si la réponse n'est pas résolue, elle vérifie s'il y a une solution de repli de l'API. Ou elle appelle `handleUnknownAnswer()`.

Les gestionnaires d'actions se trouvent dans notre module d'intentions :

À chaque fonction de gestionnaire, nous passons les paramètres de la réponse de l'API. Nous passons également le fuseau horaire de l'utilisateur que nous recevons du côté client. Parce que nous traitons de la date et de l'heure, il s'avère que le fuseau horaire joue un rôle important dans notre logique. Cela n'a rien à voir avec l'API, ou le NLU en général, mais seulement avec notre logique métier spécifique.

Par exemple, si un utilisateur à Londres, le vendredi à 20h50, demande à notre bot : « Quel jour sommes-nous aujourd'hui ? », la réponse devrait être : « Nous sommes vendredi. »

Mais si cet utilisateur demande : « Quel jour est-il à Sydney ? », la réponse devrait être : « À Sydney, nous sommes samedi. »

La localisation est également importante pour notre logique métier. Nous voulons détecter d'où provient la question (dans le cas de Sydney), afin que nous puissions obtenir le fuseau horaire de son emplacement. Nous combinerions l'API [Geocoding](https://developers.google.com/maps/documentation/geocoding/start) et l'API [Time Zone](https://developers.google.com/maps/documentation/timezone/start) de Google Maps pour cela.

#### Le front-end

Notre application est un seul composant Angular. La fonctionnalité la plus importante se trouve dans la méthode `ngOnInit()` du composant :

Nous créons d'abord la connexion WebSocket (WS) à notre serveur avec un Observable WS. Nous y abonnons ensuite quelques observateurs.

Le premier observateur obtient le `sessionId` lorsqu'il se connecte au serveur WebSocket. Immédiatement, l'opérateur `take(1)` se désabonne :

Le deuxième abonnement est celui qui est amusant :

```
this.ws$.takeUntil(this.ngUnsubscribe$)
  .filter(r => r.type === 'bot')
  .retryWhen(err$ =>
    Observable.zip(err$, Observable.range(1, 3), (e, n) => n)
      .mergeMap(retryCount => Observable.timer(1000 * retryCount))
  )
  .delayWhen(inp => Observable.interval(100 + inp.msg.length * 10))
  .subscribe(
    (msg) => this.pushMsg(msg)
  );
```

Ici, nous voulons extraire uniquement les messages du bot, d'où l'opérateur `filter(r => r.type === 'bot')`. L'opérateur `retryWhen(err$ => ...)` se reconnecte automatiquement au WebSocket après une déconnexion.

Le but de l'opérateur `delayWhen()` est d'obtenir l'effet « le bot est en train d'écrire » que les messageries utilisent. Pour ce faire, nous retardons les données de `100 + MSG_CHARACTERS_LENGTH * 10` millisecondes.

Lorsque le message passe par tous les opérateurs, nous le poussons dans notre tableau de messages `(msg) => this.pushMsg(msg)`.

Nous utilisons la méthode privée `pushMsg()` du composant pour ajouter un message et l'afficher dans le chat :

Si le message provient de l'utilisateur (le drapeau `clearUserMsg`), nous effaçons la boîte d'entrée. Nous utilisons `this.botIsTyping` pour contrôler l'effet « le bot est en train d'écrire ». Nous le définissons donc sur `false`.

Nous gérons l'entrée de l'utilisateur avec la méthode `onSubmit()` lorsque l'utilisateur appuie sur Entrée :

Avec le message de l'utilisateur, nous envoyons le sessionId de l'utilisateur et son fuseau horaire. Ceux-ci sont indiqués dans `this.ws$.next(JSON.stringify(input))`. Pour montrer l'effet « le bot est en train d'écrire », nous définissons également `this.botIsTyping` sur `true`.

Le modèle de composant Angular que nous utilisons comme interface utilisateur de notre application se compose du code suivant :

C'est tout ce dont nous avons besoin pour notre application côté front-end.

C'est incroyable de voir à quel point ce code est élégant et propre. Grâce à RxJS. Lorsque l'on utilise WebSockets, les choses ont tendance à se compliquer. Ici, nous l'avons fait avec une seule ligne de code.

Et avoir des fonctionnalités comme la reconnexion automatique — eh bien, c'est une histoire à part entière. Mais avec RxJS, nous avons géré cela de manière simple.

En conclusion, j'espère que vous comprenez pourquoi j'ai dit : « Cela ne prend pas beaucoup » pour répondre à la question : « Qu'est-ce qu'il faut pour construire un chatbot ? »

Cela ne signifie pas que construire un chatbot est une tâche facile. Ces services NLU, aussi intelligents soient-ils, ne résoudront pas tous nos problèmes. Nous devons toujours prendre soin de notre propre logique métier.

Il y a quelques années, il m'était impossible de construire quelque chose de similaire. Mais des services comme API.AI rendent désormais ce pouvoir accessible à tous.

API.AI propose également des intégrations avec Facebook Messenger, Twitter, Viber et Slack. Mais pour cet article, j'ai pensé qu'il serait préférable d'utiliser leur API pour mieux comprendre comment tout fonctionne.

J'espère que vous avez apprécié cet article et que vous le trouverez utile pour construire votre propre chatbot.