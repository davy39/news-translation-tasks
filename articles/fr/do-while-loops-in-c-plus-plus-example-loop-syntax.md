---
title: Les boucles Do While en C++ avec exemple de syntaxe de boucle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T21:27:02.000Z'
originalURL: https://freecodecamp.org/news/do-while-loops-in-c-plus-plus-example-loop-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98af740569d1a4ca1b76.jpg
tags:
- name: C++
  slug: c-2
- name: Loops
  slug: loops
seo_title: Les boucles Do While en C++ avec exemple de syntaxe de boucle
seo_desc: "By Patrick Loeber\nLoops are control flow statements that allow code to\
  \ be executed repeatedly based on a given condition. \nThe do while loop is a variant\
  \ of the while loop that executes the code block once before checking the condition.\
  \ Then it will ..."
---

Par Patrick Loeber

Les boucles sont des instructions de contrôle de flux qui permettent d'exécuter du code de manière répétée en fonction d'une condition donnée. 

La boucle `do while` est une variante de la boucle `while` qui exécute le bloc de code une fois avant de vérifier la condition. Ensuite, elle répétera la boucle tant que la condition est vraie.

## Syntaxe

Voici la syntaxe de base pour une boucle do while :

```c++
do {
    // corps de la boucle
}
while (condition);
```

Notez que le test de la condition de terminaison est effectué après chaque exécution de la boucle. Cela signifie que la boucle sera toujours exécutée au moins une fois, même si la condition est fausse au début.

Cela contraste avec la boucle `while` normale, où la condition est testée avant la boucle, et une exécution du bloc de code n'est pas garantie.

Voici maintenant une boucle while normale :

```c++
while (condition) {
    // corps de la boucle
 }
```

## Exemple de boucle do while

Examinons un exemple fonctionnel :

```c++
#include <iostream>
 
int main () {
   
    int number = 1;

    do {
        std::cout << number << std::endl;
        number++;
    }
    while (number < 5);
 
    return 0;
}
```

Sortie :

```
1
2
3
4
```

Dans cet exemple, nous initialisons une variable entière `number = 1`. Nous exécutons ensuite la boucle de manière répétée. 

À l'intérieur de la boucle, nous imprimons la variable et augmentons la variable de un. La boucle est exécutée tant que `number` est inférieur à 5. Par conséquent, les nombres de 1 à 4 sont imprimés.

## Exemple 2

Voici un autre exemple et sa sortie :

```
10
```

```c++
#include <iostream>
 
int main () {
   
    int number = 10;

    do {
        std::cout << number << std::endl;
        number++;
    }
    while (number < 5);
 
    return 0;
}
```

Dans cet exemple, nous utilisons le même code que dans le premier exemple. Mais maintenant, nous initialisons notre variable avec `number = 10`. 

Puisque 10 n'est pas inférieur à 5, notre condition est déjà fausse. La boucle sera tout de même exécutée une fois, et 10 est la seule sortie imprimée.

## Quand devez-vous utiliser la boucle Do While ?

La boucle `do while` est un excellent outil si vous avez besoin d'exécuter du code de manière répétée. Comme indiqué ci-dessus, vous devez utiliser cette syntaxe chaque fois que vous avez besoin d'une boucle, et que vous devez également garantir qu'au moins une exécution du bloc de code est effectuée.

Imaginez un code comme dans l'exemple 2, mais nous n'initialisons pas notre variable avec une valeur codée en dur. Au lieu de cela, nous utilisons une entrée utilisateur. 

Nous ne pouvons pas garantir que l'entrée utilisateur est suffisamment petite, mais nous voulons tout de même voir au moins une instruction d'impression dans la console de sortie. C'est un cas d'utilisation parfait pour la boucle `do while`.

```c++
// Pseudo code où do while est utile :

int number = getUserInput();

do {
    std::cout << number << std::endl;
    number = someUpdateCalculation();
}
while (number < 5);
```