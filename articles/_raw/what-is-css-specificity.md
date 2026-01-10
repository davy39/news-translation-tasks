---
title: CSS Specificity and When to Use the CSS Important Tag
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-11T10:09:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-css-specificity
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98bd740569d1a4ca1bc5.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Sarah Chima Atuonwu\nCSS specificity is an important topic to understand\
  \ if you want to get better at CSS. It is the set of rules applied to CSS selectors\
  \ that determines which style is applied to an element. \nTo understand this better,\
  \ it's import..."
---

By Sarah Chima Atuonwu

CSS specificity is an important topic to understand if you want to get better at CSS. It is the set of rules applied to CSS selectors that determines which style is applied to an element. 

To understand this better, it's important that we understand a related topic – cascading in CSS .

## The Cascading Nature of CSS

CSS means Cascading Style Sheets. "Cascading" means that the **order** in which CSS rules are applied to an element **actually matters**. 

Ideally, if two rules are applied to the same element, the one that comes last is the one that will be used. Let's use an example to understand this.

We'll apply two classes to an element and give each class a different `background-color`.

```text
<p class="style1 style2"> This is a test paragraph</p>
```

Here's the CSS:

```text
.style2 {
  background-color: red;
}

.style1 {
  background-color: yellow;
}
```

This is the result:

<script async src="//jsfiddle.net/sarahchima/1vpme0a8/4/embed/result,html,css/"></script>

Notice that the `style1` which comes last in the stylesheet is applied to the element. Now you may expect this to always be how CSS applies styles to elements, but it's not always the case. 

Take this next example.

```text
<p class="style1" id="paragraph"> This is a test paragraph</p>
```

The CSS looks like this:

```text
#paragraph {
  background-color: red;
}

.style1 {
  background-color: yellow;
}
```

Which style do you expect to apply to the element? The `#paragraph` or the `.style1`?

Here's the result:

<script async src="//jsfiddle.net/sarahchima/hxbta4k3/2/embed/result,html,css/"></script>

Notice that the first is applied. The `#paragraph` is an id selector, while the `style1` is a class selector. This is because cascade works with specificity to determine which values are applied to an element. 

So, what is CSS specificity?

## CSS Specificity explained

According to MDN, Specificity is the means by which browsers decide which CSS property values are the most relevant to an element and, therefore, will be applied.

Simply put, if two CSS selectors apply to the same element, the one with higher specificity is used. 

That's why in our previous example, the property value of the id selector was applied because it has a higher specificity value.

So how are the specificities of selectors calculated?

## The Specificity Hierarchy

Calculating the specificity values of selectors is quite tricky. One way to calculate it is to use a weight system to rank different selectors to create an hierarchy. 

We'll assign weights to each selector for us to better understand how each selector ranks. Let's start with the least.

### Elements and Pseudo-elements

We use element selectors like `a`, `p`, and `div` to style a selected element, while pseudo-elements like `::after` and `::before` are used to style specific parts of an element.

```text
<!-- This is an element selector-->
p { 
    color: red;
}

<!-- This is an pseudo-element selector-->
p::before {
    color: red;
}
```

Element and pseudo-element selectors have the lowest specificity. In the specificity weight system, they have a value of 1.

### Classes, Attributes and Pseudo-classes

Here are examples of classes, attributes, and pseudo-classes:

```text
<!-- This is a class selector-->
.person { 
    color: red;
}

<!-- This is an attribute selector-->
[type="radio"] { 
    color: red;
}

<!-- This is a pseudo-class selector-->
:focus {
    color: red;
}
```

They have a higher specificity than element and pseudo-element selectors. In our specificity weight system, they have a value of 10.

### ID Selectors

ID selectors are used to target an element using the element's ID.

```text
<!-- This is an ID selector-->
#header {
    color: red;
}
```

ID selectors have higher specificity than classes and elements. In our specificity weight system, they have a value of 100.

### Inline Styles

Inline styles are applied directly on the element in the HTML document. This is an example:

```text
<p style="color: red">This is a paragraph</p>
```

Inline styles have the highest specificity. In our specificity weight system, they have a value of 1000.

Here's a summary of the weights:

```text
Inline Styles                               - 1000
ID selectors                                -  100
Classes, Attributes and Pseudo-classes      -   10
Elements and Pseudo-elements                -    1 
```

Let's try to make sense of it.

The property values of selectors with a higher weight will always be applied over a selector with a lower weight. 

Inline styles have the highest weight and their property value overrides every other selector's value applied to an element. 

For example, if we have an element and for the same property `color`, there's an inline style. If the class and id selectors also have values for the same property, the inline style wins.

```text
<p style="color: red" class="yellow" id="paragraph">This is a paragraph</p>
```

The stylesheet:

```text
#paragraph {
    color: green;
}

.yellow {
    color: yellow;
}
```

This is the result:

<script async src="//jsfiddle.net/sarahchima/nrmL6ygz/3/embed/result,html,css/"></script>

The same thing happens when an ID selector and class selector have values for the same property. The property value of the ID selector will apply.

Note that the weights only apply when different selectors have values for the **same `property`**.

### Multiple Element Selectors

There are times when more than one selector is used to target an element. For example, for a list like this:

```text
<ul class="list">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

You may target the list items like this:

```text
.list > li { 
    color: green;
}
```

or like this:

```text
ul > li {
    color: red;
}
```

In a case where both selectors are used on the same stylesheet, which style will be applied to the list items?

Let's go back to our weight system to calculate the specificity of both selectors.

For `.list > li`, the weight of one class selector is `10` and the weight of an element selector is `1`. Combined their sum is `11`.

For `ul > li`, the weight of one element selector is `1`. There are two element selectors used, so their sum is `2`.

Which of the color values do you will think will be applied?

If you said the color of the `.list>li` selector will be applied, you got it right. It has a higher specificity value than the other selector.

<script async src="//jsfiddle.net/sarahchima/6xjp54yh/1/embed/result,html,css/"></script>

Let's try another example. Given this element:

```text
<div class="first-block" id="div-1"> 
    <div class="second-block" id="div-2">
        <p class="text" id="paragraph">This is a paragraph</p>
    </div>
</div>
```

and these styles

```text
#div-1 > .second-block > .text {
    color: blue
}

.first-block > #div-2 > #paragraph {
    color: red
}
```

Try to calculate the specificity and guess which `color` value will apply.

This is the result:

<script async src="//jsfiddle.net/sarahchima/7brp4nmg/4/embed/result,html,css/"></script>

Let's use our weight system to understand why the color value of the second selector is applied.

For `#div-1 > .second-block > .text`, we have one ID selector and two class selectors. The sum of their weights is `100 + 10 + 10 = 120`.

For `.first-block > #div-2 > #paragraph`, we have one class selector and two ID selectors. The sum of their weights is `10 + 100 + 100 = 210`.

That's why the value of latter selector is used.

You can try this example on your own to be sure that you get the hang of it.

```text
<div class="first-block" id="div1">
    <ul class="first-list" id="list1">
        <li class="first-list-item" id="listItem1">First 
            <span class="first-span" id="span1">item</span>
        </li>
    </ul>
</div>
```

Which color will be applied to the `span` if the following styles are in the stylesheet?

```text
div#div1 > .first-list > #list-item > span {
    color: red;
}

#list > #list-item > #span {
    color: purple;
}

#div1 > #list > .first-list-item > .first-span {
    color: light-blue;
}
```

Try to calculate the specificity and compare it with the result you get when you run the code.

Before we conclude this article, there are some important points to note.

## Important Points about CSS Specificity

The weight assigned to a selector just gives us an idea of which rules get applied to an element. However, this does not always suffice. 

For instance, you may assume that if you use more than 10 classes (weight >= 100) to target an element, the property values will override that of one ID selector. But this is not true. As long as the selector with more than 10 classes have no ID selector, the one ID selector will always take precedence over it.

Applying `!important` to the property value of any selector makes it the value that will be applied to the element. This happens regardless of the rank of the selector on the Specificity hierarchy. 

Let's use an example to understand this.

```text
<p class="blue" id="paragraph" style="color: green"> This is a paragraph </p>
```

If the following styles are applied

```text
p {
    color: red !important;
}
.blue {
    color: blue;
}

#paragraph {
    color: purple;
}
```

The value of the element selector `p` will be used because of the `!important` attached to the value. 

However, if another selector has the `!important` tag attached to the same property, the value of the later selector is used.

<script async src="//jsfiddle.net/sarahchima/2weo7cyr/4/embed/result,html,css/"></script>

That's why `!important` should be avoided because it makes it difficult override a style.

Generally, to style a specific element, it is more advisable to use a class. This makes it easier to override the styles if you ever need to do so.

## Summary

From this article, we can see that CSS specificity is an important topic to understand because it can save you hours of debugging. 

With this knowledge, you can easily find out why your styles are not being applied. 

Here are the major points to take out of this article:

* Due to the cascading nature of CSS, if two rules are applied to the same element, the one that comes last is the one that will be used.
* CSS specificity is a set of rules that determine which style is applied to an element.
* The weight system is one way of calculating the specificity of different selectors. Here's a summary of the weights:

```
Inline Styles                               - 1000
ID selectors                                -  100
Classes, Attributes and Pseudo-classes      -   10
Elements and Pseudo-elements                -    1 
```

* `!important` overrides all other styles regardless of the specificity of the selector where it is used.

I hope you enjoyed reading this article.

  



