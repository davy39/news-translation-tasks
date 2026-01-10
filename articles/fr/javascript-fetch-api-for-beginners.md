---
title: API Fetch JavaScript pour débutants – Expliqué avec des exemples de code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-02-23T12:14:53.000Z'
originalURL: https://freecodecamp.org/news/javascript-fetch-api-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/javascript-fetch-cover.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: API Fetch JavaScript pour débutants – Expliqué avec des exemples de code
seo_desc: 'The Fetch API is a JavaScript function that you can use to send a request
  to any Web API URL and get a response.

  In this article, I''m going to show you how to make HTTP requests to external APIs
  using the JavaScript Fetch API. You''re going to learn h...'
---

L'API Fetch est une fonction JavaScript que vous pouvez utiliser pour envoyer une requête à n'importe quelle URL d'API Web et obtenir une réponse.

Dans cet article, je vais vous montrer comment faire des requêtes HTTP vers des API externes en utilisant l'API Fetch JavaScript. Vous allez apprendre à créer des requêtes GET, POST, PUT/PATCH et DELETE en utilisant l'API Fetch.

Pour tirer le meilleur parti de cet article, vous devez avoir une bonne compréhension des promesses JavaScript. Vous pouvez lire mon article sur les [Promesses JavaScript](https://www.freecodecamp.org/news/javascript-promise-object-explained/) si vous avez besoin d'un rappel.

- [Comment fonctionne l'API Fetch](#heading-comment-fonctionne-lapi-fetch)
- [Comment envoyer une requête GET](#heading-comment-envoyer-une-requete-get)
- [Comment envoyer une requête POST](#heading-comment-envoyer-une-requete-post)
- [Comment envoyer une requête PUT](#heading-comment-envoyer-une-requete-put)
- [Comment envoyer une requête PATCH](#heading-comment-envoyer-une-requete-patch)
- [Comment envoyer une requête DELETE](#heading-comment-envoyer-une-requete-delete)
- [Comment utiliser Async/Await avec l'API Fetch](#heading-comment-utiliser-asyncawait-avec-lapi-fetch)
- [Exécuter des exemples de code](#heading-executer-des-exemples-de-code)
- [Résumé](#heading-resume)

Commençons !

## Comment fonctionne l'API Fetch

Pour envoyer une requête similaire à celle d'un formulaire HTML, vous devez simplement passer l'URL où vous souhaitez envoyer les données en tant qu'argument à la fonction `fetch()` :

```js
fetch('<Votre URL>', {})

```

La fonction `fetch()` accepte deux paramètres :

1. L'URL à laquelle envoyer la requête (ceci est un paramètre obligatoire).
2. Les options à définir dans la requête. Vous pouvez définir la méthode de requête ici (ceci est un paramètre facultatif).

En coulisses, la fonction `fetch()` retourne une `Promise`, vous devez donc ajouter les méthodes `.then()` et `.catch()`.

Lorsque la requête retourne une réponse, la méthode `then()` sera appelée. Si la requête retourne une erreur, alors la méthode `catch()` sera exécutée :

```js
fetch('<Votre URL>', {})
  .then(response => {
    // Gérer la réponse Fetch ici.
  })
  .catch(error => {
    // En cas d'erreur, la gérer ici
  })
```

À l'intérieur des méthodes `.then()` et `.catch()`, vous passez une fonction de rappel à exécuter lorsque les méthodes respectives sont appelées.

La méthode `.catch()` peut être omise de l'API Fetch. Elle n'est utilisée que lorsque Fetch ne peut pas faire de requête à l'API, comme en cas de non-connexion au réseau ou d'URL introuvable.

## Comment envoyer une requête GET avec l'API Fetch

La requête GET est une requête HTTP utilisée pour demander des données spécifiques à une API, par exemple lorsque vous avez besoin de données.

Dans l'exemple suivant, nous allons interroger une URL fictive située à https://jsonplaceholder.typicode.com pour demander un utilisateur enregistré sur le site :

```js
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => console.log(response))
  .catch(error => console.log(error));

```

Le code ci-dessus donnera la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/fetch-readable-stream.png)
_Réponse de la requête Fetch_

Ici, vous pouvez voir que la propriété body contient un `ReadableStream`. Pour utiliser le `ReadableStream` dans notre application JavaScript, nous devons le convertir en appelant la méthode `json()` :

```js
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => response.json())
  .then(data => console.log(data))

```

La méthode `json()` convertit le `ReadableStream` en un objet JavaScript. La variable `data` ci-dessus sera imprimée comme suit :

```js
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
```

Maintenant que vous avez l'objet `data`, vous pouvez utiliser cette valeur de la manière que vous souhaitez. Par exemple, si vous souhaitez afficher le nom et l'email de l'utilisateur en HTML, voici comment faire :

```html
<body>
  <h1 id='user-name'>En attente de données</h1>
  <h2 id='user-email'>En attente de données</h1>
  <script>
    fetch('https://jsonplaceholder.typicode.com/users/1')
      .then(response => response.json())
      .then(data => {
        document.querySelector('#user-name').textContent = data.name
        document.querySelector('#user-email').textContent = data.email
      })
  </script>
</body>

```

Dans le code ci-dessus, l'API Fetch s'exécutera dès que le navigateur chargera le document HTML.

Après avoir traité la `response` en un objet `data`, JavaScript changera le texte des éléments `<h1>` et `<h2>` ci-dessus pour refléter le `name` et l'`email` de l'utilisateur.

Si vous exécutez le code ci-dessus, vous obtiendrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/fetch-get-response.png)
_La sortie de la requête Fetch affichée dans le navigateur_

Et c'est ainsi que vous envoyez une requête GET en utilisant Fetch et affichez les données retournées en HTML.

Notez que selon la requête que vous demandez, une API peut retourner un type de données différent.

Dans cet exemple, l'API typicode envoie un objet, mais vous pourriez également obtenir un tableau lorsque vous demandez plus d'une unité de données.

Si vous accédez à l'URL [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users), vous verrez que l'API répond avec un tableau d'objets.

Pour gérer un tableau d'objets, vous pouvez itérer sur le tableau et afficher les données en HTML comme suit :

```js
// exemple
```

Vous devez connaître le type de données retourné par l'API pour le gérer correctement.

## Comment envoyer une requête POST avec l'API Fetch

Si vous souhaitez envoyer une requête POST au lieu d'une requête GET, vous devez définir le deuxième argument lors de l'appel de la fonction, qui est l'objet d'options.

À l'intérieur de l'objet d'options, définissez une propriété `method` comme suit :

```js
fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST', // Définir la méthode ici
})
.then(response => response.json())
.then(data => console.log(data))

```

Lorsque vous envoyez une méthode POST, vous devez définir les propriétés d'en-tête et de corps de la requête pour garantir un processus fluide.

Pour l'en-tête, vous devez ajouter la propriété `Content-Type` et la définir sur `application/json`.

Les données que vous souhaitez envoyer doivent être placées à l'intérieur de la propriété `body` au format JSON. Voir l'exemple ci-dessous :

```js
fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'Nathan Sebhastian',
    email: 'ns@mail.com'
  }),
}).then(response => response.json())
  .then(data => console.log(data))
```

Dans l'exemple ci-dessus, nous avons envoyé une requête POST pour créer un nouvel utilisateur. Dans la propriété `body`, un objet JavaScript régulier a été converti en une chaîne JSON en appelant la méthode `JSON.stringify()`.

JSON est l'un des formats que les ordinateurs utilisent pour communiquer entre eux sur Internet.

La réponse de l'API typicode.com serait similaire à ce qui suit :

```js
{
  "name": "Nathan Sebhastian",
  "email": "ns@mail.com",
  "id": 11
}
```

Cela signifie que nous avons réussi à créer un nouvel utilisateur. Puisque typicode.com est une fausse API, l'utilisateur ne sera pas vraiment ajouté, mais il fera semblant.

## Comment envoyer une requête PUT

Une requête PUT est utilisée pour créer une nouvelle ressource ou mettre à jour une ressource existante.

Par exemple, si vous souhaitez mettre à jour les données `name` et `email` d'un utilisateur existant. Vous pouvez utiliser une requête PUT pour ce faire :

```js
fetch('https://jsonplaceholder.typicode.com/users/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'Nathan Sebhastian',
    email: 'nathan@mail.com'
  }),
}).then(response => response.json())
  .then(data => console.log(data))
```

La requête ci-dessus recevra la réponse suivante :

```js
{
    "name": "Nathan Sebhastian",
    "email": "nathan@mail.com",
    "id": 1
}
```

Parce que les données utilisateur avec une valeur `id` de 1 existent déjà, la requête PUT ci-dessus met à jour ces données.

Ensuite, examinons la requête PATCH.

## Comment envoyer une requête PATCH

La requête PATCH est envoyée lorsque vous devez mettre à jour une requête existante.

Par exemple, si vous souhaitez modifier les données `name` et `username` d'un utilisateur existant.

Voici un exemple d'envoi d'une requête PATCH à typicode.com :

```js
fetch('https://jsonplaceholder.typicode.com/users/1', {
  method: 'PATCH',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ 
    name: 'Nathan Sebhastian',
    username: 'nsebhastian'
  }),
}).then(response => response.json())
  .then(data => console.log(data))
```

La requête ci-dessus donnera la réponse suivante :

```js
{
    "id": 1,
    "name": "Nathan Sebhastian",
    "username": "nsebhastian",
    "email": "Sincere@april.biz",
    // ... le reste des données utilisateur
}
```

Ci-dessus, vous pouvez voir que les valeurs des propriétés `name` et `username` sont mises à jour en utilisant le corps de la requête PATCH.

## Comment envoyer une requête DELETE

La requête DELETE est utilisée lorsque vous souhaitez demander la suppression permanente d'une ressource du serveur.

Pour exécuter une requête DELETE avec Fetch, vous devez simplement spécifier l'URL de la ressource à supprimer et la propriété `method: 'DELETE'` comme suit :

```js
fetch('https://jsonplaceholder.typicode.com/users/1', {
  method: 'DELETE',
}).then(response => response.json())
  .then(data => console.log(data))
```

La requête ci-dessus supprimera les données utilisateur ayant une valeur d'id de 1.

L'API peut répondre avec un message pour confirmer que la ressource a été supprimée. Mais puisque typicode.com est une fausse API, elle renverra un objet JavaScript vide `{}`.

## Comment utiliser Async/Await avec l'API Fetch

Puisque Fetch retourne un objet `Promise`, cela signifie que vous pouvez également utiliser la syntaxe `async`/`await` pour remplacer les méthodes `.then()` et `.catch()`.

Voici un exemple d'envoi d'une requête GET en utilisant Fetch avec la syntaxe async/await :

```js
try {
  const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
  const json = await response.json();
  console.log(json);
} catch (error) {
  console.log(error);
}

```

La gestion d'une réponse Fetch en utilisant `async`/`await` semble plus propre car vous n'avez pas à utiliser les rappels `.then()` et `.catch()`.

Si vous avez besoin d'un rappel sur async/await, vous pouvez lire mon article sur [JavaScript Async/Await](https://www.freecodecamp.org/news/javascript-async-await/).

## Exécuter des exemples de code

J'ai également créé un site web d'exemple qui vous montre comment exécuter ces 5 protocoles de requêtes HTTP à l'adresse [https://nathansebhastian.github.io/js-fetch-api/](https://nathansebhastian.github.io/js-fetch-api/)

Jetez-y un coup d'œil et étudiez l'objet `data` retourné. Pour savoir quelles requêtes API vous pouvez envoyer à une API spécifique, vous devez consulter la documentation de ce projet d'API.

## Résumé

L'API Fetch vous permet d'accéder aux API et d'effectuer une requête réseau en utilisant des méthodes de requête standard telles que GET, POST, PUT, PATCH et DELETE.

L'API Fetch retourne une promesse, vous devez donc enchaîner l'appel de fonction avec les méthodes `.then()` et `.catch()`, ou utiliser la syntaxe async/await.

Et c'est ainsi que fonctionne l'API Fetch ! Si vous avez aimé cet article, vous pourriez vouloir consulter mon livre [_Beginning Modern JavaScript_](https://codewithnathan.com/beginning-modern-javascript) pour améliorer vos compétences en JavaScript :

[![Beginning Modern JavaScript](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript.

À bientôt dans d'autres articles !