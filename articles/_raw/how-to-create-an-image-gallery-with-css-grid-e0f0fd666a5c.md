---
title: How to create an image gallery with CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:50:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2H0HPHmFNs2t78Zog8kd9w.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Image galleries made by websites like Unsplash, Pinterest Etc, are made
  by techniques like positioning or translating the image item which is a very cumbersome
  task to do. You can achieve the same functionality very quickly using CSS Grids.


  For exam...'
---

Image **galleries** made by websites like [Unsplash](https://unsplash.com/), [Pinterest](https://www.pinterest.com/) Etc, are made by techniques like **positioning** or **translating** the image item which is a very cumbersome task to do. You can achieve the same functionality very quickly using **CSS Grids.**

> **For example:** Above is a gallery of images with images of **varying width** and **height** which is a perfect use case for CSS grids.

#### **Let’s get started!**

### The Underlying Grid

Now, let’s create an **8x8 grid**. We can create a grid of other sizes also but that depends on the type of gallery you want. In our case, an **8x8 grid** will be ideal.

* A grid container is defined by setting an element’s **display** property to the **grid**. So, the **div**, with the **class grid** is going to be our **grid** **container.**
* We use the **grid-template-columns** property to set the **column tracks** and **grid-template-rows** to set the **row tracks.** We declare these properties on the grid container. In our example, we will we be making an 8x8 grid container.
* **grid-gap:** It defines the size of the **gap between rows** **and** **columns** in a grid layout. The value for grid gap can be any CSS length unit. In our example, I have given the value of **15px** to make our **grid look** **better**.

**HTML:**

```html
<div class="gallery"></div>
```

**CSS:**

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(8, 5vw);
    grid-gap: 15px;
}
```

> **_Note:_** _The height of the rows is tied to the viewport width, so that the cells maintain its aspect ratio perfectly fine. We have **8 rows** each with the height of **5 viewport width**. I experimented with these heights and came to the conclusion that **5%** of **viewport width** is the **perfect size** for the height. We are doing this by setting the height of the row to **5vw (viewport width)**._

![Image](https://cdn-media-1.freecodecamp.org/images/1*ho1ZrgKcjhTl6EfmTbZvEw.png)
_**8x8 CSS Grid (8 Column Tracks &amp; 8 Row Tracks) with Grid Lines from 1 to 9 (Both Columns &amp; Rows)**_

> **_Note:_** _All **direct children** of **grid** automatically become **grid items**._

### Inserting Grid Items

Now, we will be inserting the grid items inside the grid container:

```html
<div class=”gallery”>
  <figure class=”gallery__item gallery__item--1">
    <img src="img/image-1.jpg" class="gallery__img" alt="Image 1">
  </figure>
  <figure class="gallery__item gallery__item--2">
    <img src="img/image-2.jpg" class="gallery__img" alt="Image 2">
  </figure>
  <figure class="gallery__item gallery__item--3">
    <img src="img/image-3.jpg" class="gallery__img" alt="Image 3">
  </figure>
  <figure class="gallery__item gallery__item--4">
    <img src="img/image-4.jpg" class="gallery__img" alt="Image 4">
  </figure>
  <figure class="gallery__item gallery__item--5">
    <img src="img/image-5.jpg" class="gallery__img" alt="Image 5">
  </figure>
  <figure class="gallery__item gallery__item--6">
    <img src="img/image-6.jpg" class="gallery__img" alt="Image 6">
  </figure>
</div>
```

### Styling Images

```css
.gallery__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

Setting the **object fit** value to **cover** is like setting the **background size** to **cover** for the **background image**. We are doing this so the image can fill the height and width of its box (the grid item), maintaining its aspect ratio.

> **_Note:_** _The object fit property only works if we set the **width** and **height** properties._

![Image](https://cdn-media-1.freecodecamp.org/images/1*FBsVH1n06ufBr_WcB_xDDQ.png)

> **_Note:_** _By default the **grid items** are laid out according to the **grid auto placement rules**._

### **Positioning Grid Items**

Before we start positioning the grid items, we will study a few basics concepts.

The grid **div** is the **grid container**, and all the **direct child** elements are the **grid items**. When we defined the grid tracks with grid-template-columns and grid-template-rows, **grid provided** **us numbered lines called the grid lines** to use for positioning the items. You can refer to each grid line by a numerical index.

**Columns start at one**, from **left** to **right** by default, and **rows** also begin at one from **top** to **bottom**. It takes **two grid lines** to make a single column or row, one line on either side, so our **8-column** and **8-row** grid consist of   
**9-column lines** and **9-row lines**.

The vertical lines **1** and **2** determine the **start** and **end points** of the **first column.** Lines **2** and **3** the **second column** and so on. Similarly, horizontal lines **1** and **2** determine the position of the **first row**, and lines **2** and **3** the second row and so on. Knowing the above concepts will help you understand how we are going to position **items (images)** on our grid.

Now, we will use **grid line numbers** to control how items are placed by applying properties directly to a grid item. We can specify on which line a grid item **starts** and **ends**, and how many tracks it should **expand**.

#### **1st Grid Item**

So let’s create a new rule that targets the first grid item. We’ll first use the **grid-column-start** property to indicate the column grid line where the first grid item starts. The **grid-column-end** indicates where the first grid item ends.

So the grid-column-start **value** is a number that indicates the grid line at the left edge of a column. The grid-column-end **value** indicates the grid line that marks the right edge of the column.

So in the example given below, setting **grid-column-start** to **1** and **grid-column-end** to **3** means that the grid item will stretch from the left edge of the grid line, **line 1** to **line 3**, filling up **2 columns**. We will also use the **grid-row-start** and **grid-row-end** properties to indicate the **grid item start** and **end position** on the **row grid lines** in the same way as we did for the column.

```css
.gallery__item--1 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 3;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ScnDXtFn-7wffVN62rqg5w.png)
_First Item Placement_

> **_Note:_** _Now, we will position other items on the same principles which we learned above._

#### **2nd Grid Item**

```css
.gallery__item--2 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 1;
    grid-row-end: 3;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*U-OLT0CdIjjxvaV-4YpjLg.png)
_Second Item Placement_

#### **3rd Grid Item**

```css
.gallery__item--3 {
    grid-column-start: 5;
    grid-column-end: 9;
    grid-row-start: 1;
    grid-row-end: 6;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wEZB6kvCDGquI_PH1yH4gQ.png)
_Third Item Placement_

#### **4th Grid Item**

```css
.gallery__item--4 {
    grid-column-start: 1;
    grid-column-end: 5;
    grid-row-start: 3;
    grid-row-end: 6;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AkEoMuGUJM5oB7q-2SLnxA.png)
_Fourth Item Placement_

#### **5th Grid Item**

```css
.gallery__item--5 {
    grid-column-start: 1;
    grid-column-end: 5;
    grid-row-start: 6;
    grid-row-end: 9;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0SA_xLddgWzrV7y0hK8kEQ.png)
_Fifth Item Placement_

#### **6th Grid Item**

```css
.gallery__item--6 {
    grid-column-start: 5;
    grid-column-end: 9;
    grid-row-start: 6;
    grid-row-end: 9;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rmUZZ0lsviNcnofEoAnRPw.png)
_Sixth Item Placement_

You can find the complete code below.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300,400,400i|Nunito:300,300i" rel="stylesheet">
        <link rel="stylesheet" href="css/style.css">
        <link rel="shortcut icon" type="image/png" href="img/favicon.png">

        <title>CSS Grids Gallery</title>
    </head>
    <body>
        <div class="container">
            <div class="gallery">
                <figure class="gallery__item gallery__item--1">
                    <img src="img/image-1.jpg" alt="Gallery image 1" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--2">
                    <img src="img/image-2.jpg" alt="Gallery image 2" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--3">
                    <img src="img/image-3.jpg" alt="Gallery image 3" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--4">
                    <img src="img/image-4.jpg" alt="Gallery image 4" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--5">
                    <img src="img/image-5.jpg" alt="Gallery image 5" class="gallery__img">
                </figure>
                <figure class="gallery__item gallery__item--6">
                    <img src="img/image-6.jpg" alt="Gallery image 6" class="gallery__img">
                </figure>
            </div>
        </div>
    </body>
</html>
```

And the CSS:

```css
*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit; 
}

html {
  box-sizing: border-box;
  font-size: 62.5%; 
}

body {
  font-family: "Nunito", sans-serif;
  color: #333;
  font-weight: 300;
  line-height: 1.6; 
}

.container {
  width: 60%;
  margin: 2rem auto; 
}

.gallery {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-template-rows: repeat(8, 5vw);
  grid-gap: 1.5rem; 
}

.gallery__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block; 
}

.gallery__item--1 {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 3;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--2 {
  grid-column-start: 3;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 3;

  /** Alternative Syntax **/
  /* grid-column: 3 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--3 {
  grid-column-start: 5;
  grid-column-end: 9;
  grid-row-start: 1;
  grid-row-end: 6;

  /** Alternative Syntax **/
  /* grid-column: 5 / span 4;
  grid-row: 1 / span 5; */
}

.gallery__item--4 {
  grid-column-start: 1;
  grid-column-end: 5;
  grid-row-start: 3;
  grid-row-end: 6;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 4;  */
  /* grid-row: 3 / span 3; */
}

.gallery__item--5 {
  grid-column-start: 1;
  grid-column-end: 5;
  grid-row-start: 6;
  grid-row-end: 9;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 4; */
  /* grid-row: 6 / span 3; */
}

.gallery__item--6 {
  grid-column-start: 5;
  grid-column-end: 9;
  grid-row-start: 6;
  grid-row-end: 9;

  /** Alternative Syntax **/
  /* grid-column: 5 / span 4; */
  /* grid-row: 6 / span 3; */
}
```

You can try adding your own CSS to make this gallery look the way you want it to look. You can also create more complex image galleries very easily.

You can learn more about the CSS Grids in the link given below

[**A Complete Guide to Grid | CSS-Tricks**](https://css-tricks.com/snippets/css/complete-guide-grid/)  
[_CSS Grid Layout is the most powerful layout system available in CSS. It is a 2-dimensional system, meaning it can…_css-tricks.com](https://css-tricks.com/snippets/css/complete-guide-grid/)

I hope you’ve found this post informative and helpful. I would love to hear your feedback!

**Thank you for reading!**

