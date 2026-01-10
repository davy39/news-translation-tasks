---
title: What is JavaScript? JavaScript Code Explained in Plain English
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-25T15:44:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-javascript-javascript-code-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/lagos-techie-tWjzmNXKup4-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "JavaScript was created over 26 years ago and is currently one of the most\
  \ popular programming languages. But what is JavaScript? \nJavaScript is used with\
  \ HTML and CSS to create dynamic and interactive web pages and mobile applications.\
  \ We often call ..."
---

JavaScript was created over 26 years ago and is currently one of the most popular programming languages. But what is JavaScript? 

JavaScript is used with HTML and CSS to create dynamic and interactive web pages and mobile applications. We often call it one of the building blocks of [web development](https://www.freecodecamp.org/news/what-is-web-development-how-to-become-a-web-developer-career-path/).

According to [W3Techs](https://w3techs.com/technologies/details/cp-javascript/), 

> JavaScript is used as client-side programming language by 97.6% of all the websites.  

## History of JavaScript 

In 1995, Netscape developer Brendan Eich created version one of JavaScript in just 10 days. When it first came out it was called Mocha, then later changed to LiveScript and finally settled on JavaScript. 

Brendan Eich's bosses wanted JavaScript to have similar syntax to Java. They also felt that JavaScript was going to help speed up web development and be easier to learn compared to Java. 

Over the years JavaScript has grown and developed into a versatile language that can be used on the web and mobile applications. 

## What is ECMAScript?

ECMAScript stands for European Computer Manufacturers Association Script. According to [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_Resources), 

> **ECMAScript** is the scripting language that forms the basis of JavaScript.

The association created the ECMA standard to make sure that web pages were consistent across different browsers. As of August 2021, there are a total of 12 published versions of ECMAScript. 

## Is Java the same as JavaScript? 

Even though these two languages have similar syntax and share the first four letters of "Java", they are not the same language. 

Here are some key differences between the two languages. 

* Java is a compiled programming language. That means before the program is run, the code needs to be translated into machine code so the computer can understand it. 
* JavaScript is an interpreted language. In the browser, an interpreter will read the code and run it without needing to compile it first. 
* Java is used as a server side (backend) language whereas JavaScript is primarily used as a client side (frontend) language. But JavaScript can also be used to create backend web applications with Node.js. 

## How do HTML, CSS and JavaScript work together on the web page?

Now that we have learned the history of JavaScript, we need to understand how it works on a website. 

HTML renders the content, CSS styles the page to make it look good, and JavaScript makes the site interactive. But what does interactive mean and how does JavaScript work with the other two languages? 

Let's take look at an example to better understand how all three languages work together. 

In this example, when the user clicks a button a message will display with the number of times the user clicked. When the count reaches a certain threshold, the message will change and become more sarcastic as the count rises. 

%[https://codepen.io/jessica-wilkins/pen/xxrxwVp]

We use HTML to create and display the button on the page.

```html
<button id="btn">Click me</button>
```

We also have this `p` element in our HTML which does not have any text in between the opening and closing tags. In JavaScript, the text is added once the user clicks the button. 

```html
<p id="para"></p>
```

We use CSS to style the button and center it on the page.

```css
button {
  display: block;
  margin: 20px auto 10px;
  padding: 25px 20px;
  font-size: 1.4rem;
  cursor: pointer;
  border: none;
  border-radius: 50%;
  background-color: #3b5998;
  color: white;
}
```

In order to access the HTML elements, we use `getElementById`. This is where our JavaScript comes in.

```js
const btn = document.getElementById("btn");
const para = document.getElementById("para");
```

The variable called `count`  keeps track of how many times the user clicks the button. The count is continually updated every time the button is clicked. 

```js
let count = 0;
```

This is the array of responses that will display to the user. 

```js
const responsesArr = [
  "You have clicked the button this many times: ",
  "Wow, you like to click that button. Button clicks: ",
  "Why do you keep clicking it? Button clicks:",
  "Now you are just being annoying. Button clicks:"
];
```

We use the `addEventListener` which tells the computer to listen for a click event. Once the click is detected, then the message will appear on screen with the count.

```js
btn.addEventListener("click", () => {
  count++;
  if (count < 10) {
    para.innerHTML = `${responsesArr[0]} ${count}`;
  } else if (count >= 10 && count < 15) {
    para.innerHTML = `${responsesArr[1]} ${count}`;
  } else if (count >= 15 && count < 20) {
    para.innerHTML = `${responsesArr[2]} ${count}`;
  } else {
    para.innerHTML = `${responsesArr[3]} ${count}`;
  }
});
```

We use an `if else` statement to check how many times the button was clicked and display a different message based on how high the count number is. 

If `count` is less than 10 then this is the message displayed to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.26.30-PM.png)

If `count` is between 10 and 14, then this is the message displayed to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.27.27-PM.png)

If `count` is between 15 and 19, then this is the message displayed to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.28.57-PM.png)

If `count` is 20 or greater, then this is the message displayed to the screen.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.31.35-PM.png)

## How does JavaScript work on a real website?

We just looked at a basic example of how HTML, CSS and JavaScript work together. But how does JavaScript work on real websites?

Let's take a look at the [freeCodeCamp learning platform](https://www.freecodecamp.org/learn). This is an example of a HTML [challenge](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/add-images-to-your-website) from the Responsive Web Design course. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.44.19-PM.png)

 If I pass the challenge, then this message will pop up.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.45.51-PM.png)

But if my answer is incorrect, then the lesson will tell me where the issue is. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.46.41-PM.png)

But how does freeCodeCamp know if my answer is correct or not?

freeCodeCamp writes a series of tests for each challenge to ensure that the code is correct. These tests are written in JavaScript. 

These are the JavaScript tests for the [Add Images to Your Website challenge](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/add-images-to-your-website). 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-24-at-4.51.44-PM.png)

## How to start learning JavaScript 

Here is a list of great resources where you can start learning JavaScript. 

1. [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) (freeCodeCamp)
2. [Learn JavaScript - Full Course for Beginners](https://www.youtube.com/watch?v=PkZNo7MFNFg) (freeCodeCamp YouTube channel)
3. [The Modern JavaScript Tutorial](https://javascript.info/) (javascript.info)
4. [JavaScript Tutorial](https://www.javascripttutorial.net/) (javascripttutorial.net)
5. [LearnJS](https://www.learn-js.org/) (learn-js.org)
6. [Learn JavaScript](https://www.codecademy.com/learn/introduction-to-javascript) (Codecademy)
7. [JavaScript](https://www.sololearn.com/learning/1024) (SoloLearn)
8. [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) (MDN web docs)
9. [JavaScript Tutorial for Beginners: Learn JavaScript in 1 Hour](https://www.youtube.com/watch?v=W6NZfCO5SIk) (Programming with Mosh)

Once you learn the basics of JavaScript, then you can start building your own projects. I have created a list of [40 Beginner JavaScript Projects](https://www.freecodecamp.org/news/javascript-projects-for-beginners/) to get you started. 

## JavaScript libraries and frameworks

JavaScript libraries and frameworks were created to help speed up development. Once you have learned "Vanilla" (or basic/plain) JavaScript then you can start to learn a library or framework.

There are many options to choose from but you don't need to learn them all. Research job postings in your area to see what libraries and frameworks are being used. 

Here are some popular options.

* [React](https://reactjs.org/)
* [Angular](https://angular.io/) 
* [Vue](https://vuejs.org/)

Here are some suggested learning resources.

* [freeCodeCamp's React YouTube course](https://www.youtube.com/watch?v=nTeuhbP7wdE)
* [Brad Traversy's Angular YouTube course](https://www.youtube.com/watch?v=Fdf5aTYRW0E)
* [Brad Traversy's Vue YouTube course](https://www.youtube.com/watch?v=qZXt1Aom3Cs)

## Conclusion

JavaScript was first created in 1995, and has since become a powerful and versatile language used for websites, online games and mobile apps. 

Even though Java and JavaScript have similar syntax and share the first four letters of "Java", they are not the same language. Java is primarily used as a server side language whereas JavaScript is used in the browser. 

HTML, CSS and JavaScript are the three core languages of the web. HTML is for content, CSS is for styling, and JavaScript is for interactivity on the site. 

Hope you found this article helpful and best of luck on your web developer journey. 

