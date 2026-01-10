---
title: Programmation Orientée Objet en Java – Guide du Débutant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-18T22:03:31.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-concepts-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/ian-dooley-DJ7bWa-Gwks-unsplash-2-2.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Programmation Orientée Objet en Java – Guide du Débutant
seo_desc: "By Patrick Cyubahiro\nHi, folks! Today we are going to talk about object-oriented\
  \ programming in Java.\nThis article will help give you a thorough understanding\
  \ of the underlying principles of object-oriented programming and its concepts.\
  \ \nOnce you und..."
---

Par Patrick Cyubahiro

Salut, les amis ! Aujourd'hui, nous allons parler de la programmation orientée objet en Java.

Cet article vous aidera à comprendre en profondeur les principes sous-jacents de la programmation orientée objet et ses concepts.

Une fois que vous comprendrez ces concepts, vous devriez avoir la confiance et la capacité de développer des applications de résolution de problèmes de base en utilisant les principes de la programmation orientée objet en Java.

## Qu'est-ce que la Programmation Orientée Objet ?

La programmation orientée objet (POO) est un paradigme de programmation fondamental basé sur le concept d'« objets ». Ces objets peuvent contenir des données sous forme de champs (souvent appelés attributs ou propriétés) et du code sous forme de procédures (souvent appelées méthodes).

Le concept central de l'approche orientée objet est de décomposer des problèmes complexes en objets plus petits.

**Dans cet article, nous allons examiner les concepts suivants de la POO :**

1. Qu'est-ce que Java ?
2. Qu'est-ce qu'une classe ?
3. Qu'est-ce qu'un objet ?
4. Qu'est-ce qu'une Machine Virtuelle Java (JVM) ?
5. Comment fonctionnent les modificateurs d'accès en Java.
6. Comment fonctionnent les constructeurs en Java.
7. Comment fonctionnent les méthodes en Java.
8. Principes clés de la POO.
9. Interfaces en Java.

## Qu'est-ce que Java ?

Java est un langage de programmation généraliste, basé sur les classes et orienté objet, qui fonctionne sur différents systèmes d'exploitation tels que Windows, Mac et Linux.

Vous pouvez utiliser Java pour développer :

* Applications de bureau
* Applications web
* Applications mobiles (surtout les applications Android)
* Serveurs web et d'applications
* Traitement de grandes données
* Systèmes embarqués

Et bien plus encore.

En Java, chaque application commence avec un nom de classe, et cette classe doit correspondre au nom du fichier. Lors de l'enregistrement d'un fichier, enregistrez-le en utilisant le nom de la classe et ajoutez « _.java_ » à la fin du nom du fichier.

Écrivons un programme Java qui imprime le message « _Bonjour communauté freeCodeCamp. Mon nom est ..._ ».

Nous allons commencer par créer notre premier fichier Java appelé Main.java, ce qui peut être fait dans n'importe quel éditeur de texte. Après avoir créé et enregistré le fichier, nous allons utiliser les lignes de code ci-dessous pour obtenir le résultat attendu.

```java
public class Main 
{
  public static void main(String[] args) 
  {
    System.out.println("Bonjour communauté freeCodeCamp. Mon nom est Patrick Cyubahiro.");
  }
}

```

Ne vous inquiétez pas si vous ne comprenez pas le code ci-dessus pour le moment. Nous allons discuter, étape par étape, chaque ligne de code juste en dessous.

Pour l'instant, je veux que vous commenciez par noter que chaque ligne de code qui s'exécute en Java doit être dans une classe.

Vous pouvez également noter que Java est sensible à la casse. Cela signifie que Java a la capacité de distinguer les lettres majuscules et minuscules. Par exemple, la variable « _myClass_ » et la variable « _myclass_ » sont deux choses totalement différentes.

**D'accord, voyons ce que fait ce code :**

Regardons d'abord la méthode `main()` : `public static void main(String[] args)`.

Cette méthode est requise dans chaque programme Java, et c'est la plus importante car c'est le point d'entrée de tout programme Java.

Sa syntaxe est toujours `public static void main(String[] args)`. La seule chose qui peut être changée est le nom de l'argument du tableau de chaînes. Par exemple, vous pouvez changer `args` en `myStringArgs`.

## Qu'est-ce qu'une Classe en Java ?

Une classe est définie comme une collection d'objets. Vous pouvez également penser à une classe comme un plan à partir duquel vous pouvez créer un objet individuel.

Pour créer une classe, nous utilisons le mot-clé `class`.

### Syntaxe d'une classe en Java :

```java
class NomDeClasse {
  // champs
  // méthodes
}
```

Dans la syntaxe ci-dessus, nous avons des champs (également appelés variables) et des méthodes, qui représentent respectivement l'état et le comportement de l'objet.

**Notez** qu'en Java, nous utilisons des champs pour stocker des données, tandis que nous utilisons des méthodes pour effectuer des opérations.

### Prenons un exemple :

Nous allons créer une classe nommée « _Main_ » avec une variable « _y_ ». La variable « _y_ » va stocker la valeur 2.

```java
public class Main { 

int y = 2; 

}
```

Notez qu'une classe doit toujours commencer par une lettre majuscule, et que le fichier Java doit correspondre au nom de la classe.

## Qu'est-ce qu'un Objet en Java ?

Un objet est une entité du monde réel qui peut être distinctement identifiée. Les objets ont des états et des comportements. En d'autres termes, ils se composent de méthodes et de propriétés pour rendre un type particulier de données utile.

Un objet se compose de :

* **Une identité unique :** Chaque objet a une identité unique, même si l'état est identique à celui d'un autre objet.
* **État/Propriétés/Attributs :** L'état nous indique comment l'objet apparaît ou quelles propriétés il possède.
* **Comportement :** Le comportement nous indique ce que fait l'objet.

### Exemples d'états et de comportements d'objets en Java :

Regardons quelques exemples concrets des états et comportements que les objets peuvent avoir.

#### Exemple 1 :

* Objet : voiture.
* État : couleur, marque, poids, modèle.
* Comportement : freiner, accélérer, tourner, changer de vitesse.

#### Exemple 2 :

* Objet : maison.
* État : adresse, couleur, emplacement.
* Comportement : ouvrir la porte, fermer la porte, ouvrir les stores.

### Syntaxe d'un objet en Java :

```java
public class Nombre {

int y = 10;

public static void main(String[] args) {

Nombre monObj = new Nombre();

System.out.println(monObj.y);

}

}

```

## Qu'est-ce que la Machine Virtuelle Java (JVM) ?

La machine virtuelle Java (JVM) est une machine virtuelle qui permet à un ordinateur d'exécuter des programmes Java.

La JVM a deux fonctions principales, qui sont :

* Permettre aux programmes Java de s'exécuter sur n'importe quel appareil ou système d'exploitation (c'est aussi ce qu'on appelle le principe « Write once, run anywhere »).
* Et, gérer et optimiser la mémoire du programme.

## Comment fonctionnent les Modificateurs d'Accès en Java

En Java, les modificateurs d'accès sont des mots-clés qui définissent l'accessibilité des classes, méthodes et autres membres.

Ces mots-clés déterminent si un champ ou une méthode dans une classe peut être utilisé ou invoqué par une autre méthode dans une autre classe ou sous-classe.

Les modificateurs d'accès peuvent également être utilisés pour restreindre l'accès.

En Java, nous avons quatre types de modificateurs d'accès, qui sont :

* Par défaut
* Public
* Privé
* Protégé

Regardons chacun d'eux plus en détail maintenant.

### Modificateur d'Accès par Défaut

Le **modificateur d'accès par défaut** est également appelé package-private. Vous l'utilisez pour rendre tous les membres au sein du même package visibles, mais ils ne peuvent être accessibles qu'au sein du même package.

Notez que lorsqu'aucun modificateur d'accès n'est spécifié ou déclaré pour une classe, une méthode ou un membre de données, il prend automatiquement le modificateur d'accès par défaut.

Voici un exemple de la façon dont vous pouvez utiliser le modificateur d'accès par défaut :

```java
class SampleClass 
{
    void output() 
       { 
           System.out.println("Bonjour le monde ! Voici une introduction à la POO - Guide du débutant."); 
       } 
} 
class Main
{ 
    public static void main(String args[]) 
       {   
          SampleClass obj = new SampleClass(); 
          obj.output();  
       } 
}
```

**Maintenant, voyons ce que fait ce code :**

`void output()` : Lorsqu'il n'y a pas de modificateur d'accès, le programme prend automatiquement le modificateur par défaut.

`SampleClass obj = new SampleClass();` : Cette ligne de code permet au programme d'accéder à la classe avec le modificateur d'accès par défaut.

`obj.output();` : Cette ligne de code permet au programme d'accéder à la méthode de la classe avec le modificateur d'accès par défaut.

Le résultat est : `Bonjour le monde ! Voici une introduction à la POO - Guide du débutant.`

### Modificateur d'Accès Public

Le **modificateur d'accès public** permet à une classe, une méthode ou un champ de données d'être accessible depuis n'importe quelle classe ou package dans un programme Java. Le modificateur d'accès public est accessible au sein du package ainsi qu'en dehors du package.

En général, un modificateur d'accès public ne restreint pas du tout l'entité.

Voici un exemple de la façon dont le modificateur d'accès public peut être utilisé :

```java
// Fichier Car.java
// classe publique
public class Car {
    // variable publique
    public int tireCount;

    // méthode publique
    public void display() {
        System.out.println("Je suis une voiture.");
        System.out.println("J'ai " + tireCount + " pneus.");
    }
}

// Main.java
public class Main {
    public static void main( String[] args ) {
        // accès à la classe publique
        Car car = new Car();

        // accès à la variable publique
        car.tireCount = 4;
        // accès à la méthode publique
        car.display();
    }
}
```

**Résultat :**

```java
Je suis une voiture.

J'ai 4 pneus.
```

**Maintenant, voyons ce qui se passe dans ce code :**

Dans l'exemple ci-dessus,

* La classe publique `Car` est accessible depuis la classe Main.
* La variable publique `tireCount` est accessible depuis la classe Main.
* La méthode publique `display()` est accessible depuis la classe Main.

### Modificateur d'Accès Privé

Le **modificateur d'accès privé** est un modificateur d'accès qui a le niveau d'accessibilité le plus bas. Cela signifie que les méthodes et les champs déclarés comme privés ne sont pas accessibles en dehors de la classe. Ils ne sont accessibles qu'au sein de la classe qui a ces entités privées comme membres.

Vous pouvez également noter que les entités privées ne sont pas visibles même pour les sous-classes de la classe.

Voici un exemple de ce qui se passerait si vous essayez d'accéder à des variables et méthodes déclarées privées, en dehors de la classe :

```java
class SampleClass 
{
    
    private String activity;
}

public class Main 
{

    public static void main(String[] main)
    {

        SampleClass task = new SampleClass();

        task.activity = "Nous apprenons les concepts de base de la POO.";
    }
}
```

**D'accord, que se passe-t-il ici ?**

1. `private String activity` : Le modificateur d'accès privé rend la variable « activity » privée.
2. `SampleClass task = new SampleClass();` : Nous avons créé un objet de SampleClass.
3. `task.activity = "Nous apprenons les concepts de base de la POO.";` : Sur cette ligne de code, nous essayons d'accéder à la variable et au champ privés depuis une autre classe (ce qui ne peut jamais être accessible à cause du modificateur d'accès privé).

Lorsque nous exécutons le programme ci-dessus, nous obtiendrons l'erreur suivante :

```java
Main.java:49: erreur: activity a un accès privé dans SampleClass
        task.activity = "Nous apprenons les concepts de base de la POO.";
            ^
1 erreur
```

C'est parce que nous essayons d'accéder à la variable et au champ privés depuis une autre classe.

La meilleure façon d'accéder à ces variables privées est donc d'utiliser les méthodes getter et setter.

Les getters et setters sont utilisés pour protéger vos données, en particulier lors de la création de classes. Lorsque nous créons une méthode getter pour chaque variable d'instance, la méthode retourne sa valeur tandis qu'une méthode setter définit sa valeur.

Regardons comment nous pouvons utiliser les méthodes getter et setter pour accéder à la variable privée.

```java
class SampleClass 
{

    private String task;

    // C'est la méthode getter.
    public String getTask() 
    {
    
        return this.task;
    }
    
    // C'est la méthode setter.
    public void setTask(String task) 
    {
    
        this.task= task;
    }
}

public class Main 
{

    public static void main(String[] main)
    {
    
        SampleClass task = new SampleClass();

        // Nous voulons accéder à la variable privée en utilisant le getter et le setter.
        
        task.setTask("Nous apprenons les concepts de base de la POO.");
        
        System.out.println(task.getTask());
    }
}
```

Lorsque nous exécutons le programme ci-dessus, voici le résultat :

```java
Nous apprenons les concepts de base de la POO.
```

Comme nous avons une variable privée nommée `task` dans l'exemple ci-dessus, nous avons utilisé les méthodes `getTask()` et `setTask()` afin d'accéder à la variable depuis la classe externe. Ces méthodes sont appelées getter et setter en Java.

Nous avons utilisé la méthode setter (`setTask()`) pour assigner une valeur à la variable et la méthode getter (`getTask()`) pour accéder à la variable.

Pour en savoir plus sur le mot-clé `this`, vous pouvez lire cet article [ici](https://www.programiz.com/java-programming/this-keyword).

### Modificateur d'Accès Protégé

Lorsque les méthodes et les membres de données sont déclarés `protected`, nous pouvons y accéder au sein du même package ainsi que depuis les sous-classes.

Nous pouvons également dire que le modificateur d'accès `protected` est en quelque sorte similaire au modificateur d'accès par défaut. Il a juste une exception, qui est sa visibilité dans les sous-classes.

Notez que les classes ne peuvent pas être déclarées protégées. Ce modificateur d'accès est généralement utilisé dans une relation parent-enfant.

Regardons comment nous pouvons utiliser le modificateur d'accès protégé :

```java
// Multiplication.java

package learners;

public class Multiplication 
{

   protected int multiplyTwoNumbers(int a, int b)
   {
       
	return a*b;
	
   }
   
}

// Test.java

package javalearners;

import learners.*;

class Test extends Multiplication
{
    
   public static void main(String args[])
   {
       
	Test obj = new Test();
	
	System.out.println(obj.multiplyTwoNumbers(2, 4));
	
   }
   
} //sortie: 8
```

**Que fait ce code ?**

Dans cet exemple, la classe `Test` qui est présente dans un autre package est capable d'appeler la méthode `multiplyTwoNumbers()`, qui est déclarée protégée.

La méthode est capable de le faire parce que la classe `Test` étend la classe Addition et que le modificateur `protected` permet l'accès aux membres `protected` dans les sous-classes (dans n'importe quel package).

## Qu'est-ce que les Constructeurs en Java ?

Un constructeur en Java est une méthode que vous utilisez pour initialiser des objets nouvellement créés.

### Syntaxe d'un constructeur en Java :

```java
public class Main { 

int a;  

public Main() { 

a = 3 * 3; 

} 

public static void main(String[] args) { 

Main myObj = new Main();

System.out.println(myObj.a); 

} 

} 
```

**Alors, que se passe-t-il dans ce code ?**

1. Nous avons commencé par créer la classe `Main`.
2. Après cela, nous avons créé un attribut de classe, qui est la variable `a`.
3. Troisièmement, nous avons créé un constructeur de classe pour la classe Main.
4. Après cela, nous avons défini la valeur initiale pour la variable `a` que nous avons déclarée. La variable `a` aura une valeur de 9. Notre programme prendra simplement 3 fois 3, ce qui est égal à 9. Vous êtes libre d'assigner n'importe quelle valeur à la variable `a`. (En programmation, le symbole « * » signifie multiplication).

Chaque programme Java commence son exécution dans la méthode `main()`. Donc, nous avons utilisé `public static void main(String[] args)`, et c'est le point à partir duquel le programme commence son exécution. En d'autres termes, la méthode `main()` est le point d'entrée de chaque programme Java.

Maintenant, je vais expliquer ce que fait chaque mot-clé dans la méthode `main()`.

#### Le mot-clé public.

Le mot-clé **public** est un **modificateur d'accès**. Son rôle est de spécifier d'où la méthode peut être accessible, et qui peut y accéder. Donc, lorsque nous rendons la méthode `main()` publique, elle la rend globalement disponible. En d'autres termes, elle devient accessible à toutes les parties du programme.

#### Le mot-clé static.

Lorsque une méthode est déclarée avec le mot-clé **static**, elle est connue comme une méthode statique. Donc, la méthode Java `main()` est toujours **static** afin que le compilateur puisse l'appeler sans ou avant la création d'un objet de la classe.

Si la méthode `main()` était autorisée à être non statique, alors la Machine Virtuelle Java devrait instancier sa classe lors de l'appel de la méthode `main()`.

Le mot-clé static est également important car il économise le gaspillage inutile de mémoire qui aurait été utilisé par l'objet déclaré uniquement pour appeler la méthode `main()` par la Machine Virtuelle Java.

#### Le mot-clé Void.

Le mot-clé **void** est un mot-clé utilisé pour spécifier qu'une méthode ne retourne rien. Chaque fois que la méthode `main()` n'est pas censée retourner quoi que ce soit, alors son type de retour est void. Donc, cela signifie que dès que la méthode `main()` se termine, le programme Java se termine également.

#### Main.

**Main** est le nom de la méthode principale Java. C'est l'identifiant que la Machine Virtuelle Java recherche comme point de départ du programme java.

#### Le `String[] args`.

C'est un tableau de chaînes qui stocke les arguments de ligne de commande Java.

L'étape suivante consiste à créer un objet de la classe Main. Nous avons créé un appel de fonction qui appelle le constructeur de la classe.

La dernière étape consiste à imprimer la valeur de `a`, qui est 9.

## Comment fonctionnent les Méthodes en Java

Une méthode est un bloc de code qui effectue une tâche spécifique. En Java, nous utilisons le terme méthode, mais dans certains autres langages de programmation comme C++, la même méthode est couramment appelée fonction.

En Java, il existe deux types de méthodes :

* **Méthodes définies par l'utilisateur** : Ce sont des méthodes que nous pouvons créer en fonction de nos besoins.
* **Méthodes de la bibliothèque standard** : Ce sont des méthodes intégrées en Java qui sont disponibles à l'utilisation.

Permettez-moi de vous donner un exemple de la façon dont vous pouvez utiliser des méthodes en Java.

### Exemple de méthodes Java 1 :

```java
class Main {

  // créer une méthode
  public int divideNumbers(int x, int y) {
    int division = x / y;
    // retourner la valeur
    return division;
  }

  public static void main(String[] args) {
    
    int firstNumber = 4;
    int secondNumber = 2;

    // créer un objet de Main
    Main obj = new Main();
    // appeler la méthode
    int result = obj.divideNumbers(firstNumber, secondNumber);
    System.out.println("Diviser " + firstNumber + " par " + secondNumber + " donne : " + result);
  }
}
```

**Résultat :**

```java
Diviser 4 par 2 donne : 2
```

Dans l'exemple ci-dessus, nous avons créé une méthode nommée `divideNumbers()`. La méthode prend deux paramètres x et y, et nous avons appelé la méthode en passant deux arguments `firstNumber` et `secondNumber`.

Maintenant que vous connaissez quelques bases de Java, regardons les principes de la programmation orientée objet un peu plus en profondeur.

## Principes Clés de la Programmation Orientée Objet.

Il existe quatre principes principaux du paradigme de la Programmation Orientée Objet. Ces principes sont également connus comme les piliers de la Programmation Orientée Objet.

Les quatre principes principaux de la Programmation Orientée Objet sont :

1. Encapsulation (Je vais également aborder brièvement le Masquage d'Information)
2. Héritage
3. Abstraction
4. Polymorphisme

### Encapsulation et Masquage d'Information en Java

L'encapsulation consiste à regrouper vos données sous une seule unité. En termes simples, c'est plus ou moins comme un bouclier protecteur qui empêche les données d'être accessibles par le code en dehors de ce bouclier.

Un exemple simple d'encapsulation est un sac d'école. Un sac d'école peut garder tous vos articles en sécurité en un seul endroit, comme vos livres, stylos, crayons, règle, et plus encore.

Le masquage d'information ou le masquage de données en programmation consiste à protéger les données ou les informations de tout changement inadvertant tout au long du programme. C'est une fonctionnalité puissante de la Programmation Orientée Objet, et elle est étroitement associée à l'encapsulation.

L'idée derrière l'encapsulation est de s'assurer que les données « sensibles » sont cachées aux utilisateurs. Pour y parvenir, vous devez :

1. Déclarer les variables/attributs de classe comme `private`.
2. Fournir des méthodes `get` et `set` publiques pour accéder et mettre à jour la valeur d'une variable `private`.

Comme vous vous en souvenez, les variables `private` ne peuvent être accessibles qu'au sein de la même classe et une classe externe ne peut pas y accéder. Cependant, elles peuvent être accessibles si nous fournissons des méthodes `get` et `set` publiques.

Permettez-moi de vous donner un exemple supplémentaire qui démontre comment les méthodes `get` et `set` fonctionnent :

```java
public class Student {
  private String name; // private = accès restreint

  // Getter
  public String getName() {
    return name;
  }

  // Setter
  public void setName(String newName) {
    this.name = newName;
  }
}
```

### Héritage en Java

L'héritage permet aux classes d'hériter des attributs et méthodes d'autres classes. Cela signifie que les classes parentes étendent les attributs et comportements aux classes enfants. L'héritage soutient la réutilisabilité.

Un exemple simple qui explique le terme héritage est que les êtres humains (en général) héritent de certaines propriétés de la classe « Humain » telles que la capacité de parler, respirer, manger, boire, et ainsi de suite.

Nous regroupons le « concept d'héritage » en deux catégories :

* **sous-classe** (enfant) - la classe qui hérite d'une autre classe.
* **superclasse** (parent) - la classe dont on hérite.

Pour hériter d'une classe, nous utilisons le mot-clé `extends`.

Dans l'exemple ci-dessous, la classe `JerryTheMouse` est créée en héritant des méthodes et champs de la classe `Animal`.

`JerryTheMouse` est la sous-classe et `Animal` est la superclasse.

```java
class Animal {

  // champ et méthode de la classe parente
  String name;
  public void eat() {
    System.out.println("Je peux manger");
  }
}

// héritage de Animal
class JerryTheMouse extends Animal {

  // nouvelle méthode dans la sous-classe
  public void display() {
    System.out.println("Mon nom est " + name);
  }
}

class Main {
  public static void main(String[] args) {

    // créer un objet de la sous-classe
    JerryTheMouse labrador = new JerryTheMouse();

    // accès au champ de la superclasse
    mouse.name = "Jerry, la souris";
    mouse.display();

    // appel de la méthode de la superclasse
    // en utilisant l'objet de la sous-classe
    mouse.eat();

  }
}
```

**Résultat :**

```java
Mon nom est Jerry

Je peux manger
```

### Abstraction en Java

L'abstraction est un concept en programmation orientée objet qui vous permet de montrer uniquement les attributs essentiels et de masquer les informations inutiles dans votre code. Le but principal de l'abstraction est de masquer les détails inutiles à vos utilisateurs.

Un exemple simple pour expliquer l'abstraction est de penser au processus qui entre en jeu lorsque vous envoyez un e-mail. Lorsque vous envoyez un e-mail, des détails complexes tels que ce qui se passe dès qu'il est envoyé et le protocole que le serveur utilise sont cachés pour vous.

Lorsque vous envoyez un e-mail, vous devez simplement entrer l'adresse e-mail du destinataire, le sujet de l'e-mail, taper le contenu et cliquer sur envoyer.

Vous pouvez abstraire des choses en utilisant des **classes abstraites** ou des **interfaces**.

Le mot-clé `abstract` est un modificateur non d'accès, utilisé pour les classes et les méthodes :

* **Classe abstraite :** est une classe restreinte qui ne peut pas être utilisée pour créer des objets. Pour y accéder, elle doit être héritée d'une autre classe.
* **Méthode abstraite :** Une méthode qui n'a pas de corps est connue comme une méthode abstraite. Nous utilisons le même mot-clé `abstract` pour créer des méthodes abstraites.

Le corps d'une méthode abstraite est fourni par la sous-classe (héritée de).

**Exemple :**

```java
// Classe abstraite
abstract class Animal {
  // Méthode abstraite (n'a pas de corps)
  public abstract void animalSound();
  // Méthode régulière
  public void sleep() {
    System.out.println("Zzzz");
  }
}

// Sous-classe (héritée de Animal)
class Cow extends Animal {
  public void animalSound() {
    // Le corps de animalSound() est fourni ici
    System.out.println("La vache dit : Meuh");
  }
}

class Main {
  public static void main(String[] args) {
    Cow myCow = new Cow(); // Créer un objet Cow
    myCow.animalSound();
    myCow.sleep();
  }
}
```

### Polymorphisme en Java

Le polymorphisme fait référence à la capacité d'un objet à prendre de nombreuses formes. Le polymorphisme se produit normalement lorsque nous avons de nombreuses classes qui sont liées les unes aux autres par héritage.

Le polymorphisme est similaire à la façon dont une personne peut avoir différentes caractéristiques en même temps.

Par exemple, un homme peut être un père, un grand-père, un mari, un employé, et ainsi de suite – tout en même temps. Donc, la même personne possède différentes caractéristiques ou comportements dans différentes situations.

**Exemple :**

Nous allons créer des objets Cow et Cat, et appeler la méthode `animalSound()` sur chacun d'eux.

```java
class Animal {
  public void animalSound() {
    System.out.println("Un animal peut faire un son.");
  }
}

class Cow extends Animal {
  public void animalSound() {
    System.out.println("Une vache dit : Meuh");
  }
}

class Cat extends Animal {
  public void animalSound() {
    System.out.println("Un chat dit : Miaou");
  }
}

class Main {
  public static void main(String[] args) {
    Animal myAnimal = new Animal();
    Animal myCow = new Cow();
    Animal myCat = new Cat();
        
    myAnimal.animalSound();
    myCow.animalSound();
    myCat.animalSound();
  }
}
```

L'héritage et le polymorphisme sont très utiles pour la réutilisabilité du code. Vous pouvez réutiliser les attributs et méthodes d'une classe existante lorsque vous créez une nouvelle classe.

## Interfaces en Java

Une `interface` est une collection de méthodes abstraites. En d'autres termes, une `interface` est une classe complètement « **abstraite** » utilisée pour regrouper des méthodes apparentées avec des corps vides.

Une interface spécifie ce qu'une classe peut faire mais pas comment elle peut le faire.

**Exemple :**

```java
// créer une interface
interface Language {
  void getName(String name);
}

// classe implémente l'interface
class ProgrammingLanguage implements Language {

  // implémentation de la méthode abstraite
  public void getName(String name) {
    System.out.println("Un de mes langages de programmation préférés est : " + name);
  }
}

class Main {
  public static void main(String[] args) {
    ProgrammingLanguage language = new ProgrammingLanguage();
    language.getName("Java");
  }
}
```

 **Résultat :**

```java
Un de mes langages de programmation préférés est : Java
```

## Conclusion

Nous avons examiné certains des principaux concepts de la programmation orientée objet dans cet article. Avoir une bonne compréhension de ces concepts est essentiel si vous voulez les utiliser correctement et écrire un bon code.

J'espère que cet article a été utile.

Je m'appelle Patrick Cyubahiro, je suis développeur logiciel et web, designer UI/UX, rédacteur technique et constructeur de communautés.

N'hésitez pas à me contacter sur Twitter : @[Pat_Cyubahiro](https://twitter.com/Pat_Cyubahiro), ou à m'écrire à : ampatrickcyubahiro[at]gmail.com

Merci d'avoir lu et bon apprentissage !