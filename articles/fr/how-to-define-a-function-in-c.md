---
title: Def en C – Comment définir une fonction en C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-12T17:54:27.333Z'
originalURL: https://freecodecamp.org/news/how-to-define-a-function-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/npxXWgQ33ZQ/upload/070d054c2dafa7e4a5f90cf0d0af30eb.jpeg
tags:
- name: C
  slug: c
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: Def en C – Comment définir une fonction en C
seo_desc: 'Functions play a fundamental role in programming in C. They allow you to
  write code that is organized and easier to maintain.

  In this article, you''ll learn the basics of defining functions in C.

  What is a Function in C?

  In programming, a function is ...'
---

Les fonctions jouent un rôle fondamental dans la programmation en C. Elles vous permettent d'écrire du code organisé et plus facile à maintenir.

Dans cet article, vous apprendrez les bases de la définition des fonctions en C.

## **Qu'est-ce qu'une fonction en C ?**

En programmation, une fonction est un bloc de code qui effectue une tâche spécifique.

Les fonctions prennent des entrées, les traitent, effectuent des opérations et produisent une sortie.

Les fonctions sont importantes car elles organisent votre code et favorisent la réutilisabilité du code.

Au lieu d'écrire le même code encore et encore et de vous répéter, vous écrivez le code une fois et pouvez ensuite l'utiliser chaque fois que vous souhaitez effectuer cette tâche spécifique.

En C, il existe généralement deux types de fonctions :

* **Fonctions de la bibliothèque standard**. Les fonctions de la bibliothèque standard sont fournies par la bibliothèque standard C et définies dans les fichiers d'en-tête. Des exemples de fonctions de la bibliothèque standard incluent `printf()` pour imprimer une sortie formatée sur la console et `scanf()` pour lire une entrée formatée de l'utilisateur. Les deux sont définies dans le fichier d'en-tête `stdio.h`.

* **Fonctions définies par l'utilisateur**. Les fonctions définies par l'utilisateur sont définies par vous, le programmeur. Ces fonctions sont adaptées aux besoins et exigences de votre programme. Par exemple, une fonction définie par l'utilisateur peut calculer la somme de deux nombres ou vérifier si un nombre est pair ou impair.

Dans cet article, vous apprendrez à créer des fonctions définies par l'utilisateur.

## Syntaxe des fonctions en C

Voici la syntaxe générale d'une fonction en C :

```c
return_type function_name(parameter) {
  // corps de la fonction avec le code à exécuter
  return value;
}
```

Décomposons cela :

* Le `return_type` indique au compilateur C le type de données de la valeur que la fonction retournera après son exécution. Il peut s'agir de n'importe quel type de données C valide tel que `int`, `float`, `char`, ou `void` si la fonction ne retourne pas de valeur.

* Le `function_name` est le nom que vous donnez à la fonction. Il doit être significatif et décrire avec précision ce que fait la fonction. Vous l'utiliserez plus tard pour appeler la fonction.

* Le `parameter` est facultatif. Un paramètre est une variable qu'une fonction accepte comme entrée entre parenthèses. Une fonction peut recevoir zéro ou plusieurs paramètres. Si la fonction accepte plusieurs paramètres, ils sont séparés par des virgules. Chaque paramètre se compose du type de données suivi d'un nom.

* À l'intérieur des accolades, `{}`, se trouve le corps de la fonction. Ici se trouve le code réel, les instructions qui effectuent une tâche spécifique.

* À l'intérieur du corps de la fonction, il peut y avoir une valeur de retour facultative. Vous utilisez le mot-clé `return` suivi de la valeur que vous souhaitez retourner. Si la fonction a un `void return_type`, vous n'avez pas besoin de spécifier une valeur de retour.

## Comment appeler une fonction en C

Voici la syntaxe pour appeler une fonction en C :

```c
function_name(arguments);
```

Décomposons cela :

* `function_name` est le nom de la fonction que vous souhaitez appeler. Il doit être le même nom que celui que vous avez utilisé pour définir votre fonction.

* `arguments` sont les valeurs que vous passez à la fonction. Si la fonction accepte des paramètres, vous passez les arguments entre parenthèses lorsque vous appelez la fonction. Chaque argument est séparé par une virgule.

Si la fonction retourne une valeur, vous pouvez la stocker dans une variable pour une utilisation ultérieure :

```c
data_type result = function_name(arguments);
```

## Comment définir et appeler une fonction en C – Exemple

Regardons une fonction simple qui additionne deux nombres :

```c
#include <stdio.h>
int add(int num1, int num2) {
    return num1 + num2;
}

int main(void) {
    int num1, num2, result;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    result = add(num1, num2);

    printf("The sum of %d and %d is %d\n", num1, num2, result);

    return 0;
}

// Sortie :

// Enter first number: 2
// Enter second number: 3
// The sum of 2 and 3 is 5
```

Décomposons le code étape par étape.

### Inclure le fichier d'en-tête

J'ai d'abord inclus la bibliothèque `stdio.h` avec la ligne `#include <stdio.h>`.

Cette ligne inclut la bibliothèque standard d'entrée-sortie (`<stdio.h>`), qui vous donne accès aux fonctions `printf()` et `scanf()`. Maintenant, vous pouvez recevoir l'entrée de l'utilisateur et imprimer du texte sur la console.

### Définir la fonction `add`

Ensuite, j'ai défini la fonction suivante :

```c
int add(int num1, int num2) {
    return num1 + num2;
}
```

Cette fonction a un type de retour `int`, ce qui indique qu'elle retournera une valeur entière après son exécution.

La fonction est nommée `add`, et entre parenthèses, elle accepte les paramètres entiers `num1` et `num2`.

À l'intérieur des accolades, le corps de la fonction contient le code de la fonction. Dans ce cas, le code de la fonction se compose uniquement de l'instruction de retour `return num1 + num2;`. Ce code calcule la somme de `num1` et `num2` en utilisant l'opérateur `+`, et retourne le résultat.

La fonction `add()` est définie avant d'être utilisée dans la fonction `main()` plus tard. En C, les fonctions doivent être définies avant d'être utilisées. En plaçant la définition de la fonction `add()` au-dessus de la fonction `main()`, le compilateur la connaît lorsqu'il rencontre l'appel de fonction dans `main()`.

### Définir la fonction `main()`

Ensuite, j'ai défini la fonction `main()`, qui est le point de départ de chaque programme C :

```c
int main(void) {
    int num1, num2, result;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    result = add(num1, num2);

    printf("The sum of %d and %d is %d\n", num1, num2, result);

    return 0;
}
```

À l'intérieur de la fonction `main()`, j'ai d'abord déclaré les variables entières `num1`, `num2` et `result`.

Notez que les variables `num1` et `num2` sont différentes des paramètres `num1` et `num2` que la fonction `add()` reçoit. Ces deux variables stockeront les nombres que l'utilisateur entrera.

Ensuite, j'ai invité l'utilisateur à entrer le premier nombre en utilisant la fonction `printf()`, et j'ai utilisé la fonction `scanf()` pour lire l'entrée et la stocker dans la variable `num1`. Le spécificateur de format `%d` est utilisé pour indiquer que `scanf()` doit s'attendre à une entrée entière.

J'ai suivi la même procédure pour recevoir et stocker le deuxième nombre.

Ensuite, j'ai appelé la fonction `add()` avec `num1` et `num2` comme arguments. La fonction `add()` additionnera les deux nombres. Le résultat du calcul est ensuite stocké dans la variable `result`.

Ensuite, j'ai utilisé la fonction `printf()` pour imprimer les variables `num1`, `num2` et `result` sur la console. Le spécificateur de format `%d` est utilisé pour imprimer des valeurs entières.

Enfin, la ligne `return 0;` est une instruction qui indique que le programme s'est exécuté avec succès. Lorsqu'un programme C se termine, il retourne un statut de sortie au système d'exploitation, avec `0` indiquant généralement que le programme s'est exécuté sans erreur.

### Exécuter le programme

Lorsque le programme est exécuté, la fonction `main()` est appelée en premier.

Vous voyez d'abord l'invite `Enter first number:`. Dans mon cas, j'ai entré `2` comme premier nombre.

Une fois que vous avez entré un nombre, vous verrez la deuxième invite : `Enter second number:`. J'ai entré le nombre `3` comme deuxième nombre.

Ensuite, la fonction `add()` est appelée, qui additionne les nombres `2` et `3`.

Enfin, la ligne `The sum of 2 and 3 is 5` est imprimée sur la console.

## Conclusion

Dans cet article, vous avez appris les bases de la définition des fonctions en C.

Plus précisément, vous avez appris les deux différents types de fonctions en C, et la syntaxe générale pour définir vos propres fonctions.

Enfin, vous avez vu un exemple de fonction simple qui additionne deux nombres et retourne le résultat.

Merci d'avoir lu, et bon codage !