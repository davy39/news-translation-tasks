---
title: Comment utiliser Arrays.binarySearch() en Java
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-08-23T15:31:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arrays-binarysearch-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/binarysearch-arrays-java.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Comment utiliser Arrays.binarySearch() en Java
seo_desc: "In this article, I'm going to show you how to use the Arrays.binarySearch()\
  \ method in Java.\nWhat is Arrays.binarySearch() in Java?\n According to the official\
  \ docs on the Arrays.binarySearch() method:\n\n(It) Searches the specified array\
  \ of bytes for th..."
---

Dans cet article, je vais vous montrer comment utiliser la méthode `Arrays.binarySearch()` en Java.

## Qu'est-ce que `Arrays.binarySearch()` en Java ?

Selon la [documentation officielle](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#binarySearch(byte[],%20byte)) sur la méthode `Arrays.binarySearch()` :

> (Elle) recherche la valeur spécifiée dans le tableau d'octets spécifié en utilisant l'algorithme de recherche binaire.   
>   
> Le tableau doit être trié (comme par la méthode [`sort(byte[])`](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#sort(byte[]))) avant d'effectuer cet appel. Si ce n'est pas le cas, les résultats sont indéfinis.   
>   
> Si le tableau contient plusieurs éléments avec la valeur spécifiée, il n'y a aucune garantie quant à celui qui sera trouvé.

En termes simples, la méthode `Arrays.binarySearch()` peut rechercher un élément donné dans un tableau trié et retourner son index si trouvé.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char voyelles[] = {'a', 'e', 'i', 'o', 'u'};
		
		char cle = 'i';
		
		int indexElementTrouve = Arrays.binarySearch(voyelles, cle);
		
		System.out.println("La voyelle donnée est à l'index : " + indexElementTrouve);

	}
}

```

La méthode `Arrays.binarySearch()` prend le tableau que vous souhaitez rechercher comme premier argument et la clé que vous recherchez comme deuxième argument. La sortie de ce programme sera :

```
La voyelle donnée est à l'index : 2
```

Rappelez-vous, la méthode retourne l'index de l'élément trouvé et non l'élément lui-même. Vous pouvez donc stocker l'index dans un entier comme celui utilisé dans cet exemple.

Par défaut, la méthode utilise le premier index du tableau comme point de départ de la recherche et la longueur du tableau comme point de fin de la recherche. Donc dans ce cas, l'index de départ est `0` et l'index de fin est `6`.

Au lieu d'utiliser les index de départ et de fin par défaut, vous pouvez les définir vous-même. Par exemple, si vous souhaitez effectuer la recherche de l'index `2` à l'index `4`, vous pouvez le faire comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char voyelles[] = {'a', 'e', 'i', 'o', 'u'};
		
		char cle = 'i';
		int indexDebut = 2;
		int indexFin = 4;
		
		int indexElementTrouve = Arrays.binarySearch(voyelles, indexDebut, indexFin, cle);
		
		System.out.println("La voyelle donnée est à l'index : " + indexElementTrouve);

	}
}

```

Dans ce cas, la méthode `Arrays.binarySearch()` prend le tableau que vous souhaitez rechercher comme premier argument, l'index de départ comme deuxième argument, l'index de fin comme troisième argument, et la clé comme quatrième argument.

Tant que vous gardez l'index de fin dans la longueur du tableau, la méthode devrait fonctionner correctement. Si vous dépassez cela, cependant, vous obtiendrez l'exception `Array index out of range`.

C'est simple, n'est-ce pas ? La méthode retourne l'index de l'élément s'il est trouvé. Mais que se passe-t-il si elle ne trouve pas l'élément donné ?

## Que se passe-t-il lorsque `Arrays.binarySearch()` ne trouve pas l'élément donné ?

Une fois de plus, selon la [documentation officielle](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#binarySearch(byte[],%20byte)) sur la méthode `Arrays.binarySearch()` :

> (La méthode retourne l') index de la clé de recherche, si elle est contenue dans le tableau dans la plage spécifiée ; sinon, `(-(_point d'insertion_) - 1)`.   
>   
> Le _point d'insertion_ est défini comme le point auquel la clé serait insérée dans le tableau : l'index du premier élément dans la plage supérieur à la clé, ou `toIndex` (index de fin) si tous les éléments dans la plage sont inférieurs à la clé spécifiée.   
>   
> Notez que cela garantit que la valeur de retour sera >= 0 si et seulement si la clé est trouvée.

Pas très clair, n'est-ce pas ? Laissez-moi expliquer. La première ligne indique que la méthode retournera l'index de la clé de recherche si elle est trouvée dans le tableau.

Mais si elle n'est pas trouvée, la sortie sera égale à la valeur de `(-(_point d'insertion_) - 1)`. Ici, en fonction de la clé de recherche, le `point d'insertion` peut avoir différentes valeurs.

Supposons que nous avons un tableau `[5, 6, 7, 8, 9, 10]` et une clé de recherche `0` qui n'est clairement pas dans le tableau. Dans ce cas, la clé de recherche est plus petite que tous les éléments du tableau. Mais le premier élément qui est plus grand que la clé de recherche est `5`. Donc dans ce cas, le `point d'insertion` sera :

```
(-(l'index du premier élément plus grand que la clé de recherche) - 1) = (0 - 1) = -1
```

Vous pouvez implémenter cela dans un extrait de code comme suit :

```java
package arrays;

import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int nombres[] = {5, 6, 7, 8, 9, 10};
		
		System.out.println(Arrays.binarySearch(nombres, 0)); // -1
	}
}

```

Supposons à nouveau que nous avons un tableau `[5, 6, 7, 8, 9, 10]` et une clé de recherche `12` qui n'est clairement pas dans le tableau. Dans ce cas, la clé de recherche est plus grande que tous les éléments du tableau. Donc dans ce cas, le `point d'insertion` sera :

```
(-(l'index de fin -(6) - 1) = (-6 - 1) = -7
```

Rappelez-vous, lorsque vous ne définissez pas manuellement un index de fin, la méthode utilise la longueur du tableau comme index de fin, qui dans ce cas est `6`.

Vous pouvez implémenter cela dans un extrait de code comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int nombres[] = {5, 6, 7, 8, 9, 10};
		
		System.out.println(Arrays.binarySearch(nombres, 12)); // -7
	}
}

```

Cependant, les résultats changeront si vous définissez manuellement les index de début et de fin comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int nombres[] = {5, 6, 7, 8, 9, 10};
		
		int indexDebut = 1;
		int indexFin = 3;
		
		System.out.println(Arrays.binarySearch(nombres, indexDebut, indexFin, 5)); // -2
		System.out.println(Arrays.binarySearch(nombres, indexDebut, indexFin, 10)); // -4

	}
}

```

Essayez de calculer les valeurs par vous-même. Vous pouvez également utiliser la méthode `Arrays.binarySearch()` avec des caractères comme ceci :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char voyelles[] = {'a', 'e', 'i', 'o', 'u'};
		
		char cle = 'i';
		int indexDebut = 2;
		int indexFin = 4;
		
		System.out.println(Arrays.binarySearch(voyelles, indexDebut, indexFin, cle));

	}
}

```

Les mêmes principes s'appliquent dans ce cas lorsque la clé de recherche donnée n'est pas trouvée. Mais lors de la comparaison entre un caractère dans le tableau et une clé de recherche donnée, le [code ASCII](https://www.ascii-code.com/) du caractère correspondant sera utilisé. Donc `A (65)` sera plus petit que `a (97)`. Gardez cela à l'esprit lorsque vous vérifiez les sorties de votre programme.

## Conclusion

C'est à peu près tout pour celui-ci. J'espère que vous comprenez maintenant comment utiliser la méthode `Arrays.binarySearch()`. 

Si vous avez des questions ou si vous souhaitez simplement communiquer avec moi, je suis sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Envoyez-moi des messages directs.