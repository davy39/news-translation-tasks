---
title: Unit Testing Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T22:38:00.000Z'
originalURL: https://freecodecamp.org/news/unit-tests-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb3740569d1a4ca33b2.jpg
tags:
- name: toothbrush
  slug: toothbrush
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: "Unit testing is a type of testing which is found at the bottom of the software\
  \ testing pyramid. It involves breaking the codebase down into smaller parts (or\
  \ units) and testing those in isolation. \nDepending on the type of programming\
  \ language (or pa..."
---

Unit testing is a type of testing which is found at the bottom of the software testing pyramid. It involves breaking the codebase down into smaller parts (or units) and testing those in isolation. 

Depending on the type of programming language (or paradigm) these can be against anything you define as a unit, although the most common practice is against functions.

### **Why do it?**

* **Protection** - Unit testing protects against introducing new or old bugs for defensive programming
* **Confidence** - You can add changes, or reuse or refactor code (both very common) and be sure you haven’t added a bug
* **Documentation** - Unit testing documents the behavior and flow of code so its easy for someone new to the code to understand it
* **Isolation** - It isolates a module from the entire feature. This approach forces you to think of a module by itself, and ask what is its job?
* **Quality** - As unit testing forces you to think about and use your own API, it enforces good/extendable interfaces and patterns. It can point out any tight coupling or over-complexity which should be addressed. Bad code is usually much harder to test
* **Industry Standard** - Unit testing is a common discipline these days, and is a requirement for a large portion of software companies
* **Fewer bugs** - Substantial research suggests that applying testing to an application can reduce production bug density by 40% — 80%.

### **Example (in JavaScript)**

Suppose there is a function written in file **add.js**

```javascript
var add = function(number1, number2){
  return number1 + number2;
}
```

Now, in order to write unit test of this particular function we can use testing tools like [mocha](http://mochajs.org/):

```javascript
const mocha = require('mocha')
const chai = require('chai')  // It is an assertion library
describe('Test to check add function', function(){
  it('should add two numbers', function(){
    (add(2,3)).should.equal(5)  //Checking that 2+3 should equal 5 using the given add function
  });
});
```

### **Test-Driven Development**

Unit testing is a key feature of the test-driven development (TDD) approach to software development. 

In this approach, code for specific features or functions is written through the repeated use of a very short cycle. 

First, the developer writes a set of automated unit tests and ensures that they fail initially. Next, the developer implements the bare minimum amount of code required to pass the test cases. 

Once it has been validated that the code is behaving as expected, the developer then goes back and refactors code to adhere to any relevant coding standards.

## More info on Unit Tests:

* [An introduction to unit testing in Python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/)
* [An introduction to Jasmine unit testing](https://www.freecodecamp.org/news/jasmine-unit-testing-tutorial-4e757c2cbf42/)
* [How to unit test your first Vue.js component](https://www.freecodecamp.org/news/how-to-unit-test-your-first-vue-js-component-14db6e1e360d/)

## More on Test-Driven Development:

* [A practical intro to Test-Driven Development](https://www.freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b/)
* [TDD: what it is, and what it's not](https://www.freecodecamp.org/news/test-driven-development-what-it-is-and-what-it-is-not-41fa6bca02a2/)
* [A quick intro to TDD with Jest](https://www.freecodecamp.org/news/a-quick-introduction-to-test-driven-development-with-jest-cac71cb94e50/)
* [Why TDD is worth your time](https://www.freecodecamp.org/news/test-driven-development-i-hated-it-now-i-cant-live-without-it-4a10b7ce7ed6/)

