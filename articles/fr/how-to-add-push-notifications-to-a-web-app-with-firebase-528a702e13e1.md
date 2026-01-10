---
title: Comment ajouter des notifications push à une application web avec Firebase
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-04T16:03:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-push-notifications-to-a-web-app-with-firebase-528a702e13e1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dRRGbswavkQQyO_P.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: push notification
  slug: push-notification
- name: 'tech '
  slug: tech
seo_title: Comment ajouter des notifications push à une application web avec Firebase
  ?
seo_desc: 'By Leonardo Cardoso

  As web applications evolve, it is increasingly common to come across functionality
  that you’d normally associate with a native app in a web app. Many sites send notifications
  to their users through the browser for various events t...'
---

Par Leonardo Cardoso

Alors que les applications web évoluent, il est de plus en plus courant de rencontrer des fonctionnalités que l'on associerait normalement à une application native dans une application web. De nombreux sites envoient des notifications à leurs utilisateurs via le navigateur pour divers événements qui se produisent dans l'application web.

Aujourd'hui, je vais vous montrer les étapes nécessaires, en détail, pour atteindre une telle fonctionnalité dans votre application web en utilisant **Firebase**.

### Notifications avec Firebase

Firebase est une plateforme qui offre divers services pour les applications mobiles et web et aide les développeurs à construire des applications rapidement avec de nombreuses fonctionnalités.

Pour envoyer les notifications, nous allons utiliser le service appelé [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/), qui nous permet d'envoyer des messages à n'importe quel appareil en utilisant des requêtes HTTP.

### Installation du projet

Tout d'abord, vous devez avoir un compte [Firebase](https://console.firebase.google.com) et vous devrez créer un nouveau projet.

Pour cette configuration de démonstration, j'utiliserai un projet simple créé avec [**create-react-app**](https://github.com/facebook/create-react-app), mais vous pouvez utiliser le même code ailleurs avec JavaScript.

En plus de cela, nous devons ajouter la bibliothèque Firebase au projet.

```bash
npm install firebase --save
```

### Commençons à coder !

Maintenant que nous avons fait notre installation, nous pouvons commencer à coder le module qui sera responsable des notifications.

Créons un fichier dans le répertoire du projet appelé `push-notification.js`.

À l'intérieur du fichier, créons une fonction qui initialise Firebase et passe les clés de votre projet.

```js
import firebase from 'firebase';

export const initializeFirebase = () => {
  firebase.initializeApp({
    messagingSenderId: "votre messagingSenderId"
  });
}
```

Bien, maintenant que nous avons la fonction, nous devons l'appeler.

À l'intérieur du point d'entrée de votre projet, importez la fonction et appelez-la.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { initializeFirebase } from './push-notification';

ReactDOM.render(<App />, document.getElementById('root'));
initializeFirebase();
```

> Vous pouvez trouver les clés de votre projet dans la **Console Firebase**.

![Image](https://cdn-media-1.freecodecamp.org/images/yXHjfM1BfNm78YYVB1v14m7so7gfYEBqr0eX)
_Obtention des clés_

#### Service Workers

> Un service worker est un script que votre navigateur exécute en arrière-plan, séparément de la page web, permettant des fonctionnalités qui ne nécessitent pas une page web ou une interaction utilisateur.

Pour recevoir l'événement **onMessage**, votre application a besoin d'un service worker. Par défaut, lorsque vous démarrez Firebase, il recherche un fichier appelé `firebase-messaging-sw.js`.

Mais si vous en avez déjà un et que vous souhaitez l'utiliser pour recevoir des notifications, vous pouvez spécifier lors du démarrage de Firebase quel service worker il utilisera. Par exemple :

```js
export const initializeFirebase = () => {
  firebase.initializeApp({
    messagingSenderId: 'votre messagingSenderId'
  });
  
navigator.serviceWorker
    .register('/my-sw.js')
    .then((registration) => {
      firebase.messaging().useServiceWorker(registration);
    });
}
```

Ce service worker importera essentiellement le script nécessaire pour afficher les notifications lorsque votre application est en arrière-plan.

Nous devons ajouter `firebase-messaging-sw.js` à l'emplacement où vos fichiers sont servis. Comme j'utilise create-react-app, je vais l'ajouter dans le dossier public avec le contenu suivant :

```js
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-messaging.js');

firebase.initializeApp({
    messagingSenderId: "votre messagingSenderId encore"
});

const messaging = firebase.messaging();
```

### Demander la permission d'envoyer des notifications

Eh bien, tout le monde sait à quel point c'est ennuyeux d'entrer sur un site et de demander une autorisation pour envoyer des notifications. Alors faisons-le autrement !
Laissez l'utilisateur choisir s'il veut recevoir des notifications ou non.

Tout d'abord, créons la fonction qui fera la demande et retournera le token de l'utilisateur.

À l'intérieur de notre fichier push-notification.js, ajoutez la fonction :

```js
export const askForPermissioToReceiveNotifications = async () => {
  try {
    const messaging = firebase.messaging();
    await messaging.requestPermission();
    const token = await messaging.getToken();
    console.log('token de l\'utilisateur:', token);
    
    return token;
  } catch (error) {
    console.error(error);
  }
}
```

Nous devons appeler cette fonction depuis quelque part, alors je vais l'ajouter au clic d'un bouton.

```js
import React from 'react';
import { askForPermissioToReceiveNotifications } from './push-notification';

const NotificationButton = () => (
    <button onClick={askForPermissioToReceiveNotifications} >
      Cliquez ici pour recevoir des notifications
    </button>
);

export default NotificationButton;
```

D'accord, voyons cela fonctionner :

![Image](https://cdn-media-1.freecodecamp.org/images/khiSZEmyAt--sOXC1UbIYm4-GlPRI3WzBBg-)

### Envoyer des notifications

Pour envoyer la notification, nous devons faire une requête à l'API Firebase en l'informant du token que l'utilisateur recevra.

> Dans les exemples ci-dessous, j'utilise Postman, mais vous pouvez le faire depuis n'importe quel autre client REST.

Essentiellement, nous devons faire une requête POST à [https://fcm.googleapis.com/fcm/send](https://fcm.googleapis.com/fcm/send) en envoyant un JSON dans le corps de la requête.

Voici la structure du JSON qui sera envoyé :

```json
{
    "notification": {
        "title": "Firebase",
        "body": "Firebase est génial",
        "click_action": "http://localhost:3000/",
        "icon": "http://url-vers-une-icone/icon.png"
    },
    "to": "TOKEN UTILISATEUR"
}
```

Dans l'en-tête de la requête, nous devons passer la clé du serveur de notre projet dans Firebase et le type de contenu :

```
Content-Type: application/json
Authorization: key=SERVER_KEY
```

> La clé du serveur se trouve dans les paramètres du projet dans la Console Firebase sous l'onglet Cloud Messaging.

![Image](https://cdn-media-1.freecodecamp.org/images/RmPzmgbO2g2-9aexdELqtrpVyThMDDaMe4Mw)

#### Notifications en action

> Rappelez-vous que les notifications n'apparaîtront que lorsque votre application est minimisée ou en arrière-plan.

![Image](https://cdn-media-1.freecodecamp.org/images/ZCQkLJ-JT2iq1VXYSRjzio-tKEVdTEd6cSHl)

C'est ainsi que nous envoyons une notification directe à un appareil.

### Envoyer des notifications à un groupe d'utilisateurs

Eh bien, maintenant que nous avons vu comment envoyer une notification à un utilisateur, comment envoyer une notification à plusieurs utilisateurs à la fois ?

Pour cela, Firebase a une fonctionnalité appelée **topic**, où vous insérez plusieurs tokens pour un sujet spécifique, et vous pouvez envoyer la même notification à tous d'une seule requête.

#### Comment faire cela

Nous allons essentiellement envoyer une requête POST à l'adresse [https://iid.googleapis.com/iid/v1/**TOKEN**/rel/topics/**TOPIC_NAME**](https://iid.googleapis.com/iid/v1/TOKEN/rel/topics/TOPICO_NAME), en passant le nom du sujet et le token dans l'URL.

N'oubliez pas de passer dans l'en-tête la même autorisation que nous avons utilisée pour envoyer la notification.

![Image](https://cdn-media-1.freecodecamp.org/images/SkEgziQtqdWRAY91Vqat-Pli8fqwYMLrni2q)

L'envoi de la notification aux utilisateurs abonnés à un sujet est très similaire à l'envoi d'une notification à un seul utilisateur. La différence est que nous devons passer le nom du sujet dans l'attribut **"to"** au lieu du token.

Voir l'exemple ci-dessous :

```json
{
    "notification": {
        "title": "Firebase",
        "body": "Message de sujet Firebase",
        "click_action": "http://localhost:3000/",
        "icon": "http://localhost:3000/icon.png"
    },
    "to": "/topics/TOPIC_NAME"
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NzN-fFuUxFDuNbMRd8e9-qGJsbZZPdZwGnn8)

#### Conclusion

Merci d'avoir lu ceci ! J'espère que vous comprenez maintenant comment utiliser les notifications push. Le dépôt avec le code de démonstration peut être trouvé [ici](https://github.com/Leocardoso94/push-notification-demo).

Pour être informé de mes futurs articles, suivez-moi sur [GitHub](https://github.com/Leocardoso94) ou [Twitter](https://twitter.com/Leocardoso94_).