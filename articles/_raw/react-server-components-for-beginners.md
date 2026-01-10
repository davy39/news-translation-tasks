---
title: How to Use React Server Components – A Beginner's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-19T20:31:21.000Z'
originalURL: https://freecodecamp.org/news/react-server-components-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-panumas-nikhomkhai-1148820--2-.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Adwaith KS

  React Server Components have been generating significant buzz and excitement lately.
  They''ve recently been adopted as the default option in Next.js 13, so now more
  and more developers are using them.

  React Server Components seamlessly b...'
---

By Adwaith KS

React Server Components have been generating significant buzz and excitement lately. They've recently been adopted as the default option in Next.js 13, so now more and more developers are using them.

React Server Components seamlessly blend server-side rendering with the interactivity of client-side JavaScript. And in this tutorial, you'll learn all about what React Server Components are, the problems they solve, and the powerful capabilities they provide.

## **Why Server Components?**

Let's start with an example:

```jsx
const App = () => {
    return (
        <Wrapper>
            <ComponentA />
            <ComponentB />
        </Wrapper>
    )
}
```

We have two components **ComponentA** and **ComponentB** that are passed in as child props to a **Wrapper** component. Each component's body looks something like this:

```jsx
const Wrapper = ({children}) => {
  
  const [wrapperData, setWrapperData] = useState({});
  
  useEffect(() => {
    // API call to get data for Wrapper component to function
    getWrapperData().then(res => {
      setWrapperData(res.data);
    });
  }, []);
  
  // Only after API response is received, we start rendering
  // ComponentA and ComponentB (children props)
  return (
  	<>
      <h1>{wrapperData.name}</h1>
      <>
        {wrapperData.name && children}
      </>
    </>
  )
}

/*-------------------------------------------------- */

const ComponentA = () => {
  const [componentAData, setComponentAData] = useState({});
  
  useEffect(() => {
    getComponentAData().then(res => {
      setComponentAData(res.data);
    });
  }, []);
  
  return (
  	<>
      <h1>{componentAData.name}</h1>
    </>
  )
}

/*-------------------------------------------------- */

const ComponentB = () => {
  const [componentBData, setComponentBData] = useState({});
  
  useEffect(() => {
    getComponentBData().then(res => {
      setComponentBData(res.data);
    });
  }, []);
  
  return (
  	<>
      <h1>{componentBData.name}</h1>
    </>
  )
}
```

Each component is responsible for fetching its own data (as you can see in the above code). So, no component is dealing with data that is not needed for its own operation. Perfect, right? Well, not yet.

Assume the time it takes to get the response for API calls fired from each component is as follows:

* `**<Wrapper />** takes 1 sec to get the response`
* `**<ComponentB />** takes 2 sec to get the response`
* `**<ComponentA />** takes 3 sec to get the response`

Do you see a problem here?

1. **Wrapper** is visible to the user after 1 sec.
2. Then **ComponentB** appears after 2 seconds.
3. After 3 seconds, **ComponentA** appears. But ComponentA enters the view by pushing **ComponentB** down. As if ComponentA just popped out of nowhere. This is not a great user experience.

Another problem is, child components (ComponentA and ComponentB) are not even rendered until the **Wrapper** component get the response from the API call it made (refer to image 2), which results in a waterfall. Sequential data fetching always introduces waterfalls.

The term "waterfall" typically refers to the sequential execution of multiple fetch requests. This means that the subsequent fetch requests are initiated only after the previous fetch request has been resolved or completed.

In our example, only after getting the response to the API call in the Wrapper component are the other two components rendered.

How can we solve this problem? Well, we can do a single fetch to get all the data in the **App** component, and then pass the necessary data to each component. Something like this:

```jsx
const App = () => {
    
    const data = fetchAllStuffs();
    
    return (
        <Wrapper data={data.wrapperData}>
            <ComponentA data={data.componentAData} />
            <ComponentB data={data.componentBData} />
        </Wrapper>
    )
}
```

There is nothing wrong with this approach. But, the API response is very coupled to our components.

For example, if we remove **ComponentA** in the future, we also want to remove **componentAData** from the API response, since we dont wan't to deal with data not used by the component. After all, if there's no ComponentA, then there's no need of ComponentAData.

## **The Solution is Server Components**

The above problem is what server components primarily address. To recap the issue: Components make API calls to the server from the client, and we wait for the response to arrive back in order to render other components. When we have sequential data fetching going on in the client, this is going to create waterfalls (as mentioned earlier).

How about we move these components to the server? Yeah, you heard me right!

Just assume the components are on the server. Does data fetching take the same time as it would when the components were on the client side? No, it doesn't.

Fetching data is way faster when components are on the server. Well, do you really need to fetch now? Not really! Since now your components are rendered on the server, your components have access to the server infrastructure. This means that you can query the database from your components as well.

Too much information? Let's break it down a bit.

For the sake of simplicity, let's put it this way. Move your data fetching to the server. Any kind of data fetching done with the help of the server is way faster.

Why? Because, you are not fetching data all the way from the client now, therefore low latency. You are fetching data from the server itself now.

Well, this is great – but there's a catch. You are rendering components on the server. Will you be able to use hooks (for example, useState, useEffect, and others), Web APIs (like localstorage), or event handlers (like onClick) like you would use in a normal React Component? No, you won't.

This is because Server Components are rendered on the server. So they're well-suited for situations where real-time updates or user interactions are not essential.

Here's a glimpse of how a Server Component looks:

```jsx
// Note.js - Server Component

import NoteEditor from 'NoteEditor';

async function Note(props) {
  const { note } = props;
  
  return (
    <div>
      <h1>{note.title}</h1>
      <section>{note.body}</section>
    </div>
  );
}
```

Looks like a regular React Component, right? Yes. The difference between a regular React component (also called Client Component from now on) and a Server Component is in its rendering environment and the abilities they both have. More on this down below.

## **Do's and Dont's of Server Components**

Following is a list of things that you can do and cannot do with Server Components. Even though Server Components might look fancy, that doesn't mean we can use them everywhere.

### **Things You Can Do**

* Use `async/await` with server only data sources such as databases, internal services, filesystems etc.
* Render other server components, native elements like div, span, and so on or Client Components (Normal React components).

### **Things You Cannot Do**

* Cannot use hooks provided by React like useState, useReducer, useEffect and so on, as server components are rendered on the server.
* Cannot use browser API's like Local Storage and so on (You can polyfill them on server, though).
* Cannot use any utility functions that depend on browser only API's (for example: Local Storage) or custom hooks that depend on state or effects.

## **Server Components vs Client Components**

Are you wondering what a Client Component is now? Well, they're the React Components that you've been writing all these years. Yeah, the regular way of writing React.

As the name suggests, they are rendered on the client side, that is the browser. Just a note that all the React code that you were writing before Server Components existed was rendered on the client side (browser). So to differentiate from Server Components that are rendered on the server, from now on we'll call regular React components (where you use states, effects, browser-only API's) "Client Components".

First, let's look at an example of a Server Component:

```jsx
// Note.js - Server Component

import db from 'db'; 
// (A1) We import from NoteEditor.js - a Client Component.
import NoteEditor from 'NoteEditor';

async function Note(props) {
  const {id, isEditing} = props;
  // (B) Can directly access server data sources during render, e.g. databases
  const note = await db.posts.get(id);
  
  return (
    <div>
      <h1>{note.title}</h1>
      <section>{note.body}</section>
      {/* (A2) Dynamically render the editor only if necessary */}
      {isEditing 
        ? <NoteEditor note={note} />
        : null
      }
    </div>
  );
}
```

Wait, a database call inside a React Component? Yeah, you are seeing a Server Component named **Note**. This is just a React component that is rendered on the server. i.e Server component is just a react component, where you have some special abilities like the one that you see in the above example (access database directly).

Well, the **Note** component is a Server component. What about **NoteEditor** component inside the Note component? The following is the body of the NoteEditor component:

```jsx
// NoteEditor.js - Client Component

'use client';

import { useState } from 'react';

export default function NoteEditor(props) {
  const note = props.note;
  const [title, setTitle] = useState(note.title);
  const [body, setBody] = useState(note.body);
  const updateTitle = event => {
    setTitle(event.target.value);
  };
  const updateBody = event => {
    setBody(event.target.value);
  };
  const submit = () => {
    // ...save note...
  };
  return (
    <form action="..." method="..." onSubmit={submit}>
      <input name="title" onChange={updateTitle} value={title} />
      <textarea name="body" onChange={updateBody}>{body}</textarea>
    </form>
  );
}
```

If you carefully look at the above code, we are using `'use client'` to declare this component as a client component. That is, **NoteEditor** is a Client Component. What is a client component again? Just a regular React component that you have been writing all these years, and they are rendered on the client, that is the browser.

Any component which has `'use client'` at the top of the file is identified as a Client Component. If we don't specify that at the top of the file, the component in the file is considered a Server Component.

So do you think you can call the database directly inside Client Components? No! You don't have access to the server environment, since Client Components are not rendered on the server, but on the browser.

One possible question you might have is whether you can use Client components inside Server components and vice versa.

**Well, Client Components cannot import Server Components – but you can do the opposite.** Importing a Client Component or a Server Component inside a Server Component is possible. And, Server Component may pass another Server Component as a child to a Client Component, For example:

```jsx
const ServerComponentA = () => {
    return (
        <ClientComponent>
            <ServerComponentB />
        </ClientComponent>
    )
}
```

In the above example, we are passing a Server Component named ServerComponentB as a child to ClientComponent.

Again, we cannot import Server Components inside Client Components, but it's totally fine to pass a Server Component as a child to a Client Component.

Let's summarize:

* You can import Client Components inside Server Components.
* You cannot import Server Components inside Client Components.
* You can pass a Server Component as a child prop to a Client Component inside Server Component.

## **The Real Power of Server Components**

Now we'll look at some of the benefits of using Server Components. Server Components are not just about rendering static data.

### Zero Bundle Size Components

Using libraries is helpful to developers, but it increases the bundle size and can hurt application performance.

Many parts of an application aren’t interactive and don’t need full data consistency. For example, a “details” page often shows information about a product, user, or other entity and doesn't need to update in response to user interactions.

Server Components allow developers to render static content on the server. You can freely use third-party packages in Server Components while incurring **zero impact on bundle size**.

```jsx
// NOTE: *before* Server Components

import marked from 'marked'; // 35.9K (11.2K gzipped)
import sanitizeHtml from 'sanitize-html'; // 206K (63.3K gzipped)

function NoteWithMarkdown({text}) {
  const html = sanitizeHtml(marked(text));
  return (/* render */);
}
```

If we render the above example as a Server Component, we can use the _exact same code_ for our feature but avoid sending it to the client – a code savings of over 240K (uncompressed).

```jsx
// Server Component === zero bundle size

import marked from 'marked'; // zero bundle size
import sanitizeHtml from 'sanitize-html'; // zero bundle size

function NoteWithMarkdown({text}) {
  // same as before
}
```

In short, if you are using any third party library inside Server Component, the library is not included in the client side bundle. This reduces the JavaScript bundle size.

But, if you are using the library inside any of the Client Components, then as you might have guessed, the library will be included in the client bundle and will be downloaded by the browser for parsing and execution.

### Complete access to the backend

As discussed earlier, Server Components can take advantage of direct backend access to use databases, internal (micro) services, and other backend-only data sources.

```jsx
import db from 'db';

async function Note({id}) {
  const note = await db.notes.get(id);
  return <NoteWithMarkdown note={note} />;
}
```

In the above code snippet, We are passing **note** to **NoteWithMarkdown** component. From where are we getting this **note**? From the database. 

If you check out the code carefully, we didn't make any fetch API calls to get the **note**. Instead we just executed the DB query directly inside the **Note** component (usually we make DB queries in the server side code). This is possible because this is a server component, and it is rendered on the server.

Let's look at one more example, where you can access the file system of your server from a Server Component:

```jsx
import fs from 'fs';

async function Note({id}) {
  const note = JSON.parse(await fs.readFile(`${id}.json`));
  return <NoteWithMarkdown note={note} />;
}
```

As you can see in the above code, we are using the `fs` module (short for file system) to read files that is present on the server.

### Automatic Code Splitting

Server Components treat all imports of Client Components as potential code-split points.

```jsx
// PhotoRenderer.js - Server Component

// one of these will start loading *once rendered and streamed to the client*:
import OldPhotoRenderer from './OldPhotoRenderer.js';
import NewPhotoRenderer from './NewPhotoRenderer.js';

function Photo(props) {
  // Switch on feature flags, logged in/out, type of content, etc:
  if (FeatureFlags.useNewPhotoRenderer) {
    return <NewPhotoRenderer {...props} />;
  } else {
    return <OldPhotoRenderer {...props} />;
  }
}
```

In the above example, we have two components **NewPhotoRenderer** and **OldPhotoRenderer** (and both are Client Components) that are rendered conditionally.

Let's say that the `if (FeatureFlags.useNewPhotoRenderer)` evaluates to True, and NewPhotoRenderer is the component that the user is going to see. Only that component is sent to the client (or browser). OldPhotoRenderer will be loaded lazily (meaning, it won't be sent to the client immediately). So, only the JavaScript related to the component that is visible to the user is needed.

### No more waterfalls

As discussed earlier, sequential data fetching introduces waterfalls. We wanted to find a way to avoid sequential round trip delay from client to server. (That is, we have to wait until one request finishes, and the request can take some time to fulfill since it has to travel from client to the server.)

```jsx
// Note.js - Server Component

async function Note(props) {
  // NOTE: loads *during* render, w low-latency data access on the server
  const note = await db.notes.get(props.id);
  if (note == null) {
    // handle missing note
  }
  return (/* render note here... */);
}
```

Server Components allow applications to achieve this goal by moving sequential round trips to the server. ( i.e no more fetch calls from client to server )

The problem isn’t really the round trips, it’s that they are from client to server. By moving this logic to the server, we reduce the request latency and improve performance. Again, move your data fetching to the server (if possible).

## **Wrapping Up**

And that's a wrap! Currently Next.js 13 is the way to go if you want to use Server Components. Making server components the default option is arguably the boldest change made in Next.js 13.

Have fun playing around with Server Components in Next.js 13. Happy Hacking!

