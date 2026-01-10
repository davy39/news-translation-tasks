---
title: How to Use Chakra UI with Next.js and React
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-10-21T00:16:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-chakra-ui-with-next-js-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/chakra.jpg
tags:
- name: components
  slug: components
- name: Libraries
  slug: libraries
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: null
seo_desc: "Building websites and applications is hard. There are a lot of things to\
  \ consider to make sure our apps are usable and accessible including how our React\
  \ components work. \nHow can we take advantage of the power of Chakra UI to build\
  \ great web apps?\n\n..."
---

Building websites and applications is hard. There are a lot of things to consider to make sure our apps are usable and accessible including how our React components work. 

How can we take advantage of the power of Chakra UI to build great web apps?

* [What is Chakra UI?](#heading-what-is-chakra-ui)
* [What makes Chakra UI so great?](#heading-what-makes-chakra-ui-so-great)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Creating a new React project with Next.js](#heading-step-0-creating-a-new-react-project-with-nextjs)
* [Step 1: Installing and configuring Chakra UI in Next.js](#heading-step-1-installing-and-configuring-chakra-ui-in-nextjs)
* [Step 2: Adding Chakra UI components to a React app](#heading-step-2-adding-chakra-ui-components-to-a-react-app)
* [Step 3: Making responsive components with Chakra UI](#heading-step-3-making-responsive-components-with-chakra-ui)
* [Step 4: Customizing the default Chakra UI theme](#heading-step-4-customizing-the-default-chakra-ui-theme)

%[https://www.youtube.com/watch?v=ubB5l-HVPgY]

## What is Chakra UI?

[Chakra UI](https://chakra-ui.com/) is a component library for React that makes it easy to build the UI of an app or website.

Their goal is to provide a simple, modular, and accessible set of components to get up and running quickly.

## What makes Chakra UI so great?

To start, by default Chakra strives to make each component accessible. It’s a critical part of application development that’s often overlooked, and the Chakra maintainers have gone out of their way to ensure the components follow the [WAI-ARIA guidelines](https://www.w3.org/WAI/standards-guidelines/aria/).

Chakra also includes a simple API allowing developers to get productive. It allows people and teams to make inclusive apps without having to worry about building a bunch of components themselves.

For styling and customization, Chakra uses [Emotion](https://emotion.sh/) under the hood to provide developers the ability to style their components right inside of their JavaScript with style props. It comes with a default theme, but allows the ability to easily override it with custom settings.

## What are we going to build?

To get a good idea of how Chakra works, we’re going to essentially rebuild the default Next.js template with Chakra UI components.

This will help us understand a few important concepts, such as how to use Chakra UI with Next.js, how to add custom styles with props, and how to customize the Chakra UI theme.

The concepts here can apply pretty much to any [React](https://reactjs.org/) app, though the examples will be slightly specific to Next.js.

## Step 0: Creating a new React project with Next.js

To get started, we need a React app. We’re going to use Next.js as our framework which will give us the ability to easily spin up a new app.

Once inside the directory you want to create your project in, run:

```
yarn create next-app my-chakra-app
# or
npx create-next-app my-chakra-app

```

Note: feel free to change `my-chakra-app` to whatever you want to name the project directory.

And once that’s finished, you can navigate into that directory and start the project with:

```
yarn dev
# or
npm run dev

```

That should spin up your development server at [http://localhost:3000](http://localhost:3000) and we should be ready to go!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-default-template.jpg)
_Default Next.js template_

[Follow along with the commit!](https://github.com/colbyfayock/my-chakra-app/commit/01f6ec8d961eb197fe3e8a32e498d07bf0be269b)

## Step 1: Installing and configuring Chakra UI in Next.js

Next, let’s install Chakra UI.

Inside of your project directory, run:

```
yarn add @chakra-ui/core @emotion/core @emotion/styled emotion-theming
# or 
npm install @chakra-ui/core @emotion/core @emotion/styled emotion-theming

```

This will install Chakra UI and its dependencies, which includes Emotion, as it relies on it for the styling.

To get Chakra working inside of our app, we need to configure a Provider at the root of our application. This will allow all of Chakra’s components to talk to each other and use the configuration to maintain consistent styles.

Inside `pages/_app.js`, first let’s import our Provider at the top:

```
import { ThemeProvider, theme } from '@chakra-ui/core';

```

Next, replace the return statement inside of the component with:

```jsx
function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider theme={theme}>
      <Component {...pageProps} />
    </ThemeProvider>
  )
}

```

As you’ll notice, we’re also passing a `theme` variable to our provider. We’re importing the Chakra UI default theme straight from Chakra and passing it in to our `ThemeProvider` so all of our components can get the default styles and configurations.

Finally, we want to add a component called `CSSReset` right as a direct child of our `ThemeProvider`.

First, add `CSSReset` as an import:

```
import { ThemeProvider, theme, CSSReset } from '@chakra-ui/core';

```

Then add the component right inside `ThemeProvider`:

```jsx
<ThemeProvider theme={theme}>
  <CSSReset />
  <Component {...pageProps} />
</ThemeProvider>

```

And now if we reload the page, we can see that things are looking a little bit different!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-chakra-ui-css-reset.jpg)
_Next.js with Chakra UI CSS Reset_

The browser comes with a lot of default styles and by default, Chakra UI doesn’t override them. This includes styles like borders on a button element.

While we don’t necessarily need the CSS Reset here, we could override those things manually. This provides us with a foundation where we’ll know that Chakra UI is working as it’s intended to and we can start adding our components.

[Follow along with the commit!](https://github.com/colbyfayock/my-chakra-app/commit/8538b3609cfac71b6ece60e36314edf9a189941b)

## Step 2: Adding Chakra UI components to a React app

Now for the fun part. We’re going to use Chakra UI components to try to rebuild the Next.js default template. It’s not going to look 100% exactly like it, but it will carry the spirit and we can customize it as we’d like.

### Building the Title and Description

Starting from the top, let’s update our title and description.

At the top of the page, we need to import our `Heading` component:

```
import { Heading, Link } from "@chakra-ui/core";

```

Then let’s replace the `<h1>` with:

```jsx
<Heading as="h1" size="2xl" mb="2">
  Welcome to Next.js!
</Heading>

```

Here, we’re using the [Heading](https://chakra-ui.com/heading) component which we then set “as” an `h1`. We can use any HTML heading element tag name, but since we’re replacing an h1, we want to use that.

We’re also setting a `size` attribute, which allows us to control how big out heading is, as well as `mb`, which stands for `margin-bottom`, allowing us to add some space below.

And we can already see our page is looking more like the default template.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-heading-component.jpg)
_Chakra UI Heading component_

We also want to add back our link.

Add `Link` to our import statement at the top and then inside of our `<Heading>` component, replace the Next.js text with:

```jsx
<Link color="teal.500" href="https://nextjs.org">Next.js!</Link>

```

Chakra’s [Link](https://chakra-ui.com/link) component creates a link as expected, but then allows us to use the style props to customize it. Here, we’re using the color variable `teal.500` that Chakra provides to change our link to Chakra’s colors.

And we can see that we have our Next.js link!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-heading-with-link.jpg)
_Chakra UI Heading with Link component_

The last piece of the header is the description. For that, we want to use the Text component.

Add `Text`  and `Code` to the import statement and replace the description with:

```jsx
<Text fontSize="xl" mt="2">
  Get started by editing <Code>pages/index.js</Code>
</Text>

```

We’re using the [Text](https://chakra-ui.com/text) component to recreate a `<p>` tag and the [Code](https://chakra-ui.com/code) component to create our `<code>` tag. Similar to our Heading component, we’re adding a `fontSize` to make the font bigger and `mt` which stands for `margin-top` to add some space above it.

And now we have our header!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-text-with-code-component.jpg)
_Chakra UI Text component with Code_

### Replacing info cards with Chakra UI components

For each of our cards, we can use the same concepts as we did with the header to recreate each of our boxes.

To start, add an import for the `Flex` component and replace the tag `<div className={styles.grid}>` with:

```jsx
<Flex flexWrap="wrap" alignItems="center" justifyContent="center" maxW="800px" mt="10">
  ...
</Flex>

```

Make sure to leave all of the cards inside of the Flex component. The [Flex](https://chakra-ui.com/flex) component will recreate our grid by adding Flexbox along with the same properties that were on the grid before.

At this point, it should exactly the same as it did before.

Next, add `Box` to the import statement and then replace the first card with:

```jsx
<Box as="a" href="https://nextjs.org/docs" p="6" m="4" borderWidth="1px" rounded="lg" flexBasis="45%">
  <Heading as="h3" size="lg" mb="2">Documentation &rarr;</Heading>
  <Text fontSize="lg">Find in-depth information about Next.js features and API.</Text>
</Box>

```

Similar to our Heading component, we’re setting our [Box](https://chakra-ui.com/box) component “as” an `<a>` tag allowing it to serve as a link. We then configure our style props to replicate our cards.

Inside of that, we use the Heading and Text component to recreate the actual content of the cards.

And after only changing the first card, we can now see the changes:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-box-component.jpg)
_Chakra UI Box component_

Now, we can go back and replace the other three cards with the same components to finish recreating our grid.

For fun, we can add a 5th card that links to Chakra UI:

```jsx
<Box as="a" href="https://chakra-ui.com/" p="6" m="4" borderWidth="1px" rounded="lg" flexBasis="45%">
  <Heading as="h3" size="lg" mb="2">Chakra UI &rarr;</Heading>
  <Text fontSize="lg">Build accessible React apps & websites with speed.</Text>
</Box>

```

And with all of our changes, we can now see our recreated Next.js starting template!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-nextjs-grid.jpg)
_Chakra UI recreating Next.js grid_

[Follow along with the commit!](https://github.com/colbyfayock/my-chakra-app/commit/a324f8cd1d4120027a7f4dbcb16f45980de5495a)

## Step 3: Making responsive components with Chakra UI

Part of what the default Next.js grid was able to provide was the ability for the cards to expand to full width once the size of the browser becomes small enough. This is particularly relevant at `600px`, which typically means someone’s on a mobile device.

If we look at our page on a mobile device, we can see that our cards aren’t filling up the entire width.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-not-responsive.jpg)
_Chakra UI default without responsive_

Chakra allows us to [set responsive styles](https://chakra-ui.com/responsive-styles) with its baked in sizing, allowing us to easily recreate our responsive grid cards.

To do this, instead of passing in a single value to our style props, we can pass in an array.

For instance, on each of our Box components, let’s update the `flexBasis` prop to:

```jsx
flexBasis={['auto', '45%']}

```

Here, according to Chakra’s [default responsive breakpoints](https://chakra-ui.com/responsive-styles) , we’re saying that by default, we want our `flexBasis` to be set as `auto`. But for anything `480px` and larger, again which is Chakra’s default first breakpoint, we set it to `45%`.

Chakra considers its responsive styling to be mobile first, which is why you see the `480px` act as a minimum size, not a maximum size.

And with that change, we can now see that on a large device, we still have our grid.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-large-device.jpg)
_Chakra UI components on large device_

But now on mobile, our cards take up the entire width!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-small-device.jpg)
_Chakra UI components on small device_

Using the array pattern works for all of the breakpoints, so if you wanted more control over your styles, Chakra lets you do that.

[Follow along with the commit!](https://github.com/colbyfayock/my-chakra-app/commit/c08e80b60395aa738eaa8f8eb411ca7004ffac9d)

## Step 4: Customizing the default Chakra UI theme

While Chakra provides a pretty great default theme, we also have the ability to customize it to our liking to match our brand or personal taste.

For instance, while the teal that we used for our Heading link is great and uses Chakra’s styles, what if I wanted to customize all links to use the purple that I [use on my website](https://colbyfayock.com/)?

To start, Chakra comes with a default purple, so we can update our link to use that purple:

```jsx
Welcome to <Link color="purple.500" href="https://nextjs.org">Next.js!</Link>

```

And we see our change.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-purple-header.jpg)
_Making Next.js header link purple with color style prop_

That looks great, but let’s update it to the exact purple I use.

Inside of `pages/_app.js`, we’re going to create a new object at the top of the page, where we spread the default theme creating a new theme object. We’ll also replace the `theme` prop with our new object:

```
const customTheme = {
  ...theme
}

function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider theme={customTheme}>

```

If we save and reload the page, it will look exactly the same.

Next, we want to update the colors, so in our custom theme object, let’s add the colors property, where we can then set our custom purple:

```jsx
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    purple: '#692ba8'
  }
}

```

Note: you’ll see here that we’re also spreading `theme.colors`. If we don’t, we’ll be replacing the colors object with only the purple value, meaning we won’t have any other colors.

But if we reload the page, our link isn’t purple anymore!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-link-no-color.jpg)
_Next.js link with no color_

Chakra typically uses ranges of colors which allows us to use different shades of each of the colors. In our Link component, we’re specifying `purple.500` which we didn’t set to exist.

So to fix that, we can use a tool like [Smart Swatch](https://smart-swatch.netlify.app/#692ba8) to get all of our color values that we need and set those in our custom theme object:

```jsx
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    purple: {
      50: '#f5e9ff',
      100: '#dac1f3',
      200: '#c098e7',
      300: '#a571dc',
      400: '#8c48d0',
      500: '#722fb7',
      600: '#59238f',
      700: '#3f1968',
      800: '#260f40',
      900: '#10031a',
    }
  }
}

```

Tip: Smart Swatch actually lets you copy those values as a JavaScript object, making it easier to paste into our theme!

And now if we reload the page, we can see our purple!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-custom-purple.jpg)
_Next.js with custom purple_

While we used a range value here, we can also specify color variables without a range.

Say I wanted to leave the default Chakra purple “as is” but provide a way for me to reference my purple.

To do that, I could remove those purple values and add a new custom variable:

```
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    spacejelly: '#692ba8'
  }
}

```

Then update my Link to use that color:

```jsx
Welcome to <Link color="spacejelly" href="https://nextjs.org">Next.js!</Link>

```

And we can see that we’re now using our purple without overriding the original:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-spacejelly-purple.jpg)
_Next.js with custom color variable_

We can apply this to most parts of the styles of Chakra, including Typography and setting custom Breakpoints. It’s another way to make our project custom to our own while still taking advantage of the power of Chakra!

[Follow along with the commit!](https://github.com/colbyfayock/my-chakra-app/commit/b9d707ce3324207c25c2348934ca0c506402bd2f)

## What else can you do with Chakra UI?

While we went through some simpler examples, it really opens the door to more complex style changes and controls that Chakra provides with its component APIs.

There are also a whole lot of awesome components that you can use to transform your website or application and make development fast and easy!

They even [provide recipes](https://chakra-ui.com/recipes) that have some examples of how you can combine the components resulting in powerful functionality. This includes a responsive header and even adding animations with Framer Motion.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>

