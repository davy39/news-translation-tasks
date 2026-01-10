---
title: Learn Flexbox with These 8 Most Common Use Cases
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-03T23:50:56.000Z'
originalURL: https://freecodecamp.org/news/learn-flexbox-common-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Ep5_thumbnail.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Thu Nghiem

  When it comes to building responsive websites, Flexbox makes it super easy to create
  flexible and responsive layouts. So learning Flexbox is a must for front-end developers.

  But many tutorials try to teach you everything at once and for...'
---

By Thu Nghiem

When it comes to building responsive websites, Flexbox makes it super easy to create flexible and responsive layouts. So learning Flexbox is a must for front-end developers.

But many tutorials try to teach you everything at once and forget to tell you when and why you'll use each concept.

In this tutorial, I am going to show you the most common use cases of Flexbox by solving eight tasks together. By the end you will be ready to use Flexbox in your next projects.

You can download the starter here: [Flexbox-Tutorial-Starter](https://bit.ly/3eNPw2T)

Here's a video you can watch if you want to supplement this article:

%[https://youtu.be/3G4MfMAeamg]

### Setup

If you download and open the index.html file, you will see 8 tasks in total. For each task, you will find containers and items inside it. Items are `div` elements with `width` and `height` of `40px`.

## Task 1: Align block elements horizontally in Flexbox

For task number one, we want to align block elements horizontally. By default, block elements are stacked on each other. But if we put them inside a flex container:

```css
.container {
  display: flex;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-17.10.46-1.png)

All the block elements will be aligned on the horizontal axis. Quite easy, right? 😉And that's it for task number one. 

## Task 2: Center item(s) in the middle of the container in Flexbox

For the next task, we need to center some items in the middle of the container. We can do so by setting the flex container to have `justify-content: center;` and `align-items: center;`:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-17.11.13-1.png)

And that's it for the task 2. But before we move on, let's take a closer look at the `justify-content` and `align-items` properties.

### 1. justify-content property

With `justify-content`, we can align the item(s) on the horizontal axis. 

For example, if we want to align item(s) on the horizontal axis at the **beginning** of the container, we'll do this:

```scss
.container {
  display: flex;
  justify-content: flex-start;
}

```

At the **end** of the container, we'll do this:

```scss
.container {
  display: flex;
  justify-content: flex-end;
}

```

And in the **middle** of the container, we'll do this:

```scss
.container {
  display: flex;
  justify-content: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-1.png)

### 2. align-items property

This property is similar to `justify-content`, but it's on the vertical axis. With `align-items`, we can align item(s) on the vertical axis at the **beginning** of the container like this:

```scss
.container {
  display: flex;
  align-items: flex-start;
}

```

At the **end** of the container like this:

```scss
.container {
  display: flex;
  align-items: flex-end;
}

```

* And in the **middle** of the container like this:

```scss
.container {
  display: flex;
  align-items: center;
}

```

Now if we combine `justify-content` and `align-items`, we can align item(s) at the middle of the container, right-bottom corner, right-top corner, and so on.

## Task 3: Distribute space between items in Flexbox

For the third task, we need to add equal spaces between the items. To achieve this, it is quite simple. All we have to do is to give the flex container `justify-content: space-between;`.

```scss
.container {
  display: flex;
  justify-content: space-between;
}

```

`justify-content: space-between;` gives us equal spaces between items. 

This is super useful in the navigation, for example, where we need to put equal spaces between the items:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/navigation.png)

And because we are looking at `space-between`, with `justify-content` we can also give it `space-evenly` and `space-around` values.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/justify.png)

#### `justify-content: space-evenly;`

If we give `justify-content` a value of `space-evenly`, spaces will not only be added between the items but also before the first item and after the last item.

#### `justify-content: space-evenly;`

If we give `justify-content` a value of `space-around`, equal spaces will be added around the items.

## Task 4: Push items to the end of the container in Flexbox

For task 4, we need to push the last item to the end of the container on the horizontal axis. I am going to show 3 options using Flexbox.

#### Option 1: using `justify-content: space-between;`

With 2 items inside the container, we can use `justify-content: space-between;`. It will push the first item to the start and the last item to the end of the container.

```scss
.container {
  display: flex;
  justify-content: space-between;
}

```

You can see in the example when we only have the logo and the button:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dtxocmk4n22t3ga8h4ro.png)

or logo and navigation items:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/kchezon63sxjjjcr6o31.png)

#### Option 2: using an empty `div` with `flex-grow`

With more than 3 items, I like to add an empty `div` with `flex-grow: 1` between items. 

For example, if I put a `div` with `flex-grow: 1` between the second item and the last item (third item), the empty `div` will expand as much as it can and it pushes the last item to the end of the container:

```html
  <div class="option-2">
     <div class="container">
        <div class="item sm"></div>

        <div class="item"></div>

        <div class="space"></div>

        <div class="item"></div>
        </div>
  </div>

```

```scss
  .option-2 .space {
    flex-grow: 1;
  }

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-grow.png)

You might see it in more complex navigation like:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/53bomxpqg8dattgno25f.png)

#### Option 3: using `flex-grow` for one item

If we have 2 items, for example, we can give the first item `flex-grow: 1;`. By doing this, the first item will expand as much as it can, so it pushes the last item to the end of the container.

```scss
  .option-3 .item:first-child {
    flex-grow: 1;
  }

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flex-grow-2.png)

Few examples in input components:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ww5uvqfjntpfab9nah8a.png)

#### Bonus

We can also use `margin-left: auto` to push the last item to the end of the container. For example, in option 1, we can give the last item `margin-left: auto;` and it will work the same. 

```css
.task-4 .option-1 .container {
  display: flex;
}

.task-4 .option-1 .item:last-child {
  margin-left: auto;
}

```

`margin: auto` is super useful, but let's dive into it in another article and video.

## Task 5: Build relative size column layout in Flexbox

By giving the item a flex value of `flex: {number}`, we can control the size of the item relative to other items. For example with this code:

```css
.task-5 .item-1 {
  flex: 3;
}

.task-5 .item-2 {
  flex: 1;
}

.task-5 .item-3 {
  flex: 1;
}

.task-5 .item-4 {
  flex: 1;
}

```

We just created a layout that has in total 6 columns. Item 1 takes up 3 columns, whereas the other 3 items will take up 1 column:

This is useful, for example, in a table layout:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4jsmaoxclhje1bmlxr68.png)

This layout is taken from another tutorial, where I show how to build a React + Next.js application from start to finish. Here's the [YouTube link](https://youtu.be/v8o9iJU5hEA) if you want to watch and code along.

## Task 6: Build a responsive layout in Flexbox with and without media queries 

### 1. Responsive layout without media query

If we give a flex container `flex-wrap: wrap`:

```css
.task-6 .container {
  display: flex;
  flex-wrap: wrap;
}

```

We will have a responsive layout where items will not try to shrink inside the container:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.44.31.png)

### 2. Responsive layout with media query

With media queries, we will have more control over the size of the items. Say that inside a `flex-wrap` container we want to have 2 columns. We can do this by:

```css
.task-6 .container {
  display: flex;
  flex-wrap: wrap;
}

.task-6 .item {
  flex-basis: 50%;
}

```

Now items will be arranged into a 2-column layout, where each column takes up half of the container.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.45.25.png)

With the same logic, say that we want to have a 4-column layout when the screen is wider than `375px`, we can give every item `flex-basis: 25%`:

```css
@media (min-width: 375px) {
  .task-6 .item {
    display: flex;
    flex-basis: 25%;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.47.20.png)

## Task 7: Change item order in Flexbox (not common)

With Flexbox, we can change the order of the items. For example, inside a flex container, if we have 4 items and we want to put the first item at the end of the row. All we have to do is to give the item `order: 1`.

```css
.task-7 .item-1 {
  order: 1;
}

```

By default, the `order` property has a value equal to 0 and it can take a negative number.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.48.20.png)

## Task 8: Change the position of an item inside a flex container (not common)

An item inside the flex can change position by itself by using `align-self`.

```css
align-self: auto | flex-start | flex-end | center | baseline | stretch;

```

For example, say we want to have item 3 at the end of the container on the vertical axis. We can do this:

```css
.task-8 .container {
  display: flex;
}

.task-8 .item-3 {
  align-self: flex-end;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.49.00.png)

## `flex-direction` property 

Flexbox has a `flex-direction` property by default. `flex-direction` has the value of `row`, which means that items are aligned on the horizontal axis.

If we want items to be aligned on the vertical axis, we can use `flex-direction: column;`.

For example, in task 3, if we give the flex container `flex-direction: column;`:

```css
.task-3 .container {
  display: flex;

  justify-content: space-between;
  flex-direction: column;
}

```

We will have:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-03-at-21.50.19.png)

What we just learnt for flex-direction: row; will still work the same for flex-direction: column;, but instead of a horizontal axis, it will be a vertical axis.

## Conclusion

Now that you have learned about Flexbox and [CSS Grid](https://www.freecodecamp.org/news/learn-css-grid-by-building-5-layouts/), you can continue by building responsive websites. You can find a list of projects to do on [devchallenges.io](https://devchallenges.io/), or you can join me in the following video tutorial, where we will build a professional website from start to finish:

%[https://youtu.be/CrryRvjYsgc]

  
Thanks for reading this article. This topic belongs to the series of videos that I will update on [Learn.DevChallenges.io](https://learn.devchallenges.io/). So to say updated, follow me on social media or subscribe to my [Youtube Channel](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1). Otherwise, happy coding and see you in the next videos and articles 👋.

**__________ 🐣 About me __________**

I am a full-stack developer, a UX/UI designer and a content creator. You can get to know me more in this short video:

[Embedded content](https://www.youtube.com/embed/qCkmFd-72JY?feature=oembed)

* I am the founder of [DevChallenges](https://devchallenges.io/)
* Subscribe my [Youtube Channel](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1)
* Follow my [Twitter](https://twitter.com/thunghiemdinh)
* Join [Discord](https://discord.com/invite/3R6vFeM)

  

