---
title: 'L''Aide-mémoire de l''API Fetch : Neuf des Requêtes API les Plus Courantes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-16T15:00:56.000Z'
originalURL: https://freecodecamp.org/news/fetch-api-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover-2.jpg
tags:
- name: api
  slug: api
- name: cheatsheet
  slug: cheatsheet
- name: JavaScript
  slug: javascript
seo_title: 'L''Aide-mémoire de l''API Fetch : Neuf des Requêtes API les Plus Courantes'
seo_desc: "By Ondrej Polesny\nAlmost every project needs to communicate with the outside\
  \ world. If youʼre working with JavaScript frameworks, you'll most likely use Fetch\
  \ API to do that. \nBut when you're working with the API, do you remember the syntax\
  \ by heart ..."
---

Par Ondrej Polesny

Presque tous les projets doivent communiquer avec le monde extérieur. Si vous travaillez avec des frameworks JavaScript, vous utiliserez très probablement l'API Fetch pour cela. 

Mais lorsque vous travaillez avec l'API, vous souvenez-vous de la syntaxe par cœur ou avez-vous besoin d'un peu d'aide ?

J'ai écrit de nombreux articles sur JavaScript et des sujets connexes pour me retrouver plus tard à les (re)visiter fréquemment afin de rafraîchir ma mémoire ou d'obtenir un exemple de code que je sais « être là quelque part ». 

Dans cet article, je vise à créer une autre ressource de ce type. Je vais lister les 9 requêtes API Fetch les plus courantes. 

Je suis sûr que vous les avez toutes utilisées à maintes reprises. Mais ne serait-ce pas bien d'éviter de fouiller dans d'anciens projets pour trouver la syntaxe de cette requête spécifique que vous avez utilisée il y a six mois ? :)

## Pourquoi Utiliser l'API Fetch ?

De nos jours, nous sommes gâtés par tous les services qui fournissent de beaux SDK qui abstraient les requêtes API réelles. Nous demandons simplement des données en utilisant des constructions typiques du langage et ne nous soucions pas de l'échange de données réel. 

Mais que faire s'il n'y a pas de SDK pour votre plateforme choisie ? Ou si vous construisez à la fois le serveur et le client ? Dans ces cas, vous devez gérer les requêtes vous-même. Voici comment vous pouvez le faire en utilisant l'API Fetch.

### Requête GET simple avec l'API Fetch

```js
fetch('{url}')
    .then(response => console.log(response));
```

### Requête POST simple avec l'API Fetch

```js
fetch('{url}', {
    method: 'post'
})
    .then(response => console.log(response));
```

### GET avec un jeton d'autorisation (Bearer) dans l'API Fetch

```js
fetch('{url}', {
    headers: {
        'Authorization': 'Basic {token}'
    }
})
    .then(response => console.log(response));
```

### GET avec des données de requête dans l'API Fetch

```js
fetch('{url}?var1=value1&var2=value2')
    .then(response => console.log(response));
```

### GET avec CORS dans l'API Fetch

```js
fetch('{url}', {
    mode: 'cors'
})
    .then(response => console.log(response));
```

### POST avec un jeton d'autorisation et des données de requête dans l'API Fetch

```js
fetch('{url}?var1=value1&var2=value2', {
    method: 'post',
    headers: {
        'Authorization': 'Bearer {token}'
    }
})
    .then(response => console.log(response));
```

### POST avec des données de formulaire dans l'API Fetch

```js
let formData = new FormData();
formData.append('field1', 'value1');
formData.append('field2', 'value2');

fetch('{url}', {
    method: 'post',
    body: formData
})
    .then(response => console.log(response));
```

### POST avec des données JSON dans l'API Fetch

```js
fetch('{url}', {
    method: 'post',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'field1': 'value1',
        'field2': 'value2'
    })
})
    .then(response => console.log(response));
```

### POST avec des données JSON et CORS dans l'API Fetch

```js
fetch('{url}', {
    method: 'post',
    mode: 'cors',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'field1': 'value1',
        'field2': 'value2'
    })
})
    .then(response => console.log(response));
```

## Comment Traiter les Résultats de la Requête de l'API Fetch

L'API Fetch retourne une _Promise_. C'est pourquoi j'utilise toujours `.then()` et une fonction de rappel pour traiter la réponse :

```js
fetch(...).then(response => {
    // traiter la réponse
}
```

Mais vous pouvez également attendre le résultat si vous êtes dans une fonction asynchrone :

```js
async function getData(){
    let data = await fetch(...);
    // traiter la réponse
}
```

Maintenant, voyons comment nous pouvons extraire les données de la réponse :

### Comment Vérifier le Code de Statut de la Réponse de l'API Fetch

Lors de l'envoi de requêtes POST, PATCH et PUT, nous sommes généralement intéressés par le code de statut de retour :

```js
fetch(...)
    .then(response => {
        if (response.status == 200){
            // tout est OK
        } else {
            console.log(response.statusText);
        }
    });
```

### Comment Obtenir une Valeur Simple de la Réponse de l'API Fetch

Certains points de terminaison d'API peuvent renvoyer un identifiant d'un nouvel enregistrement de base de données qui a été créé à l'aide de vos données :

```js
var userId;

fetch(...)
    .then(response => response.text())
    .then(id => {
        userId = id;
        console.log(userId)
    });
```

### Comment Convertir les Données JSON de la Réponse de l'API Fetch

Mais dans la plupart des cas, vous recevrez des données JSON dans le corps de la réponse :

```js
var dataObj;

fetch(...)
    .then(response => response.json())
    .then(data => {
        dataObj = data;
        console.log(dataObj)
    });
```

Gardez à l'esprit que vous ne pouvez accéder aux données qu'après que les deux Promesses soient résolues. Cela peut parfois être un peu confus, c'est pourquoi je préfère toujours utiliser des méthodes asynchrones et attendre les résultats :

```js
async function getData(){
    var dataObj;

    const response = await fetch(...);
    const data = await response.json();
    dataObj = data;
    console.log(dataObj);
}
```

## Conclusion

Ces exemples devraient vous couvrir dans la plupart des situations. 

Y a-t-il quelque chose que j'ai manqué, une requête que vous utilisez quotidiennement ? Ou autre chose avec lequel vous avez du mal ? Faites-le moi savoir sur [Twitter](https://twitter.com/ondrabus), et je le couvrirai dans un autre article :-)

Oh, et vous pouvez obtenir cet aide-mémoire sous une [forme imprimable également](https://ondrabus.com/fetch-api-cheatsheet).