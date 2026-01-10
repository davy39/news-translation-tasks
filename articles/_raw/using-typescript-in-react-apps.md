---
title: How to Use TypeScript in React Apps
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-01-30T16:59:27.000Z'
originalURL: https://freecodecamp.org/news/using-typescript-in-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/bruno-martins-OhJmwB4XWLE-unsplash.jpg
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'Hi everyone! A while ago I wrote an article about TypeScript, explaining
  its main features and why it''s a good idea to use it in large projects.

  Today we''re going to take a quick look at how we can use TypeScript in a React
  app, so you can get an ide...'
---

Hi everyone! A while ago I wrote [an article about TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/), explaining its main features and why it's a good idea to use it in large projects.

Today we're going to take a quick look at how we can use TypeScript in a React app, so you can get an idea of how the implementation might look like and what are its benefits.

## **Table of Contents**

* [Intro to TypeScript](#intro-to-typescript)
    
* [How to Type Props](#heading-how-to-type-props)
    
* [How to Type Hooks](#heading-how-to-type-hooks)
    
    * [Typing the useState hook](#heading-typing-the-usestate-hook)
        
    * [Typing the useRef hook](#heading-typing-the-useref-hook)
        
* [Wrap up](#heading-wrap-up)
    

## Intro to TypeScript

So by now you should know that TypeScript is a superset of JavaScript. Superset means that it adds features on top of what JavaScript offers.

TypeScript takes all the functionalities and structures JavaScript provides as a language, and adds a few things to that. The main thing TypeScript provides is static typing.

When it comes to React, besides everything we can type in vanilla JS (like variables, function parameters and return values, etc.), we can mainly use TypeScript to type two things: component props and hooks.

One of the simplest ways to create a React app with TypeScript is to use [CRA](https://create-react-app.dev/docs/adding-typescript/), running `npx create-react-app my-app --template typescript`.

If you already have a CRA app created, in the docs you have info on how to install TypeScript on top of that. ;)

Also, for the examples here we're going to use CRA since it's nice and simple. But keep in mind that most frameworks like [Next](https://nextjs.org/docs/basic-features/typescript), [Vite](https://vitejs.dev/guide/features.html#typescript) and [Astro](https://docs.astro.build/en/guides/typescript/) also provide support for TypeScript.

So after running CRA's script you'll have a project that looks somewhat like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-299.png align="left")

As you can see, files are now named `.tsx` which is how TypeScript's compiler identifies you'll be using TypeScript in that file.

And besides, we have a `tsconfig.json` which is where we have all the compiler's config. You can learn more about that in [the previous article I wrote](https://www.freecodecamp.org/news/an-introduction-to-typescript/#typescriptscompiler).

Now let's create a component and see how we can put TypeScript to use.

## How to Type Props

For this example we will set up a dummy component responsible for rendering a number received as props, and adding to that number when a button gets clicked.

Regular JavaScript code would look something like this:

```javascript
const DummyComponent = ({ number, setNumber }) => {

  return (
    <>
      <div>{number}</div>

      <button
        onClick={() => setNumber(prev => prev+1)}
      >
        ADD
      </button>
    </>
  )

}

export default DummyComponent
```

And our fully typed version will look like this:

```javascript
import React, { Dispatch, SetStateAction } from 'react'

interface DummyProps {
  number: number
  setNumber: Dispatch<SetStateAction<number>>
}

const DummyComponent:React.FC<DummyProps> = ({ number, setNumber }) => {

  return (
    <>
      <div>{number}</div>

      <button
        onClick={() => setNumber(prev => prev+1)}
      >
        ADD
      </button>
    </>
  )

}

export default DummyComponent
```

You can see that next to the component name, we have added colons and `React.FC`. This basically tells the TypeScript component that `DummyComponent` is a React functional component. That itself doesn't do much, but it helps with TypeScript's intellisense.

Next to that we declared `<DummyProps>`. This declares that the props object that this component will receive must match the interface `DummyProps`.

An interface is TypeScript's way to type an object. Basically we declare all the properties that object will have, and the type for each of them.

Since this component will receive a state which is a number, and a function to update that state, that's exactly what we have within our interface:

```javascript
interface DummyProps {
  number: number
  setNumber: Dispatch<SetStateAction<number>>
}
```

Here you can see that for the `setNumber` function we're using this type: `Dispatch<SetStateAction>`. This is not a type native to TypeScript, but instead it's provided by React itself. So we have to import it each time we use it, like this:  
`import React, { Dispatch, SetStateAction } from 'react'`.

And that's it! You have typed your props now. What's cool about this is each time you call that component, you'll get intellisense about the props that component expects. Same as if you try to pass a prop not declared in the component's interface or provide a wrong type for an expected prop.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-300.png align="left")

*Intellisense on expected props*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-301.png align="left")

*Unexpected props error*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-302.png align="left")

*Wrong prop type*

This is what people mean when they say TypeScript self-documents your code. With just a few lines of boilerplate, now you can easily see what each component expects and doesn't. This comes in very handy when working in large projects, with hundreds of components which were written mostly by other people. ;)

## How to Type Hooks

When it comes to hooks, TypeScript is mostly used to type `useState` and `useRef` hooks. Let's see how that works.

#### Typing the `UseState` hook

This is what `useState` looks like without types:

```javascript
const [number, setNumber] = useState<>(0)
```

And with types it looks like this:

```javascript
const [number, setNumber] = useState<number>(0)
```

Almost no need to explain, right? We just declare the type of the state value like this: `<number>` and that's it. If we ever try to update that state with a different value type, we'll get a nice red error message to prevent us from shooting ourselves in the foot. ;)

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-303.png align="left")

*Wrong type error*

Keep in mind that if want to allow our state to hold different value types, we can declare that like this: `const [number, setNumber] = useState<number | string>(0)`.

Now we can pass either a number OR a string without getting errors.

### Typing the `UseRef` hook

`useRef` is a hook mainly used for referencing DOM elements on React. If you want to learn more about how the hook works, you can read [this guide](https://www.freecodecamp.org/news/full-guide-to-react-hooks/#useRef-hook) I recently wrote.

To see how we can implement it with TypeScript, we'll use this example:

```javascript
import React, { useEffect, useRef } from 'react'

const DummyComponent:React.FC = () => {

  const ref = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (ref.current) ref.current.focus()
  }, [])

  return (
      <input type="text" ref={ref} />
  )

}

export default DummyComponent
```

As you can see, we're initiating the `ref` variable with `null` and declaring its type as `HTMLInputElement`. When using the useRef hook and declaring its type, the variable can be assigned either to `null` or the declared type.

Then we have a `useEffect` hook that focuses the element if it has a `current` property. And lastly we're returning an `input` element and assigning the reference we previously declared: `ref={ref}`.

The cool thing about typing the `useRef` hook is that TypeScript will prevent us from trying to perform actions or read data from types that don't match.

For example, if we declared the type `number` for the ref, we would get the following errors:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-364.png align="left")

*Can't focus on type number*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-365.png align="left")

*Can't assign a number reference to an HTML element*

Again, this is nice because it avoids silly errors ahead of time and saves us from having to debug this stuff later on. Especially when working with large codebases where many other people also work on, TypeScript gives us a more controlled and ordered environment to work in.

## Wrap up

Well everyone, as always, I hope you enjoyed the article and learned something new.

If you'd like a deeper take on this topic, I recommend [this video by Firebase](https://www.youtube.com/watch?v=ydkQlJhodio) or this other one be [Ben Awad](https://www.youtube.com/watch?v=Z5iWr6Srsj8).

If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman). See you in the next one!

![Image](https://www.freecodecamp.org/news/content/images/2023/01/goodbye-farewell.gif align="left")
