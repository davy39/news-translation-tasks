---
title: How to Style Your React Apps with Less Code Using Tailwind CSS, Styled Components,
  and Twin Macro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-15T10:45:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-your-react-apps-with-less-code-using-tailwind-css-and-styled-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-1.png
tags:
- name: React
  slug: react
- name: styled-components
  slug: styled-components
- name: tailwind
  slug: tailwind
seo_title: null
seo_desc: 'By Ibrahima Ndaw

  Tailwind is a utility-first CSS framework for rapidly building custom designs. It
  can be used alone to style React Apps. However, it can be better combined with Styled
  Components. That combination brings the magic of Tailwind into CS...'
---

By Ibrahima Ndaw

Tailwind is a utility-first CSS framework for rapidly building custom designs. It can be used alone to style React Apps. However, it can be better combined with Styled Components. That combination brings the magic of Tailwind into CSS-in-JS.

In this guide, we will build a form component without writing a single line of CSS using Tailwind CSS, Styled Components, and Twin Macro.

Let's dive in!

* [Why use it?](#heading-why-use-it)
* [Setting up](#heading-setting-up)
* [Configuring Tailwind CSS](#heading-configuring-tailwind-css)
* [Tailwind CSS and Styled Components](#heading-tailwind-css-and-styled-components)
* [Conclusion](#heading-conclusion)
* [Resources](#heading-resources)

## Why use it?

The "Why" is pretty legit and important, since we can use either Tailwind CSS or Styled Components. So why combine them and use both at the same time?

Well, Tailwind classes can be quite long, and it causes our components to have some readability issues. Maintaining them can be tough.

In the case of Styled Components, there is no problem except the fact that we have to write the style. It is not that problematic – but why should we write something that Tailwind already offers?

So it makes sense to use Tailwind CSS in combination with Styled Components. Tailwind CSS helps with utility classes, and Styled Components keeps our components clean with the help of CSS-in-JS.

## Setting up

In this guide, we will build a simple form as an example. And to do so, we need a fresh React app.

So, let's run in the terminal the following command.

```shell
    npx create-react-app react-styled-tailwind

```

Next, structure your folder as follows:

```
├── src
|  ├── App.js
|  ├── App.test.js
|  ├── assets
|  |  └── tailwind.css
|  ├── index.js
|  ├── serviceWorker.js
|  ├── setupTests.js
|  ├── tailwind.config.js
|  └── styles
|     └── index.js
├── babel.plugin.js
├── package.json
├── postcss.config.js
├── README.md
├── yarn-error.log
└── yarn.lock

```

I will explain each file as we progress, but for now, let's install the dependencies.

```shell
    yarn add -D tailwindcss twin.macro autoprefixer babel-plugin-macros postcss-cli

```

Next, install Styled Components by running this command:

```shell
    yarn add styled-components

```

Once these libraries are installed, we can now move to the configuration of Tailwind CSS

## Configuring Tailwind CSS

To configure it, we have to manually add a config file or run the following command to generate a new one:

```shell
    npx tailwind init src/tailwind.config.js

```

Here, instead of generating the config file on the root directory, you have to put it on the `src` folder – otherwise an error will be thrown by Tailwind Macro.

And the generated file will look like this:

* `tailwind.config.js`

```js
module.exports = {
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}

```

As you can see, the config file is "empty" since there is no configuration. For this tutorial, we don't need to configure anything here. But you can customize it to follow your needs or run the command with the `--full` option to get the complete Tailwind config.

Next, we need to create a new file `postcss.config.js` in the root directory.

* `postcss.config.js`

```js
module.exports = {
  plugins: [
    require("tailwindcss")("./src/tailwind.config.js"),
    require("autoprefixer"),
  ],
}

```

This configuration tells the `postcss.config.js` file to use the Tailwind CSS library and the `tailwind.config.js` file during compile-time. With the help of `autoprefixer` it tracks which properties need to be prefixed.

With that setup, we can now move to the `babel.plugin.js` file which helps to transform Tailwind classes into CSS-in-JS code.

* `babel.plugin.js`

```js
module.exports = {
  tailwind: {
    plugins: ["macros"],
    config: "./src/tailwind.config.js",
    format: "auto",
  },
}

```

Later we will see in action what this file does. But for now, just keep in mind that it's the glue between Tailwind CSS and Styled Components.

_There are just three last steps to do to complete the setup._

![still](https://media.giphy.com/media/tXL4FHPSnVJ0A/source.gif)

First, in the `tailwind.css` file, we need to import some utilities from the Tailwind library.

* `src/assets/tailwind.css`

```css
@tailwind base;

@tailwind components;

@tailwind utilities;

```

Here, as you can see, there is nothing fancy, just some imports that allow us to use Tailwind utility classes.

The second step is to connect our React App with Tailwind CSS.

* `index.js`

```js
import React from "react"
import ReactDOM from "react-dom"
import App from "./App"
import "./assets/styles.css"
import * as serviceWorker from "./serviceWorker"

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
)

serviceWorker.unregister()

```

Here, we import `assets/styles.css` which contains the CSS style. And later, we will tweak the default script a bit to build the CSS and add it to the `assets/styles.css` file during compile.

And last but not the least, we have to update the `package.json` file.

* `package.json`

```js
"scripts": {
    "build:css": "postcss src/assets/tailwind.css -o src/assets/styles.css",
    "watch:css": "postcss src/assets/tailwind.css -o src/assets/styles.css",
    "start": "npm run watch:css & react-scripts start",
    "build": "npm run build:css react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
 }

```

These two scripts `build:css` and `watch:css` will respectively build the CSS and watch for changes and rebuild it if needed. And as I said earlier, the output file will be located in the `assets` folder.

With that change, we can now use Tailwind in our app. Let's now combine it with Styled Components.

## Tailwind CSS and Styled Components

Earlier, in our structure folder, we had a `styles` folder. It's time to tweak it with the following code.

* `styles/index.js`

```js
import styled from "styled-components"
import tw from "twin.macro"

const StyledForm = styled.main.attrs({
  className: "flex flex-col h-screen justify-center items-center bg-gray-100",
})`
  & {
    form {
      ${tw`bg-white text-center rounded py-8 px-5 shadow max-w-xs`}
    }
    input {
      ${tw`border-gray-300 mb-4 w-full border-solid border rounded py-2 px-4`}
    }
    button {
      ${tw`bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 border border-blue-700 rounded`}
    }
  }
`
export default StyledForm

```

We start by importing `tw` which allows us to use Tailwind classes in nested properties. It's perfectly fine to use the utility classes with the `className` attribute, but if you want to nest properties you have to use the `twin.macro` library.

This library will use the babel plugin macros config (`babel.plugin.js`) to transform the Tailwind CSS utility classes used by nested selectors into readable code that Styled Components can understand.

You can see in this example below how the transformation is done.

```js
// input
const test = ${tw`text-center bg-red w-full`}
// output
const test = {
    background: 'red',
    textAlign: 'center',
    width: '100%'
}

```

Great! Now that we have combined Tailwind with Styled Components, let's add the styled component to the `App.js` file.

* `App.js`

```js
import React from "react"
import StyledForm from "./styles"

function App() {
  return (
    <StyledForm>
      <form>
        <input type="text" placeholder="Full name" />
        <input type="text" placeholder="Email" />
        <input type="text" placeholder="Password" />
        <button>Sign In</button>
      </form>
    </StyledForm>
  )
}

export default App

```

Here, we just imported the styled component and wrapped everything with it to make our form look nice.

![Image of React form styled with Tailwind](https://www.freecodecamp.org/news/content/images/2021/10/react-tailwind-form.png)

Great! You can already see how powerful this combination is. We have built a form component without writing a line of CSS and the component is still readable.

## Conclusion

There is a bit of hassle to set up Tailwind CSS. But once it's done and combined with CSS-in-JS, it's really powerful and flexible. This is partly because we can customize the `tailwind.config.js` file to follow our need or just write normal CSS as we usually do with Styled Components. It's definitely something to consider in your next React app.

Thanks for reading!

You can find the [Source Code here](https://github.com/ibrahima92/react-styled-tailwind).

[Read more of my articles](https://www.ibrahima-ndaw.com/)

[Subscribe to my newsletter](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)

[Follow me on twitter](https://twitter.com/ibrahima92_)

## Resources

[Tailwind CSS Docs](https://tailwindcss.com/docs/installation/)

[Tailwind CSS Cheat sheet](https://nerdcave.com/tailwind-cheat-sheet)

[Twin Macro Docs](https://github.com/ben-rogerson/twin.macro)

[Styled Components Docs](https://styled-components.com/docs)

