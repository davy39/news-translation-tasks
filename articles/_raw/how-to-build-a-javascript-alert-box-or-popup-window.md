---
title: How to Build a JavaScript Alert Box or Popup Window
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T19:20:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-javascript-alert-box-or-popup-window
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8d740569d1a4ca385a.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Popup boxes (or dialog boxes) are modal windows used to notify or warn
  the user, or to get input from the user.

  Popup boxes prevent the user from accessing other aspects of a program until the
  popup is closed, so they should not be overused.

  There ar...'
---

Popup boxes (or dialog boxes) are modal windows used to notify or warn the user, or to get input from the user.

Popup boxes prevent the user from accessing other aspects of a program until the popup is closed, so they should not be overused.

There are three different kinds of popup methods used in JavaScript: [window.alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), [window.confirm()](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) and [window.prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt).

### **Alert**

The [alert method](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) displays messages that don’t require the user to enter a response. Once this function is called, an alert dialog box will appear with the specified (optional) message. Users will be required to confirm the message before the alert goes away.

### **Example:**

`window.alert("Welcome to our website");`

![MDN Alert Example](https://mdn.mozillademos.org/files/130/AlertHelloWorld.png)

### **Confirm**

The [confirm method](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) is similar to `window.alert()`, but also displays a cancel button in the popup. The buttons return boolean values: true for OK and false for Cancel.

### **Example:**

```javascript
var result = window.confirm('Are you sure?');
if (result === true) {
    window.alert('Okay, if you're sure.');
} else { 
    window.alert('You seem uncertain.');
}
```

![MDN Confirm Example](https://mdn.mozillademos.org/files/7163/firefoxcomfirmdialog_zpsf00ec381.png)

### **Prompt**

The [prompt method](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) is typically used to get text input from the user. This function can take two arguments, both of which are optional: a message to display to the user and a default value to display in the text field.

### **Example:**

`var age = prompt('How old are you?', '100');`

![MDN Prompt Example](https://mdn.mozillademos.org/files/11303/prompt.png)

### **Other Design Options:**

If you are unhappy with the default JavaScript popups, you can substitute in various UI libraries. For example, SweetAlert provides a nice replacement for standard JavaScript modals. You can include it in your HTML via a CDN (content delivery network) and begin use.

```html
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
```

The syntax is as such: `swal(title, subtitle, messageType)`

```javascript
swal("Oops!", "Something went wrong on the page!", "error");
```

The above code will produce the following popup:

![SweetAlert Example](https://ludu-assets.s3.amazonaws.com/lesson-content/rWqOoQXgDrSVSMrAKiZ9)

SweetAlert is by no means the only substitute for standard modals, but it is clean and easy to implement.

#### **More Information:**

* [MDN window.alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)
* [MDN window.confirm()](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm)
* [MDN window.prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)

