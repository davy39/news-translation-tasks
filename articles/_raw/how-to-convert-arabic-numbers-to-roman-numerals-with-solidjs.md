---
title: How to Convert Arabic Numbers to Roman Numerals with SolidJS
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-03-08T20:52:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-arabic-numbers-to-roman-numerals-with-solidjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Arabic_to_Roman_Converter_-_Mihail_Gaberov.gif
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Have you heard about the Romans? Who hasn’t, right 🙂

  They used their own numeric system, which was a bit of a mouthful, especially when
  it came to writing. It looks like this: I, II, III, IV, V, VI and so on.

  Maybe that’s one of the reasons that peo...'
---

Have you heard about the Romans? Who hasn’t, right 🙂

They used their own numeric system, which was a bit of a mouthful, especially when it came to writing. It looks like this: **I, II, III, IV**, **V**, **VI** and so on.

Maybe that’s one of the reasons that people adopted and started using the Arabic numeric system. It's the one we all know and use on a daily basis. Yes, yes, the same – 1,2,3…and so on.

## **What Are We Building?**

In this tutorial, we will see how to build a small app that gives the user an input for entering Arabic numbers and displays their Roman numeral equivalent with a nice, sleek animation.

We will use [SolidJS](https://www.solidjs.com/) for building the UI and good old [JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript) for implementing the algorithm for the actual conversion. More on this later in the article.

We also will take advantage of [CSS Modules](https://css-tricks.com/css-modules-part-1-need/) and [SASS](https://sass-lang.com/) to help make our application a bit more eye pleasing.

## GitHub Repo and Demo Project

💡If you want to skip the reading, [here](https://github.com/mihailgaberov/arabic-roman-visualized/) 💁 is the GitHub repository, and here you can see the live [demo](https://arabic-roman-visualized.vercel.app/) 📺.

## What is SolidJS?

![Image](https://www.freecodecamp.org/news/content/images/2023/03/logo.png align="left")

SolidJS is a front-end library for creating reactive user interfaces. It is still relatively new. It looks a lot like [React](https://beta.reactjs.org/), but they say it’s [simpler and faster](https://www.webtips.dev/solidjs-vs-react).

It got my attention recently, so I’ve decided to take a deeper look and educate myself. And, of course, share my experience with you here.

## The Project

Our application is really simple. It has just a few dependencies and contains only several components. Let me walk you briefly through them.

### Dependencies

```json
{
  "devDependencies": {
    "vite": "^4.1.1",
    "vite-plugin-solid": "^2.5.0"
  },
  "dependencies": {
    "@motionone/solid": "^10.15.5",
    "@solid-primitives/keyed": "^1.1.8",
    "sass": "^1.58.3",
    "solid-js": "^1.6.10"
  }
}
```

Except the obvious dependency – `solid-js` – I’ve only installed the `sass`, `@motionone/solid` and `@solid-primitives/keyed` libraries. We will use these for the styling and the animations. [Vite](https://vitejs.dev/)\-related packages come with the SolidJS app installation, which means that when you run this:

`npx degit solidjs/templates/js my-app`

It will install all you need to initially run your new SolidJS app.

### Project Structure

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled.png align="left")

*Project Structure*

Maybe folks with React experience will see immediately how much this looks like a regular React application. We have the same file/folders organization. And yes, we can use JSX with Solid as well.

After seeing the ‘new’ Solid application structure, let's dive into the basic components that come from the library and that we need in order to build the UI.

### Components

Components in Solid are, surprise surprise 😲, regular JavaScript functions. A Solid app is composed of these functions. And, same way as in React, they support [JSX](https://beta.reactjs.org/learn/writing-markup-with-jsx). This means we can write functions that produce DOM elements.

For example, here is how our [Logo](https://github.com/mihailgaberov/arabic-roman-visualized/tree/main/src/components/Logo) component looks:

```jsx
import styles from './Logo.module.scss';
import gameLogo from '../../../assets/logo.png';

export function Logo() {
  return (
      <div className={styles.logo}>
          <img src={gameLogo} alt="logo" />
      </div>
  );
}
```

Yes, you guessed right. This will produce HTML code like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-1.png align="left")

*Logo component (HTML)*

Maybe some of you are already asking “C’mon Mihail, are you kidding? What’s the difference between Solid and React?” and I agree. So far everything looks pretty much the same. Let’s talk about Signals now.

### SolidJS Signals

![Image](https://www.freecodecamp.org/news/content/images/2023/03/SolidJS-Create-Signal-Component-2-1270x762.jpeg align="left")

*SolidJS Signal*

Signals are the foundation of reactivity in Solid. They hold values that change over time and they update everything else that uses these values. Which means that if you change a signal’s value, this change will be propagated everywhere else in your app where it’s being used.

This is something that’s missing in the React world. At least in name.

When a signal is created, it gives you back two functions, a getter and setter. You use the first one to get the current value the signal contains. And the setter function is used to change that value. The syntax is the following:

```jsx
const [count, setCount] = createSignal(0)
```

The value you pass as an argument to `createSignal` is the initial value that will be held by the signal, 0 in this case. This means that if you call `count()`without calling `setCount` with a different value before that, the result you will get is that zero.

Now that you've seen how to use it and what its purpose is, you might be thinking about its equivalent in React, `useState`. In my case, that was the initial association that popped into my mind. The so-called signals are means to manage the state in a Solid application. As it gives you an easy way for accessing and changing it.

## The Algorithm

There are multiple implementations of this algorithm. And in many different programming languages. Only a Google search can say how many 🤓.

We'll implement it in JavaScript. I keep the file containing the algorithm separate, in a directory called [lib](https://github.com/mihailgaberov/arabic-roman-visualized/tree/main/lib). This approach keeps our hands untied when it comes to replacing the UI with, say, one done with a different UI library. Or maybe we use it in completely different context. That is, the `frontend` and the `backend` of our application are totally decoupled.

Let’s first walk through the algorithm itself and then we can discuss some improvements we can do.

### Algorithm Steps

First things first, let me layout the code here so that it’s easier for you to follow:

```javascript
export const convertArabicToRoman = function (num) {
	const rules = {
		"M": 1000,
		"CM": 900,
		"D": 500,
		"CD": 400,
		"C": 100,
		"XC": 90,
		"L": 50,
		"XL": 40,
		"XXX": 30,
		"XX": 20,
		"X": 10,
		"IX": 9,
		"V": 5,
		"IV": 4,
		"I": 1
	}
	
	let res = "";
	const romans = Object.keys(rules);

	for (let i = 0; i < romans.length; ++i) {
		const val = rules[romans[i]];
		
		while (num >= val) {
			num -= val;
			res += romans[i];
		}
	}
	return res;
};
```

Next, let’s take a look at the rules that define how the Roman numerals are created.

These rules allow you to write down any number:

* If a smaller numeral comes after a larger numeral, add the smaller number to the larger number.
    
* If a smaller numeral comes before a larger numeral, subtract the smaller number from the larger number.
    
* Do not use the same symbol more than three times in a row.
    
* Modern usage employs seven symbols, each with a fixed integer value:
    

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-57.png align="left")

Keeping in mind these rules, here are few examples:

* 399 in Roman Numerals is **CCCXCIX**
    
* 151 in Roman Numerals is **CLI**
    
* 185 in Roman Numerals is **CLXXXV**
    
* 3070 in Roman Numerals is **MMMLXX**
    
* 570 in Roman Numerals is **DLXX**
    
* 7 in Roman Numerals is **VII**
    
* 290 in Roman Numerals is **CCXC**
    
* 1880 in Roman Numerals is **MDCCCLXXX**
    
* 47 in Roman Numerals is **XLVII**
    

**Let’s go through our solution now step by step:** 🎢.

1. Create a data structure that will hold the representations of the known numbers from the rules. In our case it is a simple JavaScript object.
    
2. Add a few more known numbers that will help us in the later calculations, that is 4, 9, 20, 30, 40, 90, 400 and 900.
    
3. Create an empty string that will hold the result.
    
4. Then use the Object.keys() method to get all Roman numerals from our structure.
    
5. Iterate through them via a for-loop.
    
6. For each Roman numeral letter, get its Arabic counterpart and check if it’s less than or equal to the number we are converting.
    
7. If it is, first subtract it from the number we are converting and then store the current Roman representation in the `res` string by concatenating it with what’s already there.
    
8. After both loops finish, return the end result in our string variable.
    

After defining the algorithm steps, let’s run a specific example through them and it will get clearer.

### Example

OK, let’s take a random number and pass it to our algorithm. Say number **1293**. We will skip the **preparation** steps and go straight to where the real magic happens. Which means we start with getting the Romans numerals which are the keys of our key-value data structure:

```python
	const romans = Object.keys(rules); // ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "XXX", "XX", "X", "IX", "V", "IV", "I"]
```

This results in an array holding the Roman numeral representations we have there. That allows us to iterate over them via the \*\*for-\*\*loop and access each of them on every cycle.

Then, having access to each Roman numeral from this array, we then get its value:

```javascript
const val = rules[romans[i]]; // First cycle this will give 1000, 900 in the second, and so on
```

So we have number 1293 as our input, which we named `num`. In the inner **while-** loop we compare the input with the currently selected value (from the `rules` data structure) and if it’s bigger or equal, we subtract it from our input value. Then we concatenate the Roman numeral letter to our string result.

In our example that would mean the following:

```python
Is 1293 >= 1000 > yes => num = 1293 - 1000 = 293 and res = 'M'
```

Then we keep iterating with the result value from the previous iteration.

```python
Is 293 >= 1000 => no => 293 >= 900 => no => 293 >= 500 => no
=> 293 >= 400 => no => 293 >= 100 => yes => 293 - 100 = 193
and res = 'MC'
```

```python
Is 193 >= 100 => yes => 193 - 100 = 93 and res = 'MCC'
```

```python
Is 93 >= 100 => no => 93 >= 90 => yes => 93 - 90 = 3 and res = 'MCCXC'
```

```python
Is 3 >= 90 => no => 3 >= 50 => no => 3 >= 40 => no => 3 >= 30 => no => 3 >= 20
=> no => 3 >= 10 => no => 3 >= 9 => no => 3 >= 5 => no => 3 >= 4 => no => 3 >= 1
=> yes => 3 - 1 = 2 and res = 'MCCXCI'
```

```python
Is 2 >= 1 => yes => 2 - 1 = 1 and res = 'MCCXCII'
```

and lastly

```python
Is 1 >= 1 => yes => 1 - 1 = 0 and res = 'MCCXCIII' is the final result! 🎉🎉🎉
```

### How to Improve the Process

One thing is important to mention here. If we use the algorithm directly as it is, it could consume whatever number we pass to it. But, keeping in mind the rules mentioned above, the result string could get really long. This could break the UI or at the very least it would make it ugly and unusable for writing.

This is why some implementations talk about adding more letters to the rules. As shown on the table below, we could have letters signifying bigger numbers. Adding this to the algorithm would significantly reduce the length of the result string when a bigger number is added.

For example, with our current implementation, if we enter 1,000,000, the result would be 1000 times the letter M. You can imagine it, it’s a long string of Ms, such as MMMMMMMM\_…\_ But, if we introduce additional letters for bigger numbers, this will become just the letter M with a line above, as shown in the table below.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-2.png align="left")

*Possible improvement using more letters. Source: by* [*https://www.calculateme.com/roman-numerals/to-roman*](https://www.calculateme.com/roman-numerals/to-roman)

## Conclusion

Yet another learning-by-sharing session ends here 🎉.

We achieved two main goals in this tutorial. First we touched on a relatively new player on the front-end libraries market, SolidJS. We got familiar with its basic elements. We figured out how to use them in order to quickly build a decent user interface. And we’ve manage to use this UI to show the workings of our algorithm.

And second, we tackled the algorithm itself. We saw how can we implement it in JavaScript. We also know understand the limitations of this approach, and what would be possible improvements. For example, you can add more letters for signifying the bigger numbers. This could easily remove our top limit. And instead of 4999 we could go unlimited.

Last thing I would like to say here is, as always, thank you for reading 🙏🏻, I hope it was fun and interesting for you!

### References:

* [SolidJS docs](https://www.solidjs.com/)
