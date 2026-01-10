---
title: Learn Web Development Basics – HTML, CSS, and JavaScript Explained for Beginners
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-10T21:02:00.000Z'
originalURL: https://freecodecamp.org/news/html-css-and-javascript-explained-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/HTMLCSS.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'If you are learning web development, you will come across terms like HTML,
  CSS, and JavaScript. These are often called the building blocks of the Web.

  These three tools dominate web development. Every library or tool seems to be centered
  around HTML,...'
---

If you are learning web development, you will come across terms like HTML, CSS, and JavaScript. These are often called the building blocks of the Web.

These three tools dominate web development. Every library or tool seems to be centered around HTML, CSS, and JS. So if you want to become a web developer, you need to learn them well.

You'll also discover that websites are mostly built from these three languages.

But you're probably wondering what each one is and what it's really used for. What makes these languages so special and important? And what makes them so ubiquitous that you can’t help but see them in every tutorial and topic based on web development?

Well, now you need wonder no more.

In this article, I will explain the basics of what HTML, CSS, and JavaScript are, how they make the Web work, and what they do on their own.

## What is the Internet?

The internet is simply a network of computers that communicate with each other to send and receive data (information).

Each of these computers on the internet can be distinguished and located by a unique number called an **IP Address.** An IP Address looks something like this: `168.212.226.204`

### What is the Web?

The Web is a subset of the internet.

Like every other computer network out there, the Web is made up of two main components: the web browser client and the web server.

The client requests the data and the server **shares** or **serves** its data. To achieve this, the two parties have to establish an agreement. That agreement is called the **Application Programming Interface** or in short, the **API.**

But this data has to be arranged and formatted into a form that's understandable by end-users who have a wide range of technical experiences and abilities.

This is where HTML, CSS, JavaScript and the whole concept of web development come into play.

## What is HTML?

HTML stands for **Hyper Text Markup Language.**

[Dictionary.com](https://www.dictionary.com/browse/markup) defines a Markup as:

> *a set of detailed instructions, usually written on a manuscript to be typeset, concerning style of type, makeup of pages, and the like.*

So you can think of HTML as the language used for creating detailed instructions concerning style, type, format, structure and the makeup of a web page before it gets printed (shown to you).

But in the context of web development, we can replace the term ‘printed’ with ‘rendered’ as a more accurate term.

HTML helps you structure your page into elements such as paragraphs, sections, headings, navigation bars, and so on.

To illustrate what a page looks like, let's create a basic HTML document:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="./styles.css">
  <title>Document</title>
</head>
<body>
  <h1>This is a first level heading in HTML. With CSS, I will turn this into red color</h1>
  <h2>This is a second level heading in HTML. With CSS, I will turn this into blue color</h2>
  <h3>This is a third level heading in HTML. With CSS, I will turn this into green color</h3>
  <p>This is a <em>paragragh</em> As you can see, I placed an empahisis on the word "paragraph". Now, I will change also
    the background color of the word "paragraph" to black, and its text color  to green, all with just CSS.</p>
  <p>The main essence of this tutorial is to:</p>
    <ul>
       <li>Show you how to format a web document with HTML</li>
       <li>Show you how to design a web page with CSS</li>
       <li>Show you how to program a web document with JavaScript</li>
    </ul>

  <p>Next, I am going to add the following two numbers and display the result, all with JavaScript<p/>
    <p>First number:<span id= "firstNum">2</span> <br></p>
    <p>Second number: <span id= "secondNum">7</span> </p>
    <p>Therefore, the sum of the two of those numbers is: <span id= "answer">(placeholder for the answer)</span></p>
    <input type="button" id="sumButton" value="Click to add!">
</body>
</html>
```

This is how you can format and structure a document with just HTML. As you can see, this markup contains some web elements such as:

* Level 1 heading `h1`
    
* Level 2 heading `h2`
    
* Level 3 heading `h3`
    
* A paragraph `p`
    
* An unordered list with bullet points `ul` `li`
    
* A button input `input`
    
* And the whole body of the page `body`
    

This is what that markup above renders on a web browser:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/HTML.png align="left")

*localhost:3000/index.html*

You can also add attributes to these elements which you can use to identify the elements and access them from other places in the site.

In our example, we set the `id` attributes to all of the three `span` elements. This will help us access them from our JavaScript as you will see later.

Think of this attribute the same way as your social media username. With this name, others can find you on social media. And someone can also refer to you or mention you with this name (you can get tagged in a post, and so on).

This page is very basic and unattractive, though. If you are building anything other than a demo, you will need to add some basic styling to make it more presentable. And we can do exactly that with CSS.

Want to learn more about HTML? You can [start with freeCodeCamp's Responsive Web Design certification](https://www.freecodecamp.org/learn/responsive-web-design/) and this [brand new full HTML course from Beau Carnes](https://www.freecodecamp.org/news/html-crash-course/).

## What is CSS?

While HTML is a **markup language** used to format/structure a web page, CSS is a **design language** that you use to make your web page look nice and presentable.

CSS stands for **Cascading Style Sheets**, and you use it to improve the appearance of a web page. By adding thoughtful CSS styles, you make your page more attractive and pleasant for the end user to view and use.

Imagine if human beings were just made to have skeletons and bare bones – how would that look? Not nice if you ask me. So CSS is like our skin, hair, and general physical appearance.

You can also use CSS to layout elements by positioning them in specified areas of your page.

To access these elements, you have to “select” them. You can select a single or multiple web elements and specify how you want them to look or be positioned.

The rules that govern this process are called [CSS **selectors**](https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/)**.**

With CSS you can set the colour and background of your elements, as well as the typeface, margins, spacing, padding and so much more.

If you remember our example HTML page, we had elements which were pretty self-explanatory. For example, I stated that I would change the color of the level one heading `h1` to red.

To illustrate how CSS works, I will be sharing the code which sets the background-color of the three levels of headers to red, blue, and green respectively:

```css
h1 {
  background-color: #ff0000;
}

h2 {
  background-color: #0000FF;
}

h3 {
  background-color: #00FF00;
}

em {
  background-color: #000000;
  color: #ffffff;
}
```

The above style, when applied, will change the appearance of our web page to this:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/CSS.png align="left")

Cool, right?

We access each of the elements we want to work on by "selecting" them. The `h1` selects all level 1 headings in the page, the `h2` selects the level 2 elements, and so on. You can select any single HTML element you want and specify how you want it to look or be positioned.

Want to learn more about CSS? You can check out the [second part of freeCodeCamp's Responsive Web Design](https://www.freecodecamp.org/learn/responsive-web-design/) certification to get started.

## What is JavaScript?

Now, if HTML is the **markup language** and CSS is the **design language**, then JavaScript is the **programming language.**

If you don’t know what programming is, think of certain actions you take in your daily life:

When you sense danger, you run. When you are hungry, you eat. When you are tired, you sleep. When you are cold, you look for warmth. When crossing a busy road, you calculate the distance of vehicles away from you.

Your brain has been programmed to react in a certain way or do certain things whenever something happens. In this same way, you can program your web page or individual elements to react a certain way and to do something when something else (an event) happens.

You can program actions, conditions, calculations, network requests, concurrent tasks and many other kinds of instructions.

You can access any elements through the [Document Object Model API (DOM)](https://www.freecodecamp.org/news/how-to-manipulate-the-dom-beginners-guide/) and make them change however you want them to.

The DOM is a tree-like representation of the web page that gets loaded into the browser.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/DOM-.png align="left")

*Each element on the web page is represented on the DOM*

Thanks to the DOM, we can use methods like `getElementById()` to access elements from our web page.

JavaScript allows you to make your webpage **“think and act”**, which is what programming is all about.

If you remember from our example HTML page, I mentioned that I was going to sum up the two numbers displayed on the page and then display the result in the place of the placeholder text. The calculation runs once the button gets clicked.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/CSS-1.png align="left")

*Clicking the "Get the sum" button will display the sum of 2 and 7*

This code illustrates how you can do calculations with JavaScript:

```js
function displaySum() {
  let firstNum = Number(document.getElementById('firstNum').innerHTML)
  let secondNum = Number(document.getElementById('secondNum').innerHTML)

  let total = firstNum + secondNum;
  document.getElementById("answer").innerHTML = ` ${firstNum} + ${secondNum}, equals to ${total}` ;
}

document.getElementById('sumButton').addEventListener("click", displaySum);
```

Remember what I told you about HTML attributes and their uses? This code displays just that.

The `displaySum` is a function which gets both items from the web page, converts them to numbers (with the Number method), sums them up, and passes them in as inner values to another element.

The reason we were able to access these elements in our JavaScript was because we had set unique attributes on them, to help us identify them.

So thanks to this:

```html
// id attribute has been set in all three

<span id= "firstNum">2</span> <br> 
    ...<span id= "secondNum">7</span> 
    ...... <span id= "answer">(placeholder for the answer)</span>
```

We were able to do this:

```js
//getElementById will get all HTML elements by a specific "id" attribute
...
let firstNum = Number(document.getElementById('firstNum').innerHTML)
  let secondNum = Number(document.getElementById('secondNum').innerHTML)

  let total = firstNum + secondNum;
  document.getElementById("answer").innerHTML = ` ${firstNum} + ${secondNum}, equals to ${total}` ;
```

Finally, upon clicking the button, you will see the sum of the two numbers on the newly updated page:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/JAVASCRIPT.png align="left")

*2 plus 7 is equals to 9*

If you want to get started with JavaScript, you can check out freeCodeCamp's [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) certification. And you can use this [great Intro to JS course](https://www.freecodecamp.org/news/learn-javascript-full-course/) to supplement your learning.

## How to Put HTML, CSS, and JavaScript Together

Together, we use these three languages to format, design, and program web pages.

And when you link together some web pages with hyperlinks, along with all their assets like images, videos, and so on that are on the server computer, it gets rendered into a **website**.

This rendering typically happens on the front end, where the users can see what's being displayed and interact with it.

On the other hand, data, especially sensitive information like passwords, are stored and supplied from the back end part of the website. This is the part of a website which exists only on the server computer, and isn't displayed on the front-end browser. There, the user cannot see or readily access that information.

## Wrapping Up

As a web developer, the three main languages we use to build websites are HTML, CSS, and JavaScript.

JavaScript is the programming language, we use HTML to structure the site, and we use CSS to design and layout the web page.

These days, CSS has become more than just a design language, though. You can actually implement animations and smooth transitions with just CSS.

In fact, you can do some basic programming with CSS too. An example of this is when you use media queries, where you define different style rules for different kinds of screens (resolutions).

JavaScript has also grown beyond being used just in the browser as well. We now use it on the server thanks to **Node.js**.

But the basic fact remains: HTML, CSS, and JavaScript are the main languages of the Web.

So that's it. The languages of the Web explained in basic terms. I really hope you got something useful from this article.

To round off this article, I have something to share. I recently started a **weekly coding challenge series** aimed at teaching beginners how to program in JavaScript. Check it out on [my blog](https://ubahthebuilder.tech/day-1-who-likes-it).

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
