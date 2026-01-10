---
title: 'The Inverted Triangle Architecture: how to manage large CSS Projects'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-05T15:58:12.000Z'
originalURL: https://freecodecamp.org/news/managing-large-s-css-projects-using-the-inverted-triangle-architecture-3c03e4b1e6df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l6ZhrrSG2cqp_ObV1jZrgQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luuk Gruijs

  You’re assigned a small task to fix some little styling issues here and there. You’ve
  found the correct CSS rules to apply the fix, so you quickly drop those rules at
  the bottom of your CSS file, push your changes, and then move on wit...'
---

By Luuk Gruijs

You’re assigned a small task to fix some little styling issues here and there. You’ve found the correct CSS rules to apply the fix, so you quickly drop those rules at the bottom of your CSS file, push your changes, and then move on with more important stuff.

Over time this happens a couple of times and before you know it “the bottom” of your CSS file consists of a few hundred lines of code that nobody understands and nobody dares to remove as it will inevitably break stuff.

Do you recognize this scenario because you’ve either done this yourself or you’ve seen colleagues do this? Well, read on and promise yourself that you will never do this again, because here’s an easier way to manage your CSS files.

### Introducing the Inverted Triangle architecture

The Inverted Triangle architecture, also know as ITCSS, is a methodology for structuring your CSS in the most effective and least wasteful way.

ITCSS was first introduced by Harry Roberts and can be best visualized by an upside-down, layered triangle. ITCSS defines the shared CSS-rules of a project in a logical and sane manner, whilst also providing a solid level of encapsulation and decoupling that which prevents non-shared CSS-rules from interfering with one another.

ITCSS is very flexible as it does not force you to use any specific naming convention methodologies like SMACCS, OOCSS or BEM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4oGYOCrfBqsjnqGwZ_GaHg.jpeg)

### The principles

ITCSS works by structuring your entire CSS project according to these 3 principles:

1. **Generic to explicit**  
We start with the most generic, low-level, catch-all styles. This could be font settings or, for example, color variables if you’re using SCSS.
2. **Low to high specificity**  
The lowest specificity selectors appear at the start of your project. The specificity steadily increases. This way we avoid specificity conflicts and specificity overrides using `!important`.
3. **Far-reaching to localized**  
Selectors at the start of our project affect a lot of DOM-elements, for example your browser reset styles, while selectors later in our project become very localized, for example specific styles for one component.

### The triangle layers

Sticking to the above principles means we have to break up our CSS into layers. Each layer must be introduced in a location that honors each of the criteria.

It happens often that CSS is grouped by, for example, typographic styles, form styles, and styles for a specific component. These groups are often not imported in the most efficient order and this creates some inheritance or specificity problems.

In ITCSS, each layer is a logical progression from the last. It increases in specificity, narrows in reach and gets more explicit. This means our CSS is easier to scale, as we’re only adding to what is already there and not overriding what was previously written.

Another big advantage of following this structure is that everybody always knows where to find certain CSS rules as they’re logically placed. This avoids the issue of people dropping their CSS rules at the bottom of the file.

Harry Roberts, the creator of ITCSS, laid out seven layers. He ordered them as follows:

1. **Settings**  
If you’re using a preprocessor like SCSS, this is your starting point. In this layer you define your variables.
2. **Tools**  
This layer can be used for your tooling. Think about mixins and functions that need to be globally available. If they don’t need to be, just place them in the layer where they’re needed.
3. **Generic**  
In this layer, we house all the very high-level, far reaching styles. This layer is often the same across all your projects as it contains things like Normalize.css, CSS resets, and for example box-sizing rules.
4. **Elements**  
In this layer we put styles for bare, unclassed HTML elements. You could, for example, think about underlines for anchors on hover or font-sizes for the different headings.
5. **Objects**  
In the object layer we style the first elements that have classes. Think about your containers, wrappers or rows. You can also define your grid here.
6. **Components**  
The component layer is the place where most of the styling magic happens as you will be styling your UI elements here. In component based frameworks like Angular, Vue or React this is the layer where you import your styling for each component if you don’t include them directly in your component.
7. **Trumps**  
The trumps layer is the dirty layer. Even after structuring your styling according to the ITCSS principles it can happen that you have to use `!important` to override some third-party styling, for example. Do that in this layer as this is the most specific, local and explicit layer.

### The end result

Now that I’ve explained the layers, it’s time to look at how a simple end result could potentially look.

```
// settings@import "globals";@import "branding";
```

```
// tools@import "mixins";
```

```
// generic@import "normalize";
```

```
// elements@import "fonts";@import "form";
```

```
// objects@import "grid";@import "wrappers";
```

```
// components@import "header";@import "sidebar";@import "carousel";@import "card";
```

```
// trumps@import "overrides";
```

### Conclusion

Just as ITCSS doesn’t force you to use a certain naming conventions, it doesn’t force you to use all layers. Use a layer structure that works best for you while maintaining the ITCSS principles of generic to explicit, low to high specificity and far-reaching to localized.

If you notice that you have to override styles, it almost always means your structure is inefficient. If you feel like learning more about this, I recommend watching this video:

### Looking for a job in Amsterdam?

I work for **Sytac** as a Senior front-end developer and we are looking for medior/senior developers that specialise in Angular, React, Java or Scala. Sytac is an ambitious consultancy company in the Netherlands that works for a lot of renowned companies in the banking, airline, government and retail sectors.

If you think you have what it takes to work with the best, send me an email at [luuk[dot]gruijs[at]sytac[dot]io](mailto:luuk.gruijs@sytac.io) and I’d be happy to tell you more.

