---
title: String to Int in Java – Comment convertir une chaîne en entier
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-03T22:02:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-integer-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/marcel-eberle-rendLSpkDtY-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: String to Int in Java – Comment convertir une chaîne en entier
seo_desc: "When working with a programming language, you may want to convert strings\
  \ to integers. An example would be performing a mathematical operation using the\
  \ value of a string variable. \nIn this article, you'll learn how to convert a string\
  \ to an integer ..."
---

Lorsque vous travaillez avec un langage de programmation, vous pouvez vouloir convertir des chaînes en entiers. Un exemple serait d'effectuer une opération mathématique en utilisant la valeur d'une variable de chaîne. 

Dans cet article, vous apprendrez comment convertir une chaîne en entier en Java en utilisant deux méthodes de la classe `Integer` — `parseInt()` et `valueOf()`.

## Comment convertir une chaîne en entier en Java en utilisant `Integer.parseInt`

La méthode `parseInt()` prend la chaîne à convertir en entier comme paramètre. C'est-à-dire :

```txt
Integer.parseInt(string_varaible)
```

Avant de voir un exemple de son utilisation, voyons ce qui se passe lorsque vous ajoutez une valeur de chaîne et un entier sans aucune sorte de conversion :

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        System.out.println(age + 20);
        // 1020
    }
}
```

Dans le code ci-dessus, nous avons créé une variable `age` avec une valeur de chaîne "10". 

Lorsque nous l'avons ajoutée à une valeur entière de 20, nous avons obtenu 1020 au lieu de 30. 

Voici une solution rapide en utilisant la méthode `parseInt()` :

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        int age_to_int = Integer.parseInt(age);
        
        System.out.println(age_to_int + 20);
        // 30
    }
}
```

Afin de convertir la variable `age` en entier, nous l'avons passée comme paramètre à la méthode `parseInt()` — `Integer.parseInt(age)` — et nous l'avons stockée dans une variable appelée `age_to_int`. 

Lorsque nous l'avons ajoutée à un autre entier, nous avons obtenu une addition correcte : `age_to_int + 20`. 

## Comment convertir une chaîne en entier en Java en utilisant `Integer.valueOf`

La méthode `valueOf()` fonctionne exactement comme la méthode `parseInt()`. Elle prend la chaîne à convertir en entier comme paramètre. 

Voici un exemple :

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        int age_to_int = Integer.valueOf(age);
        
        System.out.println(age_to_int + 20);
        // 30
    }
}
```

L'explication pour le code ci-dessus est la même que dans la section précédente :

* Nous avons passé la chaîne comme paramètre à `valueOf()` : `Integer.valueOf(age)`. Elle a été stockée dans une variable appelée `age_to_int`.
* Nous avons ensuite ajouté 20 à la variable créée : `age_to_int + 20`. La valeur résultante était 30 au lieu de 1020.

## Résumé

Dans cet article, nous avons parlé de la conversion de chaînes en entiers en Java. 

Nous avons vu comment convertir une chaîne en entier en Java en utilisant deux méthodes de la classe `Integer` — `parseInt()` et `valueOf()`.

Bon codage !