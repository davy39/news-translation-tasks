---
title: How to Use the Greater Than and Less Than Operators in JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-13T11:02:26.000Z'
originalURL: https://freecodecamp.org/news/greater-than-and-less-than-operators-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-pixabay-417173--3-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: null
seo_desc: 'In your JavaScript programs, you''ll often need to compare two values to
  see if one is greater than or less than the other. This is where the greater than
  and less than operators come in handy.

  In this article, we''ll look at how to use these operators...'
---

In your JavaScript programs, you'll often need to compare two values to see if one is greater than or less than the other. This is where the greater than and less than operators come in handy.

In this article, we'll look at how to use these operators in greater detail through code examples.

## How to Use the Greater Than `>` Operator in JavaScript

You can use the greater than operator to check if the value on the left is greater than the value on the right. It is represented by the `>` symbol.

The result will return a Boolean value of `true` if the value on the left is greater than the value on the right, and `false` if it is not.

Here is an example of checking if `5` is greater than `3`:

```js
console.log(5 > 3); // true
```

Since the number `5` is greater than `3`, the result will be `true`.

If we switch the two values, then the result will be `false`:

```js
console.log(3 > 5); // false
```

## How to Use the Less Than `<` Operator in JavaScript

You can use the less than operator to check if the value on the left is less than the value on the right. It is represented by the `<` symbol.

The result will return a Boolean value of `true` if the value on the left is less than the value on the right, and `false` if it is not.

Here is an example that checks if the number `3` is less than `5`:

```js
console.log(3 < 5); // true
```

Since `3` is less than `5`, the result will be `true`.

But if we switch the two values, then the result will be `false`:

```js
console.log(5 < 3); // false
```

## How to Use the Greater Than or Equal To `>=` Operator in JavaScript

If you need to check if the value on the left is greater than or equal to the value on the right, you can use the greater than or equal to operator. It is represented by the `>=` symbol.

The result will return a Boolean value of `true` if the value on the left is greater than or equal to the value on the right, and `false` if it is not.

Here is an example of that checks if the number `5` is greater than or equal to `5`:

```js
console.log(5 >= 5); // true
```

Since the number `5` is equal to `5`, the result will be `true`.

If we change the left value to be the number `3`, then the result will be `false`:

```js
console.log(3 >= 5); // false
```

## How to Use the Less Than or Equal To `<=` Operator in JavaScript

If you need to check if the value on the left is less than or equal to the value on the right, you can use the less than or equal to operator. It is represented by the `<=` symbol.

The result will return a Boolean value of `true` if the value on the left is less than or equal to the value on the right, and `false` if it is not.

Here is an example of that checks if the number `3` is less than or equal to `5`:

```js
console.log(3 <= 5); // true
```

If we change the left value to be the number `6`, then the result will be `false`:

```js
console.log(6 <= 5); // false
```

## How to Use Comparison Operators in a Conditional Statement

It is common to use comparison operators inside conditional statements like an `if` statement.

In this example, we have an application that asks the user for their age and displays a response based on the age they entered:

For the HTML, we'll use a form to ask the user for their age. Below the form, we'll display the message based on the age entered.

```html
<h1 class="title">How old are you?</h1>

<main>
  <form id="form">
    <div class="input-container">
      <label for="age">Enter your age: </label>
      <input type="number" id="age" required min="1" max="120" />
    </div>

    <button class="submit-btn" id="submit-btn">Submit age</button>
  </form>

  <p class="result-para" id="result"></p>
</main>
```

Next, we'll use a method called `getElementById` to go through the HTML document to find the elements that match the ids we specify. 

We can use the method to get the form element, age input and result paragraph, and assign them to `const` variables:

```js
const ageInput = document.getElementById("age");
const form = document.getElementById("form");
const resultParagraph = document.getElementById("result");
```

We then want to create an array of strings to show the user based on their age.

```js
const responsesArr = [
  "Oh wow! You are just a kid.",
  "Nice! It looks like you are old enough to drive in the States.",
  "Awesome! It looks like you are old enough to vote in the States.",
  "Cool! It looks like you are old enough to drink in the States.",
];
```

Then we need to create a function called `displayResponse` with a parameter called `age`. This function will be responsible for displaying the messages based on the age entered.

```js
function displayResponse(age) {

}
```

Inside that function, we need to check if the user's age is less than `16`. If it is, we'll display the first message in the `responsesArr` array.

We'll use the `textContent` property to change the text inside the `resultParagraph` element.

```js
if (age < 16) {
  resultParagraph.textContent = responsesArr[0];
}
```

If the user is between `16` and `18`, we will display the second message in the `responsesArr` array.

```js
else if (age >= 16 && age < 18) {
    resultParagraph.textContent = responsesArr[1];
  }
```

If the user is between `18` and `21`, we will display the third message in the `responsesArr` array.

```js
else if (age >= 18 && age < 21) {
    resultParagraph.textContent = responsesArr[2];
}
```

If the user is `21` or older, we will display the last message in the `responsesArr` array.

```js
else {
    resultParagraph.textContent = responsesArr[3];
  }
```

The last part of this function is to reset the form after the user submits their age.

```js
ageInput.value = "";
```

Here is the complete function:

```js
function displayResponse(age) {
  if (age < 16) {
    resultParagraph.textContent = responsesArr[0];
  } else if (age >= 16 && age < 18) {
    resultParagraph.textContent = responsesArr[1];
  } else if (age >= 18 && age < 21) {
    resultParagraph.textContent = responsesArr[2];
  } else {
    resultParagraph.textContent = responsesArr[3];
  }
  ageInput.value = "";
}
```

The last part of this application is to add an event listener that checks when the user submits their input into the form, and display that message based on the age entered.

We are going to use the `addEventListener` method to listen for the `submit` event on the form. When the form is submitted, we will prevent the default behavior of the form and call the `displayResponse` function with the value of the age input.

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  displayResponse(ageInput.value);
});
```

Here is a complete interactive example on CodePen:

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/zYbMBaP]

## Conclusion

Working with comparison operators like the greater than, greater than or equal to, less than and less than or equal to operators is a common task in JavaScript. They are used to compare two values and return a Boolean value of `true` or `false` based on the comparison.

I hope you enjoyed this article and found it helpful.

Happy coding!

