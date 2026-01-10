---
title: C Print String – Comment imprimer une chaîne de caractères en C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-17T13:50:03.705Z'
originalURL: https://freecodecamp.org/news/how-to-print-a-string-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/Hcfwew744z4/upload/73cd11d4c62fcaa9d6fa85514d7cb732.jpeg
tags:
- name: c programming
  slug: c-programming
- name: C
  slug: c
- name: string
  slug: string
seo_title: C Print String – Comment imprimer une chaîne de caractères en C
seo_desc: 'Printing strings is a fundamental operation in programming. It helps you
  output information, inspect and debug your code, and display prompts to users.

  In this article, you will learn some of the different techniques to print strings
  in C.

  What is a ...'
---

L'impression de chaînes de caractères est une opération fondamentale en programmation. Elle permet d'afficher des informations, d'inspecter et de déboguer votre code, et de présenter des invites aux utilisateurs.

Dans cet article, vous apprendrez différentes techniques pour imprimer des chaînes de caractères en C.

## Qu'est-ce qu'une chaîne de caractères en C ?

Une chaîne de caractères est une séquence de caractères, comme des lettres, des nombres ou des symboles, qui sont regroupés ensemble. Elle est utilisée pour représenter du texte dans les programmes.

Les chaînes de caractères ne sont pas un type de données intégré en C. Elles sont plutôt représentées comme des tableaux de caractères, terminés par un caractère spécial appelé le terminateur nul, `\0`.

Voici un exemple de création d'une chaîne de caractères en C :

```c
char greeting[] = "Hello world!";
```

Dans le code ci-dessus, j'ai déclaré un tableau de caractères nommé `greeting` et l'ai initialisé avec la chaîne `Hello world!` entourée de guillemets doubles, `" "`.

Le compilateur C inclut automatiquement le terminateur nul, `\0`, à la fin de `Hello world!`.

## Comment imprimer une chaîne de caractères en C en utilisant la fonction `printf()`

La fonction `printf()` est l'une des méthodes les plus couramment utilisées pour imprimer des chaînes de caractères en C.

Elle signifie "print formatted" (imprimer formaté) et appartient à la bibliothèque standard d'entrée/sortie, `stdio.h`. Ainsi, pour l'utiliser, vous devez d'abord inclure le fichier d'en-tête `stdio.h` au début de votre programme.

Prenons l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello world!";
  
  printf("%s\n", greeting);
}

// Sortie :
// Hello world!
```

Dans l'exemple ci-dessus, j'ai d'abord inclus le fichier d'en-tête `stdio.h` au début de mon programme, qui contient la déclaration de la fonction `printf()`.

Ensuite, j'ai déclaré un tableau de caractères nommé `greeting` et l'ai initialisé avec le texte `Hello world!` entouré de guillemets doubles.

Enfin, j'ai utilisé la fonction `printf()` pour imprimer le texte `Hello world!`.

Lors de l'impression d'une chaîne de caractères en utilisant la fonction `printf()`, vous devez utiliser un spécificateur de format.

Un spécificateur de format agit comme un espace réservé qui indique à la fonction `printf()` comment formater et imprimer des types de données spécifiques. Ils commencent par un signe de pourcentage `%`, suivi d'un caractère qui spécifie le type de données à formater. Le spécificateur de format pour les chaînes de caractères est `%s`.

Ainsi, dans la ligne `printf("%s\n", greeting);`, le spécificateur de format `%s` indique à `printf()` d'imprimer la chaîne stockée dans la variable `greeting` suivie d'un caractère de nouvelle ligne, `\n`.

Notez que le spécificateur de format `%s` n'inclut pas le terminateur nul, `\0`, lors de l'impression des chaînes de caractères. Il imprime les caractères de la chaîne jusqu'à ce qu'il le rencontre.

## Comment imprimer une chaîne de caractères en C en utilisant la fonction `puts()`

Une autre fonction utilisée pour imprimer des chaînes de caractères est `puts()`.

Prenons l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello world!";
  
  puts(greeting);
}

// Sortie
// Hello world!
```

Dans l'exemple ci-dessus, j'ai d'abord inclus le fichier d'en-tête `stdio.h` qui contient la déclaration de `puts()`.

Ensuite, j'ai déclaré un tableau de caractères et l'ai initialisé avec le texte `Hello world!`. La chaîne se termine automatiquement par le terminateur nul, `\0`.

Enfin, j'ai utilisé la fonction `puts()` pour imprimer la chaîne sur la console et j'ai passé la variable de chaîne `greeting` comme argument.

La fonction `puts()` ajoute automatiquement un caractère de nouvelle ligne, `\n`, à la fin de la chaîne.

Notez que la fonction `puts()` est utilisée pour imprimer des chaînes terminées par un caractère nul. Une chaîne terminée par un caractère nul est une séquence de caractères stockés en mémoire suivie d'un caractère appelé le terminateur nul `\0`.

Jusqu'à présent, tous les exemples ont utilisé uniquement des chaînes terminées par un caractère nul, comme `char greeting[] = "Hello world!";`. En mémoire, cela serait représenté comme `['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '!', '\0']`.

Créer intentionnellement des chaînes non terminées par un caractère nul n'est pas courant en C.

Voici un exemple de chaîne non terminée par un caractère nul : `char greeting[] = {'H', 'e', 'l', 'l', 'o'};`. Ce tableau de caractères n'inclut pas le terminateur nul, `\0`, donc c'est une chaîne non terminée par un caractère nul.

Si vous essayez d'imprimer une chaîne non terminée par un caractère nul en utilisant `puts()`, vous obtiendrez un comportement indéfini, comme des caractères indésirables à la fin de la chaîne :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = {'H', 'e', 'l', 'l', 'o'};

  puts(greeting);
}

// Sortie lors de la première exécution du code :
// Helloq

// Sortie lors de la deuxième exécution du code :
// Hellop

// Sortie lors de la troisième exécution du code :
// Hellow
```

## La fonction `printf()` VS la fonction `puts()` – Quelle est la différence ?

Vous vous demandez peut-être quelle est la différence entre `printf()` et `puts()`.

La fonction `puts()` imprime le texte tel quel, sans aucun formatage. Elle ajoute également automatiquement un caractère de nouvelle ligne à la fin de la chaîne.

La fonction `printf()` n'ajoute pas automatiquement de nouvelle ligne – vous devez le faire explicitement.

Cependant, elle permet une sortie formatée et vous donne plus de contrôle et de flexibilité sur l'endroit et la manière dont vous insérez différents types de données dans la chaîne de format :

```c
#include <stdio.h>

int main(void) {
    char name[] = "John";
    int age = 30;

    // Impression de chaînes de caractères en utilisant puts()
    puts("En utilisant puts() :");
    puts("Mon nom est John et j'ai 30 ans.");

    // Impression de chaînes de caractères en utilisant printf()
    printf("\nEn utilisant printf() :\n");
    printf("Mon nom est %s et j'ai %d ans. \n", name, age);
}
```

Dans l'exemple ci-dessus, la fonction `puts()` imprime une simple chaîne de caractères sans aucun formatage. Elle ajoute également automatiquement un caractère de nouvelle ligne, `\n`, à la fin de la chaîne.

En revanche, la fonction `printf()` formate la chaîne et intègre deux valeurs de variables. Elle utilise des spécificateurs de format, tels que `%s` pour les chaînes de caractères et `%d` pour les entiers, pour spécifier le type de données que les variables contiennent, et où les variables doivent être insérées dans la chaîne. Elle ajoute également un caractère de nouvelle ligne à la fin.

## Conclusion

Dans cet article, vous avez appris les deux fonctions les plus couramment utilisées en C pour imprimer des chaînes de caractères.

La fonction `printf()` est couramment utilisée pour imprimer du texte formaté sur la console. Elle vous permet de formater votre sortie et d'imprimer des chaînes de caractères, des nombres et des caractères.

La fonction `puts()` est plus simple par rapport à `printf()`. Elle est idéale pour une sortie de texte basique et ajoute automatiquement un caractère de nouvelle ligne, `\n`, à la chaîne imprimée.

Merci d'avoir lu cet article, et bon codage !