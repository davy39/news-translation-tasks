---
title: How to Style a React Application – Different Options Compared
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-06-05T21:52:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pawel-czerwinski-3k9PGKWt7ik-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Styling plays a vital role in creating visually appealing and user-friendly
  web applications. When it comes to React applications, there are numerous ways to
  style components and UI elements.

  In this article, we will explore several popular options, ...'
---

Styling plays a vital role in creating visually appealing and user-friendly web applications. When it comes to React applications, there are numerous ways to style components and UI elements.

In this article, we will explore several popular options, including pure CSS, CSS modules, CSS preprocessors, Tailwind CSS, CSS-in-JS libraries like Styled Components, and pre-built component libraries like Chakra UI, Material-UI, and Bootstrap.

We'll delve into each option's main characteristics, advantages, and disadvantages to help you choose the right styling approach for your React projects.

# Table of Contents

You'll learn how to style your React apps using:

* [Pure CSS](#heading-how-to-style-your-react-apps-using-pure-css)
    
* [CSS modules](#heading-how-to-style-your-react-apps-using-css-modules)
    
* [CSS preprocessors](#heading-how-to-style-your-react-apps-using-css-preprocessors)
    
* [Tailwind CSS](#heading-how-to-style-your-react-apps-using-tailwind-css)
    
* [CSS-in-JS](#heading-how-to-style-your-react-apps-using-css-in-js)
    
* [Component libraries](#heading-how-to-style-your-react-apps-using-component-libraries)
    
* [Conclusion](#heading-conclusion)
    

# How to Style Your React Apps Using Pure CSS

Pure CSS involves writing stylesheets using standard CSS syntax and linking them to your React components.

This approach is simple and widely supported, making it an excellent choice for small-scale projects. But it can become challenging to manage and scale as the application grows.

### Pros:

* **Familiarity:** Developers with CSS expertise can quickly adapt to this approach.
    
* **Browser Support:** Pure CSS is supported by all modern browsers.
    
* **Lightweight:** CSS files can be cached by the browser, resulting in faster page loading times.
    

### Cons:

* **Global Scope:** Styles defined in CSS are global by default, which can lead to naming conflicts and style leakages.
    
* **Limited Reusability:** Reusing styles across components requires manually maintaining class names and selectors.
    

### Example:

```javascript
import React from 'react';
import './MyComponent.css';

const MyComponent = () => {
  return (
    <div className="my-component">
      <h1 className="title">Hello, World!</h1>
      <p className="description">This is a styled React component.</p>
      <button className="btn">Click Me</button>
    </div>
  );
};

export default MyComponent;
```

In this example, we have a component called `MyComponent`. To apply styles using pure CSS, we import an external CSS file called `MyComponent.css`. Here's how the CSS file might look:

```css
.my-component {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.title {
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
}

.description {
  font-size: 16px;
  color: #777;
}

.btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}
```

In this CSS file, we define styles for the different classes used in the component. The `my-component` class styles the container div, the `title` class styles the heading, the `description` class styles the paragraph, and the `btn` class styles the button.

When the `MyComponent` is rendered, it will have the defined styles applied. The container div will have a light gray background with padding and border-radius. The heading will have a larger font size and a dark gray color, while the paragraph will have a smaller font size and a light gray color. The button will have a blue background with white text, and it will transition to a darker blue on hover.

Remember to import the CSS file correctly, ensuring that the path is accurate based on your project structure.

# How to Style Your React Apps Using CSS Modules

CSS Modules aim to solve the global scope and reusability issues of pure CSS. They allow you to write modular stylesheets, where class names are scoped to specific components.

### Pros:

* **Scoped Styles:** CSS Modules generate unique class names for each component, avoiding style clashes.
    
* **Reusability:** Styles defined in CSS Modules can be easily reused across components.
    
* **Clear Dependencies:** Stylesheets are imported and linked directly to the components that use them.
    

### Cons:

* **Learning Curve:** Developers must learn and understand the CSS Modules syntax and import mechanism.
    
* **Additional Configuration:** Integrating CSS Modules into a React project often requires extra configuration setup.
    

### Example

```javascript
import React from 'react';
import styles from './MyComponent.module.css';

const MyComponent = () => {
  return (
    <div className={styles.myComponent}>
      <h1 className={styles.title}>Hello, World!</h1>
      <p className={styles.description}>This is a styled React component.</p>
      <button className={styles.btn}>Click Me</button>
    </div>
  );
};

export default MyComponent;
```

In this example, we import an external CSS module file called `MyComponent.module.css` and assign it to the `styles` object. The `styles` object contains mappings of CSS class names to unique generated class names specific to the component.

Here's how the CSS module file might look:

```css
.myComponent {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.title {
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
}

.description {
  font-size: 16px;
  color: #777;
}

.btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}
```

In the CSS module file, you define styles as you would in regular CSS, but instead of using global class names, you use local class names. These local class names are scoped to the component and have unique names generated during the build process.

When the `MyComponent` is rendered, the CSS module styles are applied using the corresponding class names from the `styles` object. The component's container div, heading, paragraph, and button will have the respective styles applied.

Make sure to use the `className` attribute and reference the CSS module class names from the `styles` object in your component's JSX. The CSS module system will automatically map these class names to the unique generated class names, ensuring style encapsulation and preventing class name collisions.

Note that the CSS module file should have the `.module.css` file extension for the module to work correctly.

# How to Style Your React Apps Using CSS preprocessors

CSS preprocessors like [SASS](https://sass-lang.com/), [LESS](https://lesscss.org/) or [Stylus](https://stylus-lang.com/) provide additional features like variables, nesting, mixins, and more. It enhances the productivity and maintainability of CSS code.

### Pros:

* **Advanced Features:** SCSS introduces powerful features that simplify CSS writing and management.
    
* **Code Reusability:** SCSS allows creating reusable code snippets using mixins and variables.
    
* **Easy Migration:** Existing CSS files can be gradually converted to SCSS without significant refactoring.
    

### Cons:

* **Compilation Step:** SCSS files need to be compiled into regular CSS before they can be used.
    
* **Learning Curve:** Developers must learn SCSS syntax and its specific features.
    

### Example

Here's an example of how you can use Sass to style a React component. First, make sure you have Sass installed in your project by running `npm install node-sass` or `yarn add node-sass`.

```javascript
import React from 'react';
import './MyComponent.scss';

const MyComponent = () => {
  return (
    <div className="my-component">
      <h1 className="title">Hello, World!</h1>
      <p className="description">This is a styled React component.</p>
      <button className="btn">Click Me</button>
    </div>
  );
};

export default MyComponent;
```

In this example, we import an external SCSS file called `MyComponent.scss`. Make sure the file extension is `.scss` for Sass files. Here's how the SCSS file might look:

```scss
.my-component {
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  text-align: center;

  .title {
    font-size: 24px;
    color: #333;
    margin-bottom: 10px;
  }

  .description {
    font-size: 16px;
    color: #777;
  }

  .btn {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: #0056b3;
    }
  }
}
```

# How to Style Your React Apps Using Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that offers a vast set of pre-defined utility classes. It promotes rapid development and consistent styling across an application.

### Pros:

* **Rapid Prototyping:** Tailwind CSS provides an extensive collection of utility classes, enabling quick UI development.
    
* **Highly Customizable:** The framework allows customization through a configuration file, enabling tailored styling.
    
* **Consistent Styling:** By using predefined utility classes, styling consistency can be easily maintained.
    

### Cons:

* **File Size:** Including the entire Tailwind CSS framework can result in a larger bundle size.
    
* **Class Overload:** Over-reliance on utility classes may lead to bloated HTML markup.
    

### Example:

First, make sure you have Tailwind CSS installed in your project by following the [installation guide in the official Tailwind CSS documentation](https://tailwindcss.com/docs/installation).

```javascript
import React from 'react';

const MyComponent = () => {
  return (
    <div className="bg-gray-200 p-4 rounded-lg text-center">
      <h1 className="text-2xl text-gray-800 mb-2">Hello, World!</h1>
      <p className="text-base text-gray-600">This is a styled React component.</p>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Click Me
      </button>
    </div>
  );
};

export default MyComponent;
```

In this example, we don't import any external CSS or SCSS files. Instead, we directly use Tailwind CSS utility classes within the component's JSX. The utility classes provide ready-to-use styles for various aspects of the component.

The utility classes used in the example (`bg-gray-200`, `p-4`, `rounded-lg`, `text-center`, `text-2xl`, `text-gray-800`, `mb-2`, `text-base`, `text-gray-600`, `bg-blue-500`, `hover:bg-blue-700`, `text-white`, `font-bold`, `py-2`, `px-4`, `rounded`) define the background color, padding, border radius, text alignment, text size, text color, margins, button styling, and more.

When the `MyComponent` is rendered, the respective utility classes from Tailwind CSS will be applied to the corresponding elements, resulting in the desired styles.

Ensure that your project is properly configured to use Tailwind CSS, including importing the necessary Tailwind CSS stylesheets and applying the required build process (such as running `npm run build` or `yarn build` to generate the production-ready CSS file).

Tailwind CSS provides a wide range of utility classes, and you can mix and match them to create the desired styling for your React components. Refer to the official Tailwind CSS documentation for more information on available utility classes and customization options.

# How to Style Your React Apps Using CSS-in-JS

CSS-in-JS libraries like [Styled Components](https://styled-components.com/) offer a unique approach to styling by allowing developers to write CSS directly in their JavaScript code. Styled Components offer a way to create reusable and scoped styles within React components.

### Pros:

* **Component-Based Styling:** Styles are written within the component, enhancing code organization and reusability.
    
* **Dynamic Styling:** Styled Components enable dynamic styling based on component props or state.
    
* **Easy Theme Integration:** Themes can be easily incorporated, providing consistent styling throughout the application.
    

### Cons:

* **Build Complexity:** CSS-in-JS solutions often require additional build tools and dependencies.
    
* **Performance Impact:** Generating dynamic styles at runtime can impact the application's performance.
    

### Example

First, make sure you have the Styled Components library installed in your project by running `npm install styled-components` or `yarn add styled-components`.

```javascript
import React from 'react';
import styled from 'styled-components';

const StyledDiv = styled.div`
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
`;

const StyledTitle = styled.h1`
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
`;

const StyledDescription = styled.p`
  font-size: 16px;
  color: #777;
`;

const StyledButton = styled.button`
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056b3;
  }
`;

const MyComponent = () => {
  return (
    <StyledDiv>
      <StyledTitle>Hello, World!</StyledTitle>
      <StyledDescription>This is a styled React component.</StyledDescription>
      <StyledButton>Click Me</StyledButton>
    </StyledDiv>
  );
};

export default MyComponent;
```

In this example, we import the `styled` function from the `styled-components` library. We then create styled components by assigning the result of calling `styled` with the desired HTML element to variables (`StyledDiv`, `StyledTitle`, `StyledDescription`, `StyledButton`).

Within the backticks (\`) of each styled component, we define the CSS rules specific to that component.

When the `MyComponent` is rendered, the styled components are used in place of the regular HTML elements. The styles defined within the respective styled components will be applied to the corresponding elements.

Styled Components allow you to write CSS directly within your JavaScript code, making it easy to encapsulate styles and create reusable components. You can also pass props to styled components and use them in your CSS rules to create dynamic styles.

Make sure to import the `styled` function from `styled-components` and define your styled components before using them in your component.

Remember to install and configure Styled Components in your project before using them.

# How to Style Your React Apps Using Component Libraries

Component libraries like [Chakra UI](https://chakra-ui.com/), [Material-UI](https://mui.com/), and [Bootstrap](https://getbootstrap.com/) offer pre-built and styled React components along with accompanying styles. These libraries provide a consistent and cohesive UI design language.

### Pros:

* **Rapid Development:** Ready-to-use components speed up the development process.
    
* **Consistent Styling:** Components within a library adhere to a unified design system, ensuring visual consistency.
    
* **Extensive Documentation:** Popular component libraries have well-documented APIs and guidelines.
    

### Cons:

* **Customization Limitations:** While these libraries offer customization options, they may not fulfill every design requirement.
    
* **Bundle Size:** Including an entire component library can increase the application's bundle size.
    

### Example

First, make sure you have Material-UI installed in your project by running `npm install @mui/material` or `yarn add @mui/material`.

```javascript
import React from 'react';
import { styled } from '@mui/system';
import { Button, Paper, Typography } from '@mui/material';

const StyledPaper = styled(Paper)(({ theme }) => ({
  backgroundColor: '#f2f2f2',
  padding: theme.spacing(2),
  borderRadius: theme.spacing(1),
  textAlign: 'center',
}));

const StyledTitle = styled(Typography)(({ theme }) => ({
  fontSize: 24,
  color: '#333',
  marginBottom: theme.spacing(1),
}));

const StyledDescription = styled(Typography)(({ theme }) => ({
  fontSize: 16,
  color: '#777',
}));

const StyledButton = styled(Button)(({ theme }) => ({
  backgroundColor: '#007bff',
  color: '#fff',
  borderRadius: theme.spacing(1),
  padding: theme.spacing(1, 2),
  transition: 'background-color 0.3s ease',

  '&:hover': {
    backgroundColor: '#0056b3',
  },
}));

const MyComponent = () => {
  return (
    <StyledPaper>
      <StyledTitle variant="h1">Hello, World!</StyledTitle>
      <StyledDescription variant="body1">This is a styled React component.</StyledDescription>
      <StyledButton variant="contained">Click Me</StyledButton>
    </StyledPaper>
  );
};

export default MyComponent;
```

In this example, we import the necessary components from Material-UI (`Button`, `Paper`, `Typography`) and the `styled` function from `@mui/system`. We then create styled components using the `styled` function, assigning the result to variables (`StyledPaper`, `StyledTitle`, `StyledDescription`, `StyledButton`).

Within the function passed to `styled`, we define the CSS rules specific to each styled component using the Material-UI theme object (`theme`) for consistent theming.

When the `MyComponent` is rendered, the styled components are used in place of the regular Material-UI components. The styles defined within the respective styled components will be applied to the corresponding elements.

Styled components in Material-UI follow a similar approach to Styled Components, allowing you to encapsulate styles within your components using the `styled` function and the Material-UI theme object.

Make sure to import the necessary components and functions from Material-UI and define your styled components before using them in your component.

Remember to install and configure Material-UI in your project before using it.

# Conclusion

Based on what we've seen, here's a quick comparison table between different options for styling a React app:

| **Option** | **Main Characteristics** | **Pros** | **Cons** | **When to Use** |
| --- | --- | --- | --- | --- |
| Pure CSS | Traditional approach with global CSS files | Simple and familiar | Lack of encapsulation and potential for class name collisions | Small projects or when CSS customization is the main focus |
| CSS Modules | CSS files with locally scoped class names | Scoped styles and prevents class name clashes | Requires importing and referencing unique class names | Medium-sized projects requiring style encapsulation |
| CSS Preprocessors (e.g., Sass, Less) | Enhanced CSS syntax with variables, mixins, etc. | Reusable code, modular and maintainable styles | Build process needed for compilation | Projects that benefit from enhanced CSS syntax |
| Tailwind CSS | Utility-based CSS framework | Rapid development, consistent styling, extensive utility classes | Large file size due to utility classes | Prototyping or projects where rapid development is crucial |
| CSS-in-JS | Writing CSS directly in JavaScript using libraries like Styled Components or Emotion | Component-based styles, dynamic styling, props-based styles | Increased bundle size, additional learning curve | Projects with complex or dynamic styling requirements |
| Component Libraries (e.g., MUI, Chakra) | Pre-styled and customizable UI components | Consistent design, extensive component library, theming support | Limited customization options, larger bundle size | Projects requiring ready-to-use UI components with theming support |

Each option has its own strengths and weaknesses, and the choice depends on the specific project requirements and preferences. Here's a breakdown of when each option may be more convenient:

* **Pure CSS:** Suitable for small projects or when CSS customization is the main focus. It is simple and familiar but lacks encapsulation and can lead to class name collisions in larger projects.
    
* **CSS Modules:** Ideal for medium-sized projects that require style encapsulation. It offers scoped styles, prevents class name clashes, and requires importing and referencing unique class names.
    
* **CSS Preprocessors:** Recommended for projects that benefit from enhanced CSS syntax with variables, mixins, and other features. They promote reusable and maintainable styles but require a build process for compilation.
    
* **Tailwind CSS:** Perfect for rapid development and prototyping. It provides an extensive set of utility classes for consistent styling but can result in a large file size due to the number of utility classes.
    
* **CSS-in-JS:** Well-suited for projects with complex or dynamic styling requirements. Writing CSS directly in JavaScript offers component-based styles and dynamic styling capabilities, but it may increase the bundle size and has an additional learning curve.
    
* **Component Libraries:** Useful when you need ready-to-use UI components with consistent design and theming support. They offer extensive component libraries but may have limited customization options and result in a larger bundle size.
    

Consider the project's size, styling needs, development speed, and customization requirements when choosing the appropriate styling option. It's also worth considering the team's familiarity with the chosen option and its ecosystem.

Well everyone, as always, I hope you enjoyed the article and learned something new.

If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman). See you in the next one!

![Image](https://www.freecodecamp.org/news/content/images/2023/06/c70acd30c5bc4847faea61747c11bece.gif align="left")
