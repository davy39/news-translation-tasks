---
title: How to Work with Strings in JavaScript – Tips for Efficient String Concatenation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-29T20:39:11.000Z'
originalURL: https://freecodecamp.org/news/efficient-string-building-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/JavaScript-Strings.png_copy.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Andrey Germanov\nEverything you see in browser – except images and videos\
  \ – is a string. \nThat's why you should learn how to work with them properly. This\
  \ will dramatically increase the performance of your web applications, both on the\
  \ frontend and..."
---

By Andrey Germanov

Everything you see in browser – except images and videos – is a string. 

That's why you should learn how to work with them properly. This will dramatically increase the performance of your web applications, both on the frontend and backend.

## How Default String Concatenation Works – and Its Problems 

What should you know about strings in programming? The `string` is a primitive data type that holds an array of characters. Values of primitive data types are immutable, so a string's value cannot be changed after you've instantiated it. This is true for most programming languages, including JavaScript. 

But wait, when you do this:

```javascript
let hello = "Hello";
hello += " world";
console.log(hello);
```

You'll see **Hello world** on the console, which means that the value of the `hello` variable has changed. How is this possible? How can JavaScript change the value of a string variable and keep it immutable at the same time?

This happens because JavaScript does not add the second string to the first string directly. Instead, it creates a third empty string, copies the values of both strings to it, and finally reassigns the "hello" variable to this third string. 

In this way, the value of the third string is set only once and the values of the two initial strings stay unchanged to meet the immutability rule. 

This is how the whole string concatenation process looks:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-99.png)
_1) Create an empty range in memory to hold the new string. 2) Copy first string to it. 3) Copy second string to it 4) Reassign the "hello" variable to the new string. 5) Free memory ranges that used to hold first two "Hello" and "world" strings._

Do you see any problem here? What can we say about the performance of this operation? It seems that it does up to five times more operations than it should and it uses two times more memory in step 3 to hold the same data.

On the one hand it's not a big issue if we just want to concatenate two strings, because computers can do millions of operations in a second. But the problem becomes more serious if we need to build long strings. 

Let's say that we need to construct a big portion of HTML content from an external data array in a loop. In this case the HTML string can become huge during this process and JavaScript will create a copy of this string on each iteration of the loop.

As an example, let's see the code that builds a huge string in a loop, by concatenating the initial string a hundred million times.

```javascript
let str = "Hello";

console.log("START",new Date().toUTCString());

for (let index=0;index<100000000;index++) {
    str += "!";
}

console.log("END",new Date().toUTCString());
console.log(str.length);
```

This code appends the "!" symbol to the string a hundred million times. In a real world example you can assume that instead of the '!' symbol it would be real data from an external source that should be displayed later.

Also, this code outputs the current date and time before and after the loop which helps to measure how long it takes. Finally it displays the length of the constructed string.

When I ran this in my Google Chrome browser it took a while to complete. Finally it displayed the following on the JavaScript console:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-100.png)
_The Javascript console shows that the code of a basic string concatenation created a string of 100000005 characters in 1 minute 26 seconds._

As you can see, it took 1 minute 26 seconds and output the correct length of the concatenated string. But when I ran this on another computer, this code crashed the browser and I saw the following output:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-101.png)
_The web browser crash_

If you remember the basic algorithm of string concatenation, described above, it should be clear why this might happen. 

The default string concatenation algorithm is too inefficient and wastes a lot of memory. In this example, it copies from 1 to a hundred million chars a hundred million times while iterating through the loop. The amount of memory used for this is even difficult to realize. 

This means that whether the program crashes or not depends on the amount of available free memory and how the memory garbage collector works in a concrete JavaScript engine implementation to erase unused temporary strings.

## How to Improve the Default String Concatenation Algorithm

The JavaScript string concatenation algorithm we discussed above does not claim to be academically accurate. Various implementations of JavaScript engines may use different string handling optimizations and memory handling mechanisms.

But you should not count on the fact that your code will always run in such engines. 

For example, in the latest version of Google Chrome at the time of this writing, string concatenation worked as shown in the screenshots above. So the purpose of this article is to show how to work with strings more efficiently, regardless of how it is implemented by default.

We should definitely find a way to do exactly what we need by concatenating two strings using a single operation. Many other programming languages, like Java or Go (which also use immutable strings) have a tool called StringBuilder. This is a helper object that allows you to construct a string from elements of arrays or from other mutable objects. 

JavaScript does not have this built-in feature, but it's not difficult to implement a similar idea on your own. 

You can write the same string in a different way:

```javascript
let hello = ["Hello"];
```

This is not a string – rather, this is an array with a string. Instead of strings, arrays are mutable and you can just change them by adding items. This means that if you run this:

```javascript
hello.push(" world");

```

Javascript will just mutate the array by appending the " world" item to the end. This will be done in a single operation after which the array will contain the following:

```javascript
["Hello"," world"]

```

This way you can concatenate as many strings as you need to this array at a very low cost. 

Finally, to create the string from it, you can run the `join` operation on the array:

```javascript
hello = hello.join("");
console.log(hello);

```

After this the output of the "hello" variable will contain the "Hello world" string. Actually, the join operation also creates an empty string and then copies items from the array to it. But this only happens once (instead of every time when concatenating strings).

This approach dramatically increases string concatenation speed in a loop. Let's change the loop example to use the array instead of the string:

```javascript
let str = ["Hello"];

console.log("START",new Date().toUTCString());

for (let index=0;index<100000000;index++) {
    str.push("!");
}

str = str.join("");

console.log("END",new Date().toUTCString());
console.log(str.length);

```

After running this on the same browser, I received the following output:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-102.png)
_The Javascript console shows that the code of a string concatenation using array created a string of 100000005 characters in 8 seconds._

As you can see, the same result was achieved in 8 seconds, which is 10 times faster than regular string concatenation.

## Final Thoughts

As you can see, by changing just three lines of code, you can significantly increase the performance of your data processing pipeline. 

As part of my practice, I had a client whose website was experiencing slowdowns due to ineffective string handling that he attempted to resolve by caching content in CloudFlare. He also seriously considered moving to AWS to increase data throughput to resolve these issues. But it was enough to do a code review to fix it.

You can use the method described in this tutorial when building strings in a loop from external data streams of variable size in JavaScript. Just add strings to an array one by one, and finally join them to a string before output. 

Other programming languages recommend using internal StringBuilder or StringBuffer objects for string concatenation.

For Javascript we constructed the simple StringBuilder that can only append strings. For practice, you can extend it and add different methods to "append", "insert" or "remove" strings from an array. You could also create a class that encapsulates an array variable with functions to manipulate substrings in this array and construct the final string from it when required.

### Some limitations to this method

When adding elements to an array, it is important to keep in mind the existing limits on the number of array elements. If you do not take them into account, you may encounter the "RangeError: invalid array range" error. You can [learn more about the limits here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_array_length). 

If the number of lines to be added in the loop exceeds these limits, then you will have to periodically flush the array into temporary string buffers and then merge these buffers.

To help you to work with strings even more efficiently, there are more great string handling algorithms available. 

One of the fastest of them based on a data structure called "Rope". It was invented to handle operations on huge strings fast. You can [read more about it here](https://en.wikipedia.org/wiki/Rope_(data_structure)). This is more complex than the method discussed above, but you can start from reusing one of the Javascript implementations of the `Rope` in your projects (you can find them [here](https://github.com/component/rope) and [here](https://github.com/josephg/jumprope)).

## Thank you for reading!

Good luck and happy coding everyone :)

Feel free to connect and follow me on the below social networks where I publish announcements about my upcoming articles, similar to this one and other software development news:

LinkedIn: [https://www.linkedin.com/in/andrey-germanov-dev/](https://www.linkedin.com/in/andrey-germanov-dev/)  
Facebook: [https://web.facebook.com/AndreyGermanovDev](https://web.facebook.com/AndreyGermanovDev)  
Twitter: [https://twitter.com/GermanovDev](https://twitter.com/GermanovDev)

