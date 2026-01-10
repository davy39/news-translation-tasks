---
title: Qu'est-ce que REST ? Définition de l'API REST pour les débutants
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-28T17:21:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/REST-API.png
tags:
- name: api
  slug: api
- name: http
  slug: http
- name: REST API
  slug: rest-api
seo_title: Qu'est-ce que REST ? Définition de l'API REST pour les débutants
seo_desc: "In this article, you will learn what the term REST means and how it lets\
  \ us communicate with the server efficiently.\nBefore we get into REST, let's learn\
  \ what an API is. I believe this will help you understand REST better. \nWhat is\
  \ an API?\nSince we'r..."
---

Dans cet article, vous apprendrez ce que signifie le terme REST et comment il nous permet de communiquer avec le serveur de manière efficace.

Avant d'aborder REST, apprenons ce qu'est une API. Je crois que cela vous aidera à mieux comprendre REST.

## **Qu'est-ce qu'une API ?**

Puisque nous parlons des API REST, notre définition d'une API ne dépassera pas le cadre du web.

API signifie Application Programming Interface. Une API établit une connexion entre des programmes afin qu'ils puissent transférer des données.

Un programme qui possède une API implique que certaines parties de ses données sont exposées pour que le client puisse les utiliser. Le client pourrait être le frontend du même programme ou un programme externe.

Afin d'obtenir ces données, une requête structurée doit être envoyée à l'API. Si la requête répond aux exigences souhaitées, une réponse contenant les données est renvoyée à l'endroit où la requête a été faite. Cette réponse se présente généralement sous la forme de données JSON ou XML.

Dans certains cas, vous aurez besoin d'une sorte d'autorisation pour accéder aux données d'une API externe.

Chaque API dispose d'une documentation qui vous indique quelles données sont disponibles et comment structurer votre requête afin d'obtenir une réponse valide.

### Exemple d'API

C'était confus ?

Utilisons un scénario de la vie réelle pour donner un exemple.

Imaginez visiter un nouveau restaurant. Vous êtes là pour commander de la nourriture, et comme vous n'y êtes jamais allé auparavant, vous ne savez pas exactement quel type de nourriture ils servent.

Le serveur s'approche alors de vous avec un menu afin que vous puissiez choisir ce que vous aimeriez manger. Après avoir fait votre choix, le serveur va à la cuisine et vous apporte votre nourriture.

Dans ce cas, le serveur est l'API qui vous connecte à la cuisine. La documentation de l'API est le menu. La requête est faite lorsque vous choisissez ce que vous aimeriez manger, et la réponse est la nourriture servie.

J'espère que cela vous aide à comprendre ce qu'est une API et comment elle fonctionne.

## Qu'est-ce que REST ?

REST signifie REpresentational State Transfer. C'est une norme qui guide la conception et le développement de processus qui nous permettent d'interagir avec des données stockées sur des serveurs web.

La définition ci-dessus peut ne pas sembler aussi complexe ou "professionnelle" que celles que vous trouvez sur Internet, mais l'objectif ici est que vous compreniez le but de base des API REST.

Une API qui respecte certaines ou toutes les [six contraintes directrices](https://en.wikipedia.org/wiki/Representational_state_transfer#:~:text=The%20REST%20architectural%20style%20defines,visibility%2C%20portability%2C%20and%20reliability.) de REST est considérée comme **RESTful.**

Nous sommes capables de communiquer avec les serveurs en utilisant le protocole HTTP. Avec ces protocoles, nous pouvons **Créer**, **Lire**, **Mettre à jour** et **Supprimer** des données – autrement connu sous le nom d'opérations **CRUD**.

Mais comment pouvons-nous effectuer ces opérations CRUD et communiquer avec les données sur le serveur ?

Nous pouvons le faire en envoyant des requêtes HTTP, et c'est là que REST intervient. REST simplifie le processus de communication en fournissant diverses méthodes/opérations/verbes HTTP que nous pouvons utiliser pour envoyer des requêtes au serveur.

## Comment communiquer avec un serveur en utilisant les API REST

Comme nous l'avons discuté dans la dernière section, les API REST facilitent le processus de communication avec le serveur en nous fournissant diverses méthodes de requête HTTP. Les méthodes les plus couramment utilisées sont :

* **GET** : La méthode get est utilisée pour **Lire** les données sur le serveur.
* **POST** : La méthode post est utilisée pour **Créer** des données.
* **PATCH/PUT** : La méthode patch est utilisée pour **Mettre à jour** des données.
* **DELETE** : La méthode delete est utilisée pour **Supprimer** des données.

Ces méthodes fournies par REST nous permettent d'effectuer facilement des opérations CRUD. C'est-à-dire :

Créer => POST.  
Lire => GET.  
Mettre à jour => PATCH/PUT.  
Supprimer => DELETE.

Ainsi, si nous devons faire une requête à un serveur, disons pour récupérer des données, nous allons faire une requête **GET** à un endpoint/ressource fourni par le serveur. L'endpoint est similaire à une URL.

Si la requête faite est valide, alors le serveur nous répondra avec les données que nous avons demandées. Il envoie également un code de statut où 200 est un succès et 400 est une erreur client.

Voici un exemple de requête faite à l'API JSONPlaceholder en utilisant JavaScript :

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
```

Lors de l'envoi d'une requête en utilisant l'API `fetch`, la méthode par défaut est la méthode GET – nous ne sommes donc pas obligés de la spécifier. Mais nous devons la spécifier lorsque nous faisons une requête en utilisant les autres méthodes.

Dans l'exemple de code ci-dessus, l'endpoint est [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) et les données spécifiques que nous demandons sont un élément de todo. Les données nous seront retournées au format JSON.

Si nous devions faire une requête POST, alors nous inclurions le type de méthode qui serait POST et un corps de requête qui contiendrait les données que nous créons pour envoyer au serveur.

La suppression nécessiterait que nous utilisions la méthode de requête correspondante ainsi que l'id de l'élément todo que nous voulons supprimer. Comme ceci :

```js
fetch('https://jsonplaceholder.typicode.com/posts/3', {
  method: 'DELETE',
});
```

La mise à jour nécessiterait à la fois l'id et le corps de la requête qui serait utilisé pour mettre à jour les données. Voici un exemple :

```js
fetch('https://jsonplaceholder.typicode.com/posts/5', {
  method: 'PATCH',
  body: JSON.stringify({
    title: 'new todo',
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est REST et comment il nous aide à communiquer avec le serveur de manière efficace.

Nous avons défini une API et donné un exemple pour aider à expliquer sa signification. Nous avons également découvert certaines des méthodes fournies par REST pour créer, lire, mettre à jour et supprimer des données stockées sur le serveur.

Merci d'avoir lu !