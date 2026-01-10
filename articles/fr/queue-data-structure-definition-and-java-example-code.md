---
title: Structure de données de file d'attente – Définition et exemple de code Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-04T00:36:52.000Z'
originalURL: https://freecodecamp.org/news/queue-data-structure-definition-and-java-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/queue-data-structure.png
tags:
- name: data structures
  slug: data-structures
- name: Java
  slug: java
- name: queue
  slug: queue
seo_title: Structure de données de file d'attente – Définition et exemple de code
  Java
seo_desc: "In this article, we will talk about the queue data structure, its operations,\
  \ and how to implement these operations using an array in Java. \nWhat Is a Queue?\n\
  A queue is linear data structure that consists of a collection is of items that\
  \ follow a fir..."
---

Dans cet article, nous allons parler de la structure de données de file d'attente, de ses opérations et de la manière d'implémenter ces opérations à l'aide d'un tableau en Java. 

## Qu'est-ce qu'une file d'attente ?

Une **file d'attente** est une structure de données linéaire qui consiste en une collection d'éléments suivant une séquence **premier entré, premier sorti**. Cela implique que le premier élément inséré sera le premier à être retiré. On peut aussi dire que les éléments sont retirés dans l'ordre où ils ont été insérés.

En utilisant un exemple concret, nous pouvons comparer une structure de données de file d'attente à une file de personnes attendant pour un service. Une fois qu'une personne est servie, elle quitte la file pour que la personne suivante soit servie. Elles sont aidées dans l'ordre où elles sont arrivées.

## Structure d'une file d'attente

Une file d'attente est principalement composée de deux parties : l'avant/tête et l'arrière/queue. Pour des raisons de clarté et de cohérence, nous allons utiliser avant et arrière.

L'**arrière** est l'endroit où les éléments sont insérés et l'**avant** est la partie de la file d'attente où les éléments sont retirés/supprimés.

Voici un diagramme pour vous aider à mieux comprendre :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/queue-structure-2.png)

L'image montre un tableau avec diverses cellules. Les éléments sont insérés par l'**arrière** et retirés par l'**avant**. Il existe des termes utilisés pour l'insertion et la suppression d'éléments dans une file d'attente, que nous aborderons dans la section suivante.

Notez que vous pouvez inverser la structure de votre file d'attente – vous pouvez avoir l'avant à droite et l'arrière à gauche. Quelle que soit la structure que vous choisissez, n'oubliez pas que l'insertion des éléments se fait par l'arrière et la suppression par l'avant.

## Opérations courantes d'une file d'attente

Les opérations suivantes sont couramment utilisées dans une file d'attente :

* **Enqueue** : Ajoute un élément à l'arrière de la file d'attente.
* **Dequeue** : Retire un élément de l'avant de la file d'attente.
* **Front**/**Peek** : Retourne la valeur de l'élément à l'avant de la file d'attente sans le désenfiler (retirer) l'élément.
* **IsEmpty** : Vérifie si la file d'attente est vide.
* **IsFull** : Vérifie si la file d'attente est pleine.
* **Display** : Affiche tous les éléments de la file d'attente.

Avant de voir comment implémenter cela avec du code, vous devez comprendre comment les opérations **enqueue** et **dequeue** fonctionnent et comment elles affectent les positions avant et arrière. 

Les indices des tableaux dans la plupart des langages de programmation commencent à 0. Lors de l'implémentation de notre code, nous allons définir l'index des valeurs avant et arrière de notre tableau à -1. Cela nous permettra de déplacer correctement les positions avant et arrière à mesure que des valeurs sont ajoutées.

Considérez l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/front-and-back.png)

Les flèches montrent la position de l'avant et de l'arrière de notre tableau. Lorsque les deux positions sont à -1, cela signifie que le tableau est vide. 

Ajoutons quelques éléments à notre tableau et voyons ce qui se passe.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/queue-0.png)

Nous avons inséré (enqueued) notre premier élément – 5. La position de l'avant et de l'arrière a également changé. Ensuite, nous verrons ce qui se passe lorsque nous enqueuons plus d'éléments.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/queue-1.png)

Un deuxième élément a été ajouté, mais seule l'arrière a bougé. Cela continuera à mesure que nous enqueuons plus d'éléments. L'avant et l'arrière se sont déplacés ensemble dans le dernier exemple afin que l'avant puisse prendre la position du premier élément. 

Puisque c'était le premier et le seul élément à ce moment-là, l'avant et l'arrière se sont positionnés à cet endroit. Mais maintenant que nous avons enqueué plus d'éléments, l'arrière continuera à suivre le dernier élément. 

Nous allons continuer et remplir le tableau pour voir ce qui se passe lorsque nous désenfilons.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/queue-4.png)

Ainsi, la flèche arrière a suivi les éléments dans l'ordre où ils ont été ajoutés jusqu'au dernier. Maintenant, supprimons (dequeue) quelques éléments. 

Rappelez-vous la séquence **premier arrivé, premier servi** ? Lorsque nous exécutons l'opération dequeue, elle supprimera d'abord 5 de la file d'attente. Si nous l'exécutons à nouveau, elle passera au nombre suivant, qui est 10, et continuera dans cet ordre aussi longtemps que nous l'appellerons.

Voici la première opération dequeue :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/dequeue-1.png)

Maintenant, la flèche avant s'est déplacée à l'index 1. Cela implique que l'élément à l'index 0 a été supprimé. Par supprimé, nous ne voulons pas dire du tableau mais de la file d'attente – seuls les éléments de la position avant à la position arrière font partie de la file d'attente.

Dans le même ordre, si nous continuons à supprimer des éléments, cela arrivera à un point où la flèche avant rencontrera la flèche arrière à la fin de la file d'attente. Si nous désenfilons à nouveau à ce moment-là, la flèche avant se déplacera au-delà de la flèche arrière et la file d'attente sera considérée comme vide car il n'y a rien à supprimer. Lorsque cela se produit, nous réinitialiserons leur index à -1 (leur point de départ initial).

Il est temps pour du code !

## Implémentation de la file d'attente en Java

Nous allons décomposer cette section en créant chaque opération puis en mettant tout ensemble à la fin. 

```java
int queueLength = 3;
int items[] = new int[queueLength];
int front = -1; 
int back = -1;
```

Nous avons créé nos variables et leurs paramètres. Nous utilisons 3 comme nombre maximum d'éléments qui peuvent être enfilés dans le tableau. Comme nous l'avons vu dans les images de la section précédente, nous avons défini l'index initial de l'avant et de l'arrière à -1.

Ensuite, nous allons définir les fonctionnalités **isEmpty** et **isFull**.

Pour **isEmpty** :

```java
boolean isEmpty(){
      if(front == -1 && back == -1){
          return true;
      } else {
          return false;
      }
  }
```

Assez facile à comprendre si vous avez suivi la section précédente. Le tableau est vide uniquement si l'index de l'avant et de l'arrière est -1. 

Pour **isFull** :

```java
boolean isFull(){
      if(back == queueLength - 1){
          return true;
      } else {
          return false;
      }
  }
```

Celui-ci peut sembler un peu trompeur, mais voici la logique : notre nombre maximum d'éléments autorisés dans le tableau est 3, mais trois éléments dans un tableau ne sont pas désignés par l'index 3 mais 2 puisque le premier index est 0. Donc, la longueur maximale moins 1 nous donne l'index 2 qui est la troisième cellule dans un tableau.

Lorsque toutes les cellules ont été enfilées avec une valeur jusqu'à la troisième cellule, le tableau est plein.

Pour **enQueue** :

```java
void enQueue(int itemValue) {
      if(isFull()){
          System.out.println("La file est pleine");
      } else if(front == -1 && back == -1){
          front = back = 0;
          items[back] = itemValue;
      } else{
          back++;
          items[back] = itemValue;
      }
  }
```

Si le tableau est plein, nous obtenons un message indiquant qu'il est plein. Si l'avant et l'arrière sont à -1, alors l'élément est assigné à la première cellule qui est l'index 0 – sinon, la valeur est insérée et la position arrière est incrémentée.

Pour **deQueue** :

```java
void deQueue(){
      if(isEmpty()){
          System.out.println("La file est vide. Rien à désenfiler");
      } else if (front == back){
          front = back = -1;
      } else {
          front++;
      }
  }
```

Ici, si le tableau est vide, nous obtenons le message correspondant. Si l'avant a rencontré l'arrière, nous réinitialisons leur index à -1 comme nous l'avons vu dans les images de la section précédente. Si les deux dernières conditions ne sont pas applicables, alors l'avant est incrémenté.

Pour **display** :

```java
void display(){
      int i;
     
      if(isEmpty()){
          System.out.println("La file est vide");
      } else {
          for(i = front; i <= back; i++){
              System.out.println(items[i]);
          }
      }
  }
```

Ici, si le tableau n'est pas vide, nous parcourons et affichons tous les éléments.

Enfin, pour **peek** :

```java
void peak(){
      System.out.println("La valeur de l'avant est : " + items[front]);
  }
```

Cela affiche simplement la valeur de l'élément de l'avant.

Ce sont toutes les opérations pour notre file d'attente. Voici toutes ensemble ci-dessous :

```java
// Implémentation de la file d'attente en Java

public class Queue {
  
  int queueLength = 3;
  int items[] = new int[queueLength];
  int front = -1; 
  int back = -1;
  
  boolean isFull(){
      if(back == queueLength - 1){
          return true;
      } else {
          return false;
      }
  }
  
  boolean isEmpty(){
      if(front == -1 && back == -1){
          return true;
      } else {
          return false;
      }
  }

    
  
  void enQueue(int itemValue) {
      if(isFull()){
          System.out.println("La file est pleine");
      } else if(front == -1 && back == -1){
          front = back = 0;
          items[back] = itemValue;
      } else{
          back++;
          items[back] = itemValue;
      }
  }
  
  void deQueue(){
      if(isEmpty()){
          System.out.println("La file est vide. Rien à désenfiler");
      } else if (front == back){
          front = back = -1;
      } else {
          front++;
      }
  }
  
  void display(){
      int i;
     
      if(isEmpty()){
          System.out.println("La file est vide");
      } else {
          for(i = front; i <= back; i++){
              System.out.println(items[i]);
          }
      }
  }
  
  void peak(){
      System.out.println("La valeur de l'avant est : " + items[front]);
  }
  
}
```

Maintenant, exécutons les opérations :

```java
 public static void main(String[] args) {
    Queue myQueue = new Queue();
    
    myQueue.enQueue(3);
    myQueue.enQueue(2);
    myQueue.enQueue(1);

    
    myQueue.display();
    
    myQueue.peak();
    
    
  }
```

`enQueue(3)` insère 3 dans notre file d'attente, de même pour les deux lignes de code suivantes.

`display()` affiche les éléments du tableau.

`peak()` affiche la valeur de l'élément de l'avant.

Nous n'avons pas exécuté `deQueue`, donc vous pouvez essayer vous-même – affichez votre tableau et jetez un coup d'œil après avoir désenfilé et voyez ce qui se passe. Il existe diverses façons de modifier le code, alors amusez-vous !

## Conclusion

Dans cet article, nous avons défini une file d'attente et sa structure. Nous avons ensuite vu quelques exemples utilisant des images pour montrer comment les positions avant et arrière d'une file d'attente réagissent lorsque des éléments sont enfilés et désenfilés.

Enfin, nous avons vu comment implémenter la structure de données de file d'attente en utilisant des tableaux en Java.

Merci d'avoir lu et bon codage !