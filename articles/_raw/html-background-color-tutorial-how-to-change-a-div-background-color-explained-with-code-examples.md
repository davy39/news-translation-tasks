---
title: HTML Background Color Tutorial – How to Change a Div Background Color, Explained
  with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-07T02:28:33.000Z'
originalURL: https://freecodecamp.org/news/html-background-color-tutorial-how-to-change-a-div-background-color-explained-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b32740569d1a4ca2a54.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: "By Sarah Chima Atuonwu\nOne of the most common things you may have to do\
  \ as a web developer is to change the background-color of an HTML element. But it\
  \ may be confusing to do if you do not understand how to use the CSS background-color\
  \ property. \nIn ..."
---

By Sarah Chima Atuonwu

One of the most common things you may have to do as a web developer is to change the background-color of an HTML element. But it may be confusing to do if you do not understand how to use the CSS `background-color` property. 

In the article, we discuss 

* the default background color value of an HTML element 
* how to change the background color of a div, which is a very common element
* which parts of the CSS box model are affected by the `background-color` property, and
* the different values this property can take. 

### Default Background Color of an Element

The default background color of  a div is `transparent`. So if you do not specify the background-color of a div, it will display that of its parent element.

### Changing the Background Color of a Div

In this example, we will change the background colors of the following divs.

```html
<div class="div-1"> I love HTML </div>
<div class="div-2"> I love CSS </div>
<div class="div-3"> I love JavaScript </div>
```

Without any styling, this will translate to the following visually. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-12.22.48-PM.png)

Let's change the background color of the divs by adding styles to the classes. You can follow along by trying the examples in an HTML file.

```html
<style>
    .div-1 {
        background-color: #EBEBEB;
    }
    
    .div-2 {
    	background-color: #ABBAEA;
    }
    
    .div-3 {
    	background-color: #FBD603;
    }
</style>

<body>
    <div class="div-1"> I love HTML </div>
    <div class="div-2"> I love CSS </div>
    <div class="div-3"> I love JavaScript </div>
</body>
```

This will result in the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.12.29-AM-1.png)

Cool! We have successfully changed the background color of this div. Next, let's get to know more about this property. Let's see how the background-color property affects parts of the CSS-box model.

### Background Color and the CSS Box Model

According to the CSS box model, all HTML elements can be modeled as rectangular boxes. Every box is composed of 4 parts as shown in the diagram below. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.00-AM-1.png)
_The CSS Box Model_

You can read up on the box model if you are not familiar with it. The question is, which part of the box model is affected when you change the background color of a div? The simple answer is the padding area and the content area. Let's confirm this by using an example.

```html
<style>
    body {
        background-color: #ABBAEA;
    }
    .child {
        height: 200px;
        margin: 20px;
        border: 5px solid;
        background-color: #FBD603;
    }
</style>
<body>
    <div>
        <p>This is the parent div which contains the div we are testing</p>

        <div class="child">
            <p>This example shows that changing the background color of a div does not affect the border and margin of the div.</p>
        </div>
    </div>
</body>
```

This will result in:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.10-AM-1.png)

From the example above, we can see that the margin area and the border area are not affected by the change in background color. We can change the color of the border using the border-color property. The margin area remains transparent and reflects the background color of the parent container. 

Finally, let's discuss the values the background-color property can take.

### Background-color Values

Just like the color property, the background-color property can take six different values. Let's consider the three most common values with an example. In the example, we set the background-color of the div to red with different values.

```html
<style>
    /* Keyword value/name of color */
    .div-1 {
        background-color: red;
    }
    
    /* Hexadecimal value */
    .div-2 {
       background-color: #FF0000;	 
    }
    
    /* RGB value */
    .div-3 {
    	background-color: rgb(255,0,0);
    }
    
</style>

<body>
    <div class="div-1">
        <p>The background property can take six different values.</p>
    </div>

    <div class="div-2">
        <p>The background property can take six different values.</p>
    </div>

    <div class="div-3">
        <p>The background property can take six different values.</p>
    </div>
</body>
```

Notice that they all result with the same background color. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.07.24-AM-1.png)

Other values the `background-color` property can take include HSL value, special keyword values and global values. Here are examples of each of them.

```css
/* HSL value */
background-color: hsl(0, 100%, 25%;

/* Special keyword values */
background-color: currentcolor;
background-color: transparent;

/* Global values */
background-color: inherit;
background-color: initial;
background-color: unset;
```

You can read more on each of these values [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Applying_color).

### Extra Note

When setting the background color of an element, it is important to ensure that the contrast ratio of the background color and the color of the text it contains is high enough. This is to ensure that people with low vision can easily read the text. 

Consider these two divs.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-08-at-11.11.44-AM-1.png)

The contrast between the background color of the first div and the color of the text is not high enough for everyone to see. So unless you are the only one using the website you are building and you have very good eyesight, you should avoid such color combinations. 

The second div has a much better contrast ratio between the background color and the color of the text . Thus, it is more accessible and clearer for people to read.

## Conclusion

In this article, we saw how you can change the background-color of a div. We also discussed which parts of the CSS box model are affected by the change in background-color. Finally, we discussed the values the background-color property can take. 

I hope you found this article useful. Thanks for reading.




