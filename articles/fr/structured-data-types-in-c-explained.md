---
title: Types de données structurées en C expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-19T22:03:18.000Z'
originalURL: https://freecodecamp.org/news/structured-data-types-in-c-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9924740569d1a4ca1e14.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Types de données structurées en C expliqués
seo_desc: "By Srijan\nThere are variables of different data types in C, such as ints,\
  \ chars, and floats. And they let you store data. \nAnd we have arrays to group\
  \ together a collection of data of the same data type.\nBut in reality, we will\
  \ not always have the lu..."
---

Par Srijan

Il existe des variables de différents types de données en C, telles que les `int`, les `char` et les `float`. Et elles vous permettent de stocker des données. 

Et nous avons des tableaux pour regrouper une collection de données du même type de données.

Mais en réalité, nous n'aurons pas toujours le luxe d'avoir des données d'un seul type. C'est là qu'intervient une **structure**. Dans cet article, nous en apprendrons davantage sur les types de données structurées en C.

## Table des matières

**A. Fondamentaux**

1. [Définition et déclaration](#heading-1-definition-et-declaration)
2. [Initialisation et accès aux membres d'une structure](#heading-2-initialisation-et-acces-aux-membres-dune-structure)
3. [Opérations avec une variable de structure](#heading-3-operations-avec-une-variable-de-structure)
4. [Tableau de structures](#heading-4-tableau-de-structures)
5. [Structure imbriquée](#heading-5-structure-imbriquee)

**B. Allocation de mémoire**

1. [Alignement des données](#heading-1-alignement-des-donnees)
2. [Remplissage de structure](#heading-2-remplissage-de-structure)
3. [Alignement des membres de la structure](#heading-3-alignement-des-membres-de-la-structure)
4. [Compactage de structure](#heading-4-compactage-de-structure)

**C. Pointeurs**

1. [Pointeur en tant que membre](#heading-1-pointeur-en-tant-que-membre)
2. [Pointeur vers une structure](#heading-2-pointeur-vers-une-structure)
3. [Pointeur et tableau de structures](#heading-3-pointeur-et-tableau-de-structures)

**D. Fonctions**

1. [Fonction en tant que membre](#heading-1-fonction-en-tant-que-membre)
2. [Structure en tant qu'argument de fonction](#heading-2-structure-en-tant-quargument-de-fonction)
3. [Structure en tant que retour de fonction](#heading-3-structure-en-tant-que-retour-de-fonction)

**E. Structures auto-référentielles**

**F. Conclusion**

Commençons, d'accord ?

## Fondamentaux

### 1. Définition et déclaration

Une structure est une **collection** d'une ou plusieurs variables, éventuellement de types différents, regroupées sous un seul nom. C'est un type de données **définis par l'utilisateur**. 

Elles aident à organiser des données compliquées dans de grands programmes, car elles permettent de traiter un groupe de variables logiquement liées comme une seule.

Par exemple, un étudiant peut avoir des propriétés de nom, d'âge, de sexe et de notes. Nous pourrions créer un tableau de `char` pour le `nom`, une variable `int` pour le `numéro`, une variable `char` pour le sexe, et un tableau `int` pour les `notes`. 

Mais s'il y a 20 ou 100 étudiants, il sera difficile de gérer ces variables.

Nous pouvons déclarer une structure en utilisant le mot-clé `struct` suivant la syntaxe ci-dessous :

```c
 /* Syntaxe */
 struct nomStructure
        {
            typeDonnee membreVariable1;
            typeDonnee membreVariable2;
            ...
        };

 /* Exemple */
struct etudiant
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    };

```

L'instruction ci-dessus définit un nouveau type de données `struct etudiant`. Chaque variable de ce type de données comprendra `nom[20]`, `numero`, `sexe` et `notes[5]`. Ce sont les **membres** de la structure.

Une fois qu'une structure est déclarée comme un nouveau type de données, les variables de ce type de données peuvent être créées.

```c
 /* Déclaration de variable */
struct nomStructure variableStructure;

 /* Exemple /*
struct etudiant et1;
struct etudiant et2,et3,et4;

```

Chaque variable de `struct etudiant` a ses propres copies des membres.

**Quelques points importants :**

1. Les membres de la structure n'occupent pas de mémoire jusqu'à ce qu'une variable de structure soit créée.
2. Vous avez peut-être remarqué que nous utilisons `struct` comme une déclaration de variable également. N'est-ce pas fastidieux ?

En utilisant le mot-clé `typedef` dans la déclaration de la structure, nous pouvons éviter d'avoir à écrire `struct` à nouveau.

```c
typedef struct etudiants
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    } ETUDIANT; 

/* ou */
typedef struct
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    } ETUDIANT; 


ETUDIANT et1,et2,et3,et4;

```

Par convention, les lettres **majuscules** sont utilisées pour les _définitions de types_ (comme `ETUDIANT`).

3. La définition de la structure et la déclaration de variable peuvent être combinées comme ci-dessous.

```c
struct etudiant
    {
        char nom[20];
        int numero;
        chat sexe;
        int notes[5];
    }et1, et2, et3, et4;

```

4. L'utilisation de `nomStructure` est facultative. Le code ci-dessous est complètement valide.

```c
struct
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    }et1, et2, et3, et4;

```

5. Les structures sont généralement déclarées en haut du fichier de code source, même avant de définir les fonctions (vous verrez pourquoi).

6. C n'autorise pas l'initialisation de variable à l'intérieur d'une déclaration de structure.

### 2. Initialisation et accès aux membres d'une structure

Comme toute autre variable, une variable de structure peut également être initialisée là où elle est déclarée. Il existe une relation un-à-un entre les membres et leurs valeurs d'initialisation.

```c
 /* Initialisation de variable */
struct nomStructure = { valeur1, valeur2,...};

 /* Exemple */
typedef struct
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    }ETUDIANT;

void main(){
ETUDIANT et1 = { "Alex", 43, 'M', {76, 78, 56, 98, 92}};
ETUDIANT et2 = { "Max", 33, 'M', {87, 84, 82, 96, 78}};
}

```

Pour accéder aux membres, nous devons utiliser `.` (l'**opérateur point**).

```c
 /* Accès aux membres d'une structure */
variableStructure.membreVariable

/* Exemple */
 printf("Nom: %s\n", et1.nom);
 printf("Numéro: %d\n", et1.numero);
 printf("Sexe: %c\n", et1.sexe);
 for( int i = 0; i < 5; i++)
   printf("Notes dans la %dème matière: %d\n", i, et1.notes[i]);

/* Sortie */
Nom: Alex
Numéro: 43
Sexe: M
Notes dans la 0ème matière: 76
Notes dans la 1ère matière: 78
Notes dans la 2ème matière: 56
Notes dans la 3ème matière: 98
Notes dans la 4ème matière: 92

```

Les membres peuvent être initialisés dans la déclaration de variable dans n'importe quel ordre en utilisant `.`.

```c
ETUDIANT et3 = { .sexe = 'M', .numero = 23, .nom = "Gasly", .notes = { 99, 45, 67, 78, 94}};

```

Nous pouvons également initialiser les premiers membres et laisser les autres vides. Cependant, les membres non initialisés doivent être **uniquement** à la fin de la liste.

Les `int` et les nombres à virgule flottante non initialisés ont une valeur par défaut de `0`. C'est `\0` (NULL) pour les `char` et les chaînes de caractères.

```c
ETUDIANT et4 = { "Kviyat", 65};
 /* équivalent à { "Kviyat", 65, '\0', { 0, 0, 0, 0, 0} } */

```

### 3. Opérations avec la variable de structure

Comme les variables de types de données primitifs, nous ne pouvons pas effectuer d'opérations arithmétiques telles que `+`, `-`, `*`, `/`, et ainsi de suite. De même, les opérateurs relationnels et d'égalité ne peuvent pas être utilisés avec les variables de structure. 

Mais, nous pouvons copier une variable de structure dans une autre, à condition qu'elles appartiennent à la même structure.

```c
 /* Opérations invalides */
et1 + et2
et1 - et2
et1 == et2
et1 != et2 etc.

 /* Opération valide */
et1 = et2

```

Nous devrons comparer les membres de la structure individuellement pour comparer les variables de structure.

```c
#include <stdio.h>
#include <string.h>

 struct etudiant
    {
        char nom[20];
        double numero;
        char sexe;
        int notes[5];
    }et1,et2;


void main()
{
    struct etudiant et1= { "Alex", 43, 'M', {76, 78, 56, 98, 92}};
    struct etudiant et2 = { "Max", 33, 'M', {87, 84, 82, 96, 78}};

    if( strcmp(et1.nom,et2.nom) == 0 && et1.numero == et2.numero)
        printf("Les deux sont les enregistrements du même étudiant.\n");
    else printf("Enregistrements différents, étudiants différents.\n");

     /* Copie de la variable de structure */
    et2 = et1;

    if( strcmp(et1.nom,et2.nom) == 0 && et1.numero == et2.numero)
        printf("\nLes deux sont les enregistrements du même étudiant.\n");
    else printf("\nEnregistrements différents, étudiants différents.\n");
}

 /* Sortie */
Enregistrements différents, étudiants différents.

Les deux sont les enregistrements du même étudiant.


```

### 4. Tableau de structures

Vous avez déjà vu comment nous avons dû créer 4 variables différentes de type `struct etudiant` pour stocker les enregistrements de 4 étudiants. 

Une meilleure façon serait de créer un tableau de `struct etudiant` (comme un tableau de `int`).

```c
struct etudiant
    {
        char nom[20];
        double numero;
        char sexe;
        int notes[5];
    };

struct etudiant etu[4];

```

Pour accéder aux éléments du tableau `etu` et aux membres de chaque élément, nous pouvons utiliser des boucles.

```c
 /* Prendre les valeurs de l'utilisateur */

for(int i = 0; i < 4; i++)
    {
        printf("Entrez le nom:\n");
        scanf("%s",&etu[i].nom);
        printf("Entrez le numéro:\n");
        scanf("%d",&etu[i].numero);
        printf("Entrez le sexe:\n");
        scanf(" %c",&etu[i].sexe);

        for( int j = 0; j < 5; j++)
        {
            printf("Entrez les notes de la %dème matière:\n",j);
            scanf("%d",&etu[i].notes[j]);
        }

        printf("\n-------------------\n\n");
    }

 /* Trouver les notes moyennes et les afficher */

for(int i = 0; i < 4; i++)
    {
        float sum = 0;
        for( int j = 0; j < 5; j++)
        {
            sum += etu[i].notes[j];
        }

        printf("Nom: %s\nMoyenne des notes = %.2f\n\n", etu[i].nom,sum/5);
    }

```

### 5. Structure imbriquée

Imbriquer une structure signifie avoir une ou plusieurs variables de structure à l'intérieur d'une autre structure. Comme nous déclarons un membre `int` ou `char`, nous pouvons également déclarer une variable de structure comme membre.

```c
struct date
    {
       int jour;
       int mois;
       int annee;
    };

struct etudiant
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
        struct naissance anniversaire;
    };

void main(){
 struct etudiant etu1;

```

La variable de structure `anniversaire` de type `struct naissance` est imbriquée dans `struct etudiant`. Il devrait être clair que vous **ne pouvez pas** imbriquer une variable de structure de type `struct etudiant` dans `struct etudiant`.

Notez que la structure à imbriquer doit être déclarée en premier. En utilisant `.`, nous pouvons accéder aux membres contenus dans la structure interne ainsi qu'aux autres membres.

```c
 /* Exemple */
etu1.anniversaire.jour
etu1.anniversaire.mois
etu1.anniversaire.annee
etu1.nom

```

Les variables de structure de différents types peuvent également être imbriquées.

```c
struct naissance
    {
       int jour;
       int mois;
       int annee;
    };
    
struct relation
    {
        char nomPere[20];
        char nomMere[20];
    };

struct etudiant
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
        struct naissance anniversaire;
        struct relation parents; 
    };

```

## Allocation de mémoire

Lorsqu'une variable de structure d'un certain type est déclarée, les membres de la structure se voient attribuer des emplacements mémoire contigus (adjacents).

```c
struct etudiant
    {
        char nom[20];
        int numero;
        char sexe;
        int notes[5];
    } etu1;

```

Ici, la mémoire sera allouée à `nom[20]`, suivie de `numero`, `sexe` et `notes[5]`. Cela implique que la taille de `etu1` ou `struct etudiant` sera la somme de la taille de ses membres, n'est-ce pas ? Vérifions.

```c
void main()
{
    printf("Somme de la taille des membres = %I64d octets\n", sizeof(etu1.nom) + sizeof(etu1.numero) + sizeof(etu1.sexe) + sizeof(etu1.notes));
    printf("Utilisation de l'opérateur sizeof() = %I64d octets\n",sizeof(etu1));
}

 /* Sortie */
Somme de la taille des membres = 45 octets
Utilisation de l'opérateur sizeof() = 48 octets

```

> Puisque l'opérateur `sizeof()` retourne `long long unsigned int`, utilisez `%I64d` comme spécificateur de format. Vous devrez peut-être utiliser `%llu` ou `%lld` selon votre compilateur.   
>   
> L'utilisation de `%d` donnera un avertissement - le format '%d' attend un argument de type 'int', mais l'argument 2 a le type 'long long unsigned int'.

L'utilisation de l'opérateur `sizeof()` donne `3` octets de plus que la somme de la taille des membres. Pourquoi ? Où sont ces 3 octets dans la mémoire ? 

Répondons d'abord à la deuxième question. Nous pouvons imprimer les adresses des membres pour trouver les adresses de ces `3` octets.

```c
void main()
{
    printf("Adresse du membre nom = %d\n", &etu1.nom);
    printf("Adresse du membre numero = %d\n", &etu1.numero);
    printf("Adresse du membre sexe = %d\n", &etu1.sexe);
    printf("Adresse du membre notes = %d\n", &etu1.notes);
}

 /* Sortie */
Adresse du membre nom = 4225408
Adresse du membre numero = 4225428
Adresse du membre sexe = 4225432
Adresse du membre notes = 4225436

```

![](https://i.gyazo.com/fae6d1a3f7a5d79152e78239fa9257b4.png)

Nous pouvons voir que le tableau `notes[5]` au lieu d'être alloué à partir de `4225433` a été alloué à partir de `4224536`. Mais pourquoi ?

### 1. Alignement des données

Avant de regarder l'alignement des données, il est important de savoir comment le processeur lit les données de la mémoire.

Un processeur lit **un mot** en un cycle. Ce mot est **4 octets** pour un processeur **32 bits** et **8 octets** pour un processeur **64 bits**. Plus le nombre de cycles est faible, meilleure est la performance du CPU.

Une façon d'y parvenir est d'**aligner** les données. Aligner signifie qu'_une variable de tout type de données primitif de taille `t` aura toujours (par défaut) une adresse qui est un multiple de `t`_. C'est essentiellement l'alignement des données. Cela se produit à chaque fois.

**Adresses alignées pour certains types de données**

<table>
    <tr>
        <th> Types de données</th>
        <th> Taille (en octets)</th>
        <th> Adresse </th>
    </tr>
    <tr>
        <td>char</td>
        <td>1</td>
        <td>multiple de 1</td>
    </tr>
    <tr>
        <td>short</td>
        <td>2</td>
        <td>multiple de 2</td>
    </tr>
    <tr>
        <td>int, float</td>
        <td>4</td>
        <td>multiple de 4</td>
    </tr>
    <tr>
        <td>double, long, * (pointeurs)</td>
        <td>8</td>
        <td>multiple de 8</td>
    </tr>
    <tr>
        <td>long double</td>
        <td>16</td>
        <td>multiple de 16</td>
    </tr>
</table>

### 2. Remplissage de structure

Vous devrez peut-être insérer quelques octets supplémentaires entre les membres de la structure pour aligner les données. Ces octets supplémentaires sont appelés **remplissage**.

Dans notre exemple précédent, les `3` octets ont servi de remplissage. Sans eux, notes[0] qui est de type `int` (adresse multiple de 4) aurait son adresse de base à `4225433` (non multiple de 4).

Vous pouvez maintenant probablement voir pourquoi les structures ne peuvent pas être comparées directement.

![](https://i.gyazo.com/2992912eb4c1e6779b34d0a2ef4a9f63.png)

### 3. Alignement des membres de la structure

Pour expliquer cela, nous prendrons un autre exemple (vous comprendrez pourquoi).

```c
struct exemple
    {
        int i1;
        double d1;
        char c1;
        
    } exemple1;

void main()
{
    printf("taille = %I64d octets\n",sizeof(exemple1));
}

```

Quelle serait la sortie ? Appliquons ce que nous savons.

`i1` est de 4 octets. Il sera suivi d'un remplissage de 4 octets car l'adresse de `d1` doit être divisible par 8. 

Cela sera suivi de 8 et 1 octet respectivement pour `d1` et `c1`. Ainsi, la sortie devrait être 4 + 4 + 8 + 1 = 17 octets.

```c
 /* Sortie */
taille = 24 octets

```

Quoi ? Encore faux ! Comment ? À travers un tableau de `struct exemple`, nous pouvons mieux comprendre. Nous imprimerons également l'adresse des membres de `exemple2[0]`.

```c
void main()
{
    struct exemple exemple2[2];
    printf("Adresse de exemple2[0].i1 = %d\n", &exemple2[0].i1);
    printf("Adresse de exemple2[0].d1 = %d\n", &exemple2[0].d1);
    printf("Adresse de exemple2[0].c1 = %d\n", &exemple2[0].c1);

}

 /* Sortie */
Adresse de exemple2[0].i1 = 4225408
Adresse de exemple2[0].d1 = 4225416
Adresse de exemple2[0].c1 = 4225424

```

![](https://i.gyazo.com/4954ec331e15428bac5f3bf8eba31986.png)

Supposons que la taille de `exemple2[0]` est de 17 octets. Cela implique que l'adresse de `exemple2[1].i1` sera `4225425`. Cela **n'est pas** possible puisque l'adresse de `int` doit être un multiple de 4. 

Logiquement, l'adresse possible pour `exemple2[1].i1` semble être `4225428`, un multiple de 4.

Cela est également faux. Savez-vous pourquoi ? L'adresse de `exemple2[1].d1` sera maintenant (28 + 4 (`i1`) + 3 (remplissage)) `4225436` qui n'est pas un multiple de 8.

Afin d'éviter un tel désalignement, le compilateur introduit un alignement pour chaque structure. Cela est fait en ajoutant des octets supplémentaires après le dernier membre, connus sous le nom d'**alignement des membres de la structure**.

Dans l'exemple discuté au début de cette section, cela n'était pas nécessaire (c'est pourquoi nous avions besoin de cet autre exemple).

Une façon simple de s'en souvenir est par cette règle : L'adresse de la structure et la longueur de la structure doivent être des multiples de `t_max`. Ici, `t_max` est la taille maximale prise par un membre dans la structure.

![](https://i.gyazo.com/5e3a7ca0bb894743995e2c7d8fec8bfe.png)

Pour `struct exemple`, 8 octets est la taille maximale de `d1`. Par conséquent, il y a un remplissage de 7 octets à la fin de la structure, ce qui porte sa taille à 24 octets.

**En suivant ces deux règles, vous pouvez facilement trouver la taille de n'importe quelle structure :**

1. Tout type de données stocke sa valeur à une adresse qui est un multiple de sa taille.
2. Toute structure prend la taille qui est un multiple du nombre maximal d'octets pris par un membre.

Bien que nous soyons capables de réduire les cycles du CPU, une quantité significative de mémoire est gaspillée. 

Une façon de réduire la quantité de remplissage à un minimum possible est de déclarer les variables membres dans **l'ordre décroissant de leur taille**.

Si nous suivons cela dans `struct exemple`, la taille de la structure est réduite à 16 octets. Le remplissage est réduit de 7 à 3 octets.

![](https://i.gyazo.com/b4e23f98514884e13ff86272c8b181cd.png)

```c
struct exemple
    {
        double d1; 
        int i1;
        char c1;
        
    } exemple3;

void main()
{
    printf("taille = %I64d octets\n",sizeof(exemple3));
}

 /* Sortie */
taille = 16 octets

```

### 4. Compactage de structure

Le compactage est l'inverse du remplissage. Il empêche le compilateur de remplir et supprime la mémoire non allouée. 

Dans le cas de Windows, nous utilisons la directive `#pragma pack`, qui spécifie l'alignement de compactage pour les membres de la structure.

```c
#pragma pack(1)

struct exemple
    {
        double d1; 
        int i1;
        char c1;
        
    } exemple4;

void main()
{
    printf("taille = %I64d octets\n",sizeof(exemple4));
}

 /* Sortie */
taille = 13 octets

```

![](https://i.gyazo.com/0d76bb850b7fc75f4091cd1dbe02cb87.png)

Cela garantit que les membres sont _alignés_ sur une frontière de 1 octet. En d'autres termes, l'adresse de tout type de données doit être un multiple de 1 octet ou de leur taille (selon la valeur la plus basse).

## Pointeurs

> Si vous souhaitez réviser les pointeurs avant de continuer, voici un [lien](https://www.freecodecamp.org/news/pointers-in-c-are-not-as-difficult-as-you-think/) vers un article couvrant les pointeurs en profondeur.

### 1. Pointeur en tant que membre

Une structure peut avoir des pointeurs comme membres également.

```c
struct etudiant
    {
        char *nom;
        int *numero;
        char sexe;
        int notes[5];
    };

void main()
{   int alexNumero = 44;
   struct etudiant etu1 = { "Alex", &alexNumero, 'M', { 76, 78, 56, 98, 92 }};
}

```

En utilisant `.` (l'opérateur point), nous pouvons à nouveau accéder aux membres. Puisque `numero` a maintenant l'adresse de `alexNumero`, nous devrons déréférencer `etu1.numero` pour obtenir la valeur (et non `etu1.(*numero)`).

```c
   printf("Nom: %s\n", etu1.nom);
   printf("Numéro: %d\n", *(etu1.numero));
   printf("Sexe: %c\n", etu1.sexe);

   for( int i = 0; i < 5; i++)
    printf("Notes dans la %dème matière: %d\n", i, etu1.notes[i]);

 /* Sortie */
Nom: Alex
Numéro: 43
Sexe: M
Notes dans la 0ème matière: 76
Notes dans la 1ère matière: 78
Notes dans la 2ème matière: 56
Notes dans la 3ème matière: 98
Notes dans la 4ème matière: 92

```

### 2. Pointeur vers une structure

Comme les pointeurs d'entiers, les pointeurs de tableaux et les pointeurs de fonctions, nous avons des pointeurs vers des structures ou des **pointeurs de structure** également.

```c
struct etudiant {
    char nom[20];
    int numero;
    char sexe;
    int notes[5];
};

struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}};

struct etudiant *ptrEtu1 = &etu1;

```

Ici, nous avons déclaré un pointeur `ptrEtu1` de type `struct etudiant`. Nous avons assigné l'adresse de `etu1` à `ptrEtu1`.

`ptrEtu1` stocke l'adresse de base de `etu1`, qui est l'adresse de base du premier membre de la structure. L'incrémentation de 1 augmenterait l'adresse de `sizeof(etu1)` octets.

```c
printf("Adresse de la structure = %d\n", ptrEtu1);
printf("Adresse du membre `nom` = %d\n", &etu1.nom);
printf("Incrémenter de 1 donne %d\n", ptrEtu1 + 1);

/* Sortie */
Adresse de la structure = 6421968
Adresse du membre 'nom' = 6421968
Incrémenter de 1 donne 6422016

```

Nous pouvons accéder aux membres de `etu1` en utilisant `ptrEtu1` de deux manières. En utilisant `*` (opérateur d'indirection) ou en utilisant `->` (**opérateur infixe ou flèche**).

Avec `*`, nous continuerons à utiliser le `.` (opérateur point) alors qu'avec `->` nous n'aurons pas besoin de l'opérateur point.

```c
printf("Nom sans utiliser ptrEtu1 : %s\n", etu1.nom);
printf("Nom en utilisant ptrEtu1 et * : %s\n", (*ptrEtu1).nom);
printf("Nom en utilisant ptrEtu1 et -> : %s\n", ptrEtu1->nom);

/* Sortie */
Nom sans utiliser ptrEtu1: Alex
Nom en utilisant ptrEtu1 et *: Alex
Nom en utilisant ptrEtu1 et ->: Alex

```

De même, nous pouvons accéder et modifier d'autres membres également. Notez que les parenthèses sont nécessaires lors de l'utilisation de `*` puisque l'opérateur point (`.`) a une priorité plus élevée que `*`.

### 3. Pointeur et tableau de structures

Nous pouvons créer un tableau de type `struct etudiant` et utiliser un pointeur pour accéder aux éléments et à leurs membres.

```c
struct etudiant etu[10];

 /* Pointeur vers le premier élément (structure) du tableau */
struct etudiant *ptrEtu_type1 = etu;

 /* Pointeur vers un tableau de 10 struct etudiant */
struct etudiant (*ptrEtu_type2)[10] = &etu;

```

Notez que `ptrEtu_type1` est un pointeur vers `etu[0]` alors que `ptrEtu_type2` est un pointeur vers le tableau entier de 10 `struct etudiant`. Ajouter 1 à `ptrEtu_type1` pointerait vers `etu[1]`.

Nous pouvons utiliser `ptrEtu_type1` avec une boucle pour parcourir les éléments et leurs membres.

```c
for( int i = 0; i <  10; i++)
printf("%s, %d\n", ( ptrEtu_type1 + i)->nom, ( ptrEtu_type1 + i)->numero);

```

## Fonctions

### 1. Fonction en tant que membre

Les fonctions **ne peuvent pas** être un membre d'une structure. Cependant, en utilisant des _pointeurs de fonction_, nous pouvons appeler des fonctions en utilisant `.`. Gardez simplement à l'esprit que cela n'est pas recommandé.

```c
 struct exemple
    {
        int i;
        void (*ptrMessage)(int i);


    };

void message(int);

void message(int i)
{
    printf("Bonjour, je suis un membre d'une structure. Cette structure a également un entier avec la valeur %d", i);
}

void main()
{
    struct exemple eg1 = {6, message};
    eg1.ptrMessage(eg1.i);
}

```

Nous avons déclaré deux membres, un `int` `i` et un pointeur de fonction `ptrMessage` à l'intérieur de `struct exemple`. Le pointeur de fonction pointe vers une fonction qui prend un `int` et retourne `void`.

`message` est une telle fonction. Nous avons initialisé `eg1` avec `6` et `message`. Ensuite, nous utilisons `.` pour appeler la fonction en utilisant `ptrMessage` et passer `eg1.i`.

### 2. Structure en tant qu'argument de fonction

Comme les variables, nous pouvons passer des **membres de structure** individuels en tant qu'arguments.

```c
#include <stdio.h>

struct etudiant {
    char nom[20];
    int numero;
    char sexe;
    int notes[5];
};

void afficher(char a[], int b, char c, int notes[])
{
    printf("Nom: %s\n", a);
    printf("Numéro: %d\n", b);
    printf("Sexe: %c\n", c);

    for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,notes[i]);
}
void main()
{
    struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}};
    afficher(etu1.nom, etu1.numero, etu1.sexe, etu1.notes);
}

 /* Sortie */
Nom: Alex
Numéro: 43
Sexe: M
Notes dans la 0ème matière: 76
Notes dans la 1ère matière: 98
Notes dans la 2ème matière: 68
Notes dans la 3ème matière: 87
Notes dans la 4ème matière: 93

```

Notez que la structure `struct etudiant` est déclarée en dehors de `main()`, tout en haut. Cela est pour s'assurer qu'elle est disponible globalement et que `afficher()` peut l'utiliser.

Si la structure est définie à l'intérieur de `main()`, sa portée sera limitée à `main()`.

Passer les membres de la structure n'est pas efficace lorsqu'il y en a un grand nombre. Alors, les **variables de structure** peuvent être passées à une fonction.

```c
void afficher(struct etudiant a)
{
    printf("Nom: %s\n", a.nom);
    printf("Numéro: %d\n", a.numero);
    printf("Sexe: %c\n", a.sexe);

    for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,a.notes[i]);
}
void main()
{
    struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}};
    afficher(etu1);
}

```

Si la taille de la structure est grande, alors passer une copie de celle-ci ne sera pas très efficace. Nous pourrions passer un **pointeur de structure** à une fonction. Dans ce cas, l'adresse de la structure est passée comme _argument réel_.

```c
void afficher(struct etudiant *p)
{
    printf("Nom: %s\n", p->nom);
    printf("Numéro: %d\n", p->numero);
    printf("Sexe: %c\n", p->sexe);

    for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,p->notes[i]);
}
void main()
{
    struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}};
    struct etudiant *ptrEtu1 = &etu1;
    afficher(ptrEtu1);
}

```

Passer un **tableau de structures** à une fonction est similaire à passer un tableau de n'importe quel type à une fonction. Le nom du tableau, qui est l'adresse de base du tableau de la structure, est passé à la fonction.

```c
void afficher(struct etudiant *p)
{   
    for( int j = 0; j < 10; j++)
   {
       printf("Nom: %s\n", (p+j)->nom);
        printf("Numéro: %d\n", (p+j)->numero);
        printf("Sexe: %c\n", (p+j)->sexe);

        for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,(p+j)->notes[i]);
   }
}

void main()
{
    struct etudiant etu1[10];
    afficher(etu1);
}

```

### 3. Structure en tant que retour de fonction

Nous pouvons retourner une **variable de structure**, comme n'importe quelle autre variable.

```c
#include <stdio.h>

struct etudiant {
    char nom[20];
    int numero;
    char sexe;
    int notes[5];
};


struct etudiant augmenterDe5(struct etudiant p)
{
    for( int i =0; i < 5; i++)
        if(p.notes[i] + 5 <= 100)
           {
               p.notes[i]+=5;
           }
    return p;
}

void main()
{
    struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}};
    etu1 = augmenterDe5(etu1);
    
    printf("Nom: %s\n", etu1.nom);
    printf("Numéro: %d\n", etu1.numero);
    printf("Sexe: %c\n", etu1.sexe);

    for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,etu1.notes[i]);
}

 /* Sortie */
Nom: Alex
Numéro: 43
Sexe: M
Notes dans la 0ème matière: 81
Notes dans la 1ère matière: 98
Notes dans la 2ème matière: 73
Notes dans la 3ème matière: 92
Notes dans la 4ème matière: 98

```

La fonction `augmenterDe5()` augmente les notes de 5 pour les matières où, après avoir augmenté les notes, elles sont inférieures ou égales à 100. Notez que le type de retour est une variable de structure de type `struct etudiant`.

Lors du retour d'un **membre de structure**, le type de retour doit être celui du membre.

Un **pointeur de structure** peut également être retourné par une fonction.

```c
#include <stdio.h>
#include <stdlib.h>

struct rectangle {
    int longueur;
    int largeur;
};

struct rectangle* fonction(int longueur, int largeur)
{
    struct rectangle *p  = (struct rectangle *)malloc(sizeof(struct rectangle));
     p->longueur = longueur;
     p->largeur = largeur;
    return p;
}

void main()
{
    struct rectangle *rectangle1 = fonction(5,4);
    printf("Longueur du rectangle = %d unités\n", rectangle1->longueur);
    printf("Largeur du rectangle = %d unités\n", rectangle1->largeur);
    printf("Aire du rectangle = %d unités carrées\n", rectangle1->longueur * rectangle1->largeur);
}

 /* Sortie */
Longueur du rectangle = 5 unités
Largeur du rectangle = 4 unités
Aire du rectangle = 20 unités carrées

```

Remarquez que nous avons alloué la mémoire de taille `struct rectangle` dynamiquement en utilisant `malloc()`. Puisqu'il retourne un pointeur _void_, nous devons le _caster_ en un pointeur `struct rectangle`.

## Structures auto-référentielles

Nous avons discuté que les pointeurs peuvent également être un membre d'une structure. Que se passe-t-il si le pointeur est un pointeur de structure ? Le pointeur de structure peut être du **même type que la structure** ou **différent**.

Les structures **auto-référentielles** sont celles qui ont des pointeurs de structure du même type que leurs membres.

```c
struct etudiant {
    char nom[20];
    int numero;
    char sexe;
    int notes[5];
    struct etudiant *suivant;
};

```

C'est une structure auto-référentielle où `suivant` est un pointeur de structure de type `struct etudiant`. 

Nous allons maintenant créer deux variables de structure `etu1` et `etu2` et les initialiser avec des valeurs. Nous stockerons ensuite l'adresse de `etu2` dans le membre `suivant` de `etu1`.

```c
void main()
{
    struct etudiant etu1 = {"Alex", 43, 'M', {76, 98, 68, 87, 93}, NULL};
    struct etudiant etu2 = { "Max", 33, 'M', {87, 84, 82, 96, 78}, NULL};
    etu1.suivant = &etu2;
}

```

![](https://i.gyazo.com/d0e96dd633d93a28082bddbe932f70a8.png)

Nous pouvons maintenant accéder aux membres de `etu2` en utilisant `etu1` et `suivant`.

```c
void main()
{
    printf("Nom: %s\n", etu1.suivant->nom);
    printf("Numéro: %d\n", etu1.suivant->numero);
    printf("Sexe: %c\n", etu1.suivant->sexe);

    for(int i = 0; i < 5; i++)
        printf("Notes dans la %dème matière: %d\n",i,etu1.suivant->notes[i]);
}

 /* Sortie */
Nom: Max
Numéro: 33
Sexe: M
Notes dans la 0ème matière: 87
Notes dans la 1ère matière: 84
Notes dans la 2ème matière: 82
Notes dans la 3ème matière: 96
Notes dans la 4ème matière: 78

```

Supposons que nous voulons une variable de structure différente après `etu1`, c'est-à-dire _insérer une autre variable de structure entre `etu1` et `etu2`_. Cela peut être fait facilement.

```c
void main()
{
    struct etudiant etuEntre = { "Gasly", 23, 'M', {83, 64, 88, 79, 91}, NULL};
    etu1.suivant = &etuEntre;
    etuEntre.suivant = &etu2;
}

```

Maintenant, `etu1.suivant` stocke l'adresse de `etuEntre`. Et `etuEntre.suivant` a l'adresse de `etu2`. Nous pouvons maintenant accéder aux trois structures en utilisant `etu1`.

```c
    printf("Numéro de %s: %d\n", etu1.suivant->nom, etu1.suivant->numero);
    printf("Sexe de %s: %c\n", etu1.suivant->suivant->nom, etu1.suivant->suivant->sexe);

 /* Sortie */
Numéro de Gasly: 23
Sexe de Max: M

```

![](https://i.gyazo.com/270110c92242e31902924c84c008d489.png)

Remarquez comment nous avons formé un lien entre `etu1`, `etuEntre` et `etu3`. Ce que nous avons discuté ici est le point de départ d'une _Liste Chaînée_.

Les structures auto-référentielles sont très utiles pour créer des structures de données telles que les _listes chaînées_, les _piles_, les _files d'attente_, les _graphes_, etc.

## Conclusion

Terminé ! Nous avons couvert tout, de la définition d'une structure à l'utilisation des structures auto-référentielles. 

Essayez de récapituler tous les sous-sujets que vous avez lus. Si vous pouvez vous les rappeler, bien joué ! Relisez ceux que vous ne pouvez pas vous rappeler.

La prochaine étape logique serait d'en apprendre davantage sur les listes chaînées et les diverses autres structures de données qui ont été utilisées ici.

Continuez à apprendre. Restez chez vous et restez en sécurité.