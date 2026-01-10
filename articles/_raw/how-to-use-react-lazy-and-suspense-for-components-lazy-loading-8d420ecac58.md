---
title: How to use React.lazy and Suspense for components  lazy loading
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T18:17:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-lazy-and-suspense-for-components-lazy-loading-8d420ecac58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F8lEWMyFHCnZLxcUUofs-w.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Boris Sever

  React 16.6 brought code-splitting to a new level. You can now load your components
  when it’s really needed without installing additional libraries.

  What are code-splitting and lazy loading?

  Webpack defines code-splitting as:


  “techniqu...'
---

By Boris Sever

React 16.6 brought code-splitting to a new level. You can now load your components when it’s really needed without installing additional libraries.

### What are code-splitting and lazy loading?

Webpack defines code-splitting as:

> “technique of splitting your code into various bundles which can then be loaded on demand or in parallel”. [[Source](https://webpack.js.org/guides/code-splitting/)]

Another way to say: “loading on demand or in parallel” is **lazy-loading**.  
Opposite of lazy-loading is **eager-loading**. Here everything is loaded no matter if you use it or not.

### **Why would we use code-splitting and lazy loading?**

Sometimes we have to introduce a big chunk of code to cover some functionality. This code can be importing 3rd party dependency or writing it on our own. This code then affects the main bundle’s size.

Downloading a few MBs is a piece of cake for today’s internet speed. We still have to think about the users with a slow internet connection or using mobile data.

### How was it done before React 16.6?

Probably the most popular library for lazy loading of React components is `[react-loadable](https://github.com/jamiebuilds/react-loadable).`

It’s important that reactjs.org still recommends `_react-loadable_` if your app is rendered on the server. [[Source](https://reactjs.org/docs/code-splitting.html#reactlazy)]

`react-loadable` is actually pretty similar to the new approach by React. I will show this in the following demo.

### Is anything needed for setup?

Let's see what reactjs.org has to say about it:

> “If you’re using [Create React App](https://github.com/facebookincubator/create-react-app), [Next.js](https://github.com/zeit/next.js/), [Gatsby](https://www.gatsbyjs.org/), or a similar tool, you will have a Webpack setup out of the box to bundle your app.

> If you aren’t, you’ll need to setup bundling yourself. For example, see the [Installation](https://webpack.js.org/guides/installation/) and [Getting Started](https://webpack.js.org/guides/getting-started/) guides on the Webpack docs.“  
> - reactjs.org

Ok, so _Webpack_ is required, which handles dynamic imports of the bundles.

The following demo is generated using `Create React App.` And in that case, _Webpack_ is already configured and we’re ready to go.

### DEMO

For this demo, we will use `[react-pdf](https://github.com/diegomura/react-pdf)`. `react-pdf` is an awesome library used for creating PDF files on the browser, mobile, and server. We could generate a PDF on the server, but if we would rather do it on the client side, it comes with a cost: bundle size.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0onue7-IifphjgL0RE2c8A.png)
_Importing cost_

> _I’m using [Import cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) extension for Visual Studio Code to see the sizes of the libraries used._

Let's say our requirement is to generate a PDF file when a user clicks on the button.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C34cqIMAunhY76drcatFBQ.png)

Now, this is a simple form with only one use case. Try to imagine a huge web app where this is a fraction of possibilities. Maybe this functionality is not used very often by the users.

Let’s put ourselves into that situation. PDF generation isn’t used very often and it doesn’t make sense to load the whole code for every page request.

I’ll try to show how we can develop a solution with lazy loading and without it.

### Eager VS lazy loading showcase

For both cases, we will use one component which imports dependencies from `react-pdf` and renders a simple PDF document.

Nothing spectacular going on here. We import`PDFViewer`, `Document`, `Page`, `Text`, `View` from `react-pdf`. These are all used in `render` method of `PDFPreview` component.

`PDFPreview` receives only one `prop` called `title`. As the name implies, it is used as a title in a newly generated PDF file.

_pdfStyles.js_ looks like this:

### **Eager loading**

Let’s first see how the parent component without lazy loading could look like:

which renders the following view in the browser:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fz_R39qnUqjqOMtq5SyvRw.png)

Let's go through the code together:

On line 2 we import `PDFPreview` component.

On line 6 we initialize the state with default values. `name` is a field used as a title in the PDF file, while field `PDFPreview` is a boolean which shows or hides `PDFPreview`.

Now, let's jump to `render` method and check what will be rendered.

On line 19 and 25 we render an input and a button. When user types into the input, `name` in the state is changed.

Then when a user clicks on the “Generate PDF ”, `showPDFPreview` is set to `true`. The component re-renders and shows the`PDFPreview` component.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5IqztqRaIWMApDWog8evAw.png)

Even though we use `PDFPreview` only on user click, all code related to it is included in the app bundle:

![Image](https://cdn-media-1.freecodecamp.org/images/1*V7QyCEgy1viNzQ90XlafKg.png)

> _This is a development environment. In production, the sizes would be significantly smaller. Still, we’re not splitting the code optimally._

### **Lazy loading**

We’ve only made small changes and let's go through them.

Line 2 is replaced with:  
 `const LazyPDFDocument = React.lazy(() => import("./PDFPreview"`));

Let's see what the React docs say about React.lazy:

> `_React.lazy_` _takes a function that must call a dynamic `import()`. This must return a `Promise` which resolves to a module with a `default` export containing a React component._   
> _- reactjs.org_

On line 27 we use `Suspense`, which must be a parent of a lazy-loaded component. When `showPDFPreview` is set to true, `LazyPDFDocument` is starting to load.

Until the child component is resolved, `Suspense` shows whatever is provided to `fallback` prop.

The end result looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HzJpB-2aFBdlYflup1d5PA.gif)

We can see _0.chunk.js_ weights significantly less than before and _4.chunk.js_ and _3.chunk.js_ are loaded on button press.

### Conclusion

Every time we are introducing a new dependency into our project, our responsibility is to evaluate its cost and check how it affects the main bundle.

Then we have to ask is this functionality going to be used rarely and can we load it on demand without sacrificing the user experience.

If the answer is yes, then `React.Lazy` and `Suspense` really help us with that task.

Thank you for reading! Please share it with anyone who might find it useful and leave feedback.

