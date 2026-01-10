---
title: Tutoriel sur les méthodes Java List – Exemple d'API Util List
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T16:15:27.000Z'
originalURL: https://freecodecamp.org/news/java-list-tutorial-util-list-api-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/collection0.jpg
tags:
- name: api
  slug: api
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Tutoriel sur les méthodes Java List – Exemple d'API Util List
seo_desc: "By Yiğit Kemal Erinç\nLists are commonly used data structures in every\
  \ programming language. \nIn this tutorial we are going to investigate Java's List\
  \ API. We'll start off with basic operations, and then we will get into more advanced\
  \ stuff (like a co..."
---

Par Yiğit Kemal Erinç

Les listes sont des structures de données couramment utilisées dans chaque langage de programmation. 

Dans ce tutoriel, nous allons examiner l'API List de Java. Nous commencerons par les opérations de base, puis nous aborderons des sujets plus avancés (comme une comparaison des différents types de listes, tels que ArrayList et LinkedList). 

Je vous donnerai également quelques directives pour vous aider à choisir l'implémentation de liste qui convient le mieux à votre situation.

Bien que des connaissances de base en Java suffisent pour suivre ce tutoriel, la dernière section nécessite des connaissances de base en structures de données (Array, LinkedList) et en [Big-O](https://en.wikipedia.org/wiki/Big_O_notation). Si vous n'êtes pas familier avec ces concepts, n'hésitez pas à sauter cette section.

## Définition des listes

Les listes sont des collections ordonnées d'objets. Elles sont similaires aux séquences en mathématiques à cet égard. Elles diffèrent des ensembles, cependant, qui n'ont pas un ordre certain. 

Quelques points à garder à l'esprit : les listes peuvent contenir des doublons et des éléments null. Elles sont des types de référence ou d'objet, et comme tous les objets en Java, elles sont stockées dans le heap.

Une liste en Java est une interface et il existe de nombreux types de listes qui implémentent cette interface. 

![Image](https://www.freecodecamp.org/news/content/images/2020/09/ListHierarchy.png)
_Hiérarchie des collections_

J'utiliserai ArrayList dans les premiers exemples, car c'est le type de liste le plus couramment utilisé. 

ArrayList est essentiellement un tableau redimensionnable. Presque toujours, vous voulez utiliser ArrayList plutôt que des tableaux réguliers car ils fournissent de nombreuses méthodes utiles. 

L'unique avantage des tableaux était leur taille fixe (en n'allouant pas plus d'espace que nécessaire). Mais les listes supportent également les tailles fixes maintenant.

## Comment créer une liste en Java

Assez parlé, commençons par créer notre liste. 

```java
import java.util.ArrayList;
import java.util.List;

public class CreateArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> list0 = new ArrayList<>();

        // Utilise le polymorphisme
        List list = new ArrayList<Integer>();

        // Variable locale avec le mot-clé "var", Java 10
        var list2 = new ArrayList<Integer>();
    }
}
```

Dans les chevrons (<>) nous spécifions le type d'objets que nous allons stocker. 

Gardez à l'esprit que le **type entre crochets doit être un type d'objet et non un type primitif**. Par conséquent, nous devons utiliser des wrappers d'objets, la classe Integer au lieu de int, Double au lieu de double, et ainsi de suite.

Il existe de nombreuses façons de créer un ArrayList, mais j'ai présenté trois façons courantes dans l'extrait ci-dessus. 

La première façon est de créer l'objet à partir de la classe concrète ArrayList en spécifiant ArrayList du côté gauche de l'affectation.

Le deuxième extrait de code utilise le polymorphisme en utilisant list du côté gauche. Cela rend l'affectation faiblement couplée avec la classe ArrayList et nous permet d'affecter d'autres types de listes et de passer à une autre implémentation de List facilement.

La troisième façon est la méthode Java 10 de création de variables locales en utilisant le mot-clé var. Le compilateur interprète le type de variable en vérifiant le côté droit.

Nous pouvons voir que toutes les affectations résultent dans le même type :

```java
System.out.println(list0.getClass());
System.out.println(list.getClass());
System.out.println(list2.getClass());
```

Sortie :

```java
class java.util.ArrayList
class java.util.ArrayList
class java.util.ArrayList

```

Nous pouvons également spécifier la capacité initiale de la liste. 

```java
List list = new ArrayList<>(20);
```

Cela est utile car chaque fois que la liste est pleine et que vous essayez d'ajouter un autre élément, la liste actuelle est copiée dans une nouvelle liste avec une capacité double de la liste précédente. Tout cela se passe en arrière-plan. 

Cette opération rend notre complexité _O(n)_, donc nous voulons l'éviter. La capacité par défaut est 10, donc si vous savez que vous allez stocker plus d'éléments, vous devriez spécifier la capacité initiale.

## Comment ajouter et mettre à jour des éléments de liste en Java

Pour ajouter des éléments à la liste, nous pouvons utiliser la méthode _add_. Nous pouvons également spécifier l'index du nouvel élément, mais soyez prudent lorsque vous le faites car cela peut entraîner une _IndexOutOfBoundsException_.

```java
import java.util.ArrayList;

public class AddElement {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add(1, "world");
        System.out.println(list);
    }
}
```

Sortie :

```
[hello, world]
```

Nous pouvons utiliser la méthode _set_ pour mettre à jour un élément.

```java
list.set(1, "from the otherside");
System.out.println(list);
```

Sortie :

```
[hello, world]
[hello, from the otherside]
```

## Comment récupérer et supprimer des éléments de liste en Java

Pour récupérer un élément de la liste, vous pouvez utiliser la méthode _get_ et fournir l'index de l'élément que vous souhaitez obtenir.

```java
import java.util.ArrayList;
import java.util.List;

public class GetElement {
    public static void main(String[] args) {
        List list = new ArrayList<String>();
        list.add("hello");
        list.add("freeCodeCamp");

        System.out.println(list.get(1));
    }
}
```

Sortie :

```java
freeCodeCamp

```

La complexité de cette opération sur ArrayList est _O(1)_ car elle utilise un tableau d'accès aléatoire régulier en arrière-plan.

Pour supprimer un élément de l'ArrayList, la méthode _remove_ est utilisée. 

```java
list.remove(0);
```

Cela supprime l'élément à l'index 0, qui est "hello" dans cet exemple.

Nous pouvons également appeler la méthode remove avec un élément à trouver et à supprimer. Gardez à l'esprit qu'elle ne supprime que la première occurrence de l'élément s'il est présent.

```java
public static void main(String[] args) {
        List list = new ArrayList();
        list.add("hello");
        list.add("freeCodeCamp");
        list.add("freeCodeCamp");

        list.remove("freeCodeCamp");
        System.out.println(list);
    }
```

Sortie :

```java
[hello, freeCodeCamp]
```

Pour supprimer toutes les occurrences, nous pouvons utiliser la méthode _removeAll_ de la même manière.

Ces méthodes sont à l'intérieur de l'interface List, donc chaque implémentation de List les possède (qu'il s'agisse de ArrayList, LinkedList ou Vector).

## Comment obtenir la longueur d'une liste en Java

Pour obtenir la longueur d'une liste, ou le nombre d'éléments, nous pouvons utiliser la méthode _size()_. 

```java
import java.util.ArrayList;
import java.util.List;

public class GetSize {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add("Welcome");
        list.add("to my post");
        System.out.println(list.size());
    }
}

```

Sortie :

```
2
```

## Listes à deux dimensions en Java

Il est possible de créer des listes à deux dimensions, similaires aux tableaux 2D. 

```java
ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<>();
```

Nous utilisons cette syntaxe pour créer une liste de listes, et chaque liste interne stocke des entiers. Mais nous n'avons pas encore initialisé les listes internes. Nous devons les créer et les mettre sur cette liste nous-mêmes :

```java
int numberOfLists = 3;
for (int i = 0; i < numberOfLists; i++) {
    listOfLists.add(new ArrayList<>());
}
```

J'initialise mes listes internes, et j'ajoute 3 listes dans ce cas. Je peux également ajouter des listes plus tard si nécessaire.

Maintenant, nous pouvons ajouter des éléments à nos listes internes. Pour ajouter un élément, nous devons obtenir la référence à la liste interne d'abord. 

Par exemple, supposons que nous voulons ajouter un élément à la première liste. Nous devons obtenir la première liste, puis y ajouter.

```java
listOfLists.get(0).add(1);
```

Voici un exemple pour vous. Essayez de deviner la sortie du segment de code ci-dessous :

```java
public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<>();
        System.out.println(listOfLists);
        int numberOfLists = 3;
        for (int i = 0; i < numberOfLists; i++) {
            listOfLists.add(new ArrayList<>());
        }

        System.out.println(listOfLists);

        listOfLists.get(0).add(1);
        listOfLists.get(1).add(2);
        listOfLists.get(2).add(0,3);

        System.out.println(listOfLists);
}
```

Sortie :

```
[]
[[], [], []]
[[1], [2], [3]]
```

Remarquez qu'il est possible d'imprimer les listes directement (contrairement aux tableaux réguliers) car elles remplacent la méthode _toString()_.

## Méthodes utiles en Java

Il existe d'autres méthodes et raccourcis utiles qui sont fréquemment utilisés. Dans cette section, je veux vous familiariser avec certaines d'entre elles afin que vous ayez plus de facilité à travailler avec les listes.

### Comment créer une liste avec des éléments en Java

Il est possible de créer et de remplir la liste avec certains éléments en une seule ligne. Il existe deux façons de faire cela. 

La méthode suivante est l'ancienne méthode :

```java
public static void main(String[] args) {
        List<String> list = Arrays.asList(
                                "freeCodeCamp",
                                "let's",
                                "create");
 }
```

Vous devez être prudent à propos d'une chose lorsque vous utilisez cette méthode : Arrays.asList retourne une liste immuable. Donc si vous essayez d'ajouter ou de supprimer des éléments après avoir créé l'objet, vous obtiendrez une _UnsupportedOperationException_. 

Vous pourriez être tenté d'utiliser le mot-clé _final_ pour rendre la liste immuable, mais cela ne fonctionnera pas comme prévu. 

Il garantit simplement que la référence à l'objet ne change pas – il ne se soucie pas de ce qui se passe à l'intérieur de l'objet. Donc il permet l'insertion et la suppression.

```java
final List<String> list2 = new ArrayList<>();
list2.add("erinc.io is the best blog ever!");
System.out.println(list2);
```

Sortie :

```
[erinc.io is the best blog ever!]

```

Maintenant, regardons la méthode moderne de le faire :

```java
ArrayList<String> friends =  new ArrayList<>(List.of("Gulbike", "Sinem", "Mete"));

```

La méthode _List.of_ a été introduite avec Java 9. Cette méthode retourne également une liste immuable, mais nous pouvons la passer au constructeur ArrayList pour créer une liste mutable avec ces éléments. Nous pouvons ajouter et supprimer des éléments de cette liste sans aucun problème.

### Comment créer une liste avec N copies d'un élément en Java

Java fournit une méthode appelée _nCopies_ qui est particulièrement utile pour le benchmarking. Vous pouvez remplir un tableau avec n'importe quel nombre d'éléments en une seule ligne.

```java
public class NCopies {
    public static void main(String[] args) {
        List<String> list = Collections.nCopies(10, "HELLO");
        System.out.println(list);
    }
}
```

Sortie :

```java
[HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO]

```

### Comment cloner une liste en Java

Comme mentionné précédemment, les listes sont des types de référence, donc les règles de [passage par référence](https://www.cs.fsu.edu/~myers/c++/notes/references.html) s'appliquent à elles. 

```java
public static void main(String[] args) {
        List list1 = new ArrayList<String>();
        list1.add("Hello");
        List list2 = list1;
        list2.add(" World");

        System.out.println(list1);
        System.out.println(list2);
}
```

Sortie :

```java
[Hello,  World]
[Hello,  World]
```

La variable list1 contient une référence à la liste. Lorsque nous l'affectons à list2, elle pointe également vers le même objet. Si nous ne voulons pas que la liste originale change, nous pouvons cloner la liste.

```java
ArrayList list3 = (ArrayList) list1.clone();
list3.add(" Of Java");

System.out.println(list1);
System.out.println(list3);
```

Sortie :

```java
[Hello,  World]
[Hello,  World,  Of Java]
```

Puisque nous avons cloné list1, list3 contient une référence à son clone dans ce cas. Par conséquent, list1 reste inchangée.

### Comment copier une liste dans un tableau en Java

Parfois, vous devez convertir votre liste en tableau pour la passer à une méthode qui accepte un tableau. Vous pouvez utiliser le code suivant pour y parvenir :

```java
List<Integer> list = new ArrayList<>(List.of(1, 2));
Integer[] toArray = list.toArray(new Integer[0]);
```

Vous devez passer un tableau et la méthode _toArray_ retourne ce tableau après l'avoir rempli avec les éléments de la liste.

### Comment trier une liste en Java

Pour trier une liste, nous pouvons utiliser _Collections.sort_. Elle trie par ordre croissant par défaut, mais vous pouvez également passer un comparateur pour trier avec une logique personnalisée.

```java
List<Integer> toBeSorted = new ArrayList<>(List.of(3,2,4,1,-2));
Collections.sort(toBeSorted);
System.out.println(toBeSorted);
```

Sortie :

```
[-2, 1, 2, 3, 4]
```

## Comment choisir quel type de liste utiliser ?

Avant de terminer cet article, je veux vous donner une brève comparaison de performance des différentes implémentations de listes afin que vous puissiez choisir celle qui convient le mieux à votre cas d'utilisation. 

Nous allons comparer ArrayList, LinkedList et Vector. Chacun d'eux a ses avantages et ses inconvénients, alors assurez-vous de considérer le contexte spécifique avant de décider.

### Java ArrayList vs LinkedList

Voici une comparaison des temps d'exécution en termes de complexité algorithmique.

```markdown
|                       | ArrayList                  | LinkedList |
|-----------------------|----------------------------|------------|
| GET(index)            | O(1)                       | O(n)       |
| GET depuis le début ou la fin | O(1)                       | O(1)       |
| ADD                   | O(1), si la liste est pleine O(n) | O(1)       |
| ADD(index)            | O(n)                       | O(1)       |
| Remove(index)         | O(n)                       | O(1)       |
| Recherche et suppression     | O(n)                       | O(n)       |
```

Généralement, l'opération _get_ est beaucoup plus rapide sur ArrayList, mais _add_ et _remove_ sont plus rapides sur LinkedList. 

ArrayList utilise un tableau en arrière-plan, et chaque fois qu'un élément est supprimé, les éléments du tableau doivent être décalés (ce qui est une opération _O(n)_).

Choisir des structures de données est une tâche complexe et il n'existe pas de recette qui s'applique à toutes les situations. Néanmoins, je vais essayer de fournir quelques directives pour vous aider à prendre cette décision plus facilement :

* Si vous prévoyez de faire plus d'opérations de get et d'add plutôt que de remove, utilisez ArrayList puisque l'opération get est trop coûteuse sur LinkedList. Gardez à l'esprit que l'insertion est _O(1)_ uniquement si vous l'appelez sans spécifier l'index et ajoutez à la fin de la liste.
* Si vous allez supprimer des éléments et/ou insérer au milieu (pas à la fin) fréquemment, vous pouvez envisager de passer à une LinkedList car ces opérations sont coûteuses sur ArrayList.
* Gardez à l'esprit que si vous accédez aux éléments séquentiellement (avec un itérateur), vous ne subirez pas de perte de performance avec LinkedList lors de la récupération des éléments.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-72.png)
_Source du benchmark : [programcreek](https://www.programcreek.com/2013/03/arraylist-vs-linkedlist-vs-vector/)_

### Java ArrayList vs Vector

Vector est très similaire à ArrayList. Si vous venez d'un environnement C++, vous pourriez être tenté d'utiliser un Vector, mais son cas d'utilisation est un peu différent de celui de C++. 

Les méthodes de Vector ont le mot-clé **[synchronized](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html)**, donc Vector garantit la sécurité des threads alors qu'ArrayList ne le fait pas. 

Vous pourriez préférer Vector à ArrayList en programmation multithread ou vous pouvez utiliser ArrayList et gérer la synchronisation vous-même. 

Dans un programme monothread, il est préférable de rester avec ArrayList car la sécurité des threads entraîne un coût de performance.

## Conclusion

Dans cet article, j'ai essayé de fournir un aperçu de l'API List de Java. Nous avons appris à utiliser les méthodes de base, et nous avons également examiné quelques astuces plus avancées pour faciliter notre vie. 

Nous avons également fait une comparaison entre ArrayList, LinkedList et Vector, qui est un sujet souvent posé lors des entretiens. 

Merci d'avoir pris le temps de lire l'article entier et j'espère qu'il a été utile.

Vous pouvez accéder à l'ensemble du code depuis ce [dépôt](https://github.com/yigiterinc/list-api-tutorial).

Si vous êtes intéressé à lire plus d'articles comme celui-ci, vous pouvez vous abonner à la liste de diffusion de mon [blog](https://erinc.io/) pour être informé lorsque je publie un nouvel article.