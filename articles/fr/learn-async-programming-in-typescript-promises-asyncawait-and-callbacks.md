---
title: 'Apprendre la programmation asynchrone en TypeScript : Promesses, Async/Await
  et Callbacks [Guide complet]'
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2025-01-31T15:33:02.721Z'
originalURL: https://freecodecamp.org/news/learn-async-programming-in-typescript-promises-asyncawait-and-callbacks
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737747600016/f6df015b-cc25-4c37-8c4e-bec9c8c49dc5.png
tags:
- name: TypeScript
  slug: typescript
- name: JavaScript
  slug: javascript
- name: asynchronous
  slug: asynchronous
seo_title: 'Apprendre la programmation asynchrone en TypeScript : Promesses, Async/Await
  et Callbacks [Guide complet]'
seo_desc: Async programming is a programming paradigm that allows you to write code
  that runs asynchronously. In contrast to synchronous programming, which executes
  code sequentially, async programming allows code to run in the background while
  the rest of the...
---

La programmation asynchrone est un paradigme de programmation qui permet d'écrire du code qui s'exécute de manière `asynchrone`. Contrairement à la programmation synchrone, qui exécute le code de manière séquentielle, la programmation asynchrone permet au code de s'exécuter en arrière-plan tandis que le reste du programme continue de s'exécuter. Cela est particulièrement utile pour les tâches qui peuvent prendre beaucoup de temps à se compléter, comme la récupération de données depuis une API distante.

La `programmation asynchrone` est essentielle pour créer des applications réactives et efficaces en JavaScript. TypeScript, un sur-ensemble de JavaScript, facilite encore davantage le travail avec la programmation asynchrone.

Il existe plusieurs approches pour la `programmation asynchrone` en TypeScript, notamment l'utilisation de `promesses`, `async/await` et `callbacks`. Nous allons couvrir chacune de ces approches en détail afin que vous puissiez choisir la ou les meilleures pour votre cas d'utilisation.

## Table des matières

1. [Pourquoi la programmation asynchrone est-elle importante ?](#heading-pourquoi-la-programmation-asynchrone-est-elle-importante)
    
2. [Comment TypeScript facilite la programmation asynchrone](#heading-comment-typescript-facilite-la-programmation-asynchrone)
    
3. [Comment utiliser les promesses en TypeScript](#heading-comment-utiliser-les-promesses-en-typescript)
    
    * [Comment créer une promesse](#heading-comment-creer-une-promesse)
        
    * [Comment chaîner les promesses](#heading-comment-chainer-les-promesses)
        
4. [Comment utiliser Async / Await en TypeScript](#heading-comment-utiliser-async-await-en-typescript)
    
5. [Comment utiliser les callbacks en TypeScript](#heading-comment-utiliser-les-callbacks-en-typescript)
    
6. [Conclusion](#heading-conclusion)
    

## Pourquoi la programmation asynchrone est-elle importante ?

La programmation asynchrone est cruciale pour construire des applications web réactives et efficaces. Elle permet aux tâches de s'exécuter en arrière-plan tandis que le reste du programme continue, gardant l'interface utilisateur réactive aux entrées. De plus, la programmation asynchrone peut améliorer les performances globales en permettant à plusieurs tâches de s'exécuter en même temps.

Il existe de nombreux exemples concrets de programmation asynchrone, tels que l'accès aux caméras et microphones des utilisateurs et la gestion des événements d'entrée utilisateur. Même si vous ne créez pas fréquemment des fonctions asynchrones, il est important de savoir comment les utiliser correctement pour vous assurer que votre application est fiable et performante.

### Comment TypeScript facilite la programmation asynchrone

TypeScript offre plusieurs fonctionnalités qui simplifient la programmation asynchrone, notamment la `sécurité des types`, l'`inférence de types`, la `vérification des types` et les `annotations de types`.

Avec la sécurité des types, vous pouvez vous assurer que votre code se comporte comme prévu, même lorsque vous traitez avec des fonctions asynchrones. Par exemple, TypeScript peut attraper les erreurs liées aux valeurs null et undefined au moment de la compilation, vous faisant gagner du temps et des efforts en débogage.

L'inférence et la vérification des types de TypeScript réduisent également la quantité de code boilerplate que vous devez écrire, rendant votre code plus concis et plus facile à lire.

Et les annotations de types de TypeScript fournissent de la clarté et de la documentation pour votre code, ce qui est particulièrement utile lorsque vous travaillez avec des fonctions asynchrones qui peuvent être complexes à comprendre.

Maintenant, plongeons dans l'apprentissage de ces trois fonctionnalités clés de la programmation asynchrone : les promesses, async/await et les callbacks.

## Comment utiliser les promesses en TypeScript

Les **promesses** sont un outil puissant pour gérer les opérations asynchrones en TypeScript. Par exemple, vous pourriez utiliser une promesse pour récupérer des données depuis une API externe ou pour effectuer une tâche chronophage en arrière-plan tandis que votre thread principal continue de s'exécuter.

Pour utiliser une promesse, vous créez une nouvelle instance de la classe `Promise` et lui passez une fonction qui effectue l'opération asynchrone. Cette fonction doit appeler la méthode resolve avec le résultat lorsque l'opération réussit ou la méthode reject avec une erreur si elle échoue.

Une fois la promesse créée, vous pouvez y attacher des callbacks en utilisant la méthode `then`. Ces callbacks seront déclenchés lorsque la promesse sera remplie, avec la valeur résolue passée en tant que paramètre. Si la promesse est rejetée, vous pouvez attacher un gestionnaire d'erreurs en utilisant la méthode catch, qui sera appelée avec la raison du rejet.

L'utilisation des promesses offre plusieurs avantages par rapport aux méthodes traditionnelles basées sur les callbacks. Par exemple, les promesses peuvent aider à prévenir le "callback hell", un problème courant dans le code asynchrone où les callbacks imbriqués deviennent difficiles à lire et à maintenir.

Les promesses facilitent également la gestion des erreurs dans le code asynchrone, car vous pouvez utiliser la méthode catch pour gérer les erreurs qui se produisent n'importe où dans la chaîne de promesses.

Enfin, les promesses peuvent simplifier votre code en fournissant une manière cohérente et composable de gérer les opérations asynchrones, indépendamment de leur implémentation sous-jacente.

### Comment créer une promesse

Syntaxe de la promesse :

```typescript
const myPromise = new Promise((resolve, reject) => {
  // Effectuer une opération asynchrone
  // Si l'opération réussit, appeler resolve avec le résultat
  // Si l'opération échoue, appeler reject avec un objet d'erreur
});

myPromise
  .then((result) => {
    // Gérer le résultat réussi
  })
  .catch((error) => {
    // Gérer l'erreur
  });
```

```typescript
// Exemple 1 sur la façon de créer une promesse

function myAsyncFunction(): Promise<string> {
  return new Promise<string>((resolve, reject) => {
    // Une opération asynchrone
    setTimeout(() => {
      // Opération réussie résout la promesse
      const success = true;

      if (success) {
        // Résoudre la promesse avec le résultat de l'opération si l'opération a réussi
        resolve(
          `Le résultat est un succès et votre résultat d'opération est ${operationResult}`
        );
      } else {
        const rejectCode: number = 404;
        const rejectMessage: string = `Le résultat est un échec et votre résultat d'opération est ${rejectCode}`;
        // Rejeter la promesse avec le résultat de l'opération si l'opération a échoué
        reject(new Error(rejectMessage));
      }
    }, 2000);
  });
}

// Utiliser la promesse
myAsyncFunction()
  .then((result) => {
    console.log(result); // sortie : Le résultat est un succès et votre résultat d'opération est 4
  })
  .catch((error) => {
    console.error(error); // sortie : Le résultat est un échec et votre résultat d'opération est 404
  });
```

Dans l'exemple ci-dessus, nous avons une fonction appelée `myAsyncFunction()` qui retourne une `promesse`. Nous utilisons le constructeur `Promise` pour créer la promesse, qui prend une `fonction de callback` avec les arguments `resolve` et `reject`. Si l'opération asynchrone réussit, nous appelons la fonction resolve. Si elle échoue, nous appelons la fonction reject.

L'objet promesse retourné par le constructeur a une méthode `then()`, qui prend des fonctions de callback de succès et d'échec. Si la promesse se résout avec succès, la fonction de callback de succès est appelée avec le résultat. Si la promesse est rejetée, la fonction de callback d'échec est appelée avec un message d'erreur.

L'objet promesse a également une méthode `catch()` utilisée pour gérer les erreurs qui se produisent pendant la chaîne de promesses. La méthode `catch()` prend une fonction de callback, qui est appelée si une erreur se produit dans la chaîne de promesses.

Maintenant, passons à la façon de chaîner les promesses en TypeScript.

### Comment chaîner les promesses

Le chaînage des promesses permet d'effectuer des `opérations asynchrones multiples` en séquence ou en parallèle. Cela est utile lorsque vous devez effectuer plusieurs tâches asynchrones les unes après les autres ou en même temps. Par exemple, vous pourriez avoir besoin de récupérer des données de manière asynchrone puis de les traiter de manière asynchrone.

Regardons un exemple de la façon de chaîner les promesses :

```typescript
// Exemple sur le fonctionnement du chaînage des promesses
// Première promesse
const promise1 = new Promise((resolve, reject) => {
  const functionOne: string = "Ceci est la première fonction de promesse";
  setTimeout(() => {
    resolve(functionOne);
  }, 1000);
});

// Deuxième promesse
const promise2 = (data: number) => {
  const functionTwo: string = "Ceci est la deuxième fonction de promesse";
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(` ${data}  '+'  ${functionTwo} `);
    }, 1000);
  });
};

// Chaînage des première et deuxième promesses ensemble
promise1
  .then(promise2)
  .then((result) => {
    console.log(result); // sortie: Ceci est la première fonction de promesse + Ceci est la deuxième fonction de promesse
  })
  .catch((error) => {
    console.error(error);
  });
```

Dans l'exemple ci-dessus, nous avons deux promesses : `promise1` et `promise2`. `promise1` se résout après 1 seconde avec la chaîne "Ceci est la première fonction de promesse." `promise2` prend un nombre en entrée et retourne une promesse qui se résout après 1 seconde avec une chaîne qui combine le nombre d'entrée et la chaîne "Ceci est la deuxième fonction de promesse."

Nous chaînons les deux promesses ensemble en utilisant la méthode `then`. La sortie de `promise1` est passée en entrée à `promise2`. Enfin, nous utilisons à nouveau la méthode `then` pour journaliser la sortie de `promise2` dans la console. Si `promise1` ou `promise2` est rejetée, l'erreur sera attrapée par la méthode `catch`.

Félicitations ! Vous avez appris comment créer et chaîner des promesses en TypeScript. Vous pouvez maintenant utiliser des promesses pour effectuer des opérations asynchrones en TypeScript. Maintenant, explorons comment `Async/Await` fonctionne en TypeScript.

## Comment utiliser Async / Await en TypeScript

**Async/await** est une syntaxe introduite dans ES2017 pour faciliter le travail avec les promesses. Elle permet d'écrire du code asynchrone qui ressemble et se comporte comme du code synchrone.

En TypeScript, vous pouvez définir une fonction asynchrone en utilisant le mot-clé `async`. Cela indique au compilateur que la fonction est asynchrone et retournera une promesse.

Maintenant, voyons comment utiliser async/await en TypeScript.

Syntaxe Async / Await :

```typescript
// Syntaxe Async / Await en TypeScript
async function functionName(): Promise<ReturnType> {
  try {
    const result = await promise;
    // code à exécuter après la résolution de la promesse
    return result;
  } catch (error) {
    // code à exécuter si la promesse est rejetée
    throw error;
  }
}
```

Dans l'exemple ci-dessus, `functionName` est une fonction asynchrone qui retourne une promesse de `ReturnType`. Le mot-clé `await` est utilisé pour attendre que la promesse se résolve avant de passer à la ligne de code suivante.

Le bloc `try/catch` est utilisé pour gérer les erreurs qui se produisent lors de l'exécution du code à l'intérieur de la fonction asynchrone. Si une erreur se produit, elle sera attrapée par le bloc catch, où vous pouvez la gérer de manière appropriée.

### **Utilisation des fonctions fléchées avec Async / Await**

Vous pouvez également utiliser des fonctions fléchées avec la syntaxe async/await en TypeScript :

```typescript
const functionName = async (): Promise<ReturnType> => {
  try {
    const result = await promise;
    // code à exécuter après la résolution de la promesse
    return result;
  } catch (error) {
    // code à exécuter si la promesse est rejetée
    throw error;
  }
};
```

Dans l'exemple ci-dessus, `functionName` est définie comme une fonction fléchée qui retourne une promesse de `ReturnType`. Le mot-clé async indique qu'il s'agit d'une fonction asynchrone, et le mot-clé await est utilisé pour attendre que la promesse se résolve avant de passer à la ligne de code suivante.

### **Async / Await avec un appel d'API**

Maintenant, allons au-delà de la syntaxe et récupérons des données depuis une API en utilisant async/await.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

const fetchApi = async (): Promise<void> => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");

    if (!response.ok) {
      throw new Error(
        `Échec de la récupération des utilisateurs (code de statut HTTP : ${response.status})`
      );
    }

    const data: User[] = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
    throw error;
  }
};

fetchApi();
```

Ici, nous récupérons des données depuis l'API JSONPlaceholder, les convertissons en JSON, puis les journalisons dans la console. Il s'agit d'un exemple concret de l'utilisation de async/await en TypeScript.

Vous devriez voir les informations des utilisateurs dans la console. Cette image montre la sortie :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737554438217/a1b865ea-0903-4749-a079-c8401be05787.png align="center")

### **Async/Await avec un appel d'API Axios**

```typescript
// Exemple 2 sur l'utilisation de async / await en typescript

const fetchApi = async (): Promise<void> => {
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/users"
    );
    const data = await response.data;
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

fetchApi();
```

Dans l'exemple ci-dessus, nous définissons la fonction `fetchApi()` en utilisant async/await et la méthode `Axios.get()` pour faire une requête HTTP GET à l'URL spécifiée. Nous utilisons await pour attendre la réponse, puis extrayons les données en utilisant la propriété data de l'objet de réponse. Enfin, nous journalisons les données dans la console avec `console.log()`. Toute erreur qui se produit est attrapée et journalisée dans la console avec `console.error()`.

Nous pouvons y parvenir en utilisant Axios, vous devriez donc voir le même résultat dans la console.

Cette image montre la sortie lors de l'utilisation d'Axios dans la console :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737554631796/4f85a12d-6a9b-4eaa-9ab9-910a8a463dc6.png align="center")

Remarque : Avant d'essayer le code ci-dessus, vous devez installer Axios en utilisant npm ou yarn.

```bash

npm install axios
```

```bash

yarn add axios
```

Si vous n'êtes pas familier avec Axios, vous pouvez [en apprendre davantage ici](https://www.npmjs.com/package/axios).

Vous pouvez voir que nous avons utilisé un bloc `try` et `catch` pour gérer les erreurs. Le bloc `try` et `catch` est une méthode pour gérer les erreurs en TypeScript. Donc, chaque fois que vous faites des appels d'API comme nous venons de le faire, assurez-vous d'utiliser un bloc `try` et `catch` pour gérer les erreurs.

Maintenant, explorons une utilisation plus avancée du bloc `try` et `catch` en TypeScript :

```typescript
// Exemple 3 sur l'utilisation de async / await en typescript

interface Recipe {
  id: number;
  name: string;
  ingredients: string[];
  instructions: string[];
  prepTimeMinutes: number;
  cookTimeMinutes: number;
  servings: number;
  difficulty: string;
  cuisine: string;
  caloriesPerServing: number;
  tags: string[];
  userId: number;
  image: string;
  rating: number;
  reviewCount: number;
  mealType: string[];
}

const fetchRecipes = async (): Promise<Recipe[] | string> => {
  const api = "https://dummyjson.com/recipes";
  try {
    const response = await fetch(api);

    if (!response.ok) {
      throw new Error(`Échec de la récupération des recettes : ${response.statusText}`);
    }

    const { recipes } = await response.json();
    return recipes; // Retourner le tableau des recettes
  } catch (error) {
    console.error("Erreur lors de la récupération des recettes :", error);
    if (error instanceof Error) {
      return error.message;
    }
    return "Une erreur inconnue s'est produite.";
  }
};

// Récupérer et journaliser les recettes
fetchRecipes().then((data) => {
  if (Array.isArray(data)) {
    console.log("Recettes récupérées avec succès :", data);
  } else {
    console.error("Message d'erreur :", data);
  }
});
```

Dans l'exemple ci-dessus, nous définissons une `interface Recipe` qui décrit la structure des données que nous attendons de l'API. Nous créons ensuite la fonction `fetchRecipes()` en utilisant async/await et la méthode fetch() pour faire une requête HTTP GET à l'endpoint API spécifié.

Nous utilisons un bloc `try/catch` pour gérer les erreurs qui pourraient survenir lors de la requête API. Si la requête réussit, nous extrayons la propriété data de la réponse en utilisant await et la retournons. Si une erreur se produit, nous vérifions la présence d'un message d'erreur et le retournons sous forme de chaîne s'il existe.

Enfin, nous appelons la fonction `fetchRecipes()` et utilisons `.then()` pour journaliser les données retournées dans la console. Cet exemple démontre comment utiliser `async/await` avec des blocs `try/catch` pour gérer les erreurs dans un scénario plus avancé, où nous devons extraire des données d'un objet de réponse et retourner un message d'erreur personnalisé.

Cette image montre le résultat de sortie du code :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737557515062/922592da-e9a6-4792-9d22-d5f8f8e84889.png align="center")

### **Async / Await avec Promise.all**

`Promise.all()` est une méthode qui prend un tableau de promesses en entrée (un itérable) et retourne une seule promesse en sortie. Cette promesse se résout lorsque toutes les promesses d'entrée ont été résolues ou si l'itérable d'entrée ne contient aucune promesse. Elle est rejetée immédiatement si l'une des promesses d'entrée est rejetée ou si des non-promesses lancent une erreur, et elle sera rejetée avec le premier message de rejet ou d'erreur.

```typescript
// Exemple d'utilisation de async / await avec Promise.all
interface User {
  id: number;
  name: string;
  email: string;
  profilePicture: string;
}

interface Post {
  id: number;
  title: string;
  body: string;
}

interface Comment {
  id: number;
  postId: number;
  name: string;
  email: string;
  body: string;
}

const fetchApi = async <T>(url: string): Promise<T> => {
  try {
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      return data;
    } else {
      throw new Error(`La réponse du réseau n'était pas correcte pour ${url}`);
    }
  } catch (error) {
    console.error(error);
    throw new Error(`Erreur lors de la récupération des données depuis ${url}`);
  }
};

const fetchAllApis = async (): Promise<[User[], Post[], Comment[]]> => {
  try {
    const [users, posts, comments] = await Promise.all([
      fetchApi<User[]>("https://jsonplaceholder.typicode.com/users"),
      fetchApi<Post[]>("https://jsonplaceholder.typicode.com/posts"),
      fetchApi<Comment[]>("https://jsonplaceholder.typicode.com/comments"),
    ]);
    return [users, posts, comments];
  } catch (error) {
    console.error(error);
    throw new Error("Erreur lors de la récupération des données depuis une ou plusieurs APIs");
  }
};

fetchAllApis()
  .then(([users, posts, comments]) => {
    console.log("Utilisateurs : ", users);
    console.log("Posts : ", posts);
    console.log("Commentaires : ", comments);
  })
  .catch((error) => console.error(error));
```

Dans le code ci-dessus, nous avons utilisé `Promise.all` pour récupérer plusieurs APIs en même temps. Si vous avez plusieurs APIs à récupérer, vous pouvez utiliser `Promise.all` pour les obtenir toutes en une seule fois. Comme vous pouvez le voir, nous avons utilisé `map` pour parcourir le tableau des APIs et l'avons ensuite passé à `Promise.all` pour les récupérer simultanément.

L'image ci-dessous montre la sortie des appels d'API :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737560380441/14bbecbb-7dad-464e-b412-028f56e9d679.png align="center")

Voyons comment utiliser `Promise.all` avec Axios :

```typescript
// Exemple d'utilisation de async / await avec axios et Promise.all

const fetchApi = async () => {
  try {
    const urls = [
      "https://jsonplaceholder.typicode.com/users",
      "https://jsonplaceholder.typicode.com/posts",
    ];
    const responses = await Promise.all(urls.map((url) => axios.get(url)));
    const data = await Promise.all(responses.map((response) => response.data));
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

fetchApi();
```

Dans l'exemple ci-dessus, nous utilisons `Promise.all` pour récupérer des données depuis deux URLs différentes en même temps. D'abord, nous créons un tableau d'URLs, puis utilisons map pour créer un tableau de promesses à partir des appels `axios.get`. Nous passons ce tableau à `Promise.all`, qui retourne un tableau de réponses. Enfin, nous utilisons à nouveau map pour obtenir les données de chaque réponse et les journaliser dans la console.

## Comment utiliser les Callbacks en TypeScript

Un **callback** est une fonction passée en argument à une autre fonction. La fonction de callback est exécutée à l'intérieur de l'autre fonction. Les callbacks garantissent qu'une fonction ne s'exécute pas avant qu'une tâche soit terminée, mais qu'elle s'exécute immédiatement après la fin de la tâche. Ils nous aident à écrire du code JavaScript asynchrone et à prévenir les problèmes et erreurs.

```typescript
// Exemple d'utilisation de callbacks en typescript

const add = (a: number, b: number, callback: (result: number) => void) => {
  const result = a + b;
  callback(result);
};

add(10, 20, (result) => {
  console.log(result);
});
```

L'image ci-dessous montre la fonction de callback :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737560660649/80203145-d053-49b8-a160-a1d72ed17a7a.png align="center")

Voyons un autre exemple d'utilisation des callbacks en TypeScript :

```typescript
// Exemple d'utilisation d'une fonction de callback en TypeScript

type User = {
  name: string;
  email: string;
};

const fetchUserData = (
  id: number,
  callback: (error: Error | null, user: User | null) => void
) => {
  const api = `https://jsonplaceholder.typicode.com/users/${id}`;
  fetch(api)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("La réponse du réseau n'était pas correcte.");
      }
    })
    .then((data) => {
      const user: User = {
        name: data.name,
        email: data.email,
      };
      callback(null, user);
    })
    .catch((error) => {
      callback(error, null);
    });
};

// Utilisation de fetchUserData avec une fonction de callback
fetchUserData(1, (error, user) => {
  if (error) {
    console.error(error);
  } else {
    console.log(user);
  }
});
```

Dans l'exemple ci-dessus, nous avons une fonction appelée `fetchUserData` qui prend un `id` et un `callback` en paramètres. Ce `callback` est une fonction avec deux paramètres : une erreur et un utilisateur.

La fonction `fetchUserData` récupère les données utilisateur depuis un endpoint API JSONPlaceholder en utilisant l'`id`. Si la récupération réussit, elle crée un objet `User` et le passe à la fonction de callback avec une erreur nulle. Si une erreur se produit lors de la récupération, elle envoie l'erreur à la fonction de callback avec un utilisateur nul.

Pour utiliser la fonction `fetchUserData` avec un callback, nous fournissons un `id` et une fonction de callback en arguments. La fonction de callback vérifie les erreurs et journalise les données utilisateur s'il n'y a pas d'erreurs.

L'image ci-dessous montre la sortie des appels d'API :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737560996613/2b37fa46-1ee4-4dee-8d50-82c09a235aec.png align="center")

### Comment utiliser les Callbacks de manière responsable

Bien que les callbacks soient fondamentaux pour la programmation asynchrone en TypeScript, ils nécessitent une gestion minutieuse pour éviter le **"callback hell"** - le code en forme de pyramide, profondément imbriqué, qui devient difficile à lire et à maintenir. Voici comment utiliser les callbacks efficacement :

1. **Éviter les imbrications profondes**
    
    * Aplanissez la structure de votre code en décomposant les opérations complexes en fonctions nommées
        
    * Utilisez les promesses ou async/await pour les flux de travail asynchrones complexes (plus d'informations ci-dessous)
        
2. **Gestion des erreurs en premier**
    
    * Suivez toujours la convention Node.js des paramètres `(error, result)`
        
    * Vérifiez les erreurs à chaque niveau de callbacks imbriqués
        
    
    ```typescript
    function processData(input: string, callback: (err: Error | null, result?: string) => void) {
      // ... toujours appeler le callback avec l'erreur en premier
    }
    ```
    
3. **Utiliser les annotations de type**
    
    * Tirez parti du système de types de TypeScript pour imposer les signatures de callback
        
    * Définissez des interfaces claires pour les paramètres de callback
        
    
    ```typescript
    type ApiCallback = (error: Error | null, data?: ApiResponse) => void;
    ```
    
4. **Envisager des bibliothèques de contrôle de flux**  
    Pour les opérations asynchrones complexes, utilisez des utilitaires comme `async.js` pour :
    
    * Exécution parallèle
        
    * Exécution en série
        
    * Pipelines de gestion des erreurs
        

### Quand utiliser les Callbacks vs. les alternatives

Il y a des moments où les callbacks sont un excellent choix, et d'autres où ils ne le sont pas.

Les callbacks sont utiles lorsque vous travaillez avec des opérations asynchrones (achèvement unique), interfacer avec des bibliothèques ou APIs plus anciennes qui attendent des callbacks, gérer des écouteurs d'événements (comme les écouteurs de clics ou les événements websocket) ou créer des utilitaires légers avec des besoins asynchrones simples.

Dans d'autres scénarios où vous devez vous concentrer sur l'écriture de code maintenable avec un flux asynchrone clair, les callbacks posent problème et vous devriez préférer les promesses ou async-await. Par exemple, lorsque vous devez chaîner plusieurs opérations, gérer une propagation d'erreurs complexe, travailler avec des APIs modernes (comme l'API Fetch ou FS Promises), ou utiliser `promise.all()` pour une exécution parallèle.

**Exemple de migration des callbacks vers les promesses :**

```typescript
// Version avec callback
function fetchUser(id: number, callback: (err: Error | null, user?: User) => void) {
  // ... 
}

// Version avec promesse
async function fetchUserAsync(id: number): Promise<User> {
  // ...
}

// Utilisation avec async/await
try {
  const user = await fetchUserAsync(1);
} catch (error) {
  // Gérer l'erreur
}
```

### L'évolution des modèles asynchrones

| Modèle | Avantages | Inconvénients |
| --- | --- | --- |
| Callbacks | Simple, universel | Complexité imbriquée |
| Promesses | Chaînables, meilleur flux d'erreurs | Nécessite des chaînes .then() |
| Async/Await | Lisibilité similaire au synchrone | Nécessite une transpilation |

Les projets TypeScript modernes utilisent souvent un mélange : des callbacks pour les modèles pilotés par événements et des promesses/async-await pour la logique asynchrone complexe. La clé est de choisir le bon outil pour votre cas d'utilisation spécifique tout en maintenant la clarté du code.

## Conclusion

Dans cet article, nous avons appris les différentes façons de gérer le code asynchrone en TypeScript. Nous avons appris les callbacks, les promesses, async/await, et comment les utiliser en TypeScript. Nous avons également appris ce concept.

Si vous souhaitez en apprendre davantage sur la programmation et comment devenir un meilleur ingénieur logiciel, vous pouvez vous abonner à ma chaîne YouTube [CliffTech](https://www.youtube.com/@CliffTech/videos).

Merci d'avoir lu mon article. J'espère que vous l'avez apprécié. Si vous avez des questions, n'hésitez pas à me contacter.

Connectez-vous avec moi sur les réseaux sociaux :

* [Twitter](https://twitter.com/Clifftech_Dev)
    
* [Github](https://github.com/Clifftech123)
    
* [Linkedin](https://www.linkedin.com/in/isaiah-clifford-opoku-a506a51b2/)