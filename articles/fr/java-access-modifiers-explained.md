---
title: Les modificateurs d'accès en Java expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-13T21:42:00.000Z'
originalURL: https://freecodecamp.org/news/java-access-modifiers-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c25740569d1a4ca3049.jpg
tags:
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Les modificateurs d'accès en Java expliqués
seo_desc: 'What are Access Modifiers?

  Have you ever wanted to define how people would access some of your properties?
  You would not want anyone using your underwear. However, your close friends and
  relatives can use your sweater and maybe your car.

  Similarly to...'
---

# **Qu'est-ce que les modificateurs d'accès ?**

Avez-vous déjà voulu définir comment les gens pourraient accéder à certaines de vos propriétés ? Vous ne voudriez pas que quelqu'un utilise vos sous-vêtements. Cependant, vos amis proches et vos parents peuvent utiliser votre pull et peut-être votre voiture.

De manière similaire à la façon dont vous définissez un niveau d'accès à vos possessions, Java contrôle également l'accès. Vous souhaitez définir le niveau d'accès pour les variables, les méthodes et les classes en fonction des autres classes que vous souhaitez y accéder.

Java fournit 4 niveaux de modificateurs d'accès. Cela signifie que vous pouvez modifier l'accès à une variable, une méthode ou une classe de 4 manières. Ces 4 manières sont private, public, protected et default.

Ces modificateurs d'accès peuvent être appliqués aux champs, méthodes et classes (les classes sont un cas spécial, nous les examinerons à la fin de cet article). Voici un aperçu rapide<sup>1</sup> des niveaux d'accès pour chaque modificateur d'accès :

### Tableau de référence des modificateurs d'accès :

![Access Modifiers Table](https://i.imgur.com/zoMspyn.png)

## Modificateur d'accès Private

Permet à une variable ou une méthode d'être accessible uniquement dans la classe dans laquelle elle a été créée. Aucune autre classe en dehors de la classe qui a créé la variable ou la méthode ne peut y accéder. Cela est étroitement similaire à vos organes internes. Ils ne sont accessibles qu'au propriétaire. Pour rendre une variable ou une méthode privée, il suffit d'ajouter le mot-clé private avant le type de la variable ou de la méthode. Utilisons private dans un exemple de code. Si une banque souhaite offrir un taux d'intérêt de 10 % sur ses prêts, elle s'assurera que la variable de taux d'intérêt (supposons `int int_rate ;`) reste privée afin qu'aucune autre classe ne tente d'y accéder et de la modifier. Par exemple ;

`private String name;`  
L'exemple ci-dessus crée une variable appelée name et garantit qu'elle n'est accessible que dans la classe à partir de laquelle elle a été créée.

Un autre exemple pour une méthode est

```java
private void setAge(){
System.out.println("Set Age");
}
```

L'exemple ci-dessus garantit que la méthode setAge est accessible uniquement dans la classe à partir de laquelle elle a été créée et nulle part ailleurs.

## Modificateur d'accès Public

Le modificateur d'accès public est le contraire direct du modificateur d'accès private. Une classe, méthode ou variable peut être déclarée comme public et cela signifie qu'elle est accessible à partir de n'importe quelle classe. Le modificateur d'accès public peut être comparé à une école publique où n'importe qui peut demander l'admission et être admis.

Une classe, méthode ou variable publique peut être accessible à partir de n'importe quelle autre classe à tout moment.

Par exemple, pour déclarer une classe comme public, il suffit de :

```java
public class Animal{

}
```

Ainsi, la classe Animal peut être accessible par n'importe quelle autre classe.

```java
public int age;
public int getAge(){
}
```

Ci-dessus sont des façons de spécifier une variable et une méthode comme public.

## Le modificateur d'accès par défaut

Le modificateur d'accès par défaut est différent de tous les autres modificateurs d'accès en ce sens qu'il n'a pas de mot-clé. Pour utiliser le modificateur d'accès par défaut, il suffit de ne pas utiliser les autres modificateurs d'accès et cela signifie simplement que vous utilisez un modificateur d'accès par défaut.

Par exemple, pour utiliser le modificateur d'accès par défaut pour une classe, vous utilisez

```java
class Bird{
}
```

Cela signifie simplement que vous utilisez le modificateur d'accès par défaut. Le modificateur d'accès par défaut permet à une variable, une méthode ou une classe d'être accessible par d'autres classes au sein du même package. Un package est une collection de classes liées dans un répertoire de fichiers. Pour plus d'informations sur les packages, consultez la section sur les packages.

Toute variable, méthode ou classe déclarée pour utiliser le modificateur d'accès par défaut ne peut pas être accessible par une autre classe en dehors du package à partir duquel elle a été déclarée.

```java
int age;
void setNewAge(){
}
```

Ci-dessus sont quelques façons d'utiliser le modificateur d'accès par défaut pour une variable ou une méthode. N'oubliez pas, le modificateur d'accès par défaut n'a pas de mot-clé. L'absence des 3 autres modificateurs d'accès signifie que vous utilisez le modificateur d'accès par défaut.

## Modificateur d'accès Protected

Le modificateur d'accès protected est étroitement lié au modificateur d'accès par défaut. Le modificateur d'accès protected a les propriétés du modificateur d'accès par défaut mais avec une légère amélioration.

Une variable et une méthode sont les seules à utiliser le modificateur d'accès protected. La légère amélioration est qu'une classe en dehors du package de la classe à partir de laquelle la variable ou la méthode a été déclarée peut accéder à ladite variable ou méthode. Cela n'est possible que si elle hérite de la classe, cependant.

La classe d'un autre package qui peut voir les variables ou méthodes protected doit avoir étendu la classe qui a créé les variables ou méthodes.

Notez que sans l'avantage de l'héritage, un modificateur d'accès par défaut a exactement le même accès qu'un modificateur d'accès protected.

Des exemples d'utilisation du modificateur d'accès protected sont présentés ci-dessous :

```java
protected int age;
protected String getName(){
  return "My Name is You";
}
```

## Modificateurs d'accès sur les classes

Par défaut, les classes ne peuvent avoir que 2 modificateurs :

* public
* aucun modificateur (modificateur par défaut)

Cela signifie que les classes ne peuvent jamais être définies comme `private` ou `protected` ?

Cela est logique, pourquoi voudriez-vous créer une classe privée ? Aucune autre classe ne pourrait l'utiliser. Mais parfois, vous pouvez intégrer une classe dans une autre classe. Ces classes spéciales, `inner classes`, peuvent être définies comme private ou protected afin que seule leur classe environnante puisse y accéder :

```java
public class Car {
    private String brand;
    private Engine engine;
    // ...    
    private class Engine {
        // ...
    }
}
```

Dans l'exemple ci-dessus, seule la classe `Car` peut utiliser la classe `Engine`. Cela peut être utile dans certains cas.

Les autres classes ne peuvent jamais être définies comme `protected` ou `private`, car cela n'a pas de sens. Le modificateur d'accès `protected` est utilisé pour rendre les choses `package-private` mais avec l'option d'être accessible aux sous-classes. Il n'existe pas de concept tel que sous-packages ou héritage de package en Java.