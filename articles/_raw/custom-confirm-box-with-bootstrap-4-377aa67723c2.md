---
title: How to create a custom confirm box with Bootstrap4 and ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-23T15:55:43.000Z'
originalURL: https://freecodecamp.org/news/custom-confirm-box-with-bootstrap-4-377aa67723c2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8tI8tEqNrAaaNkDAbXEQsw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Prashant Yadav

  We put lots of sweat into achieving a good design, but imagine a scenario where
  we have to use something which is styled default to browsers. It ruins our hard
  work as it changes browser to browser.

  Same happened with me: I had put ...'
---

By Prashant Yadav

We put lots of sweat into achieving a good design, but imagine a scenario where we have to use something which is styled default to browsers. It ruins our hard work as it changes browser to browser.

Same happened with me: I had put lots of effort into creating a SPA but the client wanted a confirm box with business logic. Unfortunately, using the inbuilt confirm box was the only odd factor in the design. So I created a custom confirm box.

Let us see how you can create your own custom confirm box with Bootstrap4 and [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/).

A **modal** is a popup dialog that is available with Bootstrap. We can use its functionality to handle the popup and design it according to our needs. It has different methods which we can use to achieve our goal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jrEUFkPpPS4MUkcTpS9Chw.png)
_Custom Confirm Box_

Check out the live demo [here](https://learnersbucket.com/examples/bootstrap4/custom-confirm-box-with-bootstrap/).

* We are going to use Bootstrap4 modal for creating the popup dialog.
* We will use the Javascript _callback_ function to handle the response.
* As Bootstrap has a JQuery dependency, we will use it for events.

### #Bootstrap Modal Methods

.modal(options): Activates the content as a modal with the below options.

.modal(“toggle”): Shows or Hides the modal based on its current state.

.modal(“show”): Opens the modal.

.modal(“hide”): Hides the modal.

### #Bootstrap Modal Options

{backdrop: true or false, default: true}: Should modal hide when clicked outside the modal.

{ keyboard: true or false, default: true}: Should modal hide when a keyboard button is pressed.

{ show: true or false, default: true}: To show the modal when initialized.

### #Bootstrap Modal Events

.on(‘show.bs.modal’): When modal is about to be shown but it is not yet shown.

.on(‘ shown.bs.modal’): When modal is shown.

.on(‘ hide.bs.modal’): When modal is about to be hidden but it is not yet hidden.

.on(‘ hidden.bs.modal’): When modal is hidden.

#### Dependencies

Import all the dependencies using CDN.

We will now create a function that will generate our confirm box with our custom message and return the output selected by the user.

We don’t need the header and footer of the modal. We will just use the modal body and display our message in an <h4> tag. Then we will create two buttons below it with different cl`asses b`tn-ye`s and` btn-no which will be used to handle the response.

#### Explanation

* We have created a `function` which accepts a `message` and a callback `handler`.
* In this, we are appending the modal at the end of the `body` tag with JQuery’s `appendto` method.
* After appending the modal, we are triggering or showing the modal with Bootstrap’s `modal` method. We are also passing two parameters `{backdrop: 'static', keyboard:false}` which prevent the modal from hiding with keyboard events, like pressing the **ESC** button or clicking in the backdrop area.
* We are checking if the modal is hidden with bootstrap’s `hidden.bs.modal` and then we are removing the modal with JQuery’s `remove` method. This will prevent it from adding a modal every time.

We have created a function that will render and open our custom confirm box, so now we have to handle the response provided by the user.

We will use a callback function to handle the response. In JavaScript, we can pass the function as an argument to another function and call it. The functions passed as arguments are called the callback functions.

### Handling the response

#### Explanation

If **yes** or **no** button is pressed then we pass `true` or `false` to the callback function and call it. After that, we hide the modal.

We can call our confirm box like this wherever we want.

Check out the live demo [here](https://learnersbucket.com/examples/bootstrap4/custom-confirm-box-with-bootstrap/).

With a custom confirm box, we have complete control over the design and some control over the functionality.

If you liked this article, please give it some ?and share it! If you have any questions related to this feel free to ask me.

_For more like this and algorithmic solutions in Javascript, follow me on_ [**Twitter**](https://twitter.com/LearnersBucket)_._ I write about [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/), and [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) on [_learnersbucket.com_](https://learnersbucket.com/)_._

