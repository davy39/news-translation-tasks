---
title: indexOf en Java – Comment trouver l'index d'une chaîne de caractères en Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-24T16:11:05.000Z'
originalURL: https://freecodecamp.org/news/indexof-in-java-how-to-find-the-index-of-a-string-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/index.jpg
tags:
- name: Java
  slug: java
seo_title: indexOf en Java – Comment trouver l'index d'une chaîne de caractères en
  Java
seo_desc: 'A string is a collection of characters nested in double quotes. The indexOf
  method returns the index position of a specified character or substring in a string.

  In this article, we''ll see the syntax for the different indexOf methods. We''ll
  also look ...'
---

Une chaîne de caractères (string) est une collection de caractères entourée de guillemets doubles. La méthode `indexOf` renvoie la position de l'index d'un caractère ou d'une sous-chaîne spécifiée dans une chaîne.

Dans cet article, nous verrons la syntaxe des différentes méthodes `indexOf`. Nous examinerons également quelques exemples pour vous aider à les comprendre et à les utiliser efficacement pour trouver l'index d'un caractère ou d'une sous-chaîne dans votre code Java.

## Syntaxe de la méthode `indexOf` 

La méthode `indexOf` dispose des variantes suivantes :

```java
public int indexOf(int char)
public int indexOf(int char, int fromIndex)
public int indexOf(String str)
public int indexOf(String str, int fromIndex)
```

Expliquons ces paramètres avant de voir quelques exemples :

* `char` représente un caractère unique dans une chaîne.
* `fromIndex` signifie la position à partir de laquelle la recherche de l'index d'un caractère ou d'une sous-chaîne doit commencer. C'est important lorsque vous avez deux caractères/chaînes qui ont la même valeur dans une chaîne de caractères. Avec ce paramètre, vous pouvez indiquer à la méthode `indexOf` où commencer son opération.
* `str` représente une sous-chaîne dans une chaîne.

Ne vous inquiétez pas si vous ne comprenez pas encore comment tout cela fonctionne – les exemples rendront tout cela clair !

## Comment utiliser la méthode indexOf en Java

Dans le premier exemple ci-dessous, nous allons trouver l'index d'un seul caractère dans une chaîne. Cet exemple nous aidera à comprendre la méthode `public int indexOf(int char)`.

### Exemple de la méthode `indexOf(int Char)`

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    System.out.println(greetings.indexOf("o"));
    
    // 4
  }
}

```

Dans le code ci-dessus, l'index du caractère « o » qui nous a été renvoyé est 4. Nous avons deux caractères « o » mais c'est l'index du premier qui a été renvoyé.

Dans l'exemple suivant, nous verrons comment nous pouvons renvoyer l'index du deuxième « o ».

Si vous vous demandez comment les numéros d'index sont calculés, notez que le premier caractère d'une chaîne a un index de zéro, le deuxième caractère a un index de un, et ainsi de suite.

### Exemple de la méthode `indexOf(int Char, Int fromIndex)`

Voici un exemple qui explique la méthode `int indexOf(int char, int fromIndex)` :

```java
public class Main {
  public static void main(String[] args) {
    String greetings = "Hello World";
    
    System.out.println(greetings.indexOf("o", 5));
    
    // 7
  }
}

```

Dans l'exemple ci-dessus, nous indiquons à la méthode `indexOf` de commencer son opération à partir du cinquième index.

H => index 0

e => index 1

l => index 2

l => index 3

o => index 4

Notez que l'index 5 n'est pas le caractère « W ». Le cinquième index est l'espace entre « Hello » et « World ».

Ainsi, avec le code ci-dessus, tous les autres caractères précédant le cinquième index seront ignorés. 7 est renvoyé comme l'index du deuxième caractère « o ».

### Exemple de la méthode `Int indexOf(String Str)`

Dans l'exemple suivant, nous allons comprendre comment fonctionne la méthode `public int indexOf(String str)` qui renvoie l'index d'une sous-chaîne.

```java
public class Main {
  public static void main(String[] args) {
    String motivation = "Coding can be difficult but don't give up";
    
    System.out.println(motivation.indexOf("be"));
    
    // 11
  }
}

```

Vous vous demandez comment nous avons obtenu 11 ? Vous devriez consulter la section précédente pour comprendre comment les index sont comptés et comment les espaces entre les sous-chaînes comptent également comme des index.

Notez que lorsqu'une sous-chaîne est passée en paramètre, l'index renvoyé est l'index du premier caractère de la sous-chaîne – 11 est l'index du caractère « b ».

### Exemple de la méthode `indexOf(String Str, Int fromIndex)`

La dernière méthode – `public int indexOf(String str, int fromIndex)` – est identique à la méthode `public int indexOf(int char, int fromIndex)`. Elle renvoie un index à partir d'une position spécifiée.

Voici un exemple :

```java
public class Main {
  public static void main(String[] args) {
    String motivation = "The for loop is used for the following";
    
    System.out.println(motivation.indexOf("for", 5));
    
    // 21
  }
}

```

Dans l'exemple ci-dessus, nous avons spécifié que la méthode doit commencer son opération à partir du cinquième index, qui est l'index venant après la première sous-chaîne « for ». 21 est l'index de la deuxième sous-chaîne « for ».

Enfin, lorsque nous passons un caractère ou une sous-chaîne qui n'existe pas dans une chaîne, la méthode `indexOf` renvoie la valeur -1. Voici un exemple :

```java
public class Main {
  public static void main(String[] args) {
    String motivation = "The for loop is used for the following";
    
    System.out.println(motivation.indexOf("code"));
    
    // -1
  }
}

```

## Conclusion

Dans cet article, nous avons appris à utiliser les quatre méthodes `indexOf` avec un exemple expliquant chacune d'entre elles.

Nous avons également vu à quoi ressemble la syntaxe de chacune de ces méthodes et comment elles déterminent l'index à renvoyer.

Nous avons terminé en montrant ce qui se passe lorsqu'un caractère ou une sous-chaîne qui n'existe pas est passé en paramètre.

Bon codage !