---
title: Les différences entre les temporisateurs asynchrones de l'API JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:28:59.000Z'
originalURL: https://freecodecamp.org/news/the-differences-between-javascripts-asynchronous-api-timers-d916e0596716
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Les différences entre les temporisateurs asynchrones de l'API JavaScript
seo_desc: 'By Rajika Imal

  JavaScript is a single-threaded language, which makes use of asynchronous constructs
  to handle tasks concurrently. Interestingly, it handles concurrent tasks efficiently
  with a different approach compared to traditional languages likes...'
---

Par Rajika Imal

JavaScript est un langage à thread unique, qui utilise des constructions asynchrones pour gérer les tâches de manière concurrente. Intéressamment, il gère les tâches concurrentes efficacement avec une approche différente comparée aux langages traditionnels comme Java et C#.

#### Boucle d'événements

Que ce soit dans un environnement de navigateur ou Node.js, JavaScript est asynchrone grâce au fait qu'il utilise la boucle d'événements. Dans l'environnement Node, elle est implémentée en utilisant une bibliothèque libuv. À l'origine, libuv a été développée comme un wrapper pour libev. Dans la version Node 0.9.0, la dépendance de libev a été supprimée.

#### Phases dans les boucles d'événements

```
   ┌────────────────────────┐┌─>│           timers          ││  └────────────────────────┘│  └────────────────────────┐┌─>│     pending callbacks     ││  └────────────────────────┘│  └────────────────────────┐┌─>│       idle, prepare       ││  └────────────────────────┘│  └────────────────────────┐┌─>│   incoming:   ││  │           poll            │<─────────────┤  connections, ││  └────────────────────────┘│  └────────────────────────┐┌─>│   data, etc.  ││  └────────────────────────┘│  └────────────────────────┐┌─>│           check           ││  └────────────────────────┘│  └────────────────────────┐┌─>│      close callbacks      │   └────────────────────────┘
```

> source: [https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

Les boucles d'événements peuvent être divisées en plusieurs phases comme illustré ci-dessus. Chaque phase sera exécutée à chaque itération. Une telle itération est appelée un tick dans la boucle d'événements. Chaque phase a une file d'attente premier entré, premier sorti (FIFO) qui enregistrera différentes tâches. Pour comprendre comment setTimeout, setImmediate et nextTick fonctionnent, nous allons passer en revue les phases importantes pertinentes.

#### Phase des temporisateurs

Les rappels enregistrés par _setTimeout_ et _setInterval_ seront exécutés dans cette phase. Il est important de noter que les rappels ne seront pas exécutés immédiatement mais plutôt après qu'un certain seuil de temps soit écoulé.

#### Phase de vérification

Si la phase de sondage qui gère les rappels d'E/S devient inactive ou si le nombre maximum d'exécutions est dépassé, elle passera à la phase de vérification, où elle exécutera les rappels enregistrés par _setImmediate_.

#### File d'attente des micro-tâches et file d'attente des macro-tâches

Ces deux files d'attente sont importantes pour comprendre l'ordre des tâches exécutées via différentes API. Les macro-tâches sont exécutées dans chacune des phases montrées dans le diagramme ci-dessus.

_setImmediate_ fait partie de la file d'attente des macro-tâches. Les micro-tâches seront exécutées jusqu'à ce que la file d'attente soit vide avant de passer à l'itération suivante ou au tick de la boucle d'événements.

Les rappels de process.nextTick seront enregistrés dans la file d'attente des micro-tâches et ils seront exécutés jusqu'à ce qu'elle soit vide. Par conséquent, avoir des appels récursifs dans process.nextTick peut affamer la boucle d'événements, l'empêchant de passer au tick suivant. Les macro-tâches n'affameront pas la boucle d'événements car elle passera au tick suivant une fois que le nombre maximum d'exécutions sera atteint.

Examinons quelques exemples pour voir comment chacune des API se comporte dans le monde réel pour mieux comprendre.

Dans le reste des exemples montrés dans cet article, Node.js sera utilisé comme environnement d'exécution.

#### setTimeout vs setImmediate

Remarquez que les appels ne sont pas dans un cycle d'E/S. En raison de ce fait, l'exécution dépendra des performances du CPU. Par conséquent, les logs seront imprimés de manière aléatoire dans ce cas.

Dans cet exemple, ils sont dans un cycle d'E/S. Le rappel de _setImmediate_ sera exécuté à chaque fois puisque la file d'attente des macro-tâches (phase de vérification) sera exécutée après le tick. setTimeout sera appelé dans la phase des temporisateurs une fois que le seuil sera dépassé.

#### setImmediate vs process.nextTick

_nextTick_ fait partie de la file d'attente des micro-tâches, et il sera exécuté avant que la boucle d'événements ne passe au tick suivant. Après nextTick dans le tick suivant, setImmediate déclenchera son rappel dans la file d'attente des macro-tâches dans la phase de vérification.

nextTick exécute la fonction récursive qui sera exécutée jusqu'à ce qu'elle entre dans la condition de base (si num > 5). Ce n'est qu'après l'exécution de nextTick que setImmediate déclenchera son rappel. Le comportement récursif continu est dû au fait que nextTick fait partie de la file d'attente des micro-tâches qui n'autorise pas la boucle d'événements à passer au tick suivant.

#### setImmediate vs setTimeout vs process.nextTick

Comme prévu, nextTick est appelé en premier, suivi de setImmediate et setTimeout. Il est important de noter que les fonctions sont appelées dans un cycle d'E/S. Si elles ne sont pas dans un cycle d'E/S, la sortie sera différente et dépendra des performances du processus.

> Ressources complémentaires

[**Modèle de concurrency et boucle d'événements**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)
[_JavaScript a un modèle de concurrency basé sur une "boucle d'événements". Ce modèle est assez différent des modèles dans d'autres..._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)
[**La boucle d'événements Node.js, les temporisateurs et process.nextTick() | Node.js**](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)
[_Modifier sur GitHub La boucle d'événements est ce qui permet à Node.js d'effectuer des opérations d'E/S non bloquantes - malgré le fait que..._nodejs.org](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)
[**Tâches, micro-tâches, files d'attente et plannings**](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
[_Quand j'ai dit à mon collègue Matt Gaunt que je pensais écrire un article sur la mise en file d'attente des micro-tâches et l'exécution dans..._jakearchibald.com](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)