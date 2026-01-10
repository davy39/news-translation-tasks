---
title: JavaScript Array.find() Tutorial – How to Iterate Through Elements in an Array
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-01T16:41:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-find-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/find-method-js.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When you''re working with an array collection, sometimes you''ll only need
  to find out if an item exists in the array so you can retrieve it. And you won''t
  care how many other items (if any) exist within the same array.

  Well, we can use the find() meth...'
---

When you're working with an array collection, sometimes you'll only need to find out if an item exists in the array so you can retrieve it. And you won't care how many other items (if any) exist within the same array.

Well, we can use the `find()` method to do just that.

## How the Array.find() Method Works

The `find()` method is an `Array.prototype` (aka built-in) method which takes in a callback function and calls that function for every item it iterates over inside of the array it is bound to.

When it finds a match (in other words, the callback function returns `true`), the method returns that particular array item and immediately breaks the loop. So the `find()` method returns the first element inside an array which satisfies the callback function.

The callback function can take in the following parameters:

* `currentItem`: This is the element in the array which is currently being iterated over.
    
* `index`: This is the index position of the `currentItem` inside the array.
    
* `array`: This represents the target array along with all its items.
    

## **How to Use the** `find()` Method in JavaScript

In the following examples, I will demonstrate how you can use the `find()` method to retrieve the first item from an array which matches a specified condition in JavaScript.

### How to get a single item with find()

Let's assume you have a dog which goes missing. You report it to the relevant authorities and they bring together a group of recovered dogs.

To be able to find your dog, you need to provide unique information about him. For example, the breed of your dog (a Chihuahua) might be used to identify it.

We can express this scenario in JavaScript using an array collection. The array called `foundDogs` will contain all the names of the recovered dogs as well as their respective breeds. And we'll use the `find()` method to find the dog which is a Chihuahua from inside the array.

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
]

function findMyDog(dog) {
  return dog.breed === "Chihuahua"
}

let myDog = foundDogs.find(dog => findMyDog(dog));

console.log(myDog);


/*

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

The find method stops iterating when a match is found.

There is something very important to remember about `find()`: it stops executing once the callback function returns a `true` statement.

To illustrate this, we will once again use the missing dog example. This time, we will assume that two Chihuahuas were found.

But the `find()` method will only return the first instance of Chihuahua it discovers within the array. Any other instance will then be subsequently ignored.

We can also easily see this by logging the index position of that item into the console:

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
  
  {
    breed: "Chihuahua",
    color: "yellow"
  }
]


function findMyDog(dog, index) {
	if (dog.breed === "Chihuahua") console.log(index);
  return dog.breed === "Chihuahua"
}


let myDog = foundDogs.find((dog, index) => findMyDog(dog, index));


console.log(myDog);

/* 
1

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/findreturns1.png align="left")

### How to use a Destructuring Assignment

You can make your code more concise by combining both the destructuring assignment and an arrow function expression.

We'll use destructuring to extract only the name property from the object which we then pass in as a parameter to the callback function.

We'll get the same result:

```js
let foundDogs = [{
    breed: "Beagle",
    color: "white"
  },

  {
    breed: "Chihuahua",
    color: "yellow"
  },

  {
    breed: "Pug",
    color: "black"
  },
]

 


let myDog = foundDogs.find(({breed}) => breed === "Chihuahua");

console.log(myDog);

/*

{
  breed: "Chihuahua",
  color: "yellow"
}

*/
```

### How to find an item by its index

In this example, we will be finding and returning the spot belonging to 'David' from inside the array using its unique index value. This demonstrates one way we can use the `index` property inside of our `callback` function with the `find()` method:

```js
let reservedPositions = [{
    name: "Anna",
    age: 24
  },

  {
    name: "Beth",
    age: 22
  },

  {
    name: "Cara",
    age: 25
  },
  
  {
    name: "David",
    age: 30
  },
  
  {
    name: "Ethan",
    age: 26
  }
]


function findByIndex(person, index) {
  return index === 3
}


let myPosition = reservedPositions.find((person, index) => findByIndex(person, index));

console.log(myPosition);

/*
{
  age: 30,
  name: "David"
}
*/
```

## You Can Use the Context Object with find()

In addition to the callback function, the `find()` method can also take in a context object.

```js
find(callback, contextObj)
```

We can then refer to this object from inside the **callback** function on each iteration, using the `this` keyword as a reference. This allows us to access any properties or methods defined inside of the context object.

### How to use the context object with find()

Let's say we have an array of job applications and want to select just the first applicant who meets all of the criteria.

All criteria is defined inside a context object called `criteria` and that object is subsequently passed as a second parameter into the `find()` method. Then, from inside the callback function, we access the object to check if an applicant matches all of the criteria specified there.

```js
let applicants = [
    {name: "aaron", yrsOfExperience: 18, age: 66},
    {name: "beth", yrsOfExperience:  0, age: 18},
    {name: "cara", yrsOfExperience: 4, age: 22},
    {name: "daniel", yrsOfExperience: 3, age: 16},
    {name: "ella", yrsOfExperience: 5, age: 25},
    {name: "fin", yrsOfExperience: 0, age: 16},
    {name: "george", yrsOfExperience: 6, age: 28},
]

let criteria = {
	minimumExperience: 3,
  lowerAge: 18,
  upperAge: 65
}

   
let luckyApplicant = applicants.find(function(applicant) {
	return applicant.yrsOfExperience >= this.minimumExperience && applicant.age <= this.upperAge
  && applicant.age >= this.lowerAge ;
}, criteria)

console.log(luckyApplicant);

/*
{
  age: 22,
  name: "cara",
  yrsOfExperience: 4
}
*/
```

Technically, three applicants (Cara, Ella and George) all qualify based on the criteria. In other words, the three of them are at least 18 years old, not older than 65, and have at least 3 years of working experience.

However since the `find()` method always returns ONLY the first instance which evaluates to true, the other two will be ignored and the loop will be broken.

## **Wrapping Up**

The `find()` method is an `Array.prototype` method which takes in a callback function and calls that function for every item within the bound array.

When the callback function evaluates to `true`, the method returns the current item and breaks the loop. It returns just the first match – any other matches present inside of the array will be ignored.

In addition to the callback function, the `find()` method can also take in a context object as the second argument. This will enable you access any of its properties from the callback function using `this`.

I hope you got something useful from this article.

**I**f you want to learn more about Web Development, feel free to visit my\*\*\*\* [blog\*\*.\*\*](https://ubahthebuilder.tech/the-ultimate-tutorial-on-javascript-dom-js-dom-with-examples)

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
