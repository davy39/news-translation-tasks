---
title: How to Render an Array of Components in React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-27T19:18:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-render-array-of-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Array-components.png
tags:
- name: arrays
  slug: arrays
- name: components
  slug: components
- name: React
  slug: react
seo_title: null
seo_desc: 'In this tutorial, I will show you how using indices to render an array
  of components in React can be problematic. I''ll also teach you how to mitigate
  array rendering issues with unique ids.

  As always, we''ll work on a real world example and solve prob...'
---

In this tutorial, I will show you how using indices to render an array of components in React can be problematic. I'll also teach you how to mitigate array rendering issues with unique ids.

As always, we'll work on a real world example and solve problem I stumbled across while building my 2048 Game in React. All the code snippets are inspired by this project. If you want to review the code before reading this article, you can [find it on GitHub](https://mateuszsokola.github.io/2048-in-react/).

## The 2048 Game

Let me explain the rules of the 2048 game first. The player must combine tiles that have the same numbers until they reach the number 2048. The tiles can contain only numbers that represent a power of two starting from 2 – this means 2, 4, 8, 16, 32, and so on – until they reach the number 2048. The board has dimensions of 4 x 4 tiles, so that it can fit up to 16 tiles.

Here's an example:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/demo-1.gif)
_2048 Game Preview_

In this article, I will only teach you how to render arrays in React and show you some best practices when comes to rendering lists in React components. 

Unfortunately, we cannot create the entire game because it would make this article confusing. But if you want to do it from scratch, you should consider enrolling to my [course on Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106) where I will walk you through creating the 2048 Game with animations in React 18.

## **P**rerequisites****

Before we start, make sure you know some basics of React. Nothing sophisticated – just be sure you've worked with React before, otherwise you might feel a bit lost.

If you don't yet know React, freeCodeCamp has a [5-hour React course for beginners](https://www.freecodecamp.org/news/learn-react-course/) so feel free to watch it before reading this article. You can also enroll in my [React 18 course](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106).

Now let's get started.

## **How to Render Array Elements**

As I mentioned at the beginning, the game board has dimensions of 4 x 4 tiles. That means the best data structure to store tiles on the board will be a multidimensional array, like the one you see below:

```js
const board = [
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 0],
]
```

Unfortunately, this data structure will be expensive, since it requires nested loops iterating across each other. That's why I decided to flatten this array into a one-dimensional one:

```js
const tilesOnBoard = [0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]
```

As you can see, there are a lot of empty elements in this array, and it gives room for further improvements. We can reduce the amount of operations by replacing tile values with objects containing tile information. 

For example, you can introduce a new type to store the meta data of every tile like this:

```ts
type TileModel = {
  position: [number, number];
  value: number;
};

```

As you can see, this data type makes tiles smart. Every tile will know its position and value. I decided to store the position as an array of two elements. These elements will represent `x` and `y` coordinates. Rather than pixels, I will use array indices on the board array I mentioned in the first step.

Now let's improve the `tilesOnBoard` array and make it store only existing tiles without empty values:

```js
const tilesOnBoard = [
	{ position: [1, 0], value: 2 },
    { position: [2, 0], value: 2 },
]
```

Thanks to this simplification, I can render tiles by using the simple `map` functor that will iterate through all array elements and create Tile components out of them.

```jsx
const renderTiles = () => {
  return tilesOnBoard.map((tile: TileModel, index: number) => (
    <Tile key={index} {...tile} />
  ));
};
```

Let's focus on the second argument of the `map` functor for a moment. As you can see, it uses the item index of the `tilesOnBoard` array. I am using it as a `key` property to initialize React components – in this case `Tile` components.

If you've never used `key` props, React needs keys to identify which elements have changed, are added, or are removed. Keys should be assigned to every item inside the array of components. 

That's why I assigned array indices to all tiles. Unfortunately, array indices aren't the best unique identifiers, as you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/array-indexes.gif)
_Strange behavior when array indices are used as key props_

It might be hard to spot what's happening here, so let me briefly explain. Basically, React is reusing existing HTML elements to render new tiles. This isn't an intended behavior – instead, I should have removed merged tiles and created a new tile after every move. 

But why is this happening? After the tiles are getting merged, a new tile is created, and that means the array still has two elements with the same array indices. 

React uses a mechanism called the Virtual DOM to detect changes and modify elements on the DOM tree. Unfortunately, this mechanism is optimized for speed so that it doesn't analyze the entire component but only the `key` prop. This means React cannot differentiate the new tile creation from a style change on an existing div element. That's why we are experiencing this issue.  
  
To confirm that my reasoning is right, let's take a brief look at the _Element_ tab in Chrome DevTools:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/reusing-html-elements.gif)
_DOM Element reusability due to array indices used as key props_

As you can see, two existing div elements only changed their style attributes but nothing was added or removed. This isn't an intended behavior, but it tells us that array indices are poor unique identifiers for React components.

If you aren't familiar with Chrome Developer Tools, you should read my article on implementing [mobile touch events in React 18](https://www.freecodecamp.org/news/how-to-build-mobile-swiping-component-in-react/) where I do a deep dive on how to use it. 

## **Unique Identifiers As Key Props**

To fixing array rendering problems in React, we'll need to use some unique identifiers such as incremental ids, uuids, or others. To focus on the essentials, I decided to use a library called `uid`, which you can install by running the following in your terminal: 

```bash
npm install --save uid
```

Now I need to modify tiles to support those identifiers. First, I added a new property `id` in the tile meta data type:

```ts
type TileModel = {
  id: string;
  position: [number, number];
  value: number;
};
```

And I assigned an id to every element in the  `tilesOnBoard` array (here's where the `uid` library comes into play):

```js
const tilesOnBoard = [
	{ id: uid(), position: [1, 0], value: 2 },
    { id: uid(), position: [2, 0], value: 2 },
]
```

The last thing I did was to change the `renderTiles` helper:

```jsx
const renderTiles = () => {
  return tilesOnBoard.map((tile: TileModel) => (
    <Tile key={tile.id} {...tile} />
  ));
};
```

As you can see, I removed an index argument from the `map` functor, and replaced the `key` prop with an unique id which I added to the tile meta data.

Now the 2048 game works like a charm:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/array-tile-ids.gif)

## **Conclusion**

In this article, you learned that indices aren't the best option to render arrays of components in React and that they might lead to strange behaviors. If there is only one thing you should remember from this article it's that you should always use unique identifies as the `key` prop of React components.

Wanna learn more tricks like this one? You should join to my [React 18 course on Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106). I will teach you how to **create 2048 game in React** from scratch and show you solutions to the most common mistakes React developers make.

