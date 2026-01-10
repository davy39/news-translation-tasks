---
title: Evolving Patterns in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-04T17:19:41.000Z'
originalURL: https://freecodecamp.org/news/evolving-patterns-in-react-116140e5fe8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rJr_bOm3mD5V8_C5JaPrsQ.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Alex Moldovan

  Let’s take a closer look at some of the patterns that are emerging in the React
  ecosystem. These patterns improve readability, code clarity, and push your code
  towards composition and reusability.

  I started working with React roughly...'
---

By Alex Moldovan

Let’s take a closer look at some of the patterns that are emerging in the React ecosystem. These patterns improve readability, code clarity, and push your code towards composition and reusability.

I started working with [**React**](https://reactjs.org/) roughly about 3 years ago. At that time, there were no established practices from which to learn in order to leverage its capabilities.

It took about 2 years for the community to settle around a few ideas. We shifted from `React.createClass` to the ES6 `class` and pure functional components. We dropped mixins and [we simplified our APIs](https://reactjs.org/blog/2016/04/07/react-v15.html).

Now as the community is larger than ever, we’re starting to see a couple of nice patterns **evolving**.

In order to understand these patterns you need a basic understanding of the **React** concepts and its ecosystem. Please note, however, that I will not cover them in this article.

So let’s begin!

#### Conditional Render

I’ve seen the following scenario in a lot of projects.

When people think of **React** and **JSX**, they still think in terms of **HTML** and **JavaScript**.

So the natural step is to **separate** the conditional logic from the actual return code.

```javascript
const condition = true;

const App = () => {
  const innerContent = condition ? (
    <div>
      <h2>Show me</h2>
      <p>Description</p>
    </div>
  ) : null;
  
  return (
    <div>
      <h1>This is always visible</h1>
      { innerContent }
    </div>
  );
};
```

This tends to get out of control, with multiple [ternaries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) at the beginning of each `render` function. You constantly have to jump inside the function to understand when a certain element is rendered or not.

As an alternative, try the following pattern, where you benefit from the execution model of the language.

```javascript
const condition = true;

const App = () => (
  <div>
    <h1>This is always visible</h1>
    {
      condition && (
        <div>
          <h2>Show me</h2>
          <p>Description</p>
        </div>
      )
    }
  </div>
);
```

If `condition` is false, the second operand of the `&&` operator is not evaluated. If it is true, the second operand — **or the JSX we wish to render** — is returned.

This allows us to **mix** UI logic with the actual UI elements in a **declarative** way!

Treat JSX like it’s an integral part of your code! After all, it’s just **JavaScript**.

#### Passing Down Props

When your application grows, you have smaller components that act as containers for other components.

As this happens, you need to pass down a good chunk of props through a component. The component doesn’t need them, but its children do.

A good way of bypassing this is to use **props destructuring** together with **JSX spread**, as you can see here:

```javascript
const Details = ( { name, language } ) => (
  <div>
    <p>{ name } works with { language }</p>
  </div>
);

const Layout = ( { title, ...props } ) => (
  <div>
    <h1>{ title }</h1>
    <Details { ...props } />
  </div>
);

const App = () => (
  <Layout 
    title="I'm here to stay"
    language="JavaScript"
    name="Alex"
  />
);
```

So now, you can change the props needed for `Details` and be sure that those props are not referenced in multiple components.

#### Destructuring Props

An app changes over time, and so do your components. A component you wrote two years ago might be stateful, but now it can be transformed into a stateless one. The other way around also happens a lot of times!

Since we talked about props destructuring, here’s a good trick I use to make my life easier on the long run. You can destructure your props in a similar manner for both types of components, as you can see below:

```javascript
const Details = ( { name, language } ) => (
  <div>
    <p>{ name } works with { language }</p>
  </div>
);

class Details extends React.Component {
  render() {
    const { name, language } = this.props;
    return (
      <div>
        <p>{ name } works with { language }</p>
      </div>
    )
  }
}
```

Notice that lines `2–4` and `11–13` are **identical.** Transforming components is much easier using this pattern. Also, you limit the usage of `this` inside the component.

#### Provider Pattern

We looked at an example where props need to be sent down through another component. But what if you have to send it down 15 components?

Enter [React Context](https://reactjs.org/docs/context.html)!

This is not necessarily the most recommended feature of React, but it gets the job done when needed.

It was [recently announced](https://twitter.com/acdlite/status/956390180637650944) that the Context is getting a new API, which implements the **provider pattern** out of the box.

If you are using things like [React Redux](https://github.com/reactjs/react-redux) or [Apollo](https://github.com/apollographql/react-apollo), you might be familiar with the pattern.

Seeing how it works with today’s API will help you understand the new API as well. You can play around with the following sandbox.

%[https://codesandbox.io/s/rww6k3mq94?fontsize=14]

The top level component — called **Provider** — sets some values on the context. The child components — called **Consumers** — will grab those values from the context.

The current context syntax is a bit strange, but the upcoming version is implementing this exact pattern.

#### High Order Components

Let’s talk about reusability. Together with dropping the old `React.createElement()` factory, the React team also dropped the support for [mixins](https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html). They were, at some point, the standard way of composing components through plain object composition.

[High Order Components](https://reactjs.org/docs/higher-order-components.html) — HOCs from now on — went out to fill the need for reusing behavior across multiple components.

A HOC is a function that takes an input component and returns an **enhanced/modified** version of that component. You will find HOCs under different names, but I like to think of them as **decorators**.

If you are using Redux, you will recognize that the `connect` function is a HOC — takes your component and adds a bunch of _props_ to it.

Let’s implement a basic HOC that can add props to existing components.

```javascript
const withProps = ( newProps ) => ( WrappedComponent ) => {
  const ModifiedComponent = ( ownProps ) => ( // the modified version of the component
    <WrappedComponent { ...ownProps } { ...newProps } /> // original props + new props
  );

  return ModifiedComponent;
};

const Details = ( { name, title, language } ) => (
  <div>
    <h1>{ title }</h1>
    <p>{ name } works with { language }</p>
  </div>
);

const newProps = { name: "Alex" }; // this is added by the hoc
const ModifiedDetails = withProps( newProps )( Details ); // hoc is curried for readability

const App = () => (
  <ModifiedDetails 
    title="I'm here to stay"
    language="JavaScript"
  />
);
```

If you like functional programming, you will love working with high order components. [Recompose](https://github.com/acdlite/recompose) is a great package that gives you all these nice utility HOCs like `**withPro**ps`, `**withContext**`, `**lifecycle**`, and so on.

Let’s have a look at a very useful example of **reusing functionality**.

```javascript
function withAuthentication(WrappedComponent) {
  const ModifiedComponent = (props) => {
    if (!props.isAuthenticated) {
      return <Redirect to="/login" />;
    }

    return (<WrappedComponent { ...props } />);
  };

  const mapStateToProps = (state) => ({
    isAuthenticated: state.session.isAuthenticated
  });

  return connect(mapStateToProps)(ModifiedComponent);
}
```

You can use `withAuthentication` when you want to render sensitive content inside a route. That content will only be available to logged-in users.

This is a [cross-cutting concern](https://en.wikipedia.org/wiki/Cross-cutting_concern) of your application implemented in a single place and reusable across the entire app.

However, there is a downside to HOCs. Each HOC will introduce an additional React Component in your DOM/vDOM structure. This can lead to potential performance problems as your application scales.

Some additional problems with HOCs are summarized in [this great article](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) by [Michael Jackson](https://twitter.com/mjackson). He advocates replacing HOCs with the pattern we’ll be talking about next.

#### Render Props

While it is true that **render props** and **HOCs** are interchangeable, I don’t favor one over another. Both patterns are used to improve reusability and code clarity.

The idea is that you **yield** the control of your render function to another component that then passes you back the control through a function prop.

Some people prefer to use a **dynamic prop** for this, some just use `**this.props.children**`.

I know, it’s still very confusing, but let’s see a simple example.

```javascript
class ScrollPosition extends React.Component {
  constructor( ) {
    super( );
    this.state = { position: 0 };
    this.updatePosition = this.updatePosition.bind(this);
  }
  
  componentDidMount( ) {
    window.addEventListener( "scroll", this.updatePosition );
  }

  updatePosition( ) {
    this.setState( { position: window.pageYOffset } )
  }

  render( ) {
    return this.props.children( this.state.position )
  }
}

const App = () => (
  <div>
    <ScrollPosition>
      { ( position ) => (
        <div>
          <h1>Hello World</h1>
          <p>You are at { position }</p>
        </div>
      ) }
    </ScrollPosition>
  </div>
);
```

Here we are using `children` as the render prop. Inside the `_<ScrollPositi_`on> component we will send a function which receive`s the po`sition as a parameter.

Render props can be used in situations where you need some reusable logic **inside** the component and you don’t want to wrap your component in a HOC.

[React-Motion](https://github.com/chenglou/react-motion) is one of the libraries that offer some great examples of using render props.

Finally, let’s look at how we can integrate **async** flows with render props. Here’s a nice example of creating a reusable `Fetch` component.

I’m sharing a sandbox link so you can play with it and see the results.

%[https://codesandbox.io/s/myv3nywvp?fontsize=14]

You can have **multiple** render props for the same component. With this pattern, you have endless possibilities of composing and reusing functionality.

What patterns do you use? Which of them would fit in this article? Drop me a message bellow or write your thoughts on [Twitter](https://twitter.com/alexnmoldovan).

If you found this article useful, help me share it with the community!

