---
title: Pourquoi Static en Java ? Que signifie ce mot-clé ? [Résolu]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-24T21:38:54.000Z'
originalURL: https://freecodecamp.org/news/why-static-in-java-what-does-this-keyword-mean
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/radowan-nakif-rehan-cYyqhdbJ9TI-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: Pourquoi Static en Java ? Que signifie ce mot-clé ? [Résolu]
seo_desc: "You can use the static keyword in different parts of a Java program like\
  \ variables, methods, and static blocks. \nThe main purpose of using the static\
  \ keyword in Java is to save memory. When we create a variable in a class that will\
  \ be accessed by oth..."
---

Vous pouvez utiliser le mot-clé `static` dans différentes parties d'un programme Java comme les variables, les méthodes et les blocs statiques. 

Le but principal de l'utilisation du mot-clé `static` en Java est d'économiser de la mémoire. Lorsque nous créons une variable dans une classe qui sera accessible par d'autres classes, nous devons d'abord créer une instance de la classe puis assigner une nouvelle valeur à chaque instance de variable – même si la valeur des nouvelles variables doit être la même dans toutes les nouvelles classes/objets. 

Mais lorsque nous créons des variables statiques, leur valeur reste constante dans toutes les autres classes, et nous n'avons pas besoin de créer une instance pour utiliser la variable. Ainsi, nous créons la variable une seule fois, donc la mémoire n'est allouée qu'une seule fois. 

Vous comprendrez mieux cela avec les exemples dans les sections qui suivent.

Afin de comprendre ce qu'est le mot-clé `static` et ce qu'il fait réellement, nous verrons quelques exemples qui montrent son utilisation dans la déclaration de variables statiques, de méthodes et de blocs en Java. 

## Comment créer une variable statique en Java

Pour comprendre l'utilisation du mot-clé `static` dans la création de variables, regardons la manière habituelle de créer des variables partagées dans chaque instance d'une classe.

```java
class Student {
    String studentName; 
    String course; 
    String school;
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        Student1.school = "freeCodeCamp";
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        Student2.school = "freeCodeCamp";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

Je vais expliquer ce qui s'est passé dans le code ci-dessus étape par étape. 

Nous avons créé une classe appelée `Student` avec trois variables – `studentName`, `course` et `school`. 

Nous avons ensuite créé deux instances de la classe `Student` :

```java
Student Student1 = new Student();
Student Student2 = new Student();
```

La première instance – `Student1` – qui a accès aux variables créées dans sa classe avait ces valeurs : 

```java
Student1.studentName = "Ihechikara";
Student1.course = "Data Visualization";
Student1.school = "freeCodeCamp";
```

La deuxième instance avait ces valeurs : 

```java
Student2.studentName = "John";
Student2.course = "Data Analysis with Python";
Student2.school = "freeCodeCamp";
```

Si vous regardez de près, vous réaliserez que les deux étudiants ont le même nom d'école – "freeCodeCamp". Et si nous devions créer 100 étudiants pour la même école ? Cela signifie que nous initialiserions une variable avec la même valeur 100 fois – allouant une nouvelle mémoire à chaque fois. 

Bien que cela ne semble pas être un problème, dans une base de code beaucoup plus grande, cela pourrait devenir un défaut et ralentir inutilement votre programme.

Pour résoudre ce problème, nous utiliserons le mot-clé `static` pour créer la variable `school`. Après cela, toutes les instances de la classe peuvent utiliser cette variable.

Voici comment :

```java
class Student {
    String studentName; 
    String course; 
    static String school;
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        Student1.school = "freeCodeCamp";
        
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

Dans le code ci-dessus, nous avons créé une variable statique appelée `school`. Vous remarquerez que le mot-clé `static` précédait le type de données et le nom de la variable : `static String school = "freeCodeCamp";`. 

Maintenant, lorsque nous créons une nouvelle instance de notre classe, nous n'avons pas besoin d'initialiser la variable `school` pour chaque instance. Dans notre code, nous avons seulement assigné une valeur à la variable dans la première instance et elle a été héritée par la deuxième instance également.

Notez que changer la valeur de la variable statique n'importe où dans le code remplace la valeur dans d'autres parties du code où elle a été déclarée précédemment. 

Vous ne devriez donc utiliser le mot-clé `static` que pour les variables qui doivent rester constantes dans le programme. 

Vous pouvez également assigner une valeur à la variable lorsqu'elle est créée afin de ne pas avoir à la déclarer à nouveau lorsque vous créez une instance de classe : `static String school = "freeCodeCamp";`.

Vous aurez ceci si vous utilisez la méthode ci-dessus :

```java
class Student {
    String studentName; 
    String course; 
    static String school = "freeCodeCamp";
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

Dans la dernière section, vous verrez comment initialiser des variables statiques en utilisant des blocs statiques.

## Comment créer une méthode statique en Java

Avant de regarder un exemple, voici quelques choses que vous devez savoir sur les méthodes statiques en Java : 

* Les méthodes statiques ne peuvent **accéder et modifier que** les variables statiques. 
* Les méthodes statiques peuvent être appelées/utilisées sans créer d'instance de classe.

Voici un exemple pour vous aider à comprendre :

```java
class EvenNumber {
    
    static int evenNumber;
    
    static void incrementBy2(){
        evenNumber = evenNumber + 2;
        System.out.println(evenNumber);
    }
        
    public static void main(String[] args) {
        incrementBy2(); // 2
        incrementBy2(); // 4
        incrementBy2(); // 6
        incrementBy2(); // 8
    }
}
```

Dans le code ci-dessus, nous avons créé un entier (`evenNumber`) dans une classe appelée `EvenNumber`. 

Notre méthode statique s'appelle `incrementBy2()`. Cette méthode augmente la valeur de l'entier `evenNumber` et imprime sa valeur. 

Sans créer d'instance de classe, nous avons pu appeler la méthode `incrementBy2()` dans la méthode `main` du programme. Chaque fois que nous avons appelé la méthode, la valeur de `evenNumber` a été incrémentée de 2 et imprimée.

Vous pouvez également attacher le nom de la classe à la méthode en utilisant la notation pointée lors de l'appel de la méthode : `EvenNumber.incrementBy2();`. Chaque méthode statique appartient à la classe et non aux instances de la classe.

## Comment créer un bloc statique en Java

Les blocs statiques en Java sont similaires aux constructeurs. Nous pouvons les utiliser pour initialiser des variables statiques, et ils sont exécutés par le compilateur avant la méthode `main`. 

```java
class Block {
    
    static int year;
    
    static {
        year = 2022;
        System.out.println("This code block got executed first");
    }
        
    public static void main(String[] args) {
        
        System.out.println("Hello World");
        System.out.println(year);
    }
}

```

Dans le code ci-dessus, nous avons créé une variable statique entière `year`. Nous l'avons ensuite initialisée dans un bloc statique :

```java
static {
        year = 2022;
        System.out.println("This code block got executed first");
    }
```

Vous pouvez créer un bloc statique, comme vous pouvez le voir ci-dessus, en utilisant le mot-clé `static` suivi d'accolades. Dans le bloc statique de notre code, nous avons initialisé la variable `year` avec une valeur de 2022. Nous avons également imprimé un texte – "This code block got executed first". 

Dans la méthode `main`, nous avons imprimé "Hello World" et la variable statique `year`. 

Dans la console, le code sera exécuté dans cet ordre : 

```txt
This code block got executed first
Hello World
2022
```

Cela démontre comment le code dans le bloc statique est exécuté en premier avant la méthode `main`. 

## Résumé

Dans cet article, nous avons parlé du mot-clé `static` en Java. C'est un mot-clé qui nous aide principalement à optimiser la mémoire dans nos programmes Java. 

Nous avons vu comment créer des variables et des méthodes statiques avec des exemples. 

Enfin, nous avons parlé des blocs statiques que vous pouvez utiliser pour initialiser des variables statiques. Les blocs statiques sont exécutés avant la méthode principale.

Bon codage !