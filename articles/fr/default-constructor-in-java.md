---
title: Constructeur par défaut en Java – Exemple de constructeur de classe
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-13T16:53:28.000Z'
originalURL: https://freecodecamp.org/news/default-constructor-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/default-constructor.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Constructeur par défaut en Java – Exemple de constructeur de classe
seo_desc: 'In this article, we will talk about constructors, how to create our own
  constructors, and what default constructors are in Java.

  What is a constructor?

  As a class-based object-oriented programming term, a constructor is a unique method
  used to initia...'
---

Dans cet article, nous allons parler des constructeurs, comment créer nos propres constructeurs et ce que sont les constructeurs par défaut en Java.

## Qu'est-ce qu'un constructeur ?

En tant que terme de programmation orientée objet basée sur les classes, un constructeur est une méthode unique utilisée pour initialiser un nouvel objet (classe). Il y a quelques règles que vous devez suivre lors de la création de constructeurs. Ces règles incluent :

* Le nom du constructeur doit être le même que le nom de la classe.
* Le constructeur ne doit pas avoir de type de retour.

Avant de continuer, voyons à quoi ressemble une classe en Java :

```java
public class Student {
  String firstName;
  String lastName;
  int age;
}
```

Le code ci-dessus montre une classe appelée Student avec trois attributs – `firstName`, `lastName` et `age`. Nous supposerons que la classe est censée être un exemple pour l'inscription des étudiants. Rappelez-vous que les trois attributs n'ont aucune valeur, donc aucune des informations n'est codée en dur.

Maintenant, nous allons utiliser des constructeurs pour créer une nouvelle instance de notre objet `Student`. C'est-à-dire :

```java
public class Student {
  String firstName;
  String lastName;
  int age;

  // Constructeur Student
  public Student(){
      firstName = "Ihechikara";
      lastName = "Abba";
      age = 100;
  }
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      System.out.println(myStudent.age);
      // 100
  }
}
```

Nous avons créé un constructeur que nous avons utilisé pour initialiser les attributs définis dans l'objet `Student`. Le code ci-dessus est un exemple de constructeur **sans argument**. Voyons maintenant un exemple d'un autre type :

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  // constructeur
  public Student(String firstName, String lastName, int age){
      this.firstName = firstName;
      this.lastName = lastName;
      this.age = age;
  }
  
  public static void main(String args[]) {
    Student myStudent = new Student("Ihechikara", "Abba", 100);
    System.out.println(myStudent.age);
  }

}
```

Nous avons maintenant créé un **constructeur paramétré**. Un constructeur paramétré est un constructeur créé avec des arguments/paramètres. Décomposons-le.

```java
public Student(String firstName, String lastName, int age){
      
  }
```

Nous avons créé un nouveau constructeur qui prend trois arguments – deux chaînes de caractères et un entier.

```java
this.firstName = firstName;
this.lastName = lastName;
this.age = age;
```

Nous avons ensuite lié ces arguments aux attributs que nous avons définis lors de la création de notre classe. Maintenant, nous avons initialisé l'objet Student en utilisant un constructeur.

```java
public static void main(String args[]) {
    Student myStudent = new Student("Ihechikara", "Abba", 100);
    System.out.println(myStudent.age);
  }
```

Enfin, nous avons créé une nouvelle instance de l'objet Student et passé nos arguments. Nous avons pu passer ces arguments parce que nous les avions déjà définis dans un constructeur.

J'ai créé un constructeur avec trois arguments, mais vous pouvez également créer des constructeurs séparés pour initialiser chaque attribut.

Maintenant que vous savez ce qu'est un constructeur en Java et comment l'utiliser, examinons maintenant les constructeurs par défaut.

## Qu'est-ce qu'un constructeur par défaut ?

Un constructeur par défaut est un constructeur créé par le compilateur si nous ne définissons aucun constructeur pour une classe. Voici un exemple :

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      
      myStudent.firstName = "Ihechikara";
      myStudent.lastName = "Abba";
      myStudent.age = 100;
      
      System.out.println(myStudent.age);
      //100
      
      System.out.println(myStudent.firstName);
      //Ihechikara
  }
}
```

Pouvez-vous repérer la différence entre ceci et les deux exemples précédents ? Remarquez que nous n'avons défini aucun constructeur avant de créer `myStudent` pour initialiser les attributs créés dans la classe.

Cela ne nous lancera pas d'erreur. Au contraire, le compilateur créera un constructeur vide, mais vous ne verrez ce constructeur nulle part dans le code – cela se passe sous le capot.

Voici à quoi ressemblera le code ci-dessus lorsque le compilateur commencera à faire son travail :

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  
  /* constructeur vide créé par le compilateur. Ce constructeur ne sera pas vu dans votre code */
  Student() {
  
  }
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      
      myStudent.firstName = "Ihechikara";
      myStudent.lastName = "Abba";
      myStudent.age = 100;
      
      System.out.println(myStudent.age);
      //100
      
      System.out.println(myStudent.firstName);
      //Ihechikara
  }
}
```

Beaucoup de gens confondent le constructeur par défaut avec le constructeur sans argument, mais ils ne sont pas les mêmes en Java. Tout constructeur créé par le programmeur n'est pas considéré comme un constructeur par défaut en Java.

## Conclusion

Dans cet article, nous avons appris ce que sont les constructeurs et comment nous pouvons les créer et les utiliser pour initialiser nos objets.

Nous avons également parlé des constructeurs par défaut et de ce qui les distingue des constructeurs sans argument.

Bon codage !