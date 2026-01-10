---
title: Tableaux d'entiers en C – Comment déclarer des tableaux d'entiers avec la programmation
  C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-13T17:22:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-integer-arrays-with-c-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nick-hillier-yD5rv8_WzxA-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Tableaux d'entiers en C – Comment déclarer des tableaux d'entiers avec
  la programmation C
seo_desc: "In this article, you will learn how to work with arrays in C.\nI will first\
  \ explain how to declare and initialize arrays. \nThen, I will also go over how\
  \ to access and change items in an array in C with the help of code examples along\
  \ the way.\nLet's ge..."
---

Dans cet article, vous apprendrez à travailler avec les tableaux en C.

Je vais d'abord expliquer comment déclarer et initialiser des tableaux. 

Ensuite, je passerai en revue la manière d'accéder et de modifier les éléments d'un tableau en C à l'aide d'exemples de code tout au long du parcours.

C'est parti !


## Qu'est-ce qu'un tableau en programmation C ?
Un tableau est une structure de données qui stocke plusieurs valeurs dans une seule variable et dans un ordre séquentiel facilement accessible.

Les tableaux en C sont une collection de valeurs qui stockent des éléments du même type de données – un tableau d'entiers ne contient que des éléments de type `int`, un tableau de flottants ne contient que des éléments de type `float`, et ainsi de suite.


## Comment déclarer un tableau d'entiers en programmation C
La syntaxe générale pour déclarer un tableau en C ressemble à ce que vous pouvez voir dans l'extrait de code ci-dessous :

```
data_type array_name[array_size];
```

Prenons l'exemple suivant :

```c
int my_numbers[5];
```

Décomposons-le :

- J'ai d'abord défini le type de données du tableau, `int`.
- J'ai ensuite spécifié le nom, `my_numbers`, suivi d'une paire de crochets ouvrants et fermants, `[]`.
- À l'intérieur des crochets, j'ai défini la taille (`5`), ce qui signifie que le tableau peut contenir `5` valeurs entières.
- Enfin, j'ai terminé l'instruction par un point-virgule (`;`).

Une fois que vous avez défini le type et la taille du tableau lors de la déclaration, le tableau ne peut pas contenir d'éléments d'un autre type.

Le tableau est également de taille fixe, ce qui signifie que vous ne pouvez pas ajouter ou supprimer d'éléments.


## Comment initialiser un tableau d'entiers en programmation C
Il existe plusieurs façons d'initialiser un tableau d'entiers en C.

La première façon consiste à initialiser le tableau lors de la déclaration et à insérer les valeurs à l'intérieur d'une paire d'accolades ouvrantes et fermantes, `{}`. 

La syntaxe générale pour ce faire ressemble à ceci :
```
data_type array_name[array_size] = {valeur1, valeur2, valeur3, ...};
```

Prenons le tableau que j'ai déclaré dans la section précédente qui peut contenir cinq entiers et initialisons-le avec quelques valeurs :
```c
int my_numbers[5] = {10, 20, 30, 40, 50};
```

Dans l'exemple ci-dessus, j'ai placé cinq valeurs séparées par des virgules à l'intérieur d'accolades, et j'ai assigné ces valeurs à `my_numbers` via l'opérateur d'affectation (`=`).

Une chose à noter ici est que lorsque vous spécifiez la taille du tableau, vous pouvez assigner un nombre inférieur d'éléments, comme ceci :
```c
int my_numbers[5] = {10, 20, 30};
```

Bien que la taille du tableau soit `5`, je n'ai placé que trois valeurs à l'intérieur. 

Le tableau peut contenir deux éléments supplémentaires, et ces deux positions restantes ont une valeur par défaut de `0`.

Une autre façon d'initialiser un tableau est de ne pas spécifier la taille, comme ceci :
```c
int my_numbers[] = {10, 20, 30, 40, 50};
```

Même si je n'ai pas défini la taille du tableau, le compilateur la connaît car il connaît le nombre d'éléments qui y sont stockés.


## Comment accéder aux éléments d'un tableau d'entiers en programmation C
Pour accéder à un élément d'un tableau, vous devez spécifier l'index de l'élément entre crochets après le nom du tableau.

La syntaxe pour accéder à un élément ressemble à ceci :
```
array_name[index_element]
```

En C et en programmation en général, l'index d'un tableau commence toujours à `0`, car en informatique, le comptage commence à `0`.

Ainsi, le premier élément d'un tableau a un index de `0`, le deuxième élément a un index de `1`, le troisième élément a un index de `2`, et ainsi de suite.

En reprenant le même tableau de la section précédente, voici comment vous accéderiez au premier élément, c'est-à-dire `10` :
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  printf("%d\n",my_numbers[0]);
  return 0;
}
```

Gardez à l'esprit que le dernier élément d'un tableau a un index de `array_size - 1` – il est toujours inférieur d'une unité à la taille du tableau. Ainsi, dans un tableau contenant cinq éléments, l'index du dernier élément est `4`.

Si dans un tableau de cinq éléments, vous essayez d'accéder au dernier élément en utilisant un index de `5`, le programme s'exécutera, mais l'élément n'est pas disponible et vous obtiendrez un comportement indéfini :
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  printf("%d\n",my_numbers[5]);
  return 0;
}

// sortie
// -463152408
```


## Comment modifier les éléments d'un tableau d'entiers en programmation C
Pour modifier la valeur d'un élément spécifique, spécifiez son numéro d'index et, avec l'opérateur d'affectation, `=`, assignez une nouvelle valeur :
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  my_numbers[0] = 11;
  return 0;
}
```

Dans l'exemple ci-dessus, j'ai changé le premier élément du tableau de `10` à `11`.


## Conclusion
Et voilà ! Vous connaissez maintenant les bases de l'utilisation des tableaux en C.

Pour en savoir plus sur le C, lisez ce [manuel du débutant en C](https://www.freecodecamp.org/news/the-c-beginners-handbook/) pour vous familiariser avec les bases du langage.

Merci de m'avoir lu, et bon codage !