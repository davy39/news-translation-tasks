---
title: How to impress interviewers by using recursion in JavaScript with ES6 features
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-impress-interviewers-by-using-recursion-in-javascript-with-es6-features-a14c763110d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*krm8DV5lopMRYxuH0DevlQ.jpeg
tags:
- name: ES6
  slug: es6
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hugo Di Francesco

  There’s nothing as flashy and useful for JavaScript interviews than recursion.

  If you just want to be impressive with recursion in JavaScript, here are some semi
  real-world (technical test type) examples.

  The short definition of ...'
---

By Hugo Di Francesco

There’s nothing as flashy and useful for JavaScript interviews than recursion.

If you just want to be impressive with recursion in JavaScript, here are some semi real-world (technical test type) examples.

The short definition of a recursive solution to a problem (in computer science) is: don’t use iteration. This usually means a function has to call itself with a smaller instance of the same problem. It does this until it hits a trivial case (usually defined in the problem).

Hence, recursion is composed of a couple of steps.

In this post, we’ll discuss:

* ? Recursion to wrap sequential HTTP requests
* ? Count number of characters

The examples for this post are also on [ObervableHQ](http://beta.observablehq.com/), which is a super cool tool that allows you to build JavaScript notebooks:

* [Recursion to wrap sequential HTTP request](https://beta.observablehq.com/@hugodf/recursion-to-wrap-http-requests)
* [Count number of characters](https://beta.observablehq.com/@hugodf/count-something-in-something-else)

# ? Recursion to wrap sequential HTTP requests

Say you need to get multiple pages from a REST API and you’re forced to use the native HTTPS module, ([example here](https://beta.observablehq.com/@hugodf/recursion-to-wrap-http-requests)). In this situation, we’ll be fetching comments from the Reddit API.

With this API:

* if there are more comments than fit in one response, it will return an `after` field in the data. This can be used as a query param in a request to get the next chunk of comments
* if there are no more comments, `after` will be falsy

That defines our terminating and recursive cases. We fetch data from the Reddit API and then either:

* `after` is falsy → **terminating case**, return the data
* `after` is defined → **recursive case**, pass it to fetch the next page as well as data returned from the current call

One of the tricks used here is passing an empty `data` array into the `recursiveCommentFetch` function from the first pass. This allows us to keep injecting more and more values as we go through each recursive call. We are able to resolve to the full set at the terminating case.

```js
const fetch = require('node-fetch');
const user = 'hugo__df';
function makeRedditCommentUrl(user, queryParams) {
  return `https://www.reddit.com/user/${user}/comments.json?${
    Object.entries(queryParams)
      .filter(([k, v]) => Boolean(v))
      .map(
        ([k, v]) => `${k}=${v}`
      ).join('&')
  }`;
}
function recursiveCommentFetch(user, data = [], { after, limit = 100 } = {}) {
  const url = makeRedditCommentUrl(user, { after, limit });
  return fetch(url)
    .then(res => res.json())
    .then(res => {
      const { after, children } = res.data;
      const newData = [...data, ...children];
      if (after) {
        // recursive case, there's a way to fetch more comments
        return recurseCommentFetch(user, newData, { after });
      }
      // base or terminating case
      return newData;
    });
}
recursiveCommentFetch(user)
  .then(comments => console.log(comments));
```

I familiarized myself with this API by creating the following visualization for Reddit contributions (in GitHub’s contribution graph style). [See it here](https://beta.observablehq.com/@hugodf/reddit-contributions-per-week-graph). The [blog version is also live](https://accountableblogging.com/post-frequency).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/0_H5rcQi_HW8UZTipm.png)

# ? Count number of characters

When the question goes something like this: “given an input, return an object containing how many times each character is present in the input” you’ll use this method.

There’s a [live demo here](https://beta.observablehq.com/@hugodf/count-something-in-something-else).

The terminating and recursive case isn’t immediately obvious, so there are a few leaps here:

1. understanding that an input can be cast to a string, which can be `.split` into an Array (ie. most arbitrary input can be converted into an Array).
2. knowing how to recurse through an Array. It’s probably one of the easier/most common things to recurse through. But it takes seeing it a couple of times to start feeling comfortable doing it.

That gives us the following situation for a recursive function:

* list/array of characters is empty → **terminating case**, return the `characterToCount` map
* list/array of characters is not empty → **recursive case**, update `characterToCountMap` by incrementing/ initializing the current character’s entry. Call the recursive function with the updated map and the rest of the list/array.

I’ve written a more complete post: [**Recursion in JavaScript with ES6, destructuring and rest/spread**](https://codewithhugo.com/recursion-in-javascript-with-es6-destructuring-and-rest/spread/), which goes into more detail (examples and techniques) about how we can recurse through lists (arrays) in ES6 JavaScript. It explains things like the `[firstCharacter, ...rest]` notation.

```js
function recurseCountCharacters(
  [firstCharacter, ...rest],
  characterToCountMap = {}
) {
  const currentCharacterCount = characterToCountMap[firstCharacter] || 0;
  const newCharacterToCountMap = {
    ...characterToCountMap,
    [firstCharacter]: currentCharacterCount + 1
  };
  
  if (rest.length === 0) {
    // base/terminating case
    // -> nothing characters left in the string
    return newCharacterToCountMap;
  }
  // recursive case
  return recurseCountCharacters(rest, newCharacterToCountMap);
}
function countCharacters(input) {
  return recurseCountCharacters(String(input).split(''));  
}
console.log(countCharacters(1000000));
// { "0":6, "1": 1 }
console.log(countCharacters('some sentence'));
// { "s":2,"o":1,"m":1,"e":4," ":1,"n":2,"t":1,"c":1}
```

That’s how you breeze through interviews using recursion ?, running circles around those toy problems.

Recursive solutions to interview problems end up looking cooler and cleaner than iterative ones. They’re interviewer eye-candy.

For any questions, you can reach me on Twitter [@hugo__df](https://twitter.com/hugo__df).

Get all the posts of the week before anyone else in your inbox: [Code with Hugo newsletter](https://buttondown.email/hugo).

