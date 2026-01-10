---
title: How I built an async form validation library in ~100 lines of code with React
  Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T17:40:04.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-async-form-validation-library-in-100-lines-of-code-with-react-hooks-81dbff6c4a04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EGRMyNT8x7gb0LdLmj4xMQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Austin Malerba

  Form validation can be a tricky thing. There are a surprising number of edge cases
  as you get into the guts of a form implementation. Thankfully, there are many form
  validation libraries out there which provide the necessary flags a...'
---

By Austin Malerba

Form validation can be a tricky thing. There are a surprising number of edge cases as you get into the guts of a form implementation. Thankfully, there are many form validation libraries out there which provide the necessary flags and handlers to implement a robust form, but I challenged myself to build one in under 100 lines of code using the [React Hooks API](https://reactjs.org/docs/hooks-reference.html) (currently in alpha). As React Hooks are still an experimental proposal, this is a proof of concept for the application of React Hooks to implement form validation.

Also, fair warning, the _library_ I build is 100 lines of code, but this tutorial has ~200 lines of code because I need to show how the library is used.

Many form tutorials I’ve seen fail to address three big topics: **async validation**, field validations that should be triggered when **other** **fields change**, and optimization of **validation frequency**. I am bothered by tutorials that focus on a single use case and hold all other variables constant because that’s not how the real world works, so I will try to hit a variety of use cases.

Let’s aim to satisfy the following:

* Synchronously validate a field and any dependent fields when the field value changes
* Asynchronously validate a field and any dependent fields when the field value changes
* Synchronously validate all fields before submitting
* Asynchronously validate all fields before submitting
* Attempt async submission and if the form fails to submit, display errors from the response
* Expose validation methods to the developer so the developer can validate onBlur or at other times that make sense
* Allow multiple validations per field
* Disable submission if the form has errors
* Do not show a field’s errors until it has been changed or until a form submission has been attempted

We will hit these use cases by implementing an account registration form with a username, password, and password confirmation. Below I’ve outlined the kind of interface we’re looking for, we will build a library to satisfy this contract.

This is a relatively simple API, but should give us a lot of flexibility. You might have noticed that this interface includes two similarly named functions, validation and validate. We will define a validation as a function that takes in form data and a field name and returns an error message if an issue is found, otherwise it will return a falsey value. On the other hand, a validate function will run all validation functions for a field and will update the field’s error list.

First things first, we need a skeleton to handle value changes and form submission. Our first iteration will not include any validation, it will merely handle form state.

There’s nothing too crazy happening in this code. The only state we track is the field values. We have each field register itself with the form at the end of its initialization. Our onChange handlers are simple. The most intimidating function in here is getFormData, but even this is pretty trivial behind the unsightly reduce syntax. getFormData iterates over the form fields and gives us a plain object representation of the form values. The last thing I feel I should explain is that we need to call preventDefault on submit to prevent the page from reloading.

This is good and dandy, but let’s add support for validations now. We won’t yet specify which fields should be validated when a field value changes. Instead, we’ll validate all fields whenever a value changes and whenever the form is submitted.

The above code is an improvement and, at first glance, it seems like it could work well, but it’s actually quite [sloppy to the end user](https://codesandbox.io/s/wy074qmk98?module=%2Fsrc%2FformHooks.js). It’s missing a lot of necessary flags that help prevent errors from showing at inappropriate times. It immediately validates fields before the user has had a chance to modify them and displays corresponding errors.

At the very least we need a pristine flag to tell the UI not to show errors if the user hasn’t changed a field. But let’s go further. In addition to a pristine flag, we will want a few more flags.

We will want a flag to indicated that the user has attempted to submit the form and we will want flags to indicate when the form is submitting and when each field is validating asynchronously. You may also be wondering why we invoke validateFields inside useEffect as opposed to inside of the onChange handler. We need useEffect because setValue happens asynchronously and neither returns a promise nor offers a callback. Therefore, the only way we can be sure setValue has completed, is by listening to a value change via useEffect.

Let’s implement the flags I mentioned to help clean up the UI and to handle some edge cases.

Our final iteration adds a lot. It adds four flags: pristine, validating, submitted, and submitting. It also adds the fieldsToValidateOnChange parameter, which is passed to validateFields to indicate which fields should be validated when a field value changes. We use these flags in the UI to control when spinners and errors are displayed as well as to disable the submit button.

One peculiar thing you may have noticed is the validateCounter. We need to track how many times the validate function has been called because by the time our validate function has reached completion, it’s possible that validate will have been called again. If this is the case, we need to ignore the results of this invocation and only use the results of the most recent invocation to update the error state for a field.

When all is said and done, here is the functional result.

React Hooks provide a neat solution to form validation. This is my first experimentation with the proposed API and I have found it powerful, but a little awkward. The interface is peculiar, with a bit too much magic for my liking. However, once I accepted its blemishes, it proved quite capable.

I did feel it was lacking a few features, namely a callback mechanism to indicate when a useState setter has finished updating the state and also a way to inspect prop deltas in the useEffect hook.

#### After Note

I have intentionally left out some argument validation and error handling in order to keep this tutorial brief and simple to follow. Take, for example, the way I do not check whether the form passed into a field is indeed a form. It would be a lot nicer to check this explicitly and to throw a verbose error. However, as I have written it, the code would bomb out with something like

```
Cannot read property ‘addField’ of undefined
```

This code needs proper argument validation and error handling before it could ever be published as an npm library. That said, I have implemented a [more robust version](https://codesandbox.io/s/1417995kx4) that includes argument validation via [superstruct](https://github.com/ianstormtaylor/superstruct) if you would care to check it out.

