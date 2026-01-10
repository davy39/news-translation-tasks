---
title: Comment coder un chatbot adapté aux applications web comme Google Maps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T08:25:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-chatbot-tailored-for-web-apps-like-google-maps-cf97fc090676
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aJhKGNE9DKAbp8YODtMfSQ.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Applications
  slug: web-applications
seo_title: Comment coder un chatbot adapté aux applications web comme Google Maps
seo_desc: 'By Paul Pinard

  In this article, we’ll learn how to integrate a SAP Conversational AI chatbot into
  any of your web applications and provide users with a fun and intuitive way to interact
  with the UI!

  Conversational interfaces are gaining in popularity...'
---

Par Paul Pinard

_Dans cet article, nous allons apprendre comment intégrer un chatbot SAP Conversational AI dans n'importe laquelle de vos applications web et offrir aux utilisateurs une manière amusante et intuitive d'interagir avec l'interface utilisateur !_

Les interfaces conversationnelles gagnent en popularité, notamment pour interagir avec des systèmes backend semblant opaques. Par exemple, nous pouvons déployer un chatbot pour guider un client à travers un processus de dépannage et créer un ticket s'il a besoin d'une assistance supplémentaire ; tout cela sans que le client ait besoin de connaître le processus de création de ticket.

Cela permet une expérience plus intuitive pour votre client, augmentant la satisfaction client, tout en améliorant l'efficacité en libérant les employés de la gestion de la classification et du routage des tickets.

L'IA conversationnelle peut gérer cela directement, mais que faire si vos utilisateurs veulent pouvoir interagir avec votre application front-end ?

Par exemple, il pourrait être agréable pour votre utilisateur de naviguer vers une certaine page au sein de votre site web sans avoir à trouver le lien exact. Ou permettre à votre utilisateur d'appliquer un filtre complexe à une liste de produits sans avoir à cliquer dans les menus.

Bien que notre webchat puisse être intégré dans n'importe quel site web, il n'a pas la conscience contextuelle de l'interface utilisateur nécessaire pour ces types d'interactions. Pour démontrer comment nous pouvons accomplir cette conscience contextuelle, nous allons créer une application de carte simple avec un bot intégré capable de déplacer la carte et de zoomer ou dézoomer :

![Image](https://cdn-media-1.freecodecamp.org/images/toqt9Ke0kTZX07moBvygkjtYpv7qsRdFzxB0)

### Ressources

[Créez votre premier chatbot sur SAP Conversational AI](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/)

[Apprenez à héberger vous-même le Webchat](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat)

[API Google Maps](https://developers.google.com/maps/documentation/javascript/tutorial)

[Bot de déplacement de carte](https://cai.tools.sap/timoteo/map-mover)

[Code source de l'application Frontend](https://github.com/timothy-janssen/map-app)

[Application de carte finale](https://map-app-demo-1.herokuapp.com/)

### Prérequis

* Tout d'abord, vous devrez être à l'aise pour construire un bot simple en utilisant [SAP Conversational AI](https://cai.tools.sap/). Si vous n'êtes pas familier avec la plateforme, rendez-vous sur [ce tutoriel](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/) pour apprendre à construire un bot de blagues hilarantes.
* Vous devrez également être en mesure d'héberger notre composant webchat quelque part que vous contrôlez. Notre [GitHub](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat) contient toutes les informations pour vous aider à démarrer.
* Il est également attendu que vous soyez au moins familier avec JavaScript et les bases du développement web front-end.

### Tutoriel

Pour commencer, nous devrons définir l'interface pour que notre bot puisse envoyer des commandes et des messages à notre front-end. Cela sera accompli en envoyant un objet JSON stringifié à la place de la chaîne de message normale que nous envoyons généralement à l'utilisateur. Notre webchat modifié sera capable de comprendre cet objet JSON, de prendre l'action définie et enfin d'afficher un « message » à l'utilisateur.

Cela peut être accompli assez simplement ; nous allons envoyer un objet avec une action soit « move » soit « zoom » et ensuite un message que nous pouvons montrer à l'utilisateur. Notez que nous allons passer cet objet JSON sous forme de chaîne, et il est de notre responsabilité que l'application le parse et n'affiche que la valeur de « message » à l'utilisateur.

```
{ "action": "move" || "zoom", "message": "Ceci sera affiché à l'utilisateur" }
```

Si notre type d'action est « move », la carte aura besoin de coordonnées pour naviguer. Nous allons donc inclure les coordonnées d'un lieu dans notre objet JSON. Alternativement, si notre action est zoom, nous aurons besoin de savoir si nous devons zoomer ou dézoomer. Pour cela, nous inclurons une direction représentée par un 1 pour zoomer ou un -1 pour dézoomer. Avec cela défini, voici quelques exemples de ce à quoi nos objets JSON pourraient ressembler :

```
{"action": "move", "location": { "lat": -8.3405389, "lng": 115.0919509 }, "message": "Direction Bali, Indonésie !"}
{"action": "zoom", "direction": 1, "message": "Zoom avant !"}
```

Avec cela en tête, nous pouvons commencer à construire notre bot. Comme toujours, nous allons commencer par définir les intentions que notre utilisateur pourrait dire. Dans ce cas, nous avons zoom et move-map.

![Image](https://cdn-media-1.freecodecamp.org/images/NIEtf89-2sa-bqKdTwqZHGGUZHtWPWMHoF7n)

Notez que nous devrons tagger les phrases dans @zoom avec l'entité 'direction', mais 'location' est automatiquement reconnu dans @move-map. Heureusement pour nous, l'entité gold location vient avec la longitude et la latitude directement, donc nous pourrons facilement passer ces informations au front-end.

Pour obtenir le 1 ou -1 qui représente notre direction de zoom, nous allons utiliser des enrichissements personnalisés. Nous allons ajouter les clés « name » et « direction » avec les valeurs suivantes. Ensuite, mapper les valeurs d'entité correctes à leurs valeurs de clé respectives.

![Image](https://cdn-media-1.freecodecamp.org/images/XZ0zra0PVE06eW8KruOypINZ4675DnIY6JJB)

Maintenant que nous pouvons reconnaître notre intention move-map, nous avons juste besoin d'une compétence qui est déclenchée si notre intention est reconnue :

![Image](https://cdn-media-1.freecodecamp.org/images/Zax0InkCgVVGJNFdLbbENHLmsesnwdhmnuBh)

Et nécessite un emplacement :

![Image](https://cdn-media-1.freecodecamp.org/images/XyP2bn7OkfeOh75b5I5CcconwlgIdZZ1PPhk)

Et enfin envoie un message en retour indiquant au front-end où aller :

![Image](https://cdn-media-1.freecodecamp.org/images/BEwrDwYK-iaXCdAyYgT-npS2a2AJ7Fjvh1rG)

La compétence de zoom peut être implémentée de manière similaire ; je vous encourage à essayer par vous-même !

Maintenant que notre bot est terminé, nous devrons héberger le webchat localement afin de pouvoir le modifier pour comprendre nos réponses « inhabituelles ». Si vous n'êtes pas familier avec le processus d'auto-hébergement, consultez [ce github](https://github.com/SAPConversationalAI/Webchat#self-hosted-webchat).

Enfin, il est temps de construire notre application web. Nous allons commencer par inclure une div de conteneur pour notre carte, le script que nous allons écrire pour gérer les interactions de la carte (map_controls.js), le script nécessaire tel que décrit dans [ce tutoriel de Google](https://developers.google.com/maps/documentation/javascript/tutorial), et la balise de script pointant vers notre bot hébergé localement. Cela devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/e4i94mJRLa5VonQkSluAfu0GyjxAvnNc0B5Z)

Pour compléter notre application simple, nous allons implémenter notre initialisation de carte et les méthodes de zoom/déplacement :

```
function initMap() {
  window.map = new google.maps.Map(document.getElementById('map'), {
    // OPTIONS
    center: {lat: -34.397, lng: 150.644},
    zoom: 8,
    zoomControl: false,
    streetViewControl: false,
    mapTypeControl: false,
    rotateControl: false,
    scaleControl: false,
    fullscreenControl: false
  });
}

const zoom = (direction) => {
  window.map.setZoom(window.map.getZoom() + direction);
}
```

```
const setCenter = (lat, lng) => {
  window.map.setCenter({lat: lat, lng: lng});
}
```

Une fois que nous avons ajouté avec succès le chatbot à notre application, nous pourrons lui demander de se déplacer ou de zoomer/dézoomer, mais il affichera toujours cette chaîne JSON peu attrayante. Pour résoudre cela, nous allons ajouter le code suivant à Webchat/src/containers/Chat/index.js. Cela recherchera dans l'objet window une fonction appelée applicationParse et l'appellera si elle existe.

```
const getApplicationParse = messages => {
  return new Promise(resolve => {
    if (!window.webchatMethods || !window.webchatMethods.applicationParse) {
      return resolve()
    }
    // afin que nous traitons le message dans tous les cas
    setTimeout(resolve, MAX_GET_MEMORY_TIME)
    try {
      const applicationParseResponse = window.webchatMethods.applicationParse(messages)
      if (!applicationParseResponse) {
        return resolve()
      }
      if (applicationParseResponse.then && typeof applicationParseResponse.then === 'function') {
        // la fonction a retourné une Promesse
        applicationParseResponse
          .then(applicationParse => resolve())
          .catch(err => {
            console.error(FAILED_TO_GET_MEMORY)
            console.error(err)
            resolve()
          })
      } else {
        resolve()
      }
    } catch (err) {
      console.error(FAILED_TO_GET_MEMORY)
      console.error(err)
      resolve()
    }
  })
}
```

Maintenant, nous allons appeler getApplicationParse avant l'appel à setState dans componentWillReceiveProps. Cela garantira que notre application ait une chance de parser la réponse du bot avant que quoi que ce soit ne soit renvoyé à l'utilisateur.

```
componentWillReceiveProps(nextProps) {
  const { messages, show } = nextProps
  if (messages !== this.state.messages) {
    getApplicationParse(messages)
    this.setState({ messages }, () => {
      const { getLastMessage } = this.props
      if (getLastMessage) {
        getLastMessage(messages[messages.length - 1])
      }
    })
  }
  if (show && show !== this.props.show && !this.props.sendMessagePromise && !this._isPolling) {
    this.doMessagesPolling()
  }
}
```

Enfin, nous devons implémenter applicationParse et l'inclure dans l'objet window depuis map_controls.js. Ici, nous allons parcourir nos messages, et si c'est une commande d'action valide du bot, prendre l'action et retourner uniquement le message à l'utilisateur.

```
window.webchatMethods = {
  applicationParse: (messages) => {
    messages.map(message => {
      try {
        var obj = JSON.parse(message.attachment.content);
        console.log(obj);
        if(obj !== undefined &&
            obj.action == 'zoom' &&
            typeof obj.direction === "number"){
          message.attachment.content = obj.message.toString();
          zoom(obj.direction);
        } else if (obj !== undefined &&
                    obj.action == 'move' &&
                    typeof obj.location.lat === "number" &&
                    typeof obj.location.lng === "number") {
          message.attachment.content = obj.message.toString();
          setCenter(obj.location.lat, obj.location.lng);
        }
      } catch (err) {
        // JSON invalide - traiter comme un message régulier et le renvoyer à l'UI tel quel
      }
      message
    })
    return messages;
  }
}
```

Vous pouvez maintenant demander à votre bot de déplacer ou de zoomer la carte et il enverra un message que l'application peut interpréter et agir en conséquence.

Avec cet outil dans votre boîte à outils, vous pouvez maintenant intégrer un chatbot dans n'importe laquelle de vos applications web !

_Originalement publié sur [SAP Conversational AI blog](https://cai.tools.sap/blog/how-to-control-your-web-application-with-an-integrated-chatbot/)._