---
title: Extern – Mot-clé Extern en C et C++ pour les Fonctions
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-04-21T00:08:58.000Z'
originalURL: https://freecodecamp.org/news/extern-keyword-function-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Extern
seo_title: Extern – Mot-clé Extern en C et C++ pour les Fonctions
---

C-and-C---Extern-Keyword-Function-Tutorial.png
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "Le mot-clé extern en C et C++ étend la visibilité des variables et\
  \ des fonctions à travers plusieurs fichiers sources. \nDans le cas des fonctions, le mot-clé extern\
  \ est utilisé implicitement. Mais avec les variables, vous devez utiliser le mot-clé explicitement.\n\
  Je crois qu'un ..."
---

Le mot-clé `extern` en C et C++ étend la visibilité des variables et des fonctions à travers plusieurs fichiers sources. 

Dans le cas des fonctions, le mot-clé `extern` est utilisé implicitement. Mais avec les variables, vous devez utiliser le mot-clé explicitement.

Je crois qu'un simple exemple de code peut expliquer les choses mieux dans certains cas qu'un long texte. Je vais donc rapidement configurer un simple programme C++ pour la démonstration. 

Si vous avez GCC installé sur votre système, vous pouvez suivre. Sinon, j'inclurai les sorties de chaque extrait de code pour que vous puissiez les lire.

## `extern` avec les Fonctions

Dans l'exemple, j'ai deux fichiers C++ nommés `main.cpp` et `math.cpp` et un fichier d'en-tête nommé `math.h`. Le code pour le fichier `math.h` est le suivant :

```header
int sum(int a, int b);
```

Comme vous pouvez le voir, le fichier d'en-tête contient la déclaration pour une simple fonction appelée `sum` qui prend deux entiers comme paramètres. Le code pour le fichier `math.cpp` est le suivant :

```cpp
int sum(int a, int b) {
    return a + b;
}
```

Ce fichier contient la définition pour la fonction `sum` précédemment déclarée et elle retourne la somme des paramètres donnés sous forme d'entier.

Enfin, le code pour le fichier `main.cpp` est le suivant :

```cpp
#include <iostream>
#include "math.h"

int main () {
    std::cout << sum(10, 8) << std::endl;
}
```

Ce fichier inclut le fichier d'en-tête `math.h` contenant la déclaration pour la fonction `sum`. Ensuite, à l'intérieur de la fonction `main`, l'instruction `std::cout << sum(10, 8) << std::endl;` appelle la fonction `sum` en passant `10` et `8` comme les deux paramètres et imprime la valeur retournée.

Maintenant, si vous essayez de compiler ce programme, vous verrez qu'il compile sans aucun problème et, lors de l'exécution du fichier binaire résultant, vous verrez la sortie suivante dans la console :

```
18
```

Cela fonctionne (même si la définition de la fonction `sum` est dans un fichier séparé de `main.cpp`) parce que toutes les fonctions en C/C++ sont déclarées comme `extern`. Cela signifie qu'elles peuvent être invoquées depuis n'importe quel fichier source dans le programme entier. 

Vous pouvez déclarer la fonction comme `extern int sum(int a, int b)` mais cela ne causera que de la redondance.

## `extern` avec les Variables

Bien que le mot-clé `extern` soit appliqué implicitement à toutes les fonctions dans un programme C/C++, les variables se comportent un peu différemment. 

Avant de plonger dans l'utilisation de `extern` avec les variables, je voudrais clarifier la différence entre déclarer une variable et la définir.

Déclarer une variable déclare simplement l'existence de la variable au programme. Cela indique au compilateur qu'une variable d'un certain type existe quelque part dans le code. Vous déclarez une variable float comme suit :

```cpp
float pi;
```

À ce stade, la variable n'a aucune mémoire allouée. Le compilateur sait seulement qu'une variable `float` nommée `pi` existe quelque part dans le code.

Définir la variable, en revanche, signifie déclarer l'existence de la variable, ainsi qu'allouer la mémoire nécessaire pour celle-ci. Vous définissez une variable comme suit :

```cpp
float pi = 3.1416;
```

Vous pouvez déclarer une variable autant de fois que vous le souhaitez, mais vous ne pouvez définir une variable qu'une seule fois. Cela est dû au fait que vous ne pouvez pas allouer de mémoire à la même variable plusieurs fois.

Maintenant, je vais modifier le fichier d'en-tête `math.h` créé dans la section précédente pour contenir la déclaration pour la variable `pi` comme suit :

```header
extern float pi;
int sum(int a, int b);
```

Comme vous pouvez le voir, la variable a été déclarée comme `extern` dans le fichier d'en-tête, ce qui signifie qu'elle devrait être accessible n'importe où dans le programme. Ensuite, je vais mettre à jour le fichier `main.cpp` comme suit :

```cpp
#include <iostream>
#include "math.h"

int main () {
    std::cout << pi << std::endl;
    std::cout << sum(10, 8) << std::endl;
}
```

J'ai ajouté une nouvelle instruction `std::cout` pour imprimer la valeur de la variable `pi`. Si vous essayez de compiler ce programme à ce stade, le processus de compilation échouera.

```
Starting build...
C:\mingw64\bin\g++.exe -fdiagnostics-color=always -g C:\Users\shovi\repos\cpp-playground\extern\*.cpp -o C:\Users\shovi\repos\cpp-playground\extern\extern.exe
c:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/11.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:\Users\shovi\AppData\Local\Temp\ccFIWkmh.o:main.cpp:(.rdata$.refptr.pi[.refptr.pi]+0x0): undefined reference to `pi'
collect2.exe: error: ld returned 1 exit status

Build finished with error(s).
```

Cela se produit parce que la déclaration de la variable a permis au compilateur de savoir que cette variable existe quelque part dans le programme – mais en réalité, elle n'existe pas. Elle n'a aucune allocation de mémoire.

Pour résoudre ce problème, je vais définir la variable `pi` à l'intérieur du fichier `math.cpp` comme suit :

```cpp
float pi = 3.1416;

int sum(int a, int b) {
    return a + b;
}
```

Le processus de compilation se termine sans aucun problème, et si j'exécute le binaire résultant, je verrai la sortie suivante dans ma console :

```
3.1416
18
```

Puisque la variable `pi` a été déclarée comme `extern` et a été définie dans le fichier `math.cpp`, le fichier `main.cpp` est capable d'accéder à la valeur de `pi` sans aucun problème.

Vous pouvez définir la variable n'importe où dans le programme, mais j'ai choisi le fichier `math.cpp` pour la définition afin de prouver que cette variable `extern` est effectivement disponible pour tous les autres fichiers sources également.

## Conclusion

Bien qu'il ne soit pas utilisé très souvent, le mot-clé `extern` en C/C++ est sans aucun doute l'un des concepts les plus importants à comprendre. J'espère que vous avez compris comment le mot-clé fonctionne à un niveau basique à partir de cet article.

Alors que vous continuez à utiliser le mot-clé dans vos programmes, vous rencontrerez définitivement des problèmes et des situations qui sont en dehors du cadre de cet article. N'hésitez pas à me contacter sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/) si vous pensez que je peux être utile. Sinon, [Stack Overflow](https://stackoverflow.com/) est toujours là pour aider.

De plus, si vous êtes un locuteur natif bengali, consultez la [Publication Bengali](https://www.freecodecamp.org/bengali/news/) de freeCodeCamp et la [Chaîne YouTube](https://www.youtube.com/channel/UCYl5XjGuTM1gbXUuxH1e0jA). Jusqu'à la prochaine, restez en sécurité et continuez à apprendre.