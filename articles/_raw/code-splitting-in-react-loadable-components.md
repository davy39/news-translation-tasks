---
title: Code Splitting in React – Loadable Components to the Rescue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-07T20:41:40.000Z'
originalURL: https://freecodecamp.org/news/code-splitting-in-react-loadable-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/david-lezcano-zwCE12DucBo-unsplash-4.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Lusan Das\nCode splitting is a way to split up your code from a large\
  \ file into smaller code bundles. These can then be requested on demand or in parallel.\
  \ \nNow, it isn't a new concept, but it can be tricky to understand.\nWhen you're\
  \ doing code spl..."
---

By Lusan Das

Code splitting is a way to split up your code from a large file into smaller code bundles. These can then be requested on demand or in parallel. 

Now, it isn't a new concept, but it can be tricky to understand.

When you're doing code splitting, it is important to keep the bundle sizes of the HTML, CSS, and JavaScript as small as possible. But often as applications scale larger bundles are unavoidable. And this can negatively affects the [web vitals](https://web.dev/vitals/) for your website.

So in this article we'll see how code splitting works and how you can do it well.

## Code Splitting in a React Codebase

Some common ways to do code splitting are listed below:

### Code splitting using Webpack dynamic import syntax

Check out the example below:

```import(“module_name”).then({ default } => // do something)```

This syntax will let the Webpack file that's to be code split and bundled be generated accordingly. There are also other ways in Webpack like using **manual entry points** and **SplitChunksPlugin**. You can find more information in the [documentation](https://webpack.js.org/guides/code-splitting/).

### Code splitting using React.Lazy and suspense

This is a feature provided directly by React. Let’s dive into the example below from the official documentation itself:

```js
import React, { Suspense } from 'react';

const OtherComponent = React.lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <OtherComponent />
      </Suspense>
    </div>
  );
}
```

This is quite similar to Webpack dynamic import syntax, where the Suspense component can be used to offer a loading state until the component is lazy loaded.

I explored this in another article where I talked about [The future of React, unfolding with Suspense](https://blog.logrocket.com/the-future-of-react-unfolding-with-suspense/).

## When to Use Code Splitting in React

The only drawback about code splitting is that you can only use it in client side rendering.

Both the above techniques won’t work during server side rendering when it comes to React 🥺.  This is the reason why the React team recommends using loadable components for code splitting in the server.

## But why use loadable components?

I hear and feel you. It took me a while to figure it out as well.

Let’s dive into an example.

Let's go back to our initial problem statement: we would like to do code splitting during server side rendering (SSR). The best tool we have in our arsenal so far is the dynamic import syntax by Webpack which we briefly talked about in the above section. 

So we will build a component called **AsyncComponent** whose responsibility is to accept modules and use dynamic imports. 

It will have three states:

* isLoading _// as dynamic import returns a promise_
* Component _// actual module derived from code splitting_
* Error _// for logging in case import failed_

### Expected Behaviour

Our AsyncComponent will accept any import module and resolve it. On success we will set the isLoading state to false and render the resolved component.

Let’s quickly skim the below code as described above:

```js
import React from 'react';


class AsyncComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoading: true,
            component: null,
            error: null
        }
    }

    componentWillMount() {
        const { importModule } = this.props;
        importModule()
            .then((module) => {
                const component = module.default;
                console.log(component)
                this.setState(({
                    component,
                    isLoading: false
                }))
            })
            .catch(err => {
                console.log(error)
                this.setState({
                    isLoading: false,
                    error
                })
            })
    }

    render() {
        const { isLoading, component, error } = this.state;

        if(isLoading) {
            return <div>Loading</div>
        }
        if(error) {
            return <div>{error}</div>
        }
        return <div>{component}</div>
    }
}

const A = () => {
    return (
        <div>
            <AsyncComponent importModule={() => import('./F')} />
        </div>
    )
}

// We keep a reference to prevent uglify remove

export default A
```

### Actual Behaviour

But this won’t work. Since we are trying to do this on the server side, the React render lifecycle won’t wait for the dynamic import to resolve, which is a promise. So we will be stuck on the loading screen, which is evident from the screenshot below from the experiment I performed.

![Image](https://lh5.googleusercontent.com/dC4gCS9bG_07BiEbljwNtEWu_ODXXizy8geQ45XqmNJLEcl_KlliePS3niWZnrNSnpSR1qwFNNuw4h91iyN-_xRgTIZ8WWrDlTR5ruUm1pu2SuRl_v6xlbiuWb6zJepfoxYi_UnT)

This is why code splitting in React is not straightforward when we try to do it simply with our available tools.

## Enter Loadable Components in React

To solve this problem, we have [loadable components](https://loadable-components.com/docs/server-side-rendering/), a library recommended by the official react docs. 

I won't get into the configuration part, as the official documentation has enough examples and steps that cover what you need to know. Let’s look at it from a code perspective.

```js
import React from 'react';
import loadable from '@loadable/component';

const F = loadable(() => import('./F'))

const A = () => {
    return (
        <div>
            {/* <AsyncComponent importModule={() => import('./F')} /> */}
            <F />
        </div>
    )
}

// We keep a reference to prevent uglify remove

export default A
```

In our current example, we have replaced **AsyncComponent** with a **loadable component.**

**Violà – it works!** 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/viola.png)

It is indeed a complex problem to solve, but loadable components make it look easy. And the documentation is just as easy to follow as well!

The babel loadable plugin transpiles the loadable syntax in components and prepares the final string for the HTML during server side rendering and the dynamic import syntax during client side rendering. 

Note that loadable components can be used for code splitting in both client and server with the help of an SSR flag which can be turned on/off.

## Conclusion

I wrote this article to talk about why loadable components are important and what problems they solve. I also wanted to convey why code splitting is complicated during server side rendering. I really hope this helped you understand the problem.

> _Special mention to [Kashyap](https://twitter.com/kgrz) who helped me understan_d _the concept._

Follow me on [Twitter](https://twitter.com/daslusan) to get more updates regarding new articles and to stay updated in the latest frontend development. Also, share this article on Twitter to help others know about it. Sharing is caring ^_^.

### Resources

* [https://loadable-components.com/docs/server-side-rendering/](https://loadable-components.com/docs/server-side-rendering/)
* [https://webpack.js.org/guides/lazy-loading/](https://webpack.js.org/guides/lazy-loading/)
* [https://webpack.js.org/guides/code-splitting/](https://webpack.js.org/guides/code-splitting/)
* [https://reactjs.org/docs/code-splitting.html](https://reactjs.org/docs/code-splitting.html)

Here are some other articles I written that you might find interesting:

1. [The future of React, unfolding with Suspense](https://blog.logrocket.com/the-future-of-react-unfolding-with-suspense/)
2. [The Story of requesting twice — CORS](https://www.freecodecamp.org/news/the-story-of-requesting-twice-cors/)
3. [How to use Redux Persist when migrating your states](https://www.freecodecamp.org/news/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead/)
4. [Redux Observable to the resque](https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2)
5. [Building webapp for the future](https://codeburst.io/building-webapp-for-the-future-68d69054cbbd)

  

