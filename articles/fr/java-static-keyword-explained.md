---
title: Le mot-clé static en Java expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T22:36:00.000Z'
originalURL: https://freecodecamp.org/news/java-static-keyword-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cde740569d1a4ca34a0.jpg
tags:
- name: Java
  slug: java
- name: toothbrush
  slug: toothbrush
seo_title: Le mot-clé static en Java expliqué avec des exemples
seo_desc: 'What does static mean?

  When you declare a variable or a method as static, it belongs to the class, rather
  than a specific instance. This means that only one instance of a static member exists,
  even if you create multiple objects of the class, or if y...'
---

# **Que signifie static ?**

Lorsque vous déclarez une variable ou une méthode comme static, elle appartient à la classe, plutôt qu'à une instance spécifique. Cela signifie qu'une seule instance d'un membre static existe, même si vous créez plusieurs objets de la classe, ou si vous n'en créez aucun. Elle sera partagée par tous les objets.

Le mot-clé static peut être utilisé avec des variables, des méthodes, des blocs de code et des classes imbriquées.

## **Variables statiques**

**_Exemple :_**

```java
public class Counter {
  public static int COUNT = 0;
  Counter() {
    COUNT++;
  }
}
```

La variable `COUNT` sera partagée par tous les objets de cette classe. Lorsque nous créons des objets de notre classe Counter dans main, et accédons à la variable static.

```java
public class MyClass {
  public static void main(String[] args) {
    Counter c1 = new Counter();
    Counter c2 = new Counter();
    System.out.println(Counter.COUNT);
  }
}
// Affiche "2"
```

La sortie est 2, car la variable `COUNT` est static et s'incrémente de un à chaque fois qu'un nouvel objet de la classe Counter est créé. Vous pouvez également accéder à la variable static en utilisant n'importe quel objet de cette classe, comme `c1.COUNT`.

## **Méthodes statiques**

Une méthode static appartient à la classe plutôt qu'aux instances. Ainsi, elle peut être appelée sans créer d'instance de la classe. Elle est utilisée pour modifier le contenu static de la classe. Il y a certaines restrictions pour les méthodes statiques :

1. Une méthode static ne peut pas utiliser les membres non-statiques (variables ou fonctions) de la classe.
2. Une méthode static ne peut pas utiliser les mots-clés `this` ou `super`.

**_Exemple :_**

```java
public class Counter {
  public static int COUNT = 0;
  Counter() {
    COUNT++;
  }

  public static void increment(){
    COUNT++;
  }
}
```

Les méthodes statiques peuvent également être appelées à partir d'une instance de la classe.

```java
public class MyClass {
  public static void main(String[] args) {
    Counter.increment();
    Counter.increment();
    System.out.println(Counter.COUNT);
  }
}
// Affiche "2"
```

La sortie est 2 car elle s'incrémente grâce à la méthode static `increment()`. Comme pour les variables statiques, les méthodes statiques peuvent également être accessibles via des variables d'instance.

## **Blocs statiques**

Les blocs de code statiques sont utilisés pour initialiser les variables statiques. Ces blocs sont exécutés immédiatement après la déclaration des variables statiques.

**_Exemple :_**

```java
public class Saturn {
  public static final int MOON_COUNT;

  static {
    MOON_COUNT = 62;
  }
}
```

```java
public class Main {
  public static void main(String[] args) {
    System.out.println(Saturn.MOON_COUNT);
  }
}
// Affiche "62"
```

La sortie est 62, car la variable `MOON_COUNT` se voit attribuer cette valeur dans le bloc static.

## **Classes imbriquées statiques**

Une classe peut avoir une classe imbriquée static qui peut être accessible en utilisant le nom de la classe externe.

**_Exemple :_**

```java
public class Outer {

  public Outer() {
  }

  public static class Inner {
    public Inner() {
    }
  }
}
```

Dans l'exemple ci-dessus, la classe `Inner` peut être directement accessible en tant que membre static de la classe `Outer`.

```java
public class Main {
  public static void main(String[] args) {
    Outer.Inner inner = new Outer.Inner();
  }
}
```

L'un des cas d'utilisation des classes imbriquées statiques est le [Builder Pattern](https://en.wikipedia.org/wiki/Builder_pattern#Java) populaire en Java.