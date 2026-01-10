---
title: Voici les méthodes les plus populaires pour effectuer une requête HTTP en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T10:53:50.000Z'
originalURL: https://freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gqHgCNubMncv7EwWNdArGQ.png
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Voici les méthodes les plus populaires pour effectuer une requête HTTP
  en JavaScript
seo_desc: 'By Said Hayani

  JavaScript has great modules and methods to make HTTP requests that can be used
  to send or receive data from a server side resource. In this article, we are going
  to look at a few popular ways to make HTTP requests in JavaScript.

  Ajax

  ...'
---

Par Said Hayani

JavaScript dispose de grands modules et méthodes pour effectuer des requêtes HTTP qui peuvent être utilisées pour envoyer ou recevoir des données d'une ressource côté serveur. Dans cet article, nous allons examiner quelques méthodes populaires pour effectuer des requêtes HTTP en JavaScript.

### Ajax

Ajax est la méthode traditionnelle pour effectuer une requête HTTP asynchrone. Les données peuvent être envoyées en utilisant la méthode HTTP POST et reçues en utilisant la méthode HTTP GET. Examinons et effectuons une requête `GET`. J'utiliserai JSONPlaceholder, une API REST en ligne gratuite pour les développeurs qui retourne des données aléatoires au format JSON.

Pour effectuer un appel HTTP en Ajax, vous devez initialiser une nouvelle méthode `XMLHttpRequest()`, spécifier l'URL de l'endpoint et la méthode HTTP (dans ce cas GET). Enfin, nous utilisons la méthode `open()` pour lier la méthode HTTP et l'URL de l'endpoint ensemble et appelons la méthode `send()` pour lancer la requête.

Nous enregistrons la réponse HTTP dans la console en utilisant la propriété `XMLHTTPRequest.onreadystatechange` qui contient le gestionnaire d'événements à appeler lorsque l'événement `readystatechanged` est déclenché.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zXtlRe4yRF3tZkFFvBhZeA.png)

```js
const Http = new XMLHttpRequest();
const url='https://jsonplaceholder.typicode.com/posts';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
```

Si vous consultez la console de votre navigateur, elle retournera un tableau de données au format JSON. Mais comment savoir si la requête est terminée ? En d'autres termes, comment pouvons-nous gérer les réponses avec Ajax ?

La propriété `onreadystatechange` a deux méthodes, `readyState` et `status` qui nous permettent de vérifier l'état de notre requête.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UfZf6qaZwNh5Mptft4WIZA.png)

Si `readyState` est égal à 4, cela signifie que la requête est terminée. La propriété `readyState` a 5 réponses. En savoir plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState).

En plus de faire directement un appel Ajax avec JavaScript, il existe d'autres méthodes plus puissantes pour faire un appel HTTP, comme `$.Ajax` qui est une méthode jQuery. Je vais en discuter maintenant.

### Méthodes jQuery

jQuery dispose de nombreuses méthodes pour gérer facilement les requêtes HTTP. Pour utiliser ces méthodes, vous devrez inclure la bibliothèque jQuery dans votre projet.

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

#### $.ajax

jQuery Ajax est l'une des méthodes les plus simples pour faire un appel HTTP.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vZ4BqVQfsvtpJm_RCsCE2Q.png)

La méthode $.ajax prend de nombreux paramètres, certains étant obligatoires et d'autres optionnels. Elle contient deux options de rappel `success` et `error` pour gérer la réponse reçue.

#### Méthode $.get

La méthode $.get est utilisée pour exécuter des requêtes GET. Elle prend deux paramètres : l'endpoint et une fonction de rappel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2koN5FJuT68WIyRKTihe5w.png)

#### $.post

La méthode `**$.post**` est une autre façon de poster des données sur le serveur. Elle prend trois paramètres : l'`url`, les données que vous souhaitez poster, et une fonction de rappel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ql6Yp1EJfD7850GXhErwyw.png)

#### $.getJSON

La méthode `$.getJSON` ne récupère que les données au format JSON. Elle prend deux paramètres : l'`url` et une fonction de rappel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hdcFdVHiBiRAo1YOi_Kt0Q.png)

jQuery dispose de toutes ces méthodes pour demander ou poster des données sur un serveur distant. Mais vous pouvez en fait mettre toutes ces méthodes en une seule : la méthode `$.ajax`, comme le montre l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*soPARjfQXMcZ5ccPK1QMmA.png)

### fetch

`fetch` est une nouvelle API web puissante qui vous permet de faire des requêtes asynchrones. En fait, `fetch` est l'une des meilleures méthodes et ma préférée pour faire une requête HTTP. Elle retourne une "Promise" qui est l'une des grandes fonctionnalités de ES6. Si vous n'êtes pas familier avec ES6, vous pouvez en lire plus dans [cet](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2) article. Les Promises nous permettent de gérer la requête asynchrone de manière plus intelligente. Examinons comment `fetch` fonctionne techniquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kz6k4VRs0RiVCasWR0pCow.png)

La fonction `fetch` prend un paramètre obligatoire : l'URL de l'`endpoint`. Elle a également d'autres paramètres optionnels comme dans l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QasrBgYZcU4BBFHqD2bBdg.png)

Comme vous pouvez le voir, `fetch` a de nombreux avantages pour effectuer des requêtes HTTP. Vous pouvez en apprendre plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). De plus, au sein de fetch, il existe d'autres modules et plugins qui nous permettent d'envoyer et de recevoir une requête vers et depuis le serveur, tels que [axios](https://github.com/axios/axios).

### Axios

Axios est une bibliothèque open source pour effectuer des requêtes HTTP et offre de nombreuses fonctionnalités. Examinons comment elle fonctionne.

#### Utilisation :

Tout d'abord, vous devrez inclure Axios. Il existe deux façons d'inclure Axios dans votre projet.

Tout d'abord, vous pouvez utiliser npm :

```bash
npm install axios --save
```

Ensuite, vous devrez l'importer

```js
import axios from 'axios'
```

Deuxièmement, vous pouvez inclure axios en utilisant un CDN.

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

#### Effectuer une requête avec axios :

Avec Axios, vous pouvez utiliser `GET` et `POST` pour récupérer et poster des données depuis le serveur.

#### GET :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4wmqiPsSN5mdgjJiRaKVZg.png)

`axios` prend un paramètre obligatoire et peut prendre un deuxième paramètre optionnel. Cela prend certaines données sous forme de simple requête.

#### POST :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ey6-vwsrm9RAhyoU15u6xQ.png)

[Axios](https://github.com/axios/axios) retourne une "Promise". Si vous êtes familier avec les promesses, vous savez probablement qu'une promesse peut exécuter plusieurs requêtes. Vous pouvez faire la même chose avec axios et exécuter plusieurs requêtes en même temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*40Pji4utVKPpC7-dePfC6Q.png)

Axios supporte de nombreuses autres méthodes et options. Vous pouvez les explorer [ici](https://github.com/axios/axios).

### Angular HttpClient

Angular dispose de son propre module HTTP qui fonctionne avec les applications Angular. Il utilise la bibliothèque [RxJS](http://reactivex.io/rxjs/) pour gérer les requêtes asynchrones et offre de nombreuses options pour effectuer les requêtes HTTP.

#### Effectuer un appel au serveur en utilisant Angular HttpClient

Pour effectuer une requête en utilisant Angular HttpClient, nous devons exécuter notre code à l'intérieur d'une application Angular. J'en ai donc créé une. Si vous n'êtes pas familier avec Angular, consultez mon article, [apprenez à créer votre première application Angular en 20 minutes](https://medium.freecodecamp.org/learn-how-to-create-your-first-angular-app-in-20-min-146201d9b5a7).

La première chose que nous devons faire est d'importer `HttpClientModule` dans `app.module.ts`

![Image](https://cdn-media-1.freecodecamp.org/images/1*iFuW5Fbp91VR5gwQ6XNMEQ.png)

Ensuite, nous devons créer un service pour gérer les requêtes. Vous pouvez facilement générer un service en utilisant [Angular CLI](https://cli.angular.io/).

```bash
ng g service  FetchdataService
```

Ensuite, nous devons importer HttpClient dans le service `fetchdataService.ts` et l'injecter à l'intérieur du constructeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kKwELAhSSpnN8DvIgdOfcQ.png)

Et dans `app.component.ts`, importer `fetchdataService`

```ts
//import
import { FetchdataService } from './fetchdata.service';
```

Enfin, appelez le service et exécutez-le.

`app.component.ts:`

![Image](https://cdn-media-1.freecodecamp.org/images/1*OrRe183Yaclt19n5ZQ194Q.png)

Vous pouvez consulter l'exemple de démonstration [sur Stackblitz](https://stackblitz.com/edit/angular-httpclinent).

### Conclusion

Nous venons de couvrir les méthodes les plus populaires pour effectuer une requête HTTP en JavaScript.

Merci pour votre temps. Si vous aimez cet article, applaudissez jusqu'à 50 fois, cliquez sur suivre et contactez-moi sur [Twitter](https://twitter.com/SaidHYN).



_Entre parenthèses, j'ai récemment travaillé avec un groupe solide d'ingénieurs logiciels pour l'une de mes applications mobiles. L'organisation était excellente, et le produit a été livré très rapidement, beaucoup plus vite que d'autres entreprises et freelances avec lesquels j'ai travaillé, et je pense que je peux honnêtement les recommander pour d'autres projets. Envoyez-moi un email si vous voulez entrer en contact —_ [_said@devsdata.com_](mailto:said@devsdata.com)_._