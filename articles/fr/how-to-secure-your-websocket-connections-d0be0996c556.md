---
title: Comment sécuriser vos connexions WebSocket
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T22:09:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-websocket-connections-d0be0996c556
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OO2brLI8iR1wo8bJx7TKOg.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: websocket
  slug: websocket
seo_title: Comment sécuriser vos connexions WebSocket
seo_desc: 'By Mehul Mohan

  The Web is growing at a massive rate. More and more web apps are dynamic, immersive
  and do not require the end user to refresh. There is emerging support for low latency
  communication technologies like websockets. Websockets allow us t...'
---

Par Mehul Mohan

Le Web connaît une croissance massive. De plus en plus d'applications web sont dynamiques, immersives et ne nécessitent pas que l'utilisateur final actualise la page. Il existe un soutien émergent pour les technologies de communication à faible latence comme les websockets. Les websockets nous permettent d'atteindre une communication en temps réel parmi différents clients connectés à un serveur.

Beaucoup de personnes ignorent comment sécuriser leurs websockets contre certaines attaques très courantes. Voyons ce qu'elles sont et ce que vous devriez faire pour protéger vos websockets.

### #0: Activer CORS

WebSocket ne vient pas avec CORS intégré. Cela signifie que n'importe quel site web peut se connecter à la connexion websocket d'un autre site web et communiquer sans aucune restriction ! Je ne vais pas entrer dans les raisons pour lesquelles c'est ainsi, mais une solution rapide à cela est de vérifier l'en-tête `Origin` lors de la poignée de main websocket.

Bien sûr, l'en-tête Origin peut être falsifié par un attaquant, mais cela n'a pas d'importance, car pour l'exploiter, l'attaquant doit falsifier l'en-tête Origin sur le navigateur de la victime, et les navigateurs modernes ne permettent pas au javascript normal situé dans les navigateurs web de changer l'en-tête Origin.

De plus, si vous authentifiez réellement les utilisateurs en utilisant, de préférence, des cookies, alors ce n'est pas vraiment un problème pour vous (plus d'informations à ce sujet au point #4)

### #1: Implémenter la limitation de débit

La limitation de débit est importante. Sans elle, les clients peuvent, volontairement ou non, effectuer une attaque DoS sur votre serveur. DoS signifie Denial of Service. DoS signifie qu'un seul client occupe le serveur à un point tel que le serveur est incapable de gérer d'autres clients.

Dans la plupart des cas, il s'agit d'une tentative délibérée d'un attaquant pour faire tomber un serveur. Parfois, de mauvaises implémentations frontales peuvent également conduire à un DoS par des clients normaux.

Nous allons utiliser l'algorithme du seau perforé (qui est apparemment un algorithme très courant pour les réseaux) pour implémenter la limitation de débit sur nos websockets.

L'idée est que vous avez un seau qui a un trou de taille fixe à son fond. Vous commencez à y mettre de l'eau et l'eau s'écoule par le trou au fond. Maintenant, si votre débit de mise d'eau dans le seau est plus grand que le débit de sortie du trou pendant longtemps, à un moment donné, le seau sera plein et commencera à fuir. C'est tout.

Comprenons maintenant comment cela se rapporte à notre websocket :

1. L'eau est le trafic websocket envoyé par l'utilisateur.
2. L'eau passe par le trou. Cela signifie que le serveur a traité avec succès cette demande websocket particulière.
3. L'eau qui est encore dans le seau et qui n'a pas débordé est essentiellement du trafic en attente. Le serveur traitera ce trafic plus tard. Cela pourrait également être un flux de trafic en rafale (c'est-à-dire qu'un trafic trop important pendant un très court laps de temps est acceptable tant que le seau ne fuit pas)
4. L'eau qui déborde est le trafic rejeté par le serveur (trop de trafic provenant d'un seul utilisateur)

Le point ici est que vous devez vérifier l'activité de votre websocket et déterminer ces nombres. Vous allez attribuer un seau à chaque utilisateur. Nous décidons de la taille du seau (trafic qu'un seul utilisateur pourrait envoyer sur une période fixe) en fonction de la taille de votre trou (combien de temps en moyenne votre serveur a besoin pour traiter une seule demande websocket, par exemple sauvegarder un message envoyé par un utilisateur dans une base de données).

Voici une implémentation simplifiée que j'utilise sur [codedamn](https://codedamn.com) pour implémenter l'algorithme du seau perforé pour les websockets. Elle est en NodeJS mais le concept reste le même.

```js
if(this.limitCounter >= Socket.limit) {
  if(this.burstCounter >= Socket.burst) {
     return 'Le seau fuit'
  }
  ++this.burstCounter
  return setTimeout(() => {
  this.verify(callingMethod, ...args)
  setTimeout(_ => --this.burstCounter, Socket.burstTime)
  }, Socket.burstDelay)
}
++this.limitCounter
```

Alors, que se passe-t-il ici ? Basiquement, si la limite est dépassée ainsi que la limite de rafale (qui sont des constantes définies), la connexion websocket est interrompue. Sinon, après un certain délai, nous allons réinitialiser le compteur de rafale. Cela laisse à nouveau de l'espace pour une autre rafale.

### #2: Restreindre la taille de la charge utile

Cela devrait être implémenté comme une fonctionnalité dans votre bibliothèque websocket côté serveur. Si ce n'est pas le cas, il est temps de la changer pour une meilleure ! Vous devriez limiter la longueur maximale du message qui pourrait être envoyé via votre websocket. Théoriquement, il n'y a pas de limite. Bien sûr, recevoir une charge utile énorme est très susceptible de bloquer cette instance de socket particulière et de consommer plus de ressources système que nécessaire.

Par exemple, si vous utilisez la bibliothèque WS pour Node pour créer des websockets sur le serveur, vous pouvez utiliser l'option [maxPayload](https://github.com/websockets/ws/blob/master/doc/ws.md#new-websocketserveroptions-callback) pour spécifier la taille maximale de la charge utile en octets. Si la taille de la charge utile est plus grande que cela, la bibliothèque interrompra naturellement la connexion.

N'essayez pas d'implémenter cela vous-même en déterminant la longueur du message. Nous ne voulons pas lire le message entier dans la RAM du système en premier. Si elle est même 1 octet plus grande que notre limite définie, interrompez-la. Cela ne pourrait être implémenté que par la bibliothèque (qui gère les messages comme un flux d'octets plutôt que comme des chaînes fixes).

### #3: Créer un protocole de communication solide

Parce que vous êtes maintenant sur une connexion duplex, vous pourriez envoyer n'importe quoi au serveur. Le serveur pourrait envoyer n'importe quel texte au client. Vous aurez besoin d'une manière pour une communication efficace entre les deux.

Vous ne pouvez pas envoyer de messages bruts si vous voulez mettre à l'échelle l'aspect messagerie de votre site web. Je préfère utiliser JSON, mais il existe d'autres moyens optimisés pour établir une communication. Cependant, en considérant JSON, voici à quoi ressemblerait un schéma de messagerie de base pour un site générique :

```
Client vers Serveur (ou vice versa) : { status: "ok"|"error", event: EVENT_NAME, data: <n'importe quelle donnée arbitraire> }
```

Maintenant, il est plus facile pour vous sur le serveur de vérifier les événements valides et le format. Interrompez la connexion immédiatement et journalisez l'adresse IP de l'utilisateur si le format du message diffère. Il n'y a aucun moyen que le format change à moins que quelqu'un ne manipule manuellement votre connexion websocket. Si vous êtes sur node, je recommande d'utiliser la [bibliothèque Joi](https://github.com/hapijs/joi) pour une validation supplémentaire des données entrantes de l'utilisateur.

### #4: Authentifier les utilisateurs avant l'établissement de la connexion WS

Si vous utilisez des websockets pour des utilisateurs authentifiés, c'est une très bonne idée de ne permettre qu'aux utilisateurs authentifiés d'établir une connexion websocket réussie. Ne permettez pas à quiconque d'établir une connexion et d'attendre qu'ils s'authentifient via le websocket lui-même. Tout d'abord, établir une connexion websocket est déjà un peu coûteux. Vous ne voulez donc pas que des personnes non autorisées se connectent à vos websockets et monopolisent des connexions qui pourraient être utilisées par d'autres personnes.

Pour ce faire, lorsque vous établissez une connexion sur le frontend, passez quelques données d'authentification au websocket. Cela pourrait être un en-tête comme X-Auth-Token: <un jeton attribué à ce client lors de la connexion>. Par défaut, les cookies seraient passés de toute façon.

Encore une fois, cela dépend vraiment de la bibliothèque que vous utilisez sur le serveur pour implémenter les websockets. Mais si vous êtes sur Node et utilisez WS, il y a cette fonction [verifyClient](https://github.com/websockets/ws/blob/master/doc/ws.md#new-websocketserveroptions-callback) qui vous donne accès à l'objet info passé à une connexion websocket. (Tout comme vous avez accès à l'objet req pour les requêtes HTTP.)

### #5: Utiliser SSL sur les websockets

Cela semble évident, mais cela doit être dit. Utilisez wss:// au lieu de ws://. Cela ajoute une couche de sécurité à votre communication. Utilisez un serveur comme Nginx pour le proxy inverse des websockets et activez SSL sur eux. La configuration de Nginx serait un autre tutoriel complet. Je vais laisser la directive que vous devez utiliser pour Nginx pour ceux qui sont familiers avec. [Plus d'informations ici](http://nginx.org/en/docs/http/websocket.html).

```
location /votre-emplacement-websocket/ {
    proxy_pass \u200bhttp://127.0.0.1:1337;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
}
```

Ici, il est supposé que votre serveur websocket écoute sur le port 1337 et que vos utilisateurs se connectent à votre websocket de cette manière :

```
const ws = new WebSocket('wss://votresite.com/votre-emplacement-websocket')
```

### Questions ?

Vous avez des questions ou des suggestions ? Demandez !