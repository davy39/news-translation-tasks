---
title: Comment utiliser les Promises en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T05:58:00.000Z'
originalURL: https://freecodecamp.org/news/promises-in-javascript-explained-277b98850de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pkunQjHG1AknVCa_-gXJVA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les Promises en JavaScript
seo_desc: 'By Prashant Ram

  Promises in JavaScript are a way to handle async calls. Before Promises were introduced
  in JavaScript ES6, async calls in JavaScript were handled using callback functions.
  Promises provide a cleaner, more elegant syntax and methodolog...'
---

Par Prashant Ram

Les Promises en JavaScript sont un moyen de gérer les appels asynchrones. Avant l'introduction des Promises en JavaScript [ES6](http://es6-features.org/#Constants), les appels asynchrones en JavaScript étaient gérés à l'aide de fonctions de rappel. Les Promises offrent une syntaxe et une méthodologie plus propres et plus élégantes pour gérer les appels asynchrones.

### Une Promise simple en JavaScript

Commençons par examiner la syntaxe et la structure d'une Promise simple en JavaScript. Vous pouvez voir le lien JSFiddle vers le code [ici](https://jsfiddle.net/prashantram/brzdg4g5/).

```
// Promise                   // Une structure Promise a 2 parties
```

```
//Première partie//créer la Promise et définir les conditions de succès/non succèslet promise1 = new Promise( (resolve, reject) => {let dataReceivedSuccessfully = false; 
```

```
if (dataReceivedSuccessfully)   resolve('Données disponibles !'); 
```

```
if (!dataReceivedSuccessfully)   reject('Données corrompues !'); 
```

```
}) 
```

```
//Deuxième partie //définir les actions pour lorsque les conditions sont remplies  promise1.then( (message) => {   console.log(message);    }).catch( (message) => {      console.log(message);})
```

Une Promise se compose de deux parties :

1. La première partie **crée la Promise** et **définit les conditions** de ce qui est considéré comme `réussi` et `non réussi`.
2. La deuxième partie **décrit ce qu'il faut faire** lorsque la condition `réussie` est remplie avec la définition de la fonction `resolve()`, et ce qu'il faut faire lorsque la condition `non réussie` est remplie avec la définition de la fonction `reject()`.

Ainsi, dans la première partie d'une Promise, nous créons la Promise, en utilisant l'objet `Promise()` intégré dans JavaScript ES6 :

```
let promise1 = new Promise( (resolve, reject) => { ... } );
```

Dans le corps de la fonction, nous définissons **quand** invoquer la fonction `resolve()` et la fonction `reject()` :

```
if (dataReceivedSuccessfully)   resolve('Données disponibles !');
```

```
if (!dataReceivedSuccessfully)   reject('Données corrompues !');
```

Dans la deuxième partie d'une Promise, nous **définissons** les fonctions `resolve()` et `reject()` réelles :

```
promise1.then(  (message) => {...faire ceci sur resolve()...})        .catch( (message) =>; {...faire ceci sur reject()....});
```

Ajoutons quelques commentaires détaillés en ligne au code ci-dessus pour illustrer ce point :

```
// PROMISE                   /* Chaque structure Promise() a 2 parties */
```

```
//Première Partie           /* Créer la Promise() et définir les conditions de ce qui est considéré comme réussi et non réussi.*/
```

```
let promise1 = new Promise( (resolve, reject) => {
```

```
let dataReceivedSuccessfully = false; /* Ceci est une variable arbitraire et ne fait PAS partie de la Promise */
```

```
if (dataReceivedSuccessfully) //Cette condition est considérée comme réussie, donc invoquer resolve()  resolve('Données disponibles !');
```

```
if (!dataReceivedSuccessfully) //Cette condition est considérée comme NON réussie, donc invoquer reject()  reject('Données corrompues !');
```

```
})
```

```
//Deuxième Partie/* Définir ce qu'il faut faire lorsque la condition réussie (c'est-à-dire resolve()) est / remplie, et ce qu'il faut faire lorsque la condition non réussie (c'est-à-dire        / reject()) est remplie. */
```

```
promise1.then( (message) => {   console.log(message);/* définir la fonction resolve(), / en d'autres termes, ce qu'il faut faire lorsque la promise est réussie. */
```

```
}).catch( (message) => {    console.log(message);/* définir la fonction reject(), / en d'autres termes, ce qu'il faut faire lorsque la promise n'est PAS réussie.*/
```

```
})
```

Allez-y et exécutez le code ci-dessus dans [JSFiddle](https://jsfiddle.net/prashantram/brzdg4g5/) en utilisant le navigateur Chrome et ouvrez l'Inspecteur (Console). Remarquez que la `Promise()` s'exécute, et elle affiche le message « Données corrompues ! » dans le console.log. Si vous mettez à jour le booléen `dataReceivedSuccessfully=true` et exécutez le code à nouveau, vous obtiendrez le message « Données reçues ! » dans le console.log.

Notez que ces messages sont passés par les fonctions `resolve()` et `reject()` et sont exécutés dans la section `.then()` et `.catch()` de la `Promise`.

Vous remarquerez également la chaîne de caractères `message` qui est passée par les fonctions `resolve()` et `reject()` — `resolve(Données reçues)` et `reject(Données corrompues)`.

Lorsque les fonctions `resolve()` et `reject()` sont invoquées, elles peuvent être invoquées avec des arguments — ceux-ci peuvent être des chaînes de caractères, des tableaux, des objets ou rien. Plus sur cela plus tard.

Dans notre exemple simple, l'argument passé par les fonctions `resolve()` et `reject()` est de type **chaîne de caractères**. Les arguments de la fonction `resolve()` dans la première partie de la `Promise` sont destinés à la fonction `.then()` dans la deuxième partie de la `Promise`. De la même manière, les arguments de la fonction `reject()` dans la première partie de la `Promise` sont destinés à la fonction `.catch()` dans la deuxième partie de la `Promise`.

Examinons également plus en détail la partie créant la `Promise`.

```
let promise1 = new Promise( (resolve, reject) => { ... } );
```

L'objet `Promise()` est un objet intégré dans JavaScript ES6. Lorsque cet objet est instancié en utilisant le mot-clé `new`, il prend une fonction comme argument. Cette seule fonction prend à son tour deux arguments, chacun d'eux étant également des fonctions — `resolve` et `reject`. Gardez donc à l'esprit que les arguments `(resolve, reject)` dans les Promises sont en fait des fonctions de rappel.

```
let promise1 = new Promise( (fn1, fn2) => { ...} );
```

Puisque `fn1` et `fn2` sont des fonctions de rappel. Cela signifie qu'elles peuvent être invoquées dans la Promise, ce qui est exactement ce qui se passe lorsque nous appelons `resolve(Données reçues !)` et `reject(Données corrompues !)`.

### Passer des objets et des tableaux dans `resolve()` et `reject()`

Dans l'exemple précédent, nous avons utilisé un simple message de chaîne de caractères comme argument pour les fonctions `resolve()` et `reject()`. Il est important de noter que les fonctions `resolve()` et `reject()` **prennent un seul argument**. Maintenant, que faites-vous si vous voulez passer plus d'une information, puisque vous êtes limité à n'utiliser qu'un seul argument ?

Les fonctions `resolve()` et `reject()` vous permettent de passer un seul argument, mais cet argument unique peut être de type chaîne de caractères, nombre, booléen, tableau ou objet.

La manière dont vous pouvez passer plus d'une information dans les fonctions `resolve()` et `reject()` est de **les passer sous forme d'objet ou de tableau**.

L'exemple suivant illustre comment vous pouvez passer plusieurs informations en utilisant l'argument unique des fonctions `resolve()` et `reject()`, en les passant comme partie d'un seul grand objet ou d'un tableau.

```
//Passer des tableaux et des objets comme arguments
```

```
let dataReceivedSuccessfully = true;
```

```
//définir la Promisepromise1 = new Promise( (resolve, reject) => {
```

```
//construire le tableau ou l'objet que vous voulez passlet some_array = [1, 2, 3, 4, 5];  let some_object = {color:'red', person:{ name: "mike", age: '35'} };
```

```
//définir dans quelles conditions invoquer resolve() et reject()  if (dataReceivedSuccessfully)     resolve(some_array);     //passer un tableau comme argument unique  else     reject(some_object);     //passer un objet comme argument unique});
```

```
//définir la fonction d'exécution pour resolve() et reject()  promise1.then( (message) => {     console.log(`${message}`); //si dataReceivedSuccessfully=true, console.log affiche 1,2,3,4,5
```

```
}).catch( (message) => {     console.log(`error`);     console.log(`${message.color}`);//si dataReceivedSuccessfully=false, console.log affiche "error" "red"
```

```
})
```

Ouvrez cet exemple dans [JSFiddle](https://jsfiddle.net/prashantram/dzwrbvp1/) et exécutez-le. Ouvrez l'élément Inspect dans le navigateur Chrome et allez dans la Console. Ici, vous verrez que les messages appropriés sont affichés en fonction du paramètre de passage.

Il est également possible de laisser les paramètres de passage **vides** dans les Promises.

### Plus d'une Promise

Maintenant que nous comprenons la syntaxe et la structure de base des Promises, augmentons le niveau en utilisant plus d'une Promise.

Lorsque plusieurs promises sont utilisées, elles peuvent être enchaînées ensemble — avec la fonction `.then()` de la **première** Promise retournant la **prochaine** Promise, et ainsi de suite.

Dans l'exemple suivant, nous créons plusieurs Promises. Cela pourrait être un cas typique où nous voulons gérer plusieurs appels asynchrones. Vous pouvez voir le lien JSFiddle vers le code [ici](https://jsfiddle.net/prashantram/5tgqtbkm/).

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 2");})
```

```
promise3 = new Promise((resolve, reject) => {  setTimeout( ()=>{ resolve("données reçues de 3");
```

```
 },2000);//Nous simulons un délai dans la réception des données en utilisant setTimout() 
```

```
})
```

```
promise1.then((message) => {     console.log(message);     return promise2; //retourner promise2 lorsque promise1 est résolue.}).then((message) => {     console.log(message);     return promise3; //retourner promise3 lorsque promise2 est résolue.}).then((message) => {     console.log(message); //résoudre promise3.})
```

Notez que dans l'exemple ci-dessus, les Promises se résolvent en séquence les unes après les autres.

La sortie `console.log` de ce qui précède est :

```
   données reçues de 1   données reçues de 2 (....il y aura un délai simulé de 2 secondes)   données reçues de 3
```

### Promises en action

Dans de nombreux cas, nous ne sommes pas intéressés par l'exécution séquentielle des Promises. Plutôt, nous sommes intéressés à savoir si toutes les Promises ont été exécutées avec succès ou non. Dans d'autres cas, nous pouvons être intéressés à savoir si une Promise a terminé son exécution.

Les cas réels pour cela peuvent être lorsque nous essayons de récupérer les mêmes données à partir de plusieurs CDN. Dans ce cas, nous pouvons être intéressés à résoudre la Promise dès que les données de l'un des CDN deviennent disponibles.

Ces deux cas peuvent être gérés dans les Promises en utilisant les méthodes `.all()` et `.race()`.

#### Promise.all() et Promise.race()

La méthode `.all()` évalue toutes les Promises et exécute la méthode `.then()` lorsque toutes les Promises dans son tableau `Promise` ont terminé.

La méthode `.race()`, en revanche, s'exécute dès qu'une Promise du tableau `Promise` a terminé son exécution. La méthode `.race()` n'attend pas les autres Promises et se résout dès qu'une des Promises est résolue.

L'exemple suivant montre la syntaxe et la sortie de chacune de ces conditions.

```
// exemple .all()
```

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 2");})
```

```
promise3 = new Promise((resolve, reject) => {    setTimeout(()=>{  resolve("données reçues de 3");  }, 2000);
```

```
})
```

```
Promise.all([promise1, promise2, promise3]).then( (message) => {  console.log(message);
```

```
})
```

Lorsque vous exécutez ce code, la Promise attend que toutes les Promises dans le tableau de promises soient complétées. Puisque `promise3` a un délai de 2 secondes, aucune sortie n'est affichée pendant 2 secondes.

Ce n'est qu'après les 2 secondes, une fois que toutes les Promises sont résolues, que la `console.log` affiche le `message`.

Dans ce cas, le `message` est un tableau qui contient les messages de toutes les trois promises :

```
0:données reçues de 1"
```

```
1:données reçues de 2"
```

```
2:données reçues de 3"
```

```
length:3
```

Le code suivant montre la syntaxe et la structure de la méthode `.race()` :

```
// exemple .race()
```

```
var requestComplete = true;
```

```
promise1 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 1");})
```

```
promise2 = new Promise((resolve, reject) => {  if (requestComplete)    resolve("données reçues de 2");})
```

```
promise3 = new Promise((resolve, reject) => {  setTimeout(()=>{resolve("données reçues de 3");}, 2000);})
```

```
Promise.race([promise1, promise2, promise3]).then( (message) => {  console.log(message);
```

```
})
```

Lorsque l'exemple `.race()` est exécuté, la `console.log` affiche immédiatement. Elle n'attend pas que `promise3` termine son exécution. Elle exécute la fonction `.then()` dès qu'une des Promises est résolue.

Dans ce cas, le `message` n'est pas un tableau mais contient comme argument les arguments de la première Promise résolue — il ne contient qu'une seule chaîne de caractères dans ce cas :

```
données reçues de 1
```

### Un exemple réel utilisant les Promises

D'accord, super ! Je pense que nous sommes maintenant prêts pour quelques implémentations réelles de Promises.

Nous allons utiliser les Promises pour récupérer de manière asynchrone des données à partir de deux sites web différents. Nous allons utiliser l'objet intégré `XMLHttpRequest()` pour cela et surveiller la méthode `request.onreadystatechange()` pour surveiller les réponses en utilisant `request.status` et `request.response`.

Le premier site auquel nous accédons est l'API NASA, et le deuxième site utilise l'API Github. J'ai simplement choisi ces API car elles étaient ouvertes.

Nous allons utiliser la méthode `Promise.race()` pour voir lequel des deux sites répond le plus rapidement. Vous pouvez voir le lien JSFiddle vers le code [ici](https://jsfiddle.net/prashantram/p776txjk/5/).

```
promise1 = new Promise((resolve, reject) => {
```

```
  let request = new XMLHttpRequest();  let url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo";
```

```
  request.open('GET', url);  request.send();
```

```
  console.log("NASA " + request.readyState);
```

```
  request.onreadystatechange = () => {    console.log("NASA " + request.readyState);
```

```
if (request.readyState === 4) {      //console.log(request.response);      console.log("Réponse de l'API NASA : " + request.status);      resolve("NASA gagne la course !");    }  }
```

```
})
```

```
promise2 = new Promise((resolve, reject) => {
```

```
  let request = new XMLHttpRequest();  let url = 'https://api.github.com/users/mralexgray/repos';
```

```
  request.open('GET', url);  request.send();
```

```
  console.log("GITHUB " + request.readyState);
```

```
  request.onreadystatechange = () => {    console.log("GITHUB " + request.readyState);
```

```
if (request.readyState === 4) {      //console.log(request.response);      console.log("Réponse de l'API GITHUB : " + request.status);      resolve("GITHUB gagne la course !");    }  }
```

```
})
```

```
Promise.race([promise1, promise2]).then((message) => {  console.log(message);})
```

Vous pouvez exécuter ce code sur JSFiddle plusieurs fois, et voir en moyenne quel site répond le plus rapidement. J'ai trouvé que le site GitHub était plus rapide en moyenne.

### Remarques de conclusion

Les Promises sont un excellent moyen de gérer les appels asynchrones en JavaScript. Lorsqu'elles sont utilisées correctement, elles vous permettent de gérer le code de manière élégante.

Bon codage !

[**_Suivez-moi sur Medium_**](https://medium.com/@prashantramnyc) **_pour les dernières mises à jour et articles !_**

**Autres articles :**   
[Comment créer une simple animation Sprite en JavaScript](https://medium.com/@prashantramnyc/how-to-build-a-simple-sprite-animation-in-javascript-b764644244aa)

[L'approche Microservices pour le développement d'applications mobiles](https://medium.com/@prashantramnyc/microservices-architecture-for-mobile-application-development-part-i-20b4f4089a24)