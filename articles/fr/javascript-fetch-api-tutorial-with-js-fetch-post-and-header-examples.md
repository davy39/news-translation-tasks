---
title: Tutoriel sur l'API Fetch JavaScript avec des exemples de POST et d'en-têtes
  JS
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-21T20:26:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-fetch-api-tutorial-with-js-fetch-post-and-header-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wall-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
seo_title: Tutoriel sur l'API Fetch JavaScript avec des exemples de POST et d'en-têtes
  JS
seo_desc: 'If you are writing a web application, chances are you will have to work
  with external data. This can be your own database, third party APIs, and so on.

  When AJAX first appeared in 1999, it showed us a better way to build web applications.
  AJAX was a ...'
---

Si vous écrivez une application web, il est probable que vous devrez travailler avec des données externes. Cela peut être votre propre base de données, des API tierces, et ainsi de suite.

Lorsque [AJAX](https://en.wikipedia.org/wiki/Ajax_%28programming%29) est apparu pour la première fois en 1999, il nous a montré une meilleure façon de construire des applications web. AJAX a été une étape majeure dans le développement web et est le concept central derrière de nombreuses technologies modernes comme React.

Avant AJAX, vous deviez réafficher une page web entière même pour des mises à jour mineures. Mais AJAX nous a donné un moyen de récupérer du contenu depuis le backend et de mettre à jour des éléments sélectionnés de l'interface utilisateur. Cela a aidé les développeurs à améliorer l'expérience utilisateur et à construire des plateformes web plus grandes et plus complexes.

## Cours accéléré sur les API REST

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-9.png)

Nous sommes maintenant à l'ère des [API RESTful](https://restfulapi.net/). En termes simples, une API REST vous permet de pousser et de tirer des données depuis un datastore. Cela peut être votre base de données ou le serveur d'un tiers comme l'[API Twitter](https://developer.twitter.com/en/docs/twitter-api).

Il existe quelques types différents d'API REST. Examinons ceux que vous utiliserez dans la plupart des cas.

* **GET** – Obtenir des données depuis l'API. Par exemple, obtenir un utilisateur Twitter en fonction de son nom d'utilisateur.
* **POST** – Pousser des données vers l'API. Par exemple, créer un nouvel enregistrement d'utilisateur avec un nom, un âge et une adresse e-mail.
* **PUT** – Mettre à jour un enregistrement existant avec de nouvelles données. Par exemple, mettre à jour l'adresse e-mail d'un utilisateur.
* **DELETE** – Supprimer un enregistrement. Par exemple, supprimer un utilisateur de la base de données.

Il y a trois éléments dans chaque API REST. La requête, la réponse et les en-têtes.

**Requête** – Ce sont les données que vous envoyez à l'API, comme un identifiant de commande pour récupérer les détails de la commande.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2-6.png)
_Exemple de requête_

**Réponse** – Toute donnée que vous recevez du serveur après une requête réussie/échouée.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/3-5.png)
_Exemple de réponse_

**En-têtes** – Métadonnées supplémentaires transmises à l'API pour aider le serveur à comprendre le type de requête qu'il traite, par exemple "content-type".

![Image](https://www.freecodecamp.org/news/content/images/2020/08/4-2.png)
_Exemple d'en-têtes_

Le véritable avantage de l'utilisation d'une API REST est que vous pouvez construire une seule couche API pour plusieurs applications. 

Si vous avez une base de données que vous souhaitez gérer à l'aide d'une application web, mobile et de bureau, tout ce dont vous avez besoin est une seule couche API REST.

Maintenant que vous savez comment fonctionnent les API REST, voyons comment nous pouvons les consommer.

## XMLHttpRequest

Avant que [JSON](https://www.w3schools.com/js/js_json_intro.asp) ne prenne le dessus, le format principal d'échange de données était XML. XMLHttpRequest() est une fonction JavaScript qui a rendu possible la récupération de données depuis des API qui renvoyaient des données XML. 

XMLHttpRequest nous a donné l'option de récupérer des données XML depuis le backend sans recharger la page entière.

Cette fonction a évolué depuis ses débuts où elle ne supportait que XML. Maintenant, elle supporte d'autres formats de données comme JSON et plaintext.

Écrivons un simple appel XMLHttpRequest à l'API GitHub pour récupérer mon profil.

```javascript
// fonction pour gérer le succès
function success() {
    var data = JSON.parse(this.responseText); // analyser la chaîne en JSON
    console.log(data);
}

// fonction pour gérer l'erreur
function error(err) {
    console.log('La requête a échoué', err); // les détails de l'erreur seront dans l'objet "err"
}

var xhr = new XMLHttpRequest(); // invoquer une nouvelle instance de XMLHttpRequest
xhr.onload = success; // appeler la fonction de succès si la requête est réussie
xhr.onerror = error;  // appeler la fonction d'erreur si la requête a échoué
xhr.open('GET', 'https://api.github.com/users/manishmshiva'); // ouvrir une requête GET
xhr.send(); // envoyer la requête au serveur.
```

Le code ci-dessus enverra une requête GET à [https://api.github.com/users/manishmshiva](https://api.github.com/users/manishmshiva) pour récupérer mes informations GitHub en JSON. Si la réponse est réussie, elle imprimera le JSON suivant dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-2.png)

Si la requête a échoué, elle imprimera ce message d'erreur dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/8-1.png)

## API Fetch

L'API Fetch est une version plus simple et facile à utiliser de XMLHttpRequest pour consommer des ressources de manière asynchrone. Fetch vous permet de travailler avec des API REST avec des options supplémentaires comme la mise en cache des données, la lecture des réponses en streaming, et plus encore.

La principale différence est que Fetch fonctionne avec des promesses, et non des callbacks. Les développeurs JavaScript se sont éloignés des callbacks après l'introduction des promesses.

Pour une application complexe, vous pourriez facilement prendre l'habitude d'écrire des callbacks, ce qui conduit à l'enfer des callbacks ([callback hell](http://callbackhell.com/)). 

Avec les promesses, il est facile d'écrire et de gérer des requêtes asynchrones. Si vous êtes nouveau dans les promesses, [vous pouvez apprendre comment elles fonctionnent ici](https://javascript.info/promise-basics).

Voici à quoi ressemblerait la fonction que nous avons écrite précédemment si vous utilisiez fetch() au lieu de XMLHttpRequest :

```javascript
// Requête GET.
fetch('https://api.github.com/users/manishmshiva')
    // Gérer le succès
    .then(response => response.json())  // convertir en json
    .then(json => console.log(json))    // afficher les données dans la console
    .catch(err => console.log('La requête a échoué', err)); // Capturer les erreurs
```

Le premier paramètre de la fonction Fetch doit toujours être l'URL. Fetch prend ensuite un second objet JSON avec des options comme la méthode, les en-têtes, le corps de la requête, et ainsi de suite.

Il y a une différence importante entre l'objet de réponse dans XMLHttpRequest et Fetch. 

XMLHttpRequest retourne les données en tant que réponse tandis que l'objet de réponse de Fetch contient des informations sur l'objet de réponse lui-même. Cela inclut les en-têtes, le code de statut, etc. Nous appelons la fonction "res.json()" pour obtenir les données dont nous avons besoin depuis l'objet de réponse.

Une autre différence importante est que l'API Fetch ne lèvera pas d'erreur si la requête retourne un code de statut 400 ou 500. Elle sera toujours marquée comme une réponse réussie et transmise à la fonction 'then'.

Fetch ne lève une erreur que si la requête elle-même est interrompue. Pour gérer les réponses 400 et 500, vous pouvez écrire une logique personnalisée en utilisant 'response.status'. La propriété 'status' vous donnera le code de statut de la réponse retournée.

Très bien. Maintenant que vous comprenez comment fonctionne l'API Fetch, examinons quelques exemples supplémentaires comme le passage de données et le travail avec les en-têtes.

## Travailler avec les en-têtes

Vous pouvez passer des en-têtes en utilisant la propriété "headers". Vous pouvez également utiliser le [constructeur d'en-têtes](https://developer.mozilla.org/en-US/docs/Web/API/Headers) pour mieux structurer votre code. Mais passer un objet JSON à la propriété "headers" devrait fonctionner pour la plupart des cas.

```javascript
fetch('https://api.github.com/users/manishmshiva', {
  method: "GET",
  headers: {"Content-type": "application/json;charset=UTF-8"}
})
.then(response => response.json()) 
.then(json => console.log(json)); 
.catch(err => console.log(err));
```

## Passer des données à une requête POST

Pour une requête POST, vous pouvez utiliser la propriété "body" pour passer une chaîne JSON en entrée. Notez que le corps de la requête doit être une chaîne JSON tandis que les en-têtes doivent être un objet JSON.

```javascript
// données à envoyer à la requête POST
let _data = {
  title: "foo",
  body: "bar", 
  userId:1
}

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: "POST",
  body: JSON.stringify(_data),
  headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json()) 
.then(json => console.log(json));
.catch(err => console.log(err));
```

L'API Fetch est encore en développement actif. Nous pouvons nous attendre à de meilleures fonctionnalités dans un avenir proche. 

Cependant, la plupart des navigateurs supportent l'utilisation de Fetch dans vos applications. Le graphique ci-dessous devrait vous aider à déterminer quels navigateurs le supportent sur le web et les applications mobiles.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/6-2.png)

J'espère que cet article vous a aidé à comprendre comment travailler avec l'API Fetch. Assurez-vous d'essayer Fetch pour votre prochaine application web.

---

_Je rédige régulièrement des articles sur le Machine Learning, la Cybersécurité et DevOps. Vous pouvez vous inscrire à ma_ [_newsletter hebdomadaire_](https://www.manishmshiva.com/) _ici._