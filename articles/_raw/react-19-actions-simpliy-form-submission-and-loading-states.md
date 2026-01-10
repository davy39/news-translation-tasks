---
title: React 19 Actions – How to Simplify Form Submission and Loading States
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2024-07-02T21:29:47.000Z'
originalURL: https://freecodecamp.org/news/react-19-actions-simpliy-form-submission-and-loading-states
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/React--1-.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'React 19 introduces Actions, which are asynchronous functions. Actions
  are helpful in making form submissions easier. This tutorial dives into what Actions
  are and how to use them.

  You''ll learn about:


  The new React 19 feature, Actions

  The new React ...'
---

React 19 introduces Actions, which are asynchronous functions. Actions are helpful in making form submissions easier. This tutorial dives into what Actions are and how to use them.

You'll learn about:

1. The new React 19 feature, Actions
2. The new React 19 hooks, `useActionState` and `useFormStatus`
3. How to convert a React 18 form to a React 19 form

I also made a [video version of this article](https://www.youtube.com/watch?v=ExZUdkfu-KE&t=443s) if you'd like to learn from that as well.

## Feature: React Actions

To understand Actions, let's first take a look at how we manage forms today. In React 18 and earlier, we submit forms using the `handleSubmit` function in a button. Here's a simple form that has one input field `name`:

```jsx
// Form submission in React 18
console.info('React 18 form');

const [name, setName] = useState('');
const [isPending, setIsPending] = useState(false);

const handleChange = (event) => {
  setName(event.target.value);
};

const handleSubmit = (event) => {
  event.preventDefault();
  setIsPending(true);
  setTimeout(() => {
    // call API
    setIsPending(false);
  }, 500);
};

return (
  <form>
    <input type="text" name="name" onChange={handleChange} />
    {isPending ? <p>Loading...</p> : <p>Hello in React 18, {name}</p>}
    <button onClick={handleSubmit} disabled={isPending}>
      Update
    </button>
  </form>
);

```

In this code, we are doing the following:

1. Adding a loading state: We use a variable `isPending` to manually keep track of the loading state.
2. Form submission: The form is submitted using the `handleSubmit` event handler attached to the `onClick` event of the button.
3. Capturing the submitted value: The `handleChange` function captures the submitted value and stores it in state variables.

## What Are React Actions?

With React 19, handling forms becomes easier with Actions, inspired by frameworks such as Remix. One key feature is the enhanced use of `startTransition` to manage pending states.

`startTransition` was introduced in React 18, allowing developers to mark certain updates as less urgent. 

In React 19, `startTransition` can now handle async functions, making it even more powerful for managing asynchronous tasks and improving the user experience during form submissions.

```js
const [isPending, startTransition] = useTransition();

const handleSubmit = () => {
  startTransition(async () => {
    const error = await updateName(name);
    if (error) {
      setError(error);
      return;
    }
    redirect('/path');
  });
};

```

This async function inside `startTransition` is called an Action. What makes actions cool is that they can be used directly to submit forms like so:

```html
<form action="{actionFn}">...</form>

```

This format may look familiar if you are experienced with PHP.

## How to Create a React Action

To create an async function, we can use a new hook introduced in React 19 called `useActionState`. We call this hook and pass in an action function and an initial state. This hook returns the updated state and a form action `actionFn`, which can be used to wire up a form.

```js
const [state, actionFn] = useActionState(submitAction, { name: '' });

```

Now with this wired up with the form, we have the following:

```jsx
<form action={actionFn}>
  <input type="text" name="name" />

  <button type="submit" disabled="{pending}">
    Update
  </button>
</form>

```

To add a loading state, we can use a new hook introduced in React 19 called `useFormStatus`.

```js
const { pending, data, method, action } = useFormStatus();

```

This hook provides information on the status of the form. The `pending` state indicates whether the form is being submitted, and `data` is a `FormData` object containing the submitted data. We use this pending state to show a loader.

But there is one caveat: this hook can only be used in a child component, not in the form itself. So, we have to create child components `SubmitButton` and `Loader` to retrieve a `pending` state:

```js
function Loader() {
  const { pending } = useFormStatus();
  return <div>{pending && "Loading..."}</div>;
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      Update
    </button>
  );
}

....

return(
<form action={formAction}>
      <input type="text" name="name" />
      <Loader />
      <SubmitButton />
    </form>
)

```

We can also capture useful information about the data submitted to the form by retrieving it from the state returned from `useActionState`.

```js
const [state, formAction] = useActionState(submitAction, { name: '' });

```

So here's the final form:

```jsx
function Loader() {
  const { pending } = useFormStatus();
  return <div>{pending && 'Loading...'}</div>;
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      Update
    </button>
  );
}

function Name({ name }) {
  return <p>Hello in 19 {name}</p>;
}

function App() {
  console.info('React 19 form');

  const [state, formAction] = useActionState(submitAction, { name: '' });

  return (
    <form action={formAction}>
      <input type="text" name="name" />
      <Loader />
      <SubmitButton />
      <Name name={state?.name} />
    </form>
  );
}

```

Compare this with the React 18 form at the top of this post to check the difference.

## Conclusion

By utilizing actions along with hooks like `useActionState` and `useFormStatus`, we can easily manage form states, capture submitted data, and provide responsive feedback to users during form submissions to show pending states. 

I am excited for this improved experience of handling forms in React 19, and I look forward to removing unnecessary `handleSubmits`, `useState`s, and `pending` states.

In my next article, I will discuss another exciting new React feature: the React Compiler. This tool automatically memoizes, eliminating the need for `useMemo` and `useCallback`. Stay updated and get the article directly in your inbox by joining my newsletter.

<iframe src="https://shrutikapoor.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>


