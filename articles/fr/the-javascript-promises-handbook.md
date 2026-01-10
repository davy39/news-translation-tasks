---
title: Comment fonctionnent les Promises JavaScript – Guide pour débutants
subtitle: ''
author: Joe Attardi
co_authors: []
series: null
date: '2024-02-13T23:37:58.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-promises-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/How-JavaScript-Promises-Work-Cover.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Comment fonctionnent les Promises JavaScript – Guide pour débutants
seo_desc: 'Many operations, such as network requests, are asynchronous in nature.
  One of the most useful and powerful tools for working with asynchronous code is
  the Promise. In this handbook, you''ll learn all about JavaScript Promises and how
  to use them.

  Tabl...'
---

De nombreuses opérations, telles que les requêtes réseau, sont asynchrones par nature. L'un des outils les plus utiles et puissants pour travailler avec du code asynchrone est la Promise. Dans ce guide, vous apprendrez tout sur les Promises JavaScript et comment les utiliser.

## Table des matières

1. [Qu'est-ce qu'une Promise ?](#heading-quest-ce-quune-promise)
2. [Comparaison des Promises avec d'autres modèles asynchrones](#heading-comparaison-des-promises-avec-dautres-modeles-asynchrones)
3. [Comment créer une Promise](#heading-comment-creer-une-promise)
4. [Comment obtenir le résultat d'une Promise](#heading-comment-obtenir-le-resultat-dune-promise)
5. [Comment gérer les erreurs avec `then`](#heading-comment-gerer-les-erreurs-avec-then)
6. [Chaînage de Promises](#heading-chainage-de-promises)
7. [Comment créer des Promises immédiatement résolues ou rejetées](#heading-comment-creer-des-promises-immediatement-resolues-ou-rejetees)
8. [Comment utiliser `async` et `await`](#heading-comment-utiliser-async-et-await)
9. [Anti-modèles de Promises](#heading-anti-modeles-de-promises)
10. [Résumé](#heading-resume)

## Qu'est-ce qu'une Promise ?

Commençons par examiner ce qu'est une Promise.

En termes simples, une Promise est un objet représentant une opération asynchrone. Cet objet peut vous indiquer quand l'opération réussit ou quand elle échoue.

Lorsque vous appelez une API basée sur des Promises, la fonction retourne un objet Promise qui fournira éventuellement le résultat de l'opération.

### États des Promises

Au cours de son existence, une Promise peut être dans l'un des trois états suivants :

* **En attente (Pending)** : Une Promise est en attente tant que l'opération est encore en cours. Elle est dans un état inactif, attendant le résultat éventuel (ou l'erreur).
* **Résolue (Fulfilled)** : La tâche asynchrone qui a retourné la Promise s'est terminée avec succès. Une Promise est résolue avec une valeur, qui est le résultat de l'opération.
* **Rejetée (Rejected)** : Si l'opération asynchrone a échoué, la Promise est dite rejetée. Une Promise est rejetée avec une _raison_. Il s'agit généralement d'un objet `Error`, mais une Promise peut être rejetée avec n'importe quelle valeur – même un simple nombre ou une chaîne de caractères !

Une Promise commence dans l'état en attente, puis, selon le résultat, passera soit à l'état résolue, soit à l'état rejetée. Une Promise est dite _réglée_ une fois qu'elle atteint l'état résolue ou rejetée.

Bien sûr, il n'y a aucune garantie que la tâche asynchrone se terminera un jour. Il est tout à fait possible qu'une `Promise` reste dans l'état en attente pour toujours, bien que cela serait dû à un bug dans le code de la tâche asynchrone.

## Comparaison des Promises avec d'autres modèles asynchrones

Les Promises se comportent un peu différemment des autres modèles asynchrones en JavaScript. Avant de plonger plus profondément dans les Promises, comparons brièvement les Promises avec ces autres techniques.

### Fonctions de rappel (Callback functions)

Une fonction de rappel est une fonction que vous passez à une autre fonction. Lorsque la fonction que vous appelez a terminé son travail, elle exécutera votre fonction de rappel avec le résultat.

Imaginez une fonction appelée `getUsers` qui effectuera une requête réseau pour obtenir un tableau d'utilisateurs. Vous pouvez passer une fonction de rappel à `getUsers`, qui sera appelée avec le tableau d'utilisateurs une fois la requête réseau terminée :

```javascript
console.log('Préparation pour obtenir les utilisateurs');
getUsers(users => {
  console.log('Utilisateurs obtenus :', users);
});
console.log('Requête utilisateurs envoyée');

```

Tout d'abord, le code ci-dessus imprimera "Préparation pour obtenir les utilisateurs". Ensuite, il appelle `getUsers` qui initiéra la requête réseau. Mais JavaScript n'attend pas que la requête se termine. Au lieu de cela, il exécute immédiatement l'instruction `console.log` suivante.

Plus tard, une fois les utilisateurs chargés, votre rappel sera exécuté et "Utilisateurs obtenus" sera imprimé.

Certaines API basées sur des rappels, comme de nombreuses API Node.js, utilisent des _rappels error-first_. Ces fonctions de rappel prennent deux arguments. Le premier argument est une erreur, et le second est le résultat.

Typiquement, seul l'un de ces arguments aura une valeur, selon le résultat de l'opération. Cela est similaire aux états résolus et rejetés des Promises.

Le problème avec les API basées sur des rappels est celui de l'imbrication. Si vous devez effectuer plusieurs appels asynchrones en séquence, vous terminerez avec des appels de fonctions et des rappels imbriqués.

Imaginez que vous voulez lire un fichier, traiter certaines données de ce fichier, puis écrire un nouveau fichier. Ces trois tâches sont asynchrones et utilisent une API imaginaire basée sur des rappels.

```javascript
readFile('sourceData.json', data => {
	processData(data, result => {
		writeFile(result, 'processedData.json', () => {
			console.log('Traitement terminé');
		});
	});
});

```

Cela devient encore plus encombrant avec la gestion des erreurs. Imaginez que ces fonctions utilisent des rappels error-first :

```javascript
readFile('sourceData.json', (error, data) => {
	if (error) {
		console.error('Erreur de lecture du fichier :', error);
		return;
	}
	
	processData(data, (error, result) => {
		if (error) {
			console.error('Erreur de traitement des données :', error);
			return;
		}
		
		writeFile(result, 'processedData.json', error => {
			if (error) {
				console.error('Erreur d'écriture du fichier :', error);
				return;
			}
			
			console.log('Traitement terminé');
		});
	});
});

```

Les fonctions de rappel ne sont généralement pas utilisées directement comme mécanisme asynchrone dans les API modernes, mais comme vous le verrez bientôt, elles sont la base d'autres types d'outils asynchrones tels que les Promises.

### Événements

Un événement est quelque chose que vous pouvez écouter et auquel vous pouvez répondre. Certains objets en JavaScript sont des _émetteurs d'événements_, ce qui signifie que vous pouvez enregistrer des écouteurs d'événements sur eux.

Dans le DOM, de nombreux éléments implémentent l'interface `EventTarget` qui fournit les méthodes `addEventListener` et `removeEventListener`.

Un type d'événement donné peut se produire plus d'une fois. Par exemple, vous pouvez écouter l'événement de clic sur un bouton :

```javascript
myButton.addEventListener('click', () => {
   console.log('le bouton a été cliqué !'); 
});
```

Chaque fois que le bouton est cliqué, le texte "le bouton a été cliqué !" sera imprimé dans la console.

`addEventListener` lui-même accepte une fonction de rappel. Chaque fois que l'événement se produit, le rappel est exécuté.

Un objet peut émettre plusieurs types d'événements. Prenons un objet image. Si l'image à l'URL spécifiée est chargée avec succès, l'événement `load` est déclenché. Si une erreur s'est produite, cet événement n'est pas déclenché et l'événement `error` est déclenché à la place.

```javascript
myImage.addEventListener('load', () => {
    console.log('Image chargée');
});

myImage.addEventListener('error', error => {
   console.error('Échec du chargement de l'image :', error); 
});
```

Supposons que l'image ait déjà terminé son chargement avant que vous n'ajoutiez l'écouteur d'événement. Que pensez-vous qu'il se passerait ? Rien ! Un inconvénient des API basées sur des événements est que si vous ajoutez un écouteur d'événement après un événement, votre rappel ne sera pas exécuté. Cela a du sens, après tout – vous ne voudriez pas recevoir tous les événements de clic passés lorsque vous ajoutez un écouteur de clic à un bouton.

Maintenant que nous avons exploré les rappels et les événements, examinons de plus près les Promises.

## Comment créer une Promise

Vous pouvez créer une Promise en utilisant le mot-clé `new` avec le constructeur `Promise`. Le constructeur `Promise` prend une fonction de rappel qui prend deux arguments, appelés `resolve` et `reject`. Chacun de ces arguments est une fonction fournie par la Promise, qui sont utilisées pour faire passer la Promise à l'état résolue ou rejetée.

À l'intérieur de votre rappel, vous effectuez votre travail asynchrone. Si la tâche réussit, vous appelez la fonction `resolve` avec le résultat final. Si une erreur s'est produite, vous appelez la fonction `reject` avec l'erreur.

Voici un exemple de création d'une Promise qui enveloppe la fonction `setTimeout` du navigateur :

```javascript
function wait(duration) {
	return new Promise(resolve => {
        setTimeout(resolve, duration);
    });
}
```

La fonction `resolve` est passée comme premier argument à `setTimeout`. Après que le temps spécifié par `duration` se soit écoulé, le navigateur appelle la fonction `resolve` qui résout la Promise.

Remarque : Dans cet exemple, le délai avant que la fonction `resolve` soit appelée peut être plus long que la durée passée à la fonction. Cela est dû au fait que `setTimeout` ne garantit pas l'exécution à l'heure spécifiée.

Il est important de noter que souvent, vous n'aurez pas besoin de construire votre propre Promise manuellement. Vous travaillerez généralement avec des Promises retournées par d'autres API.

## Comment obtenir le résultat d'une Promise

Nous avons vu comment créer une Promise, mais comment obtenez-vous réellement le résultat de l'opération asynchrone ? Pour ce faire, vous appelez `then` sur l'objet Promise lui-même. `then` prend une fonction de rappel comme argument. Lorsque la Promise est résolue, le rappel est exécuté avec le résultat.

Voyons un exemple de cela en action. Imaginez une fonction appelée `getUsers` qui charge de manière asynchrone une liste d'objets utilisateur et retourne une Promise. Vous pouvez obtenir la liste des utilisateurs en appelant `then` sur la Promise retournée par `getUsers`.

```javascript
getUsers()
  .then(users => {
    console.log('Utilisateurs obtenus :', users);
  });
```

Tout comme avec les événements ou les API basées sur des rappels, votre code continuera à s'exécuter sans attendre le résultat. Plus tard, lorsque les utilisateurs auront été chargés, votre rappel sera planifié pour exécution.

```javascript
console.log('Chargement des utilisateurs');
getUsers()
  .then(users => {
    console.log('Utilisateurs obtenus :', users);
  });
console.log('Continuation');
```

Dans l'exemple ci-dessus, "Chargement des utilisateurs" sera imprimé en premier. La prochaine chose qui sera imprimée sera "Continuation", car l'appel à `getUsers` est toujours en train de charger les utilisateurs. Plus tard, vous verrez "Utilisateurs obtenus" imprimé.

## Comment gérer les erreurs avec `then`

Nous avons vu comment utiliser `then` pour obtenir le résultat fourni à la Promise, mais qu'en est-il des erreurs ? Que se passe-t-il si nous échouons à charger la liste des utilisateurs ?

La fonction `then` prend en réalité un deuxième argument, un autre rappel. Il s'agit du gestionnaire d'erreurs. Si la Promise est rejetée, ce rappel est exécuté avec la valeur de rejet.

```javascript
getUsers()
  .then(users => {
    console.log('Utilisateurs obtenus :', users);
  }, error => {
    console.error('Échec du chargement des utilisateurs :', error);  
  });
```

Puisqu'une Promise ne peut être soit résolue, soit rejetée, mais pas les deux, seule l'une de ces fonctions de rappel sera exécutée.

Il est important de toujours gérer les erreurs lors de l'utilisation de Promises. Si vous avez un rejet de Promise qui n'est pas géré par un rappel d'erreur, vous obtiendrez une exception dans votre console concernant un rejet non géré, ce qui peut causer des problèmes pour vos utilisateurs à l'exécution.

## Chaînage de Promises

Que faire si vous devez travailler avec plusieurs Promises en série ? Considérez l'exemple précédent où nous avons chargé des données à partir d'un fichier, effectué un traitement, et écrit le résultat dans un nouveau fichier. Supposons que les fonctions `readFile`, `processData`, et `writeFile` utilisent des Promises au lieu de rappels.

Vous pourriez essayer quelque chose comme ceci :

```javascript
readFile('sourceData.json')
  .then(data => {
    processData(data)
      .then(result => {
        writeFile(result, 'processedData.json')
          .then(() => {
            console.log('Traitement terminé');
          });
      });
  });
```

Cela ne semble pas idéal, et nous avons toujours le problème d'imbrication que nous avions avec l'approche basée sur les rappels. Heureusement, il existe une meilleure façon. Vous pouvez chaîner les Promises ensemble dans une séquence plate.

Pour voir comment cela fonctionne, examinons plus en détail le fonctionnement de `then`. L'idée clé est la suivante : la méthode `then` retourne _une autre Promise_. Quelle que soit la valeur que vous retournez de votre rappel `then` devient la valeur résolue de cette nouvelle Promise.

Considérez une fonction `getUsers` qui retourne une Promise qui est résolue avec un tableau d'objets utilisateur. Supposons que nous appelons `then` sur cette Promise, et dans le rappel, nous retournons le premier utilisateur du tableau (`users[0]`) :

```javascript
getUsers().then(users => users[0]);
```

Cette expression entière, alors, résulte en une nouvelle Promise qui sera résolue avec le premier objet utilisateur !

```javascript
getUsers()
  .then(users => users[0])
  .then(firstUser => {
    console.log('Premier utilisateur :', firstUser.username);
  });
```

Ce processus de retour d'une Promise, d'appel de `then`, et de retour d'une autre valeur, résultant en une autre Promise, est appelé chaînage.

Étendons cette idée. Que se passe-t-il si, au lieu de retourner une valeur du gestionnaire `then`, nous retournions une autre Promise ? Considérez à nouveau l'exemple de traitement de fichier, où `readFile` et `processData` sont toutes deux des fonctions asynchrones qui retournent des Promises :

```javascript
readFile('sourceData.json')
  .then(data => processData(data));
```

Le gestionnaire `then` appelle `processData`, retournant la Promise résultante. Comme avant, cela retourne une nouvelle Promise. Dans ce cas, la nouvelle Promise sera résolue lorsque la Promise retournée par `processData` sera résolue, vous donnant la même valeur. Ainsi, le code dans l'exemple ci-dessus retournerait une Promise qui sera résolue avec les données traitées.

Vous pouvez chaîner plusieurs Promises, les unes après les autres, jusqu'à obtenir la valeur finale dont vous avez besoin :

```javascript
readFile('sourceData.json')
  .then(data => processData(data))
  .then(result => writeFile(result, 'processedData.json'))
  .then(() => console.log('Traitement terminé'));
```

Dans l'exemple ci-dessus, l'expression entière résultera en une Promise qui ne sera pas résolue avant que les données traitées ne soient écrites dans un fichier. "Traitement terminé !" sera imprimé dans la console, puis la Promise finale sera résolue.

### Gestion des erreurs dans les chaînes de Promises

Dans notre exemple de traitement de fichier, une erreur peut survenir à n'importe quelle étape du processus. Vous pouvez gérer une erreur de n'importe quelle étape de la chaîne de Promises en utilisant la méthode `catch` de la Promise.

```javascript
readFile('sourceData.json')
  .then(data => processData(data))
  .then(result => writeFile(result, 'processedData.json'))
  .then(() => console.log('Traitement terminé'))
  .catch(error => console.log('Erreur lors du traitement :', error));
```

Si l'une des Promises de la chaîne est rejetée, la fonction de rappel passée à `catch` sera exécutée et le reste de la chaîne est ignoré.

### Comment utiliser `finally`

Vous pourriez avoir du code que vous voulez exécuter indépendamment du résultat de la Promise. Par exemple, peut-être voulez-vous fermer une base de données ou un fichier.

```javascript
openDatabase()
  .then(data => processData(data))
  .catch(error => console.error('Erreur'))
  .finally(() => closeDatabase());
```

### Comment utiliser `Promise.all`

Les chaînes de Promises vous permettent d'exécuter plusieurs tâches en séquence, mais que faire si vous voulez exécuter plusieurs tâches en même temps et attendre qu'elles se terminent toutes ? La méthode `Promise.all` vous permet de faire exactement cela.

`Promise.all` prend un tableau de Promises et retourne une nouvelle Promise. Cette Promise sera résolue une fois que toutes les autres Promises seront résolues. La valeur de résolution est un tableau contenant les valeurs de résolution de chaque Promise dans le tableau d'entrée.

Supposons que vous avez une fonction `loadUserProfile` qui charge les données de profil d'un utilisateur, et une autre fonction `loadUserPosts` qui charge les publications d'un utilisateur. Elles prennent toutes deux un identifiant d'utilisateur comme argument. Il y a une troisième fonction, `renderUserPage`, qui a besoin à la fois du profil et de la liste des publications.

```javascript
const userId = 100;

const profilePromise = loadUserProfile(userId);
const postsPromise = loadUserPosts(userId);

Promise.all([profilePromise, postsPromise])
  .then(results => {
    const [profile, posts] = results;
    renderUserPage(profile, posts);
  });
```

Et les erreurs ? Si l'une des Promises passées à `Promise.all` est rejetée avec une erreur, la Promise résultante est également rejetée avec cette erreur. Si l'une des autres Promises est résolue, ces valeurs sont perdues.

### Comment utiliser `Promise.allSettled`

La méthode `Promise.allSettled` fonctionne de manière similaire à `Promise.all`. La principale différence est que la Promise retournée par `Promise.allSettled` ne sera jamais rejetée.

Au lieu de cela, elle est résolue avec un tableau d'objets, dont l'ordre correspond à l'ordre des Promises dans le tableau d'entrée. Chaque objet a une propriété `status` qui est soit "fulfilled", soit "rejected", selon le résultat.

Si `status` est "fulfilled", l'objet aura également une propriété `value` indiquant la valeur de résolution de la Promise. Si `status` est "rejected", l'objet aura plutôt une propriété `reason` qui est l'erreur ou un autre objet avec lequel la Promise a été rejetée.

Considérez à nouveau une fonction `getUser` qui prend un identifiant d'utilisateur et retourne une Promise qui est résolue avec l'utilisateur ayant cet identifiant. Vous pouvez utiliser `Promise.allSettled` pour les charger en parallèle, en vous assurant d'obtenir tous les utilisateurs qui ont été chargés avec succès.

```javascript
Promise.allSettled([
  getUser(1),
  getUser(2),
  getUser(3)
]).then(results => {
   const users = results
     .filter(result => result.status === 'fulfilled')
     .map(result => result.value);
   console.log('Utilisateurs obtenus :', users);
});
```

Vous pouvez créer une fonction `loadUsers` à usage général qui charge les utilisateurs, en parallèle, étant donné un tableau d'identifiants d'utilisateurs. La fonction retourne une Promise qui est résolue avec un tableau de tous les utilisateurs qui ont été chargés avec succès.

```javascript
function getUsers(userIds) {
  return Promise.allSettled(userIds.map(id => getUser(id)))
    .then(results => {
      return results
        .filter(result => result.status === 'fulfilled')
        .map(result => result.value);
    });
}
```

Ensuite, vous pouvez simplement appeler `getUsers` avec un tableau d'identifiants d'utilisateurs :

```javascript
getUsers([1, 2, 3])
	.then(users => console.log('Utilisateurs obtenus :', users));
```

## Comment créer des Promises immédiatement résolues ou rejetées

Parfois, vous pouvez vouloir envelopper une valeur dans une Promise résolue. Par exemple, peut-être avez-vous une fonction asynchrone qui retourne une Promise, mais il y a un cas de base où vous connaissez la valeur à l'avance et vous n'avez pas besoin de faire de travail asynchrone.

Pour ce faire, vous pouvez appeler `Promise.resolve` avec une valeur. Cela retourne une Promise qui est immédiatement résolue avec la valeur que vous avez spécifiée :

```javascript
Promise.resolve('bonjour')
  .then(result => {
    console.log(result); // imprime "bonjour"
  });
```

Cela est plus ou moins équivalent à ce qui suit :

```javascript
new Promise(resolve => {
   resolve('bonjour'); 
}).then(result => {
    console.log(result); // imprime aussi "bonjour"
});
```

Pour rendre votre API plus cohérente, vous pouvez créer une Promise immédiatement résolue et la retourner dans de tels cas. Ainsi, le code qui appelle votre fonction sait toujours s'attendre à une Promise, peu importe quoi.

Par exemple, considérons la fonction `getUsers` définie précédemment. Si le tableau des identifiants d'utilisateurs est vide, vous pourriez simplement retourner un tableau vide car aucun utilisateur ne sera chargé.

```javascript
function getUsers(userIds) {
  // retourner immédiatement le tableau vide
  if (userIds.length === 0) {
    return Promise.resolve([]);
  }
    
  return Promise.allSettled(userIds.map(id => getUser(id)))
    .then(results => {
      return results
        .filter(result => result.status === 'fulfilled')
        .map(result => result.value);
    });
}
```

Une autre utilisation de `Promise.resolve` est de gérer le cas où vous recevez une valeur qui peut être ou non une Promise, mais vous voulez toujours la traiter comme une Promise.

Vous pouvez appeler en toute sécurité `Promise.resolve` sur n'importe quelle valeur. Si c'était déjà une Promise, vous obtiendrez simplement une autre Promise qui aura la même valeur de résolution ou de rejet. Si ce n'était pas une Promise, elle sera enveloppée dans une Promise immédiatement résolue.

L'avantage de cette approche est que vous n'avez pas à faire quelque chose comme ceci :

```javascript
function getResult(result) {
  if (result.then) {
     result.then(value => {
         console.log('Résultat :', value);
     });
  } else {
      console.log('Résultat :', result);
  }
}
```

De même, vous pouvez créer une Promise immédiatement rejetée avec `Promise.reject`. Revenant une fois de plus à la fonction `getUsers`, peut-être voulons-nous rejeter immédiatement si le tableau d'identifiants d'utilisateurs est `null`, `undefined`, ou n'est pas un tableau.

```javascript
function getUsers(userIds) {
  if (userIds == null || !Array.isArray(userIds)) {
    return Promise.reject(new Error('Les identifiants d\'utilisateurs doivent être un tableau'));
  }
    
  // retourner immédiatement le tableau vide
  if (userIds.length === 0) {
    return Promise.resolve([]);
  }
    
  return Promise.allSettled(userIds.map(id => getUser(id)))
    .then(results => {
      return results
        .filter(result => result.status === 'fulfilled')
        .map(result => result.value);
    });
}
```

### Comment utiliser `Promise.race`

Tout comme `Promise.all` ou `Promise.allSettled`, la méthode statique `Promise.race` prend un tableau de Promises et retourne une nouvelle Promise. Comme le nom l'indique, cependant, elle fonctionne quelque peu différemment.

La Promise retournée par `Promise.race` attendra jusqu'à ce que la première des Promises données soit résolue ou rejetée, puis cette Promise sera également résolue ou rejetée, avec la même valeur. Lorsque cela se produit, les valeurs résolues ou rejetées des autres Promises sont perdues.

### Comment utiliser `Promise.any`

`Promise.any` fonctionne de manière similaire à `Promise.race` avec une différence clé – là où `Promise.race` sera terminé dès qu'une Promise est résolue ou rejetée, `Promise.any` attend la première Promise _résolue_.

## Comment utiliser `async` et `await`

`async` et `await` sont des mots-clés spéciaux qui simplifient le travail avec les Promises. Ils éliminent le besoin de fonctions de rappel et d'appels à `then` ou `catch`. Ils fonctionnent également avec des blocs try-catch.

Voici comment cela fonctionne. Au lieu d'appeler `then` sur une Promise, vous l'`await` en plaçant le mot-clé `await` devant. Cela "met en pause" effectivement l'exécution de la fonction jusqu'à ce que la Promise soit résolue.

Voici un exemple utilisant des Promises standard :

```javascript
getUsers().then(users => {
    console.log('Utilisateurs obtenus :', users);
});
```

Voici le code équivalent utilisant le mot-clé `await` :

```javascript
const users = await getUsers();
console.log('Utilisateurs obtenus :', users);
```

Les chaînes de Promises sont également un peu plus propres :

```javascript
const data = await readFile('sourceData.json');
const result = await processData(data);
await writeFile(result, 'processedData.json');

```

Rappelez-vous que chaque utilisation de `await` mettra en pause l'exécution du reste de la fonction jusqu'à ce que la Promise que vous attendez soit résolue. Si vous voulez attendre plusieurs Promises qui s'exécutent en parallèle, vous pouvez utiliser `Promise.all` :

```javascript
const users = await Promise.all([getUser(1), getUser(2), getUser(3)]);
```

Pour utiliser le mot-clé `await`, votre fonction doit être marquée comme une fonction asynchrone. Vous pouvez faire cela en plaçant le mot-clé `async` avant votre fonction :

```javascript
async function processData(sourceFile, outputFile) {
  const data = await readFile(sourceFile);
  const result = await processData(data);
  writeFile(result, outputFile);
}
```

Ajouter le mot-clé `async` a également un autre effet important sur la fonction. Les fonctions asynchrones retournent toujours implicitement une Promise. Si vous retournez une valeur depuis une fonction asynchrone, la fonction retournera en réalité une Promise qui est résolue avec cette valeur.

```javascript
async function add(a, b) {
  return a + b;   
}

add(2, 3).then(sum => {
   console.log('La somme est :', sum); 
});
```

Dans l'exemple ci-dessus, la fonction retourne la somme des deux arguments `a` et `b`. Mais comme il s'agit d'une fonction `async`, elle ne retourne pas la somme mais plutôt une Promise qui est résolue avec la somme.

### Gestion des erreurs avec `async` et `await`

Nous utilisons `await` pour attendre qu'une Promise soit résolue, mais qu'en est-il de la gestion des erreurs ? Si vous attendez une Promise et qu'elle est rejetée, une erreur sera levée. Cela signifie que pour gérer l'erreur, vous pouvez la placer dans un bloc try-catch :

```javascript
try {
    const data = await readFile(sourceFile);
    const result = await processData(data);
    await writeFile(result, outputFile);
} catch (error) {
    console.error('Erreur survenue lors du traitement :', error);
}
```

## Anti-modèles de Promises

### Création inutile d'une nouvelle Promise

Parfois, il n'y a pas moyen d'éviter de créer une nouvelle Promise. Mais si vous travaillez déjà avec des Promises retournées par une API, vous n'aurez généralement pas besoin de créer votre propre Promise :

```javascript
function getUsers() {
  return new Promise(resolve => {
     fetch('https://example.com/api/users')
       .then(result => result.json())
       .then(data => resolve(data))
  });
}
```

Dans cet exemple, nous créons une nouvelle Promise pour envelopper l'API Fetch, qui retourne déjà des Promises. Cela est inutile. Au lieu de cela, retournez simplement la chaîne de Promises de l'API Fetch directement :

```javascript
function getUsers() {
  return fetch('https://example.com/api/users')
    .then(result => result.json());
}
```

Dans les deux cas, le code appelant `getUsers` est le même :

```javascript
getUsers()
  .then(users => console.log('Utilisateurs obtenus :', users))
  .catch(error => console.error('Erreur lors de la récupération des utilisateurs :', error));
   
```

### Avaler les erreurs

Considérez cette version d'une fonction `getUsers` :

```javascript
function getUsers() {
    return fetch('https://example.com/api/users')
    	.then(result => result.json())
    	.catch(error => console.error('Erreur lors du chargement des utilisateurs :', error));
}
```

La gestion des erreurs est bonne, n'est-ce pas ? Vous pourriez être surpris par le résultat si nous appelons cette fonction `getUsers` :

```javascript
getUsers()
  .then(users => console.log('Utilisateurs obtenus :', users))
  .catch(error => console.error('erreur :', error);)
```

Vous pourriez vous attendre à ce que cela imprime "erreur", mais il imprimera en réalité "Utilisateurs obtenus : undefined". Cela est dû au fait que l'appel à `catch` "avale" l'erreur et retourne une nouvelle Promise qui est résolue avec la valeur de retour du rappel `catch`, qui est `undefined` (`console.error` retourne `undefined`). Vous verrez toujours le message de journalisation "Erreur lors du chargement des utilisateurs" de `getUsers`, mais la Promise retournée sera résolue, et non rejetée.

Si vous voulez attraper l'erreur à l'intérieur de la fonction `getUsers` et toujours rejeter la Promise retournée, le gestionnaire `catch` doit retourner une Promise rejetée. Vous pouvez faire cela en utilisant `Promise.reject`.

```javascript
function getUsers() {
  return fetch('https://example.com/api/users')
    .then(result => result.json())
    .catch(error => {
      console.error('Erreur lors du chargement des utilisateurs :', error);
      return Promise.reject(error);
    });
}
```

Maintenant, vous obtiendrez toujours le message "Erreur lors du chargement des utilisateurs", mais la Promise retournée sera également rejetée avec l'erreur.

### Imbrication des Promises

Évitez d'imbriquer le code des Promises. Au lieu de cela, essayez d'utiliser des chaînes de Promises aplaties.

Au lieu de ceci :

```javascript
readFile(sourceFile)
  .then(data => {
    processData(data)
      .then(result => {
        writeFile(result, outputFile)
          .then(() => console.log('terminé');
      });
  });
```

Faites ceci :

```javascript
readFile(sourceFile)
  .then(data => processData(data))
  .then(result => writeFile(result, outputFile))
  .then(() => console.log('terminé'));
```

## Résumé

Voici les points clés pour travailler avec les Promises :

* Une Promise peut être en attente, résolue ou rejetée
* Une Promise est réglée si elle est soit résolue, soit rejetée
* Utilisez `then` pour obtenir la valeur résolue d'une Promise
* Utilisez `catch` pour gérer les erreurs
* Utilisez `finally` pour effectuer une logique de nettoyage dont vous avez besoin dans le cas de succès ou d'erreur
* Chaînez les Promises ensemble pour effectuer des tâches asynchrones en séquence
* Utilisez `Promise.all` pour obtenir une Promise qui est résolue lorsque toutes les Promises données sont résolues, ou qui est rejetée lorsque l'une de ces Promises est rejetée
* Utilisez `Promise.allSettled` pour obtenir une Promise qui est résolue lorsque toutes les Promises données sont soit résolues, soit rejetées
* Utilisez `Promise.race` pour obtenir une Promise qui est résolue ou rejetée lorsque la première des Promises données est soit résolue, soit rejetée
* Utilisez `Promise.any` pour obtenir une Promise qui est résolue lorsque la première des Promises données est résolue
* Utilisez le mot-clé `await` pour attendre la valeur de résolution d'une Promise
* Utilisez un bloc try-catch pour gérer les erreurs lors de l'utilisation du mot-clé `await`
* Une fonction qui utilise `await` à l'intérieur doit utiliser le mot-clé `async`

Merci d'avoir lu cette plongée en profondeur sur les Promises. J'espère que vous avez appris quelque chose de nouveau !