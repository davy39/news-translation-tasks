---
title: Comment trouver la taille d'un tableau en C avec l'opérateur sizeof
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-05T14:53:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-the-size-of-an-array-in-c-with-the-sizeof-operator
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-eduardo-dutra-2115217-1.jpg
tags:
- name: arrays
  slug: arrays
- name: c programming
  slug: c-programming
seo_title: Comment trouver la taille d'un tableau en C avec l'opérateur sizeof
seo_desc: 'When coding in the C programming language, there may be times when you
  need to know the size of an array.

  For example, when you want to loop through all the elements stored in the array
  to determine whether a specific value is present.

  In this articl...'
---

Lorsque vous codez en langage de programmation C, il peut arriver que vous ayez besoin de connaître la taille d'un tableau.

Par exemple, lorsque vous souhaitez parcourir tous les éléments stockés dans le tableau pour déterminer si une valeur spécifique est présente.

Dans cet article, vous apprendrez à trouver la taille d'un tableau en utilisant l'opérateur `sizeof()`.

Commençons !

## Qu'est-ce qu'un tableau en langage de programmation C ?

Les tableaux vous permettent de stocker plusieurs valeurs sous le même nom de variable.

Un tableau en langage de programmation C est une collection d'éléments du même type de données. Cela signifie que vous pouvez créer un tableau de valeurs entières uniquement ou un tableau de `char` et ainsi de suite.

Pour créer un tableau en C, vous devez d'abord spécifier le type de données des valeurs que le tableau stockera.

Ensuite, vous donnez un nom au tableau suivi d'une paire de crochets, `[]`.

À l'intérieur des crochets, vous pouvez spécifier la taille du tableau.

Voici donc comment vous créeriez un tableau de type `int` appelé `faveNumbers` qui contiendra `5` entiers :

```c
int faveNumbers[5];
```

Pour insérer des valeurs à l'intérieur du tableau lors de sa déclaration, utilisez l'opérateur d'affectation, `=`, et une paire d'accolades, `{}`.

À l'intérieur des accolades, entrez les éléments et séparez chacun d'eux par une virgule :

```c
int faveNumbers[5] = {7, 33, 13, 9, 29};
```

Le code ci-dessus crée un tableau avec le nom `faveNumbers` qui contient `5` entiers, `7, 33, 13, 9, 29`.

Vous pourriez également écrire le code ci-dessus comme suit :

```c
int faveNumbers[] = {7, 33, 13, 9, 29};
```

Dans l'exemple ci-dessus, je n'ai pas spécifié la taille du tableau.

Cependant, le compilateur peut dire que la taille est `5` puisque je l'ai initialisé avec `5` éléments.

Une chose à noter ici est que vous ne pouvez pas changer la taille et le type du tableau une fois que vous l'avez déclaré puisque ils ont une longueur fixe.

## Comment trouver la taille d'un tableau en langage de programmation C

C ne fournit pas de moyen intégré pour obtenir la taille d'un tableau.

Cela dit, il dispose de l'opérateur intégré `sizeof`, que vous pouvez utiliser pour déterminer la taille.

La syntaxe générale pour utiliser l'opérateur `sizeof` est la suivante :

```
type_de_donnees taille = sizeof(nom_du_tableau) / sizeof(nom_du_tableau[index]);
```

Décomposons cela :

- `taille` est le nom de la variable qui stocke la taille du tableau, et `type_de_donnees` spécifie le type de valeur de données stockée dans `taille`.
- `sizeof(nom_du_tableau)` calcule la taille du tableau en octets.
- `sizeof(nom_du_tableau[index])` calcule la taille d'un élément dans le tableau.

Maintenant, voyons cette opération en action et décomposons-la en étapes individuelles pour voir comment elle fonctionne.

Tout d'abord, l'opérateur `sizeof` retourne la quantité totale de mémoire allouée au tableau en octets.

```c
#include <stdio.h>
int main() {
    // mon tableau
    int faveNumbers[] = {7, 33, 13, 9, 29};

    // utilisation de sizeof pour obtenir la taille du tableau en octets
    size_t taille = sizeof(faveNumbers);
    
    printf("La taille est de %d octets \n", taille);
}

// sortie

// La taille est de 20 octets
```

Cependant, le code ci-dessus ne calcule pas directement la taille du tableau.

Vous aurez besoin d'une logique de programmation supplémentaire, qui ressemblera à ceci :

```
longueur_du_tableau = (taille totale du tableau) / (taille du premier élément du tableau)
```

Pour trouver la longueur du tableau, vous devez diviser la quantité totale de mémoire par la taille d'un élément - cette méthode fonctionne parce que le tableau stocke des éléments du même type.

Vous pouvez donc diviser le nombre total d'octets par la taille du premier élément du tableau.

Pour accéder au premier élément d'un tableau, spécifiez le nom et, entre crochets, incluez `0`.

En programmation et en informatique en général, l'indexation commence toujours à `0`, donc le premier élément d'un tableau aura toujours un index de `0`.


```c
#include <stdio.h>
int main() {
    int faveNumbers[] = {7, 33, 13, 9, 29};

    size_t taille = sizeof(faveNumbers) / sizeof(faveNumbers[0]);
  
    printf("La longueur du tableau est de %d \n", taille);
}

// sortie

// La longueur du tableau est de 5
```

Une chose à noter ici est que la taille des types de données variera d'une plateforme à l'autre.

## Conclusion

Espérons que cet article vous a aidé à comprendre comment trouver la taille d'un tableau en langage de programmation C en utilisant l'opérateur intégré `sizeof`.

Merci d'avoir lu, et bon codage !