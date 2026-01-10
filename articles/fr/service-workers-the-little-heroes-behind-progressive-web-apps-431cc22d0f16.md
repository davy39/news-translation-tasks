---
title: 'Service workers : les petits héros derrière les Progressive Web Apps'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-05T11:28:49.000Z'
originalURL: https://freecodecamp.org/news/service-workers-the-little-heroes-behind-progressive-web-apps-431cc22d0f16
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CqQTKb0N2o0suacfiluO8w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Service workers : les petits héros derrière les Progressive Web Apps'
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Service workers are at the core of Progressive Web Apps. They allow caching of resources
  and push notifications, which are two of the main distinguishing features that have
  set native...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Les service workers sont au cœur des [Progressive Web Apps](https://flaviocopes.com/what-is-a-progressive-web-app/). Ils permettent la mise en cache des ressources et les notifications push, deux des principales fonctionnalités qui ont distingué les applications natives jusqu'à présent.

Un service worker est un **proxy programmable** entre votre page web et le réseau, offrant la possibilité d'intercepter et de mettre en cache les requêtes réseau. Cela permet effectivement de **créer une expérience hors ligne pour votre application**.

Les service workers sont un type spécial de web worker : un fichier JavaScript associé à une page web qui s'exécute dans un contexte de worker, séparé du thread principal. Cela offre l'avantage d'être non bloquant — ainsi, les calculs peuvent être effectués sans sacrifier la réactivité de l'UI.

Étant donné qu'il s'exécute dans un thread séparé, il n'a pas accès au DOM. Il n'a pas non plus accès aux API de Local Storage et à l'API XHR. Il ne peut communiquer avec le thread principal qu'en utilisant l'**API de messagerie par canal**.

Les service workers coopèrent avec d'autres API Web récentes :

* **Promesses**
* **Fetch API**
* **Cache API**

Et ils sont **uniquement disponibles sur les pages en protocole HTTPS** (sauf pour les requêtes locales, qui n'ont pas besoin d'une connexion sécurisée. Cela facilite les tests.).

### Traitement en arrière-plan

Les service workers s'exécutent indépendamment de l'application à laquelle ils sont associés, et ils peuvent recevoir des messages lorsqu'ils ne sont pas actifs.

Par exemple, ils peuvent fonctionner :

* lorsque votre application mobile est **en arrière-plan**, non active
* lorsque votre application mobile est **fermée** et même ne s'exécute pas en arrière-plan
* lorsque **le navigateur est fermé**, si l'application s'exécute dans le navigateur

Les principaux scénarios où les service workers sont très utiles sont :

* Ils peuvent être utilisés comme une **couche de cache** pour gérer les requêtes réseau, et mettre en cache le contenu à utiliser hors ligne
* Ils peuvent permettre les **notifications push**

Un service worker ne s'exécute que lorsque cela est nécessaire, et il est arrêté lorsqu'il n'est pas utilisé.

### Support hors ligne

Traditionnellement, l'expérience hors ligne pour les applications web a été très pauvre. Sans réseau, souvent les applications web mobiles ne fonctionnent tout simplement pas. Les applications mobiles natives, en revanche, ont la capacité d'offrir soit une version fonctionnelle, soit un message agréable.

Ce n'est pas un message agréable, mais voici à quoi ressemblent les pages web dans Chrome sans connexion réseau :

![Image](https://cdn-media-1.freecodecamp.org/images/dS6TKfY7CA6UEOB2OUVeausTK3eyPx2DSZ76)

Possiblement la seule chose agréable à propos de cela est que vous pouvez jouer à un jeu gratuit en cliquant sur le dinosaure — mais cela devient ennuyeux assez rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/56VoLGuQErxh7lGJGDLw-Iuj0TpBsUXE2ZBH)

Dans le passé récent, l'AppCache HTML5 promettait déjà de permettre aux applications web de mettre en cache des ressources et de fonctionner hors ligne. Mais son manque de flexibilité et son comportement confus ont montré qu'il n'était pas assez bon pour le travail (et [il a été abandonné](https://html.spec.whatwg.org/multipage/offline.html#offline)).

Les service workers sont le nouveau standard pour la mise en cache hors ligne.

Quel type de mise en cache est possible ?

### Pré-mise en cache des ressources lors de l'installation

Les ressources qui sont réutilisées dans toute l'application, comme les images, les CSS, les fichiers JavaScript, peuvent être installées la première fois que l'application est ouverte.

Cela constitue la base de ce que l'on appelle l'**architecture App Shell**.

### Mise en cache des requêtes réseau

En utilisant l'**API Fetch**, nous pouvons modifier la réponse provenant du serveur, déterminer si le serveur n'est pas accessible et fournir une réponse à partir du cache à la place.

### Cycle de vie d'un Service Worker

Un service worker passe par trois étapes pour devenir pleinement fonctionnel :

* Enregistrement
* Installation
* Activation

### Enregistrement

L'enregistrement indique au navigateur où se trouve le service worker, et il commence l'installation en arrière-plan.

Exemple de code pour enregistrer un service worker placé dans `worker.js` :

```
if ('serviceWorker' in navigator) {   window.addEventListener('load', () => {       navigator.serviceWorker.register('/worker.js')     .then((registration) => {       console.log('Enregistrement du Service Worker terminé avec la portée : ', registration.scope)     }, (err) => {       console.log('Échec de l\'enregistrement du Service Worker', err)    })  })} else {   console.log('Service Workers non supportés') }
```

Même si ce code est appelé plusieurs fois, le navigateur ne réalisera l'enregistrement que si le service worker est nouveau et non enregistré précédemment, ou s'il a été mis à jour.

#### Portée

L'appel `register()` accepte également un paramètre de portée, qui est un chemin déterminant quelle partie de votre application peut être contrôlée par le service worker.

Par défaut, il inclut tous les fichiers et sous-dossiers contenus dans le dossier qui contient le fichier du service worker. Ainsi, si vous le placez dans le dossier racine, il aura le contrôle sur l'ensemble de l'application. Dans un sous-dossier, il ne contrôlera que les pages accessibles sous cette route.

L'exemple ci-dessous enregistre le worker en spécifiant la portée du dossier `/notifications/`.

```
navigator.serviceWorker.register('/worker.js', {   scope: '/notifications/' })
```

Le `/` est important : dans ce cas, la page `/notifications` ne déclenchera pas le Service Worker, alors que si la portée était

```
{ scope: '/notifications' }
```

cela aurait fonctionné.

NOTE : Le service worker ne peut pas se "monter" lui-même depuis un dossier : si son fichier est placé sous `/notifications`, il ne peut pas contrôler le chemin `/` ou tout autre chemin qui n'est pas sous `/notifications`.

### Installation

Si le navigateur détermine qu'un service worker est obsolète ou n'a jamais été enregistré auparavant, il procédera à son installation.

```
self.addEventListener('install', (event) => {   //... });
```

C'est un bon moment pour préparer le service worker à être utilisé en **initialisant un cache**. Ensuite, **mettre en cache l'App Shell** et les ressources statiques en utilisant l'**API Cache**.

### Activation

Une fois le service worker enregistré et installé avec succès, la troisième étape est l'activation.

À ce stade, le service worker pourra fonctionner avec les nouvelles charges de page.

Il ne peut pas interagir avec les pages déjà chargées, donc le service worker n'est utile que la deuxième fois que l'utilisateur interagit avec l'application ou recharge l'une des pages déjà ouvertes.

```
self.addEventListener('activate', (event) => {   //... });
```

Un bon cas d'utilisation pour cet événement est de nettoyer les anciens caches et les éléments associés à l'ancienne version qui ne sont pas utilisés dans la nouvelle version du service worker.

### Mise à jour d'un Service Worker

Pour mettre à jour un service worker, il suffit de changer un octet dans celui-ci. Lorsque le code d'enregistrement est exécuté, il sera mis à jour.

Une fois qu'un service worker est mis à jour, il ne deviendra pas disponible tant que toutes les pages qui ont été chargées avec l'ancien service worker attaché ne sont pas fermées.

Cela garantit que rien ne se cassera sur les applications/pages qui fonctionnent déjà.

Rafraîchir la page n'est pas suffisant, car l'ancien worker est toujours en cours d'exécution et n'a pas été supprimé.

### Événements Fetch

Un **événement fetch** est déclenché lorsqu'une ressource est demandée sur le réseau.

Cela nous offre la possibilité de **chercher dans le cache** avant de faire des requêtes réseau.

Par exemple, l'extrait de code ci-dessous utilise l'**API Cache** pour vérifier si l'URL demandée a déjà été stockée dans les réponses en cache. Si c'est le cas, il retourne la réponse en cache. Sinon, il exécute la requête fetch et la retourne.

```
self.addEventListener('fetch', (event) => {  event.respondWith(     caches.match(event.request)       .then((response) => {         if (response) {           // entrée trouvée dans le cache           return response         }         return fetch(event.request)       }     )   ) })
```

### Synchronisation en arrière-plan

La synchronisation en arrière-plan permet de reporter les connexions sortantes jusqu'à ce que l'utilisateur ait une connexion réseau fonctionnelle.

Cela est essentiel pour garantir qu'un utilisateur peut utiliser l'application hors ligne, effectuer des actions sur celle-ci, et mettre en file d'attente les mises à jour côté serveur pour lorsqu'il y a une connexion ouverte (au lieu d'afficher une roue de chargement sans fin essayant d'obtenir un signal).

```
navigator.serviceWorker.ready.then((swRegistration) => {   return swRegistration.sync.register('event1') });
```

Ce code écoute l'événement dans le service worker :

```
self.addEventListener('sync', (event) => {   if (event.tag == 'event1') {     event.waitUntil(doSomething())   } })
```

`doSomething()` retourne une promesse. Si elle échoue, un autre événement de synchronisation sera planifié pour réessayer automatiquement jusqu'à ce qu'elle réussisse.

Cela permet également à une application de mettre à jour les données du serveur dès qu'une connexion fonctionnelle est disponible.

### Événements Push

Les service workers permettent aux applications web de fournir des notifications push natives aux utilisateurs.

Push et Notifications sont en réalité deux concepts et technologies différents qui sont combinés pour fournir ce que nous connaissons sous le nom de **notifications push**. Push fournit le mécanisme qui permet à un serveur d'envoyer des informations à un service worker, et Notifications sont la manière dont les service workers peuvent montrer des informations à l'utilisateur.

Étant donné que les service workers s'exécutent même lorsque l'application ne s'exécute pas, ils peuvent écouter les événements push entrants. Ils fournissent ensuite des notifications à l'utilisateur ou mettent à jour l'état de l'application.

Les événements push sont initiés par un backend, via un service de push de navigateur, comme celui fourni par [Firebase](https://flaviocopes.com/firebase-hosting).

Voici un exemple de la manière dont le web worker peut écouter les événements push entrants :

```
self.addEventListener('push', (event) => {   console.log('Reçu un événement push', event) 
```

```
  const options = {     title: 'J\'ai un message pour vous !',     body: 'Voici le corps du message',     icon: '/img/icon-192x192.png',     tag: 'tag-pour-cette-notification',   } 
```

```
  event.waitUntil(     self.registration.showNotification(title, options)   ) })
```

### Une note sur les logs de la console :

Si vous avez des instructions de log dans la console (`console.log` et autres) dans le service worker, assurez-vous d'activer la fonction `Preserve log` fournie par les Chrome Devtools (ou équivalent).

Sinon, puisque le service worker agit avant que la page ne soit chargée, et que la console est effacée avant le chargement de la page, vous ne verrez aucun log dans la console.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)