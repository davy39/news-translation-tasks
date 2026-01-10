---
title: How to make a custom theme in Angular Material
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T00:37:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-custom-theme-in-angular-material-d47122a1e361
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u2PGM1dBW-M9oaRPMAVCXA.jpeg
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
- name: Material Design
  slug: material-design
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Charlee Li

  Angular Material is a great library that implements Material Design for Angular
  2+. The official document is sufficient regarding the component usages, while there
  are few articles about how to customize the theme itself, specifically, ...'
---

By Charlee Li

[Angular Material](https://material.angular.io/) is a great library that implements [Material Design](https://material.io/design/) for Angular 2+. The official document is sufficient regarding the component usages, while there are few articles about how to customize the theme itself, specifically, the colors used in the theme.

In this post I would like to summarize what I’ve learned these months from customizing Angular Material themes.

_Note this article is NOT about [AngularJS Material](https://material.angularjs.org/latest/), which is used for [AngularJS 1.x](https://angularjs.org/)._

### Related Posts

Some common posts about customizing themes are:

* “[Theming your Angular Material app](https://material.angular.io/guide/theming)”, the official guide for custom themes,
* “[The complete guide to Angular Material Themes](https://medium.com/@tomastrajan/the-complete-guide-to-angular-material-themes-4d165a9d24d1)” by [Tomas Trajan](https://medium.com/@tomastrajan?source=post_header_lockup), which provides many undocumented instructions. **Strongly recommended**.

I didn’t find other useful posts and would appreciate if anyone could provide some resources in the comments.

### How to Create a Custom Theme

Creating a material theme is extremely simple: you only need to pick three colors — **primary**, **accent**, and **warn** — and Angular Material will do the rest for you. [The material palette page](https://material.io/design/color/#tools-for-picking-colors) explains how it works clearly, and you can also create a theme visually with [Color Tool](https://material.io/tools/color/).

In regards to code, all you need to do is to create the following theme file:

```
// theme.scss@import '~@angular/material/theming';
```

```
$my-theme-primary: mat-palette($mat-green);$my-theme-accent : mat-palette($mat-amber);$my-theme-warn   : mat-palette($mat-red);
```

```
$my-theme: mat-light-theme(    $my-theme-primary,    $my-theme-accent,    $my-theme-warn);
```

Then you need to apply this theme in your main `style.scss` file:

```
@import "theme.scss";
```

```
@include mat-core();@include angular-material-theme($my-theme);
```

### How to Use Custom Theme in Components

After creating our own theme, requirements like this will rise:

> I want to create a text box. The text color, background color, and border color should all come from our own theme, not by hard coding.

This requirement is pretty common — anyway, being able to be used in components is exactly why we want to create a custom theme. The problem is how.

#### The mixin approach

The first official document I shared proposed a way of using SCSS’s mixin. I call it a “bottom-up” approach, which includes the following steps:

1. Each component defines a theme mixin, and retrieves colors from `$theme` parameter.
2. A global `theme.scss` defines the custom theme, then includes all the component theme mixins and calls them with the custom theme.

![Image](https://cdn-media-1.freecodecamp.org/images/ZZFo93hwLrqUn3ntyKFegxNciXyufD0I3nnv)

In addition to the `theme.scss` definition mentioned above, each component needs to create a theme file like this:

```
// src/app/comp-a/comp-a.theme.scss@import '~@angular/material/theming';
```

```
@mixin comp-a-theme($theme) {          // define mixin  $primary: map-get($theme, primary);  // retrieve color def  button {                             // apply theme to component    background-color: mat-color($primary);  }}
```

And probably you want a `custom-theme.scss` to import all the component level themes:

```
// src/app/custom-theme.scss@import '~@angular/material/theming';@import 'src/app/comp-a/comp-a.theme';@import 'src/app/comp-b/comp-b.theme';
```

```
@mixin custom-themes($theme) {  @include comp-a-theme($theme);  @include comp-b-theme($theme);}
```

Then import the above `custom-theme.scss` in your `theme.scss`:

```
// theme.scss...@import './custom-theme';@include custom-themes($my-theme);
```

This hierarchy works, and probably is the only way _when you need to support multiple themes_.

However, most of the time we only support one theme, and using a mixin could be cumbersome. Mainly there are three disadvantages with this approach:

1. Every single color reference needs a separate `.theme.scss` file.
2. `custom-theme.scss` must know exactly which components provide custom themes. This creates unnecessary dependencies.
3. Most importantly, component level theme files are not encapsulated.

The first and second points are pretty self-explanatory. Let me explain a little bit about point 3. This involves some background knowledge called “View Encapsulation”.

Angular uses a technique called “[View Encapsulation](https://angular.io/api/core/ViewEncapsulation)” to [keep component CSS local](https://angular.io/guide/component-styles). In other words, rules defined for one component will stay in that component and will not affect other components.

In this way you can define CSS class name freely in your component without worrying about naming conflicts. However, view encapsulation is done only if the CSS is defined through `@Component`, i.e. `@Component({ styleUrls: ['./comp-a.scss'] })`.

As to our custom theme file `comp-a.theme.scss`, since it is imported directly by `custom-theme.scss`, _its rules are not encapsulated_ so it will apply to all elements on the page. In the example above, I used the following code (which was WRONG!):

```
@mixin comp-a-theme($theme) {  button { ... }    // This will apply to ALL buttons!}
```

But this will apply the style to all the buttons instead of those buttons belonging to `comp-a` only. You have to do something like `comp-a button` in order to make this work correctly.

#### The direct approach

Therefore I propose a better approach. Instead of using a mixin, we let each component include the theme file and use the color definition directly.

In this approach, the component theme file will look like this:

```
// NOTE: just do this in your regular scss file.// No need to create separate theme file!// src/app/comp-a/comp-a.scss@import 'src/theme.scss';
```

```
$primary: map-get($my-theme, primary);button {  background-color: mat-color($primary);}
```

And that’s all.

Let’s see how this works. First, theme related rules are put into the component SCSS file, so no extra component level theme file required. Second, the main `theme.scss` does not need to know component level themes (since it does not need to import them), so a simple theme definition is adequate. Third, the component SCSS file is used with `@Component` so it is encapsulated correctly, which means we can simply define rules for `button`.

### Predefined Theme Keys

Probably you have noticed the next problem. What are the `foreground`, `primary` in above theme files ( `map-get($my-theme, primary)`)? Are there any other keys I can use?

Well these “keys” refer to different colors defined in the theme. However I could not find any documents explaining these “keys”, so the only way I could find out is to _read the source code_. (Although it is said that good programmers should read the code, _having_ to read the code is definitely not a good sign for a library.)

Open `node_modules/@angular/material/_theming.scss` and you will see the definitions for these keys. For future reference, I would like to summarize the keys here.

```
$theme  |- primary  |- accent  |- warn  |- foreground  |   |- base  |   |- divider  |   |- dividers  |   |- disabled  |   |- disabled-button  |   |- disabled-text  |   |- hint-text  |   |- secondary-text  |   |- icon  |   |- icons  |   |- text  |   |- slider-min  |   |- slider-off  |   `- slider-off-active  |- background  |   |- status-bar  |   |- app-bar  |   |- background  |   |- hover  |   |- card  |   |- dialog  |   |- disabled-button  |   |- raised-button  |   |- focused-button  |   |- selected-button  |   |- selected-disabled-button  |   |- disabled-button-toggle  |   |- unselected-chip  |   `- disabled-list-option  `- is-dark         // bool, whether dark theme or not
```

For example, if you want to render a disabled text in your component, you may want to use the following code:

```
$foreground: map-get($my-theme, foreground);.disabled-text {  color: mat-color($foreground, disabled-text);}
```

Okay these are some lessons I’ve learned from struggling with Angular Material. Hope this post is helpful if you are facing similar problems.

