---
title: Structures de données expliquées avec des exemples - Liste chaînée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/data-structures-explained-with-examples-linked-list
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfb740569d1a4ca353d.jpg
tags:
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: Structures de données expliquées avec des exemples - Liste chaînée
seo_desc: 'Just like a garland is made with flowers, a linked list is made up of nodes.
  We call every flower on this particular garland to be a node. And each of the node
  points to the next node in this list as well as it has data (here it is type of
  flower).

  T...'
---

Tout comme une guirlande est faite de fleurs, une liste chaînée est composée de nœuds. Nous appelons chaque fleur de cette guirlande particulière un nœud. Et chaque nœud pointe vers le nœud suivant dans cette liste ainsi qu'il contient des données (ici, il s'agit du type de fleur).

## **Types**

### Liste chaînée simplement

Les listes chaînées simplement contiennent des nœuds qui ont un champ `data` ainsi qu'un champ `next`, qui pointe vers le nœud suivant dans la séquence. Les opérations qui peuvent être effectuées sur les listes chaînées simplement sont l'insertion, la suppression et le parcours.

```text
   head
    |
    |
  +-----+--+      +-----+--+      +-----+------+
  |  1  |o----->  |  2  |o----->  |  3  | NULL |
  +-----+--+      +-----+--+      +-----+------+
```

Implémentation interne de CPython, les cadres et les variables évaluées sont conservés sur une pile.

Pour cela, nous devons itérer uniquement vers l'avant ou obtenir la tête, donc une liste chaînée simplement est utilisée.

### Liste chaînée doublement

Les listes chaînées doublement contiennent des nœuds qui ont un champ `data`, un champ `next` et un autre champ de lien `prev` pointant vers le nœud précédent dans la séquence.

```text
          head
           |
           |
  +------+-----+--+    +--+-----+--+       +-----+------+
  |      |     |o------>  |     |o------>  |     |      |
  | NULL |  1  |          |  2  |          |  3  | NULL |
  |      |     |  <------o|     |  <------o|     |      |
  +------+-----+--+    +--+-----+--+       +-----+------+
```

Le cache du navigateur qui vous permet d'utiliser les boutons PRÉCÉDENT et SUIVANT. Ici, nous devons maintenir une liste doublement chaînée, avec les `URL` comme champ de données, pour permettre l'accès dans les deux directions. Pour aller à l'URL précédente, nous utiliserons le champ `prev` et pour aller à la page suivante, nous utiliserons le champ `next`.

### Liste chaînée circulaire

Une liste chaînée circulaire est une liste chaînée simplement dans laquelle le dernier nœud, le champ `next` pointe vers le premier nœud de la séquence.

```text
     head
      |
      |
    +-----+--+      +-----+--+      +-----+--+
    ---> | 1 |o-----> | 2 |o----->    | 3 |o----| 
    +-----+--+      +-----+--+      +-----+--+
```

Problème de partage de temps résolu par le système d'exploitation.

Dans un environnement de partage de temps, le système d'exploitation doit maintenir une liste des utilisateurs présents et doit alternativement permettre à chaque utilisateur d'utiliser une petite portion de temps CPU, un utilisateur à la fois. Le système d'exploitation choisira un utilisateur, lui permettra d'utiliser une petite quantité de temps CPU, puis passera à l'utilisateur suivant.

Pour cette application, il ne devrait y avoir aucun pointeur NULL sauf s'il n'y a absolument personne qui demande du temps CPU, c'est-à-dire que la liste est vide.

## **Opérations de base**

### Insertion

Pour ajouter un nouvel élément à la liste.

Insertion au début :

* Créer un nouveau nœud avec les données données.
* Pointer le `next` du nouveau nœud vers l'ancien `head`.
* Pointer `head` vers ce nouveau nœud.

Insertion au milieu/à la fin.

Insertion après le nœud X.

* Créer un nouveau nœud avec les données données.
* Pointer le `next` du nouveau nœud vers l'ancien `next` de X.
* Pointer le `next` de X vers ce nouveau nœud.

**Complexité temporelle : O(1)**

### Suppression

Pour supprimer un élément existant de la liste.

Suppression au début

* Obtenir le nœud pointé par `head` comme Temp.
* Pointer `head` vers le `next` de Temp.
* Libérer la mémoire utilisée par le nœud Temp.

Suppression au milieu/à la fin.

Suppression après le nœud X.

* Obtenir le nœud pointé par `X` comme Temp.
* Pointer le `next` de X vers le `next` de Temp.
* Libérer la mémoire utilisée par le nœud Temp.

**Complexité temporelle : O(1)**

### Parcours

Pour parcourir la liste.

Parcours

* Obtenir le nœud pointé par `head` comme Current.
* Vérifier si Current n'est pas null et l'afficher.
* Pointer Current vers le `next` de Current et passer à l'étape précédente.

**Complexité temporelle : O(n) // Ici n est la taille de la liste chaînée**

## **Implémentation**

### **Implémentation en C++ d'une liste chaînée simplement**

```text
// Fichiers d'en-tête
#include <iostream>

struct node
{
    int data;
    struct node *next;
};

// Le pointeur head pointe toujours vers le premier élément de la liste chaînée
struct node *head = NULL;
```

#### **Affichage des données dans chaque nœud**

```text
// Afficher la liste
void printList()
{
    struct node *ptr = head;

    // Commencer depuis le début
while(ptr != NULL)
{
    std::cout << ptr->data << " ";
    ptr = ptr->next;
}

std::cout << std::endl;
}
```

#### **Insertion au début**

```text
// Insérer un lien au début
void insertFirst(int data)
{
    // Créer un nouveau nœud
    struct node *new_node = new struct node;

    new_node->data = data;

// Le pointer vers l'ancien head
new_node->next = head;

// Pointer head vers le nouveau nœud
head = new_node;

std::cout << "Insertion réussie" << std::endl;
}
```

#### **Suppression au début**

```text
// Supprimer le premier élément
void deleteFirst()
{
    // Sauvegarder la référence vers head
    struct node *temp = head;

    // Pointer head vers le next de head
head = head->next;

// Libérer la mémoire utilisée par temp
temp = NULL:
delete temp;

std::cout << "Suppression réussie" << std::endl;
}
```

#### **Taille**

```text
// Trouver le nombre de nœuds dans la liste chaînée
void size()
{
    int length = 0;
    struct node *current;

    for(current = head; current != NULL; current = current->next)
{
    length++;
}

std::cout << "La taille de la liste chaînée est " << length << std::endl;
}
```

#### **Recherche**

```text
// Trouver un nœud avec les données données
void find(int data){

    // Commencer depuis le head
struct node* current = head;

// Si la liste est vide
if(head == NULL)
{
    std::cout << "La liste est vide" << std::endl;
    return;
}

// Parcourir la liste
while(current->data != data){

    // Si c'est le dernier nœud
    if(current->next == NULL){
        std::cout << "Non trouvé" << std::endl;
        return;
    }
    else{
        // Aller au nœud suivant
        current = current->next;
    }
}

// Si les données sont trouvées
std::cout << "Trouvé" << std::endl;
}
```

#### **Suppression après un nœud**

```text
// Supprimer un nœud avec les données données
void del(int data){

    // Commencer depuis le premier nœud
struct node* current = head;
struct node* previous = NULL;

// Si la liste est vide
if(head == NULL){
    std::cout << "La liste est vide" << std::endl;
    return ;
}

// Naviguer dans la liste
while(current->data != data){

    // Si c'est le dernier nœud
    if(current->next == NULL){
        std::cout << "Élément non trouvé" << std::endl;
        return ;
    }
    else {
        // Stocker la référence au nœud courant
        previous = current;
        // Passer au nœud suivant
        current = current->next;
    }

}

// Trouvé une correspondance, mettre à jour le nœud
if(current == head) {
    // Changer head pour pointer vers le nœud suivant
    head = head->next;
}
else {
    // Sauter le nœud courant
    previous->next = current->next;
}

// Libérer l'espace utilisé par le nœud supprimé
current = NULL;
delete current;
std::cout << "Suppression réussie" << std::endl;
}
```

### **Implémentation en Python d'une liste chaînée simplement**

```text
class Node(object):
    # Constructeur
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Fonction pour obtenir les données
def get_data(self):
    return self.data

# Fonction pour obtenir le nœud suivant
def get_next(self):
    return self.next

# Fonction pour définir le champ next
def set_next(self, new_next):
    self.next = new_next
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
```

#### **Insertion**

```text
    # Fonction pour insérer des données
def insert(self, data):
    # new_node est un objet de la classe Node
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    print("Nœud avec les données " + str(data) + " est créé avec succès")
```

#### **Taille**

```text
    # Fonction pour obtenir la taille
def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    print("La taille de la liste chaînée est " + str(count))
```

#### **Recherche**

```text
    # Fonction pour rechercher des données
def search(self, data):
    current = self.head
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
    if current is None:
        print("Nœud avec les données " + str(data) + " n'est pas présent")
    else:
        print("Nœud avec les données " + str(data) + " est trouvé")
```

#### **Suppression après un nœud**

```text
    # Fonction pour supprimer un nœud avec des données
def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        print("Nœud avec les données " + str(data) + " n'est pas dans la liste")
    elif previous is None:
        self.head = current.get_next()
        print("Nœud avec les données " + str(data) + " est supprimé avec succès")
    else:
        previous.set_next(current.get_next())
        print("Nœud avec les données " + str(data) + " est supprimé avec succès")
```

**Avantages**

1. Les listes chaînées sont une structure de données dynamique, qui peut croître et décroître, allouant et désallouant de la mémoire pendant l'exécution du programme.
2. L'insertion et la suppression de nœuds sont facilement implémentées dans une liste chaînée à n'importe quelle position.

**Inconvénients**

1. Elles utilisent plus de mémoire que les tableaux en raison de la mémoire utilisée par leurs pointeurs (`next` et `prev`).
2. L'accès aléatoire n'est pas possible dans une liste chaînée. Nous devons accéder aux nœuds séquentiellement.
3. C'est plus complexe qu'un tableau. Si un langage prend en charge la vérification des limites des tableaux automatiquement, les tableaux vous serviront mieux.

#### **Remarque**

Nous devons utiliser free() en C et delete en C++ pour libérer l'espace utilisé par le nœud supprimé, tandis qu'en Python et Java, l'espace libre est collecté automatiquement par le garbage collector.