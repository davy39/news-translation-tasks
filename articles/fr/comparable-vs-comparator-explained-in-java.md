---
title: Interfaces Comparable vs Comparator en Java – Laquelle utiliser et quand ?
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2024-07-23T13:13:33.000Z'
originalURL: https://freecodecamp.org/news/comparable-vs-comparator-explained-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/comparable-comparator.png
tags:
- name: algorithms
  slug: algorithms
- name: Java
  slug: java
seo_title: Interfaces Comparable vs Comparator en Java – Laquelle utiliser et quand
  ?
seo_desc: Sorting is a fundamental operation in programming, essential for organizing
  data in a specific order. In Java, built-in sorting methods provide efficient ways
  to sort primitive data types and arrays, making it easy to manage and manipulate
  collection...
---

Le tri est une opération fondamentale en programmation, essentielle pour organiser les données dans un ordre spécifique. En Java, les méthodes de tri intégrées fournissent des moyens efficaces de trier les types de données primitifs et les tableaux, facilitant ainsi la gestion et la manipulation des collections de données. Par exemple, vous pouvez rapidement trier un tableau d'entiers ou une liste de chaînes de caractères en utilisant des méthodes comme `Arrays.sort()` et `Collections.sort()`.

Cependant, lorsqu'il s'agit de trier des objets personnalisés, tels que des instances de classes définies par l'utilisateur, les méthodes de tri intégrées montrent leurs limites. Ces méthodes ne savent pas comment ordonner les objets en fonction de critères personnalisés. C'est là que les interfaces `Comparable` et `Comparator` de Java entrent en jeu, permettant aux développeurs de définir et d'implémenter une logique de tri personnalisée adaptée à des exigences spécifiques.

Dans cet article de blog, nous explorerons comment utiliser les interfaces `Comparable` et `Comparator` pour trier des objets personnalisés en Java. Je fournirai des exemples pour illustrer les différences et les cas d'utilisation de chaque approche, vous aidant ainsi à maîtriser le tri personnalisé dans vos applications Java.

## Table des matières

* [Méthodes de tri pour les types primitifs](#heading-methodes-de-tri-pour-les-types-primitifs)
* [Comment utiliser l'interface Comparable](#heading-comment-utiliser-linterface-comparable)
* [Comment utiliser l'interface Comparator](#heading-comment-utiliser-linterface-comparator)
* [Comparable vs Comparator](#heading-comparable-vs-comparator)
* [Conclusion](#heading-conclusion)

## Méthodes de tri pour les types primitifs

Java fournit une variété de méthodes de tri intégrées qui facilitent le tri des types de données primitifs. Ces méthodes sont hautement optimisées et efficaces, vous permettant de trier des tableaux et des collections avec un minimum de code. Pour les types primitifs, tels que les entiers, les nombres à virgule flottante et les caractères, la méthode `Arrays.sort()` est couramment utilisée.

### Comment utiliser la méthode Arrays.sort()

La méthode `Arrays.sort()` trie le tableau spécifié dans l'ordre numérique ascendant. Cette méthode utilise un algorithme de tri rapide à double pivot, qui est plus rapide et plus efficace pour la plupart des ensembles de données.

Regardons un exemple de tri d'un tableau d'entiers et de caractères en utilisant `Arrays.sort()` :

```java
package tutorial;

import java.util.Arrays;

public class PrimitiveSorting {
    public static void main(String[] args) {
        int[] numbers = { 5, 3, 8, 2, 1 };
        System.out.println("Tableau original : " + Arrays.toString(numbers));

        Arrays.sort(numbers);
        System.out.println("Tableau trié : " + Arrays.toString(numbers));

        char[] characters = { 'o', 'i', 'e', 'u', 'a' };
        System.out.println("Tableau original : " + Arrays.toString(characters));

        Arrays.sort(characters);
        System.out.println("Tableau trié : " + Arrays.toString(characters));
    }
}
```

Sortie :

```bash
Tableau original : [5, 3, 8, 2, 1]
Tableau trié : [1, 2, 3, 5, 8]
Tableau original : [o, i, e, u, a]
Tableau trié : [a, e, i, o, u]
```

### Comment utiliser la méthode Collections.sort()

La méthode `Collections.sort()` est utilisée pour trier des collections telles que `ArrayList`. Cette méthode est également basée sur l'ordre naturel des éléments ou un comparateur personnalisé.

```java
package tutorial;

import java.util.ArrayList;
import java.util.Collections;

public class CollectionsSorting {
    public static void main(String[] args) {
        ArrayList<String> wordsList = new ArrayList<>();
        wordsList.add("banana");
        wordsList.add("apple");
        wordsList.add("cherry");
        wordsList.add("date");
        System.out.println("Liste originale : " + wordsList);

        Collections.sort(wordsList);
        System.out.println("Liste triée : " + wordsList);
    }
}
```

Sortie :

```plaintext
Liste originale : [banana, apple, cherry, date]
Liste triée : [apple, banana, cherry, date]
```

### Limites avec les classes personnalisées

Bien que les méthodes de tri intégrées de Java, telles que `Arrays.sort()` et `Collections.sort()`, soient puissantes et efficaces pour trier les types primitifs et les objets avec un ordre naturel (comme `String`), elles montrent leurs limites lorsqu'il s'agit de trier des objets personnalisés. Ces méthodes ne savent pas intrinsèquement comment ordonner les objets définis par l'utilisateur car il n'existe pas de moyen naturel pour eux de comparer ces objets.

Par exemple, considérons une simple classe `Person` qui a les attributs `name`, `age` et `weight` :

```java
package tutorial;

public class Person {
    String name;
    int age;
    double weight;

    public Person(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + ", weight=" + weight + " kgs]";
    }
}
```

Si nous essayons de trier une liste d'objets `Person` en utilisant `Arrays.sort()` ou `Collections.sort()`, nous rencontrerons une erreur de compilation car ces méthodes ne savent pas comment comparer les objets `Person` :

```java
package tutorial;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CustomClassSorting {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>(Arrays.asList(
                new Person("Alice", 30, 65.5),
                new Person("Bob", 25, 75.0),
                new Person("Charlie", 35, 80.0)
        ));
        System.out.println("Liste originale des personnes : " + people);

        Collections.sort(people);
        System.out.println("Liste triée des personnes : " + people);
    }
}
```

Erreur de compilation :

```bash
java: aucune méthode appropriée trouvée pour sort(java.util.List<tutorial.Person>)
    méthode java.util.Collections.<T>sort(java.util.List<T>) n'est pas applicable
      (variable d'inférence T a des bornes incompatibles
        contraintes d'égalité : tutorial.Person
        bornes inférieures : java.lang.Comparable<? super T>)
    méthode java.util.Collections.<T>sort(java.util.List<T>,java.util.Comparator<? super T>) n'est pas applicable
      (ne peut pas inférer le(s) type-variable(s) T
        (les listes d'arguments réels et formels diffèrent en longueur))
```

L'erreur se produit parce que la classe `Person` n'implémente pas l'interface `Comparable`, et il n'y a aucun moyen pour la méthode de tri de savoir comment comparer deux objets `Person`.

Pour trier des objets personnalisés comme `Person`, nous devons fournir un moyen de comparer ces objets. Java offre deux approches principales pour y parvenir :

1. Implémenter l'interface `Comparable` : Cela permet à une classe de définir son ordre naturel en implémentant la méthode `compareTo`.
2. Utiliser l'interface `Comparator` : Cela permet de créer des classes séparées ou des expressions lambda pour définir plusieurs façons de comparer des objets.

Nous explorerons ces deux approches dans les sections à venir, en commençant par l'interface `Comparable`.

## Comment utiliser l'interface Comparable

Java fournit une interface `Comparable` pour définir un ordre naturel pour les objets d'une classe définie par l'utilisateur. En implémentant l'interface `Comparable`, une classe peut fournir un seul ordre naturel qui peut être utilisé pour trier ses instances. Cela est particulièrement utile lorsque vous avez besoin d'une manière par défaut de comparer et de trier des objets.

### Aperçu

L'interface `Comparable` contient une seule méthode, `compareTo()`, qui compare l'objet courant avec l'objet spécifié pour l'ordre. La méthode retourne :

* Un entier négatif si l'objet courant est inférieur à l'objet spécifié.
* Zéro si l'objet courant est égal à l'objet spécifié.
* Un entier positif si l'objet courant est supérieur à l'objet spécifié.

### Comment Comparable permet un seul ordre naturel des objets

En implémentant l'interface `Comparable`, une classe peut garantir que ses objets ont un ordre naturel. Cela permet aux objets d'être triés en utilisant des méthodes comme `Arrays.sort()` ou `Collections.sort()` sans avoir besoin d'un comparateur séparé.

Implémentons l'interface `Comparable` dans une nouvelle classe `PersonV2`, en comparant par âge.

```java
package tutorial;

public class PersonV2 implements Comparable<PersonV2> {
    String name;
    int age;
    double weight;

    public PersonV2(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "PersonV2 [name=" + name + ", age=" + age + ", weight=" + weight + " kgs]";
    }

    @Override
    public int compareTo(PersonV2 other) {
        return this.age - other.age;
    }
}
```

Dans cette implémentation, la méthode `compareTo()` compare l'attribut `age` de l'objet `PersonV2` courant avec l'attribut `age` de l'objet `PersonV2` spécifié en soustrayant un âge de l'autre. En utilisant l'expression `this.age - other.age`, nous implémentons effectivement cette logique comme suit :

* Si `this.age` est inférieur à `other.age`, le résultat sera négatif.
* Si `this.age` est égal à `other.age`, le résultat sera zéro.
* Si `this.age` est supérieur à `other.age`, le résultat sera positif.

**Note** : Nous pouvons également utiliser `Integer.compare(this.age, other.age)` au lieu d'effectuer l'opération arithmétique manuellement.

Maintenant que la classe `PersonV2` implémente l'interface `Comparable`, nous pouvons trier une liste d'objets `PersonV2` en utilisant `Collections.sort()` :

```java
package tutorial;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CustomClassSortingV2 {
    public static void main(String[] args) {
        List<PersonV2> people = new ArrayList<>(Arrays.asList(
                new PersonV2("Alice", 30, 65.5),
                new PersonV2("Bob", 25, 75.0),
                new PersonV2("Charlie", 35, 80.0)
        ));
        System.out.println("Liste originale des personnes : " + people);

        Collections.sort(people);
        System.out.println("Liste triée des personnes : " + people);
    }
}
```

Sortie :

```bash
Liste originale des personnes : [PersonV2 [name=Alice, age=30, weight=65.5 kgs], PersonV2 [name=Bob, age=25, weight=75.0 kgs], PersonV2 [name=Charlie, age=35, weight=80.0 kgs]]
Liste triée des personnes : [PersonV2 [name=Bob, age=25, weight=75.0 kgs], PersonV2 [name=Alice, age=30, weight=65.5 kgs], PersonV2 [name=Charlie, age=35, weight=80.0 kgs]]
```

Dans cet exemple, les objets `PersonV2` sont triés par ordre croissant d'âge en utilisant la méthode `Collections.sort()`, qui repose sur l'ordre naturel défini par la méthode `compareTo()` dans la classe `PersonV2`.

### Limites de Comparable

Bien que l'interface `Comparable` fournisse un moyen de définir un ordre naturel pour les objets, elle présente plusieurs limitations qui peuvent restreindre son utilisation dans des applications pratiques. Comprendre ces limitations peut nous aider à déterminer quand utiliser d'autres mécanismes, tels que l'interface `Comparator`, pour obtenir un tri plus flexible.

* **Ordre naturel unique** : La limitation principale de `Comparable` est qu'elle permet uniquement un seul ordre naturel pour les objets d'une classe. Lorsque vous implémentez `Comparable`, vous définissez une seule façon de comparer les objets, qui est utilisée chaque fois que les objets sont triés ou comparés. Cela peut être restrictif si vous devez trier les objets de plusieurs façons.
* **Inflexibilité** : Si vous devez trier les objets par différents attributs ou dans différents ordres, vous devrez modifier la classe ou créer de nouvelles implémentations de `Comparable`. Cette inflexibilité peut conduire à une prolifération de méthodes de comparaison et peut rendre le code plus difficile à maintenir.
* **Non adaptable** : Une fois qu'une classe implémente `Comparable`, l'ordre naturel est fixé et ne peut pas être facilement changé. Par exemple, si votre classe `PersonV2` trie initialement par âge mais que vous avez ensuite besoin de trier par poids ou par nom, vous devez soit changer la méthode `compareTo()`, soit créer une nouvelle version de la classe.

C'est là que l'interface `Comparator` entre en jeu. Pour définir plusieurs façons de comparer des objets, nous pouvons utiliser l'interface `Comparator`, que nous explorerons dans la section suivante.

## Comment utiliser l'interface Comparator

L'interface `Comparator` en Java fournit un moyen de définir plusieurs façons de comparer et de trier des objets. Contrairement à l'interface `Comparable`, qui permet uniquement un seul ordre naturel, `Comparator` est conçu pour offrir de la flexibilité en permettant plusieurs stratégies de tri. Cela le rend particulièrement utile pour les scénarios où les objets doivent être triés de différentes manières.

### Aperçu

L'interface `Comparator` définit une seule méthode, `compare()`, qui compare deux objets et retourne :

* Un entier négatif si le premier objet est inférieur au second objet.
* Zéro si le premier objet est égal au second objet.
* Un entier positif si le premier objet est supérieur au second objet.

Cette méthode fournit un moyen de définir un ordre personnalisé pour les objets sans modifier la classe elle-même.

### Comment Comparator permet plusieurs façons d'ordonner les objets

L'interface `Comparator` vous permet de créer plusieurs instances `Comparator`, chacune définissant un ordre différent pour les objets. Cette flexibilité signifie que vous pouvez trier les objets par divers attributs ou dans différents ordres sans altérer la classe de l'objet.

Implémentons plusieurs instances `Comparator` pour la classe `Person`. Nous définirons des comparateurs pour trier par nom, par âge et par poids. Tout d'abord, nous devons mettre à jour la classe `Person` pour inclure des getters et nous assurer que les attributs sont accessibles.

```java
package tutorial;

public class Person {
    String name;
    int age;
    double weight;

    public Person(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + ", weight=" + weight + " kgs]";
    }
}
```

#### **Comparator par Nom**

Ce comparateur trie les objets `Person` par ordre alphabétique de leur `name`.

```java
package tutorial.comparator;

import tutorial.Person;

import java.util.Comparator;

public class PersonNameComparator implements Comparator<Person> {

    @Override
    public int compare(Person p1, Person p2) {
        return p1.getName().compareTo(p2.getName());
    }
}
```

#### Comparator par Âge

Ce comparateur trie les objets `Person` par leur `age`, dans l'ordre croissant.

```java
package tutorial.comparator;

import tutorial.Person;

import java.util.Comparator;

public class PersonAgeComparator implements Comparator<Person> {

    @Override
    public int compare(Person p1, Person p2) {
        return p1.getAge() - p2.getAge();
    }
}
```

#### Comparator par Poids

Ce comparateur trie les objets `Person` par leur `weight`, dans l'ordre croissant.

```java
package tutorial.comparator;

import tutorial.Person;

import java.util.Comparator;

public class PersonWeightComparator implements Comparator<Person> {

    @Override
    public int compare(Person p1, Person p2) {
        return (int) (p1.getWeight() - p2.getWeight());
    }
}
```

Voici comment vous pouvez utiliser ces instances `Comparator` pour trier une liste d'objets `Person` :

```java
package tutorial;

import tutorial.comparator.PersonAgeComparator;
import tutorial.comparator.PersonNameComparator;
import tutorial.comparator.PersonWeightComparator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CustomClassSortingV3 {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>(Arrays.asList(
                new Person("Alice", 30, 65.5),
                new Person("Bob", 25, 75.0),
                new Person("Charlie", 35, 80.0)
        ));
        System.out.println("Liste originale des personnes : " + people);

        Collections.sort(people, new PersonNameComparator());
        System.out.println("Liste triée des personnes par nom : " + people);

        Collections.sort(people, new PersonAgeComparator());
        System.out.println("Liste triée des personnes par âge : " + people);

        Collections.sort(people, new PersonWeightComparator());
        System.out.println("Liste triée des personnes par poids : " + people);
    }
}
```

Sortie :

```bash
Liste originale des personnes : [Person [name=Alice, age=30, weight=65.5 kgs], Person [name=Bob, age=25, weight=75.0 kgs], Person [name=Charlie, age=35, weight=80.0 kgs]]
Liste triée des personnes par nom : [Person [name=Alice, age=30, weight=65.5 kgs], Person [name=Bob, age=25, weight=75.0 kgs], Person [name=Charlie, age=35, weight=80.0 kgs]]
Liste triée des personnes par âge : [Person [name=Bob, age=25, weight=75.0 kgs], Person [name=Alice, age=30, weight=65.5 kgs], Person [name=Charlie, age=35, weight=80.0 kgs]]
Liste triée des personnes par poids : [Person [name=Alice, age=30, weight=65.5 kgs], Person [name=Bob, age=25, weight=75.0 kgs], Person [name=Charlie, age=35, weight=80.0 kgs]]
```

Dans cet exemple, les instances `Comparator` permettent de trier les objets `Person` par différents attributs : nom, âge et poids. Cela démontre comment l'interface `Comparator` permet des stratégies de tri flexibles et polyvalentes pour une classe.

## Comparable vs Comparator

Lors du tri d'objets en Java, vous avez deux options principales : les interfaces `Comparable` et `Comparator`. Comprendre les différences entre ces deux interfaces peut vous aider à choisir la bonne approche pour vos besoins. Veuillez noter que cela constitue également une question d'entretien très importante.

### Comparaison

Voici un tableau comparant et contrastant les interfaces `Comparable` et `Comparator` en Java :

<table><tbody><tr><th colspan="1" rowspan="1"><p>Fonctionnalité</p></th><th colspan="1" rowspan="1"><p>Comparable</p></th><th colspan="1" rowspan="1"><p>Comparator</p></th></tr><tr><td colspan="1" rowspan="1"><p>Définition</p></td><td colspan="1" rowspan="1"><p>Fournit un seul ordre naturel pour les objets</p></td><td colspan="1" rowspan="1"><p>Fournit plusieurs façons de comparer les objets</p></td></tr><tr><td colspan="1" rowspan="1"><p>Méthode</p></td><td colspan="1" rowspan="1"><p>compareTo(T o)</p></td><td colspan="1" rowspan="1"><p>compare(T o1, T o2)</p></td></tr><tr><td colspan="1" rowspan="1"><p>Implémentation</p></td><td colspan="1" rowspan="1"><p>Implémentée au sein de la classe elle-même</p></td><td colspan="1" rowspan="1"><p>Implémentée à l'extérieur de la classe</p></td></tr><tr><td colspan="1" rowspan="1"><p>Critères de tri</p></td><td colspan="1" rowspan="1"><p>Un ordre naturel par défaut</p></td><td colspan="1" rowspan="1"><p>Plusieurs critères de tri</p></td></tr><tr><td colspan="1" rowspan="1"><p>Flexibilité</p></td><td colspan="1" rowspan="1"><p>Limitée à une seule façon de comparer les objets</p></td><td colspan="1" rowspan="1"><p>Flexible ; plusieurs comparateurs peuvent être définis</p></td></tr><tr><td colspan="1" rowspan="1"><p>Modification de la classe</p></td><td colspan="1" rowspan="1"><p>Nécessite de modifier la classe pour implémenter <code>Comparable</code></p></td><td colspan="1" rowspan="1"><p>Ne nécessite pas de modifier la classe</p></td></tr><tr><td colspan="1" rowspan="1"><p>Cas d'utilisation</p></td><td colspan="1" rowspan="1"><p>Utiliser lorsqu'il existe un ordre naturel clair (par exemple, trier les employés par ID)</p></td><td colspan="1" rowspan="1"><p>Utiliser lorsque différents ordres de tri sont nécessaires ou lorsque vous ne pouvez pas modifier la classe</p></td></tr></tbody></table>

### Avantages et inconvénients de chaque approche

#### Comparable

##### Avantages :

* **Simplicité** : Fournit un ordre de tri par défaut facile à implémenter et à utiliser.
* **Intégré** : L'ordre naturel fait partie de la classe elle-même, il est donc toujours disponible et utilisé par défaut dans les méthodes de tri.

##### Inconvénients :

* **Ordre unique** : Ne peut définir qu'une seule façon de comparer les objets. Si différents ordres de tri sont nécessaires, la classe doit être modifiée ou des instances `Comparator` supplémentaires doivent être utilisées.
* **Modification de la classe** : Nécessite de modifier la classe pour implémenter `Comparable`, ce qui peut ne pas être réalisable si la classe fait partie d'une bibliothèque ou si son ordre naturel n'est pas clair.

#### Comparator

##### Avantages :

* **Flexibilité** : Permet plusieurs ordres de tri et critères, qui peuvent être définis externement et utilisés selon les besoins.
* **Non invasif** : Ne nécessite pas de modification de la classe elle-même, ce qui le rend adapté aux classes que vous ne contrôlez pas ou lorsque vous avez besoin de différentes options de tri.

##### Inconvénients :

* **Complexité** : Nécessite de créer et de gérer plusieurs instances `Comparator`, ce qui peut ajouter de la complexité au code.
* **Overhead** : Peut introduire un surcoût si de nombreux comparateurs sont utilisés, surtout s'ils sont créés à la volée.

En résumé, `Comparable` est mieux utilisé lorsqu'une classe a un ordre naturel qui a du sens pour la plupart des cas d'utilisation. 

`Comparator`, en revanche, offre de la flexibilité pour le tri selon plusieurs critères et est utile lorsque la classe n'a pas d'ordre naturel ou lorsque différents ordres de tri sont nécessaires. 

Choisir entre `Comparable` et `Comparator` dépend de vos besoins spécifiques en matière de tri et de savoir si vous avez besoin d'un ordre par défaut unique ou de plusieurs options de tri flexibles.

## Conclusion

Comprendre et utiliser à la fois `Comparable` et `Comparator` peut considérablement améliorer votre capacité à gérer et manipuler des collections d'objets en Java. En appliquant ces concepts, vous pouvez créer des mécanismes de tri plus flexibles et puissants.

Pour consolider votre compréhension, essayez d'implémenter à la fois `Comparable` et `Comparator` dans des scénarios réels. Expérimentez avec différentes classes et critères de tri pour voir comment chaque approche fonctionne en pratique.

### Liens vers la documentation officielle de Java :

* [Interface Java Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)
* [Interface Java Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html)