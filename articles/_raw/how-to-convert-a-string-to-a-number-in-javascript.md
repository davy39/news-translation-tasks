---
title: How to Convert a String to a Number in JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-02T22:25:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-a-number-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/volkan-olmez-aG-pvyMsbis-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "There are many ways to convert a string into a number using JavaScript.\
  \ But what does that look like in code? \nIn this article, I will show you 11 ways\
  \ to convert a string into a number. \nHere's an Interactive Scrim of How to Convert\
  \ a String to a Nu..."
---

There are many ways to convert a string into a number using JavaScript. But what does that look like in code? 

In this article, I will show you 11 ways to convert a string into a number. 

### Here's an Interactive Scrim of How to Convert a String to a Number in JavaScript:

<iframe src="https://scrimba.com/scrim/co2894c679bc693326603ac73?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## How to convert a string to a number in JavaScript using the `Number()` function

One way to convert a string into a number would be to use the `Number()` function.

In this example, we have a string called `quantity` with the value of `"12"`. 

```js
const quantity = "12";
```

If we used the `typeof` operator on `quantity`, then it will return the type of string. 

```js
console.log(typeof quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-9.50.17-AM.png)

We can convert `quantity` into a number using the `Number` function like this:

```js
Number(quantity)
```

We can check that it is now a number by using the `typeof` operator again. 

```js
console.log(typeof Number(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-9.57.35-AM.png)

If you tried to pass in a value that cannot be converted into a number, then the return value would be `NaN` (Not a Number).

```js
console.log(Number("awesome"));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.00.34-AM.png)

## How to convert a string to a number in JavaScript using the **`parseInt()`** function

Another way to convert a string into a number is to use the **`parseInt()`** function. This function takes in a string and an optional radix.

A radix is a number between 2 and 36 which represents the base in a numeral system. For example, a radix of 2 would represent the binary system, while a radix of 10 represents the decimal system. 

We can use the `quantity` variable from earlier to convert that string into a number.

```js
const quantity = "12";

console.log(parseInt(quantity, 10));
```

What happens if I try to change the `quantity` variable to `"12.99"`? Will the result using **`parseInt()`** be the number 12.99?

```js
const quantity = "12.99";

console.log(parseInt(quantity, 10));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.45.08-AM.png)

As you can see, the result is a rounded integer. If you wanted to return a floating point number, then you would need to use **`parseFloat()`.**

## How to convert a string to a number in JavaScript using the **`parseFloat()`** function

The **`parseFloat()`** function will take in a value and return a floating point number. Examples of floating point numbers would be 12.99 or 3.14. 

If we modify our example from earlier to use `parseFloat()`, then the result would be the floating point number of 12.99. 

```js
const quantity = "12.99";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.55.03-AM.png)

If you have leading or trailing whitespace in your string, then `parseFloat()` will still convert that string into a floating point number. 

```js
const quantity = "   12.99    ";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.05.35-AM.png)

If the first character in your string cannot be converted into number, then `parseFloat()` will return `NaN`. 

```js
const quantity = "F12.99";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.08.33-AM.png)

## How to convert a string to a number in JavaScript using the unary plus operator (`+`)

The unary plus operator (`+`) will convert a string into a number. The operator will go before the operand. 

```js
const quantity = "12";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.14.51-AM.png)

We can also use the unary plus operator (`+`) to convert a string into a floating point number.

```js
const quantity = "12.99";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.16.38-AM.png)

If the string value cannot be converted into a number then the result will be `NaN`. 

```js
const quantity = "awesome";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.18.10-AM.png)

## How to convert a string to a number in JavaScript by multiplying the string by the number 1

Another way to convert a string into a number is to use a basic math operation. You can multiply the string value by 1 and it will return a number. 

```js
const quantity = "12";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.42.58-AM.png)

As you can see, when we multiply the `quantity` value by 1, then it returns the number 12. But how does this work? 

In this example, JavaScript is converting our string value to a number and then performing that mathematical operation.  If the string cannot be converted to a number, then the mathematical operation will not work and it will return `NaN`. 

```js
const quantity = "awesome";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.18.10-AM.png)

This method will also work for floating point numbers.

```js
const quantity = "10.5";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.56.19-AM.png)

## How to convert a string to a number in JavaScript by dividing the string by the number 1

Instead of multiplying by 1, you can also divide the string by 1. JavaScript is converting our string value to a number and then performing that mathematical operation.

```js
const quantity = "10.5";

console.log(quantity / 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.08.37-PM.png)

## How to convert a string to a number in JavaScript by subtracting the number 0 from the string

Another method would be to subtract 0 from the string. Like before, JavaScript is converting our string value to a number and then performing that mathematical operation.

```js
const quantity = "19";

console.log(quantity - 0);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.11.59-PM.png)

## How to convert a string to a number in JavaScript using the bitwise NOT operator (`~`)

The bitwise NOT operator (`~`) will invert the bits of an operand and convert that value to a 32-bit signed integer. A 32-bit signed integer is a value that represents an integer in 32 bits (or 4 bytes). 

If we use one bitwise NOT operator (`~`)  on a number, then it will perform this operation: -(x + 1)

```js
console.log(~19);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.20.18-PM.png)

But if we use two bitwise NOT operators (`~`), then it will convert our string to a number. 

```js
const quantity = "19";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.28.16-PM.png)

This method will not work for floating point numbers because the result would be an integer. 

```js
const quantity = "19.99";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.31.16-PM.png)

If you tried to use this method on non-numeric characters, then the result would be zero.

```js
const quantity = "awesome";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.32.45-PM.png)

This method does have its limitations because it will start to break for values that are considered too large. It is important to make sure that your number is between the values of a signed 32 bit integer.

```js
const quantity = "2700000000";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.36.16-PM.png)

To learn more about the bitwise NOT operator (`~`) , please read up in the [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT).

## How to convert a string to a number in JavaScript using the **`Math.floor()`** function

Another way to convert a string to a number is to use the **`Math.floor()`** function. This function will round the number down to the nearest integer. 

```js
const quantity = "13.4";

console.log(Math.floor(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.44.53-PM.png)

Just like in earlier examples, if we tried to use non-numeric characters, then the result would be `NaN`. 

```js
const quantity = "awesome";

console.log(Math.floor(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.46.08-PM.png)

## How to convert a string to a number in JavaScript using the **`Math.ceil()`** function

The `Math.ceil()` function will round a number up to the nearest integer. 

```js
const quantity = "7.18";

console.log(Math.ceil(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.48.15-PM.png)

## How to convert a string to a number in JavaScript using the **`Math.round()`** function

The **`Math.round()`** function will round the number to the nearest integer.

If I have the value of 6.3, then **`Math.round()`** will return 6.

```js
const quantity = "6.3";

console.log(Math.round(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.50.20-PM.png)

But if I changed that value to 6.5, then **`Math.round()`** will return 7.

```js
const quantity = "6.5";

console.log(Math.round(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.51.35-PM.png)

## Conclusion

In this article, I showed you 11 ways to convert a string to a number using JavaScript. 

Here are the 11 different methods discussed in the article.

1. using the `Number()` function
2. using the `parseInt()` function
3. using the `parseFloat()` function
4. using the unary plus operator (`+`)
5. multiplying the string by the number 1
6. dividing the string by the number 1
7. subtracting the number 0 from the string
8. using the bitwise NOT operator (`~`)
9. using the `Math.floor()` function
10. using the `Math.ceil()` function
11. using the `Math.round()` function

I hope you enjoyed this article and best of luck on your JavaScript journey.   

