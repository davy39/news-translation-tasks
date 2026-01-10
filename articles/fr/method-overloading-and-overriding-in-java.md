---
title: Surcharge de méthode vs Redéfinition de méthode en Java – Quelle est la différence
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-17T17:26:47.000Z'
originalURL: https://freecodecamp.org/news/method-overloading-and-overriding-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Method-Overloading-and-Overriding-in-Java-copy.jpeg
tags:
- name: Java
  slug: java
seo_title: Surcharge de méthode vs Redéfinition de méthode en Java – Quelle est la
  différence ?
seo_desc: "By Mikael Lassa\nIn Java, method overloading and method overriding both\
  \ refer to creating different methods that share the same name. \nWhile the two\
  \ concepts share some similarities, they are distinct notions with markedly different\
  \ use cases. Having ..."
---

Par Mikael Lassa

En Java, la surcharge de méthode (method overloading) et la redéfinition de méthode (method overriding) consistent toutes deux à créer différentes méthodes partageant le même nom. 

Bien que ces deux concepts partagent des similitudes, ce sont des notions distinctes avec des cas d'utilisation très différents. Il est important de bien les maîtriser pour acquérir des bases solides en Java. 

Dans cet article, nous explorerons les règles clés de la surcharge et de la redéfinition de méthode, ainsi que les différences entre les deux. 

## Qu'est-ce que la surcharge de méthode en Java ?

Surcharger une méthode signifie, en termes simples, créer une méthode différente avec le même nom dans la même classe, mais avec une liste de paramètres différente. 

Il existe de nombreux cas où vous pourriez avoir besoin de gérer différents types d'entrées pour la même opération, et la surcharge de méthode est un moyen de gérer de tels cas. 

Par exemple, supposons que vous souhaitiez créer une méthode qui effectue l'addition de deux nombres. Ce calcul est conçu pour renvoyer un nombre en sortie. Si votre méthode gère des paramètres de type `int`, tenter de l'appeler en passant des valeurs de type `double` comme arguments entraînera une erreur de compilation. 

Pour cette raison, vous pourriez vouloir surcharger la méthode en créant une nouvelle version de celle-ci capable de gérer un type d'entrée différent (dans ce cas, de type `double`) : 

```java
public class Calculator {

    public int sum(int a, int b) {
        return a + b;
    }

    public double sum(double a, double b) {
        return a + b;
   }
}
```

Dans l'exemple ci-dessus, la méthode `sum()` est surchargée car elle est définie plus d'une fois dans la même classe, mais avec une liste de paramètres différente. 

Une méthode peut également être surchargée en modifiant le nombre de paramètres. Sur cette base, les méthodes suivantes sont également des exemples valides de la manière dont la méthode `sum()` peut être surchargée, à condition qu'elles soient placées dans la même classe : 

```java
public int sum(int a, int b, int c) {
        return a + b + c;
    }
    
protected void sum() {
        System.out.print("Rien à additionner");
    }
```

Notez que, comme dans certains des exemples ci-dessus, vous pouvez également modifier le type de retour ou le modificateur d'accès, mais cela n'est pas obligatoire. 

### Règles clés de la surcharge de méthode

Retenez ces règles lors de la surcharge d'une méthode :

* Les méthodes surchargées et surchargeantes doivent être dans la même classe (Note : cela inclut toutes les méthodes héritées, même implicitement, d'une superclasse).
* Les paramètres de la méthode doivent changer : le nombre ou le type de paramètres doit être différent dans les deux méthodes.
* Le type de retour peut être modifié librement.
* Le modificateur d'accès (`public`, `private`, etc.) peut être modifié librement.
* Les exceptions levées, le cas échéant, peuvent être modifiées librement.

## Qu'est-ce que la redéfinition de méthode en Java ?

La redéfinition de méthode consiste à redéfinir dans une sous-classe une méthode qui existe déjà dans la superclasse. 

Lorsque vous appelez une méthode redéfinie à l'aide d'un objet du type de la sous-classe, Java utilise l'implémentation de la méthode dans la sous-classe plutôt que celle de la superclasse. Pour cette raison, il est important de comprendre le concept d'héritage en Java pour bien saisir la redéfinition de méthode. 

En général, toute sous-classe peut redéfinir n'importe quelle méthode d'une superclasse, à moins qu'une méthode ne soit marquée avec les mots-clés `final` ou `static`. La méthode de redéfinition ne doit pas modifier le nom ni la liste des paramètres de la méthode redéfinie. 

Bien que ce ne soit pas obligatoire, il est recommandé d'utiliser l'annotation `@Override` lors de la redéfinition d'une méthode : cette annotation vérifiera que la méthode est correctement redéfinie et vous avertira si ce n'est pas le cas. 

Dans l'exemple suivant, vous verrez une classe `Car` qui étend la classe `Vehicle`. La classe `Car` redéfinit la méthode `move()` de la superclasse, et cela est explicité par l'utilisation de l'annotation `@Override`. Les deux méthodes sont implémentées différemment dans le corps de la méthode.

```java
class Vehicle {
    public void move() {
        System.out.println("Le véhicule se déplace");
    }
}

class Car extends Vehicle {
    @Override
    public void move() {
        System.out.println("La voiture se déplace");
    }
}
```

Le choix de la version de `move()` qui sera appelée est basé sur le type d'objet sur lequel la méthode est appelée. Notez que la version de la méthode redéfinie qui est appelée est déterminée à l'exécution (runtime) et est basée sur le type de l'objet, et non sur la référence de l'objet.

Ceci est illustré dans l'exemple suivant, particulièrement lors du troisième appel à `move()` : bien que la méthode soit appelée sur une référence d'objet de type `Vehicle`, l'objet réel est de type `Car`. Le type de l'objet ici est déterminé à l'exécution, et la version de la méthode appelée est donc celle de la sous-classe `Car`. 

```java
public static void main(String[] args) {
        
        Vehicle vehicle = new Vehicle();
        vehicle.move();     // Affiche : Le véhicule se déplace

        Car car = new Car();
        car.move();     // Affiche : La voiture se déplace

        Vehicle secondVehicle = new Car();
        secondVehicle.move();     // Affiche : La voiture se déplace
}
```

### Règles clés de la redéfinition de méthode

Retenez ces règles lors de la redéfinition d'une méthode :

* La liste des paramètres ne doit pas changer : la méthode de redéfinition doit prendre le même nombre et le même type de paramètres que la méthode redéfinie – sinon, vous seriez simplement en train de surcharger la méthode.
* Le type de retour ne doit pas changer (Note : si la méthode renvoie un objet, une sous-classe de cet objet est autorisée comme type de retour).
* Le modificateur d'accès doit être soit identique, soit moins restrictif (par exemple, si la méthode redéfinie est `protected`, vous pouvez déclarer la méthode de redéfinition comme `public`, mais pas `private`).
* Les exceptions contrôlées (checked exceptions) levées, le cas échéant, peuvent être supprimées ou réduites par la méthode de redéfinition. Cela signifie que la méthode de redéfinition peut lever la même exception contrôlée que la méthode redéfinie, ou une sous-classe de cette exception, mais pas une exception plus large. Cette restriction ne s'applique pas aux exceptions non contrôlées (unchecked exceptions).

## Conclusion

Dans cet article, nous avons exploré les principales règles de la surcharge et de la redéfinition de méthode en Java. Vous avez vu que l'objectif principal de la surcharge d'une méthode est de modifier sa liste de paramètres afin d'implémenter un comportement différent basé sur les arguments qui lui sont passés. 

La redéfinition, en revanche, consiste à redéfinir la même méthode, avec la même liste de paramètres, dans une sous-classe afin d'adapter son comportement aux besoins de la sous-classe. 

Ces concepts sont liés à certains des piliers de la programmation orientée objet, tels que l'héritage et le polymorphisme, ils sont donc fondamentaux pour maîtriser Java. Ils peuvent prêter à confusion, surtout pour les débutants, mais une bonne compréhension des règles et des utilisations de ces concepts devrait aider les développeurs à écrire un code plus efficace et plus lisible. 

Si vous souhaitez lire d'autres de mes articles, vous pouvez consulter mon [blog](https://medium.com/@mikael.lassa).