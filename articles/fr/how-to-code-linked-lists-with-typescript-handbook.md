---
title: 'Comment coder des listes chaînées avec TypeScript : Un guide pour les développeurs'
subtitle: ''
author: Yazdun
co_authors: []
series: null
date: '2025-06-02T18:16:03.997Z'
originalURL: https://freecodecamp.org/news/how-to-code-linked-lists-with-typescript-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748874008549/f7890467-2c7d-4558-a3ca-6094400530bc.png
tags:
- name: TypeScript
  slug: typescript
- name: singlylinkedlist
  slug: singlylinkedlist
- name: handbook
  slug: handbook
- name: '#linkedlists'
  slug: linkedlists
- name: '#DoublyLinkedList'
  slug: doublylinkedlist
seo_title: 'Comment coder des listes chaînées avec TypeScript : Un guide pour les
  développeurs'
seo_desc: 'A linked list is a data structure where each item, called a node, contains
  data and a pointer to the next node.

  Unlike arrays, which store elements in contiguous memory, linked lists connect nodes
  that can be scattered across memory.

  In this hands-on...'
---

Une liste chaînée est une structure de données où chaque élément, appelé nœud, contient des données et un pointeur vers le nœud suivant.

Contrairement aux tableaux, qui stockent les éléments dans une mémoire contiguë, les listes chaînées relient des nœuds qui peuvent être dispersés dans la mémoire.

Dans ce tutoriel pratique, vous allez construire des listes chaînées à partir de zéro en TypeScript, en commençant par une liste simplement chaînée de base et en progressant vers des variations avancées comme les listes doublement chaînées et les listes circulaires.

## Voici ce que nous allons couvrir

1. [Prérequis](#heading-prerequisites)
    
2. [Premiers pas](#heading-premiers-pas)
    
3. [Qu'est-ce que les listes chaînées ?](#heading-questce-que-les-listes-chainees)
    
4. [Qu'est-ce qu'une liste simplement chaînée ?](#heading-questce-quune-liste-simplement-chainee)
    
    * [Comment créer une structure de nœud générique pour une liste simplement chaînée](#heading-comment-creer-une-structure-de-noeud-generique-pour-une-liste-simplement-chainee)
        
    * [Comment implémenter une liste simplement chaînée](#heading-comment-implementer-une-liste-simplement-chainee)
        
    * [Qu'est-ce que le pointeur head dans une liste chaînée ?](#heading-questce-que-le-pointeur-head-dans-une-liste-chainee)
        
    * [Comment ajouter un nœud au début d'une liste simplement chaînée](#heading-comment-ajouter-un-noeud-au-debut-dune-liste-simplement-chainee)
        
    * [Comment ajouter un nœud à la fin d'une liste simplement chaînée](#heading-comment-ajouter-un-noeud-a-la-fin-dune-liste-simplement-chainee)
        
    * [Comment supprimer le head d'une liste simplement chaînée](#heading-comment-supprimer-le-head-dune-liste-simplement-chainee)
        
    * [Comment supprimer le dernier nœud d'une liste simplement chaînée](#heading-comment-supprimer-le-dernier-noeud-dune-liste-simplement-chainee)
        
    * [Comment supprimer un nœud d'une liste simplement chaînée](#heading-comment-supprimer-un-noeud-dune-liste-simplement-chainee)
        
    * [Comment trouver un nœud dans une liste simplement chaînée](#heading-comment-trouver-un-noeud-dans-une-liste-simplement-chainee)
        
    * [Comment insérer un nœud à une position spécifique dans une liste simplement chaînée](#heading-comment-inserer-un-noeud-a-une-position-specifique-dans-une-liste-simplement-chainee)
        
    * [Comment parcourir une liste simplement chaînée](#heading-comment-parcourir-une-liste-simplement-chainee)
        
    * [Comment tester votre liste simplement chaînée](#heading-comment-tester-votre-liste-simplement-chainee)
        
5. [Qu'est-ce qu'une liste doublement chaînée ?](#heading-questce-quune-liste-doublement-chainee)
    
    * [Comment créer une structure de nœud générique pour une liste doublement chaînée](#heading-comment-creer-une-structure-de-noeud-generique-pour-une-liste-doublement-chainee)
        
    * [Comment implémenter une liste doublement chaînée](#heading-comment-implementer-une-liste-doublement-chainee)
        
    * [Comment ajouter un nœud au début d'une liste doublement chaînée](#heading-comment-ajouter-un-noeud-au-debut-dune-liste-doublement-chainee)
        
    * [Comment ajouter un nœud à la fin d'une liste doublement chaînée](#heading-comment-ajouter-un-noeud-a-la-fin-dune-liste-doublement-chainee)
        
    * [Comment supprimer le head d'une liste doublement chaînée](#heading-comment-supprimer-le-head-dune-liste-doublement-chainee)
        
    * [Comment supprimer le dernier nœud d'une liste doublement chaînée](#heading-comment-supprimer-le-dernier-noeud-dune-liste-doublement-chainee)
        
    * [Comment supprimer un nœud d'une liste doublement chaînée](#heading-comment-supprimer-un-noeud-dune-liste-doublement-chainee)
        
    * [Comment trouver un nœud dans une liste doublement chaînée](#heading-comment-trouver-un-noeud-dans-une-liste-doublement-chainee)
        
    * [Comment parcourir une liste doublement chaînée](#heading-comment-parcourir-une-liste-doublement-chainee)
        
    * [Comment insérer un nœud à une position spécifique dans une liste doublement chaînée](#heading-comment-inserer-un-noeud-a-une-position-specifique-dans-une-liste-doublement-chainee)
        
    * [Comment tester votre liste doublement chaînée](#heading-comment-tester-votre-liste-doublement-chainee)
        
6. [Qu'est-ce qu'une liste chaînée circulaire ?](#heading-questce-quune-liste-chainee-circulaire)
    
7. [Qu'est-ce qu'une liste simplement chaînée circulaire ?](#heading-questce-quune-liste-simplement-chainee-circulaire)
    
    * [Comment créer une structure de nœud générique pour une liste simplement chaînée circulaire](#heading-comment-creer-une-structure-de-noeud-generique-pour-une-liste-simplement-chainee-circulaire)
        
    * [Comment implémenter une liste simplement chaînée circulaire](#heading-comment-implementer-une-liste-simplement-chainee-circulaire)
        
    * [Comment ajouter un nœud au début d'une liste simplement chaînée circulaire](#heading-comment-ajouter-un-noeud-au-debut-dune-liste-simplement-chainee-circulaire)
        
    * [Comment ajouter un nœud à la fin d'une liste simplement chaînée circulaire](#heading-comment-ajouter-un-noeud-a-la-fin-dune-liste-simplement-chainee-circulaire)
        
    * [Comment supprimer le head d'une liste simplement chaînée circulaire](#heading-comment-supprimer-le-head-dune-liste-simplement-chainee-circulaire)
        
    * [Comment supprimer le dernier nœud d'une liste simplement chaînée circulaire](#heading-comment-supprimer-le-dernier-noeud-dune-liste-simplement-chainee-circulaire)
        
    * [Comment supprimer un nœud d'une liste simplement chaînée circulaire](#heading-comment-supprimer-un-noeud-dune-liste-simplement-chainee-circulaire)
        
    * [Comment trouver un nœud dans une liste simplement chaînée circulaire](#heading-comment-trouver-un-noeud-dans-une-liste-simplement-chainee-circulaire)
        
    * [Comment parcourir une liste simplement chaînée circulaire](#heading-comment-parcourir-une-liste-simplement-chainee-circulaire)
        
    * [Comment insérer un nœud à une position spécifique dans une liste simplement chaînée circulaire](#heading-comment-inserer-un-noeud-a-une-position-specifique-dans-une-liste-simplement-chainee-circulaire)
        
    * [Comment tester votre liste simplement chaînée circulaire](#heading-comment-tester-votre-liste-simplement-chainee-circulaire)
        
8. [Qu'est-ce qu'une liste doublement chaînée circulaire ?](#heading-questce-quune-liste-doublement-chainee-circulaire)
    
    * [Comment créer une structure de nœud générique pour une liste doublement chaînée circulaire](#heading-comment-creer-une-structure-de-noeud-generique-pour-une-liste-doublement-chainee-circulaire)
        
    * [Comment implémenter une liste doublement chaînée circulaire](#heading-comment-implementer-une-liste-doublement-chainee-circulaire)
        
    * [Comment ajouter un nœud au début d'une liste doublement chaînée circulaire](#heading-comment-ajouter-un-noeud-au-debut-dune-liste-doublement-chainee-circulaire)
        
    * [Comment ajouter un nœud à la fin d'une liste doublement chaînée circulaire](#heading-comment-ajouter-un-noeud-a-la-fin-dune-liste-doublement-chainee-circulaire)
        
    * [Comment supprimer le dernier nœud d'une liste doublement chaînée circulaire](#heading-comment-supprimer-le-dernier-noeud-dune-liste-doublement-chainee-circulaire)
        
    * [Comment supprimer le head d'une liste doublement chaînée circulaire](#heading-comment-supprimer-le-head-dune-liste-doublement-chainee-circulaire)
        
    * [Comment trouver un nœud dans une liste doublement chaînée circulaire](#heading-comment-trouver-un-noeud-dans-une-liste-doublement-chainee-circulaire)
        
    * [Comment parcourir une liste doublement chaînée circulaire](#heading-comment-parcourir-une-liste-doublement-chainee-circulaire)
        
    * [Comment supprimer un nœud d'une liste doublement chaînée circulaire](#heading-comment-supprimer-un-noeud-dune-liste-doublement-chainee-circulaire)
        
    * [Comment insérer un nœud à une position spécifique dans une liste doublement chaînée circulaire](#heading-comment-inserer-un-noeud-a-une-position-specifique-dans-une-liste-doublement-chainee-circulaire)
        
    * [Comment tester votre liste doublement chaînée circulaire](#heading-comment-tester-votre-liste-doublement-chainee-circulaire)
        
9. [Quand utiliser les listes chaînées (et quand les éviter)](#heading-quand-utiliser-les-listes-chainees-et-quand-les-eviter)
    
    * [Pourquoi utiliser les listes chaînées ?](#heading-pourquoi-utiliser-les-listes-chainees)
        
    * [Cas d'utilisation réels](#heading-cas-dutilisation-reels)
        
    * [Quand ne pas utiliser les listes chaînées](#heading-quand-ne-pas-utiliser-les-listes-chainees)
        
    * [Meilleures alternatives pour des cas spécifiques](#heading-meilleures-alternatives-pour-des-cas-specifiques)
        
10. [Conclusion](#heading-conclusion)
    

## Prérequis

1. **TypeScript** : Vous devez connaître les [bases de TypeScript](https://www.freecodecamp.org/news/learn-typescript-with-react-handbook/), telles que les interfaces, les types et les classes.
    
2. **Fondamentaux des algorithmes** : Vous devez avoir une compréhension de base des structures de données et des algorithmes. Par exemple, vous devriez être à l'aise avec l'analyse de la complexité temporelle et spatiale en utilisant la [notation Big-O](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/).
    

## **Premiers pas**

Pour commencer avec ce tutoriel, vous allez utiliser un projet de terrain de jeu conçu pour vous aider à implémenter des listes chaînées et à suivre chaque étape de manière pratique.

Clonez le projet depuis le [dépôt GitHub](https://github.com/Yazdun/fcc-linked-list) et codez en suivant le tutoriel.

La structure du projet est la suivante :

```plaintext
fcc-linked-list/
├── src/
│   ├── examples/
│   │   ├── circular-1.ts
│   │   ├── circular-2.ts
│   │   ├── doubly.ts
│   │   └── singly.ts
│   └── playground/
│       ├── circular-1.ts
│       ├── circular-2.ts
│       ├── doubly.ts
│       └── singly.ts
```

Le répertoire `examples` contient la version finale de chaque implémentation. Si vous êtes bloqué, vous pouvez consulter ces solutions en dernier recours !

## Qu'est-ce que les listes chaînées ?

Une liste chaînée est une collection d'éléments appelés nœuds, où chaque nœud contient des données et un pointeur vers le nœud suivant, le pointeur du dernier nœud pointant généralement vers `null` pour marquer la fin de la liste.

Certaines listes chaînées ont des pointeurs supplémentaires pour accélérer les modifications n'importe où dans la liste. Mais trouver un nœud peut être lent car vous devez suivre chaque pointeur un par un et ne pouvez pas sauter directement à un nœud.

Les listes chaînées sont la base des structures de données comme les files d'attente et les piles. Les listes chaînées que vous créez dans ce tutoriel supporteront de nombreuses autres structures de données.

Bien que les listes chaînées puissent effectuer de nombreuses opérations, ce tutoriel se concentrera sur les suivantes :

* **prepend** : ajoute un nœud au début de la liste.
    
* **append** : ajoute un nœud à la fin de la liste.
    
* **delete** : supprime un nœud spécifique de la liste.
    
* **deleteTail** : supprime le dernier nœud de la liste.
    
* **deleteHead** : supprime le premier nœud de la liste.
    
* **insertAt** : insère un nœud à une position spécifique.
    
* **find** : recherche et retourne un nœud dans la liste.
    
* **traverse** : visite chaque nœud de la liste, généralement de la tête à la queue, pour lire ou traiter les données.
    

Une fois que vous comprenez ces opérations de base, vous serez en mesure d'implémenter n'importe quelle opération sur vos listes chaînées.

Maintenant que vous comprenez le concept, passons à la section suivante et créons votre première liste chaînée.

## **Qu'est-ce qu'une liste simplement chaînée ?**

Dans cette première section, vous allez créer le type de liste chaînée le plus simple, appelé liste simplement chaînée.

Elle est appelée "simplement chaînée" car chaque nœud pointe vers un seul autre nœud, qui est le suivant dans la liste.

![Diagramme d'une liste simplement chaînée avec quatre nœuds étiquetés A, B, C et D. Elle commence avec la tête au nœud A et se termine avec la queue au nœud D, pointant vers NULL. Chaque nœud pointe vers le nœud suivant dans la séquence.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748530545447/8dbffb8d-c941-4c57-934b-22c0335bdd6b.png align="center")

### Comment créer une structure de nœud générique pour une liste simplement chaînée

Pour commencer à construire une liste simplement chaînée, vous avez besoin d'une structure `Node` qui contient deux parties principales :

* **data** : Stocke la valeur du nœud.
    
* **Next pointer** : Lie le nœud suivant dans la liste ou `null` s'il n'y a pas de nœud suivant.
    

Ouvrez `src/playground/singly.ts`, où vous trouverez une classe nommée `N`. Changez-la avec le code suivant pour configurer la structure du nœud :

```typescript
// 📁 src/playground/singly.ts

class N<T> {
  /** Valeur du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null = null;

  /** Crée un nœud avec la valeur donnée */
  constructor(value: T) {
    this.data = value;
  }
}
```

Voici comment fonctionne la structure du nœud :

1. Construit un `Node` [générique](https://www.typescriptlang.org/fr/docs/handbook/2/generics.html) : Utilise `<T>` pour gérer n'importe quel type de données.
    
2. Stocke la valeur du nœud : Assigne la valeur à la propriété `data`.
    
3. Lien vers le nœud suivant : Définit le pointeur `next` vers le nœud suivant ou `null` s'il n'y en a pas.
    
4. Initialise le nœud : Prend une valeur dans le constructeur et l'assigne à `data`.
    

Maintenant, vous pouvez utiliser la classe `N` pour créer des nœuds dans votre liste simplement chaînée.

### Comment implémenter une liste simplement chaînée

Utilisons la classe Node que vous venez de créer pour construire votre liste simplement chaînée.

Ouvrez `src/playground/singly.ts` où vous trouverez la classe `SinglyLinkedList` avec un pointeur `head` et plusieurs méthodes :

```typescript
// 📁 src/playground/singly.ts

class N<T> {
  /** Valeur du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null = null;

  /** Crée un nœud avec la valeur donnée */
  constructor(value: T) {
    this.data = value;
  }
}

/** Implémentation de liste simplement chaînée */
export class SinglyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null = null;

  /** Ajoute un nœud au début de la liste */
  prepend(val: T): void {}

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {}

  /** Supprime le nœud de tête */
  deleteHead(): void {}

  /** Supprime le nœud de queue */
  deleteTail(): void {}

  /** Supprime le premier nœud avec la valeur donnée */
  delete(data: T): void {}

  /** Trouve le nœud avec la valeur donnée */
  find(data: T): N<T> | null {
    return null;
  }

  /** Affiche les valeurs de tous les nœuds */
  traverse(): void {}

  /** Insère un nœud à la position donnée */
  insertAt(pos: number, data: T): void {}
}
```

D'ici la fin de cette section, vous allez créer chacune de ces méthodes. Mais d'abord, parlons du pointeur `head`.

### Qu'est-ce que le pointeur `head` dans une liste chaînée ?

Le `head` est le premier nœud de la liste, et vous commencez par le `head` lorsque vous parcourez la liste.

Vous suivez le pointeur `next` de chaque nœud jusqu'à ce que vous atteigniez le dernier nœud, où `next` est `null`.

Si `head` est `null`, la liste est vide.

Une liste simplement chaînée non vide a besoin d'un `head` pour être valide, sinon elle est cassée.

Avec cette connaissance, vous êtes prêt à commencer à travailler sur les opérations.

### Comment ajouter un nœud au début d'une liste simplement chaînée

L'objectif est d'ajouter un nouveau nœud au début de votre liste simplement chaînée et de mettre à jour le pointeur `head` vers ce nouveau nœud.

Modifiez la méthode `prepend` dans votre classe `SinglyLinkedList` dans `src/playground/singly.ts` :

```typescript
// 📁 src/playground/singly.ts

prepend(data: T): void {
  const newNode = new N(data);
  newNode.next = this.head;
  this.head = newNode;
}
```

La propriété `data` contient la valeur pour le nouveau nœud. Voici comment fonctionne `prepend` :

* Crée un nouveau nœud avec la `data` donnée.
    
* Pointe le `next` du nouveau nœud vers le `head` actuel.
    
* Définit le `head` comme étant le nouveau nœud.
    

Maintenant, le `head` pointe vers le nouveau nœud, et l'ancien `head` est le deuxième nœud de la liste.

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment ajouter un nœud à la fin d'une liste simplement chaînée

L'objectif est d'ajouter un nouveau nœud à la fin de votre liste simplement chaînée.

Changez la méthode `append` dans votre classe `SinglyLinkedList` :

```typescript
// src/playground/singly.ts

append(data: T): void {
  const newNode = new N(data);

  if (!this.head) {
    this.head = newNode;
    return;
  }

  let current = this.head;

  while (current.next) {
    current = current.next;
  }

  current.next = newNode;
}
```

Pour ajouter un nouveau nœud à la fin de la liste, vous devez d'abord trouver le dernier nœud. Dans une liste simplement chaînée non vide, le pointeur `next` du dernier nœud pointe toujours vers `null`.

En d'autres termes, pour trouver le dernier nœud dans une liste simplement chaînée non vide, recherchez le nœud dont le pointeur `next` est `null`.

Pour ajouter un nouveau nœud, vous devez suivre ces étapes :

* Créez un nouveau nœud avec la valeur donnée.
    
* Vérifiez si le `head` est `null`. Si c'est le cas, la liste est vide, donc définissez le `head` comme étant le nouveau nœud.
    
* Si la liste a des nœuds, trouvez le dernier nœud en parcourant la liste.
    
* Commencez avec un nouveau pointeur appelé `current` au `head`.
    
* Continuez à déplacer `current` vers le nœud `next` jusqu'à ce que vous atteigniez un nœud sans nœud `next` (où `next` est `null`).
    
* Reliez le `next` du dernier nœud au nouveau nœud.
    

Maintenant, le nouveau nœud est le dernier nœud, et son `next` pointe vers `null`.

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le dernier nœud.

### Comment supprimer le `head` d'une liste simplement chaînée

L'objectif est de supprimer le `head` de la liste. Allez-y et mettez à jour la méthode `deleteHead` dans votre classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

deleteHead(): void {
  if (this.head) {
    this.head = this.head.next;
  }
}
```

Vous devez simplement déplacer le pointeur `head` vers le deuxième nœud de la liste. Le deuxième nœud est `head.next`, donc tout ce que vous avez à faire est de définir `head` comme étant `head.next`.

Et voilà, l'ancien `head` est supprimé !

### Comment supprimer le dernier nœud d'une liste simplement chaînée

L'objectif est de supprimer le dernier nœud, appelé `tail`, de votre liste simplement chaînée.

Le `tail` est le nœud dont le pointeur `next` est `null`.

Modifiez la méthode `deleteTail` dans votre classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

deleteTail(): void {
  if (!this.head) return;

  if (!this.head.next) {
    this.head = null;
    return;
  }

  let current = this.head;

  while (current.next && current.next.next) {
    current = current.next;
  }
  current.next = null;
}
```

Voici comment fonctionne `deleteTail` :

1. Si la liste est vide, elle arrête l'opération car il n'y a pas de `tail` à supprimer.
    
2. Si le `next` du `head` est `null`, la liste n'a qu'un seul nœud, qui sert à la fois de `head` et de `tail`. Pour vider la liste, il suffit de définir le `head` comme étant `null`.
    
3. Si la liste a plus d'un nœud, elle trouve le nœud juste avant le `tail`. Elle commence avec un pointeur appelé `current` au `head`.
    
4. Elle déplace `current` vers l'avant jusqu'à ce que son nœud `next` soit le `tail`. Ensuite, elle définit le pointeur `next` de ce nœud comme étant `null` pour en faire le `tail`.
    
5. Maintenant, le dernier nœud est supprimé, et le `next` du nouveau `tail` pointe vers `null`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud avant le `tail`.

### Comment supprimer un nœud d'une liste simplement chaînée

L'objectif est de supprimer la première occurrence d'un nœud avec une valeur donnée de votre liste simplement chaînée.

Commençons par changer la méthode `delete` dans votre classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

delete(data: T): void {
  if (!this.head) return;

  if (this.head.data === data) {
    this.head = this.head.next;
    return;
  }

  let current = this.head;

  while (current.next) {
    if (current.next.data === data) {
      current.next = current.next.next;
      return;
    }
    current = current.next;
  }
}
```

Voici comment fonctionne `delete` :

* La propriété `data` est la valeur à trouver et à supprimer.
    
* Si la liste est vide, elle arrête l'opération car il n'y a rien à supprimer.
    
* Elle vérifie si la valeur du nœud `head` correspond à la propriété `data`. Si c'est le cas, vous n'avez pas besoin de rechercher plus loin car le `head` est le nœud à supprimer, donc elle déplace le `head` vers `head.next` pour supprimer l'ancien `head`.
    
* Si le `head` ne correspond pas, elle crée un nouveau pointeur appelé `current` commençant au `head`.
    
* Elle déplace `current` à travers la liste tant qu'il y a un nœud suivant, et vérifie si la valeur du nœud suivant correspond à la propriété `data`.
    
* Si une correspondance est trouvée, elle supprime le nœud `next` en connectant le `next` de `current` au nœud qui le suit.
    
* Cela retire le nœud correspondant de la liste car `current` pointe maintenant vers le nœud suivant celui que vous souhaitez supprimer.
    
* Si aucune correspondance n'est trouvée, elle continue à déplacer `current` vers le nœud suivant jusqu'à la fin.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud.

### Comment trouver un nœud dans une liste simplement chaînée

L'objectif est de trouver la première occurrence d'un nœud avec la valeur donnée.

Modifiez la méthode `find` à l'intérieur de la classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

find(data: T): N<T> | null {
  if (!this.head) return null;

  let current: N<T> | null = this.head;

  while (current) {
    if (current.data === data) return current;
    current = current.next;
  }

  return null;
}
```

La propriété `data` est la valeur que vous recherchez.

Voici comment fonctionne `find` :

* Si le `head` est `null`, elle retourne `null` car la liste est vide et il n'y a pas de nœuds à trouver.
    
* Elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle déplace `current` à travers la liste tant qu'il existe et vérifie si sa valeur correspond à `data`.
    
* Si une correspondance est trouvée, elle retourne le nœud `current` car il contient la valeur que vous recherchez.
    
* Si aucune correspondance n'est trouvée, elle déplace `current` vers le nœud `next` et continue à vérifier jusqu'à la fin.
    
* Si vous atteignez la fin sans correspondance, elle retourne `null`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud.

### Comment insérer un nœud à une position spécifique dans une liste simplement chaînée

L'objectif est d'ajouter un nouveau nœud à une position spécifique dans votre liste simplement chaînée.

Modifiez la méthode `insertAt` dans votre classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

insertAt(pos: number, data: T): void {
  const newNode = new N(data);
  let current: N<T> | null = this.head;

  if (pos < 0) throw new Error("failed");

  if (pos === 0) {
    newNode.next = this.head;
    this.head = newNode;
    return;
  }

  let idx = 0;

  while (current && idx < pos - 1) {
    current = current.next;
    idx++;
  }

  if (!current) throw new Error("failed");

  newNode.next = current.next;
  current.next = newNode;
}
```

La propriété `pos` est la position dans la liste, et `data` est la valeur.

Voici comment fonctionne `insertAt` :

* Elle crée un nouveau nœud avec la valeur donnée.
    
* Si la `pos` est négative, elle arrête l'opération avec une erreur car ce n'est pas valide.
    
* Si `pos` est 0, elle insère le nœud au début. Elle lie le `next` du nouveau nœud au `head` actuel, fait du nouveau nœud le `head`, et arrête l'opération.
    
* Si la position n'est pas 0, alors elle crée un pointeur appelé `current` au début et un compteur appelé `idx` à 0.
    
* Elle déplace `current` à travers la liste jusqu'à ce que vous atteigniez le nœud juste avant la position souhaitée, en augmentant `idx` au fur et à mesure.
    
* Si vous atteignez la fin de la liste ou si la position est trop grande, elle arrête avec une erreur.
    
* Elle lie le `next` du nouveau nœud au nœud qui est actuellement après le nœud `current`.
    
* Elle lie le `next` de `current` au nouveau nœud pour l'insérer dans la liste.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir la liste pour trouver le point d'insertion.

### Comment parcourir une liste simplement chaînée

L'objectif est de journaliser les valeurs de tous les nœuds dans votre liste simplement chaînée.

Modifiez la méthode `traverse` à l'intérieur de la classe `SinglyLinkedList` :

```typescript
// 📁 src/playground/singly.ts

traverse(): void {
  let current = this.head;
  while (current) {
    console.log(current.data);
    current = current.next;
  }
}
```

Voici comment fonctionne `traverse` :

* Il commence par définir le pointeur `current` sur `head` pour commencer au début de la liste. Si `head` est `null`, la liste est vide.
    
* S'il y a des nœuds dans la liste, il utilise une boucle `while (current)` pour visiter chacun d'eux. Dans chaque boucle, il journalise `current.data` pour afficher la valeur du nœud, puis déplace le pointeur `current` vers `current.next` pour passer au nœud suivant.
    
* Cette boucle continue jusqu'à ce que `current` devienne `null`, ce qui signifie que vous avez atteint la fin de la liste.
    

Globalement, la complexité temporelle est O(n) en raison de la traversée de toute la liste.

### Comment tester votre liste simplement chaînée

Félicitations ! Vous avez réussi à créer votre liste simplement chaînée.

Voici à quoi devrait ressembler le code final :

```typescript
// 📁 src/playground/singly.ts

/** Nœud pour liste simplement chaînée */
class N<T> {
  /** Valeur du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null = null;

  /** Crée un nœud avec la valeur donnée */
  constructor(value: T) {
    this.data = value;
  }
}

/** Implémentation de liste simplement chaînée */
export class SinglyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null = null;

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {
    const newNode = new N(data);
    newNode.next = this.head;
    this.head = newNode;
  }

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {
    const newNode = new N(data);

    if (!this.head) {
      this.head = newNode;
      return;
    }

    let current = this.head;

    while (current.next) {
      current = current.next;
    }

    current.next = newNode;
  }

  /** Supprime le nœud de tête */
  deleteHead(): void {
    if (this.head) {
      this.head = this.head.next;
    }
  }

  /** Supprime le nœud de queue */
  deleteTail(): void {
    if (!this.head) return;

    if (!this.head.next) {
      this.head = null;
      return;
    }

    let current = this.head;
    while (current.next && current.next.next) {
      current = current.next;
    }

    current.next = null;
  }

  /** Supprime le premier nœud avec la valeur donnée */
  delete(data: T): void {
    if (!this.head) return;

    if (this.head.data === data) {
      this.head = this.head.next;
      return;
    }

    let current = this.head;

    while (current.next) {
      if (current.next.data === data) {
        current.next = current.next.next;
        return;
      }

      current = current.next;
    }
  }

  /** Trouve le nœud avec la valeur donnée */
  find(data: T): N<T> | null {
    if (!this.head) return null;

    let current: N<T> | null = this.head;

    while (current) {
      if (current.data === data) return current;
      current = current.next;
    }

    return null;
  }

  /** Affiche les valeurs de tous les nœuds */
  traverse(): void {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.next;
    }
  }

  /** Insère un nœud à la position donnée */
  insertAt(pos: number, data: T): void {
    const newNode = new N(data);
    let current: N<T> | null = this.head;

    if (pos < 0) throw new Error("failed");

    if (pos === 0) {
      newNode.next = this.head;
      this.head = newNode;
      return;
    }

    let idx = 0;

    while (current && idx < pos - 1) {
      current = current.next;
      idx++;
    }

    if (!current) throw new Error("failed");

    newNode.next = current.next;
    current.next = newNode;
  }
}
```

Après avoir terminé l'implémentation, exécutez la commande suivante pour tester votre liste simplement chaînée :

```bash
npm run test:file singly
```

Si des tests échouent, vous pouvez utiliser `src/examples/singly.ts` pour trouver et corriger le problème, puis exécuter les tests à nouveau.

C'est tout ! Vous avez réussi à construire une liste chaînée et appris comment créer des nœuds qui pointent vers le nœud suivant et effectuer des opérations sur eux.

Bien que les listes simplement chaînées soient utiles, elles ont une grande limitation : chaque nœud ne pointe que vers le nœud suivant.

Ne serait-ce pas génial si les nœuds pouvaient également pointer vers le nœud précédent ? Cela nous permettrait de faire beaucoup plus d'opérations avec notre liste chaînée.

C'est exactement ce que vous allez apprendre dans la section suivante.

## Qu'est-ce qu'une liste doublement chaînée ?

Dans cette section, vous allez créer une liste doublement chaînée. Elle est appelée "doublement chaînée" car chaque nœud pointe vers les nœuds suivant et précédent dans la liste.

![Diagramme d'une liste doublement chaînée avec des nœuds étiquetés A à D. Les flèches indiquent les connexions "next" et "prev" entre les nœuds, avec le nœud A comme tête et le nœud D comme queue. La queue pointe vers NULL.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748530715135/52d0559e-0767-45cf-93b6-b236ba890740.png align="center")

Tout d'abord, examinons la structure de nœud dans une liste doublement chaînée, puis vous implémenterez les opérations dans la liste chaînée réelle.

### Comment créer une structure de nœud générique pour une liste doublement chaînée

La structure de nœud dans les listes doublement chaînées est similaire à celle des listes simplement chaînées, sauf qu'elle a un pointeur supplémentaire pour pointer vers le nœud précédent.

La structure de nœud dans une liste doublement chaînée se compose de trois parties :

* **data** : Stocke la valeur du nœud.
    
* **Next pointer** : Lie le nœud suivant dans la liste ou `null` s'il n'y a pas de nœud suivant.
    
* **Previous pointer** : Lie le nœud précédent dans la liste ou `null` s'il n'y a pas de nœud précédent.
    

Ouvrez `src/playground/doubly.ts` et modifiez la classe `N` avec le code suivant pour configurer la structure du nœud :

```typescript
// 📁 src/playground/doubly.ts

export class N<T> {
  data: T;
  next: N<T> | null;
  prev: N<T> | null;

  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}
```

Voici comment fonctionne la structure du nœud :

* Elle construit un [générique](https://www.typescriptlang.org/fr/docs/handbook/2/generics.html) `Node` : Utilise `<T>` pour gérer n'importe quel type de données, comme des nombres ou des chaînes.
    
* Elle stocke la valeur du nœud : Assigne la valeur à la propriété `data`.
    
* Elle lie le nœud suivant : Définit le pointeur `next` vers le nœud suivant ou `null` s'il n'y en a pas.
    
* Elle lie le nœud précédent : Définit le pointeur `prev` vers le nœud précédent ou `null` s'il n'y en a pas.
    

Ensuite, le `constructor` définit la `data` lorsque vous créez un nouveau nœud.

### Comment implémenter une liste doublement chaînée

Maintenant que la classe Node est prête, vous pouvez commencer à construire la liste réelle.

Ouvrez `src/playground/doubly.ts` et jetez un œil à la classe `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

export class N<T> {
  data: T;
  next: N<T> | null;
  prev: N<T> | null;

  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

export class DoublyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null;
  /** Nœud de queue */
  public tail: N<T> | null;
  /** Longueur de la liste */
  public len: number;

  /** Crée une liste vide */
  constructor() {
    this.head = null;
    this.tail = null;
    this.len = 0;
  }

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {}

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {}

  /** Supprime et retourne les données du nœud de tête */
  deleteHead(): T | null {
    return null;
  }

  /** Supprime et retourne les données du nœud de queue */
  deleteTail(): T | null {
    return null;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    return false;
  }

  /** Trouve le nœud à l'index donné */
  find(idx: number): N<T> | null {
    return null;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(dir: "forward" | "backward" = "forward"): T[] {
    return [];
  }

  /** Insère un nœud à l'index donné */
  insertAt(idx: number, data: T): boolean {
    return false;
  }
}
```

Cette classe a deux pointeurs, `head` et `tail`, et une variable appelée `len` :

* `head` : Cela pointe toujours vers le premier élément de votre liste.
    
* `tail` : Cela pointe toujours vers le dernier élément de votre liste.
    
* `len` : Cela représente la longueur de votre liste chaînée. Chaque fois que vous modifiez la liste en ajoutant ou en supprimant un nœud, vous devez mettre à jour `len` pour refléter la longueur correcte.
    

Une liste doublement chaînée valide aura toujours un `head` et un `tail`. Si soit le `head` soit le `tail` est `null`, cela signifie que la liste est vide et n'a pas de nœuds.

C'est pourquoi vous définissez initialement le `head` et le `tail` à `null`. Lorsque vous créez une liste, elle est vide au début. Au fur et à mesure que vous ajoutez un nœud à la liste, vous mettez à jour les pointeurs pour pointer vers le nouveau nœud.

Maintenant, passons à la section suivante et voyons comment vous pouvez ajouter un nœud à votre liste doublement chaînée.

### Comment ajouter un nœud au début d'une liste doublement chaînée

L'objectif est d'ajouter un nouveau nœud au début de votre liste doublement chaînée et de mettre à jour le pointeur `head` vers ce nouveau nœud.

Modifiez la méthode `prepend` dans votre classe `DoublyLinkedList` située dans `src/playground/doubly.ts` :

```typescript
// 📁 src/playground/doubly.ts

prepend(data: T): void {
  let newNode = new N(data);

  if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
  } else {
    let prevHead = this.head;
    newNode.next = prevHead;
    prevHead.prev = newNode;
    this.head = newNode;
  }

  this.len++;
}
```

La propriété `data` contient la valeur pour le nouveau nœud. Voici comment fonctionne `prepend` :

* Elle crée un nouveau nœud avec les données données.
    
* Si la liste est vide (`head` est `null`), elle définit à la fois le `head` et le `tail` comme étant le nouveau nœud.
    
* Si la liste a des nœuds, elle pointe le `next` du nouveau nœud vers le `head` actuel.
    
* Elle pointe le `prev` du `head` actuel vers le nouveau nœud.
    
* Elle définit le `head` comme étant le nouveau nœud.
    
* Elle augmente la longueur de la liste de un.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment ajouter un nœud à la fin d'une liste doublement chaînée

L'objectif est d'ajouter un nouveau nœud à la fin de votre liste doublement chaînée et de mettre à jour le pointeur `tail` vers ce nouveau nœud.

Modifiez la méthode append dans votre `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

append(data: T): void {
  let newNode = new N(data);
  if (!this.head) {
    this.head = newNode;
    this.tail = newNode;
  } else {
    this.tail!.next = newNode;
    newNode.prev = this.tail;
    this.tail = newNode;
  }

  this.len++;
}
```

Voici comment fonctionne `append` :

* La propriété `data` contient la valeur pour le nouveau nœud.
    
* Elle crée un nouveau nœud avec les données données.
    
* Elle vérifie si la liste est vide ( `head` est `null` ), et définit à la fois le `head` et le `tail` comme étant le nouveau nœud.
    
* Si la liste a des nœuds, elle pointe le `next` du `tail` actuel vers le nouveau nœud.
    
* Elle pointe le `prev` du nouveau nœud vers le `tail` actuel.
    
* Elle définit le `tail` comme étant le nouveau nœud.
    
* Elle augmente la longueur de la liste de un.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment supprimer le head d'une liste doublement chaînée

L'objectif est de supprimer le premier nœud de votre liste doublement chaînée et de retourner ses données.

Modifiez la méthode `deleteHead` dans votre `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

deleteHead(): T | null {
  if (!this.head) return null;

  let removedItem = this.head;

  if (this.len === 1) {
    this.head = null;
    this.tail = null;
  } else {
    this.head = removedItem.next;
    this.head!.prev = null;
    removedItem.next = null;
  }

  this.len--;

  return removedItem.data;
}
```

Voici comment fonctionne `deleteHead` :

* Si la liste est vide, elle retourne `null` car il n'y a pas de nœud à supprimer.
    
* Elle crée une nouvelle variable appelée `removedItem` et stocke le nœud `head` dedans comme l'élément à supprimer.
    
* Si la longueur de la liste est 1, cela signifie que la liste n'a qu'un seul nœud, qui agit à la fois comme `head` et `tail` de la liste. Dans ce cas, elle définit à la fois le `head` et le `tail` comme étant `null`.
    
* Si la liste a plusieurs nœuds, elle déplace le `head` vers le nœud suivant.
    
* Elle définit le `prev` du nouveau `head` comme étant `null` puisque c'est maintenant le premier nœud.
    
* Elle efface le pointeur `next` du nœud supprimé.
    
* Elle diminue la longueur de la liste de un.
    
* Elle retourne les données du nœud supprimé.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment supprimer le dernier nœud d'une liste doublement chaînée

L'objectif est de supprimer le dernier nœud de votre liste doublement chaînée et de retourner ses données.

Modifiez la méthode `deleteTail` dans votre `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

deleteTail(): T | null {
  if (!this.tail) return null;

  let removedItem = this.tail;

  if (this.len === 1) {
    this.head = null;
    this.tail = null;
  } else {
    this.tail = this.tail.prev;
    this.tail!.next = null;
    removedItem.prev = null;
  }

  this.len--;

  return removedItem.data;
}
```

Voici comment fonctionne `deleteTail` :

* Elle vérifie si la liste est vide. Si le `tail` est `null`, elle retourne `null` car il n'y a pas de nœud à supprimer.
    
* Elle sauvegarde le nœud `tail` dans une variable nommée `removedItem` comme le nœud à supprimer.
    
* Elle vérifie si la liste a un seul nœud. Si la longueur est 1, elle définit à la fois `head` et `tail` comme étant `null`.
    
* Si la liste a plusieurs nœuds, elle déplace le `tail` vers le nœud précédent.
    
* Elle définit le `next` du nouveau `tail` comme étant `null` puisque c'est maintenant le dernier nœud.
    
* Elle efface le pointeur `prev` du nœud supprimé.
    
* Elle diminue la longueur de la liste de un.
    
* Elle retourne les données du nœud supprimé.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment supprimer un nœud d'une liste doublement chaînée

L'objectif est de supprimer le premier nœud avec la valeur donnée de votre liste doublement chaînée et de retourner `true` si l'opération est réussie.

Modifiez la méthode `delete` dans votre `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

delete(data: T): boolean {
  let current = this.head;

  if (!current) return false;

  if (current.data === data) {
    this.head = current.next;
    if (this.head) this.head.prev = null;
    else this.tail = null;
    this.len--;
    return true;
  }

  while (current.next) {
    if (current.next.data === data) {
      let nodeToRemove = current.next;
      current.next = nodeToRemove.next;
      if (current.next) current.next.prev = current;
      else this.tail = current;
      nodeToRemove.next = null;
      nodeToRemove.prev = null;
      this.len--;
      return true;
    }
    current = current.next;
  }

  return false;
}
```

La propriété `data` est la valeur à trouver et à supprimer.

Voici comment fonctionne `delete` :

* Elle vérifie si la liste est vide - si le `head` est `null`, elle retourne `false` car il n'y a rien à supprimer.
    
* Elle vérifie si la valeur du nœud `head` correspond à `data` et si c'est le cas, elle déplace le `head` vers le nœud suivant, définit le `prev` du nouveau `head` comme étant `null` ou efface le `tail` si la liste est vide, diminue la longueur, et retourne `true`.
    
* Si le `head` ne correspond pas, elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle déplace `current` à travers la liste tant qu'un nœud suivant existe, vérifiant si la valeur du nœud suivant correspond à `data`.
    
* Si une correspondance est trouvée, elle saute le nœud suivant en liant le `next` de `current` au nœud qui le suit.
    
* Elle met à jour le `prev` du nœud suivant comme étant `current` ou définit le `tail` comme étant `current` si c'est le dernier nœud, efface les pointeurs du nœud supprimé, diminue la longueur, et retourne `true`.
    
* Si aucune correspondance n'est trouvée, elle déplace `current` vers le nœud suivant et continue à vérifier.
    
* Si vous atteignez la fin sans correspondance, elle retourne `false`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud.

### Comment trouver un nœud dans une liste doublement chaînée

L'objectif est de trouver le nœud à une position spécifique dans votre liste doublement chaînée.

Modifiez la méthode `find` dans votre `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

find(idx: number): N<T> | null {
  if (idx < 0 || idx >= this.len) return null;

  let current: N<T> | null = this.head;

  if (idx <= this.len / 2) {
    current = this.head;
    for (let i = 0; i < idx; i++) {
      current = current!.next;
    }
  } else {
    current = this.tail;
    for (let i = this.len - 1; i > idx; i--) {
      current = current?.prev ?? null;
    }
  }

  return current;
}
```

La propriété `idx` est la position dans la liste, en commençant à 0.

Voici comment fonctionne `find` :

* Elle vérifie si l'index est valide. Si `idx` est négatif ou trop grand, elle retourne `null` car aucun nœud n'existe.
    
* Elle commence un nouveau pointeur appelé `current` au `head`.
    
* Elle vérifie si `idx` est dans la première moitié de la liste. Si c'est le cas, elle déplace `current` vers l'avant `idx` fois en utilisant le pointeur `next`.
    
* Si `idx` est dans la deuxième moitié, elle commence `current` au `tail` et se déplace vers l'arrière jusqu'à la position en utilisant le pointeur `prev`.
    
* Elle retourne le nœud `current`, qui est à l'index donné, ou `null` si la liste est vide.
    

Cela s'exécute en temps O(n) car vous devrez peut-être vous déplacer à travers la moitié de la liste pour trouver le nœud.

### Comment parcourir une liste doublement chaînée

L'objectif est de retourner un tableau de toutes les données des nœuds dans votre liste doublement chaînée, soit vers l'avant soit vers l'arrière. Modifiez la méthode traverse dans votre classe `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

traverse(dir: "forward" | "backward" = "forward"): T[] {
  const isForward = dir === "forward";
  let current = isForward ? this.head : this.tail;
  const result: T[] = [];

  while (current) {
    result.push(current.data);
    current = isForward ? current.next : current.prev;
  }

  return result;
}
```

La propriété `dir` définit si vous allez vers l'avant (de `head` à `tail`) ou vers l'arrière (de `tail` à `head`).

Voici comment fonctionne `traverse` :

* Elle vérifie la direction et définit un drapeau à vrai si vous vous déplacez vers l'avant.
    
* Elle commence un nouveau pointeur appelé `current` au `head` si vous allez vers l'avant, ou au `tail` si vous allez vers l'arrière.
    
* Elle crée un tableau vide pour stocker les données des nœuds.
    
* Tant que `current` existe, elle ajoute ses données au tableau.
    
* Elle déplace `current` vers le nœud suivant si vous allez vers l'avant, ou vers le nœud précédent si vous allez vers l'arrière.
    
* Elle retourne le tableau avec toutes les données des nœuds.
    

Cela s'exécute en temps O(n) car vous devrez peut-être visiter chaque nœud de la liste.

### **Comment insérer un nœud à une position spécifique dans une liste doublement chaînée**

L'objectif est d'ajouter un nouveau nœud à un index spécifique dans votre liste doublement chaînée.

Modifiez la méthode `insertAt` dans votre classe `DoublyLinkedList` :

```typescript
// 📁 src/playground/doubly.ts

insertAt(idx: number, data: T): boolean {
  if (idx < 0 || idx > this.len) return false;

  if (idx === 0) {
    this.prepend(data);
    return true;
  }

  if (idx === this.len) {
    this.append(data);
    return true;
  }

  let newNode = new N(data);
  let current = this.find(idx);

  if (!current) return false;

  newNode.next = current;
  newNode.prev = current?.prev ?? null;
  current.prev!.next = newNode;
  current.prev = newNode;

  this.len++;

  return true;
}
```

La propriété `idx` est la position dans la liste, et `data` est la valeur.

Voici comment fonctionne `insertAt` :

* Elle vérifie si l'index est invalide, si `idx` est négatif ou supérieur à la longueur de la liste, elle retourne `false`.
    
* Si l'index est 0, elle insère le nœud au début. Elle lie le `next` du nouveau nœud au `head` actuel, fait du nouveau nœud le `head`, et arrête l'opération.
    
* Si la position n'est pas 0, alors elle crée un pointeur appelé `current` au `head` et un compteur appelé `idx` à 0.
    
* Elle déplace `current` à travers la liste jusqu'à ce que vous atteigniez le nœud juste avant la position souhaitée, en augmentant `idx` au fur et à mesure.
    
* Si vous atteignez la fin de la liste ou si la position est trop grande, elle arrête avec une erreur.
    
* Elle lie le `next` du nouveau nœud au nœud qui est actuellement après le nœud `current`.
    
* Elle lie le `next` de `current` au nouveau nœud pour l'insérer dans la liste.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir la liste pour trouver le point d'insertion.

### Comment tester votre liste doublement chaînée

Super, quel excellent progrès ! Vous avez réussi à implémenter votre liste doublement chaînée. Voici à quoi devrait ressembler l'implémentation finale :

```typescript
// 📁 src/playground/doubly.ts
export class N<T> {
  data: T;
  next: N<T> | null;
  prev: N<T> | null;

  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

/** Implémentation de liste doublement chaînée */
export class DoublyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null;
  /** Nœud de queue */
  public tail: N<T> | null;
  /** Longueur de la liste */
  public len: number;

  /** Crée une liste vide */
  constructor() {
    this.head = null;
    this.tail = null;
    this.len = 0;
  }

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {
    let newNode = new N(data);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      let prevHead = this.head;
      newNode.next = prevHead;
      prevHead.prev = newNode;
      this.head = newNode;
    }

    this.len++;
  }

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {
    let newNode = new N(data);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail!.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }

    this.len++;
  }

  /** Supprime et retourne les données du nœud de tête */
  deleteHead(): T | null {
    if (!this.head) return null;

    let removedItem = this.head;

    if (this.len === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = removedItem.next;
      this.head!.prev = null;
      removedItem.next = null;
    }

    this.len--;

    return removedItem.data;
  }

  /** Supprime et retourne les données du nœud de queue */
  deleteTail(): T | null {
    if (!this.tail) return null;

    let removedItem = this.tail;

    if (this.len === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail!.next = null;
      removedItem.prev = null;
    }

    this.len--;

    return removedItem.data;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    let current = this.head;

    if (!current) return false;

    if (current.data === data) {
      this.head = current.next;
      if (this.head) this.head.prev = null;
      else this.tail = null;
      this.len--;
      return true;
    }

    while (current.next) {
      if (current.next.data === data) {
        let nodeToRemove = current.next;
        current.next = nodeToRemove.next;
        if (current.next) current.next.prev = current;
        else this.tail = current;
        nodeToRemove.next = null;
        nodeToRemove.prev = null;
        this.len--;
        return true;
      }
      current = current.next;
    }

    return false;
  }

  /** Trouve le nœud à l'index donné */
  find(idx: number): N<T> | null {
    if (idx < 0 || idx >= this.len) return null;

    let current: N<T> | null = this.head;

    if (idx <= this.len / 2) {
      current = this.head;
      for (let i = 0; i < idx; i++) {
        current = current!.next;
      }
    } else {
      current = this.tail;
      for (let i = this.len - 1; i > idx; i--) {
        current = current?.prev ?? null;
      }
    }

    return current;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(dir: "forward" | "backward" = "forward"): T[] {
    const isForward = dir === "forward";
    let current = isForward ? this.head : this.tail;
    const result: T[] = [];

    while (current) {
      result.push(current.data);
      current = isForward ? current.next : current.prev;
    }

    return result;
  }

  /** Insère un nœud à l'index donné */
  insertAt(idx: number, data: T): boolean {
    if (idx < 0 || idx > this.len) return false;

    if (idx === 0) {
      this.prepend(data);
      return true;
    }

    if (idx === this.len) {
      this.append(data);
      return true;
    }

    let newNode = new N(data);
    let current = this.find(idx);

    if (!current) return false;

    newNode.next = current;
    newNode.prev = current?.prev ?? null;
    current.prev!.next = newNode;
    current.prev = newNode;

    this.len++;

    return true;
  }
}
```

Exécutez la commande suivante pour vous assurer que votre implémentation est correcte :

```bash
npm run test:file doubly
```

Si les tests s'exécutent avec succès, vous êtes prêt à continuer ! Si des tests échouent, vérifiez `src/examples/doubly.ts`, corrigez le problème et exécutez les tests à nouveau.

Vous avez appris comment implémenter un nœud lié avec deux pointeurs. Les listes doublement chaînées sont utiles dans de nombreux scénarios, mais comme les listes simplement chaînées, elles ont une limitation que vous devez considérer.

Disons que vous avez une playlist musicale, et chaque fois que vous atteignez la fin, vous voulez revenir à la première chanson au lieu de vous arrêter.

Dans les listes simplement et doublement chaînées, une fois que vous atteignez la fin, il n'y a aucun moyen de revenir au premier élément car le dernier nœud pointe vers `null`. Alors, que ferez-vous si vous voulez créer une playlist musicale en utilisant des listes chaînées ?

C'est ce que vous allez apprendre dans la section suivante de ce tutoriel !

## Qu'est-ce qu'une liste chaînée circulaire ?

Jusqu'à présent, vous avez appris les listes simplement et doublement chaînées, où le dernier élément pointe toujours vers `null`.

Parfois, vous avez besoin de revenir au premier élément après avoir atteint le dernier. Dans ce cas, le pointeur `next` de la `queue` doit pointer vers le `head` au lieu de `null`.

C'est ce qu'est une liste chaînée circulaire. Dans les listes chaînées circulaires, la `queue` pointe vers le `head`, vous permettant de continuer à parcourir la liste sans vous arrêter.

Dans les 2 sections suivantes, vous allez apprendre deux types de listes chaînées circulaires :

* **Liste simplement chaînée circulaire** : Chaque nœud a un pointeur vers le nœud suivant, et la `queue` pointe toujours vers le `head`.
    
* **Liste doublement chaînée circulaire** : Chaque nœud a deux pointeurs vers les nœuds suivant et précédent. La `queue` pointe vers le `head` comme son nœud suivant, et le `head` pointe vers la `queue` comme son nœud précédent.
    

Maintenant, plongeons plus profondément et apprenons comment créer chacune de ces listes.

## Qu'est-ce qu'une liste simplement chaînée circulaire ?

Dans une liste simplement chaînée circulaire, chaque nœud n'a qu'un seul pointeur qui pointe vers le nœud suivant dans la liste. La principale différence entre une liste simplement chaînée et une liste simplement chaînée circulaire est le nœud `queue`.

Dans une liste simplement chaînée circulaire, la `queue` pointe toujours vers le `head`, formant un cercle qui permet un bouclage continu à travers la liste.

![Diagramme d'une liste simplement chaînée circulaire avec des nœuds étiquetés A, B, C et D. Les flèches indiquent les pointeurs "next", formant une boucle. Le head pointe vers le nœud A, et la queue pointe vers le nœud D.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748531277470/15e7aafc-e499-47ec-a0b7-2b0e61867162.png align="center")

Maintenant, examinons la structure de nœud dans une liste simplement chaînée circulaire.

### Comment créer une structure de nœud générique pour une liste simplement chaînée circulaire

La structure `Node` dans une liste simplement chaînée circulaire se compose de deux parties : les données et un pointeur vers le nœud suivant.

La propriété `data` contient la valeur du nœud, et `next` pointe vers le nœud suivant dans la liste.

Ouvrez `src/playground/circular-1.ts` et modifiez la classe `N` :

```typescript
/** Nœud pour liste simplement chaînée circulaire */
export class N<T> {
  /** Données du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null;

  /** Crée un nœud avec les données données */
  constructor(data: T) {
    this.data = data;
    this.next = null;
  }
}
```

Voici comment fonctionne la structure du nœud :

* Elle construit un [générique](https://www.typescriptlang.org/fr/docs/handbook/2/generics.html) Node : Utilise `<T>` pour gérer n'importe quel type de données, comme des nombres ou des chaînes.
    
* Elle stocke la valeur du nœud : Assigne la valeur à la propriété data.
    
* Elle lie le nœud suivant : Définit le pointeur `next` vers le nœud suivant, `null` uniquement pendant l'initialisation. Dans une liste circulaire valide, `next` est toujours connecté à un nœud.
    
* Elle initialise le nœud : Prend une valeur dans le constructeur et l'assigne à `data`.
    

Dans une liste chaînée circulaire valide, `next` ne reste jamais `null`.

### Comment implémenter une liste simplement chaînée circulaire

Une fois que vous avez créé votre structure de nœud, vous pouvez commencer à implémenter la liste chaînée.

Pour commencer, ouvrons `src/playground/circular-1.ts`, où vous trouverez la classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

export class N<T> {
  data: T;
  next: N<T> | null;
  prev: N<T> | null;

  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

export class CircularSinglyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null = null;

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {}

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {}

  /** Supprime le nœud de tête */
  deleteHead(): void {}

  /** Supprime le nœud de queue */
  deleteTail(): boolean {
    return false;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    return false;
  }

  /** Trouve les données à l'index donné */
  find(idx: number): T | null {
    return null;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(): T[] {
    return [];
  }
}
```

Vous allez compléter chaque méthode d'ici la fin de cette section.

Comme dans les implémentations précédentes, `head` pointera vers le premier élément de la liste. S'il est `null`, la liste est vide.

Maintenant, passons à la première méthode et apprenons comment ajouter un nœud au début d'une liste chaînée circulaire.

### Comment ajouter un nœud au début d'une liste simplement chaînée circulaire

L'objectif est d'ajouter un nouveau nœud au début de votre liste simplement chaînée circulaire et de mettre à jour le pointeur de tête vers ce nouveau nœud.

Modifiez la méthode prepend dans votre classe `CircularSinglyLinkedList` située dans `src/playground/circular-singly.ts` :

```typescript
// 📁 src/playground/circular-1.ts

prepend(data: T) {
  let newNode = new N(data);

  if (!this.head) {
    this.head = newNode;
    newNode.next = newNode;
  } else {
    let last = this.head;

    while (last.next !== this.head) {
      if (!last.next) throw new Error("invalid list");
      last = last.next;
    }

    last.next = newNode;
    newNode.next = this.head;
    this.head = newNode;
  }
}
```

La propriété `data` contient la valeur pour le nouveau nœud.

Voici comment fonctionne `prepend` :

* Elle crée un nouveau nœud avec la valeur donnée.
    
* Vérifie si la liste est vide. Si le `head` est `null`, elle définit le `head` comme étant le nouveau nœud et pointe son `next` vers lui-même pour former un cercle à un seul nœud.
    
* Si la liste a des nœuds, elle trouve le dernier nœud en se déplaçant dans la liste jusqu'à ce qu'elle atteigne le nœud dont le `next` pointe vers le `head`.
    
* Elle pointe le `next` du dernier nœud vers le nouveau nœud.
    
* Elle pointe le `next` du nouveau nœud vers le `head` actuel.
    
* Elle définit le `head` comme étant le nouveau nœud.
    
* Maintenant, le nouveau nœud est le `head`, et vous avez maintenu la structure circulaire.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le dernier nœud.

### Comment ajouter un nœud à la fin d'une liste simplement chaînée circulaire

L'objectif est d'ajouter un nouveau nœud à la fin de votre liste simplement chaînée circulaire et de maintenir la structure circulaire.

Modifions la méthode append dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

append(data: T): void {
  let newNode = new N(data);

  if (!this.head) {
    this.head = newNode;
    newNode.next = this.head;
  } else {
    let last = this.head;

    while (last.next !== this.head) {
      if (!last.next) throw new Error("invalid list");
      last = last.next;
    }

    last.next = newNode;
    newNode.next = this.head;
  }
}
```

La propriété `data` contient la valeur pour le nouveau nœud.

Voici comment fonctionne `append` :

* Elle crée un nouveau nœud avec la valeur donnée.
    
* Elle vérifie si la liste est vide. Si le `head` est `null`, elle définit le `head` comme étant le nouveau nœud et pointe son `next` vers lui-même pour former un cercle à un seul nœud.
    
* Si la liste a des nœuds, elle trouve le dernier nœud en se déplaçant dans la liste jusqu'à ce qu'elle atteigne le nœud dont le `next` pointe vers le `head`.
    
* Elle pointe le `next` du dernier nœud vers le nouveau nœud.
    
* Elle pointe le `next` du nouveau nœud vers le `head` pour maintenir la liste circulaire.
    
* Maintenant, le nouveau nœud est à la fin, et vous avez maintenu la structure circulaire.
    
* Elle augmente la longueur de la liste de un.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le dernier nœud.

### Comment supprimer le head d'une liste simplement chaînée circulaire

L'objectif est de supprimer le premier nœud de votre liste simplement chaînée circulaire et de mettre à jour le pointeur `head`.

Modifiez la méthode `deleteHead` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

deleteHead(): void {
  if (!this.head) return;

  if (this.head.next === this.head) {
    this.head = null;
    return;
  }

  let last = this.head;

  while (last.next !== this.head) {
    if (!last.next) throw new Error("invalid list");
    last = last.next;
  }

  let newHead = this.head.next;
  last.next = newHead;
  this.head = newHead;
}
```

Voici comment fonctionne `deleteHead` :

* Elle vérifie si la liste est vide et arrête l'opération si le `head` est `null` car il n'y a pas de nœud à supprimer.
    
* Elle vérifie si la liste a un seul nœud : si le `next` du `head` pointe vers lui-même, elle définit le `head` comme étant `null` pour vider la liste.
    
* Si la liste a plusieurs nœuds, elle trouve le dernier nœud en se déplaçant dans la liste jusqu'à ce qu'elle atteigne le nœud dont le `next` pointe vers le `head`.
    
* Elle définit le nœud `next` du `head` actuel comme étant le nouveau `head`.
    
* Elle pointe le `next` du nœud de queue vers le nouveau `head` pour maintenir la liste circulaire.
    
* Elle définit le `head` comme étant le nouveau `head`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le dernier nœud.

### Comment supprimer le dernier nœud d'une liste simplement chaînée circulaire

L'objectif est de supprimer le dernier nœud de votre liste simplement chaînée circulaire et de maintenir la structure circulaire.

Modifiez la méthode `deleteTail` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

deleteTail(): boolean {
  if (!this.head) return false;

  if (this.head.next === this.head) {
    this.head = null;
    return true;
  }

  let current: N<T> = this.head;
  let prev: N<T> | null = null;

  while (current.next !== this.head) {
    prev = current;
    current = current.next!;
  }

  prev!.next = this.head;
  return true;
}
```

Voici comment fonctionne `deleteTail` :

* Elle vérifie si la liste est vide. Si le `head` est `null`, elle retourne `false` car il n'y a pas de nœud à supprimer.
    
* Elle vérifie si la liste a un seul nœud. Si le `next` du `head` pointe vers lui-même, elle définit le `head` comme étant `null` et retourne `true`.
    
* Si la liste a plusieurs nœuds, elle commence un nouveau pointeur appelé `current` au `head` et un pointeur `prev` à `null`.
    
* Elle déplace `current` à travers la liste jusqu'à ce que son `next` pointe vers le `head`, en gardant `prev` un nœud en arrière.
    
* Elle pointe le `next` de `prev` vers le `head` pour sauter le dernier nœud et maintenir la liste circulaire.
    
* Elle retourne `true` pour montrer que la queue a été supprimée.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le dernier nœud.

### Comment supprimer un nœud d'une liste simplement chaînée circulaire

L'objectif est de supprimer la première occurrence d'un nœud avec la valeur donnée de votre liste simplement chaînée circulaire et de retourner `true` si l'opération est réussie.

Modifiez la méthode `delete` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

delete(data: T): boolean {
  if (!this.head) return false;

  if (this.head.data === data) {
    this.deleteHead();
    return true;
  }

  let current: N<T> = this.head;
  let prev: N<T> | null = null;

  do {
    if (current.data === data) {
      prev!.next = current.next;
      return true;
    }

    prev = current;
    current = current.next!;
  } while (current !== this.head);

  return false;
}
```

La propriété `data` est la valeur à trouver et à supprimer.

Vous devez utiliser une boucle do-while au lieu d'une simple boucle while dans la méthode car elle garantit que vous traitez toujours les données du nœud `head` au moins une fois avant de vérifier si vous êtes revenu au `head`.

Dans une liste simplement chaînée circulaire, vous commencez au `head` et continuez à vous déplacer vers le nœud suivant jusqu'à ce que vous reveniez au `head`.

Une simple boucle while pourrait sauter le `head` si elle est vérifiée en premier, mais une boucle do-while s'assure que les données du `head` sont incluses.

Voici comment fonctionne `delete` :

* Elle vérifie si la liste est vide. Si le `head` est `null`, elle retourne `false` car il n'y a rien à supprimer.
    
* Elle vérifie si la valeur du nœud `head` correspond à `data`. Si c'est le cas, elle appelle `deleteHead` pour supprimer le `head` et retourne `true`.
    
* Si le `head` ne correspond pas, elle commence un nouveau pointeur appelé `current` au `head` et un pointeur `prev` à `null`.
    
* Elle déplace `current` à travers la liste, en gardant `prev` un nœud en arrière, jusqu'à ce qu'elle revienne au `head`.
    
* Si la valeur de `current` correspond à `data`, elle lie le `next` de `prev` au `next` de `current` pour sauter le nœud correspondant.
    
* Elle retourne `true` si un nœud correspondant est supprimé, ou `false` si elle ne trouve aucune correspondance après une boucle complète.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud.

### Comment trouver un nœud dans une liste simplement chaînée circulaire

L'objectif est de trouver les données à un index spécifique dans votre liste simplement chaînée circulaire.

Modifiez la méthode `find` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

find(idx: number): T | null {
  if (!this.head || idx < 0) return null;

  let current = this.head;
  let count = 0;

  do {
    if (!current.next) throw new Error("invalid list");

    if (count === idx) {
      return current.data;
    }

    count++;
    current = current.next;
  } while (current !== this.head);

  return null;
}
```

La propriété `idx` est la position dans la liste.

Voici comment fonctionne `find` :

* Elle vérifie si la liste est vide ou si l'index est négatif. Si c'est le cas, elle retourne `null` car aucune donnée n'existe.
    
* Elle crée un nouveau pointeur appelé `current` au `head` et définit un `compteur` à 0.
    
* Elle déplace `current` à travers la liste, vérifiant chaque nœud jusqu'à ce qu'elle revienne au `head`.
    
* Si le `compteur` est égal à `idx`, elle retourne les données du nœud `current`.
    
* Si ce n'est pas le cas, elle augmente le `compteur` et déplace `current` vers le nœud suivant.
    
* Si vous revenez au `head` sans trouver l'index, elle retourne `null`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver l'index.

### Comment parcourir une liste simplement chaînée circulaire

L'objectif est de retourner un tableau de toutes les données des nœuds dans votre liste simplement chaînée circulaire.

Modifiez la méthode `traverse` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

traverse(): T[] {
  if (!this.head) return [];
  const result: T[] = [];

  let current = this.head;

  do {
    result.push(current.data);
    current = current.next!;
  } while (current !== this.head);

  return result;
}
```

Voici comment fonctionne `traverse` :

* Elle vérifie si la liste est vide. Si le `head` est `null`, elle retourne un tableau vide.
    
* Elle crée un tableau vide pour stocker les données des nœuds.
    
* Elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle déplace `current` à travers la liste, ajoutant les données de chaque nœud au tableau.
    
* Elle continue à déplacer `current` vers le nœud suivant jusqu'à ce que vous reveniez au `head`.
    
* Elle retourne le tableau avec toutes les données des nœuds.
    

Cela s'exécute en temps O(n) car vous devez visiter chaque nœud de la liste.

### **Comment insérer un nœud à une position spécifique dans une liste simplement chaînée circulaire**

L'objectif est d'ajouter un nouveau nœud à un index spécifique dans votre liste simplement chaînée circulaire.

Modifiez la méthode `insertAt` dans votre classe `CircularSinglyLinkedList` :

```typescript
// 📁 src/playground/circular-1.ts

insertAt(data: T, idx: number): boolean {
  if (idx < 0) return false;

  if (idx === 0) {
    this.prepend(data);
    return true;
  }

  if (!this.head) {
    if (idx === 0) {
      this.prepend(data);
      return true;
    }
    return false;
  }

  let current: N<T> | null = this.head;
  let prev: N<T> | null = null;
  let count = 0;

  do {
    if (count === idx) {
      const newN = new N(data);
      newN.next = current;
      prev!.next = newN;
      return true;
    }
    prev = current;
    current = current!.next;
    count++;
  } while (current !== this.head);

  if (count === idx) {
    this.append(data);
    return true;
  }

  return false;
}
```

La propriété `data` est la valeur, et `idx` est la position dans la liste.

Voici comment fonctionne `insertAt` :

* Si l'index est négatif, elle retourne `false` car il est invalide.
    
* Si l'index est 0, elle appelle `prepend` pour ajouter le nœud au début et retourne `true`.
    
* Elle crée un nouveau pointeur appelé `current` au `head`, un pointeur `prev` à `null`, et un compteur à `0`.
    
* Elle déplace `current` à travers la liste, en gardant `prev` un nœud en arrière, jusqu'à ce que vous reveniez au `head`.
    
* Si le compteur est égal à `idx`, elle crée un nouveau nœud, pointe son `next` vers `current`, pointe le `next` de `prev` vers le nouveau nœud, et retourne `true`.
    
* Si vous revenez au `head` et que le compteur est égal à `idx`, elle appelle `append` pour ajouter le nœud à la fin et retourne `true`.
    
* Enfin, si l'index n'est pas trouvé, elle retourne `false`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver l'index.

### Comment tester votre liste simplement chaînée circulaire

Parfait ! Vous avez terminé la liste simplement chaînée circulaire et vous êtes maintenant prêt à tester votre implémentation.

Votre implémentation finale devrait ressembler à ceci :

```typescript
/** Nœud pour liste simplement chaînée circulaire */
export class N<T> {
  /** Données du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null;

  /** Crée un nœud avec les données données */
  constructor(data: T) {
    this.data = data;
    this.next = null;
  }
}

/** Implémentation de liste simplement chaînée circulaire */
export class CircularSinglyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null = null;

  /** Ajoute un nœud au début de la liste */
  prepend(data: T) {
    let newNode = new N(data);

    if (!this.head) {
      this.head = newNode;
      newNode.next = newNode;
    } else {
      let last = this.head;

      while (last.next !== this.head) {
        if (!last.next) throw new Error("invalid list");
        last = last.next;
      }

      last.next = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
  }

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {
    let newNode = new N(data);

    if (!this.head) {
      this.head = newNode;
      newNode.next = this.head;
    } else {
      let last = this.head;

      while (last.next !== this.head) {
        if (!last.next) throw new Error("invalid list");
        last = last.next;
      }

      last.next = newNode;
      newNode.next = this.head;
    }
  }

  /** Supprime le nœud de tête */
  deleteHead(): void {
    if (!this.head) return;

    if (this.head.next === this.head) {
      this.head = null;
      return;
    }

    let last = this.head;

    while (last.next !== this.head) {
      if (!last.next) throw new Error("invalid list");
      last = last.next;
    }

    let newHead = this.head.next;
    last.next = newHead;
    this.head = newHead;
  }

  /** Supprime le nœud de queue */
  deleteTail(): boolean {
    if (!this.head) return false;

    if (this.head.next === this.head) {
      this.head = null;
      return true;
    }

    let current: N<T> = this.head;
    let prev: N<T> | null = null;

    while (current.next !== this.head) {
      prev = current;
      current = current.next!;
    }

    prev!.next = this.head;
    return true;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    if (!this.head) return false;

    if (this.head.data === data) {
      this.deleteHead();
      return true;
    }

    let current: N<T> = this.head;
    let prev: N<T> | null = null;

    do {
      if (current.data === data) {
        prev!.next = current.next;
        return true;
      }

      prev = current;
      current = current.next!;
    } while (current !== this.head);

    return false;
  }

  /** Trouve les données à l'index donné */
  find(idx: number): T | null {
    if (!this.head || idx < 0) return null;

    let current = this.head;
    let count = 0;

    do {
      if (!current.next) throw new Error("invalid list");

      if (count === idx) {
        return current.data;
      }

      count++;
      current = current.next;
    } while (current !== this.head);

    return null;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(): T[] {
    if (!this.head) return [];
    const result: T[] = [];

    let current = this.head;

    do {
      result.push(current.data);
      current = current.next!;
    } while (current !== this.head);

    return result;
  }

  /** Insère un nœud à l'index donné */
  insertAt(data: T, idx: number): boolean {
    if (idx < 0) return false;

    if (idx === 0) {
      this.prepend(data);
      return true;
    }

    if (!this.head) {
      if (idx === 0) {
        this.prepend(data);
        return true;
      }
      return false;
    }

    let current: N<T> | null = this.head;
    let prev: N<T> | null = null;
    let count = 0;

    do {
      if (count === idx) {
        const newN = new N(data);
        newN.next = current;
        prev!.next = newN;
        return true;
      }
      prev = current;
      current = current!.next;
      count++;
    } while (current !== this.head);

    if (count === idx) {
      this.append(data);
      return true;
    }

    return false;
  }
}
```

Maintenant, exécutons la commande suivante pour tester la liste chaînée :

```bash
npm run test:file circular-1
```

Si les tests s'exécutent avec succès, vous êtes prêt ! Si des tests échouent, vérifiez `src/examples/circular-1.ts`, corrigez le problème et exécutez les tests à nouveau.

C'est tout, vous avez terminé votre première implémentation de liste chaînée circulaire.

Dans la dernière section, vous allez apprendre à créer une liste chaînée circulaire avec deux pointeurs au lieu d'un.

## Qu'est-ce qu'une liste doublement chaînée circulaire ?

Une liste doublement chaînée circulaire forme une boucle où les nœuds se connectent aux nœuds suivant et précédent.

![Diagramme d'une liste doublement chaînée circulaire avec des nœuds étiquetés A, B, C et D, montrant les pointeurs next et prev. Le nœud A est connecté à Head, et le nœud D est connecté à Tail. Les liens forment une structure circulaire.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748531479718/6eeb89a6-ee2a-4e24-a2c5-e4c798e65ce2.png align="center")

Le `head` se connecte au `tail`, et le `tail` au `head`, vous permettant ainsi de naviguer sans fin dans les deux directions.

### Comment créer une structure de nœud générique pour une liste doublement chaînée circulaire

La structure `Node` dans une liste doublement chaînée circulaire se compose de trois parties : les données, un pointeur vers le nœud suivant et un pointeur vers le nœud précédent.

La propriété `data` contient la valeur du nœud, `next` pointe vers le nœud suivant et `prev` pointe vers le nœud précédent dans la liste.

Ouvrez `src/playground/circular-2.ts` et modifiez la classe `N` :

```typescript
// 📁 src/playground/circular-2.ts

/** Nœud pour liste doublement chaînée circulaire */
export class N<T> {
  /** Données du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null;
  /** Référence au nœud précédent */
  public prev: N<T> | null;

  /** Crée un nœud avec les données données */
  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}
```

Voici comment fonctionne la structure du nœud :

* Elle construit un [générique](https://www.typescriptlang.org/fr/docs/handbook/2/generics.html) `Node` : Utilise `<T>` pour gérer n'importe quel type de données.
    
* Elle stocke la valeur du nœud : Assigne la valeur à la propriété `data`.
    
* Elle lie le nœud suivant : Définit le pointeur `next` vers le nœud suivant, `null` uniquement pendant l'initialisation. Dans une liste circulaire valide, `next` est toujours connecté à un nœud.
    
* Elle lie le nœud précédent : Définit le pointeur `prev` vers le nœud précédent, `null` uniquement pendant l'initialisation. Dans une liste circulaire valide, `prev` est toujours connecté à un nœud.
    
* Elle initialise le nœud : Prend une valeur dans le constructeur et l'assigne à `data`.
    

Dans une liste doublement chaînée circulaire valide, `next` et `prev` ne restent jamais `null`.

### Comment implémenter une liste doublement chaînée circulaire

Vous avez créé la structure `Node` pour votre liste doublement chaînée circulaire. Maintenant, vous pouvez commencer à construire la liste chaînée elle-même. Pour commencer, ouvrez `src/playground/circular-2.ts`, où vous trouverez la classe `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

export class N<T> {
  /** Données du nœud */
  public data: T;
  /** Référence au nœud suivant */
  public next: N<T> | null;
  /** Référence au nœud précédent */
  public prev: N<T> | null;

  /** Crée un nœud avec les données données */
  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

export class CircularDoublyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null;
  /** Nœud de queue */
  public tail: N<T> | null;
  /** Longueur de la liste */
  public len: number;

  /** Crée une liste vide */
  constructor() {
    this.head = null;
    this.tail = null;
    this.len = 0;
  }

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {}

  /** Supprime et retourne les données du nœud de queue */
  deleteTail(): T | null {
    return null;
  }

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {}

  /** Supprime et retourne les données du nœud de tête */
  deleteHead(): T | null {
    return null;
  }

  /** Trouve le nœud à l'index donné */
  find(idx: number): N<T> | null {
    return null;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    return false;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(): T[] {
    return [];
  }

  /** Insère un nœud à l'index donné */
  insertAt(idx: number, data: T): boolean {
    return false;
  }
}
```

Le `head` pointe vers le premier nœud et se connecte en arrière à la queue pour former une boucle circulaire. Il est `null` lorsque la liste est vide.

Le `tail` pointe vers le dernier nœud et se connecte en avant au `head` pour compléter le cercle. Il est également `null` lorsqu'il est vide.

La longueur, `len`, suit le nombre de nœuds. Elle commence à 0 et change lorsque vous ajoutez ou supprimez des nœuds.

Maintenant, passons à la première méthode et apprenons comment ajouter un nœud au début d'une liste doublement chaînée circulaire.

### Comment ajouter un nœud au début d'une liste doublement chaînée circulaire

L'objectif est d'ajouter un nouveau nœud au début de votre liste doublement chaînée circulaire et de mettre à jour le pointeur de tête vers ce nouveau nœud.

Modifiez la méthode prepend dans votre classe `CircularDoublyLinkedList` située dans `src/playground/circular-2.ts` :

```typescript
// 📁 src/playground/circular-2.ts

prepend(data: T): void {
  let newNode = new N(data);

  if (!this.head) {
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

  this.len++;
}
```

La propriété `data` contient la valeur pour le nouveau nœud.

Voici comment fonctionne `prepend` :

* Elle crée un nouveau nœud avec les données données.
    
* Elle vérifie si la liste est vide. Si le `head` est `null`, elle définit à la fois le `head` et le `tail` comme étant le nouveau nœud et lie son `next` et son `prev` à lui-même pour former un cercle à un seul nœud.
    
* Si la liste a des nœuds, elle pointe le `next` du nouveau nœud vers le `head` actuel et son `prev` vers le `tail` actuel.
    
* Elle pointe le `prev` du `head` actuel vers le nouveau nœud.
    
* Elle pointe le `next` du `tail` actuel vers le nouveau nœud pour maintenir la liste circulaire.
    
* Elle définit le `head` comme étant le nouveau nœud.
    
* Elle augmente la longueur de la liste de un.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment ajouter un nœud à la fin d'une liste doublement chaînée circulaire

L'objectif est d'ajouter un nouveau nœud à la fin de votre liste doublement chaînée circulaire et de mettre à jour le pointeur `tail` vers ce nouveau nœud.

Modifiez la méthode append dans votre classe `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

append(data: T): void {
  let newNode = new N(data);

  if (!this.head) {
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

  this.len++;
}
```

La propriété `data` contient la valeur pour le nouveau nœud, comme un nombre ou une chaîne.

Voici comment fonctionne `append` :

* Elle crée un nouveau nœud avec la valeur donnée.
    
* Si la liste est vide, elle définit à la fois le `head` et le `tail` comme étant le nouveau nœud, et lie son `next` et son `prev` à lui-même pour former un cercle à un seul nœud.
    
* Si la liste a des nœuds, elle pointe le `next` du nouveau nœud vers le `head` pour maintenir la boucle circulaire.
    
* Elle pointe le `prev` du nouveau nœud vers le `tail` actuel.
    
* Elle pointe le `next` du `tail` actuel vers le nouveau nœud.
    
* Elle pointe le `prev` du `head` vers le nouveau nœud pour compléter le cercle.
    
* Elle définit le `tail` comme étant le nouveau nœud.
    
* Elle augmente la longueur de la liste de un.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment supprimer le dernier nœud d'une liste doublement chaînée circulaire

L'objectif est de supprimer le dernier nœud de votre liste doublement chaînée circulaire et de retourner ses données.

Modifiez la méthode `deleteTail` dans votre classe `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

deleteTail(): T | null {
  if (!this.tail) return null;

  let removedItem = this.tail;

  if (this.len === 1) {
    this.head = null;
    this.tail = null;
  } else {
    this.tail = this.tail.prev;
    this.tail!.next = this.head;
    this.head!.prev = this.tail;
  }

  removedItem.next = null;
  removedItem.prev = null;
  this.len--;

  return removedItem.data;
}
```

Voici comment fonctionne `deleteTail` :

* Si la liste est vide, elle retourne `null` car il n'y a pas de nœud à supprimer.
    
* Elle déclare une variable appelée `removedItem` et stocke le nœud `tail` dedans pour garder une trace du nœud que vous souhaitez supprimer.
    
* Elle vérifie si la liste a un seul nœud. Si la longueur est 1, elle définit à la fois le `head` et le `tail` comme étant `null`.
    
* Si la liste a plusieurs nœuds, elle déplace le `tail` vers le nœud précédent.
    
* Elle pointe le `next` du nouveau `tail` vers le `head` pour maintenir la boucle circulaire.
    
* Elle pointe le `prev` du `head` vers le nouveau `tail` pour maintenir le cercle.
    
* Elle efface les pointeurs `next` et `prev` du nœud supprimé.
    
* Elle diminue la longueur de la liste de un.
    
* Elle retourne les données du nœud supprimé.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment supprimer le head d'une liste doublement chaînée circulaire

L'objectif est de supprimer le premier nœud de votre liste doublement chaînée circulaire et de retourner ses données.

Modifiez la méthode deleteHead dans votre classe `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

deleteHead(): T | null {
  if (!this.head) return null;

  let removedItem = this.head;

  if (this.len === 1) {
    this.head = null;
    this.tail = null;
  } else {
    this.head = removedItem.next;
    this.head!.prev = this.tail;
    this.tail!.next = this.head;
  }

  this.len--;
  removedItem.next = null;
  removedItem.prev = null;
  return removedItem.data;
}
```

Voici comment fonctionne `deleteHead` :

* Si la liste est vide, elle retourne `null` car il n'y a pas de nœud à supprimer.
    
* Elle déclare une variable appelée `removedItem` et stocke le nœud `head` dedans pour garder une trace du nœud que vous souhaitez supprimer.
    
* Elle vérifie si la liste a un seul nœud. Si la longueur est 1, elle définit à la fois le `head` et le `tail` comme étant `null`.
    
* Si la liste a plusieurs nœuds, elle déplace le `head` vers le nœud `next` pour en faire le nouveau premier nœud.
    
* Elle pointe le `prev` du nouveau `head` vers le `tail` pour maintenir la boucle arrière dans la structure circulaire.
    
* Elle pointe le `next` du `tail` vers le nouveau `head` pour maintenir la boucle avant dans la structure circulaire.
    
* Elle efface les pointeurs `next` et `prev` du nœud supprimé pour le déconnecter de la liste.
    
* Elle diminue la longueur de la liste de un.
    
* Elle retourne les données du nœud supprimé.
    

Cela s'exécute en temps O(1) car vous ne changez que quelques pointeurs sans boucle.

### Comment trouver un nœud dans une liste doublement chaînée circulaire

L'objectif est de trouver le nœud à un index spécifique dans votre liste doublement chaînée circulaire.

Modifiez la méthode `find` dans votre classe `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

find(idx: number): N<T> | null {
  if (!this.head || idx < 0 || idx >= this.len) {
    return null;
  }

  let current = this.head;
  for (let i = 0; i < idx; i++) {
    current = current!.next!;
  }

  return current;
}
```

La propriété `idx` est la position dans la liste. Voici comment fonctionne `find` :

* Elle vérifie si la liste est vide ou si l'index est invalide. Si le `head` est `null`, `idx` est négatif, ou `idx` est trop grand, elle retourne `null` car aucun nœud n'existe.
    
* Elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle déplace `current` vers l'avant à travers les pointeurs `next` autant de fois que la valeur de l'index.
    
* Une fois que vous sortez de la boucle, elle retourne le nœud `current`, qui est à l'index spécifié.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir jusqu'à `n` nœuds pour atteindre l'index.

### Comment parcourir une liste doublement chaînée circulaire

L'objectif est de retourner un tableau de toutes les données des nœuds dans votre liste doublement chaînée circulaire.

Modifiez la méthode `traverse` dans votre `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

traverse(): T[] {
  if (!this.head) return [];

  let current = this.head;
  const result: T[] = [];

  do {
    if (!current.next) throw new Error("invalid list");

    result.push(current.data);

    current = current.next;
  } while (current !== this.head);

  return result;
}
```

Voici comment fonctionne `traverse` :

* Si la liste est vide, elle retourne un tableau vide.
    
* Elle crée un tableau vide pour stocker les données des nœuds.
    
* Elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle ajoute les données du nœud `current` au tableau.
    
* Elle déplace `current` vers le nœud suivant en utilisant le pointeur `next`.
    
* Elle répète l'ajout des données et le déplacement de `current` jusqu'à ce que vous reveniez au `head`.
    
* Elle retourne le tableau avec toutes les données des nœuds.
    

Cela s'exécute en temps O(n) car vous devez visiter chaque nœud de la liste.

### Comment supprimer un nœud d'une liste doublement chaînée circulaire

L'objectif est de supprimer le premier nœud avec la valeur donnée de votre liste doublement chaînée circulaire et de retourner `true` si l'opération est réussie.

Modifiez la méthode delete dans votre classe `CircularDoublyLinkedList` située dans :

```typescript
// 📁 src/playground/circular-2.ts

delete(data: T): boolean {
  if (!this.head) return false;

  let current = this.head;

  do {
    if (current.data === data) {
      if (this.len === 1) {
        this.head = null;
        this.tail = null;
      } else {
        current.prev!.next = current.next;
        current.next!.prev = current.prev;
        if (current === this.head) {
          this.head = current.next;
        }
        if (current === this.tail) {
          this.tail = current.prev;
        }
      }
      this.len--;
      return true;
    }
    current = current.next!;
  } while (current !== this.head);

  return false;
}
```

La propriété `data` est la valeur à trouver et à supprimer. Voici comment fonctionne `delete` :

* Si la liste est vide, elle retourne `false` car il n'y a rien à supprimer.
    
* Elle crée un nouveau pointeur appelé `current` au `head`.
    
* Elle déplace `current` à travers la liste et vérifie la valeur de chaque nœud jusqu'à ce que vous reveniez au `head`.
    
* Si la valeur de `current` correspond à `data`, elle vérifie si la liste a un seul nœud, si c'est le cas, elle définit à la fois le `head` et le `tail` comme étant `null` puisque le seul nœud dans la liste est à la fois le `head` et le `tail`.
    
* Si la liste a plusieurs nœuds, elle lie le `next` du nœud précédent au nœud suivant et le `prev` du nœud suivant au nœud précédent pour sauter `current`.
    
* Si `current` est le `head`, elle met à jour le `head` vers le nœud suivant. Si `current` est le `tail`, elle met à jour le `tail` vers le nœud précédent.
    
* Elle diminue la longueur de la liste de un et retourne `true`.
    
* Si aucune correspondance n'est trouvée, elle déplace `current` vers le nœud suivant et continue à vérifier.
    
* Si vous revenez au `head` sans correspondance, elle retourne `false`.
    

Cela s'exécute en temps O(n) car vous devrez peut-être parcourir toute la liste pour trouver le nœud.

### **Comment insérer un nœud à une position spécifique dans une liste doublement chaînée circulaire**

L'objectif est d'ajouter un nouveau nœud à un index spécifique dans votre liste doublement chaînée circulaire.

Modifiez la méthode `insertAt` dans votre `CircularDoublyLinkedList` :

```typescript
// 📁 src/playground/circular-2.ts

insertAt(idx: number, data: T): boolean {
  if (idx < 0 || idx > this.len) return false;

  if (idx === 0) {
    this.prepend(data);
    return true;
  }

  if (idx === this.len) {
    this.append(data);
    return true;
  }

  let newNode = new N(data);
  let current = this.find(idx);

  if (!current) return false;

  newNode.next = current;
  newNode.prev = current!.prev;
  current.prev!.next = newNode;
  current.prev = newNode;

  this.len++;
  return true;
}
```

La propriété `idx` est la position dans la liste, et `data` est la valeur.

Voici comment fonctionne `insertAt` :

* Si `idx` est négatif ou supérieur à la longueur de la liste, alors la propriété `idx` est un index invalide, et vous devez retourner `false` pour arrêter l'opération.
    
* Si l'index est 0, elle appelle `prepend` pour ajouter le nœud au début et retourne `true`.
    
* Si `idx` est égal à la longueur de la liste, vous ajoutez un nouveau `tail`. Dans ce cas, elle appelle `append` pour ajouter le nœud à la fin et retourne `true`.
    
* Si les conditions précédentes ne sont pas remplies, elle crée un nouveau nœud avec les données données.
    
* Elle trouve le nœud à l'index donné en utilisant la méthode `find` et le stocke comme `current`.
    
* Si aucun nœud n'est trouvé à l'`idx`, elle retourne `false`.
    
* Elle pointe le `next` du nouveau nœud vers `current`. Cela définit le nouveau nœud pour précéder `current` dans la direction avant de la liste circulaire.
    
* Cela définit le `prev` du nouveau nœud vers le nœud `prev` de `current`. Cela lie le nouveau nœud au nœud avant `current` et maintient le lien arrière dans la liste circulaire intact.
    
* Elle définit le `next` du nœud précédent vers le nouveau nœud, donc le nœud avant `current` lie maintenant au nouveau nœud. Cela maintient la boucle circulaire intacte en s'assurant que la chaîne avant saute le prédécesseur original de `current` et inclut le nouveau nœud.
    
* Elle définit le `prev` de `current` vers le nouveau nœud. Cela complète l'insertion en faisant en sorte que `current` lie en arrière au nouveau nœud et maintient la structure circulaire avec des liens bidirectionnels corrects.
    
* Elle augmente la longueur de la liste de un.
    
* Elle retourne `true` pour montrer que le nœud a été inséré.
    

Cela s'exécute en temps O(n) car la recherche de l'index peut nécessiter de parcourir la liste.

### Comment tester votre liste doublement chaînée circulaire

Excellent travail ! Vous avez terminé la liste doublement chaînée circulaire, et vous êtes maintenant prêt à tester votre implémentation.

Votre implémentation finale devrait ressembler à ceci :

```typescript
// 📁 src/playground/circular-2.ts

/** Nœud pour liste doublement chaînée circulaire */
export class N<T> {
  /** Données du nœud */
  public data;
  /** Référence au nœud suivant */
  public next: N<T> | null;
  /** Référence au nœud précédent */
  public prev: N<T> | null;

  /** Crée un nœud avec les données données */
  constructor(data: T) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

/** Implémentation de liste doublement chaînée circulaire */
export class CircularDoublyLinkedList<T> {
  /** Nœud de tête */
  public head: N<T> | null;
  /** Nœud de queue */
  public tail: N<T> | null;
  /** Longueur de la liste */
  public len: number;

  /** Crée une liste vide */
  constructor() {
    this.head = null;
    this.tail = null;
    this.len = 0;
  }

  /** Ajoute un nœud à la fin de la liste */
  append(data: T): void {
    let newNode = new N(data);

    if (!this.head) {
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

    this.len++;
  }

  /** Supprime et retourne les données du nœud de queue */
  deleteTail(): T | null {
    if (!this.tail) return null;

    let removedItem = this.tail;

    if (this.len === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail!.next = this.head;
      this.head!.prev = this.tail;
    }

    removedItem.next = null;
    removedItem.prev = null;
    this.len--;

    return removedItem.data;
  }

  /** Ajoute un nœud au début de la liste */
  prepend(data: T): void {
    let newNode = new N(data);

    if (!this.head) {
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

    this.len++;
  }

  /** Supprime et retourne les données du nœud de tête */
  deleteHead(): T | null {
    if (!this.head) return null;

    let removedItem = this.head;

    if (this.len === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = removedItem.next;
      this.head!.prev = this.tail;
      this.tail!.next = this.head;
    }

    this.len--;
    removedItem.next = null;
    removedItem.prev = null;
    return removedItem.data;
  }

  /** Trouve le nœud à l'index donné */
  find(idx: number): N<T> | null {
    if (!this.head || idx < 0 || idx >= this.len) {
      return null;
    }

    let current = this.head;
    for (let i = 0; i < idx; i++) {
      current = current!.next!;
    }

    return current;
  }

  /** Supprime le premier nœud avec les données données */
  delete(data: T): boolean {
    if (!this.head) return false;

    let current = this.head;

    do {
      if (current.data === data) {
        if (this.len === 1) {
          this.head = null;
          this.tail = null;
        } else {
          current.prev!.next = current.next;
          current.next!.prev = current.prev;
          if (current === this.head) {
            this.head = current.next;
          }
          if (current === this.tail) {
            this.tail = current.prev;
          }
        }
        this.len--;
        return true;
      }
      current = current.next!;
    } while (current !== this.head);

    return false;
  }

  /** Retourne un tableau des données des nœuds */
  traverse(): T[] {
    if (!this.head) return [];

    let current = this.head;
    const result: T[] = [];

    do {
      if (!current.next) throw new Error("invalid list");

      result.push(current.data);

      current = current.next;
    } while (current !== this.head);

    return result;
  }

  /** Insère un nœud à l'index donné */
  insertAt(idx: number, data: T): boolean {
    if (idx < 0 || idx > this.len) return false;

    if (idx === 0) {
      this.prepend(data);
      return true;
    }

    if (idx === this.len) {
      this.append(data);
      return true;
    }

    let newNode = new N(data);
    let current = this.find(idx);

    if (!current) return false;

    newNode.next = current;
    newNode.prev = current!.prev;
    current.prev!.next = newNode;
    current.prev = newNode;

    this.len++;
    return true;
  }
}
```

Exécutez la commande suivante pour tester la liste chaînée :

```bash
npm run test:file circular-2
```

Si les tests passent avec succès, vous êtes prêt ! Si des tests échouent, passez en revue `src/examples/circular-2.ts`, corrigez les problèmes et exécutez les tests à nouveau.

## Quand utiliser les listes chaînées (et quand les éviter)

Les listes chaînées sont des structures de données puissantes, mais elles ne sont pas toujours le meilleur choix. Il est donc important de savoir quand les utiliser et quand choisir une alternative.

### Pourquoi utiliser les listes chaînées ?

Les listes chaînées sont idéales pour les situations nécessitant des données dynamiques ou une navigation flexible.

Leurs principaux avantages incluent :

* **Taille dynamique** : Ajoutez ou supprimez des nœuds sans redimensionnement, contrairement aux tableaux qui nécessitent une réallocation.
    
* **Insertions/suppressions efficaces** : Les opérations comme `prepend` ou `delete` sont rapides (`O(1)` à des positions connues), ce qui est idéal pour les mises à jour fréquentes.
    
* **Parcours flexible** : Les listes doublement et circulaires permettent de se déplacer vers l'avant ou l'arrière, ce qui les rend utiles pour des schémas de navigation complexes.
    

### Cas d'utilisation réels

Vous devriez envisager d'utiliser des listes chaînées dans des scénarios où les données sont fréquemment mises à jour ou nécessitent un accès cyclique ou bidirectionnel :

* **Historique du navigateur** : Une liste doublement chaînée garde une trace des pages visitées et permet aux utilisateurs de se déplacer facilement en avant et en arrière. L'ajout d'une nouvelle page (`prepend`) ou la suppression d'une page (`delete`) est rapide, et la liste s'agrandit dynamiquement à mesure que les utilisateurs naviguent.
    
* **Playlist musicale** : Les listes doublement chaînées circulaires sont utilisées pour les playlists en boucle dans des applications comme Spotify. Les utilisateurs peuvent facilement sauter en avant (`next`) ou en arrière (`prev`), et les nouvelles chansons (`append`) s'intègrent en douceur dans la boucle.
    
* **Fonctionnalité Annuler/Rétablir** : Les éditeurs de texte utilisent des listes doublement chaînées pour stocker les actions. Chaque modification est un nœud, et le déplacement en arrière (`undo`) ou en avant (`redo`) navigue à travers la liste.
    
* **Planification des tâches** : Les listes simplement chaînées circulaires sont utilisées pour la planification round-robin dans les systèmes d'exploitation. Chaque processus est un nœud, et la liste parcourt chacun d'eux pour allouer du temps CPU. Les nouvelles tâches sont ajoutées en utilisant `append`.
    

### Quand ne pas utiliser les listes chaînées

Malgré leurs forces, les listes chaînées ont des faiblesses dans certaines situations en raison de leur structure :

* **Accès aléatoire lent** : Atteindre un index nécessite de parcourir depuis la tête (`O(n)`), contrairement aux tableaux, qui ont un accès `O(1)`.
    
* **Surcoût mémoire élevé** : Chaque nœud dans une liste chaînée stocke des pointeurs (`next`, `prev`), ce qui utilise plus de mémoire que les tableaux. Cela peut être un problème pour les grands ensembles de données.
    
* **Performance de recherche médiocre** : Trouver une valeur nécessite de vérifier chaque nœud (`O(n)`), ce qui est plus lent que les tables de hachage (`O(1)`) ou les arbres de recherche binaire (`O(log n)`).
    

### Meilleures alternatives pour des cas spécifiques

Dans certains cas, d'autres structures de données surpassent les listes chaînées :

* **Accès aléatoire** : Utilisez des tableaux ou des tableaux dynamiques (comme `Array` de JavaScript) pour un indexage rapide. Par exemple, si vous devez afficher un tableau dans une application web, l'accès `O(1)` d'un tableau vous permet d'atteindre rapidement n'importe quelle ligne.
    
* **Recherches fréquentes** : Les tables de hachage (comme `Map` de JavaScript) sont meilleures pour des recherches rapides. Par exemple, une application de liste de contacts qui recherche par nom utiliserait une table de hachage pour accélérer le processus.
    
* **Environnements contraints en mémoire** : Les tableaux utilisent moins de mémoire pour les grands ensembles de données de taille fixe, comme les tampons de traitement d'image dans les applications graphiques.
    

Le point clé à retenir est que les listes chaînées sont idéales lorsque vos données nécessitent une croissance dynamique, des insertions ou suppressions fréquentes, ou une navigation cyclique, comme dans les playlists ou les fonctionnalités d'historique.

Évitez d'utiliser les listes chaînées pour l'accès aléatoire, les recherches fréquentes ou les tâches sensibles à la mémoire, où les tableaux, les tables de hachage ou les arbres sont de meilleures options.

Vous pouvez expérimenter avec vos implémentations `src/playground` pour voir comment les listes chaînées s'adaptent aux besoins de votre projet.

## Conclusion

Félicitations pour avoir terminé ce manuel ! 🎉 Vous avez appris à implémenter différents types de listes chaînées en utilisant TypeScript, y compris les listes simplement chaînées, les listes doublement chaînées et les listes chaînées circulaires.

En comprenant ces listes chaînées, vous êtes bien préparé à travailler avec des structures de données plus complexes.

Merci d'avoir suivi ce tutoriel. Vous pouvez me suivre sur [X](https://x.com/Yazdun), où je partage plus de conseils utiles sur les structures de données et le développement web.

Bonne programmation !