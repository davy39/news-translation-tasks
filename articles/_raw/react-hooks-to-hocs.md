---
title: How to Convert React Hooks into HOCs for Legacy Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-07T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-to-hocs
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/hooks-to-hoc.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Rico Kahler

  Super TL;DR: here ? https://github.com/ricokahler/hocify ? is a library that converts
  hooks into HOCs.

  Scenario: You made this beautiful custom hook and you''re happily using it in your
  new function components. You then realize that thi...'
---

By Rico Kahler

**Super TL;DR:** here ? [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify) ? is a library that converts hooks into HOCs.

Scenario: You made this beautiful [custom hook](https://reactjs.org/docs/hooks-custom.html) and you're happily using it in your new function components. You then realize that this custom hook could be used in one of your older class-based components, so you try to use it by dropping it in like so…

```js
import React from 'react';
import useCoolCustomHook from './useCoolCustomHook';

class ClassComponent extends React.Component {
  // ...
  
  render() {
    // ? spoiler alert: this doesn't work
    const coolStuff = useCoolCustomHook();

    return <div>{/* ... */}</div>
  }
}

export default ClassComponent;
```

…but then you see this error message:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-4.png)
_This is the actual error message you get when you try to use hooks within a class component._

Let's say this component is really complex and already well-tested. You'd rather not rewrite the class-based component as a function component, and you'd rather not rewrite your custom hook as a higher-order component.

What do you do in this situation?

---

**TL;DR,** I wrote a library `hocify`, that converts hooks into HOCs so they can be used in class-based components.

Check out the library here: [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify)

However, if you're curious how I got there, continue reading for the full story!

---

Hooks are great! They're the [React team's answer to many problems in React today](https://youtu.be/dpw9EHDh2bM?t=757). However, using them comes with a prerequisite:

> Hooks can only be called inside the body of a function component.

This is unfortunate because it prevents us from using newer hook-based modules in our older class-based components.

Fortunately for us, there are some clever ways around this. This article will cover how to convert hooks into HOCs so they can be used within class components.

> **Disclaimer:** The purpose of "using hooks" within class components is more for compatibility of newer hook-based modules with older class-based components. If your component is already implemented as a function, then use the hook directly. If you're writing a new component, try writing it as a function component.

## The example hook: useMousePosition

Let's start by creating a custom hook that we want to use within a class component.

The hook we'll create will capture the current mouse's `x` and `y` positions on the screen and report that back to the component.

? `useMousePosition.js`: the custom hook

```js
import { useState, useEffect } from 'react';

function useMousePosition() {
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);
  
  useEffect(() => {
    const handleMouseMove = e => {
      setX(e.clientX);
      setY(e.clientY);
    };

    document.addEventListener('mousemove', handleMouseMove);
    
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);
    
  return { x, y };
}

export default useMousePosition;
```

? `ExampleComponent.js`: example usage of the above hook

```js
import React from 'react';
import useMousePosition from './useMousePosition';

function ExampleComponent() {
  const { x, y } = useMousePosition();
    
  return <div>Current Mouse Position: ({x}, {y})</div>;
}

export default ExampleComponent;
```

[**See the demo.**](https://codesandbox.io/s/boring-babbage-959ow?fontsize=14)

We'll use this hook in the rest of the examples.

## Realization 1: You can use hooks in class components by wrapping and prop drilling.

The first step of this journey is to figure out how to get the data and effects from the hook into a class component.

Hooks can only be used in function components, so an option we have is to wrap the class component with a function component and pass in the required data as props.

```js
import React from 'react';

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Current Mouse Position: ({x}, {y})</div>;
  }
}

function WrapperComponent() {
  const { x, y } = useMousePosition();
  
  return <ClassComponent x={x} y={y} />;
}

export default WrapperComponent;
```

[**See the demo.**](https://codesandbox.io/s/hocify-example-hook-0lyjx?fontsize=14)

## Realization 2: You can write a function that takes in a component and returns a wrapped one.

The next step is to make this wrapping generic so we can apply this hook to _any_ class.

We can do this using [higher-order components (aka HOCs)](https://reactjs.org/docs/higher-order-components.html). HOCs are functions that take in a component and return another component that wraps the input component. This pattern allows us to inject props to the input component from the wrapping component.

If the returned wrapper component is implemented using a function, then we can use hooks in there!

```js
function withMousePosition(Component) {  
  function WrappedComponent(props) {
    const { x, y } = useMousePosition();
      
    return <Component x={x} y={y} {...props} />;
  }
    
  return WrappedComponent;
}

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Current Mouse Position: ({x}, {y})</div>;
  }
}

export default withMousePosition(ClassComponent);
```

[**See the demo.**](https://codesandbox.io/s/hocify-realization-2-qyu09?fontsize=14)

## Realization 3: You can write a function that takes in a hook and returns an HOC.

Can we take this idea even further?

Yes! Similar to how we wrote a function that returned a component, we can take it one step higher and write a function that takes in a hook and returns a higher-order component.

The next code block is the function `hocify` (that's HOC-ify — similar to the `stringify` or `promisify` conventions).

`hocify` is a function that takes in a hook and returns an HOC.

?  `hocify.js` 

```js
import React from 'react';

function hocify(useHook) {
  function hoc(InputComponent) {
    function WrapperComponent(props) {
      const result = useHook();
      
      return <InputComponent {...result} {...props} />
    }
      
    return WrapperComponent;
  }
    
  return hoc;
}

export default hocify;
```

? Usage in `ClassComponent.js`:

```js
import React from 'react';
import hocify from 'hocify';
import useMousePosition from './useMousePosition';

const withMousePosition = hocify(useMousePosition);

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Current Mouse Position: ({x}, {y})</div>;
  }
}

export default withMousePosition(ClassComponent);
```

[**See the demo.**](https://codesandbox.io/s/hocify-realization-3-3mmg9?fontsize=14)

> **Note:** It might be tempting to call `hocify` a "higher order hook" or some other mash-up of words but I would recommend refraining ?

## Realization 4: Wouldn't this thing be nice in a package?

Probably!

`npm install --save hocify` 

Check out the library here: [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify)

> **Last Note:** There are a few considerations in the library not mentioned here.  
> Read the docs before using.

Thanks for the read!

