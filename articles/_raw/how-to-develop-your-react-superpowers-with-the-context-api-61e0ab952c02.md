---
title: How to develop your React superpowers with the Context API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-19T19:37:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-context-api-61e0ab952c02
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XUtWIwT2DgPoLkd5
tags:
- name: coding
  slug: coding
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: null
seo_desc: 'By Eduardo Vedes

  Hey everyone! ❤️

  This time I’m going to show how to use the Context API in React.

  Context provides a way to pass data through the component tree without having to
  pass props down manually along every level.

  React typically works with...'
---

By Eduardo Vedes

Hey everyone! ❤️

This time I’m going to show how to use the Context API in React.

Context provides a way to pass data through the component tree without having to pass props down manually along every level.

React typically works with a top-down (parent to child) flow of data. This works very well in a cascade of props, always giving the virtual DOM ability to check it and trigger re-renderings when they’re needed.

We also have local state inside each stateful component to manage changes allowing the user to change data that is propagated via props.

When we want to abstract a little bit more, we can use [Redux](https://redux.js.org/) to abstract state or props to an “external” store, a single source of truth — if you haven’t read my article about [How to get the ball rolling with Redux in ten minutes](https://www.freecodecamp.org/news/redux-get-the-ball-rolling-in-10min-9d9551ff4b3c/), feel free to do it!

Even with all these tools in the tool belt it can be cumbersome to handle some type of data (props, state, whatever) inside our application.

**Imagine current authenticated user info**, **themes**, **locale️ o**r **even language r**ela**ted data.**

**This is information that is considered to be “global” in a tree of React components. Once you change this info, all the application should re-render to get up-to-date with it.**

**Context is designed to share data that can be considered **“global”.****

**So, to understand this, let’s get our hands dirty! If you want you can pull my GitHub repo [here](https://github.com/evedes/context-api) and play a bit with these things we’re going to do:**

### **01. Getting Our Hands Dirty**

**Let’s build an App, which has a Dashboard.**

**Inside the Dashboard there’s a Widget which renders a Themed Button.**

**The Themed Button allows the user to change the App Theme.**

**Something like this:**

![Image](https://cdn-media-1.freecodecamp.org/images/6MtkhVhYrMlECQeAxuheRqIg3KoaxjSdyXXn)
_Image of the App_

**So, let’s start with our App component:**

![Image](https://cdn-media-1.freecodecamp.org/images/2EqqvPMMI15R9OCIkgOlUl8sdQvtGJ4TGcVr)
_App Component_

**This component has a state, a `changeTheme` method and a render which renders the `<Dashboard` /> Component.**

![Image](https://cdn-media-1.freecodecamp.org/images/oSyRro0zLaTZDxeupfrGsEbvDC0sQnWJkNFH)
_Dashboard Component_

**Dashboard Component receives props and renders a Widget Component passing the `changeTheme` and theme props.**

![Image](https://cdn-media-1.freecodecamp.org/images/4c8zM8aEJ-X8Z97TM5KZV5r1pITAAPfeebQr)
_Widget Component_

**Widget Component receives props from its parent and renders a Button passing into it `changeTheme` and theme props.**

![Image](https://cdn-media-1.freecodecamp.org/images/DiKuckapUyedtersEvx4XKMlCy114dILkFXP)
_Button Component_

**The Button receives the props from its parent and finally makes use of it rendering a button with a `className` that depends on the theme that was chosen by the user.**

**The Button also allows the user to switch the theme from red to blue and vice-versa. That’s why it has an `onClick` handler which triggers the `changeTheme` method passed top down from App Component -> Dashboard -> Widget -> Button.**

**As you see everyone, this is a lot of props, a lot of complexity, a lot of repeated code, a lot of ?.**

**So, at this moment, you’re asking how can we avoid this? How can we abstract all these theme things and make our code cleaner?**

**The answer for this is making use of the Context API provided by React!!**

### **02. Implementing the Context API**

**Okay, first things first.**

**Let’s take all the theme related complexity outside of our main App Component.**

![Image](https://cdn-media-1.freecodecamp.org/images/ezlk3BhbsT4QLsjJobmLVFMF9ztfb7U1sGGG)
_ThemeContext and ThemeProvider_

**To do this we’ve started by creating a `ThemeContext` using the `React.createContext()`.**

**Then we’ve created a stateful component called `ThemeProvider` which will handle the state, the `changeTheme` method which is specific to this theming concern.**

**In the render method we’ll return the <ThemeContext.Provider> with the `value` props which self-contains whatever we want to propagate. This Component will embrace the { this.props.children } using the render props pattern.**

> **By the way, if you want to know more about the render props pattern don’t miss my article about it [here](https://medium.freecodecamp.org/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053).**

**This way we can inject into everything that the <ThemeProvider /> embraces the value props with our state and changeTheme method.**

**Okay, next step is to clean all the props ? we’ve passed in our top down parent to child flow and, very important, to wrap the return of our App Component in our <ThemeProvider/> component — this will give “context” to our App ?.**

![Image](https://cdn-media-1.freecodecamp.org/images/RTL2t1GEAdEdAni6TwyC6SPN6LHF815ZyXzX)

**It’s so much cleaner now, everyone! ❤️ I’m so happy with this! ?**

**Let’s focus on our Button Component:**

![Image](https://cdn-media-1.freecodecamp.org/images/IeENT3TT5mmn6El3raVFbw2PSDuw8f4XayxP)

**Well, here we’ve just connected the <ThemeContext.Consumer> Component and inside of it we’ve passed a function to be rendered as a child with the context.**

**For those of you who aren’t aware this <> </> notation is the same as doing<React.Fragment>;</React.Fragment>.**

### **03. Conclusion**

**I had so much fun with this, everyone! We’ve been able to encapsulate all the theming logic inside a proper component called <ThemeProvider>.**

**We’ve injected the context where we needed it. In this case it was in the <App> Component but it could be done anywhere above the place we want to consume the data.**

**In the end, we’ve consumed the data at the required point. In this case it was in a Button Component.**

**We’ve cleaned our app from all the top-down props flow.**

**It’s a win-win, my friends! ?**

**Thank you very much, and always remember to _“Be Strong and Code On!”_ ?**

### **04. Bibliography**

**01. [React Documentation](https://reactjs.org/docs/getting-started.html)**

**evedes, Jan2019**

