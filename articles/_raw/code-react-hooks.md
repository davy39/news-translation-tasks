---
title: How to Create Your First React Hook from Start to Finish
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-02T14:58:22.000Z'
originalURL: https://freecodecamp.org/news/code-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/how-to-create-your-first-react-hook.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'You can use custom React hooks to solve many different real-world problems
  in your React projects.

  As a result, learning how to make React hooks is a necessary skill in becoming a
  top-notch React developer.

  In this article, let''s take a look at how t...'
---

You can use custom React hooks to solve many different real-world problems in your React projects.

As a result, learning how to make React hooks is a necessary skill in becoming a top-notch React developer.

In this article, let's take a look at how to create our own custom React hook from start to finish that lets users copy code snippets or any other text in our app.

## What feature do we want to add?

On my website, reedbarger.com, I allow users to copy code from my articles with the help of a package called `react-copy-to-clipboard`.

A user just hovers over the snippet, clicks the clipboard button, and the code is added to their computer's clipboard. This allows them to paste and use the code, wherever they like.

![copy-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/fnmmit9fvxb4lejz3dcm.gif)

## How to recreate react-copy-to-clipboard

Instead of using a third party library, however, I wanted to recreate this functionality with my own custom React hook. 

As with every custom React hook I create, I put it a dedicated folder, usually called `utils` or `lib`, specifically for functions that I can reuse across my app.

We'll put this hook in a file called `useCopyToClipboard.js` and I'll make a function of the same name. Also make sure to import React up at the top.

There are various ways that we can copy some text to the user's clipboard. However, I prefer to use a library for this, which makes the process more reliable, called `copy-to-clipboard`.

It exports a function, which we will call `copy`.

```jsx
// utils/useCopyToClipboard.js
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {}

```

Next we will create a function that will be used for copying whatever text wants to be added to the users clipboard. We will call this function `handleCopy`.

## How to make the handleCopy function

Within the function, we first need to make sure that it only accepts data that is of type string or number. 

We will set up an if-else, which will make sure that the type is either the string or number. Else, we will log an error to the console that tells the user they cannot copy any other types.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {
  const [isCopied, setCopied] = React.useState(false);

  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      // copy
    } else {
      // don't copy
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }
}

```

Next we will want to take the text and convert it to a string, which we will then pass to the `copy` function. From there, we want to return the handle copying function from the hook wherever we like in our application. Generally, the `handleCopy` function will be connected to an `onClick` of a button.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {
  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
    } else {
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }

  return handleCopy;
}

```

Additionally, we want some state that represents whether the text was copied or not. To create that, we will call `useState` at the top of our hook and make a new state variable `isCopied`, where the setter will be called `setCopy`.

Initially this value will be false. If the text is successfully copied. We will set `copy` to true. Else, we will set it to false.

Finally, we will return `isCopied` from the hook within an array along with `handleCopy`.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard(resetInterval = null) {
  const [isCopied, setCopied] = React.useState(false);

  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
      setCopied(true);
    } else {
      setCopied(false);
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }

  return [isCopied, handleCopy];
}

```

## How to use useCopyToClipboard

We can now use `useCopyToClipboard` within any component that we like.

In my case I will use it with a copy button component, which received the code for our code snippet.

To make this work all we need to do is add an on click to the button. And in the return of a function called handle copy with the code asked to it as text. And once it's copied it's true. We can show a different icon indicating that a copy was successful.

```jsx
import React from "react";
import ClipboardIcon from "../svg/ClipboardIcon";
import SuccessIcon from "../svg/SuccessIcon";
import useCopyToClipboard from "../utils/useCopyToClipboard";

function CopyButton({ code }) {
  const [isCopied, handleCopy] = useCopyToClipboard();

  return (
    <button onClick={() => handleCopy(code)}>
      {isCopied ? <SuccessIcon /> : <ClipboardIcon />}
    </button>
  );
}

```

## How to add a reset interval

There's one improvement we can make to our code. As we've currently written our hook, `isCopied` will always be true, meaning we will always see the success icon:

![success-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/pgpdz9f5xp7nr4twovsn.gif)

If we want to reset our state after a few seconds we can pass a time interval to useCopyToClipboard. Let's add that functionality.

Back in our hook, we can create a parameter called `resetInterval`, whose default value is `null`, which will ensure that the state will not reset if no argument is passed to it.

We will then add `useEffect` to say that if the text is copied and we have a reset interval we will set `isCopied` back to false after that interval using a `setTimeout`.

Additionally, we need to clear that timeout if our component that the hook is being used in unmounts (meaning our state is no longer there to update).

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard(resetInterval = null) {
  const [isCopied, setCopied] = React.useState(false);

  const handleCopy = React.useCallback((text) => {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
      setCopied(true);
    } else {
      setCopied(false);
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }, []);

  React.useEffect(() => {
    let timeout;
    if (isCopied && resetInterval) {
      timeout = setTimeout(() => setCopied(false), resetInterval);
    }
    return () => {
      clearTimeout(timeout);
    };
  }, [isCopied, resetInterval]);

  return [isCopied, handleCopy];
}

```

Finally, the last improvement we can make is to wrap `handleCopy` in the `useCallback` hook in order to ensure that it will not be recreated every time there is a rerender.

## Final Result

And with that, we have our final hook, which allows the state to be reset after a given time interval. If we pass one to it, we should see a result like what we have below:

```jsx
import React from "react";
import ClipboardIcon from "../svg/ClipboardIcon";
import SuccessIcon from "../svg/SuccessIcon";
import useCopyToClipboard from "../utils/useCopyToClipboard";

function CopyButton({ code }) {
  // isCopied is reset after 3 second timeout
  const [isCopied, handleCopy] = useCopyToClipboard(3000);

  return (
    <button onClick={() => handleCopy(code)}>
      {isCopied ? <SuccessIcon /> : <ClipboardIcon />}
    </button>
  );
}

```

![final-result.gif](https://dev-to-uploads.s3.amazonaws.com/i/kul32jsgeevk92j2j5ll.gif)

I hope you learned a few things through this process of creating our hook, and that you use it throughout your own personal projects to copy any text you like to the clipboard.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

