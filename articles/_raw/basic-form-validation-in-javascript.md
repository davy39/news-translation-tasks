---
title: Basic Form Validation in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/basic-form-validation-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d33740569d1a4ca3673.jpg
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "In the past, form validation would occur on the server, after a person\
  \ had already entered in all of their information and pressed the submit button.\
  \ \nIf the information was incorrect or missing, the server would have to send everything\
  \ back with a m..."
---

In the past, form validation would occur on the server, after a person had already entered in all of their information and pressed the submit button. 

If the information was incorrect or missing, the server would have to send everything back with a message telling the person to correct the form before submitting it again.

This was a lengthy process and would put a lot of the burden on the server.

These days, JavaScript provides a number of ways to validate a form's data right in the browser before sending it to the server.

Here's the HTML code we'll use in the following examples:

```html
<html>
<head>
  <title>Form Validation</title>
  <script type="text/javascript">
    // Form validation will go here
  </script>
</head>
<body>
  <form id="form">
    <table cellspacing="2" cellpadding="2" border="1">
      <tr>
        <td align="right">Username</td>
        <td><input type="text" id="username" /></td>
      </tr>
      <tr>
        <td align="right">Email Address</td>
        <td><input type="text" id="email-address" /></td>
      </tr>
      <tr>
        <td></td>
        <td><input type="submit" value="Submit" id="submit-btn" /></td>
      </tr>
    </table>
  </form>
</body>
</html>
```

## Basic Validation

This type of validation involves checking all the mandatory fields and making sure they're properly filled in.

Here's a basic example of a function `validate` that shows an alert if the username and email address inputs are blank, otherwise it returns true:

```js
const submitBtn = document.getElementById('submit-btn');

const validate = (e) => {
  e.preventDefault();
  const username = document.getElementById('username');
  const emailAddress = document.getElementById('email-address');
  if (username.value === "") {
    alert("Please enter your username.");
    username.focus();
    return false;
  }
  if (emailAddress.value === "") {
    alert("Please enter your email address.");
    emailAddress.focus();
    return false;
  }
  
  return true;
}

submitBtn.addEventListener('click', validate);

```

But what if someone enters in random text as their email address? Currently the `validate` function will still return true. As you can imagine, sending bad data to the server can lead to problems.

That's where data format validation comes in.

## Data Format Validation

This type of validation actually looks at the values in the form and verifies that they are correct.

Validating email addresses is notoriously difficult – there are a vast number of legitimate email addresses and hosts, and it's impossible to guess all the valid combinations of characters.

That said, there are a few key factors that are common in all valid email addresses: 

* An address must contain one @ and at least one dot (.) character
* The @ character cannot be the first character in the address
* The . must come at least one character after the @ character

With this in mind, maybe developers use regex to determine if an email address is valid or not. Here's a function that [Tyler McGinnis recommends on his blog](https://tylermcginnis.com/validate-email-address-javascript/):

```js
const emailIsValid = email => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

emailIsValid('free@code@camp.org') // false
emailIsValid('quincy@freecodecamp.org') // true
```

Added to the code from the last example, it will look like this:

```js
const submitBtn = document.getElementById('submit-btn');

const validate = (e) => {
  e.preventDefault();
  const username = document.getElementById('username');
  const emailAddress = document.getElementById('email-address');
  if (username.value === "") {
    alert("Please enter your username.");
    username.focus();
    return false;
  }
    
  if (emailAddress.value === "") {
    alert("Please enter your email address.");
    emailAddress.focus();
    return false;
  }

  if (!emailIsValid(emailAddress.value)) {
    alert("Please enter a valid email address.");
    emailAddress.focus();
    return false;
  }
  
  return true; // Can submit the form data to the server
}

const emailIsValid = email => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

submitBtn.addEventListener('click', validate);

```

## HTML5 Form Constraints

Some of commonly used HTML5 constraints for `<input>` are the `type` attribute (e.g. `type="password"`), `maxlength`, `required` and `disabled`. 

A less commonly used constraint is the `pattern` attribute that takes a JavaScript regular expression.

## More Information

* [Form Data Validation | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)
* [Constraint validation | MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation)

