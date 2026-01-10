---
title: C++ Vector – How to Initialize a Vector in a Constructor in C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-27T20:08:33.000Z'
originalURL: https://freecodecamp.org/news/cpp-vector-how-to-initialize-a-vector-in-a-constructor
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/uday-awal-UjJWhMerJx0-unsplash--2-.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "When you're working with a collection of variables or data in programming,\
  \ you usually store them in specific data types. \nIn C++, you can store them in\
  \ arrays, structures, vectors, strings and so on. While these data structures have\
  \ their distinctiv..."
---

When you're working with a collection of variables or data in programming, you usually store them in specific data types. 

In C++, you can store them in arrays, structures, vectors, strings and so on. While these data structures have their distinctive features, we'll focus mainly on the various methods of initializing vectors.

Before that, let's talk briefly about vectors and what makes them stand out when dealing with data collections in C++.

## What are Vectors in C++?

Unlike arrays in C++ where the memory allocated to the collection is static, vectors let us create more dynamic data structures. 

Here's an array in C++:

```c++
#include <iostream>
using namespace std;

int main() {
    string names[2] = {"Jane", "John"};
    cout << names[1];
    // John
}
```

The array in the code above was created and allocated space enough to contain only two items. Attempting to assign new values through a new index would throw an error our way.

With vectors, things are a bit different. We don't have to specify the vector's capacity when it's defined. Under the hood, the vector's allocated memory changes as the size of the vector changes.

## Syntax for Vectors in C++

Declaring a `vector` is different from initializing it. Declaring a `vector` means creating a new `vector` while initializations involves passing items into the `vector`. 

Here's what the syntax looks like:

```txt
vector <data_type> vector_name
```

Every new `vector` must be declared starting with the **vector** keyword. This is followed by angle brackets which contain the the type of data the vector can accept like strings, integers, and so on. Lastly, the vector name - we can call this whatever we want. 

Note that you must put `include <vector>` at the top of your file to be able to use vectors.

## How to Initialize a Vector in C++

In this section, we'll go over the different ways of initializing a `vector` in C++. We'll divide them into sub-sections with some examples for each sub-section.

Let's start with the most basic. 

### How to Initialize a Vector in C++ Using the `push_back()` Method

`push_back()` is one out of the many methods you can use to interact with vectors in C++. It takes in the new item to be passed in as a parameter. This allows us to push new items to the last index of a `vector`. 

Here's an example:

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> myVector;

	myVector.push_back(5);
	myVector.push_back(10);
	myVector.push_back(15);

	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

In the code above, we created an empty `vector`: `vector<int> myVector;`. 

Using the `push_back()`, we passed in three new numbers to the `vector`. 

We the looped through these new numbers and logged them out to the console. 

### How to Initialize a Vector When Declaring the Vector in C++

Just like arrays, we can assign values to a vector when it is being declared. 

Here's an example:

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> myVector{ 5, 10, 15 };

	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

In this example, both declaration and initialization were done at the same time. 

At the point of declaring the `vector`, we passed in three numbers and then looped through and printed them out. 

You'll notice that I put `int` between the angle brackets. This is to show that the data the `vector` will hold is specifically integers. 

### How to Initialize a Vector From an Array in C++

In this section, we'll first create and initialize an array. Then we'll copy all the items in the array into our vector using two vector methods – `begin()` and `end()`.

Let's see how that works. 

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int myArray[] = { 5, 10, 15 };
    
    vector<int> myVector(begin(myArray), end(myArray));


	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

We can also initialize a `vector` from another vector using the same methods above. You'll have to define the first `vector` then use the `begin()` and `end()` methods to copy its values into the second `vector`.

### How to Initialize a Vector by Specifying the Size and Value in C++

We can specify the size and items of a `vector` during its declaration. This is mainly in situations where the `vector` is required to have a specific value all through. 

Here's an example:

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {

  int num_of_items = 5; 
  
  vector<int> myVector(num_of_items, 2); 
  
  	for (int x : myVector)
		cout << x << " ";
// 		2 2 2 2 2 
}
```

In the code above, we first defined a variable and passed a value of 5 to it. This acts as the maximum number of values the `vector` will have. 

We then declared our `vector`: `vector myVector(num_of_items, 2);`. The first parameter is the maximum number of items variable while the second parameter is the actual item to be stored in the `vector`.

We looped through and logged out the items in the `vector`. We got 2 printed five times. 

### How to Initialize a Vector Using a Constructor in C++

We can also initialize vectors in constructors. We can make the values to be a bit dynamic. This way, we don't have to hardcode the vector's items. 

Here's an example:

```c++
#include <iostream>
#include <vector>
using namespace std;

class Vector {
	vector<int> myVec;

public:
	Vector(vector<int> newVector) {
	    myVec = newVector;
	}
	
	void print() {
		for (int i = 0; i < myVec.size(); i++)
			cout << myVec[i] << " ";
	}
	
};

int main() {
    vector<int> vec;
    
	vec.push_back(5);
	vec.push_back(10);
	vec.push_back(15);
	
	Vector vect(vec);
	vect.print();
	// 5 10 15 
}

```

Let's break the code down. 

```c++
class Vector {
	vector<int> myVec;

public:
	Vector(vector<int> newVector) {
	    myVec = newVector;
	}
	
	void print() {
		for (int i = 0; i < myVec.size(); i++)
			cout << myVec[i] << " ";
	}
	
};
```

We created a class called **Vector**. Then we created a vector variable called `myVec`. 

After that, we defined our constructor. The constructor has two methods – one that takes in an initialized `vector` and another that prints out the items in the `vector`. 

```c++
int main() {
    vector<int> vec;
    
	vec.push_back(5);
	vec.push_back(10);
	vec.push_back(15);
	
	Vector vect(vec);
	vect.print();
	// 5 10 15 
}
```

Lastly, as you can see in the code above, we created a new `vector` and pushed in new items to it. We then went on to log these items to the console.

The logic in `main` was created in the **Vector** class which also has a constructor. 

## Conclusion

In this article, we talked about vectors in C++. 

We started by differentiating arrays and vectors. Arrays have a static size while vectors are more dynamic and can expand as items are added. 

We then went over a few methods which we can use to initialize a `vector` in C++ with examples for each section. 

Happy coding!

