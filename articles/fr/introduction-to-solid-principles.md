---
title: Quels sont les principes SOLID en Java ? Expliqués avec des exemples de code
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-06-24T15:45:17.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-solid-principles
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/kozjat-mlsSgJ6LiP4-unsplash.jpg
tags:
- name: Java
  slug: java
- name: solid
  slug: solid
seo_title: Quels sont les principes SOLID en Java ? Expliqués avec des exemples de
  code
seo_desc: 'In this article, you''ll learn about the SOLID principles. You''ll gain
  an understanding of each principle along with Java code examples.

  SOLID principles are a set of five design principles used in object-oriented programming.
  Adhering to these princi...'
---

Dans cet article, vous apprendrez les principes SOLID. Vous comprendrez chaque principe avec des exemples de code Java.

Les principes SOLID sont un ensemble de cinq principes de conception utilisés en programmation orientée objet. Le respect de ces principes vous aidera à développer des logiciels robustes. Ils rendront votre code plus efficace, lisible et maintenable.

SOLID est un acronyme qui signifie :
- Principe de responsabilité unique
- Principe ouvert/fermé
- Principe de substitution de Liskov
- Principe de ségrégation des interfaces
- Principe d'inversion des dépendances

## Principe de responsabilité unique
Le principe de responsabilité unique stipule que chaque classe doit avoir une seule responsabilité, une seule raison de changer.

```java
public class Employee{
  public String getDesignation(int employeeID){ // }
  public void updateSalary(int employeeID){ // }
  public void sendMail(){ // }
}
```

Dans l'exemple ci-dessus, la classe `Employee` a quelques comportements spécifiques à la classe employé comme `getDesignation` et `updateSalary`.

De plus, elle a également une autre méthode nommée `sendMail` qui s'écarte de la responsabilité de la classe `Employee`.

Ce comportement n'est pas spécifique à cette classe, et l'avoir viole le principe de responsabilité unique. Pour surmonter cela, vous pouvez déplacer la méthode `sendMail` vers une classe séparée.

Voici comment :

```java
public class Employee{
  public String getDesignation(int employeeID){ // }
  public void updateSalary(int employeeID){ // }
}

public class NotificationService {
    public void sendMail() { // }
}
```

## Principe ouvert/fermé

Selon le principe ouvert/fermé, les composants doivent être ouverts pour l'extension, mais fermés pour la modification. Pour comprendre ce principe, prenons un exemple de classe qui calcule l'aire d'une forme.

```java
public class AreaCalculator(){
  public double area(Shape shape){
    double areaOfShape;
    if(shape instanceof Square){
        // calculer l'aire du carré
    } else if(shape instanceof Circle){
        // calculer l'aire du cercle
    }
    return areaOfShape;
  }
```

Le problème avec l'exemple ci-dessus est que si une nouvelle instance de type `Shape` pour laquelle vous devez calculer l'aire dans le futur, vous devez modifier la classe ci-dessus en ajoutant un autre bloc conditionnel `else-if`. Vous finirez par faire cela pour chaque nouvel objet du type `Shape`.

Pour surmonter cela, vous pouvez créer une interface et faire en sorte que chaque `Shape` implémente cette interface. Ensuite, chaque classe peut fournir sa propre implémentation pour calculer l'aire. Cela rendra votre programme facilement extensible à l'avenir.

```java
interface IAreaCalculator(){
  double area();
}

class Square implements IAreaCalculator{
  @Override
  public double area(){
    System.out.println("Calcul de l'aire pour le carré");
    return 0.0;
   }
}

class Circle implements IAreaCalculator{
  @Override
  public double area(){
    System.out.println("Calcul de l'aire pour le cercle");
    return 0.0;
   }
}
```

## Principe de substitution de Liskov

Le principe de substitution de Liskov stipule que vous devez pouvoir remplacer un objet de superclasse par un objet de sous-classe sans affecter la justesse du programme.

```java
abstract class Bird{
   abstract void fly();
}

class Eagle extends Bird {
   @Override
   public void fly() { // une certaine implémentation }
}

class Ostrich extends Bird {
   @Override
   public void fly() { // implémentation factice }
}
```

Dans l'exemple ci-dessus, les classes `Eagle` et `Ostrich` étendent toutes deux la classe `Bird` et remplacent la méthode `fly()`. Cependant, la classe `Ostrich` est forcée de fournir une implémentation factice car elle ne peut pas voler, et donc elle ne se comporte pas de la même manière si nous remplaçons l'objet de la classe `Bird` par celui-ci.

Cela viole le principe de substitution de Liskov. Pour résoudre cela, nous pouvons créer une classe séparée pour les oiseaux qui peuvent voler et faire en sorte que `Eagle` l'étende, tandis que les autres oiseaux peuvent étendre une classe différente, qui n'inclura aucun comportement `fly`.

```java
abstract class FlyingBird{
   abstract void fly();
}

abstract class NonFlyingBird{
   abstract void doSomething();
}

class Eagle extends FlyingBird {
   @Override
   public void fly() { // une certaine implémentation }
}

class Ostrich extends NonFlyingBird {
   @Override
   public void doSomething() { // une certaine implémentation }
}
```

## Principe de ségrégation des interfaces

Selon le principe de ségrégation des interfaces, vous devez construire des interfaces petites et ciblées qui ne forcent pas le client à implémenter un comportement dont il n'a pas besoin.

Un exemple simple serait d'avoir une interface qui calcule à la fois l'aire et le volume d'une forme.

```java
interface IShapeAreaCalculator(){
  double calculateArea();
  double calculateVolume();
}

class Square implements IShapeAreaCalculator{
  double calculateArea(){ // calculer l'aire }
  double calculateVolume(){ // implémentation factice }
}
```

Le problème avec cela est que si une forme `Square` implémente cela, alors elle est forcée d'implémenter la méthode `calculateVolume()`, dont elle n'a pas besoin.

D'autre part, un `Cube` peut implémenter les deux. Pour surmonter cela, nous pouvons ségréguer l'interface et avoir deux interfaces séparées : une pour calculer l'aire et une autre pour calculer le volume. Cela permettra aux formes individuelles de décider quoi implémenter.

```java
interface IAreaCalculator {
    double calculateArea();
}

interface IVolumeCalculator {
    double calculateVolume();
}

class Square implements IAreaCalculator {
    @Override
    public double calculateArea() { // calculer l'aire }
}

class Cube implements IAreaCalculator, IVolumeCalculator {
    @Override
    public double calculateArea() { // calculer l'aire }

    @Override
    public double calculateVolume() {// calculer le volume }
}
```

## Principe d'inversion des dépendances

Dans le principe d'inversion des dépendances, les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. En d'autres termes, vous devez suivre l'abstraction et assurer un couplage lâche.

```java
public interface Notification {
    void notify();
}

public class EmailNotification implements Notification {
    public void notify() {
        System.out.println("Envoi de notification par email");
    }
}

public class Employee {
    private EmailNotification emailNotification; 
    public Employee(EmailNotification emailNotification) {
        this.emailNotification = emailNotification;
    }
    public void notifyUser() {
        emailNotification.notify();
    }
}
```

Dans l'exemple donné, la classe `Employee` dépend directement de la classe `EmailNotification`, qui est un module de bas niveau. Cela viole le principe d'inversion des dépendances.

```java
public interface Notification{
  public void notify();
}

public class Employee{
  private Notification notification;
  public Employee(Notification notification){
      this.notification = notification;
  }
  public void notifyUser(){
    notification.notify();
  }
 }
 
 public class EmailNotification implements Notification{
    public void notify(){
        //implémenter la notification par email 
    }
 }
 
 public static void main(String [] args){
    Notification notification = new EmailNotification();
    Employee employee = new Employee(notification);
    employee.notifyUser();
 }
```

Dans l'exemple ci-dessus, nous avons assuré un couplage lâche. `Employee` ne dépend d'aucune implémentation concrète, mais dépend uniquement de l'abstraction (interface de notification).

Si nous devons changer le mode de notification, nous pouvons créer une nouvelle implémentation et la passer à `Employee`.

## Conclusion

En conclusion, nous avons couvert l'essence des principes SOLID à travers des exemples simples dans cet article.

Ces principes constituent les blocs de construction pour développer des applications hautement extensibles et réutilisables.

Connectons-nous sur [LinkedIn](https://www.linkedin.com/in/abaradwaj/)