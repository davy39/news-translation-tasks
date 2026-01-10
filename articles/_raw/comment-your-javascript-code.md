---
title: How to Comment Your JavaScript Code
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-12-11T21:55:46.000Z'
originalURL: https://freecodecamp.org/news/comment-your-javascript-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Comment-Your-JS-Code-fCC.png
tags:
- name: best practices
  slug: best-practices
- name: code comments
  slug: code-comments
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Writing comments in JavaScript is crucial for code readability, maintainability,\
  \ and developer collaboration. Comments serve as notes within the codebase, explaining\
  \ its functionality and logic, or providing context. \nIn this article, I will explain\
  \ ..."
---

Writing comments in JavaScript is crucial for code readability, maintainability, and developer collaboration. Comments serve as notes within the codebase, explaining its functionality and logic, or providing context. 

In this article, I will explain the significance of commenting your code, best practices to follow, and examples showcasing effective commenting in JavaScript.

## Why Comments are Important in JavaScript

### They enhance code readability:

Comments provide clarity to code, making it easier for developers to understand the code's purpose and functionality. Comments act as a guide, especially when you need to revisit older code after a period of time.

Consider this un-commented code:

```javascript
function calculateTotal(price, quantity) {
    return price * quantity;
}

let totalPrice = calculateTotal(25, 5);
console.log(totalPrice); // Output: 125
```

It is quite difficult for us to understand what the code does, right? Now, let's add comments for clarity:

```javascript
// Calculates the total cost by multiplying the price per item with the quantity
function calculateTotal(price, quantity) {
    return price * quantity;
}

// Example usage: Calculates the total price for 5 items at $25 each by multiplying the price per item ($25) with the quantity (5), and stores the result in the totalPrice variable.
let totalPrice = calculateTotal(25, 5);
console.log(totalPrice); // Output: 125
```

With comments, it is quite understandable what each part of the code does, and it also enhances its readability.

### They facilitate collaboration:

In a team environment, comments aid collaboration by allowing developers to comprehend each other's code, making it easier to work together on projects.

Imagine working in a team where different developers handle various parts of a project. Clear comments aid in understanding each other's code. Here's an example:

```javascript
// Validates the format of the provided email address using a regular expression, which checks for the presence of "@" symbol, domain name, and top-level domain (TLD) in the email
function validateEmail(email) {
    // Regular expression pattern to match the standard email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
```

In a collaborative setting, another developer can quickly comprehend the purpose of the `validateEmail` function due to the comment, enabling smoother teamwork. This would've been very difficult without the comments indicating what the code block does.

### They make maintenance and debugging easier:

Well-commented code simplifies maintenance and debugging. Comments can highlight potential issues, outline the reasoning behind specific solutions, and aid in locating bugs.

Comments assist in debugging and maintaining code. Consider the following commented code:

```javascript
// Finds the maximum number between num1 and num2 using a ternary operator for comparison and returns the larger number
function findMax(num1, num2) {
    /* Using ternary operator to compare num1 and num2
       and return the larger number */
    return (num1 > num2) ? num1 : num2;
}
```

If a bug arises or modifications are needed, the comment clarifies the logic used, aiding in swift debugging or updates.

## Best Practices for Commenting in JavaScript

### Use descriptive comments:

Explain the purpose of functions, variables, or complex logic using descriptive comments. This helps other developers, including your future self, understand the code's intention.

```javascript
// Calculates the area of a circle using the provided radius by multiplying the square of the radius by the mathematical constant π (pi)
function calculateCircleArea(radius) {
    return Math.PI * radius * radius;
}
```

Descriptive comments like this explain the purpose of functions or operations, aiding in understanding the code's intention.

### Avoid over-commenting:

While comments are beneficial, excessive commenting can clutter the code. Aim for a balance where comments add value without stating the obvious.

```javascript
// Variable to store user data
let userData = fetchUserData(); // Fetch user data from the server
```

In this case, the comment merely reiterates what the code already expresses clearly. Avoiding over-commenting maintains code clarity.

### Update comments regularly:

As code evolves, ensure comments remain accurate and aligned with the code changes. Outdated comments can lead to confusion.

```javascript
// Function to calculate the area of a rectangle
function calculateRectangleArea(length, width) {
    return length * width;
    // Updated comment: Area calculated by multiplying length and width
}
```

Ensuring that comments align with the current functionality or logic of the code is vital for accurate documentation.

### Comment complex sections:

When dealing with intricate algorithms or unconventional solutions, detailed comments explaining the logic can be immensely helpful.

```javascript
// Performs a complex calculation on the provided data, involving multiple steps including data preprocessing, calculation based on preprocessed data, and returning the final result
function performComplexCalculation(data) {
    /* 
        Complex logic involving multiple steps:
        - Step 1: Data preprocessing
        - Step 2: Calculation based on preprocessed data
        - Step 3: Final result
    */
    // ... complex calculation logic
}
```

For intricate algorithms or multi-step processes, detailed comments explaining each step can immensely aid in understanding.

## Types of Comments in JavaScript

### Single-line comments:

In JavaScript, single-line comments start with `//`. They're suitable for brief explanations or annotating specific lines. Keep in mind that the two forward slashes don't have any spaces between them.

Example:

```javascript
// This function calculates the square of a number
function square(number) {
    return number * number;
}

```

### Multi-line comments:

Multi-line comments begin with `/*` and end with _`/`._ They are useful for commenting out blocks of code or providing longer explanations. Keep in mind that the forward slash and the asterisk (`*`) don't have any spaces between them.

Example:

```javascript
/*
    This block of code finds the maximum of two numbers
    and returns the larger number.
*/
function findMax(num1, num2) {
    // Logic to find the maximum
    return (num1 > num2) ? num1 : num2;
}

```

### JSDoc comments:

JSDoc is a convention for adding comments to JavaScript code that enables the automatic generation of documentation. It uses a specific syntax to describe functions, parameters, return values, and so on.

Example:

```javascript
/**
 * Calculates the area of a rectangle
 * @param {number} length - The length of the rectangle
 * @param {number} width - The width of the rectangle
 * @returns {number} - The area of the rectangle
 */
function calculateArea(length, width) {
    return length * width;
}

```

## Practice Commenting Your Code 📝✍️

Learning without practicing is an incomplete process. So here's [**a learning challenge from the freeCodeCamp Certification Course**](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/comment-your-javascript-code) where you will learn how comments work in JavaScript, and how you can use them in your code. 

In this challenge, you will try to understand how single-line comments and multiline comments work.

I've included the solution next in case you can't solve the challenge yourself.

If you'd like to watch a video on this topic as well, you can find it here:

%[https://www.youtube.com/watch?v=oqFs3bRQDSY]

## The Solution to the Challenge

Make sure that you have tried to solve this challenge on your own before checking my solution.

Alright, if you're ready...here it is:

```javascript
// Fahim

/*
My
Name
Is
Fahim
*/
```

The first one is the single-line comment, and the second one is the multi-line comment.

## Conclusion

Commenting on JavaScript code is an essential practice in software development. It improves code comprehension, aids collaboration, and facilitates maintenance and debugging. 

By following best practices and using various comment types, we can create codebases that are easier to understand, maintain, and build upon.

I hope you have gained some valuable insights from the article. 

If you have enjoyed the procedures step-by-step, then don't forget to let me know on [Twitter/X](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can follow me on [GitHub](https://github.com/FahimFBA) as well if you are interested in open source. Make sure to check [my website](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) as well!

If you like to watch programming and technology-related videos, then you can check my [YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1), too. You can also check my other writings on [Dev.to](https://dev.to/fahimfba).

All the best for your programming and development journey. 😊

You can do it! Don't give up, never! ❤️


