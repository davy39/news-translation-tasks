---
title: Comment fonctionne une liste chaînée ? Un guide pour débutants sur les listes
  chaînées
subtitle: ''
author: Palistha Singh
co_authors: []
series: null
date: '2023-05-12T17:45:27.000Z'
originalURL: https://freecodecamp.org/news/how-linked-lists-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-joey-kyber-119562.jpg
tags:
- name: data structures
  slug: data-structures
- name: Java
  slug: java
seo_title: Comment fonctionne une liste chaînée ? Un guide pour débutants sur les
  listes chaînées
seo_desc: 'A Linked List is a linear data structure used for storing a collection
  of elements. Unlike arrays, linked lists use nodes to store elements which are not
  stored in contiguous memory locations.

  In this article, you will learn what linked lists are, ho...'
---

Une liste chaînée est une structure de données linéaire utilisée pour stocker une collection d'éléments. Contrairement aux tableaux, les listes chaînées utilisent des nœuds pour stocker des éléments qui ne sont pas stockés dans des emplacements mémoire contigus.

Dans cet article, vous apprendrez ce que sont les listes chaînées, comment elles fonctionnent et comment en construire une.

Bien que les concepts discutés ne soient pas spécifiques à un langage de programmation particulier, cet article utilisera Java pour démontrer comment créer une liste chaînée de manière programmatique.

## Qu'est-ce qu'une liste chaînée ?

Une liste chaînée est une collection de nœuds où chaque nœud contient des données ainsi que l'adresse mémoire du nœud suivant dans la liste.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7.png align="left")

*Illustration d'une liste chaînée avec trois nœuds*

Ici, vous pouvez voir que les adresses des nœuds ne sont pas nécessairement immédiatement séquentielles. Le premier nœud a une adresse de **200** et le deuxième nœud a une adresse de **801**, au lieu de **201** comme vous pourriez vous y attendre.

Alors, comment les nœuds sont-ils stockés de manière linéaire ?

Même si les nœuds ne sont pas dans une mémoire contiguë, les nœuds sont stockés de manière linéaire grâce à des liens. Chaque nœud a l'adresse de son nœud suivant. C'est ainsi que chaque nœud peut accéder à son nœud suivant.

## Nœuds dans une liste chaînée

Les nœuds sont les éléments de base de la liste chaînée. Après tout, une liste chaînée est une collection de nœuds.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8.png align="left")

*Exemple de nœud*

Un nœud dans une liste chaînée se compose de deux parties :

* `data` qui désigne la valeur du nœud.

* `next` qui est une référence au nœud suivant.

## Tête et queue dans une liste chaînée

Comme mentionné précédemment, une liste chaînée est une collection de nœuds.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9.png align="left")

*Illustration d'une liste chaînée montrant la tête et la queue*

Le premier nœud de la liste chaînée est appelé le nœud `head`. C'est le point de départ d'une liste chaînée.

Le dernier nœud est appelé le nœud `tail`. Comme il n'y a pas de nœud après le dernier nœud, le dernier nœud pointe toujours vers `null`.

Un pointeur `null` ne pointe vers aucun emplacement mémoire.

## Comment créer une liste chaînée de manière programmatique

À ce stade, vous devriez avoir une connaissance de base du fonctionnement d'une liste chaînée et de sa structure. Créons une liste chaînée avec les étapes suivantes :

* Créer un nœud.

* Connecter les nœuds.

* Ajouter des nœuds.

* Insérer des nœuds.

* Supprimer des nœuds.

## Comment créer un nœud dans une liste chaînée

Comme vous le savez, un nœud se compose de deux parties : les données et l'adresse du nœud suivant.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10.png align="left")

*Illustration d'un seul nœud*

Voici comment vous pouvez créer une classe appelée `Node` :

```java
class Node {
    int data;
    Node next;
 
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

La classe `Node` représente un nœud dans une liste chaînée, avec deux variables d'instance : data (contient les données stockées dans le nœud), et next (contient une référence au nœud suivant dans la liste).

Le constructeur prend un argument `int` data pour initialiser la variable data et définit la variable next à null par défaut.

Maintenant, vous pouvez simplement créer des nœuds et ajouter des données en créant de nouvelles instances de la classe `Node` :

```java
// créer des nœuds
Node node1 = new Node(11);
Node node2 = new Node(18);
Node node3 = new Node(24);
```

Dans le code ci-dessus, nous avons créé trois nœuds :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/11.png align="left")

*Montrant les trois nœuds que nous avons créés avec le code ci-dessus*

## Comment lier les nœuds dans une liste chaînée

Après avoir créé les nœuds, vous devez les connecter pour former une liste chaînée.

Pour cela, vous devez d'abord créer une liste chaînée avec un nœud `head`.

```bash
class LinkedList {

    Node head;

        LinkedList() {
        this.head = null;
    }

}
```

Initialement, le nœud `head` est défini à `null` car il n'y a pas encore de nœuds dans la liste chaînée.

Maintenant, pour connecter les nœuds ensemble dans une liste chaînée, vous pouvez commencer par définir le nœud `head` comme le premier nœud de la liste, dans ce cas `node1`.

```bash
head = node1;
```

Ensuite, faites en sorte que le suivant de `node1` pointe vers `node2`, et le suivant de `node2` pointe vers `node3`. C'est-à-dire :

```java
node1.next = node2;
node2.next = node3;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-1.png align="left")

*Illustration montrant la liaison des nœuds*

Vous avez réussi à créer une liste chaînée et à connecter les nœuds.

## Comment ajouter un nœud à une liste chaînée

Ajouter un nœud signifie ajouter un nœud à la fin d'une liste chaînée. Il y a deux cas à considérer lors de l'ajout d'un nœud :

* Ajouter à une liste chaînée vide.

* Ajouter à une liste chaînée non vide.

### Comment ajouter un nœud à une liste chaînée vide

S'il n'y a pas de nœuds dans une liste chaînée, c'est une liste chaînée vide. Pour ajouter un nœud à une liste chaînée vide, vous devez d'abord vous assurer que la liste chaînée est vide. Vous pouvez le faire en vérifiant si le nœud `head` est `null`.

Si le nœud `head` est `null`, vous pouvez simplement définir `head` comme le nouveau nœud :

```java
if (head == null) {
    head = newNode;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13.png align="left")

*Le nœud head est null*

### Comment ajouter un nœud à une liste chaînée non vide

S'il y a un ou plusieurs nœuds dans une liste chaînée, c'est une liste chaînée non vide.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-2.png align="left")

*Illustration d'une liste chaînée non vide*

Pour ajouter un nœud à une liste chaînée non vide, faites en sorte que le dernier nœud pointe vers le nouveau nœud.

Contrairement aux tableaux, nous ne pouvons pas accéder directement à des éléments dans une liste chaînée. Nous devons parcourir depuis le nœud `head` jusqu'au nœud `last`.

Pour cela, créez un pointeur temporaire (vous pouvez appeler le pointeur `current`) qui pointe vers le nœud head.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/17-2.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers le nœud head*

Ensuite, faites en sorte que `current` pointe vers son nœud `next`, jusqu'à ce que le `next` du nœud courant pointe vers `null`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/18-1.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers son nœud suivant*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/16-2.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers son nœud suivant*

Lorsque le nœud `next` de `current` est `null`, vous pouvez alors faire en sorte que le `next` du nœud `current` pointe vers le nouveau nœud. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/15-1.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers le nouveau nœud*

```java
while (current.next != null) {
    current = current.next;
}
current.next = newNode;
```

## Comment insérer un nœud dans une liste chaînée

Insérer un nœud signifie ajouter un nœud à un index donné. Il y a deux cas à considérer lors de l'insertion d'un nœud :

* Insérer un nœud au premier index.

* Insérer un nœud à un index donné.

### Comment insérer un nœud au premier index

Pour insérer un nœud au premier index :

* faites en sorte que `next` du nouveau nœud pointe vers le nœud `head`

* définissez le `head` comme le nouveau nœud

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13-1.png align="left")

*Illustration montrant le nouveau nœud pointant vers le nœud head*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/14-1.png align="left")

*Illustration montrant le nœud head pointant vers le nouveau nœud*

```java
if (index == 0) {
    newNode.next = head;
    head = newNode;
}
```

### Comment insérer un nœud à n'importe quelle position

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-1.png align="left")

*Liste chaînée avec index*

Supposons que vous souhaitez ajouter un nœud à l'index 2 dans la liste chaînée ci-dessus.

Pour insérer un nœud à l'index 2, vous devez parcourir le nœud qui précède l'index 2.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/5-1.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers le nœud head*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10-1.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers son nœud suivant*

Ensuite, créez un nouveau nœud et faites en sorte que le `next` du nouveau nœud pointe vers le `next` du nœud `current`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9-1.png align="left")

*Illustration montrant le nouveau nœud pointant vers le nœud suivant de current*

Faites en sorte que le `next` de `current` pointe vers le nouveau nœud.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8-2.png align="left")

*Illustration montrant current pointant vers le nouveau nœud*

Voici le code pour faire tout cela :

```java
for (int i = 0; i < index - 1 && current != null; i++) {
    current = current.next;
}
if (current != null) {
    newNode.next = current.next;
    current.next = newNode;
}
```

## Comment supprimer un nœud dans une liste chaînée

Il existe deux façons de supprimer des nœuds dans une liste chaînée :

* Supprimer le nœud head.

* Supprimer un nœud à une position donnée.

### Comment supprimer le nœud head

Supprimer le nœud `head` d'une liste chaînée est simple. Vous pouvez stocker les données du nœud `head` dans une variable temporaire si elles doivent être accessibles plus tard. Ensuite, définissez le pointeur `head` pour qu'il pointe vers le nœud `next` après le nœud `head`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7-1.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers le nœud head*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/6.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers son nœud suivant*

```java
if (index == 0) {
    deletedValue = head.data;
    head = head.next;
}
```

### Comment supprimer un nœud à une position donnée

Supposons que vous souhaitez supprimer le nœud à l'index 2 dans le diagramme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-2.png align="left")

*Liste chaînée avec index*

Vous pouvez supprimer le nœud à l'index 2 en faisant en sorte que le nœud à l'index 1 pointe vers le nœud à l'index 3.

Pour supprimer un nœud, vous devez accéder au nœud que vous souhaitez supprimer et au nœud qui le précède. Prenez deux pointeurs temporaires (vous pouvez appeler les pointeurs `previous` et `current`). Laissez `previous` pointer vers `null` et `current` pointer vers le nœud `head`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/data--3-.png align="left")

*Illustration montrant le pointeur temporaire (current) pointant vers le nœud head*

Maintenant, déplacez `current` d'un pas vers l'avant et déplacez `previous` vers `current` jusqu'à ce que vous atteigniez l'index 2.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/2-2.png align="left")

*Illustration montrant le pointeur temporaire (previous) pointant vers le nœud head*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/3-1.png align="left")

*Illustration montrant le pointeur temporaire pointant vers ses nœuds suivants*

Faites en sorte que le `next` de `previous` pointe vers le `next` du nœud `current`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/1.png align="left")

*Illustration montrant previous pointant vers le nœud suivant current*

Ensuite, stockez les données de `current` dans une variable pour une utilisation future.

Après avoir supprimé le lien vers le nœud à l'index 2, il n'est plus accessible via aucune référence dans la liste chaînée.

Il est important de noter que lors de la suppression d'un nœud d'une liste chaînée, vous n'avez pas besoin de supprimer explicitement le nœud lui-même à l'index donné. Cela est dû au fait que le nœud supprimé sera automatiquement géré par le garbage collector lorsqu'il n'est plus accessible via aucune référence.

Cependant, dans des langages comme C ou C++, qui n'ont pas de garbage collection automatique, vous devez supprimer manuellement le nœud lorsqu'il n'est plus nécessaire pour éviter les fuites de mémoire et le gaspillage des ressources mémoire.

```java
for (int i = 0; i < index && current != null; i++) {
    previous = current;
    current = current.next;
}

if (current != null) {
    deletedValue = current.data;
    previous.next = current.next;
}
```

## Code complet de la liste chaînée

Le code ci-dessous montre une liste chaînée complète. Vous pouvez créer, ajouter, insérer, supprimer et afficher les nœuds dans la liste chaînée :

```java
class Node {

	int data;
	Node next;

	Node(int data) {
		this.data = data;
		this.next = null;
	}
}

class LinkedList {

	Node head;

	LinkedList() {
		this.head = null;
	}

	public void createLinkedList() {

		Node node1 = new Node(11);
		this.head = node1;

		Node node2 = new Node(18);
		node1.next = node2;

		Node node3 = new Node(24);
		node2.next = node3;
	}

	public void append(Node newNode) {

		Node current = this.head;

		if (current == null) {
			this.head = newNode;
		} else {
			while (current.next != null) {
				current = current.next;
			}
			current.next = newNode;
		}

	}

	public void insert(Node newNode, int index) {

		Node current = this.head;
		if (index == 0) {
			newNode.next = current;
			this.head = newNode;
		} else {

			for (int i = 0; i < index - 1 && current != null; i++) {
				current = current.next;
			}
			if (current != null) {
				newNode.next = current.next;
				current.next = newNode;
			}

		}

	}

	public int delete(int index) {

		Node current = this.head;
		Node previous = null;
		int deletedValue = -1;

		if (index == 0) {
			deletedValue = this.head.data;
			this.head = this.head.next;
			return deletedValue;
		}

		else {
			for (int i = 0; i < index && current != null; i++) {
				previous = current;
				current = current.next;

			}
			if (current != null) {

				deletedValue = current.data;
				previous.next = current.next;
			}
			return deletedValue;
		}
	}
	
	public void displayLinkedList() {

		Node current = this.head;
		while (current != null) {
			System.out.println(current.data);
			current = current.next;

		}
	}

}

class Main {
	public static void main(String[] args) {
		LinkedList l1 = new LinkedList();
		Node newNode1 = new Node(22);
		Node newNode2 = new Node(43);
		Node newNode3 = new Node(5);
		l1.createLinkedList();

		l1.append(newNode1);
		l1.insert(newNode2, 0);
		l1.insert(newNode3, 2);
		l1.delete(2);
		l1.displayLinkedList();
	}
}
```

## Conclusion

La structure de données de liste chaînée peut être utilisée dans diverses applications, telles que les navigateurs web et les lecteurs de musique.

Par exemple, dans un navigateur web, l'historique du navigateur peut être stocké sous forme de liste chaînée. Chaque page visitée peut être représentée par un nœud, avec le lien pointant vers la page suivante visitée. Cela permet une navigation facile dans l'historique, en parcourant simplement la liste chaînée.

De même, dans un lecteur de musique, la playlist peut être représentée sous forme de liste chaînée. Chaque chanson peut être représentée par un nœud, avec le lien pointant vers la chanson suivante dans la playlist. Cela permet une navigation facile dans la playlist, en parcourant simplement la liste chaînée.

Il n'est pas très probable que vous créiez une liste chaînée pour vos applications, car presque tous les langages de programmation ont une liste chaînée intégrée.

Cependant, en créer une et comprendre son implémentation peut approfondir vos connaissances de la structure de données. Cette connaissance peut vous aider à déterminer quand utiliser une liste chaînée plutôt que d'autres structures de données dans des applications réelles.