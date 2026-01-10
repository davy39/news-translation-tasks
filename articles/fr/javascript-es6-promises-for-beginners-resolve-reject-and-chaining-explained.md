---
title: 'Tutoriel JavaScript Promise : Résoudre, Rejeter et Chaînage en JS et ES6'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T19:25:04.000Z'
originalURL: https://freecodecamp.org/news/javascript-es6-promises-for-beginners-resolve-reject-and-chaining-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a73740569d1a4ca25b0.jpg
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: 'Tutoriel JavaScript Promise : Résoudre, Rejeter et Chaînage en JS et ES6'
seo_desc: 'By Cem Eygi

  Promises are one of the ways we can deal with asynchronous operations in JavaScript.
  Many people struggle with understanding how Promises work, so in this post I will
  try to explain them as simply as I can.

  Promises are a broad topic so I...'
---

Par Cem Eygi

Les Promesses sont l'une des façons dont nous pouvons gérer les opérations asynchrones en JavaScript. Beaucoup de gens ont du mal à comprendre comment fonctionnent les Promesses, alors dans cet article, je vais essayer de les expliquer aussi simplement que possible.

Les Promesses sont un sujet vaste, donc je ne peux pas entrer dans tous les détails dans cet article. Mais vous trouverez une introduction générale à ce que sont les Promesses, des explications sur des termes comme résoudre, rejeter et chaînage, ainsi qu'un exemple de code pour créer et utiliser des Promesses.

**Prérequis :** Pour mieux comprendre cet article, consultez mon autre article sur les [Fonctions de rappel JavaScript](https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/).

## Qu'est-ce qu'une Promesse ?

Une promesse en JavaScript est similaire à une promesse dans la vie réelle. Lorsque nous faisons une promesse dans la vie réelle, c'est une garantie que nous allons faire quelque chose à l'avenir. Parce que les promesses ne peuvent être faites que pour l'avenir.

Une promesse a 2 résultats possibles : elle sera soit tenue lorsque le moment sera venu, soit elle ne le sera pas.

C'est également la même chose pour les promesses en JavaScript. Lorsque nous définissons une promesse en JavaScript, elle sera résolue lorsque le moment sera venu, ou elle sera rejetée.

### Promesses en JavaScript

Tout d'abord, une Promesse est un objet. Il existe 3 états de l'objet Promesse :

* **En attente :** État initial, avant que la Promesse ne réussisse ou n'échoue
* **Résolue :** Promesse complétée
* **Rejetée :** Promesse échouée

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ekran-Resmi-2020-06-06-12.21.27.png)
_**Représentation du processus des Promesses**_

Par exemple, lorsque nous demandons des données au serveur en utilisant une Promesse, elle sera en mode attente jusqu'à ce que nous recevions nos données.

Si nous parvenons à obtenir les informations du serveur, la Promesse sera résolue avec succès. Mais si nous n'obtenons pas les informations, alors la Promesse sera dans l'état rejeté.

De plus, s'il y a plusieurs requêtes, alors après que la première Promesse soit résolue (ou rejetée), un nouveau processus démarrera auquel nous pourrons l'attacher directement par une méthode appelée chaînage.

Si vous préférez, vous pouvez également regarder la version vidéo ci-dessous :

%[https://youtu.be/OXpZfyVXeI8]

### Quelle est la différence entre les Callbacks et les Promesses ?

La principale différence entre les Fonctions de rappel et les Promesses est que nous attachons un rappel à une Promesse plutôt que de le passer. Donc nous utilisons toujours des fonctions de rappel avec les Promesses, mais d'une manière différente (chaînage).

C'est l'un des plus grands avantages de l'utilisation des Promesses, mais pourquoi ?

### Qu'est-ce que le Chaînage ?

Les fonctions de rappel ont été utilisées seules pour les opérations asynchrones en JavaScript pendant de nombreuses années. Mais dans certains cas, l'utilisation des Promesses peut être une meilleure option.

S'il y a plusieurs opérations asynchrones à effectuer et si nous essayons d'utiliser les bons vieux Callbacks pour elles, nous nous retrouverons rapidement dans une situation appelée [Callback hell](http://callbackhell.com/) :

```javascript
firstRequest(function(response) {  
    secondRequest(response, function(nextResponse) {    
        thirdRequest(nextResponse, function(finalResponse) {     
            console.log('Final response: ' + finalResponse);    
        }, failureCallback);  
    }, failureCallback);
}, failureCallback);
```

Cependant, si nous gérons la même opération avec des Promesses, puisque nous pouvons attacher des Callbacks plutôt que de les passer, cette fois le même code ci-dessus semble beaucoup plus propre et plus facile à lire :

```javascript
firstRequest()
  .then(function(response) {
    return secondRequest(response);
}).then(function(nextResponse) {  
    return thirdRequest(nextResponse);
}).then(function(finalResponse) {  
    console.log('Final response: ' + finalResponse);
}).catch(failureCallback);
```

Le code juste au-dessus montre comment plusieurs rappels peuvent être enchaînés les uns après les autres. Le chaînage est l'une des meilleures fonctionnalités des Promesses.

### Création et Utilisation d'une Promesse Étape par Étape

Tout d'abord, nous utilisons un constructeur pour créer un objet Promesse :

```javascript
const myPromise = new Promise();
```

Il prend deux paramètres, un pour le succès (resolve) et un pour l'échec (reject) :

```javascript
const myPromise = new Promise((resolve, reject) => {  
    // condition
});
```

Enfin, il y aura une condition. Si la condition est remplie, la Promesse sera résolue, sinon elle sera rejetée :

```javascript
const myPromise = new Promise((resolve, reject) => {  
    let condition;  
    
    if(condition is met) {    
        resolve('Promise is resolved successfully.');  
    } else {    
        reject('Promise is rejected');  
    }
});
```

Nous avons donc créé notre première Promesse. Maintenant, utilisons-la.

### then( ) pour les Promesses résolues :

Si vous revisitez l'image au début de cet article, vous verrez qu'il y a 2 cas : un pour les promesses résolues et un pour les promesses rejetées. Si la Promesse est résolue (cas de succès), alors quelque chose se passera ensuite (cela dépend de ce que nous faisons avec la Promesse réussie).

```javascript
myPromise.then();
```

La méthode then( ) est appelée après que la Promesse soit résolue. Ensuite, nous pouvons décider quoi faire avec la Promesse résolue.

Par exemple, enregistrons le message dans la console que nous avons obtenu de la Promesse :

```javascript
myPromise.then((message) => {  
    console.log(message);
});
```

### catch( ) pour les Promesses rejetées :

Cependant, la méthode then( ) est uniquement pour les Promesses résolues. Que se passe-t-il si la Promesse échoue ? Alors, nous devons utiliser la méthode catch( ).

De même, nous attachons la méthode then( ). Nous pouvons également attacher directement la méthode catch( ) juste après then( ) :

```javascript
myPromise.then((message) => { 
    console.log(message);
}).catch((message) => { 
    console.log(message);
});
```

Ainsi, si la promesse est rejetée, elle passera à la méthode catch( ) et cette fois nous verrons un message différent sur la console.

## Conclusion

Voici comment nous créons une Promesse en JavaScript et l'utilisons pour les cas résolus et rejetés. Les Promesses sont un sujet plus large, et il y a beaucoup plus de choses à apprendre à leur sujet. Donc, comprendre comment elles fonctionnent prend du temps.

Cet article n'est qu'une introduction aux Promesses, et j'espère que vous l'avez trouvé utile pour vous faire une idée de ce que sont les Promesses JavaScript et comment les utiliser.

Si vous souhaitez en savoir plus sur le développement Web, n'hésitez pas à visiter ma [Chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber) pour plus d'informations.

Merci d'avoir lu !