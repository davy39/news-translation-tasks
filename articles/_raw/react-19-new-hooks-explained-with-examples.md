---
title: React 19 – New Hooks Explained with Examples
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-05-28T12:56:51.000Z'
originalURL: https://freecodecamp.org/news/react-19-new-hooks-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/thumb.jpeg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Hi fellow readers! Web Development is a constantly evolving landscape.
  The whole ecosystem consists of different libraries and technologies. React is one
  of the most widely used libraries in web development.

  There are small releases every now and the...'
---

Hi fellow readers! Web Development is a constantly evolving landscape. The whole ecosystem consists of different libraries and technologies. React is one of the most widely used libraries in web development.

There are small releases every now and then. However, this year, the React team has made a significant announcement introducing a new version, React 19. On April 25, 2024, React officially released the beta version of React 19 to the public.

This version comes with a whole host of new features, along with new hooks. In this post, we are going to discuss four new hooks available in the new version:

* [useFormStatus](#heading-useformstatus)
    
* [useActionState](#heading-useactionstate)
    
* [useOptimistic](#heading-useoptimistic)
    
* [use](#heading-use)
    

## Existing Form Handling Implementation

Before going into the first hook, let's see how we currently implement form handling in React:

```javascript
import { submitAction } from "./actions";

const FormHandling = () => {
  const [name, setName] = useState("");
  const [pending, setPending] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setPending(true);
    await submitAction({ name });
    setPending(false);
    setName("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        placeholder="Enter your name"
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Submit</button>
      {pending && <p>Submitting {name}...</p>}
    </form>
  );
};
```

Normally, we use state-controlled form to set the form data and use it to submit the same to the server with the `onSubmit` attribute of the form. Also, we use a `pending` state variable to handle submission pending states.

The next three hooks I have shown will change the way we handle forms.

## useFormStatus

The `useFormStatus` hook gives information about the form's status while submitting the form. This hook is part of the React DOM, so import it from `react-dom`:

```javascript
import {useFormStatus} from 'react-dom'
```

This hook can be used in the following way:

```javascript
  const { pending, data } = useFormStatus();
```

The hook does not take any arguments and returns an object containing information about the form's status. It returns:

* `pending`, which is a boolean value that indicates whether the form is in pending state.
    
* `data`, which is an object of type `[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)`, and contains the values of the form fields.
    

This hook can only be used inside a component that has a

element as its parent. It only returns status information of the parent form element and not the `<form>` element rendered in the same component.

The following will not work:

```javascript
const {pending, data} = useFormStatus()
return (
    <form action={submit}></form>
  );
```

Let's use the same previous form and write it in a separate component:

```javascript
import { submitAction } from "../../actions";
import { useFormStatus } from "react-dom";

const Form = () => {
  const { pending, data } = useFormStatus();

  return (
    <div>
      <input type="text" name="username" placeholder="Enter your name" />
      <button disabled={pending} type="submit">
        Submit
      </button>
      {pending && <p>Submitting {data?.get("username")}...</p>}
    </div>
  );
};

const FormStatusWithHooks = () => {
  return (
    <form
      action={async () => {
        await submitAction();
      }}
    >
      <Form />
    </form>
  );
};
```

Here, instead of using `onSubmit`, we are using the action prop of the form element. And we have used the `data` object to access the form fields and render them.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731049965919/b3e23267-8d1b-4d76-b996-8c7d965b96a5.png align="center")

*Rendering form data with pending state*

You can use any number of forms inside the parent `<form>` element and get the form state with `useFormStatus` hook. So, you do not need to implement the same logic every time. This improves reusability in the code.

## useActionState

`useActionState` can be used in the following way:

```javascript
const [state, formAction] = useActionState(submitData, initialState);
```

It takes the following parameters:

* `submitData`, which is the function that is called when form is submitted. This function should take two parameters: the current state and a FormData object.
    
* `initialState`, which is the initial value of the state when the form is not submitted.
    

It returns an array with following:

* `state`, which is the current state that is being rendered in the component. This state is equal to the initial state.
    
* `formAction`, which is the new action that you can pass to the action prop of your form element. This executes the action that you passed with the current state and returns a new, updated state.
    

Let's understand how to use the hook with the following form:

```javascript
<form action={formAction}>
      <div>
        <input type="text" name="username" placeholder="Enter your name" />
        <input type="number" name="age" placeholder="Enter age" />
        <button type="submit">Submit</button>
      </div>
    </form>
```

This form submits user information, name and age, which is appended to a list of users stored as state. Let's use the `useActionState` hook to get the state:

```javascript
import { useActionState, useEffect } from "react";
import { submitActionWithCurrentState } from "../../actions";
const ActionStateComponent = () => {
  const [state, formAction] = useActionState(submitActionWithCurrentState, {
    users: [],
    error: null,
  });

return <form action={formAction}>...</form>
```

The `submitActionWithCurrentState` method returns a new state consisting of the modified users list and gives an error if a user with the given name already exists. Let's render the list of users and error (if any):

```javascript
<div className="error">{state?.error}</div>
      {state?.users?.map((user) => (
        <div key={user.username}>
          Name: {user.username} Age: {user.age}
        </div>
      ))}
```

After you submit the form, the component re-renders and updates the state in the component.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050034809/e30a20be-aca2-4973-99ba-8cc6192657bb.png align="center")

*List of submitted users stored as state*

If you try to submit an existing user name you get an error:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050059494/a5d51224-c6e4-43eb-b2ae-0ee4059d0b54.png align="center")

*Error if user already exists*

## useOptimistic

As the name suggests, `useOptimistic` optimistically updates the UI while an async operation is still underway. When a user submits a form that changes a piece of UI, this hook can "optimistically" show the expected result while the form is still submitting.

* If the form submission is successful, the UI remains the same.
    
* If the form submission fails, the UI reverts back to the previous state.
    

This allows you to immediately update the UI even if the form submission takes time:

```javascript
const [optimisticState, setOptimisticState] = useOptimistic(actualState, updateFn);
```

The `useOptimistic` hook takes the following parameters:

* `actualState`, which is the value of the optimistic state when no action is pending.
    
* `updateFn` (optional), which is a function that takes the actual state and the value passed to the `setOptimisticState` method and calculates the optimisticState. If this parameter is not specified, the optimistic state is equal to the new value.
    

It returns the following:

* `optimisticState`, which is the optimistic (temporary) value shown while the action is pending.
    
* `setOptimisticState`, which is a function that sets the optimistic state to a new value.
    

Let's have a form that performs an async operation to change the title of the page:

```javascript
import { useOptimistic, useState } from "react";

const OptimisticComponent = () => {
  const [title, setTitle] = useState("Title");
  const [optimisticTitle, setOptimisticTitle] = useOptimistic(title);
  const [error, setError] = useState(null);
  const pending = title !== optimisticTitle;
  const handleSubmit = async (formData) => {
   
  };
  return (
    <div>
      <h2>{optimisticTitle}</h2>
      <p> {pending && "Updating..."} </p>
      <form action={handleSubmit}>
        <input type="text" name="title" placeholder="Change Title" />
        <button type="submit" disabled={pending}>
          Submit
        </button>
      </form>
      <div className="error">{error && error}</div>
    </div>
  );
};
```

In the code above:

* We are displaying the optimistic value of the title, which is set to `title` state when no action is pending.
    
* We have defined a pending variable that is set to true if the current and optimistic state do not match. Depending on this, we display a pending text and disable the button.
    
* We display an error in case the async operation throws an error.
    

Now, let's call our async function that either resolves or rejects our request:

```javascript
import { submitTitle } from "../../actions";

const OptimisticComponent = () => {
  
  ...
  
  const handleSubmit = async (formData) => {
    setError(null);
    setOptimisticTitle(formData.get("title"));
    try {
      const updatedTitle = await submitTitle(formData);
      setTitle(updatedTitle);
    } catch (e) {
      setError(e);
    }
  };
  
  ...
  
};
```

In the code above:

* We have updated the states as we originally did.
    
* Before calling the async operation, we set the optimistic state to the updated title we just submitted.
    
* If the promise rejects, the optimistic state reverts back to the original one, so no need to set it again.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050097373/a130fbe2-f3b4-4073-9330-4e38de8dfb4c.png align="center")

*Title Updating optimistically*

## use

The `use` method has not been released as a hook, but as part of the React API. Unlike React hooks, `use` can also be called inside `if` and `for` statements. However, `use` can only be called inside a Component or a Hook.

`use` lets you read the value of a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) or a [Context](https://react.dev/learn/passing-data-deeply-with-context) inside a component. Let's understand its usage in reading both context and promise.

#### Reading contexts

In case of contexts, `use` works similar to the [`useContext`](https://react.dev/reference/react/useContext) hook. It returns the value provided by the context to be used inside the component:

```javascript
import { createContext, use } from "react";
import "../../styles.css";

const ThemeContext = createContext(null);
const UseHookWithContext = () => {
  return (
    <ThemeContext.Provider theme="dark">
      <MyComponent />
    </ThemeContext.Provider>
  );
};

const MyComponent = () => {
  const theme = use(ThemeContext);
  return (
    <div className={`myContainer theme-${theme}`}>
      <h2>Hi There!</h2>
    </div>
  );
};
```

The code above gives the following output:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050125728/19276d93-21ad-4694-8eb0-3f5f517235a7.png align="center")

*Dark Theme*

Unlike `useContext`, `use` provides more flexibility since it can also be used conditionally using `if` statements:

```javascript
const CodeSnippet = ({canShow}) => {
    if(canShow) {
        const theme = use(ThemeContext)
        return <h2>Code snippet shown with {theme} theme </h2>
    }
    return null
}
```

#### Reading resolved values of promises

`use` returns the resolved value of the promise to be used inside the component. It integrates with the [Suspense](https://react.dev/reference/react/Suspense) API to display a temporary message till a promise is resolved.

Let's have a client component with a promise passed down as a prop from a server component:

```javascript
"use client";

import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

const DataContainer = ({ dataPromise }) => {
  return (
      <Suspense fallback={<p>Fetching Data...</p>}>
        <DataComponent dataPromise={dataPromise} />
      </Suspense>
  );
};

const DataComponent = ({ dataPromise }) => {
  const data = use(dataPromise);
  return <div>{data && data}</div>;
};
```

In the code above:

* The promise created in a server component is passed down to client component as a prop. This in turn, can be passed to the `use` method. This allows the client component to read the resolved value of the promise.
    
* The `Suspense` API renders the element passed to the `fallback` prop while the promise is still pending.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050154298/a5cc1b8f-63ba-400f-b42e-df1da7a81b3c.png align="center")

*Data shown on button click*

In case a promise rejects, there are two ways to display an error to the users:

1. Returning an error message in the `catch` block of the promise and treating it as a resolved promise:
    

```javascript
export function fetchData() {
  return new Promise((resolve, reject) => {
    ...
    // ...
    
  }).catch((err) => err);
}
```

2. Wrapping the component with an [ErrorBoundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary):
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1731050189144/2aa97ad6-0da9-4ee2-8ba1-5770d8e66156.png align="center")

*Error Boundary rendered when Promise rejected*

You can find the complete code in the CodeSandbox [here](https://codesandbox.io/p/sandbox/gracious-haslett-4qdzn4?file=%2Fsrc%2Findex.js&from-embed=). Feel free to fork it and play around.

%[https://codesandbox.io/embed/4qdzn4?view=preview&module=%2Fsrc%2FApp.js] 

This is not the end. React 19 has a lot more to offer. You can check out all the new features in the [docs](https://react.dev/blog/2024/04/25/react-19).

Currently, React 19 is still in beta version, so do not use it for production systems yet. However, you can install React 19 canary version by adding the following dependencies in your `package.json` file and running `npm i`:

```javascript
"dependencies": {
    "react": "canary",
    "react-dom": "canary",
  },
```

## Conclusion

The React Team has introduced several useful hooks that will improve convenience for developers.

The first three hooks: `useFormStatus`, `useActionState`, and `useOptimistic` change the way we handle forms. The `use` hook makes it really convenient to get the resolved value of a promise inside a component.

In this post, I have explained the syntax of each hook and demonstrated their usage examples. This would surely help you to understand these hooks and how to use them. I hope this helps you in your future projects.

If you have any questions or need further clarification, let me know. Your feedback is always valued and appreciated! Connect with me on Twitter for more updates and discussions. Thank you for reading, and I look forward to seeing you next time!
