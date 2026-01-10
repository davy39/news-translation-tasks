---
title: React + RESS = More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T11:27:47.000Z'
originalURL: https://freecodecamp.org/news/react-ress-awesome-6086d784195
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cBoVlAjRrKCOKIaBNnW1Kg.png
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bukhari Muhammad

  RESSheet (React Evaluated StyleSheet), better known as RESS, is a tiny pre-processor
  that aims to be for React (Native) what LESS is to CSS. RESS uses a LESS-like styling
  approach to avoid repetitive style definitions. I styled th...'
---

By Bukhari Muhammad

**RESSheet** (_React Evaluated StyleSheet)_, better known as **RESS**, is a tiny pre-processor that aims to be for **React** (**Native**) what **LESS** is to **CSS**. **RESS** uses a **LESS**-like styling approach to avoid repetitive style definitions. I styled the following buttons totally in **RESS.**

![Image](https://cdn-media-1.freecodecamp.org/images/6G2CRgMl8N-hczD8LIJFYplxVQyfqVGPAtlI)
_The code to accomplish this could be found in this [Gist](https://gist.github.com/bukharim96/e0b415d99847aac3799bc25b33873a83" rel="noopener" target="_blank" title=")._

#### A bit of history

I first got hit with the idea to write a better styling solution for **React** while working on a new **UI** package for **React Native**. During development, one of the first issues that bothered me about the traditional `StyleSheet` component is its enormous lack of significant features that **CSS** presented. In addition, **inline-styling** is pretty taboo for someone who spent the last half-decade preaching against it. I get religious about this.

I started building a Bootstrap-like button component for my **UI** framework. I first made use of the `StyleSheet` component to achieve this, I ended-up using a series of `if` statements in order to check whether certain props existed before styling the button accordingly. Example: `<Button primary>Submit<`;/Button> should’ve rendered out a blue button, and so forth.

The `<Butt`on> component’s file size became unnecessarily large due to this inefficient method. It wasn’t long before I decided to ditched this tedious styling technique and searched for a more robust solution.

I began by testing out some packages that attempted to provide better styling in **React** — namely: [styled-components](https://www.npmjs.com/package/styled-components), [radium](https://www.npmjs.com/package/radium) and [glamorous](https://www.npmjs.com/package/glamorous) — only to discover that most had their own share of cons. I mainly did not appreciate the performance curve and large package size that most of them entailed. And worst of all, none of them had support for **React Native**.

I finally came to the resolve that I should just build a simple solution that catered for my needs and that of the lot out there that share my dread. I basically wanted a solution that would make me more comfortable writing styles for both **React** and **React Native** components.

Hailing from a ‘LESS is more’ background, I decided to write a light-weight package that mimics some of my favorite **CSS** and **LESS** features — such as multi-selectors (done via props), nested-styling and the cascading styles feature. All this without compromising performance or introducing a completely foreign approach with a high-learning-curve.

This is what lead to the idea of **RESS**.

#### Under the hood

**RESS** outputs a style object based on two required arguments, namely: a `props` object and a **RESSheet** object. It automatically validates the existence of the props and returns the corresponding styles of the ‘selectors’ (object keys) supplied in the **RESSheet** object. The **RESSheet** object is an ordinary **React StyleSheet** object — the one used in `StyleSheet.create({…})` — with a few extra useful features:

* The `default` selector which applies to the component automatically. Examle: `default: {fontSize: 16}` — this would apply to the component initially regardless of its `props`.
* The ability to specify **multi-props** as selectors — `‘h1, h2, h3, h4, h5, h6’: {fontWeight: ‘bold’}`, this would _bolden_ the text of a component with any of the h1 — h6 range of props.
* **Nested-styles** — a component with the following **RESSheet** would be hidden by default, and shown when it has an `active` prop, this could be used in tab / accordion behaviour:

![Image](https://cdn-media-1.freecodecamp.org/images/0f874h5o2Huo7M-SlRTv1O6TJKRU7b9H6wHA)

The returned object will then be placed in the `style` property of the component.

I’ve slated a few more great features to add to **RESS** for the near foreseeable future.

#### RESS in comparison to other solutions

In comparison to **RESS**, one could argue that the default `StyleSheet` component is pretty-much an anti-**DRY** (Dont Repeat Yourself) pattern in handling component styles. I’ve noticed this when I ended up with a flood of `if` statements on trying to style a component dynamically.

I find [styled-components](https://www.npmjs.com/package/styled-components) to be the closest to rival **RESS**, had it only been for its performance issues and huge file size. Not to mention, its lack in error reporting and syntax highlighting, which is due to the use of ES6 template strings. I did not bother reading its humongous script, since one could imagine the type of `string` parsing and interpretation that takes place under its hood — from possibly converting **CSS** style properties all the way to regex complexities.

In contrast, **RESS** uses **style-objects** instead of interpreted `strings` in order not to sacrifice **React**’s powerful error reporting and the syntax highlights of your favorite text editor.

Now don’t get me wrong, I think that [styled-components](https://www.npmjs.com/package/styled-components) along with the rest of the solutions I mentioned are a decent attempt add some flavor to **React**’s dull styling methods. All I’m saying is that they just don’t cut out to be the best way for me personally.

#### Bottomline…

**RESS** is just an awesome little script that allows me to write better **UI** for my React and React Native projects at a faster pace by leveraging **LESS**-like patterns to encourage abstraction and less repetition.

If you find it interesting make sure to clap to this post, star this project’s repository on [GitHub](https://github.com/bukharim96/ressheet) and give it a try by installing it via NPM:

```
npm install ressheet --save
```

To get updates on the progress of this repository along with some cool JavaScript / React related tips, follow me on twitter: [@bukharim96](https://twitter.com/bukharim96)

I’d like to hear positive responses and criticism, so feel free to do so. Enjoy ;)

