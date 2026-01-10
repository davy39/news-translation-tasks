---
title: Let’s make multi-colored icons with SVG symbols and CSS variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-31T13:25:33.000Z'
originalURL: https://freecodecamp.org/news/lets-make-your-svg-symbol-icons-multi-colored-with-css-variables-cddd1769fca4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WO5mgu0bcFNdt7R6JH6mhQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sarah Dayan

  Long gone are the days of using images and CSS sprites to make icons for the web.
  With the explosion of web fonts, icon fonts have become the number one solution
  for displaying icons in your web projects.

  Fonts are vectors, so you don’...'
---

By Sarah Dayan

Long gone are the days of using images and CSS sprites to make icons for the web. With the explosion of web fonts, icon fonts have become the number one solution for displaying icons in your web projects.

Fonts are vectors, so you don’t have to worry about resolution. They benefit from the same CSS properties as text. As a result, you have full control over size, color, and style. You can add transforms, effects, and decorations such as rotations, underlines, or shadows.

![Image](https://cdn-media-1.freecodecamp.org/images/jPs5hZEkOo7Q7SPfh2fuoQEcU2LGDgFCffM6)
_No wonder projects like Font Awesome have been downloaded [more than 15 million times on npm alone](http://npm-stats.com/~packages/font-awesome" rel="noopener" target="_blank" title=") to this day._

**Icon fonts aren’t perfect though**, which is why a growing number of people prefer using inline SVG images. CSS Tricks wrote a [list of areas where icon fonts fall short compared to native SVG elements](https://css-tricks.com/icon-fonts-vs-svg): sharpness, positioning, or even failures because of cross-domain loading, browser-specific bugs, and ad-blockers. Now you can circumvent most of these issues, generally making icon fonts a safe choice.

Yet, there’s one thing that remains absolutely impossible with icon fonts: **multicolor support**. Only SVG can do this.

**_TL;DR_**_: this post goes in-depth into the how and why. If you want to understand the whole thought process, read on. Otherwise you can look at the final code on [CodePen](https://codepen.io/sarahdayan/pen/GOzaEQ)._

### Setting up SVG symbol icons

The problem with inline SVGs is how verbose they are. You don’t want to copy/paste all those coordinates every single time you need to use the same icon. This would be repetitive, hard to read, and a pain to maintain.

With SVG symbol icons, you have one copy of each SVG element, and you instantiate them anywhere with a reference.

You start by including the SVG inline, hide it, wrap it in a `<symb`ol> and identify it wi`th` an id attribute.

```
<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path d="..." />  </symbol></svg>
```

_The full SVG markup is included once and hidden in the HTML._

Then, all you have to do is instantiate the icon with a `<u`se> element.

```
<svg>  <use xlink:href="#my-first-icon" /></svg>
```

_This will display an exact copy of your original SVG icon._

![Image](https://cdn-media-1.freecodecamp.org/images/h50v1hbWZfisticSZPXcpnw8B27gYBQS-bpK)

**That’s it!** Pretty nice, right?

You probably noticed the funny `xlink:href` attribute: this is the link between your instance and the original SVG.

It’s important to mention that `xlink:href` is a deprecated SVG attribute. Even if most browsers still support it, **you should use `href` instead**. Now the thing is, some browsers like Safari don’t support SVG resource references through the `href` attribute, so you still need to provide `xlink:href`.

To be safe, provide both attributes.

### Adding some color

Unlike with fonts, `color` doesn’t have any effect on SVG icons: you must use the `fill` attributes to define a color. This means that they won’t inherit parent text color like icon fonts do, but you can still style them in CSS.

```
// HTML<svg class="icon">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon {  width: 100px;  height: 100px;  fill: red;}
```

From here, you can create other instances of the same icon with a different fill color.

```
// HTML<svg class="icon icon-red">  <use xlink:href="#my-first-icon" /></svg>
```

```
<svg class="icon icon-blue">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon {  width: 100px;  height: 100px;}.icon-red {  fill: red;}.icon-blue {  fill: blue;}
```

It works, but this isn’t **exactly** what we want. So far, all we have done can be achieved with a regular icon font. What we want is to have a **different** color for each **part** of the icon. We want to fill each **path** with a different color, without altering other instances, and we want to be able to override it if necessary.

At first, you might be tempted to rely on specificity.

```
// HTML<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path class="path1" d="..." />    <path class="path2" d="..." />    <path class="path3" d="..." />  </symbol></svg>
```

```
<svg class="icon icon-colors">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors .path1 {  fill: red;}.icon-colors .path2 {  fill: green;}.icon-colors .path3 {  fill: blue;}
```

**This won’t work.**

We’re trying to style `.path1`, `.path2` and `.path3` as if they were nested in `.icon-colors`, but technically speaking **they’re not**. The `<u`se> element is**n’t a place**holder that gets replaced by your SVG definition. I**t’s a ref**erence which clones the content it’s pointing to int[**o the shad**](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Shadow_DOM)ow DOM ?

**What can we do then?** How can we affect children content in a scoped way when said children aren’t in the DOM?

### CSS variables to the rescue

In CSS, [some properties](https://developer.mozilla.org/en-US/docs/Web/CSS/inheritance) are inherited from ancestors to children. If you assign a text color to the `body`, all the text in the page will inherit that color until it’s overridden. The ancestor isn’t aware of the children, but the **inheritable** styles are still propagated.

In our early example, we inherited the `fill` property. Look again, and you’ll see that the class in which we declared a `fill` color is appended on the **instances**, not the definitions. This is how we were able to get different colors for each instance of a single definition.

Now here’s the problem: we want to pass **different** colors to **different** paths of the original SVG, but there’s only one `fill` attribute we can inherit from.

Meet **CSS variables**.

CSS variables are declared within rulesets just like any other property. You can name them anything you want, and assign them any valid CSS value. Then, you declare it as a **value** for itself, or any child property, and **it will be inherited**.

```
.parent {  --custom-property: red;  color: var(--custom-property);}
```

_All children of `.parent` will have red text._

```
.parent {  --custom-property: red;}.child {  color: var(--custom-property);}
```

_All `.child` nested in `.parent` elements will have red text._

Now let’s apply this concept to our SVG symbol. We’ll use the `fill` attribute on each path of the SVG definition, and set them to different CSS variables. Then, we’ll assign them different colors.

```
// HTML<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path fill="var(--color-1)" d="..." />    <path fill="var(--color-2)" d="..." />    <path fill="var(--color-3)" d="..." />  </symbol></svg>
```

```
<svg class="icon icon-colors">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors {  --color-1: #c13127;  --color-2: #ef5b49;  --color-3: #cacaea;}
```

And… **it works**! ?

![Image](https://cdn-media-1.freecodecamp.org/images/YsRaKkdEcVKJNcnPE1ezPjuEt1eVAOmOvNq6)

From now on, all we need to do to create an instance with a different color scheme is to create a new class.

```
// HTML<svg class="icon icon-colors-alt">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors-alt {  --color-1: brown;  --color-2: yellow;  --color-3: pink;}
```

If you still want to have monochrome icons, **you don’t have to repeat the same color on every CSS variable**. Instead, you can declare a single `fill` rule: because CSS variables aren’t defined, it will fall back on your `fill` declaration.

```
.icon-monochrome {  fill: grey;}
```

_Your `fill` declaration will work because the `fill` attributes on the original SVG are set with undefined CSS variables values._

### What to name my CSS variables?

There are usually two routes you can take when it comes to naming things in CSS: **descriptive** or **semantic**. Descriptive means calling a color **what it is**: if you’re storing `#ff0000`, you’d call it `--red`. Semantic means calling the color by **how it’s applied**: if you’re using `#ff0000` for the handle of a coffee cup, you’d call it `--cup-handle-color`.

Descriptive names might be your first instinct. It feels DRYer since `#ff0000` can be used for other things than the handle of the coffee cup. A `--red` CSS variable is reusable for other icon paths that need to be red. After all, this is how utility-first CSS works and [it’s a fine system](https://frontstuff.io/in-defense-of-utility-first-css).

Problem is, in our case **we can’t apply granular classes to the elements we want to style**. Utility-first principles can’t apply, because we have a single reference for each icon, and we have to style it through class variations.

Using semantic class names, like `--cup-handle-color` for example, makes more sense for this use case. When you want to change the color of a part of an icon, you instantly know what it is and what to override. The class name will remain relevant no matter what color you assign.

### To default or not to default

It’s tempting to make the multi-colored version of your icons their default state. This way, you could use them with no need for extra styling, and you would add your own classes only when necessary.

There are two ways to achieve that: **:root** and **var() default**.

### :root

You can define all your CSS variables on the `:root` selector. This keeps them all in one place and allows you to “share” similar colors. `:root` has the lowest priority, so it remains easy to override.

```
:root {  --color-1: red;  --color-2: green;  --color-3: blue;  --color-4: var(--color-1);}
```

```
.icon-colors-alt {  --color-1: brown;  --color-2: yellow;  --color-3: pink;  --color-4: orange;}
```

However, **there are major drawbacks to this method**. First, keeping color definitions separate from their respective icons can be confusing. When you decide to override them, you have to go back and forth between the class and the `:root` selector. But more importantly, **it doesn’t allow you to scope your CSS variables**, thus keeps you from reusing the same names.

Most of the time, when an icon only uses one color, I use the `--fill-color` name. It’s simple, understandable, and it makes sense to use the same name for all icons that only need one fill color. If I have to declare all variables in the `:root` declaration, I can’t have several `--fill-color`. I’ll be forced to define `--fill-color-1`, `--fill-color-2`, or use namespaces like `--star-fill-color`, `--cup-fill-color`.

### var() default

The `var()` function, which you use to assign a CSS variable to a property, can take a default value as a second argument.

```
<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path fill="var(--color-1, red)" d="..." />    <path fill="var(--color-2, blue)" d="..." />    <path fill="var(--color-3, green)" d="..." />  </symbol></svg>
```

Until you define `--color-1`, `--color-2` and `--color-3`, the icon will use the default values you set for each `<pa`th>. This solves the global scope issue we have when `using` :root, but be car**eful: you now have a default value and it’s doing i**ts job. As a result, you can’t use a s`ingl`e fill declaration to define monochrome icons anymore. You’ll have to assign the color to every CSS variable used on the icon, one by one.

Setting default values can be useful, but it’s a tradeoff. I suggest you don’t make it a habit, and only do it when it makes sense for a given project.

### How browser-friendly is all that?

[CSS variables are compatible with most modern browsers](https://caniuse.com/#feat=css-variables), but as you probably expect it, Internet Explorer doesn’t support it **at all**. Not even IE11, and since development was discontinued in favor of Edge, there’s no chance it will ever get up to speed.

Now, just because a feature isn’t supported by a browser you need to cater to, that doesn’t mean you have to rule it out altogether. In such cases, go for **graceful degradation**: offer multi-colored icons to modern browsers, and provide a fallback fill color for older ones.

What you want to do is set a declaration that will only work if CSS variables aren’t supported. This can be achieved by setting the `fill` property to the fallback color: if CSS variables are supported, it won’t even be taken into account. If they’re not, your `fill` declaration will apply.

If you’re using Sass, this can be abstracted into a `@mixin`.

```
@mixin icon-colors($fallback: black) {  fill: $fallback;  @content;}
```

We can now define color schemes without worrying about browser compatibility.

```
.cup {  @include icon-colors() {    --cup-color: red;    --smoke-color: grey;  };}
```

```
.cup-alt {  @include icon-colors(green) {    --cup-color: green;    --smoke-color: grey;  };}
```

_Passing the CSS variables in the mixin through `@content` is optional. If you do it outside, the compiled CSS will be the same. But it can be helpful to package it all in one place: you can fold snippets in your editor and visually identify declarations that go together._

Check out [this pen](https://codepen.io/sarahdayan/pen/GOzaEQ/) on different browsers. On up-to-date versions of Firefox, Chrome, and Safari, the last two cups will respectively be red with grey smoke and blue with grey smoke. On Internet Explorer and Edge before version 15, the third cup will be all red and the fourth will be all blue! ✨

If you want to learn more about SVG symbol icons (and SVG in general), I **strongly** suggest you read [everything by Sara Soueidan](https://www.sarasoueidan.com/blog). And if you have any question about CSS symbol icons, don’t hesitate to hit me up on [Twitter](https://twitter.com/frontstuff_io)!

_Originally published at [frontstuff.io](https://frontstuff.io/multi-colored-svg-symbol-icons-with-css-variables)._

