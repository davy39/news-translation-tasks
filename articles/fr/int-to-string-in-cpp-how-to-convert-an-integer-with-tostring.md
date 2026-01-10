---
title: Int to String en C++ – Comment convertir un entier avec to_string
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-02T21:01:13.000Z'
originalURL: https://freecodecamp.org/news/int-to-string-in-cpp-how-to-convert-an-integer-with-tostring
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/oskar-yildiz-cOkpTiJMGzA-unsplash.jpg
tags:
- name: C++
  slug: c-2
seo_title: Int to String en C++ – Comment convertir un entier avec to_string
seo_desc: "When working with strings in your code, you might want to perform certain\
  \ operations like concatenating (or linking together) two strings. \nBut there are\
  \ cases when you'd rather work with numerical values as though they were strings\
  \ because concatena..."
---

Lorsque vous travaillez avec des chaînes de caractères dans votre code, vous pourriez vouloir effectuer certaines opérations comme la concaténation (ou le lien) de deux chaînes.

Mais il y a des cas où vous préféreriez travailler avec des valeurs numériques comme si elles étaient des chaînes, car la concaténation d'une chaîne et d'un entier vous donnera une erreur.

Dans cet article, nous verrons comment convertir un entier en chaîne en utilisant la méthode `to_string()` en C++.

## Comment convertir un entier avec `to_string()`

Pour utiliser la méthode `to_string()`, nous devons passer l'entier comme paramètre. Voici à quoi ressemble la syntaxe pour vous aider à comprendre :

```txt
to_string(ENTIER)
```

Voyons un exemple.

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    int age = 80;
    
    cout << first_name + " is " + age + " years old";
    
}
```

D'après le code ci-dessus, vous vous attendez à voir "John is 80 years old" dans la console. Mais cela retourne en réalité une erreur car nous essayons de concaténer des chaînes avec un entier.

Corrigeons cela en utilisant la méthode `to_string()`.

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    int age = 80;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    
}
```

Nous avons créé une nouvelle variable appelée `AGE_TO_STRING` qui stocke la valeur de chaîne de la variable `age` à l'aide de la méthode `to_string()`.

Comme vous pouvez le voir dans l'exemple, l'entier `age` a été passé comme paramètre à la méthode `to_string()`, le convertissant en chaîne.

Maintenant, lorsque nous exécutons le code, nous obtenons "John is 80 years old" imprimé dans la console.

La méthode `to_string()` fonctionne également lorsque nous voulons convertir les valeurs des types de données `float` et `double` — utilisés pour stocker des nombres avec des décimales — en chaînes.

Voici quelques exemples pour démontrer cela :

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    float age = 10.5;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    // John is 10.500000 years old
    
}
```

L'exemple ci-dessus montre une valeur `float` convertie en chaîne. Dans la sortie (commentée dans le code ci-dessus), vous pouvez voir la valeur décimale dans la chaîne.

Pour le type de données `double` :

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    double age = 10.5;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    // John is 10.500000 years old
    
}
```

C'est le même résultat que le dernier exemple. La seule différence est que nous utilisons une valeur `double`.

## Conclusion

Dans cet article, nous avons parlé de la conversion d'un entier en chaîne en C++ en utilisant la méthode `to_string()`.

Dans notre exemple, nous avons essayé de concaténer des chaînes et un entier en une seule chaîne plus grande, mais cela nous a donné une erreur.

En utilisant la méthode `to_string()`, nous avons pu convertir des variables avec les types de données `int`, `float` et `double` et les utiliser comme si elles étaient des chaînes.

Bon codage !