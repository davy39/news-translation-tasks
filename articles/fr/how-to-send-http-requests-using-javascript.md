---
title: Comment envoyer des requêtes HTTP en utilisant JavaScript
subtitle: ''
author: Eric Hu
co_authors: []
series: null
date: '2024-07-10T17:06:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-http-requests-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/js-http.png
tags:
- name: http
  slug: http
- name: JavaScript
  slug: javascript
seo_title: Comment envoyer des requêtes HTTP en utilisant JavaScript
seo_desc: Nowadays, the interaction between web applications relies on HTTP. For instance,
  let's say you have an online shop application and you want to create a new product.
  You have to fill in all the necessary information and probably click on a button
  that...
---

De nos jours, l'interaction entre les applications web repose sur [HTTP](https://www.freecodecamp.org/news/what-is-http/). Par exemple, imaginons que vous avez une application de boutique en ligne et que vous souhaitez créer un nouveau produit. Vous devez remplir toutes les informations nécessaires et probablement cliquer sur un bouton qui dit "Créer".

Cette action enverra une requête HTTP au backend, avec toutes les données nécessaires, et l'application backend utilisera ces données pour apporter des modifications à la base de données. Une fois l'action terminée, qu'elle soit réussie ou non, une réponse HTTP sera renvoyée au frontend, qui agira en conséquence en fonction du statut de cette réponse.

Lorsque ces requêtes et réponses sont transférées d'un bout à l'autre, elles doivent suivre un certain format afin que les deux extrémités puissent se comprendre. HTTP a été créé à cette fin. Il s'agit d'un protocole réseau standard qui permet aux applications web de se comprendre et de communiquer entre elles.

## Quelles sont les méthodes de requête HTTP ?

Il existe plusieurs méthodes que vous pouvez utiliser pour envoyer une requête HTTP, et chacune d'entre elles sert un but différent, comme montré ci-dessous :

### La méthode `GET`

La méthode `GET` est utilisée pour demander des données et des ressources au serveur. Lorsque vous envoyez une requête `GET`, les paramètres de requête sont intégrés dans l'URL sous forme de paires nom/valeur comme ceci :

```text
http://example.com/index.html?name1=value1&name2=value2
```

Notez que le point d'interrogation (`?`) indique le début d'une liste de paramètres. Chaque paramètre forme une paire clé/valeur (`name=value`), et le esperluette (`&`) est utilisé pour séparer deux paramètres différents.

### La méthode `POST`

La méthode `POST` est utilisée pour envoyer des données au serveur, soit pour ajouter une nouvelle ressource, soit pour mettre à jour une ressource existante. Les paramètres sont stockés dans le corps de la requête HTTP.

```text
POST /index.html HTTP/1.1
Host: example.com
name1=value1&name2=value2
```

### La méthode `DELETE`

Cette méthode supprime une ressource du serveur.

### La méthode `HEAD`

La méthode `HEAD` fonctionne exactement comme `GET`, sauf que la réponse HTTP envoyée par le serveur ne contiendra que l'en-tête mais pas le corps. Cela signifie que si le serveur est "OK" avec la requête, il vous donnera une réponse `200 OK` mais pas la ressource que vous avez demandée. Vous ne pouvez récupérer la ressource qu'avec la méthode `GET`.

Cela est très utile lorsque vous testez si le serveur fonctionne. Parfois, la ressource peut prendre beaucoup de temps à être transmise, et à des fins de test, vous n'avez besoin que d'une réponse `200 OK` pour savoir que tout fonctionne correctement.

### La méthode `PUT`

La méthode `PUT` est utilisée pour mettre à jour des ressources existantes, et elle est similaire à la méthode `POST` avec une petite différence.

Lorsque vous `PUT` une ressource qui existe déjà, l'ancienne ressource sera écrasée. Et faire plusieurs requêtes `PUT` identiques aura le même effet que de le faire une seule fois.

Lorsque vous `POST` des ressources identiques, cette ressource sera dupliquée à chaque fois que la requête est faite.

## Qu'est-ce que l'API Fetch ?

Pendant longtemps, la communauté JavaScript manquait d'une méthode standard pour envoyer des requêtes HTTP. Certaines personnes utilisaient `XMLHttpRequest`, également connu sous le nom d'AJAX, tandis que d'autres préféraient des bibliothèques externes telles qu'Axios ou jQuery.

L'API Fetch a été introduite en 2015 comme la méthode moderne, simplifiée et standard d'envoi de requêtes HTTP en utilisant JavaScript. Elle est supportée nativement, donc il n'est pas nécessaire d'installer des bibliothèques tierces.

## Comment envoyer une requête GET en utilisant JavaScript

L'API Fetch est [basée sur les promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), ce qui signifie qu'elle offre une syntaxe claire et concise pour écrire des opérations asynchrones. Par exemple, voici comment vous pouvez envoyer une requête `GET` en utilisant l'API Fetch.

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
  .then((response) => {
    // Si la réponse n'est pas 2xx, lancer une erreur
    if (!response.ok) {
      throw new Error("La réponse du réseau n'était pas correcte");
    }

    // Si la réponse est 200 OK, retourner la réponse au format JSON.
    return response.json();
  })
  .then((data) => console.log(data)) // Vous pouvez continuer à faire quelque chose avec la réponse.
  .catch((error) => console.error("Erreur de Fetch :", error)); // En cas d'erreur, elle sera capturée et enregistrée.
```

Vous pouvez également inclure des options personnalisées avec la requête, telles que des en-têtes personnalisés, des jetons d'autorisation, etc.

```javascript
fetch("https://jsonplaceholder.typicode.com/users", {
  headers: {
    "Content-Type": "application/json",
    "Authorization": "votre-jeton-ici",
  },
  credentials: "same-origin",
})
  .then(. . .);
```

## Comment envoyer une requête POST en utilisant JavaScript

Lorsque vous envoyez une requête `POST`, les choses deviennent un peu plus complexes car vous devez envoyer des données au serveur avec le corps de la requête. Cela peut devenir compliqué en fonction du type de données que vous envoyez et de votre cas d'utilisation spécifique.

Par exemple, le code suivant envoie des données JSON au backend :

```javascript
fetch("https://jsonplaceholder.typicode.com/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: "John Doe",
    email: "johndoe@example.com",
  }),
});
```

Il y a quelques points auxquels vous devez prêter attention ici. Tout d'abord, vous devez spécifier explicitement la méthode de requête. Si vous omettez cela, la méthode `GET` par défaut sera utilisée.

De plus, le corps de la requête n'accepte que les données de type chaîne, vous devez donc utiliser la méthode `stringify()` pour convertir le JSON en chaîne avant de l'assigner au corps de la requête.

C'est aussi pourquoi il est important d'inclure l'en-tête `Content-Type`, qui permet à celui qui reçoit de savoir comment analyser le corps de la requête.

Cependant, les choses sont généralement plus complexes en pratique. Par exemple, lorsque vous travaillez avec des formulaires web, au lieu de JSON, vous utilisez probablement l'encodage de formulaire `x-www-form-urlencoded`, auquel cas la requête peut être envoyée comme ceci.

L'exemple suivant suppose que vous comprenez ce que sont les [gestionnaires d'événements](https://www.freecodecamp.org/news/dom-events-and-javascript-event-listeners/).

```javascript
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const usernameInput = document.getElementById("username");
  const emailInput = document.getElementById("email");

  const formData = new URLSearchParams();

  usernameInput.addEventListener("input", function () {
    formData.set("username", usernameInput.value);
  });

  emailInput.addEventListener("input", function () {
    formData.set("email", emailInput.value);
  });

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Empêcher l'action de soumission de formulaire par défaut

    await fetch("https://jsonplaceholder.typicode.com/users", {
      method: "POST",
      body: formData.toString(),
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  });
});
```

Si vous devez télécharger des fichiers vers le backend, vous aurez besoin de l'encodage de formulaire `multipart/form-data`.

```javascript
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("myForm");
  const usernameInput = document.getElementById("username");
  const emailInput = document.getElementById("email");
  const pictureInput = document.getElementById("picture");

  const formData = new FormData();

  usernameInput.addEventListener("input", function () {
    formData.set("username", usernameInput.value);
  });

  emailInput.addEventListener("input", function () {
    formData.set("email", emailInput.value);
  });

  pictureInput.addEventListener("change", function () {
    formData.set("picture", pictureInput.files[0]);
  });

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Empêcher la soumission de formulaire par défaut

    await fetch("https://jsonplaceholder.typicode.com/users", {
      method: "POST",
      body: formData,
    });
  });
});
```

Notez que lorsque vous utilisez `FormData()` pour construire le corps de la requête, le `Content-Type` sera verrouillé sur `multipart/form-data`. Dans ce cas, il n'est pas nécessaire de définir un en-tête `Content-Type` personnalisé.

## Comment envoyer une requête PUT en utilisant JavaScript

La requête `PUT` fonctionne de manière similaire à `POST`, mais vous devez vous souvenir de définir `method` sur `PUT`.

```javascript
fetch("https://jsonplaceholder.typicode.com/users", {
  method: "PUT",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    id: "123",
    name: "John Doe",
    email: "johndoe@example.com",
  }),
});
```

En réalité, vous devrez fournir un `id`, ou toute autre clé qui vous permet de localiser l'enregistrement à mettre à jour dans le backend.

## Comment envoyer une requête DELETE en utilisant JavaScript

La requête `DELETE` fonctionne de manière similaire à `PUT`, mais souvenez-vous de définir `method` sur `DELETE`.

```javascript
fetch("https://jsonplaceholder.typicode.com/users/123", {
  method: "DELETE",
});
```

Et de même, souvenez-vous de fournir un `id` afin que l'application backend sache quel enregistrement supprimer.

## Comment envoyer une requête en utilisant XMLHttpRequest (AJAX)

En plus de `fetch()`, il est également possible de faire une requête HTTP en utilisant `XMLHttpRequest`. L'exemple suivant montre comment faire une requête `GET` à l'endpoint `https://jsonplaceholder.typicode.com`

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://jsonplaceholder.typicode.com/users", true);
xhr.onload = function () {
  if (xhr.status >= 200 && xhr.status < 300) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.error("Erreur :", xhr.statusText);
  }
};
xhr.onerror = function () {
  console.error("La requête a échoué");
};
xhr.send();
```

La syntaxe est un peu plus complexe, car `XMLHttpRequest` repose sur des fonctions de rappel pour travailler avec des opérations asynchrones, ce qui signifie qu'il est facile de tomber dans ce que l'on appelle l'enfer des rappels, où vous avez des couches et des couches de fonctions de rappel, rendant votre base de code difficile à lire et à maintenir.

Cependant, `XMLHttpRequest` a certains avantages. En raison du fait que `XMLHttpRequest` est beaucoup plus ancien par rapport à `fetch()`, il est plus largement supporté. Vous devriez envisager d'utiliser `XMLHttpRequest` lorsque votre application web doit être compatible avec des navigateurs plus anciens.

## Comment envoyer une requête en utilisant des bibliothèques externes

En plus des méthodes intégrées, vous pouvez également envoyer des requêtes HTTP en utilisant des bibliothèques tierces. Par exemple, voici comment vous pouvez envoyer une requête `GET` en utilisant jQuery :

```javascript
$.get("https://api.example.com/data", function (data) {
  console.log(data);
}).fail(function (error) {
  console.error("Erreur :", error);
});
```

[jQuery](https://jquery.com/) est l'une des bibliothèques JavaScript les plus populaires. Elle vise à corriger la partie de JavaScript qui est difficile à utiliser, et elle a été assez réussie à cet égard.

Ces dernières années, jQuery a perdu une partie de sa popularité car le JavaScript vanilla s'est amélioré au fil des ans et les problèmes qui dérangeaient les gens ont été résolus. Ce n'est plus le choix de prédilection pour créer des applications JavaScript, surtout pour les nouveaux développeurs.

Alternativement, vous pourriez opter pour Axios, qui est un client HTTP basé sur les promesses tout comme `fetch()`, et il a été le préféré des gens pendant très longtemps avant l'arrivée de `fetch()`.

```javascript
axios
  .get("https://api.example.com/data")
  .then((response) => console.log(response.data))
  .catch((error) => console.error("Erreur Axios :", error));
```

[Axios](https://axios-http.com/docs/intro) et `fetch()` ont une syntaxe très similaire car ils sont tous deux basés sur les promesses. La principale différence entre eux est que `fetch()` est intégré, tandis qu'Axios nécessite l'installation d'une bibliothèque externe. Cependant, Axios est beaucoup plus riche en fonctionnalités, car il dispose d'intercepteurs de requête/réponse, de gestion automatique du JSON et de délais d'attente intégrés.

## Conclusion

Nous avons présenté quatre méthodes différentes pour envoyer des requêtes HTTP en utilisant JavaScript dans ce tutoriel. C'est à vous de décider laquelle est la meilleure pour votre projet.

L'API Fetch est la méthode moderne et standard pour envoyer des requêtes HTTP en utilisant JavaScript. Elle a une syntaxe relativement simple, ce qui rend votre projet plus facile à maintenir.

`XMLHttpRequest` est la méthode héritée pour envoyer des requêtes HTTP. Elle n'est généralement pas recommandée pour les nouveaux projets, mais si votre projet doit être compatible avec des navigateurs hérités, `XMLHttpRequest` peut encore être utile.

jQuery est un package externe qui peut faire beaucoup de choses, y compris envoyer des requêtes HTTP. Bien que l'importance de jQuery ait diminué ces dernières années, il est encore utilisé dans de nombreux projets plus anciens, et vous pourriez le rencontrer dans votre travail en tant que développeur JavaScript.

Axios est une bibliothèque tierce utilisée pour envoyer des requêtes HTTP. Elle a une syntaxe très similaire à l'API Fetch mais offre beaucoup plus de fonctionnalités avancées. C'est à vous de décider si vous avez besoin de ces fonctionnalités. Si ce n'est pas le cas, il est généralement recommandé d'utiliser `fetch()` à la place.

Pour en savoir plus sur JavaScript et le développement web, visitez [thedevspace.io](https://www.thedevspace.io)