---
title: JavaScript Void 0 – What Does javascript:void(0); Mean?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-27T20:27:10.000Z'
originalURL: https://freecodecamp.org/news/javascript-void-keyword-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9811740569d1a4ca17fb.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  The word void means "completely empty space" according to the dictionary. This term,
  when used in programming, refers to a return of "nothing" - an "empty value" so
  to speak.

  What is the void keyword?

  When a function is void, it mea...'
---

By Dillion Megida

The word void means "completely empty space" according to the dictionary. This term, when used in programming, refers to a return of "nothing" - an "empty value" so to speak.

## What is the void keyword?

When a function is void, it means that the function returns nothing. This is similar to functions in JavaScript which return `undefined` explicitly, like so:

```js
function und() {
  return undefined
}
und()
```

or implicitly, like so:

```js
function und() {
}
und()
```

Regardless of the expressions and statements in the functions above (adds 2 numbers together, finds the average of 5 numbers, whatever), there is no result returned.

Now we know what the `void` keyword is all about. What about `javascript:void(0)`?

## What is `javascript:void(0)`?

If we split this up, we have `javascript:` and `void(0)`. Let's look at each part in more detail.

### `javascript:`

This is referred to as a **Pseudo URL**. When a browser receives this value as the value of `href` on an anchor tag, it interprets the JS code that follows the colon (:) rather than treating the value as a referenced path. 

For example:

```html
<a href="javascript:console.log('javascript');alert('javascript')">Link</a>
```

When "Link" is clicked, here is the result:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-119.png)

As seen above, the browser does not treat `href` as a referenced path. Instead, it treats it as some JavaScript code starting after "javascript:" and separated by semi-colons.

### `void(0)`

The void operator evaluates given expressions and returns `undefined`.

For example:

```js
const result = void(1 + 1);
console.log(result);
// undefined
```

`1 + 1` is evaluated but `undefined` is returned. To confirm that, here's another example:

```html
<body>
  <h1>Heading</h1>
  <script>
        void(document.body.style.backgroundColor = 'red',
             document.body.style.color = 'white'
        )
  </script>
</body>
```

The result of the above code is:          
                 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-122.png)

Here's another example:

```js
console.log(void(0) === undefined)
// true
```

### Combining `javascript:` and `void(0)`

Sometimes, you do not want a link to navigate to another page or reload a page. Using `javascript:`, you can run code that does not change the current page. 

This, used with `void(0)` means, **do nothing** - don't reload, don't navigate, do not run any code.

For example:

```html
<a href="javascript:void(0)">Link</a>
```

The "Link" word is treated as a link by the browser. For example, it's focusable, but it doesn't navigate to a new page.

`0` is an argument passed to `void` that does nothing, and returns nothing. 

JavaScript code (as seen above) can also be passed as arguments to the `void` method. This makes the link element run some code but it maintains the same page.

For example:

```js
<a id='link' href="javascript:void(
  document.querySelector('#link').style.color = 'green'
)">Link</a>
```

When the button is clicked, this is the result:    

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-121.png)

With `void`, it tells the browser not to return anything (or return `undefined`).

Another use case of links with the `javascript:void(0)` reference is that sometimes, a link may run some JavaScript code in the background, and navigating may be unnecessary. In this case, the expressions would be used as the arguments passed to `void`.

## Conclusion

In this simplified article, we've learned what the `void` operator is, how it works, and how it is used with the `javascript:` pseudo URL for `href` attributes of links. 

This ensures that a page does not navigate to another page or reload the current page when clicked.


