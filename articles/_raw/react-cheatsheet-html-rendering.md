---
title: React Cheatsheet – 9 Common HTML Rendering Cases You Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-23T21:40:22.000Z'
originalURL: https://freecodecamp.org/news/react-cheatsheet-html-rendering
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/teaser.jpg
tags:
- name: cheatsheet
  slug: cheatsheet
- name: HTML
  slug: html
- name: React
  slug: react
seo_title: null
seo_desc: "By Ondrej Polesny\nWhenever I'm starting with a new framework or it's been\
  \ a while since I've used it, I always end up searching for the same simple things.\
  \ \nI'll Google how to render raw HTML, how to display a component based on a condition,\
  \ how to a..."
---

By Ondrej Polesny

Whenever I'm starting with a new framework or it's been a while since I've used it, I always end up searching for the same simple things. 

I'll Google how to render raw HTML, how to display a component based on a condition, how to assign a class to an element, and so on.

That's why I created this cheat sheet with the nine most common tasks you will perform on a regular basis with React [and JSX](https://reactjs.org/docs/introducing-jsx.html). 

I ordered them in the way I typically stumble upon them when building an application. In the examples below, the first code snippet will show the syntax, and the second one will show how to use it with real data.

## How to Output Data into HTML

The simplest use-case of all – render the value of a variable into HTML markup. It's usually the first test that shows you the app has processed the data and can render them:

```js
{ variable }
```
```js
{ metadata.subtitle.value }
```

## How to Add a Standard Class Attribute

While many frameworks keep the HTML markup untouched, React does not allow the reserved word "class" to be used for styling. We need to use `className` instead, like this:

```js
<... className="classname">
```
```js
<div className="sidebar__inner">
```

## How to Output Data into HTML Attributes

This use-case is related to building links. But in many cases, you also need to fill attributes like title, data-{something-your-app-needs}, or even simple alt tags of images:

```js
< ... name={variable}>
```
```js
<a href={`https://twitter.com/${author.twitter.value}`}>
```

## How to Output Raw HTML

Some content is structured in another system, for example, rich text composed in a headless CMS. 

In those cases, you typically use a tool like an SDK to build the HTML for you. This is how you can add it to your markup:

```js
< ... dangerouslySetInnerHTML={{__html: variable}}></...>
```
```js
<div dangerouslySetInnerHTML={{__html: article.teaser}}></div>
```

## How to Iterate Over Data Sets

On index pages, sitemaps, search pages, or wherever you need to display data from a collection, React and JSX allow you to combine the (almost) almighty `map` function with HTML markup:

```js
let components = collectionVariable.map((item) =>
  <Component data={item} key={item.uniqueKey} />);
...
<div>{components}</div>
```
```js
let articleComponents = articles.map((article) =>
  <Article data={article} key={article.id} ... />);
...
<div>{articleComponents}</div>
```

## How to Iterate Over Data Sets with an index

This is the same use case, but it gives you access to an index of each iterated item. In some cases, the index can also be used to replace unique key:

```js
let components = collectionVariable.map((item, index) =>
  <Component data={item} index={index} key={uniqueKey} />);
...
<div>{components}</div>
```
```js
let articleComponents = articles.map((article) =>
  <Article data={article} index={index} key={article.id} ... />);
...
<div>{articleComponents}</div>
```

## How to Render Conditional Markup

This is the typical _if_ condition in JSX. It's often used during data loading to display pre-loaders or to just decide which portion of the markup to use based on data:

```js
{variable !== null && <... >}
```
```js
{data.length > 0 && <div> ... </div>}
```

## How to Render Conditional Markup Including else branch

The else branch is achieved by reversing the condition:

```js
{variable !== null && <... >}
{variable == null && <... >}
```
```js
{data.length > 0 && <div> ... </div>}
{data.length == 0 && <div>Loading...</div>}
```

## How to Pass Data to Child Components

And finally, when you start using components, this is how you provide the children with data through props:

```js
<component componentVariable={variable}>
```
```js
<links author={author}>
```

I hope this saves you some Googling :-)

If you're looking for a printable (PDF) version, it's available on my [personal site](https://ondrabus.com/react-vue-angular-cheatsheet) where you'll also find similar cheatsheets for Vue and Angular.

