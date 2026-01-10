---
title: 'Le guide du débutant en C : Apprenez les bases du langage de programmation
  C en quelques heures'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-03-09T11:50:52.000Z'
originalURL: https://freecodecamp.org/news/the-c-beginners-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/coverc-1-opt.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: 'Le guide du débutant en C : Apprenez les bases du langage de programmation
  C en quelques heures'
seo_desc: 'This C Beginner''s Handbook follows the 80/20 rule. You''ll learn 80% of
  the C programming language in 20% of the time.

  This approach will give you a well-rounded overview of the language.

  This handbook does not try to cover everything under the sun re...'
---

Ce guide du débutant en C suit la règle 80/20. Vous apprendrez 80 % du langage de programmation C en 20 % du temps.

Cette approche vous donnera un aperçu bien équilibré du langage.

Ce guide ne tente pas de couvrir tout ce qui concerne C. Il se concentre sur le cœur du langage, en essayant de simplifier les sujets les plus complexes.

Et notez bien : [Vous pouvez obtenir une version PDF et ePub de ce guide du débutant en C ici](https://flaviocopes.com/page/c-handbook/).

Bonne lecture !

## Table des matières

1. [Introduction à C](#heading-introduction-a-c)
2. [Variables et types](#heading-variables-et-types)
3. [Constantes](#heading-constantes)
4. [Opérateurs](#heading-operateurs)
5. [Conditionnelles](#heading-conditionnelles)
6. [Boucles](#heading-boucles)
7. [Tableaux](#heading-tableaux)
8. [Chaînes de caractères](#heading-chaines-de-caracteres)
9. [Pointeurs](#heading-pointeurs)
10. [Fonctions](#heading-fonctions)
11. [Entrée et sortie](#heading-entree-et-sortie)
12. [Portée des variables](#heading-portee-des-variables)
13. [Variables statiques](#heading-variables-statiques)
14. [Variables globales](#heading-variables-globales)
15. [Définitions de types](#heading-definitions-de-types)
16. [Types énumérés](#heading-types-enumeres)
17. [Structures](#heading-structures)
18. [Paramètres de ligne de commande](#heading-parametres-de-ligne-de-commande)
19. [Fichiers d'en-tête](#heading-fichiers-dentete)
20. [Le préprocesseur](#heading-le-preprocesseur)
21. [Conclusion](#heading-conclusion)

## Introduction à C

C est probablement le langage de programmation le plus connu. Il est utilisé comme langage de référence pour les cours d'informatique dans le monde entier, et c'est probablement le langage que les gens apprennent le plus à l'école, avec Python et Java.

Je me souviens que c'était mon deuxième langage de programmation, après Pascal.

C n'est pas seulement ce que les étudiants utilisent pour apprendre la programmation. Ce n'est pas un langage académique. Et je dirais que ce n'est pas le langage le plus facile, car C est un langage de programmation plutôt bas niveau.

Aujourd'hui, C est largement utilisé dans les appareils embarqués, et il alimente la plupart des serveurs Internet, qui sont construits en utilisant Linux. Le noyau Linux est construit en utilisant C, et cela signifie également que C alimente le cœur de tous les appareils Android. Nous pouvons dire que le code C exécute une bonne partie du monde entier. Maintenant même. Assez remarquable.

Lorsqu'il a été créé, C était considéré comme un langage de haut niveau, car il était portable sur différentes machines. Aujourd'hui, nous prenons un peu pour acquis que nous pouvons exécuter un programme écrit sur un Mac sous Windows ou Linux, peut-être en utilisant Node.js ou Python.

Il fut un temps où ce n'était pas du tout le cas. Ce que C a apporté, c'est un langage qui était simple à implémenter et qui avait un compilateur qui pouvait être facilement porté sur différentes machines.

J'ai dit compilateur : C est un langage de programmation compilé, comme Go, Java, Swift ou Rust. D'autres langages de programmation populaires comme Python, Ruby ou JavaScript sont interprétés. La différence est significative : un langage compilé génère un fichier binaire qui peut être directement exécuté et distribué.

C n'est pas garbage collected. Cela signifie que nous devons gérer la mémoire nous-mêmes. C'est une tâche complexe et qui nécessite beaucoup d'attention pour éviter les bugs, mais c'est aussi ce qui rend C idéal pour écrire des programmes pour des appareils embarqués comme Arduino.

C ne cache pas la complexité et les capacités de la machine sous-jacente. Vous avez beaucoup de pouvoir, une fois que vous savez ce que vous pouvez faire.

Je veux introduire le premier programme C maintenant, que nous appellerons "Bonjour, le monde !"

hello.c

```c
#include <stdio.h>

int main(void) {
    printf("Bonjour, le monde !");
}

```

Décrivons le code source du programme : nous importons d'abord la bibliothèque `stdio` (le nom signifie bibliothèque d'entrée-sortie standard).

Cette bibliothèque nous donne accès aux fonctions d'entrée/sortie.

C est un langage très petit dans son cœur, et tout ce qui ne fait pas partie du cœur est fourni par des bibliothèques. Certaines de ces bibliothèques sont construites par des programmeurs normaux, et mises à disposition pour que d'autres les utilisent. Certaines autres bibliothèques sont intégrées dans le compilateur. Comme `stdio` et d'autres.

`stdio` est la bibliothèque qui fournit la fonction `printf()`.

Cette fonction est enveloppée dans une fonction `main()`. La fonction `main()` est le point d'entrée de tout programme C.

Mais qu'est-ce qu'une fonction, au fait ?

Une fonction est une routine qui prend un ou plusieurs arguments, et retourne une seule valeur.

Dans le cas de `main()`, la fonction ne reçoit aucun argument, et retourne un entier. Nous l'identifions en utilisant le mot-clé `void` pour l'argument, et le mot-clé `int` pour la valeur de retour.

La fonction a un corps, qui est enveloppé dans des accolades. À l'intérieur du corps, nous avons tout le code dont la fonction a besoin pour effectuer ses opérations.

La fonction `printf()` est écrite différemment, comme vous pouvez le voir. Elle n'a pas de valeur de retour définie, et nous passons une chaîne, enveloppée dans des guillemets doubles. Nous n'avons pas spécifié le type de l'argument.

C'est parce que c'est une invocation de fonction. Quelque part, à l'intérieur de la bibliothèque `stdio`, `printf` est défini comme

```c
int printf(const char *format, ...);

```

Vous n'avez pas besoin de comprendre ce que cela signifie maintenant, mais en bref, c'est la définition. Et lorsque nous appelons `printf("Bonjour, le monde !");`, c'est là que la fonction est exécutée.

La fonction `main()` que nous avons définie ci-dessus :

```c
#include <stdio.h>

int main(void) {
    printf("Bonjour, le monde !");
}

```

sera exécutée par le système d'exploitation lorsque le programme est exécuté.

Comment exécutons-nous un programme C ?

Comme mentionné, C est un langage compilé. Pour exécuter le programme, nous devons d'abord le compiler. Tout ordinateur Linux ou macOS est déjà équipé d'un compilateur C intégré. Pour Windows, vous pouvez utiliser le sous-système Windows pour Linux (WSL).

Dans tous les cas, lorsque vous ouvrez la fenêtre de terminal, vous pouvez taper `gcc`, et cette commande devrait retourner une erreur indiquant que vous n'avez pas spécifié de fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.10.50.png)

C'est bien. Cela signifie que le compilateur C est là, et nous pouvons commencer à l'utiliser.

Maintenant, tapez le programme ci-dessus dans un fichier `hello.c`. Vous pouvez utiliser n'importe quel éditeur, mais pour simplifier, je vais utiliser l'éditeur `nano` en ligne de commande :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.11.39.png)

Tapez le programme :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.16.52.png)

Maintenant, appuyez sur `ctrl-X` pour quitter :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.18.11.png)

Confirmez en appuyant sur la touche `y`, puis appuyez sur entrée pour confirmer le nom du fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.18.15.png)

C'est tout, nous devrions être de retour au terminal maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.13.46.png)

Maintenant, tapez

```sh
gcc hello.c -o hello

```

Le programme ne devrait vous donner aucune erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.16.31.png)

mais il devrait avoir généré un exécutable `hello`. Maintenant, tapez

```sh
./hello

```

pour l'exécuter :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.19.20.png)

Je préfixe `./` au nom du programme pour indiquer au terminal que la commande se trouve dans le dossier courant.

Génial !

Maintenant, si vous appelez `ls -al hello`, vous pouvez voir que le programme ne fait que 12 Ko :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-01-29-at-10.19.55.png)

C'est l'un des avantages de C : il est hautement optimisé, et c'est aussi l'une des raisons pour lesquelles il est si bon pour les appareils embarqués qui ont une quantité très limitée de ressources.

## Variables et types

C est un langage typé statiquement.

Cela signifie que toute variable a un type associé, et ce type est connu au moment de la compilation.

C'est très différent de la façon dont vous travaillez avec des variables en Python, JavaScript, PHP et autres langages interprétés.

Lorsque vous créez une variable en C, vous devez spécifier le type de la variable au moment de la déclaration.

Dans cet exemple, nous initialisons une variable `age` avec le type `int` :

```c
int age;

```

Un nom de variable peut contenir n'importe quelle lettre majuscule ou minuscule, peut contenir des chiffres et le caractère de soulignement, mais il ne peut pas commencer par un chiffre. `AGE` et `Age10` sont des noms de variables valides, `1age` ne l'est pas.

Vous pouvez également initialiser une variable au moment de la déclaration, en spécifiant la valeur initiale :

```c
int age = 37;

```

Une fois que vous avez déclaré une variable, vous pouvez alors l'utiliser dans votre code de programme. Vous pouvez changer sa valeur à tout moment, en utilisant l'opérateur `=` par exemple, comme dans `age = 100;` (à condition que la nouvelle valeur soit du même type).

Dans ce cas :

```c
#include <stdio.h>

int main(void) {
    int age = 0;
    age = 37.2;
    printf("%u", age);
}

```

le compilateur émettra un avertissement au moment de la compilation, et convertira le nombre décimal en une valeur entière.

Les types de données intégrés de C sont `int`, `char`, `short`, `long`, `float`, `double`, `long double`. Découvrons-en plus sur ceux-ci.

### Nombres entiers

C nous fournit les types suivants pour définir des valeurs entières :

* `char`
* `int`
* `short`
* `long`

La plupart du temps, vous utiliserez probablement un `int` pour stocker un entier. Mais dans certains cas, vous pourriez vouloir choisir l'une des trois autres options.

Le type `char` est couramment utilisé pour stocker les lettres du tableau ASCII, mais il peut être utilisé pour contenir de petits entiers de `-128` à `127`. Il prend au moins 1 octet.

`int` prend au moins 2 octets. `short` prend au moins 2 octets. `long` prend au moins 4 octets.

Comme vous pouvez le voir, nous ne sommes pas garantis des mêmes valeurs pour différents environnements. Nous n'avons qu'une indication. Le problème est que les nombres exacts qui peuvent être stockés dans chaque type de données dépendent de l'implémentation et de l'architecture.

Nous sommes garantis que `short` n'est pas plus long que `int`. Et nous sommes garantis que `long` n'est pas plus court que `int`.

La spécification ANSI C standard détermine les valeurs minimales de chaque type, et grâce à elle, nous pouvons au moins savoir quelle est la valeur minimale que nous pouvons nous attendre à avoir à notre disposition.

Si vous programmez en C sur un Arduino, différentes cartes auront différentes limites.

Sur une carte Arduino Uno, `int` stocke une valeur de 2 octets, allant de `-32,768` à `32,767`. Sur un Arduino MKR 1010, `int` stocke une valeur de 4 octets, allant de `-2,147,483,648` à `2,147,483,647`. Une différence assez grande.

Sur toutes les cartes Arduino, `short` stocke une valeur de 2 octets, allant de `-32,768` à `32,767`. `long` stocke 4 octets, allant de `-2,147,483,648` à `2,147,483,647`.

### Entiers non signés

Pour tous les types de données ci-dessus, nous pouvons préfixer `unsigned` pour commencer la plage à 0, au lieu d'un nombre négatif. Cela peut avoir du sens dans de nombreux cas.

* `unsigned char` ira de `0` à au moins `255`
* `unsigned int` ira de `0` à au moins `65,535`
* `unsigned short` ira de `0` à au moins `65,535`
* `unsigned long` ira de `0` à au moins `4,294,967,295`

### Le problème de débordement

Étant donné toutes ces limites, une question peut se poser : comment pouvons-nous nous assurer que nos nombres ne dépassent pas la limite ? Et que se passe-t-il si nous dépassons la limite ?

Si vous avez un nombre `unsigned int` à 255, et que vous l'incrémentez, vous obtiendrez 256 en retour. Comme prévu. Si vous avez un nombre `unsigned char` à 255, et que vous l'incrémentez, vous obtiendrez 0 en retour. Il se réinitialise en commençant par la valeur initiale possible.

Si vous avez un nombre `unsigned char` à 255 et que vous ajoutez 10 à celui-ci, vous obtiendrez le nombre `9` :

```c
#include <stdio.h>

int main(void) {
  unsigned char j = 255;
  j = j + 10;
  printf("%u", j); /* 9 */
}

```

Si vous n'avez pas de valeur signée, le comportement est indéfini. Il vous donnera essentiellement un nombre énorme qui peut varier, comme dans ce cas :

```c
#include <stdio.h>

int main(void) {
  char j = 127;
  j = j + 10;
  printf("%u", j); /* 4294967177 */
}

```

En d'autres termes, C ne vous protège pas du dépassement des limites d'un type. Vous devez vous en occuper vous-même.

### Avertissements lors de la déclaration du mauvais type

Lorsque vous déclarez la variable et l'initialisez avec la mauvaise valeur, le compilateur `gcc` (celui que vous utilisez probablement) devrait vous avertir :

```c
#include <stdio.h>

int main(void) {
  char j = 1000;
}

```

```
hello.c:4:11: warning: implicit conversion 
  from 'int' to
      'char' changes value from 1000 to -24
      [-Wconstant-conversion]
        char j = 1000;
             ~   ^~~~
1 warning generated.

```

Et il vous avertit également dans les affectations directes :

```c
#include <stdio.h>

int main(void) {
  char j;
  j = 1000;
}

```

Mais pas si vous incrémentez le nombre en utilisant, par exemple, `+=` :

```c
#include <stdio.h>

int main(void) {
  char j = 0;
  j += 1000;
}

```

### Nombres à virgule flottante

Les types à virgule flottante peuvent représenter un ensemble de valeurs beaucoup plus grand que les entiers, et peuvent également représenter des fractions, ce que les entiers ne peuvent pas faire.

En utilisant des nombres à virgule flottante, nous représentons les nombres comme des nombres décimaux multipliés par des puissances de 10.

Vous pourriez voir des nombres à virgule flottante écrits comme

* `1.29e-3`
* `-2.3e+5`

et d'autres façons apparemment étranges.

Les types suivants :

* `float`
* `double`
* `long double`

sont utilisés pour représenter des nombres avec des points décimaux (types à virgule flottante). Tous peuvent représenter à la fois des nombres positifs et négatifs.

Les exigences minimales pour toute implémentation C sont que `float` peut représenter une plage entre 10^-37 et 10^+37, et est généralement implémenté en utilisant 32 bits. `double` peut représenter un ensemble plus grand de nombres. `long double` peut contenir encore plus de nombres.

Les chiffres exacts, comme pour les valeurs entières, dépendent de l'implémentation.

Sur un Mac moderne, un `float` est représenté en 32 bits, et a une précision de 24 bits significatifs. 8 bits sont utilisés pour encoder l'exposant.

Un nombre `double` est représenté en 64 bits, avec une précision de 53 bits significatifs. 11 bits sont utilisés pour encoder l'exposant.

Le type `long double` est représenté en 80 bits, a une précision de 64 bits significatifs. 15 bits sont utilisés pour encoder l'exposant.

Sur votre ordinateur spécifique, comment pouvez-vous déterminer la taille spécifique des types ? Vous pouvez écrire un programme pour le faire :

```c
#include <stdio.h>

int main(void) {
  printf("char size: %lu bytes\n", sizeof(char));
  printf("int size: %lu bytes\n", sizeof(int));
  printf("short size: %lu bytes\n", sizeof(short));
  printf("long size: %lu bytes\n", sizeof(long));
  printf("float size: %lu bytes\n", sizeof(float));
  printf("double size: %lu bytes\n", 
    sizeof(double));
  printf("long double size: %lu bytes\n", 
    sizeof(long double));
}

```

Dans mon système, un Mac moderne, il imprime :

```
char size: 1 bytes
int size: 4 bytes
short size: 2 bytes
long size: 8 bytes
float size: 4 bytes
double size: 8 bytes
long double size: 16 bytes

```

## Constantes

Parlons maintenant des constantes.

Une constante est déclarée de manière similaire aux variables, sauf qu'elle est précédée du mot-clé `const`, et vous devez toujours spécifier une valeur.

Comme ceci :

```c
const int age = 37;

```

Ceci est un C parfaitement valide, bien qu'il soit courant de déclarer les constantes en majuscules, comme ceci :

```c
const int AGE = 37;

```

Ce n'est qu'une convention, mais une convention qui peut grandement vous aider lors de la lecture ou de l'écriture d'un programme C car elle améliore la lisibilité. Un nom en majuscules signifie constante, un nom en minuscules signifie variable.

Un nom de constante suit les mêmes règles que les noms de variables : peut contenir n'importe quelle lettre majuscule ou minuscule, peut contenir des chiffres et le caractère de soulignement, mais il ne peut pas commencer par un chiffre. `AGE` et `Age10` sont des noms de variables valides, `1AGE` ne l'est pas.

Une autre façon de définir des constantes est d'utiliser cette syntaxe :

```c
#define AGE 37

```

Dans ce cas, vous n'avez pas besoin d'ajouter un type, et vous n'avez pas non plus besoin du signe `=` égal, et vous omettez le point-virgule à la fin.

Le compilateur C déduira le type de la valeur spécifiée, au moment de la compilation.

## Opérateurs

C nous offre une grande variété d'opérateurs que nous pouvons utiliser pour opérer sur les données.

En particulier, nous pouvons identifier divers groupes d'opérateurs :

* opérateurs arithmétiques
* opérateurs de comparaison
* opérateurs logiques
* opérateurs d'affectation composés
* opérateurs bit à bit
* opérateurs de pointeur
* opérateurs de structure
* opérateurs divers

Dans cette section, je vais détailler chacun d'eux, en utilisant deux variables imaginaires `a` et `b` comme exemples.

Je garde les opérateurs bit à bit, les opérateurs de structure et les opérateurs de pointeur hors de cette liste, pour garder les choses plus simples.

### Opérateurs arithmétiques

Dans ce groupe macro, je vais séparer les opérateurs binaires et les opérateurs unaires.

Les opérateurs binaires fonctionnent en utilisant deux opérandes :

| Opérateur    | Nom           | Exemple      |
|-------------|----------------|--------------|
| `=`       | Affectation     | `a = b`     |
| `+`       | Addition       | `a + b`     |
| `-`       | Soustraction    | `a - b`     |
| `*`       | Multiplication | `a * b`     |
| `/`       | Division       | `a / b`     |
| `%`       | Modulo         | `a % b`     |

Les opérateurs unaires ne prennent qu'un seul opérande :

| Opérateur    | Nom           | Exemple      |
|-------------|----------------|--------------|
| `+`       | Plus unaire     | `+a`     |
| `-`       | Moins unaire      | `-a`     |
| `++`       | Incrément    | `a++` ou `++a`     |
| `--`       | Décrément    | `a--` ou `--a`     |



La différence entre `a++` et `++a` est que `a++` incrémente la variable `a` après l'avoir utilisée. `++a` incrémente la variable `a` avant de l'utiliser.

Par exemple :

```c
int a = 2;
int b;
b = a++ /* b est 2, a est 3 */
b = ++a /* b est 4, a est 4 */

```

La même chose s'applique à l'opérateur de décrément.

### Opérateurs de comparaison

| Opérateur    | Nom           | Exemple      |
|-------------|----------------|--------------|
| `==`  | Opérateur égal     | `a == b`   |
| `!=`  | Opérateur non égal | `a != b` |
| `>`   | Plus grand que    | `a > b` |
| `<`   | Plus petit que | `a < b`  |
| `>=`  | Plus grand que ou égal à | `a >= b` |
| `<=`  | Plus petit que ou égal à | `a <= b` |


### Opérateurs logiques

* `!` NON (exemple : `!a`)
* `&&` ET (exemple : `a && b`)
* `||` OU (exemple : `a || b`)

Ces opérateurs sont excellents lorsque vous travaillez avec des valeurs booléennes.

### Opérateurs d'affectation composés

Ces opérateurs sont utiles pour effectuer une affectation et en même temps effectuer une opération arithmétique :

| Opérateur | Nom                      | Exemple  |
| -------- | ------------------------- | -------- |
| `+=`     | Affectation d'addition       | `a += b` |
| `-=`     | Affectation de soustraction    | `a -= b` |
| `*=`     | Affectation de multiplication | `a *= b` |
| `/=`     | Affectation de division       | `a /= b` |
| `%=`     | Affectation de modulo         | `a %= b` |


### L'opérateur ternaire

L'opérateur ternaire est le seul opérateur en C qui fonctionne avec 3 opérandes, et c'est une manière courte d'exprimer des conditionnelles.

Voici à quoi il ressemble :

```c
<condition> ? <expression> : <expression>

```

Exemple :

```c
a ? b : c

```

Si `a` est évalué à `true`, alors l'instruction `b` est exécutée, sinon `c` l'est.

L'opérateur ternaire est fonctionnellement identique à une conditionnelle if/else, sauf qu'il est plus court à exprimer et qu'il peut être intégré dans une expression.

### sizeof

L'opérateur `sizeof` retourne la taille de l'opérande que vous passez. Vous pouvez passer une variable, ou même un type.

Exemple d'utilisation :

```c
#include <stdio.h>

int main(void) {
  int age = 37;
  printf("%ld\n", sizeof(age));
  printf("%ld", sizeof(int));
}

```

### Priorité des opérateurs

Avec tous ces opérateurs (et plus encore, que je n'ai pas couverts dans cet article, y compris les opérateurs bit à bit, les opérateurs de structure et les opérateurs de pointeur), nous devons faire attention lorsque nous les utilisons ensemble dans une seule expression.

Supposons que nous avons cette opération :

```c
int a = 2;
int b = 4;
int c = b + a * a / b - a;

```

Quelle est la valeur de `c` ? Est-ce que nous obtenons l'addition exécutée avant la multiplication et la division ?

Il existe un ensemble de règles qui nous aident à résoudre ce puzzle.

Dans l'ordre de la priorité la moins élevée à la plus élevée, nous avons :

* l'opérateur d'affectation `=`
* les opérateurs `+` et `-` **binaires**
* les opérateurs `*` et `/`
* les opérateurs unaires `+` et `-`

Les opérateurs ont également une règle d'associativité, qui est toujours de gauche à droite sauf pour les opérateurs unaires et l'affectation.

Dans :

```c
int c = b + a * a / b - a;

```

Nous exécutons d'abord `a * a / b`, qui, en raison de l'ordre de gauche à droite, nous pouvons séparer en `a * a` et le résultat `/ b` : `2 * 2 = 4`, `4 / 4 = 1`.

Ensuite, nous pouvons effectuer la somme et la soustraction : 4 + 1 - 2. La valeur de `c` est `3`.

Dans tous les cas, cependant, je veux m'assurer que vous réalisez que vous pouvez utiliser des parenthèses pour rendre toute expression similaire plus facile à lire et à comprendre.

Les parenthèses ont une priorité plus élevée que tout le reste.

L'expression de l'exemple ci-dessus peut être réécrite comme :

```c
int c = b + ((a * a) / b) - a;

```

et nous n'avons pas à y penser autant.

## Conditionnelles

Tout langage de programmation offre aux programmeurs la possibilité de faire des choix.

Nous voulons faire X dans certains cas, et Y dans d'autres cas.

Nous voulons vérifier les données, et faire des choix en fonction de l'état de ces données.

C nous offre 2 façons de le faire.

La première est l'instruction `if`, avec son aide `else`, et la seconde est l'instruction `switch`.

### if

Dans une instruction `if`, vous pouvez vérifier qu'une condition est vraie, puis exécuter le bloc fourni dans les accolades :

```c
int a = 1;

if (a == 1) {
  /* faire quelque chose */
}

```

Vous pouvez ajouter un bloc `else` pour exécuter un bloc différent si la condition originale s'avère fausse :

```c
int a = 1;

if (a == 2) {
  /* faire quelque chose */
} else {
  /* faire quelque chose d'autre */
}

```

Méfiez-vous d'une source courante de bugs - utilisez toujours l'opérateur de comparaison `==` dans les comparaisons, et non l'opérateur d'affectation `=`. Si vous ne le faites pas, la vérification conditionnelle `if` sera toujours vraie, sauf si l'argument est `0`, par exemple si vous faites :

```c
int a = 0;

if (a = 0) {
  /* jamais invoqué */
}

```

Pourquoi cela se produit-il ? Parce que la vérification conditionnelle recherchera un résultat booléen (le résultat d'une comparaison), et le nombre `0` équivaut toujours à une valeur fausse. Tout le reste est vrai, y compris les nombres négatifs.

Vous pouvez avoir plusieurs blocs `else` en empilant plusieurs instructions `if` :

```c
int a = 1;

if (a == 2) {
  /* faire quelque chose */
} else if (a == 1) {
  /* faire quelque chose d'autre */
} else {
  /* faire quelque chose d'autre encore */
}

```

### switch

Si vous devez faire trop de blocs if / else / if pour effectuer une vérification, peut-être parce que vous devez vérifier la valeur exacte d'une variable, alors `switch` peut être très utile pour vous.

Vous pouvez fournir une variable comme condition, et une série de points d'entrée `case` pour chaque valeur que vous attendez :

```c
int a = 1;

switch (a) {
  case 0:
    /* faire quelque chose */
    break;
  case 1:
    /* faire quelque chose d'autre */
    break;
  case 2:
    /* faire quelque chose d'autre */
    break;
}

```

Nous avons besoin d'un mot-clé `break` à la fin de chaque cas pour éviter que le cas suivant soit exécuté lorsque le précédent se termine. Cet effet "cascade" peut être utile de manière créative.

Vous pouvez ajouter un cas "attrape-tout" à la fin, étiqueté `default` :

```c
int a = 1;

switch (a) {
  case 0:
    /* faire quelque chose */
    break;
  case 1:
    /* faire quelque chose d'autre */
    break;
  case 2:
    /* faire quelque chose d'autre */
    break;
  default:
    /* gérer tous les autres cas */
    break;
}

```

## Boucles

C nous offre trois façons de réaliser une boucle : **les boucles for**, **les boucles while** et **les boucles do while**. Elles permettent toutes d'itérer sur des tableaux, mais avec quelques différences. Examinons-les en détail.

### Boucles For

La première et probablement la manière la plus courante de réaliser une boucle est **les boucles for**.

En utilisant le mot-clé `for`, nous pouvons définir les _règles_ de la boucle dès le départ, puis fournir le bloc qui sera exécuté de manière répétée.

Comme ceci :

```c
for (int i = 0; i <= 10; i++) {
  /* instructions à répéter */
}

```

Le bloc `(int i = 0; i <= 10; i++)` contient 3 parties des détails de la boucle :

* la condition initiale (`int i = 0`)
* le test (`i <= 10`)
* l'incrément (`i++`)

Nous définissons d'abord une variable de boucle, dans ce cas nommée `i`. `i` est un nom de variable courant utilisé pour les boucles, avec `j` pour les boucles imbriquées (une boucle à l'intérieur d'une autre boucle). Ce n'est qu'une convention.

La variable est initialisée à la valeur 0, et la première itération est effectuée. Ensuite, elle est incrémentée comme l'indique la partie incrément (`i++` dans ce cas, incrémentant de 1), et tout le cycle se répète jusqu'à ce que vous atteigniez le nombre 10.

À l'intérieur du bloc principal de la boucle, nous pouvons accéder à la variable `i` pour savoir à quelle itération nous sommes. Ce programme devrait imprimer `0 1 2 3 4 5 5 6 7 8 9 10` :

```c
for (int i = 0; i <= 10; i++) {
  /* instructions à répéter */
  printf("%u ", i);
}

```

Les boucles peuvent également commencer par un nombre élevé et descendre à un nombre plus bas, comme ceci :

```c
for (int i = 10; i > 0; i--) {
  /* instructions à répéter */
}

```

Vous pouvez également incrémenter la variable de boucle par 2 ou une autre valeur :

```c
for (int i = 0; i < 1000; i = i + 30) {
  /* instructions à répéter */
}

```

### Boucles While

**Les boucles While** sont plus simples à écrire qu'une boucle `for`, car elles nécessitent un peu plus de travail de votre part.

Au lieu de définir toutes les données de la boucle dès le début lorsque vous commencez la boucle, comme vous le faites dans la boucle `for`, en utilisant `while`, vous vérifiez simplement une condition :

```c
while (i < 10) {

}

```

Cela suppose que `i` est déjà défini et initialisé avec une valeur.

Et cette boucle sera une **boucle infinie** à moins que vous n'incrémentiez la variable `i` à un moment donné à l'intérieur de la boucle. Une boucle infinie est mauvaise car elle bloquera le programme, ne permettant rien d'autre de se produire.

Voici ce dont vous avez besoin pour une boucle "while" "correcte" :

```c
int i = 0;

while (i < 10) {
  /* faire quelque chose */

  i++;
}

```

Il y a une exception à cela, et nous la verrons dans une minute. Avant cela, laissez-moi vous présenter `do while`.

### Boucles Do while

Les boucles While sont excellentes, mais il peut y avoir des moments où vous devez faire une chose particulière : vous voulez toujours exécuter un bloc, puis _peut-être_ le répéter.

Cela se fait en utilisant le mot-clé `do while`. D'une certaine manière, c'est très similaire à une boucle `while`, mais légèrement différent :

```c
int i = 0;

do {
  /* faire quelque chose */

  i++;
} while (i < 10);

```

Le bloc qui contient le commentaire `/* faire quelque chose */` est toujours exécuté au moins une fois, indépendamment de la vérification de la condition en bas.

Ensuite, jusqu'à ce que `i` soit inférieur à 10, nous répéterons le bloc.

### Sortir d'une boucle en utilisant break

Dans toutes les boucles C, nous avons un moyen de sortir d'une boucle à tout moment, immédiatement, indépendamment des conditions définies pour la boucle.

Cela se fait en utilisant le mot-clé `break`.

Cela est utile dans de nombreux cas. Vous pourriez vouloir vérifier la valeur d'une variable, par exemple :

```c
for (int i = 0; i <= 10; i++) {
  if (i == 4 && someVariable == 10) {
    break;
  }
}

```

Avoir cette option pour sortir d'une boucle est particulièrement intéressant pour les boucles `while` (et `do while` aussi), car nous pouvons créer des boucles apparemment infinies qui se terminent lorsqu'une condition se produit. Vous définissez cela à l'intérieur du bloc de la boucle :

```c
int i = 0;
while (1) {
  /* faire quelque chose */

  i++;
  if (i == 10) break;
}

```

Il est assez courant d'avoir ce type de boucle en C.

## Tableaux

Un tableau est une variable qui stocke plusieurs valeurs.

Chaque valeur dans le tableau, en C, doit avoir le **même type**. Cela signifie que vous aurez des tableaux de valeurs `int`, des tableaux de valeurs `double`, et plus encore.

Vous pouvez définir un tableau de valeurs `int` comme ceci :

```c
int prices[5];

```

Vous devez toujours spécifier la taille du tableau. C ne fournit pas de tableaux dynamiques prêt à l'emploi (vous devez utiliser une structure de données comme une liste chaînée pour cela).

Vous pouvez utiliser une constante pour définir la taille :

```c
const int SIZE = 5;
int prices[SIZE];

```

Vous pouvez initialiser un tableau au moment de la définition, comme ceci :

```c
int prices[5] = { 1, 2, 3, 4, 5 };

```

Mais vous pouvez également attribuer une valeur après la définition, de cette manière :

```c
int prices[5];

prices[0] = 1;
prices[1] = 2;
prices[2] = 3;
prices[3] = 4;
prices[4] = 5;

```

Ou, plus pratique, en utilisant une boucle :

```c
int prices[5];

for (int i = 0; i < 5; i++) {
  prices[i] = i + 1;
}

```

Et vous pouvez référencer un élément dans le tableau en utilisant des crochets après le nom de la variable de tableau, en ajoutant un entier pour déterminer la valeur de l'index. Comme ceci :

```c
prices[0]; /* valeur de l'élément du tableau : 1 */
prices[1]; /* valeur de l'élément du tableau : 2 */

```

Les index des tableaux commencent à 0, donc un tableau avec 5 éléments, comme le tableau `prices` ci-dessus, aura des éléments allant de `prices[0]` à `prices[4]`.

La chose intéressante à propos des tableaux C est que tous les éléments d'un tableau sont stockés séquentiellement, les uns à la suite des autres. Ce n'est pas quelque chose qui se produit normalement avec les langages de programmation de plus haut niveau.

Une autre chose intéressante est la suivante : le nom de la variable du tableau, `prices` dans l'exemple ci-dessus, est un **pointeur** vers le premier élément du tableau. En tant que tel, il peut être utilisé comme un pointeur normal.

Plus sur les pointeurs bientôt.

## Chaînes de caractères

En C, les chaînes de caractères sont un type spécial de tableau : une chaîne est un tableau de valeurs `char` :

```c
char name[7];

```

J'ai introduit le type `char` lorsque j'ai présenté les types, mais en bref, il est couramment utilisé pour stocker les lettres du tableau ASCII.

Une chaîne peut être initialisée comme vous initialisez un tableau normal :

```c
char name[7] = { "F", "l", "a", "v", "i", "o" };

```

Ou plus commodément avec un littéral de chaîne (également appelé constante de chaîne), une séquence de caractères enfermée dans des guillemets doubles :

```c
char name[7] = "Flavio";

```

Vous pouvez imprimer une chaîne via `printf()` en utilisant `%s` :

```c
printf("%s", name);

```

Remarquez-vous comment "Flavio" fait 6 caractères de long, mais j'ai défini un tableau de longueur 7 ? Pourquoi ? C'est parce que le dernier caractère d'une chaîne doit être une valeur `0`, le terminateur de chaîne, et nous devons faire de la place pour celui-ci.

C'est important à garder à l'esprit, surtout lorsque vous manipulez des chaînes.

En parlant de manipulation de chaînes, il y a une bibliothèque standard très importante qui est fournie par C : `string.h`.

Cette bibliothèque est essentielle car elle abstrait de nombreux détails de bas niveau du travail avec les chaînes, et nous fournit un ensemble de fonctions utiles.

Vous pouvez charger la bibliothèque dans votre programme en ajoutant en haut :

```c
#include <string.h>

```

Et une fois que vous l'avez fait, vous avez accès à :

* `strcpy()` pour copier une chaîne sur une autre chaîne
* `strcat()` pour ajouter une chaîne à une autre chaîne
* `strcmp()` pour comparer deux chaînes pour l'égalité
* `strncmp()` pour comparer les premiers `n` caractères de deux chaînes
* `strlen()` pour calculer la longueur d'une chaîne

et bien d'autres.

## Pointeurs

Les pointeurs sont l'une des parties les plus confuses/difficiles de C, à mon avis. Surtout si vous êtes nouveau en programmation, mais aussi si vous venez d'un langage de programmation de plus haut niveau comme Python ou JavaScript.

Dans cette section, je veux les introduire de la manière la plus simple possible sans les simplifier à l'excès.

Un pointeur est l'adresse d'un bloc de mémoire qui contient une variable.

Lorsque vous déclarez un nombre entier comme ceci :

```c
int age = 37;

```

Nous pouvons utiliser l'opérateur `&` pour obtenir la valeur de l'adresse en mémoire d'une variable :

```c
printf("%p", &age); /* 0x7ffeef7dcb9c */

```

J'ai utilisé le format `%p` spécifié dans `printf()` pour imprimer la valeur de l'adresse.

Nous pouvons assigner l'adresse à une variable :

```c
int *address = &age;

```

En utilisant `int *address` dans la déclaration, nous ne déclarons pas une variable entière, mais plutôt un **pointeur vers un entier**.

Nous pouvons utiliser l'opérateur de pointeur `*` pour obtenir la valeur de la variable à laquelle une adresse pointe :

```c
int age = 37;
int *address = &age;
printf("%u", *address); /* 37 */

```

Cette fois, nous utilisons à nouveau l'opérateur de pointeur, mais comme ce n'est pas une déclaration cette fois, cela signifie "la valeur de la variable vers laquelle ce pointeur pointe".

Dans cet exemple, nous déclarons une variable `age`, et nous utilisons un pointeur pour initialiser la valeur :

```c
int age;
int *address = &age;
*address = 37;
printf("%u", *address);

```

Lorsque vous travaillez avec C, vous constaterez que beaucoup de choses sont construites sur ce concept simple. Assurez-vous donc de vous familiariser un peu avec lui en exécutant les exemples ci-dessus par vous-même.

Les pointeurs sont une grande opportunité car ils nous obligent à réfléchir aux adresses mémoire et à la manière dont les données sont organisées.

Les tableaux en sont un exemple. Lorsque vous déclarez un tableau :

```c
int prices[3] = { 5, 4, 3 };

```

La variable `prices` est en fait un pointeur vers le premier élément du tableau. Vous pouvez obtenir la valeur du premier élément en utilisant cette fonction `printf()` dans ce cas :

```c
printf("%u", *prices); /* 5 */

```

Le truc cool est que nous pouvons obtenir le deuxième élément en ajoutant 1 au pointeur `prices` :

```c
printf("%u", *(prices + 1)); /* 4 */

```

Et ainsi de suite pour toutes les autres valeurs.

Nous pouvons également faire de nombreuses opérations de manipulation de chaînes intéressantes, puisque les chaînes sont des tableaux sous le capot.

Nous avons également de nombreuses autres applications, y compris le passage de la référence d'un objet ou d'une fonction pour éviter de consommer plus de ressources pour le copier.

## Fonctions

Les fonctions sont le moyen par lequel nous pouvons structurer notre code en sous-routines que nous pouvons :

1. donner un nom
2. appeler lorsque nous en avons besoin

À partir de votre tout premier programme, un "Bonjour, le monde !", vous utilisez immédiatement les fonctions C :

```c
#include <stdio.h>

int main(void) {
    printf("Bonjour, le monde !");
}

```

La fonction `main()` est une fonction très importante, car c'est le point d'entrée d'un programme C.

Voici une autre fonction :

```c
void doSomething(int value) {
    printf("%u", value);
}

```

Les fonctions ont 4 aspects importants :

1. elles ont un nom, afin que nous puissions les invoquer ("appeler") plus tard
2. elles spécifient une valeur de retour
3. elles peuvent avoir des arguments
4. elles ont un corps, enveloppé dans des accolades

Le corps de la fonction est l'ensemble des instructions qui sont exécutées chaque fois que nous invoquons une fonction.

Si la fonction n'a pas de valeur de retour, vous pouvez utiliser le mot-clé `void` avant le nom de la fonction. Sinon, vous spécifiez le type de valeur de retour de la fonction (`int` pour un entier, `float` pour une valeur à virgule flottante, `const char *` pour une chaîne, etc).

Vous ne pouvez pas retourner plus d'une valeur d'une fonction.

Une fonction peut avoir des arguments. Ils sont optionnels. Si elle n'en a pas, à l'intérieur des parenthèses, nous insérons `void`, comme ceci :

```c
void doSomething(void) {
   /* ... */
}

```

Dans ce cas, lorsque nous invoquons la fonction, nous l'appellerons avec rien dans les parenthèses :

```c
doSomething();

```

Si nous avons un paramètre, nous spécifions le type et le nom du paramètre, comme ceci :

```c
void doSomething(int value) {
   /* ... */
}

```

Lorsque nous invoquons la fonction, nous passerons ce paramètre dans les parenthèses, comme ceci :

```c
doSomething(3);

```

Nous pouvons avoir plusieurs paramètres, et si c'est le cas, nous les séparons en utilisant une virgule, à la fois dans la déclaration et dans l'invocation :

```c
void doSomething(int value1, int value2) {
   /* ... */
}

doSomething(3, 4);

```

Les paramètres sont passés par **copie**. Cela signifie que si vous modifiez `value1`, sa valeur est modifiée localement. La valeur en dehors de la fonction, où elle a été passée dans l'invocation, ne change pas.

Si vous passez un **pointeur** comme paramètre, vous pouvez modifier la valeur de cette variable car vous pouvez maintenant y accéder directement en utilisant son adresse mémoire.

Vous ne pouvez pas définir de valeur par défaut pour un paramètre. C++ peut le faire (et donc les programmes en langage Arduino), mais pas C.

Assurez-vous de définir la fonction avant de l'appeler, sinon le compilateur émettra un avertissement et une erreur :

```
  ~ gcc hello.c -o hello; ./hello
hello.c:13:3: warning: implicit declaration of
      function 'doSomething' is invalid in C99
      [-Wimplicit-function-declaration]
  doSomething(3, 4);
  ^
hello.c:17:6: error: conflicting types for
      'doSomething'
void doSomething(int value1, char value2) {
     ^
hello.c:13:3: note: previous implicit declaration
      is here
  doSomething(3, 4);
  ^
1 warning and 1 error generated.

```

L'avertissement que vous obtenez concerne l'ordre, que j'ai déjà mentionné.

L'erreur concerne une autre chose, liée. Puisque C ne "voit" pas la déclaration de la fonction avant l'invocation, il doit faire des suppositions. Et il suppose que la fonction retourne `int`. La fonction, cependant, retourne `void`, d'où l'erreur.

Si vous changez la définition de la fonction en :

```c
int doSomething(int value1, int value2) {
  printf("%d %d\n", value1, value2);
  return 1;
}

```

vous n'obtiendrez que l'avertissement, et non l'erreur :

```
  ~ gcc hello.c -o hello; ./hello
hello.c:14:3: warning: implicit declaration of
      function 'doSomething' is invalid in C99
      [-Wimplicit-function-declaration]
  doSomething(3, 4);
  ^
1 warning generated.

```

Dans tous les cas, assurez-vous de déclarer la fonction avant de l'utiliser. Soit déplacez la fonction vers le haut, soit ajoutez le prototype de la fonction dans un fichier d'en-tête.

À l'intérieur d'une fonction, vous pouvez déclarer des variables.

```c
void doSomething(int value) {
  int doubleValue = value * 2;
}

```

Une variable est créée au moment de l'invocation de la fonction et est détruite lorsque la fonction se termine. Elle n'est pas visible de l'extérieur.

À l'intérieur d'une fonction, vous pouvez appeler la fonction elle-même. Cela s'appelle la **récursivité** et c'est quelque chose qui offre des opportunités particulières.

## Entrée et sortie

C est un petit langage, et le "cœur" de C n'inclut aucune fonctionnalité d'entrée/sortie (I/O).

Ce n'est pas quelque chose de unique à C, bien sûr. Il est courant que le cœur du langage soit agnostique de l'I/O.

Dans le cas de C, l'entrée/sortie nous est fournie par la bibliothèque standard C via un ensemble de fonctions définies dans le fichier d'en-tête `stdio.h`.

Vous pouvez importer cette bibliothèque en utilisant :

```c
#include <stdio.h>

```

en haut de votre fichier C.

Cette bibliothèque nous fournit, parmi de nombreuses autres fonctions :

* `printf()`
* `scanf()`
* `sscanf()`
* `fgets()`
* `fprintf()`

Avant de décrire ce que font ces fonctions, je veux prendre une minute pour parler des **flux I/O**.

Nous avons 3 types de flux I/O en C :

* `stdin` (entrée standard)
* `stdout` (sortie standard)
* `stderr` (erreur standard)

Avec les fonctions I/O, nous travaillons toujours avec des flux. Un flux est une interface de haut niveau qui peut représenter un périphérique ou un fichier. Du point de vue de C, il n'y a aucune différence entre la lecture d'un fichier ou la lecture de la ligne de commande : c'est un flux I/O dans tous les cas.

C'est une chose à garder à l'esprit.

Certaines fonctions sont conçues pour travailler avec un flux spécifique, comme `printf()`, que nous utilisons pour imprimer des caractères sur `stdout`. En utilisant son homologue plus général `fprintf()`, nous pouvons spécifier sur quel flux écrire.

Puisque j'ai commencé à parler de `printf()`, je vais l'introduire maintenant.

`printf()` est l'une des premières fonctions que vous utiliserez lorsque vous apprendrez la programmation C.

Dans sa forme d'utilisation la plus simple, vous lui passez un littéral de chaîne :

```c
printf("hey!");

```

et le programme imprimera le contenu de la chaîne à l'écran.

Vous pouvez imprimer la valeur d'une variable. Mais c'est un peu délicat car vous devez ajouter un caractère spécial, un espace réservé, qui change en fonction du type de la variable. Par exemple, nous utilisons `%d` pour un chiffre entier décimal signé :

```c
int age = 37;

printf("Mon âge est %d", age);

```

Nous pouvons imprimer plus d'une variable en utilisant des virgules :

```c
int age_yesterday = 37;
int age_today = 36;

printf("Hier, mon âge était %d et aujourd'hui, il est %d", age_yesterday, age_today);

```

Il existe d'autres spécificateurs de format comme `%d` :

* `%c` pour un char
* `%s` pour un char
* `%f` pour les nombres à virgule flottante
* `%p` pour les pointeurs

et bien d'autres.

Nous pouvons utiliser des caractères d'échappement dans `printf()`, comme `\n` que nous pouvons utiliser pour faire en sorte que la sortie crée une nouvelle ligne.

### `scanf()`

`printf()` est utilisé comme fonction de sortie. Je veux maintenant introduire une fonction d'entrée, afin que nous puissions dire que nous pouvons faire toute la chose I/O : `scanf()`.

Cette fonction est utilisée pour obtenir une valeur de l'utilisateur qui exécute le programme, à partir de la ligne de commande.

Nous devons d'abord définir une variable qui contiendra la valeur que nous obtenons de l'entrée :

```c
int age;

```

Ensuite, nous appelons `scanf()` avec 2 arguments : le format (type) de la variable, et l'adresse de la variable :

```c
scanf("%d", &age);

```

Si nous voulons obtenir une chaîne comme entrée, rappelez-vous qu'un nom de chaîne est un pointeur vers le premier caractère, donc vous n'avez pas besoin du caractère `&` avant celui-ci :

```c
char name[20];
scanf("%s", name);

```

Voici un petit programme qui utilise à la fois `printf()` et `scanf()` :

```c
#include <stdio.h>

int main(void) {
  char name[20];
  printf("Entrez votre nom : ");
  scanf("%s", name);
  printf("vous avez entré %s", name);
}

```

## Portée des variables

Lorsque vous définissez une variable dans un programme C, selon l'endroit où vous la déclarez, elle aura une **portée** différente.

Cela signifie qu'elle sera disponible dans certains endroits, mais pas dans d'autres.

La position détermine 2 types de variables :

* **variables globales**
* **variables locales**

Voici la différence : une variable déclarée à l'intérieur d'une fonction est une variable locale, comme ceci :

```c
int main(void) {
  int age = 37;
}

```

Les variables locales ne sont accessibles qu'à partir de la fonction, et lorsque la fonction se termine, elles cessent d'exister. Elles sont effacées de la mémoire (avec quelques exceptions).

Une variable définie à l'extérieur d'une fonction est une variable globale, comme dans cet exemple :

```c
int age = 37;

int main(void) {
  /* ... */
}

```

Les variables globales sont accessibles à partir de n'importe quelle fonction du programme, et elles sont disponibles pour toute l'exécution du programme, jusqu'à ce qu'il se termine.

J'ai mentionné que les variables locales ne sont plus disponibles après la fin de la fonction.

La raison est que les variables locales sont déclarées sur la **pile**, par défaut, sauf si vous les allouez explicitement sur le tas en utilisant des pointeurs. Mais alors vous devez gérer la mémoire vous-même.

## Variables statiques

À l'intérieur d'une fonction, vous pouvez initialiser une **variable statique** en utilisant le mot-clé `static`.

J'ai dit "à l'intérieur d'une fonction" car les variables globales sont statiques par défaut, donc il n'est pas nécessaire d'ajouter le mot-clé.

Qu'est-ce qu'une variable statique ? Une variable statique est initialisée à 0 si aucune valeur initiale n'est spécifiée, et elle conserve la valeur entre les appels de fonction.

Considérez cette fonction :

```c
int incrementAge() {
  int age = 0;
  age++;
  return age;
}

```

Si nous appelons `incrementAge()` une fois, nous obtiendrons `1` comme valeur de retour. Si nous l'appelons plus d'une fois, nous obtiendrons toujours 1 en retour, car `age` est une variable locale et elle est réinitialisée à `0` à chaque appel de fonction.

Si nous changeons la fonction en :

```c
int incrementAge() {
  static int age = 0;
  age++;
  return age;
}

```

Maintenant, chaque fois que nous appelons cette fonction, nous obtiendrons une valeur incrémentée :

```c
printf("%d\n", incrementAge());
printf("%d\n", incrementAge());
printf("%d\n", incrementAge());

```

nous donnera

```
1
2
3

```

Nous pouvons également omettre d'initialiser `age` à 0 dans `static int age = 0;`, et simplement écrire `static int age;` car les variables statiques sont automatiquement définies à 0 lors de leur création.

Nous pouvons également avoir des tableaux statiques. Dans ce cas, chaque élément individuel du tableau est initialisé à 0 :

```c
int incrementAge() {
  static int ages[3];
  ages[0]++;
  return ages[0];
}

```

## Variables globales

Dans cette section, je veux parler davantage de la différence entre **variables globales et locales**.

Une **variable locale** est définie à l'intérieur d'une fonction, et elle n'est disponible qu'à l'intérieur de cette fonction.

Comme ceci :

```c
#include <stdio.h>

int main(void) {
  char j = 0;
  j += 10;
  printf("%u", j); //10
}

```

`j` n'est pas disponible ailleurs en dehors de la fonction `main`.

Une **variable globale** est définie en dehors de toute fonction, comme ceci :

```c
#include <stdio.h>

char i = 0;

int main(void) {
  i += 10;
  printf("%u", i); //10
}

```

Une variable globale peut être accessible par n'importe quelle fonction du programme. L'accès n'est pas limité à la lecture de la valeur : la variable peut être mise à jour par n'importe quelle fonction.

En raison de cela, les variables globales sont l'un des moyens que nous avons de partager les mêmes données entre les fonctions.

La principale différence avec les variables locales est que la mémoire allouée pour les variables est libérée une fois la fonction terminée.

Les variables globales ne sont libérées que lorsque le programme se termine.

## Définitions de types

Le mot-clé `typedef` en C vous permet de définir de nouveaux types.

À partir des types intégrés de C, nous pouvons créer nos propres types, en utilisant cette syntaxe :

```c
typedef existingtype NEWTYPE

```

Le nouveau type que nous créons est généralement, par convention, en majuscules.

Cela permet de le distinguer plus facilement, et de le reconnaître immédiatement comme un type.

Par exemple, nous pouvons définir un nouveau type `NUMBER` qui est un `int` :

```c
typedef int NUMBER

```

et une fois que vous l'avez fait, vous pouvez définir de nouvelles variables `NUMBER` :

```c
NUMBER one = 1;

```

Maintenant, vous pourriez demander : pourquoi ? Pourquoi ne pas simplement utiliser le type intégré `int` à la place ?

Eh bien, `typedef` devient vraiment utile lorsqu'il est associé à deux choses : les types énumérés et les structures.

## Types énumérés

En utilisant les mots-clés `typedef` et `enum`, nous pouvons définir un type qui peut avoir soit une valeur, soit une autre.

C'est l'une des utilisations les plus importantes du mot-clé `typedef`.

Voici la syntaxe d'un type énuméré :

```c
typedef enum {
  //...valeurs
} TYPENAME;

```

Le type énuméré que nous créons est généralement, par convention, en majuscules.

Voici un exemple simple :

```c
typedef enum {
  true,
  false
} BOOLEAN;

```

C vient avec un type `bool`, donc cet exemple n'est pas vraiment pratique, mais vous comprenez l'idée.

Un autre exemple est de définir les jours de la semaine :

```c
typedef enum {
  monday,  
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday
} WEEKDAY;

```

Voici un programme simple qui utilise ce type énuméré :

```c
#include <stdio.h>

typedef enum {
  monday,  
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday
} WEEKDAY;

int main(void) {
  WEEKDAY day = monday;

  if (day == monday) {
    printf("C'est lundi !"); 
  } else {
    printf("Ce n'est pas lundi"); 
  }
}

```

Chaque élément dans la définition de l'énumération est associé à un entier, en interne. Donc dans cet exemple, `monday` est 0, `tuesday` est 1 et ainsi de suite.

Cela signifie que la conditionnelle aurait pu être `if (day == 0)` au lieu de `if (day == monday)`, mais il est beaucoup plus simple pour nous, humains, de raisonner avec des noms plutôt qu'avec des nombres, donc c'est une syntaxe très pratique.

## Structures

En utilisant le mot-clé `struct`, nous pouvons créer des structures de données complexes en utilisant des types C de base.

Une structure est une collection de valeurs de différents types. Les tableaux en C sont limités à un type, donc les structures peuvent s'avérer très intéressantes dans de nombreux cas d'utilisation.

Voici la syntaxe d'une structure :

```c
struct <structname> {
  //...variables
};

```

Exemple :

```c
struct person {
  int age;
  char *name;
};

```

Vous pouvez déclarer des variables qui ont comme type cette structure en les ajoutant après l'accolade fermante, avant le point-virgule, comme ceci :

```c
struct person {
  int age;
  char *name;
} flavio;

```

Ou plusieurs, comme ceci :

```c
struct person {
  int age;
  char *name;
} flavio, people[20];

```

Dans ce cas, je déclare une seule variable `person` nommée `flavio`, et un tableau de 20 `person` nommé `people`.

Nous pouvons également déclarer des variables plus tard, en utilisant cette syntaxe :

```c
struct person {
  int age;
  char *name;
};

struct person flavio;

```

Nous pouvons initialiser une structure au moment de la déclaration :

```c
struct person {
  int age;
  char *name;
};

struct person flavio = { 37, "Flavio" };

```

et une fois que nous avons une structure définie, nous pouvons accéder aux valeurs qu'elle contient en utilisant un point :

```c
struct person {
  int age;
  char *name;
};

struct person flavio = { 37, "Flavio" };
printf("%s, age %u", flavio.name, flavio.age);

```

Nous pouvons également changer les valeurs en utilisant la syntaxe de point :

```c
struct person {
  int age;
  char *name;
};

struct person flavio = { 37, "Flavio" };

flavio.age = 38;

```

Les structures sont très utiles car nous pouvons les passer comme paramètres de fonction, ou les retourner, en y intégrant diverses variables. Chaque variable a une étiquette.

Il est important de noter que les structures sont **passées par copie**, sauf bien sûr si vous passez un pointeur vers une structure, auquel cas elle est passée par référence.

En utilisant `typedef`, nous pouvons simplifier le code lors de l'utilisation de structures.

Regardons un exemple :

```c
typedef struct {
  int age;
  char *name;
} PERSON;

```

La structure que nous créons en utilisant `typedef` est généralement, par convention, en majuscules.

Maintenant, nous pouvons déclarer de nouvelles variables `PERSON` comme ceci :

```c
PERSON flavio;

```

et nous pouvons les initialiser à la déclaration de cette manière :

```c
PERSON flavio = { 37, "Flavio" };

```

## Paramètres de ligne de commande

Dans vos programmes C, vous pourriez avoir besoin d'accepter des paramètres de la ligne de commande lorsque la commande est lancée.

Pour des besoins simples, tout ce que vous avez à faire pour cela est de changer la signature de la fonction `main()` de

```c
int main(void)

```

en

```c
int main (int argc, char *argv[])

```

`argc` est un nombre entier qui contient le nombre de paramètres fournis dans la ligne de commande.

`argv` est un tableau de chaînes.

Lorsque le programme démarre, les arguments nous sont fournis dans ces 2 paramètres.

Notez qu'il y a toujours au moins un élément dans le tableau `argv` : le nom du programme

Prenons l'exemple du compilateur C que nous utilisons pour exécuter nos programmes, comme ceci :

```sh
gcc hello.c -o hello

```

Si c'était notre programme, nous aurions `argc` à 4 et `argv` étant un tableau contenant

* `gcc`
* `hello.c`
* `-o`
* `hello`

Écrivons un programme qui imprime les arguments qu'il reçoit :

```c
#include <stdio.h>

int main (int argc, char *argv[]) {
  for (int i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
}

```

Si le nom de notre programme est `hello` et que nous l'exécutons comme ceci : `./hello`, nous obtiendrions ceci comme sortie :

```
./hello

```

Si nous passons quelques paramètres aléatoires, comme ceci : `./hello a b c`, nous obtiendrions cette sortie dans le terminal :

```
./hello
a
b
c

```

Ce système fonctionne très bien pour des besoins simples. Pour des besoins plus complexes, il existe des packages couramment utilisés comme **getopt**.

## Fichiers d'en-tête

Les programmes simples peuvent être mis dans un seul fichier. Mais lorsque votre programme devient plus grand, il est impossible de tout garder dans un seul fichier.

Vous pouvez déplacer des parties d'un programme dans un fichier séparé. Ensuite, vous créez un **fichier d'en-tête**.

Un fichier d'en-tête ressemble à un fichier C normal, sauf qu'il se termine par `.h` au lieu de `.c`. Au lieu des implémentations de vos fonctions et des autres parties d'un programme, il contient les **déclarations**.

Vous avez déjà utilisé des fichiers d'en-tête lorsque vous avez utilisé pour la première fois la fonction `printf()`, ou une autre fonction I/O, et que vous avez dû taper :

```c
#include <stdio.h>

```

pour l'utiliser.

`#include` est une directive de préprocesseur.

Le préprocesseur recherche le fichier `stdio.h` dans la bibliothèque standard car vous avez utilisé des crochets autour de celui-ci. Pour inclure vos propres fichiers d'en-tête, vous utiliserez des guillemets, comme ceci :

```c
#include "myfile.h"

```

Ce qui précède recherchera `myfile.h` dans le dossier courant.

Vous pouvez également utiliser une structure de dossiers pour les bibliothèques :

```c
#include "myfolder/myfile.h"

```

Examinons un exemple. Ce programme calcule les années depuis une année donnée :

```c
#include <stdio.h>

int calculateAge(int year) {
  const int CURRENT_YEAR = 2020;
  return CURRENT_YEAR - year;
}

int main(void) {
  printf("%u", calculateAge(1983));
}

```

Supposons que je veux déplacer la fonction `calculateAge` vers un fichier séparé.

Je crée un fichier `calculate_age.c` :

```c
int calculateAge(int year) {
  const int CURRENT_YEAR = 2020;
  return CURRENT_YEAR - year;
}

```

Et un fichier `calculate_age.h` où je mets le _prototype de fonction_, qui est le même que la fonction dans le fichier `.c`, sauf le corps :

```c
int calculateAge(int year);

```

Maintenant, dans le fichier `.c` principal, nous pouvons supprimer la définition de la fonction `calculateAge()`, et nous pouvons importer `calculate_age.h`, ce qui rendra la fonction `calculateAge()` disponible :

```c
#include <stdio.h>
#include "calculate_age.h"

int main(void) {
  printf("%u", calculateAge(1983));
}

```

N'oubliez pas que pour compiler un programme composé de plusieurs fichiers, vous devez tous les lister dans la ligne de commande, comme ceci :

```sh
gcc -o main main.c calculate_age.c

```

Et avec des configurations plus complexes, un Makefile est nécessaire pour indiquer au compilateur comment compiler le programme.

## Le préprocesseur

Le préprocesseur est un outil qui nous aide beaucoup lors de la programmation avec C. Il fait partie de la norme C, tout comme le langage, le compilateur et la bibliothèque standard.

Il analyse notre programme et s'assure que le compilateur obtient tout ce dont il a besoin avant de continuer le processus.

Que fait-il, en pratique ?

Par exemple, il recherche tous les fichiers d'en-tête que vous incluez avec la directive `#include`.

Il regarde également toutes les constantes que vous avez définies en utilisant `#define` et les remplace par leur valeur réelle.

Ce n'est que le début. J'ai mentionné ces 2 opérations car ce sont les plus courantes. Le préprocesseur peut faire beaucoup plus.

Avez-vous remarqué que `#include` et `#define` ont un `#` au début ? C'est commun à toutes les directives du préprocesseur. Si une ligne commence par `#`, elle est prise en charge par le préprocesseur.

### Conditionnelles

L'une des choses que nous pouvons faire est d'utiliser des conditionnelles pour changer la façon dont notre programme sera compilé, en fonction de la valeur d'une expression.

Par exemple, nous pouvons vérifier si la constante `DEBUG` est 0 :

```c
#include <stdio.h>

const int DEBUG = 0;

int main(void) {
#if DEBUG == 0
  printf("Je ne suis PAS en train de déboguer\n");
#else
  printf("Je suis en train de déboguer\n");
#endif
}

```

### Constantes symboliques

Nous pouvons définir une **constante symbolique** :

```c
#define VALUE 1
#define PI 3.14
#define NAME "Flavio"

```

Lorsque nous utilisons NAME ou PI ou VALUE dans notre programme, le préprocesseur remplace son nom par la valeur avant d'exécuter le programme.

Les constantes symboliques sont très utiles car nous pouvons donner des noms aux valeurs sans créer de variables au moment de la compilation.

### Macros

Avec `#define`, nous pouvons également définir une **macro**. La différence entre une macro et une constante symbolique est qu'une macro peut accepter un argument et contient généralement du code, tandis qu'une constante symbolique est une valeur :

```c
#define POWER(x) ((x) * (x))

```

Remarquez les parenthèses autour des arguments : c'est une bonne pratique pour éviter les problèmes lorsque la macro est remplacée dans le processus de précompilation.

Ensuite, nous pouvons l'utiliser dans notre code comme ceci :

```c
printf("%u\n", POWER(4)); //16

```

La grande différence avec les fonctions est que les macros ne spécifient pas le type de leurs arguments ou valeurs de retour, ce qui peut être pratique dans certains cas.

Les macros, cependant, sont limitées aux définitions en une seule ligne.

### Si défini

Nous pouvons vérifier si une constante symbolique ou une macro est définie en utilisant `#ifdef` :

```c
#include <stdio.h>
#define VALUE 1

int main(void) {
#ifdef VALUE
  printf("La valeur est définie\n");
#else
  printf("La valeur n'est pas définie\n");
#endif
}

```

Nous avons également `#ifndev` pour vérifier l'inverse (macro non définie).

Nous pouvons également utiliser `#if defined` et `#if !defined` pour effectuer la même tâche.

Il est courant d'envelopper un bloc de code dans un bloc comme ceci :

```c
#if 0

#endif

```

pour l'empêcher temporairement de s'exécuter, ou pour utiliser une constante symbolique DEBUG :

```c
#define DEBUG 0

#if DEBUG
  //code uniquement envoyé au compilateur
  //si DEBUG n'est pas 0
#endif

```

### Constantes symboliques prédéfinies que vous pouvez utiliser

Le préprocesseur définit également un certain nombre de constantes symboliques que vous pouvez utiliser, identifiées par les 2 traits de soulignement avant et après le nom, notamment :

* `__LINE__` se traduit par la ligne actuelle dans le fichier de code source
* `__FILE__` se traduit par le nom du fichier
* `__DATE__` se traduit par la date de compilation, au format `Mmm jj aaaa`
* `__TIME__` se traduit par l'heure de compilation, au format `hh:mm:ss`

## Conclusion

Merci beaucoup d'avoir lu ce guide !

J'espère qu'il vous inspirera à en savoir plus sur C.

Pour plus de tutoriels, consultez mon blog [flaviocopes.com](https://flaviocopes.com).

Envoyez vos commentaires, errata ou opinions à [hey@flaviocopes.com](mailto:hey@flaviocopes.com)

Et n'oubliez pas : [Vous pouvez obtenir une version PDF et ePub de ce guide du débutant en C ici](https://flaviocopes.com/page/c-handbook/)

Vous pouvez me rejoindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).