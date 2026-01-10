---
title: Learn the Bootstrap 4 Grid System in 10 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T21:17:11.000Z'
originalURL: https://freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9nkJt3S1Fe_KMkDtpIhgXw.png
tags:
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Elena-Cristina Conacel

  The Bootstrap 4 Grid System is used for responsive layouts.

  A responsive layout represents the way elements align in the page on different resolutions.
  It is important you understand how to use the grid before learning about...'
---

By Elena-Cristina Conacel

The Bootstrap 4 Grid System is used for responsive layouts.

A responsive layout represents the way elements align in the page on different resolutions. It is important you understand how to use the grid before learning about any other Bootstrap 4 component, because whatever element you use, you will need to place it somewhere on the screen.

Let’s get started!

![Image](https://cdn-media-1.freecodecamp.org/images/bIvdmOpWL2YSwkrfoTrOUWMPwyhyjhgyDDND)
_Photo credit to [shot](https://dribbble.com/animade" rel="noopener" target="_blank" title="">Animade </a>for his <a href="https://dribbble.com/shots/4948320-Computer-Mouse" rel="noopener" target="_blank" title=")._

### Table of Contents

* [Bootstrap 4 Containers](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-containers)
* [Bootstrap 4 Rows](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-rows)
* [Bootstrap 4 Columns](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-columns)
* [Further Reading](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#further-reading)

The Bootstrap 4 grid consists of containers, rows and columns. We will take them one by one and explain them.

### Bootstrap 4 Containers

A Bootstrap 4 container is an element with the class `.container`. The container is the root of the Bootstrap 4 grid system and it is used to control the width of the layout.

The Bootstrap 4 container contains all the elements in a page. This means your page should have the following structure: first the body of the HTML page, inside of it you should add the container and all the other elements inside the container.

```html
<body>
   <div class="container">
    ...
   </div>
</body>
```

The simple `.container` class sets the width of the layout depending on the width of the screen. It places the content in the middle of the page aligning it horizontally. There is equal space between the Bootstrap 4 container and the left and the right edge of the page.

The `.container` scales down in width as the screen width narrows and becomes full-width on mobile. The width of the container is defined inside the Bootstrap 4 library for every screen size. You can see the exact [sizes here](https://getbootstrap.com/docs/4.1/layout/grid/#grid-options).

A full-width container takes 100% of the screen size regardless of the screen width. To use it you need to add the class .`container-fluid`.

![Image](https://cdn-media-1.freecodecamp.org/images/1rf1sYoCfHD8IlHcFIed9qH5pttf4Bf1KSsw)

```html
<div class="container">
  Hello! I am in a simple container.
</div>

<div class="container-fluid">
  Hello! I am in a full-width container.
</div>
```

You can view the CodePen [here](https://codepen.io/cristinaconacel/pen/XBLVre).

To see the differences between the two types of containers, you can open the pen in your console and switch between screen sizes.

### Bootstrap 4 Rows

Bootstrap 4 rows are horizontal slices of the screen. They are used only as wrappers for columns. To use them, you need the `.row` class.

```html
<div class="row">
  ...
</div>
```

Here are the most important things you need to remember about Bootstrap 4 rows:

* **They are only used for containing columns.** If you place other elements inside the row along with columns you will not get the expected result.
* **They have to be placed in containers.** If you don’t do this, you will get a horizontal scroll on your page. This happens because rows have negative left and right margins of 15. The container has 15px paddings so it counteracts the margins.
* **The columns have to be children of the row.** Otherwise they will not align. The rows and columns are created to work together in this strict hierarchy.

### Bootstrap 4 Columns

We can now get to the nice part of this tutorial, the Bootstrap 4 columns. Columns are great! They help you divide the screen horizontally.

If you place a single column in your row, it will take up all the width. If you add two columns, they will each take 1/2 from the width. And so it goes for any number of columns.

![Image](https://cdn-media-1.freecodecamp.org/images/aaNpgARcShivW4WorInpghjdLbX7Jiohd2DA)

```html
<div class="container">
  <div class="row">
    <div class="col">
      ...
    </div>
  </div>
  <div class="row">
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
  </div>
  <div class="row">
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
    <div class="col">
       ...
    </div>
  </div>
</div>
```

_You can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/NOLEyy)._

**Side note:** Columns are not coloured. I just added colours for a more visually compelling description/so they look pretty.

### **Setting Sizes for Columns**

Using the `.col` class sets the width for the column dynamically. That means that depending on the number of columns in a row, the width of a column will be the width of the container divided by the number of columns.

But there is another way to define columns. You can use classes for columns and define their size.

By default, the Bootstrap 4 grid consists of 12 columns. You can select any size from 1 to 12 for your column. If you want 3 equal columns, you can use `.col-4` for each one (because 3*4 cols each = 12). Or you can set different sizes for them. Here are some examples:

![Image](https://cdn-media-1.freecodecamp.org/images/3ib3OrRrGbxeQNZengIzNKNf4Pkm3nYuVGW8)

```html
<div class="row">
  <div class="col-6">
    ...
  </div>
  <div class="col-6">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-5">
    ...
  </div>
  <div class="col-7">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-3">
    ...
  </div>
  <div class="col-4">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-6">
    ...
  </div>
  <div class="col-7">
     ...     
  </div>
</div>
```

You can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/xyaQNw).

If the sum of the cols in your row doesn’t get to 12, then they don’t fill the whole row. If the sum of the columns goes beyond 12 then it will move to the next line. The first line will only display the first elements that add up to 12 or lower.

### Setting Breakpoints for Columns

If you take the example above and want to display it on mobile, you may run into some problems. Displaying five columns on mobile will make the content unreadable.

This is where one of the most powerful Bootstrap 4 components comes into play. In order to have different layouts on different screens you won’t need to write media queries, instead you can use the column breakpoints.

A breakpoint is a Bootstrap 4 variable that stands for a screen resolution. When you are specifying a breakpoint for a class, you are telling the class to be active only for resolutions that are at least as big as the number that the breakpoint holds.

The simplest class that we will learn about is the `.col-[breakpoint]` class. When you use this class, you are defining the behaviour for the columns only when they are displayed on devices that have a resolution of at least the defined breakpoint. Up to the given breakpoint, your columns will align vertically by default. And after your breakpoint, they will align horizontally because of the class.

Bootstrap has 4 breakpoints that you can use:

* `.col-sm` for larger mobile phones (devices with resolutions ≥ 576px);
* `.col-md` for tablets (≥768px);
* `.col-lg` for laptops (≥992px);
* `.col-xl` for desktops (≥1200px)

Let’s say you want to display two columns one after another vertically on small screens and on the same line on bigger screens. You will need to specify the breakpoint where the columns go on the same line.

In our example we will use the `.col-lg` breakpoint and see how the columns look on different screens. For resolutions that are lower than the given breakpoint (<992px) the columns will be displayed vertically. This means that on mobile devices and tablets, the columns will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/JZZ4xgPEjOQ09MBX8NoX65F9XLn4esZ2HnCi)
_The display for resolutions &lt; 992px (mobile devices)._

And for devices that have a resolution that is higher or equal to the breakpoint (≥992px) the columns will go on the same row. This means that on laptops and desktops you will get this result:

![Image](https://cdn-media-1.freecodecamp.org/images/YCvBIbCtFgLI9Ret9gwVbnkNxuu1wk8EjR-l)
_The display for resolutions &gt;= 992px (laptops and bigger screens)._

```html
<div class="row">
 <div class="col-lg">
   ...
 </div>
 <div class="col-lg">
    ...   
 </div>
</div>
```

You can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/OBoqqz). If you open the Codepen in another window and see the page at different resolutions, you will see the columns change their positioning.

If you wanted for the 2 columns to go on the same line starting with larger mobile phones you would use `.col-sm`, for tablets `.col-md` and for extra large screens `.col-xl`.

### **Setting Sizes and Breakpoints for Columns**

You can combine the sizes and breakpoints and use a single class with the format `.col-[breakpoint]-[size]`.

For example, if you want three columns of different sizes to align on a row starting with the laptop resolution you need to do this:

```html
<div class="row">
  <div class="col-lg-4">
    ...
  </div>
  <div class="col-lg-3">
    ...
  </div>
  <div class="col-lg-5">
    ...     
  </div>
</div>
```

You will get this result on resolutions <992px:

![Image](https://cdn-media-1.freecodecamp.org/images/KH7dwBmHGHssTgFII9tlk0IlzJ2lTFjoDuY1)

And for screens that are ≥992px:

![Image](https://cdn-media-1.freecodecamp.org/images/xLOVbs29mzGIiSe9WKNfIUyKwL2fEc6n0pp8)

Again, you can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/ReYOwZ).

But what if you want to display one column per row on small mobile resolutions, two columns per row on tablets and four on laptops or devices with higher resolutions?

Then you add multiple classes for a single column to describe the behaviour for every resolution. Using multiple classes, you specify that the content will take six slots on tablets and three on laptops.

```html
<div class="row">
  <div class="col-sm-6 col-lg-3">
    ...
  </div>
  <div class="col-sm-6 col-lg-3">
    ...
  </div>
  <div class="col-sm-6 col-lg-3">
     ...     
  </div>
  <div class="col-sm-6 col-lg-3">
     ...     
  </div>
</div>
```

The result will show like this on tablets:

![Image](https://cdn-media-1.freecodecamp.org/images/8Ub6sFDws2UJO8qyLNx3zXiWMylQWpIeLPyX)

And like this on laptops and higher resolutions:

![Image](https://cdn-media-1.freecodecamp.org/images/hVaaOjxUkTRDXBpyKNRBIZt6mzerVq-UoFHO)

This example is also live on [CodePen](https://codepen.io/cristinaconacel/pen/mjZBPO).

As an exercise, you can try and create rows with different number of columns depending on the screensize and verify the behaviour in your browser console.

### **Offsetting Columns**

If you don’t want your columns to be next to each other, you can use the class `.offset-[breakpoint]-[size]` together with the `.col-[breakpoint]-[size]`.

Using this class is the same as adding an empty column before your column. Here is a simple example:

![Image](https://cdn-media-1.freecodecamp.org/images/b7dxvLZ2St8xI37XTc0R8kFvdfae2Zjvqbmf)

```html
<div class="row">
  <div class="col-md-4 offset-md-4">
     ...     
  </div>  
  <div class="col-md-4">
     ...     
  </div>  
</div>
```

You can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/KGxYaL).

You can use the class on any column in the row. Here are some more examples:

![Image](https://cdn-media-1.freecodecamp.org/images/tem6Qp-WqVavEKizT-OIshNBMSDDrSVP3wIY)

```html
<div class="row">
  <div class="col-md-4">
     ...     
  </div>  
  <div class="col-md-4 offset-md-4">
     ...     
  </div>  
</div>
<div class="row">
  <div class="col-md-4 offset-md-2">
     ...    
  </div>  
  <div class="col-md-4 offset-md-2">
     ...     
  </div>  
</div>
<div class="row">
  <div class="col-md-6 offset-md-3">
     ...
  </div>   
</div>
```

### **Nesting Columns**

This may come as a surprise, but you can add a row inside a column!

The row in question (which will have the width of its parent column) will then be divided into 12 (smaller) columns that you can reference through the `.col-*` classes.

Let’s take a look at what happens when we insert a new row inside a column:

![Image](https://cdn-media-1.freecodecamp.org/images/SiRLnZuYJJqLeAK2eN42Xhb9dZz9s87wDaN7)

```html
<div class="row">
    <div class="col-md-8">
        ...
        <div class="row">
            <div class="col-md-5">
               ...
            </div>
            <div class="col-md-7">
               ...   
            </div>
        </div>
      </div>     
    </div>
    <div class="col-md-4">
       ...
    </div>
</div>
```

You can see the code live on [CodePen](https://codepen.io/cristinaconacel/pen/OBoGZr).

Knowing this, you can go many levels deep to organise your information. The columns will provide a simple way for you to manage your space.

This wraps up the basic knowledge regarding the Bootstrap 4 responsive grid system. If you have questions, please let me know in the comments, I will be glad to answer.

### Further Reading

If you have more time, here are some useful resources:

* [Official Grid Documentation](https://getbootstrap.com/docs/4.1/layout/grid/) from GetBootstrap
* [Video Tutorial](https://scrimba.com/p/pD5KUE/cdm3asD) from Scrimba

This article was initially posted on the [BootstrapBay Blog](https://bootstrapbay.com/blog/day-2-bootstrap-4-grid-system-tutorial-examples/). It is part of a larger series of Bootstrap 4 tutorials called [14 Days of Bootstrap 4](https://bootstrapbay.com/blog/14-days-bootstrap-4/). If you want to continue learning about the Bootstrap 4 components, these articles are a good place to start.

And if you want to jump start your development with a Bootstrap template, you can check out our [marketplace](http://bootstrapbay.com).

But before delving deeper, take a moment to celebrate your newly acquired skills!?

![Image](https://cdn-media-1.freecodecamp.org/images/gS3FeSJGquHlZEzANXWSsAakOD2FbabpNvD7)
_Photo credit to [shot](https://dribbble.com/jonasmosesson" rel="noopener" target="_blank" title="">Jonas Mosesson</a> for his <a href="https://dribbble.com/shots/4198035-Sweet-Berry-Wine" rel="noopener" target="_blank" title=")._

