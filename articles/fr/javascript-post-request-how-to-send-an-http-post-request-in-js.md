---
title: Requête POST JavaScript – Comment envoyer une requête HTTP POST en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-06T23:40:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--7-.png
tags:
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: Requête POST JavaScript – Comment envoyer une requête HTTP POST en JS
seo_desc: 'HTTP requests allow your front-end application to interact successfully
  with a back-end server or database.

  One of the five popular HTTP methods for making requests and interacting with your
  servers is the POST method, which you can use to send data ...'
---

Les requêtes HTTP permettent à votre application front-end d'interagir avec succès avec un serveur back-end ou une base de données.

L'une des cinq méthodes HTTP populaires pour faire des requêtes et interagir avec vos serveurs est la méthode POST, que vous pouvez utiliser pour envoyer des données à un serveur.

Dans cet article, vous apprendrez les différentes méthodes que vous pouvez utiliser pour envoyer une requête HTTP POST à votre serveur back-end en JavaScript. Nous enverrons des requêtes GET à l'API [free JSON Placeholder todos](https://jsonplaceholder.typicode.com/todos) pour ce guide.

Il existe deux méthodes JavaScript intégrées pour faire une requête HTTP POST qui ne nécessitent pas l'installation d'une bibliothèque ou l'utilisation d'un CDN. Ces méthodes sont le FetchAPI, basé sur les promesses JavaScript, et XMLHttpRequest, basé sur les callbacks.

Il existe d'autres méthodes, telles que Axios et jQuery, que vous apprendrez également à utiliser.

## Comment envoyer une requête POST avec le Fetch API

Le FetchAPI est une méthode intégrée qui prend un paramètre obligatoire : le endpoint (URL de l'API). Bien que les autres paramètres ne soient pas nécessaires pour une requête GET, ils sont très utiles pour la requête HTTP POST.

Le deuxième paramètre est utilisé pour définir le corps (données à envoyer) et le type de requête à envoyer, tandis que le troisième paramètre est l'en-tête qui spécifie le type de données que vous allez envoyer, par exemple JSON.

```js
fetch("https://jsonplaceholder.typicode.com/todos", {
  method: "POST",
  body: JSON.stringify({
    userId: 1,
    title: "Corriger mes bugs",
    completed: false
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});
```

Dans le code ci-dessus, le corps contient les données à envoyer au serveur et à ajouter à l'API JSONPlaceholder todos. De plus, les en-têtes contiennent le type de contenu que vous souhaitez envoyer au serveur, qui dans ce cas est des données JSON.

**Note :** Il est toujours préférable de sérialiser vos données avant de les envoyer à un serveur web ou à une API en utilisant la méthode **JSON.stringify()**. Cela aidera à convertir et à garantir que vos données JSON sont au format chaîne.

Le Fetch API est basé sur les promesses JavaScript, vous devez donc utiliser la méthode .then pour accéder à la promesse ou à la réponse retournée.

```js
fetch("https://jsonplaceholder.typicode.com/todos", {
  method: "POST",
  body: JSON.stringify({
    userId: 1,
    title: "Corriger mes bugs",
    completed: false
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

Si cela réussit, il retournera les nouvelles données JSON que vous envoyez au serveur.

## Comment envoyer une requête POST avec `XMLHttpRequest`

Comme le Fetch API, `XMLHttpRequest` est également intégré et existe depuis beaucoup plus longtemps que le Fetch API. Cela signifie que presque tous les navigateurs modernes ont un objet XMLHttpRequest intégré pour demander des données à un serveur.

Vous commenerez par créer un nouvel objet XMLHttpRequest stocké dans une variable appelée `xhr`. Cela est important car cela vous donne accès à tous ses objets en utilisant la variable.

Par exemple, vous pouvez ensuite ouvrir une connexion avec `.open()`, qui est utilisé pour spécifier le type de requête et le endpoint (l'URL du serveur). Comme vous l'avez fait pour le FetchAPI, vous spécifierez le type de données en utilisant la méthode `setRequestHeader`.

```js
const xhr = new XMLHttpRequest();
xhr.open("POST", "https://jsonplaceholder.typicode.com/todos");
xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
```

L'étape suivante consiste à créer les données à envoyer au serveur. Assurez-vous de sérialiser les données et de les stocker dans une variable que vous enverrez avec la méthode `.send()` après avoir effectué quelques vérifications avec la méthode `.onload`.

```js
const body = JSON.stringify({
  userId: 1,
  title: "Corriger mes bugs",
  completed: false
});
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 201) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.log(`Erreur: ${xhr.status}`);
  }
};
xhr.send(body);
```

Lorsque vous assemblez le code, il ressemblera à ceci et retournera les données JSON que vous envoyez au serveur :

```js
const xhr = new XMLHttpRequest();
xhr.open("POST", "https://jsonplaceholder.typicode.com/todos");
xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
const body = JSON.stringify({
  userId: 1,
  title: "Corriger mes bugs",
  completed: false
});
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 201) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.log(`Erreur: ${xhr.status}`);
  }
};
xhr.send(body);
```

La principale différence entre le Fetch API et la méthode `XMLHttpRequest` est que le Fetch API a une meilleure syntaxe qui est plus facile à lire et à comprendre.

À ce stade, vous avez appris à utiliser les deux méthodes intégrées de JavaScript pour envoyer des requêtes HTTP POST. Apprenons maintenant à utiliser Axios et jQuery.

## Comment envoyer une requête POST avec Axios

Axios est une bibliothèque cliente HTTP. Cette bibliothèque est basée sur des promesses qui simplifient l'envoi de requêtes HTTP asynchrones aux endpoints REST. Nous enverrons une requête GET à l'endpoint de l'API JSONPlaceholder Posts.

Contrairement au Fetch API et à `XMLHttpRequest`, Axios n'est pas intégré. Cela signifie que vous devez installer Axios dans votre projet JavaScript.

Pour installer une dépendance dans votre projet JavaScript, vous devez d'abord initialiser un nouveau projet `npm` en exécutant la commande suivante dans votre terminal :

```bash
$ npm init -y
```

Et maintenant, vous pouvez installer Axios dans votre projet en exécutant la commande suivante :

```bash
$ npm install axios
```

Une fois Axios installé avec succès, vous pouvez envoyer votre requête POST. Cela est assez similaire à la requête Fetch API.

Vous passerez le endpoint/URL de l'API à la méthode `post()`, qui retournera une promesse. Vous pouvez ensuite gérer la promesse avec les méthodes `.then()` et `.catch()`.

```js
axios.post("https://jsonplaceholder.typicode.com/todos", {
    userId: 1,
    title: "Corriger mes bugs",
    completed: false
  })
  .then((response) => console.log(response.data))
  .then((error) => console.log(error));
```

**Note :** Axios sérialisera automatiquement l'objet en JSON et définira l'en-tête Content-Type sur 'application/json' pour vous.

Cela retournera les nouvelles données envoyées au serveur.

## Comment envoyer une requête POST avec jQuery

Faire une requête HTTP en jQuery est similaire au Fetch API et à Axios, mais jQuery n'est pas intégré. Vous devrez donc d'abord l'installer ou utiliser son CDN dans votre projet :

```js
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.2/jquery.min.js" integrity="sha512-tWHlutFnuG0C6nQRlpvrEhE4QpkG1nn2MOUMWmUeRePl4e3Aki0VB6W1v3oLjFtd0hVOtRQ9PHpSfN6u6/QXkQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

Avec jQuery, vous pouvez accéder à la méthode POST `$.post()`, qui prend trois paramètres : le endpoint/URL de l'API, les données à envoyer au serveur et une fonction de callback qui s'exécute lorsque la requête est réussie.

```js
const body = {
  userId: 1,
  title: "Corriger mes bugs",
  completed: false
};
$.post("https://jsonplaceholder.typicode.com/todos", body, (data, status) => {
  console.log(data);
});
```

**Note :** Vous pouvez accéder aux données et au statut de la requête dans la fonction de callback.

Vous pouvez consulter [cet article similaire sur comment faire une requête HTTP GET en JavaScript](https://www.freecodecamp.org/news/javascript-get-request-tutorial/).

## Conclusion

Dans cet article, vous avez appris comment envoyer une requête HTTP POST en JavaScript. Vous pourriez maintenant commencer à penser — quelle méthode devrais-je utiliser ?

Vous pouvez choisir entre le Fetch API et Axios si c'est un nouveau projet. De plus, si vous souhaitez consommer des API basiques pour un petit projet, Axios est optionnel car il nécessite l'installation d'une bibliothèque.

Amusez-vous bien à coder !

Vous pouvez accéder à plus de 150 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.