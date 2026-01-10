---
title: HTML Button Link Code Examples – How to Make HTML Hyperlinks Using the HREF
  Attribute on Tags
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-15T13:51:15.000Z'
originalURL: https://freecodecamp.org/news/html-button-link-code-examples-how-to-make-html-hyperlinks-using-the-href-attribute-on-tags
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6049c377a7946308b76862f0.jpg
tags:
- name: best practices
  slug: best-practices
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In this article, we are going to explore three different ways you can make
  an HTML button act like a link.

  These are the methods we''ll go over:


  Styling a link to look like a button

  Using the action and formaction attributes in a form

  Using the JavaS...'
---

In this article, we are going to explore three different ways you can make an HTML button act like a link.

These are the methods we'll go over:

1. Styling a link to look like a button
2. Using the action and formaction attributes in a form
3. Using the JavaScript onclick event

But first, let's take a look at the wrong approach.

## Why doesn't this approach with the `a` element work?

The code snippet below leads to the freeCodeCamp website when it is clicked.

```html
  <a href="https://www.freecodecamp.org/">
    <button>freeCodeCamp</button>
  </a> 
```

However, this is not valid HTML. 

> The `[a](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element)` element can be wrapped around entire paragraphs, lists, tables, and so forth, even entire sections, so long as there is no interactive content within (e.g., buttons or other links). - (Source: [Web Hypertext Application Technology Working Group](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element))

This is considered bad practice because it makes it unclear as to the user's intent. 

Links are supposed to navigate the user to another part of the webpage or an external site. And buttons are supposed to perform a specific action like submitting a form.  

When you nest one inside the other, it makes it confusing as to what action you want performed. That is why it is best to not nest a button inside an anchor tag. 

## How to style a link to look like a button with CSS

This first approach does not use the button at all. We can style an anchor tag to look like a button using CSS.

This is the default HTML styling for an anchor tag.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/blue-anchor-tag.png)

We can add a class to the anchor tag and then use that class selector to style the element.  

```html
  <a class="fcc-btn" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

If you wanted the link to open up a new page, you can add the `target="_blank"` attribute like this: 

```html
  <a target="_blank" class="fcc-btn" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

Then, we can add a background color and change the font color like this:

```css
.fcc-btn {
  background-color: #199319;
  color: white;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/background-and-white-text.png)

The next step would be to add some padding around the text:

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/adding-padding-1.png)

Lastly, we can use the text-decoration property to remove the underline from the text:

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
  text-decoration: none;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/removing-underline.png)

Now we have an anchor tag that looks like a button. 

We can also make this "button" be a little more interactive by changing the background color depending on the state of the link. 

```css
.fcc-btn:hover {
  background-color: #223094;
}
```

%[https://codepen.io/jessica-wilkins/pen/XWNyGBR]

We could get more intricate with the design, but this is just to show you the basics of styling a link like a button.

You could also choose to use a CSS library like [Bootstrap](https://getbootstrap.com/).

```html
  <a class="btn btn-primary" href="https://www.freecodecamp.org/">freeCodeCamp</a>  

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/bootstrap-styles.png)

If your project already includes Bootstrap, then you can use the built-in button styles. But I would not import Bootstrap just to style one link. 

### What are the issues with this approach?

There is some debate whether it is good practice to style links as buttons. Some will argue that links should always look like links and buttons should look like buttons. 

In the web book titled [Resilient Web Design](https://resilientwebdesign.com/), Jeremy Keith states that 

> one material should not be used as a substitute for another, otherwise the end result is deceptive. 

Why did I bother to bring up this debate? 

My goal is not to make you choose one side of the debate over another. I just want you to be aware of this ongoing discussion. 

## How to use the `action` and `formaction` attributes to make a button in a form

### How to use the `action` attribute

Another alternative would be to nest the button inside a form and use the action attribute. 

Input example:

```html
  <form action="https://www.freecodecamp.org/">
    <input type="submit" value="freeCodeCamp">
  </form>
```

Button example:

```html
  <form action="https://www.freecodecamp.org/">
    <button type="submit">freeCodeCamp</button>
  </form>
```

This would be the default button style.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/default-button-style.png)

We could use the same styles as earlier, but we would have to add the cursor pointer and set the border to none, like this: 

```css
.fcc-btn {
  background-color: #199319;
  color: white;
  padding: 15px 25px;
  text-decoration: none;
  cursor: pointer;
  border: none;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/removing-underline-1.png)

### How to use the `formaction` attribute

Similar to the previous approach, we can create a form and use the formaction attribute.

Input example:

```html
  <form>
    <input type="submit" formaction="https://www.freecodecamp.org/" value="freeCodeCamp">
  </form>
```

Button example:

```html
  <form>
    <button type="submit" formaction="https://www.freecodecamp.org/">freeCodeCamp</button>
  </form>
```

You can only use the formaction attribute with inputs and buttons that have `type="image"` or `type="submit"`.  

### Is this semantically correct?

While this appears to be a working solution, there is a question if this is semantically correct. 

We are using the form tags but this does not function like a real form. The purpose of a form is to collect and submit user data. 

But we are using the submit button to navigate the user to another page. 

When it comes to semantics, this is a not a good way to use the form tags. 

### Side effects for using the action and formaction attributes

When you click on the button, something interesting happens with the URL. The URL now has a question mark at the end of it. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/question-mark-at-end.png)

The reason for this change is because the form is using the GET method. You could switch to the POST method, but there might be cases where that is not ideal either. 

```html
  <form method="POST" action="https://www.freecodecamp.org/">
    <button type="submit">freeCodeCamp</button>
  </form>
```

While this approach is valid HTML, it does come with this unintended side effect. 

## How to use the JavaScript onclick event to make a button

In the previous approaches, we have looked at HTML and CSS solutions. But we can also use JavaScript to achieve the same result. 

Input example:

```html
 <form>
    <input type="button" onclick="window.location.href='https://www.freecodecamp.org/';" value="freeCodeCamp" />
 </form>
```

 Button example:

```html
<button onclick="window.location.href='https://www.freecodecamp.org/';">freeCodeCamp</button>  

```

The `location.href` represents the location of a specific URL. In this case, `Window.location.href` will return [https://www.freecodecamp.org/](https://www.freecodecamp.org/). 

### Drawbacks to this approach

While this solution does work, there are some potential issues to consider. 

If the user has decided to disable JavaScript in their browser, then clearly this solution would not work. Unfortunately, that could lead to a poor user experience. 

## Conclusion

The goal of this article was to show you three different ways you can make buttons act like links.

The first approach was to design a link to look like a button. We also looked into the debate whether it is a good idea to change the appearance of links to look like another element.

The second approach used the form and formaction attributes. But we also learned that this approach has some side effects with the URL and is not semantically correct. 

The third approach used the JavaScript onclick event and the Window.location.href. But we also learned that this approach might not work if the user decides to disable JavaScript in their browser. 

As a developer, it is really important to look at the pros and cons of a particular approach before incorporating it into your project.   

I hope you enjoyed this article and learned a few things along the way. 

Happy coding! 


