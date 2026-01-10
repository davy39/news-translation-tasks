---
title: Comment appeler une API en JavaScript – avec des exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-03T18:34:49.000Z'
originalURL: https://freecodecamp.org/news/make-api-calls-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Brown-Aesthetic-Scrapbook-Vintage-Group-Project-Presentation.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Comment appeler une API en JavaScript – avec des exemples
seo_desc: "Calling an API (Application Programming Interface) in JavaScript is a fundamental\
  \ action that web developers need to know how to perform. It allows you to fetch\
  \ data from external sources and integrate it into your web applications. \nIn this\
  \ tutorial..."
---

Appeler une API (Application Programming Interface) en JavaScript est une action fondamentale que les développeurs web doivent savoir effectuer. Cela permet de récupérer des données à partir de sources externes et de les intégrer dans vos applications web. 

Dans ce tutoriel, je vais vous guider à travers le processus de réalisation d'appels API en JavaScript, étape par étape. À la fin de cet article, vous aurez une compréhension solide de la manière d'interagir avec les APIs dans vos projets JavaScript.

### Table des matières:

* [Qu'est-ce qu'une API ?](#heading-quest-ce-quune-api)
* [Comment choisir une API](#heading-comment-choisir-une-api)
* [Comment utiliser l'API Fetch pour les requêtes GET](#heading-comment-utiliser-lapi-fetch-pour-les-requetes-get)
* [Comment gérer les réponses](#heading-comment-gerer-les-reponses)
* [Gestion des erreurs dans les appels API](#heading-gestion-des-erreurs-dans-les-appels-api)
* [Comment faire des requêtes POST](#heading-comment-faire-des-requetes-post)
* [Comment travailler avec les clés API](#heading-comment-travailler-avec-les-cles-api)
* [JavaScript asynchrone](#heading-javascript-asynchrone)
* [Exemples concrets d'appels API](#heading-exemples-concrets-dappels-api)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une API ?

Avant de plonger dans les détails techniques de l'appel d'une API en JavaScript, commençons par les bases. Une API, ou Interface de Programmation d'Applications, est comme un pont qui permet à deux systèmes logiciels différents de communiquer entre eux. Elle définit un ensemble de règles et de protocoles pour demander et échanger des données.

Les APIs peuvent être utilisées pour récupérer des informations à partir de sources externes, envoyer des données à des services externes ou effectuer diverses autres actions. Elles sont largement utilisées dans le développement web pour accéder à des données provenant de divers services en ligne tels que les plateformes de médias sociaux, les données météorologiques, les informations financières, et plus encore.

## Comment choisir une API

La première étape pour appeler une API consiste à choisir celle qui répond à vos besoins. Il existe d'innombrables APIs disponibles, fournissant des données sur une grande variété de sujets. 

Certains des types populaires d'APIs incluent :

* APIs RESTful : Elles sont largement utilisées pour la récupération et la manipulation simples de données. Elles utilisent des méthodes HTTP standard comme GET, POST, PUT et DELETE.
* APIs tierces : De nombreux services en ligne offrent des APIs qui permettent d'accéder à leurs données, comme l'API Twitter pour les tweets ou l'API Google Maps pour les données de localisation.
* APIs météorologiques : Si vous avez besoin de données météorologiques, des APIs comme OpenWeatherMap ou WeatherAPI sont de bons choix.
* APIs financières : Pour récupérer des données financières comme les prix des actions, vous pouvez utiliser des APIs comme Alpha Vantage ou Yahoo Finance.

Pour ce guide, nous utiliserons une API RESTful fictive comme exemple pour garder les choses simples. Vous pouvez la remplacer par l'API de votre choix.

## Comment utiliser l'API Fetch pour les requêtes GET

Pour faire des requêtes API en JavaScript, vous pouvez utiliser l'API `fetch`, intégrée dans les navigateurs modernes. Il s'agit d'une API basée sur les promesses qui facilite l'envoi de requêtes HTTP et la gestion des réponses de manière asynchrone. 

Voici comment faire une requête GET en utilisant `fetch` :

```javascript
// Définir l'URL de l'API
const apiUrl = 'https://api.example.com/data';

// Faire une requête GET
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'est pas correcte');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans le code ci-dessus :

* Nous avons défini l'URL de l'API que nous voulons appeler.
* Nous avons utilisé la fonction `fetch` pour faire une requête GET à l'URL de l'API. La fonction `fetch` retourne une Promesse.
* La méthode `.then()` gère la réponse asynchrone du serveur.
* La propriété `response.ok` est vérifiée pour s'assurer que la réponse est valide.
* Nous analysons les données JSON en utilisant la méthode `response.json()`.
* Enfin, nous enregistrons les données dans la console ou gérons les erreurs qui peuvent survenir.

## Comment gérer les réponses

Lorsque vous faites un appel API, le serveur répond avec des données. La manière dont vous gérez ces données dépend des exigences de votre application. Dans l'exemple précédent, nous avons simplement enregistré les données dans la console. Cependant, vous pouvez traiter les données de diverses manières, comme les afficher sur une page web ou les stocker dans une base de données.

Voici un exemple modifié qui affiche les données de l'API dans un élément HTML :

```javascript
const apiUrl = 'https://api.example.com/data';
const outputElement = document.getElementById('output');

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'est pas correcte');
    }
    return response.json();
  })
  .then(data => {
    // Afficher les données dans un élément HTML
    outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, nous utilisons la variable `outputElement` pour sélectionner un élément HTML où nous voulons afficher les données. La propriété `textContent` est utilisée pour mettre à jour le contenu de cet élément avec les données JSON.

## Gestion des erreurs dans les appels API

La gestion des erreurs est une partie essentielle de la réalisation d'appels API en JavaScript. Les requêtes API peuvent échouer pour diverses raisons, telles que des problèmes de réseau, des problèmes de serveur ou des URL incorrectes. 

Dans nos exemples précédents, nous avons utilisé la gestion des erreurs basée sur les promesses de `fetch` pour attraper et gérer les erreurs.

En plus du bloc `catch`, vous pouvez également vérifier le code de statut HTTP en utilisant `response.status` pour déterminer la nature de l'erreur. Voici comment vous pouvez le faire :

```javascript
const apiUrl = 'https://api.example.com/data';

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error('Données non trouvées');
      } else if (response.status === 500) {
        throw new Error('Erreur de serveur');
      } else {
        throw new Error('La réponse du réseau n\'est pas correcte');
      }
    }
    return response.json();
  })
  .then(data => {
    outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, nous vérifions des codes de statut HTTP spécifiques (comme 404 et 500) et fournissons des messages d'erreur plus descriptifs. Vous pouvez personnaliser la gestion des erreurs pour répondre aux besoins de votre application.

## Comment faire des requêtes POST

Jusqu'à présent, nous nous sommes concentrés sur la réalisation de requêtes GET, qui sont utilisées pour récupérer des données à partir d'une API. Mais vous pouvez également avoir besoin d'envoyer des données à une API, ce que vous pouvez faire en utilisant des requêtes POST. 

Voici comment faire une requête POST simple en utilisant `fetch` :

```javascript
const apiUrl = 'https://api.example.com/data';
const data = {
  name: 'John Doe',
  email: 'johndoe@example.com',
};

const requestOptions = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
};

fetch(apiUrl, requestOptions)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'est pas correcte');
    }
    return response.json();
  })
  .then(data => {
    outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple :

* Nous avons défini l'URL de l'API et les données que nous voulons envoyer sous forme d'objet.
* Nous avons créé un objet `requestOptions` qui spécifie la méthode (POST), le type de contenu (application/json) et les données à envoyer au format JSON.
* Nous avons passé l'objet `requestOptions` à la fonction `fetch`.

Le reste du code reste similaire à nos exemples précédents, avec la gestion des erreurs et le traitement des données.

## Comment travailler avec les clés API

De nombreuses APIs nécessitent une authentification via des clés API pour s'assurer que seuls les utilisateurs autorisés peuvent accéder à leurs données. Lorsque vous travaillez avec des APIs qui nécessitent des clés API, vous devez inclure la clé dans vos requêtes.

Voici un exemple de la manière d'inclure une clé API dans une requête :

```javascript
const apiKey = 'votre_cle_api_ici';
const apiUrl = 'https://api.example.com/data';

const requestOptions = {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${apiKey}`,
  },
};

fetch(apiUrl, requestOptions)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'est pas correcte');
    }
    return response.json();
  })
  .then(data => {
    outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, nous définissons une variable `apiKey` et l'incluons dans les `headers` de l'objet `requestOptions` avec le préfixe "Bearer". Assurez-vous de remplacer `'votre_cle_api_ici'` par votre véritable clé API.

## JavaScript asynchrone

Les appels API sont généralement asynchrones, ce qui signifie qu'ils ne bloquent pas l'exécution de votre code en attendant une réponse. Cela est important car cela permet à votre application web de rester réactive même lorsqu'elle traite des requêtes réseau potentiellement lentes.

Pour gérer les opérations asynchrones, nous utilisons des promesses et la méthode `.then()` pour spécifier ce qui doit se passer lorsque l'opération est terminée. Cela permet au thread principal de votre application JavaScript de continuer à exécuter d'autres tâches tout en attendant la réponse de l'API.

Voici un récapitulatif du fonctionnement de JavaScript asynchrone :

Lorsque vous appelez `fetch`, cela initie une opération asynchrone et retourne une promesse immédiatement.

Vous utilisez la méthode `.then()` pour attacher des fonctions qui doivent s'exécuter lorsque la promesse se résout avec succès (avec une réponse) ou échoue (avec une erreur).

Tout code en dehors des blocs `.then()` peut continuer à s'exécuter pendant que l'appel API est en cours.

Ce comportement asynchrone aide à garantir que votre application reste réactive et ne se fige pas en attendant des données.

## Exemples concrets d'appels API

Maintenant que nous avons couvert les bases de la réalisation d'appels API en JavaScript, explorons quelques exemples concrets pour voir comment ces connaissances peuvent être appliquées en pratique.

### Exemple 1 : Récupération des données météorologiques

Dans cet exemple, nous allons utiliser l'API OpenWeatherMap pour récupérer des données météorologiques pour un lieu spécifique. Vous pouvez vous inscrire pour obtenir une clé API gratuite sur leur site web. 

Voici comment vous pouvez faire une requête GET pour récupérer les données météorologiques et les afficher sur une page web :

```javascript
const apiKey = 'votre_cle_openweathermap_api';
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=London&appid=${apiKey}`;

const outputElement = document.getElementById('weather-output');

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('La réponse du réseau n\'est pas correcte');
    }
    return response.json();
  })
  .then(data => {
    const temperature = data.main.temp;
    const description = data.weather[0].description;
    const location = data.name;
    outputElement.innerHTML = `<p>Température à ${location} : ${temperature}°C</p>
                               <p>Météo : ${description}</p>`;
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, nous faisons une requête GET à l'API OpenWeatherMap, passons la clé API comme paramètre dans l'URL et affichons la température et la description de la météo sur une page web.

### Exemple 2 : Envoi d'un formulaire à un serveur

Supposons que vous avez un simple formulaire de contact sur votre site web et que vous souhaitez envoyer les données du formulaire à un serveur pour traitement. Voici comment vous pouvez faire une requête POST pour envoyer les données du formulaire à un serveur :

HTML :

```html
<form id="contact-form">
  <input type="text" name="name" placeholder="Nom">
  <input type="email" name="email" placeholder="Email">
  <textarea name="message" placeholder="Message"></textarea>
  <button type="submit">Envoyer</button>
</form>
<div id="response-message"></div>

```

JavaScript :

```javascript
const apiUrl = 'https://api.example.com/submit';

const contactForm = document.getElementById('contact-form');
const responseMessage = document.getElementById('response-message');

contactForm.addEventListener('submit', function (event) {
  event.preventDefault();

  const formData = new FormData(contactForm);

  const requestOptions = {
    method: 'POST',
    body: formData,
  };

  fetch(apiUrl, requestOptions)
    .then(response => {
      if (!response.ok) {
        throw new Error('La réponse du réseau n\'est pas correcte');
      }
      return response.text();
    })
    .then(data => {
      responseMessage.textContent = data;
    })
    .catch(error => {
      console.error('Erreur :', error);
    });
});

```

Dans cet exemple, nous écoutons l'événement de soumission du formulaire, empêchons la soumission par défaut du formulaire et utilisons `FormData` pour sérialiser les données du formulaire. Nous faisons ensuite une requête POST au serveur, envoyons les données du formulaire et affichons la réponse du serveur.

## Conclusion

Appeler une API en JavaScript est une compétence précieuse pour les développeurs web, permettant d'accéder à une richesse de données et de services pour enrichir vos applications web. 

Dans ce guide complet, nous avons couvert les concepts et techniques essentiels, y compris la réalisation de requêtes GET et POST, la gestion des réponses et des erreurs, et le travail avec les clés API. Vous avez également vu deux exemples pratiques qui démontrent comment récupérer des données météorologiques et envoyer des données de formulaire à un serveur.

Alors que vous continuez à travailler avec des APIs dans vos projets, vous rencontrerez diverses APIs avec leurs exigences et documentations uniques. N'oubliez pas que les APIs peuvent avoir des limites de taux, des politiques d'utilisation et des restrictions, alors consultez toujours la documentation de l'API pour vous assurer de l'utiliser correctement et de manière responsable.

Avec les connaissances acquises grâce à ce guide, vous serez bien équipé pour interagir avec des APIs dans vos applications JavaScript, vous permettant de créer des expériences web dynamiques et riches en données. Bon codage !