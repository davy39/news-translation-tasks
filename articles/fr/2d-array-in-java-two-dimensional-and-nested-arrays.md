---
title: Tableau 2D en Java – Tableaux à deux dimensions et imbriqués
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-10T20:49:04.000Z'
originalURL: https://freecodecamp.org/news/2d-array-in-java-two-dimensional-and-nested-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pawel-czerwinski-dYjFmiQb_aE-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Tableau 2D en Java – Tableaux à deux dimensions et imbriqués
seo_desc: "A multidimensional array is simply an array of arrays. You can look it\
  \ as a single container that stores multiple containers. \nIn this article, we'll\
  \ talk two dimensional arrays in Java. You'll see the syntax for creating one, and\
  \ how to add and acce..."
---

Un tableau multidimensionnel est simplement un [tableau](https://www.freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example/) de tableaux. Vous pouvez le voir comme un seul conteneur qui stocke plusieurs conteneurs. 

Dans cet article, nous allons parler des tableaux à deux dimensions en Java. Vous verrez la syntaxe pour en créer un, et comment ajouter et accéder aux éléments dans un tableau à deux dimensions. 

## Comment déclarer un tableau à deux dimensions en Java

Pour créer un tableau à deux dimensions en Java, vous devez spécifier le type de données des éléments à stocker dans le tableau, suivi de deux crochets et du nom du tableau. 

Voici à quoi ressemble la syntaxe :

```txt
type_de_données[][] nom_du_tableau;
```

Regardons un exemple de code. 

```java
int[][] nombresImpairs = { {1, 3, 5, 7}, {9, 11, 13, 15} };
```

Ne vous inquiétez pas si vous ne comprenez pas encore ce qui se passe ci-dessus. Dans la section suivante, vous en apprendrez davantage sur le fonctionnement des tableaux à deux dimensions et sur la façon d'accéder aux éléments qui y sont stockés. 

## Comment accéder aux éléments d'un tableau à deux dimensions en Java

Nous pouvons accéder aux éléments d'un tableau à deux dimensions en utilisant deux crochets. 

Le premier désigne le tableau à partir duquel nous voulons accéder aux éléments, tandis que le second désigne l'index de l'élément que nous voulons accéder. 

Simplifions l'explication ci-dessus avec un exemple :

```java
int[][] nombresImpairs = { {1, 3, 5, 7}, {9, 11, 13, 15} };

System.out.println(nombresImpairs[0][0]);
// 1
```

Dans l'exemple ci-dessus, nous avons deux tableaux dans le tableau `nombresImpairs` – `{1, 3, 5, 7}` et `{9, 11, 13, 15}`. 

Le premier tableau – `{1, 3, 5, 7}` – est désigné par 0. 

Le deuxième tableau – `{9, 11, 13, 15}` – est désigné par 1. 

Le premier tableau est 0, le deuxième est 1, le troisième est 2, et ainsi de suite. 

Ainsi, pour accéder à un élément du premier tableau, nous avons attribué 0 au premier crochet. Comme nous essayions d'accéder au premier élément du tableau, nous avons utilisé son index qui est zéro : `nombresImpairs[0][0]`. 

Décomposons cela encore plus. 

Voici le code pour accéder aux éléments : `nombresImpairs[?][?]`

J'ai mis des points d'interrogation dans les deux crochets – nous les remplirons au fur et à mesure. 

Donc, disons que nous voulons accéder à un élément du deuxième tableau qui est désigné par 1, notre code ressemblera à ceci : `nombresImpairs[1][?]`.

Maintenant que nous sommes dans le deuxième tableau (`{9, 11, 13, 15}`), essayons d'accéder à un élément à l'intérieur. Tout comme les tableaux réguliers, chaque élément a un index commençant par zéro. 

Ainsi, pour accéder à `13` qui est le troisième élément, nous passons son numéro d'index au deuxième crochet : `nombresImpairs[1][2]`. 

Dans la section suivante, nous commencerons avec un nouvel exemple. 

## Comment accéder aux éléments d'un tableau à deux dimensions en Java – Exemple

```java
int[][] nombresImpairs = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };
```

L'objectif ici est d'accéder à 21 dans le troisième tableau. Notre code d'accès a encore des points d'interrogation : `nombresImpairs[?][?]`. 

Nous commencerons par donner une valeur au premier point d'interrogation qui pointe vers le tableau particulier à accéder. 

Tableau 0 => `{1, 3, 5, 7}`  
Tableau 1 => `{9, 11, 13, 15}`  
Tableau 2 => `{17, 19, 21, 23}`

Le nombre que nous cherchons est dans le troisième tableau avec un index de tableau de 2. Nous avons donc trouvé la valeur pour le premier crochet : `nombresImpairs[2][?]`

La valeur du deuxième crochet pointera vers l'élément réel à accéder. Pour ce faire, nous devons spécifier le numéro d'index de l'élément. Voici les index dans ce tableau :

17 => Index 0  
19 => Index 1  
21 => Index 2  
23 => Index 3

21 a un index de 2, nous pouvons donc ajouter cela au deuxième crochet : `nombresImpairs[2][2]`. Lorsque vous imprimez cela sur la console, vous obtiendrez 21 imprimé. 

Voici à quoi ressemble le code :

```java
int[][] nombresImpairs = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };

System.out.println(nombresImpairs[2][2]);
// 21
```

Vous pouvez parcourir tous les éléments d'un tableau à deux dimensions en utilisant une boucle imbriquée. Voici un exemple :

```java
int[][] nombresImpairs = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };

for(int i = 0; i < nombresImpairs.length; i++){
    for(int j = 0; j < nombresImpairs[i].length; j++){
        System.out.println(nombresImpairs[i][j]);
    }   
}

// 1
// 3
// 5
// 7
// 9
// 11
// 13
// 15
// 17
// 19
// 21
// 23
```

Le code ci-dessus imprime tous les éléments du tableau `nombresImpairs`. 

## Résumé

Dans cet article, nous avons parlé des tableaux à deux dimensions en Java.

Nous avons vu la syntaxe pour créer des tableaux à deux dimensions. Nous avons également vu des exemples qui montraient comment accéder aux éléments qui y sont stockés. 

Enfin, nous avons vu comment parcourir et imprimer les éléments d'un tableau à deux dimensions.

Bon codage !