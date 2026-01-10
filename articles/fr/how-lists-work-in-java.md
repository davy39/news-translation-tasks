---
title: Java List – Exemples de listes en Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-31T18:09:00.000Z'
originalURL: https://freecodecamp.org/news/how-lists-work-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/java-list-interface-cover.png
tags:
- name: Java
  slug: java
seo_title: Java List – Exemples de listes en Java
seo_desc: "You can use the Java List interface to store objects/elements in an ordered\
  \ collection. It extends the Collection interface. \nThe  List interface provides\
  \ us with various methods for inserting, accessing, and deleting elements in a collection.\
  \  \nIn t..."
---

Vous pouvez utiliser l'interface Java `List` pour stocker des objets/éléments dans une collection ordonnée. Elle étend l'interface Collection. 

L'interface `List` nous fournit diverses méthodes pour insérer, accéder et supprimer des éléments dans une collection. 

Dans cet article, vous apprendrez comment étendre et implémenter l'interface `List` en Java, et comment interagir avec les éléments d'une collection. 

## Classes d'implémentation de l'interface Java List

Voici les différentes classes d'implémentation de l'interface `List` en Java :

* AbstractList.
* AbstractSequentialList.
* ArrayList.
* AttributeList.
* CopyOnWriteArrayList.
* LinkedList.
* RoleList.
* RoleUnresolvedList.
* Stack.
* Vector.

Les implémentations les plus couramment utilisées de l'interface `List` sont `ArrayList` et `LinkedList`. 

Puisque les deux classes ci-dessus implémentent l'interface `List`, elles utilisent les mêmes méthodes pour ajouter, accéder, mettre à jour et supprimer des éléments dans une collection. 

Dans ce tutoriel, nous allons voir comment nous pouvons ajouter, accéder, mettre à jour et supprimer des éléments dans une collection en utilisant `ArrayList`.

## Comment implémenter une `List` en Java en utilisant `ArrayList`

Contrairement aux tableaux en Java, qui ont une taille spécifiée, `ArrayList` est plus dynamique lorsqu'il s'agit de stocker des éléments. Cela signifie que vous pouvez ajouter des éléments comme vous le souhaitez. 

Voici comment vous pouvez créer un `ArrayList` :

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
  }
}
```

Dans le code ci-dessus, nous avons d'abord importé la classe `ArrayList` : `import java.util.ArrayList;`.

Nous avons ensuite créé un nouvel objet `ArrayList` appelé `students` : `ArrayList<String> students = new ArrayList<String>();`.

Notez que les types de données des éléments qui seraient stockés dans l'`ArrayList` ont été spécifiés entre chevrons : `<String>`.

### Comment ajouter des éléments à l'`ArrayList`

Vous pouvez utiliser la méthode `add()` pour ajouter des éléments à l'`ArrayList`.

Voici un exemple :

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    
    System.out.println(students);
    // [John, Jane, Doe]
    
  }
}
```

Dans le code ci-dessus, nous avons passé l'élément à ajouter à l'`ArrayList` en tant que paramètre : `students.add("Doe")`.

### Comment accéder aux éléments de l'`ArrayList`

Pour accéder aux éléments de l'`ArrayList`, vous utilisez la méthode `get()`. Voici comment :

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    System.out.println(students.get(1));
    // Jane
    
  }
}


```

Comme on peut le voir ci-dessus, nous avons passé l'index de l'élément à accéder en tant que paramètre à la méthode `get()` : `students.get(1)`.

### Comment mettre à jour les éléments de l'`ArrayList`

Pour mettre à jour la valeur des éléments dans l'`ArrayList`, vous utilisez la méthode `set()`. 

Elle prend deux paramètres : l'index de l'élément à mettre à jour et la nouvelle valeur. 

Voici un exemple :

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.set(2,"Jade");
    
    System.out.println(students);
    // [John, Jane, Jade]
    
  }
}
```

### Comment supprimer des éléments de l'`ArrayList`

Pour supprimer des éléments de l'`ArrayList`, vous utilisez la méthode `remove()`. Nous utilisons également l'index pour spécifier quel élément supprimer. 

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.remove(2);
    
    System.out.println(students);
    // [John, Jane]
    
  }
}


```

Vous pouvez utiliser la méthode `clear()` pour supprimer tous les éléments de la collection :

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.clear();
    
    System.out.println(students);
    // []
    
  }
}


```

Bien que les classes `ArrayList` et `LinkedList` aient toutes deux les mêmes méthodes comme vu dans les exemples de cet article, la classe `LinkedList` a quelques méthodes supplémentaires comme :

* `addFirst()` ajoute un élément au début de la liste.
* `addLast()` ajoute un élément à la fin de la liste.
* `getFirst()` retourne le premier élément de la liste.
* `getLast()` retourne le dernier élément de la liste.
* `removeFirst()` supprime le premier élément de la liste.
* `removeLast()` supprime le dernier élément de la liste.

## Résumé

Dans cet article, nous avons parlé de l'interface `List` en Java. Vous l'utilisez pour stocker des collections ordonnées d'éléments. 

Nous avons examiné certaines des classes d'implémentation de l'interface `List`. Les plus couramment utilisées sont les classes `ArrayList` et `LinkedList`.

En utilisant des exemples de code, nous avons vu comment ajouter, accéder, mettre à jour et supprimer des éléments dans une collection avec `ArrayList`.

Bien que `ArrayList` et `LinkedList` aient des méthodes similaires, nous avons mis en évidence certaines des méthodes supplémentaires que vous pouvez utiliser avec la classe `LinkedList`. 

Bon codage !