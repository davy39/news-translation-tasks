---
title: 'Tutoriel Java : Convertir une Chaîne en Tableau de Caractères'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T23:06:14.000Z'
originalURL: https://freecodecamp.org/news/string-to-char-array-java-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/k.png
tags:
- name: Java
  slug: java
seo_title: 'Tutoriel Java : Convertir une Chaîne en Tableau de Caractères'
seo_desc: 'By Thanoshan MV

  In this article, we’ll look at how to convert a string to an array of characters
  in Java. I''ll also briefly explain to you what strings, characters, and arrays
  are.

  What is a Character in Java?

  Characters are primitive datatypes. A ch...'
---

Par Thanoshan MV

Dans cet article, nous allons voir comment convertir une chaîne de caractères en un tableau de caractères en Java. Je vais également vous expliquer brièvement ce que sont les chaînes, les caractères et les tableaux.

## Qu'est-ce qu'un Caractère en Java ?

Les caractères sont des types de données primitifs. Un caractère est un seul caractère enfermé dans des guillemets simples. Il peut s'agir d'une lettre, d'un chiffre, d'un signe de ponctuation, d'un espace ou autre chose de similaire. Par exemple :

```java
char firstVowel = 'a';
```

## Qu'est-ce qu'une Chaîne en Java ?

Les chaînes sont des objets (type de référence). Une chaîne est composée d'une suite de caractères. C'est tout ce qui se trouve à l'intérieur de guillemets doubles. Par exemple :

```java
String vowels = "aeiou";
```

## Qu'est-ce qu'un Tableau en Java ?

Les tableaux sont des structures de données fondamentales qui peuvent stocker un nombre fixe d'éléments du même type de données en Java. Par exemple, déclarons un tableau de caractères :

```java
char[] vowelArray = {'a', 'e', 'i', 'o', 'u'};
```

Maintenant, nous avons une compréhension de base de ce que sont les chaînes, les caractères et les tableaux.

## Convertissons une Chaîne en Tableau de Caractères

### 1. Utiliser la Méthode d'Instance toCharArray()

`toCharArray()` est une méthode d'instance de la classe `String`. Elle retourne un nouveau tableau de caractères basé sur l'objet chaîne actuel.

Regardons un exemple :

```java
// définir une chaîne
String vowels = "aeiou";

// créer un tableau de caractères
char[] vowelArray = vowels.toCharArray();

// imprimer vowelArray
System.out.println(Arrays.toString(vowelArray));
```

Sortie : `[a, e, i, o, u]`

Lorsque nous convertissons une chaîne en un tableau de caractères, la longueur reste la même. Vérifions la longueur de `vowels` et `vowelArray` :

```java
System.out.println("La longueur de 'vowels' est " + vowels.length());
System.out.println("La longueur de 'vowelArray' est " + vowelArray.length);
```

Sortie :

```
La longueur de 'vowels' est 5
La longueur de 'vowelArray' est 5
```

Nous pouvons utiliser diverses méthodes pour imprimer un tableau. J'ai utilisé la méthode statique `toString()` de la classe utilitaire `Arrays`.

Vous pouvez en savoir plus sur la méthode d'instance `toCharArray()` dans la [documentation Java](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#toCharArray--).

### 2. Utiliser la Méthode d'Instance charAt()

`charAt()` est une méthode d'instance de la classe `String`. Elle retourne un caractère à l'index spécifié de la chaîne actuelle.

**NOTE :** une chaîne est basée sur un index zéro, similaire à un tableau.

Voyons comment nous pouvons convertir une chaîne en un tableau de caractères en utilisant `charAt()` :

```java
// définir une chaîne
String vowels = "aeiou";

// créer un tableau de caractères. La longueur est celle de vowels
char[] vowelArray = new char[vowels.length()];

// boucle pour itérer chaque caractère dans la chaîne 'vowels'
for (int i = 0; i < vowels.length(); i++) {
    // ajouter chaque caractère au tableau de caractères
    vowelArray[i] = vowels.charAt(i);
}

// imprimer le tableau
System.out.println(Arrays.toString(vowelArray));
```

Sortie : `[a, e, i, o, u]`

Vous pouvez en savoir plus sur la méthode d'instance `charAt()` dans la [documentation Java](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#charAt-int-).

Je viens de vous montrer une autre façon de convertir une chaîne en un tableau de caractères, mais nous pouvons utiliser la méthode `toCharArray()` pour convertir facilement au lieu de créer des boucles et de les itérer.

N'hésitez pas à me faire part de vos suggestions ou questions.

Photo par [Alex Alvarez](https://unsplash.com/@a2_foto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://www.freecodecamp.org/news/s/photos/happy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

**Soutenez freeCodeCamp dans leur [Campagne de Promesse de Curriculum en Science des Données](https://www.freecodecamp.org/news/building-a-data-science-curriculum-with-advanced-math-and-machine-learning/).**

Connectez-vous avec moi sur [Medium](https://mvthanoshan.medium.com/).

Merci 😇

**Bon Codage ❤️**

### **Plus sur la Programmation en Java**

1. [Principes de la Programmation Orientée Objet en Java : Concepts POO pour Débutants](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/)
2. [Méthodes de Tableau Java – Comment Imprimer un Tableau en Java](https://www.freecodecamp.org/news/java-array-methods-how-to-print-an-array-in-java/)
3. [Java String to Int – Comment Convertir une Chaîne en Entier](https://www.freecodecamp.org/news/java-string-to-int-how-to-convert-a-string-to-an-integer/)
4. [Générateur de Nombres Aléatoires Java – Comment Générer des Entiers avec Math Random](https://www.freecodecamp.org/news/generate-random-numbers-java/)