---
title: How to Use Recoil for State Management in Your React Projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-28T23:19:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-recoil-for-state-management-in-your-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/fcc-recoil-article.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: "By Abdullah Adeel\nIf you're a React developer, you've probably used a\
  \ library for managing state in your React applications. And you've likely heard\
  \ of Redux \"the state management\" library for React. \nFor a long time, Redux\
  \ was the only reliable and ..."
---

By Abdullah Adeel

If you're a React developer, you've probably used a library for managing state in your React applications. And you've likely heard of Redux "**the state management**" library for React. 

For a long time, Redux was the only reliable and most widely-adopted solution for state management in React applications. And Redux has proven its use cases in big applications. 

But the main problem that developers often face with Redux was the overall developer experience. In early versions of Redux, you had to manually set up your global data store and manually connect each component to consume it and update the global state. Basically, it used to take a lot of both time and effort for developers to set up and use Redux in their applications. 

Over time Redux has improved and now it too provides simple plugin solutions like **redux-toolkit**. But now there are even much simpler state management solutions available for React like [zustand](https://github.com/pmndrs/zustand), [recoil](https://github.com/facebookexperimental/Recoil), and [react-query](https://github.com/tannerlinsley/react-query) just to name a few.

In this article, we'll have a look at how to set up and use **Recoil** in your React applications by building a simple traditional todo app.

Before we start, I just want to mention that all the code for the todo app example is in [this sandbox](https://codesandbox.io/s/wwlgu). Feel free to reference it and tweak it.

%[https://codesandbox.io/embed/to-do-app-using-recoil-wwlgu?fontsize=14&hidenavigation=1&theme=dark]

## How to Install Recoil

Let's start by installing the library. If you are working on your local computer, you can install Recoil using `npm` or `yarn`.

```node
npm i recoil

// or

yarn add recoil
```

## How to Add Recoil's Root Component

The first thing that you need to do is wrap your entire application with the `RecoilRoot` component provided by `recoil`. 

Since Recoil uses a 100% hook-based approach, it's good to wrap your entire application with the root component provided by Recoil so that you can access your application state from any component. 

You can simply do this by importing and adding `RecoilRoot` in your index.js (entry file). This is how your index.js will look after you add it:

```js

import { StrictMode } from "react";
import ReactDOM from "react-dom";
import { RecoilRoot } from "recoil";
import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </StrictMode>,
  rootElement
);
```

## How to Create an Atom in Recoil

After this, we need to create an **atom.** An atom in Recoil is simply an isolated piece of memory that holds data. You can create as many atoms as you want. 

For example, say you are creating a social media application where users can bookmark a certain post. To store users' bookmarked posts, you can have a separate atom holding just the data for bookmarks. 

When some data changes in the atom – for example, the user bookmarks a post – it will re-render components subscribed to or using that atom. 

This is where the performance part of `recoil` comes into play. Recoil will make sure that only those components are being re-rendered that are subscribed to that specific atom.

Creating an atom is extremely easy. Create a `src/recoil/atom/todoAtom.js` file and add the following code:

```js
import { atom } from "recoil";

export const todoListAtom = atom({
  key: "todoListState",
  default: [],
});
```

## How to Create Your First Atom

You just need to import the `atom` function from `recoil`. This function takes an object as its argument. 

The first entry in that object is `key`. This is a unique string that will represent this specific atom. `default` is the initial state of this atom. And that's it. That's all you need to do to set it up. 

Make sure to export `todoListAtom` as we will be using it to reference this atom.

## How to Add Data to an Atom

Now let's create an input where the user can type in their todo. Create `components/TodoItemCreator.js`. 

In this component, we have an input where the user will type and we will see how simple it is to add a new todo in the atom. Later we will see how all the components which are using the same atom update to show the newly added todo. You can be as creative as you want while styling the input. 

Here I will only show how we can use the `useRecoilState` hook (it's provided by the `recoil` library to get the current state of the data inside the atom) and a handy function to update the state. 

If you have used `useState` in React, this will look quite identical to what you're used to in your local component state. The `useRecoilState` hook takes an atom as the argument.

```js
import { useState } from "react";
import { useRecoilState } from "recoil";
import { todoListAtom } from "../recoil/atoms/todoAtom";
import { generateUID } from "../utils/uuid";

export const TodoItemCreator = () => {
  const [inputValue, setInputValue] = useState("");
  const [_, setTodoList] = useRecoilState(todoListAtom);

  const onChange = (event) => {
    setInputValue(event.target.value);
  };

  const addTodoItem = () => {
    if (inputValue) {
      setTodoList((oldTodoList) => [
        ...oldTodoList,
        {
          id: generateUID(),
          text: inputValue,
          isComplete: false
        }
      ]);
      setInputValue("");
    }
  };

  return (
    <div className="todo-creator">
      <input type="text" value={inputValue} onChange={onChange} />
      <button className="add-btn" onClick={addTodoItem}>
        Add Task
      </button>
    </div>
  );
};


```

When the user types in the input and clicks the `Add Task` button, an `addTodoItem` function is called. This function simply calls the `setTodoList` function given by the hook. 

Since it is recommended to never update your global state directly, instead create a shallow copy of previous todos and add a new one. In the above code snippet, `generateUID` is just a utility function that will return a `uuidv4` unique id to return a random unique id that we will later use to update a simple todo from a list of `todos`.

## How to Consume Data from the Atom

Now let's create a component to display a todo in a list and enable the user to update, delete, or mark the todos as done. Create `src/components/TodoMain.js`.

```js
import { useRecoilValue } from "recoil";
import { TodoItemCreator } from "./TodoItemCreator";
import { TodoItem } from "./TodoItem";
import { todoListAtom } from "../recoil/atoms/todoAtom";
import "./todo.css";

export const TodoMain = () => {
  const todoList = useRecoilValue(todoListAtom);

  return (
    <div className="parent-container">
      <div>
        <TodoItemCreator />
        {todoList.length > 0 && (
          <div className="todos-list">
            {todoList.map((todoItem) => (
              <TodoItem key={todoItem.id} item={todoItem} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};


```

`useRecoilValue` is a hook provided by `recoil` that only returns the current state of date in the atom. We will use this hook to get all todos and `map` over them to display them on the screen. 

## How to Update Data in Atom

`TodoItem` is a component that uses the same `useRecoilState` hook and some helper functions to find and update the state of a specific todo.

```js
import { useRecoilState } from "recoil";
import { todoListAtom } from "../recoil/atoms/todoAtom";

export const TodoItem = ({ item }) => {
  const [todoList, setTodoList] = useRecoilState(todoListAtom);
  const index = todoList.findIndex((listItem) => listItem === item);

  const editItemText = (event) => {
    const newList = replatItemAtIndex(todoList, index, {
      ...item,
      text: event.target.value
    });

    setTodoList(newList);
  };

  const toggleItemCompletion = () => {
    const newList = replatItemAtIndex(todoList, index, {
      ...item,
      isComplete: !item.isComplete
    });

    setTodoList(newList);
  };

  const deleteItem = () => {
    const newList = removeItemAtIndex(todoList, index);

    setTodoList(newList);
  };

  return (
    <div className="container">
      <input
        className={item.isComplete.toString() === "true" && "done-task"}
        type="text"
        value={item.text}
        onChange={editItemText}
      />
      <input
        type="checkbox"
        checked={item.isComplete}
        onChange={toggleItemCompletion}
      />
      <button className="del-btn" onClick={deleteItem}>
        X
      </button>
    </div>
  );
};

const replatItemAtIndex = (arr, index, newValue) => {
  return [...arr.slice(0, index), newValue, ...arr.slice(index + 1)];
};

const removeItemAtIndex = (arr, index) => {
  return [...arr.slice(0, index), ...arr.slice(index + 1)];
};


```

And that's it. With two hooks and one function, you can handle all the state management requirements of your React applications. Recoil's power is its simple and beginner-friendly API and performance.

With that, thank you very much for taking time to read this article. If you find it interesting, join me over on [Twitter](https://twitter.com/abdadeel_) [abdadeel_](https://twitter.com/abdadeel_) where I share interesting web development content.

