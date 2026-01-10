---
title: 'Les constantes en C expliquées – Comment utiliser #define et le qualificatif
  const pour définir des constantes'
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-26T21:13:20.000Z'
originalURL: https://freecodecamp.org/news/constants-in-c-explained-how-to-use-define-and-const-keyword
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/andrew-coop-9F5IWESAxL4-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: 'Les constantes en C expliquées – Comment utiliser #define et le qualificatif
  const pour définir des constantes'
seo_desc: 'When you''re programming, there are times when you''ll want the values
  of certain variables to remain unchanged. In the C language, you''ll likely define
  them as constants.

  You can define constants in C in a few different ways. In this tutorial, you''ll
  ...'
---

Lorsque vous programmez, il arrive que vous souhaitiez que les valeurs de certaines variables restent inchangées. En langage C, vous les définirez probablement comme des constantes.

Vous pouvez définir des constantes en C de plusieurs manières. Dans ce tutoriel, vous apprendrez à utiliser `#define` et le qualificatif `const` pour les définir.

Commençons.

## Comment utiliser `#define` pour définir des constantes en C

L'une des méthodes courantes pour définir des constantes en C consiste à utiliser la directive de préprocesseur `#define`, comme illustré ci-dessous :

```c
#define <VAR_NAME> <VALUE>
```

Dans la syntaxe ci-dessus :

* `<VAR_NAME>` est un espace réservé pour le nom de la constante.
* Il est recommandé de nommer les constantes en _majuscules_, car cela aide à les différencier des autres variables définies dans le programme.
* `<VALUE>` est un espace réservé pour la valeur que prend `<VAR_NAME>`.
* `#define` est une directive de préprocesseur.
* Avant la compilation du programme, le préprocesseur remplace toutes les occurrences de `<VAR_NAME>` par `<VALUE>`.

En C, les préprocesseurs traitent le code source avant la compilation pour produire le code source étendu. Cela est illustré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-59.png)
_Préprocesseur C_

Il est bon de pratique d'inclure la définition de toutes les _constantes_ après les fichiers d'en-tête dans votre programme, comme illustré ci-dessous :

```c
#include <stdio.h>

#define CONSTANT_1 VALUE_1
#define CONSTANT_2 VALUE_2
//

int main()
    {
        // instructions ici
    }
```

➡ Dans la section suivante, vous verrez un exemple utilisant `#define` pour déclarer des constantes en C.

### Comment déclarer des constantes en utilisant `#define` - Exemple

Considérez l'extrait de code suivant, où vous avez deux constantes `STUDENT_ID` et `COURSE_CODE`.

```c
#include <stdio.h>
#define STUDENT_ID 27
#define COURSE_CODE 502

int main()
{
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}


# Sortie
Student ID: 27 is taking the class 502

```

Dans cet exemple :

* Le préprocesseur remplace `STUDENT_ID` et `COURSE_CODE` par 27 et 502, respectivement. Ainsi, le corps de la fonction `main()` sera maintenant :

```c
int main()
{
    printf("Student ID: %d is taking the class %d\n", 27, 502);

    return 0;
}
```

* Comme la fonction `printf()` peut imprimer des chaînes formatées, les deux occurrences des spécificateurs de format `%d` (pour les entiers décimaux) sont remplacées par 27 et 502.

> Bien que `#define` vous permette de définir des constantes, vous devez faire attention à ne pas les redéfinir ailleurs dans le programme.

Par exemple, dans le code ci-dessous, vous avez redéfini `STUDENT_ID`. Et il compilera et s'exécutera sans erreurs.

```c
#include <stdio.h>
#define STUDENT_ID 27
#define STUDENT_ID 207 // redéfinition d'une constante #define.
#define COURSE_CODE 502

int main()
{
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}

```

Selon votre compilateur, vous pouvez obtenir un avertissement indiquant que vous essayez de _redéfinir_ une constante déjà définie.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-76.png)

Et la valeur de la définition la plus récente sera utilisée.

Remarquez comment la valeur redéfinie de `207` a été utilisée comme `STUDENT_ID`, écrasant la valeur précédemment définie `27`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-77.png)

Ainsi, vous savez maintenant que les constantes `#define` ne sont pas, en un sens, de vraies constantes, car vous pouvez toujours les redéfinir.

Passez à la section suivante pour en savoir plus sur le qualificatif `const`.

## Comment utiliser le qualificatif `const` pour définir des constantes en C

En C, `<data_type> <var_name> = <value>` est la syntaxe pour déclarer une variable `<var_name>` de type `<data_type>`, et lui attribuer la valeur `<value>`.

Pour rendre `<var_name>` une constante, vous devez simplement ajouter le qualificatif `const` à cette instruction comme suit :

```c
const <data_type> <var_name> = <value>;
```

> L'ajout du mot-clé `const` dans la définition de la variable garantit que sa valeur reste inchangée dans le programme.

Le qualificatif `const` rend la variable _en lecture seule_. Et essayer de la modifier ailleurs dans le programme générera des erreurs lors de la compilation.

➡ Passez à la section suivante pour modifier l'exemple précédent en utilisant `const`.

### Comment déclarer des constantes en utilisant le qualificatif `const` - Exemple

Dans l'exemple précédent, vous avez les constantes `STUDENT_ID` et `COURSE_CODE`. Maintenant, vous allez les définir comme des constantes en utilisant le qualificatif `const`.

* Puisqu'elles sont toutes deux des entiers, vous pouvez les définir comme étant de type `int`, prenant les valeurs prévues : `27` et `502`.
* Incluez le qualificatif `const` dans les définitions respectives.

Cela est montré dans l'extrait de code ci-dessous :

```c
#include <stdio.h>

int main()
{
    const int STUDENT_ID = 27;
    const int COURSE_CODE = 502;
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}

# Sortie
Student ID: 27 is taking the class 502

```

Vous pouvez voir que le code fonctionne comme prévu.

> En C, vous ne pouvez pas redéfinir une variable existante.

Par exemple, si `int my_var = 2` est la première définition, votre programme ne compilera pas avec succès si vous essayez de redéfinir `my_var` comme `int my_var = 3`.

> Cependant, vous pouvez toujours réassigner des valeurs à une variable.

Cela signifie que si `int my_var = 2` est la définition, vous pouvez attribuer une valeur différente à `my_var` en utilisant une simple instruction d'assignation comme `my_var = 3`.

Essayons maintenant de modifier la variable `const` `STUDENT_ID`.

```c
#include <stdio.h>

int main()
{
    const int STUDENT_ID = 27;
    STUDENT_ID = 207; // modification d'une vraie constante : IMPOSSIBLE
    const int COURSE_CODE = 502;
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}


```

Vous verrez que le programme ne compile pas avec succès.

Et le message d'erreur indique : `error: assignment of read-only variable 'student_id'` ce qui signifie que vous ne pouvez que lire la valeur de `STUDENT_ID` et non lui attribuer une valeur.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-82.png)

Ainsi, le qualificatif `const` crée une _vraie constante_ qui est immunisée contre les changements et ne peut pas être altérée pendant l'exécution du programme.

## Conclusion

Dans ce tutoriel, vous avez appris à définir des constantes :

* en utilisant la directive de préprocesseur `#define` avec la syntaxe `#define <VAR_NAME> <VALUE>`, et
* en utilisant le qualificatif `const` pour rendre les variables _en lecture seule_.

J'espère que vous avez trouvé ce tutoriel utile. Bon codage ! 😄