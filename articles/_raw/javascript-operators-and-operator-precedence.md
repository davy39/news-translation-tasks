---
title: JavaScript Operators and Operator Precedence – Beginner's Guide
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2023-03-20T21:15:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-operators-and-operator-precedence
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/JavaScript_Operator_precedence.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "A few months ago, I attempted to solve a math problem in my head before\
  \ writing it in JavaScript. It was then that I received the most stunning revelation\
  \ of my career, which was both shocking and eye-opening. \nSo what did I attempt\
  \ to do? I made the..."
---

A few months ago, I attempted to solve a math problem in my head before writing it in JavaScript. It was then that I received the most stunning revelation of my career, which was both shocking and eye-opening. 

So what did I attempt to do? I made the following mental arithmetic calculations:

```js
2 + 3 * 4
```

Naturally, my response was `20`, so I proceeded to code it. But when the output on the console revealed the answer to be `14`, it completely altered how I thought about JavaScript.

But how did I perform arithmetic operations before JavaScript? Well, I just entered the relevant numbers into a calculator and waited for my results. Easy! 

How inaccurate my mental model was about how mathematical operations are carried out in JavaScript was made clear by mentally performing the calculations.

As a JavaScript developer, you may have encountered this type of "error" when doing mathematics in your head versus how JavaScript or your calculator does it. It's not magic, but rather a simple concept known as **Operator Precedence.**

In this article, we'll go over what operators are and how operators in JavaScript are parsed. This will help you not only with JavaScript but also with other programming languages if you choose to learn them.

## What are Operators?

Operators are special symbols used to perform operations on operands, which can be variables or values. For example, in 13 / 3, the "/" division symbol serves as the operator, while "13" and "3" serve as operands.

A value or variable on which operators conduct operations is known as an operand. This is a little exercise to put yourself to the test. Examine the code snippet below and distinguish between operators and operands:

```js
1. 2 + 5 * 3
2. (12 + 4) / 4
3. 20 ** 4 - 4

/* ANSWERS
  Operators from the above operations are "+", "*" , "()", "**", "/" and "-"
  
 The numbers are the operands of the operation
 
 */
```

## Types of Operators in JavaScript

Not all operators in JavaScript perform arithmetic operations. Rather, operators vary in their functions. In this section we will look at some of the different types of operators and how they work in JavaScript.

### Arithmetic Operators

An arithmetic operator is used to perform basic mathematical operations. It takes numerical values as operands, which can be variables or literals, and returns a value.

 Arthmetic operators in JavaScript include:

* Addition (+) 
* Subtraction (-)
* Multiplication (*)
* Exponentiation (**)
* Modulus (%)
* Decrement (--)
* Increment (++)
* Division (/)

The following code snippet contains example operations that use the arithmetic operators:

```js
2 + 3   // ANSWER: 5. This adds the operands.

10 * 5 // ANSWER: 50. This multiplies the operands.

10 % 3 // ANSWER: 1. This returns the remainder of dividing the two operands.

10++   // ANSWER: 11. This increases the operands by 1.

100-- // ANSWER: 9. This decreases the operands by 1

10 ** 3 // ANSWER: 1000. This multiplies the operands by the power of 3 ( 10 * 10 * 10)

10 - 3 // ANSWER: 7. This substracts the operands

10 / 5 //ANSWER: 2. This divides 10 by 5
```

### Comparison Operators

A comparison operator compares two operands and returns a Boolean (true or false) value as a result of the comparison.

The JavaScript comparison operators are as follows:

* Equals (==)
* Not Equal (!=)
* Strict Equal (===)
* Strict Not Equal (!==)
* Greater than (>)
* Greater than or equal (>=)
* Less than (<)
* Less than or equal (<=)

The code snippet below provides some examples of how the comparison operators operate:

```js
10 == 10  // ANSWER: True. It returns true because 10 is equal to 10.

10 != 7 // ANSWER: True. It returns a Truthy value because 10 is not equal to 7.

10 == "10" //ANSWER: True. It returns true because 10 equals 10.

10 === "10" //ANSWER: False. This returns false because 10, which is of type number, is not equal to "10" which is of type string. It compares them strictly by their values and by their type.

10 !== "10" // ANSWER: True. It returns a Truthy value because 10, which is of type number, is not equal to "10", which of type string.

10 > 30  //ANSWER: False. It returns false because 10 is not greater than 30.

10 < 50 //ANSWER: True. This returns a truthy value because 10 is less than 50.

10 >= 70  //ANSWER: False. This will return a falsly value because 10 is not greater than 70, nor is it equal to 70.

10 <= 34 //ANSWER: True. This is true because 10 is less than 34 (even though it's not equal to 34 - it's "less than or equal to").

```

### Assignment Operators

Based on the value of its right operand, an assignment operator assigns a value to its left operand. The most fundamental application is the use of the assignment operator (=) to assign a value to a variable. It essentially assigns the value of one operand to another.

The code snippet below provides some examples of how the assignment operator works:

```js
const author = "Franklin"

const platform = "Freecodecamp"

const age = 78

```

Let's look at some further assignment operator examples:.

* Assignment (=)
* Addition Assignment (+=)
* Subtraction Assignment (-=)
* Division Assignment (/=)
* Multiplication Assignment (*=)
* Exponentiation Assignment (**=)
* Modulus Assignment (%=)

It's important to remember that when employing assignment operators other than the "=" operator—which I like to refer to as "arthmetic assignments"—that they also carry out an arthmetic operation before assigning the value to the operand. 

To see an example of it in action, look at the code below:

```js
let people = 20;

people += 20

console.log(people) // OUTPUT: 40

let cars = 30

cars -= 20

console.log(cars) //OUTPUT: 10
```

We can see from the code excerpt above that the arthimetic operations were first performed on the operands before they were assigned, using the appropriate arithmetic operators. 

The "arithmetic assignments" basically operate as follows: JavaScript first executes the arithmetic operation, then it assigns the value of the operation to the operand (variable).

After seeing how that operates, let's learn more about the various operators and how to use them:

```js
let result = 400;  //The Assignment operator was used to assign the value 400 to the variable result.

result += 20; 
consle.log(result)  //OUTPUT: 420. The value of the left operand was added to 20 and the value assigned to the left operand. (400 + 20)

result -= 20; 
consle.log(result)  //OUTPUT: 400. The value of the right operand was subtracted from the left operand the value assigned to the left operand. (420 - 20)

result *= 10 
consle.log(result)  //OUTPUT: 4000. The values of both operands are multiplied and the value from the operation is assigned to the left operand.

result /= 10; 
consle.log(result)  //OUTPUT: 400. The left operand is divided by 10 and the value from the operation is assigned to the left operand.

result %= 21;
consle.log(result)  //OUTPUT: 21. The left operand is divided by 21 and the remainder from the operation is assigned to the left operand.

result **= 2; 
consle.log(result)  //OUTPUT: 440. The left operand is raised by the power of 2 and the value is assigned to the left operand.
```

Let's move on to the next type of operator now that we have seen how the assignment operators function and how we may use them.

### Logical Operators

When used with boolean values, a logical operator produces a boolean value (true or false), otherwise it returns the value of one of the operands. Logical operators are used to check and determine the logic between two or more operands.

Although they can be difficult to understand, let's go over the operators and see how they function:

* OR (| |)
* AND (&&)
* NOT (!)

Examples of the operators in use are provided below:

```js
// USING THE AND(&&) OPERATOR

let canDrive = true;
let hasLicense = false;

const readyToDrive = canDrive && hasLicense;

console.log(readyToDrive) //OUTPUT: false
```

With the help of the code snippet above, we were able to construct a logic that determines whether a person is qualified to drive if they possess a driver's license and have driving experience. Both requirements must be satisfied before the person can pass the eligibility test.

The AND (&&) operator determines this because if one of the requirements is false, the operation's result will also be false. The operation cannot produce a truthy value unless both values are true:

```js
// USING THE AND(&&) OPERATOR

let canDrive = true;
let hasLicense = true;

const readyToDrive = canDrive && hasLicense;

console.log(readyToDrive) // OUTPUT: true
```

Next, given the identical scenario as earlier, let's investigate how we can use the OR(||) operator:

```js
// USING THE OR(||) OPERATOR

let canDrive = true;
let hasLicense = false;

const readyToDrive = canDrive || hasLicense;

console.log(readyToDrive) // OUTPUT: true
```

As an illustration, the eligibility regulations were changed to permit those who lack a license to drive as long as they are capable of doing so. 

We created a logic that tests this using the OR (||) operator. If one of the operands is a true value, the operation returns true, indicating that in this case the person has passed the eligibility test and is permitted to drive.

You might find it difficult to determine whether an operation returns true or false when using logical operators, so I made a little cheat sheet you can memorize and refer to whenever you get stuck:

```js
// AND(&&) Operator cheatsheet.

true && false = false;
false && false = false;
true && true = true
```

```js
// OR(||) Operator cheatsheet.

true || false = true;
false || false = false;
true || true = true
```

If the above is too long for you to memorize, here is another cheat sheet that is as simple:

```js
false && anything = false;
true || anything = true;
```

Hopefully, these little tips will serve as a reference as you utilize the logical operators in JavaScript.

Check out the code sample below for an example of how to use the NOT(!) operator, which is the last logical operator on the list:

```js
const author = "Franklin"

if (author != "Franklin) {
    console.log("This is not the author")
}
```

We created a basic program from the above code snippet that checks the author of an article or book and outputs a message if the author does not match the original author of the book. The NOT (!) operator is typically combined with other operators to create useful operations.

You can also use it to determine whether a value is true or false by inverting a Boolean value. Let's take a look at how that works below, using the driving eligibility test scenario:

```js
// USING THE NOT(!) OPERATOR

let canDrive = true;
let hasLicense = false;

if (!canDrive && !hasLicense) {
     console.log("Sorry, you are not eligible to drive")
}

//OUTPUT: "Sorry, you are not eligible to drive"
```

Let us break down the logic. First, we have a person who knows how to drive but does not have a driver's license, which is required by law for a person to be eligible to drive.

We created logic to ensure that if a person lacks either of the two qualities, they are not permitted to drive. The preceding logic can be translated as follows:

"If a person CANNOT drive and DOES NOT have a driver's license, they are not allowed to drive".

Because the variables declared `canDrive` is `true` so the `!canDrive` inverts to `false` and the `hasLicense` is `false`, it inverts to `true`.

So how does it end up being false? Remember our cheatsheet from earlier? We can use it to check the outcome of the operation.

`false` && `true` will be `false`.

If you have read this far into the article, congratulations on your new knowledge of JavaScript operators. If you would like to explore further and see more types of operators, here is a link to an [MDN resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators). Operators are crucial in our day-to-day activities with JavaScript, so learning about them is important.

Now we can go on to the next section of this article where you will learn how you can utilize several operators in an operation and how JavaScript calculates this operation.

## Operator Precedence in JavaScript

The concept of operator precedence describes how operators are compared to one another throughout an operation. Operators that have higher precedence are given a higher priority than the operators with lower precedence.

Aside from writing basic logic in JavaScript every day, we spend about half of our time writing complex mathematical operations, logical operations, and occasionally we even translate some physics and math formulas into JavaScript code. This causes significant complications because neither of the aforementioned formulas are simple – they both contain multiple operators and operands.

But how does JavaScript parse this condition when it encounters it? Let's see an example below:

```js
/*GIVEN A SET OF SCORES GOTTEN BY A TEAM,
CALCULATE THE AVERAGE SCORE OF THE TEAM

FORMULA FOR AVERAGE IS: SUM OF VALUES DIVIDED BY TOTAL NUMBER OF VALUES

firstScore = 40;
secondScore = 38;
thridScore = 24;
fourthScore = 32; 
*/

const averageScore = 40 + 38 + 24 + 32 / 4;

console.log(averageScore)    //OUPUT: 110
```

If you use any [online average calculator tool](https://www.omnicalculator.com/math/average), the result will be `33.5`, which is the right answer. The outcome of the aforementioned operation in our code is `110`, which is quite "wrong" because the average on those values cannot be `110`. Yet why? Here, operator precedence is in effect.

Similar to how hierarchies operate in the real world, some operators in the land of JavaScript are more significant than others. JavaScript first recognizes and uses the "more" important operators before the "less" essential ones in an operation.

### Rules of the Operator Precedence

JavaScript doesn't randomly choose which operator it grants priority to in an operation based on the order in which they appear or for any other reason. Doing so would result in a JavaScript universe plagued by mathematical inconsistencies.

JavaScript has a rule that it carefully adheres to in order to determine precedence. Rather to going through a lengthy table or chart of all these rules, there is a quicker method that is easier to remember: **BODMAS**

BODMAS translates to:

* Bracket "()"
* Of (**)
* Division (/)
* Multiplication (**)
* Addition (+)
* Subtraction(-)

Each operand is listed above in the precise order that their precedence is determined. Easy? I adore this technique and employ it regularly to avoid errors that Operator precedence can introduce.

Let's investigate how JavaScript handled the average score operation. As we can see from the small formula above (**BODMAS**), the Division(/) operator has a higher precedence than the Addition(+) operator, so JavaScript first performs the Division(/) operations by dividing `32` by `4`, which results in `8`. Then it moves on to the next operator in accordance with the precedence, which is the Addition(+) operator, which sums up all the values and returns a result of 110.

Now let's look again at the exaxmple from the beginning of this tutorial:

```js
let attendees = 2 + 3 * 4;

console.log(attendees) // OUTPUT: 14.
```

You may have mentally performed the preceding computation and come up with `20` (this is what I got), but JavaScript believes otherwise, which is actually right.

According to the **BODMAS** rule of precedence, multiplication comes before addition. So JavaScript multiplied 3 by 4 (which is 12) before adding the result to the other operand to get the number 14.

Because we needed to divide the total count of the scores by the sum of the scores, we can now adjust our average score operation with this knowledge:

```js
/*GIVEN A SET OF SCORES GOTTEN BY A TEAM,
CALCULATE THE AVERAGE SCORE OF THE TEAM

FORMULA FOR AVERAGE IS: SUM OF VALUES DIVIDED BY TOTAL NUMBER OF VALUES

 firstScore = 40;
secondScore = 38;
thridScore = 24;
fourthScore = 32; 
*/

const averageScore = (40 + 38 + 24 + 32) / 4;

console.log(averageScore) //OUPUT: 33.5
```

Hurray! Finally, we got the correct answer! Can you tell how JavaScript interpreted this?

The precedence hierarchy places brackets first, so JavaScript executes the operations contained within the brackets before moving on to the next operation. As a consequence, it added 40, 38, 34, and 32 to produce 144, which was then divided by the score count of 4, giving us the final result of 33.5.

Here are a few exercises you can try to put your newly acquired operator precedence knowledge to the test:

```js
1. 2 + 4 - 6 / 2
2. 4 + 4 * 8 / 3
3. 8 ** 2 + 4


/* 
ANSWERS: 
1. 3
2. 20
3. 68
*/
```

There are certain operators missing from the **BODMAS** formula above. The formula is not "absloute" because it only covers a tiny portion of operators, namely the arithmetic operators that we employ in our daily coding operations. This [MDN resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#table) shows a more thorough precedence table of hierarchy.

## Conclusion

We're at the end of this tutorial, in which we learned about JavaScript operators and how JavaScript parses them when performing an operation using a technique called **Operator precedence**. Using this [MDN resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence), you can learn more about Operator precedence.

As it can be pretty cumbersome to remember all of the **Operator precedence**, so you can use the acronym **BODMAS.**

I really hope you took a lot away from this article.

Follow me on [Twitter](https://twitter.com/developeraspire). for more tip on JavaScript and CSS.

I appreciate you reading. See you next time!

