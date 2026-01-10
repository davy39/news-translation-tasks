---
title: What is Margin Collapse in CSS? And How to Avoid It
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-01-11T18:07:52.000Z'
originalURL: https://freecodecamp.org/news/what-is-margin-collapse-and-how-to-avoid-it
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/domino-g6f10860f9_1280.jpg
tags:
- name: CSS Margins
  slug: css-margins
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "What is Margin Collapse?\nMargin collapse occurs when vertically adjacent\
  \ margins of block-level elements collide to share a general margin space. The size\
  \ of this shared space is dictated by the larger number margin. \nYou can visualize\
  \ this as an arm..."
---

## What is Margin Collapse?

Margin collapse occurs when vertically adjacent margins of block-level elements collide to share a general margin space. The size of this shared space is dictated by the larger number margin. 

You can visualize this as an arm wrestling match, where the larger margin will take over and win.

It is important to clarify what it means to be the larger number. 

If a margin of 70px collides with a margin of 90px, the 90px margin will win. If a margin of -70px collides with a margin of -90px, -90px will win. 

Although a negative number is technically a smaller value on a mathematical scale than a positive number, with margin collapse instead it is helpful to remember that a higher numerical value will hold the higher significance. 

Collapsing is relevant regardless of the unit of measurement such as pixels, rem, em, or percentages. These units can be calculated against each other even with mixed use.

In various scenarios this interaction can become problematic. For example, if you are creating a reusable component that is expected to have a set consistent margin space surrounding it, regardless of placement. 

Inconsistencies may occur depending on, where that component is placed as the margin may interact with another. Fortunately, there are precautions we can take to avoid this.

Margin collapse can cause unexpected behaviors in your layout. You'll likely see applied spacing that doesn't seem to match up with what you expect. 

Instead of trying to increase margins by adding extra pixels until the spacing is correct, you can learn the inner workings of the margin property so you can recognize when collapsing can occur. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/margin-collapse-2.png)

### Margin Collapse Code Example

```html
<div class="one">Block-Level Element One</div>
<div class="two">Block-level Element Two</div>
```

```css
div.one {
    margin-bottom: 30px;
}

div.two {
    margin-top: 100px;
}
```

## Negative Margins

Negative margin values are also susceptible to margin collapse. They work as positive margins do, where the greater number will take over.   
  
The result of a -30px margin and a -100px collision will result in a margin space of -100px.

### Mixing Negative and Positive margins

When a negative and a positive margin interact, the pixels will be added together, cancelling each other out. Here is where some math will factor in. 

For example, a margin of -30px and a margin of 10px will result in a shared margin space of -20px. Alternatively, a margin of 10px and a margin of -1opx will result in no margin spacing (-10 + 10 = 0)! 

## How to Recognize Margin Collapse

There are different scenarios when margins can collapse. Review the comparisons below to gain a better grasp on when margin collapse can happen.

### Margin Collapse

* Elements are block-level, such as `div` or `p`
* Vertical margins will collapse
* Collapse will only occur in Flow Layout, which is the default layout mode
* An "invisible" element like a  `<br/>` will not stop margin collapse

### No Margin Collapse

* Horizontal sibling elements will not collapse
* No margin collapse in Flex, Grid, or Positioned Layout 
* Margin collapse can stack and create a domino effect of siblings effecting each other
* A `<hr/>` element between vertical siblings can prevent collapsing

### How to Inspect your Margins

The Inspect feature in your browser is a great tool to get a visual on your margins, padding, and other aspects of the Box Model. This will help you to see if margins are shared.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/boxmodel.png)
_The Box Model_

## How to Avoid Margin Collapse

First, remember that margins should preferably be used to increase the distance between sibling elements, not to create spacing between a child and a parent. If you need to increase space within the Flow layout, reach first for padding if possible.

Also, consider the layout mode when adding a margin. Take note of which layout mode you are in and watch out for margin collapse whenever in normal Flow Layout. 

To add spacing between siblings and avoid margin collapse altogether, consider using Flexbox or Grid and utilizing their gap functionalities.

You can also consider using a component library aligned with the spacing guidelines of a particular design system. Or you can use an open-source library that has already resolved margin collapse issues. You can also setup a system of design for you team where you can use consistent margin and padding throughout your UI. 

Finally, try to develop a sense for when margin collapse is occurring. Now that you are more aware of this behavior, you will start to notice it more frequently. 

Use your trusty browser inspector tools when your margin collapse radar is activated. If you find it, remove it to prevent repeated use of the style as it may be reused and cause issues in the future.

### Resources on Margin Collapse

If you'd like to do a deeper dive on margin collapse, I highly suggest reading [The Rules of Margin Collapse](https://www.joshwcomeau.com/css/rules-of-margin-collapse/) by Josh W. Comeau. 

I also recommend his comprehensive course [CSS for JavaScript Developers](https://css-for-js.dev/) if you'd like to fill in any gaps in your CSS knowledge and learn more about topics such as this.

## Summary

Margin collapse may be a CSS behavior that you have previously experienced and didn't yet had a definition for, or you might not have had all the tools available to avoid it. 

This tricky aspect of the margin property can often go overlooked and wreak havoc through expected behaviors. Understanding these effects can help to improve your UI and reduce the number of bugs in your CSS.

Happy coding!

