---
title: Comment initialiser une liste Java - Initialisation d'une liste de chaînes
  en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-14T14:30:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-initialize-a-java-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Shittu-Olumide-How-to-Initialize-a-Java-List
seo_title: Comment initialiser une liste Java - Initialisation d'une liste de chaînes
  en Java
---

List-of-String-Initialization-in-Java.png
étiquettes:
- nom: Java
  slug: java
seo_title: null
seo_desc: 'Par Shittu Olumide

  Java est un langage de programmation populaire largement utilisé pour développer des applications robustes et évolutives. L'une des structures de données essentielles en Java est une liste, qui permet aux développeurs de stocker et de manipuler une collection d'éléments.

Dans...'
---

Par Shittu Olumide

Java est un langage de programmation populaire largement utilisé pour développer des applications robustes et évolutives. L'une des structures de données essentielles en Java est une liste, qui permet aux développeurs de stocker et de manipuler une collection d'éléments.

L'initialisation d'une liste en Java est une étape cruciale dans le processus de développement, car elle définit l'état initial de la liste et la prépare pour les opérations ultérieures. Il existe diverses façons d'initialiser une liste en Java, et le choix dépend des exigences spécifiques du projet.

Dans cet article, nous allons explorer les différentes méthodes pour initialiser une liste Java et fournir des exemples pour illustrer leur utilisation. Que vous soyez débutant ou développeur Java expérimenté, ce guide vous aidera à comprendre les meilleures pratiques pour initialiser une liste Java et améliorer les performances de votre application.

En Java, il existe différentes façons d'initialiser une liste :

1. En utilisant le constructeur `ArrayList`.
2. En utilisant la méthode `add()`.
3. En utilisant la méthode `Arrays.asList()`.
4. En utilisant la méthode `Stream.of()`.

Examinons de plus près ces méthodes.

## Comment initialiser une liste en utilisant le constructeur `ArrayList`

En Java, la classe `ArrayList` est une implémentation de tableau dynamique de l'interface `List`, permettant d'ajouter et de supprimer des éléments de la liste selon les besoins. La classe `ArrayList` fournit plusieurs constructeurs pour créer une instance de la classe.

La syntaxe pour créer un objet `ArrayList` sans capacité initiale est :

```java
ArrayList<Object> list = new ArrayList<Object>();
```

Le constructeur sans arguments crée une liste vide avec une capacité initiale de 10 éléments. Si la liste dépasse cette capacité, la classe `ArrayList` augmente automatiquement la capacité en créant un nouveau tableau avec une taille plus grande et en copiant les éléments de l'ancien tableau vers le nouveau tableau.

Alternativement, nous pouvons créer un objet `ArrayList` avec une capacité initiale en utilisant le constructeur avec un argument entier unique :

```java
ArrayList<Object> list = new ArrayList<Object>(capacity);
```

où `capacity` est la capacité initiale de la liste.

Pour initialiser une `List` avec des valeurs, nous pouvons utiliser le constructeur qui prend une `Collection` comme argument. Nous pouvons passer n'importe quel objet de collection qui implémente l'interface `Collection` à ce constructeur, comme un autre `ArrayList` ou un `LinkedList`. Les éléments de la collection sont ajoutés au nouvel `ArrayList` dans l'ordre où ils apparaissent dans la collection.

Voici un exemple de la façon de créer un `ArrayList` et de l'initialiser avec des valeurs en utilisant le constructeur qui prend une `Collection` :

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Example {
    public static void main(String[] args) {
        // créer un tableau d'entiers
        Integer[] array = {1, 2, 3, 4, 5};

        // créer une liste à partir du tableau
        ArrayList<Integer> list = new ArrayList<Integer>(Arrays.asList(array));

        // imprimer la liste
        System.out.println(list); // [1, 2, 3, 4, 5]
    }
}
```

Dans cet exemple, nous créons un tableau d'entiers, puis nous le passons à la méthode `Arrays.asList()` pour créer un objet `List`. Nous passons ensuite cet objet `List` au constructeur `ArrayList` pour créer un nouvel `ArrayList` avec les mêmes éléments que le tableau d'origine. Enfin, nous imprimons le contenu de la liste en utilisant la méthode `System.out.println()`.

## Comment initialiser une liste en utilisant la méthode `add()`

La méthode `add()` est une méthode couramment utilisée en Java qui est utilisée pour ajouter des éléments à une collection ou à une liste. Cette méthode est disponible pour plusieurs types de collections en Java, y compris List, Set et Map. La méthode `add()` prend un seul argument, qui est l'élément qui doit être ajouté à la collection.

En ce qui concerne l'ajout d'éléments à une liste Java, la méthode `add()` est particulièrement utile. Les listes en Java sont des collections ordonnées qui peuvent contenir des doublons. La méthode `add()` peut être utilisée pour ajouter des éléments à la fin d'une liste, ce qui en fait un moyen pratique d'initialiser une liste avec certaines valeurs initiales.

Voici un exemple de la façon d'utiliser la méthode `add()` pour initialiser une liste Java :

```java
import java.util.ArrayList;
import java.util.List;

public class ListExample {
    public static void main(String[] args) {
        // créer une nouvelle ArrayList
        List<String> myList = new ArrayList<>();

        // ajouter des éléments à la liste en utilisant la méthode add()
        myList.add("apple");
        myList.add("banana");
        myList.add("cherry");

        // imprimer le contenu de la liste
        System.out.println(myList);
    }
}
```

Dans cet exemple, nous créons d'abord une nouvelle ArrayList appelée `myList`. Nous utilisons ensuite la méthode `add()` pour ajouter trois chaînes ("apple", "banana" et "cherry") à la fin de la liste. Enfin, nous imprimons le contenu de la liste en utilisant la méthode `System.out.println()`.

Lorsque nous exécutons ce programme, la sortie sera :

```
[apple, banana, cherry]
```

## Comment initialiser une liste en utilisant la méthode `Arrays.asList()`

La méthode `Arrays.asList()` est une méthode intégrée en Java qui convertit un tableau en une liste. Cette méthode prend un tableau comme argument et retourne un objet List. L'objet List retourné par la méthode `Arrays.asList()` est une liste de taille fixe, ce qui signifie que nous ne pouvons pas ajouter ou supprimer d'éléments.

Pour utiliser la méthode `Arrays.asList()` pour initialiser une liste Java, nous pouvons suivre ces étapes :

Tout d'abord, déclarer un tableau d'éléments avec lesquels nous voulons initialiser la liste. Par exemple, supposons que nous voulons initialiser une liste avec trois éléments : "apple", "banana" et "orange". Nous pouvons déclarer un tableau comme suit :

```java
String[] fruits = {"apple", "banana", "orange"};
```

Ensuite, appeler la méthode `Arrays.asList()` et passer le tableau comme argument. Cela retournera un objet List contenant les éléments du tableau.

```java
List<String> fruitList = Arrays.asList(fruits);
```

Nous pouvons maintenant utiliser l'objet `fruitList` pour accéder aux éléments de la liste. Par exemple, nous pouvons itérer sur la liste et imprimer chaque élément :

```java
for (String fruit : fruitList) {
    System.out.println(fruit);
}
```

Sortie :

```
apple
banana
orange
```

Il est important de noter que la méthode `Arrays.asList()` ne crée pas un nouvel objet List, mais retourne plutôt une vue du tableau d'origine en tant qu'objet List. Cela signifie que si nous modifions le tableau d'origine, les changements seront reflétés dans l'objet List également. Par exemple :

```java
fruits[0] = "pear";
System.out.println(fruitList.get(0)); // Sortie : pear
```

Dans l'exemple ci-dessus, nous avons modifié le premier élément du tableau `fruits` en "pear". Lorsque nous accédons au premier élément de l'objet `fruitList`, nous obtenons également "pear", car `fruitList` est simplement une vue du tableau `fruits`.

## Comment initialiser une liste en utilisant la méthode `Stream.of()`

La méthode `Stream.of()` est une méthode pratique fournie par Java 8 et les versions ultérieures dans le package `java.util.stream`. Elle est utilisée pour créer un flux d'éléments de n'importe quel type, y compris les types primitifs, les tableaux et les objets. Cette méthode prend un ou plusieurs arguments et retourne un flux constitué de ces arguments.

Voici la syntaxe de la méthode `Stream.of()` :

```java
Stream<T> stream = Stream.of(t1, t2, t3, ..., tn);
```

où `T` est le type des éléments dans le flux, et `t1` à `tn` sont les éléments à inclure dans le flux.

Pour initialiser une liste Java en utilisant la méthode `Stream.of()`, nous pouvons suivre ces étapes :

Tout d'abord, importer le package `java.util.stream`.

Ensuite, créer une liste du type souhaité en utilisant le constructeur `ArrayList`, par exemple :

```java
List<String> myList = new ArrayList<>();
```

Initialiser la liste en utilisant la méthode `Stream.of()`, en passant les éléments souhaités comme arguments, puis utiliser la méthode `collect()` pour collecter les éléments du flux dans la liste, par exemple :

```java
myList = Stream.of("Apple", "Banana", "Cherry", "Date")
              .collect(Collectors.toList());
```

Nous pouvons ensuite imprimer la liste pour vérifier son contenu.

```java
System.out.println(myList);
```

Sortie :

```
[Apple, Banana, Cherry, Date]
```

## Conclusion

En conclusion, l'initialisation d'une liste Java est une tâche courante en programmation Java, et il existe plusieurs façons de le faire.

En suivant les étapes décrites dans cet article, nous pouvons facilement créer et initialiser une liste Java avec les éléments souhaités en utilisant la méthode `Stream.of()`. Cette approche est concise et flexible, et elle peut être particulièrement utile lorsque nous devons initialiser une liste avec un petit nombre d'éléments.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !