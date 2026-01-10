---
title: Les interfaces Java expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/java-interfaces-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce6740569d1a4ca34c5.jpg
tags:
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Les interfaces Java expliquées avec des exemples
seo_desc: 'Interfaces

  Interface in Java is a bit like the Class, but with a significant difference: an
  interface can only have method signatures, fields and default methods. Since Java
  8, you can also create default methods. In the next block you can see an exa...'
---

# **Interfaces**

Une interface en Java ressemble un peu à une classe, mais avec une différence significative : une `interface` ne peut contenir que des signatures de méthodes, des champs et des méthodes par défaut. Depuis Java 8, vous pouvez également créer des [méthodes par défaut](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html). Dans le bloc suivant, vous pouvez voir un exemple d'interface :

```java
public interface Vehicle {
    public String licensePlate = "";
    public float maxVel
    public void start();
    public void stop();
    default void blowHorn(){
      System.out.println("Blowing horn");
   }
}
```

L'interface ci-dessus contient deux champs, deux méthodes et une méthode par défaut. Seul, il n'est pas très utile, mais ils sont généralement utilisés avec des classes. Comment ? Simple, vous devez vous assurer qu'une classe l'`implémente`.

```java
public class Car implements Vehicle {
    public void start() {
        System.out.println("starting engine...");
    }
    public void stop() {
        System.out.println("stopping engine...");
    }
}
```

Maintenant, il y a une **règle fondamentale** : La classe doit implémenter **toutes** les méthodes de l'interface. Les méthodes doivent avoir _exactement la même_ signature (nom, paramètres et exceptions) que celle décrite dans l'interface. La classe _n'a pas_ besoin de déclarer les champs, seulement les méthodes.

## **Instances d'une interface**

Une fois que vous créez une classe Java qui `implémente` une interface, l'instance de l'objet peut être référencée comme une instance de l'interface. Ce concept est similaire à celui de l'instanciation par héritage.

```java
// suivant notre exemple précédent

Vehicle tesla = new Car();

tesla.start(); // starting engine ...
```

Une interface **ne peut pas** contenir de méthodes constructeur. Par conséquent, vous **ne pouvez pas** créer une instance d'une interface elle-même. Vous devez créer une instance d'une classe implémentant une interface pour la référencer.

Pensez aux interfaces comme à un formulaire de contrat vierge, ou à un modèle.

Que pouvez-vous faire avec cette fonctionnalité ? Du polymorphisme ! Vous pouvez utiliser uniquement des interfaces pour référencer des instances d'objets !

```java
class Truck implements Vehicle {
    public void start() {
        System.out.println("starting truck engine...");
    }
    public void stop() {
        System.out.println("stopping truck engine...");
    }
}

class Starter {
    // méthode statique, peut être appelée sans instancier la classe
    public static void startEngine(Vehicle vehicle) {
        vehicle.start();
    }
}

Vehicle tesla = new Car();
Vehicle tata = new Truck();

Starter.startEngine(tesla); // starting engine ...
Starter.startEngine(tata); // starting truck engine ...
```

## **Mais qu'en est-il de plusieurs interfaces ?**

Oui, vous pouvez implémenter plusieurs interfaces dans une seule classe. Alors que dans l'[héritage](https://forum.freecodecamp.com/t/java-docs-inheritance) au sein des classes, vous étiez limité à hériter d'une seule classe, ici vous pouvez étendre n'importe quel nombre d'interfaces. Mais n'oubliez pas d'implémenter _toutes_ les méthodes de toutes les interfaces, sinon la compilation échouera !

```java
public interface GPS {
    public void getCoordinates();
}

public interface Radio {
    public void startRadio();
    public void stopRadio();
}

public class Smartphone implements GPS,Radio {
    public void getCoordinates() {
        // return some coordinates
    }
    public void startRadio() {
      // start Radio
    }
    public void stopRadio() {
        // stop Radio
    }
}
```

## **Quelques caractéristiques des interfaces**

* Vous pouvez placer des variables dans une interface, bien que ce ne soit pas une décision judicieuse car les classes ne sont pas obligées d'avoir la même variable. En bref, évitez de placer des variables !
* Toutes les variables et méthodes dans une interface sont publiques, même si vous omettez le mot-clé `public`.
* Une interface ne peut pas spécifier l'implémentation d'une méthode particulière. C'est aux classes de le faire. Bien qu'il y ait eu une exception récente (voir ci-dessous).
* Si une classe implémente plusieurs interfaces, il y a une faible chance de chevauchement des signatures de méthodes. Comme Java n'autorise pas plusieurs méthodes avec exactement la même signature, cela peut poser des problèmes. Voir [cette question](http://stackoverflow.com/questions/2598009/method-name-collision-in-interface-implementation-java) pour plus d'informations.

## **Méthodes par défaut des interfaces**

Avant Java 8, nous n'avions aucun moyen de diriger une interface pour avoir une implémentation de méthode particulière. Cela a conduit à beaucoup de confusion et de ruptures de code si une définition d'interface est soudainement modifiée.

Supposons que vous ayez écrit une bibliothèque open source, qui contient une interface. Disons que vos clients, c'est-à-dire pratiquement tous les développeurs du monde, l'utilisent massivement et sont satisfaits. Maintenant, vous avez dû mettre à jour la bibliothèque en ajoutant une nouvelle définition de méthode à l'interface pour supporter une nouvelle fonctionnalité. Mais cela briserait _toutes_ les builds puisque toutes les classes implémentant cette interface doivent maintenant changer. Quelle catastrophe !

Heureusement, Java 8 nous fournit maintenant des méthodes `default` pour les interfaces. Une méthode `default` _peut_ contenir sa propre implémentation _directement_ dans l'interface ! Donc, si une classe n'implémente pas une méthode par défaut, le compilateur prendra l'implémentation mentionnée dans l'interface. Sympa, n'est-ce pas ? Donc dans votre bibliothèque, vous pouvez ajouter n'importe quel nombre de méthodes par défaut dans les interfaces sans craindre de casser quoi que ce soit !

```java
public interface GPS {
    public void getCoordinates();
    default public void getRoughCoordinates() {
        // implémentation pour retourner des coordonnées à partir de sources approximatives
        // telles que le wifi et le mobile
        System.out.println("Fetching rough coordinates...");
    }
}

public interface Radio {
    public void startRadio();
    public void stopRadio();
}

public class Smartphone implements GPS,Radio {
    public void getCoordinates() {
        // return some coordinates
    }
    public void startRadio() {
      // start Radio
    }
    public void stopRadio() {
        // stop Radio
    }

    // pas d'implémentation de getRoughCoordinates()
}

Smartphone motoG = new Smartphone();
motog.getRoughCoordinates(); // Fetching rough coordinates...
```

**Mais, que se passe-t-il si deux interfaces ont la même signature de méthode ?**

Excellente question. Dans ce cas, si vous ne fournissez pas l'implémentation dans la classe, le pauvre compilateur sera confus et échouera simplement ! Vous devez fournir une implémentation de méthode par défaut dans la classe également. Il existe également un moyen astucieux d'utiliser `super` pour appeler l'implémentation que vous souhaitez :

```java
public interface Radio {
    // public void startRadio();
    // public void stopRadio();

    default public void next() {
        System.out.println("Next from Radio");
    }
}

public interface MusicPlayer {
    // public void start();
    // public void pause();
    // public void stop();

    default public void next() {
        System.out.println("Next from MusicPlayer");
    }
}

public class Smartphone implements Radio, MusicPlayer {
    public void next() {
        // Supposons que vous voulez appeler MusicPlayer next
        MusicPlayer.super.next();
    }
}

Smartphone motoG = new Smartphone();
motoG.next(); // Next from MusicPlayer
```

## **Méthodes statiques dans les interfaces**

Nouveauté de Java 8, la possibilité d'ajouter des méthodes statiques aux interfaces. Les méthodes statiques dans les interfaces sont presque identiques aux méthodes statiques dans les classes concrètes. La seule grande différence est que les méthodes `static` ne sont pas héritées dans les classes qui implémentent l'interface. Cela signifie que l'interface est référencée lors de l'appel de la méthode statique et non la classe qui l'implémente.

```java
interface MusicPlayer {
  public static void commercial(String sponsor) {
    System.out.println("Now for a message brought to you by " + sponsor);
  }
  
  public void play();
}


class Smartphone implements MusicPlayer {
	public void play() {
		System.out.println("Playing from smartphone");
	}
}

class Main {
  public static void main(String[] args) {
    Smartphone motoG = new Smartphone();
    MusicPlayer.commercial("Motorola"); // Appelé sur l'interface et non sur la classe implémentante
    // motoG.commercial("Motorola"); // Cela provoquerait une erreur de compilation 
  }
}
```

## **Héritage d'une interface**

Il est également possible en Java qu'une interface _hérite_ d'une autre interface, en utilisant, vous l'avez deviné, le mot-clé `extends` :

```java
public interface Player {
    public void start();
    public void pause();
    public void stop();
}

public interface MusicPlayer extends Player {
    default public void next() {
        System.out.println("Next from MusicPlayer");
    }
}
```

Cela signifie que la classe implémentant l'interface `MusicPlayer` doit implémenter _toutes_ les méthodes de `MusicPlayer` ainsi que celles de `Player` :

```java
public class SmartPhone implements MusicPlayer {
    public void start() {
        System.out.println("start");
    }
    public void stop() {
        System.out.println("stop");
    }
    public void pause() {
        System.out.println("pause");
    }
}
```

Vous avez maintenant une bonne compréhension des interfaces Java ! Allez apprendre les classes abstraites pour voir comment Java vous donne une autre façon de définir des contrats.