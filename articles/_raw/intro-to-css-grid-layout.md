---
title: An Introduction to CSS Grid Layout (with Examples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-26T16:15:21.000Z'
originalURL: https://freecodecamp.org/news/intro-to-css-grid-layout
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1_4O4lprdERnQvKFbdbZPIig-1.jpeg
tags:
- name: CSS Grid
  slug: css-grid
seo_title: null
seo_desc: "By Zafar Saleem\nCSS Grid has taken over the world of web design. It’s\
  \ really cool. There are plenty of tutorials, blogs and articles on the internet,\
  \ which are great sources of knowledge. \nBut the majority of them teach you the\
  \ basics with very few r..."
---

By Zafar Saleem

CSS Grid has taken over the world of web design. It’s really cool. There are plenty of tutorials, blogs and articles on the internet, which are great sources of knowledge. 

But the majority of them teach you the basics with very few real examples. So in this guide, we'll look at examples as we learn.

## What is Grid?

CSS Grid allows us to write better layouts using the in-browser capability of grids. Prior to CSS Grid, we either had to use our own custom grid system or something like Bootstrap. 

These other options work fine, but CSS grid takes the pain out of most of the things we faced in those solutions.

CSS Grid makes it a piece of cake to develop simple and complex layouts. In this blog we will learn some basic terminologies and then go ahead with a simple layout example.

## Basic Terminologies

The basic terms associated with CSS Grid are as follows:

1. Columns
2. Rows
3. Cells
4. Grid Lines
5. Gutter

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_B80r8wi2JB9HIrCIYJggxg.png)

All the terms are explained in the diagram above. This example is a 3x2 column grid, which means 3 columns and 2 rows.

## Example Layout

Now that the basic concepts are out of the way, we are going to use these concepts to make an example layout like the below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_4VirrlRLYMrFWwmp852N3A.png)

As you can see, there is a header and a footer. Then the center row has 3 columns with nav in the first column sidebar on the right, and the main content area in the center (which occupies most of the row).

Below is the sample HTML for this example.

```html
<div class="wrapper">
  <header class="items">HEADER</header>
  <nav class="items">NAV</nav>
  <div class="items contents">CONTENTS</div>
  <aside class="items">ASIDE</aside>
  <footer class="items">FOOTER</footer>
</div>
```

Now that the HTML is out of our way, let's dig into the CSS. First and foremost, let's give it some styling so that our HTML looks like the above. These CSS rules are not part of CSS grid, so you can omit them if you want.

```css
.wrapper * {
  background: orange;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1px;
  margin-right: 1px;
}
```

As you can see, I am styling all the items inside a wrapper container. I am setting its background color to `orange` and giving `bottom` and `right` `margins.` I'm setting `display` `flex` just to align items dead center by setting `justify-content` and `align-items` to `center`.

Next, let's get into the CSS Grid part of it.

```css
.wrapper {
  display: grid;
  grid-template-columns: 1fr 5fr 2fr;
  grid-template-rows: 5fr 20fr 5fr;
  grid-gap: 10px;
  height: 720px;
}
```

In the above piece of code we are setting `display` to `grid` – hence the title of this topic. That is how we convert a container into `grid`. 

Next we set the columns and rows. We'll do this by using the `grid-template-columns` and `grid-template-rows` properties. `grid-template-columns` allows us to set the number of columns with their appropriate `width`. `grid-template-rows` allows us to set the number of `rows` with their appropriate `height`. 

In the example above, there are 3 columns with first column taking `1 fraction` , the second column taking `5 fraction`, and the third column `2 fractions`. A single fraction unit means _“one piece of however many pieces we are splitting this into”_.

If you look at the same example above the same concept applies to `rows`. There are three rows, and the first row contains the `header` which takes the entire row across all three columns. The second row takes the nav, contents, and aside, whereas the footer goes to the third and last row and takes up all three columns.

This means the first and last rows take up the same amount of height, that is `5 fractions`. And the center row takes up the rest of the remaining height.

Next we will also create a gutter of 10px. We can do this in CSS Grid by using the `grid-gap` property. Lastly, we set a height for our wrapper container.

If we take a look at it in the browser we'll get the result we're looking for:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_YpRMEUzHN96jqnQf8AVEow.png)

Now let's make it look more like we want it to look by setting some properties for the header and footer. We are going to tell the header and footer to take up their entire rows.

We'll do this by using the `grid-column-start` and `grid-column-end` properties, like this:

```css
header {
  grid-column-start: 1;
  grid-column-end: 4;
}

footer {
  grid-column-start: 1;
  grid-column-end: 4;
}
```

As you can see, both the header and footer start from `grid line` 1 and end at `grid line` 4. This allows them to take up their entire rows. This will yield the exact output we are looking for, as below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_4VirrlRLYMrFWwmp852N3A--1-.png)

## Complete Code

```html
<!DOCTYPE html>
<html>
<head>
	<title>CSS Grid</title>
	<style type="text/css">
		.wrapper {
			display: grid;
			grid-template-columns: 1fr 5fr 2fr;
			grid-template-rows: 5fr 20fr 5fr;
			grid-gap: 10px;
			height: 720px;
		}

		header {
			grid-column-start: 1;
			grid-column-end: 4;
		}

		footer {
			grid-column-start: 1;
			grid-column-end: 4;
		}

		.wrapper * {
			background: orange;
			display: flex;
			justify-content: center;
			align-items: center;
			margin-bottom: 1px;
			margin-right: 1px;
		}
	</style>
</head>
<body>
	<div class="wrapper">
		<header class="items">HEADER</header>
		<nav class="items">NAV</nav>
		<div class="items contents">CONTENTS</div>
		<aside class="items">ASIDE</aside>
		<footer class="items">FOOTER</footer>
	</div>
</body>
</html>
```

That is it for this article. You can follow me [here](https://www.freecodecamp.org/news/author/zafar/) for more articles. If you liked it, don’t forget to share it on social media.

