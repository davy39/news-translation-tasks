---
title: JavaScript — des callbacks à async/await
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-31T01:12:12.000Z'
originalURL: https://freecodecamp.org/news/javascript-from-callbacks-to-async-await-1cc090ddad99
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_GgmGZJnFec994dvCDpbWQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: JavaScript — des callbacks à async/await
seo_desc: 'By Diogo Spínola

  JavaScript is synchronous. This means that it will execute your code block by order
  after hoisting. Before the code executes, var and function declarations are “hoisted”
  to the top of their scope.

  This is an example of a synchronous ...'
---

Par Diogo Spínola

JavaScript est synchrone. Cela signifie qu'il exécutera votre bloc de code dans l'ordre après le [hoisting](https://scotch.io/tutorials/understanding-hoisting-in-javascript). Avant l'exécution du code, les déclarations `var` et `function` sont « hissées » en haut de leur portée.

Voici un exemple de code synchrone :

```js
console.log('1')

console.log('2')

console.log('3')
```

Ce code affichera de manière fiable « 1 2 3 ».

Les requêtes asynchrones attendront qu'un minuteur se termine ou qu'une requête réponde tandis que le reste du code continue de s'exécuter. Ensuite, lorsqu'il est temps, un [callback](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) déclenchera ces requêtes asynchrones.

Voici un exemple de code asynchrone :

```js
console.log('1')

setTimeout(function afterTwoSeconds() {
  console.log('2')
}, 2000)

console.log('3')
```

Cela affichera en réalité « 1 3 2 », car le « 2 » est dans un `setTimeout` qui ne s'exécutera, dans cet exemple, qu'après deux secondes. Votre application n'attend pas que les deux secondes se terminent. Au lieu de cela, elle continue d'exécuter le reste du code et, lorsque le délai est écoulé, elle revient à afterTwoSeconds.

Vous pourriez demander « Pourquoi est-ce utile ? » ou « Comment faire pour que mon code asynchrone devienne synchrone ? ». Espérons que je puisse vous montrer les réponses.

### **« Le problème »**

Supposons que notre objectif est de rechercher un utilisateur GitHub et d'obtenir tous les dépôts de cet utilisateur. Le problème est que nous ne connaissons pas le nom exact de l'utilisateur. Nous devons donc lister tous les utilisateurs avec un nom similaire et leurs dépôts respectifs.

Pas besoin d'être super sophistiqué, quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/OHwdYj5jqLgcI0Sad-H3K0p0VUT14C0DmVV8)
_Tel style, wow ! C'est le « [f](http://"https://jsfiddle.net/fp9pk8pq/" rel="noopener" target="_blank" title="iddle"_)iddle »_

Dans ces exemples, le code de requête utilisera XHR ([XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)). Vous pouvez le remplacer par `$.ajax` de jQuery ou l'approche native plus récente appelée `fetch`. Les deux vous donneront l'approche par promesses dès le départ.

Il sera légèrement modifié en fonction de votre approche, mais pour commencer :

```js
// L'argument url peut être quelque chose comme 'https://api.github.com/users/daspinola/repos'

function request(url) {
  const xhr = new XMLHttpRequest();
  xhr.timeout = 2000;
  xhr.onreadystatechange = function(e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
       // Code ici pour la réponse du serveur en cas de succès
      } else {
       // Code ici pour la réponse du serveur en cas d'échec
      }
    }
  }
  xhr.ontimeout = function () {
    // Bon, cela a pris trop de temps, faites quelque chose ici pour gérer cela
  }
  xhr.open('get', url, true)
  xhr.send();
}
```

Rappelez-vous que dans ces exemples, la partie importante n'est pas le résultat final du code. Au lieu de cela, votre objectif devrait être de comprendre les différences des approches et comment vous pouvez les exploiter pour votre développement.

### **Callback**

Vous pouvez enregistrer une référence d'une fonction dans une variable lorsque vous utilisez JavaScript. Ensuite, vous pouvez les utiliser comme arguments d'une autre fonction pour les exécuter plus tard. C'est notre « callback ».

Un exemple serait :

```js
// Exécutez la fonction "doThis" avec une autre fonction comme paramètre, dans ce cas "andThenThis". doThis exécutera le code qu'elle a et, lorsqu'elle aura terminé, elle devrait avoir "andThenThis" qui s'exécute.

doThis(andThenThis)

// À l'intérieur de "doThis", elle est référencée comme "callback" qui est juste une variable qui contient la référence à cette fonction

function andThenThis() {
  console.log('and then this')
}

// Vous pouvez la nommer comme vous voulez, "callback" est une approche courante

function doThis(callback) {
  console.log('this first')
  
  // les '()' est lorsque vous dites à votre code d'exécuter la référence de la fonction, sinon il affichera simplement la référence
  
  callback()
}
```

Utiliser le `callback` pour résoudre notre problème nous permet de faire quelque chose comme ceci pour la fonction `request` que nous avons définie précédemment :

```js
function request(url, callback) {
  const xhr = new XMLHttpRequest();
  xhr.timeout = 2000;
  xhr.onreadystatechange = function(e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
       callback(null, xhr.response)
      } else {
       callback(xhr.status, null)
      }
    }
  }
  xhr.ontimeout = function () {
   console.log('Timeout')
  }
  xhr.open('get', url, true)
  xhr.send();
}
```

Notre fonction pour la requête acceptera maintenant un `callback` afin que, lorsqu'une `request` est faite, il sera appelé en cas d'erreur et en cas de succès.

```js
const userGet = `https://api.github.com/search/users?page=1&q=daspinola&type=Users`

request(userGet, function handleUsersList(error, users) {
  if (error) throw error
  const list = JSON.parse(users).items
  
  list.forEach(function(user) {
    request(user.repos_url, function handleReposList(err, repos) {
      if (err) throw err
      // Traitez la liste des dépôts ici
    })
  })
})
```

Décomposons cela :

* Nous faisons une requête pour obtenir les dépôts d'un utilisateur
* Après la fin de la requête, nous utilisons le callback `handleUsersList`
* S'il n'y a pas d'erreur, nous analysons notre réponse du serveur en un objet en utilisant `JSON.parse`
* Ensuite, nous itérons notre liste d'utilisateurs car elle peut en contenir plus d'un  
Pour chaque utilisateur, nous demandons leur liste de dépôts.  
Nous utiliserons l'URL qui est retournée par utilisateur dans notre première réponse  
Nous appelons `repos_url` comme l'URL pour nos prochaines requêtes ou à partir de la première réponse
* Lorsque la requête est terminée, le callback sera appelé   
Cela gérera soit son erreur, soit la réponse avec la liste des dépôts pour cet utilisateur

**Note** : Envoyer l'erreur en premier en tant que paramètre est une pratique courante, surtout lorsque vous utilisez Node.js.

Une approche plus « complète » et lisible consisterait à avoir une gestion des erreurs. Nous garderions le callback séparé de l'exécution de la requête.

Quelque chose comme ceci :

```js
try {
  request(userGet, handleUsersList)
} catch (e) {
  console.error('Request boom! ', e)
}

function handleUsersList(error, users) {
  if (error) throw error
  const list = JSON.parse(users).items
  
  list.forEach(function(user) {
    request(user.repos_url, handleReposList)
  })
}

function handleReposList(err, repos) {
  if (err) throw err
  
  // Traitez la liste des dépôts ici
  console.log('Mes très rares dépôts', repos)
}
```

Cela finit par avoir des problèmes comme des courses et des problèmes de gestion des erreurs. Les courses se produisent lorsque vous ne contrôlez pas quel utilisateur vous obtiendrez en premier. Nous demandons les informations pour tous, au cas où il y en aurait plus d'un. Nous ne prenons pas en compte un ordre. Par exemple, l'utilisateur 10 peut arriver en premier et l'utilisateur 2 en dernier. Nous avons une solution possible plus tard dans l'article.

Le principal problème avec les callbacks est que la maintenance et la lisibilité peuvent devenir un casse-tête. C'est déjà un peu le cas et le code ne fait presque rien. Cela est connu sous le nom de **callback hell** qui peut être évité avec notre prochaine approche.

![Image](https://cdn-media-1.freecodecamp.org/images/gnjFO34QsB-GSxf1kW-rES6NKbXikObOWHTG)
_Image prise [ici](https://medium.com/@sagish/node-with-benefits-using-coffeescript-in-your-stack-e9754bf58668" rel="noopener" target="_blank" title="). Callback hell à son meilleur._

### **Promesses**

Les promesses vous permettent de rendre votre code plus lisible. Un nouveau développeur peut venir à la base de code et voir un ordre clair d'exécution de votre code.

Pour créer une promesse, vous pouvez utiliser :

```js
const myPromise = new Promise(function(resolve, reject) {
  
  // code ici
  
  if (codeIsFine) {
    resolve('fine')
  } else {
    reject('error')
  }
  
})

myPromise
  .then(function whenOk(response) {
    console.log(response)
    return response
  })
  .catch(function notOk(err) {
    console.error(err)
  })
```

Décomposons cela :

* Une promesse est initialisée avec une `function` qui a des instructions `resolve` et `reject`
* Faites votre code asynchrone à l'intérieur de la fonction `Promise`  
`resolve` lorsque tout se passe comme souhaité  
Sinon `reject`
* Lorsqu'un `resolve` est trouvé, la méthode `.then` s'exécutera pour cette `Promise`  
Lorsqu'un `reject` est trouvé, le `.catch` sera déclenché

Points à garder à l'esprit :

* `resolve` et `reject` n'acceptent qu'un seul paramètre  
`resolve('yey', 'works')` n'enverra que 'yey' à la fonction de callback `.then`
* Si vous enchaînez plusieurs `.then`  
Ajoutez un `return` si vous voulez que la valeur du prochain `.then` ne soit pas `undefined`
* Lorsqu'un `reject` est attrapé avec `.catch` si vous avez un `.then` enchaîné à celui-ci  
Il exécutera toujours ce `.then`  
Vous pouvez voir le `.then` comme un « toujours exécute » et vous pouvez vérifier un exemple dans ce [commentaire](https://medium.com/@daspinola/you-are-completely-right-when-the-article-was-written-i-believe-my-thoughts-were-of-a-scenario-75a4c6944356)
* Avec un enchaînement sur `.then` si une erreur se produit sur le premier  
Il ignorera les `.then` suivants jusqu'à ce qu'il trouve un `.catch`
* Une promesse a trois états  
**en attente**
* En attente d'un `resolve` ou `reject`  
**résolue**   
**rejetée**
* Une fois qu'elle est dans un état `résolue` ou `rejetée`  
Elle ne peut plus être changée

**Note** : Vous pouvez créer des promesses sans la fonction au moment des déclarations. La manière dont je vous la montre n'est qu'une manière courante de le faire.

« Théorie, théorie, théorie... Je suis confus » pourriez-vous dire.

Essayons d'utiliser notre exemple de requête avec une promesse pour essayer de clarifier les choses :

```js
function request(url) {
  return new Promise(function (resolve, reject) {
    const xhr = new XMLHttpRequest();
    xhr.timeout = 2000;
    xhr.onreadystatechange = function(e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          resolve(xhr.response)
        } else {
          reject(xhr.status)
        }
      }
    }
    xhr.ontimeout = function () {
      reject('timeout')
    }
    xhr.open('get', url, true)
    xhr.send();
  })
}
```

Dans ce scénario, lorsque vous exécutez `request`, il retournera quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/NAgYZaSSRVgbc42aFAOEaTIYnA-2JweED-At)
_Une promesse en attente d'être résolue ou rejetée_

```js
const userGet = `https://api.github.com/search/users?page=1&q=daspinola&type=Users`

const myPromise = request(userGet)

console.log('sera en attente lorsqu'il sera enregistré', myPromise)

myPromise
  .then(function handleUsersList(users) {
    console.log('lorsqu'un resolve est trouvé, il vient ici avec la réponse, dans ce cas les utilisateurs ', users)
    
    const list = JSON.parse(users).items
    return Promise.all(list.map(function(user) {
      return request(user.repos_url)
    }))
  })
  .then(function handleReposList(repos) {
    console.log('Tous les dépôts des utilisateurs dans un tableau', repos)
  })
  .catch(function handleErrors(error) {
    console.log('lorsqu'un reject est exécuté, il viendra ici en ignorant l'instruction then ', error)
  })
```

C'est ainsi que nous résolvons les problèmes de course et certains des problèmes de gestion des erreurs. Le code est encore un peu compliqué. Mais c'est une façon de vous montrer que cette approche peut également créer des problèmes de lisibilité.

Une solution rapide serait de séparer les callbacks comme ceci :

```js
const userGet = `https://api.github.com/search/users?page=1&q=daspinola&type=Users`

const userRequest = request(userGet)

// Juste en lisant cette partie à voix haute, vous avez une bonne idée de ce que fait le code
userRequest
  .then(handleUsersList)
  .then(repoRequest)
  .then(handleReposList)
  .catch(handleErrors)
  
function handleUsersList(users) {
  return JSON.parse(users).items
}

function repoRequest(users) {
  return Promise.all(users.map(function(user) {
    return request(user.repos_url)
  }))
}

function handleReposList(repos) {
  console.log('Tous les dépôts des utilisateurs dans un tableau', repos)
}

function handleErrors(error) {
  console.error('Quelque chose s'est mal passé ', error)
}
```

En regardant ce que `userRequest` attend dans l'ordre avec le `.then`, vous pouvez avoir une idée de ce que nous attendons de ce bloc de code. Tout est plus ou moins séparé par responsabilité.

Cela ne fait qu'effleurer la surface de ce que sont les promesses. Pour avoir une excellente compréhension de leur fonctionnement, je ne peux que trop recommander cet [article](https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html).

### **Générateurs**

Une autre approche consiste à utiliser les générateurs. C'est un peu plus avancé, donc si vous débutez, n'hésitez pas à passer au sujet suivant.

Une utilisation des générateurs est qu'ils permettent d'avoir un code asynchrone qui ressemble à du code synchrone.

Ils sont représentés par un `*` dans une fonction et ressemblent à ceci :

```js
function* foo() {
  yield 1
  const args = yield 2
  console.log(args)
}
var fooIterator = foo()

console.log(fooIterator.next().value) // affichera 1
console.log(fooIterator.next().value) // affichera 2

fooIterator.next('aParam') // affichera le console.log à l'intérieur du générateur 'aParam'
```

Au lieu de retourner avec un `return`, les générateurs ont une instruction `yield`. Il arrête l'exécution de la fonction jusqu'à ce qu'un `.next` soit fait pour cette itération de fonction. C'est similaire à la promesse `.then` qui ne s'exécute que lorsque le resolved revient.

Notre fonction de requête ressemblerait à ceci :

```js
function request(url) {
  return function(callback) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          callback(null, xhr.response)
        } else {
          callback(xhr.status, null)
        }
      }
    }
    xhr.ontimeout = function () {
      console.log('timeout')
    }
    xhr.open('get', url, true)
    xhr.send()
  }
}
```

Nous voulons avoir l'`url` comme argument. Mais au lieu d'exécuter la requête immédiatement, nous la voulons seulement lorsqu'un callback est disponible pour gérer la réponse.

Notre `generator` serait quelque chose comme :

```js
function* list() {
  const userGet = `https://api.github.com/search/users?page=1&q=daspinola&type=Users`
 
  const users = yield request(userGet)
  
  yield
  
  for (let i = 0; i<=users.length; i++) {
    yield request(users[i].repos_url)
  }
}
```

Il fera :

* Attendre que la première `request` soit prête
* Retourner une référence de `function` attendant un `callback` pour la première `request`  
Notre fonction `request` accepte une `url`  
et retourne une `function` qui attend un `callback`
* Attendre qu'un `users` soit envoyé dans le prochain `.next`
* Itérer sur `users`
* Attendre un `.next` pour chacun des `users`
* Retourner leur fonction de callback respective

Donc une exécution de ceci serait :

```js
try {
  const iterator = list()
  iterator.next().value(function handleUsersList(err, users) {
    if (err) throw err
    const list = JSON.parse(users).items
    
    // envoyer la liste des utilisateurs pour l'itérateur
    iterator.next(list)
    
    list.forEach(function(user) {
      iterator.next().value(function userRepos(error, repos) {
        if (error) throw repos
        
        // Traitez chaque dépôt individuel de l'utilisateur ici
        console.log(user, JSON.parse(repos))
      })
    })
  })  
} catch (e) {
  console.error(e)
}
```

Nous pourrions séparer les fonctions de callback comme nous l'avons fait précédemment. Vous comprenez maintenant le principe, un point à retenir est que nous pouvons maintenant gérer chaque liste de dépôts d'utilisateurs individuellement.

J'ai des sentiments mitigés à propos des générateurs. D'un côté, je peux comprendre ce qui est attendu du code en regardant le générateur.

Mais son exécution finit par avoir des problèmes similaires à ceux de l'enfer des callbacks.

Comme pour [async/await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function), un compilateur est recommandé. Cela est dû au fait qu'il n'est pas supporté dans les anciennes versions de navigateurs.

De plus, ce n'est pas si courant dans mon expérience. Cela peut donc générer de la confusion dans les bases de code maintenues par divers développeurs.

Un excellent aperçu du fonctionnement des générateurs peut être trouvé dans cet [article](https://codeburst.io/generators-in-javascript-1a7f9f884439). Et voici une autre excellente [ressource](http://chrisbuttery.com/articles/synchronous-asynchronous-javascript-with-es6-generators/).

### **Async/Await**

Cette méthode semble être un mélange de générateurs avec des promesses. Vous devez simplement indiquer à votre code quelles fonctions doivent être `async`. Et quelle partie du code devra `await` pour que cette `promise` se termine.

```js
sumTwentyAfterTwoSeconds(10)
  .then(result => console.log('after 2 seconds', result))
  
async function sumTwentyAfterTwoSeconds(value) {
  const remainder = afterTwoSeconds(20)
  return value + await remainder
}

function afterTwoSeconds(value) {
  return new Promise(resolve => {
    setTimeout(() => { resolve(value) }, 2000);
  });
}
```

Dans ce scénario :

* Nous avons `sumTwentyAfterTwoSeconds` comme étant une fonction asynchrone
* Nous disons à notre code d'attendre le `resolve` ou `reject` pour notre fonction de promesse `afterTwoSeconds`
* Il ne se terminera dans le `.then` que lorsque les opérations `await` seront terminées  
Dans ce cas, il n'y en a qu'une seule

En appliquant cela à notre `request`, nous la laissons comme une `promise` comme vu précédemment :

```js
function request(url) {
  return new Promise(function(resolve, reject) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          resolve(xhr.response)
        } else {
          reject(xhr.status)
        }
      }
    }
    xhr.ontimeout = function () {
      reject('timeout')
    }
    xhr.open('get', url, true)
    xhr.send()
  })
}
```

Nous créons notre fonction `async` avec les awaits nécessaires comme suit :

```js
async function list() {
  const userGet = `https://api.github.com/search/users?page=1&q=daspinola&type=Users`
  
  const users = await request(userGet)
  const usersList = JSON.parse(users).items
  
  usersList.forEach(async function (user) {
    const repos = await request(user.repos_url)
    
    handleRepoList(user, repos)
  })
}

function handleRepoList(user, repos) {
  const userRepos = JSON.parse(repos)
  
  // Traitez chaque dépôt individuel de l'utilisateur ici
  
  console.log(user, userRepos)
}
```

Ainsi, nous avons maintenant une fonction `list` asynchrone qui gérera les requêtes. Une autre fonction asynchrone est nécessaire dans le `forEach` afin que nous ayons la liste des `repos` pour chaque utilisateur à manipuler.

Nous l'appelons comme suit :

```js
list()
  .catch(e => console.error(e))
```

Cela et l'approche par promesses sont mes préférées, car le code est facile à lire et à modifier. Vous pouvez lire plus en profondeur sur async/await [ici](https://davidwalsh.name/async-await).

Un inconvénient de l'utilisation de async/await est qu'il n'est pas supporté dans le front-end par les anciens navigateurs ou dans le back-end. Vous devez utiliser Node 8.

Vous pouvez utiliser un compilateur comme [babel](https://babeljs.io/) pour aider à résoudre cela.

### **« Solution »**

Vous pouvez voir le [code final](https://codepen.io/daspinola/pen/EvOEKB) accomplissant notre objectif initial en utilisant async/await dans cet extrait.

Une bonne chose à faire est d'essayer vous-même dans les diverses formes référencées dans cet article.

### **Conclusion**

Selon le scénario, vous pourriez vous retrouver à utiliser :

* async/await
* callbacks
* mix

C'est à vous de voir ce qui correspond à vos besoins. Et ce qui vous permet de maintenir le code afin qu'il soit compréhensible pour les autres et pour vous-même dans le futur.

**Note** : Chacune des approches devient légèrement moins verbeuse lorsque vous utilisez les alternatives pour les requêtes comme `$.ajax` et `fetch`.

Faites-moi savoir ce que vous feriez différemment et les différentes façons que vous avez trouvées pour rendre chaque approche plus lisible.

C'est l'article 11 sur 30. Il fait partie d'un projet pour publier un article au moins une fois par semaine, des pensées oisives aux tutoriels. Laissez un commentaire, suivez-moi sur [Diogo Spínola](https://www.freecodecamp.org/news/javascript-from-callbacks-to-async-await-1cc090ddad99/undefined) et retournez ensuite à votre projet brillant !