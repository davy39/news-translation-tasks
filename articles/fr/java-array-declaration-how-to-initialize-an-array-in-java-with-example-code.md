---
title: Déclaration de tableau Java – Comment initialiser un tableau en Java avec un
  exemple de code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-09T14:34:15.000Z'
originalURL: https://freecodecamp.org/news/java-array-declaration-how-to-initialize-an-array-in-java-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/javaArrays.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: Déclaration de tableau Java – Comment initialiser un tableau en Java avec
  un exemple de code
seo_desc: "Arrays are an important part of the fundamental data structures in Java.\
  \ And they are incredibly useful in solving a lot of programming problems. \nWhat\
  \ is an array?\nBy definition, an array is a collection of data of the same type.\
  \ \nAn array is usuall..."
---

Les tableaux sont une partie importante des structures de données fondamentales en Java. Et ils sont incroyablement utiles pour résoudre de nombreux problèmes de programmation. 

## Qu'est-ce qu'un tableau ?

Par définition, un tableau est une collection de données de même type. 

Un tableau est généralement déclaré afin que vous puissiez avoir plusieurs valeurs dans la même mémoire – contrairement aux variables où vous ne pouvez avoir qu'une seule valeur en mémoire. 

Ainsi, les tableaux vous permettent de créer une variable qui contient différentes valeurs ensemble, au lieu de déclarer une variable pour chaque valeur. 

La position d'un point de données particulier dans le tableau est appelée son index, tandis que la donnée elle-même est appelée un élément.

Dans ce tutoriel, je vais vous montrer comment déclarer un tableau, l'initialiser et le parcourir avec la boucle for et la boucle for améliorée. Ensuite, vous pourrez commencer à l'utiliser dans vos projets Java.

J'utiliserai l'IDE intelliJIDEA pour écrire le code. Vous pouvez l'utiliser si vous le souhaitez, ou vous pouvez également utiliser n'importe quel IDE de votre choix.

## Comment déclarer et initialiser un tableau en Java

Il existe deux façons de déclarer et d'initialiser un tableau en Java. La première est avec le mot-clé `new`, où vous devez initialiser les valeurs une par une. La seconde consiste à mettre les valeurs entre accolades.

### Comment initialiser un tableau avec le mot-clé `new`

Vous pouvez déclarer le tableau avec la syntaxe suivante :

```java
typeDeDonnée [ ] nomDuTableau;
```

`typeDeDonnée` : le type de données que vous souhaitez mettre dans le tableau. Cela pourrait être une chaîne de caractères, un entier, un double, etc.
`[ ]` : signifie que la variable à déclarer contiendra un tableau de valeurs
`nomDuTableau` : L'identifiant du tableau.

Avec les informations ci-dessus, vous avez seulement déclaré le tableau – vous devez encore l'initialiser.

La syntaxe de base pour initialiser un tableau de cette manière ressemble à ceci :

```java
typeDeDonnée [] nomDuTableau = new typeDeDonnée [taille]
```

La taille est généralement exprimée avec une valeur numérique. Elle indique combien de valeurs vous souhaitez stocker dans le tableau. Sa valeur est immuable, ce qui signifie que vous ne pourrez pas mettre plus que le nombre spécifié comme taille dans le tableau. 

Vous pouvez maintenant mettre des valeurs dans le tableau comme ceci : 

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // écrivez votre code ici
String [] noms = new String[3];
noms[0] = "Quincy";
noms[1] = "Abbey";
noms[2] = "Kolade";
   }
}
```

Dans l'extrait de code ci-dessus, j'ai initialisé un tableau de chaînes de caractères appelé noms (l'identifiant). La taille est de 3, donc il ne peut contenir que trois valeurs. 

Il y a 3 index au total : 

- La valeur, `Quincy` est à l'index `0`
- La valeur `Abbey` est à l'index `1`
- La valeur `Kolade` est à l'index `2`

Ne soyez pas confus par les nombres 0, 1, 2. Les tableaux sont indexés à partir de zéro, donc le comptage commence à 0, pas à 1.

Dans le tableau ci-dessus, si vous ajoutez des données supplémentaires – par exemple, `noms[3] = "Chris"` – vous obtiendrez une erreur car vous avez spécifié que le tableau ne doit contenir que 3 valeurs. Si vous souhaitez ajouter plus de valeurs, vous devez augmenter la taille du tableau.

![error-1](https://www.freecodecamp.org/news/content/images/2021/09/error-1.png)

Pour imprimer le tableau dans la console, vous pouvez utiliser la méthode intégrée `toString()` :

```java
System.out.println(Arrays.toString(noms));
```

![names-print](https://www.freecodecamp.org/news/content/images/2021/09/names-print.png)

### 2. Comment initialiser un tableau en une ligne

Vous pouvez initialiser un tableau en une ligne avec la syntaxe de base suivante :

```java
typeDeDonnée [ ] nomDuTableau = {valeur1, valeur2, valeur3, valeur4}

```

Avec cette méthode, vous n'avez pas besoin de spécifier la taille du tableau, donc vous pouvez y mettre autant de valeurs que vous le souhaitez.

Consultez l'exemple dans l'extrait de code ci-dessous :

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // écrivez votre code ici
     String [] nomsDeux = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};
  }
}
```

L'impression du tableau dans la console montre les valeurs comme ceci :
![names-print-2](https://www.freecodecamp.org/news/content/images/2021/09/names-print-2.png)

## Comment parcourir un tableau en Java

Vous pouvez parcourir un tableau en Java avec la boucle for et la boucle for améliorée. Avec la boucle for, vous avez accès à l'index des valeurs individuelles, mais avec la boucle for améliorée, vous ne l'avez pas.

### Comment parcourir un tableau avec la boucle `for`

En Java, vous pouvez utiliser la boucle for avec la syntaxe de base suivante :

```java
for (typeDeDonnée i = 0; i < nomDuTableau.length; i++) {
    //   Code à exécuter
}
```

Vous pouvez ensuite parcourir le tableau `nomsDeux` comme ceci :

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // écrivez votre code ici

        String [] nomsDeux = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};

        for (int i = 0; i < nomsDeux.length; i++) {
            System.out.println("Élément à l'index " + i + " : " + nomsDeux[i]);
        }
    }
}
``` 

![for-loop](https://www.freecodecamp.org/news/content/images/2021/09/for-loop.png)

### Comment parcourir un tableau avec la boucle `for` améliorée

La boucle for améliorée est une version plus propre de la boucle for. L'inconvénient est que vous n'avez pas accès à l'index des valeurs individuelles dans le tableau.

La syntaxe de base de la boucle for améliorée ressemble à ceci : 

```java
for (typeDeDonnée variable : nomDuTableau) {
    // Code à exécuter
}
```

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // écrivez votre code ici

        String [] nomsDeux = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};

        for (String noms : nomsDeux) {
            System.out.println(noms);
        }
    }
}
```

![enhanced-for-loop](https://www.freecodecamp.org/news/content/images/2021/09/enhanced-for-loop.png)

## Conclusion

Dans ce tutoriel, vous avez appris comment déclarer et initialiser un tableau de deux manières différentes – avec le mot-clé new et en utilisant des accolades. 

Vous avez également appris comment parcourir des tableaux avec la boucle for et la boucle for améliorée, afin de ne pas simplement initialiser un tableau et ne rien en faire.

Merci d'avoir lu, et continuez à coder.