---
title: Tableau Java – Comment déclarer et initialiser un tableau en Java avec exemple
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-04T16:42:44.000Z'
originalURL: https://freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/andrew-moca-yAGNjU4rtss-unsplash-1.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Tableau Java – Comment déclarer et initialiser un tableau en Java avec
  exemple
seo_desc: 'In this article, we will talk about arrays in Java. We will go over some
  examples to help you understand what an array is, how to declare them, and how to
  use them in your Java code.

  What is an array?

  In Java, you use an array to store multiple value...'
---

Dans cet article, nous allons parler des tableaux en Java. Nous allons passer en revue quelques exemples pour vous aider à comprendre ce qu'est un tableau, comment les déclarer et comment les utiliser dans votre code Java.

## Qu'est-ce qu'un tableau ?

En Java, vous utilisez un tableau pour stocker plusieurs valeurs du même type de données dans une seule variable. Vous pouvez également le voir comme une collection de valeurs du même type de données. Cela signifie que si vous allez stocker des chaînes de caractères dans votre tableau, par exemple, alors toutes les valeurs de votre tableau doivent être des chaînes de caractères.

## Comment déclarer un tableau en Java

Nous utilisons des crochets `[]` pour déclarer un tableau. C'est-à-dire :

```java
String[] noms;
```

Nous avons déclaré une variable appelée `noms` qui contiendra un tableau de chaînes de caractères.

Si nous devions déclarer une variable pour des entiers (nombres entiers), nous ferions comme ceci :

```java
int[] mesEntiers;
```

Ainsi, pour créer un tableau, vous spécifiez le type de données qui sera stocké dans le tableau, suivi de crochets et ensuite du nom du tableau.

## Comment initialiser un tableau en Java

Initialiser un tableau signifie simplement assigner des valeurs au tableau. Initialisons les tableaux que nous avons déclarés dans la section précédente :

```java
String[] noms = {"John", "Jade", "Love", "Allen"};
```

```java
int[] mesEntiers = {10, 11, 12};
```

Nous avons initialisé nos tableaux en passant des valeurs du même type de données, chaque valeur étant séparée par une virgule.

Si nous voulions accéder aux éléments/valeurs de notre tableau, nous ferions référence à leur numéro d'index dans le tableau. L'index du premier élément est 0. Voici un exemple :

```java
String[] noms = {"John", "Jade", "Love", "Allen"};

System.out.println(noms[0]);
// John

System.out.println(noms[1]);
// Jade

System.out.println(noms[2]);
// Love

System.out.println(noms[3]);
// Allen
```

Maintenant que nous savons comment accéder à chaque élément, changeons la valeur du troisième élément. Voici comment cela se présente :

```java
String[] noms = {"John", "Jade", "Love", "Allen"};
noms[2] = "Victor";

System.out.println(noms[2]);
// Victor
```

Nous pouvons également vérifier la longueur d'un tableau en utilisant la propriété `length`. Voici un exemple :

```java
String[] noms = {"John", "Jade", "Love", "Allen"};
System.out.println(noms.length);
// 4
```

## Comment parcourir un tableau en Java

Nous pouvons utiliser la boucle `for` pour parcourir les éléments d'un tableau.

```java
String[] noms = {"John", "Jade", "Love", "Allen"};
for (int i = 0; i < noms.length; i++) {
  System.out.println(noms[i]);
}

// John
// Jade
// Love
// Allen
```

La boucle ci-dessus imprimera les éléments de notre tableau. Nous avons utilisé la propriété `length` pour spécifier le nombre de fois que la boucle doit s'exécuter.

## Conclusion

Dans cet article, nous avons appris comment déclarer et initialiser des tableaux dans notre code Java. Nous avons également vu comment accéder à chaque élément du tableau et comment parcourir ces éléments.

Bon codage !