---
title: 'Structures de données 101 : Files d''attente'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:18:47.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-queues-a6960a3c98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EhimF7dL04AkpisbKM2LJg.jpeg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: 'Structures de données 101 : Files d''attente'
seo_desc: 'By Kevin Turney

  Starting with a Queue

  When you go the Shake Shack, most often there are other people on the line waiting
  to be served. The customers are arranged in a particular order, First In, First
  Out. Other real-life scenarios are toll booths or...'
---

Par Kevin Turney

### Commencer avec une file d'attente

Lorsque vous allez au Shake Shack, la plupart du temps, il y a d'autres personnes dans la file d'attente qui attendent d'être servies. Les clients sont disposés dans un ordre particulier, Premier Arrivé, Premier Servi. D'autres scénarios de la vie réelle sont les péages ou les chapelles de mariage à Vegas. Cette méthode d'ordonnancement des données pour le service, dans notre cas, des personnes, est ce que les files d'attente sont tout à fait.

Les files d'attente sont très similaires aux piles en termes d'interface, la différence étant que les piles traitent les données Dernier Arrivé, Premier Servi.

Nous avons donc des différences dans l'ordre de traitement — pourquoi ? Nous avons besoin d'une méthode différente de traitement des données qui préserve l'ordre. Par exemple, supposons que nous avons un flux de données dans le nœud. À mesure qu'il arrive, nous devons faire quelque chose avec et puis l'écrire dans un fichier à lire plus tard. Pour simplifier, disons que nous devons mettre en majuscule chaque lettre diffusée. Que se passerait-il si nous utilisions une structure de données LIFO, ou pile ?

![Image](https://cdn-media-1.freecodecamp.org/images/YqhoftqFVXVQ0XQ22oh6Ds0IQgObVjsd1eNQ)

La principale raison est que les files d'attente traitent les données de manière équitable et préservent l'ordre de la collection. Cela se produit également lorsque nous itérons sur les éléments avec une boucle for ou while, la méthode forEach() ou map(). Chaque élément du tableau est traité dans l'ordre où il a été inséré, de l'index 0 à index.length — 1.

**Dans les files d'attente, les éléments sont traités dans l'ordre où ils sont insérés.**

### Implémentation

Une implémentation simple utilisant des tableaux est avec la méthode shift() pour retirer de l'avant et unshift() pour ajouter à l'avant.

Comme dans [mon article sur les piles](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980), nous allons décrire l'API pour une file d'attente. Ensuite, nous commencerons avec une implémentation utilisant la méthode pseudoclassique et un objet de base.

Lorsque qu'un élément est inséré dans une file d'attente, il est appelé **enfilé**. Lorsque qu'un élément est retiré, il est **défiler**. D'autres méthodes incluent peek, contains, until, et count.

![Image](https://cdn-media-1.freecodecamp.org/images/aQcmAeS9hN4ormkWg3L00rJZEfk3mmJdx6Pk)

Pour suivre nos éléments, nous utilisons la tête pour l'avant de la file d'attente et la queue pour l'arrière. La différence entre les deux donne la taille de la file d'attente.

Notre mécanisme de stockage est le suivant :

```
// _underscores indique "variables privées" aux autres ingénieurs
```

```
const Queue = function(capacity) {  this.storage = {};  this.capacity = capacity || Infinity;  this._head = 0;  this._tail = 0}
```

```
let q = new Queue();q; // Queue { storage: {}, capacity: Infinity, _head: 0, _tail: 0 }
```

Pour Enfiler :

```
Queue.prototype.enqueue = function(value) {  if (this.count() < capacity) {    this.storage[this._tail++] = value;    return this.count();  }  return "Capacité maximale atteinte, veuillez retirer une valeur avant d'enfiler"}
```

Pour Défiler :

```
Queue.prototype.dequeue = function() {    if (this.count() === 0) {      return "Rien dans la file d'attente";    }    else {      let element = this.storage[this._head];      delete this.storage[this._head];      if (this._head < this._tail) {        this._head++;      }      return element;    }}
```

Le reste de l'API :

```
Queue.prototype.peek = function() {  return this.storage[this._head]}
```

```
Queue.prototype.contains = function(value) {  for (let i = this._head; i < this._tail; i++) {    if (this.storage[i] === value) {      return true;    }  }  return false;}
```

```
Queue.prototype.until = function(value) {  for (let i = this._head; i < this._tail; i++) {    if (this.storage[i] === value){      return i - this._head + 1;    }  }  return null;}
```

```
Queue.prototype.count = function() {  return this._tail - this._head;}
```

```
let q = new Queue();q.enqueue('ww');q.enqueue('aa');q; // Queue {capacity: Infinity, storage: { 0: 'ww', 1: 'aa' }, _head: 0, _tail: 2 }q.enqueue('bb');q.peek(); // 'ww'q.dequeue(); // 'ww'q; //Queue {capacity: Infinity, storage: { 1: 'aa', 2: 'bb' }, _head: 1, _tail: 3 }q.contains('bb'); // trueq; //Queue {capacity: Infinity,storage: { 1: 'aa', 2: 'bb' }, _head: 1, _tail: 3 }q.until('bb'); // 2q.count(); // 2
```

Sous le capot, nous avons appris dans [mon article sur les piles](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980), que chaque fois qu'une fonction est appelée, elle crée un contexte d'exécution et se voit allouer un cadre de pile sur la pile d'exécution. Y a-t-il quelque chose de similaire en JavaScript qui utilise des files d'attente ? Oui : la boucle d'événements.

### La boucle d'événements et les files d'attente

Avant d'en venir à ce qu'est la boucle d'événements, nous devons d'abord comprendre quelques termes.

**Concurrency** — En informatique, des parties d'un programme informatique peuvent s'exécuter dans le désordre sans affecter le résultat. Dans le contexte de JavaScript, cela fait référence à la capacité de la boucle d'événements à exécuter des fonctions de rappel après avoir terminé d'autres travaux.

**Runtime** — le temps pendant lequel un programme est en cours d'exécution.

**Non-bloquant vs. bloquant** — bloquant est lorsque l'exécution d'un programme JavaScript doit attendre jusqu'à ce qu'une autre partie du programme soit terminée, parfois des opérations non-JavaScript. Essentiellement, synchrone, faire une chose à la fois.

Les opérations non-bloquantes, en revanche, fonctionnent de manière asynchrone. Elles emploient des rappels qui permettent aux opérations de continuer, et lorsque le travail est terminé, le rappel associé à cette fonction ou événement particulier se déclenche.

**Noyau du système** — est la partie centrale d'un système d'exploitation. Il gère les opérations de l'ordinateur et de la mémoire et du matériel, spécifiquement le CPU. Pour être plus efficace, la boucle d'événements délègue certaines opérations au noyau.

#### Maintenant, la boucle d'événements.

JavaScript est un langage à thread unique. Cela signifie que le flux d'exécution se fait dans l'ordre, et il fait une chose à la fois. Node.js est construit sur le [moteur Chrome V8](https://developers.google.com/v8/intro), et il emploie une boucle en rotation continue attendant les connexions entrantes.

Lorsque qu'une fonction asynchrone s'exécute, elle entre dans la boucle d'événements. Un message associé à cette fonction entre dans la **file de messages** dans l'ordre où il a été reçu. D'autres fonctions déjà dans la boucle sont exécutées ou sont en cours de traitement. Lorsque le message est défiler, la fonction de rappel s'exécute et est placée sur la pile d'exécution.

Pendant ce temps, la boucle d'événements continue de tourner, attendant plus de connexions. C'est ainsi que les files d'attente sont utilisées en coulisses dans JavaScript.

### Complexité temporelle

Les opérations de file d'attente sont très efficaces. Enfiler, Défiler, Peek et Count sont les plus rapides fonctionnant en temps constant. Contains et Until prennent plus de temps à mesure que notre taille d'entrée augmente, fonctionnant en temps linéaire O(N) ;

Enfiler O(1)
Défiler O(1)
Peek O(1)
Count O(1)
Contains O(N)
Until O(N)

Merci d'avoir lu. Si vous n'êtes pas familier avec les piles, veuillez consulter [mon autre article](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980) sur elles pour plus de contexte.