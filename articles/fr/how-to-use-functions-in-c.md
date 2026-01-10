---
title: Comment utiliser les fonctions en C - Expliqué avec des exemples
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-04-06T14:20:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-functions-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/guillaume-bolduc-uBe2mknURG4-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: Comment utiliser les fonctions en C - Expliqué avec des exemples
seo_desc: "Functions are an essential component of the C programming language. They\
  \ help you divide bigger problems into smaller, more manageable chunks of code,\
  \ making it simpler to create and run programs. \nWe'll look at functions in C,\
  \ their syntax, and how ..."
---

Les fonctions sont un composant essentiel du langage de programmation C. Elles vous aident à diviser des problèmes plus grands en morceaux de code plus petits et plus faciles à gérer, ce qui simplifie la création et l'exécution de programmes. 

Nous allons examiner les fonctions en C, leur syntaxe et comment les utiliser avec succès dans cet article.

## Qu'est-ce qu'une fonction en C ?

Une fonction est un bloc de code qui exécute une tâche particulière en programmation. C'est un morceau de code autonome qui peut être appelé de n'importe où dans le programme. 

Une fonction peut prendre des paramètres, exécuter des calculs et retourner une valeur. Une fonction en C peut être créée en utilisant cette syntaxe :

```c
return_type function_name(parameter list) {
   // corps de la fonction
}

```

Le `return_type` spécifie le type de valeur que la fonction retournera. Si la fonction ne retourne rien, le `return_type` sera `void`. 

Le `function_name` est le nom de la fonction, et le `parameter list` spécifie les paramètres que la fonction prendra.

## Comment déclarer une fonction en C

Déclarer une fonction en C informe le compilateur de la présence d'une fonction sans donner de détails d'implémentation. Cela permet à la fonction d'être appelée par d'autres sections du logiciel avant qu'elle ne soit spécifiée ou implémentée.

Une déclaration de fonction contient généralement le `nom de la fonction`, le `type de retour` et les types de paramètres. Voici la syntaxe pour définir une fonction en C :

```c
return_type function_name(parameter_list);

```

Ici, `return_type` est le type de données de la valeur que la fonction retourne. `function_name` est le nom de la fonction, et `parameter_list` est la liste des paramètres que la fonction prend en entrée.

Par exemple, supposons que nous avons une fonction appelée `add` qui prend deux entiers en entrée et retourne leur somme. Nous pouvons déclarer la fonction comme suit :

```c
int add(int num1, int num2);

```

Cela indique au compilateur qu'il existe une fonction appelée `add` qui prend deux entiers en entrée et retourne un entier en sortie.

Il est important de noter que les déclarations de fonctions n'incluent pas le corps de la fonction, qui contient le code réel qui s'exécute lorsque la fonction est appelée. 

Le corps de la fonction est défini indépendamment de la déclaration de la fonction, généralement dans un bloc de code séparé appelé la définition de la fonction.

Voici un exemple :

```c
#include <stdio.h>

/* déclaration de fonction */
int add(int a, int b);

/* définition de fonction */
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(2, 3);
    printf("Le résultat est %d\n", result);
    return 0;
}

```

Dans cet exemple, la fonction `add` est déclarée avec une déclaration de fonction en haut du fichier, qui spécifie son nom, son type de retour (`int`), et ses paramètres (`a` et `b`, tous deux `int`).

Le code réel pour la fonction `add` est défini dans la définition de la fonction. Ici, la fonction additionne simplement ses deux paramètres et retourne le résultat.

La fonction `main` appelle la fonction `add` avec les arguments `2` et `3`, et stocke le résultat dans la variable `result`. Enfin, elle imprime le résultat en utilisant la fonction `printf`.

### Comment utiliser une fonction dans plusieurs fichiers sources

Si vous souhaitez utiliser une fonction dans plusieurs fichiers sources, vous devez inclure une déclaration de fonction (également connue sous le nom de prototype de fonction) dans le fichier d'en-tête et la définition dans un fichier source.

Lorsque vous construisez, vous compilez d'abord les fichiers sources en fichiers objets, puis vous liez les fichiers objets dans l'exécutable final.

Créons un fichier d'en-tête appelé `myfunctions.h` :

```c
#ifndef MYFUNCTIONS_H
#define MYFUNCTIONS_H

int add(int a, int b);// Prototype de fonction, sa déclaration

#endif /* MYFUNCTIONS_H */

```

Dans ce fichier d'en-tête, nous déclarons une fonction `add` en utilisant une déclaration de fonction.

Ensuite, créons un fichier source appelé `myfunctions.c`, qui définit la fonction `add` :

```c
#include "myfunctions.h"

int add(int a, int b) {
    return a + b;
}

```

Dans ce fichier, nous incluons le fichier d'en-tête `myfunctions.h` en utilisant des guillemets, et nous définissons la fonction `add`.

Enfin, créons un fichier source appelé `main.c`, qui utilise la fonction `add` :

```c
#include <stdio.h>
#include "myfunctions.h"

int main() {
    int a = 10, b = 5;
    int sum = add(a, b);

    printf("La somme de %d et %d est %d\n", a, b, sum);

    return 0;
}

```

Dans ce fichier, nous incluons à la fois le fichier d'en-tête `stdio.h` et notre fichier d'en-tête `myfunctions.h` en utilisant des chevrons et des guillemets, respectivement. Nous appelons ensuite la fonction `add`, en passant les valeurs `a` et `b` et en stockant le résultat dans `sum`. Enfin, nous imprimons le résultat en utilisant `printf`.

La manière dont vous le créez est fortement influencée par votre environnement. Si vous utilisez un IDE (comme Visual Studio), vous devez positionner tous les fichiers aux emplacements appropriés dans le projet.

Si vous créez à partir de la ligne de commande, par exemple sous Linux, pour compiler ce programme, vous devrez compiler à la fois `myfunctions.c` et `main.c` et les lier ensemble comme montré ci-dessous :

```
gcc -c myfunctions.c
gcc -c main.c
gcc -o program main.o myfunctions.o

```

L'option `-c` indique au compilateur de créer un fichier objet avec le même nom que le fichier source mais avec une extension `.o`. La dernière instruction joint les deux fichiers objets pour créer l'exécutable final, qui est nommé `program` (l'option -o spécifie le nom du fichier de sortie).

## Que se passe-t-il si vous appelez une fonction avant sa déclaration en C ?

Dans ce cas, l'ordinateur pense que le type de retour habituel est un entier. Si la fonction retourne un type de données différent, elle génère une erreur. 

Si le type de retour est également un entier, elle fonctionnera correctement. Mais certains avertissements peuvent être générés :

```c
#include<stdio.h>
main() {
   printf("La valeur retournée : %d", function);
}
char function() {
   return 'V';
}

```

Dans ce code, la fonction `function()` est appelée avant d'être déclarée. Cela retourne une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-from-2023-04-05-14-03-36.png)
_avertissements et erreurs_

## Comment définir une fonction en C

Supposons que vous souhaitiez créer un code qui accepte deux entiers et retourne leur somme, vous pouvez définir une fonction qui fait cela de cette manière :

```c
int sum(int num1, int num2) {
   int result = num1 + num2;
   return result;
}

```

Dans cet exemple, la fonction `sum` prend deux paramètres entiers – `num1` et `num2`. La fonction calcule leur somme et retourne le résultat. Le type de retour de la fonction est `int`.

## Où une fonction doit-elle être définie ?

En C, une fonction peut être définie n'importe où dans le programme, tant qu'elle est définie avant d'être utilisée. Mais il est bon de définir les fonctions au début du fichier ou dans un fichier séparé pour rendre le code plus lisible et organisé.

Voici un exemple de code montrant comment définir une fonction en C :

```c
#include <stdio.h>

// déclaration de fonction (également connue sous le nom de prototype de fonction)
int add(int a, int b);

int main() {
   int x = 10, y = 20, sum;
   sum = add(x, y);
   printf("La somme de %d et %d est %d\n", x, y, sum);
   return 0;
}

// définition de fonction
int add(int a, int b) {
   int result;
   result = a + b;
   return result;
}

```

Dans cet exemple, la fonction `add()` est définie après sa déclaration (ou prototype) dans le même fichier.

Une autre approche consiste à définir la fonction dans un fichier d'en-tête séparé, qui est ensuite inclus dans le fichier principal en utilisant la directive `#include`. Par exemple :

```c
// fichier d'en-tête : math.h
#ifndef MATH_H
#define MATH_H

int add(int a, int b);

#endif

```

```c
// fichier principal : main.c
#include <stdio.h>
#include "math.h"  // inclure le fichier d'en-tête

int main() {
   int x = 10, y = 20, sum;
   sum = add(x, y);
   printf("La somme de %d et %d est %d\n", x, y, sum);
   return 0;
}
```

```c
// fichier d'implémentation : math.c
int add(int a, int b) {
   int result;
   result = a + b;
   return result;
}
```

Dans cette approche, la déclaration de fonction (ou prototype) est incluse dans le fichier d'en-tête `math.h`, qui est ensuite inclus dans le fichier principal `main.c` en utilisant la directive `#include`. La définition de la fonction est définie dans un fichier séparé `math.c`.

Cette approche permet une meilleure organisation du code et une meilleure modularité, car l'implémentation de la fonction peut être séparée du code principal du programme.

### Comment appeler une fonction en C

Nous pouvons appeler une fonction de n'importe où dans le programme une fois que nous l'avons définie. Nous utilisons le nom de la fonction suivi de la liste des arguments entre parenthèses pour appeler une fonction. Par exemple, nous pouvons utiliser le code suivant pour appeler la fonction `sum` que nous avons définie précédemment :

```c
int a = 5;
int b = 10;
int c = sum(a, b);

```

Dans ce code, nous appelons la fonction `sum` avec `a` et `b` comme ses paramètres. La fonction retourne la somme de `a` et `b`, qui est ensuite stockée dans la variable `c`.

## Comment passer des paramètres à une fonction

Il existe deux méthodes pour passer des paramètres (également appelés arguments) à une fonction en C : par valeur et par référence. 

Lorsque nous passons un paramètre par valeur, la méthode reçoit une copie de la valeur du paramètre. Les modifications apportées au paramètre dans le code n'ont aucun effet sur la variable initiale en dehors de la fonction. 

Lorsque nous passons un paramètre par référence, la méthode reçoit un lien vers l'emplacement mémoire du paramètre. Toute modification du paramètre dans le code aura un impact sur la variable initiale en dehors de la fonction.

Considérons les exemples suivants de passage de paramètres par valeur et par référence. Supposons que nous voulons créer une fonction qui accepte un entier et le multiplie par deux, la fonction peut être définie comme suit :

```c
void doubleValue(int num) {
   num = num * 2;
}

```

Dans cet exemple, la fonction `doubleValue` prend un paramètre entier `num` par valeur. Elle double la valeur de `num` et l'assigne à nouveau à `num`. Cependant, ce changement n'affectera pas la valeur originale de `num` en dehors de la fonction.

Voici un autre exemple qui montre comment vous pouvez passer un seul paramètre par valeur :

```c
#include <stdio.h>

void square(int num) {
    // Fonction pour calculer le carré d'un nombre.
    int result = num * num;
    printf("%d\n", result);
}

int main() {
    square(5);  // Sortie : 25
    return 0;
}

```

Dans cet exemple, nous définissons une fonction appelée `square` qui prend un paramètre entier `num` par valeur. À l'intérieur de la fonction, nous calculons le carré de `num` et imprimons le résultat. Nous appelons ensuite la fonction avec l'argument `5`.

Maintenant, regardons un exemple de passage d'un paramètre par référence :

```c
#include <stdio.h>

void square(int* num) {
    // Fonction pour calculer le carré d'un nombre.
    *num = (*num) * (*num);
}

int main() {
    int x = 5;
    square(&x);
    printf("%d\n", x);  // Sortie : 25
    return 0;
}

```

Dans cet exemple, nous définissons une fonction `square` qui prend un paramètre de pointeur entier `num` par référence. À l'intérieur de la fonction, nous référençons le pointeur et calculons le carré de la valeur pointée par `num`. 

Nous appelons ensuite la fonction avec l'adresse de la variable entière `x`. Après avoir appelé la fonction, la valeur de `x` est modifiée pour être le carré de sa valeur originale, que nous imprimons ensuite dans la fonction `main`.

## Conclusion

En conclusion, les fonctions sont un composant essentiel de la programmation C. Vous pouvez les utiliser pour diviser de grands problèmes en morceaux de code plus petits et plus faciles à gérer.

Vous pouvez déclarer et définir des fonctions en C, et passer des paramètres soit par valeur soit par référence. Il est bon de déclarer toutes les fonctions avant de les utiliser, et de les définir au début du fichier ou dans un fichier séparé pour une meilleure organisation du code et une meilleure modularité. 

En utilisant efficacement les fonctions, vous pouvez écrire un code plus propre, plus lisible, plus facile à déboguer et à maintenir.