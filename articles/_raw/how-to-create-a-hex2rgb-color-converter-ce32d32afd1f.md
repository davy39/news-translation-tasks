---
title: 'Diving into JavaScript: How to Create a Hex2RGB Color Converter'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T22:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-hex2rgb-color-converter-ce32d32afd1f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca62e740569d1a4ca6e7b.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vaibhav Kandwal

  Update (23/07/2019): I have corrected a few grammatical errors and changed app.js
  code a bit by removing the checkBG function.

  In this article, we’ll be creating a web-app that converts color codes between Hexadecimal
  form and RGB ...'
---

By Vaibhav Kandwal

_Update (23/07/2019): I have corrected a few grammatical errors and changed app.js code a bit by removing the checkBG function._

In this article, we’ll be creating a web-app that converts color codes between Hexadecimal form and RGB form.

You can find a [demo here](https://boxdox.github.io/hex2rgb/?source=post_page---------------------------) and the [source code here](https://github.com/boxdox/hex2rgb?source=post_page---------------------------).

## Project Structure:

The project structure is pretty simple.

1. `index.html` : Contains the structure of the app.
2. `style.css` : Styles the page.
3. `app.js` : Contains all the magic code.

## Idea:

Here’s the list of things I wanted this app to perform:

1. Whenever something is typed in a text-field for hex, the app should check if the color is valid. If it is, convert it to RGB, set it as the background and then put the RGB value in the RGB text-field and vice versa.
2. If a short hex color code is typed into the text-field, expand it when the text-field loses focus (user clicks outside of text area).
3. Automatically prepend ‘#’ symbol to the hex input.

## Let’s Begin!

## index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Hex to RGB Converter</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <div class="head">
    HEX &lt;--&gt; RGB
  </div>
  <div id="content">
    <input type="text" id="hex" placeholder="hex">
    <img id="hexError" class="hidden" src="data:image/svg+xml;utf8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzYgNTEyIj48cGF0aCBkPSJNNTY5LjUxNyA0NDAuMDEzQzU4Ny45NzUgNDcyLjAwNyA1NjQuODA2IDUxMiA1MjcuOTQgNTEySDQ4LjA1NGMtMzYuOTM3IDAtNTkuOTk5LTQwLjA1NS00MS41NzctNzEuOTg3TDI0Ni40MjMgMjMuOTg1YzE4LjQ2Ny0zMi4wMDkgNjQuNzItMzEuOTUxIDgzLjE1NCAwbDIzOS45NCA0MTYuMDI4ek0yODggMzU0Yy0yNS40MDUgMC00NiAyMC41OTUtNDYgNDZzMjAuNTk1IDQ2IDQ2IDQ2IDQ2LTIwLjU5NSA0Ni00Ni0yMC41OTUtNDYtNDYtNDZ6bS00My42NzMtMTY1LjM0Nmw3LjQxOCAxMzZjLjM0NyA2LjM2NCA1LjYwOSAxMS4zNDYgMTEuOTgyIDExLjM0Nmg0OC41NDZjNi4zNzMgMCAxMS42MzUtNC45ODIgMTEuOTgyLTExLjM0Nmw3LjQxOC0xMzZjLjM3NS02Ljg3NC01LjA5OC0xMi42NTQtMTEuOTgyLTEyLjY1NGgtNjMuMzgzYy02Ljg4NCAwLTEyLjM1NiA1Ljc4LTExLjk4MSAxMi42NTR6Ii8+PC9zdmc+" />
    </br>
    <input type="text" id="rgb" placeholder="rgb">
    <img id="rgbError" class="hidden" src="data:image/svg+xml;utf8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzYgNTEyIj48cGF0aCBkPSJNNTY5LjUxNyA0NDAuMDEzQzU4Ny45NzUgNDcyLjAwNyA1NjQuODA2IDUxMiA1MjcuOTQgNTEySDQ4LjA1NGMtMzYuOTM3IDAtNTkuOTk5LTQwLjA1NS00MS41NzctNzEuOTg3TDI0Ni40MjMgMjMuOTg1YzE4LjQ2Ny0zMi4wMDkgNjQuNzItMzEuOTUxIDgzLjE1NCAwbDIzOS45NCA0MTYuMDI4ek0yODggMzU0Yy0yNS40MDUgMC00NiAyMC41OTUtNDYgNDZzMjAuNTk1IDQ2IDQ2IDQ2IDQ2LTIwLjU5NSA0Ni00Ni0yMC41OTUtNDYtNDYtNDZ6bS00My42NzMtMTY1LjM0Nmw3LjQxOCAxMzZjLjM0NyA2LjM2NCA1LjYwOSAxMS4zNDYgMTEuOTgyIDExLjM0Nmg0OC41NDZjNi4zNzMgMCAxMS42MzUtNC45ODIgMTEuOTgyLTExLjM0Nmw3LjQxOC0xMzZjLjM3NS02Ljg3NC01LjA5OC0xMi42NTQtMTEuOTgyLTEyLjY1NGgtNjMuMzgzYy02Ljg4NCAwLTEyLjM1NiA1Ljc4LTExLjk4MSAxMi42NTR6Ii8+PC9zdmc+" />
  </div>
  <script src="app.js"></script>
</body>

</html>
```

We created two text fields with id of ‘hex’ and ‘rgb’ respectively. Next to each input is an SVG icon for error, which has a class of hidden, by default.

## style.css

```css
:root {
     --color: rgba(255,255,255,0.9);
     --tweet: white;
}
 * {
     margin: 0;
     padding: 0;
     box-sizing: border-box;
}
 ::placeholder {
     color: var(--color)!important;
}
 body {
     padding: 50px;
     width: 100vw;
     height: 100vh;
     display: flex;
     align-items: center;
     justify-content: center;
     background-color: #28a745;
     font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;
}
 .head {
     position: absolute;
     top: 30px;
     text-align: center;
     color: var(--tweet);
     font-size: 3rem;
     border-bottom: 2px solid var(--tweet);
}
 #content {
     display: block;
}
 input {
     color: var(--color)!important;
     margin: 1rem 0;
     width: 400px;
     border: none;
     border-bottom: 1px solid var(--color);
     font-size: 2.5rem;
     background-color: transparent;
}
 input:focus {
     outline: none;
}
 img {
     width: 24px;
}
 .hidden {
     visibility: hidden;
     opacity: 0.8;
}
 .dark {
     --color: rgba(0,0,0,0.75);
     --tweet: rgba(0,0,0,0.95);
}
 @media only screen and (max-width: 560px){
     #content input {
         margin: 0.75rem 0;
         width: 90%;
         font-size: 1.875rem;
    }
     #content img {
         width: 16px;
    }
     .head {
         font-size: 2rem;
    }
}

```

Here’s a basic layout to make the markup look a bit better. We have defined two classes here, `.hidden` and `.dark`. `.hidden` is used to hide/show the error SVG icon and `.dark` is to change the text color based on the background color. By default, I have set the text to a dark color (for bright backgrounds).

## app.js

Here’s the magic part. I will be breaking down the code into chunks:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_vkFx7EZWK1gr8yecEb2UpQ.png)

First, we have defined variables that target the inputs with id ‘hex’ and ‘rgb’. Next up, we have functions to check if input Hex/RGB is valid or not. They use a basic regex setup and return a boolean. If you get intimidated by them, I recommend you to try out this [RegexTutorial](http://regextutorials.com/?source=post_page---------------------------).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_US53im4jHtPwS30i_VpSQA.png)

Here, We wrote a parse function called `modifyHex` which checks if the input hex is 4 characters long; that is, contains ‘#’ and is shorthand (for example, #333) and replaces the ‘#’ with an empty character. Then it checks if the length now is 3 and expands it to 6 characters long (for example, #123 = #112233).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_OkqZufTfvTtTH4wdXm44nw--2-.png)

We have defined two functions that convert hex to rgb and vice versa. Here’s a step-by-step breakdown for `hexToRgb`(This process is written in expanded form for better understanding):

1. Define an empty array to store the result.
2. Replace the ‘#’ symbol, if it exists, and if the length is not equal to 6 (that is, the shorthand version), call the above `modifyHex` function and expand it.
3. In a very basic way, hex to rgb works by converting the hex code (in base 16) to rgb code (in base 10). Every two characters in the hex code represent a value in the rgb color code. For Example in #aabbcc, red is (aa to base 10), green is (bb to base 10) and blue is (cc to base 10). So in the function, we are slicing the hex value, converting it to base 10 using `parseInt`, and then storing it in the defined array.
4. Finally, we are returning the output string by joining the above array.

For the `rgbToHex` function (this is written with shorter logic):

1. We are directly using a regex to extract only the number values — that is, rgb(123,21,24) will return 123,21,24.
2. Next, we are using a map function to return a new array, which converts the number to base 16, then pads the value.

The regex we used above returns data of type ‘string’. To convert it to Base 16, we have to use the `toString()`  method, with a parameter of ‘16’.

Now, `toString()` method is applicable to only numeric data types, so we use `parseInt` to first convert every element of the array to a number, then use `toString(16)` to convert it to hexadecimal form and then finally add padding to make it exactly 2 characters long. Padding is necessary, if you have something like ‘14’, which you want to convert to hexadecimal, it will return ‘e’. But hex color code needs 2 characters for each part, so padding is required, which makes it ‘0e’.

_Note:_ `_padStart_` _is an ES8 feature, which might not be supported in every browser. To keep this tutorial simple, I have not transpiled it to ES5._

3. Finally, we are returning the resulting array by joining it and converting it to uppercase.  


![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_GS58ex_1iIswypXdZjaoHA.png)

`errorMark()` function is used to show or hide the error SVG icon. It simply passes the contents of the input ( `hex.value` and `rgb.value` ) through their respective check functions and uses the returned boolean to add/remove the `.hidden` class.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_05piBJK1b3tsaEdxkjK8JA.png)

Now we are defining a function which takes the background color and then determines if it is dark or bright (I got this code from StackOverflow). It multiplies the individual color values with some calculated numbers and returns ‘black’ or ‘white’. I then use another function to change the text color by adding/removing the `.dark` class.

## Adding Event Listeners:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_wAKHCvq61Bw83rkTNqZcZw.png)

Finally, we are connecting all functions through adding Event Listeners.

First, we are adding a `keyup` event to the `hex` input. This event is triggered each time a key is released. Here's the process breakdown:

1. Check if the input code is valid and expand it if it’s shorthand.
2. Sett the body’s background color to the input value.
3. Check the color contrast and change the text color accordingly.
4. Call the convert function and place the converted color into the RGB input field.

The other event listener we used is `blur` . It is triggered each time the input loses ‘focus’, or in layman terms, each time you click/tap outside of input element, `blur` is triggered. So it’s good to modify the input hex!

So, we check if the hex color is valid or not, then we expand it if it is short, and finally we add a ‘#’ if it doesn’t exist. Note that we are checking if index 0 and 1 contain ‘#’. This is done so that the function doesn’t prepend ‘#’ twice.  


![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_TZODzwqCrGnQCARdrzarBw.png)

The same `keyup` event listener is added to the RGB input and it too follows the same series of steps as the hex event listener.

Lastly, we have added an event listener `keyup` to the entire document, that is, it will be triggered for any of the two input elements. In it, we are calling the `errorMark` function, which adds the error icon, in case there’s an error, or removes it if everything is valid.

Here’s the final code for `app.js` :

```js
const hex = document.getElementById("hex");
const rgb = document.getElementById("rgb");

// Check Functions
function checkHex(hex) {
  const hexRegex = /^[#]*([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/i
  if (hexRegex.test(hex)) {
    return true;
  }
}

function checkRgb(rgb) {
  const rgbRegex = /([R][G][B][A]?[(]\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\s*,\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\s*,\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\s*,\s*((0\.[0-9]{1})|(1\.0)|(1)))?[)])/i
  if (rgbRegex.test(rgb)) {
    return true
  }
}
// Parse Function
function modifyHex(hex) {
  if (hex.length == 4) {
    hex = hex.replace('#', '');
  }
  if (hex.length == 3) {
    hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
  }
  return hex;
}

// Converting Functions
function hexToRgb(hex) {
  let x = [];
  hex = hex.replace('#', '')
  if (hex.length != 6) {
    hex = modifyHex(hex)
  }
  x.push(parseInt(hex.slice(0, 2), 16))
  x.push(parseInt(hex.slice(2, 4), 16))
  x.push(parseInt(hex.slice(4, 6), 16))
  return "rgb(" + x.toString() + ")"
}

function rgbToHex(rgb) {
  let y = rgb.match(/\d+/g).map(function(x) {
    return parseInt(x).toString(16).padStart(2, '0')
  });
  return y.join('').toUpperCase()
}

// Helper Functions
function addPound(x) {
  return '#' + x;
}

// Function to add cross mark on error values
function errorMark() {
  if (checkHex(hex.value)) {
    document.getElementById('hexError').classList.add('hidden');
  } else {
    document.getElementById('hexError').classList.remove('hidden');
  }
  if (checkRgb(rgb.value)) {
    document.getElementById('rgbError').classList.add('hidden');
  } else {
    document.getElementById('rgbError').classList.remove('hidden');
  }
}

// Finding Contrast Ratio to change text color. Thanks https://stackoverflow.com/a/11868398/10796932
function getContrastYIQ(hexcolor) {
  if (checkHex(hexcolor)) {
    hexcolor = hexcolor.replace("#", '')
  } else {
    hexcolor = rgbToHex(hexcolor)
  }
  var r = parseInt(hexcolor.substr(0, 2), 16);
  var g = parseInt(hexcolor.substr(2, 2), 16);
  var b = parseInt(hexcolor.substr(4, 2), 16);
  var yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000;
  return (yiq >= 128) ? document.body.classList.add('dark') : document.body.classList.remove('dark')
}

// Adding Event Listeners
hex.addEventListener('keyup', function() {
  let color = hex.value
  if (checkHex(color)) {
    color = modifyHex(color);
    document.body.style.backgroundColor = addPound(color);
    getContrastYIQ(color)
    rgb.value = hexToRgb(color);
  }
})
hex.addEventListener('blur', function() {
  if (checkHex(hex.value)) {
    hex.value = modifyHex(hex.value)
    if (hex.value[1] != '#') {
      if (hex.value[0] != '#') {
        hex.value = addPound(hex.value);
      }
    }
  }
})
rgb.addEventListener('keyup', function() {
  let color = rgb.value
  if (checkRgb(color)) {
    hex.value = color = addPound(rgbToHex(color))
    document.body.style.backgroundColor = color;
    getContrastYIQ(color)
  }
})
document.addEventListener('keyup', function() {
  errorMark();
})
```

# Conclusion

There you have it! I know the code is not perfect and can be refactored, but hey, this is just the beginning. If you want to improve this code, you can go ahead and open a PR on my [github repo](https://github.com/boxdox/hex2rgb?source=post_page---------------------------).

Happy Coding!

