---
title: Un guide pour tirer le meilleur parti de l'API Push
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-04-07T02:39:53.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-getting-the-most-out-of-the-push-api-72a139bfeb44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zhjnyEri0hw-WNu2dLLgmg.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide pour tirer le meilleur parti de l'API Push
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  The Push API allows a web app to receive messages pushed by a server, even if the
  web app is not currently open in the browser or not running on the device.

  The Push API is a recent a...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

L'API Push permet à une application web de recevoir des messages envoyés par un serveur, même si l'application web n'est pas actuellement ouverte dans le navigateur ou n'est pas en cours d'exécution sur l'appareil.

L'API Push est une addition récente aux API des navigateurs, et elle est actuellement supportée par Chrome (Desktop et Mobile), Firefox, et Opera depuis 2016.

IE et Edge ne la supportent pas encore, et Safari [a sa propre implémentation](https://developer.apple.com/notifications/safari-push-notifications/). Puisque Chrome et Firefox la supportent, environ 60 % des utilisateurs naviguant sur leur bureau y ont accès, donc il est assez sûr de l'utiliser.

### Que pouvez-vous faire avec

Vous pouvez envoyer des messages à vos utilisateurs, en les poussant depuis le serveur vers le client, même lorsque l'utilisateur ne navigue pas sur le site.

Cela vous permet de livrer des notifications et des mises à jour de contenu, vous donnant la capacité de mieux engager votre audience.

C'est énorme, car l'un des piliers manquants du web mobile, comparé aux applications natives, était la capacité de recevoir des notifications, ainsi que le support hors ligne.

### Comment cela fonctionne

Lorsque qu'un utilisateur visite votre application web, vous pouvez déclencher un panneau demandant la permission d'envoyer des mises à jour. Un [Service Worker](https://flaviocopes.com/service-workers) est installé, et fonctionne en arrière-plan à l'écoute d'un [Push Event](https://flaviocopes.com/service-workers#push-events).

> _Push et Notifications sont deux concepts et API séparés. Ils sont parfois confondus à cause du terme **push notifications** utilisé dans iOS. Basiquement, l'API Notifications est invoquée lorsqu'un événement push est reçu en utilisant l'API Push._

Votre **serveur** envoie la notification au client, et le Service Worker, si la permission est donnée, reçoit un **événement push**. Le Service Worker réagit à cet événement en **déclenchant une notification**.

### Obtenir la permission de l'utilisateur

La première étape pour travailler avec l'API Push est d'obtenir la permission de l'utilisateur pour recevoir des données de votre part.

> _De nombreux sites implémentent mal ce panneau, en le montrant dès le premier chargement de la page. L'utilisateur n'est pas encore convaincu que votre contenu est bon, et il refusera la permission. Faites-le donc judicieusement._

Il y a six étapes pour obtenir la permission de votre utilisateur :

1. Vérifier si les Service Workers sont supportés
2. Vérifier si l'API Push est supportée
3. Enregistrer un Service Worker
4. Demander la permission à l'utilisateur
5. Souscrire l'utilisateur et obtenir l'objet PushSubscription
6. Envoyer l'objet PushSubscription à votre serveur

Passons-les en revue une par une.

### Vérifier si les Service Workers sont supportés

```
if (!('serviceWorker' in navigator)) {  // Les Service Workers ne sont pas supportés. Retour  return}
```

### Vérifier si l'API Push est supportée

```
if (!('PushManager' in window)) {  // L'API Push n'est pas supportée. Retour  return}
```

### Enregistrer un Service Worker

Ce code enregistre le Service Worker situé dans le fichier `worker.js` placé à la racine du domaine :

```
window.addEventListener('load', () => {  navigator.serviceWorker.register('/worker.js')  .then((registration) => {    console.log('Enregistrement du Service Worker terminé avec la portée : ',      registration.scope)  }, (err) => {    console.log('Échec de l\'enregistrement du Service Worker', err)  })})
```

Pour en savoir plus sur le fonctionnement détaillé des Service Workers, consultez le [guide des Service Workers](https://flaviocopes.com/service-workers).

### Demander la permission à l'utilisateur

Maintenant que le Service Worker est enregistré, vous pouvez demander la permission.

L'API pour faire cela a changé au fil du temps, et elle est passée de l'acceptation d'une fonction de rappel en tant que paramètre au retour d'une [Promise](https://flaviocopes.com/javascript-promises/), rompant la compatibilité ascendante et descendante. Et notez que nous devons faire **les deux**, car nous ne savons pas quelle approche est implémentée par le navigateur de l'utilisateur.

Le code est le suivant, appelant `Notification.requestPermission()`.

```
const askPermission = () => {  return new Promise((resolve, reject) => {    const permissionResult = Notification.requestPermission(      (result) => {        resolve(result)      }    )    if (permissionResult) {      permissionResult.then(resolve, reject)    }  })  .then((permissionResult) => {    if (permissionResult !== 'granted') {      throw new Error('Permission refusée')    }  })}
```

La valeur `permissionResult` est une chaîne, qui peut avoir la valeur suivante : - `granted` - `default` - `denied`

Ce code fait en sorte que le navigateur affiche la boîte de dialogue de permission :

![Image](https://cdn-media-1.freecodecamp.org/images/S3HKfHLPj2Vg24jR3u0m0letQehHJjKwcqZ0)

**Si l'utilisateur clique sur Bloquer, vous ne pourrez plus demander la permission de l'utilisateur**, à moins qu'il ne se rende manuellement dans les paramètres avancés du navigateur pour débloquer le site (très peu probable).

Si l'utilisateur nous a donné la permission, nous pouvons le souscrire en appelant `registration.pushManager.subscribe()`.

```
const APP_SERVER_KEY = 'XXX'window.addEventListener('load', () => {  navigator.serviceWorker.register('/worker.js')  .then((registration) => {    askPermission().then(() => {      const options = {        userVisibleOnly: true,        applicationServerKey: urlBase64ToUint8Array(APP_SERVER_KEY)      }      return registration.pushManager.subscribe(options)    }).then((pushSubscription) => {      // nous avons obtenu l'objet pushSubscription    }  }, (err) => {    console.log('Échec de l\'enregistrement du Service Worker', err)  })})
```

`APP_SERVER_KEY` est une chaîne — appelée _Application Server Key_ ou _VAPID key_ — qui identifie la clé publique de l'application, faisant partie d'une paire de clés publique/privée.

Elle sera utilisée dans le cadre de la validation qui, pour des raisons de sécurité, permet de s'assurer que vous (et uniquement vous, et non quelqu'un d'autre) pouvez envoyer un message push à l'utilisateur.

### Envoyer l'objet PushSubscription à votre serveur

Dans l'extrait précédent, nous avons obtenu l'objet `pushSubscription`, qui contient tout ce dont nous avons besoin pour envoyer un message push à l'utilisateur. Nous devons envoyer ces informations à notre serveur afin de pouvoir envoyer des notifications plus tard.

Nous créons d'abord une représentation JSON de l'objet

```
const subscription = JSON.stringify(pushSubscription)
```

et nous pouvons l'envoyer à notre serveur en utilisant l'[API Fetch](https://flaviocopes.com/fetch-api) :

```
const sendToServer = (subscription) => {  return fetch('/api/subscription', {    method: 'POST',    headers: {      'Content-Type': 'application/json'    },    body: JSON.stringify(subscription)  })  .then((res) => {    if (!res.ok) {      throw new Error('Une erreur est survenue')    }    return res.json()  })  .then((resData) => {    if (!(resData.data && resData.data.success)) {      throw new Error('Une erreur est survenue')    }  })}sendToServer(subscription)
```

Côté serveur, le point de terminaison `/api/subscription` reçoit la requête POST et peut stocker les informations de souscription dans son stockage.

### Comment fonctionne le côté serveur

Jusqu'à présent, nous n'avons parlé que de la partie côté client : obtenir la permission d'un utilisateur pour être notifié à l'avenir.

Et le serveur ? Que doit-il faire, et comment doit-il interagir avec le client ?

> _Ces exemples côté serveur utilisent [Express.js](http://expressjs.com/) comme framework HTTP de base, mais vous pouvez écrire un gestionnaire d'API Push côté serveur dans n'importe quel langage ou framework_

### Enregistrer une nouvelle souscription client

Lorsque le client envoie une nouvelle souscription, rappelez-vous que nous avons utilisé le point de terminaison HTTP POST `/api/subscription`, envoyant les détails de l'objet PushSubscription au format JSON, dans le corps.

Nous initialisons Express.js :

```
const express = require('express')const app = express()
```

Cette fonction utilitaire s'assure que la requête est valide et a un corps et une propriété de point de terminaison, sinon elle retourne une erreur au client :

```
const isValidSaveRequest = (req, res) => {  if (!req.body || !req.body.endpoint) {    res.status(400)    res.setHeader('Content-Type', 'application/json')    res.send(JSON.stringify({      error: {        id: 'no-endpoint',        message: 'La souscription doit avoir un point de terminaison'      }    }))    return false  }  return true}
```

La fonction utilitaire suivante sauvegarde la souscription dans la base de données, retournant une promesse résolue lorsque l'insertion est terminée (ou a échoué). La fonction `insertToDatabase` est un espace réservé — nous n'entrons pas dans ces détails ici :

```
const saveSubscriptionToDatabase = (subscription) => {  return new Promise((resolve, reject) => {    insertToDatabase(subscription, (err, id) => {      if (err) {        reject(err)        return      }      resolve(id)    })  })}
```

Nous utilisons ces fonctions dans le gestionnaire de requêtes POST ci-dessous. Nous vérifions si la requête est valide, puis nous sauvegardons la requête et retournons une réponse `data.success: true` au client, ou une erreur :

```
app.post('/api/subscription', (req, res) => {  if (!isValidSaveRequest(req, res)) {    return  }  saveSubscriptionToDatabase(req, res.body)  .then((subscriptionId) => {    res.setHeader('Content-Type', 'application/json')    res.send(JSON.stringify({ data: { success: true } }))  })  .catch((err) => {    res.status(500)    res.setHeader('Content-Type', 'application/json')    res.send(JSON.stringify({      error: {        id: 'unable-to-save-subscription',        message: 'Souscription reçue mais échec de la sauvegarde'      }    }))  })})app.listen(3000, () => {  console.log('App listening on port 3000')})
```

### Envoyer un message Push

Maintenant que le serveur a enregistré le client dans sa liste, nous pouvons lui envoyer des messages Push. Voyons comment cela fonctionne en créant un exemple de code qui récupère toutes les souscriptions et envoie un message Push à toutes en même temps.

Nous utilisons une bibliothèque car le [**protocole Web Push**](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol) est complexe, et une bibliothèque nous permet d'abstraire beaucoup de code de bas niveau qui garantit que nous pouvons travailler en toute sécurité et gérer correctement tous les cas particuliers.

> _Cet exemple utilise la bibliothèque `web-push` [Node.js](https://flaviocopes.com/nodejs/) [library](https://github.com/web-push-libs/web-push) pour gérer l'envoi du message Push._

Nous initialisons d'abord la bibliothèque `web-push`, et nous générons un couple de clés privée et publique, et nous les définissons comme les détails VAPID :

```
const webpush = require('web-push')const vapidKeys = webpush.generateVAPIDKeys()const PUBLIC_KEY = 'XXX'const PRIVATE_KEY = 'YYY'const vapidKeys = {  publicKey: PUBLIC_KEY,  privateKey: PRIVATE_KEY}webpush.setVapidDetails(  'mailto:my@email.com',  vapidKeys.publicKey,  vapidKeys.privateKey)
```

Ensuite, nous configurons une méthode `triggerPush()`, responsable de l'envoi de l'événement push à un client. Elle appelle simplement `webpush.sendNotification()` et capture toute erreur. Si le code d'état HTTP de l'erreur retournée est [410](https://developer.mozilla.org/docs/Web/HTTP/Status/410), ce qui signifie **disparu**, nous supprimons cet abonné de la base de données.

```
const triggerPush = (subscription, dataToSend) => {  return webpush.sendNotification(subscription, dataToSend)  .catch((err) => {    if (err.statusCode === 410) {      return deleteSubscriptionFromDatabase(subscription._id)    } else {      console.log('La souscription n\'est plus valide : ', err)    }  })}
```

Nous n'implémentons pas la récupération des souscriptions depuis la base de données, mais nous le laissons comme un stub :

```
const getSubscriptionsFromDatabase = () => {  //stub}
```

Le cœur du code est le rappel de la requête POST au point de terminaison `/api/push` :

```
app.post('/api/push', (req, res) => {  return getSubscriptionsFromDatabase()  .then((subscriptions) => {    let promiseChain = Promise.resolve()    for (let i = 0; i < subscriptions.length; i++) {      const subscription = subscriptions[i]      promiseChain = promiseChain.then(() => {        return triggerPush(subscription, dataToSend)      })    }    return promiseChain  })  .then(() => {    res.setHeader('Content-Type', 'application/json')    res.send(JSON.stringify({ data: { success: true } }))  })  .catch((err) => {    res.status(500)    res.setHeader('Content-Type', 'application/json')    res.send(JSON.stringify({      error: {        id: 'unable-to-send-messages',        message: `Échec de l\'envoi du push ${err.message}`      }    }))  })})
```

Le code ci-dessus récupère toutes les souscriptions de la base de données, puis itère sur elles, et appelle la fonction `triggerPush()` que nous avons expliquée précédemment.

Une fois les souscriptions terminées, nous retournons une réponse JSON réussie. Sauf si une erreur s'est produite, et alors nous retournons une erreur 500.

### Dans le monde réel...

Il est peu probable que vous configuriez votre propre serveur Push à moins d'avoir un cas d'utilisation très spécial, ou que vous souhaitiez simplement apprendre la technologie ou que vous aimiez le DIY.

Au lieu de cela, vous voudrez généralement utiliser des plateformes telles que [OneSignal](https://onesignal.com) qui gèrent de manière transparente les événements Push pour tous types de plateformes, y compris Safari et iOS, gratuitement.

### Recevoir un événement Push

Lorsque qu'un événement Push est envoyé depuis le serveur, comment le client le reçoit-il ?

C'est un écouteur d'événements JavaScript normal, sur l'événement `push`, qui s'exécute à l'intérieur d'un Service Worker :

```
self.addEventListener('push', (event) => {  // les données sont disponibles dans event.data})
```

`event.data` contient l'objet `[PushMessageData](https://developer.mozilla.org/docs/Web/API/PushMessageData)` qui expose des méthodes pour récupérer les données push envoyées par le serveur, dans le format que vous souhaitez :

* **arrayBuffer()** : en tant qu'objet ArrayBuffer
* **blob()** : en tant qu'objet Blob
* **json()** : analysé en JSON
* **text()** : texte brut

Vous utiliserez normalement `event.data.json()`.

### Afficher une notification

Ici, nous intersectons un peu avec l'[API Notifications](https://flaviocopes.com/notifications-api), mais pour une bonne raison, car l'un des principaux cas d'utilisation de l'API Push est d'afficher des notifications.

À l'intérieur de notre écouteur d'événements `push` dans le Service Worker, nous devons afficher la notification à l'utilisateur. Nous devons également indiquer à l'événement d'attendre que le navigateur l'ait affichée avant que la fonction ne puisse se terminer. Nous prolongeons la durée de vie de l'événement jusqu'à ce que le navigateur ait fini d'afficher la notification (jusqu'à ce que la promesse ait été résolue), sinon le Service Worker pourrait être arrêté au milieu de votre traitement :

```
self.addEventListener('push', (event) => {  const promiseChain = self.registration.showNotification('Hey!')  event.waitUntil(promiseChain)})
```

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)