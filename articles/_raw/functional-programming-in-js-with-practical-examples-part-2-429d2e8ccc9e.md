---
title: Functional Programming In JavaScript — With Practical Examples (Part 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-16T18:13:04.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U1TQD4tsM3JLZ-MfBH-vJA.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By rajaraodv

  In Part 1, we talked through: Functional Programming basics, Currying, Pure Functions,
  “Fantasy-land” specs, “Functors”, “Monads”, “Maybe Monads” and “Either Monads” via
  couple of examples.

  In this part, we’ll cover: Applicative, curryN ...'
---

By rajaraodv

[**In Part 1**](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.8dao66cag), we talked through: Functional Programming basics, Currying, Pure Functions, “Fantasy-land” specs, “Functors”, “Monads”, “Maybe Monads” and “Either Monads” via couple of examples.

**In this part, we’ll cover: Applicative, curryN function and “Validation Applicative”.**

> Thanks to FP gurus [Brian Lonsdorf](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined), [keithalexander](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined) and others for reviewing _??_

### _Example 3— Assigning Values To Potentially Null Objects_

_**FP Concepts Used: “Applicative”**_

_**Use Case:** Let’s say we want to give discount to the user if the user is logged in and if we are running promotion (i.e. discount exists)._

![Image](https://cdn-media-1.freecodecamp.org/images/1*qqkZuYVXrxIsyuJ5xTa_Yw.png)

_Let’s say we are using the **applyDiscount** method below. As you can imagine, applyDiscount might throw null errors if either the user (the left-hand side or the discount (the right-hand side) is null._

_`//Adds discount to the user object if BOTH user and discount exists.`_  
_`//Throws null errors if either user or discount is nullconst applyDiscount = (user, discount) => {    let userClone = clone(user);// use some lib to make a copy`_    
   _`    **userClone.discount = discount.code;**   return userClone;`_  
_`}`_

_Let’s see how we can solve this using “applicative”._

_**Applicative:**_

_Any Class that have a method “ap” and implements the Applicative spec is called an Applicative. Applicatives can be used in functions that are dealing with null values on both left-hand-side(user) and right-hand-side(discount) of the equation._

_It turns out “Maybe” Monads (and every Monads) also implement “ap” spec and hence are also “Applicatives” and not just Monads. So we can use “Maybe” Monads to deal with null at function level._

_Let’s see how we can solve make applyDiscount work using Maybe used as an “applicative”._

#### _**Step 1:** wrap our potential null values in Maybe Monads_

_`const maybeUser = Maybe(user);`_  
_`const maybeDiscount = Maybe(discount);`_

#### _**Step 2:** Rewrite the function and curry it so we can pass one param at a time._

_`//Rewrite the function and curry it so we can`_   
_`//pass one param at a time`_  
_`var applyDiscount = curry(function(user, discount) {`_       
       _`user.discount = discount.code;`_       
       _`return user;`_   
_`});`_

#### _**Step 3:** let’s pass the first argument(maybeUser) to applyDiscount via “map”._

_`//pass the first argument to applyDiscount via "map"`_  
_`**const maybeApplyDiscountFunc = maybeUser.map(applyDiscount);**//Note, since applyDiscount is "curried", and "map" will only pass 1 parameter, the return result (**maybeApplyDiscountFunc**) will be a Maybe wrapped "applyDiscount" function that now has maybeUser(1st param) in it's closure.**In other words, we now have a function wrapped in a Monad!**`_

#### _**Step 4: Deal With** maybeApplyDiscountFunc_

_At this stage maybeApplyDiscountFunc can be:_  
_1. If user actually exists, then maybeApplyDiscountFunc is a function wrapped inside a Maybe._  
_2. If the user does not exist, then maybeApplyDiscountFunc will be “Nothing” (subclass of Maybe)_

_If user doesn’t exist, then “Nothing” is returned and any further interaction with this are ignore completely. So if we pass 2nd argument, nothing happens. And also no Null errors are thrown._

_But in the case where the user actually exists, we can try to pass the 2nd argument to maybeApplyDiscountFunc via “map” to execute the function like below:_

_`maybeDiscount.map(maybeApplyDiscountFunc)! // PROBLEM!`_

_**Uh oh! “map” doesn’t know how to run function(**maybeApplyDiscountFunc) **when the function itself is inside a MayBe!**_

_That’s why we need a different interface to deal with this scenario. It turns out that’s “ap”!_

_**Step5:** Let’s recap “ap” function. “ap” method takes another Maybe monad and passes/applies the function it’s currently storing to that Maybe._

_So we can simply apply (“ap”) maybeApplyDiscountFunc to maybeDiscount instead of using “map” like below and it’ll work like a charm!_

_`maybeApplyDiscountFunc.**ap**(maybeDiscount)//Internally it is doing the following because applyDiscount is store in the this.val of maybeApplyDiscountFunc wrapper:`_  
_`maybeDiscount.map(applyDiscount)//Now, if maybeDiscount actually has the discount, then the function is is run.If maybeDiscount is Null, then nothing happens.`_

> _FYI: Apparently there is a change in the FL spec, The old version has (eg): `Just(f).ap(Just(x))` (where `f` is a function and `x` is a value) but the new version would have you write `Just(x).ap(Just(f))`But the implementations mostly haven’t changed yet. Thanks [keithalexander](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined)_

_To summarize, if you have a function that deals with multiple parameters that might all be null, you curry it first, then put it inside a Maybe. Further, also put all params in a Maybe and then use “ap” to run the function._

### _curryN function_

_We are familiar with “curry”. It simply converts a function that takes multiple arguments to take them one-by-one._

_`**//Curry Example:**`_  
_`const add = (a, b) =>a+b;const curriedAdd = R.curry(add);const add10 = curriedAdd(10);//pass the 1st argument. Returns a function that takes 2nd (b) parameter.//run function by passing 2nd argument`_  
_`add10(2) // -> 12 //internally runs "add" with 10 and 2.`_

_But instead of adding just two numbers, what if the **add** function can sum up all the numbers passed to it as an argument?_

_`const add = (...args) => R.sum(args); //sum all the numbers in args`_

_We can still curry it by limiting number of args using **curryN** like below:_

_`**//curryN example**`_  
_`const add = (...args) => R.sum(args);//CurryN Example:`_  
_`const add = (...args) => R.sum(args);const add3Numbers = R.**curryN**(3, add);`_  
_`const add5Numbers = R.**curryN**(5, add);`_  
_`const add10Numbers = R.**curryN**(10, add);add3Numbers(1,2,3) // 6`_  
_`add3Numbers(1) // returns a function that takes 2 more params.`_  
_`add3Numbers(1, 2) // returns a function that take 1 more param.`_

#### _Using “curryN” to wait for number of function calls_

_Let’s say we want to write a function that only logs if we call it 3 times (and ignore the 1st and 2nd call). Something like below:_

_`//impure`_  
_`let counter = 0;`_  
_`const logAfter3Calls = () => {`_  
 _`if(++counter == 3)`_  
   _`console.log('called me 3 times');`_  
_`}logAfter3Calls() // Nothing happens`_  
_`logAfter3Calls() // Nothing happens`_  
_`logAfter3Calls() // 'called me 3 times'`_

_We can simulate that using curryN like below._

_`//Pure`_  
_`const log = () => {`_  
   _`console.log('called me 3 times');`_  
_`}**const logAfter3Calls = R.curryN(3, log);**//call`_  
_`**logAfter3Calls('')('')('')**//'called me 3 times'//Note: We are passing '' to satisfy CurryN that we are passing some parameter.`_

> _**Note: We’ll be using this technique in the Applicative validation.**_

### _Example 4— Collecting And Displaying Multiple Errors_

_Topics covered: **Validation (aka “Validation Functor”, “Validation Applicative”, “Validation Monad”)**._

> _**Validations** are commonly referred as **Validation Applicative** because it is commonly used for validation using it’s “ap”(apply) function._

_**Validations** are similar to **Either Monads** and used to work with composing multiple error-throwing functions. But unlike with Either Monad, where we typically use its “chain” method to compose, in Validation Monads, we typically use “ap” method to compose. And unlike either’s “chain” method, where we only collect the 1st error, **“ap” method, especially in Validation Monads allows us to collect all the errors in an Array**._

_They are typically used in form validation where we may want to show all the errors at the same time._

_**Use case:** We have a sign up form that validates username, password and email using 3 functions(isUsernameValid, isPwdLengthCorrect and ieEmailValid. We need to show all 1, 2 or 3 errors if they all occur at the same time._

![Image](https://cdn-media-1.freecodecamp.org/images/1*qru9EDCwqmj-o2FgtVqAQg.png)
_In order to show multiple errors, use “Validation” Functor_

_OK, let’s see how to implement it using “Validation Applicative”._

> _We’ll use data.validation lib from [folktalejs](https://github.com/folktale/data.validation) because ramda-fantasy doesn’t implement it yet._

_Similar to “Either” Monad, it has two constructors: **Success** and **Failure**. These are like subclasses that each implement Either’s specs._

_**Step1:** In order to use Validation, all we need to do is to wrap valid values and errors inside **Success** and **Failure** constructors (i.e. create instances of those classes)._

_`const Validation = require('data.validation') //from [folktalejs](https://github.com/folktale/data.validation)`_  
_`const Success = Validation.Success`_  
_`const Failure = Validation.Failure`_  
_`const R = require('ramda');**//Instead Of:**`_  
_`function isUsernameValid(a) {`_  
    _`return /^(0|[1-9][0-9]*)$/.test(a) ?`_   
           _`["Username can't be a number"] : a`_  
_`}**//Use:**`_  
_`function isUsernameValid(a) {`_  
    _`return /^(0|[1-9][0-9]*)$/.test(a) ?`_   
         _`         **Failure**(["Username can't be a number"]) : **Success**(a)`_  
_`}`_

> _**Repeat the process for ALL error throwing validation functions.**_

_**Step 2:** Create a dummy function to hold validation success._

_`const returnSuccess = () => 'success';//simply returns success`_

_**Step 3: Use curryN to repeatedly apply “ap”**_

_The problem with “ap” is that the left-hand side should be a functor (or a monad) containing **function**._

_For example, let’s say we want to repeatedly apply “ap” like below. It will only work if monad1 contains a function. And the result of monad1.ap(monad2) i.e. **resultingMonad** is also a monad with a function so that we can “ap” to monad3._

_`**let finalResult = monad1.ap(monad2).ap(monad3)**//Can be rewritten as:`_  
_`let resultingMonad = monad1.ap(monad2)`_  
_`let **finalResult** = resultingMonad.ap(monad3)**//will only work if: monad1 has a function and monad1.ap(monad2) results in another monad (resultingMonad) with a function**`_

> _Generally speaking, we need 2 monads that has functions in order to apply “ap” twice._

_In our case, we have 3 functions that we need to apply._

_Let’s say we did something like below._

_`Success(returnSuccess)`_  
        _`.ap(isUsernameValid(username)) //works`_  
        _`.ap(isPwdLengthCorrect(pwd))//wont work`_  
        _`.ap(ieEmailValid(email))//wont work`_

_The above won’t work because Success(returnSuccess).ap(isUsernameValid(username)) will result in a value. And we can no longer continue to do “ap” on 2nd and 3rd function._

_Enter curryN._

_We can use curryN to keep returning function until it is called “N” number of times._

_So we can simply do:_

_`//3 coz we are calling "ap" 3 times.`_  
_`let success = R.curryN(3, returnSuccess);`_

_Now, the curried **success keeps returning function 3 times.**_

_`function validateForm(username, pwd, email) {`_  
    _`//3 coz we are calling "ap" 3 times.`_  
    _`let success = R.curryN(3, returnSuccess);    return Success(success)// default; used for 3 "ap"s`_  
        _`.ap(isUsernameValid(username))`_  
        _`.ap(isPwdLengthCorrect(pwd))`_  
        _`.ap(ieEmailValid(email))`_  
_`}`_

_Putting it all together:_

_**If you liked the post by clicking on the ? it below and sharing it on Twitter! Thanks for reading!** ??_

### _My Other Posts_

_**LATEST:** [_The Inner workings of the Browser — for JavaScript & Web Developers_](https://medium.com/@rajaraodv/the-inner-workings-of-the-browser-for-javascript-web-developers-course-d26f11270f41) _**Use code: INNER15 and get 50% off!**__

#### _Functional Programming_

1. _[JavaScript Is Turing Complete — Explained](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)_
2. _[Functional Programming In JS — With Practical Examples (Part 1)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)_
3. _[Functional Programming In JS — With Practical Examples (Part 2)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.mmpv20wsv)_

#### _ES6_

1. _[5 JavaScript “Bad” Parts That Are Fixed In ES6](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)_
2. _[Is “Class” In ES6 The New “Bad” Part?](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)_

#### _WebPack_

1. _[Webpack — The Confusing Parts](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)_
2. _[Webpack & Hot Module Replacement [HMR]](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg)_ _(under-the-hood)_
3. _[Webpack’s HMR And React-Hot-Loader — The Missing Manual](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)_

#### _Draft.js_

1. _[Why Draft.js And Why You Should Contribute](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)_
2. _[How Draft.js Represents Rich Text Data](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)_

#### _React And Redux :_

1. _[Step by Step Guide To Building React Redux Apps](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)_
2. _[A Guide For Building A React Redux CRUD App](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz)_ _(3-page app)_
3. _[Using Middlewares In React Redux Apps](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)_
4. _[Adding A Robust Form Validation To React Redux Apps](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)_
5. _[Securing React Redux Apps With JWT Tokens](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)_
6. _[Handling Transactional Emails In React Redux Apps](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)_
7. _[The Anatomy Of A React Redux App](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)_

#### _Salesforce_

1. _[Developing React Redux Apps In Salesforce’s Visualforce](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)_

