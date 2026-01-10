---
title: A quick guide to learn React and how its Virtual DOM works
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vQXljCx6DN_aNLWD.jpg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jérémy Bardon


  This is part of my “React for beginners” series on introducing React, its core features
  and best practices to follow. More articles are coming!

  Next article >


  Do you want to learn React without crawling the documentation (well writ...'
---

By Jérémy Bardon

> This is part of my “React for beginners” series on introducing React, its core features and best practices to follow. More articles are coming!

> [Next article >](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

Do you want to learn React without crawling [the documentation](https://reactjs.org/docs/hello-world.html) (well written by the way)? You clicked on the right article.

We will learn how to run React with a single HTML file and then expose ourselves to a first snippet.

By the end, you will be able to explain these concepts: props, functional component, JSX, and Virtual DOM.

The goal is to make a watch which displays hours and minutes. React offers to architect our code with components. `Let’s create our watch component.

```html
<!-- Skipping all HTML5 boilerplate -->
<script src="https://unpkg.com/react@16.2.0/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16.2.0/umd/react-dom.development.js"></script>

<!-- For JSX support (with babel) -->
<script src="https://unpkg.com/babel-standalone@6.24.2/babel.min.js" charset="utf-8"></script> 

<div id="app"></div> <!-- React mounting point-->

<script type="text/babel">
  class Watch extends React.Component {
    render() {
      return <div>{this.props.hours}:{this.props.minutes}</div>;
    }
  }

  ReactDOM.render(<Watch hours="9" minutes="15"/>, document.getElementById('app'));
</script>
```

Ignore HTML boilerplate and script imports for dependencies (with [unpkg](https://unpkg.com/#/), see [React example](https://raw.githubusercontent.com/reactjs/reactjs.org/master/static/html/single-file-example.html)). The few remaining lines are actually React code.

First, define the Watch component and its template. Then mount React into the DOM and ask to render a watch.

### Inject data into the component

Our watch is quite stupid, it displays the hours and minutes we provided to it.

You can try to play around and change the value for those properties (called **props** in React). It will always display what you asked for even if it’s not numbers.

This kind of React component with only a render function are **functional component.** They have a more concise syntax compared to classes.

```js
const Watch = (props) =>
  <div>{props.hours}:{props.minutes}</div>;

ReactDOM.render(<Watch hours="Hello" minutes="World"/>, document.getElementById('app'));
```

Props are only data passed to a component, generally by a surrounding component. The component uses props for business logic and rendering.

But as soon as props do not belong to the component they are **immutable**. Thus, the component which provided the props is the only piece of code able to update props values.

Using props is pretty straightforward. Create a DOM node with your component name as the tag name. Then give it attributes named after props. Then the props will be available through `this.props` in the component.

### What about unquoted HTML ?

I was sure you will notice the unquoted HTML returned by the `render` function. This code is using JSX language, it’s a shorthand syntax to define HTML template in React components.

```js
// Equivalent to JSX: <Watch hours="9" minutes="15"/>
React.createElement(Watch, {'hours': '9', 'minutes': '15'});
```

Now you may want to avoid JSX to define the component’s template. Actually, JSX looks like [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar).

Take a look at the following snippet which shows both JSX and React syntax to build your opinion.

```js
// Using JS with React.createElement
React.createElement('form', null, 
  React.createElement('div', {'className': 'form-group'},
    React.createElement('label', {'htmlFor': 'email'}, 'Email address'),
    React.createElement('input', {'type': 'email', 'id': 'email', 'className': 'form-control'}),
  ),
  React.createElement('button', {'type': 'submit', 'className': 'btn btn-primary'}, 'Submit')
)

// Using JSX
<form>
  <div className="form-group">
    <label htmlFor="email">Email address</label>
    <input type="email" id="email" className="form-control"/>
  </div>
  <button type="submit" className="btn btn-primary">Submit</button>
</form>
```

### Going further with the Virtual DOM

This last part is more complicated but very interesting. It will help you to understand how React is working under the hood.

Updating elements on a webpage (a node in the DOM tree) involves using the DOM API. It will repaint the page but it can be slow (see [this article](https://hashnode.com/post/the-one-thing-that-no-one-properly-explains-about-react-why-virtual-dom-cisczhfj41bmssp53mvfwmgrq) for why).

Many frameworks such as React and Vue.js get around this problem. They come up with a solution called the Virtual DOM.

```json
{
   "type":"div",
   "props":{ "className":"form-group" },
   "children":[
     {
       "type":"label",
       "props":{ "htmlFor":"email" },
       "children":[ "Email address"]
     },
     {
       "type":"input",
       "props":{ "type":"email", "id":"email", "className":"form-control"},
       "children":[]
     }
  ]
}
```

The idea is simple. Reading and updating the DOM tree is very expensive. So make as few changes as possible and update as few nodes as possible.

Reducing calls to DOM API involves keeping DOM tree representation in memory. Since we are talking about JavaScript frameworks, choosing JSON sounds legitimate.

This approach immediately reflects changes in the Virtual DOM.

Besides, it gathers a few updates to apply later on the Real DOM at once (to avoid performance issues).

Do you remember `React.createElement` ? Actually, this function (called directly or through JSX) creates a new node in the Virtual DOM.

```js
// React.createElement naive implementation (using ES6 features)
function createElement(type, props, ...children) {
  return { type, props, children };
}
```

To apply updates, the Virtual DOM core feature comes into play, the [reconciliation algorithm](https://reactjs.org/docs/reconciliation.html).

Its job is to come up with the most optimized solution to resolve the difference between previous and current Virtual DOM state.

And then apply the new Virtual DOM to the real DOM.

### Further readings

This article goes far on React internal and Virtual DOM explanations. Still, it’s important to know a bit about how a framework works when using it.

If you want to learn how the Virtual DOM works in details, follow my reading recommendations. You can write your own Virtual DOM and [learn about DOM rendering](http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/).

> [**How to write your own Virtual DOM**](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)‌‌

> [_There are two things you need to know to build your own Virtual DOM. You do not even need to dive into React’s source…_](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)

Thank you for reading. Sorry if this is too technical for your first step in React. But I hope now you are aware of what props, functional component, JSX, and Virtual DOM are.

**If you found this article useful, please click on the** ? **button a few times to make others find the article and to show your support! ?**

**Don’t forget to follow me to get notified of my upcoming articles** ?

> This is part of my “React for beginners” series on introducing React, its core features and best practices to follow.

> [Next article >](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

### Check out my [Other](https://medium.com/@jbardon/latest) Articles

#### ➥ JavaScript

* [How to Improve Your JavaScript Skills by Writing Your Own Web Development Framework](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190) ?
* [Common Mistakes to Avoid While Working with Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➥ Tips & tricks

* [Stop Painful JavaScript Debug and Embrace Intellij with Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [How To Reduce Enormous JavaScript Bundles Without Effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)

Originally published at [www.linkedin.com](https://www.linkedin.com/pulse/intro-react-virtual-dom-jeremy-bardon) on February 6, 2018.

