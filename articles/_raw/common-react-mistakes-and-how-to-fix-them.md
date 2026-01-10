---
title: 4 Common React Mistakes You Might Be Making – And How to Fix Them
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-24T17:01:44.000Z'
originalURL: https://freecodecamp.org/news/common-react-mistakes-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/fix-react-code-cover-image.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Let''s go over the most common mistakes you might be making in your React
  code right now, plus how to fix them.

  If you want to create amazing React applications, it''s essential to avoid many
  common errors along the way.

  In this article, we''ll not only...'
---

Let's go over the most common mistakes you might be making in your React code right now, plus how to fix them.

If you want to create amazing React applications, it's essential to avoid many common errors along the way.

In this article, we'll not only cover how to fix your mistakes quickly, but also give you some awesome design patterns to make your code better and more reliable going forward.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Blue-and-Yellow-Photo-Fun-Job-Post--Vacancy--Announcement-Twitter-Post-2-2.gif)

## 1. Don't pass state variables to setState in React

In the code below, we have a todo application that displays an array of todos (in `TodoList`). 

We can add new todos in the `AddTodo` component, which updates the `todos` array in App.

What's the problem with the props that we have passed to `AddTodo`?

```js
export default function App() {
  const [todos, setTodos] = React.useState([]);

  return (
    <div>
      <h1>Todo List</h1>
      <TodoList todos={todos} />
      <AddTodo setTodos={setTodos} todos={todos} />
    </div>
  );
}

function AddTodo({ setTodos, todos }) {
  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
    const newTodos = todos.concat(todo);
    setTodos(newTodos);
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Add todo" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

We are adding the new todo to the `todos` array and then setting state as we should. This will update the displayed todos in the `TodoList` component.

However, since the new state is based off of the previous state, we do not need to pass down the todos array.

Instead, we can access the previous todos state by writing a function within the setState function. Whatever we return from this function will be set as the new state.

In other words, we only need to pass down the `setTodos` function to properly update state:

```js
export default function App() {
  const [todos, setTodos] = React.useState([]);

  return (
    <div>
      <h1>Todo List</h1>
      <TodoList todos={todos} />
      <AddTodo setTodos={setTodos} />
    </div>
  );
}

function AddTodo({ setTodos }) {
  function handleAddTodo(event) {
    event.preventDefault();
    const text = event.target.elements.addTodo.value;
    const todo = {
      id: 4,
      text,
      done: false
    };
    setTodos(prevTodos => prevTodos.concat(todo));
  }

  return (
    <form onSubmit={handleAddTodo}>
      <input name="addTodo" placeholder="Add todo" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

## 2. Make your React components single responsibility

In the application below, we're fetching a number of the users from an API within our app component, putting that user data in a state, and then displaying it within our user interface. 

What is the problem with the `App` component?

```js
export default function App() {
  const [users, setUsers] = React.useState([]);

  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
      });
  }, []);

  return (
    <>
      <h1>Users</h1>
      {users.map((user) => (
        <div key={user.id}>
          <div>{user.name}</div>
        </div>
      ))}
    </>
  );
}
```

In our component, we're doing multiple things.

We are not only doing remote data fetching from a server, but we are also managing state as well as displaying that state with JSX.

We are making our component do multiple things. Instead, your components should do only one thing and do that thing well. 

This is one key design principle from the acronym SOLID, which lays out five rules for writing more reliable software. 

The S in SOLID stands for the "single-responsibility principle", an essential one to use when writing React components.

We can divide our `App` component into separate components and hooks that each have their own responsibility. First, we will be extracting the remote data fetching to a custom React hook. 

This hook, which we'll call useUserData, will take care of fetching the data and putting it in local state.

```js
function useUserData() {
  const [users, setUsers] = React.useState([]);

  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((json) => {
        setUsers(json);
      });
  }, []);

  return users;
}
```

After that, we will call the hook within `App` to access our `users` array.

However, instead of displaying user data directly within our return statement in `App`, we will create a separate `User` component which will contain all of the JSX necessary to display each element in that array, plus any related styles (if we have any).

```js
function User({ user }) {
  const styles = {
    container: {
      margin: '0 auto',
      textAlign: 'center' 
    }
  };  
    
  return (
    <div style={styles.container}>
      <div>{user.name}</div>
    </div>
  );
}

export default function App() {
  const users = useUserData();

  return (
    <>
      <h1>Users</h1>
      {users.map((user) => (
        <User key={user.id} user={user} />
      ))}
    </>
  );
}
```

After this refactoring, our components now have a clear, individual task to perform, which makes our app much easier to understand and extend.

## 3. Make your side effects single responsibility

In our `App` component below, we are fetching both user and post data.

When the location – the URL – of our app changes, we fetch both the user and post data.

```js
export default function App() {
  const location = useLocation();

  function getAuthUser() {
    // fetches authenticated user
  }
    
  function getPostData() {
    // fetches post data
  }

  React.useEffect(() => {
    getAuthUser();
    getPostData();
  }, [location.pathname]);

  return (
    <main>
      <Navbar />
      <Post />
    </main>
  );
}
```

We display a new post if the URL changes, but do we need to fetch that every time the location changes? 

We don't.

In much of your React code, you may be tempted to stuff all of your side effects within a single use effect function. But doing so violates the single responsibility principle we just mentioned. 

This can result in problems such as performing side effects when we don't need to. Remember to keep your side effects to a single responsibility as well. 

In order to fix our code, all we need to do is call `getAuthUser` within a separate use effect hook. This ensures it is not called whenever the location pathname changes, but only once when our app component mounts.

```js
export default function App() {
  const location = useLocation();

  React.useEffect(() => {
    getAuthUser();
  }, []);

  React.useEffect(() => {
    getPostData();
  }, [location.pathname]);

  return (
    <main>
      <Navbar />
      <Post />
    </main>
  );
}
```

## 4. Use ternaries instead of `&&` in JSX

Let's say we are displaying a list of posts in a dedicated component, `PostList`.

It makes sense to check whether we have posts before we iterate over them. 

Since our `posts` list is an array, we can use the `.length` property to check and see if it is a truthy value (greater than 0). If so, we can map over that array with our JSX. 

We can express all this with the and `&&` operator:

```js
export default function PostList({ posts }) {
  return (
    <div>
      <ul>
        {posts.length &&
          posts.map((post) => <PostItem key={post.id} post={post} />)}
      </ul>
    </div>
  );
}

```

However, you might be surprised with what we see, if we were to execute such code. If our array is empty, we don't see nothing – we see the number 0! 

What? Why is this?! 

This is a JavaScript-related problem, because the length of our array is 0. Because 0 is a falsy value, the `&&` operator doesn't look at the right hand side of the expression. It just returns the left hand side – 0. 

What is the best way to fix this and to prevent such errors in the future? 

In many cases we shouldn't use the and operator, but instead use a ternary to explicitly define what will be displayed in the event that condition is not met. 

If we were to write the following code with a ternary, we would include the value `null` in the else condition to ensure that nothing is displayed.

```js
export default function PostList({ posts }) {
  return (
    <div>
      <ul>
        {posts.length
          ? posts.map((post) => <PostItem key={post.id} post={post} />)
          : null}
      </ul>
    </div>
  );
}
```

By using ternaries instead of `&&`, you can avoid many annoying bugs like this one.

Thanks for reading!

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

