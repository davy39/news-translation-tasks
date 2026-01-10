---
title: Shining a Spotlight on Error Boundaries in React 16
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:35:51.000Z'
originalURL: https://freecodecamp.org/news/shining-a-spotlight-on-error-boundaries-in-react-16-caed07453b22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fQhvR9UVrNLee-95ZCNcXQ.jpeg
tags:
- name: coding
  slug: coding
- name: error handling
  slug: error-handling
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mae Capozzi

  React 16 has better error handling than previous React versions. If an error occurred
  inside of a component, it would “corrupt React’s internal state.” Then, we would
  end up with “cryptic” error messages, or just a blank screen. React ...'
---

By Mae Capozzi

React 16 has better error handling than previous React versions. If an error occurred inside of a component, it would “[corrupt React’s internal state](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html).” Then, we would end up with “cryptic” error messages, or just a blank screen. React lacked a way to expressively and eloquently handle these errors.

That has changed in React 16, thanks to Error Boundaries. [The React Docs](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) explain how they work:

> Error boundaries are React components that **catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI** instead of the component tree that crashed.

I’ve developed a real-life scenario that can describe how Error Boundaries work:

### A Real Life Scenario

Imagine that you are a parent at a swimming pool, and you have one child. The swimming pool represents the app, you represent a Parent component, and your child represents a Child component.

There’s also a lifeguard, who represents an Error Boundary component.

At the pool, your child is jumping off of the diving board, along with their friends, (any third-party like a user, a library, or an HTTP request).

![Image](https://cdn-media-1.freecodecamp.org/images/NthYEZyaGRw2rAq36wM61oVrC6zLMeeP2Nkx)

You’re tanning when your child falls off of the diving board and hits her leg.

Without a lifeguard, you’d never know what caused your child to fall. Did her friends push her? Was the board slippery? Did she suddenly become unconscious?

Because this is React 16, the lifeguard has been watching everything ensue. After rescuing your child, the lifeguard can tell you exactly what happened. In this case, her friend pushed her off of the diving board.

Now, it’s easy to tell what actually caused the error. The establishment that owns the swimming pool (the developer), can now easily mitigate future risk by making sure only one person stands on the diving board at a time.

### Step 1: Spin up a React application using create-react-app

We’ll start by spinning up a React application using create-react-app. If you haven’t done this before, I’ve written up a [cheatsheet](https://gist.github.com/maecapozzi/41e249c24e683647babf451c675b22c8) that you can follow. If you need a bit more guidance, you can follow the instructions in [Tutorial: How to Make HTTP Requests in React, Part 1.](https://hackernoon.com/tutorial-how-to-make-http-requests-in-react-part-1-f7afa3cd0cc8)

Once you’ve set up your application and know that it runs locally, we can get started with the actual coding.

### Step 2: Start building out components

I’ve removed a lot of the boilerplate code that `create-react-app` includes, so my `App.js` file looks like this:

```
import React, { Component } from 'react'import './App.css'
```

```
class App extends Component {  render () {    return (      <div className='App'>              <h1>Hello World</h1>      </div>        )  }}
```

```
export default App
```

You can feel free to copy/paste my code into your `App.js` file, so that we can make sure we are on the same page! When you check in your browser, you should see “Hello World” in big letters.

Create a new file called `Parent.js` and copy/paste this code into that file:

```
import React from 'react'import Child from './Child'
```

```
const Parent = () =&gt; (  <div>    <h1>Parent</h1>    <Child />  </div>)
```

```
export default Parent
```

Then, create another file called `Child.js` and copy/paste this code into **that** file:

```
import React, { Component } from 'react'
```

```
class Child extends Component {  constructor () {    super()  }
```

```
  render () {    return (      <div>        <h3>Child</h3>      </div>    )  }}
```

```
export default Child
```

Normally, if I were building a component like this, I’d use a stateless functional component. The only reason I am not is because I want to throw an error in my constructor for example purposes.

Now, let’s import the `Parent` component into the `App.js` file, and display it on the page. Your `App.js` file will look like this:

```
import React, { Component } from 'react'import Parent from './Parent'
```

```
import './App.css'
```

```
class App extends Component {  render () {    return (      <div className='App'>        <Parent />      </div>    )  }}
```

```
export default App
```

On your screen, you should see this:

![Image](https://cdn-media-1.freecodecamp.org/images/pIuDTagXiJleGofowvb-V9cv1UcHk03QnUfM)

### Step 3: Throw an error in the Child component

Now, I’m going to throw an error in the constructor of our `Child` component so that we can see what happens when we get that kind of error when we aren’t using Error Boundaries.

In `Child.js` add `throw new Error('This is an error')` to your `constructor` function.

```
constructor () {  super()   throw new Error('This is an error')}
```

If we refresh our page, we’ll see an error message like this in development:

![Image](https://cdn-media-1.freecodecamp.org/images/-DdczflKjbNCKMDkesEj5AR3gpDJIn-KO3LM)

If we remove the error by clicking the ‘x’ in the upper right corner, all we see is a blank screen!

### Step 4: Build an Error Boundary component

Here’s an example of an Error Boundary component:

```
import React, { Component } from 'react'  class ErrorBoundary extends Component {  constructor (props) {    super(props)    this.state = { hasError: false }  }
```

```
  componentDidCatch (error, info) {    this.setState({ hasError: true })  }
```

```
  render () {    if (this.state.hasError) {      return <h1>Something went wrong.</h1>    }
```

```
    return this.props.children  }}
```

```
export default ErrorBoundary
```

Let’s walk through how this component works:

1. In the constructor, I set an attribute on `state` called `hasError`. I initialized it to `false`.
2. I use the `componentDidCatch` lifecycle method, which can take two arguments, `error` and `info`.   
If `componentDidCatch` is triggered, I set the state of `hasError` to `true`.
3. In the `render` method, I say that `if hasError` is `true`, let the user know that “`**Something went wrong**`.”   
`Else`, continue to operate as usual.

### 4. Set the Error Boundary

Finally, we need to set the Error Boundary around the component that is throwing the error.

In this case, the `Child` component is throwing the error, so we need to set the boundary around it, inside of the `Parent` component.

```
import React from 'react'import Child from './Child'import ErrorBoundary from './ErrorBoundary'
```

```
const Parent = props =&gt; (  <div>    <h1>Parent</h1>    <ErrorBoundary>      <Child />    </ErrorBoundary>  </div>)
```

```
export default Parent
```

Now, if we refresh the page, we’ll see this error in development, like we did before:

![Image](https://cdn-media-1.freecodecamp.org/images/Yd88gvxtLedqaMLNzDcpEZwevQkOhwpML3td)

The difference is that if we click out of the error, we see this on the page instead:

![Image](https://cdn-media-1.freecodecamp.org/images/fC8w6endl647qpQrgcBmg40CNOGvyVoZ57hF)

That’s a lot better than just a blank screen!

Please let me know if you have any questions in the comments section below.

? I**_f you liked this post,_** m**_ake sure to f[ollow me on medium,](https://medium.com/@MCapoz) f[ollow me on twitter,](https://twitter.com/MCapoz) and support me on P[atreon!](https://www.patreon.com/maecapozzi)?_**

