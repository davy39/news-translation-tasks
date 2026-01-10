---
title: Learn JavaScript Form Validation – Build a JS Project for Beginners ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-09-22T18:33:54.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-form-validation-by-making-a-form
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Frame-31.png
tags:
- name: Form validations
  slug: form-validations
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Today we're going to learn how to do form validation in JavaScript. We'l\
  \ also add images and media queries to build out the entire project and keep it\
  \ as a portfolio.  \nHere's the project demo that we're gonna build \U0001F447\n\
  \nDesktop design\nHere's a small ..."
---

Today we're going to learn how to do **form validation** in JavaScript. We'l also add images and media queries to build out the entire project and keep it as a **portfolio**.  

Here's the project demo that we're gonna build 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-30--1-.png)
_**Desktop design**_

Here's a small sample of how the form will work 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dvdfvdf-1.gif)
_**project sample**_

## **You can watch this tutorial on YouTube as well if you like:**

%[https://youtu.be/VufN46OyFng]

## Source code

You can get the source code, including the images, from here:

* [CodePen](https://codepen.io/joyshaheb/pen/XWgdOyY)
* [GitHub](https://github.com/JoyShaheb/Project-image-repo/tree/main/Form-Validation)

# How to Setup the Project

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-1--1-.png)

Follow these steps to set up our project: 👇

* Create a new folder named "Project" and open VS Code
* Create index.html, style.css, and main.js files
* Link the files inside the HTML 
* Download the [images from my GitHub repository](https://github.com/JoyShaheb/Project-image-repo/tree/main/Form-Validation)
* Paste this font-awesome link inside the head tag. Then, we can access Font Awesome icons 👇👇

```html
<link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
      crossorigin="anonymous"
    />
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-2--1-.png)

# Here's what we'll cover:

* Writing the HTML
* Adding the CSS
* Writing the JavaScript
* Adding a social media button
* Adding the images
* Media queries for the mobile version (responsive)

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-20--2-.png)
_**Table of contents**_

# How to Write the HTML

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-3.png)

Create a class named `.container` inside the body tag and host the form tag which will have an id of form 👇

```html
<div class="container">

	<form id="form"></form>
    
</div>
```

And inside the form tag, create 4 `div`s, like this 👇

```html
<form id="form">

    <div class="title">Get Started</div>
    
    <div></div>
    <div></div>
    <div></div>
    
</form>
```

Inside those 3 empty div tags, let's create 3 inputs [Username, Email, and Password] along with the icons and labels.

**Note**: we are creating an `.error` class name. We will inject the error message here using JavaScript. 

#### Username Input

```html
<!-- User Name input -->
        
<div>
	<label for="username">User Name</label>
    <i class="fas fa-user"></i>
    
    <input
        type="text"
        name="username"
        id="username"
        placeholder="Joy Shaheb"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### Email Input

```html
<!-- Email input -->
        
<div>
	<label for="email">Email</label>
    <i class="far fa-envelope"></i>
    
    <input
        type="email"
        name="email"
        id="email"
        placeholder="abc@gmail.com"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### Password Input

```html
<!--   Password input -->
        
<div>
	<label for="password">Password</label>
    <i class="fas fa-lock"></i>
    
    <input
        type="password"
        name="password"
        id="password"
        placeholder="Password here"
     />
    
    <i class="fas fa-exclamation-circle failure-icon"></i>
    <i class="far fa-check-circle success-icon"></i>
    
    <div class="error"></div>
    
</div>
```

#### How to make the button 

Finally, add the button before the form closing tag like this:

```html
<form>
    <!-- other codes are here -->
    
    <button id="btn" type="submit">Submit</button>
    
</form>
```

Here's the result so far 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdgdfgdfdffcvb.png)
_**Result So far**_

Congrats on completing the HTML part! 🍾🎉🥂

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-7.png)

# How to Add the CSS

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-4.png)

Let's add the CSS to style our form. First, let's remove the default styles of our browser including the font-family👇

```css
/**
* ! changing default styles of brower
**/

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: sans-serif;
}
```

Now, apply these styles for the form tag:

```css
/**
* ! style rules for form section
**/

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 400px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  padding: 50px;
}
```

Next, make these changes for our title text: 👇👇

```css
.title {
  font-size: 25px;
  font-weight: bold;
  margin-bottom: 20px;
}
```

Your result so far 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fsdfsdsfxvxcvxd.png)
_**Result so far**_

Now, add a margin to the bottom of our label text like this:

```css
label {
  display: block;
  margin-bottom: 5px;
}
```

And add these styles to change the look and feel of our input tags 👇👇

```css
form div input {
  width: 100%;
  height: 40px;
  border-radius: 8px;
  outline: none;
  border: 2px solid #c4c4c4;
  padding: 0 30px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

```

Add this code to add some space and color changing effects:

```css
form div {
  position: relative;
  margin-bottom: 15px;
}

input:focus {
  border: 2px solid #f2796e;
}
```

The result so far 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdfdfdfdfvdfv.png)
_**Result so far**_

## How to Style the Icons

Now we're gonna style the icons which we imported from font-awesome. Follow along with the code: ✨✨

```css
/**
* ! style rules for form icons
**/

form div i {
  position: absolute;
  padding: 10px;
}

```

Here's the result of adding those two lines 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fddfvdfvdfvgfbh.png)
_**Result so far**_

Now, add these styles to style the error class, along with the success and failure icons 👇👇

```css
.failure-icon,
.error {
  color: red;
}

.success-icon {
  color: green;
}

.error {
  font-size: 14.5px;
  margin-top: 5px;
}
```

Here's the result so far 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ddsfsddsdscsfvv.png)
_**Result so far**_

Look, the success and failure icons are overlapping each other. Don't worry, we will manipulate those in JavaScript. For now, you can hide them like this👇👇

```css
.success-icon,
.failure-icon {
  right: 0;
  opacity: 0;
}

```

Now, let's style our submit button, like this 👇

```css
/* Style rules for submit btn */

button {
  margin-top: 15px;
  width: 100%;
  height: 45px;
  background-color: #f2796e;
  border: 2px solid #f2796e;
  border-radius: 8px;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.1s ease;
}
```

If you want to add a hover effect, then sure, add these styles 👇👇

```css
button:hover {
  opacity: 0.8;
}
```

# Take a Break!

So far so good. Take a break – you deserve it.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-33.png)

# How to Add the JavaScript

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-6.png)

First, we need to target all our classes and id from the HTML inside the JavaScript. To do this task efficiently, make these two functions 👇👇

```css
let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);
```

Then, store the classes and id inside these variables 👇

**Note:** Try not to make spelling mistakes. Otherwise, your JavaScript will not work.

```javascript
let username = id("username"),
  email = id("email"),
  password = id("password"),
  form = id("form"),
  
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");
```

Now, we're gonna target our form and add the **submit** event listener 👇 

```css

form.addEventListener("submit", (e) => {
  e.preventDefault();
});

```

Now, we will create a function named engine which will do all sorts of form validation work for us. It will have three arguments – follow along here: 👇

```js
let engine = (id, serial, message) => {}
```

The arguments represent the following:

* `id` will target our id
* `serial` will target our classes [error class, success and failure icons]
* `message` will print a message inside our .error class 

Now create an `if, else` statement like this 👇

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
  } 
  
  else {
  }
}
```

**Note:** the **`id.value.trim()`** will remove all the extra white spaces from the value which the user inputs. You can get an idea of how it works by looking at this illustration 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-19-1.png)
_**trim() used to remove extra spaces**_

Now, look at our objectives 👇

* We want the JavaScript to print a message inside the **error** class whenever the user **submits a blank** **form**. At the same time, we want the **failure** icons to highlight as well. 
* But, if the user **fills in all the inputs** and submits it, we want the **success** icon to be visible.

To accomplish this, write this logic 👇 to print the message:

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
  } 
  
  else {
    errorMsg[serial].innerHTML = "";
  }
}
```

For the icons to work properly, add this code: 👇👇

```js
let engine = (id, serial, message) => {

  if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
    id.style.border = "2px solid red";
    
    // icons
    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
  } 
  
  else {
    errorMsg[serial].innerHTML = "";
    id.style.border = "2px solid green";
    
    // icons
    failureIcon[serial].style.opacity = "0";
    successIcon[serial].style.opacity = "1";
  }
}
```

Time to implement our newly created function. Write these inside the place where we added the submit event listener 👇

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();

  engine(username, 0, "Username cannot be blank");
  engine(email, 1, "Email cannot be blank");
  engine(password, 2, "Password cannot be blank");
});
```

Here, we are passing the id names, serials of our class names, and passing the message which should be printed when we find an error when the user submits the form. 

Here are the results so far 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dvdfvdf.gif)
_**The Result so far**_

## How to Add the Social Media Buttons

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-10.png)

So far so good, let's add social media sign up options. Follow along here. 👇 

Inside the form tag, create a new `div` with the class name `social`:

```html
<form id="form">

    <div class="social">
    
      <div class="title">Get Started</div>
      
      <div class="question">
        Already Have an Account? <br />
        <span>Sign In</span>
      </div>

      <div class="btn"></div>

      <div class="or">Or</div>
    </div>
    
    <!-- other codes are here-->
</form>
```

Inside the `.btn` class, we create two more divs with class names `.btn-1` and `.btn-2` with the images and text as well

```html
<div class="btn">
  <div class="btn-1">
     <img src="https://img.icons8.com/color/30/000000/google-logo.png" />
     Sign Up
  </div>
  
  <div class="btn-2">
    <img src="https://img.icons8.com/ios-filled/30/ffffff/facebook-new.png" />
     Sign Up
   </div>
</div>
```

Here are the results so far 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfvgdfdsfdsf.png)
_**The Result so far**_

Now, let's style the `.btn-1` and `.btn-2` first. We'll change the alignment of the buttons to row from column 👇

```css
/**
* ! style rules for social section
**/

.btn {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 15px;
}
```

Here's what it looks like now:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfdfdfdbgf.png)
_**The Result so far**_

Now, add styles for the button like this: 👇

```css
.btn-1,
.btn-2 {
  padding: 10px 5px;
  width: 100%;
  display: flex;
  gap: 15px;
  justify-content: center;
  align-items: center;
  border: 2px solid #c4c4c4;
  border-radius: 8px;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
```

Change the icon color and text color of `.btn-2` like this: 👇

```css
.btn-2 {
  background-color: #4f70b5;
  color: white;
}
```

Then add these small changes to make the component look better:

```css
.or {
  text-align: center;
}

.question {
  font-size: 15px;
}

span {
  color: #f2796e;
  cursor: pointer;
}
```

The result so far:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fdfhgnmhg.png)
_**Result so far**_

## How to Add the Images 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-9.png)

Now, let's add images to our project. First, let's write the HTML 👇

```html
<div class="container">

      <div class="content">
        <div class="logo">
          <img src="https://svgshare.com/i/_go.svg" alt="" />
        </div>
        
        <div class="image"></div>
        
        <div class="text">
          Start for free & get <br />
          attractive offers today !
        </div>  
      </div>
      
   <form id="form">
   <!--other codes are here -->
   </form>
   
</div>
```

The result so far 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dfghgjgjgytfh.png)
_**Result so far**_

Now we need to change the orientation of our content from column to row. Follow along 👇

```css
.container {
  display: flex;
  flex-direction: row;
}
```

Add these style rules for the content section:

```css
/**
* ! style rules for content section
**/

.content {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  background-color: #f2796e;
  width: 55%;
  min-height: 100vh;
  padding: 10px 20px;
}

form {
   width: 45%;
   max-width: none;
}
```

The result so far 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/dsffgythjy.png)
_**Result so far**_

Add the main illustration in CSS:

```css
.image {
  background-image: url("https://svgshare.com/i/_gZ.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  /* border: 2px solid black; */
  height: 65%;
}

```

And add these styles for the `.text` class:

```css
.text {
  text-align: center;
  color: white;
  font-size: 18px;
}

form {
   width: 45%;
   max-width: none;
}
```

The result so far 👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/wewrwerew.png)
_**Result so far**_

## How to Add Media Queries for the Mobile Version

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-8.png)

We want to make this responsive. So we'll add media queries to help us with that.

For screens with a width from 900px, we will add these styles. Follow along 👇👇

```css
@media (max-width: 900px) {
  .container {
    flex-direction: column;
  }

  form,
  .content {
    width: 100%;
  }

  .btn {
    flex-direction: column;
  }
  .image {
    height: 70vh;
  }
}
```

For screens with a width from 425px, we will make these minor changes 👇

```css
@media (max-width: 425px) {
  form {
    padding: 20px;
  }
}

```

Here's the final result 👇👇

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fgbgfnghnghnhgmjhgnmhgnhgnggfbgfgfb.gif)
_**The final result**_

# Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Frame-5.png)
_**Congratulations !**_

Congratulations for reading until the end. Now you can easily and efficiently use JavaScript to handle form validation. Not only that, **you also have a project to show your local recruiter!**

Here's your medal for reading till the end ❤️

### Suggestions & Criticisms Are Highly Appreciated ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

* [**LinkedIn/ JoyShaheb**](https://www.linkedin.com/in/joyshaheb/)
* **[YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)**
* **[Twitter / JoyShaheb](https://twitter.com/JoyShaheb)**
* **[Instagram/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

