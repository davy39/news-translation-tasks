---
title: React Background Image Tutorial – How to Set backgroundImage with Inline CSS
  Style
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2020-12-14T16:03:20.000Z'
originalURL: https://freecodecamp.org/news/react-background-image-tutorial-how-to-set-backgroundimage-with-inline-css-style
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/fcc-bg-image-2.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'There are four ways to set a backgroundImage style property using React''s
  inline CSS.

  This tutorial will show you all four methods, with code samples for each.

  Here''s an Interactive Scrim of Setting a Background Image with React



  How to Set a Backgr...'
---

There are four ways to set a `backgroundImage` style property using React's inline CSS.

This tutorial will show you all four methods, with code samples for each.

### Here's an Interactive Scrim of Setting a Background Image with React

<iframe src="https://scrimba.com/scrim/co9b0447ba3a6a610fe96f96b?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## How to Set a Background Image in React Using an External URL

If your image is located somewhere online, you can set the background image of your element by placing the URL like this:

```jsx
function App() {
  return (
    <div style={{ 
      backgroundImage: `url("https://via.placeholder.com/500")` 
    }}>
      Hello World
    </div>
  );
}
```

The code above will render a single `<div>` element with the style `background-image: url([https://via.placeholder.com/500](https://via.placeholder.com/500))` applied into it.

## How to Set a Background Image in React From Your /src Folder 

If you bootstrap your application using Create React App and have your image inside the `src/` folder, you can `import` the image first and then place it as the background of your element:

```jsx
import React from "react";
import background from "./img/placeholder.png";

function App() {
  return (
    <div style={{ backgroundImage: `url(${background})` }}>
      Hello World
    </div>
  );
}

export default App;
```

When you run the `npm start` command, React will show a "Failed to Compile" error and stop the build when the image is not found:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/React-failed-to-compile-image.png)
_React failed to compile. The image is not found._

This way, you won't show any broken image links on your web app. In the code above, the value of `backgroundImage` is set using a template string, which allows you to embed JavaScript expressions.

## How to Set a Background Image in React Using the Relative URL Method

The `public/` folder in Create React App can be used to add static assets into your React application. Any files you put inside the folder will be accessible online.

If you put an `image.png` file inside the `public/` folder, you can access it at `<your host address>/image.png`. When running React in your local computer, the image should be at `http://localhost:3000/image.png`.

You can then assign the URL relative to your host address to set the background image. Here's an example:

```jsx
<div style={{ backgroundImage: "url(/image.png)" }}>
  Hello World
</div>
```

By setting the URL path to `/image.png` like the example above, the browser will look for the background image at `<your host address>/image.png`.

You can also create another folder inside `public/` if you want to organize your images into folders. For example:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen-Shot-2020-12-14-at-20.18.30.png)
_Creating an img/ folder inside public/ folder_

Don't forget to adjust the `backgroundImage` value to `url(/img/image.png)` if you decide to create the folder.

## How to Set a Background Image in React Using the Absolute URL Method

You can also include the absolute URL by using Create React App's `PUBLIC_URL` environment variable like this:

```jsx
<div style={{ 
  backgroundImage: `url(${process.env.PUBLIC_URL + '/image.png'})` 
}}>
  Hello World
</div>
```

When you run this on your local computer, React scripts will handle the value of the `PUBLIC_URL` value. When you run it locally, it will look like a relative URL instead of absolute URL:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/absolute-url-background-image-1.png)
_Absolute URL of the image is not shown in local computer_

The absolute URL will only be seen when you deploy React into production application later.

## How to Set a Background Image with Additional Properties

If you want to customize the background image further, you can do so by adding additional properties after the `backgroundImage`. Here's an example:

```jsx

<div style={{ 
  backgroundImage: `url(${process.env.PUBLIC_URL + '/image.png'})`,
  backgroundRepeat: 'no-repeat',
  width:'250px' 
}}>
  Hello World
</div>
```

The properties set above will add `background-repeat: no-repeat` and `width: 250px` together with the `background-image` style to the `<div>` element.

Thank you for reading. If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

