---
title: Comment fonctionnent les callbacks dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T22:53:02.000Z'
originalURL: https://freecodecamp.org/news/nodejs-callbacks
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-chepte--cormani-1416530.jpg
tags:
- name: callbacks
  slug: callbacks
- name: node
  slug: node
- name: node js
  slug: node-js
seo_title: Comment fonctionnent les callbacks dans Node.js
seo_desc: "By Aditya Gupta\nNode.js callbacks are a special type of function passed\
  \ as an argument to another function. \nThey're called when the function that contains\
  \ the callback as an argument completes its execution, and allows the code in the\
  \ callback to ru..."
---

Par Aditya Gupta

Les callbacks de Node.js sont un type spécial de fonction passé en tant qu'argument à une autre fonction. 

Ils sont appelés lorsque la fonction qui contient le callback en tant qu'argument termine son exécution, et permettent au code dans le callback de s'exécuter en attendant.

Les callbacks nous aident à effectuer des appels asynchrones. Même les API de Node.js sont écrites de manière à supporter les callbacks.

**Voici la syntaxe d'un callback dans Node :**

```javascript
function function_name(argument, callback)
```

## **Comment utiliser les callbacks dans Node**

Le callback est utilisé pour définir ce qui se passe lorsque la fonction contenant le callback en tant qu'argument termine son exécution.

Par exemple, nous pouvons définir un callback pour afficher l'erreur et le résultat après l'exécution de la fonction.

```javascript
function function_name(argument, function (error, result){ if(error){ console.log(error) } else { console.log(result) } })
```

## **Comment écrire des callbacks**

Vous pouvez écrire une fonction de callback de deux manières : sous forme de fonction fléchée, et sous forme de fonction standard sans nom. Les deux méthodes donneront le même résultat.

### Comment écrire un callback sous forme de fonction standard sans nom

Vous pouvez écrire un callback sous forme de fonction régulière. Vous le faites en utilisant le mot-clé function puis l'argument à l'intérieur de parenthèses. Ensuite, vous utilisez des accolades où vous pouvez définir le corps du callback. Il n'est pas nécessaire de définir le nom de la fonction puisqu'elle est appelée automatiquement.

**Syntaxe :**

```javascript
function function_name(argument, function (callback_argument){
    // corps du callback 
})
```

Voyons un exemple de callback en utilisant la fonction setTimeout. Vous pouvez utiliser cette méthode pour définir une fonction de callback qui s'exécute après un temps défini.

```javascript
setTimeout(function () { 
    console.log('Callback en tant que fonction standard'); 
}, 1000);
```

Ici, nous définissons un callback qui s'exécute après 1000 millisecondes, ce qui équivaut à 1 seconde.

**Sortie :**

![Callback Standard](https://codeforgeek.com/wp-content/uploads/2022/11/callback-standard.png)

### Comment écrire un callback sous forme de fonction fléchée

Il peut être confus d'avoir plusieurs mots-clés function dans un bloc de code. Pour éliminer le mot-clé function dans le callback, vous pouvez utiliser une fonction fléchée. La fonction fléchée a été introduite dans ES6 et vous aide à écrire un code plus propre en supprimant le mot-clé function.

**Syntaxe :**

```javascript
function function_name(argument, (callback_argument) => { 
    // corps du callback 
})
```

Réécrivons le même exemple que nous avons écrit dans la section précédente en utilisant une fonction fléchée. Ici, nous changeons la chaîne en "Callback en tant que fonction fléchée".

```javascript
setTimeout(() => { 
    console.log('Callback en tant que fonction fléchée'); 
}, 1000);
```

**Sortie :**

![Callback en tant que fonction fléchée](https://codeforgeek.com/wp-content/uploads/2022/11/callback-as-arrow-function.png)

## Programmation asynchrone utilisant les callbacks

La programmation asynchrone est une approche pour exécuter plusieurs processus en même temps sans bloquer les autres parties du code.

En utilisant les callbacks, nous pouvons écrire du code asynchrone de manière plus efficace. Par exemple, nous pouvons définir un callback qui affiche le résultat après que la fonction parente ait terminé son exécution. Ainsi, il n'est pas nécessaire de bloquer d'autres blocs de code pour afficher le résultat.

Prenons l'exemple d'un module de système de fichiers qui est utilisé pour interagir avec les fichiers dans Node.js. Pour lire un fichier, nous pouvons utiliser la méthode `readFileSync`.

```javascript
const fs = require('fs');

const data = fs.readFileSync('hello.txt', 'utf-8'); console.log(data);
```

**Sortie :**

![Sortie Read Sync](https://codeforgeek.com/wp-content/uploads/2022/11/output-read-sync.png)

Mais de cette manière, notre code retarde l'exécution du reste du programme jusqu'à ce qu'il termine son exécution et affiche le résultat. 

Heureusement, nous pouvons utiliser un callback pour écrire le code de manière asynchrone sans bloquer le reste de l'exécution en utilisant la méthode readFile. Lorsque la lecture du fichier est terminée, le callback est déclenché et affiche le résultat.

```javascript
const fs = require('fs'); 

const data = fs.readFile('hello.txt', 'utf-8', function(err, result){ 
    if(err){ 
        console.log(err) 
    } else { 
        console.log(result) 
    } 
});
```

**Sortie :**

![Sortie Read Async](https://codeforgeek.com/wp-content/uploads/2022/11/output-read-sync-1.png)

## **Résumé**

Les callbacks de NodeJS sont un type spécial de fonction que vous pouvez utiliser pour écrire du code asynchrone. Ils vous donnent un moyen d'exécuter un bloc de code en attendant après l'exécution d'une fonction. Vous pouvez définir s'il affiche un résultat, une erreur, ou effectue une opération supplémentaire sur le résultat de la fonction. 

Il existe deux façons d'écrire une fonction : sans nom de fonction, ou sous la forme d'une fonction fléchée. La fonction fléchée est plus pratique et permet d'obtenir un code plus propre en supprimant l'utilisation de mots-clés de fonction ennuyeux. 

J'espère que cet article vous aide à comprendre les callbacks de Node.js.

Vous pouvez [consulter la documentation ici](https://nodejs.org/en/knowledge/getting-started/control-flow/what-are-callbacks/) si vous souhaitez en apprendre davantage.