---
title: Programmation asynchrone en JavaScript – Guide pour débutants
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-01-31T23:17:27.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-programming-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Asynchronous-programming.jpg
tags:
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
seo_title: Programmation asynchrone en JavaScript – Guide pour débutants
seo_desc: 'To understand what asynchronous programming means, think about multiple
  people working on a project simultaneously, each on a different task.

  In traditional (synchronous) programming, each person would have to wait for the
  person before them to finis...'
---

Pour comprendre ce que signifie la programmation asynchrone, pensez à plusieurs personnes travaillant sur un projet simultanément, chacune sur une tâche différente.

En programmation traditionnelle (synchrone), chaque personne devrait attendre que la personne avant elle termine sa tâche avant de commencer la sienne.

Mais avec la programmation asynchrone, tout le monde peut commencer et travailler sur ses tâches simultanément sans attendre que les autres aient terminé.

De même, dans un programme informatique, la programmation asynchrone permet à un programme de travailler sur plusieurs tâches simultanément au lieu de compléter une tâche avant de passer à la suivante. Cela peut permettre au programme de faire plus de choses en un temps plus court.

Par exemple, un programme peut envoyer une requête à un serveur tout en gérant les entrées utilisateur et en traitant des données, tout cela en même temps. De cette façon, le programme peut s'exécuter plus efficacement.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-321.png)

Dans cet article, nous allons plonger dans le monde de la programmation asynchrone en JavaScript, en explorant les différentes techniques et concepts utilisés pour atteindre ce paradigme de programmation puissant.

Des callbacks aux promesses et async/await, vous comprendrez comment exploiter la puissance de la programmation asynchrone dans vos projets JavaScript.

Comprendre la programmation asynchrone est essentiel pour construire des applications web haute performance, que vous soyez un développeur expérimenté ou que vous débutiez avec JavaScript. Alors, continuez à lire pour en apprendre davantage sur ce concept vital.

## Qu'est-ce que la programmation synchrone ?

La programmation synchrone est une manière pour les ordinateurs de faire les choses une étape à la fois, dans l'ordre où les instructions sont données.

Imaginez que vous préparez le dîner et que vous avez une liste de tâches, comme faire bouillir de l'eau pour les pâtes, faire frire du poulet et préparer une salade.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-343.png)

Vous feriez ces tâches une à la fois et attendriez que chacune soit terminée avant de passer à la suivante.

La programmation synchrone fonctionne de manière similaire, où l'ordinateur complétera une tâche avant de passer à la suivante. Cela rend facile la compréhension et la prédiction de ce que l'ordinateur fera à un moment donné.

Voici un exemple de code synchrone en JavaScript :

```javascript
// Définir trois fonctions
function firstTask() {
  console.log("Tâche 1");
}

function secondTask() {
  console.log("Tâche 2");
}

function thirdTask() {
console.log("Tâche 3");  
}

// Exécuter les fonctions
firstTask();
secondTask();
thirdTask();
```

Ce code produira les messages suivants dans l'ordre où ils apparaissent :

```
"Tâche 1"
"Tâche 2"
"Tâche 3"
```

Le code exécutera les tâches dans l'ordre où vous les voyez et attendra que chaque tâche soit terminée avant de passer à la suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-244.png)
_Diagramme montrant comment fonctionne la programmation synchrone._

Cependant, la programmation synchrone peut poser problème dans certaines situations, en particulier lorsqu'il s'agit de tâches qui prennent un temps significatif à compléter.

Par exemple, supposons qu'un programme synchrone effectue une tâche qui nécessite d'attendre une réponse d'un serveur distant. Le programme sera bloqué en attendant la réponse et ne pourra rien faire d'autre jusqu'à ce que la réponse soit retournée. Cela est connu sous le nom de _blocage_, et cela peut conduire à une application apparaissant comme non réactive ou "gelée" pour l'utilisateur.

Considérez le code suivant :

```javascript
function someLongRunningFunction() {
    let start = Date.now();
    while (Date.now() - start < 5000) {
        // ne rien faire
    }
    return "Hello";
}

console.log('Début...');

let result = someLongRunningFunction();
console.log(result);

console.log('...Fin');


```

Dans cet exemple :

* Le programme commence par logger _"Début..."_ dans la console.
* Ensuite, il appelle la fonction `someLongRunningFunction`, qui simule une tâche longue prenant 5 secondes à compléter. Cette fonction bloquera l'exécution du reste du programme pendant son exécution.
* Une fois la fonction terminée, elle retournera _"Hello"_, et le programme le loguera dans la console.
* Enfin, le programme loguera _"...Fin"_ dans la console.

Pendant les 5 secondes où `someLongRunningFunction()` est en cours d'exécution, le programme sera bloqué, deviendra non réactif et ne pourra pas exécuter la ligne de code suivante. Cela peut faire que le programme prend un temps long à compléter et rendre l'application non réactive pour l'utilisateur.

Cependant, si le programme est exécuté de manière asynchrone, il continuera à exécuter la ligne de code suivante plutôt que de se bloquer. Cela permettra au programme de rester réactif et d'exécuter d'autres instructions de code tout en attendant que le délai d'attente se termine.

## Qu'est-ce que la programmation asynchrone ?

La programmation asynchrone est une manière pour un programme informatique de gérer plusieurs tâches simultanément plutôt que de les exécuter les unes après les autres.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-336.png)
_Diagramme montrant comment fonctionne la programmation asynchrone._

La programmation asynchrone permet à un programme de continuer à travailler sur d'autres tâches tout en attendant des événements externes, tels que des requêtes réseau, pour se produire. Cette approche peut grandement améliorer les performances et la réactivité d'un programme.

Par exemple, tandis qu'un programme récupère des données d'un serveur distant, il peut continuer à exécuter d'autres tâches telles que répondre aux entrées utilisateur.

Voici un exemple de programme asynchrone utilisant la méthode `setTimeout` :

```javascript
console.log("Début du script");

setTimeout(function() {
  console.log("Premier timeout terminé");
}, 2000);

console.log("Fin du script");

```

Dans cet exemple, la méthode `setTimeout` exécute une fonction après un temps spécifié. La fonction passée à `setTimeout` sera exécutée de manière asynchrone, ce qui signifie que le programme continuera à exécuter la ligne de code suivante sans attendre que le délai d'attente se termine.

Lorsque vous exécutez le code, la sortie sera :

```
Début du script
Fin du script
Premier timeout terminé

```

Comme vous pouvez le voir, `console.log("Premier timeout terminé")` sera exécuté après 2 secondes. Pendant ce temps, le script continue à exécuter la déclaration de code suivante et ne provoque aucun comportement de "blocage" ou de "gel".

En JavaScript, la programmation asynchrone peut être réalisée à travers diverses techniques. L'une des méthodes les plus courantes est l'utilisation de _callbacks_.

## Comment utiliser une fonction de rappel (Callback)

Disons que vous voulez organiser une fête d'anniversaire pour votre enfant. Vous devez inviter les invités, commander un gâteau et planifier les jeux. Mais vous voulez aussi engager un clown pour divertir les invités. Vous ne pouvez faire venir le clown à la fête qu'une fois que toutes les autres dispositions de la fête sont faites et que les invités sont arrivés.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-341.png)
_Illustration d'un clown_

Alors, vous dites au clown de venir à la fête seulement après que vous l'avez notifié que les invités sont arrivés. Dans ce cas, le clown représente une fonction de rappel, et "l'arrivée des invités" représente la fonction qui doit compléter son exécution avant que le rappel puisse être exécuté.

En code, une fonction de rappel est une fonction qui est passée en argument à une autre fonction, et elle est exécutée après que la première fonction a terminé son exécution. Elle est couramment utilisée en JavaScript pour gérer des opérations asynchrones comme la récupération de données d'un serveur, l'attente d'une entrée utilisateur ou la gestion d'événements.

Voici un exemple simple de la façon dont vous pouvez utiliser une fonction de rappel pour gérer une opération asynchrone :

```javascript
// Déclarer la fonction
function fetchData(callback) {
  setTimeout(() => {
    const data = {name: "John", age: 30};
    callback(data);
  }, 3000);
}

// Exécuter la fonction avec un rappel
fetchData(function(data) {
  console.log(data);
});

console.log("Les données sont en cours de récupération...");

```

Dans cet exemple :

* Nous avons une fonction appelée `fetchData` qui utilise la méthode `setTimeout` pour simuler une opération asynchrone. La fonction prend un rappel en argument.
* La fonction de rappel est ensuite passée avec les données récupérées par la fonction après que le délai d'attente a été complété.

La méthode `setTimeout` est utilisée pour exécuter le rappel après un temps spécifié (dans ce cas, 3 secondes). Le rappel sera exécuté de manière asynchrone, ce qui signifie que le programme continuera à exécuter la ligne de code suivante sans attendre que le délai d'attente se termine.

Lorsque vous exécutez le code, la sortie sera :

```
Les données sont en cours de récupération...
{name: "John", age: 30}

```

Comme vous pouvez le voir, `console.log("Premier timeout terminé")` sera exécuté après 3 secondes. Pendant ce temps, le script continue à exécuter la déclaration suivante, `console.log("Les données sont en cours de récupération...");`.

C'est le concept de base de la programmation asynchrone. Le script n'attend pas que l'opération asynchrone se termine. Il continue simplement à exécuter l'instruction suivante.

## Qu'est-ce que l'enfer des callbacks (Callback Hell) ?

Les callbacks fournissent un moyen utile de gérer les opérations asynchrones. Cependant, lorsque de nombreux callbacks sont imbriqués, le code peut devenir complexe et difficile à lire et à comprendre.

Cela se produit lorsque vous enchaînez plusieurs callbacks les uns après les autres, créant une structure en forme de pyramide d'indentation appelée l'enfer des callbacks, également connu sous le nom de "Pyramide de la Mort".

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-340.png)

Voici un exemple d'enfer des callbacks :

```javascript
getData(function(a) {
  getMoreData(a, function(b) {
    getEvenMoreData(b, function(c) {
      getEvenEvenMoreData(c, function(d) {
        getFinalData(d, function(finalData) {
          console.log(finalData);
        });
      });
    });
  });
});

```

Dans cet exemple :

1. La fonction `getData` prend un callback en argument et est exécutée après la récupération des données.
2. La fonction de callback prend ensuite les données et appelle la fonction `getMoreData`, qui prend également un callback en argument, et ainsi de suite.

Cette imbrication de callbacks peut rendre le code difficile à maintenir, et l'indentation le rend encore plus difficile à voir la structure globale du code.

Pour éviter l'enfer des callbacks, vous pouvez utiliser une méthode plus moderne de gestion des opérations asynchrones connue sous le nom de promesses. Les promesses offrent une manière plus élégante de gérer le flux asynchrone d'un programme par rapport aux fonctions de callback. C'est le sujet de la section suivante.

## Comment fonctionnent les promesses ?

Une promesse représente une manière de gérer les opérations asynchrones de manière plus organisée. Elle sert le même but qu'un callback mais offre de nombreuses capacités supplémentaires et une syntaxe plus lisible.

Une promesse en JavaScript est un espace réservé pour une valeur ou une action future. En créant une promesse, vous dites essentiellement au moteur JavaScript de "promettre" d'effectuer une action spécifique et de vous notifier une fois qu'elle est terminée ou a échoué.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-339.png)
_Illustration d'une promesse et du moteur JS_

Ensuite, des fonctions de callback sont attachées à la promesse pour gérer le résultat de l'action. Ces callbacks seront invoqués lorsque la promesse est remplie (action terminée avec succès) ou rejetée (action échouée).

En tant que développeur JavaScript, vous passerez probablement plus de temps à consommer des promesses retournées par des API Web asynchrones et à gérer leurs résultats plutôt qu'à les créer vous-même.

### Comment créer une promesse

Pour créer une promesse, vous créerez une nouvelle instance de l'objet `Promise` en appelant le constructeur `Promise`.

Le constructeur prend un seul argument : une fonction appelée `executor`. La fonction "executor" est appelée immédiatement lorsque la promesse est créée, et elle prend deux arguments : une fonction `resolve` et une fonction `reject`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-345.png)
_Diagramme de l'anatomie d'une promesse._

Écrivez la ligne de code suivante pour déclarer une promesse :

```javascript
// Initialiser une promesse
const myPromise = new Promise(function(resolve, reject) => {})
```

Maintenant, inspectons l'objet `myPromise` en le loguant dans la console.

```javascript
console.log(myPromise);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/promise-object.jpg)
_Cette image représente une sortie de l'inspection de l'objet `promise`._

Comme vous pouvez le voir, la promesse a un statut _en attente_ et une valeur _indéfinie_. Cela est dû au fait que rien n'a été configuré pour l'objet de la promesse, donc il restera là dans un état en attente pour toujours sans aucune valeur ou résultat.

Maintenant, configurons `myPromise` pour qu'elle se résolve avec une chaîne imprimée dans la console après 2 secondes.

```javascript
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Bonjour de la promesse !");
    }, 2000);
});
```

Maintenant, lorsque vous inspectez l'objet `myPromise`, vous trouverez qu'il a un statut de _"réussi"_, et une valeur définie sur la chaîne que vous avez passée à la fonction `resolve`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/myPromise-obj.jpg)

Une promesse a trois états :

* **En attente** : état initial, ni remplie ni rejetée.
* **Remplie** : signifie qu'une opération a été complétée avec succès.
* **Rejetée** : signifie qu'une opération a échoué.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-347.png)
_États en attente, remplie et rejetée d'une promesse._

Il est important de noter qu'une promesse est dite réglée lorsqu'elle est résolue ou rejetée.

Maintenant que vous savez comment les promesses sont créées, voyons comment vous pouvez les consommer.

### Comment consommer une promesse

Consommer une promesse implique les étapes suivantes :

1. **Obtenir une référence à la promesse** : Pour consommer une promesse, vous devez d'abord obtenir une référence à celle-ci. Basé sur le code de la section précédente, notre référence à une promesse sera l'objet `myPromise`.
2. **Attacher des callbacks à la promesse** : Une fois que vous avez une référence, vous pouvez attacher des fonctions de callback en utilisant les méthodes `.then` et `.catch`. La méthode `.then` est appelée lorsqu'une promesse est remplie et la méthode `.catch` est appelée lorsqu'une promesse est rejetée.
3. **Attendre que la promesse soit remplie ou rejetée** : Une fois que vous avez attaché des callbacks à la promesse, vous pouvez attendre que la promesse soit remplie ou rejetée.

Voici un exemple de la façon dont vous pourriez consommer une promesse :

```javascript
myPromise
    .then((result) => {
        console.log(result);
    })
    .catch((error) => {
        console.log(error);
    });

```

Une fois la promesse remplie, la méthode de callback `.then` sera appelée avec la valeur résolue. Et si la promesse est rejetée, la méthode `.catch` sera appelée avec un message d'erreur.

Vous pouvez également ajouter la méthode `.finally()`, qui sera appelée après qu'une promesse soit réglée. Cela signifie que `.finally()` sera invoqué indépendamment du statut d'une promesse (qu'elle soit résolue ou rejetée).

```javascript
myPromise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  })
  .finally(() => {
    // le code ici sera exécuté indépendamment du statut
    // d'une promesse (remplie ou rejetée)
  });
```

### Comment enchaîner les promesses

L'enchaînement de promesses est un modèle qui permet une approche claire et facile à comprendre pour gérer les opérations asynchrones.

Le modèle implique de connecter plusieurs promesses dans une séquence, où la sortie d'une promesse est passée en entrée à la promesse suivante.

La liaison des promesses est réalisée en utilisant la méthode `then()`. Cette méthode utilise une fonction de callback comme argument et retourne une nouvelle promesse. La nouvelle promesse est ensuite résolue avec la valeur retournée par la fonction de callback.

Voici un exemple d'enchaînement de promesses :

```javascript
fetch('https://example.com/data')
    .then(response => response.json())
    .then(data => processData(data))
    .then(processedData => {
        // faire quelque chose avec les données traitées
    })
    .catch(error => console.log(error))

```

D'après le code ci-dessus :

* La première promesse, qui est la fonction `fetch API`, récupère des données d'un serveur.
* La deuxième promesse analyse la réponse en JSON.
* La troisième promesse traite les données.
* La quatrième promesse effectue une action sur les données.
* La méthode `.catch` à la fin de la chaîne gérera toute erreur survenue dans l'une des promesses précédentes.

Il est important de garder à l'esprit que les méthodes `.then` sont exécutées de manière asynchrone et dans l'ordre, chacune attendant que la précédente soit résolue, et que la valeur retournée de chaque `.then` sera passée en argument à la suivante.

### Gestion des erreurs

Lorsque une promesse est rejetée, elle déclenchera la méthode `.catch()`, qui gère les erreurs. La méthode `.catch()` prend un seul argument, qui est l'erreur lancée.

Une autre façon de gérer les erreurs dans une promesse est d'utiliser le bloc "try-catch" à l'intérieur d'une méthode `.then`.

Voici un exemple :

```javascript
fetch("https://api.github.com/users/octocat")
  .then((response) => response.json())
  .then((data) => {
    try {
      // traitement des données reçues
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  })
  .catch((error) => console.log(error));
```

D'après le code ci-dessus :

* La fonction `fetch()` fait une requête à l'API GitHub pour récupérer les données utilisateur.
* Le bloc "try-catch" est utilisé à l'intérieur de la deuxième méthode `.then` pour gérer toute erreur qui peut survenir lors du traitement des données reçues du serveur.
* Et la méthode `.catch` externe ne capturera que les erreurs qui se produisent pendant la requête fetch.

La gestion des erreurs est très importante car les promesses sont utilisées pour gérer les opérations asynchrones, et ces opérations peuvent échouer pour diverses raisons.

Si une erreur se produit pendant l'exécution d'une promesse et qu'elle n'est pas gérée, le programme continuera à s'exécuter et peut conduire à un comportement inattendu ou à des plantages.

En gérant les erreurs, nous pouvons nous assurer que le programme peut continuer à fonctionner même lorsqu'une erreur se produit et également fournir un retour significatif à l'utilisateur concernant le problème.

### Comment utiliser la méthode Promise.all

La méthode `Promise.all()` prend un tableau de promesses en entrée et retourne une seule promesse qui est remplie lorsque toutes les promesses d'entrée ont été remplies. Elle peut être utile lorsque vous attendez que plusieurs promesses soient résolues avant de prendre une action.

Par exemple, si vous voulez récupérer des données à partir de plusieurs URL.

```javascript
let promise1 = fetch('https://jsonplaceholder.typicode.com/posts/1');
let promise2 = fetch('https://jsonplaceholder.typicode.com/posts/2');
let promise3 = fetch('https://jsonplaceholder.typicode.com/posts/3');

```

Ici, `promise1`, `promise2`, et `promise3` sont des promesses qui récupèrent des données à partir de trois URL différentes.

Maintenant, vous pouvez utiliser `Promise.all([promise1, promise2, promise3])` pour attendre que toutes les promesses soient résolues avant de faire quelque chose avec les données, comme montré ci-dessous.

```javascript
Promise.all([promise1, promise2, promise3])
.then((values) => {
  console.log(values);
})

```

Dans l'exemple ci-dessus :

* `Promise.all()` prend un tableau de promesses en entrée et retourne une nouvelle promesse.
* La méthode `then` est ensuite appelée sur la promesse retournée pour logger les valeurs résolues de toutes les promesses d'entrée dans l'ordre où elles ont été passées à `Promise.all()`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-26-103003-1.jpg)

Notez que dans une instance où une promesse d'entrée est rejetée, la promesse retournée sera également rejetée avec la valeur de la première promesse rejetée.

### Comment utiliser l'API Fetch avec les promesses

J'ai utilisé l'API Fetch pour certains exemples dans cet article, et je comprends qu'elle peut être peu familière pour certains lecteurs. J'ai donc créé cette section pour expliquer les bases de l'API Fetch pour ceux qui pourraient avoir besoin de se familiariser davantage avec elle.

L'API Fetch est une fonctionnalité intégrée de JavaScript qui vous permet de faire des requêtes réseau, comme récupérer des données d'un serveur. C'est une alternative moderne à l'ancienne API XMLHttpRequest et est conçue pour être plus facile et plus puissante.

Voici un exemple de la façon d'utiliser l'API Fetch pour récupérer des données d'un serveur :

```javascript
fetch('https://some-api.com/data')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple,

* La méthode `fetch()` est utilisée pour faire une requête au serveur situé à "[https://some-api.com/data](https://some-api.com/data)". La valeur retournée est une promesse qui sera remplie avec la réponse du serveur.
* La première méthode `.then()` est appelée pour consommer la promesse et extraire les données JSON de la réponse.
* La méthode `then()` suivante est appelée pour logger les données extraites dans la console.
* Si des erreurs se produisent, elles seront capturées dans la méthode `catch()` et loggées dans la console.

J'espère que l'explication ci-dessus aide à clarifier toute confusion concernant l'API Fetch et vous permet de mieux comprendre les exemples fournis dans cet article.

## **Fonctions asynchrones avec `async`/`await`**

`Async/Await` est une fonctionnalité qui vous permet d'écrire du code asynchrone de manière plus synchrone et lisible.

* `async` est un mot-clé utilisé pour déclarer une fonction comme asynchrone.
* `await` est un mot-clé utilisé à l'intérieur d'une fonction `async` pour suspendre l'exécution de la fonction jusqu'à ce qu'une promesse soit résolue.

Voici un exemple de la façon dont vous pouvez utiliser `async/await` :

```javascript
async function getData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
  const data = await response.json();
  console.log(data);
}

getData();

```

Dans cet exemple,

* la fonction `getData` est déclarée comme une fonction asynchrone en utilisant le mot-clé `async`.
* À l'intérieur de la fonction asynchrone, nous utilisons le mot-clé `await` pour attendre que la fonction `fetch` se termine et récupère des données d'une API.
* Une fois les données récupérées, nous utilisons `await` à nouveau pour attendre et analyser les données récupérées en JSON.
* Et enfin, nous loggons les données dans la console.

"Async/Await" est un outil puissant pour gérer les opérations asynchrones. Il permet d'écrire un code plus lisible et maintenable en éliminant le besoin de callbacks et en fournissant une manière plus intuitive de gérer les opérations asynchrones.

L'utilisation du mot-clé "async" avant une définition de fonction et du mot-clé "await" avant une opération asynchrone fait que le code ressemble davantage à du code synchrone, le rendant plus facile à comprendre.

Dans l'ensemble, "Async/Await" est un atout précieux dans la boîte à outils du développeur JavaScript et peut grandement simplifier la gestion des opérations asynchrones dans votre code.

## Conclusion

En résumé, la programmation asynchrone est un concept essentiel en JavaScript qui permet à votre code de s'exécuter en arrière-plan sans bloquer l'exécution d'autres codes.

En utilisant des fonctionnalités comme les callbacks, async/await et les promesses, les développeurs peuvent créer des applications plus efficaces et réactives.

La programmation asynchrone peut être difficile à comprendre au début. Mais avec de la pratique et une compréhension solide des concepts, elle devient un outil puissant pour construire des applications web haute performance.

Merci d'avoir lu cet article !

Si vous avez aimé cet article et que vous souhaitez en apprendre davantage sur la programmation, suivez-moi sur Instagram à [@alege_dev](https://www.instagram.com/alege_dev/), où je poste régulièrement des mises à jour et des conseils sur divers sujets de programmation.