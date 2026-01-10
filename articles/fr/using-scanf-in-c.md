---
title: Comment utiliser scanf() en C pour lire et stocker les entrées utilisateur
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-03-06T21:59:30.000Z'
originalURL: https://freecodecamp.org/news/using-scanf-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-element-digital-1370294.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Comment utiliser scanf() en C pour lire et stocker les entrées utilisateur
seo_desc: "The scanf() function is a commonly used input function in the C programming\
  \ language. It allows you to read input from the user or from a file and store that\
  \ input in variables of different data types. \nInput is an essential part of most\
  \ programs, an..."
---

La fonction `scanf()` est une fonction d'entrée couramment utilisée dans le langage de programmation C. Elle permet de lire des entrées de l'utilisateur ou d'un fichier et de stocker ces entrées dans des variables de différents types de données. 

L'entrée est une partie essentielle de la plupart des programmes, et la fonction `scanf()` fournit un moyen facile de lire des entrées dans une variété de formats. Mais il est important d'utiliser `scanf()` avec soin et de toujours valider les entrées utilisateur pour prévenir les vulnérabilités de sécurité et les comportements de programme inattendus. 

Dans cet article, nous allons examiner de plus près la fonction `scanf()` et comment l'utiliser efficacement en programmation C.

### **Ce que vous allez apprendre**

Voici quelques choses que vous allez apprendre :

1. Ce qu'est `scanf()` et à quoi il sert
2. Comment utiliser `scanf()` pour lire des entrées de l'utilisateur ou d'un fichier
3. La syntaxe de la fonction `scanf()` et comment utiliser les spécificateurs de conversion pour lire des entrées
4. Comment stocker des entrées dans des variables en utilisant des pointeurs
5. L'importance de la validation des entrées et de la vérification des erreurs pour prévenir les comportements de programme inattendus et les vulnérabilités de sécurité

## Syntaxe de la fonction `scanf()`

La syntaxe de base de la fonction `scanf()` est la suivante :

```c
int scanf(const char *format, ...);
```

La fonction `scanf()` retourne le nombre d'éléments lus avec succès, ou `EOF` si une erreur se produit ou si la fin du flux d'entrée est atteinte. 

La fonction prend deux arguments :

1. `format` : Une chaîne qui spécifie le format de l'entrée à lire. Cette chaîne peut contenir des spécificateurs de conversion qui indiquent à `scanf()` quel type d'entrée attendre et comment la lire. Voir la section suivante pour plus de détails sur les spécificateurs de conversion.
2. `...` : Une liste d'arguments de longueur variable qui contient les adresses mémoire des variables où les valeurs d'entrée seront stockées. Ces adresses mémoire doivent être passées sous forme de pointeurs.

## Comment utiliser les spécificateurs de conversion pour lire des entrées

La fonction `scanf()` prend une chaîne de format comme premier argument, qui spécifie le format et les types de données des entrées qui seront lues. 

La chaîne de format peut inclure des spécificateurs de conversion, qui commencent par le signe de pourcentage (`%`) et sont suivis d'un ou plusieurs caractères qui spécifient le type de données à lire. 

Les spécificateurs de conversion les plus courants sont :

* `%d` : lit une valeur entière
* `%f` : lit une valeur à virgule flottante
* `%c` : lit un caractère unique
* `%s` : lit une chaîne de caractères
* `%lf` : lit une valeur à virgule flottante de double précision

Après la chaîne de format, la fonction `scanf()` prend un nombre variable d'arguments, chacun étant un pointeur vers la variable où la valeur d'entrée sera stockée. Le nombre et le type des arguments doivent correspondre aux spécificateurs de conversion dans la chaîne de format.

Par exemple, le code suivant lit une valeur entière et une valeur à virgule flottante de l'utilisateur, et les stocke dans les variables `num` et `fnum`, respectivement :

```c
#include <stdio.h>

int main() {
    int num;
    float fnum;
    printf("Entrez un entier et un nombre à virgule flottante : ");
    scanf("%d %f", &num, &fnum);
    printf("Vous avez entré %d et %f\n", num, fnum);
    return 0;
}

```

Voici la sortie attendue :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-from-2023-03-06-11-06-14.png)
_sortie_

Dans cet exemple, la chaîne de format `"%d %f"` indique à `scanf()` de lire une valeur entière suivie d'une valeur à virgule flottante, séparées par un espace. L'opérateur `&` est utilisé pour passer l'adresse des variables `num` et `fnum` à `scanf()`, afin que les valeurs d'entrée puissent être stockées dans ces variables.

## Spécificateurs de conversion vs spécificateurs de type

Dans le langage de programmation C, les "spécificateurs de conversion" et les "spécificateurs de type" sont des concepts apparentés, mais ils ont des significations et des objectifs différents.

Un "spécificateur de type" est un mot-clé qui spécifie le type de données d'une variable ou d'une expression. Par exemple, les mots-clés `int`, `float` et `char` sont des spécificateurs de type qui indiquent respectivement les types de données entier, à virgule flottante et caractère. Nous utilisons des spécificateurs de type pour déclarer des variables et des fonctions et pour définir le type de retour d'une fonction.

En revanche, un "spécificateur de conversion" est un symbole que nous utilisons dans les chaînes de format pour spécifier le format des opérations d'entrée et de sortie. Les spécificateurs de conversion commencent par le caractère `%`, suivi d'une lettre unique ou d'une séquence de caractères qui indique le type de données à lire ou à écrire. Par exemple, le spécificateur de conversion `%d` lit des valeurs entières, tandis que le spécificateur `%f` lit des valeurs à virgule flottante.

En résumé, les spécificateurs de type sont utilisés pour spécifier le type de données des variables et des expressions, tandis que les spécificateurs de conversion sont utilisés pour spécifier le format des opérations d'entrée et de sortie. Les deux concepts sont importants en programmation C et sont utilisés dans différents contextes.

## Comment stocker des entrées dans des variables en utilisant des pointeurs

Pour stocker une entrée dans une variable en utilisant `scanf()`, vous devez passer l'adresse mémoire de la variable en tant qu'argument à la fonction en utilisant l'opérateur `&` (adresse de). Cela est dû au fait que `scanf()` attend des pointeurs comme arguments pour stocker les valeurs d'entrée directement dans les emplacements mémoire.

Voici un exemple d'utilisation de `scanf()` pour lire une valeur entière de l'utilisateur et la stocker dans une variable appelée `num` :

```c
int num;
printf("Entrez un entier : ");
scanf("%d", &num);
```

Dans cet exemple, le spécificateur de conversion `%d` indique à `scanf()` de s'attendre à une valeur d'entrée entière. L'adresse mémoire de la variable `num` est passée à `scanf()` en utilisant l'opérateur `&`, qui retourne un pointeur vers l'emplacement mémoire de `num`.

Si vous devez lire plusieurs valeurs d'entrée, vous pouvez passer plusieurs pointeurs comme arguments à `scanf()` dans l'ordre où ils apparaissent dans la chaîne de format. Par exemple, pour lire deux valeurs entières et les stocker dans les variables `num1` et `num2`, vous pourriez faire :

```c
int num1, num2;
printf("Entrez deux entiers : ");
scanf("%d %d", &num1, &num2);
```

Notez qu'il est important de vous assurer que les types de données des valeurs d'entrée correspondent aux types de données des variables dans lesquelles vous les stockez. Si les types ne correspondent pas, la valeur d'entrée peut être interprétée incorrectement, entraînant un comportement de programme inattendu. 

De plus, il est bon de valider les valeurs d'entrée et de gérer les erreurs d'entrée, comme discuté dans la section suivante.

## Validation des entrées et vérification des erreurs

La validation des entrées et la vérification des erreurs sont des concepts importants en programmation, surtout lorsqu'on traite avec des entrées utilisateur ou des entrées provenant de sources externes. En C, vous pouvez utiliser diverses techniques pour valider les entrées et gérer les erreurs d'entrée.

Une technique courante consiste à utiliser la valeur de retour de `scanf()` pour vérifier si l'opération d'entrée a réussi ou si une erreur s'est produite. La fonction `scanf()` retourne le nombre de valeurs d'entrée qui ont été lues et stockées avec succès, ou `EOF` si une erreur s'est produite ou si la fin du flux d'entrée a été atteinte. 

En vérifiant la valeur de retour, vous pouvez déterminer si l'opération d'entrée a réussi ou si une erreur s'est produite.

Par exemple, si vous utilisez `scanf()` pour lire une valeur entière de l'utilisateur et la stocker dans une variable appelée `num`, vous pourriez utiliser le code suivant pour valider l'entrée :

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;
    printf("Entrez un entier : ");
    if (scanf("%d", &num) != 1) {
        printf("Erreur : Entrée invalide\n");
        exit(1);
    }
    return 0;
}

```

Dans cet exemple, la fonction `scanf()` est utilisée pour lire une valeur entière et la stocker dans la variable `num`. La valeur de retour de `scanf()` est comparée à `1` pour vérifier si une valeur d'entrée a été lue et stockée avec succès. Si la valeur de retour n'est pas `1`, un message d'erreur est affiché sur la console et le programme se termine avec un code d'erreur.

Voici la sortie attendue :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-from-2023-03-06-11-02-36.png)
_Sortie_

Vous pouvez utiliser des techniques similaires pour valider les entrées d'autres types, tels que les nombres à virgule flottante ou les chaînes de caractères. Par exemple, pour valider l'entrée d'une valeur à virgule flottante, vous pourriez utiliser le spécificateur de conversion `%f` et vérifier si la valeur de retour de `scanf()` est égale à `1`.

En plus de vérifier la valeur de retour de `scanf()`, vous pouvez également utiliser d'autres techniques pour valider les entrées et gérer les erreurs, comme utiliser `fgets()` pour lire les entrées sous forme de chaîne de caractères et analyser ensuite la chaîne pour extraire les valeurs souhaitées, ou utiliser des expressions régulières pour valider les motifs d'entrée.

Il est important de valider soigneusement les entrées et de gérer les erreurs pour prévenir les comportements de programme inattendus ou les vulnérabilités de sécurité.

## `scanf()` et la bibliothèque standard C

La fonction `scanf()` est incluse dans la bibliothèque standard C, qui fournit une collection de fonctions pré-définies que vous pouvez utiliser dans les programmes C. Le fichier d'en-tête `stdio.h` fait également partie de la bibliothèque standard C et contient des déclarations pour les fonctions d'entrée et de sortie comme `scanf()`, `printf()`, et d'autres.

Pour utiliser la fonction `scanf()` dans un programme C, vous devez inclure le fichier d'en-tête `stdio.h` au début de votre programme en utilisant la directive de préprocesseur `#include`. Cela vous permet d'accéder aux fonctions et aux types de données définis dans la bibliothèque standard C, y compris `scanf()`.

Voici un exemple de comment utiliser `scanf()` dans un programme C :

```c
#include <stdio.h>

int main() {
    int num;
    printf("Entrez un entier : ");
    scanf("%d", &num);
    printf("Vous avez entré : %d\n", num);
    return 0;
}
```

Dans cet exemple, nous incluons d'abord le fichier d'en-tête `stdio.h` en utilisant `#include`. Nous définissons ensuite une variable `num` de type `int`. Nous utilisons la fonction `printf()` pour inviter l'utilisateur à entrer un entier, et la fonction `scanf()` lit l'entrée de l'utilisateur et la stocke dans la variable `num`. Enfin, nous utilisons une autre instruction `printf()` pour afficher la valeur de `num`.

Notez que nous utilisons l'opérateur `&` avant le nom de la variable dans la fonction `scanf()` pour passer l'adresse mémoire de la variable à la fonction. Cela permet à la fonction `scanf()` de stocker l'entrée de l'utilisateur directement dans la variable.

## Conclusion

La fonction `scanf()` en C est un outil puissant pour lire des entrées de l'utilisateur ou d'un fichier et les stocker dans des variables. En spécifiant des spécificateurs de conversion dans la chaîne de format, vous pouvez lire des valeurs d'entrée de différents types, tels que des entiers, des nombres à virgule flottante et des chaînes de caractères.

Lorsque vous utilisez `scanf()`, il est important d'être conscient des erreurs d'entrée potentielles et de valider les valeurs d'entrée pour prévenir les comportements de programme inattendus ou les vulnérabilités de sécurité. 

Vous pouvez utiliser la valeur de retour de `scanf()` pour vérifier si l'opération d'entrée a réussi. Vous pouvez également utiliser diverses techniques pour valider les entrées et gérer les erreurs, comme vérifier les plages d'entrée, utiliser des expressions régulières, ou convertir les valeurs d'entrée en chaînes de caractères et les analyser.

Dans l'ensemble, `scanf()` est une fonction polyvalente que vous pouvez utiliser dans une variété de scénarios de programmation. En comprenant comment utiliser `scanf()` efficacement et comment valider et gérer les erreurs d'entrée, vous pouvez construire des programmes C robustes et fiables qui interagissent avec les utilisateurs et les sources de données externes de manière sûre et sécurisée.