---
title: A Better Way to Structure React Projects
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2021-02-02T22:54:52.000Z'
originalURL: https://freecodecamp.org/news/a-better-way-to-structure-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/z02wxvp94dwg84c4ifhj.jpeg
tags:
- name: Code Quality
  slug: code-quality
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Hello, everyone! A lot of e-ink has already been spilt on the relatively
  easier pickings of “Doing X in React” or “Using React with technology X”.

  So instead, I want to talk about the experiences I''ve had building frontends from
  scratch at DelightCha...'
---

Hello, everyone! A lot of e-ink has already been spilt on the relatively easier pickings of “Doing X in React” or “Using React with technology X”.

So instead, I want to talk about the experiences I've had building frontends from scratch at [DelightChat](https://delightchat.io/) and at my previous companies.

These projects require a deeper understanding of React and extended usage in a production setting.

If you want to watch a video version of this tutorial to supplement your reading, [you can do so here](https://www.youtube.com/watch?v=lViIdphWTwY).

%[https://www.youtube.com/watch?v=lViIdphWTwY] 

## Introduction

In a nutshell, a complex React project should be structured like this. Although I use NextJS in production, this file structure should be quite useful in any React setting.

```javascript
src
|---adapters
|---contexts
|---components
|---styles
|---pages
```

*Note: In the above file structure, the assets or static files should be placed in whatever the variant of* `public *` *folder for your framework is.*

For each of the above folders, let’s discuss them in order of precedence.

## 1\. Adapters

`Adapters` are the connectors of your application with the outside world. Any form of API call or websocket interaction which needs to happen, to share data with an external service or client, should happen within the adapter itself.

There are cases where some data is always shared between all the adapters – for example, sharing of cookies, base URL and headers across your AJAX (XHR) adapters. These can be initialized in the xhr folder, and then imported inside of your other adapters to be used further.

This structure will look like this:

```javascript
adapters
|---xhr
|---page1Adapter
|---page2Adapter
```

In the case of axios, you can use `axios.create` to create a base adapter, and either export this initialized instance, or create different functions for get, post, patch and delete to abstract it further. This would look like this:

```javascript
// adapters/xhr/index.tsx

import Axios from "axios";

function returnAxiosInstance() {
  return Axios.create(initializers);
}

export function get(url){
  const axios = returnAxiosInstance();
  return axios.get(url);
}

export function post(url, requestData){
  const axios = returnAxiosInstance();
  return axios.post(url, requestData);
}

... and so on ...
```

After you have your base file (or files) ready, create a separate adapter file for each page, or each set of functionalities, depending on how complex your app is. A well-named function makes it very easy to understand what each API call does and what it should accomplish.

```javascript
// adapters/page1Adapter/index.tsx

import { get, post } from "adapters/xhr";
import socket from "socketio";

// well-named functions
export function getData(){
  return get(someUrl);
}

export function setData(requestData){
  return post(someUrl, requestData);
}

... and so on ...
```

But how will these adapters be of any use? Let’s find out in the next section.

## 2\. Components

Although in this section we should talk about contexts, I want to talk about components first. This is to understand why context is required (and needed) in complex applications.

`Components` are the life-blood of your application. They will hold the UI for your application, and can sometimes hold the Business Logic and also any State which has to be maintained.

In case a component becomes too complex to express Business Logic with your UI, it is good to be able to split it into a separate bl.tsx file, with your root index.tsx importing all of the functions and handlers from it.

This structure would look like this:

```javascript
components
|---page1Components
        |--Component1
        |--Component2
|---page2Component
        |--Component1
               |---index.tsx
               |---bl.tsx
```

In this structure, each page gets its own folder inside of components, so that it’s easy to figure out which component affects what.

It’s also important to limit the scope of a component. Hence, a component should only use `adapters` for data-fetching, have a separate file for complex Business Logic, and only focus on the UI part.

```javascript
// components/page1Components/Component1/index.tsx

import businessLogic from "./bl.tsx";

export default function Component2() {
  
  const { state and functions } = businessLogic();

  return {
    // JSX
  }
}
```

While the BL file only imports data and returns it:

```javascript
// components/page1Components/Component1/bl.tsx

import React, {useState, useEffect} from "react";
import { adapters } from "adapters/path_to_adapter";

export default function Component1Bl(){
  const [state, setState] = useState(initialState);

  useEffect(() => {
    fetchDataFromAdapter().then(updateState);
  }, [])
}
```

However, there’s a problem which is common across all complex apps. State Management, and how to share state across distant components. For example, consider the following file structure:

```javascript
components
|---page1Components
        |--Component1
               |---ComponentA
|---page2Component
        |--ComponentB
```

If some state has to be shared across ComponentA and B in the above example, it will have to be passed through all the intermediate components, and also to any other components who want to interact with the state.

To solve this, their are several solutions which can be used like Redux, Easy-Peasy, and React Context, each of them having their own pros and cons. Generally, React Context should be “good enough” to solve this problem. We store all of the files related to context in `contexts`.

## 3\. Contexts

The `contexts` folder is a bare minimum folder only containing the state which has to be shared across these components. Each page can have several nested contexts, with each context only passing the data forward in a downward direction. But to avoid complexity, it is best to only have a single context file. This structure will look like this:

```javascript
contexts
|---page1Context
        |---index.tsx (Exports consumers, providers, ...)
        |---Context1.tsx (Contains part of the state)
        |---Context2.tsx (Contains part of the state)
|---page2Context
        |---index.tsx (Simple enough to also have state)
```

In the above case, since `page1` may be a bit more complex, we allow some nested context by passing the child context as a child to the parent. However, generally a single `index.tsx` file containing state and exporting relevant files should be enough.

I won’t go into the implementation part of React state management libraries since each of them are their own beasts and have their own upsides and downsides. So, I recommend going through the tutorial of whatever you decide to use to learn their best practises.

The context is allowed to import from `adapters` to fetch and react to external effects. In case of React Context, the providers are imported inside pages to share state across all components, and something like `useContext` is used inside these `components` to be able to utilize this data.

Moving on to the final major puzzle-piece, `pages`.

## 4\. Pages

I want to avoid being biased to a framework for this piece, but in general, having a specific folder for route-level components to be placed is a good practise.

Gatsby & NextJS enforce having all routes in a folder named `pages`. This is quite a readable way of defining route-level components, and mimicking this in your CRA-generated application would also result in better code readability.

A centralized location for routes also helps you utilize the “Go To File” functionality of most IDEs by jumping to a file by using (Cmd or Ctrl) + Click on an import.

This helps you move through the code quickly and with clarity of what belongs where. It also sets a clear hierarchy of differentiation between `pages` and `components`, where a page can import a component to display it and do nothing else, not even Business Logic.

However, it’s possible to import Context Providers inside of your page so the child components can consume it. Or, in the case of NextJS, write some server-side code which can pass data to your components using getServerSideProps or getStaticProps.

## 5\. Styles

Finally, we come to styles. Although my go-to way is to just embed styles inside of the UI by using a CSS-in-JS solution like Styled-Components, it’s sometimes helpful to have a global set of styles in a CSS file.

A plain old CSS file is more shareable across projects, and can also affect the CSS of components which styled-components can’t reach (for example, third-party components).

So, you can store all of these CSS files inside of the `styles` folder, and import or link to them freely from wherever you wish.

Those were my thoughts. Feel free to email me in case you want to discuss something or have any more inputs on how this can be improved!

For further updates or discussions, you can follow me on Twitter [here](https://twitter.com/thewritingdev).

My last article on freeCodeCamp was written on how you can get started with Deno by building a URL shortener, which [you can read here](https://www.freecodecamp.org/news/build-a-url-shortener-in-deno/).
