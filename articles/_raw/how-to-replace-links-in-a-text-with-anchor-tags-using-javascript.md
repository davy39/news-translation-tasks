---
title: How to replace links in a text with Anchor Tags using JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-28T10:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-links-in-a-text-with-anchor-tags-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/23.-modify-links-in-strings.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  When you make a post on social media, and that post contains links, you would see
  the links styled differently from other text. How can you achieve this?

  For example, here''s a tweet I made on Twitter


  The text for my tweet is:


  hi g...'
---

By Dillion Megida

When you make a post on social media, and that post contains links, you would see the links styled differently from other text. How can you achieve this?

For example, here's a tweet I made on Twitter

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-199.png)

The text for my tweet is:
> hi good morning
> 
> my website is dillionmegida.com and you can also find me on youtube here youtube.com/@deeecode
> 
> thank youuu

There are two links here: **dillionmegida.com** and **youtube.com/@deeecode**. And as you can see in the tweet, these links are styled differently (colored blue) from the other texts (colored white). In addition, when you click on any of these links, the browser is navigated to the right destination.

What happens here?

These links are replaced with anchor elements which are also styled, and that makes their appearance and behavior different from the other texts.

So how can you achieve this with JavaScript? One way you can do this is by replacing the links in a string with anchor elements and embedding the modified string in the DOM.

Let's start by learning how to replace links in a string

I have a [video version of this topic](https://youtu.be/ADQ_UvfiYLk) you can also check out.

## String.Replace() Method

The `replace` method in strings allows you to replace substrings in a string with new characters. This method returns the new string which contains the replacement. Here's an example usage of this method:

```js
const str = "I love JavaScript"
const updatedStr = str.replace("JavaScript", "Python")

console.log(updatedStr)
// "I love Python"
```

In this example, we replaced "JavaScript" with "Python"

For the substring to be replaced, you can use a literal string pattern (as we saw above) or you can use a regular expression.

Here's an example with a regular expression:

```js
const str = "Her passwords are 345543, 995533 and 884499"
const regex = /\d+/g

const updatedStr = str.replace(regex, "******")

console.log(updatedStr)
// "Her passwords are ******, ****** and ******"
```

Here, we specify a regular expression that matches one or more digits.

## String.Replace() Method with Callback Function

For the replacement argument, you can either specify a string (as we have seen in the examples above) or a callback function. The relevance of a callback function is that you can get the matched substring, and use it in your replacement.

Let's use the example we have above:

```js
const str = "Her passwords are 345543, 995533 and 884499"
const regex = /\d+/g

const updatedStr = str.replace(regex, function(matched) {
  const firstChar = matched[0]
  const lastChar = matched.at(-1)
  
  return firstChar + "****" + lastChar
})

console.log(updatedStr)
// "Her passwords are 3****3, 9****3 and 8****9"
```

As you can see here, using a callback function as an argument, I'm able to capture the matched substring and use the first and last characters of that substring in my replacement.

You can learn more about this concept [in this article](https://www.freecodecamp.org/news/how-to-pass-callback-functions-to-string-replace-javascript/)

## Replacing links in a string

To replace a link in a string, you specify a regular expression that matches a link and then you replace that substring with an anchor element `a`. The anchor element would have the `href` attribute and the text content as the substring. Also, the anchor element can have a class that you could use in your stylesheet for changing its appearance.

Let's look at an example. Let's say we have the string from the twitter example:

```js
const str = `hi good morning

my website is dillionmegida.com and you can also find me on youtube here youtube.com/@deeecode

thank youuu`
```

I'm using a backtick so that I can have the string on multiple lines.

Next, our regular expression to match the string:

```js
const linkRegex = /(https?\:\/\/)?(www\.)?[^\s]+\.[^\s]+/g
```

This is a basic regular expression for links.

Explaining how this regular expression works in depth is beyond the scope of this article, but simply put: this regular expression matches substrings that begin (or do not) with "https://", followed by (or not) "www", followed by some characters, followed by a period sign, then followed by some characters. So this pattern would match "https://google.com", "http://www.google.com", "google.io", and so on.

You can improve this expression in multiple ways, such as specifying only accepted domains, because this pattern will also match "google.wrong". That's not the scope of this article, so let's continue with the basic pattern we have.

Now, let's define the callback function:

```js
function replacer(matched) {
  let withProtocol = matched
  
  if(!withProtocol.startsWith("http")) {
    withProtocol = "http://" + matched
  }
 
  const newStr = `<a
    class="text-link"
    href="${withProtocol}"
  >
    ${matched}
  </a>`
  
  return newStr
}
```

This replacer method would take each matched substring as an argument. First, we check if the matched substring begins with "http", and if it doesn't, we prefix the protocol with the string, and assign it to the `withProtocol` variable.

Then we have a `newStr` variable, which we assign a string. This string contains an HTML anchor element with a `class` of "text-link", `href` of the value of `withProtocol` and the text content is `matched`.

Now let's get the modified string:

```js
const modifiedStr = str.replace(linkRegex, replacer)

console.log(modifiedStr)
// "hi good morning

// my website is <a
//   class='text-link'
//   href='http://dillionmegida.com'
// >
//   dillionmegida.com
// </a> and you can also find me on youtube here <a
//   class='text-link'
//   href='http://youtube.com/@deeecode'
// >
//   youtube.com/@deeecode
// </a>

// thank youuu"
```

As you see in this modified string, the links have the replaced with anchor tags. Now let's add this to the DOM. Let's say we have the following html:

```html
<div id='text-target'>
</div>
```

Now, we can have some code in our JavaScript file to embed `modifiedStr` to this element:

```js
const textTarget = document.getElementById('text-target')

textTarget.innerHTML = modifiedStr
```

Let's also add some styles in our css file:

```css
#text-target {
  font-size: 20px;
  padding: 20px;
}

.text-link {
  color: orange;
  font-weight: bold;
  margin-right: 2px;
}
```

Here's the result we get on our browser:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-200.png)

As you can see, the links in the string are replaced with the anchor element and styled just the way we want. Also when you click the link, you would be navigated to the URL.

You can verify this live [on this Codepen project](https://codepen.io/Dillion/pen/gOddxPG).

## Wrap up

Many social media platforms apply this concept where links in a string look and behave differently from the other text in a string. These differences imply that "this is a link".

As we have seen in this article, we achieved this with the `replace` method, a callback replacer function, and by embedding it into the DOM.

You can use this approach in different ways to modify the appearance of your strings.

If you enjoyed this article, please share :)


