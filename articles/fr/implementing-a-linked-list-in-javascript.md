---
title: Comment implémenter une liste chaînée en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T21:29:00.000Z'
originalURL: https://freecodecamp.org/news/implementing-a-linked-list-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a86740569d1a4ca2622.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
seo_title: Comment implémenter une liste chaînée en JavaScript
seo_desc: "By Sarah Chima Atuonwu\nIf you are learning data structures, a linked list\
  \ is one data structure you should know. If you do not really understand it or how\
  \ it is implemented in JavaScript, this article is here to help you. \nIn this article,\
  \ we will di..."
---

Par Sarah Chima Atuonwu

Si vous apprenez les structures de données, une liste chaînée est une structure de données que vous devriez connaître. Si vous ne la comprenez pas vraiment ou ne savez pas comment elle est implémentée en JavaScript, cet article est là pour vous aider.

Dans cet article, nous discuterons de ce qu'est une liste chaînée, en quoi elle diffère d'un tableau, et comment l'implémenter en JavaScript. Commençons.

## Qu'est-ce qu'une liste chaînée ?

Une liste chaînée est une structure de données linéaire similaire à un tableau. Cependant, contrairement aux tableaux, les éléments ne sont pas stockés dans un emplacement mémoire ou un index particulier. Chaque élément est un objet séparé qui contient un pointeur ou un lien vers l'objet suivant dans cette liste.

Chaque élément (communément appelé nœud) contient deux éléments : les données stockées et un lien vers le nœud suivant. Les données peuvent être de n'importe quel type de données valide. Vous pouvez voir cela illustré dans le diagramme ci-dessous.

![Image d'une liste chaînée](https://res.cloudinary.com/dvj2hbywq/image/upload/v1590572188/Group_14_5_bvpwu0.png)

Le point d'entrée d'une liste chaînée est appelé la tête (head). La tête est une référence au premier nœud de la liste chaînée. Le dernier nœud de la liste pointe vers null. Si une liste est vide, la tête est une référence nulle.

En JavaScript, une liste chaînée ressemble à ceci :

```js
const list = {
    head: {
        value: 6
        next: {
            value: 10                                             
            next: {
                value: 12
                next: {
                    value: 3
                    next: null	
                    }
                }
            }
        }
    }
};
```

## Un avantage des listes chaînées

* Les nœuds peuvent être facilement supprimés ou ajoutés à une liste chaînée sans réorganiser toute la structure de données. C'est un avantage qu'elle a sur les tableaux.

## Inconvénients des listes chaînées

* Les opérations de recherche sont lentes dans les listes chaînées. Contrairement aux tableaux, l'accès aléatoire aux éléments de données n'est pas autorisé. Les nœuds sont accédés séquentiellement en commençant par le premier nœud.
* Elle utilise plus de mémoire que les tableaux en raison du stockage des pointeurs.

## Types de listes chaînées

Il existe trois types de listes chaînées :

* **Listes chaînées simples** : Chaque nœud contient uniquement un pointeur vers le nœud suivant. C'est ce dont nous avons parlé jusqu'à présent.
* **Listes chaînées doubles** : Chaque nœud contient deux pointeurs, un pointeur vers le nœud suivant et un pointeur vers le nœud précédent.
* **Listes chaînées circulaires** : Les listes chaînées circulaires sont une variation d'une liste chaînée dans laquelle le dernier nœud pointe vers le premier nœud ou tout autre nœud avant lui, formant ainsi une boucle.

## Implémentation d'un nœud de liste en JavaScript

Comme indiqué précédemment, un nœud de liste contient deux éléments : les données et le pointeur vers le nœud suivant. Nous pouvons implémenter un nœud de liste en JavaScript comme suit :

```js
class ListNode {
    constructor(data) {
        this.data = data
        this.next = null                
    }
}
```

## Implémentation d'une liste chaînée en JavaScript

Le code ci-dessous montre l'implémentation d'une classe de liste chaînée avec un constructeur. Remarquez que si le nœud de tête n'est pas passé, la tête est initialisée à null.

```js
class LinkedList {
    constructor(head = null) {
        this.head = head
    }
}
```

## Mettre le tout ensemble

Créons une liste chaînée avec la classe que nous venons de créer. Tout d'abord, nous créons deux nœuds de liste, `node1` et `node2`, et un pointeur de node1 vers node2.

```js
let node1 = new ListNode(2)
let node2 = new ListNode(5)
node1.next = node2
```

Ensuite, nous allons créer une liste chaînée avec `node1`.

```js
let list = new LinkedList(node1)
```

Essayons d'accéder aux nœuds de la liste que nous venons de créer.

```js
console.log(list.head.next.data) // retourne 5
```

## Quelques méthodes de LinkedList

Ensuite, nous allons implémenter quatre méthodes auxiliaires pour la liste chaînée. Ce sont :

1. size()
2. clear()
3. getLast()
4. getFirst()

### 1. size()

Cette méthode retourne le nombre de nœuds présents dans la liste chaînée.

```js
size() {
    let count = 0; 
    let node = this.head;
    while (node) {
        count++;
        node = node.next
    }
    return count;
}

```

### 2. clear()

Cette méthode vide la liste.

```js
clear() {
    this.head = null;
}
```

### 3. getLast()

Cette méthode retourne le dernier nœud de la liste chaînée.

```js
getLast() {
    let lastNode = this.head;
    if (lastNode) {
        while (lastNode.next) {
            lastNode = lastNode.next
        }
    }
    return lastNode
}
```

### 4. getFirst()

Cette méthode retourne le premier nœud de la liste chaînée.

```js
getFirst() {
    return this.head;
}
```

## Résumé

Dans cet article, nous avons discuté de ce qu'est une liste chaînée et comment elle peut être implémentée en JavaScript. Nous avons également discuté des différents types de listes chaînées ainsi que de leurs avantages et inconvénients globaux.

J'espère que vous avez apprécié sa lecture.

_Voulez-vous être informé lorsque je publie un nouvel article ? [Cliquez ici](https://mailchi.mp/69ea601a3f64/join-sarahs-mailing-list)._