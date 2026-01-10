---
title: 'React''s new context API: toggle between local and global state'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T02:21:51.000Z'
originalURL: https://freecodecamp.org/news/reacts-new-context-api-how-to-toggle-between-local-and-global-state-c6ace81443d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XlDCO_6ml5lRCbxJZnkzow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Diego Haz

  Consider a component that handles a visibility state and passes it down to its children
  via render props:

  const PopoverContainer = () => (  <VisibilityContainer>    {({ toggle, hidden })
  => (      <div>        <button onClick={toggle}>Po...'
---

By Diego Haz

Consider a component that handles a visibility state and passes it down to its children via [render props](https://reactjs.org/docs/render-props.html):

```
const PopoverContainer = () => (  <VisibilityContainer>    {({ toggle, hidden }) => (      <div>        <button onClick={toggle}>PopoverButton</button&gt;        <div hidden={hidden}>PopoverContent</div>      </div>    )}  </VisibilityContainer>);
```

![Image](https://cdn-media-1.freecodecamp.org/images/bR7Wyd-qYPxK46wEMMsZyBwQuj8ZZc4pHrQy)

What would you think about being able to make that state **global** by just changing a `context` property on the component?

```
const PopoverButton = () => (  <VisibilityContainer context="popover1">    {({ toggle }) => (      <button onClick={toggle}>PopoverButton</button>    )}  </VisibilityContainer>);
```

```
const PopoverContent = () => (  <VisibilityContainer context="popover1">    {({ hidden }) => (      &lt;div hidden={hidden}>PopoverContent</div>    )}  </VisibilityContainer>);
```

That's what we're going to achieve in this article.

### Context and State

First, before talking about **context** and **state** in React, let me give you some **context** on the **state** of this topic (!).

Some months ago I published [reas](https://github.com/diegohaz/reas), an experimental UI toolkit powered by React and [styled-components](https://www.styled-components.com).

Besides components themselves, I wanted to provide helpers to handle their state. The approach I took at that time was to export some [high-order components](https://reactjs.org/docs/higher-order-components.html) (HOCs), such as `withPopoverContainer`, so as to control the visibility state of a `Popover` component. Take a look at this example:

```
import { Popover, withPopoverContainer } from "reas";
```

```
const MyComponent = ({ toggle, visible }) => (  <div>    <button onClick={toggle}>Toggle</button>    <Popover visible={visible}>Popover</Popover>  </div>);
```

```
export default withPopoverContainer(MyComponent);
```

But HOCs have some problems, such as name collision. What if another HOC or a parent component passes its own `toggle` prop to `MyComponent`? Things will certainly break.

Even before that, inspired by [Michael Jackson](https://www.freecodecamp.org/news/reacts-new-context-api-how-to-toggle-between-local-and-global-state-c6ace81443d0/undefined) and his [great talk](https://www.youtube.com/watch?v=BcVAq3YFiuc), the React community started to adopt [render props](https://reactjs.org/docs/render-props.html) over HOCs.

Also, React v16.3.0 introduced a new [context API](https://reactjs.org/docs/context.html), replacing the [old unstable one](https://reactjs.org/docs/legacy-context.html), using render props.

I've learned to look at all that stuff that gets hyped up, especially the stuff brought up by the JavaScript community, with a critical eye. This keeps my mind sane and prevents me from having to refactor my code every single day with cool new libraries.

Finally, I posted a [tweet](https://twitter.com/diegohaz/status/978335493023821824) asking people which they prefer: render props or HOCs. All comments were favorable to render props, which eventually made me turn all HOCs in [reas](https://github.com/diegohaz/reas) into components with render props:

```
import { Popover } from "reas";
```

```
const MyComponent = () => (  <Popover.Container>    {({ toggle, visible }) => (      <div>        <button onClick={toggle}>Toggle&lt;/button&gt;        <Popover visible={visible}>Popover</Popover>      </div>    )}  </Popover.Container>);
```

```
export default MyComponent;
```

`Popover.Container` was a regular React component class with a `toggle` method using `this.setState` to change `this.state.visible`. Simple as that.

It was good and worked pretty well. However, in one of my projects I had a `button` that was supposed to control the `Popover` component placed in a completely different path in the React tree.

I either needed to have some sort of global state manager like [Redux](https://redux.js.org/), or I needed to move `Popover.Container` up in the tree in a common parent and pass the props down until they touched both `button` and `Popover` . But this sounded like a terrible idea.

Also, setting up Redux and rewriting all the logic I already had with `this.setState` into actions and reducers just to have that functionality would be an awful job.

I think this imminent need of shared state is one of the reasons why people [prematurely optimize](http://wiki.c2.com/?PrematureOptimization) their apps. That is, setting up all the libraries they **might** need up front, which includes a global state management library.

React's new context API comes in handy to solve this issue. I wanted to keep using regular React local state and only scale up to global state when needed, without needing to rewrite my state logic. That's why I built [constate](https://github.com/diegohaz/constate).

### Constate

![Image](https://cdn-media-1.freecodecamp.org/images/pvU1j2TKHu1rm1dVouIoSLZpuwYhU8elzO3e)

Let's see how `PopoverContainer` would look with [constate](https://github.com/diegohaz/constate):

```
import React from "react";import { Container } from "constate";
```

```
const PopoverContainer = props => (  <Container    initialState={{ visible: false }}    actions={{      toggle: () => state =>; ({ visible: !state.visible })    }}    {...props}  />);
```

```
export default PopoverContainer;
```

Now we can wrap our component with `PopoverContainer` so as to have access to `visible` and `toggle` members already passed by `Container` to the `children` function as an argument.

Also, note that we are passing all props received from `PopoverContainer` to `Container`. This means that we can compose it to create a new derived state component, such as `AdvancedPopoverContainer`, with new `initialState` and `actions`.

#### Under the hood

If you're like me, and you like to know how things were implemented under the hood, you're probably thinking about how `Container` was implemented. So, let's recreate a simple `Container` component:

```
import React from "react";
```

```
class Container extends React.Component {  state = this.props.initialState;
```

```
  render() {    return this.props.children({      ...this.state,      ...mapStateToActions(...)    });  }}
```

```
export default Container;
```

`[mapStateToActions](https://github.com/diegohaz/constate/blob/93b7b5b469be4521784b51380f49e6589c3e56b9/src/utils.js#L1-L8)` is a utility function that passes state to each member of `actions`. That's what makes it possible to define our `toggle` function like this:

```
const actions = {  toggle: () =&gt; state => ({ visible: !state.visible})};
```

Our goal, however, is to be able to use the same `PopoverContainer` as a global state. With [constate](https://github.com/diegohaz/constate) we just need to pass a `context` prop to `Container`:

```
<PopoverContainer context="popover1">  {({ toggle }) => (    <button onClick={toggle}>PopoverToggle</button>  )}</PopoverContainer>
```

Now, every `Container` with `context="popover1"` will share the same state.

Of course, you're curious about how `Container` handles that `context` prop. So here you go:

```
import React from "react";import Consumer from "./Consumer";
```

```
class Container extends React.Component {  state = this.props.initialState;
```

```
  render() {    if (this.props.context) {      return <Consumer {...this.props} />;    }
```

```
    return this.props.children({      ...this.state,      ...mapStateToActions(...)    });  }}
```

```
export default Container;
```

Ok, I'm sorry. Those four added lines don't tell you much. To create `Consumer`, we need to understand how to deal with the new React Context API.

#### React Context

We can break the new React Context API into three parts: `Context`, `Provider` and `Consumer`.

Let's create the context:

```
import React from "react";
```

```
const Context = React.createContext();
```

```
export default Context;
```

Then, we create our `Provider`, which uses `Context.Provider` and passes `state` and `setState` down:

```
import React from "react";import Context from "./Context";
```

```
class Provider extends React.Component {  handleSetState = fn => {    this.setState(state => ({      state: fn(state.state)    }));  };
```

```
  state = {    state: this.props.initialState,    setState: this.handleSetState  };
```

```
  render() {    return (      <Context.Provider value={this.state}>        {this.props.children}      </Context.Provider>    );  }}
```

```
export default Provider;
```

It can be a little tricky. We can't simply pass `{ state, setState }` as a literal object to `Context.Provider`'s `value` since it would recreate that object on every render. Learn more [here](https://github.com/diegohaz/constate/issues/2).

Finally, our `Consumer` needs to use `Context.Consumer` to access `state` and `setState` passed by `Provider`:

```
import React from "react";import Context from "./Context";
```

```
const Consumer = ({ context, children, actions }) => (  <Context.Consumer>    {({ state, setState }) =&gt; children({      ...state[context],      ...mapContextToActions(...)    })}  </Context.Consumer>);
```

```
export default Consumer;
```

`[mapContextToActions](https://github.com/diegohaz/constate/blob/93b7b5b469be4521784b51380f49e6589c3e56b9/src/Consumer.js#L27-L35)` is similar to `mapStateToActions`. The difference is that the former maps `state[context]` instead of just `state`.

The final step is to wrap our app with `Provider`:

```
import React from "react";import ReactDOM from "react-dom";import Provider from "./Provider";
```

```
const App = () => (  <Provider>    ...  &lt;/Provider>);
```

```
ReactDOM.render(<App />, document.getElementById("root"));
```

Finally, we have rewritten [constate](https://github.com/diegohaz/constate). Now you can use `Container` component to switch between local and global state with ease.

### Conclusion

You might be thinking that starting a project with something like [constate](https://github.com/diegohaz/constate) could also be a premature optimization. And you're probably right. You should stick with `this.setState` without abstractions as long as you can.

However, not all _premature optimizations are the root of all evil_. You should find a good balance between simplicity and scalability. That is, you should pursue simple implementations, specially if you're building small applications. But, if you're planning to grow, you should look for simple implementations that are also easy to scale.

### Thank you for reading this!

If you like it and find it useful, here are some things you can do to show your support:

* Hit the clap ? button on this article a few times (up to 50)
* Give a star ⭐️ on GitHub: [https://github.com/diegohaz/constate](https://github.com/diegohaz/constate)
* Follow me on GitHub: [https://github.com/diegohaz](https://github.com/diegohaz)
* Follow me on Twitter: [https://twitter.com/diegohaz](https://twitter.com/diegohaz)

