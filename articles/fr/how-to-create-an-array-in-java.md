---
title: Comment créer un tableau en Java – Exemple de déclaration de tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-16T19:48:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-array-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/array-declaration.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Comment créer un tableau en Java – Exemple de déclaration de tableau
seo_desc: 'By Shittu Olumide

  Creating and manipulating arrays is an essential skill for any Java programmer.
  Arrays provide a way to store and organize multiple values of the same type, making
  it easier to work with large sets of data.

  In this article, we will ...'
---

Par Shittu Olumide

Créer et manipuler des tableaux est une compétence essentielle pour tout programmeur Java. Les tableaux offrent un moyen de stocker et d'organiser plusieurs valeurs du même type, ce qui facilite le travail avec de grands ensembles de données.

Dans cet article, nous fournirons un guide étape par étape sur la façon de créer un tableau en Java, y compris comment initialiser ou créer un tableau. Nous aborderons également certains sujets avancés tels que les tableaux multidimensionnels, la copie de tableaux et le tri de tableaux.

Que vous soyez nouveau dans la programmation Java ou un développeur expérimenté cherchant à rafraîchir vos compétences, cet article vous apportera les connaissances nécessaires pour devenir compétent dans le travail avec les tableaux Java.

## Qu'est-ce qu'un tableau en Java ?

En Java, un tableau est une structure de données qui peut stocker une séquence de taille fixe d'éléments du même type de données. Un tableau est un objet en Java, ce qui signifie qu'il peut être assigné à une variable, passé comme paramètre à une méthode et retourné comme valeur par une méthode.

Les tableaux en Java sont indexés à partir de zéro, ce qui signifie que le premier élément d'un tableau a un index de 0, le deuxième élément a un index de 1, et ainsi de suite. La longueur d'un tableau est fixée lors de sa création et ne peut pas être modifiée ultérieurement.

Les tableaux Java peuvent stocker des éléments de n'importe quel type de données, y compris des types primitifs tels que int, double et boolean, ainsi que des types d'objets tels que String et Integer. Les tableaux peuvent également être multidimensionnels, ce qui signifie qu'ils peuvent avoir plusieurs lignes et colonnes.

Les tableaux en Java sont couramment utilisés pour stocker des collections de données, telles qu'une liste de nombres, un ensemble de chaînes de caractères ou une série d'objets. En utilisant des tableaux, nous pouvons accéder et manipuler des collections de données plus efficacement qu'en utilisant des variables individuelles.

Il existe plusieurs façons de créer un tableau en Java. Dans cette section, nous aborderons certaines des approches les plus courantes pour la déclaration et l'initialisation de tableaux en Java.

## Comment déclarer et initialiser un tableau en Java en une seule instruction

La déclaration et l'initialisation d'un tableau en une seule instruction est un moyen concis et pratique de créer un tableau en Java. Cette approche vous permet de déclarer et d'initialiser un tableau en utilisant une seule ligne de code.

Pour créer un tableau en une seule instruction, vous déclarez d'abord le type du tableau, suivi du nom du tableau, puis les valeurs du tableau entourées d'accolades, séparées par des virgules.

Voici un exemple :

```java
int[] numbers = {1, 2, 3, 4, 5};

```

Dans cet exemple, nous déclarons un tableau d'entiers nommé `numbers` et l'initialisons avec les valeurs 1, 2, 3, 4 et 5. Le type du tableau est `int[]`, indiquant qu'il s'agit d'un tableau d'entiers.

Vous pouvez également créer un tableau d'un type de données différent, comme un tableau de chaînes de caractères. Voici un exemple :

```java
String[] names = {"John", "Mary", "David", "Sarah"};

```

Dans cet exemple, nous déclarons un tableau de chaînes nommé `names` et l'initialisons avec les valeurs "John", "Mary", "David" et "Sarah".

Lorsque vous utilisez cette approche, vous n'avez pas besoin de spécifier explicitement la taille du tableau, car elle est inférée.

## Comment déclarer et initialiser un tableau en Java en instructions séparées

La déclaration et l'initialisation d'un tableau en instructions séparées est une autre façon de créer un tableau en Java. Cette approche consiste à déclarer une variable de tableau, puis à l'initialiser avec des valeurs dans une instruction séparée.

Pour créer un tableau en utilisant cette approche, vous déclarez d'abord la variable de tableau en utilisant la syntaxe `datatype[] arrayName`, où `datatype` est le type de données que le tableau contiendra, et `arrayName` est le nom du tableau.

Voici un exemple :

```java
int[] numbers;

```

Dans cet exemple, nous déclarons un tableau d'entiers nommé `numbers`, mais nous ne l'avons pas encore initialisé avec des valeurs.

Pour initialiser le tableau avec des valeurs, nous utilisons le mot-clé `new` suivi du type de données que le tableau contiendra, entouré de crochets, et du nombre d'éléments que le tableau contiendra. Voici un exemple :

```java
numbers = new int[]{1, 2, 3, 4, 5};

```

Dans cet exemple, nous initialisons le tableau `numbers` avec les valeurs 1, 2, 3, 4 et 5. Notez que nous utilisons la syntaxe `{valeur1, valeur2, ..., valeurN}` pour spécifier les valeurs du tableau.

Vous pouvez également initialiser le tableau avec des valeurs dans des instructions séparées, comme ceci :

```java
String[] names;
names = new String[]{"John", "Mary", "David", "Sarah"};

```

Dans cet exemple, nous déclarons un tableau de chaînes nommé `names` et l'initialisons avec les valeurs "John", "Mary", "David" et "Sarah" dans une instruction séparée.

En utilisant cette approche, vous pouvez également initialiser le tableau avec des valeurs par défaut en omettant les valeurs dans l'instruction d'initialisation. Par exemple :

```java
boolean[] flags = new boolean[5];

```

Dans cet exemple, nous déclarons un tableau de booléens nommé `flags` et l'initialisons avec 5 éléments. Comme nous n'avons spécifié aucune valeur, chaque élément est initialisé avec la valeur par défaut `false`.

## Comment déclarer un tableau en Java avec des valeurs par défaut

La déclaration de tableau avec des valeurs par défaut est un moyen de créer un tableau en Java et de l'initialiser avec les valeurs par défaut du type de données spécifié. Cette approche est utile lorsque vous devez créer un tableau d'une taille fixe, mais que vous n'avez pas de valeurs spécifiques pour l'initialiser.

Pour créer un tableau avec des valeurs par défaut, vous déclarez d'abord la variable de tableau en utilisant la syntaxe `datatype[] arrayName = new datatype[length]`, où `datatype` est le type de données, `arrayName` est le nom du tableau, et `length` est le nombre d'éléments. Voici un exemple :

```java
int[] numbers = new int[5];

```

Dans cet exemple, nous déclarons un tableau d'entiers nommé `numbers` avec une longueur de 5. Comme nous n'avons spécifié aucune valeur, chaque élément du tableau est initialisé avec la valeur par défaut 0.

You can also create an array of a different data type and initialize it with default values. For example:

```java
boolean[] flags = new boolean[3];

```

Dans cet exemple, nous déclarons un tableau de booléens nommé `flags` avec une longueur de 3. Comme nous n'avons spécifié aucune valeur, chaque élément du tableau est initialisé avec la valeur par défaut `false`.

Lorsque vous utilisez cette approche, il est important de noter que les valeurs par défaut d'un tableau dépendent de son type de données. Par exemple, la valeur par défaut d'un entier est 0, tandis que la valeur par défaut d'un booléen est `false`. Si le tableau contient des objets, la valeur par défaut est `null`.

La déclaration de tableau avec des valeurs par défaut est utile lorsque vous devez créer un tableau d'une taille fixe, mais que vous n'avez pas encore de valeurs spécifiques pour l'initialiser. Vous pourrez plus tard assigner des valeurs aux éléments du tableau en utilisant l'indexation.

## Tableaux multidimensionnels en Java

Un tableau multidimensionnel est un tableau qui contient d'autres tableaux. En Java, vous pouvez créer des tableaux multidimensionnels avec deux dimensions ou plus. Un tableau bidimensionnel est un tableau de tableaux, tandis qu'un tableau tridimensionnel est un tableau de tableaux de tableaux, et ainsi de suite.

Pour créer un tableau bidimensionnel en Java, vous déclarez d'abord la variable de tableau en utilisant la syntaxe `datatype[][] arrayName`. Voici un exemple :

```java
int[][] matrix;

```

Dans cet exemple, nous déclarons un tableau bidimensionnel d'entiers nommé `matrix`, mais nous ne l'avons pas encore initialisé.

Pour initialiser le tableau avec des valeurs, nous utilisons le mot-clé `new` suivi du type de données, entouré de crochets, et du nombre de lignes et de colonnes. Voici un exemple :

```java
matrix = new int[3][4];

```

Dans cet exemple, nous initialisons le tableau `matrix` avec 3 lignes et 4 colonnes. Notez que nous utilisons la syntaxe `new datatype[rows][columns]` pour spécifier les dimensions du tableau.

Voici un autre exemple de déclaration d'un tableau bidimensionnel d'entiers :

```java
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}};

```

Vous pouvez également créer un tableau multidimensionnel avec des valeurs par défaut en omettant les valeurs dans l'instruction d'initialisation. Par exemple :

```java
boolean[][] flags = new boolean[2][3];

```

Dans cet exemple, nous déclarons un tableau bidimensionnel de booléens nommé `flags` avec 2 lignes et 3 colonnes. Comme nous n'avons spécifié aucune valeur, chaque élément du tableau est initialisé avec la valeur par défaut `false`.

Les tableaux multidimensionnels sont utiles lorsque vous devez stocker des données dans une structure de type table ou grille, comme un échiquier ou une feuille de calcul.

## Conclusion

Créer des tableaux est une compétence fondamentale en programmation Java. Dans cet article, nous avons couvert quatre approches différentes pour la déclaration et l'initialisation de tableaux en Java, y compris la déclaration et l'initialisation en une seule instruction, la déclaration et l'initialisation séparées, les valeurs par défaut et les tableaux multidimensionnels.

Comprendre ces différentes techniques vous aidera à écrire un code Java plus efficace et à travailler plus efficacement avec les tableaux Java.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !