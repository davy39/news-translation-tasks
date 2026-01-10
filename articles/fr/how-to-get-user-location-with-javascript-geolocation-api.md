---
title: Tutoriel sur l'API de géolocalisation JavaScript – Comment obtenir la localisation
  d'un utilisateur en JS
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-09-07T18:29:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-user-location-with-javascript-geolocation-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Blog-article-cover-images--4
seo_title: Tutoriel sur l'API de géolocalisation JavaScript – Comment obtenir la localisation
  d'un utilisateur en JS
---

1-.png
étiquettes:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Programmation générale
  slug: programming
- name: Développement web
  slug: web-development
seo_title: null
seo_desc: 'Certaines applications nécessitent de connaître la localisation de vos utilisateurs, comme les applications de livraison de nourriture ou de commerce électronique. Vous aurez donc besoin d''un moyen efficace d''obtenir ces informations.

L''API de géolocalisation, que nous allons examiner aujourd''hui, est une solution simple. Vous pouvez l''utiliser pour déterminer la localisation de vos utilisateurs, leur monnaie locale, leur langue et d''autres informations utiles. Vous pouvez ensuite utiliser ces informations pour leur fournir le contenu le plus pertinent en fonction de leur localisation.

Dans cet article, nous allons passer en revue ce qu''est l''API de géolocalisation, pourquoi elle est utile et comment l''utiliser dans vos applications.

## Qu''est-ce que l''API de géolocalisation ?

L''API de géolocalisation JavaScript fournit un accès aux données de localisation géographique associées à l''appareil d''un utilisateur. Cela peut être déterminé en utilisant le GPS, le WIFI, la géolocalisation IP, etc.

Pour protéger la vie privée de l''utilisateur, elle demande la permission de localiser l''appareil. Si l''utilisateur accorde la permission, vous aurez accès aux données de localisation telles que la latitude, la longitude, l''altitude et la vitesse. Vous obtiendrez également la précision des données de localisation acquises et l''heure approximative à laquelle la position a été acquise.

Voici quelques utilisations de la géolocalisation :

* Afficher la position de l''utilisateur sur une carte

* Obtenir des informations locales à jour

* Afficher les points d''intérêt (POI) locaux près de l''utilisateur

* Activer la navigation pas à pas (GPS)

* Suivre une flotte ou un véhicule de livraison

* Taguer des photographies avec une localisation

## Comment utiliser l''API de géolocalisation

Vous pouvez accéder à l''API de géolocalisation en appelant l''objet `navigator.geolocation`. Il accorde à l''application l''accès à la localisation de l''appareil.

Cet objet fournit les méthodes listées ci-dessous pour travailler avec la position de l''appareil :

1. getCurrentPosition : Retourne la localisation actuelle de l''appareil.

2. watchPosition : Une fonction de gestion qui est automatiquement invoquée lorsque la localisation de l''appareil change.

Il y a trois arguments possibles avec ces méthodes :

* Une fonction de rappel de succès (requise)

* Une fonction de rappel d''erreur (optionnelle)

* Un objet d''options (optionnel)

### Comment obtenir la localisation de l''utilisateur avec `getCurrentPosition()`

Vous pouvez utiliser la méthode `getCurrentPosition` pour obtenir la localisation actuelle de l''utilisateur. Elle envoie une requête asynchrone au navigateur, demandant le consentement pour partager leur localisation.

Voici la syntaxe pour obtenir la localisation d''un utilisateur :

```js
const successCallback = (position) => {
  console.log(position);
};

const errorCallback = (error) => {
  console.log(error);
};

navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
```

Lorsque vous exécutez cela, vous obtiendrez une fenêtre contextuelle dans le navigateur demandant la permission :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/popup.PNG align="left")

Cliquez sur **Autoriser**, et ouvrez la console de développement. Vous verrez que l''appel réussi retourne deux choses :

1. L''objet `GeolocationPosition.coords` : représente la position, l''altitude et la précision avec laquelle l''appareil calcule ces propriétés.

2. `timestamp` : représente l''heure à laquelle la localisation a été obtenue.

Vous devriez voir quelque chose comme ceci dans votre console :

```plaintext
GeolocationPosition {coords: GeolocationCoordinates, timestamp: 1662499816712}
    coords: GeolocationCoordinates
        accuracy: 7173.528443511279
        altitude: null
        altitudeAccuracy: null
        heading: null
        latitude: 6.5568768
        longitude: 3.3488896
        speed: null
        [[Prototype]]: GeolocationCoordinates
timestamp: 1662499816712
```

Avec cette simple requête, nous avons réussi à obtenir la localisation. Mais ce n''est pas tout. Nous pouvons également suivre l''utilisateur en surveillant sa localisation.

### Comment suivre la localisation de l''utilisateur avec `watchPosition()`

La méthode `watchPosition()` permet à l''application de suivre en continu l''utilisateur et d''être mise à jour lorsque sa position change. Elle le fait en installant une fonction de gestion qui sera appelée automatiquement chaque fois que la position de l''appareil de l''utilisateur change.

Voici la syntaxe ci-dessous, où `id` est essentiellement utilisé pour gérer ou référencer la méthode :

```js
const id = navigator.geolocation.watchPosition(successCallback, errorCallback);
```

### Comment arrêter de suivre la position avec `clearWatch()`

Nous utilisons la méthode `clearWatch()` pour annuler les fonctions de gestion qui ont été précédemment installées en utilisant `watchPosition`.

```js
navigator.geolocation.clearWatch(id);
```

### Comment utiliser l''objet `options`

Bien que l''objet [`options`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition#parameters) soit optionnel, il fournit des paramètres qui peuvent vous aider à obtenir des résultats plus précis, par exemple :

```js
const options = {
  enableHighAccuracy: true,
  timeout: 10000,
};

navigator.geolocation.getCurrentPosition(
  successCallback,
  errorCallback,
  options
);
```

Dans le code ci-dessus, nous avons spécifié dans notre objet d''options que :

* La réponse doit fournir une position plus précise, en définissant enableHighAccuracy sur true.

* La durée maximale (en millisecondes) pendant laquelle l''appareil est autorisé à prendre pour retourner une position. Dans ce cas, 10 secondes.

## Conclusion

Dans cet article, nous avons appris à connaître l''API de géolocalisation JavaScript, comment l''utiliser pour obtenir la localisation d''un utilisateur et également suivre l''utilisateur en utilisant la méthode watchPosition().

Vous pouvez aller plus loin en explorant cette API en construisant une application météo, une application de recherche ou une application de carte. Merci d''avoir lu !'