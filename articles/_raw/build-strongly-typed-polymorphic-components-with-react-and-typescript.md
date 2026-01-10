---
title: Intermediate TypeScript and React Handbook – How to Build Strongly Typed Polymorphic
  Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-26T14:49:10.000Z'
originalURL: https://freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/6Lc6ro2.png
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Emmanuel Ohans

  Hey everyone! 😎 In this detailed guide, I’ll show you how to build strongly typed
  Polymorphic React components with Typescript.

  If you prefer to read the entire guide in a single PDF document, you can download
  the accompanying free...'
---

By Emmanuel Ohans

Hey everyone! 😎 In this detailed guide, I’ll show you how to build **strongly typed Polymorphic React components with Typescript**.

If you prefer to read the entire guide in a single PDF document, you can download the [accompanying free PDF](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-173.png)
_You can [download the eBook for free](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)._

## Table of contents 

* [Github repository](#heading-github-repository)
* [Ideal audience for this book](#heading-ideal-audience-for-this-book)
* [What are Polymorphic Components?](#heading-what-are-polymorphic-components)
* [Examples of Polymorphic Components in the Real World](#heading-examples-of-polymorphic-components-in-the-real-world)
* [Polymorphic components in Chakra UI](#heading-polymorphic-components-in-chakra-ui)
* [Material UI’s component prop](#heading-material-uis-component-prop)
* [How to Build Your First Polymorphic Component](#heading-how-to-build-your-first-polymorphic-component)
* [The Problems with This Simple Implementation](#heading-the-problems-with-this-simple-implementation)
* [Welcome, TypeScript](#heading-welcome-typescript)
* [Introduction to TypeScript Generics](#heading-introduction-to-typescript-generics)
* [How to Constrain Generics](#heading-how-to-constrain-generics)
* [Making sure the Polymorphic prop only accepts valid HTML strings](#heading-make-sure-the-as-prop-only-receives-valid-html-element-strings)
* [How to Handle Valid Component Attributes](#heading-how-to-handle-valid-component-attributes)
* [How to Handle Default Polymorphic Props](#heading-how-to-handle-default-as-attributes)
* [The Component Should Be Reusable with its Props](#heading-the-component-should-be-reusable-with-its-props)
* [How to Create a Reusable Utility for Polymorphic Types](#heading-how-to-create-a-reusable-utility-for-polymorphic-types)
* [The Component Should Support refs](#heading-the-component-should-support-refs)
* [Conclusion and Next Steps](#heading-conclusion-and-next-steps)

## Github repository

The [Github repository](https://github.com/ohansemmanuel/polymorphic-react-component) contains all the code implementation in this guide.

## Ideal audience for this book

If you have no idea what strongly typed Polymorphic React components with Typescript means, that’s fine. That’s a decent pointer that this is just the right guide for you.

This guide has been written specifically for beginners and mid level engineers in mind. This will help you learn more advanced Typescript concepts in a practical way.  

Ready? Let's dive in.

## What are Polymorphic Components?

When you learn React, one of the first concepts you learn is how to build reusable components.

This is the fine art of writing components once, and reusing them multiple times.

If you remember from React 101, the essential building blocks of classic reusable components are props and state—where props are external, and state is internal.  


![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-129.png)
_Building blocks of reusable components_

The essential building blocks of reusability remain valid for this article. However, we will take advantage of props to allow the users of your component decide what “element” to eventually render.

OK, wait, don’t get confused by that.

Consider the following React component:

```js
const MyComponent = (props) => {
  return (
    <div>
     This is an excellent component with props {JSON.stringify(props)}
   </div>
  );
};
```

Typically, your component would receive some props. You’d go ahead to use these internally and then finally render some React element which gets translated to the corresponding DOM element. In this case, the div element.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-131.png)
_Rendering a single element_

What if your component could take in props to do more than just provide some data to be consumed within your component?

Instead of `MyComponent` always rendering a `div`, what if you could pass in a prop to determine the eventual element rendered to the `DOM`?

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-132.png)
_An illustration on deciding the render UI of a component_

This is where polymorphic components come in.

By standard definition, the word _Polymorphic_ means occurring in several forms. In the world of React components, a polymorphic component is a component that can be rendered with a different container element / node.

Even though the concept may sound strange to you (if you’re new to it in general), you’ve likely already used a Polymorphic component.

## Examples of Polymorphic Components in the Real World

Open-source component libraries typically implement some sort of Polymorphic component.

Let’s consider some you may be familiar with.

I may not discuss your favourite open-source library, but please don't hesitate to take a look at your favourite OS library after you understand the examples here.

### Polymorphic components in Chakra UI

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-133.png)
_Chakra UI_

[Chakra UI](https://chakra-ui.com/) has been my component library of choice for a decent number of production applications.

It’s easy to use, has dark-theme support, and is accessible by default (oh, not to forget the subtle component animations!).

So, how does Chakra UI implement polymorphic props? The answer is by exposing an `as` prop.

The `as` prop is passed to a component to determine what eventual container element to render.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.33.33@2x.png)
_The chakra UI as prop used with the Box component_

Using the `as` prop is quite straightforward.

You pass it to the component, in this case, `Box` :

```js
<Box as="button"> Hello </Box>
```

And the component will render a button element.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.34.22@2x.png)
_The Box component rendered as a "button" element_

If you went ahead and changed the `as` prop to a `h1`:

```js
<Box as="h1"> Hello </Box>
```

Now, the `Box` component renders an h1:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.40.06@2x-1.png)
_The Box component rendered as an "h1" element_

That’s a polymorphic component at work!

This component can be rendered to entirely unique elements, all by passing down a single prop.

### Material UI’s component prop

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-134.png)
_The Material UI component library_

Material UI in most cases needs no introduction. It’s been a staple of component libraries for years now. It’s a robust component library with a mature user base.

Similar to chakra UI, Material UI allows for a polymorphic prop called `component` — it doesn’t matter what you choose to call your polymorphic prop (for example Chakra UI calls it `as`).

Its usage is similar. You pass it to a component, stating what element or custom component you’d like to render.

Enough talking, here’s an example from the official docs:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.41.34@2x.png)
_The Material UI component prop_

```jsx
<List component="nav">
 <ListItem button>
   <ListItemText primary="Trash" />
 </ListItem>
</List>
```

`List` is passed a component prop of `nav`, and so when this is rendered, it’ll render a `nav` container element.

Another user may use the same component, but not as navigation. They may just want to render a to-do list:

```jsx
<List component="ol">
...
</List>
```

And in this case, List will render an ordered list `ol` element.

Talk about flexibility! You can see a summary of the [use cases here](https://github.com/ohansemmanuel/polymorphic-react-component/blob/master/use-cases.pdf) (PDF) for polymorphic components.

As you’ll come to see in the following sections of this handbook, polymorphic components are powerful. Apart from just accepting a prop of an element type, they can also accept custom components as props.

We'll discuss them in a coming section of this guide. For now, let’s get you building your first Polymorphic component!

![Image](https://www.freecodecamp.org/news/content/images/2022/05/stprc-meta-2.png)
_[The Build strongly Typed Polymorphic React Components ebook](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)_

If you're serious about becoming a pro Typescript React developer, you can [download the accompanying free ebook](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components). I'll also send you a free email newsletter on real-world Typescript titled: **5 Typescript secrets you did not know.** You can [get it here](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

## How to Build Your First Polymorphic Component

Contrary to what you may think, building your first Polymorphic component is quite straightforward.

Here’s a basic implementation:

```jsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

What to note here is the polymorphic prop `as` — similar to chakra UI’s. This is the exposed prop to control the render element of the Polymorphic component.

Secondly, note that the `as` prop isn’t rendered directly. The following would be wrong:

```jsx
const MyComponent = ({ as, children }) => {
  // wrong render below 👇
  return <as>{children}</as>;
};
```

When rendering an [element type at runtime](https://reactjs.org/docs/jsx-in-depth.html#choosing-the-type-at-runtime), you must first assign it to a capitalised variable, and then render the capitalised variable.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-135.png)
_Using a capitlized variable within a React component_

Now you can go ahead and use this component as follows:

```jsx
<MyComponent as="button">Hello Polymorphic!<MyComponent>
<MyComponent as="div">Hello Polymorphic!</MyComponent>
<MyComponent as="span">Hello Polymorphic!</MyComponent>
<MyComponent as="em">Hello Polymorphic!</MyComponent>
```

Note the different `as` prop passed to the rendered components above.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-136.png)
_The different rendered elements of the component_

## The Problems with This Simple Implementation

The implementation in the previous section, while quite standard, has quite a few issues.

Let’s explore some of these.

### 1. The `as` prop can receive invalid HTML elements.

Presently, it is possible for a user to go ahead and write the following:

```tsx
<MyComponent as="emmanuel">Hello Wrong Element</MyComponent>
```

The `as` prop passed here is `emmanuel`. 

`Emmanuel` is an incorrect `HTML` element, but the browser also tries to render this element.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-152.png)
_Rendering a wrong HTML element type_

An ideal development experience is to show some kind of error during development. For example, a user may make a simple typo: `divv` instead of `div` — and would get no indication of what’s wrong.

### 2. Incorrect attributes can be passed for valid elements.

Consider the following component usage:

```tsx
<MyComponent as="span" href="https://www.google.com">
   Hello Wrong Attribute
</MyComponent>
```

A consumer can pass a `span` element to the `as` prop, and an `href` prop as well.

This is technically invalid.

A `span` element does not (and should not) take in an `href` attribute. That is invalid `HTML` syntax.

However, now, a consumer of the component we've built could go ahead and write this and they’d get no errors during development.

### 3. No attribute support!

Consider the simple implementation again:

```tsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

The only props this component accepts are `as` and children, nothing else. There’s no attribute support for even valid as element props. That is, if `as` were an anchor element `a`, we should also support passing an `href` to the component.

```tsx
<MyComponent as="a" href="...">A link </MyComponent>
```

Even though `href` is passed in the example above, the component implementation receives no other props. Only `as` and children are deconstructed.

Your initial thoughts may be to go ahead and spread every other prop passed to the component as follows:

```jsx
const MyComponent = ({ as, children, ...rest }) => { 
  const Component = as || "span";

  return <Component {...rest}>{children}</Component>;
};
```

It seems like a decent solution, but now it highlights the second problem mentioned above. Wrong attributes will now be passed down to the component as well.

Consider the following:

```jsx
<MyComponent as="span" href="https://www.google.com">
  Hello Wrong Attribute
</MyComponent>
```

And note the eventual rendered markup:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-153.png)
_A span element with an href attribute_

A span with an `href` is invalid `HTML`.

How do we resolve these concerns?

To be clear, there’s no magic wand to wave here. However, we’re going to leverage Typescript to ensure you build strongly typed Polymorphic components.

Upon completion, developers using your component will avoid the runtime errors above and instead catch them during development or build time—thanks to TypeScript.

### Why is this bad?

To recap, our simple implementation is subpar because:

* It provides a terrible developer experience
* It is not type-safe. Bugs can (and will) creep in.

## Welcome, TypeScript

If you’re reading this, a prerequisite is you already know some `TypeScript`—at least the basics. If you have no clue what TypeScript is, I strongly recommend giving this [document](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html) a read first.

OK, we’ve established a starting point – that is, we will leverage TypeScript to solve the concerns we just discussed. Essentially, we will leverage TypeScript to build strongly typed Polymorphic components.

The first two requirements we will start off with include:

* The `as` prop should not receive invalid `HTML` element strings
* Wrong attributes should not be passed for valid elements

In the following section, we will see how TypeScript can make our solution more robust, developer friendly, and production worthy.

## Introduction to TypeScript Generics

If you have a solid grasp of TypeScript generics, feel free to skip this section. This only provides a brief introduction for readers who aren’t as familiar with generics.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-154.png)
_Illustration: Javascript variables and Typescript generics are identical_

### What are Generics in TypeScript?

If you’re new to TypeScript generics, they can come off as difficult. But once you get the hang of it, you’ll see it for what it truly is: an arguably simple construct for parametizing your types.

So, what are generics?

A simple mental model you can use to approach generics is to see them as special variables for your types. Where JavaScript has variables, TypeScript has generics (for types).

Let’s have a look at a classic example.

Below is an `echo` function where `v` represents any arbitrary value:

```jsx
const echo = (v) => {
  console.log(v)
  return v
}
```

The `echo` function takes in this value v, logs it to the console, and then returns the same value to the caller. No input transformations carried out!

Now, we can go ahead and use this function on varying input types:

```js
echo(1) // number
echo("hello world") // string
echo({}) // object
```

And this works perfectly.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-155.png)
_The echo function code block_

There’s just one problem. We haven’t typed this function at all.

Let’s sprinkle some TypeScript in here. 🧁

Start off with a naïve way to accept any input values `v` by using the `any` keyword:

```js
const echo = (v: any) => {
  console.log(v)
  return v
}
```

It seems to work.

You’ll get no TypeScript errors when you do this. However, if you take a look at where you invoke this function, you’ll notice one important thing: you’ve now lost every form of type safety.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-156.png)
_The any type used in the echo function_

This may not be clear now, but if you went ahead to perform an operation as follows:

```ts
const result = echo("hello world")
let failure = result.hi.me
```

Line 2 will fail with an error.

```tsx
let failure = result.hi.me
```

`result` is technically a `string` because echo will return the string `hello world`, and `"hello world".hi.me` will throw an error.

However, by typing `v` as `any`, `result` is equally typed as `any`. This is because `echo` returns the same value. TypeScript infers the return type as the same as `v`. that is, any.

With `result` being of type `any`, you get no type safety here. TypeScript cannot catch this error. This is one of the downsides of using `any`.

OK, using `any` here is a bad idea. Let’s avoid it.

What else could you possibly do?

Another solution would be to spell out exactly what types are acceptable by the `echo` function, as follows:

```tsx
const echo = (v: string | number | object) => {
  console.log(v);
  return v;
};
```

Essentially, you represent v with a union type.

`v` can either be a `string`, a `number` or an `object`.

This works great.

Now if you go ahead to wrongly access a property on the return type of echo, you’ll get an appropriate error. For example,

```js
const result = echo("hi").hi
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-157.png)
_Property "hi" does not exist error_

You’ll get the following error: Property 'hi' does not exist on type 'string | number | object'.

This seems perfect.

We’ve represented v with a decent rage of acceptable values.

However, what if you wanted to accept more value types? You’d have to keep adding more union types.

Is there a better way to handle this? For example, by declaring some sort of variable type based on whatever the user passes to `echo` ?

For a start, let's replace the union type with an hypothetical type we’ll call `Value`:

```ts
const echo = (v: Value) => {
  console.log(v);
  return v;
};
```

Once you do this, you’ll get the following Typescript error:

```ts
Cannot find name 'Value'.ts (2304)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-158.png)
_Cannot find name "Value" error_

This is expected.

However, here’s the beauty of generics. We can go ahead to define this `Value` type as a generic—some sort of variable represented by the type of `v` passed to echo when invoked.

To complete this, we’ll use angle braces just after the `=` sign as follows:

```ts
const echo = <Value> (v: Value) => {
  console.log(v);
  return v;
};
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-159.png)
_The "Value" generic_

If you’re coding along, you’ll notice there are no more TypeScript errors. TypeScript understands this to be a generic. The Value type is a generic.

But how does TypeScript know what Value is?

Well, this is where the variable form of a generic becomes evident.

Take a look at how echo is invoked:

```ts
echo(1)
echo("hello world")
echo({})
```

The generic `Value` will take on whatever the argument type passed into echo at invocation time.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-160.png)
_The Value generic represents what the function argument type_

For example, with `echo(1)`, the type of `Value` will be the literal number `1`. For `echo("hello world")`, the type of `Value` will be the literal string `hello world`.

Note how this changes based on the type of argument passed to `echo`.

This is wonderful.

If you went ahead to perform any operations on the return type of echo, you’ll get all the type safety you’d expect—without specifying a single type but by representing the input with a **generic**, aka a variable type.

### How to constrain generics

Having learned the basics of generics, there’s one more concept to understand before we get back to leveraging TypeScript in our polymorphic component solution.

Let’s consider a variant of the echo function. Call this `echoLength`:

```js
const echoLength = <Value> (v: Value) => {
  console.log(v.length);
  return v.length;
};
```

Instead of echoing the input value v, the function echoes the length of the input value, that is `v.length`.

If you wrote this code out as is, the Typescript compiler will yell with an error:

```ts
Property 'length' does not exist on type 'Value'.ts (2339)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-161.png)
_Property "length" does not exist error_

This is quite an important error.

The `echoLength` parameter, `v`, is represented by the generic `Value` – which in fact represents the type of the argument passed to the function.

However, within the body of the function, we are accessing the `length` property of the variable parameter.

So, what’s the problem here?

The issue is, not every input will have a `length` property.

The generic `Value` as it stands represents any argument type passed by the function caller – but not every argument type will have a `length` property.

Consider the following:

```js
echoLength("hello world")
echoLength(2)
echoLength({})
```

`echoLength("hello world")` will work as expected because a `string` has a `length` property.

However, the other two examples will return undefined. Numbers and objects don’t have length properties. So the code within the function body isn’t the most type safe.

Now, how do we fix this?

We need to be able to take in a generic, but we want to specify exactly what kind of generic is valid.

In more technical terms, we need to constrain the generic accepted by this function to be limited to types that have a length property.

To accomplish this, we will leverage the `extends` keyword.

Take a look:

```ts
const echoLength = <Value extends {length: number}> (v: Value) => {
    console.log(v.length);
    return v.length;
};
```

Now, when you declare the `Value` generic, add `extends {length: number}` to denote that the generic will be constrained to types which have a length property.

If you go ahead to use `echoLength` as before, you should now get a TypeScript error when you pass in values without a length property, for example:

```js
// these will yield a typescript error
echoLength(2)
echoLength({})
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-162.png)
_Argument of type number is not assignable error_

What we’ve done here is constrain the `Value` generic to a specific mould. Yes, we want variable types. But we only want those that fit this specific mould, that is that fit a certain type signature.

Lovely!

Now that you understand these two concepts, we’ll now head back to updating our polymorphic component solution to be a lot more type safe — starting with the initial requirements we’ll set.

### Make sure the `as` prop only receives valid HTML element strings

Here’s our current solution:

```tsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

To make the next sections of this guide practical, we’ll change the name of the component from MyComponent to `Text`. That is, assume we’re building a polymorphic Text component.

Now, with your knowledge of generics, it becomes clear that we’re better off representing as with a generic type, that is a variable type based on whatever the user passes in.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-163.png)
_The as prop: a variable passed by the user when the component is rendered_

Let’s go ahead and take the first step as follows:

```jsx
export const Text = <C>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Note how the generic `C` is defined and then passed on in the type definition for the prop `as`.

However, if you wrote this seemingly perfect code, you’ll have TypeScript yelling out numerous errors with more squiggly red lines than you’d like 🤷‍♀️

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-164.png)
_The JSX generic error code block_

What’s going on here is a flaw in the [syntax for generics](https://stackoverflow.com/questions/32308370/what-is-the-syntax-for-typescript-arrow-functions-with-generics?) in `.tsx` files. There are two ways to solve this.

**1. Add a comma after the generic declaration.**

This is the syntax for declaring multiple generics. Once you do this, the TypeScript compiler clearly understands your intent and the error is banished.

```jsx
// note the comma after "C" below 👇
export const Text = <C,>({
as,
children,
}: {
as?: C;
 children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

**2. Constrain the generic.**

The second option is to constrain the generic as you see fit. For starters, you can just use the unknown type as follows:

```jsx
// note the extends keyword below 👇
export const Text = <C extends unknown>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

For now, I’ll stick to solution 2 because it’s closer to our final solution. In most cases, I use the multiple generic syntax (adding a comma).

OK, now what next?

With our current solution, we get another TypeScript error:

```ts
JSX element type 'Component' does not have any construct or call signatures.ts(2604)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-165.png)
_No construct or call error highlighted_

This is similar to the error we had when we worked with the `echoLength` function. Just like accessing the length property of an unknown variable type, the same may be said here.

Trying to render any generic type as a valid React component doesn’t make sense.

We need to constrain the generic ONLY to fit the mould of a valid React element type.

To achieve this, we’ll leverage the internal React type: `React.ElementType`, and make sure the generic is constrained to fit that type:

```jsx
// look just after the extends keyword 👇
export const Text = <C extends React.ElementType>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Note that if you’re on an older version of React, you may have to import React as follows: `**import** **React** **from** **'react'**`**.**

With this, we have no more errors!

Now, if you go ahead and use this component as follows, it’ll work just fine:

```jsx
<Text as="div">Hello Text world</Text>
```

However, if you pass an invalid `as` prop, you’ll now get an appropriate TypeScript error. Consider the example below:

```jsx
<Text as="emmanuel">Hello Text world</Text>
```

And the error thrown:

```ts
Type '"emmanuel"' is not assignable to type 'ElementType<any> | undefined'.
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-166.png)
_Type "emmanuel" is not assignable error highlighted_

This is excellent!

We now have a solution that doesn’t accept gibberish for the `as` prop and will also prevent against nasty typos, for example `divv` instead of `div`.

This is a much better developer experience.

## How to Handle Valid Component Attributes

In solving this second use case, you’ll come to appreciate how powerful generics truly are.

First, you do have to understand what we’re trying to accomplish here.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-167.png)
_Illustration showing the props: "as" and other valid attributes_

Once we receive a generic as type, we want to make sure that the remaining props passed to our component are relevant, based on the ``as prop.

So, for example, if a user passed in an `as` prop of img, we’d want href to equally be a valid prop!

To give you a sense of how we’d accomplish this, take a look at the current state of our solution:

```jsx
export const Text = <C extends React.ElementType>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

The props of this component is now represented by the object type:

```jsx
{
  as?: C;
  children: React.ReactNode;
}

```

In pseudocode, what we’d like would be the following:

```jsx
{
  as?: C;
  children: React.ReactNode;
 } & {...otherValidPropsBasedOnTheValueOfAs}
```

This requirement is enough to leave one grasping at straws. We can’t possibly write a function that determines appropriate types based on the value of `as`, and it’s not smart to list out a union type manually.

Well, what if there was a provided type from React that acted as a “function” that’ll return valid element types based on what you pass it?

Before introducing the solution, let’s have a bit of a refactor. Let’s pull out the props of the component into a separate type.

```jsx
// 👇 See TextProps pulled out below
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
}

export const Text = <C extends React.ElementType>({
  as,
  children,
}: TextProps<C>) => { // 👈 see TextProps used
  const Component = as || "span";
  return <Component>{children}</Component>;
};
```

What’s important here is to note how the generic is passed on to `TextProps<C>`. Similar to a function call in JavaScript — but with angle braces.

Now, on to the solution.

The magic wand here is to leverage the `React.ComponentPropsWithoutRef` type as shown below:

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>; // 👈 look here

export const Text = <C extends React.ElementType>({
  as,
  children,
}: TextProps<C>) => {
  const Component = as || "span";
  return <Component>{children}</Component>;
};
```

Note that we’re introducing an intersection here. Essentially, we’re saying, the type of `TextProps` is an object type containing `as` and `children`, and some other types represented by `React.ComponentPropsWithoutRef`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-168.png)
_The collection of the component props and other props based on the "as" prop_

If you read the code, it perhaps becomes apparent what’s going on here.

Based on the type of `as`, represented by the generic `C`, `React.componentPropsWithoutRef` will return valid component props that correlates with the `string` attribute passed to the as prop.

There’s one more significant point to note.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-169.png)
_Exploring the different ComponentProps type variants_

If you just started typing and rely on intellisense from your editor, you’d realise there are three variants of the `React.ComponentProps`... type.

1. `React.ComponentProps`
2. `React.ComponentPropsWithRef`
3. `React.ComponentPropsWithoutRef`

If you attempted to use the first, ComponentProps, you’d see a relevant note that reads:

> Prefer ComponentPropsWithRef, if the ref is forwarded, or ComponentPropsWithoutRef when refs are not supported.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-170.png)
_Note to prefer ComponentPropsWithRef or ComponentPropsWithoutRef_

And this is precisely what we’ve done.

For now, we will ignore the use case for supporting a ref prop and stick to ComponentPropsWithoutRef.

Now, let’s give the solution a try!

If you go ahead and use this component wrongly, for example passing a valid ``as prop with other incompatible props, you’ll get an error.

```jsx
<Text as="div" href="www.google.com">Hello Text world</Text>
```

A value of `div` is perfectly valid for the as prop, but a div should NOT have an href attribute. That’s wrong, and righty caught by TypeScript with the error: Property 'href' does not exist on type ...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-171.png)
_Property href does not exist error_

This is great! We’ve got an even better (robust) solution.

Finally, make sure to pass on other props down to the rendered element:

```tsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>; 

export const Text = <C extends React.ElementType>({
  as,
  children,
  ...restProps, // 👈 look here
}: TextProps<C>) => {
  const Component = as || "span";
	
  // see restProps passed 👇
  return <Component {...restProps}>{children}</Component>;
};
```

Let’s keep going 🙌🏼

## How to Handle Default `as` Attributes

Consider our current solution:

```jsx
export const Text = <C extends React.ElementType>({
 as,
 children,
...restProps
}: TextProps<C>) => {
 const Component = as || "span"; // 👈 look here

 return <Component {...restProps}>{children}</Component>;
};
```

Particularly pay attention to where a default element is provided if the `as` prop is omitted.

```jsx
const Component = as || "span"
```

This is properly represented in the JavaScript world, that is by implementation, if `as` is optional, it’ll default to a span.

The question is, how does TypeScript handle this case? Like when `as` isn’t passed? Are we equally passing a default type?

Well, the answer is no. But below’s a practical example.

If you went ahead to use the Text component as follows:

```jsx
<Text>Hello Text world</Text>
```

Note that we’ve passed no `as` prop here. Will TypeScript be aware of the valid props for this component?

Let’s go ahead and add an href:

```jsx
<Text href="https://www.google.com">Hello Text world</Text>
```

If you go ahead and do this, you’ll get no errors.

That’s bad.

A span should not receive an href prop / attribute. While we default to a span in the implementation, TypeScript is unaware of this default implementation. Let’s fix this with a simple, generic default assignment:

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;

/**
* See default below. TS will treat the rendered element as a
span and provide typings accordingly
*/
export const Text = <C extends React.ElementType = "span">({
  as,
  children,
...restProps
}: TextProps<C>) => {
  const Component = as || "span";
  return <Component {...restProps}>{children}</Component>;
};
```

The important bit is highlighted below:

```jsx
<C extends React.ElementType = "span">
```

And voilà! The previous example we had should now throw an error, that is when you pass href to the Text component without an `as` prop.

The error should read: Property 'href' does not exist on type ...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-172.png)
_The href is not assignable ... error (as expected)_

## The Component Should Be Reusable with its Props

Our current solution is much better than where we started. Give yourself a pat on the back for making it this far. However, it only gets more interesting from here.

The use case to cater to in this section is very applicable in the real world. There’s a high chance that if you’re building some sort of component, then that component will also take in some specific props, that are unique to the component.

Our current solution takes into consideration the `as`, children, and other component props based on the `as` prop. But what if we wanted this component to handle its own props?

Let’s make this practical.

We will have the `Text` component receive a `color` prop. The `color` here will be any of the rainbow colours, or `black`.

We will go ahead and represent this as follows:

```jsx
type Rainbow =
| "red"
| "orange"
| "yellow"
| "green"
| "blue"
| "indigo"
| "violet";
```

Next, we must define the `color` prop in the `TextProps` object as follows:

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 look here
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;
```

Before we go ahead, let’s have a bit of a refactor. 

Let's represent the actual `props` of the `Text` component by a `Props` object, and specifically type only props specific to our component in the `TextProps` object.

This will become clear, as you’ll see below:

```jsx
// new "Props" type
type Props <C extends React.ElementType> = TextProps<C>

export const Text = <C extends React.ElementType = "span">({
as,
children,
...restProps,
}: Props<C>) => {
const Component = as || "span";
return <Component {...restProps}>{children}</Component>;
};

```

Now let’s clean up `TextProps`:

```jsx
// before 
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 look here
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;

// after
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};
```

Now, `TextProps` should just contain props specific to our `Text` component: `as` and `color`.

We must now update the definition for `Props` to include the types we’ve removed from `TextProps`, that is `children` and `React.ComponentPropsWithoutRef<C>`.

For the `children` prop, we’ll take advantage of the `React.PropsWithChildren` prop.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-141.png)
_The PropsWithChildren type injects the children prop_

The way `PropsWithChildren` works is easy to reason about. You pass it your component props, and it’ll inject the children props definition for you.

Let’s leverage that below:

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>>
```

Note how we use the angle braces.

This is the syntax for passing on generics. Essentially, the `React.PropsWithChildren` accepts your component props as a generic and augments it with the children prop. Sweet!

For `React.ComponentPropsWithoutRef<C>`, we’ll just go ahead and leverage an intersection type here:

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>
```

And here’s the full current solution:

```jsx
type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};

type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>

export const Text = <C extends React.ElementType = "span">({
  as,
  children,
}: Props<C>) => {
  const Component = as || "span";
  return <Component> {children} </Component>;
};
```

I know these can feel like a lot, but take a closer look, and it’ll all make sense. It’s really just putting together everything you’ve learnt so far. Nothing should be particularly new.

All clear? Now, you’re becoming something of a pro!

Having done this necessary refactor, we can now continue with our solution. What we have now actually works. We’ve explicitly typed the color prop, and you may go ahead to use it as follows:

```jsx
<Text color="violet">Hello world</Text>
```

There’s just one thing I’m not particularly comfortable with.

`color` turns out to also be a valid attribute for numerous `HTML` tags. This was the case pre-HTML5. So, if we removed `color` from our type definition, it’ll be accepted as any valid string.

See below:

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  // remove color from the definition here
};
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-142.png)
_Removing the color type definition_

Now, if you go ahead to use `Text` as before, it’s equally valid:

```jsx
<Text color="violet">Hello world</Text>
```

The only difference here is how it is typed. `color` is now represented by the following definition `color?: string | undefined`:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-143.png)
_The default color type_

Again, this is NOT a definition we wrote in our types!

This is a default HTML typing where color is a valid attribute for most HTML elements. See this [stackoverflow question](https://stackoverflow.com/questions/67142430/why-color-appears-as-html-attribute-on-a-div) for some more context.

Now, there are two ways to go here.

Firstly, you can keep our initial solution where we explicitly declared the color prop:

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 look here
};
```

Secondly, you can go ahead and arguably provide some more safety. To achieve this, you must realise where the previous default color definition came from.

It came from the definition `React.ComponentPropsWithoutRef<C>` – this is what adds other props based on what the type of `as` is.

So, what we can do here is to explicitly remove any definition that exists in our component types from `React.ComponentPropsWithoutRef<C>`.

This can be tough to understand before you see it in action, so let’s take it step by step.

`React.ComponentPropsWithoutRef<C>`, as stated earlier, contains every other valid props based on the type of `as`, for example `href`, `color`, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-144.png)
_The ComponentPropsWithoutRef type_

Where these types all have their definition, like `color?: string | undefined` and so on.

It is possible that some values that exist in `React.ComponentPropsWithoutRef<C>` also exist in our component props type definition.

In our case, `color` exists in both!

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-145.png)
_ComponentPropsWithoutRef and TextProps_

Instead of relying on our color definition to override what’s coming from `React.ComponentPropsWithoutRef<C>`, we will explicitly remove any type that also exists in our component types definition.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-146.png)
_Removing existing props from ComponentPropsWithoutRef_

So, if any type exists in our component types definition, we will explicitly remove it from `React.ComponentPropsWithoutRef<C>`.

How do we do this?

Well, here’s what we had before:

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>
```

Instead of just having an intersection type where we just add everything that comes from React.ComponentPropsWithoutRef<C>, we will be more selective. We will use the Omit and keyof TypeScript utility types to perform some TS magic.

Take a look:

```jsx
// before 
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>

// after
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> &   
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

The important bit is this:

```jsx
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

If you don’t know how `Omit` and `keyof` work, below’s a quick summary.

`Omit` takes in two generics. The first is an object type, and the second a union of types you’d like to “omit” from the object type.

Here’s my favourite example. Consider a Vowel object type as follows:

```jsx
type Vowels = {
  a: 'a',
  e: 'e',
  i: 'i',
  o: 'o',
  u: 'u'
}
```

This is an object type of key and value.

What if I wanted to derive a new type from `Vowels` called `VowelsInOhans`?

Well, I do know that the name Ohans contains two vowels `o` and `a`.

Instead of manually declaring these:

```jsx
type VowelsInOhans = {
  a: 'a',
  o: 'o'
}
```

I can go ahead to leverage `Omit` as follows:

```jsx
type VowelsInOhans = Omit<Vowels, 'e' | 'i' | 'u'>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-147.png)
_The VowelsInOhans type using Omit_

`Omit` will “omit” the e, i, and u keys from the object type Vowels.

On the other hand, `keyof` works as you would imagine. Think of `Object.keys` in JavaScript.

Given an object type, `keyof` will return a union type of the keys of the object. Phew! That’s a mouth full.

Here’s an example:

```jsx
type Vowels = {
  a: 'a',
  e: 'e',
  i: 'i',
  o: 'o',
  u: 'u'
}

type Vowel = keyof Vowels 
```

Now, Vowel will be a union type of the keys of Vowels, that is:

```jsx
type Vowel = 'a' | 'e' | 'i' | 'o' | 'u'

```

If you put these together and take a second look at our solution, it’ll all come together nicely:

```tsx
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

`keyof TextProps<C>` returns a union type of the keys of our component props. This is in turn passed to `Omit` to omit them from `React.ComponentPropsWithoutRef<C>`.

Sweet! 🕺

For completeness, let’s go ahead and actually pass the color prop down to the rendered element:

```tsx
xport const Text = <C extends React.ElementType = "span">({
  as,
  color, // 👈 look here
  children,
  ...restProps
}: Props<C>) => {
  const Component = as || "span";
	
  // 👇 compose an inline style object
  const style = color ? { style: { color } } : {};
	
  // 👇 pass the inline style to the rendered element
  return (
    <Component {...restProps} {...style}>
      {children}
    </Component>
  );
};
```

## How to Create a Reusable Utility for Polymorphic Types

You must be proud of how far you’ve come if you’ve been following along.

We’ve got a solution that works — well.

But now, let’s take it one step further.

The solution we have works great for our Text component. But what if you’d rather have a solution you can reuse on any component of your choosing?

This way, you can have a reusable solution for every use case.

How does that sound? Lovely, I bet!

Let’s get started.

First, here’s the current complete solution with no annotations:

```tsx
type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};

type Props<C extends React.ElementType> = React.PropsWithChildren<
  TextProps<C>
> &
  Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;

export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
  ...restProps
}: Props<C>) => {
  const Component = as || "span";

  const style = color ? { style: { color } } : {};

  return (
    <Component {...restProps} {...style}>
      {children}
    </Component>
  );
};
```

Succinct and practical.

If we made this reusable, then it has to work for any component. This means removing the hardcoded TextProps and representing that with a generic — so anyone can pass in whatever component props they need.

Currently, we represent our component props with the definition Props<C>. Where C represents the element type passed for the as prop.

We will now change that to:

```tsx
// before
Props<C>

// after 
PolymorphicProps<C, TextProps>
```

`PolymorphicProps` represents the utility type we will write shortly. But note that this accepts two generic types. The second being the component props in question, that is `TextProps`.

Let’s go ahead and define the `PolymorphicProps` type:

```tsx
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = {} // 👈 empty object for now 
```

The definition above should be understandable. `C` represents the element type passed in `as` and `Props` the actual component props, for example `TextProps`.

Before going ahead, let’s actually split the `TextProps` we had before into the following:

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type TextProps = { color?: Rainbow | "black" };
```

So, we’ve separated the `AsProp` from the `TextProps`. To be fair, they represent two different things. This is a nicer representation.

Now, let’s change the PolymorphicComponentProp utility definition to include the `as` prop, component props, and children prop as we’ve done in the past:

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>>
```

I’m sure you understand what’s going on here.

We now have an intersection type of `Props` (representing the component props) and AsProp representing the `as` prop, and these all passed into `PropsWithChildren` to add the children prop definition.

Excellent!

Now, we need to include the bit where we add the `React.ComponentPropsWithoutRef<C>` definition. However, we must remember to omit props that exist in our component definition.

Let’s come up with a robust solution.

Write out a new type that just comprises the props we’d like to omit. Namely, the keys of the `AsProp` and the component props as well.

```tsx
type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);
```

Remember the `keyof` utility type?

PropsToOmit will now comprise a union type of the props we want to omit, which is, every prop of our component represented by `P` and the actual polymorphic prop as represented by `AsProps`.

I’m glad you’re still following.

Now, let’s put this all together nicely in the `PolymorphicComponentProp` definition:

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

// before 
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>>

// after
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, 
   PropsToOmit<C, Props>>;
```

This basically omits the right types from `React.componentPropsWithoutRef`. Do you still remember how [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys) works?

Simple as it may seem, you now have a solution you can reuse on multiple components across different projects!

Here’s the complete implementation:

```tsx
type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;
```

Now we can go ahead and use `PolymorphicComponentProp` on our `Text` component as follows:

```tsx
export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
  // look here 👇
}: PolymorphicComponentProp<C, TextProps>) => {
  const Component = as || "span";
  const style = color ? { style: { color } } : {};
  return <Component {...style}>{children}</Component>;
};
```

How nice!

Now if you build another component, you can go ahead and type it like this:

```tsx
PolymorphicComponentProp<C, MyNewComponentProps>
```

Do you hear that sound? That’s the sound of victory — you’ve come so far!

## The Component Should Support refs

Do you remember every reference to `React.ComponentPropsWithoutRef`so far? 😅

Component props …. _without_ ref. Well, now’s the time to put the ref in it!

This is the final and most complex part of our solution. I’ll need you to be patient here, but I’ll also do my best to explain every step in detail.

Let’s delve in.

First things first, do you remember how refs in React work?

The most important concept here is the fact that you just don’t pass `ref` as a prop and expect it to be passed down into your component like every other prop.

The recommended way to handle refs in your functional components is to use the `forwardRef` function.

Let’s start off on a practical note.

If you go ahead and pass a `ref` to our `Text` component now, you’ll get an error that reads Property `'ref'` does not exist on type ...

```tsx
// Create the ref object 
const divRef = useRef<HTMLDivElement | null>(null);
... 
// Pass the ref to the rendered Text component
<Text as="div" ref={divRef}>
  Hello Text world
</Text>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-148.png)
_Property ref does not exist error_

This is expected.

Our first shot at supporting refs will be to use `forwardRef` in the `Text` component as shown below:

```tsx
// before 
export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
}: PolymorphicComponentProp<C, TextProps>) => {
  ...
};


// after
import React from "react";

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">({
    as,
    color,
    children,
  }: PolymorphicComponentProp<C, TextProps>) => {
    ...
  }
);
```

This is essentially just wrapping the previous code in `React.forwardRef`, that’s all.

Now, `React.forwardRef` has the following signature:

```jsx
React.forwardRef((props, ref) ... )
```

Essentially, the second argument received is the `ref` object.

Let’s go ahead and handle that:

```tsx
type PolymorphicRef<C extends React.ElementType> = unknown;

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    // 👇 look here
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);
```

What we’ve done here is added the second argument ref and declared its type as PolymorphicRef.

A type that just points to `unknown` for now.

Also note that PolymorphicRef takes in the generic `C`. This is similar to previous solutions. The ref object for a div differs from that of a `span`. So, we need to take into consideration the element type passed in the as prop.

Let’s now point our attention to the `PolymorphicRef` type.

I need you to think with me.

How can we get the `ref` object type based on the as prop?

Let me give you a clue: `React.ComponentPropsWithRef` !

Note that this says _with_ ref. Not _without_ ref.

Essentially, if this were a bundle of keys (which in fact it is), it’ll include all the relevant component props based on the element type, _plus_ the ref object.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-149.png)
_The ComponentPropsWithRef type_

So now, if we know this object type contains the `ref` key, we may as well get that ref type by doing the following:

```tsx
// before 
type PolymorphicRef<C extends React.ElementType> = unknown;

// after 
type PolymorphicRef<C extends React.ElementType> =
  React.ComponentPropsWithRef<C>["ref"];
```

Essentially, `React.ComponentPropsWithRef<C>` returns an object type, for example:

```js
{
  ref: SomeRefDefinition, 
  // ... other keys, 
  color: string 
  href: string 
  // ... etc
}
```

To pick out just the ref type, we then do this:

```jsx
React.ComponentPropsWithRef<C>["ref"];
```

Note that the syntax is similar to the property accessor syntax in JavaScript, that is ["ref"]. In TypeScript, we call this **Type indexing**.

**_Quick quiz_**_: Do you know why using “Pick” may not work well here, for example_ Pick<React.ComponentPropsWithRef<C>, "ref">_?_

You can [tweet me](https://twitter.com/ohansemmanuel) your answers.

Now that we’ve got the `ref` prop typed, we can go ahead and pass that down to the rendered element:

```tsx
export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    ref?: PolymorphicRef<C>
  ) => {
    //...
    
    return (
      <Component {...style} ref={ref}> // 👈 look here
        {children}
      </Component>
    );
  }
);
```

We’ve made decent progress! In fact, if you go ahead and check the usage of Text like we did before, there’ll be no more errors:

```tsx
// create the ref object 
const divRef = useRef<HTMLDivElement | null>(null);
... 
// pass ref to the rendered Text component
<Text as="div" ref={divRef}>
  Hello Text world
</Text>
```

But our solution still isn’t as strongly typed as I’d like.

Let’s go ahead and change the ref passed to the Text as shown below:

```tsx
// create a "button" ref object 
const buttonRef = useRef<HTMLButtonElement | null>(null);
... 
// pass a button ref to a "div". NB: as = "div"
<Text as="div" ref={buttonRef}>
  Hello Text world
</Text>
```

Typescript should throw an error here, but it doesn’t. We’re creating a “button” ref, but we're passing that to a `div` element.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-150.png)
_No error thrown when a wrong element ref is passed_

If you take a look at the exact type, `ref` it looks like this:

```tsx
React.RefAttributes<unknown>.ref?: React.Ref<unknown>
```

Do you see the `unknown` in there? That’s the sign of weak typing. We should ideally have `HTMLDivElement` in there, explicitly defining the ref object as a `div` element ref.

We’ve got work to do.

Firstly, the types for the other props of the `Text` component still reference the `PolymorphicComponentProp` type.

Let’s change this to a new type called `PolymorphicComponentPropWithRef`. You guessed right. This will just be a union of `PolymorphicComponentProp` and the ref prop.

Here it is:

```tsx
type PolymorphicComponentPropWithRef<
  C extends React.ElementType,
  Props = {}
> = PolymorphicComponentProp<C, Props> & 
{ ref?: PolymorphicRef<C> };
```

Note that this is just a union of the previous `PolymorphicComponentProp` and `{ ref?: PolymorphicRef<C> }`.

Now we need to change the props of the component to reference the new `PolymorphicComponentPropWithRef` type:

```tsx
// before
type TextProps = { color?: Rainbow | "black" };

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);


// now 
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: TextProps<C>, // 👈 look here
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);
```

Now, we’ve updated `TextProps` to reference `PolymorphicComponentPropWithRef` and that’s now passed as the props for the Text component.

Lovely!

There’s only one final thing to do now. We will provide a type annotation for the `Text` component. It goes similar to:

```tsx
export const Text : TextComponent = ...
```

Where `TextComponent` is the type annotation we’ll write. Here it is:

```tsx
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;
```

This is essentially a functional component that takes in `TextProps` and returns `React.ReactElement | null`.

Where `TextProps` is as defined earlier:

```tsx
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;
```

With this, we now have a complete solution.

I’m going to share the complete solution now. It may seem daunting at first, but remember we’ve worked line by line through everything you see here. Read it with that confidence.

```tsx
import React from "react";

type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

// This is the first reusable type utility we built
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;

// This is a new type utitlity with ref!
type PolymorphicComponentPropWithRef<
  C extends React.ElementType,
  Props = {}
> = PolymorphicComponentProp<C, Props> & { ref?: PolymorphicRef<C> };

// This is the type for the "ref" only
type PolymorphicRef<C extends React.ElementType> =
  React.ComponentPropsWithRef<C>["ref"];

/**
* This is the updated component props using PolymorphicComponentPropWithRef
*/
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;

/**
* This is the type used in the type annotation for the component
*/
type TextComponent = <C extends React.ElementType = "span">(
  props: TextProps<C>
) => React.ReactElement | null;

export const Text: TextComponent = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: TextProps<C>,
    ref?: PolymorphicRef<C>
  ) => {
    const Component = as || "span";

    const style = color ? { style: { color } } : {};

    return (
      <Component {...style} ref={ref}>
        {children}
      </Component>
    );
  }
);
```

And there you go!

You have successfully built a robust solution for handling Polymorphic components in React.

I know it wasn’t an easy ride, but you did it.

## Conclusion and Next Steps

Thanks for following along. If you're keen to keep improving your TypeScript, you can [download the accompanying free PDF](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/stprc-meta-3.png)
_[Download the free PDF](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)_

I'll also send you an email series of 5 TypeScript secrets that'll get you thinking (and writing) like a pro.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/5-TS-secrets@3x.png)
_[Download the free ebook](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components) to automatically get my 5-day Typescript secrets newsletter_

You can [get it here](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

Thanks for reading!



  

