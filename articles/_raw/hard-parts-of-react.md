---
title: How to Learn the Hard Parts of React – and Tips to Conquer Them
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-02-26T21:07:53.000Z'
originalURL: https://freecodecamp.org/news/hard-parts-of-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Article-Cover.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: "Have you started learning React, only to face bugs that made you contemplate\
  \ a career in goat herding? Don't worry – we've all been there. \nIn this guide,\
  \ you'll join me on a quest through the quirky wonders of React. I'll help you navigate\
  \ the perpl..."
---

Have you started learning React, only to face bugs that made you contemplate a career in goat herding? Don't worry – we've all been there. 

In this guide, you'll join me on a quest through the quirky wonders of React. I'll help you navigate the perplexing moments, ensuring you never have to ask yourself, "What’s up with React?"

Whether you're a seasoned React adventurer or unearthing the mysteries of virtual DOMs, fear not. I'm here to share the tales of my early struggles, demystify the enigmatic bugs, and pave the way for a smoother journey.

### Prerequisites

* Fundamentals of HTML and CSS
* Fundamentals of ES6 JavaScript and React

## **What We'll Cover:**

1. [Quick Recap of React Fundamentals](#heading-what-well-cover)  
– [Components: The Web Building Blocks](#heading-components-the-web-building-blocks)  
– [JSX: Where HTML Meets JavaScript](#heading-jsx-where-html-meets-javascript)  
– [State and Props: The Dynamic Duo](#heading-state-and-props-the-dynamic-duo)
2. [The Good, the Bad, and the Challenging Parts of React](#the-good-the-bad-and-the-challenging-parts-of-react)  
– [The Good Parts of React](#heading-the-good-parts-of-react)  
– [The Bad Parts of React](#heading-the-bad-parts-of-react)  
– [The Challenging Parts of React](#heading-the-challenging-parts-of-react)  
		– [Key Prop Mishaps](#heading-key-prop-mishaps)  
		– [Mutating States Directly](#heading-mutating-states-directly)  
		– [Mysterious Bugs with Conditional Rendering](#heading-mysterious-bugs-with-conditional-rendering)  
		– [Ignoring Dependency Arrays in React Hooks](#heading-ignoring-dependency-arrays-in-react-hooks)  
		– [Neglecting Optional Chaining for API Data](#heading-neglecting-optional-chaining-for-api-data)  
		– [Ignoring React Fragments for Grouping JSX Elements](#heading-ignoring-react-fragments-for-grouping-jsx-elements)
3. [Opinionated Approaches to React](#heading-opinionated-approaches-to-react)
4. [Wrapping Up the Quirky Journey with React](#heading-wrapping-up-the-quirky-journey-with-react)

## Quick Recap of React Fundamentals

The React library revolves around 3 building blocks: Components, JSX, and State & Props.

### Components: The Web Building Blocks

Imagine components as the LEGO bricks of your user interface—a single, reusable piece that contributes to the grand structure. They encapsulate functionality, styling, and behavior, making your UI both modular and scalable. 

From a simple button to an elaborate sidebar, components are the heart and soul of React development.

### JSX: Where HTML Meets JavaScript

JSX, or JavaScript XML, may seem like an odd fusion of HTML and JavaScript at first, but it’s quite straightforward. It's the secret sauce that makes React's syntax so expressive and dynamic. 

With JSX, you write your UI components using a syntax that resembles HTML, but underneath, it's pure JavaScript.

### State and Props: The Dynamic Duo

The dynamic duo of state and props bring React pages to life as they add interactivity to your web applications.

#### State: Granting Memory to Components

State provides memory to components, allowing them to remember past events and alter their behavior over time. It's the key to making your UI responsive and dynamic. 

Picture a form that remembers the user's input or a counter that increments with each click. That's the magic of state.

#### Props: Enabling Communication

Props (short for properties) facilitate communication between components. They allow parent components to pass data down to their children, creating a seamless flow of information. 

Think of props as messengers, ensuring that each component knows its role and receives the necessary information to perform it.

## The Good, the Bad, and the Puzzling Parts of React

Before we delve into the puzzling aspects of React, it's essential to shine a spotlight on the treasures that make React a true hero in your arsenal.

### The Good Parts of React

#### Virtual DOM and its Advantages

The virtual DOM is a revolutionary concept that gives React its speed and efficiency. 

When changes occur in your app, React doesn't immediately update the actual DOM. Instead, it works with a lightweight copy, the Virtual DOM, making minimal, lightning-fast adjustments. This not only optimizes performance but also provides a smoother user experience.

```js
ReactDOM.createRoot(document.getElementById("root")).render(
    <App />
 );
```

This process leverages [React's diffing algorithm](https://legacy.reactjs.org/docs/reconciliation.html) in the Virtual DOM. It identifies the minimal set of changes needed in the actual DOM to reflect the updated state.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/00--Explaing-how-react-updates-the-UI-using-the-virtual-DOM.png)
_Explaining how React updates the UI using the virtual DOM_

#### Reusable Components

In React, the guiding principle is reusability. Components, the fundamental building blocks we discussed above, can be crafted and employed across your application. This not only fosters a modular and organized code structure but also frees you from the burden of reinventing the wheel.

```js
// Reusable Button Component
const Button = ({ label, onClick }) => (
  <button onClick={onClick}>{label}</button>
);

// Usage
<Button label="Click me" onClick={() => console.log("Button Clicked")} />
```

#### One-way Data Binding for a Predictable Flow

React enforces a unidirectional data flow, ensuring predictability and maintainability. 

Parent components convey data down to their children through props, and any modifications are overseen by the parent component. This one-way street prevents the chaos with 2-way data binding seen in other frameworks.

```js
const ParentComponent = () => {
  const [data, setData] = useState("Hello from Parent!");

  return <ChildComponent data={data} />;
};

const ChildComponent = ({ data }) => <div>{data}</div>;
```

### The Bad Parts of React

There are some parts of React that aren't ideal, though. Let's go through them briefly now so you can be aware of them.

#### Steep Learning Curve for Beginners

Starting with React can be tough, especially if you're new to web development. Concepts like JSX, components, and state management might seem like a maze. But don't worry! With some practice and patience, it gets easier, and React becomes more familiar.

#### JSX Might Puzzle You at First

JSX, the special mix of HTML and JavaScript, can be a bit confusing at the beginning. It's like learning a new language that blends the two. But as you get the hang of it, you'll see how it makes your code shorter and clearer.

#### State Management Challenges

Using state in React is powerful, but it can also be tricky. Handling state across lots of different pieces, especially in big projects, can create complex setups and potential problems. Luckily, tools like [Redux](https://redux.js.org/) exist to help manage this complexity.

## The Challenging Parts of React

### Key Prop Mishaps

When building your applications, you may often have repeating elements which show similar information or share the same styles. The logical step would be to loop over them to create a list of elements.

```js
function ListComponent() {
  const people = [{ name: "Mitchelle" }, { name: "July" }, { name: "David" }];
  return (
    <ul>
      {/ Looping over the people array to create list items /}
      {people.map((person) => (
        <li>{person.name}</li>
      ))}
    </ul>
  );
}
```

Everything seems fine until you notice a warning in your console or, worse, strange behaviour in how your list renders.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/02--The-console-an-error-due-to-missing-key-prop.png)
_The console an error due to missing key prop_

React uses keys to update and reorder elements in a list. When you forget to provide a key prop or if the keys are not unique, React gets a bit lost. It's like trying to keep track of items in the array without any specific identifiers – things get mixed up, and you might end up with unexpected bugs in your UI.

#### How to solve it

The first instinct for many developers when faced with creating dynamic lists is to use the index property as the key. It seems like a convenient solution, as the index provides a unique identifier for each element in the array – but it isn’t the best approach for the following reasons:

* **Non-Persistent**: If the order or number of items changes, React may get confused. For example, if an item is added or removed from the beginning of the list, all the subsequent indices change, causing potential re-rendering issues.
* **Array Mutations**: Operations like sorting or filtering can alter the order of items, breaking the association between the index and the actual item.
* **Performance Concerns**: React relies on keys for efficient updates. Using the index as a key might impact performance when dealing with large lists or frequent updates.

Some of the better alternatives include:

* **Use a Unique ID**: If each item in your array has a unique identifier, such as an `id` property, use that as the key.

```js
{people.map((person) => (
  <li key={person.id}>{person.name}</li>
))}
```

* Generate a Unique Key: In cases where items lack a natural unique identifier, consider using a function like `crypto.randomUUID()` to generate a unique key.

```js

function ListComponent() {
  const people = [
    { name: "Mitchelle", age: 25, occupation: "Engineer" },
    { name: "July", age: 30, occupation: "Doctor" },
    { name: "David", age: 35, occupation: "Artist" }
  ];

  // Generate unique IDs for each person before rendering
  const peopleWithIds = people.map(person => ({
    ...person,
    id: crypto.randomUUID(),
  }));

  return (
    <ul>
      {/* Looping over the people array to create list items */}
      {peopleWithIds.map((person) => (
        <li key={person.id}>{person.name}</li>
      ))}
    </ul>
  );
}
```

By choosing one of these alternatives, you provide React with stable and unique keys, helping it manage and update your dynamic lists,

**Note**: You may be thinking “If `crypto.randomUUID` generates a unique ID, (`Math.random()` * some big number) would work the same, right”?

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Nope.gif)
_Nope gif_

`Math.random()` could also suffice as a key, but it's a bad idea because the generated keys won't be stable across re-renders, leading to potential performance issues and rendering inconsistencies.

### Mutating States Directly

Imagine you're working on a component that manages an array of names. Rather than using the appropriate setter method to update the state, you decide to directly mutate the state.

```js
const MutableStateComponent = () => {
  const [names, setNames] = useState(["David", "John", "Steph", "Anthony"]);

  const removeLastName = () => {
    console.log(names);
    // Direct mutation of state using pop()
    names.pop();
    setNames(names); // This won't trigger a re-render
  };

  return (
    <div>
      <p>Names: {names.join(", ")}</p>
      <button onClick={removeLastName}>Remove Last Name</button>
    </div>
  );
};
```

To your surprise, the UI doesn't update as expected, and you find yourself stuck in a scenario where the list of names seems frozen. Make no mistake, the array is getting updated as seen below:

![Image](https://lh7-us.googleusercontent.com/yey1I5L7W43d8vcNl7kEUZaRHGZw90xZfviK3rhfFHiqwXv3gsCjHqcs9nhgdWoQlbPEGAj2A_7qHcoeRI9xPtsD0JCiPJdzT4MNRrQ91GfUjdwvW4hmlHGE_LtdG49FzO1buO0yT9tzMRtO95MgvYI)
_Array getting mutated with UI being updated_

#### What's the Problem?

React relies on an immutable state for efficient updates, and when you bypass this mechanism, it disrupts the unidirectional data flow. 

In this case, using `pop()` mutates the original array in place, and React loses track of the changes. This leads to an inaccurate rendering of the component.

#### How to Solve it

To ensure your component behaves as expected and follows React's principles, always use the setter function (`setNames`) to update the state.

```js
const MutableStateComponent = () => {
  const [names, setNames] = useState(["David", "John", "Steph", "Anthony"]);

  const removeLastName = () => {
    // Use setNames to update state
    setNames((prevNames) => prevNames.slice(0, -1));
    console.log(names);
  };

  return (
    <div>
      <p>Names: {names.join(", ")}</p>
      <button onClick={removeLastName}>Remove Last Name</button>
    </div>
  );
};
```

By using `setNames` and creating a new array with the desired changes (in this case, using `slice` to remove the last element), you ensure that React can accurately track and update the state, resulting in the expected UI behavior.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/09--Result-of-Mutating-States-with-the-correct-method.gif)
_Result of mutating states with the correct method_

### Mysterious Bugs with Conditional Rendering

Conditional rendering, while powerful, can introduce subtle bugs when not handled with care. Understanding common pitfalls, particularly those related to truthy and falsy evaluations, is crucial for preventing mysterious rendering behaviour.

Consider the following example:

```js
const IncorrectConditionalComponent = ({ showContent }) => (
  {showContent && <div>Show me if true!</div>}
);
```

#### The Bug: Unexpected Rendering with Falsy Values

In this code snippet, if `showContent` happens to be a falsy value, such as `0`, the component will render an unexpected result. Instead of gracefully not rendering the content, it will display `0` on the screen due to the direct inclusion of curly braces.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Gotcha.gif)
_I gotcha gif_

#### What's the Problem?

The issue lies in the mismanagement of truthy and falsy values. The direct use of curly braces creates an object wrapper (`[object Object]`), causing the component to render whatever value is present, even if it's falsy.

#### How to Solve it

To catch rendering bugs related to truthy and falsy values, use a more explicit conditional check.

```js
const CorrectConditionalComponent = ({ showContent }) => (
  showContent ? <div>Show me if true!</div> : null
);
```

In this corrected version, the ternary operator ensures a clear check for truthiness, preventing unexpected rendering issues. By explicitly handling truthy and falsy values, you build robust components that behave predictably in various scenarios.

### Ignoring Dependency Arrays in React Hooks

Imagine working on a component that relies on an effect to perform some logic when a certain state, let's say `count`, changes. But even though you're incrementing the count, the effect doesn't seem to run, and you're left wondering why your logic isn't taking effect.

```js
const Counter = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
   
    setCount((count) => count + 1);
  };

  useEffect(() => {
    console.log("The current count value is ", count);
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
};
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/03--testing-the-count-component-without-fixing-the-useEffect-dependency-array.gif)
_Testing the count component without fixing the useEffect dependency array_

#### What's the Problem?

The issue lies in neglecting the dependency array in your `useEffect`. When you omit the dependencies, React might not recognize that the effect is tied to a specific piece of state, leading to stale data and unexpected behavior.

#### How to Solve it

To get your effect back on track, include the relevant dependencies in the dependency array. It's like setting up triggers – you're telling React, "Hey, run this effect whenever these specific pieces of data change."

```js
useEffect(() => {
    console.log("The current count value is ", count);
  }, [count]);
```

Which now fires the `useEffect` hook:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/04--testing-the-count-component-after-fixing-the-useEffect-dependency-array.gif)
_Testing the count component after fixing the useEffect dependency array_

### Neglecting Optional Chaining for API Data

You're working on a component that displays user data fetched from an API. Everything seems fine until you encounter an unexpected runtime error. The culprit? A missing optional chaining operator.

#### What's the Problem?

API responses can be unpredictable, and not all data structures match your expectations. Neglecting optional chaining, especially when accessing deeply nested properties (looking at you Strapi response data 👀) can lead to runtime errors if a property is undefined.

#### How to Solve it

To safeguard your component from unexpected errors, incorporate optional chaining (`?.`) when accessing nested properties in API data.

As an example, say you want to read a deeply nested property (label) from this data:

```js
const data = {
    id: 1,
    title: "First Item",
    content: "Content for the first item",
    category: {
      id: 101,
      name: "Category A",
      description: "Description of Category A",
      tags: [
        {
          id: 1001,
          label: "Tag 1",
        },
        {
          id: 1002,
          label: "Tag 2",
        },
      ],
    },
    author: {
      id: 201,
      name: "John Doe",
      email: "john.doe@example.com",
    },
  };
```

The correct way would be to use optional chaining to retrieve that data:

```js
 const firstLabel = data?.category?.tags?.[0]?.label;
```

Rather than accessing those properties directly:

```js
const firstLabel = data.category.tags[0].label;
```

This prevents you from seeing a white screen error and a flooded console if the data structure changes. It's like putting on a safety net – if a property is missing, your app won't come crashing down like so:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/05--Error-occuring-when-optional-chaining-isn-t-applied.png)
_Error occurring when optional chaining isn't applied_

### Ignoring React Fragments for Grouping JSX Elements

When working with React components, you may encounter a scenario where you want to return multiple JSX elements from a function, only to be met with a syntax error.

#### What's the Problem?

This is due to a limitation in JavaScript, as it doesn't allow the return of adjacent elements without a common parent.

Consider the following problematic code:

```js
function User() {
  return <div> David Jaja</div>
         <div>Twitter: https://twitter.com/JajaDavid8</div>;
}
```

This code results in an error: “Adjacent JSX elements must be wrapped in an enclosing tag.”

![Image](https://www.freecodecamp.org/news/content/images/2024/02/06--Error-occuring-when-JSX-returns-2-direct-adjacent-elements.png)
_Error occurring when JSX returns 2 direct adjacent elements_

#### How to Solve it

I know what you might be thinking—why not simply wrap the elements in a div and move on?

![Image](https://www.freecodecamp.org/news/content/images/2024/02/sponge-bob-bored.gif)
_Spongebob bored gif_

While this seems like a quick fix, it introduces a potential downside. By adding a div, you create an unnecessary parent element in the DOM. 

This additional markup, though resolving the immediate error, can lead to unintended consequences, such as affecting styles or layout, and may not align with optimal coding practices. 

And I’m sure you don’t want to end up with a "divpocalipse". 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/07--Divpocalpse.png)
_A divpocalpse_

To overcome both the syntax error and the unnecessary DOM markup, React introduced an optimized solution: React Fragments.

React Fragments are used to address the need for returning multiple JSX elements without introducing unnecessary parent elements in the DOM.

Here's how you can utilize React Fragments:

```js
import React from "react";
function User() {
  return (
    <React.Fragment>
      <div> David Jaja</div>
      <div>Twitter: https://twitter.com/JajaDavid8</div>
    </React.Fragment>
  );
}
```

Or using the shorthand syntax:

```js
function User() {
  return (
    <>
      <div> David Jaja</div>
      <div>Twitter: https://twitter.com/JajaDavid8</div>
    </>
  );
}

```

By using React Fragments, you maintain clean and concise JSX code without introducing unnecessary elements to the DOM, enhancing code readability.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Showing-the-DOM-tree-after-using-fragments-without-any-extra-elements.png)
_Showing the DOM tree after using fragments without any extra elements_

## Opinionated Approaches to React

I've found some handy ways to make working with React more enjoyable. Instead of strict rules, think of these as my personal choices to make code easier to read, improve how it works, and make sure it stays in good shape.

1. **Put data outside components**: Move things like lists and groups of information outside the main part of a component when possible. This helps avoid extra updates and makes it simpler to handle data without using special functions like `useCallback`.
2. **Be careful with `React.memo`**: Using `React.memo` can help your components run better, but it's not always needed. If a component changes a lot with new information, using `React.memo` might not be as helpful. Use it wisely.
3. **Create your own custom React hooks**: I also like making my own special tools with custom React hooks. It's a bit advanced, but it helps keep my code neat and organized.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/but-thats-just-my-opinion-just-what-i-think.gif)
_Just my opinion gif_

## Wrapping Up the Quirky Journey with React

React's journey is a blend of smooth sailing and bumpy rides. We've seen the strength of reusable components and virtual DOM and tackled puzzling moments like missing key props and conditional rendering bugs and so on.

As you continue your journey with React, may your code be clean, your components reusable, and your "What's Up with React?" moments turn into "Aha!" revelations. Happy coding! 🚀

### **Contact Information**

Want to connect or contact me? Feel free to hit me up on the following:

* Twitter: [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn: [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email: Jajadavidjid@gmail.com

  


  

