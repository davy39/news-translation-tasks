---
title: The Best File Structure for Your React Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-23T17:59:13.000Z'
originalURL: https://freecodecamp.org/news/best-file-structure-for-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/reactcomponents-1.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: null
seo_desc: "By Iva Kop\nCreating an adequate and scalable file structure for front\
  \ end projects can be challenging. The freedom we have when using un-opinionated\
  \ tools like React comes with a great deal of responsibility. \nUsually, when we\
  \ talk about file structu..."
---

By Iva Kop

Creating an adequate and scalable file structure for front end projects can be challenging. The freedom we have when using un-opinionated tools like React comes with a great deal of responsibility. 

Usually, when we talk about file structure, the discussion focuses on the project as a whole. But what is equally important (and often overlooked) is the question of how to best structure components.

Let me show you what I mean.

## What to include in the component directory

Components are the building blocks of every React app. As such, they can be treated as mini-projects in and of themselves. A component should be as self-contained as possible (but not more so).

A typical component directory might look something like this:

```
├── components
│   ├── Component
│   │   ├── SubComponent
│   │   │   ├── SubComponent.test.tsx
│   │   │   ├── index.tsx
│   │   ├──  Component.stories.tsx
│   │   ├──  Component.test.tsx
│   │   ├──  icon.svg
│   │   ├──  index.tsx
│   │   ├──  utils.ts
│   │   ├──  utils.test.ts


```

Let's break it down.

### Main index file

The default export from this file is the component itself.

In addition, the index could also include named exports. For example, if I am building a `Menu` component, I would like to be able to use it like this:

```
import Menu, { MenuItem } from 'components/Menu'

const ComponentWithMenu = () => {
    return (
        <Menu>
            <MenuItem />
            <MenuItem />
        </Menu>
    )
}


```

So, in my index file, I need to export `Menu` as the default export but also re-export the `MenuItem` subcomponent as a named export. In this way, I can later import both from the same place. 

The explicit re-export also helps document what is public (and intended to be used by the rest of the app) and what is private to the component.

> Note: There is an argument to be made that only the default export should be public and all the rest should remain private. To find out why I recommend a different approach, check out my article on [building non-trivial React components](https://blog.whereisthemouse.com/a-guide-to-building-non-trivial-react-components).

### Tests

Why put the tests here rather than in a separate `tests` directory? One word - colocation! 

Files that belong together should live together. The benefits of this approach become very clear if you imagine the process of editing or even deleting components. Maintenance is much simpler when everything is in one place.

In addition, tests often serve as documentation. So having them next to our component makes perfect sense.

### Story

[Storybook](https://storybook.js.org/) is an awesome tool for developing components in isolation. It allows us to truly treat our components as separate mini-projects. Colocating each story with its corresponding component is important for all the same reasons outlined above.

### Styles

When using CSS-in-JS, styled components can be created directly within the component file. If we have opted for CSS modules, the style files should be colocated with the component in its directory.

### Assets

Images, icons or other component-specific assets should be placed directly into the component directory. Once again - colocation!

### Utils

Utils can include everything from helper functions to custom hooks. We could separate them into different categories (hooks, services, and so on), if preferred, but the same basic principles apply. 

We should make sure all utils are component-specific and not something that is reused by other parts of the app. The tests for the utils are placed in the component directory.

### Sub-components

Sub-components are structured very similarly to the main component. They are usually used by the main component. 

If your intention is to use them throughout the app (as with out `MenuItem` example), they should be re-exported in the main index file. It should not be possible to use the sub-components without the main component. 

If this is the case, then the sub-component itself should become a main component.

The sub-components should have their own colocated unit tests (when needed), styles, and assets. Most of the time, stories are reserved for the main component only.

## What to keep outside of the component directory

Here is a good rule: if you ever feel tempted to use something other than what has been explicitly exported from the component's index, it is a clear signal that this particular piece of code should be placed elsewhere.

Let me give you an example.

Let's go back to our `Menu` component. Normally, we would expect that if a user clicks outside a menu, it should close. In order to do this, we have created a custom hook `useClickOutside` and placed it in utils. 

After a while, it becomes clear that we need the exact same behavior, this time for our `Dialog` component. 

We want to reuse our hook but, at the same time, it is no longer component-specific. We should take it out of the Menu component and place it higher up, maybe in our general utils folder.

**A note of caution**: Lifting code up to be reused should be done carefully and only when it is truly necessary. As developers, we are often tempted to [create abstractions too early](https://www.deconstructconf.com/2019/dan-abramov-the-wet-codebase) and without full context. This can have serious consequences for the maintainability of the project in the future. 

A lot of the time, if a piece of code does a similar (but not exactly the same) thing, it is better to replicate some of the functionality at first, and only create the abstraction when there is enough confidence in the use cases.

## Conclusion

Component structure is crucial for React architecture. Getting it wrong can have long-lasting consequences for the scalability and maintainability of projects. Which is why it is important to point out that what I propose above is just a template.

Although I have found this structure to be applicable to a wide range of scenarios, every React app is unique or, at the very least, has its idiosyncrasies. A generalized guide cannot replace thinking critically about the specifics of a project and making decisions accordingly.

_If you found this_ article _useful, [let's connect](https://twitter.com/iva_kop). For more in-depth React-related articles, check out [my blog](https://blog.whereisthemouse.com/)._

