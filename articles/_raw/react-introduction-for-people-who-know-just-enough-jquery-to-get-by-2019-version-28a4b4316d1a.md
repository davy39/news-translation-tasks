---
title: An Introduction to React (For People Who Know Just Enough jQuery To Get By)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T17:32:37.000Z'
originalURL: https://freecodecamp.org/news/react-introduction-for-people-who-know-just-enough-jquery-to-get-by-2019-version-28a4b4316d1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FQnrGf3EajRiFzTH528w7w.png
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Julien Benchetrit

  Back in 2015, @chibicode’s “React.js Introduction For People Who Know Just Enough
  jQuery To Get By” was my first contact with React and the tutorial that demystified
  the whole thing for me.

  It walks you through the fundamentals o...'
---

By Julien Benchetrit

Back in 2015, [@chibicode](https://twitter.com/chibicode)’s “[React.js Introduction For People Who Know Just Enough jQuery To Get By](https://chibicode.com/react-js-introduction-for-people-who-know-just-enough-jquery-to-get-by/)” was my first contact with React and the tutorial that demystified the whole thing for me.

It walks you through the fundamentals of React in a meticulous manner and is especially well-suited for anyone who comes from the world of jQuery.

Unfortunately, when trying to share it recently, I realized it was using React’s now obsolete `createClass` API and the images and embedded code samples weren’t loading anymore.

So with [@chibicode](https://twitter.com/chibicode)’s permission, I rewrote his article with the latest versions of React and JavaScript in mind and expanded upon some of the explanations.

Please note though that the vast majority of this tutorial is his work. I hope it will prove as useful to you as it did to me.

Without further ado, let’s learn us some React!

> **Small disclaimer:** Some of the images are from [@chibicode](https://twitter.com/chibicode)’s original article and the code they show is slightly different from the code we use here. The images are for illustrative purposes only. Always refer to the written code samples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FQnrGf3EajRiFzTH528w7w.png align="left")

#### Target Audience: People Who Know Just Enough jQuery to Get by

Before I begin, I’d like to clarify who the target audience is.

Zed Shaw, the author of “[Learn Code the Hard Way](https://learncodethehardway.org/)” series, wrote an excellent blog post called [Early vs. Beginning Coders](https://zedshaw.com/2015/06/16/early-vs-beginning-coders/). In his post, Zed criticizes programming educators who claim that their materials are for “beginners”, but in reality are incomprehensible for most “total” beginners.

I don’t want to make a similar mistake here. Of the people who have never tried out React, some are comfortable with frontend JS frameworks like [Backbone](http://backbonejs.org/), [Ember](https://emberjs.com/) or [Angular](https://angular.io/). Some know JavaScript pretty well. Some know just enough jQuery to get by. A tutorial that’s effective for one group may not be optimal for the other groups.

In this tutorial, I’m targeting the third group I mentioned: **people who know just enough jQuery to get by**. Examples of people who might fit in this category would be:

* Designers who can do basic coding in HTML/CSS/jQuery.
    
* WordPress developers who know how to use jQuery plugins.
    
* Beginning developers who have completed basic HTML/CSS/JS tutorials online.
    
* Backend developers who rely on Bootstrap and basic jQuery for their frontend needs.
    
* Anyone who does more copy-pasting than architecting when it comes to JavaScript.
    

**If you’re comfortable with JavaScript or any of the frontend frameworks like Backbone/Ember/Angular, this tutorial is NOT for you**, and you’ll be very frustrated with my writing style. There are tons of great tutorials you can learn from, including the [official React tutorial](https://reactjs.org/tutorial/tutorial.html).

Also, **if you already know React**, you’ll be pretty upset with me as well because I’ll be talking mostly about **state** instead of immutability or components. However, I found that teaching state first is the best way for jQuery developers to see why React is superior.

Anyways, let’s get started!

### Time Estimate: 1 ~ 2 hours

If you go really fast (and copy-paste example code instead of typing), this tutorial should take a bit over an hour. If you take your time, it should take a little over 2 hours.

#### If you’re stuck

If you’re stuck or have questions, you can tweet the original author [@chibicode](https://twitter.com/chibicode) or me [@julienbenc](https://twitter.com/julienbenc).

### Overview: We’re Going to Build a “Tweet Box”

Many React tutorials begin by explaining how React works or why React is awesome. This tutorial does not.

Instead, we’ll get right to building a simple UI, alternating between jQuery implementations and React implementations, explaining the differences along the way. I believe that you’ll think more this way as opposed to just typing out examples.

The UI we’ll build will resemble the Tweet box that you find on [Twitter](https://twitter.com/). It won’t be exactly like the real Tweet box but it’ll be pretty similar. Hopefully you’ll find this example to be practical.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R8wu8o8n48hwUQMaQ2Atlg.png align="left")

### Step 1: Introduction to CodePen (5–10 minutes)

We’ll be using [CodePen](https://codepen.io/), an online code editor which supports both jQuery and React code. You might be familiar with similar services like [JSBin](https://jsbin.com) or [JSFiddle](https://jsfiddle.net/) — they’re all pretty similar but I went with CodePen for easier embedding.

Here’s an example Pen:

%[https://codepen.io/julienben/pen/XoYQyj] 

Click “Run Pen” to see what happens when the code is run as well as the code itself (by clicking on the `HTML` button).

Next, click on “Edit on CodePen” to open the Pen in a new window. **You can now modify the HTML on the top left** — i.e. change the button’s text. You’ll see the changes appear in the bottom half of the window. That’s how CodePen works.

#### Create a CodePen Account

Unless you already have a CodePen account, **head to** [**https://codepen.io/**](https://codepen.io/) to **create an account**. Click **Sign Up** to create your account.

After creating an account, you can **fork** public Pens to your account. More or less the same as forking a GitHub repository into your account.

Let’s try it. **Open this next Pen in a new tab and click “Fork” in the top-right menu.**

%[https://codepen.io/julienben/pen/XoYQyj] 

Once you’re on the Pen, you can import popular open-source libraries. You do that by opening Settings and then heading to either the CSS or JavaScript tabs where you can then search for the library you want to add.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fhlnejWv3z1PLhdbsyWjPg.png align="left")

*CSS settings in CodePen*

**Try doing the following in your forked Pen:**

* Add the latest Bootstrap from the CSS tab (the name will be “twitter-bootstrap”)
    
* Add `btn btn-primary` classes on the `<button>` tag
    

And the output becomes a little prettier:

%[https://codepen.io/julienben/pen/dwKEWg] 

#### Create a Tweet Box

You seem to be pretty comfortable with CodePen now. Alright, let’s build out a Tweet box. Still on the same Pen as before, **change the HTML inside** `<body>` like this:

```html
<div class="card bg-light">
  <div class="card-body text-right">
    <textarea class="form-control"></textarea>
    <br/>
    <button class="btn btn-primary">Tweet</button>
  </div>
</div>
```

We’re using Bootstrap classes like `form-control`, `card`, `card-body`, etc. but those are just for the looks and irrelevant for the tutorial. Here’s the result:

%[https://codepen.io/julienben/pen/jXKgZo] 

That’s it for the first step! Not too bad, eh?

### Step 2: Implement the First Feature — Tweet Button Should Initially Be Disabled (5 minutes)

Now, time for some JS. We’ll first implement the following feature:

**Feature 1:** the “Tweet” button should initially be disabled. When there’s at least one character in the text field, the “Tweet” button should be enabled.

Here’s the demo Pen. As you can see, the button is initially disabled. If you type something into the text box, the button becomes enabled.

%[https://codepen.io/julienben/pen/gZKVjd] 

To get this to work, you first need to add jQuery into the Pen. Do that inside the JavaScript tab in your Pen’s Settings. (If you’re having trouble with this step, check out CodePen’s [official instructions](https://blog.codepen.io/documentation/editor/using-javascript-libraries/).) **Once that’s done, go to the small JavaScript window and add the following jQuery code.**

```js
// Initially disable the button
$("button").prop("disabled", true);
// When the value of the text area changes...
$("textarea").on("input", function() {
  // If there's at least one character...
  if ($(this).val().length > 0) {
    // Enable the button.
    $("button").prop("disabled", false);
  } else {
    // Else, disable the button.
    $("button").prop("disabled", true);
  }
});
```

#### Explanation

* I used the tag names `button` and `textarea` as selectors — no need to add IDs or classes for this example.
    
* To enable/disable the button, use `$(...).prop("disabled", ...)`.
    
* To listen for changes in `textarea`, use the `input` event which works on modern browsers.
    

**Try it out** by typing some text in the Tweet box and seeing the button’s enabled/disabled state change.

DO NOT PROCEED if this example was confusing to you — you might need to learn some more jQuery before moving onto React. There are lots of excellent learning resources like [Codecademy](https://www.codecademy.com), [Treehouse](https://teamtreehouse.com/), [Code School](https://www.pluralsight.com/codeschool), and others.

Now that this feature is complete, we’ll try to re-implement the same thing using React. This will take several steps.

### Step 3: The Tweet Box Using React (5–10 minutes)

One of the first things you’ll notice in React is that **you’ll be writing markup in JS, not in HTML**.

Let me show you what I mean. Here’s the React code which displays the same Tweet box.

#### WARNING! You don’t need to follow along yet — just read the code.

%[https://codepen.io/julienben/pen/majbMg] 

Some observations:

* Inside `return (...)` is HTML-like code, not JavaScript. In React, you’ll write in a special syntax called JSX which lets you put HTML-like code inside JavaScript.
    
* I say HTML-“like” because it’s not identical to HTML. Notice that it uses `className` instead of `class` — but it’s pretty similar, so you’ll learn it quickly.
    
* Your browser does not understand JSX so, before the code can be run, it is automatically converted into browser-compatible JavaScript by a JS compiler (called Babel).
    
* The HTML code inside `return (...)` is pretty much identical to the HTML code from step 1.
    
* Look at the remaining HTML code in our Pen and you’ll see that there’s no markup besides `<body><div id="container">&`lt;/div&gt;. This is what I **meant when I said that in React you’ll be writing markup in JavaScrip**t (JSX) and not in HTML.
    

#### Frequently Asked Questions & Answers

**Question:** What do `class TweetBox extends React.Component` and `ReactDOM.render` do? Do I need to understand them now?  
**Answer:** Don’t worry about it for now. Basically, the first declares a React component with a name (in this case, `TweetBox`). This then gets rendered in the DOM via `ReactDOM.render(<TweetBox />, document.getElementById("contai`ner")) — meaning this component is added insid`e the <div id="co`ntainer"&gt; tag. That’s all you need to know for now.

**Question:** Do I need to do anything special to write JSX on my local machine?  
**Answer:** Yes, but that’s outside the scope of this tutorial — in short, you need to enable something called Babel compilation. All you need to do to write JSX on CodePen is to (1) add the React and ReactDOM libraries and (2) select “Babel” from the list of JavaScript Preprocessors in the JS settings window.

**Question:** Isn’t it bad practice to write markup (HTML) and behavior (JS) in the same place?  
**Answer:** It might be bad practice for simple web pages but not necessarily so for large web applications. In large web applications, there will be hundreds of pieces of UI, each containing their own markup and behaviors. The code will be more manageable if the markup and behaviors are kept together for each piece of UI, as opposed to keeping “all markup” together and “all behaviors” together. And React is designed for developing large web applications. In fact, React is developed and used by Facebook, one of the largest web applications out there.

Next, I’ll show you how to write the above React code step-by-step.

### Step 4: Writing Your First React Code (5–10 minutes)

Here’s a starter Pen. In it, I’ve imported Bootstrap (the CSS portion) and React. I also set the JavaScript Preprocessor to Babel so we can write classes and JSX.

**Please try to follow along. To begin, fork this Pen so you can edit and save as you go.**

%[https://codepen.io/julienben/pen/YdjeWj] 

Now you’re ready to write some React. **Try to follow along and type the following JS code snippets** into your Pen.

```js
class TweetBox extends React.Component {
  render() {
    return null;
  }
};
```

This is the template for creating a piece of UI using React (in this case, a Tweet box). It’s just as essential as `$(selector).append('your HTML code or element')` in jQuery.

To actually construct the UI, we must write the `render()` method. For now, let’s keep it simple with just a single `div` tag.

```js
class TweetBox extends React.Component {
  render() {
    return (
      <div>
        Hello World!
      </div>
    );
  }
};
```

Like in the example above, **put a pair of parenthesis after** `return`, and write the markup inside.

#### JSX Gotchas

There’s one thing you need to remember with JSX — in `render()`, you must return only **one** outermost tag (or anything that can be considered a valid DOM node such as a string or a string).

This will work because it’s a string:

```javascript
return 'Hello World!';
```

But the following won’t work because there’s no quotes or outermost tag around the text:

```js
return (
  Hello World!
);
```

This also doesn’t work because there are two outer-most (`span`) tags inside `return (…)`:

```js
return (
  <span>
    Hello
  </span>
  <span>
    World
  </span>
);
```

For the above example, the workaround is to create an extra `div` tag to wrap the two `span` tags.

```js
return (
  <div>
    <span>
      Hello
    </span>
    <span>
      World
    </span>
  </div>
);
```

We used a `div` here but in the most recent versions of React, you can use the Fragment feature to render multiple outermost tags. Like this:

```js
return (
  <React.Fragment>
    <span>
      Hello
    </span>
    <span>
      World
    </span>
  </React.Fragment>
);
```

#### Attaching the UI to the DOM

Now we need to “attach” this UI to the DOM in order to see `Hello World`. To do this, **add** `ReactDOM.render()` underneath the code we just wrote:

```js
class TweetBox extends React.Component {
  ...
};
ReactDOM.render(
  <TweetBox />,
  document.getElementById("container")
);
```

(**Note**: an ellipsis (…) in the code snippet indicates code that has been omitted for clarity. In other words, don’t touch this part of the code and leave it as is.)

`ReactDOM.render` takes two arguments. The first argument is the React component, which is `<VariableName` /&gt;. The second argument is the DOM element where we want to render (in this `case, document.getElementById('conta`iner')). Put together, the above code render`s the Tw`eetBox UI i`nside <div id="co`ntainer"&gt;.

Now, you should see `Hello World` appear in your Pen. Congratulations, you wrote and rendered your first React component!

#### Write the Actual HTML for the Tweet Box

Now, instead of `Hello World`, we’ll implement the HTML for the Tweet Box. **Swap the code inside** `render()` with this:

```js
return (
  <div className="card bg-light">
    <div className="card-body text-right">
      <textarea className="form-control" />
      <br />
      <button className="btn btn-primary">Tweet</button>
    </div>
  </div>
);
```

There are two things you need to watch out for:

* **Don’t use** `class`. Instead, use `className`. It’s because JSX gets translated to JS and `class` is a reserved keyword in JS.
    
* **If you use** `<`br&gt; inste`ad of`  
    , you’ll get an error. Make sure to close all tags. Same thing w`ith images: <img src`\="…" alt="…" /&gt;
    

Everything else should be the same as the jQuery example from before.

If you typed this correctly, then you should see the Tweet box in your Pen. **If nothing appears in the output, check your code very carefully to make sure there aren’t any typos.**

That’s it for this step! Here’s the Pen up to this part:

%[https://codepen.io/julienben/pen/majbMg] 

### Step 5: Re-implement the First Feature — Tweet Button Should Initially Be Disabled — in React (5–10 minutes)

We’re going to re-implement with React the first feature we implemented using jQuery:

**Feature 1:** The “Tweet” button should initially be disabled. When there’s at least one character in the text field, the “Tweet” button should be enabled.

Here’s the jQuery code we wrote:

%[https://codepen.io/julienben/pen/gZKVjd] 

Let’s see how we can do this in React.

**Start with your Pen from the previous step.** (**Tip:** Since you won’t be touching HTML in React, **you can minimize the HTML tab on CodePen** to get more screen space. Same thing with the CSS tab.)

**First, let’s disable the button by adding** `disabled` as an attribute.

```js
render() {
  return (
    ...
    <button className="..." disabled>Tweet</button>
    ...
  );
}
```

In JSX, this is equivalent to writing `disabled={true}`.

The button should now be disabled. Note that in our jQuery implementation we wrote:

```js
$("button").prop("disabled", true);
```

to initially disable the button, but we could have instead modified the button tag like above.

Now, we need to enable the button when there’s at least one character in the text field.

#### Handle Change Event

First, we need to listen for the user typing in the `textarea`. In our jQuery implementation, we wrote:

```js
$("textarea").on("input", function() {
  ...
}
```

In the React world, we write the event handler as a **class method**. Let’s call it `handleChange`:

```js
class TweetBox extends React.Component {
  handleChange = () => {
  };
  render() {
    ...
  }
}
```

> Note that we’re using an arrow function so that we can access the class’s context (`this`) without having to bind the function in the `constructor`. Explaining this in-depth is outside the scope of this tutorial but you will very likely learn about it in due time.

Next, we call this handler when text is entered. To do so, **modify the** `textarea` tag in `render()` like this:

```html
<textarea className="form-control" onChange={this.handleChange}>
</textarea>
```

* We used the `input` event for jQuery but in React we use `onChange` — you’ll learn about how events differ in React’s JSX from the official React documentation so don’t worry too much for now.
    
* **More importantly**, we used curly brackets to include JavaScript code inside the HTML syntax part of JSX. In this case, we passed the handler `handleChange` and we prefixed it with `this` because it’s a class method.
    
* If you’re used to jQuery, this might seem like bad practice but don’t worry. Again, in large applications, the code will be more manageable if the markup and behaviors are kept together for each piece of UI.
    

To make sure that the handler is indeed being called, **let’s add** `console.log` inside `handleChange`:

```js
handleChange = (e) => {
  console.log(e.target.value);
};
```

The `event` object (nicknamed `e`) contains `target` which is the `textarea`. We get the `value` to output the current content of the `textarea`.

**In your Pen, open the** `console` tab (with the button in the bottom left of the screen) to check the output. Then type something in the Tweet box.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8mSEfP4wqKBTHRGLaR64_Q.png align="left")

*The console button in CodePen*

You can also try it out here (you’ll need to open the Pen in a new tab to see the `console` button):

%[https://codepen.io/julienben/pen/aPaoOJ] 

That’s it for this step! We’ll finish this feature in the next step.

**NOTE: Close the** `console` tab in CodePen when you’re done. We no longer need it.

### Step 6: Implementing State (10–15 minutes)

I’ll now explain one of the biggest differences between jQuery-style code and React-style code.

In jQuery, when some event happens, you usually modify the DOM directly (like we did earlier with `$("button").prop("disabled", true)`):

![Image](https://cdn-media-1.freecodecamp.org/images/0*IhZHTYtjhRnTru2C align="left")

In React, **you never modify the DOM directly.** Instead, in an event handler, you modify something called **the “component state”**. And this is done by calling `this.setState`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vB6BPnDRykxd2PFP align="left")

Then, every time the `state` is updated, `**render()**` **is called again.** And **inside** `render()` you can access the state to tell React how you want the DOM to be modified.

![Image](https://cdn-media-1.freecodecamp.org/images/0*g9bDPyxJef0yg00Y align="left")

This is how you update the UI in response to an event. Yes it’s confusing at first so let me explain using code.

#### Writing the Event Handler

**Start with your Pen from the previous step.** First, we need to **initialize the state object.** We can do that inside the class `constructor`.

What goes in the object? **Let’s create a single key called** `text` and have it store whatever is inside the Tweet box.

```js
class TweetBox extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      text: '',
    };
  }
  
  handleChange = (e) => {...};
  render() {...}
};
```

> Don’t worry about why we’re calling `super(props)` at the top of our `constructor`. It’s an important step but not necessary to understand React for now.

**Next, we’ll modify the event handler** to set the state’s `text` field to whatever is currently in the `textarea`. To do this, **we use a special method called** `setState` and pass the updated key-value pair.

```js
handleChange = (e) => {
  this.setState({ text: e.target.value });
};
```

Now, let’s check that the state is correctly being set by writing some debug-only code in `render()`.

To do this, **simply add** `this.state.text` near the end of `render()` and use curly brackets to use JS code inside the HTML syntax part of JSX.

```js
render() {
  return (
    <div className="card bg-light">
      ...
      {this.state.text}
    </div>
  );
}
```

**Now, try entering some text in the Tweet box.** The same text should appear below the button.

You can try it out on the Pen below as well:

%[https://codepen.io/julienben/pen/XoPrzR] 

Now the previous diagram might make more sense to you:

![Image](https://cdn-media-1.freecodecamp.org/images/0*8hdVUZaiVqm8J2mq align="left")

#### Remove the Debugging Code

Once you confirm that the state is correctly being set, **remove the debugging code we just added:**

```javascript
{this.state.text}
```

#### Enabling/Disabling the Button

Now that we can listen for text changes, the next step is to enable/disable the `button` depending on whether the `text` is empty or not.

Using the `state`, we can use this logic:

* If `this.state.text.length === 0`, the button should be disabled.
    

To do this in React, **add the** `disabled` attribute and set its value as the output of `this.state.text.length === 0`. Since this is JS code, you need to wrap it with `{}`.

```html
<button className="btn btn-primary" disabled={this.state.text.length === 0}>Tweet</button>
```

If you write `disabled="true"` or `disabled="false"` in raw HTML it won’t work — in raw HTML, you need to add/remove the `disabled` attribute to enable the `button`. But React is **not** raw HTML — it does the following behind the scenes:

* If you write `disabled={true}` in JSX, it gets converted to just `<button disabl`ed&gt; in HTML.
    
* If you write `disabled={false}` in JSX, the `disabled` attribute is removed from the `button` tag in HTML.
    

This works with other Boolean attributes like `checked`. (You can read more about this aspect of JSX [here](https://reactjs.org/docs/dom-elements.html).)

The resulting Pen is below:

%[https://codepen.io/julienben/pen/GPXKYa] 

#### Reflections

Again, keep this difference between jQuery and React in mind before moving on to the next step:

* In jQuery, you write event handlers which **modify the DOM**.
    
* In React, you write event handlers which **modify the state**. And you write `render()` to reflect the current state.
    

### Step 7: Remaining Character Count in jQuery (5 minutes)

The next feature we’ll implement is the remaining character count.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9ONPNObC5R_IeBvq align="left")

Here’s the spec:

* The character count will display `280 — the length of the text`.
    

**We’ll first implement this in jQuery, then in React.**

We’ll start with our previous jQuery implementation and put our React code on hold for now. **Going forward, I will give you new code to start with at the beginning of each chapter**, as we alternate between jQuery and React. That means after you’re done with each step, you can play with the code before moving to the next step.

**✔ Fork the Pen below** to get started.

%[https://codepen.io/julienben/pen/gZKVjd] 

First, **add the character count in HTML.** Let’s set it inside a `span`:

```js
<textarea {...}></textarea><br>
<span>280</span>
<button {...}>Tweet</button>
```

And **inside the input handler in JS, add this code to update the character count:**

```js
$("textarea").on("input", function() {
  $("span").text(280 - $(this).val().length);
  ...
});
```

That’s it! **Try typing in the Tweet box** and you’ll see the character count gets updated as you type. Here’s the Pen:

%[https://codepen.io/julienben/pen/gZdJNJ] 

### Step 8: Remaining Character Count in React (5 minutes)

How about in React? You should try doing this on your own. Start with our previous React implementation.

**✔ Fork the Pen below** to get started.

%[https://codepen.io/julienben/pen/GPXKYa] 

(**Tip:** Since you won’t be touching HTML in React, **you can minimize the HTML tab on CodePen** to get more screen space.)

**Hints:**

* No need to change the `constructor()` or `handleChange()` methods.
    
* Use `this.state.text.length` in `render()`.
    

#### Answer:

Add this code after `<b`r/&gt; in `your re`nder():

```html
<span>{280 - this.state.text.length}</span>
```

Here’s the Pen:

%[https://codepen.io/julienben/pen/QzVXOd] 

Too easy? Not sure why building UIs with React is so much better than jQuery? Well, the next step has more complexity and this is where React really starts to shine.

### Step 9: The “Add Photo” Button (5 minutes)

![Image](https://cdn-media-1.freecodecamp.org/images/0*N697jN99MCP3cfUn align="left")

For our next feature, we’ll add an “Add Photo” button to the Tweet Box. This is where things start to get tricky.

However, **we won’t actually write the code to upload images.** Instead, here’s what we’re going to do:

When you upload a photo on Twitter, it counts against the character limit. On my attempt, it decreased the number of remaining characters from 280 to 257.

> Yes, I know that Twitter no longer counts photos against the character limit but we’ll disregard that for this tutorial.

Here’s the spec:

* Create an “Add Photo” button.
    
* Clicking this button toggles an **ON/OFF state.**
    
* If the button is ON, it will say `**✓ Photo Added**` and the number of available characters decreases by 23.
    
* Also, if the button is ON, **even if there’s no text entered, the “Tweet” button remains enabled.**
    

Here’s the demo CodePen. **Try clicking the “Add Photo” button** and see what happens to the character count and the Tweet button.

%[https://codepen.io/julienben/pen/roZXvE] 

Let’s implement this with jQuery first.

### Step 10: The “Add Photo” Button in jQuery (15–20 minutes)

Start with the latest version of our jQuery implementation.

**✔ Fork the Pen below** to get started.

%[https://codepen.io/julienben/pen/gZdJNJ] 

Earlier, we were attaching a handler to `$("button")` but this won’t work anymore if we have two buttons. **So let’s modify the HTML like this:**

```html
...
<button class="js-tweet-button btn btn-primary" disabled>Tweet</button>
<button class="js-add-photo-button btn btn-secondary">Add Photo</button>
...
```

Here are the changes:

* **Added the second button** which says “Add Photo”.
    
* **Added classes** `js-tweet-button` and `js-add-photo-button` to each button. The class names are prefixed with `js-` to remember that they’re used only in JS and not in CSS.
    
* **Added the initial** `disabled` attribute to the Tweet button so we don’t have to do it in JS.
    

**Next, rewrite the entire JS file like this:**

```js
$("textarea").on("input", function() {
  $("span").text(280 - $(this).val().length);
  if ($(this).val().length > 0) {
    $(".js-tweet-button").prop("disabled", false);
  } else {
    $(".js-tweet-button").prop("disabled", true);
  }
});
```

Here are the changes:

* **(Important) Removed** `$("button").prop("disabled", true);` from the first line because we added the `disabled` attribute directly to the Tweet button.
    
* **Replaced** `$("button")` with `$(".js-tweet-button")` so it can be distinguished from `.js-add-photo-button`.
    

#### Adding the Button

Next, we’ll implement one of the features:

* Clicking the “Add Photo” button toggles the ON/OFF state. **If it’s ON, the button will say** `✓ Photo Added`.
    

To do this, **let’s add this piece of code:**

```js
$("textarea").on("input", function() {
  ...
});

$(".js-add-photo-button").on("click", function() {
  if ($(this).hasClass("is-on")) {
    $(this)
      .removeClass("is-on")
      .text("Add Photo");
  } else {
    $(this)
      .addClass("is-on")
      .text("✓ Photo Added");
  }
});
```

We use the class `is-on` to keep track of the state. **Check to see that this works** by clicking the “Add Photo” button multiple times and seeing the text alternate.

#### Decrement Character Count

Next, we’ll implement this feature:

* If the “Add Photo” button is ON, **the number of available characters decreases by 23.**
    

To do this, **modify the click handler we just added like this.**

```js
if ($(this).hasClass("is-on")) {
  $(this)
    .removeClass("is-on")
    .text("Add Photo");
  $("span").text(280 - $("textarea").val().length);
} else {
  $(this)
    .addClass("is-on")
    .text("✓ Photo Added");
  $("span").text(280 - 23 - $("textarea").val().length);
}
```

We change the `span`’s content on every click. If the `button` is ON, we need to subtract the text length from `257` (i.e. `280 — 23`). We use `280 — 23` for clarity right now but, if we were building a production app, we should use constants instead.

**Check to see that this works** by clicking the “Add Photo” button.

#### Fixing the Input Handler

This isn’t complete however — **if you have the “Add Photo” button ON and start typing in the** `textarea`, the remaining character count goes out of sync.

This happens because the handler for the `textarea` doesn’t take into account the status of the “Add Photo” button.

To fix this, **we need to update the handler for** `textarea` like this:

```js
$("textarea").on("input", function() {
  if ($(".js-add-photo-button").hasClass("is-on")) {
    $("span").text(280 - 23 - $(this).val().length);
  } else {
    $("span").text(280 - $(this).val().length);
  }

  if (...) {
    ...
  }
});
```

**Make sure that this works** by turning on the “Add Photo” button and then typing some text.

#### I know this is taking some time…

But stick with it! The jQuery code here is ***supposed*** to be confusing so don’t worry!

#### Implement the Last Feature

The last feature we need to implement is this:

* If the “Add Photo” button is ON, **even if there’s no text entered, the “Tweet” button remains enabled.**
    

To do this, **we need to modify the click handler of the “Add Photo” button:**

```js
$(".js-add-photo-button").on("click", function() {
  if ($(this).hasClass("is-on")) {
    ...
    if ($("textarea").val().length === 0) {
      $(".js-tweet-button").prop("disabled", true);
    }
  } else {
    ...
    $(".js-tweet-button").prop("disabled", false);
  }
});
```

Here’s the explanation:

* If the “Add Photo” button is going from ON to OFF (`if` clause), we need to check if there’s no text entered and, if so, disable the “Tweet” button.
    
* If the “Add Photo” button is going from OFF to ON (`else` clause), we always enable the “Tweet” button.
    

#### But again, this is broken

We’re not done yet. There’s a bug in the code right now. **Try it out yourself by following these steps:**

* Turn on the “Add Photo” button.
    
* Type some text.
    
* Delete all of the text.
    
* The “Tweet” button should still be enabled because the “Add Photo” button is ON, but this isn’t the case.
    

This means that our input handler for `textarea` is missing some logic. To fix this, **we need to add another condition to the** `if` statement in the input handler.

```js
$("textarea").on("input", function() {
  ...
  if ($(this).val().length > 0 || $(".js-add-photo-button").hasClass("is-on")) {
    ...
  } else {
    ...
  }
});
```

This is the explanation for this additional condition:

* When the text changes, **if the text isn’t empty OR if the “Add Photo” button is ON**, do not disable the “Tweet” button.
    

**Try the above steps again** and this time it will work as expected.

### Step 11: Reflection on the jQuery Code — Why So Confusing? (5 minutes)

Here’s the final HTML and JS code from the previous step:

%[https://codepen.io/julienben/pen/YdJKqE] 

**Take a look at the jQuery code once again.** It’s very confusing. If you’re keeping the code as-is, you’ll probably need comments everywhere to remember how it works. There are also clear signs of code duplication but you’d have to think quite a bit before refactoring.

The question is: **why did it get so ugly so fast?**

The answer has to do with the **“jQuery style”** of code we talked about previously. Recall this diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/0*9p-0fEB0Z2DPuFF7 align="left")

Things are simple when there is only 1 event handler and 1 DOM element. However, as we just saw, **if several event handlers are modifying several parts of the DOM, the code gets ugly and complicated.**

This is an example of what people mean when they say “spaghetti code”.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YTtV7PD_apkzdYMw align="left")

Imagine adding more features that could influence both the character limit and the “Tweet” button state. The code would become even harder to manage.

You can, in theory, mitigate this by refactoring into reusable functions. But you’d still have to think hard about it every time you add something new.

> **Note:** Someone shared a [refactored version of the jQuery code](https://pastebin.com/wbGZZs7U) (for the original tutorial). Very clean. You’ll notice that the `update()` function takes care of most of the updates to the DOM based on its current “state”. The event listeners then run this function on every call.

> In that way it’s similar to React’s `render`. However, there are still many downsides to this solution. For one, the absence of a real `state` object makes the logic more opaque. It also doesn’t allow you to break down your UI into multiple components and is likely to have performance issues as you continue adding to it.

Now, let’s see what it’s like to do the same thing with React.

**Spoiler alert: It’s going to be much simpler.**

### Step 12: The “Add Photo” Button in React (10–20 minutes)

Let’s start with our previous React implementation.

**✔ Fork the Pen below** to get started.

%[https://codepen.io/julienben/pen/QzVXOd] 

#### Adding the Button

First, let’s add the “Add Photo” button. **Modify the JSX:**

```html
<button ...>Tweet</button>

<button className="btn btn-secondary">
  Add Photo
</button>
```

Now, let’s add a click handler to this button so that the text changes from `Add Photo` to `✓ Photo Added`. Recall the React way of writing code:

![Image](https://cdn-media-1.freecodecamp.org/images/0*FWEJiHF2VzD8p8L2 align="left")

We will:

1. **Create a state variable** that keeps track of whether the “Add Photo” button is ON or OFF.
    
2. **Use the state** in `render()` to decide whether to show `Add Photo` or `✓ Photo Added`.
    
3. **Update the state** in the click handler.
    

For (1), **we’ll modify the initial state in the** `constructor` by adding a key-value pair to keep track of whether the photo is added or not:

```js
constructor(props) {
  super(props);
 
  this.state = {
    text: '',
    photoAdded: false,
  };
}
```

For (2), **we’ll modify the JSX markup** for the “Add Photo” button. We’ll have the button say “Photo Added” if `this.state.photoAdded` is true. We can just use a [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) here:

```html
<button className="btn btn-secondary">
  {this.state.photoAdded ? "✓ Photo Added" : "Add Photo" }
</button>
```

Finally, for (3), **we’ll attach an event handler on JSX** like we did for the `textarea`:

```html
<button className="btn btn-secondary" onClick={this.togglePhoto}>
  {this.state.photoAdded ? "✓ Photo Added" : "Add Photo" }
</button>
```

Notice that we’re using `onClick` instead of `onChange`. This is because we’re dealing with a `button` and not a `textarea` or an `input`.

We’ll also **add a handler method which toggles the value of** `this.state.photoAddded`:

```js
togglePhoto = () => {
  this.setState((prevState) => ({ photoAdded: !prevState.photoAdded }));
}
```

This time you’ll see that we’re passing a function to `this.setState`. This is necessary if you want to update your component state but need to use a value from the previous state. Why we do that is outside the scope of this tutorial but you can read about it in [this section](https://reactjs.org/docs/state-and-lifecycle.html#using-state-correctly) of the official React documentation.

Now, clicking on Add Photo should toggle the button text. **Try it out yourself.**

#### Decrement Character Count

We’ll now implement the next feature:

* If the “Add Photo” button is ON, **the number of available characters decreases by 23.**
    

Currently, the number of available characters is displayed as follows in `render()`:

```javascript
<span>{280 - this.state.text.length}</span>
```

This value will now also depend on `this.state.photoAdded` so we need an `if` and `else` here.

However, **in JSX, you can’t write** `if` or `else` inside `{ ... }`. You could use a ternary expression (`a ? b : c`) like we did earlier but it would be pretty long and hard-to-read in this case.

Often the simplest solution in this situation is to refactor a conditional into a method. Let’s try it.

**First, modify the above code to use a class method, like this**:

```html
<span>{this.getRemainingChars()}</span>
```

**And define the method like this:**

```js
getRemainingChars = () => {
  let chars = 280 - this.state.text.length;
  if (this.state.photoAdded) chars = chars - 23;
  return chars;
}
```

Now, the remaining character count should update as expected when the “Add Photo” button is toggled.

**Question**: In `render()`, why does `{this.getRemainingChars()}`have `()` but `{this.handleChange}` and `{this.togglePhoto}` don’t?

Good question. Let’s take a look at `render()` again:

```js
render() {
  return (
    ...
      <textarea className="..." onChange={this.handleChange}></textarea>
    ...
    
    <span>{this.getRemainingChars()}</span>
    ...    
          
    <button className="..." onClick={this.togglePhoto}>
      ...
    </button>
    ...
    );
  }
```

**Answer**:

* We’ve written the `getRemainingChars()` method to **return a number**. We need to get this number and put it inside `<span>&`lt;/span&gt;, so **we n**eed `to call the getRema`iningChars() meth`od` by using (). That’s `wh`y we `have () in getRema`iningChars().
    
* On the other hand, `handleChange` and `togglePhoto` are **event handlers**. We want these methods to be called only when the user interacts with the UI (typing in the `textarea` or clicking a `button`). To do so, we need to write them without `()` in `render()` and assign them to attributes like `onChange` and `onClick`. React will take care of attaching the methods to the relevant event listeners for us.
    

#### The “Tweet” Button’s Status

We have one more feature to implement:

* If the “Add Photo” button is ON, **even if there’s no text entered, the “Tweet” button remains enabled.**
    

This is actually really easy thanks to React. Previously, the Tweet button’s `disabled` option was set as:

```html
<button ... disabled={this.state.text.length === 0}>...</button>
```

In other words, previously the “Tweet” button was disabled if the text’s length was 0. **Now, the “Tweet” button is disabled if**:

* The text’s length is 0
    
* **AND**
    
* The “Add Photo” button is OFF.
    

So the logic looks like this:

```html
<button ... disabled={this.state.text.length === 0 && !this.state.photoAdded}>...</button>
```

One way you can clarify the above code is by utilizing `getRemainingChars()`. If there are 280 characters remaining, that means that the `textarea` is empty and the “Add Photo” button is OFF so the “Tweet” button should be disabled.

```html
<button ... disabled={this.getRemainingChars() === 280}>...</button>
```

This works but could break if, for example, you later refactor `getRemainingChars` so that it returns a string instead of a number. Instead, we can keep the previous logic and just move it to the top of the `render()`:

```js
render() {
    const isTweetButtonDisabled = this.state.text.length === 0 && !this.state.photoAdded;
  
    return (
      ...
        <button className="..." disabled={isTweetButtonDisabled}>Tweet</button>
      ...
    );
  }
```

That’s it! Try toggling the “Add Photo” button and check that the “Tweet Button” is enabled/disabled correctly.

#### We’re Done!

Here’s the resulting Pen:

%[https://codepen.io/julienben/pen/roZXvE] 

### Step 13: Reflection on the React Code — Why So Simple? (5 minutes)

The changes to accommodate the “Add Photo” button were minimal when using React. No refactor needed. Why is this the case?

Again, it has to do with React’s style of writing UI code. In React, event handlers modify the `state`, and whenever the state is modified, **React automatically calls** `render()` again to update the UI.

In this particular example, the diagram now looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*DN_-X4stP1U7E6-h align="left")

The `state` becomes an intermediary thing which sits in between the event handlers and `render()`:

* Event handlers don’t need to worry about which part of the DOM changes. They just need to set the `state`.
    
* Similarly, when you write `render()`, all you need to worry about is what the current `state` is.
    

### Compare with jQuery

You can imagine what would happen as the UI gets more features. Without the intermediary state, we’d have a tough time managing complexity. This is why you’d want to use React over jQuery for complex UIs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*N2IvA6TZIvC-T155 align="left")

Again, **it’s possible** to write clean jQuery code that doesn’t look like spaghetti code. **But you have to come up with the code structure yourself** and think about how to refactor every time you add a new feature. React provides you this structure and reduces your cognitive load.

> Note that the idea of separating the state from the rendering wasn’t invented with React. We’re just looking at it from the perspective of React.

### Step 14: The Final Feature — Highlighting Overflown Characters (5 minutes)

The last feature we’re going to implement is **highlighting characters that are over the limit**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C1OJuGMg8agMuugu align="left")

Unfortunately, **we’re not going to highlight the actual text inside the Tweet box** because that would require us to change `<textar`ea&`gt; to<div contenteditabl`e="tr`ue"> and con`tenteditable is a bit too complicated for illustrative purposes.

Instead, **we’ll be displaying a Bootstrap alert box** on top and indicate which characters need to be deleted, like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*3Lnj6RRDfqMk1c8l align="left")

**To try it out, copy the following quote from the official React documentation:**

> React embraces the fact that rendering logic is inherently coupled with other UI logic: how events are handled, how the state changes over time, and how the data is prepared for display.

> Instead of artificially separating technologies by putting markup and logic in separate files, React separates concerns with loosely coupled units called “components” that contain both.

%[https://codepen.io/julienben/pen/bOmdWZ] 

* It should show an alert box with the overflow characters highlighted in red.
    
* It should also show 10 characters before the cutoff point, without any highlighting.
    

If we were to implement this in jQuery, our code would become a lot messier. Notice in the diagram that we’ll be adding two more arrows for one new feature.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5IJpVy_aq3SfO9Lq align="left")

**So we’re not going to implement this in jQuery**. We’ll just do it with React and call it a day. It’ll be pretty simple to do with React — just one extra arrow in the diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/0*2lMKrwLX5WA-oUpb align="left")

### Step 15: Highlighting Overflow Characters with React (10–15 minutes)

Let’s start with our previous React implementation.

**✔ Fork the Pen below** to get started.

%[https://codepen.io/julienben/pen/roZXvE] 

We’ll do this step by step. First, **we’ll display a simple alert with static text when you write past the limit.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*ap1sBT75lN-f5hVD align="left")

Since this will require a conditional, let’s write it in a separate method. **Add** `{this.renderOverflowAlert()}` above the `textarea`:

```js
{this.renderOverflowAlert()}
<textarea ...></textarea>
```

Now, this method should return:

* **A div tag** for the alert box if there are no more characters left.
    
* **Nothing** (i.e. empty string or NULL) otherwise.
    

It turns out that in React, **you can return JSX markup from a method and use this in any other method**, everything will just work. In other words, you can do something like:

```js
someMethod = () => {
  return (
    <a href="#">Hello World</a>
  );
}
anotherMethod = () => {
  return (
    <h1>
      {this.someMethod()}
    </h1>
  );
}
```

In `renderOverflowAlert`, we can return `( <div> ... </div> )` in one case and nothing in **the other. So our** `renderOverflowAlert` method will look like this:

```js
renderOverflowAlert = () => {
  if (this.getRemainingChars() < 0) {
    return (
      <div className="alert alert-warning text-left">
        <strong>Oops! Too Long:</strong>
      </div>
    );
  }
  return '';
};
```

Notice that we’re checking `this.getRemainingChars()` to see if we need to show the alert or not.

**Try this out by typing 280+ characters (or 257+ characters with the “Add Photo” button ON).** The alert should appear just as the character limit reaches -1.

#### Displaying Overflown Characters

![Image](https://cdn-media-1.freecodecamp.org/images/0*9IQGNgFJtO4Stlpk align="left")

*(This should say 280 instead of 140 characters.)*

Here’s a breakdown of the logic we want for the alert message:

* Between “Oops! Too Long:” and the actual text, there’s an empty single space followed by three dots. I used here because when writing markup in JSX, white spaces between tags get removed. (You can add them manually using `{' '}`.)
    
* Then there are the 271st~280th (total of 10) characters of `this.state.text`.
    
* Then there are the remaining characters highlighted in red.
    

**Let’s write this in JSX. Inside the** `if` clause of `overflowAlert`, we’ll create two variables: `beforeOverflowText` and `overflowText`. We’ll use [the substring method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring) on `this.state.text`.

```js
renderOverflowAlert = () => {
  if (this.getRemainingChars() < 0) {
    const beforeOverflowText = this.state.text.substring(280 - 10, 280);
    const overflowText = this.state.text.substring(280);
    return (
      <div className="alert alert-warning text-left">
        <strong>Oops! Too Long:</strong>
        &nbsp; &#8230;
        {beforeOverflowText}
        <strong className="bg-danger text-light">{overflowText}</strong>
      </div>
    );
  }
  return '';
};
```

* If you do `.substring(a, b)`, it will return the `(a + 1)-nth` until the `b-th` characters from the string.
    
* If you do `.substring(a)`, it will return the `(a + 1)-nth` until the last characters from the string.
    
* We use Bootstrap’s `bg-danger` class to highlight the text in red and `text-light` to make the text readable against the now-dark background.
    

Copy paste the following text again and check that the part of the text after the first 280 characters is highlighted. We’re almost done!

> React embraces the fact that rendering logic is inherently coupled with other UI logic: how events are handled, how the state changes over time, and how the data is prepared for display.

> Instead of artificially separating technologies by putting markup and logic in separate files, React separates concerns with loosely coupled units called “components” that contain both.

#### What if the “Add Photo” button is ON?

If the “Add Photo” button is ON then the character limit decreases by 23. **So our** `beforeOverflowText` and `overflowText` need to take that into account:

```js
renderOverflowAlert = () => {
    if (this.getRemainingChars() < 0) {
      const imageLength = this.state.photoAdded ? 23 : 0;
      const beforeOverflowText = this.state.text.substring(
        280 - imageLength - 10,
        280 - imageLength,
      );
      const overflowText = this.state.text.substring(280 - imageLength);
      return (
        <div className="alert alert-warning text-left">
          <strong>Oops! Too Long:</strong>
          &nbsp; &#8230;
          {beforeOverflowText}
          <strong className="bg-danger text-light">{overflowText}</strong>
        </div>
      );
    }
    return '';
  };
```

Now, try toggling the “Add Photo” button while entering any text that’s longer than the limit. It should work as expected. Here’s the Pen:

%[https://codepen.io/julienben/pen/bOmdWZ] 

That’s it! Again, you can see that the code changes were simple:

![Image](https://cdn-media-1.freecodecamp.org/images/0*RJ-PiBFsvcPqqQCc align="left")

### Step 16: What’s Next? (5 minutes)

This concludes the tutorial. Hopefully you:

* understood the advantages of React’s component structure vs manually modifying the DOM with jQuery, and
    
* learned how to write simple React components using JavaScript and JSX.
    

#### **What’s next?**

There are many ways to go from here.

One possibility would be to take a look at this short article called [How to Learn React — A roadmap from beginner to advanced](https://medium.freecodecamp.org/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6). It can help you decide how to best continue learning React.

I also highly recommend reading the following portions the official React documentation:

* [Getting started](https://reactjs.org/docs/getting-started.html) which includes the React team’s recommended learning resources, and
    
* [Thinking in React](https://reactjs.org/docs/thinking-in-react.html) which will help you understand how to think about building components and applications with React.
    

Before you leave though, I have an **optional challenge** for you!

If you feel comfortable enough with React already and want to write your own code, **try to move** `remainingChars` to the component’s `state`. Make sure it gets updated where necessary and use it in all the relevant places.

**Feel free to post the result as a Pen in the comments and I’ll be very happy to check it out!**

#### Thanks

Thanks a lot for reading this far! And above all thanks to [@chibicode](https://twitter.com/chibicode) for the huge amount of work he put into the first version of this tutorial! I hope this updated version does it justice.

I’m Julien. I work as a frontend engineer at [Healthy.io](https://healthy.io) and I help maintain [react-boilerplate](https://github.com/react-boilerplate/react-boilerplate) on GitHub. If you catch a mistake, want any clarifications or think I skipped something important, please let me know and I’ll make sure to fix it.
