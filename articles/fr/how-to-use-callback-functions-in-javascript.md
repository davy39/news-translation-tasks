---
title: Comment utiliser les fonctions de rappel en JavaScript
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-07-03T21:24:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-callback-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Callback_functions_JavaScript.png
tags:
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les fonctions de rappel en JavaScript
seo_desc: 'When you''re building dynamic applications with JavaScript that display
  real-time data – like a weather app or live sports dashboard – you''ll need a way
  to automatically fetch new data from an external source without disrupting the user
  experience.

  Yo...'
---

Lorsque vous construisez des applications dynamiques avec JavaScript qui affichent des données en temps réel - comme une application météo ou un tableau de bord de sports en direct - vous aurez besoin d'un moyen de récupérer automatiquement de nouvelles données à partir d'une source externe sans perturber l'expérience utilisateur.

Vous pouvez le faire en utilisant les fonctions de rappel de JavaScript, qui montrent la capacité de JavaScript à gérer les opérations asynchrones. Explorons ce que sont les fonctions de rappel, comment elles fonctionnent et pourquoi elles sont essentielles en JavaScript.

## Table des matières

* [Qu'est-ce qu'une fonction de rappel ?](#heading-quest-ce-quune-fonction-de-rappel)
    
* [Pourquoi utiliser les fonctions de rappel ?](#heading-pourquoi-utiliser-les-fonctions-de-rappel)
    
* [Structure de base d'une fonction de rappel](#heading-structure-de-base-dune-fonction-de-rappel)
    
* [Comment fonctionnent les rappels](#heading-comment-fonctionnent-les-rappels)
    
* [Comment gérer les erreurs avec les rappels](#heading-comment-gerer-les-erreurs-avec-les-rappels)
    
* [Le problème de l'enfer des rappels](#heading-le-probleme-de-lenfer-des-rappels)
    
* [Comment utiliser les Promesses et Async/Await](#heading-comment-utiliser-les-promesses-et-asyncawait)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'une fonction de rappel ?

Une fonction de rappel est une fonction qui est passée en argument à une autre fonction et qui est exécutée après l'achèvement de certaines opérations.

Ce mécanisme permet à JavaScript d'effectuer des tâches comme la lecture de fichiers, les requêtes HTTP ou l'attente d'une entrée utilisateur sans bloquer l'exécution du programme. Cela aide à garantir une expérience utilisateur fluide.

## Pourquoi utiliser les fonctions de rappel ?

JavaScript s'exécute dans un environnement monothread, ce qui signifie qu'il ne peut exécuter qu'une seule commande à la fois. Les fonctions de rappel aident à gérer les opérations asynchrones, garantissant que le code continue à s'exécuter sans attendre que les tâches soient terminées. Cette approche est cruciale pour maintenir un programme réactif et efficace.

## Structure de base d'une fonction de rappel

Pour illustrer, regardons un exemple simple :

```javascript
function greet(name, callback) {
  console.log(`Bonjour, ${name}!`);
  callback();
}

function sayGoodbye() {
  console.log("Au revoir !");
}

greet("Alice", sayGoodbye);
```

Dans ce code :

* `greet` est une fonction qui prend un nom et une fonction de rappel comme arguments.
    
* Après avoir salué l'utilisateur, elle appelle la fonction de rappel.
    

## Comment fonctionnent les rappels

1. **Passage de la fonction :** La fonction que vous souhaitez exécuter après une opération est passée en argument à une autre fonction.
    
2. **Exécution du rappel :** La fonction principale exécute la fonction de rappel au moment approprié. Cela peut être après un délai, une fois une tâche terminée, ou lorsqu'un événement se produit.
    

Voici un exemple plus détaillé avec une opération asynchrone simulée utilisant `setTimeout` :

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: "Alice" };
    callback(data);
  }, 2000); // Simulation d'un délai de 2 secondes
}

fetchData((data) => {
  console.log("Données reçues :", data);
});
```

Dans cet exemple :

* `fetchData` simule la récupération de données après un délai de 2 secondes.
    
* La fonction de rappel journalise les données une fois qu'elles sont reçues.
    

## Comment gérer les erreurs avec les rappels

Dans des scénarios réels, vous devrez souvent gérer les erreurs. Un modèle courant consiste à passer une erreur comme premier argument à la fonction de rappel :

```js
function readFile(filePath, callback) {
  const fs = require('fs');
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      callback(err, null);
    } else {
      callback(null, data);
    }
  });
}

readFile('example.txt', (err, data) => {
  if (err) {
    console.error("Erreur de lecture du fichier :", err);
  } else {
    console.log("Contenu du fichier :", data);
  }
});
```

Ici :

* La fonction `readFile` lit un fichier de manière asynchrone.
    
* Elle appelle le rappel avec une erreur (si elle existe) ou les données du fichier.
    

## Le problème de l'enfer des rappels

À mesure que les applications grandissent, l'utilisation de plusieurs rappels imbriqués peut devenir complexe et difficile à gérer, souvent appelée "l'enfer des rappels". Voici un exemple de l'enfer des rappels :

```js
function stepOne(callback) {
  setTimeout(() => callback(null, 'Étape Une Complétée'), 1000);
}

function stepTwo(callback) {
  setTimeout(() => callback(null, 'Étape Deux Complétée'), 1000);
}

function stepThree(callback) {
  setTimeout(() => callback(null, 'Étape Trois Complétée'), 1000);
}

stepOne((err, result) => {
  if (err) return console.error(err);
  console.log(result);
  stepTwo((err, result) => {
    if (err) return console.error(err);
    console.log(result);
    stepThree((err, result) => {
      if (err) return console.error(err);
      console.log(result);
    });
  });
});
```

Ce code est difficile à lire et à maintenir. Pour résoudre ce problème, le JavaScript moderne fournit les `Promesses` et la syntaxe `async/await`, rendant le code plus propre et plus facile à gérer.

## Comment utiliser les Promesses et Async/Await

Les Promesses représentent l'achèvement éventuel (ou l'échec) d'une opération asynchrone et sa valeur résultante.

```js
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ id: 1, name: "Alice" });
    }, 2000);
  });
}

fetchData()
  .then(data => {
    console.log("Données reçues :", data);
  })
  .catch(error => {
    console.error("Erreur :", error);
  });
```

La syntaxe Async/Await simplifie le travail avec les Promesses :

```js
async function getData() {
  try {
    const data = await fetchData();
    console.log("Données reçues :", data);
  } catch (error) {
    console.error("Erreur :", error);
  }
}

getData();
```

Cette approche fait ressembler le code asynchrone et se comporter comme du code synchrone, améliorant la lisibilité et la maintenabilité.

Vous pouvez [en savoir plus sur les promesses et async/await ici](https://www.freecodecamp.org/news/guide-to-javascript-promises/).

## Conclusion

Les fonctions de rappel sont fondamentales en JavaScript pour gérer les opérations asynchrones. Bien qu'elles offrent un moyen puissant de gérer le flux asynchrone, elles peuvent devenir complexes et difficiles à maintenir.

L'utilisation des Promesses et de la syntaxe async/await peut simplifier votre code, le rendant plus propre et plus facile à gérer.

Comprendre ces concepts vous aidera à écrire un code JavaScript plus efficace et plus maintenable.

Connectez-vous avec moi sur [LinkedIn](http://www.linkedin.com/in/samuel-oluwadamisi-01b3a4236) et [Twitter](https://twitter.com/Data_Steve_) si vous avez trouvé cela utile.