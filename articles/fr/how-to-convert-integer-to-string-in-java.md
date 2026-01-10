---
title: Int to String in Java – Comment convertir un entier en chaîne de caractères
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-05T15:57:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-integer-to-string-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/marcel-eberle-rendLSpkDtY-unsplash--1-.jpg
tags:
- name: Java
  slug: java
seo_title: Int to String in Java – Comment convertir un entier en chaîne de caractères
seo_desc: "You can convert variables from one data type to another in Java using different\
  \ methods. \nIn this article, you'll learn how to convert integers to strings in\
  \ Java in the following ways:\n\nUsing the Integer.toString() method. \nUsing the\
  \ String.valueOf(..."
---

Vous pouvez convertir des variables d'un type de données à un autre en Java en utilisant différentes méthodes.

Dans cet article, vous apprendrez comment convertir des entiers en chaînes de caractères en Java de les manières suivantes :

* En utilisant la méthode `Integer.toString()`.
* En utilisant la méthode `String.valueOf()`.
* En utilisant la méthode `String.format()`.
* En utilisant la classe `DecimalFormat`.

## Comment convertir un entier en chaîne de caractères en Java en utilisant `Integer.toString()`

La méthode `Integer.toString()` prend l'entier à convertir comme paramètre. Voici à quoi ressemble la syntaxe :

```
Integer.toString(INTEGER_VARIABLE)
```

Voici un exemple :

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        String AGE_AS_STRING = Integer.toString(age);
        
        System.out.println("L'enfant a " + AGE_AS_STRING + " ans");
        // L'enfant a 2 ans
    }
}
```

Dans l'exemple ci-dessus, nous avons créé un entier – `age` – et nous lui avons assigné une valeur de 2.

Pour convertir la variable `age` en chaîne de caractères, nous l'avons passée comme paramètre à la méthode `Integer.toString()` : `Integer.toString(age)`.

Nous avons stocké cette nouvelle valeur de chaîne dans une variable de chaîne appelée `AGE_AS_STRING`.

Nous avons ensuite concaténé la nouvelle variable de chaîne avec d'autres chaînes : `"L'enfant a " + AGE_AS_STRING + " ans"`.

Mais une erreur serait-elle levée si nous concaténions simplement la variable age avec ces autres chaînes sans aucune sorte de conversion ?

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        System.out.println("L'enfant a " + age + " ans");
        // L'enfant a 2 ans
    }
}
```

La sortie ci-dessus est la même que dans l'exemple où nous avons dû convertir l'entier en chaîne de caractères.

Alors, comment savons-nous si la conversion de type a vraiment fonctionné ?

Nous pouvons vérifier les types de variables en utilisant l'objet Java `getClass()`. C'est-à-dire :

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = Integer.toString(age);
        
        
        System.out.println(((Object)age).getClass().getSimpleName());
        // Integer
        
        System.out.println(AGE_AS_STRING.getClass().getSimpleName());
        // String
    }
}
```

Maintenant, nous pouvons vérifier que lorsque la variable `age` a été créée, c'était un `Integer`, et après la conversion de type, elle est devenue une `String`.

## Comment convertir un entier en chaîne de caractères en Java en utilisant `String.valueOf()`

La méthode `String.valueOf()` prend également la variable à convertir en chaîne de caractères comme paramètre.

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = String.valueOf(age);
        
        System.out.println("L'enfant a " + AGE_AS_STRING + " ans");
        // L'enfant a 2 ans
    }
}
```

Le code ci-dessus est similaire à celui de la dernière section :

* Nous avons créé un entier appelé `age`.
* Nous avons passé l'entier `age` comme paramètre à la méthode `String.valueOf()` : `String.valueOf(age)`.

Vous pouvez également vérifier si la conversion de type a fonctionné en utilisant l'objet `getClass()` :

```java
System.out.println(((Object)age).getClass().getSimpleName());
// Integer
        
System.out.println(AGE_AS_STRING.getClass().getSimpleName());
// String
```

## Comment convertir un entier en chaîne de caractères en Java en utilisant `String.format()`

La méthode `String.format()` prend deux paramètres : un spécificateur de format et la variable à formater.

Voici un exemple :

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = String.format("%d", age);
        
        System.out.println("L'enfant a " + AGE_AS_STRING + " ans");
        // L'enfant a 2 ans
        
    }
}

```

Dans l'exemple ci-dessus, nous avons passé deux paramètres à la méthode `String.format()` : `"%d"` et `age`.

`"%d"` est un spécificateur de format qui indique que la variable à formater est un entier.

`age`, qui est le deuxième paramètre, sera converti en chaîne de caractères et stocké dans la variable `AGE_AS_STRING`.

Vous pouvez également vérifier les types de variables avant et après la conversion :

```java
System.out.println(((Object)age).getClass().getSimpleName());
// Integer
        
System.out.println(AGE_AS_STRING.getClass().getSimpleName());
// String
```

## Comment convertir un entier en chaîne de caractères en Java en utilisant `DecimalFormat`

La classe `DecimalFormat` est utilisée pour formater les nombres décimaux en Java. Vous pouvez l'utiliser de différentes manières, mais nous allons l'utiliser pour convertir un entier en chaîne de caractères.

Voici un exemple :

```java
import java.text.DecimalFormat;

class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        DecimalFormat DFormat = new DecimalFormat("#");
        
        
        String AGE_AS_STRING = DFormat.format(age);
        
        System.out.println("L'enfant a " + AGE_AS_STRING + " ans");
        // L'enfant a 2 ans
        
        
        System.out.println(((Object)age).getClass().getSimpleName());
        // Integer
        
        System.out.println(AGE_AS_STRING.getClass().getSimpleName());
        // String
        
    }
}
```

Décomposons le code :

* Pour pouvoir utiliser la classe `DecimalFormat` dans l'exemple ci-dessus, nous l'avons importée : `import java.text.DecimalFormat;`.
* Nous avons créé la variable entière `age`.
* Nous avons ensuite créé un nouvel objet de la classe `DecimalFormat` appelé `DFormat`.
* En utilisant la méthode `format()` de l'objet, nous avons converti `age` en chaîne de caractères : `DFormat.format(age);`.

## Résumé

Dans cet article, nous avons parlé de la conversion d'entiers en chaînes de caractères en Java.

Nous avons vu des exemples qui montraient comment utiliser trois méthodes différentes – `Integer.toString()`, `String.valueOf()`, `String.format()` – et la classe `DecimalFormat` pour convertir des variables d'entiers en chaînes de caractères.

Chaque exemple a montré comment vérifier le type de données d'une variable avant et après la conversion.

Bon codage !