---
title: Clever React context tricks using Typescript — not Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T16:32:26.000Z'
originalURL: https://freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*P698jwSEpcmSgYYS
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Bill Girten

  by Bill Girten, Martin Maza, and Alison Stuart


  TLDR; Leverage React’s Context API as a light and powerful alternative to Redux.

  Let’s face it: when we first started to play with React, it was like a sugar rush.
  Just create a .jsx file...'
---

By Bill Girten

by [Bill Girten](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined), Martin Maza, and [Alison Stuart](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined)

![Image](https://cdn-media-1.freecodecamp.org/images/-rYMEN2Cedi7XnC9ruyiJK5U3gztNeyKN1cO)

**TLDR;** Leverage [React’s Context API](https://reactjs.org/docs/context.html) as a light and powerful alternative to Redux.

Let’s face it: when we first started to play with React, it was like a sugar rush. Just create a .jsx file, add a couple of dependencies, and Wham-O! — lightning-quick pages.

That’s when the excitement begins.

Next thing you know, you feel limitless as you engineer the presentation layer of your application at jet-speed. Then you get this crazy idea to make an AJAX call to some microservice and manage the state of the app.

That’s when the pain begins…

So you search Al Gore’s amazing Internet and find out the go-to solution to manage the app’s state is [Dan Abramov](https://www.freecodecamp.org/news/clever-react-context-tricks-using-typescript-not-redux-7e2b9c7e5bf6/undefined)’s [Redux](http://www.redux.js.org). Now you’re learning about Actions, Reducers and Stores and diving into [ImmutableJS](https://facebook.github.io/immutable-js/) just so you can manage state. After you mapStateToProps, your React component is typically engaged in what is popularly termed “[prop drilling](https://blog.kentcdodds.com/prop-drilling-bb62e02cb691)”.

Initially, you’re okay with passing down properties from parent to child and, at times, to grandchild. However, as the application becomes more complex you notice that sometimes you are passing some properties through the component tree that are _not used_ by a given descendant component.

Now what?!? You want to be able to manage the app’s state, _but_ you want to do so without passing properties through the hierarchy. It’s time for some clever tricks.

### **How the React Context API helps**

Facebook released the Context API in React v16.3 as a mechanism to pass the app’s assets through a Provider to _any_ child component listening as a Consumer. This eliminates the “prop drilling” paradigm. Imagine: at _any_ level, a parent component could define its own state (including methods) and provide them directly to any participating consumer. Additionally, you can set state by using the methods passed in by the Context’s Provider.

![Image](https://cdn-media-1.freecodecamp.org/images/Sv7YltnxU2uwL3G0F6L7uao9zxxqgxH5BQq5)
_Fig. 2 — React Context API can reduce or eliminate the need for “Prop Drilling” image source: [The JavaScript Playground](https://javascriptplayground.com/context-in-reactjs-applications/" rel="noopener" target="_blank" title=")_

We’ll show you how to do this in the example below.

**Let’s Roll!**

[**bgirten/clever-React-Context-tricks**](https://github.com/bgirten/clever-React-Context-tricks.git)  
[_new React Context experimments. Contribute to bgirten/clever-React-Context-tricks development by creating an account on…_github.com](https://github.com/bgirten/clever-React-Context-tricks.git)

![Image](https://cdn-media-1.freecodecamp.org/images/ncb0PHxVEZansTJLq54nCpdC0IjgFpKxMQlA)

We begin by creating an “initial” State object which will be passed from the App component to the child components. Notice that this initialState also includes methods. This approach provides the capability of defining methods only once, so you can reuse them more easily.

![Image](https://cdn-media-1.freecodecamp.org/images/TpDU-j9zv5qwz9b14pNoVSaDSf0gVPUdRSNr)

Pass the initial State into the App component and provide a Context. Every component enclosed in the MyContext.Provider tag will have the capability of consuming the context (which in this case includes the initial state of the App component).

![Image](https://cdn-media-1.freecodecamp.org/images/Bt0AuoHrGBFLvqfXRUMmhS0rYp4vrUEG2J25)

Bypass the “prop drilling” from the child component to grandchild component.

![Image](https://cdn-media-1.freecodecamp.org/images/fVdLJZKi556Ibbytjb9hww-ZTIDKRpLLE9Zd)

The local method handleFetchEvent provides the capability to execute the method passed by the context (in this case, updateStats). The component’s render method fires off due to this.setState.

On line 21, we consume the incoming Context.Provider, allowing us to access all those members and methods defined in the App component’s initial state.

Even though methods can be passed from higher levels of the DOM tree, we can also invoke re-rendering of the DOM by simply calling the **setState** method directly for a given React component.

![Image](https://cdn-media-1.freecodecamp.org/images/RJiTN1aHJ6qSrFUdqesUU7kKE1mvcD21WZO0)

And here we have the loaded application. Thanks for following along — you can find more awesome content from these authors at:

[Alison’s Github,](https://www.github.com/sedulous-mortal) [Martin’s Github](https://www.github.com/87maza), and [Bill’s Github](https://www.github.com/bgirten)

