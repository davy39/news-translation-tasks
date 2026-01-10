---
title: Data Validation – How to Check User Input on HTML Forms with Example JavaScript
  Code
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2021-01-18T17:56:53.000Z'
originalURL: https://freecodecamp.org/news/form-validation-with-html5-and-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6003768298be260817e4aadc.jpg
tags:
- name: Form validations
  slug: form-validations
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Forms are ubiquitous in web applications. Some apps use forms to collect\
  \ data to sign up users and provide an email address. Others use them to fulfill\
  \ online transactions to facilitate a shopping experience. \nYou might use some\
  \ web forms to apply fo..."
---

Forms are ubiquitous in web applications. Some apps use forms to collect data to sign up users and provide an email address. Others use them to fulfill online transactions to facilitate a shopping experience. 

You might use some web forms to apply for a new car loan, whereas you'll use others to order pizza for dinner. So it's important that the data collected from those forms is cleaned, formatted correctly, and devoid of any malicious code. This process is called form validation.

We need form validation anytime we are accepting user input. We must ensure that the data entered is in the correct format, lies within a valid range of data (such as for date fields), and does not contain malicious code that could lead to SQL injections. Malformed or missing data can also cause the API to throw errors.

## What are the different types of form validations?

Form validation can happen on the client side and the server side.

Client side validation occurs using HTML5 attributes and client side JavaScript. 

You may have noticed that in some forms, as soon as you enter an invalid email address, the form gives an error "Please enter a valid email". This immediate type of validation is usually done via client side JavaScript.

![Validation error for incorrect credit card number](https://www.freecodecamp.org/news/content/images/2021/04/form-validation-cc.gif)

In other cases, you may have noticed that when you fill out a form and enter details such as a credit card, it may show a loading screen and then show an error "This credit card is invalid". 

Here, the form made a call to its server side code, and returned a validation error after performing additional credit card checks. This validation case where a server-side call is made is called server side validation.

## What data should be validated?

Form validation is needed anytime you accept data from a user. This may include:

1. Validating the format of fields such as email address, phone number, zip code, name, password.
2. Validating mandatory fields
3. Checking the type of data such as string vs number for fields such as social security number.
4. Ensuring that the value entered is a valid value such as country, date, and so on.

## How to set up client side validation

On the client side, validation can be done in two ways:

1. Using HTML5 functionality
2. Using JavaScript


### How to set up validation with HTML5 functionality

HTML5 provides a bunch of attributes to help validate data. Here are some common validation cases:

- Making fields required using `required`
- Constraining the length of data:
  - `minlength`, `maxlength`: for text data
  - `min` and `max` for max value of num type
- Restricting the type of data using `type`:
  - `<input type="email" name="multiple>`
- Specifying data patterns using `pattern`:
  - specifies a regex pattern that the entered form data needs to match

When the input value matches the above HTML5 validation, it gets assigned a psuedo-class `:valid`, and `:invalid` if it doesn't.

Let's try an example:

```HTML
<form>
<label for="firstname"> First Name: </label>
<input type="text" name="firstname" id="firstname" required maxlength="45">
<label for="lastname"> Last Name: </label>
<input type="text" name="lastname" id="lastname" required maxlength="45">
<button>Submit</button>
</form>
```

![Client side form validation for required fields using HTML5 attributes](https://www.freecodecamp.org/news/content/images/2021/04/form-validation-required.png)


[Link to JSFiddle](https://jsfiddle.net/58xc2qyj/)

Here we have two required fields - First Name and Last Name. Try this example in JSFidle. If you skip either of these fields and press submit, you'll get a message, "Please fill out this field". This is validation using in-built HTML5.


### How to set up validation using JavaScript

When implementing form validation, there are a few things to consider:

1. What is defined as "valid" data? This helps you answer questions about the format, length, required fields, and type of data.
2. What happens when invalid data is entered? This will help you define the user experience of the validation - whether to show an error message inline or at the top of the form, how detailed should the error message be, should the form be sumitted anyways, should there be analytics to track invalid format of data? And so on.

You can perform JavaScript validation in two ways:

1. Inline validation using JavaScript
1. HTML5 Constraint validation API

#### Inline validation using JavaScript

```html
<form id="form">
  <label for="firstname"> First Name* </label>
  <input type="text" name="firstname" id="firstname" />
  <button id="submit">Submit</button>

  <span role="alert" id="nameError" aria-hidden="true">
    Please enter First Name
  </span>
</form>
```

```javascript
const submit = document.getElementById("submit");

submit.addEventListener("click", validate);

function validate(e) {
  e.preventDefault();

  const firstNameField = document.getElementById("firstname");
  let valid = true;

  if (!firstNameField.value) {
    const nameError = document.getElementById("nameError");
    nameError.classList.add("visible");
    firstNameField.classList.add("invalid");
    nameError.setAttribute("aria-hidden", false);
    nameError.setAttribute("aria-invalid", true);
  }
  return valid;
}
```

```css
#nameError {
  display: none;
  font-size: 0.8em;
}

#nameError.visible {
  display: block;
}

input.invalid {
  border-color: red;
}
```

[Link to JSFiddle](https://jsfiddle.net/0tq3e49w/4/)

In this example, we check for required fields using JavaScript. If a required field is not present, we use CSS to show the error message. 

Aria labels are modified accordingly to signal an error. By using CSS to show / hide an error, we are reducing the number of DOM manipulations we need to make. The error message is provided in-context thereby making the user experience intuitive.

#### HTML5 Constraint validation API

The `required` and `pattern` HTML attributes can help perform basic validation. But if you want more complex validation or want to provide detailed error messaging, you can use the Constraint Validation API. 

Some methods provided by this API are:

1. `checkValidity`
2. `setCustomValidity`
3. `reportValidity`

The following properties are useful:

1.  `validity`
2.  `validationMessage`
3.  `willValidate`


In this example, we will validate using HTML5 inbuilt methods such as `required` and `length` in conjunction with the Constraint Validation API to provide detailed error messages.

```HTML
<form>
<label for="firstname"> First Name: </label>
<input type="text" name="firstname" required id="firstname">
<button>Submit</button>
</form>
```

```javascript
const nameField = document.querySelector("input");

nameField.addEventListener("input", () => {
  nameField.setCustomValidity("");
  nameField.checkValidity();
  console.log(nameField.checkValidity());
});

nameField.addEventListener("invalid", () => {
  nameField.setCustomValidity("Please fill in your First Name.");
});
```

[Link to JSFiddle](https://jsfiddle.net/xz2wjLck/1/)

## Don't forget server side validation

Client side validation is not the only validation check you should do. You must also validate the data received from your client on the server side code to ensure that the data matches what you expect it to be. 

You can also use server-side validation to perform business logic verifications that should not live on the client side.

## Form Validation best practices

1. Always have server side validation, since malicious actors can bypass client side validation.
2. Provide detailed error messages in-context with the field that produced the error.
3. Provide an example of what the data should look like in case of an error message, such as - "Email did not match format - test@example.com"
4. Avoid using single error pages that involve redirection. This is bad user experience and forces the user to go back to a previous page to fix the form and lose context.
5. Always mark required fields.



### Interested in more tutorials and articles like this? [Sign up for my newsletter.](https://tinyletter.com/shrutikapoor) or [follow me on Twitter](https://twitter.com/shrutikapoor08)




