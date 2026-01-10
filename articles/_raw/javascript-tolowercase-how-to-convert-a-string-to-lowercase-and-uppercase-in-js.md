---
title: JavaScript toLowerCase() – How to Convert a String to Lowercase and Uppercase
  in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-16T15:07:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-tolowercase-how-to-convert-a-string-to-lowercase-and-uppercase-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "This article explains how to convert a string to lowercase and uppercase\
  \ characters. \nWe'll also go over how to make only the first letter in a word uppercase\
  \ and how to make the first letter of every word in a sentence uppercase.\nLet's\
  \ get started!\n..."
---

This article explains how to convert a string to lowercase and uppercase characters. 

We'll also go over how to make only the first letter in a word uppercase and how to make the first letter of every word in a sentence uppercase.

Let's get started!

## How to use the `toLowerCase()` method in JavaScript

The `toLowerCase` method converts a string to lowercase letters.

The general syntax for the method looks like this:

```javascript
String.toLowerCase()
```

The `toLowerCase()` method doesn't take in any parameters. 

Strings in JavaScript are **immutable**. The `toLowerCase()` method  converts the string specified into a new one that consists of only lowercase letters and returns that value. 

It means that the old, original string is not changed or affected in any way.

```javascript
let myGreeting = 'Hey there!';

console.log(myGreeting.toLowerCase());

//output
//hey there!
```

The string `myGreeting` consists of only one capital letter that gets converted to lowercase.

Any letters that are already lowercase are not affected by the `toLowerCase()` method, only uppercase ones. These letters preserve their original form.

The string in the example below consists of all capital letters. They are all then converted to lowercase when the `toLowerCase()` method is applied.

```javascript
const  anotherGreeting = 'GOOD MORNING!!';

console.log(anotherGreeting.toLowerCase());
//output
//good morning!!
```


## How to use the `toUpperCase()` method in JavaScript

The `toUpperCase()` method is similar to the `toLowerCase()` method but it instead converts the string value to uppercase.

The general syntax for calling the method looks like this:

```javascript
String.toUpper()
```

It doesn't take in any parameters.

As strings in JavaScript are immutable, the `toLowerCase()` method does not change the value of the string specified.

It instead returns a new value. The string specified is converted to a new one whose contents consist of only all uppercase letters. This means that there will now be two strings: the original and the newly converted capitalized one.


```javascript
console.log('I am shouting!'.toUpperCase());

//output
//I AM SHOUTING!
```

Any capital letters already in the string will not be affected and will remain unchanged when the `toLowerCase()` method gets called.

### How to capitalize only the first letter in a string in JavaScript

What if you want to make only the first letter of a string a capital?

Below is a simple example that shows you one way to do just that.

Say there is a variable called `myGreeting` with the string value of `hello`, in all lowercase letters.

```javascript
let myGreeting = 'hello';
```

You first locate and extract the first letter of that string by using its index. Then you call the `toUpperCase()` method on that specific letter.

As a reminder, indexing in JavaScript (and most programming languages) starts at `0`, so the first letter has an index of `0`.

Save this operation in a new variable called `capFirstLetter`.

```javascript
let capFirstLetter = myGreeting[0].toUpperCase();

console.log(capFirstLetter);
// returns the letter 'H' in this case
```

Next, you want to isolate and cut off that first character and keep the remainder of the string.

One way to do this is by using the `slice()` method. This creates a new string starting from the index specified until the end of the word.

You want to start from the second letter until the end of the value.

In this case, the argument you should pass to `slice()` is an index of `1` since that is the index of the second letter.

This way, the first character is excluded altogether. A new string is returned without it but containing the rest of the characters – minus that first letter.

Then save that operation to a new variable.

```javascript
let restOfGreeting = myGreeting.slice(1);

console.log(restOfGreeting);
//returns the string 'ello'
```

By combining the two new variables with concatenation, you get a new string with only the first letter capitalized.

```javascript
let newGreeting = capFirstLetter + restOfGreeting;

console.log(newGreeting);
//Hello
```

Another way is to combine the steps from above and isolate them in a function.

The function gets created just once. The function then returns a new string with the first letter capitalized.

The amount of code you need to write is substantially less while also being able to pass in any string as an argument without writing repetitive code.

```javascript
function capFirst(str) {
     return str[0].toUpperCase() + str.slice(1);
 }

console.log(capFirst('hello'));
//output 
//Hello
```

### How to capitalize the first letter of every word in JavaScript

But how do you make the first letter of every word in a sentence uppercase?

The method shown in the section above won't work as it doesn't deal with multiple words, just a single word in a sentence.

Say you have a sentence like the one below. You want to capitalize every first word in the sentence.

```javascript
let learnCoding = 'learn to code for free with freeCodeCamp';
```

The first step is to split the sentence into individual words and work with each one separately.

For that, you use the `split()` method and pass a space as an argument. It means that with every space in the sentence provided, an item gets passed into a new array.

It splits the sentence based on blank spaces.

Create a new variable and store the new array.

```javascript
let splitLearnCoding = learnCoding.split(" ");

console.log(splitLearnCoding); 
//['learn', 'to', 'code', 'for', 'free', 'with', 'freeCodeCamp']
```


Now from that sentence, there is a new array of words that allows you to manipulate each word on its own, separately.

Since there is now a new array, you can use the `map()` method to iterate over each individual item inside it.

In the `map()` method, you use the same procedure shown in the section above to take each word individually, capitalize the first letter, and return the rest of the word.

```javascript
let capSplitLearnCoding = splitLearnCoding.map(word => {
    return word[0].toUpperCase() + word.slice(1);
})

console.log(capSplitLearnCoding);
//['Learn', 'To', 'Code', 'For', 'Free', 'With', 'FreeCodeCamp']
```

The first letter of every word is now capitalized. 

All that is left now is to combine the words in the array together in a single sentence again. 

For that you use the `join()` method and pass a space as the argument. 

```javascript
let learnCodingNew = capSplitLearnCoding.join(" ");

console.log(learnCodingNew);
//Learn To Code For Free With FreeCodeCamp
```

As shown in the section above, you can also create a function that combines all theses steps. You will then be able to pass as an argument any string and each first word in it will be uppercase.

```javascript
function capFirstLetterInSentence(sentence) {
    let words = sentence.split(" ").map(word => {
        return word[0].toUpperCase() + word.slice(1);
    })
    return words.join(" ");
}

console.log(capFirstLetterInSentence("i am learning how to code"));
//I Am Learning How To Code
```


## Conclusion

And there you have it! This is how you use the `toLowerCase()` and `toUpperCase()` methods in JavaScript.

You learned how to capitalize the first letter of a word and capitalize the first letter of each word in a sentence.

If you want to learn JavaScript and gain a better understanding of the language, freeCodeCamp has a [free JavaScript Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

You'll start from the basics as an absolute beginner to the language and then advance to more complex subjects such as Object Oriented Programming, Functional Programming, Data Structures, Algorithms, and helpful Debugging techniques. 

In the end, you'll build five projects to put your skills to practice.

Thanks for reading, and happy learning!


