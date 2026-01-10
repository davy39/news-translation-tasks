---
title: Les chaînes de caractères en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/strings-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d00740569d1a4ca3559.jpg
tags:
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Les chaînes de caractères en Java
seo_desc: 'Strings

  Strings are sequences of characters. In Java, a String is an Object. Strings should
  not be confused with char as characters are literally 1 value rather than a sequence
  of characters. You can still use 1 value within a String, however it is p...'
---

# **Les chaînes de caractères**

Les chaînes de caractères sont des séquences de caractères. En Java, une `String` est un `Object`. Les chaînes de caractères ne doivent pas être confondues avec `char`, car les caractères sont littéralement une seule valeur plutôt qu'une séquence de caractères. Vous pouvez toujours utiliser une seule valeur dans une chaîne de caractères, cependant, il est préférable d'utiliser `char` lorsque vous vérifiez un seul caractère.

```java
String course = "FCC";
System.out.println(course instanceof Object);
```

Sortie :

```text
true
```

Vous pouvez créer un objet String de plusieurs manières :

1. `String str = "I am a String"; //en tant que littéral de chaîne`
2. `String str = "I am a " + "String"; //en tant qu'expression constante`
3. `String str = new String("I am a String"); //en tant qu'objet String utilisant le constructeur`

Vous pourriez vous demander : Quelle est la différence entre les trois ?

Eh bien, utiliser le mot-clé `new` garantit qu'un nouvel objet `String` sera créé et qu'un nouvel emplacement mémoire sera alloué dans la mémoire `Heap` [(cliquez ici pour en savoir plus)](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html). Les littéraux de chaîne et les expressions de chaîne constantes sont mis en cache au moment de la compilation. Le compilateur les place dans le String Literal Pool pour éviter les doublons et améliorer la consommation de mémoire. L'allocation d'objets est coûteuse et cette astuce augmente les performances lors de l'instanciation des chaînes. Si vous utilisez le même littéral à nouveau, la JVM utilise le même objet. Utiliser le constructeur comme ci-dessus est presque toujours un choix moins bon.

Dans cet extrait de code, combien d'objets String sont créés ?

```java
String str = "This is a string";
String str2 = "This is a string";
String str3 = new String("This is a string");
```

La réponse est : 2 objets String sont créés. `str` et `str2` font tous deux référence au même objet. `str3` a le même contenu mais l'utilisation de `new` a forcé la création d'un nouvel objet distinct.

Lorsque vous créez un littéral de chaîne, la JVM vérifie en interne ce que l'on appelle le `String pool` pour voir si elle peut trouver un objet String similaire (en termes de contenu). Si elle le trouve, elle retourne la même référence. Sinon, elle crée simplement un nouvel objet String dans le pool afin que la même vérification puisse être effectuée à l'avenir.

Vous pouvez tester cela en utilisant la comparaison d'objets rapide `==` et la méthode `equals()`.

```java
System.out.println(str == str2); // Cela affiche 'true'
System.out.println(str == str3); // Cela affiche 'false'
System.out.println(str.equals(str3)); // Cela affiche 'true'
```

Voici un autre exemple sur la façon de créer une chaîne en Java en utilisant les différentes méthodes :

```java
public class StringExample{  

   public static void main(String args[]) {  
      String s1 = "java";  // création de chaîne par littéral de chaîne Java  
      char ch[] = {'s','t','r','i','n','g','s'};  
      String s2 = new String(ch);  // conversion de tableau de caractères en chaîne  
      String s3 = new String("example");  // création de chaîne Java par mot-clé new  
      System.out.println(s1);  
      System.out.println(s2);  
      System.out.println(s3);  
   }
}
```

#### **Comparaison des chaînes de caractères**

Si vous souhaitez comparer la valeur de deux variables de type String, vous ne pouvez pas utiliser ==. Cela est dû au fait que cela comparera les références des variables et non les valeurs qui leur sont associées. Pour comparer les valeurs stockées des chaînes, vous utilisez la méthode equals.

```java
boolean equals(Object obj)
```

Elle retourne true si deux objets sont égaux et false sinon.

```java
String str = "Hello world";
String str2 = "Hello world";

System.out.println(str == str2); // Cela affiche false
System.out.println(str.equals(str2)); // Cela affiche true
```

La première comparaison est false car "==" regarde les références et elles ne sont pas les mêmes.

La deuxième comparaison est true car les variables stockent les mêmes valeurs. Dans ce cas, "Hello world".

Nous avons plusieurs méthodes intégrées dans String. Voici un exemple de la méthode Length() de String.

```java
public class StringDemo {

   public static void main(String args[]) {
      String palindrome = "Dot saw I was Tod";
      int len = palindrome.length();
      System.out.println( "La longueur de la chaîne est : " + len );
   }
}
```

Cela donnera comme résultat - `La longueur de la chaîne est : 17`

**La réponse est : 2** objets String sont créés. **Notes**

1. Les méthodes String utilisent des index basés sur zéro, sauf pour le deuxième argument de `substring()`.
2. La classe String est finale - ses méthodes ne peuvent pas être remplacées.
3. Lorsque le littéral String est trouvé par la JVM, il est ajouté au pool de littéraux String.
4. La classe String possède une méthode nommée `length()`, tandis que les tableaux ont un attribut nommé length.
5. En Java, les objets String sont immuables. Immuable signifie simplement non modifiable ou inchangable. Une fois l'objet String créé, ses données ou son état ne peuvent pas être changés, mais un nouvel objet String est créé.

Longueur de la chaîne

La "longueur" d'une chaîne est simplement le nombre de caractères qu'elle contient. Donc "hi" a une longueur de 2 et "Hello" a une longueur de 5. La méthode length() sur une chaîne retourne sa longueur, comme ceci :

```java
String a = "Hello";
int len = a.length();  // len est 5
```

#### **Autres méthodes de comparaison qui peuvent également être utilisées sur la chaîne sont :**

1. equalsIgnoreCase() :- compare la chaîne sans prendre en compte la sensibilité à la casse.

```java
String a = "HELLO";
String b = "hello";
System.out.println(a.equalsIgnoreCase(b));   // Cela affichera true
```

1. compareTo :- compare la valeur lexicographiquement et retourne un entier.

```java
String a = "Sam";
String b = "Sam";
String c = "Ram";
System.out.println(a.compareTo(b));       // 0
System.out.println(a.compareTo(c));       // 1 puisque (a>b)
System.out.println(c.compareTo(a));       // -1 puisque (c<a)
```