---
title: Ordered List in HTML – OL Tag Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-31T18:34:40.000Z'
originalURL: https://freecodecamp.org/news/ordered-list-in-html-ol-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/oltag--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'An ordered list is a list in which the items are numbered and the order
  matters.

  This is as opposed to an unordered list where the items are bulleted by default
  (and the order doesn''t matter).

  Basic Syntax of the <ol> tag

  The <ol> tag defines ordered...'
---

An ordered list is a list in which the items are numbered and the order matters.

This is as opposed to an unordered list where the items are bulleted by default (and the order doesn't matter).

## Basic Syntax of the `<ol>` tag

The `<ol>` tag defines ordered lists in HTML. And the list items are defined by the `<li>` tag. 

The `<ol>` tag is not an empty element, so it has a closing tag in `</ol>`
```html
<ol>
      <li>...</li>
      <li>...</li>
      <li>...</li>
</ol>
```

In browsers, ordered lists appear as numbered lists, like this:
```html
<ol>
   <li>HTML</li>
   <li>CSS</li>
   <li>JavaScript</li>
   <li>Tailwind</li>
   <li>React</li>
   <li>Mongo DB</li>
   <li>React</li>
</ol>
```
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.png)

If you are wondering why the list items are centered on the page, this CSS made it happen:
```css
body {
      display: grid;
      place-items: center;
      height: 100vh;
    }
```

## Attributes of the `<ol>` Tag

The `<ol>` tag accepts `start`, `type`, and `reversed` as attributes.

### The `type` Attribute

The `type` attribute is used to specify which type of numbering you want to use for the list.

The default is Arabic numerals.

The type of lists that can be used are:

- `1` for Arabic numerals (default)

```html
<ol type="1">
   <li>HTML</li>
   <li>CSS</li>
   <li>JavaScript</li>
   <li>Tailwind</li>
   <li>React</li>
   <li>Mongo DB</li>
   <li>React</li>
</ol>
```
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.png)

**P.S.:** If you will be using Arabic numerals as the numbering type, you don’t need to specify it since it’s the default.

- `A` for uppercase letters

```html
<ol type="A">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-2-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-4.png)

- `a` for lowercase letters

```html
<ol type="a">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-3-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-5.png)

- `i` for lowercase Roman numerals

```html
<ol type="i">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-4-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-5.png)

- `I` for uppercase Roman numerals

```html
<ol type="I">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-5-6](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-6.png)

### The `start` Attribute

The start attribute can be brought in to specify which number to start the list from. So, it accepts an integer as a value. The default is 1. 

If you specify a number like 22, the next list item takes the next number 23, on and on…

```html
<ol start="22">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-6-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-2.png)

### The `reversed` Attribute

When you use the `reversed` attribute on an ordered list, the list items are rendered in reverse order. That is, from the highest number to the lowest.

You don’t need to specify a value for the `reversed` attribute because any value you specify will be neglected.

```html
<ol reversed>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-7-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-3.png)

## Conclusion

In this article, you learned about the `<ol>` tag and its attributes, so you can have more control over it in your projects.

If you find this article helpful, don't hesitate to share it with your friends and family.


