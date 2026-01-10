---
title: How to optimize React applications with Lazy Loading ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-13T17:40:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-react-applications-with-lazy-loading-232183e02768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_x1W90t0HLSSGGfngWqUA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Al-amin Nowshad

  For your components, images, and what not


  Lazy loading is an old technique to optimize web applications as well as on mobile
  apps. The thing is pretty straight forward - do not render things if they are not
  viewed or required at t...'
---

By Al-amin Nowshad

#### For your components, images, and what not

![Image](https://cdn-media-1.freecodecamp.org/images/sjshSrV2O2h-aKvcWEDi-XRIW4QF14nZEAQW)

Lazy loading is an old technique to optimize web applications as well as on mobile apps. The thing is pretty straight forward - do not render things if they are not viewed or required at that moment. So, for example, if we have a list of posts to show, we should initially only render what’s on the viewport. That means the rest of the elements will be rendered later on demand (when they’re in the viewport or about to be on the viewport).

### Why Lazy Loading?

Most of the times our users don’t see the whole web page, at least in the beginning. No matter how our application UI has been structured, there are certain components the user might not need initially or ever!

In these cases, rendering those components not only harms our application’s performance but also wastes a lot of resources (especially when they have images or similar data hungry contents).

So, loading or rendering those components on demand seems to be a more efficient decision. It can improve the application’s performance, and at the same time can save us a lot of resources.

### How?

We’re going to make a sample application where we can apply lazy loading. First, we need to initialize our React application using `create-react-app` with the commands below:

```
create-react-app lazydemocd lazydemonpm run start
```

This might take a few minutes to initialize and open our react application in browser’s `3000` port by default.

> If you don’t have `create-react-app` installed on your pc, you can install with the command: `npm install -g create-react-app`

Now, we’re gonna make a list that’ll show some random posts. So, let’s get some dummy data first. Create a file named `data.js` inside `src` folder of our project. I’ve just copy-pasted the `json` response from this `JSON` placeholder endpoint [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts). You can create your own dummy data too. Following the format below should be sufficient for this tutorial:

![Image](https://cdn-media-1.freecodecamp.org/images/nYsUwBXnStTJouo42YP5z4dXoK7dCp-XY6tk)
_data.js format_

Let’s replace `App.js` file’s content with the code below:

![Image](https://cdn-media-1.freecodecamp.org/images/70Q5LEimL51EiG1d0FA-RZZRVuDxVyIrSzbU)

![Image](https://cdn-media-1.freecodecamp.org/images/N3MLdKVosCniJCyyJ1LUx480I7Di4xdbWxCq)

Here, we are simply making a list of `posts` with their `title` and `body`. And with some simple `CSS` modifications we get the view on the right. Here’s the full list renders at once. Now, if we don’t wanna render everything initially, we should apply `lazy loading`. Let’s install it in our project:

Source: [twobin](https://github.com/twobin)/[react-lazyload](https://github.com/twobin/react-lazyload)

```
npm install —-save react-lazyload
```

Now, let’s update `App.js` file by importing and applying `lazyload`.

![Image](https://cdn-media-1.freecodecamp.org/images/w663tm74X4xB8g8SV8XWm0KxAIjBZ0kMAV6R)

Using `react-lazyload` is pretty straight forward, just wrap the component with `<LazyLoad …> … </`LazyLoad>. Here we are using a placeholde`r component` <Loading /`> tha`t’ll show Loading… till the component has loaded. We can also `set th`e eff`ective` height `and offs`et of the LazyLoad component. You can find more details on t[he documentation: https://github.com/twobin/rea](https://github.com/twobin/react-lazyload#height)ct-lazyload#height

Now, all of the posts are not being rendered initially. Only a few will be rendered initially depending on the viewport. But, as the contents are textual till now, the effect can be hardly realized unless we inspect and see the DOM’s changing when they move from `loading` to `loaded`.

To make our lazy loading more effective let’s incorporate images inside posts. We’ll use [Lorem Picsum](https://picsum.photos/) for our photos. Our updated `Post` component should look like below:

![Image](https://cdn-media-1.freecodecamp.org/images/Hxs73x97zu9teR7f2SIwbr6VmmrKVegHz2qe)

> Lorem Picsum url format  
> https://picsum.photos/id/[image_id]/[width]/[height]

![Image](https://cdn-media-1.freecodecamp.org/images/ge5QAy8G1wGFa7jAiFSlQrAQj3AyQVK4FPsC)
_The result after inserting images with posts_

Now, as I said earlier, images are data hungry components of a webpage and here we are loading images for each post. Though the whole component is lazy loaded and image also gets loaded with the component, the image loads a bit late and not so smoothly. So, we can make a better image loading experience for our user’s using LazyLoad for individual images.

The technique is to load a very low-quality image as a placeholder and then the original image gets loaded. So, the final `App.js` would look like —

![Image](https://cdn-media-1.freecodecamp.org/images/mSb4ic759dFRZMUv90WFKHA73C1rTei-yn89)

Now we can `scroll` the list with our `inspect element open` to see how these components change when they come near to the viewport then gets rendered and the placeholder gets replaced by actual contents.

And we are done, for now, our LazyLoad is working with all its grace. That was pretty easy!!!

![Image](https://cdn-media-1.freecodecamp.org/images/DSefnSg0oR-EoUpD0QlKsTPVc6yfX1mztNKR)

> The image LazyLoad here is not the best use case as it’s already handled by the component LazyLoad. But, the technique can be very useful in other use cases where we have to show a lot of images. Try disabling the LazyLoad on Post component but keep the image LazyLoad, you can see its effect.

Github: [https://github.com/nowshad-sust/lazydemo](https://github.com/nowshad-sust/lazydemo)

React LazyLoad: [twobin](https://github.com/twobin)/[react-lazyload](https://github.com/twobin/react-lazyload)

