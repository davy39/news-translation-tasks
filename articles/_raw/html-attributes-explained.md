---
title: HTML Attributes Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T18:45:00.000Z'
originalURL: https://freecodecamp.org/news/html-attributes-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3a740569d1a4ca3699.jpg
tags:
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'HTML elements can have attributes, which contain additional information
  about the element.

  HTML attributes generally come in name-value pairs, and always go in the opening
  tag of an element. The attribute name says what type of information you’re pro...'
---

HTML elements can have attributes, which contain additional information about the element.

HTML attributes generally come in name-value pairs, and always go in the opening tag of an element. The attribute name says what type of information you’re providing about the element, and the attribute value is the actual information.

For example, an anchor (`<a>`) element in an HTML document creates links to other pages, or other parts of the page. You use the `href` attribute in the opening `<a>` tag to tell the browser where the link sends a user.

Here’s an example of a link that sends users to freeCodeCamp’s home page:

```html
<a href="www.freecodecamp.org">Click here to go to freeCodeCamp!</a>
```

Notice that the attribute name (`href`) and value (“www.freeCodeCamp.org”) are separated with an equals sign, and quotes surround the value.

There are many different HTML attributes, but most of them only work on certain HTML elements. For example, the `href` attribute won’t work if it’s placed in an opening `<h1>` tag.

In the example above, the value supplied to the `href` attribute could be any valid link. However, some attributes only have a set of valid options you can use, or values need to be in a specific format. The `lang` attribute tells the browser the default language of the contents in an HTML element. The values for the `lang` attribute should use standard language or country codes, such as `en` for English, or `it` for Italian.

## **Boolean Attributes**

Some HTML attributes don’t need a value because they only have one option. These are called Boolean attributes. The presence of the attribute in a tag will apply it to that HTML element. However, it’s okay to write out the attribute name and set it equal to the one option of the value. In this case, the value is usually the same as the attribute name.

For example, the `<input>` element in a form can have a `required` attribute. This requires users to fill out that item before they can submit the form.

Here are examples that do the same thing:

```html
<input type="text" required >
<input type="text" required="required" >
```

You can read more about the <a href>, <a target>, <script> src, and roll attributes here:

## [<a href> Attribute](https://www.freecodecamp.org/news/the-a-href-attribute-explained/)

## **[<script> src Attribute](https://www.freecodecamp.org/news/link-javascript-to-html-with-the-src/)**

## [roll Attribute](https://www.freecodecamp.org/news/html-role-attribute/)

## [<a target> Attribute](https://www.freecodecamp.org/news/the-a-target-html-attribute-explained/)



Now let's learn more about some other HTML attributes:

## **P Align Attribute**

### **Important**

This attribute is not supported in HTML5. It is recommended to use the [`text-align` CSS property](https://guide.freecodecamp.org/css/text-align).

To align the text inside a `<p>` tag, this attribute will help.

### **Syntax**

```html
<p align="position">Lorem Ipsum...</p>
```

### **Attributes**

* **left** - Text aligns to the left
* **right** - Text aligns to the right
* **center** - Text aligns to the center
* **justify** - All lines of text have equal width

### **Example**

```html
<html>
<body>
<p align="center">Paragraph align attribute example</p>
</body>
</html>
```

## **Img Src Attribute**

The `<img src>` attribute refers to the source of the image you want to display. The `img` tag will not display an image without the `src` attribute. However, if you set the source to the location of the image, you can display any image.

There is an image of the freeCodeCamp Logo located at `https://avatars0.githubusercontent.com/u/9892522?v=4&s=400`

You can set that as the image using the `src` attribute.

```html
<html>
  <head>
    <title>Img Src Attribute Example</title>
  </head>
  <body>
    <img src="https://avatars0.githubusercontent.com/u/9892522?v=4&s=400">
  </body>
</html>
```

The above code displays like this:

![The freeCodeCamp Avatar](https://avatars0.githubusercontent.com/u/9892522?v=4&s=400?raw=true)

The `src` attribute is supported by all browsers.

You can also have a locally hosted file as your image.

For example, `<img src="images/freeCodeCamp.jpeg>` would work if you had a folder called `images` which had the `freeCodeCamp.jpeg` inside, as long as the ‘images’ folder was in the same location as the `index.html` file.

`../files/index.html`

`..files/images/freeCodeCamp.jpeg`

## **Font Size Attribute**

This attribute specifies the font size as either a numeric or relative value. Numeric values range from `1` to `7` with `1` being the smallest and `3` the default. It can also be defined using a relative value, like `+2` or `-3`, which set it relative to the value of the size attribute of the `<basefont>` element, or relative to `3`, the default value, if none does exist.

Syntax:

`<font size="number">`

Example:

```html
<html>
  <body>
    <font size="6">This is some text!</font>
  </body>
</html>
```

Note : `The size attribute of <font> is not supported in HTML5. Use CSS instead.`

## **Font Color Attribute**

This attribute is used to set a color to the text enclosed in a `<font>` tag.

### **Syntax:**

html

```text

### Important:
This attribute is not supported in HTML5. Instead, this [freeCodeCamp article](https://guide.freecodecamp.org/css/colors) specifies a CSS method, which can be used.

### Note:
A color can also be specified using a 'hex code' or an 'rgb code', instead of using a name.

### Example:
1. Color name attribute
```html
<html>
 <body>
  <font color="green">Font color example using color attribute</font>
</body>
</html>
```

Hex code attribute

```html
<html>
<body>
<font color="#00FF00">Font color example using color attribute</font>
</body>
</html>
```

RGB attribute

```html
<html>
<body>
<font color="rgb(0,255,0)">Font color example using color attribute</font>
</body>
</html>
```

## **Autofocus Attribute** 

The **autofocus** attribute is a boolean attribute.

When present, it specifies that the element should automatically get input focus when the page loads.

Only one form element in a document can have the **autofocus** attribute. It cannot be applied to `<input type="hidden">`.

### **Applies to**

ElementAttribute`<button>`autofocus`<input>`autofocus`<select>`autofocus`<textarea>`autofocus

### **Example**

```html
<form>
    <input type="text" name="fname" autofocus>
    <input type="text" name="lname">
</form>
```

### **Compatibility**

This is an HTML5 attribute.

## **Onclick Event Attribute**

When the element is clicked fires a event.

It works just like the _onclick method_ or `addEventListener('click')` to the element.

```html
<element onclick="event"></element>
```

`event` can be a JavaScript function or you can write raw JavaScript

### **Examples**

Changing the color of a `<p>` element when clicked

```html
<p id="text" onclick="redify()">Change my color</p>

<script>
function redify(){
  let text = document.querySelector('#text');
  text.style.color = "red";
}
</script>
```

Using raw JavaScript onclick attribute:

```html
<button onclick="alert('Hello')">Hello World</button>
```

## **Img Align Attribute**

The align attribute of an image specifies where the image should be aligned according to the surrounding element.

Attribute Values:  
right - Align image to the right left - Align image to the left  
top - Align image to the top  
bottom - Align image to the bottom  
middle - Align image to the middle

For example:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
   <title>Img Align Attribute</title>
 </head>
<body>
  <p>This is an example. <img src="image.png" alt="Image" align="middle"> More text right here
  <img src="image.png" alt="Image" width="100"/>
  </body>
</html>
```

We can also align in right if we want:

```html
<p>This is another example<img src="image.png" alt="Image" align="right"></p>
```

**Please note the align attribute is not supported in HTML5, and you should use CSS instead. However, it is still supported by all the major browsers.**

## **Input Type Attribute**

The input type attribute specifies the type of the input the user should put in your form.

### **text**

One line of a text.

```html
    <form>
      <label for="login">Login:</label>
      <input type="text" name="login">
    </form>
```

### **password**

One line of a text. Text is automatically displayed as a series of dots or asterisks (depends on the browser and OS).

```html
    <form>
      <label for="password">Password:</label>
      <input type="password" name="password">
    </form>
```

### **email**

The HTML checks if the input matches the e-mail address format (something@something).

```html
    <form>
      <label for="email">E-mail address:</label>
      <input type="email" name="email">
    </form>
```

### **number**

Allow only numeric input. You can also specify the min and max value allowed. The example below check that the input is number between 1 and 120.

```html
    <form>
      <label for="age">Age:</label>
      <input type="number" name="age" min="1" max="120">
    </form>
```

### **radio**

Only one option can be selected by the user. The group of radio buttons need to have the same name attribute. You can select automatically one option by using `checked` property (in example below the value Blue is selected).

```html
    <form>
      <label><input type="radio" name="color" value="red">Red</label>
      <label><input type="radio" name="color" value="green">Green</label>
      <label><input type="radio" name="color" value="blue" checked>Blue</label>
    </form>
```

### **checkbox**

User can select zero or more options from the group of checkboxes. You can use `checked` property here too for one or more options.

```html
    <form>
      <label><input type="checkbox" name="lang" value="english">english</label>
      <label><input type="checkbox" name="lang" value="spanish">spanish</label>
      <label><input type="checkbox" name="lang" value="french">french</label>
    </form>
```

### **button**

The input is displayed as button, the text which should be displayed in the button is in value attribute.

```html
    <form>
      <input type="button" value="click here">
    </form>
```

### **submit**

Displays the submit button. The text which should be displayed in the button is in value attribute. After clicking on the button, the HTML do the validation and if it passes, the form is submitted.

```html
    <form>
      <input type="submit" value="SUBMIT">
    </form>
```

### **reset**

Displays the reset button. The text which should be displayed in the button is in value attribute. After clicking on the button, all values from the form are deleted.

```html
    <form>
      <input type="reset" value="CANCEL">
    </form>
```

There are more types elements.

## Other HTML Attributes:

### [<script> src attribute](https://www.freecodecamp.org/news/link-javascript-to-html-with-the-src/)

### [roll attribute](https://www.freecodecamp.org/news/html-role-attribute/)

### [<a href> attribute](https://www.freecodecamp.org/news/the-a-href-attribute-explained/)

### [<a target> attribute](https://www.freecodecamp.org/news/the-a-target-html-attribute-explained/)





## 

