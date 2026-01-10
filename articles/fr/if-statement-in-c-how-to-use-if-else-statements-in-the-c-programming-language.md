---
title: Instruction If en C – Comment utiliser les instructions If-Else dans le langage
  de programmation C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-06-13T13:47:00.000Z'
originalURL: https://freecodecamp.org/news/if-statement-in-c-how-to-use-if-else-statements-in-the-c-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/christin-hume-mfB1B1s4sMc-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Instruction If en C – Comment utiliser les instructions If-Else dans le
  langage de programmation C
seo_desc: 'In the C programming language, you have the ability to control the flow
  of a program.

  In particular, the program is able to make decisions on what it should do next.
  And those decisions are based on the state of certain pre-defined conditions you
  set...'
---

Dans le langage de programmation C, vous avez la possibilité de contrôler le flux d'un programme.

En particulier, le programme est capable de prendre des décisions sur ce qu'il doit faire ensuite. Et ces décisions sont basées sur l'état de certaines conditions prédéfinies que vous avez définies.

Le programme décidera des prochaines étapes en fonction du fait que les conditions soient remplies ou non.

L'acte de faire une chose si une condition particulière est remplie et une chose différente si cette condition particulière n'est pas remplie est appelé *contrôle de flux*.

Par exemple, vous pouvez vouloir effectuer une action uniquement sous une condition spécifique. Et vous pouvez vouloir effectuer une autre action sous une condition entièrement différente. Ou, vous pouvez vouloir effectuer une autre action complètement différente lorsque cette condition spécifique que vous avez définie n'est *pas* remplie.

Pour pouvoir faire tout ce qui précède et contrôler le flux d'un programme, vous devrez utiliser une instruction `if`.

Dans cet article, vous apprendrez tout sur l'instruction `if` – sa syntaxe et des exemples de son utilisation afin que vous puissiez comprendre comment elle fonctionne.

Vous apprendrez également l'instruction `if else` – c'est-à-dire l'instruction `else` qui est ajoutée à l'instruction `if` pour une flexibilité supplémentaire du programme.

De plus, vous apprendrez l'instruction `else if` pour lorsque vous souhaitez ajouter plus de choix à vos conditions.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une instruction `if` en C ?](#introduction)
    1. [Comment créer une instruction `if` en C](#syntaxe)
    2. [Quel est un exemple d'instruction `if` ?](#exemple)
2. [Qu'est-ce qu'une instruction `if else` en C ?](#else)
    1. [Quel est un exemple d'instruction `if else` ?](#exemple-else)
3. [Qu'est-ce qu'une instruction `else if` ?](#else-if)
    1. [Quel est un exemple d'instruction `else if` ?](#exemple-else-if)

## Qu'est-ce qu'une instruction `if` en C ? <a name="introduction"></a>

Une instruction `if` est également connue sous le nom d'instruction conditionnelle et est utilisée pour la prise de décision. Elle agit comme une fourche dans la route ou une branche.

Une instruction conditionnelle effectue une action spécifique basée sur le résultat d'une vérification ou d'une comparaison qui a lieu.

Ainsi, en résumé, l'instruction `if` prend une décision basée sur une condition.

La condition est une expression booléenne. Une expression booléenne ne peut être que l'une des deux valeurs – vraie ou fausse.

Si la condition donnée est évaluée à `true`, alors le code à l'intérieur du bloc `if` est exécuté.

Si la condition donnée est évaluée à `false`, le code à l'intérieur du bloc `if` est ignoré et sauté.

### Comment créer une instruction `if` en C – Une analyse syntaxique pour les débutants <a name="syntaxe"></a>

La syntaxe générale pour une instruction `if` en C est la suivante :

```c
if (condition) {
  // exécuter ce code si la condition est vraie
}
```

Décomposons cela :

- Vous commencez une instruction `if` en utilisant le mot-clé `if`.
- Entre parenthèses, vous incluez une condition qui doit être vérifiée et évaluée, ce qui est toujours une expression booléenne. Cette condition ne sera évaluée que comme `true` ou `false`.
- Le bloc `if` est dénoté par un ensemble d'accolades, `{}`.
- À l'intérieur du bloc `if`, il y a des lignes de code – assurez-vous que le code est indenté pour qu'il soit plus facile à lire.

### Quel est un exemple d'instruction `if` ? <a name="exemple"></a>

Ensuite, voyons un exemple pratique d'une instruction `if`.

Je vais créer une variable nommée `age` qui contiendra une valeur entière.

Je vais ensuite demander à l'utilisateur d'entrer son âge et stocker la réponse dans la variable `age`.

Ensuite, je vais créer une condition qui vérifie si la valeur contenue dans la variable `age` est *inférieure à* 18.

Si c'est le cas, je veux qu'un message soit imprimé sur la console pour informer l'utilisateur que pour continuer, l'utilisateur doit avoir au moins 18 ans.

```c
#include <stdio.h>

int main(void) {
    // variable age
   int age;

   // demander à l'utilisateur d'entrer son âge
   printf("Veuillez entrer votre âge : ");

   // stocker la réponse de l'utilisateur dans la variable
   scanf("%i", &age);

    // vérifier si l'âge est inférieur à 18
    // si c'est le cas, alors et seulement alors, imprimer un message sur la console
    
   if (age < 18) {
       printf("Vous devez avoir plus de 18 ans pour continuer\n");
   }
}
```

Je compile le code en utilisant `gcc conditionals.c`, où `gcc` est le nom du compilateur C et `conditionals.c` est le nom du fichier contenant le code source C.

Ensuite, pour exécuter le code, je tape `./a.out`.

Lorsque l'on me demande mon âge, j'entre `16` et j'obtiens la sortie suivante :

```
#sortie

Veuillez entrer votre âge : 16
Vous devez avoir plus de 18 ans pour continuer
```

La condition (`age < 18`) est évaluée à `true`, donc le code dans le bloc `if` est exécuté.

Ensuite, je recompile et réexécute le programme.

Cette fois, lorsque l'on me demande mon âge, j'entre `28` et j'obtiens la sortie suivante :

```
#sortie

Veuillez entrer votre âge : 28
```

Eh bien... Il n'y a pas de sortie.

C'est parce que la condition est évaluée à `false` et donc le corps du bloc `if` est ignoré.

Je n'ai également pas spécifié ce qui devrait se passer dans le cas où l'âge de l'utilisateur est *supérieur à* 18.

Je pourrais écrire une autre instruction `if` qui imprimera un message sur la console si l'âge de l'utilisateur est supérieur à 18 pour que le code soit un peu plus clair :

```c
#include <stdio.h>

int main(void) {
    // variable age
   int age;

   // demander à l'utilisateur d'entrer son âge
   printf("Veuillez entrer votre âge : ");

   // stocker la réponse de l'utilisateur dans la variable
   scanf("%i", &age);

    // vérifier si l'âge est inférieur à 18
    // si c'est le cas, imprimer un message sur la console
    
   if (age < 18) {
       printf("Vous devez avoir plus de 18 ans pour continuer\n");
   }
   
   // vérifier si l'âge est supérieur à 18
   // si c'est le cas, imprimer un message sur la console
   
  if (age > 18) {
      printf("Vous avez plus de 18 ans donc vous pouvez continuer \n");
  }
  
   }
```

Je compile et exécute le code, et lorsque l'on me demande mon âge, j'entre à nouveau 28 :

```
#sortie

Veuillez entrer votre âge : 28
Vous avez plus de 18 ans donc vous pouvez continuer 
```

Ce code fonctionne. Cela dit, il existe une meilleure façon de l'écrire et vous verrez comment faire cela dans la section suivante.

## Qu'est-ce qu'une instruction `if else` en C ? <a name="else"></a>

Plusieurs instructions `if` seules ne sont pas utiles – surtout lorsque les programmes deviennent de plus en plus grands.

Ainsi, pour cette raison, une instruction `if` est accompagnée d'une instruction `else`.

L'instruction `if else` signifie essentiellement que "`si` cette condition est vraie, faites ce qui suit, `sinon` faites cela à la place".

Si la condition à l'intérieur des parenthèses est évaluée à `true`, le code à l'intérieur du bloc `if` sera exécuté. Cependant, si cette condition est évaluée à `false`, le code à l'intérieur du bloc `else` sera exécuté.

Le mot-clé `else` est la solution lorsque la condition `if` est fausse et que le code à l'intérieur du bloc `if` ne s'exécute pas. Il fournit une alternative.

La syntaxe générale ressemble à quelque chose comme ce qui suit :

```c
if (condition) {
  // exécuter ce code si la condition est vraie
} else {
  // si la condition ci-dessus est fausse, exécuter ce code
}
```


### Quel est un exemple d'instruction `if else` ? <a name="exemple-else"></a>

Maintenant, revisitons l'exemple avec les deux instructions `if` séparées de tout à l'heure :

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Veuillez entrer votre âge : ");


   scanf("%i", &age);

   if (age < 18) {
       printf("Vous devez avoir plus de 18 ans pour continuer\n");
   }
  if (age > 18) {
      printf("Vous avez plus de 18 ans donc vous pouvez continuer \n");
  }
  
   }
```

Réécrivons-le en utilisant une instruction `if else` à la place :

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Veuillez entrer votre âge : ");

   scanf("%i", &age);

 
    // si la condition dans les parenthèses est vraie, le code à l'intérieur des accolades sera exécuté
    // sinon il est ignoré
    // et le code dans le bloc else sera exécuté
    
   if (age < 18) {
       printf("Vous devez avoir plus de 18 ans pour continuer\n");
   } else {
      printf("Vous avez plus de 18 ans donc vous pouvez continuer \n");
  }
  
   }
```

Si la condition est `true`, le code dans le bloc `if` s'exécute :

```
#sortie

Veuillez entrer votre âge : 14
Vous devez avoir plus de 18 ans pour continuer
```

Si la condition est `false`, le code dans le bloc `if` est ignoré et le code dans le bloc `else` s'exécute à la place :

```
#sortie

Veuillez entrer votre âge : 45
Vous avez plus de 18 ans donc vous pouvez continuer 
```

## Qu'est-ce qu'une instruction `else if` ? <a name="else-if"></a>

Mais que se passe-t-il lorsque vous souhaitez avoir plus d'une condition à choisir ?

Si vous souhaitez choisir entre plus d'une option et souhaitez avoir une plus grande variété d'actions, vous pouvez introduire une instruction `else if`.

Une instruction `else if` signifie essentiellement que "Si cette condition est vraie, faites ce qui suit. Si ce n'est pas le cas, faites cela à la place. Cependant, si aucune des conditions ci-dessus n'est vraie et que tout le reste échoue, faites enfin cela."

La syntaxe générale ressemble à quelque chose comme ce qui suit :

```c
if (condition) {
   // si la condition est vraie, exécuter ce code
} else if(another_condition) {
   // si la condition ci-dessus était fausse et que cette condition est vraie,
   // exécuter le code dans ce bloc
} else {
   // si les deux conditions ci-dessus sont fausses, exécuter ce code
}
```


### Quel est un exemple d'instruction `else if` ? <a name="exemple-else-if"></a>

Voyons comment fonctionne une instruction `else if`.

Supposons que vous avez l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Veuillez entrer votre âge : ");

   scanf("%i", &age);

   if (age < 18) {
       printf("Vous devez avoir plus de 18 ans pour continuer\n");
   }  else if (age < 21) {
       printf("Vous devez avoir plus de 21 ans\n");
   } else {
      printf("Vous avez plus de 18 ans et plus de 21 ans donc vous pouvez continuer \n");
  }
  
   }
```

Si la première instruction `if` est vraie, le reste du bloc ne s'exécutera pas :

```
#sortie

Veuillez entrer votre âge : 17
Vous devez avoir plus de 18 ans pour continuer
```

Si la première instruction `if` est fausse, alors le programme passe à la condition suivante.

Si celle-ci est vraie, le code à l'intérieur du bloc `else if` s'exécute et le reste du bloc ne s'exécute pas :

```
#sortie

Veuillez entrer votre âge : 20
Vous devez avoir plus de 21 ans
```

Si les deux conditions précédentes sont toutes fausses, alors le dernier recours est le bloc `else` qui est celui à exécuter :

```
#sortie

Veuillez entrer votre âge : 22
Vous avez plus de 18 ans et plus de 21 ans donc vous pouvez continuer 
```

## Conclusion

Et voilà – vous connaissez maintenant les bases des instructions `if`, `if else` et `else if` en C !

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation C, consultez les ressources gratuites suivantes :

- [Tutoriel de programmation C pour débutants](https://www.youtube.com/watch?v=KJgsSFOSQv0)
- [Qu'est-ce que le langage de programmation C ? Un tutoriel pour débutants](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/)
- [Le guide du débutant en C : Apprenez les bases du langage de programmation C en quelques heures](https://www.freecodecamp.org/news/the-c-beginners-handbook/)

Merci beaucoup d'avoir lu et bon codage :)