---
title: JavaScript String Contains – How to use JS .includes()
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-05T16:46:38.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-contains-how-to-use-js-includes
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/amie-bell-XGqS569rdgk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "In JavaScript you can use the .includes() method to see if one string is\
  \ found in another. But how does it work exactly?\nIn this article, I will walk\
  \ you through a few code examples of the JavaScript string method called .includes().\
  \ \nBasic .includes..."
---

In JavaScript you can use the `.includes()` method to see if one string is found in another. But how does it work exactly?

In this article, I will walk you through a few code examples of the JavaScript string method called `.includes()`. 

## Basic `.includes()` Syntax

Here is the basic syntax for the `.includes()` method:

```js
str.includes(search-string, optional-position)
```

The `search-string` parameter is the string you are searching for in `str`.

The `position` parameter is an optional number for the starting search position in the `str`. If the position parameter is omitted then the default is zero. 

If the `search-string` is found then it will return `true`. If the `search-string` is not found then it will return `false`. 

## Code examples for the includes method 

In this first example, we have the sentence, "I love freeCodeCamp".  We want to see if the word "love" is included in that sentence.

In the code, `str` would be "I love freeCodeCamp" and the `search-string` would be  "love".

```js
"I love freeCodeCamp".includes("love")
```

Since the word "love" is included inside the `str`, then the code will return `true`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.35.42-PM.png)

### Is the `.includes()` method case sensitive?

If we modify our `str` to "I LOVE freeCodeCamp" and the `search-string` is still "love", then the return value would be `false`.

```js
"I LOVE freeCodeCamp".includes('love')
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.40.56-PM.png)

This is `false` because the `.includes()` method is case sensitive. "LOVE" is not the same as "love".

### How to use the optional position parameter

We are going to modify our example to use the position parameter. We now want to check if "love" is found in "I love freeCodeCamp" when the search starts at position 1.

Remember that strings use zero-based indexing which means that the first letter "I" is index 0. 

Our code will return `true` because when we start searching at position 1, the word "love" doesn't appear until position 2 so it's completely contained in the string. 

Position 1 until the end of the sentence includes these characters and spaces. 

```
" love freeCodeCamp"
```

Remember that spaces in strings get an index value. 

This is what our code would look like using the position parameter. 

```js
"I love freeCodeCamp".includes('love', 1)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.55.34-PM.png)

If we change the position to be 3, then the return would be `false`.

```js
"I love freeCodecamp".includes('love', 3)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-10.06.30-PM.png)

This returns `false` because position 3 is the letter "o".

Position 3 until the end of the sentence includes these characters and spaces. 

```
"ove freeCodeCamp"
```

You can see that the (whole) word "love" is not present in that string.

## Conclusion

In JavaScript you can use the `.includes()` method to see if one string is found in another.

Here is the basic syntax for the `.includes()` method.

```js
str.includes(search-string, optional-position)
```

If the `search-string` is found then it will return `true`. If the `search-string` is not found then it will return `false`. 

The `.includes()` method is case sensitive which means if the `search-string` doesn't match the exact casing in `str` then it will return `false`. 

The `position` parameter is an optional number for the starting search position in the `str`. If the position parameter is omitted then the default is zero. 

I hope you enjoyed this article on the `.includes()` method and best of luck on your JavaScript journey.

