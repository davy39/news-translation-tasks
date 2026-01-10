---
title: Comment apporter un peu de programmation asynchrone à Dart avec les futures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-09T14:18:59.000Z'
originalURL: https://freecodecamp.org/news/dart-asynchronous-programming-futures-5b20c62a91c0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PHW1lAVb2eup99AreoKPvQ.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment apporter un peu de programmation asynchrone à Dart avec les futures
seo_desc: 'By Mohammed Salman

  Asynchronous programming is a form of parallel programming that allows a unit of
  work to run separately from the primary application thread. When the work is complete,
  it notifies the main thread (as well as whether the work was co...'
---

Par Mohammed Salman

La programmation asynchrone est une forme de programmation parallèle qui permet à une unité de travail de s'exécuter séparément du thread principal de l'application. Lorsque le travail est terminé, il notifie le thread principal (ainsi que si le travail a été terminé ou a échoué). Il y a de nombreux avantages à l'utiliser, tels que l'amélioration des performances de l'application et une réactivité accrue.

[Originalement publié sur mon blog.](https://code.nimrey.me/dart-asynchronous-programming-futures/)

[TL;DR](#dbd5).

### Problème

Le code Dart s'exécute dans un seul thread d'exécution, donc si celui-ci est bloqué, l'ensemble du programme se fige.

Exemple :

```
//..
```

```
var data = fetchDataFromSomeApi(); // Prend du temps pour récupérer les données
```

```
doStuffWithData(data); // Manipuler les données
```

```
doOtherStuff(); // Faire autre chose sans rapport avec les données
```

```
//..
```

Puisque `fetchDataFromSomeApi()` bloque, le reste du code ne s'exécute qu'après que `fetchDataFromSomeApi()` ait retourné les données, *peu importe le temps que cela prend*.

Ce code s'exécute ligne par ligne, ce qui fait que le code s'arrête et que `doOtherStuff()` s'exécute après que l'opération de récupération des données soit terminée (ce qui n'est probablement pas ce que vous voulez).

### Solution

Les opérations asynchrones permettent à votre programme de compléter d'autres travaux tout en attendant que d'autres opérations se terminent.

Le même exemple que ci-dessus, mais avec une approche asynchrone :

```
fetchDataFromSomeApi().then((data) {  print('Données récupérées');  doStuffWithData(data);});
```

```
print('Travail sur d'autres choses...');doOtherStuff();
```

```
// Sortie :
//   Travail sur d'autres choses...
//   Données récupérées
```

`fetchDataFromSomeApi` est non-bloquant, ce qui signifie qu'il permet à d'autres codes de s'exécuter pendant la récupération des données. C'est pourquoi l'instruction `print` de niveau supérieur s'exécute avant l'instruction `print` dans la fonction de rappel.

### Futures

Un future représente un calcul qui ne se termine pas immédiatement. Là où une fonction normale retourne le résultat, une fonction asynchrone retourne un future, qui contiendra éventuellement le résultat. Le future vous informera lorsque le résultat sera prêt.

Les objets `Future` (*futures*) représentent les résultats des *opérations asynchrones* — traitement ou E/S à compléter plus tard.

Nous pouvons créer un future simplement comme ceci :

```
Future future = Future();
```

définissons une fonction appelée `f` :

```
String f() => 'le travail est terminé !';
```

et passons-la au future :

```
Future<String> future = Future(f);
```

*Remarquez que le future prend le même type que le type de retour de la fonction `f`, soit `String`.*

Pour les besoins de ce tutoriel, nous avons passé une fonction qui retourne simplement une chaîne. Cela crée un future contenant le résultat de l'appel de `f` de manière asynchrone avec `Timer.run`.

Si le résultat de l'exécution de `f` lance une erreur, le future retourné est complété avec l'erreur.

Si la valeur retournée est elle-même un `Future`, la complétion du future créé attendra que le future retourné se complète, puis se complétera avec le même résultat.

Si une valeur non-future est retournée, le future retourné est complété avec cette valeur.

#### then

appelons `then` sur le future et passons une fonction qui prend la sortie de l'opération asynchrone comme argument

```
future.then((String val) => print(val)); // le travail est terminé
```

nous pouvons le simplifier en passant uniquement la fonction `print` car elle prend une chaîne

```
future.then(print); // le travail est terminé
```

### Gestion des erreurs

Pour attraper les erreurs, utilisez des expressions try-catch dans les fonctions asynchrones (ou utilisez `catchError()`).

#### `catchError`

imaginons que notre future lance une erreur à un moment donné :

```
Future future = Future(() => throw Error());
```

Si nous appelons `then` sur le future sans gérer l'erreur, il lancera l'erreur et arrêtera l'exécution de notre programme :

```
future.then(print); // Erreur : Error: Instance of 'Error'
```

Définissons une fonction qui prend une erreur et la gère :

```
void handleError(err) { print('$err a été géré');}
```

ensuite, ajoutons `catchError()` au future et passons `handleError` :

```
future.then(print).catchError(handleError); // Erreur : Error: Instance of 'Error' a été géré
```

De cette manière, l'erreur est gérée et le programme continue de s'exécuter.

#### Async, Await

Pour suspendre l'exécution jusqu'à ce qu'un future se complète, utilisez `await` dans une fonction async (ou utilisez `then()`).

Pour utiliser le mot-clé `await`, il doit être à l'intérieur d'une fonction `async` comme ceci :

```
main() async { Future future = Future(() => 'le travail est terminé'); String res = await future; print(res); // le travail est terminé}
```

*Remarquez que la fonction `main` est marquée avec le mot-clé `async`.*

Toute fonction marquée avec `async` est appelée de manière asynchrone.

Lorsque nous appelons un future avec le mot-clé `await`, l'exécution de la fonction est suspendue jusqu'à ce que le `future` retourne une valeur ou lance une erreur.

Nous pouvons gérer les erreurs des futures en utilisant un bloc `try`...`catch` :

```
main() async { Future future = Future(() => throw Error()); try {   print(await future);  } catch (e) {   print('$e a été géré'); // Instance of 'Error' a été géré }}
```

### Conclusion

* Le code Dart s'exécute dans un seul "thread" d'exécution.
* Le code qui bloque le thread d'exécution peut faire geler votre programme.
* Les objets `Future` (*futures*) représentent les résultats des *opérations asynchrones* — traitement ou E/S à compléter plus tard.
* Pour suspendre l'exécution jusqu'à ce qu'un future se complète, utilisez `await` dans une fonction async (ou utilisez `then()`).
* Pour attraper les erreurs, utilisez des expressions try-catch dans les fonctions async (ou utilisez `catchError()`).

Si vous pensez que j'ai oublié quelque chose ici, faites-le moi savoir, ou si vous avez une question quelconque, vous pouvez me joindre sur [twitter](https://twitter.com/4msal4).

[Abonnez-vous à ma newsletter](https://tinyletter.com/nimreycode) !

### Autres ressources utiles

[Programmation asynchrone : Futures](https://www.dartlang.org/tutorials/language/futures)