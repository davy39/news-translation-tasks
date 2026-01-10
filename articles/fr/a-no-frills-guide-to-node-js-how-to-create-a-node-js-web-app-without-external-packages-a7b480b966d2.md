---
title: Comment créer une application web Node.js sans utiliser de packages externes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T18:19:08.000Z'
originalURL: https://freecodecamp.org/news/a-no-frills-guide-to-node-js-how-to-create-a-node-js-web-app-without-external-packages-a7b480b966d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1nHHJF4266PNeWGkgBdIlg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une application web Node.js sans utiliser de packages externes
seo_desc: 'By Abhinav Pandey

  No frameworks, no NPM, no Package.json, no frills

  In this post, we will dive deep inside Node.js fundamentals by creating a Node.js
  web app without any external packages. We will cover core concepts like streams,
  events, exceptions,...'
---

Par Abhinav Pandey

#### Pas de frameworks, pas de NPM, pas de Package.json, pas de fioritures

Dans cet article, nous allons **plonger au cœur des fondamentaux de Node.js** en créant une application web Node.js sans aucun package externe. Nous aborderons des concepts clés comme **les streams, les événements, les exceptions, HTTP**, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1nHHJF4266PNeWGkgBdIlg.jpeg)
_Un regard sur les fondamentaux de Node.js_

Actuellement, lorsque nous disons que nous allons implémenter un service en Node.js, la plupart du temps, nous utilisons Express ou d'autres bibliothèques tierces pour implémenter notre fonctionnalité. Et je ne vais pas dire qu'il y a un mal à faire cela. Ces bibliothèques fournissent une abstraction nécessaire sur des concepts redondants qui nous rendent efficaces.

Mais avec une abstraction plus grande, la logique de bas niveau de votre programme est cachée. En conséquence, nous ne sommes pas en mesure de développer une image claire de la manière dont notre logique métier interagit avec Node.js.

Mais comme l'a dit Ryan Dahl, le créateur de Node.js :

> Vous ne pouvez jamais tout comprendre. Mais vous devriez vous pousser à comprendre le système.

Nous allons nous pousser à former cette image claire dans son intégralité.

Alors, créons une application HTTP brute Node.js sans Framework, sans NPM et sans Package.json.

Nous allons créer une application qui va :

1. **Importer** les **modules** nécessaires
2. Créer une **instance de serveur**
3. **Attacher des écouteurs** à l'événement `**request**` de l'objet serveur
4. **Analyser le corps de la requête** et les **en-têtes**
5. **Envoyer une réponse** au client.
6. **Gérer les événements d'erreur** au niveau des streams de requête et de réponse.

**Mais voici le piège ;)**

Nous allons tout faire à partir de zéro avec juste

1. **un terminal**, et
2. un **éditeur**.

Oui !! Nous n'utiliserons **le framework de personne d'autre**, **les bibliothèques de personne d'autre**, juste **JavaScript brut** et le **runtime core de Node.js**.

**Commençons !**

Avant de créer un serveur HTTP, clarifions le concept nécessaire d'un module HTTP dans Node.js.

**Qu'est-ce que HTTP ?**

`http` dans Node.js est un module intégré qui permet la communication client-serveur via le protocole HTTP. Ce module fournit une interface pour créer soit un client HTTP, soit un serveur HTTP qui peut communiquer avec d'autres serveurs ou clients HTTP.

Et pour rendre cet espace de communication efficace, un module `http` fournit un **streaming** de données en utilisant l'interface de stream. Et puisque le stream transmet les données par morceaux, cela signifie que Node.js ne met jamais en mémoire tampon l'intégralité de la requête ou de la réponse en une seule fois. Nous aborderons bientôt les **streams**.

**Donc pour notre application, nous utiliserons cette interface `http` pour créer un serveur HTTP qui écoutera sur un port particulier et renverra des données à l'utilisateur.**

#### Importation du module HTTP

Pour utiliser soit le serveur `http`, soit le client, vous devez requérir le module `http`.

```
var http = require("http");
```

Voyons maintenant comment la ligne ci-dessus fonctionne réellement :

Pour charger une instance d'un module particulier dans notre runtime, Node.js nous fournit une variable `require` qui est accessible globalement. Nous utilisons cette variable `require` définie globalement et demandons à Node de charger le module `http` (en passant `'http'` comme seul paramètre à l'appel de la fonction `require`).

Il existe une liste d'autres objets Node.js disponibles globalement que vous pouvez consulter dans le REPL de Node (en appuyant sur <tab> deux fois).

![Image](https://cdn-media-1.freecodecamp.org/images/1*uVs_C_0FzEFexj3hzZjBqQ.png)
_Variables **Node.js** et **JavaScript** définies globalement_

**Mais les 2 plus importantes pour notre utilisation sont :**

1. Le module **require**
2. Le **module** (explication approfondie dans le prochain article)

(Nous n'avons pas besoin de `require('require')` ou `require('module')` car ils sont globaux).

**Comment fonctionne `require` ?**

Au runtime, lorsque Node.js invoque un appel `require` (require('./path/to/fileName'), il recherche un fichier avec un nom identique à celui fourni dans le seul paramètre de l'appel de la fonction require.

Et une fois que le nom du fichier correspond, Node.js vérifie 3 types d'extensions :

1. `.js` — Node.js recherche "fileName.js" au chemin spécifié pour le charger en tant que script js.
2. `.json` — Si Node.js trouve un fichier "filename.json" au chemin spécifié, il charge un fichier avec le nom correspondant à la valeur de la clé 'main' dans le fichier JSON.
3. `.node` — Node.js charge des addons binaires avec le nom fileName.node au chemin spécifié.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OCwhzxQ8FYvdX82Okd3t-Q.png)
_**Les extensions sont chargées dans l'ordre .js > .json > .node.**_

#### Créer une **instance de serveur**

Maintenant que nous avons inclus le module `http`, nous devons créer un objet serveur web HTTP. Cela peut être fait en utilisant la méthode `createServer` sur le module `http`.

À la méthode `createServer`, nous passons une fonction de rappel qui est appelée chaque fois qu'une requête est reçue sur le serveur.

Cette méthode `createServer` retourne un objet serveur que nous stockons dans la variable `app`. Cet objet serveur est un émetteur d'événements.

**Attendez, qu'est-ce qu'un `event emitter` ?**

Regardons un peu les objets nommés `event` et `emitter`.

Une grande partie des API core de Node.js sont construites autour d'une architecture pilotée par les événements. Certains types d'objets (appelés "émetteurs") peuvent faire en sorte que certaines fonctions ("écouteurs") soient appelées en émettant des événements "nommés".

Regardons un exemple pour nous familiariser avec cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_06ekq-7fkdO8I9eh3vCWg.png)

Sortie : `Called namedEvent in myEventObject's attached listener`

**Explication**

Dans l'exemple ci-dessus, nous avons vu que `namedEvent` a un écouteur (une fonction) attaché à lui. Par attaché, nous entendons que l'écouteur est appelé après avoir entendu l'événement nommé. Ainsi, l'écouteur imprime la sortie sur l'écran de la console lorsque l'objet émetteur émet `namedEvent`.

Outre l'attachement des écouteurs, l'objet `eventEmitter` fournit de nombreuses autres propriétés et fonctions telles que

* vous pouvez obtenir le nombre total d'écouteurs attachés à un événement nommé, ou
* vous pouvez également supprimer un écouteur attaché aux événements.

Vous pouvez vous référer à la [**documentation officielle de Node.js**](https://nodejs.org/api/events.html#events_eventemitter_defaultmaxlisteners) pour plus d'informations détaillées sur les événements dans Node.js.

**Revenons à notre exemple...**

Notre objet serveur web est également comme tous les autres objets émetteurs implémentant des interfaces d'émetteurs d'événements. Il émet également différents types d'événements nommés.

Certains d'entre eux sont les suivants :

1. `connect` — déclenché pour toutes les requêtes 'connect' par le client HTTP.
2. `connection` — Émis lorsqu'un nouveau flux TCP est établi. Fournit l'accès à la socket établie.
3. `request` — Émis pour chaque requête du client (nous écouterons ici).
4. `upgrade` — émis chaque fois qu'un client demande une mise à niveau du protocole (peut être la version HTTP).

Vous pouvez obtenir la liste complète des événements émis par notre serveur web à partir de la [documentation officielle de Node.js](https://nodejs.org/api/http.html#http_class_http_server).

#### Écouter l'événement de requête

Maintenant, puisque notre serveur doit écouter les requêtes entrantes, nous allons écouter l'événement `request` de notre serveur HTTP.

Exemple de code :

Dans la 3ème ligne, une fonction d'écoute est attachée pour écouter tous les événements `**request**` sur notre objet serveur.

L'événement `request` fournit à la fonction d'écoute 2 paramètres qui sont :

1. **request** — une instance de l'objet http.incomingMessage et
2. **response** — une instance de l'objet http.ServerResponse.

Ces objets `request` et `response` ont des propriétés et des méthodes qu'ils héritent des classes `http.incomingMessage` et `http.ServerResponse`, respectivement.

#### **Analyser le corps de la requête** et les **en-têtes**

Maintenant que nous avons accès aux objets `request` et `response`...

Les premières choses que vous pourriez vouloir savoir sur les requêtes entrantes sont l'**URL, la méthode et les en-têtes**. Node.js rend cela très facile en **les attachant en tant que propriétés** à l'objet `request` (passé en tant que premier paramètre pour l'écouteur de l'événement `request`).

Vous pouvez déstructurer l'objet request pour les obtenir comme ceci :

`const {headers, url, method } = request;`

Les `headers` passés dans la requête sont présents en tant qu'objet indépendant à l'intérieur de l'objet `request` (secret : ils sont tous en minuscules).

Après avoir examiné la méthode `http`, dans le cas d'une requête PUT ou POST, nous sommes intéressés par les `data` envoyées dans le corps de la requête.

Mais pour extraire les données du corps de la requête, nous devons connaître quelques points clés sur l'objet request.

**Objet Request — un stream lisible**

L'objet `request` qui est passé dans le gestionnaire implémente également l'interface de stream lisible. Cela signifie que notre objet `request` est un stream qui peut être **écouté** ou **redirigé** ailleurs pour récupérer les données qui y circulent. Nous allons également récupérer les données directement à partir du stream `request` en écoutant les événements `data` et `end` du stream.

Différents types de données peuvent être passés à notre serveur, mais pour garder cela simple, nous allons passer uniquement la chaîne dans le corps.

Pour utiliser ces données, nous devons les **analyser**, nous allons donc utiliser les événements `data` et `end` du stream lisible qui est implémenté par notre objet `request` comme mentionné précédemment.

À chaque événement `data`, le **stream lisible transmet les données sous forme de chunk de buffer**. Nous allons ajouter tous les chunks dans un tableau vide. Et à l'événement `end`, nous allons **concaténer et convertir le tableau en chaîne** pour obtenir le corps cumulatif.

Voici donc le code jusqu'à présent :

#### **Envoyer la réponse au client.**

Après avoir collecté les données de la requête HTTP, nous devons donner une réponse appropriée au client. Mais puisque l'objet `request` implémente uniquement un stream lisible, **nous avons besoin d'un stream inscriptible où nous pouvons écrire notre réponse.**

**Objet Response — un stream inscriptible**

Pour ce faire, Node.js nous fournit un deuxième paramètre qui est l'objet `response` pour l'écouteur d'événements `request`.

En utilisant l'objet `response`, nous pouvons définir le code d'état HTTP, définir les en-têtes et écrire du contenu dans le stream d'écriture de l'objet response.

Bien que si vous ne définissez pas explicitement le code de réponse, Node.js lui-même le définit à 200. Mais à mesure que la complexité augmente, vous voudrez définir le `statusCode` souhaité de la réponse HTTP.

**Définition implicite des en-têtes**

Vous pouvez **définir, obtenir** et **supprimer** les en-têtes de la réponse en utilisant `setHeader(name, value)`, `getHeader(name)` et `removeHeader(name)` API.

Exemple de code :

Lorsque vous utilisez la méthode `setHeader()` ci-dessus pour définir les en-têtes, nous dépendons de Node.js pour **définir implicitement** les en-têtes de réponse avant d'envoyer le corps de la réponse.

Pour **définir les en-têtes** et le code d'état **explicitement**, nous avons une méthode `response.writeHead()`.

Exemple de code :

Lors de la définition explicite des en-têtes, nous devons garder à l'esprit que **les en-têtes viennent avant le corps dans la réponse HTTP**. C'est-à-dire que nous devons préférer utiliser la méthode `writeHead()` avant d'écrire quoi que ce soit dans le corps de la réponse.

**Voyons maintenant comment nous pouvons écrire des données dans une réponse.**

Puisque l'objet response est un objet stream inscriptible, nous devons simplement utiliser les méthodes **write stream** pour écrire des chunks de données dans l'objet de réponse HTTP.

Exemple de code :

Après avoir écrit dans le stream de réponse, nous devons **fermer le stream** afin que Node.js sache qu'il est temps d'envoyer la réponse au client.

La méthode `.end()` nous permet de **fermer** la **connexion HTTP** qui a été établie au moment où la requête a atteint notre serveur. La méthode `end()` accepte également une dernière chaîne à écrire avant de fermer la connexion.

**Si nous n'utilisons pas la méthode end, Node.js écrira des données dans le stream d'écriture et attendra...**

...jusqu'à ce que le **timeout par défaut dans l'objet serveur expire**. C'est-à-dire que pour toute requête, **Node.js n'attend qu'un temps fixe** (qui est spécifié dans l'objet serveur) **avant de fermer la connexion**. Et une fois la connexion fermée (soit manuellement avec `end()`, soit lorsque le timeout expire), **Node libère immédiatement toutes les ressources allouées**.

Vous pouvez définir ou modifier le timeout en utilisant `server.setTimeout([msecs][, callback])`.

Pour désactiver le timeout, vous pouvez définir la valeur du timeout à 0. Mais comme le timeout est attribué au moment de la formation d'une nouvelle connexion, le **timeout ne sera mis à jour que pour les nouvelles connexions à venir**.

Maintenant que nous avons écrit notre réponse, notre serveur devrait fonctionner correctement.

#### Mais, que se passera-t-il lorsque notre serveur rencontrera une exception ?

Nous devons écouter les événements `error` des streams `request` et `response`. Un événement `error` est déclenché chaque fois qu'une exception se produit. Vous pouvez essayer de l'éviter, mais elles arrivent et nous devons les attraper et les gérer correctement.

**Mais comment ?**

Nous allons les gérer **en attachant des gestionnaires d'erreurs** aux événements `error` des streams `request` et `response`.

**Explication**

Ici, nous attrapons tous les événements `error` des streams `request` et `response` et nous les enregistrons simplement dans la console. Vous pouvez également utiliser `util` au lieu de la `console` dans l'environnement de production (bien qu'en production, il soit conseillé d'inspecter correctement les erreurs).

Regardons maintenant l'exemple de code que nous avons jusqu'à présent.

D'accord, donc notre serveur est capable des choses suivantes à ce stade :

1. **Importer** les **modules** nécessaires
2. créer une **instance de serveur**
3. **Attacher des écouteurs** à l'événement `**request**` de l'objet serveur
4. **Analyser le corps de la requête** et les **en-têtes**
5. **Écrire la réponse** dans le stream de réponse
6. **Gérer les événements d'erreur** au niveau des streams de requête et de réponse.

Jusqu'à présent, nous avons rendu notre objet serveur capable de prendre en charge de nouvelles connexions, mais nous ne lui avons pas dit où écouter les nouvelles connexions. C'est-à-dire que cet objet serveur doit également être lié à un port particulier afin que notre serveur puisse avoir accès à toutes les requêtes entrantes sur ce port.

Pour ce faire, nous allons utiliser la méthode `.listen` de notre objet serveur HTTP, `.listen(PORT, CB).`

@params PORT est le numéro de port où nous voulons que notre serveur écoute.

@params Callback est appelé une fois que le serveur commence à écouter.

Exemple de code :

À ce stade, notre serveur est prêt à recevoir des requêtes.

Lançons notre application Node.js :

```
node app.js
```

Et envoyons une requête à notre serveur avec la commande curl suivante dans un terminal :

```
curl -d "Hello World" -H "Content-Type: text" -X POST http://localhost:8008
```

WooHoo !! Félicitations, vous avez créé une application Node.js sans aucun package externe.

C'est merveilleusement applaudissable que vous soyez resté aussi longtemps.

Si vous êtes prêt à en apprendre davantage sur le cœur de Node.js comme cela, faites-le moi savoir en faisant exploser le compteur d'applaudissements à 50.

Dans les prochains articles, nous continuerons à construire sur cette application de base et ajouterons d'autres fonctionnalités critiques comme **le routage, les middlewares, la gestion des erreurs**, etc. Soyez notifié en me suivant ici sur Medium.

J'ai essayé de rendre cet article aussi complet que possible. Si vous avez des idées qui pourraient l'améliorer, veuillez les mentionner dans vos commentaires précieux.

Vous pouvez me contacter via [gmail](http://abhinavpandey.1996@gmail.com) ou me tweeter [ici](https://twitter.com/Heisabhinav).

Merci beaucoup pour votre amour ! Pardonnez mes erreurs, vous avez été un public merveilleux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aYY0Czr1b6wQSftkSBsmbQ.png)
_Félicitations !_