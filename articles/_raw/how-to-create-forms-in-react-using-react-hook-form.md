---
title: How to Create Forms in React using react-hook-form
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2022-10-27T19:47:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Creating forms in React is a complex task. It involves handling all the
  input states and their changes and validating that input when the form gets submitted.

  For simple forms, things are generally manageable. But as your form gets more complex
  and y...'
---

Creating forms in React is a complex task. It involves handling all the input states and their changes and validating that input when the form gets submitted.

For simple forms, things are generally manageable. But as your form gets more complex and you need to add various validations, it becomes a complicated task.

So instead of manually writing all of the code and handling complex forms with validation logic, we can use the most popular React library for this, [react-hook-form](https://react-hook-form.com/).

It's the most popular React library for creating forms compared to [formik](https://formik.org/), [react final form](https://final-form.org/react/), and others, and I use it for all my client projects.

In this article, we will explore how to use the [react-hook-form](https://react-hook-form.com/) library in detail.

So let's get started.

## Why the react-hook-form Library is the Most Popular Form Library in React

Following are some of the reasons why `react-hook-form` is a popular choice for creating React forms.

* The number of re-renders in the application is smaller compared to the alternatives because it uses refs instead of state.
* The amount of code you have to write is less as compared to `formik`, `react-final-form` and other alternatives.
* `react-hook-form` integrates well with the `yup` library for schema validation so you can combine your own validation schemas.
* Mounting time is shorter compared to other alternatives.

Check out the [react-hook-form](https://react-hook-form.com/) website for more detailed comparison.

## How to Create a Form Without Using a Library

Before creating a form using the `react-hook-form` library, let's create a simple form without using any library.

Take a look at the below code:

```js
import React, { useState } from "react";
import "./styles.css";

export default function App() {
  const [state, setState] = useState({
    email: "",
    password: ""
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setState((prevProps) => ({
      ...prevProps,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(state);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            value={state.email}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-control">
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={state.password}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

```

Here's a [Code Sandbox demo](https://codesandbox.io/s/login-form-zird0r?file=/src/App.js).

In the above code, we have only two input fields, namely `email` and `password` and a submit button.

Each input field has a `value` and `onChange` handler added so we can update the state based on the user's input.

Also, we have added a `handleSubmit` method which displays the data entered in the form to the console.

This looks fine. But what if we need to add validations like required field validation, minimum length validation, password validation, email field validation and also display the corresponding error messages?

The code will become more complex and lengthy as the number of input fields and their validations increases.

## How to Install react-hook-form 

Displaying forms is a very common requirement in any application. 

So let’s learn why and how to use react-hook-form. For that, we'll create a new React application.

Create a new React project by running the following command from the terminal:

```js
create-react-app demo-react-hook-form
```

Once the project is created, delete all files from the `src` folder and create new `index.js` and `styles.css` files inside the `src` folder.

To install the `react-hook-form` library, execute the following command from the terminal:

```js
npm install react-hook-form@7.38.0

OR

yarn add react-hook-form@7.38.0
```

Here, we're installing version `7.38.0` of the `react-hook-form` library which is the latest version at the time of writing this article.

## How to Create Initial Pages

Open the `src/index.js` file and add the following content inside it:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

```

Note that the above code is using React version 18+ syntax for rendering the app.

If you're using React version less than 18 (which you can confirm from the `package.json` file), then add the following code in your `src/index.js` file.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

Now, open the `src/styles.css` file and add the content from [here](https://gist.github.com/myogeshchavan97/2e0b00d38f8f927799d8180906e9dde3) inside it.

Now, create a new file called `App.js` inside the `src` folder with the following content:

```js
import React from "react";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <form>
        <div className="form-control">
          <label>Email</label>
          <input type="text" name="email" />
        </div>
        <div className="form-control">
          <label>Password</label>
          <input type="password" name="password" />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}
```

Here, we have just added the email and password fields to the form.

## How to Create a Basic Form with react-hook-form

The `react-hook-form` library provides a `useForm` hook which we can use to work with forms.

Import the `useForm` hook like this:

```js
import { useForm } from 'react-hook-form';
```

You can use the `useForm` hook like this:

```js
const {
  register,
  handleSubmit,
  formState: { errors },
} = useForm();
```

Here,

* `register` is a function provided by the `useForm` hook. We can assign it to each input field so that the `react-hook-form` can track the changes for the input field value
* `handleSubmit` is the function we can call when the form is submitted
* `errors` is a nested property in the `formState` object which will contain the validation errors, if any

Now, replace the contents of the `App.js` file with the following code:

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input type="text" name="email" {...register("email")} />
        </div>
        <div className="form-control">
          <label>Password</label>
          <input type="password" name="password" {...register("password")} />
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

```

In the above code, we have added a register function to each input field that we got from the `useForm` hook by passing a unique name to each `register` function like this:

```js
{...register("email")}
```

We're using the spread operator so `react-hook-form` will spread out all the required event handlers like `onChange`, `onBlur`, and other props for that input field.

If you add a `console.log({ ...register("email") });` inside the component, you will see what it returns as can be seen below:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/register_output.png)

We also added the `onSubmit` function which is passed to the `handleSubmit` method like this:

```js
<form onSubmit={handleSubmit(onSubmit)}>
...
```

Note that, you need to pass a unique name to the `register` function added for each input field so `react-hook-form` can track the changing data.

When we submit the form, the `handleSubmit` function will handle the form submission. It will send the user entered data to the `onSubmit` function where we're logging the user data to the console.

```js
const onSubmit = (data) => {  
 console.log(data);
};
```

Now, start the application by running the `npm start`  or `yarn start` command and you will see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/login_logs-2.gif)

Here's a [Code Sandbox demo](https://codesandbox.io/s/login-form-forked-9so04x?file=/src/App.js).

As you can see, when we submit the form, the details entered by the user are displayed in the console.

Also, as compared to the code without `react-hook-form` (which we saw at the start of this article in this [Code Sandbox demo](https://codesandbox.io/s/login-form-zird0r?file=/src/App.js)), this code is much simpler. 

This is because we don’t have to add the `value` and `onChange` handler for each input field and there is no need to manage the application state ourselves.

## How to Add Validations to the Form

Now, let’s add the required field and minimum length validation to the input fields.

To add validation we can pass an object to the `register` function as a second parameter like this:

```js
<input
  type="text"
  name="email"
  {...register("email", {
    required: true
  })}
/>

<input
  type="password"
  name="password"
  {...register("password", {
    required: true,
    minLength: 6
  })}
/>
```

Here, for the email field, we're specifying required field validation. For the password field we're specifying the required field and minimum 6 character length validation.

When the validation fails, the `errors` object coming from the `useForm` hook will be populated with the fields for which the validation failed.

So we will use that `errors` object to display custom error messages.

Open the `App.js` file and replace its contents with the following content:

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            {...register("email", {
              required: true,
              pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
            })}
          />
          {errors.email && errors.email.type === "required" && (
            <p className="errorMsg">Email is required.</p>
          )}
          {errors.email && errors.email.type === "pattern" && (
            <p className="errorMsg">Email is not valid.</p>
          )}
        </div>
        <div className="form-control">
          <label>Password</label>
          <input
            type="password"
            name="password"
            {...register("password", {
              required: true,
              minLength: 6
            })}
          />
          {errors.password && errors.password.type === "required" && (
            <p className="errorMsg">Password is required.</p>
          )}
          {errors.password && errors.password.type === "minLength" && (
            <p className="errorMsg">
              Password should be at-least 6 characters.
            </p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

```

If you check the application now, you will see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/basic_validation-2.gif)

Here's a [Code Sandbox demo](https://codesandbox.io/s/login-form-with-validations-6388wx?file=/src/App.js).

As you can see, we're getting instant validation errors for each input field once we submit the form and then try to enter the values in the input fields.

If there is any error for any of the input field, the `errors` object will be populated with the type of error which we're using to display our own custom error message like this:

```js
{errors.email && errors.email.type === "required" && (
    <p className="errorMsg">Email is required.</p>
)}
{errors.email && errors.email.type === "pattern" && (
    <p className="errorMsg">Email is not valid.</p>
)}
```

Here, based on the type of error, we're displaying different error messages.

Using the [ES11 optional chaining operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining), you can further simplify the above code like this:

```js
{errors.email?.type === "required" && (
    <p className="errorMsg">Email is required.</p>
)}
{errors.email?.type === "pattern" && (
    <p className="errorMsg">Email is not valid.</p>
)}
```

In the similar way, we have added the password field validation.

Also, as you can see, each input field is automatically focused when we submit the form if there is any validation error for that input field.

Also, the form is not submitted as long as there is a validation error. If you check the browser console, you will see that the `console.log` statement is only printed if the form is valid and there are no errors.

So using `react-hook-form` reduced the amount of code that we had to write. The validation is also responsive, so once the field becomes valid, the error message goes away instantly.

But as the number of validations for each field increases, the conditional checks and error message code will still increase. So we can further refactor the code to make it even simpler.

Take a look at the below code:

```js
import React from "react";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Email</label>
          <input
            type="text"
            name="email"
            {...register("email", {
              required: "Email is required.",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Email is not valid."
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </div>
        <div className="form-control">
          <label>Password</label>
          <input
            type="password"
            name="password"
            {...register("password", {
              required: "Password is required.",
              minLength: {
                value: 6,
                message: "Password should be at-least 6 characters."
              }
            })}
          />
          {errors.password && (
            <p className="errorMsg">{errors.password.message}</p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

```

In the code above, we have changed the email and password validation code.

For the email input field, we changed this previous code:

```js
 {...register("email", {
     required: true,
     pattern: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/
 })}
```

to the below code:

```js
{...register("email", {
    required: "Email is required.",
    pattern: {
        value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
        message: "Email is not valid."
    }
})}
```

Here, we’ve directly provided the error message we want to display while adding the validation itself.

So we no longer need to add extra checks for each validation. We are displaying the error message using the `message` property available inside the `errors` object for each input field like this:

```js
{errors.email && <p className="errorMsg">{errors.email.message}</p>}
```

So by doing it this way, the code is further simplified which makes it easy to add extra validations in the future.

Note that, if there are validation errors, the onSubmit handler will not be executed and the corresponding input field will automatically be focused (which is a good thing).

Here's an updated [Code Sandbox demo](https://codesandbox.io/s/login-form-with-validations-simplified-7o4y0k?file=/src/App.js).

## How to Add a Multiple Validations

You can even provide multiple validations for the input field by adding a `validate` object. This is useful if you need to perform complex validations like this:

```js
 <input
    type="password"
    name="password"
    {...register("password", {
        required: true,
        validate: {
            checkLength: (value) => value.length >= 6,
            matchPattern: (value) =>
            /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)(?=.*[!@#$*])/.test(
                value
            )
        }
    })}
/>
```

and to display the error messages, we use it like this:

```js
{errors.password?.type === "required" && (
    <p className="errorMsg">Password is required.</p>
)}
{errors.password?.type === "checkLength" && (
    <p className="errorMsg">
    	Password should be at-least 6 characters.
    </p>
)}
{errors.password?.type === "matchPattern" && (
    <p className="errorMsg">
    	Password should contain at least one uppercase letter, lowercase
letter, digit, and special symbol.
    </p>
)}
```

Here's a [Code Sandbox demo](https://codesandbox.io/s/login-form-with-validations-multiple-zyvp69?file=/src/App.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/multiple_validations.gif)

## How to Reset the Form Values

Sometimes, we need to reset/clear the data entered by the user after some action.

For example, once the form is submitted, we want to show the success message and then clear the form data so the user should not re-submit the same data.

In such a case, we can call the `reset` function returned by the `useForm` hook to clear the form data.

```js
const { reset } = useForm();

```

Here's a [Code Sandbox demo](https://codesandbox.io/s/reset-form-buowrs?file=/src/App.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/reset.gif)

The `reset` function also accepts an optional object where you can pass the values you want the form data to reset:

```js
reset({
    username: "Alex",
    email: "alex@example.com",
    password: "Test@123"
});
```

Here, the key username, email or password should match with the name passed to the `register` function so the respective input field will be set to the passed value.

## How to Set Initial Form Values Using defaultValues

The [useForm](https://react-hook-form.com/api/useform/) hook accepts a list of options, one of which is `defaultValues`.

Using `defaultValues` we can set initial values for the form elements and re-set them when moving from one page to another like this:

```js
const { user } = props;
const {
    register,
    handleSubmit,
    formState: { errors }
} = useForm({
   defaultValues: {
      first_name: user.first_name,
      last_name: user.last_name
    }
});

// JSX

<Form.Control
    type="text"
    {...register("first_name")}
/>

<Form.Control
    type="text"
    {...register("last_name")}
/>

```

In the above code, for the `register` function we've passed `first_name` as the name. This means that in the `defaultValues` we're using the same name to set the initial value.

So to correctly set the input value, you need to use the same name used in the `register` function for setting the initial value using `defaultValues`.

Here's a [Code Sandbox demo](https://codesandbox.io/s/nice-khorana-80rktx?file=/src/components/FirstStep.js).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/retain_values.gif)

## How to Use react-hook-form with Other Libraries

Sometimes, we might be using some external libraries like [react-select](https://react-select.com/home) to allow multiple selection in a dropdown.

In such cases, we can't directly add the `register` function for showing the select dropdown. So If we want to add `react-hook-form` validations without writing our own code and handler function, we can use the `Controller` component from `react-hook-form` like this:

```js
import React from "react";
import { useForm, Controller } from "react-hook-form";
import Select from "react-select";
import "./styles.css";

const departments = [
  { value: "Computer-Science", label: "Computer Science" },
  { value: "Physics", label: "Physics" },
  { value: "Chemistry", label: "Chemistry" },
  { value: "Mathematics", label: "Mathematics" }
];

export default function App() {
  const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-control">
          <label>Select Department of Interest</label>
          <Controller
            name="department"
            control={control}
            rules={{ required: true }}
            render={({ field }) => (
              <Select {...field} isMulti options={departments} />
            )}
          />
          {errors.department && (
            <p className="errorMsg">This is a required field.</p>
          )}
        </div>
        <div className="form-control">
          <label></label>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
}

```

Here's a [Code Sandbox demo](https://codesandbox.io/s/react-hook-form-controller-g8jxbf?file=/src/App.js).

As you can see in the above code, we're importing the `Controller` component  at the top:

```js
import { useForm, Controller } from "react-hook-form";
```

and `control` from `useForm` hook like this:

```js
const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm();
```

Note, we're not using the `register` function here.

Regular use of the [react-select](https://react-select.com/home) library to allow multiple selection goes like this:

```js
import Select from "react-select";

// use
<Select isMulti options={options} />
```

But to use it with `react-hook-form` we need to wrap it in the `Controller` component:

```js
<Controller
    name="department"
    control={control}
    rules={{ required: true }}
    render={({ field }) => (
       <Select {...field} isMulti options={options} />
    )}
 />
```

Here, we have to give a unique value for the `name` prop in the `Controller`.

The validations are added as a part of the `rules` prop and we use the `render` prop to render the `Select` dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/controller.gif)

## How to Use Other Input Types with react-hook-form

In this section, we'll see how to use radio buttons and checkboxes with `react-hook-form`.

Take a look at the below code:

```js
import React from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import "./styles.css";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit(onSubmit)}>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter your email"
            {...register("email", {
              required: "Please enter your email",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Please enter a valid email"
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="gender">
          <Form.Label>Select Gender</Form.Label>
          <Form.Check
            type="radio"
            label="Male"
            value="male"
            {...register("gender", {
              required: "Please select your gender"
            })}
          />
          <Form.Check
            type="radio"
            label="Female"
            value="female"
            {...register("gender")}
          />
          {errors.gender && <p className="errorMsg">{errors.gender.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="skills">
          <Form.Label>Select Your Skills</Form.Label>
          <Form.Check
            type="checkbox"
            label="JavaScript"
            value="JavaScript"
            {...register("skills", {
              required: "Please select at-least one skill"
            })}
          />
          <Form.Check
            type="checkbox"
            label="React"
            value="react"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Node.js"
            value="nodejs"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Angular"
            value="angular"
            {...register("skills")}
          />
          {errors.skills && <p className="errorMsg">{errors.skills.message}</p>}
        </Form.Group>
        <label></label>
        <Button type="submit" variant="primary">
          Submit
        </Button>
      </form>
    </div>
  );
}

```

Here's a [Code Sandbox demo](https://codesandbox.io/s/react-hook-form-other-inputs-zm7u7f?file=/src/App.js).

In the above code, I'm using [react-bootstrap](https://react-bootstrap.github.io/) to make the UI look good, so `Form.Check` is a `react-bootstrap` component.

The main point you need to remember is that we've not given the same names for the `register` function for a group of radio buttons and checkboxes like this:

```js
<Form.Check
    type="radio"
    label="Male"
    value="male"
    {...register("gender", {
        required: "Please select your gender"
    })}
/>
<Form.Check
    type="radio"
    label="Female"
    value="female"
    {...register("gender")}
/>
```

In the above code, we've given `gender` as the name for both the radio buttons and `skills` as the name for all the checkboxes as shown below:

```js
<Form.Check
    type="checkbox"
    label="JavaScript"
    value="JavaScript"
    {...register("skills", {
        required: "Please select at-least one skill"
    })}
/>
<Form.Check
    type="checkbox"
    label="React"
    value="react"
    {...register("skills")}
/>
<Form.Check
    type="checkbox"
    label="Node.js"
    value="nodejs"
    {...register("skills")}
/>
<Form.Check
    type="checkbox"
    label="Angular"
    value="angular"
    {...register("skills")}
/>
```

Also, note that the required field validation is added only for the first radio button or checkbox. Because we're using the same name, we don't need to add the same validation to each radio button or checkbox.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/radio_checkbox.gif)

## How to Set Initial Values for Radio Buttons And Checkboxes

Sometimes we may have pre-selected radio buttons or checkboxes which we need to display on page load, in such a case, we can again use the `defaultValues` option from for the `useForm` hook.

Take a look at the below code:

```js
import React from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import "./styles.css";

const initialValues = {
  gender: "male",
  skills: {
    JavaScript: true,
    react: false,
    nodejs: true,
    angular: false
  }
};

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: {
      gender: initialValues.gender,
      skills: Object.keys(initialValues.skills).filter(
        (item) => initialValues.skills[item] === true
      )
    }
  });

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit(onSubmit)}>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter your email"
            {...register("email", {
              required: "Please enter your email",
              pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Please enter a valid email"
              }
            })}
          />
          {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="gender">
          <Form.Label>Select Gender</Form.Label>
          <Form.Check
            type="radio"
            label="Male"
            value="male"
            {...register("gender", {
              required: "Please select your gender"
            })}
          />
          <Form.Check
            type="radio"
            label="Female"
            value="female"
            {...register("gender")}
          />
          {errors.gender && <p className="errorMsg">{errors.gender.message}</p>}
        </Form.Group>
        <Form.Group className="mb-3" controlId="skills">
          <Form.Label>Select Your Skills</Form.Label>
          <Form.Check
            type="checkbox"
            label="JavaScript"
            value="JavaScript"
            {...register("skills", {
              required: "Please select at-least one skill"
            })}
          />
          <Form.Check
            type="checkbox"
            label="React"
            value="react"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Node.js"
            value="nodejs"
            {...register("skills")}
          />
          <Form.Check
            type="checkbox"
            label="Angular"
            value="angular"
            {...register("skills")}
          />
          {errors.skills && <p className="errorMsg">{errors.skills.message}</p>}
        </Form.Group>
        <label></label>
        <Button type="submit" variant="primary">
          Submit
        </Button>
      </form>
    </div>
  );
}

```

Here's a [Code Sandbox demo](https://codesandbox.io/s/react-hook-form-other-inputs-initial-values-t38s9v?file=/src/App.js).

In the above code, we have an `initialValues` object which contains the values we want to set on the initial page load:

```js
const initialValues = {
  gender: "male",
  skills: {
    JavaScript: true,
    react: false,
    nodejs: true,
    angular: false
  }
};
```

As we can have multiple skills, `skills` is an object as shown above. So we want to show the radio button selected if its value is `male` and we want to show only those checkboxes selected for which the value is `true` in the `skills` object.

Therefore, for the `defaultValues` option, we're looping over the `skills` object using the `filter` method to find out the skills for which the value is `true` as shown below:

```js
const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: {
      gender: initialValues.gender,
      skills: Object.keys(initialValues.skills).filter(
        (item) => initialValues.skills[item] === true
      )
    }
  });
```

As the `JavaScript` and `nodejs` values are `true`, the `skills` array after the `filter` method will become `["JavaScript", "nodejs"]` so the `defaultValues` object will look like this: 

```js
useForm({
    defaultValues: {
        gender: 'male',
        skills: ["JavaScript", "nodejs"]
    }
});
```

Therefore, when the page is loaded, only the `male` gender and the `JavaScript` and `Node.js` skills will be selected/checked by default.

Note that the casing used in the `skills` object has to match with the `value` specified for the checkbox. 

So even though the label for checkbox is `Node.js`, it's value is `nodejs` so we're using `nodejs` as the key in the `initialValues` object.

Below is the demo of how it looks on page load.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/default_checked.gif)

And that's it! You've learned how to use react-hook-form to more easily build complex forms in React.

## Thanks for Reading!

If you want to learn Redux in detail from scratch and build 3 apps along with the [complete food ordering app](https://www.youtube.com/watch?v=2zaPDfCKAvM), check out my [Mastering Redux](https://master-redux.yogeshchavan.dev/) course.

In the course, you will learn:

* Basic and advanced Redux
* How to manage the complex state of array and objects
* How to use multiple reducers to manage complex redux state
* How to debug a Redux application
* How to use Redux in React using the react-redux library to make your app reactive.
* How to use the redux-thunk library to handle async API calls
* Build 3 different apps using Redux

and much more.

Finally, we'll build a complete [food ordering app](https://www.youtube.com/watch?v=2zaPDfCKAvM) from scratch with stripe integration for accepting payments and deploy it to production.

**Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**

