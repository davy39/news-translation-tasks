---
title: How to Use JavaScript for Data Analysis – A Beginner's Guide
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-17T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/basics-of-data-analysis-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-burak-the-weekender-186461.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Data analysis involves taking data you have and extracting useful information
  from them. During the process, you need to clean the data, present them in a useful
  way, and draw conclusions that can help companies make important decisions.

  Data analysi...'
---

Data analysis involves taking data you have and extracting useful information from them. During the process, you need to clean the data, present them in a useful way, and draw conclusions that can help companies make important decisions.

Data analysis is commonly done with languages like Python and R. Very few people know that you can also perform Data Analysis with JavaScript, and it is pretty easy, too.

This article focuses on the most basic data analysis functions that you can do in JavaScript. Let's dive in.

## How to Find the Average with JavaScript

When you want to find the average of a group of numbers, you add them all together and divide by the number of items you have.

For example, if you have a group of numbers 2, 5, 7, 9, and 12, you add them all together and divide that result by 5 (there are five numbers in your group). So the average is 2+5+7+9+12 = 35, and 35/5 = 7. 

The average, in other words, is the result obtained by dividing the sum of all the values in the set by the length or count of the set.

Take this sample set of random numbers between 1 and 1000 as an example:

```javascript
const data = [
    943, 504, 733, 122, 868, 994, 553, 376, 450, 212,
    295, 859, 29, 820, 148, 589, 621, 870, 941, 909,
    725, 160, 198, 568, 409, 625, 207, 338, 162, 439,
    894, 937, 929, 648, 91, 235, 550, 851, 626, 926,
    190, 770, 33, 274, 79, 355, 768, 504, 415, 232,
    33, 327, 100, 1000, 775, 803, 587, 676, 17, 952,
    931, 838, 447, 358, 282, 606, 877, 185, 514, 263,
    887, 725, 270, 716, 762, 633, 900, 948, 786, 28,
    950, 858, 587, 804, 127, 803, 111, 609, 606, 461,
    947, 868, 43, 432, 113, 607, 852, 698, 984, 575
];
```

To calculate the average of this set in JavaScript, you can use the `array.reduce` method (to get the sum of the array) along with the `array.length` method (to get the count of values in the set) to find the average like this:

```javascript
const average = data.reduce((a, b) => a + b) / data.length; // Returns 552.35
```

You could also find the average using a third party library like [math.js](https://www.npmjs.com/package/mathjs), like this:

```javascript
import { mean } from 'mathjs';

const average = mean(...data); // Returns 552.35
```

You can also find the average using either a `for` or a `forEach` loop.

```javascript
let sum = 0;

for (let datum of data) sum += datum;

const average = sum / data.length; // Returns 552.35
```

```javascript
let sum = 0;

data.forEach((datum) => sum += datum);

const average = sum / data.length; // Returns 552.35
```

## How to Find the Maximum and Minimum with JavaScript

When you're working with functions, the maximum and minimum are the largest and smallest values of that function. You can calculate these for a specific range, or for the entire set of values.

Using the same array from above, we can get the maximum value using the `max` method of the built-in `Math` module.

```javascript
const max = Math.max(...data); // Returns 1000
```

You can also get the minimum value using the `min` method.

```javascript
const min = Math.min(...data); // Returns 17
```

Alternatively, you can also use a third partly library like math.js to find the maximum and minimum values, like this:

```javascript
import { min, max } from 'mathjs';

const maxValue = max(...data); // Returns 1000
const minValue = min(...data); // Returns 17
```

You can also decide to find the maximum and minimum values by yourself. You can do this using the `array.sort` method and picking the first and last items in the list as your minimum and maximum values, respectively. Or you can also do this by using a loop and keeping track of the maximum and minimum values.

```javascript
const sortedData = data.sort((a, b) => a - b);

const min = sortedData[0]; // Returns 17
const max = sortedData[sortedData.length - 1]; // Returns 1000
```

```javascript
let min, max;

for (let datum of data) {
    if (!min || !max) {
        min = datum;
        max = datum;
    } else if (datum < min) min = datum;
    else if (datum > max) max = datum;
}
```

## How to Find the Sum with JavaScript

The sum, or total, is the result of the addition of a sequence of numbers. In the section explaining average above, we saw a way to get the sum of a sequence using `array.reduce`.

```javascript
const sum = data.reduce((a, b) => a + b); // Returns 55235
```

Another very easy way would be to use the `sum` method of math.js.

```javascript
import { sum } from 'mathjs';

const sumValue = sum(...data); // Returns 55235
```

You can also find the sum using a loop if you like.

## How to Find the Mode with JavaScript

The mode of a dataset represents the value that appears the greatest number of times in the set. If you're analyzing that dataset, it's the value that you're most likely to find.

You can find the most occurring element of an array by iterating over the array, using an object to map each value to its count, and looping over this object at the end to find the highest value.

To make this easier to illustrate, modify the `data` array that we've used so far, like this:

```javascript
data[99] = 33;
```

Now, you can find the mode like so:

```javascript
let frequency = {};

for (let datum of data) {
    if (frequency[datum]) frequency[datum] += 1;
    else frequency[datum] = 1;
}

let highestFrequency = 0;
let modeValue = 0; 

for (let datum in frequency) {
    if (frequency[datum] > highestFrequency) {
        highestFrequency = frequency[datum];
        modeValue = datum;
    }
}
```

You can make this a function if you ever need to do it more than once.

You can find the mode more easily by using the `mode` method of the math.js library:

```javascript
const modeValue = mode(...data); // Returns 33
```

## How to Find the Median with JavaScript

If you want to find the median of a dataset, you just need to find the value in the exact middle of the set. This means that the data has to be ordered, or sorted in ascending or descending order – otherwise the middle value has no significance.

You can find the median by sorting the array first, then selecting the item in the middle position if the array has an odd number of elements. If the array has an even number of elements, you select the two items in the middle and find their average.

```javascript
const sortedArray = data.sort((a, b) => a - b);

const middlePosition = Math.floor(data.length / 2);

const median = data.length % 2 == 0 ? (sortedArray[middlePosition] + sortedArray[middlePosition - 1]) / 2 : sortedArray[middlePosition]; // Returns 597.5
```

Alternatively, you can find the median by using the `median` method on math.js.

```javascript
import { median } from 'mathjs';

const medianValue = median(...data); // Returns 597.6
```

## **Summary**

I hope you now understand how to perform these basic Data Analysis functions using JavaScript. The math.js library is one of the many JavaScript libraries that contain multiple helpful functions to make Data Analysis very easy with JavaScript.

If you have any questions or relevant advice, please get in touch with me to share them.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!

