---
title: 'Fetch API vs. Axios vs. Alova : Quel client HTTP devriez-vous utiliser en
  2025 ?'
subtitle: ''
author: Abdullah Salaudeen
co_authors: []
series: null
date: '2025-04-02T14:48:52.725Z'
originalURL: https://freecodecamp.org/news/fetch-api-vs-axios-vs-alova
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743605319873/9f7583a0-1b01-4714-9fe6-f39bed3954e8.png
tags:
- name: Alova
  slug: alova
- name: XHP
  slug: xhp
- name: JavaScript
  slug: javascript
- name: javascript framework
  slug: javascript-framework
- name: js
  slug: js
- name: json
  slug: json
- name: React
  slug: reactjs
- name: blob
  slug: blob
- name: axios
  slug: axios
- name: fetch API
  slug: fetch-api
- name: fetching apis
  slug: fetching-apis
- name: APIs
  slug: apis
- name: 'API basics '
  slug: api-basics
- name: API
  slug: api
seo_title: 'Fetch API vs. Axios vs. Alova : Quel client HTTP devriez-vous utiliser
  en 2025 ?'
seo_desc: 'Before the days of the Fetch API and Axios, developers used callback-based
  HTTP requests. They manually managed requests with asynchronous operations and,
  in the process, wrote deeply nested code. This was known as callback hell.

  Then, in 2015, a pro...'
---

Avant l'ère de l'API Fetch et Axios, les développeurs utilisaient des requêtes HTTP basées sur des callbacks. Ils géraient manuellement les requêtes avec des opérations asynchrones et, dans le processus, écrivaient du code profondément imbriqué. Cela était connu sous le nom de "callback hell".

Ensuite, en 2015, une API de requête basée sur les promesses, l'API Fetch, a été intégrée à JavaScript ES6 pour simplifier le processus. Après cela, des bibliothèques comme Axios et Alova sont également apparues.

Mais pourquoi quelqu'un envisagerait-il d'utiliser une API tierce alors que l'API Fetch intégrée et légère est une option efficace ? Eh bien, Axios et Alova offrent plus que la simple récupération de réponses JSON. Alors qu'Axios automatise l'analyse du JSON et fournit des méthodes abrégées pour les requêtes, Alova met en cache les réponses, ce qui évite de faire de nouvelles requêtes redondantes.

Alors, lequel devez-vous choisir : Fetch API, Axios ou Alova ?

Dans ce guide, nous examinerons chacun de ces outils en fonction de leurs caractéristiques, performances et adéquation aux projets. Suivez-moi...

## **Table des matières**

1. [Prérequis](#heading-prerequisites)

2. [L'API Fetch](#heading-the-fetch-api)

   * [Caractéristiques clés de l'API Fetch](#heading-key-features-of-the-fetch-api)

   * [Limitations de l'API Fetch](#heading-limitations-of-the-fetch-api)

3. [Axios](#heading-axios)

   * [Caractéristiques clés d'Axios](#heading-key-features-of-axios)

   * [Limitations d'Axios](#heading-limitations-of-axios)

4. [Alova](#heading-alova)

   * [Caractéristiques clés d'Alova](#heading-key-features-of-alova)

   * [Limitations d'Alova](#heading-limitations-of-alova)

5. [Comparaison fonction par fonction](#heading-feature-by-feature-comparison)

6. [Cas d'utilisation et meilleurs scénarios](#heading-use-cases-and-best-scenarios)

   * [Quand utiliser l'API Fetch](#heading-when-to-use-fetch-api)

   * [Quand utiliser Axios](#heading-when-to-use-axios)

   * [Quand utiliser Alova](#heading-when-to-use-alova)

7. [Communauté et écosystème](#heading-community-and-ecosystem)

   * [Écosystème et intégrations](#heading-ecosystem-and-integrations)

8. [Conclusion](#heading-conclusion)

## Prérequis

Avant de commencer ce tutoriel, vous devriez avoir une compréhension de base de JavaScript et des fonctionnalités ES6+, telles que [`async/await`](https://www.freecodecamp.org/news/javascript-async-await/), les [fonctions fléchées](https://www.freecodecamp.org/news/javascript-arrow-functions-in-depth/) et la [destructuration d'objets](https://salaudeenabdu.hashnode.dev/destructuring-in-javascript). Être familiarisé avec l'API `fetch()` sera également utile, car nous la comparerons avec Axios et Alova.

Vous devriez également avoir une connaissance fondamentale des méthodes HTTP (GET, POST, PUT, DELETE, PATCH) et de la gestion des réponses d'API en fonction des codes de statut pour mieux comprendre les exemples d'API.

Bien que ce tutoriel se concentre sur JavaScript, certains exemples utilisent React. Vous devriez donc être familiarisé avec React et comprendre les bases des composants, de l'état et des hooks (comme `useState` et `useEffect`). Alova fonctionne également avec des frameworks comme Vue et Svelte.

Une expérience de base avec les gestionnaires de paquets (NPM ou Yarn) est utile pour installer des dépendances comme Axios et Alova. Et comprendre les environnements Node.js et navigateur aidera, car Alova fonctionne dans les deux contextes.

Enfin, la familiarité avec la gestion d'état et les concepts de mise en cache améliorera votre compréhension des fonctionnalités d'Alova, car il intègre la gestion d'état et la mise en cache directement dans les requêtes API.

## **L'API Fetch**

L'API Fetch est une fonctionnalité de requête API basée sur les promesses en JavaScript qui a été publiée pour remplacer l'ancien XMLHttpRequest (XHP) basé sur les callbacks. Contrairement à l'ancien outil, l'API Fetch est compatible avec les fonctionnalités modernes des sites web, y compris les [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) et le [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).

Avec cet outil, appeler des données API est aussi simple que de faire une requête fetch() sur l'URL de l'API, comme montré ci-dessous :

```javascript
fetch("https://fakestoreapi.com/products")
```

Le `fetch()` retourne la promesse du serveur qui est remplie avec un objet de réponse. Ensuite, vous passez quelques arguments optionnels pour configurer la réponse en JSON ou en texte, l'attachez à une variable et utilisez les données.

```javascript
let products;

fetch("https://fakestoreapi.com/products")

  .then((res) => res.json())

  .then((data) => {

    products = data

    console.log(products)

  })

  .catch((error) => console.error("Error fetching data:", error))
```

Dans le code ci-dessus, le `fetch()` demande des données API à partir de l'URL. La réponse `res` est analysée en JSON `res.json`. Ensuite, les données résultantes sont attachées à la variable `products` et enregistrées dans la console.

Depuis Node.js v17.5, l'API Fetch est disponible nativement, éliminant la dépendance à des paquets externes comme `node-fetch`, `got`, ou `cross-fetch` pour gérer les requêtes HTTP. Ce support natif dans les navigateurs et Node.js supprime le besoin de dépendances supplémentaires, réduisant la taille globale du bundle de votre application. Avec cette fonctionnalité intégrée, l'API Fetch est devenue l'outil de référence pour effectuer des appels API asynchrones dans les applications JavaScript.

### Caractéristiques clés de l'API Fetch

#### Syntaxe basée sur les promesses

Comme je l'ai mentionné précédemment, l'API Fetch utilise une syntaxe basée sur les promesses qui envoie une promesse depuis le serveur et l'exécute avec un objet de réponse. Bien que l'enchaînement `.then` puisse être optimal pour des requêtes simples, l'utilisation de plusieurs `.then` peut conduire à un "callback hell" et vous donner du fil à retordre pour suivre les erreurs. C'est pourquoi l'alternative `async/await` est une solution plus optimale. Consultez l'exemple de code ci-dessous :

```javascript
const fetchData = async () => {

  try {

    const response = await fetch("https://fakestoreapi.com/products");

    if (!response.ok) {

      throw new Error(`HTTP error! Status: ${response.status}`);

    }

    const data = await response.json();

    products = data

    console.log(products); //

  } catch (error) {

    console.error("Error fetching data:", error);

  }

};

fetchData();
```

Comme montré ci-dessus, le fetch fait une requête get. Ensuite, le serveur retourne un statut d'erreur si la réponse n'est pas ok (retourne un statut d'erreur comme `error 404`). Ensuite, la réponse est analysée en JSON et utilisée.

Gardez à l'esprit que toutes les méthodes passées sur la réponse sont asynchrones, y compris le `fetch()` et l'analyse `json()`.

#### Prend en charge les méthodes `GET`, `POST`, `PUT`, `PATCH` et `DELETE`

`GET`, utilisé pour recevoir des réponses, est la méthode par défaut de l'API Fetch. Donc, lorsque vous l'utilisez, vous n'avez pas à la définir explicitement ou à attacher un corps. Mais pour les méthodes qui envoient des requêtes comme `POST`, `PUT`, `PATCH` et `DELETE`, vous devez spécifier leur méthode et attacher un corps.

Toutes ces méthodes envoient des requêtes au backend. Vous pouvez envoyer des données au serveur avec `POST`, remplacer complètement une ressource existante par de nouvelles données en utilisant `PUT`, mettre à jour partiellement avec `PATCH`, ou supprimer la ressource avec `DELETE`.

1. **Voici comment vous pouvez définir une méthode :**

Dans le code ci-dessous, je définis la méthode POST pour envoyer des données à l'API spécifiée :

```javascript
const response = await fetch("https://example.com/products1", {

  method: "POST"

  //...

});
```

En plus de poster des données, vous pouvez également effacer des données sur le serveur en utilisant `DELETE` :

```javascript
const response = await fetch("https://example.com/products1", {

  method: "DELETE"

  //...

});
```

2. **Ensuite, définissez l'en-tête :**

Définir l'en-tête permet au serveur de comprendre le type de contenu que vous envoyez pour une gestion appropriée des données. Comme montré ici, l'en-tête demande au serveur de stocker le contenu en tant que fichier JSON et de définir le jeton d'autorisation sur `my-classified-token`. Gardez à l'esprit que le jeton est la clé API qui sera utilisée pour vérifier l'identité de l'utilisateur lors de l'utilisation.

```javascript
const response = await fetch("https://example.com/products1", {

  method: "POST",

  header: {

    "Content-Type": "application-json",

    "Authorization": "Bearer my-classified-token",

  }

  //..

});
```

Voici une liste complète des paramètres qui peuvent être passés dans l'en-tête :

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>En-tête</strong></p></td><td colspan="1" rowspan="1"><p><strong>Objectif</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p>"Content-Type": "application/json"</p></td><td colspan="1" rowspan="1"><p>Indique au serveur que le corps de la requête est au format JSON.</p></td></tr><tr><td colspan="1" rowspan="1"><p>"Authorization": "Bearer token"</p></td><td colspan="1" rowspan="1"><p>Fournit une authentification (clés API, JWT, jetons OAuth).</p></td></tr><tr><td colspan="1" rowspan="1"><p>"Accept": "application/json"</p></td><td colspan="1" rowspan="1"><p>Spécifie que le client attend une réponse JSON.</p></td></tr><tr><td colspan="1" rowspan="1"><p>"Content-Type": "application/x-www-form-urlencoded"</p></td><td colspan="1" rowspan="1"><p>Utilisé pour envoyer des données de formulaire au lieu de JSON.</p></td></tr><tr><td colspan="1" rowspan="1"><p>"Origin": "http://example.com"</p></td><td colspan="1" rowspan="1"><p>Indique d'où provient la requête (utilisé dans CORS).</p></td></tr></tbody></table>

3. **Ensuite, attachez le corps :**

Après avoir spécifié l'en-tête, vous attachez ensuite le corps. Le corps est les données envoyées au serveur backend. Il ne peut pas être utilisé avec la méthode GET qui ne récupère que des réponses. De plus, les informations attachées doivent toujours être dans un format valide qui correspond au type de contenu spécifié dans les en-têtes. Vous pouvez ajouter autant de valeurs que vous le souhaitez au corps.

```javascript
const response = await fetch("https://example.com/products1", {

  method: "POST",

  header: {

    "Content-Type": "application-json",

    "Authorization": "Bearer my-classified-token",

  },

  body: JSON.stringify({ name: "Laptop", price: 1200 })

});
```

#### Streaming de données

Il est également intéressant de noter que l'API Fetch facilite la gestion de grandes quantités de données via le streaming. Elle reçoit des données copieuses par morceaux au lieu de charger toutes les données et de les mettre en mémoire tampon dans le processus. Ainsi, les données s'affichent en temps réel à leur arrivée. Voici un exemple simple de streaming :

```javascript
const fetchData = async () => {

  const response = await fetch('https://www.example.com/large-text-file.txt');

  const reader = response.body.getReader();

  const decoder = new TextDecoder();

  while (true) {

    const { done, value } = await reader.read();

    if (done) break;

    const chunk = decoder.decode(value, { stream: true });

    console.log(chunk); // Traiter le morceau (par exemple, l'afficher dans l'UI)

  }

  console.log('Stream complet');

};

fetchData();
```

#### Récupération de documents avec l'analyseur DOM

Contrairement à son prédécesseur, XHP, qui peut directement retourner un document, l'API Fetch ne peut pas obtenir les mêmes résultats sans utiliser l'analyseur DOM. Pour l'utiliser, vous devez définir le type de réponse en texte, puis le convertir en document à l'aide du DOMParser. Voici un exemple :

```javascript
fetch("example.xml")

  .then(res => res.text()) // Obtenir le texte brut

  .then(data => {

    const parser = new DOMParser();

    const doc = parser.parseFromString(data, "text/xml"); // Convertir le texte en Document

    console.log(doc); // Maintenant c'est un objet Document

  })

  .catch(console.error);
```

#### Annulation de requête avec AbortController

Auparavant, l'API Fetch ne pouvait pas annuler les requêtes. Mais cela est maintenant possible avec `AbortController` et `AbortSignal`. Cependant, l'API AbortController n'est pas native non plus, ce qui signifie qu'il y a un bundle supplémentaire et une configuration requise.

### **Limitations de l'API Fetch**

#### Flexibilité de la réponse ou absence d'analyse JSON automatique

Cela dépend de votre point de vue. Devoir spécifier si vous voulez votre réponse en JSON `res.json()` ou en texte `res.text()` ou en blob `res.blob()` vous permet de définir quel type de réponse vous voulez dès le départ. Mais cela peut aussi être une limitation puisque la plupart des récupérations d'API sont en JSON. Cela signifie que des alternatives comme Axios, qui définissent les défauts comme `res.json()`, aident à écrire un code plus court et plus propre, et sont donc souvent préférées par les développeurs.

#### Pas d'intercepteurs de requête/réponse intégrés

Contrairement à Axios, l'API Fetch ne dispose pas de méthodes intégrées qui interceptent et modifient les requêtes ou les réponses. Cette limitation signifie que vous devez écrire du code boilerplate pour créer un intercepteur personnalisé.

Par exemple, via l'interception, vous pouvez attacher un jeton d'autorisation automatiquement avant d'envoyer des requêtes ou demander à toutes les erreurs 401 de se recharger automatiquement lors de la réception des réponses. Avec l'API Fetch, vous devez envelopper le `fetch()` dans une fonction pour faire cela, ce qui signifie plus de lignes de code.

Voici un exemple de code construit pour imiter l'interception des requêtes/réponses :

```javascript
const customFetch = async (url, options = {}) => {

  // Interception de la requête

  const modifiedOptions = {

    ...options,

    headers: {

      'Content-Type': 'application/json',

      Authorization: Bearer ${localStorage.getItem("token")}, // Comportement de l'intercepteur

      ...options.headers

    }

  };

  try {

    const response = await fetch(url, modifiedOptions);

    // Interception de la réponse

    if (!response.ok) {

      console.error("Erreur interceptée :", response.status);

    }

    return await response.json();

  } catch (error) {

    console.error("Erreur Fetch interceptée :", error);

    throw error;

  }

};

// Utilisation (pas besoin de définir les en-têtes manuellement)

customFetch('https://api.example.com/data')

  .then(data => console.log(data))

  .catch(error => console.error(error));
```

#### La gestion des erreurs nécessite une logique supplémentaire

L'API Fetch ne rejette que les erreurs réseau, pas les codes de statut HTTP échoués comme 404 ou 501. Cela signifie que lorsqu'une requête de récupération échoue, elle ne retourne pas de `404 Not Found` ou `500 Internal Server Error` à moins que vous ne le configuriez avec un code supplémentaire. Mais Axios le fait.

```javascript
fetch('https://jsonplaceholder.typicode.com/invalid-url')

  .then(response => {

    if (!response.ok) { // Gérer manuellement les réponses non-2xx

      throw new Error(`HTTP Error! Status: ${response.status}`);

    }

    return response.json();

  })

  .then(data => console.log(data))

  .catch(error => console.log('Error:', error.message));
```

## **Axios**

Après que XHP ait été remplacé par l'API Fetch, [Axios](https://axios-http.com/docs/intro) est apparu en 2016 pour résoudre certains problèmes avec le nouvel outil de récupération natif JavaScript. Construit sur XHP, Axios a rapidement gagné une adoption généralisée grâce à la combinaison de nombreuses fonctionnalités basées sur les promesses de l'API Fetch avec certaines méthodes de l'ancien XMLHttpRequest. En peu de temps, il est devenu un choix populaire parmi les développeurs.

Axios se distingue parce qu'il :

* Automatise l'analyse JSON

* Dispose d'une méthode intégrée pour intercepter et modifier les requêtes et les réponses

* Automatise la gestion des erreurs

* Automatise la gestion des délais d'attente

* Peut suivre la progression des téléchargements et des uploads

Et bien d'autres fonctionnalités.

En particulier, Axios est largement apprécié car il réduit le code boilerplate. Puisque la plupart des requêtes API encodent les données avec `JSON`, Axios définit son analyse par défaut en conséquence, ce qui signifie que vous n'avez pas à définir `JSON` à nouveau. Et pourquoi s'en soucier de toute façon, puisque les développeurs utilisent beaucoup moins de réponses d'API `res.text()` et `res.blob()` en comparaison.

```javascript
const fetchData = async () => {

  const response = await axios.get('https://api.example.com/data');

  console.log(response.data); // JSON est déjà analysé

};
```

Maintenant, comparez cela à une récupération similaire avec l'API Fetch :

```javascript
const fetchData = async () => {

  const response = await fetch('https://api.example.com/data');

  const data = await response.json(); // Étape supplémentaire

  console.log(data);

};
```

Oui, il y a une ligne supplémentaire, n'est-ce pas ? Cela pourrait signifier plusieurs lignes de code pour des bases de code plus grandes.

### **Caractéristiques clés d'Axios**

#### Analyse JSON automatique

Comme expliqué ci-dessus, vous n'avez pas à appeler `res.json()` à nouveau lors de l'utilisation d'Axios, puisque la méthode est automatiquement définie. Mais que se passe-t-il, dans de rares cas, lorsque vous souhaitez récupérer un blob ou un texte en utilisant Axios ? Alors, vous devez définir le type de réponse en conséquence. Voici comment vous pouvez faire cela :

```javascript
const fetchData = async () => {

  const response = await axios.get('https://api.example.com/data', {

    responseType: 'text', // Traite la réponse comme du texte brut

  });

  console.log(response.data); // Chaîne de texte brut

};
```

#### Intercepteurs intégrés pour modifier les requêtes et les réponses

Axios dispose d'intercepteurs intégrés pour intercepter et modifier les réponses ou requêtes de l'API. Les intercepteurs peuvent aider à définir des jetons d'autorisation pour les requêtes ou modifier les réponses et erreurs globales avant qu'elles ne soient rendues. Utilisez `.interceptors.request.use()` pour les requêtes et `.interceptors.response.use()` pour les réponses.

```javascript
import axios from "axios";

const apiClient = axios.create({

  baseURL: "https://api.example.com",

  headers: {

    'Content-Type': 'application/json'

  }

});

// Intercepteur de requête : Attacher les en-têtes d'autorisation

apiClient.interceptors.request.use(config => {

  config.headers.Authorization = Bearer ${localStorage.getItem("token")};

  return config;

}, error => Promise.reject(error));

// Utilisation : Axios inclut automatiquement l'en-tête d'autorisation

apiClient.get("/data")

  .then(response => console.log(response.data))

  .catch(error => console.error(error));
```

Pour atteindre cela avec l'API Fetch, vous devrez écrire un wrapper d'intercepteur sur votre API, ce qui nécessite beaucoup plus de code boilerplate.

#### Annulation de requête avec CancelToken

Bien que maintenant obsolète, Axios avait sa propre méthode native d'annulation de requête connue sous le nom de `CancelToken`. Mais maintenant, l'API `AbortController` est considérée comme une méthode globalement reconnue et fiable pour l'annulation de requêtes.

#### Gestion des erreurs

Axios gère mieux les erreurs en rejetant automatiquement tous les codes de statut non-2xx comme `Error 404` et `501`. Vous n'avez pas besoin de vérifier un message `response.ok` :

```javascript
axios.get('https://jsonplaceholder.typicode.com/invalid-url')

  .then(response => console.log(response.data))

  .catch(error => {

    console.log('Error Status:', error.response?.status); // Axios rejette automatiquement les réponses non-2xx

    console.log('Error Message:', error.message);

  });
```

#### Suivi de progression intégré

Axios intègre des méthodes XHP comme `onDownloadProgress` et `onUploadProgress`. Cette fonctionnalité intégrée facilite le suivi de la progression des téléchargements et des uploads. Alors qu'avec l'API Fetch, vous auriez besoin de `ReadableStream` pour obtenir des résultats similaires.

Voici un exemple montrant comment vous pouvez utiliser `onUploadProgress` :

```javascript
axios.post(url, data, {

  onUploadProgress: progressEvent => console.log(progressEvent.loaded)

});
```

#### Prend en charge d'autres méthodes également

Tout comme l'API Fetch, la méthode par défaut d'Axios est `GET`. Mais vous pouvez utiliser les méthodes `POST`, `PUT`, `PATCH` ou `DELETE` en utilisant `axios.request()`. Voici comment :

```javascript
import axios from "axios";

axios.request({

  method: "POST",

  url: "https://api.example.com/users",

  body: { name: "Abdullah", age: 25 }, // Corps de la requête

  headers: {

    "Authorization": Bearer ${localStorage.getItem("token")},

    "Content-Type": "application/json"

  }

})

.then(response => console.log(response.data))

.catch(error => console.error("Axios Request Error:", error));
```

Axios fournit également des raccourcis avec des méthodes comme `axios.get`, `axios.post`, `axios.put`, `axios.patch`, et `axios.delete`, comme montré ci-dessous :

```javascript
// Requête POST

axios.post("https://api.example.com/users",

  { name: "Abdullah", age: 25 }, // Corps de la requête

  { headers: { "Content-Type": "application/json" } }

)

.then(response => console.log(response.data))

.catch(error => console.error("Axios POST Error:", error));

// Requête PUT

axios.put("https://api.example.com/users/123",

  { name: "Updated Name" }, // Données mises à jour

  { headers: { "Authorization": Bearer ${localStorage.getItem("token")} } }

)

.then(response => console.log(response.data))

.catch(error => console.error("Axios PUT Error:", error));

// Requête DELETE

axios.delete("https://api.example.com/users/123", {

  headers: { "Authorization": Bearer ${localStorage.getItem("token")} }

})

.then(response => console.log("User deleted successfully"))

.catch(error => console.error("Axios DELETE Error:", error));
```

### **Limitations d'Axios**

#### Taille de bundle légèrement plus grande

Axios [ajoute 35 kb](https://bundlephobia.com/package/axios@1.8.4) de bundle supplémentaire, tandis que FetchAPI n'ajoute rien. Bien qu'Axios offre clairement plus de fonctionnalités que Fetch dans toutes les autres métriques, vous devez vous contenter de la taille de bundle plus grande. Et à une époque où les applications légères et rapides sont souvent préférées, vous ne voudrez peut-être pas de cette charge.

#### Dépendance à la maintenance tierce

Dépendre d'une option tierce pour quelque chose d'aussi crucial que l'API peut ne pas être souhaitable. Donc, un outil natif comme l'API Fetch, intégré dans JavaScript, offre plus de fiabilité.

## **Alova**

[Alova](https://github.com/alovajs/alova) est une bibliothèque de gestion de requêtes qui combine la récupération simple d'API avec d'autres fonctionnalités comme la gestion d'état, les hooks et la mise en cache, parmi beaucoup d'autres.

Alors que nous utilisons `react-query` et `SWR` pour traiter les données récupérées par Axios, Alova vous évite ces installations et codages supplémentaires en fournissant ces méthodes nativement. L'alternative tout-en-un ne se contente pas de récupérer des réponses et d'envoyer des requêtes, mais fusionne également les requêtes, met en cache les réponses et les optimise pour les frameworks UI.

Créé en 2022, l'adoption d'Alova est encore récente mais semble néanmoins prometteuse. Il est supporté sur les navigateurs, Node.js et la plupart des frameworks, y compris Vue, React, Svelte et JavaScript vanilla. Mais il a une utilisation limitée pour Angular.js.

[À seulement 10kb](https://bundlephobia.com/package/alova@2.6.1), il est environ 3 fois plus petit qu'Axios, ce qui en fait une alternative plus légère pour construire des applications rapides.

Vous pouvez également utiliser Alova pour soit remplacer react-query pour faciliter Axios, soit être la solution tout-en-un pour tout ce qui concerne l'intégration d'API.

Voici une simple récupération Alova :

```javascript
const response = await alovaInstance.Get('https://jsonplaceholder.typicode.com').send();

console.log(response); // Données de réponse
```

Lorsque vous récupérez Alova sur des composants React, vous pouvez utiliser `createAlova()` pour définir des paramètres et `useRequest()` pour gérer l'état.

```javascript
import React from "react";

import { createAlova, useRequest } from "alova";

import GlobalFetch from "alova/GlobalFetch";

// Initialiser Alova

const alovaInstance = createAlova({

  statesHook: React,

  requestAdapter: GlobalFetch(),

});

// Requête GET avec useRequest

const Profile = () => {

  const { data, loading, error } = useRequest(() => alovaInstance.Get("https://jsonplaceholder.typicode.com"));

  if (loading) return <p>Chargement...</p>;

  if (error) return <p>Erreur lors de la récupération du profil</p>;

  return <div>Nom d'utilisateur : {data.username}</div>;

};

export default Profile;
```

### **Caractéristiques clés d'Alova**

#### Solution tout-en-un

Pour certaines fonctionnalités intégrées à Alova, l'API Fetch ou Axios pourraient avoir besoin de bibliothèques supplémentaires comme `react-query` ou `SWR` pour les remplir.

#### Partage de requêtes pour éviter les requêtes redondantes

Alova fusionne les requêtes identiques. Supposons que plusieurs composants demandent les mêmes données à l'API. L'API Fetch et Axios envoient plusieurs requêtes identiques au serveur, ce qui crée du trafic. Mais Alova les fusionne, envoie une seule requête et partage sa réponse à travers tous les composants, ce qui réduit le trafic réseau.

#### Gestion d'état

Avec des outils comme l'API Fetch et Axios, vous devez gérer les données, le chargement et les états d'erreur manuellement. Alova vous permet de le faire en cours de route en une seule ligne de code. Voici à quoi cela ressemble :

```javascript
//...

const { data, loading, error } = useRequest(alova.Get("/posts/1"));

//...
```

#### Gestion avancée des requêtes

Alova offre plusieurs fonctionnalités de gestion des requêtes, chacune adaptée à des cas d'utilisation spécifiques. Avec sa gestion des requêtes, vous pouvez précharger des données à utiliser plus tard, mettre en cache des données pour éviter le rechargement, gérer la soumission de formulaires, gérer la pagination et automatiser le rafraîchissement lorsque nécessaire. Consultez leur documentation pour [en savoir plus](https://alova.js.org/tutorial/client/strategy/).

#### Mise en cache multi-niveaux

Vous pouvez également utiliser Alova pour mettre en cache des données, surtout lorsque la réponse ne change pas constamment et n'a pas besoin d'être rafraîchie. Contrairement à `react-query` qui stocke simplement les caches en RAM, Alova offre un cadre plus flexible.

Ses trois modes de mise en cache incluent le mode mémoire, le mode d'occupation de cache et le mode de récupération. Alors que le mode mémoire stocke les données en RAM, le mode de récupération les stocke de manière persistante dans un stockage local et les rend disponibles pour des périodes plus longues et même hors ligne. Pendant ce temps, le mode d'occupation empêche les requêtes en double ou redondantes arrivant en succession rapide.

Indépendamment de tout composant, les données mises en cache peuvent être accessibles n'importe où dans l'application si l'URL de la requête et les paramètres correspondent. Ces fonctionnalités réduisent le trafic allant vers les serveurs, diminuent la mise en mémoire tampon et aident à faciliter une expérience utilisateur plus rapide et meilleure.

```javascript
//...

// Initialiser l'instance Alova

const alovaInstance = createAlova({

  baseURL: "https://jsonplaceholder.typicode.com",

  statesHook: React,

  requestAdapter: GlobalFetch(),

});

// Définir la requête GET

const getPosts = alovaInstance.Get("/posts", {

  cache: {

    mode: "memory", // Met en cache en mémoire

    expires: 1000 * 60 * 5, // Expire dans 5 minutes

  },

});

const PostList = () => {

  const { data, loading, error } = useRequest(getPosts);

  if (loading) return <p>Chargement...</p>;

  if (error) return <p>Erreur lors de la récupération des données</p>;

  //...

};
```

Dans l'exemple ci-dessus, Alova met en cache la réponse en utilisant le mode mémoire `cache: {mode: "memory"}` et définit l'expiration du cache à 5 minutes `expires: 1000 * 60 * 5`. Vous pouvez changer `"memory"` en `"recovery"` si vous voulez une durée de stockage plus longue.

#### Flexibilité d'utilisation

Vous pouvez utiliser Alova avec Axios ou l'API Fetch. Voici un exemple où j'ai récupéré des données en utilisant Axios et les ai complétées avec la gestion d'état d'Alova.

```javascript
//...

// Initialiser Alova

const alovaInstance = createAlova({

  statesHook: React,

  requestAdapter: GlobalFetch(),

});

// Gérer l'état avec Alova

const { data: posts, setData } = useSnapshot([]);

const fetchPosts = async () => {

  const response = await axios.get("https://jsonplaceholder.typicode.com/posts");

  setData(response.data); // Stocker les données dans l'état Alova

};

//...
```

#### Prend en charge d'autres méthodes

Alova fait également de `GET` son option par défaut tout en supportant d'autres méthodes comme `POST`, `PATCH`, `PUT` et `DELETE`. Voici comment utiliser `POST` dans Alova, par exemple :

```javascript
import React, { useState } from "react";

import { createAlova, useRequest } from "alova";

import GlobalFetch from "alova/GlobalFetch";

const alovaInstance = createAlova({

  baseURL: "https://jsonplaceholder.typicode.com",

  statesHook: React,

  requestAdapter: GlobalFetch(),

});

const PostForm = () => {

  const [title, setTitle] = useState("");

  const { send: createPost } = useRequest(alovaInstance.Post("/posts", { title }), { immediate: false });

  createPost().then(console.log)

};

export default PostForm;
```

Bien sûr, il a aussi des méthodes abrégées :

```javascript
import React, { useState } from "react";

import { createAlova, useRequest } from "alova";

import GlobalFetch from "alova/GlobalFetch";

const alova = createAlova({

  baseURL: "https://jsonplaceholder.typicode.com",

  statesHook: React,

  requestAdapter: GlobalFetch(),

});

const { send: createPost } = useRequest(alova.Post("/posts", { title: "New Post" }), { immediate: false });

const { send: updatePost } = useRequest(alova.Put("/posts/1", { title: "Updated Post" }), { immediate: false });

const { send: patchPost } = useRequest(alova.Patch("/posts/1", { title: "Patched Post" }), { immediate: false });

createPost().then(console.log);

updatePost().then(console.log);

patchPost().then(console.log);
```

#### Taille du bundle

Alova est trois fois plus petit qu'Axios, mais cela ne raconte même pas toute l'histoire. Avec Axios et l'API Fetch, vous avez besoin de différentes bibliothèques pour gérer la mise en cache, la déduplication des requêtes et les nouvelles tentatives. Mais Alova a tout intégré. Donc, utiliser Axios et l'API Fetch en production de code réel nécessitera toujours plus de bundles qu'Axios. Et globalement, Alova facilite des applications plus légères par rapport à Axios et parfois à l'API Fetch également.

### **Limitations d'Alova**

#### Adoption encore faible

Lors de la rédaction de cet article, j'ai eu du mal à obtenir suffisamment de ressources sur Alova. Et cela est dû au fait qu'il n'a été lancé qu'en juillet 2022, ce qui signifie que l'adoption est encore récente. Donc, le dépannage d'Alova pourrait être problématique puisque les communautés d'API thématiques Alova sont moins nombreuses, ainsi que les réponses StackOverflow, les tutoriels YouTube ou les contributions GitHub.

#### Risques potentiels de stabilité et de maintenance à long terme

Les bibliothèques plus récentes ont un risque plus élevé d'abandon. Axios existe depuis des années, tandis qu'Alova est encore en croissance. De plus, il a moins de cas d'utilisation en production et d'applications testées en conditions réelles par rapport à Axios et Fetch.

#### Courbe d'apprentissage

La courbe d'apprentissage d'Alova peut prendre un certain temps d'adaptation car elle gère les requêtes API différemment des outils comme Axios ou l'API Fetch.

Au lieu de faire des requêtes directement, vous travaillez avec des instances de requêtes et gérez l'état dans le système d'Alova. Cela nécessite d'apprendre de nouvelles façons de structurer les appels API et d'utiliser des fonctionnalités comme la mise en cache et la fusion des requêtes. Bien que cela puisse sembler inhabituel au début, cela peut aider à réduire les appels API redondants et améliorer les performances une fois que vous le comprenez.

#### Moins d'intégrations tierces

Alova a moins de bibliothèques tierces construites spécifiquement pour lui, nécessitant plus de travail manuel pour la compatibilité avec les outils existants.

## **Comparaison fonction par fonction**

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Fonctionnalité</strong></p></td><td colspan="1" rowspan="1"><p><strong>API Fetch</strong></p></td><td colspan="1" rowspan="1"><p><strong>Axios</strong></p></td><td colspan="1" rowspan="1"><p><strong>Alova</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Facilité d'utilisation</strong></p></td><td colspan="1" rowspan="1"><p>Moyenne (nécessite une gestion manuelle)</p></td><td colspan="1" rowspan="1"><p>Élevée (syntaxe conviviale)</p></td><td colspan="1" rowspan="1"><p>Moyenne (nécessite de nouveaux modèles)</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Performance</strong></p></td><td colspan="1" rowspan="1"><p>Élevée (légère, native)</p></td><td colspan="1" rowspan="1"><p>Moyenne (taille légèrement plus grande)</p></td><td colspan="1" rowspan="1"><p>Élevée (optimisée pour la mise en cache et les requêtes par lots)</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Gestion du JSON</strong></p></td><td colspan="1" rowspan="1"><p>Analyse manuelle (.json())</p></td><td colspan="1" rowspan="1"><p>Automatique</p></td><td colspan="1" rowspan="1"><p>Automatique</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Annulation de requête</strong></p></td><td colspan="1" rowspan="1"><p>AbortController (manuel)</p></td><td colspan="1" rowspan="1"><p>Intégré avec CancelToken</p></td><td colspan="1" rowspan="1"><p>Intégré</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Intercepteurs</strong></p></td><td colspan="1" rowspan="1"><p>Non</p></td><td colspan="1" rowspan="1"><p>Oui</p></td><td colspan="1" rowspan="1"><p>Oui</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Gestion des délais d'attente</strong></p></td><td colspan="1" rowspan="1"><p>Non (manuel avec AbortController)</p></td><td colspan="1" rowspan="1"><p>Oui (intégré)</p></td><td colspan="1" rowspan="1"><p>Oui (intégré)</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Mise en cache des données</strong></p></td><td colspan="1" rowspan="1"><p>Non</p></td><td colspan="1" rowspan="1"><p>Non (nécessite une mise en cache tierce)</p></td><td colspan="1" rowspan="1"><p>Oui (intégré)</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Mécanisme de nouvelle tentative</strong></p></td><td colspan="1" rowspan="1"><p>Non</p></td><td colspan="1" rowspan="1"><p>Oui</p></td><td colspan="1" rowspan="1"><p>Oui</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Gestion des erreurs</strong></p></td><td colspan="1" rowspan="1"><p>Nécessite une gestion manuelle</p></td><td colspan="1" rowspan="1"><p>Rejet automatique pour les codes de statut non-2xx</p></td><td colspan="1" rowspan="1"><p>Récupération d'erreur intégrée</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Support des navigateurs</strong></p></td><td colspan="1" rowspan="1"><p>Tous les navigateurs modernes</p></td><td colspan="1" rowspan="1"><p>Tous les navigateurs modernes</p></td><td colspan="1" rowspan="1"><p>Tous les navigateurs modernes</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Support de Node.js</strong></p></td><td colspan="1" rowspan="1"><p>Oui</p></td><td colspan="1" rowspan="1"><p>Oui</p></td><td colspan="1" rowspan="1"><p>Limité</p></td></tr></tbody></table>

## **Cas d'utilisation et meilleurs scénarios**

Choisir le bon client HTTP pour votre projet dépend de plusieurs facteurs, y compris la complexité du projet, les dépendances et les considérations de performance. Explorons quand il est préférable d'utiliser l'API Fetch, Axios ou Alova.

### Quand utiliser l'API Fetch

1. #### Adapté aux projets légers et aux requêtes simples

L'API Fetch est intégrée aux navigateurs modernes et est idéale pour gérer les requêtes HTTP de base sans ajouter de dépendances. Si votre projet nécessite uniquement des requêtes GET, POST ou DELETE simples avec des configurations minimales, l'API Fetch est un excellent choix.

2. #### Lorsque vous travaillez dans des environnements où les bibliothèques tierces sont restreintes

Certaines applications d'entreprise ou sensibles à la sécurité peuvent restreindre l'utilisation de bibliothèques externes. Puisque l'API Fetch est intégrée au navigateur, elle reste une option viable lorsque les paquets tiers comme Axios ou Alova ne sont pas autorisés.

3. #### Lorsque des dépendances minimales sont préférées

Puisque l'API Fetch est native à JavaScript, elle ne nécessite pas l'installation de bibliothèques supplémentaires, ce qui la rend parfaite pour les projets qui doivent garder les dépendances faibles. Cela peut être particulièrement bénéfique pour les petites applications légères ou les sites web statiques.

### Quand utiliser Axios

1. #### Idéal pour les applications backend-lourdes ou les API complexes

Pour les projets qui nécessitent plusieurs appels API, une gestion des erreurs et une gestion efficace des requêtes, Axios est un choix solide. Il permet des requêtes concurrentes, l'annulation de requêtes et un meilleur contrôle sur les en-têtes HTTP.

2. #### Lorsque l'analyse JSON automatique, les intercepteurs et la gestion robuste des erreurs sont nécessaires

Axios simplifie le travail avec les données JSON en analysant automatiquement les réponses. Il fournit également des intercepteurs intégrés pour les transformations de requêtes et de réponses, ainsi qu'une gestion supérieure des erreurs par rapport à l'API Fetch.

3. #### Utile lorsque vous travaillez avec Node.js dans des applications full-stack

Axios fonctionne à la fois dans le navigateur et dans Node.js, ce qui en fait un excellent choix pour les applications full-stack où un client API unifié est nécessaire entre le frontend et le backend.

### Quand utiliser Alova

1. #### Lorsque vous travaillez avec des applications frontend-lourdes (React, Vue, Svelte)

Alova s'intègre bien avec les frameworks frontend et les outils de gestion d'état, ce qui en fait un excellent choix pour les applications monopages (SPA) qui dépendent de la récupération de données fluide, de la pagination et des mises à jour.

2. #### Meilleur pour les projets nécessitant une mise en cache optimisée et une synchronisation des données

Alova est conçu pour l'optimisation des performances et de meilleures stratégies de mise en cache. Il est adapté aux applications qui reposent sur la synchronisation des données en temps réel et qui doivent minimiser les requêtes réseau redondantes.

3. #### Lorsque l'optimisation des performances et la réduction de la charge réseau sont des priorités

Avec ses mécanismes de mise en cache intelligents, Alova peut réduire considérablement la fréquence des appels API, améliorant ainsi les performances globales de l'application. Il est particulièrement utile dans les scénarios où l'efficacité du réseau est cruciale, comme les applications mobiles ou les applications web progressives (PWA).

## **Communauté et écosystème**

La communauté et l'écosystème entourant un client HTTP peuvent influencer la facilité d'utilisation, les ressources d'apprentissage disponibles et l'intégration avec d'autres outils. Explorons comment l'API Fetch, Axios et Alova sont perçus en 2025.

### **Écosystème et intégrations**

Bien que l'API Fetch soit largement supportée, les développeurs la complètent souvent avec des bibliothèques supplémentaires pour améliorer la mise en cache, les délais d'attente et la mise en file d'attente des requêtes. Cela peut entraîner un effort de développement accru par rapport à l'utilisation d'une solution clé en main comme Axios ou Alova.

Pendant ce temps, Axios bénéficie d'un écosystème bien établi avec une variété de plugins et d'extensions, ce qui facilite son intégration avec différentes architectures backend, systèmes d'authentification et outils de surveillance des requêtes.

Alova est conçu pour fonctionner de manière transparente avec les bibliothèques modernes de gestion d'état telles que React Query et Vue Query. Ces intégrations en font un choix attrayant pour les développeurs axés sur l'optimisation des stratégies de récupération de données frontend.

## **Conclusion**

Choisir entre l'API Fetch, Axios et Alova dépend des besoins et des priorités de votre projet. L'API Fetch est idéale pour les applications légères nécessitant des dépendances minimales, tandis qu'Axios est un choix robuste pour les applications full-stack et les environnements backend-lourds. Alova, quant à lui, est une excellente option pour optimiser la récupération de données et la mise en cache dans les applications axées sur le frontend.

Alors que les développeurs explorent de nouvelles façons d'améliorer les performances et de réduire la charge réseau, l'adoption d'Alova devrait croître, en particulier dans les SPA et les PWA. Mais Axios reste une solution fiable et largement adoptée, tandis que l'API Fetch continue d'être le bloc de construction fondamental pour les requêtes HTTP en JavaScript.