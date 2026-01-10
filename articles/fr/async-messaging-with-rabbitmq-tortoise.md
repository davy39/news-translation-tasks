---
title: Messagerie asynchrone avec RabbitMQ et Tortoise en Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T01:04:00.000Z'
originalURL: https://freecodecamp.org/news/async-messaging-with-rabbitmq-tortoise
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cd7740569d1a4ca3478.jpg
tags:
- name: messaging
  slug: messaging
- name: Node.js
  slug: nodejs
- name: toothbrush
  slug: toothbrush
seo_title: Messagerie asynchrone avec RabbitMQ et Tortoise en Node.js
seo_desc: "RabbitMQ happens to be the easiest and most performant message broker platform\
  \ using the AMQ protocol out there today. Using it in a microservice architecture\
  \ translates into massive performance gains, as well as the promise of reliability.\
  \ \nIn this ..."
---

RabbitMQ est actuellement la plateforme de courtage de messages la plus facile et la plus performante utilisant le protocole AMQ. Son utilisation dans une architecture de microservices se traduit par des gains de performance massifs, ainsi que par la promesse de fiabilité. 

Dans ce guide, nous allons explorer les bases de l'utilisation de RabbitMQ avec Node.js.

## **Théorie**

À son niveau le plus basique, vous auriez idéalement deux services différents interagissant l'un avec l'autre via Rabbit - un _publisher_ et un _subscriber_. 

Un publisher envoie généralement des messages à Rabbit, et un subscriber écoute ces messages et exécute du code sur la base de ces messages. 

Notez qu'ils peuvent être les deux à la fois - un service peut publier des messages vers Rabbit et consommer des messages en même temps, ce qui permet de concevoir des systèmes vraiment puissants.

Maintenant, un publisher publie généralement des messages avec une _routing key_ vers ce qu'on appelle un _exchange_. Un consumer écoute une _queue_ sur le même exchange, liée à la routing key. 

En termes architecturaux, votre plateforme utiliserait un exchange Rabbit, et différents types de jobs/services auraient leurs propres routing keys et queues, afin que le pub-sub fonctionne efficacement. 

Les messages peuvent être des chaînes de caractères ; ils peuvent également être des objets natifs - les bibliothèques clientes AMQP font le travail lourd de conversion des objets d'une langue à une autre. Et oui, cela signifie que les services peuvent être écrits dans des langues différentes, tant qu'ils sont capables de comprendre AMQP.

## **Prise en main**

Nous allons créer un exemple très simple où un script publisher publie un message vers Rabbit, contenant une URL, et un script consumer écoute Rabbit, prend l'URL publiée, l'appelle et affiche les résultats. Vous pouvez trouver l'exemple terminé sur [Github](https://github.com/rudimk/freecodecamp-guides-rabbitmq-tortoise).

Tout d'abord, initialisons un projet npm :

`$ npm init`

Vous pouvez toujours simplement appuyer sur `Entrée` tout du long et utiliser les options par défaut - ou vous pouvez les remplir. 

Maintenant, installons les packages dont nous avons besoin. Nous allons utiliser [Tortoise](https://www.npmjs.com/package/tortoise) pour interagir avec RabbitMQ. Nous allons également utiliser [node-cron](https://www.npmjs.com/package/node-cron) pour planifier la publication réelle des messages.

`$ npm install --save tortoise node-cron`

Maintenant, votre `package.json` devrait ressembler à ceci :

```text
{
  "name": "freecodecamp-guides-rabbitmq-tortoise",
  "version": "1.0.0",
  "description": "Code d'exemple pour accompagner le guide FreeCodeCamp sur la messagerie asynchrone avec RabbitMQ et Tortoise.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/rudimk/freecodecamp-guides-rabbitmq-tortoise.git"
  },
  "keywords": [
    "rabbitmq",
    "tortoise",
    "amqp"
  ],
  "author": "Rudraksh M.K.",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/rudimk/freecodecamp-guides-rabbitmq-tortoise/issues"
  },
  "homepage": "https://github.com/rudimk/freecodecamp-guides-rabbitmq-tortoise#readme",
  "dependencies": {
    "node-cron": "^1.2.1",
    "tortoise": "^1.0.1"
  }
}
```

Maintenant, nous sommes prêts. Créons d'abord un publisher.

```javascript
const Tortoise = require('tortoise')
const cron = require('node-cron')

const tortoise = new Tortoise(`amqp://rudimk:YouKnowWhat@$localhost:5672`)
```

Après avoir importé `tortoise` et `node-cron`, nous avons initialisé une connexion à RabbitMQ. Ensuite, écrivons une fonction rapide et simple qui publie un message vers Rabbit :

```javascript
function scheduleMessage(){
    let payload = {url: 'https://randomuser.me/api'}
    tortoise
    .exchange('random-user-exchange', 'direct', { durable:false })
    .publish('random-user-key', payload)
}
```

C'est assez simple. Nous avons défini un dictionnaire contenant une URL vers l'API [RandomUser.me](https://randomuser.me/), qui est ensuite publiée sur l'échange `random-user-exchange` de RabbitMQ, avec la clé de routage `random-user-key`. 

Comme mentionné précédemment, la clé de routage est ce qui détermine qui peut consommer un message. Maintenant, écrivons une règle de planification, pour publier ce message toutes les 60 secondes.

```javascript
cron.schedule('60 * * * * *', scheduleMessage)
```

Et notre publisher est prêt ! Mais il n'est vraiment pas bon sans un consumer pour consommer ces messages ! Mais d'abord, nous avons besoin d'une bibliothèque qui peut appeler l'URL dans ces messages. Personnellement, j'utilise `superagent` : `npm install --save superagent`.

Maintenant, dans `consumer.js` :

```javascript
const Tortoise = require('tortoise')
const superagent = require('superagent')

const tortoise = new Tortoise(`amqp://rudimk:YouKnowWhat@$localhost:5672`)
```

Ensuite, écrivons une fonction asynchrone qui appelle une URL et affiche le résultat :

```javascript
async function getURL(url){
	let response = await superagent.get(url)
	return response.body
}
```

Il est temps d'écrire du code pour consommer réellement les messages :

```javascript
tortoise
.queue('random-user-queue', { durable: false })
// Ajoutez autant de bindings que nécessaire 
.exchange('random-user-exchange', 'direct', 'random-user-key', { durable: false })
.prefetch(1)
.subscribe(function(msg, ack, nack) {
  // Gérer 
  let payload = JSON.parse(msg)
  getURL(payload['url']).then((response) => {
    console.log('Résultat du job : ', response)
  })
  ack() // ou nack()
})
```

Ici, nous avons dit à `tortoise` d'écouter la `random-user-queue`, qui est liée à la `random-user-key` sur le `random-user-exchange`. Une fois qu'un message est reçu, la charge utile est récupérée à partir de `msg`, et est transmise à la fonction `getURL`, qui à son tour retourne une promesse avec la réponse JSON souhaitée de l'API RandomUser.

## **Conclusion**

La simplicité associée à l'utilisation de RabbitMQ pour la messagerie est sans pareille, et il est très facile de créer des modèles de microservices vraiment complexes avec seulement quelques lignes de code. 

Le meilleur aspect est que la logique derrière la messagerie ne change pas vraiment d'une langue à l'autre - Crystal, Go, Python ou Ruby fonctionnent avec Rabbit de manière pratiquement identique. Cela signifie que vous pouvez avoir des services écrits dans des langues différentes communiquant les uns avec les autres sans effort, vous permettant d'utiliser la meilleure langue pour le travail.