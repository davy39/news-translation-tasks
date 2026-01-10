---
title: Un guide des principes de la programmation orientée objet
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-06-18T09:13:37.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-object-oriented-programming-principles
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/oop-principles.png
tags:
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Un guide des principes de la programmation orientée objet
seo_desc: "A programming language is generally classified based on its support for\
  \ one or more paradigms. \nObject-oriented programming is one such paradigm, where\
  \ the code is organized as objects. \nIt is used to develop desktop and mobile applications\
  \ or more c..."
---

Un langage de programmation est généralement classé en fonction de sa prise en charge d'un ou plusieurs paradigmes. 

La programmation orientée objet est l'un de ces paradigmes, où le code est organisé en objets. 

Elle est utilisée pour développer des applications de bureau et mobiles ou des applications web ou d'entreprise plus complexes. 

En utilisant la programmation orientée objet, vous pouvez créer des logiciels modulaires et évolutifs qui sont faciles à maintenir.

Dans cet article, vous apprendrez les principes de la programmation orientée objet qui constituent la base pour construire des systèmes robustes. 

Nous utiliserons Java comme langage de programmation pour les exemples fournis ci-dessous.

## Qu'est-ce que la programmation orientée objet ?

La programmation orientée objet est une méthodologie de programmation qui modélise les entités du monde réel sous forme d'objets. 

Ces objets sont des instances de classes. 

Une classe peut être considérée comme un plan et chaque classe peut contenir des champs, qui définissent les attributs de l'objet, et des méthodes, qui décrivent le comportement de l'objet. Chaque classe peut être développée, testée et déboguée indépendamment.

Maintenant que vous avez une compréhension de la définition de base de la programmation orientée objet, examinons ses principes fondamentaux.

Il existe quatre principes fondamentaux, ou piliers, dans le paradigme de la programmation orientée objet. Ils sont :
-  Abstraction
-  Encapsulation
-  Héritage
-  Polymorphisme

Que signifient-ils ? Explorons plus en détail avec une explication simple suivie d'un exemple pour chacun d'eux dans les sections suivantes.

## Qu'est-ce que l'abstraction ?

L'abstraction est définie comme le concept de masquer les détails de l'implémentation et d'exposer uniquement les fonctionnalités nécessaires de l'objet à l'utilisateur. 

Les mots-clés que vous devez garder à l'esprit ici sont : 'Masquage de l'implémentation'. 

L'abstraction en Java peut être réalisée grâce aux interfaces et aux classes abstraites.



```java
abstract class Animal {
    public abstract void makeSomeNoise();
}

class Dog extends Animal {
    public void makeSomeNoise() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.makeSomeNoise(); // Sortie - Bark
    }
}
```

Dans l'exemple ci-dessus, l'abstraction est réalisée à l'aide d'une classe abstraite nommée `Animal`. 

Ici, seule la fonctionnalité nécessaire de la classe est exposée via la méthode `makeSomeNoise()`. 

Les détails de l'implémentation sont masqués dans la classe abstraite et ils ne sont fournis que dans la classe concrète `Dog`, qui étend la classe `Animal`. 

Notez que vous en apprendrez plus sur le mot-clé `extends` lorsque nous discuterons de l'héritage.

## Qu'est-ce que l'encapsulation ?

L'encapsulation fait référence au concept d'encapsuler ou d'envelopper les variables membres (données) et les méthodes (comportement) d'un objet dans une seule unité, telle qu'une classe. 

Les informations internes de l'objet sont masquées afin que nous puissions prévenir les modifications non intentionnelles et permettre uniquement un accès contrôlé. Les mots-clés que vous devez garder à l'esprit ici sont : 'Masquage d'informations'.

L'encapsulation en Java est réalisée grâce aux modificateurs d'accès. Nous marquons les champs comme `private` et les rendons accessibles via des méthodes publiques setter et getter.

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Raj", 30);
        person.display(); // Sortie - Name: Raj, Age: 30

        person.setName("Kumar");
        person.setAge(25);
        person.display(); // Sortie - Name: Kumar, Age: 25
    }
}

```

Dans l'exemple ci-dessus, les champs et méthodes sont encapsulés dans une classe nommée `Person`. 

Vous déclarez les champs `name` et `age` comme `private` et fournissez des méthodes publiques setter et getter `getName()`, `setName()`, `getAge()`, et `setAge()` pour modifier les valeurs selon les besoins. 

## Qu'est-ce que l'héritage ?

L'héritage établit une relation hiérarchique entre deux classes. 

Dans ce concept, une classe hérite des champs (propriétés) et des méthodes (comportement) d'une autre classe, tout en ayant ses propres propriétés et comportement. 

La classe qui hérite d'une autre est appelée une sous-classe, classe dérivée ou classe enfant. La classe dont la sous-classe hérite est connue sous le nom de superclasse, classe de base ou classe parente. 

En Java, l'héritage est réalisé en utilisant le mot-clé `extends`.

```java
class Animal {
    public void makeSomeNoise(){
    	System.out.println("Make some animal noise");
    }
}

class Dog extends Animal {
    public void makeSomeNoise() {
        System.out.println("Bark");
    }
    public void doSomething(){
    	System.out.println("Play with ball");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.makeSomeNoise(); // Sortie - Bark
        myDog.doSomething(); // Sortie - Play with ball
    }
}
```

Dans l'exemple ci-dessus, le mot-clé `extends` indique que la classe `Dog` est la sous-classe de la classe `Animal`. 

La classe `Dog` hérite de la méthode `makeSomeNoise()` de la classe `Animal`. Cela permet à la classe `Dog` de réutiliser la méthode et de fournir sa propre implémentation sans avoir à la réécrire complètement. 

Vous pouvez également noter que la classe `Dog` a son propre comportement via la méthode `doSomething()`. 

L'héritage définit une relation "EST-UN" entre les deux classes. Dans notre exemple, Dog EST-UN Animal.

Notez que Java prend en charge l'héritage multi-niveaux. Par exemple, `class Labrador` hérite de `class Dog`, qui à son tour hérite de `class Animal`. Cependant, il ne prend pas en charge l'héritage multiple. C'est-à-dire qu'une classe n'est pas autorisée à hériter de deux classes parentes ou plus.

## Qu'est-ce que le polymorphisme ?
Poly (plusieurs), morph (formes). 

Le polymorphisme définit la capacité d'un objet à être représenté sous différentes formes. 

En Java, le polymorphisme peut être catégorisé en deux types : le polymorphisme à la compilation et le polymorphisme à l'exécution.

Le polymorphisme à la compilation est réalisé grâce à la surcharge de méthodes - plusieurs méthodes ont le même nom mais des types ou un nombre de paramètres différents.

```java
class MathOperation {
    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Main {
    public static void main(String[] args) {
        MathOperation math = new MathOperation();
        System.out.println(math.add(95, 5));       // Sortie - 100
        System.out.println(math.add(75, 5, 20));   // Sortie - 100
    }
}

```

Dans l'exemple ci-dessus, nous avons surchargé la méthode `add()`. Il y a deux méthodes avec le même nom `add` mais elles ont un nombre différent de paramètres. 

Lors de la compilation, en fonction du nombre de paramètres passés à la méthode, l'appel approprié est effectué.

Le polymorphisme à l'exécution est réalisé grâce à la substitution de méthodes - une sous-classe a une méthode avec le même nom et le même ensemble de paramètres que celle de sa méthode de superclasse. Cependant, elle fournit sa propre implémentation de la méthode. 

Ici, la résolution de la méthode se fait à l'exécution.

```java
class Animal {
    public void makeSomeNoise() {
        System.out.println("Make some animal noise");
    }
}

class Dog extends Animal {
    @Override
    public void makeSomeNoise() {
        System.out.println("Barks");
    }
}

class Cat extends Animal {
    @Override
    public void makeSomeNoise() {
        System.out.println("Meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal; 
        
        myAnimal = new Dog(); 
        myAnimal.makeSomeNoise(); // Sortie - Barks

        myAnimal = new Cat(); 
        myAnimal.makeSomeNoise(); // Sortie - Meows
    }
}
```

Dans l'exemple ci-dessus, la méthode `makeSomeNoise()` de la classe `Animal` est substituée par les sous-classes `Dog` et `Cat` et elles fournissent leur propre implémentation de cette méthode. 

Lors de la création de l'objet, la variable `Animal` contient un objet `Dog` ou `Cat` et lorsque la méthode `makeSomeNoise()` est appelée, la méthode substituée appropriée est appelée en fonction du type d'objet réel.

## Conclusion

Dans cet article, nous avons exploré les principes fondamentaux de la programmation orientée objet (POO). 

La familiarité avec ces concepts est cruciale pour construire des systèmes logiciels robustes, maintenables et évolutifs.