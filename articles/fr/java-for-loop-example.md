---
title: Exemple de boucle For en Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-07T17:41:44.000Z'
originalURL: https://freecodecamp.org/news/java-for-loop-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/java-for-loop.png
tags:
- name: Java
  slug: java
seo_title: Exemple de boucle For en Java
seo_desc: "You can use loops in programming to carry out a set of instructions repeatedly\
  \ until a certain condition is met.\nThere are three types of loops in Java: \n\n\
  for loop.\nwhile loop. \ndo...while loop.\n\nIn this article, we'll focus on the\
  \ for loop, its synt..."
---

Vous pouvez utiliser des boucles en programmation pour exécuter un ensemble d'instructions de manière répétée jusqu'à ce qu'une certaine condition soit remplie.

Il existe trois types de boucles en Java : 

* boucle `for`.
* boucle `while`. 
* boucle `do...while`.

Dans cet article, nous nous concentrerons sur la boucle `for`, sa syntaxe, et quelques exemples pour vous aider à l'utiliser dans votre code. 

La boucle `for` est principalement utilisée lorsque vous connaissez le nombre de fois qu'une boucle doit s'exécuter avant de s'arrêter. 

## Syntaxe de la boucle For en Java

Voici à quoi ressemble la syntaxe de la boucle `for` en Java :

```java
for (initialisation; condition; incrément/décrément) {
   // code à exécuter
}
```

Dans la syntaxe ci-dessus :

* **initialisation** désigne une variable initiale déclarée au point de départ de la boucle, généralement un entier.
* **condition** désigne le nombre de fois que la boucle doit s'exécuter.
* **incrément/décrément** augmente/diminue la valeur de la variable initiale à chaque fois que la boucle s'exécute. À mesure que l'incrément/décrément se produit, la valeur de la variable tend vers la **condition** spécifiée.

## Exemple de boucle For en Java

Dans cette section, vous verrez quelques exemples de code pratiques de la boucle `for` en Java :

#### Exemple de boucle For en Java #1

```java
class ForLoopExample {
    public static void main(String[] args) {
        for(int x = 1; x <=10; x++) {
            System.out.println(x);
            // 1
            // 2
            // 3
            // 4
            // 5
            // 6
            // 7
            // 8
            // 9
            // 10
        }
    }
}
```

Dans le code ci-dessus, nous avons utilisé une boucle `for` pour imprimer les nombres de 1 à 10. 

Mais comment cela fonctionne-t-il ? Regardons les conditions données : `(int x = 1; x <=10; x++)`.

Au début, `x` était défini à 1. 

La deuxième condition — `x <=10` — indique que la boucle doit s'exécuter tant que la valeur de `x` est inférieure ou égale à 10. 

La troisième condition — `x++` — augmente la valeur de `x` à chaque fois que la boucle s'exécute. 

La boucle imprime ensuite la valeur de `x` à chaque fois qu'elle est augmentée.

#### Exemple de boucle For en Java #2

Dans cet exemple, vous apprendrez comment imprimer toutes les valeurs stockées dans un tableau. 

```java
class ForLoopExample {
    public static void main(String[] args) {
        int[] oddNumbers = {1, 3, 5, 7};
        for (int i = 0; i < oddNumbers.length; i++) {
          System.out.println(oddNumbers[i]);
          // 1
          // 3
          // 5
          // 7
        }
    }
}
```

Les conditions dans le code ci-dessus sont un peu différentes par rapport au premier exemple, mais la logique est la même. 

`i` a une valeur initiale de 0 car l'index d'un tableau en Java commence à 0. Le premier élément est 0, le deuxième est 1, et ainsi de suite. 

`i < oddNumbers.length` signifie que le code doit s'exécuter tant que la valeur de `i` est inférieure à la longueur du tableau. La longueur du tableau est 4, donc cela signifie `i < 4`. 

i++ augmente la valeur de `i` à chaque fois que le code s'exécute jusqu'à ce que la condition `i < 4` soit `false`.

Le code imprime 1, 3, 5, 7 dans la console. 

Sans boucle, vous obtiendriez le même résultat en faisant quelque chose comme ceci :

```java
class ForLoopExample {
    public static void main(String[] args) {
        int[] oddNumbers = {1, 3, 5, 7};
          System.out.println(oddNumbers[0]); // 1
          System.out.println(oddNumbers[1]); // 3
          System.out.println(oddNumbers[2]); // 5
          System.out.println(oddNumbers[3]); // 7
    }
}
```

Imaginez avoir un tableau avec 100 éléments. Vous devriez taper cent méthodes `println` pour les imprimer tous. 

Avec une boucle, vous pouvez y parvenir avec une ligne de code. 

## Résumé

Dans cet article, nous avons parlé de la boucle `for` en Java. Nous utilisons des boucles pour exécuter du code de manière répétée jusqu'à ce qu'une condition soit remplie. 

Nous avons d'abord vu la syntaxe pour utiliser la boucle `for` en Java. Nous avons ensuite examiné quelques exemples de code pratiques montrant comment la boucle fonctionne. 

Bon codage !