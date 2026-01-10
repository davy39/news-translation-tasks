---
title: All you need to know to understand JavaScript’s Prototype
subtitle: ''
author: Shirshendu Bhowmick
co_authors: []
series: null
date: '2019-04-03T22:16:46.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-to-understand-javascripts-prototype-a2bff2d28f03
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bgfErxHxXBw-Ccm4OMu7_w.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Most of the time, JavaScript’s prototype confuses people who have just
  started to learn JavaScript — especially if they’re from a C++ or Java background.

  In JavaScript, inheritance works a bit differently compared to C++ or Java. JavaScript
  inheritan...'
---

Most of the time, JavaScript’s prototype confuses people who have just started to learn JavaScript — especially if they’re from a C++ or Java background.

In JavaScript, inheritance works a bit differently compared to C++ or Java. JavaScript inheritance is more widely known as “prototypical inheritance”.

Things become more difficult to understand when you also encounter `class` in JavaScript. The new `class` syntax looks similar to C++ or Java, but in reality, it works differently.

In this article, we will try to understand “prototypal inheritance” in JavaScript. We also look into the new `class` based syntax and try to understand what it actually is. So let’s get started.

First, we will start with the old school JavaScript function and prototype.

#### Understanding the need for prototype

If you have ever worked with JavaScript arrays or objects or strings, you have noticed that there are a couple of methods that are available by default.

For example:

```
var arr = [1,2,3,4];arr.reverse(); // returns [4,3,2,1]
```

```
var obj = {id: 1, value: "Some value"};obj.hasOwnProperty('id'); // returns true
```

```
var str = "Hello World";str.indexOf('W'); // returns 6
```

Have you ever wondered where these methods come from? You haven’t defined these methods on your own.

Can you define your own methods like this? You could say that you can in this way:

```
var arr = [1,2,3,4];arr.test = function() {    return 'Hi';}arr.test(); // will return 'Hi'
```

This will work, but only for this variable called `arr`. Let’s say we have another variable called `arr2` then `arr2.test()` will throw an error “TypeError: arr2.test is not a function”.

So how do those methods become available to each and every instance of array / string / object? Can you create your own methods with the same behavior? The answer is yes. You need to do it in the right way. To help with this, in comes JavaScript’s prototype.

Let’s first see where these functions are coming from. Consider the code snippet below:

```
var arr1 = [1,2,3,4];var arr2 = Array(1,2,3,4);
```

We have created two arrays in two different ways: `arr1` with array literals and `arr2` with `Array` constructor function. Both are equivalent to each other with some differences that don’t matter for this article.

Now coming to the constructor function `Array` — it is a predefined constructor function in JavaScript. If you open Chrome Developer tools and go to the console and type `console.log(Array.prototype)` and hit `enter` you will see something like below:

![Image](https://cdn-media-1.freecodecamp.org/images/LgPwy0jWfYBMdxUPmjdTAtDVZmyBkYFE-x8s)
_Fig: 1_

There you will see all the methods that we were wondering about. So now we get from where those functions are coming. Feel free to try with `String.prototype` and `Object.prototype`.

Let’s create our own simple constructor function:

```
var foo = function(name) { this.myName = name; this.tellMyName = function() {   console.log(this.myName); }}
```

```
var fooObj1 = new foo('James');fooObj1.tellMyName(); // will print Jamesvar fooObj2 = new foo('Mike');fooObj2.tellMyName(); // will print Mike
```

Can you identify a fundamental problem with the above code? The problem is we are wasting memory with the above approach. Note that the method `tellMyName` is the same for each and every instance of `foo`. Each time we create an instance of `foo` the method `tellMyName` ends up taking space in the system’s memory. If `tellMyName` is the same for all the instances it’s better to keep it in a single place and make all our instances refer from that place. Let’s see how to do this.

```
var foo = function(name) { this.myName = name;}
```

```
foo.prototype.tellMyName = function() {   console.log(this.myName);}
```

```
var fooObj1 = new foo('James');fooObj1.tellMyName(); // will print Jamesvar fooObj2 = new foo('Mike');fooObj2.tellMyName(); // will print Mike
```

Let’s check the difference with the above approach and previous approach. With the above approach, if you `console.dir()` the instances then you will see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/cCfrooHWD8qhcTEt6sqlXGI6hNVo-MT00Icv)
_Fig: 2_

Note that as a property of the instances we only have `myname`. `tellMyName` is defined under `__proto__`. I will come to this `__proto__` after sometime. Most importantly note that comparing `tellMyName` of both the instances evaluates to true. Function comparison in JavaScript evaluates true only if their references are the same. This proves that `tellMyName` is not consuming extra memory for multiple instances.

Let’s see the same thing with the previous approach:

![Image](https://cdn-media-1.freecodecamp.org/images/ZNgTtP4W2av-lJDUoRDdf7DmuWtnGumvbFUe)
_Fig: 3_

Note that this time `tellMyName` is defined as a property of the instances. It’s no longer under that `__proto__`. Also, note that this time comparing the functions evaluates to false. This is because they are at two different memory locations and their references are different.

I hope by now you understand the necessity of `prototype`.

Now let’s look into some more detail about prototype.

Each and every JavaScript function will have a `prototype` property which is of the object type. You can define your own properties under `prototype`. When you will use the function as a constructor function, all the instances of it will inherit properties from the `prototype` object.

Now let’s come to that `__proto__` property you saw above. The `__proto__` is simply a reference to the prototype object from which the instance has inherited. Sounds complicated? It’s actually not that complicated. Let’s visualize this with an example.

Consider the code below. We already know creating an Array with array literals will inherit properties from `Array.prototype`.

```
var arr = [1, 2, 3, 4];
```

What I just said above is “_The `__proto__` is simply a reference to the prototype object from which the instance has inherited_”. So `arr.__proto__` should be the same with `Array.prototype`. Let’s verify this.

![Image](https://cdn-media-1.freecodecamp.org/images/j8gJ-ryF1SW3bo7IWNnJoreG3Hp5vy1ZSIbx)
_Fig: 4_

Now we shouldn’t access the prototype object with `__proto__`. According to MDN using `__proto__` is highly discouraged and may not be supported in all browsers. The correct way of doing this:

```
var arr = [1, 2, 3, 4];var prototypeOfArr = Object.getPrototypeOf(arr);prototypeOfArr === Array.prototype;prototypeOfArr === arr.__proto__;
```

![Image](https://cdn-media-1.freecodecamp.org/images/WJ6FyFSXejZFU4QONss9YDsZqDLX64UWRYwM)
_Fig: 5_

The last line of the above code snippet shows that `__proto__` and `Object.getPrototypeOf` return the same thing.

Now it’s time for a break. Grab a coffee or whatever you like and try out the examples above on your own. Once you are ready, come back to this article and we will then continue.

#### Prototype chaining & Inheritance

In Fig: 2 above, did you notice that there is another `__proto__` inside the first `__proto__` object? If not then scroll up a bit to Fig: 2. Have a look and come back here. We will now discuss what that is actually. That is known as prototype chaining.

In JavaScript, we achieve Inheritance with the help of prototype chaining.

Consider this example: We all understand the term “Vehicle”. A bus could be called as a vehicle. A car could be called a vehicle. A motorbike could be called a vehicle. Bus, car, and motorbike have some common properties that's why they are called vehicle. For example, they can move from one place to another. They have wheels. They have horns, etc.

Again bus, car, and motorbike can be of different types for example Mercedes, BMW, Honda, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/LmR5EM367CwHz0BXh8o9jBeAPjbIjmfYjFNz)
_Fig: 6_

In the above illustration, Bus inherits some property from vehicle, and Mercedes Benz Bus inherits some property from bus. Similar is the case for Car and MotorBike.

Let's establish this relationship in JavaScript.

First, let's assume a few points for the sake of simplicity:

1. All buses have 6 wheels
2. Accelerating and Braking procedures are different across buses, cars, and motorbikes, but the same across all buses, all cars, and all motorbikes.
3. All vehicles can blow the horn.

```
function Vehicle(vehicleType) {  //Vehicle Constructor    this.vehicleType = vehicleType;}
```

```
Vehicle.prototype.blowHorn = function () {    console.log('Honk! Honk! Honk!'); // All Vehicle can blow Horn}
```

```
function Bus(make) { // Bus Constructor  Vehicle.call(this, "Bus");      this.make = make}
```

```
Bus.prototype = Object.create(Vehicle.prototype); // Make Bus constructor inherit properties from Vehicle Prototype Object
```

```
Bus.prototype.noOfWheels = 6; // Let's assume all buses have 6 wheels
```

```
Bus.prototype.accelerator = function() {    console.log('Accelerating Bus'); //Bus accelerator}
```

```
Bus.prototype.brake = function() {    console.log('Braking Bus'); // Bus brake}
```

```
function Car(make) {  Vehicle.call(this, "Car");  this.make = make;}
```

```
Car.prototype = Object.create(Vehicle.prototype);
```

```
Car.prototype.noOfWheels = 4;
```

```
Car.prototype.accelerator = function() {    console.log('Accelerating Car');}
```

```
Car.prototype.brake = function() {    console.log('Braking Car');}
```

```
function MotorBike(make) {  Vehicle.call(this, "MotorBike");  this.make = make;}
```

```
MotorBike.prototype = Object.create(Vehicle.prototype);
```

```
MotorBike.prototype.noOfWheels = 2;
```

```
MotorBike.prototype.accelerator = function() {    console.log('Accelerating MotorBike');}
```

```
MotorBike.prototype.brake = function() {    console.log('Braking MotorBike');}
```

```
var myBus = new Bus('Mercedes');var myCar = new Car('BMW');var myMotorBike = new MotorBike('Honda');
```

Allow me to explain the above code snippet.

We have a `Vehicle` constructor which expects a vehicle type. As all vehicles can blow their horns, we have a `blowHorn` property in `Vehicle`'s prototype.

As `Bus` is a vehicle it will inherit properties from `Vehicle` object.

We have assumed all buses will have 6 wheels and have the same accelerating and braking procedures. So we have `noOfWheels`, `accelerator` and `brake` property defined in `Bus`’s prototype.

Similar logic applies for Car and MotorBike.

Let’s go to Chrome Developer Tools -> Console and execute our code.

After execution, we will have 3 objects `myBus`, `myCar`, and `myMotorBike`.

Type `console.dir(mybus)` in the console and hit `enter`. Use the triangle icon to expand it and you will see something like below:

![Image](https://cdn-media-1.freecodecamp.org/images/1ST6FxGCAEigEAayuqNpwlUByhTlg3jDm4GR)
_Fig: 7_

Under `myBus` we have properties `make` and `vehicleType`. Notice the value of `__proto__` is prototype of `Bus`. All the properties of its prototype are available here: `accelerator`, `brake`, `noOfWheels`.

Now have a look that the first `__proto__` object. This object has another `__proto__` object as its property.

Under which we have `blowHorn` and `constructor` property.

```
Bus.prototype = Object.create(Vehicle.prototype);
```

Remember the line above? `Object.create(Vehicle.prototype)` will create an empty object whose prototype is `Vehicle.prototype`. We set this object as a prototype of `Bus`. For `Vehicle.prototype` we haven’t specified any prototype so by default it inherits from `Object.prototype`.

Let’s see the magic below:

![Image](https://cdn-media-1.freecodecamp.org/images/VD2RXaotYkPxWd3opcuthx8dX1olyo66LN1Z)
_Fig: 8_

We can access the `make` property as it is `myBus`'s own property.

We can access the `brake` property from `myBus`'s prototype.

We can access the `blowHorn` property from `myBus`'s prototype’s prototype.

We can access the `hasOwnProperty` property from `myBus`'s prototype’s prototype’s prototype. :)

This is called prototype chaining. Whenever you access a property of an object in JavaScript, it first checks if the property is available inside the object. If not it checks its prototype object. If it is there then good, you get the value of the property. Otherwise, it will check if the property exists in the prototype’s prototype, if not then again in the prototype’s prototype’s prototype and so on.

So how long it will check in this manner? It will stop if the property is found at any point or if the value of `__proto__` at any point is `null` or `undefined`. Then it will throw an error to notify you that it was unable to find the property you were looking for.

This is how inheritance works in JavaScript with the help of prototype chaining.

Feel free to try the above example with `myCar` and `myMotorBike`.

As we know, in JavaScript everything is an object. You will find that for every instance, the prototype chain ends with `Object.prototype`.

The exception for the above rule is if you create an object with `Object.create(null)`

```
var obj = Object.create(null)
```

With the above code `obj` will be an empty object without any prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/7NnMhJUMOYgjrMLyRW7HWIcJP4bNE0FvCtI7)
_Fig: 9_

For more information on `Object.create` check out the documentation on MDN.

Can you change the prototype object of an existing object? Yes, with `Object.setPrototypeOf()` you can. Check out the documentation in MDN.

Want to check if a property is the object’s own property? You already know how to do this.`Object.hasOwnProperty` will tell you if the property is coming from the object itself or from its prototype chain. Check out its documentation on MDN.

Note that `__proto__` also referred to as `[[Prototype]]`.

Now it’s time for another break. Once you are ready, come back to this article. We will then continue and I promise this is the last part.

#### Understanding Classes in JavaScript

According to MDN:

> JavaScript classes, introduced in ECMAScript 2015, are primarily syntactical sugar over JavaScript’s existing prototype-based inheritance. The class syntax _does not_ introduce a new object-oriented inheritance model to JavaScript.

Classes in JavaScript will provide better syntax to achieve what we did above in a much cleaner way. Let’s have a look into the class syntax first.

```
class Myclass {  constructor(name) {    this.name = name;  }    tellMyName() {    console.log(this.name)  }}
```

```
const myObj = new Myclass("John");
```

`constructor` method is a special type of method. It will be automatically executed whenever you create an instance of this class. Inside your class body. Only one occurrence of `constructor` is possible.

The methods that you will define inside the class body will be moved to the prototype object.

If you want some property inside the instance you can define it in the constructor, as we did with `this.name = name`.

Let’s have a look into our `myObj`.

![Image](https://cdn-media-1.freecodecamp.org/images/8YV1-cTjvrf4za0emIjWqvDfmmonmA1287vp)
_Fig: 10_

Note that we have the `name` property inside the instance that is `myObj` and the method `tellMyName` is in the prototype.

Consider the code snippet below:

```
class Myclass {  constructor(firstName) {    this.name = firstName;  }    tellMyName() {    console.log(this.name)  }  lastName = "lewis";}
```

```
const myObj = new Myclass("John");
```

Let’s see the output:

![Image](https://cdn-media-1.freecodecamp.org/images/dY8-i7joXX5hzVuLXbgN4vUENWqoParuuoJW)
_Fig: 11_

See that `lastName` is moved into the instance instead of prototype. Only methods you that you declare inside the Class body will be moved to prototype. There is an exception though.

Consider the code snippet below:

```
class Myclass {  constructor(firstName) {    this.name = firstName;  }    tellMyName = () => {    console.log(this.name)  }  lastName = "lewis";}
```

```
const myObj = new Myclass("John");
```

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/GIb2hzCV7C92-Z9L1oEHpr-tJgAFytgrQsdN)
_Fig: 12_

Note that `tellMyName` is now an arrow function, and it has been moved to the instance instead of prototype. So remember that arrow functions will always be moved to the instance, so use them carefully.

Let’s look into static class properties:

```
class Myclass {  static welcome() {    console.log("Hello World");  }}
```

```
Myclass.welcome();const myObj = new Myclass();myObj.welcome();
```

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/CpztRyj49N2Wss0c6-o2bqAa3x5dWA3blyC4)
_Fig: 13_

Static properties are something that you can access without creating an instance of the class. On the other hand, the instance will not have access to the static properties of a class.

So is static property a new concept that is available only with the class and not in the old school JavaScript? No, it’s there in old school JavaScript also. The old school method of achieving static property is:

```
function Myclass() {}Myclass.welcome = function() {  console.log("Hello World");}
```

Now let’s have a look at how we can achieve inheritance with classes.

```
class Vehicle {  constructor(type) {    this.vehicleType= type;  }  blowHorn() {    console.log("Honk! Honk! Honk!");  }}
```

```
class Bus extends Vehicle {  constructor(make) {    super("Bus");    this.make = make;   }  accelerator() {    console.log('Accelerating Bus');  }  brake() {    console.log('Braking Bus');  }}
```

```
Bus.prototype.noOfWheels = 6;
```

```
const myBus = new Bus("Mercedes");
```

We inherit other classes using the `extends` keyword.

`super()` will simply execute the parent class’s constructor. If you are inheriting from other classes and you use the constructor in your child class, then you have to call `super()` inside the constructor of your child class otherwise it will throw an error.

We already know that if we define any property other than a normal function in the class body it will be moved to the instance instead of prototype. So we define `noOfWheel` on `Bus.prototype`.

Inside your class body if you want to execute parent class’s method you can do that using `super.parentClassMethod()`.

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/cSH-VN7BReS2g5-2FkoDEY0dC6DxpeLrG4DD)
_Fig: 14_

The above output looks similar to our previous function based approach in Fig: 7.

#### Wrapping up

So should you use new class syntax or old constructor based syntax? I guess there is no definite answer to this question. It depends on your use case.

In this article, for the classes part I have just demonstrated how you can achieve prototypical inheritance classes. There is more to know about JavaScript classes, but that’s out of the scope of this article. Check out the documentation of classes on MDN. Or I will try to write an entire article on classes at some time.

If this article helped you in understanding prototypes, I would appreciate if you could applaud a little.

If you want me to write on some other topic, let me know in the responses.

You can also connect with me over [LinkedIn](https://www.linkedin.com/in/shirshendubhowmick/).

#### Thank You for Reading. :)

