---
title: A visual guide to CSS Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T07:27:53.000Z'
originalURL: https://freecodecamp.org/news/do-you-even-flex-box-c16449cfca96
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qucqUWwkbRPaVF0muyhN-g.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zeeshaan Maudarbocus

  What is CSS Flexbox?

  As per the MDN web docs:


  “CSS Flexible Box Layout is a module of CSS that defines a CSS box model optimized
  for user interface design, and the layout of items in one dimension. In the flex
  layout model, t...'
---

By Zeeshaan Maudarbocus

### **What is CSS Flexbox?**

As per the MDN web docs:

> _“CSS Flexible Box Layout is a module of CSS that defines a CSS box model optimized for user interface design, and the layout of items in one dimension. In the flex layout model, the children of a flex container can be laid out in any direction, and can “flex” their sizes, either growing to fill unused space or shrinking to avoid overflowing the parent. Both horizontal and vertical alignment of the children can be easily manipulated.”_

So to summarize, it is a layout module that makes things easier to align and distribute space among items in a container.

Let’s have a quick look at a few examples of what can be done with just a minimum of 1–2 lines of codes using CSS flexbox:

Horizontal alignment layout:

![Image](https://cdn-media-1.freecodecamp.org/images/fNTVn8WpbfBeMCThuUM9WWA55Nclr6T-pWaI)
_display: flex_

Vertical alignment layout:

![Image](https://cdn-media-1.freecodecamp.org/images/1Loex4JPiVH4TjVuSmY7vk4BTZKGv5qu5A4o)
_flex-direction: column_

It’s pretty cool given that just one or two lines of CSS were required to manipulate the layout inside each container.

### **The Basics**

Flexbox properties can be categorized into 2 main types:

1. **Container properties** (flex-direction, flex-wrap, justify-content, align-items, align-content)
2. **Flex Item properties** (order, flex, flex-grow, flex-shrink, align-self)

#### **Display: flex**

The first property is not specific to flexbox. That property is `display` which we set to the value: `flex` . This is set on the container which contains the items we want to manipulate.

Let’s add some visuals to understand how it works:

If we initially have a container, with 3 boxes ( `div` ) inside of it. This is how they will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/499sbxU5hRDoKXof2IuvBZ86G27WiEKN9O4s)
_Container with 3 boxes_

Now let’s add `flex` to the container:

![Image](https://cdn-media-1.freecodecamp.org/images/drIav4nUAz0hGxqndfN-HJMeVNYN5UUG18Zl)
_`display: flex;`_

Just one line of CSS has changed the layout from a vertical direction to a horizontal one.

#### **Important Terminologies around Flexbox**

![Image](https://cdn-media-1.freecodecamp.org/images/CrFtHTSVIdR7Dqq-03ryhZIlqbX5r86JIJlF)
_terminologies related to flexbox_

These terminologies will be used throughout this guide.

1. **Flex Container:** This refers to the container that has `display: flex;` set to it.
2. **Flex Item:** These are the individual children inside of the Flex Container
3. **Main-axis**: By default is set from left to right.
4. **Cross-axis**: By default is set from top to bottom.

As soon as `display: flex` is set on a container, these imaginary axes are going to work together to determine how the flex items inside of the flex container should move around and behave. These two axes change directions, whenever we change certain flexbox properties which are discussed below.

#### **Flex-direction**

This property determines the direction of the imaginary axes. The axes, in turn, determines how the items in the flex container should be placed. It takes the following 4 values:

1. `row` is the default value of the main axis which points from left to right. The cross-axis remains from top to bottom.
2. `row-reverse` reverses the direction of the row from right to left. Again, the cross-axis is left unaffected.

![Image](https://cdn-media-1.freecodecamp.org/images/FoiNopDUSzaDfmBRdfkipXzknXluXnsHtZyD)
_flex-direction: row-reverse;_

3. `column` changes the main-axis from the horizontal axis to the vertical axis. Meaning that the main-axis is now flowing from top to bottom while the cross-axis now flows from left to right.

![Image](https://cdn-media-1.freecodecamp.org/images/qLRCI9W8q8TpC20lLXOXrCIKROWYsRvV8vMs)
_flex-direction: column;_

4. `column-reverse` is similar to the column value with the only difference being that the main-axis now flows from bottom to top.

![Image](https://cdn-media-1.freecodecamp.org/images/TjDPAkqDmogY31pMG-ZCaWEZhYK67ZAP3op0)
_flex-direction: column-reverse;_

#### **Flex-wrap**

The flex-container by default does not allow for items to take up several lines in a row. Instead, all of the items will be squished to fit into one row, that is, it does not allow for wrapping into several lines.

1. `flex-wrap: no-wrap` is the default.

![Image](https://cdn-media-1.freecodecamp.org/images/uroUYXVBrpQiZipR5c4JVvm5RB9DmdSv4PIg)
_no-wrap. Each block is 200px in a 500px container_

2. `flex-wrap: wrap` . By changing that property to `wrap`, we can now ensure that each flex-item will keep their respective sizes. If they cannot fit on one line, they will wrap into a next row or column depending on the flex-direction.

![Image](https://cdn-media-1.freecodecamp.org/images/JnYxdDQn1qESWUWgfBXbPafTpFNejiNwFp5Y)
_flex-wrap set to wrap for the same case as above_

If the flex-direction has been set to row-reverse, then the items will go onto the next row starting from the right to the left.

3. `wrap-reverse` on the other hand will wrap the next row of flex items above the initial one, still from left to right.

![Image](https://cdn-media-1.freecodecamp.org/images/Dp-NP6eMN4-xK987GAPEtdsHAOdoMCdIA7Fs)
_Flex-wrap now set to wrap-reverse_

#### **Justify-content**

This property is used very often. Its purpose is to distribute space between flex-items in a flex-container along the **main axis**. Its default value is set to `flex-start` .

![Image](https://cdn-media-1.freecodecamp.org/images/WQ1EGCmhvH1ectG2APn6G762jmKRJDZGJtOU)
_1. justify-content: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/DH9LFgtyTqM4OfL7AZXzDC8ELiorA0GTKxwl)
_2. justify-content: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/GM1B4g6eE7oIhDjYoFYbhJOQjSNSGKoDZqRH)
_3. justify-content: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/s7dHJo8qtbeNAXJXjIbb9woBGFiMRvqnGw-j)
_4. justify-content: space-between;_

![Image](https://cdn-media-1.freecodecamp.org/images/f9F4uWOsXXq3hj6A5qO2wdL-L6PQUj3NcrCu)
_5. justify-content: space-around;_

**Remember:** If flex-direction has been set to column, then the main-axis would now flow from top to bottom. Meaning that justify-content would now be distributing the items in a vertical fashion.

#### **Align-items**

This property is just as popular as `justify-content` and is used regularly with flexbox. It does the same thing as `justify-content` with the only difference being that it works along the **cross-axis**. The default value for `align-items` is `stretch`.

![Image](https://cdn-media-1.freecodecamp.org/images/D3nBOOnF6moyki-v6PcKY4Cp8IdKTpdUjCh8)
_1. align-items: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/PMNLD87bTT83lTpGQouFZsQEgfor7UAmdNKY)
_2. align-items: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/7KFkc53rzNF86KW9qfGtxAwKyF6EqNN6QCfl)
_3. align-items: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/mUbWmyiritrypgTTExjDjXn34oUrrhmzpt5o)
_4. align-items: baseline;_

![Image](https://cdn-media-1.freecodecamp.org/images/SpErFyFcyHdOHNEpRBLrpuvpwpD81TLWyVxQ)
_5. align-items: stretch;_

**Remember:** If flex-direction has been set to column, then the cross-axis would now flow from left to right. Meaning that align-items would now be distributing the items in a horizontal fashion.

#### **Align-content**

This property is similar to and can be easily confused with `align-items` . The purpose of this property is to determine how space between **rows** in a flex-container should be distributed along the **cross-axis**.

While `align-items` targets space between flex-items, `align-content` targets rows between the items. The default value for `align-content` is `stretch`.

![Image](https://cdn-media-1.freecodecamp.org/images/pZQxtxQPOFGOo3nPI0PP30dtSV2Kh1JWTvPq)
_1. align-content: stretch;_

![Image](https://cdn-media-1.freecodecamp.org/images/AXH1xvGBA0saPyjQlkhPB2o1SY7aKfZLMm9W)
_2. align-content: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/YVJtoXcCmR-mdR-uwSOhxzeiLEa2n1NH2Nme)
_3. align-content: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/2jTX6X2VKk4hfSDlompfbhWgztGhR6DqKj55)
_4. align-content: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/dw1WSjk4n8X4jzjFdvA1arNDP4QFMuH06RJ3)
_5. align-content: space-between;_

![Image](https://cdn-media-1.freecodecamp.org/images/mjZp6dQV9Oj5SgdEEL1GMVnTbGHwmr7HuOTq)
_6. align-content: space-around;_

#### **Flex Item Properties**

Time to move on to the second type of flexbox properties which allows us to target the individual items inside of a flex container.

#### **Align-self**

This property allows you to align an individual flex item along the **cross-axis.** It overrides the alignment set to the container through `align-items`.

It also takes the same properties as `align-items` (see above).

![Image](https://cdn-media-1.freecodecamp.org/images/lKmArHZGlbeWX8q3SWuUZeUuZjRRYUEizomC)
_align-items set to flex-start on the parent container_

![Image](https://cdn-media-1.freecodecamp.org/images/31G-EGLQX5w5cl4Xlg1s-iEEr72aVEYDuNLw)
_align-self set to flex-end on the orange box_

#### **Order**

This property allows us to re-order the positions of individual flex-items inside of their flex-container. By default, all items have a value of 0 assigned to them.

By assigning a value lower (-ve) or bigger (+ve) through `order` on the individual items, that specific item will move to be positioned according to their values.

The order will follow the most logical convention, that is -ve, 0, +ve. The lowest number will go to the far left and the biggest number to the far right, assuming that everything else is set as default. If there are items which haven’t been assigned any new value, they remain as 0.

![Image](https://cdn-media-1.freecodecamp.org/images/p5hJHrSBtqC3d5d3-t2auhtwh37l35V0YQoe)
_default — everything has a value of 0_

![Image](https://cdn-media-1.freecodecamp.org/images/WlPCp0vPzXCHcLcjgaRXctU1iQT7nC0WT9fd)
_setting order: -1 on box 4_

![Image](https://cdn-media-1.freecodecamp.org/images/rtghkbKFnM3NgK0pCXXwKrpe9LW7qnTr0YYP)
_setting order: 1 on box 3_

**Note:** The boxes, 1, 2, 5 and 6 in the example above are all still at the default value of 0. To clarify, the six boxes above have the following values: -1, 0, 0, 0, 0, 1.

If you want to place a box in front of box number 4, then you need to set your targeted box at an order of -2 or lower.

#### **Flex-basis, Flex-grow, and Flex-Shrink**

So far, all of the flex-items were equal in size. Let’s now look at how we can make a specific flex-item take up more space inside of a flex-container as compared to the other items inside of the same container.

#### **Flex-basis**

This property specifies the **ideal** size of a flex item **before** it is placed into a flex container. It works similarly to width when working with rows. It works like height when working with columns. So if we are working with columns, and an item has been given both height and flex-basis, the flex-basis will take priority as it is the **ideal** height that a flex-item will take if there is enough space available.

That being said, if there is not enough space, and no height or width assigned to the items. The items will take the max-height or max-width available in the container.

![Image](https://cdn-media-1.freecodecamp.org/images/jhEltaPaYIgLk5dDIzeaVAWkZUWyW71l7jQx)
_width of 200px and no flex-basis set_

![Image](https://cdn-media-1.freecodecamp.org/images/79Y4saDm3ADVxjuZy7RmUACikbrAbVPPdmId)
_width of 200px and flex-basis of 300px. Flex-basis wins_

![Image](https://cdn-media-1.freecodecamp.org/images/fr6HCB5oC0BCaxf1GZUG638mp-6H4NudU4kZ)
_flex-basis set to 500px. Items are smaller than 500px wide but take entire space of container_

![Image](https://cdn-media-1.freecodecamp.org/images/TC0UiVqY16oOjATjUiDoZAauk3ZBtXFLnzov)
_columns, height set to 50px each, no flex-basis_

![Image](https://cdn-media-1.freecodecamp.org/images/Kju4X3NJxGMnfKBUAV9tMmZwzufsOjyHX-j4)
_columns, height set to 50px and flex-basis set to 100px. Flex-basis wins._

#### **Flex-grow**

This property determines how the flex-items can grow in order to fill in the unused space in a flex-container.

If we assign a `flex-grow: 1` to all boxes, they will all take the remaining space evenly which is also its default value. The number can be anything, as long as they are all the same number.

If we give `flex-grow: 1` to one item and give a second one a `flex-grow: 2` , then the second item will take two times as much unused space as compared to the first one.

This applies to both rows and columns.

![Image](https://cdn-media-1.freecodecamp.org/images/nW-U0oAU8JJRaniQ7fAI7X8RlvsIjHxmjFh1)
_width set to 200px, no flex-grow_

![Image](https://cdn-media-1.freecodecamp.org/images/arjSqUCpl4KspxFj7ZOYkMliIdniKFuDtocZ)
_flex-grow set to 1 on the red box only_

![Image](https://cdn-media-1.freecodecamp.org/images/M07dCm22-YEm5EpIuPlxnAEXmv9qyGhweEIw)
_flex-grow set to 1 on both boxes_

![Image](https://cdn-media-1.freecodecamp.org/images/0FlgJ8zigEsdOUvE-BEEFdyJuQUfjFki6FIt)
_flex-grow set to 1 on the red box and 6 on the orange box._

#### **Flex-shrink**

This property determines how the flex-items can shrink whenever there is **not** enough space in a flex-container.

The `flex-shrink: 1` is the default value, meaning that all items will shrink at the same rate by default.

**Note: `flex-shrink: 0;`** means that this specific item should never shrink.

`flex-shrink: 2;` means that this specific item should shrink faster than the other ones at `flex-shrink: 1;`

![Image](https://cdn-media-1.freecodecamp.org/images/RI3cY04kjXpppx76-Ay8VqRjrtmp-pgxnHGN)
_no flex-shrink. width of items bigger than container_

![Image](https://cdn-media-1.freecodecamp.org/images/XB8ZKK8OgUZxvG0XrxjclymxPbQiizei8k4u)
_flex-shrink:2 on the red box_

![Image](https://cdn-media-1.freecodecamp.org/images/7yqbRNkF8bidJxgFfkqxPyv5U66aLw8ImY1-)
_flex-shrink: 4 on the red box_

#### **Flex**

This is the shorthand version for flex-grow, flex-shrink and flex-basis in that particular order.

If you need to use all of the three above, you could simply use something like this:

`flex: 0 2 200px;` where 0 refers to the flex-grow, 2 refers to flex-shrink and 200px refers to flex basis respectively.

### **Congratulations!**

That’s it! These are the key ingredients to becoming a flex master. And like for every other thing in life and in code, practice makes perfect. I highly recommend putting this guide into practice to get a practical understanding. One example could be to start with something small like a simple navigation bar.

You can also check out [the link to my Codepen collection on flex-box](https://codepen.io/collection/DrwYRr/) which I used to create those flexboxes in the images above and tweak them to see how they change.

Thank you for reading this guide on flexbox. I hope that it was helpful and informative. If you have any questions or want to share your thoughts on this topic, please feel free to reach out through the comments section or by email at _maudarbocus.zeeshaan@gmail.com_

If you found this read valuable, please show this article some love, by leaving some claps behind, so that other developers can find it too.

[**ZeeshaanMaudar - Overview**](https://github.com/ZeeshaanMaudar)  
[_Code for fun Code for a change Code for social good - ZeeshaanMaudar_github.com](https://github.com/ZeeshaanMaudar)

