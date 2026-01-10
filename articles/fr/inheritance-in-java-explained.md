---
title: L'héritage en Java expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T19:08:00.000Z'
originalURL: https://freecodecamp.org/news/inheritance-in-java-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc4740569d1a4ca3982.jpg
tags:
- name: inheritance
  slug: inheritance
- name: Java
  slug: java
seo_title: L'héritage en Java expliqué
seo_desc: 'Inheritance

  Java inheritance refers to the ability of a Java Class to inherit the properties
  from some other Class. Think of it like a child inheriting properties from its parents,
  the concept is very similar to that. In Java lingo, it is also called...'
---

# **Héritage**

L'héritage en Java fait référence à la capacité d'une classe Java à `hériter` des propriétés d'une autre classe. Pensez-y comme un enfant héritant des propriétés de ses parents, le concept est très similaire à cela. En jargon Java, on parle aussi d'_étendre_ une classe.

Quelques choses simples à retenir :

* La classe qui étend ou hérite est appelée une **sous-classe**
* La classe qui est étendue ou héritée est appelée une **superclasse**

Ainsi, l'héritage donne à Java la capacité sympa de _réutiliser_ du code, ou de partager du code entre les classes !

Décrivons-le avec l'exemple classique d'une classe `Vehicle` et d'une classe `Car` :

```java
public class Vehicle {
    public void start() {
        // démarrer le moteur
    }

    public void stop() {
        // arrêter le moteur
    }
}

public class Car extends Vehicle {
    int numberOfSeats = 4;

    public int getNumberOfSeats() {
        return numberOfSeats;
    }
}
```

Ici, nous pouvons voir la classe `Car` héritant des propriétés de la classe `Vehicle`. Ainsi, nous n'avons pas à écrire le même code pour les méthodes `start()` et `stop()` pour `Car`, car ces propriétés sont disponibles depuis sa classe parente ou superclasse. Par conséquent, les objets créés à partir de la classe `Car` auront _également_ ces propriétés !

```java
Car tesla = new Car();

tesla.start();

tesla.stop();
```

[Exécuter le code](https://repl.it/CJXz/0)

Mais, est-ce que la classe parente a les méthodes de l'enfant ? Non, ce n'est pas le cas.

Par conséquent, chaque fois que vous devez partager un morceau de code commun entre plusieurs classes, il est toujours bon d'avoir une classe parente, puis d'étendre cette classe chaque fois que nécessaire ! Cela réduit le nombre de lignes de code, rend le code modulaire et simplifie les tests.

## **Qu'est-ce qui peut être hérité ?**

* Tous les champs et méthodes `protected` et `public` de la classe parente

## **Qu'est-ce qui ne peut pas être hérité ?**

* Les champs et méthodes `private`
* Les constructeurs. Bien que le constructeur de la sous-classe _doive_ appeler le constructeur de la superclasse s'il est défini (Plus d'informations à ce sujet plus tard !)
* Plusieurs classes. Java ne supporte que l'**héritage simple**, c'est-à-dire que vous ne pouvez hériter que d'une seule classe à la fois.
* Les champs. Les champs individuels d'une classe ne peuvent pas être redéfinis par la sous-classe.

## **Casting de type et référence**

En Java, il est possible de référencer une sous-classe comme une _instance_ de sa superclasse. Cela s'appelle le _polymorphisme_ en programmation orientée objet (POO), la capacité pour un objet de prendre plusieurs formes. Par exemple, l'objet de la classe `Car` peut être référencé comme une instance de la classe `Vehicle` comme ceci :

```java
Vehicle car = new Car();
```

Bien que l'inverse ne soit pas possible :

```java
Car car = new Vehicle(); // ERREUR
```

[Exécuter le code](https://repl.it/CJYB/0)

Puisque vous pouvez référencer une sous-classe Java comme une instance de superclasse, vous pouvez facilement caster une instance d'un objet de sous-classe en une instance de superclasse. Il est possible de caster un objet de superclasse en un type de sous-classe, mais _uniquement si l'objet est vraiment une instance de la sous-classe_. Donc, gardez cela à l'esprit :

```java
Car car = new Car();
Vehicle vehicle = car; // upcasting
Car car2 = (Car)vehicle; // downcasting

Bike bike = new Bike(); // disons que Bike est aussi une sous-classe de Vehicle
Vehicle v = bike; // upcasting, aucun problème ici.
Car car3 = (Car)bike; // Erreur de compilation : car bike n'est PAS une instance de Car
```

[Exécuter le code](https://repl.it/CJYM/0)

Maintenant, vous savez comment partager du code grâce à une relation parent-enfant. Mais, que faire si vous n'aimez pas l'implémentation d'une méthode particulière dans la classe enfant et souhaitez en écrire une nouvelle ? Que faites-vous alors ?

## **Redéfinissez-la !**

Java vous permet de _redéfinir_ ou de redéfinir les méthodes définies dans la superclasse. Par exemple, votre classe `Car` a une implémentation différente de `start()` que la classe parente `Vehicle`, donc vous faites ceci :

```java
public class Vehicle {
    public void start() {
      System.out.println("Code de démarrage du véhicule");
    }
}

public class Car extends Vehicle {
    public void start() {
      System.out.println("Code de démarrage de la voiture");
  }
}

Car car = new Car();
car.start(); // "Code de démarrage de la voiture"
```

[Exécuter le code](https://repl.it/CJYZ/1)

Il est donc assez simple de redéfinir des méthodes dans la sous-classe. Cependant, il y a un _piège_. Seule la méthode de la superclasse avec la _signature de méthode exactement identique_ à celle de la méthode de la sous-classe sera redéfinie. Cela signifie que la définition de la méthode de la sous-classe doit avoir exactement le même nom, le même nombre et type de paramètres, et dans la même séquence exacte. Ainsi, `public void start(String key)` ne redéfinirait pas `public void start()`.

**Notes** :

* Vous ne pouvez pas redéfinir les méthodes privées de la superclasse. (Assez évident, n'est-ce pas ?)
* Que se passe-t-il si la méthode de la superclasse que vous redéfinissez dans la sous-classe est soudainement supprimée ou modifiée ? Cela échouerait à l'exécution ! Java vous fournit donc une annotation pratique `@Override` que vous pouvez placer sur la méthode de la sous-classe, ce qui avertira le compilateur de ces incidents !

Les annotations en Java sont une bonne pratique de codage, mais elles ne sont pas une nécessité. Le compilateur est suffisamment intelligent pour comprendre la redéfinition par lui-même. Contrairement à d'autres langages OOP, les annotations en Java ne modifient pas nécessairement la méthode ou n'ajoutent pas de fonctionnalités supplémentaires.

## **Comment appeler les méthodes de la superclasse ?**

Drôle que vous posiez la question ! Utilisez simplement le mot-clé `super` :

```java
public class Vehicle() {
    public void start() {
      System.out.println("Code de démarrage du véhicule");
    }
}

public class Car extends Vehicle {
    public void run() {
      super.start();
  }
}

Car car = new Car();
car.run(); // "Code de démarrage du véhicule"
```

[Exécuter le code](https://repl.it/CJY4/0)

**N.B.** : Bien que vous puissiez appeler la méthode parente en utilisant un appel `super`, vous ne pouvez pas remonter la hiérarchie d'héritage avec des appels `super` enchaînés.

## **Comment connaître le type d'une classe ?**

En utilisant le mot-clé `instanceof`. Ayant beaucoup de classes et de sous-classes, il serait un peu confus de savoir quelle classe est une sous-classe de quelle autre à l'exécution. Nous pouvons donc utiliser `instanceof` pour déterminer si un objet est une instance d'une classe, une instance d'une sous-classe, ou une instance d'une interface.

```java
Car car = new Car();

boolean flag = car instanceof Vehicle; // vrai dans ce cas !
```

## **Constructeurs et héritage**

Comme mentionné précédemment, les constructeurs ne peuvent pas être directement hérités par une sous-classe. Cependant, une sous-classe est _tenue_ d'appeler le constructeur de sa classe parente comme [première opération](http://stackoverflow.com/questions/1168345/why-does-this-and-super-have-to-be-the-first-statement-in-a-constructor) dans son propre constructeur. Comment ? Vous l'avez deviné, en utilisant `super` :

```java
public class Vehicle {
    public Vehicle() {
        // constructeur
    }
    public void start() {
      System.out.println("Code de démarrage du véhicule");
    }
}

public class Car extends Vehicle {
    public Car() {
      super();
    }
    public void run() {
      super.start();
  }
}
```

[Exécuter le code](https://repl.it/CJY8/0)

Rappelez-vous, si la superclasse n'a aucun constructeur défini, vous n'avez pas à l'appeler explicitement dans la sous-classe. Java gère cela en interne pour vous ! L'appel au constructeur `super` est effectué dans le cas où la superclasse doit être appelée avec un autre constructeur que le _constructeur par défaut_.

Si aucun autre constructeur n'est défini, alors Java appelle le constructeur par défaut de la superclasse (_même s'il n'est pas défini explicitement_).

Félicitations, vous savez maintenant tout sur l'héritage ! Lisez plus sur les façons avancées d'hériter des choses dans les classes abstraites et les [interfaces](https://forum.freecodecamp.com/t/java-docs-interfaces) !