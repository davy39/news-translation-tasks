---
title: Instruction Switch Java – Comment utiliser une instruction Switch Case en Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-21T17:39:06.000Z'
originalURL: https://freecodecamp.org/news/java-switch-statement-how-to-use-a-switch-case-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/jaye-haych-bPOEB3sy4As-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: Instruction Switch Java – Comment utiliser une instruction Switch Case
  en Java
seo_desc: "You use the switch statement in Java to execute a particular code block\
  \ when a certain condition is met. \nHere's what the syntax looks like:\nswitch(expression)\
  \ {\n  case 1:\n    // code block\n    break;\n  case 2:\n    // code block\n  \
  \  break;\n    case 3..."
---

Vous utilisez l'instruction `switch` en Java pour exécuter un bloc de code particulier lorsqu'une certaine condition est remplie. 

Voici à quoi ressemble la syntaxe :

```java
switch(expression) {
  case 1:
    // bloc de code
    break;
  case 2:
    // bloc de code
    break;
    case 3:
    // bloc de code
    break;
  default:
    // bloc de code
}
```

Ci-dessus, l'`expression` entre parenthèses du `switch` est comparée à chaque `case`. Lorsque l'`expression` est identique au `case`, le bloc de code correspondant dans le `case` est exécuté. 

Si aucun des cas ne correspond à l'`expression`, alors le bloc de code défini sous le mot-clé `default` est exécuté. 

Nous utilisons le mot-clé `break` pour terminer le code dès qu'une certaine condition est remplie (lorsque l'`expression` correspond à un `case`).

Regardons quelques exemples de code.

## Comment utiliser une instruction Switch Case en Java

Jetez un œil au code suivant :

```java
class CurrentMonth {
    public static void main(String[] args) {
        
        int month = 6;
        
        switch (month) {
          case 1:
            System.out.println("January");
            break;
          case 2:
            System.out.println("February");
            break;
          case 3:
            System.out.println("March");
            break;
          case 4:
            System.out.println("April");
            break;
          case 5:
            System.out.println("May");
            break;
          case 6:
            System.out.println("June");
            break;
          case 7:
            System.out.println("July");
            break;
          case 8:
            System.out.println("August");
            break;
          case 9:
            System.out.println("September");
            break;
          case 10:
            System.out.println("October");
            break;
          case 11:
            System.out.println("November");
            break;
          case 12:
            System.out.println("December");
            break;
            
            // June
        }
    }
}
```

Dans le code ci-dessus, June est affiché. Ne vous inquiétez pas du code volumineux. Voici une explication pour vous aider à comprendre :

Nous avons créé un entier appelé `month` et lui avons attribué une valeur de 6 : `int month = 6;`. 

Ensuite, nous avons créé une instruction `switch` et y avons passé la variable `month` comme paramètre : `switch (month){...}`. 

La valeur de `month`, qui agit comme l'expression pour l'instruction `switch`, sera comparée à chaque valeur de `case` dans le code. Nous avons les cas de 1 à 12. 

La valeur de `month` est 6, donc elle correspond au `case` 6. C'est pourquoi le code dans le `case` 6 a été exécuté. Tous les autres blocs de code ont été ignorés. 

Voici un autre exemple pour simplifier les choses :

```java
class Username {
    public static void main(String[] args) {
        
        String username = "John";
        
        switch (username) {
          case "Doe":
            System.out.println("Username is Doe");
            break;
          case "John":
            System.out.println("Username is John");
            break;
          case "Jane":
            System.out.println("Username is Jane");
            break;
            // Username is John
        }
    }
}
```

Dans l'exemple ci-dessus, nous avons créé une chaîne appelée `username` qui a une valeur de "John".

Dans l'instruction `switch`, `username` est passé en tant qu'expression. Nous avons ensuite créé trois cas – "Doe", "John", et "Jane". 

Parmi les trois classes, une seule correspond à la valeur de `username` — "John". Par conséquent, le bloc de code dans `case "John"` a été exécuté.

## Comment utiliser le mot-clé Default dans une instruction Switch

Dans les exemples de la section précédente, notre code a été exécuté parce qu'un `case` correspondait à une `expression`. 

Dans cette section, vous verrez comment utiliser le mot-clé `default`. Vous pouvez l'utiliser comme solution de repli dans les situations où aucun des cas ne correspond à l'`expression`. 

Voici un exemple :

```java
class Username {
    public static void main(String[] args) {
        
        String username = "Ihechikara";
        
        switch (username) {
          case "Doe":
            System.out.println("Username is Doe");
            break;
          case "John":
            System.out.println("Username is John");
            break;
          case "Jane":
            System.out.println("Username is Jane");
            break;
          default:
            System.out.println("Username not found!");
            // Username not found!
        }
    }
}
```

La variable `username` dans l'exemple ci-dessus a une valeur de "Ihechikara". 

Le bloc de code pour le mot-clé `default` sera exécuté parce qu'aucun des cas créés ne correspond à la valeur de `username`. 

## Résumé

Dans cet article, nous avons vu comment utiliser l'instruction `switch` en Java. 

Nous avons également parlé de l'expression de l'instruction `switch`, des cas et du mot-clé default en Java, ainsi que de leurs cas d'utilisation avec des exemples de code. 

Bon codage !