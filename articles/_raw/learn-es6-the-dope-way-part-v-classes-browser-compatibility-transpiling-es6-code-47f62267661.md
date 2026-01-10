---
title: 'Learn ES6 The Dope Way Part V: Classes, Transpiling ES6 Code & More Resources!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-27T06:02:46.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mariya Diminsky

  Welcome to Part V of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Today we’ll explore ES6 classes, learn how to compile our code into ES5 for browser
  compatibility and learn about some ...'
---

By Mariya Diminsky

Welcome to Part V of **Learn ES6 The Dope Way**, a series created to help you easily understand ES6 (ECMAScript 6)!

Today we’ll explore ES6 _classes_, learn how to compile our code into ES5 for browser compatibility and learn about some awesome resources that will help us understand ES6 in greater depth! Adventure time! ❤

![Image](https://cdn-media-1.freecodecamp.org/images/1*EwyGlROHPNaLRBejoGqM3g.gif)

#### Classes in ES6

**Benefits:**

* A simpler way of dealing with JavaScript’s Prototype-Inheritance — it’s just ‘syntactical sugar’.
* You are still using the same object-oriented inheritance model.
* Similar to _class_ syntax in Java, Python, Ruby and PHP.
* Saves you a lot of typing.

**Beware:**

* Use can only invoke a _class_ via _new_, not a function call.
* Use _super()_ to call the _constructor_ of a parent class.
* A _class_ looks like an object but behaves like a function — because it is a function.
* _Class_ declarations are not hoisted as function declarations are.
* A name given to a _class_ expression is only local to the _class_ body.
* A _SyntaxError_ will be thrown if the class contains more than one occurrence of a _constructor_ method.
* While the members of an object literal are separated by commas, commas are illegal in _classes_ — this emphasizes the difference between them. Semicolons are only allowed for future syntax (possibly ES7), which may include properties cancelled by semicolons.
* In _derived classes_(explained later), _super()_ must be called first, before you can use the _this_ keyword. Otherwise it will cause a _ReferenceError_.
* _Static_ properties are properties of the _class_ itself. Thus while they can be inherited and accessed by directly calling the _class_ name, if you call an instance of the _class_(and store it within a variable) you will not be able to access it with that variable.

#### Creating a Class

So how do we create a _class_? Let us first review how objects are created in ES5 without the use of _classes_:

```js
function Bunny(name, age, favoriteFood) {
  this.name = name;
  this.age = age;
  this.favoriteFood = favoriteFood;
}
  
Bunny.prototype.eatFavFood = function () {
  console.log('\"Mmmm! Those ' + this.favoriteFood + ' were delicious\", said ' + this.name + ', the ' + this.age + ' year old bunny.');
};

var newBunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
newBunny.eatFavFood();
// "Mmmm! Those Raspberry Leaves were delicious", said Brigadier Fluffkins, the 3 year old bunny.

```

Now observe the same thing with ES6 _classes_:

```js
class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! Those ${this.favoriteFood} were delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

let es6Bunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
es6Bunny.eatFavFood();
// "Mmmm! Those Raspberry Leaves were delicious", said Brigadier Fluffkins the 3 year old bunny.

```

What are the main differences? Clearly the _class_ syntax looks like an object, but remember that actually it’s still a function and behaves so. Test it out yourself:

```js
typeof Bunny
// function
```

Another main difference is anything you want to store must be within a _constructor_ method. Any prototype method of the _class_ should be inside of that _class,_ but outside of the _constructor,_ without writing ‘._prototype_’, and in ES6 function syntax.

#### Twos Ways of Defining a Class & Prototype Inheritance

Now there are two main ways of defining a _class_ — the example above is one of the more common ways, a _class_ declaration. While a _class_ is indeed a function and function declarations are hoisted — meaning the function can be accessed no matter if it is called before it is declared — yet you cannot hoist a _class_ declaration. This is important to remember:

```js
// Normal function declaration
// called before it is declared and it works.
callMe(); // Testing, Testing.

function callMe() {
  console.log("Testing, Testing.")
}

// This is called after, as we would do in a function expression,
// and it works too!
callMe() // Testing, Testing.


// But with classes...You can't create an instance of a class 
// before creating it:
let es6Bunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
es6Bunny.eatFavFood();

class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! Those ${this.favoriteFood} were delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

// Instead we get this: Uncaught ReferenceError: Bunny is not defined
```

The reason for this limitation is that _classes_ can have an _extends_ clause — used for inheritance — whose value can be specified at a later time or may even depend on an inputted value or computation. Since expressions may sometime need to be evaluated another time, it makes sense for this evaluation not to be hoisted before all values are evaluated. Not doing so may cause errors in your code.

Still, it is possible to store an instance of a _class_ before it is created in a function for later use and evaluate it after the _class_ has been defined:

```js
function createNewBunny() { new Bunny(); }
createNewBunny(); // ReferenceError

class Bunny {...etc}
createNewBunny(); // Works!
```

The second way to define a class is a _class_ expression. As with function expressions, class _expressions_ can be named or anonymous. Be aware, these names are only local to the _class_ body and cannot be accessed outside of it:

```js
// anonymous:
const Bunny = class {
  etc...
};
const BunnyBurgerKins = new Bunny();

// named
const Bunny = class SurferBunny {
  whatIsMyName() {
    return SurferBunny.name;
  }
};
const BunnyBurgerKins = new Bunny();

console.log(BunnyBurgerKins.whatIsMyName()); // SurferBunny
console.log(SurferBunny.name); // ReferenceError: SurferBunny is not defined
```

There are two types of _classes_: The base _class —_ or the parent class — and the derived _class —_ the inherited subclass. Here _Bunny_ is the base class and _BelgianHare_ is the derived class since it has the _extends_ clause. Notice how simple the syntax for prototype inheritance is with _classes_:

```js
class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! That ${this.favoriteFood} was delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

class BelgianHare extends Bunny {
  constructor(favDrink, favoriteFood, name, age) {
    super(name, age, favoriteFood);
    this.favDrink = favDrink;
  }
  
  drinkFavDrink() {
    console.log(`\"Thank you for the ${this.favDrink} and ${this.favoriteFood}!\", said ${this.name} the happy ${this.age} year old Belgian Hare bunny.`)
  }
}

let newBelgHare = new BelgianHare('Water', 'Grass', 'Donald', 5);
newBelgHare.drinkFavDrink();
// "Thank you for the Water and Grass!", said Donald the happy 5 year old Belgian Hare bunny.
newBelgHare.eatFavFood();
// "Mmmm! That Grass was delicious", said Donald the 5 year old bunny.
```

The _super()_ function inside of the derived _class_, _BelgianHare_, gives us access to the _constructor_ in the base _class_, _Bunny_, so when we call the prototype methods from both _classes_(_drinkFavDrink()_ from the derived _class,_ and _eatFavFood()_ from the base _class_), they both work!

#### Browser Compatibility

Not all ES6 features are fully supported on all browsers as of yet. In the meantime stay updated by checking out these sites:

* View compatibility chart: [https://kangax.github.io/compat-table/es6/](https://kangax.github.io/compat-table/es6/)
* Enter any ES6 feature in manually: [http://caniuse.com/#search=const](http://caniuse.com/#search=const)

#### Transpiling ES6 Code

Since not all browsers support all ES6 features you need to transpile your ES6 code into a compiler such as _Babel_ or module bundler like _Webpack_.

Transpiling simply means taking out ES6 code and converting it into ES5 so it can be read by all browsers — like a safety precaution!

There are many transpiling tools, the most popular are also the ones that support the most ES6 features:

* _Babel.js_
* _Closure_
* _Traceur_

You can use any of of these, but out of the three listed, I would recommend _Babel_ for smaller projects. Please follow their simple steps for installing _Babel_ into your project via _Node_: [https://babeljs.io/](https://babeljs.io/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YHKpM73vm1u2fvrKgYcYYw.png)

For larger projects I recommend using _Webpack_. _Webpack_ does a lot of complicated things for you, including: transpiling code, SAS conversions, dependency management, and even replacing tools such as _Grunt_, _Gulp_ and _Browserify_. There is already an informative tutorial written on Webpack right over [here](https://medium.com/@dabit3/beginner-s-guide-to-webpack-b1f1a3638460#.mu2kgudga).

#### Resources

Check out these resources to learn and explore ES6 in greater depth:

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6QrITdqOjVWG9-e3nkLSA.png)

The Mozilla Developer Network (MDN) is a superb tool for learning about all ES6 concepts, actually anything JavaScript. For example, let’s learn more about _classes_: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

Babel.js has super useful article summarizing all our ES6 points into one: [https://babeljs.io/docs/learn-es2015/](https://babeljs.io/docs/learn-es2015/)

This guy is always fun to watch: [https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm](https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm)

And check out this exhaustive list of ES6 study resources: [https://github.com/ericdouglas/ES6-Learning](https://github.com/ericdouglas/ES6-Learning)

There are many, many more. Go forth my child, explore thy internet.

Remember, no matter how experienced you are — Google is your friend.

Congrats! You’ve made it through **Learn ES6 The Dope Way** Part V and now you’ve learned a clever way of using prototype inheritance through ES6 _classes_, understand that it’s important to _always_ transpile your code since not all browsers support _all_ features of ES6— either through _Babel.js_ for smaller projects or _Webpack_ for larger projects.

Keep your wisdom updated by liking and following. This is the last lesson in the **Learn ES6 The Dope Way** series! Congrats, you’ve made it!! Pat yourself in the back you did a great job!! I’m so proud of you! Yay!!!

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ecYe92TjNDCisDHLDH_4Q.gif)

**Thanks for reading ❤** Stay tuned for more JavaScript lessons underway!

**[Part I: const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Part II: (Arrow) => functions and ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Part III: Template Literals, Spread Operators & Generators!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Part IV: Default Parameters, Destructuring Assignment, and a new ES6 method!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Part V: Classes, Transpiling ES6 Code & More Resources!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

You can also find me on github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)

