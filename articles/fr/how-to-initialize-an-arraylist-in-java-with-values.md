---
title: Comment initialiser une ArrayList en Java - Déclaration avec des valeurs
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-21T06:34:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-initialize-an-arraylist-in-java-with-values
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/java-arraylist-1.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Comment initialiser une ArrayList en Java - Déclaration avec des valeurs
seo_desc: "You can use an ArrayList in Java to store and manipulate a collection of\
  \ similar variables. \nAn ArrayList is just like an array but offers more flexibility.\
  \ An ArrayList is more dynamic with the size of the collection, and gives you more\
  \ control over..."
---

Vous pouvez utiliser une `ArrayList` en Java pour stocker et manipuler une collection de variables similaires. 

Une `ArrayList` est similaire à un [tableau](https://www.freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example/) mais offre plus de flexibilité. Une `ArrayList` est plus dynamique avec la taille de la collection et vous donne plus de contrôle sur les éléments d'une collection. 

Dans cet article, vous apprendrez à déclarer et initialiser une `ArrayList` en Java. Vous verrez les différentes méthodes intégrées qui peuvent être utilisées pour ajouter, accéder, modifier et supprimer des éléments dans une `ArrayList`. 

Commençons !

## Comment déclarer une ArrayList avec des valeurs en Java

Les termes "déclaration" et "initialisation" sont couramment associés aux structures de données.

La déclaration concerne la création d'une structure de données, tandis que l'initialisation implique l'assignation de valeurs à la structure de données. 

Voici comment vous pouvez déclarer une `ArrayList` en Java :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
    }
}
```

Pour utiliser une `ArrayList`, vous devez d'abord l'importer depuis la classe **ArrayList** : `import java.util.ArrayList;`.

Après cela, vous pouvez créer un nouvel objet `ArrayList`. Dans le code ci-dessus, nous avons créé un nouvel objet `ArrayList` appelé `people`.

Notez que le type de données de l'`ArrayList` est spécifié avec des chevrons : `ArrayList<String>`.

À ce stade, nous avons créé une `ArrayList` mais elle n'a pas d'éléments. Vous verrez comment ajouter des éléments dans une autre section. 

Alternativement, vous pouvez créer une `ArrayList` avec des valeurs/éléments au moment de la déclaration en utilisant la méthode `add` dans un bloc d'initialisation :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>() {{
            add("John");
            add("Jane");
            add("Doe");
        }}; 
        
        System.out.println(people);
        // [John, Jane, Doe]
    }
}
```

## Comment ajouter des éléments à une `ArrayList` Java

Vous pouvez utiliser la méthode `add()` pour ajouter des éléments à une `ArrayList`. 

Voici un exemple :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        System.out.println(people);
        // [John, Jane, Doe]
        
    }
}
```

Dans le code ci-dessus, nous avons déclaré une `ArrayList` appelée `people` sans aucun élément. 

En utilisant la notation par point et la méthode `add()`, nous avons ajouté des éléments à la collection `people` : `people.add("John")`. 

## Comment accéder aux éléments d'une `ArrayList` Java

Vous pouvez accéder aux éléments d'une `ArrayList` Java en utilisant l'index de l'élément. 

L'index de l'élément sera passé en tant que paramètre à la méthode `get()`. C'est-à-dire :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        System.out.println(people.get(0));
        // John
        
    }
}
```

Dans le code ci-dessus, `people.get(0)` obtient le premier élément — "John". 

Notez que le premier élément a un index de `0`, le deuxième a un index de `1`, et ainsi de suite.

## Comment modifier des éléments dans une `ArrayList` Java

Vous pouvez changer ou modifier la valeur d'un élément en utilisant la méthode `set()`. 

La méthode `set()` prend deux paramètres — l'index de l'élément à changer et la nouvelle valeur à assigner à cet index. 

Voici un exemple :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        people.set(1, "Jade");
        
        System.out.println(people);
        // [John, Jade, Doe]
        
    }
}
```

Dans l'exemple ci-dessus, nous avons changé le deuxième élément de "Jane" à "Jade" en utilisant son index : `people.set(1, "Jade")`. 

## Comment supprimer des éléments dans une `ArrayList` Java

Vous pouvez supprimer un élément en utilisant la méthode `remove()`. La méthode prend en paramètre l'index de l'élément à supprimer. C'est-à-dire :

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        people.remove(2);
        
        System.out.println(people);
        // [John, Jane]
        
    }
}
```

En utilisant la méthode `remove()`, nous avons supprimé le troisième élément de la collection en utilisant l'index de l'élément : `people.remove(2);`.

## Résumé

Dans cet article, nous avons parlé de la structure de données `ArrayList` en Java. Elle peut être utilisée pour stocker une collection de variables. 

Une `ArrayList` vous donne plus de contrôle sur les éléments d'une collection et a une taille dynamique qui n'est pas fixe à la déclaration comme les tableaux Java. 

Nous avons vu comment déclarer et initialiser une `ArrayList` avec des valeurs. Nous avons également vu différentes méthodes pour ajouter, accéder, modifier et supprimer des éléments dans une `ArrayList`. 

Bon codage ! Je parle également de Java sur [mon blog](https://ihechikara.com/).