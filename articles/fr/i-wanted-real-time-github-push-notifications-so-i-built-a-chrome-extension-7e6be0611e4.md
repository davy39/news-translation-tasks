---
title: Je voulais des notifications en temps réel pour les pushes GitHub. J'ai donc
  créé une extension Chrome.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-06T22:29:04.000Z'
originalURL: https://freecodecamp.org/news/i-wanted-real-time-github-push-notifications-so-i-built-a-chrome-extension-7e6be0611e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Hg7eTKIeGViovyRiASzdCw.png
tags:
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Je voulais des notifications en temps réel pour les pushes GitHub. J'ai
  donc créé une extension Chrome.
seo_desc: 'By Stacy Goh

  I’ve been using GitHub for more than two years now. A few days ago, I was wondering
  why there were no push notifications for GitHub. I already receive email notifications
  when someone creates a pull request/issue on my repositories, but ...'
---

Par Stacy Goh

#### J'utilise GitHub depuis plus de deux ans. Il y a quelques jours, je me demandais pourquoi il n'y avait pas de notifications push pour GitHub. Je reçois déjà des notifications par email lorsqu'une personne crée une pull request ou un issue sur mes dépôts, mais il n'y a pas de notifications pour les étoiles ou les forks.

De plus, les notifications par email s'accumulent en plus des 12 253 emails déjà dans ma boîte de réception. Ce n'est tout simplement pas cool >.<

![Image](https://cdn-media-1.freecodecamp.org/images/Wmj57DMUNm28INvgfkCUjnsEiyy8Y1j8QYwy)
_Vous voyez, je ne plaisante pas ! Crédit : Ma propre boîte de réception_

En tant que développeur, j'ai décidé de prendre les choses en main. J'ai décidé de créer une extension Chrome qui envoie des notifications en temps réel chaque fois que quelqu'un interagit avec un ou plusieurs de mes dépôts GitHub. Elle est disponible sur le Chrome Web Store sous le nom de [**GitHub Notifier**](https://chrome.google.com/webstore/detail/github-notifier/hoapibhhppbolnldjengllkcdbpbbgih). Vous pouvez également en savoir plus à ce sujet [**ici**](https://stacygohyunsi.github.io).

![Image](https://cdn-media-1.freecodecamp.org/images/NW4TcUDcHzAiMHBjsId06VfBq-2-4dPjB1ns)

![Image](https://cdn-media-1.freecodecamp.org/images/Zce9wGBY9ZDQ-iWibv8CLgxeaJB3rKhrLQnt)
_Notifications Chrome en temps réel_

Vous verrez l'une des notifications ci-dessus chaque fois que quelqu'un fait l'une des actions suivantes :

* Crée un issue ou commente un issue
* Crée une pull request
* Fork votre dépôt
* Star votre dépôt
* Push du code vers votre dépôt

### Comment je l'ai construit

Au début, je pensais que ce serait vraiment simple à construire. Je pensais pouvoir le faire en un jour puisque j'avais de l'expérience dans la création d'applications Chrome.

Mais comme toujours, le diable est dans les détails. Voici les outils, frameworks et autres choses que j'ai utilisés pour le faire fonctionner :

* GitHub Apps
* Express et NodeJS
* Firebase
* Google Cloud Messaging
* Extension Chrome

### GitHub Apps

Pour envoyer des notifications à un utilisateur en temps réel, nous devons utiliser un webhook pour les informer chaque fois qu'il y a une interaction utilisateur. Le payload contiendra des informations, telles que la personne qui a interagi avec votre dépôt, l'action effectuée (était-ce un star ou un fork), et le nom du dépôt.

Pour cela, enregistrez une GitHub App. Cela vous permettra de choisir les événements de webhook que votre GitHub App détectera.

![Image](https://cdn-media-1.freecodecamp.org/images/vhF7U0nC4e9Cdm7kQrwPR2SOJvEZVmFY9YZw)
_Permissions pour les applications GitHub_

Remplissez l'URL de votre webhook, que je couvrirai plus tard.

_Pour aller plus loin : [GitHub Apps](https://developer.github.com/apps/)_

### Express et NodeJS

Après avoir défini les événements que le webhook déclenche, vous avez besoin d'un serveur pour recevoir et traiter le payload. Comme les extensions Chrome autonomes ne peuvent pas lancer un serveur, nous devons créer un projet séparé pour cela.

Créez un endpoint POST dans votre projet Express et NodeJS, qui gérera le webhook.

```
app.post('/watch', function(req, res, next) {
```

```
.....
```

```
});
```

Pour les webhooks, j'aime utiliser `[ngrok](https://ngrok.com/)` — un outil gratuit (avec une limite de 30 utilisateurs), qui crée une URL accessible publiquement pour configurer le service de webhook.

Une fois que vous avez installé `ngrok`, vous pouvez l'utiliser pour créer un tunnel vers une application exécutée sur, par exemple, le port 3000. C'est aussi simple que de taper

```
ngrok http 3000
```

`ngrok` génère ensuite une URL en `http` et `https`. Vous pouvez utiliser celles-ci pour remplir temporairement l'URL de votre webhook dans GitHub Apps jusqu'à ce que vous les hébergiez.

_Pour aller plus loin : [ngrok](https://ngrok.com/)_

### **L'extension Chrome**

Ensuite, créez un projet séparé pour votre extension Chrome. Une extension Chrome en elle-même est facile à construire. Tout d'abord, créez un fichier `manifest.json` qui contient des propriétés comme le nom de l'extension, la description, le numéro de version, etc.

Nous aurons également besoin d'un fichier `popup.html`, qui affiche une popup lorsque quelqu'un télécharge et clique sur votre extension Chrome. La popup invite les utilisateurs à remplir leur nom d'utilisateur GitHub, comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/z9bvwhUjtGyjwDRlZ1QwcuCBUNHvpt0pZAtx)
_popup.html_

Après avoir enregistré votre nom d'utilisateur GitHub, connectez votre nom d'utilisateur GitHub à un ordinateur qui recevra les notifications.

Nous faisons cela avec Google Cloud Messaging et Firebase.

_Pour aller plus loin : [Getting Started: Building a Chrome Extension](https://developer.chrome.com/extensions/getstarted)_

### Google Cloud Messaging et Firebase

[Google Cloud Messaging](https://developers.google.com/cloud-messaging/gcm) (GCM) est un service de notification mobile qui permet aux développeurs d'envoyer des messages entre des serveurs et des applications client.

[Firebase](https://firebase.google.com/docs/database/) est une base de données en temps réel, hébergée dans le cloud, développée par Google. J'ai choisi Firebase pour ce cas car il est facile et rapide à configurer.

Dans votre extension Chrome, créez un fichier `popup.js`. Cela utilisera à la fois GCM et Firebase. Après avoir enregistré votre nom d'utilisateur dans la popup, utilisez GCM pour générer un registrationID afin d'identifier votre navigateur. Pensez à registrationID comme un identifiant pour différencier votre ordinateur des autres utilisateurs.

Le registrationID et le nom d'utilisateur GitHub seront enregistrés comme une entrée dans Firebase.

_Pour aller plus loin : [Firebase](https://firebase.google.com/docs/database/) et [Google Cloud Messaging](https://developers.google.com/cloud-messaging/gcm)_

### Comment tout cela fonctionne-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/eRJCkjdghFz57Lc84U8zx0RNpj2ogGSSn6m8)
_Diagramme récapitulatif de la construction du GitHub Notifier_

Pour résumer l'illustration ci-dessus, chaque fois que quelqu'un interagit avec le dépôt GitHub, les étapes suivantes se produisent :

* Un payload est envoyé de GitHub Apps à votre serveur Express et NodeJS.
* Le serveur reçoit le payload et extrait le nom d'utilisateur GitHub du payload.
* Interrogez Firebase pour obtenir le registrationID associé au nom d'utilisateur GitHub.
* Google Cloud Messaging est utilisé pour envoyer un message du serveur à l'extension Chrome en fonction du registrationID.
* Une fois que l'extension Chrome reçoit le message de Google Cloud Messaging, elle crée une notification Chrome et la push vers l'utilisateur.

Et voilà ! Vous avez reçu une notification Chrome en temps réel de GitHub !

J'espère ne pas vous avoir perdu en chemin. Une fois de plus, installez [**GitHub Notifier**](https://chrome.google.com/webstore/detail/github-notifier/hoapibhhppbolnldjengllkcdbpbbgih) si vous êtes aussi enthousiaste que moi à l'idée de recevoir des notifications push GitHub en temps réel. Envoyez-moi un message si vous avez besoin de clarifications supplémentaires.

Si vous avez des suggestions d'améliorations ou si vous connaissez une manière plus simple de construire un GitHub Chrome Notifier, envoyez-moi un message à [**hello@imstacy.com**](mailto:hello@imstacy.com) et discutons-en.

Ou si vous avez aimé mon article, suivez-moi sur [**github.com/stacygohyunsi**](http://github.com/stacygohyunsi) ou envoyez-moi un message sur [**imstacy.com**](http://imstacy.com).

#### _***Si vous avez 7 dollars à dépenser, ou si vous souhaitez sponsoriser ce projet, envoyez-moi un message à [https://imstacy.com](https://imstacy.com) ou soutenez-moi à [https://www.patreon.com/stacygohys](https://www.patreon.com/stacygohys).** C'est le montant d'argent nécessaire pour les coûts du serveur chaque mois. J'apprécierais vraiment ! (:(:_