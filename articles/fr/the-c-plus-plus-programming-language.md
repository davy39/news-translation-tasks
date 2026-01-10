---
title: Le langage de programmation C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-12T00:28:00.000Z'
originalURL: https://freecodecamp.org/news/the-c-plus-plus-programming-language
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec1740569d1a4ca3ee9.jpg
tags:
- name: C++
  slug: c-2
- name: General Programming
  slug: programming
seo_title: Le langage de programmation C++
seo_desc: 'C++ is a general purpose programming language which was first developed
  in the 1980s. The language was designed by Bjarne Stroustrup under with the name
  “C with classes”.

  C++ is a version of C that includes Object-Oriented elements, including classes...'
---

C++ est un langage de programmation généraliste qui a été développé pour la première fois dans les années 1980. Le langage a été conçu par Bjarne Stroustrup sous le nom de « C avec classes ».

C++ est une version de C qui inclut des éléments orientés objet, notamment des classes et des fonctions.

Il est considéré comme l'un des langages de programmation les plus largement utilisés, comme vous pouvez le voir dans l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-209.png)

![Img](http://static1.businessinsider.com/image/59deb30392406c21008b6148-1200/for-bonus-points-heres-the-chart-showing-these-languages-relative-popularity.jpg)
_Source : GitHub_

## Hello World en C++

```cpp
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello World" << endl;
    return 0;
}
```

Et la sortie de ce programme sera :

```text
Hello World!
```

Maintenant, décomposons le code.

### Lignes 1 et 2

```cpp
#include <iostream>
using namespace std;
```

La première ligne indique à l'ordinateur d'utiliser le fichier d'en-tête `iostream` pour ce programme spécifique. Un fichier d'en-tête est un fichier séparé avec du code C++ préécrit.

Il existe de nombreux autres fichiers d'en-tête qui sont nécessaires pour qu'un programme spécifique s'exécute correctement. Certains d'entre eux sont `math`, `vector` et `string`. Les fichiers d'en-tête sont généralement représentés par une extension `.h` (vous n'avez pas besoin d'ajouter `.h` lors de l'inclusion de fichiers de la bibliothèque standard C++).

`iostream` signifie « input-output stream ». Le fichier `iostream` contient du code permettant à l'ordinateur de prendre des entrées et de générer une sortie, en utilisant le langage C++.

La deuxième ligne, `using namespace std;`, indique à l'ordinateur d'utiliser l'espace de noms standard qui inclut les fonctionnalités du C++ standard.

Vous pourriez écrire ce programme sans cette ligne, mais vous devriez utiliser `std::cout` au lieu de `cout` et `std::endl` au lieu de `endl` à la ligne 4. Mais la deuxième ligne rend le code plus lisible et notre vie de programmeurs plus facile.

### Lignes 3 et 4

```cpp
int main()
{
```

C++ commence l'exécution d'un programme à partir de la fonction globale `main()`, qui est déclarée avec `int main()`. Pendant l'exécution, l'ordinateur commence à exécuter le code à partir de chaque ligne de l'accolade ouvrante, `{`, à l'accolade fermante, `}`.

Note : Chaque fonction commence par `{` et se termine par `}`.

La ligne 4 indique le début de la fonction `main()` avec l'accolade ouvrante.

### Lignes 5, 6 et 7

```cpp
    cout << "Hello World" << endl;
    return 0;
}
```

`cout` signifie « character output », et est un objet pour afficher la sortie à l'écran.

`cout` est suivi de `<<`, qui est un opérateur d'insertion. Les opérateurs d'insertion envoient des données aux opérateurs de flux qui les précèdent.

Ensuite, vient la phrase `Hello World` entourée de guillemets doubles (`"`). Tout ce qui se trouve entre des guillemets doubles est une chaîne de caractères. Il s'agit d'une chaîne de caractères simple avec des caractères standard, mais certains caractères spéciaux ont une syntaxe différente pour les instructions d'impression.

Ainsi, l'opérateur d'insertion, `<<`, passe la chaîne `"Hello World"` à l'objet `cout`.

Mais si vous regardez la fin de la ligne, il y a un autre opérateur d'insertion et `endl`.

`endl` est un mot réservé dans le langage C++, et signifie « end line ». En C++, vous pouvez utiliser l'objet `endl` pour terminer la ligne actuelle, vider le flux et passer à la ligne suivante dans la sortie.

Enfin, la ligne se termine par un point-virgule, `;`.

Ainsi, en regardant la ligne 5, à la fois la chaîne `"Hello World"` et `endl` sont passés à `cout` avec des opérateurs d'insertion, et la ligne se termine par un point-virgule.

À la ligne 6, `return 0;` termine en toute sécurité la fonction actuelle, `main()`. Et comme il n'y a pas de fonction après `main()`, l'ensemble du programme est terminé.

Enfin, à la ligne 7, la fonction `main()` se termine par une accolade fermante, `}`. Si vous ne terminez pas une fonction par une accolade fermante, vous rencontrerez une erreur d'exécution.

## Révision

Encore une fois, votre code devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/cpp-hello-world-review.jpg)

Félicitations ! Vous avez écrit votre premier programme en C++, et vous avez fait vos premiers pas pour apprendre le C++.

Pour compiler et exécuter votre programme C++, consultez ces tutoriels :

* [C++ Compiler Explained: What is the Compiler and How Do You Use it?](https://www.freecodecamp.org/news/c-compiler-explained-what-is-the-compiler-and-how-do-you-use-it/)
* [How to compile your C++ code in Visual Studio Code](https://www.freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code/)