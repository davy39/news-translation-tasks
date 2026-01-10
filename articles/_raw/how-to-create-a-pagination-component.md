---
title: How to create a pagination component
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-12T12:38:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-pagination-component
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/how-to-create-a-pagination.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Pagination
  slug: pagination
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
seo_title: null
seo_desc: 'By Florin Pop

  The theme for week #17 of the Weekly Coding Challenge is:

  Pagination

  A Pagination Component is used on websites where you have more content available
  than you want to display at one time to the user so you''d split it on multiple
  pages. ...'
---

By Florin Pop

The **theme** for week #17 of the [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) is:

## Pagination

A Pagination Component is used on websites where you have more content available than you want to display at one time to the user so you'd split it on multiple pages. By separating the content on different pages you are also saving a lot of bandwidth for the user because it won't be required to download all the information at once.

Some **examples** where you'd have a pagination: a blog with multiple pages, an online store with multiple products, etc.

In this article we're going to build this [Pagination Component](https://codepen.io/FlorinPop17/full/BgrvgX/):

%[https://codepen.io/FlorinPop17/pen/BgrvgX/]

**Note**: the pagination is not functional, it's just for demo purposes (the visual). As an extra challenge, you can link this on a real website. 

## The HTML

For the HTML structure we're going to use an `ul` as a wrapper with multiple `li`s. Each `li` will have an `a` tag within it because it's clickable (and semantic) and it'll send the user to the required page (if needed).

We're also using [FontAwesome](https://fontawesome.com/) for the icons (left, right and the dots icons).

```html
<ul class="pagination">
	<li>
		<a href="#"><i class="fas fa-chevron-left"></i></a>
	</li>
	<li>
		<a href="#"><i class="fas fa-ellipsis-h"></i></a>
	</li>
	<li><a href="#">2</a></li>
	<li class="active"><a href="#">3</a></li>
	<li><a href="#">4</a></li>
	<li><a href="#">5</a></li>
	<li>
		<a href="#"><i class="fas fa-ellipsis-h"></i></a>
	</li>
	<li>
		<a href="#"><i class="fas fa-chevron-right"></i></a>
	</li>
</ul>
```

As you can see I also added an `.active` class to one of the `li`s - this is just to highlight the page we are on.

## The CSS

I'm going to paste the CSS and we'll discuss the important pieces afterwards.

```css
.pagination {
	border: 2px solid #aaa;
	border-radius: 4px;
	display: flex;
	list-style-type: none;
	overflow: hidden;
	padding: 0;
}

.pagination li {
	background-color: #fff;
}

.pagination li:hover,
.pagination li.active {
	background-color: #aaa;
}

.pagination li a {
	color: #555;
	display: block;
	font-weight: bold;
	padding: 10px 15px;
	text-decoration: none;
}

.pagination li:hover a,
.pagination li.active a {
	color: #fff;
}
```

Things to note:

1. The `ul` / `.pagination` it's a **flex** container - this is because it's much easier to position the `li`s within it by using flexbox (and who doesn't like flexbox? ?)
2. Because we have a little bit of a `border-radius` on the `ul` we need to add `overflow: hidden` because otherwise the `li`'s corner will be visible on top of the border of the `ul` (remove the overflow and you'll see what I mean)
3. We have the same styling on `li:hover` as on `li.active`, but you can differentiate between these to states if you want

Other than that, I believe it's pretty straightforward, but if you have any questions please let me know. ?

## Conclusion

There are other variants of paginations out there on the web. Find one you like and convert it to code.

Make sure you share with me what you've built!

Happy Coding! ?

  

