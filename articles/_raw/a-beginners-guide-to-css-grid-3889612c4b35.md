---
title: A Beginner’s Guide to CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T02:07:53.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-css-grid-3889612c4b35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Si0jHvuuUWXo0qWXCqx2qg.jpeg
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
seo_desc: 'By Kara Luton

  I first heard about CSS Grid towards the end of 2016. I was sitting at one of my
  first Tech Ladies® meetings and an attendee mentioned hearing how amazing it was.
  Fast forward a year and a half later and I’m finally digging deeper into ...'
---

By Kara Luton

I first heard about CSS Grid towards the end of 2016. I was sitting at one of my first [Tech Ladies®](https://www.freecodecamp.org/news/a-beginners-guide-to-css-grid-3889612c4b35/undefined) meetings and an attendee mentioned hearing how amazing it was. Fast forward a year and a half later and I’m finally digging deeper into Grid. As a devoted Flexbox user, I can already tell how this will be a game changer.

The biggest question I had when beginning to learn about CSS Grid was: how is Grid different than Flexbox? And I found out that in general, Grid can do _everything_ that Flexbox can do. Some people are of the mindset that Grid is for multi-dimensional layouts while Flexbox should be used for one-dimensional layouts. But Grid is great at one-dimensional layouts as well — especially if you come back later and decide that you want to make that layout multi-dimensional.

### Setting Up CSS Grid

Grid is extremely easy to setup — all it takes is two lines of CSS.

**HTML**

```
<div class=”wrapper”>  <div class=”item”>1</div>  <div class=”item”>2</div>  <div class=”item”>3</div>  <div class=”item”>4</div>  <div class=”item”>5</div>  <div class=”item”>6</div></div>
```

**CSS**

```
.wrapper {    display: grid;    grid-template-columns: 10rem 10rem 10rem;}
```

And voila! You have a grid. Seriously, that’s all you need. It’s pretty great.

You’ll notice that, unlike when setting Flexbox to `display: flex`, adding `display: grid` to your wrapper doesn’t immediately make a difference. This is because you aren’t explicitly defining how many columns you want your grid to have. You’ll do this with `grid-template-columns` like I did above. So in this example, I’m setting three columns to have a width of 10rem each.

![Image](https://cdn-media-1.freecodecamp.org/images/Wx6aCuxkG9v5RW2lfXqtcx7xK710jszdhC2U)
_Basic CSS Grid_

You can use any value you want when setting `grid-template-columns`, but I suggest staying away from percentages unless you’re trying to add up to 100%. This is because you will have to take your amount of `grid-gap` (which we’ll dive into in a little bit) into account, and that can get a little tricky.

### Explicit vs Implicit Tracks

Before I talk about explicit and implicit tracks, let’s first talk about what tracks are. Tracks are how columns and rows are numbered. Instead of counting the individual columns and rows by themselves, in CSS Grid you count them by the track lines. Here’s the grid we started with — I’ve numbered all of the track rows and columns to make it a little easier for you to see.

![Image](https://cdn-media-1.freecodecamp.org/images/Lzsu5YPNOxOKmxdGRo1K2fHWC8iCNfjFjKWA)
_CSS Grid with column lines and row lines numbered out_

You can see that we actually have four column lines and three row lines. This will help when placing your items on the grid.

**A quick side note:** if you’re using Firefox’s Developer Edition (the beta version of the regular Firefox) it actually has some great dev tools for seeing the column and row track numbers. If you inspect your wrapper element and then go to the layout tab, check the box for your wrapper and now your grid will look like below! I really hope Chrome adds an inspect feature like this in the future. It’s extremely helpful.

![Image](https://cdn-media-1.freecodecamp.org/images/zTYIbSUwg0wmLM23ImHDlbE3KXbnSr-7rZuQ)
_Firefox Developer Edition Inspector Tools_

Let’s go back to the difference between explicit and implicit tracks. If we take our code from above, you’ll notice that we’ve only set our columns. In this case, we’ve **explicitly** set our columns to have three, but we’ve **implicitly** set our rows. We have six items, but obviously all of these items cannot fit in three columns so a second row gets implicitly set.

This is a little confusing, so I definitely recommend messing around with CSS Grid on your own to see the difference between explicit and implicit tracks.

### Adding Grid-Gap

Think of grid gap like margin except it’ll only be added between items and not to the outside of the grid. I’ve run into so many cases when I add margin on items in a Flexbox grid only to have to go to the grid’s wrapper and set the same amount of margin, but negative, to offset the margin that gets set outside of the grid. Thankfully with CSS Grid, you don’t have to deal with that.

Let’s take our example CSS above and add some grid-gap.

```
.wrapper {  display: grid;  grid-template-columns: 10rem 10rem 10rem;  grid-gap: 1rem;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/nzT7VWv1P6QnCa6VMPH-D0qlvcl934z5QI8h)
_CSS Grid with 1rem of grid-gap_

I used the shorthand property `grid-gap`, but you can define an explicit value for the columns and rows by using `grid-column-gap` and `grid-row-gap`.

_*Note: [Chrome 66](https://blog.chromium.org/2018/03/chrome-66-beta-css-typed-object-model.html) will be changing `grid-gap` to `gap` and `grid-column-gap`/`grid-row-gap` to `column-gap`/`row-gap`._

### The Repeat() Function

Defining how wide you want each of your columns to be when using `grid-template-columns` with three columns that are all the same width is pretty simple. But that’s a lot of typing if you want any more columns than that. This is where the `repeat()` function comes in.

Here’s our example we’ve been using with the `repeat()` function added in.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

As you can see in my CSS, I’m setting three columns each to be 10rems wide. This grid will look exactly like the grid pictured in our grid-gap example. By using the `repeat()` function we’re just making writing things a little simpler and easier to read for when you’re wanting to set a lot of columns.

### Fractional Units

Fractional units, or fr, are a new CSS length unit introduced with CSS Grid and one that I can see myself using all the time. Say we want three columns all of equal width. Instead of setting `width: calc(100% / 3)` on the items, we can use fractional units. Think of fractional units as “free space.”

Let’s continue on with our example that we’ve been using.

```
.wrapper {  display: grid;  grid-template-columns: 1fr 1fr 1fr;  grid-gap: 1rem;}
```

You’ll notice that the only thing I changed was `grid-template-columns`. I’m now telling the browser that I want three columns, and that I want each of those columns to take up one fractional unit or one “free space.” This works very similarly to Flexbox’s `flex-grow` property.

![Image](https://cdn-media-1.freecodecamp.org/images/1IN8vd78DiJjP6-KMqXEM3iK9oc0A6RsdYzF)
_CSS Grid using fractional units_

The reason each item is a little wider than in our previous example is because they are now taking up as much space as they can while still fitting in three columns. In this case, I didn’t set a hard width so they are taking up the full-width of my screen. I know this is a little hard to see without having it on your own screen, so I definitely recommend messing with this on your own.

You don’t have to set all of your columns to be 1fr, either. Below is an example where I’ve set my first and third column to 10rems while my middle column is 1fr. You can also set your columns to 2fr, 3fr, and so on, and that column’s items will take up 2x, 3x (and so on) the amount of space.

![Image](https://cdn-media-1.freecodecamp.org/images/gTdHQ0Sm6kYAV8PUx9PcgDPvI0oz0bxeU2D0)
_CSS Grid with only the middle column set to 1fr_

### Sizing Individual Grid Items

Let’s talk about sizing our individual grid items. You cannot place a hard width on individual items, because we explicitly set the width with `grid-template-columns`. But what if you want item five in our example to be the width of multiple columns? We can do this using `grid-column` and `span`.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column: span 2;}
```

You’ll see above that we’re setting `grid-column` of item five to be a span of two which will allow item five to span a width of two columns.

![Image](https://cdn-media-1.freecodecamp.org/images/PZKKIczjUcd2HeOw3EzIHTCYp3Z-9csboNjB)
_CSS Grid with span on an individual item_

But what if you wanted item five to span three columns? This is what will happen.

![Image](https://cdn-media-1.freecodecamp.org/images/DzshGlWqLrUDYAqbFz80hdTzlLqcVzHAyTQJ)
_CSS Grid spanning item five across three columns_

Because item five naturally starts at the second column, we don’t have enough space for it to span the total width we’ve set. So it will move down to the next row. You can apply the same concept from `grid-column` to `grid-row` if you’re wanting an item to span multiple rows.

There’s a pretty simple solution for fixing the blank space that’s leftover from item five moving down a row. It can be used whether you’re setting an item to span a row or a column— `grid-auto-flow: dense`.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;  grid-auto-flow: dense;}
```

```
.item5 {  grid-column: span 3;}
```

In CSS Grid, the grid will automatically check to see if items fit. Like I said above, if an item doesn’t fit it will break to the next line. `Grid-auto-flow: dense` tells the grid to fill in those empty spaces with any item that will fit. In this case, I’ve added a seventh grid item so the grid automatically moves that and the sixth item to the empty spots.

CSS Grid will always layout items that need to go in a specific spot first — in this case, item five, since it is spanning three columns. Then, if you have `grid-auto-flow: dense` set, it will look for other items to fit into the blank spots on the grid.

![Image](https://cdn-media-1.freecodecamp.org/images/e34AFH8TDnMbKaG21HzgjJvqa5msz02C0OD5)
_CSS Grid with grid-auto-flow: dense_

The `grid-auto-flow` property by itself determines in which direction you need to add another row or column after you’ve already defined your items. Row is the default. I haven’t see a big use case for this besides using `grid-auto-flow: dense`.

### Placing Grid Items

In our example with sizing individual grid items we were originally setting item five to `grid-column: span 2` , which allowed item five to span across two columns. Actually, `grid-column` is shorthand for `grid-column-start` and `grid-column-end`. The same goes for `grid-row` as well.

So, technically, we were setting item five to be `grid-column-start: span 2`and `grid-column-end: auto`. Essentially, we were telling the grid to start item five where it naturally would, but go twice the size.

Let’s work with item five again, and I’m going to show you this using Firefox Developer Edition’s inspector tools so it’s easier for you to see what track line item five is at. I’ve also added a couple more grid items.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column-start: 1;  grid-column-end: 3;}
```

CSS Grid will layout all of the items before our fifth one, stop and then look at where we started and ended item five, and place it where we told it to. The shorthand of this would be `grid-column: 1 / 3` where 1 is our start value and 3 is our ending value.

![Image](https://cdn-media-1.freecodecamp.org/images/C4MNJnfRJUwGoFqKM69a4y2k16-fLP0lCIrL)
_CSS Grid using grid-column-start and grid-column-end_

You can also tell an individual grid item how wide you want it to span and where you want it to end. I’m using the shorthand `grid-column` property in this example, so I’m telling item five to span two columns ending at track line four.

```
.wrapper {  display: grid;  grid-template-columns: repeat(3, 10rem);  grid-gap: 1rem;}
```

```
.item5 {  grid-column: span 2 / 4;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/LuGjQJfITo7W4To2qDog3V6qdaFO7DOfvq-N)
_CSS Grid with grid-column shorthand property_

If you want your item to span the entire width of the grid, but don’t know how wide your grid is, you can set `grid-column: 1 / -1`. Basically that -1 value is telling your item to go all the way across to the last track. If you do this with rows you’ll notice that your item may not go all the way to the bottom of your grid. It will only go to the bottom of your **explicit,** rows not your implicit rows.

### Resources

Here are some resources I highly recommend for a deeper dive into CSS Grid!

* [Wes Bos](https://www.freecodecamp.org/news/a-beginners-guide-to-css-grid-3889612c4b35/undefined)’ [CSS Grid Tutorial](https://cssgrid.io/) — it’s totally free and is where I learned about grid. I love his style of teaching!
* CSS Tricks’ [Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) — this has some great cheat sheets for when you’re stuck on a certain aspect of Grid.
* [CSS Grid Garden](https://cssgridgarden.com/) — a fun way to practice what you’ve learned about CSS Grid. I recommend doing a tutorial before attempting this as it gets a little confusing at times.

Thanks for reading my tutorial on CSS Grid! Check out my other articles like [How To Answer the Dreaded ‘Tell Me About Yourself’ Interview Question](https://medium.freecodecamp.org/how-to-answer-the-dreaded-tell-me-about-yourself-interview-question-cec7137ca17b),‘[Why You Should Hire A Bootcamp Grad](https://medium.com/@karaluton/why-you-should-hire-a-bootcamp-grad-49874ccee2e0) or [my story of how I became a developer](https://medium.com/@karaluton/from-music-publicist-to-web-developer-767b023c44cd).

And be sure to follow me on Twitter for lots of tweets about tech and, if I’m being honest, lots of tweets about dogs too.

[**Kara Luton (@karaluton) | Twitter**](https://twitter.com/karaluton)  
[_The latest Tweets from Kara Luton (@karaluton). Front end developer + former music publicist. Retired ballerina…_twitter.com](https://twitter.com/karaluton)

