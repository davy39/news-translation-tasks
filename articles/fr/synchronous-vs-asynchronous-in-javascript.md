---
title: JavaScript Synthrone vs Asynchrone – Pile d'Appels, Promesses, et Plus
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-09-13T21:00:57.000Z'
originalURL: https://freecodecamp.org/news/synchronous-vs-asynchronous-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/freeCodeCamp-Cover-2.png
tags:
- name: asynchronous
  slug: asynchronous
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: Web Development
  slug: web-development
seo_title: JavaScript Synthrone vs Asynchrone – Pile d'Appels, Promesses, et Plus
seo_desc: 'Let me start this article by asking, "What is JavaScript"? Well, here''s
  the most confusing yet to-the-point answer I have found so far:


  JavaScript is a single-threaded, non-blocking, asynchronous, concurrent programming
  language with lots of flexibi...'
---

Commençons cet article par une question : "Qu'est-ce que JavaScript" ? Voici la réponse la plus confuse mais précise que j'ai trouvée jusqu'à présent :

> JavaScript est un langage de programmation mono-thread, non bloquant, asynchrone et concurrent avec beaucoup de flexibilité.

Attendez une seconde – a-t-il dit mono-thread et asynchrone en même temps ? Si vous comprenez ce que signifie mono-thread, vous l'associez probablement principalement à des opérations synchrones. Comment JavaScript peut-il être asynchrone, alors ?

Dans cet article, nous allons tout apprendre sur les parties synchrones et asynchrones de JavaScript. Vous utilisez les deux presque quotidiennement en programmation web. 

Si vous aimez aussi apprendre à partir de contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : [1;34m

%[https://www.youtube.com/watch?v=pIjfzjsoVw4]

# Dans cet article, vous apprendrez :

* Comment JavaScript est synchrone.
* Comment les opérations asynchrones se produisent lorsque JavaScript est mono-thread.
* Comment comprendre synchrone vs asynchrone vous aide à mieux comprendre les promesses JavaScript.
* Beaucoup d'exemples simples mais puissants pour couvrir ces concepts en détail.

# Les Fonctions JavaScript sont des Citoyens de Première Classe

En JavaScript, vous pouvez créer et modifier une fonction, l'utiliser comme argument, la retourner depuis une autre fonction et l'assigner à une variable. Toutes ces capacités nous permettent d'utiliser des fonctions partout pour placer un ensemble de code logiquement.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/block-function.png)
_Lignes de code organisées en fonctions logiquement_

Nous devons dire au moteur JavaScript d'exécuter les fonctions en les invoquant. Cela ressemblera à ceci :

```js
// Définir une fonction
function f1() {
    // Faire quelque chose
    // Faire quelque chose encore
    // Encore
    // Et ainsi de suite...
}

// Invoquer la fonction
f1();
```

Par défaut, chaque ligne dans une fonction s'exécute séquentiellement, une ligne à la fois. La même chose est applicable même lorsque vous invoquez plusieurs fonctions dans votre code. Encore une fois, ligne par ligne.

# JavaScript Synchrone – Comment la Pile d'Exécution des Fonctions Fonctionne

Alors, que se passe-t-il lorsque vous définissez une fonction et que vous l'invoquez ? Le moteur JavaScript maintient une structure de données `pile` appelée `pile d'exécution des fonctions`. Le but de la pile est de suivre la fonction actuelle en cours d'exécution. Elle fait ce qui suit :

* Lorsque le moteur JavaScript invoque une fonction, il l'ajoute à la pile, et l'exécution commence.
* Si la fonction actuellement exécutée appelle une autre fonction, le moteur ajoute la deuxième fonction à la pile et commence à l'exécuter.
* Une fois qu'il a terminé l'exécution de la deuxième fonction, le moteur la retire de la pile.
* Le contrôle revient pour reprendre l'exécution de la première fonction à partir du point où elle l'avait laissée la dernière fois.
* Une fois l'exécution de la première fonction terminée, le moteur la retire de la pile.
* Continuer de la même manière jusqu'à ce qu'il n'y ait plus rien à mettre dans la pile.

La pile d'exécution des fonctions est également connue sous le nom de `Pile d'Appels`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/stack.png)
_Pile d'Exécution des Fonctions_

Regardons un exemple de trois fonctions qui s'exécutent une par une :

```js
function f1() {
  // du code
}
function f2() {
  // du code
}
function f3() {
  // du code
}

// Invoquer les fonctions une par une
f1();
f2();
f3();
```

Maintenant, voyons ce qui se passe avec la pile d'exécution des fonctions :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/first-flow.gif)
_Un flux étape par étape montre l'ordre d'exécution_

Avez-vous vu ce qui s'est passé là ? D'abord, `f1()` entre dans la pile, s'exécute et en sort. Ensuite, `f2()` fait de même, et enfin `f3()`. Après cela, la pile est vide, sans rien d'autre à exécuter.

D'accord, travaillons maintenant sur un exemple plus complexe. Voici une fonction `f3()` qui invoque une autre fonction `f2()` qui à son tour invoque une autre fonction `f1()`.

```js
function f1() {
  // Du code
}
function f2() {
  f1();
}
function f3() {
  f2();
}
f3();
```

Voyons ce qui se passe avec la pile d'exécution des fonctions :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/second-flow.gif)
_Un flux étape par étape montre l'ordre d'exécution_

Remarquez que d'abord `f3()` entre dans la pile, invoquant une autre fonction, `f2()`. Donc maintenant `f2()` entre dans la pile tandis que `f3()` reste dans la pile. La fonction `f2()` invoque `f1()`. Donc, c'est le moment pour `f1()` d'entrer dans la pile avec `f2()` et `f3()` restant à l'intérieur.

D'abord, `f1()` finit de s'exécuter et sort de la pile. Juste après cela, `f2()` finit, et enfin `f3()`.

Le point essentiel est que tout ce qui se passe à l'intérieur de la `pile d'exécution des fonctions` est séquentiel. C'est la partie `Synchrone` de JavaScript. Le thread `principal` de JavaScript s'assure qu'il prend soin de tout dans la pile avant de commencer à regarder ailleurs.

Super ! Maintenant que nous comprenons comment les opérations `synchrones` fonctionnent en JavaScript, retournons la pièce et voyons son côté `asynchrone`. Êtes-vous prêt ?

# JavaScript Asynchrone – Comment les API du Navigateur et les Promesses Fonctionnent

Le mot `asynchrone` signifie **ne se produisant pas au même moment**. Que signifie-t-il dans le contexte de JavaScript ? 

Typiquement, exécuter les choses en séquence fonctionne bien. Mais vous pouvez parfois avoir besoin de récupérer des données depuis le serveur ou d'exécuter une fonction avec un délai, quelque chose que vous ne prévoyez pas se produire `MAINTENANT`. Donc, vous voulez que le code s'exécute `asynchrone`.

Dans ces circonstances, vous ne voulez peut-être pas que le moteur JavaScript arrête l'exécution des autres codes séquentiels. Donc, le moteur JavaScript doit gérer les choses un peu plus efficacement dans ce cas.

Nous pouvons classer la plupart des opérations JavaScript asynchrones avec deux déclencheurs principaux :

1. **Événements ou fonctions d'API de Navigateur/Web API**. Cela inclut des méthodes comme `setTimeout`, ou des gestionnaires d'événements comme click, mouse over, scroll, et bien d'autres.
2. **Promesses**. Un objet JavaScript unique qui nous permet d'effectuer des opérations asynchrones.

Ne vous inquiétez pas si vous êtes nouveau dans les promesses. Vous n'avez pas besoin d'en savoir plus que cela pour suivre cet article. À la fin de l'article, j'ai fourni quelques liens pour que vous puissiez commencer à apprendre les promesses de la manière la plus adaptée aux débutants.

## Comment Gérer les API de Navigateur/Web API

Les API de navigateur comme `setTimeout` et les gestionnaires d'événements reposent sur des fonctions de `rappel`. Une fonction de rappel s'exécute lorsqu'une opération asynchrone est terminée. Voici un exemple de fonctionnement d'une fonction `setTimeout` :

```js
function printMe() {
  console.log('print me');
}

setTimeout(printMe, 2000);
```

La fonction `setTimeout` exécute une fonction après qu'un certain temps se soit écoulé. Dans le code ci-dessus, le texte `print me` est enregistré dans la console après un délai de 2 secondes.

Maintenant, supposons que nous avons quelques lignes de code supplémentaires juste après la fonction `setTimeout` comme ceci :

```js
function printMe() {
  console.log('print me');
}

function test() {
  console.log('test');
}

setTimeout(printMe, 2000);
test();

```

Alors, que devons-nous attendre ici ? Que pensez-vous que sera la sortie ?

Le moteur JavaScript attendra-t-il 2 secondes pour passer à l'invocation de la fonction `test()` et produire ceci :

```shell
printMe
test
```

Ou parviendra-t-il à mettre de côté la fonction de rappel de `setTimeout` et à continuer ses autres exécutions ? Donc la sortie pourrait être ceci, peut-être :

```shell
test
printMe
```

 Si vous avez deviné la dernière option, vous avez raison. C'est là que le mécanisme asynchrone entre en jeu.

## Comment Fonctionne la File d'Attente des Rappels JavaScript (aka Task Queue)

JavaScript maintient une file d'attente de fonctions de rappel. Elle est appelée une file d'attente de rappels ou une file d'attente de tâches. Une structure de données de file d'attente est `Premier Entré, Premier Sorti (FIFO)`. Donc, la fonction de rappel qui entre en premier dans la file d'attente a l'opportunité de sortir en premier. Mais la question est :

* Quand le moteur JavaScript la met-il dans la file d'attente ?
* Quand le moteur JavaScript la retire-t-il de la file d'attente ?
* Où va-t-elle quand elle sort de la file d'attente ?
* Plus important encore, comment toutes ces choses se rapportent-elles à la partie asynchrone de JavaScript ?

Whoa, beaucoup de questions ! Trouvons les réponses à l'aide de l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/taskQ.png)

L'image ci-dessus montre la `pile d'appels` régulière que nous avons déjà vue. Il y a deux sections supplémentaires pour suivre si une API de navigateur (comme setTimeout) entre en jeu et met en `file d'attente` la fonction de rappel de cette API.

Le moteur JavaScript continue d'exécuter les fonctions dans la pile d'appels. Comme il ne met pas la fonction de rappel directement dans la pile, il n'y a pas de question de code attendant/bloquant l'exécution dans la pile.

Le moteur crée une `boucle` pour regarder périodiquement dans la file d'attente afin de trouver ce qu'il doit en tirer. Il tire une fonction de rappel de la file d'attente vers la pile d'appels lorsque la pile est vide. Maintenant, la fonction de rappel s'exécute généralement comme toute autre fonction dans la pile. La boucle continue. Cette boucle est célèbre sous le nom de `Boucle d'Événements`.

Donc, la morale de l'histoire est :

* Lorsqu'une API de navigateur se produit, parquez les fonctions de rappel dans une file d'attente.
* Continuez à exécuter le code comme d'habitude dans la pile.
* La boucle d'événements vérifie s'il y a une fonction de rappel dans la file d'attente.
* Si oui, tirez la fonction de rappel de la file d'attente vers la pile et exécutez-la.
* Continuez la boucle.

D'accord, voyons comment cela fonctionne avec le code ci-dessous :

```js
function f1() {
    console.log('f1');
}

function f2() {
    console.log('f2');
}

function main() {
    console.log('main');
    
    setTimeout(f1, 0);
    
    f2();
}

main();
```

Le code exécute une fonction `setTimeout` avec une fonction de rappel `f1()`. Notez que nous lui avons donné un délai de zéro. Cela signifie que nous nous attendons à ce que la fonction `f1()` s'exécute immédiatement. Juste après setTimeout, nous exécutons une autre fonction, `f2()`.

Alors, que pensez-vous que sera la sortie ? La voici :

```shell
main
f2
f1
```

Mais, vous pouvez penser que `f1` devrait s'imprimer avant `f2` puisque nous ne retardons pas l'exécution de f1. Mais non, ce n'est pas le cas. Souvenez-vous du mécanisme de la `boucle d'événements` dont nous avons parlé plus haut ? Maintenant, voyons-le dans un flux étape par étape pour le code ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/third-flow.gif)
_Boucle d'événements - voir l'exécution étape par étape_

Voici les étapes écrites :

1. La fonction `main()` entre dans la pile d'appels.
2. Elle a une console log pour imprimer le mot main. Le `console.log('main')` s'exécute et sort de la pile.
3. L'API de navigateur setTimeout prend place.
4. La fonction de rappel la met dans la file d'attente de rappels.
5. Dans la pile, l'exécution se fait comme d'habitude, donc `f2()` entre dans la pile. La console log de `f2()` s'exécute. Les deux sortent de la pile.
6. Le `main()` sort également de la pile.
7. La boucle d'événements reconnaît que la pile d'appels est vide et qu'il y a une fonction de rappel dans la file d'attente.
8. La fonction de rappel `f1()` entre alors dans la pile. L'exécution commence. La console log s'exécute et `f1()` sort également de la pile.
9. À ce stade, il n'y a plus rien dans la pile et la file d'attente à exécuter.

J'espère que c'est maintenant clair pour vous comment la partie `asynchrone` de JavaScript fonctionne en interne. Mais ce n'est pas tout. Nous devons examiner les `promesses`.

## Comment le Moteur JavaScript Gère les Promesses

En JavaScript, les promesses sont des objets spéciaux qui vous aident à effectuer des opérations asynchrones. 

Vous pouvez créer une promesse en utilisant le constructeur `Promise`. Vous devez lui passer une fonction `executor`. Dans la fonction executor, vous définissez ce que vous voulez faire lorsqu'une promesse retourne avec succès ou lorsqu'elle lance une erreur. Vous pouvez faire cela en appelant les méthodes `resolve` et `reject`, respectivement.

Voici un exemple de promesse en JavaScript :

```js
const promise = new Promise((resolve, reject) =>
        resolve('I am a resolved promise');
);
```

Après l'exécution de la promesse, nous pouvons gérer le résultat en utilisant la méthode `.then()` et les erreurs avec la méthode `.catch()`.

```js
promise.then(result => console.log(result))
```

Vous utilisez des promesses chaque fois que vous utilisez la méthode `fetch()` pour obtenir des données depuis un magasin. 

Le point ici est que le moteur JavaScript n'utilise pas la même `file d'attente de rappels` que nous avons vue précédemment pour les API de navigateur. Il utilise une autre file d'attente spéciale appelée `File d'Attente de Tâches`.

## Qu'est-ce que la File d'Attente de Tâches en JavaScript ?

Chaque fois qu'une promesse se produit dans le code, la fonction executor entre dans la file d'attente de tâches. La boucle d'événements fonctionne, comme d'habitude, pour regarder dans les files d'attente mais donne la priorité aux éléments de la `file d'attente de tâches` sur les éléments de la `file d'attente de rappels` lorsque la `pile` est libre. 

L'élément dans la file d'attente de rappels est appelé une `macro tâche`, tandis que l'élément dans la file d'attente de tâches est appelé une `micro tâche`.

Donc, le flux entier se déroule comme suit :

* Pour chaque boucle de la `boucle d'événements`, une tâche est complétée à partir de la `file d'attente de rappels`.
* Une fois cette tâche terminée, la boucle d'événements visite la `file d'attente de tâches`. Elle complète toutes les `micro tâches` dans la file d'attente de tâches avant de regarder la prochaine chose.
* Si les deux files d'attente ont des entrées au même moment, la `file d'attente de tâches` obtient la préférence sur la `file d'attente de rappels`.

L'image ci-dessous montre l'inclusion de la file d'attente de tâches avec les autres éléments préexistants.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/JObQ.png)

Maintenant, regardons un exemple pour mieux comprendre cette séquence :

```js
function f1() {
    console.log('f1');
}

function f2() {
    console.log('f2');
}

function main() {
    console.log('main');
    
    setTimeout(f1, 0);
    
    new Promise((resolve, reject) =>
        resolve('I am a promise')
    ).then(resolve => console.log(resolve))
    
    f2();
}

main();
```

Dans le code ci-dessus, nous avons une fonction `setTimeout()` comme avant, mais nous avons introduit une promesse juste après. Maintenant, souvenez-vous de tout ce que nous avons appris et devinez la sortie.

Si votre réponse correspond à ceci, vous avez raison :

```shell
main
f2
I am a promise
f1
```

Maintenant, voyons le flux des actions :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fourth-flow.gif)
_File d'attente de rappels vs File d'attente de tâches_

Le flux est presque le même que ci-dessus, mais il est crucial de remarquer comment les éléments de la file d'attente de tâches priorisent les éléments de la file d'attente de tâches. Notez également qu'il n'a même pas d'importance si le `setTimeout` a un délai de zéro. Il s'agit toujours de la file d'attente de tâches qui vient avant la file d'attente de rappels.

D'accord, nous avons appris tout ce dont nous avons besoin pour comprendre l'exécution synchrone et asynchrone en JavaScript.

# Voici un Quiz pour Vous !

Testons votre compréhension en faisant un quiz. Devinez la sortie du code suivant et appliquez toutes les connaissances que nous avons acquises jusqu'à présent :

```js
function f1() {
 console.log('f1');
}

function f2() { 
    console.log('f2');
}

function f3() { 
    console.log('f3');
}

function main() {
  console.log('main');

  setTimeout(f1, 50);
  setTimeout(f3, 30);

  new Promise((resolve, reject) =>
    resolve('I am a Promise, right after f1 and f3! Really?')
  ).then(resolve => console.log(resolve));
    
  new Promise((resolve, reject) =>
    resolve('I am a Promise after Promise!')
  ).then(resolve => console.log(resolve));

  f2();
}

main();
```

Voici la sortie attendue :

```shell
main
f2
I am a Promise, right after f1 and f3! Really?
I am a Promise after Promise!
f3
f1
```

Vous voulez plus de quiz comme celui-ci ? [Rendez-vous sur ce dépôt](https://github.com/atapas/promise-interview-ready) pour pratiquer plus d'exercices.

Au cas où vous seriez bloqué ou auriez besoin de clarifications, mes DM sont toujours [ouverts sur Twitter](https://twitter.com/tapasadhikary).

# En Résumé

Pour résumer :

* Le moteur JavaScript utilise la structure de données de pile pour suivre les fonctions actuellement exécutées. La pile est appelée la pile d'exécution des fonctions.
* La pile d'exécution des fonctions (aka pile d'appels) exécute les fonctions séquentiellement, ligne par ligne, une par une.
* Les API du navigateur/web utilisent des fonctions de rappel pour compléter les tâches lorsqu'une opération asynchrone/délai est terminée. La fonction de rappel est placée dans la file d'attente de rappels.
* Les fonctions d'exécution des promesses sont placées dans la file d'attente de tâches.
* Pour chaque boucle de la boucle d'événements, une macro tâche est complétée à partir de la file d'attente de rappels.
* Une fois cette tâche terminée, la boucle d'événements visite la file d'attente de tâches. Elle complète toutes les micro-tâches dans la file d'attente de tâches avant de regarder la prochaine chose.
* Si les deux files d'attente ont des entrées au même moment, la file d'attente de tâches obtient la préférence sur la file d'attente de rappels.

# Avant de Terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article instructif et qu'il vous aide à mieux comprendre les concepts synchrones et asynchrones de JavaScript.

Restez en contact. Vous pouvez me suivre sur [Twitter(@tapasadhikary)](https://twitter.com/tapasadhikary), ma [chaîne YouTube](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), et [GitHub(atapas)](https://github.com/atapas).

Comme promis auparavant, voici quelques articles que vous pourriez trouver utiles,

* [JavaScript Promises - Explain Like I'm Five](https://blog.greenroots.info/javascript-promises-explain-like-i-am-five)
* [JavaScript Promise Chain - The art of handling promises](https://blog.greenroots.info/javascript-promise-chain-the-art-of-handling-promises)
* [JavaScript async and await - in plain English, please](https://blog.greenroots.info/javascript-async-and-await-in-plain-english-please)
* [Introducing PromiViz - visualize and learn JavaScript promise APIs](https://blog.greenroots.info/introducing-promiviz-visualize-and-learn-javascript-promise-apis)