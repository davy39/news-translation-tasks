---
title: How to Build React Forms the Easy Way with react-hook-form
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-12T16:39:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-forms
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/how-to-build-react-forms.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'Nobody enjoys creating and re-creating complex forms with validation, React
  developers included.

  When it comes to building forms in React, it''s essential to use a form library
  that provides a lot of convenient tools and doesn’t require much code.

  Bas...'
---

Nobody enjoys creating and re-creating complex forms with validation, React developers included.

When it comes to building forms in React, it's essential to use a form library that provides a lot of convenient tools and doesn’t require much code.

Based off of these two criteria, utility and simplicity, the ideal React form library to use for your applications is `react-hook-form`.

Let's see how to use react-hook-form in your own projects to build rich, featureful forms for your React apps.

## How to Install react-hook-form

Let’s cover a typical use case: a user signing up to our application. 

For our signup form, we will have three inputs for any new user's username, password, and email:

```jsx
import React from "react";

const styles = {
  container: {
    width: "80%",
    margin: "0 auto",
  },
  input: {
    width: "100%",
  },
};

export default function Signup() {
  return (
    <div style={styles.container}>
      <h4>Sign up</h4>
      <form>
        <input placeholder="Username" style={styles.input} />
        <input placeholder="Email" style={styles.input} />
        <input placeholder="Password" style={styles.input} />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

```

Once we have a React project up and running, we’ll start by installing the `react-hook-form` library.

```bash
npm i react-hook-form

```

## How to use the useForm hook

To start using `react-hook-form` we just need to call the `useForm` hook. 

When we do, we’ll get back an object from which we will destructure the `register` property.

`register` is a function, which we need to connect to each one of the inputs as a ref. 

```jsx
function App() {
  const { register } = useForm();

  return (
    <div style={styles.container}>
      <h4>Signup</h4>
      <form>
        <input ref={register} placeholder="Username" style={styles.input} />
        <input ref={register} placeholder="Email" style={styles.input} />
        <input ref={register} placeholder="Password" style={styles.input} />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

```

The register function will take the value our user has typed into each input to validate it. Register will also pass each value to a function which will be called when our form is submitted, which we'll cover next.

For register to work properly, for each input we need to provide an appropriate name attribute. For example, for the username input, it will have a name of "username".

The reason for this is that when our form is submitted, we will get all of the inputs' values on a single object. Each of the object's properties will be named according to the inputs' name attributes that we have specified.

```jsx
function App() {
  const { register } = useForm();

  return (
    <div style={styles.container}>
      <h4>My Form</h4>
      <form>
        <input
          name="username"
          ref={register}
          placeholder="Username"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Password"
          style={styles.input}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

```

## How to submit our form with handleSubmit

To handle submitting our form and receiving the input data, we’ll add an `onSubmit` to our form element and connect it to a local function with the same name:

```jsx
function App() {
  const { register } = useForm();

  function onSubmit() {}

  return (
    <div style={styles.container}>
      <h4>My Form</h4>
      <form onSubmit={onSubmit}>
        <input
          name="username"
          ref={register}
          placeholder="Username"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Password"
          style={styles.input}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

```

From `useForm`, we’ll grab a function called `handleSubmit` and wrap it around onSubmit as a higher-order function. 

The `handleSubmit` function will take care of collecting all of our data typed into each input which we’ll receive within `onSubmit` as an object called `data`.

Now if we `console.log(data)` we can see what we typed into each of our inputs on a property with the same name:

```jsx
function App() {
  const { register, handleSubmit } = useForm();

  function onSubmit(data) {
    console.log(data); 
    // { username: 'test', email: 'test', password: 'test' }
  }

  return (
    <div style={styles.container}>
      <h4>Signup</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          name="username"
          ref={register}
          placeholder="Username"
          style={styles.input}
        />
        <input
          name="email"
          ref={register}
          placeholder="Email"
          style={styles.input}
        />
        <input
          name="password"
          ref={register}
          placeholder="Password"
          style={styles.input}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

```

## Validation options with the register function

To validate our form and add constraints for each input’s value is very simple—we just need to pass information to the `register` function.

`register` accepts an object, which includes a number of properties that will tell register how to validate a given input. 

The first property is `required`. By default, it is set to false but we can set that to true to make sure the form isn’t submitted if it’s not filled out.

We want the username value to be required and we want our users’ usernames to be more than six characters but less than 24.

To apply this validation, we can set the constraint of `minLength` to six, but the `maxLength` should be 20:

```jsx
<input
  name="username"
  ref={register({
    required: true,
    minLength: 6,
    maxLength: 20,
  })}
  style={styles.input}
  placeholder="Username"
/>

```

If we were using numbers for this input (say if this input was for the person’s age), we would use the properties `min` and `max` instead of `minLength` and `maxLength`.

Next, we can supply a regex pattern if we like. 

If we want a username to only contain uppercase and lowercase characters, we can use the following regex which allows for custom validation:

```jsx
<input
  name="username"
  ref={register({
    required: true,
    minLength: 6,
    maxLength: 20,
    pattern: /^[A-Za-z]+$/i,
  })}
  style={styles.input}
  placeholder="Username"
/>

```

And finally, there is `validate`, a custom function that gives us access to the value typed into the input. `validate` allows us to provide our own logic to determine whether it is valid or not (by returning the boolean true or false).

For the email here, we also want it to be required and for it to be a valid email. To check this, we can pass the input to a function from the library `validator` called `isEmail`.

If the input is an email, it returns true. Otherwise, false:

```jsx
<input
  name="email"
  ref={register({
    required: true,
    validate: (input) => isEmail(input), // returns true if valid
  })}
  style={styles.input}
  placeholder="Email"
/>

```

For password’s `register` function, we’ll set required to true, `minlength` to six, and we won’t set a `maxLength`:

```jsx
<input
  name="password"
  ref={register({
    required: true,
    minLength: 6
  })}
  style={styles.input}
  placeholder="Password"
/>
```

## How to display errors

Right now, if an input within our form isn’t valid, we don't tell our user that anything is wrong. We need to give them feedback to fix the values they have supplied.

When one of the inputs is invalid, the form data is merely not submitted (`onSubmit` isn’t called). Additionally, the first input with an error is automatically focused, which doesn’t provide our user any detailed feedback about what’s happening.

Instead of just not submitting the form, we can grab an `errors` object from useForm.

And just like the data function we get in `onSubmit`, `errors` contains properties corresponding to each of the inputs' names if it has an error.

For our example, we can add a conditional to each of the inputs and say if there is an error, we’ll set the `borderColor` to red.

```jsx
function App() {
  const { register, handleSubmit, errors } = useForm();

  function onSubmit(data) {
    console.log(data);
  }

  return (
    <div style={styles.container}>
      <h4>My Form</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          name="username"
          ref={register({
            required: true,
            minLength: 6,
            maxLength: 20,
            pattern: /^[A-Za-z]+$/i,
          })}
          style={{ ...styles.input, borderColor: errors.username && "red" }}
          placeholder="Username"
        />
        <input
          name="email"
          ref={register({
            required: true,
            validate: (input) => isEmail(input),
          })}
          style={{ ...styles.input, borderColor: errors.email && "red" }}
          placeholder="Email"
        />
        <input
          name="password"
          ref={register({
            required: true,
            minLength: 6,
          })}
          style={{ ...styles.input, borderColor: errors.password && "red" }}
          placeholder="Password"
        />
        <button type="submit" disabled={formState.isSubmitting}>
          Submit
        </button>
      </form>
    </div>
  );
}

```

## Validation mode

You’ll notice, by default, that the errors object is updated only when we submit the form. The default validation is only performed upon submitting the form.

We can change this by passing the `useForm` an object, where we can set the mode to when we want validation to be performed: `onBlur`, `onChange`, or `onSubmit`. 

`onBlur` is going to make validation run whenever the user ‘blurs’ or clicks away from the input. `onChange` is whenever a user types in the input, and `onSubmit` is whenever the form submitted.

For our form, let's select `onBlur`.

```jsx
const { register, handleSubmit, errors } = useForm({
  mode: "onBlur",
});

```

Note that there are other helpers to both set and clear the errors manually (`setError` and `clearError`). These would be used if, for example, you had certain cases where you want it to create a different error or clear an error yourself within `onSubmit`.

## How to disable our form with formState

The last value which we can get the `useForm` hook is `formState`.

It gives us important information such as when certain inputs have been touched, as well as when the form has been submitted.

So if you want to disable your form’s button to make sure the form isn’t submitted more times than it needs to, we could set disabled to `formState.isSubmitting`.

Whenever we’re submitting our form, it’s going to be disabled until it’s done with validation and running our onSubmit function.

## Conclusion

I hope that this article showed you how to more easily create functional forms within your React apps.

It's worth nothing that there are a ton more features that come with `react-hook-form` that I didn’t cover here.  The [documentation](https://react-hook-form.com) should cover any use case you can think of.

If you are interested in seeing the final version of our code, click on the CodeSandbox link [right here](https://codesandbox.io/s/crazy-leavitt-nf74y).

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

