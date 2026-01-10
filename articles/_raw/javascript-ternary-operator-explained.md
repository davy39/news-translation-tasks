---
title: How to Use the Ternary Operator in JavaScript – Explained with Examples
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2024-02-27T13:04:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-ternary-operator-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/ternary-operator-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Tired of bulky if-else statements? JavaScript''s ternary operator offers
  a powerful solution. This handy tool lets you condense complex conditional logic
  into a single line, making your code cleaner, more elegant, and efficient.

  In this article, we''ll...'
---

Tired of bulky if-else statements? JavaScript's ternary operator offers a powerful solution. This handy tool lets you condense complex conditional logic into a single line, making your code cleaner, more elegant, and efficient.

In this article, we'll take a deep dive into the ternary operator, understanding its syntax and showcasing real-world examples to help you understand how it works to harness its full potential.

## Here is What We'll Cover:

1. [What is A Ternary Operator?](#heading-what-is-a-ternary-operator)
2. [How to Use the Ternary Operator](#heading-how-to-use-the-ternary-operator)
3. [How to Refactor if-else Statements to Ternary operator](#heading-how-to-refactor-if-else-statements-to-ternary-operator)
4. [How to Chain Ternary Operators](#heading-how-to-chain-ternary-operators)
5. [Best Practices when using the Ternary Operator](#heading-best-practices-when-using-the-ternary-operator)
6. [Conclusion](#heading-conclusion)

## What is A Ternary Operator?

A ternary operator is a conditional operator in JavaScript that evaluates a conditional expression and returns either a truthy or falsy value.

To understand how this works, let's take a closer look at its syntax below:

```js
conditionalExpression ? truthyValue : falsyValue
```

From the syntax above, the `condionalExpression` is the expression that serves as the evaluation point, determining either a truthy or falsy value. 

Following the `?` (question mark), the value provided is returned in case the expression evaluates to truthy, whereas the value following the `:` (colon) is returned if the expression results in a falsy outcome.

The `truthyValue` and `falsyValue` can be anything in JavaScript. It can encompass various entities such as functions, values stored in variables, objects, numbers, strings, and more. The ternary operator grants you the flexibility to return any desired value, offering versatility in your code.

## How to Use the Ternary Operator

Now that we've examined the syntax and its functionality, let's explore how to use the ternary operator to deepen our understanding.

Consider this scenario: we're building a gaming platform that only allows users that are aged 18 and above. We'll design a function to check a user's age. If they're under 18, they'll be denied access; otherwise, they'll gain entry to the platform.

```js
function canAccessPlatform(age) {
  const shouldAccess = age >= 18 ? true : false;

  return shouldAccess;
}
```

From the code snippet above, we created a function, `canAccessPlatform`, which evaluates whether a user, represented by their `age` parameter, meets the requirement to access the platform. 

It utilizes a ternary operator to determine if the age is 18 or older, assigning `true` to `shouldAccess` if the condition is met, and `false` otherwise. Finally, it returns the value of `shouldAccess`, indicating whether the user can access the platform or not.

If the age is 18 or older, the expression becomes true, so the operator returns true after the `?`. Otherwise, it returns false. This result is saved in a variable and then returned from the function. 

While this basic use case simplifies code and improves readability by replacing unnecessary if-else blocks, it's important to use it sparingly to avoid cluttering and complicating your code. Later, we'll discuss best practices for using the ternary operator.

Here's another example illustrating the use of the ternary operator. We'll create a function to determine whether a number is even or odd. Check out the code snippet below:

```js
function checkEvenOrOdd(number) {
  const result = number % 2 === 0 ? "even" : "odd";
  return result;
}

// Usage:
console.log(checkEvenOrOdd(4)); // Output: "even"
console.log(checkEvenOrOdd(7)); // Output: "odd"
```

From the code snippet above:

* We define a function `checkEvenOrOdd` that takes a `number` parameter.
* Inside the function, we use the ternary operator to check if the number is even or odd.
* If the number modulo 2 equals 0 (meaning it's divisible by 2 with no remainder), then the condition evaluates to true, and the string "even" is assigned to the `result` variable.
* If the condition evaluates to false (meaning the number is odd), the string "odd" is assigned to `result`.
* Finally, the function returns the value of `result`, which indicates whether the number is even or odd.

This code shows how the ternary operator quickly checks if a number is even or odd, making the code easier to read and understand.

## How to Refactor if-else Statements to Ternary Operator

An advantage of the ternary operator is avoiding unnecessary if-else blocks, which can complicate code readability and maintenance. In this section, we'll refactor some if-else statements into ternary operations, providing a clearer understanding of how to use ternary operators effectively.

Let's start with our first example:

```js
function decideActivity(weather) {
  let activity;

  if (weather === "sunny") {
    activity = "go out";
  } else {
    activity = "stay in";
  }

  console.log(activity);
}

// Usage
console.log(decideActivity("raining")); // Output: "stay in"
console.log(decideActivity("snowing")); // Output: "stay in"
console.log(decideActivity("sunny")); // Output: "go out"
```

This function, `decideActivity`, takes a `weather` parameter and determines the appropriate activity based on the weather condition. 

If the weather is "sunny", it suggests to "go out". Otherwise, it advises to "stay in". When we call the function with different weather conditions like "raining" or "snowing", it outputs the corresponding activity recommendation using `console.log()`. 

For instance, calling `decideActivity("raining")` will output "stay in". Similarly, `decideActivity("snowing")` also outputs "stay in". When `decideActivity("sunny")` is called, it outputs "go out". This straightforward function helps decide on activities based on the weather condition provided.

Now, we can refactor these blocks of code to make them look simpler and neater. Let's see how to do that below:

```js
function decideActivity(weather){
   const activity = weather === "sunny" ? "go out" ? "stay in";
   
   console.log(activity)

}

// Usage
console.log(decideActivity("raining")); // Output: "stay in"
console.log(decideActivity("snowing")); // Output: "stay in"
console.log(decideActivity("sunny")); // Output: "go out"
```

From the code sample above, this function, `decideActivity`, uses the ternary operator to quickly determine the activity based on the weather condition. It checks if the weather is "sunny" and assigns "go out" if true, otherwise "stay in". 

We've simplified the if-else statements into a one-liner ternary operator. This makes our code cleaner, clearer, and easier to read.

Let take a look at another example:

```js
function checkNumber(number) {
  let result;
  if (number > 0) {
    result = "positive";
  } else {
    result = "non-positive";
  }
  return result;
}

// Usage
console.log(checkNumber(5)); // Output: "positive"
console.log(checkNumber(-2)); // Output: "non-positive"

```

Let's explain what the code above is doing:

* **Function Definition**: We begin by defining a function named `checkNumber` that takes a single parameter called `number`.
* **Variable Declaration**: Inside the function, we declare a variable named `result` without assigning any value to it yet. This variable will store the result of our check.
* **Conditional Statement (if-else)**: We have a conditional statement that checks whether the `number` parameter is greater than 0.
* If the condition is true (meaning the number is positive), we assign the string "positive" to the `result` variable.
* If the condition is false (meaning the number is not positive, (meaning it is either negative or zero), we assign the string "non-positive" to the `result` variable.
* **Return Statement**: Finally, we return the value stored in the `result` variable.
* **Function Calls**:We then call the `checkNumber` function twice with different arguments: 5 and -2.

When we call `checkNumber(5)`, the function returns "positive", which is then logged to the console.

Similarly, when we call `checkNumber(-2)`, the function returns "non-positive", which is again logged to the console.

This function efficiently determines whether a number is positive or non-positive and provides the appropriate result based on the condition.

Let's simplify and improve the code by rewriting it using a ternary operator.

```js
function checkNumber(number) {
  const result = number > 0 ? "positive" : "non-positive";
  return result;
}

// Usage
console.log(checkNumber(5)); // Output: "positive"
console.log(checkNumber(-2)); // Output: "non-positive"

```

Great job! By refactoring the function and utilizing the ternary operator for conditional evaluation, we've achieved cleaner, more concise, and readable code.

This code, using the ternary operator, feels more concise and elegant. It efficiently determines if a number is positive or non-positive, making the code cleaner and easier to understand. When we call `checkNumber(5)`, it returns "positive",  while `checkNumber(-2)` returns "non-positive". Overall, the ternary operator enhances the code's readability.

## How to Chain Ternary Operators

When dealing with conditional checks, sometimes a single condition isn't enough. In such cases, we use 'else-if' statements alongside 'if/else' to incorporate multiple conditions. 

Let's take a look at the syntax:

```js
function exampleFn() {
  return conditionalExpression1
    ? value1
    : conditionalExpression2
    ? value2
    : conditionalExpression3
    ? value3
    : value4;
}
```

This can be translated into an if/else chain:

```js
function exampleFn() {
  if (conditionalExpression1) {
    return value1;
  } else if (conditionalExpression2) {
    return value2;
  } else if (conditionalExpression3) {
    return value3;
  } else {
    return value4;
  }
}

```

Let's explore an example below:

```js
function checkNumber(number) {
  let message;

  if (number > 0) {
    message = "Positive";
  } else if (number === 0) {
    message = "Zero";
  } else {
    message = "Negative";
  }

  return message;
}

// Usage
console.log(checkNumber(5)); // Output: "Positive"
console.log(checkNumber(0)); // Output: "Zero"
console.log(checkNumber(-3)); // Output: "Negative"

```

This code above defines a function called `checkNumber` that takes a `number` parameter and determines its status (positive, zero, or negative). It utilizes an if-else block with one else-if statement to evaluate the number's value. If the number is greater than 0, it's considered positive and if it's equal to 0, it's zero. Otherwise, it's negative. The function returns the result.

Let's refactor this code using a ternary operator to achieve the same functionality.

```js
function checkNumber(number) {
  return number > 0 ? "Positive" : number === 0 ? "Zero" : "Negative";
}

// Usage
console.log(checkNumber(5)); // Output: "Positive"
console.log(checkNumber(0)); // Output: "Zero"
console.log(checkNumber(-3)); // Output: "Negative"

```

That's it! We've refactored the function, and upon closer examination, we can observe that the operators are chained together. Now, let's explore how the chained ternary operator works in the `checkNumber` function.

In the first ternary operator:

* The first part `number > 0` checks if the number is greater than 0.
* If it's true, the expression returns "Positive".

In the second ternary operator (chained):

* If the first condition is false (meaning the number is not greater than 0), it moves to the next part of the expression: `number === 0`.
* This part checks if the number is equal to 0.
* If it's true, the expression returns "Zero".

And the default value:

* If neither of the above conditions is true (meaning the number is not greater than 0 and not equal to 0), it defaults to the last part of the expression: `"Negative"`.
* This part acts as the default value if none of the preceding conditions are met.

In summary, the chained ternary operator evaluates multiple conditions in a single line of code. It checks each condition sequentially, and the first condition that evaluates to true determines the result of the entire expression. This allows for concise and efficient conditional logic.

Let's examine another example of a chained ternary operator.

```js
function getDrink(age) {
  return age >= 21
    ? "Enjoy a cocktail"
    : age >= 18
    ? "Have a beer"
    : age >= 16
    ? "Grab a soft drink"
    : "Sorry, you're too young to drink";
}

// Usage
console.log(getDrink(25)); // Output: "Enjoy a cocktail"
console.log(getDrink(19)); // Output: "Have a beer"
console.log(getDrink(16)); // Output: "Grab a soft drink"
console.log(getDrink(10)); // Output: "Sorry, you're too young to drink"

```

In the given code sample, the ternary operators are chained together to provide different drink suggestions based on the age provided. Each conditional expression in the chain evaluates a specific age range. 

If the first condition is true (truthy), it returns 'Enjoy a cocktail'. If false (falsy), it moves to the next conditional expression, and so on. This chaining process continues until a condition evaluates to true. If none of the conditions in the chain are true, the last value is returned as a fallback, similar to the 'else' block in an if/else statement.

The concept of 'chaining' ternary operators involves linking conditional expressions based on the value of the previous expression. This can be compared to the `else if` structure in an `if/else` statement, providing a concise way to handle multiple conditions in JavaScript. 

## Best Practices when Using the Ternary Operator

Using the ternary operator efficiently can significantly enhance code readability and conciseness. In this section, we'll explore key best practices for utilizing the ternary operator effectively. 

1. **Keep it simple and readable**: Write concise expressions that are easy to understand at a glance. Avoid nesting too many ternary operators or writing overly complex conditions. 
2. **Use for simple assignments:** Ternary operators are ideal for simple assignments where there are only two possible outcomes based on a condition. For more complex scenarios, consider using `if/else` statements.
3. **Know when to use it**: Use the ternary operator when you need to perform a simple conditional check and assign a value based on the result. It's particularly useful for assigning default values or determining the value of a variable based on a condition.
4. **Test thoroughly**: Test your code thoroughly to ensure that the ternary operator behaves as expected under different conditions. Check for edge cases and validate the correctness of the assigned values.
5. **Avoid nested ternaries:** While chaining ternaries is possible, excessive nesting can lead to code that is difficult to read. Prefer clarity and consider using `if/else` for complex conditions.
6. **Keep ternaries short:** Aim to keep ternary expressions short and concise. Long ternaries can be difficult to read and understand, leading to code maintenance challenges.

These best practices outline guidelines for effectively utilizing the ternary operator. While they are not strict rules, they offer valuable insights to enhance the clarity and readability of your code.

## Conclusion

As we conclude this article, you've gained a comprehensive understanding of the ternary operator—its application in daily coding tasks, converting if/else statements, chaining operators, and best practices. I'm confident that you've acquired valuable insights that will enhance your coding practices using the ternary operator.

Thank you for reading, and see you next time!

### Contact information

Would you like to get in touch with me? Don't hesitate to reach out through any of the following channels:

* Twitter / X: [@developeraspire](https://twitter.com/developeraspire)
* Email: developeraspire5@gmail.com

