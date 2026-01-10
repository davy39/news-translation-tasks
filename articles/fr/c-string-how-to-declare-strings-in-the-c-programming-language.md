---
title: Chaînes de caractères en C – Comment déclarer des chaînes de caractères dans
  le langage de programmation C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-06T17:51:39.000Z'
originalURL: https://freecodecamp.org/news/c-string-how-to-declare-strings-in-the-c-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/carlos-alberto-gomez-iniguez-fzZEURcKr4Q-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Chaînes de caractères en C – Comment déclarer des chaînes de caractères
  dans le langage de programmation C
seo_desc: "Computers store and process all kinds of data.\nStrings are just one of\
  \ the many forms in which information is presented and gets processed by computers.\
  \ \nStrings in the C programming language work differently than in other modern\
  \ programming language..."
---

Les ordinateurs stockent et traitent toutes sortes de données.

Les chaînes de caractères ne sont qu'une des nombreuses formes sous lesquelles l'information est présentée et traitée par les ordinateurs.

Les chaînes de caractères dans le langage de programmation C fonctionnent différemment que dans d'autres langages de programmation modernes.

Dans cet article, vous apprendrez comment déclarer des chaînes de caractères en C.

Avant de le faire, vous passerez en revue un aperçu de base de ce que sont les types de données, les variables et les tableaux en C. Ainsi, vous comprendrez comment ceux-ci sont tous connectés les uns aux autres lorsqu'il s'agit de travailler avec des chaînes de caractères en C.

Connaître les bases de ces concepts vous aidera ensuite à mieux comprendre comment déclarer et travailler avec des chaînes de caractères en C.

Commençons !

## Types de données en C

C a quelques types de données intégrés.

Ils sont `int`, `short`, `long`, `float`, `double`, `long double` et `char`.

Comme vous le voyez, il n'y a pas de type de données intégré pour les chaînes de caractères ou str (abréviation de string).

### Le type de données `char` en C

Parmi ces types que vous venez de voir, la seule façon d'utiliser et de présenter des caractères en C est d'utiliser le type de données `char`.

En utilisant `char`, vous êtes capable de représenter un *seul* caractère – parmi les 256 que votre ordinateur reconnaît. Il est le plus couramment utilisé pour représenter les caractères du tableau ASCII.

Les caractères simples sont entourés de *guillemets simples*.

Les exemples ci-dessous sont tous des `char` – même un nombre entouré de guillemets simples et un seul espace est un `char` en C :

```c
'D', '!', '5', 'l', ' ' 
```

Chaque lettre, symbole, nombre et espace entouré de guillemets simples est une seule pièce de données de caractère en C.

Que faire si vous voulez présenter plus d'un seul caractère ?

Ce qui suit n'est **pas** un `char` valide – malgré le fait qu'il soit entouré de guillemets simples. Cela est dû au fait qu'il ne contient pas seulement un seul caractère à l'intérieur des guillemets simples :

`'freeCodeCamp is awesome'`

Lorsque de nombreux caractères simples sont regroupés, comme la phrase que vous voyez ci-dessus, une *chaîne de caractères* est créée. Dans ce cas, lorsque vous utilisez des chaînes de caractères, au lieu de guillemets simples, vous devez utiliser uniquement des *guillemets doubles*.

`"freeCodeCamp is awesome"`

## Comment déclarer des variables en C

Jusqu'à présent, vous avez vu comment le texte est présenté en C.

Que se passe-t-il, cependant, si vous voulez stocker du texte quelque part ? Après tout, les ordinateurs sont très bons pour sauvegarder des informations en mémoire pour une récupération et une utilisation ultérieures.

La façon dont vous stockez des données en C, et dans la plupart des langages de programmation, est dans des variables.

Essentiellement, vous pouvez penser aux variables comme à des boîtes qui contiennent une valeur qui peut changer tout au long de la vie d'un programme. Les variables allouent de l'espace dans la mémoire de l'ordinateur et permettent à C de savoir que vous voulez de l'espace réservé.

C est un langage **statiquement typé**, ce qui signifie que lorsque vous créez une variable, vous devez spécifier quel type de données cette variable sera.

Il existe de nombreux types de variables différents en C, puisque il existe de nombreux types de données différents.

Chaque variable a un type de données associé.

Lorsque vous créez une variable, vous mentionnez d'abord le type de la variable (qu'elle contiendra des valeurs entières, flottantes, char ou tout autre type de données), son nom, et ensuite, optionnellement, vous lui attribuez une valeur :

```c
#include <stdio.h>
int main(void){

char letter = 'D';

//crée une variable nommée letter
//elle ne contient que des valeurs de type char
// le caractère simple 'D' est attribué à letter
}
```

Faites attention à ne pas mélanger les types de données lorsque vous travaillez avec des variables en C, car cela provoquera des erreurs.

Par exemple, si vous essayez de changer l'exemple ci-dessus pour utiliser des guillemets doubles (rappelons que les chars *n'utilisent* que des guillemets simples), vous obtiendrez une erreur lorsque vous compilerez le code :

```c
#include <stdio.h>
int main(void){

char letter = "D";

//sortie :

test.c:4:6: warning: incompatible pointer to integer conversion initializing 'char' with an expression of type
      'char [2]' [-Wint-conversion]
char letter = "D";
     ^        ~~~
1 warning generated.


}
```

Comme mentionné précédemment, C n'a pas de type de données intégré pour les chaînes de caractères. Cela signifie également que C n'a pas de variables de chaîne de caractères !


### Comment créer des tableaux en C

Un tableau est essentiellement une variable qui stocke plusieurs valeurs. C'est une collection de nombreux éléments du même type.

Comme pour les variables régulières, il existe de nombreux types de tableaux différents car les tableaux ne peuvent contenir que des éléments du même type de données. Il existe des tableaux qui ne contiennent que des `int`, que des `float`, et ainsi de suite.

Voici comment vous définissez un tableau de `int`s par exemple :

```c
int numbers[3];
```

D'abord, vous spécifiez le type de données des éléments que le tableau contiendra. Ensuite, vous lui donnez un nom et immédiatement après le nom, vous incluez également une paire de crochets avec un entier. Le nombre entier spécifie la *longueur* du tableau.

Dans l'exemple ci-dessus, le tableau peut contenir `3` valeurs.

Après avoir défini le tableau, vous pouvez attribuer des valeurs individuellement, avec la notation des crochets, en utilisant l'indexation. L'indexation en C (et dans la plupart des langages de programmation) commence à `0`.

```c
//Définir le tableau ; il peut contenir 3 valeurs
int numbers[3];

//attribuer le 1er élément du tableau numbers la valeur de 1
int numbers[0] = 1;

//attribuer le 2ème élément du tableau numbers la valeur de 2
int numbers[1] = 2;

//attribuer le 3ème élément du tableau numbers la valeur de 3
int numbers[2] = 3;
```

Vous référencez et récupérez un élément d'un tableau en utilisant le nom du tableau et l'index de l'élément dans des crochets, comme ceci :

```c
numbers[2]; // retourne la valeur 3
```

## Que sont les tableaux de caractères en C ?

Alors, comment tout ce qui a été mentionné jusqu'à présent s'assemble-t-il, et quel est le rapport avec l'initialisation des chaînes de caractères en C et leur sauvegarde en mémoire ?

Eh bien, les chaînes de caractères en C sont en fait un type de tableau – spécifiquement, elles sont un `tableau de caractères`. Les chaînes de caractères sont une collection de valeurs `char`.

### Comment fonctionnent les chaînes de caractères en C

En C, toutes les chaînes de caractères se terminent par un `0`. Ce `0` permet à C de savoir où une chaîne de caractères se termine.

Ce zéro de terminaison de chaîne est appelé un **terminateur de chaîne**. Vous pouvez également voir le terme **zéro nul** utilisé pour cela, qui a la même signification.

Ne confondez pas ce zéro final avec l'entier numérique `0` ou même le caractère `'0'` - ils ne sont pas la même chose.

Le terminateur de chaîne est ajouté automatiquement à la fin de chaque chaîne de caractères en C. Mais il n'est pas visible pour nous – il est simplement toujours là.

Le terminateur de chaîne est représenté comme ceci : `'\0'`. Ce qui le distingue du caractère `'0'` est la barre oblique inverse qu'il possède.

Lorsque vous travaillez avec des chaînes de caractères en C, il est utile de les imaginer toujours se terminant par un *zéro nul* et ayant cet octet supplémentaire à la fin.

![Screenshot-2021-10-04-at-8.46.08-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-04-at-8.46.08-PM.png)

Chaque caractère occupe un octet en mémoire.

La chaîne de caractères `"hello"`, dans l'image ci-dessus, occupe `6 octets`.

"Hello" a cinq lettres, chacune occupant 1 octet d'espace, et ensuite le zéro nul occupe un octet également.

### La longueur des chaînes de caractères en C

La longueur d'une chaîne de caractères en C est simplement le nombre de caractères dans un mot, **sans** inclure le terminateur de chaîne (malgré le fait qu'il soit toujours utilisé pour terminer les chaînes de caractères).

Le terminateur de chaîne n'est pas pris en compte lorsque vous voulez trouver la longueur d'une chaîne de caractères.

Par exemple, la chaîne de caractères `freeCodeCamp` a une longueur de `12` caractères.

Mais lorsque vous comptez la longueur d'une chaîne de caractères, vous devez toujours compter les espaces vides également.

Par exemple, la chaîne de caractères `I code` a une longueur de `6` caractères. `I` est 1 caractère, `code` a 4 caractères, et ensuite il y a 1 espace vide.

Ainsi, la longueur d'une chaîne de caractères n'est pas le même nombre que le nombre d'octets qu'elle a et la quantité d'espace mémoire qu'elle occupe.

### Comment créer des tableaux de caractères et initialiser des chaînes de caractères en C

La première étape est d'utiliser le type de données `char`. Cela permet à C de savoir que vous voulez créer un tableau qui contiendra des caractères.

Ensuite, vous donnez un nom au tableau, et immédiatement après cela, vous incluez une paire de crochets ouvrants et fermants.

À l'intérieur des crochets, vous inclurez un entier. Cet entier sera *le nombre maximum de caractères que vous voulez que votre chaîne de caractères soit* **y compris** le terminateur de chaîne.

```c
char city[7];
```

Vous pouvez initialiser une chaîne de caractères un caractère à la fois comme ceci :

```c
#include <stdio.h>

int main(void) {
    char city[7];

    city[0] = 'A';
    city[1] = 't';
    city[2] = 'h';
    city[3] = 'e';
    city[4] = 'n';
    city[5] = 's';
    city[6] = '\0'; //n'oubliez pas cela !

    printf("I live in %s",city);

}
```

Mais cela est assez fastidieux. Au lieu de cela, lorsque vous définissez pour la première fois le tableau de caractères, vous avez la possibilité de lui attribuer une valeur directement en utilisant un littéral de chaîne entre guillemets doubles :

```c
#include <stdio.h>
int main(void){

char city[7] = "Athens";

//définir un tableau de caractères nommé city
//il peut contenir une chaîne de caractères jusqu'à 7 caractères Y COMPRIS le terminateur de chaîne
//la valeur "Athens" est attribuée lorsque le tableau de caractères est défini

//c'est ainsi que vous imprimez la valeur du tableau de caractères
printf("I live in %s",city);

}
```

Si vous le souhaitez, au lieu d'inclure le nombre dans les crochets, vous pouvez simplement attribuer une valeur au tableau de caractères. 

Cela fonctionne exactement de la même manière que l'exemple ci-dessus. Il comptera le nombre de caractères dans la valeur que vous fournissez et ajoutera automatiquement le caractère zéro nul à la fin :

```c
char city[] = "Athens";

//"Athens" a une longueur de 6 caractères
//"Athens" occupe 7 octets en mémoire, avec le zéro nul inclus

/*
char city[7]  = "Athens";

est égal à 

char city[] = "Athens";

*/
```

Rappelez-vous, vous devez toujours réserver suffisamment d'espace pour la chaîne de caractères la plus longue que vous voulez inclure *plus* le terminateur de chaîne.

Si vous voulez plus d'espace, avez besoin de plus de mémoire, et prévoyez de changer la valeur plus tard, incluez un nombre plus grand dans les crochets :

```c
char city[15] = "Athens";

/* 
Le tableau de caractères city pourra maintenant contenir 15 caractères 
(y compris le zéro nul)

Dans ce cas, les 8 (15 - 7) places restantes seront vides

Vous pourrez réattribuer une valeur jusqu'à 15 caractères (y compris le zéro nul comme toujours)
*/
```

### Comment changer le contenu d'un tableau de caractères

Donc, vous savez comment initialiser des chaînes de caractères en C. Que faire si vous voulez changer cette chaîne de caractères ?

Vous ne pouvez pas simplement utiliser l'opérateur d'affectation (`=`) et lui attribuer une nouvelle valeur. Vous ne pouvez le faire que lorsque vous définissez pour la première fois le tableau de caractères.

Comme vu précédemment, la façon d'accéder à un élément d'un tableau est de référencer le nom du tableau et le numéro d'index de l'élément.

Donc, pour changer une chaîne de caractères, vous pouvez changer chaque caractère individuellement, un par un :

```c
#include <stdio.h>

int main(void) {
    char city[7] = "Athens";

    printf("I live in %s",city);

    //changer chaque caractère individuellement signifie que vous devez utiliser des guillemets simples
    
    //la nouvelle valeur doit occuper 7 octets de mémoire

   //l'indexation commence à 0, le premier caractère a un index de 0

    city[0] = 'L';
    city[1] = 'o';
    city[2] = 'n';
    city[3] = 'd';
    city[4] = 'o';
    city[5] = 'n';
    city[6] = '\0'; //N'OUBLIEZ PAS CELA !

    printf("\nBut now I live in %s",city);

}
//sortie :
//I live in Athens
//But now I live in London
```

Cette méthode est assez fastidieuse, chronophage et sujette aux erreurs. Ce n'est définitivement pas la méthode préférée.

Vous pouvez plutôt utiliser la fonction `strcpy()`, qui signifie `string copy`.

Pour utiliser cette fonction, vous devez inclure la ligne `#include <string.h>` après la ligne `#include <stdio.h>` en haut de votre fichier.

Le fichier `<string.h>` offre la fonction `strcpy()`.

Lorsque vous utilisez `strcpy()`, vous incluez d'abord le nom du tableau de caractères, puis la nouvelle valeur que vous voulez attribuer. La fonction `strcpy()` ajoute automatiquement le terminateur de chaîne à la nouvelle chaîne de caractères qui est créée :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char city[15] = "Athens";
    strcpy(city,"Barcelona");

    printf("I am going on holiday to %s",city);
    
    //sortie :
    //I am going on holiday to Barcelona
}
```

## Conclusion

Et voilà. Maintenant, vous savez comment déclarer des chaînes de caractères en C.

Pour résumer :

- C ne dispose pas d'une fonction de chaîne de caractères intégrée.
- Pour travailler avec des chaînes de caractères, vous devez utiliser des tableaux de caractères.
- Lorsque vous créez des tableaux de caractères, laissez suffisamment d'espace pour la chaîne de caractères la plus longue que vous voudrez stocker, plus tenez compte du terminateur de chaîne qui est inclus à la fin de chaque chaîne de caractères en C.
- Pour placer ou changer des chaînes de caractères dans des tableaux de caractères, vous pouvez soit :
    - Définir le tableau puis attribuer chaque élément de caractère individuel un par un.
    - OU définir le tableau et initialiser une valeur en même temps.
- Lorsque vous changez la valeur de la chaîne de caractères, vous pouvez utiliser la fonction `strcpy()` après avoir inclus le fichier d'en-tête `<string.h>`.

Si vous voulez en savoir plus sur C, j'ai écrit un [guide](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/) pour les débutants faisant leurs premiers pas dans le langage.

Il est basé sur les premières semaines du [cours d'introduction à l'informatique CS50](https://www.freecodecamp.org/news/introduction-to-computer-science/) et j'explique certains concepts fondamentaux et passe en revue le fonctionnement du langage à un niveau élevé.

Vous pouvez également regarder le [Tutoriel de programmation C pour débutants](https://www.youtube.com/watch?v=KJgsSFOSQv0&t=14s) sur la chaîne YouTube de freeCodeCamp.

Merci d'avoir lu et bon apprentissage :)