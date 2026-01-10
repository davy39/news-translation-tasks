---
title: What is the querySelector() Method and How Does it Work in JavaScript?
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-12T23:00:54.000Z'
originalURL: https://freecodecamp.org/news/queryselector-method-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/fili-santillan-qp51FQhBnS0-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, there will be times when you need to access an HTML element.
  The querySelector method is a web API that selects the first element that matches
  the specified CSS selector passed into it.

  But how does this work in more detail? In this ar...'
---

In JavaScript, there will be times when you need to access an HTML element. The `querySelector` method is a web API that selects the first element that matches the specified CSS selector passed into it.

But how does this work in more detail? In this article, we will look at several examples on how to use the `querySelector` method as well as the `querySelectorAll` method.

## Basic Syntax for the `querySelector()` Method

The `querySelector` method is called on the `document` object and takes in an argument that represents the CSS selector of the element you want to select.

```js
document.querySelector(selector);
```

If the selector matches an element within the document, the method will return the first matching element. If there are no matches, the method will return `null`.

## How to Use the `querySelector()` Method with Type Selectors

A type selector in CSS refers to the name of an HTML element. Examples of this would be `button`, `div`, `p`, and so on.

In this first example, we have a button element inside the HTML document.

```html
<button>Show Alert</button>
```

If we wanted to access that element inside our JavaScript file, we could use the `querySelector` method like this:

```js
const buttonElement = document.querySelector("button");
```

This line of code selects the first button it sees on the page and assigns that result to a `const` variable called `buttonElement`.

If we log this `buttonElement` variable to the console, this would be the output:

```js
console.log(buttonElement);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-11-at-3.11.37-PM.png)
_console.log output for querySelector example_

We can use that `buttonElement` variable and add an event listener to show an `alert` when the button is clicked.

```js
buttonElement.addEventListener("click", () => {
  alert("Button was clicked!");
});
```

Here is the full code and interactive example to play around with.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/ZEPqwBg]

## How to Use the `querySelector()` Method with Class Selectors

A class selector in CSS refers to the name of a class that is used in an HTML element. Examples of this would be `.container`, `.button`, and so on.

Let's say we want to build out a solitaire game and want to hide/show the rules of the game when a button is clicked. We could use the `querySelector` method to select the button and the rules container.

Here is the starting HTML:

```html
<h1>Let's play solitaire!</h1>
<main>
  <button class="rules-btn">Show Rules</button>
  <section class="rules-container">
    <h2>Rules to the game</h2>
    <ul>
      <li>There are 7 columns of cards</li>
      <li>First column has 1 card, second has 2, third has 3, and so on</li>
      <li>First card in each column is face up, rest are face down</li>
      <li>Move cards to build 4 stacks of cards in ascending order</li>
      <li>Start with aces and build up to kings</li>
      <li>Move cards by dragging and dropping</li>
    </ul>
  </section>
</main>
```

Inside the JavaScript file, we can use the `querySelector` method to select the rules button and the rules container.

```js
const rulesBtn = document.querySelector(".rules-btn");
const rulesContainer = document.querySelector(".rules-container");
```

We can then add an event listener to the `rulesBtn` variable to show/hide the rules container when the button is clicked. We are using the `classList` property to toggle the class of `"show"` on the rules container element.

```js
rulesBtn.addEventListener("click", () => {
  rulesContainer.classList.toggle("show");
});
```

Here is an interactive example where you can see the rules container being shown and hidden when the button is clicked.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/LYagqMj]

While the toggle is working here, there is a small bug in the code. By default the rules will be hidden and button text says "Show Rules". When the rules are shown, the button text should change to "Hide Rules", but right now it doesn't.

Inside the event listener, we can update the text content for the button to show "Hide Rules" when the rules are shown and "Show Rules" when the rules are hidden.

```js
rulesBtn.textContent = rulesContainer.classList.contains("show")
  ? "Hide Rules"
  : "Show Rules";
```

Now the button text will change based on the state of the rules container.  
Here is the complete JavaScript code:

```js
const rulesBtn = document.querySelector(".rules-btn");
const rulesContainer = document.querySelector(".rules-container");

rulesBtn.addEventListener("click", () => {
  rulesContainer.classList.toggle("show");
  rulesBtn.textContent = rulesContainer.classList.contains("show")
    ? "Hide Rules"
    : "Show Rules";
});
```

Here is the interactive example with the updated JavaScript code.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/LYagqoz]

## How to Use the `querySelectorAll()` Method

The `querySelectorAll` method is similar to the `querySelector` method, but instead of returning the first matching element, it returns a `NodeList` of all matching elements. A `NodeList` is an array-like object that contains all the elements that match the specified selector.

In this example we have an unordered list of sports and we want to generate random background colors for each list item.

Here is the starting HTML:

```html
<button class="btn">Generate Random Background Colors</button>
<ul class="sports-list">
  <li>Football</li>
  <li>Basketball</li>
  <li>Tennis</li>
  <li>Golf</li>
  <li>Swimming</li>
</ul>
```

To select all of the list items inside the unordered list, we can use the `querySelectorAll` method like this:

```js
const sportsList = document.querySelectorAll(".sports-list li");
```

If we log the `sportsList` variable to the console, this would be the output:

```js
console.log(sportsList);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-11-at-6.10.19-PM.png)
_Example of NodeList_

We then need to use the `querySelector` method to select the button.

```js
const randomColorBtn = document.querySelector(".btn");
```

Then, we can create a random list of colors.

```js
const lightColorsArr = [
  "#FFDAB9",
  "#FFE4B5",
  "#FFFFE0",
  "#FAFAD2",
  "#F0FFF0",
  "#E0FFFF",
  "#AFEEEE",
  "#00CED1",
  "#00BFFF",
  "#1E90FF",
  "#ADD8E6",
  "#7FFFD4",
  "#7CFC00",
  "#7FFF00",
  "#32CD32",
  "#ADFF2F",
  "#FFFF00",
  "#FFD700",
  "#FFA500",
  "#FF6347",
];
```

Each time the user clicks on the button, we want to shuffle the list of colors and select 5 random light colors from the array. We can use the [Fisher-Yates shuffle algorithm](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) to shuffle the array which is a common way to shuffle an array in JavaScript.

```js
function shuffleArray(arr) {
  let currentIndex = arr.length;
  let randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [arr[currentIndex], arr[randomIndex]] = [
      arr[randomIndex],
      arr[currentIndex],
    ];
  }

  return arr;
}
```

Then we can add an event listener to the button and shuffle the array.

```js
randomColorBtn.addEventListener("click", () => {
  const shuffledColors = shuffleArray(lightColorsArr);
});
```

For each list item, we can set the background color to a random color from the shuffled array.

```js
sportsList.forEach((list, index) => {
  list.style.backgroundColor = shuffledColors[index];
});
```

Here is the complete code:

```js
const sportsList = document.querySelectorAll(".sports-list li");
const randomColorBtn = document.querySelector(".btn");

console.log(sportsList);

const lightColorsArr = [
  "#FFDAB9",
  "#FFE4B5",
  "#FFFFE0",
  "#FAFAD2",
  "#F0FFF0",
  "#E0FFFF",
  "#AFEEEE",
  "#00CED1",
  "#00BFFF",
  "#1E90FF",
  "#ADD8E6",
  "#7FFFD4",
  "#7CFC00",
  "#7FFF00",
  "#32CD32",
  "#ADFF2F",
  "#FFFF00",
  "#FFD700",
  "#FFA500",
  "#FF6347",
];

// fisher-yates shuffle algorithm

function shuffleArray(arr) {
  let currentIndex = arr.length;
  let randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [arr[currentIndex], arr[randomIndex]] = [
      arr[randomIndex],
      arr[currentIndex],
    ];
  }

  return arr;
}

randomColorBtn.addEventListener("click", () => {
  const shuffledColors = shuffleArray(lightColorsArr);

  sportsList.forEach((list, index) => {
    list.style.backgroundColor = shuffledColors[index];
  });
});

```

Here is the interactive example with the complete JavaScript code. Click on the button and you will see the list items change to random background colors.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/dyrgrOK]

## Conclusion

The `querySelector` and `querySelectorAll` methods are helpful web API's that allow you to access elements in the DOM. You can use these methods to select elements by type, class, id, attribute, pseudo-class, and pseudo-element selectors.

I suggest you experiment with these methods and see what you can come up with in your own projects.

I hope you found this article helpful and informative. Happy coding!  

