---
title: Double VS Float en C++ – La Différence Entre Floats et Doubles
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-19T22:29:11.000Z'
originalURL: https://freecodecamp.org/news/double-vs-float-in-cpp-the-difference-between-floats-and-doubles
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/nick-hillier-yD5rv8_WzxA-unsplash-1.jpg
tags:
- name: C++
  slug: c-2
seo_title: Double VS Float en C++ – La Différence Entre Floats et Doubles
seo_desc: 'In C++, there are various data types like string, int, char, bool, float,
  and double. Each of these data types have specific values that can be stored in
  them.

  When working with integers, we usually store them in an int data type. But this
  is only us...'
---

En C++, il existe divers types de données comme `string`, `int`, `char`, `bool`, `float` et `double`. Chacun de ces types de données peut stocker des valeurs spécifiques.

Lorsque nous travaillons avec des entiers, nous les stockons généralement dans un type de données `int`. Mais cela n'est utile que pour les nombres entiers.

Lorsque nous voulons stocker des nombres avec des décimales, nous pouvons utiliser soit `float`, soit `double`. Bien que ces deux types de données soient utilisés à des fins similaires, ils présentent certaines différences.

Dans cet article, nous parlerons des différences entre les floats et les doubles en C++ avec quelques exemples.

## Différence Entre Floats et Doubles

Cette section sera divisée en sous-sections, chaque section se concentrant sur une différence entre les floats et les doubles.

### Différence de Taille en Octets

La taille en octets pour `float` est de 4 tandis que la taille en octets pour `double` est de 8.

Cela implique que `double` peut stocker des valeurs qui sont deux fois plus grandes que ce que `float` peut contenir.

Nous pouvons voir cela en utilisant l'opérateur `sizeof()`. Voici un exemple :

```c++
#include <iostream>
using namespace std;
int main() {
    
    cout << "float: " << sizeof(float) << endl; // float: 4
    cout << "double: " << sizeof(double) << endl;// double: 8

}
```

### Différence de Précision (Exactitude)

Lorsque nous travaillons avec des nombres ayant beaucoup de chiffres décimaux, nous espérons généralement que la valeur résultante sera exacte. Mais l'exactitude de notre résultat dépend du nombre de chiffres décimaux avec lesquels nous travaillons.

Ne vous inquiétez pas, nous parlons toujours de C++, pas de mathématiques.

`float` et `double` ont des capacités variables en ce qui concerne le nombre de chiffres décimaux qu'ils peuvent contenir. `float` peut contenir jusqu'à 7 chiffres décimaux avec exactitude tandis que `double` peut en contenir jusqu'à 15.

Voyons quelques exemples pour démontrer cela.

```c++
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double MA_VALEUR_DOUBLE = 5.12345678987;

    float MA_VALEUR_FLOAT = 5.12345678987;
    
    cout << setprecision(7);
    cout << MA_VALEUR_DOUBLE << endl; // 5.123457
    cout << MA_VALEUR_FLOAT << endl; // 5.123457
}
```

Dans l'exemple ci-dessus, nous avons créé des variables `float` et `double` – toutes deux ayant la même valeur : `5.12345678987`.

La fonction `setprecision()` est utilisée pour indiquer au compilateur le nombre de décimales que nous voulons imprimer. Dans notre cas, la valeur est 7.

Nous pouvons observer, à partir des résultats dans le code ci-dessus, que les deux variables ont imprimé des valeurs exactes jusqu'à la 7ème décimale : `5.123457`.

Augmentons le paramètre dans la fonction `setprecision()` à 12 et voyons ce qui se passe.

```c++
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double MA_VALEUR_DOUBLE = 5.12345678987;

    float MA_VALEUR_FLOAT = 5.12345678987;
    
    cout << setprecision(12);
    cout << MA_VALEUR_DOUBLE << endl; // 5.12345678987
    cout << MA_VALEUR_FLOAT << endl; // 5.12345695496
}
```

D'après les résultats ci-dessus, la variable `MA_VALEUR_DOUBLE` a imprimé des valeurs exactes. Mais la variable `MA_VALEUR_FLOAT`, à partir de sa 7ème décimale, a imprimé des valeurs entièrement différentes de la valeur originale qui lui avait été donnée.

Cela nous montre la précision des deux types de données. Tout comme `float`, si nous essayons de retourner une valeur qui dépasse la plage d'exactitude pour le type de données `double`, nous obtiendrons une valeur inexacte.

### Différence d'Utilisation

`float` est principalement utilisé dans les bibliothèques graphiques pour une puissance de traitement élevée en raison de sa petite plage.

`double` est principalement utilisé pour les calculs en programmation afin d'éliminer les erreurs lorsque les valeurs décimales sont arrondies. Bien que `float` puisse encore être utilisé, cela ne devrait être fait que dans les cas où nous traitons avec de petites valeurs décimales. Pour être du bon côté, vous devriez toujours utiliser `double`.

## Conclusion

Dans cet article, nous avons parlé des différences entre les floats et les doubles en C++.

Nous avons parlé de trois différences : la taille en octets, la précision et l'utilisation.

Nous avons également appris que les doubles ont une taille en octets deux fois plus grande que les floats. De plus, les doubles sont plus précis lorsque nous traitons avec de grandes valeurs décimales.

Enfin, nous avons parlé des cas d'utilisation qui nous ont aidé à comprendre quand utiliser chaque type de données.

Bon codage !