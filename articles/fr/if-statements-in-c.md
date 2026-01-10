---
title: L'instruction If...Else en C expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-21T17:07:00.000Z'
originalURL: https://freecodecamp.org/news/if-statements-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9da9740569d1a4ca38ef.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: L'instruction If...Else en C expliquée
seo_desc: 'Conditional code flow is the ability to change the way a piece of code
  behaves based on certain conditions. In such situations you can use if statements.

  The if statement is also known as a decision making statement, as it makes a decision
  on the bas...'
---

Le flux de code conditionnel est la capacité de changer la manière dont un morceau de code se comporte en fonction de certaines conditions. Dans de telles situations, vous pouvez utiliser les instructions `if`.

L'instruction `if` est également connue comme une instruction de prise de décision, car elle prend une décision sur la base d'une condition ou d'une expression donnée. Le bloc de code à l'intérieur de l'instruction `if` est exécuté si la condition est évaluée à vrai. Cependant, le code à l'intérieur des accolades est ignoré si la condition est évaluée à faux, et le code après l'instruction `if` est exécuté.

### Syntaxe d'une instruction `if`

```text
if (testCondition) {
   // instructions
}
```

### Un exemple simple

Regardons un exemple de cela en action :

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    if(true) {
        printf("L'instruction est vraie !\n");
    }

    return 0;
}
```

**Sortie :**

```text
L'instruction est vraie !
```

Si le code à l'intérieur des parenthèses de l'instruction `if` est vrai, tout ce qui se trouve à l'intérieur des accolades est exécuté. Dans ce cas, `true` est évalué à vrai, donc le code exécute la fonction `printf`.

### Les instructions `if..else`

Dans une instruction `if...else`, si le code dans les parenthèses de l'instruction `if` est vrai, le code à l'intérieur de ses crochets est exécuté. Mais si l'instruction à l'intérieur des parenthèses est fausse, tout le code à l'intérieur des crochets de l'instruction `else` est exécuté à la place.

Bien sûr, l'exemple ci-dessus n'est pas très utile dans ce cas car `true` est toujours évalué à vrai. En voici un autre un peu plus pratique :

```c
#include <stdio.h>

int main(void) {
    int n = 2;

    if(n == 3) { // comparer n avec 3
        printf("L'instruction est vraie !\n");
    } 
    else { // si la première condition n'est pas vraie, venir à ce bloc de code
        printf("L'instruction est fausse !\n");
    }

    return 0;
}
```

**Sortie :**

```text
L'instruction est fausse !
```

Il y a quelques différences importantes ici. Premièrement, `stdbool.h` n'a pas été inclus. Ce n'est pas grave car `true` et `false` ne sont pas utilisés comme dans le premier exemple. En C, comme dans d'autres langages de programmation, vous pouvez utiliser des instructions qui s'évaluent à vrai ou faux plutôt que d'utiliser directement les valeurs booléennes `true` ou `false`.

Remarquez également la condition dans les parenthèses de l'instruction `if` : `n == 3`. Cette condition compare `n` et le nombre 3. `==` est l'opérateur de comparaison, et est l'un des plusieurs opérateurs de comparaison en C.

### `if...else` imbriqué

L'instruction `if...else` permet de faire un choix entre deux possibilités. Mais parfois, vous devez choisir entre trois possibilités ou plus.

Par exemple, la fonction signe en mathématiques retourne -1 si l'argument est inférieur à zéro, +1 si l'argument est supérieur à zéro, et retourne zéro si l'argument est zéro.

Le code suivant implémente cette fonction :

```c
if (x < 0)
   sign = -1;
else
   if (x == 0)
      sign = 0;
   else
      sign = 1;
```

Comme vous pouvez le voir, une deuxième instruction `if...else` est imbriquée dans l'instruction `else` de la première instruction `if..else`.

Si `x` est inférieur à 0, alors `sign` est défini à -1. Cependant, si `x` n'est pas inférieur à 0, la deuxième instruction `if...else` est exécutée. Là, si `x` est égal à 0, `sign` est également défini à 0. Mais si `x` est supérieur à 0, `sign` est plutôt défini à 1.

Plutôt qu'une instruction `if...else` imbriquée, les débutants utilisent souvent une série d'instructions `if` :

```c
if (x < 0) {
   sign = -1;
}
   
if (x == 0) {
   sign = 0;
}
   
if (x > 0) {
   sign = 1;
}
```

Bien que cela fonctionne, ce n'est pas recommandé car il n'est pas clair que seule l'une des instructions d'affectation (`sign = ...`) est censée être exécutée en fonction de la valeur de `x`. C'est aussi inefficace – chaque fois que le code s'exécute, les trois conditions sont testées, même si une ou deux n'ont pas besoin de l'être.

### Les instructions else...if

Les instructions `if...else` sont une alternative à une série d'instructions `if`. Considérez ce qui suit :

```c
#include <stdio.h>

int main(void) {
    int n = 5;

    if(n == 5) {
        printf("n est égal à 5 !\n");
    } 
    else if (n > 5) {
        printf("n est supérieur à 5 !\n");
    }

    return 0;
}
```

**Sortie :**

```text
n est égal à 5 !
```

Si la condition pour l'instruction `if` est évaluée à faux, la condition pour l'instruction `else...if` est vérifiée. Si cette condition est évaluée à vrai, le code à l'intérieur des accolades de l'instruction `else...if` est exécuté.

### Opérateurs de comparaison

|Nom de l'opérateur | Utilisation | Résultat|
| --- | --- | --- |
| Égal à |	`a == b` | Vrai si `a` est égal à `b`, faux sinon |
| Différent de |	`a != b` | Vrai si `a` n'est pas égal à `b`, faux sinon |
| Supérieur à | `a > b` | Vrai si `a` est supérieur à `b`, faux sinon |
| Supérieur ou égal à |	`a >= b` | Vrai si `a` est supérieur ou égal à `b`, faux sinon |
| Inférieur à | `a < b` | Vrai si `a` est inférieur à `b`, faux sinon |
| Inférieur ou égal à | `a <= b` | Vrai si `a` est inférieur ou égal à `b`, faux sinon |



## **Opérateurs logiques**

Nous pourrions vouloir qu'un morceau de code s'exécute si quelque chose n'est pas vrai, ou si deux choses sont vraies. Pour cela, nous avons des opérateurs logiques :

|Nom de l'opérateur | Utilisation | Résultat|
| --- | --- | --- |
| Non (`!`) |	`!(a == 3)` | Vrai si `a` n'est **pas** égal à 3 |
| Et (`&&`) |	`a == 3 && b == 6` | Vrai si `a` est égal à 3 **et** `b` est égal à 6 |
| Ou (`||`) |	`a == 2 || b == 4` | Vrai si `a` est égal à 2 **ou** `b` est égal à 4 |


Par exemple :

```c
#include <stdio.h>

int main(void) {
    int n = 5;
    int m = 10;

    if(n > m || n == 15) {
        printf("Soit n est supérieur à m, soit n est égal à 15\n");
    } 
    else if( n == 5 && m == 10 ) {
        printf("n est égal à 5 et m est égal à 10 !\n");
    } 
    else if ( !(n == 6)) {
        printf("Il n'est pas vrai que n est égal à 6 !\n");
    }
    else if (n > 5) {
        printf("n est supérieur à 5 !\n");
    }

    return 0;
}
```

**Sortie :**

```text
n est égal à 5 et m est égal à 10 !
```

### Une note importante sur les comparaisons en C

Bien que nous ayons mentionné précédemment que chaque comparaison vérifie si quelque chose est vrai ou faux, ce n'est que partiellement vrai. C est très léger et proche du matériel sur lequel il s'exécute. Avec le matériel, il est facile de vérifier si quelque chose est 0 ou faux, mais tout le reste est beaucoup plus difficile.

Au lieu de cela, il est beaucoup plus précis de dire que les comparaisons vérifient vraiment si quelque chose est 0 / faux, ou si c'est une autre valeur.

Par exemple, cette instruction if est vraie et valide :

```c
if(12452) {
    printf("Ceci est vrai !\n")
}
```

Par conception, 0 est faux, et par convention, 1 est vrai. En fait, voici un aperçu de la bibliothèque `stdbool.h` :

```c
#define false   0
#define true    1
```

Bien qu'il y ait un peu plus à cela, c'est le cœur de la manière dont les booléens fonctionnent et comment la bibliothèque opère. Ces deux lignes instruisent le compilateur de remplacer le mot `false` par 0, et `true` par 1.