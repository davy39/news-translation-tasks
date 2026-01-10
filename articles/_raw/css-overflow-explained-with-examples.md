---
title: CSS Overflow Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-overflow-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d29740569d1a4ca363e.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'The overflow property controls what happens if an element''s content overflows
  from its set width and height. It is shorthand for the overflow-x and overflow-y
  properties. Note that this property only works for block elements with a specified
  height.

  ...'
---

The `overflow` property controls what happens if an element's content overflows from its set width and height. It is shorthand for the `overflow-x` and `overflow-y` properties. Note that this property only works for block elements with a specified height.

With `overflow`, you can control whether to clip content or add scrollbars when an element’s content is too big to fit in a specified area. 

## **Values**

* `visible`: This is the default value of the property. No content is clipped when it's bigger than its set dimensions.
* `hidden`: Content that overflows is hidden.
* `scroll`: Content is hidden, but users can still scroll through and view the hidden content.
* `auto`: If content is bigger than its set dimensions, content will be hidden automatically and a scrollbar will appear.
* `initial`: Uses the default value for this property, `visible`.
* `inherit`: Uses the overflow value of the parent element.

## **Examples**

Here is the HTML and CSS we'll use for all the following examples:

```html
<div class="box-element">
  <p>
    Who's the baby cats are fats i like to pets them they like to meow back. Attack the dog then pretend like nothing happened kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff, see owner, run in terror. Rub face on everything cats are the world. Meow meow, i tell my human i rule on my back you rub my tummy i bite you hard the best thing in the universe is a cardboard box if it smells like fish eat as much as you wish and carefully drink from water glass and then spill it everywhere and proceed to lick the puddle. Paw at beetle and eat it before it gets away rub butt on table for chew foot, or love you, then bite you and pounce on unsuspecting person. What a cat-ass-trophy! cat slap dog in face let me in let me out let me in let me out let me in let me out who broke this door anyway for prance along on top of the garden fence, annoy the neighbor's dog and make it bark and chew iPad power cord purr.
  <p>
</div>
```

```css
.box-element {
  width: 400px;
  height: 200px;
  border: dashed;
}

.box-element {
  /* overflow will be set here */
}
```

### **Visible:**

```css
.box-element {
  overflow: visible;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-152.png)

### **Hidden:**

```css
.box-element { 
  overflow: hidden; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-153.png)

### **Scroll:**

```css
.box-element { 
  overflow: scroll; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-154.png)

### **Auto:**

```css
.box-element { 
  overflow: auto; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-155.png)

## **overflow-x and overflow-y**

* `overflow-x`: Allows the user to scroll through the content that extends beyond the height of the box element.
* `overflow-y`: Allows the user to scroll through the content that extends beyond the width of the box.

```css
.box-element {
  overflow-x: scroll;
  overflow-y: auto;
}
```

And the `.box-element` will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-157.png)

If the content overflows the Y-axis, then that content will be hidden, whilst a scrollbar should be visible for users to read the rest of the content.

