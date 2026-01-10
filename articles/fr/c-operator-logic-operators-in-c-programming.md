---
title: Opérateurs C – Opérateurs logiques en programmation C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-08T15:25:21.000Z'
originalURL: https://freecodecamp.org/news/c-operator-logic-operators-in-c-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-mikael-blomkvist-6476587.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Opérateurs C – Opérateurs logiques en programmation C
seo_desc: "In this article, you will learn about the three logical operators in C.\n\
  I will first explain what operators are in programming and list the different types\
  \ of operators available in C. \nThen, you will learn the role logical operators\
  \ have and how to ..."
---

Dans cet article, vous apprendrez les trois opérateurs logiques en C.

Je vais d'abord expliquer ce que sont les opérateurs en programmation et lister les différents types d'opérateurs disponibles en C.

Ensuite, vous apprendrez le rôle des opérateurs logiques et comment les utiliser à l'aide d'exemples de code.

Commençons !


## Qu'est-ce qu'un opérateur en programmation informatique ?
En programmation informatique, un opérateur est un caractère, un symbole, un mot-clé ou une combinaison de ceux-ci. Il détermine quelle action est effectuée sur un ou plusieurs opérandes.

Un opérande est un élément de données individuel qui est manipulé par l'opérateur.

Chaque langage de programmation de haut niveau définit ces caractères intégrés et les utilise pour indiquer au compilateur d'effectuer des opérations arithmétiques, relationnelles ou logiques qui manipulent des éléments de données et retournent ensuite un résultat final.


### Quels sont les différents types d'opérateurs en programmation C ?
En programmation C, les opérateurs se divisent en trois catégories :

- Opérateurs **unaires**
- Opérateurs **binaires**
- Opérateurs **ternaires**

Les opérateurs **unaires** opèrent sur un seul opérande. Certains des opérateurs unaires en C sont :
- Opérateurs arithmétiques tels que l'opérateur d'incrémentation (`++`), qui incrémente la valeur de l'opérande de `1`. Et l'opérateur de décrémentation (`--`), qui décrémente la valeur de l'opérande de `1`.
- Opérateurs logiques comme l'opérateur NOT (`!`). Cet opérateur inverse la valeur logique de l'opérande – il change `true` en `false` et `false` en `true`.
- Opérateurs bit à bit comme l'opérateur NOT (`~`), qui change chaque bit `0` en `1` et chaque bit `1` en `0`.

Les opérateurs **binaires** opèrent sur deux opérandes. Certains des opérateurs binaires en C sont :
- Opérateurs arithmétiques (`+, -, *, /, %`). Ces opérateurs effectuent des calculs mathématiques sur des données numériques tels que l'addition, la soustraction, la multiplication, la division et le calcul du reste.
- Opérateurs d'égalité/relationnels (`==, !=, >, <, >=, <=`). Ces opérateurs comparent deux valeurs et déterminent si un opérande est supérieur à, inférieur à, égal à ou différent de l'autre opérande.
- Opérateurs logiques/conditionnels tels que les opérateurs AND (`&&`) et OR (`||`).
- Opérateurs bit à bit (`(&, |, ^, <<, >>)`, qui traitent les éléments de données comme une séquence de bits (c'est-à-dire des `0` et des `1`).
- Opérateurs d'affectation (`=, +=, -=, *=, /=, %=`), qui attribuent une valeur spécifique à une variable.

L'opérateur **ternaire** (`?:`) opère sur trois opérandes. La syntaxe générale ressemble à ceci :
```c
(condition) ? expression1 : expression2;
```

L'opérateur ternaire est un opérateur conditionnel que vous pouvez utiliser comme raccourci pour une instruction `if..else`. Il effectue des comparaisons et retourne un résultat.


## Quel est le rôle des opérateurs logiques en programmation C ?
Vous verrez les opérateurs logiques couramment utilisés dans les instructions conditionnelles (telles que les instructions `if..else`) car ils aident à la prise de décision – ils déterminent quelle action doit avoir lieu et quel code doit s'exécuter ensuite en fonction des conditions que vous définissez.

Vous combinez les opérateurs logiques avec une ou plusieurs conditions pour créer une expression logique.

Les opérateurs logiques évaluent l'expression logique et retournent un résultat.

Le résultat est toujours une valeur booléenne. Une valeur booléenne détermine si l'expression est `true` ou `false`.

Il existe trois opérateurs logiques en programmation C : AND logique (`&&`), OR logique (`||`) et NOT logique (`!`).

Examinons chacun d'eux plus en détail dans les sections suivantes.


### Comment utiliser l'opérateur logique AND (`&&`) en programmation C
L'opérateur logique AND (`&&`) vérifie si **tous** les opérandes sont `true` – le résultat est `true` uniquement lorsque tous les opérandes sont `true`.

Voici la table de vérité pour l'opérateur AND (`&&`) lorsque vous travaillez avec deux opérandes :
| Premier opérande | Deuxième opérande | Résultat |
| --- | --- | --- |
| true | true | true |
| true | false | false |
| false | true | false |
| false | false | false |

Une chose à noter ici est que, lorsque le premier opérande est `false`, le deuxième opérande n'est pas évalué.

Prenons un exemple :
Le résultat de `(10 == 10) && (20 == 20)` est `true` parce que les *deux* opérandes sont `true` – `(10 == 10)` est `true` *et* `(20 == 20)` est `true`.

Prenons un autre exemple :
Le résultat de `(10 == 20) && (20 == 20)` est `false` parce qu'un des opérandes est `false` – dans ce cas, le premier opérande est `false`, donc le deuxième opérande n'est pas évalué.

Maintenant, voyons comment vous pouvez utiliser l'opérateur `&&` dans une instruction `if` :
```c
#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 30;

  if (a > 10 && b > 10)
    printf("Les deux nombres sont supérieurs à 10\n");
}

// sortie

// Les deux nombres sont supérieurs à 10
```

Dans l'exemple ci-dessus, la sortie est `Les deux nombres sont supérieurs à 10` parce que la condition `a > 10 && b > 10` est satisfaite.

`a > 10` et `b > 10` sont tous deux `true`, donc le résultat est `true`.

Si soit `a` soit `b` ne satisfaisait pas la condition, il n'y aurait pas de sortie dans la console puisque je n'ai pas spécifié de condition `else`.


### Comment utiliser l'opérateur logique OR (`||`) en programmation C
L'opérateur logique OR (`||`) vérifie si l'un des opérandes est `true` – le résultat est `true` si *au moins un* des opérandes est `true`.

Voici la table de vérité pour l'opérateur OR (`||`) lorsque vous travaillez avec deux opérandes :
| Premier opérande | Deuxième opérande | Résultat |
| --- | --- | --- |
| true | true | true |
| true | false | true |
| false | true | true |
| false | false | false |

Notez qu'avec l'opérateur OR (`||`), si le premier opérande est `true`, alors le deuxième opérande n'est pas évalué.

Prenons un exemple :
Le résultat de `(10 == 20) || (20 == 20)` est `true` parce qu'au moins un des opérandes est `true`, dans ce cas, c'est le deuxième opérande, même si le premier opérande est `false`.

Prenons un autre exemple :
Le résultat de `(20 == 20) || (10 == 20)` est `true` parce qu'un des opérandes est `true` – dans ce cas, puisque le premier opérande est `true`, le deuxième n'est pas évalué.

Maintenant, voyons comment vous pouvez utiliser l'opérateur OR (`||`) dans une instruction `if` :
```c
#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if (a > 10 || b > 10)
    printf("Au moins un des nombres est supérieur à 10");
}
```

Dans l'exemple ci-dessus, la sortie est `Au moins un des nombres est supérieur à 10` parce que la condition `a > 10 || b > 10` est satisfaite – au moins un des opérandes est `true`.

La première condition, `a > 10`, est `true`, donc le résultat est `true`.

Si `a` et `b` étaient tous deux `false`, il n'y aurait pas de sortie.


### Comment utiliser l'opérateur logique NOT (`!`) en programmation C
L'opérateur logique NOT (`!`) nie l'opérande – c'est-à-dire qu'il retourne l'opposé de l'opérande.

Si l'opérande est `true`, il retourne `false`.

Et si c'est `false`, il retourne `true`.

Voici la table de vérité pour l'opérateur NOT (`!`) :
| Opérande | Résultat |
| --- | --- |
| true | false |
| false | true |

Prenons un exemple :
Le résultat de `!(10 == 10)` est `false`.

La condition `10 == 10` est `true`, mais l'opérateur `!` la nie.

Et prenons un autre exemple :
Le résultat de `!(10 == 20)` est `true`.

La condition `10 == 20` est `false`, mais l'opérateur `!` la nie.

Maintenant, vérifiez l'exemple ci-dessous pour voir comment vous pouvez utiliser l'opérateur NOT (`!`) dans une instruction `if` :
```c

#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if ( a > b)
    printf("a est supérieur à b\n");
}
```

La sortie est `a est supérieur à b` parce que la condition `a > b` est `true`.

Cependant, si vous utilisiez l'opérateur NOT (`!`), la condition n'est plus `true`, donc il n'y aurait pas de sortie :
```c

#include <stdio.h>

int main(void) {
  int a = 20;
  int b = 5;

  if ( !(a > b))
    printf("a est supérieur à b\n");
}
```


## Conclusion
Et voilà ! Vous savez maintenant comment fonctionnent les trois opérateurs logiques en programmation C.

Pour en apprendre davantage sur le C, [lisez ce guide du débutant en C](https://www.freecodecamp.org/news/the-c-beginners-handbook/) pour vous familiariser avec les bases du langage.

Merci d'avoir lu, et bon codage !