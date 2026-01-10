---
title: How to add push notifications to a web app with Firebase ?+?
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
seo_title: null
seo_desc: 'By Leonardo Cardoso

  As web applications evolve, it is increasingly common to come across functionality
  that you’d normally associate with a native app in a web app. Many sites send notifications
  to their users through the browser for various events t...'
---

By Leonardo Cardoso

As web applications evolve, it is increasingly common to come across functionality that you’d normally associate with a native app in a web app. Many sites send notifications to their users through the browser for various events that occur within the web app.

Today, I’ll show you the steps required, in detail, to achieve such functionality in your web app using **Firebase**.

### Notifications with Firebase

Firebase is a platform that offers various services for mobile and web applications and helps developers build apps quickly with a lot of features.

To send the notifications, we will use the service called [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/), which allows us to send messages to any device using HTTP requests.

### Project Setup

First of all, you need to have a [Firebase](https://console.firebase.google.com) account and you’ll need to create a new project within it.

For this demo setup, I will use a simple project created with the [**create-react-app**](https://github.com/facebook/create-react-app), but you can use the same code anywhere else that uses JavaScript.

In addition to that, we need to add the Firebase library to the project.

```bash
npm install firebase --save
```

### So let’s get coding!

Now that we’ve done our setup, we can begin coding the module that will be in charge of notifications.

Let’s create a file inside the project directory called `push-notification.js`.

Inside the file, let’s create a function that initializes Firebase and passes the keys of your project.

```js
import firebase from 'firebase';

export const initializeFirebase = () => {
  firebase.initializeApp({
    messagingSenderId: "your messagingSenderId"
  });
}
```

Well, now that we have the function we need to call it.

Inside the entry point of your project, import the function and call it.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { initializeFirebase } from './push-notification';

ReactDOM.render(<App />, document.getElementById('root'));
initializeFirebase();
```

> You can find the keys to your project inside the **Firebase Console.**

![Image](https://cdn-media-1.freecodecamp.org/images/yXHjfM1BfNm78YYVB1v14m7so7gfYEBqr0eX)
_Getting the keys_

#### Service Workers

> A service worker is a script that your browser runs in the background, separate from the web page, enabling features that do not require a web page or user interaction.

To receive the **onMessage** event, your app needs a service worker. By default, when you start Firebase, it looks for a file called `firebase-messaging-sw.js`.

But if you already have one and want to take advantage of it to receive notifications, you can specify during the Firebase startup which service worker it will use. For example:

```js
export const inicializarFirebase = () => {
  firebase.initializeApp({
    messagingSenderId: 'your messagingSenderId'
  });
  
navigator.serviceWorker
    .register('/my-sw.js')
    .then((registration) => {
      firebase.messaging().useServiceWorker(registration);
    });
}
```

This service worker will basically import the script needed to show the notifications when your app is in the background.

We need to add `firebase-messaging-sw.js` to the location where your files are served. As I’m using the create-react-app, I’m going to add it inside the public folder with the following content:

```js
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-messaging.js');

firebase.initializeApp({
    messagingSenderId: "your messagingSenderId again"
});

const messaging = firebase.messaging();
```

### Requesting permission to send notifications

Well, everyone knows how annoying it is to enter the site and ask for authorization to send notifications. So let’s do it another way!  
Let the user choose whether or not to receive notifications.

First of all, let’s create the function that will make the request and return the user’s token.

Inside our push-notification.js file, add the function:

```js
export const askForPermissioToReceiveNotifications = async () => {
  try {
    const messaging = firebase.messaging();
    await messaging.requestPermission();
    const token = await messaging.getToken();
    console.log('token do usuário:', token);
    
    return token;
  } catch (error) {
    console.error(error);
  }
}
```

We need to call this function from somewhere, so I’ll add it at the click of a button.

```js
import React from 'react';
import { askForPermissioToReceiveNotifications } from './push-notification';

const NotificationButton = () => (
    <button onClick={askForPermissioToReceiveNotifications} >
      Clique aqui para receber notificações
    </button>
);

export default NotificationButton;
```

Okay, let’s see it working:

![Image](https://cdn-media-1.freecodecamp.org/images/khiSZEmyAt--sOXC1UbIYm4-GlPRI3WzBBg-)

### Sending notifications

To send the notification, we need to make a request to the Firebase API informing it of the token the user will receive.

> In the examples below I use Postman, but you can do this from any other REST client.

Basically, we need to make a POST request to [https://fcm.googleapis.com/fcm/send](https://fcm.googleapis.com/fcm/send) by sending a JSON in the request body.

Below is the structure of the JSON that will be sent:

```json
{
    "notification": {
        "title": "Firebase",
        "body": "Firebase is awesome",
        "click_action": "http://localhost:3000/",
        "icon": "http://url-to-an-icon/icon.png"
    },
    "to": "USER TOKEN"
}
```

In the request header, we need to pass the server key of our project in Firebase and the content-type:

```
Content-Type: application/json
Authorization: key=SERVER_KEY
```

> The server key is found in the project settings in the Firebase Console under the Cloud Messaging tab.

![Image](https://cdn-media-1.freecodecamp.org/images/RmPzmgbO2g2-9aexdELqtrpVyThMDDaMe4Mw)

#### Notifications in action

> Remember that notifications will only appear when your app is minimized or in the background.

![Image](https://cdn-media-1.freecodecamp.org/images/ZCQkLJ-JT2iq1VXYSRjzio-tKEVdTEd6cSHl)

That is how we send a direct notification to a device.

### Send notifications to a group of users

Well, now that we’ve seen how to send a notification to one user, how do we send a notification to multiple users at once?

To do this, Firebase has a feature called **topic**, where you insert multiple tokens for a specific topic, and you can send the same notification to all of them from a single request.

#### How to do this

We will basically send a POST request to the address [https://iid.googleapis.com/iid/v1/**TOKEN**/rel/topics/**TOPIC_NAME**](https://iid.googleapis.com/iid/v1/TOKEN/rel/topics/TOPICO_NAME), passing the topic name and the token in the URL.

Do not forget to pass in the header the same authorization that we used to send the notification.

![Image](https://cdn-media-1.freecodecamp.org/images/SkEgziQtqdWRAY91Vqat-Pli8fqwYMLrni2q)

Sending the notification to users subscribed to any topic is very similar to sending a notification to a single user. The difference is that we need to pass the topic name in the **“to”** attribute instead of the token.

See the example below:

```json
{
    "notification": {
        "title": "Firebase",
        "body": "Firebase topic message",
        "click_action": "http://localhost:3000/",
        "icon": "http://localhost:3000/icon.png"
    },
    "to": "/topics/TOPIC_NAME"
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NzN-fFuUxFDuNbMRd8e9-qGJsbZZPdZwGnn8)

#### Conclusion

Thanks for reading this! I hope you now understand how to make use of push notifications. The repository with the demo code can be found [here](https://github.com/Leocardoso94/push-notification-demo).

To get notified of my future posts, follow me on [GitHub](https://github.com/Leocardoso94) or [Twitter](https://twitter.com/Leocardoso94_).

