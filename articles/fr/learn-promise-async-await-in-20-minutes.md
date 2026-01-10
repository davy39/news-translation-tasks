---
title: Comment apprendre les Promesses JavaScript et Async/Await en 20 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-01T01:38:27.000Z'
originalURL: https://freecodecamp.org/news/learn-promise-async-await-in-20-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/maxresdefault.jpg
tags:
- name: async/await
  slug: asyncawait
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: promises
  slug: promises
seo_title: Comment apprendre les Promesses JavaScript et Async/Await en 20 minutes
seo_desc: 'By Thu Nghiem

  On the web, many things tend to be time-consuming – if you query an API, it can
  take a while to receive a response. Therefore, asynchronous programming is an essential
  skill for developers.

  When working with asynchronous operations in J...'
---

Par Thu Nghiem

Sur le web, de nombreuses choses tendent à être chronophages – si vous interrogez une API, cela peut prendre un certain temps pour recevoir une réponse. Par conséquent, la programmation asynchrone est une compétence essentielle pour les développeurs.

Lorsqu'on travaille avec des opérations asynchrones en JavaScript, nous entendons souvent le terme `Promise`. Mais il peut être difficile de comprendre comment elles fonctionnent et comment les utiliser.

Contrairement à de nombreux tutoriels de codage traditionnels, dans ce tutoriel, nous allons apprendre en pratiquant. Nous allons compléter quatre tâches à la fin de l'article :

* Tâche 1 : Les bases des Promesses expliquées en utilisant mon anniversaire
* Tâche 2 : Construire un jeu de devinettes
* Tâche 3 : Récupérer les informations d'un pays depuis une API
* Tâche 4 : Récupérer les pays voisins d'un pays

Si vous souhaitez suivre, assurez-vous de télécharger les ressources ici : [https://bit.ly/3m4bjWI](https://bit.ly/3m4bjWI)

%[https://youtu.be/J29jeuyMJ38]

## Tâche 1 : Les bases des Promesses expliquées en utilisant mon anniversaire

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/z51d1v0jf07b43bfhfuu.gif)

Mon ami Kayo promet de faire un gâteau pour mon anniversaire dans deux semaines.

Si tout se passe bien et que Kayo ne tombe pas malade, nous aurons un certain nombre de gâteaux. (Les gâteaux sont comptables dans ce tutoriel 😆). Sinon, si Kayo tombe malade, nous n'aurons pas de gâteaux.

Dans tous les cas, nous aurons toujours une fête.

Pour cette première tâche, nous allons traduire cette histoire en code. Commençons par créer une fonction qui retourne une `Promise` :

```js
const onMyBirthday = (isKayoSick) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!isKayoSick) {
        resolve(2);
      } else {
        reject(new Error("Je suis triste"));
      }
    }, 2000);
  });
};
```

En JavaScript, nous pouvons créer une nouvelle `Promise` avec `new Promise()`, qui prend une fonction comme argument : `(resolve, reject) => {}`. 

Dans cette fonction, `resolve` et `reject` sont des fonctions de rappel qui sont fournies par défaut en JavaScript.

Examinons de plus près le code ci-dessus.

Lorsque nous exécutons la fonction `onMyBirthday`, après `2000ms` :

* Si Kayo n'est pas malade, alors nous exécutons `resolve` avec `2` comme argument
* Si Kayo est malade, alors nous exécutons `reject` avec `new Error("Je suis triste")` comme argument. Même si vous pouvez passer n'importe quoi à `reject` comme argument, il est recommandé de passer un objet `Error`.

Maintenant, parce que `onMyBirthday()` retourne une `Promise`, nous avons accès aux méthodes `then`, `catch`, et `finally`. 

Et nous avons également accès aux arguments qui ont été passés à `resolve` et `reject` précédemment dans `then` et `catch`.

Examinons de plus près le code.

Si Kayo n'est pas malade :

```js
onMyBirthday(false)
  .then((result) => {
    console.log(`J'ai ${result} gâteaux`); // Dans la console : J'ai 2 gâteaux  
  })
  .catch((error) => {
    console.log(error); // Ne s'exécute pas
  })
  .finally(() => {
    console.log("Fête"); // S'affiche dans la console quoi qu'il arrive : Fête
  });

```

Si Kayo est malade :

```js
onMyBirthday(true)
  .then((result) => {
    console.log(`J'ai ${result} gâteaux`); // ne s'exécute pas 
  })
  .catch((error) => {
    console.log(error); // dans la console : Error: Je suis triste
  })
  .finally(() => {
    console.log("Fête"); // S'affiche dans la console quoi qu'il arrive : Fête
  });

```

D'accord, donc maintenant, j'espère que vous avez compris l'idée de base de `Promise`. Passons à la tâche 2.

## Tâche 2 : Construire un jeu de devinettes

Les exigences :

* Histoire utilisateur : Un utilisateur peut entrer un nombre
* Histoire utilisateur : Le système choisit un nombre aléatoire entre 1 et 6
* Histoire utilisateur : Si le nombre de l'utilisateur est égal à un nombre aléatoire, donner à l'utilisateur 2 points
* Histoire utilisateur : Si le nombre de l'utilisateur est différent du nombre aléatoire de 1,  
donner à l'utilisateur 1 point. Sinon, donner à l'utilisateur 0 point
* Histoire utilisateur : L'utilisateur peut jouer au jeu aussi longtemps qu'il le souhaite

Pour les quatre premières histoires utilisateur, créons une fonction `enterNumber` et retournons une `Promise` :

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    // Commençons par ici
  });
};
```

La première chose que nous devons faire est de demander un nombre à l'utilisateur et de choisir un nombre aléatoire entre 1 et 6 :

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Entrez un nombre (1 - 6) :")); // Demander à l'utilisateur d'entrer un nombre
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Choisir un nombre aléatoire entre 1 et 6
  });
};

```

Maintenant, `userNumber` peut entrer une valeur qui n'est pas un nombre. Si c'est le cas, appelons la fonction `reject` avec une erreur :

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Entrez un nombre (1 - 6) :")); // Demander à l'utilisateur d'entrer un nombre
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Choisir un nombre aléatoire entre 1 et 6

    if (isNaN(userNumber)) {
      reject(new Error("Mauvais type de saisie")); // Si l'utilisateur entre une valeur qui n'est pas un nombre, exécuter reject avec une erreur
    }
  });
};

```

La prochaine chose que nous voulons faire est de vérifier si `userNumber` est égal à `randomNumber`, si c'est le cas, nous voulons donner à l'utilisateur 2 points et nous pouvons exécuter la fonction `resolve` en passant un objet `{ points: 2, randomNumber }`. Remarquez ici que nous voulons également connaître le `randomNumber` lorsque la Promesse est résolue

Si `userNumber` est différent de `randomNumber` d'un, alors nous donnons à l'utilisateur 1 point. Sinon, nous donnons à l'utilisateur 0 point :

```js
return new Promise((resolve, reject) => {
  const userNumber = Number(window.prompt("Entrez un nombre (1 - 6) :")); // Demander à l'utilisateur d'entrer un nombre
  const randomNumber = Math.floor(Math.random() * 6 + 1); // Choisir un nombre aléatoire entre 1 et 6

  if (isNaN(userNumber)) {
    reject(new Error("Mauvais type de saisie")); // Si l'utilisateur entre une valeur qui n'est pas un nombre, exécuter reject avec une erreur
  }

  if (userNumber === randomNumber) {
    // Si le nombre de l'utilisateur correspond au nombre aléatoire, retourner 2 points
    resolve({
      points: 2,
      randomNumber,
    });
  } else if (
    userNumber === randomNumber - 1 ||
    userNumber === randomNumber + 1
  ) {
    // Si le nombre de l'utilisateur est différent du nombre aléatoire de 1, retourner 1 point
    resolve({
      points: 1,
      randomNumber,
    });
  } else {
    // Sinon retourner 0 points
    resolve({
      points: 0,
      randomNumber,
    });
  }
});
```

D'accord, créons également une autre fonction pour demander si l'utilisateur veut continuer le jeu :

```js
const continueGame = () => {
  return new Promise((resolve) => {
    if (window.confirm("Voulez-vous continuer ?")) { // Demander si l'utilisateur veut continuer le jeu avec une modale de confirmation
      resolve(true);
    } else {
      resolve(false);
    }
  });
};

```

Remarquez ici que nous créons une `Promise`, mais elle n'utilise pas le rappel `reject`. Cela est tout à fait correct.

Maintenant, créons une fonction pour gérer la devinette :

```js
const handleGuess = () => {
  enterNumber() // Cela retourne une Promesse
    .then((result) => {
      alert(`Dé : ${result.randomNumber} : vous avez obtenu ${result.points} points`); // Lorsque resolve est exécuté, nous obtenons les points et le nombre aléatoire 
      
      // Demandons à l'utilisateur s'il veut continuer le jeu
      continueGame().then((result) => {
        if (result) {
          handleGuess(); // Si oui, nous exécutons handleGuess à nouveau
        } else {
          alert("Le jeu se termine"); // Si non, nous affichons une alerte
        }
      });
    })
    .catch((error) => alert(error));
};

handleGuess(); // Exécuter la fonction handleGuess

```

Ici, lorsque nous appelons `handleGuess`, `enterNumber()` retourne maintenant une `Promise` :

* Si la `Promise` est résolue, nous appelons la méthode `then` et affichons un message d'alerte. Nous demandons également si l'utilisateur veut continuer.
* Si la `Promise` est rejetée, nous affichons un message d'alerte avec l'erreur.

Comme vous pouvez le voir, le code est assez difficile à lire.

Refactorisons un peu la fonction `handleGuess` en utilisant la syntaxe `async/await` :

```js
const handleGuess = async () => {
  try {
    const result = await enterNumber(); // Au lieu de la méthode then, nous pouvons obtenir le résultat directement en mettant simplement await avant la promesse

    alert(`Dé : ${result.randomNumber} : vous avez obtenu ${result.points} points`);

    const isContinuing = await continueGame();

    if (isContinuing) {
      handleGuess();
    } else {
      alert("Le jeu se termine");
    }
  } catch (error) { // Au lieu de la méthode catch, nous pouvons utiliser la syntaxe try, catch
    alert(error);
  }
};

```

Vous pouvez voir que nous avons créé une fonction `async` en mettant `async` avant les crochets. Ensuite, dans la fonction `async` :

* Au lieu de la méthode `then`, nous pouvons obtenir les résultats directement simplement en mettant `await` avant la promesse
* Au lieu de la méthode `catch`, nous pouvons utiliser la syntaxe `try, catch`

Voici tout le code pour cette tâche à nouveau pour votre référence :

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Entrez un nombre (1 - 6) :")); // Demander à l'utilisateur d'entrer un nombre
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Choisir un nombre aléatoire entre 1 et 6

    if (isNaN(userNumber)) {
      reject(new Error("Mauvais type de saisie")); // Si l'utilisateur entre une valeur qui n'est pas un nombre, exécuter reject avec une erreur
    }

    if (userNumber === randomNumber) { // Si le nombre de l'utilisateur correspond au nombre aléatoire, retourner 2 points
      resolve({
        points: 2,
        randomNumber,
      });
    } else if (
      userNumber === randomNumber - 1 ||
      userNumber === randomNumber + 1
    ) { // Si le nombre de l'utilisateur est différent du nombre aléatoire de 1, retourner 1 point
      resolve({
        points: 1,
        randomNumber,
      });
    } else { // Sinon retourner 0 points
      resolve({
        points: 0,
        randomNumber,
      });
    }
  });
};

const continueGame = () => {
  return new Promise((resolve) => {
    if (window.confirm("Voulez-vous continuer ?")) { // Demander si l'utilisateur veut continuer le jeu avec une modale de confirmation
      resolve(true);
    } else {
      resolve(false);
    }
  });
};

const handleGuess = async () => {
  try {
    const result = await enterNumber(); // Au lieu de la méthode then, nous pouvons obtenir le résultat directement en mettant simplement await avant la promesse

    alert(`Dé : ${result.randomNumber} : vous avez obtenu ${result.points} points`);

    const isContinuing = await continueGame();

    if (isContinuing) {
      handleGuess();
    } else {
      alert("Le jeu se termine");
    }
  } catch (error) { // Au lieu de la méthode catch, nous pouvons utiliser la syntaxe try, catch
    alert(error);
  }
};

handleGuess(); // Exécuter la fonction handleGuess

```

D'accord, nous avons terminé la deuxième tâche. Passons à la troisième.

## Tâche 3 : Récupérer les informations d'un pays depuis [une API](https://restcountries.eu/)

Vous verrez `Promises` utilisées fréquemment lors de la récupération de données depuis une API.

Si vous ouvrez [https://restcountries.eu/rest/v2/alpha/col](https://restcountries.eu/rest/v2/alpha/col) dans un nouveau navigateur, vous verrez les données du pays au format JSON.  
  
En utilisant l'[API Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), nous pouvons récupérer les données par :

```js
const fetchData = async () => {
  const res = await fetch("https://restcountries.eu/rest/v2/alpha/col"); // fetch() retourne une promesse, donc nous devons l'attendre

  const country = await res.json(); // res est maintenant seulement une réponse HTTP, donc nous devons appeler res.json()

  console.log(country); // Les données de la Colombie seront enregistrées dans la console de développement
};

fetchData();


```

Maintenant que nous avons les données du pays que nous voulons, passons à la dernière tâche.

## Tâche 4 : Récupérer les pays voisins d'un pays

Si vous ouvrez la tâche 4, vous verrez que nous avons une fonction `fetchCountry`, qui récupère les données depuis l'endpoint : `https://restcountries.eu/rest/v2/alpha/${alpha3Code}` où `alpha3code` est le code du pays.  
  
Vous voyez également qu'elle attrapera toute `erreur` qui pourrait survenir lors de la récupération des données.

```js
// Tâche 4 : obtenir les pays voisins de la Colombie

const fetchCountry = async (alpha3Code) => {
  try {
    const res = await fetch(
      `https://restcountries.eu/rest/v2/alpha/${alpha3Code}`
    );

    const data = await res.json();

    return data;
  } catch (error) {
    console.log(error);
  }
};

```

Créons une fonction `fetchCountryAndNeighbors` et récupérons les informations de la Colombie en passant `col` comme `alpha3code`.

```js
const fetchCountryAndNeighbors = async () => {
  const columbia = await fetchCountry("col");

  console.log(columbia);
};

fetchCountryAndNeighbors();

```

Maintenant, si vous regardez dans votre console, vous pouvez voir un objet qui ressemble à ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/35vkx7gewawg05wfcmni.png)

Dans l'objet, il y a une propriété `border` qui est une liste de `alpha3codes` pour les pays voisins de la Colombie.

Maintenant, si nous essayons d'obtenir les pays voisins par :

```js
  const neighbors = 
    columbia.borders.map((border) => fetchCountry(border));

```

Alors, `neighbors` sera un tableau d'objets `Promise`.

Lorsqu'on travaille avec un tableau de promesses, nous devons utiliser `Promise.all` :

```js
const fetchCountryAndNeighbors = async () => {
  const columbia = await fetchCountry("col");

  const neighbors = await Promise.all(
    columbia.borders.map((border) => fetchCountry(border))
  );

  console.log(neighbors);
};

fetchCountryAndNeighbors();

```

Dans la `console`, nous devrions pouvoir voir la liste des objets pays.

Voici tout le code pour la tâche 4 à nouveau pour votre référence :

```js
const fetchCountry = async (alpha3Code) => {
  try {
    const res = await fetch(
      `https://restcountries.eu/rest/v2/alpha/${alpha3Code}`
    );

    const data = await res.json();

    return data;
  } catch (error) {
    console.log(error);
  }
};

const fetchCountryAndNeighbors = async () => {
  const columbia = await fetchCountry("col");

  const neighbors = await Promise.all(
    columbia.borders.map((border) => fetchCountry(border))
  );

  console.log(neighbors);
};

fetchCountryAndNeighbors();

```

## Conclusion

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/34m9mus03v2zo9agn2bq.png)

Après avoir complété ces 4 tâches, vous pouvez voir que `Promise` est utile lorsqu'il s'agit d'actions asynchrones ou de choses qui ne se produisent pas en même temps.

Vous pouvez voir cela en pratique dans l'un de mes tutoriels, où nous construisons une application à partir de zéro avec React et Next.js :

%[https://youtu.be/v8o9iJU5hEA]

## __________ 🐣 À propos de moi __________

* Je suis le fondateur de [DevChallenges](https://devchallenges.io/)
* Abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1)
* Suivez-moi sur [Twitter](https://twitter.com/thunghiemdinh)
* Rejoignez [Discord](https://discord.com/invite/3R6vFeM)