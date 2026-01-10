---
title: Comment utiliser l'API de géolocalisation en JavaScript – avec des exemples
  de code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-02-26T22:34:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-geolocation-api
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/js-geolocation-api-cover.png
tags:
- name: api
  slug: api
- name: geolocation
  slug: geolocation
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'API de géolocalisation en JavaScript – avec des exemples
  de code
seo_desc: 'The Geolocation API is a standard API implemented in browsers to retrieve
  the location of the people who are interacting with a web application.

  This API enable users to send their location to a web application to enable relevant
  services, such as se...'
---

L'API de géolocalisation est une API standard implémentée dans les navigateurs pour récupérer la position des personnes qui interagissent avec une application web.

Cette API permet aux utilisateurs d'envoyer leur position à une application web pour activer des services pertinents, tels que la recherche d'un restaurant ou d'un hôtel à proximité de l'utilisateur.

Dans cet article, je vais vous montrer comment utiliser l'API de géolocalisation avec JavaScript et afficher la position actuelle d'un utilisateur à l'aide d'une API de carte.

Commençons !

## Comment accéder à l'API de géolocalisation

Les navigateurs implémentent l'API de géolocalisation dans l'objet `navigator.geolocation`. Vous pouvez vérifier si le navigateur que vous utilisez prend en charge cette API comme suit :

```js
if ('geolocation' in navigator) {
  console.log('La géolocalisation est disponible');
} else {
  console.log('La géolocalisation n\'est PAS disponible');
}

```

Si le navigateur répond avec 'La géolocalisation est disponible', alors vous pouvez utiliser les méthodes de l'objet `geolocation` pour obtenir les données de l'utilisateur.

L'API de géolocalisation n'est disponible que dans un contexte sécurisé HTTPS, mais les navigateurs modernes comme Chrome et Firefox permettent l'accès à cette API depuis localhost à des fins de développement.

Il existe deux méthodes que vous pouvez utiliser pour obtenir les données de l'utilisateur :

* `getCurrentPosition()` : Retourne la position actuelle de l'appareil.
* `watchPosition()` : Observe la position de l'appareil en continu jusqu'à ce que l'observateur soit arrêté.

Les deux méthodes ci-dessus reçoivent 3 arguments comme suit :

* `success` : une fonction de rappel pour lorsque les données de géolocalisation sont récupérées (requis).
* `error` : une fonction de rappel pour lorsque la méthode rencontre une erreur (optionnel).
* `options` : un objet définissant des paramètres supplémentaires lors de l'exécution de la méthode (optionnel).

Lorsque l'API de géolocalisation est accédée pour la première fois, une demande de permission apparaîtra près de la barre d'URL comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/geolocation-permission.png)
_Demande de permission pour accéder à la position de l'utilisateur_

Vous êtes peut-être familier avec la fenêtre contextuelle ci-dessus. Lorsque vous choisissez de bloquer la demande, la fonction de rappel `error` sera exécutée par l'API.

Sinon, la fonction de rappel `success` sera exécutée.

## Comment obtenir la position actuelle de l'utilisateur

Pour obtenir la position actuelle de l'utilisateur, vous pouvez appeler la méthode `getCurrentPosition()` de l'objet `navigator.geolocation` comme montré ci-dessous :

```js
function success(position) {
  console.log(position);
}

navigator.geolocation.getCurrentPosition(success);

```

La méthode `getCurrentPosition()` enverra l'objet `position` à la fonction `success()` ci-dessus.

L'objet `position` contient les coordonnées de localisation et un horodatage indiquant quand la localisation a été récupérée.

Voici un exemple de l'objet `position` :

```js
{
  coords: {
    latitude: 1.314,
    longitude: 103.84425
    altitude: null
  },
  timestamp: 1708674456885
}

```

En utilisant les informations de latitude et de longitude, vous pouvez localiser la position de l'utilisateur et fournir des informations et des services pertinents.

Par exemple, voyons comment vous pouvez envoyer une demande au site [OpenStreetMap](https://www.openstreetmap.org/) et épingler la position actuelle de l'utilisateur en utilisant les données de l'API de géolocalisation.

OpenStreetMap est un projet open source fournissant une carte géographique libre de la Terre entière.

Vous devez créer un document HTML avec le contenu du corps suivant :

```html
<body>
  <button id="getLocation">Obtenir la position</button>
  <br>
  <a id="locationResult" target="_blank"></a>
</body>

```

Lorsque l'utilisateur clique sur le bouton _Obtenir la position_ ci-dessus, nous accéderons à l'API de géolocalisation, récupérerons la position de l'utilisateur et fournirons un lien pour voir la position de l'utilisateur sur une carte.

Ensuite, créez une balise `<script>` avant la balise de fermeture `</body>` et écrivez le code JavaScript suivant :

```html
<script>
  const locationResult = document.querySelector('#locationResult');
  document.querySelector('#getLocation').addEventListener('click', () => {
    locationResult.textContent = 'Récupération de la position de l\'utilisateur...'

    function success(position) {
      let { coords } = position;
      locationResult.textContent = 'Voir ma position sur une carte';
      locationResult.href = `https://www.openstreetmap.org?mlat=${coords.latitude}&mlon=${coords.longitude}`;
    }

    navigator.geolocation.getCurrentPosition(success);
  });
</script>

```

Lorsque le bouton est cliqué, nous exécuterons la méthode `getCurrentPosition()` et définirons l'attribut `href` de la balise `<a>` sur le site OpenStreetMap, en transmettant les données `latitude` et `longitude` sous les paramètres de requête `mlat` et `mlon`.

Visiter le lien montrerait une carte de la position actuelle comme montré ci-dessous :

![OpenStreetMap utilisant les données de l'API de géolocalisation](https://www.freecodecamp.org/news/content/images/2024/02/geolocation-getCurrentPosition.png)
_Le site OpenStreetMap épingle les données de latitude et de longitude_

Et c'est ainsi que vous obtenez la position actuelle de l'utilisateur. La façon de traiter les informations de position vous appartient.

J'ai créé un site web où vous pouvez tester cette fonctionnalité à l'adresse [https://nathansebhastian.github.io/js-geolocation-api/](https://nathansebhastian.github.io/js-geolocation-api/)

Ensuite, apprenons à utiliser la méthode `watchPosition()`.

## Comment surveiller la position de l'utilisateur

La méthode `watchPosition()` continuera à surveiller la position de l'appareil lorsqu'elle est appelée. Elle exécutera la fonction de rappel `success` chaque fois que la position de l'appareil change.

Vous pouvez appeler la méthode comme suit :

```js
function success(position) {
  const { coords } = position;
  console.log('Données de latitude : ' + coords.latitude);
  console.log('Données de longitude : ' + coords.longitude);
}

navigator.geolocation.watchPosition(success);

```

La méthode `watchPosition()` retourne un numéro d'identification qui suit l'observateur. Si vous souhaitez arrêter l'observateur d'envoyer des données de position, vous devez appeler la méthode `clearWatch()` et passer le numéro d'identification :

```js
function success(position) {
  const { coords } = position;
  console.log('Données de latitude : ' + coords.latitude);
  console.log('Données de longitude : ' + coords.longitude);
}

// Stockez le numéro d'identification dans une variable
const watcherID = navigator.geolocation.watchPosition(success);

// Arrêtez l'observateur
navigator.geolocation.clearWatch(watcherID);

```

Et c'est tout ce qu'il y a à savoir sur la méthode `watchPosition()`.

### Comment ajouter l'objet Options

Ensuite, examinons l'objet `options` optionnel que vous pouvez passer aux méthodes `getCurrentPosition()` et `watchPosition()`.

L'objet `options` vous permet de personnaliser le comportement des méthodes. Il y a trois options que vous pouvez définir :

* `enableHighAccuracy` : une valeur booléenne qui indique à la méthode de fournir une position plus précise. Cela augmentera la consommation d'énergie. La valeur par défaut est `false`.
* `timeout` : une valeur numérique représentant la durée pendant laquelle la méthode attend une réponse. La valeur par défaut est `Infinity`, ce qui signifie que la méthode attendra jusqu'à ce qu'une position soit disponible.
* `maximumAge` : une valeur numérique représentant la durée pendant laquelle l'API de géolocalisation peut envoyer les données de position précédentes. La valeur par défaut est `0`, donc l'API retourne toujours la dernière position. Si elle est définie sur `Infinity`, alors l'API retournera toujours les premières données de position récupérées.

Vous pouvez utiliser l'objet options lors de l'appel des méthodes `geolocation`.

Par exemple :

```js
const options = {
  enableHighAccuracy: true, // activer la haute précision
  timeout: 300000, // attendre 5 minutes
};

function success(position) {
  console.log(position);
}

function error(error) {
  console.log(error);
}

// Exécutez la méthode getCurrentPosition() avec des options personnalisées
navigator.geolocation.getCurrentPosition(
  success,
  error,
  options
);

```

Dans le code ci-dessus, la méthode `getCurrentPosition()` utilisera le mode haute précision et attendra 5 minutes pour une réponse de l'appareil.

## Résumé

L'API de géolocalisation est une API JavaScript standard qui permet à une application web d'accéder aux données de position de l'utilisateur.

En utilisant les données de géolocalisation, vous pouvez fournir des services ou du contenu pertinent par rapport à la position de l'utilisateur, tels que les transports publics ou l'hôpital le plus proche.

Si vous avez aimé cet article et souhaitez en apprendre davantage de moi, je vous recommande de consulter mon nouveau livre _[Beginning Modern JavaScript](https://codewithnathan.com/beginning-modern-javascript)_.

[![Beginning Modern JavaScript](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif pour vous aider à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À bientôt dans d'autres articles !