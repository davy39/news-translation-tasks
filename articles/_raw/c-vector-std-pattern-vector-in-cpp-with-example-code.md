---
title: C++ Vector – STD Pattern Vector in CPP with Example Code
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-01T21:27:30.000Z'
originalURL: https://freecodecamp.org/news/c-vector-std-pattern-vector-in-cpp-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/christin-hume-mfB1B1s4sMc-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'Vectors in C++ are a helpful way to store dynamic data. They also help
  you avoid having to deal with the not so flexible arrays that are inherited from
  the C programming language.

  This article is a beginner friendly introduction to vectors. It will s...'
---

Vectors in C++ are a helpful way to store dynamic data. They also help you avoid having to deal with the not so flexible arrays that are inherited from the C programming language.

This article is a beginner friendly introduction to vectors. It will show you some of their basic and essential features to help you get started with your learning.


## What is a Vector in C++?

Programs need groups of data in order for them to do just about anything. 

That data could be a list of books you have read throughout the year, or  payment options for meals at a restaurant, or simply a list of names - the data can be of any kind.

But how do you store those groups of data?

Vectors in C++ are a simple and effective way of storing data and keeping it organized. 

Vectors, or  `std::vector`, are a template class in the STL (Standard Template Library). But what does that mean?

They are a more flexible, refined, and efficient replacement for arrays, which are used in the C programming language (and on which the C++ language is based). 

Unlike arrays in C that have a static, rigid, and fixed size, vectors are sequenced containers that store dynamic collections of data elements. The container's size is not set - instead it grows and shrinks dynamically.


## Why and when to use a Vector in C++

Consider using vectors when you're working with constantly changing data. 

If you find that you add or remove data often, then vectors are the prefered way to handle those dynamic elements, since they are able to resize themselves automatically.

As mentioned earlier, vectors are not fixed-sized, so that makes them ideal to use when you don't know the size of your data beforehand and when your data is not established in advance.

The size of the containers can change, so you don't need to specify their maximum size from the beginning.

## How to create vectors in C++

To create a vector in C++, you first have to include the vector library.

You do this by adding the line `#include <vector>` at the top of your file. This line goes after the line `#include <iostream>` and any other header files you've included in your program.

The `std::vector` is included in the `#include <vector>` library.

The general syntax for creating a vector looks like this:

```
std::vector<data_type> name (items);
```

Let's break it down:

- You start with the `std::vector` keyword.
- `<data_type>` specifies the type of data that the vector will store, and is surrounded by opening and closing angle brackets, `<>`. Some examples of data types that can be stored are: `<string>`s, `<int>`s, `double`s, and `char`s. Note that the  type of the vector cannot be changed once it has been declared. 
- Next is the name you want to give the vector. Defining the data type and giving the vector a name are mandatory steps.
- Optionally, you can specify the number of elements the vector will hold. This will define the size of the vector. It comes in handy when you don't know the specific values of the items that the vector will hold from the beginning, but you do know the size.
- Lastly, don't forget to end the statement with a semicolon,`;`.

For example:

```cpp
#include <iostream>
#include <vector>

int main() {
//without specifying the number of elements

//defines a vector named prices that stores floating point numbers
std::vector<double> prices;
}
```

```cpp
#include <iostream>
#include <vector>

int main() {
//specifying the number of elements

//creates a vector names prices
// it will hold floating point numbers
// the initial size of the vector is set to 10
std::vector<double> prices (10);
}
```

You don't need to prefix the `std::` when you use `using namespace std;` at the top of your file (after the header files), like so:

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
vector<double> prices;
}
```

## How to find the size of vectors in C++

The `.size()` function will return the number of elements contained in a vector.

You saw earlier on how to create a vector, which was empty.

To double check, you would do:

```cpp
#include <iostream>
#include <vector>

int main() {
std::vector<double> prices;

//returns the size
std::cout << prices.size() << std::endl;

//prints 0
}
```

## How to add items to vectors in C++

Vectors are dynamic containers of elements and their size can grow throughout the life of a program, depending on its needs.

To add items one at a time to the **end** of a vector, you use the `.push_back()` method. 

The element you want to add goes inside the parentheses.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

//add elements to the vector by using .push_back()

names.push_back("Dionysia");
names.push_back("Dimitra");
names.push_back("George");

}
```

## How to delete an item from a vector in C++

Besides adding elements to a vector, you are also able to delete them.

The `.pop_back()` function will delete the **last** item in the vector. 

Compared to the `.push_back()` method which is used for adding elements, the `.pop_back()` function doesn't take any arguments.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

//add elements to the vector by using .push_back()

names.push_back("Dionysia");
names.push_back("Dimitra");
names.push_back("George");

//check the size
std::cout << names.size() << std::endl; //outputs 3

//remove the last element
names.pop_back();

//ckeck the size again
std::cout << names.size() << std::endl; // outputs 2
}
```

## Indexing in Vectors

As mentioned earlier, vectors are containers of sequential items, so this means that each individual item can be accessed by its index.

Indexing in vectors starts from `0` – the first item in a vector has an index of `0`, the second item has an index of `1`, and so on.

You can add items individually by specifying the position you want to add them to.

So, you could rewrite the example from earlier like so:

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

names[0] = "Dionysia"; // adds the string to the 1st place
names[1] = "Dimitra";  // adds the string to the 2nd place
names[2] = "George";   // adds the string to the third place
}
```

To access an element and output each individual item, you mention the name of the vector and the position of the desired element in square brackets.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector<std::string> names;

names[0] = "Dionysia"; 
names[1] = "Dimitra";  
names[2] = "George";   

//print each element to the console:
std::cout << names[0] << std::endl; //prints 'Dionysia'
std::cout << names[1] << std::endl; // prints 'Dimitra'
std::cout << names[2] << std::endl; // prints 'George'
}
```

## Conclusion

And there you have it - you now know the basics of vectors in C++.

If you're interested in learning more about C++, watch the [C++ Tutorial For Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y&t=3457s) on freeCodeCamp's YouTube channel.

Thanks for reading and happy coding :)



