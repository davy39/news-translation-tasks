---
title: How to Build Successful Projects as a Junior Developer
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2023-11-21T21:25:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-projects-as-a-junior-developer
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/scott-graham-5fNmWej4tAA-unsplash.jpg
tags:
- name: 'Junior developer '
  slug: junior-developer
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Several months ago, I stumbled upon a coding challenge that intrigued me.\
  \ Here's what it was:\nhttps://twitter.com/hussien_coding/status/1576929379736727554\n\
  \ \nThe task was seemingly simple: build six squares with no color, make each square\
  \ turn green ..."
---

Several months ago, I stumbled upon a coding challenge that intrigued me. Here's what it was:

%[https://twitter.com/hussien_coding/status/1576929379736727554] 

The task was seemingly simple: build six squares with no color, make each square turn green when clicked. Then when the last square turned green, make them all go back to no color in the reverse order in which they were clicked.

I was excited to test out the skills of some junior developers I was working with who were just starting out in tech, so I shared the challenge with them. But the results were not what I expected.

Despite its apparent simplicity, the challenge brought out varying results. Some students successfully created a functional solution, while others struggled with the required programming concepts.

That's when I realized that this could be a great opportunity for a lot of people. So if you're a junior developer finding it challenging to create your own portfolio/demo projects, fear not! This article will guide you through the process of successfully building a project with a straightforward approach.

## Who is This Article For?

This article is specifically tailored for junior developers who might be struggling to create their own personal side projects.

If you often find yourself relying on tutorials or feel like you lack the creativity to create projects independently, then this article is for you.

## Getting Started

Let's take a look at the challenge I sent the students:

```plaintext
Build six squares with no color 
Every time you click one, it turns green 
When the last square turns green, they all go back to no color in backwards sequence to which it was clicked (not all at once)
```

If you were one of the students presented with this challenge, what would you do first? While it may be tempting to dive right into coding, it's important to recognize that **writing code** is actually the **last step** of building a project.

So, what's the first step? The first step is to **think**. Yeah I mean to literally stop and think about the problem you're trying to solve.

## How to Think About the Problem

When approaching a project, it's important to think of it as a problem that needs a solution. Take your time to carefully consider the problem, and then break it down into smaller parts.

To do this, you may find it helpful to step away from your computer and grab a pencil and piece of paper.

For example, when faced with any kind of challenge, you can start by breaking the project down into more manageable parts. This might include:

1. Creating the six squares
    
2. Determining a way to change their color when clicked
    
3. Create a mechanism to track which squares have been clicked
    
4. Devise a method for the squares to return to their original state in the reverse order they were clicked
    

No matter how big a project may seem, it's always important to break it down into smaller parts. This makes it easier to tackle each individual piece one at a time while staying organized and focused.

So, when faced with a large project, don't be intimidated. Instead, take the time to break it down into smaller pieces and focus on tackling each piece individually. By doing so, you'll be able to stay organized, stay focused, and ultimately be more successful in your project.

After taking some time to carefully consider the challenge, I was able to come up with a potential solution. Here's what I came up with:

```plaintext
// step 1: creating the six squares

- CREATE six individual buttons in HTML 
- GIVE each button a class name of square
- GIVE them unique IDs

// step 2: Determining a way to change their color when clicked

- ADD a CLICK Event Listener to each button
- CALL a function called UpdateSquares() that changes the color of a clicked button

// step 3: Create a mechanism to track which squares have been clicked

- CREATE an array called `array_sqr` that stores the unique ID of a clicked button
- When a button has been clicked, add the ID to the array

// step 4: devise a method for the squares to return to their original state in the reverse order they were clicked

- When `array_sqr.length == 6` call a function called ReverseSquares()
- In the ReverseSquares() function, loop through `array_sqr`
- Inside the loop, SELECT each button with the unique IDs in `array_sqr`
- REMOVE the color green from the selected button
```

After you have carefully thought about your project, you can now move on to the next step, which is actually building your project.

## How to Solve the Problem and Build the Solution

After careful consideration of the challenge, it's time to move on to building the project. Let's go through the steps:

### Step 1: Create the Six Squares

In this step, we have three things to do: create six individual buttons in HTML, give each button the class name of a square, and give them unique IDs.

You can do that in HTML like this:

```html
<body>
    <div class="wrapper">
        <button class="square" id="1">
            Button 1
        </button>
        <button class="square" id="2">
            Button 2
        </button>
        <button class="square" id="3">
            Button 3
        </button>
        <button class="square" id="4">
            Button 4
        </button>
        <button class="square" id="5">
            Button 5
        </button>
        <button class="square" id="6">
            Button 6
        </button>
    </div>
</body>
<script src="script.js"></script>
```

Above, we just created the buttons with unique IDs just like we wrote down.

### Step 2: Determine a way to change their color when clicked.

In this step, we just have two tasks: ADD a CLICK Event Listener to each button, and then call a function called `UpdateSquares()` that changes the color of a clicked button.

We will do this in JavaScript, so we'll create a new file called `script.js` with the following code:

```js
const buttons = document.querySelectorAll(".square");

for (const button of buttons) {
    button.addEventListener("click", UpdateSquares);
}

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id);
}
```

### Step 3: Create a mechanism to track which squares have been clicked.

In the next step we need to create an empty array called `array_sqr` that stores the unique ID of a clicked button. Then, when a button has been clicked, we need to add the ID to the array. Modifying our code to achieve the above, we have this:

```js
…
let array_sqr = []; // create the empty array

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id); // push the ID to the array
}
```

In the above code, all we have done is keep track of the way the buttons are clicked by storing them in an array.

### Step 4: Devise a method for the squares to return to their original state in the reverse order they were clicked.

In this last step, we have to call a function ReverseSquares() when `array_sqr.length == 6`.

In the `ReverseSquares()` function, loop through `array_sqr`. Inside the loop, select each button with the unique IDs in `array_sqr` and remove the color green from the selected button.

Below is the code to do this:

```js
const buttons = document.querySelectorAll(".square");

for (const button of buttons) {
    button.addEventListener("click", UpdateSquares);
}

let array_sqr = [];

function UpdateSquares(event) {
    const btn = event.target;
    btn.style.backgroundColor = 'green';
    array_sqr.push(btn.id);

    if (array_sqr.length == 6) {
        ReverseSquares();
    }
}

function ReverseSquares() {
    array_sqr.reverse();

    for (const id of array_sqr) {
        const reverse_btn = document.getElementById(id);

        // Remove the color 
        reverse_btn.style.backgroundColor = 'white';

        /* Also clear the array */
        array_sqr = [];
    }
}
```

With the code above, we are practically done with the project, and it works as expected-ish. Take a look at the demo below:

%[https://codepen.io/Spruce_khalifa/pen/PoVReva] 

The only thing left to figure out is that at the moment, all the colors are removed at the same time. So we need to solve this, which will lead us to the final aspect of building our project.

## How to Improve the Solution

Our project currently has a problem where the color is removed from all the squares at the same time. So we need to fix that.

Every project has to undergo this crucial step of making updates and fixes. It's very hard to build a perfect project on your first try. I didn't even build the demo in this tutorial on my first try.

Improving your project can sometimes be even tougher than building the project itself. Fun fact: it took me more time to get the colors to change at different intervals than actually writing the code for the demo I used in this tutorial.

This steps generally involves a lot of Googling and sometimes even asking others for help. It’s perfectly okay to do that – it doesn't make you a bad developer.

Now that we have got that out of the way, let's improve our project. All we have to do is modify the `ReverseSquares()` function like so:

```js
function ReverseSquares() {
    array_sqr.reverse();
    // Use for..of loop to apply different timeouts for each button
    for (const [index, id] of array_sqr.entries()) {
        const reverse_btn = document.getElementById(id);

        // Remove the color after a delay, with increasing delay for each button
        setTimeout(() => {
            reverse_btn.style.backgroundColor = 'white';
        }, index * 1000);

        /* Also clear the array */
        array_sqr = [];
    }
}
```

When everything is put together, you have a solution that works. It might not be perfect, but it works – and that's a win.

%[https://codepen.io/Spruce_khalifa/pen/qBgoYer] 

## Summary

Creating side projects as a junior developer might seem challenging. But by following a systematic approach of thinking things through, planning out your code, actually coding, and then improving on your solution, you can successfully build projects that showcase your skills and creativity.

Don't be afraid to break down larger projects into smaller, more manageable parts. And remember that improvement is an integral part of the development process.

If you have any questions, feel free to message on Twitter at [@sprucekhalifa](https://twitter.com/sprucekhalifa), and don't forget to follow me for more insights and updates. Happy coding!

Photo by [Scott Graham](https://unsplash.com/@homajob?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-holding-pencil-near-laptop-computer-5fNmWej4tAA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
