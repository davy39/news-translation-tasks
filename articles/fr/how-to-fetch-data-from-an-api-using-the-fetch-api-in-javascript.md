---
title: Comment récupérer des données d'une API en utilisant l'API Fetch en JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-27T21:01:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-fetch-data-from-an-api-using-the-fetch-api-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Beige-Aesthetic-Brand-Guidelines-Presentation.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Comment récupérer des données d'une API en utilisant l'API Fetch en JavaScript
seo_desc: "Interacting with external APIs, or Application Programming Interfaces,\
  \ has become an essential skill in web development. \nAPIs allow different software\
  \ applications to communicate with each other, enabling developers to access and\
  \ retrieve data from ..."
---

Interagir avec des API externes, ou interfaces de programmation d'applications, est devenu une compétence essentielle dans le développement web.

Les API permettent à différentes applications logicielles de communiquer entre elles, permettant aux développeurs d'accéder et de récupérer des données à partir de diverses sources.

Une méthode populaire pour effectuer des requêtes API en JavaScript consiste à utiliser l'API Fetch. Dans cet article, nous allons explorer ce qu'est l'API Fetch, comment elle fonctionne, et je vais fournir des exemples pratiques pour vous guider à travers la récupération de données d'une API en utilisant cet outil puissant.

## Comment fonctionne l'API Fetch

L'API Fetch est une interface JavaScript moderne pour effectuer des requêtes réseau, principalement conçue pour remplacer l'ancienne XMLHttpRequest. Elle offre une manière plus simple et flexible de gérer les requêtes HTTP, facilitant ainsi le travail des développeurs avec les API et la récupération de données à partir de serveurs.

### Syntaxe de base de l'API Fetch

Avant de plonger dans des exemples pratiques, examinons la syntaxe de base de l'API Fetch.

La fonction `fetch()` est au cœur de cette API, et elle prend un argument obligatoire : l'URL de la ressource que vous souhaitez récupérer. Optionnellement, vous pouvez inclure un objet comme deuxième argument, où vous pouvez spécifier divers paramètres tels que la méthode HTTP, les en-têtes, et plus encore.

Voici un exemple simple d'une requête fetch de base :

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erreur :', error));
```

Dans cet exemple, nous récupérons des données à partir de `https://api.example.com/data`. La méthode `then()` est utilisée pour gérer la réponse, la convertissant en JSON à l'aide de la méthode `json()`. Le deuxième bloc `then()` enregistre les données récupérées dans la console, et le bloc `catch()` gère les erreurs si la requête échoue.

## Comment effectuer une requête GET

Le type de requête le plus courant lors de l'utilisation des API est la requête GET. Elle est utilisée pour récupérer des données à partir d'un serveur. Passons en revue un exemple de réalisation d'une requête GET simple en utilisant l'API Fetch.

### Exemple : Récupération des données utilisateur

Supposons que nous voulons récupérer des informations sur un utilisateur à partir d'une API hypothétique. Voici comment vous pouvez le faire :

```javascript
// Spécifiez le point de terminaison de l'API pour les données utilisateur
const apiUrl = 'https://api.example.com/users/123';

// Effectuez une requête GET en utilisant l'API Fetch
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(userData => {
    // Traitez les données utilisateur récupérées
    console.log('Données utilisateur :', userData);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
```

Dans cet exemple, nous définissons le point de terminaison de l'API pour les données utilisateur (`https://api.example.com/users/123`). La fonction fetch est utilisée pour effectuer la requête GET, et nous gérons la réponse en vérifiant si elle est correcte à l'aide de la propriété `response.ok`. Si la réponse est correcte, nous la convertissons en JSON et traitons les données utilisateur.

## Comment effectuer une requête POST

Alors que les requêtes GET sont utilisées pour récupérer des données, les requêtes POST sont utilisées pour envoyer des données à un serveur. Cela est couramment utilisé lors de la soumission de formulaires ou de l'envoi de données pour créer une nouvelle ressource. Explorons comment effectuer une requête POST en utilisant l'API Fetch.

### Exemple : Envoi de données de formulaire

Supposons que nous avons un formulaire simple avec les détails de l'utilisateur, et que nous voulons envoyer ces données à un serveur pour créer un nouvel utilisateur. Voici comment vous pouvez effectuer une requête POST :

```javascript
// Point de terminaison de l'API pour créer un nouvel utilisateur
const apiUrl = 'https://api.example.com/users';

// Données de formulaire à envoyer dans le corps de la requête
const formData = {
  username: 'john_doe',
  email: 'john@example.com',
  password: 'securepassword123',
};

// Effectuez une requête POST en utilisant l'API Fetch
fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(formData),
})
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(newUserData => {
    // Traitez les données du nouvel utilisateur créé
    console.log('Données du nouvel utilisateur :', newUserData);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
```

Dans cet exemple, nous spécifions le point de terminaison de l'API pour créer un nouvel utilisateur (`https://api.example.com/users`). Nous utilisons la propriété `method` dans les options de fetch pour la définir comme une requête POST. De plus, nous incluons la propriété `headers` pour indiquer que nous envoyons des données JSON dans le corps de la requête.

## Comment gérer les paramètres de requête

Souvent, lors de l'utilisation des API, vous devez inclure des paramètres de requête dans vos requêtes pour filtrer ou modifier les données que vous recevez. Explorons comment gérer les paramètres de requête lors de l'exécution d'une requête GET.

### Exemple : Filtrer les données avec des paramètres de requête

Supposons que nous voulons récupérer une liste d'utilisateurs en fonction de critères spécifiques, tels que les utilisateurs qui se sont inscrits au cours des 30 derniers jours. Nous pouvons y parvenir en incluant des paramètres de requête dans l'URL :

```javascript
// Point de terminaison de l'API pour récupérer les utilisateurs récents
const apiUrl = 'https://api.example.com/users/recent';

// Configurer les paramètres de requête
const queryParams = {
  timeframe: '30days',
};

// Convertir les paramètres de requête en une chaîne
const queryString = new URLSearchParams(queryParams).toString();

// Combiner le point de terminaison de l'API avec les paramètres de requête
const fullUrl = `${apiUrl}?${queryString}`;

// Effectuer une requête GET en utilisant l'API Fetch
fetch(fullUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(recentUsers => {
    // Traiter la liste des utilisateurs récents
    console.log('Utilisateurs récents :', recentUsers);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
```

Dans cet exemple, nous définissons le point de terminaison de l'API pour récupérer les utilisateurs récents (`https://api.example.com/users/recent`). Nous configurons les paramètres de requête à l'aide d'un objet (`queryParams`) et les convertissons en une chaîne à l'aide de `URLSearchParams`. La chaîne résultante est ensuite ajoutée au point de terminaison de l'API pour former l'URL complète.

## Comment gérer l'authentification

De nombreuses API nécessitent une authentification pour accéder à des ressources protégées. L'API Fetch fournit un moyen d'inclure des informations d'authentification dans vos requêtes à l'aide d'en-têtes. Explorons comment gérer l'authentification lors de l'exécution d'une requête.

### Exemple : Ajout d'en-têtes d'authentification

Supposons que nous avons une API qui nécessite une clé API pour l'authentification. Voici comment vous pouvez inclure la clé API dans les en-têtes de la requête :

```javascript
// Point de terminaison de l'API nécessitant une authentification
const apiUrl = 'https://api.example.com/protected/resource';

// Clé API pour l'authentification
const apiKey = 'your-api-key';

// Effectuer une requête GET avec authentification en utilisant l'API Fetch
fetch(apiUrl, {
  headers: {
    Authorization: `Bearer ${apiKey}`,
  },
})
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(protectedData => {
    // Traiter les données protégées
    console.log('Données protégées :', protectedData);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
```

Dans cet exemple, nous incluons la clé API dans les en-têtes de la requête à l'aide de l'en-tête `Authorization`. Le mot-clé `Bearer` est couramment utilisé pour l'authentification par clé API, suivi de la clé API réelle.

## Gérer le code asynchrone

Une chose importante à noter lors de l'utilisation de l'API Fetch est qu'elle fonctionne de manière asynchrone. Cela signifie que lorsque vous effectuez une requête, le code JavaScript n'attend pas la réponse mais continue de s'exécuter. Pour gérer la nature asynchrone de l'API Fetch, nous utilisons des promesses.

### Exemple : Chaînage de plusieurs requêtes

Supposons que nous devons récupérer des données à partir de deux points de terminaison d'API différents et traiter les résultats ensemble. Nous pouvons utiliser le modèle de chaînage de promesses pour y parvenir :

```javascript
// Points de terminaison de l'API
const apiUrl1 = 'https://api.example.com/data1';
const apiUrl2 = 'https://api.example.com/data2';

// Récupérer les données du premier point de terminaison de l'API
fetch(apiUrl1)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(data1 => {
    // Traiter les données du premier point de terminaison de l'API
    console.log('Données de l\'API 1 :', data1);

    // Récupérer les données du deuxième point de terminaison de l'API
    return fetch(apiUrl2);
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'était pas correcte');
    }
    return response.json();
  })
  .then(data2 => {
    // Traiter les données du deuxième point de terminaison de l'API
    console.log('Données de l\'API 2 :', data2);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
```

Dans cet exemple, nous récupérons les données du premier point de terminaison de l'API (`apiUrl1`) et les traitons. Ensuite, nous utilisons la promesse retournée pour effectuer une autre requête fetch vers le deuxième point de terminaison de l'API (`apiUrl2`) et traiter ses données. Ce modèle de chaînage nous permet de gérer plusieurs requêtes asynchrones de manière séquentielle.

## Gestion des erreurs

La gestion des erreurs est une partie cruciale de la création d'applications robustes. L'API Fetch fournit un moyen pratique de capturer et de gérer les erreurs qui peuvent survenir lors d'une requête réseau.

### Exemple : Gestion des erreurs

Modifions nos exemples précédents pour inclure une gestion des erreurs plus complète :

```javascript
// Point de terminaison de l'API pour les données utilisateur
const apiUrl = 'https://api.example.com/users/123';

// Effectuer une requête GET en utilisant l'API Fetch
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
    }
    return response.json();
  })
  .then(userData => {
    // Traiter les données utilisateur récupérées
    console.log('Données utilisateur :', userData);
  })
  .catch(error => {
    console.error('Erreur :', error.message);
  });
```

Dans cet exemple modifié, nous incluons des informations supplémentaires sur le statut HTTP dans le message d'erreur lorsque la réponse n'est pas correcte. Cela peut être utile pour le débogage et fournir plus de contexte sur la nature de l'erreur.

## Conclusion

Dans cet article, nous avons couvert les bases de la récupération de données d'une API en utilisant l'API Fetch en JavaScript. Nous avons commencé par explorer les concepts fondamentaux de l'API Fetch, tels que sa syntaxe et comment effectuer des requêtes GET et POST. Nous avons ensuite approfondi la gestion des paramètres de requête, de l'authentification et du code asynchrone.

Travailler avec des API est une compétence cruciale pour les développeurs web, et l'API Fetch offre une manière simple et puissante d'interagir avec des sources de données externes. Alors que vous continuez à explorer le développement web, la pratique et la mise en œuvre de ces concepts dans des projets réels renforceront votre compréhension de la récupération de données à partir d'API en utilisant JavaScript. Bon codage !