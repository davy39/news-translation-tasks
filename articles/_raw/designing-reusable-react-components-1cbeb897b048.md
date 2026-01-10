---
title: Designing Reusable React Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-30T17:10:37.000Z'
originalURL: https://freecodecamp.org/news/designing-reusable-react-components-1cbeb897b048
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CByHyzJRQR6G8aiAkdFwcQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  What Legos Can Teach Us About Reuse in React Apps

  React is a component library. So React makes it easy to break your UI down into
  composable pieces. The question is, how granular should the pieces be?

  Let’s consider a specific example t...'
---

By Cory House

#### What Legos Can Teach Us About Reuse in React Apps

React is a component library. So React makes it easy to break your UI down into composable pieces. The question is, [how granular should the pieces be](http://sethgodin.typepad.com/seths_blog/2017/12/granularity.html)?

Let’s consider a specific example that I explored in a [previous post](https://medium.freecodecamp.org/reusable-web-application-strategies-d51517ea68c8).

Imagine your team just deployed a ToDo app, built in React. A month later, another team in your company wants to run your ToDo app within their invoice app, also built in React.

So now you need to run your ToDo app in two spots:

1. By itself
2. Embedded within the invoice app

What’s the best way to handle that? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*S3wRzzFKKlls9bTlSpFfKA.png)

To run your React app in multiple spots, you have three options:

1. **iframe** — Embed the todo app in the invoice app via an <iframe>.
2. **Reusable App Component** — Share the entire todo app via npm.
3. **Reusable UI Component** — Share the todo app’s markup via npm.

Let’s discuss the merits of each approach.

### Approach 1: iFrame

The easiest and most obvious approach is to use an [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) to frame the ToDo app into the invoice app.

But leads to multiple issues:

1. If the two apps display the same data, you risk them getting out of sync.
2. If the two apps use the same data, you end up making redundant API calls to fetch the same data.
3. You can’t customize the iframed app’s behavior.
4. If a different team owns the framed in app, when they push to production, you’re instantly affected.

Bottom-line: Walk way. Avoid iframes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w0YcpMhPGBRBeQ25G9g-iA.jpeg)
_Nope._

### Approach 2: Reusable App Component

Sharing your app via npm instead of an iframe avoids issue #4 above, but the other issues remain. API, auth, and behavior are all baked in. So I don’t recommend sharing full apps via npm either. The level of granularity is too high, so the user experience suffers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tjvQ8XV65JcxIETD53CNDg.jpeg)
_Like Lego blocks, reusable React components should be granular and composable._

### Approach 3: Reusable UI Components

I recommend a more granular approach using two flexible building blocks:

1. “Dumb” React components (Just UI. No API calls inside.)
2. API wrappers

“Dumb” React components are configurable, unopinionated, and composable. They’re reusable UI. When consuming a “dumb” component like this, you are free to provide the relevant data or specify the API calls the app should make.

However, if you’re going to compose “dumb” components, you need to wire up the same API calls for multiple apps. This is where API wrappers come in handy. What’s an API wrapper? It’s a JavaScript file full of functions that make HTTP calls to your API. My team creates API wrappers. We use [Axios](https://github.com/axios/axios) behind the scenes to make the HTTP calls.

Imagine you have a user API. Here’s how to create a user API wrapper:

1. Create a JS file with public functions like getUserById, saveUser, etc. Each function accepts the relevant parameters and uses Axios/Fetch to make HTTP calls to your API.
2. Share the wrapper as an npm package called userApi.

Here’s an example.

```js
/* This API wrapper is useful because it:
   1. Centralizes our Axios default configuration.
   2. Abstracts away the logic for determining the baseURL.
   3. Provides a clear, easily consumable list of JavaScript functions
      for interacting with the API. This keeps API calls short and consistent. 
*/
import axios from 'axios';

let api = null;

function getInitializedApi() {
  if (api) return api; // return initialized api if already initialized.
  return (api = axios.create({
    baseURL: getBaseUrl(),
    responseType: 'json',
    withCredentials: true
  }));
}

// Helper functions
function getBaseUrl() {
  // Insert logic here to get the baseURL by either:
  // 1. Sniffing the URL to determine the environment we're running in.
  // 2. Looking for an environment variable as part of the build process.
}

function get(url) {
  return getInitializedApi().get(url);
}

function post(url, data) {
  return getInitializedApi().post(url, data);
}

// Public functions
// Note how short these are due to the centralized config and helpers above. ?
export function getUserById(id) {
  return get(`user/${id}`);
}

export function saveUser(user) {
  return post(`user/${user.id}`, {user: user});
}
```

On my team, we share our React components and API wrappers as [private packages on npm](https://www.npmjs.com/pricing), but [Artifactory](https://jfrog.com/artifactory/) is a nice alternative.

These Lego blocks give us the foundation for quickly building new solutions out of reusable pieces.

> A highly composable system provides components that can be selected and assembled in various combinations to satisfy specific user requirements. — [Wikipedia](https://en.wikipedia.org/wiki/Composability)

So ideally, your “dumb” reusable UI component is composed of [other reusable components, also shared on npm](https://app.pluralsight.com/library/courses/react-creating-reusable-components/table-of-contents)!

With reusable React components and API wrappers published to npm, it’s trivial to build something awesome.

It’s like snapping Lego pieces together. ?

%[https://www.youtube.com/watch?v=Ki2C05my2K4&feature=youtu.be]

I explore the merits and downsides of the approaches above in more detail [here](https://medium.freecodecamp.org/reusable-web-application-strategies-d51517ea68c8). And I recently published a comprehensive course on [Creating a Reusable React Component Library on Pluralsight](http://bit.ly/legoreactps). ?

Have a different approach you enjoy? Chime in via the comments.

### Looking for More on React? ⚛️

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight ([free trial](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) is the author of [multiple courses on JavaScript, React, clean code, .NET, and more on Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect, Microsoft MVP, and trains software developers internationally on front-end development practices. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

