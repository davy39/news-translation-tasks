---
title: Here’s how you can make better use of JavaScript arrays
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T15:35:51.000Z'
originalURL: https://freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IZcJKz3761vChU1VFHfzkw.jpeg
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: tips
  slug: tips
seo_title: null
seo_desc: 'By pacdiv

  Quick read, I promise. Over the last few months, I noticed that the exact same four
  mistakes kept coming back through the pull requests I checked. I’m also posting
  this article because I’ve made all these mistakes myself! Let’s browse them ...'
---

By pacdiv

Quick read, I promise. Over the last few months, I noticed that the exact same four mistakes kept coming back through the pull requests I checked. I’m also posting this article because I’ve made all these mistakes myself! Let’s browse them to make sure we correctly use Array methods!

### Replacing Array.indexOf with Array.includes

“If you’re looking for something in your Array, use Array.indexOf.” I remember reading a sentence like this one in my course when I was learning JavaScript. The sentence is quite true, no doubt!

Array.indexOf “returns the first index at which a given element can be found,” says the MDN documentation. So, if we use the returned index later in our code, and Array.indexOf is the solution.

But, what if we only need to know if our array contains a value or not? Seems like a yes/no question, a boolean question I would say. For this case, I recommend using Array.includes which returns a boolean.

### Using Array.find instead of Array.filter

Array.filter is a very helpful method. It creates a new array from another one with all items passing the callback argument. As indicated by its name, we must use this method for filtering, and for getting a shorter array.

But, if we know our callback function can return only one item, I would not recommend it — for example, when using a callback argument filtering through a unique ID. In this case, Array.filter would return a new array containing only one item. By looking for a specific ID, our intention may be to use the only value contained in the array, making this array useless.

Let’s talk about the performance. To return all items matching the callback function, Array.filter must browse the entire array. Furthermore, let’s imagine that we have hundreds of items satisfying our callback argument. Our filtered array would be pretty big.

To avoid these situations, I recommend Array.find. It requires a callback argument like Array.filter, and it returns the value of the first element satisfying this callback. Furthermore, Array.find stops as soon as an item satisfies the callback. There is no need to browse the entire array. Also, by using Array.find to find an item, we give a clearer idea about our intention.

### Replacing Array.find with Array.some

I admit I’ve made this mistake many times. Then, a kind friend told me to check the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Methods_2) for a better way. Here’s the thing: this is very similar to our Array.indexOf/Array.includes case above.

In the previous case, we saw Array.find requires a callback as an argument and returns an element. Is Array.find the best solution if we need to know whether our array contains a value or not? Probably not, because it returns a value, not a boolean.

For this case, I recommend using Array.some which returns the needed boolean. Also, semantically, using Array.some highlights the fact that we don’t need the found item.

### Using Array.reduce instead of chaining Array.filter and Array.map

Let’s face it, Array.reduce isn’t simple to understand. It’s true! But, if we run Array.filter, then Array.map it feels like we’re missing something, right?

I mean, we browse the array twice here. The first time to filter and create a shorter array, the second time to create a new array (again!) containing new values based on the ones we obtained from Array.filter. To get our new array, we used two Array methods. Each method has its own callback function and an array that we cannot use later — the one created by Array.filter.

To avoid low performances on this subject, my advice is to use Array.reduce instead. Same result, better code! Array.reduce allows us to filter and add the satisfying items into an accumulator. As an example, this accumulator can be a number to increment, an object to fill, a string or an array to concat.

In our case, since we’ve been using Array.map, I recommend using Array.reduce with an array to concat as an accumulator. In the following example, depending on the value of _env_, we will add it into our accumulator or leave this accumulator as is.

#### That’s it!

Hope this helps. Be sure to leave comments if you have any thoughts on this article or have any other use cases to show. And if you found it helpful, give me some claps ? and share it. Thanks for reading!

PS: You can [follow me on Twitter here](https://twitter.com/pacdiv_io).

_Note:_ As mentioned by [malgosiastp](https://www.freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c/undefined) and [David Piepgrass](https://www.freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c/undefined) in the comments, please check the support before using Array.find and Array.includes, which are currently not supported by Internet Explorer.

