---
title: Portée des variables en C – Portée locale et globale expliquée
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-08T16:40:21.000Z'
originalURL: https://freecodecamp.org/news/scope-of-variables-in-c-local-and-global-scope-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Scope-of-variables-in-c.png
tags:
- name: c programming
  slug: c-programming
- name: variables
  slug: variables
seo_title: Portée des variables en C – Portée locale et globale expliquée
seo_desc: 'In programming, you''ll often have to deal with the scope of a variable.
  The scope of a variable determines whether or not you can access and modify it inside
  a specific block of code.

  In this tutorial, you''ll learn about variable scope in the C progr...'
---

En programmation, vous devrez souvent gérer la portée d'une variable. La portée d'une variable détermine si vous pouvez y accéder et la modifier à l'intérieur d'un bloc de code spécifique.

Dans ce tutoriel, vous apprendrez la portée des variables dans le langage de programmation C. Vous verrez des exemples de code pour vous aider à comprendre les différences entre les variables locales et globales.

## Qu'est-ce que la portée d'une variable ?

Avant d'aller plus loin pour apprendre la portée des variables locales et globales, comprenons ce que signifie _portée_.

> En termes simples, la portée d'une variable est sa _durée de vie_ dans le programme.

Cela signifie que la portée d'une variable est le bloc de code dans l'ensemble du programme où la variable est déclarée, utilisée et peut être modifiée.

Dans la section suivante, vous apprendrez la portée locale des variables.

## Portée locale des variables en C – Blocs imbriqués

Dans cette section, vous apprendrez comment fonctionnent les variables locales en C. Vous coderez d'abord quelques exemples, puis vous généraliserez le principe de portée.

▶ Voici le premier exemple :

```c
#include <stdio.h>

int main()
{
    int my_num = 7;
    {
        // ajouter 10 à my_num
        my_num = my_num + 10;
        // ou my_num += 10 - plus succinctement
        printf("my_num est %d", my_num);
    }
    
    return 0;
}
```

Comprenons ce que fait le programme ci-dessus.

En C, vous délimitez un bloc de code par `{}` . Les accolades ouvrante et fermante indiquent respectivement le début et la fin d'un bloc.

* La fonction `main()` a une variable entière `my_num` qui est initialisée à 7 dans le bloc _externe_.
* Il y a un bloc _interne_ qui essaie d'ajouter 10 à la variable `my_num`.

Maintenant, compilez et exécutez le programme ci-dessus. Voici la sortie :

```
//Sortie

my_num est 17
```

Vous pouvez voir ce qui suit :

* Le bloc interne est capable d'accéder à la valeur de `my_num` qui est déclarée dans le bloc externe, et de la modifier en ajoutant 7.
* La valeur de `my_num` est maintenant 17, comme indiqué dans la sortie.

## Portée locale des variables en C – Exemple 2 de blocs imbriqués

▶ Voici un autre exemple connexe :

```c
#include <stdio.h>

int main()
{
    int my_num = 7;
    {
        int new_num = 10;
    }
    printf("new_num est %d", new_num); // ceci est la ligne 9
    return 0;
}
```

* Dans ce programme, la fonction `main()` a une variable entière `my_num` dans le bloc _externe_.
* Une autre variable `new_num` est initialisée dans le bloc _interne_. Le bloc interne est imbriqué à l'intérieur du bloc externe.
* Nous essayons d'accéder et d'imprimer la valeur de `new_num` du bloc interne dans le bloc _externe_.

Si vous essayez de compiler le code ci-dessus, vous remarquerez qu'il ne compile pas avec succès. Et vous obtiendrez le message d'erreur suivant :

```
Ligne   Message
9      erreur : 'new_num' non déclaré (première utilisation dans cette fonction)
```

> Cela est dû au fait que la variable `new_num` est déclarée dans le bloc _interne_ et sa _portée_ est limitée au bloc interne. En d'autres termes, elle est _locale_ au bloc interne et _ne peut pas_ être accessible depuis le bloc _externe_.

Sur la base des observations ci-dessus, écrivons le principe générique suivant pour la portée locale des variables :

```
{
	/* BLOC EXTERNE */
    
      {
    	
        
        // contenu du bloc externe juste avant le début de ce bloc
        // PEUT être accessible ici
        
        /* BLOC INTERNE */
        
        
      }
     
       // le contenu du bloc interne n'est PAS accessible ici
 }
```

## Portée locale des variables en C – Blocs différents

Dans l'exemple précédent, vous avez appris comment les variables à l'intérieur du bloc interne imbriqué ne peuvent pas être accessibles depuis l'extérieur du bloc.

Dans cette section, vous comprendrez la portée locale des variables déclarées dans différents blocs.

```c
#include <stdio.h>

int main()
{
    int my_num = 7;
    printf("%d", my_num);
    my_func();
    return 0;
}

void my_func()
{
    printf("%d", my_num);
}
```

Dans l'exemple ci-dessus,

* La variable entière `my_num` est déclarée à l'intérieur de la fonction `main()`.
* À l'intérieur de la fonction `main()`, la valeur de `my_num` est imprimée.
* Il y a une autre fonction `my_func()` qui essaie d'accéder et d'imprimer la valeur de `my_num`.
* Comme l'exécution du programme commence avec la fonction `main()`, il y a un appel à `my_func()` à l'intérieur de la fonction `main()`.

▶ Compilez et exécutez maintenant le programme ci-dessus. Vous obtiendrez le message d'erreur suivant :

```
Ligne   Message
13     erreur : 'my_num' non déclaré (première utilisation dans cette fonction)
```

Si vous remarquez, à la `ligne 13`, la fonction `my_func()` a essayé d'accéder à la variable `my_num` qui a été déclarée et initialisée à l'intérieur de la fonction `main()`.

> Par conséquent, la portée de la variable `my_num` est confinée à la fonction `main()`, et est dite _locale_ à la fonction `main()`.

Nous pouvons représenter cette notion de portée locale de manière générique comme suit :

```
{

	/* BLOC 1 */
    // le contenu du BLOC 2 ne peut pas être accessible ici
    
}


{

	/* BLOC 2 */
    // le contenu du BLOC 1 ne peut pas être accessible ici
    
}

```

## Portée globale des variables en C

Jusqu'à présent, vous avez appris la portée locale des variables en C. Dans cette section, vous apprendrez comment vous pouvez déclarer des variables globales en C.

▶ Commençons par un exemple.

```c
#include <stdio.h>
int my_num = 7;

int main()
{
    printf("my_num peut être accessible depuis main() et sa valeur est %d\n", my_num);
    // appeler my_func
    my_func();
    return 0;
}

void my_func()
{
  printf("my_num peut être accessible depuis my_func() également et sa valeur est %d\n", my_num);
}
```

Dans l'exemple ci-dessus,

* La variable `my_num` est déclarée à l'extérieur des fonctions `main()` et `my_func()`.
* Nous essayons d'accéder à `my_num` à l'intérieur de la fonction `main()`, et d'imprimer sa valeur.
* Nous appelons la fonction `my_func()` à l'intérieur de la fonction `main()`.
* La fonction `my_func()` essaie également d'accéder à la valeur de `my_num`, et de l'imprimer.

Ce programme compile sans aucune erreur, et la sortie est montrée ci-dessous :

```
//Sortie
my_num peut être accessible depuis main() et sa valeur est 7
my_num peut être accessible depuis my_func() également et sa valeur est 7
```

Dans cet exemple, il y a deux fonctions – `main()` et `my_func()`.

Cependant, la variable `my_num` n'est _pas locale_ à aucune fonction dans le programme. Une telle variable qui n'est _pas locale_ à aucune fonction est dite avoir une portée _globale_ et est appelée une variable _globale_.

Ce principe de portée globale des variables peut être résumé comme montré ci-dessous :

```
// toutes les variables globales sont déclarées ici
function1()
	{
    
    // toutes les variables globales peuvent être accessibles à l'intérieur de function1
    
    }
function2()
	{
    
    // toutes les variables globales peuvent être accessibles à l'intérieur de function2
     
    }
    
```

## Conclusion

Dans ce tutoriel, vous avez appris les différences entre la portée locale et globale. Ceci est un tutoriel d'introduction sur la portée des variables en C.

En C, il existe certains modificateurs d'accès pour contrôler le niveau d'accès que les variables ont. Vous pouvez changer l'accès en utilisant les mots-clés correspondants lorsque vous déclarez des variables.

À bientôt dans le prochain tutoriel. En attendant, bon codage !