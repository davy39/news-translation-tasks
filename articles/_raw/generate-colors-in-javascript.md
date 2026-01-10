---
title: How to Generate Colors in JavaScript
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-03-07T22:11:32.000Z'
originalURL: https://freecodecamp.org/news/generate-colors-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/colotd--2-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "In this article, we'll build a random color generator in JavaScript. Along\
  \ the way, we will explore general topics in programming like functions and randomization.\
  \ \nWe will build a project called Change The Background Color to illustrate these\
  \ concep..."
---

In this article, we'll build a random color generator in JavaScript. Along the way, we will explore general topics in programming like functions and randomization. 

We will build a project called _Change The Background Color_ to illustrate these concepts. You can see the demo [here](http://rufai.github.io/buildingx/random_bg_color.html). 

In this tutorial, we will:

* learn how computers understand the concept of colors
* learn about the hexadecimal system and its usefulness to computers
* learn how to separate concerns in your code
* explore to the world of loops, arrays, and functions as used in JavaScript
* use this new knowledge to generate colors in hexadecimal
* introduce events in JavaScript
* click a button in our HTML code to call our functions
* change the body style _background-color_ when the button is clicked

This article should be accessible to anyone who is familiar with variables and how to create them in any programming language.  

## What We'll Cover

1. How Computers Understand Colors
2. What is the Hexadecimal System?
3. How Hexadecimal Is Used In Color Spaces
4. How to Generate Colors With Hexadecimals

## How Computers Understand Colors

Computer displays use tiny dots called pixels to display colors by mixing red, green, and blue light. 

To interpret and manipulate colors, computers use mathematical models called color spaces. By converting colors into a specific color space, computers can modify and adjust them before displaying them on the screen.   
  
There are many different types of color spaces, each with its own way of representing colors. Here are some examples:

1. RGB (Red, Green, Blue): This is the most common color space used in computer graphics, and it represents colors by mixing different amounts of red, green, and blue components.
2. CMYK (Cyan, Magenta, Yellow, Black): This is a color space used in printing, where colors are created by overlaying dots of different colors on top of each other.
3. HSL (Hue, Saturation, Lightness): This color space represents colors based on their hue (which color they are), saturation (how intense the color is), and lightness (how bright or dark the color is).
4. LAB (Lightness, A, B): This color space is used in digital imaging and represents colors based on their lightness, as well as their position on two color axes: A (from green to red) and B (from blue to yellow).
5. XYZ: This color space represents colors based on the amount of light that they reflect or emit, and is often used in color matching applications.

## What is the Hexadecimal System?

Hexadecimal (or simply "hex") is a base-16 numbering system that is commonly used in computing and digital electronics. 

In this system, numbers are represented using 16 digits: the regular decimal digits 0 through 9, plus the letters A through F which represent values 10 through 15.

``` [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]```

Hexadecimal is often used in computing because it provides a compact and easy-to-read way to represent binary numbers. Each hex digit corresponds to four binary digits, or bits, which means that two hexadecimal digits can represent a byte of data (8 bits).

### How Hexadecimal Is Used In Color Spaces

Hexadecimal is commonly used to represent colors in various color spaces, particularly in digital media. 

Each component in RGB can have a value between 0 and 255, and these values can be converted to hexadecimal notation using a [base-16 numbering system](https://www.colorhexa.com/11eb11).

In RGB hexadecimal notation, each component is represented by a two-digit hexadecimal number, which can range from 00 to FF.   
  
For example, 

| Color      | RGB | Hexadecimal  | 
| ----------- | ----------- |  ----------- |
| Black   | 0,0,0        | #000000        |
| Teal | 0,186,186 | #00BABA |
| Green | 17,235,17 | #11EB11 |
| Musterd-Yellow   | 250,194,134 | #FAC286 |
| White     | 255,255,255       | #FFFFFF       |




![Image](https://lh4.googleusercontent.com/X4ES_ppBld_5qGeavLFSlvSwyXHREWoFaO9WBIp3mV4psy-FNbZV6hXD5_eES4gdzpAXIS8uv1qdFeAyKCwPMgXaZnmlTpBBpw4X2Z8_pyP426g_RSLtipKJsid-e4lNy8D9cmgqE3EtDo3wnVnhC68)
_Hexadecimal color system illulstration_

## How to Generate Colors With Hexadecimals

Our goal in this section is to build the demo project. The demo project is a button. On clicking this button, a color is generated that changes the background of the HTML webpage.

There are the 6 steps to building the project. We'll walk through them one by one.

### 1. Represent hexadecimals using an array

```js

const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

```

The first step is to hold our characters in a structure. I have picked an array for simplicity. The way arrays work in JavaScript allows us to [select any item by providing its index](https://www.freecodecamp.org/news/the-javascript-array-handbook/).

### 2. Create a function to extract items from this array

```js
const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

function getCharacter(index) {
	return hexCharacters[index]
}
```

The function `getCharacter` will take the index and return the hexademical-character stored in that place. This helps us as we pick our colors.

### 3. Represent colors using the extracted value

A hexadecimal representation of RGB starts with `#` followed by 6 characters selected from our array. Thus, the function `getCharacters` will be called 6 times. We can employ a [for-loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) to call our function faster. 

```js

const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]


function getCharacter(index) {
	return hexCharacters[index]
}

function generateJustOneColor(){
    
	let hexColorRep = "#"

    for (let position = 0; position < 6; position++){
        hexColorRep += getCharacter( position )
    }
	
	return hexColorRep

}

console.log( generateJustOneColor() )
```

`generateJustOneColor()` generates a random hexadecimal color code represented as a string.

The function starts by declaring a variable named _hexColorRep_ and initializing it with the # character. 

Next, the function uses a for loop to generate the next six characters of the color code. The loop runs six times because each color code is represented by six hexadecimal digits.

Within the loop, the function calls another function named `getCharacter()` to generate a hexadecimal digit for each position of the color code. The `position` parameter is passed to the `getCharacter()` function to indicate which digit is being generated.

Once all six digits of the color code have been generated, the function returns the full color code as a string.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.56.42.png)
_The same result is returned every time._

The above code will to return this same result/color given the same `position` for our for-loop_._ So we need to introduce randomness. This means our selection of the characters must have the element of surprise. 

### 4. Improve our code to generate random colors

In JavaScript, **[`Math.random()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)** is one of the ways to introduce randomness. `Math.random()` gives a new result every time it is called in range `0 to 1`_._ 

While the `Math.random()` function generates a random decimal number between 0 (inclusive) and 1 (exclusive), we can manipulate this value to obtain a random integer between 0 and 15.

This is done by multiplying the random decimal number by the desired range of integers (in this case, 16) and then applying the `Math.floor()` method to round down the result to the nearest integer. This will ensure that the output is within the desired range of integers.

For example, if `Math.random()` generates the value `0.435`, multiplying it by 16 would result in `6.96`. Applying `Math.floor()` to this result would then round it down to `6`, which is a random integer within the range of 0 to 15.

`Math.floor()` performs 2 roles here: it helps us avoid a [RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_array_length) by rounding-down the extremes (the maximum number will be 15) and ensures we always return an integer. 

```js
const randomNumber = Math.floor ( Math.random() * hexCharacters.length ) 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.34.10.png)
_Math.random() gives a new result every-time it is called._

We have all the ingredients needed to generate our colour, so now we can combine them together. Each hex-colour must start with a "#" and be followed by 6 characters_._ 

```js


const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]



function getCharacter(index) {
	return hexCharacters[index]
}

function generateNewColor() {
	let hexColorRep = "#"

	for (let index = 0; index < 6; index++){
		const randomPosition = Math.floor ( Math.random() * hexCharacters.length ) 
    	hexColorRep += getCharacter( randomPosition )
	}
	
	return hexColorRep
}

console.log( generateNewColor() ) 
```

The `generateNewColor()` function is the main function of the program that generates the random hexadecimal color code. It starts by initializing a string variable named "hexColorRep" with the "#" character, as all hexadecimal color codes begin with this character.

Next, the function uses a for loop to generate six random characters for the color code. Within the loop, the function generates a random position within the range of the "hexCharacters" array using the `Math.random()` function and the length of the `hexCharacters` array. This random position is then used to obtain a random character from the `hexCharacters` array using the `getCharacter()` function. The resulting character is appended to the `hexColorRep` string variable.

Finally, the `generateNewColor()` function returns the complete hexadecimal color code represented as a string.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.55.07.png)
_The result is always a new hex-color-rep._

### 5. Create an interface to present our code

We need an interface so users can interact with our code and see the magic we have created. 

We are going to have an HTML page with a list of instructions and a button. The elements button and span are given the id attribute so it's easier to find them in our JavaScript code. You can see the HTML code [here](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html). 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/demo4.JPG)

### 6. Connect the button to the function using an event

Our goal is to change the _background-color_ style of this HTML page. 

```js
let btn = document.getElementById('b')
let bgColor = document.getElementById('s')

btn.addEventListener("click", (event) => {
		
	const newColor = generateNewColor()

	document.body.style.backgroundColor  = newColor
	bgColor.textContent = newColor 
		
})
```

This program that sets the background color of a webpage to a randomly generated hexadecimal color code when a button is clicked.

The program begins by defining two variables using the `document.getElementById()` method. The `btn` variable represents the button element on the webpage with the ID `b`, while the `bgColor` variable represents a text element on the webpage with the ID `s`.

Next, the program attaches an event listener to the `btn` element using the `addEventListener()` method. This listener listens for the `click` event on the button. When triggered, it executes a function that generates a new random color code using the `generateNewColor()` function.

The resulting color code is then assigned to the background color of the webpage using the `style.backgroundColor` property of the `document.body` element. This causes the entire webpage to be updated with the new color.

Finally, the color code is also displayed in the `bgColor` element on the webpage using the textContent property.

You can see the full code [here](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html). 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/ezgif.com-gif-maker-1.gif)
_FInal product_

## Summary

In this article, we have shown how to generate random colours in JavaScript. We used the methods _random_ and _floor_ from the [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) class and showed basic usage of a for-loop.  
  
In the [demo project](http://rufai.github.io/buildingx/random_bg_color.html), the generated colour was passed as background to an HTML page. This is why on clicking the button, a new colour gets generated, and updates the _background-color_ style of the page. Check out the full [code here](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html).   
  
If you want to see more of teachings, check out [Xutini](https://www.youtube.com/@xutini) - the fun way to learn digital skills.  
  

