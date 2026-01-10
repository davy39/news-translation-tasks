---
title: CSS Before and CSS After – How to Use the Content Property
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-06-26T23:42:55.000Z'
originalURL: https://freecodecamp.org/news/css-before-and-after-how-to-use-the-content-property
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/fCC_-Content-Property-1.png
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: The content property in CSS defines the content of an element. You may have
  heard that this property only applies to the ::before and ::after pseudo-elements.
  In this article, we'll explore various use cases for the content property, including
  outsid...
---

The `content` property in CSS defines the content of an element. You may have heard that this property only applies to the `::before` and `::after` pseudo-elements. In this article, we'll explore various use cases for the `content` property, including outside of pseudo-elements.

## Prerequisite

Since the majority of the use cases for the `content` property involve pseudo-elements, I would suggest that you be familiar with how the `::before` and `::after` pseudo-elements work. Here is a great article to get you up to speed:

* [CSS Pseudo-Elements - Before and After Selectors Explained](https://www.freecodecamp.org/news/css-pseudo-elements-before-and-after-selectors-explained/)
    

## Accepted Values

First, let's take a look at all of the accepted values of the `content` property.

* `normal`: This is the default value. Computes to `none` when used with pseudo-elements.
    
* `none`: A pseudo-element will not be generated.
    
* `<string>`: Sets the content to the string specified. This string can contain Unicode escape sequences. For example, the copyright symbol: `\\000A9`.
    
* `<image>`: Sets the content to an image or gradient using `url()` or `linear-gradient()`.
    
* `open-quote` | `close-quote`: Sets the content to the appropriate quote character referenced from the `quotes` property.
    
* `no-open-quote` | `no-close-quote`: Removes a quote from the selected element, but still increments or decrements the nesting level referenced from the `quotes` property.
    
* `attr(*attribute*)`: Sets the content as the string value of the selected elements selected attribute.
    
* `counter()`: Sets the content as the value of a `counter`, usually a number.
    

## String

One of the most basic examples would be the use of adding *string* content before or after an element. In this example, we'll add a link symbol before a link and add the URL for the link after it.

```css
a::before {
	content: "\\1F517 ";
}
a::after {
	content: " (" attr(href) ")";
}
```

Notice the space after the Unicode character in the `::before` pseudo-element and the before the first parenthesis in the `::after` pseudo-element. This will create space between these and the parent element.

Alternatively, you could add `padding` or `margin` to the pseudo-elements to add separation.

%[https://codepen.io/codeSTACKr/pen/OJMjpvL?editors=1100] 

## Basic Quotes

With the `content` property, you can add quotes before and/or after elements. Now, in HTML we do have the `<q>` tag. This will also add quotes around its content. However, with the `content` property, we can have more control over the implementation.

Here is the most basic example of adding quotes:

%[https://codepen.io/codeSTACKr/pen/NWxvpXq] 

You can accomplish this as well by using the HTML tag `<q>`. But maybe we want to style the quote differently. So let's only add the opening quote and not the ending quote. And let's also style the opening quote.

```css
p {
  position: relative;
  font-size: 3rem;
  margin: 4rem;
}
p::before {
  content: open-quote;
  position: absolute;
  left: -3.5rem;
  top: -2rem;
  font-size: 8rem;
  color: rgba(0, 0, 0, 0.5)
}
```

The result:

![Image showing a single styled quote on the top left of the paragraph](https://www.freecodecamp.org/news/content/images/2020/06/quote2.jpg align="left")

## Advanced Quotes

We can also specify where we do *not* want quotes. For example, you may be quoting someone who is quoting another person. So you would have quotes within quotes, which can get confusing to the reader.

In the CodePen below, we are using HTML `<q>` tags, then specifying which tags should not display the quotes.

At first glance, you might think that we should just remove the `<q>` tag where needed. But by specifying where a quote should not be still increments or decrements the nesting level referenced from the `quotes` property.

To explain this, we need to understand the `quotes` property. This is simply an "array" of characters that should be used when quoting. Here is an example:

```css
q {
  quotes: '“' '”' '‘' '’' '“' '”';
}
```

These are sets of quotes. The first set will be used for the top level of quotes. The second set will be used for the first nested quote. And the third set will be used for the second nested quote. And so on, if there were more sets included.

Now that we understand the `quotes` property, I can explain how the `no-open-quote` and `no-close-quote` properties work.

For each level of quotes, we can assign different sets of characters to use for the quotes. By specifying where a quote should not be still increments or decrements the nesting level referenced from the `quotes` property.

Take a look at the example below. You will see that the second level of quotes is skipped.

%[https://codepen.io/codeSTACKr/pen/NWxvbLw] 

## Attributes

Attributes can be used to pass content from HTML into the CSS `content` property. We actually used this already in the link example where we used the `href` attribute to include the URL string as part of our content.

A perfect use case for this is a tooltip. You can add a `title` attribute to an element in HTML to have a simple, built-in tooltip on hover. But to customize this, we can use a data attribute on our HTML tag and then use the `content` property to add a tooltip.

In this example, we use the attribute `data-tooltip` from our HTML element to pass the value into our tooltip. For the pointer of the tooltip, we set the `content` to `""`, as `content` is required to render a `::before` or `::after` pseudo-element.

%[https://codepen.io/codeSTACKr/pen/WNrEopO] 

## Counters

The `counter()` CSS function returns a string representing the current value of the named counter. In the following example we have an ordered list that we will add content using a `counter`.

```html
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
```

```css
ol {
  counter-reset: exampleCounter;
}
li {
  counter-increment: exampleCounter;
}
li::after {
  content: "[" counter(exampleCounter) "] == ["
               counter(exampleCounter, upper-roman) "]";
}
```

Without getting too in-depth on the `counter` function, we have to first initiate the counter on the `ol` element. We can name this whatever we would like. Then we tell the counter to increment on each `li` element. And lastly, we set the `content` of the `li::after`.

Here's the result:

![Ordered List](https://www.freecodecamp.org/news/content/images/2020/06/counter.jpg align="left")

You could use this to customize content within each list item that needs a corresponding number. Or you could use this to customize the list item itself. For instance, you could remove the default numbering and implement a custom-styled numbering system.

## Images

Images and gradients can be used with the `content` property. This is fairly straight-forward. Here is an example that uses both:

%[https://codepen.io/codeSTACKr/pen/WNrEpre] 

For accessibility, there is also an option to add alternate text for the image. This feature is not fully supported though.

```css
content: url(//unsplash.it/200/200) / "Alternative Text Here";
```

> Note: This is unsupported in Firefox, IE, and Safari. Also, the gradient does not work in Firefox.

## Outside of Pseudo Elements

That's right! You can use the `content` property outside of the pseudo-elements `::before` and `::after`. Although, its use is limited and not fully compatible in all browsers.

The most compatible use case would be replacement of an element.

```html
<div id='replace'>
  codeSTACKr
</div>
```

```css
#replace {
  content: url("<https://www.codestackr.com/logo_twoline_light.svg>");
  width: 100%;
}
```

> Note: Replacement is not supported in IE.

## Conclusion

Most times you will see `content: ""` found in the `::before` and `::after` pseudo-elements. But the `content` property has many useful applications.

The best use in my opinion is to use it for updating bulk elements. If you want to add an icon before every link on your site, it would be much easier to add it through the `content` property than to add it to every element in the HTML document.

## **Thanks for reading!**

Thank you for reading this article. Hopefully, it has helped you to better understand how the `content` property works in CSS.

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

I'm Jesse from Texas. Check out my other content and let me know how I can help you on your journey to becoming a web developer.

* [Subscribe To My YouTube](https://youtube.com/codeSTACKr)
    
* Say Hello! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)
    
* [Sign Up For My Newsletter](https://codeSTACKr.com)
