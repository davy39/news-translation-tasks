---
title: C++ Map Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/c-plus-plus-map-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d26740569d1a4ca3630.jpg
tags:
- name: C++
  slug: c-2
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: C++ Map Expliqué avec des Exemples
seo_desc: 'map is a container that stores elements in key-value pairs. It''s similar
  to collections in Java, associative arrays in PHP, or objects in JavaScript.

  Here are the main benefits of using map:


  map only stores unique keys, and the keys themselves are i...'
---

`map` est un conteneur qui stocke des éléments sous forme de paires clé-valeur. Il est similaire aux collections en Java, aux tableaux associatifs en PHP ou aux objets en JavaScript.

Voici les principaux avantages de l'utilisation de `map` :

* `map` ne stocke que des clés uniques, et les clés elles-mêmes sont triées
* Comme les clés sont déjà triées, la recherche d'un élément est très rapide
* Il n'y a qu'une seule valeur pour chaque clé

Voici un exemple :

```c++
#include <iostream>
#include <map>

using namespace std;

int main (){
  map<char,int> first;
  
  //initialisation
  first['a']=10;
  first['b']=20;
  first['c']=30;
  first['d']=40;
  
   map<char, int>::iterator it;
   for(it=first.begin(); it!=first.end(); ++it){
      cout << it->first << " => " << it->second << '\n';
   }
   
  return 0;
}
```

Sortie :

```text
a => 10
b => 20
c => 30
d => 40
```

### Créer un objet `map`

`map<string, int> myMap;`

### Insertion

Insertion de données avec la fonction membre insert.

```c++
myMap.insert(make_pair("earth", 1));
myMap.insert(make_pair("moon", 2));
```

Nous pouvons également insérer des données dans std::map en utilisant l'opérateur [] c'est-à-dire

`myMap["sun"] = 3;`

### Accéder aux éléments de `map`

Pour accéder aux éléments de map, vous devez créer un itérateur pour cela. Voici un exemple comme indiqué précédemment.

```c++
map<char, int>::iterator it;
for(it=first.begin(); it!=first.end(); ++it){
  cout << it->first << " => " << it->second << '\n';
}
```