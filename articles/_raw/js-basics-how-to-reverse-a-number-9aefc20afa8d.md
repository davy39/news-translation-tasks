---
title: How to reverse a number in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-03T23:17:43.000Z'
originalURL: https://freecodecamp.org/news/js-basics-how-to-reverse-a-number-9aefc20afa8d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*9bS6yWpHz8_tuY52
tags:
- name: Women Who Code
  slug: women-who-code
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By artismarti

  Examples using an arrow function and regular JS function


  _Photo by [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">chuttersnap on <a href="https://unsplash.com...'
---

By artismarti

#### Examples using an arrow function and regular JS function

![Image](https://cdn-media-1.freecodecamp.org/images/0*9bS6yWpHz8_tuY52)
_Photo by [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Reversing a string or reversing a number is one of the common questions asked at programming interviews. Let’s take a look at how this is done.

#### **Rules/Limitations**:

* Negative numbers should remain negative.

**_ex._** `-12345`_becomes_ `-54321`

* Any leading zeroes should be removed.

**_ex._** `321000` _becomes_ `123` _& not_ `000123`

* The function can accept floats or integers.

**_ex._** `543.2100` _becomes_ `12.345`

* The function will return integers as integers.

**_ex._** `54321` _becomes_ `12345` _& not_ `12345.00`

#### **Solving with an Arrow Function:**

```js
const reversedNum = num => parseFloat(num.toString().split('').reverse().join('')) * Math.sign(num)
```

#### **Solving with a Regular Function:**

```js
function reversedNum(num) {
  return (
    parseFloat(
      num
        .toString()
        .split('')
        .reverse()
        .join('')
    ) * Math.sign(num)
  )                 
}
```

#### **_Difference between an Arrow function & Regular function:_**

In this example, the only difference between the Arrow Function and the Regular function is that the Regular function needs to provide an explicit `return` value.

Arrow functions have an implicit `return` value — if they can be written in one line, without the need for the`{}` braces.

<iframe height="500px" width="100%" src="https://repl.it/@artismarti/ReversedNumbers?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

#### **Let’s break the steps down:**

* **Convert the number to a string**

`num.toString()` converts the given number into a String. We do this so we can use the `split` function on it next.

```js
let num = -5432100
num.toString()

// num = '-5432100'
```

* **Split the String into an Array**

`num.split('')` converts the String into an Array of characters. We do this so we can use the Array reverse function (_which does not work on a String_).

```js
// num = '-5432100'

num.split('')

// num = [ '-', '5', '4', '3', '2', '1', '0', '0' ]
```

* **Reverse the Array**

`num.reverse()` reverses the order of the items in the array.

```js
// num = [ '-', '5', '4', '3', '2', '1', '0', '0' ]

num.reverse()

// num = [ '0', '0', '1', '2', '3', '4', '5', '-' ]
```

* **Join it back into a string**

`num.join('')` reassembles the reversed characters into a String.

```js
// num = [ '0', '0', '1', '2', '3', '4', '5', '-' ]

num.join('')

// num = '0012345-'
```

* [**Parse**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) **the input value into a floating point number:**

`parseFloat(num)` converts `num` into a float from a String.

```js
// num = '0012345-'

parseFloat(num)

// num = 12345
```

**Note**: `parseFloat` runs in the end _(even though it is on the first line of the function)_ on the reversed number and removes any leading zeroes.

* **Multiply it by the [sign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sign) of the original number — to maintain the negative value.**

`num * Math.sign(num)` multiplies the number with the sign of the original number provided.

```js
// original value of num = -5432100
// num = 12345

num * Math.sign(-5432100)

// num = -12345
```

And, there you have it!

