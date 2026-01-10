---
title: Instructions Break et Continue en C – Explication des instructions de contrôle
  de boucle en C
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-11-04T18:56:12.000Z'
originalURL: https://freecodecamp.org/news/c-break-and-continue-statements-loop-control-statements-in-c-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/markus-spiske-C0koz3G1I4I-unsplash--1-.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Instructions Break et Continue en C – Explication des instructions de contrôle
  de boucle en C
seo_desc: 'In the C programming language, there are times when you''ll want to change
  looping behavior. And the continue and the break statements help you skip iterations,
  and exit from loops under certain conditions.

  In this tutorial, you''ll learn how break and...'
---

En langage de programmation C, il arrive que vous souhaitiez modifier le comportement des boucles. Les instructions `continue` et `break` vous aident à sauter des itérations et à sortir des boucles sous certaines conditions.

Dans ce tutoriel, vous apprendrez comment les instructions `break` et `continue` modifient le flux de contrôle de votre programme.

Commençons.

## Comment utiliser `break` pour sortir des boucles en C

En C, si vous souhaitez _sortir_ d'une boucle lorsqu'une condition spécifique est remplie, vous pouvez utiliser l'instruction `break`.

Comme pour toutes les instructions en C, l'instruction `break` doit se terminer par un point-virgule (`;`).

Prenons un exemple pour comprendre ce que cela signifie.

Considérons le fragment de code suivant.

```c
#include<stdio.h>
int main()
{
    int count = 0;
    while(count < 100)
    {
        printf("The value of count is %d \n", count);
        count++;
    }
    return 0;
}
```

Dans cet exemple, la boucle `while` répète les instructions dans le corps de la boucle tant que `count` est inférieur à 100.

Le compte commence à 0 et augmente de 1 à chaque itération.

Ceci est le flux de contrôle normal.

Modifions cela un peu.

* Lisez un entier `fav_num` depuis l'utilisateur. Supposons que `fav_num` est le nombre préféré de l'utilisateur dans l'ensemble `{0, 1, 2, ..., 99}`.
* À chaque passage dans la boucle, vous devez vérifier si la valeur actuelle de `count` est égale à `fav_num`.
* Vous souhaitez sortir de la boucle lorsque `count` est égal à `fav_num`.

Alors, comment faire ?

Lisez le fragment de code suivant :

```c
#include<stdio.h>
int main()
{
    // Lire le nombre préféré de l'utilisateur
    int fav_num;
    printf("Entrez votre nombre préféré de 0 à 99 : ");
    scanf("%d", &fav_num);
    
    int count = 0;
    while(count < 100)
    {
        printf("\nLa valeur de count est %d.", count);
        if (count == fav_num)
    		break;
        count++;
    }
    return 0;
}
```

* À chaque passage dans la boucle, vous utilisez `if (count == fav_num)` pour vérifier si `count` est égal à `fav_num`. Et vous ajoutez l'instruction `break;` au corps de l'instruction `if`.
* Tant que `count ≠ fav_num`, le contrôle n'atteint jamais l'instruction `break;`.
* Lorsque `count` est égal à `fav_num`, l'instruction `break;` est déclenchée, et vous sortez de la boucle.
* Le contrôle atteint maintenant la première instruction en dehors de la boucle.

Un exemple de sortie est montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-1.png)

Remarquez comment le contrôle sort de la boucle une fois que le compte atteint `3`, qui est ici `fav_num`.

Dans la section suivante, vous verrez un autre exemple qui renforcera votre compréhension.

### Exemple d'instruction `break` en C

▶ Considérons l'exemple suivant :

* `A[10]` est un tableau de 10 entiers, et est initialisé avec des zéros.
* Vous souhaitez lire les éléments du tableau `A` depuis l'utilisateur. Et calculer la somme des éléments du tableau.
* Cependant, vous exigez que chaque élément de `A` ne soit pas supérieur à `20`.
* Une fois que l'utilisateur entre un nombre supérieur à 20, vous choisissez de terminer la boucle. C'est là que l'instruction `break;` est utile.

Maintenant, lisez le fragment de code suivant qui fait exactement cela.

```c
#include <stdio.h>

int main()
{
    int A[10] = {0};
    int sum = 0;
    
    for(int i = 0; i < 10; i++)
    {
        printf("Entrez un nombre : ");
        scanf("%d",&A[i]);
        if (A[i] > 20)
            break;
        
        sum += A[i];
    }
    printf("Somme : %d",sum);
    return 0;
}

```

* Ici, `sum` est initialisé à `0`.
* À chaque passage dans la boucle, l'utilisateur est invité à entrer un nombre. Et le nombre entré est ajouté à la valeur actuelle de `sum`.
* Si l'utilisateur entre un nombre supérieur à 20, le contrôle sort de la boucle.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-191.png)

Remarquez comment la boucle se termine une fois que l'utilisateur entre un nombre supérieur à `20` – dans ce cas `21`. Et la somme des deux autres nombres (2 et 3) est affichée.

Si vous avez utilisé l'instruction `switch` en C, vous avez probablement utilisé l'instruction `break;` pour sortir de l'échelle de cas dès qu'une étiquette de cas correspondante est trouvée.

Cependant, ce tutoriel vise à enseigner comment utiliser les instructions `break;` et `continue;` pour modifier le comportement des boucles.

## Comment utiliser `continue` pour sauter des itérations en C

En C, si vous souhaitez sauter des itérations dans lesquelles une condition spécifique est remplie, vous pouvez utiliser l'instruction `continue`.

> Contrairement à l'instruction `break`, l'instruction `continue` ne sort pas de la boucle. Elle saute uniquement les itérations dans lesquelles la condition est vraie.

Une fois que l'instruction `continue;` est déclenchée, les instructions restantes de la boucle sont sautées. Et le contrôle de la boucle passe à l'itération suivante.

### Exemple d'instruction `continue` en C

Utilisons l'exemple de la section précédente et modifions-le un peu.

Supposons que vous ne souhaitez pas sortir de la boucle lorsque l'utilisateur entre un nombre supérieur à 20. Vous préférez ignorer ces entrées particulières et calculer la somme des nombres restants dans le tableau `A`.

* Supposons que l'utilisateur entre 10 nombres, dont 3 sont supérieurs à 20.
* Votre code doit maintenant calculer et afficher la somme des 7 nombres restants.

Alors, comment faire ?

> Vous pouvez utiliser l'instruction `continue;` pour sauter uniquement les itérations pour lesquelles l'entrée de l'utilisateur était supérieure à 20. 👨‍💻

Et vous pouvez le faire comme montré dans le code ci-dessous :

```c
#include <stdio.h>

int main()
{
    int A[10] = {0};
    int sum = 0;
    
    for(int i = 0; i < 10; i++)
    {
        printf("Entrez un nombre : ");
        scanf("%d",&A[i]);
        if (A[i] > 20)
            continue;
        
        sum += A[i];
    }
    printf("Somme : %d",sum);
    return 0;
}
```

Dans l'exemple de sortie, vous pouvez voir que la toute première entrée est `21` qui est supérieure à `20`.

Cependant, la boucle s'exécute bien 10 fois. Et si vous êtes prêt pour un rapide exercice d'addition, vous pouvez voir que les nombres autres que 21 (2, 3, 5, 4, 7, 15, 14, 2, et 5) s'additionnent bien à 57. ✅

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-192.png)

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser les instructions `break;` et `continue;` pour contrôler les boucles en C.

Pour résumer, vous avez appris :

* comment l'instruction `break;` aide à sortir des boucles sous des conditions spécifiques.
* comment l'instruction `continue;` aide à sauter des itérations sous des conditions spécifiques.

J'espère que vous avez trouvé ce tutoriel utile. Bon codage ! 😄