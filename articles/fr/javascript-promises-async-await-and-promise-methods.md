---
title: Comment utiliser les promesses JavaScript – Callbacks, Async/Await et les méthodes
  de promesse expliquées
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2023-08-15T16:03:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-promises-async-await-and-promise-methods
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/promises_async_methods.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment utiliser les promesses JavaScript – Callbacks, Async/Await et les
  méthodes de promesse expliquées
seo_desc: 'In this tutorial, you will learn everything you need to know about using
  promises and async/await in JavaScript.

  So let''s get started.

  If you''d like to learn along with a video version of this tutorial, you can also
  check out my YouTube playlist.

  Why...'
---

Dans ce tutoriel, vous apprendrez tout ce que vous devez savoir sur l'utilisation des promesses et de async/await en JavaScript.

Alors, commençons.

Si vous souhaitez apprendre avec une version vidéo de ce tutoriel, vous pouvez également consulter ma [playlist YouTube](https://www.youtube.com/watch?v=4jaiXP6vU2w&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=14).

## Pourquoi utiliser les promesses en JavaScript ?

ES6 a introduit les promesses comme une implémentation native. Avant ES6, nous utilisions des callbacks pour gérer les opérations asynchrones.

Comprenons ce que sont les callbacks et quel problème lié aux callbacks est résolu par les promesses.

Supposons que nous avons une liste de posts et leurs commentaires respectifs, comme ceci :

```js
const posts = [
  { post_id: 1, post_title: 'Premier Post' },
  { post_id: 2, post_title: 'Deuxième Post' },
  { post_id: 3, post_title: 'Troisième Post' },
];

const comments = [
  { post_id: 2, comment: 'Super !'},
  { post_id: 2, comment: 'Super Post !'},
  { post_id: 3, comment: 'Post Génial !'},
];
```

Maintenant, nous allons écrire une fonction pour obtenir un post en passant l'identifiant du post. Si le post est trouvé, nous récupérerons les commentaires liés à ce post.

```js
const getPost = (id, callback) => {
 const post = posts.find( post => post.post_id === id);
 if(post) {
   callback(null, post);
 } else {
   callback("Aucun post trouvé", undefined);
 }
};

const getComments = (post_id, callback) => {
 const result = comments.filter( comment => comment.post_id === post_id);
 if(result) {
   callback(null, result);
 } else {
   callback("Aucun commentaire trouvé", undefined);
 }
}
```

Dans les fonctions `getPost` et `getComments` ci-dessus, si une erreur se produit, nous la passerons comme premier argument. Mais si nous obtenons le résultat, nous appellerons la fonction de callback et passerons le résultat comme deuxième argument.

Si vous êtes familier avec Node.js, vous saurez que c'est un modèle très courant utilisé dans chaque fonction de callback Node.js.

Maintenant, utilisons ces fonctions :

```js
getPost(2, (error, post) => {
    if(error) {
     return console.log(error);
    }
    console.log('Post:', post);
    getComments(post.post_id, (error, comments) => {
        if(error) {
          return console.log(error);
        }
        console.log('Commentaires:', comments);
    });
});
```

Après avoir exécuté le code ci-dessus, vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/posts.jpg)
_Résultat de l'appel des fonctions getPost et getComments_

Voici une [démo CodePen](https://codepen.io/myogeshchavan97/pen/PoweVgR?editors=0011#0).

Comme vous pouvez le voir, nous avons la fonction `getComments` imbriquée dans le callback de `getPost`.

Maintenant, imaginez si nous voulions également trouver les likes de ces commentaires. Cela devrait également être imbriqué dans le callback de `getComments`, créant plus d'imbrications. Cela finira par rendre le code difficile à comprendre.

Cette imbrication des callbacks est connue sous le nom d'**enfer des callbacks**.

Vous pouvez voir que la condition de gestion des erreurs est également répétée dans le code, ce qui crée du code dupliqué – ce n'est pas bon.

Pour résoudre ce problème et permettre des opérations asynchrones, les promesses ont été introduites.

## Que sont les promesses en JavaScript ?

Les promesses sont l'une des parties les plus importantes de JavaScript – mais elles peuvent être déroutantes et difficiles à comprendre. De nombreux nouveaux développeurs, ainsi que des développeurs expérimentés, ont du mal à les comprendre pleinement.

Alors, qu'est-ce qu'une promesse ? Une promesse représente une opération asynchrone dont le résultat viendra dans le futur.

Avant ES6, il n'y avait aucun moyen d'attendre quelque chose pour effectuer une opération. Par exemple, lorsque nous voulions faire un appel d'API, il n'y avait aucun moyen d'attendre que les résultats reviennent.

Pour cela, nous utilisions des bibliothèques externes comme JQuery ou Ajax qui avaient leur propre implémentation des promesses. Mais il n'y avait pas d'implémentation JavaScript des promesses.

Mais ensuite, les promesses ont été ajoutées dans ES6 comme une implémentation native. Et maintenant, en utilisant les promesses dans ES6, nous pouvons faire un appel d'API nous-mêmes et attendre qu'il soit terminé pour effectuer une opération.

## Comment créer une promesse

Pour créer une promesse, nous devons utiliser la fonction constructeur `Promise` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 
});
```

Le constructeur `Promise` prend une fonction comme argument et cette fonction reçoit en interne `resolve` et `reject` comme paramètres.

Les paramètres `resolve` et `reject` sont en fait des fonctions que nous pouvons appeler en fonction du résultat de l'opération asynchrone.

Une `Promise` peut passer par trois états :

* En attente
* Remplie
* Rejetée

Lorsque nous créons une promesse, elle est dans un état d'attente. Lorsque nous appelons la fonction `resolve`, elle passe dans un état rempli, et si nous appelons `reject`, elle passera dans l'état rejeté.

Pour simuler l'opération longue ou asynchrone, nous utiliserons la fonction `setTimeout`.

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

```

Ici, nous avons créé une promesse qui se résoudra à la somme de `4` et `5` après un délai de 2000ms (2 secondes).

Pour obtenir le résultat de l'exécution réussie de la promesse, nous devons enregistrer un gestionnaire de callback en utilisant `.then` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

promise.then(function(result) {
 console.log(result); // 9
});

```

Ainsi, chaque fois que nous appelons `resolve`, la promesse retournera la valeur passée à la fonction `resolve` que nous pouvons collecter en utilisant le gestionnaire `.then`.

Si l'opération n'est pas réussie, alors nous appelons la fonction `reject` comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Erreur lors du calcul de la somme.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
});

```

Ici, si la `sum` n'est pas un nombre, alors nous appelons la fonction `reject` avec le message d'erreur. Sinon, nous appelons la fonction `resolve`.

Si vous exécutez le code ci-dessus, vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promises_fcc.png)
_Résultat du rejet de la promesse sans gestionnaire catch_

Comme vous pouvez le voir, nous obtenons un message d'erreur non capturée avec le message que nous avons spécifié car l'appel de la fonction `reject` lance une erreur. Mais nous n'avons pas ajouté de gestionnaire d'erreur pour capturer cette erreur.

Pour capturer l'erreur, nous devons enregistrer un autre callback en utilisant `.catch` comme ceci :

```js
promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

Vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/error_catch.png)
_Résultat du rejet de la promesse avec gestionnaire catch_

Comme vous pouvez le voir, nous avons ajouté le gestionnaire `.catch`, donc nous n'obtenons aucune erreur non capturée – nous enregistrons simplement l'erreur dans la console.

Cela évite également d'arrêter votre application de manière abrupte.

Il est donc toujours recommandé d'ajouter le gestionnaire `.catch` à chaque promesse pour que votre application ne s'arrête pas à cause de l'erreur.

### Quand utiliser `resolve` et `reject`

Prenons un exemple d'appel d'API.

Si vous faites un appel d'API et que l'appel d'API est réussi, alors vous appelez la fonction `resolve` en passant le résultat de l'API comme argument.

Et si l'API n'est pas réussie, alors vous appelez la fonction `reject` en passant un message comme argument.

Ainsi, pour indiquer que l'opération est réussie, nous appelons la fonction `resolve` et pour indiquer une opération non réussie, nous appelons la fonction `reject`.

## Qu'est-ce que le chaînage de promesses et pourquoi est-il utile ?

Le chaînage de promesses est une technique utilisée pour gérer les opérations asynchrones de manière plus organisée et lisible.

Dans le chaînage de promesses, nous pouvons attacher plusieurs gestionnaires `.then` dans lesquels le résultat du gestionnaire `.then` précédent est automatiquement passé au gestionnaire `.then` suivant.

L'utilisation du chaînage de promesses aide à éviter le problème de l'enfer des callbacks que nous avons vu précédemment.

Le chaînage de promesses permet également d'écrire du code asynchrone de manière plus linéaire et séquentielle, ce qui est plus facile à lire et à comprendre.

De plus, lors de l'utilisation du chaînage de promesses, nous pouvons attacher un seul gestionnaire `.catch` à la fin de tous les gestionnaires `.then`. Si l'une des promesses intermédiaires échoue, le dernier gestionnaire `.catch` sera automatiquement exécuté.

Ainsi, nous n'avons pas besoin d'ajouter plusieurs gestionnaires `.catch`. Cela élimine les vérifications d'erreurs multiples comme nous l'avons fait dans l'exemple de l'enfer des callbacks précédemment.

## Comment fonctionne le chaînage de promesses

Nous pouvons ajouter plusieurs gestionnaires `.then` à une seule promesse comme ceci :

```js
promise.then(function(result) {
 console.log('premier gestionnaire .then');
 return result;
}).then(function(result) {
 console.log('deuxième gestionnaire .then');
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

Lorsque nous avons plusieurs gestionnaires `.then` ajoutés, la valeur de retour du gestionnaire `.then` précédent est automatiquement passée au gestionnaire `.then` suivant.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_chaining.png)
_Résultat du chaînage de promesses_

Comme vous pouvez le voir, l'addition de `4 + 5` résout une promesse et nous obtenons cette somme dans le premier gestionnaire `.then`. Là, nous imprimons une instruction de journalisation et retournons cette somme au gestionnaire `.then` suivant.

Et à l'intérieur du gestionnaire `.then` suivant, nous ajoutons une instruction de journalisation et ensuite nous imprimons le résultat que nous avons obtenu du gestionnaire `.then` précédent.

Cette façon d'ajouter plusieurs gestionnaires `.then` est connue sous le nom de chaînage de promesses.

## Comment retarder l'exécution d'une promesse en JavaScript

Souvent, nous ne voulons pas que la promesse s'exécute immédiatement. Plutôt, nous voulons qu'elle soit retardée jusqu'à ce qu'une opération soit terminée.

Pour y parvenir, nous pouvons envelopper la promesse dans une fonction et retourner cette promesse depuis cette fonction comme ceci :

```js
function createPromise() {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = 4 + 5;
   if(isNaN(sum)) {
     reject('Erreur lors du calcul de la somme.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

```

De cette manière, nous pouvons utiliser les paramètres de la fonction à l'intérieur de la promesse, rendant la fonction vraiment dynamique.

```js
function createPromise(a, b) {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = a + b;
   if(isNaN(sum)) {
     reject('Erreur lors du calcul de la somme.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

createPromise(1,8)
 .then(function(output) {
  console.log(output); // 9
});

// OU

createPromise(10,24)
 .then(function(output) {
  console.log(output); // 34
});
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/general_function.png)
_Résultat du retard de l'exécution de la promesse_

**Note :** Lorsque nous créons une promesse, elle sera soit résolue soit rejetée mais pas les deux en même temps. Donc nous ne pouvons pas ajouter deux appels de fonction `resolve` ou `reject` dans la même promesse.

De plus, nous pouvons passer une seule valeur à la fonction `resolve` ou `reject`.

Si vous voulez passer plusieurs valeurs à une fonction `resolve`, passez-les sous forme d'objet comme ceci :

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve({
   a: 4,
   b: 5,
   sum
  });
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/object_resolve.png)
_Passer un objet à la fonction resolve pour retourner plusieurs valeurs_

## Comment utiliser les fonctions fléchées en JavaScript

Dans tous les exemples de code ci-dessus, nous avons utilisé la syntaxe de fonction ES5 régulière lors de la création de promesses.

Mais il est courant d'utiliser la syntaxe des fonctions fléchées au lieu de la syntaxe des fonctions ES5.

Alors, comprenons d'abord ce qu'est une fonction fléchée et comment l'utiliser.

### Que sont les fonctions fléchées ?

Avant ES6, il y avait deux principales façons de déclarer des fonctions.

1. Syntaxe de déclaration de fonction :

```js
function add(a, b) {
 return a + b;
}
```

2. Syntaxe d'expression de fonction :

```js
const add = function(a, b) {
 return a + b;
};
```

**La** principale différence visible **entre la** fonction **régulière et la fonction fléchée est la syntaxe d'écriture de la fonction.**

En utilisant la syntaxe des fonctions fléchées, nous pouvons écrire la fonction d'addition ci-dessus comme ceci :

```js
const add = (a, b) => {
 return a + b;
};
```

Vous ne verrez peut-être pas beaucoup de différence ici, à part la flèche. Mais si nous avons une seule ligne de code dans le corps de la fonction, nous pouvons simplifier la fonction fléchée ci-dessus comme ceci :

```js
const add = (a, b) => a + b;
```

Ici, nous retournons implicitement le résultat de `a + b`, donc il n'y a pas besoin du mot-clé `return` s'il y a une seule instruction.

Ainsi, l'utilisation des fonctions fléchées rendra votre code beaucoup plus court.

Si vous voulez apprendre d'autres fonctionnalités des fonctions fléchées, vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=tI87o_kDKN4&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=4).

En utilisant une fonction fléchée, nous pouvons écrire le code précédent comme montré ci-dessous :

```js
const promise = new Promise((resolve, reject) => {
 setTimeout(() => {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Erreur lors du calcul de la somme.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then((result) => {
 console.log(result);
});

```

Vous pouvez utiliser la syntaxe ES5 ou ES6 selon vos préférences et besoins.

## Comment utiliser Async/Await en JavaScript

Dans cette section, nous explorerons tout ce que vous devez savoir sur async/await.

Async/await offre aux développeurs une meilleure façon d'utiliser les promesses.

Pour utiliser async/await, vous devez créer une fonction et ajouter le mot-clé `async` avant le nom de la fonction en utilisant la syntaxe de déclaration de fonction ES5 comme ceci :

```js
async function someFunction() {
  // corps de la fonction
}
```

ou en utilisant la syntaxe d'expression de fonction comme ceci :

```js
const someFunction = async function () {
  // corps de la fonction
};
```

ou en utilisant une fonction fléchée comme ceci :

```js
const someFunction = async () => {
  // corps de la fonction
};
```

Rappelez-vous toujours que, lorsque vous ajoutez le mot-clé async à la fonction, elle retourne toujours une promesse.

Jetez un coup d'œil au code ci-dessous :

```js
const sayHello = async function () {
  return 'Hello';
};

sayHello();
```

Que pensez-vous que le résultat du code ci-dessus sera ?

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_1.png)
_Résultat de l'appel de la fonction marquée comme async_

Le résultat est une promesse remplie avec la chaîne `Hello`.

Ainsi, le code ci-dessous :

```js
const sayHello = async function () {
  return 'Hello';
};
```

est le même que ceci :

```js
const sayHello = function() {
 return new Promise((resolve, reject) => {
  resolve('Hello');
 });
}
```

qui est le même que ceci :

```js
const sayHello = function () {
  return Promise.resolve('Hello');
};
```

`Promise.resolve('Hello')` est simplement une façon plus courte de créer une promesse qui se résout en la chaîne `Hello`.

Ainsi, pour obtenir la chaîne réelle `Hello`, nous devons ajouter le gestionnaire `.then` comme ceci :

```js
sayHello().then(function (result) {
  console.log(result); // Hello
});
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_hello.png)
_Obtenir le résultat de la fonction async en utilisant le gestionnaire .then_

Maintenant, où utilisons-nous le mot-clé `await` ?

Il est utilisé à l'intérieur de la fonction qui est déclarée comme `async`. Ainsi, le mot-clé `await` ne doit être utilisé qu'à l'intérieur de la fonction `async`.

Vous obtiendrez une erreur si vous essayez de l'utiliser dans des fonctions non-async.

Supposons que nous avons une promesse qui retourne le produit de deux nombres comme ceci :

```js
function getProduct(a, b) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve(a * b);
    }, 1000);
  });
}
```

et nous l'utilisons comme ceci :

```js
getProduct(2, 4)
  .then(function (result) {
    getProduct(result, 2)
      .then(function (finalResult) {
        console.log('final_result', finalResult);
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
```

Dans le code ci-dessus, nous obtenons d'abord le produit de `2` et `4`. Ensuite, nous utilisons ce résultat pour le multiplier par `2` à nouveau, et enfin nous imprimons le produit.

Si vous exécutez le code ci-dessus, vous verrez le résultat final comme 16 qui est 2 * 4 = 8 et 8 * 2 = 16.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_product.png)
_Résultat de l'imbrication des gestionnaires de callback .then_

Le code ci-dessus de `.then` et `.catch` semble assez compliqué et difficile à comprendre au premier coup d'œil.

Ainsi, en utilisant async/await, nous pouvons simplifier le code ci-dessus comme ceci :

```js
const printResult = async () => {
  try {
    const result = await getProduct(2, 4); // ligne 1
    const finalResult = await getProduct(result, 2); // ligne 2
    console.log('final_result', finalResult); // ligne 3
  } catch (error) {
    console.log(error);
  }
};

printResult();
```

Cela semble beaucoup plus propre et facile à comprendre.

Ici, pour utiliser le mot-clé `await`, nous déclarons une fonction avec le mot-clé `async`. Ensuite, pour obtenir le résultat de chaque promesse, nous ajoutons le mot-clé `await` devant.

Notez également que nous avons ajouté try/catch à l'intérieur de la fonction. Vous devez toujours ajouter un bloc try autour du code qui utilise `await` afin que le bloc catch soit exécuté si la promesse est rejetée.

Il y a une chose très importante à retenir : le code async/await ci-dessus fonctionnera exactement de la même manière que lorsque nous utilisons `.then` – donc la ligne `await` suivante (ligne 2) ne sera pas exécutée tant que l'appel `await` précédent (ligne 1) n'est pas réussi.

Par conséquent, comme la fonction `getProduct` prend 1 seconde pour s'exécuter en raison de l'appel setTimeout, la ligne 2 devra attendre 1 seconde avant d'exécuter à nouveau la fonction `getProduct`.

Mais il y a une exception à ce comportement, que vous pouvez consulter dans [cet article](https://levelup.gitconnected.com/common-gotcha-with-promises-693a993568c2?source=friends_link&sk=32d92e34511f72cbcc399cded49348c8).

De plus, s'il y a une erreur lors de l'exécution de la ligne 1 (en raison d'une erreur survenue dans la fonction `getProduct`), le code suivant la ligne 1 ne sera pas exécuté. Au lieu de cela, le bloc catch sera exécuté.

Maintenant, si vous comparez le code du chaînage de promesses et de async/await, vous verrez la différence.

```js
// code utilisant async/await

const printResult = async () => {
  try {
    const product = await getProduct(2, 4); // ligne 1
    const finalResult = await getProduct(product, 2); // ligne 2
    console.log('final_result', finalResult); // ligne 3
  } catch (error) {
    console.log(error);
  }
};

printResult();
```

```js
// code utilisant .then et .catch

getProduct(2, 4)
  .then(function (result) {
    getProduct(result, 2)
      .then(function (finalResult) {
        console.log('final_result', finalResult);
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
```

Comme vous pouvez le voir, le code utilisant async/await est beaucoup plus propre et facile à comprendre par rapport au chaînage de promesses.

À mesure que l'imbrication devient plus profonde, le code utilisant le chaînage de promesses devient plus compliqué. Ainsi, async/await fournit simplement un moyen d'écrire le même code mais avec une meilleure clarté.

L'utilisation de async/await réduit également le besoin d'ajouter plusieurs gestionnaires `.catch` pour gérer les erreurs.

Nous pouvons éviter l'imbrication dans le chaînage de promesses ci-dessus en écrivant le code précédent comme ceci :

```js
getProduct(2, 4)
  .then(function (result) {
    return getProduct(result, 2);
  })
  .then(function (finalResult) {
    console.log('final_result', finalResult);
  })
  .catch(function (error) {
    console.log(error);
  });
```

Ici, à partir du premier gestionnaire `.then`, nous retournons le résultat de `getProduct(result, 2)`.

Tout ce qui est retourné par le gestionnaire `.then` précédent sera passé au gestionnaire `.then` suivant.

Comme la fonction `getProduct` retourne une promesse, nous pouvons y attacher `.then` à nouveau et éviter le besoin d'un gestionnaire `.catch` imbriqué.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/avoid_nested_handlers.png)
_utilisation du chaînage de promesses_

Mais la syntaxe async/await semble toujours plus propre et plus facile à comprendre que la syntaxe de chaînage de promesses.

## Méthodes de promesse

Dans cette section, nous explorerons les différentes méthodes fournies par l'API Promise.

Toutes ces méthodes sont utiles lorsque vous souhaitez exécuter plusieurs tâches asynchrones en même temps lorsque ces tâches ne dépendent pas les unes des autres (ce qui permet de gagner beaucoup de temps).

Car si vous exécutez chaque tâche l'une après l'autre, alors vous devez attendre que la tâche précédente se termine avant de pouvoir commencer la tâche suivante.

Et si les tâches ne sont pas liées les unes aux autres, il n'y a aucun intérêt à attendre que la tâche précédente se termine avant d'exécuter la tâche suivante.

### La méthode `Promise.all`

Cette méthode est utilisée pour exécuter plusieurs tâches asynchrones simultanément sans avoir à attendre qu'une autre tâche se termine.

Supposons que nous avons trois promesses et qu'elles sont toutes résolues avec succès :

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));
```

Maintenant, utilisons la méthode `Promise.all`.

`Promise.all` a besoin d'un tableau de promesses comme argument.

```js
Promise.all([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result); // resolved ["promise1 success", "promise2 success", "promise3 success"]
  })
  .catch((error) => {
    console.log('rejected', error);
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_all.png)

Comme toutes les promesses sont résolues, `result` sera un tableau contenant les résultats des promesses résolues.

Maintenant, que se passe-t-il si l'une des promesses est rejetée ?

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => reject('promise2 failure'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.all([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result);
  })
  .catch((error) => {
    console.log('rejected', error); // rejected promise2 failure
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_all_rejected.png)

Dans le code ci-dessus, promise2 est rejetée donc le gestionnaire catch sera exécuté, et dans le cas de `Promise.all` :

* Si l'une des promesses est rejetée, l'`error` contiendra le message d'erreur de la promesse échouée (comme dans notre cas ci-dessus)
* Si plusieurs promesses sont rejetées, l'`error` sera le message d'erreur de la première promesse échouée.

Note : Même si la promesse intermédiaire est rejetée, toutes les promesses suivantes ne seront pas arrêtées. Elles seront toutes exécutées – mais seule la valeur de la première promesse rejetée sera disponible dans le paramètre d'erreur du bloc catch.

### La méthode `Promise.race`

Considérons à nouveau les trois promesses résolues :

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.race([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result); // resolved promise1 success
  })
  .catch((error) => {
    console.log('rejected', error);
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_race_success.png)

Comme vous pouvez le voir ici, dès que la première promesse est résolue, la méthode `Promise.race` retournera le résultat de cette promesse résolue.

Maintenant, regardez le code ci-dessous :

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.race([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result);
  })
  .catch((error) => {
    console.log('rejected', error); // rejected promise1 failure
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_race_failed.png)

Comme vous pouvez le voir ici, la première promesse elle-même est rejetée donc le gestionnaire `.catch` sera exécuté.

Ainsi, lorsque nous utilisons la méthode `Promise.race`, elle attendra jusqu'à ce que la première promesse soit résolue ou rejetée et ensuite :

* Si la première promesse de la chaîne de promesses est résolue, le gestionnaire `.then` sera exécuté et le résultat sera le résultat de la première promesse résolue.
* Si la première promesse de la chaîne de promesses est rejetée, le gestionnaire `.catch` sera exécuté et le résultat sera le résultat de la première promesse échouée.
* Si plusieurs promesses sont rejetées, le gestionnaire `.catch` sera exécuté et le résultat sera le résultat de la première promesse échouée.

### La méthode `Promise.allSettled`

Cette méthode est utile lorsque vous souhaitez connaître le résultat de chaque tâche même si elles sont rejetées.

Car dans `Promise.all` et `Promise.race`, nous obtenons uniquement le résultat de la première promesse rejetée et il n'y a aucun moyen d'obtenir le résultat des autres promesses réussies ou échouées.

Ainsi, en utilisant `Promise.allSettled`, nous pouvons obtenir le résultat de toutes les promesses, même si elles ont échoué.

Jetez un coup d'œil au code ci-dessous :

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
resolved [
  {
    "status": "fulfilled",
    "value": "promise1 success"
  },
  {
    "status": "fulfilled",
    "value": "promise2 success"
  },
  {
    "status": "fulfilled",
    "value": "promise3 success"
  }
]
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_success.png)

Comme vous pouvez le voir, la méthode `Promise.allSettled` attend jusqu'à ce que toutes les promesses soient résolues ou rejetées et le `result` contiendra le résultat de chaque promesse.

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
resolved [
  {
    "status": "rejected",
    "reason": "promise1 failure"
  },
  {
    "status": "fulfilled",
    "value": "promise2 success"
  },
  {
    "status": "fulfilled",
    "value": "promise3 success"
  }
]
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_failure.png)

Dans le cas ci-dessus, même si la première promesse est rejetée, nous obtenons le résultat de toutes les promesses à l'intérieur du gestionnaire `.then`.

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => reject('promise2 failure'));
const promise3 = new Promise((resolve, reject) => reject('promise3 failure'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
 resolved [
  {
    "status": "rejected",
    "reason": "promise1 failure"
  },
  {
    "status": "rejected",
    "reason": "promise2 failure"
  },
  {
    "status": "rejected",
    "reason": "promise3 failure"
  }
] 
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_multiple_failure.png)

Ici, même si toutes les promesses sont rejetées, le gestionnaire `.then` sera toujours exécuté et nous obtenons le résultat de chaque promesse.

Vous voulez apprendre à utiliser ces méthodes de promesse dans une application React réelle ? Consultez mon [article précédent](https://www.freecodecamp.org/news/how-to-build-a-hacker-news-clone-using-react/).

## **Merci d'avoir lu !**

C'est tout pour ce tutoriel. J'espère que vous avez appris beaucoup de choses.

Vous voulez une version vidéo de ce tutoriel, consultez ma playlist Y[ouTube](https://bit.ly/3E00PlH).

Si vous voulez maîtriser JavaScript, ES6+, React et Node.js avec un contenu facile à comprendre, consultez ma [chaîne YouTube](https://www.youtube.com/@codingmastery_dev/) et n'oubliez pas de vous abonner.

Vous voulez rester à jour avec un contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).