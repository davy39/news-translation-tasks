---
title: How to Capitalize the First Letter of Each Word in JavaScript – a JS Uppercase
  Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-26T17:24:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-capitalize-words-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9905740569d1a4ca1d64.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Catalin Pit

  In this article, you are going to learn how to capitalize the first letter of any
  word in JavaScript. After that, you are going to capitalize the first letter of
  all words from a sentence.

  The beautiful thing about programming is that ...'
---

By Catalin Pit

In this article, you are going to learn how to capitalize the first letter of any word in JavaScript. After that, you are going to capitalize the first letter of all words from a sentence.

The beautiful thing about programming is that there is no one universal solution to solve a problem. Therefore, in this article you are going to see multiple ways of solving the same problem.

# Capitalize the first letter of a word

First of all, let's start with capitalizing the first letter of a single word. After you learn how to do this, we'll proceed to the next level – doing it on every word from a sentence. Here is an example:

```js
const publication = "freeCodeCamp";

```

In JavaScript, we start counting from 0. For instance, if we have an array, the first position is 0, not 1. 

Also, we can access each letter from a String in the same way that we access an element from an array. For instance, the first letter from the word "_freeCodeCamp_" is at position 0.

This means that we can get the letter **f** from _freeCodeCamp_ by doing `publication[0]`. 

In the same way, you can access other letters from the word. You can replace "0" with any number, as long as you do not exceed the word length. By exceeding the word length, I mean trying to do something like `publication[25`, which throws an error because there are only twelve letters in the word "freeCodeCamp".

### How to capitalize the first letter

Now that we know how to access a letter from a word, let's capitalize it.

In JavaScript, we have a method called `toUpperCase()`, which we can call on strings, or words. As we can imply from the name, you call it on a string/word, and it is going to return the same thing but as an uppercase. 

For instance:

```js
const publication = "freeCodeCamp";
publication[0].toUpperCase();

```

Running the above code, you are going to get a capital **F** instead of f. To get the whole word back, we can do this:

```js
const publication = "freeCodeCamp";
publication[0].toUpperCase() + publication.substring(1);

```

Now it concatenates "F" with "reeCodeCamp", which means we get back the word "FreeCodeCamp". That is all!

### Let's recap

To be sure things are clear, let's recap what we've learnt so far:

* In JavaScript, counting starts from 0.
* We can access a letter from a string in the same way we access an element from an array - e.g. `string[index]`.
* Do not use an index that exceeds the string length (use the length method - `string.length` - to find the range you can use).
* Use the built-in method `toUpperCase()` on the letter you want to transform to uppercase.

# Capitalize the first letter of each word from a string

The next step is to take a sentence and capitalize every word from that sentence. Let's take the following sentence:

```js
const mySentence = "freeCodeCamp is an awesome resource";

```

### Split it into words

We have to capitalize the first letter from each word from the sentence `freeCodeCamp is an awesome resource`. 

The first step we take is to split the sentence into an array of words. **Why?** So we can manipulate each word individually. We can do that as follows:

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

```

### Iterate over each word

After we run the above code, the variable `words` is assigned an array with each word from the sentence. The array is as follows `["freeCodeCamp", "is", "an", "awesome", "resource"]`.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
}

```

Now the next step is to loop over the array of words and capitalize the first letter of each word. 

In the above code, every word is taken separately. Then it capitalizes the first letter, and in the end, it concatenates the capitalized first letter with the rest of the string.

### Join the words

What is the above code doing? It iterates over each word, and it replaces it with the uppercase of the first letter + the rest of the string. 

If we take "freeCodeCamp" as an example, it looks like this `freeCodeCamp = F + reeCodeCamp`. 

After it iterates over all the words, the `words` array is `["FreeCodeCamp", "Is", "An", "Awesome", "Resource"]`. However, we have an array, not a string, which is not what we want. 

The last step is to join all the words to form a sentence. So, how do we do that?

In JavaScript, we have a method called `join`, which we can use to return an array as a string. The method takes a separator as an argument. That is, we specify what to add between words, for example a space.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
}

words.join(" ");

```

In the above code snippet, we can see the join method in action. We call it on the `words` array, and we specify the separator, which in our case is a space. 

Therefore, `["FreeCodeCamp", "Is", "An", "Awesome", "Resource"]` becomes `FreeCodeCamp Is An Awesome Resource`.

# Other methods

In programming, usually, there are multiple ways of solving the same problem. So let's see another approach.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

words.map((word) => { 
    return word[0].toUpperCase() + word.substring(1); 
}).join(" ");

```

**What is the difference between the above solution and the initial solution?** The two solutions are very similar, the difference being that in the second solution we are using the `map` function, whereas in the first solution we used a `for loop`.

Let's go even further, and try to do a **one-liner**. Be aware! One line solutions might look cool, but in the real world they are rarely used because it is challenging to understand them. Code readability always comes first.

```js
const mySentence = "freeCodeCamp is an awesome resource";

const finalSentence = mySentence.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());

```

The above code uses **RegEx** to transform the letters. The RegEx might look confusing, so let me explain what happens:

* `^` matches the beginning of the string.
* `\w` matches any word character.
* `{1}` takes only the first character.
* Thus, `^\w{1}` matches the first letter of the word.
* `|` works like the boolean `OR`. It matches the expression after and before the `|`.
* `\s+` matches any amount of whitespace between the words (for example spaces, tabs, or line breaks).

Thus, with one line, we accomplished the same thing we accomplished in the above solutions. If you want to play around with the RegEx and to learn more, you can use [this website](https://regexr.com/).

# Conclusion

Congratulations, you learnt a new thing today! To recap, in this article, you learnt how to:

* access the characters from a string
* capitalize the first letter of a word
* split a string in an array of words
* join back the words from an array to form a string
* use RegEx to accomplish the same task

Thanks for reading! If you want to keep in touch, let's connect on Twitter [@catalinmpit](https://twitter.com/intent/follow?screen_name=catalinmpit). I also publish articles regularly on my blog [catalins.tech](https://catalins.tech) if you want to read more content from me.

