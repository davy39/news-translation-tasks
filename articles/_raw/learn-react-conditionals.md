---
title: How to Level Up Your React Conditionals
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-11T16:04:46.000Z'
originalURL: https://freecodecamp.org/news/learn-react-conditionals
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5-ways-to-level-up-your-react-conditionals-1.png
tags:
- name: Conditionals
  slug: conditionals
- name: React
  slug: react
seo_title: null
seo_desc: "Do you write conditionals correctly within your React applications? \n\
  Good conditionals are an essential part of any React application. We use conditionals\
  \ to show or hide elements or components in our applications. \nIn short – to be\
  \ an effective Reac..."
---

Do you write conditionals correctly within your React applications? 

Good conditionals are an essential part of any React application. We use conditionals to show or hide elements or components in our applications. 

In short – to be an effective React developer, you must know how to write good conditionals.

Let's go over all of the major patterns you need to know to write clean, concise conditionals, plus what anti-patterns you should avoid.

### Want Your Own Copy?‬ 📄

**[Download the cheatsheet in PDF format here](http://bit.ly/react-conditionals-2021)** (it takes 5 seconds).

Here are some quick wins from grabbing the downloadable version:

* Quick reference guide to review however and whenever
* Tons of copyable code snippets for easy reuse
* Read this massive guide wherever suits you best. On the train, at your desk, standing in line... anywhere.

There's a ton of great stuff to cover, so let's get started.

## 1. Use if-statements primarily. No need for else or else-if.

Let's start with the most basic type of conditional in React. If we have data, we want to display it. If not, we want to show nothing.

Simple! How would we write that?

Let's say we are fetching an array of posts data from an API. When it is fetching the data, `posts` has a value of `undefined`.

We can check for that value with a simple if-statement.

```js
export default function App() {
  const { posts } = usePosts(); // posts === undefined at first

  if (!posts) return null;

  return (
    <div>
      <PostList posts={posts} />
    </div>
  );
}
```

The reason this pattern works is that we are returning early. If it meets the condition (if `!posts` is has a boolean value of `true`), we display nothing in our component by returning `null`.

If statements also work when you have multiple conditions that you want to check for. 

For example, if you want to check for loading and error states before you display your data:

```js
export default function App() {
  const { isLoading, isError, posts } = usePosts();
   
  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>Error!</div>;

  return (
    <div>
      <PostList posts={posts} />
    </div>
  );
}
```

Notice that we can reuse the if-statement and do not have to write if-else or if-else-if, which cuts down on the code that we have to write and is still just as readable.

## 2. Use the ternary operator to write conditionals in your JSX

If-statements are great when we want to exit early and display nothing or a totally different component.

However, what if we don't want to write a conditional separate from our returned JSX, but directly within it?

In React, we must include expressions (something that resolves to a value), not statements within our JSX. 

This is why we must write conditionals in our JSX only with ternaries and not if-statements.

For example, if we wanted to display one nested component on a mobile-sized screen and another on a larger screen, a ternary would be a perfect choice:

```js
function App() {
  const isMobile = useWindowSize()

  return (
    <main>
      <Header />
      <Sidebar />
      {isMobile ? <MobileChat /> : <Chat />}
    </main>
  )
}
```

Most developers think this the only pattern they can leverage when it comes to using ternaries.

In fact, you don't have to clutter your component tree by including all of these ternaries directly in your returned JSX.

Since ternaries resolve to a value, remember that you can assign the result of a ternary to a variable, which you can then use where you like:

```js
function App() {
  const isMobile = useWindowSize();
    
  const ChatComponent = isMobile ? <MobileChat /> : <Chat />;

  return (
    <main>
      <Header />
      <Sidebar />
      {ChatComponent}
    </main>
  )
}
```

## 3. No else condition? Use the && (and) operator

In many cases, you will want to use a ternary in your JSX, but will realize that if that condition is not met, you don't want to display anything.

This ternary would look like the following: `condition ? <Component /> : null`.

If you don't have an else condition, use the && operator:

```js
export default function PostFeed() {
  const { posts, hasFinished } = usePosts()

  return (
    <>
      <PostList posts={posts} />
      {hasFinished && (
        <p>You have reached the end!</p>
      )}
    </>
  )
}
```

## 4. Switch statements for multiple conditions

What if we are in a situation where have many different conditions, more than just one or two?

We could certainly write multiple if-statements, but all of these if statements, as we've seen earlier, go above our returned JSX.

Too many if-statements can clutter our components. How do we make our code cleaner?

We can often extract multiple conditions to a separate component which contains a switch statement. 

For example, we have a Menu component that we can toggle and display different tabs. 

We have tabs that can display user, chat, and room data as you see below:

```js
export default function Menu() {
  const [menu, setMenu] = React.useState(1);

  function toggleMenu() {
    setMenu((m) => {
      if (m === 3) return 1;
      return m + 1;
    });
  }

  return (
    <>
      <MenuItem menu={menu} />
      <button onClick={toggleMenu}>Toggle Menu</button>
    </>
  );
}

function MenuItem({ menu }) {
  switch (menu) {
    case 1:
      return <Users />;
    case 2:
      return <Chats />;
    case 3:
      return <Rooms />;
    default:
      return null;
  }
}

```

Since we are using a dedicated MenuItem component with a switch statement, our parent Menu component is not cluttered by conditional logic and we can easily see what component will be displayed given the `menu` state.

## 5. Want conditionals as components? Try JSX Control Statements

It's greatly beneficial to be able to use plain JavaScript within our React components. But if you want even more declarative and straightforward conditionals, check out the React library JSX control statements. 

You can bring it into your React projects by running the following command:

```bash
npm install --save-dev babel-plugin-jsx-control-statements
```

Additionally, you can list it in your .babelrc file like so:

```json
{
  "plugins": ["jsx-control-statements"]
}
```

This is a Babel plugin that allows you to use React components directly within your JSX to write very easy to understand conditionals. 

The best way to understand the use of such a library is by taking a look at an example. Let's rewrite one of our previous examples with the help of JSX control statements:

```js
export default function App() {
  const { isLoading, isError, posts } = usePosts();

  return (
    <Choose>
      <When condition={isLoading}>
        <div>Loading...</div>
      </When>
      <When condition={isError}>
        <div>Error!</div>
      </When>
      <Otherwise>
        <PostList posts={posts} />
      </Otherwise>
    </Choose>
  );
}
```

You can see that there's no if or ternary statement in sight and we have a very readable component structure. 

Give JSX control statements a try in your next React project and see if a library like this is for you.

## **What's Next**

I hope this guide gave you some helpful patterns to write great React conditionals.

If you want a copy of this cheatsheet to keep for learning purposes, you can [download a complete PDF version of this cheatsheet here.](http://bit.ly/react-conditionals-2021)

Also check out these ultimate resources, made to take your React skills to the next level, including:

* [React for beginners: The complete guide](https://reactbootcamp.com/react-for-beginners-2021/)
* [How to fetch data in React from front to back](https://reactbootcamp.com/fetch-data-in-react/)
* [How to build fullstack apps in React with Node](https://reactbootcamp.com/react-app-node-backend/)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

