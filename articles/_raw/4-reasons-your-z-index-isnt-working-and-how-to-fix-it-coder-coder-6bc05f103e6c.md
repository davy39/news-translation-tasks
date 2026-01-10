---
title: 4 reasons your z-index isn’t working (and how to fix it)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-25T16:38:07.000Z'
originalURL: https://freecodecamp.org/news/4-reasons-your-z-index-isnt-working-and-how-to-fix-it-coder-coder-6bc05f103e6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nm4AWKx-ezJBFLGShJCVAw.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jessica Chan

  Z-index is a CSS property that allows you to position elements in layers on top
  of one another. It’s super useful, and honestly a very important tool to know how
  to use in CSS.

  Unfortunately, z-index is one of those properties that do...'
---

By Jessica Chan

Z-index is a CSS property that allows you to position elements in layers on top of one another. It’s super useful, and honestly a very important tool to know how to use in CSS.

Unfortunately, z-index is one of those properties that doesn’t always behave in an intuitive way. It seems simple at first- a higher z-index number means the element will be on top of elements with lower z-index numbers. But there are some additional rules that make things more complicated. And you can’t always fix things by setting the z-index to 999999! ?

This article will explain in detail four of the most common reasons that z-index isn’t working for you, and exactly how you can fix it.

We’ll be going through some actual code examples and problem-solving them. After reading this article, you’ll be able to understand and avoid those common z-index pitfalls!

%[https://www.youtube.com/watch?v=qYi-OLf5q5g]

Let’s check out the first reason:

### 1. Elements in the same stacking context will display in order of appearance, with latter elements on top of former elements.

In our first example, we have a relatively simple layout that includes 3 main elements:

* An image of a cat
* A white block with text
* Another image of the same cat

Here’s the HTML markup for that:

```html
<div class="cat-top"></div> 

<div class="content__block"> Meow meow meow... </div> 

<div class="cat-bottom"></div>
```

In this layout, we ideally want the white block of text to be on top of both cats.

To try to achieve this, we’ve added some negative margins to the CSS for both cat images, so that they overlap the white block a bit:

```css
.cat-top { 
   margin-bottom: -110px; 
} 

.cat-bottom { 
   float: right; 
   margin-top: -120px; 
}
```

However, it looks like this:

<iframe height="600" width="800" style="width: 100%;" scrolling="no" title="Z-index: #1: set position, #2: natural stacking order, #3: CSS properties" src="//codepen.io/thecodercoder/embed/XQEyeX/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/thecodercoder/pen/XQEyeX/'>Z-index: #1: set position, #2: natural stacking order, #3: CSS properties</a> by Jessica
  (<a href='https://codepen.io/thecodercoder'>@thecodercoder</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>



The first cat is indeed positioned underneath the white content block, just like we want. But the second cat image is positioned on top of the block!

Why is this happening?

The reason for this behavior is due to the **natural stacking order** on the webpage. These guidelines basically determine which elements will be on top and which will be on the bottom.

Even if elements don’t have their z-index set, there is a rhyme and reason to which ones will be on top.

In our case, none of the elements have a z-index value. So their stacking order is determined by their order of appearance. According to this rule, elements that come later in the markup will be on top of elements that come before them.

(You can read more of the stacking order guidelines at Mozilla Developer Network [here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).)

In our example with the cats and the white block, they are obeying this rule. That’s why the first cat is underneath the white block element, and the white block is underneath the second cat.

Ok, stacking order is all well and good, but how do we fix the CSS so the second cat is underneath the white block?

Let’s look at the second reason:

### 2. The element doesn’t have its position set



One of the other guidelines that determine stacking order is if an element has its position set or not.

To set position for an element, add the CSS `position` property to anything other than `static`, like `relative` or `absolute`. (You can read more about it in [this article](https://coder-coder.com/css-position-layout/) that I wrote.)

According to this rule, positioned elements will display on top of unpositioned elements.

So setting the white block to be `position: relative`, and leaving the two cat elements unpositioned will put the white block on the top of the cats in the stacking order.

This is how it will look- you can also play around with the Codepen above.

![Image](https://cdn-media-1.freecodecamp.org/images/NlDhNhhBXrXmR35aZCt4XCGbfBCt4bRPLHzK)

Woohoo!

Now, the next thing we want to do is rotate the bottom cat upside down, using the `transform` property. That way, both cats will be underneath the white block, with only their heads sticking out.

But doing so can cause more `z-index`-related confusion. We'll address the problem and the solution in the next part.

### 3. Setting some CSS properties like opacity or transform will put the element in a new stacking context.



As we just mentioned, we want to turn the bottom cat upside down. To accomplish this, we’ll add `transform: rotate(180deg)`.

```css
.cat-bottom { 
   float: right; 
   margin-top: -120px; 
   transform: rotate(180deg); 
}
```

But this causes the bottom cat to be displayed on top of the white block again!

![Image](https://cdn-media-1.freecodecamp.org/images/GTJjexmzYUkJa37hDuIUALqGngUjSl0wxFcE)

_What the heck is going on here??_

You may not run into this issue often, but another aspect of stacking order is that some CSS properties like `transform` or `opacity` will put the element into its own, new [stacking context](https://www.w3.org/TR/css-color-3/#transparency).

What this means is that adding the `transform` to the `.cat-bottom` element makes it behave as if it had a `z-index` of 0. Even though it doesn't have its `position` or `z-index` set at all! (W3.org has some informative but [rather dense documentation](https://www.w3.org/TR/css-color-3/#transparency) on how this works with the `opacity` property)

Remember, we never added a `z-index` value to the white block, only `position: relative`. This was enough to position the white block on top of the unpositioned cats.

But since the `.bottom-cat` element is acting as though it is relatively positioned with `z-index: 0`, transforming it has positioned it on top of the white block.

The solution to this is to set `position: relative` and explicitly set `z-index` on at least the white block. You could go one step further and set `position: relative` and a lower `z-index` on the cat elements, just to be extra safe.

```css
.content__block { 
   position: relative; 
   z-index: 2; 
} 

.cat-top, .cat-bottom { 
   position: relative; z-index: 1; 
}
```

In my opinion, doing this will solve most, if not all of the more basic z-index issues.

Now, let’s move on to our last reason that your `z-index` isn't working. This one is a bit more complex, because it involves parent and child elements.

### 4. The element is in a lower stacking context due to its parent’s z-index level



Let’s check out our code example for this:

<iframe height="600" width="800" style="width: 100%;" scrolling="no" title="Z-index: #4 different stacking contexts" src="//codepen.io/thecodercoder/embed/qwYdZw/?height=265&theme-id=0&default-tab=html,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/thecodercoder/pen/qwYdZw/'>Z-index: #4 different stacking contexts</a> by Jessica
  (<a href='https://codepen.io/thecodercoder'>@thecodercoder</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>



Here’s what we have: a simple webpage with regular content, and a pink side tab that says “Send Feedback” that is positioned on top of the content.

Then, when you click on the photo of the cat, a modal window with a transparent gray background overlay opens up.

However, even when the modal window is open, the side tab is still on top of the gray overlay. We want the overlay to be displayed over everything, including the side tab.

Let’s take a look at the CSS for the elements in question:

```css
.content { 
   position: relative; 
   z-index: 1; 
} 

.modal { 
   position: fixed; 
   z-index: 100; 
} 

.side-tab { 
   position: fixed; 
   z-index: 5; 
}
```

All the elements have their position set, and the side tab has a `z-index` of 5, which positions it on top of the content element, which is at `z-index: 1`.

Then, the modal has `z-index: 100` which _should_ put it on top of the side tab at `z-index: 5`. But instead, the modal overlay is underneath the side tab.

Why is this happening?

Previously, we addressed some factors that go into the stacking context, such as if the element has its position set, as well as its order in the markup.

**But yet another aspect of stacking context is that a child element is limited to the stacking context of its parent.**

Let’s take a closer look at the three elements in question.

Here’s the markup we have:

```css
<section class="content">            
    <div class="modal"></div>
</section>

<div class="side-tab"></div>
```

Looking at the markup, we can see that the content and side tab elements are siblings. That is, they exist at the same level in the markup (this is different from z-index level). And the modal is a child element of the content element.

Because the modal is inside the content element, its `z-index` of 100 only has an effect inside its parent, the content element. For example, if there were other child elements that were siblings to the modal, their `z-index` values would put them on top of or underneath each other.

But the `z-index` value of those child elements doesn't mean anything outside the parent, because the parent content element has its `z-index` set to 1.

So its children, including the modal, can’t break out of that `z-index` level.

(You can remember it with this slightly depressing metaphor: a child can be limited by its parents, and can’t break free of them.)

There are a couple of solutions to this problem:

### Solution: Move the modal outside of the content parent, and into the main stacking context of the page.

The corrected markup would then look like this:

```css
<section class="content"></section>

<div class="modal"></div>

<div class="side-tab"></div>
```

Now, the modal element is a sibling element to the two others. This puts all three elements in the same stacking context as them, so each of their z-index levels will now affect one another.

In this new stacking context, the elements will display in the following order, from top to bottom:

* modal (`z-index: 100`)
* side tab (`z-index: 5`)
* content (`z-index: 1`)

### Alternative Solution: Remove positioning from the content, so it won’t limit the modal’s z-index.

If you don’t want to or can’t change the markup, you can fix this problem by removing the `position` setting from the content element:

```css
.content { 
   // No position set 
} 

.modal { 
   position: absolute; 
   z-index: 100; 
} 

.side-tab { 
   position: absolute; 
   z-index: 5; 
}
```

Since the content element is now unpositioned, it will no longer limit the modal’s `z-index` value. So the open modal will be positioned on top of the side tab element, due to its higher `z-index` of 100.

While this does work, I personally would go for the first solution.

Because if for some reason in the future you have to position the content element, it will again limit the modal’s order in the stacking context.

### In Summary  


I hope that you’ve found this tutorial helpful! To sum up, most issues with z-index can be solved by following these two guidelines:

1. Check that the elements have their position set and z-index numbers in the correct order.
2. Make sure that you don’t have parent elements limiting the `z-index` level of their children.

#### Want more?

I'm creating a course in responsive design! [Sign up here](https://coder-coder.com/responsive-design-beginners/) to get emailed when it's published.

I write web development tutorials on my blog c[oder-coder.com](https://coder-coder.com), post mini-tips on [Instagram](https://www.instagram.com/thecodercoder/) and coding tutorials on [YouTube](https://www.youtube.com/c/codercodertv).

