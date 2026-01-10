---
title: A behind the scenes look at Map, Filter, and Reduce in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:35:14.000Z'
originalURL: https://freecodecamp.org/news/a-behind-the-scenes-look-at-map-filter-and-reduce-in-swift-1991f5c7bc80
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nRIbaovXFpRyPpFeHBTFLA.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Boudhayan Biswas

  A function takes some input, does something to it and creates an output. A function
  has a signature and a body. If you give the same input to a function then you always
  get the same output. That is in short a definition for the fu...'
---

By Boudhayan Biswas

A function takes some input, does something to it and creates an output. A function has a signature and a body. If you give the same input to a function then you always get the same output. That is in short a definition for the **_function_**.

Now we will talk more about functions by getting a closer look into them. We will explore higher order functions in Swift. A function that takes another function as input or returns a function is called a higher order function.

In Swift, we play with **map, filter, reduce** everyday. When we use these functions, it seems like magic. At this point, you might not have an idea of what is going on behind the scenes. Map, Filter, and Reduce work through the ideas and approaches of functional programming. Even though Swift is not a pure functional language, it allows you to do functional things.

Now let’s look one by one what is happening in background for them. First we will implement the basic versions of these functions for some particular data types, then we will try to implement a generic version.

#### Map Function

Let’s say we have an array of integers and we need to write a function which returns a new array after adding some delta value to each element of the original array. We can easily write a function for this using a simple for loop like below:

Now we need another function which returns a new array by doubling each element of the original array. For this, we can implement it like below:

If we look at the above two functions, we can find that they are basically doing the same thing. Only the functionality inside the for loop is different. They both take an _Integer_ array as input, transform each element by using a for loop, and return a new array. So basically the main thing is to transform each element to something new.

Since Swift supports higher-order functions, we can write a function which will take an array of integers, transform the function as input, and return a new array by applying the transform function to each element of the original array.

But still, there is a problem with the above: it only returns an integer array. If we have a requirement to convert the input integer array to a string array, for example, then we can not do that with this function. To do that, we need to write a generic function that works for any type.

We can implement a generic function in an Array extension like this:

1. Declare a map function in the Array Extension which works with a generic type **T**.
2. The function takes a function of type **(Element) ->_;_** T as input
3. Declare an empty result array which holds **T** type’s data inside the function.
4. Implement a for loop iterating itself and call the transform function to convert the element to type **T**
5. Append the converted value in the resulting array

This is how the **map** function works in Swift. If we need to implement the **map** function_,_ then we would implement it like above. So basically, it does not make any magic happen in an array — we could have easily defined the function by ourselves.

#### Filter Function

Suppose we have an array of integers and we want to keep only the even numbers in the array. We can implement this by using a simple for loop:

Now again, say we have an array of strings representing class file names of a project and we want to keep only the **_._swift** files. This can be also done with a single loop like below:

If we closely look into the implementation of the above two functions, then we can understand that they basically do the same thing — only the data type is different for the two arrays. We can generalise this by implementing a generic filter function, which takes an array and a function as input, and depending upon the output of the **includeElement** function, it decides whether to add the element in the resulting array.

#### Reduce Function

Suppose we have an array of integers and we want to implement two functions which return the sum and the product of the elements. We can implement this by using a simple for loop:

Now instead of having an array of integers, say we have an array of strings and we want to concatenate all the elements in the array:

All three functions basically do the same thing. They take an array as input, initialise a resulting variable, iterate over the array, and update the resulting variable.

From here we can implement a generic function that should work for all. To do this we need the initial value of the resulting variable and the function to update that variable in every iteration.

So we can implement the generic function with the following definition:

The above implementation is generic for any input array of type **[Element].** It will compute a result of type **T**. To work, it needs an initial value of type **T** to assign to a resulting variable. Then, it needs a function of type **(T, Element) ->** T which will be used inside the for loop in each iteration to update the resulting variable.

#### Thank you for reading!

