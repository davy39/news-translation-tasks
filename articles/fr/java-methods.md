---
title: Méthodes en Java – Expliquées avec des Exemples de Code
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2024-02-29T20:05:17.000Z'
originalURL: https://freecodecamp.org/news/java-methods
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-divinetechygirl-1181298.jpg
tags:
- name: Java
  slug: java
seo_title: Méthodes en Java – Expliquées avec des Exemples de Code
seo_desc: "Methods are essential for organizing Java projects, encouraging code reuse,\
  \ and improving overall code structure. \nIn this article, we will look at what\
  \ Java methods are and how they work, including their syntax, types, and examples.\n\
  Here's what we'l..."
---

Les méthodes sont essentielles pour organiser les projets Java, encourager la réutilisation du code et améliorer la structure globale du code. 

Dans cet article, nous allons examiner ce que sont les méthodes Java et comment elles fonctionnent, y compris leur syntaxe, leurs types et des exemples.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce que les méthodes Java ?](#heading-quest-ce-que-les-methodes-java)
2. [Types de spécificateurs d'accès en Java](#heading-types-de-specificateurs-dacces-en-java)  
– [Public (`public`)](#heading-public-public)  
– [Privé (`private`)](#heading-prive-private)  
– [Protégé (`protected`)](#heading-protege-protected)  
– [Par défaut (`Package-Private`)](#heading-par-defaut-package-private)
3. [Types de méthodes](#heading-types-de-methodes)  
– [Prédéfinies vs. Définies par l'utilisateur](#heading-1-predefinies-vs-definies-par-lutilisateur)  
– [Basées sur la fonctionnalité](#heading-2-basees-sur-la-fonctionnalite)
4. [Conclusion](#heading-conclusion)

## Qu'est-ce que les méthodes Java ?

En Java, une méthode est un ensemble d'instructions qui effectuent une certaine action et sont déclarées au sein d'une classe. 

Voici la syntaxe fondamentale pour une méthode Java :

```java
acessSpecifier returnType methodName(parameterType1 parameterName1, parameterType2 parameterName2, ...) {
    // Corps de la méthode - instructions pour effectuer une tâche spécifique
    // Instruction de retour (si applicable)
}

```

Décomposons les composants :

* **`accessSpecifier`** : définit la visibilité ou l'accessibilité des classes, méthodes et champs au sein d'un programme.
* **`returnType`** : le type de données de la valeur que la méthode retourne. Si la méthode ne retourne aucune valeur, le mot-clé `void` est utilisé.
* **`methodName`** : le nom de la méthode, suivant les conventions de nommage Java.
* **`parameter`** : valeur d'entrée que la méthode accepte. Ceux-ci sont optionnels, et une méthode peut avoir zéro ou plusieurs paramètres. Chaque paramètre est déclaré avec son type de données et un nom.
* **corps de la méthode** : l'ensemble des instructions enfermées dans des accolades `{}` qui définissent la tâche que la méthode effectue.
* **instruction de retour** : si la méthode a un type de retour autre que `void`, elle doit inclure une instruction `return` suivie de la valeur à retourner.

Voici un exemple de méthode Java simple :

```java
public class SimpleMethodExample {

    // Méthode qui prend deux entiers et retourne leur somme
    public static int addNumbers(int a, int b) {
        int sum = a + b;
        return sum;
    }

    public static void main(String[] args) {
        // Appel de la méthode et stockage du résultat
        int result = addNumbers(5, 7);

        // Affichage du résultat
        System.out.println("La somme est : " + result);
    }
}

```

Dans cet exemple, la méthode `addNumbers` prend deux entiers comme paramètres (`a` et `b`), calcule leur somme et retourne le résultat. La méthode `main` appelle ensuite cette méthode et affiche le résultat.

Compilez le code Java en utilisant le terminal, en utilisant la commande `javac` :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-28-09-27-12.png)
_Sortie_

Les méthodes facilitent la réutilisation du code en encapsulant la fonctionnalité dans un seul bloc. Vous pouvez appeler ce bloc depuis différentes parties de votre programme, évitant la duplication de code et favorisant la maintenabilité.

## Types de spécificateurs d'accès en Java

Les spécificateurs d'accès contrôlent la visibilité et l'accessibilité des membres de classe (champs, méthodes et classes imbriquées). 

Il existe généralement quatre principaux types de spécificateurs d'accès : public, privé, protégé et par défaut. Ils dictent où et comment ces membres peuvent être accessibles, favorisant l'encapsulation et la modularité.

### Public (`public`)

Cela accorde l'accès au membre depuis **n'importe où** dans votre programme, indépendamment du package ou de la classe. Il est adapté pour les composants largement utilisés comme les fonctions utilitaires ou les constantes.

**Syntaxe :**

```java
public class MyClass {
    public int publicField;
    public void publicMethod() {
        // implémentation de la méthode
    }
}

```

**Exemple :**

```java
// Fichier : MyClass.java

// Une classe avec le spécificateur d'accès public
public class MyClass {
    
    // Champ public
    public int publicField = 10;

    // Méthode publique
    public void publicMethod() {
        System.out.println("Ceci est une méthode publique.");
    }

    // Méthode principale pour exécuter le programme
    public static void main(String[] args) {
        // Création d'un objet de MyClass
        MyClass myObject = new MyClass();

        // Accès au champ public
        System.out.println("Champ Public : " + myObject.publicField);

        // Appel de la méthode publique
        myObject.publicMethod();
    }
}

```

Dans cet exemple :

* La classe `MyClass` est déclarée avec le modificateur `public`, la rendant accessible depuis n'importe quelle autre classe.
* Le `publicField` est un champ public qui peut être accessible depuis l'extérieur de la classe.
* La `publicMethod()` est une méthode publique qui peut être appelée depuis l'extérieur de la classe.
* La méthode `main` est le point d'entrée du programme, où un objet de `MyClass` est créé, et le champ public et la méthode sont accessibles.

```output
Champ Public : 10
Ceci est une méthode publique.
```

### Privé (`private`)

Cela confine l'accès au membre **au sein de la classe** où il est déclaré. Il protège les données sensibles et impose l'encapsulation.

**Syntaxe :**

```java
public class MyClass {
    private int privateField;
    private void privateMethod() {
        // implémentation de la méthode
    }
}

```

**Exemple :**

```
// Fichier : MyClass.java

// Une classe avec le spécificateur d'accès privé
public class MyClass {
    
    // Champ privé
    private int privateField = 10;

    // Méthode privée
    private void privateMethod() {
        System.out.println("Ceci est une méthode privée.");
    }

    // Méthode publique pour accéder aux membres privés
    public void accessPrivateMembers() {
        // Accès au champ privé
        System.out.println("Champ Privé : " + privateField);

        // Appel de la méthode privée
        privateMethod();
    }

    // Méthode principale pour exécuter le programme
    public static void main(String[] args) {
        // Création d'un objet de MyClass
        MyClass myObject = new MyClass();

        // Accès aux membres privés via une méthode publique
        myObject.accessPrivateMembers();
    }
}

```

Dans cet exemple :

* La classe `MyClass` a un `privateField` et une `privateMethod`, tous deux marqués avec le modificateur `private`.
* La méthode `accessPrivateMembers()` est une méthode publique qui peut être appelée depuis l'extérieur de la classe. Elle fournit l'accès au champ privé et appelle la méthode privée.

```output
Champ Privé : 10
Ceci est une méthode privée.

```

### Protégé (`protected`)

Le spécificateur d'accès `protected` est utilisé pour rendre les membres (champs et méthodes) accessibles au sein du même package ou par les sous-classes, indépendamment du package. Ils ne sont pas accessibles depuis des classes non apparentées. Il facilite l'héritage tout en contrôlant l'accès à des membres spécifiques dans les sous-classes.

**Syntaxe :**

```java
public class MyClass {
    protected int protectedField;
    protected void protectedMethod() {
        // implémentation de la méthode
    }
}

```

**Exemple :**

```java
// Fichier : Animal.java

// Une classe avec le spécificateur d'accès protégé
public class Animal {
    
    // Champ protégé
    protected String species = "Unknown"; // Initialisation avec une valeur par défaut

    // Méthode protégée
    protected void makeSound() {
        System.out.println("Un son générique d'animal");
    }
}

```

```java
// Fichier : Dog.java

// Une sous-classe de Animal
public class Dog extends Animal {

    // Méthode publique pour accéder aux membres protégés
    public void displayInfo() {
        // Accès au champ protégé de la superclasse
        System.out.println("Espèce : " + species);

        // Appel de la méthode protégée de la superclasse
        makeSound();
    }
}

```

```java
// Fichier : Main.java

// Classe principale pour exécuter le programme
public class Main {
    public static void main(String[] args) {
        // Création d'un objet de Dog
        Dog myDog = new Dog();

        // Accès aux membres protégés via une méthode publique
        myDog.displayInfo();
    }
}

```

Dans cet exemple :

* La classe `Animal` a un champ `protected` (`species`) et une méthode `protected` (`makeSound`).
* La classe `Dog` est une sous-classe de `Animal`, et elle peut accéder aux membres `protected` de la superclasse.
* La méthode `displayInfo()` dans la classe `Dog` accède au champ protégé et appelle la méthode protégée.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-28-10-05-27.png)
_Sortie_

Avec le spécificateur d'accès `protected`, les membres sont accessibles au sein du même package et par les sous-classes, favorisant un certain niveau de visibilité et d'héritage tout en maintenant l'encapsulation.

### Par défaut (`Package-Private`)

Si aucun spécificateur d'accès n'est utilisé, le niveau d'accès par défaut est `package-private`. Les membres avec un accès par défaut sont accessibles au sein du même package, mais pas à l'extérieur. Il est souvent utilisé pour les classes utilitaires ou les méthodes auxiliaires au sein d'un module spécifique.

**Syntaxe :**

```java
class MyClass {
    int defaultField;
    void defaultMethod() {
        // implémentation de la méthode
    }
}

```

**Exemple :**

```java
// Fichier : Animal.java

// Une classe avec le spécificateur d'accès par défaut (package-private)
class Animal {
    String species = "Unknown";

    void makeSound() {
        System.out.println("Un son générique d'animal");
    }
}

```

```java
// Fichier : Main.java

// Classe principale pour exécuter le programme
public class Main {
    public static void main(String[] args) {
        // Création d'un objet de Dog
        Dog myDog = new Dog();

        // Accès aux membres par défaut (package-private) via une méthode publique
        myDog.displayInfo();
    }
}

```

```java
// Fichier : Dog.java

// Une autre classe dans le même package
public class Dog {
    Animal myAnimal = new Animal();

    void displayInfo() {
        // Accès au champ par défaut (package-private) et à la méthode
        System.out.println("Espèce : " + myAnimal.species);
        myAnimal.makeSound();
    }
}

```

Dans cet exemple :

* La classe `Animal` n'a aucun modificateur d'accès spécifié, la rendant par défaut (package-private). Elle a un champ package-private `species` et une méthode package-private `makeSound`.
* La classe `Dog` est dans le même package que `Animal`, donc elle peut accéder aux membres par défaut (package-private) de la classe `Animal`.
* La classe `Main` exécute le programme en créant un objet de `Dog` et en appelant sa méthode `displayInfo`.

Lorsque vous exécutez ce programme, il devrait afficher l'espèce et le son de l'animal. 

### Comment choisir le bon spécificateur d'accès

* **Public** : Utilisez pour les composants largement utilisés, les interfaces et les classes de base.
* **Privé** : Utilisez pour les détails d'implémentation interne et la protection des données sensibles.
* **Par défaut** : Utilisez pour les méthodes auxiliaires ou les composants spécifiques à un package.
* **Protégé** : Utilisez pour la fonctionnalité partagée parmi les sous-classes, tout en restreignant l'accès depuis l'extérieur de la hiérarchie d'héritage.

## **Types de méthodes**

En Java, les méthodes peuvent être catégorisées de deux manières principales :

### 1. Prédéfinies vs. Définies par l'utilisateur :

**Méthodes prédéfinies** : Ces méthodes sont déjà définies dans la bibliothèque de classes Java et peuvent être utilisées directement sans aucune déclaration. 

Les exemples incluent `System.out.println()` pour afficher dans la console et `Math.max()` pour trouver le maximum de deux nombres.

**Méthodes définies par l'utilisateur** : Ce sont des méthodes que vous écrivez vous-même pour effectuer des tâches spécifiques au sein de votre programme. Elles sont définies au sein de classes et sont généralement utilisées pour encapsuler la fonctionnalité et améliorer la réutilisation du code.

```java
public class RectangleAreaCalculator {

    // Méthode définie par l'utilisateur pour calculer l'aire d'un rectangle
    public static double calculateRectangleArea(double length, double width) {
        double area = length * width;
        return area;
    }

    public static void main(String[] args) {
        // Exemple d'utilisation de la méthode
        double length = 5.0;
        double width = 3.0;
        
        // Appel de la méthode
        double result = calculateRectangleArea(length, width);

        // Affichage du résultat
        System.out.println("L'aire du rectangle avec une longueur " + length + " et une largeur " + width + " est : " + result);
    }
}

```

Dans cet exemple :

* `add` est une méthode définie par l'utilisateur car elle est créée par l'utilisateur (programmeur).
* La méthode prend deux paramètres (`num1` et `num2`) et retourne leur somme.
* La méthode `main` appelle la méthode `add` avec des valeurs spécifiques, démontrant la fonctionnalité personnalisée fournie par l'utilisateur.

### 2. Basées sur la fonctionnalité :

Au sein des méthodes définies par l'utilisateur, il existe plusieurs autres classifications basées sur leurs caractéristiques :

### Méthodes d'instance : 

Associées à une instance d'une classe. Elles peuvent accéder aux variables d'instance et sont appelées sur un objet de la classe.

Voici quelques caractéristiques clés des méthodes d'instance :

**Accès aux variables d'instance :**

* Les méthodes d'instance ont accès aux variables d'instance (également connues sous le nom de champs ou propriétés) de la classe.
* Elles peuvent manipuler l'état de l'objet auquel elles appartiennent.

**Utilisation du mot-clé `this` :**

* À l'intérieur d'une méthode d'instance, le mot-clé `this` fait référence à l'instance actuelle de la classe. Il est souvent utilisé pour différencier les variables d'instance et les paramètres ayant le même nom.

**Contexte non statique :**

* Les méthodes d'instance sont appelées dans le contexte d'un objet. Elles ne peuvent pas être appelées sans créer une instance de la classe.

**Déclaration et invocation :**

* Les méthodes d'instance sont déclarées sans le mot-clé `static`.
* Elles sont invoquées sur une instance de la classe en utilisant la notation par point (`.`).

Voici un exemple simple en Java pour illustrer les méthodes d'instance :

**Exemple :**

```
public class Dog {
    // Variables d'instance
    String name;
    int age;

    // Constructeur pour initialiser les variables d'instance
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Méthode d'instance pour aboyer
    public void bark() {
        System.out.println(name + " dit Woof !");
    }

    // Méthode d'instance pour vieillir le chien
    public void ageOneYear() {
        age++;
        System.out.println(name + " a maintenant " + age + " ans.");
    }

    public static void main(String[] args) {
        // Création d'instances de la classe Dog
        Dog myDog = new Dog("Buddy", 3);
        Dog anotherDog = new Dog("Max", 2);

        // Appel des méthodes d'instance sur les objets
        myDog.bark();
        myDog.ageOneYear();

        anotherDog.bark();
        anotherDog.ageOneYear();
    }
}

```

Dans cet exemple :

* `bark` et `ageOneYear` sont des méthodes d'instance de la classe `Dog`.
* Elles sont invoquées sur des instances de la classe `Dog` (`myDog` et `anotherDog`).
* Ces méthodes peuvent accéder et manipuler les variables d'instance (`name` et `age`) des objets respectifs.

Les méthodes d'instance sont puissantes car elles permettent d'encapsuler le comportement lié à l'état d'un objet et fournissent un moyen d'interagir avec et de modifier cet état.

### Méthodes statiques : 

Une méthode statique appartient à la classe plutôt qu'à une instance de la classe. Cela signifie que vous pouvez appeler une méthode statique sans créer une instance (objet) de la classe. Elle est déclarée en utilisant le mot-clé `static`.

Les méthodes statiques sont couramment utilisées pour les fonctions utilitaires qui ne dépendent pas de l'état d'un objet. Par exemple, des méthodes pour les calculs mathématiques, les manipulations de chaînes, etc.

**Exemple :**

```java
public class MathOperations {
    // Méthode statique
    public static int add(int a, int b) {
        return a + b;
    }

    // Méthode statique
    public static int multiply(int a, int b) {
        return a * b;
    }
}

```

### Méthodes abstraites :

Ces méthodes sont déclarées mais non implémentées dans une classe. Elles sont destinées à être redéfinies par les sous-classes, fournissant un plan pour une fonctionnalité spécifique qui doit être implémentée dans chaque sous-classe.

Les méthodes abstraites sont utiles lorsque vous souhaitez définir un modèle dans une classe de base ou une interface, laissant l'implémentation spécifique aux sous-classes. Les méthodes abstraites définissent un contrat que les sous-classes doivent suivre.

**Exemple :**

```
public abstract class Shape {
    // Méthode abstraite
    abstract double calculateArea();
}

```

  
**Autres types de méthodes :** En outre, il existe des types moins courants comme les constructeurs utilisés pour l'initialisation des objets, les méthodes d'accès (getters) pour récupérer les données des objets, et les méthodes de mutation (setters) pour modifier les données des objets.

## Conclusion

Les méthodes sont essentielles pour organiser les projets Java, encourager la réutilisation du code et améliorer la structure globale du code. 

Dans cet article, nous avons examiné les méthodes Java, y compris leur syntaxe, leurs types et les pratiques recommandées.

Bon codage !