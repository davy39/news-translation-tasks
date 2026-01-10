---
title: Types de données en C - Entier, Nombre à virgule flottante et Void expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/data-types-in-c-integer-floating-point-and-void-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf3740569d1a4ca3517.jpg
tags:
- name: c programming
  slug: c-programming
- name: toothbrush
  slug: toothbrush
seo_title: Types de données en C - Entier, Nombre à virgule flottante et Void expliqués
seo_desc: 'Data Types in C

  There are several different ways to store data in C, and they are all unique from
  each other. The types of data that information can be stored as are called data
  types. C is much less forgiving about data types than other languages. A...'
---

## Types de données en C

Il existe plusieurs façons différentes de stocker des données en C, et elles sont toutes uniques les unes des autres. Les types de données sous lesquels les informations peuvent être stockées sont appelés types de données. C est beaucoup moins indulgent concernant les types de données que d'autres langages. Par conséquent, il est important de bien comprendre les types de données existants, leurs capacités et leurs limitations.

Une particularité des types de données de C est qu'ils dépendent entièrement du matériel sur lequel vous exécutez votre code. Un `int` sur votre ordinateur portable sera plus petit qu'un `int` sur un supercalculateur, il est donc important de connaître les limitations du matériel sur lequel vous travaillez. C'est aussi pourquoi les types de données sont définis comme étant des minimums - une valeur `int`, comme vous l'apprendrez, est au minimum de -32767 à 32767 : sur certaines machines, elle pourra stocker encore plus de valeurs que cela.

Il existe deux catégories dans lesquelles nous pouvons les diviser : les entiers et les nombres à virgule flottante. Les entiers sont des nombres entiers. Ils peuvent être positifs, négatifs ou nuls. Des nombres comme -321, 497, 19345 et -976812 sont tous des entiers parfaitement valides, mais 4,5 ne l'est pas car 4,5 n'est pas un nombre entier.

Les nombres à virgule flottante sont des nombres avec une décimale. Comme les entiers, -321, 497, 19345 et -976812 sont tous valides, mais maintenant 4,5, 0,0004, -324,984 et d'autres nombres non entiers sont également valides.

C nous permet de choisir entre plusieurs options différentes avec nos types de données car ils sont tous stockés de différentes manières sur l'ordinateur. Par conséquent, il est important d'être conscient des capacités et des limitations de chaque type de données pour choisir le plus approprié.

## **Types de données entières**

### Caractères : `char`

`char` contient des caractères - des choses comme des lettres, des ponctuations et des espaces. Dans un ordinateur, les caractères sont stockés sous forme de nombres, donc `char` contient des valeurs entières qui représentent des caractères. La traduction réelle est décrite par la norme ASCII. [Voici](http://www.asciitable.com/) un tableau pratique pour cela.

La taille réelle, comme tous les autres types de données en C, dépend du matériel sur lequel vous travaillez. Au minimum, il est d'au moins 8 bits, donc vous aurez au moins de 0 à 127. Alternativement, vous pouvez utiliser `signed char` pour obtenir au moins -128 à 127.

### Entiers standard : `int`

La quantité de mémoire qu'un seul `int` prend dépend du matériel. Cependant, vous pouvez vous attendre à ce qu'un `int` soit d'au moins 16 bits en taille. Cela signifie qu'il peut stocker des valeurs de -32 768 à 32 767, ou plus selon le matériel.

Comme tous ces autres types de données, il existe une variante `unsigned` qui peut être utilisée. Le `unsigned int` peut être positif et nul mais pas négatif, donc il peut stocker des valeurs de 0 à 65 535, ou plus selon le matériel.

### Entiers courts : `short`

Cela n'est pas souvent utilisé, mais il est bon de savoir que cela existe. Comme int, il peut stocker -32768 à 32767. Contrairement à int, cependant, c'est l'étendue de sa capacité. Partout où vous pouvez utiliser `short`, vous pouvez utiliser `int`.

### Entiers plus longs : `long`

Le type de données `long` stocke des entiers comme `int`, mais donne une plage de valeurs plus large au coût de prendre plus de mémoire. Long stocke au moins 32 bits, lui donnant une plage de -2 147 483 648 à 2 147 483 647. Alternativement, utilisez `unsigned long` pour une plage de 0 à 4 294 967 295.

### Entiers encore plus longs : `long long`

Le type de données `long long` est excessif pour presque toutes les applications, mais C vous permettra de l'utiliser quand même. Il est capable de stocker au moins -9 223 372 036 854 775 807 à 9 223 372 036 854 775 807. Alternativement, obtenez encore plus avec `unsigned long long`, qui vous donnera au moins 0 à 18 446 744 073 709 551 615.

## **Types de données de nombres à virgule flottante**

### Nombres à virgule flottante de base : `float`

`float` prend au moins 32 bits pour stocker, mais nous donne 6 décimales de 1,2E-38 à 3,4E+38.

### Doubles : `double`

`double` prend le double de la mémoire de float (donc au moins 64 bits). En retour, double peut fournir 15 décimales de 2,3E-308 à 1,7E+308.

### Obtenir une plage plus large de doubles : `long double`

`long double` prend au moins 80 bits. En conséquence, nous pouvons obtenir 19 décimales de 3,4E-4932 à 1,1E+4932.

## **Choisir le bon type de données**

C nous fait choisir le type de données, et nous devons être très spécifiques et intentionnels sur la manière dont nous le faisons. Cela vous donne beaucoup de pouvoir sur votre code, mais il est important de choisir le bon.

En général, vous devriez choisir le minimum pour votre tâche. Si vous savez que vous compterez de l'entier 1 à 10, vous n'avez pas besoin d'un long et vous n'avez pas besoin d'un double. Si vous savez que vous n'aurez jamais de valeurs négatives, envisagez d'utiliser les variantes `unsigned` des types de données. En fournissant cette fonctionnalité plutôt que de le faire automatiquement, C est capable de produire un code très léger et efficace. Cependant, c'est à vous, en tant que programmeur, de comprendre les capacités et les limitations, et de choisir en conséquence.

Nous pouvons utiliser l'opérateur sizeof() pour vérifier la taille d'une variable. Voir le programme C suivant pour l'utilisation des différents types de données :

```c
#include <stdio.h>

int main()
{
    int a = 1;
    
    char b ='G';
    
    double c = 3.14;
    
    printf("Hello World!\n");
 
    // impression des variables définies ci-dessus avec leurs tailles
    printf("Bonjour ! Je suis un caractère. Ma valeur est %c et "
           "ma taille est %lu octet.\n", b,sizeof(char));
    // peut utiliser sizeof(b) ci-dessus également
 
    printf("Bonjour ! Je suis un entier. Ma valeur est %d et "
           "ma taille est %lu octets.\n", a,sizeof(int));
    // peut utiliser sizeof(a) ci-dessus également
 
    printf("Bonjour ! Je suis une variable à virgule flottante double."
           " Ma valeur est %lf et ma taille est %lu octets.\n",c,sizeof(double));
    // peut utiliser sizeof(c) ci-dessus également
 
    printf("Au revoir ! À bientôt. :)\n");
    return 0;
}
```

### Sortie :

```text
Hello World!Bonjour ! Je suis un caractère. 
Ma valeur est G et ma taille est 1 octet.
Bonjour ! Je suis un entier. 
Ma valeur est 1 et ma taille est 4 octets.
Bonjour ! Je suis une variable à virgule flottante double. 
Ma valeur est 3.140000 et ma taille est 8 octets.
Au revoir ! À bientôt. :)
```

## **Le type Void**

Le type void spécifie qu'aucune valeur n'est disponible. Il est utilisé dans trois types de situations :

### 1. Retours de fonction en tant que void

Il existe diverses fonctions en C qui ne retournent aucune valeur ou vous pouvez dire qu'elles retournent void. Une fonction sans valeur de retour a le type de retour void. Par exemple, `void exit (int status);`

### 2. Arguments de fonction en tant que void

Il existe diverses fonctions en C qui n'acceptent aucun paramètre. Une fonction sans paramètre peut accepter un void. Par exemple, `int rand(void);`

### 3. Pointeurs vers void

Un pointeur de type void * représente l'adresse d'un objet, mais pas son type. Par exemple, une fonction d'allocation de mémoire `void *malloc( size_t size);` retourne un pointeur vers void qui peut être converti en n'importe quel type de données.