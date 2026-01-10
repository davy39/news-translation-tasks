---
title: Comment trier une liste en Java - Exemple de tri de liste Java
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-24T19:22:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-a-list-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kelly-sikkema-ABkfxGoB-RE-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: Comment trier une liste en Java - Exemple de tri de liste Java
seo_desc: "Sometimes data needs to be arranged in a specific order so it's easier\
  \ to understand, search, and process. \nWe call this process sorting. Sorting refers\
  \ to arranging data in a specific order using certain criteria. You can sort different\
  \ types of dat..."
---

Parfois, les données doivent être organisées dans un ordre spécifique pour faciliter leur compréhension, leur recherche et leur traitement.

Nous appelons ce processus le tri. Le tri consiste à organiser les données dans un ordre spécifique en utilisant certains critères. Vous pouvez trier différents types de données, y compris les nombres, les chaînes et les objets. Java fournit des méthodes intégrées pour le tri, telles que les classes Collections.  
  
Le tri des données en Java pourrait être utile dans une application de commerce électronique où une liste de produits doit être affichée à l'utilisateur. Les produits peuvent être triés de diverses manières en fonction des exigences définies par l'utilisateur, telles que le prix, la note, la marque, etc.

Par exemple, si l'utilisateur souhaite voir tous les produits triés par prix dans l'ordre croissant, l'application peut utiliser un algorithme de tri pour organiser les produits dans cet ordre. Ainsi, lorsque l'utilisateur consulte les produits, il pourra voir les produits les moins chers en premier et prendre une décision d'achat en conséquence.  
  
Cet article examinera diverses méthodes pour trier une liste en Java.

## Comment utiliser la méthode `Collections.sort()` en Java

L'une des méthodes les plus courantes pour trier des données en Java consiste à utiliser la méthode `Collections.sort()`. Elle trie une liste dans l'ordre croissant par défaut. 

Voici un exemple de l'utilisation de la méthode `Collections.sort()` pour trier une liste d'entiers :

```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<Integer>();
        numbers.add(3);
        numbers.add(1);
        numbers.add(4);
        numbers.add(2);
        
        Collections.sort(numbers);
        
        System.out.println("Liste triée : " + numbers);
    }
}

```

Le code ci-dessus crée une liste d'entiers, ajoute quatre nombres à celle-ci, trie la liste, puis imprime la liste triée sur la console. 

Il utilise des classes de la bibliothèque standard de Java, y compris **`java.util.Collections`**, **`java.util.List`**, et **`java.util.ArrayList`** pour effectuer les opérations. 

La sortie du code ci-dessus est montrée ci-dessous :

```bash
//Sortie
Liste triée : [1, 2, 3, 4]
```

Vous pouvez également trier une liste d'objets personnalisés en utilisant la méthode `Collections.sort()`. Pour ce faire, vous devrez créer un comparateur et le passer en argument à la méthode `Collections.sort()`. 

Un comparateur est un objet qui implémente l'interface `java.util.Comparator`. Il possède une seule méthode appelée `compare()` qui compare deux objets et retourne un entier indiquant leur ordre relatif.

Voici un exemple de l'utilisation d'un comparateur pour trier une liste d'objets personnalisés :

```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 30));
        people.add(new Person("Charlie", 20));
        
        Collections.sort(people, new PersonComparator());
        
        System.out.println("Liste triée : " + people);
    }
}

class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}

class PersonComparator implements java.util.Comparator<Person> {
    @Override
    public int compare(Person a, Person b) {
        return a.getAge() - b.getAge();
    }
}

```

Le code ci-dessus crée une liste d'objets 'Person', ajoute plusieurs objets Person à la liste, trie la liste en utilisant un comparateur personnalisé (`PersonComparator`), puis imprime la liste triée. 

La classe `Person` possède deux champs, `name` et `age`, ainsi que des méthodes getter pour ces champs. La classe `PersonComparator` implémente l'interface Comparator et remplace la méthode compare pour trier les objets `Person` par âge.  
  
La sortie de ce programme sera la suivante :

```bash
//sortie
Liste triée : [Charlie (20), Alice (25), Bob (30)]
```

Il est préférable d'utiliser la méthode **`Collections.sort()`** lorsque vous avez une collection d'objets qui doivent être triés en fonction d'un ou plusieurs champs. 

Par exemple, si vous avez une collection d'objets Employee et que vous souhaitez les trier par leur nom de famille, vous pouvez utiliser la méthode `Collections.sort()` et passer un Comparator personnalisé qui compare les noms de famille des objets Employee.

## Comment utiliser la méthode List.sort() en Java

Cette méthode trie une liste dans l'ordre croissant. Voici comment elle fonctionne :

```java
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(5, 3, 2, 4, 1);
        numbers.sort(null);
        System.out.println(numbers); // imprime [1, 2, 3, 4, 5]
    }
}

```

Dans la méthode main ci-dessus, une liste d'entiers appelée "numbers" est créée en utilisant la méthode `Arrays.asList`. Le code trie ensuite cette liste de nombres en utilisant la méthode de tri par défaut puisque null est passé à la méthode sort.

Enfin, la liste triée est imprimée sur la console en utilisant la méthode `System.out.println`, ce qui produira "[1, 2, 3, 4, 5]".

**`List.sort()`** est utile lorsque vous avez une liste d'éléments qui doivent être triés. Par exemple, si vous avez une liste de chaînes et que vous souhaitez les trier dans l'ordre alphabétique, vous pouvez utiliser la méthode `List.sort()`. 

`List.sort()` est une méthode d'instance de la classe List et elle trie les éléments dans l'ordre défini par leur ordre naturel ou par une implémentation `Icomparer` spécifiée.

## Comment utiliser la méthode `stream.sorted()` en Java

Dans Java 8 et versions ultérieures, vous pouvez utiliser l'**API Stream** pour trier une liste. L'API Stream fournit une méthode sorted que vous pouvez utiliser pour trier les éléments d'un stream. 

Voici un exemple de tri d'une liste d'entiers en utilisant un stream :

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(5, 3, 2, 4, 1);
        List<Integer> sortedList = numbers.stream().sorted().collect(Collectors.toList());
        System.out.println(sortedList); // imprime [1, 2, 3, 4, 5]

    }
}

```

Dans l'exemple ci-dessus, la liste de nombres est convertie en un stream en utilisant la méthode `stream()`. La méthode `sorted()` est ensuite appelée sur le stream pour trier les éléments. La méthode `collect(Collectors.toList())` est utilisée pour collecter les éléments triés dans une liste. Le résultat est une nouvelle liste contenant les éléments triés. La sortie sera "[1, 2, 3, 4, 5]".

**`stream.sorted()`** est principalement utilisé lorsque vous avez un stream d'éléments qui doivent être triés. Par exemple, si vous avez un stream d'entiers et que vous souhaitez les trier dans l'ordre croissant, vous pouvez utiliser la méthode `stream.sorted()`.

## Conclusion

Dans ce tutoriel, vous avez appris qu'il existe plusieurs façons de trier une liste en Java - la méthode **Collections.sort()**, la méthode **stream.sorted()**, et la méthode **List.sort()**. La meilleure méthode à utiliser dépend des exigences spécifiques de la tâche à accomplir, comme nous l'avons discuté ci-dessus.

J'espère que cet article vous a fourni les informations correctes sur la façon de trier une liste en Java.

Bon codage !