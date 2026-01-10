---
title: Qu'est-ce qu'une HashMap en Java ?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-12T20:53:24.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-java-hashmap
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/tyler-nix-7ukf-r-Oh-k-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: Qu'est-ce qu'une HashMap en Java ?
seo_desc: "In Java, you use a HashMap to store items in key/value pairs. You can access\
  \ items stored in a HashMap using the item's key, which is unique for each item.\
  \ \nIn this article, we'll talk about the features of a HashMap, how to create a\
  \ HashMap, and the..."
---

En Java, vous utilisez une HashMap pour stocker des éléments sous forme de paires clé/valeur. Vous pouvez accéder aux éléments stockés dans une `HashMap` en utilisant la clé de l'élément, qui est unique pour chaque élément. 

Dans cet article, nous allons parler des caractéristiques d'une `HashMap`, de la manière de créer une `HashMap` et des différentes méthodes que nous pouvons utiliser pour interagir avec les données qui y sont stockées. 

## Quelles sont les caractéristiques d'une HashMap en Java ?

Avant de travailler avec les HashMaps, il est important de comprendre comment elles fonctionnent.

Voici quelques-unes des caractéristiques d'une `HashMap` :

* Les éléments sont stockés sous forme de paires clé/valeur. 
* Les éléments ne maintiennent aucun ordre lorsqu'ils sont ajoutés. Les données sont non ordonnées. 
* Dans le cas où il y a des clés en double, la dernière écrasera les autres. 
* Les types de données sont spécifiés en utilisant des classes wrapper au lieu de types de données primitifs. 

## Comment créer une HashMap en Java

Pour créer et utiliser une HashMap, vous devez d'abord importer le package `java.util.HashMap`. C'est-à-dire :

```java
import java.util.HashMap;
```

Voici à quoi ressemble la syntaxe pour créer une nouvelle `HashMap` :

```txt
HashMap<KeyDataType, ValueDataType> HashMapName = new HashMap<>();
```

Expliquons certains des termes clés dans la syntaxe ci-dessus. 

* `KeyDataType` désigne le type de données de toutes les clés qui seront stockées dans la `HashMap`. 
* `ValueDataType` désigne le type de données de toutes les valeurs qui seront stockées dans la `HashMap`. 
* `HashMapName` désigne le nom de la `HashMap`. 

Voici un exemple pour simplifier les termes :

```java
HashMap<Integer, String> StudentInfo = new HashMap<>();
```

Dans le code ci-dessus, nous avons créé une `HashMap` appelée `StudentInfo`. Les clés qui seront stockées dans la `HashMap` seront toutes des entiers tandis que les valeurs seront des chaînes de caractères. 

Vous remarquerez que nous travaillons avec des classes wrapper et non des types primitifs lors de la spécification des types de données pour les clés et les valeurs. C'est ainsi que fonctionnent les HashMaps. 

Avant de plonger dans les exemples, voici une liste des classes wrapper et leurs types de données primitifs correspondants en Java :

### Classes Wrapper et Types Primitifs en Java

| Classes wrapper   |      Types de données primitifs      |
|----------|:-------------:|
| Integer |  int	 |
| Character |    char   |
| Float | float | 
| Byte |  byte	 |
| Short | short | 
| Long |  long	 |
| Double |    double   |
| Boolean | boolean | 

Lorsque vous travaillez avec des HashMaps, vous utilisez des classes wrapper. 

## Méthodes HashMap en Java

Dans cette section, nous allons parler de certaines des méthodes utiles que vous pouvez utiliser lorsque vous travaillez avec des HashMaps. 

Vous apprendrez comment ajouter, accéder, supprimer et mettre à jour des éléments dans une `HashMap`. 

### Comment ajouter des éléments à une `HashMap` en Java

Pour ajouter des éléments à une `HashMap`, nous utilisons la méthode `put()`. Elle prend deux paramètres — la clé et la valeur de l'élément ajouté. 

Voici comment cela fonctionne :

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        System.out.println(StudentInfo);
        // {1=Ihechikara, 2=Jane, 3=John}
    }
}
```

Dans le code ci-dessus, la `HashMap` s'appelle `StudentInfo`. Nous avons spécifié les clés comme des entiers tandis que les valeurs étaient des chaînes de caractères : `HashMap<Integer, String>`. 

Pour ajouter des éléments à la `HashMap`, nous avons utilisé la méthode `put()` : 

```java
StudentInfo.put(1, "Ihechikara");
StudentInfo.put(2, "Jane");
StudentInfo.put(3, "John");
```

Nous avons ajouté trois éléments, chacun ayant un entier comme clé et une chaîne de caractères comme valeur. 

### Comment accéder aux éléments d'une `HashMap` en Java

Vous pouvez utiliser la méthode `get()` pour accéder aux éléments stockés dans une `HashMap`. Elle prend un paramètre — la clé de l'élément accédé. 

Voici un exemple :

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        System.out.println(StudentInfo.get(2));
        // Jane
    }
}
```

Dans l'exemple ci-dessus, `StudentInfo.get(2)` retourne la valeur avec une clé de `2`. "Jane" a été imprimé sur la console.

### Comment changer la valeur des éléments dans une HashMap en Java

Pour changer la valeur des éléments dans une `HashMap`, nous utilisons la méthode `replace()`. Elle prend deux paramètres — la clé de l'élément à changer et la nouvelle valeur à lui attribuer.

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Mettre à jour la clé 1
        StudentInfo.replace(1, "Doe");
        
        System.out.println(StudentInfo);
        // {1=Doe, 2=Jane, 3=John}
    }
}
```

Lorsque la `HashMap` ci-dessus a reçu des éléments, l'élément avec une clé de `1` avait une valeur de "Ihechikara". 

Nous avons changé sa valeur en "Doe" en utilisant la méthode `replace()` : `StudentInfo.replace(1, "Doe");`

### Comment supprimer des éléments dans une `HashMap` en Java

Vous pouvez utiliser la méthode `remove()` pour supprimer un élément d'une `HashMap`. Elle prend un paramètre — la clé de l'élément à supprimer. 

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Supprimer la clé 1
        StudentInfo.remove(1);
        
        System.out.println(StudentInfo);
        // {2=Jane, 3=John}
    }
}
```

En utilisant la méthode `remove()`, nous avons supprimé l'élément avec une clé de `1`. 

Si vous souhaitez supprimer tous les éléments d'une `HashMap` en une seule fois, vous utilisez la méthode `clear()`. C'est-à-dire : 

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Supprimer tous les éléments
        StudentInfo.clear();
        
        System.out.println(StudentInfo);
        // {}
    }
}
```

Il existe d'autres méthodes utiles comme :

* `containsKey` qui retourne `true` si une clé spécifiée existe dans une `HashMap`.
* `containsValue` qui retourne `true` si une valeur spécifiée existe dans une `HashMap`.
* `size()` qui retourne le nombre d'éléments dans une `HashMap`. 
* `isEmpty()` qui retourne `true` si une `HashMap` n'a aucun élément, et ainsi de suite.

## Résumé

Dans cet article, nous avons parlé de `HashMap` en Java. Tout d'abord, nous avons parlé des caractéristiques d'une `HashMap`.

Nous avons ensuite vu comment créer une `HashMap` et certaines des méthodes que vous pouvez utiliser pour interagir avec les données qui y sont stockées, avec des exemples de code.

Bon codage !