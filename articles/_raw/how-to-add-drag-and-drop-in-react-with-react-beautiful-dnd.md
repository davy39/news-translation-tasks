---
title: How to Add Drag and Drop in React with React Beautiful DnD
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-10-05T16:38:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-drag-and-drop-in-react-with-react-beautiful-dnd
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/drag-and-drop-1.jpg
tags:
- name: React
  slug: react
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: null
seo_desc: "Drag and Drop is a common interaction technique added to allow people to\
  \ intuitively move things around on a page. This could be reordering a list or even\
  \ putting together a puzzle. \nHow can we add that interaction when building a React\
  \ app with Reac..."
---

Drag and Drop is a common interaction technique added to allow people to intuitively move things around on a page. This could be reordering a list or even putting together a puzzle. 

How can we add that interaction when building a React app with React Beautiful DnD?

* [What is Drag and Drop?](#heading-what-is-drag-and-drop)
* [What is React Beautiful DnD?](#heading-what-is-react-beautiful-dnd)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Creating a new React.js app](#heading-step-0-creating-a-new-reactjs-app)
* [Step 1: Installing React Beautiful DnD](#heading-step-1-installing-react-beautiful-dnd)
* [Step 2: Making a list draggable and droppable with React Beautiful DnD](#heading-step-2-making-a-list-draggable-and-droppable-with-react-beautiful-dnd)
* [Step 3: Saving list order after reordering items with React Beautiful DnD](#heading-step-3-saving-list-order-after-reordering-items-with-react-beautiful-dnd)

%[https://www.youtube.com/watch?v=aYZRRyukuIw]

## What is Drag and Drop?

Drag and drop is pretty much what it sounds like — it’s an interaction allowing someone to click and drag an item, then drop it somewhere else, often having a side effect within the app.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-board.gif)
_Moving items on a board_

This effect is pretty common in applications like to-do lists or project management dashboard, where you need to prioritize and create an order for how things should be done.

While drag and drop can have some advanced use cases, we’ll stick to basic list functionality for our walkthrough.

## What is React Beautiful DnD?

React Beautiful DnD is an accessible drag and drop library from Atlassian. If you don’t know of Atlassian, they’re the team behind Jira. If you’re not familiar with Jira, it’s probably the biggest Agile tool on the internet right now.

The team’s goals were to provide drag and drop capabilities with accessibility in mind, in addition to keeping it night and performant with a powerful API.

## What are we going to build?

We’re going to start off with a simple list and add the ability to drag and drop.

In this walkthrough, we won’t spend time building the list itself. The list that we’ll be using uses a standard unordered list (`<ul>`) and list items (`<li>`) to create a list with a little bit of CSS to make it look like cards.

We’ll be focusing on adding the ability to drag and drop to rearrange the list using React Beautiful DnD.

## Step 0: Creating a new React.js app

To get started, we want a simple app that includes a list of items. This can be an existing project or a brand new project using your favorite framework like [Create React App](https://create-react-app.dev/).

I started with a new app using Create React app and I added a simple list of [Final Space](https://www.tbs.com/shows/final-space) characters.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/list-of-final-space-characters-1.jpg)
_Final Space characters list_

If you want to start from the same place, you can clone my demo repository at that branch and start right along with me.

This command will clone [the specific branch](https://github.com/colbyfayock/my-final-space-characters/tree/part-0-starting-point) to get started:

```
git clone --single-branch --branch part-0-starting-point git@github.com:colbyfayock/my-final-space-characters.git

```

Otherwise, you can clone [the repository](https://github.com/colbyfayock/my-final-space-characters) as normal and check out the branch `part-0-starting-point`.

If you want to follow along with just the code, I first created an array of objects:

``` js
const finalSpaceCharacters = [
  {
    id: 'gary',
    name: 'Gary Goodspeed',
    thumb: '/images/gary.png'
  },
  ...

```

And then I loop through them to create my list:

```
<ul className="characters">
  {finalSpaceCharacters.map(({id, name, thumb}) => {
    return (
      <li key={id}>
        <div className="characters-thumb">
          <img src={thumb} alt={`${name} Thumb`} />
        </div>
        <p>
          { name }
        </p>
      </li>
    );
  })}
</ul>

```

[Follow along with the commit!](https://github.com/colbyfayock/my-final-space-characters/commit/8bfa61c32c1bdace7515a93a14427108056f3814)

## Step 1: Installing React Beautiful DnD

First step is to install the library via npm.

Inside of your project, run the following:

```
yarn add react-beautiful-dnd
# or
npm install react-beautiful-dnd --save

```

This will add the library to our project and we’ll be ready to use it in our app.

## Step 2: Making a list draggable and droppable with React Beautiful DnD

With our library installed, we can give our list the ability to drag and drop.

### Adding Drag and Drop context to our app

At the top of the file, import `DragDropContext` from the library with:

```jsx
import { DragDropContext } from 'react-beautiful-dnd';

```

[DragDropContext](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/drag-drop-context.md) is going to give our app the ability to use the library. It works similarly to React’s Context API, where the library can now have access to the component tree.

_Note: If you plan on adding drag and drop to more than one list, you need to make sure that your DragDropContext wraps all of those items, like at the root of your application. You can not nest DragDropContext._

We’ll want to wrap our list with DragDropContext:

```jsx
<DragDropContext>
  <ul className="characters">
  ...
</DragDropContext>

```

At this point, nothing will have changed with the app and it should still load as it did before.

### Making our list a Droppable area

Next, we want to create a Droppable area, meaning, this will allow us to provide a specific area where our items can be moved around inside.

First, add `Droppable` to our import at the top of the file:

```js
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

```

For our purpose, we want our entire unordered list (`<ul>`) to be our drop zone, so we’ll again want to wrap it with this component:

```jsx
<DragDropContext>
  <Droppable droppableId="characters">
    {(provided) => (
      <ul className="characters">
        ...
      </ul>
    )}
  </Droppable>
</DragDropContext>

```

You’ll notice we wrapped it a bit differently this time though. First, we set a `droppableId` on our `<Droppable>` component. This allows the library to keep track of this specific instance between interactions.

We’re also creating a function immediately inside of that component that passes in the `provided` argument.

Note: This function can pass in two arguments including a `snapshot` argument, but we won’t be using it in this example.

The [provided](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/droppable.md#1-provided-droppableprovided) argument include information and references to code that the library needs to work properly.

To use it, on our list element, let’s add:

```jsx
<ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>

```

This is going to create a reference (`provided.innerRef`) for the library to access the list element’s HTML element.  It also applies props to the element (`provided.droppableProps`) that allows the library to keep track of movements and positioning.

Again, at this point, there won’t be any noticeable functionality.

### Making our items Draggable

Now for the fun part!

The final piece of making our list elements draggable and droppable is wrapping each list item with a component similar to what we just did with the entire list.

We’ll be using the [Draggable](https://github.com/atlassian/react-beautiful-dnd/blob/master/docs/api/draggable.md) component, which again, similar to the Droppable component, will include a function where we’ll pass through props to our list item components.

First, we need to import Draggable along with the rest of the components.

```
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

```

Next, inside of our loop, let’s wrap the returning list item with the `<Draggable />` component and it’s top level function.

```jsx
{finalSpaceCharacters.map(({id, name, thumb}) => {
  return (
    <Draggable>
      {(provided) => (
        <li key={id}>
          ...
        </li>
      )}
    </Draggable>

```

Because we now have a new top level component in our loop, let’s move the `key` prop from the list element to Draggable:

```jsx
{finalSpaceCharacters.map(({id, name, thumb}) => {
  return (
    <Draggable key={id}>
      {(provided) => (
        <li>

```

We also need to set two addition props on `<Draggable>`, a `draggableId` and an `index`.

We’ll want to add `index` as an argument into our `map` function and then include those props on our component:

```jsx
{finalSpaceCharacters.map(({id, name, thumb}, index) => {
  return (
    <Draggable key={id} draggableId={id} index={index}>

```

Finally, we need to set some props on the list element itself.

On our list element, add this `ref` and spread additional props from the `provided` argument:

```jsx
<Draggable key={id} draggableId={id} index={index}>
  {(provided) => (
    <li ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>

```

Now, if we refresh our page, and hover over our list items, we can now drag them around!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-items-revert-state-1.gif)
_Dragging items on a list_

However, you’ll notice that when you start moving an item around, the bottom of the page appears to be a little messed up. There’s some overflow issues with our list items and our footer.

You’ll also notice that in the developer console, React Beautiful DnD is giving us a warning message that we’re missing something called a placeholder.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-warning-placeholder.jpg)
_Console warning - placeholder could not be found_

### Adding a placeholder from React Beautiful DnD

Part of React Beautiful DnD’s requirements is that we additionally include a placeholder item.

This is something that they provide out of the box, but this is used to fill up the space that the item we’re dragging previously took.

To add that, we want to include `provided.placeholder` at the bottom of our Droppable top level list component, in our case at the bottom of the `<ul>`:

```jsx
<Droppable droppableId="characters">
  {(provided) => (
    <ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>
      ...
      {provided.placeholder}
    </ul>
  )}
</Droppable>

```

And if we start dragging things around in our browser, we can see that our page flow doesn’t have issues and the content stays where it should!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-items-revert-fixed-spacing.gif)
_Dragging items with fixed spacing_

The last issue though, is when you move something around, it doesn’t stay, so how can we save the order of our items?

[Follow along with the commit!](https://github.com/colbyfayock/my-final-space-characters/commit/5ec5ee6c3e7de5b67a8fd46fdfbf157312bc8c00)

## Step 3: Saving list order after reordering items with React Beautiful DnD

When we move our items, they stay where they land for a split second. But after React Beautiful DnD finishes doing its work, our component tree will rerender.

When the components rerender, our items go back to the same place that they were before, because we never saved that outside of DnD’s memory.

To resolve this, `DragDropContext` takes in an `onDragEnd` prop that will allow us to fire a function after dragging has complete. That function passes in arguments that includes the new order of our items so that we can update our state for the next render cycle.

### Saving our list items in state

First, let’s store our items in state so that we’ll have something to update between cycles.

At the top of the file, add `useState` to the React import:

```
import React, { useState } from 'react';

```

Then, we’re going to create our state using our default list of items.

Add the following to the top of our App component:

```js
const [characters, updateCharacters] = useState(finalSpaceCharacters);

```

Because we’ll be updating our new `characters` state to provide our list items and their order, we’ll now want to replace the array we’re mapping through to our new state:

```jsx
<ul className="characters" {...provided.droppableProps} ref={provided.innerRef}>
  {characters(({id, name, thumb}, index) => {

```

And if we save and refresh our page, nothing should change!

### Updating state when dragging items

Now that we have our state, we can update that state any time our list items are dragged.

The `DragDropContext` component that we added to our page takes in a prop `onDragEnd`. Like it sounds, that will fire a function whenever someone stops dragging an item in the list.

Let’s add a function `handleOnDragEnd` as our prop:

```
<DragDropContext onDragEnd={handleOnDragEnd}>

```

Next, we need that function to actually exist.

We can define a function under our state:

```js
function handleOnDragEnd(result) {
}

```

Our function takes an argument called `result`.

If we add `console.log(result)` to the function and move an item in our list, we can see that it includes details about what should be the updated state after our move action.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/react-beautiful-dnd-ondragend-result.jpg)
_Dragged item result_

Particularly, we want to use the `index` value in both the `destination` and `source` properties, which tell us the index of the item being moved and what the new index of that item should be in the array of items.

So using that, let’s add the following to our function:

```js
const items = Array.from(characters);
const [reorderedItem] = items.splice(result.source.index, 1);
items.splice(result.destination.index, 0, reorderedItem);

updateCharacters(items);

```

Here’s what we’re doing:

* We create a new copy of our `characters` array
* We use the `source.index` value to find our item from our new array and remove it using the `splice` method
* That result is destructured, so we end up with a new object of `reorderedItem` that is our dragged item
* We then use our `destination.inddex` to add that item back into the array, but at it’s new location, again using `splice`
* Finally, we update our `characters` state using the `updateCharacters` function

And now after saving our function, we can move our characters around, and they save their location!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-drop-save-state.gif)
_Drag item with saved state_

### Preventing errors from dragging out of bounds

One issue with our implementation, is if someone doesn’t drag the item exactly within our defined containers, we get an error.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-out-of-container-error.gif)
_Error when dragging out of container_

The issue is that when we drag it outside of the defined container, we don’t have a destination.

To avoid this, we can simply add a statement above the code that moves our item around that checks if the destination exists, and if it doesn’t, exits out of the function:

```js
function handleOnDragEnd(result) {
  if (!result.destination) return;

```

And if we reload the page and try to drag our item out again, our item snaps back to the original location without an error!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/drag-out-of-container-snap-back.gif)
_Snap back when dragged out of container_

[Follow along with the commit!](https://github.com/colbyfayock/my-final-space-characters/commit/ad4f4733a974a27f5a2cfc8e366c2390809b74ca)

## What else can we do with React Beautiful DnD?

### Custom styles when dragging and dropping

When moving items, DnD will provide a snapshot of the given state. With this information, we can apply custom styles so that when we’re moving our items, we can show an active state for the list, the item we’re moving, or both!

[https://react-beautiful-dnd.netlify.app/?path=/story/single-vertical-list--basic](https://react-beautiful-dnd.netlify.app/?path=/story/single-vertical-list--basic)

### Dragging between different lists

If you’ve used Trello before or a tool like it, you should be familiar with the concept of different columns that you can drag cards between so that you can prioritize and organize your tasks and ideas.

This library allows you to do the same thing, providing the ability to drag and drop items from one draggable area to another.

[https://react-beautiful-dnd.netlify.app/?path=/story/multiple-vertical-lists--stress-test](https://react-beautiful-dnd.netlify.app/?path=/story/multiple-vertical-lists--stress-test)

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>

