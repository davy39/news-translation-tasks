---
title: An Overview of Prismane  – An Open-Source React UI Library
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-09-27T12:52:48.000Z'
originalURL: https://freecodecamp.org/news/prismane-react-ui-library
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-26-15-16-49.png
tags:
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: null
seo_desc: 'Prismane is a free, comprehensive, have-it-all React UI library that provides
  a broad array of hooks, components, and form validators to help you build beautiful
  and functional user interfaces.

  Prismane was designed with performance in mind, ensuring...'
---

Prismane is a free, comprehensive, have-it-all React UI library that provides a broad array of hooks, components, and form validators to help you build beautiful and functional user interfaces.

Prismane was designed with performance in mind, ensuring lightning-fast loading times for a better user experience.

In this article, you will learn what Prismane is, its cons and pros, how to set up our development environment, and how to build applications using Prismane.

## Key Features of Prismane UI

The library is a large collection of 107+ React components, including buttons, inputs, menus, tables, and more. This enables developers to not reinvent the wheel every time they need common UI elements. Plus, you can customize them according to your preference.

In addition, Prismane offers prebuilt Dark mode support, which adds an extra layer of accessibility and style to your projects. Many users prefer dark mode because it reduces eye strain and improves readability in low-light conditions.

It also has TypeScript support, which allows for type-safe and error-free development. TypeScript enforces strong typing, which means variables, parameters, and return values must adhere to specific data types. This helps catch type-related errors at compile-time rather than at runtime, which reduces the likelihood of unexpected issues in your code.

Prismane also offers a custom styling system that allows you to easily create and apply custom themes to your applications.

Lastly, it has a variety of custom hooks, such as a form builder hook and a toast notification hook, which allow you to encapsulate and reuse complex logic across different parts of your application.

## Benefits of Using Prismane UI

Prismane UI components are all designed to follow a consistent style guide, which ensures that your application has a polished and professional look and feel.

The library also provides a variety of styling options, as well as the ability to create your own custom components. It is highly customizable, so you can easily create user interfaces that match your specific needs.

On top of that, it is free and open source, which gives you the freedom to run, study, modify, and distribute the software. This means you have control over how the software functions, which can be crucial for customization and security.

Lastly, the library is designed to be easy to use – even for developers who are new to React. It provides developers with a large collection of pre-built components and hooks, which can significantly speed up the development process.

## Disadvantages of Using Prismane UI

Prismane is a relatively new library, so it may not have the same level of documentation, features, and community as older, more established libraries.

## How to Build A Prismane Application

We will be using Next.js and Prismane to develop our application.

Let's start by making sure our development environment is ready.

First, install Node.js (you can download it [here](https://nodejs.org/en) if you don't already have it). Node.js version 18 or above is required.

In this tutorial, we will be using Visual Studio Code, but you can use any IDE of your choice.

Now, let's create a Next.js app by running the following command:

```plaintext
npx create-next-app@latest nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/main/basics/learn-starter"
```

Then, change the directory to our project's directory using the following command:

```bash
cd nextjs-blog
```

Let's run the development server using the following command to make sure our application is running well:

```plaintext
npm run dev
```

After making sure everything is fine, press `CTRL+C` and install Prismane:

```bash
npm install @prismane/core
```

In `pages/index.js`, add the following code:

```jsx
import { Card, Image, Text, Button, Flex, fr, PrismaneProvider } from "@prismane/core";
import { Star, ShoppingCart } from "@phosphor-icons/react";


export default function App() {
  return (
    <PrismaneProvider>
    <Card w={360} gap={fr(2)} className="card">
      <Image
        src="https://img.freepik.com/free-photo/black-headphones-digital-device_53876-96805.jpg?size=626&ext=jpg&ga=GA1.1.460882575.1681882906&semt=sph"
        br="md"
        fit="cover"
        mb={fr(2)}
      />
      <Flex gap={fr(2)}>
        <Text fs="md" cl="green">
          <Star /> 4.5 (120 reviews)
        </Text>
        <Text fs="md" cl="blue">
          In Stock
        </Text>
      </Flex>
      <Text fs="lg" fw="bold" cl="black">
        Premium Headphones
      </Text>
      <Text cl="gray">
        Enjoy crystal-clear sound quality with our premium headphones, perfect
        for music lovers and audiophiles.
      </Text>
      <Text fw="bold" fs="2xl" cl="primary">
        $149.99
      </Text>
      <Flex gap={fr(4)} mt="auto">
        <Button cl="primary" bg="yellow">
          Add to Wishlist
        </Button>
        <Button cl="white" bg="blue">
          <ShoppingCart /> Add to Cart
        </Button>
      </Flex>
    </Card>
    </PrismaneProvider>
  );
}
```

The above code is a React component that renders a card with information about a product. The code imports the necessary components and icons from the Prismane and Phosphor Icons libraries, and then defines a component named `App()`.

The `App()` component renders a `Card` component with the following children:

* An `Image` component with the product image
    
* A `Flex` container with two `Button` components, one for adding the product to the wishlist, and one for adding the product to the cart
    
* A `Text` component displaying the product name
    
* A `Text` component displaying the product description
    
* A `Text` component displaying the product price
    
* A `Flex` container with two `Button` components, one for adding the product to the wishlist and one for adding the product to the cart
    

We are also using [Prismane's style props](https://www.prismane.io/docs/styling/style-props) for styling our app in the code above.

Prismane has its own `reset.css`, so it is automatically injected when the app is wrapped with the `PrismaneProvider` component.

## How to Style Our Application

Next, let's create an `_app.js` file in `pages` folder and add the following code:

```jsx
function App({ Component, pageProps }) {
    return (
      <Component {...pageProps} />
    );
  }

  export default App;
```

In a Next.js application, the `_app.js` file is a special layout component that is used to wrap our entire application. It serves as the entry point for customizing the behavior and appearance of our app across all pages.

Now, let's style our app. Create a `global.css`file in our `pages`folder and add the following code:

```plaintext
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

  .card {
    font-family: Poppins, sans-serif;
  }
  body {
    width: 100vw;
    height: 100vh;
    display: flex;
    background-color: rgb(var(--prismane-colors-base-300));
  }
```

The code is importing the `Poppins` font from Google Fonts and applying it to the `.card` element. It also defines the width, height, display property, and background color for the `body` element.

Lastly, let's import our `global.css` file in our `app.js` file by adding the following line of code:

```jsx
import './global.css';
```

You can find the full code [here](https://github.com/gatwirival/prismane-ui-demo).

And here it the code's output:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-26-13-34-29.png align="left")

*Output*

This is just a simple example of how to develop a web application using Prismane. There are many other features and options available in Prismane UI that you can use to create more complex and sophisticated applications.

## Conclusion

Overall, Prismane UI is a great React UI library that offers a wide range of features and benefits. It is a good choice for developers of all experience levels, and it is well-suited for a variety of projects.

## References

[Prismane website](https://www.prismane.io/)

[Next.js website](https://nextjs.org/learn/basics/create-nextjs-app)

[Phosphor-icons repository](https://github.com/phosphor-icons/react)
