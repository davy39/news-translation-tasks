---
title: Forms in HTML – How to Build Basic Forms with HTML
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-12T14:44:04.000Z'
originalURL: https://freecodecamp.org/news/build-basic-forms-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Presentacion-Brainstorming-Lluvia-de-Ideas-Doodle-Blanco.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Forms are a fundamental part of web development, allowing users to input
  and submit data efficiently.

  Creating forms in HTML is a relatively straightforward process. In this article,
  we''ll explore how to build basic forms using HTML <form>, <input>, ...'
---

Forms are a fundamental part of web development, allowing users to input and submit data efficiently.

Creating forms in HTML is a relatively straightforward process. In this article, we'll explore how to build basic forms using HTML `<form>`, `<input>`, and `<button>` elements. We'll also cover various input types such as text, password, radio buttons, checkboxes, and submit buttons.

## What is a Form in HTML?

In HTML, a form is a container used to collect and submit data from website visitors. It acts as an interactive area where users can input information, such as text, selections, and options, which can then be sent to a server for processing.

Forms are a fundamental component of web development, enabling user engagement and data exchange.

HTML forms are not just limited to simple text inputs. They encompass a variety of features and input types that enhance their functionality. Forms can include text inputs, password fields, radio buttons, checkboxes, and submit buttons, among others. These features allow you to collect and process data efficiently from users.

## The `<form>` Element

To start creating a form, you'll use the `<form>` element. This element defines a container for all the form elements. Here's a basic example of a form:

```html
<form>
  <!-- Form elements will go here -->
</form>

```

## Text Input

Text input fields are used for collecting single-line text data, such as a name or email address. You can create a text input field using the `<input>` element with the `type` attribute set to "text.‌

```html
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name">

```

Result:

<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name">


In this code snippet, the `for` attribute in the `<label>` element associates the label with the input field, making it more accessible and user-friendly.

## Password Input

Password input fields are like text inputs, but the entered characters are hidden as dots or asterisks for security. 

To create a password input field, set the `type` attribute to "password."

```html
<label for="password">Password:</label>
<input type="password" id="password" name="password" placeholder="Enter your password">

```

Result:

<label for="password">Password:</label>
<input type="password" id="password" name="password" placeholder="Enter your password">


## Radio Buttons

Radio buttons are used when you want users to select one option from a list. Each option is represented by a radio button. 

To create radio buttons, use the `<input>` element with the `type` attribute set to "radio."

```html
<form>

    <label>Choose Your Preferred Payment Method:</label>
    <input type="radio" id="creditCard" name="paymentMethod" value="creditCard">
    <label for="creditCard">Credit Card</label><br>

    <input type="radio" id="paypal" name="paymentMethod" value="paypal">
    <label for="paypal">PayPal</label><br>

    <input type="radio" id="bitcoin" name="paymentMethod" value="bitcoin">
    <label for="bitcoin">Bitcoin</label><br>
 
</form>

```

Result:

<form>

    <label>Choose Your Preferred Payment Method:</label>
    <input type="radio" id="creditCard" name="paymentMethod" value="creditCard">
    <label for="creditCard">Credit Card</label><br>

    <input type="radio" id="paypal" name="paymentMethod" value="paypal">
    <label for="paypal">PayPal</label><br>

    <input type="radio" id="bitcoin" name="paymentMethod" value="bitcoin">
    <label for="bitcoin">Bitcoin</label><br>
 
</form>


In this example, using the same `name` attribute for both radio buttons groups them together, allowing the user to select one option.

## Checkboxes

Checkboxes are used when you want users to select one or more options from a list. Each option is represented by a checkbox. 

To create checkboxes, use the `<input>` element with the `type` attribute set to "checkbox."

```html
<label>Interests:</label>
<input type="checkbox" id="music" name="interest" value="music">
<label for="music">Music</label>

<input type="checkbox" id="sports" name="interest" value="sports">
<label for="sports">Sports</label>

<input type="checkbox" id="reading" name="interest" value="reading">
<label for="reading">Reading</label>

```



Result:

<label>Interests:</label>
<input type="checkbox" id="music" name="interest" value="music">
<label for="music">Music</label>

<input type="checkbox" id="sports" name="interest" value="sports">
<label for="sports">Sports</label>

<input type="checkbox" id="reading" name="interest" value="reading">
<label for="reading">Reading</label>


With checkboxes, users can select multiple options based on their preferences.

## Submit Button

A submit button is used to send the form data to the server for processing. You can create a submit button using the `<button>` element with the `type` attribute set to "submit."

```html
<button type="submit">Submit</button>

```

Result:

<button type="submit">Submit</button>


This button triggers the form's submission when clicked.

## Accessibility Matters

While we've discussed the basics, it's crucial to delve into the accessibility of HTML forms. 

**Accessibility** in web development is about ensuring that all users, regardless of their abilities or disabilities, can perceive, understand, navigate, and interact with your web content. 

This principle extends to HTML forms as well. Accessible forms are not only ethical but also often legally required, as many countries have established web accessibility standards and regulations to promote inclusivity.

## How to Create Accessible Forms in HTML

### Semantic HTML

Begin by using semantic HTML elements. For example, use the `<form>` element to wrap your form, `<label>` elements to label form fields, and `<input>` elements with appropriate `type` attributes. 

Semantics help screen readers and other assistive technologies understand the content.

### Labeling

Always associate form fields with labels using the `for` attribute in the `<label>` element and the `id` attribute in the related `<input>`. This allows screen reader users to hear a label when they focus on an input, providing context and clarity.

```html
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name">

```

### Descriptive Text

Use clear and concise labels that describe the purpose of each form field. Avoid generic labels like "Field 1" or "Enter Data."

### Keyboard Accessibility

Test your forms using only the keyboard for navigation. Make sure users can interact with form elements, such as selecting radio buttons and checkboxes, using the "Tab" key and "Enter" key.

### Error Handling

When a user makes an error, provide clear and helpful error messages. Use the `aria-invalid` attribute to indicate that an input has an error.

```html
<input type="text" aria-invalid="true" />

```

### ARIA Roles and Attributes

The Accessible Rich Internet Applications (ARIA) specification provides roles and attributes to enhance the accessibility of web content. 

For example, you can use `aria-describedby` to associate a field with additional descriptive information.

```html
<label for="password">Password:</label>
<input type="password" id="password" name="password" placeholder="Enter your password" aria-describedby="password-hint">
<div id="password-hint">Password must be at least 8 characters long.</div>

```

Result:

<label for="password">Password:</label>
<input type="password" id="password" name="password" placeholder="Enter your password" aria-describedby="password-hint">
<div id="password-hint">Password must be at least 8 characters long.</div>


### Fieldset and Legend

If your form contains groups of related fields, use the `<fieldset>` element with a `<legend>` element to provide a title for the group. This helps users understand the grouping of form elements.

```html
<fieldset>
  <legend>Address Information</legend>
  <!-- Address fields go here -->
</fieldset>

```

### The Inclusive Experience

Creating accessible forms isn't just a legal requirement – it's an opportunity to offer an inclusive experience to all users. 

When your forms are designed with accessibility in mind, you ensure that everyone, regardless of their abilities, can access the information and services your website provides. 

Accessible HTML forms follow best practices in labeling, structure, keyboard navigation, and error handling. By considering these factors, you can create forms that are user-friendly for everyone, including people with disabilities.

## Mobile Responsiveness

In today's mobile-first world, it's vital to make your forms responsive to various screen sizes. Test your forms on different devices to ensure they work and appear correctly on both desktop and mobile platforms. Responsive design is integral to providing a positive user experience.

## Putting It All Together

Now that we've covered various form elements and input types, let's put them together into a complete form. Here's an example of a simple registration form:

```html
<form>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Enter your name"><br>

  <label for="email">Email:</label>
  <input type="text" id="email" name="email" placeholder="Enter your email"><br>

  <fieldset>
    <legend>Gender:</legend>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
  </fieldset>

  <fieldset>
    <legend>Interests:</legend>
    <input type="checkbox" id="music" name="interest" value="music">
    <label for="music">Music</label>

    <input type="checkbox" id="sports" name="interest" value="sports">
    <label for="sports">Sports</label>

    <input type="checkbox" id="reading" name="interest" value="reading">
    <label for="reading">Reading</label>
  </fieldset>

  <label for="password">Password:</label>
  <input type="password" id="password" name="password" placeholder="Enter your password"><br>

  <button type="submit">Submit</button>
</form>

```

Result:

<form>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Enter your name"><br>

  <label for="email">Email:</label>
  <input type="text" id="email" name="email" placeholder="Enter your email"><br>

  <fieldset>
    <legend>Gender:</legend>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
  </fieldset>

  <fieldset>
    <legend>Interests:</legend>
    <input type="checkbox" id="music" name="interest" value="music">
    <label for="music">Music</label>

    <input type="checkbox" id="sports" name="interest" value="sports">
    <label for="sports">Sports</label>

    <input type="checkbox" id="reading" name="interest" value="reading">
    <label for="reading">Reading</label>
  </fieldset>

  <label for="password">Password:</label>
  <input type="password" id="password" name="password" placeholder="Enter your password"><br>

  <button type="submit">Submit</button>
</form>


This is a complete form with text inputs, radio buttons, checkboxes, a password input, and a submit button.

## Conclusion

Creating forms in HTML is an essential skill for web development. By using the `<form>`, `<input>`, and `<button>` elements, and understanding various input types, you can design interactive and user-friendly forms to collect data from your website visitors. 

Forms are a critical component of user engagement, and mastering their creation is a significant step in web development.

In this article, we've explored the basics of building forms, including text and password inputs, radio buttons, checkboxes, and submit buttons. Now, you have the knowledge to create and customize forms for various purposes on your websites.

Start experimenting and enhancing your web applications with forms today :)

