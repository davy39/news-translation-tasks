---
title: Exemple d'opérateurs C++ – &, ou, + Opérateurs en C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-18T15:37:31.000Z'
originalURL: https://freecodecamp.org/news/cpp-operator-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/towfiqu-barbhuiya-5u6bz2tYhX8-unsplash--1-.jpg
tags:
- name: C++
  slug: c-2
seo_title: Exemple d'opérateurs C++ – &, ou, + Opérateurs en C++
seo_desc: "Most programming languages have built-in functionalities that let us carry\
  \ out certain operations like arithmetic, comparison, logical operations, and so\
  \ on. \nIn this article, we'll talk about three operators in C++ – the bitwise AND\
  \ (&) operator, th..."
---

La plupart des langages de programmation ont des fonctionnalités intégrées qui nous permettent d'effectuer certaines opérations comme l'arithmétique, la comparaison, les opérations logiques, et ainsi de suite. 

Dans cet article, nous allons parler de trois opérateurs en C++ – l'opérateur **ET** bit à bit (`&`), l'opérateur **OU** logique (`||`) et l'opérateur arithmétique `+`. 

## Comment utiliser l'opérateur ET bit à bit (`&`) en C++

L'opérateur **ET** bit à bit est représenté par le symbole `&`. 

Voici comment l'opérateur `&` fonctionne en C++ :

* Évalue la valeur binaire de chaque opérande.
* Additionne les valeurs binaires ensemble en utilisant un format de table de vérité ET (nous verrons une application pratique dans les exemples de cette section).
* Retourne la valeur en base 10 de l'addition.

Regardons un exemple tout de suite.

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x & y);
    // 8
}
```

Dans le code ci-dessus, nos opérandes sont 10 et 12, stockés dans `x` et `y` respectivement. Nous avons ensuite utilisé l'opérateur `&` pour évaluer les deux opérandes : `cout << (x & y);` et nous avons obtenu une valeur de 8. 

Cela peut sembler confus, alors décomposons-le.

La valeur binaire de 10 est 1010.

La valeur binaire de 12 est 1100.

Nous allons ensuite additionner les deux valeurs binaires, chaque index correspondant à l'autre. C'est-à-dire, nous additionnons la valeur du premier index dans 1010 qui est 1 et le premier index dans 1100 qui est également 1. Le même principe s'applique aux autres index.

Voici comment :

Pour rappel, voici comment fonctionne la table de vérité **ET** : 1 et 1 => 1, 0 et 1 => 0, 1 et 0 => 1, 0 et 0 => 0. 

Premier index dans 1010 => 1 & premier index dans 1100 => 1

1 et 1 => 1

Deuxième index dans 1010 => 0 & deuxième index dans 1100 => 1

o et 1 => 0

Troisième index dans 1010 => 1 & troisième index dans 1100 => 0

1 et 0 => 0

Quatrième index dans 1010 => 0 & quatrième index dans 1100 => 0

o et 0 => 0

Maintenant nous pouvons obtenir toutes nos sorties : 1000. 

La valeur en base 10 de 1000 est 8. C'est pourquoi l'opération `10 & 12` a retourné 8 dans l'exemple de code.

Vous pouvez également voir l'opération de cette manière :

```txt
    10 = 1010
&
    12 = 1100
        _________
         1000
 
 1000 = 8 en base 10
```

## Comment utiliser l'opérateur OU logique (`||`) en C++

L'opérateur **OU** logique est représenté par le symbole `||`. 

Voici comment l'opérateur `||` fonctionne :

* Évalue deux déclarations.
* Si les deux déclarations sont vraies, retourne 1 (vrai).
* Si les deux déclarations sont fausses, retourne 0 (faux).
* Si l'une des déclarations est vraie, retourne 1 (vrai).

Voici le premier exemple :

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 5 || y < 15);
    // 1
}
```

L'opération ci-dessus retourne 1 parce que les deux déclarations sont vraies – la valeur de `x` est supérieure à 5 et la valeur de `y` est inférieure à 15. 

Regardons un autre exemple.

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 20 || y < 10);
    // 0
}
```

Nous obtenons 0 retourné dans l'exemple parce que les deux déclarations sont fausses – la valeur de `x` n'est pas supérieure à 20 et la valeur de `y` n'est pas inférieure à 10.

Voici un autre exemple :

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 5 || y < 10);
    // 1
}
```

Dans l'exemple ci-dessus, nous avons obtenu 1 retourné parce qu'une des deux déclarations est vraie – la valeur de `x` est supérieure à 5 et la valeur de `y` est inférieure à 10. Donc, l'opérateur `||` vérifie les deux déclarations, si l'une d'elles est vraie, il retourne 1. 

## Comment utiliser l'opérateur arithmétique `+` en C++

L'opérateur `+` est utilisé pour additionner deux ou plusieurs variables/valeurs ensemble.

Voici un exemple :

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x + y);
    // 22
}
```

L'exemple ci-dessus est une simple opération mathématique qui additionne deux nombres et retourne la valeur de l'addition. 

Vous pouvez également effectuer cette opération sans les stocker dans une variable. C'est-à-dire :

```c++
#include <iostream>
using namespace std;
int main() {
    
    cout << (10 + 12);
    // 22
}
```

## Conclusion

Dans cet article, nous avons parlé de trois opérateurs en C++. Ces opérateurs sont l'opérateur **ET** bit à bit (`&`), l'opérateur **OU** logique (`||`) et l'opérateur arithmétique `+`. 

Nous avons vu comment chaque opérateur fonctionne et une partie de la logique derrière leur opération. Chaque section avait un exemple pour nous aider à comprendre les opérateurs et comment ils évaluent leurs opérandes pour nous donner un résultat.

Bon codage !