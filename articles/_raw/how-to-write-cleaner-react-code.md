---
title: How to Write Cleaner React Code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-05T20:29:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-cleaner-react-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/7-ways-to-write-clean-react-code.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: null
seo_desc: "As React developers, we all want to write cleaner code that is simpler\
  \ and easier to read. \nIn this guide, I've put together seven of the top ways that\
  \ you can start writing cleaner React code today to make building React projects\
  \ and reviewing your ..."
---

As React developers, we all want to write cleaner code that is simpler and easier to read. 

In this guide, I've put together seven of the top ways that you can start writing cleaner React code today to make building React projects and reviewing your code much easier.

In general, learning how to write cleaner React code will make you a more valuable and overall happier React developer, so let's jump right in!

## 1. Make use of JSX shorthands

How do you pass a value of true to a given prop? 

In the example below, we're using the prop `showTitle` to display the title of our app within a Navbar component. 

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar showTitle={true} />
    </main>
  );
}

function Navbar({ showTitle }) {
  return (
    <div>
      {showTitle && <h1>My Special App</h1>}
    </div>
  )
}
```

Do we need to explicitly set `showTitle` to the Boolean `true`? We don't! A quick shorthand to remember is that any prop provided on a component has a default value of true. 

So if we add the prop `showTitle` on Navbar, our title element will be shown:

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar showTitle />
    </main>
  );
}

function Navbar({ showTitle }) {
  return (
    <div>
      {showTitle && <h1>My Special App</h1>} // title shown!
    </div>
  )
}
```

Another useful shorthand to remember involves passing string props. When you're passing a prop value that's a string, you don't need to wrap it in curly braces. 

If we are setting the title of our Navbar, with the `title` prop, we can just include its value in double quotes:

```js
// src/App.js

export default function App() {
  return (
    <main>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  )
}
```

## 2. Move unrelated code into a separate component

Arguably the easiest and most important way to write cleaner React code is to get good at abstracting our code into separate React components. 

Let's look at the example below. What is our code doing? 

Our app is displaying a Navbar component. We are iterating over an array of posts with `.map()` and displaying their title on the page. 

```js
// src/App.js

export default function App() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <main>
      <Navbar title="My Special App" />
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            {post.title}
          </li>
        ))}
      </ul>
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}

```

How can we make this cleaner? 

Why don't we abstract the code that we're looping over – our posts – and display them in a separate component, which we'll call FeaturedPosts. 

Let's do that and take a look at the result:

```js
// src/App.js

export default function App() {
 return (
    <main>
      <Navbar title="My Special App" />
      <FeaturedPosts />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}

function FeaturedPosts() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

```

As you can see, we can now just look at our App component. By reading the names of the components within it, Navbar and FeaturedPosts, we see exactly what our app is displaying. 

## 3. Create separate files for each component

Going off of our previous example, we are including all of our components within a single file, the app.js file. 

Similar to how we abstract code into separate components to make our app more readable, to make our application files more readable, we can put each component that we have into a separate file.

This, again, helps us separate concerns in our application. This means that each file is responsible for just one component and there's no confusion where a component comes from if we want to reuse it across our app:

```js
// src/App.js
import Navbar from './components/Navbar.js';
import FeaturedPosts from './components/FeaturedPosts.js';

export default function App() {
  return (
    <main>
      <Navbar title="My Special App" />
      <FeaturedPosts />
    </main>
  );
}
```

```js
// src/components/Navbar.js

export default function Navbar({ title }) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}
```

```js
// src/components/FeaturedPosts.js

export default function FeaturedPosts() {
  const posts = [
    {
      id: 1,
      title: "How to Build YouTube with React"
    },
    {
      id: 2,
      title: "How to Write Your First React Hook"
    }
  ];

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

```

Additionally, by including each individual component within its own file, we avoid one file becoming too bloated. We could easily see our app.js file becoming very large if we wanted to add all of our components into that file. 

## 4. Move shared functionality into React hooks

Taking a look at our FeaturedPosts component, let's say instead of displaying static posts data, we want to fetch our post data from an API. 

We might do so with the fetch API. You can see the result below for that: 

```js
// src/components/FeaturedPosts.js

import React from 'react';

export default function FeaturedPosts() {
  const [posts, setPosts] = React.useState([]);  	
    
  React.useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

However, what if we wanted to perform this request for data across multiple components? 

Let's say in addition to a FeaturedPosts component we wanted to create a component called just Posts with the same data. We would have to copy the logic that we used to fetch our data and paste it within that component as well. 

To avoid having to do that, why don't we just use a new React hook which we could call `useFetchPosts`:

```js
// src/hooks/useFetchPosts.js

import React from 'react';

export default function useFetchPosts() {
  const [posts, setPosts] = React.useState([]);  	
    
  React.useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return posts;
}
```

Once we've created this hook in a dedicated 'hooks' folder we can reuse it in whichever components we like, including our FeaturedPosts component:

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## 5. Remove as much JavaScript from your JSX as possible

Another very helpful, but often neglected way to clean up our components is to remove as much JavaScript from our JSX as possible. 

Let's take a look at the example below:

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li onClick={event => {
          console.log(event.target, 'clicked!');
        }} key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

We're trying to handle a click event on one of our posts. You can see that our JSX becomes much harder to read. Given that our function is included as an inline function, it obscures the purpose of this component, as well as its related functions. 

What can we do to fix this? We can extract the inline function, connected to the `onClick` into a separate handler, which we can give a an appropriate name like `handlePostClick`.

Once we do, our JSX becomes readable once again:

```js
// src/components/FeaturedPosts.js

import useFetchPosts from '../hooks/useFetchPosts.js';

export default function FeaturedPosts() {
  const posts = useFetchPosts()
  
  function handlePostClick(event) {
    console.log(event.target, 'clicked!');   
  }

  return (
    <ul>
      {posts.map((post) => (
        <li onClick={handlePostClick} key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## 6. Format inline styles for less bloated code

A common pattern for React developers is to write inline styles in their JSX. But once again, this makes our code harder to read and harder to write additional JSX:

```js
// src/App.js

export default function App() {
  return (
    <main style={{ textAlign: 'center' }}>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  return (
    <div style={{ marginTop: '20px' }}>
      <h1 style={{ fontWeight: 'bold' }}>{title}</h1>
    </div>
  )
}
```

We want to apply this concept of separation of concerns to our JSX styles by moving our inline styles into a CSS stylesheet, which we can import into whatever component we like. 

An alternative way to rewrite your inline styles is by organizing them into objects. You can see what such a pattern would look like below:

```js
// src/App.js

export default function App() {
  const styles = {
    main: { textAlign: "center" }
  };

  return (
    <main style={styles.main}>
      <Navbar title="My Special App" />
    </main>
  );
}

function Navbar({ title }) {
  const styles = {
    div: { marginTop: "20px" },
    h1: { fontWeight: "bold" }
  };

  return (
    <div style={styles.div}>
      <h1 style={styles.h1}>{title}</h1>
    </div>
  );
}
```

## 7. Reduce prop drilling with React context

Another essential pattern to employ for your React projects (especially if you have common properties that you want to reuse across your components, and you find yourself writing lots of duplicate props) is to use React Context. 

For example, if we wanted to share user data across multiple components, instead of multiple repeat props (a pattern called props drilling), we could use the context feature that's built into the React library. 

In our case, if we wanted to reuse user data across our Navbar and FeaturedPosts components, all we would need to do is wrap our entire app in a provider component. 

Next, we can pass the user data down on the value prop and consume that context in our individual components with the help of the `useContext` hook:

```js
// src/App.js

import React from "react";

const UserContext = React.createContext();

export default function App() {
  const user = { name: "Reed" };

  return (
    <UserContext.Provider value={user}>
      <main>
        <Navbar title="My Special App" />
        <FeaturedPosts />
      </main>
    </UserContext.Provider>
  );
}

// src/components/Navbar.js

function Navbar({ title }) {
  const user = React.useContext(UserContext);

  return (
    <div>
      <h1>{title}</h1>
      {user && <a href="/logout">Logout</a>}
    </div>
  );
}

// src/components/FeaturedPosts.js

function FeaturedPosts() {
  const posts = useFetchPosts();
  const user = React.useContext(UserContext);

  if (user) return null;

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## Conclusion

I hope you find this guide useful when you're trying to improve your own React code to make it cleaner, easier to read, and ultimately more enjoyable to create your React projects.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

