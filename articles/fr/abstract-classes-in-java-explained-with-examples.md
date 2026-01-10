---
title: Les classes abstraites en Java expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/abstract-classes-in-java-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d14740569d1a4ca35ca.jpg
tags:
- name: class
  slug: class
- name: Java
  slug: java
- name: object oriented
  slug: object-oriented
- name: toothbrush
  slug: toothbrush
seo_title: Les classes abstraites en Java expliquées avec des exemples
seo_desc: 'Abstract classes are classes declared with abstract. They can be subclassed
  or extended, but cannot be instantiated. You can think of them as a class version
  of interfaces, or as an interface with actual code attached to the methods.

  For example, say...'
---

Les classes abstraites sont des classes déclarées avec `abstract`. Elles peuvent être sous-classées ou étendues, mais ne peuvent pas être instanciées. Vous pouvez les considérer comme une **version classe** des interfaces, ou comme une interface avec du code réel attaché aux méthodes.

Par exemple, disons que vous avez une classe `Vehicle` qui définit la fonctionnalité de base (méthodes) et les composants (variables d'objet) que les véhicules ont en commun. 

Vous ne pouvez pas créer un objet de `Vehicle` car un véhicule est lui-même un concept abstrait et général. Les véhicules ont des roues et des moteurs, mais le nombre de roues et la taille des moteurs peuvent varier considérablement.

Vous pouvez cependant étendre la fonctionnalité de la classe véhicule pour créer une `Car` ou une `Motorcycle` :

```java
abstract class Vehicle
{
  // variable utilisée pour déclarer le nombre de roues dans un véhicule
  private int wheels;
  
  // Variable pour définir le type de moteur utilisé
  private Motor motor;
  
  // une méthode abstraite qui déclare uniquement, mais ne définit pas la fonctionnalité de démarrage 
  // car chaque véhicule utilise un mécanisme de démarrage différent
  abstract void start();
}

public class Car extends Vehicle
{
  ...
}

public class Motorcycle extends Vehicle
{
  ...
}
```

Rappelez-vous, vous ne pouvez pas instancier un `Vehicle` n'importe où dans votre programme – à la place, vous pouvez utiliser les classes `Car` et `Motorcycle` que vous avez déclarées précédemment et créer des instances de celles-ci :

```java
Vehicle newVehicle = new Vehicle();    // Invalide
Vehicle car = new Car();  // valide
Vehicle mBike = new Motorcycle();  // valide

Car carObj = new Car();  // valide
Motorcycle mBikeObj = new Motorcycle();  // valide
```

## Plus d'informations :

* [Apprendre la programmation fonctionnelle en Java - Cours complet](https://www.freecodecamp.org/news/functional-programming-in-java-course/)
* [Getters et Setters en Java expliqués](https://www.freecodecamp.org/news/java-getters-and-setters/)
* [L'héritage en Java expliqué](https://www.freecodecamp.org/news/inheritance-in-java-explained/)