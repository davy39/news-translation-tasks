---
title: How to Use Set and Map in JavaScript
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-02-10T15:29:36.000Z'
originalURL: https://freecodecamp.org/news/set-and-map-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/kamaldeenlawal94@gmail.com--1-.jpg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "There are three major iterables available in JavaScript: Arrays, Maps,\
  \ and Sets. \nIn this article, we will cover the following topics: \n\nWhat is an\
  \ Array?\nWhat is a Set?\nWhat is a Map?\nHow to Create a Seta. How to Create a\
  \ Set with a Value\nProperties..."
---

There are three major iterables available in JavaScript: Arrays, Maps, and Sets. 

In this article, we will cover the following topics: 

* [What is an Array?](#heading-what-is-an-array)
* [What is a Set?](#heading-what-is-a-set)
* [What is a Map?](#heading-what-is-a-map)
* [How to Create a Set](#heading-how-to-create-a-set)  
a. [How to Create a Set with a Value](#heading-how-to-create-a-set-with-a-value)
* [Properties and Methods of a Set](#heading-properties-and-methods-of-a-set)  
a. [How to use the `add` method in a set](#heading-how-to-use-the-add-method-in-a-set)  
b. [How to use the `has` method in a set](#heading-how-to-use-the-has-method-in-a-set)  
c. [How to use the `delete` method in a set](#heading-how-to-use-the-delete-method-in-a-set)  
d. [How to use the `clear` method in a set](#heading-how-to-use-the-clear-method-in-a-set)  
e. [How to use the `entries` method in a set](#heading-how-to-use-the-entries-method-in-a-set)  
f. [How to use the `values` method in a set](#heading-how-to-use-the-values-method-in-a-set)  
g. [How to use the `size` property in a set](#heading-how-to-use-the-size-property-in-a-set)  
h. [How to use `forEach` in a set](#heading-how-to-use-foreach-in-a-set)  
i. [How to use a set to Get Unique Value from an Array.](#heading-how-to-use-a-set-to-get-unique-value-from-an-array)
* [How to Create a Map](#heading-how-to-create-a-map)
* [Properties and Methods of Map](#heading-properties-and-methods-of-map)  
a. [How to Get Values from the Map Object](#heading-how-to-get-values-from-the-map-object)  
b. [How to Add Data with the `set` Method](#heading-how-to-add-data-with-the-set-method)  
c. [How to Search an Element with the `has` Method](#heading-how-to-search-an-element-with-the-has-method)  
d. [How to Delete an Element with the `delete` Method](#heading-how-to-delete-an-element-with-the-delete-method)  
e. [How to Clear All Elements with the `clear` Method](#heading-how-to-clear-all-elements-with-the-clear-method)  
f. [How to get all Entries in a Map with the `entries` Method](#heading-how-to-get-all-entries-in-a-map-with-the-entries-method)  
g. [How to Get All Keys in a Map with the `keys` Method](#heading-how-to-get-all-keys-in-a-map-with-the-keys-method)  
h. [How to Get All Values in a Map with the `values` Method](#heading-how-to-get-all-values-in-a-map-with-the-values-method)  
i. [How to Enumerate Over a Map](#heading-how-to-enumerate-over-a-map)  
j. [How to Use Size Property in Map](#heading-how-to-use-size-property-in-map)
* [Map vs Object – What's the Difference?](#heading-map-vs-object-whats-the-difference)
* [Benefits of Sets over Arrays](#heading-benefits-of-sets-over-arrays)
* [Conclusion](#heading-conclusion)

## What is an Array?

An **array** is the most important and most commonly used iterable among the trio. We use it to store lists and connected data of any kind and length. 

Arrays have a lot of special array methods. They also have zero-based indexing for accessing elements. You can have duplicate elements in an array, and the element order is guaranteed.

## What is a Set?

A **set** is a data structure used for storing data of any length and kind. Sets are iterables that have various special methods that are different from arrays. 

Some of the characteristics of sets are that the order of elements is not guaranteed, you can't access elements by index, and you can't have duplicate elements. Sets are a great choice when you want to store data without duplicates.

## What is a Map?

A **map** is another data structure/container used to store key-value pairs of data of any kind and length. 

Maps are similar to objects, but with maps, you can use anything as a key. An object, on the other hand, takes strings, symbols, and numbers as keys. 

Maps are iterables and come with various methods. Some of the features of maps are that the order is guaranteed, and values can be duplicated (but keys can't).

Now we'll learn more about each of these iterables so you understand how to use them.

## How to Create a Set

Since we use sets to create unique values, an ID is a perfect example of something to create with a set. We can create a new set like this:

```javascript
const ids = new Set();
```

To create a set, you start with the `new` keyword along with `set`. In the above code, we created a set of ids which returns an empty set.

```javascript
Set(0) {size: 0}
```

### How to Create a Set with a Value

You initialize the set with an iterable by creating a set with some initial value. An iterable such as an array, set, or nodelist can be passed to the set. The example below shows a set created from an array of 4 elements.

```javascript
const ids = new Set([3,6,9,7]);
console.log(ids);
```

The output will be like this:

```javascript
Set(4) {3,6,9,7}
```

From the result, the code returns a set with 4 elements.

## Properties and Methods of a Set

**Sets** have several methods and a properties that you can use to retrieve, add, delete, check, and clear all the elements in the set. We will talk about all these methods and properties, and how to use them while working with the set.

### How to use the `add` method in a set

We use the `add` method to add elements to the set. Create a set of fruits with 4 elements, it works like this:

```javascript
const fruits = new Set(['apple'.'mango']);
fruits.add('banana');
console.log(fruits)
```

From the above code, banana was added to the set with the help of the add method which gives us this result:

```javascript
Set(3) {'apple'. 'mango', 'banana'}
```

Sets store unique elements, which means that adding another banana to the set won’t be accepted.

### How to use the `has` method in a set

To check if an element is contained in a set, you'll use the `has` method. In the code below, we'll check if a fruit set with various elements contained a specific `banana` element.

```javascript
const fruits = new Set(['apple','mango']);
console.log(fruits.has('banana'));
```

This method will return false, because the element searched for is banana, which is not in the set. If it had been present, we would've gotten true back.

### How to use the `delete` method in a set

You delete an item from a set using the "delete" method. The example below shows the "delete" method being used on a set of fruits containing 3 elements to delete one of the elements.

```javascript
const fruits = new Set(['apple','mango', 'banana']);
fruits.delete('apple');
console.log(fruits);
```

The code prints out a new set of 2 elemets. If you try deleting an element that is not in the set, it ignores it.

```javascript
Set(2) {'mango', 'banana'};
```

### How to use the `clear` method in a set

The clear method is used to clear all the elements in the set. With a set of fruits containing 3 elements, we use the delete method to delete one of the elements.

```javascript
const fruits = new Set(['apple','mango', 'banana']);
fruits.clear('apple');
console.log(fruits);
```

The code prints out a new set of 0 elements, as the clear method will return a set without any elements.

```javascript
Set(0) {size : 0};
```

### How to use the `entries` method in a set

You can retrieve all elements in a set using the "entries" method, which returns an iterable. You can then use a for loop or for-of loop to loop through the values. 

The example below shows the creation of a set of fruits containing 5 elements, followed by the use of the "entries" method to loop through all elements of the array.

```javascript
const fruits = new Set([100,160, 200,400,300]);
for( const fruit of fruits.entries()){
    console.log(fruit);
}
```

It returns an iterable of arrays, each with two elements.

```javascript
(2) {100, 100}
(2) {160, 160}
(2) {200, 200}
(2) {400, 400}
(2) {300, 300}
```

### How to use the `values` method in a set

You retrieve the values in a set by using the "values" method, which returns an iterable. You can then use a for loop or for-of loop to loop through the values. 

The example below shows the creation of a set of fruits with 4 elements and the use of the "values" method to loop through the elements with a for-of loop.

```javascript
const fruits = new Set([100,160, 200,300]);
for( const fruit of fruits.values()){
    console.log(fruit);
}
```

It returns an iterable, each with a single value:

```javascript
100
160
200
300
```

### How to use the `size` property in a set

You use the `size` property to determine the size of the set by returning the number of elements in it. To demonstrate this, we'll create a set of fruits that contains 3 elements.

```javascript
const fruits = new Set(['apple','mango','banana']);
console.log(fruits.size);
```

The above code will return 3 as the size of the fruit set.

```javascript
3
```

### How to use `forEach` in a set

You can easily enumerate a set by using "forEach." The example below shows the creation of a set of fruits with some elements, followed by the use of "forEach" to print each element of the set.

```javascript
const fruits = new Set([100,160, 200,400,300]);
fruits.forEach((fruit) => {
    console.log(fruit)
});
```

The code prints each element of the set like this:

```javascript
100
160
200
400
300

```

### How to use a set to Get Unique Value from an Array.

You can remove duplicate values from an array by using a set. The example below shows the creation of an array of duplicated numbers, followed by passing the array into a set to get all unique numbers, free from duplicates.

```javascript
const numbers = [1,2,4,1,6,8,2,5,9,2,0,9,7,6,3,4,6,7,8,4,2,1,5,8,9,0,2,4,5,3,2,6,8,9,6];

const numbers1 = new Set(numbers);
console.log(numbers1);
```

The above code shows an array of numbers with different duplicated numbers. The array was then passed on to the set of numbers and the output is shown below.

```javascript
Set(10) {1,2,4,6,8,5,9,0,7,3};
```

The code above shows that the set has removed all the duplicated numbers and now has a size of 10.

As you can see, set is a data structure that helps you manage unique values.

## How to Create a Map

You create a map by starting with the "new" keyword followed by "map." The example below shows the creation of a map of a player, which returns an empty map. You can create a new map like this:

```javascript
const player = new Map();
console.log(player);
```

And it returns a map with an empty value.

```javascript
Map(0) {size : 0}
```

You can also create a map using a constructor initialized with an array of arrays. Each array in the array is one key-value pair, and the key can be of any type. The example below shows the creation of a map of two arrays using the constructor.

```javascript
const player = new Map([['key','value'],['lawal','kamal']]);
console.log(player);
```

The above code returns a map with two elements:

```javascript
Map(2) { 'key' => 'value', 'lawal' => 'kamal'}
```

`key` and `lawal` are the keys of the map, while `value` and `kamal` are the values.

## Properties and Methods of Map

**Map** has several methods and properties that we can use to retrieve, add, delete, search, and clear all the elements in the map. 

We will talk about all these methods and properties, and how to use them while working with map.

### How to Get Values from the Map Object

Extracting data from map is easy using the get method. Let's create an object of player1 with name and age properties. Then, the player1 object will be use as key in map. It works like this:

```javascript
const player1 = { name: 'kamal', age: 30};

const playerData = new Map([[player1, [{date:'today',price :400}]]]);
 console.log(playerData);
```

In the above code, you can see that we used the `player1` object as a key in a Map in playerData. By using the get method, you can extract values from the player1 used as a key in the Map.

```javascript
Map(1)
```

It returns a map of size 1. The map contains a key which is the player1 that we created above.

```javascript
key :{ name : 'kamal', age : 30}
```

And it returns a value, which was an array of a single object that contains a date and price.

```javascript
0: {date:'today', price:400}
```

### How to Add Data with the `set` Method

You can add data to the Map after you create it with the help of the set method as shown below:

```javascript
const player = new Map();

player.set('kamal','lawal');

console.log(player);
```

We added the key-value pair `kamal` and `lawal` to an empty map with the set method. The set method is where you set a key-value pair. The key has to be the first option and the value has to be the last. Both the key and values can be of any type of data.

```javascript
Map(1) {'kamal' => 'lawal'}
```

### How to Search an Element with the `has` Method

The `has` method returns true if the map contains keys that match the search term. We can create a map of `player` with two key-value pairs as shown below.

```javascript
const player = new Map([['key','value'],['small','medium']]);

console.log(player.has('small'));
```

The code will print true because the search term (`small`) is present in the map as a key.

```javascript
true

```

But it will print false if the search term (`medium`) is present in the map not as a key but as a value.

```javascript
const player = new Map([['key','value'],['small','medium']]);

console.log(player.has('medium'));

// output will be false, the searched term, (medium) is not a key but value
```

### **How to Delete an Element with the `delete` Method**

We use the delete method to delete a specific element. Delete works if the searched term matches a key in an element. In this case, we're deleting `small`.

```javascript
const player = new Map([['key','value'],['small','medium']]);

player.delete('small');

console.log(player);

```

The code will delete the key-value pair of `small` and `medium`. But, it won't work if the search term is not a key in the map.

```javascript
const player = new Map([['key','value'],['small','medium']]);

player.delete('value');

console.log(player);
// It won't work, because the search term is a value in the map
```

### How to Clear All Elements with the `clear` Method

To clear all elements of a map, we'll use the clear method.

```javascript
const player = new Map([['key','value'],['small','medium']]);
player.clear();

console.log(player);

```

The code will print an empty map as its output.

```javascript
Map(0) { size : 0}
```

### How to get all Entries in a Map with the `entries` Method

The entries method is one of the Map methods you can use with for or for-of loops directly because it returns `MapIterator`. 

#### What is a MapIterator?

A MapIterator is an iterator returned by the `entries()` method of a JavaScript Map object. It returns an array-like object of key-value pairs, with each pair represented as an array containing 2 elements. The `MapIterator` can be used in a `for...of` loop to iterate over all key-value pairs in a Map object.

With `entries`, you can get all the data, both the key and value of a map.

```javascript
const player = new Map([['key','value'],['small','medium'],['fruit','another']]);

console.log(player.entries());
```

The values of all the keys and values will be logged as shown below:

```javascript
MapIterator {'key' => 'value', 'small'=> 'medium', 'fruit' => 'another'}
```

### How to Get All Keys in a Map with the `keys` Method

Aside from the `entries` method, the `keys` method also returns a `MapIterator`. With the keys method, you can get all the keys of a map, and it also runs a for or for-of loop:

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

for(const player of players.keys()){
  console.log(player);
}
```

This will print all the keys in the map as an output, like this:

```javascript
key
small
fruit
```

### How to Get All Values in a Map with the `values` Method

The `values` method is the last map method that returns a `MapIterator` and you can run a for or for-of loop directly on it. This is the method you should use when getting only values in the map is the priority.

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

for(const player of players.values()){
  console.log(player);
}
```

The output of the above code will be this:

```javascript
value
medium
another
```

### How to Enumerate Over a Map

For easy iteration in maps, you can use the popular `forEach` method as shown below:

```javascript
const players = new Map([['key','value'],['small','medium'],['fruit','another']]);

players.forEach((key, value) =>{
  const message = `I want to be remeembered as the best ${key} pair ${value}`;
    console.log(message)
})
```

The above code will print this as the output of the iteration:

```javascript
I want to be remembered as the best value pair key
I want to be remembered as the best medium pair small
I want to be remembered as the best another pair fruit

```

### How to Use Size Property in Map

You can use the property size to determine the size of the map by returning the number of elements in it.

```javascript
const player = new Map([['key', 'value'],['small','medium'],['fruit','another']]);

console.log(player.size);
```

This will print out 3 as the size of the map.

### Map vs Object – What's the Difference?

As you can see, a map is similar to an object which raises the question – when should you use each one?

When to use map:

1. With map, you can use any type (and values) as keys.
2. Map provides better performance for large quantities of data.
3. Use a map for better performance when adding and removing data frequently.

When to use an object:

1. Objects can only use numbers, strings, and symbols as keys.
2. Objects are perfect for small to medium-sized sets of data.
3. Objects have better performance and are easier to create.

### Benefits of Sets over Arrays

Arrays and sets are both data structures used for storing collections of elements. But sets have a slight edge over arrays because of:

* Uniqueness: With a set, duplicates are removed to reduce the size of the data structure (unlike an array which stores duplicates).
* Manipulating collections: It is easy to combine a set with other sets to perform various operations like intersections, unions, and differences.
* Performance: Because of the implementation using hash tables, set offers faster lookups and membership tests.

## Conclusion

In this tutorial, you learned about the relationship between arrays, sets, and maps. 

We created, modified, and deleted elements in maps and sets. We compared maps and objects, and lastly, we talked about the benefits of sets over arrays.


