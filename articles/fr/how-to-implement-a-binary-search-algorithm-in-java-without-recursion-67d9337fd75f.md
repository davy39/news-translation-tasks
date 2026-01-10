---
title: Comment implémenter un algorithme de recherche binaire en Java sans récursivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-21T22:30:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-binary-search-algorithm-in-java-without-recursion-67d9337fd75f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pFQO8pwHj6QwYaQewgKM0Q.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Comment implémenter un algorithme de recherche binaire en Java sans récursivité
seo_desc: 'By javinpaul

  An Iterative implementation of the popular binary search algorithm to find an element
  in a sorted array.


  Hello everyone! I have published a lot of algorithms and data structure articles
  on my blog, but this one is the first one here. In...'
---

Par javinpaul

#### Une implémentation itérative de l'algorithme populaire de recherche binaire pour trouver un élément dans un tableau trié.

![Image](https://cdn-media-1.freecodecamp.org/images/Tfy1QANC2jqqQyLtL2XjiPLc80XxVlCEOP5V)

Bonjour à tous ! J'ai publié de nombreux articles sur les algorithmes et les structures de données sur mon blog, mais celui-ci est le premier ici. Dans cet article, nous examinerons les [algorithmes fondamentaux populaires pour les entretiens](http://www.java67.com/2018/06/data-structure-and-algorithm-interview-questions-programmers.html).

Oui, vous avez deviné juste : vous devez implémenter une **recherche binaire** en Java, et vous devez écrire à la fois des algorithmes de recherche binaire itératifs et récursifs.

En informatique, une recherche binaire, ou recherche par demi-intervalle, est un **algorithme de type diviser pour régner** qui localise la position d'un élément dans un [tableau trié](http://www.java67.com/2014/12/how-to-find-missing-number-in-sorted.html). La recherche binaire fonctionne en comparant une valeur d'entrée à l'élément central du tableau.

La comparaison détermine si l'élément est égal à l'entrée, est inférieur à l'entrée, ou est supérieur à l'entrée.

Lorsque l'élément comparé est égal à l'entrée, la recherche s'arrête et retourne généralement la position de l'élément.

Si l'élément n'est pas égal à l'entrée, une comparaison est faite pour déterminer si l'entrée est inférieure ou supérieure à l'élément.

En fonction du résultat, l'[algorithme](https://javarevisited.blogspot.com/2018/11/top-5-data-structures-and-algorithm-online-courses.html#axzz5YFaOvjsh) redémarre, mais ne recherche que dans le sous-ensemble supérieur ou inférieur des éléments du tableau.

Si l'entrée n'est pas localisée dans le [tableau](https://javarevisited.blogspot.com/2015/06/3-ways-to-find-duplicate-elements-in-array-java.html), l'algorithme retournera généralement une valeur unique indiquant cela, comme -1, ou lancera une [RuntimeException](http://www.java67.com/2012/12/difference-between-runtimeexception-and-checked-exception.html) en Java comme NoValueFoundException.

Les algorithmes de recherche binaire réduisent généralement de moitié le nombre d'éléments à vérifier à chaque itération successive, localisant ainsi l'élément donné (ou déterminant son absence) en temps logarithmique.

Au fait, si vous n'êtes pas familier avec les algorithmes de recherche et de tri fondamentaux, vous pouvez également suivre un cours comme [**Data Structures and Algorithms: Deep Dive Using Java**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F) pour apprendre les algorithmes fondamentaux.

![Image](https://cdn-media-1.freecodecamp.org/images/Zt9Z-B2aXoNxNBMlPUPF5lsJlenEMLYCpqlz)

Si Java n'est pas votre langage de prédilection, vous pouvez trouver plus de recommandations pour JavaScript et Python dans cette [liste de cours d'algorithmes](https://javarevisited.blogspot.com/2018/11/top-5-data-structures-and-algorithm-online-courses.html#axzz5YFaOvjsh).

Au fait, si vous préférez les livres, je vous suggère de lire un livre complet sur les algorithmes comme [**Introduction to Algorithms**](http://www.amazon.com/dp/0072970545/?tag=javamysqlanta-20) par Thomas H. Cormen.

![Image](https://cdn-media-1.freecodecamp.org/images/EXhvYsB0TaNmtUXJgxwRhdAZjhruvJKSMHjD)

Voici un exemple de code qui montre la logique de la **recherche binaire itérative en Java** :

![Image](https://cdn-media-1.freecodecamp.org/images/EXXBjdY30v3FxQ1Ug5nPzJPt0sPxlw9ZOBFt)

### Implémentation de la recherche binaire en Java

Voici un programme exemple pour implémenter la recherche binaire en Java. L'algorithme est implémenté de manière récursive. De plus, un fait intéressant à savoir sur l'implémentation de la recherche binaire en Java est que Joshua Bloch, auteur du célèbre livre [Effective Java](https://www.amazon.com/Effective-Java-3rd-Joshua-Bloch/dp/0134685997/?tag=javamysqlanta-20), a écrit la recherche binaire dans "java.util.Arrays".

```
import java.util.Arrays;import java.util.Scanner;
```

```
/** * Programme Java pour implémenter la recherche binaire. Nous avons implémenté la version itérative * de l'algorithme de recherche binaire en Java * @author Javin Paul */
```

```
public class IterativeBinarySearch {
```

```
  public static void main(String args[]) {    int[] list = new int[]{23, 43, 31, 12};    int number = 12;    Arrays.sort(list);    System.out.printf("Recherche binaire %d dans le tableau d'entiers %s %n", number, Arrays.toString(list));
```

```
    binarySearch(list, 12);    System.out.printf("Recherche binaire %d dans le tableau d'entiers %s %n", 43, Arrays.toString(list));
```

```
    binarySearch(list, 43);    list = new int[]{123, 243, 331, 1298};    number = 331;    Arrays.sort(list);    System.out.printf("Recherche binaire %d dans le tableau d'entiers %s %n", number,    Arrays.toString(list));
```

```
    binarySearch(list, 331);    System.out.printf("Recherche binaire %d dans le tableau d'entiers %s %n",   331, Arrays.toString(list));    binarySearch(list, 1333);
```

```
   // Utilisation de l'API Core Java et du framework Collection   // Précondition pour Arrays.binarySearch   Arrays.sort(list);
```

```
   // Recherche d'un élément   int index = Arrays.binarySearch(list, 3);
```

```
}
```

```
/** * Effectue une recherche binaire dans un tableau trié en Java * @param input * @param number * @return position de l'élément dans le tableau */
```

```
public static void binarySearch(int[] input, int number) {int first = 0;int last = input.length - 1;int middle = (first + last) / 2;
```

```
while (first <= last) {  if (input[middle] < number) {  first = middle + 1;} else if (input[middle] == number) {
```

```
System.out.printf(number + " trouvé à la position %d %n", middle);break;} else {  last = middle - 1;}
```

```
middle = (first + last) / 2;
```

```
}
```

```
if (first > last) {  System.out.println(number + " n'est pas présent dans la liste.\n");}
```

```
}
```

```
}
```

```
SortieRecherche binaire 12 dans le tableau d'entiers [12, 23, 31, 43]12 trouvé à la position 0Recherche binaire 43 dans le tableau d'entiers [12, 23, 31, 43]43 trouvé à la position 3Recherche binaire 331 dans le tableau d'entiers [123, 243, 331, 1298]331 trouvé à la position 2Recherche binaire 331 dans le tableau d'entiers [123, 243, 331, 1298]1333 n'est pas présent dans la liste.
```

C'est tout sur **comment implémenter la recherche binaire en utilisant la récursivité en Java**. Avec la recherche linéaire, ce sont deux des algorithmes de recherche essentiels que vous apprenez dans votre cours d'informatique.

La structure de données de l'arbre de recherche binaire tire parti de cet algorithme et organise les données dans une structure hiérarchique afin que vous puissiez rechercher n'importe quel nœud en temps O(logN).

Cependant, vous devez vous rappeler que pour utiliser la recherche binaire, vous avez besoin d'une liste ou d'un tableau trié, vous devez donc également prendre en compte le coût du tri lorsque vous envisagez d'utiliser l'algorithme de recherche binaire dans le monde réel.  
   
 **Apprentissage supplémentaire**  
 [Data Structures and Algorithms: Deep Dive Using Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F)  
 [Algorithms and Data Structures — Part 1 and 2](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fads-part1)   
 [Data Structures in Java 9 by Heinz Kabutz](https://learning.javaspecialists.eu/courses/data-structures?affcode=92815_johrd7r8)  
[10 Algorithms books for Interviews](http://www.java67.com/2015/09/top-10-algorithm-books-every-programmer-read-learn.html)  
[10 Data Structure and Algorithm Courses for Interviews](https://hackernoon.com/10-data-structure-algorithms-and-programming-courses-to-crack-any-coding-interview-e1c50b30b927)  
[5 Free Courses to Learn Data Structure and Algorithms](https://javarevisited.blogspot.com/2018/01/top-5-free-data-structure-and-algorithm-courses-java--c-programmers.html)

Autres **tutoriels sur les structures de données et les algorithmes** que vous pourriez aimer

* Comment implémenter l'algorithme Quicksort en place en Java ? ([tutoriel](http://javarevisited.blogspot.sg/2014/08/quicksort-sorting-algorithm-in-java-in-place-example.html))
* Comment implémenter un arbre de recherche binaire en Java ? ([solution](http://javarevisited.blogspot.sg/2015/10/how-to-implement-binary-search-tree-in-java-example.html))
* Comment implémenter l'algorithme Quicksort sans récursivité ? ([tutoriel](http://javarevisited.blogspot.sg/2016/09/iterative-quicksort-example-in-java-without-recursion.html))
* Comment implémenter l'algorithme de tri par insertion en Java ? ([tutoriel](http://javarevisited.blogspot.sg/2014/12/insertion-sort-algorithm-in-java-to-array-example.html))
* Comment implémenter l'algorithme de tri à bulles en Java ? ([tutoriel](http://www.java67.com/2012/12/bubble-sort-in-java-program-to-sort-integer-array-example.html))
* Quelle est la différence entre les algorithmes de tri par comparaison et non-par comparaison ? ([réponse](http://javarevisited.blogspot.sg/2017/02/difference-between-comparison-quicksort-and-non-comparison-counting-sort-algorithms.html))
* Comment implémenter le tri par compartiment en Java ? ([tutoriel](http://javarevisited.blogspot.sg/2017/01/bucket-sort-in-java-with-example.html))
* Comment implémenter un algorithme de recherche binaire sans récursivité en Java ? ([tutoriel](http://www.java67.com/2016/05/java-program-to-perform-binary-search-without-recursion.html))
* 50+ Cours sur les structures de données et les algorithmes pour les programmeurs ([questions](https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0))

Merci d'avoir lu cet article. Si vous aimez cet article, veuillez le partager avec vos amis et collègues. Si vous avez des suggestions ou des commentaires, n'hésitez pas à laisser un commentaire.

#### P.S. — Si vous êtes sérieux pour améliorer vos compétences en algorithmes, je pense que [Data Structures and Algorithms: Deep Dive Using Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F) est le meilleur pour commencer.