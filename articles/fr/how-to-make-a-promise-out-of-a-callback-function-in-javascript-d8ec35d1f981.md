---
title: Comment transformer une fonction de rappel (Callback) en Promise en JavaScript
date: '2018-07-24T22:06:26.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/how-to-make-a-promise-out-of-a-callback-function-in-javascript-d8ec35d1f981
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7EYmjkeLQs8QXSLr_6iTMg.jpeg
tags:
- name: backend
  slug: backend
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_desc: 'By Adham El Banhawy

  Back-end developers run into challenges all the time while building applications
  or testing code. As a developer who is fairly new and getting acquainted with those
  challenges, I have never run into a challenge or inconvenience mo...'
---


Par Adham El Banhawy

<!-- more -->

Les développeurs back-end font face à des défis en permanence lors de la création d'applications ou du test de code. En tant que développeur relativement nouveau et me familiarisant avec ces défis, je n'ai jamais rencontré de difficulté ou d'inconvénient plus fréquent — ou plus mémorable — que les **fonctions de rappel (callbacks).**

Je ne vais pas m'étendre trop profondément sur les détails des callbacks, leurs avantages et inconvénients, ou les alternatives comme les promises et async/await. Pour une explication plus vivante, vous pouvez consulter [cet article][1] qui les explique en détail.

### **L'enfer des callbacks (Callback Hell)**

Les callbacks sont une fonctionnalité utile de JavaScript qui lui permet d'effectuer des appels asynchrones. Ce sont des fonctions qui sont généralement passées en second paramètre à une autre fonction qui récupère des données ou effectue une opération d'E/S (I/O) prenant du temps.

Par exemple, essayez de faire un appel API en utilisant le module `request` ou de vous connecter à une base de données MongoDB. Mais que se passe-t-il si les deux appels dépendent l'un de l'autre ? Et si la donnée que vous récupérez est l'URL MongoDB dont vous avez besoin pour vous connecter ?

Vous devriez imbriquer ces appels l'un dans l'autre :

```
request.get(url, function(error, response, mongoUrl) {

  if(error) throw new Error("Error while fetching fetching data");

  MongoClient.connect(mongoUrl, function(error, client) {

    if(error) throw new Error("MongoDB connection error");

    console.log("Connected successfully to server");    
    const db = client.db("dbName");
    // Do some application logic
    client.close();

  });

});
```

D'accord... alors où est le problème ? Eh bien, d'une part, la lisibilité du code souffre de cette technique.

Cela peut sembler correct au début quand la base de code est petite. Mais cela ne passe pas bien à l'échelle, surtout si vous descendez de plusieurs niveaux dans l'imbrication des callbacks.

Vous finirez avec énormément de parenthèses et d'accolades fermantes qui vous perdront, vous et les autres développeurs, peu importe la qualité du formatage de votre code. Il existe un site web appelé [callbackhell][2] qui traite spécifiquement de ce problème.

J'entends certains d'entre vous, y compris mon moi passé naïf, me dire de l'envelopper dans une fonction `async` puis d'utiliser `await` sur la fonction de rappel. Cela ne fonctionne tout simplement pas.

S'il y a un bloc de code après la fonction qui utilise des callbacks, ce bloc de code s'exécutera et **n'attendra PAS** le callback.

Voici l'erreur que je commettais auparavant :

```
var request = require('request');

// FAUX

async function(){

  let joke;
  let url = "https://api.chucknorris.io/jokes/random"

  await request.get(url, function(error, response, data) {

    if(error) throw new Error("Error while fetching fetching data");

    let content = JSON.parse(data);
    joke = content.value;

  });

  console.log(joke); // undefined

};

// Faux

async function(){

  let joke;
  let url = "https://api.chucknorris.io/jokes/random"

  request.get(url, await function(error, response, data) {

    if(error) throw new Error("Error while fetching fetching data");

    let content = JSON.parse(data);
    joke = content.value;

  });

  console.log(joke); // undefined

};
```

Certains développeurs plus expérimentés pourraient dire : « Utilise simplement une bibliothèque différente qui utilise des promises pour faire la même chose, comme [axios][3], ou utilise simplement [fetch][4] ». Bien sûr, je peux le faire dans ce scénario, mais c'est juste fuir le problème.

De plus, ce n'est qu'un exemple. Parfois, vous pouvez être contraint d'utiliser une bibliothèque qui ne supporte pas les promises sans alternative possible. Comme l'utilisation de kits de développement logiciel (SDK) pour communiquer avec des plateformes comme Amazon Web Services (AWS), Twitter ou Facebook.

Parfois, même utiliser un callback pour effectuer un appel très simple avec une opération d'E/S ou CRUD rapide est acceptable, et aucune autre logique ne dépend de ses résultats. Mais vous pourriez être limité par l'environnement d'exécution, comme dans une [fonction Lambda][5] qui tuerait tous les processus une fois le thread principal terminé, quels que soient les appels asynchrones non achevés.

### Solution 1 (facile) : Utiliser le module « util » de Node

La solution est étonnamment simple. Même si vous n'êtes pas très à l'aise avec l'idée des promises en JavaScript, vous allez adorer la façon dont vous pouvez résoudre ce problème en les utilisant.

Comme l'ont souligné Erop et Robin dans les commentaires, la version 8 de Node.js et les suivantes permettent désormais de transformer des fonctions de rappel en promises en utilisant le module intégré **util**.

```
const request = require('request');

const util = require('util');

const url = "https://api.chucknorris.io/jokes/random";

// Use the util to promisify the request method

const getChuckNorrisFact = util.promisify(request);

// Use the new method to call the API in a modern then/catch pattern

getChuckNorrisFact(url).then(data => {

   let content = JSON.parse(data.body);

   console.log('Joke: ', content.value);

}).catch(err => console.log('error: ', err))
```

Le code ci-dessus résout proprement le problème en utilisant la méthode [**util.promisify**][6] disponible dans la bibliothèque standard de Node.js.

Tout ce que vous avez à faire est de passer la fonction de rappel comme argument à `util.promisify` et de la stocker dans une variable. Dans mon cas, c'est `getChuckNorrisFact`.  
Ensuite, vous utilisez cette variable comme une fonction que vous pouvez appeler comme une promise avec les méthodes **.then()** et **.catch()**.

### Solution 2 (plus complexe) : Transformer le callback en Promise

Parfois, l'utilisation des bibliothèques `request` et `util` n'est tout simplement pas possible, que ce soit à cause d'un environnement ou d'une base de code héritée (legacy), ou parce que vous effectuez les requêtes côté client dans le navigateur ; vous devez alors envelopper votre fonction de rappel dans une promise.

Prenons l'exemple de Chuck Norris ci-dessus et transformons-le en promise.

```
var request = require('request');
let url = "https://api.chucknorris.io/jokes/random";

// A function that returns a promise to resolve into the data //fetched from the API or an error
let getChuckNorrisFact = (url) => {
  return new Promise(
    (resolve, reject) => {
      request.get(url, function(error, response, data){
        if (error) reject(error);

let content = JSON.parse(data);
        let fact = content.value;
        resolve(fact);
      })
   }
 );
};

getChuckNorrisFact(url).then(
   fact => console.log(fact) // actually outputs a string
).catch(
   error => console.(error)
);
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZXNYPRkv4mC2cHoq-4PIdoAx0WK-DyuUybzA) _ça fonctionne comme par magie_

Dans le code ci-dessus, j'ai placé la fonction `request` basée sur un callback à l'intérieur d'un wrapper de Promise `Promise( (resolve, reject) => { //fonction callback})`. Ce wrapper nous permet d'appeler la fonction `getChuckNorrisFact` comme une promise avec les méthodes `.then()` et `.catch()`. Lorsque `getChuckNorrisFact` est appelée, elle exécute la requête vers l'API et **attend** soit une instruction `resolve()`, soit une instruction `reject()`. Dans la fonction de rappel, vous passez simplement les données récupérées aux méthodes `resolve` ou `reject`.

Une fois que les données (dans ce cas, un fait génial sur Chuck Norris) sont récupérées et transmises au résolveur, `getChuckNorrisFact` exécute la méthode `then()`. Cela retournera le résultat que vous pourrez **utiliser à l'intérieur d'une fonction dans le `then()`** pour réaliser votre logique souhaitée — dans ce cas, l'afficher dans la console.

Vous pouvez en apprendre davantage à ce sujet dans [la documentation MDN Web Docs.][7]

[1]: https://medium.com/codebuddies/getting-to-know-asynchronous-javascript-callbacks-promises-and-async-await-17e0673281ee
[2]: http://callbackhell.com/
[3]: https://www.npmjs.com/package/axios
[4]: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
[5]: https://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction-function.html
[6]: https://nodejs.org/docs/latest-v8.x/api/util.html#util_util_promisify_original
[7]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#Creating_a_Promise_around_an_old_callback_API