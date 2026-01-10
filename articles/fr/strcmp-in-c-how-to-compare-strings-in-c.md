---
title: strcmp en C – Comment comparer des chaînes de caractères en C
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-27T20:32:00.000Z'
originalURL: https://freecodecamp.org/news/strcmp-in-c-how-to-compare-strings-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/max-duzij-qAjJk-un3BI-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: strcmp en C – Comment comparer des chaînes de caractères en C
seo_desc: "Comparing strings is a common task in most programming languages. In C,\
  \ you can use the strcmp function to handle string comparisons. \nIn this article,\
  \ I will show you practical examples of the strcmp function, and offer insights\
  \ into how it compares..."
---

Comparer des chaînes de caractères est une tâche courante dans la plupart des langages de programmation. En C, vous pouvez utiliser la fonction `strcmp` pour gérer les comparaisons de chaînes.

Dans cet article, je vais vous montrer des exemples pratiques de la fonction `strcmp`, et vous offrir des informations sur la manière dont elle compare les chaînes, ce que ses valeurs de retour signifient, et comment l'utiliser efficacement.

Vous verrez également quelques bonnes pratiques pour vous aider à optimiser votre code.

## Qu'est-ce qu'une chaîne de caractères en C ?

Avant de discuter de la fonction `strcmp`, il est important de comprendre les bases des chaînes de caractères en C.

Une chaîne de caractères est un tableau de caractères terminé par un caractère nul ('\0'). Les chaînes de caractères sont généralement représentées soit en utilisant des pointeurs de caractères (`char *`), soit des tableaux de caractères (`char []`).

## Qu'est-ce que la fonction `strcmp()` de C, et comment fonctionne-t-elle ?

La fonction `strcmp()` fait partie de la bibliothèque standard C (`string.h`). Son objectif principal est de comparer les caractères des deux chaînes en séquence jusqu'à ce qu'elle trouve une non-correspondance ou jusqu'à ce que la fin des chaînes soit atteinte (c'est-à-dire le caractère nul '\0'). Dans notre monde de la programmation, nous appelons cela une recherche basée sur l'ordre [lexicographique](https://en.wikipedia.org/wiki/Lexicographic_order).

Le prototype de la fonction `strcmp` est le suivant :

```c
int strcmp(const char *s1, const char *s2);
```

Voici ce que signifient les paramètres ci-dessus :

* **s1** désigne la première chaîne à comparer.
* **s2** désigne la deuxième chaîne à comparer.

`strcmp()` est comme un jeu qui compare deux mots. Il nous aide à identifier si un mot vient avant ou après un autre mot dans le dictionnaire.

* Si le premier mot (**s1**) vient avant le deuxième mot (**s2**) dans le dictionnaire, `strcmp()` donne un nombre négatif.
* Si le premier mot (**s1**) vient après le deuxième (**s2**) mot dans le dictionnaire, `strcmp()` donne un nombre positif.
* Si les deux mots sont identiques, `strcmp()` donne le nombre 0.

`strcmp()` compare les caractères correspondants des deux chaînes en fonction de leurs valeurs ASCII, qui sont des codes numériques représentant chaque caractère.

Par conséquent, si la valeur ASCII du premier caractère différent dans la première chaîne est inférieure à la valeur ASCII du caractère correspondant dans la deuxième chaîne, `strcmp()` retourne un nombre négatif. Cela indique que la première chaîne vient avant la deuxième chaîne dans le dictionnaire.

Si la valeur ASCII du premier caractère différent dans la première chaîne est supérieure à la valeur ASCII du caractère correspondant dans la deuxième chaîne, `strcmp()` retourne un nombre positif. Cela indique que la première chaîne vient après la deuxième chaîne dans le dictionnaire.

Si les deux chaînes sont égales jusqu'à la fin de la chaîne la plus courte, `strcmp()` retourne une valeur négative, nulle ou positive selon que la chaîne la plus longue a un caractère avec une valeur ASCII inférieure, égale ou supérieure au caractère nul.

En réalité, le compilateur C implémente cette logique de comparaison des valeurs ASCII des caractères dans deux chaînes et retourne le résultat en conséquence.

## Exemple de la fonction `strcmp()` #1 – Comparaison de chaînes de base

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";

    int result = strcmp(str1, str2);

    if (result == 0) {
        printf("Les chaînes sont égales.\n");
    } else if (result < 0) {
        printf("La chaîne 1 est inférieure à la chaîne 2.\n");
    } else {
        printf("La chaîne 1 est supérieure à la chaîne 2.\n");
    }

    return 0;
}
```

Sortie :

```
La chaîne 1 est inférieure à la chaîne 2.
```

Permettez-moi maintenant d'expliquer chaque ligne du code donné ci-dessus.

Ici, j'ai pris deux chaînes différentes sous forme de deux tableaux de caractères différents, car nous n'avons pas accès aux chaînes directes dans le langage de programmation **C**.

Dans la première chaîne de caractères (`str1[]`), j'ai stocké la chaîne `apple`. Dans la deuxième chaîne de caractères (`str2[]`), j'ai stocké la chaîne `banana`. Comme la fonction `strcmp()` donne une sortie booléenne (vrai/faux, ou 0/1), j'ai pris une autre variable int nommée `result` pour stocker la valeur booléenne (`1` pour `vrai` et `0` pour `faux`).

La fonction `strcmp()` compare les deux chaînes et découvre que la première chaîne `apple` vient avant la deuxième chaîne `banana`. Par conséquent, la fonction `strcmp()` retourne une valeur négative indiquant que la première chaîne est inférieure à la deuxième chaîne.

En fonction de la valeur dans `result`, elle imprime `La chaîne 1 est inférieure à la chaîne 2.`

Si vous êtes confus à propos de "la chaîne vient avant ou après une autre chaîne", alors permettez-moi de vous expliquer un peu plus.

Lorsque nous disons que la première chaîne vient avant la deuxième chaîne, nous voulons dire que si les deux chaînes étaient listées dans un dictionnaire ou une liste triée de mots, la première chaîne apparaîtrait avant la deuxième chaîne.

Dans le cas du programme ci-dessus, la première chaîne est `"apple"`, et la deuxième chaîne est `"banana"`. Si nous devions chercher ces deux mots dans un dictionnaire, nous trouverions que `"apple"` apparaît avant `"banana"`, ce qui signifie que la première chaîne vient avant la deuxième chaîne.

La fonction `strcmp()` compare les deux chaînes caractère par caractère et détermine quelle chaîne vient en premier dans le dictionnaire en fonction des valeurs ASCII des caractères.

Dans ce cas, le premier caractère de `"apple"` (qui est `'a'`) a une valeur ASCII inférieure (valeur ASCII pour a = 97) à celle du premier caractère de `"banana"` (qui est `'b'` et la valeur ASCII pour b = 98), donc `strcmp()` retourne une valeur négative, indiquant que la première chaîne vient avant la deuxième chaîne.

J'espère que cela clarifie toute confusion concernant la phrase "une chaîne vient après/avant une autre chaîne".

## Exemple de la fonction `strcmp()` #2 – Comparaison de chaînes insensible à la casse

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "apple";

    // Convertir les deux chaînes en minuscules
    for (int i = 0; str1[i]; i++) {
        str1[i] = tolower(str1[i]);
    }
    for (int i = 0; str2[i]; i++) {
        str2[i] = tolower(str2[i]);
    }

    int result = strcmp(str1, str2);

    if (result == 0) {
        printf("Les chaînes sont égales.\n");
    } else if (result < 0) {
        printf("La chaîne 1 est inférieure à la chaîne 2.\n");
    } else {
        printf("La chaîne 1 est supérieure à la chaîne 2.\n");
    }

    return 0;
}
```

Sortie :

```
Les chaînes sont égales.
```

Ici, j'ai converti les deux chaînes en minuscules. J'ai utilisé une boucle `for` pour changer tous les caractères de la chaîne en minuscules en utilisant la fonction `tolower()`. Les boucles `for` convertissent les deux chaînes en minuscules en itérant sur chaque caractère des chaînes en utilisant une variable d'index `i`, et en appelant la fonction `tolower()` sur chaque caractère pour le convertir en minuscules.

Après avoir converti les deux chaînes en minuscules, j'ai appelé la fonction `strcmp()` pour vérifier si les deux chaînes sont égales ou non, comme précédemment. J'ai stocké la sortie de la fonction `strcmp()` dans une nouvelle variable nommée `result`, comme précédemment.

L'instruction `if` vérifie la valeur de `result` et imprime le message correspondant selon que les chaînes sont égales, ou quelle chaîne est inférieure ou supérieure. Ici, les deux chaînes deviennent égales après les avoir converties en minuscules. Ainsi, la première instruction `if` s'exécute et fournit la sortie.

Gardez à l'esprit que, après avoir converti les deux chaînes en minuscules, la valeur de `str1` est `"apple"`, qui est la même que la valeur de `str2` en ASCII.

Par conséquent, lorsque la fonction `strcmp()` est appelée, elle retourne `0`, ce qui indique que les chaînes sont égales. Cela peut être utile lorsque nous voulons comparer des chaînes qui peuvent différer en casse mais qui doivent être considérées comme égales.

## Bonnes pratiques pour `strcmp()`

Voici quelques bonnes pratiques à suivre lors de l'utilisation de la fonction `strcmp()` :

* Incluez toujours l'en-tête `string.h` lors de l'utilisation de `strcmp()`.
* Pour comparer des chaînes insensibles à la casse, utilisez une fonction personnalisée comme `strcasecmp()` ou une fonction de bibliothèque standard comme `stricmp()`.
* Soyez prudent lorsque vous comparez des chaînes qui peuvent contenir des caractères non-ASCII, car `strcmp()` utilise la différence de valeurs ASCII pour les comparaisons, ce qui peut ne pas fonctionner comme prévu pour les caractères non-ASCII. Dans de tels cas, envisagez d'utiliser une fonction ou une bibliothèque de comparaison compatible Unicode.

Si vous souhaitez en savoir plus sur les caractères ASCII, consultez [cet article](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/).

## Fonctions alternatives de comparaison de chaînes

Outre `strcmp()`, il existe d'autres fonctions de comparaison de chaînes disponibles dans la bibliothèque standard C :

* `strncmp()` : Compare jusqu'à un nombre spécifié de caractères de deux chaînes. Elle est utile lorsque vous souhaitez comparer uniquement une partie des chaînes.
* `strcoll()` : Cela est assez intéressant. Permettez-moi de vous expliquer plus en détail.

La fonction `strcoll()` est comme un jeu qui nous aide à comparer deux mots ou chaînes, tout comme `strcmp()`. Mais `strcoll()` est conçue pour gérer les chaînes qui contiennent des caractères non-ASCII ou nécessitent des comparaisons spécifiques à une langue, comme des mots provenant de différentes langues.

`strcoll()` utilise les règles de comparaison des mots spécifiques à la langue ou à la région, basées sur le paramètre régional actuel de l'ordinateur. En d'autres termes, elle compare les mots selon les règles de collation spécifiques à la langue du paramètre régional, qui peuvent être différentes de l'ordre ASCII standard utilisé par `strcmp()`.

Par exemple, en espagnol, le mot "cañón" (qui signifie "canyon" en anglais) est classé après "casa" (qui signifie "maison" en anglais), car la lettre "ñ" est considérée comme une lettre distincte dans l'alphabet espagnol, et vient après "n".

Ainsi, `strcoll()` peut être utile pour comparer des mots provenant de différentes langues ou régions ayant des règles de collation spécifiques, et nous utilisons cette fonction pour ce type de besoin spécifique.

## Conclusion

Dans cet article, nous avons exploré la fonction `strcmp()` en C, comment elle compare les chaînes et ses valeurs de retour. Nous avons également examiné des exemples et des bonnes pratiques pour utiliser `strcmp` efficacement.

Avec ces connaissances, vous pouvez facilement comparer des chaînes en C comme un professionnel. N'oubliez pas de considérer des fonctions de comparaison alternatives comme `strncmp()` et `strcoll()` lorsque vous travaillez avec des cas d'utilisation spécifiques, tels que des comparaisons de chaînes partielles ou spécifiques à une locale.

Si cet article vous aide d'une manière ou d'une autre, faites-le moi savoir via [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/). Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) et consulter ma [chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1), et [mon site web](https://fahimbinamin.com/). Vous pouvez également [m'offrir un café](https://www.buymeacoffee.com/fahimbinamin) si vous souhaitez me soutenir.

Couverture : Photo de [Max Duzij](https://unsplash.com/@max_duz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/programming?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)