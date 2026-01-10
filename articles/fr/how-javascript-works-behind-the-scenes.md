---
title: Comment fonctionne JavaScript en coulisses ? Moteur JS et Runtime expliqués
subtitle: ''
author: Esther Christopher
co_authors: []
series: null
date: '2023-05-30T18:41:00.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-works-behind-the-scenes
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/CFF8A164-D6C4-4A88-85F2-388E83A2E3E7.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne JavaScript en coulisses ? Moteur JS et Runtime expliqués
seo_desc: "So you may know that your code somehow compiles and executes in your browser\
  \ to display the beautiful web application you’ve built. But are you aware of all\
  \ the components that come into play to enable the output? \nLet’s dive a little\
  \ into JavaScript..."
---

Vous savez peut-être que votre code est compilé et exécuté d'une manière ou d'une autre dans votre navigateur pour afficher la belle application web que vous avez construite. Mais êtes-vous conscient de tous les composants qui entrent en jeu pour permettre ce résultat ?

Plongeons un peu dans JavaScript en coulisses. La partie abstraite que vous ne pouvez pas exactement voir.

Pourquoi un sujet apparemment abstrait devrait-il vous importer ? Une compréhension du fonctionnement interne de JavaScript vous permet d'explorer le langage au-delà du niveau de surface et d'une perspective plus profonde.

Cela fournit des informations contextuelles sur le langage et la manière dont le moteur JavaScript optimise le code. Cela vous donnera quelques connaissances fondamentales importantes qui façonnent la manière dont vous écrivez du code. Cela vous aide également à écrire un code plus efficace, évolutif et maintenable.

## Le Moteur JavaScript

![Image](https://www.freecodecamp.org/news/content/images/2023/05/09BA18A6-3F7A-4DBE-AA43-C482725CA5E4.jpeg)
_Moteur JavaScript montrant la pile d'appels et le tas_

Le moteur JavaScript est simplement un programme informatique qui interprète le code JavaScript. Le moteur est responsable de l'exécution du code.

Chaque navigateur majeur possède un moteur JavaScript qui exécute le code JavaScript. Le plus populaire est le moteur [V8](https://en.wikipedia.org/wiki/JavaScript_engine) de Google Chrome. Le V8 de Google alimente Google Chrome et [Node.js](https://nodejs.org/en/docs), un environnement d'exécution JavaScript côté serveur utilisé pour construire des applications côté serveur.

D'autres moteurs de navigateurs majeurs incluent :

* SpiderMonkey développé par Mozilla pour Firefox
* JavaScriptCore qui alimente le navigateur Safari
* Chakra qui alimente Internet Explorer

Tout moteur JavaScript contient typiquement une pile d'appels et un tas. La pile d'appels est l'endroit où le code est exécuté. Le tas est une mémoire non structurée qui stocke tous les objets nécessaires pour l'application.

Puisque le processeur de l'ordinateur ne comprend que le binaire, des 0 et des 1, le code doit être traduit en 0 et 1.

Lorsque qu'un extrait de code passe dans le moteur, le code est initialement analysé, c'est-à-dire lu. Le code est ensuite analysé en une structure de données appelée l'arbre de syntaxe abstraite (AST). L'arbre résultant est ensuite utilisé pour créer des codes machine.

L'exécution se fait dans la pile d'appels du moteur JavaScript en utilisant le contexte d'exécution. C'est l'environnement où le code JavaScript est exécuté.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/FA4EDBD9-0348-4445-B795-8D1FEF904CBE.jpeg)
_Une illustration de diagramme montrant le processus d'exécution JavaScript_

## Le Runtime JavaScript

Pensez au runtime JavaScript comme à la maison qui englobe tous les composants nécessaires pour exécuter JavaScript. Cette maison comprend le moteur JavaScript, les Web APIs et la file d'attente de rappels.

Les Web APIs sont des fonctionnalités qui sont fournies au moteur mais ne font pas partie du langage JavaScript. Elles sont accessibles au moteur via le navigateur et aident à accéder aux données ou à améliorer la fonctionnalité du navigateur. Des exemples sont le Document Object Model (DOM) et les Fetch APIs.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/CDFBBA53-5533-478E-91CE-5904714E1043.jpeg)
_Un diagramme du Runtime JavaScript dans le navigateur contenant le moteur JavaScript, les Web APIs et la file d'attente de rappels_

La file d'attente de rappels inclut les fonctions de rappel qui sont prêtes à être exécutées. La file d'attente de rappels garantit que les rappels sont exécutés selon la méthode Premier Entré, Premier Sorti (FIFO) et ils sont passés dans la pile lorsqu'elle est vide.

Le runtime du navigateur et Node.js sont des exemples d'environnements d'exécution.

Lorsque JavaScript s'exécute dans un navigateur web, il fonctionne dans l'environnement d'exécution du navigateur. L'environnement d'exécution du navigateur fournit l'accès au DOM qui permet l'interaction avec les éléments de la page web, la gestion des événements et la manipulation de la structure de la page.

Node.js fournit un environnement d'exécution côté serveur pour exécuter JavaScript en dehors du navigateur. Parce qu'il exécute JavaScript en dehors du navigateur, il n'a pas accès aux Web APIs. À la place, l'environnement d'exécution de Node.js le remplace par ce qu'on appelle les liaisons C++ et le pool de threads.

## Stratégies d'optimisation de JavaScript

Les moteurs JavaScript modernes ont mis en place certaines stratégies d'optimisation pour améliorer les performances de l'exécution du code. Ces optimisations se produisent dynamiquement pendant le processus d'exécution. Examinons quelques-unes de ces stratégies.

### Compilation Just-in-Time

Le processus qui implique la traduction du code JavaScript en code machine se fait en utilisant la compilation et l'interprétation.

Dans la compilation, l'ensemble du code source est converti en code machine en une seule fois et écrit dans un fichier binaire pour être exécuté par l'ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/EB039874-52DC-4CD8-B95C-F9E75F2D2283_4_5005_c.jpeg)
_Un diagramme montrant le processus de compilation du code_

En revanche, lors de l'interprétation, l'interpréteur parcourt le code source et l'interprète ligne par ligne, exécutant chaque ligne lorsqu'il la rencontre.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/D3DC97A6-3D79-46E0-A2F2-BB3FA694F0EF_4_5005_c.jpeg)
_Un diagramme montrant le processus d'interprétation du code_

JavaScript était autrefois un langage interprété, mais les langages interprétés sont plus lents comparés aux langages compilés.

Afin d'optimiser les performances des applications web, JavaScript combine à la fois la compilation et l'interprétation. Cela s'appelle la compilation Just-in-Time. Cette méthode compile l'ensemble du code en code machine en une seule fois et l'exécute.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/E2BA4399-5F52-408C-B2AB-A9E6F74B3238_4_5005_c.jpeg)
_Un diagramme montrant la compilation Just-in-Time du code_

La compilation Just-in-Time implique les mêmes deux processus que la compilation régulière, mais ici le code machine n'est pas écrit dans un fichier binaire. Le code est également exécuté immédiatement après la compilation.

Cela a eu un impact significatif sur la vitesse d'exécution du code en JavaScript. Donc, espérons que cela aide à dissiper l'idée que JavaScript est un langage purement interprété.

Pour optimiser pleinement le code JavaScript, le moteur crée d'abord une version non optimisée du code machine afin qu'il puisse commencer à s'exécuter immédiatement. Pendant ce temps, le code est réoptimisé et recompilé en arrière-plan de l'exécution du programme en cours. Cela est fait plusieurs fois pour produire la version finale, la plus optimisée.

Le processus d'analyse, de compilation et d'exécution se produit dans un thread spécial du moteur qui ne peut pas être accessible depuis le code.

### Qu'est-ce que l'inlining ?

L'inlining est une autre technique d'optimisation que JavaScript utilise pour améliorer les performances et la vitesse.

```js
function add(a, b) {
  return a + b;
}

let result = 0;
result = result + 5;
result = result + 3;

console.log(result); //
```

Dans cet extrait, la fonction `add()` originale n'est pas appelée directement. Au lieu de cela, le code à l'intérieur de la fonction `return a + b;` est inséré à l'endroit de l'appel.

Cette optimisation est faite surtout pour les fonctions qui sont appelées répétitivement. Le moteur JavaScript exécutera la fonction comme il le ferait normalement. Mais à mesure que la fonction est appelée souvent, le moteur remplace l'appel de fonction par le code réel de la fonction à l'endroit de l'appel. Cela aide à prévenir plusieurs appels de fonction et améliore les performances.

### Considérations de performance

Plusieurs facteurs affectent la performance de votre application web. Alors que le moteur JavaScript emploie certaines stratégies pour assurer l'optimisation, il y a aussi certaines meilleures pratiques à prendre en considération par les développeurs pour une exécution efficace.

Des techniques telles que la minimisation de la manipulation du DOM et la réduction des appels de fonction améliorent la performance du code.

L'accès fréquent et l'interaction avec le DOM ralentissent le rendu des pages web et contribuent au lag de performance. Puisque vous ne pouvez pas éviter complètement d'interagir avec le DOM, vous pouvez minimiser l'interaction en regroupant les mises à jour du DOM pour réduire les frais généraux.

De plus, la réduction des appels de fonction améliore la performance. En réduisant les appels de fonction, vous rationalisez votre code et le rendez plus efficace, rendant vos applications JavaScript plus rapides et plus réactives.

```js
// Code inefficace avec des appels de fonction inutiles
function calculateTotal(a, b, c) {
  return addNumbers(a, b) + multiplyNumbers(c, b);
}
function addNumbers(x, y) {
  return x + y;
}
function multiplyNumbers(x, y) {
  return x * y;
}
// Code amélioré avec des appels de fonction réduits
function calculateTotal(a, b, c) {
  const sum = a + b;
  return sum + c * b;
}
console.log(calculateTotal(2, 3, 4)); // Sortie : 23
```

Dans le code inefficace, la fonction `calculateTotal()` fait des appels de fonction séparés à `addNumbers()` et `multiplyNumbers()`. Cela cause des frais généraux d'appel de fonction.

Dans le code amélioré, les appels de fonction sont réduits en effectuant directement les opérations d'addition et de multiplication dans la fonction `calculateTotal()`. En réduisant les appels de fonction, le code devient plus efficace et améliore la vitesse d'exécution.

## Développements et tendances futurs de JavaScript

Il continuera d'y avoir des améliorations et des avancées dans les moteurs JavaScript et les environnements d'exécution. Ces changements sont orientés vers l'amélioration des performances des applications web.

Une telle avancée est l'essor de [WebAssembly](https://webassembly.org/). WebAssembly apporte des performances quasi natives aux applications web et supporte plusieurs langages. Il ouvre de nouvelles possibilités pour l'optimisation des performances et la vitesse d'exécution.

Il est important pour les développeurs JavaScript de rester à jour avec ces tendances et d'adapter les nouvelles meilleures pratiques de codage en conséquence.

## Conclusion

De nombreux processus sont impliqués dans la manière dont votre code JavaScript est analysé jusqu'à ce qu'il rende une application web fonctionnelle.

Cet article fournit un aperçu de haut niveau des principaux concepts. Il explique comment le moteur JavaScript exécute le code, le runtime et ses composants. Il explique également les stratégies d'optimisation et met en évidence les considérations de performance.

Comprendre comment JavaScript fonctionne en coulisses façonne la manière dont les développeurs abordent les problèmes et écrivent des codes plus efficaces. Cela les aide également à rester en avance sur la courbe d'apprentissage et à s'adapter facilement aux changements futurs des fonctionnalités de JavaScript.

Pour un apprentissage plus approfondi, vous pouvez visiter ces ressources :

* [Contexte d'exécution](https://www.freecodecamp.org/news/execution-context-how-javascript-works-behind-the-scenes/)
* [Boucle d'événements](https://www.freecodecamp.org/news/javascript-concurrency-model-and-event-loop/)
* [File d'attente des micro-tâches](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)

Si vous avez aimé lire cet article, alors connectez-vous avec moi sur [Twitter](https://twitter.com/thedocsgirl) et [LinkedIn](https://www.linkedin.com/in/esther-christopher-a0909419b) où je partage mes connaissances.