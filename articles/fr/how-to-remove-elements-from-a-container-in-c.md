---
title: Comment supprimer des éléments d'un conteneur en C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:04:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-elements-from-a-container-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1d740569d1a4ca3b68.jpg
tags:
- name: c programming
  slug: c-programming
- name: interview questions
  slug: interview-questions
seo_title: Comment supprimer des éléments d'un conteneur en C++
seo_desc: "How to remove elements from container is a common C++ interview question,\
  \ so you can earn some brownie points if you read this page carefully. \nThe erase–remove\
  \ idiom is a C++ technique to eliminate elements that fulfill a certain criterion\
  \ from a co..."
---

Comment supprimer des éléments d'un conteneur est une question courante lors des entretiens en C++, donc vous pouvez gagner quelques points si vous lisez cette page attentivement. 

L'idiome erase-remove est une technique C++ pour éliminer les éléments qui remplissent un certain critère d'un conteneur. Cependant, il est possible d'éliminer des éléments avec une boucle écrite à la main traditionnelle, mais l'idiome erase-remove présente plusieurs avantages.

### **Comparaison**

```cpp
// Utilisation d'une boucle écrite à la main
std::vector<int> v = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
for (auto iter = v.cbegin(); iter < v.cend(); /*iter++*/)
{
    if (is_odd(*iter))
    {
        iter = v.erase(iter);
    }
    else
    {
        ++iter;
    }
}

// Utilisation de l'idiome erase-remove
std::vector<int> v = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
v.erase(std::remove_if(v.begin(), v.end(), is_odd), v.end());
```

Comme vous pouvez le voir, le code avec la boucle écrite à la main nécessite un peu plus de frappe, mais il a aussi un problème de performance. Chaque appel à `erase` doit déplacer vers l'avant tous les éléments après celui supprimé, pour éviter les "trous" dans la collection. Appeler `erase` plusieurs fois sur le même conteneur génère beaucoup de surcharge de déplacement des éléments.

D'autre part, le code avec l'idiome erase-remove n'est pas seulement plus expressif, mais il est aussi plus efficace. Tout d'abord, vous utilisez `remove_if/remove` pour déplacer tous les éléments qui ne correspondent pas aux critères de suppression vers l'avant de la plage, en conservant l'ordre relatif des éléments. Ainsi, après avoir appelé `remove_if/remove`, un seul appel à `erase` supprime tous les éléments restants à la fin de la plage.

### **Exemple**

```cpp
#include <vector> // le conteneur vectoriel à usage général
#include <iostream> // cout
#include <algorithm> // remove et remove_if

bool is_odd(int i)
{
    return (i % 2) != 0;
}

void print(const std::vector<int> &vec)
{
    for (const auto& i : vec)
        std::cout << i << ' ';
    std::cout << std::endl;
}

int main()
{
    // initialise un vecteur qui contient les nombres de 1 à 10.
    std::vector<int> v = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    print(v);

    // supprime tous les éléments avec la valeur 5
    v.erase(std::remove(v.begin(), v.end(), 5), v.end());
    print(v);

    // supprime tous les nombres impairs
    v.erase(std::remove_if(v.begin(), v.end(), is_odd), v.end());
    print(v);

    // supprime les multiples de 4 en utilisant une lambda
    v.erase(std::remove_if(v.begin(), v.end(), [](int n) { return (n % 4) == 0; }), v.end());
    print(v);

    return 0;
}

/*
Sortie:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 6 7 8 9 10
2 4 6 8 10
2 6 10
*/
```

### **Sources**

"Erase-remove idiom" Wikipedia: The Free Encyclopedia. Wikimedia Foundation, Inc. [en.wikipedia.org/wiki/Erase-remove_idiom](https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom)

Meyers, Scott (2001). Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library. Addison-Wesley.