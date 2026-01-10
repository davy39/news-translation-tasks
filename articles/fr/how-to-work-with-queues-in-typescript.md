---
title: Comment travailler avec les files d'attente en TypeScript
subtitle: ''
author: Yazdun
co_authors: []
series: null
date: '2025-06-16T21:50:21.630Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-queues-in-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750082265731/de8b778c-935d-4a38-a5ef-748896475327.png
tags:
- name: TypeScript
  slug: typescript
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
seo_title: Comment travailler avec les files d'attente en TypeScript
seo_desc: 'A queue is a collection of items arranged in a First-In-First-Out (FIFO)
  order. This means that the first item added is the first to be removed, much like
  a supermarket line where customers are served in the order they arrive.


  In this hands-on tutor...'
---

Une file d'attente est une collection d'éléments organisés selon l'ordre First-In-First-Out (FIFO). Cela signifie que le premier élément ajouté est le premier à être retiré, tout comme une file d'attente au supermarché où les clients sont servis dans l'ordre de leur arrivée.

![Diagramme illustrant une file d'attente. Les éléments sont ajoutés à l'arrière via "enqueue" et retirés de l'avant via "dequeue". Des flèches montrent le flux entrant et sortant d'une boîte rectangulaire représentant la file.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749741091206/42a62a3c-cf1b-4e7a-b8ce-4209e13f70d3.png align="center")

Dans ce tutoriel pratique, vous apprendrez comment implémenter des files d'attente en TypeScript en utilisant des listes chaînées.

## Voici ce que nous allons couvrir

* [Prérequis](#heading-prerequis)
    
* [Pour commencer](#heading-pour-commencer)
    
* [Que sont les files d'attente ?](#heading-que-sont-les-files-d-attente)
    
* [Que sont les listes chaînées ?](#heading-que-sont-les-listes-chainees)
    
* [Qu'est-ce qu'une file d'attente simple ?](#heading-qu-est-ce-qu-une-file-d-attente-simple)
    
* [Qu'est-ce qu'une file d'attente circulaire ?](#heading-qu-est-ce-qu-une-file-d-attente-circulaire)
    
* [Qu'est-ce qu'une file d'attente à double extrémité ?](#heading-qu-est-ce-qu-une-file-d-attente-a-double-extremite)
    
* [Qu'est-ce qu'une file d'attente prioritaire ?](#heading-qu-est-ce-qu-une-file-d-attente-prioritaire)
    
* [Quand utiliser les files d'attente (et quand les éviter)](#heading-quand-utiliser-les-files-d-attente-et-quand-les-eviter)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

1. **TypeScript :** Vous devez connaître les [bases de TypeScript](https://www.freecodecamp.org/news/learn-typescript-with-react-handbook/), telles que les interfaces, les types et les classes.
    
2. **Fondamentaux des algorithmes :** Vous avez besoin d'une compréhension de base des structures de données et des algorithmes. Par exemple, vous devriez être à l'aise avec l'analyse de la complexité temporelle et spatiale en utilisant la [notation Big-O.](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/)
    
3. **Structure de données des listes chaînées :** Il est important d'avoir une solide compréhension des listes chaînées avant de commencer ce tutoriel. J'ai écrit un [tutoriel détaillé sur les listes chaînées](https://www.freecodecamp.org/news/how-to-code-linked-lists-with-typescript-handbook) que vous pouvez utiliser pour apprendre sur cette structure de données.
    

## Pour commencer

Pour commencer ce tutoriel, vous utiliserez un projet de terrain de jeu conçu pour vous aider à implémenter des files d'attente et à suivre chaque étape de manière pratique.

Clonez le projet depuis le [dépôt GitHub et codez en même temps](https://github.com/Yazdun/fcc-queues) avec le tutoriel.

La structure du projet est la suivante :

```plaintext
.
├── index.ts
├── examples
│   ├── 01-linked-list.ts
│   ├── 02-simple-queue.ts
│   ├── 03-circular-queue.ts
│   ├── 04-double-ended-queue.ts
│   └── 05-priority-queue.ts
└── playground
    ├── 01-linked-list.ts
    ├── 02-simple-queue.ts
    ├── 03-circular-queue.ts
    ├── 04-double-ended-queue.ts
    └── 05-priority-queue.ts
```

Tout au long du tutoriel, vous utiliserez le répertoire `playground` pour implémenter et tester votre code.

Le répertoire `examples` contient la version finale de chaque implémentations. Si vous êtes bloqué, vous pouvez consulter ces solutions en dernier recours !

## Que sont les files d'attente ?

Une file d'attente est une structure de données qui gère les éléments selon l'ordre premier arrivé, premier sorti (FIFO), où le premier élément ajouté est le premier retiré.

Par exemple, imaginez une imprimante traitant des travaux. Si vous envoyez trois documents à imprimer, l'imprimante les traite dans l'ordre de leur arrivée. Le premier document est imprimé en premier, puis le second, et enfin le troisième.

En programmation, les files d'attente aident à gérer les tâches qui doivent se produire dans l'ordre, telles que :

* Un serveur web met en file d'attente les requêtes entrantes pour les traiter une par une.
    
* Une application de chat met en file d'attente les messages pour les envoyer dans l'ordre où ils sont tapés.
    
* Une application de navigation met en file d'attente les localisations pour explorer une carte niveau par niveau. (Recherche en largeur d'abord)
    

Il existe quatre types de files d'attente dans une structure de données :

* **File d'attente simple** : Ajoute les éléments à l'arrière et les retire de l'avant selon l'ordre premier arrivé, premier sorti (FIFO).
    
* **File d'attente circulaire** : Elle est similaire à une file d'attente simple, sauf que le dernier élément est connecté au premier.
    
* **File d'attente à double extrémité (Deque)** : Permet d'ajouter ou de retirer des éléments à la fois de l'avant et de l'arrière, comme une file d'attente d'arrêt de bus où les gens rejoignent ou quittent l'une ou l'autre extrémité.
    
* **File d'attente prioritaire** : Traite les éléments en fonction de la priorité, et non de l'ordre d'arrivée. Comme une application de livraison qui traite les commandes VIP avant les commandes normales.
    

Chacune de ces files d'attente possède un ensemble d'opérations pour gérer ses éléments. Dans ce tutoriel, vous apprendrez les opérations courantes et largement utilisées suivantes :

* **enqueue** : Ajoute un élément à l'arrière de la file, comme un nouveau client qui rejoint la fin d'une file d'attente pour les billets.
    
* **dequeue** : Retire et renvoie l'élément à l'avant de la file.
    
* **getFront** : Regarde l'élément à l'avant sans le retirer, comme vérifier qui est le premier dans la file.
    
* **getRear** : Regarde l'élément à l'arrière sans le retirer, comme voir qui est le dernier dans la file.
    
* **isEmpty** : Vérifie si la file d'attente n'a aucun élément.
    
* **isFull** : Vérifie si la file d'attente a atteint sa taille maximale.
    
* **peek** : Identique à `getFront`, visualise l'élément de tête sans le retirer, comme un coup d'œil rapide sur la première tâche.
    
* **size** : Renvoie le nombre d'éléments dans la file, comme compter combien de personnes sont dans la file.
    

Maintenant que vous connaissez les files d'attente et leurs principales opérations, passons à l'implémentation réelle et voyons à quoi cela ressemble dans le code.

Il existe quelques façons différentes d'implémenter des files d'attente, mais dans ce tutoriel, vous apprendrez les **files d'attente basées sur des listes chaînées**, qui utilisent une liste chaînée pour créer les files.

Tout d'abord, apprenons brièvement la structure de données des listes chaînées, puis passons à l'implémentation de la file.

## Que sont les listes chaînées ?

Une liste chaînée est une méthode de stockage d'une collection d'éléments où chaque élément, connu sous le nom de "nœud", contient deux parties : les données réelles et une référence (ou pointeur) vers l'élément suivant dans la liste.

Contrairement aux tableaux, où tous les éléments sont stockés les uns à côté des autres en mémoire, les listes chaînées connectent les nœuds à l'aide de ces références, comme une chaîne.

Les listes chaînées sont utilisées pour implémenter des files d'attente car elles permettent une **insertion efficace à la fin** et une **suppression du début**, ce qui sont les deux principales opérations d'une file d'attente.

Dans une file d'attente basée sur une liste chaînée, vous pouvez ajouter un nouveau nœud à la queue et en retirer un de la tête en temps constant (`O(1)`) sans avoir besoin de décaler les éléments, comme vous le feriez dans un tableau.

![Diagramme d'une liste chaînée avec quatre nœuds connectés séquentiellement. Le nœud 1 est étiqueté comme tête et le nœud 4 comme queue.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749741385495/1bfab581-481d-4108-9f48-bf93d9dcf4f1.png align="center")

Dans ce tutoriel, vous allez utiliser un type spécifique de liste chaînée appelée **Liste chaînée doublement circulaire**.

Une liste chaînée doublement circulaire est un type de liste chaînée où chaque nœud se connecte à la fois aux nœuds suivants et précédents, et le dernier nœud boucle vers le premier pour former un cercle.

Cela signifie que vous pouvez parcourir la liste dans les deux directions sans jamais rencontrer une impasse. Cela facilite le déplacement vers l'avant ou vers l'arrière à travers les nœuds et aide à éviter les cas spéciaux comme la gestion de `null` aux extrémités.

Dans une liste chaînée doublement circulaire, tout est connecté dans une boucle, ce qui simplifie certaines opérations de file d'attente et maintient l'efficacité.

![Diagramme montrant une liste chaînée doublement circulaire avec cinq nœuds étiquetés du nœud 1 (tête) au nœud 5 (queue), connectés en boucle.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749741872784/d01a9c89-945e-4b4a-acff-56b7e528ea7e.png align="center")

Vous pouvez en apprendre plus sur les listes chaînées circulaires dans mon [Handbook des listes chaînées](https://www.freecodecamp.org/news/how-to-code-linked-lists-with-typescript-handbook/#heading-what-is-a-circular-linked-list).

Pour ce tutoriel, j'ai déjà ajouté une liste chaînée doublement circulaire dans `src/playground/01-linked-list.ts` :

```typescript
// 📁 src/playground/01-linked-list.ts

/**
 * Node for doubly linked list
 */
export class NodeItem<T> {
  value: T;
  next: NodeItem<T> | null = null;
  prev: NodeItem<T> | null = null;

  constructor(value: T) {
    this.value = value;
  }
}

/**
 * Circular Doubly Linked List
 */
export class LinkedList<T> {
  private head: NodeItem<T> | null = null;
  private tail: NodeItem<T> | null = null;
  private currentSize: number = 0;

  /**
   * Add a new node to the front of the list
   * @param value The value to add
   */
  prepend(value: T): void {
    const newNode = new NodeItem(value);
    if (this.isEmpty()) {
      this.head = newNode;
      this.tail = newNode;
      newNode.next = newNode;
      newNode.prev = newNode;
    } else {
      newNode.next = this.head;
      newNode.prev = this.tail;
      this.head!.prev = newNode;
      this.tail!.next = newNode;
      this.head = newNode;
    }
    this.currentSize++;
  }

  /**
   * Add a new node to the back of the list
   * @param value The value to add
   */
  append(value: T): void {
    const newNode = new NodeItem(value);
    if (this.isEmpty()) {
      this.head = newNode;
      this.tail = newNode;
      newNode.next = newNode;
      newNode.prev = newNode;
    } else {
      newNode.next = this.head;
      newNode.prev = this.tail;
      this.tail!.next = newNode;
      this.head!.prev = newNode;
      this.tail = newNode;
    }
    this.currentSize++;
  }

  /**
   * Remove and return the value from the front of the list
   * @returns The value at the head or undefined if empty
   */
  deleteHead(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }
    const value = this.head!.value;
    if (this.currentSize === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head!.next;
      this.head!.prev = this.tail;
      this.tail!.next = this.head;
    }
    this.currentSize--;
    return value;
  }

  /**
   * Remove and return the value from the back of the list
   * @returns The value at the tail or undefined if empty
   */
  deleteTail(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }
    const value = this.tail!.value;
    if (this.currentSize === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail!.prev;
      this.tail!.next = this.head;
      this.head!.prev = this.tail;
    }
    this.currentSize--;
    return value;
  }

  /**
   * Get the value at the front without removing it
   * @returns The value at the head or undefined if empty
   */
  getHead(): T | undefined {
    return this.head?.value;
  }

  /**
   * Get the value at the back without removing it
   * @returns The value at the tail or undefined if empty
   */
  getTail(): T | undefined {
    return this.tail?.value;
  }

  /**
   * Check if the list is empty
   * @returns True if the list is empty, false otherwise
   */
  isEmpty(): boolean {
    return this.currentSize === 0;
  }

  /**
   * Get the current size of the list
   * @returns The number of nodes in the list
   */
  size(): number {
    return this.currentSize;
  }
}
```

Dans ce module, vous avez une liste chaînée doublement circulaire avec 8 méthodes différentes qui faciliteront la construction de files d'attente plus tard dans le tutoriel :

* `prepend` : Ajoute une nouvelle valeur au **début** de la liste.
    
* `append` : Ajoute une nouvelle valeur à la **fin** de la liste.
    
* `deleteHead` : Retire et renvoie la valeur au **début**.
    
* `deleteTail` : Retire et renvoie la valeur à la **fin**.
    
* `getHead` : Renvoie la valeur de tête **sans la retirer**.
    
* `getTail` : Renvoie la valeur de fin **sans la retirer**.
    
* `isEmpty` : Vérifie si la liste n'a **aucun élément**.
    
* `size` : Renvoie le **nombre d'éléments** actuellement dans la liste.
    

Maintenant que votre liste chaînée est prête, commençons à créer votre première file d'attente !

## Qu'est-ce qu'une file d'attente simple ?

Une file d'attente simple suit la règle de base FIFO : vous devez ajouter les éléments à l'arrière et les retirer de l'avant.

C'est comme une file de clients à un comptoir de billets, où la première personne dans la file achète un billet en premier.

Pour commencer, ouvrez `src/playground/02-simple-queue.ts`, où vous trouverez l'espace réservé pour la file d'attente simple avec ses méthodes :

```typescript
// 📁 src/playground/02-simple-queue.ts

import { LinkedList } from "./01-linked-list";

/**
 * Simple Queue implemented with a circular doubly linked list
 */
export class SimpleQueue<T> {
  private list: LinkedList<T>;
  private maxSize?: number;

  /**
   * @param maxSize Optional maximum size of the queue
   */
  constructor(maxSize?: number) {
    this.list = new LinkedList<T>();
    this.maxSize = maxSize;
  }

  ...methods
}
```

Au cœur de cette classe `SimpleQueue`, vous utilisez une liste chaînée doublement circulaire pour stocker les éléments, et autorisez optionnellement une limite de taille maximale pour contrôler la taille de la file.

* `private list: LinkedList<T>` est l'endroit où les données de la file sont stockées. Au lieu d'un simple tableau, vous utilisez une liste chaînée personnalisée, ce qui rend efficace l'ajout ou la suppression d'éléments à chaque extrémité. La liste chaînée gère la structure de données et vous permet de vous concentrer sur le fonctionnement de la file.
    
* `private maxSize` est une limite optionnelle pour le nombre d'éléments que la file peut contenir. Si elle n'est pas fournie, la file peut croître autant que nécessaire.
    
* Ensuite, la méthode `constructor` qui s'exécute lorsque vous créez une nouvelle file. Elle crée une nouvelle liste chaînée vide pour contenir les éléments de la file.
    

Maintenant, implémentons les méthodes de la file.

Ouvrez votre éditeur de code et mettez à jour `src/playground/02-simple-queue.ts` avec le code suivant :

```typescript
// 📁 src/playground/02-simple-queue.ts

import { LinkedList } from "./01-linked-list";

/**
 * Simple Queue implemented with a circular doubly linked list
 */
export class SimpleQueue<T> {
  private list: LinkedList<T>;
  private maxSize?: number;

  /**
   * @param maxSize Optional maximum size of the queue
   */
  constructor(maxSize?: number) {
    this.list = new LinkedList<T>();
    this.maxSize = maxSize;
  }

  /**
   * Add an element to the rear of the queue
   * @param item The element to add
   */
  enqueue(item: T): void {
    if (this.isFull()) {
      throw new Error("Queue is full");
    }
    this.list.append(item);
  }

  /**
   * Remove and return the element from the front of the queue
   * @returns The element at the front or undefined if empty
   */
  dequeue(): T | undefined {
    return this.list.deleteHead();
  }

  /**
   * Get the element at the front without removing it
   * @returns The element at the front or undefined if empty
   */
  getFront(): T | undefined {
    return this.list.getHead();
  }

  /**
   * Get the element at the rear without removing it
   * @returns The element at the rear or undefined if empty
   */
  getRear(): T | undefined {
    return this.list.getTail();
  }

  /**
   * Check if the queue is empty
   * @returns True if the queue is empty, false otherwise
   */
  isEmpty(): boolean {
    return this.list.isEmpty();
  }

  /**
   * Check if the queue is full
   * @returns True if the queue is full, false otherwise
   */
  isFull(): boolean {
    return this.maxSize !== undefined && this.list.size() >= this.maxSize;
  }

  /**
   * Peek at the front element without removing it
   * @returns The element at the front or undefined if empty
   */
  peek(): T | undefined {
    return this.getFront();
  }

  /**
   * Get the current size of the queue
   * @returns The number of elements in the queue
   */
  size(): number {
    return this.list.size();
  }
}
```

Comme vous pouvez le voir, la liste chaînée simplifie grandement votre implémentation de file d'attente car elle agit comme le moteur derrière votre file.

Voici comment fonctionne votre file d'attente simple :

* **isEmpty()** : Cette méthode vérifie si la file contient des éléments. Elle appelle la méthode `isEmpty()` sur la liste chaînée, qui vérifie interne si la taille actuelle de la liste est zéro. Si la liste n'a pas de nœuds, elle renvoie `true`, indiquant que la file est vide. C'est une méthode utilitaire de base souvent utilisée avant d'essayer de défilement ou d'inspecter la file.
    
* **isFull()** : Cette méthode détermine si la file a atteint sa capacité. Elle compare la taille actuelle de la liste chaînée (via la méthode `size()`) à la valeur optionnelle `maxSize`. Si `maxSize` est défini et que la taille est égale ou supérieure à cette limite, elle renvoie `true`, indiquant qu'aucun autre élément ne peut être ajouté. C'est utile pour éviter le débordement dans les files d'attente bornées.
    
* **size()** : Cette méthode renvoie le nombre d'éléments actuellement stockés dans la file. Elle appelle directement la méthode `size()` de la liste chaînée, qui suit combien de nœuds sont présents. Cela vous permet de surveiller l'utilisation de la file et la capacité restante.
    
* **enqueue()** : Cette méthode ajoute un nouvel élément à la fin (arrière) de la file. Elle vérifie d'abord si la file est pleine en appelant la méthode `isFull()`. Si c'est le cas, la méthode lève une erreur. Sinon, elle ajoute le nouvel élément à la liste chaînée interne en utilisant la méthode `append()`, qui ajoute le nouveau nœud à la queue de la liste chaînée doublement circulaire.
    
* **dequeue()** : Cette méthode retire et renvoie l'élément à l'avant de la file. Elle appelle la méthode `deleteHead()` de la liste chaînée, qui supprime le nœud de tête et met à jour les liens des nœuds environnants pour maintenir la structure circulaire. Si la file est vide, elle renvoie `undefined`.
    
* **getFront()** : Cette méthode renvoie la valeur à l'avant de la file sans la retirer. Elle utilise la méthode `getHead()` de la liste chaînée pour récupérer la valeur du nœud de tête. Cette opération ne modifie pas la file et est utile pour prévisualiser le prochain élément à être défilé.
    
* **getRear()** : Cette méthode renvoie la valeur à l'arrière de la file sans la retirer. Elle utilise la méthode `getTail()` de la liste chaînée, qui renvoie la valeur du nœud de queue. Cela vous aide à inspecter l'élément le plus récemment ajouté sans modifier la file.
    
* **peek()** : Cette méthode est un alias de `getFront()`. Elle renvoie l'élément à l'avant de la file sans le retirer. En interne, elle appelle `getFront()` pour obtenir la valeur de tête. C'est souvent utilisé dans les API de file d'attente pour vérifier le prochain élément dans la file.
    

![Diagramme de flux illustrant les opérations de file d'attente. Le processus commence par une opération enqueue ou dequeue. Enqueue vérifie si la file est pleine : si oui, déclenche une erreur ; si non, ajoute un élément, met à jour le pointeur arrière et se termine. Dequeue vérifie si la file est vide : si oui, déclenche une erreur ; si non, supprime un élément, met à jour le pointeur avant et se termine.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749742108067/3f5aab62-8314-4889-925a-cb9d52d9a277.png align="center")

Vous venez d'implémenter votre première file d'attente en TypeScript. Pour vous assurer que votre implémentation fonctionne correctement, exécutez la commande suivante dans votre terminal à la racine du projet :

```bash
npm run test:file 02
```

Si l'un des tests échoue, utilisez l'exemple final de `src/examples/02-simple-queue.ts` pour déboguer le problème, puis réexécutez les tests.

Si tous les tests passent, vous pouvez passer à la section suivante, où vous implémenterez une file d'attente circulaire.

## Qu'est-ce qu'une file d'attente circulaire ?

Une `CircularQueue` est une file d'attente de taille fixe où la dernière position se reconnecte à la première. Cela permet de réutiliser l'espace après avoir retiré des éléments.

Imaginez une file d'attente de buffet avec un nombre limité d'assiettes : quand quelqu'un prend une assiette de l'avant, une nouvelle est ajoutée à l'arrière, en utilisant le même espace à nouveau.

La `CircularQueue` est assez similaire à la `SimpleQueue`, mais elle a quelques différences uniques.

Modifions `src/playground/03-circular-queue.ts` et ajoutons le code suivant :

```typescript
// 📁 src/playground/03-circular-queue.ts

import { LinkedList } from "./01-linked-list";

/**
 * Circular Queue implemented with a circular doubly linked list
 */
export class CircularQueue<T> {
  private list: LinkedList<T>;
  private maxSize: number;

  /**
   * @param maxSize Required maximum size of the circular queue
   */
  constructor(maxSize: number) {
    this.list = new LinkedList<T>();
    this.maxSize = maxSize;
  }

  /**
   * Add an element to the rear of the queue
   * @param item The element to add
   */
  enqueue(item: T): void {
    if (this.isFull()) {
      throw new Error("Circular queue is full");
    }
    this.list.append(item);
  }

  /**
   * Remove and return the element from the front of the queue
   * @returns The element at the front or undefined if empty
   */
  dequeue(): T | undefined {
    return this.list.deleteHead();
  }

  /**
   * Get the element at the front without removing it
   * @returns The element at the front or undefined if empty
   */
  getFront(): T | undefined {
    return this.list.getHead();
  }

  /**
   * Get the element at the rear without removing it
   * @returns The element at the rear or undefined if empty
   */
  getRear(): T | undefined {
    return this.list.getTail();
  }

  /**
   * Check if the queue is empty
   * @returns True if the queue is empty, false otherwise
   */
  isEmpty(): boolean {
    return this.list.isEmpty();
  }

  /**
   * Check if the queue is full
   * @returns True if the queue is full, false otherwise
   */
  isFull(): boolean {
    return this.list.size() >= this.maxSize;
  }

  /**
   * Peek at the front element without removing it
   * @returns The element at the front or undefined if empty
   */
  peek(): T | undefined {
    return this.getFront();
  }

  /**
   * Get the current size of the queue
   * @returns The number of elements in the queue
   */
  size(): number {
    return this.list.size();
  }
}
```

Cela peut ressembler beaucoup à une `SimpleQueue`, mais il y a quelques différences clés :

* **Différence de constructeur** : Contrairement à la `SimpleQueue`, la `CircularQueue` **requiert** un paramètre `maxSize` lors de l'instanciation. Cela impose une limite stricte supérieure sur le nombre d'éléments pouvant être dans la file à la fois.
    
    En revanche, `SimpleQueue` traite `maxSize` comme optionnel et autorise les files non bornées. En rendant la taille obligatoire, `CircularQueue` est mieux adaptée aux scénarios de tampon de taille fixe où le contrôle de la mémoire ou des ressources est important (par exemple, dans les systèmes en temps réel ou la mise en cache).
    
* **enqueue()** : Cette méthode est presque identique à celle de `SimpleQueue`, mais la différence clé réside dans l'intention de conception. Dans `CircularQueue`, lever une erreur lorsque la file est pleine fait partie du contrat et suppose que vous gérez un tampon fixe.
    
    La nature circulaire entre en jeu conceptuellement : une fois pleine, aucune donnée ne peut entrer à moins que les anciennes entrées ne soient retirées, ce qui imite un mécanisme d'écrasement circulaire (bien que cette implémentation spécifique ne s'écrase pas automatiquement).
    
* **isFull()** : Cette méthode se comporte de la même manière que dans `SimpleQueue` lorsqu'un `maxSize` est défini, mais dans `CircularQueue`, elle est toujours applicable car `maxSize` est requis. La présence cohérente d'une limite de taille rend la file prévisible et idéale pour les cas d'utilisation bornés comme le traitement de flux de données et le traitement à débit limité.
    

Maintenant, testons l'implémentation pour voir si elle fonctionne :

```bash
npm run test:file 03
```

Si l'un des tests échoue, utilisez le répertoire final `/examples` pour déboguer le problème.

Si les tests passent, vous serez prêt à passer à la section suivante, où vous apprendrez les files d'attente à double extrémité.

## Qu'est-ce qu'une file d'attente à double extrémité ?

Une file d'attente à double extrémité (deque) vous permet d'ajouter ou de retirer des éléments à la fois de l'avant et de l'arrière.

C'est comme une file d'attente à un arrêt de bus où les gens peuvent rejoindre ou quitter l'une ou l'autre extrémité.

Modifions `src/playground/04-double-ended-queue.ts` et ajoutons le code suivant :

```typescript
// 📁 src/playground/04-double-ended-queue.ts

import { LinkedList } from "./01-linked-list";

/**
 * Double-Ended Queue (Deque) implemented with a circular doubly linked list
 */
export class Deque<T> {
  private list: LinkedList<T>;
  private maxSize?: number;

  /**
   * @param maxSize Optional maximum size of the deque
   */
  constructor(maxSize?: number) {
    this.list = new LinkedList<T>();
    this.maxSize = maxSize;
  }

  /**
   * Add an element to the front of the deque
   * @param item The element to add
   */
  enqueueFront(item: T): void {
    if (this.isFull()) {
      throw new Error("Deque is full");
    }
    this.list.prepend(item);
  }

  /**
   * Add an element to the rear of the deque
   * @param item The element to add
   */
  enqueueRear(item: T): void {
    if (this.isFull()) {
      throw new Error("Deque is full");
    }
    this.list.append(item);
  }

  /**
   * Remove and return the element from the front of the deque
   * @returns The element at the front or undefined if empty
   */
  dequeueFront(): T | undefined {
    return this.list.deleteHead();
  }

  /**
   * Remove and return the element from the rear of the deque
   * @returns The element at the rear or undefined if empty
   */
  dequeueRear(): T | undefined {
    return this.list.deleteTail();
  }

  /**
   * Get the element at the front without removing it
   * @returns The element at the front or undefined if empty
   */
  getFront(): T | undefined {
    return this.list.getHead();
  }

  /**
   * Get the element at the rear without removing it
   * @returns The element at the rear or undefined if empty
   */
  getRear(): T | undefined {
    return this.list.getTail();
  }

  /**
   * Check if the deque is empty
   * @returns True if the deque is empty, false otherwise
   */
  isEmpty(): boolean {
    return this.list.isEmpty();
  }

  /**
   * Check if the deque is full
   * @returns True if the deque is full, false otherwise
   */
  isFull(): boolean {
    return this.maxSize !== undefined && this.list.size() >= this.maxSize;
  }

  /**
   * Peek at the front element without removing it
   * @returns The element at the front or undefined if empty
   */
  peek(): T | undefined {
    return this.getFront();
  }

  /**
   * Get the current size of the deque
   * @returns The number of elements in the deque
   */
  size(): number {
    return this.list.size();
  }
}
```

Maintenant, passons en revue les méthodes :

* **enqueueFront()** : Cette méthode permet d'ajouter un élément au **début** de la deque, contrairement à `SimpleQueue` ou `CircularQueue` qui ne supportent que l'ajout à l'arrière. En interne, elle utilise `list.prepend(item)` pour insérer l'élément à la tête.
    
    Cette opération rend la deque adaptée aux cas d'utilisation où les éléments doivent être poussés et extraits des deux extrémités, comme dans les systèmes d'annulation/répétition ou les planificateurs de tâches.
    
* **enqueueRear()** : Ce comportement est similaire à `enqueue` de `SimpleQueue`, ajoutant des éléments à l'arrière en utilisant `list.append(item)`.
    
    La distinction dans `Deque` est que c'est l'une des deux opérations symétriques et cela vous donne un contrôle complet à double extrémité.
    
* **dequeueFront()** : Cela retire et renvoie l'élément du **début** de la deque en utilisant `list.deleteHead()`.
    
    Bien que similaire à la méthode `dequeue` dans les files d'attente, la nommature ici est explicite pour clarifier qu'elle opère sur le début et peut être associée à une homologue de l'arrière.
    
* **dequeueRear()** : C'est une fonctionnalité unique aux deques, elle retire et renvoie l'élément à l'arrière en utilisant `list.deleteTail()`. Cela complète `dequeueFront()` et permet un comportement LIFO (comme une pile) si nécessaire.
    
* **Différence de constructeur** : Comme `SimpleQueue`, la `Deque` accepte un `maxSize` optionnel. Cela permet des configurations flexibles.
    
    Vous pouvez avoir des deques non bornées lorsque `maxSize` n'est pas fourni, ou des deques de taille fixe lorsque les contraintes sont importantes. C'est en contraste avec `CircularQueue`, qui requiert une taille maximale.
    

Une fois que vous avez complété l'implémentation, exécutez la commande suivante pour tester le module :

```bash
npm run test:file 04
```

Maintenant, vous êtes prêt à passer à la dernière section du tutoriel, où vous apprendrez la file d'attente prioritaire.

## Qu'est-ce qu'une file d'attente prioritaire ?

Une file d'attente prioritaire traite les éléments en fonction de leur priorité, et non de leur ordre d'arrivée.

Les éléments de haute priorité sont retirés en premier, comme dans une salle d'urgence où les patients avec des conditions graves sont traités avant les autres.

Modifions `src/playground/05-priority-queue.ts` :

```typescript
// 📁 src/playground/05-priority-queue.ts

import { LinkedList, NodeItem } from "./01-linked-list";

/**
 * Interface for an element with priority
 */
interface PriorityItem<T> {
  value: T;
  priority: number;
}

/**
 * Priority Queue implemented with a circular doubly linked list
 */
export class PriorityQueue<T> {
  private list: LinkedList<PriorityItem<T>>;
  private maxSize?: number;

  /**
   * @param maxSize Optional maximum size of the priority queue
   */
  constructor(maxSize?: number) {
    this.list = new LinkedList<PriorityItem<T>>();
    this.maxSize = maxSize;
  }

  /**
   * Add an element to the queue based on its priority
   * Higher priority numbers are dequeued first
   * @param value The value to add
   * @param priority The priority of the value (higher number = higher priority)
   */
  enqueue(value: T, priority: number): void {
    if (this.isFull()) {
      throw new Error("Priority queue is full");
    }

    const newItem: PriorityItem<T> = { value, priority };
    if (this.isEmpty()) {
      this.list.prepend(newItem);
      return;
    }

    let current = this.list["head"];
    let count = 0;
    while (
      current &&
      current.value.priority >= priority &&
      count < this.size()
    ) {
      current = current.next;
      count++;
    }

    if (count === this.size()) {
      this.list.append(newItem);
    } else {
      const newNode = new NodeItem(newItem);
      newNode.next = current;
      newNode.prev = current!.prev;
      if (current!.prev) {
        current!.prev.next = newNode;
      } else {
        this.list["head"] = newNode;
      }
      current!.prev = newNode;
      if (current === this.list["head"]) {
        this.list["head"] = newNode;
      }
      this.list["tail"]!.next = this.list["head"];
      this.list["head"]!.prev = this.list["tail"];
      this.list["currentSize"]++;
    }
  }

  /**
   * Remove and return the element with the highest priority from the queue
   * @returns The value with the highest priority or undefined if empty
   */
  dequeue(): T | undefined {
    return this.list.deleteHead()?.value;
  }

  /**
   * Get the element with the highest priority without removing it
   * @returns The value at the front or undefined if empty
   */
  getFront(): T | undefined {
    return this.list.getHead()?.value;
  }

  /**
   * Get the element with the lowest priority without removing it
   * @returns The value at the rear or undefined if empty
   */
  getRear(): T | undefined {
    return this.list.getTail()?.value;
  }

  /**
   * Check if the queue is empty
   * @returns True if the queue is empty, false otherwise
   */
  isEmpty(): boolean {
    return this.list.isEmpty();
  }

  /**
   * Check if the queue is full
   * @returns True if the queue is full, false otherwise
   */
  isFull(): boolean {
    return this.maxSize !== undefined && this.list.size() >= this.maxSize;
  }

  /**
   * Peek at the element with the highest priority without removing it
   * @returns The value at the front or undefined if empty
   */
  peek(): T | undefined {
    return this.getFront();
  }

  /**
   * Get the current size of the queue
   * @returns The number of elements in the queue
   */
  size(): number {
    return this.list.size();
  }
}
```

Comprendons comment les méthodes fonctionnent au sein d'une file d'attente prioritaire :

* **enqueue()** : Cette méthode insère un nouvel élément dans la file en fonction de sa `priority`. Contrairement aux autres types de files où l'ordre est basé sur l'heure d'insertion, `PriorityQueue` utilise un mécanisme de tri où les éléments avec des valeurs de `priority` plus élevées sont placés plus près du début.
    
    La méthode traverse la liste chaînée à partir de la tête, recherchant la position correcte où le nouvel élément doit être inséré pour que la liste reste triée par ordre de priorité décroissant.
    
    Elle ajuste manuellement les pointeurs `prev` et `next` pour maintenir la liste chaînée doublement circulaire intacte. Ce tri lors de l'insertion assure un accès rapide à l'élément de plus haute priorité plus tard.
    
* **dequeue()** : Cette méthode retire et renvoie l'élément avec la plus haute priorité, qui est toujours positionné au début de la liste.
    
    En interne, elle appelle `deleteHead()` puis renvoie la `value` du nœud `PriorityItem<T>`. Comme les éléments sont triés lors de l'insertion, cette opération est toujours efficace et récupère l'élément correct.
    
* **getFront()** : Ceci récupère la valeur au début de la file sans la retirer. Puisque la liste est triée par priorité décroissante, cette valeur représente toujours l'élément de plus haute priorité.
    
* **getRear()** : Ceci renvoie la valeur à l'arrière de la file, qui est l'élément avec la **plus basse** priorité. Il accède au dernier élément de la liste en utilisant `getTail()` et extrait la `value`.
    
* **isEmpty()** : Ceci vérifie si la file contient des éléments en déléguant à la méthode `isEmpty()` de la liste chaînée.
    
* **isFull()** : Ceci vérifie si la file a atteint sa taille maximale autorisée. Il compare la taille actuelle avec `maxSize` s'il est défini.
    
* **peek()** : Ceci est fonctionnellement équivalent à `getFront()`. Il fournit un nom sémantique plus clair lorsque les utilisateurs souhaitent examiner l'élément de plus haute priorité sans le retirer.
    
* **size()** : Ceci renvoie le nombre total d'éléments actuellement dans la file d'attente prioritaire. C'est utile pour surveiller la capacité ou déboguer.
    
* **Différences clés** : La file d'attente prioritaire diffère des autres types de files en imposant l'ordre lors de l'insertion basé sur une priorité numérique.
    
    Cela permet un **accès en temps constant à l'élément de plus haute priorité** mais introduit une **complexité d'insertion en temps linéaire** en raison de la nécessité de trouver l'endroit correct pour chaque nouvel élément.
    
    Elle supporte des cas d'utilisation avancés de planification et d'équilibrage de charge où l'urgence ou l'importance de la tâche compte plus que l'heure d'arrivée.
    

![Diagramme de flux illustrant le processus d'insertion d'un élément dans une file d'attente prioritaire. Il commence par vérifier si la file est vide, puis évalue la priorité, met à jour la file, la traverse si nécessaire, et vérifie continuellement la position correcte pour l'insertion.](https://cdn.hashnode.com/res/hashnode/image/upload/v1749743948626/78505f93-d7fd-4c63-b59a-5db1edcdae6c.png align="center")

Une fois que vous avez terminé l'implémentation, exécutez la commande suivante pour tester votre code :

```bash
npm run test:file 05
```

C'est tout, félicitations !

Vous avez réussi à compléter le tutoriel et à apprendre sur les files d'attente et leurs différentes variations. Excellent travail !

Avant de conclure, apprenons brièvement où utiliser les files d'attente et où les éviter. Nous discuterons également des goulots d'étranglement et des problèmes que les files d'attente peuvent créer si elles ne sont pas utilisées correctement et au bon endroit.

## **Quand utiliser les files d'attente (et quand les éviter)**

Les files d'attente sont idéales dans les scénarios où les tâches ou les données doivent être traitées dans l'ordre exact de leur arrivée, telles que la planification de travaux et les systèmes de gestion d'événements.

Par exemple, lorsque plusieurs travaux d'impression sont envoyés à une imprimante, une file d'attente peut s'assurer que chaque document est imprimé dans l'ordre où il a été soumis.

De même, les files d'attente sont utilisées dans les systèmes d'exploitation pour la gestion des tâches dans des pools de threads ou la planification du CPU (par exemple, Round Robin), où l'ordre est crucial.

Les files d'attente sont également largement utilisées dans les systèmes de communication asynchrones tels que les courtiers de messages comme RabbitMQ et Kafka.

Dans ces systèmes, les producteurs et les consommateurs opèrent de manière indépendante : un producteur pousse des messages dans la file d'attente, et un consommateur les traite plus tard.

Ce modèle est extrêmement utile dans l'architecture de microservices ou les environnements serverless, où différentes parties d'un système doivent rester faiblement couplées et hautement évolutives.

De même, dans les systèmes en temps réel comme le streaming vidéo ou l'ingestion de données de capteur, les files d'attente aident à tamponner les données entrantes pour éviter la perte de données et permettre un traitement en aval fluide.

### Quand éviter les files d'attente

Les files d'attente ne conviennent pas aux problèmes qui nécessitent un accès aléatoire aux éléments, des opérations de recherche complexes ou un tri.

Comme les files d'attente permettent généralement l'insertion à une extrémité et la suppression de l'autre, elles sont inefficaces pour les cas d'utilisation où vous devez fréquemment accéder aux éléments du milieu ou rechercher à travers tous les éléments.

Un tableau, un arbre ou une table de hachage serviraient mieux dans de tels cas.

L'utilisation inappropriée des files d'attente peut introduire une complexité inutile et des goulots d'étranglement cachés.

Par exemple, placer aveuglément une file d'attente entre chaque microservice pourrait découpler les composants mais rendre également le débogage et la gestion des pannes plus difficiles.

La sur-filage peut également entraîner des problèmes de pression de retour où les files d'attente croissent de manière incontrôlable sous forte charge, ce qui augmentera la latence ou même fera planter le système s'il n'est pas géré correctement.

Vous devez donc utiliser les files d'attente délibérément : lorsque l'ordre, la mise en tampon ou le traitement asynchrone est requis.

## Conclusion

Les files d'attente sont une structure de données de base qui fonctionnent bien lorsque vous avez besoin d'ordre et de traitement asynchrone.

Les files d'attente sont utiles pour gérer les tâches, les flux de données ou la coordination des services, et pour s'assurer que les choses fonctionnent de manière fluide et efficace.

Mais elles ne conviennent pas à tous les problèmes. Il est important de comprendre leurs avantages et leurs inconvénients pour les utiliser correctement et éviter une complexité inutile.

Merci d'avoir suivi ce tutoriel. Vous pouvez me suivre sur [X](https://x.com/Yazdun), où je partage plus de conseils utiles sur les structures de données et le développement web.

Bon codage !