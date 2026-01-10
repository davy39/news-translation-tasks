---
title: 'Styled Components: The Essentials Explained in 3 Steps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/styled-components-essentials-in-three-steps
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lego-1.jpeg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: styled-components
  slug: styled-components
seo_title: null
seo_desc: 'By Thomas Weibenfalk


  Cover Photo by Hello I’m Nik ?? on Unsplash


  I love React and Styled Components. It’s like building stuff with lego bricks into
  something bigger and whole.

  Styled Components are awesome and a perfect match for React. They really...'
---

By Thomas Weibenfalk

> Cover Photo by [Hello I’m Nik ??](https://unsplash.com/@helloimnik?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/lego-part?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

I love React and Styled Components. It’s like building stuff with lego bricks into something bigger and whole.

Styled Components are awesome and a perfect match for React. They really are. And they’re also easy to understand…really. 

In this article I will break down everything you need to know to get started (and beyond started) in three parts. Not deeply technical, and simply explained. If you know these three things, you know enough to use Styled Components in your project without hassle.

The three things are:

1. **How to create and use a Styled Component.**
2. **How to modify your CSS conditionally with props**
3. **How to create Global Styling.**

I’ll go through them one by one now.

# 1. How to create and use a Styled Component

I’ll dive right into it. First you have to install Styled Components in your project. Do it by typing:

```js
npm i styled-components
```

Now you’re good to go. You can use Styled Components in your projects. Below is some code that I’ll explain below. Have a good look at it and continue reading below the code.

```js
import React from "react";
import styled from "styled-components";

const StyledLogin = styled.div`
  display: flex;
  align-items: center;
  flex-flow: column;
  width: 200px;
  height: 200px;
  margin: 0 auto;
  border: 2px solid #000;
  border-radius: 20px;
  background: #eee;

  h2 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 14px;
  }

  button {
    background: green;
    color: #fff;
    padding: 10px;
    margin: 5px;
    width: 150px;
    border: none;
    border-radius: 10px;
    box-sizing: border-box;
  }
`;

const StyledInput = styled.input`
  border: 1px solid #000;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  width: 150px;
  box-sizing: border-box;
`;

const Login = () => (
  <StyledLogin>
    <h2>Login</h2>
    <StyledInput type="text" placeholder="email" />
    <StyledInput type="password" placeholder="password" />
    <button>Login</button>
  </StyledLogin>
);

export default Login;
```

The above code will create a component called Login that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/login_1.png)
_Login form from the component Login.js_

Nothing fancy, nothing special. Just a Login component to help us understand Styled Components better. Ok - the first thing you’ll notice in the above code is that we have to somehow tell React that we want to use Styled Components. We do this by importing it like so:

```js
import styled from “styled-components”;
```

Now we have imported an object called `styled` that we can use to style our components. This object has different properties that you can use depending on what you want to style. If it is a div, like in our example, you just simply access the div property on the `styled` object. Like so: `styled.div`

If you want to style a button you can simply type `styled.button` instead.  
Or if it was an h2 tag you can type `styled.h2` …you get the point!

These properties are holding functions that you can call with _tagged template literals_. Meaning that we can send in the data to these functions by using back-ticks and then put our CSS between these back-ticks (````). You also create a const to hold the Styled Component. So if we want to create a Styled Component for our Login component we just write the below code:

```js
const StyledLogin = styled.div`
  display: flex;
  align-items: center;
  flex-flow: column;
  width: 200px;
  height: 200px;
  // And more CSS code below
`;
```

In short, to create styling for a div element with Styled Components you just use this syntax:

```js
const SomeName = styled.div` CSS code goes here … `;
```

Then you can just use it as a regular component:

```js
<SomeName> Your other code here … </SomeName>
```

You can create as many of these Styled Components as you need. In the above example I’ve created two Styled Components, one that’s called `StyledLogin` and one that’s called `StyledInput`**.**

One more thing about creating a standard Styled Component that’s good to know is the nesting part. Styled Components have the ability to nest styling just like you can do in, for example, SASS. 

You can see in the above code that I have nested my styling for the **h2** and the **button** elements. This is great in so many ways! It will make your code a lot more structural and clean. You can easily see what styling belongs to what component. You are also isolating the styling to only that component, meaning that other **h2** and **button** elements in your App won’t be affected.

So, when it makes sense, use nesting to style elements. It doesn’t always make sense, though. You don’t have to create a completely new Styled Component for every little element. That’s when nesting like this come in handy instead.

_That’s one_ - _two to go._

# **2. How to modify your CSS conditionally with props.**

Styled components can receive props. Just like a regular Component. By passing in props to your Styled Component you can do some conditional CSS styling. Smooooooth … ?‍♂️

Let’s say we want to change the color of the password input field depending on if the user typed in the wrong password or not.

Ok, I realize that this is a really simplified solution and there would be much more than a simple prop involved in stuff like this. But for the sake of this tutorial article, let’s say that we do it like this.

If we have a prop that’s called `correct` set to false, we make our textbox red instead. Let’s have a look at the below code. I’ve intentionally left out the styling code for the whole Login component to save space. So let’s pretend that that’s there and is the same as above.

```js
const StyledInput = styled.input`
  border: 1px solid #000;
  border-radius: 10px;
  padding: 10px;
  margin: 5px;
  width: 150px;
  box-sizing: border-box;
  background: ${prop => prop.correct ? 'white' : 'red'};
`;

const Login = () => (
  <StyledLogin>
    <h2>Login</h2>
    <StyledInput correct={true} type="text" placeholder="email" />
    <StyledInput correct={false} type="password" placeholder="password" />
    <button>Login</button>
  </StyledLogin>
);
```

This will give us this result:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/login_2.png)

First, take a look at the `Login` component. And the `StyledInput` components. I’ve created a prop that's called `correct` and I'm passing in `true` and `false` to the two different components. The one that gets the _true_ value will be shown in white.  
To access this prop value in your Styled Component CSS you can use the below code:

```js
background: ${prop => prop.correct ? ‘white’ : ‘red’};
```

You just simply create a ternary operator inside an arrow function surrounded by `${}` telling this Styled Component to select the white color if `prop.correct` is `false`. And use the red color if `prop.correct` is `true`. Simple as that!

You can do this with any CSS property you want! ✌️And that’s how you do conditional CSS with props in Styled Components.

_Two down_ - _one to go._

# **3. How to create Global Styling.**

The last essential thing you need to know to use Styled Components is how to create global styling.

Global styling is achieved by using a special function for this purpose from the Styled Components library. It’s called `createGlobalStyle` and you import it like this**:**

```js
import { createGlobalStyle } from ‘styled-components’;
```

Then you can create a Global Styled Component like this:

```js
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    background: #000;
    color: #fff;
  }
`;

const App = () => {
  <>
    <GlobalStyle />
    <Login />
  </>
}
```

You just place the global style component at the top level of your application. Then, it will use the style throughout your App. In this case, I assume that the top-level Component is named `App`. You can also use props and do some conditional CSS in global Styled Components. Just like the regular Styled Components.

# Conclusion

That is it! There’s more to Styled Components than this, but I think that these really are the essentials that you need to know for using Styled Components. 

If you’re interested in learning more I highly recommend that you go to the website [https://www.styled-components.com/docs/](https://www.styled-components.com/docs/) and read the docs there.

Also, thank you for reading this post. I’m a Developer from Sweden that loves to teach and code. I also create courses on React and Gatsby online. You can find me on Udemy. Just search for Thomas Weibenfalk or hook me up on Twitter **@weibenfalk**

I also have a Youtube channel were I teach free stuff, check it out [**here**](https://www.youtube.com/channel/UCnnnWy4UTYN258FfVGeXBbg)**.**

