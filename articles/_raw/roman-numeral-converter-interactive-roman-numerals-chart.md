---
title: How to Build a Roman Numeral Converter and an Interactive Roman Numerals Chart
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-04T07:16:00.000Z'
originalURL: https://freecodecamp.org/news/roman-numeral-converter-interactive-roman-numerals-chart
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99dd740569d1a4ca2223.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: null
seo_desc: 'By Alexander Arobelidze

  The Roman numerals are no longer an essential part of our daily lives. But we do
  use them when designing monuments, clocks, and even for sporting events.

  What are the Roman Numerals?

  Roman numerals originated in ancient Rome a...'
---

By Alexander Arobelidze

The Roman numerals are no longer an essential part of our daily lives. But we do use them when designing monuments, clocks, and even for sporting events.

## What are the Roman Numerals?

Roman numerals originated in ancient Rome and remained the common way of writing numbers throughout Europe for many centuries. Their use long outlived the Roman Empire itself. They were gradually replaced by the Hindu-Arabic system of numeration that we use today – the numbers zero through nine.

Roman numerals are represented by combinations of letters of the Latin alphabet, that serve as digits in this system. But unlike decimal base, with symbols **0 through 9**, the the Roman system employs seven capitalized Latin letters **I, V, X, L, C, D, M**.

Originally, there was no single letter designation for zero. Instead, they used the Latin word **Nulla**, which means "none". 

## How do Roman Numerals work?

The Hindu-Arabic representation of these letters is as follows: **I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 and M = 1000**.

Other numbers are formed by combining these letters per certain rules: A symbol placed **after** another of equal or greater value, adds its value. 

For example,   **VI = V + I = 5 + 1 = 6** or **LX = L + X = 50 + 10 = 60**. The notations VI and LX are read as "one more than five" and "ten more than fifty". 

A symbol placed **before** one of greater values subtracts its value. For example, **IX = X - I = 10 - 1 = 9,** and **XC = C - X = 100 - 10 = 90**. 

The notations IX and XC are read as "one less than ten" and "ten less than a hundred." 

Numbers greater than 1,000 are formed by placing a dash over the symbol. Thus **V̅ = 5,000**, **X̅ = 10,000**, **L̅ = 50,000**, **C̅ = 100,000**, **D̅ = 500,000** and **M̅ = 1,000,000**. 

The so called "standard" form disallows using the same symbol more than three times in a row. But occasionally, exceptions can be seen. For example, IIII for number 4, VIIII for number 9, and LXXXX for 90.

## An Interactive Chart of Roman Numerals and Their Combinations

Hover over each symbol to reveal its Hindu-Arabic equivalent:

<!-- HTML utilizes Flexbox. Container is composed of buttons as basic 
elements. Buttons are wired to functions that fire on mouseover and mouseout
events. Current button ids, arabic and roman numbers serve as arguments for event listener functions. -->
<div class='flex-container'>
    
	<div class='row1'>
    	<button class='item' id='1' onmouseover='handleMouseOver("1")' onmouseout='handleMouseOut("1", "I")'>I</button>
        <button class='item' id='2' onmouseover='handleMouseOver("2")' onmouseout='handleMouseOut("2", "II")'>II</button>
        <button class='item' id='3' onmouseover='handleMouseOver("3")' onmouseout='handleMouseOut("3", "III")'>III</button>
        <button class='item' id='4' onmouseover='handleMouseOver("4")' onmouseout='handleMouseOut("4", "IV")'>IV</button>
        <button class='item' id='5' onmouseover='handleMouseOver("5")' onmouseout='handleMouseOut("5", "V")'>V</button>
        <button class='item' id='6' onmouseover='handleMouseOver("6")' onmouseout='handleMouseOut("6", "VI")'>VI</button>
        <button class='item' id='7' onmouseover='handleMouseOver("7")' onmouseout='handleMouseOut("7", "VII")'>VII</button>
        <button class='item' id='8' onmouseover='handleMouseOver("8")' onmouseout='handleMouseOut("8", "VIII")'>VIII</button>
        <button class='item' id='9' onmouseover='handleMouseOver("9")' onmouseout='handleMouseOut("9", "IX")'>IX</button>
    </div>
    <div class='row2'>
    	<button class='item' id='10' onmouseover='handleMouseOver("10")' onmouseout='handleMouseOut("10", "X")'>X</button>
        <button class='item' id='20' onmouseover='handleMouseOver("20")' onmouseout='handleMouseOut("20", "XX")'>XX</button>
        <button class='item' id='30' onmouseover='handleMouseOver("30")' onmouseout='handleMouseOut("30", "XXX")'>XXX</button>
        <button class='item' id='40' onmouseover='handleMouseOver("40")' onmouseout='handleMouseOut("40", "XL")'>XL</button>
        <button class='item' id='50' onmouseover='handleMouseOver("50")' onmouseout='handleMouseOut("50", "L")'>L</button>
        <button class='item' id='60' onmouseover='handleMouseOver("60")' onmouseout='handleMouseOut("60", "LX")'>LX</button>
        <button class='item' id='70' onmouseover='handleMouseOver("70")' onmouseout='handleMouseOut("70", "LXX")'>LXX</button>
        <button class='item' id='80' onmouseover='handleMouseOver("80")' onmouseout='handleMouseOut("80", "LXXX")'>LXXX</button>
        <button class='item' id='90' onmouseover='handleMouseOver("90")' onmouseout='handleMouseOut("90", "XC")'>XC</button>
    </div>
    <div class='row3'>
    	<button class='item' id='100' onmouseover='handleMouseOver("100")' onmouseout='handleMouseOut("100", "C")'>C</button>
        <button class='item' id='200' onmouseover='handleMouseOver("200")' onmouseout='handleMouseOut("200", "CC")'>CC</button>
        <button class='item' id='300' onmouseover='handleMouseOver("300")' onmouseout='handleMouseOut("300", "CCC")'>CCC</button>
        <button class='item' id='400' onmouseover='handleMouseOver("400")' onmouseout='handleMouseOut("400", "CD")'>CD</button>
        <button class='item' id='500' onmouseover='handleMouseOver("500")' onmouseout='handleMouseOut("500", "D")'>D</button>
        <button class='item' id='600' onmouseover='handleMouseOver("600")' onmouseout='handleMouseOut("600", "DC")'>DC</button>
        <button class='item' id='700' onmouseover='handleMouseOver("700")' onmouseout='handleMouseOut("700", "DCC")'>DCC</button>
        <button class='item' id='800' onmouseover='handleMouseOver("800")' onmouseout='handleMouseOut("800", "DCCC")'>DCCC</button>
        <button class='item' id='900' onmouseover='handleMouseOver("900")' onmouseout='handleMouseOut("900", "CM")'>CM</button>
    </div>
    <div class='row4'>
    	<button class='item special' id='1000' onmouseover='handleMouseOver("1000")' onmouseout='handleMouseOut("1000", "M")'>M</button>
        <button class='item special' id='5000' onmouseover='handleMouseOver("5000")' onmouseout='handleMouseOut("5000", "V&#773;")'>V&#773;</button>
        <button class='item special' id='10000' onmouseover='handleMouseOver("10000")' onmouseout='handleMouseOut("10000", "X&#773;")'>X&#773;</button>
        <button class='item special' id='50000' onmouseover='handleMouseOver("50000")' onmouseout='handleMouseOut("50000", "L&#773;")'>L&#773;</button>
        <button class='item special' id='100000' onmouseover='handleMouseOver("100000")' onmouseout='handleMouseOut("100000", "C&#773;")'>C&#773;</button>
        <button class='item special' id='500000' onmouseover='handleMouseOver("500000")' onmouseout='handleMouseOut("500000", "D&#773;")'>D&#773;</button>
        <button class='item special' id='1000000' onmouseover='handleMouseOver("1000000")' onmouseout='handleMouseOut("1000000", "M&#773;")'>M&#773;</button>
    </div>
</div>


<!-- CSS  -->

<style>
    .flex-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;    
    margin: 0 auto; 
    align-items: center;
    justify-content: center;   
   }
    /* Mobile phones */
@media screen and (max-width: 767px){
    .flex-container {
       transform: scale(0.6);
    }
}
/* Tablets and iPads */
@media screen and (min-width: 768px) and (max-width: 1023px){
    .flex-container {
        transform: scale(0.8);
    }
}
    .row1, .row2, .row3 {
    display: flex;
    flex-direction: row;    
    align-items: center;
    justify-content: space-between;    
    }
    .row4 {
    display: flex;
    flex-direction: row nowrap;  
    align-items: center;
    justify-content: space-evenly;     
    }
    .item {
    margin: 0.2rem 0.2rem;
    width: 9rem;
    height: 9rem;  
    background-color: #3F51B5; 
    color: white;
    font-weight: 600;  
    border-radius: 0.2rem;
    box-shadow: 0 0 1rem 0.25rem; 
    transition-duration: 0.2s;
   }
    .special {
    margin: 0.2rem 0.3rem;    
    width: 11.5rem;
    height: 9rem;    
    }

</style>

<!-- JavaScript consists of two functions. One is called on mouseover event, another on mouseout event. The arguments they take determine which node is currently active and change its appearance/content accordingly. -->
<script>
 
function handleMouseOver(arabic) {
    let currentButton = document.getElementById(arabic)
 	currentButton.style.transform = 'scale(1.3)'
    currentButton.style.zIndex = '9'
    currentButton.textContent = arabic 
} 
 
function handleMouseOut(id, roman) {
    let currentButton = document.getElementById(id) 
    currentButton.style.transform = 'scale(1)'
    currentButton.style.zIndex = '0'
    currentButton.textContent = roman 
 }   
</script>

I wrote the code for this interactive Roman numeral chart to embed here on freeCodeCamp News.

Given the fact that the HTML embed feature is not a full scale code editor, the given code is not structured and presented as separate HTML, CSS, and JavaScript files. Rather it is written as a single HTML file with `<style>` and `<script>` elements added for styling and functionality.

Here is [the full code repository for my interactive Roman Numeral Chart](https://github.com/sandroarobeli/RomanNumeralChart.git). 

## Roman Numeral Converter

Enter a non negative integer between 0 and 5,000. Then click Convert to reveal a Roman numeral equivalent. 

<!-- HTML elements 
UI consists of an input element of type 'number' that ensures only numeric characters and decimal point can be entered. Handling of decimal points is 
managed through javascript logic below. Also, a 'convert' button element clicking on which triggers conversion of arabic numerals into roman numerals and another button element that displays the result of conversion. In case one wanders why a button element displays the result, the answer has to do with manageability of styling given quite limited functionality of the platform.  
-->

<div  
    id='converter' 
    style='box-sizing: border-box; 
           width: 90%; 
           margin: 0 auto;'>
   <label 
         for='arabicNumeral' 
         style='display:block; 
                text-align: center; 
                font-weight: 600; 
                color: #3F51B5;'>Arabic to Roman
      <input 
            type='number' 
            name='arabicNumeral'  
            id='arabicNumeral' 
            min='0' max='5000' step='1' 
            placeholder='Enter an integer between 0 and 5000' 
            style='padding: 10px; 
                   margin: 0 auto; 
                   border: 2px solid #eee; 
                   box-shadow:0 0 15px 4px rgba(0,0,0,0.06); 
                   border-radius:10px; 
                   width:100%; 
                   font-size: inherit;' /> 				
   </label> <hr/>
   <button 
          type='button' 
          id='convert'
          onclick='convertToRoman()'           
          style='padding:10px; 
                 border:none;
                 margin: 0 auto;                                                                background-color:#3F51B5;
                 color:#fff;
                 font-weight:600;
                 border-radius:5px;
                 width:100%;'>Convert
   </button>
   <button 
          type='button' 
          id='display' 
          style='padding:10px;
                 border:none;
                 margin: 0 auto;                                                                background-color:#fff;
                 color:#3F51B5;
                 font-weight:600;
                 font-size: 3rem;       
                 border-radius:5px;
                 width:100%; '>
   </button>
 </div>   
 
<script>
 
  /* The following block is structured the way it is primarily due to limitations of the platform. The converter currently covers numbers between 0 and 5000, however it can be altered to cover negative numbers as well as numbers beyond 5000. The chosen range more than covers the purpose of the converter as being an interactive tool in the article. 
  */   	
   
 
 const inputField = document.querySelector('input');
 const outputField = document.getElementById('display');
 const convertButton = document.getElementById('convert');
 

  
 
function convertToRoman() {
 
 let arabic = document.getElementById('arabicNumeral').value;
 let roman = '';
    
 const arabicArray = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
 const romanArray = ['V&#773;', 'MV&#773;','M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

  
if (/^(0|[1-9]\d*)$/.test(arabic)) {
  if (arabic == 0) {  
    outputField.innerHTML = 'Nulla'
  } else if (arabic != 0) {
   for (let i = 0; i < arabicArray.length; i++) {
    while (arabicArray[i] <= arabic) {
      roman += romanArray[i]
      arabic -= arabicArray[i]
    }
 }
   outputField.innerHTML = roman
  }
} else {
   outputField.innerHTML = 'Please enter non negative integers only. No decimal points.'
}
 
 }     
 
</script>

There is no programmatic limitation to the number 5,000 or beyond. The algorithm that governs the conversion would work all the same. 

The space required to display Roman numeral equivalents of large numbers grows larger and larger without much added benefit of revealing something new. 

The code itself consists of an HTML part describing the content with inline styles for ease of interaction and added JavaScript for functionality.

The is an input element of the type "number" to limit input data to numeric values and two buttons. The "Convert" button is wired to the function that performs the conversion, and the "Display" button outputs the Roman number equivalent. 

Why output through a button element? Styling worked well when applied to both buttons together. And considering the limited functionality of the embed, it seemed like a time saver. 

For clarity, these elements are assigned to variables:

```js
const inputField = document.querySelector('input'); // input element
const convertButton = document.getElementById('convert'); // convert button
const outputField = document.getElementById('display'); // output element
```

Function `convertToRoman()` contains the logic and renders the result:

```js
function convertToRoman() {
  let arabic = document.getElementById('arabicNumeral').value; // input value
  let roman = '';  // variable that will hold the result
}
```

The numerical value from input element is saved in a variable called "**arabic**" for further testing. The variable named "**roman**" will hold the string representing Roman equivalent of Arabic input.

Next, there are two arrays of equal lengths, one holding Arabic numerals and one holding their Roman counterparts. Both are in descending order to simplify subtraction:

```js
// descending order simplifies subtraction while looping
const arabicArray = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
const romanArray = ['V&#773;', 'MV&#773;','M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] 
```

Unicode tables help with forming symbols greater than 1,000. 

Finally, here is the logic that test the inputted number and converts it.

```js
if (/^(0|[1-9]\d*)$/.test(arabic)) {
  // Regular expression tests
  if (arabic == 0) {
    // for decimal points and negative
    outputField.innerHTML = "Nulla"; // signs
  } else if (arabic != 0) {
    for (let i = 0; i < arabicArray.length; i++) {
      while (arabicArray[i] <= arabic) {
        roman += romanArray[i];
        arabic -= arabicArray[i];
      }
    }
    outputField.innerHTML = roman;
  }
} else {
  outputField.innerHTML =
    "Please enter non negative integers only. No decimal points.";
}
```

The first test checks for decimal points and negative signs. If found, the message asks to "enter non-negative integers only."

The next test checks whether the number entered equals zero. In such a case, the string "Nulla" is displayed. 

Otherwise, the loops keep concatenating Roman strings while subtracting Arabic numbers until the latter satisfies the condition for the while loop. Then it displays the Roman equivalent of the user input.

Just like with the interactive chart, the code for the Roman Numeral Converter is all set for you to copy it and embed it into any article. Here's [the full code repository](https://github.com/sandroarobeli/RomanNumeralConverter.git).

