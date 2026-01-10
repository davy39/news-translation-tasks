---
title: Types de données Java et variables – Expliqué pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T16:59:18.000Z'
originalURL: https://freecodecamp.org/news/java-data-types-and-variables
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/data-types-and-variables.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Java
  slug: java
seo_title: Types de données Java et variables – Expliqué pour les débutants
seo_desc: "By Jacob Isah \nAs a beginner learning Java, one of the fundamental topics\
  \ you'll need to understand is data types. \nEvery day in the life of every software\
  \ engineer is about how to manipulate data, how to get data from users, the format\
  \ of the data, ..."
---

Par Jacob Isah

En tant que débutant apprenant Java, l'un des sujets fondamentaux que vous devrez comprendre est les types de données.

Chaque jour dans la vie de chaque ingénieur logiciel concerne la manipulation des données, comment obtenir des données des utilisateurs, le format des données, et comment ces données sont stockées et gérées.

Java est un langage de programmation populaire connu pour son système de typage fort, ce qui signifie que chaque variable doit avoir un type déclaré. Java fournit une large gamme de types de données pour accommoder divers types de données et d'opérations.

Dans cet article, je vais vous guider à travers les types de données de Java et expliquer comment ils fonctionnent.

Il existe deux types de types de données en Java – les types de données primitifs et les types de données de référence. Plongeons-nous et apprenons-en plus sur chacun.

## Différences entre les types de données primitifs et les types de données de référence

En Java, il existe des différences importantes entre les types de données de référence et les types de données primitifs.

Les types de données primitifs stockent la valeur réelle directement en mémoire, tandis que les types de données de référence stockent des références ou des adresses mémoire qui pointent vers l'emplacement où l'objet est stocké.

Les types de données primitifs ont des valeurs par défaut si elles ne sont pas explicitement initialisées, tandis que les types de données de référence sont par défaut `null`.

Les types de données primitifs ont des tailles fixes définies par le langage, tandis que les types de données de référence ont une taille fixe, indépendamment de l'objet auquel ils font référence.

Les opérations sur les types de données primitifs peuvent être effectuées directement, tandis que les opérations sur les types de données de référence ne peuvent être effectuées que par les méthodes fournies par l'objet.

Les types de données primitifs ont des classes d'emballage correspondantes, tandis que les types de données de référence n'en ont pas.

Lors du passage d'un type de données primitif en tant qu'argument de méthode, une copie de la valeur est passée, tandis que le passage d'un type de données de référence passe la référence par valeur.

Ces différences montrent à quel point le stockage, les valeurs par défaut, la taille, les opérations et la sémantique de passage par valeur entre les types de données de référence et les types de données primitifs fonctionnent en Java.

### Types de données primitifs en Java

Java dispose de huit types de données primitifs, qui sont les blocs de construction les plus basiques pour stocker des données. Ces types servent de blocs de construction de la manipulation des données en Java.

Les types de données primitifs servent un seul but — contenir des valeurs pures et simples d'un certain type. Ils sont des mots-clés réservés en Java. Parce qu'ils sont des mots-clés, ils ne peuvent pas être utilisés comme noms de variables. Ils incluent les éléments suivants :

#### Byte

Imaginez que vous avez une petite boîte qui peut contenir des nombres. Cette boîte peut contenir des nombres de -128 à 127. C'est comme une boîte à jouets qui ne peut contenir qu'une certaine plage de jouets, de -128 à 127. Vous pouvez mettre n'importe quel nombre de cette plage à l'intérieur de la boîte.

Le type de données `byte` est un entier signé sur 8 bits qui peut contenir des valeurs de -128 à 127. Il est couramment utilisé lorsque l'espace mémoire est une préoccupation. Créons une variable de type `byte` :

```java
byte myByte = 100;
System.out.println("byte: " + myByte);
```

```java
Sortie
byte: 100
```

#### Short

Maintenant, imaginez que vous avez une boîte plus grande. Cette boîte peut contenir le type de données `short` qui est un entier signé sur 16 bits qui peut contenir des valeurs de -32 768 à 32 767. Il est utile pour stocker des valeurs entières plus grandes que le type de données `byte`.

```java
short myShort = 30000;
System.out.println("short: " + myShort);
```

```java
Sortie :
short: 30000
```

#### Int

Maintenant, pensons à un conteneur de stockage plus grand. La boîte est un type de données `int` qui est un entier signé sur 32 bits qui peut contenir des nombres de -2 147 483 648 à 2 147 483 647. C'est comme une grande boîte à trésors qui peut contenir une large gamme de nombres, positifs et négatifs. C'est le type de données le plus couramment utilisé pour représenter des nombres entiers en Java.

```java
int myInt = 2000000000;
System.out.println("int: " + myInt);
```

```java
Sortie ::
int: 2000000000
```

#### Long

D'accord, maintenant nous avons une énorme salle de stockage. Cette salle peut contenir des nombres de -9 223 372 036 854 775 808 à 9 223 372 036 854 775 807. C'est comme avoir un entrepôt massif qui peut stocker une gamme gigantesque de nombres. Il est utilisé lorsqu'une plage plus large de valeurs entières est requise.

```java
long myLong = 9223372036854775807L;
System.out.println("long: " + myLong);
```

```java
Sortie ::
long: 9223372036854775807
```

#### Float

Imaginez que vous avez une boîte spéciale qui peut contenir des nombres décimaux. Cette boîte peut contenir des nombres décimaux avec une précision modérée. C'est comme un conteneur qui peut contenir de l'eau avec une quantité raisonnable de précision.

Le type de données `float` est un nombre à virgule flottante de précision simple sur 32 bits. Il est utile pour représenter des nombres décimaux avec une précision modérée.

```java
float myFloat = 3.14f;
System.out.println("float: " + myFloat);
```

```java
Sortie ::
float: 3.14
```

#### Double

Le type de données `double` est un nombre à virgule flottante de précision double sur 64 bits. Il offre une précision plus élevée que float et est couramment utilisé pour les calculs impliquant des nombres décimaux.

```java
double myDouble = 129.7;
System.out.println("double: " + myDouble);
```

```java
Sortie ::
double: 129.7
```

#### Boolean

Le type de données `boolean` représente une valeur `boolean`, qui peut être soit vraie soit fausse. Il est utilisé pour les opérations logiques et le contrôle de flux.

```java
boolean isJavaFun = true;
boolean isProgrammingFun = false;

System.out.println(isJavaFun);
System.out.println(isProgrammingFun);
```

```java
Sortie ::
true
false
```

#### Char

Le type de données `char` représente un seul caractère Unicode et est de 16 bits en taille. Il peut stocker n'importe quel caractère de l'ensemble de caractères Unicode.

```java
char johnGrade = 'B';
System.out.println(johnGrade);
```

```java
Sortie ::
B
```

### Types de données de référence en Java

En plus des types de données primitifs, les types de données de référence sont utilisés pour stocker des références ou des adresses mémoire qui pointent vers des objets stockés en mémoire.

Ces types de données ne stockent pas réellement les données elles-mêmes mais plutôt une référence à l'emplacement mémoire où les données sont stockées. Regardons quelques types populaires de données de référence maintenant.

#### Strings

La classe `String` représente une séquence de caractères. Elle est largement utilisée pour manipuler et stocker des données textuelles.

```java
String name = "John Doe";
System.out.println("Name: " + name);
```

```java
Sortie ::
Name: John Doe
```

#### Arrays

Les `Arrays` sont utilisés pour stocker une collection d'éléments du même type. Ils fournissent un moyen pratique de travailler avec des groupes de valeurs liées.

```java
int[] numbers = {1, 2, 3, 4, 5};
System.out.println("Numbers: " + java.util.Arrays.toString(numbers));
```

```java
Sortie ::
Numbers: [1, 2, 3, 4, 5]
```

#### Classes

Le type de données `class` représente une `class` en Java. Il est utilisé pour créer des objets et définir leur comportement.

Pour comprendre comment les classes fonctionnent en Java, nous allons créer un exemple de classe et implémenter la classe dans la classe principale.

Dans l'exemple suivant, nous allons créer une classe `Car` qui représente une voiture avec des attributs de couleur et de vitesse. Nous aurons un constructeur pour initialiser la couleur et la vitesse sera définie à 0 par défaut. La classe inclura également des méthodes pour accélérer la voiture et freiner la voiture.

Voici un exemple :

```java
public class ClassCarExample {
    // Variables d'instance ou champs
    String color;
    int speed;

    // Méthode start qui démarre la voiture
    public void start() {
        System.out.println("La voiture a démarré.");
    }

    // Méthode accelerate qui augmente la vitesse de la voiture de 10 km/h
    public void accelerate() {
        speed += 10;
        System.out.println("La voiture accélère. Vitesse actuelle : " + speed + " km/h");
    }

    // Méthode brake qui réduit la vitesse de la voiture de 5 à chaque fois que la méthode est appelée
    public void brake() {
        speed -= 5;
        System.out.println("La voiture freine. Vitesse actuelle : " + speed + " km/h");
    }
}
```

Nous allons maintenant créer la méthode principale où nous allons exécuter notre classe et faire démarrer notre voiture, accélérer et freiner.

```java
public class Main {
    public static void main(String[] args) {
        // Créer une instance de ClassCarExample
        ClassCarExample car = new ClassCarExample();

        // Démarrer la voiture
        car.start();

        // Accélérer la voiture
        car.accelerate();

        // Freiner la voiture
        car.brake();
    }
}
```

```java
Sortie :
La voiture a démarré.
La voiture accélère. Vitesse actuelle : 10 km/h
La voiture freine. Vitesse actuelle : 5 km/h
```

#### Interfaces

Le mot-clé `interface` est utilisé pour déclarer une `interface`. Une abstraction totale (masquage) est offerte, ce qui signifie que toutes les méthodes dans une `interface` sont déclarées avec un corps vide et que tous les champs sont par défaut `public`, `static` et `final`.

Toutes les méthodes déclarées dans une `interface` doivent être implémentées par une `class` qui implémente l'`interface`.

Pour mieux comprendre comment fonctionne une interface, nous allons créer une classe d'interface appelée `MyInterfaceClass` qui déclare trois méthodes : `methodExampleOne()`, `methodExampleTwo()` et `methodExampleThree()` :

```java
// La classe d'interface
interface MyInterfaceClass {
    void methodExampleOne();
    void methodExampleTwo();
    void methodExampleThree();
}
```

Maintenant, nous avons besoin d'une classe qui implémente la classe d'interface. Nous allons créer une classe `MyClass` qui implémente l'interface `MyInterfaceClass` et fournit l'implémentation pour les trois méthodes créées ci-dessus.

```java
// Implémenter l'interface dans une classe
class MyClass implements MyInterfaceClass {
    public void methodExampleOne() {
        System.out.println("Implémentation de methodExampleOne");
    }

    public void methodExampleTwo() {
        System.out.println("Implémentation de methodExampleTwo");
    }

    public void methodExampleThree() {
        System.out.println("Implémentation de methodExampleThree");
    }
}
```

Pour mieux illustrer cela, créons une méthode principale où nous pouvons créer un objet de notre `MyClass` et appeler nos méthodes sur l'objet `myObj` que nous allons créer et exécuter notre programme Java.

```java
// Classe principale pour tester l'implémentation
public class Main {
    public static void main(String[] args) {

        // Créer myObj à partir de MyClass
        MyClass myObj = new MyClass();

        // Appeler les méthodes implémentées sur l'objet que nous avons créé.
        myObj.methodExampleOne();
        myObj.methodExampleTwo();
        myObj.methodExampleThree();
    }
}
```

Lorsque nous exécutons la classe `Main`, nous verrons la sortie suivante :

```java
Sortie :
Implémentation de methodExampleOne
Implémentation de methodExampleTwo
Implémentation de methodExampleThree
```

#### Enums

Le type de données `Enum` représente un type d'énumération (liste). Il est utilisé pour définir un ensemble fixe de valeurs nommées, telles que les jours de la semaine ou les couleurs.

```java
class EnumClassExample {
    // Définition de l'énumération à l'intérieur de la classe
    public enum Weekdays {
        SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
    }

    // Méthode principale
    public static void main(String[] args) {

        // Boucle à travers l'énumération

        for (Weekdays w : Weekdays.values())
            System.out.println(w);
    }
}
```

```java
Sortie ::
SUNDAY
MONDAY
TUESDAY
WEDNESDAY
THURSDAY
FRIDAY
SATURDAY
```

## Conclusion

Comprendre les types de données Java est crucial pour une programmation efficace en Java. Qu'il s'agisse des types de données primitifs pour le stockage de valeurs de base ou des types de données de référence pour les objets et comportements complexes, chaque type de données sert un but spécifique.

En utilisant les types de données appropriés, les ingénieurs logiciels peuvent écrire un code plus efficace, fiable et maintenable en Java.

Vos commentaires sont grandement appréciés. Vous pouvez me suivre sur [Twitter](https://twitter.com/IsahJakub) et [LinkedIn](https://www.linkedin.com/in/isahejacob/).