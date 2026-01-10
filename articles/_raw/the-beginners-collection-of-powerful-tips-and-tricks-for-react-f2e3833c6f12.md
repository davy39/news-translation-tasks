---
title: The beginner’s collection of powerful tips and tricks for React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T18:13:15.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s9b85nv7ZKzqxCkg6ps0QA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jérémy Bardon


  This is part of my “React for beginners” series on introducing React, its core features
  and best practices to follow. More articles are coming!

  << Start over | < Previous


  As you can tell from the title of this article, it’s aimed a...'
---

By Jérémy Bardon

> This is part of my “React for beginners” series on introducing React, its core features and best practices to follow. More articles are coming!

> [<< Start over](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [< Previous](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

As you can tell from the title of this article, it’s aimed at beginners.

Actually, I started to learn React a few months ago. Reading the React documentation, open source projects, and Medium articles has helped me a lot.

Without a doubt, I’m not an expert in React. And so I read a lot about this topic. Also, building a small projects has helped me get to know React better. Along the way, I’ve adopted some best practices — and I want to share with you here. So let’s get started.

### Name your components

To figure which component has a bug, it’s important to always give your component a name.

Even more so when you begin to use React Router or third party libraries.

```js
// Avoid thoses notations 
export default () => {};
export default class extends React.Component {};
```

There is a debate about whether to use a default or named import. Note that a **default import** doesn’t ensure that the component’s name is consistent in the project. Besides, [tree-shaking](https://en.wikipedia.org/wiki/Tree_shaking) will be less effective.

#### No matter how you expose your component, name it

You need to define the class name or the variable name (for functional components) that’s hosting the component.

React will actually [infer the component name](https://reactjs.org/docs/react-component.html#displayname) from it in error messages.

```js
export const Component = () => <h1>I'm a component</h1>;
export default Component;

// Define user custom component name
Component.displayName = 'My Component';
```

Here’s my last piece of advice about imports (taken from [here](https://medium.freecodecamp.org/the-most-important-eslint-rule-for-redux-applications-c10f6aeff61d)): If you use ESLint, you should consider setting the following two rules:

```js
"rules": {
    // Check named import exists
    "import/named": 2, 
  
    // Set to "on" in airbnb preset
    "import/prefer-default-export": "off"
}
```

### Prefer functional components

If you have many components whose purpose is only to display data, take advantage of the many ways to [define a React component](https://reactjs.org/docs/components-and-props.html#functional-and-class-components):

```js
class Watch extends React.Component {
  render () {
    return <div>{this.props.hours}:{this.props.minutes}</div>
  }
}

// Equivalent functional component
const Watch = (props) =>
  <div>{props.hours}:{props.minutes}</div>;
```

Both snippets define the same `Watch` component. Yet, the second is way shorter and even drops `this` to access the props in the JSX template.

### Replace divs with fragments

Every component must expose a unique root element as a template. To adhere to this rule, the common fix is to wrap the template in a `div`.

React 16 brings us a new feature called [_Fragments_](https://reactjs.org/docs/fragments.html). Now you can replace those useless `div`s with `React.Fragment`s_._

The output template will be the fragment content without any wrapper.

```js
const Login = () => 
  <div><input name="login"/><input name="password"/></div>;

const Login = () =>
  <React.Fragment><input name="login"/><input name="password"/></React.Fragment>;

const Login = () => // Short-hand syntax
  <><input name="login"/><input name="password"/></>;
```

### Be careful while setting state

As soon as your React app is dynamic, you have to deal with components’ states.

Using states seems pretty straightforward. Initialize the state content in the `constructor` and then call `setState` to update the state_._

For some reason, you may need to use the current **state** or **props** values when calling `setState` to set the next state’s value.

```js
// Very bad pratice: do not use this.state and this.props in setState !
this.setState({ answered: !this.state.answered, answer });

// With quite big states: the tempatation becomes bigger 
// Here keep the current state and add answer property
this.setState({ ...this.state, answer });
```

The issue is that React doesn’t ensure `this.state` and `this.props` have the value you’re expecting. `setState` is asynchronous, because state updates are batch to optimize DOM manipulations (see the details in the [React docs](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous) and this [issue](https://github.com/facebook/react/issues/11527#issuecomment-360199710)).

```js
// Note the () notation around the object which makes the JS engine
// evaluate as an expression and not as the arrow function block
this.setState((prevState, props) 
              => ({ ...prevState, answer }));
```

To prevent corrupted states, you must use `setState` with the function parameter. It provides proper state and props values.

### Binding component functions

There are many ways to bind an element’s events to its component, and some are not recommended.

The first and legitimate solution appears in the [React documentation](https://reactjs.org/docs/handling-events.html):

```js
class DatePicker extends React.Component {
   handleDateSelected({target}){
     // Do stuff
   }
   render() {   
     return <input type="date" onChange={this.handleDateSelected}/>
   }
 }
```

It might disappoint you when you find out that it doesn’t work.

The reason is that when using JSX, `this` value is not bound to the component instance. Here are three alternatives to make it work:

```js
// #1: use an arrow function
<input type="date" onChange={(event) => this.handleDateSelected(event)}/>

// OR #2: bind this to the function in component constructor
constructor () { 
  this.handleDateSelected = this.handleDateSelected.bind(this); 
}

// OR #3: declare the function as a class field (arrow function syntax)
handleDateSelected = ({target}) => {
   // Do stuff
}
```

Using an arrow function in JSX as in the first example seems appealing at first. But don’t do it. In reality, your arrow function will be [created again upon each component rendering](https://reactjs.org/docs/handling-events.html) and it’ll hurt performance.

Also, be careful about the last solution. It uses class fields syntax which is only a [proposal for ECMAScript](https://github.com/tc39/proposal-class-fields).

This means that you have to use [Babel](https://babeljs.io/docs/plugins/transform-class-properties) to [transpile](https://en.wikipedia.org/wiki/Source-to-source_compiler) the code. If the syntax is not finally adopted, your code will break.

### Adopt container pattern (even with Redux)

Last but not the least, the container design pattern. This allows you to follow the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle in the React component.

```js
export class DatePicker extends React.Component {
  state = { currentDate: null };

  handleDateSelected = ({target}) =>
     this.setState({ currentDate: target.value });

  render = () => 
     <input type="date" onChange={this.handleDateSelected}/>
}
```

A single component handles template rendering and user actions in the same place. Let’s use two components instead:

```js
const DatePicker = (props) => 
  <input type="date" onChange={props.handleDateSelected}/>
        
export class DatePickerController extends React.Component { 
  // ... No changes except render function ...
  render = () => 
     <DatePicker handleDateSelected={this.handleDateSelected}/>;
}
```

Here is the trick. `DatePickerContainer` handles user interactions and API calls if necessary. Then it renders a `DatePicker` and supplies props.

Thanks to this pattern, the container component replaces the presentational component. This functional component becomes useless without props.

```js
export const DatePickerContainer = 
 connect(mapStateToProps, mapDispatchToProps)(DatePickerController);
```

In addition, if you use Redux as the state manager for you app, it also plugs well with this pattern.

The `connect` function injects props into the component. In our case, it will feed the controller which will forward those props to the component.

Thus both components will be able to access to Redux data. Here is the full code for the container design pattern (without Redux or class fields syntax).

%[https://codepen.io/jbardon/pen/oNXOWEy]

### Bonus: Fix props drilling

While writing my learning project for React, I noticed a bad pattern that bothered me with props. On each page, I had a main component that used the store and rendered some nested dumb components.

How can deeply nested dumb components access the main component data ? Actually, they can’t — but you can fix it by:

* wrapping the dumb component in a container (it becomes smart)
* or pass down props from the top component

The second solution implies that components between the top component and the dumb component will have to pass down props they don’t need.

```js
const Page = props => <UserDetails fullName="John Doe"/>;
   
const UserDetails = props => 
<section>
    <h1>User details</h1>
    <CustomInput value={props.fullName}/> // <= No need fullName but pass it down
</section>;

const inputStyle = {
   height: '30px',
   width: '200px',
	fontSize: '19px',
   border: 'none',
   borderBottom: '1px solid black'
};
const CustomInput = props => // v Finally use fullName value from Page component
   <input style={inputStyle} type="text" defaultValue={props.value}/>;
```

The React community has named this issue **prop drilling**.

`Page` is the main component that loads the user details. It is necessary to pass this data through `UserDetails` to take it to `CustomInput`.

In this example, the prop only passes through one component which doesn’t need it. But it can be far more if you have reusable components. For example, the Facebook codebase contains a few thousand reusable components!

Don’t worry, I’m going to teach you three ways to fix it. The two first methods appear in the [Context API documentation](https://reactjs.org/docs/context.html#before-you-use-context) : **children prop** and **render prop**.

```js
// #1: Use children prop
const UserDetailsWithChildren = props => 
<section>
    <h1>User details (with children)</h1>
    {props.children /* <= use children */} 
</section>;

// #2: Render prop pattern
const UserDetailsWithRenderProp = props => 
<section>
    <h1>User details (with render prop)</h1>
    {props.renderFullName() /* <= use passed render function */}
</section>;

const Page = () => 
<React.Fragment>
    {/* #1: Children prop */}
    <UserDetailsWithChildren>
        <CustomInput value="John Doe"/> {/* Defines props.children */}
    </UserDetailsWithChildren>
  
    {/* #2: Render prop pattern */}
    {/* Remember: passing arrow functions is a bad pratice, make it a method of Page class instead */}
    <UserDetailsWithRenderProp renderFullName={() => <CustomInput value="John Doe"/>}/>
</React.Fragment>;
```

These solutions are pretty similar. I prefer using children, because it works well within the render method. Note that you can also extend those patterns by providing deeper nested components.

```html
const Page = () =>  
<PageContent>
  <RightSection> 
    <BoxContent>
      <UserDetailsWithChildren>
          <CustomInput value="John Doe"/>
      </UserDetailsWithChildren>
    </BoxContent>
  </RightSection>
</PageContent>
```

The third example uses the experimental context API.

```js
const UserFullNameContext = React.createContext('userFullName');

const Page = () => 
<UserFullNameContext.Provider value="John Doe"> {/* Fill context with value */}
    <UserDetailsWithContext/>
</UserFullNameContext.Provider>;

const UserDetailsWithContext = () => // No props to provide
<section>
    <h1>User details (with context)</h1>
    <UserFullNameContext.Consumer> {/* Get context value */}
        { fullName => <CustomInput value={fullName}/> }
    </UserFullNameContext.Consumer>
</section>;
```

I don’t recommend this method, because it’s using an experimental feature. (And this is why the API recently [changed on a minor version](https://reactjs.org/blog/2018/03/29/react-v-16-3.html).) Also, it forces you to create a global variable to store the context, and your component gets an unclear new dependency (the context can contain anything).

#### That’s it!

Thanks for reading. I hope you learned some interesting tips about React!

**If you found this article useful, please click on the** ? **button a few times to make others find the article and to show your support!** ?

**Don’t forget to follow me to get notified of my upcoming articles** ?

> This is part of my “React for beginners” series on introducing React, its core features and best practices to follow.

> [<< Start over](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [< Previous](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

### Check out my [Other](https://www.freecodecamp.org/news/author/jbardon/) Articles

#### ➥ JavaScript

* [How to Improve Your JavaScript Skills by Writing Your Own Web Development Framework](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190) ?
* [Common Mistakes to Avoid While Working with Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➥ Tips & tricks

* [Stop Painful JavaScript Debug and Embrace Intellij with Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [How To Reduce Enormous JavaScript Bundles Without Effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)

