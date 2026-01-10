---
title: How to Use HTML Forms – HTML Form Basics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-06T10:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-forms
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/glenn-carstens-peters-RLw-UC03Gwc-unsplash.jpg
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: null
seo_desc: "By Kelechukwu Isaac Awoke\nHTML forms are used to get information from\
  \ users. They are widely used in webpages or apps for surveys or registration processes.\
  \ \nHTML form basics include the common HTML elements, tags, attributes, concepts,\
  \ or best pract..."
---

By Kelechukwu Isaac Awoke

HTML forms are used to get information from users. They are widely used in webpages or apps for surveys or registration processes. 

HTML form basics include the common HTML elements, tags, attributes, concepts, or best practices required for you to create good HTML forms. The collected data is sent to a server for processing.

* [Basic Structure of HTML Form](#heading-basic-structure-of-html-form)
* [How to Use HTML Form Elements](#heading-how-to-use-html-form-elements)
* [How to Use the HTML <input> Element](#heading-how-to-use-the-html-element)
* [How to Use the HTML <label> Element](#heading-how-to-use-the-html-element)
* [How to Use the HTML <textarea> Element](#heading-how-to-use-the-html)
* [How to Use the HTML <select> Element](#heading-how-to-use-the-html-element)
* [Form Validation](#heading-form-validation)
* [Importance of Form Validation](#heading-importance-of-form-validation)
* [Types of Form Validation](#heading-types-of-form-validation)
* [Common Validation Techniques](#heading-common-validation-techniques)
* [Form Submission and Methods](#heading-form-submission-and-methods)
* [How to Style HTML Forms](#heading-how-to-style-html-forms)
* [Best Practices and Accessibility](#heading-best-practices-and-accessibility)
* [Conclusion](#heading-conclusion)

## Basic Structure of HTML Form

You can use the `<form>` element to create an HTML form

```html
<form action="submit_form" method=" post">
  <label for="name">Name:</label>
  <input type="text" id="name" name=" name" required>
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  
  <button type="submit">Submit</button>
</form>
```

 The HTML `<form>` element is a container for several HTML form elements. The `<form>` element can contain the following:

* `<input>`
* `<label>`
* `<select>`
* `<textarea>`
* `<button>`
* `<fieldset>`
* `<legend>`
* `<datalist>`
* `<output>`
* `<option>`
* `<optgroup>`

## How to Use HTML Form Elements

In this section, you'll learn how to use some of the HTML form elements.

### How to Use the HTML <input> Element

The `<input>` element is the most commonly used form element. The type of information an `<input>` element can hold depends on the `<type>` attribute. 

The `<input>`  element can only accept a particular type of data assigned to it using the `<type>`  attribute.

```html
<form action="">
      <input
        type="text"
        id="name"
        name="username"
        placeholder="Enter your username"
        required
      />
      <input
        type="password"
        id="security"
        name="password"
        placeholder="Enter your password"
        required
      />
      <input type="email" name="email" placeholder="Enter your email" />
      <input type="checkbox" name="subscribe" value="yes" /> Subscribe to the
      newsletter <input type="radio" name="gender" value="male" /> Male
      <input type="radio" name="gender" value="female" /> Female
      <input type="submit" name="submit" />
</form>
```

 The following are the different  `<type>` attributes that can be assigned to an `<input>` element:

* `<input type="text">`: Allows the user to type in text.
* `<input type="email">`: The user input must follow an email format.
* `<input type="password">` : Accepts password from the user. The passwords are masked, usually displayed as asterisks (*) or dots, to protect the privacy of the input.
* `<input type="checkbox">`: The user can select none or many of the displayed checkboxes. Checkboxes can be checked or unchecked.
* `<input type="radio">`: Allows the user to select only one from the multiple-choice radio buttons.
* `<input type="submit">`: Enables the user to submit the form.

The following are other possible attributes found in the input element:

* `<input name=" ">` : Assigns the input field a name. The assigned name identifies the input data when the form is submitted.
* `<input id=" ">`: The identifier creates a unique id for the input field. It is usually associated with CSS for styling and JavaScript for other manipulations.
* `<input value=" ">`: Used to set the initial value for the input field. The default initial value gives the user an idea of the information required.
* `<input placeholder=" ">`: A faint pseudo value set to the input field that disappears once the user starts typing. Gives a hint on what data to enter, similar to the value attribute.
* `<input required>`: Requires that the input field must be filled out before submission. Gives an error message when not filled out.
* `<input disabled>`: As the name implies, this prevents the user from interacting with the input field. Disables the input field from accepting input. With this attribute, the input field becomes unclickable.
* `<input readonly>`: The user can only read the initially set value but can't change it. Unlike the disabled attribute, the input field is clickable but can't be modified.

Note that the `<input>` element doesn't contain a `for` attribute.

### How to Use the HTML <label> Element

The label element associates text with a form input, checkbox, or radio button.

```html
<form action=" ">
	<label for="name" id="user">Username:</label>
</form> 
```

The label element describes the information required in the text field.

The label element is important for accessibility, this makes it easier for screen-reader users to navigate the form. The assistive technologies read the label loud to users.

Clicking on the label focuses the corresponding input field when the `for` attribute of the label element corresponds with the id attribute of the input element, making it more convenient for users to interact with the form.

Label improves the overall usage of the form, providing context and guidance.

The following are the commonly used attributes for the `label` element:

* `<label for=" "></label>`: Associates the label with the corresponding form element, usually an input element. The value of the `for` attribute is always the same as the id value of the associated form element, usually the input element.
* id attribute `<label id=" "></label>`: Gives the label a unique identifier. The value is set to the same value with the `for` attribute of the corresponding form element, usually an input element. Used for selecting the label for styling in CSS or other manipulations in JavaScript.

### How to Use the HTML <textarea> Element

A multi-line text input field, allows users to write longer text or paragraphs. The `rows` and `cols` attributes control the initial size of the textarea box. 

```html
<form action="">
      <label for="testimony">Testimony:</label>
      <textarea name="testimony" id="testimony" cols="30" rows="10"></textarea>
</form>
```

The `rows` attribute controls the height (vertical size) of the textarea box, determining the number of visible lines while the `cols` attribute controls the width (horizontal size), specifying the number of visible characters per line. 

Note, that the `textarea` box can _wrap_ to fit the entered text within its defined width.

Unlike the single-line input field, the `textarea` element does not have a `maxlength` attribute or `value` attribute. The content is placed within the opening and closing tags. 

For accessibility, it's a good practice to associate label or context with the `textarea` element to assist users who use screen-readers or other assistive technologies.

#### How to Use the HTML <select> Element

The `<select>` element creates a drop-down list, that allows users to select one or multiple options from the listed choices.

```html
<form action="">
      <label for="numbers">Choose a favorite number:</label>
      <select name="numbers" id="numbers" size="5" multiple>
        <option value="" disabled selected>Select a number</option>
        <option value="one">1</option>
        <option value="two">2</option>
        <option value="three">3</option>
        <option value="four">4</option>
        <option value="five">5</option>
        <option value="six">6</option>
        <option value="seven">7</option>
        <option value="eight">8</option>
        <option value="nine">9</option>
        <option value="ten">10</option>
      </select>
</form>
```

The `<option>` element is contained within the `<select>` element. The `<option>` element holds the items to be selected. Each `<option>` represents one item in the drop-down list.

Each `<option>` element is expected to have a `<value=" ">` attribute, which holds the value to be submitted when the form containing the `<select>` element is submitted. If the `<value=" ">` attribute is omitted, the text content of the `<option>` element becomes the value to be submitted instead.

The `<name=" ">` attribute identifies the select control on the server side when the form is submitted. The `<name=" ">` is important for processing the form data on the server. 

You can select one of the options as the default selection by including the `<selected>` attribute in the `<option>` element. If no option is selected, then the first option in the list will be selected by default.

The `<size=" ">` attribute sets the number of options you can see at once in the drop-down by setting the `<size=" ">` attribute on the `<select>`. Note that other options are seen as you scroll down. 

Including the `<disabled>` attribute on the `<select>` element, disables the select option and prevents the users from selecting any option. The select option becomes unclickable. 

Also, multiple options can be selected by including `<multiple>` attribute on the `<select>` element. You can hold the `Ctrl` (or Command on Mac) key to select multiple options.

Understanding the `<select>` element and using the necessary attributes can make your form convenient for users to select different options and for easy processing of the `<select>` element on the server side.

## Form Validation

Simply put, this is the process of checking whether the data entered in the form is correct, complete, and meets the specified format.

### Importance of Form Validation

* **Data Accuracy:**  Prevents submission of incorrect or incomplete data.
* **Security:** Checks the data to prevent incorrect or malicious data from being submitted, thereby reducing harmful attacks or data breaches. 
* **User Experience:**  Makes filling out the forms less stressful by giving a quick error message if the user is entering the wrong data. Also, it can be used to suggest the expected format. 
* **Efficiency:** Form validation before submission saves time and resources. Reduces unnecessary requests to the server, improving the overall performance of your application.

### Types of Form Validation

1. **Client-Side Validation:** The user's browser performs the checks before submission. How does the browser validate forms? Browsers use JavaScript, CSS, or HTML attributes to validate forms. The advantage of client-side validation is the quick error message the user receives when data is incorrect or incomplete. The response is quick and doesn't require validation from the server side. One of the disadvantages is that client-side validation can be bypassed by an experienced user. 
2. **Server-Side Validation:** The server checks the form data after submission. Server-side validation is more robust and secure. Performs double verification, and validates form data again, even if the client-side validation fails or is bypassed. The server-side validation is commonly done by using scripting languages like PHP or ASP.NET. 

Note that you can use either of the two or a combination of both.    

### Common Validation Techniques

These are common HTML attributes that help you decide the pattern of form validation.

#### Length Limits 

You can use the `maxlength` attribute to set the maximum number of characters an input field can hold.

```html
<form>
  <input type="text" id="username" name="username" placeholder="Username" maxlength="20" required>
  <button type="submit">Submit</button>
</form>
```

#### Required Fields 

Requires that certain input fields are filled before the form is submitted. The `<required>` attribute is used to perform this technique. An error message is displayed when the required field is not filled by the user. 

```html
<form>
  <input type="text" id="username" name="username" placeholder="Username" required>
  <input type="email" id="email" name="email" placeholder="Email" required>
  <button type="submit">Submit</button>
</form>
```

#### Data Format 

Ensures the data entered by the user follows the required format. The `<input type="email">` type attribute set to email will require the user to enter the correct email format (for example: me@example.com) before form submission. 

The same thing happens if the type attribute is set to number `<input type="number">`, the user can only put data from 0-9.

```html
<form>
  <input type="email" id="email" name="email" placeholder="Email" required>
  <button type="submit">Submit</button>
</form>
```

#### Password Strength 

The `<pattern="">` attribute is used to specify password complexity such as minimum length, and the inclusion of uppercase or lowercase letters, numbers, and special characters. 

The `<title="">` attribute displays the error message when the user hovers over the input field or when the entered password does not match the specified password format. The higher the password complexity, the higher the user account is protected from unauthorized access.

```html
<form>
  <input type="password" id="password" name="password" placeholder="Password" pattern="(?=.\d)(?=.[a-z])(?=.*[A-Z]).{8,}" title="Password must contain at least one number, one uppercase letter, one lowercase letter, and at least 8 or more characters" required>
  <button type="submit">Submit</button>
</form>
```

#### Numeric values 

You can set the range of numeric values to be entered by the user by using the `min` and `max` attributes. For example, to check if a user is within the specified age range:

```html
<form>
  <input type="number" id="age" name="age" placeholder="Age" min="18" max="100" required>
  <button type="submit">Submit</button>
</form>
```

Having a good form validation practice helps to create forms with accurate data and reduces vulnerability to malicious attacks. 

## Form Submission and Methods

When the submit button is clicked after filling out a form, your information is sent to the server for processing. This is called form submission. 

### Methods of Form Submission

Form data is sent to the server using the `method` attribute. There are two commonly used methods:

#### GET Method

With the `get` method `<method="get">`, the form data is sent using the URL in the browser's address bar to the server. 

```html
<form action="http://example.com" method="get">
          <input type="text" name="name" />
          <input type="submit" value="Submit" />
 </form>
```

Using the above code sample, when the user enters a name (let's say the user's name is KC) in the input field named ''name'', and clicks the submit button, the form data will be sent to the server in the URL like this: "http://example.com?name=KC". 

The GET method is not safe, as it is commonly used for sending small amounts of data that is not sensitive.  

#### POST Method

The post method attribute `<method=post>` sends the form data in the body of the HTTP request to the server, rather than in the URL.

```html
<form action="http://example.com" method="get">
          <input type="text" name="name" />
          <input type="submit" value="Submit" />
 </form>
```

Using the same code sample above, the POST method will send the form data to the server like this: "https://example.com/submit.php". 

You'd should notice that the POST request does not contain the form data in the URL but rather points to the server-side script (submit.php) that will process the form data. 

The sent form data is not visible. The POST request is used to submit sensitive information, like passwords, since the data is not visible in the URL, but rather sent in the HTTP body request.

## How to Style HTML Forms

HTML forms can be styled using CSS, just like any other HTML element. You can do the following with CSS to match the design of your website:

* **Selectors**: CSS selectors such as element selectors, class selectors, or ID selectors can be used to select specific elements in the HTML code for styling.
* **Typography**: Typography can be used to set the font-family, adjust the size, font-weight, and color of the text within the form element to enhance readability. 
* **Box Model**: With the knowledge of CSS properties like padding, border, and margin, which affect the spacing and layout, you can style HTML elements.
* **Colors and Backgrounds**: The color of your text or background can be styled using the CSS properties like color and background-color (or background-image) respectively. 
* **Responsiveness**: With media queries, you can make your form responsive and adapt to different screen sizes and devices. 
* **Layout**: You can control the layout of a form to make it user-friendly with CSS properties like display, float, and positioning.

## Best Practices and Accessibility

Like every other HTML document, ensure your form complies with web standards and is accessible to people with disabilities. For best practices and accessibility, take note of the following:

### Structures and Semantics

* Always use proper semantic HTML elements (like  `<form>`, `<input>`, `<label>`, and so on) to structure not just forms but every other HTML document.
* Nest elements properly and associate labels to their respective input field. 
* Make sure your input fields have the appropriate type attributes.

### Error Handling and Validation

* Combine both client-side and server-side validation to avoid incorrect or incomplete data submission.
* Use the appropriate attribute to display error messages when form submission fails or validation errors occur. 

### Responsive Design

* Your forms should be responsive and adapt to various screen sizes and devices.
* Use CSS media queries to adjust your form layouts and styles based on the viewport size.

### Design and Contrast

* Use fonts and colors that are easy to see.
* The color contrast between text and background should ensure readability, especially for users with low vision. 

### ARIA Roles and Attributes

* ARIA (Accessible Rich Internet Application) roles and attributes improve accessibility for screen-reader users or other assistive technologies.
* ARIA attributes ( `aria-labelledby`, `aria-describedby`, and `aria-invalid`) provide additional context and feedback for form elements.

## Conclusion

Creating good HTML forms that meet web standards improve user interaction and experience on your website. By following the best practices and accessibility, developers can create forms that are user-friendly, and effective in collecting data from users. 

You can learn more about HTML forms and responsive web design using [freeCodeCamp's Responsive Web Design Certification](https://www.freecodecamp.org/learn/2022/responsive-web-design/)

