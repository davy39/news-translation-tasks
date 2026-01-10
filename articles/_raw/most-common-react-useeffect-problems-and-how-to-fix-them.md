---
title: React.useEffect Hook – Common Problems and How to Fix Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-14T22:07:02.000Z'
originalURL: https://freecodecamp.org/news/most-common-react-useeffect-problems-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/react-1.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'By Iva Kop

  React hooks have been around for a while now. Most developers have gotten pretty
  comfortable with how they work and their common use cases. But there is one useEffect
  gotcha that a lot of us keep falling for.

  The use case

  Let''s start with ...'
---

By Iva Kop

React hooks have been around for a while now. Most developers have gotten pretty comfortable with how they work and their common use cases. But there is one `useEffect` gotcha that a lot of us keep falling for.

# The use case

Let's start with a simple scenario. We are building a React app and we want to display the user name of the current user in one of our components. But first, we need to fetch the user name from an API. 

Because we know we will need to use the user data in other places of our app as well, we also want to abstract the data-fetching logic in a custom React hook.

Essentially, we want our React component to look something like this:

```
const Component = () => {
  // useUser custom hook
  
  return <div>{user.name}</div>;
};

```

Looks simple enough!

# The useUser React hook

The second step would be to create our `useUser` custom hook.

```
const useUser = (user) => {
  const [userData, setUserData] = useState();
  useEffect(() => {
    if (user) {
      fetch("users.json").then((response) =>
        response.json().then((users) => {
          return setUserData(users.find((item) => item.id === user.id));
        })
      );
    }
  }, []);

  return userData;
};

```

Let's break it down. We are checking if the hook is receiving a user object. After that, we are fetching a list of our users from a file called `users.json` and filtering it in order to find the user with the id that we need. 

Then, once we have the necessary data, we are saving it the `userData` state of our hook. In the end are returning the `userData`.

_**Note**: This is a contrived example for illustrative purpose only! Data-fetching in the real world is much more complicated. If you are interested in the topic, [check out my article](https://blog.whereisthemouse.com/graphql-requests-made-easy-with-react-query-and-typescript) on how to create a great data-fetching setup with ReactQuery, Typescript and GraphQL._

Let's plug the hook in our React component and see what happens.

```
const Component = () => {
  const user = useUser({ id: 1 });
  return <div>{user?.name}</div>;
};

```

Nice! Everything looks and works as expected. But wait... what is this?

# ESLint exhaustive-deps rule

We have an ESLint warning in our hook:

```
React Hook useEffect has a missing dependency: 'user'. Either include it or remove the dependency array. (react-hooks/exhaustive-deps)

```

Hmm, our `useEffect` seems to have a missing dependency. Oh, well! Let's add it. What's the worst that can happen? 😂

```
const useUser = (user) => {
  const [userData, setUserData] = useState();
  useEffect(() => {
    if (user) {
      fetch("users.json").then((response) =>
        response.json().then((users) => {
          return setUserData(users.find((item) => item.id === user.id));
        })
      );
    }
  }, [user]);

  return userData;
};

```

Uh-oh! It looks like our `Component` won't stop re-rendering now. What is going on here?!

Let's explain.

# The infinite re-renders problem

The reason our component is re-rendering is because our `useEffect` dependency is constantly changing. But why? We are always passing the same object to our hook!

While it is true that we are passing an object with the same key and value, it is not the same object exactly. We are actually creating a new object every time we re-render our `Component`. Then we pass the new object as an argument to our `useUser` hook. 

Inside, `useEffect` compares the two objects, and since they have a different reference, it once again fetches the users and sets the new user object to the state. The state updates then triggers a re-render in the component. And on, and on, and on...

So what can we do?

# How to fix it

Now that we understand the problem, we can start searching for a solution.

The first and probably most obvious option is to remove the dependency from the `useEffect` dependency array, ignore the ESLint rule, and move on with our lives. 

But this is the wrong approach. It can (and probably will) lead to bugs and unexpected behaviour in our app. If you want to know more about how `useEffect` works, I highly recommend Dan Abramov's [complete guide](https://overreacted.io/a-complete-guide-to-useeffect/).

So what's next?

In our case, the easiest solution is to take the `{ id: 1 }` object out of the component. This will give the object a stable reference and solve our problem.

```
const userObject = { id: 1 };

const Component = () => {
  const user = useUser(userObject);
  return <div>{user?.name}</div>;
};

export default Component;

```

But this is not always possible. Imagine that the user id was somehow dependent on the component props or state. 

It could be that we are using URL parameters to access it, for example. If this is the case, we have a handy `useMemo` hook at our disposal that will memoize the object and once again ensure a stable reference.

```
const Component = () => {
  const { userId } = useParams();
  
  const userObject = useMemo(() => {
    return { id: userId };
  }, [userId]); // Don't forget the dependencies here either!

  const user = useUser(userObject);
  return <div>{user?.name}</div>;
};

export default Component;

```

Finally, instead of passing an object variable to our `useUser` hook, it is possible to pass only the user id itself, which is a primitive value. This will prevent referential equality issues in the `useEffect` hook.

```
const useUser = (userId) => {
  const [userData, setUserData] = useState();

  useEffect(() => {
    fetch("users.json").then((response) =>
      response.json().then((users) => {
        return setUserData(users.find((item) => item.id === userId));
      })
    );
  }, [userId]);

  return userData;
};

const Component = () => {
  const user = useUser(1);

  return <div>{user?.name}</div>;
};

```

Problem solved! 

And we didn't even have to break any ESLint rules along the way...

_**Note:** If the argument we were passing to the custom hook was a function, rather than an object, we would use very similar techniques to avoid infinite re-renders. One notable difference is that we would have to replace `useMemo` with `useCallback` in the example above._

Thank you for reading!

Curious about the code? Play with it yourself [here](https://codesandbox.io/s/useeffect-gotcha-20jw9?file=/src/App.js).

Visit my [blog](https://blog.whereisthemouse.com/) and [follow me](https://twitter.com/iva_kop) on Twitter for more React-related content.

Image by [vectorjuice](https://www.freepik.com/vectors/technology)

