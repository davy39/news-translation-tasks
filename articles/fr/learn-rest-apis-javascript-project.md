---
title: Apprendre les API REST en construisant un projet JavaScript
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2023-12-11T15:18:44.000Z'
originalURL: https://freecodecamp.org/news/learn-rest-apis-javascript-project
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/desktop-preview-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
seo_title: Apprendre les API REST en construisant un projet JavaScript
seo_desc: 'So, you''ve been learning JavaScript. I bet you''re loving it. You''ve
  learned the basics and you''re starting to get the hang of it. So you might be wondering
  what to do next.

  Well, let me introduce you to REST APIs, a powerful tool that you are going t...'
---

Alors, vous apprenez JavaScript. Je parie que vous l'aimez. Vous avez appris les bases et vous commencez à vous habituer. Vous vous demandez peut-être quoi faire ensuite.

Eh bien, laissez-moi vous présenter les API REST, un outil puissant que vous allez ajouter à votre arsenal.

Dans cet article, nous allons apprendre ce que sont les API REST et comment les utiliser en tant que développeur JavaScript.

## Table des matières

1. [Introduction et prérequis](#heading-pour-qui-est-cet-article)

2. [Prise en main des API REST](#heading-prise-en-main-des-api-rest)

3. [Comment faire des requêtes avec les API REST](#heading-comment-faire-des-requetes-avec-les-api-rest)

4. [Comprendre les méthodes HTTP](#heading-comprendre-les-methodes-http)

5. [Comment gérer les réponses de l'API REST](#heading-comment-gerer-les-reponses-de-lapi-rest)

6. [Exemple pratique : Comment construire une application web avec une API REST publique](#heading-exemple-pratique-comment-construire-une-application-web-avec-une-api-rest-publique)

7. [Conclusion](#heading-conclusion)

## Pour qui est cet article ?

Si vous êtes nouveau dans le concept des API REST, ou si vous en avez entendu parler mais que vous ne savez pas comment elles fonctionnent, cet article est fait pour vous. Il est conçu pour les développeurs JavaScript qui souhaitent apprendre les bases du travail avec les API REST.

## Qu'ai-je besoin pour continuer avec cet article ?

Pour tirer le meilleur parti de cet article, vous avez besoin de quelques connaissances de base en JavaScript, d'un navigateur et d'un éditeur de code. Ça vous semble bien ?

## Que vais-je apprendre à la fin de cet article ?

À la fin de cet article, vous serez familiarisé avec les API REST. Vous apprendrez à faire votre première requête API et à gérer les réponses. Vous construirez également une application de suivi d'adresse IP pour mettre vos compétences en pratique.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/desktop-preview.jpg align="left")

*Application de suivi d'adresse IP*

## Prise en main des API REST

Avant de plonger dans le monde des API REST, prenons un peu de recul et comprenons ce qu'est une API.

### Qu'est-ce qu'une API ?

API signifie Application Programming Interface. Elle agit comme un canal de communication entre deux applications, comme un formulaire web soumettant des données à une base de données.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727423426199/ecb2d72f-b8d0-4821-8040-6cd1b0d507e6.png align="center")

*Diagramme montrant comment une API aide deux applications à communiquer en demandant et en envoyant des données.*

D'après l'image ci-dessus, vous pouvez voir que l'API agit comme un pont entre le formulaire web et la base de données. L'API gère la **requête** faite à partir du formulaire web et envoie une **réponse** au formulaire web. En termes simples, c'est ainsi que fonctionnent les API.

### Qu'est-ce qu'une API REST ?

Maintenant que vous savez ce qu'est une API et comment elles fonctionnent, qu'est-ce que REST ? REST (Representational State Transfer) est un ensemble de règles (eh bien, vous pouvez les appeler des directives) qui définissent des méthodes et des protocoles pour la manière dont les données doivent être envoyées, reçues et stockées.

Donc, en gros, REST est un type d'API qui suit un ensemble de règles qui rendent la communication entre deux applications fluide et organisée.

Nous n'allons pas entrer dans les détails des règles des API REST. Ici, nous voulons simplement savoir comment les utiliser pour l'instant.

Il n'y a que deux opérations qui se produisent lorsqu'il s'agit d'utiliser des API : faire une **requête** et **recevoir une réponse**. Nous allons nous concentrer sur ces deux opérations alors que nous avançons.

## Comment faire des requêtes avec les API REST

Les API REST sont généralement exposées sous forme d'Endpoint, une URL qui dirige votre requête. Par exemple, il existe une API REST appelée `jsonplaceholder` fournissant des données utilisateur aléatoires. L'endpoint pour obtenir les données utilisateur ressemble à ceci : https://jsonplaceholder.typicode.com/users.

Pour obtenir les données utilisateur, vous faites une requête à cet endpoint en utilisant l'API Fetch de JavaScript :

```javascript
const request = fetch('https://jsonplaceholder.typicode.com/users');
console.log(request.json());
```

Exécutez le code ci-dessus pour le voir en action. Vous vous demandez peut-être pourquoi vous obtenez une Promise au lieu des données. C'est parce que l'API Fetch retourne une Promise, et vous devez instruire votre code d'attendre la réponse de l'API avant de terminer.

Mais comment faites-vous cela ? Vous pouvez utiliser la méthode `async/await` en JavaScript comme ceci :

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint);
  const response = await request.json();
  console.log(response);
}

GetData(); // appeler la fonction
```

Ou vous pouvez utiliser la méthode `.then()` :

```javascript
fetch('https://jsonplaceholder.typicode.com/users')
  .then((response) => response.json())
  .then((json) => console.log(json));
```

N'importe laquelle des méthodes ci-dessus fonctionnera très bien. Si vous n'êtes pas familier avec ce code, j'ai écrit un [guide pour débutants sur les Promesses en JavaScript](https://www.freecodecamp.org/news/javascript-promises-for-beginners/) que vous pouvez consulter.

Hey, maintenant vous savez comment faire une requête et `GET` des données à partir d'une API REST. Mais que faire si vous voulez ajouter des données à une base de données en utilisant une API ? Comment feriez-vous cela ?

Eh bien, nous devons toujours utiliser l'API Fetch, mais cette fois nous devons spécifier la méthode à utiliser. Nous allons examiner ces méthodes ensuite.

## Comprendre les méthodes HTTP

En plus de la syntaxe minimale que nous avons vue, l'API Fetch prend en compte certaines options, et l'une de ces options est la méthode HTTP.

Les méthodes HTTP informent l'API REST du type de requête que vous faites. Les types courants sont POST, GET, PUT et DELETE, collectivement connus sous le nom d'opérations CRUD (Create, Read, Update, Delete).

Examinons chaque méthode HTTP séparément.

### Méthode HTTP GET

Cette méthode HTTP est utilisée pour lire des données à partir du serveur lors de l'utilisation de l'API REST. Pour ajouter une méthode à l'API Fetch, vous la spécifiez après l'endpoint, comme ceci :

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, { method: 'GET' });
  const response = await request.json();
  console.log(response);
}

GetData(); // appeler la fonction
```

Lors de l'utilisation de l'API Fetch, il est facultatif de spécifier la méthode HTTP GET. Si vous ne spécifiez aucune méthode HTTP, l'API Fetch suppose que vous faites une requête GET. C'est pourquoi le code que vous avez utilisé pour votre première requête API fonctionne toujours bien même sans la méthode HTTP.

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint);
  const response = await request.json();
  console.log(response);
}

GetData(); // appeler la fonction
```

### Méthode HTTP POST

Contrairement à la méthode HTTP `GET`, qui récupère des données à partir d'une API, la méthode HTTP POST est utilisée pour ajouter des données lors de l'utilisation des API REST.

```javascript
async function AddData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data),
  });

  const response = await request.json();
  console.log(response);
}

const data = { username: 'John Snow', age: 22 };

AddData(); // appeler la fonction
```

Si vous voulez ajouter des données à l'API REST en utilisant cette méthode, vous devez spécifier la méthode HTTP `POST`. Vous pouvez également voir que nous avons passé les données que nous essayons d'ajouter à l'option `body`.

Outre les méthodes HTTP, l'API Fetch dispose également de l'option `body` à laquelle nous pouvons passer nos données lors de l'ajout de données à notre API. Ces données que nous essayons d'ajouter sont généralement au format JSON, c'est pourquoi nous devons convertir notre `Object` en JSON en utilisant la méthode `JSON.stringify()`.

```javascript
const data = { username: 'John Snow', age: 22 };
const json = JSON.stringify(data);
console.log(json);
```

### Méthode HTTP PUT

Cette méthode est utilisée pour mettre à jour des données lors de l'utilisation des API REST. Vous utilisez cette méthode avec les données que vous souhaitez mettre à jour, tout comme la méthode HTTP POST.

Mettons à jour l'utilisateur avec l'`id` 11 que nous avons créé ci-dessus.

```javascript
async function UpdateData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users/2';
  const request = await fetch(endpoint, {
    method: 'PUT',
    body: JSON.stringify(data),
  });

  const response = await request.json();
  console.log(response);
}

const data = { age: 42 }; // mettre à jour l'âge

UpdateData(); // appeler la fonction
```

### Méthode HTTP DELETE

Cette méthode, comme son nom l'indique, est utilisée pour supprimer définitivement des données d'un serveur lors de l'utilisation des API REST. Vous ne passez aucune donnée au corps lors de l'utilisation de cette méthode. Supprimons l'utilisateur que nous avons créé ci-dessus :

```javascript
async function UpdateData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users/2';
  const request = await fetch(endpoint, { method: 'DELETE' });

  const response = await request.json();
  console.log(response);
}

UpdateData(); // appeler la fonction
```

Ayant appris tout cela, vous pouvez maintenant créer, lire, mettre à jour et supprimer des données du serveur en utilisant les API REST.

Maintenant, lors de la réalisation de requêtes à une API REST, la méthode HTTP et les options de corps ne sont pas les seules choses que vous pouvez spécifier avec votre requête. Vous pouvez également passer des `headers` avec votre requête.

Les headers vous permettent de fournir des informations supplémentaires sur la requête que vous faites. Par exemple, nous pouvons informer l'API REST du type de contenu que nous envoyons à l'avance.

```javascript
async function AddData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  });

  const response = await request.json();
  console.log(response);
}

const data = { username: 'John Snow', age: 22 };

AddData(); // appeler la fonction
```

Le header `headers: { "Content-Type": "application/json"}` indique simplement à l'API REST à l'avance que nous essayons d'ajouter des données au format JSON. Bien sûr, cela est complètement facultatif.

Jusqu'à présent, nous n'avons examiné que la réalisation de requêtes. Regardons maintenant comment gérer les réponses d'une API REST.

## Comment gérer les réponses de l'API REST

À chaque fois que vous faites une requête à une API, vous recevrez toujours une réponse. Il existe plusieurs types de réponses que vous pouvez obtenir d'un appel d'API REST. Vous obtenez soit une réponse de succès 2XX, soit une réponse d'erreur 4XX/5XX. Dans votre code JavaScript, vous devez gérer ces réponses en conséquence.

Ne vous inquiétez pas, nous allons décomposer ce que signifient les réponses ci-dessus.

### Comprendre les codes de réponse

Comme indiqué ci-dessus, chaque fois que vous faites une requête, vous recevrez toujours une réponse. Selon le statut de votre code de réponse, vous pouvez déterminer si une réponse a été réussie ou non.

#### Code de statut de succès 2XX

Les réponses de succès sont généralement dans la plage des codes de statut HTTP 200 à 299. Le code de succès le plus courant est 200 OK, indiquant que la requête a réussi. Lorsque vous recevez une réponse réussie, vous pouvez gérer les données retournées par l'API.

Voici un exemple qui montre le code de statut de notre réponse :

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, { method: 'GET' });
  const response = await request.json();

  console.log(response.status);
}

GetData(); // appeler la fonction
```

Si vous obtenez un code de statut `200`, cela signifie que la requête a réussi et est OK.

Nous devons toujours utiliser ce code de statut pour vérifier si notre requête a réussi avant d'essayer d'utiliser les données retournées par une requête API.

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, { method: 'GET' });
  const response = await request.json();

  if (request.status == 200) {
    // La requête a réussi
    console.log(request.status);
  }
}

GetData(); // appeler la fonction
```

De plus, vous pouvez également utiliser la propriété `Response.ok` pour vérifier si la requête a réussi ; cette propriété retournera `true` si la requête a réussi.

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint, { method: 'GET' });
  const response = await request.json();

  if (response.ok) {
    // La requête a réussi
    console.log(response.status);
  }
}

GetData(); // appeler la fonction
```

#### Code de statut d'erreur 4XX/5XX

Lorsque vous faites une requête à une API et que vous ne recevez pas de code de statut de succès, vous obtiendrez soit un code d'erreur 400-499, soit 500-599. Le code d'erreur que vous recevrez tombera dans l'une de ces plages.

Ces deux codes de statut indiquent généralement une erreur. Les codes d'erreur 400-499 indiquent qu'il y a quelque chose qui ne va pas avec votre requête, tandis que les codes d'erreur 500-599 indiquent que l'erreur provient du serveur.

Prenons l'exemple ci-dessous où nous avons intentionnellement fait une requête à un endpoint inexistant ([`https://jsonplaceholder.typicode.com/nonexistent`](https://jsonplaceholder.typicode.com/nonexistent)) pour déclencher une erreur `404 Not Found`.

```javascript
async function AddData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/nonexistent';
  const request = await fetch(endpoint, {
    method: 'POST',
    body: data, // ne convertissez pas les données en json
  });

  const response = await request.json();

  if (response.ok) {
    console.log(response);
  } else {
    console.log(`Une erreur avec le code de statut ${response.status} s'est produite`);
  }
}

const data = { username: 'John Snow', age: 22 };

AddData(); // appeler la fonction
```

Le code de statut `404` que nous avons reçu ici indique qu'il y a quelque chose qui ne va pas avec notre requête.

Je n'ai pas couvert tous les codes de statut ici, mais si vous cherchez une liste complète des codes de statut, vous pouvez consulter ce [guide](https://www.restapitutorial.com/httpstatuscodes.html).

Maintenant, en fonction de la réponse que vous recevez, vous pouvez montrer différentes choses à vos utilisateurs.

* si vous recevez un code de statut de succès, vous pouvez utiliser les données pour construire votre application comme vous le jugez approprié

* Si vous recevez un code de statut d'erreur, vous pouvez également afficher un message d'erreur à vos utilisateurs

### Comment gérer le corps de la réponse

En fonction du type de requête que vous faites, vous allez recevoir des données en réponse. Pour obtenir ces données, nous utilisons `request.json();`. Nous avons déjà utilisé cela plusieurs fois, cela obtiendra le corps de la requête et analysera les données pour les convertir en un objet que nous pouvons utiliser.

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint);

  const response = await request.json(); // analyser les données

  console.log(response);
}

GetData(); // appeler la fonction
```

Vous n'avez pas besoin de faire autre chose pour traiter les données retournées par votre requête API.

Outre le corps de la requête, vous recevez également les `headers` avec la réponse. Cela peut être utile si, par exemple, vous voulez vérifier le type de données retournées par votre requête API à l'avance :

```javascript
async function GetData() {
  let endpoint = 'https://jsonplaceholder.typicode.com/users';
  const request = await fetch(endpoint);

  const dataType = request.headers.get('content-type');

  if (dataType.includes('application/json')) {
    const response = await request.json(); // analyser les données
    console.log(response);
  } else {
    console.log('Nous nous attendions à ce que les données soient au format json');
  }
}
GetData(); // appeler la fonction
```

Assez parlé, retroussons nos manches et essayons un exemple pratique.

## Exemple pratique : Comment construire une application web avec une API REST publique

J'ai l'impression que nous avons déjà beaucoup appris, alors mettons en pratique nos nouvelles compétences en API REST, d'accord ?

Notre tâche est de construire une application web avec une API d'adresse IP. Elle récupérera des informations sur une adresse IP et affichera l'emplacement de l'adresse IP sur une carte avec quelques autres informations. Voici à quoi elle devrait ressembler :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727424349562/2f32e4cf-908f-411b-8eea-89e97984b18a.jpeg align="center")

*Application que nous allons construire*

Pour construire cela, nous allons utiliser :

* [API de géolocalisation IP par IPify](https://geo.ipify.org/) pour obtenir les emplacements des adresses IP.

* L'endpoint pour l'API : [`https://geo.ipify.org/api/v2/country,city?apiKey=XXXXXXXX&ipAddress=XXXXXXX`](https://geo.ipify.org/api/v2/country,city?apiKey=XXXXXXXX&ipAddress=XXXXXXX)

* Pour obtenir la clé API, vous devez vous inscrire pour un compte avec [IPify](https://geo.ipify.org/)

* Pour générer la carte, nous allons utiliser [LeafletJS](https://leafletjs.com/)

Maintenant que nous avons cela de côté, construisons le HTML et le CSS de l'application web. Si vous êtes confiant dans vos compétences en HTML et CSS, essayez de construire la page web par vous-même. Voici mon implémentation :

%[https://codepen.io/Spruce_khalifa/pen/GRzzeNp]

Maintenant que nous avons le HTML et le CSS de côté, la première chose que nous devons faire est d'obtenir l'adresse IP que l'utilisateur a entrée. Créez donc un fichier `index.js` et ajoutez le code suivant :

```js
/* Sélectionner le formulaire */
const search_form = document.querySelector('.header_form');

search_form.addEventListener('submit', (event) => {
  /* empêcher le formulaire de se soumettre automatiquement au clic */
  event.preventDefault();

  /* obtenir la valeur du champ de formulaire */
  const value = document.querySelector('#search').value;

  console.log(value);
});
```

Soumettez le formulaire pour voir la valeur que vous avez entrée dans le formulaire d'entrée HTML.

Ensuite, nous devons passer cette valeur à une fonction `search_Ip_Address()`. Elle fait en réalité une requête GET pour récupérer nos données de localisation et utilise les données pour mettre à jour l'UI de notre application web :

```js
/* Sélectionner le formulaire */
const search_form = document.querySelector('.header_form');

search_form.addEventListener('submit', (event) => {
  /* empêcher le formulaire de se soumettre automatiquement au clic */
  event.preventDefault();

  /* obtenir la valeur du champ de formulaire */
  const value = document.querySelector('#search').value;

  /* Passer l'adresse IP à la fonction search_Ip_Address() */
  search_Ip_Address(value);
});

/* Rechercher une adresse IP */
async function search_Ip_Address(ip_address) {
  const api_key = 'xxxxxxxxxxxxxxxxxxxxxxx';
  const request = await fetch(
    `https://geo.ipify.org/api/v2/country,city?apiKey=${api_key}&ipAddress=${ip_address}`,
  );
  const response = await request.json();

  /* Mettre à jour l'UI sur la page */
  const { location, ip, isp } = response;
  update_ui(ip, location.city, location.timezone, isp);
}

/* fonction de mise à jour de l'UI */
function update_ui(ip_address, location, timezone, isp) {
  /* sélectionner tous les éléments sur la page */
  const address = document.querySelector('.address');
  const city = document.querySelector('.location');
  const utc = document.querySelector('.utc');
  const isprovider = document.querySelector('.isp');

  /* Mettre à jour tous les éléments sur la page */
  address.textContent = ip_address;
  city.textContent = location;
  utc.textContent = 'UTC' + timezone;
  isprovider.textContent = isp;
}
```

Ensuite, nous devons créer notre carte. Pour commencer, ajoutez ce qui suit à la section `head` de votre fichier HTML :

```html
<head>
  ...
  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
    integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
    crossorigin=""
  />
  <script
    src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
    integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
    crossorigin=""
  ></script>
  ...
</head>
```

Assurez-vous également d'avoir un élément div sur la page avec un `id` de map :

```html
<div class="map" id="map"></div>
```

Ensuite, nous devons créer une fonction qui créera la carte pour nous. Ajoutez donc le code suivant dans votre `script.js` :

```js
/* créer la carte */
let map;
function create_map(lat, lng) {
  map = L.map('map').setView([lat, lng, country, region], 14);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  L.marker([lat, lng])
    .addTo(map)
    .bindPopup(`${region}, ${country}`)
    .openPopup();
}
```

Enfin, nous devons simplement appeler la fonction `create_map()` chaque fois que l'utilisateur recherche une adresse IP.

Pour appeler `create_map()` lorsque l'utilisateur recherche une adresse IP, mettez à jour la fonction `search_Ip_Address()` :

```js
/* Rechercher une adresse IP */
async function search_Ip_Address(ip_address) {
  const api_key = 'at_HhKzCe09UZIYJC9pY7YTg7kMMUzZd';
  const request = await fetch(
    `https://geo.ipify.org/api/v2/country,city?apiKey=${api_key}&ipAddress=${ip_address}`,
  );
  const response = await request.json();

  const { location, ip, isp } = response;

  /* Mettre à jour l'UI sur la page */
  update_ui(ip, location.city, location.timezone, isp);

  /* Mettre à jour la carte sur la page */
  /* d'abord supprimer toutes les instances de carte si elles existent */
  if (map !== undefined && map !== null) {
    map.remove();
  }
  create_map(location.lat, location.lng, location.country, location.region);
}
```

Enfin, appelez simplement la fonction `search_Ip_Address()` lorsque la page a fini de charger :

```js
const defaultIp = '197.210.78.172';
search_Ip_Address(defaultIp);
```

Et voilà, une belle application web de suivi d'IP. J'espère que la construction de cette application vous a aidé à renforcer vos nouvelles compétences en API REST.

Pour vous offrir une opportunité de pratique, voici un défi que vous pouvez entreprendre. Voici un aperçu final de l'application web :

%[https://codepen.io/Spruce_khalifa/pen/rNPPoag]

### Défi :

Actuellement, notre application de suivi d'IP manque de gestion des erreurs. Par exemple, si un utilisateur entre un mot aléatoire dans le champ de recherche qui n'est pas une adresse IP valide, toute l'application plantera.

En tant que développeurs consciencieux, nous devons toujours être vigilants quant aux erreurs et les gérer avec grâce. Par conséquent, votre défi est double :

1. Implémentez une validation d'entrée pour vous assurer que la valeur entrée est toujours une adresse IP valide. Si l'utilisateur entre une adresse IP invalide, affichez un message d'erreur.

2. Gérez toutes les erreurs imprévues que les utilisateurs peuvent rencontrer lors de l'utilisation de l'application.

## Conclusion

Savoir comment travailler avec les API REST est une compétence clé que les développeurs doivent avoir. Dans cet article, vous avez appris ce que sont les API REST et comment les utiliser pour développer vos propres applications.

Si vous avez des questions, n'hésitez pas à m'envoyer un message sur Twitter à [@sprucekhalifa](https://twitter.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus d'informations et de mises à jour. Bon codage !

L'exemple utilisé dans ce tutoriel provient de [frontendmentor.io](http://frontendmentor.io) [Défi de suivi d'adresse IP sur Frontend Mentor](https://www.frontendmentor.io/challenges/ip-address-tracker-I8-0yYAH0).