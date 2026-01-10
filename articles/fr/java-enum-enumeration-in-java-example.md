---
title: Java Enum – Exemple d'énumération en Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-25T21:33:55.000Z'
originalURL: https://freecodecamp.org/news/java-enum-enumeration-in-java-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/enum.jpg
tags:
- name: Java
  slug: java
seo_title: Java Enum – Exemple d'énumération en Java
seo_desc: "An enumeration (enum for short) in Java is a special data type which contains\
  \ a set of predefined constants. \nYou'll usually use an enum when dealing with\
  \ values that aren't required to change, like days of the week, seasons of the year,\
  \ colors, and ..."
---

Une énumération (enum en abrégé) en Java est un type de données spécial qui contient un ensemble de constantes prédéfinies. 

Vous utiliserez généralement un `enum` lorsque vous traitez des valeurs qui n'ont pas besoin de changer, comme les jours de la semaine, les saisons de l'année, les couleurs, etc.

Dans cet article, nous verrons comment créer un `enum` et comment attribuer sa valeur à d'autres variables. Nous verrons également comment utiliser un `enum` dans des instructions `switch` ou parcourir ses valeurs. 

## Comment créer un Enum en Java

Pour créer un `enum`, nous utilisons le mot-clé `enum`, de la même manière que vous créeriez une classe en utilisant le mot-clé `class`.  

Voici un exemple :

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}
```

Dans le code ci-dessus, nous avons créé un `enum` appelé `Colors`. Vous remarquerez peut-être que les valeurs de cet `enum` sont toutes écrites en majuscules – c'est juste une convention générale. Vous n'obtiendrez pas d'erreur si les valeurs sont en minuscules.

Chaque valeur dans un `enum` est séparée par une virgule.

Ensuite, nous allons créer une nouvelle variable et lui attribuer l'une des valeurs de notre `enum`. 

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red); 
    // RED
  } 
}

```

C'est similaire à l'initialisation de n'importe quelle autre variable. Dans le code ci-dessus, nous avons initialisé une variable `Colors` et lui avons attribué l'une des valeurs d'un `enum` en utilisant la syntaxe par point : `Colors red = Colors.RED;`. 

Notez que nous pouvons créer notre `enum` à l'intérieur de la classe `Main` et le code fonctionnera toujours. C'est-à-dire : 

```java
public class Main { 
  enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red); 
  } 
}

```

Si nous voulons obtenir le numéro d'index de l'une des valeurs, nous devrons utiliser la méthode `ordinal()`. Voici un exemple : 

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red.ordinal()); 
    // 0
  } 
}

```

`red.ordinal()` du code ci-dessus renvoie 0. 

## Comment utiliser un Enum dans une instruction Switch

Dans cette section, nous verrons comment nous pouvons utiliser un `enum` dans une instruction `switch`.

Voici un exemple :

```java
  public class Main { 
      enum Colors {
      RED,
      BLUE,
      YELLOW,
      GREEN
  }
  public static void main(String[] args) { 
    
    Colors myColor = Colors.YELLOW;

    switch(myColor) {
      case RED:
        System.out.println("La couleur est rouge");
        break;
      case BLUE:
         System.out.println("La couleur est bleue");
        break;
      case YELLOW:
        System.out.println("La couleur est jaune");
        break;
      case GREEN:
        System.out.println("La couleur est verte");
        break;
    }
  } 
}

```

C'est un exemple très basique de la façon dont nous pouvons utiliser un `enum` dans une instruction `switch`. Nous obtiendrions "La couleur est jaune" imprimé dans la console car c'est le seul `case` qui correspond à la condition de l'instruction `switch`.

## Comment parcourir les valeurs d'un Enum

L'`enum` en Java possède une méthode `values()` qui renvoie un tableau des valeurs d'un `enum`. Nous allons utiliser une boucle for-each pour parcourir et afficher les valeurs de notre `enum`. 

Voici comment nous pouvons faire cela :

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
      
      for (Colors allColors : Colors.values()) {
      System.out.println(allColors);
      
      /* 
      RED
      BLUE
      YELLOW
      GREEN
      */
    }
    
  } 
}

```

## Conclusion

Dans cet article, nous avons appris ce qu'est un `enum` en Java, comment le créer et comment attribuer ses valeurs à d'autres variables.

Nous avons également vu comment utiliser le type `enum` avec une instruction `switch` et comment nous pouvons parcourir les valeurs d'un `enum`. 

Bon codage !