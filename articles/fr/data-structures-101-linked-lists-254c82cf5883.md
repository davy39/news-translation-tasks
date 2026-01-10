---
title: 'Structures de données 101 : Listes chaînées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:24:14.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-linked-lists-254c82cf5883
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CPkY32KFN7fmxppL
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'Structures de données 101 : Listes chaînées'
seo_desc: 'By Kevin Turney

  Like stacks and queues, Linked Lists are a form of a sequential collection. It does
  not have to be in order. A Linked list is made up of independent nodes that may
  contain any type of data. Each node has a reference to the next node i...'
---

Par Kevin Turney

Comme les [piles](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980) et les [files d'attente](https://medium.freecodecamp.org/data-structures-101-queues-a6960a3c98), les listes chaînées sont une forme de collection séquentielle. Elles n'ont pas besoin d'être dans l'ordre. Une liste chaînée est composée de nœuds indépendants qui peuvent contenir n'importe quel type de données. Chaque nœud a une référence au nœud suivant dans le lien.

![Image](https://cdn-media-1.freecodecamp.org/images/VSLri8VM6VeXUN4Ml43JlFh6SspOdtkXNkj-)

Nous pouvons émuler des piles et des files d'attente avec des listes chaînées. Nous pouvons également l'utiliser comme base pour créer ou augmenter d'autres structures de données. Avec les listes chaînées, nos principales préoccupations sont les **insertions et suppressions rapides**, qui sont plus performantes que les tableaux.

Le bloc de construction de cette structure est un Nœud.

```
const Node = function(value) {  this.value = value;  this.next = null;};
```

Notre Nœud est construit avec deux propriétés, une `value` pour contenir des données, et `next`, une référence initialement définie sur null. La propriété `next` est utilisée pour "pointer" vers le Nœud suivant dans le lien. L'un des inconvénients des listes chaînées est que chaque référence nécessite une plus grande surcharge de mémoire qu'un tableau.

### Implémentation

```
const LinkedList = function(headvalue) {  // !! force une valeur à un Booléen  if (!!headvalue) {    return "Must provide an initial value for the first node"  } else {    this._head = new Node(headvalue);    this._tail = this.head;  }};
```

Dans notre deuxième constructeur, nous testons une valeur à fournir pour le premier Nœud. Si vrai, nous procédons à la création d'un nouveau Nœud avec la valeur passée et définissons la tête sur la queue initialement.

#### Insertion

```
LinkedList.prototype.insertAfter = function(node, value) {  let newNode = new Node(value);  let oldNext = node.next;  newNode.next = oldNext;  node.next = newNode;  if (this._tail === node) {    this._tail = newNode;  }  return newNode;};
```

Pour cette méthode, nous créons un nouveau Nœud et ajustons les références. L'ancienne référence suivante du nœud original est maintenant dirigée vers newNode. La référence suivante de newNode est "pointée" vers ce que la référence suivante du nœud précédent était. Enfin, nous vérifions et réinitialisons la propriété de queue.

```
LinkedList.prototype.insertHead = function(value) {  let newHead = new Node(value);  let oldHead = this._head  newHead.next = oldHead;  this._head = newHead;  return this._head;};
```

```
LinkedList.prototype.appendToTail = function(value) {  let newTail = new Node(value);  this._tail.next = newTail;  this._tail = newTail;  return this._tail;};
```

L'insertion au début ou à la fin d'une liste chaînée est rapide, fonctionnant en temps constant. Pour cela, nous créons un nouveau nœud avec une valeur et réorganisons nos variables de référence. Nous réinitialisons le nœud qui est maintenant la tête avec `insertHead` ou la queue avec `appendToTail`.

Ces opérations représentent des insertions rapides pour les collections, push pour les piles, et enqueue pour les files d'attente. Il peut venir à l'esprit que unshift pour les tableaux est la même chose. Non, car avec unshift tous les membres de la collection doivent être déplacés d'un index. Cela en fait une opération en temps linéaire.

#### Suppression

```
LinkedList.prototype.removeAfter = function(node) {  let removedNode = node.next;  if (!!removedNode) {    return "Nothing to remove"  } else {    let newNext = removedNode.next    node.next = newNext;    removedNode.next = null; // déréférencer à null pour libérer de la mémoire    if (this._tail === removedNode) {      this._tail = node;    }  }  return removedNode;};
```

En commençant par un test pour un nœud à supprimer, nous procédons à l'ajustement des références. Le déréférencement du `removedNode` et sa définition à null est important. Cela libère de la mémoire et évite d'avoir plusieurs références au même objet.

```
LinkedList.prototype.removeHead = function() {  let oldHead = this._head;  let newHead = this._head.next;  this._head = newHead;  oldHead.next = null;  return this._head;};
```

La suppression d'une tête et d'un nœud spécifié dans, removeAfter, sont des suppressions en temps constant. De plus, si la valeur de la queue est connue, alors la suppression de la queue peut être faite en O(1). Sinon, nous devons nous déplacer linéairement à la fin pour la supprimer, O(N);

#### Boucles et forEach

Nous utilisons ce qui suit pour itérer à travers une liste chaînée ou pour opérer sur chaque valeur de nœud.

```
LinkedList.prototype.findNode = function(value) {  let node = this._head;  while(node) {    if (node.value === value) {      return node;    }    node = node.next;  }  return `No node with ${value} found`;};
```

```
LinkedList.prototype.forEach = function(callback) {  let node = this._head;  while(node) {    callback(node.value);    node = node.next;  }};
```

```
LinkedList.prototype.print = function() {  let results = [];  this.forEach(function(value) {    result.push(value);  });  return result.join(', ');};
```

![Image](https://cdn-media-1.freecodecamp.org/images/xCK9TNXHamXNv5KYdpUQ10HmD46HH6aoFYQw)

Le principal avantage des listes chaînées est les insertions et suppressions rapides sans réorganiser les éléments ou réallouer de l'espace. Lorsque nous utilisons un tableau, l'espace mémoire est contigu, ce qui signifie que nous le gardons tout ensemble. Avec les listes chaînées, nous pouvons avoir des espaces mémoire partout, un stockage non contigu grâce à l'utilisation de références. Pour les tableaux, cette localité des références signifie que les tableaux ont une meilleure mise en cache des valeurs pour une recherche plus rapide. Avec les listes chaînées, la mise en cache n'est pas optimisée et le temps d'accès est plus long.

Un autre aspect des listes chaînées est les différents types de configuration. Deux exemples principaux sont les listes chaînées **circulaires**, où la queue a une référence à la tête et la tête à la queue. Les listes **doublement** chaînées sont lorsque, en plus du nœud ayant une référence au nœud suivant, il a également une référence regardant en arrière vers le nœud précédent.

### Complexité temporelle

Insertion

* insertHead, appendToTail — O(1)
* si un nœud spécifique est connu, insertAfter — O(1)

Suppression

* removeHead — O(1);
* si un nœud spécifique est connu, removeAfter — O(1)
* si le nœud n'est pas connu — O(N)

Parcours

* findNode, forEach, print — O(N)

### Ressources

[Localité de référence](https://en.wikipedia.org/wiki/Locality_of_reference)
[Grandes réponses ici](https://stackoverflow.com/questions/166884/array-versus-linked-list)
[et ici](https://stackoverflow.com/questions/166884/array-versus-linked-list)
[Liste chaînée](https://en.wikipedia.org/wiki/Linked_list)

Merci d'avoir lu. Pour vous entraîner, essayez d'implémenter une pile ou une file d'attente avec une liste chaînée, ou stockez des tableaux dans chaque nœud et extrayez des données. Demandez-vous quand j'utilise un tableau, est-ce en fait le meilleur choix pour mes besoins ?