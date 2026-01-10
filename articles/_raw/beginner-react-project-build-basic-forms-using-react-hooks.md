---
title: Beginner React Project - How to Build Basic Forms Using React Hooks
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-08-17T16:39:03.000Z'
originalURL: https://freecodecamp.org/news/beginner-react-project-build-basic-forms-using-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Basic-Forms-App.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "What we're building\nIn this beginner React Project, we're going to learn\
  \ how to build basic forms using React hooks. We'll learn how to manage form state,\
  \ handle validation, and work with submit handlers. \nCheck it out:\n\nTry it yourself\n\
  If you want t..."
---

## What we're building

In this beginner React Project, we're going to learn how to build basic forms using React hooks. We'll learn how to manage form state, handle validation, and work with submit handlers. 

Check it out:

![](https://jschris.com/0988e0e5975472dc7fe616d48f906494/project.gif)

## Try it yourself

If you want to have a go yourself first, here are the scenarios (you can also grab the CSS/starter code below):

- The user should be able to enter values into the form
- When the user clicks submit, if any fields are empty, then an error message should appear in red
- If the form is submitted and is valid, a success message should appear

## Video Walkthrough

[Check out the video walkthrough on YouTube here.](https://youtu.be/8hU0I8rY4u4)

## Starter Code

[Grab it over at GitHub here.](https://github.com/chrisblakely01/basic-react-forms)

## Let's go! Adding state

We're going to start by adding a state object to hold our form. We will take a new line at the top of our `App function` in **App.js** and add the following:

```jsx
const [values, setValues] = useState({
	firstName: '',
	lastName: '',
	email: '',
});
```

We have three fields on the form that we need to know the state for.

Now, the initial state is going to be an object. And this object is going to have three values, one for each of these fields. So we'll call them something similar to what they're called in the form.

The `firstName` is going to be set to blank initially, same with `lastName` and same with `email`. 

And now, you'll notice an error that says "useState is not defined", so you need to import it from React here. Do this at the top of the file as part of the imports:

```
import React, { useState } from "react";
```

Okay, so now it's telling us that these variables aren't used yet. This is fine because we haven't applied these values to the form. But all we've done so far is we've created a state object, and this state object pulls `firstName`, `lastName` and `email`. 

Now that we have some values in state, it make sense to apply them to our input fields. Add a `value` property to each of your input fields like so:

```jsx

<input
    id="first-name"
    class="form-field"
    type="text"
    placeholder="First Name"
    name="firstName"
    value={values.firstName}
/>

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Last Name"
    name="lastName"
    value={values.lastName}
/>

<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
/>

```

All we've done here is say, "Okay, for this input, the value is going to be whatever value is in state." Let's save this and see what is going on in our forms, to make sure things are still working.

And they're not. Oh, no!

If you select an input and start vigorously typing on the keyboard, nothing appears on the screen. What's going on here?

## Updating input states

Well, we've said that the value of this input is going to be whatever it is in state. 

For example, `firstName` is currently set to blank because that's what we set it to, but we haven't told the input, "Okay. Any time I type or the input changes, I want you to go and update the state with the new values."

Whenever we do things like this, it effectively gives control to React. So we have to tell React to also update the values. 

This means we have to update the state values anytime we type into these fields. 

Okay. The simplest way to do this is to create a **handler** for each of these input fields, which updates the state any time an on change event occurs. 

Go ahead and add the following just below the state objects:

```jsx
const handleFirstNameInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		firstName: event.target.value,
	}));
};
```

This takes the event which we get from the `onChange`. We are basically updating this object and then saving it back to state.

We will copy the old values by doing the three dots, which is also known as a spread operator. And then, we'll just type values and add a comma. 

Next, we'll say **firstName is going to be equal to event.target.value**. We want to add this to our input. So in our JSX in the **input for first name**, we'll take a new line somewhere (anywhere, it doesn't really matter), and add the `onChange` property like so:

```jsx
<input 
    id='first-name' 
    class='form-field' 
    type='text' 
    placeholder='First Name' 
    name='firstName' 
    value={values.firstName} 
    onChange={handleFirstNameInputChange} />
```

Now, if we go into our browser and start typing, you can see that things work. There rest of them aren't working because we haven't added handlers for these yet. We'll have a look at that in a minute.

Just to recap what's happening: anytime we type into this box, the **onChange event** happens for every keystroke. This gets called every time. 

The event gets passed in by React, and we want to update our state object. So to do that, we call the `setValues` function and pass in a new object with the updated values.

Now, we just want to do the same for `lastName` and `email`. Add another handler for each:

```jsx
const handleLastNameInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		lastName: event.target.value,
	}));
};

const handleEmailInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		email: event.target.value,
	}));
};
```

And don't forget to add the `onChange` properties to the input fields for each:

```jsx

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Last Name"
    name="lastName"
    value={values.lastName}
    onChange={handleLastNameInputChange}
/>
<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
    onChange={handleEmailInputChange}
/>

```

Okay. Now is the moment of truth. Is everything working or have we broken something along the way? Let's try it and see. Fill in some data and the input fields should be working now. Hurray!

Even though our input fields are working, we still have a funny issue where if we type stuff in the form and try to submit, it's not going to do anything. It will just refresh the page and all our form data is lost. 

Let's do something about that.

## Showing a success message

After clicking register, it should show a success message if the form is valid. What we want to do is go to our JSX, and just beneath the form add a new div. Again, I've added the classes for you for a success message:

```jsx
<div class='success-message'>Success! Thank you for registering</div>
```

Now, of course, this isn't going to go anywhere. It's just going to pretend that we've called a server or an end point somewhere. And it's come back with a success message, so we're just going to display this to a user. 

But currently it's appearing all the time. What we wanted is only to show this if the user has successfully submitted the form. 

So we'll add another state object like so:

```jsx
const [submitted, setSubmitted] = useState(false);
```

We'll keep this separate from the values as it's a different part of the form. We don't want to mix everything up in here and cause an entire re-render. This is going to tell us whether the form has been submitted or not.

It's going to be set to `false` initially because the first time a user lands on the page, it's not going to be submitted. 

And now, we just want to do some clever stuff down in the JSX to say, "If submitted is true, then we want to show the success message." 

Update the line we just added with the following:

```jsx
{showSuccess && <div class='success-message'>Success! Thank you for registering</div>}
```

We'll wrap our **success message** in a ternary operator. That is basically a shorthand if statement that lets us render things dynamically on the page.

The success message will now only appear if `showSuccess` is true. As you can see now in the browser, this has disappeared. 

If we jump back up to our state object for `submitted` and change this to `true`, it should appear again. And it does.

We'll change this back to false. And then we'll refresh our Chrome and just see what happens now. 

We haven't told the register button or the form what happens on summit, so it's still going to refresh the page. Now, we just need a new handler to handle the register button click. 

If we jump into our event handlers and add the following:

```jsx
const handleSubmit = (e) => {
	e.preventDefault();
	setSubmitted(true);
};
```

`event.preventDefault` will stop the refresh from happening that we've been seeing. 

We'll add some more logic in here in a minute around validation and stuff. But for now, we're just going to say "setSubmitted" to be a true. 

Next we need to tell the form to call this function when it gets submitted. Update the JSX to include an `onSubmit` property in the form tag like so:

```jsx
<form class='register-form' onSubmit={handleSubmit}>
	//... other code
</form>
```

Now if we run the code in the browser, click the register button, the message appears. Hurray!

## Adding Validation and showing error messages

Our form is looking good so far, but we're missing one key component of any form, and that is the validation. If we look at our working example, if I submit this with any empty fields, an error appears which says, "Please enter your details."

Below each input, we'll add a `<span>` which will hold the error message. Your JSX should look similar to this:

```jsx

<input
    id="first-name"
    class="form-field"
    type="text"
    disabled={showSuccess}
    placeholder="First Name"
    name="firstName"
    value={values.firstName}
    onChange={handleInputChange}
/>
<span id="first-name-error">Please enter a first name</span>

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Last Name"
    name="lastName"
    value={values.lastName}
    onChange={handleInputChange}
/>
<span id="last-name-error">Please enter a last name</span>

<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
    onChange={handleInputChange}
/>
<span id="email-error">Please enter an email address</span>

```

You can see these errors always appear, because we haven't got any conditional logic that says "don't appear."

Now, we only want these error messages to show if the register button has been clicked. 

We'll jump back into the code. We want to add some conditional logic in and around the error messages, so that they only appear if the button has been clicked and the field is empty:

```jsx
{submitted && !values.firstName && <span id='first-name-error'>Please enter a first name</span>}
```

What we're doing here is checking if the form is submitted, and if the `firstName` state object is empty. If so, we want to display the error message. Again, we're just using a ternary operator, nothing fancy!

Do the same for the other errors:

```jsx
{submitted && !values.lastName && <span id='last-name-error'>Please enter a last name</span>}

//...other code

{submitted && !values.email && <span id='email-error'>Please enter an email address</span>}
```

If we leave the form blank and click register, errors appear. If we start typing things, we can see that the error disappears. And if we remove what we typed, the error comes back again.

Let's try and submit some stuff. Okay, so this seems to be working. 

The last thing we want to do is just make sure that this success message only appears if the form is valid. Go ahead and add a new state value:

```jsx
const [valid, setValid] = useState(false);
```

This is used to tell us if our form is valid - remember, using state objects is a good way to hold the "state" of the different parts of your app (who would have guessed?). 

The success messages should only appear if submitted is true and followed is also true. Since we've set valid as false initially, it won't show up.

In our `handleSubmit` function, we want to say value is true if a form is valid. We can do this by checking each of our state values for the form fields, making sure that they are a truthy value. 

Add the following:

```jsx

const handleSubmit = (event) => {
event.preventDefault();
if(values.firstName && values.lastName && values.email) {
    setValid(true);
}
setSubmitted(true);
}

```

If any of these fields are false, then `valid` will stay as false. This means the success message div will not get shown. Let's see it working.  If we click register without the fields, our error messages show up. Let's type some valid stuff, hit register, and the message appears! 

## Want more project ideas?

Why not try building some React projects to boost your learning even further? I send out emails every few weeks(ish) with project ideas, starter code, and tips. [Subscribe to get this straight to your inbox!](https://subscribe.jschris.com)




