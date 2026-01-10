---
title: Comment utiliser les pointeurs en programmation C
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-05-03T19:46:04.000Z'
originalURL: https://freecodecamp.org/news/pointers-in-c-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-eyu-p-belen-1428634.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Comment utiliser les pointeurs en programmation C
seo_desc: "If you are learning C programming, you have probably heard the term \"\
  pointer\" before. \nPointers are one of the most important and powerful features\
  \ of the C programming language. They allow us to manipulate memory directly, which\
  \ can be very useful i..."
---

Si vous apprenez la programmation C, vous avez probablement déjà entendu le terme "pointeur".

Les pointeurs sont l'une des fonctionnalités les plus importantes et puissantes du langage de programmation C. Ils nous permettent de manipuler directement la mémoire, ce qui peut être très utile dans de nombreux scénarios de programmation.

En C, un pointeur est simplement une variable qui contient une adresse mémoire. Nous pouvons le considérer comme un moyen de faire référence à un emplacement spécifique en mémoire.

## Comment déclarer un pointeur

Pour déclarer une variable de pointeur en C, nous utilisons le symbole astérisque `*` avant le nom de la variable. Il existe deux façons de déclarer des variables de pointeur en C :

```c
int *p;
```

```c
int* p;
```

Ces deux déclarations sont équivalentes et elles déclarent une variable de pointeur nommée "p" qui peut contenir l'adresse mémoire d'un entier.

Cependant, il est important de noter que si vous déclarez plusieurs variables dans une seule instruction, vous devez inclure l'astérisque avant chaque nom de variable pour indiquer qu'elles sont toutes des pointeurs. Par exemple :

```c
int *p, *q, *r;
```

Cela déclare trois variables de pointeur nommées "p", "q" et "r" qui peuvent contenir l'adresse mémoire d'un entier.

## Comment initialiser un pointeur

Lorsque nous déclarons une variable de pointeur, elle ne pointe pas automatiquement vers un emplacement mémoire particulier. Pour initialiser un pointeur afin qu'il pointe vers une variable ou un emplacement mémoire spécifique, nous utilisons l'opérateur esperluette `&` pour obtenir l'adresse de cette variable.

Par exemple, pour initialiser le pointeur `p` afin qu'il pointe vers une variable entière appelée `x`, nous écririons :

```c
int x = 42;
int *p = &x;
```

Cela définit la valeur de `p` comme étant l'adresse mémoire de `x`.

## Comment déréférencer un pointeur

Une fois que nous avons un pointeur qui pointe vers un emplacement mémoire spécifique, nous pouvons accéder ou modifier la valeur stockée à cet emplacement en déréférençant le pointeur.

Pour déréférencer un pointeur, nous utilisons à nouveau le symbole astérisque `*`, mais cette fois-ci devant la variable de pointeur elle-même. Par exemple, pour imprimer la valeur de l'entier vers lequel `p` pointe, nous écririons :

```c
printf("%d\n", *p);
```

## Que signifie "pointeur vers un pointeur" ?

Un pointeur peut également pointer vers une autre variable de pointeur. Cela est connu sous le nom de "pointeur vers un pointeur". Nous déclarons un pointeur vers un pointeur en utilisant deux astérisques `**`. Par exemple :

```
int x = 42;
int *p = &x;
int **q = &p;
```

Ici, `q` est un pointeur vers un pointeur. Il pointe vers l'adresse de la variable `p`, qui à son tour pointe vers l'adresse de la variable `x`.

## Comment passer des pointeurs à des fonctions

Nous pouvons passer des pointeurs à des fonctions en tant qu'arguments, ce qui permet à la fonction de modifier la valeur de la variable originale passée. Cela est connu sous le nom de "passage par référence".

Pour passer un pointeur à une fonction, nous déclarons simplement le paramètre de la fonction comme un pointeur. Par exemple :

```c
void increment(int *p) {
    (*p)++;
}

int main() {
    int x = 42;
    int *p = &x;
    increment(p);
    printf("%d\n", x); // imprime 43
    return 0;
}

```

Ici, la fonction `increment` prend un pointeur vers un entier (`int *p`) et incrémente la valeur de l'entier de un (`(*p)++`).

Dans `main()`, nous déclarons l'entier `x` et un pointeur `p` qui pointe vers `x`. Nous appelons ensuite la fonction `increment`, en passant le pointeur `p`. Après l'appel de la fonction, `x` a été incrémenté à `43`.

## Comment utiliser les pointeurs pour l'allocation dynamique de mémoire

L'une des utilisations les plus puissantes des pointeurs en C est l'allocation dynamique de mémoire. Cela nous permet d'allouer de la mémoire à l'exécution, plutôt qu'à la compilation.

Nous utilisons la fonction `malloc` pour allouer dynamiquement de la mémoire, et elle retourne un pointeur vers la mémoire allouée. Par exemple :

```c
int *p = (int*)malloc(sizeof(int));

```

Ici, `p` est un pointeur vers un entier qui a été alloué en utilisant `malloc`. L'opérateur `sizeof` est utilisé pour déterminer la taille d'un entier en octets.

Après avoir alloué de la mémoire, nous pouvons utiliser la variable de pointeur comme n'importe quel autre pointeur. Lorsque nous avons terminé avec la mémoire, nous devons la libérer en utilisant la fonction `free`. Par exemple :

```c
free(p);
```

Cela libère la mémoire qui était allouée à `p`.

## Qu'est-ce que le transtypage de pointeur ?

Parfois, vous devrez peut-être transtyper un pointeur d'un type à un autre. Vous pouvez le faire en utilisant la syntaxe `(type *)`. Par exemple :

```c
double *p = (double *)malloc(sizeof(double));
```

Ici, `p` est transtypé en un pointeur vers un type `double`.

## Comment fonctionne l'arithmétique des pointeurs ?

Parce que les pointeurs contiennent des adresses mémoire, nous pouvons effectuer des opérations arithmétiques sur eux pour les déplacer vers différents emplacements mémoire.

Par exemple, nous pouvons incrémenter un pointeur pour le déplacer vers l'emplacement mémoire suivant. Cela est souvent utilisé dans les opérations sur les tableaux, où nous utilisons un pointeur pour accéder aux éléments d'un tableau.

Par exemple, pour imprimer le premier élément d'un tableau d'entiers en utilisant un pointeur, nous pourrions écrire :

```c
int arr[] = {1, 2, 3};
int *p = arr; // p pointe vers le premier élément de arr
printf("%d\n", *p); // imprime 1
```

Ici, `p` est défini pour pointer vers le premier élément du tableau `arr`, et `*p` déréférence le pointeur pour obtenir la valeur du premier élément (qui est `1`).

## Comment utiliser les tableaux de pointeurs

Nous pouvons également déclarer des tableaux de pointeurs en C. Par exemple :

```c
int *arr[3];
```

Cela déclare un tableau de trois pointeurs vers des entiers. Chaque élément du tableau peut pointer vers une variable entière séparée.

## Arithmétique des pointeurs et tableaux

Nous pouvons utiliser l'arithmétique des pointeurs pour accéder aux éléments d'un tableau. Par exemple :

```c
int arr[] = {1, 2, 3};
int *p = arr; // p pointe vers le premier élément de arr
printf("%d\n", *(p + 1)); // imprime 2
```

Ici, `p` est défini pour pointer vers le premier élément du tableau `arr`. Nous pouvons utiliser l'arithmétique des pointeurs pour accéder au deuxième élément du tableau (`*(p + 1)`), qui est `2`.

## Exemple d'utilisation des pointeurs

Voici un exemple de programme qui démontre certains des concepts que nous avons discutés :

```
#include <stdio.h>
#include <stdlib.h>

void increment(int *p) {
    (*p)++;
}

int main() {
    int x = 42;
    int *p = &x;
    printf("x = %d\n", x); // imprime x = 42
    increment(p);
    printf("x = %d\n", x); // imprime x = 43

    int *arr = (int *)malloc(3 * sizeof(int));
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;
    int *q = arr;
    printf("arr[0] = %d\n", *q); // imprime arr[0] = 1
    q++;
    printf("arr[1] = %d\n", *q); // imprime arr[1] = 2
    q++;
    printf("arr[2] = %d\n", *q); // imprime arr[2] = 3
    free(arr);

    return 0;
}
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-01-12-03-41.png)

Ce programme démontre plusieurs concepts liés aux pointeurs.

Tout d'abord, nous avons déclaré une variable entière `x` et un pointeur `p` qui pointe vers `x`. Nous avons appelé la fonction `increment`, en passant le pointeur `p`. La fonction `increment` modifie la valeur de `x` en l'incrémentant de un. Nous avons ensuite imprimé la valeur de `x` avant et après l'appel de la fonction pour démontrer que `x` a été incrémenté.

Ensuite, nous avons utilisé l'allocation dynamique de mémoire pour allouer un tableau de trois entiers. Nous avons défini les valeurs des éléments du tableau en utilisant l'arithmétique des pointeurs (`arr[0] = 1`, `arr[1] = 2`, etc.). Nous avons ensuite déclaré un pointeur `q` qui pointe vers le premier élément du tableau. De plus, nous avons utilisé l'arithmétique des pointeurs pour accéder et imprimer les valeurs de chaque élément du tableau.

Enfin, nous avons libéré la mémoire qui était allouée au tableau en utilisant la fonction `free`.

Ce programme démontre comment les pointeurs peuvent être utilisés pour modifier la valeur d'une variable, accéder aux éléments d'un tableau en utilisant l'arithmétique des pointeurs, et allouer et libérer dynamiquement de la mémoire.

## Erreurs courantes avec les pointeurs

Les pointeurs peuvent être délicats à utiliser et peuvent conduire à des erreurs courantes.

Une erreur courante est l'utilisation d'un pointeur non initialisé. Si vous déclarez une variable de pointeur mais ne l'initialisez pas pour qu'elle pointe vers un emplacement mémoire valide, vous pouvez obtenir une erreur de segmentation ou une autre erreur lorsque vous essayez de déréférencer le pointeur.

Une autre erreur courante est le déréférencement d'un pointeur nul, ce qui peut également provoquer une erreur de segmentation.

Une autre erreur à connaître est l'utilisation du mauvais type de pointeur. Par exemple, si vous déclarez un pointeur vers un entier mais que vous essayez ensuite de le déréférencer comme un pointeur vers un caractère, vous pouvez obtenir des résultats inattendus ou des erreurs.

## Conclusion

Les pointeurs sont un outil puissant en programmation C, mais ils peuvent être un peu délicats à utiliser. Avec de la pratique et de la patience, vous pouvez maîtriser les pointeurs et les utiliser pour manipuler la mémoire et travailler avec des structures de données complexes.

Merci d'avoir lu !