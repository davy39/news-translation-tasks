---
title: How to Build a JavaScript Utility Library like Lodash
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2023-08-08T21:15:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-javascript-utility-library-like-lodash
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/inaki-del-olmo-NIJuEQw0RKg-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'A utility library is a library that helps you streamline the implementation
  of common coding tasks. With it, you only need to focus on writing code that makes
  your project unique.

  One of the most popular JavaScript utility libraries is Lodash. Lodash...'
---

A utility library is a library that helps you streamline the implementation of common coding tasks. With it, you only need to focus on writing code that makes your project unique.

One of the most popular JavaScript utility libraries is Lodash. Lodash is a JS library with over 40 million weekly downloads on npm. It helps provide additional functionalities to preexisting vanilla JS objects. Lodash uses a functional programming approach in implementing common tasks in JavaScript.

Although this library is great, using it in smaller projects might be overkill, especially if you only need 3 or 4 functionalities. With a package size of over [1.4MB](https://www.npmjs.com/package/lodash) comprising over 1000 files and 500 functions, having Lodash on your front-end can hinder the performance of your website.

In this article, I'll be showing you how to implement some of the key functionalities provided by Lodash. At the end of this tutorial, you’ll not only know how to implement the functionality of a popular library but you’ll also see an improvement in your JavaScript skills.

## Prerequisites
For this article, all you need is a code editor, a web browser, and a basic knowledge of JavaScript.

## Table of Contents
1. [Project Setup](#heading-project-setup)
2. [How to Create Array Methods](#heading-how-to-create-array-methods)
    1. [The _.chunk() method](#heading-the-chunk-method)
    2. [The _.compact() method](#heading-the-compact-method)
    3. [The _.concat() method](#heading-the-concat-method)
    4. [The _.drop() method](#heading-the-drop-method)
    5. [The _.dropRight() method](the_droprightmethod)
    6. [The _.fill() method](#heading-the-fill-method)
    7. [The _.flatten() method](#heading-the-flatten-method)
    8. [The _.intersection() method](#heading-the-intersection-method)
    9. [The _.remove() method](#the_removemethod)
    10. [The _.union() method](#heading-the-union-method)
3. [How to Create Collection Methods](#heading-how-to-create-collection-methods)
    1. [The _.filter() method](#heading-the-filter-method)
    2. [The _.find() method](#heading-the-find-method)
    3. [The _.partition() method](#heading-the-partition-method)
    4. [The _.shuffle() method](#heading-the-shuffle-method)
4. [How to Create Math Methods](#heading-how-to-create-math-methods)
    1. [The _.mean() method](#heading-the-mean-method)
    2. [The _.max() method](#heading-the-max-method)
    3. [The _.min() method](#heading-the-min-method)
    4. [The _.sum() method](#heading-the-sum-method)
5. [How to Create Object Methods](#heading-how-to-create-object-methods)
    1. [The _.keys() method](#heading-the-keys-method)
    2. [The _.values() method](#heading-the-values-method)
6. [How to Create String Methods](#heading-how-to-create-string-methods)
    1. [The _.repeat() method](#heading-the-repeat-method)
    2. [The _.split() method](#heading-the-split-method)
7. [Conclusion](#heading-conclusion)

## Project Setup
The first thing to do is to create a folder called `lodash-project` that contains an HTML file and a JavaScript file. 

The JavaScript file will contain the code, while our HTML file will be used to link the files together. 

You can give them any valid name you like but I’ll be sticking with `index.html` and `index.js`.

Within the HTML file, you’ll add the script element to link with your index.js file.

Here’s the code for `index.html`:

```html
<!DOCTYPE HTML>
<html>
      <head>
             <title>Lodash project</title>
      </head>
      <body>
             <script src='index.js'></script>
      </body>
</html>
```

Within the JavaScript file (index.js), we'll be using a JavaScript class (`_`) and static methods (whose name will be the Lodash methods we'll be implementing) for structuring our code.

Here's the format it should be in:

```javascript
class _ {
    static name_of_method(){
        //code
    }
}
```

From this point onward, I’ll be showing you how to implement 10 Lodash array methods, four collection methods, four math methods, two object methods, and two string methods. Are you ready? Let’s go!

## How to Create Array Methods

### The `_.chunk()` method

First, we'll see how to implement the `_.chunk()` method. In Lodash, the chunk method helps you divide the content of your array into groups. 

This method is useful when you want to display a long list of items in a paginated user interface. 

By applying the `chunk()` method, you can divide the array into smaller arrays, each containing a fixed number of items. This allows you to efficiently manage the display of items page by page, enhancing the user experience and minimizing load time.

It can also be used for dealing with data that needs to be processed in parallel or batched operations.

According to the [Lodash documentation](https://lodash.com/docs/#chunk), this is how it works: 

```javascript
//divides the array into a group of 2
_.chunk(['a', 'b', 'c', 'd'], 2);
//returns [ ['a', 'b'], ['c', 'd'] ]
 
//divides the array into a group of 3 and shifts the rest into another
_.chunk(['a', 'b', 'c', 'd'], 3);
//returns [ ['a', 'b', 'c'], ['d'] ]
```

Here's how to implement it yourself: 

```javascript
class {
     //... other methods
     
      static chunk(array, size=1){
             let newArray = [];  
             for(let i = 0; i < array.length; i += size){ 
                    let chunk = array.slice(i, i + size);
                    newArray.push(chunk) 
             } 
             return newArray;                        
      }
}
```

In the code above, the first step is creating a static `chunk()` method with an `array` and `size` parameter. The `size` parameter gets a default value of 1. 

Next, we create an empty array (`newArray`) that’ll store the split chunks. Then we’ll use loops and the `array.slice()` method to slice out chunks from the original array and push it to the new array (`newArray`). 
 
### The `_.compact()` method

Now let's look at the `_.compact()` method. In Lodash, the `compact()` method returns an array with all falsy elements removed. Examples of falsy values are `undefined`, `null`, `''`, `false`, `0`, and so on.

This method is useful when you want to clean up an array and focus on meaningful and non-empty values.

You can also use it for cleaning arrays that have incomplete data or irrelevant information.

According to the [Lodash documentation](https://lodash.com/docs/#compact), this is how it works:

```javascript
let surveyReport = ['yes', 'no', 'not sure', null, 'no', ''];

//removes the falsy elements
_.compact(surveyReport);
//returns ['yes', 'no', 'not sure', 'no']
```

Here’s how you to implement it yourself:

```javascript
class _ {
      //... other codes
      static compact(array){
             let newArray = array.filter( val => {return Boolean(val) === true})
             return newArray;
      }
}
```

From the code above, we created a static `compact()` method with an `array` parameter. Then we used the `array.filter()` method and the `Boolean()` function to filter out values that are truthy, not falsy. 
 
### The `_.concat()` method

In Lodash, the `concat()` method is used for concatenating two or more arrays or values. This is particularly useful when you're dealing with data from different sources and want to present them in a comprehensive view.

Imagine a scenario where you have multiple arrays containing related information, such as customer names, addresses, and order details. The `concat()` method allows you to effortlessly combine these arrays, creating a unified dataset that can be easily processed or displayed.

According to the [Lodash documentation](https://lodash.com/docs/#concat), this is how it works:
 
```javascript
let array = [1, 2];
let other = _.concat(array, 4, [1], [ [12, true] ] );
 
console.log(other)
//returns [ 1, 2, 4, 1, [12, true] ]
```

Here’s how to implement it yourself:

```javascript
class _ {
      //...other methods
      
      static concat(array, ...values){
                          
             for(let i = 0; i < values.length; i++){
                    array = array.concat( values[i] ) 
             } 
             return array;
      }
}
```

In the code above, I created a static `concat()` method with an `array` and `values` parameter. The parameter will be treated as an array representing the separate arrays/values we’ll be concatenating. 

Next, we used the for loop and the `array.concat()` method to concatenate every element in the values parameter to our array parameter.
 
### The `_.drop()` method

The `drop()` method returns an array with some of its elements dropped from the beginning.
 
The `drop()` method plays a crucial role in implementing stack-like behavior with arrays. You can use this method to ensure that only the most recent tasks are prioritized.

According to the [Lodash documentation](https://lodash.com/docs/#drop), this is how it works:

```javascript
//drops the first element and returns the rest
_.drop([1,2,3])
//=> [2,3]
 
//drops the first 2 elements and returns the rest
_.drop([1,2,3,4], 2)
//=> [3,4]
 
//drops the first 3 elements and returns the rest
_.drop([2,4,6], 3)
//=> []
 ```
 
Here's how to implement it yourself:

```javascript
class _ {
    //other methods
    
    static drop(array, n=1){
           return array.slice(n, array.length) 
     }
}
```

In the code above, we created a static `drop()` method with an `array` and `n` parameter. `array` represents the array whose elements will be dropped while `n` represents the number of elements to be dropped from the beginning. 

Then we used an `array.slice()` method to return an array starting from position `n` to the last element.

### The `_.dropRight()` method

The ` dropRight()` method returns an array with some of its elements dropped from the end.
 
The `drop()` method plays a crucial role in implementing queue-like behavior with arrays. You can use this method to ensure that only the oldest tasks are prioritized.

According to [Lodash](https://lodash.com/docs/#dropRight), this is how it works:

```javascript
//drops the last element and returns the rest
_.dropRight([1,2,3,4]) 
 
//drops the last 2 elements and returns the rest
_.dropRight([1,2,3,4], 2)
//[2, 3]
```

Here’s how to implement it yourself:

```javascript
class _ {
    //other methods ...
    
     static dropRight(array, n=1){
           return array.slice(0, -n)
     }
}
```

From the code above, we created a static `dropRight()` method with an `array` and `n` parameter. `array` represents the array whose elements will be dropped while `n` represents the number of elements to be dropped from the end. 

Next, we use the `array.slice()` method to return an array starting from position 0 to (but not including) –`n`.
 
### The `_.fill()` method

The `fill()` method fills an array with a specific value.
 
Imagine you have an array representing a game board where certain cells need to be marked as occupied. By using the `fill()` method, you can efficiently replace a range of cells with a marker value, indicating their status.

According to [Lodash](https://lodash.com/docs/#fill), this is how it works:

```javascript
let board = Array(9);
 
//replaces or fills all the elements in the array with '0'
_.fill(array, 0);
console.log(array)
//returns [0, 0, 0, 0, 0, 0, 0, 0, 0];
 
let array = [1,3,5,7];
//replaces or fills the array with 'hello' from index 0 to(but not including) index 3
_.fill(array, 'hello', 0, 3)

console.log(array)
//returns ['hello', 'hello', 'hello', 7];
```

Here's how to implement it yourself:

```javascript
class _ {
    //other methods ...
    
     static fill(array, value, start=0, end=array.length){ 
           for(let i = start; i < end; i++){ 
                 array[i] = value 
           } 
           return array;    
     }
}
```

In the code above, we created a static `fill()` method with an `array`, `value`, `start`, and `end` parameter. 

`array` represents the array whose element will be filled. `value` is the value that’ll fill/replace the elements in the array. `start` is the position to start filling from. It has a default value of 0. `end` represents the position that the filling will end at. Its default value is `array.length`. 

Within the method, we created a loop that changes the value of each element to `value`.

### The `_.flatten()` method

The `flatten()` method flattens an array one level deep.

Imagine you have an array containing sub-arrays representing different categories of items. By applying the `flatten()` method, you can seamlessly merge these sub-arrays into a single array, simplifying the process of iterating, searching, or performing operations on the combined dataset. 

According to the [Lodash documentation](https://lodash.com/docs/#flatten), this is how it works:

```javascript
_.flatten([['James'], [17], ['Male']]);
//-> ['James', 17, 'Male']
```

Here’s how to implement it:

```javascript
class _ {
    //... other methods
    
     static flatten(array){
           return [].concat(...array);
     }
}
```

In the code above, we created a static `flatten()` method with an `array` argument. Then we used the spread operator and `array.concat()` to concatenate an empty array with the expanded iterable.

### The `_.intersection()` method

The `intersection()` method returns an array that contains values that are present in all given arrays.

Imagine you have multiple arrays containing user preferences for different features of your application. By using the `intersection()` method, you can easily determine which preferences are common across all users, helping you identify the most popular or preferred features. 

According to the [Lodash documentation](https://lodash.com/docs/#intersection), this is how it works:

```javascript
let preference1 = ['Post', 'View', 'Comment'];
let preference2 = ['Like', 'Comment', 'Share'];

_.intersection(preference1, preference2)
returns ['Comment']
```

Here’s how to implement it yourself:

```javascript
class _ {
     //...other methods
     
     static intersection(...arrays){ 
           if (arrays.length === 0){
                 return []
           }
           let intersection = arrays.reduce((prev, current) => {
                 return prev.filter((element) => current.includes(element) );
           })
                       
           return [...new Set(intersection)]; //remove duplicates
     }
}
```

From the code above, we created a static `intersection()` method with an `arrays` parameter that has a spread operator. Within the function, we'll return an empty array if the method is called without any parameter. 

Next, we use the `reduce()` method to recursively iterate over the arrays and filter the common elements at each step, until it finds the intersection of all arrays. 

Then we return the final result as an array after removing the duplicates with a `Set` constructor function.

### The `_.remove()` function

The `remove()` function removes some elements that satisfy a condition and returns the result. It also permanently removes those elements from the original array. 

For example, if you have an array of numbers and you want to remove all occurrences of a certain value, you can use `remove()` to achieve this efficiently.

According to the [Lodash documentation](https://lodash.com/docs/#remove), here’s how it works:

```javascript
let array = [1,2,3,4,5,6,7];

let odd = _.remove(array, function(){
     return n%2 !== 0
});

console.log(odd)
//[1,2,5,7]
     
console.log(array)
//returns the remaining => [2,4,6]
```

Here’s how to implement it yourself:

```javascript
class _ {
     //... other methods
     
     static remove(array, predicate){
           let truthy = array.filter(predicate);
           for(let i of truthy){
                 let n = array.indexOf(i)
                 array.splice(n, 1); 
           } 
           return truthy;
     }
}
```

From the code above, we created a static `remove()` method that contains two parameters: `array` and `predicate`. `array` refers to the array whose elements will be removed while `predicate` is a function that'll specify the conditions the elements must pass to be removed.

Next, we use the `array.filter()` method to filter out elements that pass the conditions. Then we used loops and `array.splice()` to remove the passed element from the original array. Finally, we return the truthy array.

### The `_.union()` method

The `union()` method returns an array of unique values from one or more arrays.

Imagine you have several arrays representing different categories of items, and you want to combine them into a single array without repeating any items. By using the `union()` method, you can easily merge these arrays, ensuring that each value appears only once in the resulting array.

This is valuable when dealing with data from various sources that might contain overlapping information.

According to [Lodash](https://lodash.com/docs/#union), here is how it works:

```javascript
let basket1 = ['Egg', 'Shoe', 'Milk'];
let basket2 = ['Shoe, 'Milk', 'Honey'];

let allBasket = _.union(basket1, basket2)
console.log(allBasket)
//['Egg', 'Shoe', 'Milk', 'Honey']
```

Here’s how to implement it yourself:

 ```javascript
class _ {
    //other methods ...
    
    static union(...arrays){
          let total = []
          for(let i of arrays){
                total.push(...i)
          }
          return new Set(total);
    }
}
```

In the code above, we created a static `union()` method with an `arrays` parameter that has a spread operator. We created a variable storing an empty array and used the `for-of` loop to push elements in the `arrays` parameter to `total`. 

Next, we insert the total variable into a `Set` function to remove duplicate and return it.

## How to Create Collection Methods

### The `_.filter()` method

In Lodash, the `filter()` method returns an array of elements that satisfies a condition. Unlike `remove()`, it doesn’t modify the original array.

Its applications range from data filtering to creating custom subsets. 

For example, if you have an array of objects representing users, and you want to retrieve all users who are active. By using the `filter()` method, you can efficiently create a new array containing only the active users.

Another example is using this method for data transformation scenarios. If you have an array of numeric values and you want to extract only the even numbers, you can easily achieve this by applying the `filter()` method with a custom filtering function.

According to the [Lodash documentation](https://lodash.com/docs/#filter), this is how it works:

```javascript
let users = [
    {name: 'Zoe', age: 24, active: false},
    {name: 'Aisha', age: 20, active: true},
    {name: 'Alex', age: 19, active: true}
];
filter(users, function(element){ return element.active > true})

//returns => [
    {name: 'Aisha', age: 20, active: true},
    {name: 'Alex', age: 19, active: true}
]
 ```
 
Here’s how to implement it on your own:

```javascript
class _ {
     //... other methods
    
     static filter(collection, predicate){
           return collection.filter(predicate);
    }
}
```

From the code above, we created a static `filter()` method with an `array` and `predicate` parameter. `array` is the array whose elements will be filtered and `predicat`e is the function that contains the conditions each element must pass to be filtered out. 

Then we use the `array.filter()` method to filter the array and return the result.

### The `_.find()` method

The `find()` method returns the first element in an array that satisfies a particular condition.

Its applications range from targeted searches to efficient data retrieval.

For example, say you have an array of objects representing products in an online store, and you want to find the first product that is currently on sale. By using the `find(`) method, you can quickly locate the desired product object that matches the sale condition.

The `find()` method also plays a crucial role in scenarios where you need to search for a specific item within a collection, such as finding a particular user by their username or locating a book by its title. 

According to the [Lodash documentation](https://lodash.com/docs/#find), this is how it works:

```javascript
let products = [
     {name: 'Rice', qty: 20},
     {name: 'Egg', qty: 24},
     {name: 'Milk', qty: 19},
     {name: 'Wheat', qty: 20}
]

//finds the first product whose quantity is greater than 20
_.find(products, function(product){ return product.qty > 20})
 
//returns {name: 'Egg', qty: 24}
```

Here's how to implement it yourself:

```javascript
class _ {
    //... other methods
    
     static find(collection, predicate, fromIndex=0){
           let ans = collection.slice(fromIndex, collection.length)
           return ans.find(predicate);
     }
}
```

In the code above, we created a static `find()` method with 3 parameters: `collection`, `predicate`, `fromIndex`. 

`collection` is the array we’ll be searching from. `predicate` is a function containing the condition that the element must pass to be returned. `fromIndex` specifies the index to begin the search from. 

First, we used the `array.slice()` method to slice the array from a start position specified by `fromIndex` parameter to the end of the collection. Next, we use the `array.find()` method on the sliced array and return the result.

### The `_.partition()` method

The `partition()` method creates an array comprised of two elements. The first is an array of elements that satisfies a certain condition while the second is an array of elements that doesn’t satisfy the condition.
 
Its applications range from data segregation to creating distinct subsets.

Imagine you have an array of numbers, and you want to separate the even numbers from the odd numbers. By using the `partition()` method, you can easily create two arrays: one containing all the even numbers and another containing all the odd numbers. This makes it convenient to perform separate operations or analyses on each subset.

Also, the `partition()` method is beneficial when dealing with filtering and categorization scenarios. If you have a collection of objects representing products and you want to categorize them into two groups – those that are on sale and those that are not – the `partition()` method provides an elegant solution.

According to the [Lodash documentation](https://lodash.com/docs/#partition), this is how it works:

 ```javascript
 let products = [
     {name: 'Milk', sold: true},
     {name: 'Cream', sold: false},
     {name: 'Bicycle', sold: true},
     {name: 'Socks', sold: false}
 ];
 
_.partition(products, function(e){ return e.sold === true})
returns [
     [
    {name: 'Milk', sold: true},
    {name: 'Bicycle', sold: true}
],
     [
     {name: 'Cream', sold: false},
     {name: 'Socks', sold: false}
]
]
 ```
 
Here’s how to implement it yourself:

```javascript
class _ {
    //... other methods
    
    static partition(collection, predicate){
        let truthy = array.filter(predicate);
        let falsy = collection;
        
        for(let i of truthy){
            let n = falsy.indexOf(i)
            falsy.splice(n, 1); 
        } 
        
        return [truthy, falsy];
    }
}
```

In the code above, we created a static `partition()` method with a `collection` and `predicate` parameter. `collection` is the array that’ll be used while `predicate` is the function that contains the conditions the elements must pass to be partitioned to the first element. 

First, we created two variables: `truthy` and `falsy`. `truthy` is an array containing the elements that passed the condition while `falsy` stores the collection. 

Next, we used a `for-of` loop and the `splice()` method to remove the elements in the `falsy` array from `truthy`. And finally, we returned an array containing both `truthy` and `falsy` arrays.

### The `_.shuffle()` method

The `shuffle()` method returns an a shuffled array using the Fisher-Yates shuffle.

Its applications range from enhancing user engagement to introducing randomness into various scenarios

Imagine you have an array of questions for a quiz app, and you want to present the questions in a different order each time a user takes the quiz. By using the `shuffle()` method, you can easily create a new array with the questions in a randomized order, providing a fresh experience for users in each quiz session.

According to [Lodash](https://lodash.com/docs/#shuffle), this is how it works:

```javascript
let quizQuestions = [1, 2, 3, 4, 5, 6, 7, 8];

_.shuffle(quizQuestions)
//shuffled version eg [2,3,8,5,1,7,4,6]
 ```
 
Here's how to implement it yourself:

```javascript
class _ {
    //... other methods
    
     static shuffle(collection){
           function sh(array=collection, shuffled=[], length=collection.length){
                 if(length === 0){
                      return shuffled;
                 }
                       
                 let rand = Math.floor( Math.random() * ( length - 1) );
                       
                 shuffled.push( array[rand] )
           
                length -= 1;
                       
                       array.splice(rand, 1);
                       
                 return sh(array, shuffled, length);
                       
           }
           return sh() 
                 
     }
}
```

In the code above, we created a static `shuffle()` method with a `collection` parameter that represents the array to shuffle. Within it is another function `sh()` that uses recursion to shuffle the array.

## How to Create Math Methods

### The `_.mean()` method

In Lodash, the `mean()` method calculates the average value of the elements in an array.

This method can be used for performing data analysis.

Imagine you have an array of test scores, and you want to find out the average score of the students. By using the `mean()` method, you can effortlessly calculate the average test score, which gives you a sense of the overall performance of the group.

Furthermore, the `mean()` method plays a crucial role in data analysis and statistics.

Whether you're working with financial data, scientific measurements, or any other numerical data, calculating the mean helps you understand the typical value and make informed decisions based on the data's central tendency.

According to the [Lodash documentation](https://lodash.com/docs/#mean), this is how it works:

```javascript
let mathScore = [60, 70, 50, 80];

_.mean(mathScore)
returns 65
```

Here's how to implement it yourself:

```javascript
class _ {
    //... other methods
    
     static mean(array){
           let sum = array.reduce( (accumulator, current) => {
                 return accumulator + current
           }, 0);
           return sum/array.length;
    }
}
```

In the code above, we created a static `mean()` method with an `array` parameter that represents the array whose elements we'll use to calculate the mean. 

Next, we use the `array.reduce()` method to find the sum of all the values. 

Finally, we divide the result by the length of the array and return it.

### The `_.max()` method

The `max()` method returns the maximum value in an array.

Its applications range from identifying the highest values to detecting outliers.

The `max()` method is crucial in scenarios where you need to identify extreme values in a dataset.

Whether you're analyzing temperature readings, stock prices, or any other numeric data, finding the maximum value can help you understand the range and potential outliers within the data.

According to the [Lodash docs](https://lodash.com/docs/#max), here's how it works:

```javascript
let topStockPrices = [545, 230, 123, 1004, 890,890];

_.max(topStockPrices)
//1004
```

Here's how to implement it:

```javascript
class _ {
    //... other methods
    
     static max(array){
           return Math.max(...array)
     }
}
```

In the code above, we created a static `mean()` method with an array `parameter` that represents the array whose elements will be used to calculate the max value. 

Next, we use the spread operator and `Math.max()` function to calculate the maximum value.

### The `_.min()` method

The `_.min()` method returns the minimum value in an array.

The `min()` method is crucial in scenarios where you need to identify the smallest value in a dataset.

Whether you're analyzing prices, durations, or any other numeric data, finding the minimum value can help you understand the range and potential outliers within the data.

According to the [Lodash docs](https://lodash.com/docs/#min), here's how it works:

```javascript
let productPrice = [200, 150, 500, 230, 99];

_.min(productPrice)
//returns 99
```

Here's how to implement it:
```javascript
class _ {
    //...other methods
    
     static max(array){
           return Math.min(...array)
     }
}
```

In the code above, we created a static `min()` method with an `array` parameter that represents the array whose elements will be used to calculate the min. 

Next, we use the spread operator and `Math.min()` function to calculate the minimum value.
 
### The `_.sum()` method

The `sum()` method calculates the sum of all the elements in an array.

This method can be used for calculating aggregate values.

For example, the `sum()` method is crucial in scenarios where you need to determine the aggregate value of a dataset.

Whether you're working with financial transactions, quantities, or any other numeric data, calculating the sum helps you understand the overall magnitude of the data.

According to the [Lodash docs](https://lodash.com/docs/#sum), here’s how it works:

```javascript
let sales = [20000, 34000, 21000, 15000];

_.sum(sales)
//returns -> 90000
```

Here’s how to implement it:

```javascript
class _ {
    //... other methods
    
     static sum(array){
           let total = array.reduce( (accumulator, current) => {
                 return accumulator + current
           }, 0);
           return total;
     }
}
```

In the code above, we created a static `sum()` method with an `array` parameter. Next, we used the `array.reduce()` method to add up all the array element's values.

## How to Create Object Methods

### The `_.keys()` method
	
In Lodash, the `keys()` method returns an array containing the properties of an object.

Imagine you have an object representing a user profile with properties like name, email, and age. By using the `keys()` method, you can easily extract the property names and work with them.

According to the [Lodash docs](https://lodash.com/docs/#keys), here’s how it works:

```javascript
returns all the properties of th object
_.keys({name: 'john', age: 7})
//['name', 'age']
```

Here's how to implement it:

```javascript
Class _{
     static keys(object){
           return Object.keys(object)
    }
}
```

In the code above, we created a static `keys()` method with an `object` parameter that represents the object whose properties would be extracted. 

Then we use the `Object.keys()` method to extract the properties and return the result.

### The `_.values()` method

The `values()` method returns an array containing the values of an object's properties.

Imagine you have an object representing a user profile with properties like name, email, and age. By using the `values()` method, you can easily extract the property values and work with them.

According to the [Lodash docs](https://lodash.com/docs/#values), here's how it works:

```javascript
//returns the object values
_.values({name: 'john', age: 7})
//['john', 7]
```

Here's how to implement it:
```javascript
class _{
     static values(){
           return Object.values(object)
    }
}
```

In the code above, we created a `values()` method with an `object` parameter that represents the object whose property values would be extracted. Then we use the `Object.values()` method to extract the values and returned the result.
 
## How to Create String Methods

### The `_.repeat()` method

In Lodash, the `repeat()` method returns a string that has been duplicated a specific number of times.

Its applications range from creating patterns to formatting output, making it a handy tool for various string manipulation tasks.

For instance, if you want to create a separator line of hyphens in a console output, you can use the `repeat()` method to generate the necessary number of hyphens.

According to [Lodash](https://lodash.com/docs/#repeat), here is how it works:

```javascript
//repeats the string '-' 10 times

_.repeat('-', 10)
console.log('hello world')
_.repeat('-', 10)

//returns:
//'----------'
//'hello world'
//'----------'
```

Here's how to implement it:

```javascript
class _ { 
    //... other methods
    
     static repeat(string='', n=1){
           let repeated ='';
                       
           for(let i = 0; i < n; i++){
                 repeated += string;
           }
           return repeated;
     }
}
```

In the code above, we created a static `repeat()` method with a string and n parameter. `string` refers to the string that’ll be duplicated while `n` specifies the number of times it’ll be repeated.

Next, we created a `repeated` variable that stores an empty string. ANd finally, we used the `for` loop to concatenate the string `n` times.

### The `_.split()` method

The `split()` method splits a string by a separator and stores the parts in an array.

Its applications range from text processing to data extraction.

The `split()` method can be beneficial in scenarios where you're dealing with data in a specific format.

For example, if you have a list of values in a string separated by plus sign(+), you can use the `split()` method to extract each value and store them in an array.

According to the [Lodash docs](https://lodash.com/docs/#split), here’s how it works:

```javascript
//Splits all the characters
_.split('hello', '')
['h', 'e', 'l', 'l', 'o']
 
//Split using _ as separator 
_.split('h_e_l_l_o', '_')
['h', 'e', 'l', 'l', 'o']
 
Splits the string using + as a separator and limits the elements to 2
_.split'`how+to+cook+rice', '+', 2)
['how', 'to']
```
 
Here's how to implement it:

```javascript
class _ {
    //... other methods
    
     static split(string='', separator, limit){
           let spl = string.split(separator);
           let limited = [];
                       
           if (limit === undefined){
                 return spl;
           } else {
                 for(let i=0; i<limit; i++){
                       limited.push(spl[i])
                 }
                 return limited
                       
            }
     }
}
```

In the code above, we created a `split()` method with a `string`, `separator`, and `limit` parameter. 

`string` is the string whose characters will be split. `separator` will be used as the string separator and `limit` sets a limit for the split characters to be returned. 

Next, we used the `string.split()` method to split string with separator. Then we returned the split string if no limit was specified. If the limit was specified, we used the `for` loop to push the selected elements to a `limited` variable and returned its result.

## Conclusion
Phew – that was a lot. If you made it this far, let me congratulate you on time well spent. 

Throughout the article, you learned how to implement some functionalities of the Lodash library. 

Now you can challenge yourself to complete the library by implementing the remaining methods and functions, or add more functionalities to it. 

I hope this helps. Unrelated, but if you need a skilled technical writer don’t forget to contact me through [Twitter(@GidtheCoder)](https://twitter.com/gidthecoder) or [email(akinsanmi20700@gmail.com)](mailto:akinsanmi20700@gmail.com). Bye for now.




