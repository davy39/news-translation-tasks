---
title: How to tackle CSS specificity issues and when to use the !important keyword
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T18:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-tackle-css-specificity-issues-and-when-to-use-the-important-keyword-b54123995e1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O8s-GnxQPCyWNVc2WJyB5g.jpeg
tags:
- name: CSS
  slug: css
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Muna Mohamed

  A Case Study


  Recently, there was a Twitter poll floating around where the user asked their followers
  a question about CSS specificity . Unfortunately, I was unable to find the original
  tweet (comment below if you happen to find it!) ...'
---

By Muna Mohamed

#### A Case Study

![Image](https://cdn-media-1.freecodecamp.org/images/MzDK5rCsyUZQUDJtzNPCrrCVqob-ULXNImuE)

Recently, there was a Twitter poll floating around where the user asked their followers a question about CSS specificity . Unfortunately, I was unable to find the original tweet (comment below if you happen to find it!) but long story short, the majority of people got the answer wrong.

That Twitter poll (and its aftermath) led to me brushing up on my own knowledge of the topic of specificity and in turn, made me start fixing specificity issues in my own projects — which brings me to the purpose of this post.

In this post, we will be refactoring CSS code from a project of mine that has CSS specificity issues that are in need of fixing.

### CSS Specificity

#### Definition

Specificity is described by [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) as:

> _the means by which browsers decide which CSS property values are the most relevant to an element and therefore, applied._

#### Rules

When deciding which CSS property values are the most relevant to apply to an element, the browser uses the source order (i.e the cascade) of the CSS stylesheet to determine this. But this rule applies when the CSS selectors have equal specificity. What happens when the specificity of one CSS selector is higher than another?

![Image](https://cdn-media-1.freecodecamp.org/images/vS9jdbLJDgW1IWycyuIWGFlX9xPnJxekCte-)

In that case, browsers will use the specificity of a CSS selector to determine what CSS statements to apply. The higher the specificity of a CSS selector, the more likely that browsers will apply its CSS declarations over another.

```css
nav a {
  color: green;
}

a {
  color: red;
}
```

For example, in the example above, both of the CSS selectors are targeting the same HTML element, the anchor tag. In order to determine which CSS rule to apply to the anchor tag, the browser will calculate the specificity value and check which one is the highest. In this case, the first selector has a higher specificity value, therefore the browser will use its declarations to apply to the anchor tag.

I’d like to point out here that although _!important_ is not a CSS selector, it is a keyword that is used to forcefully override a CSS rule regardless of the specificity value, origin or source order of a CSS selector. Some use cases include:

* Temporary fixes (a bit like putting duct-tape on a leaky pipe)
* Overriding inline styling
* Testing/debugging purposes

As useful as using the _!important_ keyword may seem, the use of it can be more problematic than helpful. Over time, it can make it difficult to maintain your CSS and it can negatively affect the readability of your stylesheet, particularly for anyone else who is or will be working with it in the future.

Which brings us to what we’ll be doing today — fixing the specificity issues in a project.

### The Project

![Image](https://cdn-media-1.freecodecamp.org/images/jLPGiwbON7agN2c4M5yy0IPHIvvmpcmFFn75)

A little background about the project we’ll be refactoring — it is a Netflix inspired landing page using MovieDB’s API.

#### The stylesheet

The aim is to remove the _“!important”_ keyword from the CSS rules that it has been applied to by refactoring the code so that it follows specificity rules.

Below, you can see the stylesheet for the project.

```css
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,400i,700");

body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.wrapper {
  width: 100%;
}

.wrapper #header {
  position: fixed;
  z-index: 300;
  padding: 15px;
  width: calc(100% - 30px);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(to bottom, black 0%, transparent 100%);
}

.wrapper #header #brand-logo {
  color: #d32f2f;
  text-shadow: 1px 1px 2px black;
  letter-spacing: 5px;
  text-transform: uppercase;
  font-family: Montserrat;
  font-weight: bold;
  font-size: 22px;
}

.wrapper #header #menu-icon {
  display: none;
}

.wrapper #header .nav-link,
.wrapper #header .icon {
  color: #bdbdbd;
  cursor: pointer;
}

.wrapper #header .nav-menu {
  width: 400px;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.wrapper #header .nav-link {
  padding: 5px 10px;
  font-size: 15px;
  font-family: century gothic;
  text-decoration: none;
  transition: background-color 0.2s ease-in;
}

.wrapper #header .nav-link:hover {
  color: #c62828;
  background-color: rgba(0, 0, 0, 0.7);
}

.wrapper #header .icon {
  font-size: 16px;
}

.wrapper #header .icon:hover {
  color: #c62828;
}

.wrapper #site-banner,
.wrapper #categories {
  width: 100%;
}

.wrapper #site-banner {
  height: 550px;
  background-image: url("https://s1.gifyu.com/images/rampage_2018-1024x576.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.wrapper #site-banner .main-movie-title,
.wrapper #site-banner .watch-btn,
.wrapper #site-banner .main-overview {
  position: absolute;
  z-index: 3;
}

.wrapper #site-banner .main-movie-title, .wrapper #site-banner .watch-btn {
  text-transform: uppercase;
}

.wrapper #site-banner .main-movie-title {
  top: 120px;
  left: 20px;
  background: -webkit-linear-gradient(#ff9100, #dd2c00);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 55px;
  font-family: Montserrat;
  font-weight: bold;
}

.wrapper #site-banner .main-overview {
  width: 400px;
  top: 230px;
  left: 25px;
  color: #fafafa;
  line-height: 25px;
  font-family: helvetica;
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  top: 350px;
  left: 25px;
  border: none;
  border-radius: 20px;
  color: #fafafa;
  cursor: pointer;
  transition: all 0.2s ease-in;
  background-color: #ff0000;
  box-shadow: 1px 5px 15px #940000;
}

.wrapper #site-banner .watch-btn:hover {
  color: #F5F5F5;
  background-color: #940000;
}

.wrapper .after {
  position: relative;
  top: 0;
  left: 0;
  z-index: 2;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
}

.wrapper #categories {
  padding: 30px 0;
  display: flex;
  flex-direction: column;
  background: linear-gradient(to top, #090909 0%, #000000 100%);
  overflow: hidden;
}

.wrapper #categories .category {
  margin: 30px 0;
}

.wrapper #categories .category-header, .wrapper #categories .content {
  margin-left: 20px;
  color: #B0BEC5;
  font-family: helvetica;
}

.wrapper #categories .category-header {
  margin-bottom: 50px;
  font-weight: normal;
  letter-spacing: 5px;
}

.wrapper #categories .content {
  position: relative;
  right: 0;
  display: flex;
  justify-content: flex-start;
  transition: all 3s ease-in-out;
}

.wrapper #categories .movie {
  margin-right: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.wrapper #categories .movie-img {
  transition: all 0.2s ease-in;
}

.wrapper #categories .movie-img:hover {
  -webkit-filter: contrast(1.1);
          filter: contrast(1.1);
  -webkit-transform: scale(1.05);
          transform: scale(1.05);
  cursor: pointer;
}

.wrapper #footer {
  width: 100%;
  height: 120px;
  background-color: #090909;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
}

.wrapper #footer #copyright-label {
  margin-left: 20px;
  padding: 10px;
  color: rgba(255, 255, 255, 0.3);
  opacity: 0.7;
  letter-spacing: 2px;
  font-family: helvetica;
  font-size: 12px;
}

//Media Query
@media (max-width: 750px) {
  .nav-menu {
    visibility: hidden;
  }
    
#menu-icon {
    display: block !important;
    font-size: 22px;
  }
    
.main-movie-title {
    font-size: 45px !important;
  }
    
.main-overview {
    width: 350px !important;
    font-size: 14px !important;
  }
    
.watch-btn {
    width: 130px !important;
    height: 25px !important;
    font-size: 13px;
  }
    
.movie-img {
    width: 170px;
  }
}
```

So, we can see from the stylesheet that the use of the _!important_ keyword is mainly focused in the media query section which outlines the styles that the browser should apply when the screen-width is less than 750 pixels.

So, what happens when we remove the _!important_ keyword from the CSS rules that it has been applied to? Well, we no longer have a “trump card” forcefully overriding the CSS rules of other CSS selectors that target the same HTML element. So, the browser will look at the stylesheet to see if there are any conflicting CSS rules.

If there are, then in order to determine which CSS rules to apply over another, the browser will use the source order, specificity and importance of the CSS selectors. If the CSS selectors with conflicting CSS rules have equal specificity, then the browser will use the source order rule and apply the CSS rules of the CSS selector that comes lower down in the stylesheet. Using this information, we can see that this situation is not the case for our stylesheet.

But, if the CSS selectors with conflicting CSS rules don’t have equal specificity, then the browser will apply the CSS rules of the CSS selector that has higher specificity. We can see from our stylesheet that this is the case; the CSS selectors in our media query have lower specificity than the CSS selectors in the main part of our stylesheet.

Now that we have identified the issue, let’s fix it!

First we have to locate the corresponding CSS selectors that match the CSS selectors in our media query.

```css
.wrapper #header #menu-icon {
  display: none;
}

.wrapper #site-banner .main-movie-title {
  ...
  font-size: 55px;
  ...
}

.wrapper #site-banner .main-overview {
  width: 400px;
  ...
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  ...
}

@media (max-width: 750px) {
#menu-icon {
    display: block !important;
    ...
  }
    
.main-movie-title {
    font-size: 45px !important;
  }
    
.main-overview {
    width: 350px !important;
    font-size: 14px !important;
  }
    
.watch-btn {
    width: 130px !important;
    height: 25px !important;
    ...
  }
}
```

We can see that the CSS selectors in the main part of the stylesheet have higher specificity than the corresponding CSS selectors in the media query. Despite the CSS selectors in the media query appearing later on in the stylesheet, because of specificity rules (which take precedence over source order rules), the browser will apply the CSS rules of the CSS selectors that come before it.

To fix this, we must increase the specificity values of the CSS selectors in the media query. If we make it so that the CSS selectors that target the same HTML elements have equal specificity, then the browser will follow the source order rule. The CSS rules outlined in the media query (that’s located lower down in the stylesheet) will be applied when the screen-width is less than 750 pixels.

The end result will look like this:

```css
.wrapper #header #menu-icon {
  display: none;
}

.wrapper #site-banner .main-movie-title {
  ...
  font-size: 55px;
  ...
}

.wrapper #site-banner .main-overview {
  width: 400px;
  ...
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  ...
}

@media (max-width: 750px) {
.wrapper #header #menu-icon {
    display: block;
    ...
  }
    
.wrapper #site-banner .main-movie-title {
    font-size: 45px;
  }
    
.wrapper #site-banner .main-overview {
    width: 350px;
    font-size: 14px;
  }
    
.wrapper #site-banner .watch-btn {
    width: 130px;
    height: 25px;
    font-size: 13px;
  }
}
```

And that’s it! We have removed all traces of the _!important_ keyword from the stylesheet. Already we can see that the stylesheet is easier to read, and you can imagine that our refactored stylesheet would be a lot easier to work with and maintain (particularly if others will be working on it too).

### Conclusion

So, what have we learned?

We have learned about how browsers determine which CSS styles to apply by using the source order, specificity and origin of selectors. We have also learned about the problems which can arise by using _!important_ in your CSS and why its use should be kept to a bare minimum.

We do not have to resort to using _!important_ in order to fix things — there are much better solutions out there.

The concept of specificity is one that can take a while to get your head around, but I hope that by documenting the process and using a real project, it helps you better understand the concept of specificity and how to apply it in your own CSS.

**Additional Resources**

* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)
* [Batficity](http://batificity.com/) by [Mandy Michael](https://twitter.com/Mandy_Kerr)
* [CSS Specificity Wars](https://stuffandnonsense.co.uk/archives/css_specificity_wars.html) by [Andy Clarke](https://twitter.com/malarkey)
* [Specificity Visualizer](https://isellsoap.github.io/specificity-visualizer/) by [Francesco Schwarz](https://twitter.com/isellsoap).
* [When using !important is the right choice](https://css-tricks.com/when-using-important-is-the-right-choice/) by [Chris Coyier](https://twitter.com/chriscoyier)

You can find the project we’ve been working on [here](https://codepen.io/Munamohamed94/pen/LJWzGr).

#### I hope you enjoyed this post! If you did, ❤️, ? and share! Till next time! ✌️

