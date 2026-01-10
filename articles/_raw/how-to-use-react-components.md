---
title: How to Use React Components – Props, Default Props, and PropTypes Explained
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2023-09-05T22:21:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/React-compo-2-1.jpg
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'If you''re curious about web development, you''ve probably heard the buzz
  about React.

  React is an open-source JavaScript library used for building user interfaces (UIs)
  in web applications. It has taken the web development world by storm.

  One of the k...'
---

If you're curious about web development, you've probably heard the buzz about React.

React is an open-source JavaScript library used for building user interfaces (UIs) in web applications. It has taken the web development world by storm.

One of the key concepts in React is **components.** In this tutorial, we'll explore what React components are, how to pass and render data to them using props, and how to enhance their reliability using default props and propTypes.

## What Are React Components?

Imagine you're building a digital LEGO masterpiece. Each individual LEGO brick serves a purpose, but it's only when they're combined that something truly amazing takes shape.

In a similar way, React components are like those LEGO bricks. They are the individual building blocks that come together to create a full-fledged user interface. A component can be a button, a form, a header, or any other part of the webpage that you can think of.

Think of components as reusable templates that you can place throughout your web application to construct a complete user experience.

## Why are Components Important in React?

So, why are components such a big deal in React? There are a few reasons:

### Modularity and Reusability

By breaking down your UI into components, you create a modular structure. This means you can develop, test, and maintain each piece of your app separately. Plus, once you've created a component, you can reuse it throughout your app, saving you time and effort.

### Efficiency in Development

Components encourage a more efficient development process. You can have different team members working on different components simultaneously without stepping on each other's toes. This speeds up the development process and encourages collaboration.

### Maintainability

Imagine you need to update the styling of a button that appears in multiple places in your app. With components, you only need to update the styling in one place, the button's component, and it will automatically reflect wherever it's used.

## Types of React Components

There are two main types of components in React: functional components and class components.

### How to use functional components

This is the simplest way to define components in React. They are basically JavaScript functions that take in **props** (input data) and return **JSX** (JavaScript Syntax Extension) elements.

Here's a code example to show you how they work:

```jsx
import React from 'react'; // Imports the React library.

// Define a functional component named "Button"
const Button = () => {
  return (
    <button>
      Click Me
    </button>
  );
};

export default Button; // Exports the Button component to make it accessible.
```

In this example, we've defined a component called `Button` using a JavaScript function. This component returns a button element with the text "Click Me".

### How to use class components

These are JavaScript classes that extend the **React.Component** class.  
They use ES6 classes and provide more advanced features, such as state management and lifecycle methods.

Here's a code example:

```jsx
import React, { Component } from 'react'; // Create class-based React components.

// Class component
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Increment
        </button>
      </div>
    );
  }
}

export default Counter; // Exports the Counter component to make it accessible.
```

In this example, the `Counter` is a class component that maintains a `count` in its state and updates it when the button is clicked.

### Functional components vs class components – when to use each

Looking at the above two code snippets, you can differentiate them base on a few factors.

* Syntax: functional component are less verbose and easier to read due to their concise syntax. Class components are more verbose due to the class structure and the need to bind event handlers in the constructor.
    
* State: until the introduction of [hooks](https://www.freecodecamp.org/news/full-guide-to-react-hooks/), functional components couldn't hold [State](https://www.freecodecamp.org/news/react-state/#:~:text=In%20our%20React%20app%2C%20once,similarly%20to%20regular%20JavaScript%20functions.). With hooks, you can now use the **useState** hook to manage state in functional components. Class component can hold state using the `this.state` property. State updates are done using `this.setState()`.
    
* Lifecycle: functional components don't have lifecycle methods. Hooks like **useEffect** can be used to achieve similar effects. Class components support various [Lifecycle Methods](https://www.freecodecamp.org/news/react-component-lifecycle-methods/) like `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, and so on.
    
* Performance: functional components perform better as they don't need extra work required for creating classes. Class component can be a bit slower because of the extra work required for creating classes.
    
* Recommended Use: functional components are preferred for most use cases in modern React development due to their simplicity and functional nature. Class components are still relevant for more complex scenarios that require state management and lifecycle methods (though hooks have made class components less necessary).
    

React is continually evolving, and new patterns and features might emerge. Stay updated with the latest React documentation and best practices.

## How to Pass Data to Components using Props

Props (properties) are like instructions you give to your components. They allow you to pass data from a parent component to a child component. This way, you can customize how components appear and behave.

In simple terms, props are like the parameters that you pass to a function. You can use props to customize the content and behavior of a component based on the values you provide when you use or render that component.

Here's a code example to show you how they work:

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  return <ChildComponent name="Cas" />;
};

export default ParentComponent;
```

```jsx
// ChildComponent.js
import React from 'react';

const ChildComponent = (props) => {
  return <p>Hello, {props.name}!</p>;
};

export default ChildComponent;
```

In this example, the `ParentComponent` passes the `name` prop to `ChildComponent`, which displays a personalized greeting, Hello, Cas!.

### How to render with props

Rendering with props allows you to create flexible and interactive user interfaces by passing and customizing data within your components. Once you have access to the data within the child component, you can use it to render dynamic content within the component's JSX. This means you can display different UI elements based on the values of the props.

In the `ParentComponent` used above, you can pass different values to the `name` prop to customize the displayed message.

Here's a code example:

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  return (
<div>
<ChildComponent name="Cas" />;
<ChildComponent name="Nuel" />;
<ChildComponent name="Abbey" />;
</div>
)
};

export default ParentComponent;
```

In this example, different values are provided for the `name` prop. The displayed messages will be:

* `Hello, Cas!`
    
* `Hello, Nuel!`
    
* `Hello, Abbey!`
    

### What is dynamic rendering?

Rendering with props becomes powerful when combined with JavaScript expressions. You can use props along with other variables, functions, or logic to render dynamic content. This flexibility enables you to create versatile and interactive user interfaces.

Here's a code example to show you how this works:

```jsx
import React from 'react';

const Product = (props) => {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>Price: ${props.price}</p>
      {props.isOnSale && <p>On Sale!</p>}
    </div>
  );
};

export default Product;
```

In this example, the `Product` component takes multiple props to render details about a product, including its name, price, and whether it's on sale.  
The expression `{props.isOnSale && <p>On Sale!</p>}` conditionally renders the "On Sale!" message if the `isOnSale` prop is true.

### What are default props?

In some cases, you might want to provide default values for props in case they aren't explicitly passed. This ensures your component doesn't break due to missing data.

Here's a code example:

```jsx
const ChildComponent = (props) => {
  return <p>Hello, {props.name}!</p>;
};

ChildComponent.defaultProps = {
  name: "Guest",
};
```

In this example, if a value is not provided for the `name` property, it uses its default value of "Guest".

### How to use PropTypes

To maintain the integrity of your application, you can specify the expected types for your props using propTypes.

Here's a code example:

```jsx
import PropTypes from 'prop-types';

ChildComponent.propTypes = {
  name: PropTypes.string.isRequired,
};
```

In this example, if the string is not provided for the property value, it will throw an error message.

## Conclusion

Understanding the differences between functional and class components is crucial. Functional components, with their cleaner syntax and use of hooks, are favored for most use cases. Class components remain relevant for complex scenarios demanding state management and lifecycle methods.

Components thrive on the principle of passing data via props. Props are akin to instructions, allowing customization of component content and behavior. The capability to render with props enables dynamic and personalized user interfaces. When used in conjunction with JavaScript expressions, props enable versatile and interactive UIs.

Default props and PropTypes are additional tools that enhance component reliability. Default props provide fallback values to prevent breakage due to missing data, while PropTypes enforce data type validation, bolstering application integrity.

As React continues to evolve, staying updated with the latest documentation and best practices is essential. With the knowledge of components, props, default props, and PropTypes, you're well-equipped to embark on your React journey.

Interested in learning more about React? [React for Beginners](https://www.freecodecamp.org/news/react-beginner-handbook/#howmuchjavascriptyouneedtoknowtousereact) covers nearly every aspect of React. I recommend it for a deeper insight.

If you found this guide helpful and enjoyable, please give it a like. For more insightful tutorials, follow me on [X](https://twitter.com/casweb_dev) for updates 🙏.

Enjoy your coding!
