---
title: JavaScript if Statements, Equality and Truthy/Falsy – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-21T21:06:20.000Z'
originalURL: https://freecodecamp.org/news/javascript-if-statement-equality-and-truthy-falsy
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Deborah Kurata

  Decisions, decisions, decisions. Go left? Or go right? In programming, we use an
  if statement when we want our code to make a decision.

  In this tutorial, we''ll deep dive into the JavaScript if statement. Along the way,
  we''ll examine...'
---

By Deborah Kurata

Decisions, decisions, decisions. Go left? Or go right? In programming, we use an `if` statement when we want our code to make a decision.

In this tutorial, we'll deep dive into the JavaScript `if` statement. Along the way, we'll examine the difference between single equals, double equals, and triple equals. We'll also clarify the meaning of truthy and falsy in JavaScript.

You can watch the associated video here which walks through a demo.

%[https://youtu.be/_rqsd4DPKkE]

Let's say we are building a number guessing game as shown in Figure 1 below. The game generates a random number. The user tries to guess that number by entering their guess and clicking the Guess button. 

The game then checks the entered number. If the guess is too low, the game displays "too low". If the guess is too high, the game displays "too high". And if the guess is just right, the game displays "is correct ... You win!".

![User interface for a number guessing game.](https://www.freecodecamp.org/news/content/images/2023/03/GamePlay-1.png)
_Figure 1. A number guessing game._

There are numerous "ifs" in that paragraph! To write the code for this game, we'll need some `if` statements.

## **Anatomy of an if Statement in JavaScript**

In JavaScript, `if` is a block statement. A **block** statement groups a set of instructions. A block is delimited with curly braces.

Let's start with a simplified version of the logic required for our game. Here we determine if the user's guess is right or wrong.

```javascript
if (guess === randomNumber) {
  feedbackText = 'Correct ... You win!';
  displayPlayAgain(true);
}
```

The `if` statement begins with the `if` keyword. Note that all of JavaScript is case sensitive, including the key words. So if a keyword such as `if` is lowercase, it must be typed as lower case.

The `if` keyword is followed by parentheses. Inside the parentheses, we define the conditions for the `if` statement to make its decision, called the **decision criteria**.

In the above example, the decision criteria determine if the value in the variable `guess` equals the value in the variable `randomNumber`. Notice the triple equal `===`. We'll talk about that in a moment.

The `if` block body is enclosed in curly braces. The block can contain any number of statements, including additional `if` statements. If the decision criteria within the parentheses evaluate to true, the code within the block is executed. Otherwise, the code execution continues after the `if` block.

## **Single Equal vs Double Equal vs Triple Equal in JavaScript**

In JavaScript, we use one, two, or three equal signs, depending on what we need.

The single equal sign `=` is an assignment. We use it to assign a value or expression to a variable.

```javascript
let feedbackText = 'Correct ... You win!';
const randomNumber = Math.floor(Math.random() * 20) + 1;
```

In this code, we assign a string to the `feedbackText` variable. And assign a generated random number to the `randomNumber` variable.

The double equal `==` and triple equal `===` are comparison operators. They evaluate the equality of the two values. But how they perform that equality is slightly, yet significantly, different.

The double equal `==` compares the two values. If the values are of different types, it attempts to convert them to the same type before comparing.

Let's look at an example.

```javascript
let randomNumber = 8;
let guess = "8"

if (guess == randomNumber) {
  feedbackText = 'You win!';
  displayPlayAgain(true);
}
```

In the above code, instead of generating a random number we assign the number 8 to the `randomNumber` variable. And assign a string value of "8" to the `guess` variable. Since our `if` statement uses a double equal in this example, the data types are converted to the same type. The decision criteria then evaluates to true because the values are both 8. And the `feedbackText` variable is set to "You win!"

For more information on JavaScript variables and data types, check out this video.

%[https://youtu.be/hRQ3BtPmNNc]

The triple equal `===` is strict equality. It compares the data types and their values. It does not do any type coercion, meaning it won't attempt to convert the types. For strict equality to evaluate to true, the data type and the value must be the same.

Let's look at the same example, but using triple equal instead.

```javascript
let randomNumber = 8;
let guess = "8"
if (guess === randomNumber) {
  feedbackText = 'You win!';
  displayPlayAgain(true);
}
```

Using the triple equal `===`, the `guess` string value of "8" is not converted to a number. Because the values are not of the same data type, `guess` does not match `randomNumber`. The decision criteria evaluates to false and the code within the `if` block is not executed.

Figure 2 provides a summary. Use the triple equal any time you want an exact match, including their values and data types.

![Image](https://lh6.googleusercontent.com/jHUrGIhddGXeNWbtO6hGM2HMUoLckdPHiWu2rJ2Z63deCR6iDmpA98d_uHYKURwcp19sS8qrIWiht1kqE9JKFqgRZ5b3fTkPV-EKMAQKqfCtjFQDbRQEj4rCKJq7AGx6hjjtW3NKhqfZDAleEBvLkT4)
_Figure 2. In JavaScript, we use one, two, or three equal signs._

## **`if` vs `else` vs `else if` in JavaScript**

The `if` statement alone works great if you want the code to do something if some condition is true. But sometimes you also want the code to do something else if the condition is not true. That's the purpose of the `else` block.

```javascript
if (guess > randomNumber) {
  feedback = 'Too high';
} else {
  feedback = 'Too low';
}
```

In the above code example, if the user's guess is greater than the random number, the `feedback` variable is assigned 'Too high'. Otherwise (else), it is set to 'Too low'.

In general, if the decision criteria is false, the `else` block is executed.

We can also use an `else if`. The `else if` provides a second set of decision criteria. So the `else` block is only executed if those decision criteria are true.

Here is an example that uses `if`, `else` and `else if`:

```javascript
if (guess === randomNumber) {
  feedback = 'Correct ... You win! ';
} else if (guess > randomNumber) {
  feedback = 'Too high';
} else {
  feedback = 'Too low';
}
```

Let's walk through this code. 

When this code is run, the first decision criterion get evaluated. Since this criterion uses triple equal `===`, it's a strict compare, meaning it compares the data type and value. If both the data type and value are the same, the decision criterion evaluates to true and the `if` block code is executed. In this example, the `if` block has only one statement, but there could be any number of statements in the `if` block.

If the first decision criterion is false, either because the variables have a different data type or a different value, the `else if` decision criterion is evaluated. If the guess is greater than the random number, the `else if` block is executed. In this case, the block only has one statement, but there could be any number of statements in this block.

If the `else if` decision criterion is false, the `else` block code is run. Again, there could be any number of statements within this `else` block.

To see this concept visually, Figure 3 shows this logic as a flow chart.

![Flow chart of the `if` logic](https://www.freecodecamp.org/news/content/images/2023/03/flow-chart.png)
_Figure 3. Flow chart of the code logic_

On the flow chart, the decision criteria are shown as diamonds with paths for true and false.

If the user's guess exactly matches the `randomNumber` (data type and value), the decision criteria are true and we set the feedback to 'Correct ... You win!'.

If the `if` statement decision criteria are false, the `else if` decision criteria are evaluated. If the user's guess is larger than the random number, the `else if` decision criteria are true and we set the feedback to 'Too high'.

If the `else if` decision criteria are false, we set the feedback to 'Too low'.

In these `if` statements, it's generally clear when the decision criteria are true or false. The guess is exactly the same as the random number or it isn't. The guess is greater than the random number or it isn't.

But what about this `if` statement?

```javascript
if (guessInput) {
  let guess = guessInput.valueAsNumber;
}
```

With no comparison operator, this is shorthand syntax for "if this variable is truthy". How do we know if `guessInput` is true or false?

## **Truthy vs Falsy Values in JavaScript**

JavaScript has a unique sense of true and false, called **truthy** and **falsy**. Truthy and falsy are used when evaluating decision-criteria that aren't clearly true or false. Let's look at some examples.

```javascript
let guess = false;
if (guess) { … } // falsy
```

As you would expect, a variable set to `false` is falsy. The code within the `if` block is not executed.

```javascript
let guess = 0;
if (guess) { … } // falsy
```

A value of `0` (zero) is also falsy.

```javascript
let guess = "";
if (guess) { … } // falsy
```

And `""`, which is an empty string, is falsy.

```javascript
let guess;		// undefined
if (guess) { … } // falsy
```

If a variable has not been assigned a value, it is `undefined`. An `undefined` variable is falsy. A common coding pattern is to ensure a variable has a value before doing something with that variable using an `if` statement as shown above. 

```javascript
let guess = null;
if (guess) { … } // falsy
```

A `null` variable is also falsy.

```javascript
let guess = Number("four"); // NaN
if (guess) { … } // falsy
```

And if the code attempts to convert a value that is not a number to a number, the result is `NaN`, which stands for "not a number". Variables that are `NaN` evaluate to falsy.

Any other values are truthy. 

```javascript
let guess = 4;
if (guess) { … } // truthy

guess = 'four';
if (guess) { … } // truthy
```

In the first example, the variable is set to a non-zero number, so it is truthy. In the second example, the variable is set to a non-empty string, so it is truthy.

Basically, if the variable value is false, zero, empty, null, undefined, or `Nan`, it's falsy and the code within the `if` block is not run.

If the variable value is anything else, such as a number that is not zero, a non-empty string, an array, or an object, it's truthy and the code in the `if` block is run.

How about a more full-featured example?

## **Guessing Game Example**

Our guessing game includes the following code:

```javascript
// Find the elements
const guessButton = document.getElementById('guess-button');
guessButton.addEventListener('click', processGuess);

const guessInput = document.getElementById('guess-input');
const feedbackContainer = document.getElementById('feedback');

function processGuess() {
  let feedbackText;
  if (guessInput){
    const guess = guessInput.valueAsNumber;

    if (guess === randomNumber) {
      feedback = 'Correct ... You win! ';
    } else if (guess > randomNumber) {
      feedback = 'Too high';
    } else {
      feedback = 'Too low';
    }
  }

  if (feedbackContainer) {
    feedbackContainer.innerHTML += '<br>' + feedbackText;
  }
}
```

We first find the HTML elements we want to work with. We find the guess button, and use `addEventListener` to listen for the button click event. When the user clicks the button, the code calls the function we passed to `addEventListener`, which is `processGuess`.

For more information on finding HTML elements and reacting to their events, [check out this article](https://www.freecodecamp.org/news/reacting-to-actions-with-javascript/).

We then find the guess input element so we can read the user's guess. And we find a feedback element we'll use to write the feedback text to the page.

The `processGuess()` function reads the user's guess from the input element and displays the appropriate feedback. Let's break it down.

The first `if` statement ensures we found the input element. If the element was found, we have a reference to that element in the `guessInput` variable. The `guessInput` variable evaluates to truthy, and the `if` block code is executed.

The code within the `if` block reads the value of the input element. It uses `valueAsNumber`, which reads a numeric input as a number instead of a string. That way we can more easily compare the guess value to the randomly generated number.

The code then strictly compares the guess to the generated random number. If the values have the same type and value, the decision criteria are true and this `if` block code is run.

If the guess is not correct, an `else if` block determines if the value is too high or too low. Based on that comparison, the feedback text is set.

Lastly, we check whether we have a reference to the feedback container. If so, the `feedbackContainer` variable is set, the `if` statement evaluates to truthy, and we write the appropriate feedback text to that container.

## **Wrapping Up**

We use `if` statements to make decisions in our code. The statements inside an `if` block are run if the decision criteria defined within the parentheses evaluate to true or truthy. The statements inside an `else` block are run if the decision criteria evaluate to false or falsy.

When defining decision criteria, it's important to set the appropriate comparison:

* A single equal `=` in JavaScript assigns a value to a variable. It should not be used in decision criteria.
* The double equals `==` compares the values to see if they are equal. If the values are not the same data type, it tries to convert them to the same type before checking for equality.
* The triple equals `===` strictly compares the values to see if they are equal. If they are not the same type, they are not equal.

And be mindful of JavaScript's rules for truthy and falsy, especially when defining decision criteria.

You can find the code for the guess a number game here: [https://github.com/DeborahK/Gentle-Introduction-to-JavaScript](https://github.com/DeborahK/Gentle-Introduction-to-JavaScript)

For more information on programming with JavaScript and to build this guess a number game step by step, check out this course:

%[https://youtu.be/jJLn5XxyXWc]

Now don't be iffy, use those `if` statements wisely!

  

