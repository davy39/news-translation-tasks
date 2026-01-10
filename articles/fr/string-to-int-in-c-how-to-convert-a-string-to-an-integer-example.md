---
title: String to Int en C++ – Comment convertir une chaîne de caractères en entier
  avec un exemple
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-18T14:54:58.000Z'
originalURL: https://freecodecamp.org/news/string-to-int-in-c-how-to-convert-a-string-to-an-integer-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/nick-hillier-yD5rv8_WzxA-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: C++
  slug: c-2
seo_title: String to Int en C++ – Comment convertir une chaîne de caractères en entier
  avec un exemple
seo_desc: 'When you''re coding in C++, there will often be times when you''ll want
  to convert one data type to a different one.

  In this article you''ll learn how to convert a string to an integer in C++ by seeing
  two of the most popular ways to do so.

  Let''s get st...'
---

Lorsque vous codez en C++, il y aura souvent des moments où vous voudrez convertir un type de données en un autre.

Dans cet article, vous apprendrez comment convertir une chaîne de caractères en un entier en C++ en voyant deux des méthodes les plus populaires pour le faire.

Commençons !

## Types de données en C++

Le langage de programmation C++ dispose de quelques types de données intégrés :

- `int`, pour les nombres entiers (par exemple 10, 150)
- `double`, pour les nombres à virgule flottante (par exemple 5.0, 4.5)
- `char`, pour les caractères simples (par exemple 'D', '!')
- `string`, pour une séquence de caractères (par exemple "Hello")
- `bool`, pour les valeurs booléennes (vrai ou faux)


C++ est un langage de programmation **fortement typé**, ce qui signifie que lorsque vous créez une variable, vous devez déclarer explicitement quel type de valeur y sera stocké.

## Comment déclarer et initialiser des `int` en C++

Pour *déclarer* une variable `int` en C++, vous devez d'abord écrire le type de données de la variable – `int` dans ce cas. Cela permettra au compilateur de savoir quel type de valeurs la variable peut stocker et donc quelles actions elle peut effectuer.

Ensuite, vous devez donner un nom à la variable.

Enfin, n'oubliez pas le point-virgule pour terminer l'instruction !

```cpp
#include <iostream>

int main() {
    int age;
}
```

Vous pouvez ensuite donner une valeur à la variable que vous avez créée, comme ceci :

```cpp
#include <iostream>

int main() {
    int age;
    age = 28;
}
```

Au lieu de faire ces actions en étapes séparées, vous pouvez les combiner en *initialisant* la variable et enfin en imprimant le résultat :

```cpp
// un fichier d'en-tête qui permet l'utilisation de fonctions pour sortir des informations
// par exemple cout ou entrer des informations par exemple cin
#include <iostream> 

// une déclaration de namespace ; vous n'aurez pas à utiliser le préfixe std::
using namespace std;


int main() { // début de la fonction principale du programme
    int age = 28; 
    // initialiser une variable. 
    // Initialiser consiste à fournir le type, le nom et la valeur de la variable en une seule fois.

    // sortie vers la console : "Mon âge est 28", en utilisant l'enchaînement, <<
    cout << "Mon âge est : " << age << endl;
}// fin de la fonction principale
```

## Comment déclarer et initialiser des `string`s en C++

Les chaînes de caractères sont une collection de caractères individuels.

Déclarer des chaînes de caractères en C++ fonctionne très similaire à la déclaration et à l'initialisation des `int`, que vous avez vus dans la section précédente.

La bibliothèque standard C++ fournit une classe `string`. Pour utiliser le type de données string, vous devrez inclure la bibliothèque d'en-tête `<string>` en haut de votre fichier, après `#include <iostream>`.

Après avoir inclus ce fichier d'en-tête, vous pouvez également ajouter `using namespace std;` que vous avez vu précédemment.

Entre autres choses, après avoir ajouté cette ligne, vous n'aurez pas à utiliser `std::string` lors de la création d'une variable de chaîne – juste `string` seul.


```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    //déclarer une variable de chaîne

    string greeting;
    greeting = "Hello";
    //le `=` est l'opérateur d'assignation, assignant la valeur à la variable

}
```

Ou vous pouvez initialiser une variable de chaîne et l'imprimer sur la console :

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    //initialiser une variable de chaîne

    string greeting = "Hello";
   
   //sortie "Hello" vers la console
   cout << greeting << endl;
}
```

## Comment convertir une chaîne de caractères en un entier

Comme mentionné précédemment, C++ est un langage *fortement typé*.

Si vous essayez de donner une valeur qui ne correspond pas au type de données, vous obtiendrez une erreur.

De plus, convertir une chaîne de caractères en un entier n'est pas aussi simple que d'utiliser le transtypage, que vous pouvez utiliser lors de la conversion de `double` en `int`.

Par exemple, vous **ne pouvez pas** faire ceci :

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
   string str = "7";
   int num;

   num = (int) str;
}
```

L'erreur après compilation sera :

```
hellp.cpp:9:10: error: no matching conversion for C-style cast from 'std::__1::string' (aka
      'basic_string<char, char_traits<char>, allocator<char> >') to 'int'
   num = (int) str;
         ^~~~~~~~~
/Library/Developer/CommandLineTools/usr/bin/../include/c++/v1/string:875:5: note: candidate function
    operator __self_view() const _NOEXCEPT { return __self_view(data(), size()); }
    ^
1 error generated.
```

Il existe plusieurs façons de convertir une chaîne en un entier, et vous en verrez deux mentionnées dans les sections suivantes.

### Comment convertir une chaîne en un entier en utilisant la fonction `stoi()`

Une méthode efficace pour convertir un objet chaîne en un entier numérique est d'utiliser la fonction `stoi()`.

Cette méthode est couramment utilisée pour les versions plus récentes de C++, ayant été introduite avec C++11.

Elle prend en entrée une valeur de chaîne et retourne en sortie la version entière de celle-ci.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
   // une variable de chaîne nommée str
   string str = "7";
   // imprimer sur la console
   cout << "Je suis une chaîne " << str << endl;

   // convertir la variable de chaîne str pour avoir une valeur int
   // placer la nouvelle valeur dans une nouvelle variable qui contient des valeurs int, nommée num
   int num = stoi(str);
   
   // imprimer sur la console
   cout << "Je suis un int " << num << endl;
}
```

Sortie :

```
Je suis une chaîne 7
Je suis un int 7
```


### Comment convertir une chaîne en un entier en utilisant la classe `stringstream`

La classe `stringstream` est principalement utilisée dans les versions antérieures de C++. Elle fonctionne en effectuant des entrées et des sorties sur des chaînes.

Pour l'utiliser, vous devez d'abord inclure la bibliothèque `sstream` en haut de votre programme en ajoutant la ligne `#include <sstream>`.

Vous ajoutez ensuite `stringstream` et créez un objet `stringstream`, qui contiendra la valeur de la chaîne que vous souhaitez convertir en un entier et qui sera utilisé lors du processus de conversion en un entier.

Vous utilisez l'opérateur `<<` pour *extraire* la chaîne de la variable de chaîne.

Enfin, vous utilisez l'opérateur `>>` pour *entrer* la valeur entière nouvellement convertie dans la variable entière.

```cpp
#include <iostream>
#include <string>
#include <sstream> // cela vous permettra d'utiliser stringstream dans votre programme

using namespace std;

int main() {
    // créer un objet stringstream, pour entrer/sortir des chaînes
   stringstream ss; 
   
   // une variable nommée str, qui est de type de données string
   string str = "7";
   
   // une variable nommée num, qui est de type de données int
   int num;
   
   
   // extraire la chaîne de la variable str (entrer la chaîne dans le flux)
   ss << str;
   
   // placer la valeur convertie dans la variable int
   ss >> num;
   
   // imprimer sur la console
   cout << num << endl; // imprime la valeur entière 7
}
```

## Conclusion

Et voilà ! Vous avez vu deux méthodes simples pour convertir une chaîne de caractères en un entier en C++.

Si vous cherchez à en apprendre davantage sur le langage de programmation C++, consultez [ce cours de 4 heures](https://www.youtube.com/watch?v=vLnPwxZdW4Y&t=3485s) sur la chaîne YouTube de freeCodeCamp.

Merci d'avoir lu et bon apprentissage 😊