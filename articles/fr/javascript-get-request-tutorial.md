---
title: JavaScript Get Request – Comment faire une requête HTTP en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-15T19:05:24.000Z'
originalURL: https://freecodecamp.org/news/javascript-get-request-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--2-.png
tags:
- name: api
  slug: api
- name: axios
  slug: axios
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: JavaScript Get Request – Comment faire une requête HTTP en JS
seo_desc: 'When building applications, you will have to interact between the backend
  and frontend to get, store, and manipulate data.

  This interaction between your frontend application and the backend server is possible
  through HTTP requests.

  There are five pop...'
---

Lors de la création d'applications, vous devrez interagir entre le backend et le frontend pour obtenir, stocker et manipuler des données.

Cette interaction entre votre application frontend et le serveur backend est possible grâce aux requêtes HTTP.

Il existe cinq méthodes HTTP populaires que vous pouvez utiliser pour faire des requêtes et interagir avec vos serveurs. L'une de ces méthodes est la méthode GET, qui permet de récupérer des données depuis votre serveur.

Cet article vous apprendra à demander des données depuis vos serveurs en effectuant une requête GET. Vous apprendrez les méthodes populaires qui existent actuellement ainsi que quelques autres méthodes alternatives.

Pour ce guide, nous récupérerons des posts depuis l'API gratuite [JSON Placeholder posts API](https://jsonplaceholder.typicode.com/posts).

Il existe deux méthodes populaires que vous pouvez facilement utiliser pour faire des requêtes HTTP en JavaScript. Il s'agit de l'API Fetch et d'Axios.

## Comment faire une requête GET avec l'API Fetch

L'API Fetch est une méthode JavaScript intégrée pour récupérer des ressources et interagir avec votre serveur backend ou un point de terminaison d'API. L'API Fetch est intégrée et ne nécessite pas d'installation dans votre projet.

L'API Fetch accepte un argument obligatoire : le point de terminaison/URL de l'API. Cette méthode accepte également un argument **option**, qui est un objet facultatif lors de l'envoi d'une requête GET **car c'est la requête par défaut**.

```js
  fetch(url, {
      method: "GET" // par défaut, donc nous pouvons l'ignorer
  })
```

Créons une requête GET pour obtenir un post depuis l'API [JSON Placeholder posts API](https://jsonplaceholder.typicode.com/posts).

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => response.json())
  .then((json) => console.log(json));
```

Cela retournera un seul post que vous pouvez maintenant stocker dans une variable et utiliser dans votre projet.

> Note : Pour d'autres méthodes, telles que POST et DELETE, vous devez attacher la méthode à l'objet d'options.

## Comment faire une requête GET avec Axios

Axios est une bibliothèque cliente HTTP. Cette bibliothèque est basée sur les promesses qui simplifient l'envoi de requêtes HTTP asynchrones aux points de terminaison REST. Nous allons envoyer une requête GET au point de terminaison de l'API JSONPlaceholder Posts.

Contrairement à l'API Fetch, Axios n'est pas intégré. Cela signifie que vous devez installer Axios dans votre projet JavaScript.

Pour installer une dépendance dans votre projet JavaScript, vous devez d'abord initialiser un nouveau projet `npm` en exécutant la commande suivante dans votre terminal :

```js
$ npm init -y
```

Et maintenant, vous pouvez installer Axios dans votre projet en exécutant la commande suivante :

```js
$ npm install axios
```

Une fois Axios installé avec succès, vous pouvez créer votre requête GET. Cela est assez similaire à la requête de l'API Fetch. Vous passerez le point de terminaison/URL de l'API à la méthode `get()`, qui retournera une promesse. Vous pouvez ensuite gérer la promesse avec les méthodes `.then()` et `.catch()`.

```js
axios.get("https://jsonplaceholder.typicode.com/posts/1")
.then((response) => console.log(response.data))
.catch((error) => console.log(error));
```

> **Note :** La principale différence est que, pour l'API Fetch, vous devez d'abord convertir les données en JSON, tandis qu'Axios retourne vos données directement en tant que données JSON.

À ce stade, vous avez appris à faire une requête HTTP GET avec l'API Fetch et Axios. Mais il existe d'autres méthodes qui existent encore. Certaines de ces méthodes sont [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) et jQuery.

## Comment faire une requête GET avec `XMLHttpRequest`

Vous pouvez utiliser l'objet XMLHttpRequest pour interagir avec les serveurs. Cette méthode peut demander des données depuis un point de terminaison/URL d'API de serveur web sans effectuer un rafraîchissement complet de la page.

> **Note :** Tous les navigateurs modernes ont un objet XMLHttpRequest intégré pour demander des données depuis un serveur.

Effectuons la même requête avec XMLHttpRequest en créant un nouvel objet XMLHttpRequest. Vous ouvrirez ensuite une connexion en spécifiant le type de requête et le point de terminaison (l'URL du serveur), puis vous enverrez la requête, et enfin vous écouterez la réponse du serveur.

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://jsonplaceholder.typicode.com/posts/1");
xhr.send();
xhr.responseType = "json";
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    console.log(xhr.response);
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
```

Dans le code ci-dessus, un nouvel objet XMLHttpRequest est créé et stocké dans une variable appelée `xhr`. Vous pouvez maintenant accéder à tous ses objets en utilisant la variable, comme la méthode `.open()`, lorsque vous spécifiez le type de requête (GET) et le point de terminaison/URL où vous souhaitez demander des données.

Une autre méthode que vous utiliserez est `.send()`, qui envoie la requête au serveur. Vous pouvez également spécifier le format dans lequel les données seront retournées en utilisant la méthode `responseType`. À ce stade, la requête GET est envoyée, et tout ce que vous avez à faire est d'écouter sa réponse en utilisant l'écouteur d'événement `onload`.

Si l'état du client est terminé (**4**), et que le code de statut est réussi (**200**), alors les données seront enregistrées dans la console. Sinon, un message d'erreur indiquant le statut de l'erreur apparaîtra.

## Comment faire une requête GET avec jQuery

Faire des requêtes HTTP en jQuery est relativement simple et similaire à l'API Fetch et Axios. Pour faire une requête GET, vous devez d'abord installer jQuery ou utiliser son CDN dans votre projet :

```js
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.2/jquery.min.js" integrity="sha512-tWHlutFnuG0C6nQRlpvrEhE4QpkG1nn2MOUMWmUeRePl4e3Aki0VB6W1v3oLjFtd0hVOtRQ9PHpSfN6u6/QXkQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

Avec jQuery, vous pouvez accéder à la méthode GET `$.get()`, qui prend deux paramètres, le point de terminaison/URL de l'API et une fonction de rappel qui s'exécute lorsque la requête est réussie.

```js
$.get("https://jsonplaceholder.typicode.com/posts/1", (data, status) => {
  console.log(data);
});
```

> **Note :** Dans la fonction de rappel, vous avez accès aux **data** de la requête et au **status** de la requête.

Vous pouvez également utiliser la méthode AJAX de jQuery, qui est assez différente et peut être utilisée pour faire des requêtes asynchrones :

```js
$.ajax({
  url: "https://jsonplaceholder.typicode.com/posts/1",
  type: "GET",
  success: function (data) {
    console.log(data);
  }
});
```

## Conclusion

Dans cet article, vous avez appris à faire une requête HTTP GET en JavaScript. Vous pourriez maintenant commencer à vous demander — quelle méthode devrais-je utiliser ?

Si c'est un nouveau projet, vous pouvez choisir entre l'API Fetch et Axios. De plus, si vous souhaitez consommer des API basiques pour un petit projet, il n'est pas nécessaire d'utiliser Axios, qui demande d'installer une bibliothèque.

Amusez-vous bien à coder !