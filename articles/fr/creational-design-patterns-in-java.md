---
title: Qu'est-ce que les Design Patterns de Création en Java ? Explications avec des
  Exemples
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-07-26T13:04:50.000Z'
originalURL: https://freecodecamp.org/news/creational-design-patterns-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Creational.png
tags: []
seo_title: Qu'est-ce que les Design Patterns de Création en Java ? Explications avec
  des Exemples
seo_desc: 'Design Patterns provide you with an idea or a strategy for solving commonly
  occurring problems. They are proven solutions that follow the best practices and
  help you make your code flexible, reusable, and maintainable.

  The design patterns are classif...'
---

Les Design Patterns vous fournissent une idée ou une stratégie pour résoudre des problèmes courants. Ce sont des solutions éprouvées qui suivent les meilleures pratiques et vous aident à rendre votre code flexible, réutilisable et maintenable.

Les design patterns sont classés en trois catégories selon leur objectif :

- Créationnels
- Structurels
- Comportementaux

Dans cet article, je vais vous expliquer ce que sont les design patterns de création, examiner les différents types et explorer certains d'entre eux à l'aide d'exemples de code Java.

## Design Patterns de Création

Comme leur nom l'indique, les design patterns de création traitent de la création d'objets. Ils fournissent différentes façons de créer des objets. En suivant ces design patterns, vous vous assurez que le processus d'instanciation des objets est flexible et hautement efficace. Cela est réalisé en rendant le système indépendant de la création, de la composition et de la représentation de l'objet.

Il existe cinq types différents de design patterns de création :
1. Singleton
2. Factory Method
3. Abstract Factory
4. Builder
5. Prototype

Dans les sections suivantes, nous parlerons de ces design patterns en les définissant, en fournissant des exemples de code et en expliquant leurs cas d'utilisation potentiels.

## Design Pattern Singleton

Un design pattern singleton garantit qu'il n'y a qu'une seule instance d'une classe dans toute votre application. Vous êtes autorisé à créer un seul objet de la classe singleton, et tout appel ultérieur pour créer un autre objet de la même classe retournera la référence de l'objet existant.

Cela vous permet d'avoir un point d'accès unique à l'objet dans toute votre application. Examinons le code pour implémenter le pattern singleton :

```java
public class Singleton {
    
    private static Singleton instance;

    private Singleton() {
      
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
    
    public void displayMessage() {
        System.out.println("Bonjour, je suis une instance Singleton !");
    }

    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();

        singleton.displayMessage();
    }
}
```

Dans l'exemple ci-dessus, vous remarquerez les trois aspects cruciaux que vous devez retenir lors de l'implémentation d'une classe singleton :

- Une instance privée et statique
- Un constructeur privé
- Une méthode publique et statique

L'instance privée et statique est du même type que la classe elle-même, et elle est marquée comme statique car elle doit être accessible uniquement via la référence de la classe et non en créant un objet.

Le constructeur de la classe est marqué comme privé pour empêcher la création d'objets de la classe.

Nous avons également une méthode publique et statique nommée `getInstance`, qui vérifie d'abord si l'instance est nulle. Si c'est le cas, elle permet la création d'une nouvelle instance de la classe. Sinon, elle retourne la référence de l'instance existante.

Nous avons créé une instance de la classe `Singleton` en appelant la méthode statique `getInstance`.

### Cas d'Utilisation

Voici quelques cas où vous pourriez utiliser le design pattern singleton :

- Connexions à la base de données : Ces opérations sont coûteuses, donc pour éviter le surcoût de l'ouverture et de la fermeture répétées des connexions, vous pouvez implémenter le design pattern singleton pour réutiliser les connexions existantes du pool.
- Journalisation : Vous pouvez avoir une seule instance du logger pour journaliser les messages dans votre application afin de promouvoir l'efficacité et la cohérence.
- Configuration : Vous pouvez avoir un gestionnaire de configuration centralisé unique pour charger les paramètres à partir de n'importe quelle source et l'utiliser dans toute l'application.

Remarque : Il existe quelques autres variations pour implémenter une classe singleton, mais nous n'explorerons pas celles-ci dans cet article. De plus, ce que nous avons vu ci-dessus est une implémentation simple dans une application monothread. Il y a des chances que vous rencontriez certains défis avec cela dans un environnement multithread et traiter cela dépasse également le cadre de cet article.

## Design Pattern Factory Method

Dans le livre "[Design Patterns: Elements of Reusable Object-Oriented Software](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/)", les auteurs (appelés le Gang of Four ou GoF) définissent la factory method comme suit :
> définit une interface pour créer un objet, mais laisse les sous-classes décider quelle classe instancier

Comme le montre la définition, dans le design pattern factory method, une interface est fournie pour créer des objets. Diverses classes implémentent cette interface et retournent des instances de leurs types respectifs. Une factory détermine ensuite quel type d'objet doit être retourné en fonction de conditions prédéfinies.

Ce design pattern encapsule la logique d'instanciation, découple le processus de création d'objets, rendant votre code plus flexible, et favorise l'extensibilité. Examinons l'exemple de code pour une meilleure compréhension :

1. Nous définissons une interface `Shape` :

```java
public interface Shape {
    void draw();
}
```

2. Nous créons des implémentations concrètes de la classe `Shape` nommées `Square` et `Circle` :

```java
public class Square implements Shape {
    public void draw() {
        System.out.println("Dessin d'un carré");
    }
}

public class Circle implements Shape {
    public void draw() {
        System.out.println("Dessin d'un cercle");
    }
}

```

3. Nous définissons une interface `ShapeFactory` pour créer les objets de type `Shape` :

```java
public interface ShapeFactory {
    Shape createShape();
}

```

4. Enfin, nous implémentons des factories concrètes :

```java
public class SquareFactory implements ShapeFactory {
    public Shape createShape() {
        return new Square();
    }
}

public class CircleFactory implements ShapeFactory {
    public Shape createShape() {
        return new Circle();
    }
}
```

5. Le client utilise la factory pour créer des objets de différentes formes :

```java
public class Main {

    public static void main(String[] args) {
        ShapeFactory squareFactory = new SquareFactory();
        Shape square = squareFactory.createShape();
        square.draw();

        ShapeFactory circleFactory = new CircleFactory();
        Shape circle = circleFactory.createShape();
        circle.draw();
    }
}
```

De cette manière, nous pouvons nous assurer que le code client est découplé des classes spécifiques, car il n'a pas besoin d'instancier ces objets directement. Cela facilite l'ajout de nouvelles formes.

### Cas d'Utilisation :

- Connexions à la base de données : Vous pouvez configurer une `DatabaseConnectionFactory` dans votre application pour vous connecter à différents types de bases de données (par exemple : MySQL, PostgreSQL, Oracle)
- Authentification des utilisateurs : Vous pouvez configurer une `AuthenticationFactory` qui prend en charge différentes méthodes d'authentification (par exemple : OAuth, SAML, LDAP)

## Design Pattern Abstract Factory

Nous allons une fois de plus nous référer au livre "[Design Patterns: Elements of Reusable Object-Oriented Software](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/)" pour la définition de l'abstract factory. Il stipule :
> Abstract Factory fournit une interface pour créer des familles d'objets liés ou dépendants sans spécifier leurs classes concrètes.

Cela signifie que vous avez une super-factory qui vous permet de créer un groupe de factories liées. Vous pouvez penser au design pattern abstract factory comme une factory de factories, fournissant une couche d'abstraction supplémentaire par rapport au design pattern factory method que nous avons discuté précédemment.

Prenons un exemple du design pattern abstract factory en utilisant l'idée d'une `CarFactory` pour créer différents types de voitures.

1. Nous définissons une interface commune pour toutes les voitures nommée `Car` :

```java
public interface Car {
    void drive();
}
```

2. Nous créons des implémentations concrètes de l'interface `Car` nommées `Sedan` et `SUV` :

```java
public class Sedan implements Car {
    @Override
    public void drive() {
        System.out.println("Conduite d'une berline");
    }
}

public class SUV implements Car {
    @Override
    public void drive() {
        System.out.println("Conduite d'un SUV");
    }
}
```

3. Nous définissons une interface pour les factories de voitures nommée `CarFactory` :

```java
public interface CarFactory {
    Car createCar();
}
```

4. Nous définissons des factories concrètes nommées `SedanFactory` et `SUVFactory` qui créent respectivement des voitures `Sedan` et `SUV` :

```java
public class SedanFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Sedan();
    }
}

public class SUVFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new SUV();
    }
}
```

5. La classe `AbstractCarFactory` définit une classe abstraite pour créer différentes factories de voitures :

```java
public abstract class AbstractCarFactory {
    public abstract CarFactory getCarFactory(String type);
}
```

6. La classe `ConcreteCarFactory` implémente `AbstractCarFactory` pour retourner la factory appropriée en fonction du type de voiture :

```java
public class ConcreteCarFactory extends AbstractCarFactory {
    @Override
    public CarFactory getCarFactory(String type) {
        if (type.equalsIgnoreCase("Sedan")) {
            return new SedanFactory();
        } else if (type.equalsIgnoreCase("SUV")) {
            return new SUVFactory();
        }
        return null;
    }
}
```

7. Enfin, dans le code client, nous utilisons le design pattern abstract factory pour créer des voitures `Sedan` et `SUV` sans spécifier leurs classes concrètes :

```java
public class Main {
    public static void main(String[] args) {
        AbstractCarFactory carFactory = new ConcreteCarFactory();

        CarFactory sedanFactory = carFactory.getCarFactory("Sedan");
        Car sedan = sedanFactory.createCar();
        sedan.drive();  // Sortie - Conduite d'une berline

        CarFactory suvFactory = carFactory.getCarFactory("SUV");
        Car suv = suvFactory.createCar();
        suv.drive();  // Sortie - Conduite d'un SUV
    }
}
```

### Cas d'Utilisation

- Lorsque vous voulez avoir un système qui est indépendant de la création, de la composition et de la représentation de ses composants.
- Lorsque vous voulez configurer un système avec une famille de composants liés.

## Design Pattern Builder

Le design pattern builder est un autre design pattern de création utilisé pour construire des objets complexes. Vous pourriez rencontrer une classe avec de nombreux paramètres requis pour créer une instance. Certains peuvent être obligatoires, tandis que d'autres peuvent être optionnels. En utilisant le design pattern builder, vous pouvez séparer le processus de création de tels objets complexes de leur représentation.

Voici un exemple :

```java
public class Person {
    
    private final String firstName;
    private final String lastName;

    private final int age;
    private final String address;
    private final String phoneNumber;

    private Person(PersonBuilder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
        this.address = builder.address;
        this.phoneNumber = builder.phoneNumber;
    }

    // Getters pour tous les paramètres

    @Override
    public String toString() {
        return "Person{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", age=" + age +
                ", address='" + address + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                '}';
    }

    public static class PersonBuilder {
        
        private final String firstName;
        private final String lastName;

        private int age;
        private String address;
        private String phoneNumber;

        public PersonBuilder(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public PersonBuilder age(int age) {
            this.age = age;
            return this;
        }

        public PersonBuilder address(String address) {
            this.address = address;
            return this;
        }

        public PersonBuilder phoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
            return this;
        }

        public Person build() {
            return new Person(this);
        }
    }
}

```

Dans l'exemple ci-dessus, nous avons une classe `Person` qui contient quelques paramètres requis (`firstName` et `lastName`) et certains paramètres optionnels (`age`, `address`, `phoneNumber`). Le constructeur est également marqué comme privé afin que seule la classe `PersonBuilder` associée à celle-ci soit autorisée à y accéder.

La classe `PersonBuilder` a les mêmes propriétés que la classe `Person`. Les paramètres requis sont définis via son constructeur. Elle dispose également de méthodes appropriées pour définir les paramètres optionnels qui retournent `this` et permettent l'enchaînement de méthodes.

```java
public class Main {
    public static void main(String[] args) {
        Person person = new Person.PersonBuilder("Mikel", "Arteta")
                .age(42)
                .address("1 North London")
                .phoneNumber("111-1234")
                .build();

        System.out.println(person);
    }
}

```

Pour utiliser cela, nous avons créé une instance `PersonBuilder` avec les paramètres requis. Nous avons défini les paramètres optionnels en utilisant l'enchaînement de méthodes. Enfin, nous avons appelé la méthode `build()` pour créer un objet `Person`.

### Cas d'Utilisation :
- Vous pouvez utiliser le design pattern builder lorsque vous voulez construire un objet complexe d'une classe qui a une combinaison de propriétés obligatoires et optionnelles.
- Vous pouvez l'utiliser lorsque votre classe a de nombreux paramètres et qu'il est inefficace d'avoir différents constructeurs pour chaque combinaison de paramètres.
- Vous pouvez l'utiliser pour fournir différentes représentations du même objet au client.

## Design Pattern Prototype

Il pourrait y avoir un scénario où vous voulez créer un objet similaire à un objet existant. Le design pattern prototype vous permet d'y parvenir. Dans ce pattern, l'objet existant est connu sous le nom de prototype, et l'idée est qu'il est beaucoup plus efficace de copier un objet existant que d'en créer un nouveau à partir de zéro.

Il pourrait ne pas être possible pour vous de créer une copie exacte du prototype car certains champs de cet objet pourraient être marqués comme privés. Cela peut être surmonté en utilisant l'approche de la méthode clone. Nous créons une interface commune qui inclut uniquement une méthode clone, et toutes les classes qui prennent en charge le clonage de leurs objets implémentent cette interface. Examinons l'exemple de code pour cela :

1. Nous créons une interface `Prototype` qui définit une méthode `clone` que les classes doivent implémenter :

```java
public interface Prototype extends Cloneable {
    Prototype clone();
}
```

2. Nous créons `Circle` et `Rectangle` qui sont des classes concrètes implémentant l'interface `Prototype` :

```java
public class Circle implements Prototype {
    private int radius;
    
    public Circle(int radius) {
        this.radius = radius;
    }

    public int getRadius() {
        return radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    @Override
    public Prototype clone() {
        return new Circle(this.radius);
    }

    @Override
    public String toString() {
        return "Cercle avec un rayon : " + radius;
    }
}

public class Rectangle implements Prototype {
    private int width;
    private int height;
    
    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    @Override
    public Prototype clone() {
        return new Rectangle(this.width, this.height);
    }

    @Override
    public String toString() {
        return "Rectangle avec une largeur : " + width + " et une hauteur : " + height;
    }
}
```

3. Dans le code client, nous créons les objets originaux (`originalCircle` et `originalRectangle`) puis nous les clonons pour créer de nouvelles instances (`clonedCircle` et `clonedRectangle`)

Notez que les instances clonées peuvent être modifiées indépendamment des objets originaux.

```java
public class Main {
    public static void main(String[] args) {
        Circle originalCircle = new Circle(10);
        Circle clonedCircle = (Circle) originalCircle.clone();
        clonedCircle.setRadius(20);

        System.out.println(originalCircle);  
        System.out.println(clonedCircle);    

        Rectangle originalRectangle = new Rectangle(15, 25);
        Rectangle clonedRectangle = (Rectangle) originalRectangle.clone();
        clonedRectangle.setWidth(30);
        clonedRectangle.setHeight(50);

        System.out.println(originalRectangle);  
        System.out.println(clonedRectangle);    
    }
}
```

### Cas d'Utilisation

- Suivez le design pattern prototype lorsque l'objet que vous voulez créer implique un processus de construction complexe.
- Utilisez-le lorsque l'initialisation de l'objet est coûteuse et implique beaucoup de ressources coûteuses.

## Conclusion

Dans cet article, nous avons exploré les design patterns de création et nous sommes penchés sur des exemples de code et des cas d'utilisation. Comprendre ces patterns et leur application vous aidera à rendre votre code plus extensible et maintenable.

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/abaradwaj/)