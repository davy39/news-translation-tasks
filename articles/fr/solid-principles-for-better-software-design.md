---
title: Qu'est-ce que SOLID ? Principes pour une meilleure conception logicielle
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-05-03T14:00:01.000Z'
originalURL: https://freecodecamp.org/news/solid-principles-for-better-software-design
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/solid-principles.png
tags:
- name: design patterns
  slug: design-patterns
- name: software design
  slug: software-design
- name: solid
  slug: solid
seo_title: Qu'est-ce que SOLID ? Principes pour une meilleure conception logicielle
seo_desc: "The SOLID principles are a set of guidelines for writing high-quality,\
  \ maintainable, and scalable software. \nThey were introduced by Robert C. Martin\
  \ in his 2000 paper “Design Principles and Design Patterns” to help developers write\
  \ software that is ..."
---

Les principes SOLID sont un ensemble de directives pour écrire des logiciels de haute qualité, maintenables et évolutifs. 

Ils ont été introduits par Robert C. Martin dans son article de 2000 [Design Principles and Design Patterns](https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf) pour aider les développeurs à écrire des logiciels faciles à comprendre, modifier et étendre. 

Ces concepts ont ensuite été développés par Michael Feathers, qui nous a présenté l'acronyme SOLID.

L'acronyme SOLID signifie :

* **S**ingle Responsibility Principle (SRP)
* **O**pen-Closed Principle (OCP)
* **L**iskov Substitution Principle (LSP)
* **I**nterface Segregation Principle (ISP)
* **D**ependency Inversion Principle (DIP)

Ces principes offrent un moyen pour les développeurs d'organiser leur code et de créer des logiciels flexibles, faciles à modifier et testables. L'application des principes SOLID peut conduire à un code plus modulaire, maintenable et extensible, et peut faciliter la collaboration des développeurs sur une base de code.

Dans ce tutoriel, nous allons explorer chacun des principes SOLID en détail, expliquer pourquoi ils sont importants et fournir des exemples de la manière dont vous pouvez les appliquer en pratique. À la fin de ce tutoriel, vous devriez avoir une bonne compréhension des principes SOLID et de la manière de les appliquer à vos projets de développement logiciel.

## **Qu'est-ce que le principe de responsabilité unique ?**

Le principe de responsabilité unique (SRP) stipule qu'**une classe ne devrait avoir qu'une seule raison de changer**, ou en d'autres termes, **elle ne devrait avoir qu'une seule responsabilité**. Cela signifie qu'une classe ne devrait avoir qu'un seul travail à faire, et elle devrait le faire bien.

Si une classe a trop de responsabilités, elle peut devenir difficile à comprendre, maintenir et modifier. Les changements apportés à une responsabilité peuvent involontairement affecter une autre responsabilité, entraînant des conséquences imprévues et des bugs. En suivant le SRP, nous pouvons créer un code plus modulaire, plus facile à comprendre et moins sujet aux erreurs.

Prenons un exemple qui viole le SRP :

```java
class Marker {
    String name;
    String color;
    int price;

    public Marker(String name, String color, int price) {
        this.name = name;
        this.color = color;
        this.price = price;
    }
}

```

Le code ci-dessus définit une classe `Marker` simple ayant trois variables d'instance - `name`, `color` et `price`.

```java
class Invoice {
    private Marker marker;
    private int quantity;

    public Invoice(Marker marker, int quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    public int calculateTotal() {
        return marker.price * this.quantity;
    }

    public void printInvoice() {
        // implémentation de l'impression
    }

    public void saveToDb() {
        // implémentation de la sauvegarde dans la base de données
    }
}
```

La classe `Invoice` ci-dessus viole le SRP car elle a plusieurs responsabilités - elle est responsable du calcul du montant total, de l'impression de la facture et de la sauvegarde de la facture dans la base de données. Par conséquent, si la logique de calcul change, comme l'ajout de taxes, la méthode `calculateTotal()` nécessiterait une modification. De même, si l'implémentation de l'impression ou de la sauvegarde dans la base de données change à un moment donné, la classe devrait être modifiée. 

Il existe plusieurs raisons pour lesquelles la classe doit être modifiée, ce qui pourrait entraîner une augmentation des coûts de maintenance et de la complexité.

Voici comment vous pouvez modifier le code pour suivre le SRP :

```java
class Invoice {
    private Marker marker;
    private int quantity;

    public Invoice(Marker marker, int quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    public int calculateTotal() {
        return marker.price * this.quantity;
    }
}

```

```java
class InvoiceDao {
    private Invoice invoice;

    public InvoiceDao(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToDb() {
        // implémentation de la sauvegarde dans la base de données
    }
}

```

```java
class InvoicePrinter {
    private Invoice invoice;

    public InvoicePrinter(Invoice invoice) {
        this.invoice = invoice;
    }

    public void printInvoice() {
        // implémentation de l'impression
    }
}

```

Dans cet exemple refactorisé, nous avons divisé les responsabilités de la classe `Invoice` en trois classes distinctes : `Invoice`, `InvoiceDao` et `InvoicePrinter`. 

La classe `Invoice` est responsable uniquement du calcul du montant total, et les responsabilités d'impression et de sauvegarde ont été déléguées à des classes distinctes. Cela rend le code plus modulaire, plus facile à comprendre et moins sujet aux erreurs.

## **Qu'est-ce que le principe ouvert-fermé ?**

Le principe ouvert-fermé (OCP) stipule que **les entités logicielles (classes, modules, fonctions, etc.) doivent être ouvertes à l'extension mais fermées à la modification**. Cela signifie que le comportement d'une entité logicielle peut être étendu sans modifier son code source.

L'OCP est essentiel car il favorise l'extensibilité et la maintenabilité des logiciels. En permettant aux entités logicielles d'être étendues sans modification, les développeurs peuvent ajouter de nouvelles fonctionnalités sans risquer de casser le code existant. Cela donne un code plus facile à maintenir, à étendre et à réutiliser.

Prenons à nouveau l'exemple précédent.

```java
class InvoiceDao {
    private Invoice invoice;

    public InvoiceDao(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToDb() {
        // implémentation de la sauvegarde dans la base de données
    }
}

```

La classe `InvoiceDao` a une seule responsabilité : sauvegarder la facture dans la base de données. Mais supposons qu'il y ait une nouvelle exigence pour sauvegarder la facture dans un fichier également. Une façon d'implémenter cette exigence serait de modifier la classe `InvoiceDao` existante en ajoutant une méthode `saveToFile()`. Mais cela viole le principe ouvert-fermé car il modifie le code existant qui a déjà été testé et est en production.

Pour suivre l'OCP, une meilleure solution serait de créer une interface `InvoiceDao` et de l'implémenter séparément pour la sauvegarde dans la base de données et dans un fichier comme montré ci-dessous :

```java
interface InvoiceDao {
    public void save(Invoice invoice);
}

class DatabaseInvoiceDao implements InvoiceDao {
    @Override
    public void save(Invoice invoice) {
        // implémentation de la sauvegarde dans la base de données
    }
}

class FileInvoiceDao implements InvoiceDao {
    @Override
    public void save(Invoice invoice) {
        // implémentation de la sauvegarde dans un fichier
    }
}

```

De cette manière, s'il y a une nouvelle exigence pour sauvegarder la facture dans un autre magasin de données, vous pouvez implémenter une nouvelle implémentation `InvoiceDao` sans modifier le code existant. Maintenant, l'interface `InvoiceDao` est ouverte à l'extension et fermée à la modification, ce qui suit l'OCP.

## **Qu'est-ce que le principe de substitution de Liskov ?**

Le principe de substitution de Liskov (LSP) stipule que **toute instance d'une classe dérivée doit être substituable à une instance de sa classe de base sans affecter la justesse du programme**. 

En d'autres termes, une classe dérivée doit se comporter comme sa classe de base dans tous les contextes. En termes plus simples, si la classe A est un sous-type de la classe B, vous devriez pouvoir remplacer B par A sans casser le comportement de votre programme.

L'importance du LSP réside dans sa capacité à garantir que le comportement d'un programme reste cohérent et prévisible lors de la substitution d'objets de différentes classes. La violation du LSP peut entraîner un comportement inattendu, des bugs et des problèmes de maintenabilité.

Prenons un exemple.

```java
interface Bike {
    void turnOnEngine();

    void accelerate();
}

```

Dans l'exemple donné, l'interface `Bike` a deux méthodes, `turnOnEngine()` et `accelerate()`. Deux classes implémentent cette interface, `Motorbike` et `Bicycle`.

```java
class Motorbike implements Bike {

    boolean isEngineOn;
    int speed;

    @Override
    public void turnOnEngine() {
        isEngineOn = true;
    }

    @Override
    public void accelerate() {
        speed += 5;
    }
}

```

`Motorbike` implémente correctement la méthode `turnOnEngine()`, car elle définit le booléen `isEngineOn` sur vrai. Elle implémente également correctement la méthode `accelerate()` en augmentant la `speed` de 5.

```java
class Bicycle implements Bike {

    boolean isEngineOn;
    int speed;

    @Override
    public void turnOnEngine() {
        throw new AssertionError("There is no engine!");
    }

    @Override
    public void accelerate() {
        speed += 5;
    }
}

```

Cependant, la classe `Bicycle` lève une `AssertionError` dans la méthode `turnOnEngine()` car elle n'a pas de moteur. Cela signifie qu'une instance de `Bicycle` ne peut pas être substituée à une instance de `Bike` sans casser le comportement du programme.

En d'autres termes, si la classe `Bicycle` est considérée comme un sous-type de l'interface `Bike`, alors selon le LSP, toute instance de `Bike` devrait être remplaçable par une instance de `Bicycle` sans altérer la justesse du programme. 

Mais dans ce cas, ce n'est pas vrai car `Bicycle` lève une `AssertionError` en essayant de démarrer le moteur. Par conséquent, le code viole le LSP.

## **Qu'est-ce que le principe de ségrégation des interfaces ?**

Le principe de ségrégation des interfaces (ISP) se concentre sur la conception d'interfaces spécifiques aux besoins de leurs clients. Il stipule qu'aucun client ne devrait être forcé de dépendre de méthodes qu'il n'utilise pas.

Le principe suggère que **au lieu de créer une grande interface qui couvre toutes les méthodes possibles, il est préférable de créer des interfaces plus petites et plus ciblées pour des cas d'utilisation spécifiques**. Cette approche donne des interfaces plus cohésives et moins couplées.

Considérons une interface `Vehicle` comme ci-dessous :

```java
interface Vehicle {
    void startEngine();
    void stopEngine();
    void drive();
    void fly();
}

```

Et puis vous avez une classe appelée `Car` qui implémente l'interface `Vehicle` :

```java
class Car implements Vehicle {

    @Override
    public void startEngine() {
        // implémentation
    }

    @Override
    public void stopEngine() {
        // implémentation
    }

    @Override
    public void drive() {
        // implémentation
    }

    @Override
    public void fly() {
        throw new UnsupportedOperationException("This vehicle cannot fly.");
    }
}

```

Dans cet exemple, l'interface `Vehicle` a trop de méthodes. La classe `Car` est forcée de toutes les implémenter, même si elles ne peuvent pas voler. Cela viole l'ISP car l'interface `Vehicle` n'est pas correctement ségrégée en interfaces plus petites basées sur des fonctionnalités connexes.

Comprenons comment vous pouvez suivre l'ISP ici. Supposons que vous refactorisez l'interface `Vehicle` en interfaces plus petites et plus ciblées :

```java
interface Drivable {
    void startEngine();
    void stopEngine();
    void drive();
}

interface Flyable {
    void fly();
}

```

Maintenant, vous pouvez avoir une classe appelée `Car` qui n'implémente que l'interface `Drivable` :

```java
class Car implements Drivable {

    @Override
    public void startEngine() {
        // implémentation
    }

    @Override
    public void stopEngine() {
        // implémentation
    }

    @Override
    public void drive() {
        // implémentation
    }
}

```

Et, grâce à la ségrégation des interfaces, vous pouvez avoir une autre classe appelée `Airplane` qui implémente à la fois les interfaces `Drivable` et `Flyable` :

```java
class Airplane implements Drivable, Flyable {

    @Override
    public void startEngine() {
        // implémentation
    }

    @Override
    public void stopEngine() {
        // implémentation
    }

    @Override
    public void drive() {
        // implémentation
    }

    @Override
    public void fly() {
        // implémentation
    }
}

```

Dans cet exemple, vous avez correctement ségrégé l'interface `Vehicle` en interfaces plus petites basées sur des fonctionnalités connexes. Cela adhère à l'ISP et rend votre code plus flexible et maintenable.

## **Qu'est-ce que le principe d'inversion des dépendances ?**

Le principe d'inversion des dépendances (DIP) stipule que **les modules de haut niveau ne doivent pas dépendre des modules de bas niveau, mais les deux doivent dépendre des abstractions**. Les abstractions ne doivent pas dépendre des détails - les détails doivent dépendre des abstractions. 

Ce principe vise à réduire le couplage entre les modules, à augmenter la modularité et à rendre le code plus facile à maintenir, à tester et à étendre.

Par exemple, considérons un scénario où vous avez une classe qui doit utiliser une instance d'une autre classe. Dans l'approche traditionnelle, la première classe créerait directement une instance de la deuxième classe, entraînant un couplage serré entre elles. Cela rend difficile la modification de l'implémentation de la deuxième classe ou le test indépendant de la première classe. 

Mais si vous appliquez le DIP, la première classe dépendrait d'une abstraction de la deuxième classe au lieu de l'implémentation. Cela rendrait possible le changement facile de l'implémentation et le test indépendant de la première classe.

Voici un exemple qui viole le DIP :

```java
class WeatherTracker {
    private String currentConditions;
    private Emailer emailer;

    public WeatherTracker() {
        this.emailer = new Emailer();
    }

    public void setCurrentConditions(String weatherDescription) {
        this.currentConditions = weatherDescription;
        if (weatherDescription == "rainy") {
            emailer.sendEmail("It is rainy");
        }
    }
}

class Emailer {
    public void sendEmail(String message) {
        System.out.println("Email sent: " + message);
    }
}

```

Dans cet exemple, la classe `WeatherTracker` crée directement une instance de la classe `Emailer`, ce qui la couple étroitement à l'implémentation. Cela rend difficile la modification de l'implémentation de la classe `Emailer` ou le test indépendant de la classe `WeatherTracker`.

Voici un exemple de la manière d'appliquer le DIP au code ci-dessus :

```java
interface Notifier {
    public void alertWeatherConditions(String weatherDescription);
}

class WeatherTracker {
    private String currentConditions;
    private Notifier notifier;

    public WeatherTracker(Notifier notifier) {
        this.notifier = notifier;
    }

    public void setCurrentConditions(String weatherDescription) {
        this.currentConditions = weatherDescription;
        if (weatherDescription == "rainy") {
            notifier.alertWeatherConditions("It is rainy");
        }
    }
}

class Emailer implements Notifier {
    public void alertWeatherConditions(String weatherDescription) {
        System.out.println("Email sent: " + weatherDescription);
    }
}

class SMS implements Notifier {
    public void alertWeatherConditions(String weatherDescription) {
        System.out.println("SMS sent: " + weatherDescription);
    }
}

```

Dans cet exemple, nous avons créé une interface `Notifier` qui définit la méthode `alertWeatherConditions`. La classe `WeatherTracker` dépend maintenant de cette interface au lieu de la classe `Emailer`, ce qui permet de changer facilement l'implémentation et de tester la classe `WeatherTracker` indépendamment. 

Nous avons également créé deux implémentations de l'interface `Notifier`, `Emailer` et `SMS`, pour démontrer comment vous pouvez changer l'implémentation de la classe `WeatherTracker` sans affecter son comportement.

## **Conclusion**

Dans cet article, vous avez appris les principes SOLID qui sont une partie très importante des principes généraux de conception. 

En appliquant ces principes dans vos projets de développement logiciel, vous pouvez créer un code plus facile à maintenir, à étendre et à modifier, conduisant à des logiciels plus robustes, flexibles et réutilisables. Cela conduira également à une meilleure collaboration entre les membres de l'équipe, car le code devient plus modulaire et plus facile à travailler.

> Pour plus de tutoriels comme celui-ci, vous pouvez suivre [mon blog personnel](https://blog.ashutoshkrris.in/).