---
title: Comment convertir un Int en String en C++ - Tutoriel de conversion d'entier
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-10T18:54:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-an-int-to-a-string-in-cpp
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/uday-awal-UjJWhMerJx0-unsplash.jpg
tags:
- name: C++
  slug: c-2
seo_title: Comment convertir un Int en String en C++ - Tutoriel de conversion d'entier
seo_desc: "Type casting or type conversion is the process of converting a variable\
  \ from one data type to another. \nType casting can be done implicitly or explicitly.\
  \ \nImplicit type casting gets done automatically via the compiler, while explicit\
  \ type casting is..."
---

Le transtypage ou la conversion de type est le processus de conversion d'une variable d'un type de données à un autre.

Le transtypage peut être fait implicitement ou explicitement.

Le transtypage implicite est effectué automatiquement via le compilateur, tandis que le transtypage explicite est effectué par le développeur.

Dans cet article, vous apprendrez comment convertir un entier en chaîne de caractères en C++ en utilisant la classe `stringstream` et la méthode `to_string()`.

## Comment convertir un Int en String en C++ en utilisant la classe `stringstream`

En utilisant la classe `stringstream`, nous pouvons convertir un entier en chaîne de caractères.

Voici un exemple pour vous aider à comprendre pourquoi vous auriez besoin de convertir un entier en chaîne de caractères :

```c++
#include <iostream>
using namespace std;

int main() {

    int age = 20;

    cout << "The user is " + age + " years old";
    // erreur : opérandes invalides de types 'const char*' et 'const char [11]' pour l'opérateur binaire '+'

    return 0; 

}

```

Dans l'exemple ci-dessus, nous avons créé une variable `int` avec une valeur de 20.

Lorsque nous avons essayé de concaténer cette valeur dans une chaîne de caractères, nous avons obtenu une erreur disant "opérandes invalides de types... ".

L'erreur a été soulevée parce que nous avons essayé d'effectuer une opération en utilisant deux types de variables incompatibles. La solution serait de convertir une variable et de la rendre compatible avec l'autre.

La classe `stringstream` possède des opérateurs d'insertion (`<<`) et d'extraction (`>>`).

L'opérateur d'insertion est utilisé pour passer une variable au flux. Dans notre cas, pour passer un entier au flux.

L'opérateur d'extraction est utilisé pour sortir la variable modifiée.

En d'autres termes, un objet `stringstream` prendrait un type de données, le convertirait en un autre type de données et assignerait le nouveau type de données à une variable.

Voici un exemple :

```c++
#include <iostream>
#include <sstream>  
using namespace std;

int main() {

    int age = 20;
    
    // objet stringstream
    stringstream stream;
    
    // insertion de la variable entière dans le flux
    stream << age;
    
    // variable pour contenir la nouvelle variable du flux
    string age_as_string;
    
    // extraction du type chaîne de caractères de la variable entière
    stream >> age_as_string;
    
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old

    return 0; 

}

```

Dans le code ci-dessus, nous avons créé un objet `stringstream` appelé `stream`. Notez que vous devez inclure la classe stringstream avant de pouvoir l'utiliser : `include <sstream>`.

Nous avons ensuite inséré l'entier dans le flux : `stream << age;`.

Après cela, nous avons créé une nouvelle variable appelée `age_as_string`. Cette variable stockera la variable de chaîne de caractères qui sera extraite du flux.

Enfin, nous avons extrait le type chaîne de caractères de l'entier et l'avons stocké dans la variable créée ci-dessus : `stream >> age_as_string;`.

Maintenant, nous pouvons concaténer les chaînes de caractères et obtenir le résultat souhaité :

```c++
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old
```

## Comment convertir un Int en String en C++ en utilisant la méthode `to_string()`

Vous pouvez utiliser la [méthode to_string()](https://www.freecodecamp.org/news/int-to-string-in-cpp-how-to-convert-an-integer-with-tostring/) pour convertir les types de données int, float et double en chaînes de caractères.

Voici un exemple :

```c++
#include <iostream>
using namespace std;

int main() {

    int age = 20;
    
    string age_as_string = to_string(age);
    
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old

    return 0; 

}

```

Dans le code ci-dessus, nous avons passé la variable `age` à `to_string()` : `string age_as_string = to_string(age);`.

Cela a converti la variable `age` en une chaîne de caractères. Tout comme l'exemple dans la section précédente, nous pouvons maintenant utiliser la variable comme une chaîne de caractères :

```c++
cout << "The user is " + age_as_string + " years old";
// The user is 20 years old
```

## Résumé

Dans cet article, nous avons parlé des différentes façons de convertir un entier en chaîne de caractères en C++.

Les exemples ont montré comment utiliser la classe `stringstream` et la méthode `to_string()` pour convertir un entier en chaîne de caractères.

Bon codage !