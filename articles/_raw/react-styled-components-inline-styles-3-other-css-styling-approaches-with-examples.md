---
title: 'React Styled Components: Inline Styles + 3 Other CSS Styling Approaches (with
  examples)'
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2020-03-06T14:02:00.000Z'
originalURL: https://freecodecamp.org/news/react-styled-components-inline-styles-3-other-css-styling-approaches-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/brush-painting-color-paint-102127.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'There''s no one right way to style your React components. It all depends
  on how complex your front-end application is, and which approach you''re the most
  comfortable with.

  There are four different ways to style React application, and in this post you ...'
---

There's no one right way to style your React components. It all depends on how complex your front-end application is, and which approach you're the most comfortable with.

There are four different ways to style React application, and in this post you will learn about them all. Let’s start with inline styling.

# Inline Styling

React components are composed of JSX elements. But just because you’re not writing regular HTML elements doesn’t mean you can’t use the old inline style method. 

The only difference with JSX is that inline styles must be written as an object instead of a string.

Here is a simple example:

```javascript
import React from "react";

export default function App() {
  return (
      <h1 style={{ color: "red" }}>Hello World</h1>
  );
}
```

In the style attribute above, the first set of curly brackets will tell your JSX parser that the content between the brackets is JavaScript (and not a string). The second set of curly bracket will initialize a JavaScript object.

Style property names that have more than one word are written in camelCase instead of using the traditional hyphenated style. For example, the usual `text-align` property must be written as `textAlign` in JSX:

```javascript
import React from "react";

export default function App() {
  return (
      <h1 style={{ textAlign: "center" }}>Hello World</h1>
  );
}
```

Because the style attribute is an object, you can also separate the style by writing it as a constant. This way, you can reuse it on other elements as needed:

```javascript
import React from "react";

const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
      <p style={pStyle}>The weather is sunny with a small chance of rain today.</p>
  );
}
```

If you need to extend your paragraph style further down the line, you can use the object spread operator. This will let you add inline styles to your already-declared style object:

```javascript
import React from "react";
const pStyle = {
  fontSize: "16px",
  color: "blue"
};
export default function App() {
  return (
    <>
      <p style={pStyle}>
        The weather is sunny with a small chance of rain today.
      </p>
      <p style={{ ...pStyle, color: "green", textAlign: "right" }}>
        When you go to work, don't forget to bring your umbrella with you!
      </p>
    </>
  );
}

```

Inline styles are the most basic example of a CSS in JS styling technique.

One of the benefits in using the inline style approach is that you will have a simple component-focused styling technique. By using an object for styling, you can extend your style by spreading the object. Then you can add more style properties to it if you want.

But in a big and complex project where you have a hundreds of React components to manage, this might not be the best choice for you.

You can’t specify pseudo-classes using inline styles. That means `:hover`, `:focus`, `:active`, or `:visited` go out the window rather than the component.

Also, you can’t specify media queries for responsive styling. Let’s consider another way to style your React app.

## CSS Stylesheets

When you build a React application using `create-react-app`, you will automatically use webpack to handle asset importing and processing. 

The great thing about webpack is that, since it handles your assets, you can also use the JavaScript `import` syntax to import a `.css` file to your JavaScript file. You can then use the CSS class name in JSX elements that you want to style, like this:

```css
.paragraph-text {
  font-size: 16px;
  color: 'blue';
}
```

```javascript
import React, { Component } from 'react';
import './style.css';

export default function App() {
  return (
    <>
      <p className="paragraph-text">
        The weather is sunny with a small chance of rain today.
      </p>
    </>
  );
}
```

This way, the CSS will be separated from your JavaScript files, and you can just write CSS syntax just as usual.

You can even include a CSS framework such as [Bootstrap](https://create-react-app.dev/docs/adding-bootstrap/) in your React app using this approach. All you need to is import the CSS file into your root component.

This method will enable you to use all of the CSS features, including pseudo-classes and media queries. But the drawback of using a stylesheet is that your style won’t be localized to your component. 

All CSS selectors have the same global scope. This means one selector can have unwanted side effects, and break other visual elements of your app.

Just like inline styles, using stylesheets still leaves you with the problem of maintaining and updating CSS in a big project.

# CSS Modules

[A CSS module](https://create-react-app.dev/docs/adding-a-css-modules-stylesheet/) is a regular CSS file with all of its class and animation names scoped locally by default.

Each React component will have its own CSS file, and you need to import the required CSS files into your component.

In order to let React know you’re using CSS modules, name your CSS file using the `[name].module.css` convention.

Here is an example:

```css
.BlueParagraph {
  color: blue;
  text-align: left;
}
.GreenParagraph {
  color: green;
  text-align: right;
}
```

```javascript
import React from "react";
import styles from "./App.module.css";
export default function App() {
  return (
    <>
      <p className={styles.BlueParagraph}>
        The weather is sunny with a small chance of rain today.
      </p>
      <p className={styles.GreenParagraph}>
        When you go to work, don't forget to bring your umbrella with you!
      </p>
    </>
  );
} 
```

When you build your app, webpack will automatically look for CSS files that have the `.module.css` name. Webpack will take those class names and map them to a new, generated localized name.

Here is the sandbox for the above example. If you inspect the blue paragraph, you’ll see that the element class is transformed into `_src_App_module__BlueParagraph`.

%[https://codesandbox.io/s/css-modules-example-eqh5o?fontsize=14&hidenavigation=1&theme=dark]

CSS Modules ensures that your CSS syntax is scoped locally. 

Another advantage of using CSS Modules is that you can compose a new class by inheriting from other classes that you’ve written. This way, you’ll be able to reuse CSS code that you’ve written previously, like this:

```css
.MediumParagraph {
  font-size: 20px;
}
.BlueParagraph {
  composes: MediumParagraph;
  color: blue;
  text-align: left;
}
.GreenParagraph {
  composes: MediumParagraph;
  color: green;
  text-align: right;
}
```

Finally, in order to write normal style with a global scope, you can use the `:global` selector in front of your class name:

```css
:global .HeaderParagraph {
  font-size: 30px;
  text-transform: uppercase;
}
```

You can then reference the global scoped style like a normal class in your JS file:

```html
<p className="HeaderParagraph">Weather Forecast</p>
```

# Styled Components

Styled Components is a library designed for React and React Native. It combines both the CSS in JS and the CSS Modules methods for styling your components.

Let me show you an example:

```javascript
import React from "react";
import styled from "styled-components";

// Create a Title component that'll render an <h1> tag with some styles
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

export default function App() {
  return <Title>Hello World!</Title>;
}
```

When you write your style, you’re actually creating a React component with your style attached to it. The funny looking syntax of `styled.h1` followed by backtick is made possible by utilizing JavaScript’s tagged template literals. 

Styled Components were created to tackle the following problems:

* **Automatic critical CSS**: Styled-components keep track of which components are rendered on a page, and injects their styles and nothing else automatically. Combined with code splitting, this means your users load the least amount of code necessary.
* **No class name bugs**: Styled-components generate unique class names for your styles. You never have to worry about duplication, overlap, or misspellings.
* **Easier deletion of CSS**: It can be hard to know whether a class name is already used somewhere in your codebase. Styled-components makes it obvious, as every bit of styling is tied to a specific component. If the component is unused (which tooling can detect) and gets deleted, all of its styles get deleted with it.
* **Simple dynamic styling**: Adapting the styling of a component based on its props or a global theme is simple and intuitive, without you having to manually manage dozens of classes.
* **Painless maintenance**: You never have to hunt across different files to find the styling affecting your component, so maintenance is a piece of cake no matter how big your codebase is.
* **Automatic vendor prefixing**: Write your CSS to the current standard and let styled-components handle the rest.

You get all of these benefits while still writing the same CSS you know and love – just bound to individual components.

If you’d like to learn more about styled components, you can visit the [documentation](https://styled-components.com/docs) and see more examples.

# Conclusion

Many developers still debate the best way to style a React application. There are both benefits and drawbacks in writing CSS in a non-traditional way.

For a long time, separating your CSS file and HTML file was regarded as the best practice, even though it caused a lot of problems.

But today, you have the choice of writing component-focused CSS. This way, your styling will take advantage of React’s modularity and reusability. You are now able to write more enduring and scalable CSS.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

