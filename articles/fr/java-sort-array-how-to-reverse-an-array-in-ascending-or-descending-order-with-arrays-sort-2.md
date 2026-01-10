---
title: Java Tri de Tableau – Comment Inverser un Tableau en Ordre Croissant ou Décroissant
  avec Arrays.sort()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-14T21:14:36.000Z'
originalURL: https://freecodecamp.org/news/java-sort-array-how-to-reverse-an-array-in-ascending-or-descending-order-with-arrays-sort-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/andre-taissin-hOwcob_3dpc-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Java Tri de Tableau – Comment Inverser un Tableau en Ordre Croissant ou
  Décroissant avec Arrays.sort()
seo_desc: "In Java, you use arrays to store a collection of variables (with the same\
  \ data type) in a single variable. \nIn many cases, the values stored in an array\
  \ appear in a random order. Using the Arrays class in Java, you have access to various\
  \ methods you ..."
---

En Java, vous utilisez des tableaux pour stocker une collection de variables (du même type de données) dans une seule variable. 

Dans de nombreux cas, les valeurs stockées dans un tableau apparaissent dans un ordre aléatoire. En utilisant la classe `Arrays` en Java, vous avez accès à diverses méthodes que vous pouvez utiliser pour manipuler des tableaux.

L'une des méthodes que nous utiliserons de la classe `Arrays` est la méthode `sort()` qui trie un tableau en ordre croissant.

Nous verrons également comment trier un tableau en ordre décroissant en utilisant la méthode `reverseOrder()` de la classe `Collections` en Java. 

## Comment Trier un Tableau en Ordre Croissant en Java en Utilisant `Arrays.sort()`

Dans cette section, nous verrons un exemple de la façon dont nous pouvons utiliser la méthode `sort()` pour trier un tableau en ordre croissant. 

```java
import java.util.Arrays;

class ArraySort {
    public static void main(String[] args) {
        int[] arr = { 5, 2, 1, 8, 10 };
        Arrays.sort(arr);
        
        for (int values : arr) {
            System.out.print(values + ", ");
            // 1, 2, 5, 8, 10,
        }
    }
}
```

La première chose que nous avons faite dans l'exemple ci-dessus a été d'importer la classe `Arrays` : `import java.util.Arrays;`. Cela nous donne accès à toutes les méthodes de la classe `Arrays`. 

Nous avons ensuite créé un tableau avec des nombres dans un ordre aléatoire : `int[] arr = { 5, 2, 1, 8, 10 };`.

Pour trier ce tableau en ordre croissant, nous avons passé le tableau en paramètre à la méthode `sort()` : `Arrays.sort(arr);`.

Notez que la classe `Arrays` a été écrite en premier avant d'accéder à la méthode `sort()` en utilisant la notation par point.

Enfin, nous avons parcouru et imprimé le tableau dans la console. Le résultat était un tableau trié : `1, 2, 5, 8, 10`.

Dans la section suivante, nous parlerons du tri d'un tableau en ordre décroissant. 

## Comment Trier un Tableau en Ordre Décroissant en Java en Utilisant `Collections.reverseOrder()`

Pour trier un tableau en ordre décroissant, nous utilisons `reverseOrder()` que nous pouvons accéder depuis la classe `Collections`.

Nous utiliserons toujours `Arrays.sort();`, mais dans cet exemple, il prendra deux paramètres – le tableau à trier et `Collections.reverseOrder()`. 

Voici un exemple :

```java
import java.util.Arrays;
import java.util.Collections;

class ArraySort {
    public static void main(String[] args) {
        Integer[] arr = { 5, 2, 1, 8, 10 };
        Arrays.sort(arr, Collections.reverseOrder());
        
        for (int values : arr) {
            System.out.print(values + ", ");
            // 10, 8, 5, 2, 1,
        }
    }
}
```

Tout d'abord, nous avons importé les classes Arrays et Collections car nous utiliserons les méthodes fournies par ces classes. 

Nous avons ensuite créé un tableau de nombres dans un ordre aléatoire : `Integer[] arr = { 5, 2, 1, 8, 10 };`. Vous remarquerez que nous avons utilisé `Integer[]` au lieu de `int[]` comme dans le dernier exemple – ce dernier aurait généré une erreur. 

Pour trier le tableau en ordre décroissant, nous avons fait ceci : `Arrays.sort(arr, Collections.reverseOrder());`. 

Le premier paramètre est le tableau `arr` qui sera trié en ordre croissant. Le deuxième paramètre – `Collections.reverseOrder()` – inversera ensuite l'ordre du tableau trié pour qu'il soit disposé en ordre décroissant.

Lorsqu'il est parcouru et imprimé, le tableau ressemblera à ceci : `10, 8, 5, 2, 1`.

## Résumé

Dans cet article, nous avons parlé du tri des tableaux en Java. Les tableaux peuvent être triés en ordre croissant ou décroissant. 

Nous pouvons trier les tableaux en ordre croissant en utilisant la méthode `sort()` à laquelle on peut accéder depuis la classe `Arrays`. La méthode `sort()` prend en paramètre le tableau à trier. 

Pour trier un tableau en ordre décroissant, nous avons utilisé la méthode `reverseOrder()` fournie par la classe `Collections`. Celle-ci est passée en tant que deuxième paramètre dans la méthode `sort()` afin que le tableau trié puisse être réorganisé en ordre décroissant. 

Bon codage !