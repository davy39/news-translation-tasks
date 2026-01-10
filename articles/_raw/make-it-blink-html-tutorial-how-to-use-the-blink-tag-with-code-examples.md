---
title: Make It Blink HTML Tutorial – How to Use the Blink Tag, with Code Examples
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-27T23:21:14.000Z'
originalURL: https://freecodecamp.org/news/make-it-blink-html-tutorial-how-to-use-the-blink-tag-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/blink-1.jpg
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'In the earlier days of the web, HTML elements like the blink tag were native
  ways to add some animation effects to liven up a webpage. How can we use those animations
  today to add flare to our websites and apps?


  What is the HTML tag blink?

  How do yo...'
---

In the earlier days of the web, HTML elements like the blink tag were native ways to add some animation effects to liven up a webpage. How can we use those animations today to add flare to our websites and apps?

* [What is the HTML tag blink?](#heading-what-is-the-html-tag-blink)
* [How do you use the blink tag?](#heading-how-do-you-use-the-blink-tag)
* [Can you still use the blink tag?](#heading-can-you-still-use-the-blink-tag)
* [Recreating the blink tag with CSS animations](#heading-recreating-the-blink-tag-with-css-animations)

%[https://www.youtube.com/watch?v=-gU-gkfEA1Q]

## What is the HTML tag blink?

The [blink](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blink) tag (`<blink>`) is an obsolete HTML tag that makes the content of that tag slowly flash.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/google-search-blink.gif)
_Google search of "blink tag"_

This, along with some other obsolete tags like the [marquee](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee) tag (`<marquee>`), were an easy way to add simple animation effects to your site.

## How do you use the blink tag?

Being that the blink tag was a simple HTML element, you would use it right in line with your content.

For example, if you wanted the word "blink" in blink-182 to blink, you would write the following HTML:

```html
<p>
  <blink>blink</blink>-182
</p>
```

## Can you still use the blink tag?

As you might have noticed in the gif above, this tag is obsolete.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/html-blink-browser-compatability.jpg)
_Blink tag browser compatibility_

This means you can’t use the blink HTML tag itself. However, that shouldn't stop us from remaking it in all of its blinking glory.

_Note: the Blink tag was deprecated due to accessibility concerns. Please [do your research](https://en.wikipedia.org/wiki/Blink_element#Usability_and_accessibility) before trying to use a solution that provides the same effect, as we should all be making an effort to make our projects as inclusive as possible._

## Recreating the blink tag with CSS animations

In today’s web development world, animations are generally handled with CSS or JavaScript. Using CSS animations, we can recreate our blink tag with a few lines and be back in business.

With the following CSS:

```css
.blink {
  animation: blink 1s steps(1, end) infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

```

You can add the `.blink` class to any HTML element to make it blink.

```
<p>
  <span class="blink">blink</span>-182
</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/html-blink-effect.gif)
_HTML CSS blink effect_

## Modernizing the blink tag

This is 2020, what if we wanted something a little smoother?

Well to start, we can make the animation fade by removing the `steps` from the animation definitions.

```css
.blink {
  animation: blink 1s infinite;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-blink-fade.gif)
_Blink fade effect_

Or what if we wanted to make it fade out like a sci-fi effect?

```
.blink {
  animation: blink 3s infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    color: blue;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-scfifi-fade.gif)
_CSS blink fade sci-fi effect_

Or even a nice grow and fade effect.

```css
.blink {
  animation: blink 3s infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: scale(2);
  }
  51% {
    opacity: 0;
    transform: scale(0);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-grow-fade.gif)
_CSS blink grow and fade effect_

## Taking control of animations with CSS

Though you might not be able to use the blink tag, you still have a lot of options. CSS provides a ton of animation options natively, so whether you want to recreate your favorite HTML pastime or [recreate the Alien title sequence](https://codepen.io/colbyfayock/pen/aEqsL), the possibilities are virtually endless.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

