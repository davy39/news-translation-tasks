---
title: A guide to this in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-26T21:02:04.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-this-in-javascript-e3b9daef4df1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dJjQKiKhX-PbafQS
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ashay Mandwarya ?️??

  The this keyword hands-down is one of the most widely used and yet misunderstood
  in JavaScript. I’ll try to change that today.

  Let’s go back to the good old school days, when we learned about pronouns.


  Phelps is swimming fast...'
---

By Ashay Mandwarya ?️??

The `this` keyword hands-down is one of the most widely used and yet misunderstood in JavaScript. I’ll try to change that today.

Let’s go back to the good old school days, when we learned about pronouns.

> Phelps is swimming fast because _he_ wants to win the race.

Note the use of the pronoun “he”. We don’t directly address Phelps here but use the pronoun he to _refer to_ Phelps_._ Similarly JavaScript uses the `this` keyword as a referent to refer to the object in context _i.e the subject_.

Example:

![Image](https://cdn-media-1.freecodecamp.org/images/wTwrO4Y9ico1Ieh1NZV1HJK-PFVgeBlIq4rE)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make+" " +this.model);console.log(car.make+ " " +car.model);}}car.fullName();
```

In the above code, we have an object `car` which has the properties `make`, `model` and `fullName`. The value of `fullName` is a function which prints the full name of the car using 2 different syntaxes.

* Using `this` =&g`t; this.make+” “ +this.mod`el `the t`his refers to the object in context which `is c`ar `so this.ma`ke is effective`ly car.m`ake and so `is this.mo`del .
* Using dot notation, we can access the properties of objects, `car.make` & `car.model` .

### `this` is it!

Now that we have understood what is `this` and it’s most basic usage, let’s make some rules of thumb so we can always remember.

#### The JS `this` keyword refers to the object it belongs to.

```
var car={make:'....'func:()=>{console.log(this.make)}}
```

The `this` in the above snippet belongs to the object car.

#### It takes different values depending upon the usage

1. Inside a method.
2. Inside a function.
3. Alone.
4. In an event.
5. `call()`, and `apply().`

**Inside a method**

When `this` is used inside a method, it refers to the owner object.

Functions defined inside an object are called methods. Let’s take our car example again.

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make+" " +this.model);console.log(car.make+ " " +car.model);}}car.fullName();
```

`fullName()` here is a method. The `this` inside this method belongs to `car`.

**Inside a function**

`this` inside a function is a bit complicated. First thing to understand is that, like all objects have properties, likewise functions have properties too. Whenever that function is executed, it gets the `this` property, which is a variable with the value of the object that invokes it.

> _this_ is really just a shortcut reference for the “antecedent object” — the invoking object. — javascriptissexy.com

If the function is not invoked by an object then the `this` inside the function belongs to the global object, which is called window. In this case this will refer to the values defined in the global scope. Let’s see an example for better understanding:

```
var make= "Mclaren";var model= "720s"function fullName(){ console.log(this.make+ " " + this.model);}
```

```
var car = {    make:"Lamborghini",    model:"Huracán",    fullName:function () {    console.log (this.make + " " + this.model);    }}    car.fullName(); // Lmborghini Huracán    window.fullName(); // Mclaren 720S    fullName(); // Mclaren 720S
```

![Image](https://cdn-media-1.freecodecamp.org/images/gZYHKpKwNHIdbUskoYkA9lrq4hORsGZb0MrX)

Here `make, model` and `fullName` are defined globally, while `car` object has an implementation of `fullName` as well. When invoked by the `car` object this referred to the properties defined inside the object. On the other hand, the other two function callings are the same and return the globally defined properties.

**Alone**

When used alone not inside any function or object, `this` refers to the global object.

![Image](https://cdn-media-1.freecodecamp.org/images/kDPYXnkWNp3oS7XWmnz9A9UpO5BobzsU8Rac)

The `this` here refers to the global name property.

**In an event**

Events can be of any type, but for the sake of simplicity and clarity, let’s take a click event.

![Image](https://cdn-media-1.freecodecamp.org/images/vjRoyCEJjhZ6wuLoFwmJ8ZcUBs9q4CbCteLE)

Whenever a button is clicked and an event is raised, it can call another function to do a certain task based on the click. If `this` is used inside that function, it will refer to the element which raised the event. In the DOM, all the elements are stored as objects. That is why when an event is raised it refers to that element, because that _webpage element is actually an object inside the DOM_.

Example:

```
<button onclick="this.style.display='none'">  Remove Me!</button>
```

**call(), apply() & bind()**

* bind: allows us to set the `this` value on methods.
* call & apply: allow us to borrow functions and set the `this` value on function invocation.

Call, Bind and Apply are in themselves a topic of another post. They are very important, and explaining them here is not possible as we should know all about `this` to know the usage of these functions.

### The trickiest part

If understood well, `this` make our work easier in a way. But there are some cases where it is misunderstood.

#### Example 1.

![Image](https://cdn-media-1.freecodecamp.org/images/QECIynBJi8AJ0BtMQ9WrKxhdDHTn5PCYzYM1)

```
var car = {make:"Lamborghini",model:"Huracán",name:null,fullName:function () {this.name=this.make + " " + this.model;console.log (this.name);}}
```

```
var anotherCar={make:"Ferrari",model:"Italia",name:null}
```

```
    anotherCar.name= car.fullName();
```

We get an unexpected result here. We borrowed a method that uses `this` from another object, but the problem here is that the method is only assigned to `anotherCar` function but is actually invoked on `car` object. That’s why we get the result as Lamborghini and not Ferrari.

To resolve this, we use the `call()` method.

![Image](https://cdn-media-1.freecodecamp.org/images/j-mA-iIgaiRYxmuvvi0ToNl3GN5jUJGMxLjS)

Here the `call()` method calls `fullName()` on `anotherCar` object which originally does not have the `fullName()` function.

We can also see that, when we log the `car.name` and `anotherCar.name` we get the result for the latter not on former, which means that the function was indeed invoked on `anotherCar` and not on `car`.

#### Example 2.

![Image](https://cdn-media-1.freecodecamp.org/images/OxopdQevmTVOOZrzt4Q3FtJf9yjOUl6GYUd3)

```
var cars=[{ make: "Mclaren", model: "720s"},{make: "Ferrari",model: "Italia"}]
```

```
var car = {cars:[{make:"Lamborghini", model:"Huracán"}],fullName:function () {console.log(this.cars[0].make + " " + this.cars[0].model);}}var vehicle=car.fullName;vehicle()
```

In the above snippet we have a global object called cars and we have the same name object inside the car object. The `fullName()` method is then assigned to the vehicle variable which is then called. The variable belongs to the global object so `this` calls the global `cars` object instead of the `cars` object because of the context.

To resolve that we use `.bind()` function to solve the issue.

![Image](https://cdn-media-1.freecodecamp.org/images/MkmeqFWxySNTcnDJtc-HgSAzXzTejtvEg4d0)

Binding helps us with specifically setting the `this` value and hence the vehicle variable explicitly points to the car object and not the global object, so this lies in the context of the `car` object.

#### Example 3.

![Image](https://cdn-media-1.freecodecamp.org/images/ctGttd8h1qWNlNrursCjmjOcMzsGbNh5Z0lj)

```
var car = {cars:[{make:"Lamborghini",model:"Huracán"},{ make: "Mclaren", model: "720s"},{make: "Ferrari",model: "Italia"}],fullName:function(){this.cars.forEach(()=>{console.log (this.make + " " + this.model);})}}car.fullName();
```

In the above snippet, the `fullName()` calls upon a function which iterated through the cars array using `forEach`. Inside the `forEach` there is an anonymous function where this loses context. A function inside a function in JavaScript is called a `closure`. `Closures` are very important and widely used in JavaScript.

Another important concept playing a role here is `scope`. A variable inside a function cannot access variables and properties outside its `scope`. `this` inside the anon function cannot access `this` outside it. So `this` has nowhere to go but to point to global object. But there, no property is defined for `this` to access so `undefined` is printed.

A workaround for the above is that we can assign a variable the value of `this`, outside the anonymous function and then use it inside it.

![Image](https://cdn-media-1.freecodecamp.org/images/QnnxvDSMK09VH6ESN6P-Wg7f641JAiNZAYL5)

Here, the self variable contains the value of `this` which is used with the inner function thus giving us the output.

#### Example 4.

![Image](https://cdn-media-1.freecodecamp.org/images/KNmGVCmOuov8GWgyQax139PGvdfUBVmuPMz3)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function (cars) {cars.forEach(function(vehicle){console.log(vehicle +" "+ this.model);})}}car.fullName(['lambo','ferrari','porsche']);
```

This is a revisited example, in which `this` wasn't accessible so we preserved it's value by using a variable called self. Let's use arrow function to solve the same:

![Image](https://cdn-media-1.freecodecamp.org/images/ADnAYyjYS7xXBZqC6U7FM8PdB4AV3TNk40N1)

As you can see, using an arrow function in `forEach()` automatically solves the problem and we don’t have to do bind, or give the `this` value to some other variable. This is because arrow functions bind their context so `this` actually refers to the originating context, or the originating object.

#### Example 5.

![Image](https://cdn-media-1.freecodecamp.org/images/oKsJC9oHyb0etj1IqlWF3gZW1x6gSQYOPnAC)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make +" "+ this.model);}}var truck= {make: "Tesla",model: "Truck",fullName: function (callback) {console.log(this.make +" "+ this.model);callback();}}truck.fullName(car.fullName);
```

The above code consists of two identical objects, with one containing a **callback** function. A **callback** function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine.

Here, the truck object’s `fullName` method consists of a **callback** which is also invoked inside it**.** Our car object is as before. When we invoke the truck’s `fullName` method with the callback(argument) as the `fullName` method of the car object, we get output as `Tesla Truck` and `undefined undefined.`

After reading about `this` some of you might have gotten a hunch that `car.fullName` would print the model and make of the truck object, but to your disappointment, `this` again played a trick on us. Here the `car.fullName` is passed as an argument and is not actually invoked by the truck object. The callback invokes the car object method, but note that the actual call site for the function is the callback which binds this to the global object. It's a bit confusing, so read it again!

![Image](https://cdn-media-1.freecodecamp.org/images/ygRcPGWkKHvfGTrXGnqA5nHxZxZG1C1zKXhd)

Here to get clarity, we print `this` itself. We can see that the `this` of callback is given a global scope. So to get a result we create global `make` and `model` properties.

![Image](https://cdn-media-1.freecodecamp.org/images/lpWM9its6z5qKDw0jwWiD5GJtfqicPu-w3Dl)

Again, running the same code with global `make` and `model` properties we finally get the answer to the global `this`. This proves that `this` references the global object.

To get the results which we desire, the `car.fullName` result we will again use `bind()` to hard-bind the car object to the callback, which will make everything right again.

![Image](https://cdn-media-1.freecodecamp.org/images/rQ3vsBx5Wafjo7E01sHQiQdsrs1cXI4WKKcy)

### Solved!

No doubt that `this` is very useful, but has it's own pitfalls too. Hope I made it quite easy for you to understand. If you want more content simplified like this, follow me on Medium. Please leave your responses and share this if you liked it.

![Image](https://cdn-media-1.freecodecamp.org/images/Wdps8LMY6qHwRYPkdMh200uv4BmBLUPAM-PW)
_Google_

