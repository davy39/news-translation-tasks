---
title: CSS Naming Conventions that Will Save You Hours of Debugging
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T23:17:20.000Z'
originalURL: https://freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YunI3ChUVMlpmFzo75FczQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: style
  slug: style
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Emmanuel Ohans

  I have heard lots of developers say they hate CSS. In my experience, this comes
  as a result of not taking the time to learn CSS.

  CSS isn’t the prettiest ‘language,’ but it has successfully powered the styling
  of the web for over 20 ...'
---

By Emmanuel Ohans

I have heard lots of developers say they hate CSS. In my experience, this comes as a result of not taking the time to learn CSS.

CSS isn’t the prettiest ‘language,’ but it has successfully powered the styling of the web for over 20 years now. Not doing too badly, huh?

However, as you write more CSS, you quickly see one big downside.

It is darn difficult to maintain CSS.

Poorly written CSS will quickly turn into a nightmare.

Here are a few naming conventions that will save you a bit of stress and countless hours down the line.

![Image](https://cdn-media-1.freecodecamp.org/images/0Nm4l3DA3bWTbPc6C4ViWDqewokYYootpoqb)
_you’ve been there before, haven’t you?_

### Use Hyphen Delimited Strings

If you write a lot of JavaScript, then writing variables in camel case is common practice.

```
var redBox = document.getElementById('...')
```

Great, right?

The problem is that this form of naming isn’t well-suited to CSS.

Do not do this:

```
.redBox {  border: 1px solid red;}
```

Instead, do this:

```
.red-box {   border: 1px solid red;}
```

This is a pretty standard CSS naming convention. It is arguably more readable.

Also, it is consistent with the CSS property names.

```
// Correct
```

```
.some-class {   font-weight: 10em}
```

```
// Wrong
```

```
.some-class {   fontWeight: 10em}
```

### The BEM Naming Convention

Teams have different approaches to writing CSS selectors. Some teams use hyphen delimiters, while others prefer to use the more structured naming convention called BEM.

Generally, there are 3 problems that CSS naming conventions try to solve:

1. To know what a selector does, just by looking at its name
2. To have an idea of where a selector can be used, just by looking at it
3. To know the relationships between class names, just by looking at them

Have you ever seen class names written like this:

```
.nav--secondary {  ...}
```

```
.nav__header {  ...}
```

That is the BEM naming convention.

### Explaining BEM to a 5 year Old

BEM attempts to divide the overall user interface into small reusable components.

Consider the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/pIFVbUmRtKN8x6DvLHEvJeUSM9Oda8ClkY5f)
_It is an award winning image of a stick-man :)_

No, it’s not award winning :(

The stick-man represents a component, such as a block of design.

You may have already guessed that the B in BEM stands for ‘Block’.

In the real world, this ‘block’ could represent a site navigation, header, footer, or any other block of design.

Following the practice explained above, an ideal class name for this component would be `stick-man`.

The component should be styled like so:

```
.stick-man {   }
```

We have used delimited strings here. Good!

![Image](https://cdn-media-1.freecodecamp.org/images/ThMVqj-sv26pjpzLJU3MIF2TCdn-S4CjlEZk)

### E for Elements

The E in ‘BEM’ stands for Elements.

Overall blocks of design rarely live in isolation.

For instance, the stick-man has a `head`, two gorgeous `arms`, and `feet`.

![Image](https://cdn-media-1.freecodecamp.org/images/bf2jyOzcZ8wgd95I3qR9IS3Cf6pRlQ2hHuGM)

The `head` , `feet`, and `arms` are all elements within the component. They may be seen as child components, i.e. children of the overall parent component.

Using the BEM naming convention, element class names are derived by adding **two underscores,** followed by the element name.

For example:

```
.stick-man__head {
```

```
}
```

```
.stick-man__arms {
```

```
}
```

```
.stick-man__feet {
```

```
}
```

### M for Modifiers

The M in ‘BEM’ stands for Modifiers.

What if the stick-man was modified and we could have a `blue` or a `red` stick- man?

![Image](https://cdn-media-1.freecodecamp.org/images/Q-aWWnpw1UuoXxp5NGHxsjP5689VQBT0oGdQ)

In the real world, this could be a `red` button or `blue` button. These are modifications of the component in question.

Using BEM, modifier class names are derived by adding two **hyphens** followed by the element name.

For example:

```
.stick-man--blue {
```

```
}
```

```
.stick-man--red {
```

```
}
```

The last example showed the parent component being modified. This is not always the case.

What if we had stick-men of different `head` sizes?

![Image](https://cdn-media-1.freecodecamp.org/images/ZK-riYJhmFfBVEof6xO8yGGR3O10g2dW7Xqn)

This time the element has been modified. Remember, the element is a child component within the overall containing block.

The `.stick-man` represents the `Block` , `.stick-man__head` the element.

As seen in the example above, double hyphens may also be used like so:

```
.stick-man__head--small {
```

```
}
```

```
.stick-man__head--big {
```

```
}
```

Again, note the use of the double **hyphens** in the example above. This is used to denote a modifier.

Now you’ve got it.

That’s basically how the BEM naming convention works.

Personally, I tend to use only hyphen delimeter class names for simple projects, and BEM for more involved user interfaces.

You can [read more](http://getbem.com/naming/) about BEM.

[**BEM - Block Element Modifier**](http://getbem.com/naming/)  
[_BEM - Block Element Modifier is a methodology, that helps you to achieve reusable components and code sharing in the…_getbem.com](http://getbem.com/naming/)

### Why Use Naming Conventions?

> There are only two hard problems in Computer Science: cache invalidation and naming things — _Phil Karlton_

Naming things is hard. We’re trying to make things easier, and save ourselves time in the future with more maintainable code.

Naming things correctly in CSS will make your code easier to read and maintain.

If you choose to use the BEM naming convention, it will become easier to see the relationship between your design components/blocks just by looking at the markup.

Feeling confident?

### CSS Names with JavaScript Hooks

Today is John’s first day at work.

He is handed over an `HTML` code that looks like this:

```
<div class="siteNavigation">
```

```
</div>
```

John has read this article and realizes this may not be the best way to name things in `CSS`. So he goes ahead and refactors the codebase like so:

```
<div class="site-navigation">
```

```
</div>
```

Looks good, huh?

Unknown to John, he had broken the codebase ???

How?

Somewhere in the JavaScript code, there was a relationship with the previous class name, `siteNavigation`:

```
//the Javasript code
```

```
const nav = document.querySelector('.siteNavigation')
```

So, with the change in the class name, the `nav` variable became `null`.

How sad.

To prevent cases like this, developers have come up with different strategies.

#### 1. Use js- class names

One way to mitigate such bugs is to use a `**js-***` class name to denote a relationship with the DOM element in question.

For example:

```
<div class="site-navigation js-site-navigation">
```

```
</div>
```

And in the JavaScript code:

```
//the Javasript code
```

```
const nav = document.querySelector('.js-site-navigation')
```

As a convention, anyone who sees the `**js-**site-navigation` class name would understand that there is a relationship with that DOM element in the JavaScript code.

#### 2. Use the Rel attribute

I don’t use this technique myself, but I have seen people do.

Do you recognize this?

```
<link rel="stylesheet" type="text/css" href="main.css">
```

Basically, the **rel attribute** defines the relationship that the linked resource has to the document from which it’s referenced.

In the previous example with John, proponents of this technique would do this:

```
<div class="site-navigation" rel="js-site-navigation">
```

```
</div>
```

And in the JavaScript:

```
const nav = document.querySelector("[rel='js-site-navigation']")
```

I have my doubts about this technique, but you’re likely to come accross it in some codebases. The claim here is, _“well, there’s a relationship with Javascript, so I use the rel attribute to denote that”_.

The web is a big place with lots of different “methods” for solving the same problem.

#### 3. Don’t use data attributes

Some developers use data attributes as JavaScript hooks. This isn’t right. By definition, data attributes are used **to store custom data**.

![Image](https://cdn-media-1.freecodecamp.org/images/08r5ESO6cpzZvcZz-KczJEGXtPBtCLorryI6)
_Good use of data attributes. As seen on Twitter_

**Edit #1: As mentioned by some amazing people in the comment section, if people use the ‘rel’ attribute, then it’s perhaps okay to use data attributes in certain cases. It’s your call afterall.**

### Bonus Tip: Write More CSS Comments

This has nothing to do with naming conventions, but it will save you some time too.

While a lot of web developers try to NOT write JavaScript comments or stick to a few, I think you should write more CSS comments.

Since CSS isn’t the most elegant “language,” well-structured comments can save time when you’re trying to understand your code.

It doesn’t hurt.

Take a look at how well commented the Bootstrap [source code](https://github.com/twbs/bootstrap/blob/v4-dev/scss/_carousel.scss) is.

You do not need to write comments to say `color: red` will give a red color. But, if you’re using a CSS trick that is less obvious, feel free to write a comment.

### Ready to become Pro?

I have created a free CSS guide to get your CSS skills blazing, immediately. [Get the free ebook](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/4AqtYrYGSx6s9Mwmzji1vj8RqwvarVns4y7V)
_Seven CSS Secrets you didn’t know about_

