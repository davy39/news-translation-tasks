---
title: Comment fonctionne la boucle d'événements (Event Loop) de Node.js
subtitle: ''
author: Amanda Ene Adoyi
co_authors: []
series: null
date: '2025-09-03T16:28:58.802Z'
originalURL: https://freecodecamp.org/news/how-the-nodejs-event-loop-works
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756916907320/01074df6-0f8e-4a63-9a3e-07c8297fc22b.png
tags:
- name: Node.js
  slug: nodejs
- name: Event Loop
  slug: event-loop
- name: asynchronous
  slug: asynchronous
- name: synchronous
  slug: synchronous
- name: concurrency
  slug: concurrency
- name: parallelism
  slug: parallelism
seo_title: Comment fonctionne la boucle d'événements (Event Loop) de Node.js
seo_desc: 'The Node.js event loop is a concept that may seem difficult to understand
  at first. But as with any seemingly complex subject, the best way to understand
  it is often through an analogy.

  In this article, you’ll learn how overworked managers, busy wait...'
---

La boucle d'événements (Event Loop) de Node.js est un concept qui peut sembler difficile à comprendre au premier abord. Mais comme pour tout sujet apparemment complexe, la meilleure façon de le comprendre est souvent de passer par une analogie.

Dans cet article, vous découvrirez comment des managers débordés, des serveurs occupés et des gares ferroviaires peuvent aider à assimiler le concept fondamental de la boucle d'événements. Si vous travaillez avec Node, vous devrez comprendre comment fonctionne la boucle d'événements, car elle est à la base de certaines des applications les plus puissantes d'aujourd'hui.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que le code synchrone et asynchrone ?](#heading-quest-ce-que-le-code-synchrone-et-asynchrone)
    
* [Ce que signifient la concurrence et le parallélisme](#heading-ce-que-signifient-la-concurrence-et-le-parallelisme)
    
    * [La concurrence dans Node.js](#heading-la-concurrence-dans-nodejs)
        
    * [Le parallélisme dans Node.js](#heading-le-parallelisme-dans-nodejs)
        
* [Qu'est-ce que la boucle d'événements ?](#heading-quest-ce-que-la-boucle-devenements)
    
* [Les phases de la boucle d'événements](#heading-les-phases-de-la-boucle-devenements)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre cet article sans difficulté, il serait utile que vous soyez familier avec les concepts suivants :

1. **Une compréhension de base de JavaScript :** Node.js fonctionne sur JavaScript, vous devrez donc comprendre les variables, les fonctions et le flux de contrôle.
    
2. **Une connaissance des bases de Node.js :** Exécuter des scripts simples avec Node et utiliser `require` pour les modules.
    
3. **Une certaine exposition aux modèles asynchrones :** Savoir ce que font des fonctions comme `setTimeout()`.
    
4. **Une certaine familiarité avec les concepts de base du CPU (cœurs et threads) :** Cela vous aidera à mieux comprendre la concurrence et le parallélisme.
    
5. **La connaissance des promesses et de async/await :** C'est optionnel et n'est pas une exigence stricte, mais cela sera utile.
    

## Qu'est-ce que le code synchrone et asynchrone ?

Lors de l'écriture de code pour les applications Node.js, il existe deux manières différentes de l'exécuter : synchrone (sync) et asynchrone (async). Le code synchrone est dit *bloquant* car lorsqu'il s'exécute, aucun autre code ne s'exécute tant que l'exécution n'est pas terminée.

Une analogie pour cela est un restaurant très fréquenté. Imaginez un serveur qui refuse de s'occuper d'autres tables tant que la table qu'il sert actuellement n'a pas reçu ses commandes et n'a pas commencé à manger. Pendant que la nourriture est en préparation, le serveur attend sans rien faire et ne s'approche de votre table pour prendre votre commande que lorsqu'il en a complètement fini avec la table précédente. Il va sans dire que le serveur risque de ne pas recevoir un gros pourboire pour ce service.

C'est ce qu'est le code synchrone. Il interrompt l'exécution des autres processus jusqu'à ce qu'il soit terminé. Vous pouvez voir comment cela fonctionne dans l'exemple ci-dessous :

```javascript
const syncWaiter = (name) => {
    console.log(`${name} s'occupe des tables assez lentement.`);
};

syncWaiter("Devin");
console.log("Au moins, toutes les commandes sont correctes !");
```

Le code ci-dessus sera exécuté en séquence, dans l'ordre où il apparaît.

Le code asynchrone, contrairement au code synchrone, n'interrompt pas tous les autres processus jusqu'à ce qu'une tâche soit exécutée – il procède plutôt à l'exécution d'autres tâches pendant qu'un processus plus long s'exécute en arrière-plan.

En reprenant notre analogie du serveur, dans ce cas, le serveur du restaurant irait prendre la commande d'une table, transmettrait la commande à la cuisine et, pendant qu'elle est en préparation, se rendrait à votre table pour prendre également votre commande. De cette façon, le serveur est en mesure de s'assurer que différents processus sont lancés même si un processus prend un peu plus de temps que les autres. Consultez l'exemple ci-dessous :

```javascript
const asyncWaiter = (name) => {
    setTimeout(()=> {console.log(`${name} s'occupe des tables assez rapidement.`)}, 3000)
};

asyncWaiter("James");
console.log("Wow ! Toutes les tables sont servies en peu de temps.");
```

Contrairement au code synchrone, ce code exécute bien la fonction `asyncWaiter()` – mais le callback à l'intérieur de la fonction s'exécute plus tard. Lorsque la durée s'est écoulée, le résultat est alors affiché à l'écran. C'est pourquoi les programmes asynchrones sont dits *non bloquants.* Ils n'interrompent pas le programme, mais passent d'une tâche disponible à une autre.

Le code ci-dessus renvoie ce qui suit :

```bash
Wow ! Toutes les tables sont servies en peu de temps.
James s'occupe des tables assez rapidement.
```

Cet ordre d'affichage se produit en raison de la façon dont la *boucle d'événements* gère les tâches : le `console.log()` synchrone qui vient après `asyncWaiter()` s'exécute immédiatement, tandis que le callback asynchrone à l'intérieur de `asyncWaiter()` (provenant de `setTimeout`) est programmé pour s'exécuter plus tard. Si vous ne comprenez pas encore cela, ne vous inquiétez pas, car je vais le détailler sous peu.

## Ce que signifient la concurrence et le parallélisme

Node.js est monothreadé (single-threaded) mais donne souvent l'apparence d'un environnement multithread en raison de la façon dont il gère la concurrence et le parallélisme. Un thread est une séquence unique d'instructions exécutées par le CPU de manière indépendante. Pensez-y comme à un serveur unique nommé James dans un restaurant.

Si James gère plusieurs tâches à peu près en même temps et rapidement, un observateur à l'extérieur du restaurant qui voit le nombre de clients entrer et sortir pourrait supposer qu'il y a une tonne de serveurs. En réalité, James gère simplement ses tâches de manière asynchrone.

Avant de saisir le concept de la boucle d'événements, il est bon de comprendre ce que sont la concurrence et le parallélisme, car ils aident à expliquer cela.

### La concurrence dans Node.js

La concurrence signifie que plusieurs processus s'exécutent à peu près en même temps. Dans l'analogie du serveur, c'est comme James effectuant différentes tâches, bien que pas simultanément. Il pourrait, par exemple, prendre la commande d'une table et, en attendant que la nourriture arrive, demander que du sel supplémentaire soit fourni à une autre table. Pendant que le sel est en route, il utilise le temps d'attente pour lire l'addition à une troisième table.

L'idée clé est que James ne reste jamais inactif — il travaille sur d'autres tâches en attendant qu'une se termine. Si cela ressemble beaucoup à de la programmation asynchrone, c'est parce que le code asynchrone n'est qu'un moyen d'atteindre la concurrence.

D'autres façons d'exécuter la concurrence sont le [multithreading](https://www.freecodecamp.org/news/multithreading-for-beginners/) sur un seul cœur de CPU et les [coroutines](https://www.freecodecamp.org/news/how-to-handle-concurrency-in-go/) qui sont simplement des fonctions qui suspendent leur exécution pour la reprendre ultérieurement.

### Le parallélisme dans Node.js

Le parallélisme, en revanche, signifie également que plusieurs tâches s'exécutent en même temps – mais au lieu que les tâches soient simplement traitées à peu près au même moment, elles sont exécutées exactement en même temps, simultanément. Dans ce cas, le gérant du restaurant décide d'embaucher plusieurs serveurs et chaque table a un serveur qui prend les commandes exactement au même moment.

Le parallélisme peut être atteint en utilisant le multithreading sur plusieurs cœurs de CPU. Dans cette configuration, les threads partagent la même mémoire et s'exécutent simultanément tout en utilisant des clusters qui s'exécutent indépendamment – chacun avec son propre espace mémoire. Voici un exemple clair de parallélisme utilisant le module `worker_threads` :

```javascript
const { Worker } = require('worker_threads');

new Worker('./worker.js');
new Worker('./worker.js');
new Worker('./worker.js');

console.log("Le thread principal continue de s'exécuter dans le processus...");
```

Le code ci-dessus crée trois threads ouvriers (worker threads) en parallèle sur une machine multicœur. Cela n'arrête pas le thread principal qui continue de s'exécuter, permettant à chaque thread ouvrier d'effectuer sa tâche indépendamment. `worker.js` pourrait être un fichier simple effectuant n'importe quelle tâche. Dans ce cas, il enregistre simplement un message à l'écran :

```javascript
console.log("Ce thread ouvrier s'exécute ici !");
```

Notez que l'argument du constructeur `Worker` peut être n'importe quel chemin de fichier, et l'ordre dans lequel ils sont exécutés ne dépend pas de l'ordre dans lequel ils apparaissent dans le code. Chaque ouvrier s'exécute indépendamment des autres et ils s'exécutent en parallèle.

La concurrence et le parallélisme permettent à Node.js (qui est monothreadé) de sembler gérer plusieurs tâches simultanément. La compréhension de ces concepts prépare le terrain pour la boucle d'événements, montrant comment Node.js parvient à donner l'apparence de la concurrence tout en exécutant du code dans un environnement à thread unique.

## Qu'est-ce que la boucle d'événements ?

La boucle d'événements écoute les événements dans l'environnement Node.js. Elle écoute essentiellement les actions puis traite les tâches ou produit des valeurs.

Pour mieux comprendre comment cela fonctionne, vous pouvez imaginer l'environnement Node.js comme une organisation au rythme effréné et la boucle d'événements comme un manager débordé qui refuse d'embaucher un assistant personnel. Le manager supervise les opérations de tout le bureau et possède un bureau dédié qui contient tout ce sur quoi il travaille à ce moment précis. Appelons ce bureau *la pile d'appels (call stack)*.

La pile d'appels se compose de tous les processus ou tâches sur lesquels Node.js travaille actuellement. Lorsqu'une entrée est saisie ou qu'un code est écrit pour faire quelque chose, il est déplacé vers la pile d'appels et à partir de là, il est exécuté.

L'ordre dans lequel cette exécution a lieu est important, car le code synchrone arrive dans la pile d'appels avant le code asynchrone. Qu'arrive-t-il au code asynchrone, me demanderez-vous ? Il va d'abord dans ce qu'on appelle la file d'attente des callbacks (callback queue) avant de finir sur la pile d'appels.

La file d'attente des callbacks est une file d'attente de tâches asynchrones qui n'arrivent sur la pile d'appels que si celle-ci est vide. Vous pouvez y penser comme à un classeur dans le bureau, où le code asynchrone traité par une équipe spécialisée de travailleurs sous la direction du manager va rester jusqu'à ce que le bureau du manager soit débarrassé. Le manager ne se rend au classeur que lorsqu'il a fini de gérer toutes les tâches synchrones sur la pile d'appels. Cette équipe spécialisée qui gère le code asynchrone comme les callbacks et async/await sont les APIs Node ou les APIs Web.

Les APIs Node ou Web traitent le code asynchrone. Lorsque le code arrive, il est traité ici puis placé dans la file d'attente des callbacks pour que la boucle d'événements le récupère et l'emmène vers la pile d'appels. Mais certaines tâches asynchrones sont prioritaires. Celles-ci sont connues sous le nom de microtâches (microtasks), comme les [promesses (promises)](https://www.freecodecamp.org/news/guide-to-javascript-promises/).

Les microtâches reçoivent une priorité particulière et sont mises en file d'attente dans une file d'attente de microtâches spéciale. Celle-ci est généralement vérifiée après une opération avant de vérifier la file d'attente des callbacks. Si rien n'est présent, la boucle d'événements vérifie la file d'attente des callbacks, mais si une tâche existe telle que `process.nextTick()`, elle est traitée immédiatement. Les macrotâches (macrotasks) consistent en des tâches qui sont régulièrement planifiées et gérées par la boucle d'événements seulement après le traitement des microtâches, comme `setTimeout()` et `setInterval()`.

Donc, comme vous pouvez le voir, la boucle d'événements est fondamentalement ce que son nom indique : une boucle. Elle parcourt les événements et gère les tâches selon un calendrier hiérarchisé.

Une chose à noter, cependant, est que même au sein des files d'attente de callbacks et des files d'attente de microtâches, il y a des phases. La boucle d'événements, par exemple, doit gérer certaines tâches avant d'autres, même au sein de la même catégorie. C'est là que les phases de la boucle d'événements interviennent.

## Les phases de la boucle d'événements

Par analogie, la boucle d'événements s'apparente à un manager qui vérifie l'état des projets et des tâches à intervalles réguliers. Dans ce cas, il a un calendrier spécifique pour vérifier l'état des projets. Certains projets ou tâches sont prioritaires sur d'autres, et le manager doit les examiner dans un ordre précis.

Vous pouvez également visualiser les phases de la boucle d'événements comme un train se déplaçant de gare en gare. Il part d'un endroit et se déplace vers d'autres dans un ordre particulier jusqu'à ce qu'il ait terminé, puis recommence le voyage. Cet arrangement détermine quelles tâches sont exécutées avant les autres.

Voici les phases de la boucle d'événements dans l'ordre :

1. La phase des minuteurs (timers) : Cette phase exécute les callbacks de `setTimeout()` et `setInterval()` une fois la durée écoulée. La boucle d'événements commence ici, comme la première gare du voyage d'un train.
    
2. La phase des callbacks en attente (pending callbacks) : Ce sont des callbacks au niveau du système, vérifiés après les opérations de la phase des minuteurs.
    
3. La phase de scrutation (poll) : Cette phase gère les événements d'entrée/sortie (I/O) et exécute les callbacks. En l'absence de callbacks, la boucle d'événements attend ici les nouveaux.
    
4. La phase de vérification (check) : Cette phase exécute les callbacks de `setImmediate()`.
    
5. La phase de fermeture des callbacks (close callbacks) : Cette phase s'occupe de l'exécution des événements de fermeture comme les fermetures de sockets.
    

Ces événements de callback sont vérifiés dans l'ordre et exécutés en conséquence, de sorte que si `setTimeout()` et `setImmediate()` sont dans le même code, `setTimeout()` s'exécute en premier, à moins que le « train » ne se trouve, disons, dans la phase de scrutation (Poll) de la boucle, de sorte que `setImmediate()` s'exécute avant `setTimeout()`.

Vous pouvez voir cela illustré avec l'exemple ci-dessous :

```javascript
const fs = require('fs');

fs.readFile('trainMap.txt', () => {
    setTimeout(() => {
        console.log("Le train démarre");
    }, 0);
    setImmediate(() => {
        console.log("Oups ! Arrêt immédiat ! Il y a un chat sur les rails !");
    })
});
```

Vous voyez dans le code ci-dessus que les callbacks sont gérés de manière asynchrone. Rappelez-vous que la boucle d'événements attend de nouveaux callbacks dans la phase de scrutation (poll). Cela signifie que puisque `fs.readfile()` est un callback, il est traité dans la phase de scrutation.

`setTimeout()` est configuré pour s'exécuter dans la phase des minuteurs, mais la boucle d'événements passe à la phase de vérification (qui vient ensuite) où `setImmediate()` est exécuté. C'est pourquoi `setImmediate()` s'exécute avant `setTimeout()` dans ce cas. La boucle d'événements continue ensuite de la phase de vérification à la phase de fermeture, puis revient à la phase des minuteurs, répétant ce cycle continuellement.

Cela explique pourquoi vous voyez la sortie ci-dessous affichée à l'écran :

```bash
Oups ! Arrêt immédiat ! Il y a un chat sur les rails !
Le train démarre
```

Ceci illustre comment la boucle d'événements impose l'ordre d'exécution à travers les différentes phases, garantissant que les opérations asynchrones s'exécutent dans la bonne séquence.

## Conclusion

La boucle d'événements de Node.js peut parfois paraître mystérieuse, mais elle n'est vraiment pas aussi complexe qu'elle en a l'air. À la base, c'est simplement le moteur qui garantit que JavaScript peut gérer plusieurs tâches sans se figer.

Dans cet article, vous avez découvert le code synchrone et asynchrone, la concurrence, le parallélisme et comment ces concepts aident à expliquer la boucle d'événements et ses différentes phases. Comprendre comment ils fonctionnent vous donne la confiance nécessaire pour écrire du code asynchrone sans crainte, déboguer plus efficacement et apprécier la puissance derrière la capacité de Node.js à gérer des tâches concurrentes.