---
title: La pile d'appels JavaScript - Qu'est-ce que c'est et pourquoi est-elle nécessaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T07:12:22.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-javascript-call-stack-861e41ae61d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-WOpjPy_2Idl4jIAzPokRQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: La pile d'appels JavaScript - Qu'est-ce que c'est et pourquoi est-elle
  nécessaire
seo_desc: 'By Charles Freeborn

  The JavaScript engine (which is found in a hosting environment like the browser),
  is a single-threaded interpreter comprising of a heap and a single call stack. The
  browser provides web APIs like the DOM, AJAX, and Timers.

  This ar...'
---

Par Charles Freeborn

Le moteur JavaScript (que l'on trouve dans un environnement hôte comme le navigateur) est un interpréteur monothread composé d'un tas et d'une seule pile d'appels. Le navigateur fournit des API web comme le DOM, AJAX et les Timers.

Cet article vise à expliquer ce qu'est la pile d'appels et pourquoi elle est nécessaire. Une compréhension de la pile d'appels donnera de la clarté sur le fonctionnement de la "hiérarchie des fonctions et de l'ordre d'exécution" dans le moteur JavaScript.

La pile d'appels est principalement utilisée pour l'invocation de fonctions (appel). Puisque la pile d'appels est unique, l'exécution des fonctions se fait une à la fois, de haut en bas. Cela signifie que la pile d'appels est synchrone.

La compréhension de la pile d'appels est vitale pour la programmation asynchrone (que nous examinerons dans un article ultérieur).

En JavaScript asynchrone, nous avons une fonction de rappel, une boucle d'événements et une file d'attente de tâches. La fonction de rappel est traitée par la pile d'appels pendant l'exécution après que la fonction de rappel a été poussée dans la pile par la boucle d'événements.

Mais avant de nous précipiter, essayons d'abord de répondre à la question - Qu'est-ce que la pile d'appels ?

Au niveau le plus basique, une pile d'appels est une structure de données qui utilise le principe Last In, First Out (LIFO) pour stocker et gérer temporairement l'invocation de fonctions (appel).

Décomposons notre définition :

**LIFO** : Lorsque nous disons que la pile d'appels fonctionne selon le principe de la structure de données Last In, First Out, cela signifie que la dernière fonction qui est poussée dans la pile est la première à être retirée, lorsque la fonction retourne.

Prenons un exemple de code pour démontrer le LIFO en imprimant une erreur de trace de pile dans la console.

```js
function firstFunction(){
  throw new Error('Stack Trace Error');
}

function secondFunction(){
  firstFunction();
}

function thirdFunction(){
  secondFunction();
}

thirdFunction();
```

Lorsque le code est exécuté, nous obtenons une erreur. Une pile est imprimée montrant comment les fonctions sont empilées les unes sur les autres. Jetez un coup d'œil au diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/zOINLHPC8E56ac8yyINYOFWeImsjM2Wk2rdU)
_Erreur de trace de pile_

Vous remarquerez que l'arrangement des fonctions en tant que pile commence avec la `firstFunction()` (qui est la dernière fonction à être entrée dans la pile et est retirée pour lancer l'erreur), suivie de la `secondFunction()`, puis de la `thirdFunction()` (qui est la première fonction à être poussée dans la pile lorsque le code est exécuté).

**Stockage temporaire** : Lorsqu'une fonction est invoquée (appelée), la fonction, ses paramètres et ses variables sont poussés dans la pile d'appels pour former un cadre de pile. Ce cadre de pile est un emplacement mémoire dans la pile. La mémoire est effacée lorsque la fonction retourne, car elle est retirée de la pile.

![Image](https://cdn-media-1.freecodecamp.org/images/QgR2uIk7tW0YNz0Xm8g0jAPeRFI0e4sCejsv)
_Crédit image : [CMU](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html" rel="noopener" target="_blank" title=")_

**Gérer l'invocation de fonctions (appel)** : La pile d'appels maintient un enregistrement de la position de chaque cadre de pile. Elle sait quelle est la prochaine fonction à être exécutée (et la supprimera après exécution). C'est ce qui rend l'exécution du code en JavaScript synchrone.

Imaginez-vous debout dans une file d'attente, à un point de caisse d'une épicerie. Vous ne pouvez être servi qu'après que la personne devant vous ait été servie. C'est synchrone.

C'est ce que nous entendons par "gérer l'invocation de fonctions".

### **Comment la pile d'appels gère-t-elle les appels de fonctions ?**

Nous répondrons à cette question en examinant un exemple de code d'une fonction qui appelle une autre fonction. Voici l'exemple de code :

```js
function firstFunction(){
  console.log("Hello from firstFunction");
}

function secondFunction(){
  firstFunction();
  console.log("The end from secondFunction");
}

secondFunction();
```

![Image](https://cdn-media-1.freecodecamp.org/images/oEp65Ec9CD4CnL7t0uSPoyzrkA1i1BR-Ij1n)
_Voici la sortie_

Voici ce qui se passe lorsque le code est exécuté :

1. Lorsque `secondFunction()` est exécutée, un cadre de pile vide est créé. C'est le point d'entrée principal (anonyme) du programme.  
2. `secondFunction()` appelle ensuite `firstFunction()` qui est poussée dans la pile.  
3. `firstFunction()` retourne et imprime "Hello from firstFunction" dans la console.  
4. `firstFunction()` est retirée de la pile.  
5. L'ordre d'exécution passe ensuite à `secondFunction()`.  
6. `secondFunction()` retourne et imprime "The end from secondFunction" dans la console.  
7. `secondFunction()` est retirée de la pile, libérant la mémoire.

### Qu'est-ce qui cause un débordement de pile ?

Un débordement de pile se produit lorsqu'il y a une fonction récursive (une fonction qui s'appelle elle-même) sans point de sortie. Le navigateur (environnement hôte) a un nombre maximum d'appels de pile qu'il peut accommoder avant de lancer une erreur de pile.

Voici un exemple :

```js
function callMyself(){
  callMyself();
}

callMyself();
```

La fonction `callMyself()` s'exécutera jusqu'à ce que le navigateur lance une erreur "Taille maximale d'appel dépassée". Et c'est un débordement de pile.

![Image](https://cdn-media-1.freecodecamp.org/images/lvjT-ud6XfVQ5KYVWxZZWkKeVTgtJqFD0pWv)
_Erreur de pile d'appels maximale_

### En résumé

Les points clés à retenir de la pile d'appels sont :  
1. Elle est monothread. Cela signifie qu'elle ne peut faire qu'une seule chose à la fois.  
2. L'exécution du code est synchrone.  
3. Une invocation de fonction crée un cadre de pile qui occupe une mémoire temporaire.  
4. Elle fonctionne comme une structure de données LIFO - Last In, First Out.

Nous avons utilisé l'article sur la pile d'appels pour poser les bases d'une série que nous examinerons sur le JavaScript asynchrone (que nous examinerons dans un autre article).

Tous les exemples de code peuvent être trouvés dans ce dépôt GitHub [repo](https://github.com/charlesfreeborn/JS-CallStack-CodeSamples/blob/master/codesamples.md).

_Merci d'avoir lu. Si cet article vous a été utile, veuillez lui donner quelques applaudissements ? afin que d'autres puissent le trouver. J'aimerais aussi lire vos commentaires._