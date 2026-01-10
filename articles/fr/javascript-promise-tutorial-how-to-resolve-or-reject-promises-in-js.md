---
title: Tutoriel JavaScript Promise – Comment résoudre ou rejeter des Promesses en
  JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-12-15T00:49:56.000Z'
originalURL: https://freecodecamp.org/news/javascript-promise-tutorial-how-to-resolve-or-reject-promises-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Tutoriel JavaScript Promise – Comment résoudre ou rejeter des Promesses
  en JS
seo_desc: "Promises are important building blocks for asynchronous operations in JavaScript.\
  \ You may think that promises are not so easy to understand, learn, and work with.\
  \ And trust me, you are not alone! \nPromises are challenging for many web developers,\
  \ eve..."
---

`Promise` sont des éléments de construction importants pour les opérations asynchrones en JavaScript. Vous pouvez penser que les promesses ne sont pas si faciles à comprendre, à apprendre et à utiliser. Et croyez-moi, vous n'êtes pas seul !

Les promesses sont un défi pour de nombreux développeurs web, même après des années de travail avec elles.

Dans cet article, je veux essayer de changer cette perception tout en partageant ce que j'ai appris sur les Promesses JavaScript au cours des dernières années. J'espère que vous le trouverez utile.

# Qu'est-ce qu'une Promesse en JavaScript ?

Un `Promise` est un objet spécial JavaScript. Il produit une valeur après qu'une opération `asynchrone` (aka, async) est terminée avec succès, ou une erreur si elle ne se termine pas avec succès en raison d'un délai d'attente, d'une erreur réseau, etc.

Les appels réussis sont indiqués par l'appel de la fonction `resolve`, et les erreurs sont indiquées par l'appel de la fonction `reject`.

Vous pouvez créer une promesse en utilisant le constructeur de promesse comme ceci :

```js
let promise = new Promise(function(resolve, reject) {    
    // Faire un appel asynchrone et soit résoudre soit rejeter
});
```

Dans la plupart des cas, une promesse peut être utilisée pour une opération asynchrone. Cependant, techniquement, vous pouvez résoudre/rejeter à la fois sur des opérations synchrones et asynchrones.

# Attendez, n'avons-nous pas des fonctions `callback` pour les opérations async ?

Oh, oui ! C'est vrai. Nous avons des fonctions `callback` en JavaScript. Mais un callback n'est pas une chose spéciale en JavaScript. C'est une fonction régulière qui produit des résultats après qu'un appel `asynchrone` est terminé (avec succès/erreur).

Le mot 'asynchrone' signifie que quelque chose se produit dans le futur, pas maintenant. Habituellement, les callbacks ne sont utilisés que lorsque l'on fait des choses comme des appels réseau, ou des téléchargements/téléchargements, parler à des bases de données, et ainsi de suite.

Bien que les `callbacks` soient utiles, ils ont aussi un énorme inconvénient. Parfois, nous pouvons avoir un callback à l'intérieur d'un autre callback qui est dans un autre callback et ainsi de suite. Je suis sérieux ! Comprenons cet "enfer des callbacks" avec un exemple.

## Comment éviter l'enfer des callbacks – Exemple PizzaHub

Commandons une pizza Veg Margherita 🍕 chez PizzaHub. Lorsque nous passons la commande, PizzaHub détecte automatiquement notre localisation, trouve un restaurant de pizza à proximité, et vérifie si la pizza que nous demandons est disponible.

Si elle est disponible, il détecte quel type de boissons nous obtenons gratuitement avec la pizza, et enfin, il passe la commande.

Si la commande est passée avec succès, nous recevons un message avec une confirmation.

Alors, comment codons-nous cela en utilisant des fonctions de callback ? J'ai imaginé quelque chose comme ceci :

```js
function orderPizza(type, name) {
    
    // Interroger le pizzahub pour un magasin
    query(`/api/pizzahub/`, function(result, error){
       if (!error) {
           let shopId = result.shopId;
           
           // Obtenir le magasin et interroger les pizzas
           query(`/api/pizzahub/pizza/${shopid}`, function(result, error){
               if (!error) {
                   let pizzas = result.pizzas;
                   
                   // Trouver si ma pizza est disponible
                   let myPizza = pizzas.find((pizza) => {
                       return (pizza.type===type && pizza.name===name);
                   });
                   
                   // Vérifier les boissons gratuites
                   query(`/api/pizzahub/beverages/${myPizza.id}`, function(result, error){
                       if (!error) {
                           let beverage = result.id;
                           
                           // Préparer une commande
                           query(`/api/order`, {'type': type, 'name': name, 'beverage': beverage}, function(result, error){
                              if (!error) {
                                  console.log(`Votre commande de ${type} ${name} avec ${beverage} a été passée`);
                              } else {
                                  console.log(`Mauvaise chance, pas de pizza pour vous aujourd'hui !`);
                              }
                           });

                       }
                   })
               }
           });
       } 
    });
}

// Appeler la méthode orderPizza
orderPizza('veg', 'margherita');
```

Examinons de plus près la fonction `orderPizza` dans le code ci-dessus.

Elle appelle une API pour obtenir l'id du magasin de pizza à proximité. Après cela, elle obtient la liste des pizzas disponibles dans ce restaurant. Elle vérifie si la pizza que nous demandons est trouvée et fait un autre appel API pour trouver les boissons pour cette pizza. Enfin, l'API de commande passe la commande.

Ici, nous utilisons un callback pour chacun des appels API. Cela nous amène à utiliser un autre callback à l'intérieur du précédent, et ainsi de suite.

Cela signifie que nous tombons dans ce que nous appelons (très expressivement) l'`Enfer des Callbacks`. Et qui veut ça ? Cela forme également une pyramide de code qui n'est pas seulement confuse mais aussi sujette aux erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/callback-hell.png)
_Démonstration de l'enfer des callbacks et de la pyramide_

Il existe quelques moyens de sortir (ou de ne pas entrer) de l'`enfer des callbacks`. Le plus courant est d'utiliser une fonction `Promise` ou `async`. Cependant, pour bien comprendre les fonctions `async`, vous devez d'abord avoir une bonne compréhension des `Promise`s.

Alors, commençons et plongeons dans les promesses.

# Comprendre les états des Promesses

Juste pour réviser, une promesse peut être créée avec la syntaxe du constructeur, comme ceci :

```js
let promise = new Promise(function(resolve, reject) {
  // Code à exécuter
});
```

La fonction constructeur prend une fonction comme argument. Cette fonction est appelée la `fonction exécutrice`.

```js
// Fonction exécutrice passée au
// Constructeur de Promise comme argument
function(resolve, reject) {
    // Votre logique va ici...
}
```

La fonction exécutrice prend deux arguments, `resolve` et `reject`. Ce sont les callbacks fournis par le langage JavaScript. Votre logique va à l'intérieur de la fonction exécutrice qui s'exécute automatiquement lorsqu'une `new Promise` est créée.

Pour que la promesse soit efficace, la fonction exécutrice doit appeler l'une des fonctions de callback, `resolve` ou `reject`. Nous en apprendrons plus sur cela en détail dans un instant.

Le constructeur `new Promise()` retourne un objet `promise`. Comme la fonction exécutrice doit gérer des opérations async, l'objet promesse retourné doit être capable d'informer lorsque l'exécution a été démarrée, complétée (résolue) ou retournée avec une erreur (rejetée).

Un objet `promise` a les propriétés internes suivantes :

1. `state` – Cette propriété peut avoir les valeurs suivantes :

* `pending` : Initialement lorsque la fonction exécutrice commence l'exécution.
* `fulfilled` : Lorsque la promesse est résolue.
* `rejected` : Lorsque la promesse est rejetée.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/states_1.png)
_États des promesses_

2. `result` – Cette propriété peut avoir les valeurs suivantes :

* `undefined` : Initialement lorsque la valeur de `state` est `pending`.
* `value` : Lorsque `resolve(value)` est appelé.
* `error` : Lorsque `reject(error)` est appelé.

Ces propriétés internes sont inaccessibles par le code mais elles sont inspectables. Cela signifie que nous pourrons inspecter les valeurs des propriétés `state` et `result` en utilisant l'outil de débogage, mais nous ne pourrons pas y accéder directement en utilisant le programme.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/promise_state_inspect.png)
_Pouvant inspecter les propriétés internes d'une promesse_

L'état d'une promesse peut être `pending`, `fulfilled` ou `rejected`. Une promesse qui est soit résolue soit rejetée est appelée `settled`.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/states_2.png)
_Une promesse réglée est soit remplie soit rejetée_

### Comment les promesses sont résolues et rejetées

Voici un exemple de promesse qui sera résolue (état `fulfilled`) avec la valeur `I am done` immédiatement.

```js
let promise = new Promise(function(resolve, reject) {
    resolve("I am done");
});
```

La promesse ci-dessous sera rejetée (état `rejected`) avec le message d'erreur `Something is not right!`.

```js
let promise = new Promise(function(resolve, reject) {
    reject(new Error('Something is not right!'));
});
```

Un point important à noter :

> Un exécutant de promesse doit appeler seulement un `resolve` ou un `reject`. Une fois qu'un état est changé (pending => fulfilled ou pending => rejected), c'est tout. Tout appel supplémentaire à `resolve` ou `reject` sera ignoré.

```js
let promise = new Promise(function(resolve, reject) {
  resolve("I am surely going to get resolved!");

  reject(new Error('Will this be ignored?')); // ignoré
  resolve("Ignored?"); // ignoré
});
```

Dans l'exemple ci-dessus, seul le premier à résoudre sera appelé et le reste sera ignoré.

# Comment gérer une Promesse une fois que vous l'avez créée

Une `Promise` utilise une fonction exécutrice pour compléter une tâche (principalement de manière asynchrone). Une fonction consommatrice (qui utilise un résultat de la promesse) doit être notifiée lorsque la fonction exécutrice a terminé soit en résolvant (succès) soit en rejetant (erreur).

Les méthodes de gestion, `.then()`, `.catch()` et `.finally()`, aident à créer le lien entre les fonctions exécutrices et consommatrices afin qu'elles puissent être synchronisées lorsqu'une promesse `resolve` ou `reject`.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/consumer_executor.png)
_Les fonctions exécutrices et consommatrices_

## Comment utiliser le gestionnaire de Promesse `.then()`

La méthode `.then()` doit être appelée sur l'objet promesse pour gérer un résultat (resolve) ou une erreur (reject).

Elle accepte deux fonctions comme paramètres. Habituellement, la méthode `.then()` doit être appelée à partir de la fonction consommatrice où vous souhaitez connaître le résultat de l'exécution d'une promesse.

```js
promise.then(
  (result) => { 
     console.log(result);
  },
  (error) => { 
     console.log(error);
  }
);
```

Si vous êtes intéressé uniquement par les résultats réussis, vous pouvez simplement passer un argument, comme ceci :

```js
promise.then(
  (result) => { 
      console.log(result);
  }
);
```

Si vous êtes intéressé uniquement par le résultat d'erreur, vous pouvez passer `null` pour le premier argument, comme ceci :

```js
promise.then(
  null,
  (error) => { 
      console.log(error)
  }
);
```

Cependant, vous pouvez gérer les erreurs de manière plus efficace en utilisant la méthode `.catch()` que nous verrons dans un instant.

Regardons quelques exemples de gestion des résultats et des erreurs en utilisant les gestionnaires `.then` et `.catch`. Nous allons rendre cet apprentissage un peu plus amusant avec quelques requêtes asynchrones réelles. Nous utiliserons l'API [PokeAPI](https://pokeapi.co/) pour obtenir des informations sur les Pokémon et les résoudre/rejeter en utilisant des Promesses.

Tout d'abord, créons une fonction générique qui accepte une URL PokeAPI comme argument et retourne une Promesse. Si l'appel API est réussi, une promesse résolue est retournée. Une promesse rejetée est retournée pour tout type d'erreurs.

Nous utiliserons cette fonction dans plusieurs exemples à partir de maintenant pour obtenir une promesse et travailler dessus.

```js
function getPromise(URL) {
  let promise = new Promise(function (resolve, reject) {
    let req = new XMLHttpRequest();
    req.open("GET", URL);
    req.onload = function () {
      if (req.status == 200) {
        resolve(req.response);
      } else {
        reject("Il y a une erreur !");
      }
    };
    req.send();
  });
  return promise;
}
```

Exemple 1 : Obtenir les informations de 50 Pokémon :

```js
const ALL_POKEMONS_URL = 'https://pokeapi.co/api/v2/pokemon?limit=50';

// Nous avons déjà discuté de cette fonction !
let promise = getPromise(ALL_POKEMONS_URL);

const consumer = () => {
    promise.then(
        (result) => {
            console.log({result}); // Journaliser le résultat de 50 Pokémon
        },
        (error) => {
            // Comme l'URL est valide, cela ne sera pas appelé.
            console.log('Nous avons rencontré une erreur !'); // Journaliser une erreur
    });
}

consumer();
```

Exemple 2 : Essayons une URL invalide

```js
const POKEMONS_BAD_URL = 'https://pokeapi.co/api/v2/pokemon-bad/';

// Cela sera rejeté car l'URL est 404
let promise = getPromise(POKEMONS_BAD_URL);

const consumer = () => {
    promise.then(
        (result) => {
            // La promesse n'a pas été résolue. Par conséquent, elle ne
            // ne sera pas exécutée.
            console.log({result});
        },
        (error) => {
            // Une promesse rejetée exécutera ceci
            console.log('Nous avons rencontré une erreur !'); // Journaliser une erreur
        }
    );
}

consumer();
```

## Comment utiliser le gestionnaire de Promesse `.catch()`

Vous pouvez utiliser cette méthode de gestionnaire pour gérer les erreurs (rejets) des promesses. La syntaxe de passage de `null` comme premier argument à `.then()` n'est pas une excellente façon de gérer les erreurs. Nous avons donc `.catch()` pour faire le même travail avec une syntaxe plus propre :

```js
// Cela sera rejeté car l'URL est 404
let promise = getPromise(POKEMONS_BAD_URL);

const consumer = () => {
    promise.catch(error => console.log(error));
}

consumer();
```

Si nous lançons une erreur comme `new Error("Something wrong!")` au lieu d'appeler `reject` depuis l'exécutant de la promesse et les gestionnaires, elle sera toujours traitée comme un rejet. Cela signifie que cela sera capturé par la méthode de gestionnaire `.catch`.

Cela est valable pour toute exception _synchrone_ qui se produit dans les fonctions exécutrices et gestionnaires de la promesse.

Voici un exemple où cela sera traité comme un rejet et la méthode de gestionnaire `.catch` sera appelée :

```js
new Promise((resolve, reject) => {
  throw new Error("Something is wrong!"); // Pas d'appel de reject
}).catch((error) => console.log(error));
```

## Comment utiliser le gestionnaire de Promesse `.finally()`

Le gestionnaire `.finally()` effectue des nettoyages comme l'arrêt d'un chargeur, la fermeture d'une connexion en direct, et ainsi de suite. La méthode `finally()` sera appelée indépendamment du fait qu'une promesse `resolve` ou `reject`. Elle transmet le résultat ou l'erreur au gestionnaire suivant qui peut appeler un .then() ou .catch() à nouveau.

Voici un exemple qui vous aidera à comprendre les trois méthodes ensemble :

```js
let loading = true;
loading && console.log('Chargement...');

// Obtenir la Promesse
promise = getPromise(ALL_POKEMONS_URL);

promise.finally(() => {
    loading = false;
    console.log(`Promesse réglée et chargement est ${loading}`);
}).then((result) => {
    console.log({result});
}).catch((error) => {
    console.log(error)
});
```

Pour expliquer un peu plus :

* La méthode `.finally()` rend le chargement `false`.
* Si la promesse se résout, la méthode `.then()` sera appelée. Si la promesse rejette avec une erreur, la méthode `.catch()` sera appelée. Le `.finally()` sera appelé indépendamment de la résolution ou du rejet.

# Qu'est-ce que la Chaîne de Promesses ?

L'appel `promise.then()` retourne toujours une promesse. Cette promesse aura l'état `pending` et le résultat `undefined`. Cela nous permet d'appeler la méthode `.then` suivante sur la nouvelle promesse.

Lorsque la première méthode `.then` retourne une valeur, la méthode `.then` suivante peut la recevoir. La deuxième peut maintenant passer à la troisième `.then()` et ainsi de suite. Cela forme une chaîne de méthodes `.then` pour transmettre les promesses. Ce phénomène est appelé la `Chaîne de Promesses`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-105.png)
_Chaîne de Promesses_

Voici un exemple :

```js
let promise = getPromise(ALL_POKEMONS_URL);

promise.then(result => {
    let onePokemon = JSON.parse(result).results[0].url;
    return onePokemon;
}).then(onePokemonURL => {
    console.log(onePokemonURL);
}).catch(error => {
    console.log('Dans le catch', error);
});
```

Ici, nous obtenons d'abord une promesse résolue, puis nous extrayons l'URL pour atteindre le premier Pokémon. Nous retournons ensuite cette valeur et elle sera transmise comme une promesse au gestionnaire de fonction .then() suivant. D'où la sortie,

```shell
https://pokeapi.co/api/v2/pokemon/1/
```

La méthode `.then` peut retourner soit :

* Une valeur (nous avons déjà vu cela)
* Une toute nouvelle promesse.

Elle peut également lancer une erreur.

Voici un exemple où nous avons créé une chaîne de promesses avec les méthodes `.then` qui retournent des résultats et une nouvelle promesse :

```js
// Chaîne de Promesses avec plusieurs then et catch
let promise = getPromise(ALL_POKEMONS_URL);

promise.then(result => {
    let onePokemon = JSON.parse(result).results[0].url;
    return onePokemon;
}).then(onePokemonURL => {
    console.log(onePokemonURL);
    return getPromise(onePokemonURL);
}).then(pokemon => {
    console.log(JSON.parse(pokemon));
}).catch(error => {
    console.log('Dans le catch', error);
});
```

Dans le premier appel `.then`, nous extrayons l'URL et la retournons comme une valeur. Cette URL sera transmise au deuxième appel `.then` où nous retournons une nouvelle promesse prenant cette URL comme argument.

Cette promesse sera résolue et transmise dans la chaîne où nous obtenons les informations sur le Pokémon. Voici la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-159.png)
_Sortie de l'appel de la chaîne de promesses_

En cas d'erreur ou de rejet de promesse, la méthode .catch dans la chaîne sera appelée.

Un point à noter : Appeler `.then` plusieurs fois ne forme pas une chaîne de promesses. Vous pourriez finir par faire quelque chose comme ceci seulement pour introduire un bug dans le code :

```js
let promise = getPromise(ALL_POKEMONS_URL);

promise.then(result => {
    let onePokemon = JSON.parse(result).results[0].url;
    return onePokemon;
});
promise.then(onePokemonURL => {
    console.log(onePokemonURL);
    return getPromise(onePokemonURL);
});
promise.then(pokemon => {
    console.log(JSON.parse(pokemon));
});

```

Nous appelons la méthode `.then` trois fois sur la même promesse, mais nous ne transmettons pas la promesse. Cela est différent de la chaîne de promesses. Dans l'exemple ci-dessus, la sortie sera une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-160.png)

# Comment gérer plusieurs promesses

En plus des méthodes de gestion (.then, .catch, et .finally), il y a six méthodes statiques disponibles dans l'API Promise. Les quatre premières méthodes acceptent un tableau de promesses et les exécutent en parallèle.

1. Promise.all
2. Promise.any
3. Promise.allSettled
4. Promise.race
5. Promise.resolve
6. Promise.reject

Passons en revue chacune d'elles.

## La méthode Promise.all()

`Promise.all([promises])` accepte une collection (par exemple, un tableau) de promesses comme argument et les exécute en parallèle.

Cette méthode attend que toutes les promesses soient résolues et retourne le tableau des résultats des promesses. Si l'une des promesses est rejetée ou échoue en raison d'une erreur, tous les autres résultats de promesses seront ignorés.

Créons trois promesses pour obtenir des informations sur trois Pokémon.

```js
const BULBASAUR_POKEMONS_URL = 'https://pokeapi.co/api/v2/pokemon/bulbasaur';
const RATICATE_POKEMONS_URL = 'https://pokeapi.co/api/v2/pokemon/raticate';
const KAKUNA_POKEMONS_URL = 'https://pokeapi.co/api/v2/pokemon/kakuna';


let promise_1 = getPromise(BULBASAUR_POKEMONS_URL);
let promise_2 = getPromise(RATICATE_POKEMONS_URL);
let promise_3 = getPromise(KAKUNA_POKEMONS_URL);
```

Utilisez la méthode Promise.all() en passant un tableau de promesses.

```js
Promise.all([promise_1, promise_2, promise_3]).then(result => {
    console.log({result});
}).catch(error => {
    console.log('Une erreur est survenue');
});
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-161.png)

Comme vous le voyez dans la sortie, le résultat de toutes les promesses est retourné. Le temps pour exécuter toutes les promesses est égal au temps maximum que la promesse prend pour s'exécuter.

## La méthode Promise.any()

`Promise.any([promises])` - Similaire à la méthode `all()`, `.any()` accepte également un tableau de promesses pour les exécuter en parallèle. Cette méthode n'attend pas que toutes les promesses soient résolues. Elle est terminée lorsqu'une des promesses est réglée.

```javascript
 Promise.any([promise_1, promise_2, promise_3]).then(result => {
     console.log(JSON.parse(result));
 }).catch(error => {
     console.log('Une erreur est survenue');
 });
```

La sortie serait le résultat de l'une des promesses résolues :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-162.png)

## La méthode Promise.allSettled()

`Promise.allSettled([promises])` - Cette méthode attend que toutes les promesses soient réglées (résolues/rejetées) et retourne leurs résultats sous forme de tableau d'objets. Les résultats contiendront un état (rempli/rejeté) et une valeur, si rempli. En cas de statut rejeté, elle retournera une raison pour l'erreur.

Voici un exemple de toutes les promesses remplies :

```js
Promise.allSettled([promise_1, promise_2, promise_3]).then(result => {
    console.log({result});
}).catch(error => {
    console.log('Il y a une erreur !');
});
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-163.png)

Si l'une des promesses est rejetée, disons, la promise_1,

```javascript
let promise_1 = getPromise(POKEMONS_BAD_URL);
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-164.png)

## La méthode Promise.race()

`Promise.race([promises])` – Elle attend que la première (la plus rapide) promesse soit réglée, et retourne le résultat/erreur en conséquence.

```js
Promise.race([promise_1, promise_2, promise_3]).then(result => {
    console.log(JSON.parse(result));
}).catch(error => {
    console.log('Une erreur est survenue');
});
```

Sortie de la promesse la plus rapide qui a été résolue :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-165.png)

## Les méthodes Promise.resolve/reject

`Promise.resolve(value)` – Elle résout une promesse avec la valeur qui lui est passée. C'est la même chose que ce qui suit :

```js
let promise = new Promise(resolve => resolve(value));
```

`Promise.reject(error)` – Elle rejette une promesse avec l'erreur qui lui est passée. C'est la même chose que ce qui suit :

```js
let promise = new Promise((resolve, reject) => reject(error));
```

# Pouvez-vous réécrire l'exemple PizzaHub avec des Promesses ?

Bien sûr, faisons-le. Supposons que la méthode `query` retournera une promesse. Voici un exemple de méthode query(). Dans la vraie vie, cette méthode pourrait parler à une base de données et retourner des résultats. Dans ce cas, elle est très codée en dur mais sert le même but.

```js
function query(endpoint) {
  if (endpoint === `/api/pizzahub/`) {
    return new Promise((resolve, reject) => {
      resolve({'shopId': '123'});
    })
  } else if (endpoint.indexOf('/api/pizzahub/pizza/') >=0) {
    return new Promise((resolve, reject) => {
      resolve({pizzas: [{'type': 'veg', 'name': 'margherita', 'id': '123'}]});
    })
  } else if (endpoint.indexOf('/api/pizzahub/beverages') >=0) {
    return new Promise((resolve, reject) => {
      resolve({id: '10', 'type': 'veg', 'name': 'margherita', 'beverage': 'coke'});
    })
  } else if (endpoint === `/api/order`) {
    return new Promise((resolve, reject) => {
      resolve({'type': 'veg', 'name': 'margherita', 'beverage': 'coke'});
    })
  }
}
```

Ensuite, nous allons refactoriser notre `callback hell`. Pour ce faire, nous allons d'abord créer quelques fonctions logiques :

```js
// Retourne un identifiant de magasin
let getShopId = result => result.shopId;

// Retourne une promesse avec la liste des pizzas pour un magasin
let getPizzaList = shopId => {
  const url = `/api/pizzahub/pizza/${shopId}`;
  return query(url);
}

// Retourne une promesse avec la pizza qui correspond à la demande du client
let getMyPizza = (result, type, name) => {
  let pizzas = result.pizzas;
  let myPizza = pizzas.find((pizza) => {
    return (pizza.type===type && pizza.name===name);
  });
  const url = `/api/pizzahub/beverages/${myPizza.id}`;
  return query(url);
}

// Retourne une promesse après avoir passé la commande
let performOrder = result => {
  let beverage = result.id;
   return query(`/api/order`, {'type': result.type, 'name': result.name, 'beverage': result.beverage});
}

// Confirmer la commande
let confirmOrder = result => {
    console.log(`Votre commande de ${result.type} ${result.name} avec ${result.beverage} a été passée !`);
}
```

Utilisez ces fonctions pour créer les promesses requises. C'est ici que vous devriez comparer avec l'exemple `callback hell`. C'est si beau et élégant.

```js
function orderPizza(type, name) {
  query(`/api/pizzahub/`)
  .then(result => getShopId(result))
  .then(shopId => getPizzaList(shopId))
  .then(result => getMyPizza(result, type, name))
  .then(result => performOrder(result))
  .then(result => confirmOrder(result))
  .catch(function(error){
    console.log(`Mauvaise chance, pas de pizza pour vous aujourd'hui !`);
  })
}
```

Enfin, appelez la méthode orderPizza() en passant le type et le nom de la pizza, comme ceci :

```js
orderPizza('veg', 'margherita');

```

# Qu'est-ce qui suit à partir de là ?

Si vous êtes ici et avez lu la plupart des lignes ci-dessus, félicitations ! Vous devriez maintenant avoir une meilleure compréhension des Promesses JavaScript. Tous les exemples utilisés dans cet article se trouvent dans ce [dépôt GitHub](https://github.com/atapas/js-promise-example).

Ensuite, vous devriez apprendre la fonction `async` en JavaScript qui simplifie encore les choses. Le concept des promesses JavaScript est mieux appris en écrivant de petits exemples et en construisant sur eux.

Indépendamment du framework ou de la bibliothèque (Angular, React, Vue, etc.) que nous utilisons, les opérations asynchrones sont inévitables. Cela signifie que nous devons comprendre les promesses pour que les choses fonctionnent mieux.

De plus, je suis sûr que vous trouverez l'utilisation de la méthode `fetch` beaucoup plus facile maintenant :

```js
fetch('/api/user.json')
.then(function(response) {
    return response.json();
})
.then(function(json) {
    console.log(json); // {"name": "tapas", "blog": "freeCodeCamp"}
});
```

* La méthode `fetch` retourne une promesse. Nous pouvons donc appeler la méthode de gestionnaire `.then` sur celle-ci.
* Le reste concerne la chaîne de promesses que nous avons apprise dans cet article.

# Avant de terminer...

Merci d'avoir lu jusqu'ici ! Restons en contact. Vous pouvez me mentionner sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary) avec des commentaires.

Vous pourriez également aimer ces autres articles :

* [JavaScript undefined et null : Parlons-en une dernière fois !](https://blog.greenroots.info/javascript-undefined-and-null-lets-talk-about-it-one-last-time-ckh64kmz807v848s15kdkg3dd)
* [JavaScript : Comparaison d'égalité avec ==, === et Object.is](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis-ckdpt2ryk01vel9s186ft8cwl)
* [Le mot-clé `this` de JavaScript + 5 règles de liaison clés expliquées pour les débutants JS](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)
* [JavaScript TypeOf – Comment vérifier le type d'une variable ou d'un objet en JS](https://www.freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js/)

C'est tout pour l'instant. À bientôt avec mon prochain article. En attendant, prenez bien soin de vous.