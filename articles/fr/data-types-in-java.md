---
title: Types de données en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T21:01:00.000Z'
originalURL: https://freecodecamp.org/news/data-types-in-java
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7f740569d1a4ca3815.jpg
tags:
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Types de données en Java
seo_desc: Java is a strongly typed language. This means that, in Java, each data type
  has its own strict definition. There are no implicit data type conversions when
  any conflicts occur between the data types. Any change in data types should be explicitly
  decl...
---

Java est un langage fortement typé. Cela signifie qu'en Java, chaque type de données a sa propre définition stricte. Il n'y a pas de conversions implicites de types de données lorsqu'il y a des conflits entre les types de données. Tout changement de type de données doit être explicitement déclaré par le programmeur.

Java définit 8 types de données primitifs : `byte`, `short`, `int`, `long`, `char`, `float`, `double` et `boolean`.

Ils sont divisés en les catégories suivantes :

* Entiers
* Nombres à virgule flottante
* Caractères
* Type booléen

Les détails de chaque type de données sont donnés ci-dessous :

## **Entiers :**

Ils sont de quatre types : `byte`, `short`, `int`, `long`. Il est important de noter que ceux-ci sont des valeurs signées positives et négatives. Les entiers signés sont stockés dans un ordinateur en utilisant le [complément à deux](http://www.ele.uri.edu/courses/ele447/proj_pages/divid/twos.html). Il comprend à la fois des valeurs négatives et positives mais dans différents formats comme `(-1 à -128)` ou `(0 à +127)`. Un entier non signé peut contenir une valeur positive plus grande, et aucune valeur négative comme `(0 à 255)`. Contrairement au C++, il n'y a pas d'entier non signé en Java.

### **byte :**

Le type de données byte est un entier de 8 bits signé en complément à deux.

```text
Classe Wrapper : Byte

Valeur minimale : -128 (-2^7)

Valeur maximale : 127 (2^7 -1)

Valeur par défaut : 0

Exemple : byte a = 10, byte b = -50;
```

### **short :**

Le type de données short est un entier de 16 bits signé en complément à deux.

```text
Classe Wrapper : Short

Valeur minimale : -32,768 (-2^15)

Valeur maximale : 32,767 (2^15 -1)

Valeur par défaut : 0.

Exemple : short s = 10, short r = -1000;
```

### **int :**

Le type de données int est un entier de 32 bits signé en complément à deux. Il est généralement utilisé comme type de données par défaut pour les valeurs entières sauf s'il y a une préoccupation concernant la mémoire.

```text
Classe Wrapper : Integer

Valeur minimale : (-2^31)

Valeur maximale : (2^31 -1)

Valeur par défaut : 0.

Exemple : int a = 50000, int b = -20
```

### **long :**

Le type de données long est un entier de 64 bits signé en complément à deux.

```text
Classe Wrapper : Long

Valeur minimale : (-2^63)

Valeur maximale : (2^63 -1)

Valeur par défaut : 0L.

Exemple : long a = 100000L, long b = -600000L;

Par défaut, toutes les variables de type entier sont "int". Donc long num=600851475143 donnera une erreur.
Mais il peut être spécifié comme long en ajoutant le suffixe L (ou l)
```

## **Nombres à virgule flottante :**

Ceux-ci sont également appelés nombres réels et sont utilisés pour les expressions impliquant une précision fractionnaire. Ils sont de deux types : `float`, `double`. Float est en fait évité dans le cas de données précises telles que la monnaie ou les données de recherche.

### **float :**

Le type de données float est un nombre à virgule flottante de 32 bits en simple précision [IEEE 754](http://steve.hollasch.net/cgindex/coding/ieeefloat.html).

```text
Classe Wrapper : Float

Float est principalement utilisé pour économiser de la mémoire dans les grands tableaux de nombres à virgule flottante.

Valeur par défaut : 0.0f.

Exemple : float f1 = 24.5f;

Le type de données par défaut des nombres à virgule flottante est double. Donc float f = 24.5 introduira une erreur.
Cependant, nous pouvons ajouter le suffixe F (ou f) pour désigner le type de données comme float.
```

### **double :**

Le type de données double est un nombre à virgule flottante de 64 bits en double précision [IEEE 754](http://steve.hollasch.net/cgindex/coding/ieeefloat.html). Ce type de données est généralement le choix par défaut. Ce type de données ne doit jamais être utilisé pour des valeurs précises, telles que la monnaie.

```text
Classe Wrapper : Double

Ce type de données est généralement utilisé comme type de données par défaut pour les valeurs décimales.

Valeur par défaut : 0.0d.

Exemple : double d1 = 123.400778;
```

## **Caractère :**

Nous utilisons ce type de données pour stocker des caractères. Ce n'est pas la même chose que le char en C/C++. Java utilise un `UNICODE`, un ensemble de caractères internationalement accepté. Char en Java est de 16 bits tandis qu'en C/C++ il est de 8 bits.

```text
Classe Wrapper : Character

Valeur minimale : '\u0000' (ou 0).

Valeur maximale : '\uffff' (ou 65,535).

Valeur par défaut : null ('\u0000').

Exemple : char letterA ='a';
```

## **Booléen :**

Ceci est utilisé pour stocker des valeurs logiques. Un type booléen peut avoir une valeur de vrai ou faux. Ce type est généralement retourné par les opérateurs relationnels.

```text
Il n'y a que deux valeurs possibles : true et false.

Classe Wrapper : Boolean

Ce type de données est utilisé pour des drapeaux simples qui suivent les conditions vrai/faux.

La valeur par défaut est false.

Exemple : boolean b = true, boolean b1 = 1(ceci n'est pas possible en java et donne une erreur de type incompatible), boolean b2;
```

## **Types de données de référence :**

En plus des types de données primitifs, il y a des variables de référence créées en utilisant des constructeurs de différentes classes. Les variables de référence sont utilisées pour toute classe ainsi que pour les tableaux, String, Scanner, Random, Die, etc. Les variables de référence sont initialisées en utilisant le mot-clé new.

Exemple :

```java
public class Box{

    int length, breadth, height;

    public Box(){
        length=5;
        breadth=3;
        height=2;
    }
}

class demo{

    public static void main(String args[]) {
        Box box1 = new Box();                //box1 est la variable de référence  
        char[] arr = new char[10];           //arr est la variable de référence
    }
}
```

## **String :**

String n'est pas un type de données primitif, mais il vous permet de stocker plusieurs types de données de caractères dans un tableau et possède de nombreuses méthodes qui peuvent être utilisées. Il est utilisé assez couramment lorsque l'utilisateur tape des données et que vous devez les manipuler.

Dans l'exemple ci-dessous, nous essayons de supprimer toutes les lettres de la chaîne et de l'afficher :

```java
String input = "My birthday is 10 January 1984 and my favorite number is 42";
String output = "";

for(int i=0;i<input.length();i++){

//si le caractère à l'index i de la chaîne est une lettre ou un espace, passez à l'index suivant
if(Character.isLetter(input.charAt(i)) || input.charAt(i)==' '){ 
    
    continue;
}

output = output + input.charAt(i); //le nombre est ajouté à la sortie

}

System.out.println(output);
```

Sortie :

```text
10198442
```

## Plus d'informations sur Java :

* [Java pour les débutants absolus (cours vidéo complet)](https://www.freecodecamp.org/news/java-for-absolute-beginners-full-course/)
* [Les bases du langage de programmation Java](https://www.freecodecamp.org/news/java-programming-language-basics/)
* [Les meilleurs exemples Java](https://www.freecodecamp.org/news/java-example/)
* [Les meilleurs tutoriels Java 8](https://www.freecodecamp.org/news/best-java-8-tutorial/)
* [L'héritage en Java expliqué](https://www.freecodecamp.org/news/inheritance-in-java-explained/)
* [Modificateurs d'accès Java](https://guide.freecodecamp.org/java/access-modifiers/)