---
title: C++ String – Exemple de std::string en C++
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2022-01-31T23:37:41.000Z'
originalURL: https://freecodecamp.org/news/c-string-std-string-example-in-cpp
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/c
seo_title: C++ String – Exemple de std::string en C++
---

string.jpeg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'Les chaînes de caractères sont des composants essentiels dans tout langage de programmation, et le C++ ne fait pas exception.

Que vous souhaitiez stocker du texte, le manipuler, ou accepter des entrées et sorties clavier, comprendre ce que sont les chaînes de caractères et comment les utiliser efficacement est extrêmement i...'
---

Les chaînes de caractères sont des composants essentiels dans tout langage de programmation, et le C++ ne fait pas exception.

Que vous souhaitiez stocker du texte, le manipuler, ou accepter des entrées et sorties clavier, comprendre ce que sont les chaînes de caractères et comment les utiliser efficacement est extrêmement important.

Cet article vous apprendra tout ce que vous devez savoir sur la manipulation et le travail avec les chaînes de caractères en C++.

## Qu'est-ce qu'une chaîne de caractères ?

Les chaînes de caractères, à leur core, sont essentiellement des collections de caractères. Certains exemples incluent "Hello World", "Mon nom est Bob", et ainsi de suite. Elles sont enfermées dans des guillemets doubles `"`.

En C++, nous avons deux types de chaînes de caractères :

1. Les chaînes de style C

2. Les `std::string`s (de la classe string standard de C++)

Vous pouvez très facilement créer votre propre classe de chaîne avec leurs propres petites fonctions, mais ce n'est pas quelque chose que nous allons aborder dans cet article.

# Chaînes de style C

Ce sont des chaînes dérivées du langage de programmation C et elles continuent d'être supportées en C++. Ces "collections de caractères" sont stockées sous la forme de tableaux de type `char` qui sont *null-terminated* (le caractère null `\0`).

#### Comment définir une chaîne de style C :

```c
char str[] = "chaîne c";
```

Ici, `str` est un tableau `char` de longueur `9` (le caractère supplémentaire provient du caractère null `\0` qui est ajouté par le compilateur).

Voici quelques autres façons de définir des chaînes de style C en C++ :

```c
char str[9] = "chaîne c";
char str[] = {'c', ' ', 'h', 'a', 'î', 'n', 'e', ' ', 'c', '\0'};
char str[9] = {'c', ' ', 'h', 'a', 'î', 'n', 'e', ' ', 'c', '\0'};
```

#### Comment passer des chaînes de style C à une fonction

```c++
#include <iostream>

int main() {
    char str[] = "Ceci est une chaîne de style C";
    afficher(str);
}

// Les chaînes de style C peuvent être passées aux fonctions comme suit :
void afficher(char str[]) {
    std::cout << str << "\n";
}
```

### Comment utiliser les fonctions de chaînes de style C en C++

La bibliothèque standard C est livrée avec quelques fonctions pratiques que vous pouvez utiliser pour manipuler les chaînes. Bien qu'elles ne soient pas largement recommandées à utiliser (voir ci-dessous), vous pouvez toujours les utiliser dans le code C++ en incluant l'en-tête `<cstring>` :

```json
#include <cstring> // requis


1. strcpy(s1,s2) --> Copie la chaîne s2 dans la chaîne s1.                 
2. strcat(s1,s2) --> Concatène la chaîne s2 à la fin de la chaîne s1
3. strlen(s1)    --> Retourne la longueur de la chaîne s1         
4. strcmp(s1,s2) --> Retourne 0 si s1==s2 ; moins que 0 si s1<s2 ; plus grand que 0 si s1>s2
5. strchr(s1,ch) --> Retourne un pointeur vers la première occurrence du caractère ch dans la chaîne s1
6. strstr(s1,s2) --> Retourne un pointeur vers la première chaîne s2 dans la chaîne s1
```

# std::string

Les chaînes de style C sont relativement *non sécurisées* – si la chaîne/tableau de caractères n'est pas terminée par un caractère null, cela peut entraîner une multitude de bugs potentiels.

Par exemple, les [débordements de tampon](https://en.wikipedia.org/wiki/Buffer_overflow) parmi une [multitude d'autres inconvénients](https://stackoverflow.com/questions/312570/what-are-some-of-the-drawbacks-to-using-c-style-strings) sont quelques raisons pour lesquelles l'utilisation des chaînes de style C n'est pas recommandée dans la communauté des développeurs C++.

La classe `std::string` fournie par la bibliothèque standard C++ est une alternative beaucoup plus sûre. Voici comment l'utiliser :

#### Comment définir une `std::string`

```c++
#include <iostream> 
#include <string> // la classe de chaîne standard C++

int main() {
    std::string str = "Chaîne C++";
    std::cout << str << "\n"; // imprime `Chaîne C++`"
}
```

La différence la plus évidente à noter entre les chaînes de style C et les `std::string`s est la *longueur* de la chaîne. Si vous avez besoin de la longueur d'une chaîne de style C, vous devrez la calculer chaque fois en utilisant la fonction `strlen()` comme suit :

```c++
#include <iostream>
#include <cstring> // requis pour utiliser `strlen`

int main() {
    char str[] = "bonjour le monde";
    std::cout << strlen(str) << "\n";
}
```

Si vous ne stockez pas cela dans une variable et que vous en avez besoin dans plusieurs parties de votre programme, vous pouvez rapidement observer à quel point cette option est coûteuse.

D'autre part, une chaîne `std::string` a déjà une propriété de longueur intégrée. Pour y accéder, vous utilisez la propriété `.length()` comme suit :

```c++
#include <iostream>
#include <string> // requis pour utiliser `std::string`

int main() {
    std::string str = "freeCodeCamp";
    std::cout << str.length() << "\n";
}
```

Simple, net, concis, mais une réduction computationnelle importante.

Mais l'accès à la propriété *length* n'est pas le seul avantage à utiliser les `std::string`s. Voici quelques exemples supplémentaires :

```c++
#include <iostream>
#include <string>

int main() {
   std::string str = "freeCodeCamp";
   
   // Insérer un seul caractère dans `str`
   str.push_back('s');
   std::cout << str << "\n"; // `str` est maintenant `freeCodeCamps`
   
   // Supprimer le dernier caractère de `str`
   str.pop_back();
   std::cout << str << "\n"; // `str` est maintenant `freeCodeCamp`
   
   // Redimensionner une chaîne
   str.resize(13);
   std::cout << str << "\n"; 
   
   // Réduire la capacité excédentaire de la chaîne
   str.shrink_to_fit()
   std::cout << str << "\n";
}
```

#### Comment passer une `std::string` à une fonction

```c++
#include <iostream>

int main() {
    std::string str = "Ceci est une chaîne de style C";
    afficher(str);
}

// Passer des `std::string`s comme vous le feriez normalement pour un objet régulier
void afficher(std::string str) {
    std::cout << str << "\n";
}
```

## Quand utiliseriez-vous une chaîne de style C plutôt qu'une `std::string` ?

À ce stade, vous devriez être convaincu des nombreux avantages que les `std::string`s ont sur les chaînes de style C (notamment la gestion automatique de la mémoire). Mais il y a des moments où vous voudrez utiliser des chaînes de style C à la place :

1. Si vous venez d'un milieu C, vous pourriez être à l'aise de travailler avec des chaînes de style C.

2. Une `std::string`, malgré ses avantages, est énormément complexe. Comme le reste du langage, si vous ne savez pas ce que vous faites, cela peut devenir très compliqué très rapidement. De plus, elle utilise une tonne de mémoire qui peut ne pas être idéale pour les besoins de vos programmes.

3. Si vous êtes prudent pour gérer la mémoire de votre programme pendant l'exécution (en libérant la mémoire d'un objet lorsque vous avez terminé de l'utiliser), il y a un avantage de performance à utiliser des chaînes de style C étant donné leur petite taille et leur légèreté.

# Conclusion

J'espère que cet article a servi d'introduction aux chaînes de caractères en C++. Il y a *tellement plus* à apprendre sur cette merveilleuse abstraction, et j'espère écrire plus d'articles approfondissant les concepts plus avancés des chaînes de caractères et du C++.

Bonne apprentissage !