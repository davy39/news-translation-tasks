---
title: Fetch API – Comment faire une requête GET et POST en JavaScript
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-06-02T19:39:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-api-calls-with-fetch
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/Fetch-API.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Fetch API – Comment faire une requête GET et POST en JavaScript
seo_desc: 'Often times you might want your system to communicate with other web servers
  to get information.

  For example, let''s say a new user wants to sign up for an account on your website.
  And instead of having to manually fill out a form to send their inform...'
---

Souvent, vous pourriez vouloir que votre système communique avec d'autres serveurs web pour obtenir des informations.

Par exemple, imaginons qu'un nouvel utilisateur souhaite s'inscrire sur votre site web. Et au lieu de devoir remplir manuellement un formulaire pour envoyer ses informations à votre système, il veut utiliser ses informations déjà présentes sur un autre service ou une autre plateforme (c'est-à-dire, **l'authentification tierce**) pour s'inscrire.

Dans un tel cas, votre système doit communiquer avec le système du tiers pour obtenir les informations de cet utilisateur. Et cela se fait via une **API**.

> Une API, ou Interface de Programmation d'Application, est simplement un ensemble de règles qui guident la manière dont un logiciel ou un système communique avec un autre.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/IMG_20210530_115853.jpg align="left")

*Ma explication dessinée à la main d'une API*

Si votre application est une application monopage construite avec un langage de programmation asynchrone comme JavaScript, vous disposez d'un outil utile pour effectuer cette fonction : `fetch()`.

## Qu'est-ce que l'API Fetch ?

`fetch()` est un mécanisme qui vous permet de faire des appels AJAX (Asynchronous JavaScript and XML) simples avec JavaScript.

**Asynchrone** signifie que vous pouvez utiliser fetch pour faire un appel à une API externe sans interrompre l'exécution des autres instructions. Ainsi, les autres fonctions du site continueront à s'exécuter même lorsqu'un appel API n'a pas encore été résolu.

Lorsque l'API envoie une réponse (des données), les tâches asynchrones (fetch) reprennent. Si cela semble toujours difficile, vous pouvez lire mon introduction détaillée sur [le code asynchrone ici](https://ubahthebuilder.tech/introduction-to-asynchronous-programming-with-javascript).

Il est important de noter, cependant, que fetch ne fait pas partie de la spécification JavaScript, mais de la WWTAG. Par conséquent, vous ne pourrez pas l'utiliser dans un environnement Node.js (sauf si vous installez un module spécial).

## Comment utiliser `fetch()` en JavaScript

Lorsque nous parlons d'API, nous devons également parler des **endpoints**. Un endpoint est simplement une URL unique que vous appelez pour interagir avec un autre système.

Supposons que nous faisons une requête à une API externe pour obtenir des données (comme un article de blog). Pour cela, nous utiliserons une simple requête GET.

Il suffit d'appeler `fetch()` avec l'URL de l'endpoint comme argument :

```js
fetch('https://ubahthebuilder.tech/posts/1');
```

Le corps de la réponse pour cet endpoint contiendra des informations sur un article de blog :

```js
{
userId: 1,
id: 1,
title: 'Un article de Kingsley',
body: 'Excellent article sur fetch...',
};
```

En fin de compte, vous voudrez obtenir le corps de la réponse. Mais l'objet de réponse contient bien plus d'informations que le corps, y compris le code de statut, les en-têtes, et plus encore.

> Notez que l'API fetch retourne une promesse. Pour cette raison, vous devez imbriquer une méthode then() pour gérer la résolution. En savoir plus sur les promesses [ici](https://ubahthebuilder.tech/introduction-to-asynchronous-programming-with-javascript).

Les données retournées par l'API ne sont généralement pas dans un format utilisable. Vous devrez donc convertir les données dans un format que votre JavaScript peut utiliser. Heureusement, vous pouvez utiliser la méthode `json()` pour cela :

```js
fetch('https://ubahthebuilder.tech/posts/1')
.then(data => {
return data.json();
})
.then(post => {
console.log(post.title);
});
```

Comme vous pouvez le voir dans le code ci-dessus, vous pouvez imbriquer une méthode `then()` ultérieure pour analyser les données (j'ai extrait uniquement le titre dans notre cas).

Dans cet exemple, nous voulions simplement obtenir un article de blog depuis l'API. Mais que faire si nous voulions publier une histoire à la place ?

## Comment faire une requête POST

Une fois que vous allez au-delà des requêtes GET, vous devrez définir quelques options supplémentaires. Jusqu'à présent, vous n'avez fourni qu'un seul argument à `fetch()` — l'URL de l'endpoint.

Pour une requête POST, vous devrez passer un objet d'options de configuration comme deuxième argument. L'objet optionnel peut prendre de nombreux paramètres différents. Dans ce cas, incluez uniquement les informations les plus nécessaires.

Puisque vous envoyez une requête POST, vous devrez déclarer que vous utilisez la méthode POST.

Vous devrez également passer certaines données pour créer effectivement le nouvel article de blog. Puisque vous envoyez des données JSON, vous devrez définir un en-tête de *Content-Type* à *application/json*. Enfin, vous aurez besoin du corps, qui sera une seule chaîne de données JSON.

```js
const update = {
title: 'Un article de blog par Kingsley',
body: 'Excellent article sur l'API Fetch',
userId: 1,
};

const options = {
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
body: JSON.stringify(update),
};
```

Et ensuite, l'appel à l'API :

```js
fetch('https://jsonplaceholder.typicode.com/posts', options)
  .then(data => {
      if (!data.ok) {
        throw Error(data.status);
       }
       return data.json();
      }).then(update => {
      console.log(update);
      // {
      //
      title: 'Un article de blog par Kingsley',
      //
      body: 'Excellent article sur l'API Fetch',
      //
      userId: 1,
      //
      id: 101
      // };
      }).catch(e => {
      console.log(e);
      });
```

Si votre requête est réussie, vous obtiendrez un corps de réponse contenant l'objet de l'article de blog ainsi qu'un nouvel ID. La réponse variera en fonction de la configuration de l'API.

Enfin, vous devez noter que les endpoints peuvent changer avec le temps et que les API peuvent être restructurées. Il est donc conseillé de regrouper tous vos appels fetch pour un accès plus facile.

## Conclusion

Voici quelques points pour résumer cet article :

* Les systèmes informatiques comme les logiciels communiquent entre eux et partagent des informations via une couche appelée API.

* Une API contient l'ensemble des règles et protocoles guidant la manière dont deux systèmes ou plus interagissent. Par exemple, le système de Facebook peut interagir avec le système de Google pour obtenir des informations sur un utilisateur via une API.

* En JavaScript côté client, vous pouvez faire des appels API simples avec l'utilitaire `fetch()`.

* Pour faire une simple requête GET avec fetch, vous devez simplement passer l'URL de l'endpoint comme argument.

* Pour faire une requête POST, vous devrez passer certains autres paramètres, y compris un objet de configuration.

Si vous avez aimé mon article et souhaitez offrir votre soutien, veuillez visiter ma page [Buy Me A Coffee](https://buymeacoffee.com/ubahthebuilder).

Merci et à bientôt.