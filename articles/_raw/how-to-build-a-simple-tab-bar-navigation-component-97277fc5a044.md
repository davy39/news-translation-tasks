---
title: How to build a simple tab bar navigation component
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T17:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-tab-bar-navigation-component-97277fc5a044
coverImage: https://cdn-media-1.freecodecamp.org/images/0*E5R1ZESIMi18_upW.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Florin Pop

  The theme for week #3 of my Weekly Coding Challenge is navigation! So let’s learn
  a bit more about it.

  Navigation

  A navigation component is crucial on a website because you want your users be able
  to easily navigate through your pages. ...'
---

By Florin Pop

The **theme** for week #3 of my [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) is **navigation**! So let’s learn a bit more about it.

### Navigation

A navigation component is crucial on a website because you want your users be able to easily navigate through your pages. You can find a navigation component even on single page websites that’ll allow you to jump to a certain section on the page. So as a developer, it is very useful to know how to build this kind of component.

In this article, I decided to build a [Tab Bar Navigation](https://codepen.io/FlorinPop17/full/qvyWxX/), but you can build any kind of navigation you want.

I was inspired by [this](https://dribbble.com/shots/5925052-Google-Bottom-Bar-Navigation-Pattern) design made by [Aurelien Salomon](https://dribbble.com/aureliensalomon). Here is what the final result of what we’re going to build will look like:

%[https://codepen.io/FlorinPop17/pen/ZZajGB]

### The HTML

The HTML structure is going to be simple. We’ll have a `.tab-nav-container` and four `.tab`s within it:

```html
<div class="tab-nav-container">
    <div class="tab active purple">
        <i class="fas fa-home"></i>
        <p>House</p>
    </div>
    <div class="tab pink">
        <i class="far fa-heart"></i>
        <p>Likes</p>
    </div>
    <div class="tab yellow">
        <i class="fas fa-search"></i>
        <p>Search</p>
    </div>
    <div class="tab teal">
        <i class="far fa-user"></i>
        <p>Profile</p>
    </div>
</div>
```

As you can see, each `.tab` has an icon (from [FontAwesome](https://fontawesome.con/)), the corresponding text, and some extra classes that will be used to give each tab specific `background-color` and `color` properties. Also the `.active` class, which will be used to style the active tab. Pretty basic, right? ?

### The CSS

First, let’s style the `.tab-nav-container`:

**Note**: we have a `fixed` width on the container as we don't want it to change its size when we change the active `.tab` since each tab might have a text that's either longer or shorter in size (e.g. Home (4 letters) vs Profile (6 letters)).

We are using `flexbox` to distribute the `.tab`s evenly inside the container. Other than that I believe that the CSS is pretty self-explanatory.

Next…the `.tab`'s styling:

```css
.tab {
    background-color: #ffffff;
    border-radius: 50px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 20px;
    margin: 0 10px;
    transition: background 0.4s linear;
}

.tab i {
    font-size: 1.2em;
}

.tab p {
    font-weight: bold;
    overflow: hidden;
    max-width: 0;
}

.tab.active p {
    margin-left: 10px;
    max-width: 200px;
    transition: max-width 0.4s linear;
}

.tab.active.purple {
    background-color: rgba(91, 55, 183, 0.2);
    color: rgba(91, 55, 183, 1);
}

.tab.active.pink {
    background-color: rgba(201, 55, 157, 0.2);
    color: rgba(201, 55, 157, 1);
}

.tab.active.yellow {
    background-color: rgba(230, 169, 25, 0.2);
    color: rgba(230, 169, 25, 1);
}

.tab.active.teal {
    background-color: rgba(28, 150, 162, 0.2);
    color: rgba(28, 150, 162, 1);
}
```

Few things to note here:

1. In order to have a smooth transition when we change the `.active` tab, we are setting a `transition: background` property to the `.tab` class.
2. By default the `p` tag inside the `.tab` has a `max-width` of `0` and its `overflow` property set to `hidden`. This is because we only want to show the text only when the `.tab` is active.
3. We are using the custom color classes (`.purple`, `.pink`, etc) to have different colors in the tabs.

Let’s make sure it looks good on mobile too:

```css
@media (max-width: 450px) {
    .tab-nav-container {
        padding: 20px;
        width: 350px;
    }

    .tab {
        padding: 0 10px;
        margin: 0;
    }

    .tab i {
        font-size: 1em;
    }
}
```

As you can see, we are shrinking the `.tab-nav-container` when the max-width of the viewport is `450px` and we are also reducing the padding to make it look smaller.

### The JavaScript

At the end, in JS we have to make sure that when the user clicks another `.tab` the `.active` class is added to it and removed from the previous active `.tab`:

```css
// Get all the tabs
const tabs = document.querySelectorAll('.tab');

tabs.forEach(clickedTab => {
    // Add onClick event listener on each tab
    clickedTab.addEventListener('click', () => {
        // Remove the active class from all the tabs (this acts as a "hard" reset)
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });

        // Add the active class on the clicked tab
        clickedTab.classList.add('active');
    });
});
```

### Conclusion

This kind of tab bar navigation is mostly used on mobile devices, so if you want to reuse it for a mobile app make sure that you position the container to the bottom of the screen (with `position: fixed`) and you recalculate the width to fill in the entire screen's width.

In the Codepen example, we’re also changing the background color of the body when another tab is clicked. This is just for visual purposes and it’s not exactly related to the Coding Theme of this week. But if you want to see how I did that, check out the JS code in the [pen](https://codepen.io/FlorinPop17/pen/qvyWxX) (just 2 extra lines of code).

### More examples for this Coding Challenge

In a [previous](https://www.florin-pop.com/blog/2017/09/responsive-animated-navigation-menu) article, I demonstrated how to build a responsive navigation menu. You can check it out too if you want to build something like that.

Also if you haven’t, make sure you read the [Weekly Coding Challenge](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) “rules” if you want to participate in the Challenge! And why wouldn’t you? It’s a great way to improve your coding skills! ?

Happy coding! ?

_Originally published at [www.florin-pop.com](https://www.florin-pop.com/blog/2019/03/tab-bar-navigation/)._

