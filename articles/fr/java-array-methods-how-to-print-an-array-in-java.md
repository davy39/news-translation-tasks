---
title: Méthodes de tableau Java – Comment imprimer un tableau en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T22:19:03.000Z'
originalURL: https://freecodecamp.org/news/java-array-methods-how-to-print-an-array-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Untitled-design--1-.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Méthodes de tableau Java – Comment imprimer un tableau en Java
seo_desc: "By Thanoshan MV\nAn array is a data structure used to store data of the\
  \ same type. Arrays store their elements in contiguous memory locations. \nIn Java,\
  \ arrays are objects. All methods of class object may be invoked in an array. We\
  \ can store a fixed n..."
---

Par Thanoshan MV

Un tableau est une structure de données utilisée pour stocker des données de même type. Les tableaux stockent leurs éléments dans des emplacements mémoire contigus. 

En Java, les tableaux sont des objets. Toutes les méthodes de la classe objet peuvent être invoquées dans un tableau. Nous pouvons stocker un nombre fixe d'éléments dans un tableau.

Déclarons un simple type primitif de tableau :

```java
int[] intArray = {2,5,46,12,34};
```

Essayons maintenant de l'imprimer avec la méthode `System.out.println()` :

```java
System.out.println(intArray);
// sortie : [I@74a14482
```

Pourquoi Java n'a-t-il pas imprimé notre tableau ? Que se passe-t-il sous le capot ?

La méthode `System.out.println()` convertit l'objet que nous avons passé en une chaîne en appelant `String.valueOf()` . Si nous regardons l'implémentation de la méthode `String.valueOf()`, nous verrons ceci :

```java
public static String valueOf(Object obj) {
    return (obj == null) ? "null" : obj.toString();
}
```

Si l'objet passé est `null`, elle retourne null, sinon elle appelle `obj.toString()` . Finalement, `System.out.println()` appelle `toString()` pour imprimer la sortie.

Si la classe de cet objet ne remplace pas l'implémentation de `Object.toString()`, elle appellera la méthode `Object.toString()`.

`Object.toString()` retourne `getClass().getName()+**'@'**`+Integer.toHexString(hashCode()) . En termes simples, elle retourne : « nom de la classe @ code de hachage de l'objet ».

Dans notre sortie précédente `[I@74a14482`, le `[` indique que ceci est un tableau, et `I` signifie int (le type du tableau). `74a14482` est la représentation hexadécimale non signée du code de hachage du tableau.

Lorsque nous créons nos propres classes personnalisées, il est une bonne pratique de remplacer la méthode `Object.toString()`.

Nous ne pouvons pas imprimer des tableaux en Java en utilisant une simple méthode `System.out.println()`. Voici les différentes façons dont nous pouvons imprimer un tableau :

1. Boucles : boucle for et boucle for-each 
2. Méthode `Arrays.toString()`
3. Méthode `Arrays.deepToString()`
4. Méthode `Arrays.asList()`
5. Interface Java Iterator
6. API Java Stream

Examinons-les une par une.

# 1. Boucles : boucle for et boucle for-each

Voici un exemple de boucle for :

```java
int[] intArray = {2,5,46,12,34};

for(int i=0; i<intArray.length; i++){
    System.out.print(intArray[i]);
    // sortie : 25461234
}
```

Toutes les classes wrapper remplacent `Object.toString()` et retournent une représentation sous forme de chaîne de leur valeur.

Et voici une boucle for-each :

```java
int[] intArray = {2,5,46,12,34};

for(int i: intArray){
    System.out.print(i);
    // sortie : 25461234
}
```

# 2. Méthode Arrays.toString()

`Arrays.toString()` est une méthode statique de la classe array qui appartient au package `java.util`. Elle retourne une représentation sous forme de chaîne du contenu du tableau spécifié. Nous pouvons imprimer des tableaux unidimensionnels en utilisant cette méthode. 

Les éléments du tableau sont convertis en chaînes en utilisant la méthode `String.valueOf()`, comme ceci :

```java
int[] intArray = {2,5,46,12,34};
System.out.println(Arrays.toString(intArray));
// sortie : [2, 5, 46, 12, 34]
```

Pour un type de référence de tableau, nous devons nous assurer que la classe de type de référence remplace la méthode `Object.toString()`.

Par exemple :

```java
public class Test {
    public static void main(String[] args) {
        Student[] students = {new Student("John"), new Student("Doe")};
        
        System.out.println(Arrays.toString(students));
        // sortie : [Student{name='John'}, Student{name='Doe'}]
    }
}

class Student {
    private String name;

    public Student(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Student{" + "name='" + name + '\'' + '}';
    }
}
```

Cette méthode n'est pas appropriée pour les tableaux multidimensionnels. Elle convertit les tableaux multidimensionnels en chaînes en utilisant `Object.toString()` qui décrit leurs identités plutôt que leurs contenus.

Par exemple :

```java
// création d'un tableau multidimensionnel
int[][] multiDimensionalArr = { {2,3}, {5,9} };

System.out.println(Arrays.toString(multiDimensionalArr));
// sortie : [[I@74a14482, [I@1540e19d]
```

Avec l'aide de `Arrays.deepToString()`, nous pouvons imprimer des tableaux multidimensionnels.

# 3. Méthode Arrays.deepToString()

`Arrays.deepToString()` retourne une représentation sous forme de chaîne des « contenus profonds » du tableau spécifié.

Si un élément est un tableau de type primitif, il est converti en une chaîne en invoquant le surchargement approprié de `Arrays.toString()`.

Voici un exemple de type primitif de tableau multidimensionnel :

```java
// création d'un tableau multidimensionnel
int[][] multiDimensionalArr = { {2,3}, {5,9} };

System.out.println(Arrays.deepToString(multiDimensionalArr));
// sortie : [[2, 3], [5, 9]]
```

Si un élément est un tableau de type référence, il est converti en une chaîne en invoquant `Arrays.deepToString()` de manière récursive.

```java
Teacher[][] teachers = 
{{ new Teacher("John"), new Teacher("David") }, {new Teacher("Mary")} };

System.out.println(Arrays.deepToString(teachers));
// sortie : 
[[Teacher{name='John'}, Teacher{name='David'}],[Teacher{name='Mary'}]]
```

Nous devons remplacer `Object.toString()` dans notre classe Teacher.

Si vous êtes curieux de savoir comment elle fait la récursion, voici le [code source](http://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/be44bff34df4/src/share/classes/java/util/Arrays.java#l4611) pour la méthode `Arrays.deepToString()`.

**NOTE :** Les tableaux de référence unidimensionnels peuvent également être imprimés en utilisant cette méthode. Par exemple :

```java
Integer[] oneDimensionalArr = {1,4,7};

System.out.println(Arrays.deepToString(oneDimensionalArr));
// sortie : [1, 4, 7]
```

# 4. Méthode Arrays.asList()

Cette méthode retourne une liste de taille fixe soutenue par le tableau spécifié.

```java
Integer[] intArray = {2,5,46,12,34};

System.out.println(Arrays.asList(intArray));
// sortie : [2, 5, 46, 12, 34]
```

Nous avons changé le type en Integer au lieu de int, car List est une collection qui contient une liste d'objets. Lorsque nous convertissons un tableau en une liste, il doit s'agir d'un tableau de type référence.

Java appelle `Arrays._asList_`(intArray).toString() . Cette technique utilise en interne la méthode `toString()` du type des éléments dans la liste.

Un autre exemple avec notre classe Teacher personnalisée :

```java
Teacher[] teacher = { new Teacher("John"), new Teacher("Mary") };

System.out.println(Arrays.asList(teacher));
// sortie : [Teacher{name='John'}, Teacher{name='Mary'}]
```

**NOTE :** Nous ne pouvons pas imprimer des tableaux multidimensionnels en utilisant cette méthode. Par exemple :

```java
Teacher[][] teachers = 
{{ new Teacher("John"), new Teacher("David") }, { new Teacher("Mary") }};
        
System.out.println(Arrays.asList(teachers));

// sortie : [[Lcom.thano.article.printarray.Teacher;@1540e19d, [Lcom.thano.article.printarray.Teacher;@677327b6]
```

# 5. Interface Java Iterator

Similaire à une boucle for-each, nous pouvons utiliser l'interface Iterator pour parcourir les éléments d'un tableau et les imprimer.

L'objet Iterator peut être créé en invoquant la méthode `iterator()` sur une Collection. Cet objet sera utilisé pour itérer sur les éléments de cette Collection.

Voici un exemple de la façon dont nous pouvons imprimer un tableau en utilisant l'interface Iterator :

```java
Integer[] intArray = {2,5,46,12,34};

// création d'une Liste de Integer
List<Integer> list = Arrays.asList(intArray);

// création d'un itérateur de la Liste de Integer
Iterator<Integer> it = list.iterator();

// si la Liste a des éléments à itérer
while(it.hasNext()) {
    System.out.print(it.next());
    // sortie : 25461234
}
```

# 6. API Java Stream

L'API Stream est utilisée pour traiter des collections d'objets. Un stream est une séquence d'objets. Les streams ne changent pas la structure de données originale, ils fournissent uniquement le résultat selon les opérations demandées.

Avec l'aide de l'opération terminale `forEach()`, nous pouvons itérer à travers chaque élément du stream.

Par exemple :

```java
Integer[] intArray = {2,5,46,12,34};

Arrays.stream(intArray).forEach(System.out::print);
// sortie : 25461234
```

Maintenant, nous savons comment imprimer un tableau en Java.

Merci d'avoir lu.

Image de couverture par [Aziz Acharki](https://unsplash.com/@acharki95?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

Vous pouvez lire mes autres articles sur [Medium](https://medium.com/@mvthanoshan9/object-oriented-programming-principles-in-java-820919dced1a). 

**Bon codage !**