---
title: Here's a Free Course to Help Front End Developers Learn Math
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-25T15:05:47.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-practical-math-for-front-end-developers-heres-our-free-11-part-course-by-radical-coder
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-23-at-16.49.35.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: Scrimba
  slug: scrimba
seo_title: null
seo_desc: 'By Per Harald Borgen

  Are you looking to become a more effective developer by improving your fundamental
  math skills without reaching for NASA-level calculations? Look no further!

  At Scrimba, we''re are really excited to announce our new course ''Practi...'
---

By Per Harald Borgen

Are you looking to become a more effective developer by improving your fundamental math skills without reaching for NASA-level calculations? Look no further!

At Scrimba, we're are really excited to announce our new course ['Practical Math for Front-End Developers'](https://scrimba.com/course/gpracticalmath), which offers exactly that. In the course we build 3 projects:

1. A Shopping Cart, where we generate a list of products, calculate the total price of the products and apply a tax rate.
2. A Weekly Schedule, where we introduce the `Date` object, perform layout manipulation and learn about the `reduce` function.
3. A Monthly Expense Sheet, which brings together everything we've learned and gives us a few handy tips and tricks.

This course is brought to you by Ryan Gonyon, who has his own [Twitch](https://www.google.com/url?q=https://www.twitch.tv/radicalcoder&sa=D&ust=1585686482555000&usg=AFQjCNHoQP_okALIk85y1YojlBM-DwEiHw) and [YouTube](https://www.google.com/url?q=https://www.youtube.com/channel/UC2J1l95xB98Fd-v9xGkxHIg&sa=D&ust=1585686482556000&usg=AFQjCNGzqdwTLYFINOKqnrb4a0XgwxY_DA) channels.

With 5 years of Web Dev experience, a B.S. in Computer Science, and experience tutoring K-12 and University-level math, Ryan is the perfect tutor for this course. Head over to [Scrimba](https://scrimba.com/playlist/pzKyeuP?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) to see what he has in store!

# App Layout and CSS calc() Introduction

[![Site header, main and footer](https://dev-to-uploads.s3.amazonaws.com/i/6ox8mhsqz51nnxda6q0t.png)](https://scrimba.com/p/pzKyeuP/c73zJGtp?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

In this screencast, Ryan shows us how to build the outer shell of our applications by correctly sizing the `<header>`, `<footer>` and `<main>` tags with CSS variables and the `calc()` function.

We use `overflow-y: auto`; to ensure that the contents of the `<main>` tag do not extend over the footer.

```css
* {
	--headerFontSize: 2rem;
	--headerPadding: 0.5rem;
	--footerFontSize: 1rem;
	--footerPadding: 1rem;
}

header {
	font-size: var(--headerFontSize);
	padding: var(--headerPadding);
}

main {
	font-size: 1.5rem;
	height: calc(
		100vh - var(--headerFontSize) - (2 * var(--headerPadding)) - var(
				--footerFontSize
			) - (2 * var(--footerPadding))
	);
	overflow-y: auto;
}

footer {
	font-size: var(--footerFontSize);
	padding: var(--footerPadding);
}
```

# The roll() Function

At some point during your front-end journey, it will be useful to generate random data to test your layouts. The `roll()` function does exactly that. This cast also shows us how to use JavaScript's `Math` module and `random()` function.

```js
function roll(min, max, floatFlag) {
	let r = Math.random() * (max - min) + min;
	return floatFlag ? r : Math.floor(r);
}
```

# Shopping Cart - Generate Data / Build Layout

[![Finished Shopping Cart layout](https://dev-to-uploads.s3.amazonaws.com/i/bd17qggr11kjt0mwjsib.png)](https://scrimba.com/p/pzKyeuP/cn4kQnUK?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

Now we start building our first project, the Shopping Cart, using our newly written `roll()` function to generate prices. This shows us how much time we save using our new knowledge!

```js
let products = [...Array(5)].map((_, i) => {
	return {
		index: i,
		title: possibleProducts[roll(0, possibleProducts.length)],
		price: roll(1, 10, 1).toFixed(2),
		count: roll(1, 6),
	};
});
```

# Shopping Cart - Calculate Total / Apply Tax Rate

In this screencast, we learn how to use `.reduce` to calculate the total price of the cart

```js
let cartTotal = products
	.reduce(function (accumulator, product) {
		console.log(accumulator, product);
		return accumulator + parseFloat(product.price) * product.count;
	}, 0)
	.toFixed(2);
```

We also see how to use `roll()` to generate a random tax rate and apply it.

```js
let taxRate = roll(5, 9, 1).toFixed(1);
```

Along the way, we practise parsing float values and rounding them to a specified number after a decimal point.

# Shopping Cart (Bonus Challenge) - Weights

As a bonus challenge in this cast, we randomly generate the weight of each item in our shopping cart and calculate the total weight at the checkout. In the real world, this could be used to estimate the shipping cost for the buyer.

No spoilers here, so if you want to see the solution you'll have to click through [to the course.](https://scrimba.com/p/pzKyeuP/ce99mQsa?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) ?

# A Brief Exploration of CSS Shapes

[![Rendered shapes built with CSS](https://dev-to-uploads.s3.amazonaws.com/i/afroa8rcp6hv0g24aej2.png)](https://scrimba.com/p/pzKyeuP/cGmWKMfR?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

In this cast, we learn how to create a square, a circle, a diamond and a triangle with CSS shapes.

```css
.triangle {
	height: 0;
	width: 0;
	border-left: 5.5rem solid transparent;
	border-right: 5.5rem solid transparent;
	border-bottom: 5.5rem solid black;
	margin: 1rem;
	position: relative;
}

.triangle:after {
	content: "";
	position: absolute;
	height: 0;
	width: 0;
	border-left: 4.5rem solid transparent;
	border-right: 4.5rem solid transparent;
	border-bottom: 4.5rem solid red;
	left: -4.5rem;
	top: 0.6rem;
}
```

# Weekly Schedule - Using Date() to Build Week / Generating Tasks

In this cast, we start work on our Weekly Schedule app. First up, we learn about JavaScript's `Date` object.

```js
function getNextDay(day) {
	let nextDay = new Date(day);
	nextDay.setDate(day.getDate() + 1);
	return nextDay;
}
```

Next, we look at using the `roll()` function to test the layout and produce a list of tasks. Take a look [at the course](https://scrimba.com/p/pzKyeuP/c2KKPGh6?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) to see how it works

# Weekly Schedule - Build Layout / Display Data

[![Weekly Schedule app](https://dev-to-uploads.s3.amazonaws.com/i/uezalgp2o5marghv69gs.png)](https://scrimba.com/p/pzKyeuP/caZZyNA9?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

In this cast, Ryan shows us how to use the `calc()` function to display the data generated in the previous cast.

```css
--mainHeight: calc(
	100vh - var(--headerFontSize) - (2 * var(--headerPadding)) - var(
			--footerFontSize
		) - (2 * var(--footerPadding))
);
```

We also learn how to cross out completed tasks ([click through](https://scrimba.com/p/pzKyeuP/caZZyNA9?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) to find out how.) The result is a clean, functional app that we can use in everyday life.

# Monthly Expense Sheet - Generate and Display Month

[![Grid display](https://dev-to-uploads.s3.amazonaws.com/i/a6you8qo65mq9smjyhrv.png)](https://scrimba.com/p/pzKyeuP/cD44VpTW?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

Next, use the concepts from the previous casts to build something more complex - our expenses tracker. In this project we generate data, display months and draw up a grid.

```js
function displayMonth(month) {
	// <div class="day">3</div>
	let monthHtml = month.reduce(function (accumulator, day) {
		return accumulator + `<div class="day">${day.date.getDate()}</div>`;
	}, "");
	document.getElementById("MonthlyExpenses").innerHTML = monthHtml;
}
```

# Monthly Expense Sheet - Generate, Display, and Track Expenses

[![Monthly Expense Sheet app](https://dev-to-uploads.s3.amazonaws.com/i/kb2kp4o9k4p6mwlvi0hl.png)](https://scrimba.com/p/pzKyeuP/cD4weyhd?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Click the image to access the course._

In the final cast, we perform budget calculations by writing functions to track our expenses, rent and utility bills. We then display the expenditures alongside the remaining available budget.

```js
function displayMonth(month, budget, netValue) {
	let monthHtml =
		`<div class="monthly-summary">
        Budget: \$${budget.toFixed(2)} | Net Value: \$${netValue.toFixed(2)}
    </div>` +
		month.reduce(function (accumulator, day) {
			return accumulator + `<div class="day">${day.date.getDate()}</div>`;
		}, "");
	document.getElementById("MonthlyExpenses").innerHTML = monthHtml;
}
```

# Conclusion

Well done for finishing this course, I really hope you have learned some useful tips and tricks that you can apply in your future coding adventures!

Happy learning ;)



