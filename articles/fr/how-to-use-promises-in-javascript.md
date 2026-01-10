---
title: JavaScript asynchrone – Comment utiliser les promesses dans votre code JS
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-12-11T21:52:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-promises-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Orange-and-white-modern-creative-marketing-plan-Presentation-.png
tags:
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: JavaScript asynchrone – Comment utiliser les promesses dans votre code
  JS
seo_desc: "JavaScript is a versatile programming language that powers the dynamic\
  \ behavior of websites. \nAs web applications become more sophisticated, the need\
  \ to handle asynchronous operations efficiently becomes crucial. Asynchronous JavaScript\
  \ allows you to..."
---

JavaScript est un langage de programmation polyvalent qui alimente le comportement dynamique des sites web.

À mesure que les applications web deviennent plus sophistiquées, la nécessité de gérer efficacement les opérations asynchrones devient cruciale. JavaScript asynchrone vous permet d'exécuter du code sans bloquer le thread principal, garantissant ainsi une expérience utilisateur plus fluide.

Les promesses sont un outil puissant en JavaScript pour gérer les opérations asynchrones, offrant une approche plus propre et plus organisée pour gérer le code asynchrone.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que JavaScript asynchrone ?](#heading-quest-ce-que-javascript-asynchrone)
2. [Le besoin de promesses](#heading-le-besoin-de-promesses)
3. [Qu'est-ce que l'enfer des callbacks ?](#heading-quest-ce-que-lenfer-des-callbacks)
4. [Comment créer une promesse](#heading-comment-creer-une-promesse)
5. [Comment consommer les promesses avec `.then()` et `.catch()`](#heading-comment-consommer-les-promesses-avec-then-et-catch)
6. [Comment enchaîner les promesses avec `.then()`](#heading-comment-enchainer-les-promesses-avec-then)
7. [Exemples plus complexes d'enchaînement de promesses](#heading-exemples-plus-complexes-denchainement-de-promesses)
8. [Comment gérer les erreurs avec `.catch()`](#heading-comment-gerer-les-erreurs-avec-catch)
9. [Gestion des erreurs en détail](#heading-gestion-des-erreurs-en-detail)
10. [Async/await en JavaScript](#heading-asyncawait-en-javascript)
11. [Méthodes alternatives de programmation asynchrone](#heading-methodes-alternatives-de-programmation-asynchrone)
12. [Conclusion](#heading-conclusion)

## Qu'est-ce que JavaScript asynchrone ?

JavaScript est mono-thread, ce qui signifie qu'il ne peut exécuter qu'une seule opération à la fois. Cependant, dans le développement web, il existe des tâches qui prennent du temps à s'achever, comme la récupération de données depuis une API, la lecture d'un fichier ou l'attente d'une entrée utilisateur. Si ces tâches étaient exécutées de manière synchrone, elles bloqueraient le thread principal, rendant l'interface utilisateur non réactive.

JavaScript asynchrone vous permet d'exécuter du code sans attendre la fin des tâches chronophages. Au lieu de bloquer le thread principal, ces tâches sont déléguées aux processus d'arrière-plan du navigateur, et une fois terminées, une fonction de rappel est déclenchée pour gérer le résultat.

## Le besoin de promesses

Avant les promesses, les développeurs utilisaient des callbacks pour gérer les opérations asynchrones. Les callbacks sont des fonctions passées en arguments à d'autres fonctions, et elles sont exécutées une fois l'opération asynchrone terminée.

Bien que les callbacks servent leur but, ils mènent souvent à un phénomène connu sous le nom d'"enfer des callbacks" – une situation où plusieurs callbacks imbriqués rendent le code difficile à lire et à maintenir.

L'enfer des callbacks apparaît lorsque des opérations asynchrones dépendent des résultats d'autres opérations asynchrones, créant des fonctions de rappel profondément imbriquées. Cela peut rendre le code difficile à suivre, à déboguer et à maintenir.

Les promesses ont été introduites pour résoudre ce problème et offrir une solution plus élégante au code asynchrone.

## Qu'est-ce que l'enfer des callbacks ?

L'enfer des callbacks, également connu sous le nom de "pyramide de la mort", se produit lorsque vous avez plusieurs callbacks imbriqués dans votre code. Chaque niveau d'imbrication représente une opération asynchrone ultérieure qui dépend du résultat de la précédente. Voici un exemple simplifié :

```javascript
getData(function (data) {
  processData(data, function (processedData) {
    updateUI(processedData, function () {
      // Plus de callbacks imbriqués...
    });
  });
});

```

Comme vous pouvez le voir, à mesure que le nombre d'opérations asynchrones augmente, l'indentation du code s'approfondit, conduisant à un code moins lisible et maintenable.

Les promesses offrent un moyen de mitiger l'enfer des callbacks en proposant une approche plus propre et plus structurée pour gérer le code asynchrone.

## Comment créer une promesse

Plongeons dans les bases de la création d'une promesse. Le constructeur `Promise` prend une fonction comme argument, qui a deux paramètres : `resolve` et `reject`. Ces paramètres sont des fonctions que vous appelez pour indiquer l'achèvement ou l'échec de l'opération asynchrone.

```javascript
// Création d'une promesse qui se résout avec succès
const successPromise = new Promise((resolve, reject) => {
  // Simulation d'une opération asynchrone réussie
  const success = true;

  if (success) {
    resolve("Opération terminée avec succès");
  } else {
    reject("Opération échouée");
  }
});

// Création d'une promesse qui se résout avec une erreur
const errorPromise = new Promise((resolve, reject) => {
  // Simulation d'une opération asynchrone échouée
  const success = false;

  if (success) {
    resolve("Opération terminée avec succès");
  } else {
    reject("Opération échouée");
  }
});

```

Dans `successPromise`, l'opération asynchrone est simulée pour être réussie, et `resolve` est appelé avec le message de succès. Dans `errorPromise`, l'opération est simulée pour échouer, et `reject` est appelé avec le message d'erreur.

## Comment consommer les promesses avec `.then()` et `.catch()`

Une fois une promesse créée, vous pouvez consommer son résultat en utilisant les méthodes `.then()` et `.catch()`. La méthode `.then()` est utilisée lorsque la promesse est remplie, et la méthode `.catch()` est utilisée lorsque la promesse est rejetée.

```javascript
// Consommation de la successPromise
successPromise
  .then((result) => {
    console.log(result); // Sortie : Opération terminée avec succès
  })
  .catch((error) => {
    console.error(error); // Cela ne sera pas exécuté
  });

// Consommation de la errorPromise
errorPromise
  .then((result) => {
    console.log(result); // Cela ne sera pas exécuté
  })
  .catch((error) => {
    console.error(error); // Sortie : Opération échouée
  });

```

Dans l'exemple ci-dessus, la méthode `.then()` journalise le message de succès pour `successPromise` et le message d'erreur pour `errorPromise`. La méthode `.catch()` gère les erreurs pour les deux promesses.

## Comment enchaîner les promesses avec `.then()`

L'une des fonctionnalités puissantes des promesses est la capacité de les enchaîner ensemble en utilisant la méthode `.then()`. Cela est particulièrement utile lorsque vous avez plusieurs opérations asynchrones qui dépendent les unes des autres.

```javascript
const firstPromise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("Première opération terminée");
  }, 1000);
});

const secondPromise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("Deuxième opération terminée");
  }, 500);
});

const thirdPromise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("Troisième opération terminée");
  }, 800);
});

firstPromise
  .then((result) => {
    console.log(result); // Sortie : Première opération terminée
    return secondPromise;
  })
  .then((result) => {
    console.log(result); // Sortie : Deuxième opération terminée
    return thirdPromise;
  })
  .then((result) => {
    console.log(result); // Sortie : Troisième opération terminée
  });

```

Dans cet exemple, les deuxième et troisième promesses sont enchaînées à la première en utilisant l'instruction `return` à l'intérieur des callbacks `.then()`. Cela garantit que chaque promesse attend la fin de la précédente avant de s'exécuter.

## Exemples plus complexes d'enchaînement de promesses

Explorons des exemples plus complexes d'enchaînement de promesses pour démontrer comment cela peut être appliqué dans des scénarios réels.

### Exemple 1 : Récupération des données utilisateur et des publications

```javascript
function fetchUserData(userId) {
  return new Promise((resolve, reject) => {
    // Simulation de la récupération des données utilisateur depuis une API
    setTimeout(() => {
      const userData = { id: userId, username: 'john_doe' };
      resolve(userData);
    }, 1000);
  });
}

function fetchUserPosts(userId) {
  return new Promise((resolve, reject) => {
    // Simulation de la récupération des publications utilisateur depuis une API
    setTimeout(() => {
      const posts = [
        { id: 1, title: 'Publication 1' },
        { id: 2, title: 'Publication 2' },
      ];
      resolve(posts);
    }, 800);
  });
}

// Enchaînement des promesses pour récupérer les données utilisateur et les publications de manière séquentielle
fetchUserData(123)
  .then((userData) => {
    console.log(userData); // Sortie : { id: 123, username: 'john_doe' }
    return fetchUserPosts(userData.id);
  })
  .then((userPosts) => {
    console.log(userPosts); // Sortie : [{ id: 1, title: 'Publication 1' }, { id: 2, title: 'Publication 2' }]
  })
  .catch((error) => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, deux opérations asynchrones (`fetchUserData` et `fetchUserPosts`) sont enchaînées pour récupérer les données utilisateur et les publications de manière séquentielle.

### Exemple 2 : Traitement des données avec plusieurs étapes

```javascript
function processData(data) {
  return new Promise((resolve, reject) => {
    // Simulation du traitement des données
    setTimeout(() => {
      const processedData = data.map((item) => item * 2);
      resolve(processedData);
    }, 500);
  });
}

function displayData(data) {
  return new Promise((resolve, reject) => {
    // Simulation de l'affichage des données
    setTimeout(() => {
      console.log(data); // Sortie : [2, 4, 6, 8, 10]
      resolve('Données affichées avec succès');
    }, 300);
  });
}

// Enchaînement des promesses pour traiter et afficher les données de manière séquentielle
const originalData = [1, 2, 3, 4, 5];
processData(originalData)
  .then((processedData) => {
    console.log(processedData); // Sortie : [2, 4, 6, 8, 10]
    return displayData(processedData);
  })
  .then((result) => {
    console.log(result); // Sortie : Données affichées avec succès
  })
  .catch((error) => {
    console.error('Erreur :', error);
  });

```

Dans cet exemple, deux opérations asynchrones (`processData` et `displayData`) sont enchaînées pour traiter et afficher les données de manière séquentielle.

## Comment gérer les erreurs avec `.catch()`

Lors de la manipulation d'opérations asynchrones, la gestion des erreurs est cruciale. Les promesses rendent la gestion des erreurs plus facile en fournissant la méthode `.catch()`, qui est utilisée pour capturer toute erreur survenant pendant la chaîne de promesses.

```javascript
const errorPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = false;

    if (success) {
      resolve("Opération terminée avec succès");
    } else {
      reject("Opération échouée");
    }
  }, 1000);
});

errorPromise
  .then((result) => {
    console.log(result); // Cela ne sera pas exécuté
  })
  .catch((error) => {
    console.error(error); // Sortie : Opération échouée
  });

```

Dans cet exemple, puisque la variable `success` est définie sur `false`, la promesse est rejetée, et la méthode `.catch()` est invoquée avec la raison de l'échec.

## Gestion des erreurs en détail

Bien que les exemples précédents aient abordé la gestion des erreurs, approfondissons les techniques de gestion des erreurs avec les promesses.

### Utilisation des blocs Try-Catch

Vous pouvez utiliser des blocs try-catch pour gérer les erreurs au sein des opérations asynchrones elles-mêmes.

```javascript
function fetchData() {
  return new Promise(async (resolve, reject) => {
    try {
      const response = await fetch('https://api.example.com/data');
      if (!response.ok) {
        throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
      }
      const data = await response.json();
      resolve(data);
    } catch (error) {
      reject(`Erreur lors de la récupération des données : ${error.message}`);
    }
  });
}

fetchData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });

```

Dans cet exemple, le bloc `try` tente de récupérer les données, vérifie si la réponse est correcte, puis procède à l'analyse en JSON. Si une erreur se produit dans le bloc `try`, le bloc `catch` est exécuté, et l'erreur est transmise à la fonction reject.

### Utilisation de la méthode `.catch()`

Vous pouvez également utiliser la méthode `.catch()` à la fin de la chaîne de promesses pour gérer les erreurs qui peuvent survenir à n'importe quelle étape.

```javascript
fetchData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });

```

Cette approche est particulièrement utile lorsque vous souhaitez gérer les erreurs globalement pour une séquence d'opérations asynchrones.

### Gestion des erreurs dans l'enchaînement de promesses

Lors de l'enchaînement de promesses, il est important de gérer les erreurs à chaque étape de la chaîne. Voici un exemple démontrant la gestion des erreurs dans une chaîne de promesses :

```javascript
function stepOne() {
  return new Promise((resolve, reject) => {
    // Simulation d'une opération asynchrone
    setTimeout(() => {
      const success = true;
      if (success) {
        resolve('Étape un terminée');
      } else {
        reject('Étape un échouée');
      }
    }, 500);
  });
}

function stepTwo(data) {
  return new Promise((resolve, reject) => {
    // Simulation d'une opération asynchrone
    setTimeout(() => {
      const success = false;
      if (success) {
        resolve(`Étape deux terminée avec les données : ${data}`);
      } else {
        reject('Étape deux échouée');
      }
    }, 300);
  });
}

function stepThree(result) {
  return new Promise((resolve) => {
    // Simulation d'une opération asynchrone
    setTimeout(() => {
      resolve(`Étape trois terminée avec le résultat : ${result}`);
    }, 200);
  });
}

stepOne()
  .then((data) => stepTwo(data))
  .then((result) => stepThree(result))
  .then((finalResult) => {
    console.log(finalResult); // Cela ne sera pas exécuté en cas de rejet dans la chaîne
  })
  .catch((error) => {
    console.error('Erreur dans la chaîne de promesses :', error);
  });

```

Dans cet exemple, si une étape de la chaîne rencontre une erreur (soit dans l'opération asynchrone, soit en raison de la logique conditionnelle), le bloc `catch` à la fin de la chaîne gérera l'erreur.

## Async/Await en JavaScript

Async/await est une syntaxe sucrée introduite dans ECMAScript 2017 (ES8) qui simplifie la gestion du code asynchrone. Elle fournit une structure plus lisible et plus synchrone, facilitant ainsi le travail des développeurs avec les opérations asynchrones.

### Comment cela fonctionne :

* Le mot-clé `async` est utilisé pour définir une fonction asynchrone. Cette fonction retourne toujours une promesse.
* Le mot-clé `await` est utilisé au sein de la fonction asynchrone pour suspendre son exécution jusqu'à ce que la promesse soit résolue. Il permet de travailler avec les promesses de manière plus synchrone.

**Exemple :**

```javascript
// Fonction asynchrone utilisant async/await
async function fetchData() {
  try {
    // Simulation d'une opération asynchrone, comme la récupération de données depuis une API
    let response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    
    // Une fois la promesse résolue, le code ci-dessous sera exécuté
    let data = await response.json();
    
    console.log('Données :', data);
  } catch (error) {
    console.error('Erreur :', error);
  }
}

// Appel de la fonction asynchrone
fetchData();

```

Que fait ce code ?

1. La fonction `fetchData` est déclarée comme `async`, indiquant qu'elle contient des opérations asynchrones.
2. À l'intérieur de la fonction, `await fetch(...)` est utilisé pour faire une requête asynchrone à une URL, et la fonction pause jusqu'à ce que la requête soit complète.
3. Après avoir reçu la réponse, `await response.json()` est utilisé pour extraire les données JSON de la réponse.
4. Le bloc `try` gère l'exécution réussie, et les données sont journalisées dans la console.
5. Si une erreur se produit pendant les opérations asynchrones, le bloc `catch` gère l'erreur.

Maintenant, discutons des avantages et des inconvénients de async/await.

### Avantages de async/await

#### 1. **Lisibilité et simplicité :**

La syntaxe async/await rend le code asynchrone similaire au code synchrone, améliorant la lisibilité et facilitant la compréhension des développeurs.

```javascript
// Utilisation des promesses
function fetchData() {
  return fetch('https://api.example.com/data')
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}

// Utilisation de Async/Await
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

```

#### 2. **Gestion des erreurs :**

Async/await simplifie la gestion des erreurs en permettant l'utilisation de blocs try-catch traditionnels, rendant la gestion des erreurs au sein des fonctions asynchrones plus intuitive.

```javascript
// Utilisation des promesses
function fetchData() {
  return fetch('https://api.example.com/data')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
      }
      return response.json();
    })
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}

// Utilisation de Async/Await
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) {
      throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

```

#### 3. **Exécution séquentielle :**

Async/await permet aux développeurs d'écrire du code asynchrone de manière plus séquentielle, ce qui peut être plus facile à raisonner et à déboguer.

```javascript
// Utilisation des promesses
function fetchDataSequentially() {
  fetchUserData()
    .then((userData) => fetchUserPosts(userData.id))
    .then((userPosts) => processPosts(userPosts))
    .then((result) => displayResult(result))
    .catch((error) => console.error(error));
}

// Utilisation de Async/Await
async function fetchDataSequentially() {
  try {
    const userData = await fetchUserData();
    const userPosts = await fetchUserPosts(userData.id);
    const result = await processPosts(userPosts);
    displayResult(result);
  } catch (error) {
    console.error(error);
  }
}

```

### Inconvénients de async/await

#### 1. **Pas de timeout intégré :**

Async/await n'a pas de support intégré pour définir un timeout sur les opérations asynchrones. Si vous devez implémenter un timeout, vous devrez peut-être utiliser une combinaison de `Promise.race()` et `setTimeout`.

```javascript
async function fetchDataWithTimeout() {
  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Timeout dépassé')), 5000);
  });

  try {
    const response = await Promise.race([fetch('https://api.example.com/data'), timeoutPromise]);
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

```

#### 2. **Exécution séquentielle vs. parallélisme :**

Bien que async/await facilite l'écriture de code séquentiel, il peut ne pas être idéal pour les scénarios où vous souhaitez une exécution parallèle de tâches asynchrones indépendantes. Dans de tels cas, les promesses et `Promise.all()` peuvent être plus adaptés.

```javascript
// Utilisation des promesses et de Promise.all()
function fetchAndProcessData() {
  const userDataPromise = fetchUserData();
  const userPostsPromise = fetchUserPosts();

  Promise.all([userDataPromise, userPostsPromise])
    .then(([userData, userPosts]) => processAndDisplayData(userData, userPosts))
    .catch((error) => console.error(error));
}

// Utilisation de Async/Await
async function fetchAndProcessData() {
  try {
    const userData = await fetchUserData();
    const userPosts = await fetchUserPosts();
    processAndDisplayData(userData, userPosts);
  } catch (error) {
    console.error(error);
  }
}

```

#### 3. **Potentiel de rejets de promesses non gérés :**

Async/await peut conduire à des rejets de promesses non gérés si utilisé sans précaution. Par exemple, oublier d'utiliser des blocs `try-catch` ou ne pas enchaîner `.catch()` à la fin d'une fonction asynchrone peut entraîner des rejets de promesses non gérés.

```javascript
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}

fetchData(); // Rejet de promesse non géré si fetch échoue

```

Pour atténuer cela, assurez-vous de mettre en place une gestion appropriée des erreurs dans toutes les fonctions async.

### Utilisation de la méthode `.catch()`

Vous pouvez également utiliser la méthode `.catch()` à la fin de la chaîne de promesses pour gérer les erreurs qui peuvent survenir à n'importe quelle étape.

```javascript
fetchData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });

```

Cette approche est particulièrement utile lorsque vous souhaitez gérer les erreurs globalement pour une séquence d'opérations asynchrones.

## Méthodes alternatives de programmation asynchrone

Bien que les promesses soient un outil populaire et puissant pour la programmation asynchrone, il est utile de mentionner d'autres méthodes que les développeurs pourraient rencontrer ou choisir d'utiliser.

### Syntaxe Async/Await

Comme nous en avons parlé dans la section précédente, async/await fournit une syntaxe sucrée par-dessus les promesses, rendant le code asynchrone plus synchrone et lisible.

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Erreur lors de la récupération des données :', error);
  }
}

fetchData();

```

Dans cet exemple, le mot-clé `async` est utilisé pour définir une fonction asynchrone, et le mot-clé `await` est utilisé pour attendre la résolution de l'opération `fetch` et la conversion `json` ultérieure.

### Web Workers

Les Web Workers sont une approche différente pour gérer la concurrence en JavaScript. Ils permettent d'exécuter des scripts en arrière-plan, séparément du thread principal, pour effectuer des tâches sans affecter la réactivité de l'interface utilisateur.

Bien que les Web Workers ne remplacent pas directement les promesses, ils offrent une alternative pour atteindre le parallélisme et gérer les tâches intensives en calcul de manière asynchrone.

```javascript
// À l'intérieur d'un script de web worker (worker.js)
self.addEventListener('message', (event) => {
  const data = event.data;
  const result = processData(data);
  self.postMessage(result);
});

// Dans le script principal
const worker = new Worker('worker.js');

worker.addEventListener('message', (event) => {
  const result = event.data;
  console.log(result);
});

const dataToSend = [1, 2, 3, 4, 5];
worker.postMessage(dataToSend);

```

Dans cet exemple, un script de Web Worker (`worker.js`) traite les données et envoie le résultat au script principal. Les Web Workers sont un outil puissant pour paralléliser les tâches et décharger le travail du thread principal.

## Conclusion

Les promesses offrent une manière propre et organisée de gérer le code asynchrone en JavaScript, abordant des problèmes tels que l'enfer des callbacks et fournissant une syntaxe plus lisible pour les opérations asynchrones.

En comprenant les bases des promesses, en les enchaînant, en gérant les erreurs et en explorant des concepts avancés, vous pouvez améliorer votre capacité à écrire du code JavaScript asynchrone efficace et maintenable.

Bien que les promesses soient largement adoptées, il est essentiel d'être conscient des approches alternatives comme async/await et les Web Workers, car elles peuvent mieux convenir à des cas d'utilisation spécifiques ou à des préférences.

À mesure que vous continuez à explorer et à appliquer différentes méthodes de programmation asynchrone, vous serez mieux équipé pour construire des applications web réactives et conviviales.