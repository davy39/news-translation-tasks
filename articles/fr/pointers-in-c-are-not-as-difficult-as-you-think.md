---
title: Les pointeurs en C expliqués – Ils ne sont pas aussi difficiles que vous le
  pensez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-11T21:37:11.000Z'
originalURL: https://freecodecamp.org/news/pointers-in-c-are-not-as-difficult-as-you-think
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c994c740569d1a4ca1ef5.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Les pointeurs en C expliqués – Ils ne sont pas aussi difficiles que vous
  le pensez
seo_desc: 'By Srijan

  Pointers are arguably the most difficult feature of C to understand. But, they are
  one of the features which make C an excellent language.

  In this article, we will go from the very basics of pointers to their usage with
  arrays, functions, a...'
---

Par Srijan

Les pointeurs sont sans doute la caractéristique la plus difficile de C à comprendre. Mais ils font partie des fonctionnalités qui font de C un excellent langage.

Dans cet article, nous allons passer des bases des pointeurs à leur utilisation avec les tableaux, les fonctions et les structures.

Alors détendez-vous, prenez un café et préparez-vous à tout apprendre sur les pointeurs.

## Sujets

##### A. Fondamentaux

1. [Qu'est-ce que les pointeurs exactement ?](#heading-1-quest-ce-que-les-pointeurs)
2. [Définition et notation](#heading-2-definition-et-notation)
3. [Quelques pointeurs spéciaux](#heading-3-quelques-pointeurs-speciaux)
4. [Arithmétique des pointeurs](#heading-4-arithmetique-des-pointeurs)

##### B. Tableaux et chaînes de caractères

1. [Pourquoi les pointeurs et les tableaux ?](#heading-1-pourquoi-les-pointeurs-et-les-tableaux)
2. [Tableaux 1-D](#heading-2-tableaux-1-d)
3. [Tableaux 2-D](#heading-3-tableaux-2-d)
4. [Chaînes de caractères](#heading-4-chaines-de-caracteres)
5. [Tableau de pointeurs](#heading-5-tableau-de-pointeurs)
6. [Pointeur vers un tableau](#heading-6-pointeur-vers-un-tableau)

##### C. Fonctions

1. [Appel par valeur vs Appel par référence](#1-appel-par-valeur-vs-appel-par-reference)
2. [Pointeurs comme arguments de fonction](#heading-2-pointeurs-comme-arguments-de-fonction)
3. [Pointeurs comme retour de fonction](#heading-3-pointeurs-comme-retour-de-fonction)
4. [Pointeur vers une fonction](#heading-4-pointeur-vers-une-fonction)
5. [Tableau de pointeurs vers des fonctions](#heading-5-tableau-de-pointeurs-vers-des-fonctions)
6. [Pointeur vers une fonction comme argument](#heading-6-pointeur-vers-une-fonction-comme-argument)

##### D. Structure

1. [Pointeur vers une structure](#heading-1-pointeur-vers-une-structure)
2. [Tableau de structures](#heading-2-tableau-de-structures)
3. [Pointeur vers une structure comme argument](#heading-3-pointeur-vers-une-structure-comme-argument)

##### E. Pointeur vers un pointeur

##### F. Conclusion



## A. Définition, notation, types et arithmétique

### 1. Qu'est-ce que les pointeurs exactement ?

Avant d'arriver à la définition des pointeurs, comprenons ce qui se passe lorsque nous écrivons le code suivant :

```c
int digit = 42;

```

![Qu'est-ce que les pointeurs exactement ?](https://i.gyazo.com/971e405f8dff71e187f627e154077e7d.png)

Un bloc de mémoire est réservé par le compilateur pour contenir une valeur `int`. Le nom de ce bloc est `digit` et la valeur stockée dans ce bloc est `42`. 

Maintenant, pour mémoriser le bloc, il est assigné avec une **adresse** ou un numéro de localisation (disons, 24650).

La valeur du numéro de localisation n'est pas importante pour nous, car c'est une valeur aléatoire. Mais nous pouvons accéder à cette adresse en utilisant l'opérateur `&` (esperluette) ou **adresse de**.

```c
printf("L'adresse de digit = %d.", &digit);
 /* imprime "L'adresse de digit = 24650. */

```

Nous pouvons obtenir la valeur de la variable `digit` à partir de son adresse en utilisant un autre opérateur `*` (astérisque), appelé l'opérateur **indirection** ou **déréférencement** ou **valeur à l'adresse**.

```c
printf("La valeur de digit = %d.", *(&digit);
 /* imprime "La valeur de digit = 42. */

```

### 2. Définition et notation

L'adresse d'une variable peut être stockée dans une autre variable connue sous le nom de variable pointeur. La syntaxe pour stocker l'adresse d'une variable dans un pointeur est :

```c
dataType *pointerVariableName = &variableName;

```

Pour notre variable `digit`, cela peut s'écrire comme ceci :

```c
int *addressOfDigit = &digit;

```

ou comme ceci :

```c
int *addressOfDigit;
addressOfDigit = &digit;

```

![Déclaration et définition](https://www.freecodecamp.org/news/content/images/2020/08/456d4568d6e2c00e377b9dfae76e1809.gif)

Cela peut se lire comme - _Un pointeur vers `int` (entier) `addressOfDigit` stocke l'`adresse de(&)` la variable `digit`._

#### Quelques points à comprendre :

`dataType` – Nous devons indiquer à l'ordinateur quel est le type de données de la variable dont nous allons stocker l'adresse. Ici, `int` était le type de données de `digit`. 

Cela **ne signifie pas** que `addressOfDigit` stockera une valeur de type `int`. Un pointeur d'entier (comme `addressOfDigit`) ne peut **que** stocker l'adresse de variables de type entier.

```c
int variable1;
int variable2;
char variable3;
int *addressOfVariables;

```

`*` – Une variable pointeur est une variable _spéciale_ dans le sens où elle est utilisée pour stocker une adresse d'une autre variable. Pour la différencier des autres variables qui ne stockent pas une adresse, nous utilisons `*` comme symbole dans la déclaration.

Ici, nous pouvons assigner l'adresse de `variable1` et `variable2` au pointeur d'entier `addressOfVariables` mais pas à `variable3` puisque celle-ci est de type `char`. Nous aurons besoin d'une variable pointeur de caractère pour stocker son adresse.

Nous pouvons utiliser notre variable pointeur `addressOfDigit` pour imprimer l'adresse et la valeur de `digit` comme ci-dessous :

```c
printf("L'adresse de digit = %d.", addressOfDigit);
 /* imprime "L'adresse de digit = 24650." */
printf("La valeur de digit = %d.", *addressOfDigit);
 /* imprime "La valeur de digit = 42. */

```

Ici, `*addressOfDigit` peut se lire comme _la valeur à l'adresse stockée dans `addressOfDigit`._

Remarquez que nous avons utilisé `%d` comme **identifiant de format** pour `addressOfDigit`. Eh bien, ce n'est pas complètement correct. L'identifiant correct serait `%p`.

En utilisant `%p`, l'adresse est affichée comme une valeur hexadécimale. Mais l'adresse mémoire peut être affichée en entiers ainsi qu'en valeurs octales. Cependant, puisque ce n'est pas une manière _entièrement correcte_, un avertissement est affiché.

```c
int num = 5;
int *p = &num;
printf("Adresse en utilisant %%p = %p", p);
printf("Adresse en utilisant %%d = %d", p);
printf("Adresse en utilisant %%o = %o", p);

```

La sortie selon le compilateur que j'utilise est la suivante :

```c
Adresse en utilisant %p = 000000000061FE00
Adresse en utilisant %d = 6422016
Adresse en utilisant %o = 30377000

```

> Voici l'avertissement affiché lorsque vous utilisez %d - " warning: format '%d' expects argument of type 'int', but argument 2 has type 'int *' ".

### 3. Quelques pointeurs spéciaux

#### Le pointeur sauvage

```c
char *alphabetAddress; /* pointeur non initialisé ou sauvage */
char alphabet = "a";
alphabetAddress = &alphabet; /* maintenant, ce n'est plus un pointeur sauvage */

```

Lorsque nous avons défini notre pointeur de caractère `alphabetAddress`, nous ne l'avons pas initialisé. 

De tels pointeurs sont connus sous le nom de **pointeurs sauvages**. Ils stockent une valeur aléatoire (c'est-à-dire une adresse mémoire) d'un octet dont nous ne savons pas s'il est réservé ou non (souvenez-vous de `int digit = 42;` nous avons réservé une adresse mémoire lorsque nous l'avons déclaré).

Supposons que nous déréférencions un pointeur sauvage et que nous assignons une valeur à l'adresse mémoire vers laquelle il pointe. Cela conduira à un comportement inattendu puisque nous allons écrire des données dans un bloc mémoire qui peut être libre ou réservé.

#### Pointeur nul

Pour nous assurer que nous n'avons pas de pointeur sauvage, nous pouvons initialiser un pointeur avec une valeur `NULL`, en faisant un **pointeur nul**.

```c
char *alphabetAddress = NULL /* Pointeur nul */ 

```

Un pointeur nul ne pointe vers rien, ou vers une adresse mémoire à laquelle les utilisateurs ne peuvent pas accéder.

#### Pointeur void

Un **pointeur void** peut être utilisé pour pointer vers une variable de n'importe quel type de données. Il peut être réutilisé pour pointer vers n'importe quel type de données que nous voulons. Il est déclaré comme ceci :

```c
void *pointerVariableName = NULL;

```

Puisqu'ils sont très _généraux_ par nature, ils sont également connus sous le nom de **pointeurs génériques**.

Avec leur flexibilité, les pointeurs void apportent également quelques contraintes. Les pointeurs void **ne peuvent pas** être déréférencés comme n'importe quel autre pointeur. Un _casting de type_ approprié est nécessaire.

```c
void *pointer = NULL;
int number = 54;
char alphabet = "z";
pointer = &number;
printf("La valeur de number = ", *pointer); /* Erreur de compilation */
/* Méthode correcte */
printf("La valeur de number = ", *(int *)pointer); /* imprime "La valeur à number = 54" */
pointer = &alphabet;
printf("La valeur de alphabet = ", *pointer); /* Erreur de compilation */
printf("La valeur de alphabet = ", *(char *)pointer); /* imprime "La valeur à alphabet = z */

```

De même, les pointeurs void doivent être castés pour effectuer des opérations arithmétiques.

Les pointeurs void sont très utiles en C. Les fonctions de bibliothèque `malloc()` et `calloc()` qui allouent dynamiquement de la mémoire retournent des pointeurs void. `qsort()`, une fonction de tri intégrée en C, a une fonction comme argument qui elle-même prend des pointeurs void comme arguments.

#### Pointeur pendouillant

Un pointeur pendouillant pointe vers une adresse mémoire qui **contenait** une variable. Puisque l'adresse vers laquelle il pointe n'est plus réservée, son utilisation conduira à des résultats inattendus.

```c
main(){
  int *ptr;
  ptr = (int *)malloc(sizeof(int));
  *ptr = 1;
  printf("%d",*ptr); /* imprime 1 */
  free(ptr); /* désallocation */
  *ptr = 5;
  printf("%d",*ptr); /* peut ou non imprimer 5 */
}

```

Bien que la mémoire ait été désallouée par `free(ptr)`, le pointeur vers l'entier `ptr` pointe toujours vers cette adresse mémoire non réservée.

### 4. Arithmétique des pointeurs

Nous savons maintenant que les pointeurs ne sont pas comme n'importe quelle autre variable. Ils ne stockent aucune valeur mais l'adresse des blocs mémoire. 

Il devrait donc être assez clair que toutes les opérations arithmétiques ne seraient pas valides avec eux. Est-ce que multiplier ou diviser deux pointeurs (_ayants des adresses_) aurait du sens ?

#### Les pointeurs ont peu mais immensément utiles **opérations valides** :

1.  Vous pouvez assigner la valeur d'un pointeur à un autre seulement s'ils sont du même type (sauf s'ils sont castés ou si l'un d'eux est `void *`).

```c
int ManU = 1;
int *addressOfManU = &ManU;
int *anotherAddressOfManU = NULL;
anotherAddressOfManU = addressOfManU; /* Valide */
double *wrongAddressOfManU = addressOfManU; /* Invalide */

```

2.   Vous ne pouvez **ajouter ou soustraire que des entiers** aux pointeurs.

```c
int myArray = {3,6,9,12,15};
int *pointerToMyArray = &myArray[0];
pointerToMyArray += 3; /* Valide */
pointerToMyArray *= 3; /* Invalide */

```

Lorsque vous ajoutez (ou soustrayez) un entier (disons n) à un pointeur, vous n'ajoutez (ou ne soustrayez) **pas** réellement n octets à la valeur du pointeur. Vous ajoutez (ou soustrayez) en réalité n-_fois la taille du type de données de la variable pointée_ octets.

```c
int number = 5;
 /* Supposons que l'adresse de number est 100 */
int *ptr = &number;
int newAddress = ptr + 3;
 /* Équivalent à ptr + 3 * sizeof(int) */

```

La valeur stockée dans `newAddress` **ne** sera pas 103, mais plutôt `112`.

3.  **Soustraction et comparaison de pointeurs** est valide seulement si les deux sont membres du même tableau. La soustraction de pointeurs donne le nombre d'éléments qui les séparent.

```c
int myArray = {3,6,9,12,15};
int sixthMultiple = 18;
int *pointer1 = &myArray[0];
int *pointer2 = &myArray[1];
int *pointer6 = &sixthMuliple;
 /* Expressions valides */
if(pointer1 == pointer2)
pointer2 - pointer1;
 /* Expressions invalides
if(pointer1 == pointer6)
pointer2 - pointer6

```

4.  Vous pouvez assigner ou comparer un pointeur avec `NULL`.

> _La seule exception aux règles ci-dessus est que l'adresse du premier bloc mémoire après le dernier élément d'un tableau suit l'arithmétique des pointeurs._

Les pointeurs et les tableaux existent ensemble. Ces manipulations valides des pointeurs sont extrêmement utiles avec les tableaux, ce qui sera discuté dans la section suivante.

## B. Tableaux et chaînes de caractères

### 1. Pourquoi les pointeurs et les tableaux ?

En C, les pointeurs et les tableaux ont une relation assez forte. 

La raison pour laquelle ils **devraient** être discutés ensemble est que ce que vous pouvez réaliser avec la notation des tableaux (`arrayName[index]`) peut également être réalisé avec des pointeurs, mais généralement plus rapidement.

### 2. Tableaux 1-D

Regardons ce qui se passe lorsque nous écrivons `int myArray[5];`.

Cinq blocs de mémoire **consécutifs** commençant de `myArray[0]` à `myArray[4]` sont créés avec des valeurs aléatoires. Chacun des blocs fait 4 octets.

Ainsi, si l'adresse de myArray[0] est `100` (disons), l'adresse du reste des blocs serait `104`, `108`, `112`, et `116`.

Jetez un coup d'œil au code suivant :

```c
int prime[5] = {2,3,5,7,11};
printf("Résultat en utilisant &prime = %d\n", &prime);
printf("Résultat en utilisant prime = %d\n", prime);
printf("Résultat en utilisant &prime[0] = %d\n", &prime[0]);

/* Sortie */
Résultat en utilisant &prime = 6422016
Résultat en utilisant prime = 6422016
Résultat en utilisant &prime[0] = 6422016

```

Donc, `&prime`, `prime`, et `&prime[0]` donnent tous la même adresse, n'est-ce pas ? Eh bien, attendez et lisez car vous allez avoir une surprise (et peut-être une certaine confusion). 

Essayons d'incrémenter chacun de `&prime`, `prime`, et `&prime[0]` de 1.

```c
printf("Résultat en utilisant &prime = %d\n", &prime + 1);
printf("Résultat en utilisant prime = %d\n", prime + 1);
printf("Résultat en utilisant &prime[0] = %d\n", &prime[0] + 1);

/* Sortie */
Résultat en utilisant &prime = 6422036
Résultat en utilisant prime = 6422020
Résultat en utilisant &prime[0] = 6422020

```

Attendez ! Comment se fait-il que `&prime + 1` donne quelque chose de différent des deux autres ? Et pourquoi `prime + 1` et `&prime[0] + 1` sont-ils encore égaux ? Répondons à ces questions.

`prime` et `&prime[0]` pointent tous deux vers le 0ème élément du tableau `prime`. Ainsi, **le nom d'un tableau est lui-même un pointeur vers le 0ème élément du tableau**.

Ici, les deux pointent vers le premier élément de taille 4 octets. Lorsque vous ajoutez 1 à eux, ils pointent maintenant vers le 1er élément du tableau. Par conséquent, cela entraîne une augmentation de l'adresse de 4.

`&prime`, en revanche, est **un pointeur vers un tableau `int` de taille 5**. Il stocke l'adresse de base du tableau `prime[5]`, qui est égale à l'adresse du premier élément. Cependant, une augmentation de 1 entraîne une adresse avec une augmentation de 5 x 4 = 20 octets.

En résumé, `arrayName` et `&arrayName[0]` pointent vers le 0ème élément alors que `&arrayName` pointe vers le tableau entier.

![Tableau 1-D](https://www.freecodecamp.org/news/content/images/2020/08/09f8f82032f04a27fce46cc048644f8d.gif)

Nous pouvons accéder aux éléments du tableau en utilisant des variables indicées comme ceci :

```c
int prime[5] = {2,3,5,7,11};
for( int i = 0; i < 5; i++)
{
  printf("index = %d, address = %d, value = %d\n", i, &prime[i], prime[i]);
}

```

Nous pouvons faire de même en utilisant des pointeurs qui sont **toujours** plus rapides qu'en utilisant des indices.

```c
int prime[5] = {2,3,5,7,11};
for( int i = 0; i < 5; i++)
{
  printf("index = %d, address = %d, value = %d\n", i, prime + i, *(prime + i));
}

```

Les deux méthodes donnent la sortie :

```c
index = 0, address = 6422016, value = 2
index = 1, address = 6422020, value = 3
index = 2, address = 6422024, value = 5
index = 3, address = 6422028, value = 7
index = 4, address = 6422032, value = 11

```

Ainsi, `&arrayName[i]` et `arrayName[i]` sont les mêmes que `arrayName + i` et  `*(arrayName + i)`, respectivement.

### 3. Tableaux 2-D

Les tableaux à deux dimensions sont un tableau de tableaux.

```c
int marks[5][3] = { { 98, 76, 89},
                    { 81, 96, 79},
                    { 88, 86, 89},
                    { 97, 94, 99},
                    { 92, 81, 59}
                  };

```

Ici, `marks` peut être considéré comme un tableau de 5 éléments, chacun d'eux étant un tableau à une dimension contenant 3 entiers. Travaillons à travers une série de programmes pour comprendre différentes expressions indicées.

```c
printf("Adresse du tableau 2-D entier = %d\n", &marks);
printf("L'addition de 1 donne %d\n", &marks +1);

/* Sortie */
Adresse du tableau 2-D entier = 6421984
L'addition de 1 donne 6422044

```

Comme pour les tableaux 1-D, `&marks` pointe vers le tableau 2-D entier, `marks[5][3]`. Ainsi, l'incrémentation de 1 ( = 5 tableaux X 3 entiers chacun X 4 octets = 60) entraîne une augmentation de 60 octets.

```c
printf("Adresse du 0ème tableau = %d\n", marks);
printf("L'addition de 1 donne %d\n", marks +1);
printf("Adresse du 0ème tableau =%d\n", &marks[0]);
printf("L'addition de 1 donne %d\n", &marks[0] + 1);

/* Sortie */
Adresse du 0ème tableau = 6421984
L'addition de 1 donne 6421996
Adresse du 0ème tableau = 6421984
L'addition de 1 donne 6421996

```

Si `marks` était un tableau 1-D, `marks` et `&marks[0]` auraient pointé vers le `0ème` élément. **Pour un tableau 2-D, les éléments sont maintenant des tableaux 1-D**. Par conséquent, `marks` et `&marks[0]` pointent vers le `0ème` tableau (élément), et l'addition de 1 pointe vers le `1er` tableau.

```c
printf("Adresse du 0ème élément du 0ème tableau = %d\n", marks[0]);
printf("L'addition de 1 donne %d\n", marks[0] + 1);
printf("Adresse du 0ème élément du 1er tableau = %d\n", marks[1]);
printf("L'addition de 1 donne %d\n", marks[1] + 1);

 /* Sortie */
Adresse du 0ème élément du 0ème tableau = 6421984
L'addition de 1 donne 6421988
Adresse du 0ème élément du 1er tableau = 6421996
L'addition de 1 donne 6422000

```

Et maintenant vient la différence. Pour un tableau 1-D, `marks[0]` donnerait la valeur du 0ème élément. Une incrémentation de 1 augmenterait la valeur de 1.

Mais, dans un tableau 2-D, `marks[0]` pointe vers le `0ème` élément du `0ème` tableau. De même, `marks[1]` pointe vers le `0ème` élément du `1er` tableau. Une incrémentation de 1 pointerait vers le `1er` élément du `1er` tableau.

```c
printf("Valeur du 0ème élément du 0ème tableau = %d\n", marks[0][0]);
printf("L'addition de 1 donne %d", marks[0][0] + 1);

/* Sortie */
Valeur du 0ème élément du 0ème tableau = 98
L'addition de 1 donne 99

```

C'est la nouvelle partie. `marks[i][j]` donne la valeur du `jème` élément du `ième` tableau. Une incrémentation de celui-ci change la valeur stockée à `marks[i][j]`. Maintenant, essayons d'écrire `marks[i][j]` en termes de pointeurs.

Nous savons que `marks[i] + j` pointerait vers le `ième` élément du `jème` tableau à partir de notre discussion précédente. Le déréférencer signifierait la valeur à cette adresse. Ainsi, **`marks[i][j]` est la même chose que `*(marks[i] + j)`**.

À partir de notre discussion sur les tableaux 1-D, `marks[i]` est la même chose que `*(marks + i)`. Ainsi, **`marks[i][j]` peut s'écrire `*(*(marks + i) + j)`** en termes de pointeurs.

Voici un résumé des notations comparant les tableaux 1-D et 2-D.

<table>
    <style>
        table
        { width: 10%;
        }
        th
        {text-align:center;}
    </style>
    <tr>
        <th>Expression</th>
    	<th>Tableau 1-D</th>
        <th>Tableau 2-D</th>
    </tr>
    <tr>
        <td>&arrayName</td>
        <td>pointe vers l'adresse du tableau entier <br>ajouter 1 augmente l'adresse de 1 x sizeof(arrayName)</td>
        <td>pointe vers l'adresse du tableau entier<br>ajouter 1 augmente l'adresse de 1 x sizeof(arrayName)</td>
    </tr>
    <tr>
        <td>arrayName</td>
        <td>pointe vers le 0ème élément<br>ajouter 1 augmente l'adresse vers le 1er élément</td>
        <td>pointe vers le 0ème élément (tableau)<br>ajouter 1 augmente l'adresse vers le 1er élément (tableau)</td>
    </tr>
    <tr>
        <td>&arrayName[i]</td>
        <td>pointe vers le ième élément<br>ajouter 1 augmente l'adresse vers le (i+1)ème élément</td>
        <td>pointe vers le ième élément (tableau)<br>ajouter 1 augmente l'adresse vers le (i+1)ème élément (tableau)</td>
    </tr>
    <tr>
        <td>arrayName[i]</td>
        <td>donne la valeur du ième élément<br>ajouter 1 augmente la valeur du ième élément</td>
        <td>pointe vers le 0ème élément du ième tableau<br>ajouter 1 augmente l'adresse vers le 1er élément du ième tableau</td>
    </tr>
    <tr>
        <td>arrayName[i][j]</td>
        <td>Rien</td>
        <td>donne la valeur du jème élément du ième tableau<br>ajouter 1 augmente la valeur du jème élément du ième tableau</td>
    </tr>
    <tr>
        <td>Expression de pointeur pour accéder aux éléments</td>
        <td>*( arrayName + i)</td>
        <td>*( *( arrayName + i) + j)</td>
    </tr>
</table>

### 4. Chaînes de caractères

Une chaîne de caractères est un tableau à une dimension de caractères terminé par un `null(\0)`. Lorsque nous écrivons `char name[] = "Srijan";`, chaque caractère occupe un octet de mémoire, le dernier étant toujours `\0`.

De manière similaire aux tableaux que nous avons vus, `name` et `&name[0]` pointent vers le `0ème` caractère de la chaîne, tandis que `&name` pointe vers la chaîne entière. De plus, `name[i]` peut s'écrire `*(name + i)`.

```c
/* Chaîne de caractères */
char champions[] = "Liverpool";

printf("Pointeur vers la chaîne entière = %d\n", &champions);
printf("L'addition de 1 donne %d\n", &champions + 1);

/* Sortie */
Adresse de la chaîne entière = 6421974
L'addition de 1 donne 6421984

printf("Pointeur vers le 0ème caractère = %d\n", &champions[0]);
printf("L'addition de 1 donne %d\n", &champions[0] + 1);

/* Sortie */
Adresse du 0ème caractère = 6421974
L'addition de 1 donne un pointeur vers le 1er caractère 6421975

printf("Pointeur vers le 0ème caractère = %d\n", champions);
printf("L'addition de 1 donne un pointeur vers le 1er caractère %d\n", champions + 1);

/* Sortie */
Adresse du 0ème caractère = 6421974
L'addition de 1 donne 6421975

printf("Valeur du 4ème caractère = %c\n", champions[4]);
printf("Valeur du 4ème caractère en utilisant des pointeurs = %c\n", *(champions + 4));

/* Sortie */
Valeur du 4ème caractère = r
Valeur du 4ème caractère en utilisant des pointeurs = r

```

Un tableau à deux dimensions de caractères ou un tableau de chaînes de caractères peut également être accédé et manipulé comme discuté précédemment.

```c
/* Tableau de chaînes de caractères */
char top[6][15] = {
                    "Liverpool",
                    "Man City",
                    "Man United",
                    "Chelsea",
                    "Leicester",
                    "Tottenham"
                  };

printf("Pointeur vers le tableau 2-D = %d\n", &top);
printf("L'addition de 1 donne %d\n", &top + 1);

 /* Sortie */
Pointeur vers le tableau 2-D = 6421952
L'addition de 1 donne 6422042

printf("Pointeur vers la 0ème chaîne = %d\n", &top[0]);
printf("L'addition de 1 donne %d\n", &top[0] + 1);

 /* Sortie */
Pointeur vers la 0ème chaîne = 6421952
L'addition de 1 donne 6421967

printf("Pointeur vers la 0ème chaîne = %d\n", top);
printf("L'addition de 1 donne %d\n", top + 1);

 /* Sortie */
Pointeur vers la 0ème chaîne = 6421952
L'addition de 1 donne 6421967

printf("Pointeur vers le 0ème élément de la 4ème chaîne = %d\n", top[4]);
printf("Pointeur vers le 1er élément de la 4ème chaîne = %c\n", top[4] + 1);

 /* Sortie */
Pointeur vers le 0ème élément de la 4ème chaîne = 6422012
Pointeur vers le 1er élément de la 4ème chaîne = 6422013

printf("Valeur du 1er caractère dans la 3ème chaîne = %c\n", top[3][1]);
printf("Même en utilisant des pointeurs = %c\n", *(*(top + 3) + 1));

 /* Sortie */
Valeur du 1er caractère dans la 3ème chaîne = h
Même en utilisant des pointeurs = h

```

### 5. Tableau de pointeurs

Comme un tableau d'`int` et un tableau de `char`, il existe également un tableau de pointeurs. Un tel tableau serait simplement une collection d'adresses. Ces adresses pourraient pointer vers des variables individuelles ou un autre tableau.

La syntaxe pour déclarer un **tableau de pointeurs** est la suivante :

```c
dataType *variableName[size];

/* Exemples */
int *example1[5];
char *example2[8];

```

En suivant la [priorité des opérateurs](http://unixwiz.net/techtips/reading-cdecl.html), le premier exemple peut se lire comme - _`example1` est un tableau(`[]`) de 5 pointeurs vers `int`_. De même, _`example2` est un tableau de 8 pointeurs vers `char`_.

Nous pouvons stocker le tableau à deux dimensions de chaînes `top` en utilisant un tableau de pointeurs et économiser de la mémoire.

```c
char *top[] = {
                    "Liverpool",
                    "Man City",
                    "Man United",
                    "Chelsea",
                    "Leicester",
                    "Tottenham"
                  };

```

`top` contiendra les adresses de base de tous les noms respectifs. L'adresse de base de `"Liverpool"` sera stockée dans `top[0]`, `"Man City"` dans `top[1]`, et ainsi de suite.

Dans la déclaration précédente, nous avions besoin de 90 octets pour stocker les noms. Ici, nous n'avons besoin que de (58 (somme des octets des noms) + 12 (octets nécessaires pour stocker l'adresse dans le tableau)) 70 octets.

La manipulation de chaînes de caractères ou d'entiers devient beaucoup plus facile lorsque l'on utilise un tableau de pointeurs.

Si nous essayons de mettre `"Leicester"` devant `"Chelsea"`, nous devons simplement échanger les valeurs de `top[3]` et `top[4]` comme ci-dessous :

```c
char *temporary;
temporary = top[3];
top[3] = top[4];
top[4] = temporary;

```

Sans pointeurs, nous aurions dû échanger chaque caractère des chaînes, ce qui aurait pris plus de temps. C'est pourquoi les chaînes de caractères sont généralement déclarées en utilisant des pointeurs.

### 6. Pointeur vers un tableau

Comme "pointeur vers `int`" ou "pointeur vers `char`", nous avons également un pointeur vers un tableau. Ce pointeur pointe vers le tableau entier plutôt que vers ses éléments.

Souvenez-vous, nous avons discuté de la manière dont `&arrayName` pointe vers le tableau entier ? Eh bien, c'est un pointeur vers un tableau.

Un pointeur vers un tableau peut être déclaré comme ceci :

```c
dataType (*variableName)[size];

/* Exemples */
int (*ptr1)[5];
char (*ptr2)[15];

```

Remarquez les parenthèses. Sans elles, ce serait un tableau de pointeurs. Le premier exemple peut se lire comme - _`ptr1` est un pointeur vers un tableau de 5 `int`(entiers)_.

```c
int goals[] = { 85,102,66,69,67};
int (*pointerToGoals)[5] = &goals;
printf("Adresse stockée dans pointerToGoals %d\n", pointerToGoals);
printf("Déréférençant, nous obtenons %d\n",*pointerToGoals);

/* Sortie */
Adresse stockée dans pointerToGoals 6422016
Déréférençant, nous obtenons 6422016

```

Lorsque nous déréférençons un pointeur, il donne la valeur à cette adresse. De même, en déréférençant un pointeur vers un tableau, nous obtenons le tableau et le nom du tableau pointe vers l'adresse de base. Nous pouvons confirmer que `*pointerToGoals` donne le tableau `goals` si nous trouvons sa taille.

```c
printf("Taille de goals[5] = %d, *pointerToGoals);

/* Sortie */
Taille de goals[5] = 20

```

Si nous le déréférençons à nouveau, nous obtiendrons la valeur stockée à cette adresse. Nous pouvons imprimer tous les éléments en utilisant `pointerToGoals`.

```c
for(int i = 0; i < 5; i++)
printf("%d ", *(*pointerToGoals + i));

/* Sortie */
85 102 66 69 67

```

Les pointeurs et les pointeurs vers des tableaux sont très utiles lorsqu'ils sont associés à des fonctions. À venir dans la section suivante !

## C. Fonctions

### 1. Appel par valeur vs Appel par référence

Jetez un coup d'œil au programme ci-dessous :

```c
#include <stdio.h>

int multiply(int x, int y){
  int z;
  z = x * y;
  return z;
}

main(){
int x = 3, y = 5; 
int product = multiply(x,y);
printf("Produit = %d\n", product);
 /* imprime "Produit = 15" */
}

```

La fonction `multiply()` prend deux arguments `int` et retourne leur produit en tant que `int`. 

Dans l'appel de fonction `multiply(x,y)`, nous avons passé la valeur de `x` et `y` (de `main()`), qui sont des _arguments réels_, à `multiply()`.

Les valeurs des arguments réels sont passées ou copiées vers les _arguments formels_ `x` et `y` (de `multiply()`). Le `x` et `y` de `multiply()` sont différents de ceux de `main()`. Cela peut être vérifié en imprimant leurs adresses.

```c
#include <stdio.h>

int multiply(int x, int y){
  printf("Adresse de x dans multiply() = %d\n", &x);
  printf("Adresse de y dans multiply() = %d\n", &y);
  int z;
  z = x * y;
  return z;
}

main(){
int x = 3, y = 5;
printf("Adresse de x dans main() = %d\n", &x);
printf("Adresse de y dans main() = %d\n", &y);
int product = multiply(x,y);
printf("Produit = %d\n", product);
}

/* Sortie */
Adresse de x dans main() = 6422040
Adresse de y dans main() = 6422036
Adresse de x dans multiply() = 6422000
Adresse de y dans multiply() = 6422008
Produit = 15

```

Puisque nous avons créé des valeurs stockées dans un nouvel emplacement, cela nous coûte de la mémoire. Ne serait-il pas mieux si nous pouvions effectuer la même tâche sans gaspiller d'espace ?

**L'appel par référence** nous aide à atteindre cet objectif. Nous passons l'adresse ou la référence des variables à la fonction qui ne crée pas de copie. En utilisant l'opérateur de déréférencement `*`, nous pouvons accéder à la valeur stockée à ces adresses.

Nous pouvons réécrire le programme ci-dessus en utilisant l'appel par référence.

```c
#include <stdio.h>

int multiply(int *x, int *y){
  int z;
  z = (*x) * (*y);
  return z;
}

main(){
int x = 3, y = 5; 
int product = multiply(&x,&y);
printf("Produit = %d\n", product);
 /* imprime "Produit = 15" */
}

```

### 2. Pointeurs comme arguments de fonction

Dans cette section, nous allons examiner divers programmes où nous donnons `int`, `char`, des tableaux et des chaînes de caractères comme arguments en utilisant des pointeurs.

```c
#include <stdio.h>

void add(float *a, float *b){
 float c = *a + *b;
 printf("L'addition donne %.2f\n",c);
}

void subtract(float *a, float *b){
 float c = *a - *b;
 printf("La soustraction donne %.2f\n",c);
}

void multiply(float *a, float *b){
 float c = *a * *b;
 printf("La multiplication donne %.2f\n",c);
}

void divide(float *a, float *b){
 float c = *a / *b;
 printf("La division donne %.2f\n",c);
}

main(){
    printf("Entrez deux nombres :\n");
    float a,b;
    scanf("%f %f",&a,&b);
    printf("Que voulez-vous faire avec les nombres?\nAddition : a\nSoustraction : s\nMultiplication : m\nDivision : d\n");
    char operation = '0';
    scanf(" %c",&operation);
    printf("\nOpération en cours...\n\n");
    switch (operation) {
    case 'a':
        add(&a,&b);
        break;
    case 's':
        subtract(&a,&b);
        break;
    case 'm':
        multiply(&a,&b);
        break;
    case 'd':
        divide(&a,&b);
        break;
    default:
        printf("Entrée invalide!!!\n");

  }

}

```

Nous avons créé quatre fonctions, `add()`, `subtract()`, `multiply()` et `divide()` pour effectuer des opérations arithmétiques sur les deux nombres `a` et `b`. 

L'adresse de `a` et `b` a été passée aux fonctions. À l'intérieur de la fonction, en utilisant `*` nous avons accédé aux valeurs et imprimé le résultat.

De même, nous pouvons donner des tableaux comme arguments en utilisant un pointeur vers leur premier élément.

```c
#include <stdio.h>

void greatestOfAll( int *p){
 int max = *p;
 for(int i=0; i < 5; i++){
    if(*(p+i) > max)
        max = *(p+i);
 }
 printf("Le plus grand élément est %d\n",max);
 }
main(){
  int myNumbers[5] = { 34, 65, -456, 0, 3455};
  greatestOfAll(myNumbers);
   /* Imprime : "Le plus grand élément est 3455" */
}

```

Puisque le nom d'un tableau est lui-même un pointeur vers le premier élément, nous envoyons cela comme argument à la fonction `greatestOfAll()`. Dans la fonction, nous parcourons le tableau en utilisant une boucle et un pointeur.

```c
#include <stdio.h>
#include <string.h>

void wish(char *p){
 printf("Passez une bonne journée, %s",p);
}

main(){
 printf("Entrez votre nom : \n");
 char name[20];
 gets(name);
 wish(name);
}

```

Ici, nous passons la chaîne de caractères `name` à `wish()` en utilisant un pointeur et imprimons le message.

### 3. Pointeurs comme retour de fonction

```c
#include <stdio.h>

int* multiply(int *a, int *b){
 int c = *a * *b;
 return &c;
}

main(){
int a= 3, b = 5;
int *c = multiply (&a,&b);
printf("Produit = %d",*c);
}

```

La fonction `multiply()` prend deux pointeurs vers `int`. Elle retourne également un pointeur vers `int` qui stocke l'adresse où le produit est stocké.

Il est très facile de penser que la sortie serait 15. Mais ce n'est pas le cas !

Lorsque `multiply()` est appelée, l'exécution de `main()` est suspendue et la mémoire est maintenant allouée pour l'exécution de `multiply()`. Après que son exécution soit terminée, la mémoire allouée à `multiply()` est désallouée.

Par conséquent, bien que `c` (local à `main()`) stocke l'adresse du produit, les données à cet endroit ne sont **pas garanties** puisque cette mémoire a été désallouée.

Cela signifie-t-il que les pointeurs ne peuvent pas être retournés par une fonction ? Non !

Nous pouvons faire deux choses. Soit stocker l'adresse dans le tas ou la section globale, soit déclarer la variable comme `static` afin que leurs valeurs persistent.

Les variables statiques peuvent simplement être créées en utilisant le _mot-clé_ `static` avant le type de données lors de la déclaration de la variable.

Pour stocker des adresses dans le tas, nous pouvons utiliser les fonctions de bibliothèque `malloc()` et `calloc()` qui allouent de la mémoire dynamiquement. 

Les programmes suivants expliqueront les deux méthodes. Les deux méthodes retournent la sortie comme 15.

```c
#include <stdio.h>
#include <stdlib.h>

/* Utilisation de malloc() */

int* multiply(int *a, int *b){
 int *c = malloc(sizeof(int));
 *c = *a * *b;
 return c;
}

main(){
int a= 3, b = 5;
int *c = multiply (&a,&b);
printf("Produit = %d",*c);
}

/* Utilisation du mot-clé static */
#include <stdio.h>

int* multiply(int *a, int *b){
 static int c;
 c = *a * *b;
 return &c;
}

main(){
int a= 3, b = 5;
int *c = multiply (&a,&b);
printf("Produit = %d",*c);
}

```

### 4. Pointeur vers une fonction

Comme les pointeurs vers différents types de données, nous avons également un pointeur vers une fonction. 

Un pointeur vers une fonction ou **pointeur de fonction** stocke l'adresse de la fonction. Bien qu'il ne pointe vers aucune donnée. Il pointe vers la première instruction de la fonction.

La syntaxe pour déclarer un pointeur vers une fonction est :

```c
 /* Déclaration d'une fonction */
returnType functionName(parameterType1, pparameterType2, ...);

 /* Déclaration d'un pointeur vers une fonction */
returnType (*pointerName)(parameterType1, parameterType2, ...);
pointerName = &functionName; /* ou pointerName = functionName; */

```

L'exemple ci-dessous rendra cela plus clair.

```c
int* multiply(int *a, int *b)
{
    int *c = malloc(sizeof(int));
    *c = *a * *b;
    return c;
}

main()
{ 
    int a=3,b=5;
    int* (*p)(int*, int*) = &multiply; /* ou int* (*p)(int*, int*) = multiply; */
    int *c = (*p)(&a,&b); /* ou int *c = p(&a,&b); */
    printf("Produit = %d",*c);
}

```

La déclaration pour le pointeur `p` vers la fonction `multiply()` peut se lire comme (suivant la [priorité des opérateurs](http://unixwiz.net/techtips/reading-cdecl.html)) - _`p` est un pointeur vers une fonction avec deux pointeurs `int` (ou deux pointeurs vers `int`) comme paramètres et retournant un pointeur vers `int`_.

Puisque le nom de la fonction est également un pointeur vers la fonction, l'utilisation de `&` n'est pas nécessaire. De plus, supprimer `*` de l'appel de fonction n'affecte pas le programme.

### 5. Tableau de pointeurs vers des fonctions

Nous avons déjà vu comment créer un tableau de pointeurs vers `int`, `char`, et ainsi de suite. De même, nous pouvons créer un tableau de pointeurs vers des fonctions.

Dans ce tableau, chaque élément stockera une adresse de fonction, où toutes les fonctions sont du même type. C'est-à-dire qu'elles ont le même type et nombre de paramètres et types de retour.

Nous allons modifier un programme discuté précédemment dans cette section. Nous allons stocker les adresses de `add()`, `subtract()`, `multiply()` et `divide()` dans un tableau et faire un appel de fonction par indice.

```c
#include <stdio.h>

void add(float *a, float *b){
 float c = *a + *b;
 printf("L'addition donne %.2f\n",c);
}

void subtract(float *a, float *b){
 float c = *a - *b;
 printf("La soustraction donne %.2f\n",c);
}

void multiply(float *a, float *b){
 float c = *a * *b;
 printf("La multiplication donne %.2f\n",c);
}

void divide(float *a, float *b){
 float c = *a / *b;
 printf("La division donne %.2f\n",c);
}

main(){
    printf("Entrez deux nombres :\n");
    float a,b;
    scanf("%f %f",&a,&b);
    printf("Que voulez-vous faire avec les nombres?\nAddition : a\nSoustraction : s\nMultiplication : m\nDivision : d\n");
    char operation = '0';
    scanf(" %c",&operation);
    void (*p[])(float* , float*) = {add,subtract,multiply,divide};
    printf("\nOpération en cours...\n\n");
    switch (operation) {
    case 'a':
        p[0](&a,&b);
        break;
    case 's':
        p[1](&a,&b);
        break;
    case 'm':
        p[2](&a,&b);
        break;
    case 'd':
        p[3](&a,&b);
        break;
    default:
        printf("Entrée invalide!!!\n");

  }

}

```

La déclaration ici peut se lire comme - _`p` est un tableau de pointeurs vers des fonctions avec deux pointeurs `float` comme paramètres et retournant void_.

### 6. Pointeur vers une fonction comme argument

Comme n'importe quel autre pointeur, les pointeurs de fonction peuvent également être passés à une autre fonction, donc connus sous le nom de **fonction de rappel** ou **fonction appelée**. La fonction à laquelle il est passé est connue sous le nom de **fonction appelante**. 

Une meilleure façon de comprendre serait de regarder `qsort()`, qui est une fonction intégrée en C. Elle est utilisée pour trier un tableau d'entiers, de chaînes de caractères, de structures, et ainsi de suite. La déclaration pour `qsort()` est :

```c
void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));

```

`qsort()` prend quatre arguments :

1. un pointeur `void` vers le début d'un tableau
2. le nombre d'éléments
3. la taille de chaque élément
4. un pointeur de fonction qui prend deux pointeurs `void` comme arguments et retourne un `int`

Le pointeur de fonction pointe vers une _fonction de comparaison_ qui retourne un entier qui est supérieur, égal ou inférieur à zéro si le premier argument est respectivement supérieur, égal ou inférieur au second argument.

Le programme suivant montre son utilisation :

```c
#include <stdio.h>
#include <stdlib.h>

int compareIntegers(const void *a, const void *b)
{
  const int *x = a;
  const int *y = b;
  return *x - *y;
}

main(){

  int myArray[] = {97,59,2,83,19,97};
  int numberOfElements = sizeof(myArray) / sizeof(int);

  printf("Avant le tri - \n");
  for(int i = 0; i < numberOfElements; i++)
   printf("%d ", *(myArray + i));

  qsort(myArray, numberOfElements, sizeof(int), compareIntegers);

  printf("\n\nAprès le tri - \n");
  for(int i = 0; i < numberOfElements; i++)
   printf("%d ", *(myArray + i));
 }

/* Sortie */

Avant le tri -
97 59 2 83 19 97

Après le tri -
2 19 59 83 97 97

```

Puisqu'un nom de fonction est lui-même un pointeur, nous pouvons écrire `compareIntegers` comme quatrième argument.

## D. Structure

### 1. Pointeur vers une structure

Comme les pointeurs d'entiers, les pointeurs de tableaux et les pointeurs de fonctions, nous avons également des pointeurs vers des structures ou des pointeurs de structure.

```c
struct records {
    char name[20];
    int roll;
    int marks[5];
    char gender;
};

struct records student = {"Alex", 43, {76, 98, 68, 87, 93}, 'M'};

struct records *ptrStudent = &student;

```

Ici, nous avons déclaré un pointeur `ptrStudent` de type `struct records`. Nous avons assigné l'adresse de `student` à `ptrStudent`.

`ptrStudent` stocke l'adresse de base de `student`, qui est l'adresse de base du premier membre de la structure. L'incrémentation de 1 augmenterait l'adresse de `sizeof(student)` octets.

```c
printf("Adresse de la structure = %d\n", ptrStudent);
printf("Adresse du membre `name` = %d\n", &student.name);
printf("Incrémentation de 1 donne %d\n", ptrStudent + 1);

/* Sortie */
Adresse de la structure = 6421984
Adresse du membre `name` = 6421984
Incrémentation de 1 donne 6422032

```

Nous pouvons accéder aux membres de `student` en utilisant `ptrStudent` de deux manières. En utilisant notre vieil ami `*` ou en utilisant `->` (**opérateur infixe ou flèche**).

Avec `*`, nous continuerons à utiliser le `.` (opérateur point) alors qu'avec `->` nous n'aurons pas besoin de l'opérateur point.

```c
printf("Nom sans utiliser ptrStudent : %s\n", student.name);
printf("Nom en utilisant ptrStudent et * : %s\n", ( *ptrStudent).name);
printf("Nom en utilisant ptrStudent et -> : %s\n", ptrStudent->name);

/* Sortie */
Nom sans utiliser ptrStudent : Alex
Nom en utilisant ptrStudent et * : Alex
Nom en utilisant ptrStudent et -> : Alex

```

De même, nous pouvons accéder et modifier d'autres membres. Notez que les parenthèses sont nécessaires lors de l'utilisation de `*` puisque l'opérateur point (`.`) a une priorité plus élevée que `*`.

### 2. Tableau de structures

Nous pouvons créer un tableau de type `struct records` et utiliser un pointeur pour accéder aux éléments et à leurs membres.

```c
struct records students[10];

 /* Pointeur vers le premier élément (structure) du tableau */
struct records *ptrStudents1 = &students;

 /* Pointeur vers un tableau de 10 struct records */
struct records (*ptrStudents2)[10] = &students;

```

Notez que `ptrStudent1` est un pointeur vers `student[0]` alors que `ptrStudent2` est un pointeur vers le tableau entier de 10 `struct records`. Ajouter 1 à `ptrStudent1` pointerait vers `student[1]`.

Nous pouvons utiliser `ptrStudent1` avec une boucle pour parcourir les éléments et leurs membres.

```c

for( int i = 0; i <  10; i++)
printf("%s, %d\n", ( ptrStudents1 + i)->name, ( ptrStudents1 + i)->roll);

```

### 3. Pointeur vers une structure comme argument

Nous pouvons également passer l'adresse d'une variable de structure à une fonction.

```c
#include <stdio.h>

struct records {
    char name[20];
    int roll;
    int marks[5];
    char gender;
};

main(){
 struct records students = {"Alex", 43, {76, 98, 68, 87, 93}, 
'M'};
 printRecords(&students);
}

void printRecords( struct records *ptr){
  printf("Nom : %s\n", ptr->name);
  printf("Roll : %d\n", ptr->roll);
  printf("Genre : %c\n", ptr->gender);
  for( int i = 0; i < 5; i++)
   printf("Notes dans le %dème sujet : %d\n", i, ptr->marks[i]);
}

 /* Sortie */
Nom : Alex
Roll : 43
Genre : M
Notes dans le 0ème sujet : 76
Notes dans le 1ème sujet : 98
Notes dans le 2ème sujet : 68
Notes dans le 3ème sujet : 87
Notes dans le 4ème sujet : 93

```

Notez que la structure `struct records` est déclarée en dehors de `main()`. Cela est pour s'assurer qu'elle est disponible globalement et que `printRecords()` peut l'utiliser.

Si la structure est définie à l'intérieur de `main()`, sa portée sera limitée à `main()`. De plus, la structure **doit** être déclarée avant la déclaration de la fonction également.

> Comme les structures, nous pouvons avoir des pointeurs vers des unions et accéder aux membres en utilisant l'opérateur flèche (`->`).

## E. Pointeur vers un pointeur

Jusqu'à présent, nous avons examiné les pointeurs vers divers types de données primitifs, tableaux, chaînes de caractères, fonctions, structures et unions.

La question automatique qui vient à l'esprit est – qu'en est-il des pointeurs vers des pointeurs ?

Eh bien, bonne nouvelle pour vous ! Ils existent aussi.

```c
int var = 6;
int *ptr_var = &var;

printf("Adresse de var = %d\n", ptr_var);
printf("Adresse de ptr_var = %d\n", &ptr_var);

/* Sortie */
Adresse de var = 6422036
Adresse de ptr_var = 6422024

```

Pour stocker l'adresse de la variable `int` `var`, nous avons le pointeur vers `int` `ptr_var`. Nous aurions besoin d'un autre pointeur pour stocker l'adresse de `ptr_var`.

Puisque `ptr_var` est de type `int *`, pour stocker son adresse, nous devrions créer un pointeur vers `int *`. Le code ci-dessous montre comment cela peut être fait.

```c
int * *ptr_ptrvar = &ptr_var; /* ou int* *ppvar ou int **ppvar */

```

Nous pouvons utiliser `ptr_ptrvar` pour accéder à l'adresse de `ptr_var` et utiliser le double déréférencement pour accéder à var.

```c
printf("Adresse de ptr_var = %d\n", ptr_ptrvar);
printf("Adresse de var = %d\n", *ptr_ptrvar);
printf("Valeur à var = %d\n", *(*ptr_ptrvar));

/* Sortie */
Adresse de ptr_var = 6422024
Adresse de var = 6422036
Valeur à var = 6

```

Il n'est pas nécessaire d'utiliser des crochets lors du déréférencement de `ptr_ptrvar`. Mais c'est une bonne pratique de les utiliser. Nous pouvons créer un autre pointeur `ptr_ptrptrvar`, qui stockera l'adresse de `ptr_ptrvar`.

Puisque `ptr_ptrvar` est de type `int**`, la déclaration pour `ptr_ptrptrvar` sera

```c
int** *ptr_ptrptrvar = &ptr_ptrvar;

```

Nous pouvons à nouveau accéder à `ptr_ptrvar`, `ptr_var` et `var` en utilisant `ptr_ptrptrvar`.

```c
printf("Adresse de ptr_ptrvar = %d\n", ptr_ptrptrvar);
printf("Valeur à ptr_ptrvar = %d\n",*ptr_ptrptrvar);
printf("Adresse de ptr_var = %d\n", *ptr_ptrptrvar);
printf("Valeur à ptr_var = %d\n", *(*ptr_ptrptrvar));
printf("Adresse de var = %d\n", *(*ptr_ptrptrvar));
printf("Valeur à var = %d\n", *(*(*ptr_ptrptrvar)));

/* Sortie */
Adresse de ptr_ptrvar = 6422016
Valeur à ptr_ptrvar = 6422024
Adresse de ptr_var = 6422024
Valeur à ptr_var = 6422036
Adresse de var = 6422036
Valeur à var = 6

```

![Pointeur vers un pointeur](https://www.freecodecamp.org/news/content/images/2020/08/1534533aefc96880ba542070037d147b.gif)

Si nous changeons la valeur à l'un des pointeurs en utilisant `ptr_ptrptrvar` ou `ptr_ptrvar`, le(s) pointeur(s) cesseront de pointer vers la variable.

## Conclusion

Ouf ! Oui, nous avons terminé. Nous avons commencé avec les pointeurs et terminé avec les pointeurs (d'une certaine manière). Ne disent-ils pas que _la courbe d'apprentissage est un cercle !_

Essayez de récapituler tous les sous-sujets que vous avez lus. Si vous pouvez vous en souvenir, bien joué ! Relisez ceux dont vous ne vous souvenez pas.

Cet article est terminé, mais vous ne devriez pas avoir fini avec les pointeurs. Jouez avec eux. Ensuite, vous pouvez regarder l'_Allocation Dynamique de Mémoire_ pour mieux connaître les pointeurs.

Restez chez vous, restez en sécurité.