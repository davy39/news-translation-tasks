---
title: How to Build Forms in React
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-03-10T17:43:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-forms-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-rodnae-productions-7821577.jpg
tags:
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: null
seo_desc: "Forms play an essential role in modern web applications. They enable users\
  \ to share information, complete tasks and provide feedback. \nWithout forms, many\
  \ of the tasks that we take for granted on the web, such as logging in, signing\
  \ up, or making pur..."
---

Forms play an essential role in modern web applications. They enable users to share information, complete tasks and provide feedback. 

Without forms, many of the tasks that we take for granted on the web, such as logging in, signing up, or making purchases, would not be possible.

As such, learning how to create effective and user-friendly forms is essential for developers looking to build engaging and interactive web applications.

With its extensive collection of built-in hooks, React provides several features and techniques for creating and managing forms, including state management, event handling, and form validation.

The purpose of this guide is to provide a comprehensive and in-depth look at creating forms in React. 

## Getting Started...

In React, there are two ways of handling form data:

* **Controlled Components:** In this approach, form data is handled by React through the use of hooks such as the `useState` hook.
* **Uncontrolled Components:** Form data is handled by the Document Object Model (DOM) rather than by React. The DOM maintains the state of form data and updates it based on user input.

To better understand the difference between controlled and uncontrolled components, consider there are two ways of riding a bike.

In the first approach, you let the bike take control. You sit on the bike and let it decide the direction and speed. You might try to make it go in a certain direction by leaning your body, but ultimately, the bike decides where to go.

This is similar to uncontrolled components in React. You place a form element in the component, and the DOM takes control of it. The DOM decides the state of the input element and updates it based on a user's input.

In the second approach, you take control of the bike. You hold the handlebars and pedal, and you decide where to go and how fast to ride. You can easily slow down or speed up as needed.

This is similar to controlled components where a React component takes control of the form data, and maintains the state of form elements. The component decides when and how to update the state, and it re-renders itself based on the state changes.

In the upcoming sections, we will expound upon the distinction between controlled and uncontrolled components and provide practical examples to illustrate how each operates.

## Controlled Components in React

In React, a controlled component is a component where form elements derive their value from a React state.

When a component is controlled, the value of form elements is stored in a state, and any changes made to the value are immediately reflected in the state.

To create a controlled component, you need to use the `value` prop to set the value of form elements and the `onChange` event to handle changes made to the value.

The `value` prop sets the initial value of a form element, while the `onChange` event is triggered whenever the value of a form element changes. Inside the `onChange` event, you need to update the state with the new value using a state update function.

Here's an example:

```javascript
import {useState} from 'react';
 
export default function  ControlledComponent()  {
	const  [inputValue, setInputValue] =  useState('');

	const  handleChange = (event) => {
		setInputValue(event.target.value);
	};

return  (
<form>
	<label>Input Value:
	<input  type="text"  value={inputValue} onChange={handleChange} />
	</label>
	<p>Input Value: {inputValue}</p>
</div>
)};

```

In this example:

The `useState` hook defines a state variable (inputValue) and a state update function (setInputValue).

The `value` prop sets the initial value of the input element to the value of `inputValue`.

Also, the `onChange` event handles changes made to the input value. The `handleChange` function updates the `inputValue` state with the new value of the input element, and the updated value is immediately reflected in the state and displayed on the screen.

<img src="https://i.imgur.com/N77Ohpv.gif" style="border: 1px solid #333; border-radius: 5px"/>

As the user types into the input field, the `handleChange` function updates the state variable using the "setInputValue" function. The component is then re-rendered, and the input field's `value` attribute is updated to reflect the new value of `inputValue`.

The value of the input field and the text displayed below it are always in sync, making it a controlled component.

### How to handle dropdowns and checkboxes in Controlled Components

Just like with input elements, the value of a dropdown can be set by using the `value` prop in conjunction with the `onChange` event handler to update the state of the component.

For example, to handle a dropdown menu, you can define the initial value of the dropdown menu within the state of the component, then update the state when the value of the dropdown changes:

```javascript
import { useState } from "react";

export default function Dropdown()  {
	const [selectedOption, setSelectedOption] = useState("option1");

	const  handleDropdownChange = (event) => {
		setSelectedOption(event.target.value);
	};

return  (
	<div>
		<label>
			Select an option:
				<select  value={selectedOption} onChange={handleDropdownChange}>
				<option  value="option1">Option 1</option>
				<option  value="option2">Option 2</option>
				<option  value="option3">Option 3</option>
			</select>
		</label>
		<p>Selected option: {selectedOption}</p>
	</div>
	);
}

```

<img src="https://i.imgur.com/5cjbAeO.gif" style="border: 1px solid #333; border-radius: 5px"/>

Similarly, you can handle checkboxes by setting the `checked` prop of the checkbox input element based on the state of a component, and then updating the state when a checkbox is clicked.

Here's an example:

```javascript
import { useState } from "react";

function Checkbox() {
  const [isChecked, setIsChecked] = useState(false);

  const handleChange = (event) => {
    setIsChecked(event.target.checked);
  };

  return (
    <form>
      <label htmlFor="color">
        <input type="checkbox" name="color" checked={isChecked} onChange={handleChange}/>
        Blue
      </label>

      {isChecked && <div>Blue is selected!</div>}
    </form>
  );
}

export default Checkbox;

```

In this example, we have defined a state variable `isChecked` to keep track of whether the checkbox is checked or not. When the checkbox is clicked, the `handleChange` function is called, and it updates the `isChecked` state variable to a new value (true or false.).

The `isChecked` variable controls the `checked` attribute of the checkbox input and conditionally renders a message indicating that the checkbox is selected.

<img src="https://i.imgur.com/81zMRzO.gif" style="border: 1px solid #333; border-radius: 5px"/>

### How to handle multiple form fields

When working with forms in React, it's common to have several form elements, such as text inputs, checkboxes, radio buttons, and others. 

To manage the state of these form elements, you can define the values for the input fields as an object using a single state variable and update each respective state variable using the `onChange` event.

As an example, suppose you wish to create a form with the following fields:

* Text input for the user's name
* An email field for the user's email
* A textarea field for the user's message

Here's how you could handle these fields:

```javascript
import { useState } from "react";

export default function Multiple() {
  const [formData, setFormData] = useState({name: "",email: "",message: ""});

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Name: ${formData.name}, Email: ${formData.email}, Message: ${formData.message}`
    );
};

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Name:</label>
      <input type="text" id="name" name="name" value={formData.name} onChange={handleChange}/>

      <label htmlFor="email">Email:</label>
      <input type="email" id="email" name="email" value={formData.email} onChange={handleChange}/>

      <label htmlFor="message">Message:</label>
      <textarea id="message" name="message" value={formData.message} onChange={handleChange}/>

      <button type="submit">Submit</button>
    </form>
  );
}

```

<img src="https://i.imgur.com/4ln01Wq.gif" style="border: 1px solid #333; border-radius: 5px"/>

In the example code:

The `useState` hook defines a state object named `formData` that contains three properties: `name`, `email`, and `message`, each initialized to an empty string.

The `handleChange` function is called whenever a user types in one of the form fields. It extracts the `name` and `value` of the form field that has changed using the `event.target` object and then updates the `formData` state variable using the `setFormData` function.

The `setFormData` function uses the spread operator (`...`) to copy the previous `formData` object. Then it updates the value of the changed form field by setting its value prop with the new value.

By using an object to manage form data, we can easily keep track of the values of multiple form elements. This makes it easier to manage and manipulate the state of our form data, especially when dealing with complex forms with many form elements.

### How to validate form input

Validating forms refers to the process of checking user input data to ensure that it meets specific criteria or requirements before it is submitted to a server or used in some other way.

Form validation can take various forms, depending on the type and complexity of the data being collected. Common types of form validation include:

* Required field validation: Checking that required fields are not left empty.
* Format validation: Ensuring that input data is in the correct format (for example, email addresses, phone numbers, and so on).
* Length validation: Checking that input data is within a certain length range.
* Pattern validation: Checking that input data matches a specific pattern.

Common methods for form validation include using built-in HTML validation attributes like `required`, `minlength`, and `maxlength`, as well as using React to perform custom validation logic.

As an example, suppose we have a form with an input field that requires a minimum of 5 characters. We can use state to track the value of the input field and display an error message if the length of the value is less than 5.

```javascript
import { useState } from 'react';

function MyForm() {
  const [inputValue, setInputValue] = useState('');
  const [inputError, setInputError] = useState(null);

  function handleInputChange(event) {
    const value = event.target.value;
    setInputValue(value);

    if (value.length < 5) {
      setInputError('Input must be at least 5 characters');
    } else {
      setInputError(null);
    }
  }

  function handleSubmit(event) {
    event.preventDefault();
    if (inputValue.length >= 5) {
      // submit form
    } else {
      setInputError('Input must be at least 5 characters');
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Fruit:
        <input type="text" value={inputValue} onChange={handleInputChange} />
      </label>
      {inputError && <div style={{ color: 'red' }}>{inputError}</div>}
      <button type="submit">Submit</button>
    </form>
  );
} 

```

<img src="https://i.imgur.com/Dfm7dtp.gif" style="border: 1px solid #333; border-radius: 5px"/>

In this example, we have a simple form that allows the user to input a fruit name. The form has two states:

* `inputValue`: Represents the current value of the input field
* `inputError`: Represents any errors that may arise during form validation.

The `handleInputChange` function is called every time a user types a character in the input field. It updates the `inputValue` state to reflect the current value of the input field, and then checks whether the value is at least 5 characters long.

If the value is less than 5 characters, it sets the `inputError` state to the appropriate error message. Otherwise, it sets the `inputError` state to `null` (indicating that there are no errors).

## Uncontrolled Components in React

Uncontrolled components in React refer to form elements whose state is not managed by React. Instead, their state is handled by the browser's DOM.

For instance, let's say you have a form that consists of a text input field, a select box, and a checkbox. In a controlled component, you would create a state for each form element and write event handlers to update the state whenever the user interacts with any of the form elements.

In contrast, an uncontrolled component allows the browser to handle the form elements' state. When a user enters text into a text input field or selects an option from a select box, the browser updates the DOM's state for that element automatically.

To get the value of an uncontrolled form element, you can use a feature called "ref". "Refs" provide a way to access the current value of DOM elements. You can create a "ref" using the `useRef` hook, then attach it to the form element you want to access. This allows you to retrieve the current value of an element at any time, without needing to manage its state in your React component.

Here's an example of an uncontrolled component:

```javascript
import { useRef } from "react";

export default function Uncontrolled() {
  const selectRef = useRef(null);
  const checkboxRef = useRef(null);
  const inputRef = useRef(null);

  function handleSubmit(event) {
    event.preventDefault();
    console.log("Input value:", inputRef.current.value);
    console.log("Select value:", selectRef.current.value);
    console.log("Checkbox value:", checkboxRef.current.checked);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        <p>Name:</p>
        <input ref={inputRef} type="text" />
      </label>
      <label>
        <p>Favorite color:</p>
        <select ref={selectRef}>
          <option value="red">Red</option>
          <option value="green">Green</option>
          <option value="blue">Blue</option>
        </select>
      </label>
      <label>
        Do you like React?
        <input type="checkbox" ref={checkboxRef} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}


```

<img src="https://i.imgur.com/4zXvzMm.gif" style="border: 1px solid #333; border-radius: 5px"/>

In this example:

We have a form that contains a text input field, a select box, and a checkbox. Instead of creating state for each form element and writing event handlers to update the state, we're using uncontrolled components. This means that the browser is responsible for managing the state of the form elements.

When a user interacts with a form element, the browser automatically updates the DOM's state for that element. And to retrieve the current values of each form element, we're using the `useRef` hook.

Uncontrolled components can be useful in certain situations, such as when you need to integrate with third-party libraries or when you don't need to manipulate the form data.

Overall, uncontrolled components are a simpler approach to working with forms in React, and they can make your code more concise and easier to read. But it's important to note that using `ref` to access form element values can make your code harder to test and maintain, so use them judiciously.

## How to Use React Component Libraries

Creating forms in React can be overwhelming, especially if you're new to the framework. You need to manage form state, handle user input, validate input data and more.

But the good news is that there are third-party libraries available to make everything easier for you.

These libraries can help simplify your form creation process. They provide a wide range of features including form validation, input masking, submission handling, error handling, and more. This makes it much easier to create forms that are both user-friendly and functional.

Some popular form libraries include:

* Formik
* Redux Form
* React Hook Form
* Yup.

In this section, we'll focus on learning how to use the **React Hook Form** library.

### How to use React Hook Form

React Hook Form is a lightweight library for managing forms in React applications. Whether you need to create a simple contact form or a complex multi-step form, React Hook Form can help simplify your form creation process.

#### Installation

Getting started with React Hook Form is straightforward and requires only a few steps. First, you'll need to install the library in your project. You can do this using `npm` by running the following command:

```npm
npm install react-hook-form

```

Alternatively, you can use yarn to install React Hook Form:

```yarn
yarn add react-hook-form

```

Once you've installed the library, you need to import the `useForm` hook from the `react-hook-form` package in your component.

```javascript
import  { useForm }  from  "react-hook-form";

```

By importing the `useForm` hook, you can start using React Hook Form to manage forms in your application.

The `useForm` hook provides several functions and properties that you can use to manage your form:

* `register`: This function is used to register form fields with React Hook Form.
* `handleSubmit`: This is used to handle form submissions. It takes a callback function that is called when the form is submitted.
* `errors`: This represents an object containing any validation errors that occur when a form is submitted.
* `watch`: This function is used to watch for changes to specific form fields. It takes an array of form field names and returns the current value of those fields.

These are just a few examples of the functions and properties the useForm hook provides. You can find the complete list of functions and properties in the React Hook Form [documentation](https://www.react-hook-form.com/api/useform/).

#### How to set up the form

After importing the `useForm` hook, you can invoke it to get access to the functions and properties that it provides:

```jsx
const { register, handleSubmit, formState:{errors} } = useForm();

```

In the above code, we're using destructuring to extract the `register`, `handleSubmit`, and `errors` properties from the `useForm` hook.

#### How to register form fields

The next step is to register form fields using the `register` function. The `register` function takes two parameters:

* `name`: The name of the form field.
* `validationOptions`: An optional object containing validation rules you can apply to a form field.

Here's an example of registering an input field and adding a validation rule that it is a required field.

```jsx
<input name="firstName" {...register("firstName", { required: true })} />

```

#### How to handle form submission

To handle form submission, you can use the `handleSubmit` function.

```jsx
const onSubmit = (data) => console.log(data);

<form onSubmit={handleSubmit(onSubmit)}>
  // form fields
</form>


```

In this example, we pass the `onSubmit` function to the `handleSubmit` function. The `onSubmit` function will be called when the form is submitted and will receive an object containing the values of each form field.

#### How to display validation errors

You can use the `errors` object to display any validation errors.

```jsx
<input {...register("firstName", { required: true })} />
{errors.firstName && <p>This field is required</p>}

```

In the above code, we're using the `errors` object to display a validation error message if the `firstName` field is not filled out. We can also display error messages for other validation rules, such as minimum and maximum lengths, regular expressions, and more.

#### How to put it all together

With a basic understanding of React Hook Form, let's now put everything into practice and create a simple form with two fields: `email` and `password`. We'll require both fields to be filled out and validate the email field using a regular expression.

```jsx
import { useForm } from 'react-hook-form';

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  
  const onSubmit = (data) => {
    console.log(data);
  };
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Email</label>
      <input type="email" {...register("email", { required: true, pattern: /^\S+@\S+$/i })} />
      {errors.email && <p>Email is required and must be valid</p>}
      
      <label>Password</label>
      <input type="password" {...register("password", { required: true })} />
      {errors.password && <p>Password is required</p>}
      
      <button type="submit">Submit</button>
    </form>
  );
}

export default LoginForm;

```

<img src="https://i.imgur.com/zDd8ZDK.gif" style="border: 1px solid #333; border-radius: 5px"/>

In this section, we've covered the basics of how to use React Hook Form:

* To register form fields
* Handle form submissions
* Display validation errors

But this is just the tip of the iceberg. React Hook Form offers many more features and capabilities that we haven't covered here. So I highly recommend that you check out the React Hook Form [documentation](https://react-hook-form.com/get-started/) to learn more about how to use it effectively in your projects.

## Recap

In this tutorial, we covered the basics of building forms in React. We learned that there are two common approaches to building forms in React: controlled and uncontrolled components.

Controlled components rely on state management to track the state of form inputs, while uncontrolled components use `refs` to access the form inputs and their values.

We also learned that using third-party libraries make form creation in React much easier. Libraries like React Hook Form provide a lot of functionality out of the box and can help reduce the amount of boilerplate code you need to build forms in React.

With these concepts in mind, you should be able to build complex forms in React that are easy to manage and provide a great user experience.

## Conclusion

If you want access to all the code used in this article, including the styling, I have compiled it all in a single [repository](https://github.com/dboatengg/react-forms) for your convenience. Head over to the repository and you will find everything you need.

Happy coding!

