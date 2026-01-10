---
title: How to build a double slider sign-in and sign-up form
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:30:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-double-slider-sign-in-and-sign-up-form-6a5d03612a34
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6-JxbwsPgUN6VvBZ.gif
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Florin Pop

  Some of you might already know but for those who don’t, I’m starting a Weekly Coding
  Challenge with all of you! ?

  This challenge is meant to help improve our coding skills by practicing on real-life
  projects.

  You can read more about thi...'
---

By Florin Pop

Some of you might already know but for those who don’t, I’m starting a Weekly Coding Challenge with all of you! ?

This challenge is meant to help improve our coding skills by practicing on real-life projects.

You can read more about this challenge and how you can join it by reading [The Complete Guide](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/).

Alright… so the **challenge** for this week was: **Create a Sign in or Sign up form (or both).**

Below you can see a demo of what I’ve created:

![Image](https://cdn-media-1.freecodecamp.org/images/0*6-JxbwsPgUN6VvBZ.gif)

Truth to be told, I’ve struggled a bit with creating the animation ?, but in the end, I managed to make it work. ? I was inspired by this shot on Dr[ibbble b](https://dribbble.com/shots/5311359-Diprella-Login)y SE[LECTO —](https://dribbble.com/selecto) they have some awesome designs, you should check them out!

### Project description

Before we move to the actual code, I’d like to break down the things we’re going to have in the component. This will help as it will make the code we write much clearer.

We have 4 smaller screens/boxes inside the main component (the `.container`):

1. The **Sign In** form
2. The _Sign Up_ form
3. The **Sign In** overlay
4. The _Sign Up_ overlay

Also, at one moment in time you can see either:

* The **Sign In** form alongside the _Sign Up_ overlay
* The _Sign Up_ form alongside the **Sign In** overlay

In the _overlay_ panels, we have some text and a `button`. By clicking it you will bring up the other combination of screens and vice-versa. Check the GIF above one more time to see what I mean.

### The overlay animation — explained

This is where it might be a little trickier, but I’ll do my best to explain so you can understand the logic behind it.

We have the following _layers_ for the overlay component:

**The overlay-container** — this will display the **visible** area (more on this below) at a certain moment in time. It has a `width` of `50%` of the total container's width.

**The overlay** — this div has a double `width` size (`200%`) so it's taking the full width of the main container. (`200% * 50%= 100%`. The 50% is from the `.overlay-container` above).

**The overlay-panel**s — are the divs which are holding the actual content (the text and the button) we see on the screen. They both have a `position` of `absolute`. We can position them wherever we want in the `.overlay` component. One of the panels is positioned to the `left` and the other one is positioned to the `right`. Both having a width of `50%` of the `.overlay` component.

“Why do we need 3 layers?” you might ask… Well, let’s see how it would look like without the first layer:

![Image](https://cdn-media-1.freecodecamp.org/images/0*xbuYkIKyX8a5IlhY.png)

In the picture above you can see that both of the panels are “visible”, which is not what we want. This is why we’re adding the `.overlay-container` to act like a “focus area”. This allows us to hide the panel which is **overflow**ing, or which is out of its boundaries. This is why we needed the `.overlay` to be twice as big as the `.overlay-container`. By moving around the `.overlay-container`, which also has a `position` of `absolute`, we can hide or show which panel we want.

It was a little bit confusing ?, I’ll admit, but I hope I made it clearer.

### The forms animation — explained

These aren’t difficult to understand at all. Basically, we have again two containers — the `.form-container`s. Each has a `width` of `50%` and a `position` - `absolute`. We move both of them at the same time from left to right. When they get behind the `.overlay-container` from above (while these are moving) we quickly change the `z-index` value. The **Sign Up** form (for example) will move on top of the **Sign In** form, and vice-versa. Magic to the eyes, but some code logic behind! ?

### The HTML

Now that we have broken down the core “functionality” of the animation, it’s time to see the actual HTML code. Let’s start with the basic skeleton:

```html
<div class="container" id="container">
    <div class="form-container sign-up-container">
        <!-- Sign Up form code goes here -->
    </div>
    <div class="form-container sign-in-container">
        <!-- Sign In form code goes here -->
    </div>
    <div class="overlay-container">
        <!-- The overlay code goes here -->
    </div>
</div>
```

The main div has a class of `.container` and also an id of `container` because we want to target this element in the JavaScript (more on this below). ?

#### **The Sign Up form**

```html
<div class="form-container sign-up-container">
    <form action="#">
        <h1>Create Account</h1>
        <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
        </div>
        <span>or use your email for registration</span>
        <input type="text" placeholder="Name" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button>Sign Up</button>
    </form>
</div>
```

#### **The Sign In form**

We also have a few classes on each div:

```html
<div class="form-container sign-in-container">
    <form action="#">
        <h1>Sign in</h1>
        <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
        </div>
        <span>or use your account</span>
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <a href="#">Forgot your password?</a>
        <button>Sign In</button>
    </form>
</div>
```

* The `.form-container` class will contain the CSS which is duplicated for both the `.sign-in-container` and `.sign-up-container` classes;
* the 2 different classes (mentioned above) will contain the CSS which is different.

This way we avoid having to write the same CSS code twice and we use the power of being able to add multiple classes.

You might have also noticed that the `i` tags have some classes. These are because we are using [FontAwesome](http://fontawesome.io/) for the icons. Read more about them on their website.

#### **The overlay container**

```html
<div class="overlay-container">
    <div class="overlay">
        <div class="overlay-panel overlay-left">
            <h1>Welcome Back!</h1>
            <p>
                To keep connected with us please login with your personal info
            </p>
            <button class="ghost" id="signIn">Sign In</button>
        </div>
        <div class="overlay-panel overlay-right">
            <h1>Hello, Friend!</h1>
            <p>Enter your personal details and start journey with us</p>
            <button class="ghost" id="signUp">Sign Up</button>
        </div>
    </div>
</div>
```

Same as above, we have a common class `.overlay-panel` and two different classes: `.overlay-left` and `.overlay-right`. Also, we have `id`s for the buttons as we're going to add an **onClick** `eventListener` for both of them in the `JavaScript`.

### The JavaScript

Usually, we cover the CSS before the JS part, but this time it is easier to show and explain the JavaScript code first. It will help you understand the CSS we’re going to have later on.

```js
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});
```

As explained above, we add the event listeners. When the buttons are clicked we `add` or `remove` the `.right-panel-active` class (not the best name for the class, but it’s the best I got at the moment ?). This class will be used to style the subcomponents differently as we have two screens.

### The CSS

First, we have the base CSS for the basic components:

```css
h1 {
    font-weight: bold;
    margin: 0;
}

p {
    font-size: 14px;
    font-weight: 100;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 20px 0 30px;
}

span {
    font-size: 12px;
}

a {
    color: #333;
    font-size: 14px;
    text-decoration: none;
    margin: 15px 0;
}

button {
    border-radius: 20px;
    border: 1px solid #ff4b2b;
    background-color: #ff4b2b;
    color: #ffffff;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
}

button:active {
    transform: scale(0.95);
}

button:focus {
    outline: none;
}

button.ghost {
    background-color: transparent;
    border-color: #ffffff;
}

form {
    background-color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 50px;
    height: 100%;
    text-align: center;
}

input {
    background-color: #eee;
    border: none;
    padding: 12px 15px;
    margin: 8px 0;
    width: 100%;
}

.social-container {
    margin: 20px 0;
}

.social-container a {
    border: 1px solid #dddddd;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 0 5px;
    height: 40px;
    width: 40px;
}
```

Few things to note here:

1. We are styling the elements directly (h1, p, a). Usually, you wouldn’t do that as it might get mixed up with other styles, so it’s good to add a class to each of them. But for this example it’s working ok because we only have these elements on the page.
2. We have a little `transition` on the `button`. When it's clicked, the _active_ state is triggered so we make it a little smaller. Nice and simple clicking effect ?!
3. The `form` is a `flex` container as we want to center everything within it, and it's easy to do that with `flexbox`. You'll see below that it's used a few more times.

The `.container` CSS:

```css
.container {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
}
```

* `Relative` positioned because we'll have `absolute` positioned children elements (explained why, above).
* `Overflow` is set to `hidden` because we have set a `border-radius` and we don't want the child elements to break this radius and be displayed outside of the `.container`.

Now for the fun part, the `.form-container` and related styles:

```css
.form-container {
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

.sign-in-container {
    left: 0;
    width: 50%;
    z-index: 2;
}

.sign-up-container {
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
}

.container.right-panel-active .sign-in-container {
    transform: translateX(100%);
}

.container.right-panel-active .sign-up-container {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: show 0.6s;
}

@keyframes show {
    0%,
    49.99% {
        opacity: 0;
        z-index: 1;
    }

    50%,
    100% {
        opacity: 1;
        z-index: 5;
    }
}
```

**Note** the following:

1. The `animation` (`show`) which is responsible for changing the `z-index` of the `.form-container`s as discussed above. We go by having the z-index **1** from `0-49.99%` and having it at **5** from `50-100%`. These ranges are used because we want them to change fast.
2. We use the `.right-panel-active` class to move around the `.form-container`s when the buttons are clicked.

And finally, the `.overlay-container` and related styles:

```css
.overlay-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform 0.6s ease-in-out;
    z-index: 100;
}

.container.right-panel-active .overlay-container {
    transform: translateX(-100%);
}

.overlay {
    background: #ff416c;
    background: -webkit-linear-gradient(to right, #ff4b2b, #ff416c);
    background: linear-gradient(to right, #ff4b2b, #ff416c);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0 0;
    color: #ffffff;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    transform: translateX(0);
    transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
    transform: translateX(50%);
}

.overlay-panel {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    text-align: center;
    top: 0;
    height: 100%;
    width: 50%;
    transform: translateX(0);
    transition: transform 0.6s ease-in-out;
}

.overlay-left {
    transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
    transform: translateX(0);
}

.overlay-right {
    right: 0;
    transform: translateX(0);
}

.container.right-panel-active .overlay-right {
    transform: translateX(20%);
}
```

* the `.overlay` has a gradient background, I used [UI Gradients](https://uigradients.com/) to get it;
* `.overlay-left` and `.container.right-panel-active .overlay-right` have a `-20%` and `20%` translation on the X-axis. This is because I wanted to add a little effect to the text when it's displayed as if it's coming from outside (sort of) ?;

Other than that… Nothing! We covered everything. We’re done! ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*sv0wmyb-gqD-Tp27.gif)

### Conclusion

This post was a little tough on animations, wasn’t it? ? Nevertheless, I hope you’ve learned something from it.

Don’t forget that you can participate too in the [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) by creating your own version of the **Sign in/up Form.** Share it with me on Twitter: [@florinpop1705](https://twitter.com/@florinpop1705) so I can see it!

Also, you can suggest what we should build for the next Challenge in [this Google Form](https://docs.google.com/forms/d/1oxBbwgMrPCcybKaR90AXxMeITv4kg2f2AelOAVHTqgo).

You can find the live version of the project we’ve built on [Codepen](https://codepen.io/FlorinPop17/full/vPKWjd).

Thank you for spending your time reading this ?, I hope that you learned something new!

_Originally published at [www.florin-pop.com](https://www.florin-pop.com/blog/2019/03/double-slider-sign-in-up-form/)._

