---
title: Longueur d'une chaîne C - Comment trouver la taille d'une chaîne en C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-16T15:00:09.504Z'
originalURL: https://freecodecamp.org/news/how-to-find-length-of-c-string-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/JfhNqZtV56s/upload/0d58732b5a311298756b16ad3540b820.jpeg
tags:
- name: c programming
  slug: c-programming
seo_title: Longueur d'une chaîne C - Comment trouver la taille d'une chaîne en C
seo_desc: 'When working with strings in C, you need to know how to find their length.

  Finding the length of a string in C is essential for many reasons.

  You may need to perform string manipulation, and many string manipulation functions
  require the length of th...'
---

Lorsque vous travaillez avec des chaînes en C, vous devez savoir comment trouver leur longueur.

Trouver la longueur d'une chaîne en C est essentiel pour de nombreuses raisons.

Vous devrez peut-être effectuer des manipulations de chaînes, et de nombreuses fonctions de manipulation de chaînes nécessitent la longueur de la chaîne comme argument. Vous devrez peut-être également valider les entrées de l'utilisateur, comparer deux chaînes ou gérer et allouer de la mémoire dynamiquement.

Dans cet article, vous apprendrez différentes façons de trouver la longueur d'une chaîne en C.

## Qu'est-ce qu'une chaîne en C ?

Contrairement à d'autres langages de programmation, C n'a pas de type de données chaîne intégré.

Au lieu de cela, les chaînes en C sont des tableaux de caractères qui ont un caractère appelé le terminateur nul `\0` à la fin.

Il existe de nombreuses façons de créer une chaîne en C. Voici un exemple d'une façon de le faire :

```c
char greeting[] = "Hello";
```

Dans le code ci-dessus, j'ai créé un tableau de caractères nommé `greeting` en utilisant le type de données `char` suivi de crochets, `[]`.

J'ai ensuite assigné la chaîne `Hello`, entourée de guillemets doubles, à `greeting`.

Dans cet exemple, la taille du tableau n'est pas spécifiée explicitement - la taille est déterminée par la taille de la chaîne qui lui est assignée. De plus, le terminateur nul, `\0`, est automatiquement ajouté à la fin de la chaîne.

### Qu'est-ce que le fichier d'en-tête `string.h` en C ?

Le fichier d'en-tête `string.h` fournit des fonctions pour manipuler et travailler avec des chaînes.

Il contient des fonctions qui accomplissent des tâches telles que la copie et la concaténation. Il fournit également des fonctions pour trouver la longueur d'une chaîne, comme `strlen()`, dont vous apprendrez à vous servir dans la section suivante.

Pour utiliser les fonctions de `string.h`, vous devez l'inclure au début de votre fichier comme ceci :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
  // Votre code va ici
}
```

## Comment trouver la longueur d'une chaîne en C en utilisant la fonction `strlen()`

La fonction `strlen()` est définie dans le fichier d'en-tête `string.h` et est utilisée pour trouver la longueur d'une chaîne.

Prenons l'exemple suivant :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
  char greeting[] = "Hello";

  int length = strlen(greeting);

  printf("La longueur est : %d\n", length);
}

// Sortie :
// La longueur est : 5
```

Dans l'exemple ci-dessus, j'ai d'abord inclus le fichier d'en-tête `stdio.h` pour pouvoir utiliser les fonctions d'entrée/sortie telles que `printf()`. J'ai également inclus le fichier d'en-tête `string.h` pour pouvoir utiliser la fonction `strlen()`.

À l'intérieur de la fonction `main()`, j'ai créé un tableau `greeting` et stocké la chaîne `Hello`.

Ensuite, j'ai appelé la fonction `strlen()` et passé `greeting` comme argument - c'est la chaîne dont je veux trouver la longueur.

Enfin, j'ai utilisé la valeur retournée dans `length` et l'ai imprimée en utilisant la fonction `printf()`.

Notez que la fonction `strlen()` retourne le nombre de caractères dans la chaîne, à l'exclusion du terminateur nul (`\0`).

## Comment trouver la longueur d'une chaîne en C en utilisant l'opérateur `sizeof()`

Une autre façon de trouver la longueur d'une chaîne en C est d'utiliser l'opérateur `sizeof()`.

L'opérateur `sizeof()` retourne la taille totale en octets d'une chaîne.

Prenons l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";

  int size = sizeof(greeting);

  printf("La taille est %d octets \n", size);
}

// Sortie :
// La taille est 6 octets
```

Dans l'exemple suivant, `sizeof(greeting)` retourne la taille totale du tableau `greeting` en octets - y compris l'opérateur nul, `\0`.

Ce n'est pas toujours très utile.

Pour exclure ce caractère, vous devez soustraire un du total `size` :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";

  int length = sizeof(greeting) - 1;

  printf("La longueur est %d\n", length);
}

// Sortie :
// La longueur est 5
```

Bien que l'opérateur `sizeof()` ne nécessite pas d'inclure le fichier d'en-tête `string.h` comme le fait `strlen()`, il retourne la taille totale du tableau et non la longueur de la chaîne.

La taille totale du tableau inclut le terminateur nul, `\0`, alors que la longueur de la chaîne est le nombre de caractères avant le terminateur nul.

## Comment trouver la longueur d'une chaîne en C en utilisant une boucle `while`

Une autre façon de trouver la longueur d'une chaîne en C est d'utiliser une boucle `while`.

Le fonctionnement de cette méthode consiste à continuer à itérer sur les caractères d'une chaîne jusqu'à atteindre la fin et rencontrer le terminateur nul `\0`.

Examinons l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";
  int length = 0;

while (greeting[length] != '\0') {
    length++;
}
    printf("La longueur est %d", length );
}

// Sortie :
// La longueur est 5
```

Décomposons comment fonctionne la boucle.

J'ai initialisé une variable de compteur, `length`, à `0`. Cette variable stockera la longueur de la chaîne.

La condition de la boucle `while`, `greeting[length] != '\0'`, vérifie si le caractère à l'index `length` de la chaîne n'est pas égal au terminateur nul `\0`.

Si ce n'est pas le cas, la variable `length` est incrémentée et la boucle continue et passe au caractère suivant dans `greeting`.

La boucle `while` itère sur `greeting` jusqu'à ce qu'elle rencontre `\0` et l'itération s'arrête.

## Conclusion

Dans cet article, vous avez appris comment trouver la longueur d'une chaîne en C.

Vous avez appris à utiliser la fonction `strlen()`, qui retourne le nombre de caractères dans la chaîne, à l'exclusion du terminateur nul.

Vous avez également appris à utiliser l'opérateur `sizeof()` qui ne retourne pas toujours le résultat souhaité car il inclut le terminateur nul dans la longueur.

Enfin, vous avez appris à utiliser une boucle `while` pour trouver la longueur d'une chaîne. Une boucle compte les caractères dans la chaîne jusqu'à ce qu'elle atteigne le terminateur nul.

Merci d'avoir lu, et bon codage !