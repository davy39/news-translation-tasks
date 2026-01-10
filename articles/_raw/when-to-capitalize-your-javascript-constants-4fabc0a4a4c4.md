---
title: When to capitalize your JavaScript constants
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-03-08T18:14:14.000Z'
originalURL: https://freecodecamp.org/news/when-to-capitalize-your-javascript-constants-4fabc0a4a4c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XhNtWWMZPXU--QwrKShjpQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: variables
  slug: variables
seo_title: null
seo_desc: Many JavaScript style guides suggest capitalizing constant names. Personally,
  I rarely see this convention used where I thought it should be. This was because
  my definition of a constant was a bit off. I decided to do a bit of digging and
  become a bi...
---

Many JavaScript style guides suggest capitalizing constant names. Personally, I rarely see this convention used where I thought it should be. This was because my definition of a constant was a bit off. I decided to do a bit of digging and become a bit more familiar with this convention.

#### How do we define the term “constant”?

In programming, a constant it something that doesn’t change.

> [It is a value that cannot be altered by the program during normal execution](https://en.wikipedia.org/wiki/Constant_(computer_programming)).

So, does JavaScript gives us a way to declare a value that can’t be changed? Before we answer this, let’s look at the roots of this convention.

#### The capitalization convention has roots in C

C is a compiled language. This means that another program converts all of your code into machine code before it runs.

JavaScript, on the other hand, is an interpreted language. An interpreter reads your code, line-by-line, as it runs.

The difference between compilation and interpretation plays a role in how we declare constant values in C.

In C, I can declare a variable like this:

`int hoursInDay = 24;`

Or, a constant like this:

`#define hoursInDay 24`

The second example is called a **symbolic constant**. Symbolic constants can be a sequence of characters, a numeric constant, or a string. These are also called primitive values. The primitive values in JavaScript are strings, numbers, booleans, null, undefined, symbol (not to be confused with symbolic constants) and big int.

Now, let’s revisit compilation.

Before compilation, there is a pre-compilation phase. Here, the pre-compiler replaces all instances of symbolic constants with the respective value. The compiler never knows that the programmer wrote `hoursInDay`. It only sees the number `24`.

Capitalization helps the programmer see these truly constant values.

`#define HOURS_IN_DAY 24`

#### JavaScript constants are different than symbolic constants

Before ES6, we stored most values in variables, even those values that you wanted to remain constant.

Capitalization helped us see values we wanted to remain constant.

```js
var HOURS_IN_DAY = 24;
var hoursRemaining = currentHour - HOURS_IN_DAY;
var MY_NAME = 'Brandon';
MY_NAME = ... // oops don't want to do this.
```

ES6 introduced the declaration `const` which isn’t a “constant” in the purest sense.

ES6 added the terms `const` and `let` as ways to create variables with different intentions.

With those two terms, you may think that we either:

1. don’t need to capitalize anything since we can clearly see which variables are intended to remain the same, or
    
2. we should capitalize everything that we declare with `const`.
    

By definition, `const` creates a constant that is a read-only reference to a value. This does not mean the value it holds is immutable. It only says that [the variable identifier cannot be reassigned](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).

In other words, some `const` references can change.

```js
const firstPerson = {
  favoriteNumber: 10,
};
const secondPerson = firstPerson;
console.log(secondPerson.favoriteNumber); //10
firstPerson.favoriteNumber +=1;
console.log(secondPerson.favoriteNumber); //11
```

The above example shows that the declaration `const` doesn’t ensure that the variable is immutable.

`const` only prevents us from trying to reassign the variable name. It doesn’t stop the object property from changing. Remember: objects are pass-by-reference.

```js
// "TypeError: Assignment to constant variable."secondPerson = 'something else';
const secondPerson = 'Me'
secondPerson = 'something else';
```

So, for JavaScript, we have to go beyond merely looking for a `const` declaration. We need to ask two questions to determine if a variable is a constant:

1. Is the value of the variable primitive?
    
2. Do we intend to keep the variable name pointing at the same value throughout our program?
    

If the answer is yes to both, we should declare the variable with `const` and may capitalize the name.

Notice I said “may.” The spirit of this convention comes from different languages that had actual constants. JavaScript doesn’t. At least in the purest sense. This may be why you see this convention less often than you might expect. [Airbnb has a great section in their style guide with their take here.](https://github.com/airbnb/javascript/#naming--uppercase)

The **key takeaway** is to recognize defining a constant in JavaScript has to include the programmer's intentions.

In addition, not every convention from one language makes sense in a different language. Finally, I can only imagine many conventions were used long before IDEs had the capabilities they have today. I’m convinced my IDE takes pleasure in telling me I’m wrong. It happens a lot.

Thanks for reading!

woz

Follow me on [Twitter.](https://twitter.com/Brandonwoz)

#### Notes

* You may wonder why I didn’t use `PI` in any of these examples. Acronyms– especially two-letter acronyms–tend to be either always capitalized or always lowercase by convention.
