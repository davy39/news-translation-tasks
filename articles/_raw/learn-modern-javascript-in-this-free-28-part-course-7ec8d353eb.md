---
title: Learn ES6 in this free 28-part Scrimba course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T16:09:50.000Z'
originalURL: https://freecodecamp.org/news/learn-modern-javascript-in-this-free-28-part-course-7ec8d353eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bBlPwnLZ3hoVAUbxoczzqQ.png
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  As a part of our collaboration with freeCodeCamp, their eminent instructor Beau
  Carnes has turned their entire ES6 curriculum into an interactive Scrimba course
  which you can watch today.

  As yo...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/dIB4enxTUgFHbooVsnQOkXnoQLJqvnYlQIpe)
_[Click here to get to the course.](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

As a part of our collaboration with freeCodeCamp, their eminent instructor [Beau Carnes](https://twitter.com/carnesbeau?lang=en) has turned their entire ES6 curriculum into an interactive Scrimba course [which you can watch today.](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

As you might know, ES6 is just a way to describe newer JavaScript features that weren’t fully and widely accepted until 2017. Now, almost all JavaScript is written using ES6 features, so this course sets you up to become a modern JavaScript developer.

In this article, I’ll list out the chapters and give you a sentence or two about it. This way you should be able to quickly judge whether this course looks interesting to you.

If so, be sure to [head over to Scrimba to watch it!](https://scrimba.com/g/ges6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

### 1. Introduction

In the first screencast, Beau gives you a quick intro to the course and himself and talks a little bit about ES6. He also shows you how you can find the curriculum if you’d like to go through it on [the freeCodeCamp site](https://freecodecamp.org) as well.

### 2. Explore Differences Between the var and let Keywords

The first subject is variables. In ES5 we could only declare variables with `var`, but starting with ES6 we can now use `let` and `const`.

How are `let` and `var` different? `let` doesn’t allow you to declare a variable twice.

```js
var catName = "Quincy";  
var catName = "Beau";  
// Works fine!

let dogName = "Quincy";  
let dogName = "Beau";  
// Error: TypeError: unknown: Duplicate declaration "dogName"

```

### 3. Compare Scopes of the var and let Keywords

Another major difference between `var` and `let` is how they are scoped ([freeCodeCamp’s guide on scope](https://guide.freecodecamp.org/javascript/scopes/)).

When you declare a variable with `var` it is declared globally or locally if inside a function.

When it’s declared with `let` it would be limited to a block statement or expression scope.

Beau shows you two examples.

![Click on an image to go to the Scrimba cast](https://cdn-media-1.freecodecamp.org/images/1*laCp2HN4_bQD3BBf0QLkDw.png)

![Click on an image to go to the Scrimba cast](https://cdn-media-1.freecodecamp.org/images/1*2qchOXyzuS8lMoVgYuRd2Q.png)
_[Click here to go to the Scrimba cast](https://scrimba.com/p/p7v3gCd/cLez8TE?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

### 4. Declare a Read-Only Variable with the const Keyword

`const` is a way to assign a read-only variable that cannot be reassigned.

```js
const fcc = "freeCodeCamp";  
const sentence = fcc + " is cool!";  
sentence = fcc + " is amazing!";  
// Error: SyntaxError: unknown: "sentence" is read-only

```

### 5. Mutate an Array Declared with const

You should be careful with `const`, though as it is still possible to mutate arrays assigned with it.

```js
const myArray = [5, 7, 2];

myArray[0] = 2;  
myArray[1] = 7;  
myArray[2] = 5;

console.log(myArray);   
// [2, 7, 5]

```

Same applies to objects.

### 6. Prevent Object Mutation

In order to avoid object and array mutation, you can use `Object.freeze()`:

```js
const MATH_CONSTANTS = {  
  PI: 3.14  
};

Object.freeze(MATH_CONSTANTS);  
MATH_CONSTANTS.PI = 99;

// TypeError: Cannot assign to read-only property 'PI' of object '#<Object>'

```

If you wish to freeze arrays, you can also use `Object.freeze()` and pass your array, but it might not work on some old browsers.

### 7. Use Arrow Functions to Write Concise Anonymous Functions

ES6 also introduces a shorter way of writing anonymous functions.

```js
// ES5 anonymous function  
var magic = function() {  
  return new Date();  
};

// A shorter ES6 arrow function  
var magic = () => {  
  return new Date();  
};

// And we can shorten it even further  
var magic = () => new Date();

```

### 8. Write Arrow Functions with Parameters

Passing parameters to arrow functions is also easy.

```js
var myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [3, 4, 5]));  
// [1, 2, 3, 4, 5]

```

### 9. Write Higher Order Arrow Functions

Arrow functions shine when used with higher order functions, like `map()`, `filter()`, `reduce()`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-4.png)
_[Click here to go to the Scrimba cast](https://scrimba.com/p/p7v3gCd/ck4L6T9?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

### 10. Set Default Parameters for Your Functions

If some of our function parameters can be set to a default value, this is how you can do it in ES6:

```js
// If value parameter is not passed in, it will be assigned to 1.   
function increment(number, value = 1) {  
  return number + value;  
};

console.log(increment(5, 2)); // 7  
console.log(increment(5)); // 6

```

### 11. Use the Rest Operator with Function Parameters

Rest operator allows you to create a function that takes a variable number of arguments.

```js
function sum(...args) {  
  return args.reduce((a, b) => a + b);  
};

console.log(sum(1, 2, 3)); // 6  
console.log(sum(1, 2, 3, 4)); // 10

```

### 12. Use the Spread Operator to Evaluate Arrays In-Place

The _spread_ operator looks exactly like the _rest_ operator and looks like this: `…`, but it expands an already existing array into individual parts.

```js
const monthsOriginal = ['JAN', 'FEB', 'MAR'];

let monthsNew = [...monthsOriginal];  
monthsOriginal[0] = 'potato';

console.log(monthsOriginal); // ['potato', 'FEB', 'MAR']  
console.log(monthsNew); // ['JAN', 'FEB', 'MAR']

```

### 13. Use Destructuring Assignment to Assign Variables from Objects

Destructuring is a special syntax for neatly assigning values taken directly from an object to a new variable.

```js
// Object we want to destructure  
var voxel = {x: 3.6, y: 7.4, z: 6.54 };

// This is how we would do it in ES5  
var a = voxel.x; // a = 3.6  
var b = voxel.y; // b = 7.4  
var c = voxel.z; // c = 6.54

// A shorter ES6 way  
const { x : a, y : b, z : c } = voxel;   
// a = 3.6, b = 7.4, c = 6.54

```

### 14. Use Destructuring Assignment to Assign Variables from Nested Objects

You can use destructuring to get values out of even nested objects:

```js
const LOCAL_FORECAST = {  
  today: { min: 72, max: 83 },  
  tomorrow: { min: 73.3, max: 84.6 }  
};

function getMaxOfTmrw(forecast) {  
  "use strict";

// we get tomorrow object out of the forecast  
  // and then we create maxOfTomorrow with value from max  
  const { tomorrow : { max : maxOfTomorrow }} = forecast;

return maxOfTomorrow;  
}  
console.log(getMaxOfTmrw(LOCAL_FORECAST));  
// 84.6

```

### 15. Use Destructuring Assignment to Assign Variables from Arrays

Do you wonder if destructuring can be used with arrays? Absolutely! There is one important difference though. While destructuring arrays, you cannot specify a value you wish to go into a specific variable and they all go in order.

```js
const [z, x, , y] = [1, 2, 3, 4, 5, 6];

// z = 1;  
// x = 2;   
// Skip 3  
// y = 4;

```

### 16. Use Destructuring Assignment with the Rest Operator to Reassign Array Elements

Let’s now combine the rest operator with destructuring to supercharge our ES6 skills.

```js
const list = [1,2,3,4,5,6,7,8,9,10];

// Create a and b out of first two members  
// Put the rest in a variable called newList  
const [ a, b, ...newList] = list;

// a = 1;  
// b = 2;  
// newList = [3,4,5,6,7,8,9,10];

```

### 17. Use Destructuring Assignment to Pass an Object as a Function’s Parameters

We can create more readable functions.

```js
const stats = {  
  max: 56.78,  
  standard_deviation: 4.34,  
  median: 34.54,  
  mode: 23.87,  
  min: -0.75,  
  average: 35.85  
};

// ES5  
function half(stats) {  
  return (stats.max + stats.min) / 2.0;  
};

// ES6 using destructuring  
function half({max, min}) {  
  return (max + min) / 2.0;  
};

console.log(half(stats));   
// 28.015

```

### 18. Create Strings using Template Literals

Template literals help us to create complex strings. They use a special syntax of ```` and `${}` where you can combine template text with variables together. For example ``Hello, my name is ${myNameVariable} and I love ES6!``

```js
const person = {  
  name: "Zodiac Hasbro",  
  age: 56  
};

// Template literal with multi-line and string interpolation

const greeting = `Hello, my name is ${person.name}!   
I am ${person.age} years old.`;

console.log(greeting);

```

### 19. Write Concise Object Literal Declarations Using Simple Fields

ES6 added support for easily defining object literals.

```js
// returns a new object from passed in parameters  
const createPerson = (name, age, gender) => ({  
  name: name,  
  age: age,   
  gender: gender  
});

console.log(createPerson("Zodiac Hasbro", 56, "male"));

// { name: "Zodiac Hasbro", age: 56, gender: "male" }

```

### 20. Write Concise Declarative Functions with ES6

Objects in JavaScript can contain functions.

```js

const ES5_Bicycle = {  
  gear: 2,  
  setGear: function(newGear) {  
    "use strict";  
    this.gear = newGear;  
  }  
};

const ES6_Bicycle = {  
  gear: 2,  
  setGear(newGear) {  
    "use strict";  
    this.gear = newGear;  
  }  
};

ES6_Bicycle.setGear(3);

console.log(ES6Bicycle.gear); // 3

```

### 21. Use class Syntax to Define a Constructor Function

ES6 provides syntax to create objects using the `class` keyword:

```js

var ES5_SpaceShuttle = function(targetPlanet){  
  this.targetPlanet = targetPlanet;  
}

class ES6_SpaceShuttle {  
  constructor(targetPlanet){  
    this.targetPlanet = targetPlanet;  
  }  
}

var zeus = new ES6_SpaceShuttle('Jupiter');

console.log(zeus.targetPlanet); // 'Jupiter'

```

### 22. Use getters and setters to Control Access to an Object

With an object, you often want to obtain values of properties and set a value of a property within an object. These are called _getters_ and _setters._ They exist to hide some underlying code, as it should not be of concern for anyone using the class.

```js

class Thermostat {  
  // We create Thermostat using temperature in Fahrenheit.  
  constructor(temp) {  
    // _temp is a private variable which is not meant   
    // to be accessed from outside the class.  
    this._temp = 5/9 * (temp - 32);  
  }

// getter for _temp  
  get temperature(){  
    return this._temp;  
  }

// setter for _temp  
  // we can update temperature using Celsius.  
  set temperature(updatedTemp){  
    this._temp = updatedTemp;  
  }  
}

// Create Thermostat using Fahrenheit value  
const thermos = new Thermostat(76);  
let temp = thermos.temperature;

// We can update value using Celsius  
thermos.temperature = 26;  
temp = thermos.temperature;  
console.log(temp) // 26

```

### 23. Understand the Differences Between import and require

In the past, we could only use `require` to import functions and code from other files. In ES6 we can use `import`:

```js

// in string_function.js file  
export const capitalizeString = str => str.toUpperCase()

// in index.js file  
import { capitalizeString } from "./string_function"

const cap = capitalizeString("hello!");

console.log(cap); // "HELLO!"

```

### 24. Use export to Reuse a Code Block

You would normally `export` functions and variables in certain files so that you can import them in other files — and now we can reuse the code!

```js

const capitalizeString = (string) => {  
  return string.charAt(0).toUpperCase() + string.slice(1);  
}

// Named export  
export { capitalizeString };

// Same line named export  
export const foo = "bar";  
export const bar = "foo";

```

### 25. Use * to Import Everything from a File

If a file exports several different things, you can either import them individually, or you can use `*` to import everything from a file.

This is how you would import all the variables from the file in the previous exercise.

```js

import * as capitalizeStrings from "capitalize_strings";

```

### 26. Create an Export Fallback with export default

We looked at named exports in previous chapters and sometimes there might be a single function or a variable that we want to export from a file — `export default`, often used as a fallback export too.

```js

// In math_functions.js file

export default function subtract(x,y) {  
  return x - y;  
}

```

### 27. Import a Default Export

If you wish to import `export default` function from the previous exercise, this is how you would do it.

Note the absence of `{}` around the `subtract` function. Default exports don’t need them.

```js

// In index.js file  
import subtract from "math_functions";

subtract(7,4); // returns 3;

```

### 28. JavaScript ES6 Outro

If you’ve reached this far: congratulations! Most people who start courses never finish them, so you can be proud of yourself.

If you’re looking for your next challenge, you should check out Beau’s course on [Regex here!](https://scrimba.com/g/gregularexpressions?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article)

![Click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*wkctXSR70cUrFBAyiqK1Qw.png)
_[Click here to get to the course.](https://scrimba.com/g/gregularexpressions?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

Good luck! :)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ges6_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ges6_launch_article)_

