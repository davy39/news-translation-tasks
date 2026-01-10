---
title: How to create a Custom Progress Bar
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-13T04:02:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-custom-progress-bar
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/how-to-create-a-custom-progress-bar.png
tags:
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
- name: coding challenge
  slug: coding-challenge
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: progress bar
  slug: progress-bar
seo_title: null
seo_desc: 'By Florin Pop

  Originally published on www.florin-pop.com

  The theme for week #14 of the Weekly Coding Challenge is:

  Progress Bar

  A progress bar is used to show how far a user action is still in process until it''s
  completed. A good example is a downloa...'
---

By Florin Pop

_Originally published on [www.florin-pop.com](https://www.florin-pop.com/blog/2019/06/how-to-create-a-custom-progress-bar/)_

The **theme** for week #14 of the [Weekly Coding Challenge](https://florin-pop.com/blog/2019/03/weekly-coding-challenge/) is:

## Progress Bar

A progress bar is used to show how far a user action is still in process until it's completed. A good example is a download progress bar which shows you how much of the file is downloaded already (or it could also be an upload progress bar if you upload files ?).

In this article we're going to build this kind of a [Progress Bar](https://codepen.io/FlorinPop17/full/jjPWbv/):

%[https://codepen.io/FlorinPop17/pen/jjPWbv/]

## The HTML

For the HTML structure we need two things:

1. a _container_ which will display the total length (100%) of the progress bar - `.progress-bar`
2. the actual progress element which will basically track the current progress (e.g. 20%) - `.progress`

```html
<div class="progress-bar">
    <div data-size="20" class="progress"></div>
</div>
```

As you can see the `.progress` div has a `data-size` attribute. This will be used in **JavaScript** to actually set the `width` of the progress. You'll see in a moment what I mean, but first let's style these two elements. ?

## The CSS

```css
.progress-bar {
    background-color: #fefefe;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    margin: 15px;
    height: 30px;
    width: 500px;
    max-width: 100%;
}

.progress {
    background: #ad5389;
    background: -webkit-linear-gradient(to bottom, #3c1053, #ad5389);
    background: linear-gradient(to bottom, #3c1053, #ad5389);
    border-radius: 3px;
    height: 30px;
    width: 0;
    transition: width 0.5s ease-in;
}
```

Few things to note regarding the above CSS:

1. both elements are rectangles that have the same height (`30px`) and the same `border-radius`
2. initially the `.progress` width it set to `0` and we'll update this in the **JavaScript** code below
3. also the `.progress` has a nice `linear-gradient` from [uiGradients](https://uigradients.com/)
4. the `transition` added to the `.progress` is used to create a nice animation when the value of it's `data-size` attribute is dynamically changed

## The JavaScript

For this we'll need to loop over all the `.progress` elements (in our example is only one, but you can add multiple ones in an app) to get their `data-set` value and to set it as their width. We'll use percentage (`%`) in this case.

```js
const progress_bars = document.querySelectorAll('.progress');

progress_bars.forEach(bar => {
    const { size } = bar.dataset;
    bar.style.width = `${size}%`;
});
```

We're using a little bit of [Object Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

`const { size } = bar.dataset`

is the same as:

`const size = bar.dataset.size`

but you might know that already ?.

## Conclusion

There are multiple things you could do to improve this component. Some of which are:

1. Add multiple color variants via different _classes_
2. Add the percentage value
3. Make it animate dynamically by changing the size value.

I hope you enjoyed it and make sure you share with me what you're creating!

Happy Coding! ?



