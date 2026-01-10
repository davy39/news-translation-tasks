---
title: C++ Map Explained with Examples
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
seo_title: null
seo_desc: 'map is a container that stores elements in key-value pairs. It''s similar
  to collections in Java, associative arrays in PHP, or objects in JavaScript.

  Here are the main benefits of using map:


  map only stores unique keys, and the keys themselves are i...'
---

`map` is a container that stores elements in key-value pairs. It's similar to collections in Java, associative arrays in PHP, or objects in JavaScript.

Here are the main benefits of using `map`:

* `map` only stores unique keys, and the keys themselves are in sorted order
* Because the keys are already in order, searching for an element is very fast
* There is only one value for every key

Here is an example:

```c++
#include <iostream>
#include <map>

using namespace std;

int main (){
  map<char,int> first;
  
  //initializing
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

Output:

```text
a => 10
b => 20
c => 30
d => 40
```

### Creating a `map` object

`map<string, int> myMap;`

### Insertion

Inserting data with insert member function.

```c++
myMap.insert(make_pair("earth", 1));
myMap.insert(make_pair("moon", 2));
```

We can also insert data in std::map using operator [] i.e.

`myMap["sun"] = 3;`

### Accessing `map` elements

To access map elements, you have to create iterator for it. Here is an example as stated before.

```c++
map<char, int>::iterator it;
for(it=first.begin(); it!=first.end(); ++it){
  cout << it->first << " => " << it->second << '\n';
}
```

